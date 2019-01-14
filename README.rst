qbpy
====

.. image:: https://gitlab.com/abethke/qbpy/badges/master/pipeline.svg
    :target: https://gitlab.com/abethke/qbpy/commits/master
.. image:: https://gitlab.com/abethke/qbpy/badges/master/coverage.svg
    :target: https://gitlab.com/abethke/qbpy/commits/master


qbpy (\ **py**\ thon-\ **q**\ uick\ **b**\ ase) is a Python wrapper for the
`Quick Base API <https://help.quickbase.com/api-guide/index.html>`_.
While other language wrappers for Quick Base exist, the current implementations
in Python didn't have some of the features that we wanted to see, or hadn't been
updated in a while.

This package is designed to facilitate common data engineering tasks which we
rely on to use Quick Base an enterprise setting. We would welcome contributes
which would improve qbpy. You can read more about :ref:`contributing`, and take
a look at the :ref:`license` to learn more.

Acknowledgements
----------------

This package benefits from the excellent work done by @tflanagan on
`node-quickbase <https://github.com/tflanagan/node-quickbase>`_, which defines
an easy to use API for constructing Quick Base API calls and parsing responses.
While the data structures and code is different, node-quickbase's API informed
the development of the qbpy API.
