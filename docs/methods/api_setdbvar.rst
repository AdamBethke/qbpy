API_SetDBVar
************

`Quick Base Documentation: API_SetDBVar <https://help.quickbase.com/api-guide/#setdbvar.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_SetDBVar', {
        'varname': 'variable',
        'value': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_SetDBVar'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
