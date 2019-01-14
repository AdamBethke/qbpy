API_GetUsersInGroup
*******************

`Quick Base Documentation: API_GetUsersInGroup <https://help.quickbase.com/api-guide/#API_GetUsersInGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetUsersInGroup', {
        'gid': 1,
        'includeallmgrs': True,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetUsersInGroup'),
        ('errcode', 0), ('errtext', 'No error'),
        ('group', OrderedDict([
            ('id', '12345.abcd'),
            ('name', 'Group Name'),
            ('description', None),
            ('users', OrderedDict([
                ('user', OrderedDict([
                    ('id', '12345678.abcd'),
                    ('firstName', 'FirstName'),
                    ('lastName', 'LastName'),
                    ('email', 'example@example.org'),
                    ('screenName', None),
                    ('isAdmin', 'true')
                ]))
            ])),
            ('managers', OrderedDict([
                ('manager', OrderedDict([
                    ('id', '12345678.abcd'),
                    ('firstName', 'FirstName'),
                    ('lastName', 'LastName'),
                    ('email', 'example@example.org'),
                    ('screenName', None),
                    ('isMember', 'true')
                ]))
            ])),
            ('subgroups', None)
        ]))
    ])
