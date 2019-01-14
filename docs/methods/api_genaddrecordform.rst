API_GenAddRecordForm
********************

`Quick Base Documentation: API_GenAddRecordForm <https://help.quickbase.com/api-guide/gen_add_record_form.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GenAddRecordForm', {
        'dbid': 'tabledbid',
        'field': {
            '7': 'Prefill Example',
        },
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    https://realm.quickbase.com/db/tabledbid?a=API_GenAddRecordForm...
