API_GetAncestorInfo
*******************

`Quick Base Documentation: API_GetAncestorInfo <https://help.quickbase.com/api-guide/getancestorinfo.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetAncestorInfo', {
        'ticket': 'authenticationticket',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_FindDBByName'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('ancestorappid', 'appdbid'),
        ('oldestancestorappid', 'appdbid')
    ])
