API_RemoveSubgroup
******************

`Quick Base Documentation: API_RemoveSubgroup <https://help.quickbase.com/api-guide/#API_RemoveSubgroup.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_RemoveSubgroup', {
        'gid': 1,
        'subgroupid': 2,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_RemoveSubgroup'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
