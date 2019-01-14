API_DeleteRecord
****************

`Quick Base Documentation: API_DeleteRecord <https://help.quickbase.com/api-guide/#delete_record.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_DeleteRecord', {
        'dbid': 'tabledbid',
        'rid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_DeleteRecord'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('rid', 1)
    ])
