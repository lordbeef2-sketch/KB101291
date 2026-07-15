# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=.codecov.yml sha256=6996cf75378d317188239996c7a2c0c23ee0fa7ef193705d71f87cf0ee917094 bytes=315 -->
## FILE: .codecov.yml

- repository: `ni/nimi-python`
- source_path: `.codecov.yml`
- sha256: `6996cf75378d317188239996c7a2c0c23ee0fa7ef193705d71f87cf0ee917094`
- bytes: 315

````yaml
coverage:
  precision: 2
  round: down
  range: "70...100"

  status:
    project:
      default:
        # TODO(texasaggie97) - target lowered when adding system test coverage. Raise as coverage rises.
        target: 85%
        threshhold: 5
    patch:
      default:
        target: 70%
        threshhold: 5
````

<!--NI_OSS_SOURCE repo=nimi-python path=.gitattributes sha256=df28aeca06279b9d4ae7260ebd1ec6e422a645614522db62787dc34a09e2e9e8 bytes=741 -->
## FILE: .gitattributes

- repository: `ni/nimi-python`
- source_path: `.gitattributes`
- sha256: `df28aeca06279b9d4ae7260ebd1ec6e422a645614522db62787dc34a09e2e9e8`
- bytes: 741

````text
# Auto detect text files and perform LF normalization
# We explicitly set eol to LF on checkin and checkout
*.py text=set eol=lf
*.rst text=set eol=lf
*.inc text=set eol=lf
*.md text=set eol=lf
*.ini text=set eol=lf
*.txt text=set eol=lf
*.yml text=set eol=lf
VERSION text=set eol=lf
*.mak text=set eol=lf
Makefile text=set eol=lf
License text=set eol=lf
*.rc text=set eol=lf
*.mako text=set eol=lf

# Custom for Visual Studio
*.cs     diff=csharp

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/actions/linux/action.yml sha256=e3ba271c111009e81856b22e0ac4181c896934c54d11dc88518db6138b17e723 bytes=389 -->
## FILE: .github/actions/linux/action.yml

- repository: `ni/nimi-python`
- source_path: `.github/actions/linux/action.yml`
- sha256: `e3ba271c111009e81856b22e0ac4181c896934c54d11dc88518db6138b17e723`
- bytes: 389

````yaml
name: "Run system tests"
description: "Run system tests for the specified module"
inputs:
  module_name:
    description: "module name"
    required: true
    default: ""

runs:
  using: "composite"
  steps:
    - run: |
        source /etc/bashrc
        cd generated
        mkdir junit
        cd ${{ inputs.module_name }}
        python -m tox -c tox-system_tests.ini
      shell: bash
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/actions/run_examples_using_pypi_uploads/action.yml sha256=c9f8c9b28f238956cfcd469a79c6b4d7ba389796b1ac85334923f4adf1148da1 bytes=1304 -->
## FILE: .github/actions/run_examples_using_pypi_uploads/action.yml

- repository: `ni/nimi-python`
- source_path: `.github/actions/run_examples_using_pypi_uploads/action.yml`
- sha256: `c9f8c9b28f238956cfcd469a79c6b4d7ba389796b1ac85334923f4adf1148da1`
- bytes: 1304

````yaml
name: Run examples using PyPI uploads
description: Install module(s) from PyPI and run examples. Intended for release validation.
inputs:
  module_name:
    description: module name (e.g. "nidcpower")
    required: true
    default: ""
  module_version:
    description: module version (e.g. "1.8.1")
    required: true
    default: ""

runs:
  using: composite
  steps:
    # The local wheel installation and single environment would have made using tox-system_tests.ini difficult.
    # To keep things simple, we just use pip and pytest directly for a single Python version.
    - run: py -3.14 -m venv --clear .venv
      shell: powershell
    - run: |
        .venv\Scripts\Activate.ps1
        python -m pip install ${{ inputs.module_name }}==${{ inputs.module_version }} pytest
      shell: powershell
    - if: ${{ inputs.module_name == 'nitclk' }}
      run: |
        .venv\Scripts\Activate.ps1
        python -m pip install niscope==${{ inputs.module_version }}
      shell: powershell
    - if: ${{ inputs.module_name == 'niscope' }}
      run: |
        .venv\Scripts\Activate.ps1
        python -m pip install numpy
      shell: powershell
    - run: |
        .venv\Scripts\Activate.ps1
        cd src/${{ inputs.module_name }}
        python -m pytest ./examples -v
      shell: powershell
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/actions/windows/action.yml sha256=8e216845aee0fe04540b849419373104b3c089384cc8c7c2eae35d6257ea43d4 bytes=376 -->
## FILE: .github/actions/windows/action.yml

- repository: `ni/nimi-python`
- source_path: `.github/actions/windows/action.yml`
- sha256: `8e216845aee0fe04540b849419373104b3c089384cc8c7c2eae35d6257ea43d4`
- bytes: 376

````yaml
name: "Run system tests"
description: "Run system tests for the specified module"
inputs:
  module_name:
    description: "module name"
    required: true
    default: ""

runs:
  using: "composite"
  steps:
    - run: |
        cd generated        
        mkdir junit
        cd ${{ inputs.module_name }}
        python -m tox -c tox-system_tests.ini
      shell: powershell
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/CODEOWNERS sha256=101a90991917a26f58524101c76158705074885e21f0c076b72f9077b6de79bf bytes=41 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nimi-python`
- source_path: `.github/CODEOWNERS`
- sha256: `101a90991917a26f58524101c76158705074885e21f0c076b72f9077b6de79bf`
- bytes: 41

````text
* @marcoskirsch @ni-jfitzger @vnktshr21
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/ISSUE_TEMPLATE/bug-report.md sha256=ad219c0507ee1a44638980ffaa51aa6fc4eba32daf6b7ec6f39df73dd50257be bytes=852 -->
## FILE: .github/ISSUE_TEMPLATE/bug-report.md

- repository: `ni/nimi-python`
- source_path: `.github/ISSUE_TEMPLATE/bug-report.md`
- sha256: `ad219c0507ee1a44638980ffaa51aa6fc4eba32daf6b7ec6f39df73dd50257be`
- bytes: 852

````markdown
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

<!--
When filing an issue, please fill in the requested fields as thoroughly as you can and then delete this comment
Note: For issues, assistance, and questions about using NI products, please visit ni.com/support. Issues opened here should be specifically related to these Python APIs.
-->

### Description of issue

    <Replace with a description of the issue>

### System report

`python -c "import niscope; niscope.print_diagnostic_information()"` output (replace `niscope` with appropriate package name)

    ```
    <Replace with the output of the above command>
    ```

### Steps to reproduce issue

    ``` python
    <Replace with a script that clearly shows the issue, if applicable>
    ```

    1. Step 1
    2. Step 2
    3. etc...
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=076daebc05b5cd47f5fa4040c70f30ce000ad374f740dde8a47aa08f0d79eaf5 bytes=1240 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nimi-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `076daebc05b5cd47f5fa4040c70f30ce000ad374f740dde8a47aa08f0d79eaf5`
- bytes: 1240

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md).

- [ ] I've updated [CHANGELOG.md](https://github.com/ni/nimi-python/blob/master/CHANGELOG.md) if applicable.

TODO: Check the above box with an 'x' if considered if there were any and then documented client facing changes in [CHANGELOG.md](https://github.com/ni/nimi-python/blob/master/CHANGELOG.md). Strike through if this is not a relevant client facing change.

- [ ] I've added tests applicable for this pull request

TODO: Check the above box with an 'x' indicating you have considered and added any applicable system or unit tests. Strike through if you considered and decided additional tests were not warranted.

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### List issues fixed by this Pull Request below, if any.

TODO: List of issues.

* Fix #xxx
* Fix #yyy

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/workflows/check_latest_release.yml sha256=8cc46aad31334cf288f919311b42a338c5d55fec22bcb811e84e29764099adcf bytes=2094 -->
## FILE: .github/workflows/check_latest_release.yml

- repository: `ni/nimi-python`
- source_path: `.github/workflows/check_latest_release.yml`
- sha256: `8cc46aad31334cf288f919311b42a338c5d55fec22bcb811e84e29764099adcf`
- bytes: 2094

````yaml
name: check_latest_release

on:
  release:
    types: [released]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
    inputs:
      release_tag:
        description: The GitHub release tag corresponding to the PyPI releases to test
        required: true
        default: non-existent-tag
  
jobs:
  install-module-and-run-examples:
    name: example_test
    if: github.repository == 'ni/nimi-python'
    # Use win32 nimibot
    # win64 already handles post-commit testing for coverage
    # linux doesn't support all modules
    runs-on:
      - self-hosted
      - windows
      - x64
      - rdss-nimibot-win-10-py32
    timeout-minutes: 30
    steps:
      - name: checkout repository
        uses: actions/checkout@v3

      - name: Extract module name and version from release tag
        id: extract_tag
        shell: python
        run: |
          import os
          import json

          # Extract module name and version from the release tag
          # Assuming the tag format is <module_name>-<version>, e.g., nidigital-1.4.0
          with open(os.getenv("GITHUB_EVENT_PATH"), "r", encoding="utf-8") as event_file:
            event = json.load(event_file)
          if os.getenv("GITHUB_EVENT_NAME") == "workflow_dispatch":
            tag = event["inputs"]["release_tag"]
          else:
            tag = event["release"]["tag_name"]

          assert tag.count("-") == 1, f"Invalid tag format: {tag}. Expected format: <module_name>-<version>"
          module_name, module_version = tag.split("-")
          with open(os.getenv("GITHUB_OUTPUT"), "a", encoding="utf-8") as output_file:
            output_file.write(f"module_name={module_name}\n")
            output_file.write(f"module_version={module_version}\n")
      # NOTE: we don't upload test coverage for this
      - name: run examples using PyPI uploads
        uses: ./.github/actions/run_examples_using_pypi_uploads
        with:
          module_name: ${{ steps.extract_tag.outputs.module_name }}
          module_version: ${{ steps.extract_tag.outputs.module_version }}
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/workflows/github_actions_aws_rhel_python64.yml sha256=ad608ca6dedf2104ac2a6f8691c2c7b25979601decb5cbaa660acb417bc3b0b0 bytes=1344 -->
## FILE: .github/workflows/github_actions_aws_rhel_python64.yml

- repository: `ni/nimi-python`
- source_path: `.github/workflows/github_actions_aws_rhel_python64.yml`
- sha256: `ad608ca6dedf2104ac2a6f8691c2c7b25979601decb5cbaa660acb417bc3b0b0`
- bytes: 1344

````yaml
name: nimibot_rhel_64

on:
  pull_request:
    branches:
      - master
      - releases/*
    paths-ignore:
      - CHANGELOG.md
      - CONTRIBUTING.md
      - .gitattributes
      - LICENSE
      - VERSION
    types:
      - opened
      - synchronize
      - reopened

  # Allows you to run this workflow manually from the Actions tab.
  workflow_dispatch:
jobs:
  do-the-job1:
    name: system_test
    if: github.repository == 'ni/nimi-python'
    runs-on: 
      - self-hosted
      - linux
      - x64
      - rdss-nimibot-rhel-83-py64
    timeout-minutes: 40
    strategy:
      matrix:
        module_name:
          - nidcpower
          - nidmm
          - nifgen
          - nimodinst
          - nirfsg
          - niscope
          - niswitch
          - nitclk
    steps:
      - name: checkout repository
        uses: actions/checkout@v3
      - name: execute system tests
        uses: ./.github/actions/linux
        with:
          module_name: ${{ matrix.module_name }}
      - name: upload coverage
        uses: codecov/codecov-action@v3
        with:
          # See ../PUBLIC_CODECOV_TOKEN_README.md
          token: 4c58f03d-b74c-489a-889a-ab0a77b7809f
          flags: ${{ matrix.module_name }}systemtests
          name: ${{ matrix.module_name }}
          files: ./generated/${{ matrix.module_name }}/coverage.xml
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/workflows/github_actions_aws_windows_python32.yml sha256=045aba5f949ef3035b7a00af8cd748ac434586a3e9b69ac1532ac001e48ade0b bytes=1459 -->
## FILE: .github/workflows/github_actions_aws_windows_python32.yml

- repository: `ni/nimi-python`
- source_path: `.github/workflows/github_actions_aws_windows_python32.yml`
- sha256: `045aba5f949ef3035b7a00af8cd748ac434586a3e9b69ac1532ac001e48ade0b`
- bytes: 1459

````yaml
name: nimibot_win_32

on:
  pull_request:
    branches:
      - master
      - releases/*
    paths-ignore:
      - CHANGELOG.md
      - CONTRIBUTING.md
      - .gitattributes
      - LICENSE
      - VERSION
    types:
      - opened
      - synchronize
      - reopened

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
  
jobs:
  do-the-job1:
      name: system_test
      if: github.repository == 'ni/nimi-python'
      runs-on: 
        - self-hosted
        - windows
        - x64
        - rdss-nimibot-win-10-py32
      timeout-minutes: 80
      strategy:
        matrix:
          module_name:
            - nidigital
            - nitclk
            - nifgen
            - nidcpower
            - nidmm
            - nirfsg
            - niscope
            - nimodinst
            - nise
            - niswitch
      steps:
        - name: checkout repository
          uses: actions/checkout@v3
        - name: execute system tests
          uses: ./.github/actions/windows
          with:
            module_name: ${{ matrix.module_name }}
        - name: upload coverage
          uses: codecov/codecov-action@v3
          with:
            # See ../PUBLIC_CODECOV_TOKEN_README.md
            token: 4c58f03d-b74c-489a-889a-ab0a77b7809f
            flags: ${{ matrix.module_name }}systemtests
            name: ${{ matrix.module_name }}
            files: ./generated/${{ matrix.module_name }}/coverage.xml
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/workflows/github_actions_aws_windows_python64.yml sha256=3205d1ff5179e3b641b130e45f40de44a29cd45ee3bbb19dd123e33b0816880a bytes=1884 -->
## FILE: .github/workflows/github_actions_aws_windows_python64.yml

- repository: `ni/nimi-python`
- source_path: `.github/workflows/github_actions_aws_windows_python64.yml`
- sha256: `3205d1ff5179e3b641b130e45f40de44a29cd45ee3bbb19dd123e33b0816880a`
- bytes: 1884

````yaml
name: nimibot_win_64

on:
  pull_request:
    branches:
      - master
      - releases/*
    paths-ignore:
      - CHANGELOG.md
      - CONTRIBUTING.md
      - .gitattributes
      - LICENSE
      - VERSION
    types:
      - opened
      - synchronize
      - reopened

  # For this action, also trigger on a merge to master, because
  # the coverage badge tracks coverage of master, not PRs.
  # Doing this for windows_python32 and rhel_python64 is unlikely to
  # add any coverage, so don't bother triggering those on pushes to master.
  push:
    branches:
      - master
    paths-ignore:
      - CHANGELOG.md
      - CONTRIBUTING.md
      - .gitattributes
      - LICENSE
      - VERSION

  # Allows you to run this workflow manually from the Actions tab.
  workflow_dispatch:
  
jobs:
  do-the-job1:
      name: system_test
      if: github.repository == 'ni/nimi-python'
      runs-on: 
        - self-hosted
        - windows
        - x64
        - rdss-nimibot-win-10-py64
      timeout-minutes: 80
      strategy:
        matrix:
          module_name:
            - nidigital
            - nitclk
            - nifgen
            - nidcpower
            - nidmm
            - nirfsg
            - niscope
            - nimodinst
            - nise
            - niswitch
      steps:
        - name: checkout repository
          uses: actions/checkout@v3
        - name: execute system tests
          uses: ./.github/actions/windows
          with:
            module_name: ${{ matrix.module_name }}
        - name: upload coverage
          uses: codecov/codecov-action@v3
          with:
            # See ../PUBLIC_CODECOV_TOKEN_README.md
            token: 4c58f03d-b74c-489a-889a-ab0a77b7809f
            flags: ${{ matrix.module_name }}systemtests
            name: ${{ matrix.module_name }}
            files: ./generated/${{ matrix.module_name }}/coverage.xml
````

<!--NI_OSS_SOURCE repo=nimi-python path=.github/workflows/PUBLIC_CODECOV_TOKEN_README.md sha256=b6868045f3f27033a9dfd8c92315dd36d2e78a496587f06685b5833a2648f5c1 bytes=1331 -->
## FILE: .github/workflows/PUBLIC_CODECOV_TOKEN_README.md

- repository: `ni/nimi-python`
- source_path: `.github/workflows/PUBLIC_CODECOV_TOKEN_README.md`
- sha256: `b6868045f3f27033a9dfd8c92315dd36d2e78a496587f06685b5833a2648f5c1`
- bytes: 1331

````markdown
# WHY DO WE NEED THIS TOKEN WHEN THE ACTION DOCUMENTATION CLAIMS NO TOKEN IS NEEDED FOR PUBLIC REPOSITORIES?
See ISSUE #2013: codecov-action does not reliably upload system-test coverage to codecov
According to community discussion, failed uploads often occur due to "Codecov’s inability to check the validity
of a coverage upload when using tokenless uploads. The underlying issue is rate-limiting from GitHub."

There are 2 possible fixes:
1. Pass the token, when uploading
2. Implement a retry on upload failure (we do this for travis-ci)

# OKAY, BUT WHY AREN'T WE STORING THIS TOKEN IN A SECRET?
According to GitHub: "With the exception of GITHUB_TOKEN, secrets are not passed to the runner when a workflow is triggered from a forked repository."
We require contributors to fork this repository, so that rules out secrets.

# WHAT ARE THE SECURITY RAMIFICATIONS OF MAKING THIS TOKEN PUBLICLY VISIBLE?
From the community discussion:
"The scope of the Codecov token is only to confirm that the coverage uploaded comes from a specific repository,
not to pull down source code or make any code changes."
"A malicious actor would be able to upload incorrect or misleading coverage reports to a specific repository if
they have access to your upload token, but would not be able to pull down source code or make any code changes."
````

<!--NI_OSS_SOURCE repo=nimi-python path=.gitignore sha256=0ce2ff65c9e1e76649f4b4b90985a8609d249f089cc3ccbbb09cccd0df2cdae6 bytes=1164 -->
## FILE: .gitignore

- repository: `ni/nimi-python`
- source_path: `.gitignore`
- sha256: `0ce2ff65c9e1e76649f4b4b90985a8609d249f089cc3ccbbb09cccd0df2cdae6`
- bytes: 1164

````text
*.pyc
.cache
.com.apple.timemachine.supported

# The "generated" folder is created during a build.
# Normally you wouldn't want build artifacts to be in source control.
# But we actually do keep the latest copy of some of the generated code, specifically the Python modules, for two reasons:
#   1. So that we can make changes to the generator and easily review what effect those changes have in the generated code.
#   2. So that our system tests can create a wheel out of the files and quickly install them, instead of going through the full code-generation process.
# These are the generated files we do NOT want in git
generated/docs/
generated/examples/
generated/htmlcov/
generated/processed_metadata/
generated/*/build/
generated/*/dist/
generated/*/log/
generated/*/*.egg-info/
generated/driver_file_built
generated/printed_global_files
generated/junit/
generated/*/coverage.xml

.eggs/
.tox/
.venv/
.coverage
nidcpowerunittest.xml
nidigitalunittest.xml
nifakeunittest.xml
nimodinstunittest.xml
niscopeunittest.xml
nitclkunittest.xml
codegen.xml
commands.log
.vscode/launch.json
.vscode/settings.json

.pytest_cache/
````

<!--NI_OSS_SOURCE repo=nimi-python path=.gitmodules sha256=bc64a236366fe63e09e578e7b969ac257e587513dcd45b994882dd37cc4dbee3 bytes=106 -->
## FILE: .gitmodules

- repository: `ni/nimi-python`
- source_path: `.gitmodules`
- sha256: `bc64a236366fe63e09e578e7b969ac257e587513dcd45b994882dd37cc4dbee3`
- bytes: 106

````text
[submodule "third_party/ni-apis"]
	path = third_party/ni-apis
	url = https://github.com/ni/ni-apis.git
````

<!--NI_OSS_SOURCE repo=nimi-python path=.travis.yml sha256=4abad60786cac4b876b18fc38d7703a9cf043371275ce07ee9deb12d64ec944e bytes=2562 -->
## FILE: .travis.yml

- repository: `ni/nimi-python`
- source_path: `.travis.yml`
- sha256: `4abad60786cac4b876b18fc38d7703a9cf043371275ce07ee9deb12d64ec944e`
- bytes: 2562

````yaml
group: travis_latest
language: python
dist: focal
git:
  submodules: false
matrix:
    include:
      # Historically, we've run tests on the latest supported version of Python first.
      # For now, we're running Python 3.12 first, because it's the version currently used for codegen.
      # This is where additional tests are run so we give it more time.
      # When the version used for codegen changes, the version that runs first should change to match.
      - python: "3.12"
      - python: "3.10"
      - python: "3.11"
      - python: "3.13"
      - python: "3.14"

install:
  - git submodule update --init --recursive --progress
  - travis_retry sudo apt-get -y install python3-pip
  - travis_retry pip install --upgrade pip
  # tox 4.0 broke plugin compatibility
  # TODO(ni-jfitzger): When tox-travis has a release compatible with tox>=4.0, remove the tox version specifier (Tracked on GitHub by #1876)
  - travis_retry pip install --upgrade tox==3.* tox-travis

before_script:
  # Python 3.13 is only supported by grpcio-tools >= 1.67.0, a later version than what we use in the tox.ini
  # Python 3.14 is only supported by grpcio-tools >= 1.75.1, a later version than what we use in the tox.ini
  - if [[ "$TRAVIS_PYTHON_VERSION" != "3.13" && "$TRAVIS_PYTHON_VERSION" != "3.14" ]]; then python tools/ensure_codegen_up_to_date.py; fi

script:
  - tox -c tox-travis.ini

after_success:
  # Install and verify codecov tool
  - travis_retry curl https://keybase.io/codecovsecurity/pgp_keys.asc | gpg --no-default-keyring --keyring trustedkeys.gpg --import
  - travis_retry curl -Os https://uploader.codecov.io/latest/linux/codecov  # download codecov tool
  - travis_retry curl -Os https://uploader.codecov.io/latest/linux/codecov.SHA256SUM
  - travis_retry curl -Os https://uploader.codecov.io/latest/linux/codecov.SHA256SUM.sig
  - travis_retry gpgv codecov.SHA256SUM.sig codecov.SHA256SUM
  - travis_retry shasum -a 256 -c codecov.SHA256SUM
  - travis_retry chmod +x codecov
  # upload coverage
  - travis_retry ./codecov --flags codegenunittests --file codegen.xml
  - travis_retry ./codecov --flags nifakeunittests --file nifakeunittest.xml
  - travis_retry ./codecov --flags nidcpowerunittests --file nidcpowerunittest.xml
  - travis_retry ./codecov --flags nidigitalunittests --file nidigitalunittest.xml
  - travis_retry ./codecov --flags nimodinstunittests --file nimodinstunittest.xml
  - travis_retry ./codecov --flags niscopeunittests --file niscopeunittest.xml
  - travis_retry ./codecov --flags nitclkunittests --file nitclkunittest.xml
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/__init__.py sha256=01a43c20fbeed865fef98ca1b34f01aa99dc198f7a7dcc79fd983d6d7b399b9f bytes=454 -->
## FILE: build/__init__.py

- repository: `ni/nimi-python`
- source_path: `build/__init__.py`
- sha256: `01a43c20fbeed865fef98ca1b34f01aa99dc198f7a7dcc79fd983d6d7b399b9f`
- bytes: 454

````python
from contextlib import contextmanager
import os

pathname = os.path.dirname(os.path.realpath(__file__))


@contextmanager
def add_to_path(p):
    import sys
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path


with add_to_path(pathname):
    from generate_template import generate_template  # noqa: F401

    from utilities import configure_logging  # noqa: F401
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/__main__.py sha256=791636eec1595a32f79ada82fbc1e6774894b01639f91e86a62313ed45d2d575 bytes=2881 -->
## FILE: build/__main__.py

- repository: `ni/nimi-python`
- source_path: `build/__main__.py`
- sha256: `791636eec1595a32f79ada82fbc1e6774894b01639f91e86a62313ed45d2d575`
- bytes: 2881

````python
#!/usr/bin/python3

import argparse
import logging
import os
import pprint
import sys

# Part of this package
import generate_template
import utilities

pp = pprint.PrettyPrinter(indent=4)

# Setup the required arguments for this script
usage = "Codegen driver files"

parser = argparse.ArgumentParser(description=usage, prog='build')
verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
verbosity_group.add_argument(
    "-v", "--verbose",
    action="count", dest="verbose", default=0,
    help="Verbose output")
verbosity_group.add_argument(
    "--test",
    action="store_true", dest="test", default=False,
    help="Run doctests and quit")
verbosity_group.add_argument(
    "--log-file",
    action="store", dest="logfile", default=None,
    help="Send logging to listed file instead of stdout")
build_group = parser.add_argument_group("Build")
build_group.add_argument(
    "--metadata",
    action='append', dest='metadata', default=[],
    help='Absolute or relative path to metadata package. Multiple allowed. Will build in order added to command line.')
build_group.add_argument(
    "--include-grpc-support",
    action='store_true', dest='include_grpc_support', default=[],
    help='Include gRPC support in the generated files.')
utility_group = parser.add_argument_group("Utility")
utility_group.add_argument(
    "--template",
    action="store", dest="template", default=None, required=True,
    help="Mako template to use. Can only be used if no actions.")
utility_group.add_argument(
    "--dest-dir",
    action="store", dest="dest_dir", default=None, required=False,
    help="Output folder.")
utility_group.add_argument(
    "--dest-file",
    action="store", dest="dest_file", default=None, required=False,
    help="Output file name. Optional. If not set, file will be named based on mako template name.")
args = parser.parse_args()

if args.verbose > 1:
    utilities.configure_logging(logging.DEBUG, args.logfile)
elif args.verbose == 1:
    utilities.configure_logging(logging.INFO, args.logfile)
else:
    utilities.configure_logging(logging.WARNING, args.logfile)

logging.info(pp.pformat(args))

for m in args.metadata:
    if not os.path.isabs(m):
        m = os.path.normpath(os.path.join(os.getcwd(), m))
    metadata = utilities.load_build(m)

    if args.dest_dir is None:
        logging.error('--dest-dir is required when using --template')
        sys.exit(1)

    template_params = {}
    template_params['metadata'] = metadata
    template_params['include_grpc_support'] = args.include_grpc_support

    logging.debug(pp.pformat(template_params))

    file_name = args.dest_file
    if file_name is None:
        file_name = os.path.basename(args.template).replace('.mako', '')
    dest_file = os.path.join(args.dest_dir, file_name)
    generate_template.generate_template(args.template, template_params, dest_file)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/defines.mak sha256=dc5c11e827468cf7ada05e98672363dd6adf03ec24a6b55dea4cab999d1f0e97 bytes=2603 -->
## FILE: build/defines.mak

- repository: `ni/nimi-python`
- source_path: `build/defines.mak`
- sha256: `dc5c11e827468cf7ada05e98672363dd6adf03ec24a6b55dea4cab999d1f0e97`
- bytes: 2603

````makefile
OUTPUT_DIR := $(GENERATED_DIR)/$(DRIVER)
LOG_DIR := $(OUTPUT_DIR)/log
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/unit_tests
TEMPLATE_DIR := $(BUILD_HELPER_DIR)/templates
TOX_INI := $(OUTPUT_DIR)/tox.ini

DRIVER_DIR := $(ROOT_DIR)/src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata
METADATA_FILES := $(wildcard $(METADATA_DIR)/*.py)
SHARED_PROTOS_DIR := $(ROOT_DIR)/src/shared_protos
NI_APIS_PROTOS_DIR := $(ROOT_DIR)/third_party/ni-apis/ni/grpcdevice/v1
PROTO_DIRS := $(METADATA_DIR) $(SHARED_PROTOS_DIR) $(NI_APIS_PROTOS_DIR)
PROTO_FILE ?= $(METADATA_DIR)/$(DRIVER).proto

BUILD_HELPER_SCRIPTS := $(wildcard $(BUILD_HELPER_DIR)/*.py $(BUILD_HELPER_DIR)/helper/*.py)

DRIVER_DOCS_DIR := $(DOCS_DIR)/$(DRIVER)

MKDIRECTORIES += \
    $(DRIVER_DOCS_DIR) \
    $(OUTPUT_DIR) \
    $(MODULE_DIR) \
    $(UNIT_TEST_DIR) \
    $(LOG_DIR) \

VPATH = $(TEMPLATE_DIR)

true := T
false :=
GRPC_SUPPORTED := $(if $(wildcard $(PROTO_FILE)),$(true))

PYTHON_CMD ?= python
GRPC_SUPPORT_PARAM := $(if $(GRPC_SUPPORTED),--include-grpc-support)
define GENERATE_SCRIPT
$(PYTHON_CMD) -m build --template $1 --dest-dir $2 --metadata $3 $(if $4,--dest-file $4) $(if $(PRINT),-v,) $(GRPC_SUPPORT_PARAM)
endef

ifeq (,$(PRINT))
_hide_cmds := @
LOG_OUTPUT := >
else
LOG_OUTPUT := | tee
endif

TARGETS := $(filter-out run_unit_tests,$(DEFAULT_TARGETS))

.PHONY:
all: $(TARGETS)

DEFAULT_PY_FILES_TO_GENERATE := \
    _attributes.py \
    enums.py \
    _library.py \
    _library_interpreter.py \
    _library_singleton.py \
    session.py \
    errors.py \
    unit_tests/_mock_helper.py \
    unit_tests/_matchers.py \
    __init__.py \
    _converters.py \
    VERSION \
    $(if $(GRPC_SUPPORTED), \
        _grpc_stub_interpreter.py \
        grpc_session_options.py \
        $(basename $(notdir $(PROTO_FILE)))_pb2.py \
        $(basename $(notdir $(PROTO_FILE)))_pb2_grpc.py \
        nidevice_pb2.py \
        nidevice_pb2_grpc.py \
    ) \

DEFAULT_PY_FILES_TO_COPY := \
    _visatype.py \

DEFAULT_RST_FILES_TO_GENERATE := \
    about_$(DRIVER).inc \
    index.rst \
    $(DRIVER).rst \
    enums.rst \
    examples.rst \
    installation.inc \
    status.inc \
    class.rst \
    toc.inc \
    errors.rst \
    rep_caps.rst \
    $(if $(GRPC_SUPPORTED), \
        grpc_session_options.rst \
    ) \

DEFAULT_SPHINX_CONF_PY := $(DRIVER_DOCS_DIR)/conf.py
DEFAULT_READTHEDOCS_CONFIG := $(DRIVER_DOCS_DIR)/.readthedocs.yaml

# Files for tracking parts of the build
SDIST_WHEEL_BUILD_DONE := $(LOG_DIR)/sdist_wheel_build_done
GENERATED_FILES_COPY_DONE := $(LOG_DIR)/generated_files_copy_done
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/generate_template.py sha256=149a3a0fb407c55f04f09c4b73255c897b976ce190cc118164488760e45329e9 bytes=2154 -->
## FILE: build/generate_template.py

- repository: `ni/nimi-python`
- source_path: `build/generate_template.py`
- sha256: `149a3a0fb407c55f04f09c4b73255c897b976ce190cc118164488760e45329e9`
- bytes: 2154

````python
#!/usr/bin/python3

import logging
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.template import Template
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


def generate_template(template_name, template_params, dest_file, in_zip_file=False):
    try:
        template_params['encoding_tag'] = '# -*- coding: utf-8 -*-'
        module_name = template_params['metadata'].config['module_name']
        lookup = TemplateLookup(directories=[f'src/{module_name}/templates', 'build/templates'])
        template = Template(filename=template_name, lookup=lookup)
        rendered_template = template.render(template_parameters=template_params)

    except Exception:
        # Because mako expands into python, we catch all errors, not just MakoException.
        # Ideally, we'd use text_error_template, but it sucks.  html_error_template,
        # however, is useful.  Unfortunately emitting html isn't acceptable.  So we
        # re-implement using mako.exceptions.RichTraceback here.
        tback = RichTraceback(traceback=None)
        line = tback.lineno
        lines = tback.source.split('\n')

        # The underlying error.
        logging.error("\n{}: {}\n".format(str(tback.error.__class__.__name__), str(tback.error)))
        logging.error("Offending Template: %s\n" % template_name)

        # Show a source listing of the template, with offending line marked.
        for index in range(max(0, line - 4), min(len(lines), line + 5)):
            if index + 1 == line:
                logging.error(">> %#08d: %s" % (index + 1, lines[index]))
            else:
                logging.error("   %08d: %s" % (index + 1, lines[index]))

        logging.error("\nTraceback (most recent call last):")
        for (filename, lineno, function, line) in tback.reverse_traceback:
            logging.error("   File %s, line %d, in %s\n     %s" % (filename, lineno, function, line))

        logging.error("\n")
        sys.exit(1)

    logging.debug(rendered_template)
    with open(dest_file, 'wb') as file_handle_public:
        file_handle_public.write(bytes(rendered_template, "UTF-8"))
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/__init__.py sha256=a65fb984a8ad59408ff4b67a5028c97fe85c3066508dfc27eaf48ea5c9abb2a2 bytes=4301 -->
## FILE: build/helper/__init__.py

- repository: `ni/nimi-python`
- source_path: `build/helper/__init__.py`
- sha256: `a65fb984a8ad59408ff4b67a5028c97fe85c3066508dfc27eaf48ea5c9abb2a2`
- bytes: 4301

````python
from build.helper.codegen_helper import get_ctype_variable_declaration_snippet  # noqa: F401
from build.helper.codegen_helper import get_dictionary_snippet  # noqa: F401
from build.helper.codegen_helper import get_enum_type_check_snippet  # noqa: F401
from build.helper.codegen_helper import get_enum_value_snippet  # noqa: F401
from build.helper.codegen_helper import get_grpc_interpreter_method_return_snippet  # noqa: F401
from build.helper.codegen_helper import get_library_interpreter_method_return_snippet  # noqa: F401
from build.helper.codegen_helper import get_parameter_size_check_snippets  # noqa: F401
from build.helper.codegen_helper import get_params_snippet  # noqa: F401
from build.helper.codegen_helper import get_session_method_return_snippet  # noqa: F401
from build.helper.codegen_helper import IviDanceStep  # noqa: F401

from build.helper.parameter_usage_options import ParameterUsageOptions  # noqa: F401

from build.helper.documentation_helper import add_attribute_rep_cap_tip  # noqa: F401
from build.helper.documentation_helper import add_notes_re_links  # noqa: F401
from build.helper.documentation_helper import as_rest_table  # noqa: F401
from build.helper.documentation_helper import find_attribute_by_name  # noqa: F401
from build.helper.documentation_helper import find_enum_by_value  # noqa: F401
from build.helper.documentation_helper import format_type_for_rst_documentation  # noqa: F401
from build.helper.documentation_helper import get_attribute_repeated_caps  # noqa: F401
from build.helper.documentation_helper import get_documentation_for_node_docstring  # noqa: F401
from build.helper.documentation_helper import get_documentation_for_node_rst  # noqa: F401
from build.helper.documentation_helper import get_function_docstring  # noqa: F401
from build.helper.documentation_helper import get_function_rst  # noqa: F401
from build.helper.documentation_helper import get_indented_docstring_snippet  # noqa: F401
from build.helper.documentation_helper import get_rst_header_snippet  # noqa: F401
from build.helper.documentation_helper import get_rst_picture_reference  # noqa: F401
from build.helper.documentation_helper import module_supports_repeated_caps  # noqa: F401
from build.helper.documentation_helper import rep_cap_method_desc  # noqa: F401
from build.helper.documentation_helper import square_up_tables  # noqa: F401

from build.helper.documentation_snippets import close_function_def_for_doc  # noqa: F401
from build.helper.documentation_snippets import initiate_function_def_for_doc  # noqa: F401

from build.helper.helper import camelcase_to_snakecase  # noqa: F401
from build.helper.helper import enum_uses_converter  # noqa: F401
from build.helper.helper import get_array_type_for_api_type  # noqa: F401
from build.helper.helper import get_development_status  # noqa: F401
from build.helper.helper import get_numpy_type_for_api_type  # noqa: F401
from build.helper.helper import get_python_type_for_api_type  # noqa: F401
from build.helper.helper import sorted_attrs  # noqa: F401

from build.helper.metadata_add_all import add_all_metadata  # noqa: F401

from build.helper.metadata_filters import are_complex_parameters_used  # noqa: F401
from build.helper.metadata_filters import filter_codegen_attributes  # noqa: F401
from build.helper.metadata_filters import filter_codegen_attributes_public_only  # noqa: F401
from build.helper.metadata_filters import filter_codegen_enums  # noqa: F401
from build.helper.metadata_filters import filter_codegen_functions  # noqa: F401
from build.helper.metadata_filters import filter_ivi_dance_parameters  # noqa: F401
from build.helper.metadata_filters import filter_len_parameters  # noqa: F401
from build.helper.metadata_filters import filter_library_functions  # noqa: F401
from build.helper.metadata_filters import filter_parameters  # noqa: F401
from build.helper.metadata_filters import filter_public_functions  # noqa: F401

from build.helper.metadata_find import find_custom_type  # noqa: F401
from build.helper.metadata_find import find_session_handle_parameter  # noqa: F401
from build.helper.metadata_find import find_size_parameter  # noqa: F401

from build.helper.metadata_merge_dicts import merge_dicts  # noqa: F401
from build.helper.metadata_merge_dicts import merge_helper  # noqa: F401
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/codegen_helper.py sha256=ec680acd66ef42399a5c3c0b805bb0ae8eb17ad6924e5734eb9b378b5c420bfa bytes=35745 -->
## FILE: build/helper/codegen_helper.py

- repository: `ni/nimi-python`
- source_path: `build/helper/codegen_helper.py`
- sha256: `ec680acd66ef42399a5c3c0b805bb0ae8eb17ad6924e5734eb9b378b5c420bfa`
- bytes: 35745

````python
import builtins

from .helper import get_array_type_for_api_type
from .metadata_filters import filter_parameters
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions
from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=4, width=200)

_ParameterUsageOptionsSnippet = {
    ParameterUsageOptions.SESSION_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.SESSION_INIT_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'interpreter_method_call_snippet',
    },
    ParameterUsageOptions.SESSION_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.SESSION_INIT_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name_or_default_for_init',
    },
    ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD: {
        'skip_self': True,
        'name_to_use': 'python_name_with_doc_default',
    },
    ParameterUsageOptions.LIBRARY_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.LIBRARY_METHOD_CALL: {
        'skip_self': True,
        # when calling into Library, we need to build and pass parameters as ctypes types
        'name_to_use': 'ctypes_method_call_snippet',
    },
    ParameterUsageOptions.CDLL_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.INTERPRETER_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'interpreter_method_call_snippet',
    },
    ParameterUsageOptions.CTYPES_ARGTYPES: {
        'skip_self': True,
        'name_to_use': 'ctypes_type_library_call',
    },
    ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.GRPC_REQUEST_PARAMETERS: {
        'skip_self': True,
        'name_to_use': 'grpc_request_snippet',
    },
}
# Only used for filtering
#   ParameterUsageOptions.INPUT_PARAMETERS
#   ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS
#   ParameterUsageOptions.API_OUTPUT_PARAMETERS
#   ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS
#   ParameterUsageOptions.IVI_DANCE_PARAMETER
#   ParameterUsageOptions.LEN_PARAMETER
#   ParameterUsageOptions.INPUT_ENUM_PARAMETERS
#   ParameterUsageOptions.GRPC_OUTPUT_PARAMETERS


# Functions that return snippets that can be placed directly in the templates.
def get_params_snippet(function, parameter_usage_options):
    '''get_params_snippet

    Get a parameter list snippet based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _ParameterUsageOptionsSnippet[parameter_usage_options]

    parameters_to_use = filter_parameters(function['parameters'], parameter_usage_options)

    snippets = []
    if not options_to_use['skip_self']:
        snippets.append('self')

    # Render based on options
    for p in parameters_to_use:
        snippets.append(p[options_to_use['name_to_use']])
    return ', '.join(snippets)


def _get_interpreter_output_param_return_type(output_parameter, config):
    assert output_parameter['direction'] == 'out', 'Expected parameter {} (a.k.a. {}) to have direction out'.format(output_parameter['name'], output_parameter['python_name'])

    custom_type = find_custom_type(output_parameter, config)
    is_custom_type = custom_type is not None

    module_name = custom_type['file_name'] + '.' if is_custom_type else ''

    if output_parameter['enum'] is not None:
        return 'enums.' + output_parameter['enum'], is_custom_type
    else:
        return module_name + output_parameter['python_type'], is_custom_type


def _get_library_interpreter_output_param_return_snippet(output_parameter, parameters, config):
    '''Returns the snippet for returning a single output parameter from a LibraryInterpreter method, i.e. "reading_ctype.value"'''
    return_type, is_custom_type = _get_interpreter_output_param_return_type(output_parameter, config)
    # Custom types (i.e. inherit from ctypes.Structure) don't need a .value
    val_suffix = '' if is_custom_type else '.value'

    if output_parameter['use_array']:
        snippet = '{}_array'.format(output_parameter['python_name'])
    elif output_parameter['is_buffer']:
        if output_parameter['size']['mechanism'] == 'fixed':
            size = str(output_parameter['size']['value'])
        elif output_parameter['size']['mechanism'] == 'python-code':
            size = output_parameter['size']['value']
        else:
            size_parameter = find_size_parameter(output_parameter, parameters)
            size = size_parameter['ctypes_variable_name'] + '.value'

        snippet = '[' + return_type + '(' + output_parameter['ctypes_variable_name'] + '[i]) for i in range(' + size + ')]'
    else:
        if output_parameter['is_string']:
            # '_encoding' is a variable on the LibraryInterpreter object
            snippet = output_parameter['ctypes_variable_name'] + '.value.decode(self._encoding)'
        else:
            snippet = return_type + '(' + output_parameter['ctypes_variable_name'] + val_suffix + ')'

    return snippet


def _get_grpc_interpreter_output_param_return_snippet(output_parameter, parameters, config):
    param_accessor = 'response.' + output_parameter['grpc_name']

    return_type, is_custom_type = _get_interpreter_output_param_return_type(output_parameter, config)
    if hasattr(builtins, return_type):
        return_type = None

    convert_array_elements = output_parameter['is_buffer'] and return_type is not None
    if output_parameter.get('python_api_converter_name') == 'convert_to_bytes':
        # Don't convert individual array elements; convert_to_bytes will handle it
        convert_array_elements = False

    if convert_array_elements:
        return '[' + return_type + '(x) for x in ' + param_accessor + ']'
    elif return_type is not None:
        return return_type + '(' + param_accessor + ')'
    else:
        return param_accessor


def _get_session_output_param_return_snippet(output_parameter, parameters, config):
    '''Returns the snippet for returning a single output parameter from a Session method'''
    snippet = output_parameter['python_name']

    # Handle output converter
    if 'python_api_converter_name' in output_parameter:
        snippet = '_converters.' + output_parameter['python_api_converter_name'] + '(' + snippet + ')'

    return snippet


def get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=False):
    '''Returns a string suitable to use as the return argument of a LibraryInterpreter method, i.e. "return reading_ctype.value"'''
    options = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS if use_numpy_array else ParameterUsageOptions.API_OUTPUT_PARAMETERS
    parameters_to_use = filter_parameters(parameters, options)
    snippets = [_get_library_interpreter_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_grpc_interpreter_method_return_snippet(parameters, config):
    '''Returns a string suitable to use as the return argument of a _gprc.LibraryInterpreter method'''
    parameters_to_use = filter_parameters(parameters, ParameterUsageOptions.API_OUTPUT_PARAMETERS)
    snippets = [_get_grpc_interpreter_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_session_method_return_snippet(parameters, config, use_numpy_array=False):
    '''Returns a string suitable to use as the return argument of a Session method'''
    options = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS if use_numpy_array else ParameterUsageOptions.API_OUTPUT_PARAMETERS
    parameters_to_use = filter_parameters(parameters, options)
    snippets = [_get_session_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_enum_type_check_snippet(parameter, indent):
    '''Returns python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None, pp.pformat(parameter)
    assert parameter['direction'] == 'in', pp.pformat(parameter)
    enum_check = 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ':\n'
    enum_check += (' ' * indent) + 'raise TypeError(\'Parameter {} must be of type \' + str({}))'.format(parameter['python_name'], parameter['python_type'])
    return enum_check


def _get_buffer_parameters_for_size_parameter(parameter, parameters):
    '''Return all parameters that use this parameter for size. Empty list if none'''
    buffer_params = []
    for p in parameters:
        if (p['is_buffer'] or p['is_string']) and p['size']['value'] == parameter['name']:
            buffer_params.append(p)
        elif (p['is_buffer'] or p['is_string']) and 'value_twist' in p['size'] and p['size']['value_twist'] == parameter['name']:
            buffer_params.append(p)
    return buffer_params


class IviDanceStep(Enum):
    NOT_APPLICABLE = 0
    'Use this when the function in question does not do the IVI dance.'

    QUERY_SIZE = 1
    'Step 1: Call into the driver in order to query the size of the buffer to be allocated.'

    GET_DATA = 2
    'Step 2: Allocate the buffer, call back into the driver to get the actual data.'


def get_ctype_variable_declaration_snippet(parameter, parameters, ivi_dance_step, config, use_numpy_array=False):
    '''Returns array of python snippets that declares and initializes a ctypes variable for the parameter that can be passed to the Library.

    Logic for creating the appropriate snippet is split up in two helper functions. One for scalars and one for buffers.
    '''

    custom_type = find_custom_type(parameter, config)

    # Determine the module.
    if custom_type is not None:
        # Module is the file associated with that type.
        module_name = custom_type['file_name']
    elif parameter['numpy'] is True and use_numpy_array is True:
        assert parameter['is_buffer'] is True
        module_name = 'numpy'
    else:
        module_name = '_visatype'

    # Use _complextype.py file for complex parameter
    if parameter.get('complex_array_representation') is not None:
        module_name = '_complextype'

    if parameter['is_string'] is True:
        definitions = _get_ctype_variable_definition_snippet_for_string(parameter, parameters, ivi_dance_step, module_name)
    elif parameter['is_buffer'] is True:
        definitions = _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name)
    else:
        definitions = _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name, config)

    return definitions


def _get_ctype_variable_definition_snippet_for_string(parameter, parameters, ivi_dance_step, module_name):
    '''These are the different cases for initializing the ctype variables for strings

    C010. Input repeated capability:                                           ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
    C020. Input string:                                                        ctypes.create_string_buffer(parameter_name.encode(self._encoding))
    C030. Input string enum:                                                   ctypes.create_string_buffer(parameter_name.value.encode(self._encoding))
    C050. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
    C060. Output buffer with mechanism ivi-dance, GET_DATA:                    (visatype.ViChar * buffer_size_ctype.value)()
    C070. Output buffer with mechanism fixed-size:                             visatype.ViChar * 256
    C080. Output buffer with mechanism python-code:                            visatype.ViChar * <python_code>
    C090. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
    C100. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       (visatype.ViChar * buffer_size_ctype.value)()
    '''
    definitions = []
    definition = None

    if parameter['direction'] == 'in':
        if parameter['is_repeated_capability'] is True:
            definition = 'ctypes.create_string_buffer({}.encode(self._encoding))  # case C010'.format(parameter['python_name'])
        elif parameter['enum'] is not None:
            definition = 'ctypes.create_string_buffer({}.value.encode(self._encoding))  # case C030'.format(parameter['python_name'])
        else:
            definition = 'ctypes.create_string_buffer({}.encode(self._encoding))  # case C020'.format(parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        if parameter['size']['mechanism'] == 'ivi-dance':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case C050'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters)
                definition = '({}.ViChar * {}.value)()  # case C060'.format(module_name, size_parameter['ctypes_variable_name'])
            else:
                assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])

        elif parameter['size']['mechanism'] == 'ivi-dance-with-a-twist':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case C090'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters, key='value_twist')
                definition = '({}.ViChar * {}.value)()  # case C100'.format(module_name, size_parameter['ctypes_variable_name'])
            else:
                assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])

        elif parameter['size']['mechanism'] == 'fixed':
            assert parameter['size']['value'] != 1, "Parameter {} has 'direction':'out' and 'size':{}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            definition = '({}.ViChar * {})()  # case C070'.format(module_name, parameter['size']['value'])

        elif parameter['size']['mechanism'] == 'python-code':
            assert parameter['size']['value'] != 1, "Parameter {} has 'direction':'out' and 'size':{}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            definition = '({}.ViChar * {})()  # case C080'.format(module_name, parameter['size']['value'])

        else:
            assert False, "Invalid mechanism for parameters with 'direction':'out': " + str(parameter)

    if definition is not None:
        definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)

    return definitions


def _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name, config):
    '''These are the different cases for initializing the ctype variable for scalars:

        S110. Input session handle:                                                visatype.ViSession(self._vi)
        S120. Input is size of buffer with mechanism is python-code:               visatype.ViInt32(<custom python code>)
        S130. Input enum:                                                          visatype.ViInt32(parameter_name.value)
        S150. Input scalar:                                                        visatype.ViInt32(parameter_name)
        S160. Input is size of 1-dimensional input buffer:                         visatype.ViInt32(0 if list is None else len(list))
        S161. Input is total number of elements in multidimensional input buffer:  visatype.ViInt32(0 if array is None else array.size)
        S170. Input is size of output buffer with mechanism ivi-dance, QUERY_SIZE: visatype.ViInt32()
        S180. Input is size of output buffer with mechanism ivi-dance, GET_DATA:   visatype.ViInt32(error_code)
        S190. Input is size of output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE: visatype.ViInt32()
        S200. Input is size of output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:   visatype.ViInt32(error_code)
        S210. Input is size of output buffer with mechanism passed-in:             visatype.ViInt32(buffer_size)
        S220. Output scalar or enum:                                               visatype.ViInt32()

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter
    '''

    assert parameter['is_buffer'] is False, f'Parameter {parameter}'
    assert parameter['numpy'] is False, f'Parameter {parameter}'
    corresponding_buffer_parameters = _get_buffer_parameters_for_size_parameter(parameter, parameters)

    definitions = []
    definition = None

    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] is True:
            definition = '{}.{}(self._{})  # case S110'.format(module_name, parameter['ctypes_type'], config['session_handle_parameter_name'])
        elif parameter['size']['mechanism'] == 'python-code':
            definition = '{}.{}({})  # case S120'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
        elif parameter['enum'] is not None:
            definition = '{}.{}({}.value)  # case S130'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif not corresponding_buffer_parameters:
            definition = '{}.{}({})  # case S150'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif corresponding_buffer_parameters and corresponding_buffer_parameters[0]['direction'] == 'in':  # We are only looking at the first one to see if it is 'in'. Assumes all are the same here, assert below if not
            # Parameter denotes the size of another (the "corresponding") parameter.
            # Interleaved array length is going to be double the length of number of samples.
            # This is used for complex waveforms, where the real and imaginary parts are interleaved in the array.
            if corresponding_buffer_parameters[0].get('complex_array_representation') == 'interleaved_real_number_array':
                definitions.append(parameter['ctypes_variable_name'] + ' = {0}.{1}(0 if {2} is None else len({2}) // 2)  # case S160'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameters[0]['python_name']))
            else:
                array_dimensions = corresponding_buffer_parameters[0].get('array_dimensions')
                if isinstance(array_dimensions, int) and array_dimensions > 1:
                    definitions.append(parameter['ctypes_variable_name'] + ' = {0}.{1}(0 if {2} is None else {2}.size)  # case S161'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameters[0]['python_name']))
                else:
                    definitions.append(parameter['ctypes_variable_name'] + ' = {0}.{1}(0 if {2} is None else len({2}))  # case S160'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameters[0]['python_name']))
        else:
            if corresponding_buffer_parameters[0]['size']['mechanism'] == 'ivi-dance':  # We are only looking at the first one. Assumes all are the same here, assert below if not
                # Verify all corresponding_buffer_parameters are 'out' and 'ivi-dance'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out'
                    assert p['size']['mechanism'] == 'ivi-dance'
                if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                    definition = '{}.{}()  # case S170'.format(module_name, parameter['ctypes_type'])
                elif ivi_dance_step == IviDanceStep.GET_DATA:
                    definition = '{}.{}(error_code)  # case S180'.format(module_name, parameter['ctypes_type'])
                else:
                    assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
            elif corresponding_buffer_parameters[0]['size']['mechanism'] == 'ivi-dance-with-a-twist':  # We are only looking at the first one. Assumes all are the same here, assert below if not
                # Verify all corresponding_buffer_parameters are 'out' and 'ivi-dance-with-a-twist'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out'
                    assert p['size']['mechanism'] == 'ivi-dance-with-a-twist'
                if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                    definition = '{}.{}(0)  # case S190'.format(module_name, parameter['ctypes_type'])
                elif ivi_dance_step == IviDanceStep.GET_DATA:
                    size_parameter_twist = find_size_parameter(corresponding_buffer_parameters[0], parameters, key='value_twist')
                    definition = '{}.{}({}.value)  # case S200'.format(module_name, parameter['ctypes_type'], size_parameter_twist['ctypes_variable_name'])
                else:
                    assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])
            else:
                # Verify all corresponding_buffer_parameters are 'out' and not 'fixed-size'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out', 'Parameter direction not "out", Parameter: {}'.format(p['name'])
                    assert p['size']['mechanism'] != 'fixed-size' and p['size']['mechanism'] != 'fixed-size', 'Parameter: {}, Actual mechanism: {}'.format(p['name'], p['size']['mechanism'])
                definition = '{}.{}({})  # case S210'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        definition = '{}.{}()  # case S220'.format(module_name, parameter['ctypes_type'])

    if definition is not None:
        definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)
    return definitions


def _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name):
    '''These are the different cases for initializing the ctype variable for buffers:

        B510. Input/output numpy array:                                            _get_ctypes_pointer_for_buffer(value=waveform)
        B540. Input buffer (custom type):                                          _get_ctypes_pointer_for_buffer(value=[custom_struct(l) for l in list], library_type=custom_struct)
        B550. Input buffer of simple types:                                        _get_ctypes_pointer_for_buffer(value=array.array('d', list), library_type=visatype.ViReal64)
        B560. Output buffer with mechanism python-code:                            _get_ctypes_pointer_for_buffer(value=array.array('d'), library_type=ViInt32)
        B570. Output buffer with mechanism fixed-size:                             _get_ctypes_pointer_for_buffer(library_type=ViInt32, size=256)
        B580. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
        B590. Output buffer with mechanism ivi-dance, GET_DATA:                    _get_ctypes_pointer_for_buffer(value=array.array('d', [0]) * buffer_size_ctype.value, library_type=ViInt32)
        B600. Output buffer with mechanism passed-in:                              _get_ctypes_pointer_for_buffer(value-array.array('d', [0]) * buffer_size, library_type=ViInt32)
        B610. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
        B620. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       _get_ctypes_pointer_for_buffer(value=array.array('d', [0]) * buffer_size_ctype.value, library_type=ViInt32)

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter

    All versions that have array.array have an alternate format for lists
    '''

    assert parameter['is_buffer'] is True
    definitions = []
    definition = None

    if parameter['numpy'] is True and use_numpy_array is True:
        if parameter.get('complex_array_representation') is None:
            definition = '_get_ctypes_pointer_for_buffer(value={})  # case B510'.format(parameter['python_name'])
        else:
            definition = '_get_ctypes_pointer_for_buffer(value={}, library_type={}.{})  # case B510'.format(parameter['python_name'], module_name, parameter['ctypes_type'])
    elif parameter['direction'] == 'in':
        if custom_type is not None:
            definition = '_get_ctypes_pointer_for_buffer([{0}.{1}(c) for c in {2}], library_type={0}.{1})  # case B540'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        else:
            if parameter['use_array']:
                # If the incoming type is array.array, we can just use that, otherwise we need to create an array.array that is initialized with the passed in value, which must be iterable
                array_declaration = '{0}_array = _convert_to_array(value={0}, array_type="{1}")  # case B550'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(array_declaration)
                definition = '_get_ctypes_pointer_for_buffer(value={}_array, library_type={}.{})  # case B550'.format(parameter['python_name'], module_name, parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(value={}, library_type={}.{})  # case B550'.format(parameter['python_name'], module_name, parameter['ctypes_type'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
    else:
        assert parameter['direction'] == 'out'
        assert 'size' in parameter, "Parameter {} is output buffer but metadata doesn't define its 'size'".format(parameter['name'])
        if parameter['size']['mechanism'] == 'python-code':
            line1 = '{}_size = {}  # case B560'.format(parameter['python_name'], parameter['size']['value'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0]) * {0}_size  # case B560'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(line2)
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B560'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={}.{}, size={}_size)  # case B560'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        elif parameter['size']['mechanism'] == 'fixed':
            assert parameter['size']['value'] != 1, "Parameter {} has 'direction':'out' and 'size':{}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            line1 = '{}_size = {}  # case B570'.format(parameter['python_name'], parameter['size']['value'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0]) * {0}_size  # case B570'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(line2)
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B570'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={}.{}, size={}_size)  # case B570'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        elif parameter['size']['mechanism'] == 'ivi-dance':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case B580'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters)
                line1 = '{}_size = {}.value  # case B590'.format(parameter['python_name'], size_parameter['ctypes_variable_name'])
                definitions.append(line1)
                if parameter['use_array']:
                    line2 = '{0}_array = array.array("{1}", [0]) * {0}_size  # case B590'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                    definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B590'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                    definitions.append(line2)
                elif parameter['use_list']:
                    definition = '_get_ctypes_pointer_for_buffer(library_type={}.{}, size={}_size)  # case B590'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
                else:
                    assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
            else:
                assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
        elif parameter['size']['mechanism'] == 'ivi-dance-with-a-twist':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case B610'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter_twist = find_size_parameter(parameter, parameters, key='value_twist')
                line1 = '{}_size = {}.value  # case B620'.format(parameter['python_name'], size_parameter_twist['ctypes_variable_name'])
                definitions.append(line1)
                if parameter['use_array']:
                    line2 = '{0}_array = array.array("{1}", [0]) * {0}_size  # case B620'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                    definitions.append(line2)
                    definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B620'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                elif parameter['use_list']:
                    definition = '_get_ctypes_pointer_for_buffer(library_type={}.{}, size={}_size)  # case B620'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
                else:
                    assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
            else:
                assert False, "ivi_dance_step {} not valid for parameter {} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])
        elif parameter['size']['mechanism'] == 'passed-in':
            size_parameter = find_size_parameter(parameter, parameters)
            line1 = '{}_size = {}  # case B600'.format(parameter['python_name'], size_parameter['python_name'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0]) * {0}_size  # case B600'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B600'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                definitions.append(line2)
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={}.{}, size={}_size)  # case B600'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        else:
            assert False, "Invalid mechanism for parameters with 'direction':'out': " + str(parameter)

    definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)
    return definitions


def get_parameter_size_check_snippets(parameters):
    '''Returns python snippets to check that parameter sizes are correct.'''
    snippets = []

    for parameter in parameters:
        if parameter['is_string'] or parameter['is_buffer']:
            continue
        else:
            snippets.extend(_get_parameter_size_check_snippets(parameter, parameters))

    return snippets


def _get_parameter_size_check_snippets(parameter, parameters):
    snippets = []

    corresponding_buffer_parameters = _get_buffer_parameters_for_size_parameter(parameter, parameters)
    if not corresponding_buffer_parameters:
        return snippets

    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] or parameter['size']['mechanism'] == 'python-code' or parameter['enum']:
            pass
        elif corresponding_buffer_parameters[0]['direction'] == 'in':  # We are only looking at the first one to see if it is 'in'. Assumes all are the same here, assert below if not
            # Parameter denotes the size of another (the "corresponding") parameter.
            for i in range(1, len(corresponding_buffer_parameters)):
                snippets.append('if {0} is not None and len({0}) != len({1}):  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))
                snippets.append('    raise ValueError("Length of {} and {} parameters do not match.")  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))

    return snippets


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)


def get_enum_value_snippet(value):
    '''Returns value formatted into string, surrounding it with single quotes if it is of str type'''
    return ("'{}'" if type(value) is str else "{}").format(value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/documentation_helper.py sha256=8f797d2ce2f002acd4a288d8d7478110dce1ce8ac3b1ed363812715db5c4d9c1 bytes=33687 -->
## FILE: build/helper/documentation_helper.py

- repository: `ni/nimi-python`
- source_path: `build/helper/documentation_helper.py`
- sha256: `8f797d2ce2f002acd4a288d8d7478110dce1ce8ac3b1ed363812715db5c4d9c1`
- bytes: 33687

````python
from .codegen_helper import filter_parameters
from .codegen_helper import get_params_snippet
from .documentation_snippets import attr_note_text
from .documentation_snippets import enum_note_text
from .documentation_snippets import func_note_text
from .documentation_snippets import rep_cap_attr_desc
from .documentation_snippets import rep_cap_method_desc
from .helper import get_array_type_for_api_type
from .helper import get_numpy_type_for_api_type
from .parameter_usage_options import ParameterUsageOptions

import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def get_indented_docstring_snippet(d, indent=4):
    '''Returns a docstring with the correct amount of indentation.

    First line is not indented.

    Can't use similar construct as get_dictionary_snippet
    ('\n' + (' ' * indent)).join(d_lines) because empty lines would get
    the spaces, which violates pep8 and causes the flake8 step to fail

    Args:
        docstring (str): multiline string to format
        indent (int): How much to indent lines 2+

    Returns:
        str: formatted string
    '''
    d_lines = d.strip().splitlines()
    ret_val = ''
    for line in d_lines:
        if len(ret_val) > 0:
            ret_val += '\n'
            if len(line.rstrip()) > 0:
                ret_val += (' ' * indent)
        ret_val += line.rstrip()
    return ret_val


def get_rst_header_snippet(t, header_level='='):
    '''Get rst formatted heading'''
    ret_val = t + '\n'
    ret_val += header_level * len(t)
    return ret_val


def get_rst_picture_reference(tag, url, title, link, indent=0):
    '''Get rst formatted snippet that represents a picture'''
    ret_val = (' ' * indent) + f'.. |{tag}| image:: {url}\n'
    ret_val += (' ' * (indent + 4)) + f':alt: {title}\n'
    ret_val += (' ' * (indent + 4)) + f':target: {link}\n'
    return ret_val


def _get_rst_table_snippet(node, d, config, indent=0, make_link=True):
    '''Returns an rst table snippet if table_header and/or table_body are in the dictionary'''
    if 'table_body' in d:
        table_body = d['table_body']
    else:
        return ''

    if len(table_body) == 0:
        return ''

    header = False
    # If there is no body, then we ignore the header
    if 'table_header' in d:
        table_header = d['table_header']
        header = True

    table_contents = []
    if header:
        header_contents = []
        for i in table_header:
            contents = _fix_references(node, i, config, make_link)
            header_contents.append(contents)
        table_contents.append(header_contents)

    for t in table_body:
        line_contents = []
        for i in t:
            contents = _fix_references(node, i, config, make_link)
            line_contents.append(contents)
        table_contents.append(line_contents)

    table = as_rest_table(table_contents, header=header)
    return get_indented_docstring_snippet(table, indent)


def get_rst_admonition_snippet(node, admonition, d, config, indent=0):
    '''Returns a rst formatted admonition if the given admonition ('note', 'caution') exists in the dictionary'''
    if admonition in d:
        admonition_content = d[admonition]
        if not isinstance(admonition_content, list):
            admonition_content = [admonition_content]
        a = ''
        for admonition_text in admonition_content:
            a += '\n\n' + (' ' * indent) + f'.. {admonition}:: '
            a += get_indented_docstring_snippet(_fix_references(node, admonition_text, config, make_link=True), indent + 4)
        return a
    else:
        return ''


def add_attribute_rep_cap_tip(attr, config):
    '''Add the appropriate docstring formatted repeated capability tip for an attribute'''
    if 'supported_rep_caps' in attr:
        if 'documentation' not in attr:
            attr['documentation'] = {}

        multi_capability = get_attribute_repeated_caps_with_conjunction(attr)
        single_capability = attr['supported_rep_caps'][0]
        attr['documentation']['tip'] = rep_cap_attr_desc.format(config['module_name'], multi_capability, single_capability, attr['python_name'])


def get_documentation_for_node_rst(node, config, indent=0):
    '''Returns any documentation information formatted for rst

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    '''
    doc = ''
    if 'documentation' not in node:
        return doc

    nd = node['documentation']
    doc += get_rst_admonition_snippet(node, 'caution', nd, config, indent)
    if 'description' in nd:
        doc += '\n\n' + (' ' * indent) + get_indented_docstring_snippet(_fix_references(node, nd['description'], config, make_link=True), indent)

    doc += '\n\n' + (' ' * indent) + _get_rst_table_snippet(node, nd, config, indent)
    doc += get_rst_admonition_snippet(node, 'note', nd, config, indent)
    doc += '\n'
    doc += get_rst_admonition_snippet(node, 'tip', nd, config, indent)
    doc += '\n'

    return doc


def get_docstring_admonition_snippet(node, admonition, d, config, indent=0, extra_newline='\n'):
    '''Returns a docstring formatted admonition if the given admonition ('note', 'caution') exists in the dictionary

    Args:
        admonition (str) - admonition to check and format. I.e. 'note', 'tip', etc.
        d (dict) - documentation note dictionary
        config (dict) - build configuration
        indent (int) - how much each line should be indented
        extra_newline (str) - empty string or newline - needed to keep docstring formatting correct

    Returns:
        str - empty string if no admonition, else formatted string with one or more admonitions
    '''
    if admonition in d:
        admonition_content = d[admonition]
        if not isinstance(admonition_content, list):
            admonition_content = [admonition_content]
        a = ''
        for admonition_text in admonition_content:
            admonition_text = f'{admonition.title()}: {admonition_text}'
            admonition_text = _fix_references(node, admonition_text, config, make_link=False)
            a += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(admonition_text, indent)
            extra_newline = '\n'
        return a
    else:
        return ''


def get_documentation_for_node_docstring(node, config, indent=0):
    '''Returns any documentation information formatted for docstring

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition
    - 'tip' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    '''
    doc = ''
    if 'documentation' not in node:
        return doc

    nd = node['documentation']
    extra_newline = ''
    if 'caution' in nd:
        doc += get_docstring_admonition_snippet(node, 'caution', nd, config, indent, extra_newline)
        extra_newline = '\n'

    if 'description' in nd:
        doc += '\n' + extra_newline + (' ' * indent) + get_indented_docstring_snippet(_fix_references(node, nd['description'], config, make_link=False), indent)
        extra_newline = '\n'

    tbl = _get_rst_table_snippet(node, nd, config, indent, make_link=False)
    if len(tbl) > 0:
        doc += '\n' + extra_newline + (' ' * indent) + tbl
        extra_newline = '\n'

    doc += get_docstring_admonition_snippet(node, 'note', nd, config, indent, extra_newline)

    doc += get_docstring_admonition_snippet(node, 'tip', nd, config, indent, extra_newline)

    return doc.strip()


# We need this in the global namespace so we can reference it from the sub() callback
config = None


def find_enum_by_value(enums, value, start_enum=None):
    '''Returns the enum that contains the given value if there is one

    There should only be one so return that individual parameter and not a list
    '''
    enum = []
    values = []
    if start_enum:
        e = enums[start_enum]
        for v in e['values']:
            if v['name'] == value:
                enum.append(e)
                values.append(v)
        if len(enum) == 1:
            return enum[0], values[0]

    for e_name in enums:
        e = enums[e_name]
        for v in e['values']:
            if v['name'] == value:
                enum.append(e)
                values.append(v)

    if len(enum) == 0 or len(enum) > 1:
        return None, None
    return enum[0], values[0]


def _replace_enum_python_name(e_match):
    '''callback function for enum value regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the enum value, possibly set to sphinx python domain data item link
    '''
    ename = e_match.group(1)
    start_enum = config['start_enum']
    if e_match:
        ename = '{}_VAL_{}'.format(config['module_name'].upper(), ename.replace('\\', ''))
        enum, value = find_enum_by_value(config['enums'], ename, start_enum)
        if enum and enum['codegen_method'] != 'no':
            ename = enum['python_name'] + '.' + value['python_name']

    if config['make_link']:
        return ':py:data:`~{}.{}`'.format(config['module_name'], ename)
    else:
        return f'{ename}'


def find_attribute_by_name(attributes, name):
    '''Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    '''
    attr = [attributes[x] for x in attributes if attributes[x]['name'] == name]
    assert len(attr) <= 1, f'{len(attr)} attributes with name {name}. No more than one is allowed'
    if len(attr) == 0:
        return None
    return attr[0]


def _replace_attribute_python_name(a_match):
    '''callback function for attribute regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the attribute, possibly set to sphinx python domain data item link
    '''
    aname = "Unknown"
    if a_match:
        aname = a_match.group(1).replace('\\', '')
        attr = find_attribute_by_name(config['attributes'], aname)
        if attr:
            aname = attr['name'].lower()

    if config['make_link']:
        if config['module_name'] == 'nitclk':
            return ':py:attr:`{}.SessionReference.{}`'.format(config['module_name'], aname)
        else:
            return ':py:attr:`{}.Session.{}`'.format(config['module_name'], aname)
    else:
        return f'{aname}'


def _replace_func_python_name(f_match):
    '''callback function for function regex sub command

    Args:
        f_match (match object): Match object from the function substitution command

    Returns:
        str: rst link to function using python name, possibly set to sphinx python domain meth item link
    '''
    fname = "Unknown"
    if f_match:
        fname = f_match.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            if 'method_name_for_documentation' in config['functions'][fname]:
                fname = config['functions'][fname]['method_name_for_documentation']
            else:
                fname = config['functions'][fname]['python_name']
        except KeyError:
            print(f'Warning: "{fname}" not found in function metadata. Typo? Generated code will be funky!')
    else:
        print(f'Unknown function name: {f_match.group(1)}')
        print(config['functions'])

    if config['make_link']:
        if config['module_name'] == 'nitclk':
            return ':py:func:`{}.{}`'.format(config['module_name'], fname)
        else:
            return ':py:meth:`{}.Session.{}`'.format(config['module_name'], fname)
    else:
        return f'{fname}'


def _replace_urls(u_match):
    '''callback function for regex when url link needed

    Args:
        u_match (match object): Match object from the function substitution command

    Returns:
        str: replacement url
    '''
    if config['make_link']:
        pages = u_match.group(1)
        pages_list = pages.split(',')
        url_template = config['driver_urls'][config['url_key']]
        url = url_template.format(*pages_list)
        return url
    else:
        return u_match.group(1)


def _fix_references(node, doc, cfg, make_link=False):
    '''Replace ATTR and function mentions in documentation

    Args:
        doc (str): documentation string to be updated
        config (dict): config dictionary from metadata
        make_link (bool): Default False
            True - references are replaced with a rst style link
            False - references are replaced with just the python name

    Returns:
        str: documentation with references replaces based on make_link
    '''

    # We have to put config into the global namespace because we need the information in the search
    # callbacks but cannot pass them in via the search command itself
    global config
    config = cfg

    config['make_link'] = make_link
    config['start_enum'] = None
    if 'enum' in node:
        config['start_enum'] = node['enum']

    attr_search_string = '{}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper())
    func_search_string = '{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', ''))
    func_search_string_lower = '{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].lower().replace('_', ''))
    enum_search_string = '{}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper())
    attr_re = re.compile(attr_search_string)
    func_re = re.compile(func_search_string)
    func_lower_re = re.compile(func_search_string_lower)
    enum_re = re.compile(enum_search_string)

    doc = attr_re.sub(_replace_attribute_python_name, doc)
    doc = func_re.sub(_replace_func_python_name, doc)
    doc = func_lower_re.sub(_replace_func_python_name, doc)
    doc = enum_re.sub(_replace_enum_python_name, doc)

    if 'driver_urls' in cfg:
        for url_key in cfg['driver_urls']:
            url_re = re.compile(fr'{url_key}\((.+?)\)')
            config['url_key'] = url_key
            doc = url_re.sub(_replace_urls, doc)

    # Clean up config
    del config['make_link']
    del config['start_enum']

    # Several other standard replacements
    doc = re.sub(r'\bVI_FALSE\b', 'False', doc)
    doc = re.sub(r'\bVI_TRUE\b', 'True', doc)
    doc = re.sub(r'\ban attribute\b', 'a property', doc)
    doc = re.sub(r'\bAn attribute\b', 'A property', doc)
    doc = re.sub(r'\bAn Attribute\b', 'A Property', doc)
    doc = re.sub(r'\battribute\b', 'property', doc)
    doc = re.sub(r'\battributes\b', 'properties', doc)
    doc = re.sub(r'\bAttribute\b', 'Property', doc)
    doc = re.sub(r'\bAttributes\b', 'Properties', doc)
    doc = re.sub(r'\bfunction\b', 'method', doc)
    doc = re.sub(r'\bfunctions\b', 'methods', doc)
    doc = re.sub(r'\bFunction\b', 'Method', doc)
    doc = re.sub(r'\bFunctions\b', 'Methods', doc)

    return doc


def format_type_for_rst_documentation(param, numpy, config):
    if numpy and param['numpy']:
        p_type = param['numpy_type']
    elif param['enum'] is not None:
        p_type = ':py:data:`{}.{}`'.format(config['module_name'], param['enum'])
    else:
        p_type = param['type_in_documentation']

    # If type_in_documentation was set in metadata, we use it as is
    if param['type_in_documentation_was_calculated'] or numpy:
        if param['is_string'] is True and param['enum'] is None:
            p_type = 'str'
        elif param['is_buffer'] is True and numpy is True:
            p_type = 'numpy.array(dtype=numpy.{})'.format(get_numpy_type_for_api_type(param['type'], config))
        elif param['use_list'] is True:
            p_type = 'list of ' + p_type
        elif param['use_array'] is True:
            p_type = 'array.array("{}")'.format(get_array_type_for_api_type(param['type']))

    return p_type


def get_function_rst(function, method_template, numpy, config, indent=0, method_or_function='method'):
    '''Gets formatted documentation for given function or method that can be used in rst documentation

    Args:
        function (dict): function dictionary
        config (dict): configuration dictoionary (from metadata)
        method_template (dict): entry from function['methos_temlates'] that corresponds to specific entry we are processon
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: rst formatted documentation
    '''

    suffix = method_template['method_python_name_suffix']
    session_method = ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.API_OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION
        output_parameters = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS

    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc.format(config['module_name'], function['repeated_capability_type'], function['python_name'])

    rst = '.. py:{}:: {}{}('.format(method_or_function, function['python_name'], suffix)
    rst += get_params_snippet(function, session_method) + ')'
    indent += 4
    rst += get_documentation_for_node_rst(function, config, indent)

    input_params = filter_parameters(function['parameters'], session_declaration)
    if len(input_params) > 0:
        rst += '\n'
    for p in input_params:
        rst += '\n' + (' ' * indent) + ':param {}:'.format(p['python_name']) + '\n'
        rst += get_documentation_for_node_rst(p, config, indent + 4)

        p_type = format_type_for_rst_documentation(p, numpy, config)
        rst += '\n' + (' ' * indent) + ':type {}: '.format(p['python_name']) + p_type

    output_params = filter_parameters(function['parameters'], output_parameters)
    if len(output_params) > 1:
        rst += '\n\n' + (' ' * indent) + ':rtype: tuple (' + ', '.join([p['python_name'] for p in output_params]) + ')\n\n'
        rst += (' ' * (indent + 4)) + 'WHERE\n'
        for p in output_params:
            p_type = format_type_for_rst_documentation(p, numpy, config)
            rst += '\n' + (' ' * (indent + 4)) + '{} ({}): '.format(p['python_name'], p_type) + '\n'
            rst += get_documentation_for_node_rst(p, config, indent + 8)
    elif len(output_params) == 1:
        p = output_params[0]
        p_type = format_type_for_rst_documentation(p, numpy, config)
        rst += '\n\n' + (' ' * indent) + ':rtype: ' + p_type + '\n'
        rst += (' ' * indent) + ':return:\n' + get_documentation_for_node_rst(p, config, indent + 8)

    return rst


def _format_type_for_docstring(param, numpy, config):
    if numpy and param['numpy']:
        p_type = param['numpy_type']
    else:
        p_type = param['type_in_documentation']

    # We assume everything that is a buffer of ViChar is really a string (otherwise
    # it would end up as 'list of int'
    # If type_in_documentation was set in metadata, we use it as is
    if param['type_in_documentation_was_calculated'] or numpy:
        if param['is_string'] is True and param['enum'] is None:
            p_type = 'str'
        elif param['is_buffer'] is True and numpy is True:
            p_type = 'numpy.array(dtype=numpy.{})'.format(get_numpy_type_for_api_type(param['type'], config))
        elif param['use_list'] is True:
            p_type = 'list of ' + p_type
        elif param['use_array'] is True:
            p_type = 'array.array("{}")'.format(get_array_type_for_api_type(param['type']))

    return p_type


def get_function_docstring(function, numpy, config, indent=0):
    '''Gets formatted documentation for given function that can be used as a docstring

    Args:
        function (dict): function dictionary
        config (dict): configuration dictionary (from metadata)
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: docstring formatted documentation
    '''
    session_declaration = ParameterUsageOptions.SESSION_METHOD_DECLARATION
    output_parameters = ParameterUsageOptions.API_OUTPUT_PARAMETERS
    if numpy:
        session_declaration = ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION
        output_parameters = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS

    docstring = ''
    if function['has_repeated_capability'] is True:
        function['documentation']['tip'] = rep_cap_method_desc.format(config['module_name'], function['repeated_capability_type'], function['python_name'])

    docstring += get_documentation_for_node_docstring(function, config, indent)

    input_params = filter_parameters(function['parameters'], session_declaration)
    if len(input_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Args:'
    for p in input_params:
        docstring += '\n' + (' ' * (indent + 4)) + '{} ({}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
        ds = get_documentation_for_node_docstring(p, config, indent + 8)
        if len(ds) > 0:
            docstring += ' ' + ds
        docstring += '\n'

    output_params = filter_parameters(function['parameters'], output_parameters)
    if len(output_params) > 0:
        docstring += '\n\n' + (' ' * indent) + 'Returns:'
        for p in output_params:
            docstring += '\n' + (' ' * (indent + 4)) + '{} ({}):'.format(p['python_name'], _format_type_for_docstring(p, numpy, config))
            ds = get_documentation_for_node_docstring(p, config, indent + 8)
            if len(ds) > 0:
                docstring += ' ' + ds
            docstring += '\n'

    return docstring


# From http://code.activestate.com/recipes/579054-generate-sphinx-table/
def as_rest_table(data, header=True):
    """Create rst formatted table

    >>> data = [('what', 'how', 'who'),
    ...         ('lorem', 'that is a long value', 3.1415),
    ...         ('ipsum', 89798, 0.2)]
    >>> print(as_rest_table(data))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +=======+======================+========+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    >>> print(as_rest_table(data, header=False))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +-------+----------------------+--------+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    """
    data = data if data else [['No Data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member] for member in data]))
    if sys.version_info.major >= 3:
        sizes = list(sizes)
    num_elts = len(sizes)

    start_of_line = '| '
    vertical_separator = ' | '
    end_of_line = ' |'
    line_marker = '-'

    meta_template = vertical_separator.join(['{{{{{0}:{{{0}}}}}}}'.format(i) for i in range(num_elts)])
    template = f'{start_of_line}{meta_template.format(*sizes)}{end_of_line}'
    # determine top/bottom borders
    to_separator = {ord('|'): '+', ord(' '): '-'}

    start_of_line = start_of_line.translate(to_separator)
    vertical_separator = vertical_separator.translate(to_separator)
    end_of_line = end_of_line.translate(to_separator)
    separator = f'{start_of_line}{vertical_separator.join([x * line_marker for x in sizes])}{end_of_line}'
    # determine header separator
    th_separator_tr = {ord('-'): '='}
    start_of_line = start_of_line.translate(th_separator_tr)
    line_marker = line_marker.translate(th_separator_tr)
    vertical_separator = vertical_separator.translate(th_separator_tr)
    end_of_line = end_of_line.translate(th_separator_tr)
    th_separator = f'{start_of_line}{vertical_separator.join([x * line_marker for x in sizes])}{end_of_line}'
    # prepare result
    table.append(separator)
    # set table header
    titles = data[0]
    table.append(template.format(*titles))

    if header:
        table.append(th_separator)
    else:
        table.append(separator)

    for d in data[1:-1]:
        table.append(template.format(*d))
        table.append(separator)
    table.append(template.format(*data[-1]))
    table.append(separator)
    return '\n'.join(table)


def _square_up_table(nd):
    '''_square_up_table

    The function we use to generate rst tables requires the table be a rectangle. I.e. all
    rows must have the same number of cells. This will check 'table_header' and 'table_body'
    to get the longest row and then make sure they are all that length
    '''
    if 'table_header' not in nd and 'table_body' not in nd:
        return  # We don't need to do anything

    # First we get max length
    max_len = 0
    table_header = nd['table_header'] if 'table_header' in nd else None
    table_body = nd['table_body']
    if table_header:
        max_len = len(table_header)
    for line in table_body:
        if len(line) > max_len:
            max_len = len(line)

    # Now make sure all lines have the same number of cells
    if table_header:
        while len(table_header) != max_len:
            table_header.append('')
    for line in table_body:
        while len(line) != max_len:
            line.append('')


def square_up_tables(config):
    '''Go through all documentation and make sure tables rows have consistent lengths'''
    # First we go through the function and parameter documentation
    for f_name in config['functions']:
        f = config['functions'][f_name]
        for p in f['parameters']:
            if 'documentation' not in p:
                continue
            _square_up_table(p['documentation'])

        if 'documentation' not in f:
            continue
        _square_up_table(f['documentation'])

    # Check attribute documentation
    for a_id in config['attributes']:
        a = config['attributes'][a_id]
        if 'documentation' not in a:
            continue
        _square_up_table(a['documentation'])

    # Check enum documentation
    for e_name in config['enums']:
        e = config['enums'][e_name]
        if 'documentation' not in e:
            continue
        _square_up_table(e['documentation'])
        for v in e['values']:
            if 'documentation' not in v:
                continue
            _square_up_table(v['documentation'])


def _need_func_note(nd, config):
    '''Determine if we need the extra note about function names not matching anything in Python'''
    func_re = re.compile('{}_([A-Za-z0-9_]+)'.format(config['c_function_prefix'].replace('_', '')))
    for m in func_re.finditer(nd):
        fname = m.group(1).replace('.', '').replace(',', '').replace('\\', '')
        try:
            config['functions'][fname]['python_name']
        except KeyError:
            return True

    return False


def _need_attr_note(nd, config):
    '''Determine if we need the extra note about attribute names not matching anything in Python'''
    attr_re = re.compile('{}_ATTR_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in attr_re.finditer(nd):
        aname = m.group(1).replace('\\', '')
        attr = find_attribute_by_name(config['attributes'], aname)
        if not attr:
            return True

    return False


def _need_enum_note(nd, config, start_enum=None):
    '''Determine if we need the extra note about enum names not matching anything in Python'''
    enum_re = re.compile('{}_VAL_([A-Z0-9_]+)'.format(config['module_name'].upper()))
    for m in enum_re.finditer(nd):
        ename = '{}_VAL_{}'.format(config['module_name'].upper(), m.group(1).replace('\\', ''))
        enum, _ = find_enum_by_value(config['enums'], ename, start_enum=start_enum)
        if not enum or enum['codegen_method'] == 'no':
            return True
    return False


def _check_documentation(nd, config, start_enum=None):
    '''_check_documentation

    Look through all the different documentation pieces for this node documentation object for
    any references to functions, attributes or enums that will not exist in the Python API for
    whatever reason. If we find something, we will add a note admonition stating that.

    Args:
        nd (dict) - documentation dictionary - expected to follow standard layout we have been using
        config (dict) - configuration information'
        start_enum (book) - possible context - used for finding enums based on the value
    '''
    keys_to_check = ['description', 'tip', 'caution', 'note']  # table_body needs special handling
    need_func_note = False
    need_attr_note = False
    need_enum_note = False
    for k in keys_to_check:
        if k in nd:
            try:
                need_func_note = need_func_note or _need_func_note(nd[k], config)
                need_attr_note = need_attr_note or _need_attr_note(nd[k], config)
                need_enum_note = need_enum_note or _need_enum_note(nd[k], config)
            except TypeError:
                # If we get a type error then we will assume it is an iterable (list)
                for n in nd[k]:
                    need_func_note = need_func_note or _need_func_note(n, config)
                    need_attr_note = need_attr_note or _need_attr_note(n, config)
                    need_enum_note = need_enum_note or _need_enum_note(n, config)

    if 'table_body' in nd:
        tb = nd['table_body']
        for line in tb:
            for cell in line:
                need_func_note = need_func_note or _need_func_note(cell, config)
                need_attr_note = need_attr_note or _need_attr_note(cell, config)
                need_enum_note = need_enum_note or _need_enum_note(cell, config)

    if need_func_note or need_attr_note or need_enum_note:
        if 'note' not in nd:
            nd['note'] = []
        elif not isinstance(nd['note'], list):
            nd['note'] = [nd['note']]

    if need_func_note:
        nd['note'].append(func_note_text)
    if need_attr_note:
        nd['note'].append(attr_note_text)
    if need_enum_note:
        nd['note'].append(enum_note_text)


def add_notes_re_links(config):
    '''_add_notes_re_links

    Go through all documentation looking for names that won't exist in the Python API and
    adding a note about it.
    '''
    # First we go through the function and parameter documentation
    for f_name in config['functions']:
        f = config['functions'][f_name]
        for p in f['parameters']:
            start_enum = None
            if 'documentation' not in p:
                continue
            if 'enum' in p:
                start_enum = p['enum']
            _check_documentation(p['documentation'], config, start_enum)

        if 'documentation' not in f:
            continue
        start_enum = None
        if 'enum' in f:
            start_enum = f['enum']
        _check_documentation(f['documentation'], config, start_enum)

    # Check attribute documentation
    for a_id in config['attributes']:
        a = config['attributes'][a_id]
        if 'documentation' not in a:
            continue
        start_enum = None
        if 'enum' in a:
            start_enum = a['enum']
        _check_documentation(a['documentation'], config, start_enum)

    # Check enum documentation
    for e_name in config['enums']:
        e = config['enums'][e_name]
        if 'documentation' not in e:
            continue
        _check_documentation(e['documentation'], config)
        for v in e['values']:
            if 'documentation' not in v:
                continue
            _check_documentation(v['documentation'], config)


def get_attribute_repeated_caps(attr):
    '''Creates a comma-separated string representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities'''
    if 'supported_rep_caps' in attr and len(attr['supported_rep_caps']) > 0:
        supported_rep_caps = attr['supported_rep_caps']
        caps = ', '.join(supported_rep_caps)
    else:
        caps = 'None'
    return caps


def get_attribute_repeated_caps_with_conjunction(attr):
    '''Creates a comma-separated string, with terminating 'and', representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities'''
    if 'supported_rep_caps' in attr and len(attr['supported_rep_caps']) > 0:
        supported_rep_caps = attr['supported_rep_caps']
        num_items = len(supported_rep_caps)
        if num_items > 1:
            caps = ', '.join(supported_rep_caps[:-1]) + ' or ' + supported_rep_caps[num_items - 1]
        else:
            caps = supported_rep_caps[0]
    else:
        caps = 'None'
    return caps


def module_supports_repeated_caps(config):
    if 'repeated_capabilities' in config:
        return len(config['repeated_capabilities']) > 0
    return False
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/documentation_snippets.py sha256=50f21bc826b1ed4c79406eae070fb0ae124013bd6c7c2bb41749d293c9003a60 bytes=5504 -->
## FILE: build/helper/documentation_snippets.py

- repository: `ni/nimi-python`
- source_path: `build/helper/documentation_snippets.py`
- sha256: `50f21bc826b1ed4c79406eae070fb0ae124013bd6c7c2bb41749d293c9003a60`
- bytes: 5504

````python
# Different documentation snippets we add to the generated documentation

rep_cap_method_desc = '''
This method can be called on specific {1} within your :py:class:`{0}.Session` instance.
Use Python index notation on the repeated capabilities container {1} to specify a subset,
and then call this method on the result.

Example: :py:meth:`my_session.{1}[ ... ].{2}`

To call the method on all {1}, you can call it directly on the :py:class:`{0}.Session`.

Example: :py:meth:`my_session.{2}`

'''

rep_cap_attr_desc = '''
This property can be set/get on specific {1} within your :py:class:`{0}.Session` instance.
Use Python index notation on the repeated capabilities container {1} to specify a subset.

Example: :py:attr:`my_session.{2}[ ... ].{3}`

To set/get on all {1}, you can call the property directly on the :py:class:`{0}.Session`.

Example: :py:attr:`my_session.{3}`
'''

func_note_text = '''
One or more of the referenced functions are not in the Python API for this driver.
'''

attr_note_text = '''
One or more of the referenced attributes are not in the Python API for this driver.
'''

enum_note_text = '''
One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
'''

session_return_text = '''
A session object representing the device.
'''

options_table_header = ['Attribute', 'Default']
options_table_body = [
    ['range_check', 'True'],
    ['query_instrument_status', 'False'],
    ['cache', 'True'],
    ['simulate', 'False'],
    ['record_value_coersions', 'False'],
    ['driver_setup', '{}'],
]

options_text = '''
Specifies the initial value of certain attributes for the session. The
syntax for **options** is a dictionary of attributes with an assigned
value. For example:

{ 'simulate': False }

You do not have to specify a value for all the attributes. If you do not
specify a value for an attribute, the default value is used.

Advanced Example:
{ 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }
'''

default_close_function_doc = '''
Closes the driver session and cleans up. After calling this the Session object
is no longer valid and cannot be used.
'''

close_function_note = '''
This function is not needed when using the session context manager
'''

default_initiate_function_doc = '''
Calls initiate
'''

initiate_function_note = '''
This function will return a Python context manager that will initiate on entering and abort on exit.
'''


def close_function_def_for_doc(functions, config):
    # This is very specific to session based APIs. We look for a 'close' function in
    # the metadata which is to become a code-generated "private" method of Session
    # for which we provide a public wrapper. Copy its documentation so we apply it to
    # the said public wrapper.
    if 'close_function' not in config or config['close_function'] is None:
        # There is no close function so we don't need to worry about documentation (nitclk only)
        return None

    close_name = config['close_function']
    if close_name in functions:
        import copy
        function_def = copy.deepcopy(functions[close_name])
        if 'documentation' not in function_def:
            function_def['documentation'] = {}
        if 'description' not in function_def['documentation']:
            function_def['documentation']['description'] = default_close_function_doc
        if 'note' not in function_def['documentation']:
            function_def['documentation']['note'] = []
        if type(function_def['documentation']['note']) is not list:
            function_def['documentation']['note'] = [function_def['documentation']['note']]
        function_def['documentation']['note'].append(close_function_note)
        function_def['python_name'] = 'close'
    else:
        assert False, f"No '{close_name}' function defined"

    return function_def


def initiate_function_def_for_doc(functions, config):
    # This is very specific to session based APIs. We look for a 'initiate' function in
    # the metadata which is to become a code-generated "private" method of Session
    # for which we then use in a context manager. Copy its documentation so we apply it to
    # the said context manager.
    session_context_manager_initiate = None
    if 'initiate_function' in config['context_manager_name']:
        session_context_manager_initiate = config['context_manager_name']['initiate_function']

    if session_context_manager_initiate is None:
        # Don't have an initiate
        return None

    if session_context_manager_initiate in functions:
        import copy
        function_def = copy.deepcopy(functions[session_context_manager_initiate])
        if 'documentation' not in function_def:
            function_def['documentation'] = {}
        if 'description' not in function_def['documentation']:
            function_def['documentation']['description'] = default_initiate_function_doc
        if 'note' not in function_def['documentation']:
            function_def['documentation']['note'] = []
        if type(function_def['documentation']['note']) is not list:
            function_def['documentation']['note'] = [function_def['documentation']['note']]
        function_def['documentation']['note'].append(initiate_function_note)
        function_def['python_name'] = 'initiate'
    else:
        assert False, f"No '{session_context_manager_initiate}' function defined"

    return function_def
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/helper.py sha256=aa27d7756ae527988ff1543be5d2e5fe2de92bb04bfc6ee88eed71a40b6a79b3 bytes=7746 -->
## FILE: build/helper/helper.py

- repository: `ni/nimi-python`
- source_path: `build/helper/helper.py`
- sha256: `aa27d7756ae527988ff1543be5d2e5fe2de92bb04bfc6ee88eed71a40b6a79b3`
- bytes: 7746

````python
from packaging.version import Version
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)


# noqa statements because we want to format the table in a readable way
_type_map = {
    'ViConstString':      { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViString':           { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViInt8':             { 'array_type': 'b',      'python_type': 'int',   'numpy_type': 'int8',       },  # noqa: E201, E202, E241
    'ViUInt8':            { 'array_type': 'B',      'python_type': 'int',   'numpy_type': 'uint8',      },  # noqa: E201, E202, E241
    'ViInt16':            { 'array_type': 'h',      'python_type': 'int',   'numpy_type': 'int16',      },  # noqa: E201, E202, E241
    'ViUInt16':           { 'array_type': 'H',      'python_type': 'int',   'numpy_type': 'uint16',     },  # noqa: E201, E202, E241
    'ViInt32':            { 'array_type': 'l',      'python_type': 'int',   'numpy_type': 'int32',      },  # noqa: E201, E202, E241
    'ViUInt32':           { 'array_type': 'L',      'python_type': 'int',   'numpy_type': 'uint32',     },  # noqa: E201, E202, E241
    'ViInt64':            { 'array_type': 'q',      'python_type': 'int',   'numpy_type': 'int64',      },  # noqa: E201, E202, E241
    'ViUInt64':           { 'array_type': 'Q',      'python_type': 'int',   'numpy_type': 'uint64',     },  # noqa: E201, E202, E241
    'ViReal32':           { 'array_type': 'f',      'python_type': 'float', 'numpy_type': 'float32',    },  # noqa: E201, E202, E241
    'ViReal64':           { 'array_type': 'd',      'python_type': 'float', 'numpy_type': 'float64',    },  # noqa: E201, E202, E241
    'ViStatus':           { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViSession':          { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViAttr':             { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViChar':             { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViChar[]':           { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViBoolean':          { 'array_type': None,     'python_type': 'bool',  'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViRsrc':             { 'array_type': None,     'python_type': 'str',   'numpy_type': 'bool_',      },  # noqa: E201, E202, E241
    'NIComplexNumber':    { 'array_type': None,     'python_type': None,    'numpy_type': 'complex128', },  # noqa: E201, E202, E241
    'NIComplexNumberF32': { 'array_type': None,     'python_type': None,    'numpy_type': 'complex64',  },  # noqa: E201, E202, E241
    'NIComplexI16':       { 'array_type': None,     'python_type': None,    'numpy_type': 'int16',      },  # noqa: E201, E202, E241
}


# Coding convention transformation functions.
# TODO(marcoskirsch): not being used
def shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = shout_string.split('_')
    return components[0].lower() \
        + "".join(component.title() for component in components[1:])


def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    return re.sub('([a-z])([A-Z])', r'\1_\2', s1).lower()


# TODO(marcoskirsch): not being used
def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    return f['name'][0].lower() + f['name'][1:]


def sorted_attrs(a):
    return sorted(a, key=lambda k: a[k]['name'])


def get_python_type_for_api_type(api_type, config):
    '''Returns the type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''

    if api_type in _type_map and _type_map[api_type]['python_type'] is not None:
        return _type_map[api_type]['python_type']
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']

    # We didn't find it anywhere so return as is
    return api_type


def get_numpy_type_for_api_type(api_type, config):
    '''Returns the numpy type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''

    if api_type in _type_map and _type_map[api_type]['numpy_type'] is not None:
        return _type_map[api_type]['numpy_type']
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']
        # We didn't find it so assert
        assert False, f'Unknown value for api_type: {api_type}'


def get_array_type_for_api_type(api_type):
    '''Returns the array type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''

    if api_type in _type_map and _type_map[api_type]['array_type'] is not None:
        return _type_map[api_type]['array_type']
    else:
        raise TypeError(f'Only simple types allowed for arrays: {api_type}')


def get_development_status(config):
    '''Get the PyPI Development Status, based on module version

    module_version must be PEP 440 conformant
    See https://packaging.pypa.io/en/latest/version/ and https://www.python.org/dev/peps/pep-0440/
    Arbitrary rules:
    version < 0.5 - alpha
    version >= 0.5 && version < 1.0 - beta
    version >= 1.0
       .devN or .aN - Alpha
       .bN, cN, rcN - Beta
       <nothing> or postN - Stable
    '''
    if 'development_status' in config:
        dev_status = config['development_status']
    else:
        v = Version(config['module_version'])
        if v.release[0] == 0 and v.release[1] < 5:
            dev_status = '3 - Alpha'
        elif v.release[0] == 0:
            dev_status = '4 - Beta'
        else:
            if v.dev is not None or (v.pre is not None and v.pre[0] == 'a'):
                # .devN or .aN
                dev_status = '3 - Alpha'
            elif v.pre is not None:
                # .bN, .cN, .rcN
                dev_status = '4 - Beta'
            else:
                # <nothing> or .postN
                dev_status = '5 - Production/Stable'

    return dev_status


def enum_uses_converter(enum):
    '''Returns True if enum uses converter, False otherwise.

    An enum uses converter if it has both 'enum_to_converted_value_function_name' and
    'converted_value_to_enum_function_name' defined which are not None. If one of them is defined
    and not None but not the other, an AssertionError would be thrown.
    '''
    has_enum_to_converted_value_function_name = enum.get(
        'enum_to_converted_value_function_name', None
    ) is not None
    has_converted_value_to_enum_function_name = enum.get(
        'converted_value_to_enum_function_name', None
    ) is not None
    assert has_enum_to_converted_value_function_name == has_converted_value_to_enum_function_name, (
        "An enum must either define both 'converted_value_to_enum_function_name' and 'converted_value_to_enum_function_name', or define none of them"
    )
    return has_enum_to_converted_value_function_name and has_converted_value_to_enum_function_name
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/metadata_add_all.py sha256=2e8a482aa554bdcc80940681665fd2d98f95dbb7813ecdd41a1ecc57050a00b3 bytes=36188 -->
## FILE: build/helper/metadata_add_all.py

- repository: `ni/nimi-python`
- source_path: `build/helper/metadata_add_all.py`
- sha256: `2e8a482aa554bdcc80940681665fd2d98f95dbb7813ecdd41a1ecc57050a00b3`
- bytes: 36188

````python
# Useful functions for use in the metadata modules

from .documentation_helper import add_notes_re_links
from .documentation_helper import square_up_tables
from .documentation_snippets import options_table_body
from .documentation_snippets import options_table_header
from .documentation_snippets import options_text
from .documentation_snippets import session_return_text
from .helper import camelcase_to_snakecase
from .helper import enum_uses_converter
from .helper import get_numpy_type_for_api_type
from .helper import get_python_type_for_api_type
from .metadata_filters import filter_codegen_attributes
from .metadata_filters import filter_codegen_functions
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .metadata_merge_dicts import merge_helper

import codecs
import copy
import os
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


# These functions can be used by any type, function, attribute or enum


def _add_name(n, name):
    '''Adds a name' key/value pair to the function metadata'''
    assert 'name' not in n, "'name' is already populated which means issue #372 is closed, rendering _add_name() redundant."
    n['name'] = name


def _add_codegen_method(n):
    '''Add 'codegen_method' as public if it isn't already there'''
    if 'codegen_method' not in n:
        n['codegen_method'] = 'public'


def _add_enum(n):
    '''Add 'enum' as None if it isn't already there'''
    if 'enum' not in n:
        n['enum'] = None


def _add_grpc_enum(n):
    '''Add 'grpc_enum' if it isn't already there'''
    if 'grpc_enum' not in n:
        if 'enum' in n:
            n['grpc_enum'] = n['enum']
        else:
            n['grpc_enum'] = None


def _add_python_method_name(function, name):
    '''Adds 'python_name' to the function metadata if not already there'''
    if 'python_name' not in function:
        if function['codegen_method'] == 'private':
            function['python_name'] = '_' + camelcase_to_snakecase(name)
        else:
            function['python_name'] = camelcase_to_snakecase(name)
            assert function['codegen_method'] == 'no' or 'method_name_for_documentation' not in function, "'method_name_for_documentation' not allowed to be set: function['method_name_for_documentation'] = '{}', function['python_name'] = '{}'".format(function['method_name_for_documentation'], function['python_name'])


def _add_interpreter_method_name(function, name):
    '''Adds 'interpreter_name' to the function metadata if not already there'''
    if 'interpreter_name' not in function:
        function['interpreter_name'] = function['python_name'].lstrip('_')


def _add_python_parameter_name(parameter):
    '''Adds a python_name key/value pair to the parameter metadata'''
    if 'python_name' not in parameter:
        parameter['python_name'] = camelcase_to_snakecase(parameter['name'])


def _add_grpc_parameter_name(parameter):
    '''Adds a grpc_name key/value pair to the parameter metadata'''
    if 'grpc_name' not in parameter:
        if parameter.get('grpc_mapped_enum') is not None or parameter['grpc_enum'] is not None:
            parameter['grpc_name'] = parameter['python_name'] + '_raw'
        else:
            parameter['grpc_name'] = parameter['python_name']


def _add_python_type(item, config):
    '''Adds the type to use in the Python API and the documentation to the item metadata, if not already there'''
    if 'python_type' not in item:
        if item['enum'] is None:
            item['python_type'] = get_python_type_for_api_type(item['type'], config)
        else:
            item['python_type'] = 'enums.' + item['enum']

    # If 'type_in_documentation' isn't in the item, use 'python_type'
    item['type_in_documentation_was_calculated'] = False
    if 'type_in_documentation' not in item:
        item['type_in_documentation'] = item['python_type']
        item['type_in_documentation_was_calculated'] = True


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'


def _add_ctypes_type(parameter, config):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    if parameter['type'] == 'ViAddr' and (parameter['use_array'] or parameter['use_list']):
        parameter['ctypes_type'] = 'ViInt8'
    else:
        parameter['ctypes_type'] = parameter['type']
    module_name = ''
    custom_type = find_custom_type(parameter, config)
    if custom_type is not None:
        module_name = custom_type['file_name'] + '.'

    if parameter['is_string']:
        parameter['ctypes_type_library_call'] = 'ctypes.POINTER(ViChar)'
    elif parameter['direction'] == 'out' or parameter['is_buffer'] is True:
        parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + module_name + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = module_name + parameter['ctypes_type']


def _add_complex_array_representation(parameter):
    '''Adds a complex_array_representation parameter to the metadata for complex numbers'''
    if 'complex_array_representation' not in parameter:
        parameter['complex_array_representation'] = None


def _add_array_dimensions(parameter):
    '''Adds a array_dimensions parameter to the metadata for multi dimensional arrays'''
    if 'array_dimensions' not in parameter:
        parameter['array_dimensions'] = 1


def _add_numpy_info(parameter, parameters, config):
    '''Adds the following numpy-related information:

             numpy: Default to False unless already set. True for buffers that allow being passed as a numpy.ndarray.
        numpy_type: The name of the element type to use in the numpy.ndarray.
    '''

    if 'numpy' not in parameter:
        parameter['numpy'] = False

    if parameter['numpy']:
        parameter['numpy_type'] = get_numpy_type_for_api_type(parameter['type'], config)

        if parameter['size']['mechanism'] == 'passed-in':
            size_param = find_size_parameter(parameter, parameters)
            if size_param:
                size_param['use_in_python_api'] = False


def _add_is_error_handling(f):
    '''Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.'''
    # TODO(marcoskirsch): The information is added in functions_addon.py. I think we can instead infer from method
    # name but I am not sure if it's a good idea (heuristics vs being explicit - both error prone in different ways).
    if 'is_error_handling' not in f:
        # Not populated, assume False
        f['is_error_handling'] = False


def _add_buffer_info(parameter, config):
    '''Adds buffer information to the parameter metadata

    These are the pieces of information that will be added to metadata:
        'is_string' - Used for any string type - see below for complete list
        'use_list'  - Used for an array of custom types. We are not putting custom types into array.array or numpy.array
        'use_array' - Used for arrays of simple types
        'is_buffer' - True when either 'use_list' or 'use_array' is True
        'size'      - set to default value of {'mechanism': 'fixed', 'value': 1} if it doesn't already exist
    '''

    assert 'is_buffer' not in parameter or not parameter['is_buffer'], "if 'is_buffer' is in metadata then it must be set to False"
    assert 'is_string' not in parameter, "'is_string' should not be set by metadata or in addons"
    assert 'use_list' not in parameter, "'use_list' should not be set by metadata or in addons"

    is_string = False
    use_array = False
    use_list = False
    original_type = parameter['type']

    # We set all string types to ViString, and say it is NOT a buffer/array
    string_types = ['ViConstString', 'ViRsrc', 'ViString', 'ViChar[]', ]
    if original_type in string_types:
        is_string = True
    elif original_type.find('[]') > 0:
        parameter['type'] = original_type.replace('[]', '')  # TODO(marcoskirsch) Don't change metadata, add new key
        parameter['original_type'] = original_type

        if 'use_array' not in parameter or parameter['use_array'] is False:
            use_list = True
        else:
            use_array = True

    # If 'is_buffer' is in the parameter information and False, we also force 'use_list' and 'use_array' to False
    use_list = parameter['is_buffer'] if 'is_buffer' in parameter else use_list
    use_array = parameter['is_buffer'] if 'is_buffer' in parameter else use_array

    # If not populated, assume {'mechanism': 'fixed', 'value': 1}
    parameter['size'] = parameter['size'] if 'size' in parameter else {'mechanism': 'fixed', 'value': 1}

    parameter['use_array'] = parameter['use_array'] if 'use_array' in parameter else use_array
    parameter['use_list'] = parameter['use_list'] if 'use_list' in parameter else use_list
    parameter['is_string'] = parameter['is_string'] if 'is_string' in parameter else is_string
    parameter['is_buffer'] = parameter['is_buffer'] if 'is_buffer' in parameter else (use_array or use_list)

    assert parameter['is_buffer'] is False or parameter['is_string'] is False


def _add_ctypes_method_call_snippet(parameter):
    '''Code snippet for calling a ctypes method for this parameter.'''
    if parameter['direction'] == 'out' and not parameter['is_buffer'] and not parameter['is_string']:
        parameter['ctypes_method_call_snippet'] = 'None if {0} is None else (ctypes.pointer({0}))'.format(parameter['ctypes_variable_name'])
    else:
        parameter['ctypes_method_call_snippet'] = parameter['ctypes_variable_name']


def _add_interpreter_method_call_snippet(parameter, config):
    '''Code snippet for calling a method of Library for this parameter.'''
    if parameter['is_session_handle']:
        parameter['interpreter_method_call_snippet'] = 'self._' + config['session_handle_parameter_name']
    elif parameter['is_repeated_capability']:
        parameter['interpreter_method_call_snippet'] = 'self._repeated_capability'
    else:
        parameter['interpreter_method_call_snippet'] = parameter['python_name']


def _add_grpc_request_snippet(parameter, config):
    param_name = parameter['grpc_name']

    if parameter['use_list']:
        param_accessor = 'x'
    else:
        param_accessor = parameter['python_name']

    if parameter['is_session_handle']:
        param_value = 'self._' + config['session_handle_parameter_name']
    elif parameter['size']['mechanism'] == 'python-code' and parameter['direction'] == 'in':
        param_value = parameter['size']['value']
    elif parameter['enum'] is not None:
        param_value = param_accessor + '.value'
    elif parameter['type'].startswith('struct_'):
        for custom_type in config['custom_types']:
            if parameter['type'] == custom_type['ctypes_type']:
                ct_grpc_name = custom_type.get('grpc_name', custom_type['python_name'])
                param_value = param_accessor + '._create_copy(grpc_types.' + ct_grpc_name + ')'
                break
        else:
            ctypes_types = [t["ctypes_type"] for t in config["custom_types"]]
            assert False, f'Custom type not found for {parameter["type"]} among {ctypes_types}'
    else:
        param_value = param_accessor

    if parameter['use_list']:
        if param_value == param_accessor:
            param_value = parameter['python_name']
        else:
            param_value = parameter['python_name'] + ' and [' + param_value + ' for x in ' + parameter['python_name'] + ']'

    parameter['grpc_request_snippet'] = param_name + '=' + param_value


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None and parameter['default_value'] is not None:
            name_with_default = parameter['python_name'] + "=enums." + parameter['default_value']
        else:
            name_with_default = parameter['python_name'] + "=" + str(parameter['default_value'])

        if 'python_api_converter_name' in parameter:
            name_for_init = '_converters.{}({}, self._encoding)'.format(parameter['python_api_converter_name'], parameter['python_name'])
        elif parameter['use_in_python_api']:
            name_for_init = parameter['python_name']
        else:
            name_for_init = parameter['default_value']

    else:
        name_with_default = parameter['python_name']
        name_for_init = parameter['python_name']

    parameter['python_name_with_default'] = name_with_default
    parameter['python_name_or_default_for_init'] = str(name_for_init)


def _add_default_value_name_for_docs(parameter, module_name):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None and parameter['default_value'] is not None:
            name = parameter['python_name'] + "=" + module_name + '.' + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + str(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_doc_default'] = name


# Parameter names denoting channel/repeated capabilities was compiled by looking at public header files for different MI drivers.
_repeated_capability_parameter_names = ['channelName', 'channelList', 'channel', 'channelNameList', 'channelsString']


def _add_method_templates(f):
    '''Adds a list of 'method_template_filenames' value to function metadata if not found. This are the mako templates that will be used to render the method.'''
    if 'method_templates' not in f:
        f['method_templates'] = [{'session_filename': '/default_method', 'library_interpreter_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ]
    # Prefix the templates with a / so mako can find them. Not sure mako it works this way.
    for method_template in f['method_templates']:
        method_template['session_filename'] = '/' + method_template['session_filename'] if method_template['session_filename'][0] != '/' else method_template['session_filename']
        method_template['library_interpreter_filename'] = '/' + method_template['library_interpreter_filename'] if method_template['library_interpreter_filename'][0] != '/' else method_template['library_interpreter_filename']
        # Some functions don't get code-generated documentation (i.e. private methods) so no need to specify template for those.
        if 'documentation_filename' in method_template and method_template['documentation_filename'] is not None:
            method_template['documentation_filename'] = '/' + method_template['documentation_filename'] if method_template['documentation_filename'][0] != '/' else method_template['documentation_filename']


def _add_has_repeated_capability(f):
    '''Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated.'''
    if 'has_repeated_capability' not in f:
        f['has_repeated_capability'] = False
        for p in f['parameters']:
            if p['is_repeated_capability']:
                f['has_repeated_capability'] = True
                f['repeated_capability_type'] = p['repeated_capability_type']


def _add_render_in_session_base(f):
    '''Adds a boolean 'render_in_session_base' to the function metadata if not previously populated.

    This tells the code generator to render those methods in _SessionBase class and not Session.
    By default, we want all functions that have repeated capability input and all error handling related functions in _SessionBase but there are exceptions to this rule.
    '''
    if 'render_in_session_base' not in f:
        f['render_in_session_base'] = f['has_repeated_capability'] or f['is_error_handling']


def _add_is_repeated_capability(parameter):
    '''Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.'''
    if 'is_repeated_capability' not in parameter:
        if parameter['name'] in _repeated_capability_parameter_names:
            parameter['is_repeated_capability'] = True
            parameter['repeated_capability_type'] = 'channels'
        else:
            parameter['is_repeated_capability'] = False


def _add_use_session_lock(f):
    '''Set 'use_session_lock' to True unless it already exists

    Only nimodinst doesn't have session locking and the modinst session.py.mako doesn't even look at this
    '''
    f['use_session_lock'] = True if 'use_session_lock' not in f else f['use_session_lock']


def _add_is_session_handle(parameter):
    '''Adds a boolean 'is_session_handle' to the parameter metadata by inferring it from its type, if not previously populated.'''
    if 'is_session_handle' not in parameter:
        parameter['is_session_handle'] = parameter['type'] == 'ViSession' and parameter['direction'] == 'in'


def _fix_type(parameter):
    '''Replace any spaces in the parameter type with an underscore.'''
    parameter['type'] = parameter['type'].replace('[ ]', '[]').replace(' []', '[]').replace(' ', '_')


# TODO(olsl21): Metadata is inconsistent with regards to how structs are treated.
#  This is a hack to workaround that inconsistency. The real root cause is tracked
#  by internal NI bug 1918101. Once that is addressed, this method can be removed.
def _fix_custom_type(parameter, config):
    '''Add "struct_" prefix to custom type if necessary to match its ctypes_type.'''
    parameter_type_with_struct_prefix = 'struct_' + parameter['type']
    for custom_type in config['custom_types']:
        if parameter_type_with_struct_prefix == custom_type['ctypes_type']:
            parameter['type'] = custom_type['ctypes_type']
            break


def _add_use_in_python_api(p, parameters):
    '''Add 'use_in_python_api' if not there with value of True'''
    if 'use_in_python_api' not in p:
        p['use_in_python_api'] = True

    if p['size']['mechanism'] == 'len' or p['size']['mechanism'] == 'ivi-dance':
        size_param = find_size_parameter(p, parameters)
        size_param['use_in_python_api'] = False

    if p['size']['mechanism'] == 'ivi-dance-with-a-twist':
        # We have two parameters to remove from the API
        size_param = find_size_parameter(p, parameters)
        size_param['use_in_python_api'] = False
        size_param = find_size_parameter(p, parameters, key='value_twist')
        size_param['use_in_python_api'] = False


def _setup_init_function(functions, config):
    '''Copy the selected init function to a known name and update information about it for documentation purposes'''
    try:
        init_function = copy.deepcopy(functions[config['init_function']])
        init_function['codegen_method'] = 'no'

        # Change the init_function information for generating the docstring
        # We are assuming the last parameter is vi out
        for p in init_function['parameters']:
            if p['name'] == config['session_handle_parameter_name']:
                p['documentation']['description'] = session_return_text
                p['type_in_documentation'] = config['module_name'] + '.Session'
                p['python_name'] = 'session'
            elif p['python_name'] == 'option_string':
                p['python_name'] = 'options'
                p['python_name_with_default'] = 'options={}'
                p['documentation']['description'] = options_text
                p['documentation']['table_header'] = options_table_header
                p['documentation']['table_body'] = options_table_body
                # Additional options documentation may be added in metadata __init__ if it is driver specific

        functions['_init_function'] = init_function
    except KeyError:
        if 'init_function' not in config or config['init_function'] is None:
            # We don't have an init function or it is set to None (same thing) so we can't
            # do anything here
            pass
        else:
            print("Couldn't find {} init function".format(config['init_function']))


def add_all_function_metadata(functions, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    functions = merge_helper(functions, 'functions', config, use_re=True)

    for f in functions:
        _add_codegen_method(functions[f])
        # Some drivers do not have any documentation, so make sure the
        # documentation key exists
        if 'documentation' not in functions[f]:
            functions[f]['documentation'] = {}

    for f in functions:
        _add_name(functions[f], f)
        _add_python_method_name(functions[f], f)
        _add_interpreter_method_name(functions[f], f)
        _add_is_error_handling(functions[f])
        _add_method_templates(functions[f])
        _add_use_session_lock(functions[f])
        for p in functions[f]['parameters']:
            if 'documentation' not in p:
                p['documentation'] = {}
            _add_enum(p)
            _add_grpc_enum(p)
            _fix_type(p)
            _add_buffer_info(p, config)
            _fix_custom_type(p, config)
            _add_use_in_python_api(p, functions[f]['parameters'])
            _add_python_parameter_name(p)
            _add_grpc_parameter_name(p)
            _add_python_type(p, config)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p, config)
            _add_complex_array_representation(p)
            _add_array_dimensions(p)
            _add_numpy_info(p, functions[f]['parameters'], config)
            _add_default_value_name(p)
            _add_default_value_name_for_docs(p, config['module_name'])
            _add_is_repeated_capability(p)
            _add_is_session_handle(p)
            _add_ctypes_method_call_snippet(p)
            _add_interpreter_method_call_snippet(p, config)
            _add_grpc_request_snippet(p, config)

        # We can't do these until the parameters have been processed
        _add_has_repeated_capability(functions[f])
        _add_render_in_session_base(functions[f])

    _setup_init_function(functions, config)

    return functions


def _add_python_name(a, attributes):
    '''Adds 'python_name' - lower case + leading '_' if first character is a digit'''
    if 'python_name' not in attributes[a]:
        n = attributes[a]['name'].lower()
        if attributes[a]['codegen_method'] == 'private':
            n = '_' + n

        attributes[a]['python_name'] = n

    assert not attributes[a]['python_name'][0].isdigit()


def _add_default_attribute_class(a, attributes):
    '''Set 'attribute_class' if not set.

    By default, the 'attribute_class' is only based on the 'type'.
    It can be set in attributes_addon if we want to convert to/from a different datatype, such as hightime.timedelta
    '''
    if 'attribute_class' not in attributes[a]:
        attributes[a]['attribute_class'] = 'Attribute' + attributes[a]['type']


def add_all_attribute_metadata(attributes, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    attributes = merge_helper(attributes, 'attributes', config, use_re=False)

    for a in attributes:
        _add_codegen_method(attributes[a])
        _add_enum(attributes[a])
        _add_grpc_enum(attributes[a])
        _add_python_name(a, attributes)
        _add_python_type(attributes[a], config)
        _add_default_attribute_class(a, attributes)

    return attributes


def _add_enum_codegen_method(enums, config):
    '''Adds 'codegen_method' if not explicitly specified that will determine whether and how the enum is code-generated.

    If an enum does not explicitly specify its 'codegen_method' in metadata, it will be assigned the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it. The default codegen_method is 'no' (if no function nor attribute uses it).

    If an enum explicitly specifies its 'codegen_method' in metadata, it will be checked against the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it (if its explicit 'codegen_method' is more restrictive than the calculated least
    restrictive codegen_method and it does not use converter, a ValueError would be thrown).

    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public' if not explicitly specified)
    '''
    enum_to_client_functions = _get_functions_that_use_enums(enums, config)
    enum_to_client_attributes = _get_attributes_that_use_enums(enums, config)
    for e in enums:
        least_restrictive_codegen_method = _get_least_restrictive_codegen_method(
            set.union(
                {config['functions'][f]['codegen_method'] for f in enum_to_client_functions[e]},
                {config['attributes'][a]['codegen_method'] for a in enum_to_client_attributes[e]}
            )
        )
        if 'codegen_method' not in enums[e]:
            enums[e]['codegen_method'] = least_restrictive_codegen_method
        else:
            explicit_codegen_method = enums[e]['codegen_method']
            # Check if explicit_codegen_method is more restrictive than
            #  least_restrictive_codegen_method and the enum does not use converter
            # _get_least_restrictive_codegen_method() might change 'python-only' to 'public',
            #  so avoid comparing explicit_codegen_method with the output of
            #  _get_least_restrictive_codegen_method() directly
            if _get_least_restrictive_codegen_method([
                explicit_codegen_method,
                least_restrictive_codegen_method
            ]) != _get_least_restrictive_codegen_method([
                explicit_codegen_method
            ]) and not enum_uses_converter(enums[e]):
                client_function_names = enum_to_client_functions[e]
                client_attribute_names = [
                    config['attributes'][a]['name'] for a in enum_to_client_attributes[e]
                ]
                raise ValueError(
                    f'Codegen_method of enum {e} used by functions {client_function_names} and attributes {client_attribute_names} must be {least_restrictive_codegen_method}, is {explicit_codegen_method}'
                )


def _get_functions_that_use_enums(enums, config):
    '''Generate a dict that maps each enum to a list of functions that use it in their parameters'''
    enum_to_client_functions = {e: [] for e in enums}
    for f in filter_codegen_functions(config['functions']):
        for p in config['functions'][f]['parameters']:
            e = p['enum']
            if e is not None:
                if e not in enum_to_client_functions:
                    print(f'Missing enum {e} referenced by function {f}')
                else:
                    enum_to_client_functions[e].append(f)
    return enum_to_client_functions


def _get_attributes_that_use_enums(enums, config):
    '''Generate a dict that maps each enum to a list of attributes that use it'''
    enum_to_client_attributes = {e: [] for e in enums}
    for a in filter_codegen_attributes(config['attributes']):
        e = config['attributes'][a]['enum']
        if e is not None:
            if e not in enum_to_client_attributes:
                print(f'Missing enum {e} referenced by attribute {a}')
            else:
                enum_to_client_attributes[e].append(a)
    return enum_to_client_attributes


def _get_least_restrictive_codegen_method(codegen_methods):
    '''Get the least restrictive codegen_method among the input codegen_methods.

    If the codegen_methods parameter is empty, return 'no'.
    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public')
    '''
    if len(codegen_methods) == 0:
        return 'no'

    codegen_method_to_permissiveness = {
        'no': 0,
        'private': 1,
        'python-only': 2,
        'public': 2
    }
    permissiveness_to_codegen_method = {
        0: 'no',
        1: 'private',
        2: 'public'
    }
    return permissiveness_to_codegen_method[
        max(codegen_method_to_permissiveness[codegen_method] for codegen_method in codegen_methods)
    ]


def _add_enum_value_python_name(enum_info, config):
    '''Add 'python_name' for all values, removing any common prefixes and suffixes'''
    for v in enum_info['values']:
        if 'python_name' not in v:
            v['python_name'] = v['name'].replace('{}_VAL_'.format(config['module_name'].upper()), '')

    # We are using an os.path function do find any common prefix. So that we don't
    # get 'O' in 'ON' and 'OFF' we remove characters at the end until they are '_'
    names = [v['python_name'] for v in enum_info['values']]
    prefix = os.path.commonprefix(names)
    while len(prefix) > 0 and prefix[-1] != '_':
        prefix = prefix[:-1]

    # If the prefix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_prefix' in config and prefix in config['enum_whitelist_prefix']:
        prefix = ''

    # We only remove the prefix if there is one and it isn't '_'.
    # '_' only means the name starts with a number
    if len(prefix) > 0 and prefix != '_':
        for v in enum_info['values']:
            assert v['python_name'].startswith(prefix), '{} does not start with {}'.format(v['name'], prefix)
            v['prefix'] = prefix
            v['python_name'] = v['python_name'].replace(prefix, '')

    # Now we need to look for common suffixes
    # Using the slow method of reversing a string for readability
    rev_names = [''.join(reversed(v['python_name'])) for v in enum_info['values']]
    suffix = os.path.commonprefix(rev_names)
    while len(suffix) > 0 and suffix[-1] != '_':
        suffix = suffix[:-1]

    # Unreverse the suffix
    suffix = ''.join(reversed(suffix))

    # If the suffix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_suffix' in config and suffix in config['enum_whitelist_suffix']:
        suffix = ''

    # We only remove the suffix if there is one.
    # '_' only means the name starts with a number
    if len(suffix) > 0:
        for v in enum_info['values']:
            assert v['python_name'].endswith(suffix), '{} does not end with {}'.format(v['name'], suffix)
            v['suffix'] = suffix
            v['python_name'] = v['python_name'][:-len(suffix)]

    # We need to check again to see if we have any values that start with a digit
    # If we are not going to code generate this enum, we don't care about this
    for v in enum_info['values']:
        assert v['python_name'], enum_info
        if enum_info['codegen_method'] != 'no' and v['python_name'][0].isdigit():
            raise ValueError('Invalid name: {}'.format(v['python_name']))  # pragma: no cover

    return enum_info


def fixup_enum_names(config):
    '''Fix enum types for private enums

    Now that we have all the metadata calculated, we need to fix any enum types in attributes and functions
    where the underlying enum is private. At the time the 'python_type' was set, we hadn't yet calculated
    whether the enum would be private or not. We couldn't because we needed to process all the functions and
    attributes first.
    '''
    # Check all the functions that will be code generated
    for f in config['functions']:
        if config['functions'][f]['codegen_method'] != 'no':
            for p in config['functions'][f]['parameters']:
                if p['enum'] is not None and config['enums'][p['enum']]['codegen_method'] == 'private':
                    # We need to update the python type since the enum is private
                    p['python_type'] = 'enums.' + config['enums'][p['enum']]['python_name']

    # Check all attributes that will be code generated
    for a in config['attributes']:
        attr = config['attributes'][a]
        if attr['codegen_method'] != 'no':
            if attr['enum'] is not None and config['enums'][attr['enum']]['codegen_method'] == 'private':
                # We need to update the python type since the enum is private
                attr['python_type'] = 'enums.' + config['enums'][attr['enum']]['python_name']


def add_all_enum_metadata(enums, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    enums = merge_helper(enums, 'enums', config, use_re=False)

    # Workaround for NI Internal CAR #675174
    try:
        replacement_enums = config['modules']['metadata.enums_addon'].__getattribute__('replacement_enums')
        for e in replacement_enums:
            enums[e] = replacement_enums[e]
    except AttributeError:
        pass

    _add_enum_codegen_method(enums, config)
    for e in enums:
        enums[e] = _add_enum_value_python_name(enums[e], config)
        enums[e]['python_name'] = ('_' if enums[e]['codegen_method'] == 'private' else '') + (enums[e]['python_name'] if 'python_name' in enums[e] else e)

    return enums


def add_all_config_metadata(config):
    '''add_all_config_metadata

    Ensure all defaults added to config
    '''
    config = merge_helper(config, 'config', config, use_re=False)

    if 'use_locking' not in config:
        config['use_locking'] = True

    if 'uses_nitclk' not in config:
        config['uses_nitclk'] = False

    return config


def add_all_metadata(functions, attributes, enums, config, persist_output=True):
    '''merge and add all additional metadata_dir

    Updates all parameters
        functions, attributes, enums - addon data merged, additional metadata
        config - functions, attributes, enums added
    '''
    config = add_all_config_metadata(config)

    functions = add_all_function_metadata(functions, config)
    config['functions'] = functions

    attributes = add_all_attribute_metadata(attributes, config)
    config['attributes'] = attributes

    enums = add_all_enum_metadata(enums, config)
    config['enums'] = enums

    add_notes_re_links(config)

    square_up_tables(config)

    fixup_enum_names(config)

    pp_persist = pprint.PrettyPrinter(indent=4, width=200)
    metadata_dir = os.path.join('generated', 'processed_metadata')

    # If we are not persisting the output (I.e. during a test) we return early
    if not persist_output:
        return config

    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_functions.py'), "w", "utf-8") as text_file:
        text_file.write(f"function =\n{pp_persist.pformat(functions)}")

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_attributes.py'), "w", "utf-8") as text_file:
        text_file.write(f"attributes =\n{pp_persist.pformat(attributes)}")

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_enums.py'), "w", "utf-8") as text_file:
        text_file.write(f"enums =\n{pp_persist.pformat(enums)}")

    # We need to delete modules before we deepcopy, otherwise we get an error
    # These were needed only for merging, which has already happened
    del config['modules']

    # We need to make a copy so we can delete functions, attributes and enums since
    # they are already in individual files
    config_copy = copy.deepcopy(config)
    del config_copy['functions']
    del config_copy['attributes']
    del config_copy['enums']

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_config.py'), "w", "utf-8") as text_file:
        text_file.write(f"enums =\n{pp_persist.pformat(config_copy)}")

    return config
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/metadata_filters.py sha256=4fc6264adc22c3c1ec61a5530fa6a56d463e0e38c9caf9b5d175d892f9b4b71b bytes=22532 -->
## FILE: build/helper/metadata_filters.py

- repository: `ni/nimi-python`
- source_path: `build/helper/metadata_filters.py`
- sha256: `4fc6264adc22c3c1ec61a5530fa6a56d463e0e38c9caf9b5d175d892f9b4b71b`
- bytes: 22532

````python
from .metadata_find import find_len_size_parameter_names
from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions

import pprint
pp = pprint.PrettyPrinter(indent=4)
# Filters

_ParameterUsageOptionsFiltering = {
    ParameterUsageOptions.SESSION_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in, len',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in, len',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in',
        'python_api_list': False,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in',
        'python_api_list': False,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.SESSION_METHOD_CALL: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.LIBRARY_METHOD_DECLARATION: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.LIBRARY_METHOD_CALL: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.GRPC_REQUEST_PARAMETERS: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.CTYPES_ARGTYPES: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in, len',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.INPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.API_OUTPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': False,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': True,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': False,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.GRPC_OUTPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': False,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.NUMPY_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': True,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.IVI_DANCE_PARAMETER: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'ivi-dance, ivi-dance-with-a-twist',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.LEN_PARAMETER: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'len',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.INPUT_ENUM_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': True,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': False,
    },
    ParameterUsageOptions.COMPLEX_NUMBER_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_numpy_parameters': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
        'skip_all_except_complex_array_representation_parameters': True,
    },
}

# Only difference is we want to skip parameters not in api
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_DECLARATION] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_DECLARATION].copy()
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_DECLARATION]['python_api_list'] = False

# Only difference is we want to skip parameters not in api
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_CALL] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_CALL].copy()

_ParameterUsageOptionsFiltering[ParameterUsageOptions.INTERPRETER_METHOD_CALL] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION].copy()
_ParameterUsageOptionsFiltering[ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION].copy()
_ParameterUsageOptionsFiltering[ParameterUsageOptions.CDLL_METHOD_CALL] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.LIBRARY_METHOD_CALL].copy()


def filter_parameters(parameters, parameter_usage_options):
    '''filter_parameters

    Filters and reorders the parameters passed in based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _ParameterUsageOptionsFiltering[parameter_usage_options]

    parameters_to_use = []

    # Filter based on options
    ivi_dance_size_parameter = None
    len_size_parameter_names = set()
    size_twist_parameter = None
    # If we are being called looking for the ivi-dance, len or code param, we do not care about the size param so we do
    #  not call back into ourselves, to avoid infinite recursion
    if parameter_usage_options not in [ParameterUsageOptions.IVI_DANCE_PARAMETER, ParameterUsageOptions.LEN_PARAMETER]:
        # Determine any size parameters that should be skipped based on the presence of ivi-dance or len-sized buffers.
        # For ivi-dance, there is a single shared size parameter; for len, there may be multiple independent size parameters.
        ivi_dance_size_parameter = find_size_parameter(filter_ivi_dance_parameters(parameters), parameters)
        len_size_parameter_names = find_len_size_parameter_names(parameters)
        size_twist_parameter = find_size_parameter(filter_ivi_dance_twist_parameters(parameters), parameters, key='value_twist')
    for x in parameters:
        skip = False
        if x['direction'] == 'out' and options_to_use['skip_output_parameters']:
            skip = True
        if x['direction'] == 'in' and options_to_use['skip_input_parameters']:
            skip = True
        if ivi_dance_size_parameter is not None and x == ivi_dance_size_parameter and options_to_use['skip_size_parameter']:
            skip = True
        if len_size_parameter_names and x['name'] in len_size_parameter_names and options_to_use['skip_size_parameter']:
            skip = True
        if size_twist_parameter is not None and x == size_twist_parameter and options_to_use['skip_size_parameter']:
            skip = True
        if x['is_session_handle'] is True and options_to_use['skip_session_handle']:
            skip = True
        if x['is_repeated_capability'] is True and options_to_use['skip_repeated_capability_parameter']:
            skip = True
        if x['enum'] is None and options_to_use['skip_non_enum_parameter']:
            skip = True
        if options_to_use['mechanism'] != 'any' and x['size']['mechanism'] not in options_to_use['mechanism']:
            skip = True
        if options_to_use['skip_numpy_parameters'] is True and x['numpy'] is True:
            skip = True
        if options_to_use['skip_all_except_numpy_parameters'] and not x['numpy']:
            skip = True
        if options_to_use['but_keep_output_numpy_array_parameters'] is True and x['numpy'] is True:
            skip = False
        if not options_to_use['python_api_list'] and not x['use_in_python_api']:
            skip = True
        if options_to_use['skip_all_except_complex_array_representation_parameters'] and x['complex_array_representation'] is None:
            skip = True
        if not skip:
            parameters_to_use.append(x)

    # Reorder based on options
    if options_to_use['reordered_for_default_values']:
        new_order = []
        for x in parameters_to_use:
            if 'default_value' not in x:
                new_order.append(x)
        for x in parameters_to_use:
            if 'default_value' in x:
                new_order.append(x)
        parameters_to_use = new_order

    return parameters_to_use


def filter_ivi_dance_parameters(parameters):
    '''Returns the ivi-dance parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the ivi-dance.

    asserts all parameters that use ivi-dance reference the same parameter
    Args:
        parameters: parameters to be checked

    Return:
        None if no ivi-dance parameter found
        Parameters dict if one is found
    '''
    params = filter_parameters(parameters, ParameterUsageOptions.IVI_DANCE_PARAMETER)
    if len(params) > 0:
        size_param = params[0]['size']['value']
        assert all(x['size']['value'] == size_param for x in params)
    return params


def filter_ivi_dance_twist_parameters(parameters):
    '''Returns the ivi-dance parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the ivi-dance.

    asserts all parameters that use ivi-dance reference the same parameter
    Args:
        parameters: parameters to be checked

    Return:
        None if no ivi-dance parameter found
        Parameters dict if one is found
    '''
    params = filter_parameters(parameters, ParameterUsageOptions.IVI_DANCE_PARAMETER)
    if len(params) > 0:
        if params[0]['size']['mechanism'] == 'ivi-dance-with-a-twist':
            size_param = params[0]['size']['value_twist']
            assert all(x['size']['value_twist'] == size_param for x in params)
    return params


def filter_len_parameters(parameters):
    '''Returns the len parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the value of a different parameter.

    Note: Multiple len parameters may reference different size parameters.
    Args:
        parameters: parameters to be checked

    Return:
        Empty list if no len parameter found
        List of parameter dicts if any are found
    '''
    params = filter_parameters(parameters, ParameterUsageOptions.LEN_PARAMETER)
    return params


def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no' and v['codegen_method'] != 'library-only'}


def filter_library_functions(functions):
    '''Returns function metadata only for those functions to included the library layer (library.py and mock_helper.py)'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no' and v['codegen_method'] != 'python-only'}


def filter_public_functions(functions):
    '''Returns function metadata only for those functions that are public'''
    return {k: v for k, v in functions.items() if v['codegen_method'] == 'public' or v['codegen_method'] == 'python-only'}


def filter_codegen_attributes(attributes):
    '''Returns attribute metadata only for those attributes to be included in codegen'''
    return {k: v for k, v in attributes.items() if v['codegen_method'] != 'no'}


def filter_codegen_attributes_public_only(attributes):
    '''Returns attribute metadata only for those attributes to be included in codegen'''
    return {k: v for k, v in attributes.items() if v['codegen_method'] == 'public'}


def filter_codegen_enums(enums):
    '''Returns enum metadata only for those enums to be included in codegen'''
    return {k: v for k, v in enums.items() if v['codegen_method'] != 'no'}


def are_complex_parameters_used(functions):
    '''Returns bool based on whether any complex parameters are used in the functions metadata.'''
    are_complex_parameters_used = False
    complex_parameters = []
    for k, v in functions.items():
        complex_parameters = filter_parameters(v['parameters'], ParameterUsageOptions.COMPLEX_NUMBER_PARAMETERS)
        if complex_parameters != []:
            are_complex_parameters_used = True
            break
    return are_complex_parameters_used
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/metadata_find.py sha256=fa7d7f2706a80ec3048df217d67ab0545d7355fdef2310c0e1a36056e6f64273 bytes=2647 -->
## FILE: build/helper/metadata_find.py

- repository: `ni/nimi-python`
- source_path: `build/helper/metadata_find.py`
- sha256: `fa7d7f2706a80ec3048df217d67ab0545d7355fdef2310c0e1a36056e6f64273`
- bytes: 2647

````python
# Find utilities
def find_parameter(name, parameters):
    parameter = [x for x in parameters if x['name'] == name]
    assert len(parameter) == 1, f'Parameter {name} not found in {parameters}. Check your metadata.'
    return parameter[0]


def find_session_handle_parameter(parameters):
    '''Returns the ViSession parameter.

    Usually it's the one marked as is_session_handle. For Init functions, it's the output parameter.
    '''
    matching = [p for p in parameters if p['is_session_handle']]
    assert len(matching) <= 1, f'More than one parameter found with is_session_handle=True:\n{parameters}'
    if len(matching) == 0:
        matching = [p for p in parameters if p['type'] == 'ViSession']
        assert len(matching) <= 1, f'More than one ViSession parameter found:\n{parameters}'
        assert len(matching) > 0, f'No ViSession parameter found:\n{parameters}'
    return matching[0]


def find_size_parameter(parameter_list, parameters, key='value'):
    '''Returns the parameter that is used to specify the size other parameters. Applies to 'ivi-dance', 'ivi-dance-with-a-twist' and 'passed-in'.

    Most behaviors will use 'value', but 'ivi-dance-with-a-twist' uses 'value' and 'value_twist'
    '''
    assert type(parameter_list) is list or type(parameter_list) is dict, f'Wrong type: {type(parameter_list)}'
    if len(parameter_list) == 0:
        return None
    # Assumption: all parameters have the same size parameter, so we only need to use the first one
    try:
        # Try first as a list
        if key in parameter_list[0]['size']:
            return find_parameter(parameter_list[0]['size'][key], parameters)
    except KeyError:
        # Not a list, so must be a single parameter
        if key in parameter_list['size']:
            return find_parameter(parameter_list['size'][key], parameters)

    return None


def find_len_size_parameter_names(parameters):
    '''Returns names of size parameters referenced by len-sized parameters.

    A function may have multiple len-sized parameters, each with a different size parameter.
    '''
    len_size_parameter_names = set()
    len_parameters = [parameter for parameter in parameters if parameter['size']['mechanism'] == 'len']

    for parameter in len_parameters:
        len_size_parameter = find_size_parameter(parameter, parameters)
        if len_size_parameter is not None:
            len_size_parameter_names.add(len_size_parameter['name'])

    return len_size_parameter_names


def find_custom_type(p, config):
    for c in config['custom_types']:
        if p['ctypes_type'] == c['ctypes_type']:
            return c
    return None
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/metadata_merge_dicts.py sha256=2feadaec7c2fec3d92fa317ebfc5fff3373c7680ab76348618800c785654a7c5 bytes=2884 -->
## FILE: build/helper/metadata_merge_dicts.py

- repository: `ni/nimi-python`
- source_path: `build/helper/metadata_merge_dicts.py`
- sha256: `2feadaec7c2fec3d92fa317ebfc5fff3373c7680ab76348618800c785654a7c5`
- bytes: 2884

````python
# Useful functions for use in the metadata modules

import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=80)


def merge_helper(metadata, metadata_type, config, use_re):
    metadata_module = f'metadata.{metadata_type}_addon'
    if 'modules' in config and metadata_module in config['modules']:
        for m in dir(config['modules'][metadata_module]):
            if m.startswith(f'{metadata_type}_additional_'):
                # We need to explicitly copy new entries
                outof = config['modules'][metadata_module].__getattribute__(m)
                for a in outof:
                    metadata[a] = outof[a]
            elif m.startswith(f'{metadata_type}_'):
                merge_dicts(metadata, config['modules'][metadata_module].__getattribute__(m), use_re, m)

    # Delete any entries that are empty
    # Have to do this in two steps. Otherwise the dictionary changes size and errors
    to_delete = []
    for m in metadata:
        if type(m) is dict and len(metadata[m]) == 0:
            to_delete.append(m)
    for m in to_delete:
        metadata.pop(m, None)

    return metadata


def merge_dicts(into, outof, use_re, dict_name):
    '''merge_dicts

    Recursively merges the contents of dictionary 'outof' into dictionary 'into'.
    'into' may contain lists as values.
    'outof' may contain regular expressions as keys, in which case values are
    merged with all key matches in into.
    '''
    for item in sorted(outof):
        # If we're not using regex's then this is an easy check
        if not use_re and item not in into and dict_name is not None:
            raise KeyError(f'Key {item} from {dict_name} is not in the destination')
        # If we are using regex's we need to seach all keys to see if any match
        if use_re and dict_name is not None:
            key_exists = False
            for item2 in into:
                if re.search(item, item2):
                    key_exists = True
            if not key_exists:
                raise KeyError(f'Key {item} from {dict_name} is not in the destination')

        if type(outof[item]) is dict:
            if item in into:
                merge_dicts(into[item], outof[item], use_re, None)
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:
                # attributes keys are integers so they do not need the regex check (and
                # in fact will error)
                if type(item) is str:
                    # Handle regex in addon
                    for item2 in into:
                        if use_re is True and re.search(item, item2):
                            assert type(into[item2]) is dict
                            merge_dicts(into[item2], outof[item], use_re, None)
        else:
            into[item] = outof[item]
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/helper/parameter_usage_options.py sha256=44accea2435bd7c71f74422c33f733935759968da2bf0cbc66080aeda60ea8eb bytes=2717 -->
## FILE: build/helper/parameter_usage_options.py

- repository: `ni/nimi-python`
- source_path: `build/helper/parameter_usage_options.py`
- sha256: `44accea2435bd7c71f74422c33f733935759968da2bf0cbc66080aeda60ea8eb`
- bytes: 2717

````python
from enum import Enum


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class ParameterUsageOptions(AutoNumber):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = ()
    '''For declaring a regular method in Session'''
    SESSION_METHOD_PASSTHROUGH_CALL = ()
    '''Same as SESSION_METHOD_DECLARATION but without default values - For calling into Session using parameters of the same name and order that are simply passed through'''
    SESSION_INIT_DECLARATION = ()
    '''For declaring an init method in Session'''
    SESSION_NUMPY_INTO_METHOD_DECLARATION = ()
    '''For declaring a Session method that uses numpy arrays.'''
    INTERPRETER_NUMPY_INTO_METHOD_DECLARATION = ()
    '''For declaring a **Interpreter method that uses numpy arrays.'''
    INTERPRETER_NUMPY_INTO_METHOD_CALL = ()
    '''For calling into a **Interpreter method (from Session) that uses numpy arrays.'''
    SESSION_METHOD_CALL = ()
    '''For calling into a regular Session method.'''
    SESSION_INIT_CALL = ()
    '''For calling into an init Session method.'''
    DOCUMENTATION_SESSION_METHOD = ()
    '''For documentation (rst) of Session methods'''
    LIBRARY_METHOD_DECLARATION = ()
    '''For declaring a Library method.'''
    CDLL_METHOD_CALL = ()
    '''For calling into a CDLL method (from Library).'''
    LIBRARY_METHOD_CALL = ()
    '''For calling into a Library method (from LibraryInterpreter).'''
    INTERPRETER_METHOD_CALL = ()
    '''For calling into a **Interpreter method (from Session).'''
    GRPC_REQUEST_PARAMETERS = ()
    '''For creating a gRPC Request object.'''
    CTYPES_ARGTYPES = ()
    '''For setting up the ctypes argument types'''
    INTERPRETER_METHOD_DECLARATION = ()
    '''For declaring a **Interpreter method.'''
    INPUT_PARAMETERS = ()
    '''Get all input parameters, other than self, rep caps, and size'''
    LIBRARY_OUTPUT_PARAMETERS = ()
    '''Get all output parameters, other than ivi-dance'''
    API_OUTPUT_PARAMETERS = ()
    '''We also want to skip size parameters'''
    API_NUMPY_OUTPUT_PARAMETERS = ()
    '''Output parameters for numpy function'''
    GRPC_OUTPUT_PARAMETERS = ()
    '''Get all gRPC output parameters'''
    IVI_DANCE_PARAMETER = ()
    '''Get the ivi-dance parameter'''
    NUMPY_PARAMETERS = ()
    '''Get all buffer parameters that support numpy.array in the Python API'''
    LEN_PARAMETER = ()
    '''Get the len parameter'''
    INPUT_ENUM_PARAMETERS = ()
    '''Get any input parameters whose type is enum'''
    COMPLEX_NUMBER_PARAMETERS = ()
    '''Get all parameters of complex type'''
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/Makefile sha256=0bc5062b59b6f23b108992b9c0296193fcf43112aea0793e703febc14e7e0c46 bytes=6137 -->
## FILE: build/Makefile

- repository: `ni/nimi-python`
- source_path: `build/Makefile`
- sha256: `0bc5062b59b6f23b108992b9c0296193fcf43112aea0793e703febc14e7e0c46`
- bytes: 6137

````text
include $(BUILD_HELPER_DIR)/tools.mak

DEFAULT_TARGETS := module doc_files
export DEFAULT_TARGETS

GENERATED_DIR := $(ROOT_DIR)/generated
export GENERATED_DIR

COMMAND_LOG := $(ROOT_DIR)/commands.log
export COMMAND_LOG

DOCS_DIR := $(ROOT_DIR)/docs
export DOCS_DIR

STATIC_DOCS_DIR := $(DOCS_DIR)/_static
export STATIC_DOCS_DIR

ifeq (,$(PRINT))
_hide_cmds := @
endif

# We only add root files if we are building the 'all' target (nothing on the command line)
ifeq (,$(MAKECMDGOALS))
ROOT_FILES := \
	$(ROOT_DIR)/README.rst \

endif

all: $(DRIVERS) $(ROOT_FILES)

define per_driver_per_target
$1_$2: start
	@echo
	@echo "Making $1"
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1 $2
endef

define per_driver_all
$1: start
	@echo
	@echo "Making $1"
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1
endef

$(foreach d,$(ALL_DRIVERS),$(eval $(call per_driver_all,$(d))))
$(foreach d,$(ALL_DRIVERS),\
   $(foreach t,$(DEFAULT_TARGETS),\
      $(eval $(call per_driver_per_target,$(d),$(t)))))

define per_target
$1:
	$(foreach d,$(DRIVERS),make --no-print-directory -f src/$(d)/$(d).mak DRIVER=$(d) $1 &&)  echo
endef

$(foreach t,$(DEFAULT_TARGETS),$(eval $(call per_target,$(t))))

define per_driver_installers
$1_installers: start
	@echo
	@echo "Making $1 installers"
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -s -f src/$1/$1.mak DRIVER=$1 installers
endef

$(foreach d,$(ALL_DRIVERS),$(eval $(call per_driver_installers,$(d))))
installers: $(foreach d,$(ALL_DRIVERS), $(d)_installers)

SUPPRESS_ERROR_OUTPUT ?= 2> /dev/null

# We need to ensure generated exists for Travis CI builds
clean: start
	@echo 'Cleaning...'
	-$(_hide_cmds)rm -Rf $(GENERATED_DIR)/ $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)find $(ROOT_DIR)/build -path '*/__pycache__/*' -exec rm {} \; $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)find $(ROOT_DIR)/build -name __pycache__ -exec rmdir {} \; $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)find $(ROOT_DIR)/build -name '*.pyc' -exec rm {} \; $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)rm $(foreach d,$(DRIVERS), $(ROOT_DIR)/docs/$(d)/*) $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)rm $(foreach d,$(DRIVERS), $(ROOT_DIR)/docs/$(d)/.readthedocs.yaml) $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)rm -Rf $(ROOT_DIR)/.coverage $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)rm -Rf $(ROOT_DIR)/README.rst $(SUPPRESS_ERROR_OUTPUT) ||:
	-$(_hide_cmds)mkdir $(GENERATED_DIR) $(SUPPRESS_ERROR_OUTPUT) ||:

start:
	-@echo "# This is the list of commands that make invoked in order to build nimi-python. If" > $(COMMAND_LOG)
	-@echo "# you want to reproduce the build but don't have GNU Make setup in your system, you" >> $(COMMAND_LOG)
	-@echo "# can use the commands in this log file." >> $(COMMAND_LOG)


# From https://stackoverflow.com/questions/14760124/how-to-split-in-gnu-makefile-list-of-files-into-separate-lines
DRIVER_ALL_TARGETS_HELP := echo Drivers: $(addprefix  && echo - ,$(ALL_DRIVERS))
TARGETS_HELP := echo Targets: $(addprefix  && echo - ,$(DEFAULT_TARGETS))
PER_DRIVER_PER_TARGET := \
   $(foreach d,$(ALL_DRIVERS),\
      $(foreach t,$(DEFAULT_TARGETS),\
         $(d)_$(t)))
DRIVER_TARGETS_HELP := echo Per driver, per target: $(addprefix  && echo - ,$(PER_DRIVER_PER_TARGET))
help:
	@echo 'Supported targets:'
	@echo '* help'
	@echo '* clean'
	@echo '* print-<VARIABLE> (only top level variables)'
	@echo '* printvar VAR=<VARIABLE> (per driver print variable)'
	@echo ''
	@echo 'Any/multiple target(s) listed below:'
	@$(DRIVER_ALL_TARGETS_HELP)
	@echo ''
	@$(TARGETS_HELP)
	@echo ''
	@$(DRIVER_TARGETS_HELP)
	@echo ''

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $* is $(flavor $*) variable set to [$($*)]) @true

# Per driver variable printing
per_driver_variable_print = make --no-print-directory -f src/$1/$1.mak DRIVER=$1 print-$2
.PHONY:
printvar:
	$(_hide_cmds)$(foreach d,$(DRIVERS),$(call per_driver_variable_print,$(d),$(VAR)) && ) echo


PYTHON_CMD ?= python

.PHONY: help Makefile

# For the global files, instead of trying to keep track of which files from the driver builds matter for any target,
# we just say that if anything from any driver built, we will rebuld the global files
export DRIVER_FILE_BUILT = $(GENERATED_DIR)/driver_file_built

GLOBAL_FILES_STARTED_FILE = $(GENERATED_DIR)/printed_global_files
$(GLOBAL_FILES_STARTED_FILE): $(DRIVER_FILE_BUILT)
	@echo
	@echo "Making Global Files"
	@touch $(GLOBAL_FILES_STARTED_FILE)

# Executes a command, then logs it to $(COMMAND_LOG).
# $1 is the command.
# We need our own copy that does not touch DRIVER_FILE_BUILT
define global_log_command
	$1
	@echo '$1' >> $(COMMAND_LOG)
endef

$(ROOT_DIR)/README.rst: $(GLOBAL_FILES_STARTED_FILE)
	$(call trace_to_console, "Creating Root",$(notdir $@))
	$(_hide_cmds)$(call global_log_command,cat $(STATIC_DOCS_DIR)/status_project.inc \
                                               $(STATIC_DOCS_DIR)/about.inc \
                                               $(DOCS_DIR)/*/status.inc \
                                               $(STATIC_DOCS_DIR)/installation.inc \
                                               $(STATIC_DOCS_DIR)/contributing.inc \
                                               $(STATIC_DOCS_DIR)/nidmm_usage.inc \
                                               $(STATIC_DOCS_DIR)/support.inc \
                                               $(STATIC_DOCS_DIR)/documentation.inc \
                                               $(STATIC_DOCS_DIR)/license.inc > $@)

# Any step that any driver build does that would invalidate unit testing, flake8 or generated html
# needs to delete this file. This will trigger a tox run.
TOX_RUN_DONE := $(GENERATED_DIR)/tox_run_done
export TOX_RUN_DONE

test: $(TOX_RUN_DONE)

$(TOX_RUN_DONE):
	@echo
	$(call trace_to_console, "Running tox",$@)
	$(_hide_cmds)$(call make_with_tracking_file,$@,tox)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/rules.mak sha256=4639a6e362399ed0c219e437406d6b774cb30c7a0797ba8ccb23136a85471117 bytes=7897 -->
## FILE: build/rules.mak

- repository: `ni/nimi-python`
- source_path: `build/rules.mak`
- sha256: `4639a6e362399ed0c219e437406d6b774cb30c7a0797ba8ccb23136a85471117`
- bytes: 7897

````makefile

include $(BUILD_HELPER_DIR)/tools.mak

README := $(OUTPUT_DIR)/README.rst
SETUP := $(OUTPUT_DIR)/setup.py
TOX_INI := $(OUTPUT_DIR)/tox-system_tests.ini

MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_COPY)) \
                $(addprefix $(MODULE_DIR)/,$(CUSTOM_TYPES_TO_COPY)) \
                $(README) \
                $(SETUP) \
                $(TOX_INI) \

RST_FILES := \
                $(addprefix $(DRIVER_DOCS_DIR)/,$(RST_FILES_TO_GENERATE)) \

EXAMPLE_FILES := $(if $(wildcard src/$(DRIVER)/examples/*),$(shell find src/$(DRIVER)/examples/* -type f -print),)

# If there are any examples, we will need to build the examples zip file for this driver
ifneq (,$(EXAMPLE_FILES))

EXAMPLES_DIR := $(GENERATED_DIR)/examples
MKDIRECTORIES += $(EXAMPLES_DIR)
DRIVER_EXAMPLES_ZIP_FILE := $(EXAMPLES_DIR)/$(DRIVER)_examples.zip
MODULE_FILES += $(DRIVER_EXAMPLES_ZIP_FILE)

endif # ifneq (,$(EXAMPLE_FILES))

MKDIR: $(MKDIRECTORIES)

define mkdir_rule
$1:
	$(call trace_to_console, "Making dir",$1)
	$(_hide_cmds)$(call log_command,mkdir -p $1)
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

# We set up some additional dependencies for specific files
# examples.rst needs to use find since there may be folders of files and it needs to be recursive. wildcard is not recursive
$(MODULE_DIR)/session.py: $(wildcard $(TEMPLATE_DIR)/session.py/*.mako) $(wildcard $(DRIVER_DIR)/templates/session.py/*.mako)
$(MODULE_DIR)/_grpc_stub_interpreter.py: $(wildcard $(TEMPLATE_DIR)/_grpc_stub_interpreter.py/*.mako) $(wildcard $(DRIVER_DIR)/templates/_grpc_stub_interpreter.py/*.mako)
$(MODULE_DIR)/_library_interpreter.py: $(wildcard $(TEMPLATE_DIR)/_library_interpreter.py/*.mako) $(wildcard $(DRIVER_DIR)/templates/_library_interpreter.py/*.mako)
$(DRIVER_DOCS_DIR)/class.rst: $(wildcard $(TEMPLATE_DIR)/functions.rst/*.mako) $(wildcard $(DRIVER_DIR)/templates/functions.rst/*.mako)
$(DRIVER_DOCS_DIR)/examples.rst: $(EXAMPLE_FILES) $(MODULE_DIR)/VERSION

$(MODULE_DIR)/%.py: %.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/unit_tests/%.py: %.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%: %.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%_pb2.py: %.proto
	$(call trace_to_console, "Generating",$@ and $(notdir $*)_pb2_grpc.py)
	$(_hide_cmds)$(call log_command,python -m grpc_tools.protoc $(addprefix -I=,$(PROTO_DIRS)) --python_out=$(MODULE_DIR) --grpc_python_out=$(MODULE_DIR) $*.proto)
	$(_hide_cmds)$(call log_command,sed -i 's/^import nidevice_pb2/from . import nidevice_pb2/' $(MODULE_DIR)/$*_pb2*.py)
	$(_hide_cmds)$(call log_command,sed -i 's/^import $(notdir $*)_pb2/from . import $(notdir $*)_pb2/' $(MODULE_DIR)/$*_pb2*.py)

vpath %.proto $(PROTO_DIRS)

$(MODULE_DIR)/%_pb2_grpc.py: $(MODULE_DIR)/%_pb2.py

$(MODULE_DIR)/%.py: %.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)cp $< $@

$(MODULE_DIR)/%.py: $(DRIVER_DIR)/custom_types/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)cp $< $@

$(DRIVER_DOCS_DIR)/%.rst: %.rst.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_DOCS_DIR)/$(DRIVER).rst: driver.rst.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR), $(notdir $@)))

$(DRIVER_DOCS_DIR)/%.inc: %.inc.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_DOCS_DIR)/about_$(DRIVER).inc: about_driver.inc.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR), $(notdir $@)))

$(SPHINX_CONF_PY): $(TEMPLATE_DIR)/conf.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(READTHEDOCS_CONFIG): $(TEMPLATE_DIR)/.readthedocs.yaml.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_EXAMPLES_ZIP_FILE): $(EXAMPLE_FILES)
	$(call trace_to_console, "Zipping",$@)
	$(_hide_cmds)$(call log_command,cd src/$(DRIVER)/examples && zip -u -r -9 $@ * || ([ $$? -eq 12 ] && exit 0) || exit)

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/unit_tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/unit_tests/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

clean:

.PHONY: module doc_files sdist wheel installers
module: $(MODULE_FILES) $(UNIT_TEST_FILES)
doc_files: $(RST_FILES) $(SPHINX_CONF_PY) $(READTHEDOCS_CONFIG)
installers: sdist wheel

$(UNIT_TEST_FILES): $(MODULE_FILES)

$(SETUP): $(TEMPLATE_DIR)/setup.py.mako $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(TOX_INI): $(TEMPLATE_DIR)/tox-system_tests.ini.mako $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

sdist wheel: $(SDIST_WHEEL_BUILD_DONE)

$(SDIST_WHEEL_BUILD_DONE): # codegen should have already run or just use what is in git
	$(call trace_to_console, "Creating sdist and wheel",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command_no_tracking,cd $(OUTPUT_DIR) && $(PYTHON_CMD) -m build $(LOG_OUTPUT) $(LOG_DIR)/sdist_wheel.log)
	$(_hide_cmds)$(call log_command_no_tracking,touch $@)

# If we are building nifake, we just need a placeholder file for inclusion into the wheel that will never be used. We can't build the actual readme since not all the files are created
ifeq (nifake,$(DRIVER))
$(README):
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $(ROOT_DIR)/LICENSE $@)

else
# We piece together the readme files instead of relying on the rst include directive because we need these files to be standalone and not require any additional files that are in specific locations.
$(README): $(RST_FILES) $(wildcard $(STATIC_DOCS_DIR)/*)
	$(call trace_to_console, "Creating",$@)
	$(_hide_cmds)$(call log_command,cat $(STATIC_DOCS_DIR)/status_project.inc \
                                        $(DRIVER_DOCS_DIR)/about_$(DRIVER).inc \
                                        $(DRIVER_DOCS_DIR)/status.inc \
                                        $(DRIVER_DOCS_DIR)/installation.inc \
                                        $(STATIC_DOCS_DIR)/contributing.inc \
                                        $(STATIC_DOCS_DIR)/$(DRIVER)_usage.inc \
                                        $(STATIC_DOCS_DIR)/support.inc \
                                        $(STATIC_DOCS_DIR)/$(DRIVER)_documentation.inc \
                                        $(STATIC_DOCS_DIR)/license.inc > $@)

endif

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/.readthedocs.yaml.mako sha256=9b7d3d9ad8eaff37a218fde28c6d76ceed84a2f45fbe0ad22601c0140fa151ff bytes=2420 -->
## FILE: build/templates/.readthedocs.yaml.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/.readthedocs.yaml.mako`
- sha256: `9b7d3d9ad8eaff37a218fde28c6d76ceed84a2f45fbe0ad22601c0140fa151ff`
- bytes: 2420

````mako
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
<%
    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    # All of the files used to configure and build docs and readthedocs are in these 2 folders
    build_trigger_paths = f'docs/_static/ docs/{module_name}/'
    conf_py_path = f'docs/{module_name}/conf.py'
%>\

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: ${build_trigger_paths}.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- ${build_trigger_paths};
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: ${conf_py_path}

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
## TODO(ni-jfitzger): Create requirements file for docs to make builds reproducible. See https://github.com/ni/nimi-python/issues/1968
## Note: Our nimi-python readthedocs project used the defaults here: https://docs.readthedocs.io/en/stable/build-default-versions.html#external-dependencies
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/__init__.py.mako sha256=103c4b1acd542105fac13f878c884eca284c961db1276339d1ffd7bc3481b0e4 bytes=5303 -->
## FILE: build/templates/__init__.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/__init__.py.mako`
- sha256: `103c4b1acd542105fac13f878c884eca284c961db1276339d1ffd7bc3481b0e4`
- bytes: 5303

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

enums = template_parameters['metadata'].enums
functions = helper.filter_codegen_functions(template_parameters['metadata'].functions)
config = template_parameters['metadata'].config
grpc_supported = template_parameters['include_grpc_support']
module_name = config['module_name']
registry_name = config['driver_registry'] if 'driver_registry' in config else config['driver_name']
%>

__version__ = '${config['module_version']}'

% if len(enums) > 0:
from ${module_name}.enums import *  # noqa: F403,F401,H303
% endif
from ${module_name}.errors import DriverWarning  # noqa: F401
from ${module_name}.errors import Error  # noqa: F401
% if grpc_supported:
from ${module_name}.grpc_session_options import *  # noqa: F403,F401,H303
% endif
<%
# nitclk is different. It does not have a Session class that we open a session on
# Instead it is a bunch of stateless function calls. So if we are NOT building for
# nitclk, we import the Session class. If it is nitclk then we will
# import each function and the SessionReference class
%>\
% if config['module_name'] == 'nitclk':
from ${module_name}.session import SessionReference  # noqa: F401

# Function imports
<%
# There two types of functions in `nitclk`:
#
# 1. Functions that take a single SessionReference (get/set attribute)
# 2. Functions that take in a list of SessionReference
#
# The second type are the public functions that clients will call, so we need to import them explicitly into
# the `nitclk` namespace. We are using the `render_in_session_base` metadata in order to distinguish them
%>\
%   for func_name in sorted([functions[k]['python_name'] for k in functions if not functions[k]['render_in_session_base']]):
from ${module_name}.session import ${func_name}  # noqa: F401
%   endfor
% else:
from ${module_name}.session import Session  # noqa: F401
% endif
<%
 # Blank lines are to make each import separate so that they do not need to be sorted
 # Otherwise flake8 test fails
%>\
% for c in config['custom_types']:
% if c['python_name']:

from ${module_name}.${c['file_name']} import ${c['python_name']}  # noqa: F401
% endif
% if c['ctypes_type']:

from ${module_name}.${c['file_name']} import ${c['ctypes_type']}  # noqa: F401
% endif
% endfor


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import importlib.metadata
    import os
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\${registry_name}\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages_names = [
        name
        for name_list in importlib.metadata.packages_distributions().values()
        for name in name_list
    ]
    installed_packages_names = set(installed_packages_names)
    installed_packages_list = [
        {'name': name, 'version': importlib.metadata.distribution(name).version}
        for name in sorted(installed_packages_names)
    ]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "${config['driver_name']}"
    info['driver']['version'] = driver_version
    info['module']['name'] = '${module_name}'
    info['module']['version'] = "${config['module_version']}"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_attributes.py.mako sha256=110f7e6efd7f9dae39053ebf63677369df3c551dfd3aab4b23e518e812591333 bytes=6353 -->
## FILE: build/templates/_attributes.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_attributes.py.mako`
- sha256: `110f7e6efd7f9dae39053ebf63677369df3c551dfd3aab4b23e518e812591333`
- bytes: 6353

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
    module_name = template_parameters['metadata'].config['module_name']
    config = template_parameters['metadata'].config
%>\
import ${module_name}._converters as _converters
import ${module_name}.errors as errors

import hightime


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds_int32(value))


class AttributeViInt32TimeDeltaMonths(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_month_to_timedelta(session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_months_int32(value))


class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds_real64(value))


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


class AttributeViStringRepeatedCapability(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_repeated_capabilities_without_prefix(value))


class AttributeViStringCommaSeparated(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_comma_separated_string_to_list(session._get_attribute_vi_string(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_list_to_comma_separated_string(value))


class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


class AttributeEnum(Attribute):

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        super(AttributeEnum, self).__init__(attribute_id)
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class

    def __get__(self, session, session_type):
        return self._attribute_type(self._underlying_attribute.__get__(session, session_type))

    def __set__(self, session, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


class AttributeEnumWithConverter(Attribute):
    '''Class for attributes that use enums internally but are exposed in the ${module_name} Python module as something else, thus need conversion.'''

    def __init__(self, underlying_attribute_enum, getter_converter, setter_converter):
        '''Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        '''
        super(AttributeEnumWithConverter, self).__init__(underlying_attribute_enum._attribute_id)
        self._underlying_attribute_enum = underlying_attribute_enum
        self._getter_converter = getter_converter
        self._setter_converter = setter_converter

    def __get__(self, session, session_type):
        try:
            return self._getter_converter(
                self._underlying_attribute_enum.__get__(session, session_type)
            )
        except (KeyError, ValueError):
            raise errors.DriverTooNewError()

    def __set__(self, session, value):
        try:
            return self._underlying_attribute_enum.__set__(session, self._setter_converter(value))
        except KeyError:
            raise ValueError(f'Invalid value: {value}')


# nitclk specific attribute type
class AttributeSessionReference(Attribute):

    def __get__(self, session, session_type):
        # Import here to avoid a circular dependency when initial import happens
        from ${module_name}.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_complextype.py.mako sha256=2ab119fa4171198fff245536a5b0a98de8323eb5c69dea0d405790e35d987eda bytes=612 -->
## FILE: build/templates/_complextype.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_complextype.py.mako`
- sha256: `2ab119fa4171198fff245536a5b0a98de8323eb5c69dea0d405790e35d987eda`
- bytes: 612

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper
    config = template_parameters['metadata'].config
    module_name = config['module_name']
%>\
import ctypes
import ${module_name}._visatype as _visatype


class NIComplexNumber(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class NIComplexNumberF32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class NIComplexI16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_converters.py.mako sha256=02413cb3271984fc4fe7019f50e1ffce8734c5d99faa562a0b723aeb3dec1d53 bytes=16949 -->
## FILE: build/templates/_converters.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_converters.py.mako`
- sha256: `02413cb3271984fc4fe7019f50e1ffce8734c5d99faa562a0b723aeb3dec1d53`
- bytes: 16949

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper
    config = template_parameters['metadata'].config
    module_name = config['module_name']
    extra_errors_used = config['extra_errors_used']
    enums = config['enums']
%>\
import ${module_name}._visatype as _visatype
% if any(helper.enum_uses_converter(enums[enum_name]) for enum_name in helper.filter_codegen_enums(enums)):
import ${module_name}.enums as enums
% endif
import ${module_name}.errors as errors

import array
import collections
import hightime
import numbers

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        try:
            start = int(rc[0])
            end = int(rc[1])
        except ValueError:
            # This exception is raised when repeated_capability is of the form "dev/0-1". rc[0] == "dev/0" in this case.
            # Just return the repeated_capability string as-is in that case.
            pass
        else:
            if end < start:
                rng = range(start, end - 1, -1)
            else:
                rng = range(start, end + 1)
            return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def expand_channel_string(channel_string, all_channels_in_session):
    '''Expands a channel_string to a list of individual channel names.

    The individual channel names may or may not be fully qualified channel names as applicable for
    the session. In other words, the individual channel names will be a subset of
    all_channels_in_session.

    Examples:
        - expand_channel_string('1', ['0', '1', '2', '3']) --> ['1']
        - expand_channel_string('4,1:2', ['1', '2', '4']) --> ['4', '1', '2']
        - expand_channel_string('2:3,0', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/2', 'Dev1/3', 'Dev1/0']
        - expand_channel_string('Dev1/1', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/1']
        - expand_channel_string('4,Dev1/1:2', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/1', 'Dev1/2']
        - expand_channel_string('Dev1/4,Dev1/2,Dev1/3', ['Dev1/2', 'Dev1/3', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/2', 'Dev1/3']
        - expand_channel_string('Dev1/1,Dev2/2', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3'])
            --> ['Dev1/1', 'Dev2/2']
        - expand_channel_string(' Dev1 / 1 : 2 , 4 ', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/1', 'Dev1/2', 'Dev1/4']
        - expand_channel_string('DEV1/0-1    , Dev1/3', ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3'])
            --> ['dev1/0', 'dev1/1', 'dev1/3']

    Args:
        channel_string (str) - refer to _convert_repeated_capabilities() for the
            supported formats (this string is expected to be used as the index of session.channels)

        all_channels_in_session (list of str) - names of all the channels in the session as returned
            by get_channel_names()

    Returns:
        channel_names (list of str) - A list in which each element is the name of a single channel,
            with the exact capitalization used by the driver runtime.
    '''
    if channel_string.strip() == '':
        return all_channels_in_session

    # Rule 1: If all_channels_in_session is fully-qualified then returned channel names should be
    #         fully-qualified, otherwise returned channel names should not be fully-qualified.
    # Rule 2: If any channel in the input is not fully-qualified, but we need to return
    #         fully-qualified channels because of Rule 1, then use the channel qualifier obtained
    #         from all_channels_in_session. This can only happen on a single-instrument session,
    #         so all the channel qualifiers are the same and we pick the first one.

    instrument, separator, channel = all_channels_in_session[0].rpartition('/')
    default_channel_qualifier = instrument + separator

    expanded_channel_list = []
    for token in channel_string.split(','):
        instrument, separator, channel = token.rpartition('/')
        instrument = instrument.strip()
        channel_qualifier = instrument + separator if instrument else default_channel_qualifier
        expanded_channel_list.extend(
            convert_repeated_capabilities(channel.strip(), channel_qualifier)
        )

    # Convert the expanded channel names to their canonical form based on all_channels_in_session
    lowercase_channel_name_to_session_channel_name_dict = {
        channel_name.lower(): channel_name for channel_name in all_channels_in_session
    }
    return [
        lowercase_channel_name_to_session_channel_name_dict[channel_name.lower()]
        for channel_name in expanded_channel_list
    ]


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return scaled_value


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# Scaling factor to apply on seconds to get months
# would be 1/(60 seconds * 60 minutes * 24 hours * 30.4167 days)
def convert_timedelta_to_months_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1.0 / (60 * 60 * 24 * 30.4167))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_list_to_comma_separated_string(list_of_strings):
    '''Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    '''
    if not isinstance(list_of_strings, (list, tuple)) or not all(isinstance(item, str) for item in list_of_strings):
        raise TypeError('Input must be a list or tuple of str')
    return ','.join(list_of_strings)


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]


<%
# Beginning of module-specific converters
%>\
<%
# nitclk is different. Only nitclk needs to be able to convert sessions like this
%>\
% if config['module_name'] == 'nitclk':
# nitclk specific converters
def convert_to_nitclk_session_number(item):
    '''Convert from supported objects to NI-TClk Session Num

    Supported objects are:
    - class with .tclk object of type nitclk.SessionReference
    - nitclk.SessionReference
    '''
    try:
        return item.tclk._get_tclk_session_reference()
    except AttributeError:
        pass

    try:
        return item._get_tclk_session_reference()
    except AttributeError:
        pass

    raise TypeError('Unsupported type for nitclk session: {}'.format(type(item)))


def convert_to_nitclk_session_number_list(item_list):
    '''Converts a list of items to nitclk session nums'''
    return [convert_to_nitclk_session_number(i) for i in item_list]


% endif
<%
# This converter is only needed for nifake testing
%>\
% if config['module_name'] == 'nifake':
# nifake specific converter(s) - used only for testing
def convert_double_each_element(numbers):
    return [x * 2 for x in numbers]


% endif
% for enum_name in sorted(helper.filter_codegen_enums(enums)):
    % if helper.enum_uses_converter(enums[enum_name]):
def ${enums[enum_name]['enum_to_converted_value_function_name']}(value):
    return {
        % for enum_value in enums[enum_name]['values']:
        enums.${enums[enum_name]['python_name']}.${enum_value['python_name']}: ${helper.get_enum_value_snippet(enum_value['converts_to_value'])},
        % endfor
    }[value]


def ${enums[enum_name]['converted_value_to_enum_function_name']}(value):
    return {
    % for enum_value in enums[enum_name]['values']:
        ${helper.get_enum_value_snippet(enum_value['converts_to_value'])}: enums.${enums[enum_name]['python_name']}.${enum_value['python_name']},
    % endfor
    }[value]


    % endif
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/default_method.py.mako sha256=4a10659ee4388c5d5e69afc1e57600243c33421075817597f6cdb85a8a1a1085 bytes=1231 -->
## FILE: build/templates/_grpc_stub_interpreter.py/default_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/default_method.py.mako`
- sha256: `4a10659ee4388c5d5e69afc1e57600243c33421075817597f6cdb85a8a1a1085`
- bytes: 1231

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method corresponding to the passed-in function metadata.'''
    import build.helper as helper
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
    included_in_proto = f.get('included_in_proto', True)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if included_in_proto:
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
% if return_statement:
        ${return_statement}
% endif
% else:
        raise NotImplementedError('${full_func_name} is not supported over gRPC')
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/initialization_method.py.mako sha256=b34003a93912a7df5e326a63a99c48f60f8cb87d57651302a2058744923a1a6a bytes=1380 -->
## FILE: build/templates/_grpc_stub_interpreter.py/initialization_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/initialization_method.py.mako`
- sha256: `b34003a93912a7df5e326a63a99c48f60f8cb87d57651302a2058744923a1a6a`
- bytes: 1380

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter initialization method, adding proto-specific fields to the passed-in function metadata.'''

    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
% if return_statement:
        ${return_statement}
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/lock.py.mako sha256=f7a7ef4584316eb2f6324459f5350ff9c345583b803b7e3cc23236ce07f94611 bytes=431 -->
## FILE: build/templates/_grpc_stub_interpreter.py/lock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/lock.py.mako`
- sha256: `f7a7ef4584316eb2f6324459f5350ff9c345583b803b7e3cc23236ce07f94611`
- bytes: 431

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        self._lock.acquire()
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/numpy_read_method.py.mako sha256=9aebbb1bb353f49c238b67e7ca7efb265c5bbd86ff9cbe4b27d6acb80d5ca521 bytes=569 -->
## FILE: build/templates/_grpc_stub_interpreter.py/numpy_read_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/numpy_read_method.py.mako`
- sha256: `9aebbb1bb353f49c238b67e7ca7efb265c5bbd86ff9cbe4b27d6acb80d5ca521`
- bytes: 569

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a NotImplemented method for to the passed-in function metadata, because numpy is not supported over grpc.'''

    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/numpy_write_method.py.mako sha256=8f0fc56c8d42a23a4945a53d09c2556fde07c5f6a3611c32cb445280369acb0f bytes=2863 -->
## FILE: build/templates/_grpc_stub_interpreter.py/numpy_write_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/numpy_write_method.py.mako`
- sha256: `8f0fc56c8d42a23a4945a53d09c2556fde07c5f6a3611c32cb445280369acb0f`
- bytes: 2863

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for numpy write operations with complex number support.'''
    
    import build.helper as helper
    
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
    grpc_request_args = helper.get_params_snippet(f, helper.ParameterUsageOptions.GRPC_REQUEST_PARAMETERS)
    return_statement = helper.get_grpc_interpreter_method_return_snippet(f['parameters'], config)
    if return_statement == 'return':
        return_statement = None
    capture_response = 'response = ' if return_statement else ''
    included_in_proto = f.get('included_in_proto', True)
    numpy_complex_params = helper.filter_parameters(f['parameters'], helper.ParameterUsageOptions.COMPLEX_NUMBER_PARAMETERS)
    for param in numpy_complex_params:
        grpc_request_args = grpc_request_args.replace(
            param['grpc_name'] + '=' + param['python_name'],
            param['grpc_name'] + '=' + param['python_name'] + '_list'
        )
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
% if included_in_proto:
%   if numpy_complex_params:
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
%     for param in numpy_complex_params:
%       if param['original_type'] == 'NIComplexNumber[]':
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in ${param['python_name']}.ravel()
        ]
%       elif param['original_type'] == 'NIComplexNumberF32[]':
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in ${param['python_name']}.ravel()
        ]
%       elif param['original_type'] == 'NIComplexI16[]':
        arr = ${param['python_name']}.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        ${param['python_name']}_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
%       endif
%     endfor
        ${capture_response}self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(${grpc_request_args}),
        )
%     if return_statement:
        ${return_statement}
%     endif
%   else:
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')
%   endif
% else:
        raise NotImplementedError('${full_func_name} is not supported over gRPC')
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py/unlock.py.mako sha256=0fbab10c6a834df058c0e3d654f32bae00b3fa3ef833644dfd2df25ba5e09eb2 bytes=431 -->
## FILE: build/templates/_grpc_stub_interpreter.py/unlock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py/unlock.py.mako`
- sha256: `0fbab10c6a834df058c0e3d654f32bae00b3fa3ef833644dfd2df25ba5e09eb2`
- bytes: 431

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        self._lock.release()
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_grpc_stub_interpreter.py.mako sha256=59252878e1218e6fe812b0ae053eb6729d1b9f8f6012c0a4d8428cc3a32ae3ed bytes=3874 -->
## FILE: build/templates/_grpc_stub_interpreter.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_grpc_stub_interpreter.py.mako`
- sha256: `59252878e1218e6fe812b0ae053eb6729d1b9f8f6012c0a4d8428cc3a32ae3ed`
- bytes: 3874

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
module_name = config['module_name']
proto_name = config.get('proto_name', module_name)
service_class_prefix = config['grpc_service_class_prefix']
functions = helper.filter_codegen_functions(config['functions'])
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>\

import grpc
import hightime  # noqa: F401
import session_pb2 as session_grpc_types
import threading
import warnings

% if config['enums']:
from . import enums as enums  # noqa: F401
% endif
from . import errors as errors
% if are_complex_parameters_used:
from . import nidevice_pb2 as grpc_complex_types  # noqa: F401
% endif
from . import ${proto_name}_pb2 as grpc_types
from . import ${proto_name}_pb2_grpc as ${module_name}_grpc
% for c in config['custom_types']:

from . import ${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = ${module_name}_grpc.${service_class_prefix}Stub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._${config['session_handle_parameter_name']} = value

    def get_session_handle(self):
        return self._${config['session_handle_parameter_name']}

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
% if method_template['library_interpreter_filename'] != '/none':
<%include file="${'/_grpc_stub_interpreter.py' + method_template['library_interpreter_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library.py.mako sha256=23dbc92c8e1755ff5df16d3f2b13091cf950dada9189059710f102ce529c71a6 bytes=2419 -->
## FILE: build/templates/_library.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library.py.mako`
- sha256: `23dbc92c8e1755ff5df16d3f2b13091cf950dada9189059710f102ce529c71a6`
- bytes: 2419

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
attributes = config['attributes']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = config['functions']
functions = helper.filter_library_functions(functions)
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>\

import ctypes
import ${module_name}.errors as errors
import threading

% if are_complex_parameters_used:
from ${module_name}._complextype import *  # noqa: F403
% endif
from ${module_name}._visatype import *  # noqa: F403,H303
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
% for func_name in sorted(functions):
        self.${c_function_prefix}${func_name}_cfunc = None
% endfor

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    c_func_name = c_function_prefix + func_name
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CDLL_METHOD_CALL)
    param_ctypes_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.CTYPES_ARGTYPES)
%>\

    def ${c_func_name}(${param_names_method}):  # noqa: N802
        with self._func_lock:
            if self.${c_func_name}_cfunc is None:
                self.${c_func_name}_cfunc = self._get_library_function('${c_func_name}')
                self.${c_func_name}_cfunc.argtypes = [${param_ctypes_library}]  # noqa: F405
                self.${c_func_name}_cfunc.restype = ${f['returns']}  # noqa: F405
        return self.${c_func_name}_cfunc(${param_names_library})
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/_get_error_description.py.mako sha256=22faf50a29c0f71b360c19f8c1104ad7b9393a1c571fc119a3f02277b29ff503 bytes=2048 -->
## FILE: build/templates/_library_interpreter.py/_get_error_description.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/_get_error_description.py.mako`
- sha256: `22faf50a29c0f71b360c19f8c1104ad7b9393a1c571fc119a3f02277b29ff503`
- bytes: 2048

````mako
<%page args="config"/>\
<%
    import build.helper as helper

    get_error_func = config['functions']['GetError']
    get_error_params = helper.filter_parameters(get_error_func['parameters'], helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)
    assert all(p.get('default_value') for p in get_error_params), [[p['name'], p.get('default_value')] for p in get_error_params]
    get_error_params_snippet = ", ".join(str(p['default_value']) for p in get_error_params)
%>\
    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error(${get_error_params_snippet})
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass
% if 'error_message' in config['functions']:

        try:
            # get_error reads the session's error queue, which may have been overwritten,
            # causing it to return a mismatched error code. error_message takes the error
            # code directly as a parameter and looks up its description without reading the
            # queue, it will return the description for the specific error code.
            # Use error_message in current session before the handle reset in the next block.

            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass

        save_vi = self.get_session_handle()
        try:
            # It is expected for get_error to raise when the session is invalid
            # (IVI spec requires GetError to fail).
            # Use error_message instead. It doesn't require a session.

            self.set_session_handle()
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        finally:
            self.set_session_handle(save_vi)
% endif
        return "Failed to retrieve error description."
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/default_method.py.mako sha256=7467c1396968e21102f417958c9c8aa4bd1a478a7a33ceb4ecf79d2404903b30 bytes=2379 -->
## FILE: build/templates/_library_interpreter.py/default_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/default_method.py.mako`
- sha256: `7467c1396968e21102f417958c9c8aa4bd1a478a7a33ceb4ecf79d2404903b30`
- bytes: 2379

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)

    ivi_dance_parameters = helper.filter_ivi_dance_parameters(parameters)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameters, parameters)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']

    # If a method uses codegen_method=python-only, it should specify non-default method_templates
    assert f['codegen_method'] != 'python-only', full_func_name + ' uses default_method method_template, but is python-only!'
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
<% ivi_dance_step = helper.IviDanceStep.QUERY_SIZE if (p in ivi_dance_parameters or p == ivi_dance_size_parameter) else helper.IviDanceStep.NOT_APPLICABLE %>\
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
% endfor
% if len(ivi_dance_parameters) > 0:
<% ivi_dance_step = helper.IviDanceStep.GET_DATA %>\
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
%   for declaration in helper.get_ctype_variable_declaration_snippet(ivi_dance_size_parameter, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
%   for param in ivi_dance_parameters:
%       for declaration in helper.get_ctype_variable_declaration_snippet(param, parameters, ivi_dance_step, config):
        ${declaration}
%       endfor
%   endfor
% endif
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_library_interpreter_method_return_snippet(parameters, config)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/initialization_method.py.mako sha256=e89475d4ae5a6c748821f957670e9c2ffc719e475233d508945308c4bbea4b11 bytes=2523 -->
## FILE: build/templates/_library_interpreter.py/initialization_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/initialization_method.py.mako`
- sha256: `e89475d4ae5a6c748821f957670e9c2ffc719e475233d508945308c4bbea4b11`
- bytes: 2523

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter initialization method, specifying the session should be closed on exit.'''

    import build.helper as helper

    grpc_supported = template_parameters['include_grpc_support']
    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)

    ivi_dance_parameters = helper.filter_ivi_dance_parameters(parameters)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameters, parameters)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']

    # If a method uses codegen_method=python-only, it should specify non-default method_templates
    assert f['codegen_method'] != 'python-only', full_func_name + ' uses default_method method_template, but is python-only!'
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
<% ivi_dance_step = helper.IviDanceStep.QUERY_SIZE if (p in ivi_dance_parameters or p == ivi_dance_size_parameter) else helper.IviDanceStep.NOT_APPLICABLE %>\
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
% endfor
% if len(ivi_dance_parameters) > 0:
<% ivi_dance_step = helper.IviDanceStep.GET_DATA %>\
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=${f['is_error_handling']})
%   for declaration in helper.get_ctype_variable_declaration_snippet(ivi_dance_size_parameter, parameters, ivi_dance_step, config):
        ${declaration}
%   endfor
%   for param in ivi_dance_parameters:
%       for declaration in helper.get_ctype_variable_declaration_snippet(param, parameters, ivi_dance_step, config):
        ${declaration}
%       endfor
%   endfor
% endif
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
% if grpc_supported:
        self._close_on_exit = True
% endif
        ${helper.get_library_interpreter_method_return_snippet(parameters, config)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/lock.py.mako sha256=0c759508dc3972132f008f6f299fbc8aae8c0d7326e1575f1038d882e636b6e3 bytes=839 -->
## FILE: build/templates/_library_interpreter.py/lock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/lock.py.mako`
- sha256: `0c759508dc3972132f008f6f299fbc8aae8c0d7326e1575f1038d882e636b6e3`
- bytes: 839

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter lock method.
    
    The Session class doesn't keep track of the callerHasLock pointer,
    so we should just pass None.
    '''

    import build.helper as helper

    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.${c_func_name}(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        return
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/numpy_read_method.py.mako sha256=1e1b60858a68d4073264ff114445a883239771cedad437e9c03ada3a1d13995c bytes=1566 -->
## FILE: build/templates/_library_interpreter.py/numpy_read_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/numpy_read_method.py.mako`
- sha256: `1e1b60858a68d4073264ff114445a883239771cedad437e9c03ada3a1d13995c`
- bytes: 1566

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter method for reading into a numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
<% size_param = helper.find_size_parameter(p, parameters) if p['size']['mechanism'] == 'passed-in' else None %>\
%   if size_param:
        ${size_param['python_name']} = len(${p['python_name']})
%   endif
% endfor
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, None, config, use_numpy_array=p['numpy']):
        ${declaration}
%   endfor
% endfor
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=True)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/numpy_write_method.py.mako sha256=a25f3e9b11cb854ed420b056f0abebe8c3949464586ebdb855b8dffe63fd342b bytes=1237 -->
## FILE: build/templates/_library_interpreter.py/numpy_write_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/numpy_write_method.py.mako`
- sha256: `a25f3e9b11cb854ed420b056f0abebe8c3949464586ebdb855b8dffe63fd342b`
- bytes: 1237

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter method for writing numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
%   for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, None, config, use_numpy_array=p['numpy']):
        ${declaration}
%   endfor
% endfor
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=True)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py/unlock.py.mako sha256=8b3c14b58bf5af0ffaf579ecb10383b4e32c876deffd01a9b742893ae8e451f1 bytes=837 -->
## FILE: build/templates/_library_interpreter.py/unlock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py/unlock.py.mako`
- sha256: `8b3c14b58bf5af0ffaf579ecb10383b4e32c876deffd01a9b742893ae8e451f1`
- bytes: 837

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a LibraryInterpreter unlock method.

    The Session class doesn't keep track of the callerHasLock pointer,
    so we should just pass None.
    '''

    import build.helper as helper

    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.${c_func_name}(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        return
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_interpreter.py.mako sha256=44b2b3f4b1d4ad59a37e869a5e266abb5518c3372da369af83af21b339f266f2 bytes=5021 -->
## FILE: build/templates/_library_interpreter.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_interpreter.py.mako`
- sha256: `44b2b3f4b1d4ad59a37e869a5e266abb5518c3372da369af83af21b339f266f2`
- bytes: 5021

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config = template_parameters['metadata'].config
attributes = config['attributes']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = config['functions']
functions = helper.filter_codegen_functions(functions)
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>\

import array
import ctypes
import hightime  # noqa: F401
% if 'SetRuntimeEnvironment' in functions:
import platform

% endif
% if are_complex_parameters_used:
import ${module_name}._complextype as _complextype
% endif
import ${module_name}._library_singleton as _library_singleton
import ${module_name}._visatype as _visatype
% if config['enums']:
import ${module_name}.enums as enums  # noqa: F401
% endif
import ${module_name}.errors as errors
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor


% if 'SetRuntimeEnvironment' in functions:
_was_runtime_environment_set = None


% endif
# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        % if are_complex_parameters_used:
        if library_type in (_complextype.NIComplexI16, _complextype.NIComplexNumberF32, _complextype.NIComplexNumber):
            complex_dtype = numpy.dtype(library_type)
            if value.ndim > 1:
                # we create a flattened view of the multi-dimensional numpy array
                restructured_array_view = value.ravel().view(complex_dtype)
            else:
                restructured_array_view = value.view(complex_dtype)
            return restructured_array_view.ctypes.data_as(ctypes.POINTER(library_type))
        else:
            return numpy.ctypeslib.as_ctypes(value)
        % else:
        return numpy.ctypeslib.as_ctypes(value)
        % endif
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        % if 'SetRuntimeEnvironment' in functions:
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        % endif
        # Initialize _${config['session_handle_parameter_name']} to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._${config['session_handle_parameter_name']} = value

    def get_session_handle(self):
        return self._${config['session_handle_parameter_name']}

<%include file="/_library_interpreter.py/_get_error_description.py.mako" args="config=config" />\
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
% if method_template['library_interpreter_filename'] != '/none':
<%include file="${'/_library_interpreter.py' + method_template['library_interpreter_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_library_singleton.py.mako sha256=ee20795584c3f8cb853d0f0714fe26d4e3d2b0b2db26643ba595c1ba98ebccaf bytes=1717 -->
## FILE: build/templates/_library_singleton.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_library_singleton.py.mako`
- sha256: `ee20795584c3f8cb853d0f0714fe26d4e3d2b0b2db26643ba595c1ba98ebccaf`
- bytes: 1717

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper
config        = template_parameters['metadata'].config

module_name = config['module_name']
%>\

import platform

import ctypes
import ctypes.util
import ${module_name}._library as _library
import ${module_name}.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = ${helper.get_dictionary_snippet(config['library_info'], indent=16)}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for ${config['module_name']}.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_matchers.py.mako sha256=358c2d3d23952cb9b08a39df5e01a617addfa8b4e4d10e0b6811a9703512018e bytes=14491 -->
## FILE: build/templates/_matchers.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_matchers.py.mako`
- sha256: `358c2d3d23952cb9b08a39df5e01a617addfa8b4e4d10e0b6811a9703512018e`
- bytes: 14491

````mako
${template_parameters['encoding_tag']}
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''
<%
import build.helper as helper

config = template_parameters['metadata'].config
functions = config['functions']
functions = helper.filter_codegen_functions(functions)
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>\

import ctypes
% if are_complex_parameters_used:
import ${template_parameters['metadata'].config['module_name']}._complextype as _complextype
% endif
import ${template_parameters['metadata'].config['module_name']}._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


% if are_complex_parameters_used:
def _compare_complex_number_arrays(expected, actual):
    for i in range(expected.expected_size):
        expected_value = expected.expected_data[i]
        actual_value = actual[i]
        if expected_value.real != actual_value.real or expected_value.imag != actual_value.imag:
            return False
    return True


class NIComplexNumberPointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexNumber)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexNumberPointerMatcher({self.expected_data})"


class NIComplexNumberF32PointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexNumberF32)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexNumberF32PointerMatcher({self.expected_data})"


class NIComplexI16PointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexI16)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexI16PointerMatcher({self.expected_data})"


% endif
# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_mock_helper.py.mako sha256=aa56725bcb1705cf2e421b550d9e508b53bff99bd11a6a47b4b30704160b3e13 bytes=5520 -->
## FILE: build/templates/_mock_helper.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/_mock_helper.py.mako`
- sha256: `aa56725bcb1705cf2e421b550d9e508b53bff99bd11a6a47b4b30704160b3e13`
- bytes: 5520

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper

config        = template_parameters['metadata'].config
attributes    = config['attributes']
functions     = config['functions']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = template_parameters['metadata'].functions
functions = helper.filter_library_functions(functions)
%>\
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
% for func_name in sorted(functions):
<%
f = functions[func_name]
params = f['parameters']
ivi_dance_params = helper.filter_ivi_dance_parameters(params)
%>\
        self._defaults['${func_name}'] = {}
        self._defaults['${func_name}']['return'] = 0
%   for p in helper.filter_parameters(params, helper.ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS):
%     if p not in ivi_dance_params:
        self._defaults['${func_name}']['${p['name']}'] = None
%     endif
%   endfor
%   for param in ivi_dance_params:
        self._defaults['${func_name}']['${param['name']}'] = None
%   endfor
% endfor

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

% for func_name in sorted(functions):
<%
f = functions[func_name]
params = f['parameters']
output_params = helper.filter_parameters(params, helper.ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS)
ivi_dance_params = helper.filter_ivi_dance_parameters(params)
ivi_dance_size_param = helper.find_size_parameter(ivi_dance_params, params)
output_params_minus_ivi_dance_params = [p for p in output_params if p not in ivi_dance_params]
%>\
    def ${c_function_prefix}${func_name}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_DECLARATION)}):  # noqa: N802
        if self._defaults['${func_name}']['return'] != 0:
            return self._defaults['${func_name}']['return']
%    for p in output_params_minus_ivi_dance_params:
        # ${p['python_name']}
        if self._defaults['${func_name}']['${p['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${p['name']}')
%       if p['is_buffer']:
        test_value = self._defaults['${func_name}']['${p['name']}']
<% param_name = p['python_name'] %>\
        try:
            ${param_name}_ref = ${param_name}.contents
        except AttributeError:
            ${param_name}_ref = ${param_name}
        assert len(${param_name}_ref) >= len(test_value)
        for i in range(len(test_value)):
            ${param_name}_ref[i] = test_value[i]
%       else:
%           if helper.find_custom_type(p, config) is not None:
        for field in self._defaults['${func_name}']['${p["python_name"]}']._fields_:
            field_name = field[0]
            setattr(${p["python_name"]}.contents, field_name, getattr(self._defaults['${func_name}']['${p["python_name"]}'], field_name))
%           elif p['is_string']:
        test_value = self._defaults['${func_name}']['${p['name']}']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
<%
param_name = p['python_name']
if p['use_array']:
    param_name += '.contents'
%>\
        assert len(${param_name}) >= len(test_value)
        for i in range(len(test_value)):
            ${param_name}[i] = test_value[i]
%           else:
        if ${p['python_name']} is not None:
            ${p['python_name']}.contents.value = self._defaults['${func_name}']['${p['name']}']
%           endif
%       endif
%    endfor
%    for id_param in ivi_dance_params:
        # ${id_param['python_name']}
        if self._defaults['${func_name}']['${id_param['name']}'] is None:
            raise MockFunctionCallError("${c_function_prefix}${func_name}", param='${id_param['name']}')
        if ${ivi_dance_size_param['python_name']}.value == 0:
            return len(self._defaults['${func_name}']['${id_param['name']}'])
%       if id_param['is_string']:  # strings
        ${id_param['python_name']}.value = self._defaults['${func_name}']['${id_param['name']}'].encode('ascii')
%       else:  # arrays
<% param_name = id_param['python_name'] %>\
        try:
            ${param_name}_ref = ${param_name}.contents
        except AttributeError:
            ${param_name}_ref = ${param_name}
        for i in range(len(self._defaults['${func_name}']['${id_param["name"]}'])):
            ${param_name}_ref[i] = self._defaults['${func_name}']['${id_param["name"]}'][i]
%       endif
%    endfor
        return self._defaults['${func_name}']['return']

% endfor
    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
% for func_name in sorted(functions):
<%
f = functions[func_name]
%>\
        mock_library.${c_function_prefix}${func_name}.side_effect = MockFunctionCallError("${c_function_prefix}${func_name}")
        mock_library.${c_function_prefix}${func_name}.return_value = 0
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: build/templates/_visatype.py

- repository: `ni/nimi-python`
- source_path: `build/templates/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/about_driver.inc.mako sha256=f2f89416e8e8380a427525548e3bdde0878fe86caa5a10bdf7b2528ff7a1d3d5 bytes=708 -->
## FILE: build/templates/about_driver.inc.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/about_driver.inc.mako`
- sha256: `f2f89416e8e8380a427525548e3bdde0878fe86caa5a10bdf7b2528ff7a1d3d5`
- bytes: 708

````mako
<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    driver_name   = config['driver_name']
%>\
.. _about-section:

About
=====

The **${module_name}** module provides a Python API for ${driver_name}. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**${module_name}** supports all the Operating Systems supported by ${driver_name}.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **${module_name}**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/class.rst.mako sha256=d80668dcf0dcd63d4f5b08fbd4389f1cc61919eb2d4f06335cb146b6a18b16da bytes=5100 -->
## FILE: build/templates/class.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/class.rst.mako`
- sha256: `d80668dcf0dcd63d4f5b08fbd4389f1cc61919eb2d4f06335cb146b6a18b16da`
- bytes: 5100

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    c_function_prefix = config['c_function_prefix']
    driver_name = config['driver_name']
    module_name = config['module_name']

    functions_all = template_parameters['metadata'].functions
    functions = helper.filter_public_functions(functions_all)

    grpc_supported = template_parameters['include_grpc_support']

    if 'context_manager_name' in config:
        # Add a InitiateDoc entry - only used to add initiate() to the Session documentation
        initiate_doc = helper.initiate_function_def_for_doc(functions_all, config)
        if initiate_doc is not None:
            functions['InitiateDoc'] = initiate_doc

    # Add a CloseDoc entry - only used to add close() to the Session documentation
    close_doc = helper.close_function_def_for_doc(functions_all, config)
    if close_doc is not None:
        functions['CloseDoc'] = close_doc

    doc_list = {}
    for fname in sorted(functions):
        for method_template in functions[fname]['method_templates']:
            name =  functions[fname]['python_name'] + method_template['method_python_name_suffix']
            doc_list[name] = { 'filename': method_template['documentation_filename'], 'method_template': method_template, 'function': functions[fname], }

    attributes = helper.filter_codegen_attributes_public_only(config['attributes'])

    init_function = config['functions']['_init_function']
    init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
    constructor_params = helper.filter_parameters(init_function['parameters'], helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
    input_params = helper.filter_parameters(init_function['parameters'], helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
%>\
.. py:module:: ${module_name}

${helper.get_rst_header_snippet('Session', '=')}

<%
grpc_options_param = ', *, grpc_options=None' if grpc_supported else ''
if grpc_supported:
    input_params.append(
        {
            'default_value': None,
            'direction': 'in',
            'documentation': { 'description': 'MeasurementLink gRPC session options' },
            'enum': None,
            'is_repeated_capability': False,
            'is_session_handle': False,
            'python_name': 'grpc_options',
            'size': {'mechanism': 'fixed', 'value': 1},
            'type_in_documentation': module_name + '.GrpcSessionOptions',
            'type_in_documentation_was_calculated': False,
            'use_in_python_api': False,
        },
    )
%>\
.. py:class:: Session(${init_method_params}${grpc_options_param})

    ${helper.get_documentation_for_node_rst(init_function, config, indent=4)}

% for p in input_params:
    :param ${p['python_name']}:
        ${helper.get_documentation_for_node_rst(p, config, 8)}
    :type ${p['python_name']}: ${helper.format_type_for_rst_documentation(p, numpy, config)}

% endfor

${helper.get_rst_header_snippet('Methods', '=')}

% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
${helper.get_rst_header_snippet(item, '-')}

    .. py:currentmodule:: ${module_name}.Session

<%include file="${'/functions.rst' + function_item['filename'] + '.rst.mako'}" args="function=function_item['function'], config=config, method_template=function_item['method_template'], indent=8" />\

% endfor

% if len(attributes) > 0:
${helper.get_rst_header_snippet('Properties', '=')}

% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]['python_name'], '-')}

    .. py:attribute:: ${attributes[attr]["python_name"]}

<%
a = attributes[attr]
table_contents = [
         ('Characteristic', 'Value'),
         ('Datatype', a['type_in_documentation']),
         ('Permissions', a['access']),
         ]
if helper.module_supports_repeated_caps(config):
    table_contents.append(('Repeated Capabilities', helper.get_attribute_repeated_caps(a)))

table = helper.as_rest_table(table_contents)

helper.add_attribute_rep_cap_tip(a, config)

desc = helper.get_documentation_for_node_rst(a, config, indent=0)
%>\
        ${helper.get_indented_docstring_snippet(desc, indent=8)}

        The following table lists the characteristics of this property.

            ${helper.get_indented_docstring_snippet(table, indent=12)}

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr] and len(attributes[attr]['lv_property']) > 0:
                - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
                - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor
% endif

% if config['uses_nitclk']:
${helper.get_rst_header_snippet('NI-TClk Support', '=')}

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


% endif
.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/conf.py.mako sha256=62e5856f2ea628fb263af1683eb3bda4d2b1ed5e351bfc856caf7c9a062fa9c2 bytes=6728 -->
## FILE: build/templates/conf.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/conf.py.mako`
- sha256: `62e5856f2ea628fb263af1683eb3bda4d2b1ed5e351bfc856caf7c9a062fa9c2`
- bytes: 6728

````mako
<%
import datetime
current_year = datetime.datetime.today().year

config = template_parameters['metadata'].config
copyright_start_year = config['initial_release_year']
version = config['module_version']

api_name = f"{config['driver_name']} Python API"
api_name_no_spaces_or_hyphens = api_name.replace(" ", "").replace("-", "")
api_name_no_spaces_or_hyphens_lower = api_name_no_spaces_or_hyphens.lower()

all_modules = {'nidcpower', 'nidigital', 'nidmm', 'nifgen', 'nimodinst', 'nirfsg', 'niscope', 'niswitch', 'nise', 'nitclk'}
module_name   = config['module_name']
external_modules = all_modules - {module_name}
%>\
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ${api_name} documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 14 13:04:36 2017.
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
import os
import sys
sys.path.insert(0, os.path.abspath('../generated'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

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
project = '${api_name}'
copyright = '${copyright_start_year}-${current_year}, National Instruments Corporation'
author = 'NI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '${version}'
# The short X.Y version.
version = release[:3]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Fix wide tables of RTD per https://github.com/rtfd/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    app.add_css_file('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NIModularInstrumentsPythonAPIdoc'


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
    (master_doc, '${api_name_no_spaces_or_hyphens}.tex', '${api_name} Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '${api_name_no_spaces_or_hyphens_lower}', '${api_name} Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '${api_name_no_spaces_or_hyphens}', '${api_name} Documentation',
     author, '${api_name_no_spaces_or_hyphens}', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
% for module in sorted(external_modules):
    '${module}': ('https://${module}.readthedocs.io/en/latest/', None),
% endfor
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/driver.rst.mako sha256=e211e1f1861823e9780841560380019b9aa9235dfc76a5da0a3622e47702cfc5 bytes=354 -->
## FILE: build/templates/driver.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/driver.rst.mako`
- sha256: `e211e1f1861823e9780841560380019b9aa9235dfc76a5da0a3622e47702cfc5`
- bytes: 354

````mako
<%
    '''This is a template for the module-specific .rst'''

    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    doc_header    = f"{module_name} module"
%>\
${doc_header}
${"=" * len(doc_header)}

.. include:: installation.inc

.. include:: ../_static/${module_name}_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/enums.py.mako sha256=bab2b8912f0e9daf3dafac474caf4e9fb9c8c7133cdd5f2b3a1143c747d76719 bytes=1285 -->
## FILE: build/templates/enums.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/enums.py.mako`
- sha256: `bab2b8912f0e9daf3dafac474caf4e9fb9c8c7133cdd5f2b3a1143c747d76719`
- bytes: 1285

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper
config = template_parameters['metadata'].config
enums = config['enums']
%>
from enum import Enum
% if any(enums[e].get('class', 'Enum') == 'IntFlag' for e in enums):
from enum import IntFlag
% endif
% for enum_name in sorted(helper.filter_codegen_enums(enums)):


class ${enums[enum_name]['python_name']}(${enums[enum_name].get('class', 'Enum')}):
<%
    print_list = []
%>\
    % for enum_value in enums[enum_name]['values']:
    % if type(enum_value['value']) is str:
    ${enum_value['python_name']} = '${enum_value['value']}'
    % else:
    ${enum_value['python_name']} = ${enum_value['value']}
    % endif
    % if 'documentation' in enum_value and len(helper.get_documentation_for_node_docstring(enum_value, config, indent=4).strip()) > 0:
    r'''
    ${helper.get_documentation_for_node_docstring(enum_value, config, indent=4)}
    '''
    % endif
<%
if 'pretty_name' in enum_value:
    print_list.append(enum_value)
%>\
    % endfor
    % if print_list:

    def __str__(self):
        return {
    % for enum_value in print_list:
            '${enum_value['python_name']}': '${enum_value['pretty_name']}',
    % endfor
        }.get(self.name, self.name)
    % endif
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/enums.rst.mako sha256=708204370ea3ecd27fa71e890494c796e67663ea582130046dac4396f5ff376d bytes=825 -->
## FILE: build/templates/enums.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/enums.rst.mako`
- sha256: `708204370ea3ecd27fa71e890494c796e67663ea582130046dac4396f5ff376d`
- bytes: 825

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    enums = config['enums']
%>\
${helper.get_rst_header_snippet('Enums', '=')}

Enums used in ${driver_name}

.. py:currentmodule:: ${module_name}

% for enum_name in sorted(helper.filter_codegen_enums(enums)):
% if enums[enum_name]['codegen_method'] == 'public':  # For documentation we only want public enums

${helper.get_rst_header_snippet(enums[enum_name]['python_name'], '-')}

.. py:class:: ${enums[enum_name]['python_name']}
    % for enum_value in enums[enum_name]['values']:

    .. py:attribute:: ${enum_name}.${enum_value['python_name']}

${helper.get_documentation_for_node_rst(enum_value, config, indent=8)}
    % endfor
% endif
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/errors.py.mako sha256=ff9b25b0b2c974e7112cdaee4744a87ad28e5865a83024681417f2f49344c40a bytes=5089 -->
## FILE: build/templates/errors.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/errors.py.mako`
- sha256: `ff9b25b0b2c974e7112cdaee4744a87ad28e5865a83024681417f2f49344c40a`
- bytes: 5089

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
config            = template_parameters['metadata'].config
grpc_supported    = template_parameters['include_grpc_support']
attributes        = config['attributes']
functions         = config['functions']
extra_errors_used = config['extra_errors_used']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


<%
# All drivers need Error, DriverError, DriverWarning, UnsupportedConfigurationError and DriverNotInstalledError
%>\
class Error(Exception):
    '''Base error class for ${driver_name}'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the ${driver_name} driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


% if grpc_supported:
class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


% endif
class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The ${driver_name} runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the ${driver_name} driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the ${driver_name} runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the ${driver_name} driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The ${driver_name} runtime returned an unexpected value. This can occur if it is too new for the ${module_name} Python module. Upgrade the ${module_name} Python module.')


% if 'InvalidRepeatedCapabilityError' in extra_errors_used:
class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


% endif
% if 'SelfTestError' in extra_errors_used:
class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


% endif
def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by ${module_name}.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/errors.rst.mako sha256=c2536a314a7aa47183a82a3e48fbbbbf5bee1a59b3746df9cbf4397f7b243cad bytes=2729 -->
## FILE: build/templates/errors.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/errors.rst.mako`
- sha256: `c2536a314a7aa47183a82a3e48fbbbbf5bee1a59b3746df9cbf4397f7b243cad`
- bytes: 2729

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    driver_name = config['driver_name']
    enums = config['enums']
    extra_errors_used = config['extra_errors_used']
    module_name = config['module_name']

    grpc_supported = template_parameters['include_grpc_support']
%>\
${helper.get_rst_header_snippet('Exceptions and Warnings', '=')}

${helper.get_rst_header_snippet('Error', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: Error

        Base exception type that all ${driver_name} exceptions derive from


${helper.get_rst_header_snippet('DriverError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverError

        An error originating from the ${driver_name} driver


${helper.get_rst_header_snippet('UnsupportedConfigurationError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

${helper.get_rst_header_snippet('DriverNotInstalledError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

${helper.get_rst_header_snippet('DriverTooOldError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the ${driver_name} driver runtime.

${helper.get_rst_header_snippet('DriverTooNewError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverTooNewError

        An error due to the ${driver_name} driver runtime being too new for this module.

% if 'InvalidRepeatedCapabilityError' in extra_errors_used:
${helper.get_rst_header_snippet('InvalidRepeatedCapabilityError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


% endif
% if 'SelfTestError' in extra_errors_used:
${helper.get_rst_header_snippet('SelfTestError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


% endif
% if grpc_supported:
${helper.get_rst_header_snippet('RpcError', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


% endif
${helper.get_rst_header_snippet('DriverWarning', '-')}

    .. py:currentmodule:: ${module_name}.errors

    .. exception:: DriverWarning

        A warning originating from the ${driver_name} driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/examples.rst.mako sha256=d423bc9d77b199ab017cc33948ca7c80ca155ceeee457a1867d42acf44bb14a1 bytes=2778 -->
## FILE: build/templates/examples.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/examples.rst.mako`
- sha256: `d423bc9d77b199ab017cc33948ca7c80ca155ceeee457a1867d42acf44bb14a1`
- bytes: 2778

````mako
<%
    import build.helper as helper

    config         = template_parameters['metadata'].config
    module_name    = config['module_name']
    module_version = config['module_version']

    import glob
    import os

    examples_dir = os.path.join('src', module_name, 'examples')
    examples = glob.glob(examples_dir + '/**/*.py', recursive=True)
    examples = sorted(examples)

    # The examples page will show 2 things:
    #   1) URL to zip file containing all examples and in cases like nidigital, support files
    #   2) Code snippet and URL to example file in src folder, for each example
    #
    #  - If there is dev or pre ('a', 'b', 'rc') in module_version then:
    #       - it means code generator is being run during development
    #       - (1) will link to the zip file created during last release and the text will include "..for latest version.."
    #       - (2) will include current code snippet and URL will point to master branch
    #  - Else:
    #       - it means code generator is being run during a release
    #       - (1) will link to the zip file for the current release
    #       - (2) will include current code snippet and URL will point to release version

    with open(f'./src/{module_name}/LATEST_RELEASE') as vf:
        latest_release_version = vf.read().strip()

    from packaging.version import Version
    v = Version(module_version)

    # Check if the module name and version match the old tag formatting criteria
    use_old_tag_format = (
        module_name in ['nidcpower', 'nidigital', 'nidmm', 'nifake', 'niswitch', 'nimodinst', 'nifgen', 'niscope', 'nise', 'nitclk']
        and latest_release_version == '1.4.9'
    )

    if not use_old_tag_format:
        latest_release_version = module_name + '-' + latest_release_version
    
    released_zip_url = 'https://github.com/ni/nimi-python/releases/download/{}/{}_examples.zip'.format(latest_release_version, module_name)

    example_url_base = 'https://github.com/ni/nimi-python/blob/'

    if v.dev is None and v.pre is None:
        examples_zip_url_text = '`You can download all {} examples here <{}>`_'.format(module_name, released_zip_url)
        example_url_base += latest_release_version
    else:
        examples_zip_url_text = '`You can download all {} examples for latest version here <{}>`_'.format(module_name, released_zip_url)
        example_url_base += 'master'
%>\
${helper.get_rst_header_snippet('Examples', '=')}

${examples_zip_url_text}

% for e in examples:
${helper.get_rst_header_snippet(os.path.basename(e), '-')}

.. literalinclude:: ${os.path.join('..', '..', e).replace('\\', '/')}
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(${os.path.basename(e)}) <${example_url_base}/${e.replace('\\', '/')}>`_

% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/functions.rst/default_method.rst.mako sha256=f74effc2d1f9ed5d68e63d5740761436783b734c283577061814b01c2bb32702 bytes=217 -->
## FILE: build/templates/functions.rst/default_method.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/functions.rst/default_method.rst.mako`
- sha256: `f74effc2d1f9ed5d68e63d5740761436783b734c283577061814b01c2bb32702`
- bytes: 217

````mako
<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
    ${helper.get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=indent)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/functions.rst/lock.rst.mako sha256=268e2b2488a423ab1f4c447acd4ee18f466f4b459d8a485c8c0fb91be4c67435 bytes=2319 -->
## FILE: build/templates/functions.rst/lock.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/functions.rst/lock.rst.mako`
- sha256: `268e2b2488a423ab1f4c447acd4ee18f466f4b459d8a485c8c0fb91be4c67435`
- bytes: 2319

````mako
<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`${config['module_name']}.Session.lock` method.
        -  A call to ${config['driver_name']} locked the session.
        -  After a call to the :py:meth:`${config['module_name']}.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`${config['module_name']}.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`${config['module_name']}.Session.lock` method and the
           :py:meth:`${config['module_name']}.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`${config['module_name']}.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`${config['module_name']}.Session.lock` method with a call to
    the :py:meth:`${config['module_name']}.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with ${config['module_name']}.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`${config['module_name']}.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/functions.rst/numpy_method.rst.mako sha256=2398b6c610fee9d61f3993785d14672025d3a530c6ec63da2dfa82fd3d8c8aaa bytes=216 -->
## FILE: build/templates/functions.rst/numpy_method.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/functions.rst/numpy_method.rst.mako`
- sha256: `2398b6c610fee9d61f3993785d14672025d3a530c6ec63da2dfa82fd3d8c8aaa`
- bytes: 216

````mako
<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
    ${helper.get_function_rst(function, method_template=method_template, numpy=True, config=config, indent=indent)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/functions.rst/unlock.rst.mako sha256=e6e3fa34e93df2415770e04444176cc44d95badcdf3d7e6f42b0e57fe590130b bytes=373 -->
## FILE: build/templates/functions.rst/unlock.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/functions.rst/unlock.rst.mako`
- sha256: `e6e3fa34e93df2415770e04444176cc44d95badcdf3d7e6f42b0e57fe590130b`
- bytes: 373

````mako
<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    Releases a lock that you acquired on an device session using
    :py:meth:`${config['module_name']}.Session.lock`. Refer to :py:meth:`${config['module_name']}.Session.unlock` for additional
    information on session locks.
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/grpc_session_options.py.mako sha256=af478ed8ec6eff8e35fcdceba07ac4ac04c391bb0117c36b0aedeb59ea6553d5 bytes=3660 -->
## FILE: build/templates/grpc_session_options.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/grpc_session_options.py.mako`
- sha256: `af478ed8ec6eff8e35fcdceba07ac4ac04c391bb0117c36b0aedeb59ea6553d5`
- bytes: 3660

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
    config = template_parameters['metadata'].config
    module_name = config['module_name']
    proto_name = config.get('proto_name', module_name)
%>\

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = '${proto_name}_grpc.${config["grpc_service_class_prefix"]}'

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.

    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(
        self,
        grpc_channel,
        session_name,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO
    ):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a Session constructor.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.

            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.

            api_key (str): Specifies the API license key required by the NI gRPC Device Server.

            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/grpc_session_options.rst.mako sha256=d2c3f772756e5630fa3c8861c2e48c5312dfb2106a8fe14c38436425b5cb3971 bytes=3140 -->
## FILE: build/templates/grpc_session_options.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/grpc_session_options.rst.mako`
- sha256: `d2c3f772756e5630fa3c8861c2e48c5312dfb2106a8fe14c38436425b5cb3971`
- bytes: 3140

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    enums = config['enums']
%>\
${helper.get_rst_header_snippet('gRPC Support', '=')}

Support for using ${driver_name} over gRPC

.. py:currentmodule:: ${module_name}



SessionInitializationBehavior
-----------------------------

.. py:class:: SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO


        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.


    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION


        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will automatically close the
            server session.


    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION


        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will detach from the server session
            and leave it open.



GrpcSessionOptions
------------------


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)


    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a Session constructor.


    :param grpc_channel:
        

        Specifies the channel to the NI gRPC Device Server.

        

    :type grpc_channel: grpc.Channel


    :param session_name:
        

        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
        You can use an empty string if you want to always initialize a new session on the server.
        To attach to an existing session, you must specify the session name it was initialized with.

        

    :type session_name: str


    :param initialization_behavior:
        

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.

        

    :type initialization_behavior: :py:data:`${module_name}.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/index.rst.mako sha256=98aad70bd3277c3b0feb9bb11e339ffec61c3e782a623f64a24c8cd4195d1b54 bytes=1119 -->
## FILE: build/templates/index.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/index.rst.mako`
- sha256: `98aad70bd3277c3b0feb9bb11e339ffec61c3e782a623f64a24c8cd4195d1b54`
- bytes: 1119

````mako
<%
    config        = template_parameters['metadata'].config
    doc_header    = f"{config['driver_name']} Python API Documentation"
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    mi_drivers = ['nidcpower', 'nidigital', 'nidmm', 'nifgen', 'nimodinst', 'niscope', 'niswitch', 'nise', 'nitclk']
    read_the_docs_note = (
        "Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier."
    )
%>\

${doc_header}
${"=" * len(doc_header)}

.. include:: about_${module_name}.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   ${module_name}

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

% if module_name in mi_drivers:
${read_the_docs_note}
% endif

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/installation.inc.mako sha256=14b3c7f578bc60019af527a63177aa3a02e4a9d4ab2d16e632479ffc9a4e65d8 bytes=1289 -->
## FILE: build/templates/installation.inc.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/installation.inc.mako`
- sha256: `14b3c7f578bc60019af527a63177aa3a02e4a9d4ab2d16e632479ffc9a4e65d8`
- bytes: 1289

````mako
<%
    import build.helper as helper
    from packaging.version import Version

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    v = Version(config['module_version'])
    if v.pre is not None or v.dev is not None:
        # If the version is a prerelease or a dev release we do not put a version to pin to in the installation instructions
        # This is confusing when seen in master because the version doesn't exist yet
        version_pin = ''
    else:
        version_pin = '~=' + config['module_version']
%>\

.. _${module_name}_installation-section:

Installation
------------

As a prerequisite to using the **${module_name}** module, you must install the ${driver_name} runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **${driver_name}**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install ${module_name}${version_pin}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/rep_caps.rst.mako sha256=e0580dca59df36c59273f098456dee329897f769e5261d6944a7ba1a75d8fb0f bytes=2262 -->
## FILE: build/templates/rep_caps.rst.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/rep_caps.rst.mako`
- sha256: `e0580dca59df36c59273f098456dee329897f769e5261d6944a7ba1a75d8fb0f`
- bytes: 2262

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']

%>\
.. py:module:: ${module_name}
    :noindex:

.. py:currentmodule:: ${module_name}.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

${helper.get_rst_header_snippet('Repeated Capabilities', '=')}

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`${config['c_function_prefix']}SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
prefix = rep_cap['prefix']
%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

% if len(prefix) > 0:
        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.${name}['0-2'].channel_enabled = True

        passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

% endif
        .. code:: python

            session.${name}['${prefix}0-${prefix}2'].channel_enabled = True

        passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.


% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/datetime_wrappers.py.mako sha256=b12a1d1961ce6b0833373f69a942d2393d1bc8afa0971888f85c9e388446f595 bytes=1050 -->
## FILE: build/templates/session.py/datetime_wrappers.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/datetime_wrappers.py.mako`
- sha256: `b12a1d1961ce6b0833373f69a942d2393d1bc8afa0971888f85c9e388446f595`
- bytes: 1050

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    output_params_list = []
    called_function = config['functions'][f['real_datetime_call']]
    for p in called_function['parameters']:
        if p['direction'] == 'out':
            output_params_list.append(p['python_name'])

    output_params = ', '.join(output_params_list)
    include_second = False
    if "second" in output_params_list:
        include_second = True
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        ${output_params} = self.${called_function['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_CALL)})
        %if include_second is False:
        return hightime.datetime(year, month, day, hour, minute)
        %else:
        return hightime.datetime(year, month, day, hour, minute, second)
        %endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/default_method.py.mako sha256=a91b31f359d20ce1a1bf43e5d11106ddb7eac23e95e059f7e8bf1c6a865b78f2 bytes=1769 -->
## FILE: build/templates/session.py/default_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/default_method.py.mako`
- sha256: `a91b31f359d20ce1a1bf43e5d11106ddb7eac23e95e059f7e8bf1c6a865b78f2`
- bytes: 1769

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method corresponding to the passed-in function metadata.'''

    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    parameters = f['parameters']
    enum_input_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    output_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.API_OUTPUT_PARAMETERS)
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for size_check_snippet in helper.get_parameter_size_check_snippets(parameters):
        ${size_check_snippet}
% endfor
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(parameters, config)}
% else:
        self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/fancy_self_test.py.mako sha256=48d6ee75a2cb4e92817fac2585af4b28785c4b30230734930baae02af8f6e38b bytes=499 -->
## FILE: build/templates/session.py/fancy_self_test.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/fancy_self_test.py.mako`
- sha256: `48d6ee75a2cb4e92817fac2585af4b28785c4b30230734930baae02af8f6e38b`
- bytes: 499

````mako
<%page args="f, config, method_template"/>\
<%
    '''Call self-test and throw if there is a failure'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/get_channel_names.py.mako sha256=2ff1cdac76f251e9143a11e514caf767a909e4a67d20b6850640a5ba7c0280ef bytes=924 -->
## FILE: build/templates/session.py/get_channel_names.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/get_channel_names.py.mako`
- sha256: `2ff1cdac76f251e9143a11e514caf767a909e4a67d20b6850640a5ba7c0280ef`
- bytes: 924

````mako
<%page args="f, config, method_template"/>\
<%
    '''Some "fancy" methods in _SessionBase need to get channel names, but exposing
    get_channel_names() from _SessionBase as part of public API would allow
    users to call it with "channels" repeated capability which we want to avoid.
    For that reason, some modules code-generate _get_channel_names() as private in
    _SessionBase and then put this public wrapper in Session.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        return self._${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL)})
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/lock.py.mako sha256=1fcc59d15533d39ffa020dd58c3b6a35d96e25b9f7ee6a9e4b48eeeca5f1e885 bytes=1767 -->
## FILE: build/templates/session.py/lock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/lock.py.mako`
- sha256: `1fcc59d15533d39ffa020dd58c3b6a35d96e25b9f7ee6a9e4b48eeeca5f1e885`
- bytes: 1767

````mako
<%page args="f, config, method_template"/>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to ${config['driver_name']} locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, ${config['module_name']}.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/numpy_read_method.py.mako sha256=e2e6d7903ea5457bcff84a0ea56ed319ac6bc488faad6f6312d0f33878b312c7 bytes=2609 -->
## FILE: build/templates/session.py/numpy_read_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/numpy_read_method.py.mako`
- sha256: `e2e6d7903ea5457bcff84a0ea56ed319ac6bc488faad6f6312d0f33878b312c7`
- bytes: 2609

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method for reading into a numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    enum_input_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    output_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS)
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        import numpy

% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for size_check_snippet in helper.get_parameter_size_check_snippets(parameters):
        ${size_check_snippet}
% endfor
% for parameter in helper.filter_parameters(parameters, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        if type(${parameter['python_name']}) is not numpy.ndarray:
            raise TypeError('${parameter['python_name']} must be {0}, is {1}'.format(numpy.ndarray, type(${parameter['python_name']})))
        if numpy.isfortran(${parameter['python_name']}) is True:
            raise TypeError('${parameter['python_name']} must be in C-order')
        if ${parameter['python_name']}.dtype is not numpy.dtype('${parameter['numpy_type']}'):
            raise TypeError('${parameter['python_name']} must be numpy.ndarray of dtype=${parameter['numpy_type']}, is ' + str(${parameter['python_name']}.dtype))
% endfor
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(parameters, config, use_numpy_array=True)}
% else:
        self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL)})
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/numpy_write_method.py.mako sha256=4c77dcc154e18ea996c4c5117ae5936ffb7cb17910ee7f55abe707c446c22c5a bytes=2811 -->
## FILE: build/templates/session.py/numpy_write_method.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/numpy_write_method.py.mako`
- sha256: `4c77dcc154e18ea996c4c5117ae5936ffb7cb17910ee7f55abe707c446c22c5a`
- bytes: 2811

````mako
<%page args="f, config, method_template"/>\
<%
    '''Renders a Session method for writing numpy.array corresponding to the passed-in function metadata.'''

    import build.helper as helper

    parameters = f['parameters']
    enum_input_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.INPUT_ENUM_PARAMETERS)
    output_parameters = helper.filter_parameters(parameters, helper.ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS)
    output_parameters_snippet = ', '.join(p['python_name'] for p in output_parameters)
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}${suffix}

        ${helper.get_function_docstring(f, True, config, indent=8)}
        '''
        import numpy

% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter, indent=12)}
% endfor
% for size_check_snippet in helper.get_parameter_size_check_snippets(parameters):
        ${size_check_snippet}
% endfor
% for parameter in helper.filter_parameters(parameters, helper.ParameterUsageOptions.NUMPY_PARAMETERS):
        if type(${parameter['python_name']}) is not numpy.ndarray:
            raise TypeError('${parameter['python_name']} must be {0}, is {1}'.format(numpy.ndarray, type(${parameter['python_name']})))
        if numpy.isfortran(${parameter['python_name']}) is True:
            raise TypeError('${parameter['python_name']} must be in C-order')
        if ${parameter['python_name']}.dtype is not numpy.dtype('${parameter['numpy_type']}'):
            raise TypeError('${parameter['python_name']} must be numpy.ndarray of dtype=${parameter['numpy_type']}, is ' + str(${parameter['python_name']}.dtype))
        if ${parameter['python_name']}.ndim != ${parameter['array_dimensions']}:
            raise TypeError('${parameter['python_name']} must be numpy.ndarray of dimension=${parameter['array_dimensions']}, is ' + str(${parameter['python_name']}.ndim))
% endfor
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL):
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor
% if output_parameters:
        ${output_parameters_snippet} = self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
        ${helper.get_session_method_return_snippet(parameters, config, use_numpy_array=True)}
% else:
        self._interpreter.${f['interpreter_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_CALL)})
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py/unlock.py.mako sha256=2678a717fd6fdd271917ff7aed33ad3916ae27928f2cb1ecef2cdad782312057 bytes=308 -->
## FILE: build/templates/session.py/unlock.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py/unlock.py.mako`
- sha256: `2678a717fd6fdd271917ff7aed33ad3916ae27928f2cb1ecef2cdad782312057`
- bytes: 308

````mako
<%page args="f, config, method_template"/>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/session.py.mako sha256=44cd69556613de60cb5a96649410432af4e34996b8c5a7cb8174fb18f3f05673 bytes=14406 -->
## FILE: build/templates/session.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/session.py.mako`
- sha256: `44cd69556613de60cb5a96649410432af4e34996b8c5a7cb8174fb18f3f05673`
- bytes: 14406

````mako
${template_parameters['encoding_tag']}
# This file was generated
<%
    import build.helper as helper
    import os

    grpc_supported = template_parameters['include_grpc_support']

    config = template_parameters['metadata'].config
    attributes = config['attributes']
    enums = config['enums']
    functions = helper.filter_codegen_functions(config['functions'])

    module_name = config['module_name']

    attributes = helper.filter_codegen_attributes(config['attributes'])

    close_function_name = helper.camelcase_to_snakecase(config['close_function'])

    session_context_manager = None
    if 'task' in config['context_manager_name']:
        session_context_manager = '_' + config['context_manager_name']['task'].title()
        session_context_manager_initiate = functions[config['context_manager_name']['initiate_function']]['python_name']
        session_context_manager_abort = functions[config['context_manager_name']['abort_function']]['python_name']
        render_initiate_in_session_base = functions[config['context_manager_name']['initiate_function']]['render_in_session_base']
%>\
import array  # noqa: F401
% if config['use_locking']:
# Used by @ivi_synchronized
from functools import wraps
% endif

% if attributes:
import ${module_name}._attributes as _attributes
% endif
import ${module_name}._converters as _converters
import ${module_name}._library_interpreter as _library_interpreter
import ${module_name}.enums as enums
import ${module_name}.errors as errors
% for c in config['custom_types']:

import ${module_name}.${c['file_name']} as ${c['file_name']}  # noqa: F401
% endfor

import hightime
% if config['uses_nitclk']:
import nitclk
% endif

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


% if session_context_manager is not None:
class ${session_context_manager}(object):
    def __init__(self, session):
        self._session = session
        self._session.${session_context_manager_initiate}()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.${session_context_manager_abort}()


% endif
% if config['use_locking']:
# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


% endif
% if len(config['repeated_capabilities']) > 0:
class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


% endif
class _SessionBase(object):
    '''Base class for all ${config['driver_name']} sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(helper.filter_codegen_attributes(attributes)):
<%
helper.add_attribute_rep_cap_tip(attributes[attribute], config)
%>\
    %if attributes[attribute]['enum']:
        %if helper.enum_uses_converter(enums[attributes[attribute]['enum']]):
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute}), _converters.${enums[attributes[attribute]['enum']]['enum_to_converted_value_function_name']}, _converters.${enums[attributes[attribute]['enum']]['converted_value_to_enum_function_name']})
        %else:
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute})
        %endif
    %else:
    ${attributes[attribute]['python_name']} = _attributes.${attributes[attribute]['attribute_class']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute] and len(helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4).strip()) > 0:
    '''Type: ${attributes[attribute]['type_in_documentation']}

    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor
<%
init_function = config['functions']['_init_function']
init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
init_call_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_CALL)
constructor_params = helper.filter_parameters(init_function['parameters'], helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
%>\
% if attributes:

% endif
    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

% if len(config['repeated_capabilities']) > 0:
        # Instantiate any repeated capability objects
%   for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}', repeated_capability_list)
%   endfor

% endif
        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

% if session_context_manager is not None and render_initiate_in_session_base:
    def initiate(self):
        '''initiate

        ${helper.get_function_docstring(helper.initiate_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        return ${session_context_manager}(self)

% endif
    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor


class Session(_SessionBase):
    '''${config['session_class_description']}'''

<% grpc_options_param = ', *, grpc_options=None' if grpc_supported else '' %>\
    def __init__(${init_method_params}${grpc_options_param}):
        r'''${config['session_class_description']}

<%
ctor_for_docs = init_function
if grpc_supported:
    import copy
    ctor_for_docs = copy.deepcopy(ctor_for_docs)
    ctor_for_docs['parameters'].append(
        {
            'default_value': None,
            'direction': 'in',
            'documentation': { 'description': 'MeasurementLink gRPC session options' },
            'enum': None,
            'is_repeated_capability': False,
            'is_session_handle': False,
            'python_name': 'grpc_options',
            'size': {'mechanism': 'fixed', 'value': 1},
            'type_in_documentation': module_name + '.grpc_session_options.GrpcSessionOptions',
            'type_in_documentation_was_calculated': False,
            'use_in_python_api': False,
        },
    )
%>\
        ${helper.get_function_docstring(ctor_for_docs, False, config, indent=8)}
        '''
% if grpc_supported:
        if grpc_options:
            import ${module_name}._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')
% else:
        interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')
% endif

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
% for p in init_function['parameters']:
%   if 'python_api_converter_name' in p:
        ${p['python_name']} = _converters.${p['python_api_converter_name']}(${p['python_name']})
%   endif
% endfor

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if ${init_function['python_name']} fails, the error handler can reference it.
        # And then here, once ${init_function['python_name']} succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self.${init_function['python_name']}(${init_call_params}))

% if config['uses_nitclk']:
%   if grpc_supported:
        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())
%   else:
        self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())
%   endif

% endif
        # Store the parameter list for later printing in __repr__
        param_list = []
%       for param in constructor_params:
        param_list.append("${param['python_name']}=" + pp.pformat(${param['python_name']}))
%       endfor
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
% if grpc_supported:
        if self._interpreter._close_on_exit:
            self.close()
% else:
        self.close()
% endif

% if session_context_manager is not None and not render_initiate_in_session_base:
    def initiate(self):
        '''initiate

        ${helper.get_function_docstring(helper.initiate_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        return ${session_context_manager}(self)

% endif
    def close(self):
        '''close

        ${helper.get_function_docstring(helper.close_function_def_for_doc(functions, config), False, config, indent=8)}
        '''
        try:
            self._${close_function_name}()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

% if functions[func_name]['use_session_lock'] and config['use_locking']:
    @ivi_synchronized
% endif
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/setup.py.mako sha256=2d6093ca056101c5868d7adb95969277fb3607beddca6cf8f3d3b4564aaa09a1 bytes=2464 -->
## FILE: build/templates/setup.py.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/setup.py.mako`
- sha256: `2d6093ca056101c5868d7adb95969277fb3607beddca6cf8f3d3b4564aaa09a1`
- bytes: 2464

````mako
#!/usr/bin/python
# This file was generated
<%
import build.helper as helper

config         = template_parameters['metadata'].config
grpc_supported = template_parameters['include_grpc_support']
module_version = config['module_version']
functions = config['functions']
functions = helper.filter_codegen_functions(functions)
are_complex_parameters_used = helper.are_complex_parameters_used(functions)
%>

from setuptools import setup


pypi_name = '${config['module_name']}'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='${config['module_version']}',
    description='${config['driver_name']} Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['${config['module_name']}'],
    license='MIT',
    include_package_data=True,
    packages=['${config['module_name']}'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
        % if config['uses_nitclk']:
        'nitclk',
        % endif
        % if are_complex_parameters_used:
        'numpy',
        % endif
    ],
    % if grpc_supported:
    extras_require={
        'grpc': [
            'grpcio>=1.59.0,<2.0',
            'protobuf>=4.21.6',
            'ni.grpcdevice.v1.proto>=1.0.0'
        ],
    },
    % endif
    classifiers=[
        "Development Status :: ${helper.get_development_status(config)}",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Instrument Drivers",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    package_data={pypi_name: ['VERSION']},
)
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/status.inc.mako sha256=7c34b9fb9fc0d71a59261a01cb9147d96058ab478e52c412c435480824df261e bytes=2621 -->
## FILE: build/templates/status.inc.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/status.inc.mako`
- sha256: `7c34b9fb9fc0d71a59261a01cb9147d96058ab478e52c412c435480824df261e`
- bytes: 2621

````mako
<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\
<%
table_contents = []
table_contents.append(['{} ({})'.format(driver_name, module_name), '', ])
table_contents.append(['Driver Version Tested Against', config['latest_runtime_version_tested_against']])
table_contents.append(['PyPI Version', '|{}LatestVersion|'.format(module_name)])
table_contents.append(['Supported Python Version', '|{}PythonVersion|'.format(module_name)])
table_contents.append(['Documentation', '|{}Docs|'.format(module_name)])
table_contents.append(['Open Issues', '|{}OpenIssues|'.format(module_name)])
table_contents.append(['Open Pull Requests', '|{}OpenPRs|'.format(module_name)])

driver_status_table = helper.as_rest_table(table_contents, header=True)

%>
${helper.get_rst_header_snippet(driver_name + ' Python API Status', '-')}

${helper.get_indented_docstring_snippet(driver_status_table, indent=0)}


${helper.get_rst_picture_reference('{}LatestVersion'.format(module_name), 'http://img.shields.io/pypi/v/{}.svg'.format(module_name), 'Latest {} Version'.format(driver_name), 'http://pypi.python.org/pypi/{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}PythonVersion'.format(module_name), 'http://img.shields.io/pypi/pyversions/{}.svg'.format(module_name), '{} supported Python versions'.format(driver_name), 'http://pypi.python.org/pypi/{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}Docs'.format(module_name), 'https://readthedocs.org/projects/{}/badge/?version=latest'.format(module_name), '{} Python API Documentation Status'.format(driver_name), 'https://{}.readthedocs.io/en/latest'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}OpenIssues'.format(module_name), 'https://img.shields.io/github/issues/ni/nimi-python/{}.svg'.format(module_name), 'Open Issues + Pull Requests for {}'.format(driver_name), 'https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3A{}'.format(module_name), indent=0)}

${helper.get_rst_picture_reference('{}OpenPRs'.format(module_name), 'https://img.shields.io/github/issues-pr/ni/nimi-python/{}.svg'.format(module_name), 'Pull Requests for {}'.format(driver_name), 'https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3A{}'.format(module_name), indent=0)}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/toc.inc.mako sha256=4fc2242982606ed6074fad665f552d52418e0d608ab92a8574b1ae66176ad50d bytes=461 -->
## FILE: build/templates/toc.inc.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/toc.inc.mako`
- sha256: `4fc2242982606ed6074fad665f552d52418e0d608ab92a8574b1ae66176ad50d`
- bytes: 461

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    enums = config['enums']
    grpc_supported = template_parameters['include_grpc_support']
%>\
API Reference
--------------

.. toctree::

   class
% if len(config['repeated_capabilities']) > 0:
   rep_caps
% endif
% if len(enums) > 0:
   enums
% endif
   errors
   examples
% if grpc_supported:
   grpc_session_options
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/tox-system_tests.ini.mako sha256=1bc73b0fdda0d57f6265738abf8f5cc2a5e4016e05d5e4f819dce4b9b3dca29a bytes=5326 -->
## FILE: build/templates/tox-system_tests.ini.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/tox-system_tests.ini.mako`
- sha256: `1bc73b0fdda0d57f6265738abf8f5cc2a5e4016e05d5e4f819dce4b9b3dca29a`
- bytes: 5326

````mako
<%
    import build.helper as helper
    import os

    grpc_supported = template_parameters['include_grpc_support']

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    if config['uses_nitclk'] or module_name == 'nitclk':
        wheel_env_no_py = '{}-wheel_dep'.format(module_name)
        # We only actually need to build it once, but we specify multiple versions here
        # to prevent tox from trying to build the wheel with an unsupported (earlier) Python version
        wheel_env = 'py{310,311,312,313,314}-' + wheel_env_no_py + ','
        uses_other_wheel = True
        if module_name == 'nitclk':
            # nitclk system tests use niscope
            other_wheel = 'niscope'
        else:
            other_wheel = 'nitclk'
    else:
        wheel_env = ''
        other_wheel = ''
        uses_other_wheel = False
%>\
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/${module_name})
[tox]
envlist = ${wheel_env}py{310,311,312,313,314}-${module_name}-system_tests, py314-${module_name}-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
% if uses_other_wheel:
    ${wheel_env_no_py}: Build the ${other_wheel} wheel because we use it in ${module_name} tests
% endif
    ${module_name}-system_tests: Run ${module_name} system tests (requires ${driver_name} runtime to be installed)
    ${module_name}-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
% if uses_other_wheel:
    ${wheel_env_no_py}: ../${other_wheel}
% endif
    ${module_name}-system_tests: .
    ${module_name}-coverage: .

commands =
% if uses_other_wheel:
    ${wheel_env_no_py}: python -m build --wheel

% endif
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    ${module_name}-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
% if uses_other_wheel:
    ${module_name}-system_tests: python ../../tools/install_local_wheel.py --driver ${other_wheel} --start-path ../..
% endif
    ${module_name}-system_tests: python -c "import ${module_name}; ${module_name}.print_diagnostic_information()"
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m pytest ../../src/${module_name}/examples --junitxml=../junit/junit-${module_name}-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    ${module_name}-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source ${module_name} --parallel-mode -m pytest ../../src/${module_name}/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-${module_name}-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    ${module_name}-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    ${module_name}-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    ${module_name}-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
% if uses_other_wheel:
    ${wheel_env_no_py}: build

% endif
% if module_name == 'nidigital':
    ${module_name}-system_tests: nisync
% endif
    ${module_name}-system_tests: pytest
    ${module_name}-system_tests: coverage
    ${module_name}-system_tests: numpy
    ${module_name}-system_tests: hightime
    ${module_name}-system_tests: fasteners
    ${module_name}-system_tests: pytest-json
% if grpc_supported:
    ${module_name}-system_tests: .[grpc]
% endif

    ${module_name}-coverage: coverage

depends =
    ${module_name}-coverage: py{310,311,312,313,314}-${module_name}-system_tests
% if uses_other_wheel:
    ${module_name}-system_tests: ${wheel_env}
% endif

passenv =
    GIT_BRANCH
    GIT_COMMIT
    BUILD_URL
    BRANCH_NAME
    JENKINS_URL
    BUILD_NUMBER

[pytest]
addopts = --verbose
filterwarnings =
   error::pytest.PytestUnhandledThreadExceptionWarning
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
junit_family = xunit1
% if module_name == 'nidcpower':
markers = # Defines custom markers used by nidcpower system tests. Prevents PytestUnknownMarkWarning.
    include_legacy_session: Include a legacy session in nidcpower system tests.
    legacy_session_only: Exclude an independent channels session in nidcpower system tests.
    resource_name: Overrides the default resource_name argument in the nidcpower session fixture.
    channels: Overrides the default channels argument in the nidcpower session fixture.
    reset: Overrides the default reset argument in the nidcpower session fixture.
    options: Overrides the default options argument in the nidcpower session fixture.
    independent_channels: Overrides the default independent_channels argument in the nidcpower session fixture.
% endif
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/templates/VERSION.mako sha256=e933dc84d35bc4895164b0adcb808ad3f8676e994582c4b34edc3ba7359488ee bytes=104 -->
## FILE: build/templates/VERSION.mako

- repository: `ni/nimi-python`
- source_path: `build/templates/VERSION.mako`
- sha256: `e933dc84d35bc4895164b0adcb808ad3f8676e994582c4b34edc3ba7359488ee`
- bytes: 104

````mako
<%
    module_version = template_parameters['metadata'].config['module_version']
%>\
${module_version}
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/tools.mak sha256=58309b5e30e8835f43be0016ac6d199fe2bda3229e899d1434091bb8bb5cca84 bytes=1088 -->
## FILE: build/tools.mak

- repository: `ni/nimi-python`
- source_path: `build/tools.mak`
- sha256: `58309b5e30e8835f43be0016ac6d199fe2bda3229e899d1434091bb8bb5cca84`
- bytes: 1088

````makefile
# Useful functions

CURRENT_DIR := $(shell pwd)

# Traces to console, nicely formatted.
# $1 is the Action, for example: "Generating"
# $2 is a Path.
# Action will be padded on the left so colons align, for readability.
# Path will be turned from absolute to relative, for readability.
define trace_to_console
	@echo "$(shell printf '%15s' $1): $(subst $(CURRENT_DIR)/,,$2)"
endef

# Executes a command, logs it to $(COMMAND_LOG), updates tracking file to show module file generated.
# $1 is the command.
define log_command
	$1
	@echo '$1' >> $(COMMAND_LOG)
	@touch $(DRIVER_FILE_BUILT)
endef

# Executes a command, then logs it to $(COMMAND_LOG).
# $1 is the command.
define log_command_no_tracking
	$1
	@echo '$1' >> $(COMMAND_LOG)
endef

# Helper function for running a command with a tracking file
# created/updated upon completion
# $1 is tracking file path
# $2 is command to run
define make_with_tracking_file
	$(_hide_cmds)$(call log_command,touch $1)
	$(_hide_cmds)$(call log_command,rm $1)
	$(_hide_cmds)$(call log_command,$2)
	$(_hide_cmds)$(call log_command,touch $1)
endef
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_codegen_helper.py sha256=2e74f9082b988d041ed3fe456ceb76f8df97db5b71bc932e4fb16a02dbf22fc4 bytes=57812 -->
## FILE: build/unit_tests/test_codegen_helper.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_codegen_helper.py`
- sha256: `2e74f9082b988d041ed3fe456ceb76f8df97db5b71bc932e4fb16a02dbf22fc4`
- bytes: 57812

````python
from build.helper.codegen_helper import *
from build.helper.codegen_helper import _get_buffer_parameters_for_size_parameter

# We need a config object for our testing
config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [
        {'file_name': 'custom_struct', 'python_name': 'CustomStruct', 'ctypes_type': 'custom_struct', },
    ],
}


# We also need some function parameters that cover all cases.
parameters_for_testing = [
    {  # 0
        'ctypes_method_call_snippet': 'vi_ctype',
        'ctypes_type': 'ViSession',
        'ctypes_type_library_call': 'ViSession',
        'ctypes_variable_name': 'vi_ctype',
        'direction': 'in',
        'documentation': {'description': 'Identifies a particular instrument session.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'vi',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': True,
        'interpreter_method_call_snippet': 'self._vi',
        'name': 'vi',
        'python_name': 'vi',
        'python_name_with_default': 'vi',
        'python_name_with_doc_default': 'vi',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViSession',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 1
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 2
        'ctypes_method_call_snippet': 'error_message_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'error_message_ctype',
        'direction': 'out',
        'documentation': {'description': 'The error information formatted into a string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'error_message',
        'is_buffer': False,
        'use_array': False,
        'use_list': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'error_message',
        'name': 'errorMessage',
        'python_name': 'error_message',
        'python_name_with_default': 'error_message',
        'python_name_with_doc_default': 'error_message',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 3
        'ctypes_method_call_snippet': 'array_out_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_out_ctype',
        'direction': 'out',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_out',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_out',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_out',
        'python_name_with_default': 'array_out',
        'python_name_with_doc_default': 'array_out',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 4
        'ctypes_method_call_snippet': 'number_of_elements_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements',
        'name': 'numberOfElements',
        'python_name': 'number_of_elements',
        'python_name_with_default': 'number_of_elements',
        'python_name_with_doc_default': 'number_of_elements',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 5
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt16)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 16 bit integers under the hood '},
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_array_raw',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 6
        'ctypes_method_call_snippet': 'an_int_enum_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_enum_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Indicates a ninja turtle',
            'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']]
        },
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_int_enum_raw',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int_enum',
        'name': 'anIntEnum',
        'python_name': 'an_int_enum',
        'python_name_with_default': 'an_int_enum',
        'python_name_with_doc_default': 'an_int_enum',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 7
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt64',
        'numpy': True,
        'numpy_type': 'int64',
        'numpy_type_library_call': 'numpy.int64',
        'use_in_python_api': True,
    },
    {  # 8
        'ctypes_method_call_snippet': 'number_of_elements_python_code_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_python_code_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array, determined via mechanism python-code.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements_python_code',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements_python_code',
        'name': 'numberOfElementsPythonCode',
        'numpy': False,
        'python_name': 'number_of_elements_python_code',
        'python_name_with_default': 'number_of_elements_python_code',
        'python_name_with_doc_default': 'number_of_elements_python_code',
        'python_type': 'int',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 9
        'ctypes_method_call_snippet': 'input_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'input_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input value.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input',
        'name': 'input',
        'numpy': False,
        'python_name': 'input',
        'python_name_with_default': 'input',
        'python_name_with_doc_default': 'input',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'use_in_python_api': True,
    },
    {  # 10
        'ctypes_method_call_snippet': 'input_array_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array',
        'name': 'inputArray',
        'numpy': False,
        'python_name': 'input_array',
        'python_name_with_default': 'input_array=None',
        'python_name_with_doc_default': 'input_array=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 11
        'ctypes_method_call_snippet': 'input_array_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'input_array_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Size of inputArray'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_size',
        'name': 'inputArraySize',
        'numpy': False,
        'python_name': 'input_array_size',
        'python_name_with_default': 'input_array_size',
        'python_name_with_doc_default': 'input_array_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 12
        'ctypes_method_call_snippet': 'string_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aString'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size',
        'name': 'stringSize',
        'numpy': False,
        'python_name': 'string_size',
        'python_name_with_default': 'string_size',
        'python_name_with_doc_default': 'string_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 13
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 14
        'ctypes_method_call_snippet': 'timeout_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ViReal64',
        'ctypes_variable_name': 'timeout_ctype',
        'default_value': 1.0,
        'direction': 'in',
        'documentation': {'description': 'Timeout in seconds'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'timeout',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'timeout',
        'name': 'Timeout',
        'numpy': False,
        'python_name': 'timeout',
        'python_name_with_default': 'timeout=1.0',
        'python_name_with_doc_default': 'timeout=1.0',
        'python_type': 'float',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViReal64',
        'use_in_python_api': True,
        'python_api_converter_name': 'timedelta_converter_seconds_real64',
    },
    {  # 15
        'ctypes_method_call_snippet': 'channel_list_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'channel_list_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'The channel to configure. For more information, refer to `Channel String'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'channel_list',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': True,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'self._repeated_capability',
        'name': 'channelList',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_name': 'channel_list',
        'python_name_with_default': 'channel_list',
        'python_name_with_doc_default': 'channel_list',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 16
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'int',
        'size': {'mechanism': 'len', 'value': 'a_string'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 17
        'ctypes_method_call_snippet': 'array_in_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_in_ctype',
        'direction': 'in',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_in',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_in',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_in',
        'python_name_with_default': 'array_in',
        'python_name_with_doc_default': 'array_in',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'len', 'value': 'array_in'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 18
        'ctypes_method_call_snippet': 'an_int_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_ctype',
        'direction': 'out',
        'documentation': {
            'description': 'Indicates a ninja turtle',
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'an_int',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int',
        'name': 'anInt',
        'python_name': 'an_int',
        'python_name_with_default': 'an_int',
        'python_name_with_doc_default': 'an_int',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 19
        'ctypes_method_call_snippet': 'a_string_2_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_2_ctype',
        'direction': 'out',
        'documentation': {'description': 'A fixed size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_2',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_2',
        'name': 'aString2',
        'numpy': False,
        'python_name': 'a_string_2',
        'python_name_with_default': 'a_string_2',
        'python_name_with_doc_default': 'a_string_2',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 20
        'ctypes_method_call_snippet': 'a_string_3_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_3_ctype',
        'direction': 'out',
        'documentation': {'description': 'A python-code size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_3',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_3',
        'name': 'aStrin3g',
        'numpy': False,
        'python_name': 'a_string_3',
        'python_name_with_default': 'a_string_3',
        'python_name_with_doc_default': 'a_string_3',
        'python_type': 'str',
        'size': {'mechanism': 'python-code', 'value': 'string_size'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 21
        'ctypes_method_call_snippet': 'a_string_twist_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_twist',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_twist',
        'name': 'aStringTwist',
        'numpy': False,
        'python_name': 'a_string_twist',
        'python_name_with_default': 'a_string_twist',
        'python_name_with_doc_default': 'a_string_twist',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 22
        'ctypes_method_call_snippet': 'ctypes.pointer(output_twist_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output_twist',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output_twist',
        'name': 'output_twist',
        'python_name': 'output_twist',
        'python_name_with_default': 'output_twist',
        'python_name_with_doc_default': 'output_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 23
        'ctypes_method_call_snippet': 'string_size_twist_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_twist_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aStringTwist'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size_twist',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size_twist',
        'name': 'stringSizeTwist',
        'numpy': False,
        'python_name': 'string_size_twist',
        'python_name_with_default': 'string_size_twist',
        'python_name_with_doc_default': 'string_size_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 24
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferArray',
        'numpy': False,
        'python_name': 'a_buffer_array',
        'python_name_with_default': 'a_buffer_array',
        'python_name_with_doc_default': 'a_buffer_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 25
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferList',
        'numpy': False,
        'python_name': 'a_buffer_list',
        'python_name_with_default': 'a_buffer_list',
        'python_name_with_doc_default': 'a_buffer_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 26
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using an array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistArray',
        'numpy': False,
        'python_name': 'a_buffer_twist_array',
        'python_name_with_default': 'a_buffer_twist_array',
        'python_name_with_doc_default': 'a_buffer_twist_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 27
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistList',
        'numpy': False,
        'python_name': 'a_buffer_twist_list',
        'python_name_with_default': 'a_buffer_twist_list',
        'python_name_with_doc_default': 'a_buffer_twist_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 28
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 29
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 30
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_3_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_3',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray3',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_3',
        'python_name_with_default': 'input_array_3=None',
        'python_name_with_doc_default': 'input_array_3=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize3'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 31
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 32
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 33
        'ctypes_method_call_snippet': 'a_string_enum_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_enum_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string-valued enum.'},
        'enum': 'Color',
        'grpc_enum': 'Color',
        'grpc_name': 'a_string_enum_raw',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_enum',
        'name': 'aStringEnum',
        'numpy': False,
        'python_name': 'a_string_enum',
        'python_name_with_default': 'a_string_enum',
        'python_name_with_doc_default': 'a_string_enum',
        'python_type': 'enums.Color',
        'size': {'mechanism': 'len', 'value': 'a_string_enum'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 34
        'ctypes_method_call_snippet': 'indices_ctype',
        'ctypes_type': 'ViConstString',
        'ctypes_type_library_call': 'ViConstString',
        'ctypes_variable_name': 'indices_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Specifies a list of indices for the channels in the session.'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'indices',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'indices',
        'name': 'indices',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
        'python_name': 'indices',
        'python_name_with_default': 'indices',
        'python_name_with_doc_default': 'indices',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViConstString',
        'use_in_python_api': True,
    },
    {  # 35
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt8',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt8)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 8 bit integers under the hood '},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_grpc_array',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_api_converter_name': 'convert_to_bytes',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt8',
        'numpy': False,
        'use_in_python_api': True,
    },
]


def test_get_library_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_library_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return int(output_ctype.value)'


def test_get_library_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return error_message_ctype.value.decode(self._encoding)'


def test_get_library_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]'


def test_get_library_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]'


def test_get_library_interpreter_method_return_snippet_into():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_grpc_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_grpc_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.output'


def test_get_grpc_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.error_message'


def test_get_grpc_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(x) for x in response.array_out]'


def test_get_grpc_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(x) for x in response.an_array_raw]'


def test_get_grpc_interpreter_method_return_snippet_bytes():
    param = [parameters_for_testing[35]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.a_grpc_array'


def test_get_session_method_return_snippet():
    param = [dict(parameters_for_testing[14])]
    param[0]['direction'] = 'out'
    assert get_session_method_return_snippet(param, config_for_testing) == 'return _converters.timedelta_converter_seconds_real64(timeout)'


def test_get_session_method_return_snippet_non_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing) == 'return output'


def test_get_session_method_return_snippet_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_enum_type_check_snippet():
    param = parameters_for_testing[6]
    assert get_enum_type_check_snippet(param, 0) == "if type(an_int_enum) is not enums.Turtle:\nraise TypeError('Parameter an_int_enum must be of type ' + str(enums.Turtle))"


def test_get_buffer_parameters_for_size_parameter_none():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[0], parameters_for_testing)
    assert len(params) == 0


def test_get_buffer_parameters_for_size_parameter():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[4], parameters_for_testing)
    assert params[0] == parameters_for_testing[5]


def test_get_ctype_variable_declaration_snippet_case_c010():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[15], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010"]


def test_get_ctype_variable_declaration_snippet_case_c020():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[16], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020"]


def test_get_ctype_variable_declaration_snippet_case_c030():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[33], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_enum_ctype = ctypes.create_string_buffer(a_string_enum.value.encode(self._encoding))  # case C030"]


def test_get_ctype_variable_declaration_snippet_case_c050():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = None  # case C050"]


def test_get_ctype_variable_declaration_snippet_case_c060():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060"]


def test_get_ctype_variable_declaration_snippet_case_c070():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[19], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_2_ctype = (_visatype.ViChar * 256)()  # case C070"]


def test_get_ctype_variable_declaration_snippet_case_c080():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[20], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_3_ctype = (_visatype.ViChar * string_size)()  # case C080"]


def test_get_ctype_variable_declaration_snippet_case_c090():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = None  # case C090"]


def test_get_ctype_variable_declaration_snippet_case_c100():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = (_visatype.ViChar * output_twist_ctype.value)()  # case C100"]


def test_get_ctype_variable_declaration_snippet_case_s110():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[0], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["vi_ctype = _visatype.ViSession(self._vi)  # case S110"]


def test_get_ctype_variable_declaration_snippet_case_s120():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[8], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_python_code_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120"]


def test_get_ctype_variable_declaration_snippet_case_s130():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[6], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130"]


def test_get_ctype_variable_declaration_snippet_case_s150():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[9], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_ctype = _visatype.ViInt16(input)  # case S150"]


def test_get_ctype_variable_declaration_snippet_case_s160():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[11], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert actual == ["input_array_size_ctype = _visatype.ViInt32(0 if input_array is None else len(input_array))  # case S160"]


def test_get_ctype_variable_declaration_snippet_case_s161():
    parameters_with_multidim_buffer = list(parameters_for_testing)
    # Create a copy to add 'array_dimensions' without modifying original parameters_for_testing[10]
    buffer_parameter = dict(parameters_with_multidim_buffer[10])
    buffer_parameter['array_dimensions'] = 3
    parameters_with_multidim_buffer[10] = buffer_parameter
    snippet = get_ctype_variable_declaration_snippet(parameters_with_multidim_buffer[11], parameters_with_multidim_buffer, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_array_size_ctype = _visatype.ViInt32(0 if input_array is None else input_array.size)  # case S161"]


def test_get_ctype_variable_declaration_snippet_case_s170():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32()  # case S170"]


def test_get_ctype_variable_declaration_snippet_case_s180():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32(error_code)  # case S180"]


def test_get_ctype_variable_declaration_snippet_case_s2190():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(0)  # case S190"]


def test_get_ctype_variable_declaration_snippet_case_s200():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(output_twist_ctype.value)  # case S200"]


def test_get_ctype_variable_declaration_snippet_case_s210():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[4], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210"]


def test_get_ctype_variable_declaration_snippet_case_s220():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[1], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["output_ctype = _visatype.ViInt64()  # case S220"]


def test_get_ctype_variable_declaration_snippet_case_b510():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=True)
    assert snippet == ["output_ctype = _get_ctypes_pointer_for_buffer(value=output)  # case B510"]


def test_get_ctype_variable_declaration_snippet_case_b540():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[17], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["array_in_ctype = _get_ctypes_pointer_for_buffer([custom_struct.custom_struct(c) for c in array_in], library_type=custom_struct.custom_struct)  # case B540"]


def test_get_ctype_variable_declaration_snippet_case_b550_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[10], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'input_array_array = _convert_to_array(value=input_array, array_type="d")  # case B550',
        'input_array_ctype = _get_ctypes_pointer_for_buffer(value=input_array_array, library_type=_visatype.ViReal64)  # case B550',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b550_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[28], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_array_2_ctype = _get_ctypes_pointer_for_buffer(value=input_array_2, library_type=_visatype.ViReal64)  # case B550"]


def test_get_ctype_variable_declaration_snippet_case_b560():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[3], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'array_out_size = self.get_array_size_for_python_code()  # case B560',
        'array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.custom_struct, size=array_out_size)  # case B560',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b570():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[18], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'an_int_size = 256  # case B570',
        'an_int_array = array.array("h", [0]) * an_int_size  # case B570',
        'an_int_ctype = _get_ctypes_pointer_for_buffer(value=an_int_array, library_type=_visatype.ViInt16)  # case B570',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_array_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_array_size = string_size_ctype.value  # case B590',
        'a_buffer_array_array = array.array("l", [0]) * a_buffer_array_size  # case B590',
        'a_buffer_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_array_array, library_type=_visatype.ViInt32)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_list_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_list_size = string_size_ctype.value  # case B590',
        'a_buffer_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_list_size)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b600():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'output_size = number_of_elements  # case B600',
        'output_array = array.array("q", [0]) * output_size  # case B600',
        'output_ctype = _get_ctypes_pointer_for_buffer(value=output_array, library_type=_visatype.ViInt64)  # case B600',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_array_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_array_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_array_array = array.array("l", [0]) * a_buffer_twist_array_size  # case B620',
        'a_buffer_twist_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_twist_array_array, library_type=_visatype.ViInt32)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_list_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_list_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_twist_list_size)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_bad_ivi_dance_step():
    try:
        get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
        assert False
    except AssertionError:
        pass


# TODO(marcoskirsch): unit tests for reamining cases of get_ctype_variable_declaration_snippet(): parameter is a buffer.


def test_get_enum_value_snippet():
    assert get_enum_value_snippet(None) == 'None'
    assert get_enum_value_snippet(True) == 'True'
    assert get_enum_value_snippet(0) == '0'
    assert get_enum_value_snippet('True') == "'True'"
    assert get_enum_value_snippet('0') == "'0'"
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_documentation_helper.py sha256=3564c0dcc73b3462e2c3a645716d1b4dfc3a0703f08444eedede123a2fb3d760 bytes=29424 -->
## FILE: build/unit_tests/test_documentation_helper.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_documentation_helper.py`
- sha256: `3564c0dcc73b3462e2c3a645716d1b4dfc3a0703f08444eedede123a2fb3d760`
- bytes: 29424

````python
from build.helper.documentation_helper import *


def _remove_trailing_whitespace(s):
    '''Removes trailing whitespace and empty lines in multi-line strings.'''
    initial_lines = s.strip().splitlines()
    fixed_lines = []
    blank_lines = 0
    for line in initial_lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0 and blank_lines == 0:
            fixed_lines.append(stripped_line)
            blank_lines = 1
        if len(stripped_line) > 0:
            fixed_lines.append(stripped_line)
            blank_lines = 0

    return fixed_lines


def assert_rst_strings_are_equal(expected, actual):
    '''Asserts rst formatted strings (multiline) are equal. Ignores trailing whitespace and empty lines.'''
    expected = _remove_trailing_whitespace(expected)
    actual = _remove_trailing_whitespace(actual)
    for expected_line, actual_line in zip(expected, actual):
        assert expected_line == actual_line, f'Difference found:\n{expected_line}\n{actual_line}'


config = {
    'functions': {
        'GetTurtleID': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'python_name': 'vi',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'interpreter_method_call_snippet': 'self._vi',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'in',
                    'enum': 'Turtle',
                    'name': 'turtleType',
                    'type': 'ViInt32',
                    'documentation': {
                        'description': '''Specifies the type of Turtle type
wanted to choose.''',
                        'note': 'You wont be able to import NIFAKE_VAL_RAPHAEL',
                        'table_body': [
                            ['NIFAKE_VAL_LEONARDO (default)', '0', 'LEONARDO'],
                            ['NIFAKE_VAL_DONATELLO', '1', 'DONATELLO'],
                            ['NIFAKE_VAL_RAPHAEL', '2', 'RAPHAEL'],
                            ['NIFAKE_VAL_MICHELANGELO', '3', 'MICHELANGELO']
                        ]
                    },
                    'python_name': 'turtle_type',
                    'python_type': 'Turtle',
                    'type_in_documentation': 'Turtle',
                    'type_in_documentation_was_calculated': True,
                    'ctypes_variable_name': 'turtle_type_ctype',
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'turtle_type',
                    'python_name_with_doc_default': 'turtle_type',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'turtle_type',
                    'use_in_python_api': True,
                },
                {
                    'direction': 'out',
                    'enum': None,
                    'name': 'turtleId',
                    'type': 'ViReal64',
                    'documentation': {
                        'description': 'Returns the **ID** of selected turtle.'
                    },
                    'python_name': 'turtle_id',
                    'python_type': 'float',
                    'type_in_documentation': 'float',
                    'type_in_documentation_was_calculated': True,
                    'ctypes_variable_name': 'turtleId_ctype',
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'python_name_with_default': 'turtleId',
                    'python_name_with_doc_default': 'turtleId',
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'ctypes.pointer(turtleId_ctype)',
                    'use_in_python_api': True,
                }
            ],
            'documentation': {
                'description': 'Returns the **ID** of selected Turtle Type. See `NIFAKE help <REPLACE_DRIVER_SPECIFIC_URL_1(fake_functional_overview)>`__',
                'note': [
                    'The NIFAKE_VAL_RAPHAEL Turtles dont have an ID.',
                    'DO NOT call niFake_FetchWaveform after calling this function.',
                    'NIFAKE_ATTR_READ_WRITE_BOOL will have an incorrect value after this calling this function',
                ]
            },
            'name': 'GetTurtleID',
            'python_name': 'get_turtle_id',
            'interpreter_name': 'get_turtle_id',
            'is_error_handling': False,
            'has_repeated_capability': False
        },
        'FetchWaveform': {
            'codegen_method': 'public',
            'documentation': {'description': 'Returns waveform data.'},
            'has_repeated_capability': False,
            'is_error_handling': False,
            'method_templates': [{'filename': '/default_method', 'method_python_name_suffix': ''}, {'filename': '/numpy_method', 'method_python_name_suffix': '_into'}],
            'name': 'FetchWaveform',
            'parameters': [
                {
                    'ctypes_type': 'ViSession',
                    'ctypes_type_library_call': 'ViSession',
                    'ctypes_variable_name': 'vi_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Identifies a particular instrument session.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'interpreter_method_call_snippet': 'vi_ctype',
                    'name': 'vi',
                    'numpy': False,
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViSession',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ViInt32',
                    'ctypes_variable_name': 'number_of_samples_ctype',
                    'direction': 'in',
                    'documentation': {'description': 'Number of samples to return'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'number_of_samples_ctype',
                    'name': 'numberOfSamples',
                    'numpy': False,
                    'python_name': 'number_of_samples',
                    'python_name_with_default': 'number_of_samples',
                    'python_name_with_doc_default': 'number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViReal64',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
                    'ctypes_variable_name': 'waveform_data_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Samples fetched from the device. Array should be numberOfSamples big.'},
                    'enum': None,
                    'is_buffer': True,
                    'is_string': False,
                    'use_list': False,
                    'use_array': True,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'waveform_data_ctype',
                    'name': 'waveformData',
                    'numpy': True,
                    'numpy_type': 'float64',
                    'original_type': 'ViReal64[]',
                    'python_name': 'waveform_data',
                    'python_name_with_default': 'waveform_data',
                    'python_name_with_doc_default': 'waveform_data',
                    'python_type': 'float',
                    'type_in_documentation': 'float',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'passed-in', 'value': 'numberOfSamples'},
                    'type': 'ViReal64',
                    'use_in_python_api': True,
                },
                {
                    'ctypes_type': 'ViInt32',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                    'ctypes_variable_name': 'actual_number_of_samples_ctype',
                    'direction': 'out',
                    'documentation': {'description': 'Number of samples actually fetched.'},
                    'enum': None,
                    'is_buffer': False,
                    'is_string': False,
                    'use_list': False,
                    'use_array': False,
                    'is_repeated_capability': False,
                    'is_session_handle': False,
                    'interpreter_method_call_snippet': 'ctypes.pointer(actual_number_of_samples_ctype)',
                    'name': 'actualNumberOfSamples',
                    'numpy': False,
                    'python_name': 'actual_number_of_samples',
                    'python_name_with_default': 'actual_number_of_samples',
                    'python_name_with_doc_default': 'actual_number_of_samples',
                    'python_type': 'int',
                    'type_in_documentation': 'int',
                    'type_in_documentation_was_calculated': True,
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViInt32',
                    'use_in_python_api': True,
                }
            ],
            'python_name': 'fetch_waveform',
            'interpreter_name': 'fetch_waveform',
            'render_in_session_base': False,
            'returns': 'ViStatus'
        },
    },
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '0.3.0.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'driver_urls': {
        'REPLACE_DRIVER_SPECIFIC_URL_1': 'http://zone.ni.com/reference/en-XX/help/370384T-01/fake/{0}/',
    },
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'attributes': {
        1000000: {
            'access': 'read-write',
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'type': 'ViBoolean',
            'documentation': {
                'description': 'An attribute of type bool with read/write access.',
            },
        },
    },
    'enums': {
        'Turtle': {
            'codegen_method': 'public',
            'python_name': 'Turtle',
            'values': [
                {
                    'name': 'NIFAKE_VAL_LEONARDO',
                    'python_name': 'LEONARDO',
                    'value': 0,
                    'documentation': {
                        'description': 'Wields two katanas.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_DONATELLO',
                    'python_name': 'DONATELLO',
                    'value': 1,
                    'documentation': {
                        'description': 'Uses a bo staff.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_RAPHAEL',
                    'python_name': 'RAPHAEL',
                    'value': 2,
                    'documentation': {
                        'description': 'Has a pair of sai.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_MICHELANGELO',
                    'python_name': 'MICHELANGELO',
                    'value': 3,
                    'documentation': {
                        'description': 'Owns nunchucks.',
                    }
                },
            ],
        },
    },
}


def test_get_function_rst_default():
    function = config['functions']['GetTurtleID']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: get_turtle_id(turtle_type)

    Returns the **ID** of selected Turtle Type. See `NIFAKE help <http://zone.ni.com/reference/en-XX/help/370384T-01/fake/fake_functional_overview/>`__

    .. note:: The :py:data:`~nifake.Turtle.RAPHAEL` Turtles dont have an ID.

    .. note:: DO NOT call :py:meth:`nifake.Session.fetch_waveform` after calling this method.

    .. note:: :py:attr:`nifake.Session.read_write_bool` will have an incorrect value after this calling this method

    :param turtle_type:

    Specifies the type of Turtle type
    wanted to choose.

    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.LEONARDO` (default) | 0 | LEONARDO     |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.DONATELLO`          | 1 | DONATELLO    |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.RAPHAEL`            | 2 | RAPHAEL      |
    +----------------------------------------------+---+--------------+
    | :py:data:`~nifake.Turtle.MICHELANGELO`       | 3 | MICHELANGELO |
    +----------------------------------------------+---+--------------+

    .. note:: You wont be able to import :py:data:`~nifake.Turtle.RAPHAEL`

    :type turtle_type: :py:data:`nifake.Turtle`

    :rtype: float
    :return:

        Returns the **ID** of selected turtle.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_function_rst_numpy():
    function = config['functions']['FetchWaveform']
    method_template = function['method_templates'][0]
    actual_function_rst = get_function_rst(function, method_template=method_template, numpy=True, config=config, indent=0)
    expected_fuction_rst = '''.. py:method:: fetch_waveform(number_of_samples)

    Returns waveform data.

    :param number_of_samples:

        Number of samples to return

    :type number_of_samples: int
    :param waveform_data:

        Samples fetched from the device. Array should be numberOfSamples big.

    :type waveform_data: numpy.array(dtype=numpy.float64)

    :rtype: int
    :return:

        Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_rst, actual_function_rst)


def test_get_attribute_repeated_caps():
    attr = {'supported_rep_caps': ['channels', 'instruments', 'pins']}
    expected_caps = 'channels, instruments, pins'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels']}
    expected_caps = 'channels'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': []}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps

    attr = {}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps(attr)
    assert actual_caps == expected_caps


def test_get_attribute_repeated_caps_with_conjunction():
    attr = {'supported_rep_caps': ['channels', 'instruments', 'pins']}
    expected_caps = 'channels, instruments or pins'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels', 'instruments']}
    expected_caps = 'channels or instruments'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': ['channels']}
    expected_caps = 'channels'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps

    attr = {'supported_rep_caps': []}
    expected_caps = 'None'
    actual_caps = get_attribute_repeated_caps_with_conjunction(attr)
    assert actual_caps == expected_caps


def test_module_supports_repeated_caps():
    config = {'repeated_capabilities': [{'python_name': 'channels'}]}
    expected_value = True
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value

    config = {'repeated_capabilities': []}
    expected_value = False
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value

    config = {}
    expected_value = False
    actual_value = module_supports_repeated_caps(config)
    assert actual_value == expected_value


def test_get_function_docstring_default():
    function = config['functions']['GetTurtleID']
    actual_function_docstring = get_function_docstring(function, numpy=False, config=config, indent=0)
    expected_function_docstring = '''Returns the **ID** of selected Turtle Type. See `NIFAKE help <fake_functional_overview>`__

Note: The Turtle.RAPHAEL Turtles dont have an ID.

Note: DO NOT call fetch_waveform after calling this method.

Note: read_write_bool will have an incorrect value after this calling this method

Args:
    turtle_type (Turtle): Specifies the type of Turtle type
        wanted to choose.

        +---------------------------+---+--------------+
        | Turtle.LEONARDO (default) | 0 | LEONARDO     |
        +---------------------------+---+--------------+
        | Turtle.DONATELLO          | 1 | DONATELLO    |
        +---------------------------+---+--------------+
        | Turtle.RAPHAEL            | 2 | RAPHAEL      |
        +---------------------------+---+--------------+
        | Turtle.MICHELANGELO       | 3 | MICHELANGELO |
        +---------------------------+---+--------------+

        Note: You wont be able to import Turtle.RAPHAEL

Returns:
    turtle_id (float): Returns the **ID** of selected turtle.''' # noqa
    assert_rst_strings_are_equal(expected_function_docstring, actual_function_docstring)


def test_get_function_docstring_numpy():
    function = config['functions']['FetchWaveform']
    actual_function_docstring = get_function_docstring(function, numpy=True, config=config, indent=0)
    expected_fuction_docstring = '''Returns waveform data.

    Args:
        number_of_samples (int): Number of samples to return

        waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

    Returns:
        actual_number_of_samples (int): Number of samples actually fetched.
'''
    assert_rst_strings_are_equal(expected_fuction_docstring, actual_function_docstring)


def test_get_rst_header_snippet():
    header = "This will be your method header"
    actual_rst_header = get_rst_header_snippet(header)
    expected_rst_header = """This will be your method header
==============================="""
    assert actual_rst_header == expected_rst_header


def test_get_documentation_for_node_docstring():
    caution = """ this is a very
long string if I had the
energy to type more and more ..."""
    description = """ This string might be
at maximum size I can handle"""
    node = {
        'documentation': {
            'caution': caution,
            'description': description,
            'table_header': ['what', 'how', 'who'],
            'table_body': [
                ['lorem', 'that is a dummy string', 'Place holder string'],
                ['ipsum', 'this is a random strinf', 'Yes, I am a random string']
            ]
        }
    }
    actual_documentation = get_documentation_for_node_docstring(node, config, indent=4)
    expected_documentation = """Caution:  this is a very
    long string if I had the
    energy to type more and more ...

    This string might be
    at maximum size I can handle

    +-------+-------------------------+---------------------------+
    | what  | how                     | who                       |
    +=======+=========================+===========================+
    | lorem | that is a dummy string  | Place holder string       |
    +-------+-------------------------+---------------------------+
    | ipsum | this is a random strinf | Yes, I am a random string |
    +-------+-------------------------+---------------------------+""" # noqa
    assert_rst_strings_are_equal(expected_documentation, actual_documentation)


def test_get_rst_picture_reference():
    actual_pic_ref = get_rst_picture_reference('test1', 'test2', 'test3', 'test4')
    expected_pic_ref = """
    .. |test1| image:: test2
        :alt: test3
        :target: test4
    """
    assert_rst_strings_are_equal(expected_pic_ref, actual_pic_ref)


def test_square_up_tables():
    local_config = config_for_testing.copy()
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
                'table_header': ['Just one'],
                'table_body': [['Just', 'two'], ['this', 'has', 'three']],
            },
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = {}
    local_config['enums'] = {}

    square_up_tables(local_config)
    assert len(local_config['functions']['MakeAFoo']['documentation']['table_header']) == 3
    for line in local_config['functions']['MakeAFoo']['documentation']['table_body']:
        assert len(line) == 3


config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [],
}


def test_add_notes_re_links():
    local_config = config_for_testing.copy()
    local_config['c_function_prefix'] = 'niFake'
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session for niFake_MakeAFoo using NIFAKE_ATTR_READ_WRITE_BOOL. You should use NIFAKE_VAL_BLUE',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on. Similar to niFake_TakeAFoo using NIFAKE_ATTR_NOT_HERE. Use NIFAKE_VAL_PURPLE',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
            },
            'python_name': 'make_a_foo',
            'interpreter_name': 'make_a_foo',
        },
    }
    attributes = {
        1000000: {
            'access': 'read-write',
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'type': 'ViBoolean',
            'documentation': {
                'description': 'An attribute of type bool with read/write access.',
            },
        },
    }
    enums = {
        'Color': {
            'values': [
                {
                    'name': 'NIFAKE_VAL_RED',
                    'value': 1,
                    'documentation': {
                        'description': 'Like blood.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLUE',
                    'value': 2,
                    'documentation': {
                        'description': 'Like the sky.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_YELLOW',
                    'value': 2,
                    'documentation': {
                        'description': 'Like a banana.',
                    }
                },
                {
                    'name': 'NIFAKE_VAL_BLACK',
                    'value': 2,
                    'documentation': {
                        'description': 'Like this developer\'s conscience.',
                    }
                },
            ],
            'codegen_method': 'public',
        },
    }
    local_config['functions'] = functions
    local_config['attributes'] = attributes
    local_config['enums'] = enums

    add_notes_re_links(local_config)

    assert 'note' not in local_config['functions']['MakeAFoo']['parameters'][0]['documentation']
    assert func_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert attr_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
    assert enum_note_text in local_config['functions']['MakeAFoo']['parameters'][1]['documentation']['note']
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_documentation_snippets.py sha256=1de1249336744af6ae9cadb77100b0697ab5c86b5dbc4146d1ec0a844d7f4556 bytes=3258 -->
## FILE: build/unit_tests/test_documentation_snippets.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_documentation_snippets.py`
- sha256: `1de1249336744af6ae9cadb77100b0697ab5c86b5dbc4146d1ec0a844d7f4556`
- bytes: 3258

````python
from build.helper.documentation_snippets import *


def test_close_function_def_for_doc_note_not_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
                'note': 'test',
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict
    return


def test_close_function_def_for_doc_note_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
                'note': ['test'],
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict
    return


def test_close_function_def_for_doc_no_note():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'close': {
            'documentation': {
                'description': 'test',
            },
        },
    }
    config = {
        'close_function': 'close'
    }
    close_doc = close_function_def_for_doc(functions, config)
    assert type(close_doc) is dict


def test_initiate_function_def_for_doc_note_not_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
                'note': 'test',
            },
            'python_name': '_initiate',
        },
    }
    config = {
        'context_manager_name': {
            'task': 'acquisition',
            'initiate_function': 'Initiate',
            'abort_function': 'Abort',
        },
    }
    initiate_doc = initiate_function_def_for_doc(functions, config)
    assert type(initiate_doc) is dict
    return


def test_initiate_function_def_for_doc_note_list():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
                'note': ['test'],
            },
            'python_name': '_initiate',
        },
    }
    config = {
        'context_manager_name': {
            'task': 'acquisition',
            'initiate_function': 'Initiate',
            'abort_function': 'Abort',
        },
    }
    initiate_doc = initiate_function_def_for_doc(functions, config)
    assert type(initiate_doc) is dict
    return


def test_initiate_function_def_for_doc_no_note():
    '''Testing for lack of syntax error - not actual documentation'''
    functions = {
        'Initiate': {
            'documentation': {
                'description': 'test',
            },
            'python_name': '_initiate',
        },
    }
    config = {
        'context_manager_name': {
            'task': 'acquisition',
            'initiate_function': 'Initiate',
            'abort_function': 'Abort',
        },
    }
    initiate_doc = initiate_function_def_for_doc(functions, config)
    assert type(initiate_doc) is dict
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_helper.py sha256=5130f8d958f6e7607e62f4d4d4ea5b52a1bd53b52d55e75ec4acd801c3cbe3c4 bytes=4433 -->
## FILE: build/unit_tests/test_helper.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_helper.py`
- sha256: `5130f8d958f6e7607e62f4d4d4ea5b52a1bd53b52d55e75ec4acd801c3cbe3c4`
- bytes: 4433

````python
from build.helper.helper import *


def test_get_development_status():
    config = {}

    config['module_version'] = '0.0.0.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.0.0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.4.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.4.9'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '0.5.0.dev0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.5.0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.9.9.dev0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '0.9.9'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.0.0.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.0.0.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.0.0'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '1.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '1.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '1.9.9'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '9.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '9.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '9.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '9.9.9'
    assert get_development_status(config) == '5 - Production/Stable'

    config['module_version'] = '19.9.9.dev0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '19.9.9.a0'
    assert get_development_status(config) == '3 - Alpha'

    config['module_version'] = '19.9.9.b0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9.c0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9.rc0'
    assert get_development_status(config) == '4 - Beta'

    config['module_version'] = '19.9.9'
    assert get_development_status(config) == '5 - Production/Stable'


def test_enum_uses_converter():
    import pytest

    assert not enum_uses_converter({})
    assert not enum_uses_converter({
        'enum_to_converted_value_function_name': None,
        'converted_value_to_enum_function_name': None
    })

    assert enum_uses_converter({
        'enum_to_converted_value_function_name': lambda x: x,
        'converted_value_to_enum_function_name': lambda x: x
    })

    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'converted_value_to_enum_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': None,
            'converted_value_to_enum_function_name': lambda x: x
        })
    with pytest.raises(AssertionError):
        enum_uses_converter({
            'enum_to_converted_value_function_name': lambda x: x,
            'converted_value_to_enum_function_name': None
        })
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_metadata_add_all.py sha256=b4042689eb19fadb3ef133076c9175de07857cd93b15df16a11d6c5f6cff3a52 bytes=46569 -->
## FILE: build/unit_tests/test_metadata_add_all.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_metadata_add_all.py`
- sha256: `b4042689eb19fadb3ef133076c9175de07857cd93b15df16a11d6c5f6cff3a52`
- bytes: 46569

````python
from build.helper.metadata_add_all import *
from build.helper.metadata_add_all import _add_enum_codegen_method
from build.helper.metadata_add_all import _get_attributes_that_use_enums
from build.helper.metadata_add_all import _get_functions_that_use_enums
from build.helper.metadata_add_all import _get_least_restrictive_codegen_method


def _compare_values(actual, expected, k):
    if type(actual) is dict:
        _compare_dicts(actual, expected)
    elif type(actual) is list:
        _compare_lists(actual, expected)
    else:
        assert actual == expected, f"Value mismatch with key/index '{k}', {actual} != {expected}"


def _compare_lists(actual, expected):
    assert isinstance(actual, type(expected)), f'Type mismatch, {type(actual)} != {type(expected)}'
    assert len(actual) == len(expected), f'Length mismatch, {len(actual)} != {len(expected)}'
    for k in range(len(actual)):
        _compare_values(actual[k], expected[k], k)


def _compare_dicts(actual, expected):
    assert isinstance(actual, type(expected)), f'Type mismatch, {type(actual)} != {type(expected)}'
    for k in actual:
        assert k in expected, f'Key {k} not in expected'
        _compare_values(actual[k], expected[k], k)
    for k in expected:
        assert k in actual, f'Key {k} not in actual'


functions_input = {
    'MakeAFoo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'python_name': 'name',
                'is_repeated_capability': False,
                'type': 'ViString',
                'documentation': {
                    'description': 'The channel to call this on.',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'enum': None,
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'enum': None,
                'name': 'pythonCodeInput',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'enum': None,
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'enum': None,
                'name': 'customTypeInput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'enum': None,
                'name': 'customTypeOutput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixInput',
                'type': 'CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixOutput',
                'type': 'CustomStruct'
            },
        ],
        'documentation': {
            'description': 'Performs a foo, and performs it well.',
        },
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'enum': None,
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize'
                },
                'type': 'ViUInt32[]'
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined',
        },
    },
    'MakeANoCodegenMethod': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'This is a method with codegen_method set to no',
        },
        'method_name_for_documentation': 'MakeAPublicMethod',
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': '',
            },
        ],
        'parameters': [],
        'returns': 'ViStatus',
    },
}


functions_expected = {
    'MakeAFoo': {
        'name': 'MakeAFoo',
        'codegen_method': 'public',
        'use_session_lock': True,
        'documentation': {
            'description': 'Performs a foo, and performs it well.'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type_library_call': 'ViSession',
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'is_repeated_capability': False,
                'is_session_handle': True,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'vi',
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViSession',
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'name_ctype',
                'ctypes_type': 'ViString',
                'ctypes_variable_name': 'name_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'direction': 'in',
                'documentation': {
                    'description': 'The channel to call this on.'
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'name': 'channelName',
                'grpc_name': 'name',
                'python_name': 'name',
                'python_name_with_default': 'name',
                'python_name_with_doc_default': 'name',
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'ViString',
                'interpreter_method_call_snippet': 'name',
                'grpc_request_snippet': 'name=name',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'name',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'pin_data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'pin_data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pinDataBufferSize',
                'grpc_name': 'pin_data_buffer_size',
                'python_name': 'pin_data_buffer_size',
                'python_name_with_default': 'pin_data_buffer_size',
                'python_name_with_doc_default': 'pin_data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'pin_data_buffer_size',
                'grpc_request_snippet': 'pin_data_buffer_size=pin_data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'pin_data_buffer_size',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'python_code_input_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'python_code_input_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pythonCodeInput',
                'grpc_name': 'python_code_input',
                'python_name': 'python_code_input',
                'python_name_with_default': 'python_code_input',
                'python_name_with_doc_default': 'python_code_input',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'python_code_input',
                'grpc_request_snippet': 'python_code_input=2 ** 14',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'python_code_input',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype))',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'actual_num_pin_data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'actualNumPinData',
                'grpc_name': 'actual_num_pin_data',
                'python_name': 'actual_num_pin_data',
                'python_name_with_default': 'actual_num_pin_data',
                'python_name_with_doc_default': 'actual_num_pin_data',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'actual_num_pin_data',
                'grpc_request_snippet': 'actual_num_pin_data=actual_num_pin_data',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'actual_num_pin_data',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'expected_pin_states_ctype',
                'ctypes_type': 'ViUInt8',
                'ctypes_variable_name': 'expected_pin_states_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt8)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'expectedPinStates',
                'original_type': 'ViUInt8[]',
                'grpc_name': 'expected_pin_states',
                'python_name': 'expected_pin_states',
                'python_name_with_default': 'expected_pin_states',
                'python_name_with_doc_default': 'expected_pin_states',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8',
                'interpreter_method_call_snippet': 'expected_pin_states',
                'grpc_request_snippet': 'expected_pin_states=expected_pin_states',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'expected_pin_states',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'custom_type_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeInput',
                'grpc_name': 'custom_type_input',
                'python_name': 'custom_type_input',
                'python_name_with_default': 'custom_type_input',
                'python_name_with_doc_default': 'custom_type_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_input',
                'grpc_request_snippet': 'custom_type_input=custom_type_input._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_input',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_output_ctype is None else (ctypes.pointer(custom_type_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeOutput',
                'grpc_name': 'custom_type_output',
                'python_name': 'custom_type_output',
                'python_name_with_default': 'custom_type_output',
                'python_name_with_doc_default': 'custom_type_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_output',
                'grpc_request_snippet': 'custom_type_output=custom_type_output._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_output',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixInput',
                'grpc_name': 'custom_type_without_struct_prefix_input',
                'python_name': 'custom_type_without_struct_prefix_input',
                'python_name_with_default': 'custom_type_without_struct_prefix_input',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_input',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_input=custom_type_without_struct_prefix_input._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_input',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_without_struct_prefix_output_ctype is None else (ctypes.pointer(custom_type_without_struct_prefix_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixOutput',
                'grpc_name': 'custom_type_without_struct_prefix_output',
                'python_name': 'custom_type_without_struct_prefix_output',
                'python_name_with_default': 'custom_type_without_struct_prefix_output',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_output',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_output=custom_type_without_struct_prefix_output._create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_output',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
        ],
        'python_name': 'make_a_foo',
        'interpreter_name': 'make_a_foo',
        'returns': 'ViStatus',
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'use_session_lock': True,
        'method_templates': [{'session_filename': '/default_method', 'library_interpreter_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'direction': 'in',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_type_library_call': 'ViSession',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'is_repeated_capability': False,
                'is_session_handle': True,
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'status_ctype',
                'direction': 'out',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status'
                },
                'grpc_name': 'status',
                'python_name': 'status',
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'status_ctype',
                'ctypes_type': 'ViString',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'python_name_with_default': 'status',
                'python_name_with_doc_default': 'status',
                'is_repeated_capability': False,
                'is_session_handle': False,
                'interpreter_method_call_snippet': 'status',
                'grpc_request_snippet': 'status=status',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'status',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'dataBufferSize',
                'grpc_name': 'data_buffer_size',
                'python_name': 'data_buffer_size',
                'python_name_with_default': 'data_buffer_size',
                'python_name_with_doc_default': 'data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'data_buffer_size',
                'grpc_request_snippet': 'data_buffer_size=data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'data_buffer_size',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
            {
                'ctypes_method_call_snippet': 'data_ctype',
                'ctypes_type': 'ViUInt32',
                'ctypes_variable_name': 'data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'data',
                'original_type': 'ViUInt32[]',
                'grpc_name': 'data',
                'python_name': 'data',
                'python_name_with_default': 'data',
                'python_name_with_doc_default': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize',
                },
                'type': 'ViUInt32',
                'interpreter_method_call_snippet': 'data',
                'grpc_request_snippet': 'data=data',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'data',
                'complex_array_representation': None,
                'array_dimensions': 1,
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined'
        },
        'name': 'MakeAPrivateMethod',
        'python_name': '_make_a_private_method',
        'interpreter_name': 'make_a_private_method',
        'is_error_handling': False,
        'render_in_session_base': False,
        'has_repeated_capability': False
    },
    'MakeANoCodegenMethod': {
        'name': 'MakeANoCodegenMethod',
        'codegen_method': 'no',
        'method_name_for_documentation': 'MakeAPublicMethod',
        'use_session_lock': True,
        'documentation': {
            'description': 'This is a method with codegen_method set to no'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': ''
            }
        ],
        'parameters': [],
        'python_name': 'make_a_no_codegen_method',
        'interpreter_name': 'make_a_no_codegen_method',
        'returns': 'ViStatus',
    }
}


attributes_input = {
    1000000: {
        'access': 'read-write',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'type': 'ViBoolean',
        'documentation': {
            'description': 'An attribute of type bool with read/write access.',
        },
    },
}


attributes_expected = {
    1000000: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {'description': 'An attribute of type bool with read/write access.'},
        'enum': None,
        'grpc_enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'python_name': 'read_write_bool',
        'type': 'ViBoolean',
        'python_type': 'bool',
        'type_in_documentation': 'bool',
        'type_in_documentation_was_calculated': True,
        'attribute_class': 'AttributeViBoolean',
    },
}


enums_input = {
    'Color': {
        'values': [
            {
                'name': 'RED',
                'value': 1,
                'documentation': {
                    'description': 'Like blood.',
                }
            },
            {
                'name': 'BLUE',
                'value': 2,
                'documentation': {
                    'description': 'Like the sky.',
                }
            },
            {
                'name': 'YELLOW',
                'value': 2,
                'documentation': {
                    'description': 'Like a banana.',
                }
            },
            {
                'name': 'BLACK',
                'value': 2,
                'documentation': {
                    'description': 'Like this developer\'s conscience.',
                }
            },
        ],
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {
                'converts_to_value': True,
                'name': 'RED',
                'value': 1
            },
            {
                'converts_to_value': False,
                'name': 'BLUE',
                'value': 2
            },
            {
                'converts_to_value': 'yellow',
                'name': 'YELLOW',
                'value': 5
            },
            {
                'converts_to_value': 42,
                'name': 'BLACK',
                'value': 42
            }
        ]
    },
}


enums_expected = {
    'Color': {
        'codegen_method': 'no',
        'python_name': 'Color',
        'values': [
            {'documentation': {'description': 'Like blood.'}, 'name': 'RED', 'value': 1, 'python_name': 'RED'},
            {'documentation': {'description': 'Like the sky.'}, 'name': 'BLUE', 'value': 2, 'python_name': 'BLUE'},
            {'documentation': {'description': 'Like a banana.'}, 'name': 'YELLOW', 'value': 2, 'python_name': 'YELLOW'},
            {'documentation': {'description': "Like this developer's conscience."}, 'name': 'BLACK', 'value': 2, 'python_name': 'BLACK'}
        ]
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'python_name': '_EnumWithConverter',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {'name': 'RED', 'value': 1, 'converts_to_value': True, 'python_name': 'RED'},
            {'name': 'BLUE', 'value': 2, 'converts_to_value': False, 'python_name': 'BLUE'},
            {'name': 'YELLOW', 'value': 5, 'converts_to_value': 'yellow', 'python_name': 'YELLOW'},
            {'name': 'BLACK', 'value': 42, 'converts_to_value': 42, 'python_name': 'BLACK'}
        ]
    },
}


config_input = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    # These are added here strictly for testing.
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
}


config_expected = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    'use_locking': True,
    'functions': functions_expected,
    'attributes': attributes_expected,
    'enums': enums_expected,
    'modules': {
        'metadata.enums_addon': {}
    },
    'uses_nitclk': False,
}


def _do_the_test_add_functions_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_functions_metadata_simple():
    _do_the_test_add_functions_metadata(functions=functions_input, expected=functions_expected)


def _do_the_test_add_attributes_metadata(attributes, expected):
    actual = copy.deepcopy(attributes)
    actual = add_all_attribute_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_attributes_metadata_simple():
    _do_the_test_add_attributes_metadata(attributes=attributes_input, expected=attributes_expected)


def _do_the_test_add_enums_metadata(enums, expected):
    actual = copy.deepcopy(enums)
    actual = add_all_enum_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_enums_metadata_simple():
    _do_the_test_add_enums_metadata(enums_input, expected=enums_expected)


def _do_the_test_add_all_metadata(functions, attributes, enums, config, expected):
    actual = add_all_metadata(functions, attributes, enums, config, persist_output=False)
    _compare_dicts(actual, expected)


def test_add_all_metadata_defaults():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=config_expected)


def test_add_all_metadata():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    actual_config['use_locking'] = False
    expected = copy.deepcopy(config_expected)
    expected['use_locking'] = False
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=expected)


def _setup_inputs_for_enum_codegen_method_tests():
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    # Set up minimal input functions metadata
    actual_config['functions'] = {
        'PublicMethod': {
            'codegen_method': 'public',
            'parameters': [{'enum': None}, {'enum': 'EnumWithConverter'}],
        },
        'PythonOnlyMethod': {
            'codegen_method': 'python-only',
            'parameters': [{'enum': 'Color'}, {'enum': None}],
        },
        'PrivateMethod': {
            'codegen_method': 'private',
            'parameters': [{'enum': 'EnumWithConverter'}],
        },
        'NoCodegenMethod': {
            'codegen_method': 'no',
            'parameters': [{'enum': 'Color'}],
        },
    }
    # Set up minimal input attributes metadata
    actual_config['attributes'] = {
        '1000000': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR', 'enum': None},
        '1000001': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000002': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR', 'enum': 'Color'},
        '1000003': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000004': {'codegen_method': 'no', 'name': 'NO_CODEGEN_ATTR', 'enum': 'Color'},
    }
    return actual_enums, actual_config


def test_add_enum_codegen_method():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    _add_enum_codegen_method(actual_enums, actual_config)
    assert actual_enums['Color']['codegen_method'] == 'public'
    assert actual_enums['EnumWithConverter']['codegen_method'] == 'private'


def test_add_enum_codegen_method_error():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    actual_enums['Color']['codegen_method'] = 'private'
    expected_error_description = "Codegen_method of enum Color used by functions ['PythonOnlyMethod'] and attributes ['PRIVATE_ATTR'] must be public, is private"
    try:
        _add_enum_codegen_method(actual_enums, actual_config)
    except ValueError as actual_error:
        actual_error_message = actual_error.args[0]
        assert actual_error_message == expected_error_description


def test_get_functions_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['PythonOnlyMethod'],
        'EnumWithConverter': ['PublicMethod', 'PrivateMethod'],
    }
    actual_output = _get_functions_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_attributes_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['1000002'],
        'EnumWithConverter': ['1000001', '1000003'],
    }
    actual_output = _get_attributes_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_least_restrictive_codegen_method():
    for codegen_methods, expected_least_restrictive_codegen_method in (
        ([], 'no'),
        (['no'], 'no'),
        (['private', 'private'], 'private'),
        (['no', 'private'], 'private'),
        (['public', 'private'], 'public'),
        (['private', 'python-only', 'private', 'no'], 'public'),
        (['public', 'python-only', 'public'], 'public')
    ):
        assert _get_least_restrictive_codegen_method(
            codegen_methods
        ) == expected_least_restrictive_codegen_method
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_metadata_filters.py sha256=17a9fd6aacb89bcac58eeefa6c085dbbd5891dafc0b224fb459d8214742c54d0 bytes=1747 -->
## FILE: build/unit_tests/test_metadata_filters.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_metadata_filters.py`
- sha256: `17a9fd6aacb89bcac58eeefa6c085dbbd5891dafc0b224fb459d8214742c54d0`
- bytes: 1747

````python
from build.helper.metadata_filters import filter_parameters
from build.helper.parameter_usage_options import ParameterUsageOptions


def _parameter(name, direction='in', mechanism='passed-in', size_value=None):
    size = {'mechanism': mechanism}
    if size_value is not None:
        size['value'] = size_value

    return {
        'name': name,
        'direction': direction,
        'size': size,
        'is_session_handle': False,
        'is_repeated_capability': False,
        'enum': None,
        'numpy': False,
        'use_in_python_api': True,
        'complex_array_representation': None,
    }


def test_filter_parameters_mixed_usage_ivi_dance_and_len():
    parameters = [
        _parameter('ivi_size'),
        _parameter('out_waveform', direction='out', mechanism='ivi-dance', size_value='ivi_size'),
        _parameter('len_size'),
        _parameter('len_data', mechanism='len', size_value='len_size'),
        _parameter('timeout'),
    ]

    filtered = filter_parameters(parameters, ParameterUsageOptions.SESSION_METHOD_DECLARATION)
    filtered_names = [parameter['name'] for parameter in filtered]

    assert filtered_names == ['len_data', 'timeout']


def test_filter_parameters_multiple_len_sizes():
    parameters = [
        _parameter('len_a_size'),
        _parameter('len_b_size'),
        _parameter('len_a_data', mechanism='len', size_value='len_a_size'),
        _parameter('len_b_data', mechanism='len', size_value='len_b_size'),
        _parameter('timeout'),
    ]

    filtered = filter_parameters(parameters, ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    filtered_names = [parameter['name'] for parameter in filtered]

    assert filtered_names == ['len_a_data', 'len_b_data', 'timeout']
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_metadata_find.py sha256=c631ce9a10130e7cc305fe843a9767c187d0fbae702be8ec2a8d5b15c1ea44e4 bytes=999 -->
## FILE: build/unit_tests/test_metadata_find.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_metadata_find.py`
- sha256: `c631ce9a10130e7cc305fe843a9767c187d0fbae702be8ec2a8d5b15c1ea44e4`
- bytes: 999

````python
from build.helper.metadata_find import find_len_size_parameter_names


def _parameter(name, mechanism='passed-in', size_value=None):
    size = {'mechanism': mechanism}
    if size_value is not None:
        size['value'] = size_value

    return {
        'name': name,
        'size': size,
    }


def test_find_len_size_parameter_names_multiple_sizes():
    parameters = [
        _parameter('len_a_size'),
        _parameter('len_b_size'),
        _parameter('len_a_data', mechanism='len', size_value='len_a_size'),
        _parameter('len_b_data', mechanism='len', size_value='len_b_size'),
        _parameter('timeout'),
    ]

    size_names = find_len_size_parameter_names(parameters)

    assert size_names == {'len_a_size', 'len_b_size'}


def test_find_len_size_parameter_names_empty_when_no_len_parameters():
    parameters = [
        _parameter('value'),
        _parameter('timeout'),
    ]

    size_names = find_len_size_parameter_names(parameters)

    assert size_names == set()
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/unit_tests/test_metadata_merge_dicts.py sha256=4a0d75ebce2c94d30d07f24b99f24216befbf9b00c0328314631eab1f547152c bytes=2422 -->
## FILE: build/unit_tests/test_metadata_merge_dicts.py

- repository: `ni/nimi-python`
- source_path: `build/unit_tests/test_metadata_merge_dicts.py`
- sha256: `4a0d75ebce2c94d30d07f24b99f24216befbf9b00c0328314631eab1f547152c`
- bytes: 2422

````python
from build.helper.metadata_merge_dicts import *


def _do_the_test_merge_dicts(a, b, expected, use_re):
    actual = a.copy()
    merge_dicts(actual, b, use_re, 'test')
    assert expected == actual, f"\na = {a}\nb = {b}\nexpected = {expected}\nactual = {actual}"


def test_merge_dict_second_is_empty():
    a = {'a': 1, 'b': 2}
    b = {}
    expected = {'a': 1, 'b': 2}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_key_exists():
    a = {'a': 1, 'b': 2}
    b = {'b': 3}
    expected = {'a': 1, 'b': 3}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_recurse():
    a = {'a': 1, 'b': {'b1': 5, 'b2': 6}}
    b = {'b': {'b3': 7}}
    expected = {'a': 1, 'b': {'b1': 5, 'b2': 6, 'b3': 7}}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_replace_in_list():
    a = {'a': 1, 'b': {'b1': 5, 'b2': 6}, 'c': ['x', 'y', 'z']}
    b = {'b': {'b3': 7, 'b1': 8}, 'c': {0: 'r', 1: 's', 2: 't'}}
    expected = {'a': 1, 'b': {'b1': 8, 'b2': 6, 'b3': 7}, 'c': ['r', 's', 't']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_replace_in_dict_and_list():
    a = {'a': 1, 'b': {'b1': 2, 'b2': 3}, 'c': ['x', 'y', 'z']}
    b = {'b': {'b3': 7, 'b1': 8}, 'c': {0: 'r', 1: 's', 2: 't'}}
    expected = {'a': 1, 'b': {'b1': 8, 'b2': 3, 'b3': 7}, 'c': ['r', 's', 't']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_with_regex():
    a = {'aaa': {}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    b = {'a+': {'z': 99}}
    expected = {'aaa': {'z': 99}, 'aaaa': {'x': 98, 'z': 99}, 'aaaaa': {'z': 99}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    _do_the_test_merge_dicts(a, b, expected, use_re=True)


def test_merge_dict_with_regex_off():
    a = {'aaa': {}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    b = {'aaa': {'z': 99}}
    expected = {'aaa': {'z': 99}, 'aaaa': {'x': 98}, 'aaaaa': {}, 'bbb': {'bbb1': 2, 'bbb2': 3}, 'ccc': ['x', 'y', 'z']}
    _do_the_test_merge_dicts(a, b, expected, use_re=False)


def test_merge_dict_top_level_key_missing():
    a = {'a': 1, 'b': 2}
    b = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    try:
        _do_the_test_merge_dicts(a, b, expected, use_re=True)
        assert False
    except KeyError:
        pass
````

<!--NI_OSS_SOURCE repo=nimi-python path=build/utilities.py sha256=5a5d396f2fd2adb972fd9fd067aceab8429d4ea381662c22995a90ac89a0921b bytes=1583 -->
## FILE: build/utilities.py

- repository: `ni/nimi-python`
- source_path: `build/utilities.py`
- sha256: `5a5d396f2fd2adb972fd9fd067aceab8429d4ea381662c22995a90ac89a0921b`
- bytes: 1583

````python
#!/usr/bin/python3

from contextlib import contextmanager
import importlib
import logging
import os
import sys


# From https://stackoverflow.com/questions/41861427/python-3-5-how-to-dynamically-import-a-module-given-the-full-file-path-in-the
@contextmanager
def add_to_path(p):
    import sys
    logging.debug("Adding path %s" % p)
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        logging.debug("Removing path %s" % p)
        sys.path = old_path


def path_import(absolute_path):
    '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
    if not os.path.isabs(absolute_path):
        absolute_path = os.path.join(sys.path[0], absolute_path)
    logging.debug("Importing %s" % absolute_path)
    with add_to_path(os.path.dirname(absolute_path)):
        module = importlib.import_module(os.path.basename(absolute_path))
        return module


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    # Remove all handlers. We will add our own
    while root.handlers:
        root.handlers.pop()
    root.setLevel(lvl)
    formatter = logging.Formatter('%(funcName)s - %(levelname)s - %(message)s')
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)


def load_build(m):
    metadata = path_import(m)

    return metadata
````

<!--NI_OSS_SOURCE repo=nimi-python path=build.sh sha256=72b00a14cf622033c70faa0c44554ba348816d6118bc9f02866b9d8be5554c53 bytes=59 -->
## FILE: build.sh

- repository: `ni/nimi-python`
- source_path: `build.sh`
- sha256: `72b00a14cf622033c70faa0c44554ba348816d6118bc9f02866b9d8be5554c53`
- bytes: 59

````bash
# Python 3 is required for build.py

make clean
make
````

<!--NI_OSS_SOURCE repo=nimi-python path=CHANGELOG.md sha256=4d6dda64408dcb57dfd3c9aedd9f5e2cdb812b815366a26480c85b2490c7d5bb bytes=143125 -->
## FILE: CHANGELOG.md

- repository: `ni/nimi-python`
- source_path: `CHANGELOG.md`
- sha256: `4d6dda64408dcb57dfd3c9aedd9f5e2cdb812b815366a26480c85b2490c7d5bb`
- bytes: 143125

````markdown
# Changelog

## Packages
- [nidcpower (NI-DCPower)](#nidcpower-ni-dcpower)
- [nidigital (NI-Digital Pattern Driver)](#nidigital-ni-digital-pattern-driver)
- [nidmm (NI-DMM)](#nidmm-ni-dmm)
- [nifgen (NI-FGEN)](#nifgen-ni-fgen)
- [nimodinst (NI-ModInst)](#nimodinst-ni-modinst)
- [nirfsg (NI-RFSG)](#nirfsg-ni-rfsg)
- [niscope (NI-SCOPE)](#niscope-ni-scope)
- [nise (NI Switch Executive)](#nise-ni-switch-executive)
- [niswitch (NI-SWITCH)](#niswitch-ni-switch)
- [nitclk (NI-TClk)](#nitclk-ni-tclk)

---

### nidcpower (NI-DCPower)
- [Unreleased](#nidcpower-unreleased)
- [1.5.0](#nidcpower-150---2025-07-01)
- [1.4.9](#nidcpower-149---2025-02-26)
- [1.4.8](#nidcpower-148---2024-04-26)
- [1.4.7](#nidcpower-147---2023-12-15)
- [1.4.6](#nidcpower-146---2023-09-11)
- [1.4.5](#nidcpower-145---2023-06-12)
- [1.4.4](#nidcpower-144---2023-04-14)
- [1.4.3](#nidcpower-143---2022-12-16)
- [1.4.2](#nidcpower-142---2022-08-03)
- [1.4.1](#nidcpower-141---2021-08-23)
- [1.4.0](#nidcpower-140---2021-07-09)
- [1.3.3](#nidcpower-133---2021-02-26)
- [1.3.2](#nidcpower-132---2020-09-18)
- [1.3.1](#nidcpower-131---2020-06-08)
- [1.3.0](#nidcpower-130---2020-05-21)
- [1.2.1](#nidcpower-121---2020-04-21)
- [1.2.0](#nidcpower-120---2020-03-06)
- [1.1.5](#nidcpower-115---2019-11-22)
- [1.1.4](#nidcpower-114---2019-11-19)
- [1.1.3](#nidcpower-113---2019-10-21)
- [1.1.2](#nidcpower-112---2019-06-06)
- [1.1.0](#nidcpower-110---2018-10-25)
- [1.0.1](#nidcpower-101---2018-10-17)
- [1.0.0](#nidcpower-100---2018-06-08)
- [0.9.0](#nidcpower-090---2018-05-22)
- [0.8.0](#nidcpower-080---2018-04-27)
- [0.7.0](#nidcpower-070---2018-02-20)
- [0.6.0](#nidcpower-060---2017-12-20)
- [0.5.0](#nidcpower-050---2017-11-27)
- [0.4.0](#nidcpower-040---2017-11-07)
- [0.3.0](#nidcpower-030---2017-10-13)

#### [nidcpower] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nidcpower] 1.5.0 - 2025-07-01
- Added
  - API parity with NI-DCPower 2025 Q2.
      - Properties:
        - `constant_power_compensation_frequency`
        - `constant_power_current_limit`
        - `constant_power_gain_bandwidth`
        - `constant_power_level`
        - `constant_power_level_range`
        - `constant_power_pole_zero_ratio`
        - `constant_resistance_compensation_frequency`
        - `constant_resistance_current_limit`
        - `constant_resistance_gain_bandwidth`
        - `constant_resistance_level`
        - `constant_resistance_level_range`
        - `constant_resistance_pole_zero_ratio`
        - `output_shorted`
      - Enum values:
        - `CONSTANT_RESISTANCE` and `CONSTANT_POWER` added to enum `OutputFunction`
  - `nidcpower_constant_resistance_and_constant_power.py` and `nidcpower_sink_dc_current_into_electronic_load.py` examples

#### [nidcpower] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
  - API parity with NI-DCPower 2025 Q1.
      - Enum value added:
        - `INHIBITED` added to enum `OutputStates`.
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
  - Fixed #2067: `nidcpower.OutputStates` values are incorrect.
- Removed
  - (Common) Support for Python 3.8

#### [nidcpower] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12
- Changed
  - Fix [#1664](https://github.com/ni/nimi-python/issues/1970): nidcpower_advanced_sequence.py has several issues preventing it from working out of the box on real hardware.

#### [nidcpower] 1.4.7 - 2023-12-15
- Added
  - API parity with NI-DCPower 2023 Q4.
      - Properties added:
         - `current_level_rising_slew_rate`
         - `current_level_falling_slew_rate`
         - `conduction_voltage_mode`
         - `conduction_voltage_on_threshold`
         - `conduction_voltage_off_threshold`
         - `output_cutoff_voltage_measure_limit_high`
         - `output_cutoff_voltage_measure_limit_low`
      - Enum added:
         - `ConductionVoltageMode`
      - Enum values added:
         - `E_LOAD` added to enum `InstrumentMode`
         - `CURRENT_SATURATED`, `VOLTAGE_MEASURE_HIGH` and `VOLTAGE_MEASURE_LOW` added to enum `OutputCutoffReason`


#### [nidcpower] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7


#### [nidcpower] 1.4.5 - 2023-06-12
- Removed
  - (Common) `easy_install` support

#### [nidcpower] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
  - API parity with NI-DCPower 2023 Q2.
      - Properties added:
         - `lcr_ac_dither_enabled`
         - `lcr_ac_electrical_cable_length_delay`
         - `lcr_dc_bias_transient_response`
         - `lcr_source_aperture_time`
         - `measure_complete_event_output_behavior`
         - `measure_complete_event_toggle_initial_state`
         - `sequence_engine_done_event_output_behavior`
         - `sequence_engine_done_event_toggle_initial_state`
         - `sequence_iteration_complete_event_output_behavior`
         - `sequence_iteration_complete_event_toggle_initial_state`
         - `source_complete_event_output_behavior`
         - `source_complete_event_toggle_initial_state`
      - Enums added:
         - `CurrentLimitBehavior`
         - `EventOutputBehavior`
         - `EventToggleInitialState`
         - `LCRDCBiasTransientResponse`
      - Enum values added:
         - `AS_CONFIGURED` added to enum `LCROpenShortLoadCompensationDataSource`
         - `NI_STANDARD_0_5M` added to enum `CableLength`
      - Methods added:
         - `configure_lcr_compensation`
         - `get_lcr_compensation_data`
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.
  - Enums reordered:
    - `AutoZero`
    - `CableLength`

#### [nidcpower] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Changed
  - Binary compatibility change for type `LCRLoadCompensationSpot` on Linux. Client code using method `nidcpower.Session.perform_lcr_load_compensation` on Linux now requires NI-DCPower 2023 Q1 driver runtime or newer.
- Removed
  - (Common) Support for Python 3.6

#### [nidcpower] 1.4.2 - 2022-08-03
- Added
  - API parity with NI-DCPower 2022 Q3.
      - Properties added:
         - `aperture_time_auto_mode`
         - `autorange_maximum_delay_after_range_change`
         - `cable_length`
         - `instrument_mode`
         - `isolation_state`
         - `lcr_actual_load_reactance`
         - `lcr_actual_load_resistance`
         - `lcr_automatic_level_control`
         - `lcr_current_amplitude`
         - `lcr_current_range`
         - `lcr_custom_measurement_time`
         - `lcr_dc_bias_automatic_level_control`
         - `lcr_dc_bias_current_level`
         - `lcr_dc_bias_current_range`
         - `lcr_dc_bias_source`
         - `lcr_dc_bias_voltage_level`
         - `lcr_dc_bias_voltage_range`
         - `lcr_frequency`
         - `lcr_impedance_auto_range`
         - `lcr_impedance_range`
         - `lcr_impedance_range_source`
         - `lcr_load_capacitance`
         - `lcr_load_compensation_enabled`
         - `lcr_load_inductance`
         - `lcr_load_resistance`
         - `lcr_measured_load_reactance`
         - `lcr_measured_load_resistance`
         - `lcr_measurement_time`
         - `lcr_open_compensation_enabled`
         - `lcr_open_conductance`
         - `lcr_open_short_load_compensation_data_source`
         - `lcr_open_susceptance`
         - `lcr_short_compensation_enabled`
         - `lcr_short_custom_cable_compensation_enabled`
         - `lcr_short_reactance`
         - `lcr_short_resistance`
         - `lcr_source_delay_mode`
         - `lcr_stimulus_function`
         - `lcr_voltage_amplitude`
         - `lcr_voltage_range`
      - Enums added:
         - `ApertureTimeAutoMode`
         - `CableLength`
         - `InstrumentMode`
         - `LCRCompensationType`
         - `LCRDCBiasSource`
         - `LCRImpedanceRangeSource`
         - `LCRMeasurementTime`
         - `LCROpenShortLoadCompensationDataSource`
         - `LCRReferenceValueType`
         - `LCRSourceDelayMode`
         - `LCRStimulusFunction`
      - Methods added:
         - `configure_lcr_custom_cable_compensation`
         - `fetch_multiple_lcr`
         - `get_lcr_compensation_last_date_and_time`
         - `get_lcr_custom_cable_compensation_data`
         - `measure_multiple_lcr`
         - `perform_lcr_load_compensation`
         - `perform_lcr_open_compensation`
         - `perform_lcr_open_custom_cable_compensation`
         - `perform_lcr_short_compensation`
         - `perform_lcr_short_custom_cable_compensation`
      - Custom types added:
         - `LCRLoadCompensationSpot`
         - `LCRMeasurement`
  - `nidcpower_lcr_source_ac_voltage.py` example
- Changed
  - Updated supported devices information in documentation for methods and properties
  - Added `channel` field to the `Measurement` namedtuple instances returned by `fetch_multiple` and `measure_multiple`

#### [nidcpower] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
  - API parity with NI-DCPower 21.0.0.
      - Properties added:
         - `output_cutoff_delay`
- Removed
  - (Common) Support for Python 3.5

#### [nidcpower] 1.4.0 - 2021-07-09
- Added
  - `get_channel_names` - [#1588](https://github.com/ni/nimi-python/issues/1588)
  - `create_advanced_sequence_commit_step` - [#1636](https://github.com/ni/nimi-python/issues/1636)
  - API parity with NI-DCPower 20.7.0 by adding Output Cutoff functionality.
       - Properties added:
         - `output_cutoff_current_change_limit_high`
         - `output_cutoff_current_change_limit_low`
         - `output_cutoff_current_measure_limit_high`
         - `output_cutoff_current_measure_limit_low`
         - `output_cutoff_current_overrange_enabled`
         - `output_cutoff_enabled`
         - `output_cutoff_voltage_change_limit_high`
         - `output_cutoff_voltage_change_limit_low`
         - `output_cutoff_voltage_output_limit_high`
         - `output_cutoff_voltage_output_limit_low`
      - Methods added:
         - `clear_latched_output_cutoff_state`
         - `query_latched_output_cutoff_state`
  - Support for independent operation of instrument channels. Creating an `nidcpower.Session`
    with independent channels allows you to use multiple instruments in the same session. With
    independent channels, you can configure multiple channels of the same instrument, or of
    multiple instruments, independently of one another within the same session. Requires NI-DCPower
    driver runtime 20.6.0 or later. In order to use with older runtime or to maintain old behavior,
    pass `independent_channels=False` to `nidcpower.Session` constructor.



#### [nidcpower] 1.3.3 - 2021-02-26
- Added
  - API parity with NI-DCPower 20.6.0 by adding Merged Channels and Shutdown Triggers support. The following properties are added:
      - `merged_channels`
      - `digital_edge_shutdown_trigger_input_terminal`
      - `shutdown_trigger_type`

#### [nidcpower] 1.3.2 - 2020-09-18
- Added
  - API parity with NI-DCPower 20.5.0 by adding measurement autoranging threshold range support, for which the following properties are added:
      - `autorange`
      - `autorange_aperture_time_mode`
      - `autorange_behavior`
      - `autorange_minimum_aperture_time`
      - `autorange_minimum_aperture_time_units`
      - `autorange_minimum_current_range`
      - `autorange_minimum_voltage_range`
      - `autorange_threshold_mode`
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nidcpower] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0



#### [nidcpower] 1.3.0 - 2020-05-21
- Added
  - API parity with NI-DCPower 20.0 by adding the following properties:
      `Session.serial_number`
      `Session.actual_power_allocation`
      `Session.requested_power_allocation`
      `Session.power_allocation_mode`
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nidcpower] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [nidcpower] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
  - `create_advanced_sequence()` - [#504](https://github.com/ni/nimi-python/issues/504)
      - Instead of a list of attribute IDs, you pass in a list of property names as strings
      - Includes example to see how to use it
      - Additional methods and properties that were made public (rather than private)
        - `create_advanced_sequence_step()`
        - `delete_advanced_sequence()`
        - `active_advanced_sequence`
        - `active_advanced_sequence_step`
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [nidcpower] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.



#### [nidcpower] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [nidcpower] 1.1.3 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.
  - Fix type of `sequence_step_delta_time_enabled ` property - [#1015](https://github.com/ni/nimi-python/issues/1015)

#### [nidcpower] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata

#### [nidcpower] 1.1.0 - 2018-10-25
- Added
  - import_attribute_configuration_file function
  - export_attribute_configuration_file function
  - import_attribute_configuration_buffer function
  - import_attribute_configuration_buffer function
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [nidcpower] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)

#### [nidcpower] 1.0.0 - 2018-06-08
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
  - Remove trigger configuration methods, use attributes instead [#860](https://github.com/ni/nimi-python/issues/860)
      - `configure_digital_edge_measure_trigger()` - use `session.digital_edge_measure_trigger_edge` & `session.digital_edge_measure_trigger_input_terminal`
      - `configure_digital_edge_pulse_trigger()` - use `session.digital_edge_pulse_trigger_edge` & `session.digital_edge_pulse_trigger_input_terminal`
      - `configure_digital_edge_sequence_advance_trigger()` - use `session.digital_edge_sequence_advance_trigger_edge` & `session.digital_edge_sequence_advance_trigger_input_terminal`
      - `configure_digital_edge_source_trigger()` - use `session.digital_edge_source_trigger_edge` & `session.digital_edge_source_trigger_input_terminal`
      - `configure_digital_edge_start_trigger()` - use `session.digital_edge_start_trigger_edge` & `session.digital_edge_start_trigger_input_terminal`
  - Remove polarity attributes for triggers that are PXI backplane only (only support rising edge) [#860](https://github.com/ni/nimi-python/issues/860)
      - `digital_edge_measure_trigger_edge`
      - `digital_edge_pulse_trigger_edge`
      - `digital_edge_sequence_advance_trigger_edge`
      - `digital_edge_source_trigger_edge`
      - `digital_edge_start_trigger_edge`

#### [nidcpower] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`
  - `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
  - `active_advanced_sequence` [#832](https://github.com/ni/nimi-python/issues/832)
  - `active_advanced_sequence_step` [#832](https://github.com/ni/nimi-python/issues/832)
  - Default value for trigger parameter on `send_software_edge_trigger()` [#832](https://github.com/ni/nimi-python/issues/832)

#### [nidcpower] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
  - `Session.fetch_multiple()` and `Session.measure_multiple()` now return list of named tuples instead of multiple arrays. See [fetch_multiple](http://nimi-python.readthedocs.io/en/master/nidcpower/functions.html#nidcpower.Session.fetch_multiple) and [measure_multiple](http://nimi-python.readthedocs.io/en/master/nidcpower/functions.html#nidcpower.Session.measure_multiple)
  - `Session.cal_self_calibration()` renamed to `Session.self_cal()` to match other drivers - issue [#615](https://github.com/ni/nimi-python/issues/615)
  - `Session.set_sequence()` values parameter no longer has a default value and must be passed in. Parameter order has changed as a result of this - issue [#797](https://github.com/ni/nimi-python/issues/797)
  - Session constructor channel parameter can now use any channel format that repeated capabilities can use [#807](https://github.com/ni/nimi-python/issues/807)
  - `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)
- Removed
  - Advanced Sequence functions - until [#504](https://github.com/ni/nimi-python/issues/504) can be fixed in a proper way
      - `create_advanced_sequence()`
      - `create_advanced_sequence_step()`
      - `delete_advanced_sequence()`

#### [nidcpower] 0.7.0 - 2018-02-20
- Added
  - `channel` repeated capability - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - Metadata updated to NI-DCPower 17.6.1
  - The following functions timeout parameter now is required to be a `datetime.timedelta()` object:
      - `fetch_multiple()`
      - `wait_for_event()`
  - The following functions return a `datetime.datetime()` object representing the date and time
      - `get_ext_cal_last_date_and_time()`
      - `get_self_cal_last_date_and_time()`
- Removed
  - Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
      - `CurrentLimitAutorange` - `CURRENT_LIMIT_AUTORANGE`
      - `CurrentLevelAutorange` - `CURRENT_LEVEL_AUTORANGE`
      - `VoltageLevelAutorange` - `VOLTAGE_LEVEL_AUTORANGE`
      - `VoltageLimitAutorange` - `VOLTAGE_LIMIT_AUTORANGE`

#### [nidcpower] 0.6.0 - 2017-12-20
- Added
  - (Common) `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
- Changed
  - Property power_line_frequency no longer uses enum PowerLineFrequency.
  - Removed `actual_count` from `fetch_multiple()` returned tuple

#### [nidcpower] 0.5.0 - 2017-11-27
- Added
  - `get_ext_cal_last_date_and_time`
  - `get_ext_cal_last_temp`
  - `get_ext_cal_recommended_interval`
  - `measure_multiple`
- Removed
  - (Common) enum definitions that are not referenced by a function and/or an attributes

#### [nidcpower] 0.4.0 - 2017-11-07
- Added
  - New example `nidcpower_advanced_sequence.py`
- Changed
  - (Common) Simplified examples by removing try/except
  - (Common) **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
  - Fixed method signature for:
      - `wait_for_event`
      - `create_sequence`
      - `create_advanced_sequence`
- Removed
  - Support for `measure_multiple` until issue #444 is addressed.

#### [nidcpower] 0.3.0 - 2017-10-13
- Added
  - Initial release

---

### nidigital (NI-Digital Pattern Driver)

- [Unreleased](#nidigital-unreleased)
- [1.4.9](#nidigital-149---2025-02-26)
- [1.4.8](#nidigital-148---2024-04-26)
- [1.4.6](#nidigital-146---2023-09-11)
- [1.4.5](#nidigital-145---2023-06-12)
- [1.4.4](#nidigital-144---2023-04-14)
- [1.4.3](#nidigital-143---2022-12-16)
- [1.4.1](#nidigital-141---2021-08-23)
- [1.0.0](#nidigital-100---2021-02-26)
- [0.9.2](#nidigital-092---2020-09-18)
- [0.9.1](#nidigital-091---2020-06-08)
- [0.9.0](#nidigital-090---2020-05-21)
- [0.5.0](#nidigital-050---2020-04-21)
- [0.4.0](#nidigital-040---2020-03-06)
- [0.2.1](#nidigital-021---2019-11-22)
- [0.2.0](#nidigital-020---2019-11-19)
- [0.1.1](#nidigital-011---2019-10-21)

#### [nidigital] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nidigital] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
  - Methods Added:
      - `enable_match_fail_combination`

- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nidigital] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [nidigital] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7


#### [nidigital] 1.4.5 - 2023-06-12
- Added
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
- Removed
  - (Common) `easy_install` support

#### [nidigital] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.
  - Update `GRPC_SERVICE_INTERFACE_NAME` to use the correct gRPC package name (`nidigitalpattern_grpc`).

#### [nidigital] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Removed
  - (Common) Support for Python 3.6

#### [nidigital] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
  - API parity with NI-Digital Pattern Driver 21.0.0.
      - Properties added:
         - `digital_edge_rio_trigger_edge`
         - `digital_edge_rio_trigger_source`
         - `exported_rio_event_output_terminal`
         - `rio_event_terminal_name`
         - `rio_trigger_terminal_name`
         - `rio_trigger_type`
      - Repeated Capabilities added:
         - `rio_events`
         - `rio_triggers`

- Removed
  - (Common) Support for Python 3.5

#### [nidigital] 1.0.0 - 2021-02-26
- Added
  - API reference documentation and API usage examples
  - API parity with NI-Digital Pattern Driver 20.6.0 by adding support for configuration of frequency counter measurement mode. The following properties are added:
      - `frequency_counter_measurement_mode`
      - `frequency_counter_hysteresis_enabled`

#### [nidigital] 0.9.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nidigital] 0.9.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [nidigital] 0.9.0 - 2020-05-21
- Added
  - Public API is considered complete, stable, and tested
  - Parity with public API for other ADEs supported in NI-Digital Pattern Driver 19.0.1
  - API reference documentation and example code are not complete
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.
  - Changed initial_state parameters in `apply_levels_and_timing` to basic sequence types - [#1391](https://github.com/ni/nimi-python/issues/1391)
  - Changed HistoryRAMCycleInformation.__repr__ to include `__module__` - [#1426](https://github.com/ni/nimi-python/issues/1426)
  - Changed return type of `get_time_set_period` and `get_time_set_edge` to `datetime.timedelta` - [#1397](https://github.com/ni/nimi-python/issues/1397)

#### [nidigital] 0.5.0 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`
  - `get_pattern_pin_names` - [#1292](https://github.com/ni/nimi-python/issues/1292)
  - Support for `instruments` repeated capability in the following properties - `instrument_firmware_revision`, `serial_number`, and `timing_absolute_delay` -  [#1228](https://github.com/ni/nimi-python/issues/1228)
  - `load_specifications_levels_and_timing` that allows loading of multiple specs, levels, and/or timing files in a single call - [#1392](https://github.com/ni/nimi-python/issues/1392)
  - `get_channel_names` - [#1386](https://github.com/ni/nimi-python/issues/1386)
- Changed
  - Change the type of applicable method parameters and properties to enums - [#1066](https://github.com/ni/nimi-python/issues/1066)
  - `get_site_pass_fail` returns dictionary where each key is a site number and value is a bool indicating pass/fail - [#1297](https://github.com/ni/nimi-python/issues/1297)
  - `burst_pattern` returns dictionary where each key is a site number and value is a bool indicating pass/fail, if `wait_until_done` is specified as `True` - [#1296](https://github.com/ni/nimi-python/issues/1296)
  - Update enum types to match the API in other ADEs - [#1330](https://github.com/ni/nimi-python/issues/1330):
      - Update the names of many enum types. See [#1330](https://github.com/ni/nimi-python/issues/1330) for the full list.
      - Added `WriteStaticPinState` enum type and changed the parameter type of `write_static` method to the newly added enum.
      - Added `SoftwareTrigger` enum type and changed the parameter type of `send_software_edge_trigger` method to the newly added enum.
  - Update `fetch_history_ram_cycle_information`, `get_history_ram_sample_count`, and `is_site_enabled` to use `sites` repeated capability - [#1337](https://github.com/ni/nimi-python/issues/1337)
  - Rename parameter `time_set` to `time_set_name` in applicable time set methods - [#1396](https://github.com/ni/nimi-python/issues/1396)
  - Modified `unload_specifications` to allow unloading of one or more specs files in a single call - [#1392](https://github.com/ni/nimi-python/issues/1392)
  - In `load_pin_map`, changed parameter name `pin_map_file_path` to `file_path` - [#1393](https://github.com/ni/nimi-python/issues/1393)
- Removed
  - `get_pattern_pin_list`, `get_pattern_pin_indexes` and `get_pin_name` - [#1292](https://github.com/ni/nimi-python/issues/1292)
  - `get_site_results_site_numbers` method and `SiteResultType` enum - [#1298](https://github.com/ni/nimi-python/issues/1298)
  - `reset_attribute` - [#1364](https://github.com/ni/nimi-python/issues/1364)
  - `clear_error` - [#1366](https://github.com/ni/nimi-python/issues/1366)
  - `clock_generator_initiate` - [#1370](https://github.com/ni/nimi-python/issues/1370)
  - `load_specifications`, `load_levels`, and `load_timing` - [#1392](https://github.com/ni/nimi-python/issues/1392)
  - `get_channel_name` and `get_channel_name_from_string` - [#1386](https://github.com/ni/nimi-python/issues/1386)

#### [nidigital] 0.4.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
  - `conditional_jump_triggers` and `pattern_opcode_events` repeated capabilities - [#1191](https://github.com/ni/nimi-python/issues/1191), [#1192](https://github.com/ni/nimi-python/issues/1192)
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - `write_source_waveform_site_unique()` now supports `numpy.array` and `list` as site waveform types
  - sites are now a repeated capability instead of a parameter: `session.sites[1,2].fetch_capture_waveform(...)` - [#1111](https://github.com/ni/nimi-python/issues/1111)
  - `fetch_history_ram_cycle_information` method now supports fetching multiple History RAM samples in a single API call - [#1071](https://github.com/ni/nimi-python/issues/1071)
  - Update methods that require `pin_list` to be passed in, such that `pin_list` can be passed in via `pins` repeated capability - [#1294](https://github.com/ni/nimi-python/issues/1294)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)
  - Removed redundant (redundant because corresponding properties can be used instead) API methods - [#1065](https://github.com/ni/nimi-python/issues/1065)
  - Removed programmatic pin map creation API - [#1124](https://github.com/ni/nimi-python/issues/1124)
  - Removed `fetch_history_ram_cycle_pin_data` and `fetch_history_ram_scan_cycle_number`. They are not needed since `fetch_history_ram_cycle_information`
      was updated to return class instances that contains cycle pin data and scan cycle number - [#1071](https://github.com/ni/nimi-python/issues/1071)

#### [nidigital] 0.2.1 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nidigital] 0.2.0 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs
  - `fetch_capture_waveform()` - returns dictionary { site: data, site: data, ... }
  - `write_source_waveform_site_unique()` - takes waveform_name and dictionary { site: data, site: data, ... }
  - `pins` is now a valid repeated capability
- Changed
  - Fix get/set properties - [#1062](https://github.com/ni/nimi-python/issues/1062)
  - Removed array-size parameter from apply_tdr_offsets() and write_source_waveform_broadcast_u32() methods - [#1070](https://github.com/ni/nimi-python/issues/1070)
  - Renamed `write_source_waveform_broadcast_u32()` to `write_source_waveform_broadcast()`
  - `get_pin_results_pin_information()` - returns namedtuple `PinInfo(pin_indexes, site_numbers, channel_indexes)`

#### [nidigital] 0.1.1 - 2019-10-21
- Added
  - Initial support
  - Very basic at this point and subject to change
  - Looking for any testing and/or feedback
  - `get_channel_name_from_string()`
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
    - version >= 1.0
       - .devN or .aN - Alpha
       - .bN, .cN or .rcN - Beta
       - \<nothing\> or .postN - Stable
    - version < 1.0 and version >= 0.5 - Beta
    - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.
  - New enums:
    | Enum name                  | Where used                                                                       |
    |----------------------------|----------------------------------------------------------------------------------|
    | `DigitalEdge`              | `digital_edge_conditional_jump_trigger_edge`, `digital_edge_start_trigger_edge`  |
    | `ApertureTimeUnits`        | `ppmu_aperture_time_units`, `ppmu_configure_aperture_time(units)`                |
    | `PPMUOutputFunction`       | `ppmu_output_function`                                                           |
    | `SelectedFunction`         | `selected_function`                                                              |
    | `TDREndpointTermination`   | `tdr_endpoint_termination`                                                       |
    | `Signal`                   | `export_signal(signal)`                                                          |
  - **[Source Breaker]** No longer return the "actual size" from functions that use 'ivi-dance-with-a-twist'. This only affects `nidigital`.
- Removed
  - Should be private - `get_session_state()`, `get_desired_attribute_*()`, `ppmu_measure_cached()`, `read_static_cached()`, `configure_ref_clock()`, `disable()`,
       `get_number_of_vectors()`, `get_pattern_file_path()`, `get_pin_type()`, `get_time_set_compare_edges()`, `get_time_set_drive_edges()`,
       `is_pattern_file_modified_since_load()`, `load_levels_internal()`, `load_pattern_internal()`, `load_timing_internal()`, `uncommit()`
  - Need to determine how to generate this function - `fetch_capture_waveform_u32()`

---

### nidmm (NI-DMM)

- [Unreleased](#nidmm-unreleased)
- [1.4.9](#nidmm-149---2025-02-26)
- [1.4.8](#nidmm-148---2024-04-26)
- [1.4.6](#nidmm-146---2023-09-11)
- [1.4.5](#nidmm-145---2023-06-12)
- [1.4.4](#nidmm-144---2023-04-14)
- [1.4.3](#nidmm-143---2022-12-16)
- [1.4.1](#nidmm-141---2021-08-23)
- [1.3.2](#nidmm-132---2020-09-18)
- [1.3.1](#nidmm-131---2020-06-08)
- [1.3.0](#nidmm-130---2020-05-21)
- [1.2.1](#nidmm-121---2020-04-21)
- [1.2.0](#nidmm-120---2020-03-06)
- [1.1.5](#nidmm-115---2019-11-22)
- [1.1.4](#nidmm-114---2019-11-19)
- [1.1.3](#nidmm-113---2019-10-21)
- [1.1.2](#nidmm-112---2019-06-06)
- [1.1.0](#nidmm-110---2018-10-25)
- [1.0.1](#nidmm-101---2018-10-17)
- [1.0.0](#nidmm-100---2018-06-08)
- [0.9.0](#nidmm-090---2018-05-22)
- [0.8.0](#nidmm-080---2018-04-27)
- [0.7.0](#nidmm-070---2018-02-20)
- [0.6.0](#nidmm-060---2017-12-20)
- [0.5.0](#nidmm-050---2017-11-27)
- [0.4.0](#nidmm-040---2017-11-07)
- [0.3.0](#nidmm-030---2017-10-13)
- [0.2.0](#nidmm-020---2017-09-20)
- [0.1.0](#nidmm-010---2017-09-01)

#### [nidmm] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nidmm] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nidmm] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [nidmm] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7

#### [nidmm] 1.4.5 - 2023-06-12
- Added
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
- Removed
  - (Common) `easy_install` support

#### [nidmm] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [nidmm] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Removed
  - (Common) Support for Python 3.6

#### [nidmm] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [nidmm] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nidmm] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [nidmm] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nidmm] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
        session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [nidmm] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [nidmm] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nidmm] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [nidmm] 1.1.3 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.

#### [nidmm] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata

#### [nidmm] 1.1.0 - 2018-10-25
- Added
  - import_attribute_configuration_file function
  - export_attribute_configuration_file function
  - import_attribute_configuration_buffer function
  - import_attribute_configuration_buffer function
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [nidmm] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)

#### [nidmm] 1.0.0 - 2018-06-08
- Changed
  - Fixed name `freq_voltage_autorange` became `freq_voltage_auto_range`
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
  - `configure_ac_bandwidth()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `configure_open_cable_comp_values()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `configure_power_line_frequency()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `configure_short_cable_comp_values()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `get_aperture_time_info()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `get_auto_range_value()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `get_measurement_period()` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `latency` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `shunt_value` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `meas_dest_slope` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `sample_trigger_slope` - [#875](https://github.com/ni/nimi-python/issues/875)
  - `trigger_slope` - [#875](https://github.com/ni/nimi-python/issues/875)

#### [nidmm] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`

#### [nidmm] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
  - Enum values that start with an underscore + digit have been renamed
      - `Function._2_WIRE_RES` --> `Function.TWO_WIRE_RES`
      - `Function._4_WIRE_RES` --> `Function.FOUR_WIRE_RES`
      - `ThermistorType._44004` --> `ThermistorType.THERMISTOR_44004`
      - `ThermistorType._44006` --> `ThermistorType.THERMISTOR_44006`
      - `ThermistorType._44007` --> `ThermistorType.THERMISTOR_44007`
      - `TransducerType._2_WIRE_RTD` --> `TransducerType.TWO_WIRE_RTD`
      - `TransducerType._4_WIRE_RTD` --> `TransducerType.FOUR_WIRE_RTD`
  - `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)

#### [nidmm] 0.7.0 - 2018-02-20
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - `nidmm.Session()` no longer takes id_query parameter (Fix [#670](https://github.com/ni/nimi-python/issues/670))
  - The following functions timeout or delay parameter now is required to be a `datetime.timedelta()` object:
      - `configure_multi_point()`
      - `configure_trigger()`
      - `fetch()`
      - `fetch_multi_point()`
      - `fetch_waveform()`
      - `read()`
      - `read_multi_point()`
      - `read_waveform()`
  - The following functions return a `datetime.datetime()` object representing the date and time
      - `get_cal_date_and_time()`
  - Metadata updated to NI-DMM 17.5
- Removed
  - Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
      - `DCBias` - `DC_BIAS`
      - `OffsetCompensatedOhms` - `OFFSET_COMP_OHMS`

#### [nidmm] 0.6.0 - 2017-12-20
- Added
  - (Common) `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
  - `fetch_waveform_into` for high-performance fetch using numpy.array of float64.
- Changed
  - Property powerline_freq no longer uses enum PowerlineFrequency.
  - Property current_source no longer uses enum CurrentSource.
  - Property input_resistance no longer uses enum InputResistance.
  - Removed `actual_number_of_points` from `fetch_waveform()` returned tuple
  - Removed `actual_number_of_points` from `fetch_multi_point()` returned tuple
  - Removed `actual_number_of_points` from `read_multi_point()` returned tuple
  - Removed `actual_number_of_points` from `read_waveform()` returned tuple

#### [nidmm] 0.5.0 - 2017-11-27
- Added
  - `get_ext_cal_recommended_interval`
- Removed
  - (Common) enum definitions that are not referenced by a function and/or an attributes

#### [nidmm] 0.4.0 - 2017-11-07
- Changed
  - (Common) Simplified examples by removing try/except
  - (Common) **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
  - Removed incorrect leading underscore from some enum values:
      - `Function.AC_VOLTS_DC_COUPLED`
      - `Function.WAVEFORM_CURRENT`
      - `MeasurementCompleteDest.LBR_TRIG_0`
      - `OperationMode.IVIDMM_MODE`
      - `SampleTrigger.EXTERNAL`
      - `SampleTrigger.TTL_3`
      - `TriggerSource.TTL_0`
      - `TriggerSource.TTL_3`
      - `TriggerSource.TTL_7`
      - `TriggerSource.PXI_STAR`

#### [nidmm] 0.3.0 - 2017-10-13
- Added
  - (Common) Support for ViInt64 (64-bit integers)
- Changed
  - (Common) Modified how methods with repeated capabilities are invoked. There's no longer (for example) a `channel_name` input. Instead:
      ``` python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
  - (Common) Enum value documentation lists the fully qualified name - this is to allow easy copy/paste
  - Added default values to some parameters.
- Removed
  - Removed methods that aren’t useful in the Python bindings.

#### [nidmm] 0.2.0 - 2017-09-20
- Added
  - (Common) Suport for channel-based properties
- Changed
  - (Common) Warnings no longer raise an exception
      -  Warnings are now added to warnings.warn()
  - Added support for enums with types other than ViInt32 (Fixes [#330](https://github.com/ni/nimi-python/issues/330))

#### [nidmm] 0.1.0 - 2017-09-01
- Added
  - Initial release

---

### nifgen (NI-FGEN)

- [Unreleased](#nifgen-unreleased)
- [1.4.9](#nifgen-149---2025-02-26)
- [1.4.8](#nifgen-148---2024-04-26)
- [1.4.6](#nifgen-146---2023-09-11)
- [1.4.5](#nifgen-145---2023-06-12)
- [1.4.4](#nifgen-144---2023-04-14)
- [1.4.3](#nifgen-143---2022-12-16)
- [1.4.2](#nifgen-142---2022-08-03)
- [1.4.1](#nifgen-141---2021-08-23)
- [1.3.3](#nifgen-133---2021-02-26)
- [1.3.2](#nifgen-132---2020-09-18)
- [1.3.1](#nifgen-131---2020-06-08)
- [1.3.0](#nifgen-130---2020-05-21)
- [1.2.1](#nifgen-121---2020-04-21)
- [1.2.0](#nifgen-120---2020-03-06)
- [1.1.5](#nifgen-115---2019-11-22)
- [1.1.4](#nifgen-114---2019-11-19)
- [1.1.3](#nifgen-113---2019-10-21)
- [1.1.2](#nifgen-112---2019-06-06)
- [1.1.0](#nifgen-110---2018-10-25)
- [1.0.1](#nifgen-101---2018-10-17)
- [1.0.0](#nifgen-100---2018-06-08)
- [0.9.0](#nifgen-090---2018-05-22)
- [0.8.0](#nifgen-080---2018-04-27)
- [0.7.0](#nifgen-070---2018-02-20)
- [0.6.0](#nifgen-060---2017-12-20)
- [0.5.0](#nifgen-050---2017-11-27)
- [0.4.0](#nifgen-040---2017-11-07)

#### [nifgen] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nifgen] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nifgen] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12
  - Properties added:
      - `started_event_pulse_width` - [#1873](https://github.com/ni/nimi-python/issues/1873)
      - `done_event_pulse_width` - [#1873](https://github.com/ni/nimi-python/issues/1873)
      - `marker_event_pulse_width` - [#1873](https://github.com/ni/nimi-python/issues/1873)
      - `started_event_pulse_width_units` - [#1873](https://github.com/ni/nimi-python/issues/1873)
      - `done_event_pulse_width_units` - [#1873](https://github.com/ni/nimi-python/issues/1873)
      - `marker_event_pulse_width_units` - [#1873](https://github.com/ni/nimi-python/issues/1873)

  - Enum added:
      - `EventPulseWidthUnits` - [#1873](https://github.com/ni/nimi-python/issues/1873)

#### [nifgen] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7

#### [nifgen] 1.4.5 - 2023-06-12
- Added
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
- Removed
  - (Common) `easy_install` support

#### [nifgen] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [nifgen] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Removed
  - (Common) Support for Python 3.6

#### [nifgen] 1.4.2 - 2022-08-03
- Added
  - `data_markers` repeated capability support - [#1668](https://github.com/ni/nimi-python/issues/1668)
- Changed
  - Addressed [#1627](https://github.com/ni/nimi-python/issues/1627) for attributes supporting the following repeated capabilities
      - `channels`
      - `markers`
      - `data_markers`
      - `script_triggers`
  - Corrected multiple mistakes in repeated capability info of attribute metadata
      - alters API behavior (repeated capability access of attributes) and documentation

#### [nifgen] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [nifgen] 1.3.3 - 2021-02-26
- Added
  - nifgen_trigger.py example to demonstrate pulling a trigger from another device.

#### [nifgen] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nifgen] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [nifgen] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nifgen] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [nifgen] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
  - `nifgen.Session.import_attribute_configuration_file()`
  - `nifgen.Session.import_attribute_configuration_buffer()`
  - `nifgen.Session.export_attribute_configuration_file()`
  - `nifgen.Session.export_attribute_configuration_buffer()`
  - `nifgen.Session.get_channel_name()`
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - `nifgen.Session.send_software_edge_trigger()` now takes two parameters - `trigger` and `trigger_id`
      - See documentation on how to call this function
      - Calling the previous way will log a DeprecationWarning to the warning subsystem
      - [#1300](https://github.com/ni/nimi-python/issues/1300)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [nifgen] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nifgen] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [nifgen] 1.1.3 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.
- Removed
  - `configure_custom_fir_filter_coefficients()` - [#996](https://github.com/ni/nimi-python/issues/996) - Should have been removed as part of - [#891](https://github.com/ni/nimi-python/issues/891)

#### [nifgen] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata
  - Enum values for `HardwareState` were incorrect - fix to match niFgen.h

#### [nifgen] 1.1.0 - 2018-10-25
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [nifgen] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)

#### [nifgen] 1.0.0 - 2018-06-08
- Changed
  - `num_channels` attribute renamed to `channel_count` - now consistent with other drivers
  - `send_software_edge_trigger()` no longer takes any parameters.
      - To send a start software trigger, call it on the session directly:
        ``` python
        session.send_software_edge_trigger()
        ```
      - To send a script software trigger, call it on the script triggers container:
        ``` python
        session.script_triggers[1].send_software_edge_trigger()
        ```
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
  - Remove trigger configuration methods, use attributes instead [#860](https://github.com/ni/nimi-python/issues/860)
      - `configure_digital_edge_script_trigger()` - use `session.digital_edge_script_trigger_source` & `session.digital_edge_script_trigger_edge`
      - `configure_digital_level_script_trigger()` - use `session.digital_level_script_trigger_source` & `session.digital_level_script_trigger_active_level`
      - `configure_digital_edge_start_trigger()` - use `session.digital_edge_start_trigger_source` & `session.digital_edge_start_trigger_edge`
  - Removed `get_fir_filter_coefficients()` - [#535](https://github.com/ni/nimi-python/issues/535), [#596](https://github.com/ni/nimi-python/issues/596)

#### [nifgen] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
  - Some functions missed setting repeated capabilities, leaving these as parameters instead of using the repeated capabilites object.
      - `session.configure_digital_edge_script_trigger('ScriptTrigger0', source, ...)` becomes `session.script_triggers[0].configure_digital_edge_script_trigger(source, ...)`
      - `session.configure_digital_level_script_trigger('ScriptTrigger0', source, ...)` becomes `session.script_triggers[0].configure_digital_level_script_trigger(source, ...)`
  - Combined named and un-named waveform methods into one [#862](https://github.com/ni/nimi-python/issues/862)
      - `set_waveform_next_write_position()` and `set_named_waveform_next_write_position()` becomes `set_next_write_position()`
      - `clear_arb_waveform()` and `delete_named_waveform()` becomes `delete_waveform()`
- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`
  - `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
  - `osp_fir_filter_interpolation` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_gaussian_bt` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_flat_passband` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_data_processing_mode` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_compensate_for_filter_group_delay` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_cic_filter_interpolation` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_cic_filter_gain` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_cic_filter_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_carrier_phase_q` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_carrier_phase_i` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_carrier_frequency` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_carrier_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_pre_filter_offset_q` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_pre_filter_offset_i` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_pre_filter_gain_q` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_pre_filter_gain_i` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_overflow_status` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_overflow_error_reporting` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_mode` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_frequency_shift` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_type` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_root_raised_cosine_alpha` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `osp_fir_filter_raised_cosine_alpha` - [#864](https://github.com/ni/nimi-python/issues/864)
  - `ready_for_start_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_toggle_initial_state` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_live_status` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `ready_for_start_event_live_status` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `marker_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `started_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `done_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
  - `direct_dma_enabled` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `direct_dma_windowaddress` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `direct_dma_window_size`  [#858](https://github.com/ni/nimi-python/issues/858)
  - `gain_dac_value` - [#88](https://github.com/ni/nimi-python/issues/858)
  - `offset_dac_vaue` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `id_query_respone` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `oscillator_freq_ac_value` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `oscillator_phase_dac_vale` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `post_amplifier_attenuatio` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `pre_amplifier_attenuation` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `p2p_endpoint_fullness_strt_trigger_level` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `pci_dma_optimizations_enabled` - [#858](ttps://github.com/ni/nimi-python/issues/858)
  - `sample_clock_absolute_delay`- [#858](https://github.com/ni/nimi-python/issues/858)
  - `synchronization` - [#858](ttps://github.com/ni/nimi-python/issues/858)
  - `sync_duty_cycl_high` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `sync_out_output_terinal` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `trigger_source` - [#858](https://github.com/ni/nimi-python/issues/858)
  - `video_wavefor_type` - [#858](https://github.com/ni/nimi-python/issues/858)

#### [nifgen] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
  - `Session.export_signal()` signal_identifier now has a default of "". This moves it to the end of the parameter list [#801](https://github.com/ni/nimi-python/issues/801)
  - `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)
- Removed
  - `Session.cal_adc_input` attribute and `Session.enums.CalADCInput` enum - External Cal not supported in Python
  - Session constructor channel parameter can now use any channel format that repeated capabilities can use [#807](https://github.com/ni/nimi-python/issues/807)

#### [nifgen] 0.7.0 - 2018-02-20
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - Repeated capablilites - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion:
     - `channel` repeated capability
     - `markers` repeated capability
     - `script_triggers` repeated capability
  - The following functions timeout parameter now is required to be a `datetime.timedelta()` object:
     - `adjust_sample_clock_relative_delay()`
     - `wait_until_done()`
  - The following functions return a `datetime.datetime()` object representing the date and time
     - `get_ext_cal_last_date_and_time()`
     - `get_self_cal_last_date_and_time()`

#### [nifgen] 0.6.0 - 2017-12-20
- Added
  - (Common) `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
  - Support for calling `write_waveform` using list (float) or numpy.array (int16 or float64)
  - Support for calling `write_waveform` with a waveform handle (int) or a name (str).
  - Support for calling `create_waveform` using list (float) or numpy.array (int16 or float64)
- Changed
  - Renamed `create_waveform_f64` -> `create_waveform`
- Removed
  - `create_waveform_i16`
  - `write_binary16_waveform`: Use `write_waveform`
  - `write_named_waveform_i16`: Use `write_waveform`
  - `write_named_waveform_f64`: Use `write_waveform`

#### [nifgen] 0.5.0 - 2017-11-27
- Removed
  - (Common) enum definitions that are not referenced by a function and/or an attributes
  - `adjust_sample_clock_relative_delay`

#### [nifgen] 0.4.0 - 2017-11-07
- Added
  - Initial release
---

### nimodinst (NI-ModInst)

- [Unreleased](#nimodinst-unreleased)
- [1.4.9](#nimodinst-149---2025-02-26)
- [1.4.8](#nimodinst-148---2024-04-26)
- [1.4.6](#nimodinst-146---2023-09-11)
- [1.4.5](#nimodinst-145---2023-06-12)
- [1.4.4](#nimodinst-144---2023-04-14)
- [1.4.3](#nimodinst-143---2022-12-16)
- [1.4.1](#nimodinst-141---2021-08-23)
- [1.3.2](#nimodinst-132---2020-09-18)
- [1.3.1](#nimodinst-131---2020-06-08)
- [1.3.0](#nimodinst-130---2020-05-21)
- [1.2.1](#nimodinst-121---2020-04-21)
- [1.2.0](#nimodinst-120---2020-03-06)
- [1.1.5](#nimodinst-115---2019-11-22)
- [1.1.4](#nimodinst-114---2019-11-19)
- [1.1.3](#nimodinst-113---2019-10-21)
- [1.1.2](#nimodinst-112---2019-06-06)
- [1.1.0](#nimodinst-110---2018-10-25)
- [1.0.1](#nimodinst-101---2018-10-17)
- [1.0.0](#nimodinst-100---2018-06-08)
- [0.9.0](#nimodinst-090---2018-05-22)
- [0.8.0](#nimodinst-080---2018-04-27)
- [0.7.0](#nimodinst-070---2018-02-20)
- [0.5.0](#nimodinst-050---2017-11-27)
- [0.4.0](#nimodinst-040---2017-11-07)
- [0.3.0](#nimodinst-030---2017-10-13)
- [0.2.0](#nimodinst-020---2017-09-20)

#### [nimodinst] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nimodinst] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nimodinst] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [nimodinst] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7

#### [nimodinst] 1.4.5 - 2023-06-12
- Removed
  - (Common) `easy_install` support

#### [nimodinst] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [nimodinst] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
- Removed
  - (Common) Support for Python 3.6

#### [nimodinst] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [nimodinst] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nimodinst] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [nimodinst] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nimodinst] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [nimodinst] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [nimodinst] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nimodinst] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [nimodinst] 1.1.3 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.

#### [nimodinst] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata

#### [nimodinst] 1.1.0 - 2018-10-25
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [nimodinst] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)

#### [nimodinst] 1.0.0 - 2018-06-08
- Changed
  - Double close will now allow NI-ModInst to return error
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)

#### [nimodinst] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
  - Indexing on `nimodinst.Session` is no longer allowed
      - `session[0].device_name` becomes `session.devices[0].device_name`
      - This is to be consistent with other drivers

- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`

#### [nimodinst] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)

#### [nimodinst] 0.7.0 - 2018-02-20
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion

#### [nimodinst] 0.5.0 - 2017-11-27
- Removed
  - (Common) enum definitions that are not referenced by a function and/or an attributes

#### [nimodinst] 0.4.0 - 2017-11-07
- Changed
  - (Common) Simplified examples by removing try/except
  - (Common) **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines

#### [nimodinst] 0.3.0 - 2017-10-13
- Added
  - (Common) Support for ViInt64 (64-bit integers)
- Changed
  - (Common) Modified how methods with repeated capabilities are invoked. There's no longer (for example) a `channel_name` input. Instead:
      ``` python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
  - (Common) Enum value documentation lists the fully qualified name - this is to allow easy copy/paste

#### [nimodinst] 0.2.0 - 2017-09-20
- Added
  - (Common) Suport for channel-based properties
- Changed
  - (Common) Warnings no longer raise an exception
      -  Warnings are now added to warnings.warn()
  - Device index is now on session not attribute. The correct way is now
      ``` python
      i = 0
      with nimodinst.Session('nidmm') as session:
          name = session[i].device_name
      ```

#### [nimodinst] 0.1.0 - 2017-09-01
- Added
  - Initial release
---

### nirfsg (NI-RFSG)

- [Unreleased](#nirfsg-unreleased)
- [1.1.0](#nirfsg-110---2026-04-17)
- [1.0.1](#nirfsg-101---2026-01-09)
- [1.0.0](#nirfsg-100---2025-08-05)

#### [nirfsg] Unreleased
- Added
- Changed
- Removed

#### [nirfsg] 1.1.0 - 2026-04-17
- Added
  - Python 3.14 Support
  - `get_script` and `delete_script` methods
  - `SCRIPTS` added to enum `LoadOptions`
  - `DO_NOT_DRIVE_SIGNAL` added to enum `PulseModulationSource`
  - `numpy` is now an install dependency
  - gRPC support, enabling remote session management via NI gRPC Device Server
- Changed
  - Fixed `error_message` method to return the error string as output
- Removed

#### [nirfsg] 1.0.1 - 2026-01-09
- Changed
  - Added default value for `module` parameter in `get_self_cal_last_date_and_time` and `get_self_calibration_temperature` methods to align with documentation and allow duck-typing
  - Changed the parameter name for waveform name from `name` to `waveform_name` in `clear_arb_waveform` and `select_arb_waveform` to be consistent with other waveform methods
  - Changed the name of below methods to be consistent with other APIs in the repository
    - `get_self_calibration_last_date_and_time` to `get_self_cal_last_date_and_time`
    - `get_external_calibration_last_date_and_time` to `get_ext_cal_last_date_and_time`
  - Changed `frequency_settling` property to be of type float instead of hightime.timedelta, since it can have multiple interpretation based on `frequency_settling_units` property value
  - Changed `interpolation_delay` and `relative_delay` properties to be of type hightime.timedelta, so that it aligns with _delay_ attributes across other APIs in the repository
  - Changed `exported_ref_clock_rate` and `ref_clock_rate` properties to be of type float instead of enum, since the enums just represented raw float values
  - Fixed the return type of `get_all_script_names` and `get_all_named_waveform_names` to remove the size parameter and return a list of strings instead of a comma-separated string
  - Updated `external_calibration_recommended_interval` property to return a hightime.timedelta object instead of months as an int, aligning with other APIs in the repository
  - Updated `self_test` to not have any parameters, aligning with other APIs in the repository
  - Updated `wait_until_settled` method to have `max_time_milliseconds` parameter as type hightime.timedelta with a default value of 10 seconds
  - Updated below properties and method parameters to be of string enum type instead of plain string, since they would support only fixed set of strings
    - `pulse_modulation_source`
    - `exported_pulse_modulation_event_output_terminal`
    - `exported_ref_clock_output_terminal`
    - `lo_source`
    - `arb_sample_clock_source`
    - `ref_clock_source`
    - `trigger_identifier` parameter in `send_software_edge_trigger` method
  - Updated below properties to be list of str instead of them returning a comma separated list of string values 
    - `available_paths`
    - `available_ports`
    - `fixed_group_delay_across_ports`
    - `group_capabilities`
    - `supported_instrument_models`
- Removed
  - Python 3.9 Support
  - Methods and properties applicable only to hardware which are not supported anymore
    - Methods
      - `configure_digital_modulation_user_defined_waveform`
      - `configure_pxi_chassis_clk10`
    - Properties
      - `analog_modulation_fm_deviation`
      - `analog_modulation_waveform_frequency`
      - `arb_filter_raised_cosine_alpha`
      - `arb_filter_root_raised_cosine_alpha`
      - `arb_filter_type`
      - `arb_oscillator_phase_dac_value`
      - `arb_power`
      - `attenuator_hold_enabled`
      - `attenuator_hold_max_power`
      - `compensate_for_filter_group_delay`
      - `data_transfer_block_size`
      - `data_transfer_maximum_bandwidth`
      - `data_transfer_maximum_in_flight_reads`
      - `data_transfer_preferred_packet_size`
      - `digital_modulation_fsk_deviation`
      - `digital_modulation_prbs_order`
      - `digital_modulation_prbs_seed`
      - `digital_modulation_symbol_rate`
      - `digital_modulation_type`
      - `digital_modulation_waveform_type`
      - `digital_pattern`
      - `frequency_tolerance`
      - `peak_power_adjustment_inheritance`
      - `pxi_chassis_clk10_source`
  - Methods and properties which are necessary for IVI compliance of the driver, but are not applicable for Python
    - Methods
      - `check_attribute_vi_boolean`
      - `check_attribute_vi_int32`
      - `check_attribute_vi_int64`
      - `check_attribute_vi_real64`
      - `check_attribute_vi_session`
      - `check_attribute_vi_string`
      - `clear_error`
      - `disable`
      - `error_query`
      - `get_channel_name`
      - `reset_attribute`
      - `revision_query`
    - Properties
      - `cache`
      - `interchange_check`
      - `query_instrument_status`
      - `range_check`
      - `record_coercions`
      - `simulate`

#### [nirfsg] 1.0.0 - 2025-08-05
- Added
  - Initial release
---

### niscope (NI-SCOPE)

- [Unreleased](#niscope-unreleased)
- [1.4.9](#niscope-149---2025-02-26)
- [1.4.8](#niscope-148---2024-04-26)
- [1.4.6](#niscope-146---2023-09-11)
- [1.4.5](#niscope-145---2023-06-12)
- [1.4.4](#niscope-144---2023-04-14)
- [1.4.3](#niscope-143---2022-12-16)
- [1.4.1](#niscope-141---2021-08-23)
- [1.3.2](#niscope-132---2020-09-18)
- [1.3.1](#niscope-131---2020-06-08)
- [1.3.0](#niscope-130---2020-05-21)
- [1.2.1](#niscope-121---2020-04-21)
- [1.2.0](#niscope-120---2020-03-06)
- [1.1.5](#niscope-115---2019-11-22)
- [1.1.4](#niscope-114---2019-11-19)
- [1.1.3](#niscope-113---2019-10-21)
- [1.1.2](#niscope-112---2019-06-06)
- [1.1.0](#niscope-110---2018-10-25)
- [1.0.1](#niscope-101---2018-10-17)
- [1.0.0](#niscope-100---2018-06-08)
- [0.9.0](#niscope-090---2018-05-22)
- [0.8.0](#niscope-080---2018-04-27)
- [0.7.0](#niscope-070---2018-02-20)
- [0.6.0](#niscope-060---2017-12-20)
- [0.5.0](#niscope-050---2017-11-27)

#### [niscope] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [niscope] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [niscope] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [niscope] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7


#### [niscope] 1.4.5 - 2023-06-12
- Added
  - `get_channel_names()`
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
- Changed
  - Fix [#1770](https://github.com/ni/nimi-python/issues/1770): fetch(), read(), and friends return wrong data when called with channel ranges on multi-instrument session.
- Removed
  - (Common) `easy_install` support

#### [niscope] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.
  - Fix [#1941](https://github.com/ni/nimi-python/issues/1941): When calling niscope.Session.fetch_array_measurement in a MeasurementLink measurement plugin, meas_wfm_size cannot be set.
      - Requires NI gRPC Device Server 2023 Q2 or later. Older versions do not support this parameter and return all available samples.

#### [niscope] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Removed
  - (Common) Support for Python 3.6

#### [niscope] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [niscope] 1.3.2 - 2020-09-18
- Added
  - New methods for getting calibration information. - [#1463](https://github.com/ni/nimi-python/issues/1463)
      - `get_ext_cal_last_date_and_time`
      - `get_ext_cal_last_temp`
      - `get_self_cal_last_date_and_time`
      - `get_self_cal_last_temp`
  - Measurement library methods. - [#806](https://github.com/ni/nimi-python/issues/806)
      - `add_waveform_processing`
      - `clear_waveform_measurement_stats`
      - `clear_waveform_processing`
      - `fetch_array_measurement`
      - `fetch_measurement_stats`
  - Measurement library properties.
      - `meas_array_gain`
      - `meas_array_offset`
      - `meas_chan_high_ref_level`
      - `meas_chan_low_ref_level`
      - `meas_chan_mid_ref_level`
      - `meas_filter_center_freq`
      - `meas_filter_cutoff_freq`
      - `meas_filter_order`
      - `meas_filter_ripple`
      - `meas_filter_taps`
      - `meas_filter_transient_waveform_percent`
      - `meas_filter_type`
      - `meas_filter_width`
      - `meas_fir_filter_window`
      - `meas_high_ref`
      - `meas_low_ref`
      - `meas_mid_ref`
      - `meas_hysteresis_percent`
      - `meas_interpolation_sampling_factor`
      - `meas_last_acq_histogram_size`
      - `meas_other_channel`
      - `meas_percentage_method`
      - `meas_polynomial_interpolation_order`
      - `meas_ref_level_units`
      - `meas_time_histogram_high_time`
      - `meas_time_histogram_high_volts`
      - `meas_time_histogram_low_time`
      - `meas_time_hisogram_low_volts`
      - `meas_time_histogram_size`
      - `meas_voltage_histogram_high_volts`
      - `meas_voltage_histogram_low_volts`
      - `meas_voltage_histogram_size`
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.
  - Fix [#1509](https://github.com/ni/nimi-python/issues/1509): `channel` and `record` fields are swapped in `waveform_info` struct returned from niscope fetch methods
  - Fix [#1510](https://github.com/ni/nimi-python/issues/1510): `record` value in `waveform_info` struct returned from niscope fetch methods is wrong if `record_number` is non-zero



#### [niscope] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [niscope] 1.3.0 - 2020-05-21
- Added
  - API parity with NI-SCOPE 20.0 by adding the following properties:
      - `Session.end_of_acquisition_event_terminal_name`
      - `Session.end_of_record_event_terminal_name`
      - `Session.advance_trigger_terminal_name`
      - `Session.ref_trigger_terminal_name`
      - `Session.start_trigger_terminal_name`
      - `Session.ready_for_advance_event_terminal_name`
      - `Session.ready_for_ref_event_terminal_name`
      - `Session.ready_for_start_event_terminal_name`
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.
#### [niscope] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [niscope] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [niscope] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [niscope] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [niscope] 1.1.3 - 2019-10-21
- Added
  - `cable_sense_signal_enable`, `cable_sense_voltage`, `cable_sense_mode` properties and associated enum
  - `enabled_channels`, `product_code` properties
  - `glitch_condition`, `glitch_polarity`, `glitch_width` properties and associated enums
  - `runt_high_threshold`, `runt_low_threshold`, `runt_polarity`, `runt_condition`, `runt_time_high_limit`, `runt_time_low_limit` properties and associated enums
  - `width_condition`, `width_high_threshold`, `width_low_threshold`, `width_polarity` properties and associated enums
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.

#### [niscope] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata
  - Fixed enum values for `TIME_HISTOGRAM_MEAN_PLUS_STDEV`, `TIME_HISTOGRAM_MEAN_PLUS_2_STDEV`, `HF_REJECT` and `LF_REJECT`

#### [niscope] 1.1.0 - 2018-10-25
- Added
  - import_attribute_configuration_file function
  - export_attribute_configuration_file function
  - import_attribute_configuration_buffer function
  - import_attribute_configuration_buffer function

- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [niscope] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)
  - Format of output of wavefrom_info.__str__()

#### [niscope] 1.0.0 - 2018-06-08
- Added
  - `niscope_fetch_forever.py` example
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
  - Removed default value for `level` parameter on `configure_trigger_edge()`
      - parameter list is now
        ``` python
        configure_trigger_edge(self, trigger_source, level, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))
        ```
  - Removed default values for `level` and `hysteresis` parameters on `configure_trigger_hysteresis()`
      - parameter list is now
        ``` python
        configure_trigger_hysteresis(self, trigger_source, level, hysteresis, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))
        ```

#### [niscope] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`
  - Properties removed
      - `stream_relative_to` [#825](https://github.com/ni/nimi-python/issues/825)
      - `oscillator_phase_dac_value` [#825](https://github.com/ni/nimi-python/issues/825)
      - `mux_mode_register` [#825](https://github.com/ni/nimi-python/issues/825)
      - `ddc_center_frequency` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_data_processing_mode` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_frequency_translation_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_frequency_translation_phase_i` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_frequency_translation_phase_q` [#823](https://github.com/ni/nimi-python/issues/823)
      - `ddc_q_source` [#823](https://github.com/ni/nimi-python/issues/823)
      - `digital_gain` [#823](https://github.com/ni/nimi-python/issues/823)
      - `digital_offset` [#823](https://github.com/ni/nimi-python/issues/823)
      - `dither_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
      - `fetch_interleaved_iq_data` [#823](https://github.com/ni/nimi-python/issues/823)
      - `fractional_resample_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
      - `overflow_error_reporting` [#823](https://github.com/ni/nimi-python/issues/823)
      - `adjust_pretrigger_samples_5102` [#822](https://github.com/ni/nimi-python/issues/822)
      - `five_v_out_output_terminal` [#822](https://github.com/ni/nimi-python/issues/822)
      - `clock_sync_pulse_source` [#822](https://github.com/ni/nimi-python/issues/822)
      - `device_number` [#822](https://github.com/ni/nimi-python/issues/822)
      - `fetch_interleaved_data` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_from_pfi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_from_rtsi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_from_star_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_to_pfi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_to_rtsi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `trigger_to_star_delay` [#822](https://github.com/ni/nimi-python/issues/822)
      - `slave_trigger_delay` [#822](https://github.com/ni/nimi-python/issues/822)
  - Methods removed
      - `get_frequency_response()` [#823](https://github.com/ni/nimi-python/issues/823)
      - `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)

#### [niscope] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
  - `Session.fetch()`, `Session.read()` and `Session.fetch_into()` updated
      - Takes additional parameters that modify fetch behavior
      - Add resulting record as part of the waveform info
      - Channel name and record number added to waveform info
      - See documentation for [fetch](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch),
           [read](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.read),
           and [fetch_into](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch_into) for more details.
  - Rename `wfm` parameter to `waveform` in `fetch()` and `fetch_into()`
  - Enum values and attribute names that start with an underscore + digit have been renamed
         - `Session._5102_adjust_pretrigger_samples` --> `Session.adjust_pretrigger_samples_5102`
         - `Session._5v_out_output_terminal` --> `Session.five_v_out_output_terminal`
         - `ExportableSignals._5V_OUT` --> `ExportableSignals.FIVE_V_OUT`
         - `FlexFIRAntialiasFilterType._48_TAP_STANDARD` --> `FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_STANDARD`
         - `FlexFIRAntialiasFilterType._48_TAP_HANNING` --> `FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_HANNING`
         - `FlexFIRAntialiasFilterType._16_TAP_HANNING` --> `FlexFIRAntialiasFilterType.SIXTEEN_TAP_HANNING`
         - `FlexFIRAntialiasFilterType._8_TAP_HANNING` --> `FlexFIRAntialiasFilterType.EIGHT_TAP_HANNING`
         - `VideoSignalFormat._480I_59_94_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_480I_59_94_FIELDS_PER_SECOND`
         - `VideoSignalFormat._480I_60_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_480I_60_FIELDS_PER_SECOND`
         - `VideoSignalFormat._480P_59_94_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_480P_59_94_FRAMES_PER_SECOND`
         - `VideoSignalFormat._480P_60_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_480P_60_FRAMES_PER_SECOND`
         - `VideoSignalFormat._576I_50_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_576I_50_FIELDS_PER_SECOND`
         - `VideoSignalFormat._576P_50_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_576P_50_FRAMES_PER_SECOND`
         - `VideoSignalFormat._720P_50_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_50_FRAMES_PER_SECOND`
         - `VideoSignalFormat._720P_59_94_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_59_94_FRAMES_PER_SECOND`
         - `VideoSignalFormat._720P_60_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_60_FRAMES_PER_SECOND`
         - `VideoSignalFormat._1080I_50_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_50_FIELDS_PER_SECOND`
         - `VideoSignalFormat._1080I_59_94_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_59_94_FIELDS_PER_SECOND`
         - `VideoSignalFormat._1080I_60_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_60_FIELDS_PER_SECOND`
         - `VideoSignalFormat._1080P_24_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080P_24_FRAMES_PER_SECOND`
  - `Session.cal_self_calibration()` renamed to `Session.self_cal()` to match other drivers - issue [#615](https://github.com/ni/nimi-python/issues/615)
- Removed
  - Following properties are now removed (use parameters to fetch calls):
      - `fetch_relative_to`
      - `fetch_offset`
      - `fetch_record_number`
      - `fetch_num_records`
  - Removed `number_of_coefficients` parameter from `get_equalization_filter_coefficients()`
  - Removed Measurement Library waveform methods and properties - issue [#809](https://github.com/ni/nimi-python/issues/809)
      - `actual_meas_wfm_size()`
      - `add_waveform_processing()`
      - `clear_waveform_processing()`
      - `fetch_array_measurement()`
      - `clear_waveform_measurement_stats()`
      - `fetch_measurement()`
      - `fetch_measurement_stats()`
      - `read_measurement()`
      - `configure_ref_levels()`
      - `meas_ref_level_units`
      - `meas_other_channel`
      - `meas_hysteresis_percent`
      - `meas_last_acq_histogram_size`
      - `meas_voltage_histogram_size`
      - `meas_voltage_histogram_low_volts`
      - `meas_voltage_histogram_high_volts`
      - `meas_time_histogram_size`
      - `meas_time_histogram_low_volts`
      - `meas_time_histogram_high_volts`
      - `meas_time_histogram_low_time`
      - `meas_time_histogram_high_time`
      - `meas_polynomial_interpolation_order`
      - `meas_interpolation_sampling_factor`
      - `meas_filter_cutoff_freq`
      - `meas_filter_center_freq`
      - `meas_filter_ripple`
      - `meas_filter_transient_waveform_percent`
      - `meas_filter_type`
      - `meas_filter_order`
      - `meas_filter_taps`
      - `meas_chan_low_ref_level`
      - `meas_chan_mid_ref_level`
      - `meas_chan_high_ref_level`
      - `meas_filter_width`
      - `meas_fir_filter_window`
      - `meas_array_gain`
      - `meas_array_offset`
      - `meas_percentage_method`
      - `fetch_meas_num_samples`

#### [niscope] 0.7.0 - 2018-02-20
- Added
  - Repeated capablilites - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion:
      `channel` repeated capability
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - `niscope.Session()` no longer takes id_query parameter (Fix [#670](https://github.com/ni/nimi-python/issues/670))
  - The following functions timeout, delay or holdoff parameters now is required to be a `datetime.timedelta()` object:
      `configure_trigger_digital()`
      `configure_trigger_edge()`
      `configure_trigger_hysteresis()`
      `configure_trigger_software()`
      `configure_trigger_video()`
      `configure_trigger_window()`
      `fetch()`
      `fetch_measurement_stats()`
      `read()`
- Removed
  - Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
      `BoolEnableDisable` - `P2P_ENABLED`, `P2P_ADVANCED_ATTRIBUTES_ENABLED`, `P2P_ONBOARD_MEMORY_ENABLED`
      `BoolEnableDisableChan` - `CHANNEL_ENABLED`
      `BoolEnableDisableIQ` - `FETCH_INTERLEAVED_IQ_DATA`
      `BoolEnableDisableRealtime` - `HORZ_ENFORCE_REALTIME`
      `BoolEnableDisableTIS` - `ENABLE_TIME_INTERLEAVED_SAMPLING`

#### [niscope] 0.6.0 - 2017-12-20
- Added
  - (Common) `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
  - `fetch_into` for high-performance fetch using numpy.array. Supported element types:
      - `numpy.float64`
      - `numpy.int8`
      - `numpy.int16`
      - `numpy.int32`
- Changed
  - Added default values for timeout on all fetch and read functions.
  - Property input_impedance no longer uses enum InputImpedance.
- Removed
  - `AddWaveformProcessing` - See #667 for rationale
  - `ClearWaveformProcessing` - See #667 for rationale
  - `FetchArrayMeasurement` - See #667 for rationale

#### [niscope] 0.5.0 - 2017-11-27
- Added
  - Initial release
---

### nise (NI Switch Executive)

- [Unreleased](#nise-unreleased)
- [1.4.9](#nise-149---2025-02-26)
- [1.4.8](#nise-148---2024-04-26)
- [1.4.6](#nise-146---2023-09-11)
- [1.4.5](#nise-145---2023-06-12)
- [1.4.4](#nise-144---2023-04-14)
- [1.4.3](#nise-143---2022-12-16)
- [1.4.1](#nise-141---2021-08-23)
- [1.3.2](#nise-132---2020-09-18)
- [1.3.1](#nise-131---2020-06-08)
- [1.3.0](#nise-130---2020-05-21)
- [1.2.1](#nise-121---2020-04-21)
- [1.2.0](#nise-120---2020-03-06)
- [1.1.5](#nise-115---2019-11-22)
- [1.1.4](#nise-114---2019-11-19)
- [1.0.0](#nise-100---2019-10-21)
- [0.2.2](#nise-022---2019-06-06)
- [0.2.0](#nise-020---2018-10-25)
- [0.1.0](#nise-010---2018-10-17)

#### [nise] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nise] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nise] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [nise] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7

#### [nise] 1.4.5 - 2023-06-12
- Removed
  - (Common) `easy_install` support

#### [nise] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [nise] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
- Removed
  - (Common) Support for Python 3.6

#### [nise] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [nise] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nise] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0



#### [nise] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nise] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```
      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [nise] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [nise] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nise] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs
- Changed
  - Version updated to 1.1.4 to match other released nimi-python modules

#### [nise] 1.0.0 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.
  - Update to 1.0 - now ready for production use

#### [nise] 0.2.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata

#### [nise] 0.2.0 - 2018-10-25
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [nise] 0.1.0 - 2018-10-17
- Added
  - Initial Release
---

### niswitch (NI-SWITCH)

- [Unreleased](#niswitch-unreleased)
- [1.4.9](#niswitch-149---2025-02-26)
- [1.4.8](#niswitch-148---2024-04-26)
- [1.4.6](#niswitch-146---2023-09-11)
- [1.4.5](#niswitch-145---2023-06-12)
- [1.4.4](#niswitch-144---2023-04-14)
- [1.4.3](#niswitch-143---2022-12-16)
- [1.4.1](#niswitch-141---2021-08-23)
- [1.3.3](#niswitch-133---2021-02-26)
- [1.3.2](#niswitch-132---2020-09-18)
- [1.3.1](#niswitch-131---2020-06-08)
- [1.3.0](#niswitch-130---2020-05-21)
- [1.2.1](#niswitch-121---2020-04-21)
- [1.2.0](#niswitch-120---2020-03-06)
- [1.1.5](#niswitch-115---2019-11-22)
- [1.1.4](#niswitch-114---2019-11-19)
- [1.1.3](#niswitch-113---2019-10-21)
- [1.1.2](#niswitch-112---2019-06-06)
- [1.1.0](#niswitch-110---2018-10-25)
- [1.0.1](#niswitch-101---2018-10-17)
- [1.0.0](#niswitch-100---2018-06-08)
- [0.9.0](#niswitch-090---2018-05-22)
- [0.8.0](#niswitch-080---2018-04-27)
- [0.7.0](#niswitch-070---2018-02-20)
- [0.6.0](#niswitch-060---2017-12-20)
- [0.5.0](#niswitch-050---2017-11-27)
- [0.4.0](#niswitch-040---2017-11-07)
- [0.3.0](#niswitch-030---2017-10-13)
- [0.2.0](#niswitch-020---2017-09-20)

#### [niswitch] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [niswitch] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [niswitch] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [niswitch] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7


#### [niswitch] 1.4.5 - 2023-06-12
- Added
  - Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
- Removed
  - (Common) `easy_install` support

#### [niswitch] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [niswitch] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
  - MeasurementLink support
- Changed
  - Fix [#1652](https://github.com/ni/nimi-python/issues/1652): Topology constants haven't been updated on help page
- Removed
  - (Common) Support for Python 3.6

#### [niswitch] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [niswitch] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [niswitch] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [niswitch] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [niswitch] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```

      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`

#### [niswitch] 1.2.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)

#### [niswitch] 1.1.5 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [niswitch] 1.1.4 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [niswitch] 1.1.3 - 2019-10-21
- Changed
  - (Common) The development status in `setup.py` will be based on the module version:
      - version >= 1.0
        - .devN or .aN - Alpha
        - .bN, .cN or .rcN - Beta
        - \<nothing\> or .postN - Stable
      - version < 1.0 and version >= 0.5 - Beta
      - version < 0.5 - Alpha
  - (Common) Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.

#### [niswitch] 1.1.2 - 2019-06-06
- Changed
  - (Common) Switched to slightly different metadata format - Actual `True`/`False` instead of strings
  - (Common) New internal process for generating metadata

#### [niswitch] 1.1.0 - 2018-10-25
- Changed
  - (Common) Updated generated metadata
  - (Common) Updated "Driver Version Tested Against"
  - (Common) Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)

#### [niswitch] 1.0.1 - 2018-10-17
- Added
  - (Common) Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
  - (Common) \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
- Changed
  - (Common) No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
  - (Common) Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)

#### [niswitch] 1.0.0 - 2018-06-08
- Removed
  - (Common) Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
  - `cabled_module_scan_advanced_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `cabled_module_trigger_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `master_slave_scan_advanced_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `master_slave_trigger_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `parsed_scan_list` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `trigger_mode` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `scan_advanced_polarity` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `trigger_input_polarity` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `configure_scan_list()` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `configure_scan_trigger()` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `route_trigger_input()` - [#881](https://github.com/ni/nimi-python/issues/881)
  - `set_continuous_scan()` - [#881](https://github.com/ni/nimi-python/issues/881)

#### [niswitch] 0.9.0 - 2018-05-22
- Added
  - (Common) Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
  - (Common) Fix thread-safety issues by using IVI session lock where aplicable
- Changed
  - (Common) `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
  - (Common) Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
- Removed
  - (Common) IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
      - `engine_major_version`
      - `engine_minor_version`
      - `engine_revision`
      - `primary_error`
      - `secondary_error`
      - `error_elaboration`
      - `io_session_type`
      - `io_session` / `visa_rm_session`
      - `group_capabilities`
      - `interchange_check`
      - `range_check`
      - `record_coercions`
      - `specific_driver_class_spec_major_version`
      - `specific_driver_class_spec_minor_version`
      - `query_instrument_status`
      - `cache`
      - `specific_driver_prefix`

#### [niswitch] 0.8.0 - 2018-04-27
- Changed
  - (Common) All exceptions raised by the Python bindings inherit from `<driver>.Error`
  - (Common) Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
     - This encapsulates any error that is returned by the underlying driver
  - (Common) All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)

#### [niswitch] 0.7.0 - 2018-02-20
- Changed
  - (Common) Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
      - Key/Value pairs approporiate for desired behavior
       ``` python
       session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
       ```
  - (Common) Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
  - (Common) All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - (Common) All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
  - The following functions timeout, delay or holdoff parameters now is required to be a `datetime.timedelta()` object:
      - `configure_scan_trigger()`
      - `wait_for_debounce()`
      - `wait_for_scan_complete()`

#### [niswitch] 0.6.0 - 2017-12-20
- Added
  - (Common) `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
- Removed
  - Removed `init_with_topology`. Clients should use `niswitch.Session` constructor. See [#660](https://github.com/ni/nimi-python/issues/660).

#### [niswitch] 0.5.0 - 2017-11-27
- Removed
  - (Common) enum definitions that are not referenced by a function and/or an attributes

#### [niswitch] 0.4.0 - 2017-11-07
- Changed
  - (Common) Simplified examples by removing try/except
  - (Common) **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
- Removed
  - Support for `is_debounced` and `is_scanning` functions. Instead use the attribute of the same name.

#### [niswitch] 0.3.0 - 2017-10-13
- Added
  - (Common) Support for ViInt64 (64-bit integers)
- Changed
  - (Common) Modified how methods with repeated capabilities are invoked. There's no longer (for example) a `channel_name` input. Instead:
      ``` python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
  - (Common) Enum value documentation lists the fully qualified name - this is to allow easy copy/paste
  - Added default values to some parameters.
- Removed
  - Removed methods that aren’t useful in the Python bindings.

#### [niswitch] 0.2.0 - 2017-09-20
- Added
  - Initial release
---

### nitclk (NI-TClk)

- [Unreleased](#nitclk-unreleased)
- [1.4.9](#nitclk-149---2025-02-26)
- [1.4.8](#nitclk-148---2024-04-26)
- [1.4.6](#nitclk-146---2023-09-11)
- [1.4.5](#nitclk-145---2023-06-12)
- [1.4.4](#nitclk-144---2023-04-14)
- [1.4.3](#nitclk-143---2022-12-16)
- [1.4.1](#nitclk-141---2021-08-23)
- [1.3.3](#nitclk-133---2021-02-26)
- [1.3.2](#nitclk-132---2020-09-18)
- [1.3.1](#nitclk-131---2020-06-08)
- [1.3.0](#nitclk-130---2020-05-21)
- [1.2.1](#nitclk-121---2020-04-21)
- [1.0.0](#nitclk-100---2020-03-06)
- [0.3.1](#nitclk-031---2019-11-22)
- [0.3.0](#nitclk-030---2019-11-19)
- [0.1.0](#nitclk-010---2019-10-21)

#### [nitclk] Unreleased
- Added
  - Python 3.14 Support
- Changed
- Removed
  - Python 3.9 Support

#### [nitclk] 1.4.9 - 2025-02-26
- Added
  - (Common) Support for Python 3.13
- Changed
  - (Common) Fix [#2069](https://github.com/ni/nimi-python/issues/2069)
- Removed
  - (Common) Support for Python 3.8

#### [nitclk] 1.4.8 - 2024-04-26
- Added
  - (Common) Support for Python 3.12

#### [nitclk] 1.4.6 - 2023-09-11
- Changed
  - (Common) Fix [#1970](https://github.com/ni/nimi-python/issues/1970): Incorrect error when driver runtime not installed.
  - (Common) Fix [#1998](https://github.com/ni/nimi-python/issues/1998): nimi-python APIs inefficiently allocate Python arrays.
- Removed
  - (Common) Support for Python 3.7

#### [nitclk] 1.4.5 - 2023-06-12
- Removed
  - (Common) `easy_install` support

#### [nitclk] 1.4.4 - 2023-04-14
- Added
  - (Common) Support for Python 3.11
- Changed
  - (Common) Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.

#### [nitclk] 1.4.3 - 2022-12-16
- Added
  - (Common) Support for Python 3.10
- Removed
  - (Common) Support for Python 3.6

#### [nitclk] 1.4.1 - 2021-08-23
- Added
  - (Common) Support for Python 3.9
- Removed
  - (Common) Support for Python 3.5

#### [nitclk] 1.3.3 - 2021-02-26
- Added
  - nitclk_niscope_synchronize_with_trigger.py to demonstrate homogenous triggering.
- Removed
  - nitclk_configure.py as it did not do anything.

#### [nitclk] 1.3.2 - 2020-09-18
- Changed
  - (Common) Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

#### [nitclk] 1.3.1 - 2020-06-08
- Changed
  - (Common) Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
  - (Common) Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0

#### [nitclk] 1.3.0 - 2020-05-21
- Changed
  - (Common) Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.

#### [nitclk] 1.2.1 - 2020-04-21
- Added
  - (Common) Support for chained repeated capabilities. This allows things like
      ``` python
      session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
      ```
      The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`
- Changed
  - Version updated to 1.2.1 to match other released nimi-python modules

#### [nitclk] 1.0.0 - 2020-03-06
- Added
  - (Common) Zip file per driver for all examples and any helper files
  - (Common) Link to zip file on examples documentation
  - (Common) Support for Python 3.8
- Changed
  - (Common) `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - (Common) `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
  - Method parameters and properties that are time based now take or return a `datetime.timedelta` object
- Removed
  - (Common) Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
  - (Common) Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
  - (Common) PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)
  - Ability to pass an integer as a session / session reference
  - `nitclk.SessionReference.script_trigger_master_session` removed - repeated capabilities not supported on `nitclk` attributes - [#1221](https://github.com/ni/nimi-python/issues/1221)

#### [nitclk] 0.3.1 - 2019-11-22
- Changed
  - (Common) Fix #1140: Linux support was accidentally broken.
  - (Common) Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.

#### [nitclk] 0.3.0 - 2019-11-19
- Added
  - (Common) Support for Python 3.8
  - (Common) `ViUInt8` is now a valid type in APIs

#### [nitclk] 0.1.0 - 2019-10-21
- Added
  - Initial support


The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

<!--
- [Unreleased](#nitclk-unreleased)

#### [nitclk] Unreleased
- Added
- Changed
- Removed
-->
````

<!--NI_OSS_SOURCE repo=nimi-python path=CONTRIBUTING.md sha256=954b6f4f2dd2878fde00880aae633028130142723d0ff057ac02bc5320c2fd6a bytes=12817 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nimi-python`
- source_path: `CONTRIBUTING.md`
- sha256: `954b6f4f2dd2878fde00880aae633028130142723d0ff057ac02bc5320c2fd6a`
- bytes: 12817

````markdown
Contributing to nimi-python
===========================

Contributions to **[`nimi-python`](https://github.com/ni/nimi-python)** are welcome from all!

**[`nimi-python`](https://github.com/ni/nimi-python)** is managed via [Git](https://git-scm.com), with the canonical
upstream repository hosted on [GitHub](http://developercertificate.org/).

**[`nimi-python`](https://github.com/ni/nimi-python)** follows a pull request model for development.
If you wish to contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/)
for more details.


Setting up your system
----------------------

In order to have the ability to build and run the tests you will need a few things to be set up on your system.

### Windows:

- Install and enable [Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
- Install the following in **Windows Subsystem for Linux**:
  - GNU Make: ``sudo apt-get install make``
  - zip: ``sudo apt-get install zip``
  - 64-bit [Python](https://www.python.org/downloads/)
    -- Use the version that `build_test` uses. See `envlist` definition in [tox.ini](./tox.ini)

### macOS:

- Install [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
- Install command line developer tools
- Install [Python](https://www.python.org/downloads/)
    - Use the version that `build_test` uses. See `envlist` definition in [tox.ini](./tox.ini)

### Linux:

- Install Python: ``sudo apt-get install python3-pip``
    - Use the version that `build_test` uses. See `envlist` definition in [tox.ini](./tox.ini)

### All:

Once your system has been setup with the above, install required additional Python modules using PyPI.

        sudo pip install pytest tox --upgrade


Building **[`nimi-python`](https://github.com/ni/nimi-python)**
---------------------------------------------------------------

1. Fork [the repository](https://github.com/ni/nimi-python) on GitHub and clone it to your local system.
1. Initialize and fetch submodules (also re-run this after `git pull` to keep the submodule up to date):

       git submodule update --init --recursive

   Optionally, configure git to do this automatically after `git fetch`, `git pull` and `git checkout`:

       git config submodule.recurse true

1. On a terminal, navigate to the **[`nimi-python`](https://github.com/ni/nimi-python)** root
   directory. Then run

       tox

   It will do the following, for each driver:

    * Validate the code generator and build scripts
    * Generate Python bindings
    * Generate [RST documentation](http://www.sphinx-doc.org/)
     * Create installer packages
     * Run [flake8](http://flake8.pycqa.org/)
     * Generate [HTML documentation](http://www.sphinx-doc.org/)
     * Iterate over all installed and supported Python versions and run unit tests

1. To clean everything and start fresh

        tox -e clean


Updating submodules
-------------------

To update the submodule (e.g., ni-apis) to the latest version from its remote repository:

    git submodule update --remote

This fetches and checks out the latest commit from the submodule's default branch. You'll periodically need to do this to pick up the latest changes.


Running the system tests
------------------------

**[`nimi-python`](https://github.com/ni/nimi-python)** includes system tests that exercise the Python modules against the real driver runtimes. Our CI includes invoking [`nimibot`](https://github.com/ni/nimi-python/wiki/nimibot-System-Test-machine) to run these tests for you on PRs pending admin approval.

But it is recommended that during development you run the system tests locally, especially if the areas of the code affected by your changes may impact interaction with the driver runtimes.

In order to run the **[nimi-python](https://github.com/ni/nimi-python)** system tests locally:

### Install the corresponding driver runtimes.

Download and install the latest versions for the supported driver runtimes from [ni.com](http://www.ni.com/downloads/ni-drivers/):
* NI-DCPower
* NI-Digital Pattern Driver
* NI-DMM
* NI-FGEN
* NI-SCOPE
* NI-SWITCH
* NI Switch Executive

NI-ModInst and NI-TClk are included with the above, they have no separate installers.

### Install build artifacts

After you have successfully built **[nimi-python](https://github.com/ni/nimi-python)**, install the locally built PyPI packages using PyPI:

    find generated | grep \.whl | xargs sudo python3 -m pip install -U

Once the Python bindings are installed, run the system tests for the desired driver. For example:

    pytest src/nidmm/system_tests -c generated/nidmm/tox-system_tests.ini

You can also use ``tox`` to run the system tests for the desired driver, *using all installed Python versions*. For example:

    tox -c generated/nidmm/tox-system_tests.ini


Contributing
------------

After you've verified that you can successfully build and run system tests for
**[`nimi-python`](https://github.com/ni/nimi-python)**, you may
begin contributing to to the project.

1. If applicable, write a failing test for the new feature / bugfix.
    * If you are modifying the code generator, write new [NI-FAKE](src/nifake/tests) unit
      tests. If the new functionality requires changes to [metadata](src/nifake/metadata),
      apply those to NI-FAKE.
    * If you are modifying driver-specific metadata, write new
      [system tests](src/nidmm/system_tests).
1. Make your change.
1. Verify all tests, including the new ones, pass.
1. Update CHANGELOG.md for customer-visible changes.
    * Put the change into the Unreleased section for each package that it applies to.
    * If it's a common change for all the packages, include the `(Common)` string before the newly added change in [CHANGELOG.md].
    * DO NOT MENTION: Internal-only changes like refactors or test improvements.
1. Commit modifications to generated files.
1. On GitHub, send a New pull request to the main repository's master branch. GitHub
   pull requests are the expected method of code collaboration on this project.

Release Process
---------------
1. Pre-Release Steps
    1. Checkout the master branch and pull down the latest changes
        ```bash
        git checkout master
        # Discard all local changes
        git restore .
        # Merge changes from upstream
        git pull upstream master
        ```
    1. Build master to ensure it is in a good state and ready for release
        ```bash
        tox -e clean
        tox
        ```
    1. Ensure no commits are made on ni/nimi-python/master until the release is complete
    1. Create and checkout a branch for release-related changes
    1. Perform Version Bump (If Needed)
        * If you need to upgrade the major or minor versions, include any of the following parameters:
           * --increment-major-version - To increment the major version of package. This will update the version to (N+1).X.X.dev0
           * --increment-minor-version - To increment the minor version of package. This will update the version to X.(N+1).X.dev0
             * Example: `python3 tools/build_release.py --increment-minor-version`
        * If you need to update the version for any specific driver(s), include the `drivers` parameter. By default, all drivers will be considered.
          For example: 
              ```bash
              python3 tools/build_release.py --drivers nidcpower --increment-minor-version
              ```
        * Commit to branch
    1. Update [CHANGELOG.md](./CHANGELOG.md)
        * For packages that are releasing:
          * Delete empty (i.e. No changes) sub-sections under "Unreleased" section 
          * Remove the Unreleased section from the TOC if there are no changes for the package.
          * Change the "Unreleased" header to the version of the release
          * Change [Unreleased] in TOC to the version of the release
        * Commit to branch
    1. Update release versions
        * `python3 tools/build_release.py --update-for-release`
            * For each module, this will drop the .devN from our versions in config_addon.py and update the LATEST_RELEASE versions to match.
            * If you need to release any specific module(s), include the `drivers` parameter. 
          For example: 
              ```bash
              python3 tools/build_release.py --drivers nidcpower --update-for-release
              ```
        * Commit to branch
    1. Clean and build to update generated files with new version
        * `python3 tools/build_release.py --build`
        * Commit to branch
    1. Create a pull request
        * It should contain all the changes made so far
        * Get the pull request reviewed but DO NOT merge to master yet
1. Release Steps
    1. Wait until the pull request has been approved
    1. Upload the releases to PyPI
        * `python3 tools/build_release.py --upload`
        * If you need to upload any specific module(s), include the `drivers` parameter. 
        For example: 
             ```bash
            python3 tools/build_release.py --drivers nidcpower --upload
            ```
        * You will need to type in your PyPI credentials
    1. Merge the pull request to origin/master
    1. For each package released, create a release on GitHub using the module's portion from the changelog for this release for the description
        * The release tag should be named as follows: `MODULE_NAME-version`.
          * Example: `nidcpower-1.5.0`.
          * This tag format allows the individual `Read the Docs` projects to determine whether a release applies to them.
        * Add the ZIP files under `generated/examples` for each module (not just the releasing one) as a release artifact.
          * Internal test code will only look for the latest release tag and expect it to have examples attached for any module
        * This should trigger the [check_latest_release](.github/workflows/check_latest_release.yml) workflow. Check the [results](https://github.com/ni/nimi-python/actions/workflows/check_latest_release.yml) before continuing.
1. Post-Release Steps
    1. Create and checkout another branch for post-release changes
    1. Update the module version for a patch version upgrade. This will update the version to X.X.(N+1).dev0
        * `python3 tools/build_release.py --increment-patch-version`
        * If you need to update any specific module(s), include the `drivers` parameter. 
        For example: 
             ```bash
            python3 tools/build_release.py --drivers nidcpower --increment-patch-version
            ```
        * Commit to branch
    1. Clean and build to update generated files with new version
        * `python3 tools/build_release.py --build`
        * Ensure that all changes made as part of build command are specific to intended drivers.
        * Commit to branch
    1. Update changelog
        * Copy Unreleased section from the bottom of the changelog. Modify the package name in the example and TOC. Paste the modified section at the top of intended package's changelog and add a corresponding link to it in the package's TOC.
        * Commit to branch
    1. Create a pull request containing post-release changes and get it merged

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

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/nimi-python/blob/master/LICENSE) for details about
how **[`nimi-python`](https://github.com/ni/nimi-python)** is licensed.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/about.inc sha256=10a0e26672f573c766555399351d8a64fa9a91b4fca183730ede4e8f2ebbbcd2 bytes=1163 -->
## FILE: docs/_static/about.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/about.inc`
- sha256: `10a0e26672f573c766555399351d8a64fa9a91b4fca183730ede4e8f2ebbbcd2`
- bytes: 1163

````text
.. _about-section:

About
=====

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. The
following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-Digital Pattern Driver (Python module: nidigital)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-ModInst (Python module: nimodinst)
* NI-RFSG (Python module: nirfsg)
* NI-SCOPE (Python module: niscope)
* NI Switch Executive (Python module: nise)
* NI-SWITCH (Python module: niswitch)
* NI-TClk (Python module: nitclk)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is
called through its public C API using the `ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions.

NI created and supports **nimi-python**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/contributing.inc sha256=40835e499a46927ec583c85e979ce565d4cc12e189a93810f24e1ccf2e9f5e72 bytes=217 -->
## FILE: docs/_static/contributing.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/contributing.inc`
- sha256: `40835e499a46927ec583c85e979ce565d4cc12e189a93810f24e1ccf2e9f5e72`
- bytes: 217

````text
Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/documentation.inc sha256=28c5ace5e4a910d6a8a6e563d10efa6232c3a1d77c5125fe605c5fdbe55f9bf1 bytes=439 -->
## FILE: docs/_static/documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/documentation.inc`
- sha256: `28c5ace5e4a910d6a8a6e563d10efa6232c3a1d77c5125fe605c5fdbe55f9bf1`
- bytes: 439

````text
.. _documentation-section:

Documentation
=============

Documentation is available on **Read the Docs**:

- https://nidcpower.readthedocs.io
- https://nidigital.readthedocs.io
- https://nidmm.readthedocs.io
- https://nifgen.readthedocs.io
- https://nimodinst.readthedocs.io
- https://nirfsg.readthedocs.io
- https://niscope.readthedocs.io
- https://nise.readthedocs.io
- https://niswitch.readthedocs.io
- https://nitclk.readthedocs.io
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/installation.inc sha256=24f4dfab63ff57c0bc863b90d35aa245ffbecabfb1b508dde7754abf9c8fd0bd bytes=951 -->
## FILE: docs/_static/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/installation.inc`
- sha256: `24f4dfab63ff57c0bc863b90d35aa245ffbecabfb1b508dde7754abf9c8fd0bd`
- bytes: 951

````text
.. _installation-section:

Installation
============

Driver specific installation instructions can be found on **Read the Docs**:

* `nidcpower <https://nidcpower.readthedocs.io/en/latest/nidcpower.html#installation>`_
* `nidigital <https://nidigital.readthedocs.io/en/latest/nidigital.html#installation>`_
* `nidmm <https://nidmm.readthedocs.io/en/latest/nidmm.html#installation>`_
* `nifgen <https://nifgen.readthedocs.io/en/latest/nifgen.html#installation>`_
* `nimodinst <https://nimodinst.readthedocs.io/en/latest/nimodinst.html#installation>`_
* `nirfsg <https://nirfsg.readthedocs.io/en/latest/nirfsg.html#installation>`_
* `niscope <https://niscope.readthedocs.io/en/latest/niscope.html#installation>`_
* `nise <https://nise.readthedocs.io/en/latest/nise.html#installation>`_
* `niswitch <https://niswitch.readthedocs.io/en/latest/niswitch.html#installation>`_
* `nitclk <https://nitclk.readthedocs.io/en/latest/nitclk.html#installation>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/license.inc sha256=1d82f8766c0491ac793c73cfb993be55bc50ecc0ae329adc209cd935b5b91735 bytes=544 -->
## FILE: docs/_static/license.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/license.inc`
- sha256: `1d82f8766c0491ac793c73cfb993be55bc50ecc0ae329adc209cd935b5b91735`
- bytes: 544

````text
.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


**gRPC Features**

For driver APIs that support it, passing a GrpcSessionOptions instance as a parameter to Session.__init__() is
subject to the NI General Purpose EULA (`see NILICENSE <https://github.com/ni/nimi-python/blob/master/NILICENSE>`_).
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidcpower_documentation.inc sha256=1d5b34bd7ab9acb83b0f539a093d11d3883c133a9652f4b74536664bef8b5f72 bytes=129 -->
## FILE: docs/_static/nidcpower_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidcpower_documentation.inc`
- sha256: `1d5b34bd7ab9acb83b0f539a093d11d3883c133a9652f4b74536664bef8b5f72`
- bytes: 129

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nidcpower.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidcpower_usage.inc sha256=93a1a83e6ff7441143539913a172f1b7b63685a9c8fc447aef372db9087de382 bytes=1617 -->
## FILE: docs/_static/nidcpower_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidcpower_usage.inc`
- sha256: `93a1a83e6ff7441143539913a172f1b7b63685a9c8fc447aef372db9087de382`
- bytes: 1617

````text
Usage
------

The following is a basic example of using the **nidcpower** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nidcpower
    # Configure the session.

    with nidcpower.Session(resource_name='PXI1Slot2/0') as session:
        session.measure_record_length = 20
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = 5.0

        session.commit()
        print('Effective measurement rate: {} S/s'.format(session.measure_record_delta_time / 1))

        samples_acquired = 0
        print('Channel           Num  Voltage    Current    In Compliance')
        row_format = '{0:15} {1:3d}    {2:8.6f}   {3:8.6f}   {4}'
        with session.initiate():
            channel_indices = '0-{}'.format(session.channel_count - 1)
            channels = session.get_channel_names(channel_indices)
            for i, channel_name in enumerate(channels):
                samples_acquired = 0
                while samples_acquired < 20:
                    measurements = session.channels[channel_name].fetch_multiple(count=session.fetch_backlog)
                    samples_acquired += len(measurements)
                    for i in range(len(measurements)):
                        print(row_format.format(channel_name, i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidcpower/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidigital_documentation.inc sha256=54e7b5dd95b8c1bf7475f41fd83a09a9ba6f828001cfe3996fbcf5e5dfa090a0 bytes=129 -->
## FILE: docs/_static/nidigital_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidigital_documentation.inc`
- sha256: `54e7b5dd95b8c1bf7475f41fd83a09a9ba6f828001cfe3996fbcf5e5dfa090a0`
- bytes: 129

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nidigital.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidigital_usage.inc sha256=9a8b7b01dc8648e8d701d38890cf538e40bd990f2a84a5e1f46149b17f83ae90 bytes=1913 -->
## FILE: docs/_static/nidigital_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidigital_usage.inc`
- sha256: `9a8b7b01dc8648e8d701d38890cf538e40bd990f2a84a5e1f46149b17f83ae90`
- bytes: 1913

````text
Usage
------

The following is a basic example of using the **nidigital** module to open a session to a digital pattern instrument,
source current, and measure both voltage and current using the PPMU on selected channels.

.. code-block:: python

    import nidigital
    import time

    with nidigital.Session(resource_name='PXI1Slot2') as session:

        channels = 'PXI1Slot2/0,PXI1Slot2/1'

        # Configure PPMU measurements
        session.channels[channels].ppmu_aperture_time = 0.000004
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

        session.channels[channels].ppmu_current_level_range = 0.000002
        session.channels[channels].ppmu_current_level = 0.000002
        session.channels[channels].ppmu_voltage_limit_high = 3.3
        session.channels[channels].ppmu_voltage_limit_low = 0

        # Sourcing
        session.channels[channels].ppmu_source()

        # Settling time between sourcing and measuring
        time.sleep(0.01)

        # Measuring
        current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

        print('{:<20} {:<10} {:<10}'.format('Channel Name', 'Current', 'Voltage'))
        for channel, current, voltage in zip(channels.split(','), current_measurements, voltage_measurements):
            print('{:<20} {:<10f} {:<10f}'.format(channel, current, voltage))

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidigital/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidmm_documentation.inc sha256=77ead61fe77383f2602284f795188775c4c08e05efcacda71748b8ebb6a03b6f bytes=125 -->
## FILE: docs/_static/nidmm_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidmm_documentation.inc`
- sha256: `77ead61fe77383f2602284f795188775c4c08e05efcacda71748b8ebb6a03b6f`
- bytes: 125

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nidmm.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nidmm_usage.inc sha256=0bb516eaf8b362467f0ecd90e74561493d0e33ebd38d498d3f8a3e7e163369fc bytes=518 -->
## FILE: docs/_static/nidmm_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nidmm_usage.inc`
- sha256: `0bb516eaf8b362467f0ecd90e74561493d0e33ebd38d498d3f8a3e7e163369fc`
- bytes: 518

````text
Usage
------

The following is a basic example of using the **nidmm** module to open a session to a DMM and perform a 5.5 digits of resolution voltage measurement in the 10 V range.

.. code-block:: python

    import nidmm
    with nidmm.Session("Dev1") as session:
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10.0, 5.5)
        print("Measurement: " + str(session.read()))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidmm/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nifgen_documentation.inc sha256=9c8b10dca171c2768c87ff91ddddfc741e8190823b06e44e2cd907ec4130efbf bytes=126 -->
## FILE: docs/_static/nifgen_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nifgen_documentation.inc`
- sha256: `9c8b10dca171c2768c87ff91ddddfc741e8190823b06e44e2cd907ec4130efbf`
- bytes: 126

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nifgen.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nifgen_usage.inc sha256=7c58856cf62ae74f46144d5f045d816556bebb8a836297ab655ced81c84d7e2c bytes=635 -->
## FILE: docs/_static/nifgen_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nifgen_usage.inc`
- sha256: `7c58856cf62ae74f46144d5f045d816556bebb8a836297ab655ced81c84d7e2c`
- bytes: 635

````text
Usage
------

The following is a basic example of using the **nifgen** module to open a session to a Function Generator and generate a sine wave for 5 seconds.

.. code-block:: python

    import nifgen
    import time
    with nifgen.Session("Dev1") as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform.SINE, amplitude=1.0, frequency=10000000, dc_offset=0.0, start_phase=0.0)
        with session.initiate():
            time.sleep(5)

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nifgen/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nimodinst_documentation.inc sha256=566c06f191d8694a87ae2935d27c25a4e55851b6e7a523001fda4fdd54a49532 bytes=129 -->
## FILE: docs/_static/nimodinst_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nimodinst_documentation.inc`
- sha256: `566c06f191d8694a87ae2935d27c25a4e55851b6e7a523001fda4fdd54a49532`
- bytes: 129

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nimodinst.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nimodinst_usage.inc sha256=ddd07595e6d606df2b3248ec59715c9ea4ab02934dcc55aa684345859af7f0db bytes=522 -->
## FILE: docs/_static/nimodinst_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nimodinst_usage.inc`
- sha256: `ddd07595e6d606df2b3248ec59715c9ea4ab02934dcc55aa684345859af7f0db`
- bytes: 522

````text
Usage
------

The following is a basic example of using the **nimodinst** module to retrieve information on all High Speed Digitizers currently in the system.

.. code-block:: python

    import nimodinst
    with nimodinst.Session("niscope") as session:
        for device in session:
            print("{: >20} {: >15} {: >10}".format(device.device_name, device.device_model, device.serial_number))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nimodinst/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nirfsg_documentation.inc sha256=6b7c2b5d740ca9921a9163ba1770eb93009666529bba587e9b1f66896246b38c bytes=126 -->
## FILE: docs/_static/nirfsg_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nirfsg_documentation.inc`
- sha256: `6b7c2b5d740ca9921a9163ba1770eb93009666529bba587e9b1f66896246b38c`
- bytes: 126

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nirfsg.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nirfsg_usage.inc sha256=a75c8a3450c571b720a8289a2f5bf934669fe08b6bc0247f39b5100dbdec38da bytes=843 -->
## FILE: docs/_static/nirfsg_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nirfsg_usage.inc`
- sha256: `a75c8a3450c571b720a8289a2f5bf934669fe08b6bc0247f39b5100dbdec38da`
- bytes: 843

````text
Usage
------

The following is a basic example of using the **nirfsg** module to open a session to an RF Signal Generator and generate a continuous wave (CW) signal.

.. code-block:: python

    import nirfsg

    # Configure the session
    with nirfsg.Session(resource_name='5841', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5841') as session:
        # Configure RF settings
        session.configure_rf(
            frequency=1e9,  # Frequency in Hz
            power_level=-10.0  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start signal generation
        with session.initiate():
            input("Press Enter to stop generation")

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsg/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/niscope_documentation.inc sha256=140081e842b9e7c3ca4228f6f938079fa7511b39f991ee4bfb0796c7f0e82181 bytes=127 -->
## FILE: docs/_static/niscope_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/niscope_documentation.inc`
- sha256: `140081e842b9e7c3ca4228f6f938079fa7511b39f991ee4bfb0796c7f0e82181`
- bytes: 127

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://niscope.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/niscope_usage.inc sha256=5986f27232d52bc3480d69eb3cde7c9bff8bc7eb1debe016c7b487f3f87b1ba7 bytes=1433 -->
## FILE: docs/_static/niscope_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/niscope_usage.inc`
- sha256: `5986f27232d52bc3480d69eb3cde7c9bff8bc7eb1debe016c7b487f3f87b1ba7`
- bytes: 1433

````text
Usage
------

The following is a basic example of using the **niscope** module to open a session to a High Speed Digitizer and capture a single record of 1000 points.

.. code-block:: python

    import niscope
    with niscope.Session("Dev1") as session:
        session.channels[0].configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.AC)
        session.channels[1].configure_vertical(range=10.0, coupling=niscope.VerticalCoupling.DC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=5, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[0,1].fetch(num_records=5)
        for wfm in waveforms:
            print('Channel {}, record {} samples acquired: {:,}\n'.format(wfm.channel, wfm.record, len(wfm.samples)))

        # Find all channel 1 records (Note channel name is always a string even if integers used in channel[])
        chan1 = [wfm for wfm in waveforms if wfm.channel == '0']

        # Find all record number 3
        rec3 = [wfm for wfm in waveforms if wfm.record == 3]

If you need faster fetch performance, or to directly interface with `SciPy <https://www.scipy.org/>`_, you can use the **fetch_into()** method instead of **fetch()**. See the fetch_into example.


`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/niscope/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nise_documentation.inc sha256=9a7bb36a926de437079c01cae1f0dc81f8c7a0f21b9cb7fc6205030783400159 bytes=124 -->
## FILE: docs/_static/nise_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nise_documentation.inc`
- sha256: `9a7bb36a926de437079c01cae1f0dc81f8c7a0f21b9cb7fc6205030783400159`
- bytes: 124

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nise.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nise_usage.inc sha256=1f356a657f1aff1ee612837eafe7e2725e3d65b56f3d4a0264f0286bbbccaa8a bytes=410 -->
## FILE: docs/_static/nise_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nise_usage.inc`
- sha256: `1f356a657f1aff1ee612837eafe7e2725e3d65b56f3d4a0264f0286bbbccaa8a`
- bytes: 410

````text
Usage
------

The following is a basic example of using the **nise** module to open a session to a Switch Executive Virtual Device and connect a routegroup.

.. code-block:: python

    import nise
    with nise.Session('SwitchExecutiveExample') as session:
        session.connect('DIOToUUT')

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nise/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/niswitch_documentation.inc sha256=cf4b45457c8709d7ffa501980c3188563e48e685177875031ad7e65d231c3602 bytes=128 -->
## FILE: docs/_static/niswitch_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/niswitch_documentation.inc`
- sha256: `cf4b45457c8709d7ffa501980c3188563e48e685177875031ad7e65d231c3602`
- bytes: 128

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://niswitch.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/niswitch_usage.inc sha256=4eabc0503afdc2d5d6de83692ec13f9bc22c41725fc1e818552bb5a89c4b5da0 bytes=397 -->
## FILE: docs/_static/niswitch_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/niswitch_usage.inc`
- sha256: `4eabc0503afdc2d5d6de83692ec13f9bc22c41725fc1e818552bb5a89c4b5da0`
- bytes: 397

````text
Usage
------

The following is a basic example of using the **niswitch** module to open a session to a Switch and connect channels.

.. code-block:: python

    import niswitch
    with niswitch.Session("Dev1") as session:
        session.connect(channel1='r0', channel2='c0')

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/niswitch/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nitclk_documentation.inc sha256=729d80136915d8d824367a8bdf4f27bcff782af0aa26ac2dde2cd051060eaeb6 bytes=126 -->
## FILE: docs/_static/nitclk_documentation.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nitclk_documentation.inc`
- sha256: `729d80136915d8d824367a8bdf4f27bcff782af0aa26ac2dde2cd051060eaeb6`
- bytes: 126

````text
.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nitclk.readthedocs.io>`_.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/nitclk_usage.inc sha256=23acdda5effd5132f7ff1d6b1a91c96f33606107c8d8299d77e5a3935374e576 bytes=239 -->
## FILE: docs/_static/nitclk_usage.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/nitclk_usage.inc`
- sha256: `23acdda5effd5132f7ff1d6b1a91c96f33606107c8d8299d77e5a3935374e576`
- bytes: 239

````text
Usage
------

The following is a basic example of using the **nitclk** module

.. code-block:: python

    import nitclk

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nitclk/examples>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/status_project.inc sha256=7c3bf8a393878d00348e3b11eb3f84de56fed858829f8bd0a9f0f4dccd149aad bytes=2008 -->
## FILE: docs/_static/status_project.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/status_project.inc`
- sha256: `7c3bf8a393878d00348e3b11eb3f84de56fed858829f8bd0a9f0f4dccd149aad`
- bytes: 2008

````text
Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         NI Modular Instrument driver APIs for Python.
Author       NI
===========  ============================================================================================================================

.. |BuildStatus| image:: https://api.travis-ci.com/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://codecov.io/github/ni/nimi-python/graph/badge.svg
    :alt: Test Coverage - master branch
    :target: https://codecov.io/github/ni/nimi-python

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/support.inc sha256=3f6b3c64bd6db6c1aba5e9ff33bd70099bdf183ad7eda9ee145ea44a42b1bffe bytes=628 -->
## FILE: docs/_static/support.inc

- repository: `ni/nimi-python`
- source_path: `docs/_static/support.inc`
- sha256: `3f6b3c64bd6db6c1aba5e9ff33bd70099bdf183ad7eda9ee145ea44a42b1bffe`
- bytes: 628

````text
.. _support-section:

Support / Feedback
==================

For support specific to the Python API, follow the processs in `Bugs / Feature Requests`_.
For support with hardware, the driver runtime or any other questions not specific to the Python API, please visit `NI Community Forums <https://forums.ni.com/>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to Python API, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/_static/theme_overrides.css sha256=0385360e0ad6701d9e05defd5c822d0ad203dee0bc68524525f4883e3198f33e bytes=313 -->
## FILE: docs/_static/theme_overrides.css

- repository: `ni/nimi-python`
- source_path: `docs/_static/theme_overrides.css`
- sha256: `0385360e0ad6701d9e05defd5c822d0ad203dee0bc68524525f4883e3198f33e`
- bytes: 313

````text
/* override table width restrictions */
.wy-table-responsive table td {
   /* !important prevents the common CSS stylesheets from overriding
      this as on RTD they are loaded after this stylesheet */
   white-space: normal !important;
}

.wy-table-responsive {
   overflow: visible !important;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidcpower/.readthedocs.yaml sha256=60a58b679e72c198448f35544d576f834b3b296680fa375067188af3a7673ad5 bytes=1885 -->
## FILE: docs/nidcpower/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nidcpower/.readthedocs.yaml`
- sha256: `60a58b679e72c198448f35544d576f834b3b296680fa375067188af3a7673ad5`
- bytes: 1885

````yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nidcpower/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nidcpower/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nidcpower/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidcpower/about_nidcpower.inc sha256=608583ae8dfa2b3db1ac107947592ea25004280382c9834fc3b14c64e2e3e589 bytes=500 -->
## FILE: docs/nidcpower/about_nidcpower.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidcpower/about_nidcpower.inc`
- sha256: `608583ae8dfa2b3db1ac107947592ea25004280382c9834fc3b14c64e2e3e589`
- bytes: 500

````text
.. _about-section:

About
=====

The **nidcpower** module provides a Python API for NI-DCPower. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidcpower** supports all the Operating Systems supported by NI-DCPower.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nidcpower**.
````
