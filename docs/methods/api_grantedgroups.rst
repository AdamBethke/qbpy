API_GrantedGroups
*****************

`Quick Base Documentation: API_GrantedGroups <https://help.quickbase.com/api-guide/#.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GrantedGroups', {
        'userid': '12345678.abcd',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GrantedGroups'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('groups',
            OrderedDict([
                ('group', OrderedDict([
                    ('id', '12345.abcd'),
                    ('name', 'GroupName'),
                    ('description', 'Description of group'),
                    ('managedByUser', 'true')
                ])
            )]
        ))
    ])
