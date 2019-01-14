API_Webhooks_Activate
*********************

`Quick Base Documentation: API_Webhooks_Activate <https://help.quickbase.com/api-guide/API_Webhooks_Activate.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_Webhooks_Activate', {
        'actionidlist': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_Webhooks_Activate'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('numChanged', 1),
        ('success', 'True')
    ])
