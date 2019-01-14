API_GrantedDBs
**************

`Quick Base Documentation: API_GrantedDBs <https://help.quickbase.com/api-guide/#granteddbs.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GrantedDBs')

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GrantedDBs'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('databases', OrderedDict([
            ('dbinfo', [
                OrderedDict([
                    ('dbname', 'Application'),
                    ('dbid', 'appdbid')
                ]),
                OrderedDict([
                    ('dbname', 'Application: TableName'),
                    ('dbid', 'tabledbid')
                ]),
                OrderedDict([
                    ('dbname', 'Application: TableName'),
                    ('dbid', 'tabledbid')
                ])
            ])
        ]))
    ])
