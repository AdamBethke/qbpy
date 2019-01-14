API_CloneDatabase
*****************

`Quick Base Documentation: API_CloneDatabase <https://help.quickbase.com/api-guide/clone_database.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_CloneDatabase', {
        'newdbname': 'Cloned Database',
        'newdbdesc': 'Description of cloned database',
        'keepdata': 0,
        'usersandroles': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_CloneDatabase'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('newdbid', 'appdbid')
    ])
