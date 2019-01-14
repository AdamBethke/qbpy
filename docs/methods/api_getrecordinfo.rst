API_GetRecordInfo
*****************

`Quick Base Documentation: API_GetRecordInfo <https://help.quickbase.com/api-guide/#getrecordinfo.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetRecordInfo', {
        'dbid': 'tabledbid',
        'rid': 3,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetRecordInfo'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('rid', 3),
        ('num_fields', 7),
        ('update_id', 1544191809459),
        ('field', [
            OrderedDict([
                ('fid', 7),
                ('name', 'Sample Field'),
                ('type', 'Checkbox'),
                ('value', 0),
                ('printable', 'no')
            ]),
            ...
            OrderedDict([
                ('fid', 1),
                ('name', 'Date Created'),
                ('type', 'Date / Time'),
                ('value', 1544191809459),
                ('printable', '12-07-2018 09:10 AM')
            ]),
            OrderedDict([
                ('fid', 2),
                ('name', 'Date Modified'),
                ('type', 'Date / Time'),
                ('value', 1544191809459),
                ('printable', '12-07-2018 09:10 AM')
            ]),
            OrderedDict([
                ('fid', 3),
                ('name', 'Record ID#'),
                ('type', 'Record ID#'),
                ('value', 3)
            ]),
            OrderedDict([
                ('fid', 4),
                ('name', 'Record Owner'),
                ('type', 'User'),
                ('value', 'example@example.org'),
                ('printable', 'LastName, FirstName')
            ]),
            OrderedDict([
                ('fid', 5),
                ('name', 'Last Modified By'),
                ('type', 'User'),
                ('value', 'example@example.org'),
                ('printable', 'LastName, FirstName')
            ])
        ])
    ])
