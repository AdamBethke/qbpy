API_FieldAddChoices
*******************

`Quick Base Documentation: API_FieldAddChoices <https://help.quickbase.com/api-guide/field_add_choices.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_FieldAddChoices', {
        'dbid': 'tabledbid',
        'fid': 7,
        'choice': 'Choice B',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_FieldAddChoices'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('fid', 7),
        ('fname', 'multchoice'),
        ('numadded', 1)
    ])
