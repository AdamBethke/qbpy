API_ImportFromCSV
*****************

`Quick Base Documentation: API_ImportFromCSV <https://help.quickbase.com/api-guide/importfromcsv.html>`_

.. note:: The ``records_csv`` parameter **cannot** be empty, or it will throw an error.

Importing from a CSV is both a critical and finicky feature. Actually creating
the CSV is no small part of the task, as CSVs is a loosely structured data format.
Rather than try to prescribe the best way to generate the content for ``records_csv``,
we leave it open to accept any generic text input.

If you're looking for a way to generate a CSV programmatically, you might consider
something like:

.. code:: python

    import csv
    import pandas

    csv = pandas.DataFrame() # dataframe with meaningful content
    csv = csv.to_csv(index=False, na_rep='', quoting=csv.QUOTE_ALL)

Request
^^^^^^^

.. code:: python

    qb.api('API_ImportFromCSV', {
        'dbid': 'tabledbid',
        'clist': '6.7',
        'skipfirst': 1,
        'records_csv':
            '''
            fid_6, fid_7,
            value1, Choice A,
            value2, Choice B,
            ''',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_ImportFromCSV'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('num_recs_input', 2),
        ('num_recs_added', 2),
        ('rids', OrderedDict([
            ('rid', [
                OrderedDict([
                    ('update_id', 1546793240830),
                    ('value', 5)
                ]),
                OrderedDict([
                    ('update_id', 1546793240830),
                    ('value', 6)
                ])
            ])
        ]))
    ])
