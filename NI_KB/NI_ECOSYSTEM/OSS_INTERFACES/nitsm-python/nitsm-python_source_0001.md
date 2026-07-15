# NI OSS SOURCE SNAPSHOT: nitsm-python

<!--NI_OSS_SNAPSHOT repo=ni/nitsm-python commit=334552e02b324bf5663e96a4fc31399570c3138a -->

<!--NI_OSS_SOURCE repo=nitsm-python path=.coveragerc sha256=4fb5ac70ae296970bf44c5c744f1e721f0153d50687568b57202da9d8b7938fc bytes=246 -->
## FILE: .coveragerc

- repository: `ni/nitsm-python`
- source_path: `.coveragerc`
- sha256: `4fb5ac70ae296970bf44c5c744f1e721f0153d50687568b57202da9d8b7938fc`
- bytes: 246

````text
[run]
source_pkgs = nitsm
omit =
    */nitsm/_pinmapinterfaces.py
    */nitsm/__init__.py
    */nitsm/debug.py

[paths]
tox =
    src/nitsm/
    */nitsm/

[report]
exclude_lines =
    pragma: no cover
    if typing.TYPE_CHECKING:
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/actions/build/action.yml sha256=9991f941e72604f682d5e4eba068a81f91b54dd396ddabc26965bc1440d8ef28 bytes=261 -->
## FILE: .github/actions/build/action.yml

- repository: `ni/nitsm-python`
- source_path: `.github/actions/build/action.yml`
- sha256: `9991f941e72604f682d5e4eba068a81f91b54dd396ddabc26965bc1440d8ef28`
- bytes: 261

````yaml
name: Build Package

runs:
  using: composite

  steps:
  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install build
    shell: bash

  - name: Build package
    run: python -m build
    shell: bash
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=10e5f768a6212ab91b4091bfb4f3c488d6d934e1ac69b74172ccf418ae0dd28f bytes=717 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nitsm-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `10e5f768a6212ab91b4091bfb4f3c488d6d934e1ac69b74172ccf418ae0dd28f`
- bytes: 717

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nitsm-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/tsm-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.

- [ ] I have run the automated tests (required if there are code changes)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/workflows/lint.yml sha256=17e2936695a000743b6ccb8652ae30b15eb9fc707ad793d49436b94bbde718b7 bytes=938 -->
## FILE: .github/workflows/lint.yml

- repository: `ni/nitsm-python`
- source_path: `.github/workflows/lint.yml`
- sha256: `17e2936695a000743b6ccb8652ae30b15eb9fc707ad793d49436b94bbde718b7`
- bytes: 938

````yaml
# Checks pull request for proper code formatting and style
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Lint

on:
  pull_request:
    branches:
      - main

jobs:
  lint:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Upgrade pip
      run: |
        python -m pip install --upgrade pip

    - name: Check code formatting with black
      run: |
        python -m pip install --upgrade black
        python -m black --check .

    - name: Lint with NI style guide
      run: |
        python -m pip install --upgrade ni-python-styleguide
        python -m ni_python_styleguide lint --extend-ignore=D203,D204,D205,D213,D215,D400,D401,D404,D406,D407,D408,D409,D413,D415 src
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/workflows/publish-pypi.yml sha256=39ce6af18990256f64f7f69c50a4e8002864e4f3920dc8c5633528efb60eaeae bytes=455 -->
## FILE: .github/workflows/publish-pypi.yml

- repository: `ni/nitsm-python`
- source_path: `.github/workflows/publish-pypi.yml`
- sha256: `39ce6af18990256f64f7f69c50a4e8002864e4f3920dc8c5633528efb60eaeae`
- bytes: 455

````yaml
name: Publish Package to PyPI

on: workflow_dispatch

jobs:
  deploy:

    runs-on: ubuntu-latest

    permissions:
      id-token: write

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.x"

    - name: Build package
      uses: ./.github/actions/build

    - name: Publish package
      uses: pypa/gh-action-pypi-publish@release/v1
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/workflows/publish-testpypi.yml sha256=9a90f001a1bf85b81bd0778f136c04fc5d17b69483063f3f06afa25dc76aeab6 bytes=527 -->
## FILE: .github/workflows/publish-testpypi.yml

- repository: `ni/nitsm-python`
- source_path: `.github/workflows/publish-testpypi.yml`
- sha256: `9a90f001a1bf85b81bd0778f136c04fc5d17b69483063f3f06afa25dc76aeab6`
- bytes: 527

````yaml
name: Publish Package to TestPyPI

on: workflow_dispatch

jobs:
  deploy:

    runs-on: ubuntu-latest

    permissions:
      id-token: write

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.x"

    - name: Build package
      uses: ./.github/actions/build

    - name: Publish package
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.github/workflows/test-build-install.yml sha256=069bd3cf32b6f97cc5a5e7da63f90fb83f0b5ac35ff44a9b3eb3e97ddbee6d29 bytes=545 -->
## FILE: .github/workflows/test-build-install.yml

- repository: `ni/nitsm-python`
- source_path: `.github/workflows/test-build-install.yml`
- sha256: `069bd3cf32b6f97cc5a5e7da63f90fb83f0b5ac35ff44a9b3eb3e97ddbee6d29`
- bytes: 545

````yaml
name: Test Build and Install Package

on:
  pull_request:
    branches:
      - main

jobs:
  build-install:

    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Build package
      uses: ./.github/actions/build

    - name: Install package
      run: |
        pip install pywin32  # install from pypi
        pip install nitsm --no-index -f dist/  # install local distribution
````

<!--NI_OSS_SOURCE repo=nitsm-python path=.gitignore sha256=74d72391daadee7f12438f02928a274f29a79b113879ae5c35083e564f7356d7 bytes=521 -->
## FILE: .gitignore

- repository: `ni/nitsm-python`
- source_path: `.gitignore`
- sha256: `74d72391daadee7f12438f02928a274f29a79b113879ae5c35083e564f7356d7`
- bytes: 521

````text
# PyCharm
.idea/

# Python
__pycache__/
*.pyc
.venv/
venv/

# pytest
.pytest_cache/
*-results.xml

# build
dist/
*.egg-info

# tox
.tox/

# coverage
*.coverage*
coverage.xml

# Digital Pattern Editor
*.digiprojcache

# TestStand Reports
systemtests/*BatchReport*.xml
systemtests/*.html
systemtests/*.xml

# TSM Reports. Example: File_10Sep2020_1030_Site1.txt
systemtests/*_[0-9][0-9]???202[0-9]_*.csv
systemtests/*_[0-9][0-9]???202[0-9]_*.std
systemtests/*_[0-9][0-9]???202[0-9]_*.txt
````

<!--NI_OSS_SOURCE repo=nitsm-python path=azure-pipelines.yml sha256=e0d8bfa97630c61bba041a61ae0a56483187f0f2e808941f50d80402677ee9db bytes=1476 -->
## FILE: azure-pipelines.yml

- repository: `ni/nitsm-python`
- source_path: `azure-pipelines.yml`
- sha256: `e0d8bfa97630c61bba041a61ae0a56483187f0f2e808941f50d80402677ee9db`
- bytes: 1476

````yaml

trigger:
- main

pr:
  branches:
    include:
    - main

jobs:
- job: CI
  workspace:
    clean: all
    
  pool:
    name: nitsm-python-test

  steps:
  - script: |
      python -m pip install --upgrade pip
    displayName: 'Upgrade pip'

  - script: |
      python -m pip install --upgrade "tox<4" "virtualenv<20.22"
    displayName: 'Install or upgrade tox'

  - task: PowerShell@2
    displayName: 'Switch to old TestStand/TSM'
    inputs:
      targetType: filePath
      filePath: 'C:\Activate_TSVersion.ps1'
      arguments: '-VersionToActivate old'

  - script: |
      python -m tox -- older
    displayName: 'Run python unit tests with older version of TestStand/TSM'

  - task: PowerShell@2
    displayName: 'Switch to new TestStand/TSM'
    inputs:
      targetType: filePath
      filePath: 'C:\Activate_TSVersion.ps1'
      arguments: '-VersionToActivate new'

  - script: |
      python -m tox -- newer
    displayName: 'Run python unit tests with newer version of TestStand/TSM'

  - task: PublishTestResults@2
    condition: succeededOrFailed()
    inputs:
      testResultsFiles: '**/*-results.xml'
      testRunTitle: 'Publish test results'
    displayName: 'Display test results'

  - task: PublishCodeCoverageResults@1
    inputs:
      codeCoverageTool: Cobertura
      summaryFileLocation: '$(System.DefaultWorkingDirectory)/**/coverage.xml'
    displayName: 'Display code coverage results'
````

<!--NI_OSS_SOURCE repo=nitsm-python path=CONTRIBUTING.md sha256=8d467a897fa2c08b4820b46b7cf27dd5ac66facfc53576cf28988d1e388be297 bytes=5684 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nitsm-python`
- source_path: `CONTRIBUTING.md`
- sha256: `8d467a897fa2c08b4820b46b7cf27dd5ac66facfc53576cf28988d1e388be297`
- bytes: 5684

````markdown
Contributing to nitsm-python
===========================

Contributions to [nitsm-python](https://github.com/ni/nitsm-python) are welcome from all!

nitsm-python is managed via [Git](https://git-scm.com), with the canonical upstream repository hosted on
[GitHub](https://github.com/ni/nitsm-python).

nitsm-python follows a pull request model for development. If you wish to contribute, you will need to create a GitHub
account, fork this project, push a branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

## Environment Setup
Before beginning development, it is recommended to install the following dependencies:
* [TestStand 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
* [TestStand Semiconductor Module 20.0+](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
* NI instrument drivers:
  - [NI-DCPower 20.6+](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dcpower.html)
  - [NI-DMM](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html)
  - [NI-SCOPE](https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html)
  - [NI-Digital](https://www.ni.com/en-us/support/downloads/drivers/download.ni-digital-pattern-driver.html)
  - [NI-SWITCH](https://www.ni.com/en-us/support/downloads/drivers/download.ni-switch.html)
  - [NI-DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html)
  - [NI-FGEN](https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html)
* Python packages:
```
pip install -r requirements.txt
```

## Code Formatting
nitsm-python uses [black](https://black.readthedocs.io/en/stable/index.html) for formatting. To format the entire
project, run:
```
black .
```

## Linting
nitsm-python uses [ni-python-styleguide](https://github.com/ni/python-styleguide) for linting. To lint the entire
project, run:
```
ni-python-styleguide lint
```

## Testing
Executing nitsm-python tests in the [tests/](https://github.com/ni/nitsm-python/tree/main/tests) directory requires the
**TSM Standalone Semiconductor Module Context**. If you are an NI employee, contact one of the repository owners to
determine how to obtain a copy of this non-public component. If you are not an NI employee, hang tight! We are currently
working on a process to enable external contributors to use this tool. Note that this does not apply to tests in the
[systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests) directory.

nitsm uses [pytest](https://docs.pytest.org/) to run tests. First, install nitsm in edit mode:
```
pip install -e .
```
Then, run pytest:
```
pytest
```

Running pytest without arguments will run all tests in the [tests/](https://github.com/ni/nitsm-python/tree/main/tests)
directory. To include system tests, include the [systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests)
directory.
```
pytest tests systemtests
```

[tox](https://tox.readthedocs.io/en/latest/) is used to run tests against multiple versions of python. To test against
all environments, run:
```
tox
```

The tox configuration in [pyproject.toml](https://github.com/ni/nitsm-python/blob/main/pyproject.toml) creates
environments for running pytest in [tests/](https://github.com/ni/nitsm-python/tree/main/tests) and
[systemtests/](https://github.com/ni/nitsm-python/tree/main/systemtests). It also defines two additional environments,
`clean` and `report` for cleaning and creating report files respectively. To specify a subset of tox environments, run
tox with the `-e` flag followed by a comma separated list of environments:
```
tox -e clean,py36-tests,py36-sysytemtests,report
```

## Building
To build nitsm-python, you will first need to install [build](https://pypi.org/project/build/):
```
pip install build
```
Next, build the project:
```
python -m build
```
If the build succeeds, artifacts will be placed in `dist/`.

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

See [LICENSE](https://github.com/ni/nitsm-python/blob/master/LICENSE) for details about how
[nitsm-python](https://github.com/ni/nitsm-python) is licensed.
````

<!--NI_OSS_SOURCE repo=nitsm-python path=LICENSE sha256=c46f918d4dbc56cf4b59796538fa233061e0175c5e49b9413aca9666fcb5e4ea bytes=1080 -->
## FILE: LICENSE

- repository: `ni/nitsm-python`
- source_path: `LICENSE`
- sha256: `c46f918d4dbc56cf4b59796538fa233061e0175c5e49b9413aca9666fcb5e4ea`
- bytes: 1080

````text
MIT License

Copyright (c) 2021 NI

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

<!--NI_OSS_SOURCE repo=nitsm-python path=pyproject.toml sha256=b93ce43e37090aacc1fee0919178b821bc82c9ba5620b5944222b437f4d89e33 bytes=1774 -->
## FILE: pyproject.toml

- repository: `ni/nitsm-python`
- source_path: `pyproject.toml`
- sha256: `b93ce43e37090aacc1fee0919178b821bc82c9ba5620b5944222b437f4d89e33`
- bytes: 1774

````toml
[tool.black]
line-length = 100
target-version = ["py36", "py37", "py38", "py311"]
extend-exclude = "^/src/nitsm/_pinmapinterfaces.py"

[tool.ni-python-styleguide]
extend_exclude = "src/nitsm/_pinmapinterfaces.py"
# ignore codes not relevant to the Google docstring conventions (http://www.pydocstyle.org/en/stable/error_codes.html#default-conventions)
# also ignore D415 which requires docstrings to start with a one line summary
extend_ignore = "D203,D204,D205,D213,D215,D400,D401,D404,D406,D407,D408,D409,D413,D415"  # must also be passed via the command line until https://github.com/ni/python-styleguide/issues/76 is resolved

[tool.pytest.ini_options]
testpaths = [
    "tests"
]
markers = [
    "pin_map",
    "sequence_file",
    "offline_mode"
]

[tool.tox]
legacy_tox_ini = """
[tox]
isolated_build = True
envlist = clean, py3{6,7,8,11}-tests, py3{6,7,8,11}-systemtests, report

[testenv]
deps =
    pytest
    pytest-cov
    nidcpower
    nidmm
    niscope
    nidigital
    niswitch
    nidaqmx
    nifgen
commands =
    tests: pytest tests --junitxml={envname}-{posargs:any}-tsm-version-results.xml --cov --cov-report=term
    systemtests: pytest systemtests --junitxml={envname}-{posargs:any}-tsm-version-results.xml --cov --cov-report=term
passenv =
    systemtests: TestStandPublic64 ProgramFiles(x86)
setenv =
    tests,systemtests: COVERAGE_FILE = .coverage.{envname}-{posargs:any}-tsm-version

[testenv:clean]
deps = coverage
skip_install = true
commands = coverage erase

[testenv:report]
deps = coverage
skip_install = true
commands =
    coverage combine
    coverage report -m
    coverage xml
"""

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=README.md sha256=15f0a4ec1b8f9cf844b2a2d35446c439d0b67a8580fb6ba458a9890d746c44d8 bytes=3235 -->
## FILE: README.md

- repository: `ni/nitsm-python`
- source_path: `README.md`
- sha256: `15f0a4ec1b8f9cf844b2a2d35446c439d0b67a8580fb6ba458a9890d746c44d8`
- bytes: 3235

````markdown
[![Build Status](https://ni.visualstudio.com/DevCentral/_apis/build/status/TSM/nitsm-python-tests?branchName=main)](https://ni.visualstudio.com/DevCentral/_build/latest?definitionId=5945&branchName=main)
# nitsm-python
Write code modules with the TestStand Semiconductor Module in python.

## Note to End Users
This project is intended for use in automated device validation. Our primary focus is to provide a pythonic approach to
automated testing with TestStand and TSM. More emphasis has been placed on simplicity and usability than execution time.

## Python Version Support
nitsm supports python versions 3.6, 3.7, 3.8, 3.10, and 3.11. Newer versions of python might work, but it is not guaranteed. Python
2.7 is not supported.

## Installation
```
pip install nitsm
```

nitsm requires [NI TestStand](https://www.ni.com/en-us/support/downloads/software-products/download.teststand.html)
20.0 or higher and
[NI TestStand Semiconductor Module](https://www.ni.com/en-us/support/downloads/software-products/download.teststand-semiconductor-module.html)
20.0 or higher.

To use nitsm in conjunction with [nimi-python](https://github.com/ni/nimi-python), you must also install the appropriate
NI instrument driver for each device you plan to use:
  - [NI-DCPower 20.6+](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dcpower.html)
  - [NI-DMM](https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html)
  - [NI-SCOPE](https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html)
  - [NI-Digital](https://www.ni.com/en-us/support/downloads/drivers/download.ni-digital-pattern-driver.html)
  - [NI-SWITCH](https://www.ni.com/en-us/support/downloads/drivers/download.ni-switch.html)
  - [NI-DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html)
  - [NI-FGEN](https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html)

Visit the [nimi-python](https://github.com/ni/nimi-python) project for information on which python packages to install
alongside each instrument driver.

## Usage
Define code modules with the `code_module` decorator in the `nitsm.codemoduleapi` module. When called from TestStand,
the decorator will convert the [pywin32](https://pypi.org/project/pywin32/) COM object into an
`nitsm.codemoduleapi.SemiconductorModuleContext` object.

```python
import nidcpower
import nitsm.codemoduleapi

@nitsm.codemoduleapi.code_module
def source_current(tsm_context, pins, current_level):
    pin_query_context, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)
    for session, channel_string in zip(sessions, channel_strings):
        session.channels[channel_string].output_function = nidcpower.OutputFunction.DC_CURRENT
        session.channels[channel_string].current_level = current_level
        session.channels[channel_string].initiate()
```

## Known Limitations
* Instrument alarms are currently not supported
* The Set Relays TestStand step is not supported when creating relay sessions in python 
* See [STATUS.md](https://github.com/ni/nitsm-python/blob/main/STATUS.md) for additional information about the current 
state of the API and system tests
````

<!--NI_OSS_SOURCE repo=nitsm-python path=requirements.txt sha256=b5324f85deaf27ed063cf619015c01ccd9941bbed691a3589c331e6c599af885 bytes=128 -->
## FILE: requirements.txt

- repository: `ni/nitsm-python`
- source_path: `requirements.txt`
- sha256: `b5324f85deaf27ed063cf619015c01ccd9941bbed691a3589c331e6c599af885`
- bytes: 128

````text
pywin32
nidcpower
nidmm
niscope
nidigital
niswitch
nidaqmx
nifgen
tox
pytest
pytest-cov
black
ni-python-styleguide
````

<!--NI_OSS_SOURCE repo=nitsm-python path=setup.cfg sha256=775345ee9c3ae5693299d5e1ca620a6dc26f76fef78b995dc4b8e0b7cf4726e3 bytes=601 -->
## FILE: setup.cfg

- repository: `ni/nitsm-python`
- source_path: `setup.cfg`
- sha256: `775345ee9c3ae5693299d5e1ca620a6dc26f76fef78b995dc4b8e0b7cf4726e3`
- bytes: 601

````ini
[metadata]
name = nitsm
version = attr: nitsm.__version__
url = https://github.com/ni/nitsm-python
author = NI
author_email = opensource@ni.com
classifiers =
    License :: OSI Approved :: MIT License
    Operating System :: Microsoft :: Windows
description = NI TestStand Semiconductor Module Python API
long_description = file: README.md
long_description_content_type = text/markdown

[options]
install_requires =
    pywin32>=228;platform_system=="Windows"
python_requires = >=3.6
package_dir =
    =src
packages = find:

[options.packages.find]
where = src
include = nitsm
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/__init__.py sha256=d86549b1cc8782b35bb50dc2906476d3023e20aaad280c51c9498922bcf110b3 bytes=77 -->
## FILE: src/nitsm/__init__.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/__init__.py`
- sha256: `d86549b1cc8782b35bb50dc2906476d3023e20aaad280c51c9498922bcf110b3`
- bytes: 77

````python
"""NI TestStand Semiconductor Module Python API"""

__version__ = "0.2.2"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/_pinmapinterfaces.py sha256=17500f54fc4ae5a1a3ecb104652de100bcdde04352c6ad47d21ea679dfc8c15c bytes=118571 -->
## FILE: src/nitsm/_pinmapinterfaces.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/_pinmapinterfaces.py`
- sha256: `17500f54fc4ae5a1a3ecb104652de100bcdde04352c6ad47d21ea679dfc8c15c`
- bytes: 118571

````python
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# From type library 'NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb'
# On Tue Nov 16 10:28:31 2021
'NI TestStand 2020 Semiconductor Module Pin Map Interfaces'
makepy_version = '0.5.01'
python_version = 0x30608f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{AC54E909-CA87-48AB-9935-A908E5DCB97B}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	PinMapErrorCode_MismatchedHistoryRamPinNames=1          # from enum PinMapErrorCode

from win32com.client import DispatchBaseClass
class IMeasurementPublisher(DispatchBaseClass):
	CLSID = IID('{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}')
	coclass_clsid = None

	def GetInputDataBoolean(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (11, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def GetInputDataDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (5, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def GetInputDataString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (8, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def PublishBool(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (11, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishBoolToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (24, 0), ((3, 1), (8, 1), (11, 1)),siteNumber
			, expression, measurement)

	def PublishDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (5, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishDoubleToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), ((3, 1), (8, 1), (5, 1)),siteNumber
			, expression, measurement)

	def PublishString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishStringToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1)),siteNumber
			, expression, measurement)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentInstanceData(DispatchBaseClass):
	CLSID = IID('{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentModel": (1610743809, 2, (8, 0), (), "InstrumentModel", None),
		"instrumentName": (1610743808, 2, (8, 0), (), "instrumentName", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentProperty(DispatchBaseClass):
	CLSID = IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')
	coclass_clsid = None

	_prop_map_get_ = {
		"PropertyName": (1610743808, 2, (8, 0), (), "PropertyName", None),
		"PropertyValue": (1610743809, 2, (8, 0), (), "PropertyValue", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentPropertyList(DispatchBaseClass):
	CLSID = IID('{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentModel": (1610743808, 2, (8, 0), (), "InstrumentModel", None),
		# Method 'Properties' returns object of type 'IModelBasedInstrumentProperty'
		"Properties": (1610743809, 2, (8201, 0), (), "Properties", '{A8A78603-E18C-4BCB-A347-334AA757B4D5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentResourcePropertyList(DispatchBaseClass):
	CLSID = IID('{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentResource": (1610743808, 2, (8, 0), (), "InstrumentResource", None),
		# Method 'Properties' returns object of type 'IModelBasedInstrumentProperty'
		"Properties": (1610743809, 2, (8201, 0), (), "Properties", '{A8A78603-E18C-4BCB-A347-334AA757B4D5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISemiconductorModuleContext(DispatchBaseClass):
	'NI TestStand Semiconductor Module Pin Map'
	CLSID = IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')
	coclass_clsid = None

	def CreateMultisiteDataForAnalogOutput(self, perPinWaveform=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743864, 1, (8204, 0), ((8204, 1), (8, 1), (12, 1), (16387, 2)), 'CreateMultisiteDataForAnalogOutput', None,perPinWaveform
			, pin, idleValue, numberOfChannelsInTask)

	def CreateMultisiteDataForAnalogOutput_2(self, perPinWaveform=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743865, 1, (8204, 0), ((8204, 1), (8200, 1), (12, 1), (16387, 2)), 'CreateMultisiteDataForAnalogOutput_2', None,perPinWaveform
			, pins, idleValue, numberOfChannelsInTask)

	def CreatePerSiteMultisiteDataForAnalogOutput(self, sitePinWaveforms=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743866, 1, (8204, 0), ((8204, 1), (8, 1), (12, 1), (16387, 2)), 'CreatePerSiteMultisiteDataForAnalogOutput', None,sitePinWaveforms
			, pin, idleValue, numberOfChannelsInTask)

	def CreatePerSiteMultisiteDataForAnalogOutput_2(self, sitePinWaveforms=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743867, 1, (8204, 0), ((8204, 1), (8200, 1), (12, 1), (16387, 2)), 'CreatePerSiteMultisiteDataForAnalogOutput_2', None,sitePinWaveforms
			, pins, idleValue, numberOfChannelsInTask)

	def ExtractPinData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743946, 1, (8197, 0), ((8197, 1), (8200, 1), (8, 1)), 'ExtractPinData', None,data
			, pins, pin)

	def ExtractPinData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743948, 1, (8197, 0), ((8197, 1), (8200, 1), (8, 1)), 'ExtractPinData_2', None,data
			, pins, pin)

	def ExtractPinData_3(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743949, 1, (8203, 0), ((8203, 1), (8200, 1), (8, 1)), 'ExtractPinData_3', None,data
			, pins, pin)

	def ExtractPinData_4(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743951, 1, (8203, 0), ((8203, 1), (8200, 1), (8, 1)), 'ExtractPinData_4', None,data
			, pins, pin)

	def FilterPinsByInstrumentType(self, pins=defaultNamedNotOptArg, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743811, 1, (8200, 0), ((8200, 1), (8, 1), (8, 1)), 'FilterPinsByInstrumentType', None,pins
			, instrumentTypeId, capability)

	def GetAllInstrumentDefinitions(self, instrumentTypeId=defaultNamedNotOptArg, instrumentNames=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743812, 1, (24, 0), ((8, 1), (24584, 2), (24584, 2), (24584, 2)), 'GetAllInstrumentDefinitions', None,instrumentTypeId
			, instrumentNames, channelGroupIds, channelLists)

	def GetAllSessionData(self, instrumentTypeId=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743814, 1, (24, 0), ((8, 1), (24588, 2), (24584, 2), (24584, 2)), 'GetAllSessionData', None,instrumentTypeId
			, sessions, channelGroupIds, channelLists)

	def GetChannelGroupAndChannelIndex(self, pins=defaultNamedNotOptArg, numberOfPinsPerChannelGroup=pythoncom.Missing, channelGroupIndices=pythoncom.Missing, channelIndices=pythoncom.Missing):
		return self._ApplyTypes_(1610743818, 1, (24, 0), ((8200, 1), (24579, 2), (24579, 2), (24579, 2)), 'GetChannelGroupAndChannelIndex', None,pins
			, numberOfPinsPerChannelGroup, channelGroupIndices, channelIndices)

	def GetChannelGroupAndChannelIndex_2(self, pinsInLookup=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, siteNumber=defaultNamedNotOptArg, channelGroupIndex=pythoncom.Missing
			, channelIndex=pythoncom.Missing):
		return self._ApplyTypes_(1610743819, 1, (24, 0), ((8200, 1), (8, 1), (3, 1), (16387, 2), (16387, 2)), 'GetChannelGroupAndChannelIndex_2', None,pinsInLookup
			, pin, siteNumber, channelGroupIndex, channelIndex)

	def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, samplesPerSiteArrayLength=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg
			, perTaskChannelSiteIndexes=pythoncom.Missing, perTaskChannelPinIndexes=pythoncom.Missing, numberOfChannelsPerTask=pythoncom.Missing):
		return self._ApplyTypes_(1610744056, 1, (24, 0), ((8200, 1), (3, 1), (3, 1), (8, 1), (24579, 2), (24579, 2), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite', None,pinNames
			, samplesPerSiteArrayLength, samplesPerPinArrayLength, parameterName, perTaskChannelSiteIndexes, perTaskChannelPinIndexes
			, numberOfChannelsPerTask)

	def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, perTaskChannelPinIndexes=pythoncom.Missing
			, numberOfChannelsPerTask=pythoncom.Missing):
		return self._ApplyTypes_(1610744054, 1, (24, 0), ((8200, 1), (3, 1), (8, 1), (24579, 2), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites', None,pinNames
			, samplesPerPinArrayLength, parameterName, perTaskChannelPinIndexes, numberOfChannelsPerTask)

	def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, samplesPerSiteArrayLength=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg
			, channelSiteIndexes=pythoncom.Missing, channelPinIndexes=pythoncom.Missing):
		return self._ApplyTypes_(1610744055, 1, (24, 0), ((8200, 1), (3, 1), (3, 1), (8, 1), (24579, 2), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite', None,pinNames
			, samplesPerSiteArrayLength, samplesPerPinArrayLength, parameterName, channelSiteIndexes, channelPinIndexes
			)

	def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, channelPinIndexes=pythoncom.Missing):
		return self._ApplyTypes_(1610744053, 1, (24, 0), ((8200, 1), (3, 1), (8, 1), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites', None,pinNames
			, samplesPerPinArrayLength, parameterName, channelPinIndexes)

	def GetDigitalPatternProjectCaptureWaveformFilePaths(self):
		return self._ApplyTypes_(1610743975, 1, (8200, 0), (), 'GetDigitalPatternProjectCaptureWaveformFilePaths', None,)

	def GetDigitalPatternProjectLevelsFilePaths(self):
		return self._ApplyTypes_(1610743971, 1, (8200, 0), (), 'GetDigitalPatternProjectLevelsFilePaths', None,)

	def GetDigitalPatternProjectPatternFilePaths(self):
		return self._ApplyTypes_(1610743973, 1, (8200, 0), (), 'GetDigitalPatternProjectPatternFilePaths', None,)

	def GetDigitalPatternProjectSourceWaveformFilePaths(self):
		return self._ApplyTypes_(1610743974, 1, (8200, 0), (), 'GetDigitalPatternProjectSourceWaveformFilePaths', None,)

	def GetDigitalPatternProjectSpecificationsFilePaths(self):
		return self._ApplyTypes_(1610743970, 1, (8200, 0), (), 'GetDigitalPatternProjectSpecificationsFilePaths', None,)

	def GetDigitalPatternProjectTimingFilePaths(self):
		return self._ApplyTypes_(1610743972, 1, (8200, 0), (), 'GetDigitalPatternProjectTimingFilePaths', None,)

	def GetFPGAInstrumentNames(self, instrumentNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743887, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetFPGAInstrumentNames', None,instrumentNames
			, fpgaFilePaths)

	def GetFPGAVIReference(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743888, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetFPGAVIReferences(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743889, 1, (8213, 0), ((8, 1),), 'GetFPGAVIReferences', None,pin
			)

	def GetFPGAVIReferences_2(self):
		return self._ApplyTypes_(1610743890, 1, (8213, 0), (), 'GetFPGAVIReferences_2', None,)

	def GetGlobalData(self, dataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743944, 1, (12, 0), ((8, 1),), 'GetGlobalData', None,dataId
			)

	def GetInputDataBoolean(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743928, 1, (8203, 0), ((8, 1), (8, 1)), 'GetInputDataBoolean', None,pin
			, inputDataId)

	def GetInputDataDouble(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743929, 1, (8197, 0), ((8, 1), (8, 1)), 'GetInputDataDouble', None,pin
			, inputDataId)

	def GetInputDataString(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743930, 1, (8200, 0), ((8, 1), (8, 1)), 'GetInputDataString', None,pin
			, inputDataId)

	def GetInstrumentNameAndChannelForPinOnSingleSite(self, pinName=defaultNamedNotOptArg, instrumentName=pythoncom.Missing, channelOrPort=pythoncom.Missing):
		return self._ApplyTypes_(1610744050, 1, (24, 0), ((8, 1), (16392, 2), (16392, 2)), 'GetInstrumentNameAndChannelForPinOnSingleSite', None,pinName
			, instrumentName, channelOrPort)

	# Result is of type IModelBasedInstrumentInstanceData
	def GetModelBasedInstrumentNames(self, category=defaultNamedNotOptArg, subcategory=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744000, 1, (8201, 0), ((8, 1), (8, 1)), 'GetModelBasedInstrumentNames', '{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}',category
			, subcategory)

	# Result is of type IModelBasedInstrumentPropertyList
	def GetModelBasedInstrumentProperties(self, instrumentName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610744001, LCID, 1, (9, 0), ((8, 1),),instrumentName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetModelBasedInstrumentProperties', '{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')
		return ret

	def GetModelBasedInstrumentResourceNames(self, instrumentName=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743999, 1, (8200, 0), ((8, 1),), 'GetModelBasedInstrumentResourceNames', None,instrumentName
			)

	# Result is of type IModelBasedInstrumentResourcePropertyList
	def GetModelBasedInstrumentResourceProperties(self, instrumentName=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744002, 1, (8201, 0), ((8, 1),), 'GetModelBasedInstrumentResourceProperties', '{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}',instrumentName
			)

	def GetNI5530RFPortModuleNames(self, ni5530RFPortModuleNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743908, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetNI5530RFPortModuleNames', None,ni5530RFPortModuleNames
			, calibrationFilePaths)

	def GetNI5530RFPortModuleSessions(self, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing):
		return self._ApplyTypes_(1610743910, 1, (24, 0), ((24597, 2), (24597, 2)), 'GetNI5530RFPortModuleSessions', None,ni5530RFPortModuleSessions
			, calibrationSessions)

	def GetNI5530RFPortModuleSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing
			, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing):
		return self._ApplyTypes_(1610743911, 1, (24, 0), ((8, 1), (24585, 2), (24597, 2), (24597, 2), (24584, 2), (24584, 2)), 'GetNI5530RFPortModuleSessions_2', None,pin
			, semiconductorModuleContexts, ni5530RFPortModuleSessions, calibrationSessions, ni5530Channel1, ni5530Channel2
			)

	def GetNI5530RFPortModuleSessions_3(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing
			, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing):
		return self._ApplyTypes_(1610743912, 1, (24, 0), ((8200, 1), (24585, 2), (24597, 2), (24597, 2), (24584, 2), (24584, 2)), 'GetNI5530RFPortModuleSessions_3', None,pins
			, semiconductorModuleContexts, ni5530RFPortModuleSessions, calibrationSessions, ni5530Channel1, ni5530Channel2
			)

	def GetNIDAQmxTask(self, pin=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743860, 1, (24, 0), ((8, 1), (16396, 2), (16392, 2)), 'GetNIDAQmxTask', None,pin
			, task, channelList)

	def GetNIDAQmxTaskNames(self, taskType=defaultNamedNotOptArg, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743857, 1, (8200, 0), ((8, 1), (24584, 2)), 'GetNIDAQmxTaskNames', None,taskType
			, channelLists)

	def GetNIDAQmxTask_2(self, pins=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743861, 1, (24, 0), ((8200, 1), (16396, 2), (16392, 2)), 'GetNIDAQmxTask_2', None,pins
			, task, channelList)

	def GetNIDAQmxTasks(self, taskType=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743859, 1, (8204, 0), ((8, 1),), 'GetNIDAQmxTasks', None,taskType
			)

	def GetNIDAQmxTasks_2(self, pin=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743862, 1, (24, 0), ((8, 1), (24588, 2), (24584, 2)), 'GetNIDAQmxTasks_2', None,pin
			, tasks, channelLists)

	def GetNIDAQmxTasks_3(self, pins=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743863, 1, (24, 0), ((8200, 1), (24588, 2), (24584, 2)), 'GetNIDAQmxTasks_3', None,pins
			, tasks, channelLists)

	def GetNIDCPowerAlarmSession(self, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744048, LCID, 1, (21, 0), ((21, 1),),session
			)

	def GetNIDCPowerInstrumentNames(self, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743821, 1, (8200, 0), ((24584, 2),), 'GetNIDCPowerInstrumentNames', None,channelLists
			)

	def GetNIDCPowerResourceStrings(self):
		return self._ApplyTypes_(1610744040, 1, (8200, 0), (), 'GetNIDCPowerResourceStrings', None,)

	def GetNIDCPowerSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743826, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIDCPowerSession', None,pin
			, session, channelList)

	def GetNIDCPowerSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610744042, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIDCPowerSession_2', None,pins
			, session, channelList)

	def GetNIDCPowerSessions(self):
		return self._ApplyTypes_(1610743823, 1, (8213, 0), (), 'GetNIDCPowerSessions', None,)

	def GetNIDCPowerSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743824, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIDCPowerSessions_2', None,pin
			, sessions, channelLists)

	def GetNIDCPowerSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743825, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIDCPowerSessions_3', None,pins
			, sessions, channelLists)

	def GetNIDigitalPatternInstrumentNames(self):
		return self._ApplyTypes_(1610743952, 1, (8200, 0), (), 'GetNIDigitalPatternInstrumentNames', None,)

	def GetNIDigitalPatternSession(self, pinNames=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing):
		return self._ApplyTypes_(1610743994, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2), (16392, 2)), 'GetNIDigitalPatternSession', None,pinNames
			, session, channelList, siteList)

	def GetNIDigitalPatternSession_2(self, pinName=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing):
		return self._ApplyTypes_(1610743995, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2), (16392, 2)), 'GetNIDigitalPatternSession_2', None,pinName
			, session, channelList, siteList)

	def GetNIDigitalPatternSessions(self):
		return self._ApplyTypes_(1610743953, 1, (8213, 0), (), 'GetNIDigitalPatternSessions', None,)

	def GetNIDigitalPatternSessions_2(self, pinNames=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743955, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2), (24584, 2)), 'GetNIDigitalPatternSessions_2', None,pinNames
			, sessions, channelLists, siteLists)

	def GetNIDigitalPatternSessions_3(self, pinName=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743956, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2), (24584, 2)), 'GetNIDigitalPatternSessions_3', None,pinName
			, sessions, channelLists, siteLists)

	def GetNIDmmInstrumentNames(self):
		return self._ApplyTypes_(1610743837, 1, (8200, 0), (), 'GetNIDmmInstrumentNames', None,)

	def GetNIDmmSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743840, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIDmmSessions(self):
		return self._ApplyTypes_(1610743839, 1, (8213, 0), (), 'GetNIDmmSessions', None,)

	def GetNIDmmSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743841, 1, (8213, 0), ((8, 1),), 'GetNIDmmSessions_2', None,pin
			)

	def GetNIDmmSessions_3(self, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743842, 1, (8213, 0), ((8200, 1),), 'GetNIDmmSessions_3', None,pins
			)

	def GetNIFGenInstrumentNames(self):
		return self._ApplyTypes_(1610743850, 1, (8200, 0), (), 'GetNIFGenInstrumentNames', None,)

	def GetNIFGenSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743853, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIFGenSession', None,pin
			, session, channelList)

	def GetNIFGenSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743855, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIFGenSession_2', None,pins
			, session, channelList)

	def GetNIFGenSessions(self):
		return self._ApplyTypes_(1610743852, 1, (8213, 0), (), 'GetNIFGenSessions', None,)

	def GetNIFGenSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743854, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIFGenSessions_2', None,pin
			, sessions, channelLists)

	def GetNIFGenSessions_3(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743856, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIFGenSessions_3', None,pins
			, session, channelLists)

	def GetNIHSDIOChannelMasks(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing):
		return self._ApplyTypes_(1610743834, 1, (24, 0), ((8200, 1), (24595, 2)), 'GetNIHSDIOChannelMasks', None,pins
			, masks)

	def GetNIHSDIOChannelMasks_2(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing):
		return self._ApplyTypes_(1610743835, 1, (24, 0), ((8200, 1), (24595, 2)), 'GetNIHSDIOChannelMasks_2', None,pins
			, masks)

	def GetNIHSDIOInstrumentNames(self):
		return self._ApplyTypes_(1610743827, 1, (8200, 0), (), 'GetNIHSDIOInstrumentNames', None,)

	def GetNIHSDIOSession(self, pin=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743832, 1, (24, 0), ((8, 1), (16405, 2), (16405, 2), (16392, 2)), 'GetNIHSDIOSession', None,pin
			, acquisitionSession, generationSession, channelList)

	def GetNIHSDIOSession_2(self, pins=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743833, 1, (24, 0), ((8200, 1), (16405, 2), (16405, 2), (16392, 2)), 'GetNIHSDIOSession_2', None,pins
			, acquisitionSession, generationSession, channelList)

	def GetNIHSDIOSessions(self, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing):
		return self._ApplyTypes_(1610743829, 1, (24, 0), ((24597, 2), (24597, 2)), 'GetNIHSDIOSessions', None,acquisitionSessions
			, generationSessions)

	def GetNIHSDIOSessions_2(self, pin=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743830, 1, (24, 0), ((8, 1), (24597, 2), (24597, 2), (24584, 2)), 'GetNIHSDIOSessions_2', None,pin
			, acquisitionSessions, generationSessions, channelLists)

	def GetNIHSDIOSessions_3(self, pins=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743831, 1, (24, 0), ((8200, 1), (24597, 2), (24597, 2), (24584, 2)), 'GetNIHSDIOSessions_3', None,pins
			, acquisitionSessions, generationSessions, channelLists)

	def GetNIRFPMDeembeddingDataForDutPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743901, 1, (24, 0), ((24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMDeembeddingDataForDutPins', None,sessions
			, portLists, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFPMDeembeddingDataForSystemPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743903, 1, (24, 0), ((24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMDeembeddingDataForSystemPins', None,sessions
			, portLists, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFPMInstrumentNames(self, instrumentNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing, iviSwitchNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743892, 1, (24, 0), ((24584, 2), (24584, 2), (24584, 2), (24584, 2)), 'GetNIRFPMInstrumentNames', None,instrumentNames
			, calibrationFilePaths, iviSwitchNames, fpgaFilePaths)

	def GetNIRFPMSession(self, systemPin=defaultNamedNotOptArg, session=pythoncom.Missing, port=pythoncom.Missing, deembeddingFilePath=pythoncom.Missing
			, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610743896, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2), (16392, 2), (16387, 2)), 'GetNIRFPMSession', None,systemPin
			, session, port, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFPMSessions(self):
		return self._ApplyTypes_(1610743894, 1, (8213, 0), (), 'GetNIRFPMSessions', None,)

	def GetNIRFPMSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portList=pythoncom.Missing
			, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743895, 1, (24, 0), ((8, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_2', None,pin
			, semiconductorModuleContexts, sessions, portList, deembeddingFilePaths, deembeddingOrientations
			)

	def GetNIRFPMSessions_3(self, pin1=defaultNamedNotOptArg, pin2=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing
			, portLists1=pythoncom.Missing, portLists2=pythoncom.Missing, deembeddingFilePaths1=pythoncom.Missing, deembeddingFilePaths2=pythoncom.Missing, deembeddingOrientations1=pythoncom.Missing
			, deembeddingOrientations2=pythoncom.Missing):
		return self._ApplyTypes_(1610743897, 1, (24, 0), ((8, 1), (8, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24584, 2), (24584, 2), (24579, 2), (24579, 2)), 'GetNIRFPMSessions_3', None,pin1
			, pin2, semiconductorModuleContexts, sessions, portLists1, portLists2
			, deembeddingFilePaths1, deembeddingFilePaths2, deembeddingOrientations1, deembeddingOrientations2)

	def GetNIRFPMSessions_4(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portLists=pythoncom.Missing
			, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743898, 1, (24, 0), ((8200, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_4', None,pins
			, semiconductorModuleContexts, sessions, portLists, deembeddingFilePaths, deembeddingOrientations
			)

	def GetNIRFPMSessions_5(self, systemPins=defaultNamedNotOptArg, sessions=pythoncom.Missing, portList=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing
			, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743900, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_5', None,systemPins
			, sessions, portList, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSADeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744027, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFSADeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFSADeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744028, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFSADeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSAInstrumentNames(self):
		return self._ApplyTypes_(1610743872, 1, (8200, 0), (), 'GetNIRFSAInstrumentNames', None,)

	def GetNIRFSASession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743875, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFSASession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744021, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFSASession_2', None,pin
			, port)

	def GetNIRFSASessions(self):
		return self._ApplyTypes_(1610743874, 1, (8213, 0), (), 'GetNIRFSASessions', None,)

	def GetNIRFSASessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743876, 1, (8213, 0), ((8, 1),), 'GetNIRFSASessions_2', None,pin
			)

	def GetNIRFSASessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744022, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFSASessions_3', None,pin
			, ports)

	def GetNIRFSGDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744029, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFSGDeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFSGDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744030, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFSGDeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSGInstrumentNames(self):
		return self._ApplyTypes_(1610743882, 1, (8200, 0), (), 'GetNIRFSGInstrumentNames', None,)

	def GetNIRFSGSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743885, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFSGSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744023, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFSGSession_2', None,pin
			, port)

	def GetNIRFSGSessions(self):
		return self._ApplyTypes_(1610743884, 1, (8213, 0), (), 'GetNIRFSGSessions', None,)

	def GetNIRFSGSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743886, 1, (8213, 0), ((8, 1),), 'GetNIRFSGSessions_2', None,pin
			)

	def GetNIRFSGSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744024, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFSGSessions_3', None,pin
			, ports)

	def GetNIRFmxDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744025, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFmxDeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFmxDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744026, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFmxDeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFmxInstrumentNames(self):
		return self._ApplyTypes_(1610743877, 1, (8200, 0), (), 'GetNIRFmxInstrumentNames', None,)

	def GetNIRFmxSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743880, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFmxSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744019, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFmxSession_2', None,pin
			, port)

	def GetNIRFmxSessions(self):
		return self._ApplyTypes_(1610743879, 1, (8213, 0), (), 'GetNIRFmxSessions', None,)

	def GetNIRFmxSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743881, 1, (8213, 0), ((8, 1),), 'GetNIRFmxSessions_2', None,pin
			)

	def GetNIRFmxSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744020, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFmxSessions_3', None,pin
			, ports)

	def GetNIRelayDriverModuleNames(self):
		return self._ApplyTypes_(1610743978, 1, (8200, 0), (), 'GetNIRelayDriverModuleNames', None,)

	def GetNIRelayDriverSession(self, relay=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743981, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIRelayDriverSession', None,relay
			, niSwitchSession, niSwitchRelayNames)

	def GetNIRelayDriverSession_2(self, relays=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743982, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIRelayDriverSession_2', None,relays
			, niSwitchSession, niSwitchRelayNames)

	def GetNIRelayDriverSessions(self):
		return self._ApplyTypes_(1610743980, 1, (8213, 0), (), 'GetNIRelayDriverSessions', None,)

	def GetNIRelayDriverSessions_2(self, relay=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743983, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIRelayDriverSessions_2', None,relay
			, niSwitchSessions, niSwitchRelayNames)

	def GetNIRelayDriverSessions_3(self, relays=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743984, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIRelayDriverSessions_3', None,relays
			, niSwitchSessions, niSwitchRelayNames)

	def GetNIScopeInstrumentNames(self):
		return self._ApplyTypes_(1610743843, 1, (8200, 0), (), 'GetNIScopeInstrumentNames', None,)

	def GetNIScopeSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743846, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIScopeSession', None,pin
			, session, channelList)

	def GetNIScopeSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743848, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIScopeSession_2', None,pins
			, session, channelList)

	def GetNIScopeSessions(self):
		return self._ApplyTypes_(1610743845, 1, (8213, 0), (), 'GetNIScopeSessions', None,)

	def GetNIScopeSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743847, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIScopeSessions_2', None,pin
			, sessions, channelLists)

	def GetNIScopeSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743849, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIScopeSessions_3', None,pins
			, sessions, channelLists)

	def GetPinNames(self, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg, dutPinNames=pythoncom.Missing, systemPinNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743810, 1, (24, 0), ((8, 1), (8, 1), (24584, 2), (24584, 2)), 'GetPinNames', None,instrumentTypeId
			, capability, dutPinNames, systemPinNames)

	def GetRelayDriverSessionsFromRelayConfiguration(self, configurationName=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing, sessionsForRelaysInClosedState=pythoncom.Missing
			, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing):
		return self._ApplyTypes_(1610744003, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2), (24597, 2), (24584, 2)), 'GetRelayDriverSessionsFromRelayConfiguration', None,configurationName
			, sessionsForRelaysInOpenState, niSwitchRelayNamesForRelaysInOpenState, sessionsForRelaysInClosedState, niSwitchRelayNamesForRelaysInClosedState)

	def GetRelayDriverSessionsFromRelays(self, relayNames=defaultNamedNotOptArg, switchRelayActionsAsIntegerArray=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing
			, sessionsForRelaysInClosedState=pythoncom.Missing, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing):
		return self._ApplyTypes_(1610744032, 1, (24, 0), ((8200, 1), (8195, 1), (24597, 2), (24584, 2), (24597, 2), (24584, 2)), 'GetRelayDriverSessionsFromRelays', None,relayNames
			, switchRelayActionsAsIntegerArray, sessionsForRelaysInOpenState, niSwitchRelayNamesForRelaysInOpenState, sessionsForRelaysInClosedState, niSwitchRelayNamesForRelaysInClosedState
			)

	def GetRelayNames(self, siteRelayNames=pythoncom.Missing, systemRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743989, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetRelayNames', None,siteRelayNames
			, systemRelayNames)

	def GetRelaysInRelayGroups(self, relayGroups=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743990, 1, (8200, 0), ((8200, 1),), 'GetRelaysInRelayGroups', None,relayGroups
			)

	# Result is of type ISemiconductorModuleContext
	def GetSemiconductorModuleContextWithSites(self, SiteNumbers=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610744033, LCID, 1, (9, 0), ((8195, 1),),SiteNumbers
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSemiconductorModuleContextWithSites', '{3976D65A-5A34-45FC-B30D-79C4A601C537}')
		return ret

	def GetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupIds=pythoncom.Missing
			, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743815, 1, (24, 0), ((8, 1), (8200, 1), (24588, 2), (24584, 2), (24584, 2)), 'GetSessionData', None,instrumentTypeId
			, pins, sessionData, channelGroupIds, channelLists)

	def GetSessionData_2(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupId=pythoncom.Missing
			, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743816, 1, (24, 0), ((8, 1), (8200, 1), (16396, 2), (16392, 2), (16392, 2)), 'GetSessionData_2', None,instrumentTypeId
			, pins, sessionData, channelGroupId, channelList)

	def GetSiteData(self, dataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743942, 1, (8204, 0), ((8, 1),), 'GetSiteData', None,dataId
			)

	# Result is of type ISemiconductorModuleContext
	def GetSiteSemiconductorModuleContexts(self):
		return self._ApplyTypes_(1610743817, 1, (8201, 0), (), 'GetSiteSemiconductorModuleContexts', '{3976D65A-5A34-45FC-B30D-79C4A601C537}',)

	def GetSpecValue(self, symbol=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743932, LCID, 1, (5, 0), ((8, 1),),symbol
			)

	def GetSpecValues(self, symbols=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743931, 1, (8197, 0), ((8200, 1),), 'GetSpecValues', None,symbols
			)

	def GetSupportedAlarmNames(self, resourceString=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744043, 1, (8200, 0), ((8, 1),), 'GetSupportedAlarmNames', None,resourceString
			)

	def GetSwitchNames(self, switchTypeId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743904, 1, (8200, 0), ((8, 1),), 'GetSwitchNames', None,switchTypeId
			)

	def GetSwitchSessions(self, switchTypeId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743906, 1, (8204, 0), ((8, 1),), 'GetSwitchSessions', None,switchTypeId
			)

	def GetSwitchSessions_2(self, switchTypeId=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, switchSessions=pythoncom.Missing
			, switchRoute=pythoncom.Missing):
		return self._ApplyTypes_(1610743907, 1, (24, 0), ((8, 1), (8, 1), (24585, 2), (24588, 2), (24584, 2)), 'GetSwitchSessions_2', None,switchTypeId
			, pin, semiconductorModuleContexts, switchSessions, switchRoute)

	def GlobalDataExists(self, dataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743992, LCID, 1, (11, 0), ((8, 1),),dataId
			)

	def PerInstrumentToPerSiteData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744012, 1, (8197, 0), ((8197, 1), (8200, 1)), 'PerInstrumentToPerSiteData', None,data
			, pins)

	def PerInstrumentToPerSiteData2D(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744013, 1, (8197, 0), ((8197, 1), (8200, 1)), 'PerInstrumentToPerSiteData2D', None,data
			, pins)

	def PerInstrumentToPerSiteData2D_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744015, 1, (8203, 0), ((8203, 1), (8200, 1)), 'PerInstrumentToPerSiteData2D_2', None,data
			, pins)

	def PerInstrumentToPerSiteData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744014, 1, (8203, 0), ((8203, 1), (8200, 1)), 'PerInstrumentToPerSiteData_2', None,data
			, pins)

	def PerInstrumentToPerSitePatternResults(self, pins=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743998, 1, (8203, 0), ((8200, 1), (8203, 1)), 'PerInstrumentToPerSitePatternResults', None,pins
			, patternResults)

	def PerInstrumentToPerSiteWaveforms(self, pins=defaultNamedNotOptArg, instrumentWaveforms=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743959, 1, (8211, 0), ((8200, 1), (8211, 1)), 'PerInstrumentToPerSiteWaveforms', None,pins
			, instrumentWaveforms)

	def PerSiteToPerInstrumentWaveforms(self, pins=defaultNamedNotOptArg, perSiteWaveforms=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743960, 1, (8211, 0), ((8200, 1), (8211, 1)), 'PerSiteToPerInstrumentWaveforms', None,pins
			, perSiteWaveforms)

	def Publish(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743913, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def PublishHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, sessionIndex=defaultNamedNotOptArg, siteIndex=defaultNamedNotOptArg
			, patternName=defaultNamedNotOptArg, timeSetName=defaultNamedNotOptArg, vectorNumber=defaultNamedNotOptArg, cycleNumber=defaultNamedNotOptArg, expectedPinStates=defaultNamedNotOptArg
			, actualPinStates=defaultNamedNotOptArg, perPinPassFail=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744018, LCID, 1, (24, 0), ((8200, 1), (8, 1), (3, 1), (3, 1), (8, 1), (8, 1), (20, 1), (20, 1), (8209, 1), (8209, 1), (8203, 1)),pins
			, publishedDataId, sessionIndex, siteIndex, patternName, timeSetName
			, vectorNumber, cycleNumber, expectedPinStates, actualPinStates, perPinPassFail
			)

	def PublishPatternResults(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743958, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, patternResults)

	def PublishPatternResults_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743996, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, patternResults)

	def PublishPerSite(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744004, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_2(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744005, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744006, LCID, 1, (24, 0), ((8, 1), (8, 1), (8200, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_4(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744009, LCID, 1, (24, 0), ((8, 1), (8, 1), (5, 1)),pin
			, publishedDataId, measurement)

	def PublishPerSite_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744010, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1)),pin
			, publishedDataId, measurement)

	def PublishPerSite_6(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744011, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1)),pin
			, publishedDataId, measurement)

	def PublishPinNamesForHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, pinNames=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744017, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8200, 1)),pins
			, publishedDataId, pinNames)

	def PublishToTestStandVariablePerSite(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744034, LCID, 1, (24, 0), ((8, 1), (8197, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_2(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744035, LCID, 1, (24, 0), ((8, 1), (8203, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_3(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744036, LCID, 1, (24, 0), ((8, 1), (8200, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_4(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744037, LCID, 1, (24, 0), ((8, 1), (5, 1)),expression
			, measurement)

	def PublishToTestStandVariablePerSite_5(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744038, LCID, 1, (24, 0), ((8, 1), (11, 1)),expression
			, measurement)

	def PublishToTestStandVariablePerSite_6(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744039, LCID, 1, (24, 0), ((8, 1), (8, 1)),expression
			, measurement)

	def Publish_10(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743926, LCID, 1, (24, 0), ((8, 1), (8197, 1)),publishedDataId
			, measurements)

	def Publish_11(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743927, LCID, 1, (24, 0), ((8, 1), (8200, 1)),publishedDataId
			, measurements)

	def Publish_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743914, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8197, 1)),pins
			, publishedDataId, measurements)

	def Publish_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743915, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def Publish_4(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743917, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8197, 1)),pins
			, publishedDataId, measurements)

	def Publish_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743919, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def Publish_6(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743920, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, measurements)

	def Publish_7(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743921, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def Publish_8(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743923, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, measurements)

	def Publish_9(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743925, LCID, 1, (24, 0), ((8, 1), (8203, 1)),publishedDataId
			, measurements)

	def ReportError(self, errorCode=defaultNamedNotOptArg, parameters=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744031, LCID, 1, (24, 0), ((3, 1), (8200, 1)),errorCode
			, parameters)

	def ReportIncompatibleArrayLengths(self, arrayParameterName1=defaultNamedNotOptArg, arrayParameterName2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743986, LCID, 1, (24, 0), ((8, 1), (8, 1)),arrayParameterName1
			, arrayParameterName2)

	def ReportInvalidArray(self, parameterName=defaultNamedNotOptArg, elementType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743985, LCID, 1, (24, 0), ((8, 1), (8, 1)),parameterName
			, elementType)

	def ReportInvalidTimeToWait(self, parameterName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743987, LCID, 1, (24, 0), ((8, 1),),parameterName
			)

	def ReportMissingDriver(self, driverName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743988, LCID, 1, (24, 0), ((8, 1),),driverName
			)

	def ReportUnsupportedCapability(self, capability=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743976, LCID, 1, (24, 0), ((8, 1),),capability
			)

	def SetFPGAVIReference(self, instrumentName=defaultNamedNotOptArg, fpgaVIReference=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743891, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, fpgaVIReference)

	def SetGlobalData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743945, LCID, 1, (24, 0), ((8, 1), (12, 1)),dataId
			, data)

	def SetNI5530RFPortModuleSession(self, ni5530RFPortModuleName=defaultNamedNotOptArg, ni5530RFPortModuleSession=defaultNamedNotOptArg, calibrationSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743909, LCID, 1, (24, 0), ((8, 1), (21, 1), (21, 1)),ni5530RFPortModuleName
			, ni5530RFPortModuleSession, calibrationSession)

	def SetNIDAQmxTask(self, taskName=defaultNamedNotOptArg, task=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743858, LCID, 1, (24, 0), ((8, 1), (12, 1)),taskName
			, task)

	def SetNIDCPowerSession(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743822, LCID, 1, (24, 0), ((8, 1), (8, 1), (21, 1)),instrumentName
			, channelId, session)

	def SetNIDCPowerSession_2(self, resourceString=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg, alarmSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744041, LCID, 1, (24, 0), ((8, 1), (21, 1), (8200, 1), (21, 1)),resourceString
			, session, alarmNames, alarmSession)

	def SetNIDCPowerSession_3(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg
			, alarmSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744044, LCID, 1, (24, 0), ((8, 1), (8, 1), (21, 1), (8200, 1), (21, 1)),instrumentName
			, channelId, session, alarmNames, alarmSession)

	def SetNIDigitalPatternSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743954, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetNIDmmSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743838, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIFGenSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743851, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetNIHSDIOSessions(self, instrumentName=defaultNamedNotOptArg, acquisitionSession=defaultNamedNotOptArg, generationSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (24, 0), ((8, 1), (21, 1), (21, 1)),instrumentName
			, acquisitionSession, generationSession)

	def SetNIRFPMSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743893, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFSASession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743873, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFSGSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743883, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFmxSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743878, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRelayDriverSession(self, relayDriverName=defaultNamedNotOptArg, niSwitchSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743979, LCID, 1, (24, 0), ((8, 1), (21, 1)),relayDriverName
			, niSwitchSession)

	def SetNIScopeSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743844, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, instrumentName=defaultNamedNotOptArg, channelGroupId=defaultNamedNotOptArg, sessionData=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (12, 1)),instrumentTypeId
			, instrumentName, channelGroupId, sessionData)

	def SetSiteData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743943, LCID, 1, (24, 0), ((8, 1), (8204, 1)),dataId
			, data)

	def SetSiteData_2(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744008, LCID, 1, (24, 0), ((8, 1), (8204, 1)),dataId
			, data)

	def SetSwitchSession(self, switchTypeId=defaultNamedNotOptArg, switchName=defaultNamedNotOptArg, switchSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743905, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 1)),switchTypeId
			, switchName, switchSession)

	def SiteDataExists(self, dataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743991, LCID, 1, (11, 0), ((8, 1),),dataId
			)

	_prop_map_get_ = {
		"IsSemiconductorModuleInOfflineMode": (1610743993, 2, (11, 0), (), "IsSemiconductorModuleInOfflineMode", None),
		# Method 'MeasurementPublisher' returns object of type 'IMeasurementPublisher'
		"MeasurementPublisher": (1610743808, 2, (9, 0), (), "MeasurementPublisher", '{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}'),
		"PinMapPath": (1610743963, 2, (8, 0), (), "PinMapPath", None),
		"PinMapUsesNIDCPowerChannelGroups": (1610744052, 2, (11, 0), (), "PinMapUsesNIDCPowerChannelGroups", None),
		"SiteNumbers": (1610743809, 2, (8195, 0), (), "SiteNumbers", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IMeasurementPublisher_vtables_dispatch_ = 1
IMeasurementPublisher_vtables_ = [
	(( 'PublishDouble' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743808, (1610743808, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PublishBool' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PublishString' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743810, (1610743810, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PublishDoubleToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743811, (1610743811, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PublishBoolToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743812, (1610743812, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PublishStringToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743813, (1610743813, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataDouble' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743814, (1610743814, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataBoolean' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743815, (1610743815, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataString' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743816, (1610743816, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentInstanceData_vtables_dispatch_ = 1
IModelBasedInstrumentInstanceData_vtables_ = [
	(( 'instrumentName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InstrumentModel' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentProperty_vtables_dispatch_ = 1
IModelBasedInstrumentProperty_vtables_ = [
	(( 'PropertyName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PropertyValue' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentPropertyList_vtables_dispatch_ = 1
IModelBasedInstrumentPropertyList_vtables_ = [
	(( 'InstrumentModel' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24585, 10, None, "IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentResourcePropertyList_vtables_dispatch_ = 1
IModelBasedInstrumentResourcePropertyList_vtables_ = [
	(( 'InstrumentResource' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24585, 10, None, "IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISemiconductorModuleContext_vtables_dispatch_ = 1
ISemiconductorModuleContext_vtables_ = [
	(( 'MeasurementPublisher' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SiteNumbers' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetPinNames' , 'instrumentTypeId' , 'capability' , 'dutPinNames' , 'systemPinNames' , 
			 ), 1610743810, (1610743810, (), [ (8, 1, None, None) , (8, 1, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FilterPinsByInstrumentType' , 'pins' , 'instrumentTypeId' , 'capability' , 'pRetVal' , 
			 ), 1610743811, (1610743811, (), [ (8200, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetAllInstrumentDefinitions' , 'instrumentTypeId' , 'instrumentNames' , 'channelGroupIds' , 'channelLists' , 
			 ), 1610743812, (1610743812, (), [ (8, 1, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SetSessionData' , 'instrumentTypeId' , 'instrumentName' , 'channelGroupId' , 'sessionData' , 
			 ), 1610743813, (1610743813, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetAllSessionData' , 'instrumentTypeId' , 'sessions' , 'channelGroupIds' , 'channelLists' , 
			 ), 1610743814, (1610743814, (), [ (8, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetSessionData' , 'instrumentTypeId' , 'pins' , 'sessionData' , 'channelGroupIds' , 
			 'channelLists' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , (8200, 1, None, None) , (24588, 2, None, None) , 
			 (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetSessionData_2' , 'instrumentTypeId' , 'pins' , 'sessionData' , 'channelGroupId' , 
			 'channelList' , ), 1610743816, (1610743816, (), [ (8, 1, None, None) , (8200, 1, None, None) , (16396, 2, None, None) , 
			 (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetSiteSemiconductorModuleContexts' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (24585, 10, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelGroupAndChannelIndex' , 'pins' , 'numberOfPinsPerChannelGroup' , 'channelGroupIndices' , 'channelIndices' , 
			 ), 1610743818, (1610743818, (), [ (8200, 1, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelGroupAndChannelIndex_2' , 'pinsInLookup' , 'pin' , 'siteNumber' , 'channelGroupIndex' , 
			 'channelIndex' , ), 1610743819, (1610743819, (), [ (8200, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerInstrumentNames' , 'channelLists' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (24584, 2, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession' , 'instrumentName' , 'channelId' , 'session' , ), 1610743822, (1610743822, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743824, (1610743824, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions_3' , 'pins' , 'sessions' , 'channelLists' , ), 1610743825, (1610743825, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSession' , 'pin' , 'session' , 'channelList' , ), 1610743826, (1610743826, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOInstrumentNames' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetNIHSDIOSessions' , 'instrumentName' , 'acquisitionSession' , 'generationSession' , ), 1610743828, (1610743828, (), [ 
			 (8, 1, None, None) , (21, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions' , 'acquisitionSessions' , 'generationSessions' , ), 1610743829, (1610743829, (), [ (24597, 2, None, None) , 
			 (24597, 2, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions_2' , 'pin' , 'acquisitionSessions' , 'generationSessions' , 'channelLists' , 
			 ), 1610743830, (1610743830, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions_3' , 'pins' , 'acquisitionSessions' , 'generationSessions' , 'channelLists' , 
			 ), 1610743831, (1610743831, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSession' , 'pin' , 'acquisitionSession' , 'generationSession' , 'channelList' , 
			 ), 1610743832, (1610743832, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSession_2' , 'pins' , 'acquisitionSession' , 'generationSession' , 'channelList' , 
			 ), 1610743833, (1610743833, (), [ (8200, 1, None, None) , (16405, 2, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOChannelMasks' , 'pins' , 'masks' , ), 1610743834, (1610743834, (), [ (8200, 1, None, None) , 
			 (24595, 2, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOChannelMasks_2' , 'pins' , 'masks' , ), 1610743835, (1610743835, (), [ (8200, 1, None, None) , 
			 (24595, 2, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmInstrumentNames' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDmmSession' , 'instrumentName' , 'instrumentSession' , ), 1610743838, (1610743838, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSession' , 'pin' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions_2' , 'pin' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions_3' , 'pins' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (8200, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeInstrumentNames' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SetNIScopeSession' , 'instrumentName' , 'session' , ), 1610743844, (1610743844, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSession' , 'pin' , 'session' , 'channelList' , ), 1610743846, (1610743846, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743847, (1610743847, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSession_2' , 'pins' , 'session' , 'channelList' , ), 1610743848, (1610743848, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions_3' , 'pins' , 'sessions' , 'channelLists' , ), 1610743849, (1610743849, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenInstrumentNames' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SetNIFGenSession' , 'instrumentName' , 'session' , ), 1610743851, (1610743851, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSession' , 'pin' , 'session' , 'channelList' , ), 1610743853, (1610743853, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743854, (1610743854, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSession_2' , 'pins' , 'session' , 'channelList' , ), 1610743855, (1610743855, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions_3' , 'pins' , 'session' , 'channelLists' , ), 1610743856, (1610743856, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTaskNames' , 'taskType' , 'channelLists' , 'pRetVal' , ), 1610743857, (1610743857, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDAQmxTask' , 'taskName' , 'task' , ), 1610743858, (1610743858, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks' , 'taskType' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTask' , 'pin' , 'task' , 'channelList' , ), 1610743860, (1610743860, (), [ 
			 (8, 1, None, None) , (16396, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTask_2' , 'pins' , 'task' , 'channelList' , ), 1610743861, (1610743861, (), [ 
			 (8200, 1, None, None) , (16396, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks_2' , 'pin' , 'tasks' , 'channelLists' , ), 1610743862, (1610743862, (), [ 
			 (8, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks_3' , 'pins' , 'tasks' , 'channelLists' , ), 1610743863, (1610743863, (), [ 
			 (8200, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'CreateMultisiteDataForAnalogOutput' , 'perPinWaveform' , 'pin' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743864, (1610743864, (), [ (8204, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'CreateMultisiteDataForAnalogOutput_2' , 'perPinWaveform' , 'pins' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743865, (1610743865, (), [ (8204, 1, None, None) , (8200, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'CreatePerSiteMultisiteDataForAnalogOutput' , 'sitePinWaveforms' , 'pin' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743866, (1610743866, (), [ (8204, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'CreatePerSiteMultisiteDataForAnalogOutput_2' , 'sitePinWaveforms' , 'pins' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743867, (1610743867, (), [ (8204, 1, None, None) , (8200, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSAInstrumentNames' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFSASession' , 'instrumentName' , 'instrumentSession' , ), 1610743873, (1610743873, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASession' , 'pin' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions_2' , 'pin' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxInstrumentNames' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFmxSession' , 'instrumentName' , 'instrumentSession' , ), 1610743878, (1610743878, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSession' , 'pin' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions_2' , 'pin' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGInstrumentNames' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFSGSession' , 'instrumentName' , 'instrumentSession' , ), 1610743883, (1610743883, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSession' , 'pin' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions_2' , 'pin' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAInstrumentNames' , 'instrumentNames' , 'fpgaFilePaths' , ), 1610743887, (1610743887, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReference' , 'pin' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReferences' , 'pin' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReferences_2' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'SetFPGAVIReference' , 'instrumentName' , 'fpgaVIReference' , ), 1610743891, (1610743891, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMInstrumentNames' , 'instrumentNames' , 'calibrationFilePaths' , 'iviSwitchNames' , 'fpgaFilePaths' , 
			 ), 1610743892, (1610743892, (), [ (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFPMSession' , 'instrumentName' , 'instrumentSession' , ), 1610743893, (1610743893, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_2' , 'pin' , 'semiconductorModuleContexts' , 'sessions' , 'portList' , 
			 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610743895, (1610743895, (), [ (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSession' , 'systemPin' , 'session' , 'port' , 'deembeddingFilePath' , 
			 'deembeddingOrientation' , ), 1610743896, (1610743896, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , 
			 (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_3' , 'pin1' , 'pin2' , 'semiconductorModuleContexts' , 'sessions' , 
			 'portLists1' , 'portLists2' , 'deembeddingFilePaths1' , 'deembeddingFilePaths2' , 'deembeddingOrientations1' , 
			 'deembeddingOrientations2' , ), 1610743897, (1610743897, (), [ (8, 1, None, None) , (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , 
			 (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_4' , 'pins' , 'semiconductorModuleContexts' , 'sessions' , 'portLists' , 
			 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610743898, (1610743898, (), [ (8200, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_5' , 'systemPins' , 'sessions' , 'portList' , 'deembeddingFilePaths' , 
			 'deembeddingOrientations' , ), 1610743900, (1610743900, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , 
			 (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMDeembeddingDataForDutPins' , 'sessions' , 'portLists' , 'deembeddingFilePaths' , 'deembeddingOrientations' , 
			 ), 1610743901, (1610743901, (), [ (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMDeembeddingDataForSystemPins' , 'sessions' , 'portLists' , 'deembeddingFilePaths' , 'deembeddingOrientations' , 
			 ), 1610743903, (1610743903, (), [ (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchNames' , 'switchTypeId' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'SetSwitchSession' , 'switchTypeId' , 'switchName' , 'switchSession' , ), 1610743905, (1610743905, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchSessions' , 'switchTypeId' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchSessions_2' , 'switchTypeId' , 'pin' , 'semiconductorModuleContexts' , 'switchSessions' , 
			 'switchRoute' , ), 1610743907, (1610743907, (), [ (8, 1, None, None) , (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleNames' , 'ni5530RFPortModuleNames' , 'calibrationFilePaths' , ), 1610743908, (1610743908, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'SetNI5530RFPortModuleSession' , 'ni5530RFPortModuleName' , 'ni5530RFPortModuleSession' , 'calibrationSession' , ), 1610743909, (1610743909, (), [ 
			 (8, 1, None, None) , (21, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , ), 1610743910, (1610743910, (), [ (24597, 2, None, None) , 
			 (24597, 2, None, None) , ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions_2' , 'pin' , 'semiconductorModuleContexts' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , 
			 'ni5530Channel1' , 'ni5530Channel2' , ), 1610743911, (1610743911, (), [ (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions_3' , 'pins' , 'semiconductorModuleContexts' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , 
			 'ni5530Channel1' , 'ni5530Channel2' , ), 1610743912, (1610743912, (), [ (8200, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Publish' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743913, (1610743913, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'Publish_2' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743914, (1610743914, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'Publish_3' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743915, (1610743915, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'Publish_4' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743917, (1610743917, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'Publish_5' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743919, (1610743919, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'Publish_6' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743920, (1610743920, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'Publish_7' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743921, (1610743921, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'Publish_8' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743923, (1610743923, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'Publish_9' , 'publishedDataId' , 'measurements' , ), 1610743925, (1610743925, (), [ (8, 1, None, None) , 
			 (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'Publish_10' , 'publishedDataId' , 'measurements' , ), 1610743926, (1610743926, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'Publish_11' , 'publishedDataId' , 'measurements' , ), 1610743927, (1610743927, (), [ (8, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataBoolean' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743928, (1610743928, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataDouble' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743929, (1610743929, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataString' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743930, (1610743930, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'GetSpecValues' , 'symbols' , 'pRetVal' , ), 1610743931, (1610743931, (), [ (8200, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'GetSpecValue' , 'symbol' , 'pRetVal' , ), 1610743932, (1610743932, (), [ (8, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'GetSiteData' , 'dataId' , 'pRetVal' , ), 1610743942, (1610743942, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'SetSiteData' , 'dataId' , 'data' , ), 1610743943, (1610743943, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalData' , 'dataId' , 'pRetVal' , ), 1610743944, (1610743944, (), [ (8, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'SetGlobalData' , 'dataId' , 'data' , ), 1610743945, (1610743945, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743946, (1610743946, (), [ (8197, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_2' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743948, (1610743948, (), [ (8197, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_3' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743949, (1610743949, (), [ (8203, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_4' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743951, (1610743951, (), [ (8203, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternInstrumentNames' , 'pRetVal' , ), 1610743952, (1610743952, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions' , 'pRetVal' , ), 1610743953, (1610743953, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDigitalPatternSession' , 'instrumentName' , 'session' , ), 1610743954, (1610743954, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions_2' , 'pinNames' , 'sessions' , 'channelLists' , 'siteLists' , 
			 ), 1610743955, (1610743955, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions_3' , 'pinName' , 'sessions' , 'channelLists' , 'siteLists' , 
			 ), 1610743956, (1610743956, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1240 , (3, 0, None, None) , 0 , )),
	(( 'PublishPatternResults' , 'pins' , 'publishedDataId' , 'patternResults' , ), 1610743958, (1610743958, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1256 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteWaveforms' , 'pins' , 'instrumentWaveforms' , 'pRetVal' , ), 1610743959, (1610743959, (), [ 
			 (8200, 1, None, None) , (8211, 1, None, None) , (24595, 10, None, None) , ], 1 , 1 , 4 , 0 , 1264 , (3, 0, None, None) , 0 , )),
	(( 'PerSiteToPerInstrumentWaveforms' , 'pins' , 'perSiteWaveforms' , 'pRetVal' , ), 1610743960, (1610743960, (), [ 
			 (8200, 1, None, None) , (8211, 1, None, None) , (24595, 10, None, None) , ], 1 , 1 , 4 , 0 , 1272 , (3, 0, None, None) , 0 , )),
	(( 'PinMapPath' , 'pRetVal' , ), 1610743963, (1610743963, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1296 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectSpecificationsFilePaths' , 'pRetVal' , ), 1610743970, (1610743970, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1352 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectLevelsFilePaths' , 'pRetVal' , ), 1610743971, (1610743971, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1360 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectTimingFilePaths' , 'pRetVal' , ), 1610743972, (1610743972, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1368 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectPatternFilePaths' , 'pRetVal' , ), 1610743973, (1610743973, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1376 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectSourceWaveformFilePaths' , 'pRetVal' , ), 1610743974, (1610743974, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1384 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectCaptureWaveformFilePaths' , 'pRetVal' , ), 1610743975, (1610743975, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1392 , (3, 0, None, None) , 0 , )),
	(( 'ReportUnsupportedCapability' , 'capability' , ), 1610743976, (1610743976, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1400 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverModuleNames' , 'pRetVal' , ), 1610743978, (1610743978, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1416 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRelayDriverSession' , 'relayDriverName' , 'niSwitchSession' , ), 1610743979, (1610743979, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1424 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions' , 'pRetVal' , ), 1610743980, (1610743980, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1432 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSession' , 'relay' , 'niSwitchSession' , 'niSwitchRelayNames' , ), 1610743981, (1610743981, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1440 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSession_2' , 'relays' , 'niSwitchSession' , 'niSwitchRelayNames' , ), 1610743982, (1610743982, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1448 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions_2' , 'relay' , 'niSwitchSessions' , 'niSwitchRelayNames' , ), 1610743983, (1610743983, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1456 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions_3' , 'relays' , 'niSwitchSessions' , 'niSwitchRelayNames' , ), 1610743984, (1610743984, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1464 , (3, 0, None, None) , 0 , )),
	(( 'ReportInvalidArray' , 'parameterName' , 'elementType' , ), 1610743985, (1610743985, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1472 , (3, 0, None, None) , 0 , )),
	(( 'ReportIncompatibleArrayLengths' , 'arrayParameterName1' , 'arrayParameterName2' , ), 1610743986, (1610743986, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1480 , (3, 0, None, None) , 0 , )),
	(( 'ReportInvalidTimeToWait' , 'parameterName' , ), 1610743987, (1610743987, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1488 , (3, 0, None, None) , 0 , )),
	(( 'ReportMissingDriver' , 'driverName' , ), 1610743988, (1610743988, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1496 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayNames' , 'siteRelayNames' , 'systemRelayNames' , ), 1610743989, (1610743989, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1504 , (3, 0, None, None) , 0 , )),
	(( 'GetRelaysInRelayGroups' , 'relayGroups' , 'pRetVal' , ), 1610743990, (1610743990, (), [ (8200, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1512 , (3, 0, None, None) , 0 , )),
	(( 'SiteDataExists' , 'dataId' , 'pRetVal' , ), 1610743991, (1610743991, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1520 , (3, 0, None, None) , 0 , )),
	(( 'GlobalDataExists' , 'dataId' , 'pRetVal' , ), 1610743992, (1610743992, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1528 , (3, 0, None, None) , 0 , )),
	(( 'IsSemiconductorModuleInOfflineMode' , 'pRetVal' , ), 1610743993, (1610743993, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1536 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSession' , 'pinNames' , 'session' , 'channelList' , 'siteList' , 
			 ), 1610743994, (1610743994, (), [ (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1544 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSession_2' , 'pinName' , 'session' , 'channelList' , 'siteList' , 
			 ), 1610743995, (1610743995, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1552 , (3, 0, None, None) , 0 , )),
	(( 'PublishPatternResults_2' , 'pins' , 'publishedDataId' , 'patternResults' , ), 1610743996, (1610743996, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1560 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSitePatternResults' , 'pins' , 'patternResults' , 'pRetVal' , ), 1610743998, (1610743998, (), [ 
			 (8200, 1, None, None) , (8203, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1576 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentResourceNames' , 'instrumentName' , 'pRetVal' , ), 1610743999, (1610743999, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1584 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentNames' , 'category' , 'subcategory' , 'pRetVal' , ), 1610744000, (1610744000, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24585, 10, None, "IID('{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}')") , ], 1 , 1 , 4 , 0 , 1592 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentProperties' , 'instrumentName' , 'pRetVal' , ), 1610744001, (1610744001, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')") , ], 1 , 1 , 4 , 0 , 1600 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentResourceProperties' , 'instrumentName' , 'pRetVal' , ), 1610744002, (1610744002, (), [ (8, 1, None, None) , 
			 (24585, 10, None, "IID('{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}')") , ], 1 , 1 , 4 , 0 , 1608 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayDriverSessionsFromRelayConfiguration' , 'configurationName' , 'sessionsForRelaysInOpenState' , 'niSwitchRelayNamesForRelaysInOpenState' , 'sessionsForRelaysInClosedState' , 
			 'niSwitchRelayNamesForRelaysInClosedState' , ), 1610744003, (1610744003, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , 
			 (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1616 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744004, (1610744004, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1624 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_2' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744005, (1610744005, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1632 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_3' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744006, (1610744006, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1640 , (3, 0, None, None) , 0 , )),
	(( 'SetSiteData_2' , 'dataId' , 'data' , ), 1610744008, (1610744008, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 1656 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_4' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744009, (1610744009, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 1664 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_5' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744010, (1610744010, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1672 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_6' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744011, (1610744011, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1680 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData' , 'data' , 'pins' , 'pRetVal' , ), 1610744012, (1610744012, (), [ 
			 (8197, 1, None, None) , (8200, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1688 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData2D' , 'data' , 'pins' , 'pRetVal' , ), 1610744013, (1610744013, (), [ 
			 (8197, 1, None, None) , (8200, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1696 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData_2' , 'data' , 'pins' , 'pRetVal' , ), 1610744014, (1610744014, (), [ 
			 (8203, 1, None, None) , (8200, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1704 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData2D_2' , 'data' , 'pins' , 'pRetVal' , ), 1610744015, (1610744015, (), [ 
			 (8203, 1, None, None) , (8200, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1712 , (3, 0, None, None) , 0 , )),
	(( 'PublishPinNamesForHistoryRamCycleInformation' , 'pins' , 'publishedDataId' , 'pinNames' , ), 1610744017, (1610744017, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1728 , (3, 0, None, None) , 0 , )),
	(( 'PublishHistoryRamCycleInformation' , 'pins' , 'publishedDataId' , 'sessionIndex' , 'siteIndex' , 
			 'patternName' , 'timeSetName' , 'vectorNumber' , 'cycleNumber' , 'expectedPinStates' , 
			 'actualPinStates' , 'perPinPassFail' , ), 1610744018, (1610744018, (), [ (8200, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (20, 1, None, None) , 
			 (20, 1, None, None) , (8209, 1, None, None) , (8209, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1736 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744019, (1610744019, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1744 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744020, (1610744020, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1752 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744021, (1610744021, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1760 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744022, (1610744022, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1768 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744023, (1610744023, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1776 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744024, (1610744024, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1784 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxDeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744025, (1610744025, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1792 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxDeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744026, (1610744026, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1800 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSADeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744027, (1610744027, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1808 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSADeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744028, (1610744028, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1816 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGDeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744029, (1610744029, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1824 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGDeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744030, (1610744030, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1832 , (3, 0, None, None) , 0 , )),
	(( 'ReportError' , 'errorCode' , 'parameters' , ), 1610744031, (1610744031, (), [ (3, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1840 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayDriverSessionsFromRelays' , 'relayNames' , 'switchRelayActionsAsIntegerArray' , 'sessionsForRelaysInOpenState' , 'niSwitchRelayNamesForRelaysInOpenState' , 
			 'sessionsForRelaysInClosedState' , 'niSwitchRelayNamesForRelaysInClosedState' , ), 1610744032, (1610744032, (), [ (8200, 1, None, None) , (8195, 1, None, None) , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1848 , (3, 0, None, None) , 0 , )),
	(( 'GetSemiconductorModuleContextWithSites' , 'SiteNumbers' , 'pRetVal' , ), 1610744033, (1610744033, (), [ (8195, 1, None, None) , 
			 (16393, 10, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , ], 1 , 1 , 4 , 0 , 1856 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite' , 'expression' , 'measurements' , ), 1610744034, (1610744034, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1864 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_2' , 'expression' , 'measurements' , ), 1610744035, (1610744035, (), [ (8, 1, None, None) , 
			 (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1872 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_3' , 'expression' , 'measurements' , ), 1610744036, (1610744036, (), [ (8, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1880 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_4' , 'expression' , 'measurement' , ), 1610744037, (1610744037, (), [ (8, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 1888 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_5' , 'expression' , 'measurement' , ), 1610744038, (1610744038, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1896 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_6' , 'expression' , 'measurement' , ), 1610744039, (1610744039, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1904 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerResourceStrings' , 'pRetVal' , ), 1610744040, (1610744040, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1912 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession_2' , 'resourceString' , 'session' , 'alarmNames' , 'alarmSession' , 
			 ), 1610744041, (1610744041, (), [ (8, 1, None, None) , (21, 1, None, None) , (8200, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1920 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSession_2' , 'pins' , 'session' , 'channelList' , ), 1610744042, (1610744042, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1928 , (3, 0, None, None) , 0 , )),
	(( 'GetSupportedAlarmNames' , 'resourceString' , 'pRetVal' , ), 1610744043, (1610744043, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1936 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession_3' , 'instrumentName' , 'channelId' , 'session' , 'alarmNames' , 
			 'alarmSession' , ), 1610744044, (1610744044, (), [ (8, 1, None, None) , (8, 1, None, None) , (21, 1, None, None) , 
			 (8200, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1944 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerAlarmSession' , 'session' , 'pRetVal' , ), 1610744048, (1610744048, (), [ (21, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1976 , (3, 0, None, None) , 0 , )),
	(( 'GetInstrumentNameAndChannelForPinOnSingleSite' , 'pinName' , 'instrumentName' , 'channelOrPort' , ), 1610744050, (1610744050, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1992 , (3, 0, None, None) , 0 , )),
	(( 'PinMapUsesNIDCPowerChannelGroups' , 'pRetVal' , ), 1610744052, (1610744052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 2008 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites' , 'pinNames' , 'samplesPerPinArrayLength' , 'parameterName' , 'channelPinIndexes' , 
			 ), 1610744053, (1610744053, (), [ (8200, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 2016 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites' , 'pinNames' , 'samplesPerPinArrayLength' , 'parameterName' , 'perTaskChannelPinIndexes' , 
			 'numberOfChannelsPerTask' , ), 1610744054, (1610744054, (), [ (8200, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			 (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 2024 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite' , 'pinNames' , 'samplesPerSiteArrayLength' , 'samplesPerPinArrayLength' , 'parameterName' , 
			 'channelSiteIndexes' , 'channelPinIndexes' , ), 1610744055, (1610744055, (), [ (8200, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (8, 1, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 2032 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite' , 'pinNames' , 'samplesPerSiteArrayLength' , 'samplesPerPinArrayLength' , 'parameterName' , 
			 'perTaskChannelSiteIndexes' , 'perTaskChannelPinIndexes' , 'numberOfChannelsPerTask' , ), 1610744056, (1610744056, (), [ (8200, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , 
			 (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 2040 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{3976D65A-5A34-45FC-B30D-79C4A601C537}' : ISemiconductorModuleContext,
	'{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}' : IModelBasedInstrumentInstanceData,
	'{3BFF2733-C91A-4590-899A-BE97B57C9EDE}' : IModelBasedInstrumentPropertyList,
	'{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}' : IModelBasedInstrumentResourcePropertyList,
	'{A8A78603-E18C-4BCB-A347-334AA757B4D5}' : IModelBasedInstrumentProperty,
	'{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}' : IMeasurementPublisher,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{3976D65A-5A34-45FC-B30D-79C4A601C537}' : 'ISemiconductorModuleContext',
	'{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}' : 'IModelBasedInstrumentInstanceData',
	'{3BFF2733-C91A-4590-899A-BE97B57C9EDE}' : 'IModelBasedInstrumentPropertyList',
	'{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}' : 'IModelBasedInstrumentResourcePropertyList',
	'{A8A78603-E18C-4BCB-A347-334AA757B4D5}' : 'IModelBasedInstrumentProperty',
	'{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}' : 'IMeasurementPublisher',
}


NamesToIIDMap = {
	'ISemiconductorModuleContext' : '{3976D65A-5A34-45FC-B30D-79C4A601C537}',
	'IModelBasedInstrumentInstanceData' : '{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}',
	'IModelBasedInstrumentPropertyList' : '{3BFF2733-C91A-4590-899A-BE97B57C9EDE}',
	'IModelBasedInstrumentResourcePropertyList' : '{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}',
	'IModelBasedInstrumentProperty' : '{A8A78603-E18C-4BCB-A347-334AA757B4D5}',
	'IMeasurementPublisher' : '{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/codemoduleapi.py sha256=cc96b951c5b54e54260981c9765e6d3509138e4ba20ea1297723535611e4ded2 bytes=2755 -->
## FILE: src/nitsm/codemoduleapi.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/codemoduleapi.py`
- sha256: `cc96b951c5b54e54260981c9765e6d3509138e4ba20ea1297723535611e4ded2`
- bytes: 2755

````python
"""Code Module API"""

import functools
import inspect

from .enums import Capability, InstrumentTypeIdConstants
from .tsmcontext import SemiconductorModuleContext

__all__ = ["SemiconductorModuleContext", "Capability", "InstrumentTypeIdConstants", "code_module"]


# noinspection PyPep8Naming
class code_module:  # noqa: N801
    """This function decorator wraps the ISemiconductorModuleContext
    win32com.client.dynamic.CDispatch object passed from the Semiconductor Multi Test step into a
    nitsm.codemoduleapi.SemiconductorModuleContext object prior to calling the decorated function.
    """

    def __init__(self, func):
        """Converts a function into a TSM code module.

        The Semiconductor Multi Test step must pass the Step.SemiconductorModuleContext property to
        the code module as the first positional argument.
        """
        self._func = func
        self._signature = inspect.signature(func)
        functools.update_wrapper(self, func)

    def __get__(self, instance, owner):
        """Binds the code module to an object or class."""
        func = self._func.__get__(instance, owner)
        return type(self)(func)

    def __call__(self, *args, **kwargs):
        """Calls the code module."""
        bound_arguments = self._signature.bind(*args, **kwargs)
        arguments_iter = iter(bound_arguments.arguments.items())

        # find potential argument that could be the tsm context
        try:
            argument = next(arguments_iter)  # get first argument
            if inspect.isclass(argument[1]):  # class method check
                argument = next(arguments_iter)  # move to second argument
        except StopIteration:
            raise TypeError(
                (
                    "The number of arguments to the code module is less than expected. It must "
                    "accept as it's first argument the Semiconductor Module context passed from "
                    "TestStand or another code module.",
                )
            )

        # attempt to wrap argument in a SemiconductorModuleContext object
        argument_name, argument_value = argument
        if not isinstance(argument_value, SemiconductorModuleContext):
            try:
                argument_value = SemiconductorModuleContext(argument_value)
            except Exception:
                class_name = type(argument_value).__name__
                raise ValueError(
                    f"Failed to convert Semiconductor Module context from class '{class_name}'.",
                )
            bound_arguments.arguments[argument_name] = argument_value

        return self._func(*bound_arguments.args, **bound_arguments.kwargs)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/debug.py sha256=7792088c674b3394ee7bb05d233ca8e45f9551e7ddaf214a272c2fa467e83657 bytes=1740 -->
## FILE: src/nitsm/debug.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/debug.py`
- sha256: `7792088c674b3394ee7bb05d233ca8e45f9551e7ddaf214a272c2fa467e83657`
- bytes: 1740

````python
"""Code Module Debugging Utilities"""

import os
import tkinter.messagebox


def prompt_attach_debugger() -> None:
    """Pauses the Python interpreter and displays the process ID (PID). The PID can be used by an
    IDE such as PyCharm to attach to the process for debugging. This is useful for stepping into
    nitsm code modules from TestStand.

    Instructions for use with PyCharm:
        1. Call this function from the code module you want to debug. Placing it at the beginning
            of the code module is recommended.
        2. Add a breakpoint at the location where you want to start debugging. Make sure this
            breakpoint will be reached after this function is called.
        3. In TestStand, execute a sequence that calls into the code module.
        4. A dialog box will appear displaying the PID of the current process. Before clicking
            "Okay" on the dialog, select Run -> Attach To Process... from the PyCharm menu.
        5. PyCharm will display a window of discovered processes. Click the process with the
            matching PID.
        6. PyCharm will open a debug terminal and attach to the process. Wait for PyCharm to
            indicate it has successfully attached.
        6. Once PyCharm is attached, click "Okay" on the dialog to continue execution. If these
            steps were performed correctly, PyCharm will break at the first breakpoint it reaches in
            the code.
    """
    tkinter.Tk().withdraw()  # hide root window
    tkinter.messagebox.showinfo(
        "Attach debugger", "Process name: niPythonHost.exe and Process ID: " + str(os.getpid())
    )
    return


if __name__ == "__main__":
    prompt_attach_debugger()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/enums.py sha256=18c4b6088134112d49070ba8eece9ba74e64039ab7de7bbc777c92b86154f72c bytes=910 -->
## FILE: src/nitsm/enums.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/enums.py`
- sha256: `18c4b6088134112d49070ba8eece9ba74e64039ab7de7bbc777c92b86154f72c`
- bytes: 910

````python
"""Enumerations"""

import enum

__all__ = ["Capability", "InstrumentTypeIdConstants"]


class Capability(enum.Enum):
    """Differentiates between pins in the same instrument with different capabilities, such as
    NI-HSDIO Dynamic DIO channels and PFI lines.
    """

    ALL = ""
    NI_HSDIO_DYNAMIC_DIO = "NIHSDIODynamicDIOCapable"


class InstrumentTypeIdConstants(enum.Enum):
    """The type IDs for non-custom instruments in the pin map file."""

    ANY = ""
    NI_DAQMX = "niDAQmx"
    NI_DCPOWER = "niDCPower"
    NI_DIGITAL_PATTERN = "niDigitalPattern"
    NI_DMM = "niDMM"
    NI_FGEN = "niFGen"
    NI_GENERIC_MULTIPLEXER = "NIGenericMultiplexer"
    NI_HSDIO = "niHSDIO"
    NI_MODEL_BASED_INSTRUMENT = "niModelBasedInstrument"
    NI_RELAY_DRIVER = "niRelayDriver"
    NI_RFPM = "niRFPM"
    NI_RFSA = "niRFSA"
    NI_RFSG = "niRFSG"
    NI_SCOPE = "niScope"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/pinquerycontexts.py sha256=f5da617ef6b7aa04e03799070da825a4a36b24a7013aea834ffb71b1cf84f370 bytes=9904 -->
## FILE: src/nitsm/pinquerycontexts.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/pinquerycontexts.py`
- sha256: `f5da617ef6b7aa04e03799070da825a4a36b24a7013aea834ffb71b1cf84f370`
- bytes: 9904

````python
"""Pin Query Contexts"""

import re
import typing

__all__ = ["PinQueryContext", "DigitalPatternPinQueryContext"]

if typing.TYPE_CHECKING:
    import nitsm._pinmapinterfaces

    _PublishDataScalar = typing.Union[bool, int, float]
    _PublishDataSequence = typing.Sequence[_PublishDataScalar]
    _PublishDataJaggedSequence = typing.Sequence[_PublishDataSequence]
    _PublishDataArg = typing.Union[
        _PublishDataScalar, _PublishDataSequence, _PublishDataJaggedSequence
    ]
    _PublishPatternArg = typing.Union[
        typing.Dict[int, bool], typing.Sequence[typing.Dict[int, bool]]
    ]


def _pad_jagged_sequence(seq):
    """Pads a 2D jagged sequence with the default value of the element type to make it rectangular.

    The type of each sequence (tuple, list, etc) is maintained.
    """
    columns = max(map(len, seq))  # gets length of the longest row
    return type(seq)(
        (
            sub_seq + type(sub_seq)(type(sub_seq[0])() for _ in range(columns - len(sub_seq)))
            for sub_seq in seq
        )
    )


class PinQueryContext:
    """Provides the base class for a pin query context, which is an object a pin query method
    returns to track the sessions and channels associated with the pins for one or more sites.
    """

    def __init__(self, tsm_context, pins):
        """Not for public use."""
        self._tsm_context: nitsm._pinmapinterfaces.ISemiconductorModuleContext = tsm_context
        self._pins: typing.Union[str, typing.Sequence[str]] = pins

    def get_session_and_channel_index(self, site_number: int, pin: str):
        """Returns the index of the session and channel that corresponds to a pin query. Use this
        method to access an individual pin on a specific site when you take a measurement across
        multiple instruments. When you call a pin query method, such as
        pins_to_nidigital_sessions_for_ppmu, the method returns a tuple of sessions and a tuple of
        channel lists. Use this method to identify which session and which channel refers to the pin
        from the pin query and the site number you specify.

        Args:
            site_number: The site number of the pin to obtain the session and channel index in a
                previous pin query. For a system pin, pass any valid site number.
            pin: The name of the pin to obtain the session and channel index in a previous pin
                query.

        Returns:
            session_index: Returns the index of the session for a measurement taken on the pin and
                site number you specify.
            channel_index: Returns the index of the channel within the channel list for a
                measurement taken on the pin and site number you specify.
        """
        pins = [self._pins] if isinstance(self._pins, str) else self._pins
        return self._tsm_context.GetChannelGroupAndChannelIndex_2(pins, pin, site_number, 0, 0)

    def publish(self, data: "_PublishDataArg", published_data_id=""):
        """Publishes the measurement data for one or more pins to the Semiconductor Multi Test step
        for all sites in the PinQueryContext.

        Args:
            data: The measurement data from one or more pins connected to one or more instruments.
                The values can be bools, ints, or floats, and each value represents a measurement
                made for a single instrument channel. Pass a single value if the pin query refers
                to a single channel on a single instrument. Pass a sequence of values if the pin
                query refers to multiple channels on a single instrument or multiple instruments
                with a single channel. Pass a two dimensional sequence of values if the pin query
                refers to multiple channels on multiple instruments.
            published_data_id: The unique ID for distinguishing the measurement when you publish
                multiple measurements for the same pins within the same code module. This ID must
                match one of the values in the Published Data Id column on the Tests tab of the
                Semiconductor Multi Test step.
        """
        if isinstance(data, bool):
            return self._publish_bool_scalar(data, published_data_id)
        elif isinstance(data, (float, int)):
            return self._publish_float_scalar(data, published_data_id)
        else:
            return self._publish_sequence(data, published_data_id)

    def _publish_float_scalar(self, data, published_data_id):
        return self._publish_float_1d([data], published_data_id)

    def _publish_bool_scalar(self, data, published_data_id):
        return self._publish_bool_1d([data], published_data_id)

    def _publish_sequence(self, data, published_data_id):
        if isinstance(data[0], bool):
            return self._publish_bool_1d(data, published_data_id)
        elif isinstance(data[0], (float, int)):
            return self._publish_float_1d(data, published_data_id)
        else:
            return self._publish_sequence_2d(data, published_data_id)

    def _publish_float_1d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_2(self._pins, published_data_id, data)

    def _publish_bool_1d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_5(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_6(self._pins, published_data_id, data)

    def _publish_sequence_2d(self, data, published_data_id):
        data = _pad_jagged_sequence(data)  # make 2d sequence rectangular
        if isinstance(data[0][0], bool):
            return self._publish_bool_2d(data, published_data_id)
        else:
            return self._publish_float_2d(data, published_data_id)

    def _publish_float_2d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_3(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_4(self._pins, published_data_id, data)

    def _publish_bool_2d(self, data, published_data_id):
        if isinstance(self._pins, str):
            return self._tsm_context.Publish_7(self._pins, published_data_id, data)
        else:
            return self._tsm_context.Publish_8(self._pins, published_data_id, data)


class DigitalPatternPinQueryContext(PinQueryContext):
    """An object the pins_to_nidigital_session_for_pattern and
    pins_to_nidigital_sessions_for_pattern methods return to track the sessions and channels
    associated with the pins for one or more sites. Use this object to publish measurements to the
    Semiconductor Multi Test step and to extract data from a set of measurements.
    """

    def __init__(self, tsm_context, pins, site_lists):
        """Not for public use."""
        # convert pins to a list of pins if it isn't already
        if isinstance(pins, str):
            pins = [pins]

        super().__init__(tsm_context, pins)

        # convert site_lists to a list if it isn't already
        if isinstance(site_lists, str):
            self._site_lists = [site_lists]
        else:
            self._site_lists = site_lists

    def publish_pattern_results(
        self, instrument_site_pattern_results: "_PublishPatternArg", published_data_id=""
    ):
        """Publishes results from NI-Digital pattern burst to the Semiconductor Multi Test step for
        all sites in the Semiconductor Module context. Leave the Pin column blank for the test on
        the Semiconductor Multi Test step when publishing pattern results with this method.

        Args:
            instrument_site_pattern_results: The pattern result data from multiple pins connected to
                one or more NI-Digital Pattern instruments. Provide a dictionary that maps sites to
                result data to publish pattern results from a single NI-Digital Pattern instrument
                session. Provide a sequence of dictionaries that map sites to result data to publish
                pattern results from multiple NI-Digital Pattern instrument sessions. Each element
                in the sequence contains pattern results for the sites of a single instrument
                session. Furthermore, the size of the sequence must be the same size as the session
                data output from the pin query method.
            published_data_id: The unique ID for identifying the results. This ID must match one of
                the values in the Published Data Id column on the Tests tab of the Semiconductor
                Multi Test step.
        """
        # convert instrument_site_pattern_results to a list if it isn't already
        if isinstance(instrument_site_pattern_results, dict):
            instrument_site_pattern_results = [instrument_site_pattern_results]

        # convert pattern results dictionaries to pattern results lists then publish
        re_pattern = re.compile(r"\s*site(\d+)")
        instrument_site_pattern_results = [
            [
                pattern_results[int(match[1])]
                for match in map(re_pattern.match, site_list.split(","))
            ]
            for site_list, pattern_results in zip(self._site_lists, instrument_site_pattern_results)
        ]
        instrument_site_pattern_results = _pad_jagged_sequence(instrument_site_pattern_results)
        return self._tsm_context.PublishPatternResults(
            self._pins, published_data_id, instrument_site_pattern_results
        )
````

<!--NI_OSS_SOURCE repo=nitsm-python path=src/nitsm/tsmcontext.py sha256=5279bae27c00b3a5b80b2a9a72bbaec45a41677971789bf8f750773df3c85c11 bytes=81287 -->
## FILE: src/nitsm/tsmcontext.py

- repository: `ni/nitsm-python`
- source_path: `src/nitsm/tsmcontext.py`
- sha256: `5279bae27c00b3a5b80b2a9a72bbaec45a41677971789bf8f750773df3c85c11`
- bytes: 81287

````python
"""TSM Context Wrapper"""

import ctypes.wintypes
import time
import typing

import nitsm._pinmapinterfaces
import nitsm.enums
import nitsm.pinquerycontexts
import pythoncom
import win32com.client

__all__ = ["SemiconductorModuleContext"]

if typing.TYPE_CHECKING:
    import nidigital
    import nidcpower
    import nidaqmx
    import nidmm
    import nifgen
    import niscope
    import niswitch

    _Any = typing.Any
    _Tuple = typing.Tuple
    _Union = typing.Union
    _Sequence = typing.Sequence

    _ISemiconductorModuleContext = win32com.client.dynamic.CDispatch
    _PinQueryContext = nitsm.pinquerycontexts.PinQueryContext
    _DigitalPatternPinQueryContext = nitsm.pinquerycontexts.DigitalPatternPinQueryContext
    _InstrTypeIdArg = _Union[nitsm.enums.InstrumentTypeIdConstants, str]
    _CapabilityArg = _Union[nitsm.enums.Capability, str]
    _PinsArg = _Union[str, _Sequence[str]]  # argument that accepts 1 or more pins
    _StringTuple = _Tuple[str, ...]
    _AnyTuple = _Tuple[_Any, ...]

    _NIDigitalSingleSessionPpmuQuery = _Tuple[_PinQueryContext, nidigital.Session, str]
    _NIDigitalMultipleSessionPpmuQuery = _Tuple[
        _PinQueryContext,
        _Tuple[nidigital.Session, ...],
        _StringTuple,
    ]
    _NIDigitalSingleSessionPatternQuery = _Tuple[
        _DigitalPatternPinQueryContext, nidigital.Session, str
    ]
    _NIDigitalMultipleSessionPatternQuery = _Tuple[
        _DigitalPatternPinQueryContext,
        _Tuple[nidigital.Session, ...],
        _StringTuple,
    ]

    _NIDCPowerSingleSessionQuery = _Tuple[_PinQueryContext, nidcpower.Session, str]
    _NIDCPowerMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[nidcpower.Session, ...], _StringTuple
    ]

    _NIDAQmxSingleSessionQuery = _Tuple[_PinQueryContext, nidaqmx.Task, str]
    _NIDAQmxMultipleSessionQuery = _Tuple[_PinQueryContext, _Tuple[nidaqmx.Task, ...], _StringTuple]

    _NIDmmSingleSessionQuery = _Tuple[_PinQueryContext, nidmm.Session]
    _NIDmmMultipleSessionQuery = _Tuple[_PinQueryContext, _Tuple[nidmm.Session, ...]]

    _NIFGenSingleSessionQuery = _Tuple[_PinQueryContext, nifgen.Session, str]
    _NIFGenMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[nifgen.Session, ...], _StringTuple
    ]

    _NIScopeSingleSessionQuery = _Tuple[_PinQueryContext, niscope.Session, str]
    _NIScopeMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[niscope.Session, ...], _StringTuple
    ]

    _SwitchQuery = _Tuple[_Tuple["SemiconductorModuleContext", ...], _AnyTuple, _StringTuple]

    _RelayDriverSingleSessionQuery = _Tuple[niswitch.Session, str]
    _RelayDriverMultipleSessionQuery = _Tuple[_Tuple[niswitch.Session, ...], _StringTuple]

    _CustomSingleSessionQuery = _Tuple[_PinQueryContext, _Any, str, str]
    _CustomMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[_Any, ...], _StringTuple, _StringTuple
    ]

    _PublishPerSiteMeasurementsArg = _Union[
        float, _Sequence[float], bool, _Sequence[bool], str, _Sequence[str]
    ]


class SemiconductorModuleContext:
    """Provides a pythonic interface to an instance of ISemiconductorModuleContext.

    The Semiconductor Multi Test step creates an ISemiconductorModuleContext object that
    describes a subset of pins, relays, sites, and instruments on a test system for the instance of
    the multisite code module. Pass the Step.SemiconductorModuleContext property to the code module
    as an ISemiconductorModuleContext interface to write a test for multisite situations.
    """

    _sessions = {}

    def __init__(self, tsm_dispatch: "_ISemiconductorModuleContext"):
        """Wraps an instance of ISemiconductorModuleContext.

        Args:
            tsm_dispatch: The win32com.client.dynamic.CDispatch object provided by TestStand.
        """
        clsid = nitsm._pinmapinterfaces.ISemiconductorModuleContext.CLSID
        interface = tsm_dispatch._oleobj_.QueryInterface(clsid, pythoncom.IID_IDispatch)
        self._context = nitsm._pinmapinterfaces.ISemiconductorModuleContext(interface)

    # General and Advanced

    def get_pin_names(
        self,
        instrument_type_id: "_InstrTypeIdArg" = nitsm.enums.InstrumentTypeIdConstants.ANY,
        capability: "_CapabilityArg" = nitsm.enums.Capability.ALL,
    ) -> "_Tuple[_StringTuple, _StringTuple]":
        """Returns all DUT and system pins available in the Semiconductor Module context that are
        connected to an instrument of the type you specify in the instrument_type_id. This method
        returns only the pins specified on the Options tab of the Semiconductor Multi Test step.
        Pass an empty string to instrument_type_id to return all available pins.

        Args:
            instrument_type_id: Specifies the type of instrument for which you want to return DUT
                and system pins. All instruments defined in the pin map specify an associated type
                ID. The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type
                IDs for instrument types that TSM supports natively. For all other types of
                instruments, you must define a type ID for the instrument in the pin map file.
                Typically, this type ID is an instrument driver name or other ID that is common for
                instruments that users program in a similar way. Pass InstrumentTypeIdConstants.ANY
                to include pins from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all pins that match instrument_type_id.

        Returns:
            dut_pins: Returns a tuple of strings that contains the DUT pins in the Semiconductor
                Module context that are connected to an instrument of the type you specify in the
                instrument_type_id.
            system_pins: Returns a tuple of strings that contains the system pins in the
                Semiconductor Module context that are connected to an instrument of the type you
                specify in the instrument_type_id.
        """
        if isinstance(instrument_type_id, nitsm.enums.InstrumentTypeIdConstants):
            instrument_type_id = instrument_type_id.value
        if isinstance(capability, nitsm.enums.Capability):
            capability = capability.value
        return self._context.GetPinNames(instrument_type_id, capability, [], [])

    def filter_pins_by_instrument_type(
        self,
        pins: "_Sequence[str]",
        instrument_type_id: "_InstrTypeIdArg",
        capability: "_CapabilityArg",
    ) -> "_StringTuple":
        """Filters pins by instrument_type_id. Pass a list of all pins or pin groups to return the
        pins connected to instruments of the type you specify in the instrument_type_id. If no pins
        are connected to instruments of the type you specify in instrument_type_id, this method
        returns an empty tuple. The return value is a tuple subset of pin names in pins that are
        connected to an instrument of the filtered instrument_type_id.

        Args:
            pins: A sequence of pins or pin groups to filter. The sequence must contain only pins or
                pin groups that are included in the Semiconductor Module context.
            instrument_type_id: The type of instrument for which you want to return DUT and system
                pins. All instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way. Pass InstrumentTypeIdConstants.ANY to include pins
                from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all elements in pins that match instrument_type_id.

        Returns:
            Returns a tuple subset of pin names in the pins that are connected to an instrument of
            the filtered instrument_type_id.
        """
        if isinstance(instrument_type_id, nitsm.enums.InstrumentTypeIdConstants):
            instrument_type_id = instrument_type_id.value
        if isinstance(capability, nitsm.enums.Capability):
            capability = capability.value
        return self._context.FilterPinsByInstrumentType(pins, instrument_type_id, capability)

    def get_pins_in_pin_groups(self, pin_groups: "_PinsArg") -> "_StringTuple":
        """Returns a tuple of pins contained in the pin group(s) you specify in the pin_group(s).

        Args:
            pin_groups: A pin group or a sequence of pin groups. The pin group(s) must contain only
                pin groups that are included in the Semiconductor Module context.
        """
        if isinstance(pin_groups, str):
            pin_groups = [pin_groups]
        return self.filter_pins_by_instrument_type(pin_groups, "", "")

    @property
    def site_numbers(self) -> "_Tuple[int, ...]":
        """Returns the site numbers in the Semiconductor Module context. The site numbers can be
        different each time a step executes because some sites might not be active. The site numbers
        are in numerical order.
        """
        return self._context.SiteNumbers

    # Site and Global Data
    def get_semiconductor_module_context_with_sites(
        self, site_numbers: "_Sequence[int]"
    ) -> "SemiconductorModuleContext":
        """Returns a Semiconductor Module context object which holds information and resources
        specific to the site_numbers mentioned.

        Args:
            site_numbers: A sequence of site numbers for which the resources should be used.

        Returns:
            SemiconductorModuleContext object with resources specific to the site_numbers.
        """
        tsm_dispatch = self._context.GetSemiconductorModuleContextWithSites(site_numbers)
        semiconductor_module_context_with_sites = SemiconductorModuleContext.__new__(
            SemiconductorModuleContext
        )
        semiconductor_module_context_with_sites._context = tsm_dispatch
        return semiconductor_module_context_with_sites

    def set_site_data(self, data_id: str, data: "_Sequence[_Any]") -> None:
        """Associates a data item with each site. You can associate data with all sites or with the
        sub-set of sites in the Semiconductor Module context. You can use this method to store
        per-site data you initialize in a central location but access within each site. The data
        item is accessible from a process model controller execution and the site with which the
        data is associated. This method supports only basic data types and sequences of basic
        data types that can be represented by a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A sequence of data with one element for each site in the system or one element for
                each site in the Semiconductor Module context. If the sequence is None or empty, the
                method deletes any data with the specified data_id if it exists. If the sequence
                contains data for each site in the Semiconductor Module context, each item in the
                sequence contains data for the site specified by the corresponding item in the
                site_numbers property.
        """
        return self._context.SetSiteData(data_id, data)

    def get_site_data(self, data_id: str) -> "_Tuple[_Any, ...]":
        """Returns per-site data that a previous call to the set_site_data method stores. The
        returned tuple contains the data the Semiconductor Module context stores for each site in
        the same order as the sites that the site_numbers property returns. Raises an exception if a
        data item with the specified data_id does not exist for every site in the Semiconductor
        Module context. Use the site_data_exists method to determine if the specified data_id
        exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_site_data method.
        """
        return self._context.GetSiteData(data_id)

    def site_data_exists(self, data_id: str) -> bool:
        """Returns a Boolean value indicating whether site data exists for the data ID specified by
        the data_id . Raises an exception if a data item with the specified data_id exists for some,
        but not all, sites in the Semiconductor Module context.

        Args:
            data_id: A unique ID to distinguish the data.
        """
        return self._context.SiteDataExists(data_id)

    def set_global_data(self, data_id: str, data: "_Any") -> None:
        """Associates a data item with a data_id. You can use this method to store data you
        initialize in a central location but access from multiple sites. The data item is accessible
        from a process model controller execution and all of its test socket executions. This method
        supports only basic data types and sequences of basic data types that can be represented by
        a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A data item to store and later retrieve using the specified data_id . If the data
                item is None, the method deletes the data with the specified data_id if it exists.
        """
        return self._context.SetGlobalData(data_id, data)

    def get_global_data(self, data_id: str) -> "_Any":
        """Returns a global data item that a previous call to the set_global_data method stores.
        Throws an exception if no data item with the specified data_id exists. Use the
        global_data_exists method to determine if the specified data_id exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_global_data method.
        """
        return self._context.GetGlobalData(data_id)

    def global_data_exists(self, data_id: str) -> bool:
        """Returns a Boolean value indicating whether global data exists for the data ID specified
        by the data_id.

        Args:
            data_id: A unique ID to distinguish the data.
        """
        return self._context.GlobalDataExists(data_id)

    # NI-Digital

    def get_all_nidigital_instrument_names(self) -> "_StringTuple":
        """Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module
        context. You can use the instrument names and comma-separated lists of instrument names to
        open driver sessions.
        """
        return self._context.GetNIDigitalPatternInstrumentNames()

    def set_nidigital_session(self, instrument_name: str, session: "nidigital.Session") -> None:
        """Associates an instrument session with an NI-Digital Pattern instrument_name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument_name.
        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDigitalPatternSession(instrument_name, session_id)

    def get_all_nidigital_sessions(self) -> "_Tuple[nidigital.Session, ...]":
        """Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """
        session_ids = self._context.GetNIDigitalPatternSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nidigital_session_for_ppmu(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalSingleSessionPpmuQuery":
        """Returns the NI-Digital Pattern session and pin_set_string required to perform PPMU
        operations on pin(s). If more than one session is required to access the pin(s), the method
        raises an exception. Each group of NI-Digital Pattern instruments in the pin map creates a
        single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and pin_set_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments connected
                to pin(s) for all sites in the Semiconductor Module context.
            pin_set_string: Returns the pin set string for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin set is
                specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, pin_set_string, _ = self._context.GetNIDigitalPatternSession_2(
                pins, 0, "", ""
            )
        else:
            session_id, pin_set_string, _ = self._context.GetNIDigitalPatternSession(
                pins, 0, "", ""
            )
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, pin_set_string

    def pins_to_nidigital_sessions_for_ppmu(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalMultipleSessionPpmuQuery":
        """Returns the NI-Digital Pattern sessions and pin_set_strings required to perform PPMU
        operations on pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and
                pin_set_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            pin_set_strings: Returns the pin set strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin sets
                are specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, pin_set_strings, _ = self._context.GetNIDigitalPatternSessions_3(
                pins, [], [], []
            )
        else:
            session_ids, pin_set_strings, _ = self._context.GetNIDigitalPatternSessions_2(
                pins, [], [], []
            )
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, pin_set_strings

    def pins_to_nidigital_session_for_pattern(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalSingleSessionPatternQuery":
        """Returns the NI-Digital Pattern session and site_list required to perform pattern
        operations for patterns that use the pin(s). If more than one session is required to access
        the pin(s), the method raises an exception. Each group of NI-Digital Pattern instruments in
        the pin map creates a single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and site_list.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_list: Returns a string that is a comma-separated list of sites (e.g. "site0,site1")
                that correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        """
        if isinstance(pins, str):
            session_id, _, site_list = self._context.GetNIDigitalPatternSession_2(pins, 0, "", "")
        else:
            session_id, _, site_list = self._context.GetNIDigitalPatternSession(pins, 0, "", "")
        pin_query_context = nitsm.pinquerycontexts.DigitalPatternPinQueryContext(
            self._context, pins, site_list
        )
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, site_list

    def pins_to_nidigital_sessions_for_pattern(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalMultipleSessionPatternQuery":
        """Returns the NI-Digital Pattern sessions and site_lists required to perform pattern
        operations for patterns that use the pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and site_lists.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_lists: Returns a tuple of comma-separated lists of sites (e.g. "site0,site1") that
                correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        """
        if isinstance(pins, str):
            session_ids, _, site_lists = self._context.GetNIDigitalPatternSessions_3(
                pins, [], [], []
            )
        else:
            session_ids, _, site_lists = self._context.GetNIDigitalPatternSessions_2(
                pins, [], [], []
            )
        pin_query_context = nitsm.pinquerycontexts.DigitalPatternPinQueryContext(
            self._context, pins, site_lists
        )
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, site_lists

    @property
    def pin_map_file_path(self) -> str:
        """The absolute path to the pin map file for this Semiconductor Module context."""
        return self._context.PinMapPath

    @property
    def nidigital_project_specifications_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Specifications files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectSpecificationsFilePaths()

    @property
    def nidigital_project_levels_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Levels file in the Digital Pattern Project associated with this
        Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectLevelsFilePaths()

    @property
    def nidigital_project_timing_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Timing files in the Digital Pattern Project associated with
        this Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectTimingFilePaths()

    @property
    def nidigital_project_pattern_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Pattern files in the Digital Pattern Project associated with
        this Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectPatternFilePaths()

    @property
    def nidigital_project_source_waveform_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Source Waveform files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectSourceWaveformFilePaths()

    @property
    def nidigital_project_capture_waveform_file_paths(self) -> "_StringTuple":
        """The absolute paths to the Capture Waveform files in the Digital Pattern Project
        associated with this Semiconductor Module context.
        """
        return self._context.GetDigitalPatternProjectCaptureWaveformFilePaths()

    # NI-DCPower

    def get_all_nidcpower_resource_strings(self) -> "_StringTuple":
        """Returns the resource strings associated with each channel group in the Semiconductor
        Module context. A resource string is a comma-separated list of NI-DCPower resources, where
        each resource is defined by the <instrument>/<channel> associated with the NI-DCPower
        channel group. You can use the resource strings to open driver sessions. The same session
        controls all resources within the same resource string. This method supports only DC Power
        instruments defined with ChannelGroups in the pin map.

        Returns:
            Returns a tuple of the NI-DCPower resource strings.
        """
        return self._context.GetNIDCPowerResourceStrings()

    def set_nidcpower_session(self, resource_string: str, session: "nidcpower.Session"):
        """Associates an NI-DCPower session with all resources of an NI-DCPower resource_string.
        This method supports only DC Power instruments defined with ChannelGroups in the pin map.

        Args:
            resource_string: The resource string associated with the corresponding session. The
                resource string is a comma-separated list of resources, where each resource is
                defined as <instrument>/<channel>.
            session: The NI-DCPower session for the corresponding resource_string.
        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        # Instrument alarms are not yet supported in Python
        self._context.SetNIDCPowerSession_2(resource_string, session_id, [], 0)

    def get_all_nidcpower_sessions(self) -> "_Tuple[nidcpower.Session, ...]":
        """Returns all NI-DCPower instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """
        session_ids = self._context.GetNIDCPowerSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nidcpower_session(self, pins: "_PinsArg") -> "_NIDCPowerSingleSessionQuery":
        """Returns the NI-DCPower session and channel_string required to access the pin(s) on all
        sites in the Semiconductor Module context. If multiple sessions are required to access the
        pin(s), the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session and
                channel_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-DCPower instrument session for the instruments and channels
                connected to pin(s) for all sites in the Semiconductor Module context.
            channel_string: Returns the channel string for the NI-DCPower session required to access
                the pin(s) for all sites in the Semiconductor Module context. The channel string is
                a comma-separated list of resources, where each resource is defined as
                <instrument>/<channel>.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_string = self._context.GetNIDCPowerSession(pins, 0, "")
        else:
            session_id, channel_string = self._context.GetNIDCPowerSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_string

    def pins_to_nidcpower_sessions(self, pins: "_PinsArg") -> "_NIDCPowerMultipleSessionQuery":
        """Returns the NI-DCPower sessions and channel_strings required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions and
                channel_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-DCPower instrument sessions for the instruments and channel
                resources connected to pin(s) for all sites in the Semiconductor Module context.
            channel_strings: Returns the channel strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. Each channel
                string is a comma-separated list of channels, where each channel is defined as
                <instrument>/<channel>.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_strings = self._context.GetNIDCPowerSessions_2(pins, [], [])
        else:
            session_ids, channel_strings = self._context.GetNIDCPowerSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_strings

    # NI-DAQmx

    def get_all_nidaqmx_task_names(self, task_type: str) -> "_Tuple[_StringTuple, _StringTuple]":
        """Returns a tuple of all NI-DAQmx task names and channel lists in the Semiconductor Module
        context. You can use the task names to create DAQmx tasks.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.

        Returns:
            task_names: Returns a tuple of the NI-DAQmx task names.
            channel_lists: Returns a tuple of the NI-DAQmx physical channel names for all channels
                in the Semiconductor Module context.
        """
        return self._context.GetNIDAQmxTaskNames(task_type, [])

    def set_nidaqmx_task(self, task_name: str, task: "nidaqmx.Task") -> None:
        """Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.

        Args:
            task_name: The task name in the pin map file for the corresponding task.
            task: The DAQmx task for the corresponding task name.
        """
        task_id = id(task)
        SemiconductorModuleContext._sessions[task_id] = task
        return self._context.SetNIDAQmxTask(task_name, task_id)

    def get_all_nidaqmx_tasks(self, task_type: str) -> "_Tuple[nidaqmx.Task, ...]":
        """Returns a tuple of all NI-DAQmx tasks in the Semiconductor Module context whose task type
        matches task_type. You can use tasks to perform NI-DAQmx operations.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.
        """
        task_ids = self._context.GetNIDAQmxTasks(task_type)
        return tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)

    def pins_to_nidaqmx_task(self, pins: "_PinsArg") -> "_NIDAQmxSingleSessionQuery":
        """Returns the NI-DAQmx task and available channels list required to access the pin(s). If
        more than one task is required, the method raises an exception.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a task.

        Returns:
            pin_query_context: An object that tracks the task associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            task: Returns the NI-DAQmx task associated with the pin(s) or pin group(s) for all sites
                in the Semiconductor Module context.
            channel_list: Returns the comma-separated list of channels in the task associated with
                the pin(s) or pin group(s) for all sites in the Semiconductor Module context. Use
                the channel list to set the channels to read from for an input task or as an input
                to one of the per task data methods associated with this pin query context for an
                output task. If any of the pins are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            task_id, channel_list = self._context.GetNIDAQmxTask(pins, 0, "")
        else:
            task_id, channel_list = self._context.GetNIDAQmxTask_2(pins, 0, "")
        task = SemiconductorModuleContext._sessions[task_id]
        return pin_query_context, task, channel_list

    def pins_to_nidaqmx_tasks(self, pins: "_PinsArg") -> "_NIDAQmxMultipleSessionQuery":
        """Returns the NI-DAQmx tasks and available channels lists required to access the pin(s) or
        pin group(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a set of tasks.

        Returns:
            pin_query_context: An object that tracks the tasks associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            tasks: Returns the NI-DAQmx tasks associated with the pin(s) or pin group(s) for all
                sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated lists of channels in the tasks associated
                with the pin(s) or pin group(s) for all sites in the Semiconductor Module context.
                Use the channel lists to set the channels to read from for input tasks or as an
                input to one of the per task data methods associated with this pin query context for
                output tasks. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            task_ids, channel_lists = self._context.GetNIDAQmxTasks_2(pins, [], [])
        else:
            task_ids, channel_lists = self._context.GetNIDAQmxTasks_3(pins, [], [])
        tasks = tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)
        return pin_query_context, tasks, channel_lists

    # NI-DMM

    def get_all_nidmm_instrument_names(self) -> "_StringTuple":
        """Returns a tuple of all NI-DMM instrument names in the Semiconductor Module context. You
        can use instrument names to open driver sessions.
        """
        return self._context.GetNIDmmInstrumentNames()

    def set_nidmm_session(self, instrument_name: str, session: "nidmm.Session") -> None:
        """Associates an instrument session with an NI-DMM instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDmmSession(instrument_name, session_id)

    def get_all_nidmm_sessions(self) -> "_Tuple[nidmm.Session, ...]":
        """Returns a tuple of all NI-DMM instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """
        session_ids = self._context.GetNIDmmSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nidmm_session(self, pin: str) -> "_NIDmmSingleSessionQuery":
        """Returns the NI-DMM session required to access the pin. If more than one session is
        required, the method raises an exception.

        Args:
            pin: The name of the pin to translate to an instrument session. If more than one session
            is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-DMM instrument session for the instrument connected to the pin
                for all sites in the Semiconductor Module context.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pin)
        session_id = self._context.GetNIDmmSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session

    def pins_to_nidmm_sessions(self, pins: "_PinsArg") -> "_NIDmmMultipleSessionQuery":
        """Returns the NI-DMM instrument sessions required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to instrument sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-DMM instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids = self._context.GetNIDmmSessions_2(pins)
        else:
            session_ids = self._context.GetNIDmmSessions_3(pins)
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions

    # NI-FGEN

    def get_all_nifgen_instrument_names(self) -> "_StringTuple":
        """Returns a tuple of all NI-FGEN instrument names in the Semiconductor Module context. You
        can use the instrument names to open driver sessions.
        """
        return self._context.GetNIFGenInstrumentNames()

    def set_nifgen_session(self, instrument_name: str, session: "nifgen.Session") -> None:
        """Associates an instrument session with an NI-FGEN instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIFGenSession(instrument_name, session_id)

    def get_all_nifgen_sessions(self) -> "_Tuple[nifgen.Session, ...]":
        """Returns a tuple of all NI-FGEN instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """
        session_ids = self._context.GetNIFGenSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nifgen_session(self, pins: "_PinsArg") -> "_NIFGenSingleSessionQuery":
        """Returns the NI-FGEN session and channel list required to access the pin(s). If more than
        one session is required, the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-FGEN instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_list = self._context.GetNIFGenSession(pins, 0, "")
        else:
            session_id, channel_list = self._context.GetNIFGenSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_nifgen_sessions(self, pins: "_PinsArg") -> "_NIFGenMultipleSessionQuery":
        """Returns the NI-FGEN sessions and channel lists required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-FGEN instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_lists = self._context.GetNIFGenSessions_2(pins, [], [])
        else:
            session_ids, channel_lists = self._context.GetNIFGenSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_lists

    # NI-SCOPE

    def get_all_niscope_instrument_names(self) -> "_StringTuple":
        """Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context.
        You can use the instrument names and comma-separated lists of instrument names to open
        driver sessions.
        """
        return self._context.GetNIScopeInstrumentNames()

    def set_niscope_session(self, instrument_name: str, session: "niscope.Session") -> None:
        """Associates an instrument session with an NI-SCOPE instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIScopeSession(instrument_name, session_id)

    def get_all_niscope_sessions(self) -> "_Tuple[niscope.Session, ...]":
        """Returns a tuple of all NI-SCOPE instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """
        session_ids = self._context.GetNIScopeSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_niscope_session(self, pins: "_PinsArg") -> "_NIScopeSingleSessionQuery":
        """Returns the NI-SCOPE session and channel list required to access the pin(s). If more than
        one session is required to access the pin(s), the method raises an exception. Each group of
        NI-SCOPE instruments in the pin map creates a single instrument session.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-SCOPE instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_list = self._context.GetNIScopeSession(pins, 0, "")
        else:
            session_id, channel_list = self._context.GetNIScopeSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_niscope_sessions(self, pins: "_PinsArg") -> "_NIScopeMultipleSessionQuery":
        """Returns the NI-SCOPE sessions and channel lists required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-SCOPE instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_lists = self._context.GetNIScopeSessions_2(pins, [], [])
        else:
            session_ids, channel_lists = self._context.GetNIScopeSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_lists

    # Switching

    def get_all_switch_names(self, multiplexer_type_id: "_InstrTypeIdArg") -> "_StringTuple":
        """Returns the names of all switches of the type specified by the multiplexer_type_id in the
        Semiconductor Module context. You can use switch names to open driver sessions.

        Args:
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        """
        if isinstance(multiplexer_type_id, nitsm.enums.InstrumentTypeIdConstants):
            multiplexer_type_id = multiplexer_type_id.value
        return self._context.GetSwitchNames(multiplexer_type_id)

    def set_switch_session(
        self, switch_name: str, session_data: "_Any", multiplexer_type_id: "_InstrTypeIdArg"
    ) -> None:
        """Associates an open switch session with the switch_name for a multiplexer of type
        multiplexer_type_id.

        Args:
            switch_name: The instrument name in the pin map file for the corresponding session_data.
            session_data: The instrument session for the corresponding switch_name and
                multiplexer_type_id.
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        """
        if isinstance(multiplexer_type_id, nitsm.enums.InstrumentTypeIdConstants):
            multiplexer_type_id = multiplexer_type_id.value
        session_id = id(session_data)
        self._sessions[session_id] = session_data
        return self._context.SetSwitchSession(multiplexer_type_id, switch_name, session_id)

    def get_all_switch_sessions(self, multiplexer_type_id: "_InstrTypeIdArg") -> "_AnyTuple":
        """Returns a tuple of all switch session data of the type specified by the
        multiplexer_type_id in the Semiconductor Module context.

        Args:
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        """
        if isinstance(multiplexer_type_id, nitsm.enums.InstrumentTypeIdConstants):
            multiplexer_type_id = multiplexer_type_id.value
        session_ids = self._context.GetSwitchSessions(multiplexer_type_id)
        return tuple(map(SemiconductorModuleContext._sessions.get, session_ids))

    def pin_to_switch_sessions(
        self, pin: str, multiplexer_type_id: "_InstrTypeIdArg"
    ) -> "_SwitchQuery":
        """Returns the switch sessions, switch routes, and new Semiconductor Module context objects
        required to access the specified switched pin.

        Args:
            pin: The name of the pin to translate to session data and switch routes.
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.

        Returns:
            semiconductor_module_contexts: A tuple of Semiconductor Module context objects. Each
                element in the tuple represents a site that must be executed serially. Use each
                Semiconductor Module context object to query the pin map and publish data.
            session_data: A tuple of the session data required to access the switch that connects an
                instrument channel to the pin.
            switch_routes: The routes required to connect an instrument channel to the pin.
        """
        if isinstance(multiplexer_type_id, nitsm.enums.InstrumentTypeIdConstants):
            multiplexer_type_id = multiplexer_type_id.value
        # We have to use DumbDispatch here because pywin32 fails to recognize
        # ISemiconductorModuleContext as deriving from IDispatch; most likely because it isn't
        # natively supported. So, we fetch it as IUnknown instead.
        vt_by_ref_array = pythoncom.VT_BYREF | pythoncom.VT_ARRAY
        site_contexts = win32com.client.VARIANT(vt_by_ref_array | pythoncom.VT_UNKNOWN, [])
        sessions = win32com.client.VARIANT(vt_by_ref_array | pythoncom.VT_VARIANT, [])
        switch_routes = win32com.client.VARIANT(vt_by_ref_array | pythoncom.VT_BSTR, [])
        dumb_context = win32com.client.dynamic.DumbDispatch(self._context)
        dumb_context.GetSwitchSessions_2(
            multiplexer_type_id, pin, site_contexts, sessions, switch_routes
        )
        # As of pywin32 303, there is a bug where SAFEARRAYs of IUnknown pointers leak references.
        # See here: https://github.com/mhammond/pywin32/issues/1864
        # As a work-around, we decrement the reference count until the only one left is held by
        # Python. It will be released when the object is garbage collected.
        add_ref = ctypes.WINFUNCTYPE(ctypes.wintypes.ULONG)(1, "AddRef")
        release = ctypes.WINFUNCTYPE(ctypes.wintypes.ULONG)(2, "Release")
        for site_context in site_contexts.value:
            # address of IUnknown has to be parsed from the repr
            # https://github.com/mhammond/pywin32/blob/main/com/win32com/src/PyIUnknown.cpp
            address = ctypes.c_void_p(int(repr(site_context).split()[-1][:-1], 16))
            # first add a reference in case the bug has been fixed; prevents count from reaching 0
            add_ref(address)
            # then release the reference until only one remains
            while release(address) > 1:
                pass
        site_contexts = map(win32com.client.dynamic.DumbDispatch, site_contexts.value)
        site_contexts = tuple(map(SemiconductorModuleContext, site_contexts))
        sessions = tuple(map(SemiconductorModuleContext._sessions.get, sessions.value))
        return site_contexts, sessions, switch_routes.value

    # Relay Driver

    def get_relay_driver_module_names(self) -> "_StringTuple":
        """Returns a tuple of all relay driver module names in the Semiconductor Module context. You
        can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver
        modules.
        """
        return self._context.GetNIRelayDriverModuleNames()

    def get_relay_names(self) -> "_Tuple[_StringTuple, _StringTuple]":
        """Returns all site and system relays available in the Semiconductor Module context.

        Returns:
            site_relays: Returns a tuple of strings that contains the site relays in the
                Semiconductor Module context.
            system_relays: Returns a tuple of strings that contains the system relays in the
                Semiconductor Module context.
        """
        return self._context.GetRelayNames([], [])

    def set_relay_driver_niswitch_session(
        self, relay_driver_module_name: str, niswitch_session: "niswitch.Session"
    ) -> None:
        """Associates an NI-SWITCH session with a relay driver module.

        Args:
            relay_driver_module_name: The relay driver module name in the pin map file for the
                corresponding session.
            niswitch_session: The NI-SWITCH session for the corresponding relay driver module name.
        """
        session_id = id(niswitch_session)
        SemiconductorModuleContext._sessions[session_id] = niswitch_session
        return self._context.SetNIRelayDriverSession(relay_driver_module_name, session_id)

    def get_all_relay_driver_niswitch_sessions(self) -> "_Tuple[niswitch.Session, ...]":
        """Returns a tuple of NI-SWITCH sessions for all relay driver modules in the Semiconductor
        Module context. You can use the NI-SWITCH sessions to close the relay driver module
        sessions.
        """
        session_ids = self._context.GetNIRelayDriverSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def relays_to_relay_driver_niswitch_session(
        self, relays: "_PinsArg"
    ) -> "_RelayDriverSingleSessionQuery":
        """Returns the NI-SWITCH session and relay names required to access the relay(s) connected
        to a relay driver module. If more than one session is required to access the relay(s), the
        method raises an exception.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to an NI-SWITCH
                session and NI-SWITCH relay names.

        Returns:
            niswitch_session: Returns the NI-SWITCH session for the relay driver module connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns a comma-separated list of NI-SWITCH relay names for the
                relay driver module session connected to the relay(s) for all sites in the
                Semiconductor Module context.
        """
        if isinstance(relays, str):
            session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession(relays, 0, "")
        else:
            session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession_2(
                relays, 0, ""
            )
        niswitch_session = SemiconductorModuleContext._sessions[session_id]
        return niswitch_session, niswitch_relay_names

    def relays_to_relay_driver_niswitch_sessions(
        self, relays: "_PinsArg"
    ) -> "_RelayDriverMultipleSessionQuery":
        """Returns the NI-SWITCH sessions and relay names required to access the relay(s) connected
        to a relay driver module.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to NI-SWITCH sessions
                and NI-SWITCH relay names.

        Returns:
            niswitch_sessions: Returns NI-SWITCH sessions for the relay driver modules connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns comma-separated lists of NI-SWITCH relay names for the
                relay driver module sessions connected to the relay(s) for all sites in the
                Semiconductor Module context.
        """
        if isinstance(relays, str):
            session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_2(
                relays, [], []
            )
        else:
            session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_3(
                relays, [], []
            )
        niswitch_sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return niswitch_sessions, niswitch_relay_names

    @staticmethod
    def _apply_relay_action(
        session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
    ):
        from niswitch.enums import RelayAction

        for session_id_to_open, relay_name_to_open in zip(
            session_ids_for_open, relay_names_to_open
        ):
            session_to_open = SemiconductorModuleContext._sessions[session_id_to_open]
            session_to_open.relay_control(relay_name_to_open, RelayAction.OPEN)
        for session_id_to_close, relay_name_to_close in zip(
            session_ids_for_close, relay_names_to_close
        ):
            session_to_close = SemiconductorModuleContext._sessions[session_id_to_close]
            session_to_close.relay_control(relay_name_to_close, RelayAction.CLOSE)
        return None

    def _relay_wait(self, wait_seconds):
        if wait_seconds == 0.0:
            return None
        elif wait_seconds > 0.0:
            time.sleep(wait_seconds)
        else:
            self._context.ReportInvalidTimeToWait("wait_seconds")
        return None

    def apply_relay_configuration(self, relay_configuration: str, wait_seconds=0.0) -> None:
        """Performs the relay actions on the relays in the relay configuration.

        Args:
            relay_configuration: The name of the relay configuration to apply.
            wait_seconds: The time to wait, in seconds, for the relays to settle after performing
                all relay actions.
        """
        (
            session_ids_for_open,
            relay_names_to_open,
            session_ids_for_close,
            relay_names_to_close,
        ) = self._context.GetRelayDriverSessionsFromRelayConfiguration(
            relay_configuration, [], [], [], []
        )
        self._apply_relay_action(
            session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
        )
        self._relay_wait(wait_seconds)
        return None

    def _control_relays_single_action(self, relays, relay_action, wait_seconds=0.0):
        niswitch_sessions, relay_names = self.relays_to_relay_driver_niswitch_sessions(relays)
        for niswitch_session, niswitch_relay_name in zip(niswitch_sessions, relay_names):
            niswitch_session.relay_control(niswitch_relay_name, relay_action)
        self._relay_wait(wait_seconds)
        return None

    def _control_relays_multiple_action(self, relays, relay_actions, wait_seconds=0.0):
        if len(relays) != len(relay_actions):
            self._context.ReportIncompatibleArrayLengths("relays", "relay_actions")
        else:
            relay_actions = [relay_action.value for relay_action in relay_actions]
            (
                session_ids_for_open,
                relay_names_to_open,
                session_ids_for_close,
                relay_names_to_close,
            ) = self._context.GetRelayDriverSessionsFromRelays(
                relays, relay_actions, [], [], [], []
            )
            self._apply_relay_action(
                session_ids_for_open,
                relay_names_to_open,
                session_ids_for_close,
                relay_names_to_close,
            )
            self._relay_wait(wait_seconds)
        return None

    def control_relays(
        self,
        relays: "_PinsArg",
        relay_actions: "_Union[niswitch.RelayAction, _Sequence[niswitch.RelayAction]]",
        wait_seconds=0.0,
    ) -> None:
        """Performs the relay action(s) on the relay(s).

        Args:
            relays: The name(s) of the relay(s) or relay group(s) that identify the relays.
            relay_actions: The action(s) to perform on all identified relays.
            wait_seconds: The time to wait, in seconds, for the relay(s) to settle after performing
                the relay action(s).
        """
        if isinstance(relay_actions, (list, tuple)):
            return self._control_relays_multiple_action(relays, relay_actions, wait_seconds)
        else:
            return self._control_relays_single_action(relays, relay_actions, wait_seconds)

    # Custom Instruments

    def get_custom_instrument_names(
        self, instrument_type_id: "_InstrTypeIdArg"
    ) -> "_Tuple[_StringTuple, _StringTuple, _StringTuple]":
        """Returns the channel_group_ids and associated instrument_names and channel_lists of all
        instruments of type instrument_type_id defined in the Semiconductor Module context. You can
        use instrument_names, channel_group_ids, and channel_lists to open driver sessions. The
        instrument_names, channel_group_ids, and channel_lists return values always return the same
        number of elements. Instrument names repeat in instrument_names if the instrument has
        multiple channel groups.

        Args:
            instrument_type_id: The type of instrument for which you want to return instrument
                definitions. All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            instrument_names: Returns the names of all instruments in the Semiconductor Module
                context that are of type instrument_type_id.
            channel_group_ids: Returns the IDs of all channel groups in the Semiconductor Module
                context that belong to an instrument of type instrument_type_id. For channels that
                do not belong to a channel group in the pin map, the Semiconductor Module creates a
                channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each element of channel_group_ids. Each
                channel list is a comma-separated list of channels.
        """
        return self._context.GetAllInstrumentDefinitions(instrument_type_id, [], [], [])

    def set_custom_session(
        self,
        instrument_type_id: str,
        instrument_name: str,
        channel_group_id: str,
        session_data: "_Any",
    ) -> None:
        """Associates a session with an instrument and channel group.

        Args:
            instrument_type_id: The type of instrument for which you want to set the session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            instrument_name: The instrument name in the pin map file for the corresponding session.
                The instrument must be of type instrument_type_id.
            channel_group_id: The channel group in the pin map file for the corresponding session.
                For channels that do not belong to a channel group in the pin map, the Semiconductor
                Module creates a channel group with the same ID as the channel.
            session_data: The session for the corresponding instrument_name and channel_group_id.
        """
        session_id = id(session_data)
        SemiconductorModuleContext._sessions[session_id] = session_data
        self._context.SetSessionData(
            instrument_type_id, instrument_name, channel_group_id, session_id
        )
        return None

    def get_all_custom_sessions(
        self, instrument_type_id: "_InstrTypeIdArg"
    ) -> "_Tuple[_Tuple[_Any, ...], _StringTuple, _StringTuple]":
        """Returns all set sessions in the Semiconductor Module context that belong to instruments
        of type instrument_type_id.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            session_data: Returns a tuple of session data set in the Semiconductor Module context.
            channel_group_ids: Returns the IDs of the channel groups on which session_data was
                stored. For channels that do not belong to a channel group in the pin map, the
                Semiconductor Module creates a channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each of the channel_group_ids. Each channel
                list is a comma-separated list of channels.
        """
        session_ids, channel_group_ids, channel_lists = self._context.GetAllSessionData(
            instrument_type_id, [], [], []
        )
        session_data = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return session_data, channel_group_ids, channel_lists

    def pins_to_custom_session(
        self, instrument_type_id: "_InstrTypeIdArg", pins: "_PinsArg"
    ) -> "_CustomSingleSessionQuery":
        """Returns the session in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get a session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_id, and channel_list. The pin(s) must be connected to an instrument of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns the session data associated with pin(s).
            channel_group_id: Returns the ID of the channel group(s) that contain(s) the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_list: Returns the channel list that corresponds to pin(s) associated with
                session_data and channel_group_id. The channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_group_id, channel_list = self._context.GetSessionData_2(
                instrument_type_id, [pins], 0, "", ""
            )
        else:
            session_id, channel_group_id, channel_list = self._context.GetSessionData_2(
                instrument_type_id, pins, 0, "", ""
            )
        session_data = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session_data, channel_group_id, channel_list

    def pins_to_custom_sessions(
        self, instrument_type_id: "_InstrTypeIdArg", pins: "_PinsArg"
    ) -> "_CustomMultipleSessionQuery":
        """Returns all sessions in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_ids, and channel_lists. The pin(s) must be connected to instruments of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns a tuple of session data associated with pin(s).
            channel_group_ids: Returns the IDs of the channel groups that contain the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_lists: Returns the channel lists that correspond to the pin(s) associated with
                session_data and channel_group_ids. Each channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """
        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_group_ids, channel_lists = self._context.GetSessionData(
                instrument_type_id, [pins], [], [], []
            )
        else:
            session_ids, channel_group_ids, channel_lists = self._context.GetSessionData(
                instrument_type_id, pins, [], [], []
            )
        session_data = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, session_data, channel_group_ids, channel_lists

    def publish_per_site(
        self, measurements: "_PublishPerSiteMeasurementsArg", published_data_id="", pin=""
    ) -> None:
        """Publishes measurements from multiple sites for the Semiconductor Multi Test step to
        consume. Use this method when you want to publish data for multiple sites in the same order
        in which the sites are defined in the Semiconductor Module context.

        Args:
            measurements: The measurement data for all sites in the Semiconductor Module context.
                The number of elements passed to this parameter must be equal to the size of the
                site_numbers property. You must return results in the same order as the sites in the
                Semiconductor Module context. Use the site_numbers property to obtain the list of
                site numbers.
            published_data_id: The unique ID for distinguishing the measurement when you publish
                multiple measurements within the same code module.
            pin: The name of the pin associated with the data. This parameter must match a value you
                specify in the Pin column on the Tests tab of the Semiconductor Multi Test step. If
                you pass a blank pin, you don't have to specify a pin name in the Tests tab.
        """
        if isinstance(measurements, bool):
            self._context.PublishPerSite_5(pin, published_data_id, measurements)
        elif isinstance(measurements, (float, int)):
            self._context.PublishPerSite_4(pin, published_data_id, measurements)
        elif isinstance(measurements, str):
            self._context.PublishPerSite_6(pin, published_data_id, measurements)
        elif isinstance(measurements[0], bool):
            self._context.PublishPerSite_2(pin, published_data_id, measurements)
        elif isinstance(measurements[0], (float, int)):
            self._context.PublishPerSite(pin, published_data_id, measurements)
        else:  # default to Sequence[str]
            self._context.PublishPerSite_3(pin, published_data_id, measurements)
        return None

    # Specifications

    def get_specifications_value(self, namespaced_symbol: str) -> str:
        """Returns the value calculated for the namespaced_symbol in the Semiconductor Module
        context specifications file. Raises an exception when the associated specifications file or
        symbol cannot be found.
        """
        return self._context.GetSpecValue(namespaced_symbol)

    def get_specifications_values(self, namespaced_symbols: "_Sequence[str]") -> "_StringTuple":
        """Returns the values calculated for the namespaced_symbols in the Semiconductor Module
        context specifications file. Raises an exception when the associated specifications file or
        any symbol cannot be found.
        """
        return self._context.GetSpecValues(namespaced_symbols)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=STATUS.md sha256=393a9e8ff68bcfc860d28465955c2107a013a25ecfae50abde9317bb0d5dd0f0 bytes=21476 -->
## FILE: STATUS.md

- repository: `ni/nitsm-python`
- source_path: `STATUS.md`
- sha256: `393a9e8ff68bcfc860d28465955c2107a013a25ecfae50abde9317bb0d5dd0f0`
- bytes: 21476

````markdown
# Status
## Instrument Based Session API
(Excluding HSDIO)

| Instrument Type | .NET Method                                                             | Python                                          | Python System Tests       |
|-----------------|-------------------------------------------------------------------------|-------------------------------------------------|---------------------------|
| NI-DAQmx        | GetNIDAQmxTaskNames                                                     | get\_all\_nidaqmx\_task\_names                  | test\_nidaqmx             |
| NI-DAQmx        | SetNIDAQmxTask                                                          | set\_nidaqmx\_task                              | test\_nidaqmx             |
| NI-DAQmx        | GetNIDAQmxTask(s)                                                       | pins\_to\_nidaqmx\_task(s)                      | test\_nidaqmx             |
| NI-DAQmx        | GetAllNIDAQmxTasks                                                      | get\_all\_nidaqmx\_tasks                        | test\_nidaqmx             |
| NI-DCPower      | GetNIDCPowerInstrumentNames                                             | *omitted on purpose                             |                           |
| NI-DCPower      | GetNIDCPowerResourceStrings                                             | get\_all\_nidcpower\_resource\_strings          | test\_nidcpower           |
| NI-DCPower      | GetNIDCPowerSession(s)                                                  | pins\_to\_nidcpower\_session(s)                 | test\_nidcpower           |
| NI-DCPower      | SetNIDCPowerSession (name/channel)                                      | *omitted on purpose                             |                           |
| NI-DCPower      | SetNIDCPowerSession (resourceString)                                    | set\_nidcpower\_session                         | test\_nidcpower           |
| NI-DCPower      | GetAllNIDCPowerSessions                                                 | get\_all\_nidcpower\_sessions                   | test\_nidcpower           |
| NI-Digital      | GetNIDigitalPatternInstrumentNames                                      | get\_all\_nidigital\_instrument\_names          | test\_nidigital           |
| NI-Digital      | GetNIDigitalPatternSession(s)                                           | \*omitted on purpose                            |                           |
| NI-Digital      | GetNIDigitalPatternSession(s)ForPattern                                 | get\_nidigital\_session\_for\_pattern           | test\_nidigital           |
| NI-Digital      | GetNIDigitalPatternSession(s)ForPpmu                                    | get\_nidigital\_session\_for\_ppmu              | test\_nidigital           |
| NI-Digital      | SetNIDigitalPatternSession                                              | set\_nidigital\_session                         | test\_nidigital           |
| NI-Digital      | GetAllNIDigitalPatternSessions                                          | get\_all\_nidigital\_sessions                   | test\_nidigital           |
| NI-Digital      | FetchMultisiteHistoryRamInformation\*<br/>\*NI-Digital driver extension |                                                 |                           |
| NI-Digital      | NIDigitalHistoryRamCycleInformation\*<br/>\*class to support HRAM data  |                                                 |                           |
| NI-DMM          | GetNIDmmInstrumentNames                                                 | get\_all\_nidmm\_instrument\_names              | test\_nidmm               |
| NI-DMM          | GetNIDmmSession(s)                                                      | pin\_to\_nidmm\_session(s)                      | test\_nidmm               |
| NI-DMM          | SetNIDmmSession                                                         | set\_nidmm\_session                             | test\_nidmm               |
| NI-DMM          | GetAllNIDmmSessions                                                     | get\_all\_nidmm\_sessions                       | test\_nidmm               |
| NI-FGEN         | GetNIFGenInstrumentNames                                                | get\_all\_nifgen\_instrument\_names             | test\_nifgen              |
| NI-FGEN         | GetNIFgenSession(s)                                                     | pins\_to\_nifgen\_session(s)                    | test\_nifgen              |
| NI-FGEN         | SetNIFGenSession                                                        | set\_nifgen\_session                            | test\_nifgen              |
| NI-FGEN         | GetAllNIFGenSessions                                                    | get\_all\_nifgen\_sessions                      | test\_nifgen              |
| NI-RFmx         | GetNIRfmxInstrumentNames                                                |                                                 |                           |
| NI-RFmx         | GetNIRfmxMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFmx         | GetNIRfmxSingleDeembeddingData                                          |                                                 |                           |
| NI-RFmx         | GetNIRfmxSession(s)                                                     |                                                 |                           |
| NI-RFmx         | SetNIRfmxSession                                                        |                                                 |                           |
| NI-RFmx         | GetAllNIRFmxSessions                                                    |                                                 |                           |
| NI-RFPM         | GetNIRfpmInstrumentNames                                                |                                                 |                           |
| NI-RFPM         | GetNIRfpmSessions                                                       |                                                 |                           |
| NI-RFPM         | SetNIRfpmSession                                                        |                                                 |                           |
| NI-RFPM         | GetAllNIRfpmSessions                                                    |                                                 |                           |
| NI-RFSA         | GetNIRfsaInstrumentNames                                                |                                                 |                           |
| NI-RFSA         | GetNIRfsaMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFSA         | GetNIRfsaSingleDeembeddingData                                          |                                                 |                           |
| NI-RFSA         | GetNIRfsaSession(s)                                                     |                                                 |                           |
| NI-RFSA         | SetNIRfsaSession                                                        |                                                 |                           |
| NI-RFSA         | GetAllNIRfsaSessions                                                    |                                                 |                           |
| NI-RFSG         | GetNIRfsgInstrumentNames                                                |                                                 |                           |
| NI-RFSG         | GetNIRfsgMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFSG         | GetNIRfsgSingleDeembeddingData                                          |                                                 |                           |
| NI-RFSG         | GetNIRfsgSession(s)                                                     |                                                 |                           |
| NI-RFSG         | SetNIRfsgSession                                                        |                                                 |                           |
| NI-RFSG         | GetAllNIRfsgSessions                                                    |                                                 |                           |
| NI-Scope        | GetNIScopeInstrumentNames                                               | get\_all\_niscope\_instrument\_names            | test\_niscope             |
| NI-Scope        | GetNIScopeSession(s)                                                    | pins\_to\_niscope\_session(s)                   | test\_niscope             |
| NI-Scope        | SetNIScopeSession                                                       | set\_niscope\_session                           | test\_niscope             |
| NI-Scope        | GetAllNIScopeSessions                                                   | get\_all\_niscope\_sessions                     | test\_niscope             |
| FPGA            | GetFpgaInstrumentNames                                                  |                                                 |                           |
| FPGA            | SetFpgaVIReference                                                      |                                                 |                           |
| FPGA            | GetFpgaVIReference(s)                                                   |                                                 |                           |
| FPGA            | GetAllFpgaVIReferences                                                  |                                                 |                           |
| Relay Driver    | GetRelayDriverModuleNames                                               | get\_relay\_driver\_module\_names               | test\_nirelaydriver       |
| Relay Driver    | GetRelayDriverNISwitchSession(s)                                        | relays\_to\_relay\_driver\_niswitch\_session(s) | test\_nirelaydriver       |
| Relay Driver    | SetRelayDriverNISwitchSession                                           | set\_relay\_driver\_niswitch\_session           | test\_nirelaydriver       |
| Relay Driver    | GetAllRelayDriverNISwitchSessions                                       | get\_all\_relay\_driver\_niswitch\_sessions     | test\_nirelaydriver       |
| Relay Driver    | ControlRelay                                                            | control_relays                                  | unit test suffices        |
| Relay Driver    | ApplyRelayConfiguration                                                 | apply_relay_configuration                       | unit test suffices        |
| Custom          | GetCustomInstrumentNames                                                | get\_custom\_instrument\_names                  | test\_custom\_instruments |
| Custom          | SetCustomSession                                                        | set\_custom\_session                            | test\_custom\_instruments |
| Custom          | GetCustomSession(s)                                                     | pins\_to\_custom\_session(s)                    | test\_custom\_instruments |
| Custom          | GetAllCustomSessions                                                    | get\_all\_custom\_sessions                      | test\_custom\_instruments |
| Multiplexer     | GetSwitchNames                                                          | get\_all\_switch\_names                         | test\_switch              |
| Multiplexer     | SetSwitchSession                                                        | set\_switch\_session                            | test\_switch              |
| Multiplexer     | GetSwitchSession(s)                                                     | pin\_to\_switch\_sessions                       | test\_switch              |
| Multiplexer     | GetAllSwitchSessions                                                    | get\_all\_switch\_sessions                      | test\_switch              |

## Pin Query API
| Class                           | .NET Method                                    | Python                                                                                             | Python System Tests |
|---------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------|
| SemiconductorModuleContext      | PublishPerSite                                 | publish\_per\_site                                                                                 |                     |
| SemiconductorModuleContext      | PublishToTestStandVariablePerSite              |                                                                                                    |                     |
| PinQueryContext                 | ExtractPinData                                 |                                                                                                    |                     |
| PinQueryContext                 | PerInstrumentToPerSiteData                     |                                                                                                    |                     |
| PinQueryContext                 | GetSessionAndChannelIndex                      | get\_session\_and\_channel\_index                                                                  | unit test suffices  |
| MultiplePinQueryContext         | PerInstrumentToPerSiteData                     |                                                                                                    |                     |
| \_\_SingleSessionQueryContext   | Publish                                        | publish\*<br/>\*supports all variations of data types (float/bool) and number of pins and sessions | various             |
| \_\_MultipleSessionQueryContext | Publish                                        | publish                                                                                            | various             |
| NIDigitalPatternPinQueryContext | PublishPatternResults                          | publish\_pattern\_results                                                                          | test\_nidigital     |
| NIDigitalPatternPinQueryContext | PerInstrumentToPerSitePatternResults           |                                                                                                    |                     |
| NIDigitalPatternPinQueryContext | PerInstrumentToPerSiteWaveforms                |                                                                                                    |                     |
| NIDigitalPatternPinQueryContext | PerSiteToPerInstrumentWaveforms                |                                                                                                    |                     |
| NIDAQmxPinQueryContext          | CreateMultisiteDataForDAQmxAnalogOutput        |                                                                                                    |                     |
| NIDAQmxPinQueryContext          | CreatePerSiteMultisiteDataForDAQmxAnalogOutput |                                                                                                    |                     |

## Other
| Category/Palette     | .NET Method                                   | Python                                             | Python System Tests  |
|----------------------|-----------------------------------------------|----------------------------------------------------|----------------------|
| Specifications       | GetSpecificationsValue                        | get\_specifications\_value                         | test_specifications  |
| Specifications       | GetSpecificationsValues                       | get\_specifications\_values                        | test_specifications  |
| Site and Global Data | GetGlobalData                                 | get\_global\_data                                  | test_site_and_global |
| Site and Global Data | GetSiteData                                   | get\_site\_data                                    | test_site_and_global |
| Site and Global Data | GlobalDataExists                              | global\_data\_exists                               | test_site_and_global |
| Site and Global Data | SetGlobalData                                 | set\_global\_data                                  | test_site_and_global |
| Site and Global Data | SetSiteData                                   | set\_site\_data                                    | test_site_and_global |
| Site and Global Data | SiteDataExists                                | site\_data\_exists                                 | test_site_and_global |
| Advanced             | GetSemiconductorModuleContextWithSites        |                                                    |                      |
| Advanced             | GetSiteSemiconductorModuleContext             |                                                    |                      |
| Misc                 | FilterPinsByInstrumentType                    | filter\_pins\_by\_instrument\_type                 | unit test suffices   |
| Misc                 | GetPins                                       | get\_pin\_names                                    | unit test suffices   |
| Misc                 | GetPinsInPinGroup(s)                          | get\_pins\_in\_pin\_groups                         | unit test suffices   |
| Misc                 | GetRelays                                     | get\_relay\_names                                  | unit test suffices   |
| Misc                 | GetRelaysInRelayGroups                        |                                                    |                      |
| Misc                 | IsSemiconductorModuleInOfflineMode            |                                                    |                      |
| Misc                 | PinMapFilePath                                | pin\_map\_file\_path                               | unit test suffices   |
| Misc                 | PinMapUsesNIDCPowerChannelGroups              |                                                    |                      |
| Misc                 | SiteNumbers                                   | site\_numbers                                      | unit test suffices   |
| Misc                 | InstrumentTypeIdConstants                     | InstrumentTypeIdConstants                          | n/a                  |
| Digital Project      | DigitalPatternProjectCaptureWaveformFilePaths | nidigital\_project\_capture\_waveform\_file\_paths | test\_nidigital      |
| Digital Project      | DigitalPatternProjectLevelsFilePaths          | nidigital\_project\_levels\_file\_paths            | test\_nidigital      |
| Digital Project      | DigitalPatternProjectPatternFilePaths         | nidigital\_project\_pattern\_file\_paths           | test\_nidigital      |
| Digital Project      | DigitalPatternProjectSourceWaveformFilePaths  | nidigital\_project\_source\_waveform\_file\_paths  | test\_nidigital      |
| Digital Project      | DigitalPatternProjectSpecificationsFilePaths  | nidigital\_project\_specifications\_file\_paths    | test\_nidigital      |
| Digital Project      | DigitalPatternProjectTimingFilePaths          | nidigital\_project\_timing\_file\_paths            | test\_nidigital      |
| Input Data           | GetInputDataAsBooleans                        |                                                    |                      |
| Input Data           | GetInputDataAsDouble                          |                                                    |                      |
| Input Data           | GetInputDataAsStrings                         |                                                    |                      |

## Model-Based Instruments
| Class/Interface                   | Method/Property          | Python |
|-----------------------------------|--------------------------|--------|
| SemiconductorModuleContext        | GetModelBasedInstruments |        |
| IModelBasedInstrument             | Category                 |        |
| IModelBasedInstrument             | ModelName                |        |
| IModelBasedInstrument             | Name                     |        |
| IModelBasedInstrument             | Subcategory              |        |
| IModelBasedInstrument             | TryGetResource           |        |
| IModelBasedResource               | ModelResourceName        |        |
| IModelBasedPropertyItemContainer  | TryGetPropertyValue      |        |
| ModelBasedInstrumentSearchOptions | Category                 |        |
| ModelBasedInstrumentSearchOptions | Subcategory              |        |
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: systemtests/__init__.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/conftest.py sha256=4d40998c9736568a78f3eeb81111b4a36b705e9d066820f217510aa6187c5f74 bytes=4693 -->
## FILE: systemtests/conftest.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/conftest.py`
- sha256: `4d40998c9736568a78f3eeb81111b4a36b705e9d066820f217510aa6187c5f74`
- bytes: 4693

````python
import os
import os.path
import sys
import shutil
import subprocess
import winreg
import pytest

_python_version = ".".join(map(str, sys.version_info[:2]))
try:
    _python_environment_path = os.environ["VIRTUAL_ENV"]
except KeyError:
    _python_environment_path = ""  # global interpreter


def get_env_variable_from_registry(variable_name):
    key = winreg.CreateKey(
        winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager\Environment"
    )
    return winreg.QueryValueEx(key, variable_name)[0]


_teststand_public_path = get_env_variable_from_registry("TestStandPublic64")


class SystemTestRunner:
    # subprocess.run with check=True will throw an exception if the return code is non-zero
    # with stdout set to subprocess.PIPE, exit code and stdout will be included in the exception
    _SUBPROCESS_RUN_OPTIONS = {"stdout": subprocess.PIPE, "timeout": 180, "check": True}

    # we need to get the TestStand variables from the registry since the pipeline process
    # does not refresh its environment after running the TestStand version selector

    _csharp_oi_path = os.path.join(
        _teststand_public_path,
        "UserInterfaces",
        "Simple",
        "CSharp",
        "Source Code",
        "bin",
        "x64",
        "release",
        "TestExec.exe",
    )

    _test_fixture_path = os.path.join(os.path.dirname(__file__), "SystemTestFixture.seq")

    _offline_mode_tool_path = os.path.join(
        os.environ["ProgramFiles(x86)"],
        "National Instruments",
        "Shared",
        "OfflineMode",
        "NationalInstruments.Semiconductor.OfflineModeAPITool.exe",
    )

    def __init__(self, sequence_file_path, offline_mode_cfg_path=""):
        self._sequence_file_path = sequence_file_path
        self._offline_mode_cfg_path = offline_mode_cfg_path

    def __enter__(self):
        if self._offline_mode_cfg_path:
            subprocess.run(
                [self._offline_mode_tool_path, "/enter", self._offline_mode_cfg_path],
                **self._SUBPROCESS_RUN_OPTIONS,
            )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._offline_mode_cfg_path:
            subprocess.run([self._offline_mode_tool_path, "/leave"], **self._SUBPROCESS_RUN_OPTIONS)

    def run(self):
        subprocess.run(
            [
                self._csharp_oi_path,
                "/outputtostdio",
                "/run",
                "MainSequence",
                self._test_fixture_path,
                "/pyrunentrypoint",
                "Test UUTs",
                self._sequence_file_path,
                "/pyversion",
                _python_version,
                "/pyenvironment",
                _python_environment_path,
                "/quit",
            ],
            **self._SUBPROCESS_RUN_OPTIONS,
        )
        return True


@pytest.fixture(scope="session", autouse=True)
def teststand_login_override():
    system_tests_front_end_callbacks_path = os.path.join(
        os.path.dirname(__file__), "FrontEndCallbacks.seq"
    )
    teststand_front_end_callbacks_path = os.path.join(
        _teststand_public_path, "Components", "Callbacks", "FrontEnd", "FrontEndCallbacks.seq"
    )
    teststand_backup_front_end_callbacks_path = os.path.join(
        _teststand_public_path, "Components", "Callbacks", "FrontEnd", "FrontEndCallbacks.seq.bak"
    )
    os.replace(teststand_front_end_callbacks_path, teststand_backup_front_end_callbacks_path)
    shutil.copy(system_tests_front_end_callbacks_path, teststand_front_end_callbacks_path)
    yield None
    os.replace(teststand_backup_front_end_callbacks_path, teststand_front_end_callbacks_path)


@pytest.fixture
def system_test_runner(request):
    # get absolute path of the test program file which is assumed to be relative to the test module
    module_directory = os.path.dirname(request.module.__file__)

    sequence_file_name = request.node.get_closest_marker("sequence_file").args[0]
    sequence_file_path = os.path.join(module_directory, sequence_file_name)

    offline_mode_marker = request.node.get_closest_marker("offline_mode")
    if offline_mode_marker:
        offline_mode_cfg_name = offline_mode_marker.args[0]
        offline_mode_cfg_path = os.path.join(module_directory, offline_mode_cfg_name)
    else:
        offline_mode_cfg_path = ""

    with SystemTestRunner(sequence_file_path, offline_mode_cfg_path) as test_runner:
        # the context manager will enter and exit offline mode if the marker was supplied
        yield test_runner
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/custom_instruments.pinmap sha256=884c88cac574e2f27d3a792aa31a3a1bcb350b890f81302914fc133ea048907a bytes=1031 -->
## FILE: systemtests/custom_instruments.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/custom_instruments.pinmap`
- sha256: `884c88cac574e2f27d3a792aa31a3a1bcb350b890f81302914fc133ea048907a`
- bytes: 1031

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<Instrument name="PXI0::16" instrumentTypeId="Relay1_Id">
			<ChannelGroup id="ChannelGroup">
				<Channel id="Ch0" />
				<Channel id="Ch1" />
				<Channel id="Ch2" />
			</ChannelGroup>
		</Instrument>
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI0::16" channel="Ch0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI0::16" channel="Ch1" />
		<SystemConnection pin="SystemPin1" instrument="PXI0::16" channel="Ch2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/custom_instruments_codemodules.py sha256=a7fcb411d0758fcfd88676544b3510f4e5a49e42f0d8c877e4d360d4afe19dae bytes=3248 -->
## FILE: systemtests/custom_instruments_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/custom_instruments_codemodules.py`
- sha256: `a7fcb411d0758fcfd88676544b3510f4e5a49e42f0d8c877e4d360d4afe19dae`
- bytes: 3248

````python
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


class CustomSession:
    def __init__(self, instrument_type_id, instrument_name, channel_group_id, channel_list):
        self._instrument_type_id = instrument_type_id
        self._instrument_name = instrument_name
        self._channel_group_id = channel_group_id
        self._channel_list = channel_list

    @property
    def instrument_type_id(self):
        return self._instrument_type_id

    @property
    def instrument_name(self):
        return self._instrument_name

    @property
    def channel_group_id(self):
        return self._channel_group_id

    @property
    def channel_list(self):
        return self._channel_list


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id):
    custom_instrument_info = tsm_context.get_custom_instrument_names(instrument_type_id)
    for instrument_name, channel_group_id, channel_list in zip(*custom_instrument_info):
        session = CustomSession(instrument_type_id, instrument_name, channel_group_id, channel_list)
        tsm_context.set_custom_session(
            instrument_type_id, instrument_name, channel_group_id, session
        )


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    instrument_type_id,
    pins,
    expected_instrument_names,
    expected_channel_group_ids,
    expected_channel_lists,
):
    pin_query, *session_info = tsm_context.pins_to_custom_sessions(instrument_type_id, pins)
    expected_instrument_channels = set(
        zip(expected_instrument_names, expected_channel_group_ids, expected_channel_lists)
    )
    valid_channels = []

    for session, channel_group_id, channel_list in zip(*session_info):
        assert isinstance(session, CustomSession)
        assert session.instrument_type_id == instrument_type_id
        assert session.channel_group_id == channel_group_id

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_channels = (
            session.instrument_name,
            channel_group_id,
            channel_list,
        )
        channel_count = len(channel_list.split(","))
        valid_channels.append(
            [actual_instrument_channels in expected_instrument_channels] * channel_count
        )
        expected_instrument_channels -= {actual_instrument_channels}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id):
    session_info = tsm_context.get_all_custom_sessions(instrument_type_id)
    for session, channel_group_id, channel_list in zip(*session_info):
        assert isinstance(session, CustomSession)
        assert session.instrument_type_id == instrument_type_id
        assert session.channel_group_id == channel_group_id
        assert session.channel_list == channel_list
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/FrontEndCallbacks.seq sha256=881b8db61d6079fa1024611eef00018d4b0c9a9ff2a0c51ded1162c5baffcaca bytes=47345 -->
## FILE: systemtests/FrontEndCallbacks.seq

- repository: `ni/nitsm-python`
- source_path: `systemtests/FrontEndCallbacks.seq`
- sha256: `881b8db61d6079fa1024611eef00018d4b0c9a9ff2a0c51ded1162c5baffcaca`
- bytes: 47345

````text
[__Header__]
ProductName = "TestStand"
ProductVersion = 16.0.0.185
CompatibleProdVersion = 16.0.0.0
Version = 797
Type = "SequenceFile"
Path = ""
ProductVersionString = "2016 (16.0.0.185)"
CharEncoding = "SBCS"

[DEF, %OBJROOT]
SF = SequenceFileData
Action = StepType
Path = PathValue
StepTypeMenu = Obj
TEInf = Obj
Error = Obj
CommonResults = Obj
StepTypeSubstepsArray = Objs
Expression = ExprValue
AutomationStepAdditions = AutomationModule
AutomationParameter = AutomationParameter
SequenceCall = StepType
SeqCallStepAdditions = SeqCallModule
PassFailTest = StepType
EditSubstep = StepType
FlexCStepAdditions = FCModule
FCParameter = FCParameter
Label = StepType
NoneStepAdditions = NoneModule
StepTypeNIData = Obj
NI_CustomResult = CustomResult
NI_PropertyObjectType = PropertyObjectType
NI_ArrayDimensions = ArrayDimensions
NI_ActiveXParameterResult = ActiveXParameterResult
NI_CommonCParameterResult = CommonCParameterResult

[DEF, SF]
Seq = Objs
FileGlobalDefaults = Obj
ModelFile = "TYPE, Path"
LoadOpt = Str
UnloadOpt = Str
Type = Num
ModelOption = Num
Version = Str
BatchSync = Num
SFGlobalsScope = Num
Requirements = Obj
%NAME = "Data"

[SF]
%HI: Seq = [2]
%FLG: Seq = 4194304
%FLG: FileGlobalDefaults = 4194304
%FLG: ModelFile = 4194312
LoadOpt = "UseStepLoadOpt"
%FLG: LoadOpt = 4194312
UnloadOpt = "UseStepUnloadOpt"
%FLG: UnloadOpt = 4194312
Type = 2
%FLG: Type = 4194312
ModelOption = 1
%FLG: ModelOption = 4194312
Version = "3.0.0.12373"
%FLG: Version = 4194312
BatchSync = 1
%FLG: BatchSync = 4194312
%FLG: SFGlobalsScope = 4194312
%FLG: Requirements = 4194305

[DEF, SF.Seq]
%[0] = Sequence
%[1] = Sequence
%[2] = Sequence

[DEF, SF.Seq[0]]
Parameters = Obj
Locals = Obj
Main = Objs
Setup = Objs
Cleanup = Objs
StoreResults = Bool
RecordResults = Bool
RTS = Obj
Requirements = Obj
FailureAction = Num
%NAME = "LoginLogout"

[SF.Seq[0]]
%FLG: Parameters = 4456448
%FLG: Locals = 4194304
%HI: Main = [2]
%FLG: Main = 4194304
%FLG: Setup = 4194304
%FLG: Cleanup = 4194304
StoreResults = True
RecordResults = True
%FLG: RecordResults = 4194312
%FLG: RTS = 4456456
%FLG: Requirements = 4456456
FailureAction = 2
%FLG: FailureAction = 4194312

[DEF, SF.Seq[0].Locals]
ResultList = Objs

[DEF, SF.Seq[0].Locals.ResultList]
%EPTYPE = TEResult

[DEF, SF.Seq[0].Main]
%[0] = Step
%TYPE: %[0] = "Label"
%[1] = Step
%TYPE: %[1] = "SequenceCall"
%[2] = Step
%TYPE: %[2] = "SequenceCall"

[SF.Seq[0].Main[0].TS]
Id = "ID#:5oMuySZ1J0CKSZ3D5mJs+D"
%FLG: Requirements = 1

[DEF, SF.Seq[0].Main[0].TS]
Requirements = Obj

[DEF, SF.Seq[0].Main[0].TS.Requirements]
Links = Strs

[SF.Seq[0].Main[0].TS.Requirements]
%FLG: Links = 4194304

[SF.Seq[0].Main[0].TS.CustomResults.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[0].Main[0].TS.AdditionalResultsHints.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[0].Main[0]]
Description Line0001 = "This sequence will automatically login the user specified in FileGlobals.userToLogin and will bypass the login dialog.  "
Description Line0002 = "Only the initial login is automatic and only if the user specified is a valid user."

[DEF, SF.Seq[0].Main[0]]
%NAME = "Explain"

[SF.Seq[0].Main[1].TS]
Id = "ID#:2Bo0TnGS6Ea64N9M1LrNEC"
PreCond = "Parameters.isInitialLogin"
PassAct = "Goto"
PassActTarget = "\"<End>\""
CustTrueAct = "Goto"
CustTrueActTarget = "\"<End>\""
%FLG: Requirements = 1

[DEF, SF.Seq[0].Main[1].TS]
SData = "TYPE, SeqCallStepAdditions"
Requirements = Obj

[SF.Seq[0].Main[1].TS.SData]
SeqName = "AutoLogin"
UseCurFile = True
CustomThreadAffinity = "-1"

[DEF, SF.Seq[0].Main[1].TS.Requirements]
Links = Strs

[SF.Seq[0].Main[1].TS.Requirements]
%FLG: Links = 4194304

[SF.Seq[0].Main[1].TS.CustomResults.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[0].Main[1].TS.AdditionalResultsHints.%EPTYPE.Flags]
%NUMFMT = ""

[DEF, SF.Seq[0].Main[1]]
%NAME = "Auto Login If Initial Login"

[SF.Seq[0].Main[2].TS]
Id = "ID#:JHRhwcPu5hGm+ABQVsAACA"

[DEF, SF.Seq[0].Main[2].TS]
SData = "TYPE, SeqCallStepAdditions"

[SF.Seq[0].Main[2].TS.SData]
SeqName = "Logout"
UseCurFile = True

[DEF, SF.Seq[0].Main[2]]
%NAME = "SequenceCall"

[DEF, SF.Seq[0].RTS]
Type = Num
EPNameExpr = Str
EPEnabledExpr = Str
EPMenuHint = Str
EPIgnoreClient = Bool
EPInitiallyHidden = Bool
EPCheckToSaveTitledFile = Bool
ShowEPForFileWin = Bool
ShowEPForExeWin = Bool
CopyStepsOnOverriding = Bool
OptimizeNonReentrantCalls = Bool
Priority = Num
ShowEPAlways = Bool
ShowEPForEditorOnly = Bool
AllowIntExeOfEP = Bool

[SF.Seq[0].RTS]
%FLG: Type = 4194304
%FLG: EPNameExpr = 4194304
EPEnabledExpr = "True"
%FLG: EPEnabledExpr = 4194304
%FLG: EPMenuHint = 4194304
%FLG: EPIgnoreClient = 4194304
%FLG: EPInitiallyHidden = 4194304
EPCheckToSaveTitledFile = True
%FLG: EPCheckToSaveTitledFile = 4194304
ShowEPForFileWin = True
%FLG: ShowEPForFileWin = 4194304
%FLG: ShowEPForExeWin = 4194304
CopyStepsOnOverriding = True
%FLG: CopyStepsOnOverriding = 4194304
OptimizeNonReentrantCalls = True
%FLG: OptimizeNonReentrantCalls = 4194304
Priority = 2953567917
%FLG: Priority = 4194304
%FLG: ShowEPAlways = 4194304
%FLG: ShowEPForEditorOnly = 4194304
%FLG: AllowIntExeOfEP = 4194304

[DEF, SF.Seq[0].Requirements]
Links = Strs

[SF.Seq[0].Requirements]
%FLG: Links = 71303168

[DEF, SF.Seq[1]]
Parameters = Obj
Locals = Obj
Main = Objs
Setup = Objs
Cleanup = Objs
RecordResults = Bool
RTS = Obj
Requirements = Obj
FailureAction = Num
%NAME = "AutoLogin"

[SF.Seq[1]]
%FLG: Parameters = 4456448
%FLG: Locals = 4194304
%HI: Main = [1]
%FLG: Main = 4194304
%FLG: Setup = 4194304
%FLG: Cleanup = 4194304
RecordResults = True
%FLG: RecordResults = 4194312
%FLG: RTS = 4456456
%FLG: Requirements = 4456456
FailureAction = 2
%FLG: FailureAction = 4194312

[DEF, SF.Seq[1].Locals]
ResultList = Objs
userToLogin = Ref

[DEF, SF.Seq[1].Locals.ResultList]
%EPTYPE = TEResult

[DEF, SF.Seq[1].Main]
%[0] = Step
%TYPE: %[0] = "PassFailTest"
%[1] = Step
%TYPE: %[1] = "Action"

[SF.Seq[1].Main[0].TS]
Id = "ID#:9HZQhNVCbE6cpXZ3LXT6AB"
StatusExpr Line0001 = "Step.DataSource != \"Step.Result.PassFail\" ? Step.Result.PassFail = Evaluate(Step.DataSource) : False, Step.Result.Pass"
StatusExpr Line0002 = "Fail ? \"Passed\" : \"Failed\""
%FLG: Requirements = 1

[DEF, SF.Seq[1].Main[0].TS]
SData = "TYPE, AutomationStepAdditions"
Requirements = Obj

[SF.Seq[1].Main[0].TS.SData.Call]
ObjectVariable = "RunState.Engine"
Server = "{B2794EF3-C0B6-11D0-939C-0020AF68E893}"
ServerName = "NI TestStand API 3.0"
CoClass = "{B2794EF6-C0B6-11D0-939C-0020AF68E893}"
CoClassName = "Engine"
Interface = "{B2794EF5-C0B6-11D0-939C-0020AF68E893}"
InterfaceName = "IEngine"
MemberType = 1
Member = 72
MemberName = "GetUser"
HasMemberInfo = True
HasReturnValue = True
TypeLibVersion = "1.0"
InterfaceType = 1
VTableIndex = 15
%HI: Parameters = [1]

[DEF, SF.Seq[1].Main[0].TS.SData.Call.Parameters]
%[0] = "TYPE, AutomationParameter"
%[1] = "TYPE, AutomationParameter"

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[0]]
Name = "Return Value"
ArgVal = "Locals.userToLogin"
ArgDisplayVal = "Locals.userToLogin"
Type = 9
DisplayType = "User (Object Reference)"
TypeValid = True
Direction = 2
IsUserOptional = True
IsByRef = True
IID = "{EAAB7FB0-70D8-11D1-AF2E-006097B79EF5}"

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[0].AdditionalResults.Input.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[0].AdditionalResults.Output.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[1]]
Name = "LoginName"
ArgVal = "FileGlobals.UserToAutoLogin"
ArgDisplayVal = "FileGlobals.UserToAutoLogin"
Type = 8
DisplayType = "String"
TypeValid = True
Direction = 1

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[1].AdditionalResults.Input.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[0].TS.SData.Call.Parameters[1].AdditionalResults.Output.Flags]
%NUMFMT = ""

[DEF, SF.Seq[1].Main[0].TS.Requirements]
Links = Strs

[SF.Seq[1].Main[0].TS.Requirements]
%FLG: Links = 4194304

[SF.Seq[1].Main[0].TS.CustomResults.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[0].TS.AdditionalResultsHints.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[0].Result]
PassFail = True

[SF.Seq[1].Main[0]]
DataSource = "Locals.userToLogin != Nothing"

[DEF, SF.Seq[1].Main[0]]
%NAME = "Get User To Login"

[SF.Seq[1].Main[1].TS]
Id = "ID#:Foec0r9dKEWS041axmQGnD"
PreCond = "RunState.Sequence.Main[\"ID#:9HZQhNVCbE6cpXZ3LXT6AB\"].Result.Status == \"Passed\""
%FLG: Requirements = 1

[DEF, SF.Seq[1].Main[1].TS]
SData = "TYPE, AutomationStepAdditions"
Requirements = Obj

[SF.Seq[1].Main[1].TS.SData.Call]
ObjectVariable = "RunState.Engine"
Server = "{B2794EF3-C0B6-11D0-939C-0020AF68E893}"
ServerName = "NI TestStand API 3.0"
CoClass = "{B2794EF6-C0B6-11D0-939C-0020AF68E893}"
CoClassName = "Engine"
Interface = "{B2794EF5-C0B6-11D0-939C-0020AF68E893}"
InterfaceName = "IEngine"
MemberType = 4
Member = 301
MemberName = "CurrentUser"
HasMemberInfo = True
TypeLibVersion = "1.0"
InterfaceType = 1
VTableIndex = 69
%HI: Parameters = [0]

[DEF, SF.Seq[1].Main[1].TS.SData.Call.Parameters]
%[0] = "TYPE, AutomationParameter"

[SF.Seq[1].Main[1].TS.SData.Call.Parameters[0]]
Name = "newValue"
ArgVal = "Locals.userToLogin"
ArgDisplayVal = "Locals.userToLogin"
Type = 9
DisplayType = "User (Object Reference)"
TypeValid = True
Direction = 1
IID = "{EAAB7FB0-70D8-11D1-AF2E-006097B79EF5}"

[SF.Seq[1].Main[1].TS.SData.Call.Parameters[0].AdditionalResults.Input.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[1].TS.SData.Call.Parameters[0].AdditionalResults.Output.Flags]
%NUMFMT = ""

[DEF, SF.Seq[1].Main[1].TS.Requirements]
Links = Strs

[SF.Seq[1].Main[1].TS.Requirements]
%FLG: Links = 4194304

[SF.Seq[1].Main[1].TS.CustomResults.%EPTYPE.Flags]
%NUMFMT = ""

[SF.Seq[1].Main[1].TS.AdditionalResultsHints.%EPTYPE.Flags]
%NUMFMT = ""

[DEF, SF.Seq[1].Main[1]]
%NAME = "Set Current User"

[DEF, SF.Seq[1].RTS]
Type = Num
OptimizeNonReentrantCalls = Bool
EPNameExpr = Str
EPEnabledExpr = Str
EPMenuHint = Str
EPIgnoreClient = Bool
EPInitiallyHidden = Bool
EPCheckToSaveTitledFile = Bool
ShowEPAlways = Bool
ShowEPForFileWin = Bool
ShowEPForExeWin = Bool
ShowEPForEditorOnly = Bool
AllowIntExeOfEP = Bool
CopyStepsOnOverriding = Bool
Priority = Num

[SF.Seq[1].RTS]
%FLG: Type = 4194304
OptimizeNonReentrantCalls = True
%FLG: OptimizeNonReentrantCalls = 4194304
EPNameExpr = "\"Unnamed Entry Point\""
%FLG: EPNameExpr = 4194304
EPEnabledExpr = "True"
%FLG: EPEnabledExpr = 4194304
%FLG: EPMenuHint = 4194304
%FLG: EPIgnoreClient = 4194304
%FLG: EPInitiallyHidden = 4194304
EPCheckToSaveTitledFile = True
%FLG: EPCheckToSaveTitledFile = 4194304
%FLG: ShowEPAlways = 4194304
ShowEPForFileWin = True
%FLG: ShowEPForFileWin = 4194304
%FLG: ShowEPForExeWin = 4194304
%FLG: ShowEPForEditorOnly = 4194304
%FLG: AllowIntExeOfEP = 4194304
CopyStepsOnOverriding = True
%FLG: CopyStepsOnOverriding = 4194304
Priority = 2953567917
%FLG: Priority = 4194304

[DEF, SF.Seq[1].Requirements]
Links = Strs

[SF.Seq[1].Requirements]
%FLG: Links = 71303168

[DEF, SF.Seq[2]]
Parameters = Obj
Locals = Obj
Main = Objs
Setup = Objs
Cleanup = Objs
RecordResults = Bool
RTS = Obj
Requirements = Obj
FailureAction = Num
%NAME = "Logout"

[SF.Seq[2]]
%FLG: Parameters = 4456448
%FLG: Locals = 4194304
%FLG: Main = 4194304
%FLG: Setup = 4194304
%FLG: Cleanup = 4194304
RecordResults = True
%FLG: RecordResults = 4194312
%FLG: RTS = 4456456
%FLG: Requirements = 4456456
FailureAction = 2
%FLG: FailureAction = 4194312

[DEF, SF.Seq[2].Locals]
ResultList = Objs

[DEF, SF.Seq[2].Locals.ResultList]
%EPTYPE = TEResult

[SF.Seq[2].Locals]
%FLG: ResultList = 4194304

[DEF, SF.Seq[2].RTS]
Type = Num
OptimizeNonReentrantCalls = Bool
EPNameExpr = Str
EPEnabledExpr = Str
EPMenuHint = Str
EPIgnoreClient = Bool
EPInitiallyHidden = Bool
EPCheckToSaveTitledFile = Bool
ShowEPAlways = Bool
ShowEPForFileWin = Bool
ShowEPForExeWin = Bool
ShowEPForEditorOnly = Bool
AllowIntExeOfEP = Bool
CopyStepsOnOverriding = Bool
Priority = Num

[SF.Seq[2].RTS]
%FLG: Type = 4194304
OptimizeNonReentrantCalls = True
%FLG: OptimizeNonReentrantCalls = 4194304
EPNameExpr = "\"Unnamed Entry Point\""
%FLG: EPNameExpr = 4194304
EPEnabledExpr = "True"
%FLG: EPEnabledExpr = 4194304
%FLG: EPMenuHint = 4194304
%FLG: EPIgnoreClient = 4194304
%FLG: EPInitiallyHidden = 4194304
EPCheckToSaveTitledFile = True
%FLG: EPCheckToSaveTitledFile = 4194304
%FLG: ShowEPAlways = 4194304
ShowEPForFileWin = True
%FLG: ShowEPForFileWin = 4194304
%FLG: ShowEPForExeWin = 4194304
%FLG: ShowEPForEditorOnly = 4194304
%FLG: AllowIntExeOfEP = 4194304
CopyStepsOnOverriding = True
%FLG: CopyStepsOnOverriding = 4194304
Priority = 2953567917
%FLG: Priority = 4194304

[DEF, SF.Seq[2].Requirements]
Links = Strs

[SF.Seq[2].Requirements]
%FLG: Links = 71303168

[DEF, SF.FileGlobalDefaults]
UserToAutoLogin = Str

[SF.FileGlobalDefaults]
UserToAutoLogin = "administrator"

[DEF, SF.Requirements]
Links = Strs

[SF.Requirements]
%FLG: Links = 4194304

[%TYPES]
Action = "Action"
Path = "Path"
StepTypeMenu = "StepTypeMenu"
TEInf = "TEInf"
Error = "Error"
CommonResults = "CommonResults"
StepTypeSubstepsArray = "StepTypeSubstepsArray"
Expression = "Expression"
AutomationStepAdditions = "AutomationStepAdditions"
AutomationParameter = "AutomationParameter"
SequenceCall = "SequenceCall"
SeqCallStepAdditions = "SeqCallStepAdditions"
PassFailTest = "PassFailTest"
EditSubstep = "EditSubstep"
FlexCStepAdditions = "FlexCStepAdditions"
FCParameter = "FCParameter"
Label = "Label"
NoneStepAdditions = "NoneStepAdditions"
StepTypeNIData = "StepTypeNIData"
NI_CustomResult = "NI_CustomResult"
NI_PropertyObjectType = "NI_PropertyObjectType"
NI_ArrayDimensions = "NI_ArrayDimensions"
NI_ActiveXParameterResult = "NI_ActiveXParameterResult"
NI_CommonCParameterResult = "NI_CommonCParameterResult"

[DEF, Action]
%LOCATION = "StepTypes"
Substeps = "TYPE, StepTypeSubstepsArray"
DescriptionFormat = "TYPE, Expression"
%FLG: DescriptionFormat = 524288
DefaultNameFormat = "TYPE, Expression"
%FLG: DefaultNameFormat = 524288
Menu = "TYPE, StepTypeMenu"
AdditionalResultsHints = Objs
%FLG: AdditionalResultsHints = 524288
TS = "TYPE, TEInf"
NI_Data = "TYPE, StepTypeNIData"
Result = Obj
CodeTemplates = Str
%FLG: CodeTemplates = 524288
BlockStartTypes = Str
%FLG: BlockStartTypes = 524288
BlockEndTypes = Str
%FLG: BlockEndTypes = 524288
AppliesToBlockStructure = Bool
%FLG: AppliesToBlockStructure = 524288
CanEncapsulate = Bool
%FLG: CanEncapsulate = 524288
%ROOT_TYPE = True

[Action]
%INSTFLG: Substeps = 524312
%INSTOVRD: Substeps = 655384
DescriptionFormat Line0001 = "ResStr(\"NI_STEPTYPES\", \"ACTION_DESCRIPTION_NAME\") + ((\"%ModuleDescription\" == \"\") ? \"\" : \",  %ModuleDescripti"
DescriptionFormat Line0002 = "on\")"
%FLG: DescriptionFormat = 4194328
%INSTFLG: DescriptionFormat = 4718616
%INSTOVRD: DescriptionFormat = 4718616
DefaultNameFormat = "ResStr(\"NI_STEPTYPES\", \"ACTION_DEF_STEP_NAME\")"
%FLG: DefaultNameFormat = 4194328
%INSTFLG: DefaultNameFormat = 4718616
%INSTOVRD: DefaultNameFormat = 4718616
%INSTFLG: Menu = 524312
%INSTOVRD: Menu = 524312
%FLG: AdditionalResultsHints = 4194328
%INSTFLG: TS = 262168
%INSTOVRD: TS = 4456472
%FLG: Result = 4194304
%INSTFLG: Result = 4194304
CodeTemplates Line0001 = "DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|Defa"
CodeTemplates Line0002 = "ultHTB80_Template|Default_Template"
%FLG: CodeTemplates = 4194328
%FLG: BlockStartTypes = 4194328
%FLG: BlockEndTypes = 4194328
%FLG: AppliesToBlockStructure = 4194328
%FLG: CanEncapsulate = 4194328
%TIMESTAMP = 1462492640
%VERSION = "16.0.0.0"
%TYPELASTMOD = "16.0.0.131"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554446

[Action.Menu]
ItemName = "ResStr(\"NI_STEPTYPES\", \"ACTION_MENU_ITEM_NAME\")"
Group = "Action"

[DEF, Action.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[DEF, Action.TS]
SData = Obj
%FLG: SData = 2097152
Requirements = Obj
%FLG: Requirements = 2097152

[Action.TS]
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7143448
ConnectionLifetime = 0
%INSTFLG: PassAct = 1
%INSTOVRD: PassAct = 5046297
%INSTFLG: FailAct = 1
%INSTOVRD: FailAct = 5046297
%INSTFLG: PassActTarget = 1
%INSTOVRD: PassActTarget = 5046297
%INSTFLG: FailActTarget = 1
%INSTOVRD: FailActTarget = 5046297
%FLG: Requirements = 1
%INSTFLG: Requirements = 1

[DEF, Action.TS.Requirements]
Links = Strs

[Action.TS.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[DEF, Action.Result]
Error = "TYPE, Error"
Status = Str
ReportText = Str
Common = "TYPE, CommonResults"

[Action.Result]
%FLG: Error = 4194304
%INSTFLG: Error = 4194304
%INSTOVRD: Error = 4194304
%FLG: Status = 4194304
%INSTFLG: Status = 4194304
%FLG: ReportText = 4194304
%INSTFLG: ReportText = 4194304
%INSTOVRD: Common = 4194304

[DEF, Path]
%LOCATION = "StdTypes"
%ROOT_TYPE = True

[Path]
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554436

[DEF, StepTypeMenu]
%LOCATION = "StdTypes"
CanBeSubstepType = Bool
CanOnlyBeSubstepType = Bool
Category = Str
ItemName = "TYPE, Expression"
SingularItemName = Str
SeparatorBeforeCategory = Bool
SeparatorBeforeItemName = Bool
Group = Str
%ROOT_TYPE = True

[StepTypeMenu]
Category = "\"\""
ItemName = "\"\""
SingularItemName = "\"\""
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436
%INSTFLG = 4718616
%INSTOVRD = 4718616

[DEF, TEInf]
%LOCATION = "StdTypes"
Id = Str
Icon = Str
SData = Obj
%FLG: SData = 2097152
PreCond = "TYPE, Expression"
LoadOpt = Str
UnloadOpt = Str
Mode = Str
WindowActivation = Str
ResultOption = Num
StepFCSeqF = Bool
IgnoreRTE = Bool
UseMutex = Bool
MutexNameOrRef = "TYPE, Expression"
BatchSyncOpt = Num
SwitchEnabled = Bool
VirtualDeviceName = "TYPE, Expression"
SwitchOperation = Num
RouteGroupConnect = "TYPE, Expression"
RouteGroupDisconnect = "TYPE, Expression"
MulticonnectMode = Num
OperationOrder = Num
ConnectionLifetime = Num
WaitForDebounce = Bool
PassAct = Str
FailAct = Str
PassActTarget = "TYPE, Expression"
FailActTarget = "TYPE, Expression"
CustExpr = "TYPE, Expression"
CustTrueAct = Str
CustFalseAct = Str
CustTrueActTarget = "TYPE, Expression"
CustFalseActTarget = "TYPE, Expression"
LoopType = Str
LoopWhile = "TYPE, Expression"
LoopStatus = "TYPE, Expression"
LoopIncrement = "TYPE, Expression"
LoopInitialize = "TYPE, Expression"
LoopOpt = Num
PreExpr = "TYPE, Expression"
PostExpr = "TYPE, Expression"
StatusExpr = "TYPE, Expression"
CanSpecifyModule = Bool
CanEditCode = Bool
CanEditModulePrototype = Bool
CanEditParameterAdditionalResults = Bool
PrecondIntExe = Num
Requirements = Obj
%FLG: Requirements = 2097152
CustomResults = Objs
AdditionalResultsHints = Objs
%ROOT_TYPE = True

[TEInf]
%INSTFLG: Id = 1
%INSTOVRD: Id = 5046297
%INSTOVRD: Icon = 5046296
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7143448
%INSTOVRD: PreCond = 5046296
LoadOpt = "PreloadWhenExecuted"
%INSTOVRD: LoadOpt = 5046296
UnloadOpt = "UnloadWithFile"
%INSTOVRD: UnloadOpt = 5046296
Mode = "Normal"
%INSTOVRD: Mode = 5046296
WindowActivation = "None"
%INSTOVRD: WindowActivation = 5046296
ResultOption = 1
%INSTOVRD: ResultOption = 5046296
StepFCSeqF = True
%INSTOVRD: StepFCSeqF = 5046296
%INSTOVRD: IgnoreRTE = 5046296
%INSTOVRD: UseMutex = 5046296
%INSTOVRD: MutexNameOrRef = 5046296
%INSTOVRD: BatchSyncOpt = 5046296
%INSTOVRD: SwitchEnabled = 5046296
%INSTOVRD: VirtualDeviceName = 5046296
SwitchOperation = 1
%INSTOVRD: SwitchOperation = 5046296
%INSTOVRD: RouteGroupConnect = 5046296
%INSTOVRD: RouteGroupDisconnect = 5046296
MulticonnectMode = 1
%INSTOVRD: MulticonnectMode = 5046296
OperationOrder = 2
%INSTOVRD: OperationOrder = 5046296
ConnectionLifetime = 4
%INSTOVRD: ConnectionLifetime = 5046296
WaitForDebounce = True
%INSTOVRD: WaitForDebounce = 5046296
PassAct = "Next"
%INSTOVRD: PassAct = 5046296
FailAct = "Next"
%INSTOVRD: FailAct = 5046296
%INSTOVRD: PassActTarget = 5046296
%INSTOVRD: FailActTarget = 5046296
%INSTOVRD: CustExpr = 5046296
CustTrueAct = "Next"
%INSTOVRD: CustTrueAct = 5046296
CustFalseAct = "Next"
%INSTOVRD: CustFalseAct = 5046296
%INSTOVRD: CustTrueActTarget = 5046296
%INSTOVRD: CustFalseActTarget = 5046296
LoopType = "NoLooping"
%INSTOVRD: LoopType = 5046296
%INSTOVRD: LoopWhile = 5046296
%INSTOVRD: LoopStatus = 5046296
LoopIncrement = "RunState.LoopIndex += 1"
%INSTOVRD: LoopIncrement = 5046296
LoopInitialize = "RunState.LoopIndex = 0"
%INSTOVRD: LoopInitialize = 5046296
%INSTOVRD: LoopOpt = 5046296
%INSTOVRD: PreExpr = 5046296
%INSTOVRD: PostExpr = 5046296
%INSTOVRD: StatusExpr = 5046296
CanSpecifyModule = True
%INSTOVRD: CanSpecifyModule = 5046296
CanEditCode = True
%INSTOVRD: CanEditCode = 5046296
CanEditModulePrototype = True
%INSTOVRD: CanEditModulePrototype = 5046296
CanEditParameterAdditionalResults = True
%INSTOVRD: CanEditParameterAdditionalResults = 5046296
%INSTOVRD: PrecondIntExe = 5046296
%FLG: Requirements = 1
%INSTFLG: Requirements = 2097153
%INSTOVRD: Requirements = 7143449
%INSTOVRD: CustomResults = 5046296
%INSTOVRD: AdditionalResultsHints = 5046296
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436
%INSTFLG = 4456472
%INSTOVRD = 4456472

[DEF, TEInf.Requirements]
Links = Strs

[TEInf.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[DEF, TEInf.CustomResults]
%EPTYPE = "TYPE, NI_CustomResult"

[DEF, TEInf.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[DEF, Error]
%LOCATION = "StdTypes"
Code = Num
Msg = Str
Occurred = Bool
%ROOT_TYPE = True

[Error]
%FLG: Code = 4194304
%INSTFLG: Code = 4194304
%FLG: Msg = 4194304
%INSTFLG: Msg = 4194304
%FLG: Occurred = 4194304
%INSTFLG: Occurred = 4194304
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554436
%EXTDATA = True

[Error.Code]
%EXTDATA = True

[EXTDATA, Error.Code, STRUCT]
DataVersion = 1
Type = 6

[EXTDATA, Error.Code, CLUST]
DataVersion = 1
ClusterMemberLabelName = "code"

[EXTDATA, Error.Code, DNSTRUCT]
DataVersion = 1
StructMemberName = "code"

[Error.Msg]
%EXTDATA = True

[EXTDATA, Error.Msg, STRUCT]
DataVersion = 1
Type = 2
StringBufferSize = 1024
StringStorage = 1

[EXTDATA, Error.Msg, CLUST]
DataVersion = 1
ClusterMemberLabelName = "source"

[EXTDATA, Error.Msg, DNSTRUCT]
DataVersion = 1
StructMemberName = "msg"

[Error.Occurred]
%EXTDATA = True

[EXTDATA, Error.Occurred, STRUCT]
DataVersion = 1
Type = 6

[EXTDATA, Error.Occurred, CLUST]
DataVersion = 1
ClusterMemberLabelName = "status"

[EXTDATA, Error.Occurred, DNSTRUCT]
DataVersion = 1
StructMemberName = "occurred"

[EXTDATA, Error, STRUCT]
AllowStructPassing = True
DataVersion = 1
PackingOption = 8
Type = 0

[EXTDATA, Error, CLUST]
AllowClusterPassing = True
DataVersion = 1

[EXTDATA, Error, DNSTRUCT]
AllowStructPassing = True
DataVersion = 1
StructMemberName = ""

[DEF, CommonResults]
%LOCATION = "StdTypes"
%ROOT_TYPE = True

[CommonResults]
%TIMESTAMP = 1441304932
%VERSION = "3.1.0.100"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "3.1.0.0"
%FLG = 4194304
%TYPE_FLG = 33554432
%INSTFLG = 4194304

[DEF, StepTypeSubstepsArray]
%LOCATION = "StdTypes"
%ROOT_TYPE = True

[StepTypeSubstepsArray]
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436
%INSTFLG = 4718616
%INSTOVRD = 4849688

[DEF, Expression]
%LOCATION = "StdTypes"
%ROOT_TYPE = True

[Expression]
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554436

[DEF, AutomationStepAdditions]
%LOCATION = "StdTypes"
Call = AutomationCall
%ROOT_TYPE = True

[DEF, AutomationStepAdditions.Call]
ObjectVariable = "TYPE, Expression"
Server = Str
ServerName = Str
CreateObject = Num
CreateFromFilePath = "TYPE, Path"
CoClass = Str
CoClassName = Str
Interface = Str
InterfaceName = Str
RemoteMachine = "TYPE, Expression"
RemoteMachineByExpr = Bool
UseLoadSpec = Bool
MakeCall = Bool
MemberType = Num
Member = Num
MemberName = Str
HasMemberInfo = Bool
Locale = Num
HasReturnValue = Bool
TypeLibLocale = Num
TypeLibVersion = Str
InterfaceType = Num
VTableIndex = Num
Parameters = Objs

[AutomationStepAdditions.Call]
CreateObject = 3
MakeCall = True
MemberType = 2
InterfaceType = 2

[DEF, AutomationStepAdditions.Call.Parameters]
%EPTYPE = "TYPE, AutomationParameter"
%FLG: %EPTYPE = 131072

[AutomationStepAdditions]
%TIMESTAMP = 1466536129
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, AutomationParameter]
%LOCATION = "StdTypes"
Name = Str
ArgVal = "TYPE, Expression"
ArgDisplayVal = "TYPE, Expression"
Type = Num
DisplayType = Str
TypeValid = Bool
Direction = Num
IsUserOptional = Bool
IsServerOptional = Bool
IsByRef = Bool
IsSafeArray = Bool
IID = Str
UseDefault = Bool
AdditionalResults = Obj
UserData = Obj
%FLG: UserData = 2097152
%ROOT_TYPE = True

[AutomationParameter]
Name = "_notNamed"
%INSTFLG: UserData = 2097152
%TIMESTAMP = 1466536129
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, AutomationParameter.AdditionalResults]
Input = "TYPE, NI_ActiveXParameterResult"
Output = "TYPE, NI_ActiveXParameterResult"

[DEF, SequenceCall]
%LOCATION = "StepTypes"
Substeps = "TYPE, StepTypeSubstepsArray"
DescriptionFormat = "TYPE, Expression"
%FLG: DescriptionFormat = 524288
DefaultNameFormat = "TYPE, Expression"
%FLG: DefaultNameFormat = 524288
Menu = "TYPE, StepTypeMenu"
AdditionalResultsHints = Objs
%FLG: AdditionalResultsHints = 524288
TS = "TYPE, TEInf"
NI_Data = "TYPE, StepTypeNIData"
Result = Obj
CodeTemplates = Str
%FLG: CodeTemplates = 524288
BlockStartTypes = Str
%FLG: BlockStartTypes = 524288
BlockEndTypes = Str
%FLG: BlockEndTypes = 524288
AppliesToBlockStructure = Bool
%FLG: AppliesToBlockStructure = 524288
CanEncapsulate = Bool
%FLG: CanEncapsulate = 524288
%ROOT_TYPE = True

[SequenceCall]
%INSTFLG: Substeps = 524312
%INSTOVRD: Substeps = 655384
DescriptionFormat = "\"%ModuleDescription\""
%FLG: DescriptionFormat = 4194328
%INSTFLG: DescriptionFormat = 4718616
%INSTOVRD: DescriptionFormat = 4718616
DefaultNameFormat = "ResStr(\"NI_STEPTYPES\", \"SC_DEF_STEP_NAME\")"
%FLG: DefaultNameFormat = 4194328
%INSTFLG: DefaultNameFormat = 4718616
%INSTOVRD: DefaultNameFormat = 4718616
%INSTFLG: Menu = 524312
%INSTOVRD: Menu = 524312
%FLG: AdditionalResultsHints = 4194328
%INSTFLG: TS = 262168
%INSTOVRD: TS = 4456472
%FLG: Result = 4194304
%INSTFLG: Result = 4194304
%FLG: CodeTemplates = 4194328
%FLG: BlockStartTypes = 4194328
%FLG: BlockEndTypes = 4194328
%FLG: AppliesToBlockStructure = 4194328
%FLG: CanEncapsulate = 4194328
%TIMESTAMP = 1462492640
%VERSION = "16.0.0.0"
%TYPELASTMOD = "16.0.0.131"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554438

[SequenceCall.Menu]
ItemName = "ResStr(\"NI_STEPTYPES\", \"SC_MENU_ITEM_NAME\")"
Group = "NI_Miscellaneous"

[DEF, SequenceCall.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[SequenceCall.TS]
Icon = "SeqAdp.ico"
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7143448
ConnectionLifetime = 0
StatusExpr Line0001 = "(Step.Result.Status == \"Done\" && (Step.TS.SData.ThreadOpt == 0 || Step.TS.SData.ThreadOpt == 3)) ? \"Passed\" : Step.R"
StatusExpr Line0002 = "esult.Status"
%INSTFLG: StatusExpr = 1
%INSTOVRD: StatusExpr = 5046297
%FLG: Requirements = 1
%INSTFLG: Requirements = 1

[DEF, SequenceCall.TS]
SData = "TYPE, SeqCallStepAdditions"
%FLG: SData = 2097152
Requirements = Obj
%FLG: Requirements = 2097152

[DEF, SequenceCall.TS.Requirements]
Links = Strs

[SequenceCall.TS.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[DEF, SequenceCall.Result]
Error = "TYPE, Error"
Status = Str
ReportText = Str
Common = "TYPE, CommonResults"

[SequenceCall.Result]
%FLG: Error = 4194304
%INSTFLG: Error = 4194304
%INSTOVRD: Error = 4194304
%FLG: Status = 4194304
%INSTFLG: Status = 4194304
%FLG: ReportText = 4194304
%INSTFLG: ReportText = 4194304
%INSTOVRD: Common = 4194304

[DEF, SeqCallStepAdditions]
%LOCATION = "StdTypes"
SFPath = "TYPE, Path"
SFPathExpr = "TYPE, Expression"
SeqName = Str
SeqNameExpr = "TYPE, Expression"
ActualArgs = Arguments
%FLG: ActualArgs = 2097152
UseCurFile = Bool
SpecifyByExpr = Bool
Prototype = Obj
%FLG: Prototype = 2097152
UsePrototype = Bool
SpecifyHostByExpr = Bool
RemoteExecution = Bool
RemoteHost = Str
RemoteHostExpr = "TYPE, Expression"
AutoWaitAsync = Bool
CreateThreadSuspended = Bool
AsyncThreadExpr = "TYPE, Expression"
AsyncApartmentThreaded = Bool
ThreadAffinityOption = Num
CustomThreadAffinity = "TYPE, Expression"
ThreadOpt = Num
ExecModelOpt = Num
ExecTypeMask = Num
ExecTypeMaskExpr = "TYPE, Expression"
ExecBreakOnEntryExpr = "TYPE, Expression"
ExecModelPath = "TYPE, Path"
ExecModelPathExpr = "TYPE, Expression"
ExecSync = Bool
Trace = Str
IgnoreTerminate = Bool
%ROOT_TYPE = True

[SeqCallStepAdditions]
%INSTFLG: ActualArgs = 2097152
%INSTFLG: Prototype = 2097152
AutoWaitAsync = True
CustomThreadAffinity = "RunState.Engine.Is64Bit? -1ui64 : -1"
ExecModelOpt = 1
ExecBreakOnEntryExpr = "False"
Trace = "Don't Change"
%TIMESTAMP = 1466536089
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, PassFailTest]
%LOCATION = "StepTypes"
Substeps = "TYPE, StepTypeSubstepsArray"
DescriptionFormat = "TYPE, Expression"
%FLG: DescriptionFormat = 524288
DefaultNameFormat = "TYPE, Expression"
%FLG: DefaultNameFormat = 524288
Menu = "TYPE, StepTypeMenu"
AdditionalResultsHints = Objs
%FLG: AdditionalResultsHints = 524288
TS = "TYPE, TEInf"
NI_Data = "TYPE, StepTypeNIData"
Result = Obj
InBuf = Str
DataSource = "TYPE, Expression"
CodeTemplates = Str
%FLG: CodeTemplates = 524288
BlockStartTypes = Str
%FLG: BlockStartTypes = 524288
BlockEndTypes = Str
%FLG: BlockEndTypes = 524288
AppliesToBlockStructure = Bool
%FLG: AppliesToBlockStructure = 524288
CanEncapsulate = Bool
%FLG: CanEncapsulate = 524288
%ROOT_TYPE = True

[PassFailTest]
%HI: Substeps = [0]
%INSTFLG: Substeps = 524312
%INSTOVRD: Substeps = 655384
DescriptionFormat Line0001 = "ResStr(\"NI_STEPTYPES\", \"PASSFAIL_DESCRIPTION_NAME\") + ((\"%ModuleDescription\" == \"\") ? \"\" : \",  %ModuleDescrip"
DescriptionFormat Line0002 = "tion\")"
%FLG: DescriptionFormat = 4194328
%INSTFLG: DescriptionFormat = 4718616
%INSTOVRD: DescriptionFormat = 4718616
DefaultNameFormat = "ResStr(\"NI_STEPTYPES\", \"PASSFAIL_DEF_STEP_NAME\")"
%FLG: DefaultNameFormat = 4194328
%INSTFLG: DefaultNameFormat = 4718616
%INSTOVRD: DefaultNameFormat = 4718616
%INSTFLG: Menu = 524312
%INSTOVRD: Menu = 524312
%FLG: AdditionalResultsHints = 4194328
%INSTFLG: TS = 262168
%INSTOVRD: TS = 4456472
%FLG: Result = 4194304
%INSTFLG: Result = 4194304
DataSource = "Step.Result.PassFail"
CodeTemplates Line0001 = "PassFailLabVIEW|PassFailCVI|PassFailVB.NET|PassFailCSharp.NET|PassFailC++.NET|PassFailVC++_Template|PassFailHTB80_Templa"
CodeTemplates Line0002 = "te|PassFailHTB72_Template|PassFail_Template"
%FLG: CodeTemplates = 4194328
%FLG: BlockStartTypes = 4194328
%FLG: BlockEndTypes = 4194328
%FLG: AppliesToBlockStructure = 4194328
%FLG: CanEncapsulate = 4194328
%TIMESTAMP = 1462492640
%VERSION = "16.0.0.0"
%TYPELASTMOD = "16.0.0.131"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554446

[DEF, PassFailTest.Substeps]
%[0] = Step
%TYPE: %[0] = "EditSubstep"

[DEF, PassFailTest.Substeps[0].TS]
SData = "TYPE, FlexCStepAdditions"
%FLG: SData = 2097152

[PassFailTest.Substeps[0].TS.SData.Call]
LibPath = "CommonSubsteps.dll"
Func = "EditPassFailStep"
%HI: Parms = [3]

[DEF, PassFailTest.Substeps[0].TS.SData.Call.Parms]
%[0] = "TYPE, FCParameter"
%[1] = "TYPE, FCParameter"
%[2] = "TYPE, FCParameter"
%[3] = "TYPE, FCParameter"

[PassFailTest.Substeps[0].TS.SData.Call.Parms[0]]
Name = "Return Value"
Type = 3
ObjType = 2
%INSTOVRD: ResultAct = 5177369
%INSTOVRD: Flags = 5177369

[PassFailTest.Substeps[0].TS.SData.Call.Parms[1]]
Name = "sequenceContext"
Type = 4
%INSTOVRD: ResultAct = 5177369
ArgVal = "ThisContext"
%INSTOVRD: Flags = 5177369

[PassFailTest.Substeps[0].TS.SData.Call.Parms[2]]
Name = "reserved"
%INSTOVRD: ResultAct = 5177369
ArgVal = "0"
%INSTOVRD: Flags = 5177369

[PassFailTest.Substeps[0].TS.SData.Call.Parms[3]]
Name = "changed"
ObjType = 2
NumPass = 1
%INSTOVRD: ResultAct = 5177369
ArgVal = "RunState.InitialSelection.SelectedFile.ChangeCount"
%INSTOVRD: Flags = 5177369

[PassFailTest.Substeps[0].TS]
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 2097152
ConnectionLifetime = 0

[PassFailTest.Substeps[0]]
%INSTFLG: TS = 262168
%INSTOVRD: TS = 262168
MenuName = "ResStr(\"NI_STEPTYPES\", \"PASSFAIL_EDIT_STEP_MENU_NAME\")"
SupportsReadOnly = True
HasEditPanel = True

[PassFailTest.Substeps[0].Result]
%INSTOVRD: Error = 4194304
%INSTFLG: ReportText = 0
%INSTOVRD: Common = 4194304

[DEF, PassFailTest.Substeps[0]]
%NAME = "Edit"

[PassFailTest.Menu]
ItemName = "ResStr(\"NI_STEPTYPES\", \"PASSFAIL_MENU_ITEM_NAME\")"
Group = "Tests"

[DEF, PassFailTest.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[DEF, PassFailTest.TS]
SData = Obj
%FLG: SData = 2097152
Requirements = Obj
%FLG: Requirements = 2097152

[PassFailTest.TS]
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7143448
ConnectionLifetime = 0
StatusExpr Line0001 = "Step.DataSource != \"Step.Result.PassFail\" ? Step.Result.PassFail = Evaluate(Step.DataSource) : False, Step.Result.Pass"
StatusExpr Line0002 = "Fail ? \"Passed\" : \"Failed\" "
%INSTFLG: StatusExpr = 1
%INSTOVRD: StatusExpr = 5046297
%FLG: Requirements = 1
%INSTFLG: Requirements = 1

[DEF, PassFailTest.TS.Requirements]
Links = Strs

[PassFailTest.TS.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[PassFailTest.NI_Data]
%HI: EditPanels = [0]

[PassFailTest.NI_Data.EditPanels]
%[0] = "NIStepTypeControls.dll|NationalInstruments.TestStand.StepTypeControls.PassFailTestTabInfo"

[DEF, PassFailTest.Result]
Error = "TYPE, Error"
Status = Str
PassFail = Bool
ReportText = Str
Common = "TYPE, CommonResults"

[PassFailTest.Result]
%FLG: Error = 4194304
%INSTFLG: Error = 4194304
%INSTOVRD: Error = 4194304
%FLG: Status = 4194304
%INSTFLG: Status = 4194304
%FLG: ReportText = 4194304
%INSTFLG: ReportText = 4194304
%INSTOVRD: Common = 4194304

[DEF, EditSubstep]
%LOCATION = "StepTypes"
DescriptionFormat = "TYPE, Expression"
%FLG: DescriptionFormat = 524288
DefaultNameFormat = "TYPE, Expression"
%FLG: DefaultNameFormat = 524288
BlockStartTypes = Str
%FLG: BlockStartTypes = 524288
BlockEndTypes = Str
%FLG: BlockEndTypes = 524288
AppliesToBlockStructure = Bool
%FLG: AppliesToBlockStructure = 524288
Menu = "TYPE, StepTypeMenu"
Substeps = "TYPE, StepTypeSubstepsArray"
CodeTemplates = Str
%FLG: CodeTemplates = 524288
AdditionalResultsHints = Objs
%FLG: AdditionalResultsHints = 524288
TS = "TYPE, TEInf"
NI_Data = "TYPE, StepTypeNIData"
Result = Obj
CanEncapsulate = Bool
%FLG: CanEncapsulate = 524288
MenuName = "TYPE, Expression"
SupportsReadOnly = Bool
HasEditPanel = Bool
%ROOT_TYPE = True

[EditSubstep]
DescriptionFormat = "\"%ModuleDescription\""
%FLG: DescriptionFormat = 4194328
%INSTFLG: DescriptionFormat = 4718616
%INSTOVRD: DescriptionFormat = 4718616
DefaultNameFormat = "ResStr(\"NI_STEPTYPES\", \"EDIT_DEF_SUBSTEP_NAME\")"
%FLG: DefaultNameFormat = 4194328
%INSTFLG: DefaultNameFormat = 4718616
%INSTOVRD: DefaultNameFormat = 4718616
%FLG: BlockStartTypes = 4194328
%FLG: BlockEndTypes = 4194328
%FLG: AppliesToBlockStructure = 4194328
CodeTemplates Line0001 = "DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|Defa"
CodeTemplates Line0002 = "ultHTB80_Template|Default_Template"
%FLG: CodeTemplates = 4194328
%FLG: AdditionalResultsHints = 4194328
%INSTFLG: TS = 4456472
%FLG: Result = 4194304
%INSTFLG: Result = 4194304
%FLG: CanEncapsulate = 4194328
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554438
%INSTFLG = 4194304
%INSTOVRD = 4194304

[EditSubstep.Menu]
CanBeSubstepType = True
CanOnlyBeSubstepType = True
ItemName = "ResStr(\"NI_STEPTYPES\", \"EDIT_SUBSTEP_MENU_ITEM_NAME\")"
Group = "EditSubsteps"

[DEF, EditSubstep.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[DEF, EditSubstep.TS]
SData = Obj
%FLG: SData = 2097152
Requirements = Obj
%FLG: Requirements = 2097152

[EditSubstep.TS]
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7274521
%FLG: Requirements = 1
%INSTFLG: Requirements = 1

[DEF, EditSubstep.TS.Requirements]
Links = Strs

[EditSubstep.TS.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[DEF, EditSubstep.Result]
Error = "TYPE, Error"
Status = Str
ReportText = Str
Common = "TYPE, CommonResults"

[EditSubstep.Result]
%FLG: Error = 4194304
%INSTFLG: Error = 4194304
%FLG: Status = 4194304
%INSTFLG: Status = 4194304
%FLG: ReportText = 4194304
%INSTFLG: ReportText = 4194304

[DEF, FlexCStepAdditions]
%LOCATION = "StdTypes"
Call = ExternalCall
ModuleSrcPath = "TYPE, Path"
ModulePrjPath = "TYPE, Path"
ModuleWorkspacePath = "TYPE, Path"
CodeTemplateName = Str
ModuleCreateSrcType = Num
%ROOT_TYPE = True

[DEF, FlexCStepAdditions.Call]
LibPath = "TYPE, Path"
Func = Str
Parms = Objs

[DEF, FlexCStepAdditions.Call.Parms]
%EPTYPE = "TYPE, FCParameter"
%FLG: %EPTYPE = 131072
%[0] = "TYPE, FCParameter"

[FlexCStepAdditions.Call]
%HI: Parms = [0]

[FlexCStepAdditions.Call.Parms[0]]
Name = "Return Value"
Type = 3

[FlexCStepAdditions]
%TIMESTAMP = 1466536146
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, FCParameter]
%LOCATION = "StdTypes"
Name = Str
Type = Num
NumType = Num
ObjType = Num
StructType = Str
NumPass = Num
StrPass = Num
ElemPass = Num
ArrayDimensionsSize = Objs
StrSize = "TYPE, Expression"
ResultAct = Num
ArgVal = "TYPE, Expression"
ArgDisplayVal = "TYPE, Expression"
Flags = Num
AdditionalResults = Obj
UserData = Obj
%FLG: UserData = 2097152
ArgValImag = "TYPE, Expression"
%ROOT_TYPE = True

[FCParameter]
Name = "_notNamed"
NumType = 4
StrSize = "1024"
%INSTOVRD: ResultAct = 5177368
%INSTOVRD: Flags = 5177368
%INSTFLG: UserData = 2097152
%TIMESTAMP = 1466536146
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, FCParameter.ArrayDimensionsSize]
%EPTYPE = "TYPE, Expression"
%FLG: %EPTYPE = 131072

[FCParameter.ArrayDimensionsSize]
%EPTYPE = "1024"

[DEF, FCParameter.AdditionalResults]
Input = "TYPE, NI_CommonCParameterResult"
Output = "TYPE, NI_CommonCParameterResult"

[DEF, Label]
%LOCATION = "StepTypes"
Substeps = "TYPE, StepTypeSubstepsArray"
DescriptionFormat = "TYPE, Expression"
%FLG: DescriptionFormat = 524288
DefaultNameFormat = "TYPE, Expression"
%FLG: DefaultNameFormat = 524288
Menu = "TYPE, StepTypeMenu"
AdditionalResultsHints = Objs
%FLG: AdditionalResultsHints = 524288
TS = "TYPE, TEInf"
NI_Data = "TYPE, StepTypeNIData"
Result = Obj
CodeTemplates = Str
%FLG: CodeTemplates = 524288
Description = Str
BlockStartTypes = Str
%FLG: BlockStartTypes = 524288
BlockEndTypes = Str
%FLG: BlockEndTypes = 524288
AppliesToBlockStructure = Bool
%FLG: AppliesToBlockStructure = 524288
CanEncapsulate = Bool
%FLG: CanEncapsulate = 524288
%ROOT_TYPE = True

[Label]
%HI: Substeps = [0]
%INSTFLG: Substeps = 524312
%INSTOVRD: Substeps = 655384
DescriptionFormat = "Step.Description"
%FLG: DescriptionFormat = 4194328
%INSTFLG: DescriptionFormat = 4718616
%INSTOVRD: DescriptionFormat = 4718616
DefaultNameFormat = "ResStr(\"NI_STEPTYPES\", \"LABEL_DEF_STEP_NAME\")"
%FLG: DefaultNameFormat = 4194328
%INSTFLG: DefaultNameFormat = 4718616
%INSTOVRD: DefaultNameFormat = 4718616
%INSTFLG: Menu = 524312
%INSTOVRD: Menu = 524312
%FLG: AdditionalResultsHints = 4194328
%INSTFLG: TS = 262168
%INSTOVRD: TS = 4456472
%FLG: Result = 4194304
%INSTFLG: Result = 4194304
%FLG: CodeTemplates = 4194328
%FLG: BlockStartTypes = 4194328
%FLG: BlockEndTypes = 4194328
%FLG: AppliesToBlockStructure = 4194328
%FLG: CanEncapsulate = 4194328
%TIMESTAMP = 1462492641
%VERSION = "16.0.0.0"
%TYPELASTMOD = "16.0.0.131"
%MINPRODVER = "16.0.0.0"
%TYPE_FLG = 33554446

[DEF, Label.Substeps]
%[0] = Step
%TYPE: %[0] = "EditSubstep"

[DEF, Label.Substeps[0].TS]
SData = "TYPE, FlexCStepAdditions"
%FLG: SData = 2097152

[Label.Substeps[0].TS.SData.Call]
LibPath = "CommonSubsteps.dll"
Func = "EditLabelStep"
%HI: Parms = [3]

[DEF, Label.Substeps[0].TS.SData.Call.Parms]
%[0] = "TYPE, FCParameter"
%[1] = "TYPE, FCParameter"
%[2] = "TYPE, FCParameter"
%[3] = "TYPE, FCParameter"

[Label.Substeps[0].TS.SData.Call.Parms[0]]
Name = "Return Value"
Type = 3
%INSTOVRD: ResultAct = 5177369
%INSTOVRD: Flags = 5177369

[Label.Substeps[0].TS.SData.Call.Parms[1]]
Name = "object"
Type = 4
%INSTOVRD: ResultAct = 5177369
ArgVal = "ThisContext"
%INSTOVRD: Flags = 5177369

[Label.Substeps[0].TS.SData.Call.Parms[2]]
Name = "reserved"
%INSTOVRD: ResultAct = 5177369
ArgVal = "0"
%INSTOVRD: Flags = 5177369

[Label.Substeps[0].TS.SData.Call.Parms[3]]
Name = "changed"
NumPass = 1
%INSTOVRD: ResultAct = 5177369
ArgVal = "RunState.InitialSelection.SelectedFile.ChangeCount"
ArgDisplayVal = "RunState.InitialSelection.SelectedFile.ChangeCount"
%INSTOVRD: Flags = 5177369

[Label.Substeps[0].TS]
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 2097152
ConnectionLifetime = 0

[Label.Substeps[0]]
%INSTFLG: TS = 262168
%INSTOVRD: TS = 262168
MenuName = "ResStr(\"NI_SUBSTEPS\", \"LABEL_EDIT_STEP_MENU_NAME\")"
SupportsReadOnly = True
HasEditPanel = True

[Label.Substeps[0].Result]
%INSTOVRD: Error = 4194304
%INSTFLG: ReportText = 0
%INSTOVRD: Common = 4194304

[DEF, Label.Substeps[0]]
%NAME = "Edit"

[Label.Menu]
ItemName = "ResStr(\"NI_STEPTYPES\", \"LABEL_MENU_ITEM_NAME\")"
Group = "NI_Miscellaneous"

[DEF, Label.AdditionalResultsHints]
%EPTYPE = "TYPE, NI_CustomResult"

[Label.TS]
Icon = "label.ico"
%INSTFLG: SData = 2097152
%INSTOVRD: SData = 7143448
ResultOption = 0
ConnectionLifetime = 0
%INSTFLG: PassAct = 1
%INSTOVRD: PassAct = 5046297
%INSTFLG: FailAct = 1
%INSTOVRD: FailAct = 5046297
%INSTFLG: PassActTarget = 1
%INSTOVRD: PassActTarget = 5046297
%INSTFLG: FailActTarget = 1
%INSTOVRD: FailActTarget = 5046297
CanSpecifyModule = False
%FLG: Requirements = 1
%INSTFLG: Requirements = 1

[DEF, Label.TS]
SData = "TYPE, NoneStepAdditions"
%FLG: SData = 2097152
Requirements = Obj
%FLG: Requirements = 2097152

[DEF, Label.TS.Requirements]
Links = Strs

[Label.TS.Requirements]
%FLG: Links = 71303168
%INSTFLG: Links = 71303168
%INSTOVRD: Links = 72286233

[Label.NI_Data]
%HI: EditPanels = [0]

[Label.NI_Data.EditPanels]
%[0] = "NIStepTypeControls.dll|NationalInstruments.TestStand.StepTypeControls.LabelTabInfo"

[DEF, Label.Result]
Error = "TYPE, Error"
Status = Str
ReportText = Str
Common = "TYPE, CommonResults"

[Label.Result]
%FLG: Error = 4194304
%INSTFLG: Error = 4194304
%INSTOVRD: Error = 4194304
%FLG: Status = 4194304
%INSTFLG: Status = 4194304
%FLG: ReportText = 4194304
%INSTFLG: ReportText = 4194304
%INSTOVRD: Common = 4194304

[DEF, NoneStepAdditions]
%LOCATION = "StdTypes"
%ROOT_TYPE = True

[NoneStepAdditions]
%TIMESTAMP = 1466536108
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, StepTypeNIData]
%LOCATION = "StdTypes"
EditPanels = Strs
%ROOT_TYPE = True

[StepTypeNIData]
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436
%INSTFLG = 4718616
%INSTOVRD = 4718616

[DEF, NI_CustomResult]
%LOCATION = "StdTypes"
Name = "TYPE, Expression"
ValueToLog = "TYPE, Expression"
Condition = "TYPE, Expression"
Flags = Num
CheckedState = Num
Type = "TYPE, NI_PropertyObjectType"
Elements = Objs
IsAnyType = Bool
%ROOT_TYPE = True

[NI_CustomResult]
Flags = 8192
CheckedState = 2
IsAnyType = True
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[NI_CustomResult.Flags]
%NUMFMT = "%#x"

[DEF, NI_PropertyObjectType]
%LOCATION = "StdTypes"
ValueType = Num
IsObject = Bool
TypeName = Str
ElementType = Objs
ArrayDimensions = "TYPE, NI_ArrayDimensions"
Representation = Num
ClassName = Str
%ROOT_TYPE = True

[NI_PropertyObjectType]
ValueType = 3
IsObject = True
Representation = 1
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, NI_ArrayDimensions]
%LOCATION = "StdTypes"
LowerBounds = Nums
UpperBounds = Nums
%ROOT_TYPE = True

[NI_ArrayDimensions]
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[DEF, NI_ActiveXParameterResult]
%LOCATION = "StdTypes"
Condition = "TYPE, Expression"
Flags = Num
CheckedState = Num
%ROOT_TYPE = True

[NI_ActiveXParameterResult]
Flags = 8192
CheckedState = 1
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[NI_ActiveXParameterResult.Flags]
%NUMFMT = "%#x"

[DEF, NI_CommonCParameterResult]
%LOCATION = "StdTypes"
Condition = "TYPE, Expression"
Flags = Num
CheckedState = Num
%ROOT_TYPE = True

[NI_CommonCParameterResult]
Flags = 8192
CheckedState = 1
%TIMESTAMP = 1466535380
%VERSION = "16.0.0.185"
%TYPELASTMOD = "16.0.0.185"
%MINPRODVER = "16.0.0.0"
%FLG = 24
%TYPE_FLG = 33554436

[NI_CommonCParameterResult.Flags]
%NUMFMT = "%#x"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidaqmx.offlinecfg sha256=50bb4c6d6a6ea7d3dd20550208cbe5e5603d770199dc2edd93bc54ee9782fddf bytes=461 -->
## FILE: systemtests/nidaqmx.offlinecfg

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidaqmx.offlinecfg`
- sha256: `50bb4c6d6a6ea7d3dd20550208cbe5e5603d770199dc2edd93bc54ee9782fddf`
- bytes: 461

````text
<?xml version="1.0" encoding="utf-8"?>
<SystemConfiguration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" schemaVersion="1.0" xmlns="http://www.ni.com/TestStand/SemiconductorModule/SystemConfiguration.xsd">
  <PXIChassis Number="1" Model="NI PXIe-1085">
    <PXI Name="dev1" Model="NI PXIe-6363" Slot="2" />
    <PXI Name="dev2" Model="NI PXIe-6363" Slot="3" />
  </PXIChassis>
</SystemConfiguration>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidaqmx.pinmap sha256=00db4e6a52b1dfd7e444b0558dcc100dd59d83f0b5466bd42e70ce598611aa36 bytes=943 -->
## FILE: systemtests/nidaqmx.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidaqmx.pinmap`
- sha256: `00db4e6a52b1dfd7e444b0558dcc100dd59d83f0b5466bd42e70ce598611aa36`
- bytes: 943

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDAQmxTask name="Task1" taskType="ai" channelList="dev1/ai0,dev2/ai1" />
		<NIDAQmxTask name="Task2" taskType="ao" channelList="dev1/ao1,dev2/ao0" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="Task1" channel="dev2/ai1" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="Task1" channel="dev1/ai0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="Task2" channel="dev1/ao1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="Task2" channel="dev2/ao0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidaqmx_codemodules.py sha256=cbaddaf64392fb139866cf6a674e2a87d2c713f302581982d4e8b31b1f48bc36 bytes=2551 -->
## FILE: systemtests/nidaqmx_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidaqmx_codemodules.py`
- sha256: `cbaddaf64392fb139866cf6a674e2a87d2c713f302581982d4e8b31b1f48bc36`
- bytes: 2551

````python
import nidaqmx
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext
from sessionutils import get_task_name_from_task


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    # get task names and channel lists
    ai_task_names, ai_channel_lists = tsm_context.get_all_nidaqmx_task_names("ai")
    ao_task_names, ao_channel_lists = tsm_context.get_all_nidaqmx_task_names("ao")

    # create and set ai tasks
    for task_name, channel_list in zip(ai_task_names, ai_channel_lists):
        task = nidaqmx.Task(task_name)
        task.ai_channels.add_ai_voltage_chan(channel_list)
        tsm_context.set_nidaqmx_task(task_name, task)

    # create and set ao tasks
    for task_name, channel_list in zip(ao_task_names, ao_channel_lists):
        task = nidaqmx.Task(task_name)
        task.ao_channels.add_ao_voltage_chan(channel_list)
        tsm_context.set_nidaqmx_task(task_name, task)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_task_names,
    expected_channel_lists,
):
    pin_query, tasks, channel_lists = tsm_context.pins_to_nidaqmx_tasks(pins)
    expected_instrument_channels = set(zip(expected_task_names, expected_channel_lists))
    valid_channels = []

    for task, channel_list in zip(tasks, channel_lists):
        # call some methods on the session to ensure no errors
        task.timing.cfg_samp_clk_timing(1e3, "OnboardClock", samps_per_chan=10)
        task.in_stream.channels_to_read = task.ai_channels[channel_list]
        task.start()
        task.read()
        task.stop()

        # check instrument channel we received is in the set of instrument channels we expected
        task_name = get_task_name_from_task(task)
        actual_instrument_channel = (task_name, channel_list)
        valid_channel = actual_instrument_channel in expected_instrument_channels
        valid_channels.append([valid_channel] * len(channel_list.split(", ")))
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    tasks = tsm_context.get_all_nidaqmx_tasks("")
    for task in tasks:
        task.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidcpower.pinmap sha256=5c9a5a97d4689d93c39b6d692a8297492ba44119ccec63afbf00658a2cd7920e bytes=722 -->
## FILE: systemtests/nidcpower.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidcpower.pinmap`
- sha256: `5c9a5a97d4689d93c39b6d692a8297492ba44119ccec63afbf00658a2cd7920e`
- bytes: 722

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DCPower1" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidcpower_codemodules.py sha256=dba759d6bf7b523cf5514f26ee3c36e95a4071c0a80577def44790d436cd4efd bytes=2464 -->
## FILE: systemtests/nidcpower_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidcpower_codemodules.py`
- sha256: `dba759d6bf7b523cf5514f26ee3c36e95a4071c0a80577def44790d436cd4efd`
- bytes: 2464

````python
import nidcpower
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4162", "BoardType": "PXIe"}}


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    resource_strings = tsm_context.get_all_nidcpower_resource_strings()
    for resource_string in resource_strings:
        session = nidcpower.Session(resource_string, options=OPTIONS)
        tsm_context.set_nidcpower_session(resource_string, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_channel_strings,
):
    pin_query, sessions, channel_strings = tsm_context.pins_to_nidcpower_sessions(pins)
    expected_instrument_channels = set(
        expected_channel_string.replace(" ", "")  # remove spaces
        for expected_channel_string in expected_channel_strings
    )
    valid_channels = []

    for session, channel_string in zip(sessions, channel_strings):
        # call some methods on the session to ensure no errors
        channel_session = session.channels[channel_string]
        channel_session.abort()
        channel_session.output_function = nidcpower.OutputFunction.DC_CURRENT
        channel_session.current_level = 1e-3
        channel_session.output_enabled = True
        channel_session.source_delay = 250e-6
        channel_session.initiate()
        channel_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        channel_session.measure_multiple()

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_channels = session.io_resource_descriptor.replace(" ", "")
        channel_count = len(channel_string.split(","))
        valid_channels.append(
            [actual_instrument_channels in expected_instrument_channels] * channel_count
        )
        expected_instrument_channels -= {actual_instrument_channels}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidcpower_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital.digilevels sha256=0458471ba344d892ad4a19e54be197ba0c2e4a639ee07f55a8e1387fc3c64646 bytes=788 -->
## FILE: systemtests/nidigital.digilevels

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital.digilevels`
- sha256: `0458471ba344d892ad4a19e54be197ba0c2e4a639ee07f55a8e1387fc3c64646`
- bytes: 788

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="DUTPin1">
        <Vil>DC.Vl</Vil>
        <Vih>DC.Vh</Vih>
        <Vol>DC.Vl</Vol>
        <Voh>DC.Vh</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="DUTPin2">
        <Vil>DC.Vl</Vil>
        <Vih>DC.Vh</Vih>
        <Vol>DC.Vl</Vol>
        <Voh>DC.Vh</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital.digiproj sha256=625b16899cf23d9d34cf1f84ffd679a5d28c8afbbd317b64e02dc3eb5cb66815 bytes=3435 -->
## FILE: systemtests/nidigital.digiproj

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital.digiproj`
- sha256: `625b16899cf23d9d34cf1f84ffd679a5d28c8afbbd317b64e02dc3eb5cb66815`
- bytes: 3435

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="683565FCFDE4827C59FFFD41071B52AA" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.2.50247" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="5.3.1.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.2.50247" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.2.50247" Name="Digital Pattern Editor" Version="20.6.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="4" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="7" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="9" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="12" ModelDefinitionType="PinMap" Name="nidigital\.pinmap" StoragePath="nidigital.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="13" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="nidigital\.digipat" StoragePath="nidigital.digipat" />
			<FileReference Id="14" ModelDefinitionType="TimingDefinition" Name="nidigital\.digitiming" StoragePath="nidigital.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="nidigital\.specs" StoragePath="nidigital.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="nidigital\.digilevels" StoragePath="nidigital.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="21" ModelDefinitionType="SourceWaveformDefinition" Name="nidigital\.tdms" StoragePath="nidigital.tdms" />
			<FileReference Id="22" ModelDefinitionType="CaptureWaveformDefinition" Name="nidigital\.digicapture" StoragePath="nidigital.digicapture" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="6" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital.digitiming sha256=9bb8688b1c744d162369e5d0580ae81ce4c9db59f2da1cf115da55d73c047e09 bytes=1147 -->
## FILE: systemtests/nidigital.digitiming

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital.digitiming`
- sha256: `9bb8688b1c744d162369e5d0580ae81ce4c9db59f2da1cf115da55d73c047e09`
- bytes: 1147

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="tset">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="DUTPin1">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>AC.Period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>AC.Period / 2</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="DUTPin2">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>AC.Period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>AC.Period / 2</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital.pinmap sha256=302eb0626d83835b978da8b1a0845127778bdfa254e3f2be741ae9565f37c13b bytes=987 -->
## FILE: systemtests/nidigital.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital.pinmap`
- sha256: `302eb0626d83835b978da8b1a0845127778bdfa254e3f2be741ae9565f37c13b`
- bytes: 987

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Group1" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Group2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DigitalPattern2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital.specs sha256=d086c8b6b216b3229d02b31295daf213c145b73f7c79bb7a794cf6e6658791f3 bytes=567 -->
## FILE: systemtests/nidigital.specs

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital.specs`
- sha256: `d086c8b6b216b3229d02b31295daf213c145b73f7c79bb7a794cf6e6658791f3`
- bytes: 567

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="DC">
    <f:Formula symbol="Vh">
      <f:Definition>3.3 V</f:Definition>
    </f:Formula>
    <f:Formula symbol="Vl">
      <f:Definition>0 V</f:Definition>
    </f:Formula>
  </Section>
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>20 ns</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidigital_codemodules.py sha256=e9dcbec3ccd901caf6aff9d5c9bf71332f90f645f100b9945df5355284b821f4 bytes=6251 -->
## FILE: systemtests/nidigital_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidigital_codemodules.py`
- sha256: `e9dcbec3ccd901caf6aff9d5c9bf71332f90f645f100b9945df5355284b821f4`
- bytes: 6251

````python
import re
import nidigital
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "driver_setup": {"Model": "6570"}}


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        session = nidigital.Session(instrument_name, options=OPTIONS)
        session.load_pin_map(tsm_context.pin_map_file_path)
        session.load_specifications_levels_and_timing(
            tsm_context.nidigital_project_specifications_file_paths,
            tsm_context.nidigital_project_levels_file_paths,
            tsm_context.nidigital_project_timing_file_paths,
        )
        session.apply_levels_and_timing("nidigital", "nidigital")
        for pattern_file_path in tsm_context.nidigital_project_pattern_file_paths:
            session.load_pattern(pattern_file_path)
        tsm_context.set_nidigital_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure_ppmu(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_pin_set_strings,
):
    pin_query, sessions, pin_set_strings = tsm_context.pins_to_nidigital_sessions_for_ppmu(pins)
    expected_instrument_pin_sets = set(zip(expected_instrument_names, expected_pin_set_strings))
    valid_pin_sets = []

    for session, pin_set_string in zip(sessions, pin_set_strings):
        # call some methods on the session to ensure no errors
        session.pins[pin_set_string].ppmu_aperture_time = 4e-6
        session.pins[pin_set_string].ppmu_aperture_time_units = (
            nidigital.PPMUApertureTimeUnits.SECONDS
        )
        session.pins[pin_set_string].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT
        session.pins[pin_set_string].ppmu_current_level_range = 2e-6
        session.pins[pin_set_string].ppmu_current_level = 2e-6
        session.pins[pin_set_string].ppmu_voltage_limit_high = 3.3
        session.pins[pin_set_string].ppmu_voltage_limit_low = 0
        session.pins[pin_set_string].ppmu_source()
        session.pins[pin_set_string].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        session.abort()

        # check instrument pin set we received is in the set of instrument pin sets we expected
        actual_instrument_pin_set = (session.io_resource_descriptor, pin_set_string)
        num_pins_for_session = len(pin_set_string.split(","))
        valid_pin_sets.extend(
            [actual_instrument_pin_set in expected_instrument_pin_sets] * num_pins_for_session
        )
        expected_instrument_pin_sets -= {actual_instrument_pin_set}

    pin_query.publish(valid_pin_sets, "ValidPinSetStrings")
    num_missing_pin_sets = [len(expected_instrument_pin_sets)] * len(valid_pin_sets)
    pin_query.publish(num_missing_pin_sets, "NumMissingPinSetStrings")


@nitsm.codemoduleapi.code_module
def measure_pattern(
    tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_site_lists
):
    pin_query, sessions, site_lists = tsm_context.pins_to_nidigital_sessions_for_pattern(pins)
    expected_instrument_site_lists = set(zip(expected_instrument_names, expected_site_lists))
    valid_site_lists = []
    re_pattern = re.compile(r"\s*site(\d+)")

    for session, site_list in zip(sessions, site_lists):
        # call some methods on the session to ensure no errors
        session.sites[site_list].burst_pattern("start_label")

        # check instrument site we received is in the set of instrument sites we expected
        actual_instrument_site_list = (session.io_resource_descriptor, site_list)
        actual_in_expected = actual_instrument_site_list in expected_instrument_site_lists
        site_numbers = (int(re_pattern.match(site)[1]) for site in site_list.split(","))
        valid_site_lists.append({site: actual_in_expected for site in site_numbers})
        expected_instrument_site_lists -= {actual_instrument_site_list}

    pin_query.publish_pattern_results(valid_site_lists, "ValidSiteLists")
    num_missing_site_lists = [len(expected_instrument_site_lists)] * len(tsm_context.site_numbers)
    tsm_context.publish_per_site(num_missing_site_lists, "NumMissingSiteLists")


@nitsm.codemoduleapi.code_module
def check_project_paths(
    tsm_context: SemiconductorModuleContext,
    specifications_paths,
    levels_paths,
    timing_paths,
    pattern_paths,
    source_waveform_paths,
    capture_waveform_paths,
):
    site_count = len(tsm_context.site_numbers)
    valid_project_paths = [
        tsm_context.nidigital_project_specifications_file_paths == tuple(specifications_paths)
    ] * site_count
    valid_levels_paths = [
        tsm_context.nidigital_project_levels_file_paths == tuple(levels_paths)
    ] * site_count
    valid_timing_paths = [
        tsm_context.nidigital_project_timing_file_paths == tuple(timing_paths)
    ] * site_count
    valid_pattern_paths = [
        tsm_context.nidigital_project_pattern_file_paths == tuple(pattern_paths)
    ] * site_count
    valid_source_waveform_paths = [
        tsm_context.nidigital_project_source_waveform_file_paths == tuple(source_waveform_paths)
    ] * site_count
    valid_capture_waveform_paths = [
        tsm_context.nidigital_project_capture_waveform_file_paths == tuple(capture_waveform_paths)
    ] * site_count

    tsm_context.publish_per_site(valid_project_paths, "ValidSpecificationsPaths")
    tsm_context.publish_per_site(valid_levels_paths, "ValidLevelsPaths")
    tsm_context.publish_per_site(valid_timing_paths, "ValidTimingPaths")
    tsm_context.publish_per_site(valid_pattern_paths, "ValidPatternPaths")
    tsm_context.publish_per_site(valid_source_waveform_paths, "ValidSourceWaveformPaths")
    tsm_context.publish_per_site(valid_capture_waveform_paths, "ValidCaptureWaveformPaths")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidigital_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidmm.pinmap sha256=af1fec2ea4f1a1677bf35671faf11ba2965fabd2433d792486d14b6a6f7e81a2 bytes=642 -->
## FILE: systemtests/nidmm.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidmm.pinmap`
- sha256: `af1fec2ea4f1a1677bf35671faf11ba2965fabd2433d792486d14b6a6f7e81a2`
- bytes: 642

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDmmInstrument name="DMM1" />
		<NIDmmInstrument name="DMM2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DMM1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DMM2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nidmm_codemodules.py sha256=9e5fabedb1dc330798525d0e19cf85b6040df08e2796a2b57b4bbe8c8cbc76d0 bytes=1766 -->
## FILE: systemtests/nidmm_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nidmm_codemodules.py`
- sha256: `9e5fabedb1dc330798525d0e19cf85b6040df08e2796a2b57b4bbe8c8cbc76d0`
- bytes: 1766

````python
import nidmm
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4071", "BoardType": "PXI"}}


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nidmm_instrument_names()
    for instrument_name in instrument_names:
        session = nidmm.Session(instrument_name, options=OPTIONS)
        tsm_context.set_nidmm_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
):
    pin_query, sessions = tsm_context.pins_to_nidmm_sessions(pins)
    expected_instrument_names = set(expected_instrument_names)
    valid_instruments = []

    for session in sessions:
        # call some methods on the session to ensure no errors
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.read()
        session.abort()

        # check instrument name we received is in the set of instrument names we expected
        actual_instrument_name = session.io_resource_descriptor
        valid_instruments.append(actual_instrument_name in expected_instrument_names)
        expected_instrument_names -= {actual_instrument_name}

    pin_query.publish(valid_instruments)
    num_missing_instruments = [len(expected_instrument_names)] * len(sessions)
    pin_query.publish(num_missing_instruments, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nidmm_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nifgen.pinmap sha256=28af673ca0ccb2197b6f636f77e069ee063b69a166439ce9636f741c55bdcd82 bytes=941 -->
## FILE: systemtests/nifgen.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nifgen.pinmap`
- sha256: `28af673ca0ccb2197b6f636f77e069ee063b69a166439ce9636f741c55bdcd82`
- bytes: 941

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIFGenInstrument name="FGEN1_5433 (2CH)" numberOfChannels="2" />
		<NIFGenInstrument name="FGEN2_5433 (2CH)" numberOfChannels="2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="1" instrument="FGEN2_5433 (2CH)" channel="1" />
		<Connection pin="DUTPin1" siteNumber="0" instrument="FGEN1_5433 (2CH)" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="FGEN1_5433 (2CH)" channel="1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="FGEN2_5433 (2CH)" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nifgen_codemodules.py sha256=ec3e62f24446430f80767261d5104e0f2f9bc37584c578b21859b0998570158f bytes=2258 -->
## FILE: systemtests/nifgen_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nifgen_codemodules.py`
- sha256: `ec3e62f24446430f80767261d5104e0f2f9bc37584c578b21859b0998570158f`
- bytes: 2258

````python
import nifgen
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext
from sessionutils import get_resource_name_from_session


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_nifgen_instrument_names()
    for instrument_name in instrument_names:
        name, model = instrument_name.split("_")
        session = nifgen.Session(name, options={"Simulate": True, "DriverSetup": {"Model": model}})
        tsm_context.set_nifgen_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_channel_lists,
):
    pin_query, sessions, channel_lists = tsm_context.pins_to_nifgen_sessions(pins)
    expected_instrument_channels = set(zip(expected_instrument_names, expected_channel_lists))
    valid_channels = []

    for session, channel_list in zip(sessions, channel_lists):
        # call some methods on the session to ensure no errors
        session.output_mode = nifgen.OutputMode.FUNC
        session.channels[channel_list].configure_standard_waveform(nifgen.Waveform.DC, 0, 0, 1)
        session.channels[channel_list].output_enabled = True
        session.initiate()
        session.abort()

        # check instrument channel we received is in the set of instrument channels we expected
        resource_name = get_resource_name_from_session(session)
        actual_instrument_channel = (resource_name, channel_list)
        valid_channel = actual_instrument_channel in expected_instrument_channels
        valid_channels.append([valid_channel] * len(channel_list.split(", ")))
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [
        [len(expected_instrument_channels)] * len(row) for row in valid_channels
    ]
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_nifgen_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nirelaydriver.pinmap sha256=d69744749fd78cc514596d7f0e427addd4b2a092e0ec9eb005696daeea5f0fc8 bytes=1591 -->
## FILE: systemtests/nirelaydriver.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/nirelaydriver.pinmap`
- sha256: `d69744749fd78cc514596d7f0e427addd4b2a092e0ec9eb005696daeea5f0fc8`
- bytes: 1591

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.4" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
		<NIRelayDriverModule name="RelayDriver2" numberOfControlLines="64" />
	</Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Relays>
		<SiteRelay name="SiteRelay1" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
		<SiteRelay name="SiteRelay2" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
		<SystemRelay name="SystemRelay1" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
	</Relays>
	<RelayGroups>
		<RelayGroup name="RelayGroup1">
			<RelayReference relay="SiteRelay1" />
			<RelayReference relay="SiteRelay2" />
			<RelayReference relay="SystemRelay1" />
		</RelayGroup>
	</RelayGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<RelayConnection relay="SiteRelay1" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="SiteRelay1" siteNumber="1" relayDriverModule="RelayDriver1" controlLine="K1" />
		<RelayConnection relay="SiteRelay2" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K2" />
		<RelayConnection relay="SiteRelay2" siteNumber="1" relayDriverModule="RelayDriver1" controlLine="K3" />
		<SystemRelayConnection relay="SystemRelay1" relayDriverModule="RelayDriver2" controlLine="K0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/nirelaydriver_codemodules.py sha256=04fe433c1377f288df374defecb5bd142530f4b17cd15f7369737f5236f4540c bytes=2403 -->
## FILE: systemtests/nirelaydriver_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/nirelaydriver_codemodules.py`
- sha256: `04fe433c1377f288df374defecb5bd142530f4b17cd15f7369737f5236f4540c`
- bytes: 2403

````python
import niswitch
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


class MockSwitchSession(niswitch.Session):
    def __init__(self, resource_name, *args, **kwargs):
        # resource name must be empty string to simulate an niswitch session
        self.__resource_name = resource_name
        super().__init__("", *args, **kwargs)

    @property
    def io_resource_descriptor(self):
        return self.__resource_name


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: SemiconductorModuleContext):
    module_names = tsm_context.get_relay_driver_module_names()
    for module_name in module_names:
        session = MockSwitchSession(module_name, topology="2567/Independent", simulate=True)
        tsm_context.set_relay_driver_niswitch_session(module_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: SemiconductorModuleContext,
    relays,
    expected_instrument_names,
    expected_relay_names,
):
    sessions, relay_names = tsm_context.relays_to_relay_driver_niswitch_sessions(relays)
    expected_instrument_relays = set(zip(expected_instrument_names, expected_relay_names))
    valid_channels = []

    for session, relay_name in zip(sessions, relay_names):
        # call some methods on the session to ensure no errors
        session.relay_control(relay_name, niswitch.RelayAction.OPEN)
        session.relay_control(relay_name, niswitch.RelayAction.CLOSE)
        session.wait_for_debounce()

        # check instrument channels we received is in the set of instrument channels we expected
        actual_instrument_relays = (session.io_resource_descriptor, relay_name)
        valid_channels.append(actual_instrument_relays in expected_instrument_relays)
        missing_instrument_relays = expected_instrument_relays - {actual_instrument_relays}

    site_count = len(tsm_context.site_numbers)
    tsm_context.publish_per_site([all(valid_channels)] * site_count, "AllChannelsAreValid")
    num_missing_channels = [len(missing_instrument_relays)] * site_count
    tsm_context.publish_per_site(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: SemiconductorModuleContext):
    sessions = tsm_context.get_all_relay_driver_niswitch_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/niscope.pinmap sha256=7ffc3faf4085d91e30471c767a0e09db33deb0a31883d9182e23afe23231df7a bytes=728 -->
## FILE: systemtests/niscope.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/niscope.pinmap`
- sha256: `7ffc3faf4085d91e30471c767a0e09db33deb0a31883d9182e23afe23231df7a`
- bytes: 728

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope_1" />
		<NIScopeInstrument name="SCOPE2" numberOfChannels="4" group="Scope_2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="SCOPE2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/niscope_codemodules.py sha256=3b5e524853b7cde8914f3dcbdcc04d0e81adf418c315aa5e5ec0533dc1515f3c bytes=2002 -->
## FILE: systemtests/niscope_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/niscope_codemodules.py`
- sha256: `3b5e524853b7cde8914f3dcbdcc04d0e81adf418c315aa5e5ec0533dc1515f3c`
- bytes: 2002

````python
import niscope
import nitsm.codemoduleapi


@nitsm.codemoduleapi.code_module
def open_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext):
    instrument_names = tsm_context.get_all_niscope_instrument_names()
    for instrument_name in instrument_names:
        session = niscope.Session(instrument_name, options={"Simulate": True})
        tsm_context.set_niscope_session(instrument_name, session)


@nitsm.codemoduleapi.code_module
def measure(
    tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext,
    pins,
    expected_instrument_names,
    expected_channel_lists,
):
    pin_query, sessions, channel_lists = tsm_context.pins_to_niscope_sessions(pins)
    expected_instrument_channels = set(zip(expected_instrument_names, expected_channel_lists))
    valid_channels = []

    for session, channel_list in zip(sessions, channel_lists):
        # call some methods on the session to ensure no errors
        pin_session = session.channels[channel_list]
        session.abort()
        pin_session.configure_vertical(range=10.0, offset=5.0, coupling=niscope.VerticalCoupling.DC)
        session.initiate()
        pin_session.fetch_measurement_stats(niscope.ScalarMeasurement.VOLTAGE_MAX)

        # check instrument channel we received is in the set of instrument channels we expected
        actual_instrument_channel = (session.io_resource_descriptor, channel_list)
        valid_channels.append(actual_instrument_channel in expected_instrument_channels)
        expected_instrument_channels -= {actual_instrument_channel}

    pin_query.publish(valid_channels)
    num_missing_channels = [len(expected_instrument_channels)] * len(sessions)
    pin_query.publish(num_missing_channels, "NumMissing")


@nitsm.codemoduleapi.code_module
def close_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext):
    sessions = tsm_context.get_all_niscope_sessions()
    for session in sessions:
        session.close()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/sessionutils.py sha256=3bd1ae3631c5e1612ce4ceaa4dc1d19c4e7e202eab4a06aefba0484c0da0e0e2 bytes=528 -->
## FILE: systemtests/sessionutils.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/sessionutils.py`
- sha256: `3bd1ae3631c5e1612ce4ceaa4dc1d19c4e7e202eab4a06aefba0484c0da0e0e2`
- bytes: 528

````python
import re


def get_resource_name_from_session(session) -> str:
    """
    session.io_resource_descriptor isn't 100% reliable for simulated sessions. This method uses a
    regular expression to get the resource name from the object's repr.
    """

    return re.search(r"resource_name='(\w*)'", repr(session)).group(1)


def get_task_name_from_task(task) -> str:
    """Uses a regular expression on the task's repr to return the task's name."""
    return re.search(r"Task\(name=(\w*)\)", repr(task)).group(1)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/site_and_global_data.pinmap sha256=302eb0626d83835b978da8b1a0845127778bdfa254e3f2be741ae9565f37c13b bytes=987 -->
## FILE: systemtests/site_and_global_data.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/site_and_global_data.pinmap`
- sha256: `302eb0626d83835b978da8b1a0845127778bdfa254e3f2be741ae9565f37c13b`
- bytes: 987

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Group1" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Group2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DigitalPattern2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/site_and_global_data_codemodules.py sha256=abdb00b68028aa80242f44163c338ae1be36e7dc761e2e4948ad6831ad1d6b8c bytes=1854 -->
## FILE: systemtests/site_and_global_data_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/site_and_global_data_codemodules.py`
- sha256: `abdb00b68028aa80242f44163c338ae1be36e7dc761e2e4948ad6831ad1d6b8c`
- bytes: 1854

````python
import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


@nitsm.codemoduleapi.code_module
def set_global_data(tsm_context: SemiconductorModuleContext, data_id, data):
    tsm_context.set_global_data(data_id, data)


@nitsm.codemoduleapi.code_module
def check_global_data(tsm_context: SemiconductorModuleContext, data_id, data):
    site_count = len(tsm_context.site_numbers)
    global_data_exists = [tsm_context.global_data_exists(data_id)] * site_count
    tsm_context.publish_per_site(global_data_exists, "GlobalDataExists")

    valid_global_data = [tsm_context.get_global_data(data_id) == data] * site_count
    tsm_context.publish_per_site(valid_global_data, "ValidGlobalData")


@nitsm.codemoduleapi.code_module
def set_site_data(tsm_context: SemiconductorModuleContext, data_id, data):
    tsm_context.set_site_data(data_id, data)


@nitsm.codemoduleapi.code_module
def check_site_data(tsm_context: SemiconductorModuleContext, data_id, data):
    site_count = len(tsm_context.site_numbers)
    site_data_exists = [tsm_context.site_data_exists(data_id)] * site_count
    tsm_context.publish_per_site(site_data_exists, "SiteDataExists")

    valid_site_data = [tsm_context.get_site_data(data_id) == tuple(data)] * site_count
    tsm_context.publish_per_site(valid_site_data, "ValidSiteData")


@nitsm.codemoduleapi.code_module
def clear_site_data(tsm_context: SemiconductorModuleContext, data_id):
    tsm_context.set_site_data(data_id, [])


@nitsm.codemoduleapi.code_module
def check_site_data_cleared(tsm_context: SemiconductorModuleContext, data_id):
    site_count = len(tsm_context.site_numbers)
    site_data_does_not_exist = [not tsm_context.site_data_exists(data_id)] * site_count
    tsm_context.publish_per_site(site_data_does_not_exist, "SiteDataDoesNotExist")
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/specifications.pinmap sha256=2174e2a8faf3b4fc51c66d8632c568c203fb9cf4d843ffe728b13c842f75fd55 bytes=353 -->
## FILE: systemtests/specifications.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/specifications.pinmap`
- sha256: `2174e2a8faf3b4fc51c66d8632c568c203fb9cf4d843ffe728b13c842f75fd55`
- bytes: 353

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.4" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments></Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections></Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/specifications.specs sha256=d8eb58ac91395709bda4bcea489ded23bfbe152b8e7b8d1c89cfa606797c2d4f bytes=534 -->
## FILE: systemtests/specifications.specs

- repository: `ni/nitsm-python`
- source_path: `systemtests/specifications.specs`
- sha256: `d8eb58ac91395709bda4bcea489ded23bfbe152b8e7b8d1c89cfa606797c2d4f`
- bytes: 534

````text
<?xml version="1.0" encoding="utf-8" ?>
<Specifications xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd" xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0">
  <Section name="DC">
    <f:Formula symbol="gnd">
      <f:Definition>0.0</f:Definition>
    </f:Formula>
    <f:Formula symbol="vcc_max">
      <f:Definition>5.0</f:Definition>
    </f:Formula>
    <f:Formula symbol="vcc_typ">
      <f:Definition>3.3</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/specifications_codemodules.py sha256=e2c6c287cf40cce58768a3e3e7e9aac657635adf86df874fcf045c9f801514ba bytes=484 -->
## FILE: systemtests/specifications_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/specifications_codemodules.py`
- sha256: `e2c6c287cf40cce58768a3e3e7e9aac657635adf86df874fcf045c9f801514ba`
- bytes: 484

````python
import nitsm.codemoduleapi


@nitsm.codemoduleapi.code_module
def measure(tsm_context, namespaced_symbols, expected_values):
    tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext
    if isinstance(namespaced_symbols, str):
        actual_values = tsm_context.get_specifications_value(namespaced_symbols)
    else:
        actual_values = tsm_context.get_specifications_values(namespaced_symbols)
    tsm_context.publish_per_site(expected_values == actual_values)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/switch.pinmap sha256=4e0206032c5ed4fc0b68f731b5ae2f08c28d47e077f91db59c32b17c1b96993c bytes=913 -->
## FILE: systemtests/switch.pinmap

- repository: `ni/nitsm-python`
- source_path: `systemtests/switch.pinmap`
- sha256: `4e0206032c5ed4fc0b68f731b5ae2f08c28d47e077f91db59c32b17c1b96993c`
- bytes: 913

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital" />
		<Multiplexer name="Multiplexer1" multiplexerTypeId="SimulatedMultiplexer" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<MultiplexedConnection instrument="DigitalPattern1" channel="0">
			<MultiplexedDUTPinRoute pin="DUTPin1" siteNumber="0" multiplexer="Multiplexer1" routeName="DUTPin1Site0" />
			<MultiplexedDUTPinRoute pin="DUTPin1" siteNumber="1" multiplexer="Multiplexer1" routeName="DUTPin1Site1" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/switch_codemodules.py sha256=53e70d74f3fdbbab0b81ac8354814c545cc962eb88533069efefed159b682373 bytes=2074 -->
## FILE: systemtests/switch_codemodules.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/switch_codemodules.py`
- sha256: `53e70d74f3fdbbab0b81ac8354814c545cc962eb88533069efefed159b682373`
- bytes: 2074

````python
import nitsm.codemoduleapi as tsm

MULTIPLEXER_TYPE_ID = "SimulatedMultiplexer"


@tsm.code_module
def open_sessions(tsm_context: tsm.SemiconductorModuleContext):
    switch_names = tsm_context.get_all_switch_names(MULTIPLEXER_TYPE_ID)
    for switch_name in switch_names:
        tsm_context.set_switch_session(switch_name, switch_name, MULTIPLEXER_TYPE_ID)
    # nidigital sessions are required to satisfy the pin map but won't be used
    instrument_names = tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        tsm_context.set_nidigital_session(instrument_name, ...)


@tsm.code_module
def measure(
    tsm_context: tsm.SemiconductorModuleContext, pin, expected_switch_names, expected_switch_routes
):
    site_contexts, switch_names, switch_routes = tsm_context.pin_to_switch_sessions(
        pin, MULTIPLEXER_TYPE_ID
    )
    expected_names_and_routes = set(zip(expected_switch_names, expected_switch_routes))
    valid_names_and_routes = []

    for site_context, switch_name, switch_route in zip(site_contexts, switch_names, switch_routes):
        # check switch route we received is in the set of switch routes we expected
        actual_name_and_route = (switch_name, switch_route)
        valid_name_and_route = actual_name_and_route in expected_names_and_routes
        valid_names_and_routes.append(valid_name_and_route)
        expected_names_and_routes.discard(actual_name_and_route)
        # get a pin query context and publish result
        pin_query = site_context.pins_to_nidigital_session_for_ppmu(pin)[0]
        pin_query.publish(valid_name_and_route)

    # publish missing switch routes for all sites
    pin_query = tsm_context.pins_to_nidigital_session_for_ppmu(pin)[0]
    num_missing_routes = [len(expected_names_and_routes)] * len(site_contexts)
    pin_query.publish(num_missing_routes, "NumMissing")


@tsm.code_module
def close_sessions(tsm_context: tsm.SemiconductorModuleContext):
    tsm_context.get_all_switch_sessions(MULTIPLEXER_TYPE_ID)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=systemtests/test_system.py sha256=a5f0c4d50be1f504d3cb9fa75ada50cd7e86fddb010d4574aaf1e2e0594f6ee8 bytes=1491 -->
## FILE: systemtests/test_system.py

- repository: `ni/nitsm-python`
- source_path: `systemtests/test_system.py`
- sha256: `a5f0c4d50be1f504d3cb9fa75ada50cd7e86fddb010d4574aaf1e2e0594f6ee8`
- bytes: 1491

````python
import pytest


@pytest.mark.sequence_file("nidmm.seq")
def test_nidmm(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidcpower.seq")
def test_nidcpower(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nifgen.seq")
def test_nifgen(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidaqmx.seq")
@pytest.mark.offline_mode("nidaqmx.offlinecfg")
def test_nidaqmx(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("niscope.seq")
def test_niscope(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nidigital.seq")
def test_nidigital(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("nirelaydriver.seq")
def test_nirelaydriver(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("custom_instruments.seq")
def test_custom_instruments(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("site_and_global_data.seq")
def test_site_and_global_data(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("specifications.seq")
def test_specifications(system_test_runner):
    assert system_test_runner.run()


@pytest.mark.sequence_file("switch.seq")
def test_switch(system_test_runner):
    assert system_test_runner.run()
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/__init__.py

- repository: `ni/nitsm-python`
- source_path: `tests/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/codemoduleapi.pinmap sha256=2174e2a8faf3b4fc51c66d8632c568c203fb9cf4d843ffe728b13c842f75fd55 bytes=353 -->
## FILE: tests/codemoduleapi.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/codemoduleapi.pinmap`
- sha256: `2174e2a8faf3b4fc51c66d8632c568c203fb9cf4d843ffe728b13c842f75fd55`
- bytes: 353

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.4" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments></Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections></Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/conftest.py sha256=90ac45a23913dc4bf0e97f496df72119c2572a4b18cb5407ef8f5482ac144a02 bytes=3366 -->
## FILE: tests/conftest.py

- repository: `ni/nitsm-python`
- source_path: `tests/conftest.py`
- sha256: `90ac45a23913dc4bf0e97f496df72119c2572a4b18cb5407ef8f5482ac144a02`
- bytes: 3366

````python
import enum
import os.path
import pytest
import win32com.client
import win32com.client.selecttlb
import pythoncom
import nitsm.codemoduleapi

try:
    _standalone_tsm_context_tlb = win32com.client.selecttlb.FindTlbsWithDescription(
        "NI TestStand Semiconductor Module Standalone Semiconductor Module Context"
    )[0]
except IndexError:
    raise RuntimeError(
        "The TSM Standalone Semiconductor Module Context component is not installed. "
        "Contact one of the repository owners to determine how to obtain this "
        "non-public component."
    )


@pytest.fixture
def _published_data_reader_factory(request):
    # get absolute path of the pin map file which is assumed to be relative to the test module
    pin_map_path = request.node.get_closest_marker("pin_map").args[0]
    module_directory = os.path.dirname(request.module.__file__)
    pin_map_path = os.path.join(module_directory, pin_map_path)

    published_data_reader_factory = win32com.client.Dispatch(
        "NationalInstruments.TestStand.SemiconductorModule.Restricted.PublishedDataReaderFactory"
    )
    return published_data_reader_factory.NewSemiconductorModuleContext(pin_map_path)


@pytest.fixture
def standalone_tsm_context_com_object(_published_data_reader_factory):
    return _published_data_reader_factory[0]


@pytest.fixture
def standalone_tsm_context(standalone_tsm_context_com_object):
    return nitsm.codemoduleapi.SemiconductorModuleContext(standalone_tsm_context_com_object)


class PublishedDataType(enum.Enum):
    Double = 0
    Boolean = 1
    String = 2


class PublishedData:
    def __init__(self, published_data_com_obj):
        self._published_data = win32com.client.CastTo(
            published_data_com_obj, "IPublishedData", _standalone_tsm_context_tlb
        )
        self._published_data._oleobj_ = self._published_data._oleobj_.QueryInterface(
            self._published_data.CLSID, pythoncom.IID_IDispatch
        )

    @property
    def boolean_value(self) -> bool:
        return self._published_data.BooleanValue

    @property
    def double_value(self) -> float:
        return self._published_data.DoubleValue

    @property
    def pin(self) -> str:
        return self._published_data.Pin

    @property
    def published_data_id(self) -> str:
        return self._published_data.PublishedDataId

    @property
    def site_number(self) -> int:
        return self._published_data.SiteNumber

    @property
    def string_value(self) -> str:
        return self._published_data.StringValue

    @property
    def type(self) -> PublishedDataType:
        return PublishedDataType(self._published_data.Type)


class PublishedDataReader:
    def __init__(self, published_data_reader_com_obj):
        self._published_data_reader = win32com.client.CastTo(
            published_data_reader_com_obj, "IPublishedDataReader", _standalone_tsm_context_tlb
        )

    def get_and_clear_published_data(self):
        published_data = self._published_data_reader.GetAndClearPublishedData()
        return [PublishedData(published_data_point) for published_data_point in published_data]


@pytest.fixture
def published_data_reader(_published_data_reader_factory):
    return PublishedDataReader(_published_data_reader_factory[1])
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/custom_instruments.pinmap sha256=884c88cac574e2f27d3a792aa31a3a1bcb350b890f81302914fc133ea048907a bytes=1031 -->
## FILE: tests/custom_instruments.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/custom_instruments.pinmap`
- sha256: `884c88cac574e2f27d3a792aa31a3a1bcb350b890f81302914fc133ea048907a`
- bytes: 1031

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<Instrument name="PXI0::16" instrumentTypeId="Relay1_Id">
			<ChannelGroup id="ChannelGroup">
				<Channel id="Ch0" />
				<Channel id="Ch1" />
				<Channel id="Ch2" />
			</ChannelGroup>
		</Instrument>
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI0::16" channel="Ch0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI0::16" channel="Ch1" />
		<SystemConnection pin="SystemPin1" instrument="PXI0::16" channel="Ch2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/general_and_advanced.pinmap sha256=d2d16c855a61cb776da3276a4ed51da8107370e4dc41e70bc7066b8b52c416fb bytes=1081 -->
## FILE: tests/general_and_advanced.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/general_and_advanced.pinmap`
- sha256: `d2d16c855a61cb776da3276a4ed51da8107370e4dc41e70bc7066b8b52c416fb`
- bytes: 1081

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<Instrument name="CustomInstrument1" instrumentTypeId="CustomInstrumentTypeId1">
			<ChannelGroup id="ChannelGroup">
				<Channel id="Ch0" />
				<Channel id="Ch1" />
				<Channel id="Ch2" />
			</ChannelGroup>
		</Instrument>
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="CustomInstrument1" channel="Ch0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="CustomInstrument1" channel="Ch1" />
		<SystemConnection pin="SystemPin1" instrument="CustomInstrument1" channel="Ch2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/multi_site.pinmap sha256=1f2b823d194b86562d9cad0adfc4214b65d8a8e2b9c2dcc1f0f2799dc7471df7 bytes=1216 -->
## FILE: tests/multi_site.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/multi_site.pinmap`
- sha256: `1f2b823d194b86562d9cad0adfc4214b65d8a8e2b9c2dcc1f0f2799dc7471df7`
- bytes: 1216

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.2" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
		<SystemPin name="SystemPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin1" siteNumber="2" instrument="DigitalPattern2" channel="0" />
		<Connection pin="DUTPin1" siteNumber="3" instrument="DigitalPattern2" channel="1" />
		<SystemConnection pin="SystemPin1" instrument="DigitalPattern1" channel="2" />
		<SystemConnection pin="SystemPin2" instrument="DigitalPattern2" channel="2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nidaqmx.pinmap sha256=c33570598bc6a525c0dd4e5b4907db918e8c1bbb2cbf07bb13bba29b22c302a9 bytes=1166 -->
## FILE: tests/nidaqmx.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nidaqmx.pinmap`
- sha256: `c33570598bc6a525c0dd4e5b4907db918e8c1bbb2cbf07bb13bba29b22c302a9`
- bytes: 1166

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDAQmxTask name="DAQmx1" taskType="ai" channelList="0,1,2,3" />
		<NIDAQmxTask name="DAQmx2" taskType="ai" channelList="0,1,2,3" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DAQmx1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DAQmx1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DAQmx1" channel="2" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DAQmx1" channel="3" />
		<SystemConnection pin="SystemPin1" instrument="DAQmx2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nidcpower.pinmap sha256=2c776a2825ca0d5b3a4bf45c3fd51ebfd54c2f3b62fae7af76052bec029718fd bytes=1630 -->
## FILE: tests/nidcpower.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nidcpower.pinmap`
- sha256: `2c776a2825ca0d5b3a4bf45c3fd51ebfd54c2f3b62fae7af76052bec029718fd`
- bytes: 1630

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="ChannelGroup1" channels="0,1" />
			<ChannelGroup name="ChannelGroup2" channels="2,3" />
		</NIDCPowerInstrument>
		<NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
			<ChannelGroup name="ChannelGroup1" channels="0,1" />
			<ChannelGroup name="ChannelGroup2" channels="2,3" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DCPower2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DCPower1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DCPower2" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="DCPower1" channel="2" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="DCPower2" channel="2" />
		<SystemConnection pin="SystemPin1" instrument="DCPower1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nidigital.pinmap sha256=be0bc77cfbeecd40428c8656e1273e27d6f42146f2d09ce6ead7f07578ae9968 bytes=1265 -->
## FILE: tests/nidigital.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nidigital.pinmap`
- sha256: `be0bc77cfbeecd40428c8656e1273e27d6f42146f2d09ce6ead7f07578ae9968`
- bytes: 1265

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital1" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Digital2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
			<PinReference pin="DUTPin2" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern1" channel="2" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DigitalPattern1" channel="3" />
		<SystemConnection pin="SystemPin1" instrument="DigitalPattern2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nidmm.pinmap sha256=e8071f0e437dc55aa39852d5b48cf5357c8b89f94857ee2502bf34b856887147 bytes=905 -->
## FILE: tests/nidmm.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nidmm.pinmap`
- sha256: `e8071f0e437dc55aa39852d5b48cf5357c8b89f94857ee2502bf34b856887147`
- bytes: 905

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDmmInstrument name="DMM1" />
		<NIDmmInstrument name="DMM2" />
		<NIDmmInstrument name="DMM3" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DMM1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DMM2" channel="0" />
		<SystemConnection pin="SystemPin1" instrument="DMM3" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nifgen.pinmap sha256=de79da13ff7fe85c23eb07a9eba51565903134c9c170a7b9c6097392a9dfd5e9 bytes=1064 -->
## FILE: tests/nifgen.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nifgen.pinmap`
- sha256: `de79da13ff7fe85c23eb07a9eba51565903134c9c170a7b9c6097392a9dfd5e9`
- bytes: 1064

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIFGenInstrument name="FGen1" numberOfChannels="2" />
		<NIFGenInstrument name="FGen2" numberOfChannels="2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
		<SystemPin name="SystemPin2" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
			<PinReference pin="SystemPin2" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="FGen1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="FGen1" channel="1" />
		<SystemConnection pin="SystemPin1" instrument="FGen2" channel="0" />
		<SystemConnection pin="SystemPin2" instrument="FGen2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/nirelaydriver.pinmap sha256=782f9826c5097a933c90f48fa7a5874a4bf46555a2832d2e12e12fcc719d7bfd bytes=1893 -->
## FILE: tests/nirelaydriver.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/nirelaydriver.pinmap`
- sha256: `782f9826c5097a933c90f48fa7a5874a4bf46555a2832d2e12e12fcc719d7bfd`
- bytes: 1893

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
		<NIRelayDriverModule name="RelayDriver2" numberOfControlLines="64" />
	</Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Relays>
		<SiteRelay name="SiteRelay1" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
		<SiteRelay name="SiteRelay2" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
		<SystemRelay name="SystemRelay1" openStateDisplayLabel="Open" closedStateDisplayLabel="Closed" />
	</Relays>
	<RelayGroups>
		<RelayGroup name="RelayGroup1">
			<RelayReference relay="SiteRelay1" />
			<RelayReference relay="SiteRelay2" />
			<RelayReference relay="SystemRelay1" />
		</RelayGroup>
	</RelayGroups>
	<RelayConfigurations>
		<RelayConfiguration name="RelayConfiguration1">
			<RelayPosition relay="SiteRelay1" position="Closed" />
			<RelayPosition relay="SiteRelay2" position="Closed" />
			<RelayPosition relay="SystemRelay1" position="Open" />
		</RelayConfiguration>
	</RelayConfigurations>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<RelayConnection relay="SiteRelay1" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="SiteRelay1" siteNumber="1" relayDriverModule="RelayDriver1" controlLine="K1" />
		<RelayConnection relay="SiteRelay2" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K2" />
		<RelayConnection relay="SiteRelay2" siteNumber="1" relayDriverModule="RelayDriver1" controlLine="K3" />
		<SystemRelayConnection relay="SystemRelay1" relayDriverModule="RelayDriver2" controlLine="K0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/niscope.pinmap sha256=5738e1dcb1245551795ae51705635a0ec55bda2645c0ac4b85e4b0d22e01add0 bytes=1028 -->
## FILE: tests/niscope.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/niscope.pinmap`
- sha256: `5738e1dcb1245551795ae51705635a0ec55bda2645c0ac4b85e4b0d22e01add0`
- bytes: 1028

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIScopeInstrument name="Scope1" numberOfChannels="4" group="Scope" />
		<NIScopeInstrument name="Scope2" numberOfChannels="4" group="Scope" />
		<NIScopeInstrument name="Scope3" numberOfChannels="4" group="Scope" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="SystemPin1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="Scope1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="Scope2" channel="0" />
		<SystemConnection pin="SystemPin1" instrument="Scope3" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/pinquerycontext.pinmap sha256=7939b8e7879a0a7b9e3c2aaeb2b94901224ab0a500de6b8206600cc613f93fd9 bytes=991 -->
## FILE: tests/pinquerycontext.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/pinquerycontext.pinmap`
- sha256: `7939b8e7879a0a7b9e3c2aaeb2b94901224ab0a500de6b8206600cc613f93fd9`
- bytes: 991

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital1" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Digital2" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DigitalPattern2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/publish.pinmap sha256=1f114c889bf8478fa06e5d2d2aba40d468cf1451978a33cff82c819e7a4a2387 bytes=1570 -->
## FILE: tests/publish.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/publish.pinmap`
- sha256: `1f114c889bf8478fa06e5d2d2aba40d468cf1451978a33cff82c819e7a4a2387`
- bytes: 1570

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.2" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin1" siteNumber="2" instrument="DigitalPattern1" channel="2" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern1" channel="3" />
		<Connection pin="DUTPin2" siteNumber="2" instrument="DigitalPattern1" channel="5" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="DigitalPattern1" channel="4" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="DigitalPattern1" channel="6" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="DigitalPattern2" channel="0" />
		<Connection pin="DUTPin3" siteNumber="2" instrument="DigitalPattern2" channel="1" />
		<SystemConnection pin="SystemPin1" instrument="DigitalPattern2" channel="2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/publish_single_site.pinmap sha256=68a2b36d4554861db885186d7777c928e2c226f12a8a7e17cbe1ff545e343de2 bytes=988 -->
## FILE: tests/publish_single_site.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/publish_single_site.pinmap`
- sha256: `68a2b36d4554861db885186d7777c928e2c226f12a8a7e17cbe1ff545e343de2`
- bytes: 988

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.2" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="DigitalPattern1" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="DigitalPattern2" channel="0" />
		<SystemConnection pin="SystemPin1" instrument="DigitalPattern2" channel="2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/site_and_global_data.pinmap sha256=c01a210b9bd5c936a41b4df7df4618c4e46fad8558642ee888fe1496fb56de60 bytes=353 -->
## FILE: tests/site_and_global_data.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/site_and_global_data.pinmap`
- sha256: `c01a210b9bd5c936a41b4df7df4618c4e46fad8558642ee888fe1496fb56de60`
- bytes: 353

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.1" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments></Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections></Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/switch.pinmap sha256=048cf9be77d8062ce02632aefa86cecd1bc8af6108eccf2a029cb576d81a20ab bytes=913 -->
## FILE: tests/switch.pinmap

- repository: `ni/nitsm-python`
- source_path: `tests/switch.pinmap`
- sha256: `048cf9be77d8062ce02632aefa86cecd1bc8af6108eccf2a029cb576d81a20ab`
- bytes: 913

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital" />
		<Multiplexer name="Multiplexer1" multiplexerTypeId="NIGenericMultiplexer" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<MultiplexedConnection instrument="DigitalPattern1" channel="0">
			<MultiplexedDUTPinRoute pin="DUTPin1" siteNumber="0" multiplexer="Multiplexer1" routeName="DUTPin1Site0" />
			<MultiplexedDUTPinRoute pin="DUTPin1" siteNumber="1" multiplexer="Multiplexer1" routeName="DUTPin1Site1" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_codemoduleapi.py sha256=e4b46d7a9e9ba52baf9294f45ec814f7656cd9e22e04eaf598fe3f58f2656579 bytes=4074 -->
## FILE: tests/test_codemoduleapi.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_codemoduleapi.py`
- sha256: `e4b46d7a9e9ba52baf9294f45ec814f7656cd9e22e04eaf598fe3f58f2656579`
- bytes: 4074

````python
import re
import pytest
from nitsm.codemoduleapi import code_module, SemiconductorModuleContext


@pytest.mark.pin_map("codemoduleapi.pinmap")
class TestCodeModuleApi:
    @staticmethod
    @code_module
    def test_static_method_converts(standalone_tsm_context_com_object):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    @staticmethod
    @code_module
    def test_static_method_does_not_convert(standalone_tsm_context):
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    @code_module
    def test_instance_method_converts(self, standalone_tsm_context_com_object):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    @code_module
    def test_instance_method_does_not_convert(self, standalone_tsm_context):
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    @classmethod
    @code_module
    def class_method_converts_core(cls, standalone_tsm_context_com_object):
        assert issubclass(cls, TestCodeModuleApi)
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)

    # pytest does not collect class methods so we need a static method that calls the class method
    @staticmethod
    def test_class_method_converts(standalone_tsm_context_com_object):
        TestCodeModuleApi.class_method_converts_core(standalone_tsm_context_com_object)

    @classmethod
    @code_module
    def class_method_does_not_convert_core(cls, standalone_tsm_context):
        assert issubclass(cls, TestCodeModuleApi)
        assert isinstance(standalone_tsm_context, SemiconductorModuleContext)

    # pytest does not collect class methods so we need a static method that calls the class method
    @staticmethod
    def test_class_method_does_not_convert(standalone_tsm_context):
        TestCodeModuleApi.class_method_converts_core(standalone_tsm_context)

    @code_module
    def _invalid_number_of_positional_arguments(self):
        """Does not contain a positional argument for the TSM context."""
        assert False  # should not reach this point

    def test_invalid_number_of_positional_arguments(self):
        with pytest.raises(TypeError) as e:
            self._invalid_number_of_positional_arguments()
        assert e.value.args[0] == (
            "The number of arguments to the code module is less than expected. It must "
            "accept as it's first argument the Semiconductor Module context passed from "
            "TestStand or another code module.",
        )

    # noinspection PyUnusedLocal
    @code_module
    def _tsm_context_not_first_positional_argument(self, first_argument, tsm_context):
        assert False  # should not reach this point

    @pytest.mark.parametrize("first_argument", (None, int(), str()))
    def test_tsm_context_not_first_positional_argument(
        self, first_argument, standalone_tsm_context_com_object
    ):
        with pytest.raises(Exception) as e:
            self._tsm_context_not_first_positional_argument(
                first_argument, standalone_tsm_context_com_object
            )
        assert re.match(
            r"Failed to convert Semiconductor Module context from class '.*'\.",
            e.value.args[0],
        )

    @pytest.mark.parametrize("second_argument", (None,))
    @code_module
    def test_positional_arguments_after_tsm_context(
        self, standalone_tsm_context_com_object, second_argument
    ):
        assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)


@pytest.mark.pin_map("codemoduleapi.pinmap")
@code_module
def test_function_converts(standalone_tsm_context_com_object):
    assert isinstance(standalone_tsm_context_com_object, SemiconductorModuleContext)


@pytest.mark.pin_map("codemoduleapi.pinmap")
@code_module
def test_function_does_not_convert(standalone_tsm_context):
    assert isinstance(standalone_tsm_context, SemiconductorModuleContext)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_custom_instruments.py sha256=411ef5d750e3dc7d6bfaf951a449e60fbd366b61e42f34ecaa51e207e72e0394 bytes=8280 -->
## FILE: tests/test_custom_instruments.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_custom_instruments.py`
- sha256: `411ef5d750e3dc7d6bfaf951a449e60fbd366b61e42f34ecaa51e207e72e0394`
- bytes: 8280

````python
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_custom_instrument_sessions(standalone_tsm_context):
    instrument_names, channel_group_ids, _ = standalone_tsm_context.get_custom_instrument_names(
        TestCustomInstruments.pin_map_instrument_type_id
    )
    sessions = tuple(range(len(instrument_names)))
    for instrument_name, channel_group_id, session in zip(
        instrument_names, channel_group_ids, sessions
    ):
        standalone_tsm_context.set_custom_session(
            TestCustomInstruments.pin_map_instrument_type_id,
            instrument_name,
            channel_group_id,
            session,
        )
    return sessions


@pytest.mark.pin_map("custom_instruments.pinmap")
class TestCustomInstruments:
    pin_map_instruments = ["PXI0::16"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_instrument_type_id = "Relay1_Id"

    def test_get_custom_instrument_names(self, standalone_tsm_context: SemiconductorModuleContext):
        (
            instrument_names,
            channel_group_ids,
            channel_lists,
        ) = standalone_tsm_context.get_custom_instrument_names(self.pin_map_instrument_type_id)
        assert isinstance(instrument_names, tuple)
        assert isinstance(channel_group_ids, tuple)
        assert isinstance(channel_lists, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        assert len(instrument_names) == len(channel_group_ids)
        assert len(instrument_names) == len(channel_lists)
        for instrument_name, channel_group_id, channel_list in zip(
            instrument_names, channel_group_ids, channel_lists
        ):
            assert isinstance(instrument_name, str)
            assert isinstance(channel_group_id, str)
            assert isinstance(channel_list, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_custom_session(self, standalone_tsm_context: SemiconductorModuleContext):
        (
            instrument_names,
            channel_group_ids,
            _,
        ) = standalone_tsm_context.get_custom_instrument_names(self.pin_map_instrument_type_id)
        sessions = tuple(range(len(instrument_names)))
        for instrument_name, channel_group_id, session in zip(
            instrument_names, channel_group_ids, sessions
        ):
            standalone_tsm_context.set_custom_session(
                self.pin_map_instrument_type_id, instrument_name, channel_group_id, session
            )
            assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_custom_sessions(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        (
            queried_sessions,
            queried_channel_group_ids,
            queried_channel_lists,
        ) = standalone_tsm_context.get_all_custom_sessions(self.pin_map_instrument_type_id)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_group_ids, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
        assert len(queried_sessions) == len(queried_channel_group_ids)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_group_id, queried_channel_list in zip(
            queried_sessions, queried_channel_group_ids, queried_channel_lists
        ):
            assert isinstance(queried_session, int)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_session_single_pin(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_group_id,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_custom_session(
            self.pin_map_instrument_type_id, "SystemPin1"
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, int)
        assert isinstance(queried_channel_group_id, str)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_session_multiple_pins(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_session,
            queried_channel_group_id,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_custom_session(self.pin_map_instrument_type_id, all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, int)
        assert isinstance(queried_channel_group_id, str)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_sessions_single_pin(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_group_ids,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_custom_sessions(
            self.pin_map_instrument_type_id, "PinGroup1"
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_group_ids, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
        assert len(queried_sessions) == len(queried_channel_group_ids)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_group_id, queried_channel_list in zip(
            queried_sessions, queried_channel_group_ids, queried_channel_lists
        ):
            assert isinstance(queried_session, int)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions

    def test_pins_to_custom_sessions_multiple_pin(
        self,
        standalone_tsm_context: SemiconductorModuleContext,
        simulated_custom_instrument_sessions,
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_group_ids,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_custom_sessions(
            self.pin_map_instrument_type_id, all_pins
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_group_ids, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_custom_instrument_sessions)
        assert len(queried_sessions) == len(queried_channel_group_ids)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_group_id, queried_channel_list in zip(
            queried_sessions, queried_channel_group_ids, queried_channel_lists
        ):
            assert isinstance(queried_session, int)
            assert isinstance(queried_channel_group_id, str)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_custom_instrument_sessions
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_general_and_advanced.py sha256=91d558eafa8eb2cfb707797d83c7002c284f647e508cf14814816439f606cf10 bytes=2086 -->
## FILE: tests/test_general_and_advanced.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_general_and_advanced.py`
- sha256: `91d558eafa8eb2cfb707797d83c7002c284f647e508cf14814816439f606cf10`
- bytes: 2086

````python
import pytest
from nitsm.codemoduleapi import Capability, InstrumentTypeIdConstants


@pytest.mark.pin_map("general_and_advanced.pinmap")
class TestGeneralAndAdvanced:
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_pin_names(self, standalone_tsm_context):
        queried_dut_pins, queried_system_pins = standalone_tsm_context.get_pin_names(
            InstrumentTypeIdConstants.ANY, Capability.ALL
        )
        assert isinstance(queried_dut_pins, tuple)
        assert isinstance(queried_system_pins, tuple)
        assert len(queried_dut_pins) == len(self.pin_map_dut_pins)
        assert len(queried_system_pins) == len(self.pin_map_system_pins)
        for dut_pin in queried_dut_pins:
            assert isinstance(dut_pin, str)
            assert dut_pin in self.pin_map_dut_pins
        for system_pin in queried_system_pins:
            assert isinstance(system_pin, str)
            assert system_pin in self.pin_map_system_pins

    def test_filter_pins_by_instrument_type(self, standalone_tsm_context):
        filtered_pins = standalone_tsm_context.filter_pins_by_instrument_type(
            self.pin_map_dut_pins, "CustomInstrumentTypeId1", Capability.ALL
        )
        assert isinstance(filtered_pins, tuple)
        assert len(filtered_pins) == len(self.pin_map_dut_pins)
        for filtered_pin in filtered_pins:
            assert isinstance(filtered_pin, str)
            assert filtered_pin in self.pin_map_dut_pins

    @pytest.mark.parametrize("pin_groups", ("PinGroup1", ["PinGroup1"]))
    def test_get_pins_in_pin_groups(self, standalone_tsm_context, pin_groups):
        pin_group_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        queried_pins = standalone_tsm_context.get_pins_in_pin_groups(pin_groups)
        assert isinstance(queried_pins, tuple)
        assert len(queried_pins) == len(pin_group_pins)
        for queried_pin in queried_pins:
            assert isinstance(queried_pin, str)
            assert queried_pin in pin_group_pins
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_multi_site.py sha256=f78652347c2e093674ad2e7941938b137a182083f0e9cc935e28b71719277fe4 bytes=1466 -->
## FILE: tests/test_multi_site.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_multi_site.py`
- sha256: `f78652347c2e093674ad2e7941938b137a182083f0e9cc935e28b71719277fe4`
- bytes: 1466

````python
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.mark.pin_map("multi_site.pinmap")
class TestMultiSite:
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1", "SystemPin2"]
    sites = 4  # [0, 1, 2, 3]

    def test_get_semiconductor_module_with_sites(self, standalone_tsm_context):
        # Get context for sites 1 and 3
        site_numbers = [1, 3]
        filtered_tsm_context = standalone_tsm_context.get_semiconductor_module_context_with_sites(
            site_numbers
        )
        filtered_sites = list(filtered_tsm_context.site_numbers)

        # Validate the site numbers
        assert len(site_numbers) == len(filtered_sites)
        assert site_numbers == filtered_sites
        for site in site_numbers:
            assert site in filtered_sites

        # Validate that a fully initialized SemiconductorModuleContext wrapper is returned
        assert isinstance(filtered_tsm_context, SemiconductorModuleContext)
        # Exercise another wrapper method to catch initialization regressions
        pin_names = list(
            filtered_tsm_context.get_pin_names()
        )  # Should contain DUTPins and SystemPins as a tuple
        assert isinstance(pin_names, list)
        # Each item is a tuple, change it to list and compare
        assert list(pin_names[0]) == self.pin_map_dut_pins
        assert list(pin_names[1]) == self.pin_map_system_pins
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nidaqmx.py sha256=4d6ce96860b121480705c7af22d6206c40f973ef1ed281a8a4bf4fa49834cb74 bytes=4948 -->
## FILE: tests/test_nidaqmx.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nidaqmx.py`
- sha256: `4d6ce96860b121480705c7af22d6206c40f973ef1ed281a8a4bf4fa49834cb74`
- bytes: 4948

````python
import nidaqmx
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nidaqmx_tasks(standalone_tsm_context):
    task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
    tasks = [nidaqmx.Task(tsk_name) for tsk_name in task_names]
    for task_name, task in zip(task_names, tasks):
        standalone_tsm_context.set_nidaqmx_task(task_name, task)
    yield tasks
    for task in tasks:
        task.close()


@pytest.mark.pin_map("nidaqmx.pinmap")
class TestNIDAQmx:
    pin_map_instruments = ["DAQmx1", "DAQmx2"]
    pin_map_dut_pins = ["DUTPin1", "DUTPin2"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_nidaqmx_task_names(self, standalone_tsm_context: SemiconductorModuleContext):
        task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
        assert isinstance(task_names, tuple)
        assert isinstance(channel_lists, tuple)
        assert len(task_names) == len(channel_lists)
        for task_name, channel_list in zip(task_names, channel_lists):
            assert isinstance(task_name, str)
            assert isinstance(channel_list, str)
            assert task_name in self.pin_map_instruments

    def test_set_nidaqmx_task(self, standalone_tsm_context: SemiconductorModuleContext):
        task_names, channel_lists = standalone_tsm_context.get_all_nidaqmx_task_names("")
        for task_name, channel_list in zip(task_names, channel_lists):
            with nidaqmx.Task(task_name) as task:
                standalone_tsm_context.set_nidaqmx_task(task_name, task)
                assert SemiconductorModuleContext._sessions[id(task)] is task

    def test_get_all_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        queried_tasks = standalone_tsm_context.get_all_nidaqmx_tasks("")
        assert isinstance(queried_tasks, tuple)
        assert len(queried_tasks) == len(simulated_nidaqmx_tasks)
        for queried_task in queried_tasks:
            assert isinstance(queried_task, nidaqmx.Task)
            assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_task_single_pin(self, standalone_tsm_context, simulated_nidaqmx_tasks):
        (
            pin_query_context,
            queried_task,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nidaqmx_task("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_task, nidaqmx.Task)
        assert isinstance(queried_channel_list, str)
        assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_task_multiple_pins(
        self, standalone_tsm_context, simulated_nidaqmx_tasks
    ):
        (
            pin_query_context,
            queried_task,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nidaqmx_task(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_task, nidaqmx.Task)
        assert isinstance(queried_channel_list, str)
        assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_tasks_single_pin(
        self, standalone_tsm_context, simulated_nidaqmx_tasks
    ):
        (
            pin_query_context,
            queried_tasks,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nidaqmx_tasks("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_tasks, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_tasks) == len(queried_channel_lists)
        for queried_task, queried_channel_list in zip(queried_tasks, queried_channel_lists):
            assert isinstance(queried_task, nidaqmx.Task)
            assert isinstance(queried_channel_list, str)
            assert queried_task in simulated_nidaqmx_tasks

    def test_pins_to_nidaqmx_tasks_multiple_pins(
        self, standalone_tsm_context, simulated_nidaqmx_tasks
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_tasks,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nidaqmx_tasks(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_tasks, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_tasks) == len(queried_channel_lists)
        for queried_task, queried_channel_list in zip(queried_tasks, queried_channel_lists):
            assert isinstance(queried_task, nidaqmx.Task)
            assert isinstance(queried_channel_list, str)
            assert queried_task in simulated_nidaqmx_tasks
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nidcpower.py sha256=64256d88bdb357d12d2ee32d020871b43828f9ac53ac3df0d392d5123b2d988f bytes=4993 -->
## FILE: tests/test_nidcpower.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nidcpower.py`
- sha256: `64256d88bdb357d12d2ee32d020871b43828f9ac53ac3df0d392d5123b2d988f`
- bytes: 4993

````python
import nidcpower
import pytest
from nitsm.pinquerycontexts import PinQueryContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "4162"}}


@pytest.fixture
def simulated_nidcpower_sessions(standalone_tsm_context):
    resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
    sessions = [
        nidcpower.Session(resource_string, options=OPTIONS) for resource_string in resource_strings
    ]
    for resource_string, session in zip(resource_strings, sessions):
        standalone_tsm_context.set_nidcpower_session(resource_string, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidcpower.pinmap")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
class TestNIDCPower:
    def test_get_all_nidcpower_resource_strings(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        assert isinstance(resource_strings, tuple)
        for resource_string in resource_strings:
            assert isinstance(resource_string, str)

    def test_set_nidcpower_session(self, standalone_tsm_context):
        resource_strings = standalone_tsm_context.get_all_nidcpower_resource_strings()
        for resource_string in resource_strings:
            with nidcpower.Session(resource_string, options=OPTIONS) as session:
                standalone_tsm_context.set_nidcpower_session(resource_string, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions):
        queried_sessions = standalone_tsm_context.get_all_nidcpower_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidcpower_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidcpower.Session)
            assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_session_single_pin(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pins_to_nidcpower_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_session_multiple_pins(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_string,
        ) = standalone_tsm_context.pins_to_nidcpower_session(["DUTPin1", "DUTPin2"])
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidcpower.Session)
        assert isinstance(queried_channel_string, str)
        assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_sessions_single_pin(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pins_to_nidcpower_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions

    def test_pins_to_nidcpower_sessions_multiple_pins(
        self, standalone_tsm_context, simulated_nidcpower_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_strings,
        ) = standalone_tsm_context.pins_to_nidcpower_sessions(["DUTPin1", "DUTPin3"])
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_strings, tuple)
        assert len(queried_sessions) == len(queried_channel_strings)
        for queried_session, queried_channel_string in zip(
            queried_sessions, queried_channel_strings
        ):
            assert isinstance(queried_session, nidcpower.Session)
            assert isinstance(queried_channel_string, str)
            assert queried_session in simulated_nidcpower_sessions
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nidigital.py sha256=f776c7823facd9faf656b8b40e151066dfe58ac20be8d18182bb2ba54907b46b bytes=9067 -->
## FILE: tests/test_nidigital.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nidigital.py`
- sha256: `f776c7823facd9faf656b8b40e151066dfe58ac20be8d18182bb2ba54907b46b`
- bytes: 9067

````python
import os.path
import nidigital
import pytest
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    sessions = [
        nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidigital_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidigital.pinmap")
class TestNIDigital:
    pin_map_instruments = ["DigitalPattern1", "DigitalPattern2"]
    pin_map_dut_pins = ["DUTPin1", "DUTPin2"]
    pin_map_system_pins = ["SystemPin1"]
    pin_map_file_path = os.path.join(os.path.dirname(__file__), "nidigital.pinmap")

    def test_get_all_nidigital_instrument_names(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nidigital_session(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
        for instrument_name in instrument_names:
            with nidigital.Session(
                instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
            ) as session:
                standalone_tsm_context.set_nidigital_session(instrument_name, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nidigital_sessions(self, standalone_tsm_context, simulated_nidigital_sessions):
        queried_sessions = standalone_tsm_context.get_all_nidigital_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidigital.Session)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_ppmu_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_ppmu("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_pattern_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_ppmu_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            pin_set_string,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(pin_set_string, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_session_for_pattern_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self.pin_map_dut_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidigital.Session)
        assert isinstance(site_list, str)
        assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_ppmu_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        for queried_session, pin_set_string in zip(queried_sessions, pin_set_strings):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_pattern_single_pin(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, site_list in zip(queried_sessions, site_lists):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(site_list, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_ppmu_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            pin_set_strings,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(pin_set_strings, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(pin_set_strings)
        for queried_session, pin_set_string in zip(queried_sessions, pin_set_strings):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(pin_set_string, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pins_to_nidigital_sessions_for_pattern_multiple_pins(
        self, standalone_tsm_context, simulated_nidigital_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(site_lists, tuple)
        assert len(queried_sessions) == len(simulated_nidigital_sessions)
        assert len(queried_sessions) == len(site_lists)
        for queried_session, site_list in zip(queried_sessions, site_lists):
            assert isinstance(queried_session, nidigital.Session)
            assert isinstance(site_list, str)
            assert queried_session in simulated_nidigital_sessions

    def test_pin_map_file_path(self, standalone_tsm_context):
        assert isinstance(standalone_tsm_context.pin_map_file_path, str)
        assert standalone_tsm_context.pin_map_file_path == self.pin_map_file_path

    # not implemented in standalone tsm and therefore can't be tested:
    # nidigital_project_specifications_file_paths
    # nidigital_project_levels_file_paths
    # nidigital_project_timing_file_paths
    # nidigital_project_pattern_file_paths
    # nidigital_project_source_waveform_file_paths
    # nidigital_project_capture_waveform_file_paths
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nidmm.py sha256=9c52de4c75e3dd7193d3537cf6780970ab58760ae390f62fb637b052bc0c5d50 bytes=4010 -->
## FILE: tests/test_nidmm.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nidmm.py`
- sha256: `9c52de4c75e3dd7193d3537cf6780970ab58760ae390f62fb637b052bc0c5d50`
- bytes: 4010

````python
import nidmm
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_nidmm_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    sessions = [
        nidmm.Session(instrument_name, options={"Simulate": True})
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidmm_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nidmm.pinmap")
class TestNIDMM:
    pin_map_instruments = ["DMM1", "DMM2", "DMM3"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_nidmm_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nidmm_session(self, standalone_tsm_context: SemiconductorModuleContext):
        instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        for instrument_name in instrument_names:
            with nidmm.Session(instrument_name, options={"Simulate": True}) as session:
                standalone_tsm_context.set_nidmm_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_nidmm_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_nidmm_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_nidmm_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions

    def test_pin_to_nidmm_session(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        pin_query_context, queried_session = standalone_tsm_context.pin_to_nidmm_session(
            "SystemPin1"
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nidmm.Session)
        assert queried_session in simulated_nidmm_sessions

    def test_pins_to_nidmm_sessions_single_pin(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        pin_query_context, queried_sessions = standalone_tsm_context.pins_to_nidmm_sessions(
            "PinGroup1"
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions

    def test_pins_to_nidmm_sessions_multiple_pins(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        pin_query_context, queried_sessions = standalone_tsm_context.pins_to_nidmm_sessions(
            all_pins
        )
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nidmm.Session)
            assert queried_session in simulated_nidmm_sessions
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nifgen.py sha256=1817d4ef5e6a77fcbac2c8b877ae31f5b290d6dc404f1746404841d1db194ebe bytes=5180 -->
## FILE: tests/test_nifgen.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nifgen.py`
- sha256: `1817d4ef5e6a77fcbac2c8b877ae31f5b290d6dc404f1746404841d1db194ebe`
- bytes: 5180

````python
import nifgen
import pytest
from nitsm.pinquerycontexts import PinQueryContext

OPTIONS = {"Simulate": True, "DriverSetup": {"Model": "5442", "BoardType": "PXIe"}}


@pytest.fixture
def simulated_nifgen_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
    sessions = [
        nifgen.Session(instrument_name, options=OPTIONS) for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nifgen_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("nifgen.pinmap")
class TestNIFGen:
    pin_map_instruments = ["FGen1", "FGen2"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1", "SystemPin2"]

    def test_get_all_nifgen_instrument_names(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_nifgen_session(self, standalone_tsm_context):
        instrument_names = standalone_tsm_context.get_all_nifgen_instrument_names()
        for instrument_name in instrument_names:
            with nifgen.Session(instrument_name, options=OPTIONS) as session:
                standalone_tsm_context.set_nifgen_session(instrument_name, session)
                assert standalone_tsm_context._sessions[id(session)] is session

    def test_get_all_nifgen_sessions(self, standalone_tsm_context, simulated_nifgen_sessions):
        queried_sessions = standalone_tsm_context.get_all_nifgen_sessions()
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, nifgen.Session)
            assert queried_session in simulated_nifgen_sessions

    def test_pin_to_nifgen_session_single_pin(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nifgen_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nifgen.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_session_muliple_pins(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_nifgen_session(self.pin_map_system_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, nifgen.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_sessions_single_pin(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nifgen_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions

    def test_pins_to_nifgen_sessions_multiple_pins(
        self, standalone_tsm_context, simulated_nifgen_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_nifgen_sessions(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(simulated_nifgen_sessions)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, nifgen.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_nifgen_sessions
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_nirelaydriver.py sha256=e8b764e01c53d42f19a20b4aba5f35f5b2ff8c1ac2212e79a4913d9ffa77dac7 bytes=10862 -->
## FILE: tests/test_nirelaydriver.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_nirelaydriver.py`
- sha256: `e8b764e01c53d42f19a20b4aba5f35f5b2ff8c1ac2212e79a4913d9ffa77dac7`
- bytes: 10862

````python
import niswitch
import pytest
from niswitch.enums import RelayAction, RelayPosition
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_niswitch_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_relay_driver_module_names()
    sessions = [
        niswitch.Session("", topology="2567/Independent", simulate=True) for _ in instrument_names
    ]  # resource name must be empty string to simulate an niswitch
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


def assert_relay_positions(standalone_tsm_context, pin_map_relays, relay_position):
    (
        niswitch_sessions,
        niswitch_relay_names,
    ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions(pin_map_relays)
    for niswitch_session, relay_names in zip(niswitch_sessions, niswitch_relay_names):
        for relay_name in relay_names.split(","):
            assert niswitch_session.get_relay_position(relay_name) == relay_position


@pytest.mark.pin_map("nirelaydriver.pinmap")
class TestNIRelayDriver:
    pin_map_instruments = ["RelayDriver1", "RelayDriver2"]
    pin_map_site_relays = ["SiteRelay1", "SiteRelay2"]
    pin_map_system_relays = ["SystemRelay1"]

    def test_get_relay_driver_module_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_relay_driver_module_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_get_relay_names(self, standalone_tsm_context: SemiconductorModuleContext):
        site_relays, system_relays = standalone_tsm_context.get_relay_names()
        assert isinstance(site_relays, tuple)
        assert isinstance(system_relays, tuple)
        for site_relay in site_relays:
            assert isinstance(site_relay, str)
            assert site_relay in self.pin_map_site_relays
        for system_relay in system_relays:
            assert isinstance(system_relay, str)
            assert system_relay in self.pin_map_system_relays

    def test_set_relay_driver_niswitch_session(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_relay_driver_module_names()
        for instrument_name in instrument_names:
            with niswitch.Session("", topology="2567/Independent", simulate=True) as session:
                standalone_tsm_context.set_relay_driver_niswitch_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_relay_driver_niswitch_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        queried_niswitch_sessions = standalone_tsm_context.get_all_relay_driver_niswitch_sessions()
        assert isinstance(queried_niswitch_sessions, tuple)
        assert len(queried_niswitch_sessions) == len(simulated_niswitch_sessions)
        for queried_niswitch_session in queried_niswitch_sessions:
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_session_single_relay(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_session,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_session("SystemRelay1")
        assert isinstance(queried_niswitch_session, niswitch.Session)
        assert isinstance(queried_niswitch_relay_names, str)
        assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_session_multiple_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_session,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_session(self.pin_map_site_relays)
        assert isinstance(queried_niswitch_session, niswitch.Session)
        assert isinstance(queried_niswitch_relay_names, str)
        assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_sessions_single_relay(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        (
            queried_niswitch_sessions,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions("RelayGroup1")
        assert isinstance(queried_niswitch_sessions, tuple)
        assert isinstance(queried_niswitch_relay_names, tuple)
        assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
        for queried_niswitch_session, queried_relay_name in zip(
            queried_niswitch_sessions, queried_niswitch_relay_names
        ):
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert isinstance(queried_relay_name, str)
            assert queried_niswitch_session in simulated_niswitch_sessions

    def test_relays_to_relay_driver_niswitch_sessions_multiple_relays(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions
    ):
        all_relays = self.pin_map_site_relays + self.pin_map_system_relays
        (
            queried_niswitch_sessions,
            queried_niswitch_relay_names,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_sessions(all_relays)
        assert isinstance(queried_niswitch_sessions, tuple)
        assert isinstance(queried_niswitch_relay_names, tuple)
        assert len(queried_niswitch_sessions) == len(queried_niswitch_relay_names)
        for queried_niswitch_session, queried_relay_name in zip(
            queried_niswitch_sessions, queried_niswitch_relay_names
        ):
            assert isinstance(queried_niswitch_session, niswitch.Session)
            assert isinstance(queried_relay_name, str)
            assert queried_niswitch_session in simulated_niswitch_sessions

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_apply_relay_configuration(self, standalone_tsm_context: SemiconductorModuleContext):
        standalone_tsm_context.apply_relay_configuration("RelayConfiguration1")
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_system_relays, RelayPosition.OPEN
        )

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_single_action_open_system_relay(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        (
            niswitch_session,
            niswitch_relay_name,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_session("SystemRelay1")
        standalone_tsm_context.control_relays("SystemRelay1", RelayAction.OPEN)
        assert niswitch_session.get_relay_position(niswitch_relay_name) == RelayPosition.OPEN

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_single_action_close_system_relay(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        (
            niswitch_session,
            niswitch_relay_name,
        ) = standalone_tsm_context.relays_to_relay_driver_niswitch_session("SystemRelay1")
        standalone_tsm_context.control_relays("SystemRelay1", RelayAction.CLOSE)
        assert niswitch_session.get_relay_position(niswitch_relay_name) == RelayPosition.CLOSED

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_single_action_open_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        standalone_tsm_context.control_relays(self.pin_map_site_relays, RelayAction.OPEN)
        assert_relay_positions(standalone_tsm_context, self.pin_map_site_relays, RelayPosition.OPEN)

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_single_action_close_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        standalone_tsm_context.control_relays(self.pin_map_site_relays, RelayAction.CLOSE)
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_multiple_action_open_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        standalone_tsm_context.control_relays(
            self.pin_map_site_relays, [RelayAction.OPEN] * len(self.pin_map_site_relays)
        )
        assert_relay_positions(standalone_tsm_context, self.pin_map_site_relays, RelayPosition.OPEN)

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_multiple_action_close_all_site_relays(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        standalone_tsm_context.control_relays(
            self.pin_map_site_relays, [RelayAction.CLOSE] * len(self.pin_map_site_relays)
        )
        assert_relay_positions(
            standalone_tsm_context, self.pin_map_site_relays, RelayPosition.CLOSED
        )

    @pytest.mark.usefixtures("simulated_niswitch_sessions")
    def test_control_relays_multiple_action_mixed_site_relay_positions(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        relay_actions = [
            RelayAction.OPEN if i % 2 else RelayAction.CLOSE
            for i in range(len(self.pin_map_site_relays))
        ]
        standalone_tsm_context.control_relays(self.pin_map_site_relays, relay_actions)
        for pin_map_site_relay, relay_action in zip(self.pin_map_site_relays, relay_actions):
            relay_position = (
                RelayPosition.OPEN if relay_action == RelayAction.OPEN else RelayPosition.CLOSED
            )
            assert_relay_positions(standalone_tsm_context, [pin_map_site_relay], relay_position)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_niscope.py sha256=b6b3721893597eccb71b148c320ac4f98362a348665168fe42af13f80df7c9d4 bytes=5410 -->
## FILE: tests/test_niscope.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_niscope.py`
- sha256: `b6b3721893597eccb71b148c320ac4f98362a348665168fe42af13f80df7c9d4`
- bytes: 5410

````python
import niscope
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext
from nitsm.pinquerycontexts import PinQueryContext


@pytest.fixture
def simulated_niscope_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
    sessions = [
        niscope.Session(instrument_name, options={"Simulate": True})
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_niscope_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("niscope.pinmap")
class TestNIScope:
    pin_map_instruments = ["Scope1,Scope2,Scope3"]
    pin_map_dut_pins = ["DUTPin1"]
    pin_map_system_pins = ["SystemPin1"]

    def test_get_all_niscope_instrument_names(
        self, standalone_tsm_context: SemiconductorModuleContext
    ):
        instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
        assert isinstance(instrument_names, tuple)
        assert len(instrument_names) == len(self.pin_map_instruments)
        for instrument_name in instrument_names:
            assert isinstance(instrument_name, str)
            assert instrument_name in self.pin_map_instruments

    def test_set_niscope_session(self, standalone_tsm_context: SemiconductorModuleContext):
        instrument_names = standalone_tsm_context.get_all_niscope_instrument_names()
        for instrument_name in instrument_names:
            with niscope.Session(instrument_name, options={"Simulate": True}) as session:
                standalone_tsm_context.set_niscope_session(instrument_name, session)
                assert SemiconductorModuleContext._sessions[id(session)] is session

    def test_get_all_niscope_sessions(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        queried_sessions = standalone_tsm_context.get_all_niscope_sessions()
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_niscope_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, niscope.Session)
            assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_session_single_pin(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_niscope_session("SystemPin1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, niscope.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_session_multiple_pins(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_session,
            queried_channel_list,
        ) = standalone_tsm_context.pins_to_niscope_session(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_session, niscope.Session)
        assert isinstance(queried_channel_list, str)
        assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_sessions_single_pin(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_niscope_sessions("PinGroup1")
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, niscope.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_niscope_sessions

    def test_pins_to_niscope_sessions_multiple_pins(
        self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions
    ):
        all_pins = self.pin_map_dut_pins + self.pin_map_system_pins
        (
            pin_query_context,
            queried_sessions,
            queried_channel_lists,
        ) = standalone_tsm_context.pins_to_niscope_sessions(all_pins)
        assert isinstance(pin_query_context, PinQueryContext)
        assert isinstance(queried_sessions, tuple)
        assert isinstance(queried_channel_lists, tuple)
        assert len(queried_sessions) == len(queried_channel_lists)
        for queried_session, queried_channel_list in zip(queried_sessions, queried_channel_lists):
            assert isinstance(queried_session, niscope.Session)
            assert isinstance(queried_channel_list, str)
            assert queried_session in simulated_niscope_sessions
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_pinquerycontext.py sha256=15779b8e0f68efa5b6cd2820a755833716510e09a6de92404fe1504070497bb0 bytes=1323 -->
## FILE: tests/test_pinquerycontext.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_pinquerycontext.py`
- sha256: `15779b8e0f68efa5b6cd2820a755833716510e09a6de92404fe1504070497bb0`
- bytes: 1323

````python
from typing import TYPE_CHECKING
import nidigital
import pytest

if TYPE_CHECKING:
    from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    sessions = [
        nidigital.Session(
            instrument_name, options={"Simulate": True, "driver_setup": {"Model": "6570"}}
        )
        for instrument_name in instrument_names
    ]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidigital_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()


@pytest.mark.pin_map("pinquerycontext.pinmap")
class TestPinQueryContext:
    @pytest.mark.usefixtures("simulated_nidigital_sessions")
    def test_get_session_and_channel_index(
        self, standalone_tsm_context: "SemiconductorModuleContext"
    ):
        pin_query_context, _, _ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            ["DUTPin2", "DUTPin1"]
        )
        session_index, channel_index = pin_query_context.get_session_and_channel_index(1, "DUTPin1")
        assert session_index == 1
        assert channel_index == 1
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_publish.py sha256=c8466bed9ea10d8389ed933e30d3a738b702dadbe1e29cc6503c6577f47a8d90 bytes=14600 -->
## FILE: tests/test_publish.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_publish.py`
- sha256: `c8466bed9ea10d8389ed933e30d3a738b702dadbe1e29cc6503c6577f47a8d90`
- bytes: 14600

````python
import random
import pytest
from nitsm.codemoduleapi import SemiconductorModuleContext


@pytest.fixture
def simulated_nidigital_sessions(standalone_tsm_context: SemiconductorModuleContext):
    instrument_names = standalone_tsm_context.get_all_nidigital_instrument_names()
    for instrument_name in instrument_names:
        fake_session = instrument_name
        standalone_tsm_context.set_nidigital_session(instrument_name, fake_session)


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePinScalar:
    _PIN = "SystemPin1"
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self._PIN)
        return pin_query_context

    def test_publish_float_scalar(self, pin_query_context, published_data_reader):
        test_data = random.random()
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == self._NUM_SITES
        for published_data_point in published_data:
            assert published_data_point.double_value == test_data

    def test_publish_bool_scalar(self, pin_query_context, published_data_reader):
        pin_query_context.publish(True)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == self._NUM_SITES
        for published_data_point in published_data:
            assert published_data_point.boolean_value


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin1d:
    _PIN = "DUTPin1"
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(self._PIN)
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [random.random() for _ in range(self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [bool(i % 2) for i in range(self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self._PIN)
        test_data = {1: False, 0: True, 2: True}  # alternate True and False
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, site_number in zip(
            published_data, standalone_tsm_context.site_numbers
        ):
            assert published_data_point.boolean_value == test_data[site_number]


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestSinglePin2d:
    _PIN = "DUTPin3"

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            self._PIN
        )
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [[DigitalPattern1(ch6)], [DigitalPattern2(ch0), DigitalPattern2(ch1)]]
        test_data = [[1150.0], [1952.5, 60417]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [[DigitalPattern1(ch6)], [DigitalPattern2(ch0), DigitalPattern2(ch1)]]
        test_data = [[True], [False, True]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(self._PIN)
        expected_results = [True, False, True]  # test data across sites [0, 1, 2]
        test_data = [{0: True}, {2: True, 1: False}]
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(expected_results)
        for published_data_point, expected_result in zip(published_data, expected_results):
            assert published_data_point.boolean_value == expected_result


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins1d:
    _PINS = ["DUTPin1", "DUTPin2"]
    _NUM_SITES = 3

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_session_for_ppmu(
            self._PINS
        )
        return pin_query_context

    def test_publish_float_1d(self, pin_query_context, published_data_reader):
        test_data = [random.random() for _ in range(len(self._PINS) * self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_1d(self, pin_query_context, published_data_reader):
        test_data = [bool(i % 2) for i in range(len(self._PINS) * self._NUM_SITES)]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, test_data_point in zip(published_data, test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            session,
            site_list,
        ) = standalone_tsm_context.pins_to_nidigital_session_for_pattern(self._PINS)
        test_data = {1: False, 0: True, 2: True}
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(test_data)
        for published_data_point, site_number in zip(
            published_data, standalone_tsm_context.site_numbers
        ):
            assert published_data_point.boolean_value == test_data[site_number]


@pytest.mark.pin_map("publish.pinmap")
@pytest.mark.usefixtures("simulated_nidigital_sessions")
class TestMultiplePins2d:
    _PINS = ["DUTPin2", "DUTPin3"]

    @pytest.fixture
    def pin_query_context(self, standalone_tsm_context):
        pin_query_context, *_ = standalone_tsm_context.pins_to_nidigital_sessions_for_ppmu(
            self._PINS
        )
        return pin_query_context

    def test_publish_float_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch3,ch4,ch5,ch6), DigitalPattern2(ch0,ch1)]
        test_data = [[1150.0, 20.5, 30.5, -1.0], [1952.5, -60417]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.double_value == test_data_point

    def test_publish_bool_2d(self, pin_query_context, published_data_reader):
        # [DigitalPattern1(ch3,ch4,ch5,ch6), DigitalPattern2(ch0,ch1)]
        test_data = [[True, False, True, False], [True, False]]
        pin_query_context.publish(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        flattened_test_data = [data_point for row in test_data for data_point in row]
        assert len(published_data) == len(flattened_test_data)
        for published_data_point, test_data_point in zip(published_data, flattened_test_data):
            assert published_data_point.boolean_value == test_data_point

    def test_publish_pattern(self, standalone_tsm_context, published_data_reader):
        (
            pin_query_context,
            sessions,
            site_lists,
        ) = standalone_tsm_context.pins_to_nidigital_sessions_for_pattern(self._PINS)
        # [DigitalPattern1: site0, site1, site2], [DigitalPattern2: site1, site2]
        test_data = [{1: False, 0: True, 2: True}, {1: True, 2: True}]
        expected_results = [True, False, True]  # test_data AND'd across site
        pin_query_context.publish_pattern_results(test_data)
        published_data = published_data_reader.get_and_clear_published_data()
        assert len(published_data) == len(expected_results)
        for published_data_point, expected_result in zip(published_data, expected_results):
            assert published_data_point.boolean_value == expected_result


@pytest.mark.pin_map("publish.pinmap")
class TestPerSiteMultiSite:
    @pytest.mark.parametrize(
        "test_data", [[1150.0, 1952.5, -4.0], [11500, 19525, -4]], ids=["floats", "ints"]
    )
    def test_publish_per_site_numeric_1d(
        self, standalone_tsm_context, published_data_reader, test_data
    ):
        standalone_tsm_context.publish_per_site(test_data, "id", "DUTPin1")
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point in published_data:
            site_index = standalone_tsm_context.site_numbers.index(published_data_point.site_number)
            assert published_data_point.double_value == test_data[site_index]
            assert published_data_point.published_data_id == "id"
            assert published_data_point.pin == "DUTPin1"

    def test_publish_per_site_bool_1d(self, standalone_tsm_context, published_data_reader):
        test_data = [False, True, False]
        standalone_tsm_context.publish_per_site(test_data, "id", "DUTPin2")
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point in published_data:
            site_index = standalone_tsm_context.site_numbers.index(published_data_point.site_number)
            assert published_data_point.boolean_value == test_data[site_index]
            assert published_data_point.published_data_id == "id"
            assert published_data_point.pin == "DUTPin2"

    def test_publish_per_site_string_1d(self, standalone_tsm_context, published_data_reader):
        test_data = ["holy", "hand", "grenade"]
        standalone_tsm_context.publish_per_site(test_data, "id", "DUTPin3")
        published_data = published_data_reader.get_and_clear_published_data()
        for published_data_point in published_data:
            site_index = standalone_tsm_context.site_numbers.index(published_data_point.site_number)
            assert published_data_point.string_value == test_data[site_index]
            assert published_data_point.published_data_id == "id"
            assert published_data_point.pin == "DUTPin3"


@pytest.mark.pin_map("publish_single_site.pinmap")
class TestPerSiteSingleSite:
    @pytest.mark.parametrize("test_data", [1150.0, 11500], ids=["float", "int"])
    def test_publish_per_site_numeric_scalar(
        self, standalone_tsm_context, published_data_reader, test_data
    ):
        standalone_tsm_context.publish_per_site(test_data, "id", "DUTPin1")
        published_data = published_data_reader.get_and_clear_published_data()[0]
        assert published_data.double_value == test_data
        assert published_data.published_data_id == "id"
        assert published_data.pin == "DUTPin1"

    def test_publish_per_site_bool_scalar(self, standalone_tsm_context, published_data_reader):
        standalone_tsm_context.publish_per_site(True, "id", "DUTPin2")
        published_data = published_data_reader.get_and_clear_published_data()[0]
        assert published_data.boolean_value
        assert published_data.published_data_id == "id"
        assert published_data.pin == "DUTPin2"

    def test_publish_per_site_string_scalar(self, standalone_tsm_context, published_data_reader):
        standalone_tsm_context.publish_per_site("Tis but a scratch.", "id", "DUTPin3")
        published_data = published_data_reader.get_and_clear_published_data()[0]
        assert published_data.string_value == "Tis but a scratch."
        assert published_data.published_data_id == "id"
        assert published_data.pin == "DUTPin3"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_site_and_global_data.py sha256=6afe391ff68655089f99b56c0f37481b339a444450bd03a20f7d40199a2742d7 bytes=1396 -->
## FILE: tests/test_site_and_global_data.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_site_and_global_data.py`
- sha256: `6afe391ff68655089f99b56c0f37481b339a444450bd03a20f7d40199a2742d7`
- bytes: 1396

````python
import pytest


@pytest.mark.pin_map("site_and_global_data.pinmap")
class TestSiteAndGlobalData:
    site_data_id = "site_data_id"
    site_data = ["IES"]
    global_data_id = "global_data_id"
    global_data = "NI"

    @pytest.fixture
    def simulated_site_data(self, standalone_tsm_context):
        standalone_tsm_context.set_site_data(self.site_data_id, self.site_data)

    def test_get_site_data(self, standalone_tsm_context, simulated_site_data):
        queried_data = standalone_tsm_context.get_site_data(self.site_data_id)
        assert isinstance(queried_data, tuple)
        for data in queried_data:
            assert data in self.site_data

    def test_site_data_exists(self, standalone_tsm_context, simulated_site_data):
        assert standalone_tsm_context.site_data_exists(self.site_data_id)

    @pytest.fixture
    def simulated_global_data(self, standalone_tsm_context):
        standalone_tsm_context.set_global_data(self.global_data_id, self.global_data)

    def test_get_global_data(self, standalone_tsm_context, simulated_global_data):
        queried_data = standalone_tsm_context.get_global_data(self.global_data_id)
        assert queried_data == self.global_data

    def test_global_data_exists(self, standalone_tsm_context, simulated_global_data):
        assert standalone_tsm_context.global_data_exists(self.global_data_id)
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tests/test_switch.py sha256=b2e295d3e9723a9f5aa4ad022a95f7604028c54df809af09b3a57e611c284931 bytes=3052 -->
## FILE: tests/test_switch.py

- repository: `ni/nitsm-python`
- source_path: `tests/test_switch.py`
- sha256: `b2e295d3e9723a9f5aa4ad022a95f7604028c54df809af09b3a57e611c284931`
- bytes: 3052

````python
import pytest
import nitsm.codemoduleapi as tsm


@pytest.fixture
def simulated_switch_sessions(standalone_tsm_context):
    switch_names = standalone_tsm_context.get_all_switch_names(
        tsm.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER
    )
    for switch_name in switch_names:
        standalone_tsm_context.set_switch_session(
            switch_name, switch_name, tsm.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER
        )
    yield switch_names


@pytest.mark.pin_map("switch.pinmap")
@pytest.mark.parametrize(
    "multiplexer_type_id",
    ["NIGenericMultiplexer", tsm.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER],
)
class TestSwitch:
    switches = ["Multiplexer1"]

    def test_get_all_switch_names(self, standalone_tsm_context, multiplexer_type_id):
        switch_names = standalone_tsm_context.get_all_switch_names(multiplexer_type_id)
        assert isinstance(switch_names, tuple)
        assert len(switch_names) == len(self.switches)
        for switch_name in switch_names:
            assert isinstance(switch_name, str)
            assert switch_name in self.switches

    def test_set_switch_session(self, standalone_tsm_context, multiplexer_type_id):
        switch_names = standalone_tsm_context.get_all_nidmm_instrument_names()
        for switch_name in switch_names:
            standalone_tsm_context.set_switch_session(switch_name, switch_name, multiplexer_type_id)
            assert tsm.SemiconductorModuleContext._sessions[id(switch_name)] is switch_name

    def test_get_all_switch_sessions(
        self, standalone_tsm_context, simulated_switch_sessions, multiplexer_type_id
    ):
        queried_sessions = standalone_tsm_context.get_all_switch_sessions(multiplexer_type_id)
        assert isinstance(queried_sessions, tuple)
        assert len(queried_sessions) == len(simulated_switch_sessions)
        for queried_session in queried_sessions:
            assert isinstance(queried_session, str)
            assert queried_session in simulated_switch_sessions

    def test_pin_to_switch_sessions(
        self, standalone_tsm_context, simulated_switch_sessions, multiplexer_type_id
    ):
        tsm_contexts, sessions, switch_routes = standalone_tsm_context.pin_to_switch_sessions(
            "DUTPin1", multiplexer_type_id
        )
        assert isinstance(tsm_contexts, tuple)
        assert isinstance(sessions, tuple)
        assert isinstance(switch_routes, tuple)
        assert len(tsm_contexts) == len(sessions)
        assert len(sessions) == len(switch_routes)
        for tsm_context, session, switch_route in zip(tsm_contexts, sessions, switch_routes):
            assert isinstance(tsm_context, tsm.SemiconductorModuleContext)
            assert len(tsm_context.site_numbers) == 1
            assert isinstance(session, str)
            assert session in simulated_switch_sessions
            assert isinstance(switch_route, str)
            assert switch_route == f"DUTPin1Site{tsm_context.site_numbers[0]}"
````

<!--NI_OSS_SOURCE repo=nitsm-python path=tools/makepy_pinmapinterfaces.py sha256=e2d9a85cbab66987eeea7304d32c005f18301a061e8292dc07fd2680fb18ff9c bytes=622 -->
## FILE: tools/makepy_pinmapinterfaces.py

- repository: `ni/nitsm-python`
- source_path: `tools/makepy_pinmapinterfaces.py`
- sha256: `e2d9a85cbab66987eeea7304d32c005f18301a061e8292dc07fd2680fb18ff9c`
- bytes: 622

````python
"""Generates _pinmapinterfaces.py

You must register the correct version of TSM with TestStand Version Selector prior to running this
script.
"""

import sys
import os.path
from win32com.client import makepy

output_file = os.path.join(os.path.dirname(__file__), "_pinmapinterfaces.py")
teststand_public_path = os.environ["TestStandPublic64"]
pmi_type_library = os.path.join(
    teststand_public_path,
    "Bin",
    "NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb",
)

sys.argv = ["makepy", "-o", output_file, pmi_type_library]

if __name__ == "__main__":
    makepy.main()
````
