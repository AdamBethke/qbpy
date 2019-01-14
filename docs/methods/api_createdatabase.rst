API_CreateDatabase
******************

`Quick Base Documentation: API_CreateDatabase <https://help.quickbase.com/api-guide/create_database.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_CreateDatabase', {
        'ticket': 'authenticationticket',
        'dbname': 'New Database',
        'dbdesc': 'New database created by API',
        'createapptoken': 1,
    })


Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_CreateDatabase'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('dbid', 'appdbid'),
        ('appdbid', 'appdbid')
    ])
