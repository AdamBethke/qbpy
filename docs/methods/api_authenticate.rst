API_Authenticate
****************

`Quick Base Documentation: API_Authenticate <https://help.quickbase.com/api-guide/#API_RemoveGroupFromRole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_Authenticate', {
        'username': 'example@example.org',
        'password': 'secret',
        'hours': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_Authenticate'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('ticket', 'ticket'),
        ('userid', '12345678.abcd')
    ])
