API_GetSchema
*************

`Quick Base Documentation: API_GetSchema <https://help.quickbase.com/api-guide/#getschema.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetSchema')

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetSchema'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('time_zone', '(UTC-05:00) Eastern Time (US & Canada)'),
        ('date_format', 'MM-DD-YYYY'),
        ('table', OrderedDict([
            ('name', 'TableName'),
            ('original', OrderedDict([
                ('table_id', 'tabledbid'),
                ('app_id', 'appdbid'),
                ('cre_date', 1542750854324),
                ('mod_date', 1544195311204),
                ('next_record_id', 1),
                ('next_field_id', 6),
                ('next_query_id', 5),
                ('def_sort_fid', 0),
                ('def_sort_order', 1)
            ])),
            ('variables', OrderedDict([
                ('var', OrderedDict([
                    ('name', 'testvar'),
                    ('value', 1)
                ]))
            ])),
            ('chdbids', OrderedDict([
                ('chdbid', [
                    OrderedDict([
                        ('name', '_dbid_time_cards'),
                        ('value', 'tabledbid')
                    ]),
                    OrderedDict([
                        ('name', '_dbid_employees'),
                        ('value', 'tabledbid')
                    ])
                ])]
            )),
            ('fields', None)
        ]))
    ])
