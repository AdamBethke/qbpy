API_ChangeGroupInfo
*******************

`Quick Base Documentation: API_ChangeGroupInfo <https://help.quickbase.com/api-guide/API_ChangeGroupInfo.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_ChangeGroupInfo', {
      'gid': 1,
      'name': 'ChangedNameForGroup',
      'description': 'Changed description for group',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
      ('action', 'API_ChangeGroupInfo'),
      ('errcode', 0),
      ('errtext', 'No error')
    ])
