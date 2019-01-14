API_GetDBVar
************

`Quick Base Documentation: API_GetDBVar <https://help.quickbase.com/api-guide/#getdbvar.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetDBVar', {
        'varname': 'testvar',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetDBVar'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('value', 1)
    ])
