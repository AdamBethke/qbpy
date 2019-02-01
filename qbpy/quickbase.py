import json
import os
import requests

from .response_handler import _ResponseHandler
from .request_handler import _RequestHandler
from .configuration import CONFIGURATION
from .exceptions import QuickBaseException


class QuickBase:
    """
    Create a Quick Base connection object.

    A Quick Base connection object is initialized with a set of default parameters,
    which can be added to, or overridden by the user. The parameters created when
    initializing the connection are then made available to API calls made using
    the ``api`` method.

    :param parameters: A dictionary containing user-specified parameters which
        are added to (and override) default parameters
    :type parameters: dictionary

    .. note:: qbpy does **not** create a `PEP 249 <https://www.python.org/dev/peps/pep-0249/>`_
        complaint database connection. We use the "connection object" idiom to
        describe an instance of the class because it functions in a similar way,
        containing common parameters like `realm`, `domain`, `apptoken` and
        `usertoken`, and making them available to API calls, the same way a PEP
        249 connection can be used to create cursors, which are then able to
        execute queries against a database.
    """
    default_parameters = {
        'realm': 'www',
        'dbid': '',
        'domain': 'quickbase.com',
        'msInUTC': True,
        'includeRids': True,
        'returnPercentage': False,
        'fmt': 'structured',
        'encoding': 'UTF-8',
        'directory': os.getcwd(),
        'skipfirst': 1,
        'clist_output': None,
    }


    def __init__(self, parameters):
        self._parameters = QuickBase.default_parameters
        self._last_action = None
        self._last_response = None

        self.parameters = parameters


    def __repr__(self):
        return 'QuickBase Connection ({realm}) at {hex}'.format(
            realm=self.parameters.get('realm'),
            hex=hex(id(self)))


    @property
    def action(self):
        """
        The last API method called by the connection.

        :return: The last API method called by the connection
        :rtype: string
        """
        return self._last_action

    @action.setter
    def action(self, action):
        self._last_action = action


    @property
    def parameters(self):
        """
        The parameters currently set for a Quick Base connection.

        :return: A dictionary of connection-global parameters.
        :rtype: dictionary
        """
        return self._parameters


    @parameters.setter
    def parameters(self, parameters):
        self._parameters = dict(self._parameters, **(parameters or {}))


    @property
    def response(self):
        """
        The last response returned from Quick Base, formatted as a dictionary.

        :return: The last response returned by the Quick Base API, parsed from
            an HTTPS response and converted into a dictionary for easy use.
        :rtype: dictionary
        """
        return self._last_response

    @response.setter
    def response(self, response):
        self._last_response = response


    def api(self, action, parameters=None, response_formatter=None):
        """
        Build and send an API call.

        The ``api`` method handles the construction, sending, receiving, and
        formatting of Quick Base API calls. The method uses the connection's
        parameters as the default, and adds and overides those parameters with
        parameters specific to the API call.

        Once the API call has been built and sent, the method receives and
        formats the response so that it is easy to work with in Python, converting
        it to a dictionary. For some methods like `API_DoQuery` and `API_UserRoles`,
        the method provides a default formatter which cleans up some layers of
        XML which Quick Base includes. The defaults can be overridden by supplying
        a function which takes a response and returns the modified response.

        :param action: API method, defined by Quick Base
        :type action: string

        :param parameters: A dictionary with parameters which are specific to the
            API call; these parameters add / update parameters provided by the
            connection
        :type parameters: dictionary

        :param response_formatter: A function which takes the default response
            from Quick Base and modifies it to provide a custom response return
        :type response_formatter: function

        :return: The response from the API call, formatted as a dictionary; where
            a `response_formatter` is provided, the response is modified before
            the response is returned
        :rtype: dictionary
        """
        if action in CONFIGURATION:

            method_parameters = dict(self.parameters, **(parameters or {}))
            if {'ticket', 'usertoken'} <= set(method_parameters):
                method_parameters.pop('usertoken', None)

            self.response = _ResponseHandler(
                action=action,
                response=_RequestHandler(action, method_parameters).send_request(),
                response_formatter=response_formatter
            ).response
            self.action = action
            return self

        else:
            raise QuickBaseException({
                'errcode': -3,
                'errtext': 'Method not implemented',
                'errdetail': '{} is not implemented'.format(action),
            })


    def authenticate(self, username, password, hours=12):
        """
        Authenticate to Quick Base using the API_Authenticate method.

        This method abstracts the process of making a call to API_Authenticate,
        and then adding the resulting ticket to the set of parameters used in
        API calls. This makes it easier to get, store, and continue to use
        ticket-based authentication.

        :param username: The username, typically an email address
        :type username: str

        :param password: The user's password
        :type password: str

        :param hours: The number of hours for which the ticket will be valid
        :type hours: integer
        """
        authentication = self.api('API_Authenticate', {
            'username': username,
            'password': password,
            'hours': hours,
        })
        self.parameters['ticket'] = authentication.response.get('ticket')
        return self


    def download_files(self, file_fid, parameters=None):
        """
        Download file(s) from table records.

        This method abstracts a process which is otherwise a compound set of
        API calls. It executes a `API_DoQuery` to get a list of records which
        have file attachments, and then systematically downloads each of the files
        that are returned by the `API_DoQuery`.

        Once the execution is complete, it returns the response from the
        `API_DoQuery` call, making the list of files downloaded visible as
        the response.

        :param file_fid: The field id containing file(s) to download
        :type file_fid: integer

        :param parameters: A dictionary with parameters which are specific to
            the ``API_DoQuery`` used to get the list of files
        :type parameters: dictionary
        """
        base_file_url = 'https://{realm}.{domain}/up/{dbid}/a/r{rid}/e{fid}/v0'
        directory = self.parameters['directory']
        download_parameters = dict(self.parameters, **(parameters or {}))
        tokens = {
            key: download_parameters[key]
            for key in ['apptoken', 'ticket', 'usertoken']
            if key in download_parameters
        }

        doquery = self.api('API_DoQuery', parameters) # identify rows to download

        # generate a list of files
        files = []
        for row in doquery.response['table']['records']['record']:
            files.append(
                (
                    base_file_url.format(
                        realm=download_parameters['realm'],
                        domain=download_parameters['domain'],
                        dbid=download_parameters['dbid'],
                        rid=row['rid'],
                        fid=file_fid
                    ),
                    str(row['rid']) + '-' + row[file_fid]
                )
            )

        # download files
        for file in files:
            download = requests.get(file[0], tokens)
            with open(os.path.join(directory, file[1]), 'wb') as quickbase_download:
                for chunk in download.iter_content(1024):
                    quickbase_download.write(chunk)

        return doquery


    def json(self, indent=4):
        """
        Convert the last response from a dictionary to its JSON representation.

        :param indent: Indent size for formatted JSON
        :type indent: integer

        :return: The response as JSON.
        :rtype: json

        .. seealso:: https://docs.python.org/3.6/library/json.html#basic-usage
        """
        return json.dumps(self.response, indent=indent)


    def pandas(self, dataframe_formatter=None):
        """
        Convert the last response from a dictionary to a `pandas` DataFrame.

        Converts the response from the API call into a pandas DataFrame. The
        conversion is dictated by the response structure. Currently, formatting
        is only implemented for `API_DoQuery` and `API_UserRoles`, and
        returns an empty dataframe for all other API calls.

        The defaults can be overridden by supplying a function which takes a
        response and returns a DataFrame.

        :param dataframe_formatter: A function manipulating the connection's
            latest response and returning a DataFrame; where Quick Base has a
            deep XML structure, a default formatter is provided
        :type dataframe_formatter: function

        :return: A dataframe containing the contents of the last response
        :rtype: DataFrame

        .. seealso:: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
        """
        if not dataframe_formatter:
            dataframe_formatter = CONFIGURATION[self.action]['dataframe_formatter']
        return dataframe_formatter(self.response)
