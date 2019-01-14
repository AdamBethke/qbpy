API_FieldRemoveChoices
**********************

`Quick Base Documentation: API_FieldRemoveChoices <https://help.quickbase.com/api-guide/field_remove_choices.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_FieldRemoveChoices', {
        'dbid': 'tabledbid',
        'fid': 7,
        'choice': 'Choice B',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_FieldRemoveChoices'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('fid', 7),
        ('fname', 'multchoice'),
        ('numremoved', 1)
    ])
