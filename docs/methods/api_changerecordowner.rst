API_ChangeRecordOwner
*********************

`Quick Base Documentation: API_ChangeRecordOwner <https://help.quickbase.com/api-guide/change_record_owner.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_ChangeRecordOwner', {
        'dbid': 'tabledbid',
        'rid': 1,
        'newowner': 'example@example.org',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_ChangeRecordOwner'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
