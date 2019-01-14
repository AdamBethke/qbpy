API_AddUserToGroup
******************

`Quick Base Documentation: API_AddUserToGroup <https://help.quickbase.com/api-guide/#API_AddUserToGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddUserToGroup', {
        'gid': 1,
        'uid': '12345678.abcd',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddUserToGroup'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
