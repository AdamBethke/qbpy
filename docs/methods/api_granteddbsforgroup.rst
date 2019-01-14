API_GrantedDBsForGroup
**********************

`Quick Base Documentation: API_GrantedDBsForGroup <https://help.quickbase.com/api-guide/#API_GrantedDBsForGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GrantedDBsForGroup', {
        'gid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GrantedDBsForGroup'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('databases', OrderedDict([
            ('dbinfo', [
                OrderedDict([
                    ('dbname', 'Application'),
                    ('dbid', 'appdbid')
                ]),
                OrderedDict([
                    ('dbname', 'TableName'),
                    ('dbid', 'tabledbid')
                ]),

                OrderedDict([
                    ('dbname', 'TableName'),
                    ('dbid', 'tabledbid')
                ])
            ])
        ]))
    ])
