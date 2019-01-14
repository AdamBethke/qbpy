API_CreateGroup
***************

`Quick Base Documentation: API_CreateGroup <https://help.quickbase.com/api-guide/API_CreateGroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_CreateGroup', {
        'name': 'ExampleGroup',
        'description': 'An example group',
        'accountid': 123456,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_CreateGroup'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('group', OrderedDict([
            ('id', '1234.abcd'),
            ('name', 'ExampleGroup'),
            ('description', 'An example group'),
            ('managedByUser', 'true')
        ]))
    ])
