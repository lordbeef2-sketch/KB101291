# NI OSS SOURCE SNAPSHOT: niflexlogger-automation-python

<!--NI_OSS_SNAPSHOT repo=ni/niflexlogger-automation-python commit=6e28e4c786c3920651396b8790004ca6167824c8 -->

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=.flake8 sha256=11bb23261c28581c7627ff2bcdbb04de109e29f841e9b44d2868b6ed408e2d0c bytes=407 -->
## FILE: .flake8

- repository: `ni/niflexlogger-automation-python`
- source_path: `.flake8`
- sha256: `11bb23261c28581c7627ff2bcdbb04de109e29f841e9b44d2868b6ed408e2d0c`
- bytes: 407

````text
[flake8]

max-line-length = 100
# - use "black" to auto-format

exclude = src/flexlogger/automation/proto

ignore =
    # D400 and D205 are because we sometimes split the first line of the docstring
    *.py E203, W503, D100,D101,D102,D105,D106,D107, D400,D205, D415

# Config for flake8-docstrings
docstring-convention = google

# Config for flake8-import-order
import-order-style = smarkets
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=d30ec8e8bcf63d3d7378ba15a9d529c5bc206828215358643f9136b0334382b8 bytes=729 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/niflexlogger-automation-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `d30ec8e8bcf63d3d7378ba15a9d529c5bc206828215358643f9136b0334382b8`
- bytes: 729

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/flexlogger-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/flexlogger-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.

- [ ] I have run the automated tests (required if there are code changes)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=.github/workflows/publish-to-pypi.yml sha256=d0bf00909a62fafdcd69919281476e20bb3d77c2111d48484ba106aee948f6f4 bytes=822 -->
## FILE: .github/workflows/publish-to-pypi.yml

- repository: `ni/niflexlogger-automation-python`
- source_path: `.github/workflows/publish-to-pypi.yml`
- sha256: `d0bf00909a62fafdcd69919281476e20bb3d77c2111d48484ba106aee948f6f4`
- bytes: 822

````yaml
name: Publish Package to PyPI

on:
  release:
    types:
      - published

jobs:
  build-and-publish:
    if: github.repository == 'ni/niflexlogger-automation-python'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@master

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install setuptools and other tools
        run: python3 -m pip install setuptools wheel twine grpcio grpcio-tools

      - name: Build packages
        run: python3 setup.py bdist_wheel

      - name: Publish distribution to PyPI
        if: github.event.action == 'published'
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.pypi_password }}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=.gitignore sha256=218c0bb5d7b640e483b85ae017614eb74dbb58588bf693066aa966346939d317 bytes=1510 -->
## FILE: .gitignore

- repository: `ni/niflexlogger-automation-python`
- source_path: `.gitignore`
- sha256: `218c0bb5d7b640e483b85ae017614eb74dbb58588bf693066aa966346939d317`
- bytes: 1510

````text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
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
MANIFEST

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
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

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

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# PyCharm settings
.idea/

.vscode/
.vs/

# Generated protobuf files
src/flexlogger/automation/proto/*.proto
src/flexlogger/automation/proto/*.py
!src/flexlogger/automation/proto/__init__.py
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=.readthedocs.yaml sha256=76018e941c7c43e154000cf128a41597198160aff73b5bdab8d4b711503680c9 bytes=624 -->
## FILE: .readthedocs.yaml

- repository: `ni/niflexlogger-automation-python`
- source_path: `.readthedocs.yaml`
- sha256: `76018e941c7c43e154000cf128a41597198160aff73b5bdab8d4b711503680c9`
- bytes: 624

````yaml
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.10"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
   install:
   - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=CONTRIBUTING.md sha256=f3e4b2f8afab28e49e95e252b4ee3d0ce04521ea2d286d88633396099814ddcb bytes=3860 -->
## FILE: CONTRIBUTING.md

- repository: `ni/niflexlogger-automation-python`
- source_path: `CONTRIBUTING.md`
- sha256: `f3e4b2f8afab28e49e95e252b4ee3d0ce04521ea2d286d88633396099814ddcb`
- bytes: 3860

````markdown
# Contributing to *niflexlogger-automation-python* 

Contributions to *niflexlogger-automation-python* are welcome from all!

*niflexlogger-automation-python* is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/niflexlogger-automation-python/).

*niflexlogger-automation-python* follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Run the unit tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   [GitHub issues page](https://github.com/ni/niflexlogger-automation-python/issues).
3. Write new tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
4. Make your change.
5. Run all the unit tests again (which include the tests you just added),
   and confirm that they all pass.
6. Send a GitHub Pull Request to the main repository's master branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.


# Testing

Before running any tests, a supported version of Python must be installed.
Version 3.6 is preferred, as that version is the most likely to be problematic.
Installing multiple supported python versions is even better.

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
Every time you run that the package will be created and all tests will run.

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

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/niflexlogger-automation-python/blob/master/LICENSE)
for details about how *niflexlogger-automation-python* is licensed.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/api_reference.rst sha256=eb7148221c6b153dbbefb7c998f7ab2504354400d8b57c79ead74a7bc1bf6380 bytes=285 -->
## FILE: docs/api_reference.rst

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/api_reference.rst`
- sha256: `eb7148221c6b153dbbefb7c998f7ab2504354400d8b57c79ead74a7bc1bf6380`
- bytes: 285

````rst
.. _api_reference_page:

API Reference
==============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents


.. automodule:: flexlogger.automation
   :members:
   :imported-members:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/cleanup.py sha256=4ff3c490ded94d8a5c10ccb878c10e0e3fc41ba0077401052e7169100310587e bytes=2796 -->
## FILE: docs/cleanup.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/cleanup.py`
- sha256: `4ff3c490ded94d8a5c10ccb878c10e0e3fc41ba0077401052e7169100310587e`
- bytes: 2796

````python
# -*- coding: utf-8 -*-

"""Sphinx extension to clean up autodoc output."""

import inspect
import re


def _skip_member(app, what, name, obj, skip, options):
    # When ":meta private:" or ":meta public:" is explicitly included in the docstr,
    # obey it, regardless of what autodoc otherwise wants to do.
    doc = getattr(obj, "__doc__", None) or ""
    if ":meta private:" in doc:
        return True
    elif ":meta public:" in doc:
        return False

    # Don't include the docstring inherited from object.__init__ (for classes that have
    # no __init__ method).
    if obj is object.__init__:
        return True

    # Don't inherit a docstring for __init__ methods that have no docstring of their
    # own.
    if name == "__init__" and not obj.__doc__:
        return True

    # Don't include __init__ in the docs if the class is abstract.
    if name == "__init__":
        mod = inspect.getmodule(obj)
        class_name = obj.__qualname__.rsplit(".", 1)[0]
        if mod is not None:
            klass = getattr(mod, class_name)
            if inspect.isabstract(klass):
                return True


def _process_docstring(app, what, name, obj, options, lines):
    for i, line in enumerate(lines):
        # Modify the import path of public modules to appear as members of the package,
        # rather than the _module, as they're documented as being members of the
        # package. This makes intra-project links work, given the way we import classes
        # into the containing package.
        line = modify_flexlogger_paths(line)

        # Sphinx errors if it tries to reference a TypeVar variable.
        # (https://github.com/agronholm/sphinx-autodoc-typehints/issues/39)
        # So for now we'll need to handle them ourselves.
        line = line.replace("\\[\\~_Any]", "")
        line = re.sub(r"\b_Any\b", "typing.Any", line)

        # Don't abbreviate external classes (via "~"), except typing.* classes.
        line = re.sub(r"~(?!typing\.|flexlogger\.)(?=[a-z]\w*\.)", "", line)

        lines[i] = line


def modify_flexlogger_paths(s: str) -> str:
    """Modify flexlogger.* paths in the given string to hide implementation modules.

    Examples:
        >>> # Basic usage
        >>> modify_flexlogger_paths("flexlogger.foo._abc.Abc")
        'flexlogger.foo.Abc'
        >>> # Modify all paths in the string
        >>> modify_flexlogger_paths(" flexlogger.f._abc.Abc flexlogger.f._xyz.Xyz ")
        ' flexlogger.f.Abc flexlogger.f.Xyz '
    """
    return re.sub(r"\._\w+.", ".", s)


def setup(app):
    """Entry point for Sphinx extensions."""
    app.connect("autodoc-skip-member", _skip_member)
    app.connect("autodoc-process-docstring", _process_docstring)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/conf.py sha256=98afee90ed75d474e0424975b7076696e24fd6085a0e1febb762b78927e30057 bytes=2520 -->
## FILE: docs/conf.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/conf.py`
- sha256: `98afee90ed75d474e0424975b7076696e24fd6085a0e1febb762b78927e30057`
- bytes: 2520

````python
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "flexlogger"
copyright = "2020, National Instruments"
author = "National Instruments"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "docs.cleanup",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

nitpicky = True
nitpick_ignore = [
    ("py:class", "datetime.datetime"),
    ("py:class", "datetime.timedelta"),
    ("py:class", "pathlib.Path"),
    ("py:data", "typing.Any"),
    ("py:data", "typing.Iterable"),
    ("py:data", "typing.List"),
    ("py:data", "typing.Optional"),
    ("py:data", "typing.Union"),
]

autodoc_default_options = {
    "inherited-members": True,
    "special-members": "__init__",
    "no-private-members": True,
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/getting_started.rst sha256=d77d2b46010c4f5c5053dc333ce2a961ed0077e7070b89c2b1748209ac973529 bytes=8366 -->
## FILE: docs/getting_started.rst

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/getting_started.rst`
- sha256: `d77d2b46010c4f5c5053dc333ce2a961ed0077e7070b89c2b1748209ac973529`
- bytes: 8366

````rst
.. _getting_started:

Getting Started
===============

Learn the basic concepts required to automate FlexLogger tests using the Python API.


Prerequisites
-------------

Before using the FlexLogger Python API, complete the following tasks.
  * Install FlexLogger 2022 Q2 or later and create a FlexLogger project with one or more input channels.
  * Enable the Automation server preference in FlexLogger. In FlexLogger, navigate to **File>>Preferences** and check **Enable FlexLogger to receive remote automation commands** in the Automation server section of the General tab.
  * Download and install Python 3.6 or later from python.org/downloads. For more information on installing and using Python, refer to the Python documentation on `docs.python.org <https://docs.python.org/3/>`_. During installation, enable **Add Python to PATH** so you can execute Python commands more easily.
  * Install the FlexLogger Automation Python module, ``niflexlogger-automation``, using the method described below or one of the methods described in the `Readme <https://github.com/ni/niflexlogger-automation-python#readme>`_.

If you are new to Python, start by `creating and running your first script <https://niflexlogger-automation.readthedocs.io/en/latest/getting_started.html#create-run-script>`_. If you an experienced Python user, refer to the `examples <https://niflexlogger-automation.readthedocs.io/en/latest/getting_started.html#code-examples>`_ and `API reference <https://niflexlogger-automation.readthedocs.io/en/latest/api_reference.html>`_.


Installing the FlexLogger Automation Python module
--------------------------------------------------
Install the FlexLogger Automation Python module so you can control FlexLogger tests programatically.

1. Open the command prompt.
2. Execute the following command to install the module.

   ``pip install niflexlogger-automation``


Installing the FlexLogger Automation Python module in Visual Studio Code
------------------------------------------------------------------------
1. Open Visual Studio Code and select Terminal>>New Terminal.
2. Execute the following command in the terminal to install the module.

   ``pip install niflexlogger-automation``

If you have multiple Python versions installed in your computer, you can specify to which version you will install the module by using:

   ``py -<version> -m pip install niflexlogger-automation``


Installing the FlexLogger Automation Python module in PyCharm
------------------------------------------------------------------------
1. Open PyCharm and create or browse to a project. 
2. Go to View>>Tool Windows>>Terminal
3. Install the package with the following command:

Note: In PyCharm, when you create a new project with a virtual environment (venv), the virtual environment is automatically activated in the terminal associated with the project.  In a virtual environment, the installed packages are isolated from the global Python environment and apply only to the virtual environment being used.

   ``pip install niflexlogger-automation``

.. _create_run_script:


Creating and running your first script
--------------------------------------
Use the Start and Stop a Test example code to automate a FlexLogger test. The steps below describe how to perform this task with a text editor and the command prompt. You can also use your favorite integrated development environment (IDE). 

1. Close FlexLogger if it is running.
2. Open a text editor.
3. Copy and paste the code provided below.

.. literalinclude:: ../examples/Basic/launch_application.py
   :language: python
   :linenos:

4. Save the file with a ``.py`` extension. For example, ``my_script.py``. Enclose file paths in quotation marks if you have spaces in your folder or file names.

5. Open the command prompt as an administrator.
6. Change the directory to the location where you saved your script. For example,

   ``cd C:\Users\Desktop``
7. Run the script with the ``python`` command. The Start and Stop a Test example requires that you provide the path to the project you want to control as an input. Use quotation marks when specifying the path. For example,

   ``python my_script.py "C:\Users\Desktop\my_FlexLogger_Project.flxproj"``

   The Python script launches FlexLogger, opens the project you specified, and starts running a test. The command prompt displays a status message and provides you with the option to stop the test and close the project.

.. _code_examples:

Examples
========

Communicating with FlexLogger
-----------------------------

Launch FlexLogger and open a project

.. literalinclude:: ../examples/Basic/launch_application.py
   :language: python
   :linenos:

Connect to FlexLogger when it is already running

.. literalinclude:: ../examples/Basic/connect_to_application.py
   :language: python
   :linenos:

Test session
------------

Start and stop a test

.. literalinclude:: ../examples/Basic/start_and_stop_test_session.py
   :language: python
   :linenos:

Adding a note to a log file

.. literalinclude:: ../examples/Basic/add_note.py
   :language: python
   :linenos:

Channels
--------

Getting the value of a channel

.. literalinclude:: ../examples/Basic/get_channel_value.py
   :language: python
   :linenos:

Setting the value of a channel

.. literalinclude:: ../examples/Basic/set_channel_value.py
   :language: python
   :linenos:

Logging
-------

Getting the log file base path and name

.. literalinclude:: ../examples/Basic/get_log_file_path_and_name.py
   :language: python
   :linenos:

Setting the log file base path and name

.. literalinclude:: ../examples/Basic/set_log_file_path_and_name.py
   :language: python
   :linenos:

Getting a test property

.. literalinclude:: ../examples/Basic/get_test_property.py
   :language: python
   :linenos:

Setting a test property

.. literalinclude:: ../examples/Basic/set_test_property.py
   :language: python
   :linenos:

Troubleshooting
===============

Can't connect to running FlexLogger
-----------------------------------
If you get an error connecting to an already running instance of FlexLogger, the Automation
server preference may not be enabled. You can enable this preference by opening the
"File>>Preferences" menu item, and then enabling the "Automation server"
preference in the "General" tab.

.. image:: preference_automation_server.png

Exception on first call into FlexLogger
---------------------------------------
If you see an exception on the first call into FlexLogger similar to::

  grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.UNAVAILABLE
        details = "failed to connect to all addresses"
        debug_error_string = "{"created":"@1608052709.612000000","description":"Failed to pick subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":4143,"referenced_errors":[{"created":"@1608052633.077000000","description":"failed to connect to all addresses","file":"src/core/ext/filters/client_channel/lb_policy/pick_first/pick_first.cc","file_line":398,"grpc_status":14}]}"

the problem may be an HTTP proxy.  To test this, in your Python script add the following lines
before your FlexLogger API calls:

.. code-block:: python

   if os.environ.get('https_proxy'):
      del os.environ['https_proxy']
   if os.environ.get('http_proxy'):
      del os.environ['http_proxy']

If this fixes the problem, try configuring your proxy to not affect traffic to localhost.
See `this GitHub issue <https://github.com/ni/niflexlogger-automation-python/issues/13>`_
for an example.

Getting Python Command Redirects
---------------------------------------
If you encounter issues where typing Python commands leads you to the Microsoft Store, you may need to turn off Execution Aliases in Windows. Go to Settings>>Apps>>Apps & features>>App execution aliases and turn off the aliases for Python.


File path errors
---------------------------------------
Ensure you know the exact path to your FlexLogger project and script. Incorrect paths can lead to errors when running examples. This can be particularly important when following the provided documentation examples.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/index.rst sha256=e6271495f583215c7730ce455716e7bf855bd1784bf105c1c1d98e1a2b2dd5cc bytes=237 -->
## FILE: docs/index.rst

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/index.rst`
- sha256: `e6271495f583215c7730ce455716e7bf855bd1784bf105c1c1d98e1a2b2dd5cc`
- bytes: 237

````rst
Welcome to flexlogger's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   api_reference


Package info
************

.. include:: ../README.rst
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=docs/requirements.txt sha256=16de6a8b1b5843cd9f2c224accf188f18501003fb709730ed30a12288a7665e8 bytes=74 -->
## FILE: docs/requirements.txt

- repository: `ni/niflexlogger-automation-python`
- source_path: `docs/requirements.txt`
- sha256: `16de6a8b1b5843cd9f2c224accf188f18501003fb709730ed30a12288a7665e8`
- bytes: 74

````text
sphinx >= 2.1
sphinx-autodoc-typehints
sphinx-rtd-theme >= 1.0.0rc1
.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/add_note.py sha256=b06f84981c13a3d8ef188c1457e32e782536bd64b82989a2f732c5aa3f9458d7 bytes=873 -->
## FILE: examples/Basic/add_note.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/add_note.py`
- sha256: `b06f84981c13a3d8ef188c1457e32e782536bd64b82989a2f732c5aa3f9458d7`
- bytes: 873

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, start the test session and add a note."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        test_session = project.test_session
        test_session.start()
        note = input("Test started. Enter a note to log: ")
        test_session.add_note(note)
        print("Note added. Press Enter to stop the test and close the project...")
        input()

        test_session.stop()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/connect_to_application.py sha256=76e8ba05e00cb4de86178019d5cf11f56df57177505463ba9076586530a87989 bytes=914 -->
## FILE: examples/Basic/connect_to_application.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/connect_to_application.py`
- sha256: `76e8ba05e00cb4de86178019d5cf11f56df57177505463ba9076586530a87989`
- bytes: 914

````python
import sys

from flexlogger.automation import Application


def main():
    """Connect to an already running instance of FlexLogger with an open project

    Note that before connecting to an already running instance of FlexLogger,
    the Automation server preference must be enabled. You can enable this preference by opening the
    "File>>Preferences" menu item, and then enabling the "Automation server" preference in the
    "General" tab.
    """
    app = Application()
    project = app.get_active_project()
    if project is None:
        print("No project is open in FlexLogger!")
        return 1
    test_session_state = project.test_session.state
    print("The test session state is:")
    print(test_session_state)
    print("Press Enter to disconnect from FlexLogger...")
    input()
    app.disconnect()
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/disable_channel.py sha256=e287a7edfdf8cd1a02cc597c4eca8b141b4623001eb5d5a14ea36dbbb9060a47 bytes=869 -->
## FILE: examples/Basic/disable_channel.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/disable_channel.py`
- sha256: `e287a7edfdf8cd1a02cc597c4eca8b141b4623001eb5d5a14ea36dbbb9060a47`
- bytes: 869

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and disables a channel."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        channel_name = input("Enter the name of the channel to disable: ")
        channel_specification = project.open_channel_specification_document()
        channel_specification.set_channel_enabled(channel_name, False)
        print("Channel disabled. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/disable_channel_logging.py sha256=a5f5e7732ca71343cb50b360e9ba12bdc856eeb0ff294150efa1e46547c8a46b bytes=893 -->
## FILE: examples/Basic/disable_channel_logging.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/disable_channel_logging.py`
- sha256: `a5f5e7732ca71343cb50b360e9ba12bdc856eeb0ff294150efa1e46547c8a46b`
- bytes: 893

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and disables a channel."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        channel_name = input("Enter the name of the channel to disable logging: ")
        channel_specification = project.open_channel_specification_document()
        channel_specification.set_channel_logging_enabled(channel_name, False)
        print("Channel logging disabled. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/events.py sha256=ccb6843c666c4f817a03a8120adc7d8c5a2d8672782e09117a07a3f7043412f2 bytes=3688 -->
## FILE: examples/Basic/events.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/events.py`
- sha256: `ccb6843c666c4f817a03a8120adc7d8c5a2d8672782e09117a07a3f7043412f2`
- bytes: 3688

````python
from flexlogger.automation import AlarmPayload
from flexlogger.automation import Application
from flexlogger.automation import EventPayload
from flexlogger.automation import EventType
from flexlogger.automation import FilePayload
import os
import sys


def main(project_path):
    """Launch FlexLogger, open a project, and wait for an event."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)

        # Get a reference to the event handler and register callback functions for different event types.
        event_handler = app.event_handler
        event_handler.register_event_callback(alarms_event_handler, [EventType.ALARM])
        event_handler.register_event_callback(log_file_event_handler, [EventType.LOG_FILE])
        event_handler.register_event_callback(session_event_handler, [EventType.TEST_SESSION])

        test_session = project.test_session
        test_session.start()
        print("Test started. Press Enter to stop the test and close the project...")

        # Wait for the user to press enter
        input()

        # Cleanup: stop the session, close the project and unregister from the events
        test_session.stop()
        project.close()
        event_handler.unregister_from_events()

    return 0


def alarms_event_handler(application: Application, event_type: EventType, payload: AlarmPayload):
    """Alarm Event Handler
    This method will be called when an alarm event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: AlarmPayload       The event payload
    """

    print("Event of type: {}, received at {}".format(event_type, payload.timestamp))
    print("Event Name: {}".format(payload.event_name))
    print("Alarm occurred on channel: {}".format(payload.channel))
    print("Alarm Severity Level: {}".format(payload.severity_level))

    # Stop the session when the alarm is received
    project = application.get_active_project()
    session = project.test_session
    session.stop()


def log_file_event_handler(application: Application, event_type: EventType, payload: FilePayload):
    """FlexLogger Event Handler
    This method will be called when a file event is fired.

        Args:
            application: Application    Reference to the application, so that you can access the project, session, etc
            event_type: EventType       The event type
            payload: FilePayload        The event payload
    """

    print("Event of type: {}, received at {}".format(event_type, payload.timestamp))
    print("Event Name: {}".format(payload.event_name))
    print("TDMS file path: {}".format(payload.file_path))


def session_event_handler(application: Application, event_type: EventType, payload: EventPayload):
    """FlexLogger Event Handler
    This method will be called when a session event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: EventPayload       The event payload
    """

    print("Event of type: {}, received at {}".format(event_type, payload.timestamp))
    print("Event Name: {}".format(payload.event_name))


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_channel_value.py sha256=94f6b5164ff1ec779c2a8ebb9e9efff19d89b85a95034d974511cfa6dfbf360d bytes=938 -->
## FILE: examples/Basic/get_channel_value.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_channel_value.py`
- sha256: `94f6b5164ff1ec779c2a8ebb9e9efff19d89b85a95034d974511cfa6dfbf360d`
- bytes: 938

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and get the value of a channel."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        channel_name = input("Enter the name of the channel to get the value of: ")
        channel_specification = project.open_channel_specification_document()
        channel_value = channel_specification.get_channel_value(channel_name)
        print("Channel value:")
        print(channel_value)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_log_file_description.py sha256=b03ddcfdb523a34460f9b28c177bbaa2bc6264ed49c8a51ec0f96d61fe8bf02d bytes=858 -->
## FILE: examples/Basic/get_log_file_description.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_log_file_description.py`
- sha256: `b03ddcfdb523a34460f9b28c177bbaa2bc6264ed49c8a51ec0f96d61fe8bf02d`
- bytes: 858

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and get the log file description."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()
        log_file_description = logging_specification.get_log_file_description()
        print("Log file description: " + log_file_description)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_log_file_path_and_name.py sha256=645e286f6961c740d8bee52cb202c9de59e63014cca777cd2c8147cd63d2895d bytes=975 -->
## FILE: examples/Basic/get_log_file_path_and_name.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_log_file_path_and_name.py`
- sha256: `645e286f6961c740d8bee52cb202c9de59e63014cca777cd2c8147cd63d2895d`
- bytes: 975

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and gets the log file base path and name."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()
        log_file_base_path = logging_specification.get_log_file_base_path()
        log_file_name = logging_specification.get_log_file_name()
        print("Log file base path: " + log_file_base_path)
        print("Log file name: " + log_file_name)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_project_file_path.py sha256=967ab6515837746fea9bd0e16a003a4a5e8032d98380af34de1105ff190c837a bytes=767 -->
## FILE: examples/Basic/get_project_file_path.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_project_file_path.py`
- sha256: `967ab6515837746fea9bd0e16a003a4a5e8032d98380af34de1105ff190c837a`
- bytes: 767

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and get the loaded project's file path."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        print("Project file path: " + str(project.project_file_path))
        print("Project name: " + project.project_name)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_test_properties.py sha256=1a8967424e1ddc7cf0c07a7895763e677e56841491ab29a984515367be09441e bytes=985 -->
## FILE: examples/Basic/get_test_properties.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_test_properties.py`
- sha256: `1a8967424e1ddc7cf0c07a7895763e677e56841491ab29a984515367be09441e`
- bytes: 985

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and get all test properties."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()
        test_properties = logging_specification.get_test_properties()
        for test_property in test_properties:
            prompt = "(prompt on start)" if test_property.prompt_on_start else ""
            print(f'{test_property.name}: {test_property.value} {prompt}')
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_test_property.py sha256=4bde81b07ba29012f9f908d7be20a9995d24aeabc062582d4d4a104d10c868b7 bytes=963 -->
## FILE: examples/Basic/get_test_property.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_test_property.py`
- sha256: `4bde81b07ba29012f9f908d7be20a9995d24aeabc062582d4d4a104d10c868b7`
- bytes: 963

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and gets the value of a test property."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        test_property_name = input("Enter the name of the test property to get the value of: ")
        logging_specification = project.open_logging_specification_document()
        test_property = logging_specification.get_test_property(test_property_name)
        print("Test property:")
        print(test_property)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/get_trigger_settings.py sha256=2fb1ea981cfc5a77b4115b9d3c0d8f6b1d2047084ec00785e4940b2ae6d46d23 bytes=1955 -->
## FILE: examples/Basic/get_trigger_settings.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/get_trigger_settings.py`
- sha256: `2fb1ea981cfc5a77b4115b9d3c0d8f6b1d2047084ec00785e4940b2ae6d46d23`
- bytes: 1955

````python
import os
import sys

from flexlogger.automation import Application
from flexlogger.automation import StartTriggerCondition
from flexlogger.automation import StopTriggerCondition


def main(project_path):
    """Launch FlexLogger, open a project, and get the trigger settings."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()

        # Get and print the start trigger settings
        start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
        print("Start Trigger Condition: " + str(start_trigger_condition))
        if start_trigger_condition == StartTriggerCondition.CHANNEL_VALUE_CHANGE:
            print("Channel Value Change Condition :")
            print(start_trigger_settings)
        elif start_trigger_condition == StartTriggerCondition.ABSOLUTE_TIME:
            print("Start Time: " + start_trigger_settings.strftime("%x, %X"))

        # Get and print the stop trigger settings
        stop_trigger_condition, stop_trigger_settings = logging_specification.get_stop_trigger_settings()
        print("Stop Trigger Condition: " + str(stop_trigger_condition))
        if stop_trigger_condition == StopTriggerCondition.CHANNEL_VALUE_CHANGE:
            print("Channel Value Change Condition :")
            print(stop_trigger_settings)
        elif stop_trigger_condition == StopTriggerCondition.TEST_TIME_ELAPSED:
            print("Time Elapsed: " + stop_trigger_settings)

        print("Press Enter to close the project...")
        input()
        project.close()

    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/launch_application.py sha256=31cf771479970f366e20f473edd39f113bcc3deeda1e3a786a9cc63f280b9ef8 bytes=906 -->
## FILE: examples/Basic/launch_application.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/launch_application.py`
- sha256: `31cf771479970f366e20f473edd39f113bcc3deeda1e3a786a9cc63f280b9ef8`
- bytes: 906

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger and open a project."""
    # Note that using the "with" statement here means that when the block
    # goes out of scope, the application will be closed.  To prevent this,
    # call app.disconnect() before the scope ends.
    with Application.launch() as app:
        versions = app.get_version()
        print("FlexLogger version: " + versions[1])
        project = app.open_project(path=project_path, timeout=180)
        print("Press Enter to close project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/pause_and_resume_test_session.py sha256=cbe69cc5b0d4f874762b940ade8317c4fc2d152b49bbd5732ba4a0d1adc029ac bytes=998 -->
## FILE: examples/Basic/pause_and_resume_test_session.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/pause_and_resume_test_session.py`
- sha256: `cbe69cc5b0d4f874762b940ade8317c4fc2d152b49bbd5732ba4a0d1adc029ac`
- bytes: 998

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, pauses and resumes the test session."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        test_session = project.test_session
        test_session.start()
        print("Test started. Press Enter to pause the test...")
        input()
        test_session.pause()
        print("Test paused. Press Enter to resume the test...")
        input()
        test_session.resume()
        print("Test resumed. Press Enter to stop the test and close the project...")
        input()
        test_session.stop()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/run_test_session_and_show_log_file.py sha256=a36681610c0b0ec6f713063ef84845a4cb145302b5d67f89c54c336bc287e5c7 bytes=1159 -->
## FILE: examples/Basic/run_test_session_and_show_log_file.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/run_test_session_and_show_log_file.py`
- sha256: `a36681610c0b0ec6f713063ef84845a4cb145302b5d67f89c54c336bc287e5c7`
- bytes: 1159

````python
import os
import sys

from flexlogger.automation import Application, LogFileType


def main(project_path):
    """Launch FlexLogger, open a project, run a test session, and show log file."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()
        logging_specification.remove_log_files(delete_files=True)
        test_session = project.test_session
        test_session.start()
        print("Test started. Press Enter to stop the test and close the project...")
        input()
        test_session.stop()
        log_files = logging_specification.get_log_files(LogFileType.TDMS)
        project.close()
        print("The following TDMS log files were created during the test session:")
        for log_file in log_files:
            print(log_file)
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_channel_value.py sha256=820c3c7e0f187b5776fff621cf970424a1e359e417a493573d5a004428bc029c bytes=965 -->
## FILE: examples/Basic/set_channel_value.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_channel_value.py`
- sha256: `820c3c7e0f187b5776fff621cf970424a1e359e417a493573d5a004428bc029c`
- bytes: 965

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and sets the value of a channel."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        channel_name = input("Enter the name of the channel to set the value of: ")
        channel_value = input("Enter the new channel value: ")
        channel_specification = project.open_channel_specification_document()
        channel_specification.set_channel_value(channel_name, float(channel_value))
        print("Channel value set. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_data_rate.py sha256=d4f5bf4eaf0b49a6d24976cc7d19b267455d5959395267d2befc2673d4b46194 bytes=1788 -->
## FILE: examples/Basic/set_data_rate.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_data_rate.py`
- sha256: `d4f5bf4eaf0b49a6d24976cc7d19b267455d5959395267d2befc2673d4b46194`
- bytes: 1788

````python
import os
import sys

from flexlogger.automation import Application
from flexlogger.automation import DataRateLevel


DATA_RATE_LEVEL_LOOKUP = {
    "Slow": DataRateLevel.SLOW,
    "Medium": DataRateLevel.MEDIUM,
    "Fast": DataRateLevel.FAST
}


def main(project_path):
    """Launch FlexLogger, open a project, and set the data rate values."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        channel_specification = project.open_channel_specification_document()
        slow_date_rate = input("Specify the data rate value for the Slow level in Hertz: ")
        channel_specification.set_data_rate(DataRateLevel.SLOW, float(slow_date_rate))
        medium_date_rate = input("Specify the data rate value for the Medium level in Hertz: ")
        channel_specification.set_data_rate(DataRateLevel.MEDIUM, float(medium_date_rate))
        fast_date_rate = input("Specify the data rate value for the Fast level in Hertz: ")
        channel_specification.set_data_rate(DataRateLevel.FAST, float(fast_date_rate))
        channel_name = input("Enter the name of the channel you want to set the data rate level of: ")
        data_rate_level = input("Enter the data rate level you want to set (Slow, Medium or Fast: ")
        channel_specification.set_data_rate_level(channel_name, DATA_RATE_LEVEL_LOOKUP.get(data_rate_level))

        print("Data rate set. Press Enter to save and close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_log_file_description.py sha256=7eacd6482cd1323e931a4933d858a7351d52d406d2e697adf35000550b5b0823 bytes=891 -->
## FILE: examples/Basic/set_log_file_description.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_log_file_description.py`
- sha256: `7eacd6482cd1323e931a4933d858a7351d52d406d2e697adf35000550b5b0823`
- bytes: 891

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and set the log file description."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        log_file_description = input("Enter the log file description: ")
        logging_specification = project.open_logging_specification_document()
        logging_specification.set_log_file_description(log_file_description)
        print("Log file description set. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_log_file_path_and_name.py sha256=80f7abc0b00d49a9824a73c6a0e8872ac6d7bb8d9de21e362ce3a254d02a1422 bytes=1022 -->
## FILE: examples/Basic/set_log_file_path_and_name.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_log_file_path_and_name.py`
- sha256: `80f7abc0b00d49a9824a73c6a0e8872ac6d7bb8d9de21e362ce3a254d02a1422`
- bytes: 1022

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and sets the log file base path and name."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        log_file_base_path = input("Enter the log file base path: ")
        log_file_name = input("Enter the log file name: ")
        logging_specification = project.open_logging_specification_document()
        logging_specification.set_log_file_base_path(log_file_base_path)
        logging_specification.set_log_file_name(log_file_name)
        print("Log file base path and name set. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_test_properties.py sha256=24661d74e1f4f784e09eda9e9035b53eab2d0db8a7d70b4b70fb695f4155409d bytes=1268 -->
## FILE: examples/Basic/set_test_properties.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_test_properties.py`
- sha256: `24661d74e1f4f784e09eda9e9035b53eab2d0db8a7d70b4b70fb695f4155409d`
- bytes: 1268

````python
import os
import sys

from flexlogger.automation import Application
from flexlogger.automation import TestProperty


def main(project_path):
    """Launch FlexLogger, open a project, and set test properties."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()

        test_properties = []
        while True:
            name = input("Enter the name of the test property to set the value of (empty line to exit): ")
            if name == "":
                break
            value = input("Enter the test property value: ")
            prompt_on_start = input("Enter if you want to prompt on start (y/n): ") == "y"
            test_properties.append(TestProperty(name, value, prompt_on_start))

        logging_specification.set_test_properties(test_properties)
        print("Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_test_property.py sha256=e334418b9e256a17f2a9250e905c716e9286ee35e5ebcf0ecb596273156aa1e5 bytes=996 -->
## FILE: examples/Basic/set_test_property.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_test_property.py`
- sha256: `e334418b9e256a17f2a9250e905c716e9286ee35e5ebcf0ecb596273156aa1e5`
- bytes: 996

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and sets the value of a test property."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        test_property_name = input("Enter the name of the test property to set the value of: ")
        test_property_value = input("Enter the test property value: ")
        logging_specification = project.open_logging_specification_document()
        logging_specification.set_test_property(test_property_name, test_property_value)
        print("Test property set. Press Enter to close the project...")
        input()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_time_trigger_settings.py sha256=63fb5a0da17cd1bac9f845e9d53ac5a7e8d31bf0780f3c6c4bd7aaaa27121473 bytes=1208 -->
## FILE: examples/Basic/set_time_trigger_settings.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_time_trigger_settings.py`
- sha256: `63fb5a0da17cd1bac9f845e9d53ac5a7e8d31bf0780f3c6c4bd7aaaa27121473`
- bytes: 1208

````python
import os
import sys

from datetime import datetime
from datetime import timedelta
from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, and set the trigger settings."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()

        # Set the start trigger settings.
        # test_start_time is treated as UTC unless a timezone is explicitly specified
        test_start_time = datetime.utcnow()
        logging_specification.set_start_trigger_settings_to_absolute_time(test_start_time)
        # Set the stop trigger settings
        duration = timedelta(seconds=100)
        logging_specification.set_stop_trigger_settings_to_duration(duration)

        print("Press Enter to close the project...")
        input()
        project.close()

    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/set_value_change_trigger_settings.py sha256=1077e97ba69f85e92c98a40728bb55892000d923e43651edb9772c3f78ec2dfb bytes=1808 -->
## FILE: examples/Basic/set_value_change_trigger_settings.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/set_value_change_trigger_settings.py`
- sha256: `1077e97ba69f85e92c98a40728bb55892000d923e43651edb9772c3f78ec2dfb`
- bytes: 1808

````python
import os
import sys

from flexlogger.automation import Application
from flexlogger.automation import ValueChangeCondition
from flexlogger.automation import ValueChangeType


def main(project_path):
    """Launch FlexLogger, open a project, and set the trigger settings."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        logging_specification = project.open_logging_specification_document()

        start_value_change_condition = ValueChangeCondition()
        start_value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
        start_value_change_condition.channel_name = 'Replace this string with the channel name to monitor.'
        start_value_change_condition.min_value = 1.0
        start_value_change_condition.max_value = 2.0
        start_value_change_condition.time = 0.0

        stop_value_change_condition = ValueChangeCondition()
        stop_value_change_condition.value_change_type = ValueChangeType.FALL_BELOW_VALUE
        stop_value_change_condition.channel_name = 'Replace this string with the channel name to monitor.'
        stop_value_change_condition.threshold = 1.0
        stop_value_change_condition.time = 0.0

        logging_specification.set_start_trigger_settings_to_value_change(start_value_change_condition)
        logging_specification.set_stop_trigger_settings_to_value_change(stop_value_change_condition)

        print("Press Enter to close the project...")
        input()
        project.close()

    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Basic/start_and_stop_test_session.py sha256=be9a09e45a0ffb465e1eb49ee3f0b2e30b5909a2c0587c2562bf24032973fd6a bytes=769 -->
## FILE: examples/Basic/start_and_stop_test_session.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Basic/start_and_stop_test_session.py`
- sha256: `be9a09e45a0ffb465e1eb49ee3f0b2e30b5909a2c0587c2562bf24032973fd6a`
- bytes: 769

````python
import os
import sys

from flexlogger.automation import Application


def main(project_path):
    """Launch FlexLogger, open a project, start and stop the test session."""
    with Application.launch() as app:
        project = app.open_project(path=project_path)
        test_session = project.test_session
        test_session.start()
        print("Test started. Press Enter to stop the test and close the project...")
        input()
        test_session.stop()
        project.close()
    return 0


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Interactive/configure_logging_specification.py sha256=afbe00015599c1d848d9962966138b7e1b706b5b05aba83386f5ad9b65c7da3e bytes=8621 -->
## FILE: examples/Interactive/configure_logging_specification.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Interactive/configure_logging_specification.py`
- sha256: `afbe00015599c1d848d9962966138b7e1b706b5b05aba83386f5ad9b65c7da3e`
- bytes: 8621

````python
import os
import sys

from consolemenu import ConsoleMenu, Screen
from consolemenu.items import FunctionItem
from flexlogger.automation import (
    Application,
    FlexLoggerError,
    TestSessionState,
)
from prettytable import PrettyTable


def main(project_path):
    """Interactively configure the FlexLogger logging specification.

    Launch FlexLogger, open the specified project and interactively
    configuring the FlexLogger logging specification.
    """
    print("Launching FlexLogger . . .")
    with Application.launch() as app:
        print("Loading FlexLogger project . . .")
        project = app.open_project(path=project_path)
        test_session = project.test_session
        logging_specification_document = project.open_logging_specification_document()

        _show_interactive_menu(test_session, logging_specification_document)

        print("Closing FlexLogger project . . .")
        project.close()
    return 0


def _show_log_file_path(logging_specification_document):
    log_file_base_path = logging_specification_document.get_log_file_base_path()
    print("The log file base path is: " + log_file_base_path)
    if "{" in log_file_base_path:
        resolved_log_file_base_path = (
            logging_specification_document.get_resolved_log_file_base_path()
        )
        print("The resolved log file base path is: " + resolved_log_file_base_path)
    log_file_name = logging_specification_document.get_log_file_name()
    print("The log file name is: " + log_file_name)
    if "{" in log_file_name:
        resolved_log_file_name = logging_specification_document.get_resolved_log_file_name()
        print("The resolved log file file name is: " + resolved_log_file_name)
    Screen().input("Press [Enter] to continue")


def _set_log_file_path(logging_specification_document):
    log_file_base_path = Screen().input("Input the log file base path and press [Enter]: ")
    log_file_name = Screen().input("Input the log file name and [Enter]: ")
    logging_specification_document.set_log_file_base_path(log_file_base_path)
    logging_specification_document.set_log_file_name(log_file_name)
    Screen().input("Log file path updated. Press [Enter] to continue")


def _show_test_properties(logging_specification_document):
    test_properties = logging_specification_document.get_test_properties()
    table = PrettyTable(["Name", "Value", "Prompt on start"])
    for test_property in test_properties:
        table.add_row([test_property.name, test_property.value, test_property.prompt_on_start])
    print(table)
    Screen().input("Press [Enter] to continue")


def _show_test_property(logging_specification_document):
    test_property_name = Screen().input(
        "Input the name of the test property to show and press [Enter]: "
    )
    try:
        test_property = logging_specification_document.get_test_property(test_property_name)
        print("The test property name is: " + test_property.name)
        print("The test property value is: " + test_property.value)
        if test_property.prompt_on_start:
            print("The user will be prompted to set the value of this property on test start.")
        else:
            print("The user will not be prompted to set the value of this property on test start.")
        Screen().input("Press [Enter] to continue")
    except FlexLoggerError:
        Screen().input(
            'Test property could not be retrieved, possibly because no test property is named "'
            + test_property_name
            + '". Press [Enter] to continue'
        )


def _set_test_property(logging_specification_document):
    property_name = Screen().input(
        "Input the name of the test property to create or modify and press [Enter]: "
    )
    property_value = Screen().input("Input the value for the test property and press [Enter]: ")
    prompt_on_start_input = (
        Screen()
        .input(
            "Input if the user should be prompted to set the value of this "
            "property on test start (y|n) and press [Enter]: "
        )
        .lower()
        .strip()
    )
    if prompt_on_start_input[0] == "y":
        prompt_on_start = True
    else:
        prompt_on_start = False
    logging_specification_document.set_test_property(property_name, property_value, prompt_on_start)
    Screen().input("Test property set. Press [Enter] to continue")


def _remove_test_property(logging_specification_document):
    test_property_name = Screen().input(
        "Input the name of the test property to remove and press [Enter]: "
    )
    try:
        logging_specification_document.remove_test_property(test_property_name)
        Screen().input("Test property removed. Press [Enter] to continue")
    except FlexLoggerError:
        Screen().input(
            'Test property could not be removed, possibly because no test property is named "'
            + test_property_name
            + '". Press [Enter] to continue'
        )


def _show_interactive_menu(test_session, logging_specification_document):
    """Display an interactive menu for configuring the logging specification.

    Some configuration options are not available if the test session is running.

    This will return when the user invokes one of the exit menu items.
    """
    # A menu item for all menus, so that test_session.state is checked again
    refresh_test_session_state = FunctionItem(
        "Refresh test session state", _no_op, should_exit=True
    )

    def _create_menu(desc, epilogue_text, menu_items):
        console_menu = ConsoleMenu(
            "Logging Specification Document API Demo", desc, epilogue_text=epilogue_text
        )
        console_menu.append_item(refresh_test_session_state)
        for name, fn, args, opts in menu_items:
            menu_item = FunctionItem(name, fn, args, **opts)
            console_menu.append_item(menu_item)
        return console_menu

    edits_allowed_menu = _create_menu(
        "The test session is currently idle.",
        "",
        [
            ("Show the log file path", _show_log_file_path, [logging_specification_document], {}),
            ("Set the log file path", _set_log_file_path, [logging_specification_document], {}),
            (
                "Show all test properties",
                _show_test_properties,
                [logging_specification_document],
                {},
            ),
            ("Show a test property", _show_test_property, [logging_specification_document], {}),
            ("Set a test property", _set_test_property, [logging_specification_document], {}),
            (
                "Remove a test property",
                _remove_test_property,
                [logging_specification_document],
                {},
            ),
        ],
    )
    edits_not_allowed_menu = _create_menu(
        "The test session is currently running.",
        "",
        [
            ("Show the log file path", _show_log_file_path, [logging_specification_document], {}),
            (
                "Show all test properties",
                _show_test_properties,
                [logging_specification_document],
                {},
            ),
            ("Show a test property", _show_test_property, [logging_specification_document], {}),
        ],
    )

    while True:
        # Edits to the logging specification are not allowed while the test is running
        state = test_session.state
        if state == TestSessionState.RUNNING:
            active_menu = edits_not_allowed_menu
        elif state == TestSessionState.IDLE:
            edits_allowed_menu.subtitle = "The test session is currently idle."
            active_menu = edits_allowed_menu
        elif state == TestSessionState.NO_VALID_LOGGED_CHANNELS:
            edits_allowed_menu.subtitle = "The project has no channels to log."
            active_menu = edits_allowed_menu
        else:
            edits_allowed_menu.subtitle = "The project has one or more errors."
            active_menu = edits_allowed_menu
        active_menu.show()
        if active_menu.selected_item == active_menu.exit_item:
            break


def _no_op():
    return


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Interactive/getting_and_setting_channel_values.py sha256=30b33041093fc8a2bfc48b344d922f9140dab3aeafd83119952d204eab80747a bytes=4123 -->
## FILE: examples/Interactive/getting_and_setting_channel_values.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Interactive/getting_and_setting_channel_values.py`
- sha256: `30b33041093fc8a2bfc48b344d922f9140dab3aeafd83119952d204eab80747a`
- bytes: 4123

````python
import os
import sys

from consolemenu import ConsoleMenu, Screen
from consolemenu.items import FunctionItem
from flexlogger.automation import (
    Application,
    FlexLoggerError,
)
from prettytable import PrettyTable


def main(project_path):
    """Interactively get and set FlexLogger channel values.

    Launch FlexLogger, open the specified project and interactively
    get and set FlexLogger channel values.
    """
    print("Launching FlexLogger . . .")
    with Application.launch() as app:
        print("Loading FlexLogger project . . .")
        project = app.open_project(path=project_path)
        channel_specification_document = project.open_channel_specification_document()

        _show_interactive_menu(channel_specification_document)

        print("Closing FlexLogger project . . .")
        project.close()
    return 0


def _show_channel_values(channel_specification_document):
    channel_names = channel_specification_document.get_channel_names()
    table = PrettyTable(["Channel name", "Value", "Timestamp"])
    for channel_name in channel_names:
        try:
            channel_data_point = channel_specification_document.get_channel_value(channel_name)
            table.add_row(
                [
                    channel_data_point.name,
                    channel_data_point.value,
                    # Convert the timestamp from UTC to local time
                    channel_data_point.timestamp.astimezone(None),
                ]
            )
        except FlexLoggerError:
            # Getting a channel that is not available, configured or enabled will raise
            # an exception. Ignore those exceptions and continue to the next channel.
            pass
    print(table)
    Screen().input("Press [Enter] to continue")


def _set_channel_value(channel_specification_document):
    channel_name = Screen().input("Input the name of the channel to set and press [Enter]: ")
    channel_value = Screen().input("Input the value for the channel and press [Enter]: ")
    try:
        channel_specification_document.set_channel_value(channel_name, float(channel_value))
        Screen().input("Channel value set. Press [Enter] to continue")
    except FlexLoggerError:
        Screen().input(
            'Channel value could not be set, possibly because no channel is named "'
            + channel_name
            + '". Press [Enter] to continue'
        )
    except ValueError:
        Screen().input(
            "A value of "
            + channel_value
            + " could not be set on "
            + channel_name
            + " because it could not be converted to a floating point value."
            + " Press [Enter] to continue"
        )


def _show_interactive_menu(channel_specification_document):
    """Display an interactive menu for getting and setting channel values.

    This will return when the user invokes the exit menu item.
    """

    def _create_menu(desc, epilogue_text, menu_items):
        console_menu = ConsoleMenu(
            "Getting and Setting Channel Values API Demo", desc, epilogue_text=epilogue_text
        )
        for name, fn, args, opts in menu_items:
            menu_item = FunctionItem(name, fn, args, **opts)
            console_menu.append_item(menu_item)
        return console_menu

    get_set_channel_values_menu = _create_menu(
        "",
        "",
        [
            ("Show all channel values", _show_channel_values, [channel_specification_document], {}),
            ("Set a channel value", _set_channel_value, [channel_specification_document], {}),
        ],
    )

    while True:
        get_set_channel_values_menu.show()
        if get_set_channel_values_menu.selected_item == get_set_channel_values_menu.exit_item:
            break


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Interactive/manage_test_session.py sha256=384b78e425ee5f9042af6c5d7b1066d0a777f955bf7f77732ab5ce924bf65b7a bytes=5544 -->
## FILE: examples/Interactive/manage_test_session.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Interactive/manage_test_session.py`
- sha256: `384b78e425ee5f9042af6c5d7b1066d0a777f955bf7f77732ab5ce924bf65b7a`
- bytes: 5544

````python
import os
import sys
import threading

from consolemenu import ConsoleMenu, Screen
from consolemenu.items import FunctionItem
from flexlogger.automation import Application, TestSessionState


def main(project_path):
    """Interactively manage the state of the FlexLogger project test session.

    Launch FlexLogger, open the specified project and interactively
    manage the state of the FlexLogger project test session.
    """
    print("Launching FlexLogger . . .")
    with Application.launch() as app:
        print("Loading FlexLogger project . . .")
        project = app.open_project(path=project_path)
        test_session = project.test_session

        _show_interactive_menu(test_session)

        print("Closing FlexLogger project . . .")
        project.close()
    return 0


def _start_test(test_session):
    print("Starting test. . . ")
    test_session.start()
    Screen().input("Test started. Press [Enter] to continue")


def _add_note(test_session):
    note = Screen().input("Input the note to log and press [Enter] when the note is complete: ")
    print("Adding note. . . ")
    test_session.add_note(note)
    Screen().input("Note added. Press [Enter] to continue")


def _stop_test(test_session):
    print("Stopping test. . . ")
    test_session.stop()
    Screen().input("Test stopped. Press [Enter] to continue")


def _pause_test(test_session):
    print("Pausing test. . . ")
    test_session.pause()
    Screen().input("Test paused. Press [Enter] to continue")


def _resume_test(test_session):
    print("Resuming test. . . ")
    test_session.resume()
    Screen().input("Test resumed. Press [Enter] to continue")


def _monitor_test_time(test_session):
    print("Monitoring test time. Press [Enter] to stop monitoring. . .")
    thread_exit_event = threading.Event()
    monitor_test_thread = threading.Thread(
        target=_monitor_test_time_thread, args=(test_session, thread_exit_event)
    )
    monitor_test_thread.start()
    Screen().input()
    thread_exit_event.set()
    monitor_test_thread.join()


def _monitor_test_time_thread(test_session, exit_event):
    while not exit_event.is_set():
        sys.stdout.write("Elapsed test time: " + str(test_session.elapsed_test_time)),
        sys.stdout.flush()
        sys.stdout.write("\r")


def _show_interactive_menu(test_session):
    """Display an interactive menu based on the current test session state.

    This will return when the user invokes one of the exit menu items.
    """
    # A menu item for all menus, so that test_session.state is checked again
    refresh_test_session_state = FunctionItem(
        "Refresh test session state", _no_op, should_exit=True
    )

    def _create_menu(desc, epilogue_text, menu_items):
        console_menu = ConsoleMenu("Test Session API Demo", desc, epilogue_text=epilogue_text)
        console_menu.append_item(refresh_test_session_state)
        for name, fn, args, opts in menu_items:
            menu_item = FunctionItem(name, fn, args, **opts)
            console_menu.append_item(menu_item)
        return console_menu

    # Set up the command line menus based on the current TestSessionState
    no_channel_to_log_text = (
        "Configure at least one channel that can be logged (such as a DAQ input channel) and then "
        "refresh the test session state. "
    )
    invalid_configuration_text = (
        "Review and address the errors in FlexLogger and then refresh the test session state."
    )
    menus = {
        TestSessionState.IDLE: _create_menu(
            "The test session is idle.",
            "",
            [
                ("Start Test", _start_test, [test_session], {"should_exit": True}),
            ],
        ),
        TestSessionState.RUNNING: _create_menu(
            "The test session is running.",
            "",
            [
                ("Add Note", _add_note, [test_session], {}),
                ("Pause Test", _pause_test, [test_session], {"should_exit": True}),
                ("Stop Test", _stop_test, [test_session], {"should_exit": True}),
                ("Monitor Elapsed Test Time", _monitor_test_time, [test_session], {}),
            ],
        ),
        TestSessionState.PAUSED: _create_menu(
            "The test session is paused.",
            "",
            [
                ("Add Note", _add_note, [test_session], {}),
                ("Resume Test", _resume_test, [test_session], {"should_exit": True}),
                ("Stop Test", _stop_test, [test_session], {"should_exit": True}),
                ("Monitor Elapsed Test Time", _monitor_test_time, [test_session], {}),
            ],
        ),
        TestSessionState.NO_VALID_LOGGED_CHANNELS: _create_menu(
            "The project has no channels to log.", no_channel_to_log_text, []
        ),
        TestSessionState.INVALID_CONFIGURATION: _create_menu(
            "The project has one or more errors.", invalid_configuration_text, []
        ),
    }

    while True:
        state_menu = menus[test_session.state]
        state_menu.show()
        if state_menu.selected_item == state_menu.exit_item:
            break


def _no_op():
    return


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path of project to open>" % os.path.basename(__file__))
        sys.exit()
    project_path_arg = argv[1]
    sys.exit(main(project_path_arg))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/README.rst sha256=55ef218b94e660d6da27533bb90dddb493431d45aa5b9f940c738b7d24f4e699 bytes=2257 -->
## FILE: examples/README.rst

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/README.rst`
- sha256: `55ef218b94e660d6da27533bb90dddb493431d45aa5b9f940c738b7d24f4e699`
- bytes: 2257

````rst
===========  ====================================================
Info         NI FlexLogger Examples Readme
Author       NI
===========  ====================================================

About
=====
The Python automation API and examples enable you to modify existing FlexLogger projects and control the execution of FlexLogger test sessions.

The Python Examples folder includes the following types of examples:

* Basic: Demonstrate how to perform specific tasks.
* Test Sequencer: Demonstrate how to create basic test sequences that involve FlexLogger and hardware, such as DUTs and thermal chambers.
* Interactive: Demonstrate how to use the FlexLogger Python automation API to perform tasks interactively, depending on user input.

Requirements
============
* FlexLogger 2022 Q2 or later
* Python 3.6-3.13
* pymodbus 2.5.3 (Only for the Thermal Chamber with Communication Protocol example)
* numpy 1.0 (Only for the Thermal Chamber with Communication Protocol example)

Folder Structure
================
Each FlexLogger Example folder contains the following components:

* Python Example (.py)
* Configuration file (.csv) (Only for Test Sequencer examples)
* Communication configuration file (.ini) (Only for the Thermal Chamber with Communication Protocol example)

Installation Instructions and Getting Started
=============================================
1. Use "pip" to install the "niflexlogger-automation" package, and any additonal packages::

	$ python -m pip install niflexlogger-automation

2. If running a Test Sequencer example, open the configuration file (config.csv) next to the example and modify the first column to point to a FlexLogger project. By default, the example will point to the included FlexLogger project. 

3. Run the example by using the following command through the command line interface::

	$ python "<ExamplePath>\ExampleName.py" "<Additional parameters, if needed>"

Related Resources
=================
For additional information about using the FlexLogger Python API and FlexLogger examples, refer the `Read the Docs website <https://niflexlogger-automation.readthedocs.io/en/latest>`_.

Copyright
(c) 2021 National Instruments Corporation. All rights reserved.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/generic dut/sequencer_generic_dut.py sha256=af0ee53275dbbbd51d23f515e8c1a9534d8db361eac42d96b671a37fa06a6f05 bytes=4897 -->
## FILE: examples/Test Sequencer/generic dut/sequencer_generic_dut.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/generic dut/sequencer_generic_dut.py`
- sha256: `af0ee53275dbbbd51d23f515e8c1a9534d8db361eac42d96b671a37fa06a6f05`
- bytes: 4897

````python
import os
import sys
import time
import csv
from flexlogger.automation import Application, FlexLoggerError, TestSessionState


def test_sequence1(config_file_path):
    """Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, as needed.
    """
    print("\nLaunching FlexLogger...")
    with Application.launch() as app:
        print("FlexLogger Launched Successfully!\n")
        dut_control("powerOn")
        dut_control("updateFirmware")
        test1(app, config_file_path)
        dut_control("powerOff")
    print("FlexLogger Closed Successfully")
    return


def test1(app_reference, config_path):
    with open(config_path, newline="") as csvfile:
        csvdata = csv.reader(csvfile)
        next(csvdata)  # skip header
        for row in csvdata:
            [
                proj_path,
                state0,
                time0,
                state1,
                time1,
                state2,
                time2,
                state3,
                time3,
            ] = row
            if not os.path.isabs(proj_path):
                config_root_dir = os.path.dirname(config_path)
                proj_path = os.path.normpath(os.path.join(config_root_dir, proj_path))
            print("Loading Project...")
            try:
                project = app_reference.open_project(proj_path)
            except FlexLoggerError as upstream_error:
                if not os.path.isfile(proj_path):
                    raise FileNotFoundError(
                        "\n\nCheck CSV file. Cannot find FlexLogger project at path:\n{}".format(
                            proj_path
                        )
                    ) from upstream_error
                else:
                    raise
            print("Project Loaded\n")
            test_session = project.test_session
            print("\nStarting Test...")
            start_test(test_session)
            print("Test Started\n")
            dut_control("changeState", state0)
            display_elapsed_test_time(time0, test_session)
            dut_control("changeState", state1)
            display_elapsed_test_time(time1, test_session)
            print("Pause Test")
            test_session.pause()
            dut_control("changeState", state2)
            time.sleep(5)
            print("Resume Test")
            test_session.resume()
            display_elapsed_test_time(time2, test_session)
            dut_control("changeState", state3)
            display_elapsed_test_time(time3, test_session)
            test_session.stop()
            print("Test Completed.\n\nClosing Project...")
            project.close()
            print("Project Closed\n")
    return


def start_test(
    test_session, retries=3
):  # This is a workaround for the FlexLogger API .start() method bug
    for retry in range(retries):
        test_session.start()
        if test_session.state == TestSessionState.RUNNING:
            return
        elif retry < retries - 1:
            print("Waiting for test session to start. Retry: {}".format(retry + 1))
            time.sleep(1)
            continue
        else:
            raise RuntimeError("Test did not start within timeout.")


def dut_control(command, state="error"):
    if command == "powerOn":
        print("DUT Powered ON\n")
    elif command == "powerOff":
        print("DUT Powered OFF\n")
    elif command == "changeState":
        print("Change DUT to State " + str(state))
    elif command == "updateFirmware":
        print("Simulate Downloading DUT Firmware...")
        time.sleep(2)
        print("DUT Firmware Downloaded Successfully\n")
    else:
        print("Error: Incorrect DUT Command\n")
    return


def display_elapsed_test_time(total_time, test_session):
    elapsed_time_at_start = test_session.elapsed_test_time
    time_diff = 0
    total_time_float = float(total_time)
    while time_diff < total_time_float:
        time.sleep(0.1)
        time_diff = (test_session.elapsed_test_time - elapsed_time_at_start).total_seconds()
        print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\r")
    print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\n\n")
    return


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path to CSV file>" % os.path.basename(__file__))
        sys.exit()
    config_file_path = argv[1]
    sys.exit(test_sequence1(config_file_path))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/generic dut/test config.csv sha256=93cf8de586cfe58b4963a6bb1b113846efe6a255963c74033b183a41ee6ae073 bytes=166 -->
## FILE: examples/Test Sequencer/generic dut/test config.csv

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/generic dut/test config.csv`
- sha256: `93cf8de586cfe58b4963a6bb1b113846efe6a255963c74033b183a41ee6ae073`
- bytes: 166

````csv
Project Path,DUT State,Time,DUT State,Time,DUT State,Time,DUT State,Time
<path to FlexLogger project>,0,3,1,4,0,5,2,6
<path to FlexLogger project>,0,5,1,4,0,3,2,2
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber/sequencer_thermal_chamber.py sha256=9daac50dc8900175b7ca7bddfde3157f2d6c320bb6a53f624ffb7471282f7dea bytes=6725 -->
## FILE: examples/Test Sequencer/thermal chamber/sequencer_thermal_chamber.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/thermal chamber/sequencer_thermal_chamber.py`
- sha256: `9daac50dc8900175b7ca7bddfde3157f2d6c320bb6a53f624ffb7471282f7dea`
- bytes: 6725

````python
import os
import sys
import time
import csv
from flexlogger.automation import Application, FlexLoggerError, TestSessionState


def test_sequence1(config_file_path):
    """Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT and simulated thermal chamber.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, thermal chamber commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, and replace the 'temp_chamber_control'
    function with your specific chamber's API or communication methods,
    as needed.
    """
    print("\nLaunching FlexLogger...")
    with Application.launch() as app:
        print("FlexLogger Launched Successfully!\n")
        dut_control("powerOn")
        dut_control("updateFirmware")
        test1(app, config_file_path)
        dut_control("powerOff")
    print("FlexLogger Closed Successfully")
    return


def test1(app_reference, config_path):
    with open(config_path, newline="") as csvfile:
        csvdata = csv.reader(csvfile)
        next(csvdata)  # skip header
        for row in csvdata:
            [
                proj_path,
                state0,
                time0,
                state1,
                time1,
                state2,
                time2,
                state3,
                time3,
                temp,
                hum,
                program,
            ] = row
            if not os.path.isabs(proj_path):
                config_root_dir = os.path.dirname(config_path)
                proj_path = os.path.normpath(os.path.join(config_root_dir, proj_path))
            print("Loading Project...")
            try:
                project = app_reference.open_project(proj_path)
            except FlexLoggerError as upstream_error:
                if not os.path.isfile(proj_path):
                    raise FileNotFoundError(
                        "\n\nCheck CSV file. Cannot find FlexLogger project at path:\n{}".format(
                            proj_path
                        )
                    ) from upstream_error
                else:
                    raise
            print("Project Loaded\n")
            test_session = project.test_session
            print("Configuring temperature chamber")
            temp_chamber_control("tempSetPoint", temp)
            temp_chamber_control("humSetPoint", hum)
            temp_chamber_control("changeProgram", program)
            time.sleep(5)
            print("\nStarting Test...")
            start_test(test_session)
            print("Test Started\n")
            temp_chamber_control("startChamber", "")
            dut_control("changeState", state0)
            display_elapsed_test_time(time0, test_session)
            dut_control("changeState", state1)
            display_elapsed_test_time(time1, test_session)
            print("Pause Test")
            test_session.pause()
            dut_control("changeState", state2)
            time.sleep(5)
            print("Resume Test")
            test_session.resume()
            display_elapsed_test_time(time2, test_session)
            dut_control("changeState", state3)
            display_elapsed_test_time(time3, test_session)
            test_session.stop()
            temp_chamber_control("stopChamber", "")
            print("Test Completed.\n\nClosing Project...")
            project.close()
            print("Project Closed\n")
    return


def start_test(
    test_session, retries=3
):  # This is a workaround for the FlexLogger API .start() method bug
    for retry in range(retries):
        test_session.start()
        if test_session.state == TestSessionState.RUNNING:
            return
        elif retry < retries - 1:
            print("Waiting for test session to start. Retry: {}".format(retry + 1))
            time.sleep(1)
            continue
        else:
            raise RuntimeError("Test did not start within timeout.")


def dut_control(command, state="error"):
    if command == "powerOn":
        print("DUT Powered ON\n")
    elif command == "powerOff":
        print("DUT Powered OFF\n")
    elif command == "changeState":
        print("Change DUT to State " + str(state))
    elif command == "updateFirmware":
        print("Simulate Downloading DUT Firmware...")
        time.sleep(2)
        print("DUT Firmware Downloaded Successfully\n")
    else:
        print("Error: Incorrect DUT Command\n")
    return


def temp_chamber_control(command, command_data=""):
    if command == "tempSetPoint":
        # Add code to change temperature setpoint, read response, etc.
        print("Update temperature setpoint: " + command_data + " deg")
    elif command == "humSetPoint":
        # Add code to change humidity setpoint, read response, etc.
        print("Update humidity setpoint: " + command_data + "%")
    elif command == "changeProgram":
        # Add code to change thermal chamber program or sequence, read response, etc.
        print("Set thermal chamber active program: " + command_data)
    elif command == "startChamber":
        # Add code to start the thermal chamber, read response, etc.
        print("Start thermal chamber")
    elif command == "readStatus":
        # Add code to read thermal chamber status, parse information, etc.
        chamberStatus = "Normal"
        print("Thermal chamber status: " + chamberStatus)
    elif command == "stopChamber":
        # Add code to stop the thermal chamber, read response, etc.
        print("Stop thermal chamber")
    else:
        # Add code to handle the error, throw an exception, etc.
        print("Command not available: " + command)


def display_elapsed_test_time(total_time, test_session):
    elapsed_time_at_start = test_session.elapsed_test_time
    time_diff = 0
    total_time_float = float(total_time)
    while time_diff < total_time_float:
        time.sleep(0.1)
        time_diff = (test_session.elapsed_test_time - elapsed_time_at_start).total_seconds()
        print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\r")
    print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\n\n")
    return


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: %s <path to CSV file>" % os.path.basename(__file__))
        sys.exit()
    config_file_path = argv[1]
    sys.exit(test_sequence1(config_file_path))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber/test config.csv sha256=64c447e276c7a364db6303a0af1b1bcc0f2c8ed6c71a7b08a1758efcdba383ba bytes=232 -->
## FILE: examples/Test Sequencer/thermal chamber/test config.csv

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/thermal chamber/test config.csv`
- sha256: `64c447e276c7a364db6303a0af1b1bcc0f2c8ed6c71a7b08a1758efcdba383ba`
- bytes: 232

````csv
Project Path,DUT State,Time,DUT State,Time,DUT State,Time,DUT State,Time,Temperature Set Point,Humidity Set Point,Program
<path to FlexLogger project>,0,3,1,4,0,5,2,6,80,45,1
<path to FlexLogger project>,0,5,1,4,0,3,2,2,120,55,2
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber with hardware/modbus config.ini sha256=4ef06ebaf6f752087f913362b81df01302a6b37f648e3919e3fdbca67198e0ea bytes=34 -->
## FILE: examples/Test Sequencer/thermal chamber with hardware/modbus config.ini

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/thermal chamber with hardware/modbus config.ini`
- sha256: `4ef06ebaf6f752087f913362b81df01302a6b37f648e3919e3fdbca67198e0ea`
- bytes: 34

````ini
[Modbus]
IP = 0.0.0.0
Port = 502
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber with hardware/sequencer_thermal_chamber_hardware.py sha256=6263785d269f562ec781584146e14357967f4b0d9933b47008d73b0c545cf145 bytes=8380 -->
## FILE: examples/Test Sequencer/thermal chamber with hardware/sequencer_thermal_chamber_hardware.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/thermal chamber with hardware/sequencer_thermal_chamber_hardware.py`
- sha256: `6263785d269f562ec781584146e14357967f4b0d9933b47008d73b0c545cf145`
- bytes: 8380

````python
import os
import sys
import time
import csv
import numpy as np
import configparser
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from flexlogger.automation import Application, FlexLoggerError, TestSessionState


def test_sequence1(config_file_path, modbus_config_path):
    """Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT and Modbus thermal chamber.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, thermal chamber commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, and replace the 'temp_chamber_control'
    function with your specific chamber's API or communication methods,
    as needed.

    This example is configured to communicate with a Cincinnati Sub-Zero (CSZ) EZT-570i
    Environmental Chamber Controller through a Modbus TCP communication channel. This example may
    malfunction if used with a different environmental chamber controller.
    """
    # Configure INI File parsing structure
    config = configparser.ConfigParser()
    config["Modbus"] = {"IP": "0.0.0.0", "Port": "502"}

    # read ini file
    config.read(modbus_config_path)
    ip = config["Modbus"]["IP"]
    mport = config["Modbus"]["Port"]

    print("\nLaunching FlexLogger...")
    with Application.launch() as app:
        print("FlexLogger Launched Successfully!\n")
        dut_control("powerOn")
        dut_control("updateFirmware")
        # Configure Modbus TCP connection to the Thermal Chamber
        client = ModbusClient(ip, port=mport)
        # Connect to the Thermal Chamber
        client.connect()
        test1(app_reference=app, clienthandle=client, config_path=config_file_path)
        dut_control("powerOff")
        # Close Modbus TCP connection to the Thermal Chamber
        client.close()
    print("FlexLogger Closed Successfully")
    return


def test1(app_reference, clienthandle, config_path):
    with open(config_path, newline="") as csvfile:
        csvdata = csv.reader(csvfile)
        next(csvdata)  # skip header
        for row in csvdata:
            [
                proj_path,
                state0,
                time0,
                state1,
                time1,
                state2,
                time2,
                state3,
                time3,
                temp,
                hum,
            ] = row
            if not os.path.isabs(proj_path):
                config_root_dir = os.path.dirname(config_path)
                proj_path = os.path.normpath(os.path.join(config_root_dir, proj_path))
            print("Loading Project...")
            try:
                project = app_reference.open_project(proj_path)
            except FlexLoggerError as upstream_error:
                if not os.path.isfile(proj_path):
                    raise FileNotFoundError(
                        "\n\nCheck CSV file. Cannot find FlexLogger project at path:\n{}".format(
                            proj_path
                        )
                    ) from upstream_error
                else:
                    raise
            print("Project Loaded\n")
            test_session = project.test_session
            print("Configuring temperature chamber")
            temp_chamber_control("tempSetPoint", temp, clienthandle)
            temp_chamber_control("humSetPoint", hum, clienthandle)
            time.sleep(5)
            print("\nStarting Test...")
            start_test(test_session)
            print("Test Started\n")
            temp_chamber_control("startChamber", "", clienthandle)
            dut_control("changeState", state0)
            display_elapsed_test_time(time0, test_session)
            dut_control("changeState", state1)
            display_elapsed_test_time(time1, test_session)
            print("Pause Test")
            test_session.pause()
            dut_control("changeState", state2)
            time.sleep(5)
            print("Resume Test")
            test_session.resume()
            display_elapsed_test_time(time2, test_session)
            dut_control("changeState", state3)
            display_elapsed_test_time(time3, test_session)
            test_session.stop()
            temp_chamber_control("stopChamber", "", clienthandle)
            print("Test Completed.\n\nClosing Project...")
            project.close()
            print("Project Closed\n")
    return


def start_test(
    test_session, retries=3
):  # This is a workaround for the FlexLogger API .start() method bug
    for retry in range(retries):
        test_session.start()
        if test_session.state == TestSessionState.RUNNING:
            return
        elif retry < retries - 1:
            print("Waiting for test session to start. Retry: {}".format(retry + 1))
            time.sleep(1)
            continue
        else:
            raise RuntimeError("Test did not start within timeout.")


def dut_control(command, state="error"):
    if command == "powerOn":
        print("DUT Powered ON\n")
    elif command == "powerOff":
        print("DUT Powered OFF\n")
    elif command == "changeState":
        print("Change DUT to State " + str(state))
    elif command == "updateFirmware":
        print("Simulate Downloading DUT Firmware...")
        time.sleep(2)
        print("DUT Firmware Downloaded Successfully\n")
    else:
        print("Error: Incorrect DUT Command\n")
    return


def temp_chamber_control(command, command_data, client):
    if command == "tempSetPoint":
        # CSZ Chamber values contain a single decimal place. 52.7 degrees = 527.
        updatedValue = np.uint(np.int16(int(command_data) * 10))
        # Loop 1 setpoint (Temperature) is CSZ Chamber register 60.
        client.write_register(60, updatedValue, unit=0x1)
        # Add code to read response, validate, etc.
        print("Update temperature setpoint: " + command_data + " deg")
    elif command == "humSetPoint":
        updatedValue = np.uint(np.int16(int(command_data) * 10))
        # Loop 2 setpoint (Humidity) is CSZ Chamber register 72.
        client.write_register(72, updatedValue, unit=0x1)
        # Add code to read response, validate, etc.
        print("Update humidity setpoint: " + command_data + " %")
    elif command == "startChamber":
        # CSZ Chamber register 22 controls "Chamber Manual Events".
        # Bit0 controls the chamber/temperature and Bit1 controls humidity.
        # Set both bits to 1 to enable the events. Write "3" to the register.
        client.write_register(22, 3, unit=0x1)
        # Add code to read response, validate, etc.
        print("Start chamber and enable humidity control")
    elif command == "stopChamber":
        # Register 22 controls "Chamber Manual Events".
        # Bit0 controls the chamber and Bit1 controls humidity.
        # Disable events by setting both to 0.
        client.write_register(22, 0, unit=0x1)
        # Add code to read response, validate, etc.
        print("Stop chamber and disable humidity control")
    else:
        # Add more command cases above, such as readStatus or changeProgram.
        # Add code to handle the error, throw an exception, etc.
        print("Command not available: " + command)


def display_elapsed_test_time(total_time, test_session):
    elapsed_time_at_start = test_session.elapsed_test_time
    time_diff = 0
    total_time_float = float(total_time)
    while time_diff < total_time_float:
        time.sleep(0.1)
        time_diff = (test_session.elapsed_test_time - elapsed_time_at_start).total_seconds()
        print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\r")
    print("Test Case Time: {} seconds".format(format(time_diff, ".3f")), end="\n\n")
    return


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 3:
        print("Usage: %s <path to CSV file> <path to Modbus INI>" % os.path.basename(__file__))
        sys.exit()
    config_file_path = argv[1]
    modbus_config_path = argv[2]
    sys.exit(test_sequence1(config_file_path, modbus_config_path))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber with hardware/test config.csv sha256=bf1739a95ea20e4a204f7cfe9547369c0862074100a8bee6e77efc96a8f08e01 bytes=220 -->
## FILE: examples/Test Sequencer/thermal chamber with hardware/test config.csv

- repository: `ni/niflexlogger-automation-python`
- source_path: `examples/Test Sequencer/thermal chamber with hardware/test config.csv`
- sha256: `bf1739a95ea20e4a204f7cfe9547369c0862074100a8bee6e77efc96a8f08e01`
- bytes: 220

````csv
Project Path,DUT State,Time,DUT State,Time,DUT State,Time,DUT State,Time,Temperature Set Point,Humidity Set Point
<path to FlexLogger project>,0,3,1,4,0,5,2,6,80,45
<path to FlexLogger project>,0,5,1,4,0,3,2,2,120,55
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=generate_protobuf_classes.py sha256=90518021e52a7581e4d05eb78d8088c4eda79c7ec39cd633ec6638175fe9cd29 bytes=2953 -->
## FILE: generate_protobuf_classes.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `generate_protobuf_classes.py`
- sha256: `90518021e52a7581e4d05eb78d8088c4eda79c7ec39cd633ec6638175fe9cd29`
- bytes: 2953

````python
import subprocess
import sys
from itertools import chain
from pathlib import Path
from platform import system
from shlex import quote

PROTO_PATHS = [
    "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols",
    "Core/Automation/Core.Automation.Protocols",
    "DiagramSdk/Automation/DiagramSdk.Automation.Protocols",
]

RELATIVE_DEST_DIR = Path("./flexlogger/automation/proto")


def _has_src_dir() -> bool:
    return Path("./src/").exists()


def _get_dest_dir() -> Path:
    dest_dir = Path("./src" / RELATIVE_DEST_DIR)
    if dest_dir.exists():
        return dest_dir
    return RELATIVE_DEST_DIR


def _main(*args: str) -> int:
    _prepare_dest_dir()
    _fixup_proto_files()
    exit_code = _call_protoc()
    if exit_code != 0:
        return exit_code
    _move_generated_files()
    return 0


def _prepare_dest_dir() -> None:
    for existing_generated_file in chain(
        _get_dest_dir().glob("*_pb2.py"), _get_dest_dir().glob("*_pb2_grpc.py")
    ):
        existing_generated_file.unlink()


def _fixup_proto_files() -> None:
    for path_str in PROTO_PATHS:
        for proto_file in (Path("./protobuf") / path_str).glob("*.proto"):
            _fixup_proto_file(proto_file, _get_dest_dir() / proto_file.name)


def _fixup_proto_file(src: Path, dst: Path) -> None:
    contents = src.read_text()
    for proto_path in PROTO_PATHS:
        # We want the generated classes to import other generated classes with
        # something like
        #    from flexlogger.automation.proto import Identifiers
        # So we need the "import" statement in the .proto file to match this
        contents = contents.replace(
            'import "' + proto_path + "/", 'import "flexlogger/automation/proto/'
        )
    dst.write_text(contents)


def _move_generated_files() -> None:
    source_dir = _get_dest_dir() / "flexlogger/automation/proto"
    for source_path in source_dir.glob("*.py"):
        dest_path = _get_dest_dir() / source_path.name
        source_path.rename(dest_path)
    source_dir.rmdir()
    (_get_dest_dir() / "flexlogger/automation").rmdir()
    (_get_dest_dir() / "flexlogger").rmdir()


def _call_protoc() -> int:
    args = [
        "--proto_path=.",
        "--python_out=" + str(RELATIVE_DEST_DIR),
        "--grpc_python_out=" + str(RELATIVE_DEST_DIR),
        str(RELATIVE_DEST_DIR) + "/*.proto",
    ]

    cwd = "./src" if _has_src_dir() else None

    if system() == "Windows":
        return subprocess.run([sys.executable, "-m", "grpc_tools.protoc"] + args, cwd=cwd).returncode 
    else:
        # Need to run with shell=True so the .proto files will get
        # globbed on Linux.
        return subprocess.run(' '.join([quote(sys.executable), "-m", "grpc_tools.protoc"] + args), cwd=cwd, shell=True).returncode


if __name__ == "__main__":
    sys.exit(_main(*sys.argv[1:]))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=LICENSE sha256=5c0e9ddd6af761333aa72efd7a16879f0f2176747f4fc0d23e0e759536e0e587 bytes=1080 -->
## FILE: LICENSE

- repository: `ni/niflexlogger-automation-python`
- source_path: `LICENSE`
- sha256: `5c0e9ddd6af761333aa72efd7a16879f0f2176747f4fc0d23e0e759536e0e587`
- bytes: 1080

````text
MIT License

Copyright (c) 2020 NI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=mypy.ini sha256=44b73c036c56d4a9c440a172c4bf0c28281cae282ba3f24ccd4415216854a571 bytes=841 -->
## FILE: mypy.ini

- repository: `ni/niflexlogger-automation-python`
- source_path: `mypy.ini`
- sha256: `44b73c036c56d4a9c440a172c4bf0c28281cae282ba3f24ccd4415216854a571`
- bytes: 841

````ini
[mypy]
python_version=3.6
mypy_path=src
warn_unused_configs=True
namespace_packages=True
# needed because we import things from flexlogger.automation.proto that are untyped
disallow_untyped_calls=False
disallow_untyped_defs=True
disallow_incomplete_defs=True
disallow_untyped_decorators=True

strict_equality=True

# typeshed stubs for google.protobuf are wrong, see
# https://github.com/thundergolfer/bazel-mypy-integration/issues/21
[mypy-google.protobuf.*]
follow_imports_for_stubs=True
follow_imports=skip

[mypy-flexlogger.automation.proto.*]
follow_imports_for_stubs=True
follow_imports=skip
ignore_errors=True
ignore_missing_imports=True

[mypy-grpc]
ignore_errors=True
ignore_missing_imports=True

[mypy-consolemenu.*]
ignore_missing_imports = True

[mypy-prettytable.*]
ignore_missing_imports = True
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/AutomationClientType.proto sha256=b1bd9788f7015cfb140eec641a3f1ffc2860f2e977e8e8b51c52fc7800aceb8d bytes=676 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/AutomationClientType.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/AutomationClientType.proto`
- sha256: `b1bd9788f7015cfb140eec641a3f1ffc2860f2e977e8e8b51c52fc7800aceb8d`
- bytes: 676

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum AutomationClientType {
  // The application type that is connecting to FlexLogger through API is Unknown.
  CLIENT_TYPE_UNKNOWN = 0;
  // The application type that is connecting to FlexLogger through API is Python.
  CLIENT_TYPE_PYTHON = 1;
  // The application type that is connecting to FlexLogger through API is LabVIEW.
  CLIENT_TYPE_LABVIEW = 2;
  // The application type that is connecting to FlexLogger through API is TestStand.
  CLIENT_TYPE_TESTSTAND = 3;
  // The application type that is connecting to FlexLogger through API is .NET.
  CLIENT_TYPE_DOTNET = 4;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ChannelSpecificationDocument.proto sha256=7fbd51642f5d14e976ac5fb13955dabffd13d50855b37e8cefb7843813908056 bytes=10544 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ChannelSpecificationDocument.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ChannelSpecificationDocument.proto`
- sha256: `7fbd51642f5d14e976ac5fb13955dabffd13d50855b37e8cefb7843813908056`
- bytes: 10544

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/DataRateLevel.proto";
import "DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/timestamp.proto";

// Service interface for a server side channel specification document.
service ChannelSpecificationDocument {
    // RPC call to get all channel names
    rpc GetChannelNames(GetChannelNamesRequest) returns (GetChannelNamesResponse) {}
    // RPC call to get channel names filtered by channel type
    rpc GetFilteredChannelNames(GetFilteredChannelNamesRequest) returns (GetChannelNamesResponse) {}
    // RPC call to get the latest value of a double channel
    rpc GetDoubleChannelValue(GetDoubleChannelValueRequest) returns (GetDoubleChannelValueResponse) {}
    // RPC call to set the value of a double channel
    rpc SetDoubleChannelValue(SetDoubleChannelValueRequest) returns (SetDoubleChannelValueResponse) {}
    // RPC call to get the latest values of double channels
    rpc GetDoubleChannelValues(GetDoubleChannelValuesRequest) returns (GetDoubleChannelValuesResponse) {}
    // RPC call to set the values of double channels
    rpc SetDoubleChannelValues(SetDoubleChannelValuesRequest) returns (google.protobuf.Empty) {}
    // RPC call to get a channel's enable state
    rpc IsChannelEnabled(IsChannelEnabledRequest) returns (IsChannelEnabledResponse) {}
    // RPC call to enable/disable channels
    rpc SetChannelEnabled(SetChannelEnabledRequest) returns (SetChannelEnabledResponse) {}
    // RPC call to get a channel logging's state
    rpc IsChannelLoggingEnabled(IsChannelLoggingEnabledRequest) returns (IsChannelLoggingEnabledResponse) {}
    // RPC call to enable/disable channel logging
    rpc SetChannelLoggingEnabled(SetChannelLoggingEnabledRequest) returns (SetChannelLoggingEnabledResponse) {}
    // RPC call to get the data rate for a specific data rate level
    rpc GetDataRate(GetDataRateRequest) returns (GetDataRateResponse) {}
    // RPC call to set the data rate of a specific data rate level
    rpc SetDataRate(SetDataRateRequest) returns (google.protobuf.Empty) {}
    // RPC call to get the data rate level of the subsystem that owns a channel
    rpc GetDataRateLevel(GetDataRateLevelRequest) returns (GetDataRateLevelResponse) {}
    // RPC call to set the data rate level of the subsystem that owns a channel
    rpc SetDataRateLevel(SetDataRateLevelRequest) returns (google.protobuf.Empty) {}
    // RPC call to get the actual data rate of the subsystem that owns a channel
    rpc GetActualDataRate(GetActualDataRateRequest) returns (GetActualDataRateResponse) {}
}

// Request object for getting all channel names
message GetChannelNamesRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for getting all channel names
message GetChannelNamesResponse {
    // The channels defined in the channel specification. Can be empty.
    repeated string channel_names = 1;
}

// Request object for getting channel names filtered by channel type
message GetFilteredChannelNamesRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // Return configured channels.
    bool configuredChannels = 2;
    // Return input channels.
    bool inputChannels = 3;
    // Return output channels.
    bool outputChannels = 4;
    // Return analog channels.
    bool analogChannels = 5;
    // Return digital channels.
    bool digitalChannels = 6;
}

// Request object for getting a channel value
message GetDoubleChannelValueRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to get a double value for
    string channel_name = 2;
}

// Response object for getting a channel value
message GetDoubleChannelValueResponse {
    // The timestamp indicating when the channel value occurred
    google.protobuf.Timestamp value_timestamp = 1;
    // The value of the channel at the timestamp
    double channel_value = 2;
}

// Request object for setting a channel value
message SetDoubleChannelValueRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to set
    string channel_name = 2;
    // The value of the channel to set
    double channel_value = 3;
}

// Response object for setting a channel value
message SetDoubleChannelValueResponse {
}

// Message that defines an individual channel value
message ChannelValue {
    // The name of the channel
    string channel_name = 1;
    // The value of the channel
    double channel_value = 2;
    // The timestamp of the value
    google.protobuf.Timestamp value_timestamp = 3;
}

// Request object for getting channel values
message GetDoubleChannelValuesRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The names of the channels to get double values for
    repeated string channel_names = 2;
}

// Response object for getting channel values
message GetDoubleChannelValuesResponse {
    // The channel values and their timestamps
    repeated ChannelValue channel_values = 1;
}

// Request object for setting channel values
message SetDoubleChannelValuesRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The channel values to set
    repeated ChannelValue channel_values = 2;
}

// Request object for getting a channel enable state
message IsChannelEnabledRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to get the enable state for
    string channel_name = 2;
}

// Response object for getting a channel enable state
message IsChannelEnabledResponse {
    bool channel_enabled = 1;
}

// Request object for setting a channel enable state
message SetChannelEnabledRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to enable or disable
    string channel_name = 2;
    // The enable state to set
    bool channel_enabled = 3;
}

// Response object for setting a channel enable state
message SetChannelEnabledResponse {
}

// Request object for getting a channel logging state
message IsChannelLoggingEnabledRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to get the logging state for
    string channel_name = 2;
}

// Response object for getting a channel logging state
message IsChannelLoggingEnabledResponse {
    bool channel_logging_enabled = 1;
}

// Request object for setting a channel logging state
message SetChannelLoggingEnabledRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel to enable or disable
    string channel_name = 2;
    // The enable state to set
    bool channel_logging_enabled = 3;
}

// Response object for setting a channel enable state
message SetChannelLoggingEnabledResponse {
}

// Request object for getting the data rate
message GetDataRateRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The data rate level (Slow, Medium, Fast, Counter, Digital, OnDemand)
    DataRateLevel data_rate_level = 2;
}

// Response object for getting the data rate
message GetDataRateResponse {
    // The value of the data rate
    double data_rate = 1;
}

// Request object for setting the data rate
message SetDataRateRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The data rate level (Slow, Medium, Fast, Counter, Digital, OnDemand)
    DataRateLevel data_rate_level = 2;
    // The value of the data rate to set
    double data_rate = 3;
}

// Request object for getting the data rate of a specific channel
message GetDataRateLevelRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel in the subsystem to set the data rate to
    string channel_name = 2;
}

// Response object for getting the data rate of a specific channel
message GetDataRateLevelResponse {
    // The data rate level
    DataRateLevel data_rate_level = 1;
}

// Request object for setting the data rate level of a specific channel
message SetDataRateLevelRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel in the subsystem to set the data rate to
    string channel_name = 2;
    // The data rate level to set
    DataRateLevel data_rate_level = 3;
}

// Request object for getting the actual data rate of a specific channel
message GetActualDataRateRequest {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the channel in the subsystem to set the data rate to
    string channel_name = 2;
}

// Response object for getting the actual data rate of a specific channel
message GetActualDataRateResponse {
    // The data rate
    double data_rate = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/DataRateLevel.proto sha256=13cb09fc5d38396e5b3f5fd3fb4aa5aa593e2ad9d552b1906c8a09dbbeaa01ad bytes=516 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/DataRateLevel.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/DataRateLevel.proto`
- sha256: `13cb09fc5d38396e5b3f5fd3fb4aa5aa593e2ad9d552b1906c8a09dbbeaa01ad`
- bytes: 516

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum DataRateLevel {
  DATA_RATE_LEVEL_NONE = 0;
  // The slow analog input rate
  DATA_RATE_LEVEL_SLOW = 1;
  // The medium analog input rate
  DATA_RATE_LEVEL_MEDIUM = 2;
  // The fast analog input rate
  DATA_RATE_LEVEL_FAST = 3;
  // The counter input rate
  DATA_RATE_LEVEL_COUNTER = 4;
  // The digital input rate
  DATA_RATE_LEVEL_DIGITAL = 6;
  // On demand sample rate
  DATA_RATE_LEVEL_ON_DEMAND = 7;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Document.proto sha256=cb6e9725f4c30fdf92fe558e342fb299ed4f34c0f2e267f6445e8871246ad8be bytes=684 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Document.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Document.proto`
- sha256: `cb6e9725f4c30fdf92fe558e342fb299ed4f34c0f2e267f6445e8871246ad8be`
- bytes: 684

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto";

// Service interface for a server side document.
service Document {
  // RPC call to close the current document.
  rpc Close(CloseDocumentRequest) returns (CloseDocumentResponse) {}
}

// Request object for closing the specified document.
message CloseDocumentRequest {
    // The id of the envoy whose document should be closed.
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier envoy = 1;
}

// Response object for closing a document.
message CloseDocumentResponse {}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Events.proto sha256=2cc7189c7eff17ff02a3e4560e724e01790d70cd68f8bc54db2febbeb5e50430 bytes=2036 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Events.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Events.proto`
- sha256: `2cc7189c7eff17ff02a3e4560e724e01790d70cd68f8bc54db2febbeb5e50430`
- bytes: 2036

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/EventType.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/timestamp.proto";

// Service interface for the FlexLogger events.
service FlexLoggerEvents {
  // RPC call to send an event for test purposes.
  rpc SendEvent(SubscribeToEventsResponse) returns (google.protobuf.Empty) {}
  // RPC call to subscribe to FlexLogger events.
  rpc SubscribeToEvents(SubscribeToEventsRequest) returns (stream SubscribeToEventsResponse) {}
  // RPC call to unsubscribe from events.
  rpc UnsubscribeFromEvents(UnsubscribeFromEventsRequest) returns (google.protobuf.Empty) {}
  // RPC call to specify which events to subscribe to.
  rpc RegisterEvents(SubscribeToEventsRequest) returns (google.protobuf.Empty) {}
  // RPC call to get which events are currently registered.
  rpc GetRegisteredEvents(GetRegisteredEventsRequest) returns (GetRegisteredEventsResponse) {}
}

// Request object for subscribing to events
message SubscribeToEventsRequest {
    // The event client id
    string client_id = 1;
    // The event types to register to
    repeated EventType event_types = 2;
}

// SubscribeToEvents Response
message SubscribeToEventsResponse {
    // The type of event being sent
    EventType event_type = 1;
    // Event Name
    string event_name = 2;
    // Event payload
    string payload = 3;
    // Time the event was sent
    google.protobuf.Timestamp timestamp = 4;
}

// Request object for unsubscribing
message UnsubscribeFromEventsRequest {
    // The event client id
    string client_id = 1;
}

// Request object for getting registered events
message GetRegisteredEventsRequest {
    // The event client id
    string client_id = 1;
}

// GetRegisteredEvents response
message GetRegisteredEventsResponse {
    // The registered events
    repeated EventType event_types = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/EventType.proto sha256=a33b670193bb3c25de55f3a027cf7b3b01b63b1ca7b6bdbc3bf2ef255ca3f0fb bytes=327 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/EventType.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/EventType.proto`
- sha256: `a33b670193bb3c25de55f3a027cf7b3b01b63b1ca7b6bdbc3bf2ef255ca3f0fb`
- bytes: 327

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum EventType {
  EVENT_TYPE_NONE = 0;
  // Alarm event
  EVENT_TYPE_ALARM = 1;
  // Log File event
  EVENT_TYPE_LOG_FILE = 2;
  // Test Session event
  EVENT_TYPE_TEST_SESSION = 3;
  // Custom event
  EVENT_TYPE_CUSTOM = 4;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/FlexLoggerApplication.proto sha256=f2019b66ea20352f47c5d0cccb2dac7ff749a8c555b2636e7b54ed8991f0c4de bytes=2469 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/FlexLoggerApplication.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/FlexLoggerApplication.proto`
- sha256: `f2019b66ea20352f47c5d0cccb2dac7ff749a8c555b2636e7b54ed8991f0c4de`
- bytes: 2469

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto";
import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/AutomationClientType.proto";
import "google/protobuf/empty.proto";

// Service interface for the server application.
service FlexLoggerApplication {
  // RPC call to open an existing project on the server.
  rpc OpenProject(OpenProjectRequest) returns (OpenProjectResponse) {}
  // RPC call to get the currently active (open) project from the server.
  rpc GetActiveProject(GetActiveProjectRequest) returns (GetActiveProjectResponse) {}
  // RPC call to get the FlexLogger version from the server.
  rpc GetVersion(google.protobuf.Empty) returns (GetVersionResponse) {}
  // RPC call to initialize the API client
  rpc Initialize(InitializeRequest) returns (google.protobuf.Empty) {}
}

// Information necessary to open an existing Project.
message OpenProjectRequest {
    // The path to the existing project to be opened.
    string project_path = 1;
}

// An identifier used to identify a particular project.  The id is unique for
// each project that is created or opened in this instance.
message OpenProjectResponse {
    // The id of the project that was opened.
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Information needed to request the active project.
message GetActiveProjectRequest {
}

// Response object for the get active project request.
message GetActiveProjectResponse {
    // Indicates if there is an active project. If true, the project id will be valid. If false, the project id is not valid.
    bool active_project_available = 1;
    // The id of the active project. Should not be used if active_project_available is false.
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 2;
}

// Response object for the get version request.
message GetVersionResponse {
    // The numeric internal version (24.0.0.0)
    string version = 1;
    // The string version contaning the year and quarter (2024 Q1)
    string version_string = 2;
}

// Client initialization request, to be called immediately after connecting.
message InitializeRequest
{
    // The client type (Python, C#, TestStand, LabVIEW, etc)
    AutomationClientType client_type = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/LoggingSpecificationDocument.proto sha256=ae54cb858618954befde17a6461d5185d9c06cb126f24ad300d32399f836154c bytes=17081 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/LoggingSpecificationDocument.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/LoggingSpecificationDocument.proto`
- sha256: `ae54cb858618954befde17a6461d5185d9c06cb126f24ad300d32399f836154c`
- bytes: 17081

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StartTriggerCondition.proto";
import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StopTriggerCondition.proto";
import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ValueChangeType.proto";
import "DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/timestamp.proto";

// Service interface for a server side logging specification document.
service LoggingSpecificationDocument {
    // RPC call to get the log file base path
    rpc GetLogFileBasePath(GetLogFileBasePathRequest) returns (GetLogFileBasePathResponse) {}
    // RPC call to set the log file base path
    rpc SetLogFileBasePath(SetLogFileBasePathRequest) returns (SetLogFileBasePathResponse) {}
    // RPC call to get the log file name
    rpc GetLogFileName(GetLogFileNameRequest) returns (GetLogFileNameResponse) {}
    // RPC call to set the log file name
    rpc SetLogFileName(SetLogFileNameRequest) returns (SetLogFileNameResponse) {}
    // RPC call to get the description
    rpc GetLogFileDescription(GetLogFileDescriptionRequest) returns (GetLogFileDescriptionResponse) {}
    // RPC call to set the description
    rpc SetLogFileDescription(SetLogFileDescriptionRequest) returns (google.protobuf.Empty) {}
    // RPC call to get items from the data files pane
    rpc GetLogFiles(GetLogFilesRequest) returns (GetLogFilesResponse) {}
    // RPC call to clear the data files pane
    rpc RemoveLogFiles(RemoveLogFilesRequest) returns (google.protobuf.Empty) {}
    // RPC call to get all test properties
    rpc GetTestProperties(GetTestPropertiesRequest) returns (GetTestPropertiesResponse) {}
    // RPC call to set all test properties
    rpc SetTestProperties(SetTestPropertiesRequest) returns (google.protobuf.Empty) {}
    // RPC call to get a specific test property
    rpc GetTestProperty(GetTestPropertyRequest) returns (GetTestPropertyResponse) {}
    // RPC call to set a specific test property
    rpc SetTestProperty(SetTestPropertyRequest) returns (SetTestPropertyResponse) {}
    // RPC call to remove a specific test property
    rpc RemoveTestProperty(RemoveTestPropertyRequest) returns (RemoveTestPropertyResponse) {}
    // RPC call to get the resolved log file base path
    rpc GetResolvedLogFileBasePath(GetResolvedLogFileBasePathRequest) returns (GetResolvedLogFileBasePathResponse) {}
    // RPC call to get the resolved log file name
    rpc GetResolvedLogFileName(GetResolvedLogFileNameRequest) returns (GetResolvedLogFileNameResponse) {}
    // RPC call to get the start trigger settings
    rpc GetStartTriggerSettings(GetStartTriggerSettingsRequest) returns (GetStartTriggerSettingsResponse) {}
    // RPC call to get the stop trigger settings
    rpc GetStopTriggerSettings(GetStopTriggerSettingsRequest) returns (GetStopTriggerSettingsResponse) {}
    // RPC call to set the start trigger settings to Test Start
    rpc SetTestStartTriggerSettings(SetTestStartTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the start trigger settings to Channel value change
    rpc SetValueChangeStartTriggerSettings(SetValueChangeStartTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the start trigger settings to Absolute time
    rpc SetTimeStartTriggerSettings(SetTimeStartTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the start trigger settings to Elapsed time
    rpc SetElapsedTimeStartTriggerSettings(SetElapsedTimeStartTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the start trigger settings to a button press
    rpc SetButtonPressedStartTriggerSettings(SetButtonPressedStartTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the stop trigger settings to Test stop
    rpc SetTestStopTriggerSettings(SetTestStopTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the stop trigger settings to Channel value change
    rpc SetValueChangeStopTriggerSettings(SetValueChangeStopTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the stop trigger settings to Test time elapsed
    rpc SetTimeStopTriggerSettings(SetTimeStopTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to set the stop trigger settings to a button press
    rpc SetButtonPressedStopTriggerSettings(SetButtonPressedStopTriggerSettingsRequest) returns (google.protobuf.Empty) {}
    // RPC call to get the retrigerring configuration
    rpc IsRetriggeringEnabled(IsRetriggeringEnabledRequest) returns (IsRetriggeringEnabledResponse) {}
    // RPC call to set the retrigerring configuration
    rpc SetRetriggering(SetRetriggeringRequest) returns (google.protobuf.Empty) {}
}

// Request object for getting the log file base path
message GetLogFileBasePathRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a get log file base path request
message GetLogFileBasePathResponse {
    // The log file base path
    string log_file_base_path = 1;
}

// Request object for setting the log file base path
message SetLogFileBasePathRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The log file base path
    string log_file_base_path = 2;
}

// Response object for a set log file base path request
message SetLogFileBasePathResponse {
}

// Request object for getting the log file name
message GetLogFileNameRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a get log file name request
message GetLogFileNameResponse {
    // The log file name
    string log_file_name = 1;
}

// Request object for setting the log file name
message SetLogFileNameRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The log file name
    string log_file_name = 2;
}

// Response object for a set log file name
message SetLogFileNameResponse {
}

// Request object for getting the log file description
message GetLogFileDescriptionRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a get log file description request
message GetLogFileDescriptionResponse {
    // The log file description
    string log_file_description = 1;
}

// Request object for setting the log file description
message SetLogFileDescriptionRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The log file description
    string log_file_description = 2;
}

// Log file types
enum LogFileType {
    // TDMS files
    TDMS = 0;
    // CSV files
    CSV = 1;
    // TDMS backup files
    TDMS_BACKUP = 2;
}

// Request object for GetLogFiles
message GetLogFilesRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The type of log files to get
    LogFileType log_file_type = 2;
}

// Response object for GetLogFiles
message GetLogFilesResponse {
    // The full paths on disk of the log files, sorted chronologically by file creation time
    repeated string log_files = 1;
}

// Request object for RemoveLogFiles
message RemoveLogFilesRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // Delete files on disk?
    bool delete_files = 2;
}

// Message that defines an individual test property
message TestProperty {
    string property_name = 1;
    string property_value = 2;
    bool prompt_on_start = 3;
}

// Request object for getting all test properties
message GetTestPropertiesRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for getting all test properties
message GetTestPropertiesResponse {
    // The test properties for the logging specification document. Can be empty.
    repeated TestProperty test_properties = 1;
}

// Request object for setting all test properties
message SetTestPropertiesRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The test properties for the logging specification document. Can be empty.
    repeated TestProperty test_properties = 2;
}

// Request object for getting a specific test property
message GetTestPropertyRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the test property to get
    string property_name = 2;
}

// Response object for getting a specific test property
message GetTestPropertyResponse {
    // The requested test property
    TestProperty test_property = 1;
}

// Request object for setting a specific test property
message SetTestPropertyRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The test property to set
    TestProperty test_property = 2;
}

// Response object for setting a specific test property
message SetTestPropertyResponse {
}

// Request object for removing a specific test property
message RemoveTestPropertyRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The name of the test property to remove
    string property_name = 2;
}

// Response object for removing a specific test property
message RemoveTestPropertyResponse {
}

// Request object for getting the resolved log file base path
message GetResolvedLogFileBasePathRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a get resolved log file base path request
message GetResolvedLogFileBasePathResponse {
    // The resolved log file base path. The resolved base path has all placeholders converted to actual values.
    string resolved_log_file_base_path = 1;
}

// Request object for getting the resolved log file name
message GetResolvedLogFileNameRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a get resolved log file name request
message GetResolvedLogFileNameResponse {
    // The resolved log file name.  The resolved file name has all placeholders converted to actual values.
    string resolved_log_file_name = 1;
}

// Request object for getting the start trigger settings
message GetStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for a getting the start trigger settings
message GetStartTriggerSettingsResponse {
    // The start trigger condition
    StartTriggerCondition start_trigger_condition = 1;
    // The start trigger settings
    string start_trigger_settings = 2;
}

// Request object for getting the stop trigger settings
message GetStopTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for getting the stop trigger settings
message GetStopTriggerSettingsResponse {
    // The stop trigger condition
    StopTriggerCondition stop_trigger_condition = 1;
    // The stop trigger settings
    string stop_trigger_settings = 2;
}

// Request object for SetTestStartTriggerSettings
message SetTestStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Request object for SetValueChangeStartTriggerSettings
message SetValueChangeStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The channel name
    string channel_name = 2;
    // The value change condition
    ValueChangeType value_change_type = 3;
    // The threshold
    double threshold = 4;
    // The min value
    double min_value = 5;
    // The max value
    double max_value = 6;
    // The leading time to include in seconds
    double leading_time = 7;
}

// Request object for SetTimeStartTriggerSettings
message SetTimeStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The time to start the test
    google.protobuf.Timestamp time = 2;
}

message SetElapsedTimeStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The time to start the test
    double elapsed_time = 2;
}

// Request object for SetButtonPressedStartTriggerSettings
message SetButtonPressedStartTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The button name to start the test
    string button_name = 2;
}

// Request object for SetTestStopTriggerSettings
message SetTestStopTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Request object for SetValueChangeStopTriggerSettings
message SetValueChangeStopTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The channel name
    string channel_name = 2;
    // The value change condition
    ValueChangeType value_change_type = 3;
    // The threshold
    double threshold = 4;
    // The min value
    double min_value = 5;
    // The max value
    double max_value = 6;
    // The leading time to include in seconds
    double trailing_time = 7;
}

// Request object for SetTimeStopTriggerSettings
message SetTimeStopTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The duration
    google.protobuf.Duration duration = 2;
}

// Request object for SetButtonPressedStopTriggerSettings
message SetButtonPressedStopTriggerSettingsRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The button name to stop the test
    string button_name = 2;
}

// Request object for IsRetriggeringEnabled
message IsRetriggeringEnabledRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Response object for IsRetriggeringEnabled
message IsRetriggeringEnabledResponse {
    // The retriggering configuration
    bool is_retriggering_enabled = 1;
}

// Request object for SetRetriggering
message SetRetriggeringRequest {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
    // The triggering configuration
    bool is_retriggering_enabled = 2;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Project.proto sha256=a2ca66cb559df91b078eb165c15955fec5d4b4a65bdf1f267eeb629ad5782098 bytes=4704 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Project.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/Project.proto`
- sha256: `a2ca66cb559df91b078eb165c15955fec5d4b4a65bdf1f267eeb629ad5782098`
- bytes: 4704

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto";
import "google/protobuf/empty.proto";

// Service interface for a server side project.
service Project {
  // RPC call to open the channel specification document
  rpc OpenChannelSpecificationDocument(OpenChannelSpecificationDocumentRequest) returns (OpenChannelSpecificationDocumentResponse) {}
  // RPC call to open the logging specification document
  rpc OpenLoggingSpecificationDocument(OpenLoggingSpecificationDocumentRequest) returns (OpenLoggingSpecificationDocumentResponse) {}
  // RPC call to open the specified screen document
  rpc OpenScreenDocument(OpenScreenDocumentRequest) returns (OpenScreenDocumentResponse) {}
  // RPC call to open the test specification document
  rpc OpenTestSpecificationDocument(OpenTestSpecificationDocumentRequest) returns (OpenTestSpecificationDocumentResponse) {}
  // RPC call to close the current project.
  rpc Close(CloseProjectRequest) returns (CloseProjectResponse) {}
  // RPC call to query the file path of the current project.
  rpc GetProjectFilePath(GetProjectFilePathRequest) returns (GetProjectFilePathResponse) {}
  // RPC call to save the current project.
  rpc Save(google.protobuf.Empty) returns (google.protobuf.Empty) {}
  // RPC call to save the current project with a specific file path.
  rpc SaveAs(SaveAsRequest) returns (SaveAsResponse) {}
}

message SaveAsRequest {
    // The path to the existing project to be opened.
    string project_name = 1;
    string project_directory = 2;
}

message SaveAsResponse {
    // The id of the project that was saved.
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Information necessary to open the channel specification document.
message OpenChannelSpecificationDocumentRequest {
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Response object for the open channel specificaiton document request.
message OpenChannelSpecificationDocumentResponse {
    // The id for the channel specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Information necessary to open the logging specification document.
message OpenLoggingSpecificationDocumentRequest {
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Response object for the open logging specificaiton document request.
message OpenLoggingSpecificationDocumentResponse {
    // The id for the logging specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Information necessary to open a specific screen document.
message OpenScreenDocumentRequest {
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
    // The name of the scren document to open
    string screen_name = 2;
}

// Response object for the open screen document request.
message OpenScreenDocumentResponse {
    // The id for the screen document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Information necessary to open the test specification document.
message OpenTestSpecificationDocumentRequest {
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Response object for the open test specificaiton document request.
message OpenTestSpecificationDocumentResponse {
    // The id for the test specification document
    national_instruments.diagram_sdk.automation.protocols.ElementIdentifier document_identifier = 1;
}

// Message sent to close the current project.
message CloseProjectRequest {
    // True to allow prompts to be displayed.
    bool allow_prompts = 1;
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 2;
}

// The result of the close project message.
message CloseProjectResponse {}

// Request object for getting the project file path
message GetProjectFilePathRequest {
    // Project envoy identifier
    national_instruments.diagram_sdk.automation.protocols.ProjectIdentifier project = 1;
}

// Response object for a get project file path request
message GetProjectFilePathResponse {
    // The project file path
    string project_file_path = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ScreenDocument.proto sha256=2f310daf959f5a042e0d99bf0fdff962ba8794de7f72ba32fceeb9fa724888f9 bytes=177 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ScreenDocument.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ScreenDocument.proto`
- sha256: `2f310daf959f5a042e0d99bf0fdff962ba8794de7f72ba32fceeb9fa724888f9`
- bytes: 177

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

// Service interface for a server side screen document.
service ScreenDocument {
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StartTriggerCondition.proto sha256=aa2ad8660bec4ea97ca8d779d6be7a0d5cdef6dde4776645b0671d3216a94a6d bytes=347 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StartTriggerCondition.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StartTriggerCondition.proto`
- sha256: `aa2ad8660bec4ea97ca8d779d6be7a0d5cdef6dde4776645b0671d3216a94a6d`
- bytes: 347

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum StartTriggerCondition {
  START_TRIGGER_CONDITION_TEST_START = 0;
  START_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE  = 1;
  START_TRIGGER_CONDITION_TIME = 2;
  START_TRIGGER_CONDITION_TIME_ELAPSED = 3;
  START_TRIGGER_CONDITION_BUTTON_PRESSED = 4;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StopTriggerCondition.proto sha256=997c0aab52ae4bab299365e380a80e077ae6a36a50553eec7cc4743acc7f7754 bytes=304 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StopTriggerCondition.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/StopTriggerCondition.proto`
- sha256: `997c0aab52ae4bab299365e380a80e077ae6a36a50553eec7cc4743acc7f7754`
- bytes: 304

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum StopTriggerCondition {
  STOP_TRIGGER_CONDITION_TEST_STOP = 0;
  STOP_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE  = 1;
  STOP_TRIGGER_CONDITION_TIME_ELAPSED = 2;
  STOP_TRIGGER_CONDITION_BUTTON_PRESSED = 3;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSession.proto sha256=b7f53c6ba35891e9a6d8ed418872624a7fc8099520053ad8ebe2141c00daaa07 bytes=3086 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSession.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSession.proto`
- sha256: `b7f53c6ba35891e9a6d8ed418872624a7fc8099520053ad8ebe2141c00daaa07`
- bytes: 3086

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

import "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSessionState.proto";

// Service interface for a server side test session.
service TestSession {
    // RPC call to add a note to the log file. Notes can only be added while the test session is running.
    rpc AddNote(AddNoteRequest) returns (AddNoteResponse) {}
    // RPC call to get the state of the test session.
    rpc GetState(GetTestSessionStateRequest) returns (GetTestSessionStateResponse) {}
    // RPC call to start the test session.
    rpc Start(StartTestSessionRequest) returns (StartTestSessionResponse) {}
    // RPC call to stop the test session.
    rpc Stop(StopTestSessionRequest) returns (StopTestSessionResponse) {}
    // RPC call to pause the test session.
    rpc Pause(PauseTestSessionRequest) returns (PauseTestSessionResponse) {}
    // RPC call to resume the test session.
    rpc Resume(ResumeTestSessionRequest) returns (ResumeTestSessionResponse) {}
    // RPC call to query elapsed test time
    rpc GetElapsedTestTime(GetElapsedTestTimeRequest) returns (GetElapsedTestTimeResponse) {}
}

// Request object for adding a note.
message AddNoteRequest {
    // The note to add to the log file.
    string note = 1;
}

// Response object for an add note request.
message AddNoteResponse {
}

// Request object for getting the state of the test session.
message GetTestSessionStateRequest {
}

// Response object for a get test session state request.
message GetTestSessionStateResponse {
    // The state of the test session
    TestSessionState test_session_state = 1;
}

// Request object for starting the test session.
message StartTestSessionRequest {
}

// Response object for a start test session request.
message StartTestSessionResponse {
    // Indicates if the test session was started
    bool test_session_started = 1;
}

// Request object for stopping the test session.
message StopTestSessionRequest {
}

// Response object for a stop test session request.
message StopTestSessionResponse {
    // Indicates if the test session was stopped
    bool test_session_stopped = 1;
}

// Request object for pausing the test session.
message PauseTestSessionRequest {
}

// Response object for a pause test session request.
message PauseTestSessionResponse {
    // Indicates if the test session was paused
    bool test_session_paused = 1;
}

// Request object for resuming the test session.
message ResumeTestSessionRequest {
}

// Response object for a resume test session request.
message ResumeTestSessionResponse {
    // Indicates if the test session was resumed
    bool test_session_resumed = 1;
}

// Request object for querying elapsed test time.
message GetElapsedTestTimeRequest {
}

// Response object for querying elapsed test time request.
message GetElapsedTestTimeResponse {
    // Indicates the elapsed test time (in seconds)
    double elapsed_test_time = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSessionState.proto sha256=729c9b26beea79cfe33abbc93387fd7ae0abcc021d2551fbb70e0e0a2b9dc575 bytes=647 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSessionState.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSessionState.proto`
- sha256: `729c9b26beea79cfe33abbc93387fd7ae0abcc021d2551fbb70e0e0a2b9dc575`
- bytes: 647

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum TestSessionState {
  // The test session is idle and ready to start.
  TEST_SESSION_STATE_IDLE = 0;
  // The test session is currently running.
  TEST_SESSION_STATE_RUNNING = 2;
  // The project has an invalid configuration. The test session cannot be started.
  TEST_SESSION_STATE_INVALID_CONFIGURATION = 3;
  // The project does not have any valid channels that can be logged. The test session cannot be started.
  TEST_SESSION_STATE_NO_VALID_LOGGED_CHANNELS = 4;
  // The test session is currently paused.
  TEST_SESSION_STATE_PAUSED = 5;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSpecificationDocument.proto sha256=16ebcf45d5ab73f4834b3369af4cf82a4cc26ac4cdba55e4429921bfb9bb7d46 bytes=200 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSpecificationDocument.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/TestSpecificationDocument.proto`
- sha256: `16ebcf45d5ab73f4834b3369af4cf82a4cc26ac4cdba55e4429921bfb9bb7d46`
- bytes: 200

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

// Service interface for a server side test specification document.
service TestSpecificationDocument {
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ValueChangeType.proto sha256=25691b3da61154cf197392524e53e6b929542ba4af8a491b00c7292586b21a71 bytes=323 -->
## FILE: protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ValueChangeType.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols/ValueChangeType.proto`
- sha256: `25691b3da61154cf197392524e53e6b929542ba4af8a491b00c7292586b21a71`
- bytes: 323

````protobuf
syntax = "proto3";

package national_instruments.flex_logger.automation.protocols;

enum ValueChangeType {
  TYPE_NONE = 0;
  TYPE_RISE_ABOVE_VALUE = 1;
  TYPE_RISE_ABOVE_VALUE_INCLUSIVE = 2;
  TYPE_FALL_BELOW_VALUE = 3;
  TYPE_FALL_BELOW_VALUE_INCLUSIVE = 4;
  TYPE_ENTER_RANGE = 5;
  TYPE_LEAVE_RANGE = 6;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/Core/Automation/Core.Automation.Protocols/Application.proto sha256=77d6feca062b8473aea6710547c94d5fe7fd1ee42c32b5c5389aaf5ef8a2ad2f bytes=1398 -->
## FILE: protobuf/Core/Automation/Core.Automation.Protocols/Application.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/Core/Automation/Core.Automation.Protocols/Application.proto`
- sha256: `77d6feca062b8473aea6710547c94d5fe7fd1ee42c32b5c5389aaf5ef8a2ad2f`
- bytes: 1398

````protobuf
syntax = "proto3";

package national_instruments.core.automation.protocols;

// Service interface for a service side Log.
service Application {
    // RPC call to connect from the client to the server.
    rpc Connect(ConnectRequest) returns (ConnectResponse) {}
    // RPC call to shutdown the server.
    rpc Disconnect(DisconnectRequest) returns (DisconnectResponse) {}
    // RPT call to get the preferences directory for the application
    rpc GetPreferencesDirectory(GetPreferencesDirectoryRequest) returns (GetPreferencesDirectoryResponse) {}
}

// Message sent from the client to initiate a connection.
message ConnectRequest {}

// Message sent from the server once a connection is established.
message ConnectResponse {}

// Message sent for disconnect.
message DisconnectRequest {
    // True to cause the application to exit.  If True, this should be the last
    // call to disconect for all client sessions.
    bool exit_application = 1;
}

// The result of the disconnect message.
message DisconnectResponse {}

// Message object sent for requesting the application's preferences directory
message GetPreferencesDirectoryRequest {}

// Message object returned containing the applciation's preferences directory
message GetPreferencesDirectoryResponse {
    // Gets the application's preferences directory
    string preferences_directory = 1;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/Core/Automation/Core.Automation.Protocols/Log.proto sha256=856a69b04c61959f023104052b88a21bb2abcf69bb192ebf4397ac4772a0eb12 bytes=1556 -->
## FILE: protobuf/Core/Automation/Core.Automation.Protocols/Log.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/Core/Automation/Core.Automation.Protocols/Log.proto`
- sha256: `856a69b04c61959f023104052b88a21bb2abcf69bb192ebf4397ac4772a0eb12`
- bytes: 1556

````protobuf
syntax = "proto3";

package national_instruments.core.automation.protocols;

// Service interface for a service side Log.
service Log {
    // RPC Call initiate listening to a server side Log.
    rpc Listen(ListenRequest) returns (stream ListenResponse) {}
    // RPC call to stop listening to a server side log.
    rpc StopListening(StopListeningRequest) returns (StopListeningResponse) {}
}

// The type of the listen response.
enum ResponseType {
    // A simple message was written to the log.
    message = 0;
    // A fatal error was written to the log.
    error = 1;
    // An internal error was written to the log.
    internal_error = 2;
}

// Message describing request to listen to the server side log.
message ListenRequest {
    // A bitfield indicating which types of logging events the client is interested in receiving.
    // See NationalInstruments.Core.Automation.Protocols.LoggingEvents for the constants.
    int32 DesiredLoggingEvents = 1;
}

// Response object created while listening to a server side log.
message ListenResponse {
    // The message written to the log.
    string message = 1;
    // The type of the listen response.
    ResponseType Type = 2;
    // The unique id of the log response.  Usually only set for error type messages.
    uint32 uniqueId = 3;
}

// Message sent to indicate we're done listening to the server side log.
message StopListeningRequest { }

// Response sent once we're no longer listening to the server side log.
message StopListeningResponse { }
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=protobuf/DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto sha256=e40f8af67602e00398a9b8243714ce2b1bca8274f80e2feaa8036406b2b57d65 bytes=780 -->
## FILE: protobuf/DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto

- repository: `ni/niflexlogger-automation-python`
- source_path: `protobuf/DiagramSdk/Automation/DiagramSdk.Automation.Protocols/Identifiers.proto`
- sha256: `e40f8af67602e00398a9b8243714ce2b1bca8274f80e2feaa8036406b2b57d65`
- bytes: 780

````protobuf
syntax = "proto3";

package national_instruments.diagram_sdk.automation.protocols;
option csharp_namespace = "NationalInstruments.DiagramSdk.Automation.Protocols";

// An identifier for a server side Project.
message ProjectIdentifier {
    // The automation id for a server side Project.
    string project_id = 1;
}

message ElementIdentifier {
    // The automation id for a server side Project.
    string project_id = 1;
    // The string that identifies the file in the project containing the desired element.
    string file_name = 2;
    // The string that identifies the desired element in the file.
    string element_id = 3;
    // The string that identifies a subpart of the element (such as a terminal) in the file.
    string subpart_id = 4;
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=pyproject.toml sha256=30aaf830d0e81c27d91cc48a8785e612ba93f0e7944be11888ea28c25cac8086 bytes=207 -->
## FILE: pyproject.toml

- repository: `ni/niflexlogger-automation-python`
- source_path: `pyproject.toml`
- sha256: `30aaf830d0e81c27d91cc48a8785e612ba93f0e7944be11888ea28c25cac8086`
- bytes: 207

````toml
[tool.black]
line-length=100

[build-system]
# Minimum requirements for the build system to execute.
requires = ["setuptools", "wheel", "grpcio", "grpcio-tools"]
build-backend = "setuptools.build_meta"
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=README.rst sha256=c2acf9f6508b9d0b897967fe29f5588fa5e72f91187bde2eee2f702a7ec7fbff bytes=3472 -->
## FILE: README.rst

- repository: `ni/niflexlogger-automation-python`
- source_path: `README.rst`
- sha256: `c2acf9f6508b9d0b897967fe29f5588fa5e72f91187bde2eee2f702a7ec7fbff`
- bytes: 3472

````rst
===========  ====================================================
Info         NI FlexLogger API for Python
Author       NI
===========  ====================================================

About
=====
The **niflexlogger-automation** package contains an API (Application Programming
Interface) and examples for using Python to automate `FlexLogger <https://ni.com/flexlogger>`_.
The automation API supports modifying the configuration of existing FlexLogger projects and
controlling the execution of FlexLogger tests.
The package is implemented in Python. NI created and supports this package.

Requirements
============
**niflexlogger-automation** has the following requirements:

* FlexLogger 2024 Q1+
* CPython 3.6 - 3.13. If you do not have Python installed on your computer, go to python.org/downloads to download and install it.

.. _installation_section:

Installation
============
To install **niflexlogger-automation**, use one of the following methods:

* `pip <https://pypi.python.org/pypi/pip>`_::

   $ python -m pip install niflexlogger-automation

* **easy_install** from `setuptools <https://pypi.python.org/pypi/setuptools>`_::

   $ python -m easy_install niflexlogger-automation

* Download the project source and run::

   $ python setup.py install

.. _usage_section:

Using the FlexLogger Python API
===============================
Refer to the `documentation <https://niflexlogger-automation.readthedocs.io/en/latest/getting_started.html>`_
for detailed information on how to use **niflexlogger-automation**.

Refer to `Getting Started with CompactDAQ and FlexLogger <https://learn.ni.com/learn/article/getting-started-with-compactdaq-and-flexlogger>`_, for more information on installing FlexLogger, using hardware, or downloading FlexLogger examples.

.. _tests_section:

Contribution to the FlexLogger Python API
=========================================
If you would like to contribute to this API, first validate your changes using the provided automated tests. The Python API package contains a number of automated tests which should be used to
validate API changes before submitting a pull request. If a pull request contains
new API functionality, new automated tests that exercise the new functionality
should be included with the pull request.

To run the automated tests for the Python API, you must first configure FlexLogger
to load the test plugins that the test projects use. To do this, copy
``tests/assets/pythonTests.config`` to 
``%public%\Documents\National Instruments\FlexLogger\Plugins\IOPlugins``, and in that
file replace ``<path to git repo>`` with the path to the cloned repo.

After this is done, you can run the tests with `tox <https://pypi.org/project/tox/>`_.

.. _support_section:

Support / Feedback
==================
The **niflexlogger-automation** package is supported by NI. For support for
**niflexlogger-automation**, open a request through the NI support portal at
`ni.com <https://www.ni.com>`_.

Bugs / Feature requests
=======================
To report a bug or submit a feature request, use the
`GitHub issues page <https://github.com/ni/niflexlogger-automation-python/issues>`_.

License
=======
**niflexlogger-automation** is licensed under an MIT-style license (see `LICENSE
<LICENSE>`_).  Other incorporated projects may be licensed under different
licenses. All licenses allow for non-commercial and commercial use.
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=requirements.txt sha256=630c5b0307caaa7f1ed02f11042c95c8e6d2edc238903c649e2f7a912230a82b bytes=302 -->
## FILE: requirements.txt

- repository: `ni/niflexlogger-automation-python`
- source_path: `requirements.txt`
- sha256: `630c5b0307caaa7f1ed02f11042c95c8e6d2edc238903c649e2f7a912230a82b`
- bytes: 302

````text
console-menu
grpcio-tools
grpcio
importlib
prettytable
psutil
python-dateutil
# This package only works correctly on Windows,
# but add this specifier to allow installing it on
# Linux, which is helpful for pypi builds and readthedocs.
pywin32; platform_system=="Windows"
typing-extensions
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=setup.py sha256=714561ea26c9a100c5c90100d069e15748efe5a15d0127a54d54c966541c0a63 bytes=4563 -->
## FILE: setup.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `setup.py`
- sha256: `714561ea26c9a100c5c90100d069e15748efe5a15d0127a54d54c966541c0a63`
- bytes: 4563

````python
import subprocess
import sys
from typing import List

from setuptools import find_namespace_packages, setup  # type: ignore
from setuptools.command.build_py import build_py as BuildPyCommand  # type: ignore
from setuptools.command.test import test as TestCommand  # type: ignore

pypi_name = "niflexlogger-automation"

packages = find_namespace_packages(where="src", include=["flexlogger.*"])

PROTO_PATHS = [
    "ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols",
    "Core/Automation/Core.Automation.Protocols",
    "DiagramSdk/Automation/DiagramSdk.Automation.Protocols",
]


class GenerateProtobufAndBuildPyCommand(BuildPyCommand):
    def run(self) -> None:
        _generate_protobuf_classes()
        super().run()


def _generate_protobuf_classes() -> None:
    proc = subprocess.Popen(
        [sys.executable, "generate_protobuf_classes.py"],
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (stdout_text, stderr_text) = proc.communicate()
    if proc.returncode != 0:
        print("stdout: " + stdout_text)
        print("stderr: " + stderr_text)
        raise RuntimeError("generate_protobuf_classes returned error code %d" % proc.returncode)


class PyTest(TestCommand):
    def finalize_options(self) -> None:
        TestCommand.finalize_options(self)
        self.test_args = []  # type: List[str]
        self.test_suite = True

    def run_tests(self) -> None:
        import pytest  # type: ignore

        pytest.main(self.test_args)


def _get_version(name: str) -> str:
    import os

    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, name)
    if not os.path.exists(os.path.join(script_dir, "VERSION")):
        version = "0.2.4"
    else:
        with open(os.path.join(script_dir, "VERSION"), "r") as version_file:
            version = version_file.read().rstrip()
    return version


def _read_contents(file_to_read: str) -> str:
    with open(file_to_read, "r") as f:
        return f.read()


def _build_protobuf_paths() -> List[str]:
    # The package_data member does not support recursive ** globbing,
    # so build up the paths here.
    # Note that this path is relative to the flexlogger.automation package
    # directory
    return ["../../../protobuf/" + x + "/*.proto" for x in PROTO_PATHS]


setup(
    name=pypi_name,
    version=_get_version(pypi_name),
    description="NI FlexLogger Python API",
    long_description=_read_contents("README.rst"),
    author="National Instruments",
    maintainer="Ben Parrott, Greg Stoll",
    maintainer_email="ben.parrott@ni.com, greg.stoll@ni.com",
    keywords=["niflexlogger", "flexlogger"],
    license="MIT",
    packages=packages,
    scripts=["generate_protobuf_classes.py"],
    install_requires=[
        "typing-extensions",
        "grpcio",
        "grpcio-tools",
        "psutil",
        # This package only works correctly on Windows,
        # but add this specifier to allow installing it on
        # Linux, which is helpful for pypi builds and readthedocs.
        "pywin32; platform_system=='Windows'",
        "console-menu",
        "PrettyTable",
        "python-dateutil",
    ],
    setup_requires=["grpcio", "grpcio-tools"],
    tests_require=["pytest", "mypy", "npTDMS", "pytest-timeout", "psutil"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Hardware",
    ],
    cmdclass={"test": PyTest, "build_py": GenerateProtobufAndBuildPyCommand},
    package_data={"": ["VERSION", "*.pyi", "py.typed"] + _build_protobuf_paths()},
    package_dir={"": "src"},
)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/__init__.py sha256=5d24a470ea576cdb391158b03ce14904ae95dc9f1cf9f83b407c6cfbdd3f4a2a bytes=1192 -->
## FILE: src/flexlogger/automation/__init__.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/__init__.py`
- sha256: `5d24a470ea576cdb391158b03ce14904ae95dc9f1cf9f83b407c6cfbdd3f4a2a`
- bytes: 1192

````python
# flake8: noqa
from ._application import Application
from ._project import Project
from ._test_session import TestSession
from ._test_session_state import TestSessionState
from ._channel_specification_document import ChannelSpecificationDocument
from ._logging_specification_document import LoggingSpecificationDocument
from ._log_file_type import LogFileType
from ._screen_document import ScreenDocument
from ._test_specification_document import TestSpecificationDocument
from ._flexlogger_error import FlexLoggerError
from ._channel_data_point import ChannelDataPoint
from ._test_property import TestProperty
from ._data_rate_level import DataRateLevel
from ._event_payloads import EventPayload
from ._event_payloads import AlarmPayload
from ._event_payloads import FilePayload
from . import _event_names as EventNames
from ._event_type import EventType
from ._events import FlexLoggerEventHandler
from ._severity_level import SeverityLevel
from ._start_trigger_condition import StartTriggerCondition
from ._stop_trigger_condition import StopTriggerCondition
from ._value_change_condition import ValueChangeCondition
from ._value_change_type import ValueChangeType
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_application.py sha256=e169ad92bfdd5baedc4d81d03d157d09e94d3c0e61382a4099940d5a09850552 bytes=18890 -->
## FILE: src/flexlogger/automation/_application.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_application.py`
- sha256: `e169ad92bfdd5baedc4d81d03d157d09e94d3c0e61382a4099940d5a09850552`
- bytes: 18890

````python
from google.protobuf import empty_pb2
import mmap
import os
import re
import struct
import subprocess
import sys
import time
import uuid
from datetime import timedelta
from pathlib import Path
from socket import SOCK_STREAM
from typing import Any, List, Optional, Union

# Do not import anything from win32api here (instead, import them in the
# methods they're needed in). Linux machines need to be able to import our
# module so buildthedocs will be able to use automodule correctly to generate
# our API Reference documentation.
import psutil  # type: ignore
from grpc import insecure_channel, RpcError, StatusCode

from ._events import FlexLoggerEventHandler
from ._flexlogger_error import FlexLoggerError
from ._project import Project
from .proto import (
    Application_pb2,  # type: ignore
    Application_pb2_grpc,  # type: ignore
    FlexLoggerApplication_pb2,  # type: ignore
    FlexLoggerApplication_pb2_grpc,  # type: ignore
    AutomationClientType_pb2, # type: ignore
)

_FLEXLOGGER_REGISTRY_KEY_PATH = r"SOFTWARE\National Instruments\FlexLogger"
_FLEXLOGGER_EXE_NAME = "FlexLogger.exe"
_FLEXLOGGER_PORT_FILE_PATH = Path(r"National Instruments\FlexLogger\LastAutomationPort.txt")
_APP_CLOSE_TIMEOUT = 60


class Application:
    """Represents the FlexLogger application."""

    def __init__(self, server_port: int = None) -> None:
        """Connect to an already running instance of FlexLogger.

        Args:
            server_port: The port that the automation server is listening to.  Omit this
                argument or pass None to detect the port of a running FlexLogger automatically.

        Raises:
            FlexLoggerError: if connecting fails.
        """
        Application._raise_if_unsupported_platform()
        self._server_port = server_port if server_port is not None else self._detect_server_port()
        self._connect()
        self._launched = False
        self._event_handler = None
        self._client_id = uuid.uuid4().hex

    def __enter__(self) -> "Application":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # Only exit the application if this was created with Application.launch()
        # If the user wants to override this behavior they can call close()
        # or disconnect() explicitly.
        self._disconnect(exit_application=self._launched)

    @property
    def event_handler(self) -> FlexLoggerEventHandler:
        """The application event handler."""
        if self._event_handler is not None:
            return self._event_handler

        self._event_handler = FlexLoggerEventHandler(self._channel,
                                                     self._client_id,
                                                     self,
                                                     self._raise_exception_if_closed)
        return self._event_handler

    @property
    def server_port(self) -> int:
        """The port that the automation server is listening to."""
        return self._server_port

    @classmethod
    def launch(cls, *, timeout: float = 40, path: Union[str, Path] = None) -> "Application":
        """Launch a new instance of FlexLogger.

        Note that if this method is used to initialize a "with" statement, when
        the Application goes out of scope FlexLogger will be closed.  To prevent this,
        call :meth:`~.Application.disconnect()`.

        Args:
            timeout: The length of time, in seconds, to wait for FlexLogger to launch
                before raising an exception.
                Defaults to 40.
            path: The path to the FlexLogger executable to launch.
                Defaults to None, meaning the latest installed version will be launched.

        Returns:
            The created Application object

        Raises:
            FlexLoggerError: if launching FlexLogger or connecting to it fails.
        """
        Application._raise_if_unsupported_platform()
        if isinstance(path, str):
            path = Path(path)
        server_port = Application._launch_flexlogger(timeout_in_seconds=timeout, path=path)
        application = Application(server_port=server_port)
        application._launched = True
        return application

    def close(self) -> None:
        """Close the application and disconnect from the automation server.

        Further calls to this object will fail.
        """
        self._disconnect(exit_application=True)

    def disconnect(self) -> None:
        """Disconnect from the automation server, but leave the application running.

        Further calls to this object will fail.
        """
        self._disconnect(exit_application=False)

    @classmethod
    def _raise_if_unsupported_platform(cls) -> None:
        if sys.maxsize != 2 ** 63 - 1:
            raise FlexLoggerError("This API only supports 64-bit versions of Python.")

    def _connect(self) -> None:
        if self._server_port <= 0:
            raise ValueError("Tried to connect to invalid port number %d" % self._server_port)
        try:
            self._channel = insecure_channel("localhost:%d" % self._server_port)
            try:
                stub = FlexLoggerApplication_pb2_grpc.FlexLoggerApplicationStub(self._channel)
                stub.Initialize(FlexLoggerApplication_pb2.InitializeRequest(client_type=AutomationClientType_pb2.CLIENT_TYPE_PYTHON))
            except RpcError as error:
                # Ignore UNIMPLEMENTED exceptions. Older FLexLogger does not support the Initialize message.
                if error.code() != StatusCode.UNIMPLEMENTED:
                    raise
        except RpcError as error:
            raise FlexLoggerError(
                'Failed to connect to FlexLogger. Ensure the "Automation server" preference is '
                "enabled in the application. "
            ) from error

    def _disconnect(self, exit_application: bool) -> None:
        if self._channel is not None:
            stub = Application_pb2_grpc.ApplicationStub(self._channel)
            pid_to_wait_for = None
            if exit_application:
                # Find the application that's using this port
                pid_candidates = set(
                    x.pid
                    for x in psutil.net_connections()
                    if x.type == SOCK_STREAM
                    and x.laddr[1] == self._server_port
                    and x.pid != os.getpid()
                )
                for pid in pid_candidates:
                    if psutil.Process(pid).name().lower() == _FLEXLOGGER_EXE_NAME.lower():
                        pid_to_wait_for = pid
                        break
            try:
                if exit_application:
                    # If there is an active project, close it so closing the
                    # app won't prompt to save it.
                    active_project = self.get_active_project()
                    if active_project is not None:
                        active_project.close()
                stub.Disconnect(
                    Application_pb2.DisconnectRequest(exit_application=exit_application)
                )
                if pid_to_wait_for is not None:
                    # Wait 60 seconds for the process to exit
                    timeout_end_time = time.time() + _APP_CLOSE_TIMEOUT
                    process_still_running = True
                    while time.time() < timeout_end_time and process_still_running:
                        # Only wait for 200 ms at a time so we can still be responsive to Ctrl-C
                        time.sleep(0.2)
                        try:
                            # This will raise an exception if the process doesn't exist.
                            # But it's also possible the PID has been reused, so see if
                            # the name is the same.
                            process_still_running = (
                                psutil.Process(pid_to_wait_for).name().lower()
                                == _FLEXLOGGER_EXE_NAME.lower()
                            )
                        except psutil.Error:
                            process_still_running = False
            except (RpcError, ValueError, AttributeError) as rpc_error:
                self._raise_exception_if_closed()
                raise FlexLoggerError("Failed to disconnect") from rpc_error
            finally:
                self._channel.close()
                self._channel = None
                self._event_handler = None

    def _raise_exception_if_closed(self) -> None:
        if self._channel is None:
            raise FlexLoggerError("Application has already been disconnected") from None

    def open_project(self, path: Union[str, Path], timeout: int = -1) -> Project:
        """Open a project.

        Args:
            path: The path to the project you want to open.
            timeout: The timeout in seconds.
                     If the value is negative, it will be ignored and the call will wait indefinitely.

        Returns:
            The opened project.

        Raises:
            FlexLoggerError: if opening the project fails or the timeout is reached.
        """
        try:
            stub = FlexLoggerApplication_pb2_grpc.FlexLoggerApplicationStub(self._channel)
            if timeout < 0:
                response = stub.OpenProject(
                    FlexLoggerApplication_pb2.OpenProjectRequest(project_path=str(path)))
            else:
                response = stub.OpenProject(
                    FlexLoggerApplication_pb2.OpenProjectRequest(project_path=str(path)), timeout=timeout)

            # FlexLogger can hang if you open and then immediately close a project,
            # this seems sufficient to prevent that.
            time.sleep(1.0)
            return Project(self._channel, self._raise_exception_if_closed, response.project)
        # For most methods, catching ValueError is sufficient to detect whether the Application
        # has been closed, and avoids race conditions where another thread closes the Application
        # in the middle of the first thread's call.
        #
        # This method passes self._channel directly to a stub, and this raises an AttributeError
        # if self._channel is None, so catch this as well.
        except (RpcError, ValueError, AttributeError) as rpc_error:
            self._raise_exception_if_closed()
            raise FlexLoggerError("Failed to open project") from rpc_error

    def get_active_project(self) -> Optional[Project]:
        """Gets the currently active (open) project.

        Returns:
            The active project, or None if a project is not currently open.

        Raises:
            FlexLoggerError: if getting the active project fails.
        """
        try:
            stub = FlexLoggerApplication_pb2_grpc.FlexLoggerApplicationStub(self._channel)
            response = stub.GetActiveProject(FlexLoggerApplication_pb2.GetActiveProjectRequest())
            if response.active_project_available:
                return Project(self._channel, self._raise_exception_if_closed, response.project)
            else:
                return None
        # For most methods, catching ValueError is sufficient to detect whether the Application
        # has been closed, and avoids race conditions where another thread closes the Application
        # in the middle of the first thread's call.
        #
        # This method passes self._channel directly to a stub, and this raises an AttributeError
        # if self._channel is None, so catch this as well.
        except (RpcError, ValueError, AttributeError) as rpc_error:
            self._raise_exception_if_closed()
            raise FlexLoggerError("Failed to get the active project") from rpc_error

    def get_version(self) -> (str, str):
        """Gets the FlexLogger server version.

        Returns:
            A tuple containing the FlexLogger versions (internal version and user visible version).

        Raises:
            FlexLoggerError: if getting the version fails.
        """
        try:
            stub = FlexLoggerApplication_pb2_grpc.FlexLoggerApplicationStub(self._channel)
            response = stub.GetVersion(empty_pb2.Empty())
            return response.version, response.version_string
        # For most methods, catching ValueError is sufficient to detect whether the Application
        # has been closed, and avoids race conditions where another thread closes the Application
        # in the middle of the first thread's call.
        #
        # This method passes self._channel directly to a stub, and this raises an AttributeError
        # if self._channel is None, so catch this as well.
        except (RpcError, ValueError, AttributeError) as rpc_error:
            self._raise_exception_if_closed()
            raise FlexLoggerError("Failed to get version") from rpc_error

    @classmethod
    def _launch_flexlogger(cls, timeout_in_seconds: float, path: Optional[Path] = None) -> int:
        import win32api  # type: ignore
        import win32event  # type: ignore

        if path is not None and not path.name.lower().endswith(".exe"):
            path = path / _FLEXLOGGER_EXE_NAME
        if path is None:
            path = cls._get_latest_installed_flexlogger_path()
        if path is None:
            raise RuntimeError("Could not determine latest installed path of FlexLogger")
        event_name = uuid.uuid4().hex
        mapped_name = uuid.uuid4().hex

        event = win32event.CreateEvent(None, 0, 0, event_name)
        args = [str(path)]
        args += [
            "-mappedFileIsReadyEventName=" + event_name,
            "-mappedFileName=" + mapped_name,
        ]
        args += ["-enableAutomationServer"]

        try:
            subprocess.Popen(args)
            timeout_end_time = time.time() + timeout_in_seconds
            while True:
                # Only wait for 200 ms at a time so we can still be responsive to Ctrl-C
                object_signaled = win32event.WaitForSingleObject(event, 200)
                if object_signaled == 0:
                    return cls._read_int_from_mmap(mapped_name)
                elif object_signaled != win32event.WAIT_TIMEOUT:
                    raise RuntimeError(
                        "Internal error waiting for FlexLogger to launch. Error code %d"
                        % object_signaled
                    )
                if time.time() >= timeout_end_time:
                    raise RuntimeError(
                        "Timed out waiting for FlexLogger to launch.  This might mean an "
                        "instance of FlexLogger was already running."
                    )
        finally:
            win32api.CloseHandle(event)

    @classmethod
    def _get_server_port_file_path(cls) -> Path:
        from win32com.shell import shell, shellcon  # type: ignore

        program_data_path = Path(shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_APPDATA, 0, 0))
        return program_data_path / _FLEXLOGGER_PORT_FILE_PATH

    def _detect_server_port(self) -> int:
        """Detect the server_port of a running FlexLogger."""
        port_file_path = Application._get_server_port_file_path()
        if not port_file_path.exists():
            raise RuntimeError(
                "No running FlexLogger detected.  If FlexLogger is running, this might mean the "
                "automation server is not enabled.  To turn on the automation server, see the "
                "General tab of the Preferences in FlexLogger."
            )
        try:
            with open(str(port_file_path), "r") as f:
                text = f.read().strip()
                return int(text)
        except Exception as ex:
            raise RuntimeError("Failed to read automation port from running FlexLogger.") from ex

    @classmethod
    def _get_latest_installed_flexlogger_path(cls) -> Optional[Path]:
        import winreg  # type: ignore

        try:
            with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE, _FLEXLOGGER_REGISTRY_KEY_PATH
            ) as flexLoggerKey:
                number_of_subkeys = winreg.QueryInfoKey(flexLoggerKey)[0]
                subkey_names = [winreg.EnumKey(flexLoggerKey, i) for i in range(number_of_subkeys)]
                # Try the newer "CurrentVerison" subkey first,
                # then the older version specific subkeys
                subkey = cls._get_current_version_subkey_name(subkey_names)
                if subkey is None:
                    subkey = cls._get_latest_subkey_name(subkey_names)
                    if subkey is None:
                        return None
                with winreg.OpenKey(flexLoggerKey, subkey) as latest_flexLogger_key:
                    return (
                        Path(winreg.QueryValueEx(latest_flexLogger_key, "Path")[0])
                        / _FLEXLOGGER_EXE_NAME
                    )
        except EnvironmentError:
            return None

    @classmethod
    def _get_current_version_subkey_name(cls, names: List[str]) -> Optional[str]:
        if "CurrentVersion" in names:
            return "CurrentVersion"
        else:
            return None

    @classmethod
    def _get_latest_subkey_name(cls, names: List[str]) -> Optional[str]:
        """Get the latest version name from the registry key names.

        >>> Application._get_latest_subkey_name(["1.1", "2.0", "7", "foo"])
        '2.0'
        >>> Application._get_latest_subkey_name(["2.100", "2.9", "2.10", "2.1"])
        '2.100'
        >>> Application._get_latest_subkey_name(["9.2", "10.1", "10.0"])
        '10.1'
        >>> Application._get_latest_subkey_name([]) is None
        True
        >>> Application._get_latest_subkey_name(["not real"]) is None
        True
        """
        major_minor_re = re.compile(r"^(\d+)\.(\d+)")
        matches = [major_minor_re.match(name) for name in names]
        sorted_names = sorted(
            (int(match.group(1)), int(match.group(2)), match.group(0))
            for match in matches
            if match is not None
        )
        if len(sorted_names) == 0:
            return None
        return sorted_names[-1][2]

    @classmethod
    def _read_int_from_mmap(cls, mapped_name: str) -> int:
        with mmap.mmap(-1, 4, tagname=mapped_name, access=mmap.ACCESS_READ) as mapped_file:
            int_bytes = mapped_file.read(4)
            return struct.unpack("i", int_bytes)[0]
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_channel_data_point.py sha256=0454d88907cecb27354beb1d9dd83041942295aeaf5b9e53592e746630f6a7a0 bytes=866 -->
## FILE: src/flexlogger/automation/_channel_data_point.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_channel_data_point.py`
- sha256: `0454d88907cecb27354beb1d9dd83041942295aeaf5b9e53592e746630f6a7a0`
- bytes: 866

````python
from datetime import datetime


class ChannelDataPoint:
    """The value for a channel at the specified timestamp."""

    def __init__(self, name: str, value: float, timestamp: datetime):
        self._name = name
        self._value = value
        self._timestamp = timestamp

    def __repr__(self) -> str:
        return 'flexlogger.automation.ChannelDataPoint("%s", %f, %s)' % (
            self._name,
            self._value,
            repr(self._timestamp),
        )

    @property
    def name(self) -> str:
        """The name of the channel."""
        return self._name

    @property
    def value(self) -> float:
        """The value of the channel."""
        return self._value

    @property
    def timestamp(self) -> datetime:
        """The timestamp when the value occurred."""
        return self._timestamp
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_channel_specification_document.py sha256=f7f4b5e4c1ce98ec1386708b13ea73e9c67ab0c22a76ed2019ed9f4ff975e295 bytes=13744 -->
## FILE: src/flexlogger/automation/_channel_specification_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_channel_specification_document.py`
- sha256: `f7f4b5e4c1ce98ec1386708b13ea73e9c67ab0c22a76ed2019ed9f4ff975e295`
- bytes: 13744

````python
from datetime import timezone
from typing import Callable, List

from grpc import Channel, RpcError

from ._channel_data_point import ChannelDataPoint
from ._data_rate_level import DataRateLevel
from ._flexlogger_error import FlexLoggerError
from .proto import (
    ChannelSpecificationDocument_pb2,
    ChannelSpecificationDocument_pb2_grpc,
)
from .proto.Identifiers_pb2 import ElementIdentifier
from .proto.DataRateLevel_pb2 import DataRateLevel as DataRateLevel_pb2

DATA_RATE_LEVEL_MAP = {
    DataRateLevel.SLOW: DataRateLevel_pb2.DATA_RATE_LEVEL_SLOW,
    DataRateLevel.MEDIUM: DataRateLevel_pb2.DATA_RATE_LEVEL_MEDIUM,
    DataRateLevel.FAST: DataRateLevel_pb2.DATA_RATE_LEVEL_FAST,
    DataRateLevel.COUNTER: DataRateLevel_pb2.DATA_RATE_LEVEL_COUNTER,
    DataRateLevel.DIGITAL: DataRateLevel_pb2.DATA_RATE_LEVEL_DIGITAL,
    DataRateLevel.ON_DEMAND: DataRateLevel_pb2.DATA_RATE_LEVEL_ON_DEMAND,
}

DATA_RATE_LEVEL_PB2_MAP = {
    DataRateLevel_pb2.DATA_RATE_LEVEL_SLOW: DataRateLevel.SLOW,
    DataRateLevel_pb2.DATA_RATE_LEVEL_MEDIUM: DataRateLevel.MEDIUM,
    DataRateLevel_pb2.DATA_RATE_LEVEL_FAST: DataRateLevel.FAST,
    DataRateLevel_pb2.DATA_RATE_LEVEL_COUNTER: DataRateLevel.COUNTER,
    DataRateLevel_pb2.DATA_RATE_LEVEL_DIGITAL: DataRateLevel.DIGITAL,
    DataRateLevel_pb2.DATA_RATE_LEVEL_ON_DEMAND: DataRateLevel.ON_DEMAND,
}


class ChannelSpecificationDocument:
    """Represents the document that describes data channels.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_channel_specification_document`.
    """

    def __init__(
        self,
        channel: Channel,
        raise_if_application_closed: Callable[[], None],
        identifier: ElementIdentifier,
    ) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed
        self._identifier = identifier

    def get_actual_data_rate(self, channel_name: str) -> float:
        """Get the actual data rate for the specified channel.

        Args:
            channel_name: The name of the channel.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetActualDataRate(
                ChannelSpecificationDocument_pb2.GetActualDataRateRequest(
                    document_identifier=self._identifier,  channel_name=channel_name
                )
            )

            return response.data_rate
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the actual data rate.") from error

    def get_channel_names(self) -> List[str]:
        """Get all the channel names in the document.

        Raises:
            FlexLoggerError: if getting the channel names fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetChannelNames(
                ChannelSpecificationDocument_pb2.GetChannelNamesRequest(
                    document_identifier=self._identifier
                )
            )
            return response.channel_names
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get channel names") from error

    def get_channel_value(self, channel_name: str) -> ChannelDataPoint:
        """Get the current value of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetDoubleChannelValue(
                ChannelSpecificationDocument_pb2.GetDoubleChannelValueRequest(
                    document_identifier=self._identifier, channel_name=channel_name
                )
            )
            # Timestamps come back from FlexLogger in UTC
            return ChannelDataPoint(
                channel_name,
                response.channel_value,
                response.value_timestamp.ToDatetime().replace(tzinfo=timezone.utc),
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get channel value") from error

    def get_data_rate(self, data_rate_level: DataRateLevel) -> float:
        """Get the data rate for a specific date rate level in Hertz.

        Args:
            data_rate_level: The data rate level to get the data rate for.

        Raises:
            FlexLoggerError: if the data_rate_level is invalid.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            data_rate_level_parameter = DATA_RATE_LEVEL_MAP.get(data_rate_level)
            response = stub.GetDataRate(
                ChannelSpecificationDocument_pb2.GetDataRateRequest(
                    document_identifier=self._identifier, data_rate_level=data_rate_level_parameter
                )
            )

            return response.data_rate
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the data rate: data rate level invalid.") from error

    def get_data_rate_level(self, channel_name: str) -> DataRateLevel:
        """Get the data rate level of the specified channel

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the data rate level fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetDataRateLevel(
                ChannelSpecificationDocument_pb2.GetDataRateLevelRequest(
                    document_identifier=self._identifier, channel_name=channel_name
                )
            )

            return DATA_RATE_LEVEL_PB2_MAP.get(response.data_rate_level)
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the data rate level.") from error

    def is_channel_enabled(self, channel_name: str) -> bool:
        """Get the current enabled state of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.IsChannelEnabled(
                ChannelSpecificationDocument_pb2.IsChannelEnabledRequest(
                    document_identifier=self._identifier, channel_name=channel_name
                )
            )

            return response.channel_enabled
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get channel enable state") from error

    def set_channel_enabled(self, channel_name: str, channel_enabled: bool) -> None:
        """Enable or disable the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_enabled: The channel enabled state: true to enable the channel, false to disable it.

        Raises:
            FlexLoggerError: if enabling or disabling the channel fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            stub.SetChannelEnabled(
                ChannelSpecificationDocument_pb2.SetChannelEnabledRequest(
                    document_identifier=self._identifier,
                    channel_name=channel_name,
                    channel_enabled=channel_enabled,
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the channel enable state") from error

    def is_channel_logging_enabled(self, channel_name: str) -> bool:
        """Get the current logging state of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            response = stub.IsChannelLoggingEnabled(
                ChannelSpecificationDocument_pb2.IsChannelLoggingEnabledRequest(
                    document_identifier=self._identifier, channel_name=channel_name
                )
            )

            return response.channel_logging_enabled
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get channel logging enable state") from error

    def set_channel_logging_enabled(self, channel_name: str, channel_logging_enabled: bool) -> None:
        """Enable or disable logging for the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_logging_enabled: The channel logging enabled state: true to enable logging, false to disable it.

        Raises:
            FlexLoggerError: if enabling or disabling the channel logging fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            stub.SetChannelLoggingEnabled(
                ChannelSpecificationDocument_pb2.SetChannelLoggingEnabledRequest(
                    document_identifier=self._identifier,
                    channel_name=channel_name,
                    channel_logging_enabled=channel_logging_enabled,
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the channel logging state") from error

    def set_channel_value(self, channel_name: str, channel_value: float) -> None:
        """Set the current value of the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_value: The value to set the channel to.

        Raises:
            FlexLoggerError: if setting the channel value fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            stub.SetDoubleChannelValue(
                ChannelSpecificationDocument_pb2.SetDoubleChannelValueRequest(
                    document_identifier=self._identifier,
                    channel_name=channel_name,
                    channel_value=channel_value,
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set channel value") from error

    def set_data_rate(self, data_rate_level: DataRateLevel, data_rate: float) -> None:
        """Set the data rate of a specific data rate level.

        Args:
            data_rate_level: The data rate level to get the data rate for.
            data_rate: The value of the data rate to set in Hertz.

        Raises:
            FlexLoggerError: if setting the data rate fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            data_rate_level_parameter = DATA_RATE_LEVEL_MAP.get(data_rate_level)
            stub.SetDataRate(
                ChannelSpecificationDocument_pb2.SetDataRateRequest(
                    document_identifier=self._identifier,
                    data_rate_level=data_rate_level_parameter,
                    data_rate=data_rate
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the data rate") from error

    def set_data_rate_level(self, channel_name: str, data_rate_level: DataRateLevel) -> None:
        """Set the data rate level of the specified channel
           Note: This may affect other channels in the same module or chassis set to the same data rate level.

        Args:
            channel_name: The name of the channel.
            data_rate_level: The data rate level to set.

        Raises:
            FlexLoggerError: if setting the data rate level fails.
        """
        stub = ChannelSpecificationDocument_pb2_grpc.ChannelSpecificationDocumentStub(self._channel)
        try:
            data_rate_level_parameter = DATA_RATE_LEVEL_MAP.get(data_rate_level)
            stub.SetDataRateLevel(
                ChannelSpecificationDocument_pb2.SetDataRateLevelRequest(
                    document_identifier=self._identifier,
                    channel_name=channel_name,
                    data_rate_level=data_rate_level_parameter
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the data rate level.") from error
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_data_rate_level.py sha256=1cdebabac2b65d2182eed6d604e63eeb026f38a625b77893278061c7f9752aa0 bytes=972 -->
## FILE: src/flexlogger/automation/_data_rate_level.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_data_rate_level.py`
- sha256: `1cdebabac2b65d2182eed6d604e63eeb026f38a625b77893278061c7f9752aa0`
- bytes: 972

````python
from enum import Enum


class DataRateLevel(Enum):
    """An enumeration describing the possible data rate levels that channels can be configured to use.
    For additional information on configuring data rates, visit
    https://www.ni.com/docs/en-US/bundle/flexlogger/page/configuring-data-rates.html
    """

    SLOW = 1
    """The slow analog data rate level in Hertz at which your DAQ device acquires data."""

    MEDIUM = 2
    """The medium analog data rate level in Hertz at which your DAQ device acquires data."""

    FAST = 3
    """The fast analog data rate level in Hertz at which your DAQ device acquires data."""

    COUNTER = 4
    """The counter data rate level in Hertz at which your DAQ device acquires data."""

    DIGITAL = 6
    """The digital data rate level in Hertz at which your DAQ device acquires data."""

    ON_DEMAND = 7
    """The on-demand data rate level in Hertz at which your DAQ device acquires data."""
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_names.py sha256=599b9319f91aba5d5a2b774aade96dcc475ef45e58274d8c73a9cd348cff89cc bytes=394 -->
## FILE: src/flexlogger/automation/_event_names.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_event_names.py`
- sha256: `599b9319f91aba5d5a2b774aade96dcc475ef45e58274d8c73a9cd348cff89cc`
- bytes: 394

````python
"""List of event names."""

ALARM_ADDED = "Active Alarm Added"
ALARM_REMOVED = "Active Alarm Removed"
ALARM_CHANGED = "Active Alarm Changed"
ALARM_CLEARED = "Alarm Cleared and Acknowledged"
LOG_FILE_CREATED = "Log File Created"
LOG_FILE_CLOSED = "Log File Closed"
TEST_STARTED = "Test Started"
TEST_PAUSED = "Test Paused"
TEST_RESUMED = "Test Resumed"
TEST_STOPPED = "Test Stopped"
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_payloads.py sha256=d063aaed9a1eea8ca6258b1dc1eb93585305d906e7a6e598d631c4431deef9e1 bytes=3630 -->
## FILE: src/flexlogger/automation/_event_payloads.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_event_payloads.py`
- sha256: `d063aaed9a1eea8ca6258b1dc1eb93585305d906e7a6e598d631c4431deef9e1`
- bytes: 3630

````python
from ._event_type import EventType
from ._severity_level import SeverityLevel
from .proto import Events_pb2
from datetime import datetime
import json


class EventPayload:
    """Represents an event payload."""

    def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None:
        self._event_type = EventType.from_event_type_pb2(event_response.event_type)
        self._event_name = event_response.event_name
        self._payload = event_response.payload
        self._timestamp = event_response.timestamp

    @property
    def event_type(self) -> EventType:
        """The type of event received."""
        return self._event_type

    @property
    def event_name(self) -> str:
        """The name of the event received."""
        return self._event_name

    @property
    def timestamp(self) -> datetime:
        """The time the event was received."""
        return self._timestamp


class AlarmPayload(EventPayload):
    """Represents an alarm event payload."""

    def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None:
        super().__init__(event_response)
        json_payload = json.loads(self._payload)
        self._alarm_id = json_payload['AlarmId']
        self._active = json_payload['Active']
        self._acknowledged = json_payload['Acknowledged']
        self._acknowledged_at = json_payload['AcknowledgedAt']
        self._occurred_at = json_payload['OccurredAt']
        self._severity_level = json_payload['SeverityLevel']
        self._updated_at = json_payload['UpdatedAt']
        self._channel = json_payload['Channel']
        self._condition = json_payload['Condition']
        self._display_name = json_payload['DisplayName']
        self._description = json_payload['Description']

    @property
    def alarm_id(self) -> str:
        """The alarm ID."""
        return self._alarm_id

    @property
    def active(self) -> bool:
        """Whether the alarm is active."""
        return self._active

    @property
    def acknowledged(self) -> bool:
        """Whether the alarm has been acknowledged."""
        return self._acknowledged

    @property
    def acknowledged_at(self) -> datetime:
        """When the alarm was acknowledged."""
        return self._acknowledged_at

    @property
    def occurred_at(self) -> datetime:
        """When the alarm occurred."""
        return self._occurred_at

    @property
    def severity_level(self) -> SeverityLevel:
        """The alarm's severity level."""
        return self._severity_level

    @property
    def updated_at(self) -> datetime:
        """When the alarm was last updated."""
        return self._updated_at

    @property
    def channel(self) -> str:
        """Channel associated with the alarm."""
        return self._channel

    @property
    def condition(self) -> str:
        """The alarm condition."""
        return self._condition

    @property
    def display_name(self) -> str:
        """The alarm's display name."""
        return self._display_name

    @property
    def description(self) -> str:
        """Description of the alarm."""
        return self._description


class FilePayload(EventPayload):
    """Represents a file event payload."""

    def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None:
        super().__init__(event_response)
        self._file_path = self._payload

    @property
    def file_path(self) -> str:
        """The TDMS file path."""
        return self._file_path
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_type.py sha256=cf6f50e59756d865d07f8a01b4555b87262ab447c3d690f3233435dc8a38d8e1 bytes=945 -->
## FILE: src/flexlogger/automation/_event_type.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_event_type.py`
- sha256: `cf6f50e59756d865d07f8a01b4555b87262ab447c3d690f3233435dc8a38d8e1`
- bytes: 945

````python
from .proto.EventType_pb2 import EventType as EventType_pb2
from enum import Enum


class EventType(Enum):
    """An enumeration describing the different types of events."""

    ALARM = 1
    LOG_FILE = 2
    TEST_SESSION = 3
    CUSTOM = 4

    def to_event_type_pb2(self) -> EventType_pb2:
        return EVENT_TYPE_MAP.get(self.value)

    @staticmethod
    def from_event_type_pb2(event_type: EventType_pb2):
        return EVENT_TYPE_PB2_MAP.get(event_type)


EVENT_TYPE_MAP = {
    1: EventType_pb2.EVENT_TYPE_ALARM,
    2: EventType_pb2.EVENT_TYPE_LOG_FILE,
    3: EventType_pb2.EVENT_TYPE_TEST_SESSION,
    4: EventType_pb2.EVENT_TYPE_CUSTOM
}

EVENT_TYPE_PB2_MAP = {
    EventType_pb2.EVENT_TYPE_ALARM: EventType.ALARM,
    EventType_pb2.EVENT_TYPE_LOG_FILE: EventType.LOG_FILE,
    EventType_pb2.EVENT_TYPE_TEST_SESSION: EventType.TEST_SESSION,
    EventType_pb2.EVENT_TYPE_CUSTOM: EventType.CUSTOM
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_events.py sha256=5227cfce6cb72eca43a4ec823d9151b6ae042c20b9687367c7e7bb65223a928d bytes=7012 -->
## FILE: src/flexlogger/automation/_events.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_events.py`
- sha256: `5227cfce6cb72eca43a4ec823d9151b6ae042c20b9687367c7e7bb65223a928d`
- bytes: 7012

````python
import time

from ._event_payloads import AlarmPayload
from ._event_payloads import EventPayload
from ._event_payloads import FilePayload
from ._event_type import EventType
from ._flexlogger_error import FlexLoggerError
from .proto import (
    Events_pb2,
    Events_pb2_grpc,
)
from .proto.EventType_pb2 import EventType as EventType_pb2
from concurrent.futures import ThreadPoolExecutor
from google.protobuf.timestamp_pb2 import Timestamp
from grpc import Channel, RpcError
from typing import Callable, Iterator, List


class FlexLoggerEventHandler:
    """Represents a FlexLogger event handler.
    You must create a FlexLoggerEventHandler object to be able to register for events.
    """

    def __init__(self, channel: Channel,
                 client_id: str,
                 application,
                 raise_if_application_closed: Callable[[], None]) -> None:
        self._application = application
        self._callbacks = []
        self._channel = channel
        self._client_id = client_id
        self._event_types_per_callback = []
        self._is_subscribed = False
        self._raise_if_application_closed = raise_if_application_closed
        self._stub = Events_pb2_grpc.FlexLoggerEventsStub(self._channel)
        self._thread_executor = ThreadPoolExecutor()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.unregister_from_events()

    def get_registered_events(self) -> List[EventType]:
        """Gets the list of registered event types.

        Returns
            The list of registered event types

        Raises:
            FlexLoggerError: if the request failed.
        """
        try:
            response = self._stub.GetRegisteredEvents(Events_pb2.GetRegisteredEventsRequest(client_id=self._client_id))
            event_types_pb2 = response.event_types
            event_types = self._marshal_event_types_pb2(event_types_pb2)
            return event_types
        except (RpcError, ValueError, AttributeError) as rpc_error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the registered events") from rpc_error

    def unregister_from_events(self) -> None:
        """Unregister from events."""
        try:
            self._callbacks = []
            self._event_types_per_callback = []
            self._is_subscribed = False
            self._stub.UnsubscribeFromEvents(Events_pb2.UnsubscribeFromEventsRequest(client_id=self._client_id))
        except (RpcError, ValueError, AttributeError) as rpc_error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to unregister from events") from rpc_error

    def register_event_callback(self, callback, event_types=None) -> None:
        """Register for events and specify a callback method

        Args:
            callback: callback method. The callback method must have the following parameters:
                      application: Application      Reference to the FlexLogger application
                      event_type: EventType         The event type
                      event_payload: EventPayload   The event payload
            event_types: List of EventType to subscribe to.

        Raises:
            FlexLoggerError: if the callback registration failed.
        """
        event_types_parameter = self._marshal_event_types(event_types)
        if self._is_subscribed:
            try:
                self._stub.RegisterEvents(Events_pb2.SubscribeToEventsRequest(client_id=self._client_id,
                                                                              event_types=event_types_parameter))
                self._add_callback_and_events_to_dictionary(callback, event_types)
            except (RpcError, ValueError, AttributeError) as rpc_error:
                self._raise_if_application_closed()
                raise FlexLoggerError("Failed to register events") from rpc_error
            return

        # Add function and event types to respective lists
        self._is_subscribed = True
        self._add_callback_and_events_to_dictionary(callback, event_types)
        event_iterator = self._stub.SubscribeToEvents(
            Events_pb2.SubscribeToEventsRequest(client_id=self._client_id, event_types=event_types_parameter))
        self._thread_executor.submit(self._event_handler, event_iterator)
        # Wait for the server to register the client ID.
        time.sleep(0.15)

    @staticmethod
    def _marshal_event_types(event_types):
        if event_types is None:
            return None
        event_types_pb2 = []
        for event_type in event_types:
            event_types_pb2.append(event_type.to_event_type_pb2())

        return event_types_pb2

    @staticmethod
    def _marshal_event_types_pb2(event_types_pb2):
        if event_types_pb2 is None:
            return None
        event_types = []
        for event_type_pb2 in event_types_pb2:
            event_types.append(EventType.from_event_type_pb2(event_type_pb2))

        return event_types

    def _add_callback_and_events_to_dictionary(self, callback, event_types: [EventType]):
        # If the event type is not provided, respond to all.
        if event_types is None:
            event_types = [EventType.ALARM, EventType.LOG_FILE, EventType.TEST_SESSION, EventType.CUSTOM]

        if callback in self._callbacks:
            index = self._callbacks.index(callback)
            self._event_types_per_callback[index] = event_types
        else:
            self._callbacks.append(callback)
            self._event_types_per_callback.append(event_types)

    def _event_handler(self, event_iterator: Iterator[Events_pb2.SubscribeToEventsResponse]) -> None:
        try:
            while self._is_subscribed:
                event_response = next(event_iterator)
                if event_response is not None:
                    event_type = EventType.from_event_type_pb2(event_response.event_type)
                    for i in range(len(self._callbacks)):
                        if event_type in self._event_types_per_callback[i]:
                            payload = self._create_payload(event_response)
                            self._callbacks[i](self._application, event_type, payload)
        except Exception as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to receive event.") from error

    @staticmethod
    def _create_payload(event_response: Events_pb2.SubscribeToEventsResponse):
        if event_response.event_type == EventType_pb2.EVENT_TYPE_ALARM:
            payload = AlarmPayload(event_response)
        elif event_response.event_type == EventType_pb2.EVENT_TYPE_LOG_FILE:
            payload = FilePayload(event_response)
        else:
            payload = EventPayload(event_response)

        return payload
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_flexlogger_error.py sha256=1f2058b14989fd11c7c1eb52737e3c98b64229c96c40bb37e1f8b346b908de46 bytes=1470 -->
## FILE: src/flexlogger/automation/_flexlogger_error.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_flexlogger_error.py`
- sha256: `1f2058b14989fd11c7c1eb52737e3c98b64229c96c40bb37e1f8b346b908de46`
- bytes: 1470

````python
import re
from typing import cast

from grpc import RpcError


class FlexLoggerError(Exception):
    """Represents errors that occur when calling FlexLogger APIs."""

    def __init__(self, message: str) -> None:
        """Initialize an exception.

        Args:
            message: The message describing the error.
        """
        super().__init__(message)
        self._message = message

    @property
    def message(self) -> str:
        """The error message."""
        inner_details = self._get_inner_details()
        if len(inner_details) == 0:
            return self._message

        inner_details = re.sub(r"\[([0-9+-]+)\] ", "", inner_details)
        return self._message + ". Additional error details: " + inner_details

    @property
    def error_code(self) -> int:
        """The error code."""
        inner_details = self._get_inner_details()
        if len(inner_details) == 0:
            return 0

        error_code_result = re.search(r"\[([0-9+-]+)\] ", inner_details)
        return int(error_code_result.group(1)) if error_code_result else 0

    def __repr__(self) -> str:
        return f"FlexLoggerError({repr(self.message)})"

    def __str__(self) -> str:
        return self.message

    def _get_inner_details(self) -> str:
        if not isinstance(self.__cause__, RpcError):
            return ""

        cause = cast(RpcError, self.__cause__)
        return cause.details()
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_log_file_type.py sha256=2b69e99c4966c19021db92a09cbe51ea873936f4ba3809dd46cd95db8aa71316 bytes=248 -->
## FILE: src/flexlogger/automation/_log_file_type.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_log_file_type.py`
- sha256: `2b69e99c4966c19021db92a09cbe51ea873936f4ba3809dd46cd95db8aa71316`
- bytes: 248

````python
from enum import Enum

class LogFileType(Enum):
    """An enumeration describing the different log file types."""

    TDMS = 0
    """TDMS files"""

    TDMS_BACKUP_FILES = 1
    """TDMS backup files"""

    CSV = 2
    """CSV files"""
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_logging_specification_document.py sha256=2af2f82bba788039a28f7fae70127835836f071368461712f9d35405f690a942 bytes=34139 -->
## FILE: src/flexlogger/automation/_logging_specification_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_logging_specification_document.py`
- sha256: `2af2f82bba788039a28f7fae70127835836f071368461712f9d35405f690a942`
- bytes: 34139

````python
from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from datetime import timezone
from dateutil import parser
from dateutil import tz
from grpc import Channel, RpcError
from typing import Callable, List

from ._flexlogger_error import FlexLoggerError
from ._start_trigger_condition import StartTriggerCondition
from ._stop_trigger_condition import StopTriggerCondition
from ._test_property import TestProperty
from ._log_file_type import LogFileType
from ._value_change_condition import ValueChangeCondition
from .proto import LoggingSpecificationDocument_pb2, LoggingSpecificationDocument_pb2_grpc
from .proto.Identifiers_pb2 import ElementIdentifier

from .proto.LoggingSpecificationDocument_pb2 import LogFileType as LogFileType_pb2

LOG_FILE_TYPE_MAP = {
    LogFileType.TDMS: LogFileType_pb2.TDMS,
    LogFileType.CSV: LogFileType_pb2.CSV,
    LogFileType.TDMS_BACKUP_FILES: LogFileType_pb2.TDMS_BACKUP,
}


def _parse_time_string_to_timedelta(time_string: str) -> datetime.timedelta:
    """Parse a time string in format 'HH:MM:SS.ffffff' to timedelta.
    
    Args:
        time_string: Time string in format like '00:00:45.5000000'
        
    Returns:
        timedelta object representing the elapsed time
    """
    try:
        # Parse format like "00:00:45.5000000"
        time_parts = time_string.split(':')
        if len(time_parts) != 3:
            raise ValueError(f"Invalid time format: {time_string}")
        
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = float(time_parts[2])
        
        return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except (ValueError, IndexError) as e:
        raise ValueError(f"Failed to parse time string '{time_string}': {e}")


class LoggingSpecificationDocument:
    """Represents a document that describes how data is logged.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_logging_specification_document`.
    """

    def __init__(
        self,
        channel: Channel,
        raise_if_application_closed: Callable[[], None],
        identifier: ElementIdentifier,
    ) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed
        self._identifier = identifier

    def get_log_file_base_path(self) -> str:
        """Get the log file base path.

        Returns:
            The base path for the log file.

        Raises:
            FlexLoggerError: if getting the log file base path fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetLogFileBasePath(
                LoggingSpecificationDocument_pb2.GetLogFileBasePathRequest(
                    document_identifier=self._identifier
                )
            )
            return response.log_file_base_path
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get log file base path") from error

    def get_resolved_log_file_base_path(self) -> str:
        """Get the resolved log file base path.

        Returns:
            The resolved base path for the log file.
            The resolved base path will have any placeholders replaced with
            actual values. Note that time sourced placeholders such as
            {Second} are resolved at the time of the call, and may resolve
            to a different time on a subsequent call or when a log file is created.

        Raises:
            FlexLoggerError: if getting the resolved log file base path fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetResolvedLogFileBasePath(
                LoggingSpecificationDocument_pb2.GetResolvedLogFileBasePathRequest(
                    document_identifier=self._identifier
                )
            )
            return response.resolved_log_file_base_path
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get resolved log file base path") from error

    def set_log_file_base_path(self, log_file_base_path: str) -> None:
        """Set the log file base path.

        Args:
            log_file_base_path: The log file base path.

        Raises:
            FlexLoggerError: if setting the log file base path fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetLogFileBasePath(
                LoggingSpecificationDocument_pb2.SetLogFileBasePathRequest(
                    document_identifier=self._identifier, log_file_base_path=log_file_base_path
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set log file base path") from error

    def get_log_file_name(self) -> str:
        """Get the log file name.

        Returns:
            The file name that will be logged to.

        Raises:
            FlexLoggerError: if getting the log file name fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetLogFileName(
                LoggingSpecificationDocument_pb2.GetLogFileNameRequest(
                    document_identifier=self._identifier
                )
            )
            return response.log_file_name
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get log file name") from error

    def get_resolved_log_file_name(self) -> str:
        """Get the resolved log file name.

        Returns:
            The resolved file name that will be logged to.
            The resolved file name will have any placeholders replaced with
            actual values. Note that time sourced placeholders such as
            {Second} are resolved at the time of the call, and may resolve
            to a different time on a subsequent call or when a log file is created.

        Raises:
            FlexLoggerError: if getting the resolved log file name fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetResolvedLogFileName(
                LoggingSpecificationDocument_pb2.GetResolvedLogFileNameRequest(
                    document_identifier=self._identifier
                )
            )
            return response.resolved_log_file_name
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get resolved log file name") from error

    def set_log_file_name(self, log_file_name: str) -> None:
        """Set the log file name.

        Args:
            log_file_name: The log file name.

        Raises:
            FlexLoggerError: if setting the log file name fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetLogFileName(
                LoggingSpecificationDocument_pb2.SetLogFileNameRequest(
                    document_identifier=self._identifier, log_file_name=log_file_name
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set log file name") from error

    def get_log_file_description(self) -> str:
        """Get the log file description.

        Returns:
            The description of the log file.

        Raises:
            FlexLoggerError: if getting the log file description fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetLogFileDescription(
                LoggingSpecificationDocument_pb2.GetLogFileDescriptionRequest(
                    document_identifier=self._identifier
                )
            )
            return response.log_file_description
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get log file description") from error

    def set_log_file_description(self, log_file_description: str) -> None:
        """Set the log file description.

        Args:
            log_file_description: The log file description.

        Raises:
            FlexLoggerError: if setting the log file description fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetLogFileDescription(
                LoggingSpecificationDocument_pb2.SetLogFileDescriptionRequest(
                    document_identifier=self._identifier, log_file_description=log_file_description
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set log file description") from error

    def get_log_files(self, log_file_type: LogFileType) -> List[str]:
        """Get log files in the data files pane of the project.

        Args:
            log_file_type: The type of log files to get.

        Returns:
            A list of the log files in the project.
            The entries are sorted chronologically with the most recent file last.

        Raises:
            FlexLoggerError: if getting the log files fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetLogFiles(
                LoggingSpecificationDocument_pb2.GetLogFilesRequest(
                    document_identifier=self._identifier,
                    log_file_type = LOG_FILE_TYPE_MAP[log_file_type]
                )
            )
            return [log_file for log_file in response.log_files]
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get data files") from error

    def remove_log_files(self, delete_files: bool = False) -> None:
        """Remove log files from the data files pane of the project.

        Args:
            delete_files: True to delete files on disk, False to remove only from project.

        Raises:
            FlexLoggerError: if removing the log files fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.RemoveLogFiles(
                LoggingSpecificationDocument_pb2.RemoveLogFilesRequest(
                    document_identifier=self._identifier,
                    delete_files=delete_files
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to remove log files") from error

    def _convert_to_test_property(
        self, test_property: LoggingSpecificationDocument_pb2.TestProperty
    ) -> TestProperty:
        return TestProperty(
            test_property.property_name,
            test_property.property_value,
            test_property.prompt_on_start,
        )

    def _convert_from_test_property(
        self, test_property: TestProperty
    ) -> LoggingSpecificationDocument_pb2.TestProperty:
        return LoggingSpecificationDocument_pb2.TestProperty(
            property_name=test_property.name,
            property_value=test_property.value,
            prompt_on_start=test_property.prompt_on_start,
        )

    def get_test_properties(self) -> List[TestProperty]:
        """Get all test properties.

        Returns:
            A list of the test properties on this document.

        Raises:
            FlexLoggerError: if getting the test properties fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetTestProperties(
                LoggingSpecificationDocument_pb2.GetTestPropertiesRequest(
                    document_identifier=self._identifier
                )
            )
            return [self._convert_to_test_property(x) for x in response.test_properties]
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get test properties") from error

    def set_test_properties(self, test_properties: List[TestProperty]) -> None:
        """Set test properties.

        Args:
            test_properties: A list of test properties to add or modify on this document.

        Raises:
            FlexLoggerError: if setting the test properties fails.
        """
        if len(test_properties) == 0:
            return
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetTestProperties(
                LoggingSpecificationDocument_pb2.SetTestPropertiesRequest(
                    document_identifier=self._identifier,
                    test_properties=[self._convert_from_test_property(x) for x in test_properties]
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set test properties") from error
        
    def get_test_property(self, test_property_name: str) -> TestProperty:
        """Get the test property with the specified name.

        Throws a :class:`FlexLoggerError` if a property with the
        specified name does not exist.

        Args:
            test_property_name: The name of the test property.

        Returns:
            The :class:`TestProperty` with the specified name.

        Raises:
            FlexLoggerError: if a property with the specified name does
                not exist, or if getting the property fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetTestProperty(
                LoggingSpecificationDocument_pb2.GetTestPropertyRequest(
                    document_identifier=self._identifier, property_name=test_property_name
                )
            )
            return self._convert_to_test_property(response.test_property)
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get test property") from error

    def set_test_property(
        self, property_name: str, property_value: str, prompt_on_start: bool = False
    ) -> None:
        """Set the information for a test property.

        Use this method to add a new test property or to modify an existing
        test property.

        Args:
            property_name: The name of the test property. If a test property
                already exists with the same :attr:`~TestProperty.name`, that test property
                will be updated with the new information passed to this method. Otherwise, a new
                test property will be created to reflect the specified test information.

            property_value: The property value to set.

            prompt_on_start: Whether this property should be set when the test session starts.
                Defaults to False. If this is set to True, the operator should be prompted to
                define this property when the test session starts.

        Raises:
            FlexLoggerError: if setting the property fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            test_property = LoggingSpecificationDocument_pb2.TestProperty(
                property_name=property_name,
                property_value=property_value,
                prompt_on_start=prompt_on_start,
            )
            stub.SetTestProperty(
                LoggingSpecificationDocument_pb2.SetTestPropertyRequest(
                    document_identifier=self._identifier, test_property=test_property
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set test property") from error

    def remove_test_property(self, test_property_name: str) -> None:
        """Removes the test property with the specified name.

        Args:
            test_property_name: The name of the test property.

        Raises:
            FlexLoggerError: if a property with the specified name does not
                exist, or if removing the property fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.RemoveTestProperty(
                LoggingSpecificationDocument_pb2.RemoveTestPropertyRequest(
                    document_identifier=self._identifier, property_name=test_property_name
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to remove test property") from error

    def get_start_trigger_settings(self):
        """Get the start trigger settings.

        Returns:
            A tuple containing 2 strings:
            - The start trigger condition
            - The start trigger settings
              The object returned varies based on the start trigger condition.
                - When the start trigger condition is TEST_START, the object is None
                - When the start trigger condition is CHANNEL_VALUE_CHANGE, the object is of type ValueChangeCondition
                - When the start trigger condition is ABSOLUTE_TIME, the object is a datetime object containing the test start time.
                - When the start trigger condition is TIME_ELAPSED, the object is a datetime.timedelta containing the elapsed time.
                - When the start trigger condition is BUTTON_PRESSED, the object is a string containing the button name.

        Raises:
            FlexLoggerError: if getting the start trigger settings fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetStartTriggerSettings(
                LoggingSpecificationDocument_pb2.GetStartTriggerSettingsRequest(
                    document_identifier=self._identifier
                )
            )
            start_trigger_condition = StartTriggerCondition.from_start_trigger_condition_pb2(response.start_trigger_condition)
            if start_trigger_condition == StartTriggerCondition.TEST_START:
                return start_trigger_condition, None
            elif start_trigger_condition == StartTriggerCondition.CHANNEL_VALUE_CHANGE:
                value_change_condition = ValueChangeCondition(response.start_trigger_settings)
                return start_trigger_condition, value_change_condition
            elif start_trigger_condition == StartTriggerCondition.ABSOLUTE_TIME:
                utc_start_time = parser.parse(response.start_trigger_settings)
                utc_start_time = utc_start_time.replace(tzinfo=tz.tzutc())
                start_time = utc_start_time.astimezone(tz.tzlocal())
                return start_trigger_condition, start_time
            elif start_trigger_condition == StartTriggerCondition.TIME_ELAPSED:
                elapsed_time = _parse_time_string_to_timedelta(response.start_trigger_settings)
                return start_trigger_condition, elapsed_time
            elif start_trigger_condition == StartTriggerCondition.BUTTON_PRESSED:
                return start_trigger_condition, response.start_trigger_settings
            else:
                return start_trigger_condition, response.start_trigger_settings
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the start trigger settings") from error

    def get_stop_trigger_settings(self) -> tuple[StopTriggerCondition, str]:
        """Get the stop trigger settings.

        Returns:
            A tuple containing 2 strings:
            - The stop trigger condition
            - The stop trigger settings
              The object returned varies based on the stop trigger condition.
                - When the stop trigger condition is TEST_STOP, the object is None
                - When the stop trigger condition is CHANNEL_VALUE_CHANGE, the object is of type ValueChangeCondition
                - When the stop trigger condition is TEST_TIME_ELAPSED, the object is a string containing the test duration
                - When the stop trigger condition is BUTTON_PRESSED, the object is a string containing the button name

        Raises:
            FlexLoggerError: if getting the stop trigger settings fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.GetStopTriggerSettings(
                LoggingSpecificationDocument_pb2.GetStopTriggerSettingsRequest(
                    document_identifier=self._identifier
                )
            )
            stop_trigger_condition = StopTriggerCondition.from_stop_trigger_condition_pb2(response.stop_trigger_condition)
            if stop_trigger_condition == StopTriggerCondition.TEST_STOP:
                return stop_trigger_condition, None
            elif stop_trigger_condition == StopTriggerCondition.CHANNEL_VALUE_CHANGE:
                value_change_condition = ValueChangeCondition(response.stop_trigger_settings)
                return stop_trigger_condition, value_change_condition
            else:
                return stop_trigger_condition, response.stop_trigger_settings
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the stop trigger settings") from error

    def set_start_trigger_settings_to_test_start(self) -> None:
        """Set the start trigger to Test Start

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetTestStartTriggerSettings(
                LoggingSpecificationDocument_pb2.SetTestStartTriggerSettingsRequest(
                    document_identifier=self._identifier
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the start trigger to Test Start") from error

    def set_start_trigger_settings_to_value_change(self, value_change_condition: ValueChangeCondition) -> None:
        """Set the start trigger to Channel Value Change

        Args:
            value_change_condition: The value change parameters as an object of type ValueChangeCondition

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetValueChangeStartTriggerSettings(
                LoggingSpecificationDocument_pb2.SetValueChangeStartTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    channel_name=value_change_condition.channel_name,
                    value_change_type=value_change_condition.value_change_type.to_value_change_type_pb2(),
                    threshold=value_change_condition.threshold,
                    min_value=value_change_condition.min_value,
                    max_value=value_change_condition.max_value,
                    leading_time=value_change_condition.time
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the start trigger to Channel Value Change") from error

    def set_start_trigger_settings_to_absolute_time(self, time: datetime) -> None:
        """Set the start trigger to Absolute Time

        Args:
            time: Test start time. If it's timezone-naive, it's assumed to be in UTC.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            test_start_time = Timestamp()
            test_start_time.FromDatetime(time)
            stub.SetTimeStartTriggerSettings(
                LoggingSpecificationDocument_pb2.SetTimeStartTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    time=test_start_time
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the start trigger to Absolute Time") from error

    def set_start_trigger_settings_to_elapsed_time(self, elapsed_time: datetime.timedelta) -> None:
        """Set the start trigger to Elapsed Time

        Args:
            elapsed_time: Time delta after which to start the test.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            # Convert timedelta to total seconds for the protobuf API
            elapsed_seconds = elapsed_time.total_seconds()
            stub.SetElapsedTimeStartTriggerSettings(
                LoggingSpecificationDocument_pb2.SetElapsedTimeStartTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    elapsed_time=elapsed_seconds
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the start trigger to Elapsed Time") from error

    def set_start_trigger_settings_to_button_pressed(self, button_name: str) -> None:
        """Set the start trigger to Button Pressed

        Args:
            button_name: The name of the button that triggers the test start.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetButtonPressedStartTriggerSettings(
                LoggingSpecificationDocument_pb2.SetButtonPressedStartTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    button_name=button_name
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the start trigger to Button Pressed") from error

    def set_stop_trigger_settings_to_test_stop(self) -> None:
        """Set the stop trigger to Test Stop

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetTestStopTriggerSettings(
                LoggingSpecificationDocument_pb2.SetTestStopTriggerSettingsRequest(
                    document_identifier=self._identifier
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the stop trigger to Test Stop") from error

    def set_stop_trigger_settings_to_value_change(self, value_change_condition: ValueChangeCondition) -> None:
        """Set the stop trigger to Channel Value Change

        Args:
            value_change_condition: The value change parameters as an object of type ValueChangeCondition

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetValueChangeStopTriggerSettings(
                LoggingSpecificationDocument_pb2.SetValueChangeStopTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    channel_name=value_change_condition.channel_name,
                    value_change_type=value_change_condition.value_change_type.to_value_change_type_pb2(),
                    threshold=value_change_condition.threshold,
                    min_value=value_change_condition.min_value,
                    max_value=value_change_condition.max_value,
                    trailing_time=value_change_condition.time
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the stop trigger to Channel Value Change") from error

    def set_stop_trigger_settings_to_duration(self, duration: datetime.timedelta) -> None:
        """Set the stop trigger to Test Time Elapsed

        Args:
            duration: The length of time after which to stop the test.

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            test_duration = Duration()
            test_duration.FromTimedelta(duration)
            stub.SetTimeStopTriggerSettings(
                LoggingSpecificationDocument_pb2.SetTimeStopTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    duration=test_duration
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the stop trigger to Test Time Elapsed") from error

    def set_stop_trigger_settings_to_button_pressed(self, button_name: str) -> None:
        """Set the stop trigger to Button Pressed

        Args:
            button_name: The name of the button that triggers the test stop.

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetButtonPressedStopTriggerSettings(
                LoggingSpecificationDocument_pb2.SetButtonPressedStopTriggerSettingsRequest(
                    document_identifier=self._identifier,
                    button_name=button_name
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the stop trigger to Button Pressed") from error

    def is_retriggering_enabled(self) -> bool:
        """Get the re-triggering configuration.

        Returns:
            True if re-triggering is enabled, False otherwise

        Raises:
            FlexLoggerError: if getting the re-triggering configuration fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            response = stub.IsRetriggeringEnabled(
                LoggingSpecificationDocument_pb2.IsRetriggeringEnabledRequest(
                    document_identifier=self._identifier
                )
            )
            return response.is_retriggering_enabled
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get the re-triggering configuration") from error

    def set_retriggering(self, retriggering: bool) -> None:
        """Set the re-triggering configuration.

        Args:
            retriggering: True to enable re-triggering, False to disable it.

        Raises:
            FlexLoggerError: if setting the re-triggering configuration fails.
        """
        stub = LoggingSpecificationDocument_pb2_grpc.LoggingSpecificationDocumentStub(self._channel)
        try:
            stub.SetRetriggering(
                LoggingSpecificationDocument_pb2.SetRetriggeringRequest(
                    document_identifier=self._identifier,
                    is_retriggering_enabled=retriggering
                )
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to set the re-triggering configuration") from error
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_project.py sha256=2fd4b6a5015474c6072f1fb6b593d68ee8563a7371f72921778451c5bc09fe16 bytes=8482 -->
## FILE: src/flexlogger/automation/_project.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_project.py`
- sha256: `2fd4b6a5015474c6072f1fb6b593d68ee8563a7371f72921778451c5bc09fe16`
- bytes: 8482

````python
import os.path
import pathlib
from typing import Callable
from typing import Optional

from google.protobuf import empty_pb2
from grpc import Channel, RpcError

from ._channel_specification_document import ChannelSpecificationDocument
from ._flexlogger_error import FlexLoggerError
from ._logging_specification_document import LoggingSpecificationDocument
from ._screen_document import ScreenDocument
from ._test_session import TestSession
from ._test_specification_document import TestSpecificationDocument
from .proto import (
    Project_pb2,  # type: ignore
    Project_pb2_grpc,  # type: ignore
)
from .proto.Identifiers_pb2 import ProjectIdentifier


class Project:
    """Represents a FlexLogger project.

    Do not create this class directly; instead, use the return value of
    :meth:`.Application.open_project`.
    """

    def __init__(
        self,
        channel: Channel,
        raise_if_application_closed: Callable[[], None],
        identifier: ProjectIdentifier,
    ) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed
        self._identifier = identifier
        self._test_session = TestSession(self._channel, raise_if_application_closed)

    def open_channel_specification_document(self) -> ChannelSpecificationDocument:
        """Open the channel specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            response = stub.OpenChannelSpecificationDocument(
                Project_pb2.OpenChannelSpecificationDocumentRequest(project=self._identifier)
            )
            return ChannelSpecificationDocument(
                self._channel, self._raise_if_application_closed, response.document_identifier
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to open channel specification document") from error

    def open_logging_specification_document(self) -> LoggingSpecificationDocument:
        """Open the logging specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            response = stub.OpenLoggingSpecificationDocument(
                Project_pb2.OpenLoggingSpecificationDocumentRequest(project=self._identifier)
            )
            return LoggingSpecificationDocument(
                self._channel, self._raise_if_application_closed, response.document_identifier
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to open logging specification document") from error

    def open_screen_document(self, filename: str) -> ScreenDocument:
        """Open the specified screen document in the project.

        Args:
            filename: The name of the screen document to open.  Including
                the .flxscr extension in this argument is optional.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if a screen document of the specified name does
                not exist, or if opening the document fails.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            response = stub.OpenScreenDocument(
                Project_pb2.OpenScreenDocumentRequest(
                    project=self._identifier, screen_name=filename
                )
            )
            return ScreenDocument(
                self._channel, self._raise_if_application_closed, response.document_identifier
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to open screen document") from error

    def open_test_specification_document(self) -> TestSpecificationDocument:
        """Open the test specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            response = stub.OpenTestSpecificationDocument(
                Project_pb2.OpenTestSpecificationDocumentRequest(project=self._identifier)
            )
            return TestSpecificationDocument(
                self._channel, self._raise_if_application_closed, response.document_identifier
            )
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to open test specification document") from error

    def close(self) -> None:
        """Close the project.

        Raises:
            FlexLoggerError: if closing the project fails.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            stub.Close(Project_pb2.CloseProjectRequest(allow_prompts=False, project=self._identifier))
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to close project") from error

    def save(self) -> None:
        """Save the project.

        Raises:
            FlexLoggerError: if saving the project fails due to a communication error.
            If there is no communication error with the FlexLogger application, this function will not raise an
            exception, but instead return a boolean indicating if the project was properly saved.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            stub.Save(empty_pb2.Empty())
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to save project") from error

    def saveas(self, project_name: str, project_directory: str) -> None:
        """Saves the currently loaded project to a specified location with a given project name.

        Args:
            project_name: The name of the project to save as.
            project_directory: The directory path where the project should be saved.

        Raises:
            FlexLoggerError: if saving the project fails due to a communication error.
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            stub.SaveAs(Project_pb2.SaveAsRequest(
                project_name=project_name,
                project_directory=project_directory
            ))
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to save project") from error

    @property
    def test_session(self) -> TestSession:
        """Get the test session for the project."""
        return self._test_session

    @property
    def project_file_path(self) -> Optional[pathlib.Path]:
        """Get the project file path on disk

        Returns: The saved project file path if it exists, None otherwise
        """
        stub = Project_pb2_grpc.ProjectStub(self._channel)
        try:
            response = stub.GetProjectFilePath(
                Project_pb2.GetProjectFilePathRequest(project=self._identifier)
            )
            # return a Path() if the returned path is not empty, otherwise return None
            # pathlib.Path() treats empty string as "current directory" which could be confusing
            return pathlib.Path(response.project_file_path) if response.project_file_path else None
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get project file path") from error

    @property
    def project_name(self) -> Optional[str]:
        """Get the project name

        Returns: The project name if the file path exists, None otherwise
        """
        project_path = self.project_file_path

        return os.path.basename(os.path.splitext(project_path)[0])
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_screen_document.py sha256=6ca7d0f5d15e0a77772b08c48f934d818c2eac4073c65bc1b7cb4a8cc938cc06 bytes=752 -->
## FILE: src/flexlogger/automation/_screen_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_screen_document.py`
- sha256: `6ca7d0f5d15e0a77772b08c48f934d818c2eac4073c65bc1b7cb4a8cc938cc06`
- bytes: 752

````python
from typing import Callable

from grpc import Channel

from .proto.Identifiers_pb2 import ElementIdentifier


class ScreenDocument:
    """Represents a document that displays data.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_screen_document`.

    Note that this class currently has no functionality; more functionality
    may be added in the future.
    """

    def __init__(
        self,
        channel: Channel,
        raise_if_application_closed: Callable[[], None],
        identifier: ElementIdentifier,
    ) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed
        self._identifier = identifier
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_severity_level.py sha256=122ca487ac6e02e504ac31618505389dd63883fce5a7f25677823400633e6db0 bytes=146 -->
## FILE: src/flexlogger/automation/_severity_level.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_severity_level.py`
- sha256: `122ca487ac6e02e504ac31618505389dd63883fce5a7f25677823400633e6db0`
- bytes: 146

````python
from enum import Enum


class SeverityLevel(Enum):
    """Represents the severity level of an alarm."""

    WARNING = 2
    CRITICAL = 4
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_start_trigger_condition.py sha256=346263e8ea49b1ba72bb05af1807759ee01f7d853851f9cf2c85ffe60c191c4a bytes=1999 -->
## FILE: src/flexlogger/automation/_start_trigger_condition.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_start_trigger_condition.py`
- sha256: `346263e8ea49b1ba72bb05af1807759ee01f7d853851f9cf2c85ffe60c191c4a`
- bytes: 1999

````python
from enum import Enum
from .proto.StartTriggerCondition_pb2 import StartTriggerCondition as StartTriggerCondition_pb2


class StartTriggerCondition(Enum):
    """An enumeration describing when to the logging starts."""

    """Manually begin logging by clicking RUN."""
    TEST_START = 0

    """Begin logging when the value of the channel meets the specified value change condition."""
    CHANNEL_VALUE_CHANGE = 1

    """Begin logging at a designated date and time."""
    ABSOLUTE_TIME = 2

    """Begin logging after a designated amount of time has elapsed."""
    TIME_ELAPSED = 3

    """Begin logging when a designated button is pressed."""
    BUTTON_PRESSED = 4

    def to_start_trigger_condition_pb2(self) -> StartTriggerCondition_pb2:
        return START_TRIGGER_CONDITION_MAP.get(self.value)

    @staticmethod
    def from_start_trigger_condition_pb2(start_trigger_condition: StartTriggerCondition_pb2):
        return START_TRIGGER_CONDITION_PB2_MAP.get(start_trigger_condition)


START_TRIGGER_CONDITION_MAP = {
    0: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TEST_START,
    1: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE,
    2: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME,
    3: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME_ELAPSED,
    4: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_BUTTON_PRESSED
}

START_TRIGGER_CONDITION_PB2_MAP = {
    StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TEST_START: StartTriggerCondition.TEST_START,
    StartTriggerCondition_pb2.START_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE: StartTriggerCondition.CHANNEL_VALUE_CHANGE,
    StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME: StartTriggerCondition.ABSOLUTE_TIME,
    StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME_ELAPSED: StartTriggerCondition.TIME_ELAPSED,
    StartTriggerCondition_pb2.START_TRIGGER_CONDITION_BUTTON_PRESSED: StartTriggerCondition.BUTTON_PRESSED
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_stop_trigger_condition.py sha256=d69541426ffaa4350b4bfae9e2e18d4c6abd3559ad1f2c0ffa39efd898a67bfa bytes=1765 -->
## FILE: src/flexlogger/automation/_stop_trigger_condition.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_stop_trigger_condition.py`
- sha256: `d69541426ffaa4350b4bfae9e2e18d4c6abd3559ad1f2c0ffa39efd898a67bfa`
- bytes: 1765

````python
from enum import Enum
from .proto.StopTriggerCondition_pb2 import StopTriggerCondition as StopTriggerCondition_pb2


class StopTriggerCondition(Enum):
    """An enumeration describing when to the logging stops."""

    """Manually stop logging by clicking the STOP button."""
    TEST_STOP = 0

    """Stop logging when the value of the acquisition on a designated channel meets the specified value change condition."""
    CHANNEL_VALUE_CHANGE = 1

    """Stop logging after a designated duration of time has elapsed."""
    TEST_TIME_ELAPSED = 2

    """Stop logging when a designated button is pressed."""
    BUTTON_PRESSED = 3

    def to_stop_trigger_condition_pb2(self) -> StopTriggerCondition_pb2:
        return STOP_TRIGGER_CONDITION_MAP.get(self.value)

    @staticmethod
    def from_stop_trigger_condition_pb2(stop_trigger_condition: StopTriggerCondition_pb2):
        return STOP_TRIGGER_CONDITION_PB2_MAP.get(stop_trigger_condition)


STOP_TRIGGER_CONDITION_MAP = {
    0: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TEST_STOP,
    1: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE,
    2: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TIME_ELAPSED,
    3: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_BUTTON_PRESSED
}

STOP_TRIGGER_CONDITION_PB2_MAP = {
    StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TEST_STOP: StopTriggerCondition.TEST_STOP,
    StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE: StopTriggerCondition.CHANNEL_VALUE_CHANGE,
    StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TIME_ELAPSED: StopTriggerCondition.TEST_TIME_ELAPSED,
    StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_BUTTON_PRESSED: StopTriggerCondition.BUTTON_PRESSED
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_property.py sha256=6d65067183e33ee743af8cd2a02618d9864587061d611781b437afdc24a5b2d0 bytes=1302 -->
## FILE: src/flexlogger/automation/_test_property.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_test_property.py`
- sha256: `6d65067183e33ee743af8cd2a02618d9864587061d611781b437afdc24a5b2d0`
- bytes: 1302

````python
class TestProperty:
    """Information about a test property."""

    def __init__(self, name: str, value: str, prompt_on_start: bool):
        """Create a new TestProperty.

        Args:
            name: The name of the property.
            value: The value of the property.
            prompt_on_start: Whether the operator should be prompted to define this
                property when the test session starts.
        """
        self._name = name
        self._value = value
        self._prompt_on_start = prompt_on_start

    def __repr__(self) -> str:
        return 'flexlogger.automation.TestProperty("%s", "%s", %s)' % (
            self._name,
            self._value,
            str(self._prompt_on_start),
        )

    @property
    def name(self) -> str:
        """The name of the property."""
        return self._name

    @property
    def value(self) -> str:
        """The value of the property."""
        return self._value

    @property
    def prompt_on_start(self) -> bool:
        """Whether this property should be set when the test session starts.

        If this is set to true, the operator should be prompted to define this property
        when the test session starts.
        """
        return self._prompt_on_start
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_session.py sha256=9d67961f6fc9e61752406239af04f6f4b594468e3eeb2b2d58b68e90beb93fbd bytes=6557 -->
## FILE: src/flexlogger/automation/_test_session.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_test_session.py`
- sha256: `9d67961f6fc9e61752406239af04f6f4b594468e3eeb2b2d58b68e90beb93fbd`
- bytes: 6557

````python
from datetime import timedelta
from typing import Callable

from grpc import Channel, RpcError

from ._flexlogger_error import FlexLoggerError
from ._test_session_state import TestSessionState
from .proto import (
    TestSession_pb2,
    TestSession_pb2_grpc,
)
from .proto.TestSessionState_pb2 import TestSessionState as TestSessionState_pb2

STATE_MAP = {
    TestSessionState_pb2.TEST_SESSION_STATE_IDLE: TestSessionState.IDLE,
    TestSessionState_pb2.TEST_SESSION_STATE_RUNNING: TestSessionState.RUNNING,
    TestSessionState_pb2.TEST_SESSION_STATE_INVALID_CONFIGURATION: (
        TestSessionState.INVALID_CONFIGURATION
    ),
    TestSessionState_pb2.TEST_SESSION_STATE_NO_VALID_LOGGED_CHANNELS: (
        TestSessionState.NO_VALID_LOGGED_CHANNELS
    ),
    TestSessionState_pb2.TEST_SESSION_STATE_PAUSED: TestSessionState.PAUSED,
}


class TestSession:
    """Represents a test session for a project.

    Do not create this class directly; instead, use the property
    :attr:`.Project.test_session`.
    """

    def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None]) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed

    def add_note(self, note: str) -> None:
        """Add a note to the current log file.

        This method requires the test session to be in the
        :attr:`.TestSessionState.RUNNING` state.

        Args:
            note: The note to add to the log file.

        Raises:
            FlexLoggerError: if the test session is not in the
                :attr:`.TestSessionState.RUNNING` state, or if adding the note fails.
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            stub.AddNote(TestSession_pb2.AddNoteRequest(note=note))
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to add note") from error

    @property
    def state(self) -> TestSessionState:
        """Get the current state of the test session.

        Raises:
            FlexLoggerError: if getting the current state fails.
        """
        self._raise_if_application_closed()
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            get_test_session_state_response = stub.GetState(
                TestSession_pb2.GetTestSessionStateRequest()
            )
            state = STATE_MAP.get(get_test_session_state_response.test_session_state)
            if state is None:
                raise RuntimeError("The test session is in an undefined state.")
            return state
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to get test session state") from error

    def start(self) -> bool:
        """Start the test session, if possible.

        Returns:
            True if the test was started, otherwise False.

        Raises:
            FlexLoggerError: if starting the test session fails.
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            start_test_session_response = stub.Start(TestSession_pb2.StartTestSessionRequest())
            return start_test_session_response.test_session_started
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to start test session") from error

    def stop(self) -> bool:
        """Stop the test session, if possible.

        Returns:
            True if the test was stopped, otherwise False.

        Raises:
            FlexLoggerError: if stopping the test session fails.
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            stop_test_session_response = stub.Stop(TestSession_pb2.StopTestSessionRequest())
            return stop_test_session_response.test_session_stopped
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to stop test session") from error

    def pause(self) -> bool:
        """Pauses the test session, if possible.

        Returns:
            True if the test was paused, otherwise False.

        Raises:
            FlexLoggerError: if pausing the test session fails.
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            pause_test_session_response = stub.Pause(TestSession_pb2.PauseTestSessionRequest())
            return pause_test_session_response.test_session_paused
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to pause test session") from error

    def resume(self) -> bool:
        """Resumes the test session, if possible.

        Returns:
            True if the test was resumed, otherwise False.

        Raises:
            FlexLoggerError: if resuming the test session fails.
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            resume_test_session_response = stub.Resume(TestSession_pb2.ResumeTestSessionRequest())
            return resume_test_session_response.test_session_resumed
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to resume test session") from error

    @property
    def elapsed_test_time(self) -> timedelta:
        """Queries the elapsed test time

        Returns:
            The current tests's elapsed time if a test is running or paused,
            the most recent test's elapsed time if a test has been run and stopped.

        Raises:
            FlexLoggerError: if no test has ever been run since the project was loaded
        """
        stub = TestSession_pb2_grpc.TestSessionStub(self._channel)
        try:
            get_elapsed_test_time_response = stub.GetElapsedTestTime(
                TestSession_pb2.GetElapsedTestTimeRequest()
            )
            return timedelta(seconds=get_elapsed_test_time_response.elapsed_test_time)
        except (RpcError, ValueError) as error:
            self._raise_if_application_closed()
            raise FlexLoggerError("Failed to query elapsed test time") from error
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_session_state.py sha256=bbdfa3fa3b9f2db26421d79e77bdb9faa386ecba224435b8e0acdfdb95968d19 bytes=946 -->
## FILE: src/flexlogger/automation/_test_session_state.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_test_session_state.py`
- sha256: `bbdfa3fa3b9f2db26421d79e77bdb9faa386ecba224435b8e0acdfdb95968d19`
- bytes: 946

````python
from enum import Enum


class TestSessionState(Enum):
    """An enumeration describing the possible states of a :class:`.TestSession`."""

    IDLE = 1
    """The :class:`.TestSession` is idle and not running.

    Configuration changes can occur during this state.
    """

    RUNNING = 2
    """The :class:`.TestSession` is running.

    Logging and events are active while the test session is running.

    Configuration changes are not allowed when the test session is running.
    """

    INVALID_CONFIGURATION = 3
    """The project has a configuration error."""

    NO_VALID_LOGGED_CHANNELS = 4
    """No channels have been configured, or all channels are disabled or not available."""

    PAUSED = 5
    """The :class:`.TestSession` is paused.

    Logging and events are not active while the test session is paused.

    Configuration changes are not allowed when the test session is paused.
    """
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_specification_document.py sha256=96586cb08d29b3ea43901947c94fdfaea2e9fe65fd0224dd55ba9f270cca9086 bytes=778 -->
## FILE: src/flexlogger/automation/_test_specification_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_test_specification_document.py`
- sha256: `96586cb08d29b3ea43901947c94fdfaea2e9fe65fd0224dd55ba9f270cca9086`
- bytes: 778

````python
from typing import Callable

from grpc import Channel

from .proto.Identifiers_pb2 import ElementIdentifier


class TestSpecificationDocument:
    """Represents a document that describes a test.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_test_specification_document`.

    Note that this class currently has no functionality; more functionality
    may be added in the future.
    """

    def __init__(
        self,
        channel: Channel,
        raise_if_application_closed: Callable[[], None],
        identifier: ElementIdentifier,
    ) -> None:
        self._channel = channel
        self._raise_if_application_closed = raise_if_application_closed
        self._identifier = identifier
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_value_change_condition.py sha256=f8f000e4d0ebd46110e039bb378785b2f93b0a47a52e96b080190ce16c114db3 bytes=3882 -->
## FILE: src/flexlogger/automation/_value_change_condition.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_value_change_condition.py`
- sha256: `f8f000e4d0ebd46110e039bb378785b2f93b0a47a52e96b080190ce16c114db3`
- bytes: 3882

````python
from ._value_change_type import ValueChangeType
import json


class ValueChangeCondition:
    """Represents a value change condition.
     Create a ValueChangeCondition object when you want to set the start or stop trigger to value change.
    """

    def __init__(self, value_change_condition='') -> None:
        if len(value_change_condition) > 0:
            json_condition = json.loads(value_change_condition)
            self._channel_name = json_condition['ChannelName']
            self._value_change_type = ValueChangeType.from_value_change_type_pb2(int(json_condition['ValueChangeType']))
            self._threshold = float(json_condition['Threshold'])
            self._min_value = float(json_condition['MinValue'])
            self._max_value = float(json_condition['MaxValue'])
            self._time = float(json_condition['Time'])
        else:
            self._channel_name = ''
            self._value_change_type = ValueChangeType.NONE
            self._threshold = 0
            self._min_value = 0
            self._max_value = 0
            self._time = 0

    def __eq__(self, other):
        objects_equal = (self._channel_name == other.channel_name and
                         self._value_change_type == other.value_change_type and
                         self._threshold == other.threshold and
                         self._min_value == other.min_value and
                         self._max_value == other.max_value and
                         self._time == other.time)
        return objects_equal

    def __repr__(self):
        value_change_condition_string = 'ValueChangeCondition\r\n' \
                                        'channel_name = {0}\r\n' \
                                        'value_change_type = {1}\r\n' \
                                        'threshold = {2}\r\n' \
                                        'min_value = {3}\r\n' \
                                        'max_value = {4}\r\n' \
                                        'time = {5}'.format(self._channel_name,
                                                            self._value_change_type,
                                                            self._threshold,
                                                            self._min_value,
                                                            self._max_value,
                                                            self._time)
        return value_change_condition_string

    @property
    def channel_name(self) -> str:
        """The channel name."""
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value: str):
        self._channel_name = value

    @property
    def value_change_type(self) -> ValueChangeType:
        """The value change type."""
        return self._value_change_type

    @value_change_type.setter
    def value_change_type(self, value: ValueChangeType):
        self._value_change_type = value

    @property
    def threshold(self) -> float:
        """The threshold."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: float):
        self._threshold = value

    @property
    def min_value(self) -> float:
        """The range minimum."""
        return self._min_value

    @min_value.setter
    def min_value(self, value: float):
        self._min_value = value

    @property
    def max_value(self) -> float:
        """The range maximum."""
        return self._max_value

    @max_value.setter
    def max_value(self, value: float):
        self._max_value = value

    @property
    def time(self) -> float:
        """The leading or trailing time in seconds."""
        return self._time

    @time.setter
    def time(self, value: float):
        self._time = value
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/_value_change_type.py sha256=6ad06cdad42c2f134d19ad474d8b5ea14dda190a33aeefa41b179929c1d0bf50 bytes=1753 -->
## FILE: src/flexlogger/automation/_value_change_type.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/_value_change_type.py`
- sha256: `6ad06cdad42c2f134d19ad474d8b5ea14dda190a33aeefa41b179929c1d0bf50`
- bytes: 1753

````python
from enum import Enum
from .proto.ValueChangeType_pb2 import ValueChangeType as ValueChangeType_pb2


class ValueChangeType(Enum):
    """An enumeration describing the possible types of value change events."""

    """Start Trigger not configured."""
    NONE = 0

    """Start or stop a test when a channel value rises above a specified value."""
    RISE_ABOVE_VALUE = 1

    """Start or stop a test when a channel value falls below a specified value."""
    FALL_BELOW_VALUE = 3

    """Start or stop a test when a channel value enters a range."""
    ENTER_RANGE = 5

    """Start or stop a test when a channel value leaves a range."""
    LEAVE_RANGE = 6

    def to_value_change_type_pb2(self) -> ValueChangeType_pb2:
        return VALUE_CHANGE_TYPE_MAP.get(self.value)

    @staticmethod
    def from_value_change_type_pb2(value_change_type: ValueChangeType_pb2):
        return VALUE_CHANGE_TYPE_PB2_MAP.get(value_change_type)


VALUE_CHANGE_TYPE_MAP = {
    0: ValueChangeType_pb2.TYPE_NONE,
    1: ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE,
    2: ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE_INCLUSIVE,
    3: ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE,
    4: ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE_INCLUSIVE,
    5: ValueChangeType_pb2.TYPE_ENTER_RANGE,
    6: ValueChangeType_pb2.TYPE_LEAVE_RANGE
}

VALUE_CHANGE_TYPE_PB2_MAP = {
    ValueChangeType_pb2.TYPE_NONE: ValueChangeType.NONE,
    ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE: ValueChangeType.RISE_ABOVE_VALUE,
    ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE: ValueChangeType.FALL_BELOW_VALUE,
    ValueChangeType_pb2.TYPE_ENTER_RANGE: ValueChangeType.ENTER_RANGE,
    ValueChangeType_pb2.TYPE_LEAVE_RANGE: ValueChangeType.LEAVE_RANGE
}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/automation/proto/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: src/flexlogger/automation/proto/__init__.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/automation/proto/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=src/flexlogger/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/flexlogger/py.typed

- repository: `ni/niflexlogger-automation-python`
- source_path: `src/flexlogger/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/__init__.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/DefaultProject/Channel Specification.flxio sha256=0211d7d332a25e6d803992221777940022a3f4b78838ac175b259304639651c1 bytes=2403 -->
## FILE: tests/assets/DefaultProject/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/DefaultProject/Channel Specification.flxio`
- sha256: `0211d7d332a25e6d803992221777940022a3f4b78838ac175b259304639651c1`
- bytes: 2403

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="A065B546FD29330A57BA1494B8A435CBFE102C254C08B4F9471D69E7FF268BFB478859A19EEE4F65F75BA365F24EAFBE1E8B74618E58FBE02B0053B434B374ED" Timestamp="1D64A60CB51C127" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="FlexLogger DAQmx" Name="http://www.ni.com/FlexLogger/DAQmx" OldestCompatibleVersion="8.3.0.3" Version="8.3.0.3" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1193" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="e52bf74ca6fe4d1b993dc0ac7b75d28a">
			<ProcessingElementModelOwner Id="621e468e6da04b3f84906e5a736f10e8">
				<DAQmxProcessingElement Id="5e6516b4c9c148098ef12af07b94f2bb" xmlns="http://www.ni.com/FlexLogger/DAQmx">
					<TopLevelTimingOwner FallbackMediumSampleRateLevel="[SampleRateLevel]Fast" Id="71fe72f17e544d4288a07a957a458557">
						<SampleTiming Id="2a0225c625124f2a9bfefb94ff536e3d" Level="[SampleRateLevel]Slow" Units="[Unit]Hertz" Value="[double]1" />
						<SampleTiming Id="f0ed513700144f4a8df75cb2cbafe92a" Level="[SampleRateLevel]Medium" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="64c6143c7a084c86b33474a1c6c01d6e" Level="[SampleRateLevel]Fast" Units="[Unit]Hertz" Value="[double]1000" />
						<SampleTiming Id="b6eca8c30fa44ac18b75a64e2bd8e336" Level="[SampleRateLevel]Counter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="54c4597f5c60437e958f036285f67e11" Level="[SampleRateLevel]Digital" Units="[Unit]Hertz" Value="[double]10" />
						<OnDemandTiming Id="f8eb6a50f262488ca7482497cb5db285" Level="[SampleRateLevel]OnDemand" />
					</TopLevelTimingOwner>
				</DAQmxProcessingElement>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="df409c7727324ac0aae6a72214524bf2" />
	</ChannelSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/DefaultProject/DefaultProject.flxproj sha256=0a7d2cab0b598f28b197266532e165c9fed33636f6be447a1126943598d73d06 bytes=3947 -->
## FILE: tests/assets/DefaultProject/DefaultProject.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/DefaultProject/DefaultProject.flxproj`
- sha256: `0a7d2cab0b598f28b197266532e165c9fed33636f6be447a1126943598d73d06`
- bytes: 3947

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2EC200EFF4454B7FFAAE817A5D2D95014C5609A3209307F928838D1FBE6317DF692B0E448060A5F54EA2C864EA53314A845A71AFDA127DCAA32F73877957A5C2" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1193" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="d77ad39313b14fe1b0c8a74f8cce401a" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="f5081f4f6f27443eb7fcb809944996dd" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="b2920b5a7a564edab4f7d65b644f6592" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="8485e73aa80f4670afcdbee83683ea85" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="46ec57e0815f4572a7182f0fce6c0472" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="e5dcfa2ad5c044939dc647629606158d" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="dcd6b5923515409fbb02a41c4006cb40" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="26c6364ce9634204a230d816991f5e12" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="57db15f3097a47dea266be3f148cdc5f" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="9d8f41234355475dbfe2072518b37ede" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-06-24T19:42:26.0001535Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="67d6150a26764aef8de0f1cb0e1d309a" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="7ba47c4be5f74ac5a71cb4e40b6d2216" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="163c0dd731943b580d17e30918c0809" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/DefaultProject/Logging Specification.flxcfg sha256=b44ebec893a9fc3ec80a5ea302eecb5097533066688d767a894adf2c1e42fc48 bytes=2116 -->
## FILE: tests/assets/DefaultProject/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/DefaultProject/Logging Specification.flxcfg`
- sha256: `b44ebec893a9fc3ec80a5ea302eecb5097533066688d767a894adf2c1e42fc48`
- bytes: 2116

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2C27A4C9CB7C359B1BE4447CC4B5C0F84CED34008A061018691C587ED91546B7FB957B6F8C1FB5B19E2E632303C3B93C6C042866C6E0A2538EB9C0320F948062" Timestamp="1D6A7CE33BC1614" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="34e840b3a54d48bc9efb9247fd59721b">
			<ProcessingElementModelOwner Id="d41b1a98d8504639a53a8676829f8e46">
				<TriggeredLoggingProvider Id="62764a9c483147cca469326a07593765" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-06-24T14:42:16.227138799999999999967674468859257785879890434443950653076171875-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="cdfcce0fa61e4c0aa21693daf96f3fc6" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="6a069a8120ef4377b151e6f7f3870170">
						<UserDefinedMetadataItem DataType="String" Id="eb12d176692348eda3940f40b50c5f50" Name="Operator">
							<p.Value>bparrott</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="e11367b4a0924faeb00f26c760a312ee" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/DefaultProject/Screen.flxscr sha256=58514201c7d24cdced038d5b6df4aa29db4ac16dc458178b065640cecd2d33f9 bytes=1338 -->
## FILE: tests/assets/DefaultProject/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/DefaultProject/Screen.flxscr`
- sha256: `58514201c7d24cdced038d5b6df4aa29db4ac16dc458178b065640cecd2d33f9`
- bytes: 1338

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="B7C4E7C7FB11B41486E3EAC7B646EB4DAC909ECC1BF79FA300EFA9F5F8EDD1C5679D186D11925158FAF07672B17631C50C3C4BD5B15E2FFA615CC95A191488A4" Timestamp="1D64A60CB5714BF" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1193" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="92ea4f1ad8d84bfdacec6a49067d72b3" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="a6556a648b6940c9917f7f501abd7831" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/DefaultProject/Test Specification.flxtest sha256=52d7b24a49c4e74594265d08eb46f797b854fca467bec3765651168b85619e9a bytes=1056 -->
## FILE: tests/assets/DefaultProject/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/DefaultProject/Test Specification.flxtest`
- sha256: `52d7b24a49c4e74594265d08eb46f797b854fca467bec3765651168b85619e9a`
- bytes: 1056

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="AB56F6577B8341490C54F2613EBEA20F9A94A0D5A9F98FE6756EEF96D3D7F74DF3C339F7486194A0861F5D983C55A271B753F266F164842138F79EE26B0CEB05" Timestamp="1D64A60CB56EDC0" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1193" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1193" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="fc329d3a1cbb4642bd2f359c09d7fb2f">
			<ProcessingElementModelOwner Id="2a85c8c6bd01494786972172e3fe75fe" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/Plugins/CreateChannelsInProcess/CreateChannelsInProcess.xml sha256=70a7348548d4ec7d790c09d0ad2ea148e60f978e5725ddb61d1cacd9bf40efde bytes=699 -->
## FILE: tests/assets/Plugins/CreateChannelsInProcess/CreateChannelsInProcess.xml

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/Plugins/CreateChannelsInProcess/CreateChannelsInProcess.xml`
- sha256: `70a7348548d4ec7d790c09d0ad2ea148e60f978e5725ddb61d1cacd9bf40efde`
- bytes: 699

````xml
<?xml version="1.0" encoding="utf-8"?>
<ProcessingElement>
  <Type>94D4 1FA- F6F-6C4F-B623-8FBFB79085 1</Type>
  <Name>CreateChannelsInProcess</Name>
  <TemplateType>Plugin</TemplateType>
  <DevelopmentKitVersion>1.0</DevelopmentKitVersion>
  <Version>0.1</Version>
  <OldestCompatibleVersion>0.1</OldestCompatibleVersion>
  <AliasBase>CreateChannelsInProcess</AliasBase>
  <Icon>input</Icon>
  <Description>This template type provides a starting point for plugins that produce data for FlexLogger. For example, this type acquires data from a third-party instrument to be logged alongside other FlexLogger channels.</Description>
  <VIExec>niPluginWrapper</VIExec>  
</ProcessingElement>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/Plugins/SwitchBoard/SwitchBoard.xml sha256=17ab75c1084dd893c1cf1fe6e9a176c3c24f93604e684caa36016a4eb1976746 bytes=490 -->
## FILE: tests/assets/Plugins/SwitchBoard/SwitchBoard.xml

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/Plugins/SwitchBoard/SwitchBoard.xml`
- sha256: `17ab75c1084dd893c1cf1fe6e9a176c3c24f93604e684caa36016a4eb1976746`
- bytes: 490

````xml
<?xml version="1.0" encoding="utf-8"?>
<ProcessingElement>
  <Type>499DD1BA-7ACC-4B7A-E3C8-AB7C12 1352C</Type>
  <Name>SwitchBoard</Name>
  <TemplateType>Plugin</TemplateType>
  <DevelopmentKitVersion>1.0</DevelopmentKitVersion>
  <Version>0.1</Version>
  <OldestCompatibleVersion>0.1</OldestCompatibleVersion>
  <AliasBase>SwitchBoard</AliasBase>
  <Icon>output</Icon>
  <Description>My switchboard plugin</Description>
  <VIExec>niPluginWrapper</VIExec>  
</ProcessingElement>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithAlarms/Channel Specification.flxio sha256=d59d5487280936ea69846f6a4538fdfaa6c7c91cb28ad33cbb0cd2af56170b3b bytes=7616 -->
## FILE: tests/assets/ProjectWithAlarms/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithAlarms/Channel Specification.flxio`
- sha256: `d59d5487280936ea69846f6a4538fdfaa6c7c91cb28ad33cbb0cd2af56170b3b`
- bytes: 7616

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FE2AFC8E00394777D35D47CA98263589AEF7B13DAD309A1DE9BE6A90C5EC0030FB2C5BDA4F2974D5BB99385FF57B2438F32825CAABEC8D08CF71E6FF971D8A97" Timestamp="1D96E453A2A46BF" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.9.0.1019" FeatureSetName="FlexLogger DAQmx" Name="http://www.ni.com/FlexLogger/DAQmx" OldestCompatibleVersion="9.8.0.49152" Version="9.8.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.1019" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="9.6.0.49152" Version="9.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.834" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="9.9.0.1019" Name="FlexLogger" Version="23.3.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="fc63b6cee1b340bfb2a6c781cde271d3">
			<ProcessingElementModelOwner Id="62952760ce434f7cb9fb2d555c32b701">
				<DAQmxProcessingElement Id="7987c8c20a1744408a3df1b7b3402235" xmlns="http://www.ni.com/FlexLogger/DAQmx">
					<TopLevelTimingOwner FallbackMediumSampleRateLevel="[SampleRateLevel]Fast" Id="98ebabbd86b84e1ebd25a76b9957efaa">
						<SampleTiming Id="80421f3882cc412397c3716a4396e967" Level="[SampleRateLevel]Slow" Units="[Unit]Hertz" Value="[double]1" />
						<SampleTiming Id="29421b77d86147f6ae9c2cd50990ddd6" Level="[SampleRateLevel]Medium" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="da7296c7375b445e9ffd5dcb1af01ca6" Level="[SampleRateLevel]Fast" Units="[Unit]Hertz" Value="[double]1000" />
						<SampleTiming Id="84779f777dc54759b7830b618f947164" Level="[SampleRateLevel]Counter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="3769b6a0b9a342db8690bb7bca60c709" Level="[SampleRateLevel]LegacyCounter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="96fcc0f3ee1445dcaf602b7826b8fd4c" Level="[SampleRateLevel]Digital" Units="[Unit]Hertz" Value="[double]10" />
						<OnDemandTiming Id="f8ec7566c4574fa0bf32027eec9687a0" Level="[SampleRateLevel]OnDemand" />
					</TopLevelTimingOwner>
				</DAQmxProcessingElement>
				<AddonModel AddonCustomIconPath="[string]" AddonIcon="[AddonIconType]Input" AddonInstanceName="[string]CreateChannelsInProcess" AddonType="[string]94D4 1FA- F6F-6C4F-B623-8FBFB79085 1" DisplayName="[string]CreateChannelsInProcess" Id="6d6d93d1663c423eba835c08b36b8608" UserDisplayName="[string]CreateChannelsInProcess">
					<PeAddonOutputInfo CriticalAlarm="57d5334e89114538b19e8e9b18130518" DataType="[Type]@cad79fda0a10420d9bd8184e212e3b14" FullName="df60b754-abb5-442a-9a36-d6d3051ecb46" HasLiveData="[bool]False" Id="226ae14faa494264958e76027541ee96" SampleRate="[double]1" Source="LogEvents" Units="[string]" WarningAlarm="f49a83d910484553bf273c67c1bc394c">
						<Keyword Id="5bffef9c423f4261a2f1da88ff7a0d67" Name="DoNotTriggerChannel" />
						<AlarmModel Id="57d5334e89114538b19e8e9b18130518" Severity="[AlarmSeverity]Critical" TriggerModel="4cf1b37ead1f48118a62e5a1809c53ed">
							<ChannelMonitorTriggerModel Alias="[string]a9a4041a-19f5-4f70-965f-0f3240e3f44f" AliasToMonitor="[string]df60b754-abb5-442a-9a36-d6d3051ecb46" Id="4cf1b37ead1f48118a62e5a1809c53ed">
								<AboveValueTriggerModel Id="782ab171fdb04e56813bb14f3c2db2ce" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="f49a83d910484553bf273c67c1bc394c" Severity="[AlarmSeverity]Warning" TriggerModel="247af23a03524148aacb3e529fb1cb02">
							<ChannelMonitorTriggerModel Alias="[string]c1e7f925-4c3d-4fec-abee-606e73b05efc" AliasToMonitor="[string]df60b754-abb5-442a-9a36-d6d3051ecb46" Id="247af23a03524148aacb3e529fb1cb02">
								<AboveValueTriggerModel Id="984e8801dada45388838b95dff37af31" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo CanDisable="[bool]False" CriticalAlarm="67e9413267c44e6986ff605845f47825" DataType="[Type]Wfm(Double)" FullName="Channel 1" GroupName="[string]" Id="c755b3b07f7f4883b6bf8bd38bd6f28d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="1" Units="[string]" WarningAlarm="43c7c6f299354085a08d39b0f66bf3f3">
						<AlarmModel Enabled="[bool]True" Id="67e9413267c44e6986ff605845f47825" Severity="[AlarmSeverity]Critical" TriggerModel="261aa034258145668ff34f0b96a2ddf3">
							<ChannelMonitorTriggerModel Alias="[string]e68d88c1-3899-417e-a531-70e117c8b4f0" AliasToMonitor="[string]Channel 1" Hysteresis="[double]0" Id="261aa034258145668ff34f0b96a2ddf3">
								<AboveValueTriggerModel Id="b81dd51db35041deb852e605ed2d7bcb" Value="[double]10.7" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Enabled="[bool]True" Id="43c7c6f299354085a08d39b0f66bf3f3" Severity="[AlarmSeverity]Warning" TriggerModel="101b6f687bdb4206b3f09d95295fbc88">
							<ChannelMonitorTriggerModel Alias="[string]f153318f-fb84-452e-a578-ec59f9cde1e7" AliasToMonitor="[string]Channel 1" Id="101b6f687bdb4206b3f09d95295fbc88">
								<AboveValueTriggerModel Id="e3a2839dd5734c97a966eff703d82e20" Value="[double]10.5" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo CanDisable="[bool]False" CriticalAlarm="58c1ef0d41f04eabb47a738e5c07e33f" DataType="[Type]Wfm(Double)" FullName="Channel 2" GroupName="[string]" Id="199d591cbcf243f5b745ecd24e24fe48" InheritsTiming="[bool]False" SampleRate="[double]10" Source="2" Units="[string]" WarningAlarm="ab9e0f508bba435fb3b6dd5bb395e34a">
						<AlarmModel Id="58c1ef0d41f04eabb47a738e5c07e33f" Severity="[AlarmSeverity]Critical" TriggerModel="742dcc92424e4f398ef98ac676ef7b3f">
							<ChannelMonitorTriggerModel Alias="[string]1d5ae60c-0733-4407-9baa-c3b345003fee" AliasToMonitor="[string]Channel 2" Id="742dcc92424e4f398ef98ac676ef7b3f">
								<AboveValueTriggerModel Id="523525c25cc343fb83fc72616490130f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="ab9e0f508bba435fb3b6dd5bb395e34a" Severity="[AlarmSeverity]Warning" TriggerModel="7207860a112246dab8e7809461071c09">
							<ChannelMonitorTriggerModel Alias="[string]3f690740-8d87-4fd5-99d8-cc12d30561be" AliasToMonitor="[string]Channel 2" Id="7207860a112246dab8e7809461071c09">
								<AboveValueTriggerModel Id="29a9fbeb2ddc4ca28b830026bbbfc935" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
				</AddonModel>
				<ExternalTagProducerSubsystem Id="9a4dd850ce6c4900b2d842324967b1ae" />
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="d5b842f41fe848bc9d710961df17c7a0" />
	</ChannelSpecification>
	<DataTypeReferenceTable xmlns="http://www.ni.com/PlatformFramework">
		<p.TypeReference TypeId="cad79fda0a10420d9bd8184e212e3b14">
			<Composite Id="1" Name="" Cluster="" GenericTypeDefinition="Void" BaseType="Void">
				<Members>
					<Field FieldAccessPolicy="ReadWrite" Name="Name" DataType="String" />
					<Field FieldAccessPolicy="ReadWrite" Name="Value" DataType="@5ddb0e90d07f4d8d889e98c6bececd1e" />
				</Members>
			</Composite>
		</p.TypeReference>
		<p.TypeReference TypeId="5ddb0e90d07f4d8d889e98c6bececd1e">
			<Composite Id="1" Name="Variant" Sealed="" GenericTypeDefinition="Void" BaseType="Void" />
		</p.TypeReference>
	</DataTypeReferenceTable>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithAlarms/Logging Specification.flxcfg sha256=fddb763d259a0cf96d5e1a148092f10c71b4ae50f9090fc406c934c333a0257f bytes=2115 -->
## FILE: tests/assets/ProjectWithAlarms/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithAlarms/Logging Specification.flxcfg`
- sha256: `fddb763d259a0cf96d5e1a148092f10c71b4ae50f9090fc406c934c333a0257f`
- bytes: 2115

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="263CD0AB671914D1554780BF05A1A5AF61353ED8CC1C01C62966F60A2CCDE225934512F7F8FA989D50B7C08E25EF06C71BA5A6E98A665534B3DD15FC5A4A08B7" Timestamp="1D6A7CE9C51EF2F" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="3302b7bff24741518de43c1f1b01b360">
			<ProcessingElementModelOwner Id="58d7b6e35442424c8e242e40ebc662b1">
				<TriggeredLoggingProvider Id="600fb80409f64e15919a2e5ab48843f6" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-09-08T13:26:02.9171500999999999999691240037957840058879810385406017303466796875-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="769b2ab339c94bc5b3d2eafd4dc8151a" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="d5f250af140343559827266789a46971">
						<UserDefinedMetadataItem DataType="String" Id="1f88e6acb9df4161b6a766936fea66e1" Name="Operator">
							<p.Value>gstoll</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="445f9a4c5ea14ca2aab965b9961a70c4" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithAlarms/ProjectWithAlarms.flxproj sha256=031c8a0117dc4e58290bec7ed9606d155d5bf39c9b1f488daa56955e15085360 bytes=4475 -->
## FILE: tests/assets/ProjectWithAlarms/ProjectWithAlarms.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithAlarms/ProjectWithAlarms.flxproj`
- sha256: `031c8a0117dc4e58290bec7ed9606d155d5bf39c9b1f488daa56955e15085360`
- bytes: 4475

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D91119BBD554F4917823366D5148A09A5A0CC8C8DE03DA5FFFD7DDD195D2770A7EFA95FDA697C084FF61C4418B502639ECFCCA63E3BD886EEF2780CA24D0BE58" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="4d164a51a11a4ee4b424f02ecd260fa1" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="7a0c3a8cd754e59a1ca86fdeb31a048" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="10cdd026e8754ef991f232ebe1bcb1ec" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="3d4b9810fce047a9bab6dfc5f4f3a0f0" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="1856dfb213ab4db5a6d1dd8782d3170a" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="1b5ace284abf42519bb71f657d6224f0" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="b04ee3464b3c4e00a553b0f447d9a9c8" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="e290050e8154a50ab8c635e6408deb9" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="8c64b684b9714718adc95b4cfb22b727" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-09-08T18:26:03.0891549Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="c68155733ec4aaa8dbf1c5d94a873a9" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="ef75b5e88f7e45818e1625ab08beb05b" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="8d21fac64427474fb77d5e0b771e1abd" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithAlarms/Screen.flxscr sha256=d237f2a430bd4b52ac0a263396f14c91c3fe70713d7dba2fd59a6b69f6ab42bc bytes=1333 -->
## FILE: tests/assets/ProjectWithAlarms/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithAlarms/Screen.flxscr`
- sha256: `d237f2a430bd4b52ac0a263396f14c91c3fe70713d7dba2fd59a6b69f6ab42bc`
- bytes: 1333

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="5A78ED6E2625CF44E2E863554242599337B90CBCE3E27FD9BCAA0B4BDE1AB5762B2A1C997B7499EF55DCC101B047C1A237A074F368EAD7EF693D13DF8B1AAD65" Timestamp="1D6860E2690BB87" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="226e097e6644d5c8cf0e7f3c2544aa9" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="dd2872a6c4e149ae93032921ceeeb5f4" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithAlarms/Test Specification.flxtest sha256=7d530891f22428bc5496ee2909c5b6ace3d2ee023e2a3b27b227ac43220b8fe6 bytes=1053 -->
## FILE: tests/assets/ProjectWithAlarms/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithAlarms/Test Specification.flxtest`
- sha256: `7d530891f22428bc5496ee2909c5b6ace3d2ee023e2a3b27b227ac43220b8fe6`
- bytes: 1053

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FBE94BF7FAC8910B03E1CD72224A7AD76EA35967878B2D5D50B6FA1A36F6ABEFC02FE36CD6B0077365D5CD00801A02753F3AC0D425C77112A7922EBD607F63B7" Timestamp="1D6860E2690BB87" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="9f7000b6f74942f391ad04ece2a4221b">
			<ProcessingElementModelOwner Id="d4b11acefa1842cb8c72efdb7fada017" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithError/Channel Specification.flxio sha256=a7c7e4cd2cc5e029ac760fe4640d7191f1bce950c899d2c2754c7502c8e427f5 bytes=4475 -->
## FILE: tests/assets/ProjectWithError/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithError/Channel Specification.flxio`
- sha256: `a7c7e4cd2cc5e029ac760fe4640d7191f1bce950c899d2c2754c7502c8e427f5`
- bytes: 4475

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="7F92B1AA7857AE8C59499FC60B4DB57BA378DF21379D8E64691070A1E66ED2959BD0815E11AABD657D3990E9535DFDCE9FA1E57BCBB4EA81F941134E0FCCDA0B" Timestamp="1D65A079F2F5394" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1766" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="4c425b929f8842e1a3f1582cdc2e86aa">
			<ProcessingElementModelOwner Id="46b3f2a0b29a42a98c9abc0c4e4d077a">
				<SinewaveProvider Id="e647b19e3d3542ee85b1cd8c4779222e" ModelTypeId="[string]b5d5f126-935f-411f-9661-2fe99c581bf2">
					<ProviderParameter Id="2b000c5efe7468db5eaaf6934ef30ab" ParameterName="[string]Amplitude" Type="[Type]Double" Value="[double]1" />
					<ProviderParameter Id="5ba60435dbac4d09946a5a72a7eae096" ParameterName="[string]Frequency" Type="[Type]Double" Value="[double]0.5" />
					<ProviderParameter Id="5fcf5de3d0e0415fa0708e2b5a446b1b" ParameterName="[string]Phase" Type="[Type]Double" Value="[double]0" />
					<ProviderParameter Id="a86a106799bf4139a36a615ad0d5a211" ParameterName="[string]SampleRate" Type="[Type]Double" Value="[double]1000" />
					<ProviderParameter Id="d57c71ac92447f4b5bc8ffa2fe4b5b7" ParameterName="[string]TimeShift" Type="[Type]Double" Value="[double]0" />
					<ProviderParameter Id="8a6aac11798e41e0a0fade4d6e7ad580" ParameterName="[string]DriftFactor" Type="[Type]Double" Value="[double]1" />
					<SineWaveChannel Alias="sinewaveA" CriticalAlarm="a02ce1109a0a41dbaf73c1399680cd34" DataType="[Type]Wfm(Double)" Id="9c3e74e4a6b841189f623c0866d3b438" SampleRate="[double]1000" Source="Output/sineA" Units="[string]V" WarningAlarm="42d630f061e440b1849c0c822818c591">
						<AlarmModel Id="42d630f061e440b1849c0c822818c591" Severity="[AlarmSeverity]Warning" TriggerModel="af2b71f3dc884996aad81120509a66e0">
							<ChannelMonitorTriggerModel Alias="[string]51f0bb3d-faa9-4ccd-8dd1-66bcc6d2525e" AliasToMonitor="[string]sinewaveA" Id="af2b71f3dc884996aad81120509a66e0">
								<AboveValueTriggerModel Id="1f6c21396aab44de862e98bdc82aa3f1" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="a02ce1109a0a41dbaf73c1399680cd34" Severity="[AlarmSeverity]Critical" TriggerModel="f9ef9842cbb846ad86f2173b193c33e4">
							<ChannelMonitorTriggerModel Alias="[string]008fade2-e9b8-4ff1-8efd-0f8ee017fd1f" AliasToMonitor="[string]sinewaveA" Id="f9ef9842cbb846ad86f2173b193c33e4">
								<AboveValueTriggerModel Id="d49faba6054345ac90e3f782935f1f0e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</SineWaveChannel>
					<SineWaveChannel Alias="sinewaveB" CriticalAlarm="52ceb896226048b1a5c4c716fc5bdf0d" DataType="[Type]Wfm(Double)" Id="fa5461c65f824fe9962b2818e4129ddf" SampleRate="[double]1000" Source="Output/sineB" Units="[string]V" WarningAlarm="4f6c15ef3a2d43b096e0ec72053aaca4">
						<AlarmModel Id="4f6c15ef3a2d43b096e0ec72053aaca4" Severity="[AlarmSeverity]Warning" TriggerModel="f19630417724930b4eb65c700caf99d">
							<ChannelMonitorTriggerModel Alias="[string]11b6ebc0-1aea-497e-af7d-0d3b41c4d766" AliasToMonitor="[string]sinewaveB" Id="f19630417724930b4eb65c700caf99d">
								<AboveValueTriggerModel Id="c88d702cc964e7eada2fca19192a259" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="52ceb896226048b1a5c4c716fc5bdf0d" Severity="[AlarmSeverity]Critical" TriggerModel="84883b4ff24747b69ed9c6fbb3a2b281">
							<ChannelMonitorTriggerModel Alias="[string]e6da330a-79c6-465b-9fb3-9b914640082e" AliasToMonitor="[string]sinewaveB" Id="84883b4ff24747b69ed9c6fbb3a2b281">
								<AboveValueTriggerModel Id="2d2639ca027942beb819e3ef5910bf7f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</SineWaveChannel>
				</SinewaveProvider>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="d99723bd5f174c98b72e9521d14e7edd" />
	</ChannelSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithError/Logging Specification.flxcfg sha256=f6a2607fba99371340764038e931669433aa93fa3a3f143089068c087ad5dcf2 bytes=2191 -->
## FILE: tests/assets/ProjectWithError/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithError/Logging Specification.flxcfg`
- sha256: `f6a2607fba99371340764038e931669433aa93fa3a3f143089068c087ad5dcf2`
- bytes: 2191

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="5D04A29882F562D2222C7C8D963F997C2ED0E3DAB67018886685548FD395A45AD536F4C13E7EEFC9BAAB9D7EC67AF26E1295A972706F8581208DE1E9FC8C5B19" Timestamp="1D6A7CDAAE38B64" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="353c04c2ae9f4519b13028ec43537c68">
			<ProcessingElementModelOwner Id="713e065d92f647b28fabf928df2c0543">
				<TriggeredLoggingProvider Id="9e08b3d7e50746f1accd8be05de7e3ea" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-07-14T12:50:17.1458097999999999999881476753227360632081399671733379364013671875-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="e540217840df497ea1cf1c8a19f8f336" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" LogFileName="LogFile_{YYear}-{Month}-{Day}-{Hour}-{Minute}-{Second}.tdms" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="b760487bf6244d26b64c85b51f4062dc">
						<UserDefinedMetadataItem DataType="String" Id="d251676e4abc4988813cd72e80014a93" Name="Operator">
							<p.Value>bparrott</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="b40cf6d3d7ef49429a6cda96f1853b51" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithError/ProjectWithError.flxproj sha256=6a8bce6c18ea2583ed704879d1763e95a4b28e339a0fdcb85e287c8814c0da06 bytes=4572 -->
## FILE: tests/assets/ProjectWithError/ProjectWithError.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithError/ProjectWithError.flxproj`
- sha256: `6a8bce6c18ea2583ed704879d1763e95a4b28e339a0fdcb85e287c8814c0da06`
- bytes: 4572

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="EF94F5299DD9284C094E8915EF16E55222B3D4EF5B42F16A04F2121F2C965BBF716E6BDF9AA38A0B0E790FFC6C47D05186E4F52118ABAC9989E2130A2650A627" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1766" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="4ff5fce681664b52943ba1b55b0a42f5" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="8b8537a66b404387ae6eb40211dfb6b0" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="cb021378605b433aab6ac3d2d99c4f8c" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="cedcc559bb5147268d1254f2f69bea0f" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="f7601d6c02004fe58dedc9de585dd0ab" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="3ef84d96be7d496088fa40b70a107ae8" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="ab20acbb9378411cbed9c103453159e6" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="b5e19e54749c41f19d7005d0518a2c0c" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="24ff5449704fc1be2f12a3d0c74270" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="b54a67bbbd4c4418aca56630d9136d7a" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="46e05de524e54c90b3c7b047526b06e9" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="519eae31e7e14b69a36ca92b1a7f2d27" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-07-14T17:50:17.1767272Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="a9df951961bc41e38ff93f578f9e0d43" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="4dda3f3ea352499c973f43e6c79a9c6b" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="978717e277184a408101ee0b03f3a508" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithError/Screen.flxscr sha256=971b9def58309d6ba431fb7292a4d4a5678d915d9e79fb482186481620cf33e7 bytes=1338 -->
## FILE: tests/assets/ProjectWithError/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithError/Screen.flxscr`
- sha256: `971b9def58309d6ba431fb7292a4d4a5678d915d9e79fb482186481620cf33e7`
- bytes: 1338

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="99F87C094A86B60945F63BF221FEC089463D76DA94262139A37366A0C38A11A951291639D1D774E094E5CE71A3FB64ABA6B6C11050E9DD880A0CC5BE4B56D294" Timestamp="1D65A079F2F7A89" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1766" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="8fea3acbe8e94169b589e1b4d2b6c6fb" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="e0ef0c150be34166ac638d11b1ef8caf" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithError/Test Specification.flxtest sha256=64a71ff3ba11fe4c53422fcbd0e9cc83e0f248dff778b2c33aec25c447354932 bytes=1056 -->
## FILE: tests/assets/ProjectWithError/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithError/Test Specification.flxtest`
- sha256: `64a71ff3ba11fe4c53422fcbd0e9cc83e0f248dff778b2c33aec25c447354932`
- bytes: 1056

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="EEC3228D4CF63A75CEC1CC51C4A927599DED132E3024141EAC96DB62BFCAE2B13D1AA53551CD53AB36CEE1A413EF00F687312546EC9B09979B56D573F5304EC6" Timestamp="1D65A079F2F7A89" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.1766" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.1766" Name="FlexLogger" Version="20.2.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="52b5ad20dd77496e8f9ace026d6c3631">
			<ProcessingElementModelOwner Id="d01c73fe0517430f9eb271d2a608613b" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithLoggingSpecification/Channel Specification.flxio sha256=da538b5c9655dcdca406cc74850e31cfb910e74626c2012c6173aaeff705c383 bytes=13977 -->
## FILE: tests/assets/ProjectWithLoggingSpecification/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithLoggingSpecification/Channel Specification.flxio`
- sha256: `da538b5c9655dcdca406cc74850e31cfb910e74626c2012c6173aaeff705c383`
- bytes: 13977

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="8AEB1AA2F7E72084A97C19B685C2BECAF7129D4B8FBF5EC683B5A983D4489D0C0A1B2A84FD7C4712C9DE1656C223EAD1F47F8C4791162CB59B429BEE9913BE84" Timestamp="1D9EA8207431C98" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.10.0.2344" FeatureSetName="FlexLogger DAQmx" Name="http://www.ni.com/FlexLogger/DAQmx" OldestCompatibleVersion="9.9.0.49152" Version="9.9.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.2555" FeatureSetName="FlexLogger XNET" Name="http://www.ni.com/FlexLogger/XNET" OldestCompatibleVersion="9.3.0.49152" Version="9.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.2555" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="9.10.0.1" Version="9.10.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.2546" FeatureSetName="Calculated Channels" Name="http://www.ni.com/Lumberjack.Providers.CalculatedChannel" OldestCompatibleVersion="9.0.0.49152" Version="9.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.2546" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="9.10.0.2344" Name="FlexLogger" Version="23.6.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="982c173af0c64610a860339d38593bba">
			<ProcessingElementModelOwner Id="b1ec8a4469ce43ac85568173c0792594">
				<DAQmxProcessingElement Id="f732e335e0da4813a1615b96032f4de9" xmlns="http://www.ni.com/FlexLogger/DAQmx">
					<TopLevelTimingOwner FallbackMediumSampleRateLevel="[SampleRateLevel]Fast" Id="cac4e49a71224eb9bd4dbcc353e236aa">
						<SampleTiming Id="918ea797ca824fd3a05c23a657757219" Level="[SampleRateLevel]Slow" Units="[Unit]Hertz" Value="[double]1" />
						<SampleTiming Id="2f302cbd01a94f2a80fbe37726e91030" Level="[SampleRateLevel]Medium" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="c6101757da594484b3c21041bc845fe9" Level="[SampleRateLevel]Fast" Units="[Unit]Hertz" Value="[double]1000" />
						<SampleTiming Id="7ad873c108104154b0d61f40a438aeab" Level="[SampleRateLevel]Counter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="a2c36c356af34115b9d6825ac7f4fc20" Level="[SampleRateLevel]LegacyCounter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="814122c312aa4893a2481f15bcb5bd74" Level="[SampleRateLevel]Digital" Units="[Unit]Hertz" Value="[double]10" />
						<OnDemandTiming Id="930f7580a3a54932a0b7431eb8c0d42c" Level="[SampleRateLevel]OnDemand" />
						<SampleTiming Id="b8a327accf245468f3a40413ebf50c7" Level="[SampleRateLevel]AnalogOutput" Units="[Unit]Hertz" Value="[double]10" />
					</TopLevelTimingOwner>
				</DAQmxProcessingElement>
				<XnetPortModel CustomBaudrates="" CustomFdBaudrates="" Id="9a0e3949051d45778312e35e5f6ca7f5" PhysicalPort="[string]NI 9862/Port1" ProcessingElementName="[string]CAN2" TransceiverCapability="HighSpeed" xmlns="http://www.ni.com/FlexLogger/XNET">
					<XnetProcessingElementParameter Id="de237e0c20144a268e6c4ad66804228b" ParameterName="[string]Settings JSON" Type="[Type]String" Value="[string]" />
					<XnetCommunicationStatusOutputInfo CriticalAlarm="33429444b3814f69b886a58bcd4d3990" DataType="[Type]String" FullName="CAN2 Communication status" Id="969986e2db5040c08cc08fc2a1a1466b" LoggingDisabled="[bool]True" SampleRate="[double]100" Source="Output" Units="[string]" WarningAlarm="936802351e344aaa83e2f18958110981">
						<AlarmModel Id="936802351e344aaa83e2f18958110981" Severity="[AlarmSeverity]Warning" TriggerModel="a38c67e5dd494786844d11d3cefd3bf9" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]c7d4ce04-a8b5-4d0c-8b23-196ea05f175b" AliasToMonitor="[string]CAN2 Communication status" Id="a38c67e5dd494786844d11d3cefd3bf9">
								<AboveValueTriggerModel Id="c9d3f08db394b9c99cca9126726d00d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="33429444b3814f69b886a58bcd4d3990" Severity="[AlarmSeverity]Critical" TriggerModel="ec802cd73bd44e27aad4ae7724a42076" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]4f192af7-52c9-4c33-8ebb-4aec8016f85b" AliasToMonitor="[string]CAN2 Communication status" Id="ec802cd73bd44e27aad4ae7724a42076">
								<AboveValueTriggerModel Id="64676854e70b4513a5338cf3f0f775bd" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetCommunicationStatusOutputInfo>
					<XnetRawFrameOutputInfo CriticalAlarm="33cef1fccf554a71833ee9e6a14523c6" DataType="[Type]Wfm(UInt8)" FullName="CAN2 Raw Logging" Id="7906228e6504a4a9e03f8ac0728b242" SampleRate="[double]100" Source="Raw" Units="[string]" WarningAlarm="89f8c3ef08df4af3bc766e4cfa736e37">
						<AlarmModel Id="89f8c3ef08df4af3bc766e4cfa736e37" Severity="[AlarmSeverity]Warning" TriggerModel="19385343aef844e5922d54e63ab16bcc" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]58622ddb-1261-460f-8785-05a171e406a4" AliasToMonitor="[string]CAN2 Raw Logging" Id="19385343aef844e5922d54e63ab16bcc">
								<AboveValueTriggerModel Id="dabc371b5da348aaa35ff32269dd31b3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="33cef1fccf554a71833ee9e6a14523c6" Severity="[AlarmSeverity]Critical" TriggerModel="a7297e0dd25e4b6e9335c4c284e9ea2b" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]969edd1b-6679-42be-b50d-705303dbb7f9" AliasToMonitor="[string]CAN2 Raw Logging" Id="a7297e0dd25e4b6e9335c4c284e9ea2b">
								<AboveValueTriggerModel Id="d07914e33761410d95653006989f03e9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetRawFrameOutputInfo>
					<XnetRawFrameInputInfo FullName="Raw Frame Input" Id="dfc27bb4b7b44f4a31acc7dcb2667b8" Source="Input" />
					<XnetBusStatisticsOutputInfo CriticalAlarm="ff75765c4b3d44b78f8d549668061b06" DataType="[Type]String" FullName="CAN2 Bus Statistics" Id="5186e3b9aeb7450ea82a71304f31c0ea" LoggingDisabled="[bool]True" SampleRate="[double]100" Source="Output" Units="[string]" WarningAlarm="5d471e7f1e6499d9e0030089511ac4f">
						<AlarmModel Id="5d471e7f1e6499d9e0030089511ac4f" Severity="[AlarmSeverity]Warning" TriggerModel="e9a1a1da228442619d686f4026c3df66" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]764cf632-8c0a-41a9-b2a9-8e94a9909def" AliasToMonitor="[string]CAN2 Bus Statistics" Id="e9a1a1da228442619d686f4026c3df66">
								<AboveValueTriggerModel Id="f89b2bdad7ad48e9afe1a8aae3b0ff31" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="ff75765c4b3d44b78f8d549668061b06" Severity="[AlarmSeverity]Critical" TriggerModel="9367fd495b894390b948d41b231b7064" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]7fcfe7c3-5c5b-40c6-a980-76e7e2556837" AliasToMonitor="[string]CAN2 Bus Statistics" Id="9367fd495b894390b948d41b231b7064">
								<AboveValueTriggerModel Id="e81785aefdd4c9ca798f43a4d9d492a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetBusStatisticsOutputInfo>
				</XnetPortModel>
				<XnetPortModel CustomBaudrates="" CustomFdBaudrates="" Id="922622767c0e41a5abac5dc7bfe4659a" PhysicalPort="[string]NI 9862/Port1" ProcessingElementName="[string]CAN1" TransceiverCapability="HighSpeed" xmlns="http://www.ni.com/FlexLogger/XNET">
					<XnetProcessingElementParameter Id="844fbd75a6134f57a0cd575893648a96" ParameterName="[string]Settings JSON" Type="[Type]String" Value="[string]" />
					<XnetCommunicationStatusOutputInfo CriticalAlarm="bb0aff2fa4e146909297dbaace1c974a" DataType="[Type]String" FullName="CAN1 Communication status" Id="8c1bc5be5ee349a9890c376d8c8e68ed" LoggingDisabled="[bool]True" SampleRate="[double]100" Source="Output" Units="[string]" WarningAlarm="a8ed13e0d2a44cfb8c35e10f5813360a">
						<AlarmModel Id="a8ed13e0d2a44cfb8c35e10f5813360a" Severity="[AlarmSeverity]Warning" TriggerModel="a6b4f09438824ef1a4c30613256e9774" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]8e574fb1-b70f-4bf6-9212-d9c260c9c3cf" AliasToMonitor="[string]CAN1 Communication status" Id="a6b4f09438824ef1a4c30613256e9774">
								<AboveValueTriggerModel Id="25eee30ac56a4ae68a7280553fe76ebf" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="bb0aff2fa4e146909297dbaace1c974a" Severity="[AlarmSeverity]Critical" TriggerModel="dddc8f90b5564bae89cf02be5fc233e2" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]3ecf6ed0-e054-40e8-96eb-4bfeee46fed6" AliasToMonitor="[string]CAN1 Communication status" Id="dddc8f90b5564bae89cf02be5fc233e2">
								<AboveValueTriggerModel Id="306d3f7c76664948b7815571c0d78b03" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetCommunicationStatusOutputInfo>
					<XnetRawFrameOutputInfo CriticalAlarm="eedcb03dec4a4b8b83ec932e10c7e4a3" DataType="[Type]Wfm(UInt8)" FullName="CAN1 Raw Logging" Id="cf52f8d3a1864222b14416cd722760a6" SampleRate="[double]100" Source="Raw" Units="[string]" WarningAlarm="e12948c2ddc46a6bcb9a204a4c9cec4">
						<AlarmModel Id="e12948c2ddc46a6bcb9a204a4c9cec4" Severity="[AlarmSeverity]Warning" TriggerModel="ef52d23fc986487ea2dbd8336e266105" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]fc88c48b-580a-4b24-ac11-3565679ffabd" AliasToMonitor="[string]CAN1 Raw Logging" Id="ef52d23fc986487ea2dbd8336e266105">
								<AboveValueTriggerModel Id="587c199336754808ade8ce75f3083fcf" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="eedcb03dec4a4b8b83ec932e10c7e4a3" Severity="[AlarmSeverity]Critical" TriggerModel="dce5bb9c418b4315b6fe4cf0ac64ae2d" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]610e36ad-fb74-4d8e-8ec3-18cb778c2edb" AliasToMonitor="[string]CAN1 Raw Logging" Id="dce5bb9c418b4315b6fe4cf0ac64ae2d">
								<AboveValueTriggerModel Id="738cd3a9e6ac4292860c8ae8d6420fa4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetRawFrameOutputInfo>
					<XnetRawFrameInputInfo FullName="Raw Frame Input_1" Id="8902e1d1e42046af866859d9b0db3b64" Source="Input" />
					<XnetBusStatisticsOutputInfo CriticalAlarm="d5744887533c40a38ab23fe920d9a285" DataType="[Type]String" FullName="CAN1 Bus Statistics" Id="cc10dc720b814b35860ef75a6880763c" LoggingDisabled="[bool]True" SampleRate="[double]100" Source="Output" Units="[string]" WarningAlarm="8e5a830c3294400db5e2d189aa7cf7f3">
						<AlarmModel Id="8e5a830c3294400db5e2d189aa7cf7f3" Severity="[AlarmSeverity]Warning" TriggerModel="fe70882a25ea4a62b12adc112bb2991f" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]4990c2e4-bdd4-48d2-999b-a18c7230915b" AliasToMonitor="[string]CAN1 Bus Statistics" Id="fe70882a25ea4a62b12adc112bb2991f">
								<AboveValueTriggerModel Id="638c9023c8c347e89f5c0624aa11bd60" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="d5744887533c40a38ab23fe920d9a285" Severity="[AlarmSeverity]Critical" TriggerModel="7bb53caa0e8449a0863529c41403687b" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]5faaf52c-e70b-4263-88cc-3b110c217018" AliasToMonitor="[string]CAN1 Bus Statistics" Id="7bb53caa0e8449a0863529c41403687b">
								<AboveValueTriggerModel Id="cce9d4f1749b44c5ba757a0aadded4e4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</XnetBusStatisticsOutputInfo>
				</XnetPortModel>
				<VariableProvider Id="aabc3acc0aea40138f23718b1c4b03ef" ModelTypeId="[string]EAE65B83-4518-45A9-AA71-7A049C2B2563" xmlns="http://www.ni.com/Lumberjack.Providers.CalculatedChannel">
					<VariableConsumer AssociatedProducer="[string]Variable.producer" FullName="Variable" Id="d9673fca91aa4ed890e9898d40dc55f3" MappingAlias="[string]e97b80e5-bc3b-40d0-a59d-8160e7f7fc85">
						<SupportedDataType xmlns="http://www.ni.com/Lumberjack.Core" />
					</VariableConsumer>
					<VariableProducer CriticalAlarm="58e01ebb3f0d4e06ad613f697fec83a2" DataType="[Type]Double" FullName="Variable.producer" Id="23f2bed9c7d64395b8c91d6507a96da5" SampleRate="[double]100" Units="[string]" WarningAlarm="a132890f99294009963c68b86f385063">
						<AlarmModel Id="a132890f99294009963c68b86f385063" Severity="[AlarmSeverity]Warning" TriggerModel="bc92babcfbf046cd9bffd29c1ab8baa4" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]81011ad1-f45c-40ea-8544-0a78334ab999" AliasToMonitor="[string]Variable.producer" Id="bc92babcfbf046cd9bffd29c1ab8baa4">
								<AboveValueTriggerModel Id="98f016ac8b374e8985dc7620b2eb4900" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="58e01ebb3f0d4e06ad613f697fec83a2" Severity="[AlarmSeverity]Critical" TriggerModel="d19c4bfc523b4fb6a3eab93c45cac9ba" xmlns="http://www.ni.com/Lumberjack.Core">
							<ChannelMonitorTriggerModel Alias="[string]28808622-03e0-4f60-8229-eac7978969a6" AliasToMonitor="[string]Variable.producer" Id="d19c4bfc523b4fb6a3eab93c45cac9ba">
								<AboveValueTriggerModel Id="25781e0c2e35426b9bc0e4abb9bb0c42" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<Keyword Id="25c0872c07a7403e84296255f3266372" Name="NotPublicToSystemLink" xmlns="http://www.ni.com/Lumberjack.Core" />
					</VariableProducer>
				</VariableProvider>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="462b641e98e04963bf760b558012bc65" />
	</ChannelSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithLoggingSpecification/Logging Specification.flxcfg sha256=f401972b6b3cf7b08a9fdc1ca70c297e00ae288fc734ec904efa9a9d1d7b5871 bytes=2173 -->
## FILE: tests/assets/ProjectWithLoggingSpecification/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithLoggingSpecification/Logging Specification.flxcfg`
- sha256: `f401972b6b3cf7b08a9fdc1ca70c297e00ae288fc734ec904efa9a9d1d7b5871`
- bytes: 2173

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D683DC20688C6F7507CD9790605353F3EAB65D82993FDFAEBBD45D660903FF14EB8254B1FB4E8E938A7B0625082C552071C918DC6DF155B958D4D9ABB3764736" Timestamp="1D94DB50B56411F" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.8.0.613" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="9.6.0.49152" Version="9.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.613" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="9.8.0.613" Name="FlexLogger" Version="23.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="3b412b908301474587f70def16479b5b">
			<ProcessingElementModelOwner Id="646caa43f52446f7b6cf39e7b9d1088a">
				<TriggeredLoggingProvider Id="72313a7a17de4ed6bb1b93b0e6f8099e" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-07-30T00:12:02.774938699999999999951973139733496509506949223577976226806640625+02:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="19fe41c4dd6f4802a31edc115012cdc0" LogFileBackupPath="&quot;C:\\Users\\peteri\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\MyDataGoesHere&quot;" LogFileDescription="This is the description of the log file." LogFileName="MyData.tdms" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="894f64eb8d574af2949ab9dd4b5f0764">
						<UserDefinedMetadataItem DataType="String" Id="ca719d29575b42e99c5549d5847196a2" Name="Operator">
							<p.Value>bparrott</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="7b2083669202430784a7c3064821fbbe" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithLoggingSpecification/ProjectWithLoggingSpecification.flxproj sha256=a4cbd7af70abab949dccfc8cb0e3445ffe8240b7b457871aaacbe8dfae43c80c bytes=4481 -->
## FILE: tests/assets/ProjectWithLoggingSpecification/ProjectWithLoggingSpecification.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithLoggingSpecification/ProjectWithLoggingSpecification.flxproj`
- sha256: `a4cbd7af70abab949dccfc8cb0e3445ffe8240b7b457871aaacbe8dfae43c80c`
- bytes: 4481

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="33CC1F25C8FB983C6BF754627FDD49F2D8B788F190F9276EC3A2C9AD75087780910DD93AE4F6F1162DEBCBC0A21D36909FEA51E761237DF9225175AD16BBEEE5" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="89f9c53e7d174c7689ab21264e0581bd" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="4a6d22540bb44d6c9bf3ba6de5151677" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="1c22a02a8942450994d414e5ca4f6076" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="898f09f8bba04f0d9304743df7037f70" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="15385452ae3746e2adf9319d11b9547e" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="54c96f5f41864ae0882d6795c96e9c3c" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="a915aaf7f5f94d629ba466ba3cabb1aa" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="2dac4de3c93642e3b3eaa12abb0d5c87" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="631a8af96dc74b0d98feb485a5ed1a5e" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-07-29T22:12:03.2716109Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="cfef4d137b7e4640ba5030ec47a84a20" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="d69e12d4e10643d492b24d8fc51dfd11" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="af3bd49958104a6a906c5d96598caa7c" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithLoggingSpecification/Screen.flxscr sha256=4431c8112a38f422ace2a30bfed69ac270c68cce29c4bb80abbb990458dae9a6 bytes=1337 -->
## FILE: tests/assets/ProjectWithLoggingSpecification/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithLoggingSpecification/Screen.flxscr`
- sha256: `4431c8112a38f422ace2a30bfed69ac270c68cce29c4bb80abbb990458dae9a6`
- bytes: 1337

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="7763EFA61E0C518EFBF87CF4BF5C460D08519EBE58F77605DC49D3E1B6DC833DA81941FB7F5A7937B927987FED5A555053F8299F4CCBB4C4D88565BE44000BC8" Timestamp="1D665F58F6AD0C1" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="c806897bf1b43b88d7363318964dbf2" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="bdf00b46bfeb4a03adc47fb2860f9658" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithLoggingSpecification/Test Specification.flxtest sha256=12def231bb5eb8c7d969c5591ca3fb45442bc4b97ce8aa5300bed6f4e8ac07f7 bytes=1056 -->
## FILE: tests/assets/ProjectWithLoggingSpecification/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithLoggingSpecification/Test Specification.flxtest`
- sha256: `12def231bb5eb8c7d969c5591ca3fb45442bc4b97ce8aa5300bed6f4e8ac07f7`
- bytes: 1056

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="59E5B89FF3A85F342F6181EE21FF5855A32F0323C187642357DF47B99E5F965950532BDAD18BE12352BB3F120C94C97882D8B99F71EA1B2A3F19297CB86F9EE6" Timestamp="1D665F58F6AD0C1" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="b951f110508b4abf8934924342c43272">
			<ProcessingElementModelOwner Id="508cbaf6bffe46ee828eabf3449934fd" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithProducedData/Channel Specification.flxio sha256=01040f5f9853679f41736d108052207979bc55023e07dcf88d182e2565bb0e48 bytes=7421 -->
## FILE: tests/assets/ProjectWithProducedData/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithProducedData/Channel Specification.flxio`
- sha256: `01040f5f9853679f41736d108052207979bc55023e07dcf88d182e2565bb0e48`
- bytes: 7421

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="944BECF1021FD8BCF01658E2F88EEBDE90263B7E49C5FC4D385179F669E67D2C07E8D53970DD901A3774647299140D4739442EECD66AD2018D8CBD17627DB7AE" Timestamp="1D6860E268EE7DF" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="FlexLogger DAQmx" Name="http://www.ni.com/FlexLogger/DAQmx" OldestCompatibleVersion="8.3.0.49152" Version="8.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="fc63b6cee1b340bfb2a6c781cde271d3">
			<ProcessingElementModelOwner Id="62952760ce434f7cb9fb2d555c32b701">
				<DAQmxProcessingElement Id="7987c8c20a1744408a3df1b7b3402235" xmlns="http://www.ni.com/FlexLogger/DAQmx">
					<TopLevelTimingOwner FallbackMediumSampleRateLevel="[SampleRateLevel]Fast" Id="98ebabbd86b84e1ebd25a76b9957efaa">
						<SampleTiming Id="80421f3882cc412397c3716a4396e967" Level="[SampleRateLevel]Slow" Units="[Unit]Hertz" Value="[double]1" />
						<SampleTiming Id="29421b77d86147f6ae9c2cd50990ddd6" Level="[SampleRateLevel]Medium" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="da7296c7375b445e9ffd5dcb1af01ca6" Level="[SampleRateLevel]Fast" Units="[Unit]Hertz" Value="[double]1000" />
						<SampleTiming Id="84779f777dc54759b7830b618f947164" Level="[SampleRateLevel]Counter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="3769b6a0b9a342db8690bb7bca60c709" Level="[SampleRateLevel]LegacyCounter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="96fcc0f3ee1445dcaf602b7826b8fd4c" Level="[SampleRateLevel]Digital" Units="[Unit]Hertz" Value="[double]10" />
						<OnDemandTiming Id="f8ec7566c4574fa0bf32027eec9687a0" Level="[SampleRateLevel]OnDemand" />
					</TopLevelTimingOwner>
				</DAQmxProcessingElement>
				<AddonModel AddonCustomIconPath="[string]" AddonIcon="[AddonIconType]Input" AddonInstanceName="[string]CreateChannelsInProcess" AddonType="[string]94D4 1FA- F6F-6C4F-B623-8FBFB79085 1" DisplayName="[string]CreateChannelsInProcess" Id="6d6d93d1663c423eba835c08b36b8608" UserDisplayName="[string]CreateChannelsInProcess">
					<PeAddonOutputInfo Alias="df60b754-abb5-442a-9a36-d6d3051ecb46" CriticalAlarm="57d5334e89114538b19e8e9b18130518" DataType="[Type]@cad79fda0a10420d9bd8184e212e3b14" HasLiveData="[bool]False" Id="226ae14faa494264958e76027541ee96" SampleRate="[double]1" Source="LogEvents" Units="[string]" WarningAlarm="f49a83d910484553bf273c67c1bc394c">
						<AlarmModel Id="f49a83d910484553bf273c67c1bc394c" Severity="[AlarmSeverity]Warning" TriggerModel="247af23a03524148aacb3e529fb1cb02">
							<ChannelMonitorTriggerModel Alias="[string]c1e7f925-4c3d-4fec-abee-606e73b05efc" AliasToMonitor="[string]df60b754-abb5-442a-9a36-d6d3051ecb46" Id="247af23a03524148aacb3e529fb1cb02">
								<AboveValueTriggerModel Id="984e8801dada45388838b95dff37af31" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="57d5334e89114538b19e8e9b18130518" Severity="[AlarmSeverity]Critical" TriggerModel="4cf1b37ead1f48118a62e5a1809c53ed">
							<ChannelMonitorTriggerModel Alias="[string]a9a4041a-19f5-4f70-965f-0f3240e3f44f" AliasToMonitor="[string]df60b754-abb5-442a-9a36-d6d3051ecb46" Id="4cf1b37ead1f48118a62e5a1809c53ed">
								<AboveValueTriggerModel Id="782ab171fdb04e56813bb14f3c2db2ce" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<Keyword Id="5bffef9c423f4261a2f1da88ff7a0d67" Name="DoNotTriggerChannel" />
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Channel 1" CanDisable="[bool]False" CriticalAlarm="67e9413267c44e6986ff605845f47825" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c755b3b07f7f4883b6bf8bd38bd6f28d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="1" Units="[string]" WarningAlarm="43c7c6f299354085a08d39b0f66bf3f3">
						<AlarmModel Id="43c7c6f299354085a08d39b0f66bf3f3" Severity="[AlarmSeverity]Warning" TriggerModel="101b6f687bdb4206b3f09d95295fbc88">
							<ChannelMonitorTriggerModel Alias="[string]f153318f-fb84-452e-a578-ec59f9cde1e7" AliasToMonitor="[string]Channel 1" Id="101b6f687bdb4206b3f09d95295fbc88">
								<AboveValueTriggerModel Id="e3a2839dd5734c97a966eff703d82e20" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="67e9413267c44e6986ff605845f47825" Severity="[AlarmSeverity]Critical" TriggerModel="261aa034258145668ff34f0b96a2ddf3">
							<ChannelMonitorTriggerModel Alias="[string]e68d88c1-3899-417e-a531-70e117c8b4f0" AliasToMonitor="[string]Channel 1" Id="261aa034258145668ff34f0b96a2ddf3">
								<AboveValueTriggerModel Id="b81dd51db35041deb852e605ed2d7bcb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Channel 2" CanDisable="[bool]False" CriticalAlarm="58c1ef0d41f04eabb47a738e5c07e33f" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="199d591cbcf243f5b745ecd24e24fe48" InheritsTiming="[bool]False" SampleRate="[double]10" Source="2" Units="[string]" WarningAlarm="ab9e0f508bba435fb3b6dd5bb395e34a">
						<AlarmModel Id="ab9e0f508bba435fb3b6dd5bb395e34a" Severity="[AlarmSeverity]Warning" TriggerModel="7207860a112246dab8e7809461071c09">
							<ChannelMonitorTriggerModel Alias="[string]3f690740-8d87-4fd5-99d8-cc12d30561be" AliasToMonitor="[string]Channel 2" Id="7207860a112246dab8e7809461071c09">
								<AboveValueTriggerModel Id="29a9fbeb2ddc4ca28b830026bbbfc935" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="58c1ef0d41f04eabb47a738e5c07e33f" Severity="[AlarmSeverity]Critical" TriggerModel="742dcc92424e4f398ef98ac676ef7b3f">
							<ChannelMonitorTriggerModel Alias="[string]1d5ae60c-0733-4407-9baa-c3b345003fee" AliasToMonitor="[string]Channel 2" Id="742dcc92424e4f398ef98ac676ef7b3f">
								<AboveValueTriggerModel Id="523525c25cc343fb83fc72616490130f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
				</AddonModel>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="d5b842f41fe848bc9d710961df17c7a0" />
	</ChannelSpecification>
	<DataTypeReferenceTable xmlns="http://www.ni.com/PlatformFramework">
		<p.TypeReference TypeId="cad79fda0a10420d9bd8184e212e3b14">
			<Composite Id="1" Name="" Cluster="" GenericTypeDefinition="Void" BaseType="Void">
				<Members>
					<Field FieldAccessPolicy="ReadWrite" Name="Name" DataType="String" />
					<Field FieldAccessPolicy="ReadWrite" Name="Value" DataType="@5ddb0e90d07f4d8d889e98c6bececd1e" />
				</Members>
			</Composite>
		</p.TypeReference>
		<p.TypeReference TypeId="5ddb0e90d07f4d8d889e98c6bececd1e">
			<Composite Id="1" Name="Variant" Sealed="" GenericTypeDefinition="Void" BaseType="Void" />
		</p.TypeReference>
	</DataTypeReferenceTable>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithProducedData/Logging Specification.flxcfg sha256=fddb763d259a0cf96d5e1a148092f10c71b4ae50f9090fc406c934c333a0257f bytes=2115 -->
## FILE: tests/assets/ProjectWithProducedData/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithProducedData/Logging Specification.flxcfg`
- sha256: `fddb763d259a0cf96d5e1a148092f10c71b4ae50f9090fc406c934c333a0257f`
- bytes: 2115

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="263CD0AB671914D1554780BF05A1A5AF61353ED8CC1C01C62966F60A2CCDE225934512F7F8FA989D50B7C08E25EF06C71BA5A6E98A665534B3DD15FC5A4A08B7" Timestamp="1D6A7CE9C51EF2F" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="3302b7bff24741518de43c1f1b01b360">
			<ProcessingElementModelOwner Id="58d7b6e35442424c8e242e40ebc662b1">
				<TriggeredLoggingProvider Id="600fb80409f64e15919a2e5ab48843f6" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-09-08T13:26:02.9171500999999999999691240037957840058879810385406017303466796875-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="769b2ab339c94bc5b3d2eafd4dc8151a" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="d5f250af140343559827266789a46971">
						<UserDefinedMetadataItem DataType="String" Id="1f88e6acb9df4161b6a766936fea66e1" Name="Operator">
							<p.Value>gstoll</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="445f9a4c5ea14ca2aab965b9961a70c4" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithProducedData/ProjectWithProducedData.flxproj sha256=031c8a0117dc4e58290bec7ed9606d155d5bf39c9b1f488daa56955e15085360 bytes=4475 -->
## FILE: tests/assets/ProjectWithProducedData/ProjectWithProducedData.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithProducedData/ProjectWithProducedData.flxproj`
- sha256: `031c8a0117dc4e58290bec7ed9606d155d5bf39c9b1f488daa56955e15085360`
- bytes: 4475

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D91119BBD554F4917823366D5148A09A5A0CC8C8DE03DA5FFFD7DDD195D2770A7EFA95FDA697C084FF61C4418B502639ECFCCA63E3BD886EEF2780CA24D0BE58" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="4d164a51a11a4ee4b424f02ecd260fa1" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="7a0c3a8cd754e59a1ca86fdeb31a048" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="10cdd026e8754ef991f232ebe1bcb1ec" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="3d4b9810fce047a9bab6dfc5f4f3a0f0" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="1856dfb213ab4db5a6d1dd8782d3170a" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="1b5ace284abf42519bb71f657d6224f0" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="b04ee3464b3c4e00a553b0f447d9a9c8" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="e290050e8154a50ab8c635e6408deb9" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="8c64b684b9714718adc95b4cfb22b727" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-09-08T18:26:03.0891549Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="c68155733ec4aaa8dbf1c5d94a873a9" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="ef75b5e88f7e45818e1625ab08beb05b" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="8d21fac64427474fb77d5e0b771e1abd" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithProducedData/Screen.flxscr sha256=d237f2a430bd4b52ac0a263396f14c91c3fe70713d7dba2fd59a6b69f6ab42bc bytes=1333 -->
## FILE: tests/assets/ProjectWithProducedData/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithProducedData/Screen.flxscr`
- sha256: `d237f2a430bd4b52ac0a263396f14c91c3fe70713d7dba2fd59a6b69f6ab42bc`
- bytes: 1333

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="5A78ED6E2625CF44E2E863554242599337B90CBCE3E27FD9BCAA0B4BDE1AB5762B2A1C997B7499EF55DCC101B047C1A237A074F368EAD7EF693D13DF8B1AAD65" Timestamp="1D6860E2690BB87" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="226e097e6644d5c8cf0e7f3c2544aa9" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="dd2872a6c4e149ae93032921ceeeb5f4" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithProducedData/Test Specification.flxtest sha256=7d530891f22428bc5496ee2909c5b6ace3d2ee023e2a3b27b227ac43220b8fe6 bytes=1053 -->
## FILE: tests/assets/ProjectWithProducedData/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithProducedData/Test Specification.flxtest`
- sha256: `7d530891f22428bc5496ee2909c5b6ace3d2ee023e2a3b27b227ac43220b8fe6`
- bytes: 1053

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FBE94BF7FAC8910B03E1CD72224A7AD76EA35967878B2D5D50B6FA1A36F6ABEFC02FE36CD6B0077365D5CD00801A02753F3AC0D425C77112A7922EBD607F63B7" Timestamp="1D6860E2690BB87" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.4.0.756" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.4.0.756" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="9f7000b6f74942f391ad04ece2a4221b">
			<ProcessingElementModelOwner Id="d4b11acefa1842cb8c72efdb7fada017" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithSwitchBoard/Channel Specification.flxio sha256=f4615e374a46845a4b6dd1c640177c6604ad12fa990e00a368aa782d92fe74c9 bytes=159587 -->
## FILE: tests/assets/ProjectWithSwitchBoard/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithSwitchBoard/Channel Specification.flxio`
- sha256: `f4615e374a46845a4b6dd1c640177c6604ad12fa990e00a368aa782d92fe74c9`
- bytes: 159587

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="1625D6A442FAE89AC3E057038D8D88CB8A84769F0E13489A85EA660FA554433CA76D60D04BBABF06E27FE0119B95AE746AE47ECE3E984EA4898302A1733CD8D1" Timestamp="1D674BC82AF580F" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="642750e180394b15a51d337037420b7c">
			<ProcessingElementModelOwner Id="8a031b5176ae4ca9becdbfa2f06de6b7">
				<AddonModel AddonCustomIconPath="[string]" AddonIcon="[AddonIconType]Output" AddonInstanceName="[string]SwitchBoard" AddonType="[string]499DD1BA-7ACC-4B7A-E3C8-AB7C12 1352C" DisplayName="[string]SwitchBoard" Id="354dab974d44764b027e86d9e825222" UserDisplayName="[string]SwitchBoard">
					<PeAddonOutputInfo Alias="c12c3940-26dd-4609-9983-25e9839f3896" CriticalAlarm="dedf022bb7444daba3392aef13ab88b3" DataType="[Type]@a39c785150f24ef9bb779edaf8bee0c5" HasLiveData="[bool]False" Id="8b42b88c61f148d683e9caf4822143c0" SampleRate="[double]1" Source="LogEvents" Units="[string]" WarningAlarm="913d627ed98e415e86e99b6e4479b825">
						<AlarmModel Id="913d627ed98e415e86e99b6e4479b825" Severity="[AlarmSeverity]Warning" TriggerModel="4f62b7491a2a406f88c56ba4b259c95a">
							<ChannelMonitorTriggerModel Alias="[string]c11d2880-97f4-4ad3-b55e-e79c712648df" AliasToMonitor="[string]c12c3940-26dd-4609-9983-25e9839f3896" Id="4f62b7491a2a406f88c56ba4b259c95a">
								<AboveValueTriggerModel Id="b8ed5647615b4579a1116ff69a3de52a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="dedf022bb7444daba3392aef13ab88b3" Severity="[AlarmSeverity]Critical" TriggerModel="6a7cfa47e86f45c5ba6d97fb47e3e3fd">
							<ChannelMonitorTriggerModel Alias="[string]993461fa-0578-415a-a8ac-a3645832bea1" AliasToMonitor="[string]c12c3940-26dd-4609-9983-25e9839f3896" Id="6a7cfa47e86f45c5ba6d97fb47e3e3fd">
								<AboveValueTriggerModel Id="93e12d6380c6429aaf131fd901e23e42" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<Keyword Id="51fb5c99ec364e66a0be8fe6159251fa" Name="DoNotTriggerChannel" />
					</PeAddonOutputInfo>
					<ProviderParameter Id="5657d2b8905645dbb6e09211704f0865" ParameterName="[string]FilePath" Type="[Type]String" Value="[string]" />
					<PeAddonInputInfo Alias="Switch 0" CanDisable="[bool]False" GroupName="[string]" Id="c02e6918ec5e403e9ce0f5badea7c01d" IsUserVisible="[bool]True" MappingAlias="[string]9361a5cd-2d53-4673-8707-e0e79256908c" Source="s0" Units="[string]V" Value="[double]0">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 1" CanDisable="[bool]False" GroupName="[string]" Id="8d276b2eae3f4c33ae1a8c739f660b0f" IsUserVisible="[bool]True" MappingAlias="[string]5b754490-1fc0-4537-8618-6fb16ae0f2f5" Source="s1" Units="[string]V" Value="[double]1">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 2" CanDisable="[bool]False" GroupName="[string]" Id="ba3f31ef1801448aaaba53a9e675014d" IsUserVisible="[bool]True" MappingAlias="[string]de219334-373e-42b8-84dc-5750a2be7881" Source="s2" Units="[string]V" Value="[double]2">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 3" CanDisable="[bool]False" GroupName="[string]" Id="2fe7fafd8d8a4b77bbb1128059386dba" IsUserVisible="[bool]True" MappingAlias="[string]0ea2c4c1-7316-4da3-9709-9f3e1d9f28b5" Source="s3" Units="[string]V" Value="[double]3">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 4" CanDisable="[bool]False" GroupName="[string]" Id="9972cc9ab3af4a72bf560a145c178d56" IsUserVisible="[bool]True" MappingAlias="[string]a1589b27-a33b-4b55-8b60-5a8f78e80a40" Source="s4" Units="[string]V" Value="[double]4">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 5" CanDisable="[bool]False" GroupName="[string]" Id="88cf8f96b52648db9b199ee5a7dc48f3" IsUserVisible="[bool]True" MappingAlias="[string]1889f5a4-8d67-4a87-b243-a4655196e271" Source="s5" Units="[string]V" Value="[double]5">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 6" CanDisable="[bool]False" GroupName="[string]" Id="b1bdf8e1bb174db3b016df57de17f4d6" IsUserVisible="[bool]True" MappingAlias="[string]6cc7149f-c408-4c22-991f-a28271d79ad1" Source="s6" Units="[string]V" Value="[double]6">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 7" CanDisable="[bool]False" GroupName="[string]" Id="c1b1c9c22160416885f03ceae77d98b9" IsUserVisible="[bool]True" MappingAlias="[string]4ead545c-e9b4-4ef3-89d1-0ea15d84f152" Source="s7" Units="[string]V" Value="[double]7">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 8" CanDisable="[bool]False" GroupName="[string]" Id="f64b2d1bbaca40fd872f776b8a251992" IsUserVisible="[bool]True" MappingAlias="[string]3f7fbce3-f584-42fb-9050-7762d1a7c5eb" Source="s8" Units="[string]V" Value="[double]8">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 9" CanDisable="[bool]False" GroupName="[string]" Id="ef7faeb6f45747a88338334305481311" IsUserVisible="[bool]True" MappingAlias="[string]8b0fe554-f328-420a-9295-7b92c95a08cd" Source="s9" Units="[string]V" Value="[double]9">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 10" CanDisable="[bool]False" GroupName="[string]" Id="316220ee0559494ea97d968d4b6a623c" IsUserVisible="[bool]True" MappingAlias="[string]54bfa5d7-f7a3-46b8-831a-cbd0734af723" Source="s10" Units="[string]V" Value="[double]10">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 11" CanDisable="[bool]False" GroupName="[string]" Id="6e2496b97c914cd2b99fdbac4277fb19" IsUserVisible="[bool]True" MappingAlias="[string]28b52620-923f-4979-9965-3ceb3fa9e65e" Source="s11" Units="[string]V" Value="[double]11">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 12" CanDisable="[bool]False" GroupName="[string]" Id="38311363ad1481e80c3429da55bd7e4" IsUserVisible="[bool]True" MappingAlias="[string]93df29f2-fc6e-4447-968d-cb5e08b2e8c8" Source="s12" Units="[string]V" Value="[double]12">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 13" CanDisable="[bool]False" GroupName="[string]" Id="d607064cc79540d08cdd74b093b00bf5" IsUserVisible="[bool]True" MappingAlias="[string]ad0707c3-897e-4a47-b67b-554eb34211a3" Source="s13" Units="[string]V" Value="[double]13">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 14" CanDisable="[bool]False" GroupName="[string]" Id="fd79fa420cb848d78d460dd2ddb731a7" IsUserVisible="[bool]True" MappingAlias="[string]2ea9b782-da0f-4a05-8ded-4d911bca25d1" Source="s14" Units="[string]V" Value="[double]14">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 15" CanDisable="[bool]False" GroupName="[string]" Id="59dacc0384e5469782dcfd947906c33c" IsUserVisible="[bool]True" MappingAlias="[string]bd472742-1148-4169-bf23-7f2d8521a928" Source="s15" Units="[string]V" Value="[double]15">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 16" CanDisable="[bool]False" GroupName="[string]" Id="6f905fe8c30f449d83ab2f00e034bc5a" IsUserVisible="[bool]True" MappingAlias="[string]1fec9d80-1c6f-40eb-a481-45e12989dd36" Source="s16" Units="[string]V" Value="[double]16">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 17" CanDisable="[bool]False" GroupName="[string]" Id="8610ee7b228e4e70a17b250f8e0975c5" IsUserVisible="[bool]True" MappingAlias="[string]c3513b22-5678-4050-bd99-b3946836fcfd" Source="s17" Units="[string]V" Value="[double]17">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 18" CanDisable="[bool]False" GroupName="[string]" Id="bf58068b268a432eaa5bf53664fc5012" IsUserVisible="[bool]True" MappingAlias="[string]621932d9-c260-4f04-b6d3-ab5807d15579" Source="s18" Units="[string]V" Value="[double]18">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 19" CanDisable="[bool]False" GroupName="[string]" Id="5c01154afd2c43bab39c8c616a02258f" IsUserVisible="[bool]True" MappingAlias="[string]43d45084-3230-4ee8-9145-f1d000311e50" Source="s19" Units="[string]V" Value="[double]19">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 20" CanDisable="[bool]False" GroupName="[string]" Id="e78bae2187aa4d558d14e38caac9ad53" IsUserVisible="[bool]True" MappingAlias="[string]ee2812c0-41f6-47c4-8f1f-0dda92cdda01" Source="s20" Units="[string]V" Value="[double]20">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 21" CanDisable="[bool]False" GroupName="[string]" Id="fac2499f78e54ab0ae9ac209a8f00181" IsUserVisible="[bool]True" MappingAlias="[string]ff97e4bf-6e1f-42bf-ab5b-aaff7d105057" Source="s21" Units="[string]V" Value="[double]21">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 22" CanDisable="[bool]False" GroupName="[string]" Id="d01e9208eab43e1bc938b73e08ece4e" IsUserVisible="[bool]True" MappingAlias="[string]9e03bd16-7d12-43c2-9d51-967baf679338" Source="s22" Units="[string]V" Value="[double]22">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 23" CanDisable="[bool]False" GroupName="[string]" Id="fdf41afc8f144287b216d0b91e63bb05" IsUserVisible="[bool]True" MappingAlias="[string]09057d19-b0ff-44bd-b472-ac968f55b166" Source="s23" Units="[string]V" Value="[double]23">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 24" CanDisable="[bool]False" GroupName="[string]" Id="d95fe1f2555d4d4baad6ce1f9d75ce52" IsUserVisible="[bool]True" MappingAlias="[string]49113055-0a5b-47cb-acb4-67b40117fb38" Source="s24" Units="[string]V" Value="[double]24">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 25" CanDisable="[bool]False" GroupName="[string]" Id="8945b51b6c7d44578e9cb9beeb806b12" IsUserVisible="[bool]True" MappingAlias="[string]33d0501b-b796-4288-a54e-22c6b6268b5e" Source="s25" Units="[string]V" Value="[double]25">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 26" CanDisable="[bool]False" GroupName="[string]" Id="a37b089506e34acd9d2b02b4b322266d" IsUserVisible="[bool]True" MappingAlias="[string]d802c4e9-6819-424f-8a92-188d88bc82c4" Source="s26" Units="[string]V" Value="[double]26">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 27" CanDisable="[bool]False" GroupName="[string]" Id="c5a83f76683f4e63bc7cae2c29d4c422" IsUserVisible="[bool]True" MappingAlias="[string]76a8c976-1f7b-4d20-9a8f-b2190364f5ed" Source="s27" Units="[string]V" Value="[double]27">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 28" CanDisable="[bool]False" GroupName="[string]" Id="7688617fdb8b461fb8b452978d879582" IsUserVisible="[bool]True" MappingAlias="[string]57d325c1-b450-414c-a098-57a31839be2f" Source="s28" Units="[string]V" Value="[double]28">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 29" CanDisable="[bool]False" GroupName="[string]" Id="97d19a352fea471d8f2c453f8465c223" IsUserVisible="[bool]True" MappingAlias="[string]608b251f-6ac3-41db-8aa9-f9550030a735" Source="s29" Units="[string]V" Value="[double]29">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 30" CanDisable="[bool]False" GroupName="[string]" Id="5681a4b406984c448db857a0b78367fd" IsUserVisible="[bool]True" MappingAlias="[string]6a412d58-463e-42ca-bb2f-206137474434" Source="s30" Units="[string]V" Value="[double]30">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 31" CanDisable="[bool]False" GroupName="[string]" Id="645f4e5c68a848ef80b56f8e67369ae7" IsUserVisible="[bool]True" MappingAlias="[string]7a022add-32c2-4b8a-b917-a276b4fca7c7" Source="s31" Units="[string]V" Value="[double]31">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 32" CanDisable="[bool]False" GroupName="[string]" Id="b32b6153bb134547bac614f2ea8c9d89" IsUserVisible="[bool]True" MappingAlias="[string]af46f798-54ac-4b8b-abfa-e5cb4d6aff72" Source="s32" Units="[string]V" Value="[double]32">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 33" CanDisable="[bool]False" GroupName="[string]" Id="f6b6ab3a40b4435faab66191240c8f86" IsUserVisible="[bool]True" MappingAlias="[string]cb969a15-840e-4fc6-a589-84f94094b29b" Source="s33" Units="[string]V" Value="[double]33">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 34" CanDisable="[bool]False" GroupName="[string]" Id="36ce8cf6d7f04975935106d49e2f1ced" IsUserVisible="[bool]True" MappingAlias="[string]9a0923fc-f5a9-42b7-a4d1-d7253793baef" Source="s34" Units="[string]V" Value="[double]34">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 35" CanDisable="[bool]False" GroupName="[string]" Id="7e7ebd607bb4447ca41098fcf7b8bb62" IsUserVisible="[bool]True" MappingAlias="[string]32f421c5-d49b-400d-975a-90fb411fe13f" Source="s35" Units="[string]V" Value="[double]35">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 36" CanDisable="[bool]False" GroupName="[string]" Id="8d38317fa70b4eb0bdbce81aeeb29d89" IsUserVisible="[bool]True" MappingAlias="[string]2ddb361d-5106-47ea-8e8c-7fd8475a070e" Source="s36" Units="[string]V" Value="[double]36">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 37" CanDisable="[bool]False" GroupName="[string]" Id="bf765cc88ee1482198fdecfdf9e47f2c" IsUserVisible="[bool]True" MappingAlias="[string]ae1f3c1b-c0da-4ed5-b1c5-de38544332e9" Source="s37" Units="[string]V" Value="[double]37">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 38" CanDisable="[bool]False" GroupName="[string]" Id="1e7110bd717940b4b56bad0a960aeaa1" IsUserVisible="[bool]True" MappingAlias="[string]d4b8c94d-8d53-4299-b1cf-79689af8392a" Source="s38" Units="[string]V" Value="[double]38">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 39" CanDisable="[bool]False" GroupName="[string]" Id="f68a9c841f5648d4829aa37e1c5a3e7b" IsUserVisible="[bool]True" MappingAlias="[string]509eda03-12a5-4670-bcaa-a9224af4b758" Source="s39" Units="[string]V" Value="[double]39">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 40" CanDisable="[bool]False" GroupName="[string]" Id="3b68df6dcec04dbf8930f86338cd872c" IsUserVisible="[bool]True" MappingAlias="[string]cf59cb5b-2215-4efa-a36e-1e0bc37bcc85" Source="s40" Units="[string]V" Value="[double]40">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 41" CanDisable="[bool]False" GroupName="[string]" Id="a05c44882347fa96e8c7ad5b820bbb" IsUserVisible="[bool]True" MappingAlias="[string]1306453f-cf3b-451c-9bdf-6d47fa5ca5f4" Source="s41" Units="[string]V" Value="[double]41">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 42" CanDisable="[bool]False" GroupName="[string]" Id="8c3a1a344ccc4f4893580142b4930664" IsUserVisible="[bool]True" MappingAlias="[string]fd8c6922-4f2f-46e0-a28b-7816d34d9f6a" Source="s42" Units="[string]V" Value="[double]42">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 43" CanDisable="[bool]False" GroupName="[string]" Id="bedf7412f6fa4bf28b3f5066f01a1598" IsUserVisible="[bool]True" MappingAlias="[string]1833627e-dbfc-4614-a50e-7b145080263a" Source="s43" Units="[string]V" Value="[double]43">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 44" CanDisable="[bool]False" GroupName="[string]" Id="d500ef001eb5448a851741ea0f959d97" IsUserVisible="[bool]True" MappingAlias="[string]95cb4a80-1d7b-4edc-b357-5f54124716a2" Source="s44" Units="[string]V" Value="[double]44">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 45" CanDisable="[bool]False" GroupName="[string]" Id="582a693239aa47cdab752716a4a7f25c" IsUserVisible="[bool]True" MappingAlias="[string]36d50278-e86b-4cf0-8760-c6f3b0ee21f3" Source="s45" Units="[string]V" Value="[double]45">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 46" CanDisable="[bool]False" GroupName="[string]" Id="6a4984fc51fb428e9eaed5206e27926c" IsUserVisible="[bool]True" MappingAlias="[string]27ed74df-f43f-4501-b75e-bf1e41201c13" Source="s46" Units="[string]V" Value="[double]46">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 47" CanDisable="[bool]False" GroupName="[string]" Id="b0527b187f9544a8ac1761142d2a1f05" IsUserVisible="[bool]True" MappingAlias="[string]9a5cbba4-191b-4b4a-ab16-a4482d9c4c75" Source="s47" Units="[string]V" Value="[double]47">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 48" CanDisable="[bool]False" GroupName="[string]" Id="a1fbd73f83814ddd95ae1f3294ee040d" IsUserVisible="[bool]True" MappingAlias="[string]bff9ddd4-4e9f-46b5-abbe-209c3ceca7fb" Source="s48" Units="[string]V" Value="[double]48">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 49" CanDisable="[bool]False" GroupName="[string]" Id="a5b558937fe54b3e940ffe8c8f557082" IsUserVisible="[bool]True" MappingAlias="[string]127b1165-73d2-4dca-b9f8-376a1fd99661" Source="s49" Units="[string]V" Value="[double]49">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 50" CanDisable="[bool]False" GroupName="[string]" Id="7f584d66890403594dbe2b1c51fd942" IsUserVisible="[bool]True" MappingAlias="[string]0a34088b-bc63-41f8-889b-27f7546269ac" Source="s50" Units="[string]V" Value="[double]50">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 51" CanDisable="[bool]False" GroupName="[string]" Id="6acb2979ce6d41e98640a741964f81b0" IsUserVisible="[bool]True" MappingAlias="[string]605b8958-1d6c-4f23-b03f-88cc241ab066" Source="s51" Units="[string]V" Value="[double]51">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 52" CanDisable="[bool]False" GroupName="[string]" Id="4ae99b31bf85414f876bd07b2b44cde5" IsUserVisible="[bool]True" MappingAlias="[string]cd1f44b5-7fb9-4514-95d7-2451bff47723" Source="s52" Units="[string]V" Value="[double]52">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 53" CanDisable="[bool]False" GroupName="[string]" Id="6076b7020da541feb29ba89eeccc2b01" IsUserVisible="[bool]True" MappingAlias="[string]7a917730-fe11-40f9-99a2-30ecb77e5d8f" Source="s53" Units="[string]V" Value="[double]53">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 54" CanDisable="[bool]False" GroupName="[string]" Id="a975d86e867e489297c1b77f133f2e21" IsUserVisible="[bool]True" MappingAlias="[string]7a7c5d7c-63ef-4624-8a84-5472c4d337ac" Source="s54" Units="[string]V" Value="[double]54">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 55" CanDisable="[bool]False" GroupName="[string]" Id="8639f47b38484d8eb390186dfd0f365c" IsUserVisible="[bool]True" MappingAlias="[string]d31e108b-b721-4ecf-ba86-7af117361546" Source="s55" Units="[string]V" Value="[double]55">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 56" CanDisable="[bool]False" GroupName="[string]" Id="5604ed2a6afb44f094165feb4f552d34" IsUserVisible="[bool]True" MappingAlias="[string]f995fb75-96f0-4b8b-a50d-a2eceeee7729" Source="s56" Units="[string]V" Value="[double]56">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 57" CanDisable="[bool]False" GroupName="[string]" Id="bfa18920807141d28d4cba6c45b3ee2e" IsUserVisible="[bool]True" MappingAlias="[string]e0bf8df7-a1f9-4edf-b2a8-41a319bef167" Source="s57" Units="[string]V" Value="[double]57">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 58" CanDisable="[bool]False" GroupName="[string]" Id="4133d44d7f33432f983970518b4535a4" IsUserVisible="[bool]True" MappingAlias="[string]528094bd-282c-4ad5-86a0-01ad8c2e3949" Source="s58" Units="[string]V" Value="[double]58">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 59" CanDisable="[bool]False" GroupName="[string]" Id="48fc5ff058b04deda984c876e3564ee5" IsUserVisible="[bool]True" MappingAlias="[string]8b084e45-7c50-497b-b202-9bbcbec25f2e" Source="s59" Units="[string]V" Value="[double]59">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 60" CanDisable="[bool]False" GroupName="[string]" Id="4a011bbdba23405683f7c458d149a99d" IsUserVisible="[bool]True" MappingAlias="[string]bd542c3c-5702-445a-8909-5254d6cca66a" Source="s60" Units="[string]V" Value="[double]60">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 61" CanDisable="[bool]False" GroupName="[string]" Id="452744a1aa0f4ff68df8fab1065ed64c" IsUserVisible="[bool]True" MappingAlias="[string]a739889e-8641-4e9f-b478-823f0bdcdaa7" Source="s61" Units="[string]V" Value="[double]61">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 62" CanDisable="[bool]False" GroupName="[string]" Id="f4d956f3253b47328cf3ab982fc6af2d" IsUserVisible="[bool]True" MappingAlias="[string]318051d4-624b-460a-834d-f2d9b2ed1255" Source="s62" Units="[string]V" Value="[double]62">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 63" CanDisable="[bool]False" GroupName="[string]" Id="a1619a9e613b472782eaec0748ea9648" IsUserVisible="[bool]True" MappingAlias="[string]5d984a4a-38d6-49c1-83b6-7b16dc352fbc" Source="s63" Units="[string]V" Value="[double]63">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 64" CanDisable="[bool]False" GroupName="[string]" Id="a81a40c50e6e45749a33694425b269ee" IsUserVisible="[bool]True" MappingAlias="[string]76f22d40-dec6-49c7-92d6-a56ed42afbac" Source="s64" Units="[string]V" Value="[double]64">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 65" CanDisable="[bool]False" GroupName="[string]" Id="2e2f95c3c99e4177887d7760495a5de2" IsUserVisible="[bool]True" MappingAlias="[string]f02e4202-b510-4c5c-8e67-3890b0355210" Source="s65" Units="[string]V" Value="[double]65">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 66" CanDisable="[bool]False" GroupName="[string]" Id="70209af0ff9e4d9d998247d67646f2d0" IsUserVisible="[bool]True" MappingAlias="[string]9adbb564-d8b9-4d5a-98ad-a3375ee468c5" Source="s66" Units="[string]V" Value="[double]66">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 67" CanDisable="[bool]False" GroupName="[string]" Id="b60d5841451a47a695e1bf265fbee1ab" IsUserVisible="[bool]True" MappingAlias="[string]d874bab2-668c-4cd3-b6a1-83ed5256bc13" Source="s67" Units="[string]V" Value="[double]67">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 68" CanDisable="[bool]False" GroupName="[string]" Id="ac21052d58724e689e131ea021eac60a" IsUserVisible="[bool]True" MappingAlias="[string]7c663c0b-938b-4c6d-b4f3-ad806a296f34" Source="s68" Units="[string]V" Value="[double]68">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 69" CanDisable="[bool]False" GroupName="[string]" Id="6d0ccac54d9745088b3e9d6d55c0e641" IsUserVisible="[bool]True" MappingAlias="[string]973bd82a-9906-40a8-b9e4-e9dda5e135a3" Source="s69" Units="[string]V" Value="[double]69">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 70" CanDisable="[bool]False" GroupName="[string]" Id="89ed9d34ab764483b8a5492eddc9192a" IsUserVisible="[bool]True" MappingAlias="[string]82fa9d30-0a5e-4243-bf8a-857abf439f1d" Source="s70" Units="[string]V" Value="[double]70">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 71" CanDisable="[bool]False" GroupName="[string]" Id="eeec808d64d5403bb7739b0397d84797" IsUserVisible="[bool]True" MappingAlias="[string]19c7c73c-8b0c-4998-97a7-3a51a7effabf" Source="s71" Units="[string]V" Value="[double]71">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 72" CanDisable="[bool]False" GroupName="[string]" Id="f670bb34545e42288ef9e3c471d1d4f7" IsUserVisible="[bool]True" MappingAlias="[string]5a55b17a-e11d-45f6-a25c-d37af664d12c" Source="s72" Units="[string]V" Value="[double]72">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 73" CanDisable="[bool]False" GroupName="[string]" Id="c8b7fb6a78034a40aa8177d06167b91d" IsUserVisible="[bool]True" MappingAlias="[string]569e5d2a-565d-4dc1-a220-b9d6aca04a07" Source="s73" Units="[string]V" Value="[double]73">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 74" CanDisable="[bool]False" GroupName="[string]" Id="c24911fe563e4064b0b914c4eb8a9951" IsUserVisible="[bool]True" MappingAlias="[string]14f569dc-f743-475f-9ed1-9fbc7d20139e" Source="s74" Units="[string]V" Value="[double]74">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 75" CanDisable="[bool]False" GroupName="[string]" Id="8ed9c3bfc94c4a88910ba1efb954af7a" IsUserVisible="[bool]True" MappingAlias="[string]950e3e14-cd46-4996-94e3-4c35c2137b38" Source="s75" Units="[string]V" Value="[double]75">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 76" CanDisable="[bool]False" GroupName="[string]" Id="16999e17730c45e2a95caa41f67b7cf1" IsUserVisible="[bool]True" MappingAlias="[string]8d3fb879-9479-4646-81dc-75795e27c5ff" Source="s76" Units="[string]V" Value="[double]76">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 77" CanDisable="[bool]False" GroupName="[string]" Id="dd108c5a1c948af812f43eaac59934e" IsUserVisible="[bool]True" MappingAlias="[string]e4d841ba-4157-4c96-b3aa-09ab7279f0df" Source="s77" Units="[string]V" Value="[double]77">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 78" CanDisable="[bool]False" GroupName="[string]" Id="f81b61d184f64daf92d1c7dbed806ac6" IsUserVisible="[bool]True" MappingAlias="[string]f1495568-2cd3-466c-929a-c23a45fc2168" Source="s78" Units="[string]V" Value="[double]78">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 79" CanDisable="[bool]False" GroupName="[string]" Id="be55f7e8f8845b9bc2dfe5c633128f1" IsUserVisible="[bool]True" MappingAlias="[string]b7f9cf3d-d9f5-4bb9-a591-f0e4f6172010" Source="s79" Units="[string]V" Value="[double]79">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 80" CanDisable="[bool]False" GroupName="[string]" Id="80a51a362c1f4dce848ed4e0266339b7" IsUserVisible="[bool]True" MappingAlias="[string]af030e15-dd57-4aed-bef8-bd14432f393d" Source="s80" Units="[string]V" Value="[double]80">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 81" CanDisable="[bool]False" GroupName="[string]" Id="29d67114b4bb4aca8fec26420be14e26" IsUserVisible="[bool]True" MappingAlias="[string]b6b0c051-1d99-4fbb-a321-4ae48d13eb1d" Source="s81" Units="[string]V" Value="[double]81">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 82" CanDisable="[bool]False" GroupName="[string]" Id="959f0da0193847a4ba45fb19e1001a94" IsUserVisible="[bool]True" MappingAlias="[string]199d32e5-4091-4315-922c-eb9edf226894" Source="s82" Units="[string]V" Value="[double]82">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 83" CanDisable="[bool]False" GroupName="[string]" Id="84d9584181b54cd4b50b7f7121f1ccd0" IsUserVisible="[bool]True" MappingAlias="[string]69cf1d95-1403-4de9-95d7-bb3f228cea40" Source="s83" Units="[string]V" Value="[double]83">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 84" CanDisable="[bool]False" GroupName="[string]" Id="ec53b222acb3429f8bae6b7b57233f13" IsUserVisible="[bool]True" MappingAlias="[string]5d58616c-b678-47d7-87ec-f9564a34349a" Source="s84" Units="[string]V" Value="[double]84">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 85" CanDisable="[bool]False" GroupName="[string]" Id="a439d35f22384873b81b10a753110b17" IsUserVisible="[bool]True" MappingAlias="[string]377eda79-a3b7-4eae-9791-46bb85888b80" Source="s85" Units="[string]V" Value="[double]85">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 86" CanDisable="[bool]False" GroupName="[string]" Id="2f2a9eb8ee5e46308e9d34e75c0db618" IsUserVisible="[bool]True" MappingAlias="[string]7410a32e-8ebc-4fb7-8902-ee7874f39e00" Source="s86" Units="[string]V" Value="[double]86">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 87" CanDisable="[bool]False" GroupName="[string]" Id="63454c7ee01a432bb95ec176f9ec9166" IsUserVisible="[bool]True" MappingAlias="[string]86c2ae93-6c8d-402d-ac6e-d4c7cbac9488" Source="s87" Units="[string]V" Value="[double]87">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 88" CanDisable="[bool]False" GroupName="[string]" Id="b89683a9b5d4f7c99e40ef05b3e91ac" IsUserVisible="[bool]True" MappingAlias="[string]6108183a-8cfe-4513-8de7-a3eda38bbe38" Source="s88" Units="[string]V" Value="[double]88">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 89" CanDisable="[bool]False" GroupName="[string]" Id="dade41acfb5a4cc1bed2e190eaee5059" IsUserVisible="[bool]True" MappingAlias="[string]95d96087-192e-4d65-87a7-74fa3b944a7a" Source="s89" Units="[string]V" Value="[double]89">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 90" CanDisable="[bool]False" GroupName="[string]" Id="167a9b0b163f4713aa27039e927b7b89" IsUserVisible="[bool]True" MappingAlias="[string]8402fda2-7185-40d3-8f28-ac5d19d248f3" Source="s90" Units="[string]V" Value="[double]90">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 91" CanDisable="[bool]False" GroupName="[string]" Id="ce30604f8ddd462db5cbbd71046f46ad" IsUserVisible="[bool]True" MappingAlias="[string]622abd2c-35bd-400b-802e-75a6427ddc1d" Source="s91" Units="[string]V" Value="[double]91">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 92" CanDisable="[bool]False" GroupName="[string]" Id="912efb6cc7434d6aacc5586c8adc2352" IsUserVisible="[bool]True" MappingAlias="[string]ac025060-881c-496c-a37c-642cfc36f779" Source="s92" Units="[string]V" Value="[double]92">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 93" CanDisable="[bool]False" GroupName="[string]" Id="fa699252ac90453fae47e3f9d82f08e8" IsUserVisible="[bool]True" MappingAlias="[string]efa8c6f7-2b95-41d8-bb26-381665c7eb43" Source="s93" Units="[string]V" Value="[double]93">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 94" CanDisable="[bool]False" GroupName="[string]" Id="6b7af65a04de40fab51177d47fbbbaed" IsUserVisible="[bool]True" MappingAlias="[string]9cd92ed5-5bc2-427e-bebb-9f2729110ce0" Source="s94" Units="[string]V" Value="[double]94">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 95" CanDisable="[bool]False" GroupName="[string]" Id="47aae383a8a4ef5b733a4eb834d7ded" IsUserVisible="[bool]True" MappingAlias="[string]4ac89971-808d-4f78-843f-1a68a983f876" Source="s95" Units="[string]V" Value="[double]95">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 96" CanDisable="[bool]False" GroupName="[string]" Id="cd1f980295b94af2844946e4805b60e2" IsUserVisible="[bool]True" MappingAlias="[string]066ff139-d900-490d-a247-d0ddf7b70181" Source="s96" Units="[string]V" Value="[double]96">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 97" CanDisable="[bool]False" GroupName="[string]" Id="9a9b60691604a26b67f9eff7874643d" IsUserVisible="[bool]True" MappingAlias="[string]fcaf39a8-d335-497c-b097-edaef3658f3f" Source="s97" Units="[string]V" Value="[double]97">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 98" CanDisable="[bool]False" GroupName="[string]" Id="74935136ea644cbba81b65bda8bdeb8d" IsUserVisible="[bool]True" MappingAlias="[string]0c909be2-021a-4c94-9330-ccc105d10095" Source="s98" Units="[string]V" Value="[double]98">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonInputInfo Alias="Switch 99" CanDisable="[bool]False" GroupName="[string]" Id="2876fc5d610043e6849d334b2a09c208" IsUserVisible="[bool]True" MappingAlias="[string]f4752ba4-fffb-4ee4-8c09-8971bac730a4" Source="s99" Units="[string]V" Value="[double]99">
						<SupportedDataType />
					</PeAddonInputInfo>
					<PeAddonOutputInfo Alias="Sink 0" CanDisable="[bool]True" CriticalAlarm="5a7f22617c1e4ffd883c281bc1eda220" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="9237b01221a47a796d641cab3a699aa" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink0" Units="[string]Voltaires" WarningAlarm="6125a9e9e34b42898bac8321d7e9705e">
						<AlarmModel Id="6125a9e9e34b42898bac8321d7e9705e" Severity="[AlarmSeverity]Warning" TriggerModel="641fce4eb636478ca362f82ad2e63994">
							<ChannelMonitorTriggerModel Alias="[string]a83dc899-e09f-482d-ab17-604919acf596" AliasToMonitor="[string]Sink 0" Id="641fce4eb636478ca362f82ad2e63994">
								<AboveValueTriggerModel Id="d0bb59bc5007441984ee1983fb62141e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5a7f22617c1e4ffd883c281bc1eda220" Severity="[AlarmSeverity]Critical" TriggerModel="e26e58ef87154cd19e3e213ae9adedc0">
							<ChannelMonitorTriggerModel Alias="[string]6bdb6de3-ce64-4ba5-9efc-43d449cd0ec5" AliasToMonitor="[string]Sink 0" Id="e26e58ef87154cd19e3e213ae9adedc0">
								<AboveValueTriggerModel Id="626efe2a48a94c968c4444c642184f3a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 1" CanDisable="[bool]True" CriticalAlarm="982331cc1f3e49769755bbcc7cbb5fe7" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="159ef0c9eacb445981757d2d750e1516" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink1" Units="[string]Voltaires" WarningAlarm="fe6f16bce0334d96a9de4124851c6908">
						<AlarmModel Id="fe6f16bce0334d96a9de4124851c6908" Severity="[AlarmSeverity]Warning" TriggerModel="8118cfbda60f407186363d7eaa734e67">
							<ChannelMonitorTriggerModel Alias="[string]502399c1-e354-44c7-801e-cfaec7b05d3b" AliasToMonitor="[string]Sink 1" Id="8118cfbda60f407186363d7eaa734e67">
								<AboveValueTriggerModel Id="25de1e1351914edd8e31ff234d24f8f7" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="982331cc1f3e49769755bbcc7cbb5fe7" Severity="[AlarmSeverity]Critical" TriggerModel="e35bb97672a640ad9a0fbd696de9a211">
							<ChannelMonitorTriggerModel Alias="[string]c5781e84-2be6-4981-ac22-86d5d2a06279" AliasToMonitor="[string]Sink 1" Id="e35bb97672a640ad9a0fbd696de9a211">
								<AboveValueTriggerModel Id="65f4a169df4344b98e6c7a9a695774f0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 2" CanDisable="[bool]True" CriticalAlarm="7cb6044060374f799ced3e6dd35a3656" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="557a80c58bd248a98e38af26053e540a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink2" Units="[string]Voltaires" WarningAlarm="5724be9d6b21456db20f8395dfa06c44">
						<AlarmModel Id="5724be9d6b21456db20f8395dfa06c44" Severity="[AlarmSeverity]Warning" TriggerModel="1d1e09dd96204ec39831f71171b3019b">
							<ChannelMonitorTriggerModel Alias="[string]426dfbad-922c-4054-96b0-b9c2de908a80" AliasToMonitor="[string]Sink 2" Id="1d1e09dd96204ec39831f71171b3019b">
								<AboveValueTriggerModel Id="f39c60c5499348dc92a80604bedb63aa" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7cb6044060374f799ced3e6dd35a3656" Severity="[AlarmSeverity]Critical" TriggerModel="bcd2a7ef0bf74894bc0f8603e24ff2b1">
							<ChannelMonitorTriggerModel Alias="[string]0294e5f6-4176-4e94-8d52-cf76b5d0cb1d" AliasToMonitor="[string]Sink 2" Id="bcd2a7ef0bf74894bc0f8603e24ff2b1">
								<AboveValueTriggerModel Id="76e85028f05b41d8b99ffd277f8e41e9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 3" CanDisable="[bool]True" CriticalAlarm="dc066c713054e36b4affcfe5d9b6d9b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="9b43fdb2cb49437ebbb802a3766ae215" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink3" Units="[string]Voltaires" WarningAlarm="a74f5e2445b24cc9b1509ec8f5864100">
						<AlarmModel Id="a74f5e2445b24cc9b1509ec8f5864100" Severity="[AlarmSeverity]Warning" TriggerModel="a388b405abc142169eb029bc2384de6e">
							<ChannelMonitorTriggerModel Alias="[string]4d36d174-e39b-4ef5-88f9-1927b2eb7b76" AliasToMonitor="[string]Sink 3" Id="a388b405abc142169eb029bc2384de6e">
								<AboveValueTriggerModel Id="e2d1ab7b24614a6f838bab1fef592000" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="dc066c713054e36b4affcfe5d9b6d9b" Severity="[AlarmSeverity]Critical" TriggerModel="51838a08445c494096c045a9427747a4">
							<ChannelMonitorTriggerModel Alias="[string]ecac8d89-334c-4b30-ada9-f2c66d89f9d9" AliasToMonitor="[string]Sink 3" Id="51838a08445c494096c045a9427747a4">
								<AboveValueTriggerModel Id="e6da73af103842cebc8f5087ee57482c" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 4" CanDisable="[bool]True" CriticalAlarm="b39d9ac60b0047f99dba11bd447538f1" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="dde07ecb764849589e71735ef08d2d1b" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink4" Units="[string]Voltaires" WarningAlarm="3ec3e5a4a667428daeb9827b70d0cd70">
						<AlarmModel Id="3ec3e5a4a667428daeb9827b70d0cd70" Severity="[AlarmSeverity]Warning" TriggerModel="e896b69fb85d4a2d864aec51a5a9191a">
							<ChannelMonitorTriggerModel Alias="[string]de8e466b-cab3-4fce-81a7-985647df6938" AliasToMonitor="[string]Sink 4" Id="e896b69fb85d4a2d864aec51a5a9191a">
								<AboveValueTriggerModel Id="129bc40c94d343aba740a2170369b7ee" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="b39d9ac60b0047f99dba11bd447538f1" Severity="[AlarmSeverity]Critical" TriggerModel="4406107a91b420b8485ee6a03bb13b6">
							<ChannelMonitorTriggerModel Alias="[string]0c764134-9348-424c-b4f8-7ed07afe1cae" AliasToMonitor="[string]Sink 4" Id="4406107a91b420b8485ee6a03bb13b6">
								<AboveValueTriggerModel Id="e799c76c81b7428fade63e48a5466454" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 5" CanDisable="[bool]True" CriticalAlarm="914878d75c2546ae90f89902aa4f4d10" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="290a7d1afd234730839135d1074114c2" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink5" Units="[string]Voltaires" WarningAlarm="f49a749979b4e16b458804f9e976566">
						<AlarmModel Id="f49a749979b4e16b458804f9e976566" Severity="[AlarmSeverity]Warning" TriggerModel="16abbb5315f489fb21b0cdb566a4012">
							<ChannelMonitorTriggerModel Alias="[string]90b87720-1b5a-4300-9c5b-109e49c28d74" AliasToMonitor="[string]Sink 5" Id="16abbb5315f489fb21b0cdb566a4012">
								<AboveValueTriggerModel Id="53442584e47147079147dd1e7366aeb4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="914878d75c2546ae90f89902aa4f4d10" Severity="[AlarmSeverity]Critical" TriggerModel="ac21ff28785e403fb70f05ac2057ef1a">
							<ChannelMonitorTriggerModel Alias="[string]888dfff6-8c85-4c07-8f09-2e962c343c5a" AliasToMonitor="[string]Sink 5" Id="ac21ff28785e403fb70f05ac2057ef1a">
								<AboveValueTriggerModel Id="8bb88aa7fac640aa8a8f91ea8125f3cb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 6" CanDisable="[bool]True" CriticalAlarm="37efb94007a44b6f806e5361d8bba66b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="3c0837d98af24054a7c34886c9c4490e" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink6" Units="[string]Voltaires" WarningAlarm="b57166cfe6be44859442e1d10191467b">
						<AlarmModel Id="b57166cfe6be44859442e1d10191467b" Severity="[AlarmSeverity]Warning" TriggerModel="dcec041bcddf4373b8410573ed999ae8">
							<ChannelMonitorTriggerModel Alias="[string]27f67fe0-f3f3-4592-81b9-b060f2e580b9" AliasToMonitor="[string]Sink 6" Id="dcec041bcddf4373b8410573ed999ae8">
								<AboveValueTriggerModel Id="a68eebee21f4407f8a6baf9bc429f392" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="37efb94007a44b6f806e5361d8bba66b" Severity="[AlarmSeverity]Critical" TriggerModel="ae9b1ffd2f4543aaad32966138e0d9b2">
							<ChannelMonitorTriggerModel Alias="[string]5d5003f4-ec67-4573-8370-6ea791738155" AliasToMonitor="[string]Sink 6" Id="ae9b1ffd2f4543aaad32966138e0d9b2">
								<AboveValueTriggerModel Id="c4b6b32e3697493ba293c9d681397f45" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 7" CanDisable="[bool]True" CriticalAlarm="cc6a7f9827684b09872aa06950034e60" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="13d845e44bbd45a09c55a8795e722d4d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink7" Units="[string]Voltaires" WarningAlarm="4a790754b4dd4c9488cdf2afefdfa68e">
						<AlarmModel Id="4a790754b4dd4c9488cdf2afefdfa68e" Severity="[AlarmSeverity]Warning" TriggerModel="36eac93b79254492b637492368b2275c">
							<ChannelMonitorTriggerModel Alias="[string]31b5f987-44f3-49f1-b2c7-18e05103aefb" AliasToMonitor="[string]Sink 7" Id="36eac93b79254492b637492368b2275c">
								<AboveValueTriggerModel Id="bea78751a3cc415fb3e5195cc926ddc0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="cc6a7f9827684b09872aa06950034e60" Severity="[AlarmSeverity]Critical" TriggerModel="6267239b75834c729206cf4b7dd061c5">
							<ChannelMonitorTriggerModel Alias="[string]613a4e72-8570-4549-a672-9012f258fadb" AliasToMonitor="[string]Sink 7" Id="6267239b75834c729206cf4b7dd061c5">
								<AboveValueTriggerModel Id="2fb38c7d834c849ce6882fddf47ec3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 8" CanDisable="[bool]True" CriticalAlarm="c8ccfb3b39054b59b9536c8f5dc89c27" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4330d91fce09469ab91a1d25afed2885" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink8" Units="[string]Voltaires" WarningAlarm="6ba44d005705423d8969de459f73d293">
						<AlarmModel Id="6ba44d005705423d8969de459f73d293" Severity="[AlarmSeverity]Warning" TriggerModel="48eb73fdc4454c879d8619a0f711a3e3">
							<ChannelMonitorTriggerModel Alias="[string]0420bf4c-6cb3-428f-90ac-1b650414eee3" AliasToMonitor="[string]Sink 8" Id="48eb73fdc4454c879d8619a0f711a3e3">
								<AboveValueTriggerModel Id="2fded7d7efe947bd970ef429fd871505" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="c8ccfb3b39054b59b9536c8f5dc89c27" Severity="[AlarmSeverity]Critical" TriggerModel="a22b592ea0ec4544a540d7c80946f40a">
							<ChannelMonitorTriggerModel Alias="[string]6c3995ff-aa48-4379-84d2-2a43f7f4a8e5" AliasToMonitor="[string]Sink 8" Id="a22b592ea0ec4544a540d7c80946f40a">
								<AboveValueTriggerModel Id="ca72bb6cbd4b4553990c7fcd28b08563" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 9" CanDisable="[bool]True" CriticalAlarm="e95f45b0a3214dfdbd1fac26e530138b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4146bcaac6e943cd90ce3db7b88b88ac" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink9" Units="[string]Voltaires" WarningAlarm="62f56e89bc6c41e7ac10baa2eea6dd43">
						<AlarmModel Id="62f56e89bc6c41e7ac10baa2eea6dd43" Severity="[AlarmSeverity]Warning" TriggerModel="fa56aa7f3a254c51b31d56810c5f6047">
							<ChannelMonitorTriggerModel Alias="[string]0223978b-fa5f-4cae-a4ac-ce13689fe27e" AliasToMonitor="[string]Sink 9" Id="fa56aa7f3a254c51b31d56810c5f6047">
								<AboveValueTriggerModel Id="fab768d8753b423d98ce8cd0c7d4e830" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="e95f45b0a3214dfdbd1fac26e530138b" Severity="[AlarmSeverity]Critical" TriggerModel="d41cf9b8c824955adca1968b36390d2">
							<ChannelMonitorTriggerModel Alias="[string]c7aec220-7ad0-4c56-b6d7-1bed9407a359" AliasToMonitor="[string]Sink 9" Id="d41cf9b8c824955adca1968b36390d2">
								<AboveValueTriggerModel Id="830abb6984b74c128dcdaf5f3a6738f5" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 10" CanDisable="[bool]True" CriticalAlarm="13cb866b924457f80a2a8fbd1c660a0" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6a7b4ea1db1940cda4b99526e31c2c66" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink10" Units="[string]Voltaires" WarningAlarm="62c8c7450c174f3fb645789068af5f0a">
						<AlarmModel Id="62c8c7450c174f3fb645789068af5f0a" Severity="[AlarmSeverity]Warning" TriggerModel="6ae2b733ad524d559c63eb74225d4fd7">
							<ChannelMonitorTriggerModel Alias="[string]b619a5da-bad1-420b-abe7-99732d115dc6" AliasToMonitor="[string]Sink 10" Id="6ae2b733ad524d559c63eb74225d4fd7">
								<AboveValueTriggerModel Id="936f2265899041f1a43d6f4c79dddd82" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="13cb866b924457f80a2a8fbd1c660a0" Severity="[AlarmSeverity]Critical" TriggerModel="9d9b82827534111bafadc0313be8c8c">
							<ChannelMonitorTriggerModel Alias="[string]2779d82e-d8e2-4ba7-a039-b3954bf647e4" AliasToMonitor="[string]Sink 10" Id="9d9b82827534111bafadc0313be8c8c">
								<AboveValueTriggerModel Id="2986d137d3c1492fbc1e565851b42410" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 11" CanDisable="[bool]True" CriticalAlarm="3b9eba9ecce1404b92d03b634e1f64e7" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="9c49baf27273471c936a3852da5115e0" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink11" Units="[string]Voltaires" WarningAlarm="9b600e05ac7487a8c8cca31a46ccc93">
						<AlarmModel Id="9b600e05ac7487a8c8cca31a46ccc93" Severity="[AlarmSeverity]Warning" TriggerModel="136202ac8abc47449dcf5bac81350cb2">
							<ChannelMonitorTriggerModel Alias="[string]4d72e8f5-0086-491a-b90c-4e5532b5b255" AliasToMonitor="[string]Sink 11" Id="136202ac8abc47449dcf5bac81350cb2">
								<AboveValueTriggerModel Id="84336c20f492465db756a733cd3664f4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="3b9eba9ecce1404b92d03b634e1f64e7" Severity="[AlarmSeverity]Critical" TriggerModel="719ce3b6523e47e78abb26622f93881f">
							<ChannelMonitorTriggerModel Alias="[string]04338b8d-2862-413f-9c87-3004b3bf9309" AliasToMonitor="[string]Sink 11" Id="719ce3b6523e47e78abb26622f93881f">
								<AboveValueTriggerModel Id="33b25d6d6916443285f7ac8d47aa9db3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 12" CanDisable="[bool]True" CriticalAlarm="43ad64bcf5e4da68fe251c66e4f9930" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c85ca86ec89c4538a57ec33859e19c63" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink12" Units="[string]Voltaires" WarningAlarm="68dcbc6ea24d4978ac1434abc2496fc9">
						<AlarmModel Id="68dcbc6ea24d4978ac1434abc2496fc9" Severity="[AlarmSeverity]Warning" TriggerModel="bbd1f16f0e59480380f584b23693b52c">
							<ChannelMonitorTriggerModel Alias="[string]6476dd42-cf28-4019-9ab7-913ed9c14849" AliasToMonitor="[string]Sink 12" Id="bbd1f16f0e59480380f584b23693b52c">
								<AboveValueTriggerModel Id="c18543ce67274f64af17159dd440c6a0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="43ad64bcf5e4da68fe251c66e4f9930" Severity="[AlarmSeverity]Critical" TriggerModel="c6bbc194ef4c443493695b130cc551c3">
							<ChannelMonitorTriggerModel Alias="[string]5d4bbf78-6c2b-4f19-8be0-446fb898af86" AliasToMonitor="[string]Sink 12" Id="c6bbc194ef4c443493695b130cc551c3">
								<AboveValueTriggerModel Id="dcfca9995ce140dcbb9852340caef53a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 13" CanDisable="[bool]True" CriticalAlarm="a658334a86304392b804302a0a3197e1" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="429ee538efe4844b8fcfdddc2f6bcee" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink13" Units="[string]Voltaires" WarningAlarm="46997c0089974c1593606f4a3b5515b7">
						<AlarmModel Id="46997c0089974c1593606f4a3b5515b7" Severity="[AlarmSeverity]Warning" TriggerModel="777025f1d7d741ea8d45f22c7dd40e2d">
							<ChannelMonitorTriggerModel Alias="[string]3dd3015b-7bc9-41e0-a8e5-37e058d2572d" AliasToMonitor="[string]Sink 13" Id="777025f1d7d741ea8d45f22c7dd40e2d">
								<AboveValueTriggerModel Id="8470b24d1ebd4dd59f3c8beab835a0e1" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="a658334a86304392b804302a0a3197e1" Severity="[AlarmSeverity]Critical" TriggerModel="55b637ded747465aa3c1a0cd7926a3e3">
							<ChannelMonitorTriggerModel Alias="[string]678a5ce0-73fd-43d1-a891-bc4ad66b89a0" AliasToMonitor="[string]Sink 13" Id="55b637ded747465aa3c1a0cd7926a3e3">
								<AboveValueTriggerModel Id="d350e4431924c57b0d0ea79d9af3ae4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 14" CanDisable="[bool]True" CriticalAlarm="5804f0184ea744bd8f57f0376126d69d" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="379e176857b944c482acb7654753dfb3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink14" Units="[string]Voltaires" WarningAlarm="3e5eab6e1cca47bcb5d41277a4bb563f">
						<AlarmModel Id="3e5eab6e1cca47bcb5d41277a4bb563f" Severity="[AlarmSeverity]Warning" TriggerModel="1a21fa16b9a5491fb99fdb89a5bcd655">
							<ChannelMonitorTriggerModel Alias="[string]8d980c21-295a-4f88-a5a1-9c75eb0c30a7" AliasToMonitor="[string]Sink 14" Id="1a21fa16b9a5491fb99fdb89a5bcd655">
								<AboveValueTriggerModel Id="eadbab192ac14cbd81f60e151018ee8f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5804f0184ea744bd8f57f0376126d69d" Severity="[AlarmSeverity]Critical" TriggerModel="aa165584e34142558a236a4183ea1abd">
							<ChannelMonitorTriggerModel Alias="[string]9493acbc-9569-4e31-9ada-63d10e19c6a5" AliasToMonitor="[string]Sink 14" Id="aa165584e34142558a236a4183ea1abd">
								<AboveValueTriggerModel Id="e9033a5c6b444a049da3e3de47743099" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 15" CanDisable="[bool]True" CriticalAlarm="3d0c0345f8724fd9ab9867e7d30e4636" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="ee114ed7d38d4dbf8ab705fabceef1b8" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink15" Units="[string]Voltaires" WarningAlarm="416a8a255495428786b311fe5b2e5b74">
						<AlarmModel Id="416a8a255495428786b311fe5b2e5b74" Severity="[AlarmSeverity]Warning" TriggerModel="f26c58794f1542b1af06ee161b3d3b78">
							<ChannelMonitorTriggerModel Alias="[string]c0e7b27d-bf1f-49b9-abb0-de05bceb6061" AliasToMonitor="[string]Sink 15" Id="f26c58794f1542b1af06ee161b3d3b78">
								<AboveValueTriggerModel Id="a79e852d7fb54ec6a8677234a125b322" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="3d0c0345f8724fd9ab9867e7d30e4636" Severity="[AlarmSeverity]Critical" TriggerModel="fda64c8ba4634162991f6edce98ca3fa">
							<ChannelMonitorTriggerModel Alias="[string]26cb55dc-c5e4-4499-ab90-40d849392c7a" AliasToMonitor="[string]Sink 15" Id="fda64c8ba4634162991f6edce98ca3fa">
								<AboveValueTriggerModel Id="5894b7db69f744ebabbc39d4a307ff36" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 16" CanDisable="[bool]True" CriticalAlarm="14a035f767a9425ea96dff9967b9a29f" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="f81df8ae690e4f47ba5eb5c11583e3b7" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink16" Units="[string]Voltaires" WarningAlarm="2eed5911e3314cb4804af816d9de32f5">
						<AlarmModel Id="2eed5911e3314cb4804af816d9de32f5" Severity="[AlarmSeverity]Warning" TriggerModel="ca616a2a78734d3794b8cd9871b26520">
							<ChannelMonitorTriggerModel Alias="[string]9c3b8d19-8bcd-40d5-b764-9829c25fab53" AliasToMonitor="[string]Sink 16" Id="ca616a2a78734d3794b8cd9871b26520">
								<AboveValueTriggerModel Id="c63af1578382444184b5de163bca11a5" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="14a035f767a9425ea96dff9967b9a29f" Severity="[AlarmSeverity]Critical" TriggerModel="20ba2d7dc3ea48bfab457df2693edbe3">
							<ChannelMonitorTriggerModel Alias="[string]95599b43-145f-405a-ae19-f7d5cadc4749" AliasToMonitor="[string]Sink 16" Id="20ba2d7dc3ea48bfab457df2693edbe3">
								<AboveValueTriggerModel Id="10a8cde2e2b4438cb241896c66fe732c" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 17" CanDisable="[bool]True" CriticalAlarm="e65e5132c9ce4e1da37985f2864059df" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="ed8aa9bd684d4bb3a94d21645f136ef1" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink17" Units="[string]Voltaires" WarningAlarm="911cb06c8750447eaf22e6563f1ab258">
						<AlarmModel Id="911cb06c8750447eaf22e6563f1ab258" Severity="[AlarmSeverity]Warning" TriggerModel="db2ee7b0b9254e2bb14f98119a267b8b">
							<ChannelMonitorTriggerModel Alias="[string]35f45ce2-bbb9-4783-a5b9-fe01f79cdb92" AliasToMonitor="[string]Sink 17" Id="db2ee7b0b9254e2bb14f98119a267b8b">
								<AboveValueTriggerModel Id="fb2eab927e384af9ada9a1c06339fe6b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="e65e5132c9ce4e1da37985f2864059df" Severity="[AlarmSeverity]Critical" TriggerModel="23f795088f0d4eb6acc0da870716fcad">
							<ChannelMonitorTriggerModel Alias="[string]b67aace8-c036-47b0-b945-1288bb28abf5" AliasToMonitor="[string]Sink 17" Id="23f795088f0d4eb6acc0da870716fcad">
								<AboveValueTriggerModel Id="7095a85ea6414441a9519f1d07cf7b94" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 18" CanDisable="[bool]True" CriticalAlarm="1f6f27dfdf9d4112a7e7add8852d16c4" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="a79c87d928fa4c238d50ab91e96fbf92" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink18" Units="[string]Voltaires" WarningAlarm="e640f049e4674b529836216ae0c74ec8">
						<AlarmModel Id="e640f049e4674b529836216ae0c74ec8" Severity="[AlarmSeverity]Warning" TriggerModel="b6944fd624c144a792d3699141e2024d">
							<ChannelMonitorTriggerModel Alias="[string]d6fe70b0-6e10-4001-bf57-30043d855b05" AliasToMonitor="[string]Sink 18" Id="b6944fd624c144a792d3699141e2024d">
								<AboveValueTriggerModel Id="16bf08db5ac14c5a8d2386f0c34abeee" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="1f6f27dfdf9d4112a7e7add8852d16c4" Severity="[AlarmSeverity]Critical" TriggerModel="e3c33e3a2ca64816b43c1318ff417c82">
							<ChannelMonitorTriggerModel Alias="[string]c57a6924-9427-4669-a5c3-7cdc7fbc5e7b" AliasToMonitor="[string]Sink 18" Id="e3c33e3a2ca64816b43c1318ff417c82">
								<AboveValueTriggerModel Id="ca73073309714f5ab53c3656d31eec1d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 19" CanDisable="[bool]True" CriticalAlarm="fc005b28851a43a5a3cecfa5eaee1c7c" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="41ba8270e86e416eb60b8cb0005f6eaa" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink19" Units="[string]Voltaires" WarningAlarm="85340e5cef424ba08b52e2fe4154a93a">
						<AlarmModel Id="85340e5cef424ba08b52e2fe4154a93a" Severity="[AlarmSeverity]Warning" TriggerModel="eacf4253124a4da7bf303c4654558801">
							<ChannelMonitorTriggerModel Alias="[string]6f0b92e9-ec15-4c53-a82e-928ffe648a97" AliasToMonitor="[string]Sink 19" Id="eacf4253124a4da7bf303c4654558801">
								<AboveValueTriggerModel Id="ea1c09b3f24e48fbaaf260aa58776cdd" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="fc005b28851a43a5a3cecfa5eaee1c7c" Severity="[AlarmSeverity]Critical" TriggerModel="775b5614cf304ba7b0fc4dbfb06b1469">
							<ChannelMonitorTriggerModel Alias="[string]f3ec665a-b061-4e7a-9b42-ea9ce4f5fc3f" AliasToMonitor="[string]Sink 19" Id="775b5614cf304ba7b0fc4dbfb06b1469">
								<AboveValueTriggerModel Id="a7e7f9b55e8840c8aca780424ec62999" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 20" CanDisable="[bool]True" CriticalAlarm="dc8e5c3204774c299035fd79a538eaa7" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2a4ab03bbaf4b5988173794cf5896b2" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink20" Units="[string]Voltaires" WarningAlarm="172baba08e90478c9b8441437ec52b28">
						<AlarmModel Id="172baba08e90478c9b8441437ec52b28" Severity="[AlarmSeverity]Warning" TriggerModel="f732a17d74194ad9a9c351b15dbe7d5a">
							<ChannelMonitorTriggerModel Alias="[string]a14b138b-81e6-4328-a4d3-08f10fbaab49" AliasToMonitor="[string]Sink 20" Id="f732a17d74194ad9a9c351b15dbe7d5a">
								<AboveValueTriggerModel Id="be641e8bfd894d75b94a238eb09b0dbb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="dc8e5c3204774c299035fd79a538eaa7" Severity="[AlarmSeverity]Critical" TriggerModel="2b05d03e7804e2ab8088467f9ab2028">
							<ChannelMonitorTriggerModel Alias="[string]5a04cd03-354a-4ca6-b7d1-c2a67e0b4536" AliasToMonitor="[string]Sink 20" Id="2b05d03e7804e2ab8088467f9ab2028">
								<AboveValueTriggerModel Id="32d578c3c78440cb2ac245e0ddbc7d2" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 21" CanDisable="[bool]True" CriticalAlarm="77ee372445c348b09d32b68000ca4d1c" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="23ee1ab5eea34e2889f71d490d43d743" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink21" Units="[string]Voltaires" WarningAlarm="ea009f8675e4271ae6b019160fcc9d5">
						<AlarmModel Id="ea009f8675e4271ae6b019160fcc9d5" Severity="[AlarmSeverity]Warning" TriggerModel="a0e57eb6f9ee47bc8ab90e9926a4ea29">
							<ChannelMonitorTriggerModel Alias="[string]a4161c87-ae16-4700-a19d-c665bcfdcdef" AliasToMonitor="[string]Sink 21" Id="a0e57eb6f9ee47bc8ab90e9926a4ea29">
								<AboveValueTriggerModel Id="9f2ff28ecab34d58b5cc3fd858997728" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="77ee372445c348b09d32b68000ca4d1c" Severity="[AlarmSeverity]Critical" TriggerModel="b24be1ad35d646fe87ea8156fd49bc9d">
							<ChannelMonitorTriggerModel Alias="[string]c8e5a60b-3013-4f45-b5ff-6ed538b8f1c1" AliasToMonitor="[string]Sink 21" Id="b24be1ad35d646fe87ea8156fd49bc9d">
								<AboveValueTriggerModel Id="1387168c93cc417eb7130e1d97e80af0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 22" CanDisable="[bool]True" CriticalAlarm="189a875112134e29b3b3d188d60b5917" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="9420d4f2028448baa78a84742dfeca7d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink22" Units="[string]Voltaires" WarningAlarm="b3083cffce69474ca15fd32f025920d6">
						<AlarmModel Id="b3083cffce69474ca15fd32f025920d6" Severity="[AlarmSeverity]Warning" TriggerModel="f1dbf928eb924eeb8a5227be867964af">
							<ChannelMonitorTriggerModel Alias="[string]ae874376-9fe0-415d-b2e4-fb7954235c63" AliasToMonitor="[string]Sink 22" Id="f1dbf928eb924eeb8a5227be867964af">
								<AboveValueTriggerModel Id="8f79fb1780dd474fa08217e2287ea303" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="189a875112134e29b3b3d188d60b5917" Severity="[AlarmSeverity]Critical" TriggerModel="376920790263470b9f8178a9bc83127f">
							<ChannelMonitorTriggerModel Alias="[string]340a7f9c-1dbc-4fd0-bea4-4cf03c6bd169" AliasToMonitor="[string]Sink 22" Id="376920790263470b9f8178a9bc83127f">
								<AboveValueTriggerModel Id="e334dd2ab13648108465df360055282b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 23" CanDisable="[bool]True" CriticalAlarm="9a4bcb5f5714bdeade66c7633a2004e" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="778c1c0d8fd249659c44d15514a5a1aa" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink23" Units="[string]Voltaires" WarningAlarm="e454f5a58a1a48fca2493ac662d56906">
						<AlarmModel Id="e454f5a58a1a48fca2493ac662d56906" Severity="[AlarmSeverity]Warning" TriggerModel="f398faea28ed4934bd32fee1bbe0817f">
							<ChannelMonitorTriggerModel Alias="[string]ac871a53-e578-4394-b37b-c5630d2bbdd2" AliasToMonitor="[string]Sink 23" Id="f398faea28ed4934bd32fee1bbe0817f">
								<AboveValueTriggerModel Id="2e626ced06f441c799d4e99dad5bc932" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="9a4bcb5f5714bdeade66c7633a2004e" Severity="[AlarmSeverity]Critical" TriggerModel="78a2b59e1f42475aa6f6f43070c3e2e2">
							<ChannelMonitorTriggerModel Alias="[string]eb93b948-9778-4995-9d60-18d60617a902" AliasToMonitor="[string]Sink 23" Id="78a2b59e1f42475aa6f6f43070c3e2e2">
								<AboveValueTriggerModel Id="ad1f8c63145743f59ad808bda8e6d87b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 24" CanDisable="[bool]True" CriticalAlarm="5171a7e694b3484dbae2fcfde2d250f2" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="814a1e7407054fd3a43299912a88219a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink24" Units="[string]Voltaires" WarningAlarm="c4a54372aee14736aa98414963e2818b">
						<AlarmModel Id="c4a54372aee14736aa98414963e2818b" Severity="[AlarmSeverity]Warning" TriggerModel="79a0e2bae0f84c6da7390ebb7cf47a8f">
							<ChannelMonitorTriggerModel Alias="[string]47b7373d-12db-420e-9940-a11d35de9b55" AliasToMonitor="[string]Sink 24" Id="79a0e2bae0f84c6da7390ebb7cf47a8f">
								<AboveValueTriggerModel Id="6c0fd2aa725d4e598498eb76309734ca" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5171a7e694b3484dbae2fcfde2d250f2" Severity="[AlarmSeverity]Critical" TriggerModel="2542ad81179c41f49b4327ceecb4a3cc">
							<ChannelMonitorTriggerModel Alias="[string]02b1324a-d4ce-4fb1-a215-f63d566e6c42" AliasToMonitor="[string]Sink 24" Id="2542ad81179c41f49b4327ceecb4a3cc">
								<AboveValueTriggerModel Id="cc663f4700a14735a7fb7402d190898b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 25" CanDisable="[bool]True" CriticalAlarm="4d6ed80a41e44188ae382bc1cd2c72a0" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="82b4f65e2d1845dfa4e4b80858a3a0aa" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink25" Units="[string]Voltaires" WarningAlarm="7800ed8c7c424406804b252accefb252">
						<AlarmModel Id="7800ed8c7c424406804b252accefb252" Severity="[AlarmSeverity]Warning" TriggerModel="85b6f878e7694cf09379b5afa12c5347">
							<ChannelMonitorTriggerModel Alias="[string]6d2b4927-a9d7-4099-b96c-9d686a16f89a" AliasToMonitor="[string]Sink 25" Id="85b6f878e7694cf09379b5afa12c5347">
								<AboveValueTriggerModel Id="45ca9ce701d047a794683f3ecc934312" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="4d6ed80a41e44188ae382bc1cd2c72a0" Severity="[AlarmSeverity]Critical" TriggerModel="bf0860824f2143db8794553ac86da19f">
							<ChannelMonitorTriggerModel Alias="[string]ae5a755c-6d88-415d-9548-1c8b28dc64c2" AliasToMonitor="[string]Sink 25" Id="bf0860824f2143db8794553ac86da19f">
								<AboveValueTriggerModel Id="bbde451b8e494183bd90569459fb1605" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 26" CanDisable="[bool]True" CriticalAlarm="81e4394cfe04229b269a602b5610d84" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="cf5068e8ebf847e58dfd2518bfea6f1c" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink26" Units="[string]Voltaires" WarningAlarm="5c92225685d845b881c49b3e87932b3c">
						<AlarmModel Id="5c92225685d845b881c49b3e87932b3c" Severity="[AlarmSeverity]Warning" TriggerModel="329bf36188a94b68894bb73b39b5aeb1">
							<ChannelMonitorTriggerModel Alias="[string]8bb757da-2563-4fa4-ac20-c093b3f97a0c" AliasToMonitor="[string]Sink 26" Id="329bf36188a94b68894bb73b39b5aeb1">
								<AboveValueTriggerModel Id="4809fabce08d48db9560c2c740a69973" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="81e4394cfe04229b269a602b5610d84" Severity="[AlarmSeverity]Critical" TriggerModel="63615494aa0f4585907c5e06bb95f05b">
							<ChannelMonitorTriggerModel Alias="[string]c703c995-84f8-4dd7-ac88-8032ab69b52a" AliasToMonitor="[string]Sink 26" Id="63615494aa0f4585907c5e06bb95f05b">
								<AboveValueTriggerModel Id="4e5a0cedea649a1b4510d7f86f6d604" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 27" CanDisable="[bool]True" CriticalAlarm="378561ca348242eb9f3765787cd0d54b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="80022dbe66ab4b0c8f32286cf932a99c" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink27" Units="[string]Voltaires" WarningAlarm="86a6634cb1a24da686bf55d14992bde8">
						<AlarmModel Id="86a6634cb1a24da686bf55d14992bde8" Severity="[AlarmSeverity]Warning" TriggerModel="23b131addd2c4955b5f49113cd6c18d2">
							<ChannelMonitorTriggerModel Alias="[string]23e3a963-76cd-4d49-a404-1b8adafdbb58" AliasToMonitor="[string]Sink 27" Id="23b131addd2c4955b5f49113cd6c18d2">
								<AboveValueTriggerModel Id="bf1b976003df4aeebdd7cf45fe22b402" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="378561ca348242eb9f3765787cd0d54b" Severity="[AlarmSeverity]Critical" TriggerModel="4f8442fd61d74b11bbbdbc8f8fd2db88">
							<ChannelMonitorTriggerModel Alias="[string]7030efbb-242b-4726-be06-682495ece2a0" AliasToMonitor="[string]Sink 27" Id="4f8442fd61d74b11bbbdbc8f8fd2db88">
								<AboveValueTriggerModel Id="ecfdc987918e40239930c2b1c7e6ef51" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 28" CanDisable="[bool]True" CriticalAlarm="1ed4ee4fc88248bb8daaa624e38d4d95" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="7ff1f989d81440a08b1f260f10b02c2b" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink28" Units="[string]Voltaires" WarningAlarm="86994b1b331a4d39b7138da164919211">
						<AlarmModel Id="86994b1b331a4d39b7138da164919211" Severity="[AlarmSeverity]Warning" TriggerModel="d6cc1d8a528f46e89ea932c54f1e306c">
							<ChannelMonitorTriggerModel Alias="[string]15416d01-1201-4192-89df-f31125d72360" AliasToMonitor="[string]Sink 28" Id="d6cc1d8a528f46e89ea932c54f1e306c">
								<AboveValueTriggerModel Id="ca02162abe4649a2d6aab5634ed6f6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="1ed4ee4fc88248bb8daaa624e38d4d95" Severity="[AlarmSeverity]Critical" TriggerModel="6e6a32f33ce4f8ebdfc21b55a0c9d34">
							<ChannelMonitorTriggerModel Alias="[string]e2b1a155-5bc8-4fb4-a2c1-05d1c2db26ae" AliasToMonitor="[string]Sink 28" Id="6e6a32f33ce4f8ebdfc21b55a0c9d34">
								<AboveValueTriggerModel Id="ee0998705bdf489f86569dc9cad98551" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 29" CanDisable="[bool]True" CriticalAlarm="915a5af6864049977258710f832bd9" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4c5c3871cbd14f1bb6be0fa3b3f6327d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink29" Units="[string]Voltaires" WarningAlarm="72874a659064a8d89422f1f2a4a67d9">
						<AlarmModel Id="72874a659064a8d89422f1f2a4a67d9" Severity="[AlarmSeverity]Warning" TriggerModel="7d9827fee31c4d71855c8a74df8bfcfb">
							<ChannelMonitorTriggerModel Alias="[string]dbce7064-5165-4262-898b-97171fd04d6f" AliasToMonitor="[string]Sink 29" Id="7d9827fee31c4d71855c8a74df8bfcfb">
								<AboveValueTriggerModel Id="24ab98e4df8242a5b28a2b4dd333d0ac" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="915a5af6864049977258710f832bd9" Severity="[AlarmSeverity]Critical" TriggerModel="541e14de50a541aba38ce57b15103a72">
							<ChannelMonitorTriggerModel Alias="[string]13bcbf2f-e881-42b0-a483-cc169fc9e38b" AliasToMonitor="[string]Sink 29" Id="541e14de50a541aba38ce57b15103a72">
								<AboveValueTriggerModel Id="51eb0cb1780b46a5a2fdc8e528fc950e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 30" CanDisable="[bool]True" CriticalAlarm="5408dd544d2d4da7a3255bc729256f53" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4fd1ee019e9401fa0239c6243e6f865" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink30" Units="[string]Voltaires" WarningAlarm="40ac927d51f84182b0f2733212ffa028">
						<AlarmModel Id="40ac927d51f84182b0f2733212ffa028" Severity="[AlarmSeverity]Warning" TriggerModel="a8e2d121d1d4132a453753a53c415ed">
							<ChannelMonitorTriggerModel Alias="[string]49102b49-9bf8-4f6c-823e-91944c341105" AliasToMonitor="[string]Sink 30" Id="a8e2d121d1d4132a453753a53c415ed">
								<AboveValueTriggerModel Id="4a428a8de4ed407e9eed8f20407e9fa6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5408dd544d2d4da7a3255bc729256f53" Severity="[AlarmSeverity]Critical" TriggerModel="554d2527074a463cb1dbac7f3c809615">
							<ChannelMonitorTriggerModel Alias="[string]2e7f1771-ac3a-48ea-8443-65101781faa3" AliasToMonitor="[string]Sink 30" Id="554d2527074a463cb1dbac7f3c809615">
								<AboveValueTriggerModel Id="bc5f62714d6d447d84d2a287fb88465d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 31" CanDisable="[bool]True" CriticalAlarm="5a875ab7c26f426e87bbc9caf1f4da02" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="5caa891cf2a44114a9b2f7f2eb6ea0d3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink31" Units="[string]Voltaires" WarningAlarm="6fad029da2cf4827afcb657c642549be">
						<AlarmModel Id="6fad029da2cf4827afcb657c642549be" Severity="[AlarmSeverity]Warning" TriggerModel="43207dc64eaf4b10a8a49f08c910ae4f">
							<ChannelMonitorTriggerModel Alias="[string]b9bfecc1-2e34-42bc-a0f1-98191ce6e4b4" AliasToMonitor="[string]Sink 31" Id="43207dc64eaf4b10a8a49f08c910ae4f">
								<AboveValueTriggerModel Id="aca3460365eb43d8a7ec65be3e290579" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5a875ab7c26f426e87bbc9caf1f4da02" Severity="[AlarmSeverity]Critical" TriggerModel="7b34a548ea6e413887c8d4486d6d85e4">
							<ChannelMonitorTriggerModel Alias="[string]51efb074-c3a2-4e94-94eb-4227f259d714" AliasToMonitor="[string]Sink 31" Id="7b34a548ea6e413887c8d4486d6d85e4">
								<AboveValueTriggerModel Id="8952f825c91b4f0aa9071ae065036bae" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 32" CanDisable="[bool]True" CriticalAlarm="27bdf40de4944a75914c2d059522b0fd" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="59dec6c1596749c39914c62f052424c5" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink32" Units="[string]Voltaires" WarningAlarm="8b170bc90b8140e9aca29b30961dfc3b">
						<AlarmModel Id="8b170bc90b8140e9aca29b30961dfc3b" Severity="[AlarmSeverity]Warning" TriggerModel="302b3102c86c42538a8973ed49c197a4">
							<ChannelMonitorTriggerModel Alias="[string]163b63f6-faa6-4264-a820-3cc214a7125a" AliasToMonitor="[string]Sink 32" Id="302b3102c86c42538a8973ed49c197a4">
								<AboveValueTriggerModel Id="8d530ff8b7a48b78932a9027c148116" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="27bdf40de4944a75914c2d059522b0fd" Severity="[AlarmSeverity]Critical" TriggerModel="d22d98d8517547898183be77603957cd">
							<ChannelMonitorTriggerModel Alias="[string]2b60c5fa-eb1f-47a7-a199-7757be2f61d5" AliasToMonitor="[string]Sink 32" Id="d22d98d8517547898183be77603957cd">
								<AboveValueTriggerModel Id="6c441c3afddb46a4bd4a01b1c51d24f3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 33" CanDisable="[bool]True" CriticalAlarm="e3579d7ab63e432ca9fa71114c087a46" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="276694cbbbdb45c0958c5c47110ab40e" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink33" Units="[string]Voltaires" WarningAlarm="51628546dac5468aaeb5d1450c38bc89">
						<AlarmModel Id="51628546dac5468aaeb5d1450c38bc89" Severity="[AlarmSeverity]Warning" TriggerModel="a90f3bde00804ebda249eddcdaff5b1c">
							<ChannelMonitorTriggerModel Alias="[string]cd4cbe1b-ce07-4e85-92df-e391b9749537" AliasToMonitor="[string]Sink 33" Id="a90f3bde00804ebda249eddcdaff5b1c">
								<AboveValueTriggerModel Id="a5695608934f4b5899cb2f1d27239326" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="e3579d7ab63e432ca9fa71114c087a46" Severity="[AlarmSeverity]Critical" TriggerModel="336b112a24224650aae84b0baf0b9e01">
							<ChannelMonitorTriggerModel Alias="[string]c0fcf612-9fc0-48a8-ad23-8daf0964b325" AliasToMonitor="[string]Sink 33" Id="336b112a24224650aae84b0baf0b9e01">
								<AboveValueTriggerModel Id="8d0d182af63c45a3b008d7768363dedd" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 34" CanDisable="[bool]True" CriticalAlarm="8357bf1f22494cfe9b7f71504a237198" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="a6ca89847a7749f4be6f43530aeb0c68" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink34" Units="[string]Voltaires" WarningAlarm="b6578c02acff466f9df2a48f4252e918">
						<AlarmModel Id="b6578c02acff466f9df2a48f4252e918" Severity="[AlarmSeverity]Warning" TriggerModel="f6a30050b00f4b79b6580167fb7f4309">
							<ChannelMonitorTriggerModel Alias="[string]7cdb9979-f37c-4a69-9982-fb5eb2a96cc9" AliasToMonitor="[string]Sink 34" Id="f6a30050b00f4b79b6580167fb7f4309">
								<AboveValueTriggerModel Id="6edfbad727b14aafb646401e545ef867" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="8357bf1f22494cfe9b7f71504a237198" Severity="[AlarmSeverity]Critical" TriggerModel="c6875b06fdc240b9881a859a5f84deaf">
							<ChannelMonitorTriggerModel Alias="[string]95a2f5aa-d385-4e71-b1c2-a8ba564e895e" AliasToMonitor="[string]Sink 34" Id="c6875b06fdc240b9881a859a5f84deaf">
								<AboveValueTriggerModel Id="9eda3971f8e645058269a44e975e7c9e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 35" CanDisable="[bool]True" CriticalAlarm="24b0d93dcfa44760998b172c3bdbe1bb" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6d5aad603d614540b08441b55b0fec35" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink35" Units="[string]Voltaires" WarningAlarm="7612a620b3df45bf81598c5e8d31abbb">
						<AlarmModel Id="7612a620b3df45bf81598c5e8d31abbb" Severity="[AlarmSeverity]Warning" TriggerModel="bc70cb52f40b41e3ae18c454a12ac10a">
							<ChannelMonitorTriggerModel Alias="[string]eb8b5eed-9423-45f4-89bb-21be82954084" AliasToMonitor="[string]Sink 35" Id="bc70cb52f40b41e3ae18c454a12ac10a">
								<AboveValueTriggerModel Id="7ab45521595b4818b26982db948f93df" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="24b0d93dcfa44760998b172c3bdbe1bb" Severity="[AlarmSeverity]Critical" TriggerModel="4e0a3de796f741e393090f3f8a28cc6e">
							<ChannelMonitorTriggerModel Alias="[string]09a60288-2e1e-4de0-a418-bb13232e169f" AliasToMonitor="[string]Sink 35" Id="4e0a3de796f741e393090f3f8a28cc6e">
								<AboveValueTriggerModel Id="fc45a2cd365f499bb269e0e270a245ef" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 36" CanDisable="[bool]True" CriticalAlarm="894e245fe3af4acaae779de5eb676036" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="ba0da5f8775a45b8b0fca1d85a22212a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink36" Units="[string]Voltaires" WarningAlarm="c59f872b2ae7404799956f3f100a638a">
						<AlarmModel Id="c59f872b2ae7404799956f3f100a638a" Severity="[AlarmSeverity]Warning" TriggerModel="e93af745c1cb4781a45c71feff4e776f">
							<ChannelMonitorTriggerModel Alias="[string]fcd6f221-809d-42c7-9a7a-0ba175e5401e" AliasToMonitor="[string]Sink 36" Id="e93af745c1cb4781a45c71feff4e776f">
								<AboveValueTriggerModel Id="5f161e4e47774587837c4004801b123f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="894e245fe3af4acaae779de5eb676036" Severity="[AlarmSeverity]Critical" TriggerModel="681bd5bb08904af6be2bae9ddd8b6146">
							<ChannelMonitorTriggerModel Alias="[string]824193d8-c8f2-4463-8eb3-6e0b741d5bf9" AliasToMonitor="[string]Sink 36" Id="681bd5bb08904af6be2bae9ddd8b6146">
								<AboveValueTriggerModel Id="a24e4c63109b4cc4adb5e7c5edd44267" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 37" CanDisable="[bool]True" CriticalAlarm="7c3322a47ee0452fa55bed1996604125" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="b66a9b77a0ed461b8bc5aaabb11e157a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink37" Units="[string]Voltaires" WarningAlarm="cd2cba91bb54a62a4e8134a7681db04">
						<AlarmModel Id="cd2cba91bb54a62a4e8134a7681db04" Severity="[AlarmSeverity]Warning" TriggerModel="d5ad66947de4a10a005ccabd8f46c51">
							<ChannelMonitorTriggerModel Alias="[string]328bf0f5-140d-420a-99db-118ab6ebc335" AliasToMonitor="[string]Sink 37" Id="d5ad66947de4a10a005ccabd8f46c51">
								<AboveValueTriggerModel Id="152c37060dab40a1a2661a8a9b123f07" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7c3322a47ee0452fa55bed1996604125" Severity="[AlarmSeverity]Critical" TriggerModel="a107714d5c3b4fdaa7a027c424701e4d">
							<ChannelMonitorTriggerModel Alias="[string]0b5519bf-714a-4087-bf35-5663c3d6e068" AliasToMonitor="[string]Sink 37" Id="a107714d5c3b4fdaa7a027c424701e4d">
								<AboveValueTriggerModel Id="f8138dc5601d42ef8089c6888ad457d8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 38" CanDisable="[bool]True" CriticalAlarm="18d73e1b94a64a6e954a079375e6a176" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="e0abb41e81b0493ebb4d9d2a545fb66c" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink38" Units="[string]Voltaires" WarningAlarm="7d9dc834c051426ca5eed955fd894083">
						<AlarmModel Id="7d9dc834c051426ca5eed955fd894083" Severity="[AlarmSeverity]Warning" TriggerModel="4bbe3aaa81a94b09a8e40f0806df24dd">
							<ChannelMonitorTriggerModel Alias="[string]8f28729b-13e7-4d32-b92c-a979a4fcb014" AliasToMonitor="[string]Sink 38" Id="4bbe3aaa81a94b09a8e40f0806df24dd">
								<AboveValueTriggerModel Id="4988d41d8b794676a604dd57b33efba9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="18d73e1b94a64a6e954a079375e6a176" Severity="[AlarmSeverity]Critical" TriggerModel="2dbc6e12e192483b831fd8dbda9a7844">
							<ChannelMonitorTriggerModel Alias="[string]29aedd2a-a21f-4ad5-af2a-7de72eefbfc0" AliasToMonitor="[string]Sink 38" Id="2dbc6e12e192483b831fd8dbda9a7844">
								<AboveValueTriggerModel Id="5f77efc358d14b018fa3a8df5fb3e758" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 39" CanDisable="[bool]True" CriticalAlarm="9802fd41b544f6e86e59ab5f06eba48" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="34c686d2efb94ff9930a364bfe33d5f9" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink39" Units="[string]Voltaires" WarningAlarm="6774cf9193e54e51bd918fdb936adfc6">
						<AlarmModel Id="6774cf9193e54e51bd918fdb936adfc6" Severity="[AlarmSeverity]Warning" TriggerModel="e730c6454b3846ffa79ca2ad1f0f01a3">
							<ChannelMonitorTriggerModel Alias="[string]f9e8aa07-8970-4e48-8ba5-4eba1b1d5228" AliasToMonitor="[string]Sink 39" Id="e730c6454b3846ffa79ca2ad1f0f01a3">
								<AboveValueTriggerModel Id="3bb149b5f7384a0a9979936060faea9a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="9802fd41b544f6e86e59ab5f06eba48" Severity="[AlarmSeverity]Critical" TriggerModel="cd63658d7fb5495dbb60aa4c7899a8a1">
							<ChannelMonitorTriggerModel Alias="[string]4b72e2a3-9233-4cd1-ad2e-bd633e53179d" AliasToMonitor="[string]Sink 39" Id="cd63658d7fb5495dbb60aa4c7899a8a1">
								<AboveValueTriggerModel Id="d79d8d062c7d4759b0fc6547bab7dc2f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 40" CanDisable="[bool]True" CriticalAlarm="2d62d8a341b8491dab87aa501dcbfe2c" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="f2f719e0c7d4ed0b66c52d07b0b496b" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink40" Units="[string]Voltaires" WarningAlarm="9f2beb90bc6b408b9893f8be0d9f99d3">
						<AlarmModel Id="9f2beb90bc6b408b9893f8be0d9f99d3" Severity="[AlarmSeverity]Warning" TriggerModel="69f94d6cf5a04c97a2c8bfe5630ee1ea">
							<ChannelMonitorTriggerModel Alias="[string]b67372ff-b7b1-4a56-beea-380ec5433697" AliasToMonitor="[string]Sink 40" Id="69f94d6cf5a04c97a2c8bfe5630ee1ea">
								<AboveValueTriggerModel Id="e90853133ff84a4698e272e4e314d7fd" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="2d62d8a341b8491dab87aa501dcbfe2c" Severity="[AlarmSeverity]Critical" TriggerModel="329c77f70824416b9208b1d3722629d5">
							<ChannelMonitorTriggerModel Alias="[string]b41ae761-0ca5-4950-ab38-2a7e45c26c6a" AliasToMonitor="[string]Sink 40" Id="329c77f70824416b9208b1d3722629d5">
								<AboveValueTriggerModel Id="aa601ecc58844517a5e21208c10d3d23" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 41" CanDisable="[bool]True" CriticalAlarm="5775e6fc91b04f8c9275ae3806c77182" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="93c0e891cb0f4a9d99d9c3adba5e276e" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink41" Units="[string]Voltaires" WarningAlarm="616914eb29704ac7a0a30bcbf563de2b">
						<AlarmModel Id="616914eb29704ac7a0a30bcbf563de2b" Severity="[AlarmSeverity]Warning" TriggerModel="71e368c1e34045f3b63cb703ea08f7fb">
							<ChannelMonitorTriggerModel Alias="[string]66545fea-22dd-4ff7-9e83-9b2534d0423e" AliasToMonitor="[string]Sink 41" Id="71e368c1e34045f3b63cb703ea08f7fb">
								<AboveValueTriggerModel Id="a1434dcce6a748a68642720f471e2b01" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5775e6fc91b04f8c9275ae3806c77182" Severity="[AlarmSeverity]Critical" TriggerModel="a217fb0a82c144c981e14fbd159f75fa">
							<ChannelMonitorTriggerModel Alias="[string]934c7c57-f87d-4c87-926c-3cb7f60c0a06" AliasToMonitor="[string]Sink 41" Id="a217fb0a82c144c981e14fbd159f75fa">
								<AboveValueTriggerModel Id="bbebb09f38df4893a9bcfd6a4c821448" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 42" CanDisable="[bool]True" CriticalAlarm="d7916abbf8d942efa2669ed3b5f16682" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="798ce75f512f4c90aa66b1f6ed76691f" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink42" Units="[string]Voltaires" WarningAlarm="a0b8b5e3b671494987d809dba249ece1">
						<AlarmModel Id="a0b8b5e3b671494987d809dba249ece1" Severity="[AlarmSeverity]Warning" TriggerModel="8f94621e1dce41f5a58b8e8577af1858">
							<ChannelMonitorTriggerModel Alias="[string]6f4e6a8a-1305-406d-a4db-a5f8aa6c23c7" AliasToMonitor="[string]Sink 42" Id="8f94621e1dce41f5a58b8e8577af1858">
								<AboveValueTriggerModel Id="f5a177afebea4789a712789636785a57" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="d7916abbf8d942efa2669ed3b5f16682" Severity="[AlarmSeverity]Critical" TriggerModel="8eb6efc30cbc45acab3f334ce9dee6b6">
							<ChannelMonitorTriggerModel Alias="[string]6e5aed1f-e551-4273-b213-49619e49b7f8" AliasToMonitor="[string]Sink 42" Id="8eb6efc30cbc45acab3f334ce9dee6b6">
								<AboveValueTriggerModel Id="4fa96f08509b43939ffa5e28e6860de8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 43" CanDisable="[bool]True" CriticalAlarm="fb83c948b2b0456e85692bbbd1b77228" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6dce7f5e9b9d4089b7ab89fadac4b86d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink43" Units="[string]Voltaires" WarningAlarm="a8ad1d8b996a4a7abafa12e41a0001cc">
						<AlarmModel Id="a8ad1d8b996a4a7abafa12e41a0001cc" Severity="[AlarmSeverity]Warning" TriggerModel="7ee0d8fa32ed41a18002db954ff249e6">
							<ChannelMonitorTriggerModel Alias="[string]6bea0f19-1847-4cc3-996a-2a6c7549524f" AliasToMonitor="[string]Sink 43" Id="7ee0d8fa32ed41a18002db954ff249e6">
								<AboveValueTriggerModel Id="c1559bf36c0d40699442e7bbd6e000ed" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="fb83c948b2b0456e85692bbbd1b77228" Severity="[AlarmSeverity]Critical" TriggerModel="6f16fb77b249465b8a54b592c7c29dc2">
							<ChannelMonitorTriggerModel Alias="[string]760f55b0-693d-4b01-a6d7-c1c2b27f8844" AliasToMonitor="[string]Sink 43" Id="6f16fb77b249465b8a54b592c7c29dc2">
								<AboveValueTriggerModel Id="53be921bafce4ef6afba4d747e7e4735" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 44" CanDisable="[bool]True" CriticalAlarm="cbddd97df944a40ba3c49f7e0498925" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="b3499c2c283442469ac0c628436ecb63" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink44" Units="[string]Voltaires" WarningAlarm="8b6c2be7424a4f6487e0fa125ae15421">
						<AlarmModel Id="8b6c2be7424a4f6487e0fa125ae15421" Severity="[AlarmSeverity]Warning" TriggerModel="843449daa0654270adb7c31d41372dcc">
							<ChannelMonitorTriggerModel Alias="[string]18731b12-03ed-4ca7-b3f7-40b8448ff996" AliasToMonitor="[string]Sink 44" Id="843449daa0654270adb7c31d41372dcc">
								<AboveValueTriggerModel Id="17ab18f60bbd40c393fab8580a23e194" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="cbddd97df944a40ba3c49f7e0498925" Severity="[AlarmSeverity]Critical" TriggerModel="916f31acc27b46a6aa139436c95d9583">
							<ChannelMonitorTriggerModel Alias="[string]eb40120d-a1e5-4db2-8a0d-2cc8a76c8a16" AliasToMonitor="[string]Sink 44" Id="916f31acc27b46a6aa139436c95d9583">
								<AboveValueTriggerModel Id="6e93550c3e2e40189b4d394897d49f00" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 45" CanDisable="[bool]True" CriticalAlarm="a8baa69bfde049ed9413ef91fd349872" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="50b51dd33d124fe4b3a32787a08507a0" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink45" Units="[string]Voltaires" WarningAlarm="1b3f596127bb4aaf9304f9ebbfe884b5">
						<AlarmModel Id="1b3f596127bb4aaf9304f9ebbfe884b5" Severity="[AlarmSeverity]Warning" TriggerModel="7fdb0005d9e54fb58d00217cf91ec007">
							<ChannelMonitorTriggerModel Alias="[string]77cbf40d-7d98-48c2-9abc-93bb1e84e300" AliasToMonitor="[string]Sink 45" Id="7fdb0005d9e54fb58d00217cf91ec007">
								<AboveValueTriggerModel Id="7445037784914e079343e3b8c5077256" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="a8baa69bfde049ed9413ef91fd349872" Severity="[AlarmSeverity]Critical" TriggerModel="4aef06cee829435fbe6cf596bb325039">
							<ChannelMonitorTriggerModel Alias="[string]b6eda3ab-b23a-4041-b4c4-842c2c815780" AliasToMonitor="[string]Sink 45" Id="4aef06cee829435fbe6cf596bb325039">
								<AboveValueTriggerModel Id="4d42a85d64514ffab36dc94013146025" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 46" CanDisable="[bool]True" CriticalAlarm="8e13854948e04ff6b6dd53da5e042c78" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="a5a3957a759a42fd82ca7181ffe2e854" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink46" Units="[string]Voltaires" WarningAlarm="89b27d203f3047bbba9cafcd0431ee53">
						<AlarmModel Id="89b27d203f3047bbba9cafcd0431ee53" Severity="[AlarmSeverity]Warning" TriggerModel="e8b7129a03b64a54ae97e09ae334693d">
							<ChannelMonitorTriggerModel Alias="[string]99e2d4c1-571e-43aa-b18b-b21aee44fb61" AliasToMonitor="[string]Sink 46" Id="e8b7129a03b64a54ae97e09ae334693d">
								<AboveValueTriggerModel Id="5f61827094ea4fc6aef1942e0eb77a28" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="8e13854948e04ff6b6dd53da5e042c78" Severity="[AlarmSeverity]Critical" TriggerModel="2eb66891ce17441798fdf84967d2c209">
							<ChannelMonitorTriggerModel Alias="[string]55da6593-903e-4ab5-9c5f-5a7e5a363f24" AliasToMonitor="[string]Sink 46" Id="2eb66891ce17441798fdf84967d2c209">
								<AboveValueTriggerModel Id="13855c3e41654162af06771be0e11320" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 47" CanDisable="[bool]True" CriticalAlarm="4ceed247f74e42228e9698387c980ffb" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4ad54ac11fd14e7cb16e2058baf99288" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink47" Units="[string]Voltaires" WarningAlarm="e57672b76db44c4e85460aed561c059a">
						<AlarmModel Id="e57672b76db44c4e85460aed561c059a" Severity="[AlarmSeverity]Warning" TriggerModel="2b34aca5c74d42be81157bbad8d859e9">
							<ChannelMonitorTriggerModel Alias="[string]f4a5d9fc-1cc8-41d7-81cc-dbd231a703a1" AliasToMonitor="[string]Sink 47" Id="2b34aca5c74d42be81157bbad8d859e9">
								<AboveValueTriggerModel Id="77875372d67f4b6fa4f6e66c4c86adeb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="4ceed247f74e42228e9698387c980ffb" Severity="[AlarmSeverity]Critical" TriggerModel="bffe42ba9d6841678371d2caf3cbef4f">
							<ChannelMonitorTriggerModel Alias="[string]76b64060-a796-4649-a8ca-7335b4db3650" AliasToMonitor="[string]Sink 47" Id="bffe42ba9d6841678371d2caf3cbef4f">
								<AboveValueTriggerModel Id="d772de0364c44e9cb500bbcb63834c08" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 48" CanDisable="[bool]True" CriticalAlarm="c14f3c9a074843558434b0627192bf72" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c7d7da93f2764abc8fa6cdb28f7644d9" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink48" Units="[string]Voltaires" WarningAlarm="f9e65f98c30b47f186fbc532bd3a0095">
						<AlarmModel Id="f9e65f98c30b47f186fbc532bd3a0095" Severity="[AlarmSeverity]Warning" TriggerModel="3cd6e8c70fa94b6d98ecccd16631c6d6">
							<ChannelMonitorTriggerModel Alias="[string]726d21a1-937a-43c3-a2aa-a36c4c07bfc0" AliasToMonitor="[string]Sink 48" Id="3cd6e8c70fa94b6d98ecccd16631c6d6">
								<AboveValueTriggerModel Id="5f6f7af1e16d4350a99b80d43d4deec7" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="c14f3c9a074843558434b0627192bf72" Severity="[AlarmSeverity]Critical" TriggerModel="55b9f663d2524f9d8955abc544b6a7e4">
							<ChannelMonitorTriggerModel Alias="[string]6acfc595-f5a0-48e7-bb91-33ddb923fa25" AliasToMonitor="[string]Sink 48" Id="55b9f663d2524f9d8955abc544b6a7e4">
								<AboveValueTriggerModel Id="3521d0a943dd431dbe49dc3bf57918f3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 49" CanDisable="[bool]True" CriticalAlarm="8f2556f95bbe46a0942b7106720b0c1b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="f92f198ed69745cdbc373d8009fe99f5" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink49" Units="[string]Voltaires" WarningAlarm="a61e7429f47441c9a7560f38d2f69cd4">
						<AlarmModel Id="a61e7429f47441c9a7560f38d2f69cd4" Severity="[AlarmSeverity]Warning" TriggerModel="f03bb953df94416e8ebe4abc147c7114">
							<ChannelMonitorTriggerModel Alias="[string]6c2ab9a4-a964-4ff1-a099-d78d82617a34" AliasToMonitor="[string]Sink 49" Id="f03bb953df94416e8ebe4abc147c7114">
								<AboveValueTriggerModel Id="db5ea32d35b24c389a294939dfa0e55c" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="8f2556f95bbe46a0942b7106720b0c1b" Severity="[AlarmSeverity]Critical" TriggerModel="603d93f5695347b7a940f410eb7decb4">
							<ChannelMonitorTriggerModel Alias="[string]1c933321-179f-4c4b-b48e-884c8f94b2ad" AliasToMonitor="[string]Sink 49" Id="603d93f5695347b7a940f410eb7decb4">
								<AboveValueTriggerModel Id="c35d1395cb914bb3afa672dfdbefac3f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 50" CanDisable="[bool]True" CriticalAlarm="2919356c73a141d1a5e074f8495a2114" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="b325bedd809432f869f2058b9b7ea72" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink50" Units="[string]Voltaires" WarningAlarm="17f7afe25214c29942038f5f6a9c5ab">
						<AlarmModel Id="17f7afe25214c29942038f5f6a9c5ab" Severity="[AlarmSeverity]Warning" TriggerModel="2e003e4e7e384fc9b782e20a95ee7699">
							<ChannelMonitorTriggerModel Alias="[string]e6499c2e-1ade-4df3-b995-743b2a087618" AliasToMonitor="[string]Sink 50" Id="2e003e4e7e384fc9b782e20a95ee7699">
								<AboveValueTriggerModel Id="21c8daf8e2e94391bd792c827c51b984" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="2919356c73a141d1a5e074f8495a2114" Severity="[AlarmSeverity]Critical" TriggerModel="c07ffb919b64dc98725d64f01a5e40e">
							<ChannelMonitorTriggerModel Alias="[string]d144bb87-530c-4cb4-9f44-c326bbefb150" AliasToMonitor="[string]Sink 50" Id="c07ffb919b64dc98725d64f01a5e40e">
								<AboveValueTriggerModel Id="71e22a3202ba40b6bc0fd8a5ca097fb9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 51" CanDisable="[bool]True" CriticalAlarm="97a5337595b74d40adfd8072136b726c" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="ed4aa2cd10b94c11bc22f7ce71634a9d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink51" Units="[string]Voltaires" WarningAlarm="83629b5a635d439c9e0f29046716b804">
						<AlarmModel Id="83629b5a635d439c9e0f29046716b804" Severity="[AlarmSeverity]Warning" TriggerModel="f390c4e163264a5eb818db0c5275d545">
							<ChannelMonitorTriggerModel Alias="[string]052a75b4-7128-4325-85ae-c454de2983db" AliasToMonitor="[string]Sink 51" Id="f390c4e163264a5eb818db0c5275d545">
								<AboveValueTriggerModel Id="d536253e6fb34e0fbacd7110cbac7e8d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="97a5337595b74d40adfd8072136b726c" Severity="[AlarmSeverity]Critical" TriggerModel="8f75c971a1ed41119b4603b55018daa6">
							<ChannelMonitorTriggerModel Alias="[string]d9307356-ff09-4f5e-bf92-c77bd2806dba" AliasToMonitor="[string]Sink 51" Id="8f75c971a1ed41119b4603b55018daa6">
								<AboveValueTriggerModel Id="1b47b258433c47498bf808a16b4b96fb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 52" CanDisable="[bool]True" CriticalAlarm="49e7bbf977ab40b9a85dcb8342e0f4da" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="942313a3516a43d49f44ab68140cec21" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink52" Units="[string]Voltaires" WarningAlarm="efcd7e2b640a47f99d88dae8360d611c">
						<AlarmModel Id="efcd7e2b640a47f99d88dae8360d611c" Severity="[AlarmSeverity]Warning" TriggerModel="2afaab8d0cb04f3eab09a8b12eb07132">
							<ChannelMonitorTriggerModel Alias="[string]d88a9a4b-fa9d-46b6-bc65-c48d2fb778b0" AliasToMonitor="[string]Sink 52" Id="2afaab8d0cb04f3eab09a8b12eb07132">
								<AboveValueTriggerModel Id="10641c8af3c0471eb90f7b196e029688" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="49e7bbf977ab40b9a85dcb8342e0f4da" Severity="[AlarmSeverity]Critical" TriggerModel="2062633fa1524403a17b260489df8535">
							<ChannelMonitorTriggerModel Alias="[string]5045839f-e2d8-4e60-add7-7726af50cbca" AliasToMonitor="[string]Sink 52" Id="2062633fa1524403a17b260489df8535">
								<AboveValueTriggerModel Id="58fcbc08222b41df80b5000ab46a296c" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 53" CanDisable="[bool]True" CriticalAlarm="9fc66fa6bf36465aaa664d5bda9be9b8" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="3c438fe2be6346faa64408a7cdda7421" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink53" Units="[string]Voltaires" WarningAlarm="8c46b1d975b40cfbfa4686efcc322bc">
						<AlarmModel Id="8c46b1d975b40cfbfa4686efcc322bc" Severity="[AlarmSeverity]Warning" TriggerModel="c9797b2ea5e24b56a7a9f5d240ad89ad">
							<ChannelMonitorTriggerModel Alias="[string]8ca659f1-49b2-4724-a725-cb29f6025e27" AliasToMonitor="[string]Sink 53" Id="c9797b2ea5e24b56a7a9f5d240ad89ad">
								<AboveValueTriggerModel Id="7c116beda5f54b5181e4b9a712b47748" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="9fc66fa6bf36465aaa664d5bda9be9b8" Severity="[AlarmSeverity]Critical" TriggerModel="be6c871812854c40ad6a6930016fa272">
							<ChannelMonitorTriggerModel Alias="[string]4c042ba3-5060-4334-ab7f-a64164d7b5d7" AliasToMonitor="[string]Sink 53" Id="be6c871812854c40ad6a6930016fa272">
								<AboveValueTriggerModel Id="42e3d387c954713b2bb3d0456261e2d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 54" CanDisable="[bool]True" CriticalAlarm="21e0be1c8d1b4635b0695c7d49e2190e" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="1c2f19dda30e41b8891f93b2c28d82c2" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink54" Units="[string]Voltaires" WarningAlarm="991cceac260047089e07b6dd99282796">
						<AlarmModel Id="991cceac260047089e07b6dd99282796" Severity="[AlarmSeverity]Warning" TriggerModel="a991480b171447fb9d2e48eab42e4514">
							<ChannelMonitorTriggerModel Alias="[string]cabb5351-6569-440d-8882-2cca7129076d" AliasToMonitor="[string]Sink 54" Id="a991480b171447fb9d2e48eab42e4514">
								<AboveValueTriggerModel Id="3c84b3b7459f4cb996506ecc251c841e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="21e0be1c8d1b4635b0695c7d49e2190e" Severity="[AlarmSeverity]Critical" TriggerModel="3f2302439107497892f2e02fdeb1545e">
							<ChannelMonitorTriggerModel Alias="[string]31646861-c098-4ce5-9cc3-c2bcd9b03e16" AliasToMonitor="[string]Sink 54" Id="3f2302439107497892f2e02fdeb1545e">
								<AboveValueTriggerModel Id="cb936078825490883f3573bdfb47448" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 55" CanDisable="[bool]True" CriticalAlarm="ab21cd5f9afa4b2eab4db64a1a49c481" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="22d3aa808cdd401486c92d7e4eb1e129" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink55" Units="[string]Voltaires" WarningAlarm="1d17de8bd58c449fa4720ddc1b481dd1">
						<AlarmModel Id="1d17de8bd58c449fa4720ddc1b481dd1" Severity="[AlarmSeverity]Warning" TriggerModel="bc1b0bff8fda421db840ea84ce5ed211">
							<ChannelMonitorTriggerModel Alias="[string]4d4d7f09-e2a9-46cd-b751-751545b0d225" AliasToMonitor="[string]Sink 55" Id="bc1b0bff8fda421db840ea84ce5ed211">
								<AboveValueTriggerModel Id="c4c2a86111d84517b4038d0a82f0c85d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="ab21cd5f9afa4b2eab4db64a1a49c481" Severity="[AlarmSeverity]Critical" TriggerModel="2d96ba44b80a48249e197dcd6c24505f">
							<ChannelMonitorTriggerModel Alias="[string]31f6a141-9e58-4c9f-9d57-a88a1c1a6645" AliasToMonitor="[string]Sink 55" Id="2d96ba44b80a48249e197dcd6c24505f">
								<AboveValueTriggerModel Id="c0ea817e1894597882cc45c36a948e6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 56" CanDisable="[bool]True" CriticalAlarm="cd4974b02dbc4fa7986b19e4f12f55a5" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="15dc76239b4d4d5a90bd6b3c60a30e86" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink56" Units="[string]Voltaires" WarningAlarm="76239a69afe14afa8302526ebb71719e">
						<AlarmModel Id="76239a69afe14afa8302526ebb71719e" Severity="[AlarmSeverity]Warning" TriggerModel="e622dc48e0e143fd876588651d93b365">
							<ChannelMonitorTriggerModel Alias="[string]5b59f23c-ce07-4145-a2e7-62c169fadb85" AliasToMonitor="[string]Sink 56" Id="e622dc48e0e143fd876588651d93b365">
								<AboveValueTriggerModel Id="da1dd20aab4a4ddc8d44b0fc17b4ba92" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="cd4974b02dbc4fa7986b19e4f12f55a5" Severity="[AlarmSeverity]Critical" TriggerModel="143ca495be6a4a3a8f2c7b5a5b416c83">
							<ChannelMonitorTriggerModel Alias="[string]901384b3-9ec7-4def-bf11-ff6398a37286" AliasToMonitor="[string]Sink 56" Id="143ca495be6a4a3a8f2c7b5a5b416c83">
								<AboveValueTriggerModel Id="23076f8ec62a481e8977385e1b92f84a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 57" CanDisable="[bool]True" CriticalAlarm="3ed7cfe7d118469aa1e9d0c278b1e469" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="36c437f932d74d43ad16a1b79a906bfc" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink57" Units="[string]Voltaires" WarningAlarm="dbb667bf71ac479b9fc4ffdfdf4a4001">
						<AlarmModel Id="dbb667bf71ac479b9fc4ffdfdf4a4001" Severity="[AlarmSeverity]Warning" TriggerModel="4ebb88eb7d3e46ce97062fd0bef7b481">
							<ChannelMonitorTriggerModel Alias="[string]45e5da59-b426-441e-8e8f-e2ff80062f2a" AliasToMonitor="[string]Sink 57" Id="4ebb88eb7d3e46ce97062fd0bef7b481">
								<AboveValueTriggerModel Id="854ccaaeb0ed49649aa9bbc60edaa7a7" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="3ed7cfe7d118469aa1e9d0c278b1e469" Severity="[AlarmSeverity]Critical" TriggerModel="840e0fb47fb64cbca1f2db11da8c80c1">
							<ChannelMonitorTriggerModel Alias="[string]0f6a36bb-0bbd-4a50-aee6-bec81cc819e2" AliasToMonitor="[string]Sink 57" Id="840e0fb47fb64cbca1f2db11da8c80c1">
								<AboveValueTriggerModel Id="9aadda97fb4b446fba4f8ade6b11b785" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 58" CanDisable="[bool]True" CriticalAlarm="52d672a6b9574839a0fa9cd4637e18ad" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="f7c25909134844cc9bb2ed81b3023f6d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink58" Units="[string]Voltaires" WarningAlarm="53700b4eea4948eda577032a1d1a2d30">
						<AlarmModel Id="53700b4eea4948eda577032a1d1a2d30" Severity="[AlarmSeverity]Warning" TriggerModel="ac03ab99eb154b1bae58efa0d76a2926">
							<ChannelMonitorTriggerModel Alias="[string]59c1baad-bca5-4e98-ad89-f4e78292d251" AliasToMonitor="[string]Sink 58" Id="ac03ab99eb154b1bae58efa0d76a2926">
								<AboveValueTriggerModel Id="99c54f3ef5bf4d949f9ce314f51fb869" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="52d672a6b9574839a0fa9cd4637e18ad" Severity="[AlarmSeverity]Critical" TriggerModel="dc0d15197b484e199ac7ae28745ad4d7">
							<ChannelMonitorTriggerModel Alias="[string]1d5fdb74-bfb3-4486-a654-8a532f7b66c4" AliasToMonitor="[string]Sink 58" Id="dc0d15197b484e199ac7ae28745ad4d7">
								<AboveValueTriggerModel Id="f8927ed6497245ac84dbc713863ce45e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 59" CanDisable="[bool]True" CriticalAlarm="45663b78ba7e4176b5c28bda899a204a" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="d668c0d627984e1cb4a3c6147425f2c3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink59" Units="[string]Voltaires" WarningAlarm="fa0bac115d8342fe87f500bf53c76420">
						<AlarmModel Id="fa0bac115d8342fe87f500bf53c76420" Severity="[AlarmSeverity]Warning" TriggerModel="766acc00f44446588b3ffe79538e32bc">
							<ChannelMonitorTriggerModel Alias="[string]b1b52888-d332-4664-b0f7-82e33de4ab1d" AliasToMonitor="[string]Sink 59" Id="766acc00f44446588b3ffe79538e32bc">
								<AboveValueTriggerModel Id="8c69afd4e0e4b4aa2c8b359126c822c" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="45663b78ba7e4176b5c28bda899a204a" Severity="[AlarmSeverity]Critical" TriggerModel="5898901a0481439ca835944c07ccaa97">
							<ChannelMonitorTriggerModel Alias="[string]35872791-5737-426f-a073-3748bf09ca56" AliasToMonitor="[string]Sink 59" Id="5898901a0481439ca835944c07ccaa97">
								<AboveValueTriggerModel Id="e03f44a5311947a08c73ea4796b56aba" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 60" CanDisable="[bool]True" CriticalAlarm="7b16ed98c56e4f86bcf34aea2fb83f29" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="be7758556fd845a0b073b3e63b6a54b6" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink60" Units="[string]Voltaires" WarningAlarm="2d1c24e237064464b4e061475c3d58e4">
						<AlarmModel Id="2d1c24e237064464b4e061475c3d58e4" Severity="[AlarmSeverity]Warning" TriggerModel="d5c82695c1ce416aa572fdf6771c4bd2">
							<ChannelMonitorTriggerModel Alias="[string]64964ee6-832f-4704-852a-d9179a6f9492" AliasToMonitor="[string]Sink 60" Id="d5c82695c1ce416aa572fdf6771c4bd2">
								<AboveValueTriggerModel Id="6d77dcc4b16b416cb9c028df5938cab4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7b16ed98c56e4f86bcf34aea2fb83f29" Severity="[AlarmSeverity]Critical" TriggerModel="c72c6b89a7bd49d58c4772ea88f7b6ac">
							<ChannelMonitorTriggerModel Alias="[string]58eadad5-be04-44df-a1b2-9e0f20e3b264" AliasToMonitor="[string]Sink 60" Id="c72c6b89a7bd49d58c4772ea88f7b6ac">
								<AboveValueTriggerModel Id="f2ab2c9f0f744b3797244ca3f9229321" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 61" CanDisable="[bool]True" CriticalAlarm="40a0e2009eba4e8bbcef32f686529cda" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="195183d677fd44b78bd29322d6a15026" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink61" Units="[string]Voltaires" WarningAlarm="f9e65ae1e487433f8248af5fe7178ad1">
						<AlarmModel Id="f9e65ae1e487433f8248af5fe7178ad1" Severity="[AlarmSeverity]Warning" TriggerModel="cc099a05f3064ee2a10f6ecf4ba6083a">
							<ChannelMonitorTriggerModel Alias="[string]350bbc92-cdfd-4b6a-97d9-11279bfe99bb" AliasToMonitor="[string]Sink 61" Id="cc099a05f3064ee2a10f6ecf4ba6083a">
								<AboveValueTriggerModel Id="38afc137c46f4279a9dab19f43591997" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="40a0e2009eba4e8bbcef32f686529cda" Severity="[AlarmSeverity]Critical" TriggerModel="8d3b94f2ef754cc6854d850e2ba53cd3">
							<ChannelMonitorTriggerModel Alias="[string]741eef6c-4291-41f9-ad31-fbeef3d3c7e2" AliasToMonitor="[string]Sink 61" Id="8d3b94f2ef754cc6854d850e2ba53cd3">
								<AboveValueTriggerModel Id="ca4b25e4714c412d90d22ae3ee973397" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 62" CanDisable="[bool]True" CriticalAlarm="7c756c7dfba343b18c2a1d443b248eb7" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="af636a5b70454245806bc39d4abba71b" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink62" Units="[string]Voltaires" WarningAlarm="20bd10c01c9a4925b83dbb030a775c53">
						<AlarmModel Id="20bd10c01c9a4925b83dbb030a775c53" Severity="[AlarmSeverity]Warning" TriggerModel="566124e411784b45b1e51020d525e83e">
							<ChannelMonitorTriggerModel Alias="[string]e0aa3fb8-d44a-45a6-9c52-751159bba8ce" AliasToMonitor="[string]Sink 62" Id="566124e411784b45b1e51020d525e83e">
								<AboveValueTriggerModel Id="9fbccb47018f45628d3175c3b6d91b9e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7c756c7dfba343b18c2a1d443b248eb7" Severity="[AlarmSeverity]Critical" TriggerModel="d07c082e84bd45f4ad04f2302b5249b3">
							<ChannelMonitorTriggerModel Alias="[string]d88db1d2-c9b1-4666-8510-43caf7018011" AliasToMonitor="[string]Sink 62" Id="d07c082e84bd45f4ad04f2302b5249b3">
								<AboveValueTriggerModel Id="287ec57e67004a469a300dbf4ece5aa9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 63" CanDisable="[bool]True" CriticalAlarm="1b6482ba7eba45c4aa58d55b2913e786" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="13011faa5294e9191556bf8046791b1" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink63" Units="[string]Voltaires" WarningAlarm="f946d32cc40a4b3597a79de2bfea8f66">
						<AlarmModel Id="f946d32cc40a4b3597a79de2bfea8f66" Severity="[AlarmSeverity]Warning" TriggerModel="ea8f81a0cb2c428eb341748a60f23116">
							<ChannelMonitorTriggerModel Alias="[string]5ce867db-826f-43bd-8d2e-b9e59841e1e3" AliasToMonitor="[string]Sink 63" Id="ea8f81a0cb2c428eb341748a60f23116">
								<AboveValueTriggerModel Id="b0d1f6ea17e04878832caf0412b63e99" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="1b6482ba7eba45c4aa58d55b2913e786" Severity="[AlarmSeverity]Critical" TriggerModel="a528f2dfced14285a7f62971b8702e4d">
							<ChannelMonitorTriggerModel Alias="[string]13fd995a-5947-40a2-b11b-8053e8168bc4" AliasToMonitor="[string]Sink 63" Id="a528f2dfced14285a7f62971b8702e4d">
								<AboveValueTriggerModel Id="3d0ed53bde9f4aa28f40e7854f0c59d6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 64" CanDisable="[bool]True" CriticalAlarm="800e63fd99e84366b79092efd90790e6" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4b877221268f43dbab9369557adf875a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink64" Units="[string]Voltaires" WarningAlarm="b1a5b9acbeae4653a84ca769b5ad6915">
						<AlarmModel Id="b1a5b9acbeae4653a84ca769b5ad6915" Severity="[AlarmSeverity]Warning" TriggerModel="7eda0597b33b4773a8b8f29bfc0d53f1">
							<ChannelMonitorTriggerModel Alias="[string]902c9521-ca3a-4a99-9365-d0b4668810cb" AliasToMonitor="[string]Sink 64" Id="7eda0597b33b4773a8b8f29bfc0d53f1">
								<AboveValueTriggerModel Id="df07091d333448b1832bc3eba8de3b28" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="800e63fd99e84366b79092efd90790e6" Severity="[AlarmSeverity]Critical" TriggerModel="f434959da68f4a6c9c786263972e4011">
							<ChannelMonitorTriggerModel Alias="[string]5f201fdd-cd0f-42b9-994c-b80397f462ea" AliasToMonitor="[string]Sink 64" Id="f434959da68f4a6c9c786263972e4011">
								<AboveValueTriggerModel Id="281f175ca4b84941b84826823b88b8f0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 65" CanDisable="[bool]True" CriticalAlarm="ec74a74593b14ed48832d2fa4253d2a8" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="868e57f4f3284cb99825244d27187ba9" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink65" Units="[string]Voltaires" WarningAlarm="b52fc64ab5894b5a84dd905d41393160">
						<AlarmModel Id="b52fc64ab5894b5a84dd905d41393160" Severity="[AlarmSeverity]Warning" TriggerModel="fa784f6ef38348ae861cb4610410812e">
							<ChannelMonitorTriggerModel Alias="[string]22d12d67-1f67-41c8-ba6b-43097670c3d5" AliasToMonitor="[string]Sink 65" Id="fa784f6ef38348ae861cb4610410812e">
								<AboveValueTriggerModel Id="c520e3c9ef9d4685af5abcf9ab74d024" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="ec74a74593b14ed48832d2fa4253d2a8" Severity="[AlarmSeverity]Critical" TriggerModel="65ae80d33f3b44b2b74ce81ad5fa039a">
							<ChannelMonitorTriggerModel Alias="[string]52615ba6-c800-457e-a7a5-1997b9ab3132" AliasToMonitor="[string]Sink 65" Id="65ae80d33f3b44b2b74ce81ad5fa039a">
								<AboveValueTriggerModel Id="5ab503325eff4ac18ff388f328e1c57d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 66" CanDisable="[bool]True" CriticalAlarm="7c4bf7384ea247d89b16bec5321404c9" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="86edc1b5473940209840bf9ec151b33f" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink66" Units="[string]Voltaires" WarningAlarm="546632a0c45344559a5ac3c4de1d974c">
						<AlarmModel Id="546632a0c45344559a5ac3c4de1d974c" Severity="[AlarmSeverity]Warning" TriggerModel="13f6a60ea94143a28a696caa378f769c">
							<ChannelMonitorTriggerModel Alias="[string]5816e843-810a-45c0-a1db-0710fd8abcda" AliasToMonitor="[string]Sink 66" Id="13f6a60ea94143a28a696caa378f769c">
								<AboveValueTriggerModel Id="a2ed8f0f12b547f596ba7be585aea801" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7c4bf7384ea247d89b16bec5321404c9" Severity="[AlarmSeverity]Critical" TriggerModel="48aff9f2f69a4504ad1d34b17d577d71">
							<ChannelMonitorTriggerModel Alias="[string]1eef3a9d-3421-4069-b4f0-8659724efa9e" AliasToMonitor="[string]Sink 66" Id="48aff9f2f69a4504ad1d34b17d577d71">
								<AboveValueTriggerModel Id="9b29293bb14d447fa92ba545aefbef7f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 67" CanDisable="[bool]True" CriticalAlarm="86092d8b26944768a9b585380b0bdfb" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c8266372ad414aefb1d75cb334cb5c27" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink67" Units="[string]Voltaires" WarningAlarm="d65416b3f8064107b015b9bd2645ad74">
						<AlarmModel Id="d65416b3f8064107b015b9bd2645ad74" Severity="[AlarmSeverity]Warning" TriggerModel="293bfe99b7ab4ca3aea4b9565c0ced45">
							<ChannelMonitorTriggerModel Alias="[string]785db11c-095a-4468-a086-fe7813585dbb" AliasToMonitor="[string]Sink 67" Id="293bfe99b7ab4ca3aea4b9565c0ced45">
								<AboveValueTriggerModel Id="f62076da732c401a88528d4a76c459e1" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="86092d8b26944768a9b585380b0bdfb" Severity="[AlarmSeverity]Critical" TriggerModel="1e7b0bc6aadc414081b414e5d6ae4a81">
							<ChannelMonitorTriggerModel Alias="[string]606953ec-559c-4561-a7bf-a7be54be3afa" AliasToMonitor="[string]Sink 67" Id="1e7b0bc6aadc414081b414e5d6ae4a81">
								<AboveValueTriggerModel Id="605974b056d94d68b65073ef2f976756" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 68" CanDisable="[bool]True" CriticalAlarm="cd04627368ab457cb2e04eb2b54d5e8e" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="73b363d49c1641d3ae89579c36d7be3e" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink68" Units="[string]Voltaires" WarningAlarm="15de37a10e64d8dabca13f715e82cce">
						<AlarmModel Id="15de37a10e64d8dabca13f715e82cce" Severity="[AlarmSeverity]Warning" TriggerModel="42d9d734a04348c2804a84c7344a25fc">
							<ChannelMonitorTriggerModel Alias="[string]9ca8b1e7-1b37-4d4b-8cff-5cc2c7ddda9c" AliasToMonitor="[string]Sink 68" Id="42d9d734a04348c2804a84c7344a25fc">
								<AboveValueTriggerModel Id="97db4ce76fcb49c5986477d45feee2f2" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="cd04627368ab457cb2e04eb2b54d5e8e" Severity="[AlarmSeverity]Critical" TriggerModel="12bb669a0b3a4ce1a89f9b286b1aa6e0">
							<ChannelMonitorTriggerModel Alias="[string]3aff837c-d516-41e3-9556-855772f6b893" AliasToMonitor="[string]Sink 68" Id="12bb669a0b3a4ce1a89f9b286b1aa6e0">
								<AboveValueTriggerModel Id="d9008baa631e4c859211b016fe596e8a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 69" CanDisable="[bool]True" CriticalAlarm="3f2e0801dd3941988bf0ccd93f55db5d" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="43df023c5fdb451393cf9ae4f1c97261" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink69" Units="[string]Voltaires" WarningAlarm="3ae7b21e59ec4c86bf7ed6f48188a729">
						<AlarmModel Id="3ae7b21e59ec4c86bf7ed6f48188a729" Severity="[AlarmSeverity]Warning" TriggerModel="964957cd89014caea4e6ee0ac0e57319">
							<ChannelMonitorTriggerModel Alias="[string]e15bc37a-fb32-47ff-b371-1880b672e29a" AliasToMonitor="[string]Sink 69" Id="964957cd89014caea4e6ee0ac0e57319">
								<AboveValueTriggerModel Id="7df8ab532f5c4c6d889514fca295d7a9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="3f2e0801dd3941988bf0ccd93f55db5d" Severity="[AlarmSeverity]Critical" TriggerModel="824f35f964bb4f5d9cbbb499995c3238">
							<ChannelMonitorTriggerModel Alias="[string]9c77788e-451e-41a4-9ae5-534184111634" AliasToMonitor="[string]Sink 69" Id="824f35f964bb4f5d9cbbb499995c3238">
								<AboveValueTriggerModel Id="76eb3682766a4a8b9c25624aff0bdfcb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 70" CanDisable="[bool]True" CriticalAlarm="3bcb4e75e16341149ec7dd24a98b44c1" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="82efdfd9c74747e2a9c29e1d36610f0d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink70" Units="[string]Voltaires" WarningAlarm="167c904cc15d49138465cfc969cd7b66">
						<AlarmModel Id="167c904cc15d49138465cfc969cd7b66" Severity="[AlarmSeverity]Warning" TriggerModel="adc0c3efd664dd1bb66af700ef5f73f">
							<ChannelMonitorTriggerModel Alias="[string]353d4ab4-5205-4a01-bc6b-1b83a650a6dc" AliasToMonitor="[string]Sink 70" Id="adc0c3efd664dd1bb66af700ef5f73f">
								<AboveValueTriggerModel Id="7ad6237fea6847feafce9733e80215eb" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="3bcb4e75e16341149ec7dd24a98b44c1" Severity="[AlarmSeverity]Critical" TriggerModel="766ad69ace8a4ff8959529239b5c297a">
							<ChannelMonitorTriggerModel Alias="[string]28a7b021-f24b-4f89-ae11-471f5b2b71a1" AliasToMonitor="[string]Sink 70" Id="766ad69ace8a4ff8959529239b5c297a">
								<AboveValueTriggerModel Id="db5614e4d0d9459d8c26ad4edfcdaa2a" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 71" CanDisable="[bool]True" CriticalAlarm="bfa70e2f6a943b195735c60f5f3d2b9" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="764fae70a7164d398abcf08e711605ed" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink71" Units="[string]Voltaires" WarningAlarm="e5bee7d4c8da49bb8731fb0b77007154">
						<AlarmModel Id="e5bee7d4c8da49bb8731fb0b77007154" Severity="[AlarmSeverity]Warning" TriggerModel="9abdb2a3aeb149fa9d094e4d780de6ac">
							<ChannelMonitorTriggerModel Alias="[string]2a403b85-5a5c-4cc9-820a-bbbf44531292" AliasToMonitor="[string]Sink 71" Id="9abdb2a3aeb149fa9d094e4d780de6ac">
								<AboveValueTriggerModel Id="32d265181d674da08c77ad3eea3945b1" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="bfa70e2f6a943b195735c60f5f3d2b9" Severity="[AlarmSeverity]Critical" TriggerModel="46395cff4b4d45728a7ecbf8939fe321">
							<ChannelMonitorTriggerModel Alias="[string]ee5fb36d-2dca-4761-adea-ce9e6d2b0f40" AliasToMonitor="[string]Sink 71" Id="46395cff4b4d45728a7ecbf8939fe321">
								<AboveValueTriggerModel Id="2646a445226146cea6323cb38285acd4" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 72" CanDisable="[bool]True" CriticalAlarm="276c8cbf02664be1a844d06b70262fab" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="1d7a4329d26141938efc3476f6f7461a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink72" Units="[string]Voltaires" WarningAlarm="abc75ba660cb467bac2e369e818d5a7d">
						<AlarmModel Id="abc75ba660cb467bac2e369e818d5a7d" Severity="[AlarmSeverity]Warning" TriggerModel="84d07a1ec61c47089c3de09427937755">
							<ChannelMonitorTriggerModel Alias="[string]3d568b27-cbca-42ff-a05b-02fd631a078c" AliasToMonitor="[string]Sink 72" Id="84d07a1ec61c47089c3de09427937755">
								<AboveValueTriggerModel Id="cf0078b27ffa4d08a1edd740fc8b12f6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="276c8cbf02664be1a844d06b70262fab" Severity="[AlarmSeverity]Critical" TriggerModel="6c578444cfa044c9a04affe836400fc4">
							<ChannelMonitorTriggerModel Alias="[string]e270796d-de58-4d60-93d2-d8c69b72c094" AliasToMonitor="[string]Sink 72" Id="6c578444cfa044c9a04affe836400fc4">
								<AboveValueTriggerModel Id="2a751eba2a7b4dbbbd8faec895eca4a8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 73" CanDisable="[bool]True" CriticalAlarm="13ed95c4b54e4311a0bb4e271143c38f" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="a801cdbe3314298963b431d4be97d2a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink73" Units="[string]Voltaires" WarningAlarm="8120bf37264453bab0279deec6f3c51">
						<AlarmModel Id="8120bf37264453bab0279deec6f3c51" Severity="[AlarmSeverity]Warning" TriggerModel="7443418f782b4769856e2ff71271b650">
							<ChannelMonitorTriggerModel Alias="[string]5f32a343-3de0-40cb-a5fe-e8f4c6d6e888" AliasToMonitor="[string]Sink 73" Id="7443418f782b4769856e2ff71271b650">
								<AboveValueTriggerModel Id="6cb0c85912b64eacab9dc6e395be6ca5" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="13ed95c4b54e4311a0bb4e271143c38f" Severity="[AlarmSeverity]Critical" TriggerModel="d94effed7c064ec0b00b8f5d4b8e4994">
							<ChannelMonitorTriggerModel Alias="[string]88540e0a-c45e-41eb-8b87-181854b65901" AliasToMonitor="[string]Sink 73" Id="d94effed7c064ec0b00b8f5d4b8e4994">
								<AboveValueTriggerModel Id="3a8f9e2dd1cf40faba5e3f0d639302d3" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 74" CanDisable="[bool]True" CriticalAlarm="ebe703e5225d48288f03afd87b3af763" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="e5b0723049ea40989e2aad804628436a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink74" Units="[string]Voltaires" WarningAlarm="f6e7f5feeed24c5688127c2e6df184f7">
						<AlarmModel Id="f6e7f5feeed24c5688127c2e6df184f7" Severity="[AlarmSeverity]Warning" TriggerModel="952e1942385e42978fdbe77a88f12422">
							<ChannelMonitorTriggerModel Alias="[string]78f76683-08a7-4bdb-9362-8633439e8aec" AliasToMonitor="[string]Sink 74" Id="952e1942385e42978fdbe77a88f12422">
								<AboveValueTriggerModel Id="463b64fcac144e1080ce4602148a6b26" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="ebe703e5225d48288f03afd87b3af763" Severity="[AlarmSeverity]Critical" TriggerModel="b43ea4cbea6f4528a6607bb76f2133b5">
							<ChannelMonitorTriggerModel Alias="[string]932c6440-4d30-4e29-84e1-49a632dcf97f" AliasToMonitor="[string]Sink 74" Id="b43ea4cbea6f4528a6607bb76f2133b5">
								<AboveValueTriggerModel Id="8b7f6cd11ed34f3f8a4a43ee39fff055" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 75" CanDisable="[bool]True" CriticalAlarm="8e7ffea053214200b82ab1c3b9664593" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="81581a253984c27a2e529470475c1b9" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink75" Units="[string]Voltaires" WarningAlarm="585b8a5226df404d8c3aa76d398f191e">
						<AlarmModel Id="585b8a5226df404d8c3aa76d398f191e" Severity="[AlarmSeverity]Warning" TriggerModel="ad95e060222a4f2faee201e259239798">
							<ChannelMonitorTriggerModel Alias="[string]5c515f48-eb07-4f15-a71b-81e2a4bf7159" AliasToMonitor="[string]Sink 75" Id="ad95e060222a4f2faee201e259239798">
								<AboveValueTriggerModel Id="cc610bf5cf224f0b856893108c7205b5" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="8e7ffea053214200b82ab1c3b9664593" Severity="[AlarmSeverity]Critical" TriggerModel="1f0fc78a3c4a48afb41c64f0077653a1">
							<ChannelMonitorTriggerModel Alias="[string]4338497a-0302-4533-9990-3dd1719330ae" AliasToMonitor="[string]Sink 75" Id="1f0fc78a3c4a48afb41c64f0077653a1">
								<AboveValueTriggerModel Id="b9f28dbb83fb446bb9ee1db94bebba18" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 76" CanDisable="[bool]True" CriticalAlarm="2cb8a2b7b0e34880b3ca7f19c602f1eb" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="57771db9e4a14aedad021152baf081ff" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink76" Units="[string]Voltaires" WarningAlarm="1b768cc9ccc14affb335cd13273f49f2">
						<AlarmModel Id="1b768cc9ccc14affb335cd13273f49f2" Severity="[AlarmSeverity]Warning" TriggerModel="ed28bd8d8dc54e7c900f7fdb797ffc5b">
							<ChannelMonitorTriggerModel Alias="[string]527b8d4e-e4ba-497b-8c13-727561ef5622" AliasToMonitor="[string]Sink 76" Id="ed28bd8d8dc54e7c900f7fdb797ffc5b">
								<AboveValueTriggerModel Id="a37a1c4b8a4c47529998c1de593cf983" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="2cb8a2b7b0e34880b3ca7f19c602f1eb" Severity="[AlarmSeverity]Critical" TriggerModel="eb48f094db7841c08e2f17e8b1435930">
							<ChannelMonitorTriggerModel Alias="[string]ef0150f0-f246-47af-986a-708f37eed06c" AliasToMonitor="[string]Sink 76" Id="eb48f094db7841c08e2f17e8b1435930">
								<AboveValueTriggerModel Id="ae4ddcaf272e40dfa87e69ba870ad5b2" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 77" CanDisable="[bool]True" CriticalAlarm="57a989927dc94c50ba208a18931c1100" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="fb146099d65c45f4a791f20597aac0f4" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink77" Units="[string]Voltaires" WarningAlarm="9b5029c8b1f847a38f6be873fd480786">
						<AlarmModel Id="9b5029c8b1f847a38f6be873fd480786" Severity="[AlarmSeverity]Warning" TriggerModel="1d81232bdf04499d982f6a3c1470106c">
							<ChannelMonitorTriggerModel Alias="[string]aff9241d-457a-4653-b3db-f2cef544b470" AliasToMonitor="[string]Sink 77" Id="1d81232bdf04499d982f6a3c1470106c">
								<AboveValueTriggerModel Id="880483f231b344d1a98cd4bb172dc8ed" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="57a989927dc94c50ba208a18931c1100" Severity="[AlarmSeverity]Critical" TriggerModel="5aa81a9168bc43a784955b92bba92e3a">
							<ChannelMonitorTriggerModel Alias="[string]323b93de-a1bb-4412-b894-e6d3184dfa7c" AliasToMonitor="[string]Sink 77" Id="5aa81a9168bc43a784955b92bba92e3a">
								<AboveValueTriggerModel Id="af9e6f272a7e44ec92e85ffc515b6a3b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 78" CanDisable="[bool]True" CriticalAlarm="470ae524ca3c4692ae72c1a3a8614af0" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="7302406ee9b4319bec09e5e33f5a5b3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink78" Units="[string]Voltaires" WarningAlarm="d14d3da7652f4555b3fb7e5da5adf166">
						<AlarmModel Id="d14d3da7652f4555b3fb7e5da5adf166" Severity="[AlarmSeverity]Warning" TriggerModel="ea878264e01a4b58aed59e5c50733faa">
							<ChannelMonitorTriggerModel Alias="[string]5c69c44c-08bc-4ef8-b0ed-f11807f830aa" AliasToMonitor="[string]Sink 78" Id="ea878264e01a4b58aed59e5c50733faa">
								<AboveValueTriggerModel Id="39ec0189106c42908b489f677659cc4b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="470ae524ca3c4692ae72c1a3a8614af0" Severity="[AlarmSeverity]Critical" TriggerModel="ec37e3d4ccaf47b19e81b79d18f68aa0">
							<ChannelMonitorTriggerModel Alias="[string]614db51b-1c5d-435d-aa0e-a3a401535488" AliasToMonitor="[string]Sink 78" Id="ec37e3d4ccaf47b19e81b79d18f68aa0">
								<AboveValueTriggerModel Id="91c0aecbae71473b98c6a018cd8d3c64" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 79" CanDisable="[bool]True" CriticalAlarm="1066450537dd4102b737f318511e992b" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="4e87956cb97649098a79a7526a2e69cf" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink79" Units="[string]Voltaires" WarningAlarm="e69d20db4bb74268a0e5fc720bd6d57a">
						<AlarmModel Id="e69d20db4bb74268a0e5fc720bd6d57a" Severity="[AlarmSeverity]Warning" TriggerModel="d7fe987365eb465d91c8ea229a9b95b8">
							<ChannelMonitorTriggerModel Alias="[string]f54e6c68-c406-4d33-8b7d-6e464d46b66a" AliasToMonitor="[string]Sink 79" Id="d7fe987365eb465d91c8ea229a9b95b8">
								<AboveValueTriggerModel Id="3a523fe6e3cd44cd9df9c073c219182e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="1066450537dd4102b737f318511e992b" Severity="[AlarmSeverity]Critical" TriggerModel="3be0804bbb434d27a1eead0e4b40316d">
							<ChannelMonitorTriggerModel Alias="[string]710ab22f-a2c0-49b2-9d05-2d4967661d30" AliasToMonitor="[string]Sink 79" Id="3be0804bbb434d27a1eead0e4b40316d">
								<AboveValueTriggerModel Id="4d6d785891ac454c86651fd4d92de036" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 80" CanDisable="[bool]True" CriticalAlarm="f54a3fb55c4d45d589d0b22e9e05a168" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="a8943e058e09451aa3bd5a2f40493686" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink80" Units="[string]Voltaires" WarningAlarm="9b04cf6686d744dc9996ed9a22b7d10c">
						<AlarmModel Id="9b04cf6686d744dc9996ed9a22b7d10c" Severity="[AlarmSeverity]Warning" TriggerModel="d03ee6d3535d42568384b80a6bd19536">
							<ChannelMonitorTriggerModel Alias="[string]a2310496-990e-4c1b-bae8-d719e8bac859" AliasToMonitor="[string]Sink 80" Id="d03ee6d3535d42568384b80a6bd19536">
								<AboveValueTriggerModel Id="a74ca34f95c4d0aad51a51f6f547290" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="f54a3fb55c4d45d589d0b22e9e05a168" Severity="[AlarmSeverity]Critical" TriggerModel="7164ddf32691458facfa4145f8c93651">
							<ChannelMonitorTriggerModel Alias="[string]f48eea4e-93e4-4852-ac8c-8a58dcedf547" AliasToMonitor="[string]Sink 80" Id="7164ddf32691458facfa4145f8c93651">
								<AboveValueTriggerModel Id="6f9d971c6e3f4d869deaccadcd69ac48" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 81" CanDisable="[bool]True" CriticalAlarm="83f03cd88d594567b25cf697c6a1b825" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="1e6d105ff4f94e31aa7640db27b9f41a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink81" Units="[string]Voltaires" WarningAlarm="25e94c2bac3341f2bca67e6fbf402dac">
						<AlarmModel Id="25e94c2bac3341f2bca67e6fbf402dac" Severity="[AlarmSeverity]Warning" TriggerModel="4e82e883b7b2426a9e54777a3aff933a">
							<ChannelMonitorTriggerModel Alias="[string]aaa709b6-e6c6-4a3a-9451-0c6d948be471" AliasToMonitor="[string]Sink 81" Id="4e82e883b7b2426a9e54777a3aff933a">
								<AboveValueTriggerModel Id="2a1b8c218f1a4670bdfef8db804c9728" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="83f03cd88d594567b25cf697c6a1b825" Severity="[AlarmSeverity]Critical" TriggerModel="ac50eb1552994d4ebe59e1815610601f">
							<ChannelMonitorTriggerModel Alias="[string]638c066a-aed3-4ba4-96ae-d0b9221a4da2" AliasToMonitor="[string]Sink 81" Id="ac50eb1552994d4ebe59e1815610601f">
								<AboveValueTriggerModel Id="4ba8ac1b00a044ee88274d719efb19ed" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 82" CanDisable="[bool]True" CriticalAlarm="5f462a84985a44df8091da2cd4760b98" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c279d6ce7d6245738a8e4b9a983edaec" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink82" Units="[string]Voltaires" WarningAlarm="76f385311a6b409b91a2dfda126cc942">
						<AlarmModel Id="76f385311a6b409b91a2dfda126cc942" Severity="[AlarmSeverity]Warning" TriggerModel="e9128719dde5487f8b2c54463eddc5f3">
							<ChannelMonitorTriggerModel Alias="[string]3c9d234c-9072-4578-955e-81397d852a01" AliasToMonitor="[string]Sink 82" Id="e9128719dde5487f8b2c54463eddc5f3">
								<AboveValueTriggerModel Id="da4ae23cbcdc4c37bcdad1733556aa4f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="5f462a84985a44df8091da2cd4760b98" Severity="[AlarmSeverity]Critical" TriggerModel="586c9501cbb64266b85ab6565940a315">
							<ChannelMonitorTriggerModel Alias="[string]84e64acc-5896-478a-b57d-3074005d49f8" AliasToMonitor="[string]Sink 82" Id="586c9501cbb64266b85ab6565940a315">
								<AboveValueTriggerModel Id="469b053e5a74442e826e73f3592ba00d" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 83" CanDisable="[bool]True" CriticalAlarm="112ad13aab754c34b162ff659e8c9ca9" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2e1621b9d3e842d29ffdf0a82900e55b" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink83" Units="[string]Voltaires" WarningAlarm="d1212ccfe6c341968bec3243a7a3f19d">
						<AlarmModel Id="d1212ccfe6c341968bec3243a7a3f19d" Severity="[AlarmSeverity]Warning" TriggerModel="d965519b246f4402b3a6752d43041aac">
							<ChannelMonitorTriggerModel Alias="[string]9812bb2c-5ae4-483b-ba17-d9acc0e24351" AliasToMonitor="[string]Sink 83" Id="d965519b246f4402b3a6752d43041aac">
								<AboveValueTriggerModel Id="6f1b315a0de94b47b20f4cd541ea80de" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="112ad13aab754c34b162ff659e8c9ca9" Severity="[AlarmSeverity]Critical" TriggerModel="e38097a4d34847328191480140d54273">
							<ChannelMonitorTriggerModel Alias="[string]dfffd126-e889-4cc3-ab9b-8d7204d5e992" AliasToMonitor="[string]Sink 83" Id="e38097a4d34847328191480140d54273">
								<AboveValueTriggerModel Id="7eacda14901f46aab87b38a984e15be6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 84" CanDisable="[bool]True" CriticalAlarm="7ee0c027f64e40faa161c6016ff1644c" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="57482bb21169422ba7a9cddb8ddae2d6" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink84" Units="[string]Voltaires" WarningAlarm="a3e5499f7ecf42bfb5066caf5fda66da">
						<AlarmModel Id="a3e5499f7ecf42bfb5066caf5fda66da" Severity="[AlarmSeverity]Warning" TriggerModel="44c01e4a8ce432ea51af22cb23c8de6">
							<ChannelMonitorTriggerModel Alias="[string]7eeaefd4-1f27-4b5d-aa67-e58196dc891c" AliasToMonitor="[string]Sink 84" Id="44c01e4a8ce432ea51af22cb23c8de6">
								<AboveValueTriggerModel Id="2e2ed556b1c049538b0075bb409e367e" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="7ee0c027f64e40faa161c6016ff1644c" Severity="[AlarmSeverity]Critical" TriggerModel="e470b520ce554afba9f53ed5c666e480">
							<ChannelMonitorTriggerModel Alias="[string]9583e50b-25c0-45c2-bfc7-b813f54ce27e" AliasToMonitor="[string]Sink 84" Id="e470b520ce554afba9f53ed5c666e480">
								<AboveValueTriggerModel Id="8a79261e234944b6925d68289d22d374" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 85" CanDisable="[bool]True" CriticalAlarm="951ca212c3fb40b2ace15b37b67e3051" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="bacd6cc33d0c45d6a2803c6765d2ea0d" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink85" Units="[string]Voltaires" WarningAlarm="34022875c8b54fc3b211d11f51310fba">
						<AlarmModel Id="34022875c8b54fc3b211d11f51310fba" Severity="[AlarmSeverity]Warning" TriggerModel="ea5dde1a64f84ebbadfc026047bbb7b2">
							<ChannelMonitorTriggerModel Alias="[string]60c811b5-2919-498f-8f81-1cb8997c56f7" AliasToMonitor="[string]Sink 85" Id="ea5dde1a64f84ebbadfc026047bbb7b2">
								<AboveValueTriggerModel Id="ea32f09c17da4a4d9284878dc59e147b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="951ca212c3fb40b2ace15b37b67e3051" Severity="[AlarmSeverity]Critical" TriggerModel="9156477d4ada48e19282f323a7dd4496">
							<ChannelMonitorTriggerModel Alias="[string]b6d2d9b5-2853-4d2c-b5b2-410d0adebd57" AliasToMonitor="[string]Sink 85" Id="9156477d4ada48e19282f323a7dd4496">
								<AboveValueTriggerModel Id="30c473be1e0644dfb39ae18ae757b5d1" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 86" CanDisable="[bool]True" CriticalAlarm="4a2fb49721314b3596e7f04d5c45ba11" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2b3e28980d0b4327afb246b0b6e728da" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink86" Units="[string]Voltaires" WarningAlarm="b4da1373b78b43e4a6810bbc29f589e3">
						<AlarmModel Id="b4da1373b78b43e4a6810bbc29f589e3" Severity="[AlarmSeverity]Warning" TriggerModel="831a75f2ee944f239a20c64aa0a4c829">
							<ChannelMonitorTriggerModel Alias="[string]9ad5154f-b185-48ba-b7f6-8c64da46e112" AliasToMonitor="[string]Sink 86" Id="831a75f2ee944f239a20c64aa0a4c829">
								<AboveValueTriggerModel Id="2427d6c2ddfc4df1900f42b6b26e4518" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="4a2fb49721314b3596e7f04d5c45ba11" Severity="[AlarmSeverity]Critical" TriggerModel="7ddf33d94d514ba88945c3a4a31cc6a8">
							<ChannelMonitorTriggerModel Alias="[string]264c6a1e-8a30-4f38-b247-4cb98f611347" AliasToMonitor="[string]Sink 86" Id="7ddf33d94d514ba88945c3a4a31cc6a8">
								<AboveValueTriggerModel Id="ad74da258fa4c648c68de8d4966e81b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 87" CanDisable="[bool]True" CriticalAlarm="483f2f6a6564373911671c62e7c24b1" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6da9f063ac44464c97d7d737a020686a" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink87" Units="[string]Voltaires" WarningAlarm="1ec5cf9e56c14dec82760d91d3f994d3">
						<AlarmModel Id="1ec5cf9e56c14dec82760d91d3f994d3" Severity="[AlarmSeverity]Warning" TriggerModel="8fd99145496d42c7a331684ddaba1998">
							<ChannelMonitorTriggerModel Alias="[string]d22964fc-857b-4d84-8c87-e534a21a3573" AliasToMonitor="[string]Sink 87" Id="8fd99145496d42c7a331684ddaba1998">
								<AboveValueTriggerModel Id="de95af06988747be976221555f58dc67" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="483f2f6a6564373911671c62e7c24b1" Severity="[AlarmSeverity]Critical" TriggerModel="271e8bfeac0543f6a196182f34ecfa3c">
							<ChannelMonitorTriggerModel Alias="[string]b008af94-1e16-4340-ae16-bc76d41ef4b3" AliasToMonitor="[string]Sink 87" Id="271e8bfeac0543f6a196182f34ecfa3c">
								<AboveValueTriggerModel Id="cc93e7de608646799757593ea5947de8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 88" CanDisable="[bool]True" CriticalAlarm="a8347a612fe5437b8227426b53213e21" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="39a74165c3da40f1af45ab1e0b5ec0e3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink88" Units="[string]Voltaires" WarningAlarm="b8d2e6c7704f45da808ef3fa07655cbf">
						<AlarmModel Id="b8d2e6c7704f45da808ef3fa07655cbf" Severity="[AlarmSeverity]Warning" TriggerModel="bc595fe0357743b587380a188d0c1222">
							<ChannelMonitorTriggerModel Alias="[string]8ff5ba47-7ed9-4606-9044-ab3d76a7fafe" AliasToMonitor="[string]Sink 88" Id="bc595fe0357743b587380a188d0c1222">
								<AboveValueTriggerModel Id="218f4f50150048e682c102380b187169" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="a8347a612fe5437b8227426b53213e21" Severity="[AlarmSeverity]Critical" TriggerModel="f7651b042bd3425f9de977f4b353e41b">
							<ChannelMonitorTriggerModel Alias="[string]35a114d4-b5d0-44ea-a62b-51df4143a533" AliasToMonitor="[string]Sink 88" Id="f7651b042bd3425f9de977f4b353e41b">
								<AboveValueTriggerModel Id="bbb107b2603549e4bac02481c077a2b6" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 89" CanDisable="[bool]True" CriticalAlarm="393cacd6b34b4b609290002b56295536" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2f93dbf6cfe24f279d647012497494a9" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink89" Units="[string]Voltaires" WarningAlarm="8499d3b461174312a5e16a10755654c0">
						<AlarmModel Id="8499d3b461174312a5e16a10755654c0" Severity="[AlarmSeverity]Warning" TriggerModel="e6724c8e01be47638072551dad98eb86">
							<ChannelMonitorTriggerModel Alias="[string]0f2c451d-2426-4440-b6aa-f075313000c7" AliasToMonitor="[string]Sink 89" Id="e6724c8e01be47638072551dad98eb86">
								<AboveValueTriggerModel Id="dfb0a34469fa431d82ce941a7fc3789f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="393cacd6b34b4b609290002b56295536" Severity="[AlarmSeverity]Critical" TriggerModel="13e6f4a16f1a4841ad4d1a11779a3193">
							<ChannelMonitorTriggerModel Alias="[string]6a0b5ce1-c002-4be5-b6c8-246403be6824" AliasToMonitor="[string]Sink 89" Id="13e6f4a16f1a4841ad4d1a11779a3193">
								<AboveValueTriggerModel Id="fa5a082a17194837a6393b229b893f90" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 90" CanDisable="[bool]True" CriticalAlarm="9c377d9fd8f840b3b0d0fdf99ccfcbe8" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="3f84f14e924d407fbe61c7ffcf4e8cab" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink90" Units="[string]Voltaires" WarningAlarm="b46c5d0bd28440378007bc95f351a27c">
						<AlarmModel Id="b46c5d0bd28440378007bc95f351a27c" Severity="[AlarmSeverity]Warning" TriggerModel="fd57278fa82b4862804e625670895250">
							<ChannelMonitorTriggerModel Alias="[string]b14e7fec-9c53-4e92-b165-ef6d37d15250" AliasToMonitor="[string]Sink 90" Id="fd57278fa82b4862804e625670895250">
								<AboveValueTriggerModel Id="6937d8f4a4684acabac4ae8d5bcc40c0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="9c377d9fd8f840b3b0d0fdf99ccfcbe8" Severity="[AlarmSeverity]Critical" TriggerModel="97219ce6e62b47b5815cac841cb12b36">
							<ChannelMonitorTriggerModel Alias="[string]b2c6d59c-6b71-49af-85d4-6283106cfc62" AliasToMonitor="[string]Sink 90" Id="97219ce6e62b47b5815cac841cb12b36">
								<AboveValueTriggerModel Id="c1cecc2c43c24c8a8d13b6e352ea8102" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 91" CanDisable="[bool]True" CriticalAlarm="f1a2df96648848ae8217ffe09deacb6e" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6b181b9096da41ecbfcdeadad639b5e3" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink91" Units="[string]Voltaires" WarningAlarm="c2b3a8c2060642aca09233cc1e8d1b0d">
						<AlarmModel Id="c2b3a8c2060642aca09233cc1e8d1b0d" Severity="[AlarmSeverity]Warning" TriggerModel="d2878c30ad0e4a2d9662c23204fea34a">
							<ChannelMonitorTriggerModel Alias="[string]fa8f1e7d-a038-42ae-8f02-065e4aef7856" AliasToMonitor="[string]Sink 91" Id="d2878c30ad0e4a2d9662c23204fea34a">
								<AboveValueTriggerModel Id="ff4721efe46644478284a6e3fdb64a72" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="f1a2df96648848ae8217ffe09deacb6e" Severity="[AlarmSeverity]Critical" TriggerModel="8606981ebb6143f2a2b612f155384e65">
							<ChannelMonitorTriggerModel Alias="[string]c8198776-e926-4a06-a4e6-3258ef873e37" AliasToMonitor="[string]Sink 91" Id="8606981ebb6143f2a2b612f155384e65">
								<AboveValueTriggerModel Id="c7e68c0485ef4cc290cf0a63286282a9" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 92" CanDisable="[bool]True" CriticalAlarm="607edf5453fa42a9a627ed24c13a60e5" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2b39cc5ef86540e99a84a1391f6ab753" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink92" Units="[string]Voltaires" WarningAlarm="a20392510f344ffea3a14e6bcbe312cb">
						<AlarmModel Id="a20392510f344ffea3a14e6bcbe312cb" Severity="[AlarmSeverity]Warning" TriggerModel="deaf914d7f6e4f33af84e3a369109191">
							<ChannelMonitorTriggerModel Alias="[string]3dbd9476-d2af-435b-a693-a5fcf704942a" AliasToMonitor="[string]Sink 92" Id="deaf914d7f6e4f33af84e3a369109191">
								<AboveValueTriggerModel Id="d9dc6df9d4cd4fadb26d654624413a12" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="607edf5453fa42a9a627ed24c13a60e5" Severity="[AlarmSeverity]Critical" TriggerModel="926552391a12454eb590ed6319e27f81">
							<ChannelMonitorTriggerModel Alias="[string]6ae96e55-4aab-4de2-96d9-e1076dbe1052" AliasToMonitor="[string]Sink 92" Id="926552391a12454eb590ed6319e27f81">
								<AboveValueTriggerModel Id="fe5847eebd054c0aa0c56f4d4f0ff6ef" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 93" CanDisable="[bool]True" CriticalAlarm="fd7286cd26f34ec6a31d0e01e3a1a74f" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c2b4d93ca88f4de0b2ae661d4d989f40" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink93" Units="[string]Voltaires" WarningAlarm="e482c651fd15427e927027c4d0604957">
						<AlarmModel Id="e482c651fd15427e927027c4d0604957" Severity="[AlarmSeverity]Warning" TriggerModel="3a1414832d1a4d8c8c1af4572201f067">
							<ChannelMonitorTriggerModel Alias="[string]0ffb90e8-d54e-4d0d-a18e-3622a2e87fc9" AliasToMonitor="[string]Sink 93" Id="3a1414832d1a4d8c8c1af4572201f067">
								<AboveValueTriggerModel Id="55de20f5817a4a5c936a1ff31eab4a86" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="fd7286cd26f34ec6a31d0e01e3a1a74f" Severity="[AlarmSeverity]Critical" TriggerModel="ada50b01444485b444831766104afb">
							<ChannelMonitorTriggerModel Alias="[string]850e2892-9a5f-4f0d-af00-b8f502372238" AliasToMonitor="[string]Sink 93" Id="ada50b01444485b444831766104afb">
								<AboveValueTriggerModel Id="51abeab0edc2438bbc79935454810937" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 94" CanDisable="[bool]True" CriticalAlarm="e0fd0f31df3441eaba9b9f07244b0dd3" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2691dd322fe047b99bdc4d023ca71f22" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink94" Units="[string]Voltaires" WarningAlarm="7a913ecbb3ae4bdc8bdba3d286d63433">
						<AlarmModel Id="7a913ecbb3ae4bdc8bdba3d286d63433" Severity="[AlarmSeverity]Warning" TriggerModel="31dafdf19514c279d57f2e16ba0975e">
							<ChannelMonitorTriggerModel Alias="[string]a03d55eb-923d-41c6-8f91-574398c9f69b" AliasToMonitor="[string]Sink 94" Id="31dafdf19514c279d57f2e16ba0975e">
								<AboveValueTriggerModel Id="26cd485bf8f043bcbca631d86520f77b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="e0fd0f31df3441eaba9b9f07244b0dd3" Severity="[AlarmSeverity]Critical" TriggerModel="5810e5f25ba1421eb1ccdaa2175e7035">
							<ChannelMonitorTriggerModel Alias="[string]9d05e837-418f-4eb5-ba2f-1b29b86769bc" AliasToMonitor="[string]Sink 94" Id="5810e5f25ba1421eb1ccdaa2175e7035">
								<AboveValueTriggerModel Id="62c26ca16c8445dfb1f8797d7a09e8cc" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 95" CanDisable="[bool]True" CriticalAlarm="6c5342450ede49a0a8e62b034f1a80e5" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="2a4a8e130115461893dca49a28373e54" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink95" Units="[string]Voltaires" WarningAlarm="1ad9b771574145bc820d30e7dab76d22">
						<AlarmModel Id="1ad9b771574145bc820d30e7dab76d22" Severity="[AlarmSeverity]Warning" TriggerModel="efb2fb5e9b054f7aa25afdcc25894673">
							<ChannelMonitorTriggerModel Alias="[string]a20964c0-8bc9-4b56-adc9-863c6efd1851" AliasToMonitor="[string]Sink 95" Id="efb2fb5e9b054f7aa25afdcc25894673">
								<AboveValueTriggerModel Id="de0030680ed147f9bf93d7561024af08" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="6c5342450ede49a0a8e62b034f1a80e5" Severity="[AlarmSeverity]Critical" TriggerModel="13a3c65a2a14af7b61001181e2ce367">
							<ChannelMonitorTriggerModel Alias="[string]b1aab031-ab67-41df-950f-0cf0183b22d5" AliasToMonitor="[string]Sink 95" Id="13a3c65a2a14af7b61001181e2ce367">
								<AboveValueTriggerModel Id="d02b17b8126f491d89b4bd8e69755c1b" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 96" CanDisable="[bool]True" CriticalAlarm="98daa9915e2a4087988c46f1aaee1568" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="eeea2c2f3df84190b6f4f7f01b9b36eb" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink96" Units="[string]Voltaires" WarningAlarm="3bf811350996431db25f981efb32bcb7">
						<AlarmModel Id="3bf811350996431db25f981efb32bcb7" Severity="[AlarmSeverity]Warning" TriggerModel="f52e56dfbffc4aeb9f14ddbd7f3aa078">
							<ChannelMonitorTriggerModel Alias="[string]170f014b-d206-4073-9a90-89977ef5ca8d" AliasToMonitor="[string]Sink 96" Id="f52e56dfbffc4aeb9f14ddbd7f3aa078">
								<AboveValueTriggerModel Id="c5a0f9cd0f7e47dd9291688088467a7f" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="98daa9915e2a4087988c46f1aaee1568" Severity="[AlarmSeverity]Critical" TriggerModel="aeb891d617004260bf3472e93ac8166b">
							<ChannelMonitorTriggerModel Alias="[string]502c8ac8-bced-417a-a333-bb72cd75c370" AliasToMonitor="[string]Sink 96" Id="aeb891d617004260bf3472e93ac8166b">
								<AboveValueTriggerModel Id="bf770f6ea67e4f978f85dc3998f2fd25" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 97" CanDisable="[bool]True" CriticalAlarm="9bfe5a72da1b44f397d1fb897bfc2005" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="f4ad7b06c37c45bcabd5a6af672db8fe" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink97" Units="[string]Voltaires" WarningAlarm="11cc5a0f0d5d407b902e35d73b8ae0d8">
						<AlarmModel Id="11cc5a0f0d5d407b902e35d73b8ae0d8" Severity="[AlarmSeverity]Warning" TriggerModel="edd82f7521ad4821a839fde75e771e50">
							<ChannelMonitorTriggerModel Alias="[string]eeddcb8f-cf68-497d-9092-c41caa929473" AliasToMonitor="[string]Sink 97" Id="edd82f7521ad4821a839fde75e771e50">
								<AboveValueTriggerModel Id="496da96010f4437bab0df4b273f665d8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="9bfe5a72da1b44f397d1fb897bfc2005" Severity="[AlarmSeverity]Critical" TriggerModel="475a772f4aed4c48a7b47c6ff863785c">
							<ChannelMonitorTriggerModel Alias="[string]407ce6ad-90ce-435a-8b36-8a12d2101e6c" AliasToMonitor="[string]Sink 97" Id="475a772f4aed4c48a7b47c6ff863785c">
								<AboveValueTriggerModel Id="d2ef95ae9b004a80adc8ba6288f1e100" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 98" CanDisable="[bool]True" CriticalAlarm="afe800bcfa7c4efa94edf63fe1d85110" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="c6734127e5f04ab38dcc2bfb58ea8aa8" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink98" Units="[string]Voltaires" WarningAlarm="a82e653f10a144ed82f055fae9c63f02">
						<AlarmModel Id="a82e653f10a144ed82f055fae9c63f02" Severity="[AlarmSeverity]Warning" TriggerModel="2d507d78c8ad4c3d967478ca29688ce7">
							<ChannelMonitorTriggerModel Alias="[string]74eb6750-a7d7-4ef1-9e44-a018fc894607" AliasToMonitor="[string]Sink 98" Id="2d507d78c8ad4c3d967478ca29688ce7">
								<AboveValueTriggerModel Id="d3d21a4829844a28ace03d31e7256984" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="afe800bcfa7c4efa94edf63fe1d85110" Severity="[AlarmSeverity]Critical" TriggerModel="5627e4aabfe4272a8b8bed75deef7e8">
							<ChannelMonitorTriggerModel Alias="[string]41243852-aa5c-449a-b287-cfa907f9a1fc" AliasToMonitor="[string]Sink 98" Id="5627e4aabfe4272a8b8bed75deef7e8">
								<AboveValueTriggerModel Id="465de77624a14ca88b90f9730facadc8" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
					<PeAddonOutputInfo Alias="Sink 99" CanDisable="[bool]True" CriticalAlarm="2c0e7064d74b4a3f87a37ce8520ac513" DataType="[Type]Wfm(Double)" GroupName="[string]" Id="6a51108f72a144e9ba0d9943f3ab7a42" InheritsTiming="[bool]False" SampleRate="[double]10" Source="sink99" Units="[string]Voltaires" WarningAlarm="6cecc2b95cae4e108e26d79e64faf27d">
						<AlarmModel Id="6cecc2b95cae4e108e26d79e64faf27d" Severity="[AlarmSeverity]Warning" TriggerModel="9aaa22f513c343b8bb700753ecabd83f">
							<ChannelMonitorTriggerModel Alias="[string]1b5c88fd-e137-4994-b590-fcffdb67bc98" AliasToMonitor="[string]Sink 99" Id="9aaa22f513c343b8bb700753ecabd83f">
								<AboveValueTriggerModel Id="1b48131969024f788f3ea921200554b0" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
						<AlarmModel Id="2c0e7064d74b4a3f87a37ce8520ac513" Severity="[AlarmSeverity]Critical" TriggerModel="54e3a089202b4c288286720265ead5f8">
							<ChannelMonitorTriggerModel Alias="[string]bb1bdde6-5fd7-482f-b8aa-8aff63f7f135" AliasToMonitor="[string]Sink 99" Id="54e3a089202b4c288286720265ead5f8">
								<AboveValueTriggerModel Id="5a1365f6f2ba4178b9d1b8e633d72aed" />
							</ChannelMonitorTriggerModel>
						</AlarmModel>
					</PeAddonOutputInfo>
				</AddonModel>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="f5bbd13d97884601856e70932bb4908b" />
	</ChannelSpecification>
	<DataTypeReferenceTable xmlns="http://www.ni.com/PlatformFramework">
		<p.TypeReference TypeId="a39c785150f24ef9bb779edaf8bee0c5">
			<Composite Id="1" Name="" Cluster="" GenericTypeDefinition="Void" BaseType="Void">
				<Members>
					<Field FieldAccessPolicy="ReadWrite" Name="Name" DataType="String" />
					<Field FieldAccessPolicy="ReadWrite" Name="Value" DataType="@d6a5199331ae41169a213175b32dd925" />
				</Members>
			</Composite>
		</p.TypeReference>
		<p.TypeReference TypeId="d6a5199331ae41169a213175b32dd925">
			<Composite Id="1" Name="Variant" Sealed="" GenericTypeDefinition="Void" BaseType="Void" />
		</p.TypeReference>
	</DataTypeReferenceTable>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithSwitchBoard/Logging Specification.flxcfg sha256=5b6fc76612c56518a476bc0a559829c1937411d93c16fbe06bb6f15be28ef6a8 bytes=2112 -->
## FILE: tests/assets/ProjectWithSwitchBoard/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithSwitchBoard/Logging Specification.flxcfg`
- sha256: `5b6fc76612c56518a476bc0a559829c1937411d93c16fbe06bb6f15be28ef6a8`
- bytes: 2112

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="CCE6F3419D49B6D75A6CECF0A4B08193B48C6512FFD190AC64D1D428E21844CA6BC86823FBBFA386D5620C5B8EC836F1BAB81B6F8A5636C59A5E2D93961C4B98" Timestamp="1D6A7CBC802A6BD" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="7e44725217a460eb51c6a3150313d57">
			<ProcessingElementModelOwner Id="e6b558c32f124259b54c411db5df7345">
				<TriggeredLoggingProvider Id="9cdbeb19b7e24131929210c3523ca24e" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-08-17T12:28:04.130181999999999999974298336979927626089192926883697509765625-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="6d8bdcdab5ab42f4863fb014479bf50c" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="3f90aac8743c44f3914c9432fe7b8096">
						<UserDefinedMetadataItem DataType="String" Id="3470d409fde74c03bfc9a8135834c5b5" Name="Operator">
							<p.Value>bparrott</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="8279e73311e24f8d9343f3bfd4b6ac8e" Name="DUT">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithSwitchBoard/ProjectWithSwitchBoard.flxproj sha256=caf317793e85f98627534a06c5896bea2c6331538406638891c0dc36118e96bb bytes=4573 -->
## FILE: tests/assets/ProjectWithSwitchBoard/ProjectWithSwitchBoard.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithSwitchBoard/ProjectWithSwitchBoard.flxproj`
- sha256: `caf317793e85f98627534a06c5896bea2c6331538406638891c0dc36118e96bb`
- bytes: 4573

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="C0AE9091233E337E682423C93C2F5C89AF52653B2AEE6FDC554154A4E1108A72D71F083990CF7E006CBCA0C353BD08881A4661CB82B239D53580A019C849FFA6" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="542f06b4029b4d1db6deafe2b6b49ac3" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="268b76c5012c42aaa600ab789219a6a9" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="eb4edb53334f44eaae0353df8a8c5490" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="c11bc0055857440a9a4350adc71f0fc1" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="efbfda2d2fb64ea39cacf9db5e22f505" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="1a0ecc09cbb34cf7949a572b3370a370" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="19dfc46e01c64490aaa59eadcb110e34" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="4d65403a03e44ba9832f2ab6ea66d5f3" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="d9abccffb6594e5888ae688112f41bfc" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="2824e0b9735b49b08137ba4ef486e5fb" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="feadfd4d44140d58f852571aead11be" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="32f2fe8c4ad5425f999990b43867f701" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-08-17T17:28:04.9071124Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="7d861c6c52fc4aedb8f793efa088a894" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="71137c4350324e09a14d74abeb1ce550" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="30bd4a072735421cb2aa15d25d5b3b93" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithSwitchBoard/Screen.flxscr sha256=5dc254433bbe67bc46658038597f25d37b1e762ac953bbbc0701b66f695ccc18 bytes=1338 -->
## FILE: tests/assets/ProjectWithSwitchBoard/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithSwitchBoard/Screen.flxscr`
- sha256: `5dc254433bbe67bc46658038597f25d37b1e762ac953bbbc0701b66f695ccc18`
- bytes: 1338

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4750B27A24C20CBAF89F5CDBAFE5A3785BD5B3011161E99C9B8E16E7ED84C89F00A04AEBC408DFC1082C23528796283836DFFB7142B793AEAE8787D4F2EABF04" Timestamp="1D674BC82B5E34C" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="b836d9c8b77e43d49cce7319b0ff3bce" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="c7da2251281644589e0fc614cb64d29c" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithSwitchBoard/Test Specification.flxtest sha256=551e1ad76e3108793ef738917ea3d8a575dfa8303fde58baadd7ce855a2e0890 bytes=1055 -->
## FILE: tests/assets/ProjectWithSwitchBoard/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithSwitchBoard/Test Specification.flxtest`
- sha256: `551e1ad76e3108793ef738917ea3d8a575dfa8303fde58baadd7ce855a2e0890`
- bytes: 1055

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="B2983D872B981EB8BBA31433F8585565E171CE5E72200A7FBB85E92DECAEB152822A9C52D1AFBCCC3676BF55BCDF3EBDA6AEDF46C08754DC1993030F22382D20" Timestamp="1D674BC82B5E34C" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="c746ac9573b48bea655f7456cc258d8">
			<ProcessingElementModelOwner Id="233e407d7ca740b8b10c583f8e291fad" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithTestProperties/Channel Specification.flxio sha256=1ee78185d8e375f9b38405fd6d73f40cdca034e69db78da4ae3d4056a044a5d5 bytes=2544 -->
## FILE: tests/assets/ProjectWithTestProperties/Channel Specification.flxio

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithTestProperties/Channel Specification.flxio`
- sha256: `1ee78185d8e375f9b38405fd6d73f40cdca034e69db78da4ae3d4056a044a5d5`
- bytes: 2544

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2F4D6A7A2716121E00A891F65F4431E9440C844ABF7AE1BD0BEE55FF6D1ED0B534A28655BAF8028A5AE242BB417F6EE6F93CD3E83178B9A804D1BE02EE7846F2" Timestamp="1D66CCA9386BA27" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="FlexLogger DAQmx" Name="http://www.ni.com/FlexLogger/DAQmx" OldestCompatibleVersion="8.3.0.6" Version="8.3.0.6" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<ChannelSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<ChannelConfigurationModel Id="f0c8437308b74f78a27c2537ed9563ef">
			<ProcessingElementModelOwner Id="9f6d6edec6ba44a7bd4482e5a6c8fbcf">
				<DAQmxProcessingElement Id="79198f72c5944d27a12ad14ffb02fac8" xmlns="http://www.ni.com/FlexLogger/DAQmx">
					<TopLevelTimingOwner FallbackMediumSampleRateLevel="[SampleRateLevel]Fast" Id="2a4a9f0631d24a27993f8b09fb963b66">
						<SampleTiming Id="ceb375775e3c45c39a6853659e296fd5" Level="[SampleRateLevel]Slow" Units="[Unit]Hertz" Value="[double]1" />
						<SampleTiming Id="5b7040e9c0e9452c8c8f185723fb4aaf" Level="[SampleRateLevel]Medium" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="1d8d0a69737549f28d5355c961f5aead" Level="[SampleRateLevel]Fast" Units="[Unit]Hertz" Value="[double]1000" />
						<SampleTiming Id="cc1762641ac54bfaa02f688aceb74ce4" Level="[SampleRateLevel]Counter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="d54503269071427eb5b2f20dfadb6151" Level="[SampleRateLevel]LegacyCounter" Units="[Unit]Hertz" Value="[double]100" />
						<SampleTiming Id="acd7521b9f8246a9a80819130dd325b5" Level="[SampleRateLevel]Digital" Units="[Unit]Hertz" Value="[double]10" />
						<OnDemandTiming Id="564cb732a39b4c249c43708aaa2ad705" Level="[SampleRateLevel]OnDemand" />
					</TopLevelTimingOwner>
				</DAQmxProcessingElement>
			</ProcessingElementModelOwner>
		</ChannelConfigurationModel>
		<ChassisModelOwner Id="36ad1aa875454be691d297ce1f8c18f8" />
	</ChannelSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithTestProperties/Logging Specification.flxcfg sha256=3f2e81db04e9797d32eaec9d5deb3e54c20fed9cd72f494774675f43d9c1aaac bytes=2769 -->
## FILE: tests/assets/ProjectWithTestProperties/Logging Specification.flxcfg

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithTestProperties/Logging Specification.flxcfg`
- sha256: `3f2e81db04e9797d32eaec9d5deb3e54c20fed9cd72f494774675f43d9c1aaac`
- bytes: 2769

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D8E2D2BE7E8017AF0A0F355416483DCFD9B06B9592ED94F3C87D6A8E07DBAE8DC6D1205F2373CD5FDECD40D2BBC79487902C33B16E2046B47FFE87838F828BD1" Timestamp="1D6A7CA4D2E8771" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="21.0.0.0" />
	</SourceModelFeatureSet>
	<LoggingSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<LoggingConfigurationModel Id="f576f7d45bbb483f97eacfe876781021">
			<ProcessingElementModelOwner Id="c36b0f6a1de341ae9f08823dadc39637">
				<TriggeredLoggingProvider Id="ec1b3bf619aa46ba85486b6ccf47c414" ModelTypeId="[string]CBA104E4-2D21-4AC7-915B-D7DCC1243DCE" StartTime="2020-08-07T09:47:00.485542799999999999979553855222746960862423293292522430419921875-05:00" />
				<TdmsLoggingProvider DataReductionStrategy="Decimate" Id="44c2378b093f4dbaa9f3e2ea9ada589f" LogFileBackupPath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data\\backups&quot;" LogFileBasePath="&quot;C:\\Users\\Public\\Documents\\FlexLogger\\data&quot;" ModelTypeId="[string]59163356-411F-436B-A6B6-82FB1EFB19E1">
					<UserDefinedMetadata Id="95a7203a63e64a3e8ffd855f313486c1">
						<UserDefinedMetadataItem DataType="String" Id="30ca61a875934f46a512289cd69f7df2" Name="Operator">
							<p.Value>bparrott</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="c0e3319f484e4546bc905ed03ca4b54e" IsPromptOnStartActivated="True" Name="DUT">
							<p.Value>Serial number: &lt;replace with serial number&gt;</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="2c60b325dfa54c4dbc3fa3a829ca1468" Name="Property">
							<p.Value>""</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="e82bd7b4d28e47a3b057c3b937e217cd" Name="Best Configuration Based Data Logging Software">
							<p.Value>FlexLogger</p.Value>
						</UserDefinedMetadataItem>
						<UserDefinedMetadataItem DataType="String" Id="faed8dcc8f774b6d9bada17e9ffaceb4" Name="Who you gonna call?">
							<p.Value>Ghostbusters</p.Value>
						</UserDefinedMetadataItem>
					</UserDefinedMetadata>
				</TdmsLoggingProvider>
			</ProcessingElementModelOwner>
		</LoggingConfigurationModel>
	</LoggingSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithTestProperties/ProjectWithTestProperties.flxproj sha256=5555a0951ccff239841bd5c213e8201847877506d70a33c4333b8fbec0a63319 bytes=4480 -->
## FILE: tests/assets/ProjectWithTestProperties/ProjectWithTestProperties.flxproj

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithTestProperties/ProjectWithTestProperties.flxproj`
- sha256: `5555a0951ccff239841bd5c213e8201847877506d70a33c4333b8fbec0a63319`
- bytes: 4480

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="42395A86B5D183BD43D8BE7FC6CDC0F390771AC5FDD2D78C9E3E9C2BD7A3C5CE9B62CE351EBE1BADADFAAE2C9E5F63798E8966DC21640F6424CCE412EC04EC64" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="3c9448190be54f459c276b8ce6991a71" ModelDefinitionType="NationalInstruments.Lumberjack.Core.ChannelSpecification.ChannelSpecificationDefinition" Name="Channel Specification.flxio" StoragePath="Channel Specification.flxio" />
			<SourceFileReference Id="1fcfcfa6fb40437aac5f8085cc8af51e" ModelDefinitionType="NationalInstruments.Lumberjack.Core.LoggingSpecification.LoggingSpecificationDefinition" Name="Logging Specification.flxcfg" StoragePath="Logging Specification.flxcfg" />
			<SourceFileReference Id="c8c4c92c26314b3dba4ba51b14c3be93" ModelDefinitionType="NationalInstruments.Lumberjack.Core.TestSpecification.TestSpecificationDefinition" Name="Test Specification.flxtest" StoragePath="Test Specification.flxtest" />
			<SourceFileReference Id="ae2c38f226d54056a6f5b65989d17920" ModelDefinitionType="NationalInstruments.Lumberjack.Core.Screen.ScreenModel" Name="Screen.flxscr" StoragePath="Screen.flxscr" />
			<EmbeddedDefinitionReference Id="5c70ef306d2843d3b9ef72a5b1107bfd" ModelDefinitionType="PublishSkylineTagsDefinition" Name="PublishSkylineTagsDefinition" Reparentable="False">
				<PublishSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="b9a0ee111ddf4d3688317f04a043d90c" ModelDefinitionType="ConsumeExternalSkylineTagsDefinition" Name="ConsumeExternalSkylineTagsDefinition" Reparentable="False">
				<ConsumeExternalSkylineTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="109ffab7f2d64f5d8a5ffd6e22dfd5f9" ModelDefinitionType="PublishSkylineCloudTagsDefinition" Name="PublishSkylineCloudTagsDefinition" Reparentable="False">
				<PublishSkylineCloudTagsDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="5e90c473842946dbbc5b5f3e2d424736" ModelDefinitionType="PublishSkylineCloudApiKeyDefinition" Name="PublishSkylineCloudApiKeyDefinition" Reparentable="False">
				<PublishSkylineCloudApiKeyDefinition xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="249c5b079ba4f9381b846f2b850b968" ModelDefinitionType="ProjectCreationDate" Name="ProjectCreationDate" Reparentable="False">
				<ProjectCreationDate DateTime="2020-08-07T14:47:00.9333480Z" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="d91c3abb79624a3f9b6adc0a1c0ce234" ModelDefinitionType="ProjectRunNumber" Name="ProjectRunNumber" Reparentable="False">
				<ProjectRunNumber RunNumber="0" xmlns="http://www.ni.com/Lumberjack.Core" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="8c694ff887fc45a2a5d44516bbe7c85c" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
			<EmbeddedDefinitionReference Id="5cf81a48b0d248e3bdd8ed8a66ae2a80" ModelDefinitionType="PackageReferencesDefinition" Name="ProjectReferences">
				<PackageReferencesDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithTestProperties/Screen.flxscr sha256=c845a7a42e08057c2c79682504f74ba615c69a46ed147b7cf8ecfcf80c92c88c bytes=1338 -->
## FILE: tests/assets/ProjectWithTestProperties/Screen.flxscr

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithTestProperties/Screen.flxscr`
- sha256: `c845a7a42e08057c2c79682504f74ba615c69a46ed147b7cf8ecfcf80c92c88c`
- bytes: 1338

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="6A7E091C195A3740162C5D045EDA3E9D84CF5E85B70B844386B4167D2BD2ADB21F02AF289CE008DDB11886C415DE61FDF8F55363FB3D2BEFA2124FDE7CDCE7B2" Timestamp="1D66CCA938EA3D5" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2344" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<Screen Id="fefe647451df40408654714b2453064f" xmlns="http://www.ni.com/Lumberjack.Core">
		<ScreenSurface Height="[float]1600" Id="86ba3674f3274dc28dcad0bcaa29fd7c" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]2000" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core" />
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/ProjectWithTestProperties/Test Specification.flxtest sha256=a98506edd010d3c44dd7aa350c29ce861401303f94d7459d3ca523f469e6fd1c bytes=1055 -->
## FILE: tests/assets/ProjectWithTestProperties/Test Specification.flxtest

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/ProjectWithTestProperties/Test Specification.flxtest`
- sha256: `a98506edd010d3c44dd7aa350c29ce861401303f94d7459d3ca523f469e6fd1c`
- bytes: 1055

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="866FD63DCF3F50DABCA4624011E5EDD7DE5DD0F788E1BB0F38349947E60D80A90D3CDA19CBC090765094697F6C00D7FF68512F9488AF45350769437AF8165F3B" Timestamp="1D66CCA938D9322" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Lumberjack Core" Name="http://www.ni.com/Lumberjack.Core" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="8.3.0.2028" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="8.3.0.2028" Name="FlexLogger" Version="20.3.0.0" />
	</SourceModelFeatureSet>
	<TestSpecification xmlns="http://www.ni.com/Lumberjack.Core">
		<EventConfigurationModel Id="8fcee9485644411e85b8a647334914ff">
			<ProcessingElementModelOwner Id="66db5b0bad340f3a4b8eae8af509f10" />
		</EventConfigurationModel>
	</TestSpecification>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/assets/pythonTests.config sha256=f820cdaba2b3f1077256407d7ede0745b1aae23843df617e3184d0127175fdd9 bytes=74 -->
## FILE: tests/assets/pythonTests.config

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/assets/pythonTests.config`
- sha256: `f820cdaba2b3f1077256407d7ede0745b1aae23843df617e3184d0127175fdd9`
- bytes: 74

````text
{"AdditionalPluginPaths":["<path to git repo>\\tests\\assets\\Plugins"]}
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/conftest.py sha256=241a8a5bbdd7200ebb622f9b13ada92963546fd98167a8d77d3a308eae81d8ce bytes=1142 -->
## FILE: tests/conftest.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/conftest.py`
- sha256: `241a8a5bbdd7200ebb622f9b13ada92963546fd98167a8d77d3a308eae81d8ce`
- bytes: 1142

````python
from typing import Iterator

import pytest
from flexlogger.automation import (
    Application,
    FlexLoggerError,
    TestProperty,
    TestSession,
    TestSessionState,
    TestSpecificationDocument,
)

# Prevent pytest from thinking real classes are test classes
TestProperty.__test__ = False  # type: ignore
TestSession.__test__ = False  # type: ignore
TestSessionState.__test__ = False  # type: ignore
TestSpecificationDocument.__test__ = False  # type: ignore


# This needs to be at class scope because of the order pytest runs tests in.
# It runs a class at a time, so we can't reuse this across classes in case
# tests have run that need to call utils.kill_all_open_flexloggers()
@pytest.fixture(scope="class")
def app() -> Iterator[Application]:
    """Fixture for launching FlexLogger.

    This is useful to improve test time by not launching/closing FlexLogger in every test.
    """
    app = Application.launch()
    yield app
    try:
        app.close()
    except FlexLoggerError:
        # utils.kill_all_open_flexloggers may have killed this process already, that's fine
        pass
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/start_test_separate_process.py sha256=7269989b3372dbc5c6775e63c1051024c8548249bd9f2391b72876516c1ab399 bytes=865 -->
## FILE: tests/start_test_separate_process.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/start_test_separate_process.py`
- sha256: `7269989b3372dbc5c6775e63c1051024c8548249bd9f2391b72876516c1ab399`
- bytes: 865

````python
import sys
import time
from typing import List

from flexlogger.automation import Application


def main(argv: List[str]) -> int:
    """Connect to FlexLogger and start a test"""
    with Application.launch() as app:
        project = app.open_project(argv[0])
        temp_dir = argv[1]
        logging_specification = project.open_logging_specification_document()
        logging_specification.set_log_file_base_path(temp_dir)
        logging_specification.set_log_file_name("ShouldNotExist.tdms")
        logging_specification.set_test_property("prompts on start", "some value", True)
        project.test_session.start()
        # Make sure that if this does start running, it will actually log data
        # before we close the project.
        time.sleep(5)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_application.py sha256=1f972fb3387990a576739b2cac53b11ad02af0667e4621fd2717aeeffc00c790 bytes=545 -->
## FILE: tests/test_application.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_application.py`
- sha256: `1f972fb3387990a576739b2cac53b11ad02af0667e4621fd2717aeeffc00c790`
- bytes: 545

````python
from flexlogger.automation import Application
import pytest  # type: ignore
import re


class TestApplication:
    @pytest.mark.integration  # type: ignore
    def test__launch_flexLogger__get_versions__versions_match_pattern(self, app: Application) -> None:
        version, version_string = app.get_version()

        version_pattern = re.compile(r"2\d.\d.\d.\d")
        assert version_pattern.match(version)
        version_string_pattern = re.compile(r"20\d\d Q\d")
        assert version_string_pattern.match(version_string)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_channel_specification_document.py sha256=f34ba9b91331afaf12e890daad2927a881ef1e3364296cec209e01d79cd3456a bytes=10324 -->
## FILE: tests/test_channel_specification_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_channel_specification_document.py`
- sha256: `f34ba9b91331afaf12e890daad2927a881ef1e3364296cec209e01d79cd3456a`
- bytes: 10324

````python
from datetime import datetime, timedelta, timezone
from time import sleep
from typing import Iterator
import time

import pytest  # type: ignore
from flexlogger.automation import (
    Application,
    ChannelDataPoint,
    ChannelSpecificationDocument,
    DataRateLevel,
    FlexLoggerError,
)

from .utils import get_project_path, open_project


@pytest.fixture(scope="class")
def channels_with_produced_data(app: Application) -> Iterator[ChannelSpecificationDocument]:
    """Fixture for opening the channel specification document for ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    """
    with open_project(app, "ProjectWithProducedData") as project:
        yield project.open_channel_specification_document()


class TestChannelSpecificationDocument:
    @pytest.mark.integration  # type: ignore
    def test__get_channel_names__all_names_returned(self, app: Application) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            channel_specification = project.open_channel_specification_document()
            produced_data_channel_names = channel_specification.get_channel_names()
        with open_project(app, "ProjectWithTestProperties") as project:
            channel_specification = project.open_channel_specification_document()
            test_properties_channel_names = channel_specification.get_channel_names()
        assert "Channel 1" in produced_data_channel_names
        assert "Channel 2" in produced_data_channel_names
        produced_data_channel_names.remove("Channel 1")
        produced_data_channel_names.remove("Channel 2")
        assert sorted(produced_data_channel_names) == sorted(test_properties_channel_names)

    @pytest.mark.integration  # type: ignore
    def test__project_with_channels__get_value__values_are_changing_and_timestamps_incrementing(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        first_channel_value = channel_specification.get_channel_value("Channel 1")
        sleep(0.5)
        second_channel_value = channel_specification.get_channel_value("Channel 1")

        assert "Channel 1" == first_channel_value.name
        assert "Channel 1" == second_channel_value.name
        assert first_channel_value.value != second_channel_value.value
        assert first_channel_value.timestamp < second_channel_value.timestamp

    @pytest.mark.integration  # type: ignore
    def test__get_channel_value_for_channel_that_does_not_exist__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.get_channel_value("Not a channel")

    @pytest.mark.integration  # type: ignore
    def test__project_with_writable_channels__set_channel_value__channel_value_updated(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithSwitchboard") as project:
            channel_specification = project.open_channel_specification_document()
            now = datetime.now(timezone.utc)
            channel_specification.set_channel_value("Switch 42", 84.5)

            wait_for_channel_value_changed_timeout = 5
            start = time.time()
            updated_value = channel_specification.get_channel_value("Switch 42")
            while (updated_value.value != 84.5) and (time.time() - start < wait_for_channel_value_changed_timeout):
                sleep(0.1)

            assert "Switch 42" == updated_value.name
            assert 84.5 == updated_value.value
            assert updated_value.timestamp >= now
            assert updated_value.timestamp - now < timedelta(minutes=1)

    @pytest.mark.integration  # type: ignore
    def test__set_channel_value_for_channel_that_does_not_exist__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_value("Not a channel", 42)

    @pytest.mark.integration  # type: ignore
    def test__set_channel_value_for_readonly_channel__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_value("Channel 1", 42)

    @pytest.mark.integration  # type: ignore
    def test__close_project_with_channels__get_value__exception_raised(
        self, app: Application
    ) -> None:
        project = app.open_project(get_project_path("ProjectWithProducedData"))
        channel_specification = project.open_channel_specification_document()
        project.close()
        with pytest.raises(FlexLoggerError):
            channel_specification.get_channel_value("Channel 1")

    @pytest.mark.integration  # type: ignore
    def test__channeldatapoint_repr__returns_correct_string(self) -> None:
        channel_data_point = ChannelDataPoint("Channel", 2.5, datetime.now())
        expected_repr = 'flexlogger.automation.ChannelDataPoint("Channel", 2.500000, %s)' % repr(
            channel_data_point.timestamp
        )
        assert expected_repr == repr(channel_data_point)

    @pytest.mark.integration  # type: ignore
    def test__project_with_writable_channels__disable_channel__channel_disabled(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithSwitchboard") as project:
            channel_specification = project.open_channel_specification_document()

            channel_specification.set_channel_enabled("Sink 42", False)

            channel_enabled = channel_specification.is_channel_enabled("Sink 42")

            assert not channel_enabled

    @pytest.mark.integration  # type: ignore
    def test__set_channel_enabled_for_channel_that_does_not_exist__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_enabled("Not a channel", True)

    @pytest.mark.integration  # type: ignore
    def test__set_channel_enabled_for_readonly_channel__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_enabled("Channel 1", False)

    @pytest.mark.integration  # type: ignore
    def test__project_with_writable_channels__disable_channel_logging__channel_logging_disabled(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithSwitchboard") as project:
            channel_specification = project.open_channel_specification_document()

            channel_specification.set_channel_logging_enabled("Sink 42", False)

            channel_logging_enabled = channel_specification.is_channel_logging_enabled("Sink 42")

            assert not channel_logging_enabled

    @pytest.mark.integration  # type: ignore
    def test__project_with_writable_channels__channel_logging_enabled(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithSwitchboard") as project:
            channel_specification = project.open_channel_specification_document()

            channel_logging_enabled = channel_specification.is_channel_logging_enabled("Sink 42")

            assert channel_logging_enabled

    @pytest.mark.integration  # type: ignore
    def test__set_channel_logging_enabled_for_channel_that_does_not_exist__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_logging_enabled("Not a channel", True)

    @pytest.mark.integration  # type: ignore
    def test__set_channel_logging_enabled_for_readonly_channel__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data
        with pytest.raises(FlexLoggerError):
            channel_specification.set_channel_logging_enabled("Channel 1", False)

    @pytest.mark.integration  # type: ignore
    def test__project_with_channels__set_data_rate__data_rate_updated(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data

        channel_specification.set_data_rate(DataRateLevel.SLOW, 2)

        data_rate = channel_specification.get_data_rate(DataRateLevel.SLOW)
        assert data_rate == 2

    @pytest.mark.integration  # type: ignore
    def test__project_with_channels__get_data_rate_level_on_invalid_channel__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data

        with pytest.raises(FlexLoggerError):
            channel_specification.get_data_rate_level("Channel 1")

    @pytest.mark.integration  # type: ignore
    def test__project_with_channels__set_data_rate_level_on_invalid_channel__exception_raised(
        self, app: Application, channels_with_produced_data: ChannelSpecificationDocument
    ) -> None:
        channel_specification = channels_with_produced_data

        with pytest.raises(FlexLoggerError):
            channel_specification.set_data_rate_level("Channel 1", DataRateLevel.SLOW)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_events.py sha256=e2926fcaf10c1c5b926e9a5c5a5df90a1b18aed6d2bf8df8732b0ef02c78cdf0 bytes=6748 -->
## FILE: tests/test_events.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_events.py`
- sha256: `e2926fcaf10c1c5b926e9a5c5a5df90a1b18aed6d2bf8df8732b0ef02c78cdf0`
- bytes: 6748

````python
from .utils import open_project
import datetime
from flexlogger.automation import (
    Application,
    EventPayload,
    EventNames,
    EventType
)
import pytest  # type: ignore

received_event_type = None
received_event_payload = None


def generic_event_handler(application: Application, event_type: EventType, payload: EventPayload):
    """Event Handler
    This method will be called when a file event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: EventPayload       The event payload
    """
    global received_event_type
    global received_event_payload

    received_event_type = event_type
    received_event_payload = payload
    print("Event received: {}".format(event_type))


class TestEvents:
    @staticmethod
    def wait_for_registered_events(event_handler, timeout=3) -> [EventType]:
        start_time = datetime.datetime.now()
        while True:
            registered_events = event_handler.get_registered_events()
            current_time = datetime.datetime.now()
            delta = current_time - start_time
            if len(registered_events) > 0 or delta.total_seconds() > timeout:
                break

        return registered_events

    @staticmethod
    def wait_for_event(event_type=None, event_name=None, timeout=5) -> bool:
        global received_event_type
        global received_event_payload

        start_time = datetime.datetime.now()
        while True:
            correct_event_type = received_event_type == event_type if event_type is not None else True
            if event_name is not None:
                correct_event_name = False if received_event_payload is None else received_event_payload.event_name == event_name
            else:
                correct_event_name = True

            current_time = datetime.datetime.now()
            delta = current_time - start_time
            if (correct_event_type and correct_event_name) or delta.total_seconds() > timeout:
                break

        return correct_event_type and correct_event_name

    @staticmethod
    def reset_event() -> [None]:
        global received_event_type
        global received_event_payload
        received_event_type = None
        received_event_payload = None

    @pytest.mark.integration  # type: ignore
    def test__register_events__events_registered(self, app: Application) -> None:
        self.reset_event()
        event_handler = app.event_handler
        event_handler.register_event_callback(generic_event_handler, [EventType.ALARM])
        registered_events = self.wait_for_registered_events(event_handler)
        assert EventType.ALARM in registered_events
        assert event_handler._is_subscribed
        event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test__unregister_events__no_events_registered(self, app: Application) -> None:
        self.reset_event()
        event_handler = app.event_handler
        event_handler.register_event_callback(generic_event_handler, [EventType.ALARM])
        event_handler.unregister_from_events()
        registered_events = self.wait_for_registered_events(event_handler)
        assert len(registered_events) == 0
        assert not event_handler._is_subscribed
        event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test__start_session__session_event_received(self, app: Application) -> None:
        self.reset_event()
        with open_project(app, "ProjectWithProducedData") as project:
            event_handler = app.event_handler
            event_handler.register_event_callback(generic_event_handler, [EventType.TEST_SESSION])
            session = project.test_session
            session.start()
            event_received = self.wait_for_event(EventType.TEST_SESSION, EventNames.TEST_STARTED)
            assert event_received
            event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test__start_session__log_file_created_event_received(self, app: Application) -> None:
        self.reset_event()
        with open_project(app, "ProjectWithProducedData") as project:
            event_handler = app.event_handler
            event_handler.register_event_callback(generic_event_handler, [EventType.LOG_FILE])
            session = project.test_session
            session.start()
            event_received = self.wait_for_event(EventType.LOG_FILE, EventNames.LOG_FILE_CREATED)
            assert event_received
            event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test__stop_session__session_event_received(self, app: Application) -> None:
        self.reset_event()
        with open_project(app, "ProjectWithProducedData") as project:
            event_handler = app.event_handler
            event_handler.register_event_callback(generic_event_handler, [EventType.TEST_SESSION])
            session = project.test_session
            session.start()
            session.stop()
            event_received = self.wait_for_event(EventType.TEST_SESSION, EventNames.TEST_STOPPED)
            assert event_received
            event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test__stop_session__log_file_closed_event_received(self, app: Application) -> None:
        self.reset_event()
        with open_project(app, "ProjectWithProducedData") as project:
            event_handler = app.event_handler
            event_handler.register_event_callback(generic_event_handler, [EventType.LOG_FILE])
            session = project.test_session
            session.start()
            session.stop()
            event_received = self.wait_for_event(EventType.LOG_FILE, EventNames.LOG_FILE_CLOSED)
            assert event_received
            event_handler.unregister_from_events()

    @pytest.mark.integration  # type: ignore
    def test_open_project_with_alarms__start_session__alarm_event_received(self, app: Application) -> None:
        self.reset_event()
        with open_project(app, "ProjectWithAlarms") as project:
            event_handler = app.event_handler
            event_handler.register_event_callback(generic_event_handler, [EventType.ALARM])
            session = project.test_session
            session.start()
            event_received = self.wait_for_event(EventType.ALARM)
            assert event_received
            event_handler.unregister_from_events()
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_logging_specification_document.py sha256=6622483d7f2148007c5b727ed2b8ade500ec9503e0d1b780635aa60da870ca9b bytes=36416 -->
## FILE: tests/test_logging_specification_document.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_logging_specification_document.py`
- sha256: `6622483d7f2148007c5b727ed2b8ade500ec9503e0d1b780635aa60da870ca9b`
- bytes: 36416

````python
from datetime import datetime
from datetime import timedelta
from dateutil import tz
from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep
from typing import Iterator, Optional

import pytest  # type: ignore
from flexlogger.automation import (
    Application,
    FlexLoggerError,
    LogFileType,
    LoggingSpecificationDocument,
    Project,
    StartTriggerCondition,
    StopTriggerCondition,
    TestProperty,
    ValueChangeCondition,
    ValueChangeType
)
from nptdms import TdmsFile  # type: ignore

from .utils import get_project_path, open_project, copy_project


@pytest.fixture(scope="class")
def logging_spec_with_test_properties(app: Application) -> Iterator[LoggingSpecificationDocument]:
    """Fixture for opening the logging specification document for ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    Note that using this fixture means the test may not modify the project.
    """
    with open_project(app, "ProjectWithTestProperties") as project:
        yield project.open_logging_specification_document()

@pytest.fixture(scope="class")
def project_with_produced_data(app: Application) -> Iterator[Project]:
    """Fixture for opening ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    """
    with copy_project("ProjectWithProducedData") as project_path:
        project = app.open_project(project_path)
        yield project
        try:
            project.close()
        except FlexLoggerError:
            # utils.kill_all_open_flexloggers may have killed this process already, that's fine
            pass


class TestLoggingSpecificationDocument:
    @pytest.mark.integration  # type: ignore
    def test__open_project__get_logging_path__logging_path_matches_user_setting(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            assert r"C:\MyDataGoesHere" == logging_specification.get_log_file_base_path()
            assert r"MyData.tdms" == logging_specification.get_log_file_name()

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_logging_path__logging_path_updates(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            logging_specification.set_log_file_base_path(r"C:\MyDataGoesThere")
            logging_specification.set_log_file_name(r"EvenMoreData.tdms")

            assert r"C:\MyDataGoesThere" == logging_specification.get_log_file_base_path()
            assert r"EvenMoreData.tdms" == logging_specification.get_log_file_name()

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_logging_path__resolved_logging_path_updates(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()

            logging_specification.set_log_file_base_path(r"C:\{Operator}")
            logging_specification.set_log_file_name(
                r"{Best Configuration Based Data Logging Software}.tdms"
            )

            assert r"C:\bparrott" == logging_specification.get_resolved_log_file_base_path()
            assert r"FlexLogger.tdms" == logging_specification.get_resolved_log_file_name()

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__set_logging_base_path__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            with pytest.raises(FlexLoggerError):
                logging_specification.set_log_file_base_path(r"C:\NewBasePath")

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__get_logging_base_path__no_exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            base_path = logging_specification.get_log_file_base_path()
            assert base_path is not None

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__set_logging_name__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            with pytest.raises(FlexLoggerError):
                logging_specification.set_log_file_name(r"NewName")

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__get_logging_name__no_exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            name = logging_specification.get_log_file_name()
            assert name is not None

    @pytest.mark.integration  # type: ignore
    def test__open_project__get_logging_description__logging_description_matches_user_setting(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            assert r"This is the description of the log file." == logging_specification.get_log_file_description()

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_logging_description__logging_path_updates(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            new_description = r"This is the new description of the log file."
            # Precondition
            assert new_description != logging_specification.get_log_file_description()
            logging_specification.set_log_file_description(new_description)

            assert new_description == logging_specification.get_log_file_description()


    @pytest.mark.integration  # type: ignore
    def test__test_session_ran__remove_log_files__no_log_file_returned(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        sleep(2.0)
        project.test_session.stop()

        logging_specification = project.open_logging_specification_document()
        logging_specification.remove_log_files(delete_files=True)

        log_files = logging_specification.get_log_files(LogFileType.TDMS)
        assert len(log_files) == 0

    @pytest.mark.integration  # type: ignore
    def test__test_session_ran__get_log_files__log_file_returned(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        logging_specification = project.open_logging_specification_document()
        logging_specification.remove_log_files(delete_files=True)
        project.test_session.start()
        sleep(2.0)
        project.test_session.stop()

        log_files = logging_specification.get_log_files(LogFileType.TDMS)

        assert len(log_files) == 1
        assert Path(log_files[0]).exists() is True

    @pytest.mark.integration  # type: ignore
    def test__test_session_ran_twice__get_log_files__two_log_files_returned(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        logging_specification = project.open_logging_specification_document()
        logging_specification.remove_log_files(delete_files=True)
        project.test_session.start()
        sleep(2.0)
        project.test_session.stop()
        project.test_session.start()
        sleep(2.0)
        project.test_session.stop()

        log_files = logging_specification.get_log_files(LogFileType.TDMS)

        assert len(log_files) == 2
        assert Path(log_files[0]).exists() is True
        assert Path(log_files[1]).exists() is True
        assert Path(log_files[0]).stat().st_ctime < Path(log_files[1]).stat().st_ctime

    @pytest.mark.integration  # type: ignore
    def test__open_project__get_test_properties__all_properties_returned(
        self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument
    ) -> None:
        properties = logging_spec_with_test_properties.get_test_properties()

        assert 5 == len(properties)
        self.assert_property_matches(properties[0], "Operator", "bparrott", False)
        self.assert_property_matches(
            properties[1], "DUT", "Serial number: <replace with serial number>", True
        )
        self.assert_property_matches(properties[2], "Property", "", False)
        self.assert_property_matches(
            properties[3], "Best Configuration Based Data Logging Software", "FlexLogger", False
        )
        self.assert_property_matches(properties[4], "Who you gonna call?", "Ghostbusters", False)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_test_properties__all_properties_update(
        self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument
    ) -> None:
            # Precondition
            properties = logging_spec_with_test_properties.get_test_properties()
            assert 5 == len(properties)
            # #  Name                          Value               Prompt_on_start
            # 0  Operator                      bparrott            false
            # 1  DUT                           Serial number: ...  true
            # 2  Property                      string.Empty        false
            # 3  Best Configuration Based ...  FlexLogger          false
            # 4  Who you gonna call?           Ghostbusters        false
            logging_spec_with_test_properties.set_test_properties([
                TestProperty("Operator", "peteri", True),                        # change value and prompt
                TestProperty("DUT", "12345", True),                              # change value
                TestProperty("I cannot think", "of anything to put here", False) # add property
            ])

            properties = logging_spec_with_test_properties.get_test_properties()
            assert 6 == len(properties)
            self.assert_property_matches(properties[0], "Operator", "peteri", True)
            self.assert_property_matches(properties[1], "DUT", "12345", True)
            self.assert_property_matches(properties[2], "Property", "", False)
            self.assert_property_matches(
                properties[3], "Best Configuration Based Data Logging Software", "FlexLogger", False
            )
            self.assert_property_matches(properties[4], "Who you gonna call?", "Ghostbusters", False)
            self.assert_property_matches(properties[5], "I cannot think", "of anything to put here", False)

    @pytest.mark.integration  # type: ignore
    def test__open_project__get_test_properties__get_test_property_matches(
        self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument
    ) -> None:
        properties = logging_spec_with_test_properties.get_test_properties()

        for prop in properties:
            actual_prop = logging_spec_with_test_properties.get_test_property(prop.name)
            self.assert_property_matches(actual_prop, prop.name, prop.value, prop.prompt_on_start)

    @pytest.mark.integration  # type: ignore
    def test__open_project__get_test_property_that_does_not_exist__exception_raised(
        self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()
            with pytest.raises(FlexLoggerError):
                logging_specification.get_test_property("DoesNotExist")

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_test_property_that_does_exist__property_is_updated(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()
            assert 5 == len(logging_specification.get_test_properties())

            logging_specification.set_test_property("Property", "New Property Value", True)

            assert 5 == len(logging_specification.get_test_properties())
            new_prop = logging_specification.get_test_property("Property")
            self.assert_property_matches(new_prop, "Property", "New Property Value", True)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_test_property_that_does_exist__property_is_updated_in_tdms(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            logging_specification = project.open_logging_specification_document()
            with TemporaryDirectory() as temp_dir:
                logging_specification.set_log_file_base_path(temp_dir)
                logging_specification.set_log_file_name("PropertyThatExists.tdms")

                logging_specification.set_test_property("Operator", "A new operator", False)
                # Run the test so the TDMS file gets written
                project.test_session.start()
                sleep(5)
                project.test_session.stop()

                new_value = self._get_tdms_file_property(
                    temp_dir, "PropertyThatExists.tdms", "Operator"
                )
                assert new_value == "A new operator"

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_test_property_that_does_not_exist__property_exists_in_tdms(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            logging_specification = project.open_logging_specification_document()
            with TemporaryDirectory() as temp_dir:
                logging_specification.set_log_file_base_path(temp_dir)
                logging_specification.set_log_file_name("PropertyThatDoesNotExist.tdms")

                logging_specification.set_test_property("Something new", "I'm new!", False)
                # Run the test so the TDMS file gets written
                project.test_session.start()
                sleep(5)
                project.test_session.stop()

                new_value = self._get_tdms_file_property(
                    temp_dir, "PropertyThatDoesNotExist.tdms", "Something new"
                )
                assert new_value == "I'm new!"

    @pytest.mark.integration  # type: ignore
    def test__open_project__remove_test_property___property_does_not_exist_in_tdms(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            logging_specification = project.open_logging_specification_document()
            with TemporaryDirectory() as temp_dir:
                logging_specification.set_log_file_base_path(temp_dir)
                logging_specification.set_log_file_name("PropertyThatWasRemoved.tdms")

                logging_specification.remove_test_property("Operator")
                # Run the test so the TDMS file gets written
                project.test_session.start()
                sleep(5)
                project.test_session.stop()

                new_value = self._get_tdms_file_property(
                    temp_dir, "PropertyThatWasRemoved.tdms", "Operator"
                )
                assert new_value is None

    def _get_tdms_file_property(
        self, log_file_base_path: str, log_file_name: str, property_name: str
    ) -> Optional[str]:
        log_file_path = Path(log_file_base_path) / log_file_name
        with TdmsFile.open(str(log_file_path)) as tdms_file:
            real_property_name = f"Test_properties~{property_name}"
            return tdms_file.properties.get(real_property_name)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_test_property_that_does_not_exist__property_is_added(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()
            assert 5 == len(logging_specification.get_test_properties())

            logging_specification.set_test_property("New Property", "some value", False)

            assert 6 == len(logging_specification.get_test_properties())
            new_prop = logging_specification.get_test_property("New Property")
            self.assert_property_matches(new_prop, "New Property", "some value", False)

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__set_test_property__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            with pytest.raises(FlexLoggerError):
                logging_specification.set_test_property("Nope", "Sorry", True)

    @pytest.mark.integration  # type: ignore
    @pytest.mark.parametrize("name", ["", "12UCannotDoThat", "@!:.#IllegalChars"])  # type: ignore
    def test__set_test_property_with_invalid_name__exception_raised(
        self, app: Application, name: str
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()

            with pytest.raises(FlexLoggerError):
                logging_specification.set_test_property(name, "nope", False)

    @pytest.mark.integration  # type: ignore
    def test__remove_test_property__test_property_removed(self, app: Application) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()
            existing_properties = logging_specification.get_test_properties()
            assert 5 == len(existing_properties)
            assert "Property" in (prop.name for prop in existing_properties)

            logging_specification.remove_test_property("Property")

            new_properties = logging_specification.get_test_properties()
            assert 4 == len(new_properties)
            assert "Property" not in (prop.name for prop in new_properties)
            try:
                logging_specification.get_test_property("Property")
                assert False  # did not throw exception
            except FlexLoggerError as err:
                # Ensure the FlexLoggerError shows a description of what went wrong
                # Note that repr(err) is what gets displayed in the interactive console
                displayed_string = repr(err)
                assert "Failed to get" in displayed_string
                assert "The requested test property is not defined" in displayed_string

    @pytest.mark.integration  # type: ignore
    def test__remove_test_property_that_does_not_exist__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithTestProperties") as project:
            logging_specification = project.open_logging_specification_document()
            with pytest.raises(FlexLoggerError):
                logging_specification.remove_test_property("DoesNotExist")

    @pytest.mark.integration  # type: ignore
    def test__start_test_session__remove_test_property__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            project.test_session.start()
            logging_specification = project.open_logging_specification_document()

            with pytest.raises(FlexLoggerError):
                logging_specification.remove_test_property("Property")

    @pytest.mark.integration  # type: ignore
    def test__close_project__get_test_properties__exception_raised(self, app: Application) -> None:
        project = app.open_project(get_project_path("ProjectWithProducedData"))
        logging_specification = project.open_logging_specification_document()
        project.close()
        with pytest.raises(FlexLoggerError):
            logging_specification.get_test_properties()

    @pytest.mark.integration  # type: ignore
    def test__testproperty_repr__returns_correct_string(self) -> None:
        test_property = TestProperty("Property", "New Value", True)
        assert 'flexlogger.automation.TestProperty("Property", "New Value", True)' == repr(
            test_property
        )

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_test_start__start_trigger_is_test_start(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            logging_specification.set_start_trigger_settings_to_test_start()

            start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
            assert start_trigger_condition == StartTriggerCondition.TEST_START
            assert start_trigger_settings is None

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_channel_value_change__start_trigger_is_channel_value_change(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 5.0
            value_change_condition.max_value = 7.0
            value_change_condition.time = 1.0
            logging_specification.set_start_trigger_settings_to_value_change(value_change_condition)

            start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
            assert start_trigger_condition == StartTriggerCondition.CHANNEL_VALUE_CHANGE
            assert start_trigger_settings == value_change_condition

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_channel_value_change_with_invalid_channel__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Invalid Channel'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 5.0
            value_change_condition.max_value = 7.0
            value_change_condition.time = 1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_start_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_channel_value_change_with_invalid_range__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 8.0
            value_change_condition.max_value = 5.0
            value_change_condition.time = 1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_start_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_channel_value_change_with_invalid_time__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 4.0
            value_change_condition.max_value = 5.0
            value_change_condition.time = -1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_start_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_time__start_trigger_is_time(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            start_time = datetime.utcnow()
            start_time = start_time.replace(microsecond=0)
            logging_specification.set_start_trigger_settings_to_absolute_time(start_time)

            start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
            assert start_trigger_condition == StartTriggerCondition.ABSOLUTE_TIME
            expected_time = start_time.replace(tzinfo=tz.tzutc())
            expected_time = expected_time.astimezone(tz.tzlocal())
            assert start_trigger_settings == expected_time

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_elapsed_time__start_trigger_is_elapsed_time(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            elapsed_time = timedelta(seconds=45, milliseconds=500)
            logging_specification.set_start_trigger_settings_to_elapsed_time(elapsed_time)

            start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
            assert start_trigger_condition == StartTriggerCondition.TIME_ELAPSED
            assert start_trigger_settings == elapsed_time

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_start_trigger_button_pressed__start_trigger_is_button_pressed(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            button_name = "Start Button"
            logging_specification.set_start_trigger_settings_to_button_pressed(button_name)

            start_trigger_condition, start_trigger_settings = logging_specification.get_start_trigger_settings()
            assert start_trigger_condition == StartTriggerCondition.BUTTON_PRESSED
            assert start_trigger_settings == button_name

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_test_stop__stop_trigger_is_test_stop(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            logging_specification.set_stop_trigger_settings_to_test_stop()

            stop_trigger_condition, stop_trigger_settings = logging_specification.get_stop_trigger_settings()
            assert stop_trigger_condition == StopTriggerCondition.TEST_STOP
            assert stop_trigger_settings is None

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_channel_value_change__stop_trigger_is_channel_value_change(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 5.0
            value_change_condition.max_value = 7.0
            value_change_condition.time = 1.0
            logging_specification.set_stop_trigger_settings_to_value_change(value_change_condition)

            stop_trigger_condition, stop_trigger_settings = logging_specification.get_stop_trigger_settings()
            assert stop_trigger_condition == StopTriggerCondition.CHANNEL_VALUE_CHANGE
            assert stop_trigger_settings == value_change_condition

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_channel_value_change_with_invalid_channel__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Invalid Channel'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 5.0
            value_change_condition.max_value = 7.0
            value_change_condition.time = 1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_stop_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_channel_value_change_with_invalid_range__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 8.0
            value_change_condition.max_value = 5.0
            value_change_condition.time = 1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_stop_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_channel_value_change_with_invalid_time__exception_raised(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 4.0
            value_change_condition.max_value = 5.0
            value_change_condition.time = -1.0

            with pytest.raises(FlexLoggerError):
                logging_specification.set_stop_trigger_settings_to_value_change(value_change_condition)

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_time__stop_trigger_is_time(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            duration = timedelta(seconds=100)
            logging_specification.set_stop_trigger_settings_to_duration(duration)

            stop_trigger_condition, stop_trigger_settings = logging_specification.get_stop_trigger_settings()
            assert stop_trigger_condition == StopTriggerCondition.TEST_TIME_ELAPSED
            assert stop_trigger_settings == '00:01:40'

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_stop_trigger_button_pressed__stop_trigger_is_button_pressed(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()

            button_name = "Stop Button"
            logging_specification.set_stop_trigger_settings_to_button_pressed(button_name)

            stop_trigger_condition, stop_trigger_settings = logging_specification.get_stop_trigger_settings()
            assert stop_trigger_condition == StopTriggerCondition.BUTTON_PRESSED
            assert stop_trigger_settings == button_name

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_retriggering__re_triggering_is_set(self, app: Application) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()
            value_change_condition = ValueChangeCondition()
            value_change_condition.channel_name = 'Variable'
            value_change_condition.value_change_type = ValueChangeType.ENTER_RANGE
            value_change_condition.min_value = 5.0
            value_change_condition.max_value = 7.0
            value_change_condition.time = 1.0
            logging_specification.set_start_trigger_settings_to_value_change(value_change_condition)
            duration = timedelta(seconds=100)
            logging_specification.set_stop_trigger_settings_to_duration(duration)

            logging_specification.set_retriggering(True)

            re_triggering = logging_specification.is_retriggering_enabled()
            assert re_triggering

    @pytest.mark.integration  # type: ignore
    def test__open_project__set_retriggering__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithLoggingSpecification") as project:
            logging_specification = project.open_logging_specification_document()
            logging_specification.set_start_trigger_settings_to_test_start()

            with pytest.raises(FlexLoggerError):
                logging_specification.set_retriggering(True)

    def assert_property_matches(
        self,
        test_property: TestProperty,
        expected_name: str,
        expected_value: str,
        expected_prompt_on_start: bool,
    ) -> None:
        assert expected_name == test_property.name
        assert expected_value == test_property.value
        assert expected_prompt_on_start == test_property.prompt_on_start
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_project.py sha256=798026330334425dbedee37c5131844cb501b91535083d8daf62bf57f74ddefa bytes=11761 -->
## FILE: tests/test_project.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_project.py`
- sha256: `798026330334425dbedee37c5131844cb501b91535083d8daf62bf57f74ddefa`
- bytes: 11761

````python
from shutil import rmtree
from time import sleep

import os
import pytest  # type: ignore
from flexlogger.automation import Application, FlexLoggerError

from .utils import (
    assert_no_flexloggers_running,
    copy_project,
    get_project_path,
    kill_all_open_flexloggers,
    open_project,
)


class TestProject:
    @pytest.mark.integration  # type: ignore
    def test__launch_flexLogger__open_default_project__project_contains_standard_four_documents(
        self, app: Application
    ) -> None:
        with open_project(app, "DefaultProject") as project:
            assert project is not None
            channel_specification_document = project.open_channel_specification_document()
            assert channel_specification_document is not None
            logging_specification_document = project.open_logging_specification_document()
            assert logging_specification_document is not None
            # Validate screen can be accessed with and without extension
            screen_document = project.open_screen_document("Screen")
            assert screen_document is not None
            screen_document = project.open_screen_document("Screen.flxscr")
            assert screen_document is not None
            test_specification_document = project.open_test_specification_document()
            assert test_specification_document is not None

    @pytest.mark.integration  # type: ignore
    def test__launch_flexLogger__open_missing_screen__raises_exception(
        self, app: Application
    ) -> None:
        with open_project(app, "DefaultProject") as project:
            with pytest.raises(FlexLoggerError):
                project.open_screen_document("Not a Screen")

    # This test can hang if the API doesn't handle this error correctly, so set a
    # timeout
    @pytest.mark.timeout(120)  # type: ignore
    @pytest.mark.integration  # type: ignore
    def test__remove_channel_specification_file__open_project__raises_exception(
        self, app: Application
    ) -> None:
        with copy_project("DefaultProject") as project_path:
            cache_dir = project_path.parent / ".cache"
            if cache_dir.exists():
                rmtree(str(cache_dir))
            (project_path.parent / "Channel Specification.flxio").unlink()
            project = None
            try:
                with pytest.raises(FlexLoggerError):
                    project = app.open_project(project_path)
            finally:
                if project is not None:
                    project.close()

    @pytest.mark.integration  # type: ignore
    def test__launch_flexlogger_and_disconnect__connect_to_existing_and_open_project__is_not_None(
        self,
    ) -> None:
        kill_all_open_flexloggers()
        project_path = get_project_path("DefaultProject")
        server_port = -1
        try:
            with Application.launch() as app:
                server_port = app.server_port
                # This should prevent FlexLogger from closing when app goes out of scope
                app.disconnect()
            with Application(server_port=server_port) as app:
                project = app.open_project(project_path)
                assert project is not None
        finally:
            if server_port != -1:
                Application(server_port=server_port).close()

    @pytest.mark.integration  # type: ignore
    def test__open_project__open_different_project__using_original_project_raises_exception(
        self,
    ) -> None:
        kill_all_open_flexloggers()
        project_path = get_project_path("DefaultProject")
        second_project_path = get_project_path("ProjectWithTestProperties")
        with Application.launch() as app:
            first_project = app.open_project(project_path)
            app.open_project(second_project_path)
            with pytest.raises(FlexLoggerError):
                first_project.open_channel_specification_document()

    @pytest.mark.integration  # type: ignore
    def test__open_project_that_does_not_exist__raises_exception(self) -> None:
        kill_all_open_flexloggers()
        project_path = get_project_path("DoesNotExist")
        with Application.launch() as app:
            with pytest.raises(FlexLoggerError):
                app.open_project(project_path)

    @pytest.mark.integration  # type: ignore
    def test__open_project__close_project__using_original_project_raises_exception(self) -> None:
        kill_all_open_flexloggers()
        project_path = get_project_path("DefaultProject")
        with Application.launch() as app:
            first_project = app.open_project(project_path)
            first_project.close()
            with pytest.raises(FlexLoggerError):
                first_project.open_channel_specification_document()

    @pytest.mark.integration  # type: ignore
    def test__launch_application__close_application__using_application_raises_exception(
        self,
    ) -> None:
        kill_all_open_flexloggers()
        app = Application.launch()
        app.close()
        with pytest.raises(FlexLoggerError):
            app.open_project(get_project_path("DefaultProject"))

    @pytest.mark.integration  # type: ignore
    def test__disconnect_application__using_application_raises_exception(self) -> None:
        kill_all_open_flexloggers()
        original_app = Application.launch()
        try:
            new_app = Application(server_port=original_app.server_port)
            new_app.disconnect()
            with pytest.raises(FlexLoggerError):
                new_app.open_project(get_project_path("DefaultProject"))
        finally:
            original_app.close()

    @pytest.mark.integration  # type: ignore
    def test__open_project__close_application__using_project_raises_exception(self) -> None:
        kill_all_open_flexloggers()
        app = Application.launch()
        project = app.open_project(get_project_path("DefaultProject"))
        app.close()
        with pytest.raises(FlexLoggerError):
            project.open_channel_specification_document()

    @pytest.mark.integration  # type: ignore
    def test__launch_application__launch_application_again__raises_exception(self) -> None:
        kill_all_open_flexloggers()
        with Application.launch():
            # We expect this to fail because we don't support multiple instances of FlexLogger
            # running at the same time.
            new_app = None
            try:
                with pytest.raises(RuntimeError):
                    new_app = Application.launch(timeout=20)
            finally:
                # if the test fails, try not to mess up future tests
                if new_app is not None:
                    new_app.close()

    @pytest.mark.integration  # type: ignore
    def test__launch_application__close_application__application_has_closed(self) -> None:
        kill_all_open_flexloggers()

        with Application.launch() as app:
            # Opening a project will make closing the application take longer
            app.open_project(get_project_path("DefaultProject"))

        assert_no_flexloggers_running()

    @pytest.mark.integration  # type: ignore
    def test__connect_to_application__close_application__application_has_closed(self) -> None:
        kill_all_open_flexloggers()
        app = Application.launch()
        # Opening a project will make closing the application take longer
        app.open_project(get_project_path("DefaultProject"))

        app2 = Application(app.server_port)
        app2.close()

        assert_no_flexloggers_running()

    @pytest.mark.integration  # type: ignore
    def test__launch_application__active_project_is_none(self) -> None:
        kill_all_open_flexloggers()
        with Application.launch() as app:
            active_project = app.get_active_project()
            assert active_project is None

    @pytest.mark.integration  # type: ignore
    def test__launch_application__open_and_close_project__active_project_is_none(self) -> None:
        kill_all_open_flexloggers()
        with Application.launch() as app:
            project = app.open_project(get_project_path("DefaultProject"))
            project.close()
            active_project = app.get_active_project()
            assert active_project is None

    @pytest.mark.integration  # type: ignore
    def test__launch_application__open_project__active_project_matches_open_project(self) -> None:
        kill_all_open_flexloggers()
        with Application.launch() as app:
            project = app.open_project(get_project_path("DefaultProject"))
            active_project = app.get_active_project()
            assert active_project is not None
            assert project._identifier == active_project._identifier

    # This test can hang if the server port file never gets created, so set a
    # timeout
    @pytest.mark.timeout(120)  # type: ignore
    @pytest.mark.integration  # type: ignore
    def test__launch_flexlogger_separately__connect_to_existing_and_close__application_has_closed(
        self,
    ) -> None:
        kill_all_open_flexloggers()
        # Launch the way that Application.launch() does, but don't connect
        real_server_port = Application._launch_flexlogger(60)
        # The port file doesn't get written out until slightly after the mapped file
        # that _launch_flexlogger() is waiting for.
        # So wait for the file to exist before proceeding with the test.
        server_port_file_path = Application._get_server_port_file_path()
        while not server_port_file_path.exists():
            sleep(1)

        app = Application()
        assert real_server_port == app.server_port
        app.close()

        assert_no_flexloggers_running()

    # This test can hang if the application pops a "save changes" dialog box, so set a
    # timeout
    @pytest.mark.timeout(120)  # type: ignore
    @pytest.mark.integration  # type: ignore
    def test__make_change_to_project__close_application__no_save_dialog_box(self) -> None:
        kill_all_open_flexloggers()
        with copy_project("ProjectWithProducedData") as new_project_path:
            with Application.launch() as app:
                project = app.open_project(new_project_path)
                logging_specification = project.open_logging_specification_document()
                logging_specification.set_log_file_name("SomeNewName")
        # Just verify that closing the app doesn't prompt to save the project (this test
        # will timeout if it does)

    @pytest.mark.integration
    def test__open_project__active_project_path_matches_loaded_path(self) -> None:
        with copy_project("DefaultProject") as new_project_path:
            with Application.launch() as app:
                project = app.open_project(new_project_path)
                assert project.project_file_path == new_project_path

    @pytest.mark.integration  # type: ignore
    def test__open_default_project__save__no_error(self, app: Application) -> None:
        with open_project(app, "DefaultProject") as project:
            project.save()

    @pytest.mark.integration # type: ignore
    def test_open_default_project__saveas__no_error(self, app: Application) -> None:
        with open_project(app, "DefaultProject") as project:
            project.saveas("TestProjectSaveAs", "C:\\temp")
            assert os.path.exists("C:\\temp\\TestProjectSaveAs\\TestProjectSaveAs.flxproj")
        app.close()
        rmtree("C:\\temp\\TestProjectSaveAs")
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/test_test_session.py sha256=929188053d4a6d61e02cec009445c7a6ea5772ed5e536a6c7cc071c3a09b3f67 bytes=15688 -->
## FILE: tests/test_test_session.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/test_test_session.py`
- sha256: `929188053d4a6d61e02cec009445c7a6ea5772ed5e536a6c7cc071c3a09b3f67`
- bytes: 15688

````python
import os
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator

import pytest  # type: ignore
from flexlogger.automation import (
    Application,
    FlexLoggerError,
    Project,
    TestSessionState,
)
from nptdms import TdmsFile  # type: ignore

from .utils import (
    copy_project,
    get_project_path,
    kill_all_open_flexloggers,
    open_project,
)


@pytest.fixture(scope="class")
def project_with_produced_data(app: Application) -> Iterator[Project]:
    """Fixture for opening ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    """
    with copy_project("ProjectWithProducedData") as project_path:
        project = app.open_project(project_path)
        yield project
        try:
            project.close()
        except FlexLoggerError:
            # utils.kill_all_open_flexloggers may have killed this process already, that's fine
            pass


class TestTestSession:
    @pytest.mark.integration  # type: ignore
    @pytest.mark.parametrize(
        "project_name,expected_state",
        [
            ("DefaultProject", TestSessionState.NO_VALID_LOGGED_CHANNELS),
            ("ProjectWithError", TestSessionState.INVALID_CONFIGURATION),
            ("ProjectWithProducedData", TestSessionState.IDLE),
        ],
    )  # type: ignore
    def test__open_project__get_test_session_state__state_matches_project(
        self, project_name: str, expected_state: TestSessionState, app: Application
    ) -> None:
        with open_project(app, project_name) as project:
            assert expected_state == project.test_session.state

    @pytest.mark.integration  # type: ignore
    @pytest.mark.parametrize("project_name", ["DefaultProject", "ProjectWithError"])  # type: ignore
    def test__open_project_that_cannot_be_started__start_test_session__exception_raised(
        self, project_name: str, app: Application
    ) -> None:
        with open_project(app, project_name) as project:
            with pytest.raises(FlexLoggerError):
                project.test_session.start()

    @pytest.mark.integration  # type: ignore
    def test__open_valid_project__start_test_session__test_session_started(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        test_session_started = project.test_session.start()
        try:
            assert test_session_started is True
            assert TestSessionState.RUNNING == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__start_test_session__test_session_remained_started(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        try:
            started_again = project.test_session.start()

            assert started_again is False
            assert TestSessionState.RUNNING == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_idle__stop_test_session__test_session_not_stopped(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        stopped = project.test_session.stop()

        assert stopped is False
        assert TestSessionState.IDLE == project.test_session.state

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__stop_test_session__test_session_stopped(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()

        stopped = project.test_session.stop()

        assert stopped is True
        assert TestSessionState.IDLE == project.test_session.state

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__pause_test_session__test_session_paused(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        test_session_paused = project.test_session.pause()
        try:
            assert test_session_paused is True
            assert TestSessionState.PAUSED == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_paused__resume_test_session__test_session_resumes(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        project.test_session.pause()
        test_session_resumed = project.test_session.resume()
        try:
            assert test_session_resumed is True
            assert TestSessionState.RUNNING == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_paused__pause_test_session__test_session_remains_paused(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        project.test_session.pause()
        test_session_paused = project.test_session.pause()
        try:
            assert test_session_paused is False
            assert TestSessionState.PAUSED == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__resume_test_session__test_session_remains_running(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        test_session_resumed = project.test_session.resume()
        try:
            assert test_session_resumed is False
            assert TestSessionState.RUNNING == project.test_session.state
        finally:
            project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_paused__stop_test_session__test_session_stopped(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        project.test_session.pause()

        stopped = project.test_session.stop()

        assert stopped is True
        assert TestSessionState.IDLE == project.test_session.state

    @pytest.mark.integration  # type: ignore
    def test__open_valid_project__pause_test_session__exception_raised(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        with pytest.raises(FlexLoggerError):
            project_with_produced_data.test_session.pause()

    @pytest.mark.integration  # type: ignore
    def test__open_valid_project__resume_test_session__exception_raised(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        with pytest.raises(FlexLoggerError):
            project_with_produced_data.test_session.resume()

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__add_note__note_added(self, app: Application) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            logging_specification = project.open_logging_specification_document()
            with TemporaryDirectory() as temp_dir:
                logging_specification.set_log_file_base_path(temp_dir)
                logging_specification.set_log_file_name("AddNoteTest.tdms")
                project.test_session.start()

                note_str = "Some note about what is happening in the test"
                project.test_session.add_note(note_str)

                project.test_session.stop()
                self._verify_tdms_file_has_note(temp_dir, "AddNoteTest.tdms", note_str)

    @pytest.mark.integration  # type: ignore
    def test__test_session_paused__add_note__note_added(self, app: Application) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            logging_specification = project.open_logging_specification_document()
            with TemporaryDirectory() as temp_dir:
                logging_specification.set_log_file_base_path(temp_dir)
                logging_specification.set_log_file_name("AddNoteTest.tdms")
                project.test_session.start()
                project.test_session.pause()

                note_str = "Some note about what is happening in the test"
                project.test_session.add_note(note_str)

                project.test_session.stop()
                self._verify_tdms_file_has_note(temp_dir, "AddNoteTest.tdms", note_str)

    @staticmethod
    def _verify_tdms_file_has_note(
        log_file_base_path: str, log_file_name: str, expected_note_contents: str
    ) -> None:
        log_file_path = Path(log_file_base_path) / log_file_name
        with TdmsFile.open(str(log_file_path)) as tdms_file:
            user_notes_group = tdms_file["Test Information"]
            user_notes_channel = user_notes_group["User Notes"]
            assert user_notes_channel is not None
            user_notes_time_channel = user_notes_group["User Notes_time"]
            assert user_notes_time_channel is not None
            assert 1 == len(user_notes_channel)
            assert expected_note_contents == user_notes_channel[0]

    @pytest.mark.integration  # type: ignore
    def test__test_session_idle__add_note__exception_raised(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        with pytest.raises(FlexLoggerError):
            project_with_produced_data.test_session.add_note("Nope")

    @pytest.mark.integration  # type: ignore
    def test__close_project__start_test__exception_raised(self, app: Application) -> None:
        project = app.open_project(get_project_path("ProjectWithProducedData"))
        project.close()
        with pytest.raises(FlexLoggerError):
            project.test_session.start()

    @pytest.mark.integration  # type: ignore
    def test__add_prompt_on_start_property__start_test__app_pops_dialog(self) -> None:
        # We are testing that if a property is "prompt on start" then FlexLogger should
        # pop up the dialog to set that property when we start a test.
        # This is tricky to test because this means the call to test_session.start() will
        # hang waiting for the dialog to finish.  This is as intended.
        #
        # Since we need to kill the call after we're done, it's safer to run this in a separate
        # process, and we keep track of the results in this test.
        with TemporaryDirectory() as temp_dir:
            script_path = (
                Path(os.path.dirname(os.path.realpath(__file__))) / "start_test_separate_process.py"
            )

            with copy_project("ProjectWithProducedData") as new_project_path:
                process = None
                try:
                    process = subprocess.Popen(
                        [sys.executable, str(script_path), str(new_project_path), str(temp_dir)]
                    )
                    # We need to allow time for FlexLogger to launch and the project to open,
                    # so make sure this timeout is relatively high.
                    end_timeout_time = time.time() + 40
                    while time.time() < end_timeout_time:
                        # process.poll() will return a number if the process has exited
                        assert process.poll() is None
                    # Make sure the test hasn't started (so we haven't written any data)
                    assert (Path(temp_dir) / "ShouldNotExist.tdms").exists() is False
                finally:
                    kill_all_open_flexloggers()
                    if process is not None:
                        process.kill()


class TestTestSessionElapsedTime:
    @pytest.mark.integration  # type: ignore
    def test__test_session_idle__query_elapsed_time__exception_raised(
        self, app: Application
    ) -> None:
        with open_project(app, "ProjectWithProducedData") as project:
            with pytest.raises(FlexLoggerError):
                project.test_session.elapsed_test_time

    @pytest.mark.integration  # type: ignore
    def test__test_session_running__elapsed_time_increases(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()

        time.sleep(0.25)
        first_elapsed_time = project.test_session.elapsed_test_time
        assert first_elapsed_time.total_seconds() > 0
        time.sleep(0.25)
        second_elapsed_time = project.test_session.elapsed_test_time
        assert second_elapsed_time > first_elapsed_time

    @pytest.mark.integration  # type: ignore
    def test__test_session_paused__elapsed_time_pauses(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        time.sleep(0.25)
        elapsed_time_before_pause = project.test_session.elapsed_test_time
        assert elapsed_time_before_pause.total_seconds() > 0
        project.test_session.pause()

        time.sleep(0.25)
        first_elapsed_time_after_pause = project.test_session.elapsed_test_time
        assert first_elapsed_time_after_pause > elapsed_time_before_pause
        time.sleep(0.25)
        second_elapsed_time_after_pause = project.test_session.elapsed_test_time
        assert second_elapsed_time_after_pause == first_elapsed_time_after_pause
        project.test_session.stop()

    @pytest.mark.integration  # type: ignore
    def test__test_session_stopped__elapsed_time_returns_previous_test_session_elapsed_time(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        time.sleep(0.25)
        elapsed_time_before_stop = project.test_session.elapsed_test_time
        assert elapsed_time_before_stop.total_seconds() > 0
        time.sleep(0.25)
        project.test_session.stop()

        time.sleep(0.25)
        elapsed_time_after_stop = project.test_session.elapsed_test_time
        assert elapsed_time_after_stop > elapsed_time_before_stop

    @pytest.mark.integration  # type: ignore
    def test__test_session_stopped__start_new_test__elapsed_time_resets(
        self, app: Application, project_with_produced_data: Project
    ) -> None:
        project = project_with_produced_data
        project.test_session.start()
        time.sleep(2.0)
        project.test_session.stop()
        first_test_session_time = project.test_session.elapsed_test_time

        project.test_session.start()
        second_test_session_time = project.test_session.elapsed_test_time
        assert second_test_session_time < first_test_session_time
        project.test_session.stop()
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tests/utils.py sha256=ea583c4bfc12b704691d7c300a6082cd220046aa7a48c67e0613fc8fab96624f bytes=3941 -->
## FILE: tests/utils.py

- repository: `ni/niflexlogger-automation-python`
- source_path: `tests/utils.py`
- sha256: `ea583c4bfc12b704691d7c300a6082cd220046aa7a48c67e0613fc8fab96624f`
- bytes: 3941

````python
import os
import signal
from contextlib import contextmanager
from pathlib import Path
from shutil import copy
from tempfile import TemporaryDirectory
from typing import Iterator, List, Tuple

import psutil  # type: ignore
from flexlogger.automation import Application, Project


def get_project_path(project_name: str) -> Path:
    """Get the assets project path for the given project name (with no ".flxproj").

    If you want to open the project, please use open_project() or copy_project() instead,
    as they will copy the project to a temporary directory and clean it up afterwards.
    """
    return Path(__file__).parent / ("assets/%s/%s.flxproj" % (project_name, project_name))


def kill_all_open_flexloggers() -> None:
    """Kill all open FlexLogger.exe processes.

    The application fixture in conftest.py does not get closed until all tests
    are run, which means tests that don't use the fixture will fail because we
    won't be able to launch a new Application.  So every test that doesn't use the
    fixture needs to call this method first.
    """
    for proc in psutil.process_iter(["pid", "name"]):
        if proc.info["name"].lower() == "flexlogger.exe":
            _kill_proc_tree(proc.info["pid"])
    assert_no_flexloggers_running()


def assert_no_flexloggers_running() -> None:
    """Assert that no FlexLogger.exe processes are running."""
    assert not any_flexloggers_running()


def any_flexloggers_running() -> bool:
    """Returns whether any FlexLogger.exe processes are running."""
    for proc in psutil.process_iter(["pid", "name"]):
        if proc.info["name"].lower() == "flexlogger.exe":
            return True
    return False


@contextmanager
def open_project(application: Application, project_name: str) -> Iterator[Project]:
    """Copy the project with name project_name in the assets directory to a temp directory and open it.

    This function returns a ContextManager, so it should be used in a `with` statement,
    and when it goes out of scope it will close the project and delete the temporary directory.
    """
    with copy_project(project_name) as project_path:
        project = application.open_project(project_path)
        try:
            yield project
        finally:
            project.close()


@contextmanager
def copy_project(project_name: str) -> Iterator[Path]:
    """Copy a project with name project_name from the assets directory to a temp directory.

    This function returns a ContextManager, so it should be used in a `with` statement,
    and when it goes out of scope it will delete the temporary directory.

    Returns:
        The new project's path.
    """
    project_path = get_project_path(project_name)
    project_filename = project_path.name
    project_dir = project_path.parent

    # This directory gets cleaned up by the pytest framework, and if
    # we try to clean it up ourselves we can get pytest warnings when
    # the framework fails to delete it.
    tmp_directory = TemporaryDirectory(prefix="pyflextest_")
    source_files = project_dir.iterdir()
    for source_file in source_files:
        if source_file.is_file():
            copy(str(source_file), tmp_directory.name)
    yield Path(tmp_directory.name) / project_filename


def _kill_proc_tree(
    pid: int, sig: int = signal.SIGTERM, include_parent: bool = True, timeout: float = None
) -> Tuple[List, List]:
    """Kill a process tree (including grandchildren).

    Uses signal "sig" and returns a (gone, still_alive) tuple.
    """
    assert pid != os.getpid(), "won't kill myself"
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout)
    return (gone, alive)
````

<!--NI_OSS_SOURCE repo=niflexlogger-automation-python path=tox.ini sha256=b87c6edec827b29c70cd4d0ccdf16c95c8eaa71358188e1b63c7d8c96465b39f bytes=2613 -->
## FILE: tox.ini

- repository: `ni/niflexlogger-automation-python`
- source_path: `tox.ini`
- sha256: `b87c6edec827b29c70cd4d0ccdf16c95c8eaa71358188e1b63c7d8c96465b39f`
- bytes: 2613

````ini
# tox (https://tox.readthedocs.io/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = py313,py312,py311,py310,py39,py38,py37,py36
requires =
    setuptools >= 40.1.0

[testenv]
deps =
    py313: black
    py313: docutils
    py313: flake8
    py313: flake8-docstrings
    py313: flake8-import-order
    mypy
    pytest
    npTDMS
    pytest-timeout
    psutil
changedir = src
commands =
    py313: black --target-version py36 --exclude "flexlogger\/automation\/proto\/" --check flexlogger ../examples ../tests
    py313: flake8 flexlogger ../examples/Basic ../examples/Interactive ../tests
    py313: mypy --config-file ../mypy.ini -p flexlogger.automation
    # We don't annotate types in our examples (to make them easier to read),
    # but do check that we're using types correctly
    py313: mypy --config-file ../mypy.ini --allow-untyped-defs --allow-incomplete-defs ../examples/Basic ../examples/Interactive
    py313: mypy --config-file ../mypy.ini ../tests
    pytest --doctest-modules flexlogger
    pytest ../tests --strict-markers {posargs:-m "(not slow)"}
# WINDIR environment variable needs to be set or FlexLogger
# crashes on launch with a UriFormatException from
# MS.Internal.FontCache.Util..cctor()
passenv =
    WINDIR

[gh-actions]
python =
   3.6: py36
   3.7: py37
   3.8: py38
   3.9: py39
   3.10: py310
   3.11: py311
   3.12: py312
   3.13: py313

# Note that pytest args can be passed on the commandline after "--", e.g.
#    tox -- -m integration
# to run all integration tests. (The list of available markers is below.)
#
# The default pytest args used above say to *not* run tests marked as slow.
# If you specifically want to run *all* tests, then you must pass *some*
# argument after "--". An easy way to do this is just repeat the --strict flag:
#    tox -- --strict

[pytest]
markers =
    unit: mark a test as a unit test
    integration: mark a test as an integration test
    slow: mark a test as a slow test


[testenv:docs]
description = invoke sphinx-build to build the HTML docs
basepython = python3
deps =
    -rdocs/requirements.txt
commands =
    sphinx-build -a -E -c ../docs -d "{toxworkdir}/docs_doctree" ../docs "{toxworkdir}/docs_out" --color -W -bhtml {posargs}
    python -c 'import pathlib; print("documentation available under file://\{0\}".format(pathlib.Path(r"{toxworkdir}") / "docs_out" / "index.html"))'
````
