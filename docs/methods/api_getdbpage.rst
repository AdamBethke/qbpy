API_GetDBPage
*************

`Quick Base Documentation: API_GetDBPage <https://help.quickbase.com/api-guide/get_db_page.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetDBPage', {
        'pageID': 2,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetDBPage'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('pagebody', 'Hello World!')
    ])
