API_GenResultsTable
*******************

`Quick Base Documentation: API_GenResultsTable <https://help.quickbase.com/api-guide/gen_results_table.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GenResultsTable', {
        'dbid': 'tabledbid',
        'qid': '1',
        'clist': '1.2.3.4.5',
        'slist': 4,
        'jht': 0,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    https://realm.quickbase.com/db/tabledbid?a=API_GenResultsTable...
