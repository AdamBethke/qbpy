API_AddField
************

`Quick Base Documentation: API_AddField <https://help.quickbase.com/api-guide/#add_field.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddField', {
        'dbid': 'tabledbid',
        'label': 'Sample Field',
        'type': 'checkbox',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddField'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('fid', 7),
        ('label', 'Sample Field')
    ])
