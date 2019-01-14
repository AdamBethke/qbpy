API_GetUserInfo
***************

`Quick Base Documentation: API_GetUserInfo <https://help.quickbase.com/api-guide/#getuserinfo.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetUserInfo', {
        'email': 'example@example.org',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetUserInfo'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('user', OrderedDict([
            ('id', '12345678.abcd'),
            ('firstName', 'FirstName'),
            ('lastName', 'LastName'),
            ('login', 'example@example.org'),
            ('email', 'example@example.org'),
            ('screenName', None),
            ('isVerified', 1),
            ('externalAuth', 0)
        ]))
    ])
