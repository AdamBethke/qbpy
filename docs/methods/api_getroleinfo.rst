API_GetRoleInfo
***************

`Quick Base Documentation: API_GetRoleInfo <https://help.quickbase.com/api-guide/#getroleinfo.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetRoleInfo')

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetRoleInfo'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('roles', OrderedDict([
            ('role', [
                OrderedDict([
                    ('id', 10),
                    ('name', 'Viewer'),
                    ('access', OrderedDict([
                        ('id', 3),
                        ('value', 'Basic Access')
                    ]))
                ]),
                OrderedDict([
                    ('id', 11),
                    ('name', 'Participant'),
                    ('access', OrderedDict([
                        ('id', 2),
                        ('value', 'Basic Access with Share')
                    ]))
                ]),
                OrderedDict([
                    ('id', 12),
                    ('name', 'Administrator'),
                    ('access', OrderedDict([
                        ('id', 1),
                        ('value', 'Administrator')
                    ]))
                ])
            ])
        ]))
    ])
