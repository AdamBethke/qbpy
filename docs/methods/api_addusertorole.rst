API_AddUserToRole
*****************

`Quick Base Documentation: API_AddUserToRole <https://help.quickbase.com/api-guide/#add_user_to_role.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddUserToRole', {
        'userid': '12345678.abcd',
        'roleid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddUserToRole'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
