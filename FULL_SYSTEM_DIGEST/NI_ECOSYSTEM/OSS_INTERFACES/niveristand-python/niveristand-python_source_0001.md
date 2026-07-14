# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=.github/CODEOWNERS sha256=ecfe268f9971bef4bc3b65835834c018abc9a0979f3bd22062df7310958b6eb7 bytes=67 -->
## FILE: .github/CODEOWNERS

- repository: `ni/niveristand-python`
- source_path: `.github/CODEOWNERS`
- sha256: `ecfe268f9971bef4bc3b65835834c018abc9a0979f3bd22062df7310958b6eb7`
- bytes: 67

````text
# Add names of code owners for this repo
* @skolthay @gahegde-ni
````

<!--NI_OSS_SOURCE repo=niveristand-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=a0c8bc1ea2a172a416fcaa8a55ce8117b0644e2f886d2e1b47c7ef0574cde061 bytes=656 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/niveristand-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `a0c8bc1ea2a172a416fcaa8a55ce8117b0644e2f886d2e1b47c7ef0574cde061`
- bytes: 656

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/niveristand-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/niveristand-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=.gitignore sha256=fa6551613261abb0b9ce4cb7267f176eb6fbe857a7e31e2dd2bd1d9f8bf1115c bytes=1381 -->
## FILE: .gitignore

- repository: `ni/niveristand-python`
- source_path: `.gitignore`
- sha256: `fa6551613261abb0b9ce4cb7267f176eb6fbe857a7e31e2dd2bd1d9f8bf1115c`
- bytes: 1381

````text
# VeriStand developer configuration files
vsdev.yaml
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# dotenv
.env

# virtualenv
.venv
venv/
ENV/
venv37/
venv38/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# pycharm project files
.idea/
````

<!--NI_OSS_SOURCE repo=niveristand-python path=.readthedocs.yaml sha256=e5af6b06f99473232df2cfc89595fc05150eef1da845ff9afdcb84bd31158e91 bytes=1060 -->
## FILE: .readthedocs.yaml

- repository: `ni/niveristand-python`
- source_path: `.readthedocs.yaml`
- sha256: `e5af6b06f99473232df2cfc89595fc05150eef1da845ff9afdcb84bd31158e91`
- bytes: 1060

````yaml
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.9"
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#   - pdf
#   - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
  install:
    - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=niveristand-python path=CONTRIBUTING.md sha256=a3405f4f634ae21c32f3b0db58fd06106d22fdd35b2fb1a1a731ed61ddd3033a bytes=3834 -->
## FILE: CONTRIBUTING.md

- repository: `ni/niveristand-python`
- source_path: `CONTRIBUTING.md`
- sha256: `a3405f4f634ae21c32f3b0db58fd06106d22fdd35b2fb1a1a731ed61ddd3033a`
- bytes: 3834

````markdown
# Contributing to *niveristand-python* 

Contributions to *niveristand-python* are welcome from all!

*niveristand-python* is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](http://developercertificate.org/).

*niveristand-python* follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Run the unit tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   `GitHub issues page <http://github.com/ni/niveristand-python/issues>`_.
3. Write new tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
4. Make your change.
5. Run all the unit tests again (which include the tests you just added),
   and confirm that they all pass.
6. Send a GitHub Pull Request to the main repository's master branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.

# Testing

Before running any tests, these requirements must be met:

    - A supported version of NI VeriStand must be installed.
    - A supported version of Python must be installed.

**Note**: Many of the tests included require the NI VeriStand `Engine Demo` to be deployed and running on localhost.

To install all development dependencies required:
```
$ pip install -r .\requirements.txt
```

Use the `tox` package for running all tests. To get set up:
```
$ pip install tox
```

That should set up virtualenv and let you run tests on all supported environments.
To run all tests, run the following command:
```
$ tox
```
Every time you run that the package will get created and all tests will run.

To run all tests in place with your current python environment setup:
```
$ pytest
```

To only run the tests in one particular folder, run 
```
$ pytest tests/myfolder
```

# Developer Certificate of Origin (DCO)

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

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/niveristand-python/blob/master/LICENSE)
for details about how *niveristand-python* is licensed.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/clientapi.rst sha256=6a5e6ded9f6987a30da77dd3fb9bf6db8b57bd6878c32ad7f158936a8b3f33d1 bytes=179 -->
## FILE: docs/api_reference/clientapi.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/clientapi.rst`
- sha256: `6a5e6ded9f6987a30da77dd3fb9bf6db8b57bd6878c32ad7f158936a8b3f33d1`
- bytes: 179

````rst
.. _api_clientapi_page:

==========
Client API
==========

.. toctree::
   :maxdepth: 3
   :caption: Client API

   datatypes
   realtimesequence
   stimulusprofileapi
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/datatypes.rst sha256=8bffb39971613d8670c57becd6d2526a7472577504d61f9d71f10252123d6ba5 bytes=5121 -->
## FILE: docs/api_reference/datatypes.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/datatypes.rst`
- sha256: `8bffb39971613d8670c57becd6d2526a7472577504d61f9d71f10252123d6ba5`
- bytes: 5121

````rst
.. _api_datatypes_page:

=======================
NI VeriStand Data types
=======================

.. autoclass:: niveristand.clientapi.BooleanValue
   :show-inheritance:

    Valid initialization values:

    * bool: True, False
    * string: 'true', 'false', 'True', 'False'
    * int, float: every valid value

    Examples:

    .. code-block:: python

        a = BooleanValue(True)
        a = BooleanValue(1.0)
        a = BooleanValue(1)


.. autoclass:: niveristand.clientapi.BooleanValueArray

    Valid initialization values:

    * a list of valid :class:`BooleanValue` initializers.

    Examples:

    .. code-block:: python

        a = BooleanValueArray([True, False])
        a = BooleanValueArray([1.0, 0.0])

.. autoclass:: niveristand.clientapi.ChannelReference
   :show-inheritance:

    Valid initialization values:

    * string: the path or alias for the channel.

    Examples:

    .. code-block:: python

        a = ChannelReference('Aliases/DesiredRPM')
        a = ChannelReference('Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_RPM')

.. autoclass:: niveristand.clientapi.DoubleValue
   :show-inheritance:

    Valid initialization values:

    * (int, float): all valid values.
    * bool: True (1.0), False (0.0)

   Non-float values are converted to their closest floating-point representation. Scientific notation is supported.

    Examples:

    .. code-block:: python

        a = DoubleValue(3.1415)
        a = DoubleValue(0xFFFF)
        a = DoubleValue(True)

.. autoclass:: niveristand.clientapi.DoubleValueArray

    Valid initialization values:

    * a list of valid :class:`DoubleValue` initializers.

    Examples:

    .. code-block:: python

        a = DoubleValueArray([1, 2.0, 0.3, 0x40])

.. autoclass:: niveristand.clientapi.I32Value
   :show-inheritance:

    Valid initialization values:

    * (int, float): [-2,147,483,648 to 2,147,483,647]
    * bool: True (1), False (0)

   Floating-point values are rounded down. Scientific notation is supported.

    Examples:

    .. code-block:: python

        a = I32Value(3)
        a = I32Value(3.1415)
        a = I32Value(0x7FFFFFFF)
        a = I32Value(True)
.. autoclass:: niveristand.clientapi.I32ValueArray

    Valid initialization values:

    * a list of valid :class:`I32Value` initializers.

    Examples:

    .. code-block:: python

        a = I32ValueArray([3, 3.1415, 0x7FFFFFFF, True])
.. autoclass:: niveristand.clientapi.I64Value
   :show-inheritance:

       Valid initialization values:

       * (int, float): [–9,223,372,036,854,775,808 to 9,223,372,036,854,775,807]
       * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

       Examples:

       .. code-block:: python

        a = I64Value(3)
        a = I64Value(3.1415)
        a = I64Value(0x7FFFFFFFFFFFFFFF)
        a = I64Value(-9.2e18)
        a = I64Value(True)
.. autoclass:: niveristand.clientapi.I64ValueArray

    Valid initialization values:

    * a list of valid :class:`I64Value` initializers.

    Examples:

    .. code-block:: python

        a = I64ValueArray([3, 3.1415, 0x7FFFFFFFFFFFFFFF, -9.2e18, True])

.. autoclass:: niveristand.clientapi.U32Value
   :show-inheritance:

       Valid initialization values:

       * (int, float): [0 to 4,294,967,295]
       * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

       Examples:

       .. code-block:: python

        a = U32Value(3)
        a = U32Value(3.1415)
        a = U32Value(0xFFFFFFFF)
        a = U32Value(True)

.. autoclass:: niveristand.clientapi.U32ValueArray

   Valid initialization values:

   * a list of valid :class:`U32Value` initializers.

   Examples:

   .. code-block:: python

      a = U32ValueArray([3, 3.1415, 0xFFFFFFFF, True])

.. autoclass:: niveristand.clientapi.U64Value
   :show-inheritance:

      Valid initialization values:

      * (int, float): [0 to 18,446,744,073,709,551,615]
      * bool: True (1), False (0)

      Floating-point values are rounded down. Scientific notation is supported.

      Examples:

      .. code-block:: python

         a = U64Value(3)
         a = U64Value(3.1415)
         a = U64Value(0x7FFFFFFFFFFFFFFF)
         a = U64Value(18.4e18)
         a = U64Value(True)

.. autoclass:: niveristand.clientapi.U64ValueArray

    Valid initialization values:

    * a list of valid :class:`U64Value` initializers.

    Examples:

    .. code-block:: python

        a = U64ValueArray([3, 3.1415, 0xFFFFFFFFFFFFFFFF, 18.4e18, True])
.. autoclass:: niveristand.clientapi.VectorChannelReference

    Valid initialization values:

    * string: path or alias for the channel.

    Examples:

    .. code-block:: python

        a = VectorChannelReference('engine/a')

.. autoclass:: niveristand.clientapi._datatypes.rtprimitives.DataType
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/decorators.rst sha256=9034cec7eb383d8fa3db365741de132665ada4f403559f9fe788cc001a2dafd0 bytes=349 -->
## FILE: docs/api_reference/decorators.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/decorators.rst`
- sha256: `9034cec7eb383d8fa3db365741de132665ada4f403559f9fe788cc001a2dafd0`
- bytes: 349

````rst
.. _api_decorators_page:

=====================
Decorators
=====================

.. py:decorator:: niveristand.nivs_rt_sequence

    Marks a function as an RT sequence.
    You must mark a function as :any:`nivs_rt_sequence` to run it deterministically with :any:`run_py_as_rtseq`.


.. autoclass:: niveristand.NivsParam
   :members:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/errors.rst sha256=07209b5b5e755788255c249ae0b53e2c261813163f7b874b2d71d37dfb93688f bytes=491 -->
## FILE: docs/api_reference/errors.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/errors.rst`
- sha256: `07209b5b5e755788255c249ae0b53e2c261813163f7b874b2d71d37dfb93688f`
- bytes: 491

````rst
.. _api_errors_page:

======
Errors
======

.. autoclass:: niveristand.errors.VeristandError

.. autoclass:: niveristand.errors.TranslateError
   :show-inheritance:

.. autoclass:: niveristand.errors.SequenceError
   :members:

.. autoclass:: niveristand.errors.RunError
   :show-inheritance:
   :members: get_all_errors

.. autoclass:: niveristand.errors.RunFailedError
   :show-inheritance:

.. autoclass:: niveristand.errors.RunAbortedError
   :show-inheritance:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/legacy.rst sha256=17decedda6a9c06cf15853588bc92e02136781fe1ddf0d28cbf54994a2198a62 bytes=1667 -->
## FILE: docs/api_reference/legacy.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/legacy.rst`
- sha256: `17decedda6a9c06cf15853588bc92e02136781fe1ddf0d28cbf54994a2198a62`
- bytes: 1667

````rst
.. _legacy_clientapi_page:

==========
Legacy API
==========

This module describes the functionality equivalent to the deprecated IronPython API.

.. autoclass:: niveristand.legacy.NIVeriStand.Workspace
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.Workspace2
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.PyAlarmPriority
.. autoclass:: niveristand.legacy.NIVeriStand.PyAlarmState
.. autoclass:: niveristand.legacy.NIVeriStand.PyAlarmMode
.. autoclass:: niveristand.legacy.NIVeriStand.Alarm
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.AlarmManager
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.AlarmManager2
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.PyModelState
.. autoclass:: niveristand.legacy.NIVeriStand.PyModelCommand
.. autoclass:: niveristand.legacy.NIVeriStand.Model
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.ModelManager
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.ModelManager2
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.ChannelFaultManager
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.PyStimulusState
.. autoclass:: niveristand.legacy.NIVeriStand.PyStimulusResult
.. autoclass:: niveristand.legacy.NIVeriStand.Stimulus
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.Stimulus2
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.MacroRecorder
   :members:
.. autoclass:: niveristand.legacy.NIVeriStand.PyMacroPlayerState
.. autoclass:: niveristand.legacy.NIVeriStand.PyMacroPlayerMode
.. autoclass:: niveristand.legacy.NIVeriStand.MacroPlayer
   :members:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/library.rst sha256=2f4467588039beb7a00c27d66e400886ccc8bb4fad83eacbdf241d1bd1a9d567 bytes=1712 -->
## FILE: docs/api_reference/library.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/library.rst`
- sha256: `2f4467588039beb7a00c27d66e400886ccc8bb4fad83eacbdf241d1bd1a9d567`
- bytes: 1712

````rst
.. _api_library_page:

=======
Library
=======

.. autofunction:: niveristand.library.abstime
.. autofunction:: niveristand.library.arraysize
.. autofunction:: niveristand.library.clearfault
.. autofunction:: niveristand.library.clearlasterror
.. autofunction:: niveristand.library.deltat
.. autofunction:: niveristand.library.deltatus
.. autofunction:: niveristand.library.fault
.. autofunction:: niveristand.library.fix
.. autofunction:: niveristand.library.generate_error
.. autofunction:: niveristand.library.getlasterror
.. autofunction:: niveristand.library.iteration
.. autofunction:: niveristand.library.localhost_wait
.. autofunction:: niveristand.library.multitask
.. autofunction:: niveristand.library.nivs_yield
.. autofunction:: niveristand.library.quotient
.. autofunction:: niveristand.library.recip
.. autofunction:: niveristand.library.rand
.. autofunction:: niveristand.library.rem
.. autofunction:: niveristand.library.seqtime
.. autofunction:: niveristand.library.seqtimeus
.. autofunction:: niveristand.library.stop_task
.. autofunction:: niveristand.library.task
.. autofunction:: niveristand.library.tickcountms
.. autofunction:: niveristand.library.tickcountus
.. autofunction:: niveristand.library.wait
.. autofunction:: niveristand.library.wait_until_next_ms_multiple
.. autofunction:: niveristand.library.wait_until_next_us_multiple
.. autofunction:: niveristand.library.wait_until_settled
.. autofunction:: niveristand.library.ramp
.. autofunction:: niveristand.library.sine_wave
.. autofunction:: niveristand.library.square_wave
.. autofunction:: niveristand.library.triangle_wave
.. autofunction:: niveristand.library.uniform_white_noise_wave
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/realtimesequence.rst sha256=56537dc8a4b15f30ff19672cec34a5e68a2fe9757a98f6c443a239f45adbbc44 bytes=248 -->
## FILE: docs/api_reference/realtimesequence.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/realtimesequence.rst`
- sha256: `56537dc8a4b15f30ff19672cec34a5e68a2fe9757a98f6c443a239f45adbbc44`
- bytes: 248

````rst
.. _api_realtimesequence_page:

=======================
Real-Time Sequence APIs
=======================

.. autoclass:: niveristand.clientapi.RealTimeSequence
   :members:

.. autoclass:: niveristand.clientapi.ErrorAction
   :members:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/realtimesequencetools.rst sha256=63303430c9bf9ed69da01a76fe0ed0ea1e4867e748b388fbaf40c14caca2cd8f bytes=182 -->
## FILE: docs/api_reference/realtimesequencetools.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/realtimesequencetools.rst`
- sha256: `63303430c9bf9ed69da01a76fe0ed0ea1e4867e748b388fbaf40c14caca2cd8f`
- bytes: 182

````rst
.. _api_realtimesequencetools_page:

========================
Real-Time Sequence Tools
========================

.. automodule:: niveristand.realtimesequencetools
   :members:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference/stimulusprofileapi.rst sha256=a49a8d40400edde72d1ce856a983156baa899365a7b9f63bfdde0f81793ea15e bytes=181 -->
## FILE: docs/api_reference/stimulusprofileapi.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference/stimulusprofileapi.rst`
- sha256: `a49a8d40400edde72d1ce856a983156baa899365a7b9f63bfdde0f81793ea15e`
- bytes: 181

````rst
.. _api_stimulusprofile_page:

=======================
Stimulus Profile APIs
=======================

.. autoclass:: niveristand.clientapi.StimulusProfileState
   :members:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/api_reference.rst sha256=6a1ebb2403ca8a9b64bb6481c7db9573b31ae98f17a803d3f4ad21a9605837c1 bytes=317 -->
## FILE: docs/api_reference.rst

- repository: `ni/niveristand-python`
- source_path: `docs/api_reference.rst`
- sha256: `6a1ebb2403ca8a9b64bb6481c7db9573b31ae98f17a803d3f4ad21a9605837c1`
- bytes: 317

````rst
.. _api_reference_page:

==============
API Reference
==============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents:

   api_reference/decorators
   api_reference/clientapi
   api_reference/errors
   api_reference/library
   api_reference/realtimesequencetools
   api_reference/legacy
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/basic_rt_sequence_examples.rst sha256=9cc5ab78cca9d726235114651be0bf4ff9fae4fc0ca685fdd0fefb993aed8b70 bytes=2323 -->
## FILE: docs/basic_rt_sequence_examples.rst

- repository: `ni/niveristand-python`
- source_path: `docs/basic_rt_sequence_examples.rst`
- sha256: `9cc5ab78cca9d726235114651be0bf4ff9fae4fc0ca685fdd0fefb993aed8b70`
- bytes: 2323

````rst
.. _basic_rt_sequence_examples:

=================================
Basic Real-time Sequence Examples
=================================

Writing a real-time sequence
----------------------------
A Python real-time sequence is a Python function decorated with the :any:`niveristand.nivs_rt_sequence` decorator.
For example, the following sequence calls a function and checks the result.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: call_add_two_numbers_test

The function also takes in some parameters. You must define parameters using the :any:`niveristand.NivsParam` decorator.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: add_two_numbers

You can now run the test just like any other Python function. You can run it non-deterministically, as in the following example:

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: NON-Deterministic
   :end-before: DETERMINISTIC
   :emphasize-lines: 2

Or, you can run the test deterministically on the VeriStand engine connected to your system.

.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: run_add_two_numbers_tests
   :start-after: DETERMINISTIC
   :emphasize-lines: 2

Combining the legacy API with real-time sequences
-------------------------------------------------

To create a fully-automated test environment, you can mix the :doc:`api_reference/legacy` with Python real-time sequences.

.. literalinclude:: ../examples/legacy_mix.py
   :language: python
   :linenos:

Array operations example
------------------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: array_operations


Measuring elapsed time example
------------------------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: measure_elapsed_time

State machine
-------------
.. literalinclude:: ../examples/basic_rt_sequence_examples.py
   :language: python
   :linenos:
   :pyobject: state_machine_example
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/conf.py sha256=b9f47ff6b9bafd4a8f2514046fc68aab3b650f24f955523813fec98d0f26f2a9 bytes=6019 -->
## FILE: docs/conf.py

- repository: `ni/niveristand-python`
- source_path: `docs/conf.py`
- sha256: `b9f47ff6b9bafd4a8f2514046fc68aab3b650f24f955523813fec98d0f26f2a9`
- bytes: 6019

````python
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------

project = "niveristand-python"
copyright = str(datetime.datetime.now().year) + ", National Instruments"
author = "National Instruments"

# The short X.Y version
version = "3.2"
# The full version, including alpha/beta/rc tags
release = "3.2.3"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "rinoh.frontend.sphinx",  # output to pdf. Requires rinohtype package
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "niveristand-pythondoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "11pt",
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
    (
        master_doc,
        "niveristand-python.tex",
        "niveristand-python Documentation",
        "National Instruments",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "niveristand-python", "niveristand-python Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "niveristand-python",
        "niveristand-python Documentation",
        author,
        "niveristand-python",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

autodoc_mock_imports = [
    "clr",
    "System",
    "System.IO",
    "NationalInstruments",
    "NationalInstruments.VeriStand",
    "NationalInstruments.VeriStand.ClientAPI",
    "NationalInstruments.VeriStand.Data",
    "NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi",
    "NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities",
    "niveristand.clientapi._datatypes.rtprimitives",
]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/engine_demo.rst sha256=18890f26391be71e770ee0a571d6063434d3ce1dff560004878e248c4d2af867 bytes=618 -->
## FILE: docs/engine_demo.rst

- repository: `ni/niveristand-python`
- source_path: `docs/engine_demo.rst`
- sha256: `18890f26391be71e770ee0a571d6063434d3ce1dff560004878e248c4d2af867`
- bytes: 618

````rst
.. _examples_engine_demo:

====================
Engine Demo Examples
====================

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents

Engine Demo Basic
^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/engine_demo/engine_demo_basic.py
   :language: python
   :linenos:

Engine Demo Advanced
^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/engine_demo/engine_demo_advanced.py
   :language: python
   :linenos:


Test Engine Set Points
^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/engine_demo/test_engine_set_points.py
   :language: python
   :linenos:
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/examples.rst sha256=110beab33d3f4e81eb1f6201632ae3b71e88345e6f38d83b8683da6aacde0c8c bytes=195 -->
## FILE: docs/examples.rst

- repository: `ni/niveristand-python`
- source_path: `docs/examples.rst`
- sha256: `110beab33d3f4e81eb1f6201632ae3b71e88345e6f38d83b8683da6aacde0c8c`
- bytes: 195

````rst
.. _examples:

===============
Examples
===============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents

   sysdef_examples
   basic_rt_sequence_examples
   engine_demo
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/getting_started.rst sha256=d62be9cb385aa59d0c5119b15896ded9a38684fa9c9128a0edc1331365993eb7 bytes=1785 -->
## FILE: docs/getting_started.rst

- repository: `ni/niveristand-python`
- source_path: `docs/getting_started.rst`
- sha256: `d62be9cb385aa59d0c5119b15896ded9a38684fa9c9128a0edc1331365993eb7`
- bytes: 1785

````rst
.. _getting_started_page:

===============
Getting Started
===============

Features
========

**niveristand** has two major capabilities: system definition scripting, and real-time sequence scripting and deployment. NI recommends you use an editor with code completion, such as `Visual Studio Code <https://code.visualstudio.com/docs/languages/python/>`_, to make it easier to browse and use this code.

Scripting system definition files
---------------------------------
You can script system definition (.nivssdf) files for use in the NI VeriStand editor and deploy them to the NI VeriStand engine.

Real-time sequences
-------------------
You can create and run NI VeriStand real-time (RT) sequences from Python that work in both the NI VeriStand engine and Stimulus Profile Editor:
- Convert Python functions into real-time sequences and save the converted Python functions to a file.
- Run test sequences in two different modes:

   - Deterministic Mode
      Deploys a real-time sequence to a running NI VeriStand system and executes the sequence in real-time.
   - Python Mode
      Runs a test sequence from a host machine that communicates with an NI VeriStand system through the Gateway.
      Python mode emulates the behavior of Deterministic mode. Python mode is useful in the following cases:

      - You need to debug your real-time sequence.
      - You want to take full advantage of the Python ecosystem.

.. include:: ../README.rst
   :start-after: _installation_section:
   :end-before: _usage_section:

Usage
=====
Refer to :doc:`sysdef_examples` for detailed examples of how to script a system definition file.

Refer to :doc:`basic_rt_sequence_examples` for detailed examples of how to write a Python real-time sequence.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/index.rst sha256=2b636728022404b948472501b511bbb58ecfcfa5b95f4eff3a57ce8a23bfef69 bytes=586 -->
## FILE: docs/index.rst

- repository: `ni/niveristand-python`
- source_path: `docs/index.rst`
- sha256: `2b636728022404b948472501b511bbb58ecfcfa5b95f4eff3a57ce8a23bfef69`
- bytes: 586

````rst
.. niveristand-python documentation master file, created by
   sphinx-quickstart on Thu Mar  1 14:08:07 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VeriStand Python Documentation
==============================================

.. include:: ../README.rst

.. toctree::
   :maxdepth: 3
   :caption: User Documentation:

   getting_started
   examples
   api_reference
   restrictions



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/make.bat sha256=a67a6a467457f3ee8e037eb743bdc5bf94b3ad3c4b346d5e9ab14653f1c780d7 bytes=822 -->
## FILE: docs/make.bat

- repository: `ni/niveristand-python`
- source_path: `docs/make.bat`
- sha256: `a67a6a467457f3ee8e037eb743bdc5bf94b3ad3c4b346d5e9ab14653f1c780d7`
- bytes: 822

````batch
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ=niveristand-python

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

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/Makefile sha256=d05afc96ddda8cd013498f58cd82e58a6e71231187ba9f0b7825541b2485f051 bytes=634 -->
## FILE: docs/Makefile

- repository: `ni/niveristand-python`
- source_path: `docs/Makefile`
- sha256: `d05afc96ddda8cd013498f58cd82e58a6e71231187ba9f0b7825541b2485f051`
- bytes: 634

````text
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = niveristand-python
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

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/requirements.txt sha256=58bf0249c31f3a941f9003fd7d67541d45919afb9adbcc6d450167ae566c9c18 bytes=37 -->
## FILE: docs/requirements.txt

- repository: `ni/niveristand-python`
- source_path: `docs/requirements.txt`
- sha256: `58bf0249c31f3a941f9003fd7d67541d45919afb9adbcc6d450167ae566c9c18`
- bytes: 37

````text
pyyaml
rinohtype
sphinx_rtd_theme
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/restrictions.rst sha256=e6e4802ec0e088bd7fa3e5b20460b1e10c514ed6c8c0b332f042db41360720ae bytes=11217 -->
## FILE: docs/restrictions.rst

- repository: `ni/niveristand-python`
- source_path: `docs/restrictions.rst`
- sha256: `e6e4802ec0e088bd7fa3e5b20460b1e10c514ed6c8c0b332f042db41360720ae`
- bytes: 11217

````rst
.. _restrictions:

============
Restrictions
============

The following section contains a list of all restrictions inside a function using the :any:`nivs_rt_sequence` decorator. If you violate any of the following rules, a :any:`TranslateError` occurs.

Assignment
----------

- To assign values to an existing variable, you must use the `value` property of the object.

    .. code-block:: python

        int_var = I32Value(0)
        int_array_var = I32ValueArray([1, 2, 3])
        # Invalid value assignments
        int_var = 5
        int_array_var = [2, 3, 4]
        int_array_var[2] = 5
        # Valid value assignments
        int_var.value = 5
        int_array_var.value = [2, 3, 4]
        int_array_var[2].value = 5

- Redefining a variable is not allowed.

    .. code-block:: python

        int_var = I32Value(0)
        int_var = DoubleValue(1.0) # The variable is already defined.

Conditional
-----------

- `If` statements only allow for boolean checks. You cannot use numbers, numeric data type declarations, or numeric variables inside `If` statements.

    .. code-block:: python

        # Invalid conditions
        int_var = I32Value(0)
        if 1:
        if I32Value(0):
        if int_var.value:
        # Valid conditions
        bool_var = BooleanValue(True)
        if True:
        if False:
        if BooleanValue(True):
        if bool_var.value

- You cannot use numeric constants or data type declarations inside `If` expressions.

    .. code-block:: python

        # Invalid conditions
        int_var = I32Value(0)
        int_var.value = 1 if 1 else 2
        int_var.value = 1 if DoubleValue(1) else 2
        int_var.value = 1 if int_var.value else 2
        # Valid conditions
        bool_var = BooleanValue(True)
        int_var.value = 1 if True else 2
        int_var.value = 1 if BooleanValue(True) else 2
        int_var.value = 1 if bool_var.value else 2

Data Types
----------

- Vector channel references will only work when you run sequences deterministically.

- Channel references are the only data type declarations you can initialize with strings. All other data type declarations will fail.
    * Note: The BooleanValue data type is an exception to this rule. You can initialize BooleanValue with 'true' 'false' 'True' and 'False'.

    .. code-block:: python

        # Invalid variable declarations
        bool_var = BooleanValue("string")
        double_var = DoubleValue("3.0")
        int32_var = I32Value("1")
        int64_var = I64Value("1")
        uint32_var = U32Value("1")
        uint64_var = U64Value("1")
        bool_array_var = BooleanValueArray([True, "False"])
        double_array_var = DoubleValueArray([3.0, 5.0, "6.0"])
        int32_array_var = I32ValueArray([1, 2, "3"])
        int64_array_var = I64ValueArray([1, 2, "3"])
        uint32_array_var = U32ValueArray([1, 2, "3"])
        uint64_array_var = U64ValueArray([1, 2, "3"])

- Signed integers cannot use the full range of values.

    .. code-block:: python

        int32_invalid_var = I32Value(0xFFFFFFFF)
        int32_last_valid_var = I32Value(0x7FFFFFFF)
        int64_invalid_var = I64Value(0xFFFFFFFFFFFFFFFF)
        int64_last_valid_var = I64Value(0x7FFFFFFFFFFFFFFF)

Error Generation
----------------

-  When you generate an error, you can only use integer constants for the error code parameter, strings for the error message parameter, and ErrorAction members as the error action parameter.

    .. code-block:: python

        # Valid statement
        generate_error(-1, "My error", ErrorAction.AbortSequence)
        # Invalid statements
        int_var = I32Value(-1)
        generate_error(int_var.value, "My error", ErrorAction.AbortSequence)
        generate_error(-1, 2, ErrorAction.AbortSequence)
        generate_error(-1, "My error", 3)

Functions
---------

Built-in Math Functions
^^^^^^^^^^^^^^^^^^^^^^^

- You cannot pass down an NI VeriStand data type directly as a parameter of the built-in math functions. As an alternative, you can pass a variable or data type declaration to these functions using the `value` property.

    .. code-block:: python

        int_var = I32Value(-1)
        # Invalid usage
        int_var.value = abs(I32Value(-1))
        # Valid usages
        int_var.value = abs(I32Value(-1).value)
        int_var.value = abs(int_var.value)

- BooleanValue for `abs` behaves differently between Python and Stimulus Profile Editor.

    .. code-block:: python

        bool_var = BooleanValue(-5)
        bool_var.value = abs(bool_var.value)
        return bool_var.value # This returns False in the Stimulus Profile Editor but returns True in Python.

Built-in VeriStand Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Some of these functions are not implemented in Python. Please refer to :any:`api_reference/library` for more information.

Function Definitions
--------------------

- You cannot define new functions inside an `if` block, a loop, or a task.

- The `*args` and `kwargs` variables are not supported.

Loops
-----

- `For Loops` do not support:
    * `else` blocks
    * ranges with a start value
    * ranges with a step value
    * ranges that use a channel reference
    * ranges that use array constants

    .. code-block:: python

        # The following statements are invalid:
        for x in range(5):
            pass
        else:
            pass
        for x in range(2, 5):
        for x in range(2, 5, 2):
        channel_ref = ChannelReference('Aliases/DesiredRPM')
        for x in range(channel_ref.value):
        for x in [1, 2, 3]:

- `While Loops` do not support:
    * using `else` blocks
    * using a numeric constant as the condition
    * using `break` statements

    .. code-block:: python

        # The following statements are invalid:
        int_var = I32Value(5)
        while 1:
        while int_var:
        while int_var.value:
        while True:
            pass
        else:
            pass
        while True:
            break

Operators
---------

Add
^^^

- You cannot use several pluses one after another. Always use one plus sign. If you violate this rule, a :any:`TranslateError` occurs.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 +++ 2 # This is not supported.
        int_var.value = 1 + 2 # Always use a single plus.

Arithmetic Shift
^^^^^^^^^^^^^^^^

- You cannot use double data types to the left of an arithmetic shift operation in Python.

    .. code-block:: python

        double_var = DoubleValue(5.0)
        # The following statements only work when the code is run deterministically.
        double_var.value = DoubleValue(3.0) << 5
        double_var.value = 3.0 >> 5
        double_var.value = double_var.value >> 5

- You cannot use double or boolean data types to the right of an arithmetic shift operation.

    .. code-block:: python

        bool_var = BooleanValue(True)
        bool_var.value = 5 >> BooleanValue(True)
        bool_var.value = 5 << True
        bool_var.value = 5 << bool_var.value
        double_var = DoubleValue(5.0)
        double_var.value = 5 >> DoubleValue(3.0)
        double_var.value = 5 << 3.0
        double_var.value = 5 << double_var.value

- You cannot use a negative number to the right of an arithmetic shift operation. As an alternative, use the opposite operation with a positive value.

    .. code-block:: python

        int_var = I32Value(1)
        int_var.value = int_var.value >> -2 # This is not allowed.
        int_var.value = int_var.value << 2 # Use this instead.

Bitwise Operators
^^^^^^^^^^^^^^^^^

- You cannot use bitwise operations on float or boolean values in Python.

    .. code-block:: python

        bool_var = BooleanValue(False)
        double_var = DoubleValue(1.0)
        # The following statements only work when the code is run deterministically.
        bool_var.value = BooleanValue(True) & BooleanValue(True)
        double_var.value = 3.5 | 2.5
        double_var.value = DoubleValue(3.5) ^ DoubleValue(2.5)

Comparison Operators
^^^^^^^^^^^^^^^^^^^^

- You cannot use cascading comparison operators. Only use one comparison operator at a time.

    .. code-block:: python

        int_var = I32Value(0)
        int_var.value = 1 == 2 == 3 == 4 # This is not allowed.

Logical Operators
^^^^^^^^^^^^^^^^^

- Logical operators only accept boolean values.

- You cannot use cascading logical operators. Only use one logical operator at a time.

Unary Invert
^^^^^^^^^^^^

- The unary inversion operator (~) only accepts integer values.

Parameters
----------

- If you need to pass an immutable object (such as the `value` property of an NI VeriStand data type) by reference, you must run your code deterministically. Otherwise, the parameter will not actually pass by reference when you run the code in Python.

    .. code-block:: python

        @NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
        @nivs_rt_sequence
        def _increment_by_ref(param):
            param.value += 1
            return param.value


        @nivs_rt_sequence
        def call_increment_by_ref():
            int_var = I32Value(1)
            _increment_by_ref(int_var.value)
            return int_var.value # This will return 1 in Python and 2 in the Stimulus Profile Editor.

Return Statements
-----------------

- A function can only have a single return statement and it has to be the last line of the function.

- You cannot use return statements inside an `if` block, a `try` block, a `finally` block, a loop, a multitask, or a task.

- Return statements can only return scalar values through the `value` property.

    .. code-block:: python

        int_var = I32Value(1)
        int_array_var = I32ValueArray([1, 2, 3])
        # Invalid return statements
        return int_var
        return int_array_var
        return DoubleValueArray[1.0, 2.0]
        # Valid return statements
        return int_var.value
        return int_array_var[0].value

Tasks
-----

- You cannot create more than one task with the same name.

    .. code-block:: python

        with multitask() as mt:
            @task(mt)
            def f1():
                pass
            @task(mt)
            def f1(): # Task with the same name already exists.
                pass

- You cannot create parameters for tasks or multitasks.

    .. code-block:: python

        with multitask(param) as mt: # Parameter not allowed.
            @task(mt)
            def f1(param_task): # Parameter not allowed.

Try
---

- `Try` is only allowed to be the first statement of a function.

- You cannot use a `try` statement within:
    * another `try` statement
    * an `if` block
    * an `else` block
    * a loop
    * a task
    * a multitask

- You cannot use a `try` statement with `except` or `orelse`.

Yield
-----

- You cannot use `yield` as an operator or parameter.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=docs/sysdef_examples.rst sha256=a0cec7fca0bb97bc1041af5214eca3523b9f09fdacd906da0e522d4fff316807 bytes=3015 -->
## FILE: docs/sysdef_examples.rst

- repository: `ni/niveristand-python`
- source_path: `docs/sysdef_examples.rst`
- sha256: `a0cec7fca0bb97bc1041af5214eca3523b9f09fdacd906da0e522d4fff316807`
- bytes: 3015

````rst
.. _sysdef_examples:

==========================
System Definition Examples
==========================

.. contents::
   :depth: 4

Basic Examples
==============

Creating a basic system definition file
---------------------------------------
A system definition can be created with a target operating system of Windows or Linux_x64.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: create_system_definition
   :linenos:
   :start-after: basename(filepath)
   :end-before: return

Be sure to save the system definition when you have made all necessary modifications.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: save_system_definition
   :linenos:
   :start-after: system definition."""


Adding User Channels, Calculated Channels, and Aliases
------------------------------------------------------
User channels can be added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # User Channel
   :end-before: # Procedure

Calculated channels can likewise be added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Calculated Channel
   :end-before: # Alarm

Aliases get added to the system definition root instead of the target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Alias
   :end-before: # FPGA


Adding Alarms and Procedures
----------------------------
Procedures are added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Procedure
   :end-before: # Calculated Channel

Alarms are also added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_remaining
   :linenos:
   :start-after: # Alarm
   :end-before: # Alias


Adding Models
-------------
Models are added to a target.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_models
   :linenos:
   :start-after: definition."""
   :end-before: sinewave_model


More Detailed Examples
======================

DAQ
---
There are many options available when adding DAQ devices.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_daq
   :linenos:
   :start-after: definition."""

CAN
---
An NI-XNET CAN interface can be added.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_can
   :linenos:
   :start-after: definition."""

LIN
---
An NI-XNET LIN interface can be added.

.. literalinclude:: ../examples/sysdef_example.py
   :language: python
   :pyobject: add_lin
   :linenos:
   :start-after: definition."""
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/basic_rt_sequence_examples.py sha256=6b61e511d43897db9dc1b7038aef2322445a9a07ba72543bec4d2b2efb6ecfb0 bytes=6322 -->
## FILE: examples/basic_rt_sequence_examples.py

- repository: `ni/niveristand-python`
- source_path: `examples/basic_rt_sequence_examples.py`
- sha256: `6b61e511d43897db9dc1b7038aef2322445a9a07ba72543bec4d2b2efb6ecfb0`
- bytes: 6322

````python
from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    DoubleValueArray,
    ErrorAction,
    I32Value,
    I64Value,
)
from niveristand.errors import RunError
from niveristand.library import (
    arraysize,
    generate_error,
    iteration,
    nivs_yield,
    rand,
    seqtime,
    seqtimeus,
    tickcountms,
    tickcountus,
    wait,
)
from niveristand.library.waveforms import (
    ramp,
    sawtooth_wave,
    sine_wave,
    square_wave,
    triangle_wave,
    uniform_white_noise_wave,
)


@NivsParam("x", DoubleValue(0), NivsParam.BY_VALUE)
@NivsParam("y", DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def add_two_numbers(x, y):
    result = DoubleValue(0)
    # There is an intentional mistake here. It multiplies when the function implies it adds.
    result.value = x.value * y.value
    return result.value


@nivs_rt_sequence
def call_add_two_numbers_test():
    result = DoubleValue(0)
    result.value = add_two_numbers(1, 2)
    if result.value != 3:
        generate_error(-100, "Unexpected result", ErrorAction.ContinueSequenceExecution)


def run_add_two_numbers_tests():
    # NON-Deterministic
    try:
        call_add_two_numbers_test()
    except RunError as run_error:
        print("Something Non-deterministic went wrong:" + str(run_error))

    # DETERMINISTIC
    try:
        realtimesequencetools.run_py_as_rtseq(call_add_two_numbers_test)
    except RunError as run_error:
        print("Something Deterministic went wrong:" + str(run_error))


@nivs_rt_sequence
def array_operations():
    """
    Shows operations you can perform with array data types in a real-time sequence.

    An array can hold multiple values of the same data type. You cannot have arrays of arrays.
    Use arrays to pass buffers of data for playback or storage.

    Returns:
        float: sum of all values in the array.

    """
    var = DoubleValue(0)
    arr_size = I64Value(0)
    array = DoubleValueArray([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # Indexes a value out of an array.
    var.value = array[4].value + 100
    # Updates a value in an array.
    array[2].value = 6.0
    # Gets the size of an array.
    arr_size.value = arraysize(array)
    # Loops over each element of an array. Each time the loop iterates a value from the array is copied into x.
    var.value = 0.0
    for x in array:
        var.value += x
    return var.value


@nivs_rt_sequence
def measure_elapsed_time():
    """
    Shows different ways to measure elapsed time in a sequence.

    You can measure time in milliseconds, microseconds, or seconds.

    Returns:
        int: time, in milliseconds, it took to run this sequence.

    """
    seqtime_timer = DoubleValue(0)
    seqtime_us_timer = I64Value(0)
    tick_ms_timer = I64Value(0)
    tick_us_timer = I64Value(0)

    # The following steps demonstrate different ways you can capture an initial timestamp:
    seqtime_timer.value = seqtime()
    seqtime_us_timer.value = seqtimeus()
    tick_ms_timer.value = tickcountms()
    tick_us_timer.value = tickcountus()

    # Simulates work to time.
    while iteration() < 1000:
        nivs_yield()

    # Measures the elapsed time by subtracting the initial timestamp from the current time.
    seqtime_timer.value = seqtime() - seqtime_timer.value
    seqtime_us_timer.value = seqtimeus() - seqtime_us_timer.value
    tick_ms_timer.value = tickcountms() - tick_ms_timer.value
    tick_us_timer.value = tickcountus() - tick_us_timer.value

    return tick_ms_timer.value


@nivs_rt_sequence
def state_machine_example():
    state = I32Value(0)
    iters = I32Value(0)
    amplitude = DoubleValue(1000)
    stop = BooleanValue(False)
    output = ChannelReference("Aliases/DesiredRPM")

    while (
        stop.value != True  # noqa: E712 NI recommends you use comparison instead of identity.
        and iters.value < 10
    ):
        state.value = rand(7)
        if state.value == 0:
            wait(2)
        elif state.value == 1:
            sine_wave(output, amplitude, 1, 0, 0, 2)
        elif state.value == 2:
            square_wave(output, amplitude, 5, 0, 0, 50, 2)
        elif state.value == 3:
            triangle_wave(output, amplitude, 1, 0, 0, 2)
        elif state.value == 4:
            uniform_white_noise_wave(output, amplitude, tickcountus(), 2)
        elif state.value == 5:
            ramp(output, -amplitude.value, amplitude, 2)
        elif state.value == 6:
            sawtooth_wave(output, amplitude, 1, 0, 0, 2)
        else:
            stop.value = True
        iters.value += 1
        state.value = rand(7)


def run_non_deterministic(func):
    """Run the sequence in a non-deterministic way.

    This function will execute the RT Sequence on the host using the public ClientAPI
    that is already available to VeriStand users. It will communicate to the gateway to
    set and get channel values.

    If using a python IDE, it's possible to debug this function as any other python function,
    so setting breakpoints, stepping into and over statements, etc., will work as expected.
    """
    result = func()
    print("Function " + func.__name__ + "(None-Deterministic):" + str(result))


def run_deterministic(func):
    """Compile the sequence and run it deterministically inside the VeriStand engine.

    As the actual sequence won't be executed by python, debugging won't be available. Also, only
    functions marked as @nivs_rt_sequence will be accepted.
    """
    # The run_py_as_rtseq function takes as a parameter the function that should be called.
    result = realtimesequencetools.run_py_as_rtseq(func)
    print("Function " + func.__name__ + "(Deterministic):" + str(result))


if __name__ == "__main__":
    run_non_deterministic(array_operations)
    run_deterministic(array_operations)
    run_non_deterministic(measure_elapsed_time)
    run_deterministic(measure_elapsed_time)

    run_add_two_numbers_tests()

    run_deterministic(state_machine_example)
    run_non_deterministic(state_machine_example)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/engine_demo/engine_demo_advanced.py sha256=be70f767f859678fe4dd36829365bec13ce1eb0bd236a65bb3da68b9aba2fcc0 bytes=4267 -->
## FILE: examples/engine_demo/engine_demo_advanced.py

- repository: `ni/niveristand-python`
- source_path: `examples/engine_demo/engine_demo_advanced.py`
- sha256: `be70f767f859678fe4dd36829365bec13ce1eb0bd236a65bb3da68b9aba2fcc0`
- bytes: 4267

````python
from niveristand import nivs_rt_sequence, NivsParam, run_py_as_rtseq
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue
from niveristand.library import multitask, nivs_yield, stop_task, task, wait_until_settled

""" This module adds multitasking, return values, and cleanup tasks to engine_demo_basic.

This example mirrors the 'Engine Demo Advanced and Return Value' example that installs with VeriStand.
Open the 'Engine Demo Advanced and Return Value' stimulus profile to help you understand the following example.
"""


@NivsParam("desired_rpm", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("actual_rpm", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("engine_temp", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def engine_demo_advanced(desired_rpm, actual_rpm, engine_temp):
    """Turns on the engine, sets it to the desired rpm, and monitors the engine temperature."""
    # Use the following local variable declarations to keep track of the test's status:
    warmup_complete = BooleanValue(False)
    warmup_succeeded = BooleanValue(False)

    # Create a multitask with two tasks: one for setting rpm values and another for monitoring.
    # In general, a multitask can contain as many tasks as desired. The tasks will all execute asynchronously,
    # but not in parallel. For more information on multitask behavior, refer to the VeriStand help.
    with multitask() as mt:
        # You must decorate tasks using the following notation.
        # The following code shows example of a task.
        @task(mt)
        def engine_warmup():
            """Spawns a task to wait for the actual rpm signal to settle."""
            desired_rpm.value = 2500
            # Waits for up to 120 seconds for the actual RPM to be between 999999 and 2450 for 25 seconds.
            wait_until_settled(actual_rpm, 9999999, 2450, 25, 120)
            desired_rpm.value = 8000
            wait_until_settled(actual_rpm, 9999999, 7800, 25, 120)
            warmup_complete.value = True

        @task(mt)
        def monitor_temp():
            """Spawns a task to monitor engine temperature.

            If the temperature rises above 110 degrees (C), the previous task will stop.
            """
            while warmup_complete.value is False:
                if engine_temp.value > 110:
                    stop_task(engine_warmup)
                    warmup_complete.value = True
                    warmup_succeeded.value = False
                nivs_yield()

    # You can use a return value, but some restrictions will apply.
    # For example, the function may only return previously declared variables.
    return warmup_succeeded.value


@nivs_rt_sequence
def run_engine_demo_advanced():
    """Run the engine_demo_advanced example.

    To handle a condition that stops a task (such as, the engine temperature rising above a safe value),
    use a try/finally block.

    Regardless of the result of the execution, the finally block can be used to safely shut down the engine.
    """
    try:
        warmup_succeeded = BooleanValue(False)
        engine_power = ChannelReference("Aliases/EnginePower")
        desired_rpm = ChannelReference("Aliases/DesiredRPM")
        actual_rpm = ChannelReference("Aliases/ActualRPM")
        engine_temp = ChannelReference("Aliases/EngineTemp")
        engine_power.value = True
        warmup_succeeded.value = engine_demo_advanced(desired_rpm, actual_rpm, engine_temp)
    finally:
        engine_power.value = False
        desired_rpm.value = 0
    return warmup_succeeded.value


def run_deterministic():
    return run_py_as_rtseq(run_engine_demo_advanced, target=None)


def run_non_deterministic():
    return run_engine_demo_advanced()


if __name__ == "__main__":
    # Run the tests.
    # Note:  We expect the tests to fail because the engine temperature rises above 110 degrees (C),
    # but the cleanup code at the end turns the engine off.
    print("Non-Deterministic test:")
    print("Test Passed!" if run_non_deterministic() else "Test Failed (expected)!")
    print("Deterministic test:")
    print("Test Passed!" if run_deterministic() else "Test Failed (expected)!")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/engine_demo/engine_demo_basic.py sha256=b371e4489283a353ac4f1ba02edaac91738b1803354452ffb95a65746d823dae bytes=2978 -->
## FILE: examples/engine_demo/engine_demo_basic.py

- repository: `ni/niveristand-python`
- source_path: `examples/engine_demo/engine_demo_basic.py`
- sha256: `b371e4489283a353ac4f1ba02edaac91738b1803354452ffb95a65746d823dae`
- bytes: 2978

````python
from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue
from niveristand.library import wait

""" This module contains a basic example of how to create an RT sequence in Python.

This example mirrors the 'Engine Demo Basic' example that installs with VeriStand.
Open the 'Engine Demo Basic' stimulus profile to help you understand the following example.
"""


# You must mark RT sequences with the following decorator:
@nivs_rt_sequence
# You must also specify parameter data types, default values, and whether to pass parameters by value or by reference.
@NivsParam("engine_power", BooleanValue(0), NivsParam.BY_REF)
@NivsParam("desired_rpm", DoubleValue(0), NivsParam.BY_REF)
def engine_demo_basic(engine_power, desired_rpm):
    """Turn on the engine, set the desired_rpm to the passed value for 20 seconds, and shut down the engine.

    You must access parameters through their ".value" property.
    """
    # You can access a channel with a ChannelReference
    engine_power_chan = ChannelReference("Aliases/EnginePower")
    desired_rpm_chan = ChannelReference("Aliases/DesiredRPM")
    engine_power_chan.value = engine_power.value
    desired_rpm_chan.value = desired_rpm.value
    wait(DoubleValue(20))
    engine_power_chan.value = False
    desired_rpm_chan.value = 0


@nivs_rt_sequence
def run_engine_demo():
    """Sets up channel references and calls the actual test."""
    # You can call an RT sequence the same way you call a normal Python function.
    # However, if you pass functions by reference, you must create strongly-typed objects.
    engine_demo_basic(BooleanValue(True), DoubleValue(2500))


def run_non_deterministic():
    """Runs the sequence non-deterministically.

    This function executes the RT Sequence on the host using the public ClientAPI
    that installs with VeriStand. This function communicates with the gateway to set and get channel values.

    If you use a Python integrated developer environment (IDE),
    you can debug this function like a normal Python function.
    """
    run_engine_demo()


def run_deterministic():
    """Compiles the sequence and runs it deterministically inside the VeriStand engine.

    You cannot use debugging tools at this stage because VeriStand executes the sequence, not Python.
    If you do not mark the functions as @nivs_rt_sequence, Python will raise a :any:`niveristand.errors.VeristandError`.
    """
    # The run_py_as_rtseq function accepts, as a parameter, the Python function you want to call as an RT sequence.
    realtimesequencetools.run_py_as_rtseq(run_engine_demo)


if __name__ == "__main__":
    realtimesequencetools.save_py_as_rtseq(run_engine_demo, "d:\\share\\temp\\demo")
    run_non_deterministic()
    print("Finished non-deterministic")
    run_deterministic()
    print("Finished deterministic")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/engine_demo/test_engine_set_points.py sha256=2a42503a8e1cad1f3983113212651b062e3564205b92b7548ff8a5409088cefd bytes=3791 -->
## FILE: examples/engine_demo/test_engine_set_points.py

- repository: `ni/niveristand-python`
- source_path: `examples/engine_demo/test_engine_set_points.py`
- sha256: `2a42503a8e1cad1f3983113212651b062e3564205b92b7548ff8a5409088cefd`
- bytes: 3791

````python
from niveristand import nivs_rt_sequence, NivsParam, run_py_as_rtseq
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, DoubleValueArray
from niveristand.library import localhost_wait, seqtime, wait_until_settled


""" This module contains a complex example for running multiple tests in sequence.

This example mirrors the 'Test Engine Setpoints' stimulus profile found in the examples that install with VeriStand.

Instead of using a stimulus profile to report results, this example uses the py.test
unit-testing framework that is commonly used for running Python tests.
"""


@nivs_rt_sequence
@NivsParam("on_off", BooleanValue(False), NivsParam.BY_VALUE)
def set_engine_power(on_off):
    """Turns the engine on or off."""
    engine_power = ChannelReference("Aliases/EnginePower")
    engine_power.value = on_off.value


# If you do not specify a parameter decorator, the parameter defaults to the following:
# Type=DoubleValue
# Default Value = 0
# Passed by reference.
# In this case, the default is adequate, so you do not need to specify the decorator.
@nivs_rt_sequence
def measure_set_point_response(setpoint, timeout, tolerance):
    """Sets the desired rpm to the specified setpoint and wait until the signal settles.

    The tolerance is used to create upper and lower boundaries for the signal.
    Returns the amount of time it takes the signal to settle or timeout.
    """
    actual_rpm = ChannelReference("Aliases/ActualRPM")
    desired_rpm = ChannelReference("Aliases/DesiredRPM")
    start_time = DoubleValue(0)
    settle_time = DoubleValue(0)

    desired_rpm.value = setpoint.value
    # Waits .5 seconds, so the gateway has time to update.
    localhost_wait(0.5)

    start_time.value = seqtime()
    wait_until_settled(
        actual_rpm,
        desired_rpm.value + tolerance.value,
        desired_rpm.value - tolerance.value,
        DoubleValue(2.0),
        timeout.value,
    )
    settle_time.value = seqtime() - start_time.value
    return settle_time.value


@nivs_rt_sequence
def inbounds_check(test_value, upper, lower):
    """Returns True if lower <= value <= upper.

    Performs an inbounds check.
    """
    result = BooleanValue(False)
    # Typically, you could write this instruction as lower.value <= test_value.value <= upper.value
    # because Python supports cascading operators. However, for real-time sequences,
    # you must write all comparisons using only two operands.
    result.value = test_value.value >= lower.value and test_value.value <= upper.value
    return result.value


# The following function runs the profile above deterministically.
# A unit test framework, such as py.test, can find the function.
def test_run_engine_set_points_profile_deterministic():
    set_engine_power(True)
    setpoints = DoubleValueArray([2500, 6000, 3000])
    try:
        for setpoint in setpoints:
            test_passed = run_py_as_rtseq(
                measure_set_point_response,
                {"setpoint": setpoint, "timeout": DoubleValue(60), "tolerance": DoubleValue(100)},
            )
            assert 0 < test_passed <= 60, "Setpoint %d failed" % setpoint
    finally:
        set_engine_power(False)


# If you do not need to run the profile deterministically, you can run this function as part of a py.test run.
def test_run_engine_set_points_python():
    set_engine_power(True)
    setpoints = DoubleValueArray([2500, 6000, 3000])
    try:
        for setpoint in setpoints:
            assert (
                0 < measure_set_point_response(setpoint, DoubleValue(60), DoubleValue(100)) <= 60
            ), ("Setpoint %d failed" % setpoint)
    finally:
        set_engine_power(False)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/legacy_basic_reconnect.py sha256=9f0240bff6338de4100a859e8c34037f68e2d27b851fab394d86d33f8f3e37ab bytes=1946 -->
## FILE: examples/legacy_basic_reconnect.py

- repository: `ni/niveristand-python`
- source_path: `examples/legacy_basic_reconnect.py`
- sha256: `9f0240bff6338de4100a859e8c34037f68e2d27b851fab394d86d33f8f3e37ab`
- bytes: 1946

````python
import sys
import time
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand

# This is an example script to demonstrate the usage of ReconnectToSystem function.
# This script requires cPython(tested on cPython 3.9.6) and (obviously) NIVeriStand Python API.

# This script deploys example project on the selected GATEWAY and it prints two channel values every 100ms
# This script requires the example SineWave Delay Project(shipped with LabVIEW 2020) to be deployed.
# SineWave Delay project file path:
#    C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects\Example\Sinewave Delay.nivsproj
# Press Ctrl + C to stop the program.

GATEWAY = "localhost"
TARGET = "Controller"

SINE_WAVE = "Aliases/SineWave"
LOOP_RATE = "Targets/Controller/System Channels/Actual Loop Rate"
# channel adresses can be entered as full paths or aliases


def sleep():
    time.sleep(0.1)


wks = NIVeriStand.Workspace2(GATEWAY)  # create workspace object
try:
    print(
        "Connecting to the gateway %(gateway)s, target %(target)s"
        % {"gateway": GATEWAY, "target": TARGET}
    )
    wks.ReconnectToSystem(TARGET, True, None, 60000)  # reconnect to already deployed system
    print("NI VeriStand Running and Client Connected!")
    input("Press Enter to start printing data values, then you can press Ctrl+C to disconnect.")

    while 1:
        print("Actual Loop Rate: ", wks.GetSingleChannelValue(LOOP_RATE))
        print("Sine wave:", wks.GetSingleChannelValue(SINE_WAVE))
        print("")
        sleep()

except RunError as err:
    TEST_COMMENT = "Unexpected Exception " + err.error.message()
    print(TEST_COMMENT)
    time.sleep(10)
except KeyboardInterrupt:
    print("Press any button to exit script.")
except Exception:
    print(sys.exc_info())
    time.sleep(10)
finally:
    wks.DisconnectFromSystem("", True)  # undeploy project
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/legacy_mix.py sha256=920cc79f2b165bba92d5c37afe7ee25e6272795d12e8cae58ab5ae6ae7c9eee0 bytes=1415 -->
## FILE: examples/legacy_mix.py

- repository: `ni/niveristand-python`
- source_path: `examples/legacy_mix.py`
- sha256: `920cc79f2b165bba92d5c37afe7ee25e6272795d12e8cae58ab5ae6ae7c9eee0`
- bytes: 1415

````python
import os
from examples.engine_demo.engine_demo_basic import run_engine_demo
from niveristand import run_py_as_rtseq
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand


def mix_legacy_and_rtseq_run():
    """Combines the legacy API with Python real-time sequences to run a deterministic test."""
    # Ensures NI VeriStand is running.
    NIVeriStand.LaunchNIVeriStand()
    NIVeriStand.WaitForNIVeriStandReady()
    # Uses the ClientAPI interface to get a reference to Workspace2
    workspace = NIVeriStand.Workspace2("localhost")
    engine_demo_path = os.path.join(
        os.path.expanduser("~public"),
        "Documents",
        "National Instruments",
        "NI VeriStand 2019",
        "Examples",
        "Stimulus Profile",
        "Engine Demo",
        "Engine Demo.nivssdf",
    )
    # Deploys the system definition.
    workspace.ConnectToSystem(engine_demo_path, True, 120000)
    try:
        # Uses Python real-time sequences to run a test.
        run_py_as_rtseq(run_engine_demo)
        print("Test Success")
    except RunError as e:
        print("Test Failed: %d -  %s" % (int(e.error.error_code), e.error.message))
    finally:
        # You can now disconnect from the system, so the next test can run.
        workspace.DisconnectFromSystem("", True)


if __name__ == "__main__":
    mix_legacy_and_rtseq_run()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/sdf_deploy_with_deploy_option.py sha256=59380d1b92f745bf7df000f0a97a72ff7cc2e9960011aeb09b5cf25b638a2382 bytes=1949 -->
## FILE: examples/sdf_deploy_with_deploy_option.py

- repository: `ni/niveristand-python`
- source_path: `examples/sdf_deploy_with_deploy_option.py`
- sha256: `59380d1b92f745bf7df000f0a97a72ff7cc2e9960011aeb09b5cf25b638a2382`
- bytes: 1949

````python
import os
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand


def sdf_deploy_with_deploy_option():
    """Use legacy API to deploy a system definition along with deploy option."""
    # Ensures NI VeriStand is running.
    NIVeriStand.LaunchNIVeriStand()
    NIVeriStand.WaitForNIVeriStandReady()

    # Uses the ClientAPI interface to get a reference to Workspace2
    # For deployment in RT, make sure the model in the system definition is Linux compatible.
    # (e.g., \National Instruments\NI VeriStand *\Examples\Stimulus Profile\Engine Demo\Model\EngineDemo_linux.vsmodel)
    workspace = NIVeriStand.Workspace2("localhost")
    engine_demo_path = os.path.join(
        os.path.expanduser("~public"),
        "Documents",
        "National Instruments",
        "NI VeriStand 2021",
        "Examples",
        "Stimulus Profile",
        "Engine Demo",
        "Engine Demo.nivssdf",
    )

    try:
        # Example: Deploys the system definition with deploy option.
        # calibration_file: path of calibration file
        # filtered_targets: list of strings (target)
        calibration_file = os.path.join(
            os.path.expanduser("~public"),
            "Documents",
            "National Instruments",
            "NI VeriStand 2021",
            "Examples",
            "Stimulus Profile",
            "Engine Demo",
            "Engine Demo.nivscf",
        )
        filtered_targets = None
        workspace.ConnectToSystem(engine_demo_path, True, 120000, calibration_file, filtered_targets)
        print("Test Success")
    except RunError as e:
        print("Test Failed: %d - %s" % (int(e.error.error_code), e.error.message))
    finally:
        # You can now disconnect from the system, so the next test can run.
        workspace.DisconnectFromSystem("", True)


if __name__ == "__main__":
    sdf_deploy_with_deploy_option()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/sysdef_example.py sha256=4d98c7555a6dc3a69bef15dbbbf73915809f7f2fd4687ab72c9b19f8988c36eb bytes=14420 -->
## FILE: examples/sysdef_example.py

- repository: `ni/niveristand-python`
- source_path: `examples/sysdef_example.py`
- sha256: `4d98c7555a6dc3a69bef15dbbbf73915809f7f2fd4687ab72c9b19f8988c36eb`
- bytes: 14420

````python
"""Create an empty system definition."""
from __future__ import annotations

import os
import sys

sys.path.append(r"C:\Program Files\National Instruments\VeriStand 2024")
from niveristand import VeriStandSdfError  # noqa: E402
from niveristand.systemdefinitionapi import (  # noqa: E402
    AcquisitionMode,
    AlarmMode,
    AlarmPriority,
    AlarmState,
    Alias,
    AliasFolder,
    CANPort,
    DAQAnalogInput,
    DAQAnalogOutput,
    DAQCounterEdge,
    DAQDevice,
    DAQDeviceInputConfiguration,
    DAQDigitalInput,
    DAQDigitalOutput,
    DAQDIOPort,
    DAQFrequencyMeasurement,
    DAQInternalChannel,
    DAQMeasurementType,
    DAQPulseGeneration,
    DAQTaskAI,
    DAQTriggerDigitalEdge,
    DAQWaveformAnalogInput,
    Database,
    DataFileReplay,
    DataLoggingFile,
    DirectionType,
    FileType,
    LINPort,
    LowpassFilter,
    Model,
    PolynomialScale,
    Procedure,
    SampleMode,
    SetVariableStepFunction,
    SignalBasedFrame,
    SystemDefinition,
    XNETTermination,
)


def main(filepath=None):
    """The main portion of the script."""
    try:
        print("Creating System Definition...")
        if not filepath:
            filepath = os.path.join(os.path.dirname(__file__), "combined.nivssdf")
        system_definition = create_system_definition(filepath)

        print("Adding and populating DAQ Devices... ")
        add_daq(system_definition)

        print("Adding and populating XNET Devices... ")
        add_can(system_definition)
        add_lin(system_definition)

        print("Adding and populating Simulation Models... ")
        add_models(system_definition)

        print("Adding user channels, alarms, procedures, aliases, etc... ")
        add_remaining(system_definition)

        save_system_definition(system_definition)
    except BaseException as e:
        if isinstance(e, VeriStandSdfError):
            print(f"\nVeriStandSdfError: {str(e)}", end="")
        elif str(type(e)) == "<class 'NationalInstruments.VeriStand.VeriStandException'>":
            # VeriStandSdfError gives better error messages
            print(f"\nVeriStandException: {VeriStandSdfError(e.Code)}", end="")
        # re-raise the exception to print the stack trace to the console
        raise


def get_asset(filename: str) -> str:
    """Returns the path to an asset for this example."""
    return os.path.join(
        os.path.realpath(os.path.dirname(__file__)), "sysdef_example_assets", filename
    )


def create_system_definition(filepath: str, ip_address: str = "localhost") -> SystemDefinition:
    """Creates the system definition."""
    filename = os.path.basename(filepath)
    is_local = ip_address == "localhost" or ip_address == "127.0.0.1"
    target_type = "Windows" if is_local else "Linux_x64"
    system_definition = SystemDefinition(
        filename,
        "This is an example System Definition file created using the System Definition API",
        "System Definition API",
        "1.0.0.0",
        "Controller",
        target_type,
        filepath,
    )

    target = system_definition.root.get_targets().get_target_list()[0]
    if not is_local:
        target.ip_address = ip_address
    return system_definition


def add_daq(system_definition: SystemDefinition):
    """Adds a DAQ device to the system definition."""
    daq_device = DAQDevice(
        "Dev1",
        "This is a DAQ Device created using the System Definition Offline API.",
        DAQDeviceInputConfiguration.DEFAULT,
    )
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_daq().add_device(daq_device)

    # Analog Input Channels
    analog_inputs = daq_device.create_analog_inputs()
    analog_inputs.add_analog_input(
        DAQAnalogInput("AI0", 1, DAQMeasurementType.ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE)
    )
    analog_inputs.add_analog_input(
        DAQAnalogInput("AI1", 0, DAQMeasurementType.ANALOG_INPUT_VOLTAGE)
    )

    # Analog Output Channels
    analog_outputs = daq_device.create_analog_outputs()
    analog_outputs.add_analog_output(
        DAQAnalogOutput("AO0", 0, DAQMeasurementType.ANALOG_OUTPUT_VOLTAGE)
    )

    # Digital Input Channels
    digital_inputs = daq_device.create_digital_inputs()
    daq_input_port = DAQDIOPort(0, False)
    digital_inputs.add_dio_port(daq_input_port)
    daq_input_port.add_digital_input(DAQDigitalInput("DI0", False, 0, 0))
    daq_input_port.add_digital_input(DAQDigitalInput("DI1", False, 1, 0))

    # Digital Output Channels
    digital_outputs = daq_device.create_digital_outputs()
    daq_output_port = DAQDIOPort(1, False)
    digital_outputs.add_dio_port(daq_output_port)
    daq_output_port.add_digital_output(DAQDigitalOutput("DO4", False, 4, 1))

    # Counter Channels
    counters = daq_device.create_counters()
    counters.add_counter(
        DAQFrequencyMeasurement("FreqIn", "", 0, 0.0, 1.0, 0.0, DAQCounterEdge.FALLING)
    )
    counters.add_counter_output(DAQPulseGeneration("PWMOut", "", 1))

    # Internal Channels
    internal_channels = daq_device.create_internal_channels()
    internal_channels.add_internal_channel(DAQInternalChannel("Channel 0", 0.0))

    # Waveform Tasks
    daq_device_waveform = DAQDevice("Dev2", "", DAQDeviceInputConfiguration.DEFAULT)
    chassis.get_daq().add_device(daq_device_waveform)
    daq_tasks = chassis.get_daq().get_tasks()
    waveform_task = DAQTaskAI("Task1", 1000, AcquisitionMode.CONTINUOUS)
    waveform_task.get_triggers().start_trigger = DAQTriggerDigitalEdge(
        "PFI0", DirectionType.FALLING
    )
    daq_tasks.add_task(waveform_task)
    analog_waveform_input = DAQWaveformAnalogInput(
        "AI2", 0, DAQMeasurementType.ANALOG_INPUT_CURRENT
    )
    waveform_analog_inputs = daq_device_waveform.create_analog_inputs()
    waveform_analog_inputs.sample_mode = SampleMode.WAVEFORM
    waveform_analog_inputs.add_waveform_analog_input(analog_waveform_input)
    waveform_analog_inputs.waveform_analog_input_task = waveform_task

    # Polynomial Scale
    coefficients = [1.0]
    reverse_coefficients = []
    scale = PolynomialScale("MyScale", coefficients, reverse_coefficients, "")
    system_definition.root.get_scales().add_scale(scale)
    daq_device.get_analog_input_section().get_analog_input_list()[0].scale = scale


def add_can(system_definition: SystemDefinition):
    """Adds the CAN section to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_xnet().enable_xnet()  # enable XNET if we haven't already

    target.get_user_channels().add_new_user_channel("MyXnetUserChannel", "", "", 1.0)
    user_channel = target.get_user_channels().get_user_channel_list()[0]

    # CAN Database
    can = chassis.get_xnet().get_can()
    can_database = Database("NIXNET_example")
    target.get_xnet_databases().add_database(can_database)

    # CAN Cluster
    can_cluster = "CAN_Cluster"
    can_port = CANPort("CAN 1", 1, can_database, can_cluster, 125000)
    can_port.termination = XNETTermination.ON
    can.add_can_port(can_port)

    # Frame Variables
    cyclic_frame = "CANCyclicFrame1"
    cyclic_frame_signals = ["CANCyclicSignal1", "CANCyclicSignal2"]
    event_frame = "CANEventFrame1"
    event_frame_signals = ["CANEventSignal1", "CANEventSignal2"]

    # CAN Incoming Frames
    incoming_cyclic_frame = SignalBasedFrame(
        cyclic_frame, 64, can_database, can_cluster, 8, 0.1, False, cyclic_frame_signals
    )
    can_port.get_incoming().get_single_point().add_signal_based_frame(incoming_cyclic_frame)
    for signal in cyclic_frame_signals:
        incoming_cyclic_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    incoming_event_frame = SignalBasedFrame(
        event_frame, 66, can_database, can_cluster, 8, 0.1, False, event_frame_signals
    )
    can_port.get_incoming().get_single_point().add_signal_based_frame(incoming_event_frame)
    for signal in event_frame_signals:
        incoming_event_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    incoming_cyclic_frame.create_frame_information()

    incoming_data_logging = DataLoggingFile(
        "log", "file", os.path.dirname(system_definition.document_type.document_file_path)
    )
    incoming_data_logging.data_logging_file_type = FileType.TDMS
    can_port.get_incoming().get_raw_frame_data_logging().add_data_logging_file(
        incoming_data_logging
    )
    can_port.get_incoming().get_raw_frame_data_logging().get_data_logging_file_list()[
        0
    ].trigger_channel = user_channel

    # CAN Outgoing Frames
    outgoing_cyclic_frame = SignalBasedFrame(
        cyclic_frame, 64, can_database, can_cluster, 8, 0.1, False, cyclic_frame_signals
    )
    can_port.get_outgoing().get_cyclic().add_signal_based_frame(outgoing_cyclic_frame)
    for signal in cyclic_frame_signals:
        outgoing_cyclic_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    outgoing_event_frame = SignalBasedFrame(
        event_frame, 64, can_database, can_cluster, 8, 0.1, False, event_frame_signals
    )
    can_port.get_outgoing().get_event_triggered().add_signal_based_frame(outgoing_event_frame)
    for signal in event_frame_signals:
        outgoing_event_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    outgoing_cyclic_frame.create_frame_faulting(True, True)
    outgoing_cyclic_frame.get_frame_faulting().get_skip_cyclic_frames().trigger_channel = (
        user_channel
    )
    outgoing_cyclic_frame.get_frame_faulting().get_transmit_time().set_trigger_channel(user_channel)

    outgoing_data_replay = DataFileReplay("replay", get_asset("fake.tdms"))
    can_port.get_outgoing().get_data_replay().add_data_file_replay(outgoing_data_replay)
    can_port.get_outgoing().get_data_replay().get_data_file_replay_list()[
        0
    ].trigger_channel = user_channel


def add_lin(system_definition: SystemDefinition):
    """Adds a LIN section to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]
    chassis.get_xnet().enable_xnet()  # enable XNET if we haven't already

    # LIN Database
    lin = chassis.get_xnet().get_lin()
    lin_database = Database("NIXNET_exampleLDF")
    target.get_xnet_databases().add_database(lin_database)

    # LIN Cluster
    lin_cluster = "Cluster"
    lin_port = LINPort("LIN 1", 1, lin_database, lin_cluster, 125000, "SlowSchedule")
    lin.add_lin_port(lin_port)

    # LIN Incoming Frame
    incoming_signals = ["SlaveSignal3_U8", "SlaveSignal4_U8"]
    incoming_frame = SignalBasedFrame(
        "Slave1Frame2", 5, lin_database, lin_cluster, 8, 0.1, False, incoming_signals
    )
    lin_port.get_incoming().get_single_point().add_signal_based_frame(incoming_frame)
    for signal in incoming_signals:
        incoming_frame.create_signal_based_signal(signal, "", "volts", 0.0)

    # LIN Outgoing Frame
    outgoing_signals = ["MasterSignal3_U8", "MasterSignal4_U8"]
    outgoing_frame = SignalBasedFrame(
        "MasterFrame2", 3, lin_database, lin_cluster, 8, 0.1, False, outgoing_signals
    )
    lin_port.get_outgoing().get_unconditional().add_signal_based_frame(outgoing_frame)
    for signal in outgoing_signals:
        outgoing_frame.create_signal_based_signal(signal, "", "volts", 0.0)


def add_models(system_definition: SystemDefinition):
    """Adds models to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    simulation_models = target.get_simulation_models()

    random_model = Model("RandomFMU", "", get_asset("RandomFMU.fmu"), 0, 1, 0, True, True, True)
    simulation_models.get_models().add_model(random_model)

    sinewave_model = Model(
        "SinewaveFMU", "", get_asset("SinewaveFMU.fmu"), 0, 1, 0, True, True, True
    )
    simulation_models.get_models().add_model(sinewave_model)


def add_remaining(system_definition: SystemDefinition):
    """Add other items to the system definition."""
    target = system_definition.root.get_targets().get_target_list()[0]
    chassis = target.get_hardware().get_chassis_list()[0]

    # User Channel
    target.get_user_channels().add_new_user_channel("MyUserChannel", "", "", 1.0)
    user_channel = target.get_user_channels().get_user_channel_list()[1]

    # Procedure
    procedure = Procedure("MyProcedure", "")
    procedure.add_new_dwell("Dwell Step", "Dwell for 3 seconds.", 3)
    procedure.add_new_set_variable(
        "Counting Step", "", user_channel, SetVariableStepFunction.ADD, user_channel, 1
    )
    target.get_procedures().add_procedure(procedure)

    # Calculated Channel
    lpf_calculated_channel = LowpassFilter("MyLowpassFilterChannel", "", user_channel, 50, 1)
    target.get_calculated_channels().add_calculated_channel(lpf_calculated_channel)

    # Alarm
    target.get_alarms().add_new_alarm(
        "MyAlarm",
        "",
        user_channel,
        2,
        1,
        procedure,
        AlarmMode.NORMAL,
        AlarmState.ENABLED,
        AlarmPriority.LOW,
        0,
        "",
    )

    # Alias
    alias = Alias("MyUserChannelAlias", "", user_channel)
    alias_folder = AliasFolder("MyAliasFolder", "")
    system_definition.root.get_aliases().add_alias_folder(alias_folder)
    system_definition.root.get_aliases().get_alias_folder_list()[0].add_alias(alias)

    # FPGA
    chassis.get_fpga().add_fpga_device(
        get_asset("PXIe-7867R Analog, PWM, Digital Lines.fpgaconfig")
    )


def save_system_definition(system_definition: SystemDefinition):
    """Saves the system definition."""
    filepath = system_definition.document_type.document_file_path
    saved, error = system_definition.save_system_definition_file()
    if saved:
        print(f'System Definition saved to "{filepath}"')
    else:
        raise FileNotFoundError(f'Unable to save System Definition to "{filepath}": {error}')


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/sysdef_example_assets/fake.tdms sha256=af8458dcecd6f22697ca4bcd23ef64acc698a242d9515737c89fe8f9726a95c9 bytes=12 -->
## FILE: examples/sysdef_example_assets/fake.tdms

- repository: `ni/niveristand-python`
- source_path: `examples/sysdef_example_assets/fake.tdms`
- sha256: `af8458dcecd6f22697ca4bcd23ef64acc698a242d9515737c89fe8f9726a95c9`
- bytes: 12

````text
foo for xnet
````

<!--NI_OSS_SOURCE repo=niveristand-python path=examples/sysdef_example_assets/PXIe-7867R Analog, PWM, Digital Lines.fpgaconfig sha256=ba078441fcd7b11da6ada5185b5d384a3a0b34092400886afe76052cf1b40b6b bytes=30282 -->
## FILE: examples/sysdef_example_assets/PXIe-7867R Analog, PWM, Digital Lines.fpgaconfig

- repository: `ni/niveristand-python`
- source_path: `examples/sysdef_example_assets/PXIe-7867R Analog, PWM, Digital Lines.fpgaconfig`
- sha256: `ba078441fcd7b11da6ada5185b5d384a3a0b34092400886afe76052cf1b40b6b`
- bytes: 30282

````text
<?xml version='1.0' standalone='yes' ?>
<?xml-stylesheet type="text/xsl" href='NI VeriStand FPGA DMA.xsl'?>
<FPGADMAChannelData xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation = "NI VeriStand FPGA DMA.xsd">

    <!--This is a sample XML file for specifying the content of the DMA bitstreams.  Comments describe the various elements in the file.
    Many of the elements are optional.  The comment will specify if an element is optional and any default value that will be used if the
    tag is left out. -->
	
    <Version>2.0</Version>  <!--Version of XML file.  Always 2.0. -->
	
    <Bitfile>PXIe-7867R.lvbitx</Bitfile>
        <!--Optional: Name of bitfile.  The default value is the same name as this file, but with the
        extension .lvbitx.  The bitfile must be in same directory as this file. -->

    <Categories>    <!--Beginning of defining Categories-->
        <!--Optional: Categories describes the hierarchy of the channels used in System Explorer.  If Categories is not specified
        the hierarchy will be inferred based on the Category tags on the individual channels.  Empty descriptions and default symbols will be used
        for all folders that are not found in the Categories section, but referenced by a channel. -->

        <Category>  <!--Beginning of Inputs Category-->
            <!--Category is a single level of the hierarchy.  It can specify a description and a symbol to use in the tree, as well
            as zero or more contained category -->

            <Name>Input</Name>  <!--The name as the category should be displayed in the tree.  The name must be unique with in its set of siblings. -->
            <Description>This section contains all the inputs from the FPGA Board.</Description>    <!--Optional: Description to be shown in System Explorer -->

            <Category>  <!--Analog Input Category-->
                <Name>Analog</Name>
                <Description>This section contains all the analog inputs from the FPGA Board.</Description>
                <Symbol>AI</Symbol>
            </Category>

            <Category>  <!--Digital Input Category-->
                <Name>Digital</Name>
                <Description>This section contains all the digital inputs from the FPGA Board.</Description>
                <Symbol>DI</Symbol>
            </Category>

            <Category>  <!--PWM Input Category-->
                <Name>PWM</Name>
                <Description>This section contains all the PWM inputs from the FPGA Board.</Description>
                <Symbol>PWM In</Symbol>
            </Category>

        </Category> <!--End of Inputs Category-->

        <Category>  <!--Beginning of Outputs Category-->
            <Name>Output</Name>
            <Description>This section contains all the outputs from the FPGA Board.</Description>

            <Category>  <!--Analog Output Category-->
                <Name>Analog</Name>
                <Description>This section contains all the analog outputs from the FPGA Board.</Description>
                <Symbol>AO</Symbol>
            </Category>

            <Category>  <!--Digital Output Category-->
                <Name>Digital</Name>
                <Description>This section contains all the digital outputs from the FPGA Board.</Description>
                <Symbol>DO</Symbol>
            </Category>

            <Category>  <!--PWM Output Category-->
                <Name>PWM</Name>
                <Description>This section contains all the PWM outputs from the FPGA Board.</Description>
                <Symbol>PWM Out</Symbol>
            </Category>

        </Category> <!--End of Outputs Category-->

    </Categories>   <!--End of defining Categories-->


    <DMA_Read>  <!--Specifies the content of the DMA_Read DMA channel-->
        <Packets>8</Packets>
            <!--Number of U64 packets contained in the DMA stream.  The number of Packet elements specified in XML may be less than this number.
            If the number of Packet elements is less than the number of packets, then all the packets are read but the last U64 are ignored. -->
            <!--Number of U64 packets contained in the DMA stream.  The number of Packet elements specified in XML may be less than this number.
            If the number of Packet elements is less than the number of packets, then all the packets are read but the last U64 are ignored. -->

        <Packet>   <!--Packet 1-->
            <!--An empty Packet element specifies an element that is to be ignored.  The first bit of the first read packet must contain a
            Late Status field.  If we do not wish to use this channel you can specify an empty packet.  If you want to make this status bit available 
            to the user you can specify it as a Boolean channel in the packet. -->
        	<Void>
        		<Size>1</Size>  <!-- Late Status bit -->
        	</Void>
        </Packet>
			
         <Packet> <!--Packet 2-->
            <FXPI32>
                <Name>AI0</Name>
                <Description>Analog input channel AI0 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AI1</Name>
                <Description>Analog input channel AI1 on Connector 0 of PXIe-7867R .</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
        <Packet> <!--Packet 3-->
            <FXPI32>
                <Name>AI2</Name>
                <Description>Analog input channel AI2 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AI3</Name>
                <Description>Analog input channel AI3 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
        <Packet> <!--Packet 4-->
            <FXPI32>
                <Name>AI4</Name>
                <Description>Analog input channel AI4 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AI5</Name>
                <Description>Analog input channel AI5 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AI</Symbol>
                <FXPWL>27</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!-- packet 5 -->
            <Boolean>
                <Name>Connector0/DI0</Name>
                <Description>Digital input channel DI0 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DI1</Name>
                <Description>Digital input channel DI1 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DI2</Name>
                <Description>Digital input channel DI2 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DI3</Name>
                <Description>Digital input channel DI3 on Connector 0 of PXIe-7867R.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
        </Packet>
		<Packet> <!-- packet 6 -->
            <Boolean>
                <Name>Connector1/DI0</Name>
                <Description>Digital input channel DIO0 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI1</Name>
                <Description>Digital input channel DIO1 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI2</Name>
                <Description>Digital input channel DIO2 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI3</Name>
                <Description>Digital input channel DIO3 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI4</Name>
                <Description>Digital input channel DIO4 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI5</Name>
                <Description>Digital input channel DIO5 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI6</Name>
                <Description>Digital input channel DIO6 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DI7</Name>
                <Description>Digital input channel DIO7 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI8</Name>
                <Description>Digital input channel DIO8 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI9</Name>
                <Description>Digital input channel DIO9 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI10</Name>
                <Description>Digital input channel DIO10 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI11</Name>
                <Description>Digital input channel DIO11 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI12</Name>
                <Description>Digital input channel DIO12 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI13</Name>
                <Description>Digital input channel DIO13 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI14</Name>
                <Description>Digital input channel DIO14 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DI15</Name>
                <Description>Digital input channel DIO15 on Connector 1 of PXIe-7867R. It can be used only as a DI.</Description>
                <Category>Input\Digital</Category>
                <Symbol>DI</Symbol>
            </Boolean>
        </Packet>
		<Packet>    <!--Packet 7-->
            <PWM>
                <Name>PWM In 0</Name>
                <Description>PWM input using digital line Connector0/DIO4 on the PXIe-7867R.</Description>
                <Category>Input\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM In</Symbol>
                <Parameters>
                    <U32>
                        <Name>Time Out (ms)</Name>
                        <ControlName>PulseMeas 0 Timeout</ControlName>
                        <InitialValue>10</InitialValue>
                        <Scale>107374.182375</Scale>    <!--(2^32 - 1)(U32) / 40000 ticks (1ms) = 107374-->
                    </U32>
                </Parameters>
            </PWM>
        </Packet>
        <Packet>    <!--Packet 8-->
            <PWM>
                <Name>PWM In 1</Name>
                <Description>PWM input using digital line Connector0/DIO5 on the PXIe-7867R.</Description>
                <Category>Input\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM In</Symbol>
                <Parameters>
                    <U32>
                        <Name>Time Out (ms)</Name>
                        <ControlName>PulseMeas 1 Timeout</ControlName>
                        <InitialValue>10</InitialValue>
                        <Scale>107374.182375</Scale>    <!--(2^32 - 1)(U32) / 40000 ticks (1ms) = 107374-->
                    </U32>
                </Parameters>
            </PWM>
        </Packet>
    </DMA_Read>
	
    <DMA_Write>
		<Packets>15</Packets>
		<Packet> <!--packet 1-->
            <FXPI32>
                <Name>AO0</Name>
                <Description>Analog output channel AO0 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO1</Name>
                <Description>Analog output channel AO1 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!--packet 2-->
            <FXPI32>
                <Name>AO2</Name>
                <Description>Analog output channel AO2 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO3</Name>
                <Description>Analog output channel AO3 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!--packet 3-->
            <FXPI32>
                <Name>AO4</Name>
                <Description>Analog output channel AO4 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO5</Name>
                <Description>Analog output channel AO5 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!--packet 4-->
            <FXPI32>
                <Name>AO6</Name>
                <Description>Analog output channel AO6 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO7</Name>
                <Description>Analog output channel AO7 on Connector 0 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!-- packet 5 -->
            <Boolean>
                <Name>Connector0/DO0</Name>
                <Description>Digital output channel DIO0 on Connector 0 of PXIe-7867R. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DO1</Name>
                <Description>Digital output channel DIO1 on Connector 0 of PXIe-7867R. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DO2</Name>
                <Description>Digital output channel DIO2 on Connector 0 of PXIe-7867R. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector0/DO3</Name>
                <Description>Digital output channel DIO3 on Connector 0 of PXIe-7867R. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
        </Packet>
		<Packet> <!--packet 6-->
            <FXPI32>
                <Name>AO8</Name>
                <Description>Analog output channel AO8 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO9</Name>
                <Description>Analog output channel AO9 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
        <Packet> <!--packet 7-->
            <FXPI32>
                <Name>AO10</Name>
                <Description>Analog output channel AO10 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO11</Name>
                <Description>Analog output channel AO11 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
        <Packet> <!--packet 8-->
            <FXPI32>
                <Name>AO12</Name>
                <Description>Analog output channel AO12 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO13</Name>
                <Description>Analog output channel AO13 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
        <Packet> <!--packet 9-->
            <FXPI32>
                <Name>AO14</Name>
                <Description>Analog output channel AO14 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO15</Name>
                <Description>Analog output channel AO15 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!--packet 10-->
            <FXPI32>
                <Name>AO16</Name>
                <Description>Analog output channel AO16 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
            <FXPI32>
                <Name>AO17</Name>
                <Description>Analog output channel AO17 on Connector 2 of PXIe-7867R.</Description>
                <Category>Output\Analog</Category>
                <Unit>Volts</Unit>
                <Symbol>AO</Symbol>
                <FXPWL>20</FXPWL>
                <FXPIWL>5</FXPIWL>
            </FXPI32>
        </Packet>
		<Packet> <!--packet 11-->
            <Boolean>
                <Name>Connector1/DO0</Name>
                <Description>Digital output channel DIO16 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO1</Name>
                <Description>Digital output channel DIO17 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO2</Name>
                <Description>Digital output channel DIO18 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO3</Name>
                <Description>Digital output channel DIO19 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO4</Name>
                <Description>Digital output channel DIO20 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
            <Boolean>
                <Name>Connector1/DO5</Name>
                <Description>Digital output channel DIO21 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO6</Name>
                <Description>Digital output channel DIO22 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO7</Name>
                <Description>Digital output channel DIO23 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO8</Name>
                <Description>Digital output channel DIO24 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO9</Name>
                <Description>Digital output channel DIO25 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO10</Name>
                <Description>Digital output channel DIO26 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO11</Name>
                <Description>Digital output channel DIO27 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO12</Name>
                <Description>Digital output channel DIO28 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO13</Name>
                <Description>Digital output channel DIO29 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO14</Name>
                <Description>Digital output channel DIO30 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
			<Boolean>
                <Name>Connector1/DO15</Name>
                <Description>Digital output channel DIO31 on PXIe-7867R/Connector1. It can be used only as a DO.</Description>
                <Category>Output\Digital</Category>
                <Symbol>DO</Symbol>
            </Boolean>
        </Packet>
		<Packet>    <!-- packet 12 -->
            <PWM>
                <Name>PWM Out 0</Name>
                <Description>PWM output using digital line Connector0/DIO6 on the PXIe-7867R.</Description>
                <Category>Output\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM Out</Symbol>
            </PWM>
        </Packet>
        <Packet>    <!-- packet 13-->
            <PWM>
                <Name>PWM Out 1</Name>
                <Description>PWM output using digital line Connector0/DIO7 on the PXIe-7867R.</Description>
                <Category>Output\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM Out</Symbol>
            </PWM>
        </Packet>
        <Packet>    <!-- packet 14 -->
            <PWM>
                <Name>PWM Out 2</Name>
                <Description>PWM output using digital line Connector0/DIO8 on the PXIe-7867R.</Description>
                <Category>Output\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM Out</Symbol>
            </PWM>
        </Packet>
        <Packet>    <!-- packet 15 -->
            <PWM>
                <Name>PWM Out 3</Name>
                <Description>PWM output using digital line Connector0/DIO9 on the PXIe-7867R.</Description>
                <Category>Output\PWM</Category>
                <Scale>100</Scale>
                <Unit>%</Unit>
                <Symbol>PWM Out</Symbol>
            </PWM>
        </Packet>
	</DMA_Write>
</FPGADMAChannelData>
````
