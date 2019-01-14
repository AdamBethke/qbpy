API_SetKeyField
***************

`Quick Base Documentation: API_SetKeyField <https://help.quickbase.com/api-guide/setkeyfield.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_SetKeyField', {
        'dbid': 'tabledbid',
        'fid': 6,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_SetKeyField'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
