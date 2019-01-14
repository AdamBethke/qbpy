API_DoQuery
***********

`Quick Base Documentation: API_DoQuery <https://help.quickbase.com/api-guide/#do_query.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_DoQuery', {
        'dbid': 'tabledbid',
        'query': "{1.OAF.'2018-01-01'}",
        'clist': '1.2.3.4.5',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_DoQuery'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('qid', -1),
        ('qname', None),
        ('table',
            OrderedDict([('name', 'Tables'),
                ('original',
                    OrderedDict([
                        ('table_id', 'tabledbid'),
                        ('app_id', 'appdbid'),
                        ('cre_date', 1496939307218),
                        ('mod_date', 1542389038387),
                        ('next_record_id', 18119),
                        ('next_field_id', 66),
                        ('next_query_id', 27),
                        ('def_sort_fid', 16),
                        ('def_sort_order', 1),
                        ('key_fid', 6),
                        ('single_record_name', 'Table'),
                        ('plural_record_name', 'Tables')
                    ])),
        ('queries', OrderedDict([
            ('query', [OrderedDict([
                ('id', 15),
                ('qyname', 'Query 1'),
                ('qytype', 'table'),
                ('qycrit', "({'43'.EX.'1'}"),
                ('qyclst', '16.19.23.8.51.13.17.15.14'),
                ('qyslst', '13.23'),
                ('qyopts', 'so-AA.gb-XX.nos.ned.nvw.qws.'),
                ('qycalst', '0.0')
            ]),
            ...
        ),
        ('fields', OrderedDict([
            ('field', [OrderedDict([
                ('id', 1),
                ('field_type', 'timestamp'),
                ('base_type', 'int64'),
                ('role', 'created'),
                ('label', 'Date Created'),
                ('nowrap', 1),
                ('bold', 0),
                ('required', 0),
                ('appears_by_default', 0),
                ('find_enabled', 0),
                ('allow_new_choices', 0),
                ('sort_as_given', 1),
                ('carrychoices', 1),
                ('foreignkey', 0),
                ('unique', 0),
                ('doesdatacopy', 0),
                ('fieldhelp', None),
                ('audited', 0),
                ('display_time', 1),
                ('display_relative', 0),
                ('display_month', 'number'),
                ('default_today', 0),
                ('display_dow', 0),
                ('display_zone', 0)
            ]),
            ...
        ('lastluserid', 1927),
        ('lusers', OrderedDict([
            ('luser', [OrderedDict([
                ('id', '12345678.abcd'),
                ('value', 'example@example.org')
            ]),
            ...
        ('records', OrderedDict([
            ('record', [OrderedDict([
                ('rid', 10602),
                ('update_id', 1530131155838),
                (1, 1528656316003),
                (2, 1530131155838),
                (3, 10602),
                (4, '12345678.abcd'),
                (5, '12345678.abcd')
            ]),
            ...
        ])]))
    ]))])

**pandas DataFrame:**

+---+-----+-------------+-------------+-------------+-----+-------------+-------------+
|idx| rid | update_id   |      1      |      2      |  3  |      4      |      5      |
+===+=====+=============+=============+=============+=====+=============+=============+
| 0 |10602|1530131155838|1528656316003|1530131155838|10602|12345678.abcd|12345678.abcd|
+---+-----+-------------+-------------+-------------+-----+-------------+-------------+
