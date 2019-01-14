API_AddGroupToRole
******************

`Quick Base Documentation: API_AddGroupToRole <https://help.quickbase.com/api-guide/#API_AddGroupToRole.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddGroupToRole', {
        'gid': 1,
        'roleid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddGroupToRole'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
