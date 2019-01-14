API_CopyMasterDetail
********************

`Quick Base Documentation: API_CopyMasterDetail <https://help.quickbase.com/api-guide/API_CopyMasterDetail.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_CopyMasterDetail', {
        'dbid': 'tabledbid',
        'destrid': 1,
        'sourcerid': 1,
        'copyfid': 10,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_CopyMasterDetail'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('parentrid', 1),
        ('numCreated', 2)
    ])
