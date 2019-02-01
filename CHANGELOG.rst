All notable changes to this project will be documented in this file. The format
is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this
project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

Unreleased
------------


[0.9.1] - 2019-02-01

  - Updates to the response object returned by qb.download_files; the response
  is now the raw API_DoQuery response used to download files, not a modified
  list

  - Fixes to the default response formatter for API_DoQuery; previously, there
  were edge cases for no records, one record, and one column which were unhandled

[0.9.0] - 2019-01-14
--------------------

    - **qbpy is officially open sourced**

    - | Official repository is migrated to a clean repository to remove commit
      | history which included sensitive information, and to expose qbpy in a
      | public repository
