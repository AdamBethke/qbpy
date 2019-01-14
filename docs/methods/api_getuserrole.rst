API_GetUserRole
***************

`Quick Base Documentation: API_GetUserRole <https://help.quickbase.com/api-guide/#getuserrole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetUserRole', {
        'userid': '12345678.abcd',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetUserRole'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('user', OrderedDict([
            ('id', '12345678.abcd'),
            ('name', 'FirstName LastName'),
            ('roles', OrderedDict([
                ('role', [
                    OrderedDict([
                        ('id', 12),
                        ('name', 'Administrator'),
                        ('access', OrderedDict([
                            ('id', 1),
                            ('value', 'Administrator')
                        ]))
                    ]),
                    OrderedDict([
                        ('id', 11),
                        ('name', 'Participant'),
                        ('access', OrderedDict([
                            ('id', 2),
                            ('value', 'Basic Access with Share')
                        ]))
                    ])
                ])
            ]))
        ]))
    ])
