API_CreateTable
***************

`Quick Base Documentation: API_CreateTable <https://help.quickbase.com/api-guide/create_table.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_CreateTable', {
        'tname': 'Widgets',
        'pnoun': 'Widgets',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_CreateTable'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('newdbid', 'tabledbid')
    ])
