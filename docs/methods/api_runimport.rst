API_RunImport
*************

`Quick Base Documentation: API_RunImport <https://help.quickbase.com/api-guide/runimport.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RunImport', {
        'dbid': 'tabledbid',
        'id': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RunImport'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('import_status', '3 new records were created.')
    ])
