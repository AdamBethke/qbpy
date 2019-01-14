API_DeleteField
***************

`Quick Base Documentation: API_DeleteField <https://help.quickbase.com/api-guide/delete_field.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_DeleteField', {
        'dbid': 'tabledbid',
        'fid': 6,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_DeleteField'),
        ('errcode', 0),
        ('errtext', 'No error')
    ])
