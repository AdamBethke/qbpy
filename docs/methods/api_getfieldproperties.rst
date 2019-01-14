API_GetFieldProperties
**********************

`Quick Base Documentation: API_GetFieldProperties <https://help.quickbase.com/api-guide/API_GetFieldProperties.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_GetFieldProperties', {
        'dbid': 'tabledbid',
        'fid': 6,
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_GetFieldProperties'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('field', OrderedDict([
            ('id', 6),
            ('field_type', 'timestamp'),
            ('base_type', 'int64'),
            ('label', 'Start Time'),
            ('nowrap', 1),
            ('bold', 0),
            ('required', 0),
            ('appears_by_default', 1),
            ('find_enabled', 1),
            ('allow_new_choices', 0),
            ('sort_as_given', 1),
            ('carrychoices', 1),
            ('foreignkey', 0),
            ('unique', 0),
            ('doesdatacopy', 1),
            ('fieldhelp', None),
            ('audited', 0),
            ('display_time', 1),
            ('display_relative', 0),
            ('display_month', 'number'),
            ('default_today', 0),
            ('display_dow', 0),
            ('display_zone', 0)
        ])
    )])
