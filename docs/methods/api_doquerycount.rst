API_DoQueryCount
****************

`Quick Base Documentation: API_DoQueryCount <https://help.quickbase.com/api-guide/#do_query_count.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_DoQueryCount', {
        'dbid': 'tabledbid',
        'qid': 1,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_DoQueryCount'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('numMatches', 1)
    ])
