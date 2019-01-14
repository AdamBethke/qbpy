API_Webhooks_Delete
*******************

`Quick Base Documentation: API_Webhooks_Delete <https://help.quickbase.com/api-guide/API_Webhooks_Delete.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_Webhooks_Delete', {
        'actionidlist': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_Webhooks_Delete'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('actionId', 1)
    ])
