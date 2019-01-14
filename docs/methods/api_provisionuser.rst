API_ProvisionUser
*****************

`Quick Base Documentation: API_ProvisionUser <https://help.quickbase.com/api-guide/provisionuser.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_ProvisionUser', {
        'email': 'example@example.org',
        'roleid': 1,
        'fname': 'Tester',
        'lname': 'Role',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_ProvisionUser'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('userid', '12345678.abcd')
    ])
