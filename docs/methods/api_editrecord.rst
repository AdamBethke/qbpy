API_EditRecord
**************

`Quick Base Documentation: API_EditRecord <https://help.quickbase.com/api-guide/edit_record.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_EditRecord', {
        'dbid': 'tabledbid',
        'rid': 1,
        'field': {
            '6': 'newvalue',
            '7': 'Choice A',
        },
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_EditRecord'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('rid', 1),
        ('num_fields_changed', 2),
        ('update_id', 1546356736930)
    ])
