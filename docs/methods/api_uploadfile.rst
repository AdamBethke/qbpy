API_UploadFile
**************

`Quick Base Documentation: API_UploadFile <https://help.quickbase.com/api-guide/uploadfile.html>`_

API_UploadFile is an interesting edge case, where the documentation in Quick
Base sends you to the documentation for API_AddRecord. To handle for this,
we add a custom parameter, 'action', which tells qbpy how to direct the file.
API_AddRecord adds a new record with a file attachment, while API_EditRecord
updates an existing record. In cases where you're editing an existing record,
you must provide either the rid or key parameter to tell Quick Base which record
receives the file.

The other interesting component to uploading a file takes two components - a
filename, and a file. To facilitate working with the API, we provide these
as a dictionary within the parameters dictionary attached to the field's fid.
In the examples below, we're uploading a file called todos.md to the field
with fid 12. When providing the file, you must provide a bytes-like object.
qbpy will base64 encode the file for you, but you need to make sure it has
a bytes-like object to work with.

Request
^^^^^^^

Add New Record
@@@@@@@@@@@@@@

.. code:: python

    qb.api('API_UploadFile', {
        'action': 'API_AddRecord',
        'dbid': 'tabledbid',
        'field': {
            '6': 'Choice A',
            '7': 'Choice A',
            '12': {
                'filename': 'todos.md',
                'file': open('todos.md', 'rb').read(), # a bytes object
            },
        },
    })

Edit Existing Record
@@@@@@@@@@@@@@@@@@@@

.. code:: python

    qb.api('API_UploadFile', {
        'action': 'API_EditRecord',
        'dbid': 'tabledbid',
        'rid': 10, # or key, for non-default keys
        'field': {
            '6': 'Choice A',
            '7': 'Choice A',
            '12': {
                'filename': 'todos.md',
                'file': open('todos.md', 'rb').read(), # a bytes object
            },
        },
    })

Response
^^^^^^^^

Responses will look like the formats for ``API_AddRecord`` or ``API_EditRecord``,
depending on which upload action you take.
