API_RemoveUserFromRole
**********************

`Quick Base Documentation: API_RemoveUserFromRole <https://help.quickbase.com/api-guide/#removeuserfromrole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RemoveUserFromRole', {
        'userid': '12345678.abcd',
        'roleid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RemoveUserFromRole'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
