API_SendInvitation
******************

`Quick Base Documentation: API_SendInvitation <https://help.quickbase.com/api-guide/#.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_SendInvitation', {
        'userid': '12345678.abcd',
        'usertext': 'Hello World!',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_SendInvitation'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
