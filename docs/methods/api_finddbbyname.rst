API_FindDBByName
****************

`Quick Base Documentation: API_FindDBByName <https://help.quickbase.com/api-guide/find_db_by_name.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_FindDBByName', {
        'ticket': 'authenticationticket',
        'dbname': 'App Name',
        'parentsonly': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_FindDBByName'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('dbid', 'appdbid'),
        ('dbname', 'App Name')
    ])
