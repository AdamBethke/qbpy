API_ChangeUserRole
******************

`Quick Base Documentation: API_ChangeUserRole <https://help.quickbase.com/api-guide/change_user_role.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_ChangeUserRole', {
        'userid': '12345678.abcd',
        'roleid': 1,
        'newroleid': 2,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_ChangeUserRole'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
