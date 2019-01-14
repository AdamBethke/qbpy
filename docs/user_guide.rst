==========
User Guide
==========

Installation
------------

At this point, the easiest way to install qbpy is from its
`source <https://gitlab.com/abethke/qbpy>`_:



Initialization
--------------

You initialize a qbpy connection object by creating an instance of `QuickBase`:

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase({
        'realm': '',
        'dbid': '',
        'apptoken': '',
        'usertoken': ''
    })

When initializing the instance, you provide a set of globally relevant parameters.
It is recommended to include at least the realm and application DBID (dbid). In
many cases, it is also useful to provide an apptoken and usertoken. Additionally,
the dictionary can include `optional parameters <https://help.quickbase.com/api-guide/index.html#optional_parameters.html%3FTocPath%3DQuick%2520Base%2520API%2520Call%2520Reference%7C_____2>`_.
Parameters included when intializing the connection object are provided by default
in all API calls made by the connection object.

Authentication
++++++++++++++

In order to use qbpy, you must use either **ticket** or **usertoken** authentication.
If you choose to use token-based authentication, you simply add the 'usertoken' to the
dictionary of parameters provided, either when instantiating a connection object,
or when making a specific API call. :ref:`ticket_authentication` describes the
recommended workflow for using ticket-based authentication.

.. note:: When a connection has an associated ticket, the ticket is used in lieu of the usertoken.

Working with the Quick Base API
-------------------------------

Calls to a valid Quick Base API method can be made using `api` method of the
connection instance (e.g. `qb.api`). The `api` method has two parameters:

  - `method`: The name of the Quick Base API method to call
  - `parameters`: A dictionary of parameters, passed to the API call

Methods
+++++++

This section provides an example of how to format each API call, as well as a
sample response. For convenience, a link to Quick Base's documentation for each
call is also provided.

.. include:: ./methods/api_addfield.rst
.. include:: ./methods/api_addgrouptorole.rst
.. include:: ./methods/api_addrecord.rst
.. include:: ./methods/api_addreplacedbpage.rst
.. include:: ./methods/api_addsubgroup.rst
.. include:: ./methods/api_addusertogroup.rst
.. include:: ./methods/api_addusertorole.rst
.. include:: ./methods/api_authenticate.rst
.. include:: ./methods/api_changegroupinfo.rst
.. include:: ./methods/api_changemanager.rst
.. include:: ./methods/api_changerecordowner.rst
.. include:: ./methods/api_changeuserrole.rst
.. include:: ./methods/api_clonedatabase.rst
.. include:: ./methods/api_copygroup.rst
.. include:: ./methods/api_copymasterdetail.rst
.. include:: ./methods/api_createdatabase.rst
.. include:: ./methods/api_creategroup.rst
.. include:: ./methods/api_createtable.rst
.. include:: ./methods/api_deletedatabase.rst
.. include:: ./methods/api_deletefield.rst
.. include:: ./methods/api_deletegroup.rst
.. include:: ./methods/api_deleterecord.rst
.. include:: ./methods/api_doquery.rst
.. include:: ./methods/api_doquerycount.rst
.. include:: ./methods/api_editrecord.rst
.. include:: ./methods/api_fieldaddchoices.rst
.. include:: ./methods/api_fieldremovechoices.rst
.. include:: ./methods/api_finddbbyname.rst
.. include:: ./methods/api_genaddrecordform.rst
.. include:: ./methods/api_genresultstable.rst
.. include:: ./methods/api_getancestorinfo.rst
.. include:: ./methods/api_getappdtminfo.rst
.. include:: ./methods/api_getdbinfo.rst
.. include:: ./methods/api_getdbpage.rst
.. include:: ./methods/api_getdbvar.rst
.. include:: ./methods/api_getfieldproperties.rst
.. include:: ./methods/api_getgrouprole.rst
.. include:: ./methods/api_getnumrecords.rst
.. include:: ./methods/api_getrecordashtml.rst
.. include:: ./methods/api_getrecordinfo.rst
.. include:: ./methods/api_getroleinfo.rst
.. include:: ./methods/api_getschema.rst
.. include:: ./methods/api_getuserinfo.rst
.. include:: ./methods/api_getuserrole.rst
.. include:: ./methods/api_getusersingroup.rst
.. include:: ./methods/api_granteddbsforgroup.rst
.. include:: ./methods/api_granteddbs.rst
.. include:: ./methods/api_grantedgroups.rst
.. include:: ./methods/api_importfromcsv.rst
.. include:: ./methods/api_provisionuser.rst
.. include:: ./methods/api_purgerecords.rst
.. include:: ./methods/api_removegroupfromrole.rst
.. include:: ./methods/api_removesubgroup.rst
.. include:: ./methods/api_removeuserfromgroup.rst
.. include:: ./methods/api_removeuserfromrole.rst
.. include:: ./methods/api_renameapp.rst
.. include:: ./methods/api_runimport.rst
.. include:: ./methods/api_setdbvar.rst
.. include:: ./methods/api_sendinvitation.rst
.. include:: ./methods/api_setfieldproperties.rst
.. include:: ./methods/api_setkeyfield.rst
.. include:: ./methods/api_uploadfile.rst
.. include:: ./methods/api_userroles.rst
.. include:: ./methods/api_webhooksactivate.rst
.. include:: ./methods/api_webhookscopy.rst
.. include:: ./methods/api_webhookscreate.rst
.. include:: ./methods/api_webhooksdelete.rst
.. include:: ./methods/api_webhooksdeactivate.rst
.. include:: ./methods/api_webhooksedit.rst


Response Formatting
+++++++++++++++++++

In addition to the two required parameters, the `api` method has a `response_formatter`
parameter, which allows you to redefine the way the XML response from Quick Base
is parsed by qbpy. For most methods, qbpy leaves the response as-is after
converting it to a dictionary. In a few cases, the default response is modified
to make it easier to work with the response.

If you have a custom use-case, you can write a custom formatter which will
reshape the response into a new dictionary for your use.

Formatters **are functions** which take the initial dictionary returned by
converting the XML response to a dictionary, do something to the dictionary
to modify its structure or internals, and then return that dictionary.

For example, this is the default formatter for API_DoQuery:

.. code:: python

    def response_formatter_api_doquery(res):
        """Convert API_DoQuery response to usable format."""
        for record in res['table']['records']['record']:
            for column in record['f']:
                if 'value' in column:
                    record[column['id']] = column['value']
            del record['f']
        return res

Macros
------

In addition to direct calls to API methods, qbpy provides a set of macros which
facilitate actions which require multiple API calls, or are not available in the
API (e.g. file downloads).

.. _ticket_authentication:

Ticket Authentication
+++++++++++++++++++++

The `authenticate` macro facilitates ticket authentication. The method takes
three parameters:

  - `username`: the username of the account to authenticate
  - `password`: the user's password
  - `hours`: the number of hours for which the ticket should be valid

This macro makes calling API_Authenticate easier, automating the call to
API_Authenticate, receives the ticket response, and updates the default parameters
used by the connection object to include the ticket.

For example, API_GetAncestorInfo cannot use a usertoken, and requires a ticket.
You could make a call to API_Authenticate, and collect the ticket:

.. code:: python

    qb.api('API_Authenticate' {
        'username': 'username'
        'password': 'secret'
    })
    authenticationticket = qb.response.get('ticket')
    qb.api('API_GetAncestorInfo', {
        'ticket': authenticationticket,
    })

While that works, it's not simple. The authenticate macro allows you to do something
like this instead:

.. code:: python

    qb.authenticate(username='username', password='secret')
    qb.api('API_GetAncestorInfo')

The authenticate macro also supports outbound method chaining, so you can actually
simplify the call one step further:

.. code:: python

    qb.authenticate(username='username', password='secret').api('API_GetAncestorInfo')

Download Files
++++++++++++++

The `download_files` macro facilitates the selection of records in a Quick Base
table, and the download of files in a file attachment field. The method takes two
parameters:

  - `file_fid`: the FID of the file attachment field to be downloaded
  - `parameters`: the query parameters (`API_DoQuery`) used to find the row(s)
    with files to be downloaded

This allows the programmatic download of files, something Quick Base has indicated
it does not and does not intend to ever support via the API (Support Case #555749).
Additionally, the macro stores the response from downloading files the same way
it stores a response from a call to `API_DoQuery`. This allows you to both
download a set of files, and have access to a listing of the files downloaded
from the same API call.

An example of the download functionality:

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase(...)
    qb.download_files(
        file_fid=6,
        parameters={...}
    )

.. note::

  Because it needs to perform an API_DoQuery call, `download_files` uses API calls,
  despite the fact that the individual file downloads are **not** a Quick Base
  API method. You should factor this in when considering your API usage limits.

JSON Response
+++++++++++++

The `json` macro facilitates the conversion of a response to a JSON object.
The macro can be called either on a Quick Base connection, in which case it
converts the last response to JSON. The macro also supports method-chaining,
and can be appended to an API call.

These examples are equivalent:

**Last Response**:

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase(...)
    qb.api('API_DoQuery', {'key': 'value'})
    qb.json()

**Method-Chaining**

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase(...)
    qb.api('API_DoQuery', {'key': 'value'}).json()

Pandas Dataframe
++++++++++++++++

The `pandas` macro facilitates the conversion of a response to a pandas DataFrame.
The macro can be called either on a Quick Base connection, in which case it
converts the last response to JSON. The macro also supports method-chaining,
and can be appended to an API call. Calling the macro returns a pandas DataFrame.

These examples are equivalent:

**Last Response**:

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase(...)
    qb.api('API_DoQuery', {'key': 'value'})
    qb.pandas()

**Method-Chaining**

.. code:: python

    from qbpy import QuickBase
    qb = QuickBase(...)
    qb.api('API_DoQuery', {'key': 'value'}).pandas()

.. note::

    The `pandas` macro includes a `dataframe_formatter` paramter, which provides
    a similar ability to rework a dictionary into a desired format that the
    `response_formatter` parameter does for the `api` method. The only difference
    is that `dataframe_formatter` takes a dictionary and returns a pandas DataFrame.

    The functionalities are kept separate to allow the handling strategy to differ
    between the parsing of the response and the presentation of a dataframe.
