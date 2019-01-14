API_GetAppDTMInfo
*****************

`Quick Base Documentation: API_GetAppDTMInfo <https://help.quickbase.com/api-guide/#get_app_dtm_info.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetAppDTMInfo', {
        'dbid': 'applicationdbid',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetAppDTMInfo'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('RequestTime', 1546781634820),
        ('RequestNextAllowedTime', 1546781639820),
        ('app', OrderedDict([
            ('id', 'applicationdbid'),
            ('lastModifiedTime', 1546357871483),
            ('lastRecModTime', 1546357871483)
        ])),
        ('tables', OrderedDict([
            ('table', [
                OrderedDict([
                    ('id', 'tabledbid'),
                    ('lastModifiedTime', 1542750869953),
                    ('lastRecModTime', 1542750869953)
                ]),
                OrderedDict([
                    ('id', 'tabledbid'),
                    ('lastModifiedTime', 1544191809460),
                    ('lastRecModTime', 1544191809460)
                ]),
                OrderedDict([
                    ('id', 'tabledbid'),
                    ('lastModifiedTime', 1546357871483),
                    ('lastRecModTime', 1546357871483)
                ]),
                OrderedDict([
                    ('id', 'tabledbid'),
                    ('lastModifiedTime', 1546281185617),
                    ('lastRecModTime', 1546281185617)
                ])
            ])
        ]))
    ])

