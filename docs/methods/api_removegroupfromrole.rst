API_RemoveGroupFromRole
***********************

`Quick Base Documentation: API_RemoveGroupFromRole <https://help.quickbase.com/api-guide/#API_RemoveGroupFromRole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RemoveGroupFromRole', {
        'gid': 1,
        'roleid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RemoveGroupFromRole'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
