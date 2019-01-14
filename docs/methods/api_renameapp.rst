API_RenameApp
*************

`Quick Base Documentation: API_RenameApp <https://help.quickbase.com/api-guide/renameapp.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RenameApp', {
        'newappname': 'Renamed Application',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RenameApp'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
