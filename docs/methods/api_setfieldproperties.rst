API_SetFieldProperties
**********************

`Quick Base Documentation: API_SetFieldProperties <https://help.quickbase.com/api-guide/setfieldproperties.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_SetFieldProperties', {
        'dbid': 'tabledbid',
        'fid': 11,
        'blank_is_zero': 0,
        'does_total': 1,
        'decimal_places': 3,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_SetFieldProperties'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('fid', 11),
        ('fname', 'num')
    ])
