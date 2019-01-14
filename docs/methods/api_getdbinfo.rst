API_GetDBInfo
*************

`Quick Base Documentation: API_GetDBInfo <https://help.quickbase.com/api-guide/#get_db_info.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetDBInfo')

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetDBInfo'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('dbname', 'Employees'),
        ('lastRecModTime', 1544191809459),
        ('lastModifiedTime', 1544195311204),
        ('createdTime', 1542751030435),
        ('numRecords', 1),
        ('mgrID', '12345678.abcd'),
        ('mgrName', 'example@example.org'),
        ('version', '2.0'),
        ('time_zone', '(UTC-05:00) Eastern Time (US & Canada)')
    ])
