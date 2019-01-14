API_AddSubGroup
***************

`Quick Base Documentation: API_AddSubGroup <https://help.quickbase.com/api-guide/#API_AddSubGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddSubGroup', {
        'gid': 1,
        'subgroupid': 2,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddSubGroup'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
