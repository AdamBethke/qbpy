API_GetNumRecords
*****************

`Quick Base Documentation: API_GetNumRecords <https://help.quickbase.com/api-guide/#getnumrecords.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetNumRecords', {
        'dbid': 'tabledbid',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetNumRecords'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('num_records', 0)
    ])
