API_AddRecord
*************

`Quick Base Documentation: API_AddRecord <https://help.quickbase.com/api-guide/#add_record.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddRecord', {
        'dbid': 'tabledbid',
        'fields': {
            '6': 1,
            '7': 'Choice A',
        },
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddRecord'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('rid', 1),
        ('update_id', 1544134119254)
    ])
