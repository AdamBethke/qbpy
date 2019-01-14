API_GetGroupRole
****************

`Quick Base Documentation: API_GetGroupRole <https://help.quickbase.com/api-guide/#API_GetGroupRole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetGroupRole', {
        'gid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetGroupRole'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('roles', OrderedDict([
            ('role', OrderedDict([
                ('id', 12),
                ('name', 'Administrator')
                ])
            )]
        ))
    ])
