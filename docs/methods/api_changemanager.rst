API_ChangeManager
*****************

`Quick Base Documentation: API_ChangeManager <https://help.quickbase.com/api-guide/API_ChangeManager.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_ChangeManager', {
        'newmgr': 'example@example.org',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_ChangeManager'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
