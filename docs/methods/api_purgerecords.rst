API_PurgeRecords
****************

`Quick Base Documentation: API_PurgeRecords <https://help.quickbase.com/api-guide/#purgerecords.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_PurgeRecords', {
        'dbid': 'tabledbid',
        'qid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_PurgeRecords'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('num_records_deleted', 1)
    ])
