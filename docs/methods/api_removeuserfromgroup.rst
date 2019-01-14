API_RemoveUserFromGroup
***********************

`Quick Base Documentation: API_RemoveUserFromGroup <https://help.quickbase.com/api-guide/API_RemoveUserFromGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RemoveUserFromGroup', {
        'gid': 1,
        'uid': '12345678.abcd',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RemoveUserFromGroup'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
