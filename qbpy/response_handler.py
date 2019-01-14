"""Utilities to handle responses from the Quick Base API"""
import re
from xmltodict import parse
from .configuration import CONFIGURATION
from .exceptions import QuickBaseException, RequestException


class _ResponseHandler:
    """
    Parse responses provided by the Quick Base API.

    Converts the responseults of a Quick Base API call from an HTTPS response
        into a more legible dictionary output which can be used to work with the
        responses in a more convenient manner.

    :param action: The Quick Base API method being called
    :type action: string

    :param response: A response to a Quick Base API call
    :type response: requests.response; HTTPS response object

    :param formatter:  A function which modifies the response dictionary,
        defaults to None, which uses the built in formatter. Providing
        a formatter allows you to change how the response is returned
    :type formatter: function
    """
    def __init__(self, action, response, response_formatter=None):
        self._response = response
        self.response_type = CONFIGURATION[action]['response_type']

        if self.response.status_code != 200:
            raise RequestException(response.status_code)

        if self.response_type == 'url':
            self.response = self._return_url(response)

        else:
            self._response = self._convert_xml_to_dict(response)
            if self.response['errcode'] != 0:
                raise QuickBaseException(self.error)
            self.response = self._formatter(response_formatter)

    def __repr__(self):
        return 'ResponseHandler ({0}) at {1}'.format(self.action, hex(id(self)))

    @property
    def response(self):
        """Get response."""
        return self._response

    @response.setter
    def response(self, response):
        """Set response."""
        self._response = response

    @property
    def action(self):
        """Get action executed by the API."""
        return self.response['action']

    @property
    def error(self):
        """Get error details from API response."""
        return {
            'errcode': self.response['errcode'],
            'errtext': self.response['errtext'],
            'errdetail': self.response.get('errdetail')
        }

    @staticmethod
    def _return_url(response):
        """
        Returns response as URL to resource.

        :param response: A response to a Quick Base API call
        :type response: requests.response; HTTPS response object

        :return: A URL redirect to the resource
        :rtype: string
        """
        return response.url

    @staticmethod
    def _convert_xml_to_dict(response):
        """
        Converts xml to dictionary.

        Takes a response to an API call, and parses it into a dictionary.
        response parsing includes responseolution for Quick Base non-adherence to
        XML standard, as well as error handling for invalid requests.

        :param response: A response to a Quick Base API call
        :type response: requests.response; HTTPS response object

        :return: A dictionary containing the parsed response from the Quick Base API
        :rtype: dictionary
        """
        # handle Quick Base XML non-compliance (support case #480141)
        response = re.sub(r'<[Bb][Rr]\/>', '', response.text)

        def postprocessor(path, key, value):
            """
            Convert xml integer values to ints.

            Postprocessor for xmltodict which converts integer values from their
            text representation to integers.

            .. seealso: http://omz-software.com/pythonista/docs/ios/xmltodict.html
            """
            try:
                return key, int(value)
            except (ValueError, TypeError):
                return key, value

        # parse XML to dict
        response = parse(response, attr_prefix='', cdata_key='value', postprocessor=postprocessor)

        try:
            return response['qdbapi']
        except KeyError:
            raise QuickBaseException({
                'errcode': -1,
                'errtext': 'Incorrectly formatted response',
                'errdetail': 'XML root is not qdbapi',
            })

    def _formatter(self, response_formatter):
        """
        Format parsed xml response.

        Format the parsed response by converting the originally returned dictionary
        and reformatting it to the desired format. This allows the end user to
        reconfigure the API response to facilitate custom data structuring.

        :param response_formatter: A function that takes a response dictionary as
            its only argument, and returns a response dictionary
        :type response_formatter: function

        :return: A response dictionary, the return from the response_formatter function
        :rtype: dictionary
        """
        if not response_formatter:
            response_formatter = CONFIGURATION[self.action]['response_formatter']
        return response_formatter(self.response)
