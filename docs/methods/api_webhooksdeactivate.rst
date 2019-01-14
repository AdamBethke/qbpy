API_Webhooks_Deactivate
***********************

`Quick Base Documentation: API_Webhooks_Deactivate <https://help.quickbase.com/api-guide/API_Webhooks_Deactivate.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_Webhooks_Deactivate', {
        'actionidlist': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_Webhooks_Deactivate'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('numChanged', 1),
        ('success', 'True')
    ])
