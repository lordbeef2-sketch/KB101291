# NI OSS SOURCE SNAPSHOT: nixnet-python

<!--NI_OSS_SNAPSHOT repo=ni/nixnet-python commit=b9851d3f431183849078f174a7fb8ee349facd81 -->

<!--NI_OSS_SOURCE repo=nixnet-python path=.clog.toml sha256=62ace6bfb1fe03fbf0f61ccf9016d80de50cdc5cf420a86dc7831e6e24b43d62 bytes=112 -->
## FILE: .clog.toml

- repository: `ni/nixnet-python`
- source_path: `.clog.toml`
- sha256: `62ace6bfb1fe03fbf0f61ccf9016d80de50cdc5cf420a86dc7831e6e24b43d62`
- bytes: 112

````toml
[clog]
repository = "https://github.com/ni/nixnet-python"
changelog = "CHANGELOG.md"
from-latest-tag = true
````

<!--NI_OSS_SOURCE repo=nixnet-python path=.github/ISSUE_TEMPLATE.md sha256=9c840d9661173749b749b117548445621605c15072fff3db3fa62ea8a610832b bytes=515 -->
## FILE: .github/ISSUE_TEMPLATE.md

- repository: `ni/nixnet-python`
- source_path: `.github/ISSUE_TEMPLATE.md`
- sha256: `9c840d9661173749b749b117548445621605c15072fff3db3fa62ea8a610832b`
- bytes: 515

````markdown
*TODO* Detailed steps on how to produce the problem, including full traceback if applicable.

- OS: *NAME* *VERSION*
- Python version: *VERSION*
- NI-XNET version: *VERSION*

Note: to get the Python version, you can run
```bash
$ python -c "import sys; print(sys.version)"
```

Note: to get NI-XNET version, follow the steps in [this KB article](http://digital.ni.com/express.nsf/bycode/ex8amn).

### Installed packages and version

*TODO:* paste the output from
```bash
$ python -m pip list
```
````

<!--NI_OSS_SOURCE repo=nixnet-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=5dd9438b0b8b2c0b18337e585485d9a850a68b54993a52a7f28040a3aee83779 bytes=846 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nixnet-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `5dd9438b0b8b2c0b18337e585485d9a850a68b54993a52a7f28040a3aee83779`
- bytes: 846

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nixnet-python/blob/main/CONTRIBUTING.rst).
- [ ] New tests have been created for any new features or regression tests for bugfixes.
- [ ] `tox` successfully runs, including unit tests and style checks (see [CONTRIBUTING.md](https://github.com/ni/nixnet-python/blob/main/CONTRIBUTING.rst)).

TODO: Check the above boxes with an 'x' to indicate what steps you have taken in preparing this Pull Request.

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nixnet-python path=.gitignore sha256=8de1bee7c40441b7c45089766dd6042b67d3401de63322d8c8064c57487f7edb bytes=117 -->
## FILE: .gitignore

- repository: `ni/nixnet-python`
- source_path: `.gitignore`
- sha256: `8de1bee7c40441b7c45089766dd6042b67d3401de63322d8c8064c57487f7edb`
- bytes: 117

````text
.cache/
.mypy_cache/
.tox/
junit/
docs/_build/
dist/
__pycache__
.coverage
coverage.xml
*.egg-info/
*.pyc
````

<!--NI_OSS_SOURCE repo=nixnet-python path=.readthedocs.yaml sha256=d6a79f6e770ff446648c0792fed4125d6240b28809f8543df0f587250343cb9e bytes=699 -->
## FILE: .readthedocs.yaml

- repository: `ni/nixnet-python`
- source_path: `.readthedocs.yaml`
- sha256: `d6a79f6e770ff446648c0792fed4125d6240b28809f8543df0f587250343cb9e`
- bytes: 699

````yaml
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    post_create_environment:
      - pip install --upgrade poetry
    post_install:
      # VIRTUAL_ENV needs to be set manually for now.
      # See https://github.com/readthedocs/readthedocs.org/pull/11152/
      - VIRTUAL_ENV=$READTHEDOCS_VIRTUALENV_PATH poetry install --with docs

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Build all formats supported by Sphinx (htmlzip, pdf, epub)
formats: all
````

<!--NI_OSS_SOURCE repo=nixnet-python path=.travis.yml sha256=ca862fe17fc28f7bbf3dd2be936b6bc6fc21107eb4714a231409279cca01a65d bytes=1277 -->
## FILE: .travis.yml

- repository: `ni/nixnet-python`
- source_path: `.travis.yml`
- sha256: `ca862fe17fc28f7bbf3dd2be936b6bc6fc21107eb4714a231409279cca01a65d`
- bytes: 1277

````yaml
cache: pip
dist: jammy
language: python
# For pypy versions, see https://github.com/pyenv/pyenv/tree/master/plugins/python-build/share/python-build
# For Travis-supported Python versions, see https://docs.travis-ci.com/user/languages/python/#python-versions
python:
  - 3.9
  - 3.10
  - 3.11
  - 3.12
  - 3.13
install:
  - python -m pip install --upgrade pip
  - pip install --upgrade tox-travis
  - pip install --upgrade coveralls
  - pip install --upgrade --prefer-binary poetry
script:
  - tox
  # Verify the file is at least valid even if it isn't run.
  - tox -c tox-integration.ini -l
after_success:
  - coveralls
# Explicitly include the pypy3.9-7.3.9 job since it requires different install steps
jobs:
  include:
    - python: pypy3.9-7.3.9
      install:
        - python -m pip install --upgrade pip
        - pip install --upgrade tox-travis
        - pip install --upgrade coveralls
        # poetry-plugin-export is required for Poetry 2.0+ to export a requirements.txt file as a
        # workaround for the AsssertionError from cpyext (CPython compatibility layer) issue with
        # `poetry install / sync` when using pypy3.9-7.3.9 in Ubuntu Jammy
        - pip install --upgrade --prefer-binary poetry poetry-plugin-export
````

<!--NI_OSS_SOURCE repo=nixnet-python path=CONTRIBUTING.rst sha256=fb6914c91d386ed13e0d8cd2ccc895f8e55c92c1c447874e612f599269d3e0d2 bytes=4026 -->
## FILE: CONTRIBUTING.rst

- repository: `ni/nixnet-python`
- source_path: `CONTRIBUTING.rst`
- sha256: `fb6914c91d386ed13e0d8cd2ccc895f8e55c92c1c447874e612f599269d3e0d2`
- bytes: 4026

````rst
Contributing to nixnet
=======================

Contributions to **nixnet** are welcome from all!

**nixnet** is managed via `git <https://git-scm.com>`_, with the canonical
upstream repository hosted on `GitHub <https://github.com/ni/nixnet-python>`_.

**nixnet** follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull
request.

See `GitHub's official documentation <https://help.github.com/articles/using-pull-requests/>`_
for more details.

Getting Started
---------------

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Run the unit tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   `GitHub issues page <http://github.com/ni/nixnet-python/issues>`_.
3. Write new tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
4. Make your change.
5. Run all the unit tests again (which include the tests you just added),
   and confirm that they all pass.
6. Send a GitHub Pull Request to the ni/nixnet-python main branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.

.. _testing-section:

Testing
-------

In order to be able to run the **nixnet** unit tests, your setup should meet
the following minimum requirements:

  - Setup has a machine with NI-XNET or the NI-XNET Runtime installed.
  - Machine has a supported version of CPython or PyPy installed.
  - **TODO** Document required hardware and system setup.

**nixnet** relies on `tox <http://tox.readthedocs.io>`_ and `pytest <https://docs.pytest.org/en/latest/usage.html>`_ for testing

  $ pip install tox

To run the tests::

  $ # Unit tests:
  $ tox
  $ # Integration tests:
  $ tox -c tox-integration.ini -- --can-in-interface CAN1 --can-out-interface CAN2 --lin-in-interface LIN1 --lin-out-interface LIN2
  $ # Integration tests (no LIN board):
  $ tox -c tox-integration.ini -- --can-in-interface CAN1 --can-out-interface CAN2

Examples for debugging failures::

  $ # Only run Python 3.9 unit tests
  $ tox -e py39-test
  $ # Further filter those tests to all starting with test_frames
  $ tox -e py39-test -- -k test_frames
  $ # Drop into PDB on first failure and quit when done
  $ tox -e py39-test -- -x --pdb

Developer Certificate of Origin (DCO)
-------------------------------------

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

(taken from `developercertificate.org <http://developercertificate.org/>`_)

See `LICENSE <https://github.com/ni/nixnet-python/blob/main/LICENSE>`_
for details about how **nixnet** is licensed.
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/constants.rst sha256=14d2d7c5988c5b3fe72eb99c8d2af5d023f25ce5d36efbb35ed8544d0fb3c233 bytes=183 -->
## FILE: docs/api_reference/constants.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/constants.rst`
- sha256: `14d2d7c5988c5b3fe72eb99c8d2af5d023f25ce5d36efbb35ed8544d0fb3c233`
- bytes: 183

````rst
nixnet.constants
================

.. automodule:: nixnet.constants
    :members:
    :show-inheritance:

.. automodule:: nixnet._enums
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/convert.rst sha256=730101f8435239cc9186d372f98df9de4336c2df7828fac655b071379b314d88 bytes=232 -->
## FILE: docs/api_reference/convert.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/convert.rst`
- sha256: `730101f8435239cc9186d372f98df9de4336c2df7828fac655b071379b314d88`
- bytes: 232

````rst
nixnet.convert
==============

.. automodule:: nixnet.convert
    :members:
    :show-inheritance:
    :inherited-members:

.. toctree::
   :maxdepth: 3
   :caption: API Reference:

   session/signals
   session/j1939
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/cluster.rst sha256=6a304ab20898bdca8ae9f55b78972b831a15fdedbe55c425d5e6ab51a85cd770 bytes=158 -->
## FILE: docs/api_reference/database/cluster.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/cluster.rst`
- sha256: `6a304ab20898bdca8ae9f55b78972b831a15fdedbe55c425d5e6ab51a85cd770`
- bytes: 158

````rst
nixnet.database.cluster
=======================

.. automodule:: nixnet.database._cluster
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/collection.rst sha256=46c2a64b99fbdfa7c72f7480f9af60581618ace13f42339e4fbe0b348f6b7759 bytes=167 -->
## FILE: docs/api_reference/database/collection.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/collection.rst`
- sha256: `46c2a64b99fbdfa7c72f7480f9af60581618ace13f42339e4fbe0b348f6b7759`
- bytes: 167

````rst
nixnet.database.collection
==========================

.. automodule:: nixnet.database._collection
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/database.rst sha256=9cd35f57a8a4c86317c58cf5bc3ce3bc31ec0fd6b73a3ddd2ae9a677cfac5994 bytes=160 -->
## FILE: docs/api_reference/database/database.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/database.rst`
- sha256: `9cd35f57a8a4c86317c58cf5bc3ce3bc31ec0fd6b73a3ddd2ae9a677cfac5994`
- bytes: 160

````rst
nixnet.database.database
========================

.. automodule:: nixnet.database.database
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/dbc_attributes.rst sha256=223dab9a1c02989aff7f0b79ed1aece78dc61c51fa8424db69d91a83dfac5a7f bytes=179 -->
## FILE: docs/api_reference/database/dbc_attributes.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/dbc_attributes.rst`
- sha256: `223dab9a1c02989aff7f0b79ed1aece78dc61c51fa8424db69d91a83dfac5a7f`
- bytes: 179

````rst
nixnet.database.dbc_attributes
==============================

.. automodule:: nixnet.database._dbc_attributes
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/dbc_signal_value_table.rst sha256=7bfe66cf60038dec1f0ea0da9f7b581ec7a4a61ad6259e7bbdfb1dff5df6d3b3 bytes=203 -->
## FILE: docs/api_reference/database/dbc_signal_value_table.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/dbc_signal_value_table.rst`
- sha256: `7bfe66cf60038dec1f0ea0da9f7b581ec7a4a61ad6259e7bbdfb1dff5df6d3b3`
- bytes: 203

````rst
nixnet.database.dbc_signal_value_table
======================================

.. automodule:: nixnet.database._dbc_signal_value_table
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/ecu.rst sha256=c107ac374f17c8e023923fb0b60aa3e9aca0d294f95ce3d8ac168ca5905ca974 bytes=146 -->
## FILE: docs/api_reference/database/ecu.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/ecu.rst`
- sha256: `c107ac374f17c8e023923fb0b60aa3e9aca0d294f95ce3d8ac168ca5905ca974`
- bytes: 146

````rst
nixnet.database.ecu
===================

.. automodule:: nixnet.database._ecu
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/frame.rst sha256=a225c1211a059fd474afa8e1bb0f8cc5d0f6bcc04984b5fb8c34481a0a662186 bytes=152 -->
## FILE: docs/api_reference/database/frame.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/frame.rst`
- sha256: `a225c1211a059fd474afa8e1bb0f8cc5d0f6bcc04984b5fb8c34481a0a662186`
- bytes: 152

````rst
nixnet.database.frame
=====================

.. automodule:: nixnet.database._frame
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/lin_sched.rst sha256=11e8c8e02c4e55945502ae3ebe61e315f7753401f73ea600b4d0abc3ad36ae58 bytes=164 -->
## FILE: docs/api_reference/database/lin_sched.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/lin_sched.rst`
- sha256: `11e8c8e02c4e55945502ae3ebe61e315f7753401f73ea600b4d0abc3ad36ae58`
- bytes: 164

````rst
nixnet.database.lin_sched
=========================

.. automodule:: nixnet.database._lin_sched
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/lin_sched_entry.rst sha256=2543c2a7df76704f4d0234fd61aff0ea2e22a82c0aa08e6ddf2b3074ad8724ed bytes=182 -->
## FILE: docs/api_reference/database/lin_sched_entry.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/lin_sched_entry.rst`
- sha256: `2543c2a7df76704f4d0234fd61aff0ea2e22a82c0aa08e6ddf2b3074ad8724ed`
- bytes: 182

````rst
nixnet.database.lin_sched_entry
===============================

.. automodule:: nixnet.database._lin_sched_entry
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/pdu.rst sha256=cf4fcc6bebbd9f937514bbf26237c9c3dc675d562b628f1ace7298e0e971a242 bytes=146 -->
## FILE: docs/api_reference/database/pdu.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/pdu.rst`
- sha256: `cf4fcc6bebbd9f937514bbf26237c9c3dc675d562b628f1ace7298e0e971a242`
- bytes: 146

````rst
nixnet.database.pdu
===================

.. automodule:: nixnet.database._pdu
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/signal.rst sha256=510edb6449828a1cc868fb12ec74bf3e2051b8f519214299125f327cf9b8c66b bytes=155 -->
## FILE: docs/api_reference/database/signal.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/signal.rst`
- sha256: `510edb6449828a1cc868fb12ec74bf3e2051b8f519214299125f327cf9b8c66b`
- bytes: 155

````rst
nixnet.database.signal
======================

.. automodule:: nixnet.database._signal
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database/subframe.rst sha256=b81377edae421a1f4667750fe427fdfd0d598c260e2d66f44309d567eb7c2288 bytes=161 -->
## FILE: docs/api_reference/database/subframe.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database/subframe.rst`
- sha256: `b81377edae421a1f4667750fe427fdfd0d598c260e2d66f44309d567eb7c2288`
- bytes: 161

````rst
nixnet.database.subframe
========================

.. automodule:: nixnet.database._subframe
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/database.rst sha256=ff3de3012cde7c73d1757356aa480d4adad551d69f8929bbc67ec7828910b7e6 bytes=376 -->
## FILE: docs/api_reference/database.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/database.rst`
- sha256: `ff3de3012cde7c73d1757356aa480d4adad551d69f8929bbc67ec7828910b7e6`
- bytes: 376

````rst
nixnet.database
===============

.. toctree::
   :maxdepth: 3
   :caption: API Reference:

   database/cluster
   database/database
   database/ecu
   database/frame
   database/lin_sched
   database/lin_sched_entry
   database/pdu
   database/signal
   database/subframe
   database/collection
   database/dbc_attributes
   database/dbc_signal_value_table
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/errors.rst sha256=a4fdf2228ee78a2e15b26ee9dc7123bf386de8bdc5912dd222bd808f697dc235 bytes=102 -->
## FILE: docs/api_reference/errors.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/errors.rst`
- sha256: `a4fdf2228ee78a2e15b26ee9dc7123bf386de8bdc5912dd222bd808f697dc235`
- bytes: 102

````rst
nixnet.errors
=============

.. automodule:: nixnet.errors
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session/base.rst sha256=fa9ce7294a7052fecf0d409ead817a18115f5a7121a09f407389fce90f3ba6e3 bytes=146 -->
## FILE: docs/api_reference/session/base.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session/base.rst`
- sha256: `fa9ce7294a7052fecf0d409ead817a18115f5a7121a09f407389fce90f3ba6e3`
- bytes: 146

````rst
nixnet.session.base
===================

.. automodule:: nixnet._session.base
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session/frames.rst sha256=6f1fdd1c574d5ba67d29a292110e01fbeabdb82710d0aa22347e36d3dfdc2b0b bytes=152 -->
## FILE: docs/api_reference/session/frames.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session/frames.rst`
- sha256: `6f1fdd1c574d5ba67d29a292110e01fbeabdb82710d0aa22347e36d3dfdc2b0b`
- bytes: 152

````rst
nixnet.session.frames
=====================

.. automodule:: nixnet._session.frames
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session/intf.rst sha256=04c8a66b244555d2afde90ddd92a341d107237e6b76e21346d2243998b56ff44 bytes=121 -->
## FILE: docs/api_reference/session/intf.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session/intf.rst`
- sha256: `04c8a66b244555d2afde90ddd92a341d107237e6b76e21346d2243998b56ff44`
- bytes: 121

````rst
nixnet.session.intf
===================

.. automodule:: nixnet._session.intf
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session/j1939.rst sha256=4ce1dc257c8f1bb5cb6321fb67ea85a0e0b95eb6cab7ff88515c60fc041fc591 bytes=124 -->
## FILE: docs/api_reference/session/j1939.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session/j1939.rst`
- sha256: `4ce1dc257c8f1bb5cb6321fb67ea85a0e0b95eb6cab7ff88515c60fc041fc591`
- bytes: 124

````rst
nixnet.session.j1939
====================

.. automodule:: nixnet._session.j1939
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session/signals.rst sha256=5212a24108cb73a440ffa08eef6d4d45ee9fb4724caaa7c75f2a35f8af3c0e1c bytes=155 -->
## FILE: docs/api_reference/session/signals.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session/signals.rst`
- sha256: `5212a24108cb73a440ffa08eef6d4d45ee9fb4724caaa7c75f2a35f8af3c0e1c`
- bytes: 155

````rst
nixnet.session.signals
======================

.. automodule:: nixnet._session.signals
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/session.rst sha256=458a2da00f57f87547d57f487b861a098e7d1bbf176a20686a1d591866896117 bytes=287 -->
## FILE: docs/api_reference/session.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/session.rst`
- sha256: `458a2da00f57f87547d57f487b861a098e7d1bbf176a20686a1d591866896117`
- bytes: 287

````rst
nixnet.session
==============

.. automodule:: nixnet.session
    :members:
    :show-inheritance:
    :inherited-members:

.. toctree::
   :maxdepth: 3
   :caption: API Reference:

   session/frames
   session/signals
   session/intf
   session/j1939

   session/base
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/system/databases.rst sha256=55807ef3890183216259e7760a7a07f0a010df5e11282d030dbaa0540ce7d860 bytes=159 -->
## FILE: docs/api_reference/system/databases.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/system/databases.rst`
- sha256: `55807ef3890183216259e7760a7a07f0a010df5e11282d030dbaa0540ce7d860`
- bytes: 159

````rst
nixnet.system.databases
========================

.. automodule:: nixnet.system._databases
    :members:
    :inherited-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/system/device.rst sha256=2f49df1ada89c3d8eeab5982d82650ef4f29410445bb59237ea1517985b817fe bytes=124 -->
## FILE: docs/api_reference/system/device.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/system/device.rst`
- sha256: `2f49df1ada89c3d8eeab5982d82650ef4f29410445bb59237ea1517985b817fe`
- bytes: 124

````rst
nixnet.system.device
====================

.. automodule:: nixnet.system._device
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/system/interface.rst sha256=a312dec77e38257557f89faf7a7fc46cd15547b91b8153ea5426523485cbc7da bytes=133 -->
## FILE: docs/api_reference/system/interface.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/system/interface.rst`
- sha256: `a312dec77e38257557f89faf7a7fc46cd15547b91b8153ea5426523485cbc7da`
- bytes: 133

````rst
nixnet.system.interface
=======================

.. automodule:: nixnet.system._interface
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/system/system.rst sha256=f2eeddfafb672122fc57c950d8d087164e33148903c6a6cabb39e804a4ce11a4 bytes=99 -->
## FILE: docs/api_reference/system/system.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/system/system.rst`
- sha256: `f2eeddfafb672122fc57c950d8d087164e33148903c6a6cabb39e804a4ce11a4`
- bytes: 99

````rst
nixnet.system.system
====================

.. automodule:: nixnet.system.system
    :members:
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/system.rst sha256=f398b6ab8d7412688f3334d4a015c730a019106cc992e6df02ad75a45bb90841 bytes=172 -->
## FILE: docs/api_reference/system.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/system.rst`
- sha256: `f398b6ab8d7412688f3334d4a015c730a019106cc992e6df02ad75a45bb90841`
- bytes: 172

````rst
nixnet.system
=============

.. toctree::
   :maxdepth: 3
   :caption: API Reference:

   system/system
   system/databases
   system/device
   system/interface
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference/types.rst sha256=906bebf21e2e44dd29836e89156058de0e28aad93b5a9f75ed7a5f8e9721cff5 bytes=127 -->
## FILE: docs/api_reference/types.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference/types.rst`
- sha256: `906bebf21e2e44dd29836e89156058de0e28aad93b5a9f75ed7a5f8e9721cff5`
- bytes: 127

````rst
nixnet.types
============

.. automodule:: nixnet.types
    :members:
    :show-inheritance:
    :exclude-members: type
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/api_reference.rst sha256=8e79f2d2098732dd45ea362da5a0c1a29d9c31cc851ff1e161dd3907bee4497e bytes=321 -->
## FILE: docs/api_reference.rst

- repository: `ni/nixnet-python`
- source_path: `docs/api_reference.rst`
- sha256: `8e79f2d2098732dd45ea362da5a0c1a29d9c31cc851ff1e161dd3907bee4497e`
- bytes: 321

````rst
.. _api_reference_page:

=============
API Reference
=============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents:

   api_reference/session
   api_reference/convert
   api_reference/system
   api_reference/database
   api_reference/constants
   api_reference/types
   api_reference/errors
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/conf.py sha256=77a8964b90fb37085d6e6c963bf11b2702bf14dd26099d4cc40c1537f1dcb9d3 bytes=6017 -->
## FILE: docs/conf.py

- repository: `ni/nixnet-python`
- source_path: `docs/conf.py`
- sha256: `77a8964b90fb37085d6e6c963bf11b2702bf14dd26099d4cc40c1537f1dcb9d3`
- bytes: 6017

````python
# -*- coding: utf-8 -*-
#
# NI-XNET Python API documentation build configuration file, created by
# sphinx-quickstart on Thu Jun 14 09:40:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime
import os
import re
import sys
import tomli
sys.path.insert(0, os.path.abspath('../'))


def get_project_metadata_from_pyproject_toml():
    """
    Gets the project metadata from the pyproject.toml file.

    Returns:
        tuple(str, str, str, str): The project name, author, full version, and short version (X.Y).
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir, "../pyproject.toml"), "rb") as pyproject_file:
        pyproject = tomli.load(pyproject_file)
    pyproject_metadata = pyproject["tool"]["poetry"]
    author_regex = re.compile("(.+) <.+>")
    short_version_regex = re.compile("^\\d+\\.\\d+")
    return (
        pyproject_metadata["name"],
        author_regex.search(pyproject_metadata["authors"][0]).group(1),
        pyproject_metadata["version"],
        short_version_regex.search(pyproject_metadata["version"]).group(0),
    )


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# release: The full version, including alpha/beta/rc tags.
# version: The short X.Y version.
project, author, release, version = get_project_metadata_from_pyproject_toml()
copyright = u'2017-{}, {}'.format(datetime.now().year, author)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NI-XNETPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NI-XNETPythonAPI.tex', u'NI-XNET Python API Documentation',
     u'National Instruments', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ni-xnetpythonapi', u'NI-XNET Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NI-XNETPythonAPI', u'NI-XNET Python API Documentation',
     author, 'NI-XNETPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/contributing.rst sha256=978bd7672e8573fb90d0d611ce1777faa61206f5d0bdbc2572d7fca9231674f4 bytes=34 -->
## FILE: docs/contributing.rst

- repository: `ni/nixnet-python`
- source_path: `docs/contributing.rst`
- sha256: `978bd7672e8573fb90d0d611ce1777faa61206f5d0bdbc2572d7fca9231674f4`
- bytes: 34

````rst
.. include:: ../CONTRIBUTING.rst
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/can_lin_diff.rst sha256=92042cda0a786ab7f977dcd6231d849fd9a66549e99263a3aa983680e8ef1fe5 bytes=820 -->
## FILE: docs/examples/can_lin_diff.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/can_lin_diff.rst`
- sha256: `92042cda0a786ab7f977dcd6231d849fd9a66549e99263a3aa983680e8ef1fe5`
- bytes: 820

````rst
Adapting CAN examples to LIN
============================

To adapt the examples from CAN to LIN, reference signals in a database that use LIN:
   ``write``:
      Accepts any frame type.
   ``read``:
      Chooses the frame object to create based on the ``frame_type`` field in
      the raw data.  This can be overridden by passing a custom
      :any:`nixnet.types.FrameFactory` in the ``frame_type`` parameter.
   ``change_lin_sched``:
      Writes a request for the LIN interface to change
      the running schedule.

This displays the diff of ``can_frame_stream_io.py`` and 
``lin_frame_stream_io.py`` to demonstrate the changes required to
update CAN example code for LIN.

.. literalinclude:: ../../nixnet_examples/lin_frame_stream_io.py
	:diff: ../../nixnet_examples/can_frame_stream_io.py
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/conversion.rst sha256=5b2cc8b365c6a04335aa50ccaeced778a0228b1dfadc0178fa3ddd7708e979e6 bytes=725 -->
## FILE: docs/examples/conversion.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/conversion.rst`
- sha256: `5b2cc8b365c6a04335aa50ccaeced778a0228b1dfadc0178fa3ddd7708e979e6`
- bytes: 725

````rst
Signal/Frame Conversion Example
===============================

This example uses :any:`nixnet.convert.SignalConversionSinglePointSession` to
take signal values from the user, converts them to frames, and converts them back.

To adapt this example to LIN frames, reference signals in a database that use LIN:
   ``convert_frames_to_signals``:
      Accepts any frame type.
   ``convert_signals_to_frames``:
      Chooses the frame object to create based on the ``frame_type`` field in
      the raw data.  This can be overridden by passing a custom
      :any:`nixnet.types.FrameFactory` in the ``frame_type`` parameter.

.. literalinclude:: ../../nixnet_examples/can_signal_conversion.py
   :pyobject: main
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/dynamic_database_creation.rst sha256=f42b7d8aa31ece5a12d10804c1b5e851f2bdd95a3562b599df975d73012fef14 bytes=719 -->
## FILE: docs/examples/dynamic_database_creation.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/dynamic_database_creation.rst`
- sha256: `f42b7d8aa31ece5a12d10804c1b5e851f2bdd95a3562b599df975d73012fef14`
- bytes: 719

````rst
Dynamic Database Creation
=========================

This example programmatically modifies the in-memory database to
contain a cluster, a frame, and two signals. The database is then
used in a :any:`nixnet.session.SignalOutSinglePointSession` and
:any:`nixnet.session.SignalInSinglePointSession` to write and then
read a pair of signals.

.. _can_dynamic_database_creation_label:

CAN Dynamic Database Creation
-----------------------------

.. literalinclude:: ../../nixnet_examples/can_dynamic_database_creation.py

.. _lin_dynamic_database_creation_label:

LIN Dynamic Database Creation
-----------------------------

.. literalinclude:: ../../nixnet_examples/lin_dynamic_database_creation.py
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/programmatic_databases.rst sha256=dbe92aa700356d57e19c33f17b8eb52989c397e7e90d1ffbb2942e375fb3e20f bytes=305 -->
## FILE: docs/examples/programmatic_databases.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/programmatic_databases.rst`
- sha256: `dbe92aa700356d57e19c33f17b8eb52989c397e7e90d1ffbb2942e375fb3e20f`
- bytes: 305

````rst
Programmatic Database Usage
===========================

This example uses :any:`nixnet.system._databases.AliasCollection` to demonstrate how
databases can be programmatically added and used in a system.

.. literalinclude:: ../../nixnet_examples/programmatic_database_usage.py
   :pyobject: main
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/queued_io.rst sha256=51a8ef3893e54b9e2fc701c24d9d024225247852010171e31b36cfccb4bebd71 bytes=366 -->
## FILE: docs/examples/queued_io.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/queued_io.rst`
- sha256: `51a8ef3893e54b9e2fc701c24d9d024225247852010171e31b36cfccb4bebd71`
- bytes: 366

````rst
Queued I/O Example
==================

This example uses :any:`nixnet.session.FrameInQueuedSession` and
:any:`nixnet.session.FrameOutQueuedSession` to demonstrate how queued sessions
work.

CAN Queued I/O
---------------

.. literalinclude:: ../../nixnet_examples/can_frame_queued_io.py

Refer to :doc:`can_lin_diff` for how to adapt from CAN to LIN.
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/single_point_io.rst sha256=65548251976145e46b5461ea236ea380416a9c1c17c7222428994c35d822690d bytes=894 -->
## FILE: docs/examples/single_point_io.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/single_point_io.rst`
- sha256: `65548251976145e46b5461ea236ea380416a9c1c17c7222428994c35d822690d`
- bytes: 894

````rst
Single-Point I/O Example
========================

This example uses :any:`nixnet.session.SignalInSinglePointSession` and
:any:`nixnet.session.SignalOutSinglePointSession` to demonstrate how single-point sessions
work.

To adapt this to Frames, just change the sessions to
:any:`nixnet.session.FrameInSinglePointSession` and
:any:`nixnet.session.FrameOutSinglePointSession` with frames instead of
signals.  Then adjust ``read``/``write`` to take a frame object per frame
configured in the session rather than signals. 

This works for both CAN and LIN
frames. LIN frames also require ``change_lin_sched`` to write a request for the
LIN interface to change the running schedule. See :doc:`queued_io` to see how
to read and write frames.

CAN Single-Point I/O
--------------------

.. literalinclude:: ../../nixnet_examples/can_signal_single_point_io.py
   :pyobject: main
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples/stream_io.rst sha256=321a3916cc595538e59f9b749a93f644a931db03d7902083936d0f4daaee6443 bytes=465 -->
## FILE: docs/examples/stream_io.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples/stream_io.rst`
- sha256: `321a3916cc595538e59f9b749a93f644a931db03d7902083936d0f4daaee6443`
- bytes: 465

````rst
Stream I/O Example
==================

This example uses :any:`nixnet.session.FrameInStreamSession` and
:any:`nixnet.session.FrameOutStreamSession` to demonstrate how streamed sessions
work.

CAN Stream I/O
--------------

.. literalinclude:: ../../nixnet_examples/can_frame_stream_io.py

LIN Stream I/O
--------------

.. literalinclude:: ../../nixnet_examples/lin_frame_stream_io.py

Refer to :doc:`can_lin_diff` for how to adapt from CAN to LIN.
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/examples.rst sha256=cfaa3ed70b173cb01d8d970a3ed8c3f0e64769d5fdeff62dd4fe753e7896c129 bytes=319 -->
## FILE: docs/examples.rst

- repository: `ni/nixnet-python`
- source_path: `docs/examples.rst`
- sha256: `cfaa3ed70b173cb01d8d970a3ed8c3f0e64769d5fdeff62dd4fe753e7896c129`
- bytes: 319

````rst
.. _example_page:

========
Examples
========

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents:

   examples/queued_io
   examples/stream_io
   examples/single_point_io
   examples/conversion
   examples/can_lin_diff
   examples/programmatic_databases
   examples/dynamic_database_creation
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/index.rst sha256=c146814a84a000d587c8e34418576616f7d174f52fb4a291d1702a01cc68d094 bytes=541 -->
## FILE: docs/index.rst

- repository: `ni/nixnet-python`
- source_path: `docs/index.rst`
- sha256: `c146814a84a000d587c8e34418576616f7d174f52fb4a291d1702a01cc68d094`
- bytes: 541

````rst
.. NI-XNET Python API documentation master file, created by
   sphinx-quickstart on Thu Jun 14 09:40:36 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NI-XNET Python Documentation
============================

.. include:: ../README.rst

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents:

   installation
   api_reference
   examples
   contributing


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/installation.rst sha256=6e1cdc7758894173d8380b7f622db5f7b17931247e18e02b2caf0c98fe17d038 bytes=384 -->
## FILE: docs/installation.rst

- repository: `ni/nixnet-python`
- source_path: `docs/installation.rst`
- sha256: `6e1cdc7758894173d8380b7f622db5f7b17931247e18e02b2caf0c98fe17d038`
- bytes: 384

````rst
Installation
============

Running **nixnet** requires NI-XNET or NI-XNET Runtime. Visit the
`ni.com/downloads <http://www.ni.com/downloads/>`_ to download the latest version
of NI-XNET.

**nixnet** can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nixnet

You also can download the project source and run::

  $ poetry install
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/make.bat sha256=c0755f481bd4cfc4e3ae38c94e92c4af073f8578a0588961a820d6630fbe464e bytes=820 -->
## FILE: docs/make.bat

- repository: `ni/nixnet-python`
- source_path: `docs/make.bat`
- sha256: `c0755f481bd4cfc4e3ae38c94e92c4af073f8578a0588961a820d6630fbe464e`
- bytes: 820

````batch
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ=NI-XNETPythonAPI

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
````

<!--NI_OSS_SOURCE repo=nixnet-python path=docs/Makefile sha256=7d651ba4561256b86821243e3537475589b057cda6050fdd3fb98681464a76d1 bytes=634 -->
## FILE: docs/Makefile

- repository: `ni/nixnet-python`
- source_path: `docs/Makefile`
- sha256: `7d651ba4561256b86821243e3537475589b057cda6050fdd3fb98681464a76d1`
- bytes: 634

````text
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = NI-XNETPythonAPI
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=Jenkinsfile sha256=61da74099c9616e8a6d1f8ed30df8c2e33b11ab95e3cd412d3b0e645651c9423 bytes=1270 -->
## FILE: Jenkinsfile

- repository: `ni/nixnet-python`
- source_path: `Jenkinsfile`
- sha256: `61da74099c9616e8a6d1f8ed30df8c2e33b11ab95e3cd412d3b0e645651c9423`
- bytes: 1270

````text
#!groovy
node('xnetPython') {

	currentBuild.result = "SUCCESS"

	// Environment variables to configure the hardware for testing. This scope applies to all stages
	environment {
		CAN_FIXTURE_IN_INTERFACE = 'CAN1'
		CAN_FIXTURE_OUT_INTERFACE = 'CAN2'
		LIN_FIXTURE_IN_INTERFACE = 'LIN1'
		LIN_FIXTURE_OUT_INTERFACE = 'LIN2'
	}

	try{
		stage('Checkout'){
			// Checkout the repository from scm
			echo "Checking out source"
			checkout scm
		}

		stage('EnvironmentSetup'){
			// Stage to setup environment variables and ensure correct testing environment.
			bat 'pip install --upgrade setuptools'
		}

		stage('Testing'){
			// Run tox with the tox-integration.ini file in the root of the repository
			echo "Running Tox integration script"
			try {
				bat 'tox -c tox-integration.ini -e py39-test -- --can-in-interface CAN1 --can-out-interface CAN2 --lin-in-interface LIN1 --lin-out-interface LIN2'
			} finally {
				step([$class: 'CoberturaPublisher', coberturaReportFile: 'coverage.xml'])
				junit "junit/*.xml"
			}
		}
	}
	catch (err) {
		currentBuild.result = "FAILURE"
		emailextrecipients([[$class: 'CulpritsRecipientProvider'], [$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']])
	}
}
````

<!--NI_OSS_SOURCE repo=nixnet-python path=LICENSE sha256=82f1b99674e46f8e0417fb97370b17f387d3a573e3d22b25256f69d5dc8c194f bytes=1096 -->
## FILE: LICENSE

- repository: `ni/nixnet-python`
- source_path: `LICENSE`
- sha256: `82f1b99674e46f8e0417fb97370b17f387d3a573e3d22b25256f69d5dc8c194f`
- bytes: 1096

````text
Copyright (c) 2017-2025, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=nixnet-python path=MAINTAINING.rst sha256=f82628d989dad8c659f0e2d9fd2a2c8c488afc9c194ecdaf9f245f5bff1596cc bytes=937 -->
## FILE: MAINTAINING.rst

- repository: `ni/nixnet-python`
- source_path: `MAINTAINING.rst`
- sha256: `f82628d989dad8c659f0e2d9fd2a2c8c488afc9c194ecdaf9f245f5bff1596cc`
- bytes: 937

````rst
Maintaining nixnet
==================

Cutting a release
-----------------

Update the version

#. ``pyproject.toml``
#. ``README.rst``
#. Create release notes (`clog-cli <https://github.com/clog-tool/clog-cli/releases>`__ can help)
#. ``git clean -ndx`` to see what files to clean up
#. ``git clean -fdx`` to clean up files
#. Include release notes in commit messaage
#. Publish a PR

Tagging a release

#. (on main) ``git tag -a v<X>.<Y>.<Z>`` with the release notes as the message
#. ``git push <UPSTREAM> main --tag v<X>.<Y>.<Z>``
#. Go to https://github.com/ni/nixnet-python/releases
#. The new release should be there, but it will be poorly formatted.
#. Draft a new release. Use the same tag version. You don't need to attach any new files.

Uploading packages to PyPI

#. ``poetry config pypi-token.pypi <PyPI API token>`` (only need to be done once)
#. ``rm -Rf dist``
#. ``poetry publish --build``
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/__init__.py sha256=3b6f790c4465fed4227f579e14947d4d73b26b3fa90a69d892351a4bee0da5fe bytes=299 -->
## FILE: nixnet/__init__.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/__init__.py`
- sha256: `3b6f790c4465fed4227f579e14947d4d73b26b3fa90a69d892351a4bee0da5fe`
- bytes: 299

````python
import typing  # NOQA: F401

from nixnet.errors import XnetError  # NOQA: F401
from nixnet.errors import XnetResourceWarning  # NOQA: F401
from nixnet.errors import XnetWarning  # NOQA: F401
from nixnet.session import *  # NOQA: F401, F403

__all__ = []  # type: typing.List[typing.Text]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_cconsts.py sha256=fe1480e133cd25fe8e802da94ffd82c9de1196e49f7bbbdd2fc257de98125220 bytes=52513 -->
## FILE: nixnet/_cconsts.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_cconsts.py`
- sha256: `fe1480e133cd25fe8e802da94ffd82c9de1196e49f7bbbdd2fc257de98125220`
- bytes: 52513

````python
NX_STATUS_QUALIFIER = (0x3FF63000)
NX_STATUS_WARNING = (0x00000000)
NX_STATUS_ERROR = (0x80000000)
NX_WARNING_BASE = (NX_STATUS_QUALIFIER | NX_STATUS_WARNING)
NX_ERROR_BASE = (NX_STATUS_QUALIFIER | NX_STATUS_ERROR)

NX_SUCCESS = 0

NX_ERR_INTERNAL_ERROR = (NX_ERROR_BASE | 0x001)
NX_ERR_SELF_TEST_ERROR1 = (NX_ERROR_BASE | 0x002)
NX_ERR_SELF_TEST_ERROR2 = (NX_ERROR_BASE | 0x003)
NX_ERR_SELF_TEST_ERROR3 = (NX_ERROR_BASE | 0x004)
NX_ERR_SELF_TEST_ERROR4 = (NX_ERROR_BASE | 0x005)
NX_ERR_SELF_TEST_ERROR5 = (NX_ERROR_BASE | 0x006)
NX_ERR_POWER_SUSPENDED = (NX_ERROR_BASE | 0x007)
NX_ERR_OUTPUT_QUEUE_OVERFLOW = (NX_ERROR_BASE | 0x008)
NX_ERR_FIRMWARE_NO_RESPONSE = (NX_ERROR_BASE | 0x009)
NX_ERR_EVENT_TIMEOUT = (NX_ERROR_BASE | 0x00A)
NX_ERR_INPUT_QUEUE_OVERFLOW = (NX_ERROR_BASE | 0x00B)
NX_ERR_INPUT_QUEUE_READ_SIZE = (NX_ERROR_BASE | 0x00C)
NX_ERR_DUPLICATE_FRAME_OBJECT = (NX_ERROR_BASE | 0x00D)
NX_ERR_DUPLICATE_STREAM_OBJECT = (NX_ERROR_BASE | 0x00E)
NX_ERR_SELF_TEST_NOT_POSSIBLE = (NX_ERROR_BASE | 0x00F)
NX_ERR_MEMORY_FULL = (NX_ERROR_BASE | 0x010)
NX_ERR_MAX_SESSIONS = (NX_ERROR_BASE | 0x011)
NX_ERR_MAX_FRAMES = (NX_ERROR_BASE | 0x012)
NX_ERR_MAX_DEVICES = (NX_ERROR_BASE | 0x013)
NX_ERR_MISSING_FILE = (NX_ERROR_BASE | 0x014)
NX_ERR_PARAMETER_NULL_OR_EMPTY = (NX_ERROR_BASE | 0x015)
NX_ERR_MAX_SCHEDULES = (NX_ERROR_BASE | 0x016)
NX_ERR_SELF_TEST_ERROR6 = (NX_ERROR_BASE | 0x017)
NX_ERR_SELF_TEST_IN_PROGRESS = (NX_ERROR_BASE | 0x018)
NX_ERR_INVALID_SESSION_HANDLE = (NX_ERROR_BASE | 0x020)
NX_ERR_INVALID_SYSTEM_HANDLE = (NX_ERROR_BASE | 0x021)
NX_ERR_DEVICE_HANDLE_EXPECTED = (NX_ERROR_BASE | 0x022)
NX_ERR_INTF_HANDLE_EXPECTED = (NX_ERROR_BASE | 0x023)
NX_ERR_PROPERTY_MODE_CONFLICTING = (NX_ERROR_BASE | 0x024)
NX_ERR_TIMING_SOURCE_NOT_SUPPORTED = (NX_ERROR_BASE | 0x025)
NX_ERR_MULTIPLE_TIMING_SOURCE = (NX_ERROR_BASE | 0x026)
NX_ERR_OVERLAPPING_IO = (NX_ERROR_BASE | 0x027)
NX_ERR_MISSING_BUS_POWER = (NX_ERROR_BASE | 0x028)
NX_ERR_CDAQ_CONNECTION_LOST = (NX_ERROR_BASE | 0x029)
NX_ERR_INVALID_TRANSCEIVER = (NX_ERROR_BASE | 0x071)
NX_ERR_INVALID_BAUD_RATE = (NX_ERROR_BASE | 0x072)
NX_ERR_BAUD_RATE_NOT_CONFIGURED = (NX_ERROR_BASE | 0x073)
NX_ERR_INVALID_BIT_TIMINGS = (NX_ERROR_BASE | 0x074)
NX_ERR_BAUD_RATE_XCVR_MISMATCH = (NX_ERROR_BASE | 0x075)
NX_ERR_UNKNOWN_TIMING_SOURCE = (NX_ERROR_BASE | 0x076)
NX_ERR_UNKNOWN_SYNCHRONIZATION_SOURCE = (NX_ERROR_BASE | 0x077)
NX_ERR_MISSING_TIMEBASE_SOURCE = (NX_ERROR_BASE | 0x078)
NX_ERR_UNKNOWN_TIMEBASE_FREQUENCY = (NX_ERROR_BASE | 0x079)
NX_ERR_UNCONNECTED_SYNCHRONIZATION_SOURCE = (NX_ERROR_BASE | 0x07A)
NX_ERR_CONNECTED_SYNCHRONIZATION_TERMINAL = (NX_ERROR_BASE | 0x07B)
NX_ERR_INVALID_SYNCHRONIZATION_SOURCE = (NX_ERROR_BASE | 0x07C)
NX_ERR_INVALID_SYNCHRONIZATION_DESTINATION = (NX_ERROR_BASE | 0x07D)
NX_ERR_INVALID_SYNCHRONIZATION_COMBINATION = (NX_ERROR_BASE | 0x07E)
NX_ERR_TIMEBASE_DISAPPEARED = (NX_ERROR_BASE | 0x07F)
NX_ERR_MACROTICK_DISCONNECTED = (NX_ERROR_BASE | 0x080)
NX_ERR_CANNOT_OPEN_DATABASE_FILE = (NX_ERROR_BASE | 0x081)
NX_ERR_CLUSTER_NOT_FOUND = (NX_ERROR_BASE | 0x082)
NX_ERR_FRAME_NOT_FOUND = (NX_ERROR_BASE | 0x083)
NX_ERR_SIGNAL_NOT_FOUND = (NX_ERROR_BASE | 0x084)
NX_ERR_UNCONFIGURED_CLUSTER = (NX_ERROR_BASE | 0x085)
NX_ERR_UNCONFIGURED_FRAME = (NX_ERROR_BASE | 0x086)
NX_ERR_UNCONFIGURED_SIGNAL = (NX_ERROR_BASE | 0x087)
NX_ERR_MULTIPLE_CLUSTERS = (NX_ERROR_BASE | 0x088)
NX_ERR_SUBORDINATE_NOT_ALLOWED = (NX_ERROR_BASE | 0x089)
NX_ERR_INVALID_INTERFACE = (NX_ERROR_BASE | 0x08A)
NX_ERR_INVALID_PROTOCOL = (NX_ERROR_BASE | 0x08B)
NX_ERR_INPUT_SESSION_MUST_AUTO_START = (NX_ERROR_BASE | 0x08C)
NX_ERR_INVALID_PROPERTY_ID = (NX_ERROR_BASE | 0x08D)
NX_ERR_INVALID_PROPERTY_SIZE = (NX_ERROR_BASE | 0x08E)
NX_ERR_INCORRECT_MODE = (NX_ERROR_BASE | 0x08F)
NX_ERR_BUFFER_TOO_SMALL = (NX_ERROR_BASE | 0x090)
NX_ERR_MUST_SPECIFY_MULTIPLEXERS = (NX_ERROR_BASE | 0x091)
NX_ERR_SESSION_NOT_FOUND = (NX_ERROR_BASE | 0x092)
NX_ERR_MULTIPLE_USE_OF_SESSION = (NX_ERROR_BASE | 0x093)
NX_ERR_ONLY_ONE_FRAME = (NX_ERROR_BASE | 0x094)
NX_ERR_DUPLICATE_ALIAS = (NX_ERROR_BASE | 0x095)
NX_ERR_DEPLOYMENT_IN_PROGRESS = (NX_ERROR_BASE | 0x096)
NX_ERR_NO_FRAMES_OR_SIGNALS = (NX_ERROR_BASE | 0x097)
NX_ERR_INVALID_MODE = (NX_ERROR_BASE | 0x098)
NX_ERR_NEED_REFERENCE = (NX_ERROR_BASE | 0x099)
NX_ERR_DIFFERENT_CLUSTER_OPEN = (NX_ERROR_BASE | 0x09A)
NX_ERR_FLEX_RAY_INVALID_CYCLE_REP = (NX_ERROR_BASE | 0x09B)
NX_ERR_SESSION_CLEARED = (NX_ERROR_BASE | 0x09C)
NX_ERR_WRONG_MODE_FOR_CREATE_SELECTION = (NX_ERROR_BASE | 0x09D)
NX_ERR_INTERFACE_RUNNING = (NX_ERROR_BASE | 0x09E)
NX_ERR_FRAME_WRITE_TOO_LARGE = (NX_ERROR_BASE | 0x09F)
NX_ERR_TIMEOUT_WITHOUT_NUM_TO_READ = (NX_ERROR_BASE | 0x0A0)
NX_ERR_TIMESTAMPS_NOT_SUPPORTED = (NX_ERROR_BASE | 0x0A1)
NX_ERR_UNKNOWN_CONDITION = (NX_ERROR_BASE | 0x0A2)
NX_ERR_SESSION_NOT_STARTED = (NX_ERROR_BASE | 0x0A3)
NX_ERR_MAX_WAITS_EXCEEDED = (NX_ERROR_BASE | 0x0A4)
NX_ERR_INVALID_DEVICE = (NX_ERROR_BASE | 0x0A5)
NX_ERR_INVALID_TERMINAL_NAME = (NX_ERROR_BASE | 0x0A6)
NX_ERR_PORT_LE_DS_BUSY = (NX_ERROR_BASE | 0x0A7)
NX_ERR_INVALID_KEYSLOT = (NX_ERROR_BASE | 0x0A8)
NX_ERR_MAX_QUEUE_SIZE_EXCEEDED = (NX_ERROR_BASE | 0x0A9)
NX_ERR_FRAME_SIZE_MISMATCH = (NX_ERROR_BASE | 0x0AA)
NX_ERR_INDEX_TOO_BIG = (NX_ERROR_BASE | 0x0AB)
NX_ERR_SESSION_MODE_INCOMPATIBILITY = (NX_ERROR_BASE | 0x0AC)
NX_ERR_TRIGGER_SIGNAL_NOT_ALLOWED = (NX_ERROR_BASE | 0x0AD)
NX_ERR_ONLY_ONE_CLUSTER = (NX_ERROR_BASE | 0x0AE)
NX_ERR_CONVERT_INVALID_PAYLOAD = (NX_ERROR_BASE | 0x0AF)
NX_ERR_MEMORY_FULL_READ_DATA = (NX_ERROR_BASE | 0x0B0)
NX_ERR_MEMORY_FULL_FIRMWARE = (NX_ERROR_BASE | 0x0B1)
NX_ERR_COMMUNICATION_LOST = (NX_ERROR_BASE | 0x0B2)
NX_ERR_INVALID_PRIORITY = (NX_ERROR_BASE | 0x0B3)
NX_ERR_SYNCHRONIZATION_NOT_ALLOWED = (NX_ERROR_BASE | 0x0B4)
NX_ERR_TIME_NOT_REACHED = (NX_ERROR_BASE | 0x0B5)
NX_ERR_INTERNAL_INPUT_QUEUE_OVERFLOW = (NX_ERROR_BASE | 0x0B6)
NX_ERR_BAD_IMAGE_FILE = (NX_ERROR_BASE | 0x0B7)
NX_ERR_INVALID_LOGFILE = (NX_ERROR_BASE | 0x0B8)
NX_ERR_DONGLE_COMMUNICATION_LOST = (NX_ERROR_BASE | 0xB9)
NX_ERR_LOW_LEVEL_COMMUNICATION_TIMEOUT = (NX_ERROR_BASE | 0xBA)
NX_ERR_CDAQ_TRANSFER_ABORTED = (NX_ERROR_BASE | 0xBB)
NX_ERR_INVALID_PROPERTY_VALUE = (NX_ERROR_BASE | 0x0C0)
NX_ERR_FLEX_RAY_INTEGRATION_FAILED = (NX_ERROR_BASE | 0x0C1)
NX_ERR_PDU_NOT_FOUND = (NX_ERROR_BASE | 0x0D0)
NX_ERR_UNCONFIGURED_PDU = (NX_ERROR_BASE | 0x0D1)
NX_ERR_DUPLICATE_PDU_OBJECT = (NX_ERROR_BASE | 0x0D2)
NX_ERR_NEED_PDU = (NX_ERROR_BASE | 0x0D3)
NX_ERR_RPC_COMMUNICATION = (NX_ERROR_BASE | 0x100)
NX_ERR_FILE_TRANSFER_COMMUNICATION = (NX_ERROR_BASE | 0x101)
NX_ERR_FTP_COMMUNICATION = (NX_ERROR_BASE | 0x101)
NX_ERR_FILE_TRANSFER_ACCESS = (NX_ERROR_BASE | 0x102)
NX_ERR_FTP_FILE_ACCESS = (NX_ERROR_BASE | 0x102)
NX_ERR_DATABASE_ALREADY_IN_USE = (NX_ERROR_BASE | 0x103)
NX_ERR_INTERNAL_FILE_ACCESS = (NX_ERROR_BASE | 0x104)
NX_ERR_FILE_TRANSFER_ACTIVE = (NX_ERROR_BASE | 0x105)
NX_ERR_DLL_LOAD = (NX_ERROR_BASE | 0x117)
NX_ERR_OBJECT_STARTED = (NX_ERROR_BASE | 0x11E)
NX_ERR_DEFAULT_PAYLOAD_NUM_BYTES = (NX_ERROR_BASE | 0x11F)
NX_ERR_INVALID_ARBITRATION_ID = (NX_ERROR_BASE | 0x123)
NX_ERR_INVALID_LIN_ID = (NX_ERROR_BASE | 0x124)
NX_ERR_TOO_MANY_OPEN_FILES = (NX_ERROR_BASE | 0x130)
NX_ERR_DATABASE_BAD_REFERENCE = (NX_ERROR_BASE | 0x131)
NX_ERR_CREATE_DATABASE_FILE = (NX_ERROR_BASE | 0x132)
NX_ERR_DUPLICATE_CLUSTER_NAME = (NX_ERROR_BASE | 0x133)
NX_ERR_DUPLICATE_FRAME_NAME = (NX_ERROR_BASE | 0x134)
NX_ERR_DUPLICATE_SIGNAL_NAME = (NX_ERROR_BASE | 0x135)
NX_ERR_DUPLICATE_ECU_NAME = (NX_ERROR_BASE | 0x136)
NX_ERR_DUPLICATE_SUBFRAME_NAME = (NX_ERROR_BASE | 0x137)
NX_ERR_IMPROPER_PROTOCOL = (NX_ERROR_BASE | 0x138)
NX_ERR_OBJECT_RELATION = (NX_ERROR_BASE | 0x139)
NX_ERR_UNCONFIGURED_REQUIRED_PROPERTY = (NX_ERROR_BASE | 0x13B)
NX_ERR_NOT_SUPPORTED_ON_RT = (NX_ERROR_BASE | 0x13C)
NX_ERR_NAME_SYNTAX = (NX_ERROR_BASE | 0x13D)
NX_ERR_FILE_EXTENSION = (NX_ERROR_BASE | 0x13E)
NX_ERR_DATABASE_OBJECT_NOT_FOUND = (NX_ERROR_BASE | 0x13F)
NX_ERR_REMOVE_DATABASE_CACHE_FILE = (NX_ERROR_BASE | 0x140)
NX_ERR_READ_ONLY_PROPERTY = (NX_ERROR_BASE | 0x141)
NX_ERR_FRAME_MUX_EXISTS = (NX_ERROR_BASE | 0x142)
NX_ERR_UNDEFINED_FIRST_SLOT = (NX_ERROR_BASE | 0x144)
NX_ERR_UNDEFINED_FIRST_CHANNELS = (NX_ERROR_BASE | 0x145)
NX_ERR_UNDEFINED_PROTOCOL = (NX_ERROR_BASE | 0x146)
NX_ERR_OLD_DATABASE_CACHE_FILE = (NX_ERROR_BASE | 0x147)
NX_ERR_DB_CONFIG_SIG_OUT_OF_FRAME = (NX_ERROR_BASE | 0x148)
NX_ERR_DB_CONFIG_SIG_OVERLAPPED = (NX_ERROR_BASE | 0x149)
NX_ERR_DB_CONFIG_SIG52_BIT_INTEGER = (NX_ERROR_BASE | 0x14A)
NX_ERR_DB_CONFIG_FRAME_NUM_BYTES = (NX_ERROR_BASE | 0x14B)
NX_ERR_MULT_SYNC_STARTUP = (NX_ERROR_BASE | 0x14C)
NX_ERR_INVALID_CLUSTER = (NX_ERROR_BASE | 0x14D)
NX_ERR_DATABASE_NAME = (NX_ERROR_BASE | 0x14E)
NX_ERR_DATABASE_OBJECT_LOCKED = (NX_ERROR_BASE | 0x14F)
NX_ERR_ALIAS_NOT_FOUND = (NX_ERROR_BASE | 0x150)
NX_ERR_CLUSTER_FRAME_CHANNEL_RELATION = (NX_ERROR_BASE | 0x151)
NX_ERR_DYN_FLEX_RAY_FRAME_CHAN_AAND_B = (NX_ERROR_BASE | 0x152)
NX_ERR_DATABASE_LOCKED_IN_USE = (NX_ERROR_BASE | 0x153)
NX_ERR_AMBIGUOUS_FRAME_NAME = (NX_ERROR_BASE | 0x154)
NX_ERR_AMBIGUOUS_SIGNAL_NAME = (NX_ERROR_BASE | 0x155)
NX_ERR_AMBIGUOUS_ECU_NAME = (NX_ERROR_BASE | 0x156)
NX_ERR_AMBIGUOUS_SUBFRAME_NAME = (NX_ERROR_BASE | 0x157)
NX_ERR_AMBIGUOUS_SCHEDULE_NAME = (NX_ERROR_BASE | 0x158)
NX_ERR_DUPLICATE_SCHEDULE_NAME = (NX_ERROR_BASE | 0x159)
NX_ERR_PROTOCOL_MUX_NOT_SUPPORTED = (NX_ERROR_BASE | 0x15A)
NX_ERR_SAVE_LI_NNOT_SUPPORTED = (NX_ERROR_BASE | 0x15B)
NX_ERR_LI_NMASTER_NOT_DEFINED = (NX_ERROR_BASE | 0x15C)
NX_ERR_SESSION_TYPE_FRAME_INCOMPATIBILITY = (NX_ERROR_BASE | 0x15D)
NX_ERR_MIX_AUTO_MANUAL_OPEN = (NX_ERROR_BASE | 0x15E)
NX_ERR_AUTO_OPEN_NOT_SUPPORTED = (NX_ERROR_BASE | 0x15F)
NX_ERR_WRONG_NUM_SIGNALS_WRITTEN = (NX_ERROR_BASE | 0x160)
NX_ERR_MULTIPLE_LV_PROJECT = (NX_ERROR_BASE | 0x161)
NX_ERR_SESSION_CONFLICT_LV_PROJECT = (NX_ERROR_BASE | 0x162)
NX_ERR_DB_OBJECT_NAME_EMPTY = (NX_ERROR_BASE | 0x163)
NX_ERR_MISSING_ALIAS_IN_DB_OBJECT_NAME = (NX_ERROR_BASE | 0x164)
NX_ERR_DATABASE_IMPORT_VERSION = (NX_ERROR_BASE | 0x165)
NX_ERR_FIBEX_IMPORT_VERSION = (NX_ERROR_BASE | 0x165)
NX_ERR_EMPTY_SESSION_NAME = (NX_ERROR_BASE | 0x166)
NX_ERR_NOT_ENOUGH_MESSAGE_RAM_FOR_OBJECT = (NX_ERROR_BASE | 0x167)
NX_ERR_KEY_SLOT_ID_CONFIG = (NX_ERROR_BASE | 0x168)
NX_ERR_UNSUPPORTED_SESSION = (NX_ERROR_BASE | 0x169)
NX_ERR_OBJECT_CREATED_AFTER_START = (NX_ERROR_BASE | 0x170)
NX_ERR_SINGLE_SLOT_ENABLED_AFTER_START = (NX_ERROR_BASE | 0x171)
NX_ERR_UNSUPPORTED_NUM_MACROTICKS = (NX_ERROR_BASE | 0x172)
NX_ERR_BAD_SYNTAX_IN_DATABASE_OBJECT_NAME = (NX_ERROR_BASE | 0x173)
NX_ERR_AMBIGUOUS_SCHEDULE_ENTRY_NAME = (NX_ERROR_BASE | 0x174)
NX_ERR_DUPLICATE_SCHEDULE_ENTRY_NAME = (NX_ERROR_BASE | 0x175)
NX_ERR_UNDEFINED_FRAME_ID = (NX_ERROR_BASE | 0x176)
NX_ERR_UNDEFINED_FRAME_PAYLOAD_LENGTH = (NX_ERROR_BASE | 0x177)
NX_ERR_UNDEFINED_SIGNAL_START_BIT = (NX_ERROR_BASE | 0x178)
NX_ERR_UNDEFINED_SIGNAL_NUM_BITS = (NX_ERROR_BASE | 0x179)
NX_ERR_UNDEFINED_SIGNAL_BYTE_ORDER = (NX_ERROR_BASE | 0x17A)
NX_ERR_UNDEFINED_SIGNAL_DATA_TYPE = (NX_ERROR_BASE | 0x17B)
NX_ERR_UNDEFINED_SUBF_MUX_VALUE = (NX_ERROR_BASE | 0x17C)
NX_ERR_INVALID_LIN_SCHED_INDEX = (NX_ERROR_BASE | 0x17D)
NX_ERR_INVALID_LIN_SCHED_NAME = (NX_ERROR_BASE | 0x17E)
NX_ERR_INVALID_ACTIVE_FRAME_INDEX = (NX_ERROR_BASE | 0x17F)
NX_ERR_INVALID_ACTIVE_FRAME_NAME = (NX_ERROR_BASE | 0x180)
NX_ERR_AMBIGUOUS_PDU = (NX_ERROR_BASE | 0x181)
NX_ERR_DUPLICATE_PDU = (NX_ERROR_BASE | 0x182)
NX_ERR_NUMBER_OF_PD_US = (NX_ERROR_BASE | 0x183)
NX_ERR_PD_US_REQUIRED = (NX_ERROR_BASE | 0x184)
NX_ERR_MAX_PD_US = (NX_ERROR_BASE | 0x185)
NX_ERR_UNSUPPORTED_MODE = (NX_ERROR_BASE | 0x186)
NX_ERR_BAD_FPGA_SIGNATURE = (NX_ERROR_BASE | 0x187)
NX_ERR_BADC_SERIES_FPGA_SIGNATURE = (NX_ERR_BAD_FPGA_SIGNATURE)
NX_ERR_BAD_FPGA_REVISION = (NX_ERROR_BASE | 0x188)
NX_ERR_BADC_SERIES_FPGA_REVISION = (NX_ERR_BAD_FPGA_REVISION)
NX_ERR_BAD_FPGA_REVISION_ON_TARGET = (NX_ERROR_BASE | 0x189)
NX_ERR_ROUTE_IN_USE = (NX_ERROR_BASE | 0x18A)
NX_ERR_DA_QMX_INCORRECT_VERSION = (NX_ERROR_BASE | 0x18B)
NX_ERR_ADD_ROUTE = (NX_ERROR_BASE | 0x18C)
NX_ERR_REMOTE_SLEEP_ON_LIN_SLAVE = (NX_ERROR_BASE | 0x18D)
NX_ERR_SLEEP_WAKEUP_NOT_SUPPORTED = (NX_ERROR_BASE | 0x18E)
NX_ERR_DIAGNOSTIC_SCHEDULE_NOT_DEFINED = (NX_ERROR_BASE | 0x18F)
NX_ERR_LIN_TRANSPORT_LAYER = (NX_ERROR_BASE | 0x192)
NX_ERR_LOGFILE = (NX_ERROR_BASE | 0x193)
NX_ERR_STRM_OUT_TMG_LIN_SCHEDULER_CONFLICT = (NX_ERROR_BASE | 0x200)
NX_ERR_SESSN_TYPE_LIN_INTF_PRS_INCOMPATIBLE = (NX_ERROR_BASE | 0x201)
NX_ERR_SAVE_CLUSTER_ONLY = (NX_ERROR_BASE | 0x202)
NX_ERR_SAVE_LDF_CLUSTER_ONLY = NX_ERR_SAVE_CLUSTER_ONLY
NX_ERR_DUPLICATE_INTERFACE_NAME = (NX_ERROR_BASE | 0x203)
NX_ERR_INCOMPATIABLE_TRANSCEIVER_REVISION = (NX_ERROR_BASE | 0x204)
NX_ERR_INCOMPATIABLE_TRANSCEIVER_IMAGE = (NX_ERROR_BASE | 0x205)
NX_ERR_PROPERTY_NOTSUPPORTED = (NX_ERROR_BASE | 0x206)
NX_ERR_EXPORT_SEMANTIC = (NX_ERROR_BASE | 0x207)
NX_ERR_J1939_QUEUE_OVERFLOW = (NX_ERROR_BASE | 0x0208)
NX_ERR_NON_J1939_FRAME_SIZE = (NX_ERROR_BASE | 0x0209)
NX_ERR_J1939_MISSING_ADDRESS = (NX_ERROR_BASE | 0x020A)
NX_ERR_J1939_ADDRESS_LOST = (NX_ERROR_BASE | 0x020B)
NX_ERR_J1939_CTS_NEXT_PCK_LARGER_TOTAL_PCK_NUM = (NX_ERROR_BASE | 0x020C)
NX_ERR_J1939_CTS_NEXT_PCK = (NX_ERROR_BASE | 0x020D)
NX_ERR_J1939_CTS_NEXT_PCK_NULL = (NX_ERROR_BASE | 0x020E)
NX_ERR_J1939_CTS_PGN = (NX_ERROR_BASE | 0x020F)
NX_ERR_J1939_UNEXPECTED_SEQ_NUM = (NX_ERROR_BASE | 0x0210)
NX_ERR_J1939_MORE_PCK_REQ_THAN_ALLOWED = (NX_ERROR_BASE | 0x0211)
NX_ERR_J1939_TIMEOUT_T1 = (NX_ERROR_BASE | 0x0212)
NX_ERR_J1939_TIMEOUT_T2 = (NX_ERROR_BASE | 0x0213)
NX_ERR_J1939_TIMEOUT_T3 = (NX_ERROR_BASE | 0x0214)
NX_ERR_J1939_TIMEOUT_T4 = (NX_ERROR_BASE | 0x0215)
NX_ERR_J1939_RTS_DLC = (NX_ERROR_BASE | 0x0216)
NX_ERR_J1939_CTS_DLC = (NX_ERROR_BASE | 0x0217)
NX_ERR_J1939_BAM_DLC = (NX_ERROR_BASE | 0x0218)
NX_ERR_J1939_DT_DLC = (NX_ERROR_BASE | 0x0219)
NX_ERR_J1939_ABORT_DLC = (NX_ERROR_BASE | 0x021A)
NX_ERR_J1939_EOMA_DLC = (NX_ERROR_BASE | 0x021B)
NX_ERR_J1939_ABORT_PGN = (NX_ERROR_BASE | 0x021C)
NX_ERR_J1939_CTS_HOLD_MSG = (NX_ERROR_BASE | 0x021D)
NX_ERR_J1939_INVALID_TOTAL_SIZE = (NX_ERROR_BASE | 0x021E)
NX_ERR_J1939_TOTAL_PCK_NUM = (NX_ERROR_BASE | 0x021F)
NX_ERR_J1939_RESERVED_DATA = (NX_ERROR_BASE | 0x0220)
NX_ERR_J1939_NOT_ENOUGH_SYS_RES = (NX_ERROR_BASE | 0x0221)
NX_ERR_J1939_ABORT_MSG_ACTIVE_CONNECTION = (NX_ERROR_BASE | 0x0222)
NX_ERR_J1939_ABORT_MSG_NOT_ENOUGH_SYS_RES = (NX_ERROR_BASE | 0x0223)
NX_ERR_J1939_ABORT_MSG_TIMEOUT = (NX_ERROR_BASE | 0x0224)
NX_ERR_J1939_ABORT_MSG_CTS_REC = (NX_ERROR_BASE | 0x0225)
NX_ERR_J1939_ABORT_MSG_MAX_RETRANSMIT = (NX_ERROR_BASE | 0x0226)
NX_ERR_RPC_VERSION = (NX_ERROR_BASE | 0x0227)
NX_ERR_FRAME_CAN_IO_MODE = (NX_ERROR_BASE | 0x0228)
NX_ERR_INCOMPATIBLE_FLASH = (NX_ERROR_BASE | 0x0229)
NX_ERR_TX_IO_MODE = (NX_ERROR_BASE | 0x022A)
NX_ERR_XS_DONGLE_UNSUPPORTED_BOARD = (NX_ERROR_BASE | 0x022B)
NX_ERR_INVALID_CHAR_IN_DATABASE_ALIAS = (NX_ERROR_BASE | 0x022C)
NX_ERR_INVALID_CHAR_IN_DATABASE_FILEPATH = (NX_ERROR_BASE | 0x022D)
NX_ERR_INVALID_CAN_FD_PORT_TYPE = (NX_ERROR_BASE | 0x022E)
NX_ERR_INV_UNCONDITIONAL_ENTRY = (NX_ERROR_BASE | 0x022F)
NX_ERR_EVENT_ENTRY_NO_SCHEDULE = (NX_ERROR_BASE | 0x0230)
NX_ERR_UNSUPPORTED_USB_SPEED = (NX_ERROR_BASE | 0x0231)
NX_ERR_EVENT_UNEQUAL_PAYLOAD_LENGTH = (NX_ERROR_BASE | 0x0232)
NX_ERR_EVENT_UNEQUAL_CHECKSUM_TYPE = (NX_ERROR_BASE | 0x0233)
NX_ERR_CRIO_BAD_DRIVER_VERSIONS = (NX_ERROR_BASE | 0x0234)
NX_ERR_CRIO_MISSING_SLOT_SUPPORT = (NX_ERROR_BASE | 0x0235)
NX_ERR_INTF_ALREADY_IN_USE_BY_NI_XNET = (NX_ERROR_BASE | 0x0236)
NX_ERR_INTF_ALREADY_IN_USE_BY_NI_XCL = (NX_ERROR_BASE | 0x0237)
NX_ERR_BYTE_ARRAY_NOT_ALLOWED = (NX_ERROR_BASE | 0x0238)
NX_ERR_NO_BYTE_ARRAY_MIX = (NX_ERROR_BASE | 0x0239)
NX_ERR_ONLY_ONE_BYTE_ARRAY = (NX_ERROR_BASE | 0x023A)

NX_WARN_FD_BAUD_EXCEEDS_CAPABILITY = (NX_WARNING_BASE | 0x040)
NX_WARN_DATABASE_IMPORT = (NX_WARNING_BASE | 0x085)
NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE = (NX_WARNING_BASE | 0x086)
NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE_PLUS_WARNING = (NX_WARNING_BASE | 0x087)
NX_WARN_DATABASE_BAD_REFERENCE = (NX_WARNING_BASE | 0x131)
NX_WARN_ADVANCED_PDU = (NX_WARNING_BASE | 0x132)
NX_WARN_MUX_EXCEEDS16_BIT = (NX_WARNING_BASE | 0x133)

NX_CLASS_DATABASE = 0x00000000
NX_CLASS_CLUSTER = 0x00010000
NX_CLASS_FRAME = 0x00020000
NX_CLASS_SIGNAL = 0x00030000
NX_CLASS_SUBFRAME = 0x00040000
NX_CLASS_ECU = 0x00050000
NX_CLASS_LIN_SCHED = 0x00060000
NX_CLASS_LIN_SCHED_ENTRY = 0x00070000
NX_CLASS_PDU = 0x00080000
NX_CLASS_SESSION = 0x00100000
NX_CLASS_SYSTEM = 0x00110000
NX_CLASS_DEVICE = 0x00120000
NX_CLASS_INTERFACE = 0x00130000
NX_CLASS_ALIAS = 0x00140000
NX_CLASS_MASK = 0x00FF0000

NX_PRPTYPE_U32 = 0x00000000
NX_PRPTYPE_F64 = 0x01000000
NX_PRPTYPE_BOOL = 0x02000000
NX_PRPTYPE_STRING = 0x03000000
NX_PRPTYPE_1_DSTRING = 0x04000000
NX_PRPTYPE_REF = 0x05000000
NX_PRPTYPE_1_DREF = 0x06000000
NX_PRPTYPE_TIME = 0x07000000
NX_PRPTYPE_1_DU32 = 0x08000000
NX_PRPTYPE_U64 = 0x09000000
NX_PRPTYPE_1_DU8 = 0x0A000000
NX_PRPTYPE_MASK = 0xFF000000

NX_PROP_SESSION_APPLICATION_PROTOCOL = (0x00000091 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_AUTO_START = (0x00000001 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_CLUSTER_NAME = (0x0000000A | NX_CLASS_SESSION | NX_PRPTYPE_STRING)
NX_PROP_SESSION_DATABASE_NAME = (0x00000002 | NX_CLASS_SESSION | NX_PRPTYPE_STRING)
NX_PROP_SESSION_LIST = (0x00000003 | NX_CLASS_SESSION | NX_PRPTYPE_1_DSTRING)
NX_PROP_SESSION_MODE = (0x00000004 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_NUM_FRAMES = (0x0000000D | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_NUM_IN_LIST = (0x00000005 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_NUM_PEND = (0x00000006 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_NUM_UNUSED = (0x0000000B | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_PAYLD_LEN_MAX = (0x00000009 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_PROTOCOL = (0x00000008 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_QUEUE_SIZE = (0x0000000C | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_RESAMP_RATE = (0x00000007 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_INTF_BAUD_RATE = (0x00000016 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_BAUD_RATE64 = (0x00000016 | NX_CLASS_SESSION | NX_PRPTYPE_U64)
NX_PROP_SESSION_INTF_BUS_ERR_TO_IN_STRM = (0x00000015 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_ECHO_TX = (0x00000010 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_NAME = (0x00000013 | NX_CLASS_SESSION | NX_PRPTYPE_STRING)
NX_PROP_SESSION_INTF_OUT_STRM_LIST = (0x00000011 | NX_CLASS_SESSION | NX_PRPTYPE_1_DREF)
NX_PROP_SESSION_INTF_OUT_STRM_TIMNG = (0x00000012 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_START_TRIG_TO_IN_STRM = (0x00000014 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_EXT_TCVR_CONFIG = (0x00000023 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_LSTN_ONLY = (0x00000022 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_PEND_TX_ORDER = (0x00000020 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_SING_SHOT = (0x00000024 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_TERM = (0x00000025 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_TCVR_STATE = (0x00000028 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_TCVR_TYPE = (0x00000029 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_OUT_STRM_LIST_BY_ID = (0x00000021 | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_CAN_IO_MODE = (0x00000026 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE = (0x00000027 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE64 = (0x00000027 | NX_CLASS_SESSION | NX_PRPTYPE_U64)
NX_PROP_SESSION_INTF_CAN_TX_IO_MODE = (0x00000039 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_CAN_FD_ISO_MODE = (0x0000003E | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_ACC_START_RNG = (0x00000030 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_ALW_HLT_CLK = (0x00000031 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_ALW_PASS_ACT = (0x00000032 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP = (0x0000003A | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP = (0x00000033 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_COLDSTART = (0x00000034 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_DEC_CORR = (0x00000035 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_A = (0x00000036 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_B = (0x00000037 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID = (0x00000038 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_LATEST_TX = (0x00000041 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_LIST_TIMO = (0x00000042 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A = (0x00000043 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B = (0x00000044 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A = (0x00000045 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B = (0x00000046 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MAX_DRIFT = (0x00000047 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_MICROTICK = (0x00000048 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM = (0x00000049 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR = (0x00000058 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR_OUT = (0x00000050 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR = (0x00000059 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR_OUT = (0x00000052 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO = (0x00000053 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_SING_SLOT_EN = (0x00000054 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_STATISTICS_EN = (0x0000005A | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM = (0x0000003D | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_EVEN = (0x0000005B | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_ODD = (0x0000005C | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_EVEN = (0x0000005D | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_ODD = (0x0000005E | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_STATUS = (0x0000005F | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_TERM = (0x00000057 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_CH = (0x00000055 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_PTRN = (0x00000056 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_SLEEP = (0x0000003B | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_FLEX_RAY_CONNECTED_CHS = (0x0000003C | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_LIN_BREAK_LENGTH = (0x00000070 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_LIN_MASTER = (0x00000072 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_LIN_SCHED_NAMES = (0x00000075 | NX_CLASS_SESSION | NX_PRPTYPE_1_DSTRING)
NX_PROP_SESSION_INTF_LIN_SLEEP = (0x00000073 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_LIN_TERM = (0x00000074 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_INTF_LIN_DIAG_P_2MIN = (0x00000077 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_INTF_LIN_DIAG_S_TMIN = (0x00000076 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_INTF_LIN_ALW_START_WO_BUS_PWR = (0x00000078 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD = (0x00000079 | NX_CLASS_SESSION | NX_PRPTYPE_1_DU32)
NX_PROP_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM = (0x00000080 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_LIN_CHECKSUM_TO_IN_STRM = (0x00000081 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_SRC_TERM_START_TRIGGER = (0x00000090 | NX_CLASS_SESSION | NX_PRPTYPE_STRING)
NX_PROP_SESSION_J1939_ADDRESS = (0x00000092 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_NAME = (0x00000094 | NX_CLASS_SESSION | NX_PRPTYPE_U64)
NX_PROP_SESSION_J1939_ECU = (0x00000093 | NX_CLASS_SESSION | NX_PRPTYPE_REF)
NX_PROP_SESSION_J1939_TIMEOUT_T1 = (0x00000095 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_TIMEOUT_T2 = (0x00000096 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_TIMEOUT_T3 = (0x00000097 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_TIMEOUT_T4 = (0x00000098 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_SD = (0x00000099 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_GD = (0x0000009A | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_HOLD_TIME_TH = (0x0000009B | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_J1939_NUM_PACKETS_RECV = (0x0000009C | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_NUM_PACKETS_RESP = (0x0000009D | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_MAX_REPEAT_CTS = (0x0000009E | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_FILL_BYTE = (0x0000009F | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_WRITE_QUEUE_SIZE = (0x000000A0 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_J1939_ECU_BUSY = (0x000000A1 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_J1939_INCLUDE_DEST_ADDR_IN_PGN = (0x000000A5 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_EDGE_FILTER = (0x000000A2 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_TRANSMIT_PAUSE = (0x000000A3 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)
NX_PROP_SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING = (0x000000A4 | NX_CLASS_SESSION | NX_PRPTYPE_BOOL)

NX_PROP_SYS_DEV_REFS = (0x00000002 | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)
NX_PROP_SYS_INTF_REFS = (0x00000003 | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)
NX_PROP_SYS_INTF_REFS_CAN = (0x00000004 | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)
NX_PROP_SYS_INTF_REFS_FLEX_RAY = (0x00000005 | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)
NX_PROP_SYS_INTF_REFS_LIN = (0x00000007 | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)
NX_PROP_SYS_VER_BUILD = (0x00000006 | NX_CLASS_SYSTEM | NX_PRPTYPE_U32)
NX_PROP_SYS_VER_MAJOR = (0x00000008 | NX_CLASS_SYSTEM | NX_PRPTYPE_U32)
NX_PROP_SYS_VER_MINOR = (0x00000009 | NX_CLASS_SYSTEM | NX_PRPTYPE_U32)
NX_PROP_SYS_VER_PHASE = (0x0000000A | NX_CLASS_SYSTEM | NX_PRPTYPE_U32)
NX_PROP_SYS_VER_UPDATE = (0x0000000B | NX_CLASS_SYSTEM | NX_PRPTYPE_U32)
NX_PROP_SYS_INTF_REFS_ALL = (0x0000000D | NX_CLASS_SYSTEM | NX_PRPTYPE_1_DREF)

NX_PROP_DEV_FORM_FAC = (0x00000001 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_INTF_REFS = (0x00000002 | NX_CLASS_DEVICE | NX_PRPTYPE_1_DREF)
NX_PROP_DEV_NAME = (0x00000003 | NX_CLASS_DEVICE | NX_PRPTYPE_STRING)
NX_PROP_DEV_NUM_PORTS = (0x00000004 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_PRODUCT_NUM = (0x00000008 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_SER_NUM = (0x00000005 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_SLOT_NUM = (0x00000006 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_NUM_PORTS_ALL = (0x00000007 | NX_CLASS_DEVICE | NX_PRPTYPE_U32)
NX_PROP_DEV_INTF_REFS_ALL = (0x00000008 | NX_CLASS_DEVICE | NX_PRPTYPE_1_DREF)

NX_PROP_INTF_DEV_REF = (0x00000001 | NX_CLASS_INTERFACE | NX_PRPTYPE_REF)
NX_PROP_INTF_NAME = (0x00000002 | NX_CLASS_INTERFACE | NX_PRPTYPE_STRING)
NX_PROP_INTF_NUM = (0x00000003 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_PORT_NUM = (0x00000004 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_PROTOCOL = (0x00000005 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_CAN_TERM_CAP = (0x00000008 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_CAN_TCVR_CAP = (0x00000007 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_STATE = (0x00000009 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_ID = (0x0000000A | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_REVISION = (0x0000000C | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_FIRMWARE_VERSION = (0x0000000D | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_COMPATIBLE_REVISION = (0x0000000E | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_PROP_INTF_DONGLE_COMPATIBLE_FIRMWARE_VERSION = (0x0000000F | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)

NX_PROP_SESSION_SUB_CAN_START_TIME_OFF = (0x00000081 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_SUB_CAN_TX_TIME = (0x00000082 | NX_CLASS_SESSION | NX_PRPTYPE_F64)
NX_PROP_SESSION_SUB_SKIP_N_CYCLIC_FRAMES = (0x00000083 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_SUB_OUTPUT_QUEUE_UPDATE_FREQ = (0x00000084 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_SUB_LIN_TX_N_CORRUPTED_CHKSUMS = (0x00000085 | NX_CLASS_SESSION | NX_PRPTYPE_U32)
NX_PROP_SESSION_SUB_J1939_ADDR_FILTER = (0x00000086 | NX_CLASS_SESSION | NX_PRPTYPE_STRING)

NX_PROP_DATABASE_NAME = (0x00000001 | NX_CLASS_DATABASE | NX_PRPTYPE_STRING)
NX_PROP_DATABASE_CLST_REFS = (0x00000002 | NX_CLASS_DATABASE | NX_PRPTYPE_1_DREF)
NX_PROP_DATABASE_SHOW_INVALID_FROM_OPEN = (0x00000003 | NX_CLASS_DATABASE | NX_PRPTYPE_BOOL)

NX_PROP_CLST_BAUD_RATE = (0x00000001 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_BAUD_RATE64 = (0x00000001 | NX_CLASS_CLUSTER | NX_PRPTYPE_U64)
NX_PROP_CLST_COMMENT = (0x00000008 | NX_CLASS_CLUSTER | NX_PRPTYPE_STRING)
NX_PROP_CLST_CONFIG_STATUS = (0x00000009 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_DATABASE_REF = (0x00000002 | NX_CLASS_CLUSTER | NX_PRPTYPE_REF)
NX_PROP_CLST_ECU_REFS = (0x00000003 | NX_CLASS_CLUSTER | NX_PRPTYPE_1_DREF)
NX_PROP_CLST_FRM_REFS = (0x00000004 | NX_CLASS_CLUSTER | NX_PRPTYPE_1_DREF)
NX_PROP_CLST_NAME = (0x00000005 | NX_CLASS_CLUSTER | NX_PRPTYPE_STRING)
NX_PROP_CLST_PDU_REFS = (0x00000008 | NX_CLASS_CLUSTER | NX_PRPTYPE_1_DREF)
NX_PROP_CLST_PDUS_REQD = (0x0000000A | NX_CLASS_CLUSTER | NX_PRPTYPE_BOOL)
NX_PROP_CLST_PROTOCOL = (0x00000006 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_SIG_REFS = (0x00000007 | NX_CLASS_CLUSTER | NX_PRPTYPE_1_DREF)
NX_PROP_CLST_CAN_IO_MODE = (0x00000010 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_CAN_FD_BAUD_RATE = (0x00000011 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_CAN_FD_BAUD_RATE64 = (0x00000011 | NX_CLASS_CLUSTER | NX_PRPTYPE_U64)
NX_PROP_CLST_FLEX_RAY_ACT_PT_OFF = (0x00000020 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_CAS_RX_L_MAX = (0x00000021 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_CHANNELS = (0x00000022 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_CLST_DRIFT_DMP = (0x00000023 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_COLD_ST_ATS = (0x00000024 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_CYCLE = (0x00000025 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_DYN_SEG_START = (0x00000026 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_DYN_SLOT_IDL_PH = (0x00000027 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_LATEST_USABLE_DYN = (0x0000002A | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_LATEST_GUAR_DYN = (0x0000002B | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_LIS_NOISE = (0x00000028 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_MACRO_PER_CYCLE = (0x00000029 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_MACROTICK = (0x00000030 | NX_CLASS_CLUSTER | NX_PRPTYPE_F64)
NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT = (0x00000031 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS = (0x00000032 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_MINISLOT_ACT_PT = (0x00000033 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_MINISLOT = (0x00000034 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_NM_VEC_LEN = (0x00000035 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_NIT = (0x00000036 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_NIT_START = (0x00000037 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_NUM_MINISLT = (0x00000038 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_NUM_STAT_SLT = (0x00000039 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_OFF_COR_ST = (0x00000040 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX = (0x00000041 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_MAX = (0x00000042 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_ST = (0x00000043 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_STAT_SLOT = (0x00000045 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_SYM_WIN = (0x00000046 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_SYM_WIN_START = (0x00000047 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_SYNC_NODE_MAX = (0x00000048 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_TSS_TX = (0x00000049 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_IDL = (0x00000050 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_LOW = (0x00000051 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_WIN = (0x00000052 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_IDL = (0x00000053 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_LOW = (0x00000054 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_FLEX_RAY_USE_WAKEUP = (0x00000055 | NX_CLASS_CLUSTER | NX_PRPTYPE_BOOL)
NX_PROP_CLST_LIN_SCHEDULES = (0x00000070 | NX_CLASS_CLUSTER | NX_PRPTYPE_1_DREF)
NX_PROP_CLST_LIN_TICK = (0x00000071 | NX_CLASS_CLUSTER | NX_PRPTYPE_F64)
NX_PROP_CLST_FLEX_RAY_ALW_PASS_ACT = (0x00000072 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_APPLICATION_PROTOCOL = (0x00000073 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)
NX_PROP_CLST_CAN_FD_ISO_MODE = (0x00000074 | NX_CLASS_CLUSTER | NX_PRPTYPE_U32)

NX_PROP_FRM_APPLICATION_PROTOCOL = (0x00000064 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_CLUSTER_REF = (0x00000001 | NX_CLASS_FRAME | NX_PRPTYPE_REF)
NX_PROP_FRM_COMMENT = (0x00000002 | NX_CLASS_FRAME | NX_PRPTYPE_STRING)
NX_PROP_FRM_CONFIG_STATUS = (0x00000009 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_DEFAULT_PAYLOAD = (0x00000005 | NX_CLASS_FRAME | NX_PRPTYPE_1_DU8)
NX_PROP_FRM_ID = (0x00000003 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_NAME = (0x00000004 | NX_CLASS_FRAME | NX_PRPTYPE_STRING)
NX_PROP_FRM_PAYLOAD_LEN = (0x00000007 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_SIG_REFS = (0x00000008 | NX_CLASS_FRAME | NX_PRPTYPE_1_DREF)
NX_PROP_FRM_CAN_EXT_ID = (0x00000010 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_CAN_TIMING_TYPE = (0x00000011 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_CAN_TX_TIME = (0x00000012 | NX_CLASS_FRAME | NX_PRPTYPE_F64)
NX_PROP_FRM_FLEX_RAY_BASE_CYCLE = (0x00000020 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_FLEX_RAY_CH_ASSIGN = (0x00000021 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_FLEX_RAY_CYCLE_REP = (0x00000022 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_FLEX_RAY_PREAMBLE = (0x00000023 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_FLEX_RAY_STARTUP = (0x00000024 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_FLEX_RAY_SYNC = (0x00000025 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_FLEX_RAY_TIMING_TYPE = (0x00000026 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_ENABLED = (0x00000030 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_I_DS = (0x00000031 | NX_CLASS_FRAME | NX_PRPTYPE_1_DU32)
NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS = (0x00000032 | NX_CLASS_FRAME | NX_PRPTYPE_1_DU32)
NX_PROP_FRM_LIN_CHECKSUM = (0x00000050 | NX_CLASS_FRAME | NX_PRPTYPE_U32)
NX_PROP_FRM_MUX_IS_MUXED = (0x00000040 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_MUX_DATA_MUX_SIG_REF = (0x00000041 | NX_CLASS_FRAME | NX_PRPTYPE_REF)
NX_PROP_FRM_MUX_STATIC_SIG_REFS = (0x00000042 | NX_CLASS_FRAME | NX_PRPTYPE_1_DREF)
NX_PROP_FRM_MUX_SUBFRAME_REFS = (0x00000043 | NX_CLASS_FRAME | NX_PRPTYPE_1_DREF)
NX_PROP_FRM_PDU_REFS = (0x00000060 | NX_CLASS_FRAME | NX_PRPTYPE_1_DREF)
NX_PROP_FRM_PDU_START_BITS = (0x00000061 | NX_CLASS_FRAME | NX_PRPTYPE_1_DU32)
NX_PROP_FRM_PDU_UPDATE_BITS = (0x00000063 | NX_CLASS_FRAME | NX_PRPTYPE_1_DU32)
NX_PROP_FRM_VARIABLE_PAYLOAD = (0x00000065 | NX_CLASS_FRAME | NX_PRPTYPE_BOOL)
NX_PROP_FRM_CA_NIO_MODE = (0x00000066 | NX_CLASS_FRAME | NX_PRPTYPE_U32)

NX_PROP_PDU_CLUSTER_REF = (0x00000004 | NX_CLASS_PDU | NX_PRPTYPE_REF)
NX_PROP_PDU_DEFAULT_PAYLOAD = (0x00000005 | NX_CLASS_PDU | NX_PRPTYPE_1_DU8)
NX_PROP_PDU_COMMENT = (0x00000002 | NX_CLASS_PDU | NX_PRPTYPE_STRING)
NX_PROP_PDU_CONFIG_STATUS = (0x00000007 | NX_CLASS_PDU | NX_PRPTYPE_U32)
NX_PROP_PDU_FRM_REFS = (0x00000006 | NX_CLASS_PDU | NX_PRPTYPE_1_DREF)
NX_PROP_PDU_NAME = (0x00000001 | NX_CLASS_PDU | NX_PRPTYPE_STRING)
NX_PROP_PDU_PAYLOAD_LEN = (0x00000003 | NX_CLASS_PDU | NX_PRPTYPE_U32)
NX_PROP_PDU_SIG_REFS = (0x00000005 | NX_CLASS_PDU | NX_PRPTYPE_1_DREF)
NX_PROP_PDU_MUX_IS_MUXED = (0x00000008 | NX_CLASS_PDU | NX_PRPTYPE_BOOL)
NX_PROP_PDU_MUX_DATA_MUX_SIG_REF = (0x00000009 | NX_CLASS_PDU | NX_PRPTYPE_REF)
NX_PROP_PDU_MUX_STATIC_SIG_REFS = (0x0000000A | NX_CLASS_PDU | NX_PRPTYPE_1_DREF)
NX_PROP_PDU_MUX_SUBFRAME_REFS = (0x0000000B | NX_CLASS_PDU | NX_PRPTYPE_1_DREF)

NX_PROP_SIG_BYTE_ORDR = (0x00000001 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_COMMENT = (0x00000002 | NX_CLASS_SIGNAL | NX_PRPTYPE_STRING)
NX_PROP_SIG_CONFIG_STATUS = (0x00000009 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_DATA_TYPE = (0x00000003 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_DEFAULT = (0x00000004 | NX_CLASS_SIGNAL | NX_PRPTYPE_F64)
NX_PROP_SIG_FRAME_REF = (0x00000005 | NX_CLASS_SIGNAL | NX_PRPTYPE_REF)
NX_PROP_SIG_MAX = (0x00000006 | NX_CLASS_SIGNAL | NX_PRPTYPE_F64)
NX_PROP_SIG_MIN = (0x00000007 | NX_CLASS_SIGNAL | NX_PRPTYPE_F64)
NX_PROP_SIG_NAME = (0x00000008 | NX_CLASS_SIGNAL | NX_PRPTYPE_STRING)
NX_PROP_SIG_NAME_UNIQUE_TO_CLUSTER = (0x00000010 | NX_CLASS_SIGNAL | NX_PRPTYPE_STRING)
NX_PROP_SIG_NUM_BITS = (0x00000012 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_PDU_REF = (0x00000011 | NX_CLASS_SIGNAL | NX_PRPTYPE_REF)
NX_PROP_SIG_SCALE_FAC = (0x00000013 | NX_CLASS_SIGNAL | NX_PRPTYPE_F64)
NX_PROP_SIG_SCALE_OFF = (0x00000014 | NX_CLASS_SIGNAL | NX_PRPTYPE_F64)
NX_PROP_SIG_START_BIT = (0x00000015 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_UNIT = (0x00000016 | NX_CLASS_SIGNAL | NX_PRPTYPE_STRING)
NX_PROP_SIG_MUX_IS_DATA_MUX = (0x00000030 | NX_CLASS_SIGNAL | NX_PRPTYPE_BOOL)
NX_PROP_SIG_MUX_IS_DYNAMIC = (0x00000031 | NX_CLASS_SIGNAL | NX_PRPTYPE_BOOL)
NX_PROP_SIG_MUX_VALUE = (0x00000032 | NX_CLASS_SIGNAL | NX_PRPTYPE_U32)
NX_PROP_SIG_MUX_SUBFRM_REF = (0x00000033 | NX_CLASS_SIGNAL | NX_PRPTYPE_REF)

NX_PROP_SUBFRM_CONFIG_STATUS = (0x00000009 | NX_CLASS_SUBFRAME | NX_PRPTYPE_U32)
NX_PROP_SUBFRM_DYN_SIG_REFS = (0x00000001 | NX_CLASS_SUBFRAME | NX_PRPTYPE_1_DREF)
NX_PROP_SUBFRM_FRM_REF = (0x00000002 | NX_CLASS_SUBFRAME | NX_PRPTYPE_REF)
NX_PROP_SUBFRM_MUX_VALUE = (0x00000003 | NX_CLASS_SUBFRAME | NX_PRPTYPE_U32)
NX_PROP_SUBFRM_NAME = (0x00000004 | NX_CLASS_SUBFRAME | NX_PRPTYPE_STRING)
NX_PROP_SUBFRM_PDU_REF = (0x00000005 | NX_CLASS_SUBFRAME | NX_PRPTYPE_REF)
NX_PROP_SUBFRM_NAME_UNIQUE_TO_CLUSTER = (0x00000007 | NX_CLASS_SUBFRAME | NX_PRPTYPE_STRING)

NX_PROP_ECU_CLST_REF = (0x00000001 | NX_CLASS_ECU | NX_PRPTYPE_REF)
NX_PROP_ECU_COMMENT = (0x00000005 | NX_CLASS_ECU | NX_PRPTYPE_STRING)
NX_PROP_ECU_CONFIG_STATUS = (0x00000009 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_NAME = (0x00000002 | NX_CLASS_ECU | NX_PRPTYPE_STRING)
NX_PROP_ECU_RX_FRM_REFS = (0x00000003 | NX_CLASS_ECU | NX_PRPTYPE_1_DREF)
NX_PROP_ECU_TX_FRM_REFS = (0x00000004 | NX_CLASS_ECU | NX_PRPTYPE_1_DREF)
NX_PROP_ECU_FLEX_RAY_IS_COLDSTART = (0x00000010 | NX_CLASS_ECU | NX_PRPTYPE_BOOL)
NX_PROP_ECU_FLEX_RAY_STARTUP_FRAME_REF = (0x00000011 | NX_CLASS_ECU | NX_PRPTYPE_REF)
NX_PROP_ECU_FLEX_RAY_WAKEUP_PTRN = (0x00000012 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_FLEX_RAY_WAKEUP_CHS = (0x00000013 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_FLEX_RAY_CONNECTED_CHS = (0x00000014 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_MASTER = (0x00000020 | NX_CLASS_ECU | NX_PRPTYPE_BOOL)
NX_PROP_ECU_LIN_PROTOCOL_VER = (0x00000021 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_INITIAL_NAD = (0x00000022 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_CONFIG_NAD = (0x00000023 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_SUPPLIER_ID = (0x00000024 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_FUNCTION_ID = (0x00000025 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_LIN_P2_MIN = (0x00000026 | NX_CLASS_ECU | NX_PRPTYPE_F64)
NX_PROP_ECU_LIN_ST_MIN = (0x00000027 | NX_CLASS_ECU | NX_PRPTYPE_F64)
NX_PROP_ECU_J1939_PREFERRED_ADDRESS = (0x00000028 | NX_CLASS_ECU | NX_PRPTYPE_U32)
NX_PROP_ECU_J1939_NODE_NAME = (0x00000029 | NX_CLASS_ECU | NX_PRPTYPE_U64)

NX_PROP_LIN_SCHED_CLST_REF = (0x00000005 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_REF)
NX_PROP_LIN_SCHED_COMMENT = (0x00000006 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_STRING)
NX_PROP_LIN_SCHED_CONFIG_STATUS = (0x00000007 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_U32)
NX_PROP_LIN_SCHED_ENTRIES = (0x00000001 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_1_DREF)
NX_PROP_LIN_SCHED_NAME = (0x00000002 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_STRING)
NX_PROP_LIN_SCHED_PRIORITY = (0x00000003 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_U32)
NX_PROP_LIN_SCHED_RUN_MODE = (0x00000004 | NX_CLASS_LIN_SCHED | NX_PRPTYPE_U32)

NX_PROP_LIN_SCHED_ENTRY_COLLISION_RES_SCHED = (0x00000001 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_REF)
NX_PROP_LIN_SCHED_ENTRY_DELAY = (0x00000002 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_F64)
NX_PROP_LIN_SCHED_ENTRY_EVENT_ID = (0x00000003 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_U32)
NX_PROP_LIN_SCHED_ENTRY_FRAMES = (0x00000004 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_1_DREF)
NX_PROP_LIN_SCHED_ENTRY_NAME = (0x00000006 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_STRING)
NX_PROP_LIN_SCHED_ENTRY_NAME_UNIQUE_TO_CLUSTER = (0x00000008 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_STRING)
NX_PROP_LIN_SCHED_ENTRY_SCHED = (0x00000007 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_REF)
NX_PROP_LIN_SCHED_ENTRY_TYPE = (0x00000005 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_U32)
NX_PROP_LIN_SCHED_ENTRY_NC_FF_DATA_BYTES = (0x00000009 | NX_CLASS_LIN_SCHED_ENTRY | NX_PRPTYPE_1_DU8)

NX_MODE_SIGNAL_IN_SINGLE_POINT = 0
NX_MODE_SIGNAL_IN_WAVEFORM = 1
NX_MODE_SIGNAL_IN_XY = 2
NX_MODE_SIGNAL_OUT_SINGLE_POINT = 3
NX_MODE_SIGNAL_OUT_WAVEFORM = 4
NX_MODE_SIGNAL_OUT_XY = 5
NX_MODE_FRAME_IN_STREAM = 6
NX_MODE_FRAME_IN_QUEUED = 7
NX_MODE_FRAME_IN_SINGLE_POINT = 8
NX_MODE_FRAME_OUT_STREAM = 9
NX_MODE_FRAME_OUT_QUEUED = 10
NX_MODE_FRAME_OUT_SINGLE_POINT = 11
NX_MODE_SIGNAL_CONVERSION_SINGLE_POINT = 12

NX_START_STOP_NORMAL = 0
NX_START_STOP_SESSION_ONLY = 1
NX_START_STOP_INTERFACE_ONLY = 2
NX_START_STOP_SESSION_ONLY_BLOCKING = 3

NX_BLINK_DISABLE = 0
NX_BLINK_ENABLE = 1

NX_TERM_PXI_TRIG0 = "PXI_Trig0"
NX_TERM_PXI_TRIG1 = "PXI_Trig1"
NX_TERM_PXI_TRIG2 = "PXI_Trig2"
NX_TERM_PXI_TRIG3 = "PXI_Trig3"
NX_TERM_PXI_TRIG4 = "PXI_Trig4"
NX_TERM_PXI_TRIG5 = "PXI_Trig5"
NX_TERM_PXI_TRIG6 = "PXI_Trig6"
NX_TERM_PXI_TRIG7 = "PXI_Trig7"
NX_TERM_FRONT_PANEL0 = "FrontPanel0"
NX_TERM_FRONT_PANEL1 = "FrontPanel1"
NX_TERM_PXI_STAR = "PXI_Star"
NX_TERM_PXI_CLK10 = "PXI_Clk10"
NX_TERM_10_M_HZ_TIMEBASE = "10MHzTimebase"
NX_TERM_1_M_HZ_TIMEBASE = "1MHzTimebase"
NX_TERM_MASTER_TIMEBASE = "MasterTimebase"
NX_TERM_COMM_TRIGGER = "CommTrigger"
NX_TERM_START_TRIGGER = "StartTrigger"
NX_TERM_FLEX_RAY_START_CYCLE = "FlexRayStartCycle"
NX_TERM_FLEX_RAY_MACROTICK = "FlexRayMacrotick"
NX_TERM_LOG_TRIGGER = "LogTrigger"

NX_STATE_TIME_CURRENT = (0x00000001 | NX_CLASS_INTERFACE | NX_PRPTYPE_TIME)
NX_STATE_TIME_COMMUNICATING = (0x00000002 | NX_CLASS_INTERFACE | NX_PRPTYPE_TIME)
NX_STATE_TIME_START = (0x00000003 | NX_CLASS_INTERFACE | NX_PRPTYPE_TIME)
NX_STATE_SESSION_INFO = (0x00000004 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_CAN_COMM = (0x00000010 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_FLEX_RAY_COMM = (0x00000020 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_FLEX_RAY_STATS = (0x00000021 | NX_CLASS_INTERFACE | NX_PRPTYPE_1_DU32)
NX_STATE_LIN_COMM = (0x00000030 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_J1939_COMM = (0x00000040 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_LIN_SCHEDULE_CHANGE = (0x00000081 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_LIN_DIAGNOSTIC_SCHEDULE_CHANGE = (0x00000083 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)
NX_STATE_FLEX_RAY_SYMBOL = (0x00000082 | NX_CLASS_INTERFACE | NX_PRPTYPE_U32)

NX_CAN_FD_MODE_ISO = 0
NX_CAN_FD_MODE_NON_ISO = 1
NX_CAN_FD_MODE_ISO_LEGACY = 2

NX_SESSION_INFO_STATE_STOPPED = 0
NX_SESSION_INFO_STATE_STARTED = 1
NX_SESSION_INFO_STATE_MIX = 2

NX_CAN_COMM_STATE_ERROR_ACTIVE = 0
NX_CAN_COMM_STATE_ERROR_PASSIVE = 1
NX_CAN_COMM_STATE_BUS_OFF = 2
NX_CAN_COMM_STATE_INIT = 3

NX_CAN_LAST_ERR_NONE = 0
NX_CAN_LAST_ERR_STUFF = 1
NX_CAN_LAST_ERR_FORM = 2
NX_CAN_LAST_ERR_ACK = 3
NX_CAN_LAST_ERR_BIT1 = 4
NX_CAN_LAST_ERR_BIT0 = 5
NX_CAN_LAST_ERR_CRC = 6

NX_CAN_IO_MODE_CAN = 0
NX_CAN_IO_MODE_CAN_FD = 1
NX_CAN_IO_MODE_CAN_FD_BRS = 2

NX_FLEX_RAY_POC_STATE_DEFAULT_CONFIG = 0
NX_FLEX_RAY_POC_STATE_READY = 1
NX_FLEX_RAY_POC_STATE_NORMAL_ACTIVE = 2
NX_FLEX_RAY_POC_STATE_NORMAL_PASSIVE = 3
NX_FLEX_RAY_POC_STATE_HALT = 4
NX_FLEX_RAY_POC_STATE_MONITOR = 5
NX_FLEX_RAY_POC_STATE_CONFIG = 15

NX_LIN_COMM_STATE_IDLE = 0
NX_LIN_COMM_STATE_ACTIVE = 1
NX_LIN_COMM_STATE_INACTIVE = 2

NX_LIN_DIAGNOSTIC_SCHEDULE_NULL = 0x0000
NX_LIN_DIAGNOSTIC_SCHEDULE_MASTER_REQ = 0x0001
NX_LIN_DIAGNOSTIC_SCHEDULE_SLAVE_RESP = 0x0002

NX_LIN_LAST_ERR_CODE_NONE = 0
NX_LIN_LAST_ERR_CODE_UNKNOWN_ID = 1
NX_LIN_LAST_ERR_CODE_FORM = 2
NX_LIN_LAST_ERR_CODE_FRAMING = 3
NX_LIN_LAST_ERR_CODE_READBACK = 4
NX_LIN_LAST_ERR_CODE_TIMEOUT = 5
NX_LIN_LAST_ERR_CODE_CRC = 6

NX_CONDITION_TRANSMIT_COMPLETE = 0x8001
NX_CONDITION_INTF_COMMUNICATING = 0x8002
NX_CONDITION_INTF_REMOTE_WAKEUP = 0x8003

NX_TIMEOUT_NONE = (0)
NX_TIMEOUT_INFINITE = (-1)

NX_GET_DBC_MODE_ATTRIBUTE = 0
NX_GET_DBC_MODE_ENUMERATION_LIST = 1
NX_GET_DBC_MODE_ATTRIBUTE_LIST = 2
NX_GET_DBC_MODE_VALUE_TABLE_LIST = 3

NXDB_MERGE_COPY_USE_SOURCE = 0
NXDB_MERGE_COPY_USE_TARGET = 1
NXDB_MERGE_MERGE_USE_SOURCE = 2
NXDB_MERGE_MERGE_USE_TARGET = 3

NX_DONGLE_STATE_NO_DONGLE_NO_EXT_POWER = 1
NX_DONGLE_STATE_NO_DONGLE_EXT_POWER = 2
NX_DONGLE_STATE_DONGLE_NO_EXT_POWER = 3
NX_DONGLE_STATE_READY = 4
NX_DONGLE_STATE_BUSY = 5
NX_DONGLE_STATE_COMM_ERROR = 13
NX_DONGLE_STATE_OVER_CURRENT = 14

NX_DONGLE_ID_LS_CAN = 1
NX_DONGLE_ID_HS_CAN = 2
NX_DONGLE_ID_SW_CAN = 3
NX_DONGLE_ID_XS_CAN = 4
NX_DONGLE_ID_LIN = 6
NX_DONGLE_ID_DONGLE_LESS = 13
NX_DONGLE_ID_UNKNOWN = 14

NX_PHASE_DEVELOPMENT = 0
NX_PHASE_ALPHA = 1
NX_PHASE_BETA = 2
NX_PHASE_RELEASE = 3

NX_DEV_FORM_PXI = 0
NX_DEV_FORM_PCI = 1
NX_DEV_FORM_C_SERIES = 2
NX_DEV_FORM_PXIE = 3
NX_DEV_FORM_USB = 4
NX_DEV_FORM_PCIE = 5

NX_CAN_TERM_CAP_NO = 0
NX_CAN_TERM_CAP_YES = 1

NX_CAN_TCVR_CAP_HS = 0
NX_CAN_TCVR_CAP_LS = 1
NX_CAN_TCVR_CAP_XS = 3
NX_CAN_TCVR_CAP_XS_HS_LS = 4
NX_CAN_TCVR_CAP_UNKNOWN = 0xFFFFFFFF

NX_PROTOCOL_UNKNOWN = 0xFFFFFFFE
NX_PROTOCOL_CAN = 0
NX_PROTOCOL_FLEX_RAY = 1
NX_PROTOCOL_LIN = 2

NX_APP_PROTOCOL_NONE = 0
NX_APP_PROTOCOL_J1939 = 1

NX_CAN_TERM_OFF = 0
NX_CAN_TERM_ON = 1

NX_CAN_TCVR_STATE_NORMAL = 0
NX_CAN_TCVR_STATE_SLEEP = 1
NX_CAN_TCVR_STATE_SW_WAKEUP = 2
NX_CAN_TCVR_STATE_SW_HIGH_SPEED = 3

NX_CAN_TCVR_TYPE_HS = 0
NX_CAN_TCVR_TYPE_LS = 1
NX_CAN_TCVR_TYPE_SW = 2
NX_CAN_TCVR_TYPE_EXT = 3
NX_CAN_TCVR_TYPE_DISC = 4

NX_FLEX_RAY_SAMP_PER_MICRO_1 = 0
NX_FLEX_RAY_SAMP_PER_MICRO_2 = 1
NX_FLEX_RAY_SAMP_PER_MICRO_4 = 2

NX_FLEX_RAY_TERM_OFF = 0
NX_FLEX_RAY_TERM_ON = 1

NX_LIN_SLEEP_REMOTE_SLEEP = 0
NX_LIN_SLEEP_REMOTE_WAKE = 1
NX_LIN_SLEEP_LOCAL_SLEEP = 2
NX_LIN_SLEEP_LOCAL_WAKE = 3

NX_LIN_TERM_OFF = 0
NX_LIN_TERM_ON = 1

NX_OUT_STRM_TIMNG_IMMEDIATE = 0
NX_OUT_STRM_TIMNG_REPLAY_EXCLUSIVE = 1
NX_OUT_STRM_TIMNG_REPLAY_INCLUSIVE = 2

NX_CAN_PEND_TX_ORDER_AS_SUBMITTED = 0
NX_CAN_PEND_TX_ORDER_BY_IDENTIFIER = 1

NX_FLEX_RAY_SLEEP_LOCAL_SLEEP = 0
NX_FLEX_RAY_SLEEP_LOCAL_WAKE = 1
NX_FLEX_RAY_SLEEP_REMOTE_WAKE = 2

NX_CAN_EXT_TCVR_CONFIG_NORMAL_SUPPORTED = (1 << 2)
NX_CAN_EXT_TCVR_CONFIG_SLEEP_SUPPORTED = (1 << 5)
NX_CAN_EXT_TCVR_CONFIG_SW_WAKEUP_SUPPORTED = (1 << 8)
NX_CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_SUPPORTED = (1 << 11)
NX_CAN_EXT_TCVR_CONFIG_POWER_ON_SUPPORTED = (1 << 14)
NX_CAN_EXT_TCVR_CONFIG_NORMAL_OUTPUT0_SET = (1 << 0)
NX_CAN_EXT_TCVR_CONFIG_SLEEP_OUTPUT0_SET = (1 << 3)
NX_CAN_EXT_TCVR_CONFIG_SW_WAKEUP_OUTPUT0_SET = (1 << 6)
NX_CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_OUTPUT0_SET = (1 << 9)
NX_CAN_EXT_TCVR_CONFIG_POWER_ON_OUTPUT0_SET = (1 << 12)
NX_CAN_EXT_TCVR_CONFIG_NORMAL_OUTPUT1_SET = (1 << 1)
NX_CAN_EXT_TCVR_CONFIG_SLEEP_OUTPUT1_SET = (1 << 4)
NX_CAN_EXT_TCVR_CONFIG_SW_WAKEUP_OUTPUT1_SET = (1 << 7)
NX_CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_OUTPUT1_SET = (1 << 10)
NX_CAN_EXT_TCVR_CONFIG_POWER_ON_OUTPUT1_SET = (1 << 13)
NX_CAN_EXT_TCVR_CONFIG_N_ERR_CONNECTED = (1 << 31)

NX_FRM_FLEX_RAY_CH_ASSIGN_A = 1
NX_FRM_FLEX_RAY_CH_ASSIGN_B = 2
NX_FRM_FLEX_RAY_CH_ASSIGN_AAND_B = 3
NX_FRM_FLEX_RAY_CH_ASSIGN_NONE = 4

NX_CLST_FLEX_RAY_SAMP_CLK_PER_P0125US = 0
NX_CLST_FLEX_RAY_SAMP_CLK_PER_P025US = 1
NX_CLST_FLEX_RAY_SAMP_CLK_PER_P05US = 2

NX_FRM_FLEX_RAY_TIMING_CYCLIC = 0
NX_FRM_FLEX_RAY_TIMING_EVENT = 1

NX_FRM_CAN_TIMING_CYCLIC_DATA = 0
NX_FRM_CAN_TIMING_EVENT_DATA = 1
NX_FRM_CAN_TIMING_CYCLIC_REMOTE = 2
NX_FRM_CAN_TIMING_EVENT_REMOTE = 3
NX_FRM_CAN_TIMING_CYCLIC_EVENT = 4

NX_SIG_BYTE_ORDR_LITTLE_ENDIAN = 0
NX_SIG_BYTE_ORDR_BIG_ENDIAN = 1

NX_SIG_DATA_TYPE_SIGNED = 0
NX_SIG_DATA_TYPE_UNSIGNED = 1
NX_SIG_DATA_TYPE_IEEE_FLOAT = 2

NX_LIN_PROTOCOL_VER_1_2 = 2
NX_LIN_PROTOCOL_VER_1_3 = 3
NX_LIN_PROTOCOL_VER_2_0 = 4
NX_LIN_PROTOCOL_VER_2_1 = 5
NX_LIN_PROTOCOL_VER_2_2 = 6

NX_LIN_SCHED_RUN_MODE_CONTINUOUS = 0
NX_LIN_SCHED_RUN_MODE_ONCE = 1
NX_LIN_SCHED_RUN_MODE_NULL = 2

NX_LIN_SCHED_ENTRY_TYPE_UNCONDITIONAL = 0
NX_LIN_SCHED_ENTRY_TYPE_SPORADIC = 1
NX_LIN_SCHED_ENTRY_TYPE_EVENT_TRIGGERED = 2
NX_LIN_SCHED_ENTRY_TYPE_NODE_CONFIG_SERVICE = 3

NX_FRM_LIN_CHECKSUM_CLASSIC = 0
NX_FRM_LIN_CHECKSUM_ENHANCED = 1

NX_FRAME_TYPE_CAN_DATA = 0x00
NX_FRAME_TYPE_CAN_REMOTE = 0x01
NX_FRAME_TYPE_CAN_BUS_ERROR = 0x02
NX_FRAME_TYPE_CAN20_DATA = 0x08
NX_FRAME_TYPE_CANFD_DATA = 0x10
NX_FRAME_TYPE_CANFDBRS_DATA = 0x18
NX_FRAME_TYPE_FLEX_RAY_DATA = 0x20
NX_FRAME_TYPE_FLEX_RAY_NULL = 0x21
NX_FRAME_TYPE_FLEX_RAY_SYMBOL = 0x22
NX_FRAME_TYPE_LIN_DATA = 0x40
NX_FRAME_TYPE_LIN_BUS_ERROR = 0x41
NX_FRAME_TYPE_LIN_NO_RESPONSE = 0x42
NX_FRAME_TYPE_J1939_DATA = 0xC0
NX_FRAME_TYPE_SPECIAL_DELAY = 0xE0
NX_FRAME_TYPE_SPECIAL_LOG_TRIGGER = 0xE1
NX_FRAME_TYPE_SPECIAL_START_TRIGGER = 0xE2

NX_FRAME_ID_CAN_IS_EXTENDED = 0x20000000

NX_FRAME_FLAGS_FLEX_RAY_STARTUP = 0x01
NX_FRAME_FLAGS_FLEX_RAY_SYNC = 0x02
NX_FRAME_FLAGS_FLEX_RAY_PREAMBLE = 0x04
NX_FRAME_FLAGS_FLEX_RAY_CH_A = 0x10
NX_FRAME_FLAGS_FLEX_RAY_CH_B = 0x20
NX_FRAME_FLAGS_LIN_EVENT_SLOT = 0x01
NX_FRAME_FLAGS_TRANSMIT_ECHO = 0x80

NX_FLEX_RAY_SYMBOL_MTS = 0x00
NX_FLEX_RAY_SYMBOL_WAKEUP = 0x01

NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939 = (7)

NX_SIZEOF_FRAME_HEADER = (16)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_cfuncs.py sha256=e84083914f988dbad8a78b1a2aeace8e30b71013fce819d0f3d3d49e310d847d bytes=47906 -->
## FILE: nixnet/_cfuncs.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_cfuncs.py`
- sha256: `e84083914f988dbad8a78b1a2aeace8e30b71013fce819d0f3d3d49e310d847d`
- bytes: 47906

````python
import ctypes  # type: ignore
import threading
import typing  # NOQA: F401

from nixnet import _ctypedefs
from nixnet import _lib


class XnetLibrary(object):
    """NI-XNET C library

    This mostly serves to benefit testing by
    - Delay loading the DLL so we can import this without it being loaded.
    - Provide a mockable interface for verifying how we use ctypes
    """

    def __init__(self):
        self._cdll = None
        self._load_lock = threading.Lock()
        self._nx_create_session = None
        self._nx_create_session_by_ref = None
        self._nx_get_property = None
        self._nx_get_property_size = None
        self._nx_set_property = None
        self._nx_get_sub_property = None
        self._nx_get_sub_property_size = None
        self._nx_set_sub_property = None
        self._nx_read_frame = None
        self._nx_read_signal_single_point = None
        self._nx_read_signal_waveform = None
        self._nx_read_signal_xy = None
        self._nx_read_state = None
        self._nx_write_frame = None
        self._nx_write_signal_single_point = None
        self._nx_write_state = None
        self._nx_write_signal_waveform = None
        self._nx_write_signal_xy = None
        self._nx_convert_frames_to_signals_single_point = None
        self._nx_convert_signals_to_frames_single_point = None
        self._nx_blink = None
        self._nx_clear = None
        self._nx_connect_terminals = None
        self._nx_disconnect_terminals = None
        self._nx_flush = None
        self._nx_start = None
        self._nx_stop = None
        self._nx_status_to_string = None
        self._nx_system_open = None
        self._nx_system_close = None
        self._nx_wait = None
        self._nxdb_open_database = None
        self._nxdb_close_database = None
        self._nxdb_create_object = None
        self._nxdb_find_object = None
        self._nxdb_delete_object = None
        self._nxdb_save_database = None
        self._nxdb_get_property = None
        self._nxdb_get_property_size = None
        self._nxdb_set_property = None
        self._nxdb_get_dbc_attribute_size = None
        self._nxdb_get_dbc_attribute = None
        self._nxdb_merge = None
        self._nxdb_add_alias = None
        self._nxdb_add_alias64 = None
        self._nxdb_remove_alias = None
        self._nxdb_deploy = None
        self._nxdb_undeploy = None
        self._nxdb_get_database_list = None
        self._nxdb_get_database_list_sizes = None

    @property
    def cdll(self):
        # type: (...) -> _lib.XnetLibrary
        if self._cdll is None:
            self._cdll = _lib.import_lib()
        return self._cdll

    def nx_create_session(
            self,
            database_name,  # type: _ctypedefs.char_p
            cluster_name,  # type: _ctypedefs.char_p
            list,  # type: _ctypedefs.char_p
            interface,  # type: _ctypedefs.char_p
            mode,  # type: _ctypedefs.u32
            session_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_create_session is None:
            with self._load_lock:
                cfunc = self.cdll.nxCreateSession
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_create_session = cfunc
        return self._nx_create_session(
            database_name,
            cluster_name,
            list,
            interface,
            mode,
            session_ref)

    def nx_create_session_by_ref(
            self,
            size_of_database_refs,  # type: _ctypedefs.u32
            database_refs,  # type: typing.Any
            interface,  # type: _ctypedefs.char_p
            mode,  # type: _ctypedefs.u32
            session_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_create_session_by_ref is None:
            with self._load_lock:
                cfunc = self.cdll.nxCreateSessionByRef
                cfunc.argtypes = [
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t),
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_create_session_by_ref = cfunc
        return self._nx_create_session_by_ref(
            size_of_database_refs,
            database_refs,
            interface,
            mode,
            session_ref)

    def nx_get_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_property = cfunc
        return self._nx_get_property(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_property_size(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_property_size = cfunc
        return self._nx_get_property_size(
            session_ref,
            property_id,
            property_size)

    def nx_set_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_set_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxSetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_set_property = cfunc
        return self._nx_set_property(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_sub_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetSubProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_sub_property = cfunc
        return self._nx_get_sub_property(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property_size(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_sub_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetSubPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_sub_property_size = cfunc
        return self._nx_get_sub_property_size(
            session_ref,
            active_index,
            property_id,
            property_size)

    def nx_set_sub_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_set_sub_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxSetSubProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_set_sub_property = cfunc
        return self._nx_set_sub_property(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_read_frame(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
            number_of_bytes_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_frame is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadFrame
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_frame = cfunc
        return self._nx_read_frame(
            session_ref,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned)

    def nx_read_signal_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadSignalSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_signal_single_point = cfunc
        return self._nx_read_signal_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_read_signal_waveform(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            start_time,  # type: typing.Any
            delta_time,  # type: typing.Any
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            number_of_values_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_waveform is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadSignalWaveform
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    ctypes.POINTER(_ctypedefs.f64),
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_signal_waveform = cfunc
        return self._nx_read_signal_waveform(
            session_ref,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned)

    def nx_read_signal_xy(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            time_limit,  # type: typing.Any
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
            num_pairs_buffer,  # type: typing.Any
            size_of_num_pairs_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_xy is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadSignalXY
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_signal_xy = cfunc
        return self._nx_read_signal_xy(
            session_ref,
            time_limit,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer)

    def nx_read_state(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            state_id,  # type: _ctypedefs.u32
            state_size,  # type: _ctypedefs.u32
            state_value,  # type: _ctypedefs.nxVoidPtr
            fault,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_state is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadState
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr,
                    ctypes.POINTER(_ctypedefs.nxStatus_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_state = cfunc
        return self._nx_read_state(
            session_ref,
            state_id,
            state_size,
            state_value,
            fault)

    def nx_write_frame(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_frame is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteFrame
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    _ctypedefs.f64]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_frame = cfunc
        return self._nx_write_frame(
            session_ref,
            buffer,
            size_of_buffer,
            timeout)

    def nx_write_signal_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteSignalSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_signal_single_point = cfunc
        return self._nx_write_signal_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer)

    def nx_write_state(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            state_id,  # type: _ctypedefs.u32
            state_size,  # type: _ctypedefs.u32
            state_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_state is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteState
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_state = cfunc
        return self._nx_write_state(
            session_ref,
            state_id,
            state_size,
            state_value)

    def nx_write_signal_waveform(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_waveform is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteSignalWaveform
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_signal_waveform = cfunc
        return self._nx_write_signal_waveform(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer)

    def nx_write_signal_xy(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
            num_pairs_buffer,  # type: typing.Any
            size_of_num_pairs_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_xy is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteSignalXY
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_signal_xy = cfunc
        return self._nx_write_signal_xy(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer)

    def nx_convert_frames_to_signals_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            frame_buffer,  # type: typing.Any
            size_of_frame_buffer,  # type: _ctypedefs.u32
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_convert_frames_to_signals_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxConvertFramesToSignalsSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_convert_frames_to_signals_single_point = cfunc
        return self._nx_convert_frames_to_signals_single_point(
            session_ref,
            frame_buffer,
            size_of_frame_buffer,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_convert_signals_to_frames_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            number_of_bytes_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_convert_signals_to_frames_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxConvertSignalsToFramesSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_convert_signals_to_frames_single_point = cfunc
        return self._nx_convert_signals_to_frames_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned)

    def nx_blink(
            self,
            interface_ref,  # type: _ctypedefs.nxSessionRef_t
            modifier,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_blink is None:
            with self._load_lock:
                cfunc = self.cdll.nxBlink
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_blink = cfunc
        return self._nx_blink(
            interface_ref,
            modifier)

    def nx_clear(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_clear is None:
            with self._load_lock:
                cfunc = self.cdll.nxClear
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_clear = cfunc
        return self._nx_clear(
            session_ref)

    def nx_connect_terminals(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            source,  # type: _ctypedefs.char_p
            destination,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_connect_terminals is None:
            with self._load_lock:
                cfunc = self.cdll.nxConnectTerminals
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_connect_terminals = cfunc
        return self._nx_connect_terminals(
            session_ref,
            source,
            destination)

    def nx_disconnect_terminals(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            source,  # type: _ctypedefs.char_p
            destination,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_disconnect_terminals is None:
            with self._load_lock:
                cfunc = self.cdll.nxDisconnectTerminals
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_disconnect_terminals = cfunc
        return self._nx_disconnect_terminals(
            session_ref,
            source,
            destination)

    def nx_flush(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_flush is None:
            with self._load_lock:
                cfunc = self.cdll.nxFlush
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_flush = cfunc
        return self._nx_flush(
            session_ref)

    def nx_start(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            scope,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_start is None:
            with self._load_lock:
                cfunc = self.cdll.nxStart
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_start = cfunc
        return self._nx_start(
            session_ref,
            scope)

    def nx_stop(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            scope,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_stop is None:
            with self._load_lock:
                cfunc = self.cdll.nxStop
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_stop = cfunc
        return self._nx_stop(
            session_ref,
            scope)

    def nx_status_to_string(
            self,
            status,  # type: _ctypedefs.nxStatus_t
            size_of_status_description,  # type: _ctypedefs.u32
            status_description,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> None
        if self._nx_status_to_string is None:
            with self._load_lock:
                cfunc = self.cdll.nxStatusToString
                cfunc.argtypes = [
                    _ctypedefs.nxStatus_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p]
                cfunc.restype = None
                self._nx_status_to_string = cfunc
        return self._nx_status_to_string(
            status,
            size_of_status_description,
            status_description)

    def nx_system_open(
            self,
            system_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_system_open is None:
            with self._load_lock:
                cfunc = self.cdll.nxSystemOpen
                cfunc.argtypes = [
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_system_open = cfunc
        return self._nx_system_open(
            system_ref)

    def nx_system_close(
            self,
            system_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_system_close is None:
            with self._load_lock:
                cfunc = self.cdll.nxSystemClose
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_system_close = cfunc
        return self._nx_system_close(
            system_ref)

    def nx_wait(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            condition,  # type: _ctypedefs.u32
            param_in,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
            param_out,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_wait is None:
            with self._load_lock:
                cfunc = self.cdll.nxWait
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_wait = cfunc
        return self._nx_wait(
            session_ref,
            condition,
            param_in,
            timeout,
            param_out)

    def nxdb_open_database(
            self,
            database_name,  # type: _ctypedefs.char_p
            database_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_open_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbOpenDatabase
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_open_database = cfunc
        return self._nxdb_open_database(
            database_name,
            database_ref)

    def nxdb_close_database(
            self,
            database_ref,  # type: _ctypedefs.nxDatabaseRef_t
            close_all_refs,  # type: _ctypedefs.bool32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_close_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbCloseDatabase
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.bool32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_close_database = cfunc
        return self._nxdb_close_database(
            database_ref,
            close_all_refs)

    def nxdb_create_object(
            self,
            parent_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            object_class,  # type: _ctypedefs.u32
            object_name,  # type: _ctypedefs.char_p
            db_object_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_create_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbCreateObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_create_object = cfunc
        return self._nxdb_create_object(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_find_object(
            self,
            parent_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            object_class,  # type: _ctypedefs.u32
            object_name,  # type: _ctypedefs.char_p
            db_object_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_find_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbFindObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_find_object = cfunc
        return self._nxdb_find_object(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_delete_object(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_delete_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbDeleteObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_delete_object = cfunc
        return self._nxdb_delete_object(
            db_object_ref)

    def nxdb_save_database(
            self,
            database_ref,  # type: _ctypedefs.nxDatabaseRef_t
            db_filepath,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_save_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbSaveDatabase
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_save_database = cfunc
        return self._nxdb_save_database(
            database_ref,
            db_filepath)

    def nxdb_get_property(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_property = cfunc
        return self._nxdb_get_property(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_property_size(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_property_size = cfunc
        return self._nxdb_get_property_size(
            db_object_ref,
            property_id,
            property_size)

    def nxdb_set_property(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_set_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbSetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_set_property = cfunc
        return self._nxdb_set_property(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_dbc_attribute_size(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            mode,  # type: _ctypedefs.u32
            attribute_name,  # type: _ctypedefs.char_p
            attribute_text_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_dbc_attribute_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDBCAttributeSize
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_dbc_attribute_size = cfunc
        return self._nxdb_get_dbc_attribute_size(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size)

    def nxdb_get_dbc_attribute(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            mode,  # type: _ctypedefs.u32
            attribute_name,  # type: _ctypedefs.char_p
            attribute_text_size,  # type: _ctypedefs.u32
            attribute_text,  # type: _ctypedefs.char_p
            is_default,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_dbc_attribute is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDBCAttribute
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_dbc_attribute = cfunc
        return self._nxdb_get_dbc_attribute(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size,
            attribute_text,
            is_default)

    def nxdb_merge(
            self,
            target_cluster_ref,  # type: _ctypedefs.nxDatabaseRef_t
            source_obj_ref,  # type: _ctypedefs.nxDatabaseRef_t
            copy_mode,  # type: _ctypedefs.u32
            prefix,  # type: _ctypedefs.char_p
            wait_for_complete,  # type: _ctypedefs.bool32
            percent_complete,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_merge is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbMerge
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.bool32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_merge = cfunc
        return self._nxdb_merge(
            target_cluster_ref,
            source_obj_ref,
            copy_mode,
            prefix,
            wait_for_complete,
            percent_complete)

    def nxdb_add_alias(
            self,
            database_alias,  # type: _ctypedefs.char_p
            database_filepath,  # type: _ctypedefs.char_p
            default_baud_rate,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_add_alias is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbAddAlias
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_add_alias = cfunc
        return self._nxdb_add_alias(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_add_alias64(
            self,
            database_alias,  # type: _ctypedefs.char_p
            database_filepath,  # type: _ctypedefs.char_p
            default_baud_rate,  # type: _ctypedefs.u64
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_add_alias64 is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbAddAlias64
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u64]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_add_alias64 = cfunc
        return self._nxdb_add_alias64(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_remove_alias(
            self,
            database_alias,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_remove_alias is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbRemoveAlias
                cfunc.argtypes = [
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_remove_alias = cfunc
        return self._nxdb_remove_alias(
            database_alias)

    def nxdb_deploy(
            self,
            ip_address,  # type: _ctypedefs.char_p
            database_alias,  # type: _ctypedefs.char_p
            wait_for_complete,  # type: _ctypedefs.bool32
            percent_complete,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_deploy is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbDeploy
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.bool32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_deploy = cfunc
        return self._nxdb_deploy(
            ip_address,
            database_alias,
            wait_for_complete,
            percent_complete)

    def nxdb_undeploy(
            self,
            ip_address,  # type: _ctypedefs.char_p
            database_alias,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_undeploy is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbUndeploy
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_undeploy = cfunc
        return self._nxdb_undeploy(
            ip_address,
            database_alias)

    def nxdb_get_database_list(
            self,
            ip_address,  # type: _ctypedefs.char_p
            size_of_alias_buffer,  # type: _ctypedefs.u32
            alias_buffer,  # type: _ctypedefs.char_p
            size_of_filepath_buffer,  # type: _ctypedefs.u32
            filepath_buffer,  # type: _ctypedefs.char_p
            number_of_databases,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_database_list is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDatabaseList
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_database_list = cfunc
        return self._nxdb_get_database_list(
            ip_address,
            size_of_alias_buffer,
            alias_buffer,
            size_of_filepath_buffer,
            filepath_buffer,
            number_of_databases)

    def nxdb_get_database_list_sizes(
            self,
            ip_address,  # type: _ctypedefs.char_p
            sizeof_alias_buffer,  # type: _ctypedefs.u32
            sizeof_filepath_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_database_list_sizes is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDatabaseListSizes
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32),
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_database_list_sizes = cfunc
        return self._nxdb_get_database_list_sizes(
            ip_address,
            sizeof_alias_buffer,
            sizeof_filepath_buffer)


lib = XnetLibrary()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_cprops.py sha256=e3cdba3c4c1d774808b1d2fee2daa2a27f54da8b03c412829dc341dbfa7a3c6c bytes=23307 -->
## FILE: nixnet/_cprops.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_cprops.py`
- sha256: `e3cdba3c4c1d774808b1d2fee2daa2a27f54da8b03c412829dc341dbfa7a3c6c`
- bytes: 23307

````python
import ctypes  # type: ignore
import typing  # NOQA: F401

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _errors
from nixnet import _funcs


def get_session_bool(ref, prop_id):
    # type: (int, int) -> bool
    return bool(get_session_u8(ref, prop_id))


def set_session_bool(ref, prop_id, value):
    # type: (int, int, bool) -> None
    set_session_u8(ref, prop_id, 1 if value else 0)


def get_session_u8(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u8(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u32(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u32(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u32_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))()  # type: ignore
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_session_u32_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u32.BYTES
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u64(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u64(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_f64(ref, prop_id):
    # type: (int, int) -> float
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_f64(ref, prop_id, value):
    # type: (int, int, float) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_string(ref, prop_id):
    # type: (int, int) -> typing.Text
    value_size = _funcs.nx_get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_size)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value.decode("ascii")


def set_session_string(ref, prop_id, value):
    # type: (int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_string_array(ref, prop_id):
    # type: (int, int) -> typing.List[typing.Text]
    value = get_session_string(ref, prop_id)
    return value.split(",")


def get_session_ref(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxSessionRef_t.BYTES)
    value_ctypes = _ctypedefs.nxSessionRef_t()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_ref(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxSessionRef_t.BYTES)
    value_ctypes = _ctypedefs.nxSessionRef_t(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_ref_array_len(ref, prop_id):
    # type: (int, int) -> int
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES
    return elements


def get_session_ref_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxSessionRef_t * (elements))()  # type: ignore
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_session_ref_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.nxSessionRef_t.BYTES
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxSessionRef_t * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_u32(ref, sub, prop_id, value):
    # type: (int, int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_f64(ref, sub, prop_id, value):
    # type: (int, int, int, float) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_string(ref, sub, prop_id, value):
    # type: (int, int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_bool(ref, prop_id):
    # type: (int, int) -> bool
    return bool(get_database_u8(ref, prop_id))


def set_database_bool(ref, prop_id, value):
    # type: (int, int, bool) -> None
    set_database_u8(ref, prop_id, 1 if value else 0)


def get_database_u8(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u8(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u8_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u8.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u8 * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_u8_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u8.BYTES
    elements = value_size // _ctypedefs.u8.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u8 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u32(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u32(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u32_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_u32_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u32.BYTES
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u64(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u64(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_f64(ref, prop_id):
    # type: (int, int) -> float
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_f64(ref, prop_id, value):
    # type: (int, int, float) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_string(ref, prop_id):
    # type: (int, int) -> typing.Text
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_size)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value.decode("ascii")


def set_database_string(ref, prop_id, value):
    # type: (int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_ref(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxDatabaseRef_t.BYTES)
    value_ctypes = _ctypedefs.nxDatabaseRef_t()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_ref(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxDatabaseRef_t.BYTES)
    value_ctypes = _ctypedefs.nxDatabaseRef_t(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_ref_array_len(ref, prop_id):
    # type: (int, int) -> int
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES
    return elements


def get_database_ref_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxDatabaseRef_t * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_ref_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.nxDatabaseRef_t.BYTES
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxDatabaseRef_t * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_ctypedefs.py sha256=694435983e3c81846339054a6569e0aac80d113282ce0876b3a78a4d9741d7ff bytes=2184 -->
## FILE: nixnet/_ctypedefs.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_ctypedefs.py`
- sha256: `694435983e3c81846339054a6569e0aac80d113282ce0876b3a78a4d9741d7ff`
- bytes: 2184

````python
"""
Definition of types for calling into NI-XNET.

Distinct types (rather than aliases) are used to allow more accurate type
checking.
"""


import ctypes  # type: ignore


class char(ctypes.c_char):  # NOQA: N801

    BYTES = 1


class char_p(ctypes.c_char_p):  # NOQA: N801
    pass


class bool8(ctypes.c_ubyte):  # NOQA: N801
    """32-bit boolean C-type."""

    BYTES = 1


class bool32(ctypes.c_uint):  # NOQA: N801
    """32-bit boolean C-type."""

    BYTES = 4


class byte(ctypes.c_char):  # NOQA: N801

    BYTES = 1


class i8(ctypes.c_byte):  # NOQA: N801

    BYTES = 1


class i16(ctypes.c_short):  # NOQA: N801

    BYTES = 2


class i32(ctypes.c_int):  # NOQA: N801

    BYTES = 4


class i64(ctypes.c_longlong):  # NOQA: N801

    BYTES = 8


class u8(ctypes.c_ubyte):  # NOQA: N801

    BYTES = 1


class u16(ctypes.c_ushort):  # NOQA: N801

    BYTES = 2


class u32(ctypes.c_uint):  # NOQA: N801

    BYTES = 4


class u64(ctypes.c_ulonglong):  # NOQA: N801

    BYTES = 8


class f32(ctypes.c_float):  # NOQA: N801

    BYTES = 4


class f64(ctypes.c_double):  # NOQA: N801

    BYTES = 8


class nxVoidPtr(ctypes.c_void_p):  # NOQA: N801
    pass


class nxSessionRef_t(u32):  # NOQA: N801
    pass


class nxDatabaseRef_t(u32):  # NOQA: N801
    pass


class nxStatus_t(u32):  # NOQA: N801
    pass


class nxTimestamp_t(u64):  # NOQA: N801
    """"Absolute time, given in 100 ns increments since Jan 1, 1601, 12:00 AM UTC."""
    pass


class nxFlexRayStats_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("NumSyntaxErrorChA", u32),
        ("NumSyntaxErrorChB", u32),
        ("NumContextErrorChA", u32),
        ("NumContextErrorChB", u32),
        ("NumSlotBoundaryViolationChA", u32),
        ("NumSlotBoundaryViolationChB", u32)]


class nxJ1939CommState_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("PGN", u32),
        ("SourceAddress", u8),
        ("DestinationAddress", u8),
        ("TransmitError", u8),
        ("ReceiveError", u8),
        ("Reserved1", u32),
        ("Reserved2", u32)]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_enums.py sha256=02535f6e1872eb5335568ecc7f4713890c1a01e30af5c81ab2c50c406f4693b7 bytes=123589 -->
## FILE: nixnet/_enums.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_enums.py`
- sha256: `02535f6e1872eb5335568ecc7f4713890c1a01e30af5c81ab2c50c406f4693b7`
- bytes: 123589

````python
import enum

from nixnet import _cconsts


class Err(enum.Enum):
    """Error codes returned by NI-XNET."""
    # An internal error occurred in the NI-XNET driver. Please contact National
    # Instruments and provide the information from the file
    # %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log\\niXntErr.log. On Windows XP,
    # the file can be found at %USERPROFILE%\\Local Settings\\Application
    # Data\\National Instruments\\NI-XNET\\log\\niXntErr.log. Please note that this
    # location may be hidden on your computer.
    INTERNAL_ERROR = _cconsts.NX_ERR_INTERNAL_ERROR
    # Board self test failed(code 2). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR1 = _cconsts.NX_ERR_SELF_TEST_ERROR1
    # Board self test failed(code 3). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR2 = _cconsts.NX_ERR_SELF_TEST_ERROR2
    # Board self test failed(code 4). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR3 = _cconsts.NX_ERR_SELF_TEST_ERROR3
    # Board self test failed(code 5). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR4 = _cconsts.NX_ERR_SELF_TEST_ERROR4
    # Board self test failed(code 6). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR5 = _cconsts.NX_ERR_SELF_TEST_ERROR5
    # Computer went to hibernation mode and the board lost power. Solution:
    # prevent the computer from going to hibernation mode in the control panel.
    POWER_SUSPENDED = _cconsts.NX_ERR_POWER_SUSPENDED
    # A write queue overflowed. Solution: wait until queue space becomes available
    # and retry.
    OUTPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_OUTPUT_QUEUE_OVERFLOW
    # The board's firmware did not answer a command. Solution: Stop your
    # application and execute a self test. Try deactivating/reactivating the
    # driver in the Device Manager. If the problem persists, contact National
    # Instruments.
    FIRMWARE_NO_RESPONSE = _cconsts.NX_ERR_FIRMWARE_NO_RESPONSE
    # The operation timed out. Solution: specify a timeout long enough to complete
    # the operation, or change the operation in a way that it can get completed in
    # less time (e.g. read less data).
    EVENT_TIMEOUT = _cconsts.NX_ERR_EVENT_TIMEOUT
    # A read queue overflowed. Solution: reduce your data rate or call Read more
    # frequently.
    INPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_INPUT_QUEUE_OVERFLOW
    # The Read buffer is too small to hold a single frame. Solution: provide a
    # buffer large enough.
    INPUT_QUEUE_READ_SIZE = _cconsts.NX_ERR_INPUT_QUEUE_READ_SIZE
    # You tried to open the same frame twice. This is not permitted. Solution:
    # open each frame only once.
    DUPLICATE_FRAME_OBJECT = _cconsts.NX_ERR_DUPLICATE_FRAME_OBJECT
    # You tried to open the same stream object twice. This is not permitted.
    # Solution: open each stream object only once.
    DUPLICATE_STREAM_OBJECT = _cconsts.NX_ERR_DUPLICATE_STREAM_OBJECT
    # Self test is not possible since the board is in use by an application.
    # Solution: stop all NI-XNET applications before executing a self test.
    SELF_TEST_NOT_POSSIBLE = _cconsts.NX_ERR_SELF_TEST_NOT_POSSIBLE
    # Allocation of memory failed. You do not have sufficient memory in the
    # LabVIEW target. Solution: add more RAM or try to use fewer resources in your
    # applications (arrays, XNET sessions, etc).
    MEMORY_FULL = _cconsts.NX_ERR_MEMORY_FULL
    # The maximum number of sessions was exceeded. Solution: use fewer sessions.
    MAX_SESSIONS = _cconsts.NX_ERR_MAX_SESSIONS
    # The maximum number of frames has been exceeded. Solution: Use fewer frames
    # in your sessions.
    MAX_FRAMES = _cconsts.NX_ERR_MAX_FRAMES
    # The maximum number of devices has been detected. Solution: use fewer
    # devices.
    MAX_DEVICES = _cconsts.NX_ERR_MAX_DEVICES
    # A driver support file is missing. Solution: try reinstalling the driver. If
    # the error persists, contact National Instruments.
    MISSING_FILE = _cconsts.NX_ERR_MISSING_FILE
    # This indicates that a NULL pointer or an empty string was passed to a
    # function. The user should verify that the parameters passed in make sense
    # for the given function.
    PARAMETER_NULL_OR_EMPTY = _cconsts.NX_ERR_PARAMETER_NULL_OR_EMPTY
    # The maximum number of schedules has been detected. Solution: Use fewer
    # schedules.
    MAX_SCHEDULES = _cconsts.NX_ERR_MAX_SCHEDULES
    # Board self test failed (code 17). Solution: Try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists, contact
    # National Instruments.
    SELF_TEST_ERROR6 = _cconsts.NX_ERR_SELF_TEST_ERROR6
    # You cannot start an NI-XNET application while a self test is in progress.
    # Solution: Complete the self test before starting any NI-XNET applications.
    SELF_TEST_IN_PROGRESS = _cconsts.NX_ERR_SELF_TEST_IN_PROGRESS
    # An invalid reference has been passed to a NI-XNET session function.
    # Solution: Only pass reference retrieved from Create Session, or from an IO
    # name of a session in LabVIEW project.
    INVALID_SESSION_HANDLE = _cconsts.NX_ERR_INVALID_SESSION_HANDLE
    # An invalid reference has been passed to a NI-XNET system function. Solution:
    # Only pass a valid system reference.
    INVALID_SYSTEM_HANDLE = _cconsts.NX_ERR_INVALID_SYSTEM_HANDLE
    # A device reference was expected for a NI-XNET session function. Solution:
    # Only pass a device reference.
    DEVICE_HANDLE_EXPECTED = _cconsts.NX_ERR_DEVICE_HANDLE_EXPECTED
    # An interface reference was expected for a NI-XNET session function.
    # Solution: Only pass an interface reference.
    INTF_HANDLE_EXPECTED = _cconsts.NX_ERR_INTF_HANDLE_EXPECTED
    # You have configured a property that conflicts with the current mode of the
    # session. For example, you have created a CAN output session with a frame
    # configured with a Timing Type = Cyclic and a Transmit Time of 0.
    PROPERTY_MODE_CONFLICTING = _cconsts.NX_ERR_PROPERTY_MODE_CONFLICTING
    # XNET Create Timing Source VI is not supported on Windows. This VI is
    # supported on LabVIEW Real-Time targets only.
    TIMING_SOURCE_NOT_SUPPORTED = _cconsts.NX_ERR_TIMING_SOURCE_NOT_SUPPORTED
    # You tried to create more than one LabVIEW timing source for a single
    # interface. Only one timing source per interface is supported. The timing
    # source remains until the top-level VI is idle (no longer running). Solution:
    # Call the XNET Create Timing Source VI only once per interface. You can use
    # the timing source with multiple timed structures (e.g. timed loops).
    MULTIPLE_TIMING_SOURCE = _cconsts.NX_ERR_MULTIPLE_TIMING_SOURCE
    # You invoked two or more VIs simultaneously for the same session, and those
    # VIs do not support overlap. For example, you attempted to invoke two Read
    # VIs at the same time for the same session. Solution: Wire the error cluster
    # from one VI to another, to enforce sequential execution for the session.
    OVERLAPPING_IO = _cconsts.NX_ERR_OVERLAPPING_IO
    # You are trying to start an interface that is missing bus power for the
    # transceiver. Some physical layers on NI-XNET hardware are internally
    # powered, but others require external power for the port to operate. This
    # error occurs when starting an interface on hardware that requires external
    # power when no power is detected. Solution: Supply proper voltage to your
    # transceiver. Refer to the NI-XNET Hardware Overview in the NI-XNET Hardware
    # and Software Manual for more information.
    MISSING_BUS_POWER = _cconsts.NX_ERR_MISSING_BUS_POWER
    # The connection with a CompactDAQ chassis was lost, and the host software and
    # modules are out of sync. There is no direct recovery for this problem until
    # the chassis is reset. Solutions: Call DAQmx Reset Device as the first VI or
    # function in your application, prior to creating XNET sessions. Alternately,
    # you could reset the CompactDAQ chassis in Measurement and Automation
    # Explorer (MAX).
    CDAQ_CONNECTION_LOST = _cconsts.NX_ERR_CDAQ_CONNECTION_LOST
    # The transceiver value set is invalid (for this port, e.g. LS on a HS port)
    # or you are trying to perform an operation that requires a different
    # transceiver (e.g., trying to change the state of a disconnected
    # transceiver). Solution: set a valid value.
    INVALID_TRANSCEIVER = _cconsts.NX_ERR_INVALID_TRANSCEIVER
    # The baud rate value set is invalid. Solution: set a valid value.
    INVALID_BAUD_RATE = _cconsts.NX_ERR_INVALID_BAUD_RATE
    # No baud rate value has been set. Solution: set a valid value.
    BAUD_RATE_NOT_CONFIGURED = _cconsts.NX_ERR_BAUD_RATE_NOT_CONFIGURED
    # The bit timing values set are invalid. Solution: set valid values.
    INVALID_BIT_TIMINGS = _cconsts.NX_ERR_INVALID_BIT_TIMINGS
    # The baud rate set does not match the transceiver's allowed range. Solution:
    # change either the baud rate or the transceiver.
    BAUD_RATE_XCVR_MISMATCH = _cconsts.NX_ERR_BAUD_RATE_XCVR_MISMATCH
    # The configured terminal is not known for this interface. Solution: Make sure
    # that that you pass in a valid value to Connect Terminals or Disconnect
    # Terminals.
    UNKNOWN_TIMING_SOURCE = _cconsts.NX_ERR_UNKNOWN_TIMING_SOURCE
    # The configured terminal is inappropriate for the hardware. For example,
    # setting a source to FrontPanel0 on XNET hardware that doesn't have
    # front-panel trigger inputs, or selecting PXI_Clk10 for a non-PXI device.
    # Solution: Pick an appropriate terminal for the hardware.
    UNKNOWN_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_UNKNOWN_SYNCHRONIZATION_SOURCE
    # The source that you connected to the Master Timebase destination is missing.
    # When the start trigger is received, the interface verifies that a signal is
    # present on the configured source. This check has determined that this signal
    # is missing. Solution: Verify that your cables are configured correctly and
    # that your timebase source is generating an appropriate waveform.
    MISSING_TIMEBASE_SOURCE = _cconsts.NX_ERR_MISSING_TIMEBASE_SOURCE
    # The source that you connected to the Master Timebase destination is not
    # generating an appropriate signal. When the start trigger is received, the
    # interface verifies that a signal of a known frequency is present on the
    # configured source. This check has determined that this source is generating
    # a signal, but that the signal is not one of the supported frequencies for
    # this hardware. Solution: Verify that your source is generating a signal at a
    # supported frequency.
    UNKNOWN_TIMEBASE_FREQUENCY = _cconsts.NX_ERR_UNKNOWN_TIMEBASE_FREQUENCY
    # You are trying to disconnect a synchronization terminal that is not
    # currently connected. Solution: Only disconnect synchronization terminals
    # that have previously been connected.
    UNCONNECTED_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_UNCONNECTED_SYNCHRONIZATION_SOURCE
    # You are trying to connect a synchronization terminal that is already in use.
    # For example, you are trying to connect a trigger line to the Master Timebase
    # when a different trigger line is already connected to the Master Timebase.
    # Solution: Only connect to synchronization terminals that are not currently
    # in use.
    CONNECTED_SYNCHRONIZATION_TERMINAL = _cconsts.NX_ERR_CONNECTED_SYNCHRONIZATION_TERMINAL
    # You are trying to connect an XNET terminal as a source terminal, but the
    # desired XNET terminal is not valid as a source terminal. Solution: Only
    # connect valid source terminals to the source terminal in XNET Connect
    # Terminals.
    INVALID_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_SOURCE
    # You are trying to connect an XNET terminal as a destination terminal, but
    # the desired XNET terminal is not valid as a destination terminal. Solution:
    # Only connect valid destination terminals to the destination terminal in XNET
    # Connect Terminals.
    INVALID_SYNCHRONIZATION_DESTINATION = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_DESTINATION
    # You are trying to connect two XNET terminals that are incompatible.
    # Solution: Only connect a source and destination terminals that are
    # compatible with each other.
    INVALID_SYNCHRONIZATION_COMBINATION = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_COMBINATION
    # The source that you connected to the Master Timebase destination has
    # disappeared. When the start trigger is received, the interface verifies that
    # a signal is present on the configured source. This check has determined that
    # this signal was present, but while the interface was running, the signal
    # disappeared, so all timebase configuration has reverted to using the onboard
    # (unsynchronized) oscillator. Solution: Verify that your cables are
    # configured correctly and that your timebase source is generating an
    # appropriate waveform the entire time your application is running.
    TIMEBASE_DISAPPEARED = _cconsts.NX_ERR_TIMEBASE_DISAPPEARED
    # You called Read (State : FlexRay : Cycle Macrotick), and the FlexRay
    # Macrotick is not connected as the master timebase of the interface.
    # Solution: Call Connect Terminals to connect source of FlexRay Macrotick to
    # destination of Master Timebase.
    MACROTICK_DISCONNECTED = _cconsts.NX_ERR_MACROTICK_DISCONNECTED
    # The database specified could not be opened. Solution: Check that the alias
    # and/or the file exist and that it is a valid database.
    CANNOT_OPEN_DATABASE_FILE = _cconsts.NX_ERR_CANNOT_OPEN_DATABASE_FILE
    # The cluster was not found in the database. Solution: Make sure you only
    # initialize a cluster in a session that is defined in the database.
    CLUSTER_NOT_FOUND = _cconsts.NX_ERR_CLUSTER_NOT_FOUND
    # The frame was not found in the database. Solution: Make sure you only
    # initialize frames in a session that are defined in the database.
    FRAME_NOT_FOUND = _cconsts.NX_ERR_FRAME_NOT_FOUND
    # The signal was not found in the database. Solution: Make sure you only
    # initialize signals in a session that are defined in the database.
    SIGNAL_NOT_FOUND = _cconsts.NX_ERR_SIGNAL_NOT_FOUND
    # A necessary property for a cluster was not found in the database. Solution:
    # Make sure you only initialize a cluster in a session that is completely
    # defined in the database.
    UNCONFIGURED_CLUSTER = _cconsts.NX_ERR_UNCONFIGURED_CLUSTER
    # A necessary property for a frame was not found in the database. Solution:
    # Make sure you only initialize frames in a session that are completely
    # defined in the database.
    UNCONFIGURED_FRAME = _cconsts.NX_ERR_UNCONFIGURED_FRAME
    # A necessary property for a signal was not found in the database. Solution:
    # Make sure you only initialize signals in a session that are completely
    # defined in the database.
    UNCONFIGURED_SIGNAL = _cconsts.NX_ERR_UNCONFIGURED_SIGNAL
    # Multiple clusters have been specified in one session, either directly
    # (Stream I/O), or through the signals or frames specified. Solution: Make
    # sure that in one session, you open only one cluster, including frames or
    # signals that belong to the same cluster.
    MULTIPLE_CLUSTERS = _cconsts.NX_ERR_MULTIPLE_CLUSTERS
    # You specified a database of ':subordinate:' for a session mode other than
    # mode of Frame Input Stream. Solution: either open a Frame Input Stream
    # session, or use a real or in-memory database.
    SUBORDINATE_NOT_ALLOWED = _cconsts.NX_ERR_SUBORDINATE_NOT_ALLOWED
    # The interface name given does not specify a valid and existing interface.
    # Solution: Use a valid and existing interface. These can be obtained using
    # MAX, XNET system properties, or the LabVIEW XNET Interface IO name. If you
    # are using CompactRIO, refer to the topic "Getting Started with CompactRIO"
    # in the NI-XNET Hardware and Software Help.
    INVALID_INTERFACE = _cconsts.NX_ERR_INVALID_INTERFACE
    # The operation is invalid for this interface (e.g. you tried to open a set of
    # FlexRay frames on a CAN interface, or tried to request a CAN property from a
    # FlexRay interface). Solution: run this operation on a suitable interface.
    INVALID_PROTOCOL = _cconsts.NX_ERR_INVALID_PROTOCOL
    # You tried to set the AutoStart property to FALSE for an Input session. This
    # is not allowed. Solution: don't set the AutoStart property (TRUE is
    # default).
    INPUT_SESSION_MUST_AUTO_START = _cconsts.NX_ERR_INPUT_SESSION_MUST_AUTO_START
    # The property ID you specified is not valid (or not valid for the current
    # session mode or form factor).
    INVALID_PROPERTY_ID = _cconsts.NX_ERR_INVALID_PROPERTY_ID
    # The contents of the property is bigger than the size specified. Use the
    # nxGetPropertySize function to determine the size of the buffer needed.
    INVALID_PROPERTY_SIZE = _cconsts.NX_ERR_INVALID_PROPERTY_SIZE
    # The function you called is not defined for the session mode (e.g. you called
    # a frame I/O function on a signal I/O session).
    INCORRECT_MODE = _cconsts.NX_ERR_INCORRECT_MODE
    # The data that you passed to the XNET Write is too small to hold all the data
    # specified for the session. Solution: determine the number of elements
    # (frames or signals) that you configured for the session, and pass that
    # number of elements to XNET Write.
    BUFFER_TOO_SMALL = _cconsts.NX_ERR_BUFFER_TOO_SMALL
    # For Signal Output sessions, the multiplexer signals used in the session must
    # be specified explicitly in the signal list.
    MUST_SPECIFY_MULTIPLEXERS = _cconsts.NX_ERR_MUST_SPECIFY_MULTIPLEXERS
    # You used an XNET Session IO name, and that session was not found in your
    # LabVIEW project. Solution: Within LabVIEW project, right-click the target
    # (RT or My Computer), and select New > NI-XNET Session. Add the VI that uses
    # the session under the target. If you are using the session with a built
    # application (.EXE), ensure that you copy the built configuration file
    # nixnetSession.txt such that it resides in the same folder as the executable.
    SESSION_NOT_FOUND = _cconsts.NX_ERR_SESSION_NOT_FOUND
    # You used the same XNET session name in multiple top-level VIs, which is not
    # supported. Solution: Use each session in only one top-level VI (application)
    # at a time.
    MULTIPLE_USE_OF_SESSION = _cconsts.NX_ERR_MULTIPLE_USE_OF_SESSION
    # To execute this function properly, the session's list must contain only one
    # frame. Solution: break your session up into multiple, each of which contains
    # only one frame.
    ONLY_ONE_FRAME = _cconsts.NX_ERR_ONLY_ONE_FRAME
    # You used the same alias for different database files which is not allowed.
    # Solution: Use each alias only for a single database file.
    DUPLICATE_ALIAS = _cconsts.NX_ERR_DUPLICATE_ALIAS
    # You try to deploy a database file while another deployment is in progress.
    # Solution: wait until the other deployment has finished and try again.
    DEPLOYMENT_IN_PROGRESS = _cconsts.NX_ERR_DEPLOYMENT_IN_PROGRESS
    # A signal or frame session has been opened, but it doesn't contain signals or
    # frames. Solution: specify at least one signal or frame.
    NO_FRAMES_OR_SIGNALS = _cconsts.NX_ERR_NO_FRAMES_OR_SIGNALS
    # An invalid value has been specified for the 'mode' parameter. Solution:
    # specify a valid value.
    INVALID_MODE = _cconsts.NX_ERR_INVALID_MODE
    # A session was created by references, but no database references have been
    # specified. Solution: specify at least one appropriate database reference
    # (i.e. signal or frame or cluster ref depending on the session mode).
    NEED_REFERENCE = _cconsts.NX_ERR_NEED_REFERENCE
    # The interface has already been opened with different cluster settings than
    # the ones specified for this session. Solution: make sure that the cluster
    # settings agree for the interface, or use a different interface.
    DIFFERENT_CLUSTER_OPEN = _cconsts.NX_ERR_DIFFERENT_CLUSTER_OPEN
    # The cycle repetition of a frame in the database for the FlexRay protocol is
    # invalid. Solution: Make sure that the cycle repetition is a power of 2
    # between 1 and 64.
    FLEX_RAY_INVALID_CYCLE_REP = _cconsts.NX_ERR_FLEX_RAY_INVALID_CYCLE_REP
    # You called XNET Clear for the session, then tried to perform another
    # operation. Solution: Defer clear (session close) until you are done using
    # it. This error can also occur if you branch a wire after creating the
    # session. Solution: Do not branch a session to multiple flows in the diagram.
    SESSION_CLEARED = _cconsts.NX_ERR_SESSION_CLEARED
    # You called Create Session VI with a list of items that does not match the
    # mode. This includes using: 1) signal items for a Frame I/O mode 2) frame
    # items for a Signal I/O mode 3) cluster item for a mode other than Frame
    # Input Stream or Frame Output Stream
    WRONG_MODE_FOR_CREATE_SELECTION = _cconsts.NX_ERR_WRONG_MODE_FOR_CREATE_SELECTION
    # You tried to create a new session while the interface is already running.
    # Solution: Create all sessions before starting any of them.
    INTERFACE_RUNNING = _cconsts.NX_ERR_INTERFACE_RUNNING
    # You wrote a frame whose payload length is larger than the maximum payload
    # allowed by the database (e.g. wrote 10 bytes for CAN frame, max 8 bytes).
    # Solution: Never write more payload bytes than the Payload Length Maximum
    # property of the session.
    FRAME_WRITE_TOO_LARGE = _cconsts.NX_ERR_FRAME_WRITE_TOO_LARGE
    # You called a Read function with a nonzero timeout, and you used a negative
    # numberToRead. Negative value for numberToRead requests all available data
    # from the Read, which is ambiguous when used with a timeout. Solutions: 1)
    # Pass timeout of and numberToRead of -1, to request all available data. 2)
    # Pass timeout > 0, and numberToRead > 0, to wait for a specific number of
    # data elements.
    TIMEOUT_WITHOUT_NUM_TO_READ = _cconsts.NX_ERR_TIMEOUT_WITHOUT_NUM_TO_READ
    # Timestamps are not (yet) supported for Write Signal XY. Solution: Do not
    # provide a timestamp array for Write Signal XY.
    TIMESTAMPS_NOT_SUPPORTED = _cconsts.NX_ERR_TIMESTAMPS_NOT_SUPPORTED
    # The condition parameter passed to Wait is not known. Solution: Pass a valid
    # parameter.
    UNKNOWN_CONDITION = _cconsts.NX_ERR_UNKNOWN_CONDITION
    # You attempted an I/O operation, but the session is not yet started (and the
    # AutoStart property is set to FALSE). Solution: call Start before you use
    # this IO operation.
    SESSION_NOT_STARTED = _cconsts.NX_ERR_SESSION_NOT_STARTED
    # The maximum number of Wait operations has been exceeded. Solution: If you
    # are waiting for multiple events on the interface, use fewer Wait operations
    # on this interface (even for multiple sessions). If you are waiting for
    # multiple events for a frame (e.g. transmit complete), use only one Wait at a
    # time for that frame.
    MAX_WAITS_EXCEEDED = _cconsts.NX_ERR_MAX_WAITS_EXCEEDED
    # You used an invalid name for an XNET Device. Solution: Get valid XNET Device
    # names from the XNET System properties (only).
    INVALID_DEVICE = _cconsts.NX_ERR_INVALID_DEVICE
    # A terminal name passed to ConnectTerminals or DisconnectTerminals is
    # unknown. Solution: only pass valid names.
    INVALID_TERMINAL_NAME = _cconsts.NX_ERR_INVALID_TERMINAL_NAME
    # You tried to blink the port LEDs but these are currently busy. Solution:
    # stop all applications running on that port; do not access it from MAX or LV
    # Project.
    PORT_LEDS_BUSY = _cconsts.NX_ERR_PORT_LE_DS_BUSY
    # You tried to set a FlexRay keyslot ID that is not listed as valid in the
    # database. Solution: only pass slot IDs of frames that have the startup or
    # sync property set in the database.
    INVALID_KEYSLOT = _cconsts.NX_ERR_INVALID_KEYSLOT
    # You tried to set a queue size that is bigger than the maximum allowed.
    # Solution: Specify an in-range queue size.
    MAX_QUEUE_SIZE_EXCEEDED = _cconsts.NX_ERR_MAX_QUEUE_SIZE_EXCEEDED
    # You wrote a frame whose payload length is different than the payload length
    # configured by the database. Solution: Never write a different payload length
    # for a frame that is different than the configured payload length.
    FRAME_SIZE_MISMATCH = _cconsts.NX_ERR_FRAME_SIZE_MISMATCH
    # The index to indicate an session list element is too large. Solution:
    # Specify an index in the range ... NumInList-1.
    INDEX_TOO_BIG = _cconsts.NX_ERR_INDEX_TOO_BIG
    # You have tried to create a session that is invalid for the mode of the
    # driver/firmware. For example, you are using the Replay Exclusive mode for
    # Stream Output and you have an output session open.
    SESSION_MODE_INCOMPATIBILITY = _cconsts.NX_ERR_SESSION_MODE_INCOMPATIBILITY
    # You have tried to create a session using a frame that is incompatible with
    # the selected session type. For example, you are using a LIN diagnostic frame
    # with a single point output session.
    SESSION_TYPE_FRAME_INCOMPATIBILITY = _cconsts.NX_ERR_SESSION_TYPE_FRAME_INCOMPATIBILITY
    # The trigger signal for a frame is allowed only in Single Point Signal
    # sessions (Input or Output). For Output Single Point Signal sessions, only
    # one trigger signal is allowed per frame. Solution: Do not use the trigger
    # signal, or change to a single point I/O session.
    TRIGGER_SIGNAL_NOT_ALLOWED = _cconsts.NX_ERR_TRIGGER_SIGNAL_NOT_ALLOWED
    # To execute this function properly, the session's list must contain only one
    # cluster. Solution: Use only one cluster in the session.
    ONLY_ONE_CLUSTER = _cconsts.NX_ERR_ONLY_ONE_CLUSTER
    # You attempted to convert a CAN or LIN frame with a payload length greater
    # than 8. For example, you may be converting a frame that uses a higher layer
    # transport protocol, such as SAE-J1939. NI-XNET currently supports conversion
    # of CAN/LIN frames only (layer 2). Solutions: 1) Implement higher layer
    # protocols (including signal conversion) within your code. 2) Contact
    # National Instruments to request this feature in a future version.
    CONVERT_INVALID_PAYLOAD = _cconsts.NX_ERR_CONVERT_INVALID_PAYLOAD
    # Allocation of memory failed for the data returned from LabVIEW XNET Read.
    # Solutions: 1) Wire a smaller "number to read" to XNET Read (default -1 uses
    # queue size). 2) For Signal Input Waveform, use a smaller resample rate. 3)
    # Set smaller value for session's queue size property (default is large to
    # avoid loss of data).
    MEMORY_FULL_READ_DATA = _cconsts.NX_ERR_MEMORY_FULL_READ_DATA
    # Allocation of memory failed in the firmware. Solutions: 1) Create less
    # firmware objects 2) Set smaller value for output session's queue size
    # property (default is large to avoid loss of data).
    MEMORY_FULL_FIRMWARE = _cconsts.NX_ERR_MEMORY_FULL_FIRMWARE
    # The NI-XNET driver no longer can communicate with the device. Solution: Make
    # sure the device has not been removed from the computer.
    COMMUNICATION_LOST = _cconsts.NX_ERR_COMMUNICATION_LOST
    # A LIN schedule has an invalid priority. Solution: Use a valid priority (0 =
    # NULL schedule, 1..254 = Run once schedule, 255 = Continuous schedule).
    INVALID_PRIORITY = _cconsts.NX_ERR_INVALID_PRIORITY
    # (Dis)ConnectTerminals is not allowed for XNET C Series modules. Solution: To
    # connect the module start trigger, use the Session property Interface Source
    # Terminal Start Trigger.
    SYNCHRONIZATION_NOT_ALLOWED = _cconsts.NX_ERR_SYNCHRONIZATION_NOT_ALLOWED
    # You requested a time (like Start or Communication Time) before the event has
    # happened. Solution: Request the time only after it occurred.
    TIME_NOT_REACHED = _cconsts.NX_ERR_TIME_NOT_REACHED
    # An internal input queue overflowed. Solution: Attempt to pull data from the
    # hardware faster. If you are connected by an external bus (for example, USB
    # or Ethernet), you can try to use a faster connection.
    INTERNAL_INPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_INTERNAL_INPUT_QUEUE_OVERFLOW
    # A bad firmware image file can not be loaded to the hardware. Solution:
    # Uninstall and reinstall the NI-XNET software as the default firmware file
    # may be corrupt. If you are using a custom firmware file, try rebuilding it.
    BAD_IMAGE_FILE = _cconsts.NX_ERR_BAD_IMAGE_FILE
    # The encoding of embedded network data (CAN, FlexRay, LIN, etc.) within the
    # TDMS file is invalid. Solutions: 1) In the application that wrote (created)
    # the logfile, and the application in which you are reading it, confirm that
    # both use the same major version for frame data encoding
    # (NI_network_frame_version property of the TDMS channel). 2) Ensure that your
    # file was not corrupted.
    INVALID_LOGFILE = _cconsts.NX_ERR_INVALID_LOGFILE
    # The NI-XNET hardware no longer can communicate with the transceiver cable.
    # This may be due to the cable being removed, a power loss event, an over
    # voltage condition on the power input, or a general communication error.
    # Solution: Make sure the dongle is properly latched and, for some hardware,
    # external power is properly applied. To detect other errors, stop your
    # application and execute a self test.
    DONGLE_COMMUNICATION_LOST = _cconsts.NX_ERR_DONGLE_COMMUNICATION_LOST
    # A property value was out of range or incorrect. Solution: specify a correct
    # value.
    INVALID_PROPERTY_VALUE = _cconsts.NX_ERR_INVALID_PROPERTY_VALUE
    # Integration of the interface into the FlexRay cluster failed, so
    # communication did not start for the interface. Solution: check the cluster
    # and/or interface parameters and verify that there are startup frames
    # defined.
    FLEX_RAY_INTEGRATION_FAILED = _cconsts.NX_ERR_FLEX_RAY_INTEGRATION_FAILED
    # The PDU was not found in the database. Solution: Make sure you initialize
    # only PDUs in a session that are defined in the database.
    PDU_NOT_FOUND = _cconsts.NX_ERR_PDU_NOT_FOUND
    # A necessary property for a PDU was not found in the database. Solution: Make
    # sure you initialize only PDUs in a session that are completely defined in
    # the database.
    UNCONFIGURED_PDU = _cconsts.NX_ERR_UNCONFIGURED_PDU
    # You tried to open the same PDU twice. This is not permitted. Solution: Open
    # each PDU only once.
    DUPLICATE_PDU_OBJECT = _cconsts.NX_ERR_DUPLICATE_PDU_OBJECT
    # You can access this database object only by PDU, not by frame. Solution: For
    # CAN and LIN, this is not supported by the current version of NI-XNET; for
    # FlexRay, make sure the database is set to use PDUs.
    NEED_PDU = _cconsts.NX_ERR_NEED_PDU
    # Remote communication with the LabVIEW RT target failed. Solution: check if
    # NI-XNET has been installed on the RT target and check if the NI-XNET RPC
    # server has been started.
    RPC_COMMUNICATION = _cconsts.NX_ERR_RPC_COMMUNICATION
    # File transfer communication with the LabVIEW Real-Time (RT) target failed.
    # Solution: check if the RT target has been powered on, the RT target has been
    # connected to the network, and if the IP address settings are correct.
    FILE_TRANSFER_COMMUNICATION = _cconsts.NX_ERR_FILE_TRANSFER_COMMUNICATION
    # File transfer communication with the LabVIEW Real-Time (RT) target failed.
    # Solution: check if the RT target has been powered on, the RT target has been
    # connected to the network, and if the IP address settings are correct.
    FTP_COMMUNICATION = _cconsts.NX_ERR_FTP_COMMUNICATION
    # File transfer to the LabVIEW Real-Time (RT) target failed, because the
    # required files could not be accessed. Solution: You may have executed a VI
    # that opened the database, but did not close. If that is the case, you should
    # change the VI to call Database Close, then reboot the RT controller to
    # continue.
    FILE_TRANSFER_ACCESS = _cconsts.NX_ERR_FILE_TRANSFER_ACCESS
    # File transfer to the LabVIEW Real-Time (RT) target failed, because the
    # required files could not be accessed. Solution: You may have executed a VI
    # that opened the database, but did not close. If that is the case, you should
    # change the VI to call Database Close, then reboot the RT controller to
    # continue.
    FTP_FILE_ACCESS = _cconsts.NX_ERR_FTP_FILE_ACCESS
    # The database file you want to use is already assigned to another alias.
    # Solution: Each database file can only be assigned to a single alias. Use the
    # alias that is already assigned to the database instead.
    DATABASE_ALREADY_IN_USE = _cconsts.NX_ERR_DATABASE_ALREADY_IN_USE
    # An internal file used by NI-XNET could not be accessed. Solution: Make sure
    # that the internal NI-XNET files are not write protected and that the
    # directories for these files exist.
    INTERNAL_FILE_ACCESS = _cconsts.NX_ERR_INTERNAL_FILE_ACCESS
    # The file cannot be deployed because another file deployment is already
    # active. Solution: wait until the other file deployment has finished and try
    # again.
    FILE_TRANSFER_ACTIVE = _cconsts.NX_ERR_FILE_TRANSFER_ACTIVE
    # The nixnet.dll or one of its components could not be loaded. Solution: try
    # reinstalling NI-XNET. If the error persists,contact National Instruments.
    DLL_LOAD = _cconsts.NX_ERR_DLL_LOAD
    # You attempted to perform an action on a session or interface that is
    # started, and the action that requires the session/interface to be stopped.
    # Solution: Stop the object before performing this action.
    OBJECT_STARTED = _cconsts.NX_ERR_OBJECT_STARTED
    # You have passed a default payload to the firmware where the number of bytes
    # in the payload is larger than the number of bytes that this frame can
    # transmit. Solution: Decrease the number of bytes in your default payload.
    DEFAULT_PAYLOAD_NUM_BYTES = _cconsts.NX_ERR_DEFAULT_PAYLOAD_NUM_BYTES
    # You attempted to set a CAN arbitration ID with an invalid value. For
    # example, a CAN standard arbitration ID supports only 11 bits. If you attempt
    # to set a standard arbitration ID that uses more than 11 bits, this error is
    # returned. Solution: Use a valid arbitration ID.
    INVALID_ARBITRATION_ID = _cconsts.NX_ERR_INVALID_ARBITRATION_ID
    # You attempted to set a LIN ID with an invalid value. For example, a LIN ID
    # supports only 6 bits. If you attempt to set an ID that uses more than 6
    # bits, this error is returned. Solution: Use a valid LIN ID.
    INVALID_LIN_ID = _cconsts.NX_ERR_INVALID_LIN_ID
    # Too many open files. NI-XNET allows up to 7 database files to be opened
    # simultaneously. Solution: Open fewer files.
    TOO_MANY_OPEN_FILES = _cconsts.NX_ERR_TOO_MANY_OPEN_FILES
    # Bad reference has been passed to a database function, e.g. a session
    # reference, or frame reference to retrieve properties from a signal.
    DATABASE_BAD_REFERENCE = _cconsts.NX_ERR_DATABASE_BAD_REFERENCE
    # Creating a database file failed. Solution: Verify access rights to the
    # destination directory or check if overwritten file has read only permission.
    CREATE_DATABASE_FILE = _cconsts.NX_ERR_CREATE_DATABASE_FILE
    # A cluster with the same name already exists in the database. Solution: Use
    # another name for this cluster.
    DUPLICATE_CLUSTER_NAME = _cconsts.NX_ERR_DUPLICATE_CLUSTER_NAME
    # A frame with the same name already exists in the cluster. Solution: Use
    # another name for this frame.
    DUPLICATE_FRAME_NAME = _cconsts.NX_ERR_DUPLICATE_FRAME_NAME
    # A signal with the same name already exists in the frame. Solution: Use
    # another name for this signal.
    DUPLICATE_SIGNAL_NAME = _cconsts.NX_ERR_DUPLICATE_SIGNAL_NAME
    # An ECU with the same name already exists in the cluster. Solution: Use
    # another name for this ECU.
    DUPLICATE_ECU_NAME = _cconsts.NX_ERR_DUPLICATE_ECU_NAME
    # A subframe with the same name already exists in the frame. Solution: Use
    # another name for this subframe.
    DUPLICATE_SUBFRAME_NAME = _cconsts.NX_ERR_DUPLICATE_SUBFRAME_NAME
    # The operation is improper for the protocol in use, e.g. you cannot assign
    # FlexRay channels to a CAN frame.
    IMPROPER_PROTOCOL = _cconsts.NX_ERR_IMPROPER_PROTOCOL
    # Wrong parent relationship for a child that you are creating with XNET
    # Database Create.
    OBJECT_RELATION = _cconsts.NX_ERR_OBJECT_RELATION
    # The retrieved required property is not defined on the specified object.
    # Solution: Make sure that your database file has this property defined or
    # that you set it in the objects created in memory.
    UNCONFIGURED_REQUIRED_PROPERTY = _cconsts.NX_ERR_UNCONFIGURED_REQUIRED_PROPERTY
    # The feature is not supported under LabVIEW RT, e.g.Save Database
    NOT_SUPPORTED_ON_RT = _cconsts.NX_ERR_NOT_SUPPORTED_ON_RT
    # The object name contains unsupported characters. The name must contain just
    # alphanumeric characters and the underscore, but cannot begin with a digit.
    # The maximum size is 128.
    NAME_SYNTAX = _cconsts.NX_ERR_NAME_SYNTAX
    # Unsupported database format. For reading a database, the extension must be
    # .xml, .dbc, .ncd, or .ldf. For saving, the extension must be .xml or .ldf
    FILE_EXTENSION = _cconsts.NX_ERR_FILE_EXTENSION
    # Database object not found, e.g. an object with given name doesn't exist.
    DATABASE_OBJECT_NOT_FOUND = _cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND
    # Database cache file cannot be removed or replaced on the disc, e.g. it is
    # write-protected.
    REMOVE_DATABASE_CACHE_FILE = _cconsts.NX_ERR_REMOVE_DATABASE_CACHE_FILE
    # You are trying to write a read-only property, e.g. the mux value on a signal
    # is a read only property (can be changed on the subframe).
    READ_ONLY_PROPERTY = _cconsts.NX_ERR_READ_ONLY_PROPERTY
    # You are trying to change a signal to be a mux signal, but a mux is already
    # defined in this frame
    FRAME_MUX_EXISTS = _cconsts.NX_ERR_FRAME_MUX_EXISTS
    # You are trying to define FlexRay in-cycle-repetition slots before defining
    # the first slot. Define the first slot (frame ID) before defining
    # in-cycle-repetition slots.
    UNDEFINED_FIRST_SLOT = _cconsts.NX_ERR_UNDEFINED_FIRST_SLOT
    # You are trying to define FlexRay in-cycle-repetition channels before
    # defining the first channels. Define the Channel Assignment on a frame before
    # defining in-cycle-repetition channels.
    UNDEFINED_FIRST_CHANNELS = _cconsts.NX_ERR_UNDEFINED_FIRST_CHANNELS
    # You must define the protocol before setting this property, e.g. the frame ID
    # has a different meaning in a CAN or FlexRay cluster.
    UNDEFINED_PROTOCOL = _cconsts.NX_ERR_UNDEFINED_PROTOCOL
    # The database information on the real-time system has been created with an
    # older NI-XNET version. This version is no longer supported. To correct this
    # error, re-deploy your database to the real-time system.
    OLD_DATABASE_CACHE_FILE = _cconsts.NX_ERR_OLD_DATABASE_CACHE_FILE
    # Frame ConfigStatus: A signal within the frame exceeds the frame boundaries
    # (Payload Length).
    DB_CONFIG_SIG_OUT_OF_FRAME = _cconsts.NX_ERR_DB_CONFIG_SIG_OUT_OF_FRAME
    # Frame ConfigStatus: A signal within the frame overlaps another signal.
    DB_CONFIG_SIG_OVERLAPPED = _cconsts.NX_ERR_DB_CONFIG_SIG_OVERLAPPED
    # Frame ConfigStatus: A integer signal within the frame is defined with more
    # than 52 bits. Not supported.
    DB_CONFIG_SIG52_BIT_INTEGER = _cconsts.NX_ERR_DB_CONFIG_SIG52_BIT_INTEGER
    # Frame ConfigStatus: Frame is defined with wrong number of bytes Allowed
    # values: - CAN: 0-8, - Flexray: 0-254 and even number.
    DB_CONFIG_FRAME_NUM_BYTES = _cconsts.NX_ERR_DB_CONFIG_FRAME_NUM_BYTES
    # You are trying to add transmitted FlexRay frames to an ECU, with at least
    # two of them having Startup or Sync property on. Only one Sync or Startup
    # frame is allowed to be sent by an ECU.
    MULT_SYNC_STARTUP = _cconsts.NX_ERR_MULT_SYNC_STARTUP
    # You are trying to add TX/RX frames to an ECU which are defined in a
    # different cluster than the ECU.
    INVALID_CLUSTER = _cconsts.NX_ERR_INVALID_CLUSTER
    # Database name parameter is incorrect. Solution: Use a valid name for the
    # database, e.g. ":memory:" for in-memory database.
    DATABASE_NAME = _cconsts.NX_ERR_DATABASE_NAME
    # Database object is locked because it is used in a session. Solution:
    # Configure the database before using it in a session.
    DATABASE_OBJECT_LOCKED = _cconsts.NX_ERR_DATABASE_OBJECT_LOCKED
    # Alias name passed to a function is not defined. Solution: Define the alias
    # before calling the function.
    ALIAS_NOT_FOUND = _cconsts.NX_ERR_ALIAS_NOT_FOUND
    # Database file cannot be saved because frames are assigned to FlexRay
    # channels not defined in the cluster. Solution: Verify that all frames in the
    # FlexRay cluster are assigned to an existing cluster channel.
    CLUSTER_FRAME_CHANNEL_RELATION = _cconsts.NX_ERR_CLUSTER_FRAME_CHANNEL_RELATION
    # Frame ConfigStatus: This FlexRay frame transmitted in a dynamic segment uses
    # both channels A and B. This is not allowed. Solution: Use either channel A
    # or B.
    DYN_FLEX_RAY_FRAME_CHAN_AAND_B = _cconsts.NX_ERR_DYN_FLEX_RAY_FRAME_CHAN_AAND_B
    # Database is locked because it is being modified by an another instance of
    # the same application. Solution: Close the database in the other application
    # instance.
    DATABASE_LOCKED_IN_USE = _cconsts.NX_ERR_DATABASE_LOCKED_IN_USE
    # A frame name is ambiguous, e.g. a frame with the same name exists in another
    # cluster. Solution: Specify the cluster name for the frame using the required
    # syntax.
    AMBIGUOUS_FRAME_NAME = _cconsts.NX_ERR_AMBIGUOUS_FRAME_NAME
    # A signal name is ambiguous, e.g. a signal with the same name exists in
    # another frame. Solution: Use [frame].[signal] syntax for the signal.
    AMBIGUOUS_SIGNAL_NAME = _cconsts.NX_ERR_AMBIGUOUS_SIGNAL_NAME
    # An ECU name is ambiguous, e.g. an ECU with the same name exists in another
    # cluster. Solution: Specify the cluster name for the ECU using the required
    # syntax.
    AMBIGUOUS_ECU_NAME = _cconsts.NX_ERR_AMBIGUOUS_ECU_NAME
    # A subframe name is ambiguous, e.g. a subframe with the same name exists in
    # another cluster. Solution: Specify the cluster name for the subframe using
    # the required syntax.
    AMBIGUOUS_SUBFRAME_NAME = _cconsts.NX_ERR_AMBIGUOUS_SUBFRAME_NAME
    # A LIN schedule name is ambiguous, e.g. a schedule with the same name exists
    # in another cluster. Solution: Specify the cluster name for the schedule
    # using the required syntax.
    AMBIGUOUS_SCHEDULE_NAME = _cconsts.NX_ERR_AMBIGUOUS_SCHEDULE_NAME
    # A LIN schedule with the same name already exists in the database. Solution:
    # Use another name for this schedule.
    DUPLICATE_SCHEDULE_NAME = _cconsts.NX_ERR_DUPLICATE_SCHEDULE_NAME
    # A LIN diagnostic schedule change requires the diagnostic schedule to be
    # defined in the database. Solution: Define the diagnostic schedule in the
    # database.
    DIAGNOSTIC_SCHEDULE_NOT_DEFINED = _cconsts.NX_ERR_DIAGNOSTIC_SCHEDULE_NOT_DEFINED
    # Multiplexers (mode-dependent signals) are not supported when the given
    # protocol is used. Solution: Contact National Instruments to see whether
    # there is a newer NI-XNET version that supports multiplexers for the given
    # protocol.
    PROTOCOL_MUX_NOT_SUPPORTED = _cconsts.NX_ERR_PROTOCOL_MUX_NOT_SUPPORTED
    # Saving a FIBEX file containing a LIN cluster is not supported in this
    # NI-XNET version. Solution: Contact National Instruments to see whether there
    # is a newer NI-XNET version that supports saving a FIBEX file that contains a
    # LIN cluster.
    SAVE_LI_NNOT_SUPPORTED = _cconsts.NX_ERR_SAVE_LI_NNOT_SUPPORTED
    # This property requires an ECU configured as LIN master to be present in this
    # cluster. Solution: Create a LIN master ECU in this cluster.
    LI_NMASTER_NOT_DEFINED = _cconsts.NX_ERR_LI_NMASTER_NOT_DEFINED
    # You cannot mix open of NI-XNET database objects as both manual and
    # automatic. You open manually by calling the Database Open VI. You open
    # automatically when you 1) wire the IO name directly to a property node or
    # VI, 2) branch a wire to multiple data flows on the diagram, 3) use the IO
    # name with a VI or property node after closing it with the Database Close VI.
    # Solution: Change your diagram to use the manual technique in all locations
    # (always call Open and Close VIs), or to use the automatic technique in all
    # locations (never call Open or Close VIs).
    MIX_AUTO_MANUAL_OPEN = _cconsts.NX_ERR_MIX_AUTO_MANUAL_OPEN
    # Due to problems in LabVIEW versions 8.5 through 8.6.1, automatic open of
    # NI-XNET database objects is not supported. You open automatically when you
    # 1) wire the IO name directly to a property node or VI, 2) branch a wire to
    # multiple data flows on the diagram, 3) use the IO name with a VI or property
    # node after closing it with the Database Close VI. Solution: Change your
    # diagram to call the Database Open VI prior to any use (VI or property node)
    # in a data flow (including a new wire branch). Change your diagram to call
    # the Database Close VI when you are finished using the database in your
    # application.
    AUTO_OPEN_NOT_SUPPORTED = _cconsts.NX_ERR_AUTO_OPEN_NOT_SUPPORTED
    # You called a Write function with the number of array elements (frames or
    # signals) different than the number of elements configured in the session
    # (such as the "list" parameter of the Create Session function). Solution:
    # Write the same number of elements as configured in the session.
    WRONG_NUM_SIGNALS_WRITTEN = _cconsts.NX_ERR_WRONG_NUM_SIGNALS_WRITTEN
    # You used XNET session from multiple LabVIEW projects (or multiple
    # executables), which NI-XNET does not support. Solution: Run XNET sessions in
    # only one LabVIEW project at a time.
    MULTIPLE_LV_PROJECT = _cconsts.NX_ERR_MULTIPLE_LV_PROJECT
    # When an XNET session is used at runtime, all sessions in the same scope are
    # created on the interface. The same scope is defined as all sessions within
    # the same LabVIEW project which use the same cluster and interface (same
    # physical cable configuration). If you attempt to use a session in the same
    # scope after running the VI, this error occurs. The most likely cause is that
    # you added a new session, and tried to use that new session in a running VI.
    # Solution: Configure all session in LabVIEW project, then run the VI(s) that
    # use those sessions.
    SESSION_CONFLICT_LV_PROJECT = _cconsts.NX_ERR_SESSION_CONFLICT_LV_PROJECT
    # You used an empty name for an XNET database object (database, cluster, ECU,
    # frame, or signal). Empty name is not supported. Solution: Refer to NI-XNET
    # help for IO names to review the required syntax for the name, and change
    # your code to use that syntax.
    DB_OBJECT_NAME_EMPTY = _cconsts.NX_ERR_DB_OBJECT_NAME_EMPTY
    # You used a name for an XNET database object (such as frame or signal) that
    # did not include a valid cluster selection. Solution: Refer to the NI-XNET
    # help for the IO name that you are using, and use the syntax specified for
    # that class, which includes the cluster selection.
    MISSING_ALIAS_IN_DB_OBJECT_NAME = _cconsts.NX_ERR_MISSING_ALIAS_IN_DB_OBJECT_NAME
    # Unsupported FIBEX file version. Solution: Use only FIBEX versions that are
    # supported by this version of NI-XNET. Please see the NI-XNET documentation
    # for information on which FIBEX versions are currently supported.
    FIBEX_IMPORT_VERSION = _cconsts.NX_ERR_FIBEX_IMPORT_VERSION
    # You used an empty name for the XNET Session. Empty name is not supported.
    # Solution: Use a valid XNET session name from your LabVIEW project.
    EMPTY_SESSION_NAME = _cconsts.NX_ERR_EMPTY_SESSION_NAME
    # There is not enough message RAM on the FlexRay hardware to configure the
    # data partition for the object(s). Solution: Please refer to the manual for
    # limitations on the number of objects that can be created at any given time
    # based on the payload length.
    NOT_ENOUGH_MESSAGE_RAM_FOR_OBJECT = _cconsts.NX_ERR_NOT_ENOUGH_MESSAGE_RAM_FOR_OBJECT
    # The FlexRay keyslot ID has been configured and a startup session has been
    # created. Either the keyslot ID needs to be configured OR the startup session
    # needs to be created. Both cannot exist at the same time. Solution: Choose a
    # single method to configure startup sessions in your application.
    KEY_SLOT_ID_CONFIG = _cconsts.NX_ERR_KEY_SLOT_ID_CONFIG
    # An unsupported session was created. For example, stream output is not
    # supported on FlexRay hardware. Solution: Only use supported sessions in your
    # application.
    UNSUPPORTED_SESSION = _cconsts.NX_ERR_UNSUPPORTED_SESSION
    # An XNET session was created after starting the Interface. Only the Stream
    # Input session in the subordinate mode can be created after the Interface has
    # started. Solution: Create sessions prior to starting the XNET Interface in
    # your application.
    OBJECT_CREATED_AFTER_START = _cconsts.NX_ERR_OBJECT_CREATED_AFTER_START
    # The Single Slot property was enabled on the XNET FlexRay Interface after the
    # interface had started. Solution: Enable the Single Slot property prior to
    # starting the XNET FlexRay Interface.
    SINGLE_SLOT_ENABLED_AFTER_START = _cconsts.NX_ERR_SINGLE_SLOT_ENABLED_AFTER_START
    # The FlexRay macrotick offset specified for XNET Create Timing Source is
    # unsupported. Example: Specifying a macrotick offset greater than
    # MacroPerCycle will result in this error. Solution: Specify a macrotick
    # offset within the supported range for the cluster.
    UNSUPPORTED_NUM_MACROTICKS = _cconsts.NX_ERR_UNSUPPORTED_NUM_MACROTICKS
    # You used invalid syntax in the name of a database object (signal, frame, or
    # ECU). For example, you may have specified a frame's name as
    # [cluster].[frame], which is allowed in NI-XNET for C/C++, but not NI-XNET
    # for LabVIEW. Solution: Use the string syntax specified in the help topic for
    # the XNET I/O name class you are using.
    BAD_SYNTAX_IN_DATABASE_OBJECT_NAME = _cconsts.NX_ERR_BAD_SYNTAX_IN_DATABASE_OBJECT_NAME
    # A LIN schedule entry name is ambiguous, e.g. a schedule entry with the same
    # name exists in another schedule. Solution: Specify the schedule name for the
    # schedule entry using the required syntax.
    AMBIGUOUS_SCHEDULE_ENTRY_NAME = _cconsts.NX_ERR_AMBIGUOUS_SCHEDULE_ENTRY_NAME
    # A LIN schedule entry with the same name already exists in the schedule.
    # Solution: Use another name for this schedule entry.
    DUPLICATE_SCHEDULE_ENTRY_NAME = _cconsts.NX_ERR_DUPLICATE_SCHEDULE_ENTRY_NAME
    # At least one of the frames in the session has an undefined identifier.
    # Solution: Set the frame's "Identifier (Slot)" property before creating the
    # session.
    UNDEFINED_FRAME_ID = _cconsts.NX_ERR_UNDEFINED_FRAME_ID
    # At least one of the frames in the session has an undefined payload length.
    # Solution: Set the frame's "Payload Length (in bytes)" property before
    # creating the session.
    UNDEFINED_FRAME_PAYLOAD_LENGTH = _cconsts.NX_ERR_UNDEFINED_FRAME_PAYLOAD_LENGTH
    # At least one of the signals in the session has an undefined start bit.
    # Solution: Set the "Start Bit" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_START_BIT = _cconsts.NX_ERR_UNDEFINED_SIGNAL_START_BIT
    # At least one of the signals in the session has an undefined number of bits.
    # Solution: Set the "Number of Bits" property of the signal before creating
    # the session.
    UNDEFINED_SIGNAL_NUM_BITS = _cconsts.NX_ERR_UNDEFINED_SIGNAL_NUM_BITS
    # At least one of the signals in the session has an undefined byte order.
    # Solution: Set the "Byte Order" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_BYTE_ORDER = _cconsts.NX_ERR_UNDEFINED_SIGNAL_BYTE_ORDER
    # At least one of the signals in the session has an undefined data type.
    # Solution: Set the "Data Type" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_DATA_TYPE = _cconsts.NX_ERR_UNDEFINED_SIGNAL_DATA_TYPE
    # At least one of the subframes in the session has an undefined multiplexer
    # value. Solution: Set the "Multiplexer Value" property of the subframe before
    # creating the session.
    UNDEFINED_SUBF_MUX_VALUE = _cconsts.NX_ERR_UNDEFINED_SUBF_MUX_VALUE
    # You provided an invalid index to Write (State LIN Schedule Change).
    # Solution: Use a number from to N-1, where N is the number of LIN schedules
    # returned from the cluster property LIN Schedules. If you are using LabVIEW,
    # the string for the number must be decimal (not hexadecimal).
    INVALID_LIN_SCHED_INDEX = _cconsts.NX_ERR_INVALID_LIN_SCHED_INDEX
    # You provided an invalid name to Write (State LIN Schedule Change). Solution:
    # Use a valid LIN schedule name returned from the cluster property LIN
    # Schedules, or the session property Interface LIN Schedules. You can use the
    # short name (schedule only) or long name (schedule plus database and
    # cluster).
    INVALID_LIN_SCHED_NAME = _cconsts.NX_ERR_INVALID_LIN_SCHED_NAME
    # You provided an invalid active index for the session property.
    INVALID_ACTIVE_FRAME_INDEX = _cconsts.NX_ERR_INVALID_ACTIVE_FRAME_INDEX
    # You provided an invalid name for Frame:Active of the session property node.
    # Solution: Use a valid item name from the session's List property. You can
    # use the short name (frame or signal only) or long name (frame/signal plus
    # database and cluster).
    INVALID_ACTIVE_FRAME_NAME = _cconsts.NX_ERR_INVALID_ACTIVE_FRAME_NAME
    # The database you are using requires using PDUs, and the operation is
    # ambiguous with respect to PDUs. Example: You are trying to get the frame
    # parent of the signal, but the PDU in which the signal is contained is
    # referenced in multiple frames.
    AMBIGUOUS_PDU = _cconsts.NX_ERR_AMBIGUOUS_PDU
    # A PDU with the same name already exists in the cluster. Solution: Use
    # another name for this PDU.
    DUPLICATE_PDU = _cconsts.NX_ERR_DUPLICATE_PDU
    # You are trying to assign start bits or update bits to PDUs referenced in a
    # frame, but the number of elements in this array is different than the number
    # of referenced PDUs. Solution: Use the same number of elements in the array
    # as in the PDU references array.
    NUMBER_OF_PD_US = _cconsts.NX_ERR_NUMBER_OF_PD_US
    # The configuration of this object requires using advanced PDUs, which the
    # given protocol does not support. Solution: You cannot use this object in the
    # given protocol.
    PD_US_REQUIRED = _cconsts.NX_ERR_PD_US_REQUIRED
    # The maximum number of PDUs has been exceeded. Solution: Use fewer PDUs in
    # your sessions.
    MAX_PD_US = _cconsts.NX_ERR_MAX_PD_US
    # This mode value is not currently supported. Solution: Use a valid value.
    UNSUPPORTED_MODE = _cconsts.NX_ERR_UNSUPPORTED_MODE
    # The firmware image on your XNET hardware is corrupted. Solution: Update the
    # firmware of this XNET hardware in MAX.
    BAD_FPGA_SIGNATURE = _cconsts.NX_ERR_BAD_FPGA_SIGNATURE
    BADC_SERIES_FPGA_SIGNATURE = _cconsts.NX_ERR_BADC_SERIES_FPGA_SIGNATURE
    # The firmware version of your XNET hardware is not in sync with your host
    # computer. Solution: Update the firmware of this XNET hardware in MAX.
    BAD_FPGA_REVISION = _cconsts.NX_ERR_BAD_FPGA_REVISION
    BADC_SERIES_FPGA_REVISION = _cconsts.NX_ERR_BADC_SERIES_FPGA_REVISION
    # The firmware version of your XNET C Series module is not in sync with the
    # NI-XNET software on your remote target. Solution: Update the NI-XNET
    # software on the remote target.
    BAD_FPGA_REVISION_ON_TARGET = _cconsts.NX_ERR_BAD_FPGA_REVISION_ON_TARGET
    # The terminal you are trying to use is already in use. Only one connection
    # per terminal is allowed. Solution: disconnect the terminal that is already
    # in use.
    ROUTE_IN_USE = _cconsts.NX_ERR_ROUTE_IN_USE
    # You need to install a supported version of NI-DAQmx for your XNET C Series
    # module to work correctly with your Compact DAQ system. Solution: Check the
    # NI-XNET readme file for supported versions of the NI-DAQmx driver software.
    DA_QMX_INCORRECT_VERSION = _cconsts.NX_ERR_DA_QMX_INCORRECT_VERSION
    # Unable to create the requested route. This may be caused by a routing
    # conflict or an invalid terminal name. Solution: Fix invalid terminal names,
    # such as a blank string. Since NI-XNET relies on the NI-DAQmx driver software
    # to create routes on Compact DAQ chassis, use DAQmx to resolve routing
    # conflicts.
    ADD_ROUTE = _cconsts.NX_ERR_ADD_ROUTE
    # You attempted to transmit a go to sleep frame (by setting the LIN Sleep mode
    # to Remote Sleep) on a LIN interface configured as slave. In conformance with
    # the LIN protocol standard, only an interface configured as master may
    # transmit a go to sleep frame.
    REMOTE_SLEEP_ON_LIN_SLAVE = _cconsts.NX_ERR_REMOTE_SLEEP_ON_LIN_SLAVE
    # You attempted to set properties related to Sleep and Wakeup when the FlexRay
    # cluster defined in the Fibex file does not support it. Solution: Edit the
    # Fibex file used in your application to include all relevant cluster wakeup
    # attributes.
    SLEEP_WAKEUP_NOT_SUPPORTED = _cconsts.NX_ERR_SLEEP_WAKEUP_NOT_SUPPORTED
    # The data payload written for a diagnostic frame for transmit does not
    # conform to the LIN transport layer specification. Solution: Ensure the data
    # payload for a diagnostic frame conforms to the transport layer
    # specification.
    LIN_TRANSPORT_LAYER = _cconsts.NX_ERR_LIN_TRANSPORT_LAYER
    # An error occurred within the NI-XNET example code for logfile access (TDMS).
    # Solution: For LabVIEW, the subVI with the error is shown as the source, and
    # you can open that subVI to determine the cause of the problem. For other
    # programming languages, review the source code for the logfile example to
    # determine the cause of the problem.
    LOGFILE = _cconsts.NX_ERR_LOGFILE
    # You attempted to write a LIN schedule and use a stream output replay timing
    # mode concurrently. You can only use the stream output immediate timing mode
    # cuncurrently with the LIN scheduler.
    STRM_OUT_TMG_LIN_SCHEDULER_CONFLICT = _cconsts.NX_ERR_STRM_OUT_TMG_LIN_SCHEDULER_CONFLICT
    # You attempted to create a session that is incompatible with the LIN
    # interface personality (master or slave), or set the LIN interface
    # personality to one that is incompatible with a session already created for
    # it. For example, setting the LIN interface to slave after creating a stream
    # output session will report this error, because only LIN interface as master
    # supports stream output.
    SESSN_TYPE_LIN_INTF_PRS_INCOMPATIBLE = _cconsts.NX_ERR_SESSN_TYPE_LIN_INTF_PRS_INCOMPATIBLE
    # You attempted to save an LDF or DBC database, but the passed reference is
    # not a database cluster. Solution: A cluster reference must be used to
    # specify the cluster you want to export.
    SAVE_CLUSTER_ONLY = _cconsts.NX_ERR_SAVE_CLUSTER_ONLY
    # Need to define for compatibility with older versions
    SAVE_LDF_CLUSTER_ONLY = _cconsts.NX_ERR_SAVE_LDF_CLUSTER_ONLY
    # You tried to assign the same interface name twice. This is not permitted.
    # Solution: Assign a unique name to an interface.
    DUPLICATE_INTERFACE_NAME = _cconsts.NX_ERR_DUPLICATE_INTERFACE_NAME
    # Transceiver cable hardware revision is too new. The current driver does not
    # support this transceiver cable. Solution: Upgrade the NI-XNET driver.
    INCOMPATIABLE_TRANSCEIVER_REVISION = _cconsts.NX_ERR_INCOMPATIABLE_TRANSCEIVER_REVISION
    # Transceiver cable image revision is too new. The current driver does not
    # support this transceiver cable. Solution: Upgrade the NI-XNET driver or
    # downgrade the image on the transceiver cable.
    INCOMPATIABLE_TRANSCEIVER_IMAGE = _cconsts.NX_ERR_INCOMPATIABLE_TRANSCEIVER_IMAGE
    # The property does not apply to this type of hardware. Solution: Do not apply
    # the property to this type of hardware.
    PROPERTY_NOTSUPPORTED = _cconsts.NX_ERR_PROPERTY_NOTSUPPORTED
    # Exporting cluster into the specified database type failed. Solution: Ensure
    # the database configuration is complete. Refer to the standard documentation
    # for the related file format.
    SEMANTIC = _cconsts.NX_ERR_EXPORT_SEMANTIC
    # A J1939 input queue overflowed. Reading large J1939 frames can make the
    # queue overflow, and the Read function delivers fewer frames then specified.
    # Solution: Call the Read function again to read the remaining frames.
    J1939_QUEUE_OVERFLOW = _cconsts.NX_ERR_J1939_QUEUE_OVERFLOW
    # You are trying to transmit a non-J1939 frame with more than 8 bytes. Only
    # J1939 frames can use the J1939 transport protocol. Solution: Verify the
    # transport protocol property on the frame in the database.
    NON_J1939_FRAME_SIZE = _cconsts.NX_ERR_NON_J1939_FRAME_SIZE
    # You are trying to transmit a J1939 frame, but no J1939 address is assigned
    # to the session. Solution: Set the address using the J1939 address property.
    J1939_MISSING_ADDRESS = _cconsts.NX_ERR_J1939_MISSING_ADDRESS
    # The received J1939 TP.CM_CTS message has the wrong total size.
    J1939_ADDRESS_LOST = _cconsts.NX_ERR_J1939_ADDRESS_LOST
    # The next packet value of the received J1939 TP.CM_CTS message is larger than
    # the total number of packets.
    J1939_CTS_NEXT_PCK_LARGER_TOTAL_PCK_NUM = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK_LARGER_TOTAL_PCK_NUM
    # The received J1939 TP.CM_CTS message has a number of packets of 0, but the
    # next packet number is not 255.
    J1939_CTS_NEXT_PCK = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK
    # The received J1939 TP.CM_CTS message has not does not have the same PGN as
    # in the TP.CM_RTS message.
    J1939_CTS_NEXT_PCK_NULL = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK_NULL
    # The received J1939 TP.CM_CTS message does not have the same PGN as in the
    # TP.CM_RTS message.
    J1939_CTS_PGN = _cconsts.NX_ERR_J1939_CTS_PGN
    # Received unexpected sequence number in the J1939 TP.DT message.
    J1939_UNEXPECTED_SEQ_NUM = _cconsts.NX_ERR_J1939_UNEXPECTED_SEQ_NUM
    # More Packets are requested than allowed in the J1939 TP.CM_CTS message.
    J1939_MORE_PCK_REQ_THAN_ALLOWED = _cconsts.NX_ERR_J1939_MORE_PCK_REQ_THAN_ALLOWED
    # J1939 Timeout T1 while waiting for data.
    J1939_TIMEOUT_T1 = _cconsts.NX_ERR_J1939_TIMEOUT_T1
    # J1939 Timeout T2 while waiting for data.
    J1939_TIMEOUT_T2 = _cconsts.NX_ERR_J1939_TIMEOUT_T2
    # J1939 Timeout T3 while waiting for TP.CM_CTS or TP.CM_EndOfMsgAck.
    J1939_TIMEOUT_T3 = _cconsts.NX_ERR_J1939_TIMEOUT_T3
    # J1939 Timeout T4 while waiting for next CTS MSG.
    J1939_TIMEOUT_T4 = _cconsts.NX_ERR_J1939_TIMEOUT_T4
    # Received wrong DLC in the J1939 TP.CM_RTS message. DLC must be 8.
    J1939_RTS_DLC = _cconsts.NX_ERR_J1939_RTS_DLC
    # Received wrong DLC in the J1939 TP.CM_CTS message. DLC must be 8.
    J1939_CTS_DLC = _cconsts.NX_ERR_J1939_CTS_DLC
    # Received wrong DLC in the J1939 TP.CM_BAM message. DLC must be 8.
    J1939_BAM_DLC = _cconsts.NX_ERR_J1939_BAM_DLC
    # Received wrong DLC in the J1939 TP.DT message. DLC must be 8.
    J1939_DT_DLC = _cconsts.NX_ERR_J1939_DT_DLC
    # Received wrong DLC in the J1939 TP.CM_Abort message. DLC must be 8.
    J1939_ABORT_DLC = _cconsts.NX_ERR_J1939_ABORT_DLC
    # Received wrong DLC in the J1939 TP.CM_EndOfMsgAck message. DLC must be 8.
    J1939_EOMA_DLC = _cconsts.NX_ERR_J1939_EOMA_DLC
    # Received wrong PGN in the J1939 TP.CM_Abort message.
    J1939_ABORT_PGN = _cconsts.NX_ERR_J1939_ABORT_PGN
    # Internal error occurred for send TP.CM_CTS Hold Message.
    J1939_CTS_HOLD_MSG = _cconsts.NX_ERR_J1939_CTS_HOLD_MSG
    # Invalid total message size in J1939 TP.CM_RTS message. Expect 9..1785.
    J1939_INVALID_TOTAL_SIZE = _cconsts.NX_ERR_J1939_INVALID_TOTAL_SIZE
    # Total number of packets in received J1939 TP.CM_RTS message must be greater
    # than 1.
    J1939_TOTAL_PCK_NUM = _cconsts.NX_ERR_J1939_TOTAL_PCK_NUM
    # Reserved data bytes in J1939 received message are not BFF63FF.
    J1939_RESERVED_DATA = _cconsts.NX_ERR_J1939_RESERVED_DATA
    # Not enough system resources for the J1939 Transport Protocol.
    J1939_NOT_ENOUGH_SYS_RES = _cconsts.NX_ERR_J1939_NOT_ENOUGH_SYS_RES
    # Received J1939 TP.CM_Abort message with reason ActiveConnection: Already in
    # one or more connection managed sessions and cannot support another.
    J1939_ABORT_MSG_ACTIVE_CONNECTION = _cconsts.NX_ERR_J1939_ABORT_MSG_ACTIVE_CONNECTION
    # Received J1939 TP.CM_Abort message with reason NotEnoughSystemResources:
    # System resources were needed for another task, so this connection managed
    # session was terminated.
    J1939_ABORT_MSG_NOT_ENOUGH_SYS_RES = _cconsts.NX_ERR_J1939_ABORT_MSG_NOT_ENOUGH_SYS_RES
    # Received J1939 TP.CM_Abort message with reason Timeout: A timeout occurred,
    # and this is the connection abort to close the session.
    J1939_ABORT_MSG_TIMEOUT = _cconsts.NX_ERR_J1939_ABORT_MSG_TIMEOUT
    # Received J1939 TP.CM_Abort message with reason CtsReceived: CTS messages
    # received when data transfer is in progress.
    J1939_ABORT_MSG_CTS_REC = _cconsts.NX_ERR_J1939_ABORT_MSG_CTS_REC
    # Received J1939 TP.CM_Abort message with reason MaxRetransmit: Maximum
    # retransmit request limit reached.
    J1939_ABORT_MSG_MAX_RETRANSMIT = _cconsts.NX_ERR_J1939_ABORT_MSG_MAX_RETRANSMIT
    # Remote communication with the LabVIEW RT target failed because the host and
    # target versions of NI-XNET are different. Solution: On the target, install
    # the same NI-XNET version that is installed on the host.
    RPC_VERSION = _cconsts.NX_ERR_RPC_VERSION
    # The CAN frame I/O mode is higher than the CAN cluster I/O mode. This frame
    # cannot be transmitted on the network. Solution: Change the frame or cluster
    # I/O mode.
    FRAME_CAN_IO_MODE = _cconsts.NX_ERR_FRAME_CAN_IO_MODE
    # The current driver cannot update the firmware on your hardware. Solution:
    # Ask National Instruments for compatible driver software.
    INCOMPATIBLE_FLASH = _cconsts.NX_ERR_INCOMPATIBLE_FLASH
    # You are trying to use the CAN Transmit I/O Mode (TxIoMode) property in an
    # unsupported interface mode. Solution: You can use this property in only
    # non-ISO or ISO Legacy mode.
    TX_IO_MODE = _cconsts.NX_ERR_TX_IO_MODE
    # You are trying to use the XS Transceiver Cable on unsupported hardware. This
    # currently requires a PXIe-8510 board.
    XS_DONGLE_UNSUPPORTED_BOARD = _cconsts.NX_ERR_XS_DONGLE_UNSUPPORTED_BOARD
    # You are trying to use a database alias name that contains an invalid
    # character (for example, a comma).
    INVALID_CHAR_IN_DATABASE_ALIAS = _cconsts.NX_ERR_INVALID_CHAR_IN_DATABASE_ALIAS
    # You are trying to use a database filepath that contains an invalid character
    # (for example, a comma).
    INVALID_CHAR_IN_DATABASE_FILEPATH = _cconsts.NX_ERR_INVALID_CHAR_IN_DATABASE_FILEPATH
    # You are trying to use CAN FD with a non-HS/FD port. CAN FD is supported with
    # High Speed CAN only.
    INVALID_CAN_FD_PORT_TYPE = _cconsts.NX_ERR_INVALID_CAN_FD_PORT_TYPE
    # An unconditional LIN schedule entry is wrongly configured.
    # Solution: Reference exactly one frame in the entry.
    INV_UNCONDITIONAL_ENTRY = _cconsts.NX_ERR_INV_UNCONDITIONAL_ENTRY
    # An event LIN schedule entry has no collision resolving schedule assigned.
    # Solution: Assign a schedule to the schedule entry.
    EVENT_ENTRY_NO_SCHEDULE = _cconsts.NX_ERR_EVENT_ENTRY_NO_SCHEDULE
    # You have connected your USB device to a port that only supports Full Speed
    # (USB 1.1). NI-XNET USB devices require at least High Speed (USB 2.0+)
    # support for correct operation.
    UNSUPPORTED_USB_SPEED = _cconsts.NX_ERR_UNSUPPORTED_USB_SPEED


class Warn(enum.Enum):
    """Warning codes returned by NI-XNET."""
    # The CAN FD baud rate you supplied exceeds the capabilities the transceiver
    # manufacturer specified. In our internal testing, we have found this baud
    # rate to run, but bus errors may be detected or generated during
    # communication. Refer to the NI-XNET CAN Hardware Overview section in the
    # NI-XNET Hardware and Software Manual for more information.
    FD_BAUD_EXCEEDS_CAPABILITY = _cconsts.NX_WARN_FD_BAUD_EXCEEDS_CAPABILITY
    # There is a warning from importing the database file. For details, refer to
    # the import log file nixnetfx-log.txt or nixnetldf-log.txt under
    # %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log. On Windows XP, the files
    # can be found under %USERPROFILE%\\Local Settings\\Application Data\\National
    # Instruments\\NI-XNET\\log. Please note that this location may be hidden on
    # your computer.
    DATABASE_IMPORT = _cconsts.NX_WARN_DATABASE_IMPORT
    # The database file has been imported, but it was not created by the XNET
    # Editor or using the XNET API. Saving the database file with the XNET API or
    # XNET Editor may lose information from the original file.
    DATABASE_IMPORT_FIBEX_NO_XNET_FILE = _cconsts.NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE
    # The database file was not created by the XNET Editor or using the XNET API.
    # Additionally, there is another warning. For details, refer to the import log
    # file nixnetfx-log.txt under %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log.
    # On Windows XP, the file can be found under %USERPROFILE%\\Local
    # Settings\\Application Data\\National Instruments\\NI-XNET\\log. Please note that
    # this location may be hidden on your computer.
    DATABASE_IMPORT_FIBEX_NO_XNET_FILE_PLUS_WARNING = _cconsts.NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE_PLUS_WARNING
    # Close Database returns a warning instead of an error when an invalid
    # reference is passed to the function.
    DATABASE_BAD_REFERENCE = _cconsts.NX_WARN_DATABASE_BAD_REFERENCE
    # Your are retrieving signals from a frame that uses advanced PDU
    # configuration. The signal start bit is given relative to the PDU, and it may
    # be different than the start bit relative to the frame.
    ADVANCED_PDU = _cconsts.NX_WARN_ADVANCED_PDU
    # The multiplexer size exceeds 16 bit. This is not supported for Single Point
    # sessions.
    MUX_EXCEEDS16_BIT = _cconsts.NX_WARN_MUX_EXCEEDS16_BIT


class ObjectClass(enum.Enum):
    DATABASE = _cconsts.NX_CLASS_DATABASE
    CLUSTER = _cconsts.NX_CLASS_CLUSTER
    FRAME = _cconsts.NX_CLASS_FRAME
    SIGNAL = _cconsts.NX_CLASS_SIGNAL
    SUBFRAME = _cconsts.NX_CLASS_SUBFRAME
    ECU = _cconsts.NX_CLASS_ECU
    LIN_SCHED = _cconsts.NX_CLASS_LIN_SCHED
    LIN_SCHED_ENTRY = _cconsts.NX_CLASS_LIN_SCHED_ENTRY
    PDU = _cconsts.NX_CLASS_PDU
    SESSION = _cconsts.NX_CLASS_SESSION
    SYSTEM = _cconsts.NX_CLASS_SYSTEM
    DEVICE = _cconsts.NX_CLASS_DEVICE
    INTERFACE = _cconsts.NX_CLASS_INTERFACE
    ALIAS = _cconsts.NX_CLASS_ALIAS


class CreateSessionMode(enum.Enum):
    """Create Session Mode.

    The session mode specifies the data type (signals or frames), direction
    (input or output), and how data is transferred between your application and
    the network.

    Values:
        SIGNAL_IN_SINGLE_POINT:
            Reads the most recent value received for each signal. This mode
            typically is used for control or simulation applications, such as
            Hardware In the Loop (HIL).
        SIGNAL_IN_WAVEFORM:
            Using the time when the signal frame is received, resamples the
            signal data to a waveform with a fixed sample rate. This mode
            typically is used for synchronizing XNET data with DAQmx
            analog/digital input channels.
        SIGNAL_IN_XY:
            For each frame received, provides its signals as a value/timestamp
            pair. This is the recommended mode for reading a sequence of all
            signal values.
        SIGNAL_OUT_SINGLE_POINT:
            Writes signal values for the next frame transmit. This mode
            typically is used for control or simulation applications, such as
            Hardware In the Loop (HIL).
        SIGNAL_OUT_WAVEFORM:
            Using the time when the signal frame is transmitted according to the
            database, resamples the signal data from a waveform with a fixed
            sample rate. This mode typically is used for synchronizing XNET data
            with DAQmx analog/digital output channels.
        SIGNAL_OUT_XY:
            Provides a sequence of signal values for transmit using each frame's
            timing as the database specifies. This is the recommended mode for
            writing a sequence of all signal values.
        FRAME_IN_STREAM:
            Reads all frames received from the network using a single stream.
            This mode typically is used for analyzing and/or logging all frame
            traffic in the network.
        FRAME_IN_QUEUED:
            Reads data from a dedicated queue per frame. This mode enables your
            application to read a sequence of data specific to a frame (for
            example, CAN identifier).
        FRAME_IN_SINGLE_POINT:
            Reads the most recent value received for each frame. This mode
            typically is used for control or simulation applications that
            require lower level access to frames (not signals).
        FRAME_OUT_STREAM:
            Transmits an arbitrary sequence of frame values using a single
            stream. The values are not limited to a single frame in the
            database, but can transmit any frame.
        FRAME_OUT_QUEUED:
            Provides a sequence of values for a single frame, for transmit using
            that frame's timing as the database specifies.
        FRAME_OUT_SINGLE_POINT:
            Writes frame values for the next transmit. This mode typically is
            used for control or simulation applications that require lower level
            access to frames (not signals).
        SIGNAL_CONVERSION_SINGLE_POINT:
            This mode does not use any hardware. It is used to convert data
            between the signal representation and frame representation.
    """
    SIGNAL_IN_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_IN_SINGLE_POINT
    SIGNAL_IN_WAVEFORM = _cconsts.NX_MODE_SIGNAL_IN_WAVEFORM
    SIGNAL_IN_XY = _cconsts.NX_MODE_SIGNAL_IN_XY
    SIGNAL_OUT_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_OUT_SINGLE_POINT
    SIGNAL_OUT_WAVEFORM = _cconsts.NX_MODE_SIGNAL_OUT_WAVEFORM
    SIGNAL_OUT_XY = _cconsts.NX_MODE_SIGNAL_OUT_XY
    FRAME_IN_STREAM = _cconsts.NX_MODE_FRAME_IN_STREAM
    FRAME_IN_QUEUED = _cconsts.NX_MODE_FRAME_IN_QUEUED
    FRAME_IN_SINGLE_POINT = _cconsts.NX_MODE_FRAME_IN_SINGLE_POINT
    FRAME_OUT_STREAM = _cconsts.NX_MODE_FRAME_OUT_STREAM
    FRAME_OUT_QUEUED = _cconsts.NX_MODE_FRAME_OUT_QUEUED
    FRAME_OUT_SINGLE_POINT = _cconsts.NX_MODE_FRAME_OUT_SINGLE_POINT
    SIGNAL_CONVERSION_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_CONVERSION_SINGLE_POINT


class StartStopScope(enum.Enum):
    """Start/Stop Scope enum.

    Values:
        NORMAL:
            The session is started followed by starting the interface. This is
            equivalent to calling :any:`nixnet._session.base.SessionBase.start`
            with the Session Only Scope followed by calling
            :any:`nixnet._session.base.SessionBase.start` with the Interface Only Scope.
        SESSION_ONLY:
            The session is placed into the Started state (refer to State Models).
            If the interface is in the Stopped state before this function runs,
            the interface remains in the Stopped state, and no communication
            occurs with the bus. To have multiple sessions start at exactly the
            same time, start each session with the Session Only Scope. When you
            are ready for all sessions to start communicating on the associated
            interface, call :any:`nixnet._session.base.SessionBase.start` with
            the Interface Only scope. Starting a previously started session is
            considered a no-op. This operation sends the command to start the
            session, but does not wait for the session to be started. It is
            ideal for a real-time application where performance is critical.
        INTERFACE_ONLY:
            If the underlying interface is not previously started, the interface
            is placed into the Started state (refer to State Models). After the
            interface starts communicating, all previously started sessions can
            transfer data to and from the bus. Starting a previously started
            interface is considered a no-op.
        SESSION_ONLY_BLOCKING:
            The session is placed in the Started state (refer to State Models).
            If the interface is in the Stopped state before this function runs,
            the interface remains in the Stopped state, and no communication
            occurs with the bus. To have multiple sessions start at exactly the
            same time, start each session with the Session Only Scope. When you
            are ready for all sessions to start communicating on the associated
            interface, call nxStart with the Interface Only Scope. Starting a
            previously started session is considered a no-op. This operation
            waits for the session to start before completing.
    """
    NORMAL = _cconsts.NX_START_STOP_NORMAL
    SESSION_ONLY = _cconsts.NX_START_STOP_SESSION_ONLY
    INTERFACE_ONLY = _cconsts.NX_START_STOP_INTERFACE_ONLY
    SESSION_ONLY_BLOCKING = _cconsts.NX_START_STOP_SESSION_ONLY_BLOCKING


class BlinkMode(enum.Enum):
    '''Interface blink mode.

    Values:
        DISABLE:
            Disable blinking for identification.  This option turns off both
            LEDs for the port.
        ENABLE:
            Enable blinking for identification.  Both LEDs of the interface's
            physical port turn on and off.  The hardware blinks the LEDs
            automatically until you disable.
    '''
    DISABLE = _cconsts.NX_BLINK_DISABLE
    ENABLE = _cconsts.NX_BLINK_ENABLE


class ReadState(enum.Enum):
    TIME_CURRENT = _cconsts.NX_STATE_TIME_CURRENT
    TIME_COMMUNICATING = _cconsts.NX_STATE_TIME_COMMUNICATING
    TIME_START = _cconsts.NX_STATE_TIME_START
    SESSION_INFO = _cconsts.NX_STATE_SESSION_INFO
    CAN_COMM = _cconsts.NX_STATE_CAN_COMM
    FLEX_RAY_COMM = _cconsts.NX_STATE_FLEX_RAY_COMM
    FLEX_RAY_STATS = _cconsts.NX_STATE_FLEX_RAY_STATS
    LIN_COMM = _cconsts.NX_STATE_LIN_COMM
    J1939_COMM = _cconsts.NX_STATE_J1939_COMM


class WriteState(enum.Enum):
    LIN_SCHEDULE_CHANGE = _cconsts.NX_STATE_LIN_SCHEDULE_CHANGE
    LIN_DIAGNOSTIC_SCHEDULE_CHANGE = _cconsts.NX_STATE_LIN_DIAGNOSTIC_SCHEDULE_CHANGE
    FLEX_RAY_SYMBOL = _cconsts.NX_STATE_FLEX_RAY_SYMBOL


class CanFdIsoMode(enum.Enum):
    """CAN FD ISO MODE.

    Values:
        ISO:
            ISO CAN FD standard (ISO standard 11898-1:2015)

            In ISO CAN FD mode, for every transmitted frame, you can specify in
            the database or frame header whether a frame must be sent in CAN
            2.0, CAN FD, or CAN FD+BRS mode. In the frame type field of the
            frame header, received frames indicate whether they have been sent
            with CAN 2.0, CAN FD, or CAN FD+BRS. You cannot use the
            Interface:CAN:Transmit I/O Mode property in ISO CAN FD mode, as the
            frame defines the transmit mode.
        NON_ISO:
            non-ISO CAN FD standard (Bosch CAN FD 1.0 specification)

            In Non-ISO CAN FD mode, CAN data frames are received at CAN
            data typed frames, which is either CAN 2.0, CAN FD, or CAN FD+BRS,
            but you cannot distinguish the standard in which the frame has been
            transmitted.
        ISO_LEGACY:
            You also can set the mode to Legacy ISO mode. In this mode,
            the behavior is the same as in Non-ISO CAN FD mode
            (Interface:CAN:Transmit I/O Mode is working, and received frames
            have the CAN data type). But the interface is working in ISO CAN FD
            mode, so you can communicate with other ISO CAN FD devices. Use this
            mode only for compatibility with existing applications.
    """
    ISO = _cconsts.NX_CAN_FD_MODE_ISO
    NON_ISO = _cconsts.NX_CAN_FD_MODE_NON_ISO
    ISO_LEGACY = _cconsts.NX_CAN_FD_MODE_ISO_LEGACY


class SessionInfoState(enum.Enum):
    """State of running session.

    Values:
        STOPPED:
            All frames in the session are stopped.
        STARTED:
            All frames in the session are started.
        MIX:
            Some frames in the session are started while other frames are
            stopped. This state may occur when using ``start`` or ``stop`` with
            ``StartStopScope.SESSION_ONLY``.
    """
    STOPPED = _cconsts.NX_SESSION_INFO_STATE_STOPPED
    STARTED = _cconsts.NX_SESSION_INFO_STATE_STARTED
    MIX = _cconsts.NX_SESSION_INFO_STATE_MIX


class CanCommState(enum.Enum):
    """CAN Comm State.

    Values:
        ERROR_ACTIVE:
            This state reflects normal communication, with few errors detected.
            The CAN interface remains in this state as long as receive error
            counter and transmit error counter are both below 128.
        ERROR_PASSIVE:
            If either the receive error counter or transmit error counter
            increment above 127, the CAN interface transitions into this state.
            Although communication proceeds, the CAN device generally is assumed
            to have problems with receiving frames.

            When a CAN interface is in error passive state, acknowledgement
            errors do not increment the transmit error counter. Therefore, if
            the CAN interface transmits a frame with no other device (ECU)
            connected, it eventually enters error passive state due to
            retransmissions, but does not enter bus off state.
        BUS_OFF:
            If the transmit error counter increments above 255, the CAN
            interface transitions into this state. Communication immediately
            stops under the assumption that the CAN interface must be isolated
            from other devices.

            When a CAN interface transitions to the bus off state, communication
            stops for the interface. All NI-XNET sessions for the interface no
            longer receive or transmit frame values. To restart the CAN
            interface and all its sessions, call
            :any:`nixnet._session.base.SessionBase.start`.
        INIT:
            This is the CAN interface initial state on power-up. The interface
            is essentially off, in that it is not attempting to communicate with
            other nodes (ECUs).

            When the start trigger occurs for the CAN interface, it transitions
            from the Init state to the Error Active state. When the interface
            stops due to a call to :any:`nixnet._session.base.SessionBase.stop`.,
            the CAN interface transitions from either Error Active or Error Passive
            to the Init state. When the interface stops due to the Bus Off state,
            it remains in that state until you restart.
    """
    ERROR_ACTIVE = _cconsts.NX_CAN_COMM_STATE_ERROR_ACTIVE
    ERROR_PASSIVE = _cconsts.NX_CAN_COMM_STATE_ERROR_PASSIVE
    BUS_OFF = _cconsts.NX_CAN_COMM_STATE_BUS_OFF
    INIT = _cconsts.NX_CAN_COMM_STATE_INIT


class CanLastErr(enum.Enum):
    """CAN Last Error

    Values:
        NONE:
            The last receive or transmit was successful.
        STUFF:
            More than 5 equal bits have occurred in sequence, which the CAN
            specification does not allow.
        FORM:
            A fixed format part of the received frame used the wrong format.
        ACK:
            Another node (ECU) did not acknowledge the frame transmit.

            If you call the appropriate ``write`` function and do not have a
            cable connected, or the cable is connected to a node that is not
            communicating, you see this error repeatedly. The CAN communication
            state eventually transitions to Error Passive, and the frame
            transmit retries indefinitely.
        BIT1:
            During a frame transmit (with the exception of the arbitration ID
            field), the interface wanted to send a recessive bit (logical 1),
            but the monitored bus value was dominant (logical 0).
        BIT0:
            During a frame transmit (with the exception of the arbitration ID
            field), the interface wanted to send a dominant bit (logical 0),
            but the monitored bus value was recessive (logical 1).
        CRC:
            The CRC contained within a received frame does not match the CRC
            calculated for the incoming bits.
    """
    NONE = _cconsts.NX_CAN_LAST_ERR_NONE
    STUFF = _cconsts.NX_CAN_LAST_ERR_STUFF
    FORM = _cconsts.NX_CAN_LAST_ERR_FORM
    ACK = _cconsts.NX_CAN_LAST_ERR_ACK
    BIT1 = _cconsts.NX_CAN_LAST_ERR_BIT1
    BIT0 = _cconsts.NX_CAN_LAST_ERR_BIT0
    CRC = _cconsts.NX_CAN_LAST_ERR_CRC


class CanIoMode(enum.Enum):
    """CAN I/O Mode.

    Values:
        CAN:
            This is the default CAN 2.0 A/B standard I/O mode as defined in ISO 11898-1:2003.
            A fixed baud rate is used for transfer,
            and the payload length is limited to 8 bytes.
        CAN_FD:
            This is the CAN FD mode as specified in the CAN with *Flexible Data-Rate specification*,
            version 1.0. Payload lengths up to 64 are allowed,
            but they are transmitted at a single fixed baud rate
            (defined by :any:`Cluster.can_fd_baud_rate` or :any:`Interface.can_fd_baud_rate`).
        CAN_FD_BRS:
            This is the CAN FD as specified in the *CAN with Flexible Data-Rate* specification,
            version 1.0, with the optional Baud Rate Switching enabled.
            The same payload lengths as CAN FD mode are allowed; additionally,
            the data portion of the CAN frame is transferred at a different (higher) baud rate
            (defined by :any:`Cluster.can_fd_baud_rate` or :any:`Interface.can_fd_baud_rate`).
    """
    CAN = _cconsts.NX_CAN_IO_MODE_CAN
    CAN_FD = _cconsts.NX_CAN_IO_MODE_CAN_FD
    CAN_FD_BRS = _cconsts.NX_CAN_IO_MODE_CAN_FD_BRS


class FlexRayPocState(enum.Enum):
    DEFAULT_CONFIG = _cconsts.NX_FLEX_RAY_POC_STATE_DEFAULT_CONFIG
    READY = _cconsts.NX_FLEX_RAY_POC_STATE_READY
    NORMAL_ACTIVE = _cconsts.NX_FLEX_RAY_POC_STATE_NORMAL_ACTIVE
    NORMAL_PASSIVE = _cconsts.NX_FLEX_RAY_POC_STATE_NORMAL_PASSIVE
    HALT = _cconsts.NX_FLEX_RAY_POC_STATE_HALT
    MONITOR = _cconsts.NX_FLEX_RAY_POC_STATE_MONITOR
    CONFIG = _cconsts.NX_FLEX_RAY_POC_STATE_CONFIG


class LinCommState(enum.Enum):
    '''LIN Comm State

    Values:
        IDLE:
            This is the LIN interface initial state on power-up. The
            interface is essentially off, in that it is not attempting to
            communicate with other nodes (ECUs). When the start trigger
            occurs for the LIN interface, it transitions from the Idle
            state to the Active state. When the interface stops due to a
            call to XNET Stop, the LIN interface transitions from either
            Active or Inactive to the Idle state.
        ACTIVE:
            This state reflects normal communication. The LIN interface remains
            in this state as long as bus activity is detected (frame headers
            received or transmitted).
        INACTIVE:
            This state indicates that no bus activity has been detected in the
            past four seconds.

            Regardless of whether the interface acts as a master or slave, it
            transitions to this state after four seconds of bus inactivity. As
            soon as bus activity is detected (break or frame header), the
            interface transitions to the Active state.

            The LIN interface does not go to sleep automatically when it
            transitions to Inactive. To place the interface into sleep mode,
            set the XNET Session Interface:LIN:Sleep property when you detect
            the Inactive state.
    '''
    IDLE = _cconsts.NX_LIN_COMM_STATE_IDLE
    ACTIVE = _cconsts.NX_LIN_COMM_STATE_ACTIVE
    INACTIVE = _cconsts.NX_LIN_COMM_STATE_INACTIVE


class LinDiagnosticSchedule(enum.Enum):
    """LIN Diagnostic Schedule

    Values:
        NULL:
            The master does not execute any diagnostic schedule. No master
            request or slave response headers are transmitted on the LIN.
        MASTER_REQ:
            The master executes a diagnostic master request schedule
            (transmits a master request header onto the LIN) if it can.
            First, a master request schedule must be defined for the LIN
            cluster in the imported or in-memory database. Otherwise, error
            'nixnet._enums.Err.DIAGNOSTIC_SCHEDULE_NOT_DEFINED' is returned
            when attempting to set this value. Second, the master must have
            a frame output queued session created for the master request frame,
            and there must be one or more new master request frames pending in
            the queue. If no new frames are pending in the output queue, no
            master request header is transmitted. This allows the timing of
            master request header transmission to be controlled by the timing
            of master request frame writes to the output queue.

            If there are no normal schedules pending, the master is effectively
            in diagnostics-only mode, and master request headers are transmitted
            at a rate determined by the slot delay defined for the master request
            frame slot in the master request schedule or the
            `nixnet._session.intf.Interface.lin_diag_s_tmin` property time, whichever
            is greater, and the state of the master request frame output queue
            as described above.

            If there are normal schedules pending, the master is effectively in
            diagnostics-interleaved mode, and a master request header transmission
            is inserted between each complete execution of a run-once or
            run-continuous schedule, as long as the
            `nixnet._session.intf.Interface.lin_diag_s_tmin` property time has
            been met, and there are one or more new master request frames pending
            in the master request frame output queue.
        SLAVE_RESP:
            The master executes a diagnostic slave response schedule
            (transmits a slave response header onto the LIN) if it is able to.
            A slave response schedule must be defined for the LIN cluster in the
            imported or in-memory database. Otherwise, error
            'nixnet._enums.Err.DIAGNOSTIC_SCHEDULE_NOT_DEFINED' is returned when
            attempting to set this value.

            If there are no normal schedules pending, the master is effectively
            in diagnostics-only mode, and slave response headers are transmitted
            at the rate of the slot delay defined for the slave response frame
            slot in the slave response schedule. The addressed slave may or
            may not respond to each header, depending on its specified
            P2min and STmin timings.

            If there are normal schedules pending, the master is effectively in
            diagnostics-interleaved mode, and a slave response header transmission
            is inserted between each complete execution of a run-once or run-continuous
            schedule. Here again, the addressed slave may or may not respond to each
            header, depending on its specified P2min and STmin timings.
    """
    NULL = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_NULL
    MASTER_REQ = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_MASTER_REQ
    SLAVE_RESP = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_SLAVE_RESP


class LinLastErr(enum.Enum):
    '''LIN Comm Last Error Code

    Values:
        NONE:
            No bus error has occurred since the previous communication state read.
        UNKNOWN_ID:
            Received a frame identifier that is not valid.
        FORM:
            The form of a received frame is incorrect. For example, the
            database specifies 8 bytes of payload, but you receive only 4
            bytes.
        FRAMING:
            The byte framing is incorrect (for example, a missing stop bit).
        READBACK:
            The interface transmitted a byte, but the value read back from the
            transceiver was different. This often is caused by a cabling
            problem, such as noise.
        TIMEOUT:
            Receiving the frame took longer than the LIN-specified timeout.
        CRC:
            The received checksum was different than the expected checksum.
    '''
    NONE = _cconsts.NX_LIN_LAST_ERR_CODE_NONE
    UNKNOWN_ID = _cconsts.NX_LIN_LAST_ERR_CODE_UNKNOWN_ID
    FORM = _cconsts.NX_LIN_LAST_ERR_CODE_FORM
    FRAMING = _cconsts.NX_LIN_LAST_ERR_CODE_FRAMING
    READBACK = _cconsts.NX_LIN_LAST_ERR_CODE_READBACK
    TIMEOUT = _cconsts.NX_LIN_LAST_ERR_CODE_TIMEOUT
    CRC = _cconsts.NX_LIN_LAST_ERR_CODE_CRC


class LinProtocolVer(enum.Enum):
    """LIN Protocol Version

    Values:
        VER_1_2:
            Version 1.2
        VER_1_3:
            Version 1.3
        VER_2_0:
            Version 2.0
        VER_2_1:
            Version 2.1
        VER_2_2:
            Version 2.2
    """
    VER_1_2 = _cconsts.NX_LIN_PROTOCOL_VER_1_2
    VER_1_3 = _cconsts.NX_LIN_PROTOCOL_VER_1_3
    VER_2_0 = _cconsts.NX_LIN_PROTOCOL_VER_2_0
    VER_2_1 = _cconsts.NX_LIN_PROTOCOL_VER_2_1
    VER_2_2 = _cconsts.NX_LIN_PROTOCOL_VER_2_2


class Condition(enum.Enum):
    TRANSMIT_COMPLETE = _cconsts.NX_CONDITION_TRANSMIT_COMPLETE
    INTF_COMMUNICATING = _cconsts.NX_CONDITION_INTF_COMMUNICATING
    INTF_REMOTE_WAKEUP = _cconsts.NX_CONDITION_INTF_REMOTE_WAKEUP


class GetDbcAttributeMode(enum.Enum):
    ATTRIBUTE = _cconsts.NX_GET_DBC_MODE_ATTRIBUTE
    ENUMERATION_LIST = _cconsts.NX_GET_DBC_MODE_ENUMERATION_LIST
    ATTRIBUTE_LIST = _cconsts.NX_GET_DBC_MODE_ATTRIBUTE_LIST
    VALUE_TABLE_LIST = _cconsts.NX_GET_DBC_MODE_VALUE_TABLE_LIST


class Merge(enum.Enum):
    """Cluster Merge Behavior

    Values:
        COPY_USE_SOURCE:
            The target object with all dependent child objects
            is removed from the target cluster and replaced by the source objects.
        COPY_USE_TARGET:
            The source object is ignored (the target cluster object with child objects remains unchanged).
        MERGE_USE_SOURCE:
            This adds child objects from the source object to child objects from the destination object.
            If target object contains a child object with the same name,
            the child object from the source frame replaces it.
            The source object properties (for example, payload length of the frame) replace the target properties.
        MERGE_USE_TARGET:
            This adds child objects from the source object to child objects from the destination object.
            If the target object contains a child object with the same name, it remains unchanged.
            The target object properties remain unchanged (for example, payload length).
    """
    COPY_USE_SOURCE = _cconsts.NXDB_MERGE_COPY_USE_SOURCE
    COPY_USE_TARGET = _cconsts.NXDB_MERGE_COPY_USE_TARGET
    MERGE_USE_SOURCE = _cconsts.NXDB_MERGE_MERGE_USE_SOURCE
    MERGE_USE_TARGET = _cconsts.NXDB_MERGE_MERGE_USE_TARGET


class DongleState(enum.Enum):
    '''Dongle State.

    Values:
        NO_DONGLE_NO_EXT_POWER:
            No dongle, no external power.
        NO_DONGLE_EXT_POWER:
            No dongle, has external power.
        DONGLE_NO_EXT_POWER:
            Has dongle, no external power.
        READY:
            Ready.
        BUSY:
            Busy.
        COMM_ERROR:
            Comm Error.
        OVERCURRENT:
            Overcurrent.
    '''
    NO_DONGLE_NO_EXT_POWER = _cconsts.NX_DONGLE_STATE_NO_DONGLE_NO_EXT_POWER
    NO_DONGLE_EXT_POWER = _cconsts.NX_DONGLE_STATE_NO_DONGLE_EXT_POWER
    DONGLE_NO_EXT_POWER = _cconsts.NX_DONGLE_STATE_DONGLE_NO_EXT_POWER
    READY = _cconsts.NX_DONGLE_STATE_READY
    BUSY = _cconsts.NX_DONGLE_STATE_BUSY
    COMM_ERROR = _cconsts.NX_DONGLE_STATE_COMM_ERROR
    OVERCURRENT = _cconsts.NX_DONGLE_STATE_OVER_CURRENT


class DongleId(enum.Enum):
    '''Dongle ID

    Values:
        HSCAN:
            CAN High Speed
        XSCAN:
            CAN Software-Selectable
        LIN:
            LIN
        DONGLE_LESS:
            Dongle-Less Design
    '''
    LSCAN = _cconsts.NX_DONGLE_ID_LS_CAN
    HSCAN = _cconsts.NX_DONGLE_ID_HS_CAN
    SWCAN = _cconsts.NX_DONGLE_ID_SW_CAN
    XSCAN = _cconsts.NX_DONGLE_ID_XS_CAN
    LIN = _cconsts.NX_DONGLE_ID_LIN
    DONGLE_LESS = _cconsts.NX_DONGLE_ID_DONGLE_LESS
    UNKNOWN = _cconsts.NX_DONGLE_ID_UNKNOWN


class Phase(enum.Enum):
    '''Version Phase.

    Values:
        RELEASE
    '''
    DEVELOPMENT = _cconsts.NX_PHASE_DEVELOPMENT
    ALPHA = _cconsts.NX_PHASE_ALPHA
    BETA = _cconsts.NX_PHASE_BETA
    RELEASE = _cconsts.NX_PHASE_RELEASE


class DevForm(enum.Enum):
    '''Device physical form factor.

    Values:
        C_SERIES
        PCI
        PCIE
        PXI
        PXIE
        USB
    '''
    C_SERIES = _cconsts.NX_DEV_FORM_C_SERIES
    PCI = _cconsts.NX_DEV_FORM_PCI
    PCIE = _cconsts.NX_DEV_FORM_PCIE
    PXI = _cconsts.NX_DEV_FORM_PXI
    PXIE = _cconsts.NX_DEV_FORM_PXIE
    USB = _cconsts.NX_DEV_FORM_USB


class CanTermCap(enum.Enum):
    '''CAN Termination Capability.

    Values:
        NO
        YES
    '''
    NO = _cconsts.NX_CAN_TERM_CAP_NO
    YES = _cconsts.NX_CAN_TERM_CAP_YES


class CanTerm(enum.Enum):
    '''CAN Termination.

    Different CAN hardware has different termination requirements, and the OFF
    and ON values have different meanings.

    **High-Speed CAN**

    High-Speed CAN networks are typically terminated on the bus itself instead
    of within a node. However, NI-XNET allows you to configure termination
    within the node to simplify testing. If your bus already has the correct
    amount of termination, leave this property in the default state of Off.
    However, if you require termination, set this property to On.

    Values:
        OFF:
            Termination is disabled.
        On:
            Termination (120 Ohms) is enabled.

    **Low-Speed/Fault-Tolerant CAN**

    Every node on a Low-Speed CAN network requires termination for each CAN
    data line (CAN_H and CAN_L). This configuration allows the
    Low-Speed/Fault-Tolerant CAN port to provide fault detection and recovery.
    Refer to Termination for more information about low-speed termination. In
    general, if the existing network has an overall network termination of 125 Ohms
    or less, turn on termination to enable the 4.99 kOhms option. Otherwise, you
    should select the default 1.11 kOhms option.

    Values:
        OFF:
            Termination is set to 1.11 kOhms.
        ON:
            Termination is set to 4.99 kOhms.

    **Single-Wire CAN**

    The ISO standard requires Single-Wire transceivers to have a 9.09 kOhms
    resistor, and no additional configuration is supported.
    '''
    OFF = _cconsts.NX_CAN_TERM_OFF
    ON = _cconsts.NX_CAN_TERM_ON


class CanTcvrCap(enum.Enum):
    '''CAN bus phusical transceivers support.

    Values:
        HS:
            High-Speed / Flexible Data-Rate (HS/FD).
        LS:
            Low-Speed / Fault-Tolerant (LS//FT)
        XS:
            XS (HS//FD, LS/FT, SW, or External)
        XSHSLS:
            XS (HS//FD, LS/FT)
    '''
    HS = _cconsts.NX_CAN_TCVR_CAP_HS
    LS = _cconsts.NX_CAN_TCVR_CAP_LS
    XS = _cconsts.NX_CAN_TCVR_CAP_XS
    XSHSLS = _cconsts.NX_CAN_TCVR_CAP_XS_HS_LS
    UNKNOWN = _cconsts.NX_CAN_TCVR_CAP_UNKNOWN


class Protocol(enum.Enum):
    """Protocol.

    Values:
        UNKNOWN:
            Unknown protocol,
        CAN:
            CAN protocol.
        FLEX_RAY:
            FlexRay protocol.
        LIN:
            LIN protocol.
    """
    UNKNOWN = _cconsts.NX_PROTOCOL_UNKNOWN
    CAN = _cconsts.NX_PROTOCOL_CAN
    FLEX_RAY = _cconsts.NX_PROTOCOL_FLEX_RAY
    LIN = _cconsts.NX_PROTOCOL_LIN


class AppProtocol(enum.Enum):
    """Application Protocol.

    Values:
        NONE:
            The default application protocol.
        J1939:
            Indicates J1939 clusters. The value enables the following features:

            *   Sending/receiving long frames as the SAE J1939 specification specifies,
                using the J1939 transport protocol.
            *   Using a special notation for J1939 identifiers.
            *   Using J1939 address claiming.
    """
    NONE = _cconsts.NX_APP_PROTOCOL_NONE
    J1939 = _cconsts.NX_APP_PROTOCOL_J1939


class CanTcvrState(enum.Enum):
    '''CAN Transceiver State.

    Values:
        NORMAL:
            This state sets the transceiver to normal communication mode. If
            the transceiver is in the Sleep mode, this performs a local wakeup
            of the transceiver and CAN controller chip.
        SLEEP:
            This state sets the transceiver and CAN controller chip to Sleep
            (or standby) mode. You can set the interface to Sleep mode only
            while the interface is communicating. If the interface has not been
            started, setting the transceiver to Sleep mode returns an error.

            Before going to sleep, all pending transmissions are transmitted
            onto the CAN bus. Once all pending frames have been transmitted,
            the interface and transceiver go into Sleep (or standby) mode. Once
            the interface enters Sleep mode, further communication is not
            possible until a wakeup occurs.  The transceiver and CAN controller
            wake from Sleep mode when either a local wakeup or remote wakeup
            occurs.

            A local wakeup occurs when the application sets the transceiver
            state to either Normal or Single Wire Wakeup.

            A remote wakeup occurs when a remote node transmits a CAN frame
            (referred to as the wakeup frame). The wakeup frame wakes up the
            NI-XNET interface transceiver and CAN controller chip. The CAN
            controller chip does not receive or acknowledge the wakeup frame.
            After detecting the wakeup frame and idle bus, the CAN interface
            enters Normal mode.

            When the local or remote wakeup occurs, frame transmissions resume
            from the point at which the original Sleep mode was set.
        SW_WAKEUP:
            For a remote wakeup to occur for Single Wire transceivers, the node
            that transmits the wakeup frame first must place the network into
            the Single Wire Wakeup Transmission mode by asserting a higher
            voltage.

            This state sets a Single Wire transceiver into the Single Wire
            Wakeup Transmission mode, which forces the Single Wire transceiver
            to drive a higher voltage level on the network to wake up all
            sleeping nodes. Other than this higher voltage, this mode is
            similar to Normal mode. CAN frames can be received and transmitted
            normally.

            If you are not using a Single Wire transceiver, setting this state
            returns an error. If your current mode is Single Wire High-Speed,
            setting this mode returns an error because you are not allowed to
            wake up the bus in high-speed mode.

            The application controls the timing of how long the wakeup voltage
            is driven. The application typically changes to Single Wire Wakeup
            mode, transmits a single wakeup frame, and then returns to Normal
            mode.
        SW_HIGH_SPEED:
            This state sets a Single Wire transceiver into Single Wire
            High-Speed Communication mode. If you are not using a Single Wire
            transceiver, setting this state returns an error.

            Single Wire High-Speed Communication mode disables the
            transceiver's internal waveshaping function, allowing the SAE J2411
            High-Speed baud rate of 83.333 kbytes/s to be used. The
            disadvantage versus Single Wire Normal Communication mode, which
            allows only the SAE J2411 baud rate of 33.333 kbytes/s, is degraded
            EMC performance. Other than the disabled waveshaping, this mode is
            similar to Normal mode. CAN frames can be received and transmitted
            normally.

            This mode has no relationship to High-Speed transceivers. It is
            merely a higher speed mode of the Single Wire transceiver,
            typically used to download data when the onboard network is
            attached to an offboard tester ECU.

            The Single Wire transceiver does not support use of this mode in
            conjunction with Sleep mode. For example, a remote wakeup cannot
            transition from sleep to this Single Wire High-Speed mode.
            Therefore, setting the mode to Sleep from Single Wire High-Speed
            mode returns an error.
    '''
    NORMAL = _cconsts.NX_CAN_TCVR_STATE_NORMAL
    SLEEP = _cconsts.NX_CAN_TCVR_STATE_SLEEP
    SW_WAKEUP = _cconsts.NX_CAN_TCVR_STATE_SW_WAKEUP
    SW_HIGH_SPEED = _cconsts.NX_CAN_TCVR_STATE_SW_HIGH_SPEED


class CanTcvrType(enum.Enum):
    '''CAN Transceiver Type

    Values:
        High-Speed (HS):
            This configuration enables the High-Speed transceiver. This transceiver
            supports baud rates of 40 kbaud to 1 Mbaud. When using a High-Speed
            transceiver, you also can communicate with a CAN FD bus. Refer to NI-XNET
            Hardware Overview to determine which CAN FD baud rates are supported.
        Low-Speed/Fault-Tolerant (LS):
            This configuration enables the Low-Speed/Fault-Tolerant
            transceiver. This transceiver supports baud rates of 40-125 kbaud.
        Single Wire (SW):
            This configuration enables the Single Wire transceiver. This
            transceiver supports baud rates of 33.333 kbaud and 83.333 kbaud.
        External (EXT):
            This configuration allows you to use an external transceiver to
            connect to your CAN bus. Refer to the XNET Session
            Interface:CAN:External Transceiver Config property for more
            information.
        Disconnect (DISC):
            This configuration allows you to disconnect the CAN controller chip
            from the connector. You can use this value when you physically
            change the external transceiver.
    '''
    HS = _cconsts.NX_CAN_TCVR_TYPE_HS
    LS = _cconsts.NX_CAN_TCVR_TYPE_LS
    SW = _cconsts.NX_CAN_TCVR_TYPE_SW
    EXT = _cconsts.NX_CAN_TCVR_TYPE_EXT
    DISC = _cconsts.NX_CAN_TCVR_TYPE_DISC


class FlexRayTerm(enum.Enum):
    OFF = _cconsts.NX_FLEX_RAY_TERM_OFF
    ON = _cconsts.NX_FLEX_RAY_TERM_ON


class LinSleep(enum.Enum):
    '''LIN interface sleep/awake state

    Values:
        REMOTE_SLEEP:
            Set interface to sleep locally and transmit sleep requests to
            remote node.
        REMOTE_WAKE:
            Set interface to awake locally and transmit wakeup requests to
            remote nodes.
        LOCAL_SLEEP:
            Set interface to sleep locally and not to interact with the network.
        LOCAL_WAKE:
            Set interface to awake locally and not to interact with the network.
    '''
    REMOTE_SLEEP = _cconsts.NX_LIN_SLEEP_REMOTE_SLEEP
    REMOTE_WAKE = _cconsts.NX_LIN_SLEEP_REMOTE_WAKE
    LOCAL_SLEEP = _cconsts.NX_LIN_SLEEP_LOCAL_SLEEP
    LOCAL_WAKE = _cconsts.NX_LIN_SLEEP_LOCAL_WAKE


class LinTerm(enum.Enum):
    '''LIN Termination'''
    OFF = _cconsts.NX_LIN_TERM_OFF
    ON = _cconsts.NX_LIN_TERM_ON


class OutStrmTimng(enum.Enum):
    '''Output Stream Timing

    Values:
        IMMEDIATE:
            Frames are dequeued from the queue and transmitted immediately to
            the bus. The hardware transmits all frames in the queue as fast as
            possible. There are no restrictions on frames that you use in other
            sessions.

            For replay modes, the hardware is placed into a Replay mode. In
            this mode, the hardware evaluates the frame timestamps and attempts
            to maintain the original transmission times as the timestamp stored
            in the frame indicates.  The actual transmission time is based on
            the relative time difference between the first dequeued frame and
            the time contained in the dequeued frame.
        REPLAY_EXCLUSIVE:
            The hardware transmits only frames that do not appear in the list.
            You cannot create any other output sessions. Attempting to create
            an output session returns an error. Input sessions have no
            restrictions.

            This can be used to test an ECU when the output stream list
            contains the frames the ECU transmits.  You can replay all frames
            in this mode if the output stream list is unset.

        REPLAY_INCLUSIVE:
            The hardware transmits only frames that appear in the list.  You
            can create output sessions that use frames that do not appear in
            the Interface:Output Stream List property.  Attempting to create an
            output session that uses a frame from the Interface:Output Stream
            List property results in an error. Input sessions have no
            restrictions.

            This can be used to emulate an ECU when the output stream list
            contains the frames the ECU transmits.
    '''
    IMMEDIATE = _cconsts.NX_OUT_STRM_TIMNG_IMMEDIATE
    REPLAY_EXCLUSIVE = _cconsts.NX_OUT_STRM_TIMNG_REPLAY_EXCLUSIVE
    REPLAY_INCLUSIVE = _cconsts.NX_OUT_STRM_TIMNG_REPLAY_INCLUSIVE


class CanPendTxOrder(enum.Enum):
    '''Can Pending Transmit Order.

    Values:
        AS_SUBMITTED:
            Frames are transmitted in the order that they were submitted into
            the queue. There is no reordering of any frames, and a higher
            priority frame may be delayed due to the transmission or
            retransmission of a previously submitted frame. However, this mode
            has the highest performance.
        BY_IDENTIFIER:
            Frames with the highest priority identifier (lower CAN ID value)
            transmit first. The frames are stored in a priority queue sorted by
            ID. If a frame currently being transmitted requires retransmission
            (for example, it lost arbitration or failed with a bus error), and
            a higher priority frame is queued in the meantime, the lower
            priority frame is not immediately retried, but the higher priority
            frame is transmitted instead.  In this mode, you can emulate
            multiple ECUs and still see a behavior similar to a real bus in
            that the highest priority message is transmitted on the bus. This
            mode may be slower in performance (possible delays between
            transmissions as the queue is re-evaluated), and lower priority
            messages may be delayed indefinitely due to frequent high-priority
            messages.
    '''
    AS_SUBMITTED = _cconsts.NX_CAN_PEND_TX_ORDER_AS_SUBMITTED
    BY_IDENTIFIER = _cconsts.NX_CAN_PEND_TX_ORDER_BY_IDENTIFIER


class FlexRaySleep(enum.Enum):
    LOCAL_SLEEP = _cconsts.NX_FLEX_RAY_SLEEP_LOCAL_SLEEP
    LOCAL_WAKE = _cconsts.NX_FLEX_RAY_SLEEP_LOCAL_WAKE
    REMOTE_WAKE = _cconsts.NX_FLEX_RAY_SLEEP_REMOTE_WAKE


class FrmFlexRayChAssign(enum.Enum):
    A = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_A
    B = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_B
    AAND_B = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_AAND_B
    NONE = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_NONE


class ClstFlexRaySampClkPer(enum.Enum):
    P0125US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P0125US
    P025US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P025US
    P05US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P05US


class FrmFlexRayTiming(enum.Enum):
    CYCLIC = _cconsts.NX_FRM_FLEX_RAY_TIMING_CYCLIC
    EVENT = _cconsts.NX_FRM_FLEX_RAY_TIMING_EVENT


class FrmCanTiming(enum.Enum):
    """CAN Frame Timing

    Values:
        CYCLIC_DATA:
            The transmitting ECU transmits the CAN data frame in a cyclic (periodic) manner.
            The :any:`Frame.can_tx_time` property defines the time between cycles.
            The transmitting ECU ignores CAN remote frames received for this frame.
        EVENT_DATA:
            The transmitting ECU transmits the CAN data frame in an event-driven manner.
            The :any:`Frame.can_tx_time` property defines the minimum interval.
            For NI-XNET, the event occurs when you write data to a session.
            The transmitting ECU ignores CAN remote frames received for this frame.
        CYCLIC_REMOTE:
            The receiving ECU transmits the CAN remote frame in a cyclic (periodic) manner.
            The :any:`Frame.can_tx_time` property defines the time between cycles.
            The transmitting ECU responds to each CAN remote frame by transmitting the associated CAN data frame.
        EVENT_REMOTE:
            The receiving ECU transmits the CAN remote frame in an event-driven manner.
            The :any:`Frame.can_tx_time` property defines the minimum interval.
            For NI-XNET, the event occurs when you write a frame to a session.
            The transmitting ECU responds to each CAN remote frame by transmitting the associated CAN data frame.
        CYCLIC_EVENT:
            This timing type is a combination of the cyclic and event timing.
            The frame is transmitted when you write to a session,
            but also periodically sending the last recent values written.
            The :any:`Frame.can_tx_time` property defines the cycle period.
            There is no minimum interval time defined in this mode,
            so be careful not to write too frequently to avoid creating a high busload.
    """
    CYCLIC_DATA = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_DATA
    EVENT_DATA = _cconsts.NX_FRM_CAN_TIMING_EVENT_DATA
    CYCLIC_REMOTE = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_REMOTE
    EVENT_REMOTE = _cconsts.NX_FRM_CAN_TIMING_EVENT_REMOTE
    CYCLIC_EVENT = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_EVENT


class SigByteOrdr(enum.Enum):
    """Signal Byte Order

    Values:
        Little Endian:
            Higher significant signal bits are placed on higher byte addresses.
            In NI-CAN, this was called Intel Byte Order.

            .. image:: littleendianstartbit12.gif

            **Little Endian Signal with Start Bit 12**

        Big Endian:
            Higher significant signal bits are placed on lower byte addresses.
            In NI-CAN, this was called Motorola Byte Order.

            .. image:: bigendianstartbit12.gif

            **Big Endian Signal with Start Bit 12**
    """
    LITTLE_ENDIAN = _cconsts.NX_SIG_BYTE_ORDR_LITTLE_ENDIAN
    BIG_ENDIAN = _cconsts.NX_SIG_BYTE_ORDR_BIG_ENDIAN


class SigDataType(enum.Enum):
    """Signal Data Type

    Values:
        SIGNED:
            Signed integer with positive and negative values.
        UNSIGNED:
            Unsigned integer with no negative values.
        IEEE_FLOAT:
            Float value with 7 or 15 significant decimal digits (32 bit or 64 bit).
    """
    SIGNED = _cconsts.NX_SIG_DATA_TYPE_SIGNED
    UNSIGNED = _cconsts.NX_SIG_DATA_TYPE_UNSIGNED
    IEEE_FLOAT = _cconsts.NX_SIG_DATA_TYPE_IEEE_FLOAT


class LinSchedRunMode(enum.Enum):
    """LIN Schedule Run Mode.

    Values:
        CONTINUOUS:
            The master runs the schedule continuously.
            When the last entry executes,
            the schedule starts again with the first entry.
        ONCE:
            The master runs the schedule once (all entries),
            then returns to the previously running continuous schedule (or NULL).
            If requests are submitted for multiple run-once schedules,
            each run-once executes in succession based on its :any:`LinSched.priority`,
            then the master returns to the continuous schedule (or NULL).
        NULL:
            All communication stops immediately.
            A schedule with this run mode is called a *null schedule*.
    """
    CONTINUOUS = _cconsts.NX_LIN_SCHED_RUN_MODE_CONTINUOUS
    ONCE = _cconsts.NX_LIN_SCHED_RUN_MODE_ONCE
    NULL = _cconsts.NX_LIN_SCHED_RUN_MODE_NULL


class LinSchedEntryType(enum.Enum):
    """LIN Schedule Entry Type.

    Values:
        UNCONDITIONAL:
            A single frame transfers in this slot.
        SPORADIC:
            The master transmits in this slot.
            The master can select from multiple frames to transmit.
            Only updated frames are transmitted.
            When more than one frame is updated,
            the master decides by priority which frame to send.
            The other updated frame remains pending
            and can be sent when this schedule entry is processed the following time.
            The order of unconditional frames in :any:`LinSchedEntry.frames`
            (the first frame has the highest priority) determines the frame priority.
        EVENT_TRIGGERED:
            Multiple slaves can transmit an unconditional frame in this slot.
            The slave transmits the frame only if at least one frame signal has been updated.
            When a collision occurs (multiple slaves try to transmit in the same slot),
            this is detected and resolved using a different schedule
            specified in the :any:`LinSchedEntry.collision_res_sched` property.
            The resolving schedule runs once,
            starting in the subsequent slot after the collision,
            and automatically returns to the previous schedule
            at the subsequent position where the collision occurred.
        NODE_CONFIG_SERVICE:
            The schedule entry contains a node configuration service.
            The node configuration service is defined as raw data bytes
            in :any:`LinSchedEntry.nc_ff_data_bytes`.
    """
    UNCONDITIONAL = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_UNCONDITIONAL
    SPORADIC = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_SPORADIC
    EVENT_TRIGGERED = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_EVENT_TRIGGERED
    NODE_CONFIG_SERVICE = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_NODE_CONFIG_SERVICE


class FrmLinChecksum(enum.Enum):
    """LIN Frame Transmitted Checksum

    Values:
        CLASSIC:
            Classic checksum.
        ENHANCED:
            Enhanced checksum.
    """
    CLASSIC = _cconsts.NX_FRM_LIN_CHECKSUM_CLASSIC
    ENHANCED = _cconsts.NX_FRM_LIN_CHECKSUM_ENHANCED


class FrameType(enum.Enum):
    """Frame format type."""
    CAN_DATA = _cconsts.NX_FRAME_TYPE_CAN_DATA
    CAN_REMOTE = _cconsts.NX_FRAME_TYPE_CAN_REMOTE
    CAN_BUS_ERROR = _cconsts.NX_FRAME_TYPE_CAN_BUS_ERROR
    CAN20_DATA = _cconsts.NX_FRAME_TYPE_CAN20_DATA
    CANFD_DATA = _cconsts.NX_FRAME_TYPE_CANFD_DATA
    CANFDBRS_DATA = _cconsts.NX_FRAME_TYPE_CANFDBRS_DATA
    FLEX_RAY_DATA = _cconsts.NX_FRAME_TYPE_FLEX_RAY_DATA
    FLEX_RAY_NULL = _cconsts.NX_FRAME_TYPE_FLEX_RAY_NULL
    FLEX_RAY_SYMBOL = _cconsts.NX_FRAME_TYPE_FLEX_RAY_SYMBOL
    LIN_DATA = _cconsts.NX_FRAME_TYPE_LIN_DATA
    LIN_BUS_ERROR = _cconsts.NX_FRAME_TYPE_LIN_BUS_ERROR
    LIN_NO_RESPONSE = _cconsts.NX_FRAME_TYPE_LIN_NO_RESPONSE
    J1939_DATA = _cconsts.NX_FRAME_TYPE_J1939_DATA
    SPECIAL_DELAY = _cconsts.NX_FRAME_TYPE_SPECIAL_DELAY
    SPECIAL_LOG_TRIGGER = _cconsts.NX_FRAME_TYPE_SPECIAL_LOG_TRIGGER
    SPECIAL_START_TRIGGER = _cconsts.NX_FRAME_TYPE_SPECIAL_START_TRIGGER
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_errors.py sha256=de832ca7c9b8e9c67e24fcb7c9692518933b2e379620ba22643023e6f2a8813a bytes=992 -->
## FILE: nixnet/_errors.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_errors.py`
- sha256: `de832ca7c9b8e9c67e24fcb7c9692518933b2e379620ba22643023e6f2a8813a`
- bytes: 992

````python
import ctypes  # type: ignore
import warnings

from nixnet import _cconsts
from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import errors


def check_for_error(error_code):
    if error_code & _cconsts.NX_STATUS_ERROR:
        raise_xnet_error(error_code)
    elif error_code != _cconsts.NX_SUCCESS:
        status = status_to_string(error_code)
        warnings.warn(errors.XnetWarning(status, error_code))


def raise_xnet_error(error_code):
    status = status_to_string(error_code)
    raise errors.XnetError(status, error_code)


def status_to_string(status_code):
    buffer_size = 2048
    buffer_size_ctypes = _ctypedefs.u32(buffer_size)
    buffer_ctypes = ctypes.create_string_buffer(buffer_size)
    status_code_ctypes = _ctypedefs.nxStatus_t(status_code)
    _cfuncs.lib.nx_status_to_string(status_code_ctypes, buffer_size_ctypes, buffer_ctypes)
    status_string = buffer_ctypes.value.decode("ascii")
    return status_string
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_frames.py sha256=6d6e341ab0302eb10cc37c5739d2058666ace9135148559043f58711a4d41f18 bytes=5961 -->
## FILE: nixnet/_frames.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_frames.py`
- sha256: `6d6e341ab0302eb10cc37c5739d2058666ace9135148559043f58711a4d41f18`
- bytes: 5961

````python
import struct

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants
from nixnet import types


nxFrameFixed_t = struct.Struct('QIBBBB8s')  # NOQA: N801, N816
assert nxFrameFixed_t.size == 24, 'Incorrectly specified frame.'
FRAME_TIMESTAMP_INDEX = 0
FRAME_IDENTIFIER_INDEX = 1
FRAME_TYPE_INDEX = 2
FRAME_FLAG_INDEX = 3
FRAME_INFO_INDEX = 4
FRAME_PAYLOAD_LENGTH_INDEX = 5
FRAME_PAYLOAD_INDEX = 6

MAX_BASE_UNIT_PAYLOAD_LENGTH = 8


def _get_frame_payload_length(base):
    """Extract the payload length from a base unit.

    >>> blank_payload = 8 * b'\\0'
    >>> no_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0x0, blank_payload))
    >>> _get_frame_payload_length(no_payload)
    0
    >>> base_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0x8, blank_payload))
    >>> _get_frame_payload_length(base_payload)
    8
    >>> extra_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0xFF, blank_payload))
    >>> _get_frame_payload_length(extra_payload)
    255
    >>> j1939_type = _cconsts.NX_FRAME_TYPE_J1939_DATA
    >>> j1939 = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, j1939_type, 0, 0xFF, 0xFF, blank_payload))
    >>> _get_frame_payload_length(j1939)
    2047
    """
    payload_length = base[FRAME_PAYLOAD_LENGTH_INDEX]
    if base[FRAME_TYPE_INDEX] == _cconsts.NX_FRAME_TYPE_J1939_DATA:
        # J1939 uses three bits from the Info field as the high bites.
        payload_length |= (base[FRAME_INFO_INDEX] & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939) << 8
    return payload_length


def _calculate_payload_size(payload_length):
    """For a given payload, return the bytes needed for the payload.

    This is for the entire payload with padding, regardless of which unit it is
    stored in.

    >>> _calculate_payload_size(0)
    8
    >>> _calculate_payload_size(8)
    8
    >>> _calculate_payload_size(9)
    16
    >>> _calculate_payload_size(16)
    16
    """
    if 8 < payload_length:
        return (payload_length + 7) & 0x07F8
    else:
        return 8


def _calculate_payload_unit_size(payload_length):
    """For a given payload, return the bytes needed for the payload unit.

    This includes padding bytes

    >>> _calculate_payload_unit_size(0)
    0
    >>> _calculate_payload_unit_size(8)
    0
    >>> _calculate_payload_unit_size(9)
    8
    >>> _calculate_payload_unit_size(16)
    8
    """
    return _calculate_payload_size(payload_length) - MAX_BASE_UNIT_PAYLOAD_LENGTH


def _split_payload_length(payload_length):
    """Return how much of the payload is stored in the base unit verse the payload unit.

    This is without padding bytes.

    >>> _split_payload_length(0)
    (0, 0)
    >>> _split_payload_length(8)
    (8, 0)
    >>> _split_payload_length(9)
    (8, 1)
    >>> _split_payload_length(16)
    (8, 8)
    """
    payload_unit_length = max(payload_length - MAX_BASE_UNIT_PAYLOAD_LENGTH, 0)
    base_unit_length = payload_length - payload_unit_length
    return base_unit_length, payload_unit_length


def iterate_frames(bytes):
    """Yields RawFrames from the bytes"""
    base_pos = 0
    next_pos = base_pos
    while next_pos != len(bytes):
        base_pos = next_pos
        next_pos += nxFrameFixed_t.size
        if len(bytes) < next_pos:
            _errors.check_for_error(_cconsts.NX_ERR_INTERNAL_ERROR)

        raw_base = bytes[base_pos:next_pos]
        base_unit = nxFrameFixed_t.unpack(raw_base)
        payload_length = _get_frame_payload_length(base_unit)
        base_unit_length, payload_unit_length = _split_payload_length(payload_length)

        payload_pos = next_pos
        payload_pad_pos = payload_pos + payload_unit_length
        next_pos += _calculate_payload_unit_size(payload_length)

        base_unit_payload = base_unit[FRAME_PAYLOAD_INDEX][0:base_unit_length]
        payload_unit = bytes[payload_pos:payload_pad_pos]
        payload = base_unit_payload + payload_unit
        yield types.RawFrame(
            base_unit[FRAME_TIMESTAMP_INDEX],
            base_unit[FRAME_IDENTIFIER_INDEX],
            constants.FrameType(base_unit[FRAME_TYPE_INDEX]),
            base_unit[FRAME_FLAG_INDEX],
            base_unit[FRAME_INFO_INDEX],
            payload)


def serialize_frame(frame):
    """Yields units that compose the frame."""
    payload = bytes(frame.payload)
    base_unit_payload = payload[0:MAX_BASE_UNIT_PAYLOAD_LENGTH]
    base_unit_padding_length = max(MAX_BASE_UNIT_PAYLOAD_LENGTH - len(base_unit_payload), 0)
    base_unit_payload += b'\0' * base_unit_padding_length

    payload_unit = payload[MAX_BASE_UNIT_PAYLOAD_LENGTH:]
    payload_unit_padding_length = _calculate_payload_unit_size(len(payload)) - len(payload_unit)
    payload_unit += b'\0' * payload_unit_padding_length

    payload_length = len(payload)
    if frame.type == constants.FrameType.J1939_DATA:
        if (frame.info & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939) != 0:
            # Invalid data where info_length will go.
            _errors.check_for_error(_cconsts.NX_ERR_INTERNAL_ERROR)
        info_length = payload_length >> 8
        if info_length != (info_length & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939):
            _errors.check_for_error(_cconsts.NX_ERR_FRAME_WRITE_TOO_LARGE)
        info = frame.info | info_length
        payload_length &= 0xFF
    else:
        if payload_length != (payload_length & 0xFF):
            _errors.check_for_error(_cconsts.NX_ERR_NON_J1939_FRAME_SIZE)
        info = frame.info

    base_unit = nxFrameFixed_t.pack(
        frame.timestamp,
        frame.identifier,
        frame.type.value,
        frame.flags,
        info,
        payload_length,
        base_unit_payload)
    yield base_unit

    if payload_unit:
        yield payload_unit
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_funcs.py sha256=715aefe20b1d2f4576d4195b17c517b0c72324ec5a2e4301e66abe6854987695 bytes=27472 -->
## FILE: nixnet/_funcs.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_funcs.py`
- sha256: `715aefe20b1d2f4576d4195b17c517b0c72324ec5a2e4301e66abe6854987695`
- bytes: 27472

````python
import ctypes  # type: ignore
import typing  # NOQA: F401

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _enums  # NOQA: F401
from nixnet import _errors


def nx_create_session(
    database_name,  # type: typing.Text
    cluster_name,  # type: typing.Text
    list,  # type: typing.Text
    interface,  # type: typing.Text
    mode,  # type: _enums.CreateSessionMode
):
    # type: (...) -> int
    database_name_ctypes = ctypes.create_string_buffer(database_name.encode('ascii'))
    cluster_name_ctypes = ctypes.create_string_buffer(cluster_name.encode('ascii'))
    list_ctypes = ctypes.create_string_buffer(list.encode('ascii'))
    interface_ctypes = ctypes.create_string_buffer(interface.encode('ascii'))
    mode_ctypes = _ctypedefs.u32(mode.value)
    session_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_create_session(
        database_name_ctypes,  # type: ignore
        cluster_name_ctypes,  # type: ignore
        list_ctypes,  # type: ignore
        interface_ctypes,  # type: ignore
        mode_ctypes,
        ctypes.pointer(session_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return session_ref_ctypes.value


def nx_create_session_by_ref(
    database_refs,  # type: typing.List[_ctypedefs.nxDatabaseRef_t]
    interface,  # type: typing.Text
    mode,  # type: _enums.CreateSessionMode
):
    # type: (...) -> int
    size_of_database_refs_ctypes = _ctypedefs.u32(len(database_refs) * _ctypedefs.nxDatabaseRef_t.BYTES)
    database_refs_ctypes = (_ctypedefs.nxDatabaseRef_t * len(database_refs))(*database_refs)  # type: ignore
    interface_ctypes = ctypes.create_string_buffer(interface.encode('ascii'))
    mode_ctypes = _ctypedefs.u32(mode.value)
    session_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_create_session_by_ref(
        size_of_database_refs_ctypes,
        database_refs_ctypes,
        interface_ctypes,  # type: ignore
        mode_ctypes,
        ctypes.pointer(session_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return session_ref_ctypes.value


def nx_get_property_size(
    session_ref,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_get_property_size(
        session_ref_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nx_get_sub_property_size(
    session_ref,  # type: int
    active_index,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    active_index_ctypes = _ctypedefs.u32(active_index)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_get_sub_property_size(
        session_ref_ctypes,
        active_index_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nx_read_frame(
    session_ref,  # type: int
    bytes_to_read,  # type: int
    timeout,  # type: float
):
    # type: (...) -> typing.Tuple[bytes, int]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    buffer_ctypes = (_ctypedefs.byte * bytes_to_read)()  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(_ctypedefs.byte.BYTES * bytes_to_read)
    number_of_bytes_returned_ctypes = _ctypedefs.u32()
    timeout_ctypes = _ctypedefs.f64(timeout)
    result = _cfuncs.lib.nx_read_frame(
        session_ref_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        timeout_ctypes,
        ctypes.pointer(number_of_bytes_returned_ctypes))
    _errors.check_for_error(result.value)
    return buffer_ctypes.raw, number_of_bytes_returned_ctypes.value  # type: ignore


def nx_read_signal_single_point(
    session_ref,  # type: int
    num_signals,  # type: int
):
    # type: (...) -> typing.Tuple[ctypes.Array[_ctypedefs.nxTimestamp_t], ctypes.Array[_ctypedefs.f64]]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * num_signals)()  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES * num_signals)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * num_signals)()  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(_ctypedefs.nxTimestamp_t.BYTES * num_signals)
    result = _cfuncs.lib.nx_read_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes
    )
    _errors.check_for_error(result.value)
    return timestamp_buffer_ctypes, value_buffer_ctypes


def nx_read_state(
    session_ref,  # type: int
    state_id,  # type: _enums.ReadState
    state_size,  # type: int
    state_value_ctypes_ptr,  # type: typing.Any
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    state_id_ctypes = _ctypedefs.u32(state_id.value)
    state_size_ctypes = _ctypedefs.u32(state_size)
    fault_ctypes = _ctypedefs.nxStatus_t()
    result = _cfuncs.lib.nx_read_state(
        session_ref_ctypes,
        state_id_ctypes,
        state_size_ctypes,
        state_value_ctypes_ptr,
        ctypes.pointer(fault_ctypes),
    )
    _errors.check_for_error(result.value)
    return fault_ctypes.value


def nx_write_frame(
    session_ref,  # type: int
    buffer,  # type: typing.Any
    timeout,  # type: float
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    buffer_ctypes = (_ctypedefs.byte * len(buffer))(*buffer)  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(len(buffer) * _ctypedefs.byte.BYTES)
    timeout_ctypes = _ctypedefs.f64(timeout)
    result = _cfuncs.lib.nx_write_frame(
        session_ref_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        timeout_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_single_point(
    session_ref,  # type: int
    value_buffer,  # type: typing.List[float]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    result = _cfuncs.lib.nx_write_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_waveform(
    session_ref,  # type: int
    timeout,  # type: float
    value_buffer,  # type: typing.List[float]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    result = _cfuncs.lib.nx_write_signal_waveform(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_xy(
    session_ref,  # type: int
    timeout,  # type: float
    value_buffer,  # type: typing.List[float]
    timestamp_buffer,  # type: typing.List[int]
    num_pairs_buffer,  # type: typing.List[int]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * len(timestamp_buffer))(*timestamp_buffer)  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(len(timestamp_buffer) * _ctypedefs.nxTimestamp_t.BYTES)
    num_pairs_buffer_ctypes = (_ctypedefs.u32 * len(num_pairs_buffer))(*num_pairs_buffer)  # type: ignore
    size_of_num_pairs_buffer_ctypes = _ctypedefs.u32(len(num_pairs_buffer) * _ctypedefs.u32.BYTES)
    result = _cfuncs.lib.nx_write_signal_xy(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes,
        num_pairs_buffer_ctypes,
        size_of_num_pairs_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_state(
    session_ref,  # type: int
    state_id,  # type: _enums.WriteState
    state_value_ctypes,  # type: typing.Any
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    state_id_ctypes = _ctypedefs.u32(state_id.value)
    state_size_ctypes = state_value_ctypes.BYTES
    result = _cfuncs.lib.nx_write_state(
        session_ref_ctypes,
        state_id_ctypes,
        state_size_ctypes,
        ctypes.pointer(state_value_ctypes),  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_convert_frames_to_signals_single_point(
    session_ref,  # type: int
    frame_buffer,  # type: bytes
    num_signals,  # type: int
):
    # type: (...) -> typing.Tuple[ctypes.Array[_ctypedefs.nxTimestamp_t], ctypes.Array[_ctypedefs.f64]]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    frame_buffer_ctypes = (_ctypedefs.byte * len(frame_buffer))(*frame_buffer)  # type: ignore
    size_of_frame_buffer_ctypes = _ctypedefs.u32(len(frame_buffer) * _ctypedefs.byte.BYTES)
    value_buffer_ctypes = (_ctypedefs.f64 * num_signals)()  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES * num_signals)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * num_signals)()  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(_ctypedefs.nxTimestamp_t.BYTES * num_signals)
    result = _cfuncs.lib.nx_convert_frames_to_signals_single_point(
        session_ref_ctypes,
        frame_buffer_ctypes,
        size_of_frame_buffer_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes,
    )
    _errors.check_for_error(result.value)
    return timestamp_buffer_ctypes, value_buffer_ctypes


def nx_convert_signals_to_frames_single_point(
    session_ref,  # type: int
    value_buffer,  # type: typing.List[float]
    bytes_to_read,  # type: int
):
    # type: (...) -> typing.Tuple[bytes, int]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    buffer_ctypes = (_ctypedefs.byte * bytes_to_read)()  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(_ctypedefs.byte.BYTES * bytes_to_read)
    number_of_bytes_returned_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_convert_signals_to_frames_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        ctypes.pointer(number_of_bytes_returned_ctypes),
    )
    _errors.check_for_error(result.value)
    return buffer_ctypes.raw, number_of_bytes_returned_ctypes.value  # type: ignore


def nx_blink(
    interface_ref,  # type: int
    modifier,  # type: _enums.BlinkMode
):
    # type: (...) -> None
    interface_ref_ctypes = _ctypedefs.nxSessionRef_t(interface_ref)
    modifier_ctypes = _ctypedefs.u32(modifier.value)
    result = _cfuncs.lib.nx_blink(
        interface_ref_ctypes,
        modifier_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_clear(
    session_ref,  # type: int
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    result = _cfuncs.lib.nx_clear(
        session_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_connect_terminals(
    session_ref,  # type: int
    source,  # type: typing.Text
    destination,  # type: typing.Text
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = ctypes.create_string_buffer(source.encode('ascii'))
    destination_ctypes = ctypes.create_string_buffer(destination.encode('ascii'))
    result = _cfuncs.lib.nx_connect_terminals(
        session_ref_ctypes,
        source_ctypes,  # type: ignore
        destination_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_disconnect_terminals(
    session_ref,  # type: int
    source,  # type: typing.Text
    destination,  # type: typing.Text
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = ctypes.create_string_buffer(source.encode('ascii'))
    destination_ctypes = ctypes.create_string_buffer(destination.encode('ascii'))
    result = _cfuncs.lib.nx_disconnect_terminals(
        session_ref_ctypes,
        source_ctypes,  # type: ignore
        destination_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_flush(
    session_ref,  # type: int
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    result = _cfuncs.lib.nx_flush(
        session_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_start(
    session_ref,  # type: int
    scope,  # type: _enums.StartStopScope
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope.value)
    result = _cfuncs.lib.nx_start(
        session_ref_ctypes,
        scope_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_stop(
    session_ref,  # type: int
    scope,  # type: _enums.StartStopScope
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope.value)
    result = _cfuncs.lib.nx_stop(
        session_ref_ctypes,
        scope_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_system_open(
):
    # type: (...) -> int
    system_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_system_open(
        ctypes.pointer(system_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return system_ref_ctypes.value


def nx_system_close(
    system_ref,  # type: int
):
    # type: (...) -> None
    system_ref_ctypes = _ctypedefs.nxSessionRef_t(system_ref)
    result = _cfuncs.lib.nx_system_close(
        system_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_wait(
    session_ref,  # type: int
    condition,  # type: _enums.Condition
    param_in,  # type: int
    timeout,  # type: float
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    condition_ctypes = _ctypedefs.u32(condition.value)
    param_in_ctypes = _ctypedefs.u32(param_in)
    timeout_ctypes = _ctypedefs.f64(timeout)
    param_out_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_wait(
        session_ref_ctypes,
        condition_ctypes,
        param_in_ctypes,
        timeout_ctypes,
        ctypes.pointer(param_out_ctypes),
    )
    _errors.check_for_error(result.value)
    return param_out_ctypes.value


def nxdb_open_database(
    database_name,  # type: typing.Text
):
    # type: (...) -> int
    database_name_ctypes = ctypes.create_string_buffer(database_name.encode('ascii'))
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_open_database(
        database_name_ctypes,  # type: ignore
        ctypes.pointer(database_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return database_ref_ctypes.value


def nxdb_close_database(
    database_ref,  # type: int
    close_all_refs,  # type: bool
):
    # type: (...) -> None
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    close_all_refs_ctypes = _ctypedefs.bool32(close_all_refs)
    result = _cfuncs.lib.nxdb_close_database(
        database_ref_ctypes,
        close_all_refs_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_create_object(
    parent_object_ref,  # type: int
    object_class,  # type: _enums.ObjectClass
    object_name,  # type: typing.Text
):
    # type: (...) -> int
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class.value)
    object_name_ctypes = ctypes.create_string_buffer(object_name.encode('ascii'))
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_create_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,  # type: ignore
        ctypes.pointer(db_object_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return db_object_ref_ctypes.value


def nxdb_find_object(
    parent_object_ref,  # type: int
    object_class,  # type: _enums.ObjectClass
    object_name,  # type: typing.Text
):
    # type: (...) -> int
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class.value)
    object_name_ctypes = ctypes.create_string_buffer(object_name.encode('ascii'))
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_find_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,  # type: ignore
        ctypes.pointer(db_object_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return db_object_ref_ctypes.value


def nxdb_delete_object(
    db_object_ref,  # type: int
):
    # type: (...) -> None
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    result = _cfuncs.lib.nxdb_delete_object(
        db_object_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_save_database(
    database_ref,  # type: int
    db_filepath,  # type: typing.Text
):
    # type: (...) -> None
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    db_filepath_ctypes = ctypes.create_string_buffer(db_filepath.encode('ascii'))
    result = _cfuncs.lib.nxdb_save_database(
        database_ref_ctypes,
        db_filepath_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_get_property_size(
    db_object_ref,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_property_size(
        db_object_ref_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nxdb_get_dbc_attribute_size(
    db_object_ref,  # type: int
    mode,  # type: _enums.GetDbcAttributeMode
    attribute_name,  # type: typing.Text
):
    # type: (...) -> int
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode.value)
    attribute_name_ctypes = ctypes.create_string_buffer(attribute_name.encode('ascii'))
    attribute_text_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_dbc_attribute_size(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,  # type: ignore
        ctypes.pointer(attribute_text_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return attribute_text_size_ctypes.value


def nxdb_get_dbc_attribute(
    db_object_ref,  # type: int
    mode,  # type:  _enums.GetDbcAttributeMode
    attribute_name,  # type: typing.Text
    attribute_text_size,  # type: int
):
    # type: (...) -> typing.Tuple[typing.Text, bool]
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode.value)
    attribute_name_ctypes = ctypes.create_string_buffer(attribute_name.encode('ascii'))
    attribute_text_size_ctypes = _ctypedefs.u32(attribute_text_size)
    attribute_text_ctypes = ctypes.create_string_buffer(attribute_text_size)
    is_default_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_dbc_attribute(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,  # type: ignore
        attribute_text_size_ctypes,
        attribute_text_ctypes,  # type: ignore
        ctypes.pointer(is_default_ctypes),
    )
    _errors.check_for_error(result.value)
    attribute_text = attribute_text_ctypes.value.decode("ascii")
    is_default = bool(is_default_ctypes.value)
    return attribute_text, is_default


def nxdb_merge(
    target_cluster_ref,  # type: int
    source_obj_ref,  # type: int
    copy_mode,  # type: int
    prefix,  # type: typing.Text
    wait_for_complete,  # type: bool
):
    # type: (...) -> int
    target_cluster_ref_ctypes = _ctypedefs.nxDatabaseRef_t(target_cluster_ref)
    source_obj_ref_ctypes = _ctypedefs.nxDatabaseRef_t(source_obj_ref)
    copy_mode_ctypes = _ctypedefs.u32(copy_mode)
    prefix_ctypes = ctypes.create_string_buffer(prefix.encode('ascii'))
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_merge(
        target_cluster_ref_ctypes,
        source_obj_ref_ctypes,
        copy_mode_ctypes,
        prefix_ctypes,  # type: ignore
        wait_for_complete_ctypes,
        ctypes.pointer(percent_complete_ctypes),
    )
    _errors.check_for_error(result.value)
    return percent_complete_ctypes.value


def nxdb_add_alias(
    database_alias,  # type: typing.Text
    database_filepath,  # type: typing.Text
    default_baud_rate,  # type: int
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    database_filepath_ctypes = ctypes.create_string_buffer(database_filepath.encode('ascii'))
    default_baud_rate_ctypes = _ctypedefs.u32(default_baud_rate)
    result = _cfuncs.lib.nxdb_add_alias(
        database_alias_ctypes,  # type: ignore
        database_filepath_ctypes,  # type: ignore
        default_baud_rate_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_add_alias64(
    database_alias,  # type: typing.Text
    database_filepath,  # type: typing.Text
    default_baud_rate,  # type: int
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    database_filepath_ctypes = ctypes.create_string_buffer(database_filepath.encode('ascii'))
    default_baud_rate_ctypes = _ctypedefs.u64(default_baud_rate)
    result = _cfuncs.lib.nxdb_add_alias64(
        database_alias_ctypes,  # type: ignore
        database_filepath_ctypes,  # type: ignore
        default_baud_rate_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_remove_alias(
    database_alias,  # type: typing.Text
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    result = _cfuncs.lib.nxdb_remove_alias(
        database_alias_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_deploy(
    ip_address,  # type: typing.Text
    database_alias,  # type: typing.Text
    wait_for_complete,  # type: bool
):
    # type: (...) -> int
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_deploy(
        ip_address_ctypes,  # type: ignore
        database_alias_ctypes,  # type: ignore
        wait_for_complete_ctypes,
        ctypes.pointer(percent_complete_ctypes),
    )
    _errors.check_for_error(result.value)
    return percent_complete_ctypes.value


def nxdb_undeploy(
    ip_address,  # type: typing.Text
    database_alias,  # type: typing.Text
):
    # type: (...) -> None
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    result = _cfuncs.lib.nxdb_undeploy(
        ip_address_ctypes,  # type: ignore
        database_alias_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_get_database_list(
    ip_address,  # type: typing.Text
    size_of_alias_buffer,  # type: int
    size_of_filepath_buffer,  # type: int
):
    # type: (...) -> typing.Tuple[typing.Text, typing.Text, int]
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    size_of_alias_buffer_ctypes = _ctypedefs.u32(size_of_alias_buffer)
    size_of_filepath_buffer_ctypes = _ctypedefs.u32(size_of_filepath_buffer)
    alias_buffer_ctypes = ctypes.create_string_buffer(size_of_alias_buffer)
    filepath_buffer_ctypes = ctypes.create_string_buffer(size_of_filepath_buffer)
    number_of_databases_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_database_list(
        ip_address_ctypes,  # type: ignore
        size_of_alias_buffer_ctypes,
        alias_buffer_ctypes,  # type: ignore
        size_of_filepath_buffer_ctypes,
        filepath_buffer_ctypes,  # type: ignore
        number_of_databases_ctypes,
    )
    _errors.check_for_error(result.value)
    alias_buffer = alias_buffer_ctypes.value.decode("ascii")
    filepath_buffer = filepath_buffer_ctypes.value.decode("ascii")
    return alias_buffer, filepath_buffer, number_of_databases_ctypes.value


def nxdb_get_database_list_sizes(
    ip_address,  # type: typing.Text
):
    # type: (...) -> typing.Tuple[int, int]
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    size_of_alias_buffer_ctypes = _ctypedefs.u32()
    size_of_filepath_buffer_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_database_list_sizes(
        ip_address_ctypes,  # type: ignore
        size_of_alias_buffer_ctypes,
        size_of_filepath_buffer_ctypes,
    )
    _errors.check_for_error(result.value)
    return size_of_alias_buffer_ctypes.value, size_of_filepath_buffer_ctypes.value
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_lib.py sha256=1cfb791e276cada0432919578aa6b751ab96ad813390d54840bd30328b3197d1 bytes=2134 -->
## FILE: nixnet/_lib.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_lib.py`
- sha256: `1cfb791e276cada0432919578aa6b751ab96ad813390d54840bd30328b3197d1`
- bytes: 2134

````python
import ctypes  # type: ignore
import sys

from nixnet import errors


class PlatformUnsupportedError(errors.Error):

    def __init__(self, platform):
        message = '{0} is unsupported by this package.'.format(platform)
        super(PlatformUnsupportedError, self).__init__(message, platform)


class XnetNotFoundError(errors.Error):

    def __init__(self, *args):
        message = (
            'Could not find an installation of NI-XNET. Please '
            'ensure that NI-XNET is installed on this machine or '
            'contact National Instruments for support.')
        super(XnetNotFoundError, self).__init__(message, *args)


class XnetFunctionNotSupportedError(errors.Error):

    def __init__(self, function):
        message = (
            'The NI-XNET function "{0}" is not supported in this '
            'version of NI-XNET. Visit ni.com/downloads to upgrade your '
            'version of NI-XNET.'.format(function))
        super(XnetFunctionNotSupportedError, self).__init__(message, function)


class XnetLibrary(object):
    """Proxy Library to consolidate nixnet-specific logic."""

    def __init__(self, library):
        self._library = library

    def __getattr__(self, function):
        try:
            return getattr(self._library, function)
        except AttributeError:
            raise XnetFunctionNotSupportedError(function)


def _import_win_lib():
    lib_name = "nixnet"
    try:
        cdll = ctypes.cdll.LoadLibrary(lib_name)
    except OSError:
        raise XnetNotFoundError()
    return XnetLibrary(cdll)


def _import_linux_lib():
    lib_name = "libnixnet.so"
    try:
        cdll = ctypes.cdll.LoadLibrary(lib_name)
    except OSError:
        raise XnetNotFoundError()
    return XnetLibrary(cdll)


def _import_unsupported():
    raise PlatformUnsupportedError(sys.platform)


if sys.platform.startswith('win') or sys.platform.startswith('cli'):
    import_lib = _import_win_lib
elif sys.platform.startswith('linux'):
    import_lib = _import_linux_lib
else:
    import_lib = _import_unsupported
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_props.py sha256=bb6e860bb11d602879c925cc4bf8588fdc6d3bf193308ba4eecd9f68f53fec62 bytes=109543 -->
## FILE: nixnet/_props.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_props.py`
- sha256: `bb6e860bb11d602879c925cc4bf8588fdc6d3bf193308ba4eecd9f68f53fec62`
- bytes: 109543

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _cprops


def get_session_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_APPLICATION_PROTOCOL,
    )


def get_session_auto_start(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_AUTO_START,
    )


def set_session_auto_start(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_AUTO_START,
        value,
    )


def get_session_cluster_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_CLUSTER_NAME,
    )


def get_session_database_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_DATABASE_NAME,
    )


def get_session_list(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[typing.Text]
    return _cprops.get_session_string_array(
        ref,
        _cconsts.NX_PROP_SESSION_LIST,
    )


def get_session_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_MODE,
    )


def get_session_num_frames(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_FRAMES,
    )


def get_session_num_in_list(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_IN_LIST,
    )


def get_session_num_pend(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_PEND,
    )


def get_session_num_unused(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_UNUSED,
    )


def get_session_payld_len_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_PAYLD_LEN_MAX,
    )


def get_session_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_PROTOCOL,
    )


def get_session_queue_size(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_QUEUE_SIZE,
    )


def set_session_queue_size(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_QUEUE_SIZE,
        value,
    )


def get_session_resamp_rate(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_RESAMP_RATE,
    )


def set_session_resamp_rate(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_RESAMP_RATE,
        value,
    )


def get_session_intf_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE,
    )


def set_session_intf_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE,
        value,
    )


def get_session_intf_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE64,
    )


def set_session_intf_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE64,
        value,
    )


def get_session_intf_bus_err_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BUS_ERR_TO_IN_STRM,
    )


def set_session_intf_bus_err_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BUS_ERR_TO_IN_STRM,
        value,
    )


def get_session_intf_echo_tx(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_ECHO_TX,
    )


def set_session_intf_echo_tx(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_ECHO_TX,
        value,
    )


def get_session_intf_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_NAME,
    )


def get_session_intf_out_strm_list(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_LIST,
    )


def set_session_intf_out_strm_list(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_ref_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_LIST,
        value,
    )


def get_session_intf_out_strm_timng(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_TIMNG,
    )


def set_session_intf_out_strm_timng(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_TIMNG,
        value,
    )


def get_session_intf_start_trig_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_START_TRIG_TO_IN_STRM,
    )


def set_session_intf_start_trig_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_START_TRIG_TO_IN_STRM,
        value,
    )


def set_session_intf_can_ext_tcvr_config(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EXT_TCVR_CONFIG,
        value,
    )


def get_session_intf_can_lstn_only(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_LSTN_ONLY,
    )


def set_session_intf_can_lstn_only(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_LSTN_ONLY,
        value,
    )


def get_session_intf_can_pend_tx_order(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_PEND_TX_ORDER,
    )


def set_session_intf_can_pend_tx_order(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_PEND_TX_ORDER,
        value,
    )


def get_session_intf_can_sing_shot(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_SING_SHOT,
    )


def set_session_intf_can_sing_shot(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_SING_SHOT,
        value,
    )


def get_session_intf_can_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TERM,
    )


def set_session_intf_can_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TERM,
        value,
    )


def get_session_intf_can_tcvr_state(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_STATE,
    )


def set_session_intf_can_tcvr_state(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_STATE,
        value,
    )


def get_session_intf_can_tcvr_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_TYPE,
    )


def set_session_intf_can_tcvr_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_TYPE,
        value,
    )


def get_session_intf_can_out_strm_list_by_id(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_OUT_STRM_LIST_BY_ID,
    )


def set_session_intf_can_out_strm_list_by_id(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_OUT_STRM_LIST_BY_ID,
        value,
    )


def get_session_intf_can_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_IO_MODE,
    )


def get_session_intf_can_fd_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE,
    )


def set_session_intf_can_fd_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE,
        value,
    )


def get_session_intf_can_fd_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE64,
    )


def set_session_intf_can_fd_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE64,
        value,
    )


def get_session_intf_can_tx_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TX_IO_MODE,
    )


def set_session_intf_can_tx_io_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TX_IO_MODE,
        value,
    )


def get_session_intf_can_fd_iso_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_ISO_MODE,
    )


def set_session_intf_can_fd_iso_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_ISO_MODE,
        value,
    )


def get_session_intf_flex_ray_acc_start_rng(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ACC_START_RNG,
    )


def set_session_intf_flex_ray_acc_start_rng(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ACC_START_RNG,
        value,
    )


def get_session_intf_flex_ray_alw_hlt_clk(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_HLT_CLK,
    )


def set_session_intf_flex_ray_alw_hlt_clk(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_HLT_CLK,
        value,
    )


def get_session_intf_flex_ray_alw_pass_act(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_PASS_ACT,
    )


def set_session_intf_flex_ray_alw_pass_act(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_PASS_ACT,
        value,
    )


def get_session_intf_flex_ray_auto_aslp_whn_stp(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP,
    )


def set_session_intf_flex_ray_auto_aslp_whn_stp(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP,
        value,
    )


def get_session_intf_flex_ray_clst_drift_dmp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP,
    )


def set_session_intf_flex_ray_clst_drift_dmp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP,
        value,
    )


def get_session_intf_flex_ray_coldstart(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_COLDSTART,
    )


def get_session_intf_flex_ray_dec_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DEC_CORR,
    )


def set_session_intf_flex_ray_dec_corr(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DEC_CORR,
        value,
    )


def get_session_intf_flex_ray_delay_comp_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_A,
    )


def set_session_intf_flex_ray_delay_comp_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_A,
        value,
    )


def get_session_intf_flex_ray_delay_comp_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_B,
    )


def set_session_intf_flex_ray_delay_comp_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_B,
        value,
    )


def get_session_intf_flex_ray_key_slot_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID,
    )


def set_session_intf_flex_ray_key_slot_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID,
        value,
    )


def get_session_intf_flex_ray_latest_tx(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LATEST_TX,
    )


def get_session_intf_flex_ray_list_timo(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LIST_TIMO,
    )


def set_session_intf_flex_ray_list_timo(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LIST_TIMO,
        value,
    )


def get_session_intf_flex_ray_mac_init_off_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A,
    )


def set_session_intf_flex_ray_mac_init_off_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A,
        value,
    )


def get_session_intf_flex_ray_mac_init_off_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B,
    )


def set_session_intf_flex_ray_mac_init_off_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B,
        value,
    )


def get_session_intf_flex_ray_mic_init_off_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A,
    )


def set_session_intf_flex_ray_mic_init_off_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A,
        value,
    )


def get_session_intf_flex_ray_mic_init_off_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B,
    )


def set_session_intf_flex_ray_mic_init_off_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B,
        value,
    )


def get_session_intf_flex_ray_max_drift(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAX_DRIFT,
    )


def set_session_intf_flex_ray_max_drift(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAX_DRIFT,
        value,
    )


def get_session_intf_flex_ray_microtick(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MICROTICK,
    )


def get_session_intf_flex_ray_null_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM,
    )


def set_session_intf_flex_ray_null_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM,
        value,
    )


def get_session_intf_flex_ray_off_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR,
    )


def get_session_intf_flex_ray_off_corr_out(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR_OUT,
    )


def set_session_intf_flex_ray_off_corr_out(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR_OUT,
        value,
    )


def get_session_intf_flex_ray_rate_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR,
    )


def get_session_intf_flex_ray_rate_corr_out(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR_OUT,
    )


def set_session_intf_flex_ray_rate_corr_out(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR_OUT,
        value,
    )


def get_session_intf_flex_ray_samp_per_micro(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO,
    )


def set_session_intf_flex_ray_samp_per_micro(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO,
        value,
    )


def get_session_intf_flex_ray_sing_slot_en(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SING_SLOT_EN,
    )


def set_session_intf_flex_ray_sing_slot_en(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SING_SLOT_EN,
        value,
    )


def get_session_intf_flex_ray_statistics_en(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_STATISTICS_EN,
    )


def set_session_intf_flex_ray_statistics_en(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_STATISTICS_EN,
        value,
    )


def get_session_intf_flex_ray_sym_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM,
    )


def set_session_intf_flex_ray_sym_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM,
        value,
    )


def get_session_intf_flex_ray_sync_ch_a_even(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_EVEN,
    )


def get_session_intf_flex_ray_sync_ch_a_odd(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_ODD,
    )


def get_session_intf_flex_ray_sync_ch_b_even(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_EVEN,
    )


def get_session_intf_flex_ray_sync_ch_b_odd(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_ODD,
    )


def get_session_intf_flex_ray_sync_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_STATUS,
    )


def get_session_intf_flex_ray_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_TERM,
    )


def set_session_intf_flex_ray_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_TERM,
        value,
    )


def get_session_intf_flex_ray_wakeup_ch(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_CH,
    )


def set_session_intf_flex_ray_wakeup_ch(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_CH,
        value,
    )


def get_session_intf_flex_ray_wakeup_ptrn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_PTRN,
    )


def set_session_intf_flex_ray_wakeup_ptrn(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_PTRN,
        value,
    )


def set_session_intf_flex_ray_sleep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SLEEP,
        value,
    )


def get_session_intf_flex_ray_connected_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CONNECTED_CHS,
    )


def set_session_intf_flex_ray_connected_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CONNECTED_CHS,
        value,
    )


def get_session_intf_lin_break_length(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_BREAK_LENGTH,
    )


def set_session_intf_lin_break_length(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_BREAK_LENGTH,
        value,
    )


def get_session_intf_lin_master(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_MASTER,
    )


def set_session_intf_lin_master(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_MASTER,
        value,
    )


def get_session_intf_lin_sched_names(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[typing.Text]
    return _cprops.get_session_string_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_SCHED_NAMES,
    )


def set_session_intf_lin_sleep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_SLEEP,
        value,
    )


def get_session_intf_lin_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_TERM,
    )


def set_session_intf_lin_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_TERM,
        value,
    )


def get_session_intf_lin_diag_p2min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_P_2MIN,
    )


def set_session_intf_lin_diag_p2min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_P_2MIN,
        value,
    )


def get_session_intf_lin_diag_stmin(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_S_TMIN,
    )


def set_session_intf_lin_diag_stmin(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_S_TMIN,
        value,
    )


def get_session_intf_lin_alw_start_wo_bus_pwr(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_ALW_START_WO_BUS_PWR,
    )


def set_session_intf_lin_alw_start_wo_bus_pwr(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_ALW_START_WO_BUS_PWR,
        value,
    )


def get_session_intf_lin_ostr_slv_rsp_lst_by_nad(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD,
    )


def set_session_intf_lin_ostr_slv_rsp_lst_by_nad(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD,
        value,
    )


def get_session_intf_lin_no_response_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM,
    )


def set_session_intf_lin_no_response_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM,
        value,
    )


def get_session_intf_lin_checksum_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_CHECKSUM_TO_IN_STRM,
    )


def set_session_intf_lin_checksum_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_CHECKSUM_TO_IN_STRM,
        value,
    )


def get_session_intf_src_term_start_trigger(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_SRC_TERM_START_TRIGGER,
    )


def set_session_intf_src_term_start_trigger(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_SRC_TERM_START_TRIGGER,
        value,
    )


def get_session_j1939_address(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ADDRESS,
    )


def set_session_j1939_address(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ADDRESS,
        value,
    )


def get_session_j1939_name(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NAME,
    )


def set_session_j1939_name(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NAME,
        value,
    )


def set_session_j1939_ecu(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_ref(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ECU,
        value,
    )


def get_session_j1939_timeout_t1(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T1,
    )


def set_session_j1939_timeout_t1(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T1,
        value,
    )


def get_session_j1939_timeout_t2(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T2,
    )


def set_session_j1939_timeout_t2(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T2,
        value,
    )


def get_session_j1939_timeout_t3(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T3,
    )


def set_session_j1939_timeout_t3(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T3,
        value,
    )


def get_session_j1939_timeout_t4(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T4,
    )


def set_session_j1939_timeout_t4(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T4,
        value,
    )


def get_session_j1939_response_time_tr_sd(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_SD,
    )


def set_session_j1939_response_time_tr_sd(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_SD,
        value,
    )


def get_session_j1939_response_time_tr_gd(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_GD,
    )


def set_session_j1939_response_time_tr_gd(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_GD,
        value,
    )


def get_session_j1939_hold_time_th(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_HOLD_TIME_TH,
    )


def set_session_j1939_hold_time_th(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_HOLD_TIME_TH,
        value,
    )


def get_session_j1939_num_packets_recv(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RECV,
    )


def set_session_j1939_num_packets_recv(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RECV,
        value,
    )


def get_session_j1939_num_packets_resp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RESP,
    )


def set_session_j1939_num_packets_resp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RESP,
        value,
    )


def get_session_j1939_max_repeat_cts(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_MAX_REPEAT_CTS,
    )


def set_session_j1939_max_repeat_cts(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_MAX_REPEAT_CTS,
        value,
    )


def get_session_j1939_fill_byte(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_FILL_BYTE,
    )


def set_session_j1939_fill_byte(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_FILL_BYTE,
        value,
    )


def get_session_j1939_write_queue_size(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_WRITE_QUEUE_SIZE,
    )


def set_session_j1939_write_queue_size(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_WRITE_QUEUE_SIZE,
        value,
    )


def get_session_j1939_ecu_busy(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ECU_BUSY,
    )


def set_session_j1939_ecu_busy(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ECU_BUSY,
        value,
    )


def get_session_j1939_include_dest_addr_in_pgn(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_INCLUDE_DEST_ADDR_IN_PGN,
    )


def set_session_j1939_include_dest_addr_in_pgn(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_INCLUDE_DEST_ADDR_IN_PGN,
        value,
    )


def get_session_intf_can_edge_filter(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EDGE_FILTER,
    )


def set_session_intf_can_edge_filter(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EDGE_FILTER,
        value,
    )


def get_session_intf_can_transmit_pause(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TRANSMIT_PAUSE,
    )


def set_session_intf_can_transmit_pause(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TRANSMIT_PAUSE,
        value,
    )


def get_session_intf_can_disable_prot_exception_handling(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING,
    )


def set_session_intf_can_disable_prot_exception_handling(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING,
        value,
    )


def set_session_can_start_time_off(
    ref,  # type: int
    sub,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_sub_f64(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_CAN_START_TIME_OFF,
        value,
    )


def set_session_can_tx_time(
    ref,  # type: int
    sub,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_sub_f64(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_CAN_TX_TIME,
        value,
    )


def set_session_skip_n_cyclic_frames(
    ref,  # type: int
    sub,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_sub_u32(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_SKIP_N_CYCLIC_FRAMES,
        value,
    )


def set_session_lin_tx_n_corrupted_chksums(
    ref,  # type: int
    sub,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_sub_u32(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_LIN_TX_N_CORRUPTED_CHKSUMS,
        value,
    )


def set_session_j1939_addr_filter(
    ref,  # type: int
    sub,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_session_sub_string(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_J1939_ADDR_FILTER,
        value,
    )


def get_system_dev_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_DEV_REFS,
    )


def get_system_intf_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS,
    )


def get_system_intf_refs_can(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_CAN,
    )


def get_system_intf_refs_flex_ray(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_FLEX_RAY,
    )


def get_system_intf_refs_lin(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_LIN,
    )


def get_system_ver_build(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_BUILD,
    )


def get_system_ver_major(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_MAJOR,
    )


def get_system_ver_minor(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_MINOR,
    )


def get_system_ver_phase(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_PHASE,
    )


def get_system_ver_update(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_UPDATE,
    )


def get_system_intf_refs_all(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_ALL,
    )


def get_device_form_fac(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_FORM_FAC,
    )


def get_device_intf_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_DEV_INTF_REFS,
    )


def get_device_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_DEV_NAME,
    )


def get_device_num_ports(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_NUM_PORTS,
    )


def get_device_product_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_PRODUCT_NUM,
    )


def get_device_ser_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_SER_NUM,
    )


def get_device_slot_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_SLOT_NUM,
    )


def get_device_num_ports_all(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_NUM_PORTS_ALL,
    )


def get_device_intf_refs_all(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_DEV_INTF_REFS_ALL,
    )


def get_interface_dev_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_ref(
        ref,
        _cconsts.NX_PROP_INTF_DEV_REF,
    )


def get_interface_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_INTF_NAME,
    )


def get_interface_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_NUM,
    )


def get_interface_port_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_PORT_NUM,
    )


def get_interface_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_PROTOCOL,
    )


def get_interface_can_term_cap(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_CAN_TERM_CAP,
    )


def get_interface_can_tcvr_cap(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_CAN_TCVR_CAP,
    )


def get_interface_dongle_state(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_STATE,
    )


def get_interface_dongle_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_ID,
    )


def get_interface_dongle_revision(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_REVISION,
    )


def get_interface_dongle_firmware_version(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_FIRMWARE_VERSION,
    )


def get_interface_dongle_compatible_revision(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_COMPATIBLE_REVISION,
    )


def get_interface_dongle_compatible_firmware_version(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_COMPATIBLE_FIRMWARE_VERSION,
    )


def get_database_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_DATABASE_NAME,
    )


def get_database_clst_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_DATABASE_CLST_REFS,
    )


def get_database_show_invalid_from_open(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_DATABASE_SHOW_INVALID_FROM_OPEN,
    )


def set_database_show_invalid_from_open(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_DATABASE_SHOW_INVALID_FROM_OPEN,
        value,
    )


def get_cluster_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE,
    )


def set_cluster_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE,
        value,
    )


def get_cluster_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE64,
    )


def set_cluster_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE64,
        value,
    )


def get_cluster_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_CLST_COMMENT,
    )


def set_cluster_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_CLST_COMMENT,
        value,
    )


def get_cluster_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CONFIG_STATUS,
    )


def get_cluster_database_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_CLST_DATABASE_REF,
    )


def get_cluster_ecu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_ECU_REFS,
    )


def get_cluster_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_FRM_REFS,
    )


def get_cluster_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_CLST_NAME,
    )


def set_cluster_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_CLST_NAME,
        value,
    )


def get_cluster_pdu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_PDU_REFS,
    )


def get_cluster_pdus_reqd(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_PDUS_REQD,
    )


def get_cluster_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_PROTOCOL,
    )


def set_cluster_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_PROTOCOL,
        value,
    )


def get_cluster_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_SIG_REFS,
    )


def get_cluster_can_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_IO_MODE,
    )


def set_cluster_can_io_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_IO_MODE,
        value,
    )


def get_cluster_can_fd_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE,
    )


def set_cluster_can_fd_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE,
        value,
    )


def get_cluster_can_fd_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE64,
    )


def set_cluster_can_fd_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE64,
        value,
    )


def get_cluster_flex_ray_act_pt_off(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ACT_PT_OFF,
    )


def set_cluster_flex_ray_act_pt_off(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ACT_PT_OFF,
        value,
    )


def get_cluster_flex_ray_cas_rx_l_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CAS_RX_L_MAX,
    )


def set_cluster_flex_ray_cas_rx_l_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CAS_RX_L_MAX,
        value,
    )


def get_cluster_flex_ray_channels(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CHANNELS,
    )


def set_cluster_flex_ray_channels(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CHANNELS,
        value,
    )


def get_cluster_flex_ray_clst_drift_dmp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CLST_DRIFT_DMP,
    )


def set_cluster_flex_ray_clst_drift_dmp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CLST_DRIFT_DMP,
        value,
    )


def get_cluster_flex_ray_cold_st_ats(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_COLD_ST_ATS,
    )


def set_cluster_flex_ray_cold_st_ats(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_COLD_ST_ATS,
        value,
    )


def get_cluster_flex_ray_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CYCLE,
    )


def set_cluster_flex_ray_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CYCLE,
        value,
    )


def get_cluster_flex_ray_dyn_seg_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SEG_START,
    )


def get_cluster_flex_ray_dyn_slot_idl_ph(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SLOT_IDL_PH,
    )


def set_cluster_flex_ray_dyn_slot_idl_ph(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SLOT_IDL_PH,
        value,
    )


def get_cluster_flex_ray_latest_usable_dyn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LATEST_USABLE_DYN,
    )


def get_cluster_flex_ray_latest_guar_dyn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LATEST_GUAR_DYN,
    )


def get_cluster_flex_ray_lis_noise(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LIS_NOISE,
    )


def set_cluster_flex_ray_lis_noise(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LIS_NOISE,
        value,
    )


def get_cluster_flex_ray_macro_per_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACRO_PER_CYCLE,
    )


def set_cluster_flex_ray_macro_per_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACRO_PER_CYCLE,
        value,
    )


def get_cluster_flex_ray_macrotick(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACROTICK,
    )


def get_cluster_flex_ray_max_wo_clk_cor_fat(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT,
    )


def set_cluster_flex_ray_max_wo_clk_cor_fat(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT,
        value,
    )


def get_cluster_flex_ray_max_wo_clk_cor_pas(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS,
    )


def set_cluster_flex_ray_max_wo_clk_cor_pas(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS,
        value,
    )


def get_cluster_flex_ray_minislot_act_pt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT_ACT_PT,
    )


def set_cluster_flex_ray_minislot_act_pt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT_ACT_PT,
        value,
    )


def get_cluster_flex_ray_minislot(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT,
    )


def set_cluster_flex_ray_minislot(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT,
        value,
    )


def get_cluster_flex_ray_nm_vec_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NM_VEC_LEN,
    )


def set_cluster_flex_ray_nm_vec_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NM_VEC_LEN,
        value,
    )


def get_cluster_flex_ray_nit(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT,
    )


def set_cluster_flex_ray_nit(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT,
        value,
    )


def get_cluster_flex_ray_nit_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT_START,
    )


def get_cluster_flex_ray_num_minislt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_MINISLT,
    )


def set_cluster_flex_ray_num_minislt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_MINISLT,
        value,
    )


def get_cluster_flex_ray_num_stat_slt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_STAT_SLT,
    )


def set_cluster_flex_ray_num_stat_slt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_STAT_SLT,
        value,
    )


def get_cluster_flex_ray_off_cor_st(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_OFF_COR_ST,
    )


def set_cluster_flex_ray_off_cor_st(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_OFF_COR_ST,
        value,
    )


def get_cluster_flex_ray_payld_len_dyn_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX,
    )


def set_cluster_flex_ray_payld_len_dyn_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX,
        value,
    )


def get_cluster_flex_ray_payld_len_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_MAX,
    )


def get_cluster_flex_ray_payld_len_st(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_ST,
    )


def set_cluster_flex_ray_payld_len_st(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_ST,
        value,
    )


def get_cluster_flex_ray_stat_slot(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_STAT_SLOT,
    )


def set_cluster_flex_ray_stat_slot(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_STAT_SLOT,
        value,
    )


def get_cluster_flex_ray_sym_win(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN,
    )


def set_cluster_flex_ray_sym_win(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN,
        value,
    )


def get_cluster_flex_ray_sym_win_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN_START,
    )


def get_cluster_flex_ray_sync_node_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYNC_NODE_MAX,
    )


def set_cluster_flex_ray_sync_node_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYNC_NODE_MAX,
        value,
    )


def get_cluster_flex_ray_tss_tx(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_TSS_TX,
    )


def set_cluster_flex_ray_tss_tx(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_TSS_TX,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_idl(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_IDL,
    )


def set_cluster_flex_ray_wake_sym_rx_idl(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_IDL,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_low(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_LOW,
    )


def set_cluster_flex_ray_wake_sym_rx_low(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_LOW,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_win(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_WIN,
    )


def set_cluster_flex_ray_wake_sym_rx_win(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_WIN,
        value,
    )


def get_cluster_flex_ray_wake_sym_tx_idl(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_IDL,
    )


def set_cluster_flex_ray_wake_sym_tx_idl(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_IDL,
        value,
    )


def get_cluster_flex_ray_wake_sym_tx_low(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_LOW,
    )


def set_cluster_flex_ray_wake_sym_tx_low(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_LOW,
        value,
    )


def get_cluster_flex_ray_use_wakeup(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_USE_WAKEUP,
    )


def set_cluster_flex_ray_use_wakeup(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_USE_WAKEUP,
        value,
    )


def get_cluster_lin_schedules(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_LIN_SCHEDULES,
    )


def get_cluster_lin_tick(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_LIN_TICK,
    )


def set_cluster_lin_tick(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_LIN_TICK,
        value,
    )


def get_cluster_flex_ray_alw_pass_act(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ALW_PASS_ACT,
    )


def set_cluster_flex_ray_alw_pass_act(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ALW_PASS_ACT,
        value,
    )


def get_cluster_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_APPLICATION_PROTOCOL,
    )


def set_cluster_application_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_APPLICATION_PROTOCOL,
        value,
    )


def get_cluster_can_fd_iso_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_ISO_MODE,
    )


def get_frame_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_APPLICATION_PROTOCOL,
    )


def set_frame_application_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_APPLICATION_PROTOCOL,
        value,
    )


def get_frame_cluster_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_FRM_CLUSTER_REF,
    )


def get_frame_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_FRM_COMMENT,
    )


def set_frame_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_FRM_COMMENT,
        value,
    )


def get_frame_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CONFIG_STATUS,
    )


def get_frame_default_payload(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_FRM_DEFAULT_PAYLOAD,
    )


def set_frame_default_payload(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_FRM_DEFAULT_PAYLOAD,
        value,
    )


def get_frame_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_ID,
    )


def set_frame_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_ID,
        value,
    )


def get_frame_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_FRM_NAME,
    )


def set_frame_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_FRM_NAME,
        value,
    )


def get_frame_payload_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_PAYLOAD_LEN,
    )


def set_frame_payload_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_PAYLOAD_LEN,
        value,
    )


def get_frame_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_SIG_REFS,
    )


def get_frame_can_ext_id(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_CAN_EXT_ID,
    )


def set_frame_can_ext_id(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_CAN_EXT_ID,
        value,
    )


def get_frame_can_timing_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TIMING_TYPE,
    )


def set_frame_can_timing_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TIMING_TYPE,
        value,
    )


def get_frame_can_tx_time(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TX_TIME,
    )


def set_frame_can_tx_time(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TX_TIME,
        value,
    )


def get_frame_flex_ray_base_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_BASE_CYCLE,
    )


def set_frame_flex_ray_base_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_BASE_CYCLE,
        value,
    )


def get_frame_flex_ray_ch_assign(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CH_ASSIGN,
    )


def set_frame_flex_ray_ch_assign(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CH_ASSIGN,
        value,
    )


def get_frame_flex_ray_cycle_rep(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CYCLE_REP,
    )


def set_frame_flex_ray_cycle_rep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CYCLE_REP,
        value,
    )


def get_frame_flex_ray_preamble(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_PREAMBLE,
    )


def set_frame_flex_ray_preamble(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_PREAMBLE,
        value,
    )


def get_frame_flex_ray_startup(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_STARTUP,
    )


def set_frame_flex_ray_startup(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_STARTUP,
        value,
    )


def get_frame_flex_ray_sync(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_SYNC,
    )


def set_frame_flex_ray_sync(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_SYNC,
        value,
    )


def get_frame_flex_ray_timing_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_TIMING_TYPE,
    )


def set_frame_flex_ray_timing_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_TIMING_TYPE,
        value,
    )


def get_frame_flex_ray_in_cyc_rep_enabled(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_ENABLED,
    )


def get_frame_flex_ray_in_cyc_rep_i_ds(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_I_DS,
    )


def set_frame_flex_ray_in_cyc_rep_i_ds(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_I_DS,
        value,
    )


def get_frame_flex_ray_in_cyc_rep_ch_assigns(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS,
    )


def set_frame_flex_ray_in_cyc_rep_ch_assigns(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS,
        value,
    )


def get_frame_lin_checksum(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_LIN_CHECKSUM,
    )


def get_frame_mux_is_muxed(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_MUX_IS_MUXED,
    )


def get_frame_mux_data_mux_sig_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_FRM_MUX_DATA_MUX_SIG_REF,
    )


def get_frame_mux_static_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_MUX_STATIC_SIG_REFS,
    )


def get_frame_mux_subframe_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_MUX_SUBFRAME_REFS,
    )


def get_frame_pdu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_REFS,
    )


def set_frame_pdu_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_REFS,
        value,
    )


def get_frame_pdu_start_bits(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_START_BITS,
    )


def set_frame_pdu_start_bits(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_START_BITS,
        value,
    )


def get_frame_pdu_update_bits(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_UPDATE_BITS,
    )


def set_frame_pdu_update_bits(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_UPDATE_BITS,
        value,
    )


def get_frame_variable_payload(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_VARIABLE_PAYLOAD,
    )


def set_frame_variable_payload(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_VARIABLE_PAYLOAD,
        value,
    )


def get_frame_can_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CA_NIO_MODE,
    )


def set_frame_can_io_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CA_NIO_MODE,
        value,
    )


def get_pdu_cluster_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_PDU_CLUSTER_REF,
    )


def get_pdu_default_payload(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_PDU_DEFAULT_PAYLOAD,
    )


def set_pdu_default_payload(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_PDU_DEFAULT_PAYLOAD,
        value,
    )


def get_pdu_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_PDU_COMMENT,
    )


def set_pdu_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_PDU_COMMENT,
        value,
    )


def get_pdu_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_CONFIG_STATUS,
    )


def get_pdu_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_FRM_REFS,
    )


def get_pdu_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_PDU_NAME,
    )


def set_pdu_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_PDU_NAME,
        value,
    )


def get_pdu_payload_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_PAYLOAD_LEN,
    )


def set_pdu_payload_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_PAYLOAD_LEN,
        value,
    )


def get_pdu_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_SIG_REFS,
    )


def get_pdu_mux_is_muxed(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_PDU_MUX_IS_MUXED,
    )


def get_pdu_mux_data_mux_sig_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_PDU_MUX_DATA_MUX_SIG_REF,
    )


def get_pdu_mux_static_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_MUX_STATIC_SIG_REFS,
    )


def get_pdu_mux_subframe_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_MUX_SUBFRAME_REFS,
    )


def get_signal_byte_ordr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_BYTE_ORDR,
    )


def set_signal_byte_ordr(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_BYTE_ORDR,
        value,
    )


def get_signal_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_COMMENT,
    )


def set_signal_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_COMMENT,
        value,
    )


def get_signal_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_CONFIG_STATUS,
    )


def get_signal_data_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_DATA_TYPE,
    )


def set_signal_data_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_DATA_TYPE,
        value,
    )


def get_signal_default(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_DEFAULT,
    )


def set_signal_default(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_DEFAULT,
        value,
    )


def get_signal_frame_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_FRAME_REF,
    )


def get_signal_max(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MAX,
    )


def set_signal_max(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MAX,
        value,
    )


def get_signal_min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MIN,
    )


def set_signal_min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MIN,
        value,
    )


def get_signal_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME,
    )


def set_signal_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME,
        value,
    )


def get_signal_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME_UNIQUE_TO_CLUSTER,
    )


def get_signal_num_bits(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_NUM_BITS,
    )


def set_signal_num_bits(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_NUM_BITS,
        value,
    )


def get_signal_pdu_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_PDU_REF,
    )


def get_signal_scale_fac(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_FAC,
    )


def set_signal_scale_fac(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_FAC,
        value,
    )


def get_signal_scale_off(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_OFF,
    )


def set_signal_scale_off(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_OFF,
        value,
    )


def get_signal_start_bit(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_START_BIT,
    )


def set_signal_start_bit(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_START_BIT,
        value,
    )


def get_signal_unit(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_UNIT,
    )


def set_signal_unit(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_UNIT,
        value,
    )


def get_signal_mux_is_data_mux(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DATA_MUX,
    )


def set_signal_mux_is_data_mux(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DATA_MUX,
        value,
    )


def get_signal_mux_is_dynamic(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DYNAMIC,
    )


def get_signal_mux_value(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_MUX_VALUE,
    )


def get_signal_mux_subfrm_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_MUX_SUBFRM_REF,
    )


def get_subframe_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_CONFIG_STATUS,
    )


def get_subframe_dyn_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_SUBFRM_DYN_SIG_REFS,
    )


def get_subframe_frm_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SUBFRM_FRM_REF,
    )


def get_subframe_mux_value(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_MUX_VALUE,
    )


def set_subframe_mux_value(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_MUX_VALUE,
        value,
    )


def get_subframe_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME,
    )


def set_subframe_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME,
        value,
    )


def get_subframe_pdu_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SUBFRM_PDU_REF,
    )


def get_subframe_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME_UNIQUE_TO_CLUSTER,
    )


def get_ecu_clst_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_ECU_CLST_REF,
    )


def get_ecu_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_ECU_COMMENT,
    )


def set_ecu_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_ECU_COMMENT,
        value,
    )


def get_ecu_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_CONFIG_STATUS,
    )


def get_ecu_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_ECU_NAME,
    )


def set_ecu_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_ECU_NAME,
        value,
    )


def get_ecu_rx_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_RX_FRM_REFS,
    )


def set_ecu_rx_frm_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_RX_FRM_REFS,
        value,
    )


def get_ecu_tx_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_TX_FRM_REFS,
    )


def set_ecu_tx_frm_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_TX_FRM_REFS,
        value,
    )


def get_ecu_flex_ray_is_coldstart(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_IS_COLDSTART,
    )


def get_ecu_flex_ray_startup_frame_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_STARTUP_FRAME_REF,
    )


def get_ecu_flex_ray_wakeup_ptrn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_PTRN,
    )


def set_ecu_flex_ray_wakeup_ptrn(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_PTRN,
        value,
    )


def get_ecu_flex_ray_wakeup_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_CHS,
    )


def set_ecu_flex_ray_wakeup_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_CHS,
        value,
    )


def get_ecu_flex_ray_connected_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_CONNECTED_CHS,
    )


def set_ecu_flex_ray_connected_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_CONNECTED_CHS,
        value,
    )


def get_ecu_lin_master(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_LIN_MASTER,
    )


def set_ecu_lin_master(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_LIN_MASTER,
        value,
    )


def get_ecu_lin_protocol_ver(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_PROTOCOL_VER,
    )


def set_ecu_lin_protocol_ver(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_PROTOCOL_VER,
        value,
    )


def get_ecu_lin_initial_nad(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_INITIAL_NAD,
    )


def set_ecu_lin_initial_nad(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_INITIAL_NAD,
        value,
    )


def get_ecu_lin_config_nad(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_CONFIG_NAD,
    )


def set_ecu_lin_config_nad(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_CONFIG_NAD,
        value,
    )


def get_ecu_lin_supplier_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_SUPPLIER_ID,
    )


def set_ecu_lin_supplier_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_SUPPLIER_ID,
        value,
    )


def get_ecu_lin_function_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_FUNCTION_ID,
    )


def set_ecu_lin_function_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_FUNCTION_ID,
        value,
    )


def get_ecu_lin_p2_min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LIN_P2_MIN,
    )


def set_ecu_lin_p2_min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LIN_P2_MIN,
        value,
    )


def get_ecu_lin_st_min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LIN_ST_MIN,
    )


def set_ecu_lin_st_min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LIN_ST_MIN,
        value,
    )


def get_ecu_j1939_preferred_address(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_J1939_PREFERRED_ADDRESS,
    )


def set_ecu_j1939_preferred_address(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_J1939_PREFERRED_ADDRESS,
        value,
    )


def get_ecu_j1939_node_name(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_ECU_J1939_NODE_NAME,
    )


def set_ecu_j1939_node_name(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_ECU_J1939_NODE_NAME,
        value,
    )


def get_lin_sched_clst_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_CLST_REF,
    )


def get_lin_sched_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_COMMENT,
    )


def set_lin_sched_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_COMMENT,
        value,
    )


def get_lin_sched_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_CONFIG_STATUS,
    )


def get_lin_sched_entries(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRIES,
    )


def get_lin_sched_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_NAME,
    )


def set_lin_sched_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_NAME,
        value,
    )


def get_lin_sched_priority(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_PRIORITY,
    )


def set_lin_sched_priority(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_PRIORITY,
        value,
    )


def get_lin_sched_run_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_RUN_MODE,
    )


def set_lin_sched_run_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_RUN_MODE,
        value,
    )


def get_lin_sched_entry_collision_res_sched(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_COLLISION_RES_SCHED,
    )


def set_lin_sched_entry_collision_res_sched(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_COLLISION_RES_SCHED,
        value,
    )


def get_lin_sched_entry_delay(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_DELAY,
    )


def set_lin_sched_entry_delay(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_DELAY,
        value,
    )


def get_lin_sched_entry_event_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_EVENT_ID,
    )


def set_lin_sched_entry_event_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_EVENT_ID,
        value,
    )


def get_lin_sched_entry_frames(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_FRAMES,
    )


def set_lin_sched_entry_frames(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_FRAMES,
        value,
    )


def get_lin_sched_entry_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME,
    )


def set_lin_sched_entry_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME,
        value,
    )


def get_lin_sched_entry_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME_UNIQUE_TO_CLUSTER,
    )


def get_lin_sched_entry_sched(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_SCHED,
    )


def get_lin_sched_entry_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_TYPE,
    )


def set_lin_sched_entry_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_TYPE,
        value,
    )


def get_lin_sched_entry_nc_ff_data_bytes(
    ref,  # type: int
):
    # type: (...) -> typing.Iterable[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NC_FF_DATA_BYTES,
    )


def set_lin_sched_entry_nc_ff_data_bytes(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NC_FF_DATA_BYTES,
        value,
    )
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/__init__.py sha256=885578b14ece4b16a82737da9035f4501a448bc6fd234c3a94d95d5cca159499 bytes=82 -->
## FILE: nixnet/_session/__init__.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/__init__.py`
- sha256: `885578b14ece4b16a82737da9035f4501a448bc6fd234c3a94d95d5cca159499`
- bytes: 82

````python
import typing  # NOQA: F401

__all__ = []  # type: typing.List[typing.Text]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/base.py sha256=e6f701df44dc52aadc64ed54a18c650184d550707eb04e91e2a29354b0b7fe48 bytes=32705 -->
## FILE: nixnet/_session/base.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/base.py`
- sha256: `e6f701df44dc52aadc64ed54a18c650184d550707eb04e91e2a29354b0b7fe48`
- bytes: 32705

````python
import ctypes  # type: ignore
import typing  # NOQA: F401
import warnings

from nixnet import _ctypedefs
from nixnet import _errors
from nixnet import _funcs
from nixnet import _props
from nixnet import _utils
from nixnet import constants
from nixnet import errors
from nixnet import types  # NOQA: F401

from nixnet._session import intf as session_intf
from nixnet._session import j1939 as session_j1939


class SessionBase(object):
    """Session base object."""

    def __init__(
            self,
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            list,  # type: typing.Text
            interface_name,  # type: typing.Text
            mode,  # type: constants.CreateSessionMode
    ):
        # type: (...) -> None
        """Create an XNET session at run time using named references to database objects.

        This function creates a session using the named database objects
        specified in 'list' from the database named in 'database_name'.

        This function is intended to be used by session classes that derive from
        SessionBase; therefore, it is not public.

        Args:
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the list parameter; this is
                not allowed for modes of 'constants.CreateSessionMode.FRAME_IN_STREAM'
                or 'constants.CreateSessionMode.FRAME_OUT_STREAM'.
            list: A list of strings describing signals or frames for the session.
                The list syntax depends on the mode. Refer to mode spefic
                session classes defined below for 'list' syntax.
            interface_name: A string representing the XNET Interface to use for
                this session. If Mode is
                'constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT',
                this input is ignored. You can set it to an empty string.
            mode: The session mode. See :any:`nixnet._enums.CreateSessionMode`.

        Returns:
            A session base object.
        """
        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(database_name, cluster_name, list, interface_name, mode)
        self._intf = session_intf.Interface(self._handle)
        self._j1939 = session_j1939.J1939(self._handle)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(SessionBase, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def close(self):
        # type: () -> None
        """Close (clear) the XNET session.

        This function stops communication for the session and releases all
        resources the session uses. It internally calls
        :any:`nixnet._session.base.SessionBase.stop` with normal scope, so if
        this is the last session using the interface, communication stops.

        You typically use 'close' when you need to close the existing session to
        create a new session that uses the same objects. For example, if you
        create a session for a frame named frame_a using Frame Output
        Single-Point mode, then you create a second session for frame_a using
        Frame Output Queued mode, the second call to the session constructor
        returns an error, because frame_a can be accessed using only one output
        mode. If you call 'close' before the second constructor call, you can
        close the previous use of frame_a to create the new session.
        """
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    def start(self, scope=constants.StartStopScope.NORMAL):
        # type: (constants.StartStopScope) -> None
        """Start communication for the XNET session.

        Because the session is started automatically by default, this function
        is optional. This function is for more advanced applications to start
        multiple sessions in a specific order. For more information about the
        automatic start feature, refer to the
        :any:`nixnet._session.base.SessionBase.auto_start` property.

        For each physical interface, the NI-XNET hardware is divided into two logical units:

            Sessions: You can create one or more sessions, each of which contains
            frames or signals to be transmitted (or received) on the bus.

            Interface: The interface physically connects to the bus and transmits
            (or receives) data for the sessions.

        You can start each logical unit separately. When a session is started,
        all contained frames or signals are placed in a state where they are
        ready to communicate. When the interface is started, it takes data from
        all started sessions to communicate with other nodes on the bus. For a
        specification of the state models for the session and interface, refer
        to State Models.

        If an output session starts before you write data, or you read an input
        session before it receives a frame, default data is used. For more
        information, refer to the XNET Frame Default Payload and XNET Signal
        Default Value properties.

        Args:
            scope(:any:`nixnet._enums.StartStopScope`): Describes the impact of
                this operation on the underlying state models for the session
                and its interface.
        """
        _funcs.nx_start(self._handle, scope)  # type: ignore

    def stop(self, scope=constants.StartStopScope.NORMAL):
        # type: (constants.StartStopScope) -> None
        """Stop communication for the XNET session.

        Because the session is stopped automatically when closed (cleared),
        this function is optional.

        For each physical interface, the NI-XNET hardware is divided into two logical units:

            Sessions: You can create one or more sessions, each of which contains
            frames or signals to be transmitted (or received) on the bus.

            Interface: The interface physically connects to the bus and transmits
            (or receives) data for the sessions.

        You can stop each logical unit separately. When a session is stopped,
        all contained frames or signals are placed in a state where they are no
        longer ready to communicate. When the interface is stopped, it no longer
        takes data from sessions to communicate with other nodes on the bus. For
        a specification of the state models for the session and interface, refer
        to State Models.

        Args:
            scope(:any:`nixnet._enums.StartStopScope`): Describes the impact of
                this operation on the underlying state models for the session
                and its interface.
        """
        _funcs.nx_stop(self._handle, scope)  # type: ignore

    def flush(self):
        # type: () -> None
        """Flushes (empties) all XNET session queues.

        With the exception of single-point modes, all sessions use queues to
        store frames. For input modes, the queues store frame values (or
        corresponding signal values) that have been received, but not obtained
        by calling the read function. For output sessions, the queues store
        frame values provided to write function, but not transmitted successfully.

        :any:`nixnet._session.base.SessionBase.start` and
        :any:`nixnet._session.base.SessionBase.stop` have no effect on these
        queues. Use 'flush' to discard all values in the session's queues.

        For example, if you call a write function to write three frames, then
        immediately call :any:`nixnet._session.base.SessionBase.stop`, then
        call :any:`nixnet._session.base.SessionBase.start` a few seconds
        later, the three frames transmit. If you call 'flush' between
        :any:`nixnet._session.base.SessionBase.stop` and
        :any:`nixnet._session.base.SessionBase.start`, no frames transmit.

        As another example, if you receive three frames, then call
        :any:`nixnet._session.base.SessionBase.stop`, the three frames remains
        in the queue. If you call :any:`nixnet._session.base.SessionBase.start`
        a few seconds later, then call a read function, you obtain the three
        frames received earlier, potentially followed by other frames received
        after calling :any:`nixnet._session.base.SessionBase.start`. If you
        call 'flush' between :any:`nixnet._session.base.SessionBase.stop` and
        :any:`nixnet._session.base.SessionBase.start`, read function returns
        only frames received after the calling
        :any:`nixnet._session.base.SessionBase.start`.
        """
        _funcs.nx_flush(self._handle)  # type: ignore

    def wait_for_transmit_complete(self, timeout=10):
        # type: (float) -> None
        """Wait for transmition to complete.

        All frames written for the session have been transmitted on the bus.
        This condition applies to CAN, LIN, and FlexRay. This condition is state
        based, and the state is Boolean (true/false).

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(
            self._handle,  # type: ignore
            constants.Condition.TRANSMIT_COMPLETE,
            0,
            timeout)

    def wait_for_intf_communicating(self, timeout=10):
        # type: (float) -> None
        """Wait for the interface to begin communication on the network.

        If a start trigger is configured for the interface, this first waits for
        the trigger. Once the interface is started, this waits for the
        protocol's communication state to transition to a value that indicates
        communication with remote nodes.

        After this wait succeeds, calls to 'read_state' will return:

            :any:`nixnet._enums.CanCommState`: 'constants.CAN_COMM.ERROR_ACTIVE'

            :any:`nixnet._enums.CanCommState`: 'constants.CAN_COMM.ERROR_PASSIVE'

            'constants.ReadState.TIME_COMMUNICATING': Valid time for
            communication (invalid time of 0 prior)

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(
            self._handle,  # type: ignore
            constants.Condition.INTF_COMMUNICATING,
            0,
            timeout)

    def wait_for_intf_remote_wakeup(self, timeout=10):
        # type: (float) -> None
        """Wait for interface remote wakeup.

        Wait for the interface to wakeup due to activity by a remote node on the
        network. This wait is used for CAN, when you set the 'can_tcvr_state'
        property to 'constants.CanTcvrState.SLEEP'. Although the interface
        itself is ready to communicate, this places the transceiver into a sleep
        state. When a remote CAN node transmits a frame, the transceiver wakes
        up, and communication is restored. This wait detects that remote wakeup.

        This wait is used for LIN when you set 'lin_sleep' property to
        'constants.LinSleep.REMOTE_SLEEP' or 'constants.LinSleep.LOCAL_SLEEP'.
        When asleep, if a remote LIN ECU transmits the wakeup pattern (break),
        the XNET LIN interface detects this transmission and wakes up. This wait
        detects that remote wakeup.

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(
            self._handle,  # type: ignore
            constants.Condition.INTF_REMOTE_WAKEUP,
            0,
            timeout)

    def connect_terminals(self, source, destination):
        # type: (typing.Text, typing.Text) -> None
        """Connect terminals on the XNET interface.

        This function connects a source terminal to a destination terminal on
        the interface hardware. The XNET terminal represents an external or
        internal hardware connection point on a National Instruments XNET
        hardware product. External terminals include PXI Trigger lines for a PXI
        card, RTSI terminals for a PCI card, or the single external terminal for
        a C Series module. Internal terminals include timebases (clocks) and
        logical entities such as a start trigger.

        The terminal inputs use the Terminal I/O names. Typically, one of the
        pair is an internal and the other an external.

        Args:
            source(str): Connection source name.
            destination(str): Connection destination name.
        """
        _funcs.nx_connect_terminals(self._handle, source, destination)  # type: ignore

    def disconnect_terminals(self, source, destination):
        # type: (typing.Text, typing.Text) -> None
        """Disconnect terminals on the XNET interface.

        This function disconnects a specific pair of source/destination terminals
        previously connected with :any:`nixnet._session.base.SessionBase.connect_terminals`.

        When the final session for a given interface is cleared, NI-XNET
        automatically disconnects all terminal connections for that interface.
        Therefore, 'disconnect_terminals' is not required for most applications.

        This function typically is used to change terminal connections
        dynamically while an application is running. To disconnect a terminal,
        you first must stop the interface using
        :any:`nixnet._session.base.SessionBase.stop` with the Interface Only
        scope. Then you can call 'disconnect_terminals' and
        :any:`nixnet._session.base.SessionBase.connect_terminals` to adjust
        terminal connections. Finally, you can call
        :any:`nixnet._session.base.SessionBase.start` with the Interface Only
        scope to restart the interface.

        You can disconnect only a terminal that has been previously connected.
        Attempting to disconnect a nonconnected terminal results in an error.

        Args:
            source(str): Connection source name.
            destination(str): Connection destination name.
        """
        _funcs.nx_disconnect_terminals(self._handle, source, destination)  # type: ignore

    def change_lin_schedule(self, sched_index):
        # type: (int) -> None
        """Writes communication states of an XNET session.

        This function writes a request for the LIN interface to change
        the running schedule.

        According to the LIN protocol, only the master executes schedules,
        not slaves. If the
        :any:`nixnet._session.intf.Interface.lin_master` property is false (slave),
        this write function implicitly sets that property to true (master). If the
        interface currently is running as a slave, this write returns an error,
        because it cannot change to master while running.

        Args:
            sched_index(int): Index to the schedule table that the LIN master executes.

                The schedule tables are sorted the way they are returned from the
                database with the `nixnet.database._cluster.Cluster.lin_schedules`
                property.
        """
        _funcs.nx_write_state(
            self._handle,  # type: ignore
            constants.WriteState.LIN_SCHEDULE_CHANGE,
            _ctypedefs.u32(sched_index))

    def change_lin_diagnostic_schedule(self, schedule):
        # type: (constants.LinDiagnosticSchedule) -> None
        """Writes communication states of an XNET session.

        This function writes a request for the LIN interface to change
        the diagnostic schedule.

        Args:
            schedule(:any:`nixnet._enums.LinDiagnosticSchedule`): Diagnostic schedule
                that the LIN master executes.
        """
        _funcs.nx_write_state(
            self._handle,  # type: ignore
            constants.WriteState.LIN_DIAGNOSTIC_SCHEDULE_CHANGE,
            _ctypedefs.u32(schedule.value))

    @property
    def time_current(self):
        # type: () -> int
        """int: Current interface time."""
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.TIME_CURRENT,
            state_size,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        return time

    @property
    def time_start(self):
        # type: () -> int
        """int: Time the interface was started."""
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.TIME_START,
            state_size,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        if time == 0:
            # The interface is not communicating.
            _errors.check_for_error(constants.Err.SESSION_NOT_STARTED.value)
        return time

    @property
    def time_communicating(self):
        # type: () -> int
        """int: Time the interface started communicating.

        The time is usually later than ``time_start`` because the interface
        must undergo a communication startup procedure.
        """
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.TIME_COMMUNICATING,
            state_size,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        if time == 0:
            # The interface is not communicating.
            _errors.check_for_error(constants.Err.SESSION_NOT_STARTED.value)
        return time

    @property
    def state(self):
        # type: () -> constants.SessionInfoState
        """:any:`nixnet._enums.SessionInfoState`: Session running state."""
        state_value_ctypes = _ctypedefs.u32()
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.SESSION_INFO,
            state_size,
            ctypes.pointer(state_value_ctypes))
        state = state_value_ctypes.value
        return constants.SessionInfoState(state)

    @property
    def can_comm(self):
        # type: () -> types.CanComm
        """:any:`nixnet.types.CanComm`: CAN Communication state"""
        state_value_ctypes = _ctypedefs.u32()
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.CAN_COMM,
            state_size,
            ctypes.pointer(state_value_ctypes))
        bitfield = state_value_ctypes.value
        return _utils.parse_can_comm_bitfield(bitfield)

    @property
    def lin_comm(self):
        # type: () -> types.LinComm
        """:any:`nixnet.types.LinComm`: LIN Communication state"""
        state_value_ctypes = (_ctypedefs.u32 * 2)()  # type: ignore
        state_size = ctypes.sizeof(state_value_ctypes)
        _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.LIN_COMM,
            state_size,
            ctypes.pointer(state_value_ctypes))
        first = state_value_ctypes[0].value
        second = state_value_ctypes[1].value
        return _utils.parse_lin_comm_bitfield(first, second)

    def check_fault(self):
        # type: () -> None
        """Check for an asynchronous fault.

        A fault is an error that occurs asynchronously to the NI-XNET
        application calls. The fault cause may be related to network
        communication, but it also can be related to XNET hardware, such as a
        fault in the onboard processor. Although faults are extremely rare,
        nxReadState provides a detection method distinct from the status of
        NI-XNET function calls, yet easy to use alongside the common practice
        of checking the communication state.
        """
        state_value_ctypes = _ctypedefs.u32()
        state_size = ctypes.sizeof(state_value_ctypes)
        fault = _funcs.nx_read_state(
            self._handle,  # type: ignore
            constants.ReadState.SESSION_INFO,
            state_size,
            ctypes.pointer(state_value_ctypes))
        _errors.check_for_error(fault)

    @property
    def intf(self):
        # type: () -> session_intf.Interface
        """:any:`nixnet._session.intf.Interface`: Returns the Interface configuration object for the session."""
        return self._intf

    @property
    def j1939(self):
        # type: () -> session_j1939.J1939
        """:any:`nixnet._session.j1939.J1939`: Returns the J1939 configuration object for the session."""
        return self._j1939

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`nixnet._enums.AppProtocol`: This property returns the application protocol that the session uses.

        The database used with the session determines the application protocol.
        """
        return constants.AppProtocol(
            _props.get_session_application_protocol(self._handle))  # type: ignore

    @property
    def auto_start(self):
        # type: () -> bool
        """bool: Automatically starts the output session on the first call to the appropriate write function.

        For input sessions, start always is performed within the first call to
        the appropriate read function (if not already started using
        :any:`nixnet._session.base.SessionBase.start`). This is done
        because there is no known use case for reading a stopped input session.

        For output sessions, as long as the first call to the appropriate write
        function contains valid data, you can leave this property at its default
        value of true. If you need to call the appropriate write function
        multiple times prior to starting the session, or if you are starting
        multiple sessions simultaneously, you can set this property to false.
        After calling the appropriate write function as desired, you can call
        :any:`nixnet._session.base.SessionBase.start` to start the session(s).

        When automatic start is performed, it is equivalent to
        :any:`nixnet._session.base.SessionBase.start` with scope set to Normal.
        This starts the session itself, and if the interface is not already
        started, it starts the interface also.
        """
        return _props.get_session_auto_start(self._handle)  # type: ignore

    @auto_start.setter
    def auto_start(self, value):
        # type: (bool) -> None
        _props.set_session_auto_start(self._handle, value)  # type: ignore

    @property
    def cluster_name(self):
        # type: () -> typing.Text
        """str: This property returns the cluster (network) name used with the session."""
        return _props.get_session_cluster_name(self._handle)  # type: ignore

    @property
    def database_name(self):
        # type: () -> typing.Text
        """str: This property returns the database name used with the session."""
        return _props.get_session_database_name(self._handle)  # type: ignore

    @property
    def mode(self):
        # type: () -> constants.CreateSessionMode
        """:any:`nixnet._enums.CreateSessionMode`: This property returns the mode associated with the session.

        For more information, refer to :any:`nixnet._enums.CreateSessionMode`.
        """
        return constants.CreateSessionMode(
            _props.get_session_mode(self._handle))  # type: ignore

    @property
    def num_pend(self):
        # type: () -> int
        """int: This property returns the number of values (frames or signals) pending for the session.

        For input sessions, this is the number of frame/signal values available
        to the appropriate read function. If you call the appropriate read
        function with number to read of this number and timeout of 0.0, the
        appropriate read function should return this number of values successfully.

        For output sessions, this is the number of frames/signal values provided
        to the appropriate write function but not yet transmitted onto the network.

        Stream frame sessions using FlexRay or CAN FD protocol may use a
        variable size of frames. In these cases, this property assumes the
        largest possible frame size. If you use smaller frames, the real number
        of pending values might be higher.

        The largest possible frames sizes are:

            CAN FD: 64 byte payload.

            FlexRay: The higher value of the frame size in the static segment
            and the maximum frame size in the dynamic segment. The XNET Cluster
            FlexRay Payload Length Maximum property provides this value.
        """
        return _props.get_session_num_pend(self._handle)  # type: ignore

    @property
    def num_unused(self):
        # type: () -> int
        """int: This property returns the number of values (frames or signals) unused for the session.

        If you get this property prior to starting the session, it provides the
        size of the underlying queue(s). Contrary to the Queue Size property,
        this value is in number of frames for Frame I/O, not number of bytes;
        for Signal I/O, it is the number of signal values in both cases. After
        start, this property returns the queue size minus the
        :any:`Number of Values Pending <nixnet._session.base.SessionBase.num_pend>`
        property.

        For input sessions, this is the number of frame/signal values unused in
        the underlying queue(s).

        For output sessions, this is the number of frame/signal values you can
        provide to a subsequent call to the appropriate write function. If you
        call the appropriate write function with this number of values and
        timeout of 0.0, it should return success.

        Stream frame sessions using FlexRay or CAN FD protocol may use a
        variable size of frames. In these cases, this property assumes the
        largest possible frame size. If you use smaller frames, the real number
        of pending values might be higher.

        The largest possible frames sizes are:

            CAN FD: 64 byte payload.

            FlexRay: The higher value of the frame size in the static segment
            and the maximum frame size in the dynamic segment. The XNET Cluster
            FlexRay Payload Length Maximum property provides this value.
        """
        return _props.get_session_num_unused(self._handle)  # type: ignore

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`nixnet._enums.Protocol`: This property returns the protocol that the interface in the session uses."""
        return constants.Protocol(
            _props.get_session_protocol(self._handle))  # type: ignore

    @property
    def queue_size(self):
        # type: () -> int
        """int: Get or set queue size.

        For output sessions, queues store data passed to the appropriate
        write function and not yet transmitted onto the network. For input
        sessions, queues store data received from the network and not yet
        obtained using the appropriate read function.

        For most applications, the default queue sizes are sufficient. You can
        write to this property to override the default. When you write (set)
        this property, you must do so prior to the first session start. You
        cannot set this property again after calling
        :any:`nixnet._session.base.SessionBase.stop`.

        For signal I/O sessions, this property is the number of signal values
        stored. This is analogous to the number of values you use with the
        appropriate read or write function.

        For frame I/O sessions, this property is the number of bytes of frame
        data stored.

        For standard CAN or LIN frame I/O sessions, each frame uses exactly 24
        bytes. You can use this number to convert the Queue Size (in bytes)
        to/from the number of frame values.

        For CAN FD and FlexRay frame I/O sessions, each frame value size can
        vary depending on the payload length. For more information, refer to
        Raw Frame Format.

        For Signal I/O XY sessions, you can use signals from more than one frame.
        Within the implementation, each frame uses a dedicated queue. According
        to the formulas below, the default queue sizes can be different for each
        frame. If you read the default Queue Size property for a Signal Input XY
        session, the largest queue size is returned, so that a call to the
        appropriate read function of that size can empty all queues. If you
        read the default Queue Size property for a Signal Output XY session, the
        smallest queue size is returned, so that a call to the appropriate write
        function of that size can succeed when all queues are empty. If you
        write the Queue Size property for a Signal I/O XY session, that size is
        used for all frames, so you must ensure that it is sufficient for the
        frame with the fastest transmit time.

        For Signal I/O Waveform sessions, you can use signals from more than one
        frame. Within the implementation, each frame uses a dedicated queue. The
        Queue Size property does not represent the memory in these queues, but
        rather the amount of time stored. The default queue allocations store
        Application Time worth of resampled signal values. If you read the
        default Queue Size property for a Signal I/O Waveform session, it
        returns Application Time multiplied by the time Resample Rate. If you
        write the Queue Size property for a Signal I/O Waveform session, that
        value is translated from a number of samples to a time, and that time is
        used to allocate memory for each queue.

        For Single-Point sessions (signal or frame), this property is ignored.
        Single-Point sessions always use a value of 1 as the effective queue size.
        """
        return _props.get_session_queue_size(self._handle)  # type: ignore

    @queue_size.setter
    def queue_size(self, value):
        # type: (int) -> None
        _props.set_session_queue_size(self._handle, value)  # type: ignore
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/collection.py sha256=5dffcf2ca377dfee98cd25779af570a17af69b1a1e6b412004365c91061ef48b bytes=4619 -->
## FILE: nixnet/_session/collection.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/collection.py`
- sha256: `5dffcf2ca377dfee98cd25779af570a17af69b1a1e6b412004365c91061ef48b`
- bytes: 4619

````python
import abc
from collections.abc import Sequence
import typing  # NOQA: F401

import six

from nixnet import _props


@six.add_metaclass(abc.ABCMeta)
class Collection(Sequence):
    """Collection of items in a session."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self.__list_cache = None  # type: typing.Optional[typing.List[typing.Text]]

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __len__(self):
        # type: () -> int
        return _props.get_session_num_in_list(self._handle)

    def __iter__(self):
        item_count = len(self)
        item_names = self._list_cache
        assert item_count == len(item_names), \
            "Frame count ({}) is out of sync with items ({})".format(item_count, item_names)
        for index, name in enumerate(item_names):
            yield self._create_item(self._handle, index, name)

    def __contains__(self, index):
        if isinstance(index, six.integer_types):
            return 0 <= index and index < len(self._list_cache)
        elif isinstance(index, six.string_types):
            name = index
            return name in self._list_cache
        else:
            raise TypeError(index)

    def __getitem__(self, index):
        if isinstance(index, six.integer_types):
            name = self._list_cache[index]
        elif isinstance(index, six.string_types):
            name = index
            item_names = self._list_cache
            try:
                index = item_names.index(name)
            except ValueError:
                raise KeyError(name)
        else:
            raise TypeError(index)

        return self._create_item(self._handle, index, name)

    def get(self, index, default=None):
        # type: (typing.Union[int, typing.Text], typing.Any) -> Item
        """Access an item, returning ``default`` on failure.

        Args:
            index(str or int): Item name or index
            default: Value to return when lookup fails
        """
        if isinstance(index, six.integer_types):
            try:
                name = self._list_cache[index]
            except IndexError:
                return default
        elif isinstance(index, six.string_types):
            name = index
            item_names = self._list_cache
            try:
                index = item_names.index(name)
            except ValueError:
                return default
        else:
            raise TypeError(index)

        return self._create_item(self._handle, index, name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_collection = typing.cast(Collection, other)
            return (
                self._handle == other_collection._handle
                and self._list_cache == other_collection._list_cache
            )
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    @property
    def _list_cache(self):
        # type: () -> typing.List[typing.Text]
        if self.__list_cache is None:
            self.__list_cache = list(_props.get_session_list(self._handle))
        return self.__list_cache

    @abc.abstractmethod
    def _create_item(self, handle, index, name):
        # type: (int, int, typing.Text) -> Item
        pass


class Item(object):
    """Item configuration for a session."""

    def __init__(self, handle, index, name):
        # type: (int, int, typing.Text) -> None
        self._handle = handle
        self._index = index
        self._name = name

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_item = typing.cast(Item, other)
            return (
                self._handle == other_item._handle
                and self._index == other_item._index
            )
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __int__(self):
        # type: () -> int
        return self._index

    def __str__(self):
        # type: () -> typing.Text
        return self._name
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/frames.py sha256=f9558a4c3bb534d582d5bf46beca1d3c52fc4f8f125c412bdfe0c019a3e87cf7 bytes=16409 -->
## FILE: nixnet/_session/frames.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/frames.py`
- sha256: `f9558a4c3bb534d582d5bf46beca1d3c52fc4f8f125c412bdfe0c019a3e87cf7`
- bytes: 16409

````python
import itertools
import typing  # NOQA: F401

from nixnet import _frames
from nixnet import _funcs
from nixnet import _props
from nixnet._session import collection
from nixnet import constants
from nixnet import types


class Frames(collection.Collection):
    """Frames in a session."""

    def _create_item(self, handle, index, name):
        return Frame(handle, index, name)

    @property
    def payld_len_max(self):
        # type: () -> int
        """int: Returns the maximum payload length of all frames in this session, expressed as bytes (0-254).

        For CAN Stream (Input and Output), this property depends on the XNET
        Cluster CAN I/O Mode property. If the I/O mode is
        `constants.CanIoMode.CAN`, this property is 8 bytes. If the I/O mode is
        'constants.CanIoMode.CAN_FD' or 'constants.CanIoMode.CAN_FD_BRS', this
        property is 64 bytes.

        For LIN Stream (Input and Output), this property always is 8 bytes.

        For FlexRay Stream (Input and Output), this property is the same as the
        XNET Cluster FlexRay Payload Length Maximum property value.

        For Queued and Single-Point (Input and Output), this is the maximum
        payload of all frames specified in the List property.
        """
        return _props.get_session_payld_len_max(self._handle)


class InFrames(Frames):
    """Frames in a session."""

    def read_bytes(
            self,
            num_bytes,
            timeout=constants.TIMEOUT_NONE):
        # type: (int, float) -> bytes
        """Read data as a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            num_bytes(int): The number of bytes to read.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                To avoid returning a partial frame, even when
                'num_bytes' are available from the hardware, this
                read may return fewer bytes in buffer. For example, assume you
                pass 'num_bytes' 70 bytes and 'timeout' of 10
                seconds. During the read, two frames are received, the first 24
                bytes in size, and the second 56 bytes in size, for a total of
                80 bytes. The read returns after the two frames are received,
                but only the first frame is copied to data. If the read copied
                46 bytes of the second frame (up to the limit of 70), that frame
                would be incomplete and therefore difficult to interpret. To
                avoid this problem, the read always returns complete frames in
                buffer.

                If 'timeout' is positive, this function waits for
                'num_bytes' frame bytes to be received, then
                returns complete frames up to that number. If the bytes do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this
                function waits indefinitely for 'num_bytes' frame bytes.

                If 'timeout' is 'constants.TIMEOUT_NONE', this
                function does not wait and immediately returns all available
                frame bytes up to the limit 'num_bytes' specifies.

        Returns:
            A list of raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(self._handle, num_bytes, timeout)
        return buffer[0:number_of_bytes_returned]

    def read(
            self,
            num_frames,
            timeout=constants.TIMEOUT_NONE,
            frame_type=types.XnetFrame):
        # type: (int, float, typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Read frames.

        Args:
            num_frames(int): Number of frames to read.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits for
                'num_frames' frames to be received, then
                returns complete frames up to that number. If the frames do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this function
                waits indefinitely for 'num_frames' frames.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns all available frames up to the
                limit 'num_frames' specifies.
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # NOTE: If the frame payload exceeds the base unit, this will return
        # less than num_frames
        num_bytes = num_frames * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(num_bytes, timeout)
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)


class SinglePointInFrames(Frames):
    """Frames in a session."""

    def read_bytes(
            self,
            num_bytes):
        # type: (int) -> bytes
        """Read data as a list of raw bytes (frame data).

        Args:
            num_bytes(int): Number of bytes to read.

        Returns:
            bytes: Raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(
            self._handle,
            num_bytes,
            constants.TIMEOUT_NONE)
        return buffer[0:number_of_bytes_returned]

    def read(
            self,
            frame_type=types.XnetFrame):
        # type: (typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Read frames.

        Args:
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # NOTE: If the frame payload exceeds the base unit, this will return
        # less than num_frames
        num_frames = len(self)
        num_bytes = num_frames * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(num_bytes)
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)


class OutFrames(Frames):
    """Frames in a session."""

    def write_bytes(
            self,
            frame_bytes,
            timeout=10):
        # type: (bytes, float) -> None
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes(bytes): Frames to transmit.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits up to that 'timeout'
                for space to become available in queues. If the space is not
                available prior to the 'timeout', a 'timeout' error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this functions
                waits indefinitely for space to become available in queues.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns with a 'timeout' error if all data
                cannot be queued. Regardless of the 'timeout' used, if a 'timeout'
                error occurs, none of the data is queued, so you can attempt to
                call this function again at a later time with the same data.
        """
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), timeout)

    def write(
            self,
            frames,
            timeout=10):
        # type: (typing.Iterable[types.Frame], float) -> None
        """Write frame data.

        Args:
            frames(list of float): One or more :any:`nixnet.types.Frame` objects to be
                written to the session.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits up to that 'timeout'
                for space to become available in queues. If the space is not
                available prior to the 'timeout', a 'timeout' error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this functions
                waits indefinitely for space to become available in queues.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns with a 'timeout' error if all data
                cannot be queued. Regardless of the 'timeout' used, if a 'timeout'
                error occurs, none of the data is queued, so you can attempt to
                call this function again at a later time with the same data.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        self.write_bytes(bytes, timeout)


class SinglePointOutFrames(Frames):
    """Frames in a session."""

    def write_bytes(
            self,
            frame_bytes):
        # type: (bytes) -> None
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes(bytes): Frames to transmit.
        """
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), constants.TIMEOUT_NONE)

    def write(
            self,
            frames):
        # type: (typing.Iterable[types.Frame]) -> None
        """Write frame data.

        Args:
            frames(list of float): One or more :any:`nixnet.types.Frame` objects to be
                written to the session.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        self.write_bytes(bytes)


class Frame(collection.Item):
    """Frame configuration for a session."""

    def set_can_start_time_off(self, offset):
        # type: (float) -> None
        """Set CAN Start Time Offset.

        Use this function to have more control over the schedule of frames on
        the bus, to offer more determinism by configuring cyclic frames to be
        spaced evenly.

        If you do not call this function or you set it to a negative number,
        NI-XNET chooses this start time offset based on the arbitration
        identifier and periodic transmit time.

        ``offset`` takes effect whenever a session is started. If you stop a
        session and restart it, the start time offset is re-evaluated.

        Args:
            offset(float): The amount of time that must elapse between the
                session being started and the time that the first frame is
                transmitted across the bus. This is different than the cyclic
                rate, which determines the time between subsequent frame
                transmissions.
        """
        _props.set_session_can_start_time_off(self._handle, self._index, offset)

    def set_can_tx_time(self, time):
        # type: (float) -> None
        """Set CAN Transmit Time.

        If you call this function while a frame object is currently started, the
        frame object is stopped, the cyclic rate updated, and then the frame
        object is restarted. Because of the stopping and starting, the frame's
        start time offset is re-evaluated.

        The first time a queued frame object is started, the XNET frame's
        transmit time determines the object's default queue size. Changing this
        rate has no impact on the queue size. Depending on how you change the
        rate, the queue may not be sufficient to store data for an extended
        period of time. You can mitigate this by setting the session Queue Size
        property to provide sufficient storage for all rates you use. If you are
        using a single-point session, this is not relevant.

        Args:
            time(float): Frame's transmit time while the session is running.
                The transmit time is the amount of time that must elapse
                between subsequent transmissions of a cyclic frame. The default
                value of this property comes from the database (the XNET Frame
                CAN Transmit Time property).
        """
        _props.set_session_can_tx_time(self._handle, self._index, time)

    def set_skip_n_cyclic_frames(self, n):
        # type: (int) -> None
        """Set Skip N Cyclic Frames

        When the frame's transmission time arrives and the skip count is
        nonzero, a frame value is dequeued (if this is not a single-point
        session), and the skip count is decremented, but the frame actually is
        not transmitted across the bus. When the skip count decrements to zero,
        subsequent cyclic transmissions resume.

        This function is useful for testing of ECU behavior when a cyclic frame
        is expected, but is missing for N cycles.

        .. note:: Only CAN interfaces currently support this function.

        .. note:: This property is valid only for output sessions and frames
            with cyclic timing (that is, not event-based frames).

        Args:
            n(int): Skip the next N cyclic frames when nonzero.
        """
        _props.set_session_skip_n_cyclic_frames(self._handle, self._index, n)

    def set_lin_tx_n_corrupted_chksums(self, n):
        # type: (int) -> None
        """Set LIN Transmit N Corrupted Checksums.

        When set to a nonzero value, this function causes the next N number of
        checksums to be corrupted. The checksum is corrupted by negating the
        value calculated per the database; (EnhancedValue * -1) or
        (ClassicValue * -1).

        If the frame is transmitted in an unconditional or sporadic schedule
        slot, N is always decremented for each frame transmission. If the frame
        is transmitted in an event-triggered slot and a collision occurs, N is
        not decremented. In that case, N is decremented only when the collision
        resolving schedule is executed and the frame is successfully
        transmitted.  If the frame is the only one to transmit in the
        event-triggered slot (no collision), N is decremented at
        event-triggered slot time.

        This function is useful for testing ECU behavior when a corrupted
        checksum is transmitted.

        .. note:: This function is valid only for output sessions.

        Args:
            n(int): Number of checksums to be corrupted.
        """
        _props.set_session_lin_tx_n_corrupted_chksums(self._handle, self._index, n)

    def set_j1939_addr_filter(self, address=""):
        # type: (typing.Union[typing.Text, int]) -> None
        """Set J1939 Address Filter.

        Define a filter for the source address of the PGN transmitting node.
        You can use it when multiple nodes with different addresses are
        transmitting the same PGN.

        If the filter is active, the session accepts only frames transmitted by
        a node with the defined address. All other frames with the same PGN but
        transmitted by other nodes are ignored.

        .. note:: You can use this function in input sessions only.

        Args:
            address(str or int): Decimal value of the address. Leave blank to
                reset the filter.
        """
        _props.set_session_j1939_addr_filter(self._handle, self._index, str(address))
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/intf.py sha256=e96db29c106f7f785c0fb5225eb19130dbe6a1b26b5ad3321981fb986a7ad563 bytes=44363 -->
## FILE: nixnet/_session/intf.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/intf.py`
- sha256: `e96db29c106f7f785c0fb5225eb19130dbe6a1b26b5ad3321981fb986a7ad563`
- bytes: 44363

````python
import typing  # NOQA: F401

import six

from nixnet import _props
from nixnet import constants
from nixnet.database import _frame


class Interface(object):
    '''Interface configuration for a session'''

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __str__(self):
        return self._name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        elif isinstance(other, six.string_types):
            return self._name == other
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    @property
    def baud_rate(self):
        # type: () -> int
        '''int: CAN, FlexRay, or LIN interface baud rate.

        The default value for this interface property is the same as the
        cluster's baud rate in the database. Your application can set this
        interface baud rate to override the value in the database, or when no
        database is used.

        **CAN**

        When the upper nibble (0xF0000000) is clear, this is a numeric baud
        rate (for example, 500000).

        NI-XNET CAN hardware currently accepts the following numeric baud
        rates: 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000,
        160000, 200000, 250000, 400000, 500000, 800000, and 1000000.

        **LIN**

        When the upper nibble (0xF0000000) is clear, you can set only baud
        rates within the LIN-specified range (2400 to 20000) for the interface.
        '''
        return _props.get_session_intf_baud_rate64(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
        # type: (int) -> None
        _props.set_session_intf_baud_rate64(self._handle, value)

    @property
    def bus_err_to_in_strm(self):
        # type: () -> bool
        '''bool: Bus Error Frames to Input Stream?

        Specifies whether the hardware should place a CAN or LIN bus error
        frame into the Stream Input queue after it is generated.
        '''
        return _props.get_session_intf_bus_err_to_in_strm(self._handle)

    @bus_err_to_in_strm.setter
    def bus_err_to_in_strm(self, value):
        # type: (bool) -> None
        _props.set_session_intf_bus_err_to_in_strm(self._handle, value)

    @property
    def echo_tx(self):
        # type: () -> bool
        '''bool: Echo Transmit?

        Determines whether Frame Input or Signal Input sessions contain frames
        that the interface transmits.

        When this property is true, and a frame transmit is complete for an
        Output session, the frame is echoed to the Input session. Frame Input
        sessions can use the Flags field to differentiate frames received from
        the bus and frames the interface transmits. When reading frames with
        the :any:`nixnet.types.RawFrame`, you can parse the Flags field
        manually by reviewing the Raw Frame Format section. Signal Input
        sessions cannot differentiate the origin of the incoming data.

        .. note:: Echoed frames are placed into the input sessions only after
           the frame transmit is complete. If there are bus problems (for
           example, no listener) such that the frame did not transmit, the
           frame is not received.
        '''
        return _props.get_session_intf_echo_tx(self._handle)

    @echo_tx.setter
    def echo_tx(self, value):
        # type: (bool) -> None
        _props.set_session_intf_echo_tx(self._handle, value)

    @property
    def out_strm_list(self):
        # type: () -> typing.Iterable[_frame.Frame]
        '''Output Stream List.

        The Output Stream List property provides a list of frames for use with
        the replay feature (:any:`out_strm_timng` property set to
        :any:`OutStrmTimng` ``REPLAY_EXCLUSIVE`` or ``REPLAY_INCLUSIVE``). In
        Replay Exclusive mode, the hardware transmits only frames that do not
        appear in the list. In Replay Inclusive mode, the hardware transmits
        only frames that appear in the list. For a LIN interface, the header of
        each frame written to stream output is transmitted, and the Exclusive
        or Inclusive mode controls the response transmission. Using these
        modes, you can either emulate an ECU (Replay Inclusive, where the list
        contains the frames the ECU transmits) or test an ECU (Replay
        Exclusive, where the list contains the frames the ECU transmits), or
        some other combination.

        This property's data type is an array of database handles to frames. If
        you are not using a database file or prefer to specify the frames using
        CAN arbitration IDs or LIN unprotected IDs, you can use
        Interface:Output Stream List By ID instead of this property.

        .. note:: Only CAN and LIN interfaces currently support this property.
        '''
        for ref in _props.get_session_intf_out_strm_list(self._handle):
            yield _frame.Frame(_handle=ref)

    @out_strm_list.setter
    def out_strm_list(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        frame_handles = [frame._handle for frame in value]
        _props.set_session_intf_out_strm_list(self._handle, frame_handles)

    @property
    def out_strm_list_by_id(self):
        # type: () -> typing.Iterable[int]
        '''int: Output Stream List by Frame Identifier.

        Provide a list of frames for use with the replay feature
        Interface:Output Stream Timing property.

        This property serves the same purpose as Interface:Output Stream List,
        in that it provides a list of frames for replay filtering. This
        property provides an alternate format for you to specify the frames by
        their CAN arbitration ID or LIN unprotected ID. The property's data
        type is an array of integers. Each integer represents a CAN or LIN
        frame's identifier, using the same encoding as :any:`nixnet.types.RawFrame`.

        For CAN Frames, see :any:`nixnet.types.CanIdentifier` for parsing and
        generating raw identifiers.

        LIN frame ID values may be within the range of possible LIN
        IDs (0-63).

        See also :any:`Interface.out_strm_list`.
        '''
        for id in _props.get_session_intf_can_out_strm_list_by_id(self._handle):
            yield id

    @out_strm_list_by_id.setter
    def out_strm_list_by_id(self, value):
        # type: (typing.Iterable[int]) -> None
        _props.set_session_intf_can_out_strm_list_by_id(self._handle, list(value))

    @property
    def out_strm_timng(self):
        # type: () -> constants.OutStrmTimng
        ''':any:`nixnet._enums.OutStrmTimng`: Output Stream Timing.

        The Output Stream Timing property configures how the hardware transmits
        frames queued using a Frame Output Stream session.

        See also :any:`Interface.out_strm_list`.

        .. note:: Only CAN and LIN interfaces currently support this property.
        '''
        return constants.OutStrmTimng(_props.get_session_intf_out_strm_timng(self._handle))

    @out_strm_timng.setter
    def out_strm_timng(self, value):
        # type: (constants.OutStrmTimng) -> None
        _props.set_session_intf_out_strm_timng(self._handle, value.value)

    @property
    def start_trig_to_in_strm(self):
        # type: () -> bool
        '''bool: Start Trigger Frames to Input Stream?

        Configures the hardware to place a start trigger frame into the Stream
        Input queue after it is generated. A Start Trigger frame is generated
        when the interface is started.

        The start trigger frame is especially useful if you plan to log and
        replay CAN data.
        '''
        return _props.get_session_intf_start_trig_to_in_strm(self._handle)

    @start_trig_to_in_strm.setter
    def start_trig_to_in_strm(self, value):
        # type: (bool) -> None
        _props.set_session_intf_start_trig_to_in_strm(self._handle, value)

    def set_can_ext_tcvr_config(self, value):
        # type: (int) -> None
        '''Configure XS series CAN hardware to communicate properly with your external transceiver.

        Args:
            value(int): Bitfield
        '''
        _props.set_session_intf_can_ext_tcvr_config(self._handle, value)

    @property
    def can_lstn_only(self):
        # type: () -> bool
        '''bool:  Listen Only? property configures whether the CAN interface transmits any information to the CAN bus.

        When this property is false, the interface can transmit CAN frames and
        acknowledge received CAN frames.

        When this property is true, the interface can neither transmit CAN
        frames nor acknowledge a received CAN frame. The true value enables
        passive monitoring of network traffic, which can be useful for
        debugging scenarios when you do not want to interfere with a
        communicating network cluster.
        '''
        return _props.get_session_intf_can_lstn_only(self._handle)

    @can_lstn_only.setter
    def can_lstn_only(self, value):
        # type: (bool) -> None
        _props.set_session_intf_can_lstn_only(self._handle, value)

    @property
    def can_pend_tx_order(self):
        # type: () -> constants.CanPendTxOrder
        ''':any:`nixnet._enums.CanPendTxOrder`: Pending Transmit Order

        The Pending Transmit Order property configures how the CAN interface
        manages the internal queue of frames. More than one frame may desire to
        transmit at the same time. NI-XNET stores the frames in an internal
        queue and transmits them onto the CAN bus when the bus is idle.

        .. note:: You can modify this property only when the interface is
           stopped.
        .. note:: Setting this property causes the internal queue to be flushed.
           If you start a session, queue frames, and then stop the session and
           change this mode, some frames may be lost. Set this property to the
           desired value once; do not constantly change modes.
        '''
        return constants.CanPendTxOrder(_props.get_session_intf_can_pend_tx_order(self._handle))

    @can_pend_tx_order.setter
    def can_pend_tx_order(self, value):
        # type: (constants.CanPendTxOrder) -> None
        _props.set_session_intf_can_pend_tx_order(self._handle, value.value)

    @property
    def can_sing_shot(self):
        # type: () -> bool
        '''bool: Single Shot Transmit?

        The Single Shot Transmit? property configures whether the CAN interface
        retries failed transmissions.

        When this property is false, failed transmissions retry as specified by
        the CAN protocol (ISO 11898-1, 6.11 Automatic Retransmission). If a CAN
        frame is not transmitted successfully, the interface attempts to
        retransmit the frame as soon as the bus is idle again. This retransmit
        process continues until the frame is successfully transmitted.

        When this property is true, failed transmissions do not retry. If a CAN
        frame is not transmitted successfully, no further transmissions are
        attempted.

        .. note:: You can modify this property only when the interface is
           stopped.
        .. note:: Setting this property causes the internal queue to be flushed.
           If you start a session, queue frames, and then stop the session and
           change this mode, some frames may be lost. Set this property to the
           desired value once; do not constantly change modes.
        '''
        return _props.get_session_intf_can_sing_shot(self._handle)

    @can_sing_shot.setter
    def can_sing_shot(self, value):
        # type: (bool) -> None
        _props.set_session_intf_can_sing_shot(self._handle, value)

    @property
    def can_term(self):
        # type: () -> constants.CanTerm
        ''':any:`nixnet._enums.CanTerm`: CAN Termination.

        The Termination property configures the onboard termination of the
        NI-XNET interface CAN connector (port). The enumeration is generic and
        supports two values: Off and On. However, different CAN hardware has
        different termination requirements, and the Off and On values have
        different meanings, see :any:`nixnet._enums.CanTerm`.

        .. note:: You can modify this property only when the interface is
           stopped.
        .. note:: This property does not take effect until the interface is
           started.
        '''
        return constants.CanTerm(_props.get_session_intf_can_term(self._handle))

    @can_term.setter
    def can_term(self, value):
        # type: (constants.CanTerm) -> None
        _props.set_session_intf_can_term(self._handle, value.value)

    @property
    def can_tcvr_state(self):
        # type: () -> constants.CanTcvrState
        ''':any:`nixnet._enums.CanTcvrState`: CAN Transceiver State.

        The Transceiver State property configures the CAN transceiver and CAN
        controller modes. The transceiver state controls whether the
        transceiver is asleep or communicating, as well as configuring other
        special modes.
        '''
        return constants.CanTcvrState(_props.get_session_intf_can_tcvr_state(self._handle))

    @can_tcvr_state.setter
    def can_tcvr_state(self, value):
        # type: (constants.CanTcvrState) -> None
        _props.set_session_intf_can_tcvr_state(self._handle, value.value)

    @property
    def can_tcvr_type(self):
        # type: () -> constants.CanTcvrType
        ''':any:`nixnet._enums.CanTcvrType`: CAN Transceiver Type.

        For XNET hardware that provides a software-selectable transceiver, the
        Transceiver Type property allows you to set the transceiver type. Use
        the XNET Interface CAN.Tranceiver Capability property to determine
        whether your hardware supports a software-selectable transceiver.

        The default value for this property depends on your type of hardware.
        If you have fixed-personality hardware, the default value is the
        hardware value. If you have hardware that supports software-selectable
        transceivers, the default is High-Speed.
        '''
        return constants.CanTcvrType(_props.get_session_intf_can_tcvr_type(self._handle))

    @can_tcvr_type.setter
    def can_tcvr_type(self, value):
        # type: (constants.CanTcvrType) -> None
        _props.set_session_intf_can_tcvr_type(self._handle, value.value)

    @property
    def can_io_mode(self):
        # type: () -> constants.CanIoMode
        ''':any:`nixnet._enums.CanIoMode`: CAN IO Mode.

        This property indicates the I/O Mode the interface is using.

        The value is initialized from the database cluster when the session is
        created and cannot be changed later. However, you can transmit standard
        CAN frames on a CAN FD network.
        '''
        return constants.CanIoMode(_props.get_session_intf_can_io_mode(self._handle))

    @property
    def can_fd_baud_rate(self):
        # type: () -> int
        '''int: The fast data baud rate for :any:`can_io_mode` of :any:`nixnet._enums.CanIoMode` ``CAN_FD_BRS``

        The default value for this interface property is the same as the
        cluster's FD baud rate in the database. Your application can set this
        interface FD baud rate to override the value in the database.

        When the upper nibble (0xF0000000) is clear, this is a numeric baud
        rate (for example, 500000).

        NI-XNET CAN hardware currently accepts the following numeric baud
        rates: 200000, 250000, 400000, 500000, 800000, 1000000, 1250000,
        1600000, 2000000, 2500000, 4000000, 5000000, and 8000000.

        .. note:: Not all CAN transceivers are rated to transmit at the requested
           rate. If you attempt to use a rate that exceeds the transceiver's
           qualified rate, XNET Start returns a warning. NI-XNET Hardware
           Overview describes the CAN transceivers' limitations.
        '''
        return _props.get_session_intf_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        # type: (int) -> None
        _props.set_session_intf_can_fd_baud_rate64(self._handle, value)

    @property
    def can_tx_io_mode(self):
        # type: () -> constants.CanIoMode
        ''':any:`nixnet._enums.CanIoMode`: CAN Transmit IO Mode

        This property specifies the I/O Mode the interface uses when
        transmitting a CAN frame. By default, it is the same as the XNET
        Cluster CAN:I/O Mode property. However, even if the interface is in CAN
        FD+BRS mode, you can force it to transmit frames in the standard CAN
        format. For this purpose, set this property to CAN.

        The Transmit I/O mode may not exceed the mode set by the XNET Cluster
        CAN:I/O Mode property.

        .. note:: This property is not supported in CAN FD+BRS ISO mode. If you
           are using ISO CAN FD mode, you define the transmit I/O mode in the
           database with the I/O Mode property of the frame. (When a database
           is not used (for example, in frame stream mode), define the transmit
           I/O mode with the frame type field of the frame data.) Note that ISO
           CAN FD mode is the default mode for CAN FD in NI-XNET.
        .. note:: This property affects only the transmission of frames. Even if
           you set the transmit I/O mode to CAN, the interface still can
           receive frames in FD modes (if the XNET Cluster CAN:I/O Mode
           property is configured in an FD mode).
        '''
        return constants.CanIoMode(_props.get_session_intf_can_tx_io_mode(self._handle))

    @can_tx_io_mode.setter
    def can_tx_io_mode(self, value):
        # type: (constants.CanIoMode) -> None
        _props.set_session_intf_can_tx_io_mode(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        # type: () -> constants.CanFdIsoMode
        ''':any:`nixnet._enums.CanFdIsoMode`: CAN FS ISO Mode.

        This property is valid only when the interface is in CAN FD(+BRS) mode.
        It specifies whether the interface is working in the ISO CAN FD
        standard (ISO standard 11898-1:2015) or non-ISO CAN FD standard (Bosch
        CAN FD 1.0 specification). Two ports using different standards (ISO CAN
        FD vs. non-ISO CAN FD) cannot communicate with each other.

        When you use a CAN FD database (DBC or FIBEX file created with
        NI-XNET), you can specify the ISO CAN FD mode when creating an alias
        name for the database. An alias is created automatically when you open
        a new database in the NI-XNET Database Editor. The specified ISO CAN FD
        mode is used as default, which you can change in the session using this
        property.
        '''
        return constants.CanFdIsoMode(_props.get_session_intf_can_fd_iso_mode(self._handle))

    @can_fd_iso_mode.setter
    def can_fd_iso_mode(self, value):
        # type: (constants.CanFdIsoMode) -> None
        _props.set_session_intf_can_fd_iso_mode(self._handle, value.value)

    @property
    def can_edge_filter(self):
        # type: () -> bool
        '''bool: CAN Enable Edge Filter.

        When this property is enabled, the CAN hardware requires two
        consecutive dominant tq for hard synchronization.
        '''
        return _props.get_session_intf_can_edge_filter(self._handle)

    @can_edge_filter.setter
    def can_edge_filter(self, value):
        # type: (bool) -> None
        _props.set_session_intf_can_edge_filter(self._handle, value)

    @property
    def can_transmit_pause(self):
        # type: () -> bool
        '''bool: CAN Transmit Pause.

        When this property is enabled, the CAN hardware waits for two bit times
        before transmitting the next frame. This allows other CAN nodes to
        transmit lower priority CAN messages while this CAN node is
        transmitting high-priority CAN messages with high speed.
        '''
        return _props.get_session_intf_can_transmit_pause(self._handle)

    @can_transmit_pause.setter
    def can_transmit_pause(self, value):
        # type: (bool) -> None
        _props.set_session_intf_can_transmit_pause(self._handle, value)

    @property
    def can_disable_prot_exception_handling(self):
        # type: () -> bool
        '''bool: CAN Disable Protocol Exception Handling.

        A protocol exception occurs when the CAN hardware detects an invalid
        combination of bits on the CAN bus reserved for a future protocol
        expansion. NI-XNET allows you to define how the hardware should behave
        in case of a protocol exception:

        False (default): the CAN hardware stops receiving frames and starts a bus integration.

        True: the CAN hardware transmits an error frame when it detects a
        protocol exception condition.
        '''
        return _props.get_session_intf_can_disable_prot_exception_handling(self._handle)

    @can_disable_prot_exception_handling.setter
    def can_disable_prot_exception_handling(self, value):
        # type: (bool) -> None
        _props.set_session_intf_can_disable_prot_exception_handling(self._handle, value)

    @property
    def flex_ray_acc_start_rng(self):
        return _props.get_session_intf_flex_ray_acc_start_rng(self._handle)

    @flex_ray_acc_start_rng.setter
    def flex_ray_acc_start_rng(self, value):
        _props.set_session_intf_flex_ray_acc_start_rng(self._handle, value)

    @property
    def flex_ray_alw_hlt_clk(self):
        return _props.get_session_intf_flex_ray_alw_hlt_clk(self._handle)

    @flex_ray_alw_hlt_clk.setter
    def flex_ray_alw_hlt_clk(self, value):
        _props.set_session_intf_flex_ray_alw_hlt_clk(self._handle, value)

    @property
    def flex_ray_alw_pass_act(self):
        return _props.get_session_intf_flex_ray_alw_pass_act(self._handle)

    @flex_ray_alw_pass_act.setter
    def flex_ray_alw_pass_act(self, value):
        _props.set_session_intf_flex_ray_alw_pass_act(self._handle, value)

    @property
    def flex_ray_auto_aslp_whn_stp(self):
        return _props.get_session_intf_flex_ray_auto_aslp_whn_stp(self._handle)

    @flex_ray_auto_aslp_whn_stp.setter
    def flex_ray_auto_aslp_whn_stp(self, value):
        _props.set_session_intf_flex_ray_auto_aslp_whn_stp(self._handle, value)

    @property
    def flex_ray_clst_drift_dmp(self):
        return _props.get_session_intf_flex_ray_clst_drift_dmp(self._handle)

    @flex_ray_clst_drift_dmp.setter
    def flex_ray_clst_drift_dmp(self, value):
        _props.set_session_intf_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def flex_ray_coldstart(self):
        return _props.get_session_intf_flex_ray_coldstart(self._handle)

    @property
    def flex_ray_dec_corr(self):
        return _props.get_session_intf_flex_ray_dec_corr(self._handle)

    @flex_ray_dec_corr.setter
    def flex_ray_dec_corr(self, value):
        _props.set_session_intf_flex_ray_dec_corr(self._handle, value)

    @property
    def flex_ray_delay_comp_a(self):
        return _props.get_session_intf_flex_ray_delay_comp_a(self._handle)

    @flex_ray_delay_comp_a.setter
    def flex_ray_delay_comp_a(self, value):
        _props.set_session_intf_flex_ray_delay_comp_a(self._handle, value)

    @property
    def flex_ray_delay_comp_b(self):
        return _props.get_session_intf_flex_ray_delay_comp_b(self._handle)

    @flex_ray_delay_comp_b.setter
    def flex_ray_delay_comp_b(self, value):
        _props.set_session_intf_flex_ray_delay_comp_b(self._handle, value)

    @property
    def flex_ray_key_slot_id(self):
        return _props.get_session_intf_flex_ray_key_slot_id(self._handle)

    @flex_ray_key_slot_id.setter
    def flex_ray_key_slot_id(self, value):
        _props.set_session_intf_flex_ray_key_slot_id(self._handle, value)

    @property
    def flex_ray_latest_tx(self):
        return _props.get_session_intf_flex_ray_latest_tx(self._handle)

    @property
    def flex_ray_list_timo(self):
        return _props.get_session_intf_flex_ray_list_timo(self._handle)

    @flex_ray_list_timo.setter
    def flex_ray_list_timo(self, value):
        _props.set_session_intf_flex_ray_list_timo(self._handle, value)

    @property
    def flex_ray_mac_init_off_a(self):
        return _props.get_session_intf_flex_ray_mac_init_off_a(self._handle)

    @flex_ray_mac_init_off_a.setter
    def flex_ray_mac_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_a(self._handle, value)

    @property
    def flex_ray_mac_init_off_b(self):
        return _props.get_session_intf_flex_ray_mac_init_off_b(self._handle)

    @flex_ray_mac_init_off_b.setter
    def flex_ray_mac_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_b(self._handle, value)

    @property
    def flex_ray_mic_init_off_a(self):
        return _props.get_session_intf_flex_ray_mic_init_off_a(self._handle)

    @flex_ray_mic_init_off_a.setter
    def flex_ray_mic_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_a(self._handle, value)

    @property
    def flex_ray_mic_init_off_b(self):
        return _props.get_session_intf_flex_ray_mic_init_off_b(self._handle)

    @flex_ray_mic_init_off_b.setter
    def flex_ray_mic_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_b(self._handle, value)

    @property
    def flex_ray_max_drift(self):
        return _props.get_session_intf_flex_ray_max_drift(self._handle)

    @flex_ray_max_drift.setter
    def flex_ray_max_drift(self, value):
        _props.set_session_intf_flex_ray_max_drift(self._handle, value)

    @property
    def flex_ray_microtick(self):
        return _props.get_session_intf_flex_ray_microtick(self._handle)

    @property
    def flex_ray_null_to_in_strm(self):
        return _props.get_session_intf_flex_ray_null_to_in_strm(self._handle)

    @flex_ray_null_to_in_strm.setter
    def flex_ray_null_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_null_to_in_strm(self._handle, value)

    @property
    def flex_ray_off_corr(self):
        return _props.get_session_intf_flex_ray_off_corr(self._handle)

    @property
    def flex_ray_off_corr_out(self):
        return _props.get_session_intf_flex_ray_off_corr_out(self._handle)

    @flex_ray_off_corr_out.setter
    def flex_ray_off_corr_out(self, value):
        _props.set_session_intf_flex_ray_off_corr_out(self._handle, value)

    @property
    def flex_ray_rate_corr(self):
        return _props.get_session_intf_flex_ray_rate_corr(self._handle)

    @property
    def flex_ray_rate_corr_out(self):
        return _props.get_session_intf_flex_ray_rate_corr_out(self._handle)

    @flex_ray_rate_corr_out.setter
    def flex_ray_rate_corr_out(self, value):
        _props.set_session_intf_flex_ray_rate_corr_out(self._handle, value)

    @property
    def flex_ray_samp_per_micro(self):
        return _props.get_session_intf_flex_ray_samp_per_micro(self._handle)

    @flex_ray_samp_per_micro.setter
    def flex_ray_samp_per_micro(self, value):
        _props.set_session_intf_flex_ray_samp_per_micro(self._handle, value)

    @property
    def flex_ray_sing_slot_en(self):
        return _props.get_session_intf_flex_ray_sing_slot_en(self._handle)

    @flex_ray_sing_slot_en.setter
    def flex_ray_sing_slot_en(self, value):
        _props.set_session_intf_flex_ray_sing_slot_en(self._handle, value)

    @property
    def flex_ray_statistics_en(self):
        return _props.get_session_intf_flex_ray_statistics_en(self._handle)

    @flex_ray_statistics_en.setter
    def flex_ray_statistics_en(self, value):
        _props.set_session_intf_flex_ray_statistics_en(self._handle, value)

    @property
    def flex_ray_sym_to_in_strm(self):
        return _props.get_session_intf_flex_ray_sym_to_in_strm(self._handle)

    @flex_ray_sym_to_in_strm.setter
    def flex_ray_sym_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_sym_to_in_strm(self._handle, value)

    @property
    def flex_ray_sync_ch_a_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_even(self._handle)

    @property
    def flex_ray_sync_ch_a_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_odd(self._handle)

    @property
    def flex_ray_sync_ch_b_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_even(self._handle)

    @property
    def flex_ray_sync_ch_b_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_odd(self._handle)

    @property
    def flex_ray_sync_status(self):
        return _props.get_session_intf_flex_ray_sync_status(self._handle)

    @property
    def flex_ray_term(self):
        return _props.get_session_intf_flex_ray_term(self._handle)

    @flex_ray_term.setter
    def flex_ray_term(self, value):
        _props.set_session_intf_flex_ray_term(self._handle, value)

    @property
    def flex_ray_wakeup_ch(self):
        return _props.get_session_intf_flex_ray_wakeup_ch(self._handle)

    @flex_ray_wakeup_ch.setter
    def flex_ray_wakeup_ch(self, value):
        _props.set_session_intf_flex_ray_wakeup_ch(self._handle, value)

    @property
    def flex_ray_wakeup_ptrn(self):
        return _props.get_session_intf_flex_ray_wakeup_ptrn(self._handle)

    @flex_ray_wakeup_ptrn.setter
    def flex_ray_wakeup_ptrn(self, value):
        _props.set_session_intf_flex_ray_wakeup_ptrn(self._handle, value)

    def set_flex_ray_sleep(self, value):
        _props.set_session_intf_flex_ray_sleep(self._handle, value)

    @property
    def flex_ray_connected_chs(self):
        return _props.get_session_intf_flex_ray_connected_chs(self._handle)

    @flex_ray_connected_chs.setter
    def flex_ray_connected_chs(self, value):
        _props.set_session_intf_flex_ray_connected_chs(self._handle, value)

    @property
    def lin_break_length(self):
        # type: () -> int
        '''int: LIN Break Length

        The length of the serial break used at the start of a frame header
        (schedule entry). The value is specified in bit-times.

        The valid range is 10-36 (inclusive). The default value is 13, which is
        the value the LIN standard specifies.

        At baud rates below 9600, the upper limit may be lower than 36 to avoid
        violating hold times for the bus. For example, at 2400 baud, the valid
        range is 10-14.

        .. note:: This property is applicable only when the interface is the
           master.
        '''
        return _props.get_session_intf_lin_break_length(self._handle)

    @lin_break_length.setter
    def lin_break_length(self, value):
        # type: (int) -> None
        _props.set_session_intf_lin_break_length(self._handle, value)

    @property
    def lin_master(self):
        # type: () -> bool
        '''bool: LIN Master?

        Specifies the NI-XNET LIN interface role on the network: master (true)
        or slave (false).

        In a LIN network (cluster), there always is a single ECU in the system
        called the master. The master transmits a schedule of frame headers.
        Each frame header is a remote request for a specific frame ID. For each
        header, typically a single ECU in the network (slave) responds by
        transmitting the requested ID payload. The master ECU can respond to a
        specific header as well, and thus the master can transmit payload data
        for the slave ECUs to receive.

        The default value for this property is false (slave). This means that
        by default, the interface does not transmit frame headers onto the
        network. When you use input sessions, you read frames that other ECUs
        transmit. When you use output sessions, the NI-XNET interface waits for
        the remote master to send a header for a frame in the output sessions,
        then the interface responds with data for the requested frame.

        If you call the :any:`nixnet._session.base.SessionBase.change_lin_schedule` function to request execution of a
        schedule, that implicitly sets this property to true (master). You also
        can set this property to true using, but no schedule is active by
        default, so you still must call the
        :any:`nixnet._session.base.SessionBase.change_lin_schedule` function at some
        point to request a specific schedule.

        Regardless of this property's value, you use can input and output
        sessions. This property specifies which hardware transmits the
        scheduled frame headers: NI-XNET (true) or a remote master ECU (false).
        '''
        return _props.get_session_intf_lin_master(self._handle)

    @lin_master.setter
    def lin_master(self, value):
        # type: (bool) -> None
        _props.set_session_intf_lin_master(self._handle, value)

    @property
    def lin_sched_names(self):
        # type: () -> typing.Iterable[typing.Text]
        '''list of str: LIN Schedule Names

        List of schedules for use when the NI-XNET LIN interface acts as a
        master (``lin_master`` is true). When the interface is master, you can
        pass the index of one of these schedules to the
        :any:`nixnet._session.base.SessionBase.change_lin_schedule` function to request
        a schedule change.

        This list of schedules is the same as ``Cluster.lin_schedules`` used to
        configure the session.
        '''
        return _props.get_session_intf_lin_sched_names(self._handle)

    def set_lin_sleep(self, state):
        # type: (constants.LinSleep) -> None
        '''Set LIN Sleep State

        Use the Sleep property to change the NI-XNET LIN interface sleep/awake
        state and optionally to change remote node (ECU) sleep/awake states.

        .. note:: Setting a new value is effectively a request, and the
           function returns before the request is complete.  To detect the
           current interface sleep/wake state, use
           :any:`nixnet._session.base.SessionBase.lin_comm`.

        Args:
            state(:any:`nixnet._enums.LinSleep`): Desired state.
        '''
        _props.set_session_intf_lin_sleep(self._handle, state.value)

    @property
    def lin_term(self):
        # type: () -> constants.LinTerm
        ''':any:`nixnet._enums.LinTerm`: LIN Termination

        The Termination property configures the NI-XNET interface LIN connector
        (port) onboard termination. The enumeration is generic and supports two
        values: Off (disabled) and On (enabled).

        Per the LIN 2.1 standard, the Master ECU has a ~1 kOhm termination
        resistor between Vbat and Vbus. Therefore, use this property only if
        you are using your interface as the master and do not already have
        external termination.

        .. note:: You can modify this property only when the interface is
           stopped.
        .. note:: This property does not take effect until the interface is
           started.
        '''
        return constants.LinTerm(_props.get_session_intf_lin_term(self._handle))

    @lin_term.setter
    def lin_term(self, value):
        # type: (constants.LinTerm) -> None
        _props.set_session_intf_lin_term(self._handle, value.value)

    @property
    def lin_diag_p2min(self):
        # type: () -> float
        '''float: LIN Diag P2min

        This is the minimum time in seconds between reception of the last frame
        of the diagnostic request message and transmission of the response for
        the first frame in the diagnostic response message by the slave.

        .. note:: This property applies only to the interface as slave.
        '''
        return _props.get_session_intf_lin_diag_p2min(self._handle)

    @lin_diag_p2min.setter
    def lin_diag_p2min(self, value):
        # type: (float) -> None
        _props.set_session_intf_lin_diag_p2min(self._handle, value)

    @property
    def lin_diag_stmin(self):
        # type: () -> float
        '''float: LIN Diag STmin

        master:
            The minimum time in seconds the interface places between the end of
            transmission of a frame in a diagnostic request message and the
            start of transmission of the next frame in the diagnostic request
            message.
        slave:
            The minimum time in seconds the interface places between the end of
            transmission of a frame in a diagnostic response message and the
            start of transmission of the response for the next frame in the
            diagnostic response message.
        '''
        return _props.get_session_intf_lin_diag_stmin(self._handle)

    @lin_diag_stmin.setter
    def lin_diag_stmin(self, value):
        # type: (float) -> None
        _props.set_session_intf_lin_diag_stmin(self._handle, value)

    @property
    def lin_alw_start_wo_bus_pwr(self):
        # type: () -> bool
        '''bool: LIN Start Allowed without Bus Power?

        Configures whether the LIN interface does not check for bus power
        present at interface start, or checks and reports an error if bus power
        is missing.

        When this property is true, the LIN interface does not check for bus
        power present at start, so no error is reported if the interface is
        started without bus power.

        When this property is false, the LIN interface checks for bus power
        present at start, and an error is reported if the interface
        is started without bus power.

        .. note:: You can modify this property only when the interface is
           stopped.
        '''
        return _props.get_session_intf_lin_alw_start_wo_bus_pwr(self._handle)

    @lin_alw_start_wo_bus_pwr.setter
    def lin_alw_start_wo_bus_pwr(self, value):
        # type: (bool) -> None
        _props.set_session_intf_lin_alw_start_wo_bus_pwr(self._handle, value)

    @property
    def lin_ostr_slv_rsp_lst_by_nad(self):
        # type: () -> typing.Iterable[int]
        '''list of int: LIN Output Stream Slave Response List By NAD

        A list of NADs for use with the replay feature
        (:any:`nixnet._session.intf.Interface.out_strm_timng` set to Replay
        Exclusive or Replay Inclusive).

        For LIN, the array of frames to replay might contain multiple slave
        response frames, each with the same slave response identifier, but each
        having been transmitted by a different slave (per the NAD value in the
        data payload). This means that processing slave response frames for
        replay requires two levels of filtering. First, you can include or
        exclude the slave response frame or ID for replay using
        Interface:Output Stream List or Interface:Output Stream List By ID. If
        you do not include the slave response frame or ID for replay, no slave
        responses are transmitted. If you do include the slave response frame
        or ID for replay, you can use the Output Stream Slave Response List by
        NAD property to filter which slave responses (per the NAD values in the
        array) are transmitted. This property is always inclusive, regardless
        of the replay mode (inclusive or exclusive). If the NAD is in the list
        and the response frame or ID has been enabled for replay, any slave
        response for that NAD is transmitted. If the NAD is not in the list, no
        slave response for that NAD is transmitted.
        '''
        return _props.get_session_intf_lin_ostr_slv_rsp_lst_by_nad(self._handle)

    @lin_ostr_slv_rsp_lst_by_nad.setter
    def lin_ostr_slv_rsp_lst_by_nad(self, value):
        # type: (typing.List[int]) -> None
        _props.set_session_intf_lin_ostr_slv_rsp_lst_by_nad(self._handle, value)

    @property
    def lin_no_response_to_in_strm(self):
        # type: () -> bool
        '''bool: LIN No Response Frames to Input Stream?

        Configure the hardware to place a LIN no response frame into the
        Stream Input queue after it is generated. A no response frame is
        generated when the hardware detects a header with no response. For more
        information about the no response frame, see
        ``nixnet.types.NoResponseFrame``.
        '''
        return _props.get_session_intf_lin_no_response_to_in_strm(self._handle)

    @lin_no_response_to_in_strm.setter
    def lin_no_response_to_in_strm(self, value):
        # type: (bool) -> None
        _props.set_session_intf_lin_no_response_to_in_strm(self._handle, value)

    @property
    def lin_checksum_to_in_strm(self):
        # type: () -> bool
        """bool: LIN Checksum to Input Stream?

        Configure the hardware to place the received checksum for each LIN Data frame into the Event ID (Info) field.
        When ``False``, the Event ID field contains ``0`` for all LIN Data stream input frames.
        """
        return _props.get_session_intf_lin_checksum_to_in_strm(self._handle)

    @lin_checksum_to_in_strm.setter
    def lin_checksum_to_in_strm(self, value):
        # type: (bool) -> None
        _props.set_session_intf_lin_checksum_to_in_strm(self._handle, value)

    @property
    def src_term_start_trigger(self):
        # type: () -> typing.Text
        '''string: Source Terminal Start Trigger

        Specifies the name of the internal terminal to use as the interface
        Start Trigger.

        This property is supported for C Series modules in a CompactDAQ
        chassis. It is not supported for CompactRIO, PXI, or PCI (refer to
        :any:`nixnet._session.base.SessionBase.connect_terminals` for those platforms).

        The digital trigger signal at this terminal is for the Start Interface
        transition, to begin communication for all sessions that use the
        interface. This property routes the start trigger, but not the timebase
        (used for timestamp of received frames and cyclic transmit of frames).
        Routing the timebase is not required for CompactDAQ, because all
        modules in the chassis automatically use a shared timebase.

        Use this property to connect the interface Start Trigger to triggers in
        other modules and/or interfaces. When you read this property, you
        specify the interface Start Trigger as the source of a connection. When
        you write this property, you specify the interface Start Trigger as the
        destination of a connection, and the value you write represents the
        source.

        The connection this property creates is disconnected when you clear
        (close) all sessions that use the interface.
        '''
        return _props.get_session_intf_src_term_start_trigger(self._handle)

    @src_term_start_trigger.setter
    def src_term_start_trigger(self, value):
        # type: (typing.Text) -> None
        _props.set_session_intf_src_term_start_trigger(self._handle, value)

    @property
    def _name(self):
        # type: () -> typing.Text
        return _props.get_session_intf_name(self._handle)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/j1939.py sha256=d8d82227abaf6f1e3bf6182a2afbfcab0f7ffe81f46163dfabbe82b96ffd9046 bytes=5599 -->
## FILE: nixnet/_session/j1939.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/j1939.py`
- sha256: `d8d82227abaf6f1e3bf6182a2afbfcab0f7ffe81f46163dfabbe82b96ffd9046`
- bytes: 5599

````python
from nixnet import _props


class J1939(object):
    """J1939 configuration for a session"""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __str__(self):
        return self.name

    @property
    def address(self):
        return _props.get_session_j1939_address(self._handle)

    @address.setter
    def address(self, value):
        _props.set_session_j1939_address(self._handle, value)

    @property
    def name(self):
        return _props.get_session_j1939_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_session_j1939_name(self._handle, value)

    def set_ecu(self, value):
        _props.set_session_j1939_ecu(self._handle, value)

    @property
    def timeout_t1(self):
        return _props.get_session_j1939_timeout_t1(self._handle)

    @timeout_t1.setter
    def timeout_t1(self, value):
        _props.set_session_j1939_timeout_t1(self._handle, value)

    @property
    def timeout_t2(self):
        return _props.get_session_j1939_timeout_t2(self._handle)

    @timeout_t2.setter
    def timeout_t2(self, value):
        _props.set_session_j1939_timeout_t2(self._handle, value)

    @property
    def timeout_t3(self):
        return _props.get_session_j1939_timeout_t3(self._handle)

    @timeout_t3.setter
    def timeout_t3(self, value):
        _props.set_session_j1939_timeout_t3(self._handle, value)

    @property
    def timeout_t4(self):
        return _props.get_session_j1939_timeout_t4(self._handle)

    @timeout_t4.setter
    def timeout_t4(self, value):
        _props.set_session_j1939_timeout_t4(self._handle, value)

    @property
    def response_time_tr_sd(self):
        return _props.get_session_j1939_response_time_tr_sd(self._handle)

    @response_time_tr_sd.setter
    def response_time_tr_sd(self, value):
        _props.set_session_j1939_response_time_tr_sd(self._handle, value)

    @property
    def response_time_tr_gd(self):
        return _props.get_session_j1939_response_time_tr_gd(self._handle)

    @response_time_tr_gd.setter
    def response_time_tr_gd(self, value):
        _props.set_session_j1939_response_time_tr_gd(self._handle, value)

    @property
    def hold_time_th(self):
        return _props.get_session_j1939_hold_time_th(self._handle)

    @hold_time_th.setter
    def hold_time_th(self, value):
        _props.set_session_j1939_hold_time_th(self._handle, value)

    @property
    def num_packets_recv(self):
        return _props.get_session_j1939_num_packets_recv(self._handle)

    @num_packets_recv.setter
    def num_packets_recv(self, value):
        _props.set_session_j1939_num_packets_recv(self._handle, value)

    @property
    def num_packets_resp(self):
        return _props.get_session_j1939_num_packets_resp(self._handle)

    @num_packets_resp.setter
    def num_packets_resp(self, value):
        _props.set_session_j1939_num_packets_resp(self._handle, value)

    @property
    def max_repeat_cts(self):
        return _props.get_session_j1939_max_repeat_cts(self._handle)

    @max_repeat_cts.setter
    def max_repeat_cts(self, value):
        _props.set_session_j1939_max_repeat_cts(self._handle, value)

    @property
    def fill_byte(self):
        return _props.get_session_j1939_fill_byte(self._handle)

    @fill_byte.setter
    def fill_byte(self, value):
        _props.set_session_j1939_fill_byte(self._handle, value)

    @property
    def write_queue_size(self):
        return _props.get_session_j1939_write_queue_size(self._handle)

    @write_queue_size.setter
    def write_queue_size(self, value):
        _props.set_session_j1939_write_queue_size(self._handle, value)

    @property
    def ecu_busy(self):
        return _props.get_session_j1939_ecu_busy(self._handle)

    @ecu_busy.setter
    def ecu_busy(self, value):
        _props.set_session_j1939_ecu_busy(self._handle, value)

    @property
    def include_dest_addr_in_pgn(self):
        # type: () -> bool
        """bool: SAE J1939 Include Destination Address in PGN

        Incoming J1939 frames are matched to an XNET database by the Parameter Group Number (PGN) of the frame.
        When receiving PDU1 frames,
        the destination address of the frame (J1939 PS field) is ignored when calculating the PGN,
        in accordance to the J1939 specification.
        This causes an XNET session to receive all frames that share the same PGN,
        making it difficult to distinguish destinations for traffic.

        When set to ``True``,
        this property instructs NI-XNET to include the destination address when extracting the PGN from the frame.
        This allows the same PGN sent to different destination addresses to be handled by separate input sessions.

        This property may be set at any time.
        When set after session start,
        it will not affect frames already received.

        This property is valid only for input sessions.
        It is not valid for stream sessions.
        This property affects all frames in a session.
        """
        return _props.get_session_j1939_include_dest_addr_in_pgn(self._handle)

    @include_dest_addr_in_pgn.setter
    def include_dest_addr_in_pgn(self, value):
        # type: (bool) -> None
        _props.set_session_j1939_include_dest_addr_in_pgn(self._handle, value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_session/signals.py sha256=7cdfec70111dd5afe5f1da083e763c7a62b79c134b92ec8af9deaa458058b7ac bytes=1350 -->
## FILE: nixnet/_session/signals.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_session/signals.py`
- sha256: `7cdfec70111dd5afe5f1da083e763c7a62b79c134b92ec8af9deaa458058b7ac`
- bytes: 1350

````python
import typing  # NOQA: F401

from nixnet import _funcs

from nixnet._session import collection


class Signals(collection.Collection):
    """Signals in a session."""

    def _create_item(self, handle, index, name):
        return Signal(handle, index, name)


class SinglePointInSignals(Signals):
    """Writeable signals in a session."""

    def read(self):
        # type: () -> typing.Iterable[typing.Tuple[int, float]]
        """Read data from a Signal Input Single-Point session.

        Yields:
            tuple of int and float: Timestamp and signal
        """
        num_signals = len(self)
        timestamps, values = _funcs.nx_read_signal_single_point(self._handle, num_signals)
        for timestamp, value in zip(timestamps, values):
            yield timestamp.value, value.value


class SinglePointOutSignals(Signals):
    """Writeable signals in a session."""

    def write(
            self,
            signals):
        # type: (typing.Iterable[float]) -> None
        """Write data to a Signal Output Single-Point session.

        Args:
            signals(list of float): A list of signal values (float).
        """
        _funcs.nx_write_signal_single_point(self._handle, list(signals))


class Signal(collection.Item):
    """Signal configuration for a session."""
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/_utils.py sha256=8cf9f41a752ec57cea0f3c7c4de7d10b9514c511b77fb597835c8b25e65d4717 bytes=2254 -->
## FILE: nixnet/_utils.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/_utils.py`
- sha256: `8cf9f41a752ec57cea0f3c7c4de7d10b9514c511b77fb597835c8b25e65d4717`
- bytes: 2254

````python
from collections.abc import Iterable
import typing  # NOQA: F401

import six

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants
from nixnet import types


def flatten_items(list):
    # type: (typing.Union[typing.Text, typing.List[typing.Text], None]) -> typing.Text
    """Flatten an item list to a string

    >>> str(flatten_items('Item'))
    'Item'
    >>> str(flatten_items(['A', 'B']))
    'A,B'
    >>> str(flatten_items(None))
    ''
    """
    if isinstance(list, six.string_types):
        # For FRAME_IN_QUEUED / FRAME_OUT_QUEUED
        # Convenience for everything else
        if ',' in list:
            _errors.raise_xnet_error(_cconsts.NX_ERR_INVALID_PROPERTY_VALUE)
        flattened = list
    elif isinstance(list, Iterable):
        flattened = ",".join(list)
    elif list is None:
        # For FRAME_IN_STREAM / FRAME_OUT_STREAM
        flattened = ''
    else:
        _errors.raise_xnet_error(_cconsts.NX_ERR_INVALID_PROPERTY_VALUE)

    return flattened


def parse_can_comm_bitfield(bitfield):
    # type:  (int) -> types.CanComm
    """Parse a CAN Comm bitfield."""
    state = constants.CanCommState(bitfield & 0x0F)
    tcvr_err = ((bitfield >> 4) & 0x01) != 0
    sleep = ((bitfield >> 5) & 0x01) != 0
    last_err = constants.CanLastErr((bitfield >> 8) & 0x0F)
    tx_err_count = ((bitfield >> 16) & 0x0FF)
    rx_err_count = ((bitfield >> 24) & 0x0FF)
    return types.CanComm(state, tcvr_err, sleep, last_err, tx_err_count, rx_err_count)


def parse_lin_comm_bitfield(first, second):
    # type: (int, int) -> types.LinComm
    """Parse a LIN Comm first."""
    sleep = ((first >> 1) & 0x01) != 0
    state = constants.LinCommState((first >> 2) & 0x03)
    last_err = constants.LinLastErr((first >> 4) & 0x0F)
    last_err_received = (first >> 8) & 0x0FF
    last_err_expected = (first >> 16) & 0x0FF
    last_err_id = (first >> 24) & 0x03F
    tcvr_rdy = ((first >> 32) & 0x01) != 0

    sched_index = second & 0x0FF

    return types.LinComm(
        sleep,
        state,
        last_err,
        last_err_received,
        last_err_expected,
        last_err_id,
        tcvr_rdy,
        sched_index)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/constants.py sha256=e118ed04220865287e427fea192e355ef25fbe21c1c83f4abcaa5a917728a619 bytes=160 -->
## FILE: nixnet/constants.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/constants.py`
- sha256: `e118ed04220865287e427fea192e355ef25fbe21c1c83f4abcaa5a917728a619`
- bytes: 160

````python
from nixnet import _cconsts
from nixnet._enums import *  # NOQA


TIMEOUT_NONE = _cconsts.NX_TIMEOUT_NONE
TIMEOUT_INFINITE = _cconsts.NX_TIMEOUT_INFINITE
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/convert.py sha256=e95bebee65ce440c48dc32d03d39d3a86b8ce7ca87cb4019ff9e91083e1a22b3 bytes=10524 -->
## FILE: nixnet/convert.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/convert.py`
- sha256: `e95bebee65ce440c48dc32d03d39d3a86b8ce7ca87cb4019ff9e91083e1a22b3`
- bytes: 10524

````python
import itertools
import typing  # NOQA: F401
import warnings

from nixnet import _frames
from nixnet import _funcs
from nixnet import _props
from nixnet import _utils
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet._session import j1939 as session_j1939
from nixnet._session import signals as session_signals


__all__ = [
    "SignalConversionSinglePointSession"]


class SignalConversionSinglePointSession(object):
    """Convert NI-XNET signal data to frame data or vice versa.

    Conversion works similar to Single-Point mode. You specify a set of signals
    that can span multiple frames. Signal to frame conversion reads a set of
    values for the signals specified and writes them to the respective
    frame(s). Frame to signal conversion parses a set of frames and returns the
    latest signal value read from a corresponding frame.
    """

    def __init__(
            self,
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            signals,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create an XNET session at run time using named references to database objects.

        Args:
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``signals`` parameter.
            signals(list of str): Strings describing signals for the session. The
                list syntax is as follows:

                ``signals`` contains one or more XNET Signal names. Each name must
                be one of the following options, whichever uniquely
                identifies a signal within the database given:

                    - ``<Signal>``
                    - ``<Frame>.<Signal>``
                    - ``<Cluster>.<Frame>.<Signal>``
                    - ``<PDU>.<Signal>``
                    - ``<Cluster>.<PDU>.<Signal>``

                ``signals`` may also contain one or more trigger signals. For
                information about trigger signals, refer to Signal Output
                Single-Point Mode or Signal Input Single-Point Mode.
        """
        flattened_list = _utils.flatten_items(signals)

        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(
            database_name,
            cluster_name,
            flattened_list,
            "",
            constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT)
        self._j1939 = session_j1939.J1939(self._handle)
        self._signals = session_signals.Signals(self._handle)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(SignalConversionSinglePointSession, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def close(self):
        # type: () -> None
        """Close (clear) the XNET session."""
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    @property
    def signals(self):
        # type: () -> session_signals.Signals
        """:any:`nixnet._session.signals.Signals`: Operate on session's signals"""
        return self._signals

    @property
    def j1939(self):
        # type: () -> session_j1939.J1939
        """:any:`nixnet._session.j1939.J1939`: Returns the J1939 configuration object for the session."""
        return self._j1939

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`nixnet._enums.AppProtocol`: This property returns the application protocol that the session uses.

        The database used with the session determines the application protocol.
        """
        return constants.AppProtocol(
            _props.get_session_application_protocol(self._handle))  # type: ignore

    @property
    def cluster_name(self):
        # type: () -> typing.Text
        """str: This property returns the cluster (network) name used with the session."""
        return _props.get_session_cluster_name(self._handle)  # type: ignore

    @property
    def database_name(self):
        # type: () -> typing.Text
        """str: This property returns the database name used with the session."""
        return _props.get_session_database_name(self._handle)  # type: ignore

    @property
    def mode(self):
        # type: () -> constants.CreateSessionMode
        """:any:`nixnet._enums.CreateSessionMode`: This property returns the mode associated with the session.

        For more information, refer to :any:`nixnet._enums.CreateSessionMode`.
        """
        return constants.CreateSessionMode(
            _props.get_session_mode(self._handle))  # type: ignore

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`nixnet._enums.Protocol`: This property returns the protocol that the interface in the session uses."""
        return constants.Protocol(
            _props.get_session_protocol(self._handle))  # type: ignore

    def _convert_bytes_to_signals(self, bytes):
        # type: (bytes) -> typing.Iterable[typing.Tuple[int, float]]
        num_signals = len(self.signals)
        timestamps, values = _funcs.nx_convert_frames_to_signals_single_point(
            self._handle, bytes, num_signals)  # type: ignore
        for timestamp, value in zip(timestamps, values):
            yield timestamp.value, value.value

    def convert_frames_to_signals(self, frames):
        # type: (typing.Iterable[types.Frame]) -> typing.Iterable[typing.Tuple[int, float]]
        """Convert Frames to signals.

        The frames passed into the ``frames`` array are read one by one, and
        the signal values found are written to internal buffers for each
        signal. Frames are identified by their identifier (FlexRay: slot)
        field. After all frames in ``frames`` array are processed, the internal
        signal buffers' status is returned with the corresponding timestamps
        from the frames where a signal value was found. The signal internal
        buffers' status is being preserved over multiple calls to this
        function.

        This way, for example, data returned from multiple calls of nxFrameRead
        for a Frame Input Stream Mode session (or any other Frame Input
        session) can be passed to this function directly.

        .. note:: Frames unknown to the session are silently ignored.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        return self._convert_bytes_to_signals(bytes)

    def _convert_signals_to_bytes(self, signals, num_bytes):
        # type: (typing.Iterable[float], int) -> bytes
        buffer, number_of_bytes_returned = _funcs.nx_convert_signals_to_frames_single_point(
            self._handle,  # type: ignore
            list(signals),
            num_bytes)
        return buffer[0:number_of_bytes_returned]

    def convert_signals_to_frames(self, signals, frame_type=types.XnetFrame):
        # type: (typing.Iterable[float], typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Convert signals to frames.

        The signal values written to the ``signals`` array are written to a raw
        frame buffer array. For each frame included in the session, one frame
        is generated in the array that contains the signal values. Signals not
        present in the session are written as their respective default values;
        empty space in the frames that signals do not occupy is written with
        the frame's default payload.

        The frame header values are filled with appropriate values so that this
        function's output can be directly written to a Frame Output session.

        Args:
            signals(list of float): Values corresponding to signals configured
                in this session.
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # Unlike some session reads, this should be safe from asking to read too much.
        num_frames_to_read = 5
        while True:
            try:
                num_bytes_to_read = num_frames_to_read * _frames.nxFrameFixed_t.size
                buffer = self._convert_signals_to_bytes(signals, num_bytes_to_read)
                break
            except errors.XnetError as e:
                if e.error_type == constants.Err.BUFFER_TOO_SMALL:
                    num_frames_to_read *= 2
                else:
                    raise
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/__init__.py sha256=8f4b62377be916078c4ad1043ba46a835d6826fa641e1830d44341bc6a9c8e01 bytes=655 -->
## FILE: nixnet/database/__init__.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/__init__.py`
- sha256: `8f4b62377be916078c4ad1043ba46a835d6826fa641e1830d44341bc6a9c8e01`
- bytes: 655

````python
from nixnet.database._cluster import Cluster
from nixnet.database._database_object import DatabaseObject
from nixnet.database._ecu import Ecu
from nixnet.database._frame import Frame
from nixnet.database._lin_sched import LinSched
from nixnet.database._lin_sched_entry import LinSchedEntry
from nixnet.database._pdu import Pdu
from nixnet.database._signal import Signal
from nixnet.database._subframe import SubFrame
from nixnet.database.database import Database


__all__ = [
    "Cluster",
    "Database",
    "DatabaseObject",
    "Ecu",
    "Frame",
    "LinSched",
    "LinSchedEntry",
    "Pdu",
    "Signal",
    "SubFrame"]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_cluster.py sha256=1f615505a4c1776c6819e0e0b0ed4f8ded74bd069bce6683b6fd86f4b5872b33 bytes=29107 -->
## FILE: nixnet/database/_cluster.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_cluster.py`
- sha256: `1f615505a4c1776c6819e0e0b0ed4f8ded74bd069bce6683b6fd86f4b5872b33`
- bytes: 29107

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _funcs
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _dbc_attributes
from nixnet.database import _find_object
from nixnet.database import _signal


class Cluster(_database_object.DatabaseObject):
    """Database cluster"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]

        from nixnet.database import _ecu
        from nixnet.database import _frame
        from nixnet.database import _lin_sched
        from nixnet.database import _pdu
        self._ecus = _collection.DbCollection(
            self._handle, constants.ObjectClass.ECU, _cconsts.NX_PROP_CLST_ECU_REFS, _ecu.Ecu)
        self._frames = _collection.DbCollection(
            self._handle, constants.ObjectClass.FRAME, _cconsts.NX_PROP_CLST_FRM_REFS, _frame.Frame)
        self._lin_sched = _collection.DbCollection(
            self._handle, constants.ObjectClass.LIN_SCHED, _cconsts.NX_PROP_CLST_LIN_SCHEDULES, _lin_sched.LinSched)
        self._pdus = _collection.DbCollection(
            self._handle, constants.ObjectClass.PDU, _cconsts.NX_PROP_CLST_PDU_REFS, _pdu.Pdu)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this cluster's configuration status.

        By default, incorrectly configured clusters in the database are not returned from
        :any:`Database.clusters` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a cluster configuration status becomes invalid after the database is opened,
        the cluster still is returned from :any:`Database.clusters`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The cluster is incorrectly configured.
        """
        status_code = _props.get_cluster_config_status(self._handle)
        _errors.check_for_error(status_code)

    def export(self, db_filepath):
        # type: (typing.Text) -> None
        """Exports this cluster to a CANdb++ or LIN database file format.

        A CAN cluster is exported as a CANdb++ database file (.dbc).
        A LIN cluster is exported as a LIN database file (.ldf).
        If the target file exists, it is overwritten.

        Exporting a cluster is not supported under Real-Time (RT).

        Args:
            db_filepath(str): Contains the pathname to the database file.
        """
        _funcs.nxdb_save_database(self._handle, db_filepath)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    def merge(
            self,
            source_obj,
            copy_mode,
            prefix,
            wait_for_complete):
        # type: (typing.Any, constants.Merge, typing.Text, bool) -> int
        """Merges database objects and related subobjects from the source to this cluster.

        The source can be any of the following objects:

        *   :any:`Frame<_frame.Frame>`
        *   :any:`Pdu`
        *   :any:`Ecu`
        *   :any:`LinSched`
        *   :any:`Cluster`

        All listed objects must have unique names in the cluster.
        They are referenced here as objects,
        as opposed to child objects (for example, a signal is a child of a frame).

        If the source object name is not used in the target cluster,
        this function copies the source objects with the child objects to the target.
        If an object with the same name exists in this cluster,
        you can avoid name collisions by specifying the prefix to be added to the name.

        If an object with the same name exists in this cluster,
        the merge behavior depends on the ``copy_mode`` input.

        **Example**

        Target frame F1(v1) has signals S1 and S2(v1). Source frame F1(v2) has signals S2(v2) and S3.

        (v1) and (v2) are two versions of one object with same name, but with different properties.

        *   Result when ``copy_mode`` is ``COPY_USE_SOURCE``: F1(v2), S2(v2), S3.
        *   Result when ``copy_mode`` is ``COPY_USE_TARGET``: F1(v1), S1, S2(v1).
        *   Result when ``copy_mode`` is ``MERGE_USE_SOURCE``: F1(v2), S1, S2(v2), S3.
        *   Result when ``copy_mode`` is ``MERGE_USE_TARGET``: F1(v1), S1, S2(v1), S3.

        If the source object is a cluster,
        this function copies all contained PDUs, ECUs, and LIN schedules
        with their child objects to this cluster.

        Depending on the number of contained objects in the source and destination clusters,
        the execution can take a longer time.
        If ``wait_for_complete`` is ``True``, this function waits until the merging process gets completed.
        If the execution completes without errors,
        ``perecent_complete`` returns ``100``.
        If ``wait_for_complete`` is ``False``,
        the function returns quickly,
        and ``perecent_complete`` returns values less than ``100``.
        You must call :any:`Cluster.merge` repeatedly until ``perecent_complete`` returns ``100``.
        You can use the time between calls to perform asynchronous tasks.

        Args:
            source_obj(object): The object to be merged into this cluster.
            copy_mode(:any:`Merge`): Defines the merging behavior if this cluster
                already contains an object with the same name.
            prefix(str): The prefix to be added to the source object name if an
                object with the same name and type exists in this cluster.
            wait_for_complete(bool): Determines whether the function returns directly
                or waits until the entire transmission is completed.
        Returns:
            int: A value which indicates the merging progress as a percentage. ``100`` indicates completion.
        """
        return _funcs.nxdb_merge(self._handle, source_obj._handle, copy_mode.value, prefix, wait_for_complete)

    @property
    def baud_rate(self):
        # type: (...) -> int
        """int: Get or set the buad rate all custer nodes use.

        This baud rate represents the rate from the database,
        so it is read-only from the session.
        Use a session interface property (for example, :any:`Interface.baud_rate`)
        to override the database baud rate with an application-specific baud rate.

        **CAN**

        For CAN, this rate can be 33333, 40000, 50000, 62500, 80000, 83333,
        100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or
        1000000. Some transceivers may support only a subset of these values.

        **LIN**

        For LIN, this rate can be 2400-20000 inclusive.

        If you need values other than these,
        use the custom settings as described in :any:`Interface.baud_rate`.
        """
        return _props.get_cluster_baud_rate64(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
        # type: (int) -> None
        _props.set_cluster_baud_rate64(self._handle, value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the cluster object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_cluster_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_cluster_comment(self._handle, value)

    @property
    def database_ref(self):
        # type: () -> int
        # todo: return a Database object here
        handle = _props.get_cluster_database_ref(self._handle)
        return handle

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the cluster's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def ecus(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Ecu` objects in this cluster.

        An ECU is assigned to a cluster when the ECU object is created.
        You cannot change this assignment afterwards.
        """
        return self._ecus

    @property
    def frames(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Frame<_frame.Frame>` objects in this cluster.

        A frame is assigned to a cluster when the frame object is created.
        You cannot change this assignment afterwards.
        """
        return self._frames

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the cluster object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        If you use a FIBEX file, the short name comes from the file.
        If you use a CANdb (.dbc), LDF (.ldf),
        or NI-CAN (.ncd) file,
        no cluster name is stored in the file,
        so NI-XNET uses the name Cluster.
        If you create the cluster yourself,
        the name that you provide is used.

        A cluster name must be unique for all clusters in a database.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database name. It is for display purposes.
        """
        return _props.get_cluster_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_cluster_name(self._handle, value)

    @property
    def pdus(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Pdu<_pdu.Pdu>` objects in this cluster.

        A PDU is assigned to a cluster when the PDU object is created.
        You cannot change this assignment afterwards.
        """
        return self._pdus

    @property
    def pdus_reqd(self):
        # type: () -> bool
        """bool: Returns whether using :any:`PDUs<Pdu>` in the database API is required for this cluster.

        If this property returns ``False``,
        it is safe to use signals as child objects of a frame without PDUs.
        This behavior is compatible with NI-XNET 1.1 or earlier.
        Clusters from .dbc, .ncd, or FIBEX 2 files always return ``False`` for this property,
        so using PDUs from those files is not required.

        If this property returns ``True``,
        the cluster contains PDU configuration,
        which requires reading the PDUs as frame child objects and then signals as PDU child objects,
        as shown in the following figure.

        Internally, the database always uses PDUs,
        but shows the same signal objects also as children of a frame.

        .. image:: pdusrequired.gif

        |

        For this property to return ``False``,
        the following conditions must be fulfilled for all frames in the cluster:

        *   Only one PDU is mapped to the frame.
        *   This PDU is not mapped to other frames.
        *   The PDU Start Bit in the frame is 0.
        *   The PDU Update Bit is not used.

        If the conditions are not fulfilled for a given frame,
        signals from the frame are still returned,
        but reading the property returns a warning.
        """
        return _props.get_cluster_pdus_reqd(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`Protocol`: Get or set the cluster protocol."""
        return constants.Protocol(_props.get_cluster_protocol(self._handle))

    @protocol.setter
    def protocol(self, value):
        # type: (constants.Protocol) -> None
        _props.set_cluster_protocol(self._handle, value.value)

    @property
    def sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`: Returns a list of all :any:`Signal<_signal.Signal>` objects in this cluster."""  # NOQA: E501
        for handle in _props.get_cluster_sig_refs(self._handle):
            yield _signal.Signal(_handle=handle)

    @property
    def can_io_mode(self):
        # type: () -> constants.CanIoMode
        """:any:`CanIoMode`: Get or set the CAN I/O Mode of the cluster."""
        return constants.CanIoMode(_props.get_cluster_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        # type: (constants.CanIoMode) -> None
        _props.set_cluster_can_io_mode(self._handle, value.value)

    @property
    def can_fd_baud_rate(self):
        # type: () -> int
        """int: Get or set the fast data baud rate when :any:`Cluster.can_io_mode` is ``CanIoMode.CAN_FD_BRS``.

        Refer to the :any:`CanIoMode` for a description of ``CanIoMode.CAN_FD_BRS``.
        Use a session interface property (for example, :any:`Interface.can_fd_baud_rate`)
        to override the database fast baud rate with an application-specific fast baud rate.

        NI-XNET CAN hardware currently accepts the following numeric baud rates:
        200000, 250000, 400000, 500000, 800000, 1000000, 1250000, 1600000,
        2000000, 2500000, 4000000, 5000000, and 8000000.
        Some transceivers may support only a subset of these values.

        If you need values other than these,
        use the custom settings as described in :any:`Interface.can_fd_baud_rate`.
        """
        return _props.get_cluster_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        # type: (int) -> None
        _props.set_cluster_can_fd_baud_rate64(self._handle, value)

    @property
    def flex_ray_act_pt_off(self):
        return _props.get_cluster_flex_ray_act_pt_off(self._handle)

    @flex_ray_act_pt_off.setter
    def flex_ray_act_pt_off(self, value):
        _props.set_cluster_flex_ray_act_pt_off(self._handle, value)

    @property
    def flex_ray_cas_rx_l_max(self):
        return _props.get_cluster_flex_ray_cas_rx_l_max(self._handle)

    @flex_ray_cas_rx_l_max.setter
    def flex_ray_cas_rx_l_max(self, value):
        _props.set_cluster_flex_ray_cas_rx_l_max(self._handle, value)

    @property
    def flex_ray_channels(self):
        return _props.get_cluster_flex_ray_channels(self._handle)

    @flex_ray_channels.setter
    def flex_ray_channels(self, value):
        _props.set_cluster_flex_ray_channels(self._handle, value)

    @property
    def flex_ray_clst_drift_dmp(self):
        return _props.get_cluster_flex_ray_clst_drift_dmp(self._handle)

    @flex_ray_clst_drift_dmp.setter
    def flex_ray_clst_drift_dmp(self, value):
        _props.set_cluster_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def flex_ray_cold_st_ats(self):
        return _props.get_cluster_flex_ray_cold_st_ats(self._handle)

    @flex_ray_cold_st_ats.setter
    def flex_ray_cold_st_ats(self, value):
        _props.set_cluster_flex_ray_cold_st_ats(self._handle, value)

    @property
    def flex_ray_cycle(self):
        return _props.get_cluster_flex_ray_cycle(self._handle)

    @flex_ray_cycle.setter
    def flex_ray_cycle(self, value):
        _props.set_cluster_flex_ray_cycle(self._handle, value)

    @property
    def flex_ray_dyn_seg_start(self):
        return _props.get_cluster_flex_ray_dyn_seg_start(self._handle)

    @property
    def flex_ray_dyn_slot_idl_ph(self):
        return _props.get_cluster_flex_ray_dyn_slot_idl_ph(self._handle)

    @flex_ray_dyn_slot_idl_ph.setter
    def flex_ray_dyn_slot_idl_ph(self, value):
        _props.set_cluster_flex_ray_dyn_slot_idl_ph(self._handle, value)

    @property
    def flex_ray_latest_usable_dyn(self):
        return _props.get_cluster_flex_ray_latest_usable_dyn(self._handle)

    @property
    def flex_ray_latest_guar_dyn(self):
        return _props.get_cluster_flex_ray_latest_guar_dyn(self._handle)

    @property
    def flex_ray_lis_noise(self):
        return _props.get_cluster_flex_ray_lis_noise(self._handle)

    @flex_ray_lis_noise.setter
    def flex_ray_lis_noise(self, value):
        _props.set_cluster_flex_ray_lis_noise(self._handle, value)

    @property
    def flex_ray_macro_per_cycle(self):
        return _props.get_cluster_flex_ray_macro_per_cycle(self._handle)

    @flex_ray_macro_per_cycle.setter
    def flex_ray_macro_per_cycle(self, value):
        _props.set_cluster_flex_ray_macro_per_cycle(self._handle, value)

    @property
    def flex_ray_macrotick(self):
        return _props.get_cluster_flex_ray_macrotick(self._handle)

    @property
    def flex_ray_max_wo_clk_cor_fat(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_fat(self._handle)

    @flex_ray_max_wo_clk_cor_fat.setter
    def flex_ray_max_wo_clk_cor_fat(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_fat(self._handle, value)

    @property
    def flex_ray_max_wo_clk_cor_pas(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_pas(self._handle)

    @flex_ray_max_wo_clk_cor_pas.setter
    def flex_ray_max_wo_clk_cor_pas(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_pas(self._handle, value)

    @property
    def flex_ray_minislot_act_pt(self):
        return _props.get_cluster_flex_ray_minislot_act_pt(self._handle)

    @flex_ray_minislot_act_pt.setter
    def flex_ray_minislot_act_pt(self, value):
        _props.set_cluster_flex_ray_minislot_act_pt(self._handle, value)

    @property
    def flex_ray_minislot(self):
        return _props.get_cluster_flex_ray_minislot(self._handle)

    @flex_ray_minislot.setter
    def flex_ray_minislot(self, value):
        _props.set_cluster_flex_ray_minislot(self._handle, value)

    @property
    def flex_ray_nm_vec_len(self):
        return _props.get_cluster_flex_ray_nm_vec_len(self._handle)

    @flex_ray_nm_vec_len.setter
    def flex_ray_nm_vec_len(self, value):
        _props.set_cluster_flex_ray_nm_vec_len(self._handle, value)

    @property
    def flex_ray_nit(self):
        return _props.get_cluster_flex_ray_nit(self._handle)

    @flex_ray_nit.setter
    def flex_ray_nit(self, value):
        _props.set_cluster_flex_ray_nit(self._handle, value)

    @property
    def flex_ray_nit_start(self):
        return _props.get_cluster_flex_ray_nit_start(self._handle)

    @property
    def flex_ray_num_minislt(self):
        return _props.get_cluster_flex_ray_num_minislt(self._handle)

    @flex_ray_num_minislt.setter
    def flex_ray_num_minislt(self, value):
        _props.set_cluster_flex_ray_num_minislt(self._handle, value)

    @property
    def flex_ray_num_stat_slt(self):
        return _props.get_cluster_flex_ray_num_stat_slt(self._handle)

    @flex_ray_num_stat_slt.setter
    def flex_ray_num_stat_slt(self, value):
        _props.set_cluster_flex_ray_num_stat_slt(self._handle, value)

    @property
    def flex_ray_off_cor_st(self):
        return _props.get_cluster_flex_ray_off_cor_st(self._handle)

    @flex_ray_off_cor_st.setter
    def flex_ray_off_cor_st(self, value):
        _props.set_cluster_flex_ray_off_cor_st(self._handle, value)

    @property
    def flex_ray_payld_len_dyn_max(self):
        return _props.get_cluster_flex_ray_payld_len_dyn_max(self._handle)

    @flex_ray_payld_len_dyn_max.setter
    def flex_ray_payld_len_dyn_max(self, value):
        _props.set_cluster_flex_ray_payld_len_dyn_max(self._handle, value)

    @property
    def flex_ray_payld_len_max(self):
        return _props.get_cluster_flex_ray_payld_len_max(self._handle)

    @property
    def flex_ray_payld_len_st(self):
        return _props.get_cluster_flex_ray_payld_len_st(self._handle)

    @flex_ray_payld_len_st.setter
    def flex_ray_payld_len_st(self, value):
        _props.set_cluster_flex_ray_payld_len_st(self._handle, value)

    @property
    def flex_ray_stat_slot(self):
        return _props.get_cluster_flex_ray_stat_slot(self._handle)

    @flex_ray_stat_slot.setter
    def flex_ray_stat_slot(self, value):
        _props.set_cluster_flex_ray_stat_slot(self._handle, value)

    @property
    def flex_ray_sym_win(self):
        return _props.get_cluster_flex_ray_sym_win(self._handle)

    @flex_ray_sym_win.setter
    def flex_ray_sym_win(self, value):
        _props.set_cluster_flex_ray_sym_win(self._handle, value)

    @property
    def flex_ray_sym_win_start(self):
        return _props.get_cluster_flex_ray_sym_win_start(self._handle)

    @property
    def flex_ray_sync_node_max(self):
        return _props.get_cluster_flex_ray_sync_node_max(self._handle)

    @flex_ray_sync_node_max.setter
    def flex_ray_sync_node_max(self, value):
        _props.set_cluster_flex_ray_sync_node_max(self._handle, value)

    @property
    def flex_ray_tss_tx(self):
        return _props.get_cluster_flex_ray_tss_tx(self._handle)

    @flex_ray_tss_tx.setter
    def flex_ray_tss_tx(self, value):
        _props.set_cluster_flex_ray_tss_tx(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_idl(self._handle)

    @flex_ray_wake_sym_rx_idl.setter
    def flex_ray_wake_sym_rx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_low(self._handle)

    @flex_ray_wake_sym_rx_low.setter
    def flex_ray_wake_sym_rx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_low(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_win(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_win(self._handle)

    @flex_ray_wake_sym_rx_win.setter
    def flex_ray_wake_sym_rx_win(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_win(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_idl(self._handle)

    @flex_ray_wake_sym_tx_idl.setter
    def flex_ray_wake_sym_tx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_low(self._handle)

    @flex_ray_wake_sym_tx_low.setter
    def flex_ray_wake_sym_tx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_low(self._handle, value)

    @property
    def flex_ray_use_wakeup(self):
        return _props.get_cluster_flex_ray_use_wakeup(self._handle)

    @flex_ray_use_wakeup.setter
    def flex_ray_use_wakeup(self, value):
        _props.set_cluster_flex_ray_use_wakeup(self._handle, value)

    @property
    def lin_schedules(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`LinSched` defined in this cluster.

        You assign a LIN schedule to a cluster when you create the LIN schedule object.
        You cannot change this assignment afterwards.
        The schedules in this collection are sorted alphabetically by schedule name.
        """
        return self._lin_sched

    @property
    def lin_tick(self):
        # type: () -> float
        """float: Returns the relative time between LIN ticks (relative f64 in seconds).

        The :any:`LinSchedEntry.delay` property must be a multiple of this tick.

        This tick is referred to as the "timebase" in the LIN specification.

        The :any:`Ecu.lin_master` property defines the Tick property in this cluster.
        You cannot use the Tick property when there is no LIN Master property defined in this cluster.
        """
        return _props.get_cluster_lin_tick(self._handle)

    @lin_tick.setter
    def lin_tick(self, value):
        # type: (float) -> None
        _props.set_cluster_lin_tick(self._handle, value)

    @property
    def flex_ray_alw_pass_act(self):
        return _props.get_cluster_flex_ray_alw_pass_act(self._handle)

    @flex_ray_alw_pass_act.setter
    def flex_ray_alw_pass_act(self, value):
        _props.set_cluster_flex_ray_alw_pass_act(self._handle, value)

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`AppProtocol`: Get or set the application protocol."""
        return constants.AppProtocol(_props.get_cluster_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        # type: (constants.AppProtocol) -> None
        _props.set_cluster_application_protocol(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        # type: () -> constants.CanFdIsoMode
        """:any:`CanFdIsoMode`: Returns the mode of a CAN FD cluster.

        The default is ``CanFdIsoMode.ISO``.
        You define the value in a dialog box that appears when you define an alias for the database.
        """
        return constants.CanFdIsoMode(_props.get_cluster_can_fd_iso_mode(self._handle))
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_collection.py sha256=1aa566c2cecffefbdd304dad3b7f741f224d6899130cc48ca0e2f43c7e05dba8 bytes=3359 -->
## FILE: nixnet/database/_collection.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_collection.py`
- sha256: `1aa566c2cecffefbdd304dad3b7f741f224d6899130cc48ca0e2f43c7e05dba8`
- bytes: 3359

````python
from collections.abc import Mapping
import typing  # NOQA: F401

import six

from nixnet import _cprops
from nixnet import _funcs
from nixnet import constants  # NOQA: F401

from nixnet.database import _database_object  # NOQA: F401


class DbCollection(Mapping):
    """Collection of database objects."""

    def __init__(self, handle, db_type, prop_id, factory):
        # type: (int, constants.ObjectClass, int, typing.Any) -> None
        self._handle = handle
        self._type = db_type
        self._prop_id = prop_id
        self._factory = factory

    def __repr__(self):
        return '{}(handle={}, db_type={})'.format(type(self).__name__, self._handle, self._type)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            sys_other = typing.cast(DbCollection, other)
            return self._handle == sys_other._handle and self._prop_id == sys_other._prop_id
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return _cprops.get_database_ref_array_len(self._handle, self._prop_id)

    def __iter__(self):
        return self.keys()

    def __getitem__(self, index):
        """Return the database object.

        Args:
            Name of database object
        Returns:
            index(str): Name of database object.
        """
        if isinstance(index, six.string_types):
            ref = _funcs.nxdb_find_object(self._handle, self._type, index)
            return self._factory(_handle=ref)
        else:
            raise TypeError(index)

    def __delitem__(self, index):
        ref = _funcs.nxdb_find_object(self._handle, self._type, index)
        _funcs.nxdb_delete_object(ref)

    def keys(self):
        """Return database object names in the collection.

        Yields:
            An iterator to database object names in the collection.
        """
        for child in self._get_children():
            yield child.name

    def values(self):
        """Return database objects in the collection.

        Yields:
            An iterator to database objects in the collection.
        """
        return self._get_children()

    def items(self):
        """Return all database object names and objects in the collection.

        Yields:
            An iterator to tuple pairs of database object names and objects in the collection
        """
        for child in self._get_children():
            yield child.name, child

    def add(self, name):
        # type: (typing.Text) -> _database_object.DatabaseObject
        """Add a new database object to the collection.

        Args:
            name(str): Name of the new database object.
        Returns:
            ``DatabaseObject``: An instance of the new database object.
        """
        ref = _funcs.nxdb_create_object(self._handle, self._type, name)
        return self._factory(_handle=ref)

    def _get_children(self):
        for ref in _cprops.get_database_ref_array(self._handle, self._prop_id):
            yield self._factory(_handle=ref)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_database_object.py sha256=6a6282a6b04fba64ecfb5c5ba918b96304ef2178da2f10cbdc7b481d35c164c6 bytes=69 -->
## FILE: nixnet/database/_database_object.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_database_object.py`
- sha256: `6a6282a6b04fba64ecfb5c5ba918b96304ef2178da2f10cbdc7b481d35c164c6`
- bytes: 69

````python
class DatabaseObject(object):
    """Database object interface."""
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_dbc_attributes.py sha256=5824aa80b002e596da2d4650da7794564424f22e8c2eaa7112484e1a371edd7f bytes=4597 -->
## FILE: nixnet/database/_dbc_attributes.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_dbc_attributes.py`
- sha256: `5824aa80b002e596da2d4650da7794564424f22e8c2eaa7112484e1a371edd7f`
- bytes: 4597

````python
from collections.abc import Mapping
import six
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import constants


class DbcAttributeCollection(Mapping):
    """Collection for accessing DBC attributes."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

        # Here, we are caching the attribute names and enums to work around a driver issue.
        # The issue results in an empty attribute value after intermixing calls to get attribute values and enums.
        # We can avoid this issue if we get all attribute enums first, before getting any attribute values.
        self._cache = dict(
            (name, self._get_enums(name))
            for name in self._get_names()
        )

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(DbcAttributeCollection, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return len(list(self.keys()))

    def __iter__(self):
        return self.keys()

    def __getitem__(self, key):
        # type: (typing.Text) -> typing.Tuple[typing.Text, bool]
        """Return the attribute value and whether it's the default value.

            Args:
                key(str): attribute name.
            Returns:
                tuple(str, bool): attribute value and whether it's the default value.
        """
        if isinstance(key, six.string_types):
            return self._get_value(key)
        else:
            raise TypeError(key)

    def keys(self):
        """Return all attribute names in the collection.

            Yields:
                An iterator to all attribute names in the collection.
        """
        for name in self._cache:
            yield name

    def values(self):
        """Return all attribute values in the collection.

            Yields:
                An iterator to all attribute values in the collection.
        """
        for name in self._cache:
            yield self._get_value(name)

    def items(self):
        """Return all attribute names and values in the collection.

            Yields:
                An iterator to tuple pairs of attribute names and values in the collection.
        """
        for name in self._cache:
            yield name, self._get_value(name)

    def _get_names(self):
        # type: () -> typing.List[typing.Text]
        mode = constants.GetDbcAttributeMode.ATTRIBUTE_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, '')
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, '', attribute_size)
        name_string = attribute_info[0]
        name_list = [
            name
            for name in name_string.split(',')
            if name.strip()
        ]
        return name_list

    def _get_enums(self, name):
        # type: (typing.Text) -> typing.List[typing.Text]
        mode = constants.GetDbcAttributeMode.ENUMERATION_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, name)
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, name, attribute_size)
        enum_string = attribute_info[0]
        enum_list = [
            enum
            for enum in enum_string.split(',')
            if enum.strip()
        ]
        return enum_list

    def _get_value(self, name):
        # type: (typing.Text) -> typing.Tuple[typing.Text, bool]
        if name not in self._cache:
            raise KeyError('Attribute name %s not found in DBC attributes' % name)

        mode = constants.GetDbcAttributeMode.ATTRIBUTE
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, name)
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, name, attribute_size)
        enums = self._cache[name]
        if not enums:
            return attribute_info

        # This attribute is an enum. Replace the enum index with the enum string.
        index = int(attribute_info[0])
        attribute_info = (enums[index], attribute_info[1])
        return attribute_info
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_dbc_signal_value_table.py sha256=30767b50d90344f9de2d83f595e7f62c05339f42e89bcd79d12dd6d1e34e9c36 bytes=3041 -->
## FILE: nixnet/database/_dbc_signal_value_table.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_dbc_signal_value_table.py`
- sha256: `30767b50d90344f9de2d83f595e7f62c05339f42e89bcd79d12dd6d1e34e9c36`
- bytes: 3041

````python
from collections.abc import Mapping
import six
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import constants


class DbcSignalValueTable(Mapping):
    """Collection for accessing a DBC signal value table."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(DbcSignalValueTable, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return len(self._value_table)

    def __iter__(self):
        return self.keys()

    def __getitem__(self, key):
        # type: (typing.Text) -> int
        """Return the value.

            Args:
                Value description.
            Returns:
                Value
        """
        if isinstance(key, six.string_types):
            return self._value_table[key]
        else:
            raise TypeError(key)

    def keys(self):
        """Return all value descriptions in the collection.

            Yields:
                An iterator to all value descriptions in the collection.
        """
        return iter(self._value_table.keys())

    def values(self):
        """Return all values in the collection.

            Yields:
                An iterator to all values in the collection.
        """
        return iter(self._value_table.values())

    def items(self):
        """Return all value descriptions and values in the collection.

            Yields:
                An iterator to tuple pairs of value descriptions and values in the collection.
        """
        return iter(self._value_table.items())

    @property
    def _value_table(self):
        # type: () -> typing.Dict[typing.Text, int]
        mode = constants.GetDbcAttributeMode.VALUE_TABLE_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, '')
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, '', attribute_size)
        table_string = attribute_info[0]
        if not table_string:
            return {}

        table_list = table_string.split(',')
        if len(table_list) % 2:
            raise ValueError('Value tables require an even number of items: %s' % table_list)

        # table_string is of the format 'value1, key1, value2, key2, ...'
        # convert to a dict: { 'key1': int('value1'), 'key2': int('value2'), ... }
        table_dict = dict(
            (key, int(value))
            for value, key in zip(table_list[0::2], table_list[1::2]))
        return table_dict
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_ecu.py sha256=772a03442c67377687cd290b415f73fca3623c0d832b550c82e7daf6e449ba83 bytes=12538 -->
## FILE: nixnet/database/_ecu.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_ecu.py`
- sha256: `772a03442c67377687cd290b415f73fca3623c0d832b550c82e7daf6e449ba83`
- bytes: 12538

````python
import typing  # NOQA: F401

from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _database_object
from nixnet.database import _dbc_attributes
from nixnet.database import _frame


class Ecu(_database_object.DatabaseObject):
    """Database ECU"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this ECU's configuration status.

        By default, incorrectly configured ECUs in the database are not returned from
        :any:`Cluster.ecus` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When an ECU configuration status becomes invalid after the database is opened,
        the ECU still is returned from :any:`Cluster.ecus`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The ECU is incorrectly configured.
        """
        status_code = _props.get_ecu_config_status(self._handle)
        _errors.check_for_error(status_code)

    @property
    def clst(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Returns the parent cluster to which the ECU is connected.

        The parent cluster is determined when the ECU object is created.
        You cannot change it afterwards.
        """
        handle = _props.get_ecu_clst_ref(self._handle)
        return _cluster.Cluster(_handle=handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the ECU object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_ecu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_ecu_comment(self._handle, value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the ECU's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the ECU object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        An ECU name must be unique for all ECUs in a cluster.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database and cluster name.
        It is for display purposes.
        """
        return _props.get_ecu_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_ecu_name(self._handle, value)

    @property
    def rx_frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames the ECU receives.

        This property defines all frames the ECU receives.
        All frames an ECU receives in a given cluster must be defined in the same cluster.
        """
        for ref in _props.get_ecu_rx_frm_refs(self._handle):
            yield _frame.Frame(_handle=ref)

    @rx_frms.setter
    def rx_frms(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        handle_list = [frame._handle for frame in value]
        _props.set_ecu_rx_frm_refs(self._handle, handle_list)

    @property
    def tx_frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames the ECU transmits.

        This property defines all frames the ECU transmits.
        All frames an ECU transmits in a given cluster must be defined in the same cluster.
        """
        for ref in _props.get_ecu_tx_frm_refs(self._handle):
            yield _frame.Frame(_handle=ref)

    @tx_frms.setter
    def tx_frms(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        frame_handles = [frame._handle for frame in value]
        _props.set_ecu_tx_frm_refs(self._handle, frame_handles)

    @property
    def flex_ray_is_coldstart(self):
        return _props.get_ecu_flex_ray_is_coldstart(self._handle)

    @property
    def flex_ray_startup_frame_ref(self):
        return _props.get_ecu_flex_ray_startup_frame_ref(self._handle)

    @property
    def flex_ray_wakeup_ptrn(self):
        return _props.get_ecu_flex_ray_wakeup_ptrn(self._handle)

    @flex_ray_wakeup_ptrn.setter
    def flex_ray_wakeup_ptrn(self, value):
        _props.set_ecu_flex_ray_wakeup_ptrn(self._handle, value)

    @property
    def flex_ray_wakeup_chs(self):
        return _props.get_ecu_flex_ray_wakeup_chs(self._handle)

    @flex_ray_wakeup_chs.setter
    def flex_ray_wakeup_chs(self, value):
        _props.set_ecu_flex_ray_wakeup_chs(self._handle, value)

    @property
    def flex_ray_connected_chs(self):
        return _props.get_ecu_flex_ray_connected_chs(self._handle)

    @flex_ray_connected_chs.setter
    def flex_ray_connected_chs(self, value):
        _props.set_ecu_flex_ray_connected_chs(self._handle, value)

    @property
    def lin_master(self):
        # type: () -> bool
        """bool: Get or set whether the ECU is a LIN master (``True``) or LIN slave (``False``)."""
        return _props.get_ecu_lin_master(self._handle)

    @lin_master.setter
    def lin_master(self, value):
        # type: (bool) -> None
        _props.set_ecu_lin_master(self._handle, value)

    @property
    def lin_protocol_ver(self):
        # type: () -> constants.LinProtocolVer
        """:any:`LinProtocolVer`: Get or set the version of the LIN standard this ECU uses."""
        return constants.LinProtocolVer(_props.get_ecu_lin_protocol_ver(self._handle))

    @lin_protocol_ver.setter
    def lin_protocol_ver(self, value):
        # type: (constants.LinProtocolVer) -> None
        _props.set_ecu_lin_protocol_ver(self._handle, value.value)

    @property
    def lin_initial_nad(self):
        # type: () -> int
        """int: Get or set the initial NAD of a LIN slave node.

        NAD is the address of a slave node and is used in diagnostic services.
        Initial NAD is replaced by configured NAD with node configuration services.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_initial_nad(self._handle)

    @lin_initial_nad.setter
    def lin_initial_nad(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_initial_nad(self._handle, value)

    @property
    def lin_config_nad(self):
        # type: () -> int
        """int: Get or set the configured NAD of a LIN slave node.

        NAD is the address of a slave node and is used in diagnostic services.
        Initial NAD is replaced by configured NAD with node configuration services.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_config_nad(self._handle)

    @lin_config_nad.setter
    def lin_config_nad(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_config_nad(self._handle, value)

    @property
    def lin_supplier_id(self):
        # type: () -> int
        """int: Get or set the supplier ID.

        Supplier ID is a 16-bit value identifying the supplier of the LIN node (ECU).

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_supplier_id(self._handle)

    @lin_supplier_id.setter
    def lin_supplier_id(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_supplier_id(self._handle, value)

    @property
    def lin_function_id(self):
        # type: () -> int
        """int: Get or set the function ID.

        Function ID is a 16-bit value identifying the function of the LIN node (ECU).

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_function_id(self._handle)

    @lin_function_id.setter
    def lin_function_id(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_function_id(self._handle, value)

    @property
    def lin_p2_min(self):
        # type: () -> float
        """float: Get or set the minimum time in seconds between frame reception and node response.

        This is the minimum time between reception of the last frame
        of the diagnostic request and the response sent by the node.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_p2_min(self._handle)

    @lin_p2_min.setter
    def lin_p2_min(self, value):
        # type (float) -> None
        _props.set_ecu_lin_p2_min(self._handle, value)

    @property
    def lin_st_min(self):
        # type: () -> float
        """float: Get or set the minimum time in seconds for node preparation.

        This is the minimum time the node requires to prepare
        for the next frame of the diagnostic service.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_st_min(self._handle)

    @lin_st_min.setter
    def lin_st_min(self, value):
        # type (float) -> None
        _props.set_ecu_lin_st_min(self._handle, value)

    @property
    def j1939_preferred_address(self):
        # type: () -> int
        """int: Get or set the preferred J1939 node address to be used when simulating this ECU.

        If you assign this ECU to an XNET session (`j1939.set_ecu`),
        XNET will start address claiming for this address using
        :any:`Ecu.j1939_node_name` and use the address for the session when the address is granted.
        """
        return _props.get_ecu_j1939_preferred_address(self._handle)

    @j1939_preferred_address.setter
    def j1939_preferred_address(self, value):
        # type: (int) -> None
        _props.set_ecu_j1939_preferred_address(self._handle, value)

    @property
    def j1939_node_name(self):
        # type: () -> int
        """int: Get or set the preferred J1939 node address to be used when simulating this ECU.

        If you assign this ECU to an XNET session (`j1939.set_ecu`),
        XNET will start address claiming for this address using
        this node name and :any:`Ecu.j1939_preferred_address`.
        """
        return _props.get_ecu_j1939_node_name(self._handle)

    @j1939_node_name.setter
    def j1939_node_name(self, value):
        # type: (int) -> None
        _props.set_ecu_j1939_node_name(self._handle, value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_find_object.py sha256=f5fe7fac6ab8f7090f66eda2581c81d18fc8ce305957980a84a6217ea73b1f61 bytes=1607 -->
## FILE: nixnet/database/_find_object.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_find_object.py`
- sha256: `f5fe7fac6ab8f7090f66eda2581c81d18fc8ce305957980a84a6217ea73b1f61`
- bytes: 1607

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _funcs
from nixnet import constants
from nixnet.database import _database_object  # NOQA: F401


def find_object(
        parent_handle,  # type: int
        object_class,  # type: typing.Any
        object_name,  # type: typing.Text
):
    # type: (...) -> _database_object.DatabaseObject
    from nixnet.database._cluster import Cluster
    from nixnet.database._ecu import Ecu
    from nixnet.database._frame import Frame
    from nixnet.database._lin_sched import LinSched
    from nixnet.database._lin_sched_entry import LinSchedEntry
    from nixnet.database._pdu import Pdu
    from nixnet.database._signal import Signal
    from nixnet.database._subframe import SubFrame

    class_enum = {
        Cluster: constants.ObjectClass.CLUSTER,
        Ecu: constants.ObjectClass.ECU,
        Frame: constants.ObjectClass.FRAME,
        LinSched: constants.ObjectClass.LIN_SCHED,
        LinSchedEntry: constants.ObjectClass.LIN_SCHED_ENTRY,
        Pdu: constants.ObjectClass.PDU,
        Signal: constants.ObjectClass.SIGNAL,
        SubFrame: constants.ObjectClass.SUBFRAME,
    }.get(object_class)

    if class_enum is None:
        raise ValueError("Unsupported value provided for argument object_class.", object_class)

    found_handle = _funcs.nxdb_find_object(parent_handle, class_enum, object_name)
    if found_handle == 0:
        _errors.raise_xnet_error(_cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND)

    return object_class(_handle=found_handle)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_frame.py sha256=f3871bde4789fdc221f787e5089082aa29023c38a2fb087314d6b5435bee247d bytes=29895 -->
## FILE: nixnet/database/_frame.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_frame.py`
- sha256: `f3871bde4789fdc221f787e5089082aa29023c38a2fb087314d6b5435bee247d`
- bytes: 29895

````python
import operator
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants
from nixnet import types

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _dbc_attributes
from nixnet.database import _find_object
from nixnet.database import _signal


class Frame(_database_object.DatabaseObject):
    """Database frame"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]

        from nixnet.database import _subframe
        self._mux_static_signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_FRM_MUX_STATIC_SIG_REFS, _signal.Signal)
        self._mux_subframes = _collection.DbCollection(
            self._handle, constants.ObjectClass.SUBFRAME, _cconsts.NX_PROP_FRM_MUX_SUBFRAME_REFS, _subframe.SubFrame)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this frame's configuration status.

        By default, incorrectly configured frames in the database are not returned from
        :any:`Cluster.frames` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a frame configuration status becomes invalid after the database is opened,
        the frame still is returned from :any:`Cluster.frames`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The frame is incorrectly configured.
        """
        status_code = _props.get_frame_config_status(self._handle)
        _errors.check_for_error(status_code)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`AppProtocol`: Get or set the frame's application protocol."""
        return constants.AppProtocol(_props.get_frame_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        # type: (constants.AppProtocol) -> None
        _props.set_frame_application_protocol(self._handle, value.value)

    @property
    def cluster(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the frame has been created.

        You cannot change the parent cluster after the frame object has been created.
        """
        handle = _props.get_frame_cluster_ref(self._handle)
        return _cluster.Cluster(_handle=handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the frame object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_frame_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_frame_comment(self._handle, value)

    @property
    def default_payload(self):
        # type: () -> typing.Iterable[int]
        """list of int: Get or set the frame default payload, specified as a list of ints.

        Each int in the list represents a byte (U8).
        The number of bytes in the list must match the :any:`Frame.payload_len` property.

        This property's initial value is an list of all ``0``,
        except the frame is located in a CAN cluster with J1939 application protocol,
        which uses ``0xFF`` by default.
        For the database formats NI-XNET supports,
        this property is not provided in the database file.

        When you use this frame within an NI-XNET session,
        this property's use varies depending on the session mode.
        The following sections describe this property's behavior for each session mode.

        Frame Output Single-Point and Frame Output Queued Modes:
            Use this property when a frame transmits prior to a call to write.
            This can occur when you set the :any:`SessionBase.auto_start` property to ``False``
            and start a session prior to writing.
            When :any:`SessionBase.auto_start` is ``True`` (default),
            the first frame write also starts frame transmit, so this property is not used.

            The following frame configurations potentially can transmit prior to a call to write:

            *   :any:`Frame.can_timing_type` is  ``CYCLIC_DATA``.
            *   :any:`Frame.can_timing_type` is  ``CYCLIC_REMOTE``.
                (for example, a remote frame received prior to a call to writing).
            *   :any:`Frame.can_timing_type` is  ``EVENT_REMOTE``.
                (for example, a remote frame received prior to a call to writing).
            *   :any:`Frame.can_timing_type` is  ``CYCLIC_EVENT``.
            *   LIN frame in a schedule entry where :any:`LinSchedEntry.type` is ``UNCONDITIONAL``.

            The following frame configurations cannot transmit prior to writing, so this property is not used:

            *   :any:`Frame.can_timing_type` is  ``EVENT_DATA``..
            *   LIN frame in a schedule entry where :any:`LinSchedEntry.type` is ``SPORADIC``
                or ``EVENT_TRIGGERED``.

        Frame Output Stream Mode:
            This property is not used. Transmit is limited to frames provided to write.

        Signal Output Single-Point, Signal Output Waveform, and Signal Output XY Modes:
            Use this property when a frame transmits prior to a call to write.
            Refer to Frame Output Single-Point and Frame Output Queued Modes
            for a list of applicable frame configurations.

            This property is used as the initial payload,
            then each XNET Signal Default Value is mapped into that payload,
            and the result is used for the frame transmit.

        Frame Input Stream and Frame Input Queued Modes:
            This property is not used.
            These modes do not return data prior to receiving frames.

        Frame Input Single-Point Mode:
            This property is used for frames read returns prior to receiving the first frame.

        Signal Input Single-Point, Signal Input Waveform, and Signal Input XY Modes:
            This property is not used.
            Each :any:`Signal.default` is used when
            reading from a session prior to receiving the first frame.
        """
        return _props.get_frame_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        # type: (typing.List[int]) -> None
        _props.set_frame_default_payload(self._handle, value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the frame's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def id(self):
        # type: () -> int
        """int: Get or set the frame identifier.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this frame,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.

        CAN:
            For CAN frames, this is the Arbitration ID.

            When :any:`Frame.can_ext_id` is set to ``False``,
            this is the standard CAN identifier with a size of 11 bits,
            which results in allowed range of 0-2047.
            However, the CAN standard disallows identifiers in which the first 7 bits are all recessive,
            so the working range of identifiers is 0-2031.

            When :any:`Frame.can_ext_id` is set to ``True``,
            this is the extended CAN identifier with a size of 29 bits,
            which results in allowed range of 0-536870911.
        LIN:
            For LIN frames, this is the frame's ID (unprotected).
            The valid range for a LIN frame ID is 0-63 (inclusive)
        """
        return _props.get_frame_id(self._handle)

    @id.setter
    def id(self, value):
        # type: (int) -> None
        _props.set_frame_id(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: String identifying a frame object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A frame name must be unique for all frames in a cluster.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database and cluster name.
        It is for display purposes.
        """
        return _props.get_frame_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_frame_name(self._handle, value)

    @property
    def payload_len(self):
        # type: () -> int
        """int: Get or set the number of bytes of data in the payload.

        For CAN and LIN, this is 0-8.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this frame,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_frame_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        # type: (int) -> None
        _props.set_frame_payload_len(self._handle, value)

    @property
    def sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`:Get a list of all :any:`Signal<_signal.Signal>` objects in the frame.

        This property returns a list to all :any:`Signal<_signal.Signal>` objects in the frame,
        including static and dynamic signals and the multiplexer signal.
        """
        for handle in _props.get_frame_sig_refs(self._handle):
            yield _signal.Signal(_handle=handle)

    @property
    def can_ext_id(self):
        # type: () -> bool
        """bool: Get or set whether the :any:`Frame.id` property in a CAN cluster is extended.

        The frame identifier represents a standard 11-bit (``False``) or extended 29-bit (``True``) arbitration ID.
        """
        return _props.get_frame_can_ext_id(self._handle)

    @can_ext_id.setter
    def can_ext_id(self, value):
        # type: (bool) -> None
        _props.set_frame_can_ext_id(self._handle, value)

    @property
    def can_timing_type(self):
        # type: () -> constants.FrmCanTiming
        """:any:`FrmCanTiming`: Get or set the CAN frame timing.

        Because this property specifies the behavior of the frame's transfer within the embedded system
        (for example, a vehicle),
        it describes the transfer between ECUs in the network.
        In the following description,
        transmitting ECU refers to the ECU that transmits the CAN data frame
        (and possibly receives the associated CAN remote frame).
        Receiving ECU refers to an ECU that receives the CAN data frame
        (and possibly transmits the associated CAN remote frame).

        When you use the frame within an NI-XNET session,
        an output session acts as the transmitting ECU,
        and an input session acts as a receiving ECU.
        For a description of how these CAN timing types apply to the NI-XNET session mode,
        refer to `CAN Timing Type and Session Mode`.

        If you are using a FIBEX or AUTOSAR database,
        this property is a required part of the XML schema for a frame,
        so the default (initial) value is obtained from the file.

        If you are using a CANdb (.dbc) database,
        this property is an optional attribute in the file.
        If NI-XNET finds an attribute named GenMsgSendType,
        that attribute is the default value of this property.
        If the GenMsgSendType attribute begins with cyclic,
        this property's default value is ``CYCLIC_DATA``;
        otherwise, it is ``EVENT_DATA``.
        If the CANdb file does not use the GenMsgSendType attribute,
        this property uses a default value of ``EVENT_DATA``,
        which you can change in your application.

        If you are using an .ncd database or an in-memory database,
        this property uses a default value of ``EVENT_DATA``.
        Within your application,
        change this property to the desired timing type.
        """
        return constants.FrmCanTiming(_props.get_frame_can_timing_type(self._handle))

    @can_timing_type.setter
    def can_timing_type(self, value):
        # type: (constants.FrmCanTiming) -> None
        _props.set_frame_can_timing_type(self._handle, value.value)

    @property
    def can_tx_time(self):
        # type: () -> float
        """float: Get or set the time between consecutive frames from the transmitting ECU.

        The units are in seconds.

        Although the fractional part of the float can provide resolution of picoseconds,
        the NI-XNET CAN transmit supports an accuracy of 500 microseconds.
        Therefore, when used within an NI-XNET output session,
        this property is rounded to the nearest 500 microsecond increment (0.0005).

        For a :any:`Frame.can_timing_type` of ``CYCLIC_DATA`` or ``CYCLIC_REMOTE``,
        this property specifies the time between consecutive data/remote frames.
        A time of 0.0 is invalid.

        For a :any:`Frame.can_timing_type` of ``EVENT_DATA`` or ``EVENT_REMOTE``,
        this property specifies the minimum time between consecutive
        data/remote frames when the event occurs quickly.
        This is also known as the debounce time or minimum interval.
        The time is measured from the end of previous frame (acknowledgment) to the start of the next frame.
        A time of 0.0 specifies no minimum (back to back frames allowed).

        If you are using a FIBEX or AUTOSAR database,
        this property is a required part of the XML schema for a frame,
        so the default (initial) value is obtained from the file.

        If you are using a CANdb (.dbc) database,
        this property is an optional attribute in the file.
        If NI-XNET finds an attribute named GenMsgCycleTime,
        that attribute is interpreted as a number of milliseconds and used as the default value of this property.
        If the CANdb file does not use the GenMsgCycleTime attribute,
        this property uses a default value of 0.1 (100 ms),
        which you can change in your application.

        If you are using a .ncd database or an in-memory database,
        this property uses a default value of 0.1 (100 ms).
        Within your application, change this property to the desired time.
        """
        return _props.get_frame_can_tx_time(self._handle)

    @can_tx_time.setter
    def can_tx_time(self, value):
        # type: (float) -> None
        _props.set_frame_can_tx_time(self._handle, value)

    @property
    def flex_ray_base_cycle(self):
        return _props.get_frame_flex_ray_base_cycle(self._handle)

    @flex_ray_base_cycle.setter
    def flex_ray_base_cycle(self, value):
        _props.set_frame_flex_ray_base_cycle(self._handle, value)

    @property
    def flex_ray_ch_assign(self):
        return _props.get_frame_flex_ray_ch_assign(self._handle)

    @flex_ray_ch_assign.setter
    def flex_ray_ch_assign(self, value):
        _props.set_frame_flex_ray_ch_assign(self._handle, value)

    @property
    def flex_ray_cycle_rep(self):
        return _props.get_frame_flex_ray_cycle_rep(self._handle)

    @flex_ray_cycle_rep.setter
    def flex_ray_cycle_rep(self, value):
        _props.set_frame_flex_ray_cycle_rep(self._handle, value)

    @property
    def flex_ray_preamble(self):
        return _props.get_frame_flex_ray_preamble(self._handle)

    @flex_ray_preamble.setter
    def flex_ray_preamble(self, value):
        _props.set_frame_flex_ray_preamble(self._handle, value)

    @property
    def flex_ray_startup(self):
        return _props.get_frame_flex_ray_startup(self._handle)

    @flex_ray_startup.setter
    def flex_ray_startup(self, value):
        _props.set_frame_flex_ray_startup(self._handle, value)

    @property
    def flex_ray_sync(self):
        return _props.get_frame_flex_ray_sync(self._handle)

    @flex_ray_sync.setter
    def flex_ray_sync(self, value):
        _props.set_frame_flex_ray_sync(self._handle, value)

    @property
    def flex_ray_timing_type(self):
        return _props.get_frame_flex_ray_timing_type(self._handle)

    @flex_ray_timing_type.setter
    def flex_ray_timing_type(self, value):
        _props.set_frame_flex_ray_timing_type(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_enabled(self):
        return _props.get_frame_flex_ray_in_cyc_rep_enabled(self._handle)

    @property
    def flex_ray_in_cyc_rep_i_ds(self):
        return _props.get_frame_flex_ray_in_cyc_rep_i_ds(self._handle)

    @flex_ray_in_cyc_rep_i_ds.setter
    def flex_ray_in_cyc_rep_i_ds(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_i_ds(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_ch_assigns(self):
        return _props.get_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle)

    @flex_ray_in_cyc_rep_ch_assigns.setter
    def flex_ray_in_cyc_rep_ch_assigns(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle, value)

    @property
    def lin_checksum(self):
        # type: () -> constants.FrmLinChecksum
        """:any:`FrmLinChecksum`: Returns whether the LIN frame transmitted checksum is classic or enhanced.

        The enhanced checksum considers the protected identifier when it is generated.

        The checksum is determined from the :any:`Ecu.lin_protocol_ver` properties
        of the transmitting and receiving the frame.
        The lower version of both ECUs is significant.
        If the LIN version of both ECUs is 2.0 or higher,
        the checksum type is enhanced;
        otherwise, the checksum type is classic.

        Diagnostic frames (with decimal identifier 60 or 61) always use classic checksum,
        even on LIN 2.x.
        """
        return constants.FrmLinChecksum(_props.get_frame_lin_checksum(self._handle))

    @property
    def mux_is_muxed(self):
        # type: () -> bool
        """bool: Returns whether this frame is data multiplexed.

        This property returns ``True`` if the frame contains a multiplexer signal.
        Frames containing a multiplexer contain subframes that allow using bits
        of the frame payload for different information (signals) depending on
        the multiplexer value.
        """
        return _props.get_frame_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig(self):
        # type: () -> _signal.Signal
        """:any:`Signal<_signal.Signal>`: Returns a data multiplexer signal object in the frame.

        Use the :any:`Frame.mux_is_muxed` property to determine whether the frame contains a multiplexer signal.

        You can create a data multiplexer signal by creating a signal
        and then setting the :any:`Signal.mux_is_data_mux` property to ``True``.

        A frame can contain only one data multiplexer signal.

        Raises:
            :any:`XnetError`: The data multiplexer signal is not defined in the frame
        """
        ref = _props.get_frame_mux_data_mux_sig_ref(self._handle)
        if ref == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_SIGNAL_NOT_FOUND)

        return _signal.Signal(_handle=ref)

    @property
    def mux_static_signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of static :any:`Signal<_signal.Signal>` objects in this frame.

        Static signals are contained in every frame transmitted,
        as opposed to dynamic signals,
        which are transmitted depending on the multiplexer value.

        If the frame is not multiplexed,
        this property returns the same objects as :any:`Frame.sigs`.
        """
        return self._mux_static_signals

    @property
    def mux_subframes(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`SubFrame` objects in this frame.

        A subframe defines a group of signals transmitted using the same multiplexer value.
        Only one subframe at a time is transmitted in the frame.

        A subframe is defined by creating a subframe object as a child of a frame.
        """
        return self._mux_subframes

    @property
    def pdu_properties(self):
        # type: () -> typing.Iterable[types.PduProperties]
        """list of :any:`PduProperties`: Get or set a list that maps existing PDUs to a frame.

        A mapped PDU is transmitted inside the frame payload when the frame is transmitted.
        You can map one or more PDUs to a frame and one PDU to multiple frames.

        Mapping PDUs to a frame requires setting pdu_properties with a list of PduProperties tuples.
        Each tuple contains the following properties:

        *   :any:`PduProperties.pdu`: Defines the sequence of values for the other two properties.
        *   :any:`PduProperties.start_bit`: Defines the start bit of the PDU inside the frame.
        *   :any:`PduProperties.update_bit`: Defines the update bit for the PDU inside the frame.
            If the update bit is not used, set the value to ``-1``.

        Databases imported from FIBEX prior to version 3.0,
        from DBC, NCD, or LDF files have a strong one-to-one relationship between frames and PDUs.
        Every frame has exactly one PDU mapped, and every PDU is mapped to exactly one frame.

        To unmap PDUs from a frame, set this property to an empty list.
        A frame without mapped PDUs contains no signals.

        For CAN and LIN, NI-XNET supports only a one-to-one relationship between frames and PDUs.
        For those interfaces, advanced PDU configuration returns
        raises an exception when calling :any:`Frame.check_config_status` and when creating a session.
        If you do not use advanced PDU configuration,
        you can avoid using PDUs in the database API
        and create signals and subframes directly on a frame.
        """
        handles = _props.get_frame_pdu_refs(self._handle)
        pdu_tuples = zip(*(handles,
                           _props.get_frame_pdu_start_bits(self._handle),
                           _props.get_frame_pdu_update_bits(self._handle)))
        for (ref, start_bit, update_bit) in pdu_tuples:
            yield types.PduProperties(ref, start_bit, update_bit)

    @pdu_properties.setter
    def pdu_properties(self, pdus):
        # type: (typing.Iterable[types.PduProperties]) -> None
        _props.set_frame_pdu_refs(self._handle,
                                  list(map(lambda p: p.pdu._handle, pdus)))
        _props.set_frame_pdu_start_bits(self._handle,
                                        list(map(operator.attrgetter('start_bit'), pdus)))
        _props.set_frame_pdu_update_bits(self._handle,
                                         list(map(operator.attrgetter('update_bit'), pdus)))

    @property
    def variable_payload(self):
        # type: () -> bool
        # This property is currently not documented in the C API.
        # If/when we have C API documentation, we should add it here too.
        return _props.get_frame_variable_payload(self._handle)

    @variable_payload.setter
    def variable_payload(self, value):
        # type: (bool) -> None
        _props.set_frame_variable_payload(self._handle, value)

    @property
    def can_io_mode(self):
        # type: () -> constants.CanIoMode
        """:any:`CanIoMode`: Get or set the frame's I/O mode.

        This property is used in ISO CAN FD+BRS mode only.
        In this mode,
        you can specify every frame to be transmitted in CAN 2.0, CAN FD, or CAN FD+BRS mode.
        CAN FD+BRS frames require the interface to be in CAN FD+BRS mode;
        otherwise, it is transmitted in CAN FD mode.

        When the interface is in Non-ISO CAN FD or Legacy ISO CAN FD mode,
        this property is disregarded.
        In Non-ISO CAN FD and Legacy ISO CAN FD mode,
        you must use :any:`Interface.can_tx_io_mode` to switch the transmit mode.

        When the assigned database does not define the property in ISO CAN FD mode,
        the frames are transmitted with :any:`Interface.can_io_mode`.
        """
        return constants.CanIoMode(_props.get_frame_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        # type: (constants.CanIoMode) -> None
        _props.set_frame_can_io_mode(self._handle, value.value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_lin_sched.py sha256=42503ea4f056aabb80d557dac5b5140a9f404777eb80d90a2d48035cb341d0cf bytes=9500 -->
## FILE: nixnet/database/_lin_sched.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_lin_sched.py`
- sha256: `42503ea4f056aabb80d557dac5b5140a9f404777eb80d90a2d48035cb341d0cf`
- bytes: 9500

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object


class LinSched(_database_object.DatabaseObject):
    """Database LIN schedule"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

        from nixnet.database import _lin_sched_entry
        self._entries = _collection.DbCollection(
            self._handle,
            constants.ObjectClass.LIN_SCHED_ENTRY,
            _cconsts.NX_PROP_LIN_SCHED_ENTRIES,
            _lin_sched_entry.LinSchedEntry)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this LIN schedule's configuration status.

        By default, incorrectly configured schedules in the database are not returned from
        :any:`Cluster.lin_schedules` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a schedule configuration status becomes invalid after the database is opened,
        the schedule still is returned from :any:`Cluster.lin_schedules`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The LIN schedule is incorrectly configured.
        """
        status_code = _props.get_lin_sched_config_status(self._handle)
        _errors.check_for_error(status_code)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    @property
    def clst(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the you created the schedule.

        You cannot change the parent cluster after creating the schedule object.
        """
        handle = _props.get_lin_sched_clst_ref(self._handle)
        return _cluster.Cluster(_handle=handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the schedule object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_lin_sched_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_comment(self._handle, value)

    @property
    def entries(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`LinSchedEntry` for this LIN schedule.

        The position of each entry in this collection specifies the position in the schedule.
        The database file and/or the order that you create entries at runtime determine the position.
        """
        return self._entries

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the LIN schedule object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.),
        and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A schedule name must be unique for all schedules in a cluster.
        """
        return _props.get_lin_sched_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_name(self._handle, value)

    @property
    def priority(self):
        # type: () -> int
        """int: Get or set the priority of a run-once LIN schedule.

        This priority applies when multiple run-once schedules are pending for execution.

        The valid range for this property is 1-254.
        Lower values correspond to higher priority.

        This property applies only when the :any:`LinSched.run_mode` property is ``ONCE``.
        Run-once schedule requests are queued for execution based on this property.
        When all run-once schedules have completed,
        the master returns to the previously running continuous schedule (or null).

        Run-continuous schedule requests are not queued.
        Only the most recent run-continuous schedule is used,
        and it executes only if no run-once schedule is pending.
        Therefore, a run-continuous schedule has an effective priority of ``255``,
        but this property is not used.

        Null schedule requests take effect immediately
        and supercede any running run-once or run-continuous schedule.
        The queue of pending run-once schedule requests
        is flushed (emptied without running them).
        Therefore, a null schedule has an effective priority of ``0``,
        but this property is not used.

        This property is not read from the database,
        but is handled like a database property.
        After opening the database, the default value is returned,
        and you can change the property.
        But similar to database properties,
        you cannot change it after a session is created.
        """
        return _props.get_lin_sched_priority(self._handle)

    @priority.setter
    def priority(self, value):
        # type: (int) -> None
        _props.set_lin_sched_priority(self._handle, value)

    @property
    def run_mode(self):
        # type: () -> constants.LinSchedRunMode
        """:any:`LinSchedRunMode`: Get or set how the master runs this schedule.

        This property is not read from the database,
        but is handled like a database property.
        After opening the database, the default value is returned,
        and you can change the property.
        But similar to database properties,
        you cannot change it after a session is created.

        Usually, the default value for the run mode is ``CONTINUOUS``.
        If the schedule is configured to be a collision resolving table
        for an event-triggered entry, the default is ``ONCE``.
        """
        return constants.LinSchedRunMode(_props.get_lin_sched_run_mode(self._handle))

    @run_mode.setter
    def run_mode(self, value):
        # type: (constants.LinSchedRunMode) -> None
        _props.set_lin_sched_run_mode(self._handle, value.value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_lin_sched_entry.py sha256=8890f474e8a35a8c5bae061ae2253a58a5213a8db3b6e2f5e2c21192700596e3 bytes=8842 -->
## FILE: nixnet/database/_lin_sched_entry.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_lin_sched_entry.py`
- sha256: `8890f474e8a35a8c5bae061ae2253a58a5213a8db3b6e2f5e2c21192700596e3`
- bytes: 8842

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _database_object
from nixnet.database import _frame
from nixnet.database import _lin_sched


class LinSchedEntry(_database_object.DatabaseObject):
    """Database LIN schedule entry"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    @property
    def collision_res_sched(self):
        # type: () -> typing.Optional[_lin_sched.LinSched]
        """:any:`LinSched`: Get or set a LIN schedule that resolves a collision for this event-triggered entry.

        This property applies only when :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``.
        When a collision occurs for the event-triggered entry in this schedule,
        the master must switch to the collision resolving schedule to transfer the unconditional frames successfully.

        Raises:
            :any:`XnetError`: The property requires that :any:`LinSchedEntry.type` be set to ``EVENT_TRIGGERED``.
        """
        handle = _props.get_lin_sched_entry_collision_res_sched(self._handle)
        if handle == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND)

        return _lin_sched.LinSched(_handle=handle)

    @collision_res_sched.setter
    def collision_res_sched(self, value):
        # type: (_lin_sched.LinSched) -> None
        _props.set_lin_sched_entry_collision_res_sched(self._handle, value._handle)

    @property
    def delay(self):
        # type: () -> float
        """float: Get or set the time from the start of this entry (slot) to the start of the next entry.

        The property uses a float value in seconds, with the fractional part used for milliseconds or microseconds.
        """
        return _props.get_lin_sched_entry_delay(self._handle)

    @delay.setter
    def delay(self, value):
        # type: (float) -> None
        _props.set_lin_sched_entry_delay(self._handle, value)

    @property
    def event_id(self):
        # type: () -> int
        """int: Get or set the event-triggered entry identifier.

        This identifier is unprotected (NI-XNET handles the protection).

        This property applies only when :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``.
        This identifier is for the event triggered entry itself,
        and the first payload byte is for the protected identifier of the contained unconditional frame.
        """
        return _props.get_lin_sched_entry_event_id(self._handle)

    @event_id.setter
    def event_id(self, value):
        # type: (int) -> None
        _props.set_lin_sched_entry_event_id(self._handle, value)

    @property
    def frames(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames for this LIN schedule entry.

        If :any:`LinSchedEntry.type` is ``UNCONDITIONAL``,
        this list contains one frame,
        which is the single unconditional frame for this entry.

        If :any:`LinSchedEntry.type` is ``SPORADIC``,
        this list contains one or more unconditional frames for this entry.
        When multiple frames are pending for this entry,
        the order in the list determines the priority to transmit.

        If :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``,
        this list contains one or more unconditional frames for this entry.
        When multiple frames for this entry are pending to be sent by distinct slaves,
        this property uses the :any:`LinSchedEntry.collision_res_sched` to process the frames.
        """
        for ref in _props.get_lin_sched_entry_frames(self._handle):
            yield _frame.Frame(_handle=ref)

    @frames.setter
    def frames(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        frame_handles = [frame._handle for frame in value]
        _props.set_lin_sched_entry_frames(self._handle, frame_handles)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the LIN schedule entry object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A schedule entry name must be unique for all entries in the same schedule.
        """
        return _props.get_lin_sched_entry_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_entry_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a LIN schedule entry name unique to the cluster that contains the object.

        If the single name is not unique within the cluster,
        the name is <schedule-name>.<schedule-entry-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find`
        because it may be not unique in the cluster.
        """
        return _props.get_lin_sched_entry_name_unique_to_cluster(self._handle)

    @property
    def sched(self):
        # type: () -> _lin_sched.LinSched
        """:any:`LinSched`: Returns the LIN schedule that uses this entry.

        This LIN schedule is considered this entry's parent.
        You define the parent schedule when you create the entry object.
        You cannot change it afterwards.
        """
        handle = _props.get_lin_sched_entry_sched(self._handle)
        lin_sched = _lin_sched.LinSched(_handle=handle)
        return lin_sched

    @property
    def type(self):
        # type: () -> constants.LinSchedEntryType
        """:any:`LinSchedEntryType`: Get or set the LIN schedule entry type.

        All frames that contain a payload are ``UNCONDITIONAL``.
        The LIN schedule entry type determines the mechanism for transferring frames in this entry (slot).
        """
        return constants.LinSchedEntryType(_props.get_lin_sched_entry_type(self._handle))

    @type.setter
    def type(self, value):
        # type: (constants.LinSchedEntryType) -> None
        _props.set_lin_sched_entry_type(self._handle, value.value)

    @property
    def nc_ff_data_bytes(self):
        # type: () -> typing.Iterable[int]
        """list of int: Get or set a list of 8 ints containing raw data for LIN node configuration.

        Node configuration defines a set of services used to configure slave nodes in the cluster.
        Every service has a specific set of parameters coded in this int list.
        In the LDF, file those parameters are stored, for example, in the node (ECU) or the frame object.
        NI-XNET LDF reader composes those parameters to the byte values like they are sent on the bus.
        The LIN specification document describes the node configuration services
        and the mapping of the parameters to the free format bytes.

        The node configuration service is executed only if
        :any:`LinSchedEntry.type` is set to ``NODE_CONFIG_SERVICE``.

        .. warning:: This property is not saved to the FIBEX file.
            If you write this property, save the database, and reopen it,
            the node configuration services are not contained in the database.
            Writing this property is useful only in the NI-XNET session immediately following.
        """
        return _props.get_lin_sched_entry_nc_ff_data_bytes(self._handle)

    @nc_ff_data_bytes.setter
    def nc_ff_data_bytes(self, value):
        # type: (typing.List[int]) -> None
        _props.set_lin_sched_entry_nc_ff_data_bytes(self._handle, value)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_pdu.py sha256=5dd113e3ce310abe25d773a0ac7a92132da7f312f0fc88be1b292054553a977c bytes=11390 -->
## FILE: nixnet/database/_pdu.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_pdu.py`
- sha256: `5dd113e3ce310abe25d773a0ac7a92132da7f312f0fc88be1b292054553a977c`
- bytes: 11390

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object
from nixnet.database import _frame
from nixnet.database import _signal


class Pdu(_database_object.DatabaseObject):
    """Database PDU"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

        from nixnet.database import _signal
        from nixnet.database import _subframe
        self._signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_PDU_SIG_REFS, _signal.Signal)
        self._mux_subframes = _collection.DbCollection(
            self._handle, constants.ObjectClass.SUBFRAME, _cconsts.NX_PROP_PDU_MUX_SUBFRAME_REFS, _subframe.SubFrame)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this PDU's configuration status.

        By default, incorrectly configured PDUs in the database are not returned from
        :any:`Cluster.pdus` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a PDU configuration status becomes invalid after the database is opened,
        the PDU still is returned from :any:`Cluster.pdus`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The PDU is incorrectly configured.
        """
        status_code = _props.get_pdu_config_status(self._handle)
        _errors.check_for_error(status_code)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    @property
    def cluster(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the PDU has been created.

        You cannot change the parent cluster after creating the PDU object.
        """
        handle = _props.get_pdu_cluster_ref(self._handle)
        return _cluster.Cluster(_handle=handle)

    @property
    def default_payload(self):
        return _props.get_pdu_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        _props.set_pdu_default_payload(self._handle, value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the PDU object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_pdu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_pdu_comment(self._handle, value)

    @property
    def frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Returns a list of all frames to which the PDU is mapped.

        A PDU is transmitted within the frames to which it is mapped.

        To map a PDU to a frame,
        use the :any:`Frame.pdu_properties` property.
        You can map one PDU to multiple frames.
        """
        for handle in _props.get_pdu_frm_refs(self._handle):
            yield _frame.Frame(_handle=handle)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the PDU object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A PDU name must be unique for all PDUs in a cluster.
        """
        return _props.get_pdu_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_pdu_name(self._handle, value)

    @property
    def payload_len(self):
        # type: () -> int
        """int: Get or set the size of the PDU data in bytes.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this PDU,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_pdu_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        # type: (int) -> None
        _props.set_pdu_payload_len(self._handle, value)

    @property
    def signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of all :any:`Signal<_signal.Signal>` objects in this PDU.

        The collection includes all signals in the PDU,
        including static and dynamic signals and the multiplexer signal.
        """
        return self._signals

    @property
    def mux_is_muxed(self):
        # type: () -> bool
        """bool: Returns ``True`` if the PDU contains a multiplexer signal.

        PDUs containing a multiplexer contain subframes that allow
        using bits of the payload for different information (signals),
        depending on the value of the :any:`SubFrame.mux_value` property.
        """
        return _props.get_pdu_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig(self):
        # type: () -> _signal.Signal
        """:any:`Signal<_signal.Signal>`: Data multiplexer signal in the PDU.

        This property returns the reference to the data multiplexer signal.
        If data multiplexer is not defined in the PDU, the property raises an :any:`XnetError` exception.
        Use the :any:`Pdu.mux_is_muxed` property to determine whether the PDU contains a multiplexer signal.

        You can create a data multiplexer signal by creating a signal
        and then setting the :any:`Signal.mux_is_data_mux` property to ``True``.

        A PDU can contain only one data multiplexer signal.

        Raises:
            :any:`XnetError`: The data multiplexer is not defined in the PDU.
        """
        handle = _props.get_pdu_mux_data_mux_sig_ref(self._handle)
        if handle == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_SIGNAL_NOT_FOUND)

        return _signal.Signal(_handle=handle)

    @property
    def mux_static_sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`: Returns a list of static signals in the PDU.

        Returns an list of signal objects in the PDU that do not depend
        on value of the :any:`SubFrame.mux_value` property.
        Static signals are contained in every PDU transmitted,
        as opposed to dynamic signals,
        which are transmitted depending on the value of the :any:`SubFrame.mux_value` property.

        You can create static signals by specifying the PDU as the parent object.
        You can create dynamic signals by specifying a subframe as the parent.

        If the PDU is not multiplexed,
        this property returns the same list as the :any:`Pdu.signals` property.
        """
        for handle in _props.get_pdu_mux_static_sig_refs(self._handle):
            yield _signal.Signal(_handle=handle)

    @property
    def mux_subframes(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`SubFrame` objects in this PDU.

        A subframe defines a group of signals transmitted using the same value of the :any:`SubFrame.mux_value`.
        Only one subframe is transmitted in the PDU at a time.
        """
        return self._mux_subframes
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_signal.py sha256=4db96d109cbcc07f7ff438af1ebf214087d7edc3e8f97e5550e345dde2687f14 bytes=20576 -->
## FILE: nixnet/database/_signal.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_signal.py`
- sha256: `4db96d109cbcc07f7ff438af1ebf214087d7edc3e8f97e5550e345dde2687f14`
- bytes: 20576

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _database_object
from nixnet.database import _dbc_attributes
from nixnet.database import _dbc_signal_value_table

# workaround to avoid circular imports caused by mypy type annotations
MYPY = False
if MYPY:
    from nixnet.database import _frame  # NOQA: F401
    from nixnet.database import _pdu  # NOQA: F401
    from nixnet.database import _subframe  # NOQA: F401


class Signal(_database_object.DatabaseObject):
    """Database signal"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]
        self._dbc_signal_value_table = _dbc_signal_value_table.DbcSignalValueTable(self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this signal's configuration status.

        By default, incorrectly configured signals in the database are not returned from
        :any:`Frame.sigs` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a signal configuration status becomes invalid after the database is opened,
        the signal still is returned from :any:`Frame.sigs`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Examples of invalid signal configuration:

        *   The signal is specified using bits outside the frame payload.
        *   The signal overlaps another signal in the frame.
            For example,
            two multiplexed signals with the same multiplexer value are using the same bit in the frame payload.
        *   The signal with integer data type (signed or unsigned) is specified with more than 52 bits.
            This is not allowed due to internal limitation of the double data type that NI-XNET uses for signal values.
        *   The frame containing the signal is invalid
            (for example, a CAN frame is defined with more than 8 payload bytes).

        Raises:
            :any:`XnetError`: The signal is incorrectly configured.
        """
        status_code = _props.get_signal_config_status(self._handle)
        _errors.check_for_error(status_code)

    @property
    def byte_ordr(self):
        # type: () -> constants.SigByteOrdr
        """:any:`SigByteOrdr`: Signal byte order in the frame payload.

        This property defines how signal bytes are ordered in the frame payload when the frame is loaded in memory.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.
        *   Set a value using the nxdbSetProperty function.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return constants.SigByteOrdr(_props.get_signal_byte_ordr(self._handle))

    @byte_ordr.setter
    def byte_ordr(self, value):
        # type: (constants.SigByteOrdr) -> None
        _props.set_signal_byte_ordr(self._handle, value.value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the signal object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_signal_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_comment(self._handle, value)

    @property
    def data_type(self):
        # type: () -> constants.SigDataType
        """:any:`SigDataType`: Get or set the signal data type.

        This property determines how the bits of a signal in a frame must be interpreted to build a value.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.
        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return constants.SigDataType(_props.get_signal_data_type(self._handle))

    @data_type.setter
    def data_type(self, value):
        # type: (constants.SigDataType) -> None
        _props.set_signal_data_type(self._handle, value.value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the signal's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def dbc_signal_value_table(self):
        # type: () -> _dbc_signal_value_table.DbcSignalValueTable
        """:any:`DbcSignalValueTable`: Access the signal's DBC value table."""
        return self._dbc_signal_value_table

    @property
    def default(self):
        # type: () -> float
        """float: Get or set the signal default value, specified as scaled floating-point units.

        The initial value of this property comes from the database.
        If the database does not provide a value, this property uses a default value of 0.0.

        For all three signal output sessions,
        this property is used when a frame transmits prior to writing to a session.
        The :any:`Frame.default_payload` property is used as the initial payload,
        then the default value of each signal is mapped into that payload using this property,
        and the result is used for the frame transmit.

        For all three signal input sessions,
        this property is returned for each signal when reading a session prior to receiving the first frame.

        For more information about when this property is used,
        refer to the discussion of read and write for each session mode.
        """
        return _props.get_signal_default(self._handle)

    @default.setter
    def default(self, value):
        # type: (float) -> None
        _props.set_signal_default(self._handle, value)

    @property
    def frame(self):
        # type: () -> _frame.Frame
        """:any:`Frame<_frame.Frame>`: Returns the signal parent frame object.

        The parent frame is defined when the signal object is created. You cannot change it afterwards.
        """
        from nixnet.database import _frame  # NOQA: F811
        ref = _props.get_signal_frame_ref(self._handle)
        return _frame.Frame(_handle=ref)

    @property
    def max(self):
        # type: () -> float
        """float: Get or set the scaled signal value maximum.

        Session read and write methods do not limit the signal value to a maximum value.
        Use this database property to set the maximum value.
        """
        return _props.get_signal_max(self._handle)

    @max.setter
    def max(self, value):
        # type: (float) -> None
        _props.set_signal_max(self._handle, value)

    @property
    def min(self):
        # type: () -> float
        """float: The scaled signal value minimum.

        Session read and write methods do not limit the signal value to a minimum value.
        Use this database property to set the minimum value.
        """
        return _props.get_signal_min(self._handle)

    @min.setter
    def min(self, value):
        # type: (float) -> None
        _props.set_signal_min(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set a string identifying a signal object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A signal name must be unique for all signals in a frame.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database, cluster, and frame name.
        It is for display purposes.
        """
        return _props.get_signal_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a signal name unique to the cluster that contains the signal.

        If the single name is not unique within the cluster,
        the name is <frame-name>.<signal-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find` because it may be not unique in the cluster.
        """
        return _props.get_signal_name_unique_to_cluster(self._handle)

    @property
    def num_bits(self):
        # type: () -> int
        """int: The number of bits the signal uses in the frame payload.

        IEEE Float numbers are limited to 32 bit or 64 bit.

        Integer (signed and unsigned) numbers are limited to 1-52 bits.
        NI-XNET converts all integers to doubles (64-bit IEEE Float).
        Integer numbers with more than 52 bits
        (the size of the mantissa in a 64-bit IEEE Float)
        cannot be converted exactly to double, and vice versa; therefore,
        NI-XNET does not support this.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.
        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_signal_num_bits(self._handle)

    @num_bits.setter
    def num_bits(self, value):
        # type: (int) -> None
        _props.set_signal_num_bits(self._handle, value)

    @property
    def pdu(self):
        # type: () -> _pdu.Pdu
        """:any:`Pdu`: Returns to the signal's parent PDU.

        The parent PDU is defined when the signal object is created.
        You cannot change it afterwards.
        """
        from nixnet.database import _pdu  # NOQA: F811
        ref = _props.get_signal_pdu_ref(self._handle)
        return _pdu.Pdu(_handle=ref)

    @property
    def scale_fac(self):
        # type: () -> float
        """float: Get or set factor `a` for linear scaling `ax+b`.

        Linear scaling is applied to all signals with the IEEE Float data type,
        unsigned and signed.
        For identical scaling 1.0x+0.0,
        NI-XNET optimized scaling routines do not perform the multiplication and addition
        """
        return _props.get_signal_scale_fac(self._handle)

    @scale_fac.setter
    def scale_fac(self, value):
        # type: (float) -> None
        _props.set_signal_scale_fac(self._handle, value)

    @property
    def scale_off(self):
        # type: () -> float
        """float: Get or set offset `b` for linear scaling `ax+b`.

        Linear scaling is applied to all signals with the IEEE Float data type,
        unsigned and signed.
        For identical scaling 1.0x+0.0,
        NI-XNET optimized scaling routines do not perform the multiplication and addition
        """
        return _props.get_signal_scale_off(self._handle)

    @scale_off.setter
    def scale_off(self, value):
        # type: (float) -> None
        _props.set_signal_scale_off(self._handle, value)

    @property
    def start_bit(self):
        """int: Get or set the least significant signal bit position in the frame payload.

        This property determines the signal starting point in the frame.
        For the integer data type (signed and unsigned),
        it means the binary signal representation least significant bit position.
        For IEEE Float signals, it means the mantissa least significant bit.

        The NI-XNET Database Editor shows a graphical overview of the frame.
        It enumerates the frame bytes on the left and the byte bits on top.
        The bit number in the frame is calculated as byte number x 8 + bit number.
        The maximum bit number in a CAN or LIN frame is 63 (7 x 8 + 7);
        the maximum bit number in a FlexRay frame is 2031 (253 x 8 + 7).

        .. image:: frameoverviewsignalstartingbit12.gif

        **Frame Overview in the NI-XNET Database Editor with a Signal Starting in Bit 12**

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_signal_start_bit(self._handle)

    @start_bit.setter
    def start_bit(self, value):
        # type: (typing.Any) -> typing.Any
        _props.set_signal_start_bit(self._handle, value)

    @property
    def unit(self):
        # type: () -> typing.Text
        """str: Get or set the signal value unit.

        NI-XNET does not use the unit internally for calculations.
        You can use the string to display the signal value along with the unit.
        """
        return _props.get_signal_unit(self._handle)

    @unit.setter
    def unit(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_unit(self._handle, value)

    @property
    def mux_is_data_mux(self):
        # type: () -> bool
        """bool: Get or set whether this signal is a multiplexer signal.

        A frame containing a multiplexer value is called a multiplexed frame.

        A multiplexer defines an area within the frame to contain different information
        (dynamic signals) depending on the multiplexer signal value.
        Dynamic signals with a different multiplexer value
        (defined in a different subframe)
        can share bits in the frame payload.
        The multiplexer signal value determines which dynamic signals are transmitted in the given frame.

        To define dynamic signals in the frame transmitted with a given multiplexer value,
        you first must create a subframe in this frame and set the multiplexer value in the subframe.
        Then you must create dynamic signals using
        :any:`SubFrame.dyn_signals` to create child signals of this subframe.

        Multiplexer signals may not overlap other static or dynamic signals in the frame.

        Dynamic signals may overlap other dynamic signals when they have a different multiplexer value.

        A frame may contain only one multiplexer signal.

        The multiplexer signal is not scaled.
        Scaling factor and offset do not apply.

        In NI-CAN, the multiplexer signal was called mode channel.
        """
        return _props.get_signal_mux_is_data_mux(self._handle)

    @mux_is_data_mux.setter
    def mux_is_data_mux(self, value):
        # type: (bool) -> None
        _props.set_signal_mux_is_data_mux(self._handle, value)

    @property
    def mux_is_dynamic(self):
        # type: () -> bool
        """bool: returns whether this signal is a dynamic signal.

        Use this property to determine if a signal is static or dynamic.
        Dynamic signals are transmitted in the frame when the multiplexer signal
        in the frame has a given value specified in the subframe.
        Use the :any:`Signal.mux_value` property to determine with which
        multiplexer value the dynamic signal is transmitted.

        This property is read only.
        To create a dynamic signal,
        create the signal object as a child of a subframe instead of a frame.
        The dynamic signal cannot be changed to a static signal afterwards.

        In NI-CAN, dynamic signals were called mode-dependent signals.
        """
        return _props.get_signal_mux_is_dynamic(self._handle)

    @property
    def mux_value(self):
        # type: () -> int
        """int: Returns the multiplexer value of a dynamic signal.

        The multiplexer value applies to dynamic signals only
        (when :any:`Signal.mux_is_dynamic` is ``True``).
        This property defines which multiplexer value is transmitted in the
        multiplexer signal when this dynamic signal is transmitted in the frame.

        The multiplexer value is determined in the subframe.
        All dynamic signals that are children of the same subframe object use the same multiplexer value.

        Dynamic signals with the same multiplexer value may not overlap each other,
        the multiplexer signal, or static signals.
        """
        return _props.get_signal_mux_value(self._handle)

    @property
    def mux_subfrm(self):
        # type: () -> _subframe.SubFrame
        """:any:`SubFrame`: Returns the subframe parent.

        This property is valid only for dynamic signals that have a subframe parent.
        For static signals or the multiplexer signal,
        this property raises an :any:`XnetError` exception.

        Raises:
            :any:`XnetError`: The signal does not have a subframe parent.
        """
        from nixnet.database import _subframe  # NOQA: F811
        ref = _props.get_signal_mux_subfrm_ref(self._handle)
        if ref == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_FRAME_NOT_FOUND)

        return _subframe.SubFrame(_handle=ref)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/_subframe.py sha256=e52412e945e3bcf092980b4f0ae7cdfc9caf04efa0f305970b3f49281176e8a4 bytes=9004 -->
## FILE: nixnet/database/_subframe.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/_subframe.py`
- sha256: `e52412e945e3bcf092980b4f0ae7cdfc9caf04efa0f305970b3f49281176e8a4`
- bytes: 9004

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object
from nixnet.database import _frame

# workaround to avoid circular imports caused by mypy type annotations
MYPY = False
if MYPY:
    from nixnet.database import _pdu  # NOQA: F401


class SubFrame(_database_object.DatabaseObject):
    """Database subframe"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

        from nixnet.database import _signal
        self._dyn_signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_SUBFRM_DYN_SIG_REFS, _signal.Signal)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def check_config_status(self):
        # type: () -> None
        """Check this subframe's configuration status.


        By default, incorrectly configured subframes in the database are not returned from
        :any:`Frame.mux_subframes` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a subframe configuration status becomes invalid after the database is opened,
        the subframe still is returned from :any:`Frame.mux_subframes`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The subframe is incorrectly configured.
        """
        status_code = _props.get_subframe_config_status(self._handle)
        _errors.check_for_error(status_code)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    @property
    def dyn_signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of dynamic :any:`Signal<_signal.Signal>` objects in the subframe.

        Those signals are transmitted when the multiplexer signal
        in the frame has the multiplexer value defined in the subframe.
        """
        return self._dyn_signals

    @property
    def frm(self):
        # type: () -> _frame.Frame
        """:any:`Frame<_frame.Frame>`: Returns the reference to the parent frame.

        The parent frame is defined when the subframe is created,
        and you cannot change it afterwards.
        """
        handle = _props.get_subframe_frm_ref(self._handle)
        return _frame.Frame(_handle=handle)

    @property
    def mux_value(self):
        # type: () -> int
        """int: Get or set the multiplexer value for this subframe.

        This property specifies the multiplexer signal value used when the
        dynamic signals in this subframe are transmitted in the frame.
        Only one subframe is transmitted at a time in the frame.

        There also is a multiplexer value for a signal object as a read-only property.
        It reflects the value set on the parent subframe object.

        This property is required. If the property does not contain a valid value,
        and you create an XNET session that uses this subframe,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_subframe_mux_value(self._handle)

    @mux_value.setter
    def mux_value(self, value):
        # type: (int) -> None
        _props.set_subframe_mux_value(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the subframe object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A subframe name must be unique for all subframes in a frame.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database, cluster, and frame name. It is for display purposes.
        """
        return _props.get_subframe_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_subframe_name(self._handle, value)

    @property
    def pdu(self):
        # type: () -> _pdu.Pdu
        """:any:`Pdu`: Returns the subframe's parent PDU.

        This property returns the reference to the subframe's parent PDU.
        The parent PDU is defined when the subframe object is created.
        You cannot change it afterwards.
        """
        from nixnet.database import _pdu  # NOQA: F811
        handle = _props.get_subframe_pdu_ref(self._handle)
        return _pdu.Pdu(_handle=handle)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a subframe name unique to the cluster that contains the subframe.

        If the single name is not unique within the cluster, the name is <frame-name>.<subframe-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find`
        because it may be not unique in the cluster.
        """
        return _props.get_subframe_name_unique_to_cluster(self._handle)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/database/database.py sha256=06f44b1ed1fbc3c01342511c1bc293a190357d368ee14e9b8b49707854075e47 bytes=11516 -->
## FILE: nixnet/database/database.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/database/database.py`
- sha256: `06f44b1ed1fbc3c01342511c1bc293a190357d368ee14e9b8b49707854075e47`
- bytes: 11516

````python
import typing  # NOQA: F401
import warnings

from nixnet import _cconsts
from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors

from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object


class Database(_database_object.DatabaseObject):
    """Opens a database file.

    When an already open database is opened,
    this class grants access to the same database and increases an internal reference counter.
    A multiple referenced (open) database must be closed as many times as it has been opened.
    Until it is completely closed, the access to this database remains granted,
    and the database uses computer resources (memory and handles).
    For more information, refer to :any:`Database.close`.

    Args:
        database_name(str): The database alias or file pathname to open.
    """
    def __init__(self, database_name):
        # type: (typing.Text) -> None
        self._handle = None  # To satisfy `__del__` in case nxdb_open_database throws
        self._handle = _funcs.nxdb_open_database(database_name)

        from nixnet.database import _cluster
        self._clusters = _collection.DbCollection(
            self._handle, constants.ObjectClass.CLUSTER, _cconsts.NX_PROP_DATABASE_CLST_REFS, _cluster.Cluster)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Database was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def close(self, close_all_refs=False):
        # type: (bool) -> None
        """Closes the database.

        For the case that different threads of an application are using the same database,
        :any:`Database` and :any:`Database.close`
        maintain a reference counter indicating how many times the database is open.
        Every thread can open the database, work with it,
        and close the database independently using ``close_all_refs`` set to ``False``.
        Only the last call to :any:`Database.close` actually closes access to the database.

        .. note:: ``Database.__exit__`` calls :any:`Database.close` with ``close_all_refs`` set to ``False``.
            See examples of this in :ref:`can_dynamic_database_creation_label`
            and :ref:`lin_dynamic_database_creation_label`.

        Another option is that only one thread executes :any:`Database.close` once,
        using ``close_all_refs`` set to ``True``, which closes access for all other threads.
        This may be convenient when, for example,
        the main program needs to stop all running threads
        and be sure the database is closed properly,
        even if some threads could not execute :any:`Database.close`.

        Args:
            close_all_refs(bool): Indicates that a database open multiple times
                (refer to :any:`Database`) should be closed completely
                (``close_all_refs`` is ``True``),
                or just the reference counter should be decremented
                (``close_all_refs`` is ``False``),
                and the database remains open.
                When the database is closed completely,
                all references to objects in this database become invalid.
        """
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET database but database was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nxdb_close_database(self._handle, close_all_refs)
        self._handle = None

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)  # type: ignore

    def save(self, db_filepath=""):
        # type: (typing.Text) -> None
        """Saves the open database to a FIBEX 3.1.0 file.

        The file extension must be .xml. If the target file exists, it is overwritten.

        XNET saves to the FIBEX file only features that XNET sessions use to communicate on the network.
        If the original file was created using non-XNET software,
        the target file may be missing details from the original file.
        For example, NI-XNET supports only linear scaling.
        If the original FIBEX file used a rational equation that cannot be expressed as a linear scaling,
        XNET converts this to a linear scaling with factor 1.0 and offset 0.0.

        If ``db_filepath`` is empty, the file is saved to the same FIBEX file specified when opened.
        If opened as a file path, it uses that file path.
        If opened as an alias, it uses the file path registered for that alias.

        Saving a database is not supported under Real-Time (RT),
        but you can deploy and use a database saved on Windows on a Real-Time (RT) target (refer to `Database.deploy`).

        Args:
            db_filepath(str): Contains the pathname to the database file or is
                empty (saves to the original filepath).
        """
        _funcs.nxdb_save_database(self._handle, db_filepath)  # type: ignore

    @property
    def name(self):
        # type: () -> typing.Text
        return _props.get_database_name(self._handle)  # type: ignore

    @property
    def clusters(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Cluster` objects in this database.

        A cluster is assigned to a database when the cluster object is created.
        You cannot change this assignment afterwards.

        FIBEX and AUTOSAR files can contain any number of clusters,
        and each cluster uses a unique name.

        For CANdb (.dbc), LDF (.ldf), or NI-CAN (.ncd) files,
        the file contains only one cluster, and no cluster name is stored in the file.
        For these database formats, NI-XNET uses the name Cluster for the single cluster.
        """
        return self._clusters

    @property
    def show_invalid_from_open(self):
        # type: () -> bool
        """bool: Show or hide :any:`Frame<_frame.Frame>` and :any:`Signal<_signal.Signal>` objects that are invalid.

        After opening a database, this property always is set to ``False``,
        meaning that invalid :any:`Cluster`, :any:`Frame<_frame.Frame>`,
        and :any:`Signal<_signal.Signal>` objects
        are not returned in properties that return a :any:`DbCollection` for the database
        (for example, :any:`Cluster.frames` and :any:`Frame.mux_static_signals`).
        Invalid :any:`Cluster`, :any:`Frame<_frame.Frame>`,
        and :any:`Signal<_signal.Signal>` objects are incorrectly defined
        and therefore cannot be used in the bus communication.
        The ``False`` setting is recommended when you use the database to create XNET sessions.

        In case the database was opened to correct invalid configuration
        (for example, in a database editor),
        you must set the property to ``True`` prior to reading properties that return
        a :any:`DbCollection` for the database
        (for example, :any:`Cluster.frames` and :any:`Frame.mux_static_signals`).

        For invalid objects,
        the :any:`Cluster.check_config_status`,
        :any:`Frame.check_config_status`,
        and :any:`Signal.check_config_status` methods raise an exception if there is a problem.
        For valid objects, no error is raised.

        :any:`Cluster`, :any:`Frame<_frame.Frame>`, and :any:`Signal<_signal.Signal>` objects that became
        invalid after the database is opened are still returned from the
        :any:`Database.clusters`, :any:`Cluster.frames`, and :any:`Frame.mux_static_signals`,
        even if :any:`Database.show_invalid_from_open` is ``False``
        and Configuration Status returns an error code.
        For example, if you open a :any:`Frame<_frame.Frame>` with valid properties,
        then you set :any:`Signal.start_bit` beyond the :any:`Frame.payload_len`,
        :any:`Frame.check_config_status` raises an exception,
        but the frame is returned from :any:`Cluster.frames`.
        """
        return _props.get_database_show_invalid_from_open(self._handle)  # type: ignore

    @show_invalid_from_open.setter
    def show_invalid_from_open(self, value):
        # type: (bool) -> None
        _props.set_database_show_invalid_from_open(self._handle, value)  # type: ignore
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/errors.py sha256=b1956ef15e3cc52728c1500328c4bc7dc6965814396be9cf775d84e020357c88 bytes=2509 -->
## FILE: nixnet/errors.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/errors.py`
- sha256: `b1956ef15e3cc52728c1500328c4bc7dc6965814396be9cf775d84e020357c88`
- bytes: 2509

````python
import typing  # NOQA: F401
import warnings

from nixnet import _enums

__all__ = ['XnetError', 'XnetWarning', 'XnetResourceWarning']


class Error(Exception):
    """Base error class for module."""
    pass


class XnetError(Error):
    """Error raised by any NI-XNET method."""
    def __init__(
        self,
        message,  # type: typing.Text
        error_code,  # type: int
    ):
        # type: (...) -> None
        """Initialize error.

        Args:
            message(str): Error message.
            error_code(int): NI-XNET error code.
        """
        super(XnetError, self).__init__(message)

        self._error_code = error_code

        try:
            self._error_type = _enums.Err(self._error_code)
        except ValueError:
            self._error_type = _enums.Err.INTERNAL_ERROR

    @property
    def error_code(self):
        # type: (...) -> int
        """int: Error code reported by NI-XNET."""
        return self._error_code

    @property
    def error_type(self):
        # type: (...) -> _enums.Err
        """:any:`nixnet._enums.Err`: Error type reported by NI-XNET."""
        return self._error_type


class XnetWarning(Warning):
    """Warning raised by any NI-XNET method."""
    def __init__(
        self,
        message,  # type: typing.Text
        warning_code,  # type: int
    ):
        # type: (...) -> None
        """Initialize warning.

        Args:
            message(str): Warning message.
            warning_code(int): NI-XNET warning code.
        """
        super(XnetWarning, self).__init__(
            'Warning {0} occurred.\n\n{1}'.format(warning_code, message))

        self._warning_code = warning_code

        try:
            self._warning_type = _enums.Warn(self._warning_code)  # type: typing.Optional[_enums.Warn]
        except ValueError:
            self._warning_type = None

    @property
    def warning_code(self):
        # type: (...) -> int
        """int: Warning code reported by NI-XNET."""
        return self._warning_code

    @property
    def warning_type(self):
        # type: (...) -> typing.Optional[_enums.Warn]
        """:any:`nixnet._enums.Warn`: Warning type reported by NI-XNET."""
        return self._warning_type


XnetResourceWarning = ResourceWarning  # type: typing.Type[Warning]
warnings.filterwarnings("always", category=XnetWarning)
warnings.filterwarnings("always", category=XnetResourceWarning)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/session.py sha256=6b822bbe9280537468f0bb4dfc1236c3d1bb19ecbe799793c4243014fb299fd3 bytes=28616 -->
## FILE: nixnet/session.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/session.py`
- sha256: `6b822bbe9280537468f0bb4dfc1236c3d1bb19ecbe799793c4243014fb299fd3`
- bytes: 28616

````python
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import _utils
from nixnet import constants

from nixnet._session import base
from nixnet._session import frames as session_frames
from nixnet._session import signals as session_signals


__all__ = [
    "FrameInStreamSession",
    "FrameOutStreamSession",
    "FrameInQueuedSession",
    "FrameOutQueuedSession",
    "FrameInSinglePointSession",
    "FrameOutSinglePointSession",
    "SignalInSinglePointSession",
    "SignalOutSinglePointSession"]


class FrameInStreamSession(base.SessionBase):
    """Frame Input Stream session.

    This session reads all frames received from the network using a single
    stream.

    The input data is returned as a list of frames. Because all frames are
    returned, your application must evaluate identification in each frame (such
    as a CAN identifier or FlexRay slot/cycle/channel) to interpret the frame
    payload data.

    Previously, you could use only one Frame Input Stream session for a given
    interface. Now, multiple Frame Input Stream sessions can be open at the same
    time on CAN and LIN interfaces.

    While using one or more Frame Input Stream sessions, you can use other
    sessions with different input modes. Received frames are copied to Frame
    Input Stream sessions in addition to any other applicable input session. For
    example, if you create a Frame Input Single-Point session for frame_a, then
    create a Frame Input Stream session, when frame_a is received, its data is
    returned from the call to read function of both sessions. This duplication
    of incoming frames enables you to analyze overall traffic while running a
    higher level application that uses specific frame or signal data.

    When used with a FlexRay interface, frames from both channels are returned.
    For example, if a frame is received in a static slot on both channel A and
    channel B, two frames are returned from the read function.

    .. note:: Typical use case: Analyzing and/or logging all frame traffic in
       the network.
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name=':memory:',  # type: typing.Text
            cluster_name='',  # type: typing.Text
    ):
        # type: (...) -> None
        """Create a Frame Input Stream session.

        This function creates a Frame Input Stream session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter.
        """
        flattened_list = _utils.flatten_items(None)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_STREAM)
        self._frames = session_frames.InFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.InFrames
        """:any:`nixnet._session.frames.InFrames`: Operate on session's frames"""
        return self._frames


class FrameOutStreamSession(base.SessionBase):
    """Frame Output Stream session.

    This session transmits an arbitrary sequence of frame values using a single
    stream. The values are not limited to a single frame in the database, but
    can transmit any frame.

    The data passed to the write frame function is a list of frame values,
    each of which transmits as soon as possible. Frames transmit sequentially
    (one after another).

    Like Frame Input Stream sessions, you can create more than one Frame Output
    Stream session for a given interface.

    For CAN, frame values transmit on the network based entirely on the time
    when you call the write frame function. The timing of each frame as
    specified in the database is ignored. For example, if you provide four frame
    values to the the write frame function, the first frame value transmits
    immediately, followed by the next three values transmitted back to back. For
    this session, the CAN frame payload length in the database is ignored, and
    the write frame function is always used.

    Similarly for LIN, frame values transmit on the network based entirely on
    the time when you call the write frame function. The timing of each frame as
    specified in the database is ignored. The LIN frame payload length in the
    database is ignored, and the write frame function is always used. For LIN,
    this session/mode is allowed only on the interface as master. If the payload
    for a frame is empty, only the header part of the frame is transmitted. For
    a nonempty payload, the header + response for the frame is transmitted. If a
    frame for transmit is defined in the database (in-memory or otherwise), it
    is transmitted using its database checksum type. If the frame for transmit
    is not defined in the database, it is transmitted using enhanced checksum.

    This session is not supported for FlexRay.

    The frame values for this session are stored in a queue, such that every value
    provided is transmitted.
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name=':memory:',  # type: typing.Text
            cluster_name='',  # type: typing.Text
    ):
        # type: (...) -> None
        """Create a Frame Input Stream session.

        This function creates a Frame Output Stream session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter.
        """
        flattened_list = _utils.flatten_items(None)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_STREAM)
        self._frames = session_frames.OutFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.OutFrames
        """:any:`nixnet._session.frames.InFrames`: Operate on session's frames"""
        return self._frames


class FrameInQueuedSession(base.SessionBase):
    """Frame Input Queued session.

    This session reads data from a dedicated queue per frame. It enables your
    application to read a sequence of data specific to a frame (for example, a
    CAN identifier).

    You specify only one frame for the session, and the read frame function
    returns values for that frame only. If you need sequential data for multiple
    frames, create multiple sessions, one per frame.

    The input data is returned as a list of frame values. These values
    represent all values received for the frame since the previous call to the
    read frame function.
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            frame,  # type: typing.Text
    ):
        # type: (...) -> None
        """Create a Frame Input Queued session.

        This function creates a Frame Input Queued session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``frame`` parameter.
            frame(str): XNET Frame or PDU name. This name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    - ``<Frame>``
                    - ``<Cluster>.<Frame>``
                    - ``<PDU>``
                    - ``<Cluster>.<PDU>``
        """
        flattened_list = _utils.flatten_items(frame)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_QUEUED)
        self._frames = session_frames.InFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.InFrames
        """:any:`nixnet._session.frames.InFrames`: Operate on session's frames"""
        return self._frames


class FrameOutQueuedSession(base.SessionBase):
    """Frame Output Queued session.

    This session provides a sequence of values for a single frame, for transmit
    using that frame's timing as specified in the database.

    The output data is provided as a list of frame values, to be transmitted
    sequentially for the frame specified in the session.

    You can only specify one frame for this session. To transmit sequential
    values for multiple frames, use a different Frame Output Queued session for
    each frame or use the Frame Output Stream session.

    The frame values for this session are stored in a queue, such that every
    value provided is transmitted.

    For this session, NI-XNET transmits each frame according to its properties
    in the database. Therefore, when you call the write frame function, the
    number of payload bytes in each frame value must match that frame's Payload
    Length property. The other frame value elements are ignored, so you can
    leave them uninitialized. For CAN interfaces, if the number of payload bytes
    you write is smaller than the Payload Length configured in the database, the
    requested number of bytes transmits. If the number of payload bytes is
    larger than the Payload Length configured in the database, the queue is
    flushed and no frames transmit. For other interfaces, transmitting a number
    of payload bytes different than the frame's payload may cause unexpected
    results on the bus.
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            frame,  # type: typing.Text
    ):
        # type: (...) -> None
        """Create a Frame Output Queued session.

        This function creates a Frame Output Stream session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``frame`` parameter.
            frame(str): XNET Frame or PDU name. This name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    - ``<Frame>``
                    - ``<Cluster>.<Frame>``
                    - ``<PDU>``
                    - ``<Cluster>.<PDU>``
        """
        flattened_list = _utils.flatten_items(frame)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_QUEUED)
        self._frames = session_frames.OutFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.OutFrames
        """:any:`nixnet._session.frames.OutFrames`: Operate on session's frames"""
        return self._frames


class FrameInSinglePointSession(base.SessionBase):
    """Frame Input Single-Point session.

    This session reads the most recent value received for each frame.

    This session does not use queues to store each received frame. If the
    interface receives two frames prior to calling the read frame function, that
    read returns signals for the second frame.

    The input data is returned as a list of frames, one for each frame
    specified for the session.

    .. note:: Typical use case: Control or simulation applications that require
       lower level access to frames (not signals).
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            frames,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create a Frame Input Single-Point session.

        This function creates a Frame Input Single-Point session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``frames`` parameter.
            frames(list of str): Strings describing frames for the session. The
                list syntax is as follows:

                List contains one or more XNET Frame or PDU names. Each name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    - ``<Frame>``
                    - ``<Cluster>.<Frame>``
                    - ``<PDU>``
                    - ``<Cluster>.<PDU>``
        """
        flattened_list = _utils.flatten_items(frames)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_SINGLE_POINT)
        self._frames = session_frames.SinglePointInFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.SinglePointInFrames
        """:any:`nixnet._session.frames.InFrames`: Operate on session's frames"""
        return self._frames


class FrameOutSinglePointSession(base.SessionBase):
    """Frame Output Single-Point session.

    This session writes frame values for the next transmit.

    This session does not use queues to store frame values. If the write frame
    function is called twice before the next transmit, the transmitted frame
    uses the value from the second call to the write frame function.

    The output data is provided as a list of frames, one for each frame
    specified for the session.

    For this session, NI-XNET transmits each frame according to its properties
    in the database. Therefore, when you call the write frame function, the
    number of payload bytes in each frame value must match that frame's Payload
    Length property. The other frame value elements are ignored, so you can
    leave them uninitialized. For CAN interfaces, if the number of payload bytes
    you write is smaller than the Payload Length configured in the database, the
    requested number of bytes transmit. If the number of payload bytes is larger
    than the Payload Length configured in the database, the queue is flushed and
    no frames transmit. For other interfaces, transmitting a number of payload
    bytes different than the frame payload may cause unexpected results on the bus.

    .. note:: Typical use case: Control or simulation applications that require lower level access
       to frames (not signals).
    """
    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            frames,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create a Frame Output Single-Point session.

        This function creates a Frame Output Single-Point session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``frames`` parameter.
            frames(list of str): Strings describing frames for the session. The
                list syntax is as follows:

                List contains one or more XNET Frame or PDU names. Each name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    - ``<Frame>``
                    - ``<Cluster>.<Frame>``
                    - ``<PDU>``
                    - ``<Cluster>.<PDU>``
        """
        flattened_list = _utils.flatten_items(frames)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_SINGLE_POINT)
        self._frames = session_frames.SinglePointOutFrames(self._handle)  # type: ignore

    @property
    def frames(self):
        # type: () -> session_frames.SinglePointOutFrames
        """:any:`nixnet._session.frames.InFrames`: Operate on session's frames"""
        return self._frames


class SignalInSinglePointSession(base.SessionBase):
    """Signal Input Single-Point session.

    This session reads the most recent value received for each signal.

    This session does not use queues to store each received frame. If the
    interface receives two frames prior to calling
    :any:`nixnet._session.signals.SinglePointInSignals.read`, that call to
    :any:`nixnet._session.signals.SinglePointInSignals.read` returns signals
    for the second frame.

    Use :any:`nixnet._session.signals.SinglePointInSignals.read` for this session.

    You also can specify a trigger signal for a frame. This signal name is
    :trigger:.<frame name>, and once it is specified in the __init__ ``signals``
    list, it returns a value of 0.0 if the frame did not arrive since the last
    Read (or Start), and 1.0 if at least one frame of this ID arrived. You can
    specify multiple trigger signals for different frames in the same session.
    For multiplexed signals, a signal may or may not be contained in a received
    frame. To define a trigger signal for a multiplexed signal, use the signal
    name :trigger:.<frame name>.<signal name>. This signal returns 1.0 only if a
    frame with appropriate set multiplexer bit has been received since the last
    Read or Start.

    .. note:: Typical use case: Control or simulation applications, such as
       Hardware In the Loop (HIL).
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            signals,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create a Signal Input Single-Point session.

        This function creates a Signal Input Single-Point session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``signals`` parameter.
            signals(list of str): Strings describing signals for the session. The
                list syntax is as follows:

                ``signals`` contains one or more XNET Signal names. Each name must
                be one of the following options, whichever uniquely
                identifies a signal within the database given:

                    - ``<Signal>``
                    - ``<Frame>.<Signal>``
                    - ``<Cluster>.<Frame>.<Signal>``
                    - ``<PDU>.<Signal>``
                    - ``<Cluster>.<PDU>.<Signal>``

                ``signals`` may also contain one or more trigger signals. For
                information about trigger signals, refer to Signal Output
                Single-Point Mode or Signal Input Single-Point Mode.
        """
        flattened_list = _utils.flatten_items(signals)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.SIGNAL_IN_SINGLE_POINT)
        self._signals = session_signals.SinglePointInSignals(self._handle)  # type: ignore

    @property
    def signals(self):
        # type: () -> session_signals.SinglePointInSignals
        """:any:`nixnet._session.signals.SinglePointInSignals`: Operate on session's signals"""
        return self._signals


class SignalOutSinglePointSession(base.SessionBase):
    """Signal Out Single-Point session.

    This session writes signal values for the next frame transmit.

    This session does not use queues to store signal values. If
    :any:`nixnet._session.signals.SinglePointOutSignals.write` is called twice
    before the next transmit, the transmitted frame uses signal values from the
    second call to :any:`nixnet._session.signals.SinglePointOutSignals.write`.

    Use :any:`nixnet._session.signals.SinglePointOutSignals.write` for this session.

    You also can specify a trigger signal for a frame. This signal name is
    :trigger:.<frame name>, and once it is specified in the __init__ ``signals``
    list, you can write a value of 0.0 to suppress writing of that frame, or any
    value not equal to 0.0 to write the frame. You can specify multiple trigger
    signals for different frames in the same session.

    .. note:: Typical use case: Control or simulation applications, such as
       Hardware In the Loop (HIL).
    """

    def __init__(
            self,
            interface_name,  # type: typing.Text
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            signals,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create a Signal Output Single-Point session.

        This function creates a Signal Output Single-Point session using the named
        references to database objects.

        Args:
            interface_name(str): XNET Interface name to use for
                this session.
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``signals`` parameter.
            signals(list of str): Strings describing signals for the session. The
                list syntax is as follows:

                ``signals`` contains one or more XNET Signal names. Each name must
                be one of the following options, whichever uniquely
                identifies a signal within the database given:

                    - ``<Signal>``
                    - ``<Frame>.<Signal>``
                    - ``<Cluster>.<Frame>.<Signal>``
                    - ``<PDU>.<Signal>``
                    - ``<Cluster>.<PDU>.<Signal>``

                ``signals`` may also contain one or more trigger signals. For
                information about trigger signals, refer to Signal Output
                Single-Point Mode or Signal Output Single-Point Mode.
        """
        flattened_list = _utils.flatten_items(signals)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.SIGNAL_OUT_SINGLE_POINT)
        self._signals = session_signals.SinglePointOutSignals(self._handle)  # type: ignore

    @property
    def signals(self):
        # type: () -> session_signals.SinglePointOutSignals
        """:any:`nixnet._session.signals.SinglePointInSignals`: Operate on session's signals"""
        return self._signals


def create_session_by_ref(
        database_refs,
        interface_name,
        mode):
    return _funcs.nx_create_session_by_ref(database_refs, interface_name, mode)


def read_signal_waveform(
        session_ref,
        timeout,
        start_time,
        delta_time,
        value_buffer,
        size_of_value_buffer,
        number_of_values_returned):
    raise NotImplementedError("Placeholder")


def read_signal_xy(
        session_ref,
        time_limit,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


def write_signal_waveform(
        session_ref,
        timeout,
        value_buffer):
    _funcs.nx_write_signal_waveform(session_ref, timeout, value_buffer)


def write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        timestamp_buffer,
        num_pairs_buffer):
    _funcs.nx_write_signal_xy(session_ref, timeout, value_buffer, timestamp_buffer, num_pairs_buffer)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/__init__.py sha256=1e29fc74475f69202869ebcde84403f473fe1dfa2a2a736b97e2ff4c9146c387 bytes=67 -->
## FILE: nixnet/system/__init__.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/__init__.py`
- sha256: `1e29fc74475f69202869ebcde84403f473fe1dfa2a2a736b97e2ff4c9146c387`
- bytes: 67

````python
from nixnet.system.system import System


__all__ = ["System"]
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/_collection.py sha256=45801865c15219fe1158ad526b1a93b8d6cd0351fbe4bba5536441498375143e bytes=1306 -->
## FILE: nixnet/system/_collection.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/_collection.py`
- sha256: `45801865c15219fe1158ad526b1a93b8d6cd0351fbe4bba5536441498375143e`
- bytes: 1306

````python
from collections.abc import Iterable
from collections.abc import Sized
import typing  # NOQA: F401

from nixnet import _cprops


class SystemCollection(Iterable, Sized):
    """Collection of System related objects."""

    def __init__(self, handle, prop_id, factory):
        # type: (int, int, typing.Any) -> None
        self._handle = handle
        self._prop_id = prop_id
        self._factory = factory

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            sys_other = typing.cast(SystemCollection, other)
            return self._handle == sys_other._handle and self._prop_id == sys_other._prop_id
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return _cprops.get_session_ref_array_len(self._handle, self._prop_id)

    def __iter__(self):
        for ref in _cprops.get_session_ref_array(self._handle, self._prop_id):
            yield self._factory(ref)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/_databases.py sha256=3d9595da4f9e8c362cbf1bd408a44ea81672b52ecaf3b42b0f4435d4536521ba bytes=7308 -->
## FILE: nixnet/system/_databases.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/_databases.py`
- sha256: `3d9595da4f9e8c362cbf1bd408a44ea81672b52ecaf3b42b0f4435d4536521ba`
- bytes: 7308

````python
from collections.abc import Mapping
import typing  # NOQA: F401

import six

from nixnet import _funcs


class AliasCollection(Mapping):
    """Alias aliases."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(AliasCollection, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return self._get_database_len('')

    def __iter__(self):
        return self.keys()

    def __getitem__(self, index):
        # type: (typing.Text) -> Alias
        """Return the Alias object associated with the specified alias.

            Args:
                index(str): The value of the index (alias name).
        """
        if isinstance(index, six.string_types):
            for alias, filepath in self._get_database_list(''):
                if alias == index:
                    return self._create_item(alias, filepath)
            else:
                raise KeyError('Alias alias %s not found in the system' % index)
        else:
            raise TypeError(index)

    def __delitem__(self, index):
        # type: (typing.Text) -> None
        """Delete/Remove a database alias from the system.

        This function removes the alias from NI-XNET, but does not affect the
        database text file. It just removes the alias association to the
        database file path.

        This function is supported on Windows only, and the alias is removed
        from Windows only (not RT targets). Use 'undeploy' to remove an alias
        from a Real-Time (RT) target.

        Args:
            index(str): The name of the alias to delete.
        """
        _funcs.nxdb_remove_alias(index)

    def keys(self):
        """Return all keys (alias names) used in the AliasCollection object.

            Yields:
                An iterator to all the keys in the Alias object.
        """
        for alias, _ in self._get_database_list(''):
            yield alias

    def values(self):
        """Return all Alias objects in the system.

            Yields:
                An iterator to all the values in the AliasCollection object.
        """
        for alias, filepath in self._get_database_list(''):
            yield self._create_item(alias, filepath)

    def items(self):
        """Return all aliases and database objects associated with those aliases in the system.

            Yields:
                An iterator to tuple pairs of alias and database objects in the system.
        """
        for alias, filepath in self._get_database_list(''):
            yield alias, self._create_item(alias, filepath)

    def add_alias(self, database_alias, database_filepath, default_baud_rate=None):
        # type: (typing.Text, typing.Text, typing.Optional[int]) -> None
        """Add a new alias with baud rate size of up to 64 bits to a database file.

        NI-XNET uses alias names for database files. The alias names provide a
        shorter name for display, allow for changes to the file system without
        changing the application.

        This function is supported on Windows only.

        Args:
            database_alias(str): Provides the desired alias name. Unlike the names of
                other XNET database objects, the alias name can use special
                characters such as space and dash. Commas are not allowed in the
                alias name. If the alias name already exists, this function
                changes the previous filepath to the specified filepath.
            database_filepath(str): Provides the path to the CANdb, FIBEX, or LDF
                file. Commas are not allowed in the filepath name.
            default_baud_rate(int): Provides the default baud rate, used when
                filepath refers to a CANdb database (.dbc) or an NI-CAN database
                (.ncd). These database formats are specific to CAN and do not
                specify a cluster baud rate. Use this default baud rate to
                specify a default CAN baud rate to use with this alias. If
                database_filepath refers to a FIBEX database (.xml) or LIN LDF
                file, the default_baud_rate parameter is ignored. The FIBEX and
                LDF database formats require a valid baud rate for every
                cluster, and NI-XNET uses that baud rate as the default.
        """
        if default_baud_rate is None:
            default_baud_rate = 0

        _funcs.nxdb_add_alias64(database_alias, database_filepath, default_baud_rate)

    def _create_item(self, database_alias, database_filepath):
        # type: (typing.Text, typing.Text) -> Alias
        return Alias(database_alias, database_filepath)

    @staticmethod
    def _get_database_len(ip_address):
        # type: (typing.Text) -> int
        alias_buffer_size, filepath_buffer_size = _funcs.nxdb_get_database_list_sizes(ip_address)
        _, _, number_of_databases = _funcs.nxdb_get_database_list(ip_address, alias_buffer_size, filepath_buffer_size)
        return number_of_databases

    @staticmethod
    def _get_database_list(ip_address):
        # type: (typing.Text) -> typing.List[typing.Tuple[typing.Text, typing.Text]]
        alias_buffer_size, filepath_buffer_size = _funcs.nxdb_get_database_list_sizes(ip_address)
        aliases, filepaths, _ = _funcs.nxdb_get_database_list(ip_address, alias_buffer_size, filepath_buffer_size)
        return list(zip(aliases.split(","), filepaths.split(",")))


class Alias(object):
    """Alias alias."""

    def __init__(
            self,
            database_alias,
            database_filepath,
    ):
        # type: (typing.Text, typing.Text) -> None
        self._database_alias = database_alias
        self._database_filepath = database_filepath

    def __repr__(self):
        return '{}(alias={}, filepath={})'.format(
            type(self).__name__, self._database_alias, self._database_filepath)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_db = typing.cast(Alias, other)
            return self.alias == other_db.alias and self.filepath == other_db.filepath
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self.alias)

    @property
    def alias(self):
        return self._database_alias

    @property
    def filepath(self):
        # type: () -> typing.Text
        """str: Get the filepath associated with the Alias object"""
        return self._database_filepath
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/_device.py sha256=171e2ef91ff4c9777be4c5ba3f97f5a26a14bc6e9657ccde7499905d3a4473d3 bytes=3282 -->
## FILE: nixnet/system/_device.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/_device.py`
- sha256: `171e2ef91ff4c9777be4c5ba3f97f5a26a14bc6e9657ccde7499905d3a4473d3`
- bytes: 3282

````python
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _props
from nixnet import constants

from nixnet.system import _collection
from nixnet.system import _interface


class Device(object):
    '''Physical XNET devices in the system.'''

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self._intfs = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_DEV_INTF_REFS, _interface.Interface)
        self._intfs_all = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_DEV_INTF_REFS_ALL, _interface.Interface)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Device, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    @property
    def form_fac(self):
        # type: () -> constants.DevForm
        ''':any:`nixnet._enums.DevForm`: XNET board form factor.'''
        return constants.DevForm(_props.get_device_form_fac(self._handle))

    @property
    def intf_refs(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Interfaces associated with this device.'''
        return self._intfs

    @property
    def intf_refs_all(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Interfaces associated with this device.

        This Includes those not equipped with a Transceiver Cable.
        '''
        return self._intfs_all

    @property
    def num_ports(self):
        # type: () -> int
        '''int: The number of physical port connectors on the XNET board.'''
        return _props.get_device_num_ports(self._handle)

    @property
    def num_ports_all(self):
        # type: () -> int
        '''int: The number of physical port connectors on the XNET board.

        This Includes those not equipped with a Transceiver Cable.
        '''
        return _props.get_device_num_ports_all(self._handle)

    @property
    def product_num(self):
        # type: () -> int
        '''int: The numeric portion of the XNET device product name.'''
        return _props.get_device_product_num(self._handle)

    @property
    def product_name(self):
        # type: () -> typing.Text
        '''str: The XNET device product name.'''
        return _props.get_device_name(self._handle)

    @property
    def ser_num(self):
        # type: () -> int
        '''int: Serial number associated with the XNET device.'''
        return _props.get_device_ser_num(self._handle)

    @property
    def slot_num(self):
        # type: () -> int
        '''int: Physical slot where the module is located within a chassis.'''
        return _props.get_device_slot_num(self._handle)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/_interface.py sha256=d77a6d683976574b2e3aa9b2870b4055f608a44ae4ccd03a01e766542441e8ae bytes=8319 -->
## FILE: nixnet/system/_interface.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/_interface.py`
- sha256: `d77a6d683976574b2e3aa9b2870b4055f608a44ae4ccd03a01e766542441e8ae`
- bytes: 8319

````python
import typing  # NOQA: F401

import six

from nixnet import _funcs
from nixnet import _props
from nixnet import constants


class Interface(object):
    '''Interfaces associated with a physical hardware device.'''

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Interface, other)._handle
        elif isinstance(other, six.string_types):
            return self._name == typing.cast(typing.Text, other)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __str__(self):
        # type: () -> typing.Text
        return self._name

    def __repr__(self):
        # type: () -> typing.Text
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    # `dev_ref`: Intentionally not exposed to avoid circular imports

    @property
    def num(self):
        # type: () -> int
        '''int: The unique number associated with the XNET interface.

        The XNET driver assigns each port connector in the system a unique
        number XNET driver. This number, plus its protocol name, is the
        interface name.
        '''
        return _props.get_interface_num(self._handle)

    @property
    def port_num(self):
        # type: () -> int
        '''int: Physical port number printed near the connector on the XNET device.

        The port numbers on an XNET board are physically identified with
        numbering. Use this property, along with the XNET Device Serial Number
        property, to associate an XNET interface with a physical (XNET board
        and port) combination.
        '''
        return _props.get_interface_port_num(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        ''':any:`nixnet._enums.Protocol`: Protocol supported by the interface.'''
        return constants.Protocol(_props.get_interface_protocol(self._handle))

    @property
    def can_term_cap(self):
        # type: () -> constants.CanTermCap
        ''':any:`nixnet._enums.CanTermCap`: Indicates whether the XNET interface can terminate the CAN bus.

        Signal reflections on the CAN bus can cause communication failure. To
        prevent reflections, termination can be present as external resistance
        or resistance the XNET board applies internally. This property
        determines whether the XNET board can add termination to the bus.
        '''
        return constants.CanTermCap(_props.get_interface_can_term_cap(self._handle))

    @property
    def can_tcvr_cap(self):
        # type: () -> constants.CanTcvrCap
        ''':any:`nixnet._enums.CanTcvrCap`: Indicates the CAN bus physical transceiver support.'''
        return constants.CanTcvrCap(_props.get_interface_can_tcvr_cap(self._handle))

    @property
    def dongle_state(self):
        # type: () -> constants.DongleState
        ''':any:`nixnet._enums.DongleState`: Indicates the connected Transceiver Cable's state.

        Some Transceiver Cable types require external power from the network
        connector for operation. Refer to the hardware-specific manual for more
        information.
        '''
        return constants.DongleState(_props.get_interface_dongle_state(self._handle))

    @property
    def dongle_id(self):
        # type: () -> constants.DongleId
        ''':any:`nixnet._enums.DongleId`: Indicates the connected Transceiver Cable's type.

        Dongle-Less Design indicates this interface is not a Transceiver Cable
        but a regular XNET expansion card, cDAQ Module, and so on.
        '''
        return constants.DongleId(_props.get_interface_dongle_id(self._handle))

    @property
    def dongle_revision(self):
        # type: () -> int
        '''int: The connected Transceiver Cable's hardware revision number.'''
        return _props.get_interface_dongle_revision(self._handle)

    @property
    def dongle_firmware_version(self):
        # type: () -> int
        '''int: The connected Transceiver Cable's firmware revision number.'''
        return _props.get_interface_dongle_firmware_version(self._handle)

    @property
    def dongle_compatible_revision(self):
        # type: () -> int
        '''int: The oldest driver version compatible with the connected Transceiver Cable's hardware revision.

        The number is relative to the first driver version that supported the
        particular Transceiver Cable model, starting with 1 for the original
        revision.

        .. note:: A Transceiver Cable hardware revision might require a later
           XNET driver than the version that introduced support for this model for
           operation.
        '''
        return _props.get_interface_dongle_compatible_revision(self._handle)

    @property
    def dongle_compatible_firmware_version(self):
        # type: () -> int
        '''int: The oldest driver version compatible with the connected Transceiver Cable's firmware.

        The number is relative to the first driver version that supported the
        Transceiver Cable, starting with 1 for the original revision.

        ..note:: A Transceiver Cable running an updated firmware version may
           require a later XNET driver than the version it shipped with for
           operation.
        '''
        return _props.get_interface_dongle_compatible_firmware_version(self._handle)

    def blink(self, modifier):
        # type: (constants.BlinkMode) -> None
        '''Blinks LEDs for the XNET interface to identify its physical port in the system.

        Each XNET device contains one or two physical ports. Each port is
        labeled on the hardware as Port 1 or Port 2. The XNET device also
        provides two LEDs per port. For a two-port board, LEDs 1 and 2 are
        assigned to Port 1, and LEDs 3 and 4 are assigned to physical Port 2.

        When your application uses multiple XNET devices, this function helps
        to identify each interface to associate its software behavior to its
        hardware connection (port). Prior to running your XNET sessions, you
        can call this function to blink the interface LEDs.

        For example, if you have a system with three PCI CAN cards, each with
        two ports, you can use this function to blink the LEDs for interface
        CAN4, to identify it among the six CAN ports.

        The LEDs of each port support two states:
            Identification:
                Blink LEDs to identify the physical port assigned to the interface.
            In Use:
                LED behavior that XNET sessions control.

        **Identification LED State**

        You can use the ``blink`` function only in the Identification state. If
        you call this function while one or more XNET sessions for the
        interface are open (created), it returns an error, because the port's
        LEDs are in the In Use state.

        **In Use LED State**

        When you create an XNET session for the interface, the LEDs for that
        physical port transition to the In Use state. If you called the ``blink``
        function previously to enable blinking for identification, that LED
        behavior no longer applies. The In Use LED state remains until all XNET
        sessions are cleared. This typically occurs when the application
        terminates. The patterns that appear on the LEDs while In Use are
        documented in LEDs.

        Args:
            moodifier (:any:`nixnet._enums.BlinkMode`): Controls LED blinking

                Both LEDs blink green (not red). The blinking rate is approximately
                three times per second.
        '''
        _funcs.nx_blink(self._handle, modifier)

    @property
    def _name(self):
        # type: () -> typing.Text
        return _props.get_interface_name(self._handle)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/system/system.py sha256=c22d75beb9d17fe7302c81be61e857fe688ca1bafde9398a6b4313c54daacf51 bytes=5803 -->
## FILE: nixnet/system/system.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/system/system.py`
- sha256: `c22d75beb9d17fe7302c81be61e857fe688ca1bafde9398a6b4313c54daacf51`
- bytes: 5803

````python
import typing  # NOQA: F401
import warnings

from nixnet import _cconsts
from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet.system import _collection
from nixnet.system import _databases
from nixnet.system import _device
from nixnet.system import _interface


class System(object):
    '''Interact with the NI driver and interface hardware.'''

    def __init__(self):
        # type: () -> None
        self._handle = None  # To satisfy `__del__` in case nx_system_open throws
        self._handle = _funcs.nx_system_open()
        self._databases = _databases.AliasCollection(self._handle)
        self._devices = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_DEV_REFS, _device.Device)
        self._intfs = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_INTF_REFS, _interface.Interface)
        self._intfs_all = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_INTF_REFS_ALL, _interface.Interface)
        self._intfs_can = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_INTF_REFS_CAN, _interface.Interface)
        self._intfs_flex_ray = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_INTF_REFS_FLEX_RAY, _interface.Interface)
        self._intfs_lin = _collection.SystemCollection(
            self._handle, _cconsts.NX_PROP_SYS_INTF_REFS_LIN, _interface.Interface)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'System was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(System, other)._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def close(self):
        # type: () -> None
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET system but system was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_system_close(self._handle)

        self._handle = None

    @property
    def databases(self):
        # type: () -> _databases.AliasCollection
        """:any:`nixnet.system._databases.AliasCollection`: Operate on systems's database's aliases"""
        return self._databases

    @property
    def dev_refs(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._device.Device`: Physical XNET devices in the system.'''
        return self._devices

    @property
    def intf_refs(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system.'''
        return self._intfs

    @property
    def intf_refs_all(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system.

        This Includes those not equipped with a Transceiver Cable.
        '''
        return self._intfs_all

    @property
    def intf_refs_can(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system (CAN Protocol).'''
        return self._intfs_can

    @property
    def intf_refs_flex_ray(self):
        # type: () -> _collection.SystemCollection
        return self._intfs_flex_ray

    @property
    def intf_refs_lin(self):
        # type: () -> _collection.SystemCollection
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system (LIN Protocol).'''
        return self._intfs_lin

    @property
    def ver(self):
        # type: () -> types.DriverVersion
        ''':any:`nixnet.types.DriverVersion`: The driver version (larger numbers imply a newer version).

        Use this for:

        * Determining the driver functionality or release date
        * Determining upgrade availability
        '''
        return types.DriverVersion(
            self._ver_major,
            self._ver_minor,
            self._ver_update,
            self._ver_phase,
            self._ver_build)

    @property
    def _ver_build(self):
        # type: () -> int
        return _props.get_system_ver_build(self._handle)  # type: ignore

    @property
    def _ver_major(self):
        # type: () -> int
        return _props.get_system_ver_major(self._handle)  # type: ignore

    @property
    def _ver_minor(self):
        # type: () -> int
        return _props.get_system_ver_minor(self._handle)  # type: ignore

    @property
    def _ver_phase(self):
        # type: () -> constants.Phase
        return constants.Phase(_props.get_system_ver_phase(self._handle))  # type: ignore

    @property
    def _ver_update(self):
        # type: () -> int
        return _props.get_system_ver_update(self._handle)  # type: ignore
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet/types.py sha256=b995d507c7df223d63db7f1f7819abe38d4e777753a5dc762225875c3226833a bytes=36419 -->
## FILE: nixnet/types.py

- repository: `ni/nixnet-python`
- source_path: `nixnet/types.py`
- sha256: `b995d507c7df223d63db7f1f7819abe38d4e777753a5dc762225875c3226833a`
- bytes: 36419

````python
import abc
import collections
import typing  # NOQA: F401

import six

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants

__all__ = [
    'DriverVersion',
    'CanComm',
    'LinComm',
    'CanIdentifier',
    'FrameFactory',
    'Frame',
    'RawFrame',
    'CanFrame',
    'CanBusErrorFrame',
    'LinFrame',
    'LinBusErrorFrame',
    'DelayFrame',
    'LogTriggerFrame',
    'StartTriggerFrame',
    'XnetFrame',
    'PduProperties']


DriverVersion_ = collections.namedtuple(
    'DriverVersion_',
    ['major', 'minor', 'update', 'phase', 'build'])


class DriverVersion(DriverVersion_):
    """Driver Version

    The arguments align with the following fields: ``[major].[minor].[update][phase][build]``.

    Attributes:
        major (int):
        minor (int):
        update (int):
        phase (:any:`nixnet._enums.Phase`):
        build (int):
    """


CanComm_ = collections.namedtuple(
    'CanComm_',
    ['state', 'tcvr_err', 'sleep', 'last_err', 'tx_err_count', 'rx_err_count'])


class CanComm(CanComm_):
    """CAN Communication State.

    Attributes:
        state (:any:`nixnet._enums.CanCommState`): Communication State
        tcvr_err (bool): Transceiver Error.
            Transceiver error indicates whether an error condition exists on
            the physical transceiver. This is typically referred to as the
            transceiver chip NERR pin.  False indicates normal operation (no
            error), and true indicates an error.
        sleep (bool): Sleep.
            Sleep indicates whether the transceiver and communication
            controller are in their sleep state. False indicates normal
            operation (awake), and true indicates sleep.
        last_err (:any:`nixnet._enums.CanLastErr`): Last Error.
            Last error specifies the status of the last attempt to receive or
            transmit a frame
        tx_err_count (int): Transmit Error Counter.
            The transmit error counter begins at 0 when communication starts on
            the CAN interface. The counter increments when an error is detected
            for a transmitted frame and decrements when a frame transmits
            successfully. The counter increases more for an error than it is
            decreased for success. This ensures that the counter generally
            increases when a certain ratio of frames (roughly 1/8) encounter
            errors.
            When communication state transitions to Bus Off, the transmit error
            counter no longer is valid.
        rx_err_count (int): Receive Error Counter.
            The receive error counter begins at 0 when communication starts on
            the CAN interface. The counter increments when an error is detected
            for a received frame and decrements when a frame is received
            successfully. The counter increases more for an error than it is
            decreased for success. This ensures that the counter generally
            increases when a certain ratio of frames (roughly 1/8) encounter
            errors.
    """

    pass


LinComm_ = collections.namedtuple(
    'LinComm_',
    ['sleep', 'state', 'last_err', 'err_received', 'err_expected', 'err_id', 'tcvr_rdy', 'sched_index'])


class LinComm(LinComm_):
    """CAN Communication State.

    Attributes:
        sleep (bool): Sleep.
            Indicates whether the transceiver and communication
            controller are in their sleep state. False indicates normal
            operation (awake), and true indicates sleep.
        state (:any:`nixnet._enums.LinCommState`): Communication State
        last_err (:any:`nixnet._enums.LinLastErr`): Last Error.
            Last error specifies the status of the last attempt to receive or
            transmit a frame
        err_received (int): Returns the value received from the network
            when last error occurred.

            When ``last_err`` is ``READBACK``, this is the value read back.

            When ``last_err`` is ``CHECKSUM``, this is the received checksum.
        err_expected (int): Returns the value that the LIN interface
            expected to see (instead of last received).

            When ``last_err`` is ``READBACK``, this is the value transmitted.

            When ``last_err`` is ``CHECKSUM``, this is the calculated checksum.
        err_id (int): Returns the frame identifier in which the last error
            occurred.

            This is not applicable when ``last_err`` is ``NONE`` or ``UNKNOWN_ID``.
        tcvr_rdy (bool): Indicates whether the LIN transceiver is powered from
            the bus.

            True indicates the bus power exists, so it is safe to start
            communication on the LIN interface.

            If this value is false, you cannot start communication
            successfully. Wire power to the LIN transceiver and run your
            application again.
        sched_index (int): Indicates the LIN schedule that the interface
            currently is running.

            This index refers to a LIN schedule that you requested using the
            :any:`nixnet._session.base.SessionBase.change_lin_schedule` function. It
            indexes the array of schedules represented in the
            :any:`nixnet._session.intf.Interface.lin_sched_names`.

            This index applies only when the LIN interface is running as a
            master. If the LIN interface is running as a slave only, this
            element should be ignored.
        """

    pass


PduProperties_ = collections.namedtuple(  # type: ignore
    'PDU_PROPERTIES_',
    ['pdu', 'start_bit', 'update_bit'])


class PduProperties(PduProperties_):
    """Properties that map a PDU onto a frame.

    Mapping PDUs to a frame requires setting three frame properties that are combined into this tuple.

    Attributes:
        pdu (:any:`Pdu`): Defines the sequence of values for the other two properties.
        start_bit (int): Defines the start bit of the PDU inside the frame.
        update_bit (int): Defines the update bit for the PDU inside the frame.
            If the update bit is not used, set the value to ``-1``.
    """


class CanIdentifier(object):
    """CAN frame arbitration identifier.

    Attributes:
        identifier(int): CAN frame arbitration identifier
        extended(bool): If the identifier is extended
    """

    _FRAME_ID_MASK = 0x000007FF
    _EXTENDED_FRAME_ID_MASK = 0x1FFFFFFF

    def __init__(self, identifier, extended=False):
        # type: (int, bool) -> None
        self.identifier = identifier
        self.extended = extended

    @classmethod
    def from_raw(cls, raw):
        # type: (int) -> CanIdentifier
        """Parse a raw frame identifier into a CanIdentifier

        Args:
            raw(int): A raw frame identifier

        Returns:
            CanIdentifier: parsed value

        >>> CanIdentifier.from_raw(0x1)
        CanIdentifier(0x1)
        >>> CanIdentifier.from_raw(0x20000001)
        CanIdentifier(0x1, extended=True)
        """
        extended = bool(raw & _cconsts.NX_FRAME_ID_CAN_IS_EXTENDED)
        if extended:
            identifier = raw & cls._EXTENDED_FRAME_ID_MASK
        else:
            identifier = raw & cls._FRAME_ID_MASK
        return cls(identifier, extended)

    def __int__(self):
        """Convert CanIdentifier into a raw frame identifier

        >>> hex(int(CanIdentifier(1)))
        '0x1'
        >>> hex(int(CanIdentifier(1, True)))
        '0x20000001'
        """
        identifier = self.identifier
        if self.extended:
            if identifier != (identifier & self._EXTENDED_FRAME_ID_MASK):
                _errors.check_for_error(_cconsts.NX_ERR_UNDEFINED_FRAME_ID)
            identifier |= _cconsts.NX_FRAME_ID_CAN_IS_EXTENDED
        else:
            if identifier != (identifier & self._FRAME_ID_MASK):
                _errors.check_for_error(_cconsts.NX_ERR_UNDEFINED_FRAME_ID)
        return identifier

    def __eq__(self, other):
        if isinstance(other, CanIdentifier):
            other_id = typing.cast(CanIdentifier, other)
            return all((
                self.identifier == other_id.identifier,
                self.extended == other_id.extended))
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __repr__(self):
        """CanIdentifier debug representation.

        >>> CanIdentifier(1)
        CanIdentifier(0x1)
        >>> CanIdentifier(1, True)
        CanIdentifier(0x1, extended=True)
        """
        if self.extended:
            return "{}(0x{:x}, extended={})".format(
                type(self).__name__,
                self.identifier,
                self.extended)
        else:
            return "{}(0x{:x})".format(
                type(self).__name__,
                self.identifier)


@six.add_metaclass(abc.ABCMeta)
class FrameFactory(object):
    """ABC for creating :any:`nixnet.types.Frame` objects."""

    __slots__ = ()

    @classmethod
    @abc.abstractmethod
    def from_raw(cls, frame):  # NOQA: N805 can't detect abstractclassmethod
        # No type annotation because mypy doesn't understand
        # abstractclassmethod is the same as classmethod
        """Convert from RawFrame."""
        pass


@six.add_metaclass(abc.ABCMeta)
class Frame(FrameFactory):
    """ABC for frame objects."""

    __slots__ = ()

    @abc.abstractmethod
    def to_raw(self):
        # type: () -> RawFrame
        """Convert to RawFrame."""
        pass

    @abc.abstractproperty
    def type(self):
        # type: () -> constants.FrameType
        """:any:`nixnet._enums.FrameType`: Frame format."""
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    @abc.abstractmethod
    def __repr__(self):
        pass


class RawFrame(Frame):
    """Raw Frame.

    Attributes:
        timestamp(int): Absolute time the XNET interface received the end-of-frame.
        identifier(int): Frame identifier.
        type(:any:`nixnet._enums.FrameType`): Frame type.
        flags(int): Flags that qualify the type.
        info(int): Info that qualify the type.
        payload(bytes): Payload.
    """

    __slots__ = [
        "timestamp",
        "identifier",
        "_type",
        "flags",
        "info",
        "payload"]

    def __init__(self, timestamp, identifier, type, flags=0, info=0, payload=b""):
        # type: (int, int, constants.FrameType, int, int, bytes) -> None
        self.timestamp = timestamp
        self.identifier = identifier
        self._type = type
        self.flags = flags
        self.info = info
        self.payload = payload

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame."""
        return frame

    def to_raw(self):
        """Convert to RawFrame."""
        return self

    @property
    def type(self):
        return self._type

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(RawFrame, other)
            return all((
                self.timestamp == other_frame.timestamp,
                self.identifier == other_frame.identifier,
                self.type == other_frame.type,
                self.flags == other_frame.flags,
                self.info == other_frame.info,
                self.payload == other_frame.payload))
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """RawFrame debug representation.

        >>> RawFrame(1, 2, constants.FrameType.CAN_DATA, 3, 4)
        RawFrame(timestamp=0x1, identifier=0x2, type=FrameType.CAN_DATA, flags=0x3, info=0x4)
        """
        optional = []
        if self.flags != 0:
            optional.append('flags=0x{:x}'.format(self.flags))
        if self.info != 0:
            optional.append('info=0x{:x}'.format(self.info))
        if self.payload:
            optional.append('len(payload)={}'.format(len(self.payload)))
        if optional:
            optional_params = ', {}'.format(", ".join(optional))
        else:
            optional_params = ''
        return "{}(timestamp=0x{:x}, identifier=0x{:x}, type={}{})".format(
            type(self).__name__,
            self.timestamp,
            self.identifier,
            self.type,
            optional_params)


class CanFrame(Frame):
    """CAN Frame.

    Attributes:
        identifier(:any:`nixnet.types.CanIdentifier`): CAN frame arbitration identifier.
        echo(bool): If the frame is an echo of a successful
            transmit rather than being received from the network.
        type(:any:`nixnet._enums.FrameType`): Frame type.
        timestamp(int): Absolute time the XNET interface received the end-of-frame.
        payload(bytes): Payload.
    """

    __slots__ = [
        "identifier",
        "echo",
        "_type",
        "timestamp",
        "payload"]

    def __init__(self, identifier, type=constants.FrameType.CAN_DATA, payload=b""):
        # type: (typing.Union[CanIdentifier, int], constants.FrameType, bytes) -> None
        if isinstance(identifier, int):
            self.identifier = CanIdentifier(identifier)
        else:
            self.identifier = identifier
        self.echo = False  # Used only for Read
        self._type = type
        self.timestamp = 0  # Used only for Read
        self.payload = payload

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 0x20000001, constants.FrameType.CAN_DATA, _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO, 0, b'')
        >>> CanFrame.from_raw(raw)
        CanFrame(CanIdentifier(0x1, extended=True), echo=True, timestamp=0x5)
        """
        identifier = CanIdentifier.from_raw(frame.identifier)
        can_frame = CanFrame(identifier, constants.FrameType(frame.type), frame.payload)
        can_frame.timestamp = frame.timestamp
        can_frame.echo = bool(frame.flags & _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO)
        return can_frame

    def to_raw(self):
        """Convert to RawFrame.

        >>> CanFrame(CanIdentifier(1, True), constants.FrameType.CAN_DATA).to_raw()
        RawFrame(timestamp=0x0, identifier=0x20000001, type=FrameType.CAN_DATA)
        >>> c = CanFrame(CanIdentifier(1, True), constants.FrameType.CAN_DATA)
        >>> c.echo = True
        >>> c.to_raw()
        RawFrame(timestamp=0x0, identifier=0x20000001, type=FrameType.CAN_DATA, flags=0x80)
        """
        identifier = int(self.identifier)
        flags = 0
        if self.echo:
            flags |= _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO
        return RawFrame(self.timestamp, identifier, self.type, flags, 0, self.payload)

    @property
    def type(self):
        return self._type

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(CanFrame, other)
            return all((
                self.identifier == other_frame.identifier,
                self.echo == other_frame.echo,
                self.type == other_frame.type,
                self.timestamp == other_frame.timestamp,
                self.payload == other_frame.payload))
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """CanFrame debug representation.

        >>> CanFrame(1)
        CanFrame(CanIdentifier(0x1))
        >>> CanFrame(1, constants.FrameType.CANFD_DATA, b'\x01')
        CanFrame(CanIdentifier(0x1), type=FrameType.CANFD_DATA, len(payload)=1)
        """
        optional = []
        if self.echo:
            optional.append('echo={}'.format(self.echo))
        if self.type != constants.FrameType.CAN_DATA:
            optional.append('type={}'.format(self.type))
        if self.timestamp != 0:
            optional.append('timestamp=0x{:x}'.format(self.timestamp))
        if self.payload:
            optional.append('len(payload)={}'.format(len(self.payload)))
        if optional:
            optional_params = ', {}'.format(", ".join(optional))
        else:
            optional_params = ''
        return "{}({}{})".format(
            type(self).__name__,
            self.identifier,
            optional_params)


class CanBusErrorFrame(Frame):
    """Error detected on hardware bus of a :any:`nixnet.session.FrameInStreamSession`.

    .. note:: This requires enabling
       :any:`nixnet._session.intf.Interface.bus_err_to_in_strm`.

    See also :any:`nixnet.types.CanComm`.

    Attributes:
        timestamp(int): Absolute time when the bus error occurred.
        state (:any:`nixnet._enums.CanCommState`): Communication State
        tcvr_err (bool): Transceiver Error.
        bus_err (:any:`nixnet._enums.CanLastErr`): Last Error.
        tx_err_count (int): Transmit Error Counter.
        rx_err_count (int): Receive Error Counter.
    """

    __slots__ = [
        "timestamp",
        "state",
        "tcvr_err",
        "bus_err",
        "tx_err_count",
        "rx_err_count"]

    def __init__(self, timestamp, state, tcvr_err, bus_err, tx_err_count, rx_err_count):
        # type: (int, constants.CanCommState, bool, constants.CanLastErr, int, int) -> None
        self.timestamp = timestamp
        self.state = state
        self.tcvr_err = tcvr_err
        self.bus_err = bus_err
        self.tx_err_count = tx_err_count
        self.rx_err_count = rx_err_count

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(0x64, 0x0, constants.FrameType.CAN_BUS_ERROR, 0, 0, b'\\x00\\x01\\x02\\x03\\x04')
        >>> CanBusErrorFrame.from_raw(raw)
        CanBusErrorFrame(0x64, CanCommState.ERROR_ACTIVE, True, CanLastErr.ACK, 1, 2)
        """
        timestamp = frame.timestamp
        state = constants.CanCommState(six.indexbytes(frame.payload, 0))
        tx_err_count = six.indexbytes(frame.payload, 1)
        rx_err_count = six.indexbytes(frame.payload, 2)
        bus_err = constants.CanLastErr(six.indexbytes(frame.payload, 3))
        tcvr_err = six.indexbytes(frame.payload, 4) != 0
        return CanBusErrorFrame(timestamp, state, tcvr_err, bus_err, tx_err_count, rx_err_count)

    def to_raw(self):
        """Convert to RawFrame.

        >>> CanBusErrorFrame(100, constants.CanCommState.BUS_OFF, True, constants.CanLastErr.STUFF, 1, 2).to_raw()
        RawFrame(timestamp=0x64, identifier=0x0, type=FrameType.CAN_BUS_ERROR, len(payload)=5)
        """
        identifier = 0
        flags = 0
        info = 0

        payload_data = [
            self.state.value,
            self.tx_err_count,
            self.rx_err_count,
            self.bus_err.value,
            1 if self.tcvr_err else 0,
        ]
        payload = bytes(bytearray(payload_data))
        return RawFrame(self.timestamp, identifier, self.type, flags, info, payload)

    @property
    def type(self):
        return constants.FrameType.CAN_BUS_ERROR

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(CanBusErrorFrame, other)
            return all((
                self.timestamp == other_frame.timestamp,
                self.state == other_frame.state,
                self.tcvr_err == other_frame.tcvr_err,
                self.bus_err == other_frame.bus_err,
                self.tx_err_count == other_frame.tx_err_count,
                self.rx_err_count == other_frame.rx_err_count))
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """CanBusErrorFrame debug representation.

        >>> CanBusErrorFrame(100, constants.CanCommState.BUS_OFF, True, constants.CanLastErr.STUFF, 1, 2)
        CanBusErrorFrame(0x64, CanCommState.BUS_OFF, True, CanLastErr.STUFF, 1, 2)
        """
        return "{}(0x{:x}, {}, {}, {}, {}, {})".format(
            type(self).__name__,
            self.timestamp,
            self.state,
            self.tcvr_err,
            self.bus_err,
            self.tx_err_count,
            self.rx_err_count)


class LinFrame(object):
    """LIN Frame.

    Attributes:
        identifier(int): LIN frame arbitration identifier.
        echo(bool): If the frame is an echo of a successful
            transmit rather than being received from the network.
        type(:any:`nixnet._enums.FrameType`): Frame type.
        timestamp(int): Absolute time the XNET interface received the end-of-frame.
        eventslot(bool): Whether the frame was received within an
            event-triggered slot or an unconditional or sporadic slot.
        eventid(int): Identifier for an event-triggered slot.
        payload(bytes): A byte string representing the payload.
    """

    __slots__ = [
        "identifier",
        "echo",
        "type",
        "timestamp",
        "eventslot",
        "eventid",
        "payload"]

    _FRAME_ID_MASK = 0x0000003F

    def __init__(self, identifier, type=constants.FrameType.LIN_DATA, payload=b""):
        # type: (int, constants.FrameType, bytes) -> None
        self.identifier = identifier
        self.echo = False  # Used only for Read
        self.type = type
        self.timestamp = 0  # Used only for Read
        self.eventslot = False  # Used only for Read
        self.eventid = 0  # Used only for Read
        self.payload = payload

    @classmethod
    def from_raw(cls, frame):
        # type: (RawFrame) -> LinFrame
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 2, constants.FrameType.LIN_DATA, 0x81, 1, b'\x01')
        >>> LinFrame.from_raw(raw)
        LinFrame(identifier=0x2, echo=True, timestamp=0x5, eventslot=True, eventid=1, len(payload)=1)
        >>> raw = RawFrame(5, 2, constants.FrameType.LIN_DATA, _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO, 0, b'\x01')
        >>> LinFrame.from_raw(raw)
        LinFrame(identifier=0x2, echo=True, timestamp=0x5, len(payload)=1)
        """
        identifier = frame.identifier & cls._FRAME_ID_MASK
        lin_frame = LinFrame(identifier, constants.FrameType(frame.type), frame.payload)
        lin_frame.timestamp = frame.timestamp
        lin_frame.echo = bool(frame.flags & _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO)
        lin_frame.eventslot = bool(frame.flags & _cconsts.NX_FRAME_FLAGS_LIN_EVENT_SLOT)
        if lin_frame.eventslot:
            lin_frame.eventid = frame.info
        else:
            lin_frame.eventid = 0

        return lin_frame

    def to_raw(self):
        # type: () -> RawFrame
        """Convert to RawFrame.

        >>> LinFrame(2, constants.FrameType.LIN_DATA).to_raw()
        RawFrame(timestamp=0x0, identifier=0x2, type=FrameType.LIN_DATA)
        >>> l = LinFrame(2, constants.FrameType.LIN_DATA)
        >>> l.echo = True
        >>> l.eventslot = True
        >>> l.eventid = 1
        >>> l.to_raw()
        RawFrame(timestamp=0x0, identifier=0x2, type=FrameType.LIN_DATA, flags=0x81, info=0x1)
        """
        if self.identifier != (self.identifier & self._FRAME_ID_MASK):
            _errors.check_for_error(_cconsts.NX_ERR_UNDEFINED_FRAME_ID)
        flags = 0
        info = 0
        if self.echo:
            flags |= _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO
        if self.eventslot:
            flags |= _cconsts.NX_FRAME_FLAGS_LIN_EVENT_SLOT
            info |= self.eventid
        return RawFrame(self.timestamp, self.identifier, self.type, flags, info, self.payload)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(LinFrame, other)
            return all((
                self.identifier == other_frame.identifier,
                self.echo == other_frame.echo,
                self.type == other_frame.type,
                self.timestamp == other_frame.timestamp,
                self.eventslot == other_frame.eventslot,
                self.eventid == other_frame.eventid,
                self.payload == other_frame.payload))
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """LinFrame debug representation.

        >>> LinFrame(2)
        LinFrame(identifier=0x2)
        >>> LinFrame(2, constants.FrameType.LIN_NO_RESPONSE, b'\x01')
        LinFrame(identifier=0x2, type=FrameType.LIN_NO_RESPONSE, len(payload)=1)
        """
        optional = []
        if self.echo:
            optional.append('echo={}'.format(self.echo))
        if self.type != constants.FrameType.LIN_DATA:
            optional.append('type={}'.format(self.type))
        if self.timestamp != 0:
            optional.append('timestamp=0x{:x}'.format(self.timestamp))
        if self.eventslot:
            optional.append('eventslot={}'.format(self.eventslot))
        if self.eventid != 0:
            optional.append('eventid={}'.format(self.eventid))
        if self.payload:
            optional.append('len(payload)={}'.format(len(self.payload)))
        if optional:
            optional_params = ', {}'.format(", ".join(optional))
        else:
            optional_params = ''
        return "{}(identifier=0x{:x}{})".format(
            type(self).__name__,
            self.identifier,
            optional_params)


class LinBusErrorFrame(Frame):
    """Error detected on hardware bus of a :any:`nixnet.session.FrameInStreamSession`.

    .. note:: This requires enabling
       :any:`nixnet._session.intf.Interface.bus_err_to_in_strm`.

    See also :any:`nixnet.types.LinComm`.

    Attributes:
        timestamp(int): Absolute time when the bus error occurred.
        state (:any:`nixnet._enums.LinCommState`): Communication State.
        bus_err (:any:`nixnet._enums.LinLastErr`): Last Error.
        err_id (int): Identifier on bus.
        err_received (int): Received byte on bus
        err_expected (int): Expected byte on bus
    """

    __slots__ = [
        "timestamp",
        "state",
        "bus_err",
        "err_id",
        "err_received",
        "err_expected"]

    def __init__(self, timestamp, state, bus_err, err_id, err_received, err_expected):
        # type: (int, constants.LinCommState, constants.LinLastErr, int, int, int) -> None
        self.timestamp = timestamp
        self.state = state
        self.bus_err = bus_err
        self.err_id = err_id
        self.err_received = err_received
        self.err_expected = err_expected

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(0x64, 0x0, constants.FrameType.LIN_BUS_ERROR, 0, 0, b'\\x00\\x01\\x02\\x03\\x04')
        >>> LinBusErrorFrame.from_raw(raw)
        LinBusErrorFrame(0x64, LinCommState.IDLE, LinLastErr.UNKNOWN_ID, 0x2, 3, 4)
        """
        timestamp = frame.timestamp
        state = constants.LinCommState(six.indexbytes(frame.payload, 0))
        bus_err = constants.LinLastErr(six.indexbytes(frame.payload, 1))
        err_id = six.indexbytes(frame.payload, 2)
        err_received = six.indexbytes(frame.payload, 3)
        err_expected = six.indexbytes(frame.payload, 4)
        return LinBusErrorFrame(timestamp, state, bus_err, err_id, err_received, err_expected)

    def to_raw(self):
        """Convert to RawFrame.

        >>> LinBusErrorFrame(100, constants.LinCommState.INACTIVE, constants.LinLastErr.UNKNOWN_ID, 2, 3, 4).to_raw()
        RawFrame(timestamp=0x64, identifier=0x0, type=FrameType.LIN_BUS_ERROR, len(payload)=5)
        """
        identifier = 0
        flags = 0
        info = 0

        payload_data = [
            self.state.value,
            self.bus_err.value,
            self.err_id,
            self.err_received,
            self.err_expected,
        ]
        payload = bytes(bytearray(payload_data))
        return RawFrame(self.timestamp, identifier, self.type, flags, info, payload)

    @property
    def type(self):
        return constants.FrameType.LIN_BUS_ERROR

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(LinBusErrorFrame, other)
            return all((
                self.timestamp == other_frame.timestamp,
                self.state == other_frame.state,
                self.bus_err == other_frame.bus_err,
                self.err_id == other_frame.err_id,
                self.err_received == other_frame.err_received,
                self.err_expected == other_frame.err_expected))
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """LinBusErrorFrame debug representation.

        >>> LinBusErrorFrame(100, constants.LinCommState.INACTIVE, constants.LinLastErr.CRC, 1, 2, 3)
        LinBusErrorFrame(0x64, LinCommState.INACTIVE, LinLastErr.CRC, 0x1, 2, 3)
        """
        return "{}(0x{:x}, {}, {}, 0x{:x}, {}, {})".format(
            type(self).__name__,
            self.timestamp,
            self.state,
            self.bus_err,
            self.err_id,
            self.err_received,
            self.err_expected)


class DelayFrame(Frame):
    """Delay hardware when DelayFrame is outputted.

    .. note:: This requires
       :any:`nixnet._session.intf.Interface.out_strm_timng` to be in replay mode.

    Attributes:
        offset(int): Time to delay in milliseconds.
    """

    __slots__ = [
        "offset"]

    def __init__(self, offset):
        # type: (int) -> None
        self.offset = offset

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 0, constants.FrameType.SPECIAL_DELAY, 0, 0, b'')
        >>> DelayFrame.from_raw(raw)
        DelayFrame(5)
        """
        return DelayFrame(frame.timestamp)

    def to_raw(self):
        """Convert to RawFrame.

        >>> DelayFrame(250).to_raw()
        RawFrame(timestamp=0xfa, identifier=0x0, type=FrameType.SPECIAL_DELAY)
        """
        identifier = 0
        flags = 0
        info = 0
        payload = b''
        return RawFrame(self.offset, identifier, self.type, flags, info, payload)

    @property
    def type(self):
        return constants.FrameType.SPECIAL_DELAY

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(DelayFrame, other)
            return self.offset == other_frame.offset
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """DelayFrame debug representation.

        >>> DelayFrame(250)
        DelayFrame(250)
        """
        return "{}({})".format(type(self).__name__, self.offset)


class LogTriggerFrame(Frame):
    """Timestamp of when a trigger occurred.

    This frame is generated on input sessions when a rising edge is detected on
    an external connection.

    .. note:: This requires using
       :any:`nixnet._session.base.SessionBase.connect_terminals` to connect an
       external connection to the internal ``LogTrigger`` terminal.

    Attributes:
        timestamp(int): Absolute time that the trigger occurred.
    """

    __slots__ = [
        "timestamp"]

    def __init__(self, timestamp):
        # type: (int) -> None
        self.timestamp = timestamp

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 0, constants.FrameType.SPECIAL_LOG_TRIGGER, 0, 0, b'')
        >>> LogTriggerFrame.from_raw(raw)
        LogTriggerFrame(0x5)
        """
        return LogTriggerFrame(frame.timestamp)

    def to_raw(self):
        """Convert to RawFrame.

        >>> LogTriggerFrame(250).to_raw()
        RawFrame(timestamp=0xfa, identifier=0x0, type=FrameType.SPECIAL_LOG_TRIGGER)
        """
        identifier = 0
        flags = 0
        info = 0
        payload = b''
        return RawFrame(self.timestamp, identifier, self.type, flags, info, payload)

    @property
    def type(self):
        return constants.FrameType.SPECIAL_LOG_TRIGGER

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(LogTriggerFrame, other)
            return self.timestamp == other_frame.timestamp
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """LogTriggerFrame debug representation.

        >>> LogTriggerFrame(250)
        LogTriggerFrame(0xfa)
        """
        return "{}(0x{:x})".format(type(self).__name__, self.timestamp)


class StartTriggerFrame(Frame):
    """Timestamp of :any:`nixnet.session.FrameInStreamSession` start.

    .. note:: This requires enabling
       :any:`nixnet._session.intf.Interface.start_trig_to_in_strm`.

    Attributes:
        timestamp(int): Absolute time that the trigger occurred.
    """

    __slots__ = [
        "timestamp"]

    def __init__(self, timestamp):
        # type: (int) -> None
        self.timestamp = timestamp

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 0, constants.FrameType.SPECIAL_START_TRIGGER, 0, 0, b'')
        >>> StartTriggerFrame.from_raw(raw)
        StartTriggerFrame(0x5)
        """
        return StartTriggerFrame(frame.timestamp)

    def to_raw(self):
        """Convert to RawFrame.

        >>> StartTriggerFrame(250).to_raw()
        RawFrame(timestamp=0xfa, identifier=0x0, type=FrameType.SPECIAL_START_TRIGGER)
        """
        identifier = 0
        flags = 0
        info = 0
        payload = b''
        return RawFrame(self.timestamp, identifier, self.type, flags, info, payload)

    @property
    def type(self):
        return constants.FrameType.SPECIAL_START_TRIGGER

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(StartTriggerFrame, other)
            return self.timestamp == other_frame.timestamp
        else:
            return NotImplemented

    def __repr__(self):
        # type: () -> typing.Text
        """StartTriggerFrame debug representation.

        >>> StartTriggerFrame(250)
        StartTriggerFrame(0xfa)
        """
        return "{}(0x{:x})".format(type(self).__name__, self.timestamp)


class XnetFrame(FrameFactory):
    """Create `Frame` based on `RawFrame` content."""

    __slots__ = ()

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame."""
        frame_type = {
            constants.FrameType.CAN_DATA: CanFrame,
            constants.FrameType.CAN20_DATA: CanFrame,
            constants.FrameType.CANFD_DATA: CanFrame,
            constants.FrameType.CANFDBRS_DATA: CanFrame,
            constants.FrameType.CAN_REMOTE: CanFrame,
            constants.FrameType.CAN_BUS_ERROR: CanBusErrorFrame,
            constants.FrameType.LIN_DATA: LinFrame,
            constants.FrameType.SPECIAL_DELAY: DelayFrame,
            constants.FrameType.SPECIAL_LOG_TRIGGER: LogTriggerFrame,
            constants.FrameType.SPECIAL_START_TRIGGER: StartTriggerFrame,
        }.get(frame.type)
        if frame_type is None:
            raise NotImplementedError("Unsupported frame type", frame.type)
        return frame_type.from_raw(frame)
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: nixnet_examples/__init__.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/can_dynamic_database_creation.py sha256=6a115c5a244331bcc8978f7f9345bd395b7230fb4625bb444581eb64725b5fa4 bytes=3602 -->
## FILE: nixnet_examples/can_dynamic_database_creation.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/can_dynamic_database_creation.py`
- sha256: `6a115c5a244331bcc8978f7f9345bd395b7230fb4625bb444581eb64725b5fa4`
- bytes: 3602

````python
from random import randint
import six
import time

import nixnet
from nixnet import constants
from nixnet import database


def main():
    database_name = ':memory:'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CAN_Event_Frame'
    signal_1_name = 'CAN_Event_Signal_1'
    signal_2_name = 'CAN_Event_Signal_2'
    signal_list = [signal_1_name, signal_2_name]
    output_interface = 'CAN1'
    input_interface = 'CAN2'

    # Open the default in-memory database.
    # Database.close will be called by Database.__exit__ when exiting the 'with' block.
    with database.Database(database_name) as db:

        # Add a CAN cluster, a frame, and two signals to the database.
        cluster = db.clusters.add(cluster_name)
        cluster.protocol = constants.Protocol.CAN
        cluster.baud_rate = 125000
        frame = cluster.frames.add(frame_name)
        frame.id = 1
        frame.payload_len = 2
        signal_1 = frame.mux_static_signals.add(signal_1_name)
        signal_1.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_1.data_type = constants.SigDataType.UNSIGNED
        signal_1.start_bit = 0
        signal_1.num_bits = 8
        signal_2 = frame.mux_static_signals.add(signal_2_name)
        signal_2.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_2.data_type = constants.SigDataType.UNSIGNED
        signal_2.start_bit = 8
        signal_2.num_bits = 8

        # Using the database we just created, write and then read a pair of signals.
        with nixnet.SignalOutSinglePointSession(
                output_interface,
                database_name,
                cluster_name,
                signal_list) as output_session:
            with nixnet.SignalInSinglePointSession(
                    input_interface,
                    database_name,
                    cluster_name,
                    signal_list) as input_session:
                terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
                if terminated_cable.lower() == "y":
                    input_session.intf.can_term = constants.CanTerm.ON
                    output_session.intf.can_term = constants.CanTerm.OFF
                elif terminated_cable.lower() == "n":
                    input_session.intf.can_term = constants.CanTerm.ON
                    output_session.intf.can_term = constants.CanTerm.ON
                else:
                    print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                    input_session.intf.can_term = constants.CanTerm.ON
                    output_session.intf.can_term = constants.CanTerm.ON

                # Start the input session manually to make sure that the first
                # signal values sent before the initial read will be received.
                input_session.start()

                # Generate a pair of random values and send out the signals.
                output_values = [randint(0, 255), randint(0, 255)]
                output_session.signals.write(output_values)
                print('Sent signal values: {}'.format(output_values))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                input_signals = input_session.signals.read()
                input_values = [int(value) for timestamp, value in input_signals]
                print('Received signal values: {}'.format(input_values))


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/can_frame_queued_io.py sha256=26dfb7173a3fa02221a6f08ee2c8b0b5c4b973a70d800a879086cb499d705fc3 bytes=3341 -->
## FILE: nixnet_examples/can_frame_queued_io.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/can_frame_queued_io.py`
- sha256: `26dfb7173a3fa02221a6f08ee2c8b0b5c4b973a70d800a879086cb499d705fc3`
- bytes: 3341

````python
import time

import six

import nixnet
from nixnet import constants
from nixnet import types


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    input_frame = 'CANEventFrame1'
    output_frame = 'CANEventFrame1'
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    with nixnet.FrameInQueuedSession(
            interface1,
            database_name,
            cluster_name,
            input_frame) as input_session:
        with nixnet.FrameOutQueuedSession(
                interface2,
                database_name,
                cluster_name,
                output_frame) as output_session:
            terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
            if terminated_cable.lower() == "y":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.OFF
            elif terminated_cable.lower() == "n":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            user_value = six.moves.input('Enter payload [int, int]: ')
            try:
                payload_list = [int(x.strip()) for x in user_value.split(",")]
            except ValueError:
                payload_list = [2, 4, 8, 16]
                print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

            id = types.CanIdentifier(0)
            payload = bytearray(payload_list)
            frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)

            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.frames.write([frame])
                print('Sent frame with ID: {} payload: {}'.format(frame.identifier,
                                                                  list(frame.payload)))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                frames = input_session.frames.read(count)
                for frame in frames:
                    print('Received frame with ID: {} payload: {}'.format(frame.identifier,
                                                                          list(six.iterbytes(frame.payload))))

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/can_frame_stream_io.py sha256=ad3467fb82ab049fa30ce174dccf0a9d35949d850377b89be3bb4df8c0d3a8e1 bytes=3168 -->
## FILE: nixnet_examples/can_frame_stream_io.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/can_frame_stream_io.py`
- sha256: `ad3467fb82ab049fa30ce174dccf0a9d35949d850377b89be3bb4df8c0d3a8e1`
- bytes: 3168

````python
import time

import six

import nixnet
from nixnet import constants
from nixnet import types


def main():
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    with nixnet.FrameInStreamSession(interface1) as input_session:
        with nixnet.FrameOutStreamSession(interface2) as output_session:
            terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
            if terminated_cable.lower() == "y":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.OFF
            elif terminated_cable.lower() == "n":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON

            input_session.intf.baud_rate = 125000
            output_session.intf.baud_rate = 125000

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            user_value = six.moves.input('Enter payload [int, int]: ')
            try:
                payload_list = [int(x.strip()) for x in user_value.split(",")]
            except ValueError:
                payload_list = [2, 4, 8, 16]
                print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

            id = types.CanIdentifier(0)
            payload = bytearray(payload_list)
            frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.frames.write([frame])
                print('Sent frame with ID: {} payload: {}'.format(frame.identifier,
                                                                  list(frame.payload)))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                frames = input_session.frames.read(count)
                for frame in frames:
                    print('Received frame with ID: {} payload: {}'.format(frame.identifier,
                                                                          list(six.iterbytes(frame.payload))))

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/can_signal_conversion.py sha256=384a55884baf70859ee095cc57234c948cd59952271b61b4ce9a8d1bbb27a206 bytes=1403 -->
## FILE: nixnet_examples/can_signal_conversion.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/can_signal_conversion.py`
- sha256: `384a55884baf70859ee095cc57234c948cd59952271b61b4ce9a8d1bbb27a206`
- bytes: 1403

````python
import six

from nixnet import convert


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_names = ['CANEventSignal1', 'CANEventSignal2']

    with convert.SignalConversionSinglePointSession(
            database_name,
            cluster_name,
            signal_names) as session:

        user_value = six.moves.input('Enter {} signal values [float, float]: '.format(len(signal_names)))
        try:
            expected_signals = [float(x.strip()) for x in user_value.split(",")]
        except ValueError:
            expected_signals = [24.5343, 77.0129]
            print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, expected_signals))

        if len(expected_signals) != len(signal_names):
            expected_signals = [24.5343, 77.0129]
            print('Invalid number of signal values entered. Setting data buffer to {}'.format(expected_signals))

        frames = session.convert_signals_to_frames(expected_signals)
        print('Frames:')
        for frame in frames:
            print('    {}'.format(frame))
            print('        payload={}'.format(list(six.iterbytes(frame.payload))))

        converted_signals = session.convert_frames_to_signals(frames)
        print('Signals: {}'.format([v for (_, v) in converted_signals]))


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/can_signal_single_point_io.py sha256=03870ba5416d5b84500a2a43cefd4529d946244e91a2e7f010bfd8530fa94a06 bytes=3795 -->
## FILE: nixnet_examples/can_signal_single_point_io.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/can_signal_single_point_io.py`
- sha256: `03870ba5416d5b84500a2a43cefd4529d946244e91a2e7f010bfd8530fa94a06`
- bytes: 3795

````python
import datetime
import sys
import time

import six

import nixnet
from nixnet import constants


def convert_timestamp(timestamp):
    system_epoch = time.gmtime(0)
    system_epock_datetime = datetime.datetime(system_epoch.tm_year, system_epoch.tm_mon, system_epoch.tm_mday)
    xnet_epoch_datetime = datetime.datetime(1601, 1, 1)
    delta = system_epock_datetime - xnet_epoch_datetime
    date = datetime.datetime.fromtimestamp(timestamp * 100e-9) - delta
    return date


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    input_signals = ['CANEventSignal1', 'CANEventSignal2']
    output_signals = ['CANEventSignal1', 'CANEventSignal2']
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    with nixnet.SignalInSinglePointSession(
            interface1,
            database_name,
            cluster_name,
            input_signals) as input_session:
        with nixnet.SignalOutSinglePointSession(
                interface2,
                database_name,
                cluster_name,
                output_signals) as output_session:
            terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
            if terminated_cable.lower() == "y":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.OFF
            elif terminated_cable.lower() == "n":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON

            # Start the input session manually to make sure that the first
            # signal value sent before the initial read will be received.
            input_session.start()

            user_value = six.moves.input('Enter {} signal values [float, float]: '.format(len(input_signals)))
            try:
                value_buffer = [float(x.strip()) for x in user_value.split(",")]
            except ValueError:
                value_buffer = [24.5343, 77.0129]
                print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, value_buffer))

            if len(value_buffer) != len(input_signals):
                value_buffer = [24.5343, 77.0129]
                print('Invalid number of signal values entered. Setting data buffer to {}'.format(value_buffer))

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, value in enumerate(value_buffer):
                    value_buffer[index] = value + i
                output_session.signals.write(value_buffer)
                print('Sent signal values: {}'.format(value_buffer))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                signals = input_session.signals.read()
                for timestamp, value in signals:
                    date = convert_timestamp(timestamp)
                    print('Received signal with timestamp {} and value {}'.format(date, value))

                i += 1
                if max(value_buffer) + i > sys.float_info.max:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/lin_dynamic_database_creation.py sha256=a9d39049b58704738b8044546dc800d64196705808418b462e89b16040811806 bytes=4637 -->
## FILE: nixnet_examples/lin_dynamic_database_creation.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/lin_dynamic_database_creation.py`
- sha256: `a9d39049b58704738b8044546dc800d64196705808418b462e89b16040811806`
- bytes: 4637

````python
from random import randint
import six
import time

import nixnet
from nixnet import constants
from nixnet import database


def main():
    database_name = ':memory:'
    cluster_name = 'LIN_Cluster'
    ecu_1_name = 'LIN_ECU_1'
    ecu_2_name = 'LIN_ECU_2'
    schedule_name = 'LIN_Schedule_1'
    schedule_entry_name = 'LIN_Schedule_Entry'
    frame_name = 'LIN_Frame'
    signal_1_name = 'LIN_Signal_1'
    signal_2_name = 'LIN_Signal_2'
    signal_list = [signal_1_name, signal_2_name]
    output_interface = 'LIN1'
    input_interface = 'LIN2'

    # Open the default in-memory database.
    # Database.close will be called by Database.__exit__ when exiting the 'with' block.
    with database.Database(database_name) as db:

        # Add a LIN cluster, a frame, and two signals to the database.
        cluster = db.clusters.add(cluster_name)
        cluster.protocol = constants.Protocol.LIN
        cluster.baud_rate = 19200
        frame = cluster.frames.add(frame_name)
        frame.id = 1
        frame.payload_len = 2
        signal_1 = frame.mux_static_signals.add(signal_1_name)
        signal_1.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_1.data_type = constants.SigDataType.UNSIGNED
        signal_1.start_bit = 0
        signal_1.num_bits = 8
        signal_2 = frame.mux_static_signals.add(signal_2_name)
        signal_2.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_2.data_type = constants.SigDataType.UNSIGNED
        signal_2.start_bit = 8
        signal_2.num_bits = 8

        # Add a LIN ECU and LIN Schedule to the cluster.
        ecu_1 = cluster.ecus.add(ecu_1_name)
        ecu_1.lin_protocol_ver = constants.LinProtocolVer.VER_2_2
        ecu_1.lin_master = True
        ecu_2 = cluster.ecus.add(ecu_2_name)
        ecu_2.lin_protocol_ver = constants.LinProtocolVer.VER_2_2
        ecu_2.lin_master = False
        cluster.lin_tick = 0.01
        schedule = cluster.lin_schedules.add(schedule_name)
        schedule.priority = 0
        schedule.run_mode = constants.LinSchedRunMode.CONTINUOUS
        schedule_entry = schedule.entries.add(schedule_entry_name)
        schedule_entry.delay = 1000.0
        schedule_entry.type = constants.LinSchedEntryType.UNCONDITIONAL
        schedule_entry.frames = [frame]

        # Using the database we just created, write and then read a pair of signals.
        with nixnet.SignalOutSinglePointSession(
                output_interface,
                database_name,
                cluster_name,
                signal_list) as output_session:
            with nixnet.SignalInSinglePointSession(
                    input_interface,
                    database_name,
                    cluster_name,
                    signal_list) as input_session:
                terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
                if terminated_cable.lower() == "y":
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.OFF
                elif terminated_cable.lower() == "n":
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.ON
                else:
                    print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.ON

                # Start the input session manually to make sure that the first
                # signal values sent before the initial read will be received.
                input_session.start()

                # Set the schedule. This will also automatically enable master mode.
                output_session.change_lin_schedule(0)

                # Generate a pair of random values and send out the signals.
                output_values = [randint(0, 255), randint(0, 255)]
                output_session.signals.write(output_values)
                print('Sent signal values: {}'.format(output_values))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                input_signals = input_session.signals.read()
                input_values = [int(value) for timestamp, value in input_signals]
                print('Received signal values: {}'.format(input_values))


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/lin_frame_stream_io.py sha256=88d54b378392cf1b7b16ec9268da95abc140b0cd67cbf7927dee8d6c38be779a bytes=3286 -->
## FILE: nixnet_examples/lin_frame_stream_io.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/lin_frame_stream_io.py`
- sha256: `88d54b378392cf1b7b16ec9268da95abc140b0cd67cbf7927dee8d6c38be779a`
- bytes: 3286

````python
import time

import six

import nixnet
from nixnet import constants
from nixnet import types


def main():
    interface1 = 'LIN1'
    interface2 = 'LIN2'
    database = 'NIXNET_exampleLDF'

    with nixnet.FrameInStreamSession(interface1, database) as input_session:
        with nixnet.FrameOutStreamSession(interface2, database) as output_session:
            terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
            if terminated_cable.lower() == "y":
                input_session.intf.lin_term = constants.LinTerm.ON
                output_session.intf.lin_term = constants.LinTerm.OFF
            elif terminated_cable.lower() == "n":
                input_session.intf.lin_term = constants.LinTerm.ON
                output_session.intf.lin_term = constants.LinTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf.lin_term = constants.LinTerm.ON
                output_session.intf.lin_term = constants.LinTerm.ON

            output_session.intf.lin_master = True

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            # Set the schedule. This will also automatically enable master mode.
            output_session.change_lin_schedule(0)

            user_value = six.moves.input('Enter payload [int, int]: ')
            try:
                payload_list = [int(x.strip()) for x in user_value.split(",")]
            except ValueError:
                payload_list = [2, 4, 8, 16]
                print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

            id = 0
            payload = bytearray(payload_list)
            frame = types.LinFrame(id, constants.FrameType.LIN_DATA, payload)

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.frames.write([frame])
                print('Sent frame with ID: {} payload: {}'.format(frame.identifier,
                                                                  list(frame.payload)))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                frames = input_session.frames.read(count)
                for frame in frames:
                    print('Received frame with ID: {} payload: {}'.format(frame.identifier,
                                                                          list(six.iterbytes(frame.payload))))

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nixnet-python path=nixnet_examples/programmatic_database_usage.py sha256=b588843e693dac492421c0ee8390c9f8330924a997ca862516285d878ed7d848 bytes=2299 -->
## FILE: nixnet_examples/programmatic_database_usage.py

- repository: `ni/nixnet-python`
- source_path: `nixnet_examples/programmatic_database_usage.py`
- sha256: `b588843e693dac492421c0ee8390c9f8330924a997ca862516285d878ed7d848`
- bytes: 2299

````python
import os

import six

import nixnet
from nixnet import constants
from nixnet.system import system
from nixnet import types


def main():
    with system.System() as my_system:
        database_alias = 'custom_database'
        database_filepath = os.path.join(os.path.dirname(__file__), 'databases', 'custom_database.dbc')
        default_baud_rate = 500000
        my_system.databases.add_alias(database_alias, database_filepath, default_baud_rate)

    database_name = 'custom_database'
    cluster_name = 'CAN_Cluster'
    output_frame = 'CANEventFrame1'
    interface = 'CAN1'

    with nixnet.FrameOutQueuedSession(
            interface,
            database_name,
            cluster_name,
            output_frame) as output_session:
        terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
        if terminated_cable.lower() == "y":
            output_session.intf.can_term = constants.CanTerm.OFF
        elif terminated_cable.lower() == "n":
            output_session.intf.can_term = constants.CanTerm.ON
        else:
            print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
            output_session.intf.can_term = constants.CanTerm.ON

        user_value = six.moves.input('Enter payload [int, int]: ')
        try:
            payload_list = [int(x.strip()) for x in user_value.split(",")]
        except ValueError:
            payload_list = [2, 4, 8, 16]
            print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

        id = types.CanIdentifier(0)
        payload = bytearray(payload_list)
        frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)

        print("Writing CAN frames using {} alias:".format(database_name))

        i = 0
        while i < 3:
            for index, byte in enumerate(payload):
                payload[index] = byte + i

            frame.payload = payload
            output_session.frames.write([frame])
            print('Sent frame with ID: {} payload: {}'.format(frame.identifier, list(frame.payload)))
            i += 1

    with system.System() as my_system:
        del my_system.databases[database_name]


if __name__ == '__main__':
    main()
````
