========
qbpy API
========

.. _quickbase:

QuickBase
#########
.. automodule:: qbpy.quickbase
    :members:

Request and Response Handlers
#############################

At the core the API are the :ref:`request_handler` and the :ref:`response_handler`.
These classes are internal and are considered private for the purposes of
development and symantic versioning. We've provided documentation of their
internals because it helps to understand how we're building API calls and their
responses.

If you've built functionality which relies on these methods, please consider
submitting a merge request so that we can incorporate it into qbpy's public API.


.. _request_handler:

Request Handler
---------------
.. warning:: This is a private method, and may change as we continue to improve qbpy
.. automodule:: qbpy.request_handler
    :members:
    :private-members:


.. _response_handler:

Response Handler
----------------
.. warning:: This is a private method, and may change as we continue to improve qbpy
.. automodule:: qbpy.response_handler
    :members:
    :private-members:
