# NI OSS SOURCE SNAPSHOT: datastore-python

<!--NI_OSS_SNAPSHOT repo=ni/datastore-python commit=f78bf987f5b630b942f3f214a6a09d754331a05f -->

<!--NI_OSS_SOURCE repo=datastore-python path=.github/actions/run_and_upload_unit_tests/action.yml sha256=7a76f88154f3fe90bbe3e283a58b6329ce84575bde36eee632bb44c3c74ab7bf bytes=1207 -->
## FILE: .github/actions/run_and_upload_unit_tests/action.yml

- repository: `ni/datastore-python`
- source_path: `.github/actions/run_and_upload_unit_tests/action.yml`
- sha256: `7a76f88154f3fe90bbe3e283a58b6329ce84575bde36eee632bb44c3c74ab7bf`
- bytes: 1207

````yaml
name: 'Run and upload unit tests'
description: 'Run unit tests using pytest and upload the results as an artifact.'
runs:
  using: "composite"
  steps:
    - name: Get OS version
      run: echo "osVersion=$ImageOS" >> "$GITHUB_ENV"
      shell: bash
    - name: Cache ni.datastore virtualenv
      uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
      with:
        path: ./.venv
        key: ni.datastore-${{ runner.os }}-py${{ env.pythonVersion }}-${{ hashFiles('./poetry.lock') }}
    - name: Install ni.datastore
      run: poetry install -v
      working-directory: .
      shell: bash
    - name: Run ni.datastore unit tests and code coverage
      run: poetry run pytest ./tests/unit -v --cov=ni.datastore --junitxml=test_results/ni.datastore-${{ env.osVersion }}-py${{ env.pythonVersion }}.xml
      working-directory: .
      shell: bash
    - name: Upload ni.datastore test results
      uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
      with:
        name: test_results_unit_ni.datastore_${{ env.osVersion }}_py${{ env.pythonVersion }}
        path: ${{ github.workspace }}/test_results/*.xml
      if: always()
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/CODEOWNERS sha256=37c32292770d5aaeae2bb89d6cc8160164735ccb6518d11f4c2a7f86947f14b9 bytes=36 -->
## FILE: .github/CODEOWNERS

- repository: `ni/datastore-python`
- source_path: `.github/CODEOWNERS`
- sha256: `37c32292770d5aaeae2bb89d6cc8160164735ccb6518d11f4c2a7f86947f14b9`
- bytes: 36

````text
* @csjall @dixonjoel @mjohanse-emr
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7 bytes=363 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/datastore-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7`
- bytes: 363

````markdown
### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/check_docs.yml sha256=f2101f32574a02c4516d1a1f454980b547137fb45fc5d9c0a435a51c1c709027 bytes=1444 -->
## FILE: .github/workflows/check_docs.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/check_docs.yml`
- sha256: `f2101f32574a02c4516d1a1f454980b547137fb45fc5d9c0a435a51c1c709027`
- bytes: 1444

````yaml
name: Check docs

on:
  workflow_call:
  workflow_dispatch:

jobs:
  check_docs:
    name: Check docs for ni.datastore
    runs-on: ubuntu-latest
    defaults:
      run:
        # Set the working-directory for all steps in this job.
        working-directory: .
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Check for lock changes
        run: poetry check --lock
      - name: Cache virtualenv (with docs)
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: .venv
          key: ni.datastore-with-docs-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('./poetry.lock') }}
      - name: Install nitypes (with docs)
        run: poetry install -v --only main,docs
      - name: Generate docs
        run:  poetry run sphinx-build docs docs/_build -b html -W
      - name: Upload docs artifact
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: ni.datastore-docs
          path: ./docs/_build/
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/check_examples.yml sha256=b66895cb7c7ad1aa66a7bdc08c9d4cbd824b68c7716596dd1ef42f2d291511cc bytes=1087 -->
## FILE: .github/workflows/check_examples.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/check_examples.yml`
- sha256: `b66895cb7c7ad1aa66a7bdc08c9d4cbd824b68c7716596dd1ef42f2d291511cc`
- bytes: 1087

````yaml
name: Check examples

on:
  workflow_call:
  workflow_dispatch:

jobs:
  check_examples:
    name: Analyze example projects
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: [3.14]
        example-name: ['overview', 'system']
    runs-on: ${{ matrix.os }}
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Analyze Python Project
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: ${{ github.workspace }}/examples/${{ matrix.example-name }}
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/check_ni_datastore.yml sha256=e6794b7655b20b8b991bcc40d71b2615baee9637615fdf5b4206386d6239e2d8 bytes=1023 -->
## FILE: .github/workflows/check_ni_datastore.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/check_ni_datastore.yml`
- sha256: `e6794b7655b20b8b991bcc40d71b2615baee9637615fdf5b4206386d6239e2d8`
- bytes: 1023

````yaml
name: Check analyzers

on:
  workflow_call:
  workflow_dispatch:

jobs:
  check_analyzers:
    name: Check analyzers for ni.datastore
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: ['3.10', 3.14]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Analyze Python Project
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Bandit security checks
        run:  poetry run bandit -c pyproject.toml -r src/
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/check_utilities.yml sha256=13e0dd7b7eddc89dd80020f89288d9c4ad02c1ea96c24d3c6291029ef8e8475b bytes=1010 -->
## FILE: .github/workflows/check_utilities.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/check_utilities.yml`
- sha256: `13e0dd7b7eddc89dd80020f89288d9c4ad02c1ea96c24d3c6291029ef8e8475b`
- bytes: 1010

````yaml
name: Check utilities

on:
  workflow_call:
  workflow_dispatch:

jobs:
  check_utilities:
    name: Analyze utilities
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: [3.14]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Analyze Python Project
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: ${{ github.workspace }}/utilities
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/CI.yml sha256=97e872a8e0a76bde4c3408e5368d021452cd1c4c80685ffdbb3178181597d97c bytes=1234 -->
## FILE: .github/workflows/CI.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/CI.yml`
- sha256: `97e872a8e0a76bde4c3408e5368d021452cd1c4c80685ffdbb3178181597d97c`
- bytes: 1234

````yaml
name: CI

on:
  push:
    branches:
      - main
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

jobs:
  check_analyzers:
      name: Check analyzers for ni.datastore
      uses: ./.github/workflows/check_ni_datastore.yml
  check_examples:
      name: Check analyzers for examples
      uses: ./.github/workflows/check_examples.yml
  check_utilities:
      name: Check analyzers for utilities
      uses: ./.github/workflows/check_utilities.yml
  check_docs:
    name: Check docs for ni.datastore
    uses: ./.github/workflows/check_docs.yml
  checks_succeeded:
      name: Checks succeeded
      needs: [check_analyzers, check_examples, check_utilities, check_docs]
      runs-on: ubuntu-latest
      steps:
        - run: exit 0
  run_unit_tests:
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        python-version: ['3.10', 3.11, 3.12, 3.13, 3.14]
    name: Run unit tests
    uses: ./.github/workflows/run_unit_tests.yml
    with:
      python-version: ${{ matrix.python-version }}
      os: ${{ matrix.os }}
  tests_succeeded:
    name: Unit tests succeeded
    needs: [run_unit_tests]
    runs-on: ubuntu-latest
    steps:
      - run: exit 0
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/PR.yml sha256=2080f64c96f44ee94750ccd599df4705b205a9d96a141b56440f4237350c704d bytes=420 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/PR.yml`
- sha256: `2080f64c96f44ee94750ccd599df4705b205a9d96a141b56440f4237350c704d`
- bytes: 420

````yaml
name: PR

on:
  pull_request:
    branches:
      - main
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  run_ci:
    name: Run CI
    uses: ./.github/workflows/CI.yml
    permissions:
      contents: read
      checks: write
      pull-requests: write
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/publish.yml sha256=b5a28deecfadee538f4e6e8bc8402b14a0187ae07c22b00e249e81bc2293e2ce bytes=3632 -->
## FILE: .github/workflows/publish.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/publish.yml`
- sha256: `b5a28deecfadee538f4e6e8bc8402b14a0187ae07c22b00e249e81bc2293e2ce`
- bytes: 3632

````yaml
name: Publish ni.datastore

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      environment:
        description: The environment to publish to.
        default: 'none'
        required: true
        type: choice
        options:
          - none
          - pypi
          - testpypi

env:
  dist-artifact-name: ni.datastore-distribution-packages
  environment: ${{ github.event_name == 'release' && 'pypi' || inputs.environment }}
  environment-info: |
    {
      "pypi": {
        "base-url": "https://pypi.org",
        "upload-url": "https://upload.pypi.org/legacy/"
      },
      "testpypi": {
        "base-url": "https://test.pypi.org",
        "upload-url": "https://test.pypi.org/legacy/"
      }
    }

jobs:
  check_ni_datastore:
    name: Check ni.datastore
    uses: ./.github/workflows/check_ni_datastore.yml
  check_docs:
    name: Check docs
    uses: ./.github/workflows/check_docs.yml
  build_ni_datastore:
    name: Build ni.datastore
    runs-on: ubuntu-latest
    needs: [check_ni_datastore, check_docs]
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Check project version
        if: github.event_name == 'release'
        uses: ni/python-actions/check-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Build distribution packages
        run: poetry build
      - name: Upload build artifacts
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: ${{ env.dist-artifact-name }}
          path: dist/*
  publish_to_pypi:
    name: Publish ni.datastore to PyPI
    if: github.event_name == 'release' || inputs.environment != 'none'
    runs-on: ubuntu-latest
    needs: [build_ni_datastore]
    environment:
      # This logic is duplicated because `name` doesn't support the `env` context.
      name: ${{ github.event_name == 'release' && 'pypi' || inputs.environment }}
      url: ${{ fromJson(env.environment-info)[env.environment].base-url }}/p/ni.datastore
    permissions:
      id-token: write
    steps:
    - name: Download build artifacts
      uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
      with:
        name: ${{ env.dist-artifact-name }}
        path: dist/
    - run: ls -lR
    - name: Upload to ${{ env.environment }}
      uses: pypa/gh-action-pypi-publish@cef221092ed1bacb1cc03d23a2d87d1d172e277b # v1.14.0
      with:
        repository-url: ${{ fromJson(env.environment-info)[env.environment].upload-url }}
  update_version:
    name: Update ni.datastore version
    runs-on: ubuntu-latest
    needs: [build_ni_datastore]
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Update project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/run_unit_tests.yml sha256=e04c719e5b27d6c2a6db62d593d0fe8288711580a70ec9f515895c473688728b bytes=1251 -->
## FILE: .github/workflows/run_unit_tests.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/run_unit_tests.yml`
- sha256: `e04c719e5b27d6c2a6db62d593d0fe8288711580a70ec9f515895c473688728b`
- bytes: 1251

````yaml
name: Run unit tests

on:
  workflow_call:
    inputs:
      python-version:
        description: 'The version of Python to use'
        default: ''
        required: true
        type: string
      os:
        description: 'The name of the OS to use'
        required: true
        type: string

jobs:
  run_unit_tests:
    name: Run unit tests for ni.datastore with ${{ inputs.python-version }} on ${{ inputs.os }}
    runs-on: ${{ inputs.os }}
    strategy:
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ inputs.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Run and upload unit tests for ni.datastore
        uses: ./.github/actions/run_and_upload_unit_tests
````

<!--NI_OSS_SOURCE repo=datastore-python path=.github/workflows/sync_github_issues_to_azdo.yml sha256=78c19f0ab979aec358bdaaee0b133cc0476fef7d165f621471db3ccdf56889cd bytes=1711 -->
## FILE: .github/workflows/sync_github_issues_to_azdo.yml

- repository: `ni/datastore-python`
- source_path: `.github/workflows/sync_github_issues_to_azdo.yml`
- sha256: `78c19f0ab979aec358bdaaee0b133cc0476fef7d165f621471db3ccdf56889cd`
- bytes: 1711

````yaml
name: Sync issue to Azure DevOps work item

on:
  issues:
    # Omit "labeled" and "unlabeled" to work around https://github.com/danhellem/github-actions-issue-to-work-item/issues/70
    types:
      [opened, edited, deleted, closed, reopened, assigned]
  issue_comment:
    types: [created, edited, deleted]

jobs:
  alert:
    if: ${{ !github.event.issue.pull_request && github.event.issue.title != 'Dependency Dashboard' }}
    runs-on: ubuntu-latest
    steps:
      - name: Choose work item type
        id: choose_work_item_type
        run: |
          if [ "${{ contains(github.event.issue.labels.*.name, 'enhancement') || contains(github.event.issue.labels.*.name, 'user story') }}" == "true" ]; then
            echo "work_item_type=User Story" >> $GITHUB_OUTPUT
          elif [ "${{ contains(github.event.issue.labels.*.name, 'tech debt') }}" == "true" ]; then
            echo "work_item_type=Technical Debt" >> $GITHUB_OUTPUT
          else
            echo "work_item_type=Bug" >> $GITHUB_OUTPUT
          fi
      - uses: danhellem/github-actions-issue-to-work-item@45eb3b46e684f2acd2954f02ef70350c835ee4bb # v2.4
        env:
          ado_token: "${{ secrets.AZDO_WORK_ITEM_TOKEN }}"
          github_token: "${{ secrets.GH_REPO_TOKEN }}"
          ado_organization: "ni"
          ado_project: "DevCentral"
          ado_area_path: "DevCentral\\Product RnD\\Platform HW and SW\\SW New Invest and Tech\\Nigel\\MDI"
          ado_wit: "${{ steps.choose_work_item_type.outputs.work_item_type }}"
          ado_new_state: "New"
          ado_active_state: "Active"
          ado_close_state: "Closed"
          ado_bypassrules: true
          log_level: 100
````

<!--NI_OSS_SOURCE repo=datastore-python path=.gitignore sha256=e7cbe1a344327704160e5de3489756dc02a2205d47d5ad9802d2202b68651ba1 bytes=342 -->
## FILE: .gitignore

- repository: `ni/datastore-python`
- source_path: `.gitignore`
- sha256: `e7cbe1a344327704160e5de3489756dc02a2205d47d5ad9802d2202b68651ba1`
- bytes: 342

````text
#VS Code 
.vscode/

# Byte-compiled / optimized / DLL files
__pycache__/

# Directory for data generated from running examples and tests
temp_data/

# Unit tests
.pytest_cache/
test_results/

# Coverage output
.coverage
htmlcov/

# Environments
.venv*/

# Built artifacts
dist/
**/docs/**/_build/

# mypy
.mypy_cache/
````

<!--NI_OSS_SOURCE repo=datastore-python path=.readthedocs.yaml sha256=f6971336b39a2bce91374c5b3900a8425ae19e1e6f4928785b404ed92d342b54 bytes=316 -->
## FILE: .readthedocs.yaml

- repository: `ni/datastore-python`
- source_path: `.readthedocs.yaml`
- sha256: `f6971336b39a2bce91374c5b3900a8425ae19e1e6f4928785b404ed92d342b54`
- bytes: 316

````yaml
# .readthedocs.yml

version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.11"
  jobs:
    post_create_environment:
      - pip install poetry==2.1.4
    post_install:
      - VIRTUAL_ENV=$READTHEDOCS_VIRTUALENV_PATH poetry -C . install --only main,docs

sphinx:
  configuration: ./docs/conf.py
````

<!--NI_OSS_SOURCE repo=datastore-python path=CONTRIBUTING.md sha256=d6795560ff621e94d39a4fe8c917768399d6cfeb982d4d9939fe0a6d61a14e02 bytes=7165 -->
## FILE: CONTRIBUTING.md

- repository: `ni/datastore-python`
- source_path: `CONTRIBUTING.md`
- sha256: `d6795560ff621e94d39a4fe8c917768399d6cfeb982d4d9939fe0a6d61a14e02`
- bytes: 7165

````markdown
# Contributing to `datastore-python`

Contributions to `datastore-python` are welcome from all!

`datastore-python` is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/datastore-python/).

`datastore-python` follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

Please remember to sign off your commits (e.g., by using `git commit -s` if you
are using the command line client). This amends your git commit message with a line
of the form `Signed-off-by: Name Lastname <name.lastmail@emailaddress.com>`. Please
include all authors of any given commit into the commit message with a
`Signed-off-by` line. This indicates that you have read and signed the Developer
Certificate of Origin (see below) and are able to legally submit your code to
this repository.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

## Prerequisites

- _(Optional)_ Install [Visual Studio Code](https://code.visualstudio.com/download)
- Install [Git](https://git-scm.com)
- Install [Python](https://www.python.org/downloads/), any version from the [README](README.md)
- Install [Poetry](https://python-poetry.org/docs/#installation), version >= 2.1.4

## Install the package and its dependencies

Run `poetry install` ([usage](https://python-poetry.org/docs/cli/#install)). This creates an
in-project virtual environment (`.venv`) and installs this package's dependencies and dev-dependencies,
as specified in the `pyproject.toml` and `poetry.lock` files.

```powershell
# Include dependencies for linting, analyzing, and testing the package
poetry install

# Include dependencies for building the documentation (requires Python 3.11 or newer)
poetry install --with docs
```

## Activate the virtual environment (if needed)

- _(Recommended)_ Activate for each command by prefixing the call with `poetry run {command}`
- Activate for the lifetime of the shell in the terminal with `poetry shell`
- Activate in VS Code ([link](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment))

# Simple Development Loop

```powershell
# Update from main
git checkout main
git pull

# Create a new branch
git switch --create users/{username}/{branch-purpose}

# Install the package dependencies
poetry install --with docs

# ✍ Make source changes

# Run the analyzers -- see files in .github/workflows for details
poetry run nps lint
poetry run mypy
poetry run pyright

# Apply safe fixes
poetry run nps fix

# Run the standalone unit tests
poetry run pytest -v tests\unit

# Run the acceptance tests against an active DataStore service
poetry run pytest -v tests\acceptance

# Build and inspect the documentation
poetry run sphinx-build docs docs/_build --builder html --fail-on-warning
start docs/_build/index.html
```

# Testing

There are pytests in `ni.datastore` that you can run with poetry. There are two directories of tests:
`acceptance` and `unit`.

## Unit Tests

The unit tests in the `unit` folder are the first line of defense to catch regressions. These tests
will run on any PR that is submitted for `ni.datastore`. You can run these tests manually by running:
`poetry run pytest tests\unit`

## Acceptance Tests

Acceptance tests are system level tests that are meant to run against an actual DataStore service.
You can start the DataStore service by building the service from its repo and running it. You
can also install the Measurement Data Services installer on a test machine. If the DataStore service
is not running, these tests will fail. To run the acceptance tests, run this command:
`poetry run pytest tests\acceptance`

> Warning! Running the acceptance tests will publish data and metadata to the default global
> MDS data store location in the Documents folder.

# Publishing on PyPI

You can publish the `ni.datastore` package by creating a GitHub release
in the `datastore-python` repo. Here are the steps to follow to publish the package:

1. From the main GitHub repo page, select "Create a new release".
2. On the "New Release" page, create a new tag using the "Select Tag" drop down. The tag must be the package version, matching the
value found in pyproject.toml. Example: `0.1.0.dev0`.
3. Enter a title in the "Release title" field. The title should contain the package name and
version in the format `ni.datastore <package-version>`. For example: `ni.datastore 0.1.0.dev0`.
4. Click "Generate release notes" and edit the release notes.
  - Delete entries for PRs that do not affect users, such as "chore(deps):" and "fix(deps):" PRs.
  - Consider grouping related entries.
  - Reformat entries to be more readable. For example, change "Blah blah by so-and-so in \#123" to "Blah blah (\#123)".
5. If this is a pre-release release, check the "Set as a pre-release" checkbox.
6. Click "Publish release".
7. Creating a release will start the publish workflow. You can track the
progress of this workflow in the "Actions" page of the GitHub repo.
8. The workflow job that publishes a package to pypi requires code owner approval. This job will automatically send code owners a notification email, then it will wait for them to log in and approve the deployment.
9. After receiving code owner approval, the publish workflow will resume.
10. Once the publish workflow has finished, you should see your release on pypi.

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

See [LICENSE](https://github.com/ni/datastore-python/blob/main/LICENSE)
for details about how `datastore-python` is licensed.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/conf.py sha256=461cd76d5bc9b3b49a52fb67ec1444a8dd63b000f1e6fa362bb8deb4a97a332d bytes=2998 -->
## FILE: docs/conf.py

- repository: `ni/datastore-python`
- source_path: `docs/conf.py`
- sha256: `461cd76d5bc9b3b49a52fb67ec1444a8dd63b000f1e6fa362bb8deb4a97a332d`
- bytes: 2998

````python
"""Sphinx Configuration File."""

import datetime
import pathlib

import autoapi.extension
import toml

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

root_path = pathlib.Path(__file__).parent.parent
pyproj_file = root_path / "pyproject.toml"
proj_config = toml.loads(pyproj_file.read_text())


project = proj_config["project"]["name"]
company = "National Instruments"
copyright = f"2025-{datetime.datetime.now().year}, {company}"
if datetime.datetime.now().year == 2025:
    copyright = f"{datetime.datetime.now().year}, {company}"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
version = proj_config["project"]["version"]
release = ".".join(version.split(".")[:2])
description = proj_config["project"]["description"]


htmlhelp_basename = f"{project}doc"


# tell autoapi to doc the public options
autoapi_options = list(autoapi.extension._DEFAULT_OPTIONS)
autoapi_options.remove("private-members")  # note: remove this to include "_" members in docs
autoapi_dirs = [root_path / "src" / "ni"]
autoapi_python_use_implicit_namespaces = True
autoapi_template_dir = "templates/autoapi"
autoapi_python_class_content = "both"
autoapi_type = "python"
autodoc_typehints = "description"
autoapi_file_patterns = ["*.pyi", "*.py"]

# Optional: suppress warnings globally
suppress_warnings = [
    "autoapi.python_import_resolution"
]


def process_docstring(app, what, name, obj, options, lines):
    """Make edits to docstrings as necessary"""
    if r"@generated by mypy-protobuf" in lines[0]:
        lines.clear()


def setup(sphinx):
    """Sphinx setup callback."""
    sphinx.connect("autodoc-process-docstring", process_docstring)


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "grpc": ("https://grpc.github.io/grpc/python/", None),
}


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": -1,
}

templates_path = ["templates"]

# Napoleon settings
napoleon_numpy_docstring = False
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/examples/index.rst sha256=e8e02b5e249297432a8fff30bc7f245d8b7733b03e0200dc4b7fdac3b6f7e932 bytes=2787 -->
## FILE: docs/examples/index.rst

- repository: `ni/datastore-python`
- source_path: `docs/examples/index.rst`
- sha256: `e8e02b5e249297432a8fff30bc7f245d8b7733b03e0200dc4b7fdac3b6f7e932`
- bytes: 2787

````rst
########
Examples
########

This section contains Jupyter notebook and Python script examples demonstrating how to use the NI Data Store.

All example notebooks are located in the ``examples/notebooks/`` directory of the repository.

Each example script has its own project folder under ``examples/``.

OData Query Example Notebooks
=============================

These notebooks demonstrate how to query data and metadata using OData syntax:

**Setup and Sample Data:**

* `publish_sample_data.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/query/publish_sample_data.ipynb>`_ - Creates comprehensive sample data for query examples

**Query Examples:**

* `query_metadata.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/query/query_metadata.ipynb>`_ - Demonstrates metadata queries (operators, hardware, UUTs, etc.)
* `query_measurements.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/query/query_measurements.ipynb>`_ - Demonstrates measurement and condition queries

Other Example Notebooks
=======================

Additional examples for various use cases:

* `publish_measurement.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/overview/publish_measurement.ipynb>`_ - Basic measurement publishing
* `alias.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/alias/alias.ipynb>`_ - Working with aliases
* `extension_attributes.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/extension-attributes/extension_attributes.ipynb>`_ - Extension attributes examples
* `publish_waveforms.ipynb <https://github.com/ni/datastore-python/blob/main/examples/notebooks/voltage-regulator/publish_waveforms.ipynb>`_ - Publishing waveform data

Getting Started with Notebooks
==============================

1. **Run the setup notebook first:** Start with ``publish_sample_data.ipynb`` to create sample data
2. **Explore queries:** Try the OData query examples to learn filtering and data retrieval
3. **Adapt for your use case:** Use the other examples as templates for your specific needs

All notebooks include detailed explanations and can be run in any Jupyter environment with the ``ni.datastore`` package installed.

Python Example Scripts
======================

These Python scripts demonstrate how to publish and query both data and metadata.

* `overview.py <https://github.com/ni/datastore-python/blob/main/examples/overview>`_ - Publishing and querying measurement data
* `system.py <https://github.com/ni/datastore-python/blob/main/examples/system>`_ - Publishing and querying system metadata

Each has a ``README.md`` file that describes its runtime requirements and usage.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/index.rst sha256=23e3756640a2ac4c6bcae0d372c5cba324e2cf383930e98a2819ffaaee20f750 bytes=391 -->
## FILE: docs/index.rst

- repository: `ni/datastore-python`
- source_path: `docs/index.rst`
- sha256: `23e3756640a2ac4c6bcae0d372c5cba324e2cf383930e98a2819ffaaee20f750`
- bytes: 391

````rst
#################################
Measurement Data Store Python API
#################################

.. include:: intro.inc

Table of Contents
=================

.. toctree::
   :maxdepth: 4

   reference/index
   examples/index
   autoapi/index
   autoapi/ni/datastore/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/intro.inc sha256=c635486fa1aefa3a434896096680a58ab0cf3e465cf382bdbbd37ba3aa873d15 bytes=813 -->
## FILE: docs/intro.inc

- repository: `ni/datastore-python`
- source_path: `docs/intro.inc`
- sha256: `c635486fa1aefa3a434896096680a58ab0cf3e465cf382bdbbd37ba3aa873d15`
- bytes: 813

````text
Introduction
============

About
-----

The ``ni.datastore`` Python package provides APIs for publishing and retrieving data from the NI Measurement Data Store

NI created and supports this package.

Operating System Support
------------------------

``ni.datastore`` supports Windows and Linux operating systems.

Python Version Support
----------------------

``ni.datastore`` supports CPython 3.10+.

Installation
------------

As a prerequisite to using the ``ni.datastore`` module, you must install Measurement Data Services
Software 2026 Q3 or later on your system. You can download and install this software using
NI Package Manager.

You can directly install the ``ni.datastore`` package using ``pip`` or by listing it as a dependency in
your project's ``pyproject.toml`` file.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/reference/index.rst sha256=11753f17650f6e7c6fcee2803b760cca370c071d63d120cc80a8d347b0f5daca bytes=260 -->
## FILE: docs/reference/index.rst

- repository: `ni/datastore-python`
- source_path: `docs/reference/index.rst`
- sha256: `11753f17650f6e7c6fcee2803b760cca370c071d63d120cc80a8d347b0f5daca`
- bytes: 260

````rst
##################
Reference Guide
##################

This section provides comprehensive documentation for the NI Data Store system components.

.. toctree::
   :maxdepth: 3

   ni-data-store
   ni-metadata-store
   using-measurement-data-services
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/reference/ni-data-store.md sha256=b3111ca30ac3adb48653ab26d2c42f16ebf273a1ab19432ae9341f862bad4d2c bytes=8761 -->
## FILE: docs/reference/ni-data-store.md

- repository: `ni/datastore-python`
- source_path: `docs/reference/ni-data-store.md`
- sha256: `b3111ca30ac3adb48653ab26d2c42f16ebf273a1ab19432ae9341f862bad4d2c`
- bytes: 8761

````markdown
# NI Data Store

The NI Data Store provides a structured way to store and organize test data. It consists of several core entities that work together to capture the complete picture of test execution, from high-level test sessions down to individual measurements and environmental conditions.

## **Core Entities**

### **TestResult** 
A **TestResult** represents a complete test session or test execution run for a specific Unit Under Test (UUT). It's the top-level container that captures everything that happened when you tested a particular device.

**Fields:**
- `id` (string) - Unique identifier (GUID)
- `uut_instance_id` (string) - ID of the Unit Under Test instance
- `operator_id` (string) - ID of the operator who ran the test
- `test_station_id` (string) - ID of the test station used
- `test_description_id` (string) - ID of the test description/specification
- `software_item_ids` (list of strings) - IDs of software used during testing
- `hardware_item_ids` (list of strings) - IDs of hardware used during testing  
- `test_adapter_ids` (list of strings) - IDs of test adapters used
- `name` (string) - Human-readable name for the test run
- `start_date_time` (timestamp) - When the test execution started
- `end_date_time` (timestamp) - When the test execution finished
- `outcome` (enum) - Overall test result (PASSED, FAILED, INDETERMINATE, UNSPECIFIED)
- `link` (string) - Optional link to additional resources
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation
- `error_information` (ErrorInformation) - Error details if test result failed

**Real-world example**: When you put a circuit board on a test station and run a complete validation sequence, that entire session becomes one TestResult. It includes metadata like who ran the test, when it was run, what test station was used, and links to all the measurements and steps that were performed.

### **Step**
A **Step** represents an individual test procedure or operation within a larger test sequence. Each step typically tests a specific aspect or function of the UUT and serves as a container for related measurements and conditions.

**Fields:**
- `id` (string) - Unique identifier (GUID) 
- `parent_step_id` (string) - ID of parent step (for hierarchical steps)
- `test_result_id` (string) - ID of the associated TestResult
- `test_id` (string) - ID of the test definition/specification
- `name` (string) - Human-readable name for the step
- `step_type` (string) - Type/category of the step
- `notes` (string) - Additional notes about the step
- `start_date_time` (timestamp) - When the step started executing
- `end_date_time` (timestamp) - When the step finished executing
- `outcome` (enum) - Result of this step (PASSED, FAILED, INDETERMINATE, UNSPECIFIED)
- `link` (string) - Optional link to additional resources
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation
- `error_information` (ErrorInformation) - Error details if step failed

**Real-world examples**:
- "Measure DC Voltage on Pin 5" 
- "Verify Communication Protocol Response"
- "Check LED Brightness at 100mA"
- "Functional Test - Power On Sequence"
- "Calibration - Set Reference Voltage"

Each step belongs to a TestResult and can contain multiple measurements and conditions.

### **PublishedMeasurement**
A **PublishedMeasurement** represents actual measurement data captured during a test step. This is the core data entity that stores the measured values, whether they are simple scalars, complex waveforms, or other data types.

**Fields:**
- `published_conditions` (list) - Environmental conditions present during measurement
- `id` (string) - Unique identifier for this measurement
- `test_result_id` (string) - ID of the associated TestResult
- `step_id` (string) - ID of the associated Step
- `software_item_ids` (list of strings) - Software used to capture this measurement
- `hardware_item_ids` (list of strings) - Hardware used to capture this measurement
- `test_adapter_ids` (list of strings) - Test adapters used to capture this measurement
- `name` (string) - Name used to group related measurements
- `value_type` (string) - Type of data (e.g., "Scalar", "AnalogWaveform", "Spectrum")
- `notes` (string) - Additional notes about the measurement
- `start_date_time` (timestamp) - When measurement capture started
- `end_date_time` (timestamp) - When measurement capture finished
- `outcome` (enum) - Result of this measurement (PASSED, FAILED, INDETERMINATE, UNSPECIFIED)
- `parametric_index` (int) - Index within parametric set, or -1 for entire set
- `error_information` (ErrorInformation) - Error details if measurement failed

**Supported Data Types:**
- **Scalar** - Single float, int, str or boolean values
- **Vector** - Arrays of float, int, str or boolean values
- **DoubleAnalogWaveform** - Analog waveform with double precision
- **DoubleXYData** - XY coordinate data with double precision
- **I16AnalogWaveform** - Analog waveform with 16-bit integer precision
- **DoubleComplexWaveform** - Complex waveform with double precision
- **I16ComplexWaveform** - Complex waveform with 16-bit integer precision
- **DoubleSpectrum** - Frequency spectrum data with double precision
- **DigitalWaveform** - Digital waveform data

**Real-world examples**:
- A voltage reading: `3.297V` from a multimeter
- A waveform: Time-series data from an oscilloscope showing a signal over time
- A frequency measurement: `1.0234 MHz` from a frequency counter  
- A boolean result: `PASS/FAIL` from a functional test
- An array of values: Temperature readings over time from a thermal sensor

### **PublishedCondition**
A **PublishedCondition** represents environmental or contextual information that was present during test execution. Conditions capture the state of the test environment, input parameters, or other contextual data that might affect measurement results.

**Fields:**
- `id` (string) - Unique identifier for this condition
- `name` (string) - Name of the condition (e.g., "Temperature", "Supply Voltage")
- `condition_type` (string) - Type/category of the condition (e.g., "Environment", "Input Parameter")
- `step_id` (string) - ID of the associated Step
- `test_result_id` (string) - ID of the associated TestResult

**Real-world examples**:
- Environmental conditions: Temperature = 23.5°C, Humidity = 45%
- Input parameters: Supply Voltage = 5.0V, Input Frequency = 1kHz  
- Test configuration: Gain Setting = "High", Filter = "Low Pass"
- Calibration data: Reference Standard = "NIST-123", Cal Date = "2024-01-15"

### **Supporting Types**

#### **Outcome Enum**
Represents the result of a test or measurement:
- `UNSPECIFIED` - The outcome is not specified or unknown
- `PASSED` - The measurement or test passed successfully
- `FAILED` - The measurement or test failed
- `INDETERMINATE` - The measurement or test result is indeterminate or inconclusive

#### **ErrorInformation**
Contains error details when operations fail:
- `error_code` (int) - Numeric error code
- `message` (string) - Human-readable error message
- `source` (string) - Source/origin of the error

## **The Hierarchy**
```
TestResult (Test session for Serial# ABC123)
├── Step 1: "Power Supply Verification"
│   ├── PublishedMeasurement: "5V Rail Voltage" = 5.02V
│   ├── PublishedMeasurement: "Current Draw" = 245mA
│   └── PublishedCondition: "Temperature" = 23.5°C
├── Step 2: "Digital I/O Test"  
│   ├── PublishedMeasurement: "Pin 1 High Level" = 3.28V
│   └── PublishedMeasurement: "Pin 2 Response Time" = 150μs
└── Step 3: "Communication Test"
    └── PublishedMeasurement: "UART Data Rate" = 115200 bps
```

This hierarchical structure allows you to:
- **Organize data logically** - Group related measurements by test step
- **Drill down progressively** - From test results → steps → individual measurements
- **Track context** - Associate environmental conditions with specific measurements
- **Enable powerful queries** - Search and filter data at any level of the hierarchy
- **Maintain traceability** - Link every measurement back to its test context

## **Data Access Patterns**

The NI Data Store supports two primary data access patterns:

1. **Publishing Data** - Store test results, steps, measurements, and conditions during test execution
2. **Querying Data** - Retrieve and analyze test data using OData query syntax

All entities support OData queries for flexible data retrieval and analysis.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/reference/ni-metadata-store.md sha256=e87728ea932b7428058a3f960b56b79927bf919c143baf1fc8351b713ce09562 bytes=19719 -->
## FILE: docs/reference/ni-metadata-store.md

- repository: `ni/datastore-python`
- source_path: `docs/reference/ni-metadata-store.md`
- sha256: `e87728ea932b7428058a3f960b56b79927bf919c143baf1fc8351b713ce09562`
- bytes: 19719

````markdown
# NI Metadata Store

The NI Metadata Store supports the digital thread weaving together measurement results with metadata that describes **who**, **what**, **where**, and **how** tests are performed. This creates a complete context around your test data, enabling traceability and analysis across your entire test ecosystem.

**Based on:** [`metadata_store.proto`](https://github.com/ni/ni-apis/blob/main/ni/measurements/metadata/v1/metadata_store.proto)

## **Core Entities**

### **Operator**
An **Operator** represents a person who performs tests or operates test equipment. This captures the human element in your test process.

**Fields:**
- `id` (string) - The id of the operator
- `name` (string) - The name of the operator
- `role` (string) - The role of the operator (e.g., "Test Engineer", "Lab Technician")
- `link` (string) - URI to resource describing the operator
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- "Sarah Johnson" - Test Engineer who runs daily production tests
- "Mike Chen" - Senior Technician who performs calibrations  
- "Alex Smith" - Lab Assistant who conducts R&D validation tests

Each operator has a role (e.g., "Test Engineer", "Lab Technician", "Quality Inspector") that helps categorize their responsibilities and skill level.

## **Test Station**
A **Test Station** represents a physical location or setup where testing is performed. This could be a bench, rack, or dedicated test system.

**Fields:**
- `id` (string) - The id of the test station
- `name` (string) - The name of the test station
- `asset_identifier` (string) - For tracking and inventory purposes
- `link` (string) - URI to resource describing the test station
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- "Station_A1" - Production line station #1 for power supply testing
- "Bench_RF_Lab" - RF laboratory bench with spectrum analyzers
- "Burn_In_Rack_3" - Environmental stress testing chamber
- "Cal_Lab_Station" - Precision calibration workstation with reference standards

Test stations help track where tests were performed, enabling analysis of station-specific issues or performance variations.

## **UUT (Unit Under Test)**
A **UUT** represents a product definition or model being tested. This is the "what" - the type of device or product under test.

**Fields:**
- `id` (string) - The id of the UUT
- `model_name` (string) - The name of the UUT model
- `family` (string) - The UUT family or category
- `manufacturers` (list of strings) - List of manufacturers of the UUT
- `part_number` (string) - The part number of the UUT
- `link` (string) - URI to resource describing the UUT
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- Model: "PowerSupply v2.1", Family: "Power" - A specific power supply product
- Model: "Audio Amplifier v1.3", Family: "Audio" - An audio amplifier design
- Model: "RF Transceiver Gen3", Family: "Communications" - A radio frequency module
- Model: "Motor Controller v4.0", Family: "Industrial" - An industrial motor controller

UUTs represent the product designs, while UUT instances represent individual physical devices.

## **UUT Instance**
A **UUT Instance** represents an individual physical device with a unique serial number. This is a specific unit of the UUT model being tested.

**Fields:**
- `id` (string) - The id of the UUT instance
- `uut_id` (string) - The ID of the UUT associated with this instance (GUID or alias)
- `serial_number` (string) - The serial number of the UUT instance
- `manufacture_date` (string) - When the instance was manufactured
- `firmware_version` (string) - Version of the firmware on the UUT instance
- `hardware_version` (string) - Hardware version of the UUT instance
- `link` (string) - URI to resource describing the UUT instance
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- UUT: "PowerSupply v2.1", Serial: "PS-2024-001", FW: "1.2.3", HW: "Rev C" - First power supply unit built in 2024
- UUT: "Audio Amplifier v1.3", Serial: "AMP-2024-456", FW: "2.0.1", HW: "Rev B" - Specific amplifier with serial number
- UUT: "RF Transceiver Gen3", Serial: "RF-X7G9-2024-789", FW: "3.1.0", HW: "Rev A" - Individual transceiver unit

Each UUT instance tracks the test history for that specific physical device throughout its lifecycle.

## **Hardware Item**
A **Hardware Item** represents test equipment, instruments, or tools used during testing. This captures what physical equipment was involved in generating the measurements.

**Fields:**
- `id` (string) - The id of the hardware item
- `manufacturer` (string) - The vendor of the hardware item
- `model` (string) - The name/model number of the hardware item
- `serial_number` (string) - Unique serial number for tracking
- `part_number` (string) - Manufacturer's part number
- `asset_identifier` (string) - For tracking and inventory purposes
- `calibration_due_date` (string) - When calibration expires
- `link` (string) - URI to resource describing the hardware item
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- Manufacturer: "NI", Model: "PXIe-4081", Serial: "DMM001" - Digital multimeter
- Manufacturer: "Keysight", Model: "E5071C", Serial: "VNA789" - Vector network analyzer  
- Manufacturer: "Tektronix", Model: "MSO64", Serial: "SCOPE456" - Mixed-signal oscilloscope
- Manufacturer: "Fluke", Model: "8588A", Serial: "REF123" - Reference multimeter

Hardware items include calibration information and help ensure measurement traceability.

## **Software Item**
A **Software Item** represents software tools, environments, or versions used during testing. This captures the software context that could affect test results.

**Fields:**
- `id` (string) - The id of the software item
- `product` (string) - The software product name (letters, numbers, spaces, hyphens, underscores, parentheses, periods; must begin and end with letter or number)
- `version` (string) - The version of the software item
- `link` (string) - URI to resource describing the software item
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- Product: "Python", Version: "3.11.5" - Programming language version
- Product: "NI-DAQmx", Version: "23.3.0" - Data acquisition driver
- Product: "TestStand", Version: "2023 Q3" - Test executive software
- Product: "LabVIEW", Version: "2023 Q3" - Measurement software environment
- Product: "Custom Test App", Version: "v2.1.4" - Company-specific test application

Software items help identify if software changes affected test results or reproducibility.

## **Test Description**
A **Test Description** represents a defined test procedure or specification for testing a particular UUT. This defines what tests should be performed.

**Fields:**
- `id` (string) - The id of the test description
- `uut_id` (string) - The ID of the UUT this test is designed for
- `name` (string) - Name of the test description
- `link` (string) - URI to resource describing the test description
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- "Power Supply Validation Suite" - Complete test suite for power supply products
- "RF Compliance Test Set" - FCC/CE compliance tests for RF devices
- "Functional Verification Protocol" - Basic functionality tests for motor controllers
- "Performance Characterization Tests" - Detailed performance measurements for amplifiers

## **Test**
A **Test** represents an individual test procedure or method. This is more granular than a test description and describes specific test steps.

**Fields:**
- `id` (string) - The id of the test
- `name` (string) - Name of the test
- `description` (string) - Explanation of what the test does
- `link` (string) - URI to resource describing the test
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- "DC Voltage Accuracy Check" - Measures voltage accuracy across specified range
- "Frequency Response Sweep" - Tests frequency response from 20Hz to 20kHz
- "Power-On Self Test" - Automated built-in test executed at startup
- "Load Regulation Test" - Verifies output stability under varying loads

## **Test Adapter**
A **Test Adapter** represents a test fixture, mechanical setup, or interface used to hold, connect, or interface the UUT with the test system.

**Fields:**
- `id` (string) - The id of the test adapter
- `name` (string) - Name or label for the adapter
- `manufacturer` (string) - Vendor of the adapter
- `model` (string) - Model number or name
- `serial_number` (string) - Unique serial number
- `part_number` (string) - Manufacturer's part number
- `asset_identifier` (string) - For tracking and inventory purposes
- `calibration_due_date` (string) - When calibration expires
- `link` (string) - URI to resource describing the test adapter
- `extension` (dict) - Custom key-value pairs for additional metadata
- `schema_id` (string) - ID of the schema for extension validation

**Real-world examples**:
- "PCB Test Fixture v2.1" - Custom fixture for holding circuit boards during test
- "RF Connector Adapter Kit" - Set of adapters for different RF connector types
- "Thermal Test Chamber Fixture" - Mechanical setup for environmental testing
- "High Current Test Jig" - Specialized fixture for high-power testing

## **Extension Schema**
An **Extension Schema** defines the structure and validation rules for custom extension fields that can be added to any metadata entity.

**Fields:**
- `id` (string) - Unique identifier for the schema
- `schema` (string) - The schema definition itself (JSON Schema format)

**Real-world examples**:
- Custom fields for tracking calibration certificates
- Additional properties for regulatory compliance data
- Company-specific asset management fields
- Industry-specific metadata requirements

## **Alias**
An **Alias** provides a human-readable name that points to any metadata entity. This creates a layer of abstraction that makes test code more maintainable and readable.

**Fields:**
- `name` (string) - The registered alias name for the metadata instance
- `target_type` (enum) - The type of the aliased metadata instance (see `AliasTargetType` enum)
- `target_id` (string) - The unique identifier for the aliased metadata instance

**Supported Target Types**:
- `UUT_INSTANCE` - Points to a UUT Instance
- `UUT` - Points to a UUT
- `HARDWARE_ITEM` - Points to a Hardware Item  
- `SOFTWARE_ITEM` - Points to a Software Item
- `OPERATOR` - Points to an Operator
- `TEST_DESCRIPTION` - Points to a Test Description
- `TEST` - Points to a Test
- `TEST_STATION` - Points to a Test Station
- `TEST_ADAPTER` - Points to a Test Adapter

**Real-world examples**:
- "Primary_DMM" → points to Hardware Item "NI PXIe-4081 S/N DMM001"
- "Lead_Test_Engineer" → points to Operator "Sarah Johnson"
- "Production_Station_1" → points to Test Station "TestStation_A1"  
- "Current_PowerSupply_Design" → points to UUT "PowerSupply v2.1"

Aliases allow you to change which specific equipment or person is referenced without changing test code.

## **The Metadata Store Hierarchy**
```
Complete Test Execution Context:
├── WHO: Operator "Alex Smith" (Test Engineer)
├── WHERE: Test Station "Station_A1" (Production Line)
├── WHAT: UUT Instance "PS-2024-001" (PowerSupply v2.1)
│   └── Based on UUT "PowerSupply v2.1" (Family: Power)
├── HOW: Test Setup
│   ├── Test Description "Power Supply Validation Suite"
│   ├── Individual Tests
│   │   ├── "DC Voltage Accuracy Check"
│   │   └── "Load Regulation Test"
│   ├── Hardware Items
│   │   ├── "NI PXIe-4081" (Digital Multimeter)
│   │   └── "NI PXIe-5171" (Oscilloscope)
│   └── Test Adapters
│       └── "PCB Test Fixture v2.1"
└── ENVIRONMENT: Software Items
    ├── "Python 3.11.5"
    ├── "NI-DAQmx 23.3.0"
    └── "Custom Test Suite v1.2"

Aliases for Easy Reference:
├── "Primary_Operator" → Alex Smith
├── "Main_Station" → Station_A1  
├── "Test_DMM" → NI PXIe-4081
├── "Current_UUT_Design" → PowerSupply v2.1
└── "Standard_Test_Suite" → Power Supply Validation Suite

Extension Schemas:
├── "Calibration_Certificate_Schema" → Custom calibration tracking
└── "Asset_Management_Schema" → Company inventory fields
```

## **Custom Schemas and Extensions**

Every metadata entity in the NI Metadata Store supports **extensions** - custom key-value pairs that allow you to add organization-specific, industry-specific, or regulatory-specific metadata beyond the standard fields.

### **How Extensions Work**

**Extensions** are a dictionary of custom fields that can be attached to any metadata entity:
```python
# Example: Hardware Item with custom extensions
hardware_item = HardwareItem(
    manufacturer="NI",
    model="PXIe-5171", 
    serial_number="SCOPE001",
    extension={
        "bandwidth": "1 GHz",
        "manufacture_date": "2024-03-15",
        "calibration_certificate": "CAL-2024-001234",
        "asset_tag": "ASSET-SCOPE-789"
    }
)
```

### **Schema Validation**

To ensure consistency and enforce requirements for extension fields, you can register a **schema** that defines:
- Which extension fields are **required** vs **optional**
- Data types and validation rules
- Field descriptions and constraints

**Schema Registration Process:**
1. **Define the schema** in JSON format (like the example below)
2. **Register the schema** with the metadata store
3. **Get a schema_id** returned from registration
4. **Reference the schema_id** when creating metadata entities

### **Schema Example**

Here's an example schema for oscilloscope hardware items:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/scope.schema.json",
  "title": "Oscilloscope Hardware Item Schema",
  "description": "Schema for oscilloscope hardware item extensions",
  "type": "object",
  "properties": {
    "hardware_item": {
      "type": "object",
      "properties": {
        "bandwidth": {
          "type": "string",
          "description": "Oscilloscope bandwidth specification"
        },
        "manufacture_date": {
          "type": "string",
          "format": "date",
          "description": "Date the hardware was manufactured"
        },
        "calibration_cert": {
          "type": "string",
          "pattern": "^CAL-\\d{4}-\\d{6}$",
          "description": "Calibration certificate number"
        },
        "asset_tag": {
          "type": "string",
          "description": "Company asset tag identifier"
        }
      },
      "required": ["bandwidth", "manufacture_date"]
    }
  }
}
```

**Schema Structure:**
- **Required fields** are listed in the `required` array - must be provided when creating the entity
- **Optional fields** are defined in `properties` but not listed in `required` - can be omitted
- **Descriptions** provide documentation for each field

### **Using Schemas in Practice**

```python
# 1. Register the schema
schema_content = metadata_store_client.register_schema_from_file("scope_schema.json")  # JSON format
schema_id = metadata_store_client.register_schema(schema_content)

# 2. Create hardware item with schema validation
hardware_item = HardwareItem(
    manufacturer="NI",
    model="PXIe-5171",
    serial_number="SCOPE001",
    schema_id=schema_id,  # Links to registered schema
    extension={
        "bandwidth": "1 GHz",        # Required by schema
        "manufacture_date": "2024-03-15",  # Required by schema
        "asset_tag": "SCOPE-789"     # Optional field
        # Missing calibration_cert is OK (not in required array)
    }
)

# 3. The schema validates extensions during creation
metadata_store_client.create_hardware_item(hardware_item)
```

### **Benefits of Schema Validation**

- **Consistency** - Ensures all entities of the same type have required fields
- **Data Quality** - Prevents missing critical information
- **Documentation** - Schema serves as documentation of expected fields
- **Evolution** - Schemas can be versioned and updated over time
- **Integration** - External systems know what fields to expect

### **Schema Inheritance**

When creating metadata entities within a test result context, schema inheritance applies:
- If the **test result** has a `schema_id`, child entities inherit that schema
- Child entities can override with their own `schema_id` if needed
- This allows consistent validation across entire test sessions

**Example:**
```python
# Test result with schema
test_result = TestResult(
    schema_id="company-standard-v1.2",  # All child entities inherit this
    uut_instance_id=uut_instance_id,
    # ...
)

# Hardware item inherits test result's schema automatically
hardware_item = HardwareItem(
    manufacturer="NI", 
    model="PXIe-4081",
    # schema_id automatically inherited from test_result
    extension={
        # Fields validated against inherited schema
    }
)
```



## **Benefits of the Digital Thread**
- **Traceability**: Track which operator, equipment, and software were used for any measurement
- **Root Cause Analysis**: Identify patterns related to specific operators, stations, or equipment  
- **Compliance**: Meet regulatory requirements for test documentation and traceability
- **Quality Control**: Monitor operator performance and equipment calibration status
- **Reproducibility**: Recreate test conditions by knowing the complete test context
- **Equipment Management**: Track usage and performance of test equipment over time

This comprehensive metadata foundation enables powerful queries such as:
- "Show me all failed tests from Station A1 last month"
- "Find measurements taken with equipment due for calibration"  
- "Compare results between different operators testing the same UUT model"
- "Identify which test adapter was used for all successful RF tests"
- "Track performance trends for specific UUT instances over time"
- "Find all tests using outdated software versions"
- "Correlate test failures with specific test descriptions or procedures"

## **Extensibility**
All metadata entities support custom extensions through:
- **Extension fields** - Custom key-value pairs for entity-specific data
- **Extension schemas** - Formal validation rules for custom fields
- **Schema inheritance** - Extension schemas can be shared across test results

This allows organizations to add company-specific, industry-specific, or regulatory-specific metadata while maintaining compatibility with the core Metadata Store schemas.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/reference/using-measurement-data-services.md sha256=3d65a2dd1dc35acad7a4fa2e5ed2ca8a307f6db37cf2700c87d359c3a773e1ea bytes=19705 -->
## FILE: docs/reference/using-measurement-data-services.md

- repository: `ni/datastore-python`
- source_path: `docs/reference/using-measurement-data-services.md`
- sha256: `3d65a2dd1dc35acad7a4fa2e5ed2ca8a307f6db37cf2700c87d359c3a773e1ea`
- bytes: 19705

````markdown
# Using Measurement Data Services

The NI Measurement Data Services provide a comprehensive solution for storing, organizing, and querying test data and metadata. This document explains the typical workflow for using these services, from initial setup through data analysis.

**Services Overview:**
- **MetadataStoreService** - Manages test context metadata (who, what, where, how)
- **DataStoreService** - Stores and retrieves measurement data and test execution results

## **Complete Workflow Overview**

The typical measurement data workflow follows this sequence:

1. [**Setup Phase**](#setup-phase) - Register metadata entities and schemas
2. [**Test Execution Phase**](#test-execution-phase) - Create test sessions and publish data
3. [**Analysis Phase**](#analysis-phase) - Query and analyze results

## **Required Imports**

Before using the services, import the necessary classes and types:

```python
from datetime import datetime
from ni.datastore.data import DataStoreClient, TestResult, Step, Outcome
from ni.datastore.metadata import MetadataStoreClient
from ni.datastore.metadata import (
    Operator, TestStation, HardwareItem, SoftwareItem,
    Uut, UutInstance, TestDescription, Test, TestAdapter
)
from nitypes.scalar import Scalar
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform
```

(setup-phase)=
## Setup Phase

Before running tests, establish the metadata foundation that describes your test environment and processes.

### **1. Create Core Metadata Entities**

Start by creating the fundamental metadata entities that will be referenced throughout your testing:

#### **Operators**
Register the people who will be running tests:

```python
# Create operators
sarah = Operator(
    name="Sarah Johnson",
    role="Test Engineer",
    schema_id=schema_id,
    extension={
        "department": "Quality Assurance",
        "certification": "Level 2 Test Technician"
    }
)
sarah_id = metadata_store_client.create_operator(sarah)

mike_id = metadata_store_client.create_operator(Operator(
    name="Mike Chen",
    role="Senior Technician",
    schema_id=schema_id,
    extension={
        "department": "Manufacturing",
        "specialization": "RF Testing"
    }
))
```

#### **Test Stations**
Define the physical locations where testing occurs:

```python
# Create test stations
station_a1_id = metadata_store_client.create_test_station(TestStation(
    name="Station_A1",
    asset_identifier="STA-001",
    schema_id=schema_id,
    extension={
        "location": "Building A, Floor 1",
        "station_type": "Production Line"
    }
))

rf_lab_id = metadata_store_client.create_test_station(TestStation(
    name="RF_Lab_Bench_1",
    asset_identifier="RFL-001",
    schema_id=schema_id,
    extension={
        "location": "R&D Lab, Building B",
        "station_type": "Development"
    }
))
```

#### **Hardware Items**
Register test equipment and instruments:

```python
# Create hardware items (test equipment)
dmm = HardwareItem(
    manufacturer="NI",
    model="PXIe-4081",
    serial_number="DMM-001",
    part_number="781061-01",
    calibration_due_date="2025-06-15",
    schema_id=schema_id,
    extension={
        "accuracy": "7.5 digits",
        "asset_tag": "NI-DMM-001"
    }
)
dmm_id = metadata_store_client.create_hardware_item(dmm)

scope_id = metadata_store_client.create_hardware_item(HardwareItem(
    manufacturer="NI",
    model="PXIe-5171",
    serial_number="SCOPE-001",
    part_number="783513-01",
    calibration_due_date="2025-08-20",
    schema_id=schema_id,
    extension={
        "bandwidth": "1 GHz",
        "sample_rate": "1.25 GS/s"
    }
))
```

#### **Software Items**
Document the software environment:

```python
# Create software items
python_id = metadata_store_client.create_software_item(SoftwareItem(
    product="Python",
    version="3.11.5"
))

nidaqmx_id = metadata_store_client.create_software_item(SoftwareItem(
    product="NI-DAQmx",
    version="23.3.0"
))

custom_app_id = metadata_store_client.create_software_item(SoftwareItem(
    product="PowerSupply Test Suite",
    version="v2.1.4",
    schema_id=schema_id,
    extension={
        "build_date": "2024-09-15",
        "git_commit": "a1b2c3d4"
    }
))
```

### **2. Define Products Under Test**

Create UUT definitions and instances:

#### **UUT (Product Definitions)**
```python
# Define the product being tested
power_supply_uut = Uut(
    model_name="PowerSupply v2.1",
    family="Power",
    manufacturers=["ACME Corp"],
    part_number="PS-v2.1-001",
    schema_id=schema_id,
    extension={
        "max_output": "24V, 10A",
        "efficiency": ">90%"
    }
)
power_supply_uut_id = metadata_store_client.create_uut(power_supply_uut)
```

#### **UUT Instances (Physical Devices)**
```python
# Create specific device instances
uut_instance_id = metadata_store_client.create_uut_instance(UutInstance(
    uut_id=power_supply_uut_id,
    serial_number="PS-2024-001456",
    manufacture_date="2024-10-01",
    schema_id=schema_id,
    extension={
        "lot_number": "L2024-Q4-001",
        "assembly_line": "Line 3"
    }
))
```

### **3. Define Test Procedures**

Create test specifications and procedures:

#### **Test Descriptions**
```python
# Create comprehensive test suites
power_test_desc_id = metadata_store_client.create_test_description(TestDescription(
    uut_id=power_supply_uut_id,
    name="Power Supply Validation Suite",
    schema_id=schema_id,
    extension={
        "version": "v2.1",
        "compliance": "IEC 62368-1"
    }
))
```

#### **Individual Tests**
```python
# Create specific test procedures
voltage_test_id = metadata_store_client.create_test(Test(
    name="DC Voltage Accuracy Test",
    description="Measures DC voltage accuracy across 5V, 12V, and 24V outputs",
    schema_id=schema_id,
    extension={
        "test_limits": "±0.1% of reading",
        "test_duration": "~5 minutes"
    }
))

load_test_id = metadata_store_client.create_test(Test(
    name="Load Regulation Test",
    description="Tests voltage stability under varying load conditions",
    schema_id=schema_id,
    extension={
        "load_range": "0% to 100% rated current",
        "regulation_limit": "±0.5%"
    }
))
```

### **4. Register Extension Schemas** *(Optional)*

Define validation schemas for custom extension fields:

```python
# Register a schema for power supply testing
power_supply_schema = """
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "hardware_item": {
      "type": "object",
      "properties": {
        "asset_tag": {"type": "string"},
        "calibration_cert": {"type": "string"},
        "bandwidth": {"type": "string"}
      },
      "required": ["asset_tag"]
    }
  }
}
"""

schema_id = metadata_store_client.register_schema(power_supply_schema)
```

### **5. Create Aliases** *(Optional)*

Set up human-readable names for frequently used entities:

```python
# Create aliases for easy reference
metadata_store_client.create_alias("Primary_DMM", dmm)
metadata_store_client.create_alias("Lead_Test_Engineer", sarah)
metadata_store_client.create_alias("Current_PowerSupply_Design", power_supply_uut)
```

---

(test-execution-phase)=
## Test Execution Phase

With metadata established, execute tests and publish measurement data.

### **1. Create Test Result Session**

Start each test session by creating a **TestResult**:

```python
# Create a test result for this test session
test_result_id = data_store_client.create_test_result(TestResult(
    name="PowerSupply PS-2024-001456 Validation",
    uut_instance_id=uut_instance_id,
    operator_id=sarah_id,  # or use alias: "Lead_Test_Engineer"
    test_station_id=station_a1_id,
    test_description_id=power_test_desc_id,
    software_item_ids=[python_id, nidaqmx_id, custom_app_id],
    hardware_item_ids=[dmm_id, scope_id],  # or use aliases
    schema_id=schema_id,
    extension={
        "test_operator_notes": "First production unit validation",
        "ambient_temperature": "23°C"
    }
))
```

### **2. Create Test Steps**

Organize measurements into logical **Steps**:

```python
# Create test steps within the test result
voltage_step_id = data_store_client.create_step(Step(
    name="DC Voltage Accuracy Check",
    test_result_id=test_result_id,
    test_id=voltage_test_id,
    type="Measurement",
    notes="Testing 5V, 12V, and 24V outputs under no load"
))

load_step_id = data_store_client.create_step(Step(
    name="Load Regulation Test",
    test_result_id=test_result_id,
    test_id=load_test_id,
    type="Measurement",
    notes="Variable load from 0% to 100% rated current"
))
```

### **3. Publish Test Conditions**

Record environmental and setup conditions during testing:

```python
# Publish conditions (environmental/setup parameters)
voltage = Scalar(value=120.0, units="V")
data_store_client.publish_condition(
    condition_name="Supply Voltage",
    type="Input Parameter",
    value=voltage,
    step_id=voltage_step_id
)

temperature = Scalar(value=23.5, units="DegC")
data_store_client.publish_condition(
    condition_name="Temperature",
    type="Environment",
    value=temperature,
    step_id=voltage_step_id
)

humidity = Scalar(value=45.2, units="%RH")
data_store_client.publish_condition(
    condition_name="Humidity",
    type="Environment",
    value=humidity,
    step_id=voltage_step_id
)
```

### **4. Publish Measurements**

Capture actual measurement data:

#### **Single Measurements**
```python
# Publish individual measurements
published_measurement = data_store_client.publish_measurement(
    name="5V Output Voltage",
    value=5.023,  # Measured 5.023V
    timestamp=datetime.now(),
    outcome=Outcome.PASSED,
    step_id=voltage_step_id,
    hardware_item_ids=[dmm_id],
    notes="DMM reading at no load"
)
```

#### **Waveform Measurements**
```python
# Publish complex data (waveforms, spectra, etc.)
waveform_data = AnalogWaveform(
    samples=[1.0, 2.0, 3.0, 2.0, 1.0, 0.0, -1.0],
    sample_interval=1e-6,  # 1 µs per sample
    start_time=0.0
)

data_store_client.publish_measurement(
    name="Output Ripple Waveform",
    value=waveform_data,
    timestamp=datetime.now(),
    outcome=Outcome.PASSED,
    step_id=voltage_step_id,
    hardware_item_ids=[scope_id],
    notes="Ripple measurement at full load"
)
```

#### **Batch Measurements**
```python
# Publish multiple related measurements efficiently
load_currents = [0.0, 2.5, 5.0, 7.5, 10.0]  # Load current sweep
output_voltages = [5.025, 5.023, 5.021, 5.019, 5.018]  # Corresponding voltages

data_store_client.publish_measurement_batch(
    name="Load Regulation Sweep",
    values=output_voltages,
    timestamps=[datetime.now()] * len(output_voltages),
    outcomes=[Outcome.PASSED] * len(output_voltages),
    step_id=load_step_id,
    hardware_item_ids=[dmm_id]
)

# Publish corresponding load conditions
data_store_client.publish_condition_batch(
    name="Load Current",
    condition_type="Test Parameter",
    values=load_currents,
    step_id=load_step_id
)
```

(analysis-phase)=
## Analysis Phase

Query and analyze the stored measurement data and metadata.

### **1. Query Measurements**

Use OData queries to find and filter measurement data:

#### **Basic Queries**
```python
# Find all measurements from a specific test result
measurements = data_store_client.query_measurements(
    odata_query=f"$filter=TestResultId eq {test_result_id}"
)

# Find failed measurements
failed_measurements = data_store_client.query_measurements(
    odata_query="$filter=Outcome eq 'Failed'"
)

# Find measurements by name
voltage_measurements = data_store_client.query_measurements(
    odata_query="$filter=contains(name, 'Voltage')"
)
```

#### **Complex Queries**
```python
# Find measurements from specific equipment that failed
equipment_failures = data_store_client.query_measurements(
    odata_query=f"$filter=outcome eq 'Failed' and contains(HardwareItemIds, {dmm_id})"
)

# Find recent measurements
recent_measurements = data_store_client.query_measurements(
    odata_query="$filter=StartTime gt 2024-10-01T00:00:00Z&$orderby=StartTime"
)

# Find measurements from specific operator
operator_measurements = data_store_client.query_measurements(
    odata_query=f"$filter=TestResultId eq {test_result_id} and OperatorId eq {sarah_id}"
)
```

### **2. Query Test Context**

Analyze test metadata to understand patterns:

#### **Test Results Analysis**
```python
# Find all steps for a particular test results
test_steps = data_store_client.query_steps(
    odata_query=f"$filter=TestResultId eq {test_result_id}"
)

# Find operator named 'Sarah Johnson'
sarah_tests = metadata_store_client.query_operators(
    odata_query="$filter=Name eq 'Sarah Johnson'"
)
```

#### **Equipment Usage Tracking**
```python
# Find measurements using specific equipment
equipment_usage = data_store_client.query_measurements(
    odata_query=f"$filter=HardwareItems/any(h: h/Id eq {scope_id})"
)
```

### **3. Retrieve Measurement Data**

Access the actual measured values:

```python
# Get measurement data
for measurement in measurements:
    if measurement.data_type == "type.googleapis.com/ni.protobuf.types.Vector":
        value = data_store_client.read_data(measurement, expected_type=Vector)
        print(f"{measurement.name}: {value}")
    elif measurement.data_type == "type.googleapis.com/ni.protobuf.types.DoubleAnalogWaveform":
        waveform = data_store_client.read_data(measurement, expected_type=AnalogWaveform)
        print(f"{measurement.name}: {len(waveform.raw_data)} samples")
```

### **4. Cross-Reference with Metadata**

Combine measurement data with metadata for comprehensive analysis:

```python
# Analyze test results with full context
for measurement in measurements:
    # Get associated metadata
    test_result = data_store_client.get_test_result(measurement.test_result_id)
    step = data_store_client.get_step(measurement.step_id)

    # Get UUT instance and model info
    uut_instance = metadata_store_client.get_uut_instance(test_result.uut_instance_id)
    uut = metadata_store_client.get_uut(uut_instance.uut_id)

    # Get operator info
    operator = metadata_store_client.get_operator(test_result.operator_id)

    # Get equipment info
    hardware_items = [
        metadata_store_client.get_hardware_item(hw_id)
        for hw_id in measurement.hardware_item_ids
    ]

    print(f"Measurement: {measurement.name}")
    print(f"  UUT: {uut.model_name} S/N: {uut_instance.serial_number}")
    print(f"  Operator: {operator.name} ({operator.role})")
    print(f"  Equipment: {[hw.model for hw in hardware_items]}")
    print(f"  Outcome: {measurement.outcome}")
```

### **5. Advanced Analysis Examples**

#### **Trend Analysis**
```python
# Track performance over time for a UUT model
uut_instances = metadata_store_client.query_uut_instances(
    odata_query=f"$filter=UutId eq '{power_supply_uut_id}'"
)

for instance in uut_instances:
    # Get test results for this UUT instance
    test_results = data_store_client.query_test_results(
        odata_query=f"$filter=UutInstanceId eq '{instance.id}'"
    )
    for test_result in test_results:
        measurements = data_store_client.query_measurements(
            odata_query=f"$filter=TestResultId eq '{test_result.id}' and Name eq '5V Output Voltage'"
        )
        # Analyze voltage accuracy trends...
```

#### **Equipment Performance Analysis**
```python
# Analyze calibration impact on measurements
pre_cal_measurements = data_store_client.query_measurements(
    odata_query=f"$filter=contains(HardwareItemIds, '{dmm_id}') and start_date_time lt '2024-06-15'"
)

post_cal_measurements = data_store_client.query_measurements(
    odata_query=f"$filter=contains(HardwareItemIds, '{dmm_id}') and start_date_time gt '2024-06-15'"
)
# Compare measurement accuracy before/after calibration...
```

#### **Operator Performance Comparison**
```python
# Compare test results between operators
for operator_id in [sarah_id, mike_id]:
    operator = metadata_store_client.get_operator(operator_id)
    measurements = data_store_client.query_measurements(
        odata_query=f"$filter=OperatorId eq '{operator_id}' and outcome eq 'Failed'"
    )
    failure_rate = len(measurements) / total_measurements_by_operator[operator_id] * 100
    print(f"{operator.name}: {failure_rate:.1f}% failure rate")
```

---

## **Best Practices**

### **Metadata Management**
- **Create aliases** for frequently referenced entities
- **Use extension schemas** to enforce data consistency
- **Register metadata entities once** and reuse across multiple tests
- **Keep calibration dates current** for traceability

### **Test Execution**
- **Always create a TestResult** before publishing measurements
- **Group related measurements** into logical Steps
- **Include environmental conditions** that might affect results
- **Use batch operations** for parametric sweeps to improve performance

### **Data Organization**
- **Use consistent naming conventions** for measurements and steps
- **Include meaningful notes** and descriptions
- **Associate measurements with relevant hardware/software** for traceability
- **Set appropriate outcomes** (PASSED/FAILED/INDETERMINATE) for analysis

### **Querying and Analysis**
- **Use specific OData filters** to reduce query response size
- **Combine metadata and measurement queries** for comprehensive analysis
- **Cache frequently accessed metadata** entities
- **Use measurement names and types** to group related data

---

## **Integration Patterns**

### **Automated Test Systems**
```python
class TestAutomation:
    def __init__(self):
        self.metadata_client = MetadataStoreClient()
        self.data_client = DataStoreClient()

    def run_automated_test(self, uut_serial: str):
        # 1. Look up UUT instance by serial number
        instances = self.metadata_client.query_uut_instances(
            odata_query=f"$filter=serial_number eq '{uut_serial}'"
        )

        # 2. Create test result
        test_result_id = self.data_client.create_test_result(...)

        # 3. Execute test steps
        for test_step in self.test_sequence:
            step_id = self.data_client.create_step(...)
            self.execute_step(step_id, test_step)

        # 4. Determine overall result
        self.finalize_test_result(test_result_id)
```

### **Batch Processing**
```python
def process_test_batch(uut_serials: List[str]):
    """Process multiple UUTs efficiently."""

    # Create all test results first
    test_result_ids = []
    for serial in uut_serials:
        test_result_id = data_store_client.create_test_result(...)
        test_result_ids.append(test_result_id)

    # Execute tests in parallel/batch
    for test_result_id in test_result_ids:
        execute_test_sequence(test_result_id)

    # Analyze results
    analyze_batch_results(test_result_ids)
```

This comprehensive workflow ensures full traceability, enables powerful analysis capabilities, and maintains data integrity across your entire test ecosystem.
````

<!--NI_OSS_SOURCE repo=datastore-python path=docs/templates/autoapi/index.rst sha256=f8b8247995390ceec51bef4eecb0ff76d6f4222b75f5935ef4539f5fc1bd2d19 bytes=624 -->
## FILE: docs/templates/autoapi/index.rst

- repository: `ni/datastore-python`
- source_path: `docs/templates/autoapi/index.rst`
- sha256: `f8b8247995390ceec51bef4eecb0ff76d6f4222b75f5935ef4539f5fc1bd2d19`
- bytes: 624

````rst
API Reference
=============

This page contains auto-generated API reference documentation.

..
   Custom index: reference https://github.com/readthedocs/sphinx-autoapi/issues/298
   Add the top most levels in "ni.datastore" to the index file
   This is needed because we don't have __init__.py file in ni
   and ni/measurementlink etc. package as we use nested implicit namespace packages.

.. toctree::
   :titlesonly:

   {% for page in pages | sort %}
   {% if (page.top_level_object or page.name.split('.') | length == 5) and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/alias/alias.ipynb sha256=64704d5c99d712cb8b73c1d4a1b6cd9251724a06602bed123cb94f4b7a702ff2 bytes=6570 -->
## FILE: examples/notebooks/alias/alias.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/alias/alias.ipynb`
- sha256: `64704d5c99d712cb8b73c1d4a1b6cd9251724a06602bed123cb94f4b7a702ff2`
- bytes: 6570

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "80459a41",
   "metadata": {},
   "source": [
    "## Create the metadata to alias\n",
    "\n",
    "In this example, we create two Operators that we will subsequently alias."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a47d341",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.metadata import MetadataStoreClient, Operator\n",
    "\n",
    "metadata_store_client = MetadataStoreClient()\n",
    "operatorOne = Operator(name=\"Jane Doe\")\n",
    "operatorTwo = Operator(name=\"John Smith\")\n",
    "\n",
    "metadata_store_client.create_operator(operatorOne)\n",
    "metadata_store_client.create_operator(operatorTwo)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87f1c133",
   "metadata": {},
   "source": [
    "## Create aliases for the desired metadata\n",
    "\n",
    "Note: The metadata being aliased must have already been created prior to creating the alias."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf3e749f",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client.create_alias(\"primary_operator\", operatorOne)\n",
    "metadata_store_client.create_alias(\"secondary_operator\", operatorTwo)\n",
    "\n",
    "print(\"Aliases created successfully.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45b02d4d",
   "metadata": {},
   "source": [
    "## Reference the alias\n",
    "\n",
    "You can reference the alias in place of the metadata ID when creating further metadata or publishing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc2f25dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ni.datastore.data import DataStoreClient, TestResult\n",
    "\n",
    "test_result = TestResult(\n",
    "    name=\"Test Result with Operator Alias\",\n",
    "    operator_id=\"secondary_operator\"\n",
    ")\n",
    "\n",
    "data_store_client = DataStoreClient()\n",
    "test_result_id = data_store_client.create_test_result(test_result)\n",
    "\n",
    "print(\"The test results was created successfully using an alias to reference an operator.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be0577f7",
   "metadata": {},
   "source": [
    "## Verify expected alias usage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae1752d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve the session and verify which operator was associated with it\n",
    "retrieved_session = data_store_client.get_test_result(test_result_id)\n",
    "retrieved_operator_id = retrieved_session.operator_id\n",
    "operator_details = metadata_store_client.get_operator(retrieved_operator_id)\n",
    "\n",
    "print(f\"The name of the operator for the session: {operator_details.name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb01d26b",
   "metadata": {},
   "source": [
    "## Get alias\n",
    "\n",
    "Look up the target information of the alias (i.e. what the alias is an alias for)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63161fc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "alias = metadata_store_client.get_alias(\"primary_operator\")\n",
    "\n",
    "print(alias)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b62e51cc",
   "metadata": {},
   "source": [
    "## Query all aliases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d98697f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "aliases = metadata_store_client.query_aliases(\"\")\n",
    "for alias in aliases:\n",
    "    print(alias)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80f5ed9d",
   "metadata": {},
   "source": [
    "## Query aliases with filter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9087da6",
   "metadata": {},
   "outputs": [],
   "source": [
    "aliases = metadata_store_client.query_aliases(\"$filter=name eq 'primary_operator'\")\n",
    "for alias in aliases:\n",
    "    print(alias)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0f54d82",
   "metadata": {},
   "source": [
    "## Delete alias\n",
    "\n",
    "Deletes an existing alias on the system. This does not affect the underlying target/metadata to which the alias refers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1eadddff",
   "metadata": {},
   "outputs": [],
   "source": [
    "deleted = metadata_store_client.delete_alias(\"primary_operator\")\n",
    "\n",
    "print(f\"Success of deleting 'primary_operator': {deleted}\\n\")\n",
    "\n",
    "## Query the aliases again to confirm the alias has been removed\n",
    "aliases = metadata_store_client.query_aliases(\"\")\n",
    "for alias in aliases:\n",
    "    print(alias)\n",
    "\n",
    "# Try to delete the alias again. This should not succeed since the alias has already been removed.\n",
    "deleted = metadata_store_client.delete_alias(\"primary_operator\")\n",
    "print(f\"Success of deleting already-removed 'primary_operator': {deleted}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b253668",
   "metadata": {},
   "source": [
    "## Clean up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31c628e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ni-datastore-py3.14",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/extension-attributes/cable_schema.toml sha256=1788895c1b729a2c9cdc75723769c4aa0e379c1a183bdd054c39b7019964c594 bytes=107 -->
## FILE: examples/notebooks/extension-attributes/cable_schema.toml

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/extension-attributes/cable_schema.toml`
- sha256: `1788895c1b729a2c9cdc75723769c4aa0e379c1a183bdd054c39b7019964c594`
- bytes: 107

````toml
id = "https://example.com/cable.schema.toml"

[hardware_item]
cable_length = "*"
manufacture_date = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/extension-attributes/extension_attributes.ipynb sha256=dd54e10b4048002439a2d87dd094d015af6a69d8d8282700375a34bbdaa0bd9f bytes=8072 -->
## FILE: examples/notebooks/extension-attributes/extension_attributes.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/extension-attributes/extension_attributes.ipynb`
- sha256: `dd54e10b4048002439a2d87dd094d015af6a69d8d8282700375a34bbdaa0bd9f`
- bytes: 8072

````text
{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "0c023578",
      "metadata": {},
      "source": [
        "## Create Multiple Hardware Schemas\n",
        "\n",
        "When a measurement is associated with multiple hardware entities, it may be desirable for each type of hardware to have its own metadata schema.  This demonstrates how to create multiple hardware entities with different schemas."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8245e640",
      "metadata": {},
      "outputs": [],
      "source": [
        "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
        "from utilities import DataStoreContext\n",
        "data_store_context = DataStoreContext()\n",
        "data_store_context.initialize()\n",
        "\n",
        "from ni.datastore.metadata import MetadataStoreClient\n",
        "\n",
        "metadata_store_client = MetadataStoreClient()\n",
        "# Register schemas\n",
        "cable_schema_id = metadata_store_client.register_schema_from_file(\"cable_schema.toml\")\n",
        "socket_schema_id = metadata_store_client.register_schema_from_file(\"socket_schema.toml\")\n",
        "scope_schema_id = metadata_store_client.register_schema_from_file(\"scope_schema.toml\")\n",
        "test_result_schema_id = metadata_store_client.register_schema_from_file(\"test_result_schema.toml\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "936b1eca",
      "metadata": {},
      "source": [
        "## Create the Hardware Objects with their Extension Attributes\n",
        "\n",
        "Now that the schemas are registered, we can create Hardware objects that specify extension attributes to meet the requirements of the registered schemas.  Each piece of hardware can use it's own schema."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "13d59ad8",
      "metadata": {},
      "outputs": [],
      "source": [
        "from ni.datastore.metadata import HardwareItem\n",
        "\n",
        "cable = HardwareItem(\n",
        "    manufacturer=\"NI\",\n",
        "    model=\"cable\",\n",
        "    serial_number=\"7u2349\",\n",
        "    schema_id=cable_schema_id,\n",
        ")\n",
        "cable.extension[\"cable_length\"] = \"1.5\"\n",
        "cable.extension[\"manufacture_date\"] = \"2023-01-01\"\n",
        "\n",
        "socket = HardwareItem(\n",
        "    manufacturer=\"NI\",\n",
        "    model=\"socket\",\n",
        "    schema_id=socket_schema_id,\n",
        ")\n",
        "socket.extension[\"socket_number\"] = \"3\"\n",
        "socket.extension[\"manufacture_date\"] = \"2024-05-01\"\n",
        "\n",
        "scope = HardwareItem(\n",
        "    manufacturer=\"NI\",\n",
        "    model=\"PXIe-5171\",\n",
        "    serial_number=\"1933B4E\",\n",
        "    schema_id=scope_schema_id,\n",
        ")\n",
        "scope.extension[\"bandwidth\"] = \"250 MHz\"\n",
        "scope.extension[\"manufacture_date\"] = \"2024-11-03\""
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3fac7e79",
      "metadata": {},
      "source": [
        "## Create a Schema for the Test Result (optional)\n",
        "\n",
        "If you specify a schema for the test result, it will ensure that all the hardware extension attributes are a superset of whatever metadata is specified in the session schema.  This allows the author to ensure all hardware has some consistent attributes.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b40414fa",
      "metadata": {},
      "outputs": [],
      "source": [
        "test_result_schema_id = metadata_store_client.register_schema_from_file(\"test_result_schema.toml\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "3a5be765",
      "metadata": {},
      "source": [
        "## Publish a Measurement with the Hardware\n",
        "\n",
        "Now that all the schemas have been registered and the hardware objects have been created, we can publish our data with the associated hardware."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fc2373bd",
      "metadata": {},
      "outputs": [],
      "source": [
        "from datetime import timezone\n",
        "import hightime as ht\n",
        "from ni.datastore.data import DataStoreClient, TestResult, Step\n",
        "from nitypes.waveform import AnalogWaveform\n",
        "from nitypes.waveform import Timing\n",
        "import numpy as np\n",
        "\n",
        "cable_id = metadata_store_client.create_hardware_item(hardware_item=cable)\n",
        "socket_id = metadata_store_client.create_hardware_item(hardware_item=socket)\n",
        "scope_id = metadata_store_client.create_hardware_item(hardware_item=scope)\n",
        "\n",
        "data_store_client = DataStoreClient()\n",
        "test_result_id = data_store_client.create_test_result(\n",
        "    test_result=TestResult(\n",
        "        name=\"scope measurements\",\n",
        "        hardware_item_ids=[cable_id, socket_id, scope_id],\n",
        "        schema_id=test_result_schema_id\n",
        "    )\n",
        ")\n",
        "\n",
        "waveform = AnalogWaveform(\n",
        "    sample_count=3,\n",
        "    raw_data=np.array([1.0, 2.0, 3.0]),\n",
        "    timing=Timing.create_with_regular_interval(\n",
        "        ht.timedelta(seconds=1e-3),\n",
        "        ht.datetime.now(timezone.utc)\n",
        "    )\n",
        ")\n",
        "\n",
        "step = Step(name=\"Initial step\", test_result_id=test_result_id)\n",
        "step_id = data_store_client.create_step(step)\n",
        "data_store_client.publish_measurement(\n",
        "    name=\"scope reading\",\n",
        "    value=waveform,\n",
        "    step_id=step_id,\n",
        ")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "cf634ecb",
      "metadata": {},
      "source": [
        "## Query for the Published Data\n",
        "\n",
        "Now that we've published some data, we can use our OData query API to find it"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e746e6ac",
      "metadata": {},
      "outputs": [],
      "source": [
        "published_measurements = data_store_client.query_measurements(\"$filter=name eq 'scope reading'\")\n",
        "found_measurement = next(iter(published_measurements), None)\n",
        "if found_measurement is not None:\n",
        "    waveform = data_store_client.read_measurement_value(found_measurement, expected_type=AnalogWaveform)\n",
        "    print(f\"published data is: {waveform.raw_data}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f5e0fcfd",
      "metadata": {},
      "source": [
        "## Clean Up"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f143478e",
      "metadata": {},
      "outputs": [],
      "source": [
        "metadata_store_client.close()\n",
        "data_store_client.close()\n",
        "\n",
        "# Perform example-specific cleanup. This is not needed when writing production code.\n",
        "data_store_context.close()"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "ni-datastore-py3.10",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.11"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/extension-attributes/scope_schema.toml sha256=afe5d71139bf27c26372ab26243c5190c5b95d07d9bb1e0bbcfd5b7cd66fcf2e bytes=104 -->
## FILE: examples/notebooks/extension-attributes/scope_schema.toml

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/extension-attributes/scope_schema.toml`
- sha256: `afe5d71139bf27c26372ab26243c5190c5b95d07d9bb1e0bbcfd5b7cd66fcf2e`
- bytes: 104

````toml
id = "https://example.com/scope.schema.toml"

[hardware_item]
bandwidth = "*"
manufacture_date = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/extension-attributes/socket_schema.toml sha256=72220408ccd0ba25df7707b01890125728e71fdcf9c47e336e460c18a2e3f4a2 bytes=109 -->
## FILE: examples/notebooks/extension-attributes/socket_schema.toml

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/extension-attributes/socket_schema.toml`
- sha256: `72220408ccd0ba25df7707b01890125728e71fdcf9c47e336e460c18a2e3f4a2`
- bytes: 109

````toml
id = "https://example.com/socket.schema.toml"

[hardware_item]
socket_number = "*"
manufacture_date = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/extension-attributes/test_result_schema.toml sha256=80ba905e7c1996bba7522a069db9884d30166f49e9b42361fa00af3a13c206c4 bytes=89 -->
## FILE: examples/notebooks/extension-attributes/test_result_schema.toml

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/extension-attributes/test_result_schema.toml`
- sha256: `80ba905e7c1996bba7522a069db9884d30166f49e9b42361fa00af3a13c206c4`
- bytes: 89

````toml
id = "https://example.com/session.schema.toml"

[hardware_item]
manufacture_date = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/overview/publish_measurement.ipynb sha256=3c98d625872a17f49a66ff7addda30a18726346b72009adf086e70bb68a9edbb bytes=11047 -->
## FILE: examples/notebooks/overview/publish_measurement.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/overview/publish_measurement.ipynb`
- sha256: `3c98d625872a17f49a66ff7addda30a18726346b72009adf086e70bb68a9edbb`
- bytes: 11047

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d517ee3e",
   "metadata": {},
   "source": [
    "## Create a client\n",
    "\n",
    "To get started creating metadata and publishing measurements, the client code must first instantiate a `MetadataStoreClient` and `DataStoreClient`, respectively. The `MetadataStoreClient` is used for creating and querying metadata, and the `DataStoreClient` is used for publishing and querying measurements and conditions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eafd7dce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.data import DataStoreClient\n",
    "from ni.datastore.metadata import MetadataStoreClient\n",
    "\n",
    "metadata_store_client = MetadataStoreClient()\n",
    "data_store_client = DataStoreClient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8711333",
   "metadata": {},
   "source": [
    "__Recommendation:__ A client can be used within the context of a `with` statement in order to have its lifetime managed for it. Upon exiting the `with` statement, any gRPC channels owned by the client will be closed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2af68b27",
   "metadata": {},
   "outputs": [],
   "source": [
    "with MetadataStoreClient() as metadata_store_client_one:\n",
    "    query_results = metadata_store_client_one.query_hardware_items()  \n",
    "    # ... Perform any further operations with metadata_store_client_one ...\n",
    "\n",
    "# metadata_store_client_one will automatically close upon exiting the 'with' block"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "849e51c1",
   "metadata": {},
   "source": [
    "Alternatively, the `close()` method of the client may be called to perform the same cleanup that occurs when exiting the `with` block above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c71da07",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client_two = MetadataStoreClient()\n",
    "\n",
    "query_results = metadata_store_client_two.query_hardware_items()\n",
    "# ... Perform any further operations with metadata_store_client_two ...\n",
    "\n",
    "# Manually close the client when done using it\n",
    "metadata_store_client_two.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f4485f7",
   "metadata": {},
   "source": [
    "Because notebooks such as the current example do not support splitting a single `with` statement across multiple code snippets, this example opts to call `close()` manually in the last code snippet."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "146b50e3",
   "metadata": {},
   "source": [
    "## Register a metadata schema\n",
    "\n",
    "The registration of the metadata schema is usually done by the administrator of the system. The metadata schema is defined in a JSON file, which is then registered in the system. This registration is not usually done as part of running tests or capturing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f236135d",
   "metadata": {},
   "outputs": [],
   "source": [
    "schema_id = metadata_store_client.register_schema_from_file(\"sample_schema.json\")\n",
    "print(f\"registered schema id: {schema_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1f1b11c",
   "metadata": {},
   "source": [
    "## Create the test result metadata\n",
    "\n",
    "Now that a schema has been registered we can create our metadata objects with the expected metadata.  Note, however, the creation of each metadata object must include the required values from the schema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acce3488",
   "metadata": {},
   "outputs": [],
   "source": [
    "import grpc\n",
    "from ni.datastore.data import TestResult\n",
    "from ni.datastore.metadata import Operator, TestStation, SoftwareItem\n",
    "\n",
    "# Invalid creation of operator - no badge_number provided\n",
    "operator = Operator(name=\"James Bowery\", schema_id=schema_id)\n",
    "try:\n",
    "    operator_id = metadata_store_client.create_operator(operator)\n",
    "except grpc.RpcError as e:\n",
    "    print(\"Failed to create operator:\")\n",
    "    print(f\"  {e.details()}\")\n",
    "\n",
    "# Add the required attribute to the operator object\n",
    "operator.extension[\"badge_number\"] = \"emp-128256\"\n",
    "operator_id = metadata_store_client.create_operator(operator)\n",
    "\n",
    "# Invalid creation of test station - location is invalid\n",
    "test_station = TestStation(name=\"TestStation_12\", schema_id=schema_id)\n",
    "test_station.extension[\"location\"] = \"Texas\"\n",
    "try:\n",
    "    test_station_id = metadata_store_client.create_test_station(test_station)\n",
    "except grpc.RpcError as e:\n",
    "    print(\"Failed to create test station:\")\n",
    "    print(f\"  {e.details()}\")\n",
    "\n",
    "# Fix the location\n",
    "test_station.extension[\"location\"] = \"USA\"\n",
    "test_station_id = metadata_store_client.create_test_station(test_station)\n",
    "\n",
    "# Invalid creation of software item -  software license is invalid (not matching the pattern defined in the schema)\n",
    "software_item = SoftwareItem(product=\"Windows\", version=\"10.0.19044\", schema_id=schema_id)\n",
    "software_item.extension[\"license\"] = \"enterprise_LIC\"\n",
    "try:\n",
    "    software_item_id = metadata_store_client.create_software_item(software_item)\n",
    "except grpc.RpcError as e:\n",
    "    print(\"Failed to create software item:\")\n",
    "    print(f\"  {e.details()}\")\n",
    "\n",
    "# Fix the software license to create the software item\n",
    "software_item.extension[\"license\"] = \"LIC_enterprise\"\n",
    "software_item_id = metadata_store_client.create_software_item(software_item)\n",
    "    \n",
    "test_result = TestResult(\n",
    "    name=\"sample publish test result\",\n",
    "    operator_id=operator_id,\n",
    "    test_station_id=test_station_id,\n",
    "    schema_id=schema_id,\n",
    "    software_item_ids=[software_item_id])\n",
    "test_result.extension[\"session_file_path\"] = \"C:\\\\my_test_description.xlsx\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6f56576",
   "metadata": {},
   "source": [
    "## Create the test result object\n",
    "\n",
    "Now that we have the test result metadata, we can create the test result object. Note below that schema validation can fail if your metadata does not match what's specified in the schema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "406d8b27",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_result_id = data_store_client.create_test_result(test_result)\n",
    "print(f\"created test result id: {test_result_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00e15a92",
   "metadata": {},
   "source": [
    "## Publish the data\n",
    "\n",
    "Now that we have a valid test result and schema, we can publish our data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cd1475d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import timezone\n",
    "import hightime as ht\n",
    "from nitypes.waveform import AnalogWaveform\n",
    "from nitypes.waveform import Timing\n",
    "import numpy as np\n",
    "from ni.datastore.data import Step\n",
    "\n",
    "name = \"data publish sample\"\n",
    "waveform = AnalogWaveform(\n",
    "    sample_count=3,\n",
    "    raw_data=np.array([1.0, 2.0, 3.0]),\n",
    "    timing=Timing.create_with_regular_interval(\n",
    "        ht.timedelta(seconds=1e-3),\n",
    "        ht.datetime.now(timezone.utc)\n",
    "    )\n",
    ")\n",
    "step = Step(name=\"Initial step\", test_result_id=test_result_id)\n",
    "step_id = data_store_client.create_step(step)\n",
    "published_measurement_id = data_store_client.publish_measurement(\n",
    "    name=name,\n",
    "    value=waveform,\n",
    "    step_id=step_id,\n",
    ")\n",
    "print(f\"The published measurement id is {published_measurement_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "829f2743",
   "metadata": {},
   "source": [
    "## Query the data\n",
    "\n",
    "Now that we've got data in the database, we can query for it using our OData query api."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e912c77",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nitypes.waveform import AnalogWaveform\n",
    "\n",
    "published_measurements = data_store_client.query_measurements(odata_query=f\"$filter=id eq {published_measurement_id}\")\n",
    "found_measurement = next(iter(published_measurements), None)\n",
    "\n",
    "if found_measurement is not None:\n",
    "    test_result = data_store_client.get_test_result(found_measurement.test_result_id)\n",
    "    operator = metadata_store_client.get_operator(test_result.operator_id)\n",
    "    # badge_number is a custom attribute in the schema\n",
    "    # It's not a standard attribute of the operator object\n",
    "    badge_number = operator.extension[\"badge_number\"]\n",
    "    print(f\"operator {operator.name}'s badge number is: {badge_number}\")\n",
    "\n",
    "    waveform = data_store_client.read_measurement_value(found_measurement, expected_type=AnalogWaveform)\n",
    "    print(f\"published data is: {waveform.raw_data}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f731b1e",
   "metadata": {},
   "source": [
    "## Clean up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dbc1f07",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client.close()\n",
    "data_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/overview/sample_schema.json sha256=6d86ca70dec5bb32b39ea37992ab06c31643c34a9060d502a492b00d11be7bf0 bytes=1099 -->
## FILE: examples/notebooks/overview/sample_schema.json

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/overview/sample_schema.json`
- sha256: `6d86ca70dec5bb32b39ea37992ab06c31643c34a9060d502a492b00d11be7bf0`
- bytes: 1099

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/sample.schema.json",
  "title": "default test schema",
  "description": "A schema for the metadata of test measurements",
  "type": "object",
  "properties": {
    "test_result": {
      "type": "object",
      "properties": {
        "session_file_path": {
          "type": "string"
        }
      }
    },
    "operator": {
      "type": "object",
      "properties": {
        "badge_number": {
          "type": "string"
        }
      },
      "required": ["badge_number"]
    },
    "test_station": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "pattern": "^TestStation_\\d+$"
        },
        "location": {
          "type": "string",
          "enum": ["USA", "Canada", "Mexico"]
        }
      }
    },
    "software_item": {
      "type": "object",
      "properties": {
        "license": {
          "type": "string",
          "pattern": "^LIC_\\w+$"
        }
      }
    }
  }
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/publish/publish_batch.ipynb sha256=0a3a5d3b5468ef27fbf6b182872506ed836b9a466146c966b3c025b52fef7bec bytes=20511 -->
## FILE: examples/notebooks/publish/publish_batch.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/publish/publish_batch.ipynb`
- sha256: `0a3a5d3b5468ef27fbf6b182872506ed836b9a466146c966b3c025b52fef7bec`
- bytes: 20511

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e524afa7",
   "metadata": {},
   "source": [
    "# Batch Publishing\n",
    "\n",
    "This notebook demonstrates how to use the `DataStoreClient` to batch publish N iterations of data within a given `Step`. Rather than calling `publish_condition` or `publish_measurement` N times to publish data for each of these N iterations, this data can instead be published by a single call to `publish_condition_batch` or `publish_measurement_batch`, respectively. Batch publishing can help improve overall publishing performance.\n",
    "\n",
    "**Note:** These batching APIs handle batch publishing N iterations of data for a single condition or measurement with the specified name. They do *not* support publishing data across multiple (distinctly named) conditions or multiple (distinctly named) measurements at once."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6876aeb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "# Create the TestResult and Step into which we will later batch publish conditions and measurements.\n",
    "from ni.datastore.data import DataStoreClient, Step, TestResult\n",
    "\n",
    "data_store_client = DataStoreClient()\n",
    "\n",
    "test_result = TestResult(name=\"Batch Publish Example\")\n",
    "test_result_id = data_store_client.create_test_result(test_result)\n",
    "\n",
    "step = Step(name=\"Example Step\", test_result_id=test_result_id)\n",
    "step_id = data_store_client.create_step(step)\n",
    "\n",
    "print(f\"Created Test Result: {test_result_id}\")\n",
    "print(f\"Created Step: {step_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94b7bc49",
   "metadata": {},
   "source": [
    "## Batch Publishing Condition Values\n",
    "\n",
    "The `publish_condition_batch` method of `DataStoreClient` can be used to publish the value of a given condition across N parametric iterations at once. This usage of `publish_condition_batch` is equivalent to calling `publish_condition` for that same condition N times.\n",
    "\n",
    "The condition values themselves may be supplied to `publish_condition_batch` as either an `Iterable` or a `Vector`.\n",
    "\n",
    "Supported element types of the `Iterable` are `float`, `int`, `str`, and `bool`: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c7c5e72",
   "metadata": {},
   "outputs": [],
   "source": [
    "float_condition_id = data_store_client.publish_condition_batch(\n",
    "    name=\"Example Float Condition\",\n",
    "    condition_type=\"Setup\",\n",
    "    values=[1.25, 2.5, 3.75, 5.0],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "integer_condition_id = data_store_client.publish_condition_batch(\n",
    "    name=\"Example Integer Condition\",\n",
    "    condition_type=\"Setup\",\n",
    "    values=[1, 2, 3, 4],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "string_condition_id = data_store_client.publish_condition_batch(\n",
    "    name=\"Example String Condition\",\n",
    "    condition_type=\"Setup\",\n",
    "    values=[\"cold\", \"ambient\", \"warm\", \"hot\"],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "bool_condition_id = data_store_client.publish_condition_batch(\n",
    "    name=\"Example Bool Condition\",\n",
    "    condition_type=\"Setup\",\n",
    "    values=[True, False, True, False],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "print(f\"Published Example Float Condition ID: {float_condition_id}\")\n",
    "print(f\"Published Example Integer Condition ID: {integer_condition_id}\")\n",
    "print(f\"Published Example String Condition ID: {string_condition_id}\")\n",
    "print(f\"Published Example Bool Condition ID: {bool_condition_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1056ff7a",
   "metadata": {},
   "source": [
    "Supplying a `Vector` allows the client to specify additional information, such as units:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73e3a3ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nitypes.vector import Vector\n",
    "\n",
    "condition_vector = Vector(values=[0.5, 1.0, 1.5, 2.0], units=\"Amps\")\n",
    "\n",
    "vector_condition_id = data_store_client.publish_condition_batch(\n",
    "    name=\"Example Published-As-Vector Condition\",\n",
    "    condition_type=\"Setup\",\n",
    "    values=condition_vector,\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "print(f\"Published Example Published-As-Vector Condition ID: {vector_condition_id}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67347f3d",
   "metadata": {},
   "source": [
    "Published condition values can be read back in the same manner as when reading back condition values that were published individually via `publish_condition`.\n",
    "\n",
    "More specifically, condition values published via `publish_condition_batch` are read back as a `Vector` containing all N iterations of parametric data published for a particular condition:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e72da95e",
   "metadata": {},
   "outputs": [],
   "source": [
    "published_float_condition = data_store_client.get_condition(float_condition_id)\n",
    "published_integer_condition = data_store_client.get_condition(integer_condition_id)\n",
    "published_string_condition = data_store_client.get_condition(string_condition_id)\n",
    "published_bool_condition = data_store_client.get_condition(bool_condition_id)\n",
    "published_as_vector_condition = data_store_client.get_condition(vector_condition_id)\n",
    "\n",
    "read_back_float_vector = data_store_client.read_condition_value(published_float_condition, expected_type=Vector)\n",
    "read_back_integer_vector = data_store_client.read_condition_value(published_integer_condition, expected_type=Vector)\n",
    "read_back_string_vector = data_store_client.read_condition_value(published_string_condition, expected_type=Vector)\n",
    "read_back_bool_vector = data_store_client.read_condition_value(published_bool_condition, expected_type=Vector)\n",
    "read_back_vector = data_store_client.read_condition_value(published_as_vector_condition, expected_type=Vector)\n",
    "\n",
    "print(f\"Read Example Float Condition: {read_back_float_vector}\")\n",
    "print(f\"Read Example Integer Condition: {read_back_integer_vector}\")\n",
    "print(f\"Read Example String Condition: {read_back_string_vector}\")\n",
    "print(f\"Read Example Bool Condition: {read_back_bool_vector}\")\n",
    "print(f\"Read Example Published-As-Vector Condition: {read_back_vector}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bf5cab8",
   "metadata": {},
   "source": [
    "## Batch Publishing Measurement Values\n",
    "\n",
    "The `publish_measurement_batch` method of `DataStoreClient` can similarly be used to publish the value of a given measurement across N parametric iterations at once. This usage of `publish_measurement_batch` is equivalent to calling `publish_measurement` for that same measurement N times.\n",
    "\n",
    "This is conceptually similar to the batch publishing of condition values. One important note, however, is that whereas conditions only support a given publish iteration containing a single scalar value, measurements support both **scalar** and **non-scalar** values.\n",
    "\n",
    "Examples of supported non-scalar types are `AnalogWaveform` and `Vector`. The process of batch publishing both scalar and non-scalar measurement values is similar, though as is the case for publishing scalar and non-scalar measurement values using the non-batched `publish_measurement` method, the process of later reading that measurement data from Measurement Data Services is slightly different between the two cases, as shown below.\n",
    "\n",
    "### Scalar Measurements\n",
    "\n",
    "Scalar measurement values may be supplied to `publish_measurement_batch` as either an `Iterable` or a `Vector`.\n",
    "\n",
    "Supported element types of the `Iterable` are `float`, `int`, `str`, and `bool`: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63c8e0b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "float_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example Float Measurement\",\n",
    "    values=[0.125, 0.25, 0.5, 1.0],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "integer_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example Integer Measurement\",\n",
    "    values=[10, 20, 30, 40],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "string_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example String Measurement\",\n",
    "    values=[\"nominal\", \"warning\", \"critical\", \"retest\"],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "bool_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example Bool Measurement\",\n",
    "    values=[False, False, True, True],\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "print(f\"Published Example Float Measurement IDs: {float_measurement_ids}\")\n",
    "print(f\"Published Example Integer Measurement IDs: {integer_measurement_ids}\")\n",
    "print(f\"Published Example String Measurement IDs: {string_measurement_ids}\")\n",
    "print(f\"Published Example Bool Measurement IDs: {bool_measurement_ids}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50daa8b9",
   "metadata": {},
   "source": [
    "Note that because these are scalar measurements, only a single measurement ID is present in the returned `Sequence` from each publish call. For non-scalar measurements, the `publish_measurement_batch` method returns a `Sequence` of N IDs, as we will see further below.\n",
    "\n",
    "Supplying a `Vector` allows the client to specify additional information, such as units:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0148ddd",
   "metadata": {},
   "outputs": [],
   "source": [
    "measurement_vector = Vector(values=[1.2, 1.4, 1.6, 1.8], units=\"Volts\")\n",
    "\n",
    "vector_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example Published-As-Vector Measurement\",\n",
    "    values=measurement_vector,\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "print(f\"Published Example Published-As-Vector Measurement IDs: {vector_measurement_ids}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2194f526",
   "metadata": {},
   "source": [
    "Published measurement values can be read back in the same manner as when reading back measurement values that were published individually via `publish_measurement`.\n",
    "\n",
    "More specifically, scalar measurement values published via `publish_measurement_batch` are read back as a `Vector` containing all N iterations of parametric data published for a particular measurement:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3514a41",
   "metadata": {},
   "outputs": [],
   "source": [
    "published_float_measurement = data_store_client.get_measurement(float_measurement_ids[0])\n",
    "published_integer_measurement = data_store_client.get_measurement(integer_measurement_ids[0])\n",
    "published_string_measurement = data_store_client.get_measurement(string_measurement_ids[0])\n",
    "published_bool_measurement = data_store_client.get_measurement(bool_measurement_ids[0])\n",
    "published_as_vector_measurement = data_store_client.get_measurement(vector_measurement_ids[0])\n",
    "\n",
    "read_back_float_measurement = data_store_client.read_measurement_value(published_float_measurement, expected_type=Vector)\n",
    "read_back_integer_measurement = data_store_client.read_measurement_value(published_integer_measurement, expected_type=Vector)\n",
    "read_back_string_measurement = data_store_client.read_measurement_value(published_string_measurement, expected_type=Vector)\n",
    "read_back_bool_measurement = data_store_client.read_measurement_value(published_bool_measurement, expected_type=Vector)\n",
    "read_back_vector_measurement = data_store_client.read_measurement_value(published_as_vector_measurement, expected_type=Vector)\n",
    "\n",
    "print(f\"Read Float Measurement: {read_back_float_measurement}\")\n",
    "print(f\"Read Integer Measurement: {read_back_integer_measurement}\")\n",
    "print(f\"Read String Measurement: {read_back_string_measurement}\")\n",
    "print(f\"Read Bool Measurement: {read_back_bool_measurement}\")\n",
    "print(f\"Read Published-As-Vector Measurement: {read_back_vector_measurement}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90d45ba7",
   "metadata": {},
   "source": [
    "### Non-Scalar Measurements\n",
    "\n",
    "Unlike condition values, a measurement value for a particular publish iteration may be non-scalar, such as an `AnalogWaveform` or `Vector`.\n",
    "\n",
    "To batch publish non-scalar values for a particular measurement, supply `publish_measurement_batch` with an `Iterable` containing N non-scalar elements. Each of the N elements in the `Iterable` will correspond to a single publish iteration. This is equivalent to calling the non-batched `publish_measurement` method N times for the measurement in question:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a9fa541",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import timezone\n",
    "import hightime as ht\n",
    "import numpy as np\n",
    "from nitypes.waveform import AnalogWaveform, Timing\n",
    "\n",
    "# Batch publish two AnalogWaveform (i.e., non-scalar) values for the Example AnalogWaveform Measurement.\n",
    "waveforms = [\n",
    "    AnalogWaveform(\n",
    "        sample_count=4,\n",
    "        raw_data=np.array([0.0, 0.25, 0.5, 0.75], dtype=np.float64),\n",
    "        timing=Timing.create_with_regular_interval(\n",
    "            ht.timedelta(seconds=1e-3),\n",
    "            ht.datetime.now(timezone.utc),\n",
    "        ),\n",
    "    ),\n",
    "    AnalogWaveform(\n",
    "        sample_count=4,\n",
    "        raw_data=np.array([1.0, 0.85, 0.65, 0.4], dtype=np.float64),\n",
    "        timing=Timing.create_with_regular_interval(\n",
    "            ht.timedelta(seconds=1e-3),\n",
    "            ht.datetime.now(timezone.utc),\n",
    "        ),\n",
    "    ),\n",
    "]\n",
    "\n",
    "waveform_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example AnalogWaveform Measurement\",\n",
    "    values=waveforms,\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "# Batch publish two Vector (i.e., non-scalar) values for the Example Vector Measurement.\n",
    "vector_measurements = [\n",
    "    Vector(values=[1.0, 1.25, 1.5], units=\"Volts\"),\n",
    "    Vector(values=[2.0, 2.25, 2.5], units=\"Volts\"),\n",
    "]\n",
    "\n",
    "vector_measurement_ids = data_store_client.publish_measurement_batch(\n",
    "    name=\"Example Vector Measurement\",\n",
    "    values=vector_measurements,\n",
    "    step_id=step_id,\n",
    " )\n",
    "\n",
    "print(f\"Published Example AnalogWaveform Measurement IDs: {waveform_measurement_ids}\")\n",
    "print(f\"Published Example Vector Measurement IDs: {vector_measurement_ids}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9ce1e23",
   "metadata": {},
   "source": [
    "Published non-scalar measurement values can be read back in the same manner as when reading back measurement values that were published individually via `publish_measurement`.\n",
    "\n",
    "More specifically, non-scalar measurement values published via `publish_measurement_batch` are read back **individually**, with each published value corresponding to a separate `PublishedMeasurement`.\n",
    "\n",
    "The `parametric_index` of each `PublishedMeasurement` indicates the publish iteration to which it corresponds:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4596e9a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "published_waveform_measurement_0 = data_store_client.get_measurement(waveform_measurement_ids[0])\n",
    "published_waveform_measurement_1 = data_store_client.get_measurement(waveform_measurement_ids[1])\n",
    "published_vector_measurement_0 = data_store_client.get_measurement(vector_measurement_ids[0])\n",
    "published_vector_measurement_1 = data_store_client.get_measurement(vector_measurement_ids[1])\n",
    "\n",
    "read_back_waveform_measurement_0 = data_store_client.read_measurement_value(published_waveform_measurement_0, expected_type=AnalogWaveform)\n",
    "read_back_waveform_measurement_1 = data_store_client.read_measurement_value(published_waveform_measurement_1, expected_type=AnalogWaveform)\n",
    "read_back_vector_measurement_0 = data_store_client.read_measurement_value(published_vector_measurement_0, expected_type=Vector)\n",
    "read_back_vector_measurement_1 = data_store_client.read_measurement_value(published_vector_measurement_1, expected_type=Vector)\n",
    "\n",
    "# The 'parametric_index' field of the PublishedMeasurement indicates\n",
    "# which publish iteration the non-scalar measurement value corresponds to.\n",
    "# In this example, we published two values for each (uniquely named) measurement,\n",
    "# so the PublishedMeasurement corresponding to the first publish for each measurement \n",
    "# has a 'parametric_index' of 0 and the PublishedMeasurement corresponding to the\n",
    "# second publish for each measurement has a 'parametric_index' of 1.\n",
    "print(\n",
    "    f\"{published_waveform_measurement_0.name} at Parametric Index \"\n",
    "    f\"{published_waveform_measurement_0.parametric_index}: \"\n",
    "    f\"{read_back_waveform_measurement_0.raw_data.tolist()}\"\n",
    " )\n",
    "print(\n",
    "    f\"{published_waveform_measurement_1.name} at Parametric Index \"\n",
    "    f\"{published_waveform_measurement_1.parametric_index}: \"\n",
    "    f\"{read_back_waveform_measurement_1.raw_data.tolist()}\"\n",
    " )\n",
    "\n",
    "print(\n",
    "    f\"{published_vector_measurement_0.name} at Parametric Index \"\n",
    "    f\"{published_vector_measurement_0.parametric_index}: \"\n",
    "    f\"{read_back_vector_measurement_0}\"\n",
    " )\n",
    "print(\n",
    "    f\"{published_vector_measurement_1.name} at Parametric Index \"\n",
    "    f\"{published_vector_measurement_1.parametric_index}: \"\n",
    "    f\"{read_back_vector_measurement_1}\"\n",
    " )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6492dcaf",
   "metadata": {},
   "source": [
    "## Clean-Up\n",
    "\n",
    "Close the `DataStoreClient` and tear down the example-specific context when done."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b80c18f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/query/publish_sample_data.ipynb sha256=8675aacf3801227eff5537cb78d1739a28915caec67fe813d734f9fb5f995697 bytes=25553 -->
## FILE: examples/notebooks/query/publish_sample_data.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/query/publish_sample_data.ipynb`
- sha256: `8675aacf3801227eff5537cb78d1739a28915caec67fe813d734f9fb5f995697`
- bytes: 25553

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2517286e",
   "metadata": {},
   "source": [
    "# Publish Sample Data for OData Query Examples\n",
    "\n",
    "This notebook creates structured sample data in the NI Measurement Data Store that will be used by the OData query example notebooks.\n",
    "\n",
    "**Run this notebook first** before using any of the query example notebooks:\n",
    "- `query_measurements.ipynb` - Demonstrates measurement and condition queries\n",
    "- `query_metadata.ipynb` - Demonstrates metadata queries (operators, hardware, UUTs, etc.)\n",
    "\n",
    "## What This Creates\n",
    "\n",
    "This notebook sets up a realistic test scenario with:\n",
    "- **3 TestResults**: 2 Power Supply tests and 1 Audio Amplifier test\n",
    "- **12 Test Steps**: Various measurement procedures across all tests\n",
    "- **38 Measurements**: Comprehensive scalar measurements (voltages, currents, power, THD, etc.)\n",
    "- **48 Test Conditions**: Environmental and setup parameters (temperature, humidity, supply conditions, etc.)\n",
    "- **Comprehensive Metadata**: 3 operators, 3 test stations, 2 hardware items, 2 UUTs, 3 UUT instances, 3 software items\n",
    "- **Aliases**: Human-readable references for all metadata entities"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71709c6e",
   "metadata": {},
   "source": [
    "## Prerequisites\n",
    "\n",
    "- NI Measurement Data Store running and accessible\n",
    "- Python environment with the `ni.datastore` package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c28ff0fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.metadata import (\n",
    "    MetadataStoreClient,\n",
    "    HardwareItem,\n",
    "    Operator,\n",
    "    SoftwareItem,\n",
    "    TestStation,\n",
    "    Uut,\n",
    "    UutInstance,\n",
    ")\n",
    "from ni.datastore.data import DataStoreClient\n",
    "\n",
    "# Create clients\n",
    "metadata_store_client = MetadataStoreClient()\n",
    "data_store_client = DataStoreClient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb11173f",
   "metadata": {},
   "source": [
    "## Create Metadata Entities\n",
    "\n",
    "Setting up the metadata for operators, test stations, hardware, etc. This is typically done once and establishes 'aliases' which are human-readable strings that can be used to refer to metadata later."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "658ae5b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create sample operators\n",
    "print(\"🚀 Starting sample data creation...\")\n",
    "print(\"📊 Creating comprehensive test metadata and measurements\")\n",
    "\n",
    "# Create sample operators\n",
    "print(\"\\n✅ Creating operators...\")\n",
    "operator1 = Operator(name=\"Alex Smith\", role=\"Test Engineer\")\n",
    "metadata_store_client.create_operator(operator1)\n",
    "ALIAS_OPERATOR_ALEX = \"Operator_Alex_Smith\"\n",
    "metadata_store_client.create_alias(ALIAS_OPERATOR_ALEX, operator1)\n",
    "\n",
    "operator2 = Operator(name=\"Jordan Chen\", role=\"Senior Test Engineer\")\n",
    "metadata_store_client.create_operator(operator2)\n",
    "ALIAS_OPERATOR_JORDAN = \"Operator_Jordan_Chen\"\n",
    "metadata_store_client.create_alias(ALIAS_OPERATOR_JORDAN, operator2)\n",
    "\n",
    "operator3 = Operator(name=\"Taylor Johnson\", role=\"Lab Technician\")\n",
    "metadata_store_client.create_operator(operator3)\n",
    "ALIAS_OPERATOR_TAYLOR = \"Operator_Taylor_Johnson\"\n",
    "metadata_store_client.create_alias(ALIAS_OPERATOR_TAYLOR, operator3)\n",
    "\n",
    "# Create sample test stations\n",
    "print(\"\\n✅ Creating test stations...\")\n",
    "station1 = TestStation(name=\"TestStation_A1\")\n",
    "metadata_store_client.create_test_station(station1)\n",
    "ALIAS_STATION_A1 = \"Station_A1\"\n",
    "metadata_store_client.create_alias(ALIAS_STATION_A1, station1)\n",
    "\n",
    "station2 = TestStation(name=\"TestStation_B2\")\n",
    "metadata_store_client.create_test_station(station2)\n",
    "ALIAS_STATION_B2 = \"Station_B2\"\n",
    "metadata_store_client.create_alias(ALIAS_STATION_B2, station2)\n",
    "\n",
    "station3 = TestStation(name=\"TestStation_C3\")\n",
    "metadata_store_client.create_test_station(station3)\n",
    "ALIAS_STATION_C3 = \"Station_C3\"\n",
    "metadata_store_client.create_alias(ALIAS_STATION_C3, station3)\n",
    "\n",
    "# Create sample hardware items (test equipment)\n",
    "print(\"\\n✅ Creating hardware items...\")\n",
    "dmm = HardwareItem(manufacturer=\"NI\", model=\"PXIe-4081\", serial_number=\"DMM001\")\n",
    "metadata_store_client.create_hardware_item(dmm)\n",
    "ALIAS_DMM = \"DMM_PXIe4081\"\n",
    "metadata_store_client.create_alias(ALIAS_DMM, dmm)\n",
    "\n",
    "scope = HardwareItem(manufacturer=\"NI\", model=\"PXIe-5171\", serial_number=\"SCOPE001\")\n",
    "metadata_store_client.create_hardware_item(scope)\n",
    "ALIAS_SCOPE = \"Scope_PXIe5171\"\n",
    "metadata_store_client.create_alias(ALIAS_SCOPE, scope)\n",
    "\n",
    "# Create sample UUTs (Units Under Test - product definitions)\n",
    "print(\"\\n✅ Creating UUTs...\")\n",
    "power_supply_uut = Uut(model_name=\"PowerSupply v2.1\", family=\"Power\")\n",
    "metadata_store_client.create_uut(power_supply_uut)\n",
    "ALIAS_UUT_POWER_SUPPLY = \"UUT_PowerSupply_v2_1\"\n",
    "metadata_store_client.create_alias(ALIAS_UUT_POWER_SUPPLY, power_supply_uut)\n",
    "\n",
    "amplifier_uut = Uut(model_name=\"Audio Amplifier v1.3\", family=\"Audio\")\n",
    "metadata_store_client.create_uut(amplifier_uut)\n",
    "ALIAS_UUT_AMPLIFIER = \"UUT_AudioAmplifier_v1_3\"\n",
    "metadata_store_client.create_alias(ALIAS_UUT_AMPLIFIER, amplifier_uut)\n",
    "\n",
    "# Create sample software items\n",
    "print(\"\\n✅ Creating software items...\")\n",
    "python_env = SoftwareItem(product=\"Python\", version=\"3.11.5\")\n",
    "metadata_store_client.create_software_item(python_env)\n",
    "ALIAS_SOFTWARE_PYTHON = \"Software_Python_3_11_5\"\n",
    "metadata_store_client.create_alias(ALIAS_SOFTWARE_PYTHON, python_env)\n",
    "\n",
    "pytest_env = SoftwareItem(product=\"pytest\", version=\"7.4.0\")\n",
    "metadata_store_client.create_software_item(pytest_env)\n",
    "ALIAS_SOFTWARE_PYTEST = \"Software_pytest_7_4_0\"\n",
    "metadata_store_client.create_alias(ALIAS_SOFTWARE_PYTEST, pytest_env)\n",
    "\n",
    "nidaq_env = SoftwareItem(product=\"NI-DAQmx\", version=\"23.3.0\")\n",
    "metadata_store_client.create_software_item(nidaq_env)\n",
    "ALIAS_SOFTWARE_NIDAQ = \"Software_NI_DAQmx_23_3_0\"\n",
    "metadata_store_client.create_alias(ALIAS_SOFTWARE_NIDAQ, nidaq_env)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9436338",
   "metadata": {},
   "source": [
    "## Create UUT Instances and Software Item Metadata\n",
    "\n",
    "This setup is done for each test run. Each time we're going to run a test, we create instances of the specific UUT we are testing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fec522e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create sample UUT instances (individual devices with serial numbers)\n",
    "print(\"\\n✅ Creating UUT instances...\")\n",
    "ps_instance1 = UutInstance(uut_id=ALIAS_UUT_POWER_SUPPLY, serial_number=\"PS-2024-001\")\n",
    "metadata_store_client.create_uut_instance(ps_instance1)\n",
    "ALIAS_UUT_INSTANCE_PS1 = \"UUT_Instance_PS_001\"\n",
    "metadata_store_client.create_alias(ALIAS_UUT_INSTANCE_PS1, ps_instance1)\n",
    "\n",
    "ps_instance2 = UutInstance(uut_id=ALIAS_UUT_POWER_SUPPLY, serial_number=\"PS-2024-002\")\n",
    "metadata_store_client.create_uut_instance(ps_instance2)\n",
    "ALIAS_UUT_INSTANCE_PS2 = \"UUT_Instance_PS_002\"\n",
    "metadata_store_client.create_alias(ALIAS_UUT_INSTANCE_PS2, ps_instance2)\n",
    "\n",
    "amp_instance1 = UutInstance(uut_id=ALIAS_UUT_AMPLIFIER, serial_number=\"AMP-2024-001\")\n",
    "metadata_store_client.create_uut_instance(amp_instance1)\n",
    "ALIAS_UUT_INSTANCE_AMP1 = \"UUT_Instance_AMP_001\"\n",
    "metadata_store_client.create_alias(ALIAS_UUT_INSTANCE_AMP1, amp_instance1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f0a9f2d",
   "metadata": {},
   "source": [
    "## Create Test Results and Publish\n",
    "\n",
    "Create the individual test results and steps that will contain our measurements and conditions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a14d6ca4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "from ni.datastore.data import Outcome\n",
    "\n",
    "# Create comprehensive test scenarios with realistic measurements\n",
    "print(\"\\n🔬 Creating sample test results with measurements...\")\n",
    "\n",
    "# Scenario 1: Power Supply Test\n",
    "print(\"📋 Creating Power Supply test...\")\n",
    "from ni.datastore.data import TestResult, Step\n",
    "\n",
    "# Use aliases instead of IDs for better readability and maintenance\n",
    "power_test_result = TestResult(\n",
    "    name=\"Power Supply Test v2.1\",\n",
    "    uut_instance_id=ALIAS_UUT_INSTANCE_PS1,\n",
    "    operator_id=ALIAS_OPERATOR_ALEX,\n",
    "    test_station_id=ALIAS_STATION_A1,\n",
    "    software_item_ids=[ALIAS_SOFTWARE_PYTHON],\n",
    "    hardware_item_ids=[ALIAS_DMM, ALIAS_SCOPE],\n",
    ")\n",
    "ps_test_result_id = data_store_client.create_test_result(power_test_result)\n",
    "\n",
    "# Power Supply Test Steps\n",
    "power_steps = [\n",
    "    (\"Initialize\", [\"Configure DMM\", \"Set Load Conditions\", \"Warm-up Period\"]),\n",
    "    (\"Input Voltage Test\", [\"Measure Input Voltage\", \"Measure Input Current\", \"Calculate Input Power\"]),\n",
    "    (\"Output Voltage Test\", [\"Measure 5V Rail\", \"Measure 12V Rail\", \"Measure -12V Rail\"]),\n",
    "    (\"Load Regulation\", [\"No Load Test\", \"25% Load Test\", \"50% Load Test\", \"75% Load Test\", \"Full Load Test\"]),\n",
    "    (\"Ripple Measurement\", [\"5V Ripple\", \"12V Ripple\", \"-12V Ripple\"])\n",
    "]\n",
    "\n",
    "power_step_objects = []\n",
    "for step_name, measurement_names in power_steps:\n",
    "    step = Step(name=step_name, test_result_id=ps_test_result_id)\n",
    "    step_id = data_store_client.create_step(step)\n",
    "    power_step_objects.append((step_id, measurement_names))\n",
    "\n",
    "# Create measurements for each step\n",
    "from nitypes.scalar import Scalar\n",
    "total_measurements = 0\n",
    "power_conditions = 0\n",
    "for step_id, measurement_names in power_step_objects:\n",
    "    for measurement_name in measurement_names:\n",
    "        # Generate realistic measurement values based on measurement type\n",
    "        if \"Voltage\" in measurement_name:\n",
    "            if \"Input\" in measurement_name:\n",
    "                value = random.uniform(115, 125)  # Input voltage ~120V\n",
    "                unit = \"V\"\n",
    "            elif \"5V\" in measurement_name:\n",
    "                value = random.uniform(4.95, 5.05)  # 5V rail\n",
    "                unit = \"V\"\n",
    "            elif \"12V\" in measurement_name:\n",
    "                value = random.uniform(11.8, 12.2)  # 12V rail\n",
    "                unit = \"V\"\n",
    "            elif \"-12V\" in measurement_name:\n",
    "                value = random.uniform(-12.2, -11.8)  # -12V rail\n",
    "                unit = \"V\"\n",
    "            else:\n",
    "                value = random.uniform(0, 15)\n",
    "                unit = \"V\"\n",
    "        elif \"Current\" in measurement_name:\n",
    "            if \"Input\" in measurement_name:\n",
    "                value = random.uniform(0.8, 1.2)  # Input current\n",
    "            else:\n",
    "                value = random.uniform(0.1, 2.0)  # Various currents\n",
    "            unit = \"A\"\n",
    "        elif \"Power\" in measurement_name:\n",
    "            value = random.uniform(50, 150)  # Power measurements\n",
    "            unit = \"W\"\n",
    "        elif \"Ripple\" in measurement_name:\n",
    "            value = random.uniform(10, 50)  # Ripple in mV\n",
    "            unit = \"mV\"\n",
    "        else:\n",
    "            value = random.uniform(0, 100)\n",
    "            unit = \"\"\n",
    "        \n",
    "        # Publish measurement using Scalar values\n",
    "        # Insert some random failures\n",
    "        random_number = random.random()\n",
    "        outcome = Outcome.PASSED if random_number > 0.4 else Outcome.FAILED\n",
    "        data_store_client.publish_measurement(measurement_name, Scalar(value, unit), step_id, outcome=outcome)\n",
    "        print (f\"  🧪 Created measurement '{measurement_name}' - {'✅ Passed' if outcome == Outcome.PASSED else '❌ Failed'}\")\n",
    "        total_measurements += 1\n",
    "    \n",
    "    # Add test conditions for each power supply step\n",
    "    step_conditions = [\n",
    "        (\"Ambient Temperature\", random.uniform(21, 26), \"°C\"),\n",
    "        (\"Barometric Pressure\", random.uniform(995, 1015), \"hPa\"),\n",
    "        (\"Line Frequency\", random.uniform(59.9, 60.1), \"Hz\"),\n",
    "        (\"Calibration Date\", \"2024-03-15\", \"\"),  # String condition\n",
    "        (\"Test Fixture\", \"PS-TEST-001\", \"\")  # String condition\n",
    "    ]\n",
    "    \n",
    "    for condition_name, value, unit in step_conditions:\n",
    "        if isinstance(value, str):\n",
    "            # For string conditions, we might need a different method\n",
    "            # For now, let's skip string conditions and focus on numeric ones\n",
    "            continue\n",
    "        data_store_client.publish_condition(condition_name, \"Environment\", Scalar(value, unit), step_id)\n",
    "        power_conditions += 1\n",
    "\n",
    "print(f\"  📊 Created {total_measurements} measurements for Power Supply test\")\n",
    "print(f\"  🌡️ Created {power_conditions} conditions for Power Supply test\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "143910f1",
   "metadata": {},
   "source": [
    "## Publish Measurements and Conditions\n",
    "\n",
    "Create sample measurements with different data types including scalar values, waveforms, and test conditions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e51f538",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scenario 2: Audio Amplifier Test\n",
    "print(\"\\n📋 Creating Audio Amplifier test...\")\n",
    "amplifier_test_result = TestResult(\n",
    "    name=\"Audio Amplifier Test v1.3\",\n",
    "    uut_instance_id=ALIAS_UUT_INSTANCE_AMP1,\n",
    "    operator_id=ALIAS_OPERATOR_JORDAN,\n",
    "    test_station_id=ALIAS_STATION_B2,\n",
    "    software_item_ids=[ALIAS_SOFTWARE_PYTHON],\n",
    "    hardware_item_ids=[ALIAS_DMM, ALIAS_SCOPE],\n",
    ")\n",
    "amp_test_result_id = data_store_client.create_test_result(amplifier_test_result)\n",
    "\n",
    "# Audio Amplifier Test Steps\n",
    "amplifier_steps = [\n",
    "    (\"Power-On Test\", [\"Supply Voltage\", \"Standby Current\", \"Enable Signal\"]),\n",
    "    (\"DC Offset\", [\"Left Channel DC Offset\", \"Right Channel DC Offset\"]),\n",
    "    (\"Frequency Response\", [\"20Hz Response\", \"1kHz Response\", \"10kHz Response\", \"20kHz Response\"]),\n",
    "    (\"THD+N Test\", [\"1kHz THD+N Left\", \"1kHz THD+N Right\", \"10kHz THD+N Left\", \"10kHz THD+N Right\"]),\n",
    "    (\"Power Output\", [\"Max Power Left\", \"Max Power Right\", \"Power at 1% THD\"]),\n",
    "    (\"Signal-to-Noise\", [\"SNR Left Channel\", \"SNR Right Channel\"])\n",
    "]\n",
    "\n",
    "amplifier_step_objects = []\n",
    "for step_name, measurement_names in amplifier_steps:\n",
    "    step = Step(name=step_name, test_result_id=amp_test_result_id)\n",
    "    step_id = data_store_client.create_step(step)\n",
    "    amplifier_step_objects.append((step_id, measurement_names))\n",
    "\n",
    "# Create measurements for amplifier test\n",
    "amplifier_measurements = 0\n",
    "for step_id, measurement_names in amplifier_step_objects:\n",
    "    for measurement_name in measurement_names:\n",
    "        # Generate realistic measurement values for audio amplifier\n",
    "        if \"Voltage\" in measurement_name or \"Supply\" in measurement_name:\n",
    "            value = random.uniform(14.5, 15.5)  # Supply voltage\n",
    "            unit = \"V\"\n",
    "        elif \"Current\" in measurement_name:\n",
    "            value = random.uniform(0.01, 0.05)  # Standby current\n",
    "            unit = \"A\"\n",
    "        elif \"DC Offset\" in measurement_name:\n",
    "            value = random.uniform(-5, 5)  # DC offset in mV\n",
    "            unit = \"mV\"\n",
    "        elif \"Response\" in measurement_name:\n",
    "            value = random.uniform(-1, 1)  # Frequency response in dB\n",
    "            unit = \"dB\"\n",
    "        elif \"THD\" in measurement_name:\n",
    "            value = random.uniform(0.001, 0.01)  # THD+N percentage\n",
    "            unit = \"%\"\n",
    "        elif \"Power\" in measurement_name:\n",
    "            if \"Max\" in measurement_name:\n",
    "                value = random.uniform(45, 55)  # Max power\n",
    "            else:\n",
    "                value = random.uniform(40, 50)  # Power at 1% THD\n",
    "            unit = \"W\"\n",
    "        elif \"SNR\" in measurement_name:\n",
    "            value = random.uniform(95, 105)  # Signal-to-noise ratio\n",
    "            unit = \"dB\"\n",
    "        else:\n",
    "            value = random.uniform(0, 10)\n",
    "            unit = \"\"\n",
    "        \n",
    "        # Publish measurement using Scalar values\n",
    "        random_number = random.random()\n",
    "        outcome = Outcome.PASSED if random_number > 0.4 else Outcome.FAILED\n",
    "        data_store_client.publish_measurement(measurement_name, Scalar(value, unit), step_id, outcome=outcome)\n",
    "        amplifier_measurements += 1\n",
    "\n",
    "# Add published conditions for the amplifier test\n",
    "print(\"  🌡️ Adding test conditions for Audio Amplifier test...\")\n",
    "amplifier_conditions = 0\n",
    "for step_id, _ in amplifier_step_objects:\n",
    "    # Add environmental conditions for each step\n",
    "    conditions = [\n",
    "        (\"Ambient Temperature\", random.uniform(22, 25), \"°C\"),\n",
    "        (\"Relative Humidity\", random.uniform(45, 55), \"%\"),\n",
    "        (\"Test Load\", random.uniform(7.8, 8.2), \"Ω\")\n",
    "    ]\n",
    "    \n",
    "    for condition_name, value, unit in conditions:\n",
    "        data_store_client.publish_condition(condition_name, \"Environment\", Scalar(value, unit), step_id)\n",
    "        amplifier_conditions += 1\n",
    "\n",
    "print(f\"  📊 Created {amplifier_measurements} measurements for Audio Amplifier test\")\n",
    "print(f\"  🌡️ Created {amplifier_conditions} conditions for Audio Amplifier test\")\n",
    "\n",
    "# Scenario 3: Additional Power Supply Test (second unit)\n",
    "print(\"\\n📋 Creating second Power Supply test...\")\n",
    "power_test_2 = TestResult(\n",
    "    name=\"Power Supply Test v2.1\",\n",
    "    uut_instance_id=ALIAS_UUT_INSTANCE_PS2,  # Second power supply unit\n",
    "    operator_id=ALIAS_OPERATOR_TAYLOR,\n",
    "    test_station_id=ALIAS_STATION_C3,\n",
    "    software_item_ids=[ALIAS_SOFTWARE_PYTHON],\n",
    "    hardware_item_ids=[ALIAS_DMM, ALIAS_SCOPE],\n",
    ")\n",
    "ps_test_2_result_id = data_store_client.create_test_result(power_test_2)\n",
    "\n",
    "# Create a shorter test for the second power supply (quick verification)\n",
    "quick_steps = [\n",
    "    (\"Quick Verification\", [\"Output 5V\", \"Output 12V\", \"Load Current\"])\n",
    "]\n",
    "\n",
    "power_test_2_conditions = 0\n",
    "for step_name, measurement_names in quick_steps:\n",
    "    step = Step(name=step_name, test_result_id=ps_test_2_result_id)\n",
    "    step_id = data_store_client.create_step(step)\n",
    "    \n",
    "    for measurement_name in measurement_names:\n",
    "        if \"5V\" in measurement_name:\n",
    "            value = random.uniform(4.95, 5.05)\n",
    "            unit = \"V\"\n",
    "        elif \"12V\" in measurement_name:\n",
    "            value = random.uniform(11.8, 12.2)\n",
    "            unit = \"V\"\n",
    "        elif \"Current\" in measurement_name:\n",
    "            value = random.uniform(0.5, 1.5)\n",
    "            unit = \"A\"\n",
    "        else:\n",
    "            value = random.uniform(0, 10)\n",
    "            unit = \"\"\n",
    "            \n",
    "        # Publish measurement using Scalar values\n",
    "        random_number = random.random()\n",
    "        outcome = Outcome.PASSED if random_number > 0.4 else Outcome.FAILED\n",
    "        data_store_client.publish_measurement(measurement_name, Scalar(value, unit), step_id, outcome=outcome)\n",
    "    \n",
    "    # Add test conditions for the quick verification\n",
    "    print(\"  🌡️ Adding test conditions for second Power Supply test...\")\n",
    "    quick_conditions = [\n",
    "        (\"Room Temperature\", random.uniform(20, 24), \"°C\"),\n",
    "        # (\"Input Voltage\", random.uniform(118, 122), \"V\"),\n",
    "        # (\"Input Frequency\", random.uniform(59.8, 60.2), \"Hz\"),\n",
    "        # (\"Load Resistance\", random.uniform(9.8, 10.2), \"Ω\")\n",
    "    ]\n",
    "    \n",
    "    for condition_name, value, unit in quick_conditions:\n",
    "        data_store_client.publish_condition(condition_name, \"Environment\", Scalar(value, unit), step_id)\n",
    "        power_test_2_conditions += 1\n",
    "\n",
    "print(\"  📊 Created 3 measurements for second Power Supply test\")\n",
    "print(f\"  🌡️ Created {power_test_2_conditions} conditions for second Power Supply test\")\n",
    "\n",
    "# Summary\n",
    "total_tests = 3\n",
    "total_steps = len(power_step_objects) + len(amplifier_step_objects) + 1\n",
    "total_measurements_created = total_measurements + amplifier_measurements + 3\n",
    "total_conditions_created = amplifier_conditions + power_test_2_conditions\n",
    "\n",
    "print(f\"\\n🎯 Sample data creation complete!\")\n",
    "print(f\"📊 Summary:\")\n",
    "print(f\"  - Test Results: {total_tests}\")\n",
    "print(f\"  - Steps: {total_steps}\")\n",
    "print(f\"  - Measurements: {total_measurements_created}\")\n",
    "print(f\"  - Conditions: {total_conditions_created}\")\n",
    "\n",
    "print(f\"\\n✅ Ready to run query notebooks!\")\n",
    "print(f\"   📓 Next: query_metadata.ipynb - Query operators, stations, hardware, etc.\")\n",
    "print(f\"   📓 Then: query_measurements.ipynb - Query test results and measurements\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dd49a41",
   "metadata": {},
   "source": [
    "## Clean up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "636a5c4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_store_client.close()\n",
    "metadata_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ecc3a180",
   "metadata": {},
   "source": [
    "## Summary\n",
    "\n",
    "✅ **Sample data has been successfully created!**\n",
    "\n",
    "You can now run the other OData query example notebooks:\n",
    "- **`query_measurements.ipynb`** - Learn how to query measurements, conditions, and test data\n",
    "- **`query_metadata.ipynb`** - Learn how to query operators, hardware, UUTs, and other metadata\n",
    "\n",
    "The data represents a realistic test scenario using NI PXIe instruments to test power supply and audio amplifier products."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/query/query_measurements.ipynb sha256=1460099966111aa34424a2e368fe786540fd0c846f38293120b34443e2ca4600 bytes=9383 -->
## FILE: examples/notebooks/query/query_measurements.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/query/query_measurements.ipynb`
- sha256: `1460099966111aa34424a2e368fe786540fd0c846f38293120b34443e2ca4600`
- bytes: 9383

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "341789ca",
   "metadata": {},
   "source": [
    "# OData Measurement and Test Result Queries with Digital Thread Services\n",
    "\n",
    "This notebook demonstrates how to use OData queries to retrieve and analyze test measurements, results, and conditions from the NI Measurement Data Store. It shows hierarchical navigation through TestResults → Steps → Measurements.\n",
    "\n",
    "## Prerequisites\n",
    "\n",
    "**⚠️ Important:** Run the `publish_sample_data.ipynb` notebook first to create the sample test data that this notebook queries.\n",
    "\n",
    "- NI Measurement Data Store running and accessible\n",
    "- Python environment with the `ni.datastore` package\n",
    "- Sample test data created by running `publish_sample_data.ipynb`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5556fa1e",
   "metadata": {},
   "source": [
    "## Setup\n",
    "\n",
    "Import the required libraries and create both metadata and data store clients."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c34ac09",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.data import DataStoreClient\n",
    "\n",
    "data_store_client = DataStoreClient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87c65e48",
   "metadata": {},
   "source": [
    "## Query Measurements\n",
    "\n",
    "Measurements are the individual data points collected during test steps.\n",
    "\n",
    "**Additional measurement query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by measurement name\n",
    "voltage_measurements = data_store_client.query_measurements(\"$filter=contains(Name,'Voltage')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e981dfd0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ni.datastore.data import Outcome\n",
    "from ni.datastore.metadata import MetadataStoreClient\n",
    "\n",
    "# Find failed measurements by checking outcome\n",
    "print(\"\\n1. Failed Measurements:\")\n",
    "failed_measurements = data_store_client.query_measurements(\"\")\n",
    "for measurement in failed_measurements:\n",
    "    print(f\"*** data type: {measurement.value_type}\")\n",
    "    measurement_name = measurement.name or \"Unnamed Measurement\"\n",
    "    if measurement.start_date_time:\n",
    "        print(f\"  ❌ {measurement_name} - Failed at {measurement.start_date_time.strftime('%Y-%m-%d %H:%M:%S')}\")\n",
    "    else:\n",
    "        print(f\"  ❌ {measurement_name} - Failed at Unknown Time\")\n",
    "\n",
    "if not failed_measurements:\n",
    "    print(\"  ✅ No failed measurements found!\")\n",
    "\n",
    "if len(failed_measurements) > 15:\n",
    "    print(f\"  ... and {len(failed_measurements) - 15} more measurements\")\n",
    "\n",
    "def print_measurement_with_outcome(measurement) -> str:\n",
    "    name = measurement.name or \"Unnamed Measurement\"\n",
    "    passed = measurement.outcome == Outcome.PASSED\n",
    "    failed = measurement.outcome == Outcome.FAILED\n",
    "    return f\"{name} - {'✅ (Passed)' if passed else '❌ (Failed)' if failed else '❓ (Unknown)'}\"\n",
    "\n",
    "print(\"\\n=== Voltage Measurements ===\")\n",
    "voltage_measurements = data_store_client.query_measurements(\"$filter=contains(Name,'Voltage')\")\n",
    "for measurement in voltage_measurements:\n",
    "    print(f\"  ⚡ {print_measurement_with_outcome(measurement)}\")\n",
    "\n",
    "print(\"\\n=== Current Measurements ===\")\n",
    "current_measurements = data_store_client.query_measurements(\"$filter=contains(Name,'Current')\")\n",
    "for measurement in current_measurements:\n",
    "    print(f\"  🔌 {print_measurement_with_outcome(measurement)}\")\n",
    "\n",
    "print(\"\\n=== Failed Measurements by Operator Alex Smith ===\")\n",
    "metadata_store_client = MetadataStoreClient()\n",
    "for measurement in failed_measurements:\n",
    "    if measurement.test_result_id:\n",
    "        test_result = data_store_client.get_test_result(measurement.test_result_id)\n",
    "        if test_result.operator_id:\n",
    "            operator = metadata_store_client.get_operator(test_result.operator_id)\n",
    "            operator_name = operator.name\n",
    "            if operator_name == \"Alex Smith\":\n",
    "                print(f\"  📋 {print_measurement_with_outcome(measurement)} - Operator: {operator_name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92115861",
   "metadata": {},
   "source": [
    "## Query Steps\n",
    "\n",
    "Steps are the individual test phases within a test result. Each step can contain multiple measurements.\n",
    "\n",
    "**Additional step query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by step name\n",
    "initialization_steps = data_store_client.query_steps(\"$filter=contains(Name,'Initialize')\")\n",
    "measurement_steps = data_store_client.query_steps(\"$filter=contains(Name,'Measure')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fa79b50",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Query all steps\n",
    "all_steps = list(data_store_client.query_steps(\"\"))\n",
    "\n",
    "print(f\"Found {len(all_steps)} steps total\")\n",
    "print(\"\\nStep summary:\")\n",
    "for step in all_steps[:10]:  # Show first 10 steps\n",
    "    step_name = step.name or \"Unnamed Step\"\n",
    "    # Steps don't have a status field, so we'll skip showing status\n",
    "    print(f\"  🔧 {step_name}\")\n",
    "\n",
    "if len(all_steps) > 10:\n",
    "    print(f\"  ... and {len(all_steps) - 10} more steps\")\n",
    "\n",
    "print(\"\\n=== Steps containing 'Voltage' ===\")\n",
    "voltage_steps = list(data_store_client.query_steps(\"$filter=contains(Name,'Voltage')\"))\n",
    "for step in voltage_steps:\n",
    "    step_name = step.name or \"Unnamed Step\"\n",
    "    # Steps don't have a status field, so we'll skip showing status\n",
    "    print(f\"  🔧 {step_name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02cd81bc",
   "metadata": {},
   "source": [
    "## Query Published Conditions\n",
    "\n",
    "Published conditions represent test conditions or environmental factors during testing.\n",
    "\n",
    "**Additional condition query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by condition name\n",
    "temperature_conditions = data_store_client.query_conditions(\"$filter=contains(Name,'Temperature')\")\n",
    "humidity_conditions = data_store_client.query_conditions(\"$filter=contains(Name,'Humidity')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edfc2fce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Query all published conditions\n",
    "# Query conditions with name including 'Temperature' or 'Pressure'\n",
    "temp_and_pressure_conditions = list(data_store_client.query_conditions(\"$filter=contains(Name,'Temperature') or contains(Name,'Pressure')\"))\n",
    "\n",
    "# Get unique condition names and sort them\n",
    "unique_condition_names = sorted(set(\n",
    "    condition.name if hasattr(condition, 'name') else \"Unnamed Condition\"\n",
    "    for condition in temp_and_pressure_conditions\n",
    "))\n",
    "\n",
    "if temp_and_pressure_conditions:\n",
    "    print(\"\\nConditions related to temp and pressure:\")\n",
    "    for condition_name in unique_condition_names[:10]:  # Show first 10 conditions\n",
    "        name = condition_name\n",
    "        print(f\"  🌡️ {name}\")\n",
    "        \n",
    "    if len(temp_and_pressure_conditions) > 10:\n",
    "        print(f\"  ... and {len(temp_and_pressure_conditions) - 10} more conditions\")\n",
    "else:\n",
    "    print(\"No published conditions found in the sample data\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb446f20",
   "metadata": {},
   "source": [
    "## Clean up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34246e8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ni-datastore-py3.10",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/query/query_metadata.ipynb sha256=6dbf27dfe9fbfb43635cfeaaba0c0737e35e1f8d75f1f30b45f08a4c37f79626 bytes=16649 -->
## FILE: examples/notebooks/query/query_metadata.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/query/query_metadata.ipynb`
- sha256: `6dbf27dfe9fbfb43635cfeaaba0c0737e35e1f8d75f1f30b45f08a4c37f79626`
- bytes: 16649

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9c562433",
   "metadata": {},
   "source": [
    "# OData Metadata Queries with Digital Thread Services\n",
    "\n",
    "This notebook demonstrates how to use OData queries to retrieve and filter metadata from the NI Measurement Data Store. Metadata includes operators, test stations, hardware items, UUTs, software items, and aliases.\n",
    "\n",
    "## Prerequisites\n",
    "\n",
    "**⚠️ Important:** Run the `publish_sample_data.ipynb` notebook first to create the sample metadata that this notebook queries.\n",
    "\n",
    "- NI Measurement Data Store running and accessible\n",
    "- Python environment with the `ni.datastore` package\n",
    "- Sample metadata created by running `publish_sample_data.ipynb`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59944076",
   "metadata": {},
   "source": [
    "## Setup\n",
    "\n",
    "Import the required libraries and create the metadata store client."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34089e87",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.metadata import MetadataStoreClient\n",
    "\n",
    "metadata_store_client = MetadataStoreClient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4da766ee",
   "metadata": {},
   "source": [
    "## Query Operators\n",
    "\n",
    "Uses `query_operators` to retrieve the operators. It also shows how to filter operators by name.\n",
    "\n",
    "**Additional operator query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by exact operator name\n",
    "operators_exact = metadata_store_client.query_operators(\"$filter=Name eq 'Alex Smith'\")\n",
    "\n",
    "# Filter by operator role\n",
    "operators_by_role = metadata_store_client.query_operators(\"$filter=Role eq 'Test Engineer'\")\n",
    "\n",
    "# Filter by name starting with text\n",
    "operators_name_starts = metadata_store_client.query_operators(\"$filter=startswith(Name,'Alex')\")\n",
    "\n",
    "# Filter by name ending with text\n",
    "operators_name_ends = metadata_store_client.query_operators(\"$filter=endswith(Name,'Smith')\")\n",
    "\n",
    "# Combine multiple conditions with 'and'\n",
    "operators_combined = metadata_store_client.query_operators(\"$filter=contains(Name,'Alex') and Role eq 'Test Engineer'\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a56f513",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\nFiltered operators (by name containing 'Smith'):\")\n",
    "operators_named_smith = metadata_store_client.query_operators(\"$filter=contains(Name,'Smith')\")\n",
    "for operator in operators_named_smith:\n",
    "    print(f\"  {operator.name} ({operator.role})\")\n",
    "\n",
    "print(\"\\nFiltered operators (by role containing 'Test Engineer'):\")\n",
    "test_engineer_operators = metadata_store_client.query_operators(\"$filter=contains(Role,'Test Engineer')\")\n",
    "for operator in test_engineer_operators:\n",
    "    print(f\"  {operator.name} ({operator.role})\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45533432",
   "metadata": {},
   "source": [
    "## Query Test Stations\n",
    "\n",
    "Uses `query_test_stations` to retrieve the test stations. It also shows how to filter test stations by name.\n",
    "\n",
    "**Additional test station query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by name ending with text\n",
    "stations_name_ends = metadata_store_client.query_test_stations(\"$filter=endswith(Name,'A1')\")\n",
    "\n",
    "# Combine multiple conditions with 'and'\n",
    "stations_combined = metadata_store_client.query_test_stations(\"$filter=contains(Name,'Test') and contains(Name,'A1')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64eea755",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Test stations whose name includes 'A1'\n",
    "print(\"\\nFiltered test stations (by name containing 'A1'):\")\n",
    "a1_test_stations = metadata_store_client.query_test_stations(\"$filter=contains(Name,'A1')\")\n",
    "for station in a1_test_stations:\n",
    "    print(f\"  {station.name}\")\n",
    "\n",
    "# Test stations named exactly 'TestStation_B2'\n",
    "print(\"\\nFiltered test stations (by name exactly 'TestStation_B2'):\")\n",
    "exact_b2_test_stations = metadata_store_client.query_test_stations(\"$filter=Name eq 'TestStation_B2'\")\n",
    "for station in exact_b2_test_stations:\n",
    "    print(f\"  {station.name}\")\n",
    "\n",
    "# Test stations whose name starts with 'Test'\n",
    "print(\"\\nFiltered test stations (by name starting with 'Test'):\")\n",
    "starts_test_stations = metadata_store_client.query_test_stations(\"$filter=startswith(Name,'Test')\")\n",
    "for station in starts_test_stations:\n",
    "    print(f\"  {station.name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b687e453",
   "metadata": {},
   "source": [
    "## Query Hardware Items\n",
    "\n",
    "Uses `query_hardware_items` to retrieve the hardware items (test equipment). It also shows how to filter hardware items by various properties like manufacturer, model, and serial number.\n",
    "\n",
    "**Additional hardware item query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by manufacturer containing text\n",
    "hardware_manufacturer_contains = metadata_store_client.query_hardware_items(\"$filter=contains(Manufacturer,'NI')\")\n",
    "\n",
    "# Filter by model starting with text\n",
    "hardware_model_starts = metadata_store_client.query_hardware_items(\"$filter=startswith(Model,'PXIe')\")\n",
    "\n",
    "# Filter by part number (if available)\n",
    "hardware_by_part = metadata_store_client.query_hardware_items(\"$filter=PartNumber eq 'DMM-001-XYZ'\")\n",
    "\n",
    "# Combine multiple conditions - find NI PXIe instruments\n",
    "hardware_combined = metadata_store_client.query_hardware_items(\"$filter=Manufacturer eq 'NI' and contains(Model,'PXIe')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "114fe8ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Filtered hardware items (by manufacturer 'NI'):\")\n",
    "filtered_hardware = metadata_store_client.query_hardware_items(\"$filter=Manufacturer eq 'NI'\")\n",
    "for item in filtered_hardware:\n",
    "    print(f\"  {item.manufacturer} {item.model} (S/N: {item.serial_number})\")\n",
    "\n",
    "print(\"\\nFiltered hardware items (by model containing '4081'):\")\n",
    "model_filtered = metadata_store_client.query_hardware_items(\"$filter=contains(Model,'4081')\")\n",
    "for item in model_filtered:\n",
    "    print(f\"  {item.manufacturer} {item.model} (S/N: {item.serial_number})\")\n",
    "\n",
    "print(\"\\nFiltered hardware items (by serial number containing 'SCOPE'):\")\n",
    "serial_filtered = metadata_store_client.query_hardware_items(\"$filter=contains(SerialNumber,'SCOPE')\")\n",
    "for item in serial_filtered:\n",
    "    print(f\"  {item.manufacturer} {item.model} (S/N: {item.serial_number})\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c39d264",
   "metadata": {},
   "source": [
    "## Query UUTs (Units Under Test)\n",
    "\n",
    "Uses `query_uuts` to retrieve the UUT definitions (product types being tested). It also shows how to filter UUTs by name and family.\n",
    "\n",
    "**Additional UUT query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by name starting with text\n",
    "uuts_name_starts = metadata_store_client.query_uuts(\"$filter=startswith(Name,'Audio')\")\n",
    "\n",
    "# Combine multiple conditions\n",
    "uuts_combined = metadata_store_client.query_uuts(\"$filter=contains(Name,'Amplifier') and contains(Name,'v1')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e90d54d",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\nFiltered UUTs (by name containing 'Power'):\")\n",
    "filtered_uuts = metadata_store_client.query_uuts(\"$filter=contains(ModelName,'Power')\")\n",
    "for uut in filtered_uuts:\n",
    "    print(f\"  {uut.model_name}\")\n",
    "\n",
    "print(\"\\nFiltered UUTs (by name ending with 'v1.3'):\")\n",
    "v13_uuts = metadata_store_client.query_uuts(\"$filter=endswith(ModelName,'v1.3')\")\n",
    "for uut in v13_uuts:\n",
    "    print(f\"  {uut.model_name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4535acbb",
   "metadata": {},
   "source": [
    "## Query UUT Instances\n",
    "\n",
    "Uses `query_uut_instances` to retrieve specific UUT instances (individual devices with serial numbers). It also shows how to filter UUT instances by serial number and UUT ID.\n",
    "\n",
    "**Additional UUT instance query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by exact serial number\n",
    "instances_by_serial = metadata_store_client.query_uut_instances(\"$filter=SerialNumber eq 'PS-2024-001'\")\n",
    "\n",
    "# Filter by serial number ending with text\n",
    "instances_serial_ends = metadata_store_client.query_uut_instances(\"$filter=endswith(SerialNumber,'001')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26e75660",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\nFiltered UUT instances (by serial containing '2024'):\")\n",
    "filtered_instances = metadata_store_client.query_uut_instances(\"$filter=contains(SerialNumber,'2024')\")\n",
    "for instance in filtered_instances:\n",
    "    print(f\"  Serial: {instance.serial_number}\")\n",
    "\n",
    "print(\"\\nFiltered UUT instances (by serial starting with 'PS'):\")\n",
    "ps_instances = metadata_store_client.query_uut_instances(\"$filter=startswith(SerialNumber,'PS')\")\n",
    "for instance in ps_instances:\n",
    "    print(f\"  Serial: {instance.serial_number}\")\n",
    "\n",
    "print(\"\\nCombined filter - UUT instances (serial contains 'AMP' and '2024'):\")\n",
    "instances_combined = metadata_store_client.query_uut_instances(\"$filter=contains(SerialNumber,'AMP') and contains(SerialNumber,'2024')\")\n",
    "for instance in instances_combined:\n",
    "    print(f\"  Serial: {instance.serial_number}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b94fb9b3",
   "metadata": {},
   "source": [
    "## Query Software Items\n",
    "\n",
    "Uses `query_software_items` to retrieve software items (applications, environments, tools used in testing). It also shows how to filter software items by product and version.\n",
    "\n",
    "**Additional software item query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by exact version\n",
    "software_by_version = metadata_store_client.query_software_items(\"$filter=Version eq '3.11.5'\")\n",
    "\n",
    "# Filter by product containing text\n",
    "software_product_contains = metadata_store_client.query_software_items(\"$filter=contains(Product,'Python')\")\n",
    "\n",
    "# Filter by version ending with text\n",
    "software_version_ends = metadata_store_client.query_software_items(\"$filter=endswith(Version,'.5')\")\n",
    "\n",
    "# Combine multiple conditions - find Python 3.x versions\n",
    "software_combined = metadata_store_client.query_software_items(\"$filter=Product eq 'Python' and startswith(Version,'3.')\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de089e05",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\nFiltered software items (by product 'Python'):\")\n",
    "filtered_software = metadata_store_client.query_software_items(\"$filter=Product eq 'Python'\")\n",
    "for item in filtered_software:\n",
    "    print(f\"  {item.product} {item.version}\")\n",
    "\n",
    "print(\"\\nFiltered software items (by version starting with '3.'):\")\n",
    "version_filtered = metadata_store_client.query_software_items(\"$filter=startswith(Version,'3.')\")\n",
    "for item in version_filtered:\n",
    "    print(f\"  {item.product} {item.version}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be2b084d",
   "metadata": {},
   "source": [
    "## Query Aliases\n",
    "\n",
    "Uses `query_aliases` to retrieve aliases (human-readable references to entities). It also shows how to filter aliases by name and target type.\n",
    "\n",
    "**Additional alias query examples:**\n",
    "\n",
    "```python\n",
    "# Filter by exact alias name\n",
    "aliases_by_name = metadata_store_client.query_aliases(\"$filter=Name eq 'Operator_Smith'\")\n",
    "\n",
    "# Filter by name ending with text\n",
    "aliases_name_ends = metadata_store_client.query_aliases(\"$filter=endswith(Name,'_A1')\")\n",
    "\n",
    "# Combine multiple conditions - find all operator aliases\n",
    "aliases_combined = metadata_store_client.query_aliases(\"$filter=contains(Name,'Operator') and TargetType eq DataStore.AliasTargetType'Operator'\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd194f24",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Helper function to translate numeric target_type to human-readable enum values\n",
    "def get_target_type_name(target_type):\n",
    "    \"\"\"Convert numeric AliasTargetType to human-readable string.\"\"\"\n",
    "    target_type_map = {\n",
    "        0: \"Unspecified\",\n",
    "        1: \"UUT Instance\", \n",
    "        2: \"UUT\",\n",
    "        3: \"Hardware Item\",\n",
    "        4: \"Software Item\",\n",
    "        5: \"Operator\",\n",
    "        6: \"Test Description\",\n",
    "        7: \"Test\",\n",
    "        8: \"Test Station\",\n",
    "        9: \"Test Adapter\"\n",
    "    }\n",
    "    return target_type_map.get(target_type, f\"Unknown ({target_type})\")\n",
    "\n",
    "print(\"\\nFiltered aliases (by name containing 'Operator'):\")\n",
    "filtered_aliases = metadata_store_client.query_aliases(\"$filter=contains(Name,'Operator')\")\n",
    "for alias in filtered_aliases:\n",
    "    target_type_name = get_target_type_name(alias.target_type)\n",
    "    print(f\"  {alias.name} -> {target_type_name}\")\n",
    "\n",
    "print(\"\\nFiltered aliases (by name starting with 'UUT'):\")\n",
    "uut_aliases = metadata_store_client.query_aliases(\"$filter=startswith(Name,'UUT')\")\n",
    "for alias in uut_aliases:\n",
    "    target_type_name = get_target_type_name(alias.target_type)\n",
    "    print(f\"  {alias.name} -> {target_type_name}\")\n",
    "\n",
    "print(\"\\nFiltered aliases (by target type containing 'Test'):\")\n",
    "test_station_aliases = metadata_store_client.query_aliases(\"$filter=TargetType eq DataStore.AliasTargetType'TestStation'\")\n",
    "for alias in test_station_aliases:\n",
    "    target_type_name = get_target_type_name(alias.target_type)\n",
    "    print(f\"  {alias.name} -> {target_type_name}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9bafa1e4",
   "metadata": {},
   "source": [
    "## Clean up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9f68454",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ni-datastore-py3.10",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/README.md sha256=b451136c2998a499c9be4be1561cf3a0b5fc390aaaca33d74187d56d7b50be2b bytes=567 -->
## FILE: examples/notebooks/README.md

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/README.md`
- sha256: `b451136c2998a499c9be4be1561cf3a0b5fc390aaaca33d74187d56d7b50be2b`
- bytes: 567

````markdown
# Example Notebooks

The Jupyter Notebooks contained within the sub-directories of this directory demonstrate usage and functionality of the Measurement Data Store Python API.

These notebooks make use of the main Python environment / kernel of `ni.datastore`. To execute the code in these notebooks, first execute the following command from the repo's root directory:

```sh
poetry install
```

After executing this command, select the environment that it creates as the kernel to use for executing any of the provided notebooks that is of interest to you.
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/notebooks/voltage-regulator/publish_waveforms.ipynb sha256=3f434c17a1b4f84ed14eae0b4ba12d5f0d4da14e09afc1575cbfd973a806d2eb bytes=12270 -->
## FILE: examples/notebooks/voltage-regulator/publish_waveforms.ipynb

- repository: `ni/datastore-python`
- source_path: `examples/notebooks/voltage-regulator/publish_waveforms.ipynb`
- sha256: `3f434c17a1b4f84ed14eae0b4ba12d5f0d4da14e09afc1575cbfd973a806d2eb`
- bytes: 12270

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "60b00f85",
   "metadata": {},
   "source": [
    "# Voltage Regulator Waveform Demo\n",
    "\n",
    "This notebook demonstrates publishing and reading back parametric waveform data with the NI Measurement Data Store. To demonstrate this, it uses simulated data of the dynamic response of a voltage regulator circuit. The simulated voltage regulator is set to regulate to 5V. The input voltage is the measurement parameter and varies from 4.5V to 12V. The data shows how the regulator can only regulate voltages within a certain range. If the input voltage is too large, it will not be able to pin the output voltage to its intended 5V."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0ec35e9",
   "metadata": {},
   "source": [
    "# Set up the test station and other metadata (one time setup)\n",
    "\n",
    "Setting up the metadata for operators, test stations, hardware, etc will typically be done once. We establish 'aliases' which are human-readable strings that can be used to refer to metadata later."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72711880",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform example-specific setup with the DataStoreContext. This is not needed when writing production code.\n",
    "from utilities import DataStoreContext\n",
    "data_store_context = DataStoreContext()\n",
    "data_store_context.initialize()\n",
    "\n",
    "from ni.datastore.metadata import (\n",
    "    MetadataStoreClient,\n",
    "    HardwareItem,\n",
    "    Operator,\n",
    "    SoftwareItem,\n",
    "    TestStation,\n",
    "    Uut,\n",
    "    UutInstance,\n",
    ")\n",
    "\n",
    "# Constants\n",
    "ALIAS_JAMES_BOWERY = \"Operator_BoweryJ\"\n",
    "ALIAS_TEST_STATION_12 = \"TestStation_12\"\n",
    "ALIAS_UUT_NI_6508 = \"UUT_NI-6508\"\n",
    "ALIAS_SOFTWARE_ITEM_WINDOWS_11 = \"Windows_11_23H2\"\n",
    "ALIAS_SOFTWARE_ITEM_PYTHON_3_12 = \"Python_3.12\"\n",
    "ALIAS_HARDWARE_ITEM_PXIe_5171 = \"HardwareItem_PXIe-5171\"\n",
    "\n",
    "metadata_store_client = MetadataStoreClient()\n",
    "\n",
    "# Create alias for Operator \"James Bowery\"\n",
    "operator = Operator(name=\"James Bowery\", role=\"Test Architect\")\n",
    "metadata_store_client.create_operator(operator)\n",
    "metadata_store_client.create_alias(ALIAS_JAMES_BOWERY, operator)\n",
    "\n",
    "# Create alias for Test Station \"TestStation_12\"\n",
    "test_station = TestStation(name=\"TestStation_12\")\n",
    "metadata_store_client.create_test_station(test_station)\n",
    "metadata_store_client.create_alias(ALIAS_TEST_STATION_12, test_station)\n",
    "\n",
    "# Create alias for UUT \"NI-6508\"\n",
    "uut = Uut(model_name=\"NI-6508\", family=\"Digital\")\n",
    "metadata_store_client.create_uut(uut)\n",
    "metadata_store_client.create_alias(ALIAS_UUT_NI_6508, uut)\n",
    "\n",
    "# Create aliases for SoftwareItems\n",
    "software_item = SoftwareItem(product=\"Windows 11 Enterprise\", version=\"23H2\")\n",
    "metadata_store_client.create_software_item(software_item)\n",
    "metadata_store_client.create_alias(ALIAS_SOFTWARE_ITEM_WINDOWS_11, software_item)\n",
    "software_item_2 = SoftwareItem(product=\"Python\", version=\"3.12\")\n",
    "metadata_store_client.create_software_item(software_item_2)\n",
    "metadata_store_client.create_alias(ALIAS_SOFTWARE_ITEM_PYTHON_3_12, software_item_2)\n",
    "\n",
    "# Create aliases for HardwareItem\n",
    "scope = HardwareItem(\n",
    "    manufacturer=\"NI\",\n",
    "    model=\"PXIe-5171\",\n",
    "    serial_number=\"1933B4E\",\n",
    ")\n",
    "metadata_store_client.create_hardware_item(scope)\n",
    "metadata_store_client.create_alias(ALIAS_HARDWARE_ITEM_PXIe_5171, scope)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db8657b1",
   "metadata": {},
   "source": [
    "## Set up the test result (each test run)\n",
    "\n",
    "This setup would be done on each test run. Each time we're going to run a test, we create a `TestResult` using the aliases created for the system from the step above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aaa09bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ni.datastore.data import DataStoreClient, TestResult\n",
    "\n",
    "# Create an instance of the 'NI-6508' on each run\n",
    "uut_instance = UutInstance(uut_id=ALIAS_UUT_NI_6508, serial_number=\"A861-42367\")\n",
    "uut_instance_id = metadata_store_client.create_uut_instance(uut_instance)\n",
    "\n",
    "data_store_client = DataStoreClient()\n",
    "test_result = TestResult(\n",
    "    name=\"voltage regulator waveforms\",\n",
    "    uut_instance_id=uut_instance_id,\n",
    "    operator_id=ALIAS_JAMES_BOWERY,\n",
    "    test_station_id=ALIAS_TEST_STATION_12,\n",
    "    software_item_ids=[\n",
    "        ALIAS_SOFTWARE_ITEM_WINDOWS_11,\n",
    "        ALIAS_SOFTWARE_ITEM_PYTHON_3_12,\n",
    "    ],\n",
    "    hardware_item_ids=[ALIAS_HARDWARE_ITEM_PXIe_5171],\n",
    ")\n",
    "test_result_id = data_store_client.create_test_result(test_result)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aaaddb65",
   "metadata": {},
   "source": [
    "## Simulate Data and Publish with Conditions\n",
    "\n",
    "This step simulates the data response for the voltage regulator and publishes the `AnalogWaveforms` with conditions (parameter values) for the input voltage. There would likely be data published from multiple test runs with the same `TestResult / test_result_id`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0138bf47",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import timezone\n",
    "import hightime as ht\n",
    "import numpy as np\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "from ni.datastore.data import Step\n",
    "from nitypes.scalar import Scalar\n",
    "from nitypes.waveform import AnalogWaveform, Timing\n",
    "\n",
    "def simulate_voltage_regulator(input_voltage, time_ms, target_voltage=5.0) -> AnalogWaveform:\n",
    "    \"\"\"\n",
    "    Simulates the output voltage of a voltage regulator over time.\n",
    "    \"\"\"\n",
    "    output = np.zeros_like(time_ms, dtype=float)\n",
    "    startup_delay = 50  # ms\n",
    "    ramp_duration = 200  # ms\n",
    "    overshoot = 0.2 if input_voltage >= target_voltage else 0.0\n",
    "    max_output = min(input_voltage, target_voltage + overshoot)\n",
    "\n",
    "    for index, t in enumerate(time_ms):\n",
    "        if t < startup_delay:\n",
    "            output[index] = 0\n",
    "        elif t < startup_delay + ramp_duration:\n",
    "            ramp_progress = (t - startup_delay) / ramp_duration\n",
    "            output[index] = ramp_progress * max_output\n",
    "        else:\n",
    "            # Simulate regulation behavior\n",
    "            if input_voltage < target_voltage:\n",
    "                output[index] = input_voltage\n",
    "            elif input_voltage <= 8:\n",
    "                output[index] = target_voltage + overshoot * np.exp(-(t - startup_delay - ramp_duration)/300)\n",
    "            elif input_voltage <= 10:\n",
    "                output[index] = target_voltage + 0.5 + 0.2 * np.sin(0.01 * t)\n",
    "            else:\n",
    "                output[index] = target_voltage + 1.0 + 0.5 * np.sin(0.01 * t)\n",
    "\n",
    "    waveform = AnalogWaveform(\n",
    "            sample_count=len(output),\n",
    "            raw_data=np.array(output),\n",
    "            timing=Timing.create_with_regular_interval(\n",
    "                ht.timedelta(seconds=1e-3),\n",
    "                ht.datetime.now(timezone.utc)\n",
    "            )\n",
    "        )\n",
    "\n",
    "    return waveform\n",
    "\n",
    "# Time in milliseconds\n",
    "time_ms = np.linspace(0, 1000, 500)\n",
    "step = Step(name=\"Initial step\", test_result_id=test_result_id)\n",
    "step_id = data_store_client.create_step(step)\n",
    "\n",
    "# Input voltages to simulate\n",
    "input_voltages = [4.5, 7.0, 9.0, 12.0]\n",
    "\n",
    "# Simulate each input voltage\n",
    "for vin in input_voltages:\n",
    "    waveform = simulate_voltage_regulator(vin, time_ms)\n",
    "    published_measurement = data_store_client.publish_measurement(\n",
    "        name=\"voltage_response\",\n",
    "        value=waveform,\n",
    "        step_id=step_id,\n",
    "    )\n",
    "    scalar = Scalar(value=vin, units=\"V\")\n",
    "    published_condition = data_store_client.publish_condition(\n",
    "        \"input_voltage\",\n",
    "        \"integer\",\n",
    "        scalar,\n",
    "        step_id\n",
    "    )\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9741fdd7",
   "metadata": {},
   "source": [
    "## Read Published Data\n",
    "\n",
    "Read back the published data and plot them using the parameter (condition) values and the timing data from the stored `AnalogWaveforms` and display them in a plotly graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d4855c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nitypes.vector import Vector\n",
    "\n",
    "# Create Plotly figure\n",
    "fig = go.Figure()\n",
    "colors = ['blue', 'green', 'orange', 'red']\n",
    "\n",
    "conditions = data_store_client.query_conditions(odata_query=f\"$filter=stepid eq {step_id}\")\n",
    "condition = next(iter(conditions), None)\n",
    "condition_values = []\n",
    "if condition is not None:\n",
    "    condition_data = data_store_client.read_condition_value(condition, expected_type=Vector)\n",
    "    units = condition_data.units\n",
    "    for val in condition_data:\n",
    "        condition_values.append(str(val) + units)\n",
    "measurements = data_store_client.query_measurements(odata_query=f\"$filter=stepid eq {step_id}\")\n",
    "sorted_measurements = sorted(measurements, key=lambda m: m.parametric_index)\n",
    "for measurement in sorted_measurements:\n",
    "    waveform = data_store_client.read_measurement_value(measurement, expected_type=AnalogWaveform)\n",
    "    color = colors[measurement.parametric_index]\n",
    "    timing = waveform.timing\n",
    "    fig.add_trace(go.Scatter(\n",
    "        x=np.arange(len(waveform.raw_data)) * waveform.timing.sample_interval.total_seconds() * 1000,\n",
    "        y=waveform.raw_data,\n",
    "        mode='lines',\n",
    "        name=f'Input {condition_values[measurement.parametric_index]}',\n",
    "        line=dict(color=color)\n",
    "    ))\n",
    "\n",
    "\n",
    "# Update layout\n",
    "fig.update_layout(\n",
    "    title='Voltage Regulator Output Simulation',\n",
    "    xaxis_title='Time (ms)',\n",
    "    yaxis_title='Output Voltage (V)',\n",
    "    legend_title='Input Voltage',\n",
    "    template='plotly_white'\n",
    ")\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0317fe8",
   "metadata": {},
   "source": [
    "## Clean Up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cb4c298",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata_store_client.close()\n",
    "data_store_client.close()\n",
    "\n",
    "# Perform example-specific cleanup. This is not needed when writing production code.\n",
    "data_store_context.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/poetry.lock sha256=2512939982c3483f39bc78cd3dcabe65c2620c52c010bb67d1fec1d94af7ec07 bytes=138285 -->
## FILE: examples/overview/poetry.lock

- repository: `ni/datastore-python`
- source_path: `examples/overview/poetry.lock`
- sha256: `2512939982c3483f39bc78cd3dcabe65c2620c52c010bb67d1fec1d94af7ec07`
- bytes: 138285

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "ast-serialize"
version = "0.5.0"
description = "Python bindings for mypy AST serialization"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8f5c14f169eb0972c0c21bada5358b23d6047c76583b005234f865b11f1fa00a"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7d1a2de9de5be04652f0ed60738356ef94f66db37924a9499fffe98dc491aa0b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:be5173fb66f9b49026d9d5a2ff0fc7c7009077107c0eb285b2d60fdf1fe10bd1"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f8015cd071ac1339924ee2b8098c93e00e155f30a16f40ec9816fcf84f4753f6"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5499e8797edff2a9186aa313ed382c6b422e798e9332d9953badcee6e69a88f2"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6848f2a093fb5548751a9a09bff8fcd229e2bbeb0e3331f391b6ae6d26cd9903"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:832d4c998e0b091fd60a6d6bceee535483c4d490de9ba85003af835225719261"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:16db7c62ec0b8efe1d7afd283a388d8f74f2605d56032e5a37747d2de8dba027"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:baf5eb061eb5bccade4128ad42da33787d72f6013809cd1b590376ece8b3c937"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:104e4a35bd7c124173c41760ef9aaea17ddb3f86c65cb643671d59afbe3ee94c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:36be371028fc1675acb38a331bde160dbab7ff907fdf00b67eb6911aa106951b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:061ee58bdb52341c8201a6df41182a977736bae3b7ded87ca7176ca25a8a47ab"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b15219e9cdc9f53f6f4cb51c009203507228226148c05c5e8fe451c28b435eb3"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win32.whl", hash = "sha256:842d1c004bb466c7df036f95fabef789570541922b10976b12f5592a69cf0b38"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b0c06d760909b095cc466356dfccd05a1c7233a6ca191c020dca2c6a6f16c24c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:787baedb0262cc49e8ce37cc15c00ae818e46a165a3b36f5e21ed174998104cb"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:0668aa9459cfa8c9c49ddd2163ebcf43088ba045ef7492af6fe22e0098303101"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:bf683d6363edf2b39eed6b6d4fe22d34b6203867a67e27134d9e2a2680c4bc4a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9cc22cf0c9be65e71cf88fda130af60d61eb4a79370ad4cfe7900d48a4aa2211"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f66173891548c9f2726bf27957b41cabce12fa679dc6da505ddbde4d4b3b31cf"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e42d729ef2be96a14efbad355093284739e3670ece3e534f82cc8832790911d9"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b725026bafa801dbd7310eb13a75f0a2e370e7e51b2cb225f9d21fcfadf919ee"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b54f60c1d78767a53b67eaa663f0dfac3afe606aa07f1301572f588b73d64809"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_31_riscv64.whl", hash = "sha256:27d51654fc240a1e87e742d353d98eb45b75f62f129086b3596ab53df2ac2a43"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c36237c46dd1674542f2109740ea5ea485a169bf1431939ada0434e17934"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:1943db345233cc7194a470f13afa9c59772c0b123dea0c9414c4d4ca54369759"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:df1c00022cbbcb064bfaa505aa9c9295362443ce5dacb459d1331d3da353f887"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:cae65289fc456fde04af979a2be09302ef5d8ab92ef23e596d6746dc267ada27"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:239a4c354e8d676e9d94631d1d4a64edc6b266f86ff3a5a80aedd344f342c01d"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win32.whl", hash = "sha256:143a4ef63285a075871908fda3672dc21864b83a8ec3ee12304aa3e4c5387b9a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_amd64.whl", hash = "sha256:cf25572c526add400f26a4750dc6ce0c3bb93fc1f75e7ae0cad4ce4f2cd5c590"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_arm64.whl", hash = "sha256:92a31c9c20d25a076edaeec76b128a3535d74a24f340b9a8a7e96c9b86dc9642"},
    {file = "ast_serialize-0.5.0.tar.gz", hash = "sha256:5880091bfe6f4f986f22866375c2e884843e7a0b6343ae41aeea659613d879b6"},
]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["lint"]
files = [
    {file = "better_diff-0.1.4-py3-none-any.whl", hash = "sha256:06e63358b2047ae2695abd96316f47c6d3c38b9e641f53012279878d66d8792e"},
    {file = "better_diff-0.1.4.tar.gz", hash = "sha256:920ca76bdbcd2f0c361fa5d9a2d4727624a3545d6cb467b1b6616cad8a634de7"},
]

[[package]]
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "black-25.12.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f85ba1ad15d446756b4ab5f3044731bf68b777f8f9ac9cdabd2425b97cd9c4e8"},
    {file = "black-25.12.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:546eecfe9a3a6b46f9d69d8a642585a6eaf348bcbbc4d87a19635570e02d9f4a"},
    {file = "black-25.12.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:17dcc893da8d73d8f74a596f64b7c98ef5239c2cd2b053c0f25912c4494bf9ea"},
    {file = "black-25.12.0-cp310-cp310-win_amd64.whl", hash = "sha256:09524b0e6af8ba7a3ffabdfc7a9922fb9adef60fed008c7cd2fc01f3048e6e6f"},
    {file = "black-25.12.0-cp310-cp310-win_arm64.whl", hash = "sha256:b162653ed89eb942758efeb29d5e333ca5bb90e5130216f8369857db5955a7da"},
    {file = "black-25.12.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d0cfa263e85caea2cff57d8f917f9f51adae8e20b610e2b23de35b5b11ce691a"},
    {file = "black-25.12.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a2f578ae20c19c50a382286ba78bfbeafdf788579b053d8e4980afb079ab9be"},
    {file = "black-25.12.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e1b65634b0e471d07ff86ec338819e2ef860689859ef4501ab7ac290431f9b"},
    {file = "black-25.12.0-cp311-cp311-win_amd64.whl", hash = "sha256:a3fa71e3b8dd9f7c6ac4d818345237dfb4175ed3bf37cd5a581dbc4c034f1ec5"},
    {file = "black-25.12.0-cp311-cp311-win_arm64.whl", hash = "sha256:51e267458f7e650afed8445dc7edb3187143003d52a1b710c7321aef22aa9655"},
    {file = "black-25.12.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:31f96b7c98c1ddaeb07dc0f56c652e25bdedaac76d5b68a059d998b57c55594a"},
    {file = "black-25.12.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:05dd459a19e218078a1f98178c13f861fe6a9a5f88fc969ca4d9b49eb1809783"},
    {file = "black-25.12.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1f68c5eff61f226934be6b5b80296cf6939e5d2f0c2f7d543ea08b204bfaf59"},
    {file = "black-25.12.0-cp312-cp312-win_amd64.whl", hash = "sha256:274f940c147ddab4442d316b27f9e332ca586d39c85ecf59ebdea82cc9ee8892"},
    {file = "black-25.12.0-cp312-cp312-win_arm64.whl", hash = "sha256:169506ba91ef21e2e0591563deda7f00030cb466e747c4b09cb0a9dae5db2f43"},
    {file = "black-25.12.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a05ddeb656534c3e27a05a29196c962877c83fa5503db89e68857d1161ad08a5"},
    {file = "black-25.12.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9ec77439ef3e34896995503865a85732c94396edcc739f302c5673a2315e1e7f"},
    {file = "black-25.12.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e509c858adf63aa61d908061b52e580c40eae0dfa72415fa47ac01b12e29baf"},
    {file = "black-25.12.0-cp313-cp313-win_amd64.whl", hash = "sha256:252678f07f5bac4ff0d0e9b261fbb029fa530cfa206d0a636a34ab445ef8ca9d"},
    {file = "black-25.12.0-cp313-cp313-win_arm64.whl", hash = "sha256:bc5b1c09fe3c931ddd20ee548511c64ebf964ada7e6f0763d443947fd1c603ce"},
    {file = "black-25.12.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:0a0953b134f9335c2434864a643c842c44fba562155c738a2a37a4d61f00cad5"},
    {file = "black-25.12.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2355bbb6c3b76062870942d8cc450d4f8ac71f9c93c40122762c8784df49543f"},
    {file = "black-25.12.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9678bd991cc793e81d19aeeae57966ee02909877cb65838ccffef24c3ebac08f"},
    {file = "black-25.12.0-cp314-cp314-win_amd64.whl", hash = "sha256:97596189949a8aad13ad12fcbb4ae89330039b96ad6742e6f6b45e75ad5cfd83"},
    {file = "black-25.12.0-cp314-cp314-win_arm64.whl", hash = "sha256:778285d9ea197f34704e3791ea9404cd6d07595745907dd2ce3da7a13627b29b"},
    {file = "black-25.12.0-py3-none-any.whl", hash = "sha256:48ceb36c16dbc84062740049eef990bb2ce07598272e673c17d1a7720c71c828"},
    {file = "black-25.12.0.tar.gz", hash = "sha256:8d3dd9cea14bff7ddc0eb243c811cdb1a011ebb4800a5f0335a01a68654796a7"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "click"
version = "8.4.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "click-8.4.1-py3-none-any.whl", hash = "sha256:482be17c6991b8c19c5429a1e995d9b0efdbb63172824c41f99965dc0ade8ec2"},
    {file = "click-8.4.1.tar.gz", hash = "sha256:918b5633eddf6b41c32d4f454bf0de810065c74e3f7dbf8ee5452f8be88d3e96"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["lint"]
markers = "platform_system == \"Windows\""
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "datastore-utilities"
version = "0.1.0.dev0"
description = "Development utilities for datastore-python"
optional = false
python-versions = "^3.10"
groups = ["dev"]
files = []
develop = true

[package.source]
type = "directory"
url = "../../utilities"

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "flake8-6.1.0-py2.py3-none-any.whl", hash = "sha256:ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5"},
    {file = "flake8-6.1.0.tar.gz", hash = "sha256:d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.11.0,<2.12.0"
pyflakes = ">=3.1.0,<3.2.0"

[[package]]
name = "flake8-black"
version = "0.4.0"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_black-0.4.0-py3-none-any.whl", hash = "sha256:288762d0c9ea065782d87eeecbcc20c69079d17fe1d0f0445f0eb0b0ffb80c39"},
    {file = "flake8_black-0.4.0.tar.gz", hash = "sha256:bf226868f695dee48d55ff6d7747e900709bfd6f605b7a378c70e711e3fc26cb"},
]

[package.dependencies]
black = ">=22.1.0"
flake8 = ">=3"
tomli = {version = "*", markers = "python_version < \"3.11\""}

[package.extras]
develop = ["build", "twine"]

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["lint"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "flake8-tidy-imports"
version = "4.12.0"
description = "A flake8 plugin that helps you write tidier imports."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "grpcio"
version = "1.81.1"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "grpcio-1.81.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:6f9a0c9c1cc15c112d1c053064fd032b64917062292c3d70aea280e02ae10b77"},
    {file = "grpcio-1.81.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:69ef28e54fc85397f91b8c19592b8ef3d81952080366914823bd8572a2958120"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:15641444eca4a29358107b3dceb74c1c6305c55c822fd199b458aaea4068a7fb"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:d4b2dddfc219f54f956ccd53cf76a1d338ffe68fc7f2849ec9c7feb9927ff692"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ca1cc11d82677b9662082e5478b7528e2b7db7beaa6bdff42bd62789d81be399"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:aa2ba7d2ad6df4d80127cea65e5b8d5e2c3adbf153ff4804452836328aca7c54"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:592b5fee597faa91cce2dd294dd7d9a1c83d76c4dbf877e33ec1adb866b2fbed"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:62481553b1793a27e9b9c3cf9e5bd483ef045ca72462592074b46d42b0c4d9b9"},
    {file = "grpcio-1.81.1-cp310-cp310-win32.whl", hash = "sha256:bb693b1e3d9a2f3fd228e2110daf4b5aeedb36761ca1e4282f74725f6d89f611"},
    {file = "grpcio-1.81.1-cp310-cp310-win_amd64.whl", hash = "sha256:88268ca418cacea64cecb0d1d600d3c6b3a8038fcba02e1e205178c5b1f47661"},
    {file = "grpcio-1.81.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:d71d30f2d92f67d944631c523713934fee37292469e182ebcd2c1dd8a64ce53f"},
    {file = "grpcio-1.81.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:b137f4bf3ada9dc44d411478decc6ff09a79ed30b306cd2abaa98408c3588137"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a3acb384427816dd5d470f47e62137b87f74da694faa8a50147012cf40df276a"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f9a0ebbe45c29b5e5866593c12b78bd9035f0f0f0d4bc8361680cd580d99db49"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:0a37165cc80b1a368384b383e63a4c38116a10467ae44c904d2d7468c4470ec2"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:6282caffb41ec326d4cb67ca9cf53b739d1b2f975a2acb498c7418e9f7d9a416"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:a35009284d0d3d5c2c9601c164a911b8b4331608d98a9a66d47d97bb2f522b70"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1b22c80559854b789a01fd89e8929b3798a156c0829b5282a8939f33ad4115ad"},
    {file = "grpcio-1.81.1-cp311-cp311-win32.whl", hash = "sha256:428bec0161b48d8cf583c068591bc0016d0d9cfff52462b72b3884861ea768c5"},
    {file = "grpcio-1.81.1-cp311-cp311-win_amd64.whl", hash = "sha256:30e825f6848d9f18bba350ed6c75c1b02a0b5184474a31db9a32b1fa66fd8c79"},
    {file = "grpcio-1.81.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:8b39472beafc0bdcafc4c8c73ad082ebfdb449d566897a61e7acb4fa88089115"},
    {file = "grpcio-1.81.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:12b7524c88d4026d3dcb7b0ebe16b6714f3b4af402ddd0f0639ab064a00c87c3"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1e123f9b37edb8375fd74130d1f69c944bbf0a7b06761ae7211154b8759e94d2"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:2c2e2ae6867c2966b8daccc836d54a13218e0007e9a490aeb81dd05be64d22d7"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:766bc7c9a9c340342f4c864ccbda8e78111e4751f13b895812b9c148fb79e9d0"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b259a04a737cb3496be0901328eb8b7552ed8df4865d8c8f1cf1bffcfc0776a3"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:85b10a45b8993d195c4f3ff57025b8d1e11834909ee475c403bfa60cb4caefaf"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8ea1936c26b99999b27479853039a7f34713f56c49375ad52b38535ec93a796c"},
    {file = "grpcio-1.81.1-cp312-cp312-win32.whl", hash = "sha256:a185a04039df6cae8648bc8ab6d6fde7bf94f7188ecf7828e76ac52eef1e41d6"},
    {file = "grpcio-1.81.1-cp312-cp312-win_amd64.whl", hash = "sha256:3ad74f8bb1a18963914c5452d289422830b39459e8776ebbcd207be1fbfb1d94"},
    {file = "grpcio-1.81.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:b10e1ff4756ed27d5a29d7fc79cfce7ef1ff56ad20025b89bac7cf79e09abbbe"},
    {file = "grpcio-1.81.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:819edbdcb42ab8598b494bcf0222684bbb7a3c772bd1b1f0be7e029a6063c28e"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c5bf2dc311127d91230cc79b92188c082634a06cf66c5234db49a43b910183b0"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:e8ca6a1fcdb2943c9cbc1804a1baf3acb6071d72a471591678ded84218006e14"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e64dd101d380a115cc5a0c7856788adb535f1a4e21fc543775602f8be95180ae"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:98a07f9bf591e3a8919797bee1c53f026ba4acd587e5a4404c8e57c9ec36b2a5"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:c261d74b1a945cf895a9d6eccd1685a8e837531beaab782da4d630a8d12deffb"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:58ad1131c300d3c9b933802b3cc4dc69d380822935ba50b28703156ea826fbf7"},
    {file = "grpcio-1.81.1-cp313-cp313-win32.whl", hash = "sha256:78e29211f26da2fdd0e9c6d2b79f489476140cf7029b6a64808ade7ca4156a42"},
    {file = "grpcio-1.81.1-cp313-cp313-win_amd64.whl", hash = "sha256:edb59506291b647a30884b1d51a599d605f40b20af4a7dc3d33786a47a31de60"},
    {file = "grpcio-1.81.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:506f48f2f9c29b143fca3dad7b0d518c188b6c9648c75a2ae6e2d9f2c13a060b"},
    {file = "grpcio-1.81.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:d865db4a6318e1c1bea83292e0ed231090538fc4ca45425b0f0480eb338bbc6e"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:e2aa72e3ce1770317ef534f63d397b55e130725f5149bd36077c3b539019db27"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:0490c30c261eded63f3f354979f9dc4502a9fb944cccb60cd9dc85f5a7349854"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:410482da976329fe5f4067270401b12cf2bd552ff8020f054ecfaddb5475f9d6"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e3657301562ac3cb8018d30d0d3ebfa39932239f7b5703422057ef14b69949f5"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:24c8e57504c8f45b237e40b99262d181071e5099a07053695b75d97bb53053a0"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b427c19380991a4eaab2f6144b64b99b412043314c6bf4ab544f97bb31ee4190"},
    {file = "grpcio-1.81.1-cp314-cp314-win32.whl", hash = "sha256:61233fe8951e5c85dff81c2458b6528624760166946b5b47ea150a589168411f"},
    {file = "grpcio-1.81.1-cp314-cp314-win_amd64.whl", hash = "sha256:3768a5ff1b2125e6f552e561b6b2dca0e64982d8949689b4df145cf8b98d7821"},
    {file = "grpcio-1.81.1.tar.gz", hash = "sha256:6fa10a767143a5e82e8eaab53918af0cd8909a57a27f8cb2288b80a613ac671b"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.81.1)"]

[[package]]
name = "grpcio-tools"
version = "1.49.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["main"]
markers = "python_version < \"3.12\""
files = [
    {file = "grpcio-tools-1.49.1.tar.gz", hash = "sha256:84cc64e5b46bad43d5d7bd2fd772b656eba0366961187a847e908e2cb735db91"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:2dfb6c7ece84d46bd690b23d3e060d18115c8bc5047d2e8a33e6747ed323a348"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:8f452a107c054a04db2570f7851a07f060313c6e841b0d394ce6030d598290e6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:6a198871b582287213c4d70792bf275e1d7cf34eed1d019f534ddf4cd15ab039"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a0cca67a7d0287bdc855d81fdd38dc949c4273273a74f832f9e520abe4f20bc6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaff4c89eecb37c247b93025410db68114d97fa093cbb028e9bd7cda5912473"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:bb8773118ad315db317d7b22b5ff75d649ca20931733281209e7cbd8c0fad53e"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:7cc5534023735b8a8f56760b7c533918f874ce5a9064d7c5456d2709ae2b31f9"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win32.whl", hash = "sha256:d277642acbe305f5586f9597b78fb9970d6633eb9f89c61e429c92c296c37129"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win_amd64.whl", hash = "sha256:eed599cf08fc1a06c72492d3c5750c32f58de3750eddd984af1f257c14326701"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:9e5c13809ab2f245398e8446c4c3b399a62d591db651e46806cccf52a700452e"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:ab3d0ee9623720ee585fdf3753b3755d3144a4a8ae35bca8e3655fa2f41056be"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6ba87e3512bc91d78bf9febcfb522eadda171d2d4ddaf886066b0f01aa4929ad"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:13e13b3643e7577a3ec13b79689eb4d7548890b1e104c04b9ed6557a3c3dd452"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:324f67d9cb4b7058b6ce45352fb64c20cc1fa04c34d97ad44772cfe6a4ae0cf5"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:a64bab81b220c50033f584f57978ebbea575f09c1ccee765cd5c462177988098"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win32.whl", hash = "sha256:f632d376f92f23e5931697a3acf1b38df7eb719774213d93c52e02acd2d529ac"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win_amd64.whl", hash = "sha256:28ff2b978d9509474928b9c096a0cce4eaa9c8f7046136aee1545f6211ed8126"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-linux_armv7l.whl", hash = "sha256:46afd3cb7e555187451a5d283f108cdef397952a662cb48680afc615b158864a"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-macosx_10_10_x86_64.whl", hash = "sha256:9284568b728e41fa8f7e9c2e7399545d605f75d8072ef0e9aa2a05655cb679eb"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:aa34442cf787732cb41f2aa6172007e24f480b8b9d3dc5166de80d63e9072ea4"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3b8c9eb5a4250905414cd53a68caea3eb8f0c515aadb689e6e81b71ebe9ab5c6"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ab15db024051bf21feb21c29cb2c3ea0a2e4f5cf341d46ef76e17fcf6aaef164"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:502084b622f758bef620a9107c2db9fcdf66d26c7e0e481d6bb87db4dc917d70"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:4085890b77c640085f82bf1e90a0ea166ce48000bc2f5180914b974783c9c0a8"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win32.whl", hash = "sha256:da0edb984699769ce02e18e3392d54b59a7a3f93acd285a68043f5bde4fc028e"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win_amd64.whl", hash = "sha256:9887cd622770271101a7dd1832845d64744c3f88fd11ccb2620394079197a42e"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-linux_armv7l.whl", hash = "sha256:8440fe7dae6a40c279e3a24b82793735babd38ecbb0d07bb712ff9c8963185d9"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-macosx_10_10_x86_64.whl", hash = "sha256:b5de2bb7dd6b6231da9b1556ade981513330b740e767f1d902c71ceee0a7d196"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:1e6f06a763aea7836b63d9c117347f2bf7038008ceef72758815c9e09c5fb1fc"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e31562f90120318c5395aabec0f2f69ad8c14b6676996b7730d9d2eaf9415d57"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:49ef9a4e389a618157a9daa9fafdfeeaef1ece9adda7f50f85db928f24d4b3e8"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:b384cb8e8d9bcb55ee8f9b064374561c7a1a05d848249581403d36fc7060032f"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:73732f77943ac3e898879cbb29c27253aa3c47566b8a59780fd24c6a54de1b66"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win32.whl", hash = "sha256:b594b2745a5ba9e7a76ce561bc5ab40bc65bb44743c505529b1e4f12af29104d"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win_amd64.whl", hash = "sha256:680fbc88f8709ddcabb88f86749f2d8e429160890cff2c70680880a6970d4eef"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:e8c3869121860f6767eedb7d24fc54dfd71e737fdfbb26e1334684606f3274fd"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:73e9d7c886ba10e20c97d1dab0ff961ba5800757ae5e31be21b1cda8130c52f8"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:1760de2dd2c4f08de87b039043a4797f3c17193656e7e3eb84e92f0517083c0c"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cd4b1e216dd04d9245ee8f4e601a1f98c25e6e417ea5cf8d825c50589a8b447e"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c1c28751ab5955cae563d07677e799233f0fe1c0fc49d9cbd61ff1957e83617f"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:c24239c3ee9ed16314c14b4e24437b5079ebc344f343f33629a582f8699f583b"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:892d3dacf1942820f0b7a868a30e6fbcdf5bec08543b682c7274b0101cee632d"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win32.whl", hash = "sha256:704d21509ec06efc9d034dbe70e7152715aac004941f4f0f553cf3a0aff15bd5"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win_amd64.whl", hash = "sha256:1efa0c221c719433f441ac0e026fc3c4dbc9a1a08a552ecdc707775e2f2fbbae"},
]

[package.dependencies]
grpcio = ">=1.49.1"
protobuf = ">=4.21.3,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.59.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["main"]
markers = "python_version == \"3.12\""
files = [
    {file = "grpcio-tools-1.59.0.tar.gz", hash = "sha256:aa4018f2d8662ac4d9830445d3d253a11b3e096e8afe20865547137aa1160e93"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:882b809b42b5464bee55288f4e60837297f9618e53e69ae3eea6d61b05ce48fa"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:4499d4bc5aa9c7b645018d8b0db4bebd663d427aabcd7bee7777046cb1bcbca7"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:f381ae3ad6a5eb27aad8d810438937d8228977067c54e0bd456fce7e11fdbf3d"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f1c684c0d9226d04cadafced620a46ab38c346d0780eaac7448da96bf12066a3"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:40cbf712769242c2ba237745285ef789114d7fcfe8865fc4817d87f20015e99a"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:1df755951f204e65bf9232a9cac5afe7d6b8e4c87ac084d3ecd738fdc7aa4174"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:de156c18b0c638aaee3be6ad650c8ba7dec94ed4bac26403aec3dce95ffe9407"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win32.whl", hash = "sha256:9af7e138baa9b2895cf1f3eb718ac96fc5ae2f8e31fca405e21e0e5cd1643c52"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win_amd64.whl", hash = "sha256:f14a6e4f700dfd30ff8f0e6695f944affc16ae5a1e738666b3fae4e44b65637e"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:db030140d0da2368319e2f23655df3baec278c7e0078ecbe051eaf609a69382c"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-macosx_10_10_universal2.whl", hash = "sha256:eeed386971bb8afc3ec45593df6a1154d680d87be1209ef8e782e44f85f47e64"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:962d1a3067129152cee3e172213486cb218a6bad703836991f46f216caefcf00"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:26eb2eebf150a33ebf088e67c1acf37eb2ac4133d9bfccbaa011ad2148c08b42"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5b2d6da553980c590487f2e7fd3ec9c1ad8805ff2ec77977b92faa7e3ca14e1f"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:335e2f355a0c544a88854e2c053aff8a3f398b84a263a96fa19d063ca1fe513a"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:204e08f807b1d83f5f0efea30c4e680afe26a43dec8ba614a45fa698a7ef0a19"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win32.whl", hash = "sha256:05bf7b3ed01c8a562bb7e840f864c58acedbd6924eb616367c0bd0a760bdf483"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win_amd64.whl", hash = "sha256:df85096fcac7cea8aa5bd84b7a39c4cdbf556b93669bb4772eb96aacd3222a4e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:240a7a3c2c54f77f1f66085a635bca72003d02f56a670e7db19aec531eda8f78"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-macosx_10_10_universal2.whl", hash = "sha256:6119f62c462d119c63227b9534210f0f13506a888151b9bf586f71e7edf5088b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:387662bee8e4c0b52cc0f61eaaca0ca583f5b227103f685b76083a3590a71a3e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8f0da5861ee276ca68493b217daef358960e8527cc63c7cb292ca1c9c54939af"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d0f0806de1161c7f248e4c183633ee7a58dfe45c2b77ddf0136e2e7ad0650b1b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:c683be38a9bf4024c223929b4cd2f0a0858c94e9dc8b36d7eaa5a48ce9323a6f"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:f965707da2b48a33128615bcfebedd215a3a30e346447e885bb3da37a143177a"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win32.whl", hash = "sha256:2ee960904dde12a7fa48e1591a5b3eeae054bdce57bacf9fd26685a98138f5bf"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win_amd64.whl", hash = "sha256:71cc6db1d66da3bc3730d9937bddc320f7b1f1dfdff6342bcb5741515fe4110b"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-linux_armv7l.whl", hash = "sha256:f6263b85261b62471cb97b7505df72d72b8b62e5e22d8184924871a6155b4dbf"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-macosx_10_10_universal2.whl", hash = "sha256:b8e95d921cc2a1521d4750eedefec9f16031457920a6677edebe9d1b2ad6ae60"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:cb63055739808144b541986291679d643bae58755d0eb082157c4d4c04443905"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8c4634b3589efa156a8d5860c0a2547315bd5c9e52d14c960d716fe86e0927be"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2d970aa26854f535ffb94ea098aa8b43de020d9a14682e4a15dcdaeac7801b27"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:821dba464d84ebbcffd9d420302404db2fa7a40c7ff4c4c4c93726f72bfa2769"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:0548e901894399886ff4a4cd808cb850b60c021feb4a8977a0751f14dd7e55d9"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-win_amd64.whl", hash = "sha256:bb87158dbbb9e5a79effe78d54837599caa16df52d8d35366e06a91723b587ae"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:1d551ff42962c7c333c3da5c70d5e617a87dee581fa2e2c5ae2d5137c8886779"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-macosx_10_10_universal2.whl", hash = "sha256:4ee443abcd241a5befb05629013fbf2eac637faa94aaa3056351aded8a31c1bc"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:520c0c83ea79d14b0679ba43e19c64ca31d30926b26ad2ca7db37cbd89c167e2"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9fc02a6e517c34dcf885ff3b57260b646551083903e3d2c780b4971ce7d4ab7c"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6aec8a4ed3808b7dfc1276fe51e3e24bec0eeaf610d395bcd42934647cf902a3"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:99b3bde646720bbfb77f263f5ba3e1a0de50632d43c38d405a0ef9c7e94373cd"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:51d9595629998d8b519126c5a610f15deb0327cd6325ed10796b47d1d292e70b"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win32.whl", hash = "sha256:bfa4b2b7d21c5634b62e5f03462243bd705adc1a21806b5356b8ce06d902e160"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win_amd64.whl", hash = "sha256:9ed05197c5ab071e91bcef28901e97ca168c4ae94510cb67a14cb4931b94255a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:498e7be0b14385980efa681444ba481349c131fc5ec88003819f5d929646947c"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-macosx_10_10_universal2.whl", hash = "sha256:b519f2ecde9a579cad2f4a7057d5bb4e040ad17caab8b5e691ed7a13b9db0be9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:ef3e8aca2261f7f07436d4e2111556c1fb9bf1f9cfcdf35262743ccdee1b6ce9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:27a7f226b741b2ebf7e2d0779d2c9b17f446d1b839d59886c1619e62cc2ae472"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:784aa52965916fec5afa1a28eeee6f0073bb43a2a1d7fedf963393898843077a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:e312ddc2d8bec1a23306a661ad52734f984c9aad5d8f126ebb222a778d95407d"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:868892ad9e00651a38dace3e4924bae82fc4fd4df2c65d37b74381570ee8deb1"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win32.whl", hash = "sha256:a4f6cae381f21fee1ef0a5cbbbb146680164311157ae618edf3061742d844383"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win_amd64.whl", hash = "sha256:4a10e59cca462208b489478340b52a96d64e8b8b6f1ac097f3e8cb211d3f66c0"},
]

[package.dependencies]
grpcio = ">=1.59.0"
protobuf = ">=4.21.6,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.67.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.8"
groups = ["main"]
markers = "python_version == \"3.13\""
files = [
    {file = "grpcio_tools-1.67.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:12aa38af76b5ef00a55808c7c374ed18d5dc7cc8081b717e56da3c50df1776e2"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:b0b03d055127bbc7c629454804b53b5cad2cedfcf904576d159a8a04c22b8e66"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:02b0b50c59a8f7428326197027a2f586d216c46138c547f861533c46bff78bfe"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b2afdfe151ed9edbd4a3fd646716f83b58010769c57f9c0aa1cf4c3bfb1240a8"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc3eeb87575b2b360c5ef5aef22eb76cfdd6a255d2f628a48ab0e5a61a0039fb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:ead78089c4771605a1ff8894e47f2267440693f1beeee06fd5a788aede83370f"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:0671dcdccef09ca4eb415c1d6f470a857c6486733c146676f6810a3ade1d42cb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win32.whl", hash = "sha256:a7398d90b8c7da479aec8f853d3664d5a93c209f8ac3bd41cb7ae4e8677a45c6"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win_amd64.whl", hash = "sha256:f7e7d70a74df7e07be7cceaa694b7e8e5f3bef8e0299906f60885ecf7a40adb4"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:655716bf931a22a090134d87953710033640996d31e36f5f9b0106ff5f552d8e"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:484ae782f9d3ff58e0bbb2f4cad14d5f5d9132fc701835b1dffd2c2a06f73ba6"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:f3e34de876efe1273f91e25ef241e449ed7f9411472dd9ff56d2039618017c30"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d8301719edde2c3d388995703cdd962f558b76e9750405f772dce61402e4c3d0"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1629ea246044ccd473d9ac4c9f137a440d830b5e08d35225e1b354dbbb15b75d"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:d77a3c5cec0065267ca1a0b2589ececd1277ce25aa67f13ec50c816ee6f26f7f"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9bf992bcc7d9e6eaa20705056e1b955593092a38cec1746fef389d873ab2056"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win32.whl", hash = "sha256:7e6e3db119c38629e0767cdb2ee18726ecc87e2249117d4c9e7ce06ea8c894ea"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win_amd64.whl", hash = "sha256:c6c27aec301a0e6cf231f9ee1c467c64002af51170fa7c0f3bb10bbfcd03fee7"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:dca7f053cbdb26a587d4410ddb893877c585fb60a31f22fdd128e4f7c4dab27c"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-macosx_10_9_universal2.whl", hash = "sha256:de8c4f68ffa690769d84329c17c7fdd5fbe4c61b8f8a0de03f1ad8ef8bb06963"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:6e4ecb24c27a78f09fead45d4ed873805d6026124ccb6793b6fb93a490b78ddf"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:004d6ef1b5f724480f05c0bdc904bf8c78c43d633c537d99abe51b52ce0cadeb"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9dd257072c86eb9b36791b3674a513a215ba76bbdd38fc228f0e8c6dc5ce3524"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:a8cca551317ed26e17d13b6ee27b2bd62f5fe9b3842b4e88389deb984f995848"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:a7ac3b4f837c693142f6688b629d1f6408f6ab250d927159b572555f5339fe25"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win32.whl", hash = "sha256:95feec33388e2a8f72c360a68efe6f0bfed9c771e94d21b7f2359d0010f60219"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win_amd64.whl", hash = "sha256:50a31d035193ebe7154181eac84734e25bdcdb36adba849d3b2adf1c3b0c382b"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-linux_armv7l.whl", hash = "sha256:9ecb7c2e5da052a3feaeaa83d8f2a946a8feec8a50751b0e6175da982b49ebb1"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:3c52164f2b9d41c6d75464bb45f45737dcb421e92e98d85d94fda100c67a24d8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_aarch64.whl", hash = "sha256:471f58b919767290260d427dd9b760796e6208ee5fcda2f76bb8bd585ff842ec"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:72c6bcdf38f672721c093c92b1fb1f9a02a365acc5bd42e1c69fe6e904b26081"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:833b1eb9c03d28a798294523f75294055eff78fa897adf797876337b901afeb9"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_i686.whl", hash = "sha256:1db92ad6ade1946fc5705eb04956fcfdb3a0a4682de8dc3fce31cb97b6e4fcb8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:38128310ded818e1044c0cd0979d76f7c0d3c3946a526a8aa39cd258624c3bf3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win32.whl", hash = "sha256:db57930dc20ab678311727883bdb9f122daf06c14f3fd3067c9ccedb7eb056c3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win_amd64.whl", hash = "sha256:7de44d8d3bb920a4973a559f2950d03382fa4aed4880306416ffa73d24838477"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:793896648734aad3ad8f26795dcdd6040aecd35efef43fcbb67d221373e6379a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:941418cba6a8adfcac3ff7ff3bdef00b55a44d673634c15bddcfa7778e49239e"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:0d63ff6be6f3d0294249fc7a21f26f06c9cc209130c5328907cd678406d7d232"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:af80ced3ba49377ef7bec93e9ccbfa357875460e9a624ed12d9a7d5348741a76"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e3c3fbb4a6d10764295540579492397bc7a3334e1a92dd17a4bc7b69159cf70a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:a05c10fb783f609d16e1f754ebad9bb432a1adbfc46139d154e8fd6b15f59988"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:ea8af001f08c678ab59e2bf2614d8b09d62210e540f7af1129c172fe4fd330c7"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win32.whl", hash = "sha256:004d329aee385fa874979196e5359a967c370d31813f61eba88043ccaa2e06d8"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win_amd64.whl", hash = "sha256:fc43593bd051abb73a5d130fc041923144089ac459fb01165960106ebb686fd0"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:d285c036ddfc2618c4db60b584409dd8313d41473bd46177c763ea22ed9aeb1f"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:623fdad489447e1565d0ba5a818d54b4e74cd73800b6a32c4c009601c7f7a36c"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:24536af8a5f8e532fbd996c1763eff51526d1d1563f9499ff5ffffb9a08811f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bd64a9a8eb675dd2aa59cb4b2ab025a3b02ae1bb9e483c7fb518ffa0f0755cda"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f94378bc90fb008b0a56237748aa42c787fd86c392e7df3d65f0fe7fcd93844a"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:d0f39a9d860a6768574cd77b5d9ad81513fa1c575d3a050d4e72e6d79dcd62f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:c578f1306bfd0dd0668e24f8c04d61529928de2660217022a947a56be177bc2d"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win32.whl", hash = "sha256:0c2cf8d09bdc05e0550ad413e0bc0d552500bb7f98d36079b7b9d38e064e02f7"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win_amd64.whl", hash = "sha256:cc570bcd9c9681bb011f746ea90cc50559be629227aaaaae9fde8549525f0287"},
    {file = "grpcio_tools-1.67.0.tar.gz", hash = "sha256:181b3d4e61b83142c182ec366f3079b0023509743986e54c9465ca38cac255f8"},
]

[package.dependencies]
grpcio = ">=1.67.0"
protobuf = ">=5.26.1,<6.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.75.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.9"
groups = ["main"]
markers = "python_version >= \"3.14\""
files = [
    {file = "grpcio_tools-1.75.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:ae0f04d5ec8b8e13476bf516a08fc1de4e58c6bf79f99123a6b964ca7d02c790"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:24a881ad7292e904fc256892b647da17d9137ef2e72faf8b7c8e515314ad1377"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1b5810ace274dba12ecfac69ac32c8047c6ee0200a23274cb4885ed4187271f8"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:ab33993288b97b1180e092fa447a8ce00fbc8c59d67b23553245b88d14fe36bb"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4cac693621043ef11d3ab2318e811d919779f8cd5011ba8e37f44c178c831d94"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:a09cd5d267b296af67116fe098633ad770bc8c19831a5f3c896f65fad90c1064"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:dff4bcb4d16cf9ef745c1984394ed15187e6c23d73d71377377deaf443d11358"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:16d5986b37e2a9203f85e456c7ff8705b932718021d408adfe4a79e0f4d95949"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win32.whl", hash = "sha256:3fbac14998bfadc6b9140b6339dbc5f673700ebb4d45ba0c4d4fbe0ffb8559a9"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win_amd64.whl", hash = "sha256:b56e495844eb899de721eb77d9e077192bdeb40842f598481d32a8f6de3db124"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:f0635231feb70a9d551452829943a1a5fa651283e7a300aadc22df5ea5da696f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:626293296ef7e2d87ab1a80b81a55eef91883c65b59a97576099a28b9535100b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:071339d90f1faab332ce4919c815a10b9c3ed2c09473f550f686bf9cc148579f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:44195f58c052fa935b78c7438c85cbcd4b273dd685028e4f6d4d7b30d47daad1"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:860fafdb85726029d646c99859ff7bdca5aae61b5ff038c3bd355fc1ec6b2764"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:4559547a0cb3d3db1b982eea87d4656036339b400f48127fef932210672fb59e"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:9af65a310807d7f36a8f7cddea142fe97d6dffba74444f38870272f2e5a3a06b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:8c1de31aefc0585d2f915a7cd0994d153547495b8d79c44c58048a3ede0b65be"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win32.whl", hash = "sha256:efaf95fcaa5d3ac1bcfe44ceed9e2512eb95b5c8c476569bdbbe2bee4b59c8a9"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win_amd64.whl", hash = "sha256:7cefe76fc35c825f0148d60d2294a527053d0f5dd6a60352419214a8c53223c9"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:49b68936cf212052eeafa50b824e17731b78d15016b235d36e0d32199000b14c"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:08cb6e568e58b76a2178ad3b453845ff057131fff00f634d7e15dcd015cd455b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:168402ad29a249092673079cf46266936ec2fb18d4f854d96e9c5fa5708efa39"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:bbae11c29fcf450730f021bfc14b12279f2f985e2e493ccc2f133108728261db"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:38c6c7d5d4800f636ee691cd073db1606d1a6a76424ca75c9b709436c9c20439"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:626f6a61a8f141dde9a657775854d1c0d99509f9a2762b82aa401a635f6ec73d"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:f61a8334ae38d4f98c744a732b89527e5af339d17180e25fff0676060f8709b7"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:bd0c3fb40d89a1e24a41974e77c7331e80396ab7cde39bc396a13d6b5e2a750b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win32.whl", hash = "sha256:004bc5327593eea48abd03be3188e757c3ca0039079587a6aac24275127cac20"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win_amd64.whl", hash = "sha256:23952692160b5fe7900653dfdc9858dc78c2c42e15c27e19ee780c8917ba6028"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:ca9e116aab0ecf4365fc2980f2e8ae1b22273c3847328b9a8e05cbd14345b397"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:9fe87a926b65eb7f41f8738b6d03677cc43185ff77a9d9b201bdb2f673f3fa1e"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:45503a6094f91b3fd31c3d9adef26ac514f102086e2a37de797e220a6791ee87"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:b01b60b3de67be531a39fd869d7613fa8f178aff38c05e4d8bc2fc530fa58cb5"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:09e2b9b9488735514777d44c1e4eda813122d2c87aad219f98d5d49b359a8eab"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:55e60300e62b220fabe6f062fe69f143abaeff3335f79b22b56d86254f3c3c80"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:49ce00fcc6facbbf52bf376e55b8e08810cecd03dab0b3a2986d73117c6f6ee4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:71e95479aea868f8c8014d9dc4267f26ee75388a0d8a552e1648cfa0b53d24b4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win32.whl", hash = "sha256:fff9d2297416eae8861e53154ccf70a19994e5935e6c8f58ebf431f81cbd8d12"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win_amd64.whl", hash = "sha256:1849ddd508143eb48791e81d42ddc924c554d1b4900e06775a927573a8d4267f"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:f281b594489184b1f9a337cdfed1fc1ddb8428f41c4b4023de81527e90b38e1e"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:becf8332f391abc62bf4eea488b63be063d76a7cf2ef00b2e36c617d9ee9216b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a08330f24e5cd7b39541882a95a8ba04ffb4df79e2984aa0cd01ed26dcdccf49"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:6bf3742bd8f102630072ed317d1496f31c454cd85ad19d37a68bd85bf9d5f8b9"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:f26028949474feb380460ce52d9d090d00023940c65236294a66c42ac5850e8b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:1bd68fb98bf08f11b6c3210834a14eefe585bad959bdba38e78b4ae3b04ba5bd"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f1496e21586193da62c3a73cd16f9c63c5b3efd68ff06dab96dbdfefa90d40bf"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:14a78b1e36310cdb3516cdf9ee2726107875e0b247e2439d62fc8dc38cf793c1"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win32.whl", hash = "sha256:0e6f916daf222002fb98f9a6f22de0751959e7e76a24941985cc8e43cea77b50"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win_amd64.whl", hash = "sha256:878c3b362264588c45eba57ce088755f8b2b54893d41cc4a68cdeea62996da5c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:eca28a90020fc1596f48cf51b02e56bc3d285f7f9ebaf0493144160d69c2cae7"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-macosx_11_0_universal2.whl", hash = "sha256:6744a14983f82e04cfd799ed779d06ee92035bb497f2d0fa84e81921a6c9c985"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:2a59120f17d36de6e16a058d88f2fcd255bafaccb487fea0613860a5287f77c6"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:02b0c237882e45247570afdc34717ce80831184882186ef47afca9f8cac2f71c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4999ada9721ce2a0eae66bf7f2793bc6fe7a473eef4e38bb542d1e5c6d9f7d91"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:dd13f0d87605eb34f8b8868e3ad9202b90e9e58417276db79c3298538d0d60e3"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9555db0d2eb22850b7e9a27c0476627d483c114fcdf40d29b03aef446f5e4c43"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a35800ce3ecea4aaad511bc18daccd37b1560132694f30b606f2044f1242c9a0"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win32.whl", hash = "sha256:8e7f2c1a37a5c8db92c5cba4034c370598f7458b275606f7a2a114f8c25c0326"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win_amd64.whl", hash = "sha256:0de3a82ee33d960f117ab66da51254cccd8bda9118d11ec3379f954cfbf6bc39"},
    {file = "grpcio_tools-1.75.1.tar.gz", hash = "sha256:bb78960cf3d58941e1fec70cbdaccf255918beed13c34112a6915a6d8facebd1"},
]

[package.dependencies]
grpcio = ">=1.75.1"
protobuf = ">=6.31.1,<7.0.0"
setuptools = "*"

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "isort"
version = "8.0.1"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["lint"]
files = [
    {file = "isort-8.0.1-py3-none-any.whl", hash = "sha256:28b89bc70f751b559aeca209e6120393d43fbe2490de0559662be7a9787e3d75"},
    {file = "isort-8.0.1.tar.gz", hash = "sha256:171ac4ff559cdc060bcfff550bc8404a486fee0caab245679c2abe7cb253c78d"},
]

[package.extras]
colors = ["colorama"]

[[package]]
name = "librt"
version = "0.11.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.11.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:6e94ebfcfa2d5e9926d6c3b9aa4617ffc42a845b4321fb84021b872358c82a0f"},
    {file = "librt-0.11.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:ae627397a2f351560440d872d6f7c8dbb4072e57868e7b2fc5b8b430fe489d45"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:dc329359321b67d24efdf4bc69012b0597001649544db662c001db5a0184794c"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:7e82e642ab0f7608ce2fe53d76ca2280a9ee33a1b06556142c7c6fe80a86fc33"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:88145c15c67731d54283d135b03244028c750cc9edc334a96a4f5950ebdb2884"},
    {file = "librt-0.11.0-cp310-cp310-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9d36a51b3d93320b686588e27123f4995804dbf1bce81df78c02fc3c6eea9280"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d00f3ac06a2a8b246327f11e186a53a100a4d5c7ed52346367e5ec751d51586c"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:461bbceede621f1ffb8839755f8663e886087ee7af16294cab7fb4d782c62eeb"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0cad8a4d6a8ff03c9b76f9414caccd78e7cfbc8a2e12fa334d8e1d9932753783"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f37aa505b3cf60701562eddb32df74b12a9e380c207fd8b06dd157a943ac7ea0"},
    {file = "librt-0.11.0-cp310-cp310-win32.whl", hash = "sha256:94663a21534637f0e787ec2a2a756022df6e5b7b2335a5cdd7d8e33d68a2af89"},
    {file = "librt-0.11.0-cp310-cp310-win_amd64.whl", hash = "sha256:dec7db73758c2b54953fd8b7fe348c45188fe26b39ee18446196edd08453a5d4"},
    {file = "librt-0.11.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:93d95bd45b7d58343d8b90d904450a545144eec19a002511163426f8ab1fae29"},
    {file = "librt-0.11.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ee278c769a713638cdacd4c0436d72156e75df3ebc0166ab2b9dc43acc386c9"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f230cb1cbc9faaa616f9a678f530ebcf186e414b6bcbd88b960e4ba1b92428d5"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:5d63c855d86938d9de93e265c9bd8c705b51ec494de5738340ee93767a686e4b"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:993f028be9e96a08d31df3479ac80d99be374d17f3b78e4796b3fd3c913d4e89"},
    {file = "librt-0.11.0-cp311-cp311-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:258d73a0aa66a055e65b2e4d1b8cdb23b9d132c5bb915d9547d804fcaed116cc"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0827efe7854718f04aaddf6496e96960a956e676fe1d0f04eb41511fd8ad06d5"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:7753e57d6e12d019c0d8786f1c09c709f4c3fcc57c3887b24e36e6c06ec938b7"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:11bd19822431cc21af9f27374e7ae2e58103c7d98bda823536a6c47f6bb2bb3d"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:22bdf239b219d3993761a148ffa134b19e52e9989c84f845d5d7b71d70a17412"},
    {file = "librt-0.11.0-cp311-cp311-win32.whl", hash = "sha256:46c60b61e308eb535fbd6fa622b1ee1bb2815691c1ad9c98bf7b84952ec3bc8d"},
    {file = "librt-0.11.0-cp311-cp311-win_amd64.whl", hash = "sha256:902e546ff044f579ff1c953ff5fce97b636fe9e3943996b2177710c6ef076f73"},
    {file = "librt-0.11.0-cp311-cp311-win_arm64.whl", hash = "sha256:65ac3bc20f78aa0ee5ae84baa68917f89fef4af63e941084dd019a0d0e749f0c"},
    {file = "librt-0.11.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b87504f1690a23b9a2cca841191a04f83895d4fc2dd04df91d82b1a04ca2ad46"},
    {file = "librt-0.11.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:40071fc5fe0ce8daa6de616702314a01e1250711682b0523d6ab8d4525910cb3"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:137e79445c896a0ea7b265f52d23954e05b64222ee1af69e2cb34219067cbb67"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:cca6644054e78746d8d4ef238681f9c34ff8b584fe6b988ecebb8db3b15e622a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5b0eea49f5562861ee8d757a32ef7d559c1d35be2aaaa1ec28941d74c9ffc8a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0d1029d7e1ae1a7e647ed6fb5df8c4ce2dffefb7a9f5fd1376a4554d96dac09f"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:bc3ce6b33c5828d9e80592011a5c584cb2ce86edbc4088405f70da47dc1d1b3b"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:936c5995f3514a42111f20099397d8177c79b4d7e70961e396c6f5a0a3566766"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:9bc0ca6ad9381cbe8e4aa6e5726e4c80c78115a6e9723c599ed1d73e092bc49d"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:070aa8c26c0a74774317a72df8851facc7f0f012a5b406557ac56992d92e1ec8"},
    {file = "librt-0.11.0-cp312-cp312-win32.whl", hash = "sha256:6bf14feb84b05ae945277395451998c89c54d0def4070eb5c08de544930b245a"},
    {file = "librt-0.11.0-cp312-cp312-win_amd64.whl", hash = "sha256:75672f0bc524ede266287d532d7923dbce94c7514ad07627bac3d0c6d92cc4d9"},
    {file = "librt-0.11.0-cp312-cp312-win_arm64.whl", hash = "sha256:2f10cf143e4a9bb0f4f5af568a00df94a2d69ef41c2579584454bb0fe5cc642c"},
    {file = "librt-0.11.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:78dc31f7fdfe9c9d0eb0e8f42d139db230e826415bbcabd9f0e9faaaee909894"},
    {file = "librt-0.11.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:fa475675db22290c3158e1d42326d0f5a65f04f44a0e68c3630a25b53560fb9c"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:621db29691044bdeda22e789e482e1b0f3a985d90e3426c9c6d17606416205ea"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:a9010e2ed5b3a9e158c5fd966b3ab7e834bb3d3aacc8f66c91dd4b57a3799230"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7c39513d8b7477a2e1ed8c43fc21c524e8d5a0f8d4e8b7b074dbdbe7820a08e2"},
    {file = "librt-0.11.0-cp313-cp313-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7aef3cf1d5af86e770ab04bfd993dfc4ae8b8c17f66fb77dd4a7d50de7bbb1a3"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:557183ddc36babe46b27dd60facbd5adb4492181a5be887587d57cda6e092f21"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:83d3e1f72bd42f6c5c0b7daec530c3f829bd02db42c70b8ddf0c2d90a2459930"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:4ce1f21fbe589bc1afd7872dece84fb0e1144f794a288e58a10d2c54a55c43be"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b09f7044ea2b64c9da42fd3d335666518cfd1c6e8a182c95da73d0214b41e"},
    {file = "librt-0.11.0-cp313-cp313-win32.whl", hash = "sha256:78fddc31cd4d3caa897ad5d31f856b1faadc9474021ad6cb182b9018793e254e"},
    {file = "librt-0.11.0-cp313-cp313-win_amd64.whl", hash = "sha256:8ca8aa88751a775870b764e93bad5135385f563cb8dcee399abf034ea4d3cb47"},
    {file = "librt-0.11.0-cp313-cp313-win_arm64.whl", hash = "sha256:96f044bb325fd9cf1a723015638c219e9143f0dfbc0ca54c565df2b7fc748b44"},
    {file = "librt-0.11.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:4a017a95e5837dc15a8c5661d60e05daa96b90908b1aa6b7acdf443cd25c8ebd"},
    {file = "librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:b1ecbd9819deccc39b7542bf4d2a740d8a620694d39989e58661d3763458f8d4"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7da327dacd7be8f8ec36547373550744a3cc0e536d54665cd83f8bcd961200e8"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:0dc56b1f8d06e60db362cc3fdae206681817f86ce4725d34511473487f12a34b"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:05fb8fb2ab90e21c8d12ea240d744ad514da9baf381ebfa70d91d20d21713175"},
    {file = "librt-0.11.0-cp314-cp314-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cae74872be221df4374d10fec61f93ed1513b9546ea84f2c0bf73ab3e9bd0b03"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:32bcc918c0148eb7e3d57385125bac7e5f9e4359d05f07448b09f6f778c2f31c"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f9743fc99135d5f78d2454435615f6dec0473ca507c26ce9d92b10b562a280d3"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:5ba067f4aadae8fda802d91d2124c90c42195ff32d9161d3549e6d05cfe26f96"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:de3bf945454d032f9e390b85c4072e0a0570bf825421c8be0e71209fa65e1abe"},
    {file = "librt-0.11.0-cp314-cp314-win32.whl", hash = "sha256:d2277a05f6dcb9fd13db9566aac4fabd68c3ea1ea46ee5567d4eef8efa495a2f"},
    {file = "librt-0.11.0-cp314-cp314-win_amd64.whl", hash = "sha256:ab73e8db5e3f564d812c1f5c3a175930a5f9bc96ccb5e3b22a34d7858b401cf7"},
    {file = "librt-0.11.0-cp314-cp314-win_arm64.whl", hash = "sha256:aea3caa317752e3a466fa8af45d91ee0ea8c7fdd96e42b0a8dd9b76a7931eba1"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:d1b36540d7aaf9b9101b3a6f376c8d8e9f7a9aec93ed05918f2c69d493ffef72"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:efbb343ab2ce3540f4ecbe6315d677ed70f37cd9a72b1e58066c918ca83acbaa"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:aa0dd688aab3f7914d3e6e5e3554978e0383312fb8e771d84be008a35b9ee548"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:f5fb36b8c6c63fdcbb1d526d94c0d1331610d43f4118cc1beb4efef4f3faacb2"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4a9a237d13addb93715b6fee74023d5ee3469b53fce527626c0e088aa585805f"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5ddd17bd87b2c56ddd60e546a7984a2e64c4e8eab92fb4cf3830a48ad5469d51"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:bd43992b4473d42f12ff9e68326079f0696d9d4e6000e8f39a0238d482ba6ee2"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:f8e3e8056dd674e279741485e2e512d6e9a751c7455809d0114e6ebf8d781085"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:c1f708d8ae9c56cf38a903c44297243d2ec83fd82b396b977e0144a3e76217e3"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0add982e0e7b9fc14cf4b33789d5f13f66581889b88c2f58099f6ce8f92617bd"},
    {file = "librt-0.11.0-cp314-cp314t-win32.whl", hash = "sha256:2b481d846ac894c4e8403c5fd0e87c5d11d6499e404b474602508a224ff531c8"},
    {file = "librt-0.11.0-cp314-cp314t-win_amd64.whl", hash = "sha256:28edb433edde181112a908c78907af28f964eabc15f4dd16c9d66c834302677c"},
    {file = "librt-0.11.0-cp314-cp314t-win_arm64.whl", hash = "sha256:dee008f20b542e3cd162ba338a7f9ec0f6d23d395f66fe8aeeec3c9d067ea253"},
    {file = "librt-0.11.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6bd72d903911d995ab666dbd1871f8b1e80925a699af8063fbf50053329fb05f"},
    {file = "librt-0.11.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0ef69ac715f3cd8e5cd252cb2aebfa72c015492aacc339d5d7bf8fef3c62c677"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:624a40c4a4ad7773315c287276cd024509b2c66ff5904f504bfc08d2c70293ab"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:41dc19fe150b69716c8ece4f76773a9e8813fe3e35e032a58b4d46423fb8d7c0"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4e8bd98ea9c47ae90b319a087ab28dac493f1ffbc1ecd1f28fcdbf3b7e1108d1"},
    {file = "librt-0.11.0-cp39-cp39-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:84308fc49423ce6475d1c5d1985cd69a8ca9f0325fc7d5f81bb690a3f3625d4e"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:ff0fbaf5f44a21beeb0110f2ab64f45135a9536a834b79c0d1ef018f2786bbfa"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9c028a9442a18e266955d364ce42259136e79a7ba14d773e0d778d5f70cd56f1"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:9f1692105a02bcf853f355032a5fdc5494358ef83d8fd22d16de375c85cec3f5"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7a80a71e1fda83cc752a9141e87aae7fef279538597564d670e9ce513f286192"},
    {file = "librt-0.11.0-cp39-cp39-win32.whl", hash = "sha256:140695816ddf3c86eb972981a26f35efd871c44b0c3aed44c8cd01749386617f"},
    {file = "librt-0.11.0-cp39-cp39-win_amd64.whl", hash = "sha256:92f7ff819c197fc30473190a12c2856f325ac90aabfccbeb2072d28cc2e234e3"},
    {file = "librt-0.11.0.tar.gz", hash = "sha256:075dc3ef4458a278e0195cbf6ac9d38808d9b906c5a6c7f7f79c3888276a3fb1"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mypy"
version = "2.1.0"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "mypy-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:11a6beb180257a805961aea9ec591bbd0bd17f1e18d35b8456d57aee5bedfedc"},
    {file = "mypy-2.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8ef78c1d306bbf9a8a12f526c44902c9c28dffd6c52c52bf6a72641ce18d3849"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c209a90853081ff01d01ee895cafe10f7db1474e0d95beaeef0f6c1db9119bbd"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:47cebf61abde7c088a4e27718a8b13a81655686b2e9c251f5c0915a802248166"},
    {file = "mypy-2.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:d57a90ae5e872138a425ec328edbc9b235d1934c4377881a33ec05b341acc9a8"},
    {file = "mypy-2.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:aea7f7a8a55b459c34275fc468ada6ca7c173a5e43a68f5dbe588a563d8a06b8"},
    {file = "mypy-2.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:c989640253f0d76843e9c6c1bbf4bd48c5e85ada61bde4beb37cb3eca035685e"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a683016b16fe2f572dc04c72be7ee0504ac1605a265d0200f5cea695fb788f41"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a293c534adb55271fef24a26da04b855540a8c13cc07bc5917b9fd2c394f2ca"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7406f4d048e71e576f5356d317e5b0a9e666dfd966bd99f9d14ca06e1a341538"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0210d626fc8b31ccc90233754c7bc90e1f43205e85d96387f7db1285b55c398"},
    {file = "mypy-2.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3712c20deed54e814eaaa825603bada8ea1c390670a397c95b98405347acc563"},
    {file = "mypy-2.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fcaa0e479066e31f7cceb6a3bea39cb22b2ff51a6b2f24f193d19179ba17c389"},
    {file = "mypy-2.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:0b1a5260c95aa443083f9ed3592662941951bca3d4ca224a5dc517c38b7cf666"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:244358bf1c0da7722230bce60683d52e8e9fd030554926f15b747a84efb5b3af"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4ec7c57657493c7a75534df2751c8ae2cda383c16ecc55d2106c54476b1b16f6"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8161b6ff4392410023224f0969d17db93e1e154bc3e4ba62598e720723ae211"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bf03e12003084a67395184d3eb8cbd6a489dc3655b5664b28c210a9e2403ab0b"},
    {file = "mypy-2.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:20509760fd791c51579d573153407d226385ec1f8bcce55d730b354f3336bc22"},
    {file = "mypy-2.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:6753d0c1fdd6b1a23b9e4f283ce80b2153b724adcb2653b20b85a8a28ac6436b"},
    {file = "mypy-2.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:98ebb6589bb3b6d0c6f0c459d53ca55b8091fbc13d277c4041c885392e8195e8"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:35aac3bb114e03888f535d5eb51b8bafbb3266586b599da1940f9b1be3ec5bd5"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8de55a8c861f2a49331f807be98d90caeceeef520bde13d43a160207f8af613e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5fdf2941a07434af755837d9880f7d7d25f1dacb1af9dcd4b9b66f2220a3024e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e195b817c13f02352a9c124301f9f30f078405444679b6753c1b96b6eed37285"},
    {file = "mypy-2.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5431d42af987ebd92ba2f71d45c85ed41d8e6ca9f5fd209a69f68f707d2469e5"},
    {file = "mypy-2.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:767fe8c66dc3e01e19e1737d4c38ebefead16125e1b8e58ad421903b376f5c65"},
    {file = "mypy-2.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:ecfe70d43775ab99562ab128ce49854a362044c9f894961f68f898c23cb7429d"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:7354c5a7f69d9345c3d6e69921d57088eea3ddeeb6b20d34c1b3855b02c36ec2"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:49890d4f76ac9e06ec117f9e09f3174da70a620a0c300953d8595c926e80947f"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:761be68e023ef5d94678772396a8af1220030f80837a3afd8d0aef3b419666f4"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c90345fc182dc363b891350457ec69c35140858538f38b4540845afcc32b1aef"},
    {file = "mypy-2.1.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b84802e7b5a6daf1f5e15bc9fcd7ddae77be13981ffab037f1c67bb84d67d135"},
    {file = "mypy-2.1.0-cp314-cp314-win_amd64.whl", hash = "sha256:022c771234936ceac541ebaf836fe9e2abeb3f5e09aff21588fe543ff006fe21"},
    {file = "mypy-2.1.0-cp314-cp314-win_arm64.whl", hash = "sha256:498207db725cec88829a6a5c2fc771205fd043719ef98bc49aba8fb9fc4e6d57"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:7d5e5cad0efeba72b93cd17490cc0d69c5ac9ca132994fe3fb0314808aeeb83e"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ff715050c127d724fd260a2e666e7747fdd83511c0c47d449d98238970aef780"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:82208da9e09414d520e912d3e462d454854bed0810b71540bb016dcbca7308fd"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e79ebc1b904b84f0310dff7469655a9c36c7a68bddb37bdd42b67a332df61d08"},
    {file = "mypy-2.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e583edc957cfb0deb142079162ae826f58449b116c1d442f2d91c69d9fced081"},
    {file = "mypy-2.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b33b6cd332695bba180d55e717a79d3038e479a2c49cc5eb3d53603409b9a5d7"},
    {file = "mypy-2.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:4f910fe825376a7b66ef7ca8c98e5a149e8cd64c19ae71d84047a74ee060d4e6"},
    {file = "mypy-2.1.0-py3-none-any.whl", hash = "sha256:a663814603a5c563fb87a4f96fb473eeb30d1f5a4885afcf44f9db000a366289"},
    {file = "mypy-2.1.0.tar.gz", hash = "sha256:81e76ad12c2d804512e9b13240d1588316531bfba07558286078bfbce9613633"},
]

[package.dependencies]
ast-serialize = ">=0.3.0,<1.0.0"
librt = {version = ">=0.11.0", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=1.0.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = [
    {version = ">=4.6.0", markers = "python_version < \"3.15\""},
    {version = ">=4.14.0", markers = "python_version >= \"3.15\""},
]

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
reports = ["lxml"]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "ni-datamonikers-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI data moniker gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_datamonikers_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:77d078d810656b3e90152a065047c6203140e0998e8cbdf9d2dbb6e9f477840e"},
    {file = "ni_datamonikers_v1_proto-1.0.0.tar.gz", hash = "sha256:2e4cf30f9dee343af4a5f328fb785320d2eb30705abc15f0695057177afd5f00"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-datastore"
version = "2.0.0.dev1"
description = "APIs for publishing and retrieving data from NI Measurement Data Services"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_datastore-2.0.0.dev1-py3-none-any.whl", hash = "sha256:31236c2ad091b11617553cec93671a4d8c45fca9e9364583092bd6b19ca716fc"},
    {file = "ni_datastore-2.0.0.dev1.tar.gz", hash = "sha256:254437977771517a379c1327958364cbda6cd3ad2a6cb2c28d42d145b0b9923e"},
]

[package.dependencies]
hightime = ">=1.0.0"
ni-measurements-data-v1-client = ">=1.1.0"
ni-measurements-metadata-v1-client = ">=1.0.0"
ni-protobuf-types = ">=1.2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-data-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Data Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:dfc38d56fdd710a930fbc05383d43ab96f64aee545937f9ef605a3bb6f88cc31"},
    {file = "ni_measurements_data_v1_client-1.1.0.tar.gz", hash = "sha256:16b1ac8b82277e41719aa8b1aeae3f1040dba47e63651f83e30fe115cd036278"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-data-v1-proto = ">=1.1.0"

[[package]]
name = "ni-measurements-data-v1-proto"
version = "1.1.0"
description = "Protobuf data types and service stubs for NI data store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:06096cea733717b60281c92d0a1b44eac97194781507ba4fd9b3aa080a4450df"},
    {file = "ni_measurements_data_v1_proto-1.1.0.tar.gz", hash = "sha256:df1ca7ce3603dd5a0adc8795f0844da9a78ddc026f219bf596957cf3ed08da3d"},
]

[package.dependencies]
ni-datamonikers-v1-proto = ">=1.0.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"
ni-protobuf-types = ">=1.2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-metadata-v1-client"
version = "1.0.0"
description = "gRPC Client for NI Metadata Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_client-1.0.0-py3-none-any.whl", hash = "sha256:c697ce4e98105b810f4da844a598e86e359ff6c90ca7a832e1e23a70327551a7"},
    {file = "ni_measurements_metadata_v1_client-1.0.0.tar.gz", hash = "sha256:9f9a10810c4c6693239081abbc026414a18df3e3d04daa3cd59010b1eed07f51"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"

[[package]]
name = "ni-measurements-metadata-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI metadata store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:8844806d6775ac65144100fcd03099aea0c17ed55de696683d0663166f45cee3"},
    {file = "ni_measurements_metadata_v1_proto-1.0.0.tar.gz", hash = "sha256:3283cf7f0c452812a311b2b9274b5ba1e549f994f6a978a125f1746b85746e6f"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.2.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_protobuf_types-1.2.0-py3-none-any.whl", hash = "sha256:461c4825571d0054fd5427664403c3d69fcd180c9c00868ac1911693dd9bf901"},
    {file = "ni_protobuf_types-1.2.0.tar.gz", hash = "sha256:e8226f8ef44b104ffb1b1f6e416511c416be4d91bf5c2633db7ab58294e037bb"},
]

[package.dependencies]
nitypes = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["lint"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "nitypes"
version = "1.1.0"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "nitypes-1.1.0-py3-none-any.whl", hash = "sha256:b43ac7027e1cceeca7ceffa58f31ffadd03feeb1788ca5cb8f9d105e73893b14"},
    {file = "nitypes-1.1.0.tar.gz", hash = "sha256:f273b5131ef0d5b848c37a0a63452626caf5c2938f7744c324f7991b76fa0b60"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main"]
markers = "python_version < \"3.12\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.5.0"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.12"
groups = ["main"]
markers = "python_version >= \"3.12\""
files = [
    {file = "numpy-2.5.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:489780423903667933b4ed6197b6ec3b75ea5dd17d1d8f0f38d798feb6921561"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ece55976ced6bca95a03ae2839e2e5ccffe8eb6a3e7022415645eb154a81e4e6"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:c83b664b0e6eee9594fa920cf0639d8af796606d3fad6cc70180c87e4b97c7be"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:bf80333980bf37f523341ddd72c783f39d6829ec7736b9eb99086388a2d52cc2"},
    {file = "numpy-2.5.0-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a1a4874217b36d5ac8fc876f52e39df56f8182c88463e9e2dceabf7ca8b7efb8"},
    {file = "numpy-2.5.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:aaa760137137e8d3c920d27927748215b56014f92667dc9b6c27dfc61249255a"},
    {file = "numpy-2.5.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:7174ce8265fc7f7417d171c9ea8fe905220748893ea67a2a7abe726ec331c4b0"},
    {file = "numpy-2.5.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b8c3daaf99de52415d20b42f8e8155c78642cb04207d02f9d317a0dcf1b3fb54"},
    {file = "numpy-2.5.0-cp312-cp312-win32.whl", hash = "sha256:6206db0af545d73d068add6d992279145f158428d1da6cc49adc4b630c5d6ee5"},
    {file = "numpy-2.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:6f2d6873e2940c860a309d21e25b1e69af6aaffdd80aa056b04c16380db1c4f2"},
    {file = "numpy-2.5.0-cp312-cp312-win_arm64.whl", hash = "sha256:a55e1eb2bca2cfd17a16b213c99dfc8502d47b0d494224d2122277d0400935ca"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:520e6b8be0a4b65840ac8090d4f51cef4bed66e2b0894d5a520f099adc24a9b2"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:146b81cdd3967fdb6beca8ba25f00c58741d8f3cbd797f55af0fbe0bfec3469c"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:126b88d95e8ff9b00c9e717aa540469f21d6180162f84c0caec51b16215d49cd"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:d4313cef1594c5ce46c31b6e54e918338f63f16ee9322304e8c9114d6d81c8bd"},
    {file = "numpy-2.5.0-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:750fb097caf26fa878746d9d119f6f9da12dedcbff1eea966c3e3447647c4a9e"},
    {file = "numpy-2.5.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3893adc2dc7c0412ba76777db55a049215d99c9aa3113003be8f49f4f1290ab9"},
    {file = "numpy-2.5.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:835e454dd99b238cdc5a3f63bce2371296f5ebc53ca1e0f8e6ddbb6d92a29aab"},
    {file = "numpy-2.5.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6f9836778081a0a3c02a6a21493f3e9f5b311f8d2541934f31f05583dc999ea4"},
    {file = "numpy-2.5.0-cp313-cp313-win32.whl", hash = "sha256:0b525be4744b60bb0557ac872d53ef07d085b5f39622bc579c98d3809d05b988"},
    {file = "numpy-2.5.0-cp313-cp313-win_amd64.whl", hash = "sha256:44353e2878930039db472b99dc353d749826e4010bd4d2a7f835e94a97a5c748"},
    {file = "numpy-2.5.0-cp313-cp313-win_arm64.whl", hash = "sha256:48f54b00711f83a5f796b70c518e8c2b3c5848dda03a54911f23eb68519b9b60"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:f27582c55ba4c750b7c58c8faf021d2cd9324a662b466229db8a417b41368af9"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:28e7137057d551e4a83c4ae414e3451f50568409db7569aacc7f9811ee06a446"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:e1da54b53e75cd9fcfc23efcc7edab2c6aecf97b6037566d8a0fe804af8ec57c"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:694d8f74e156f7fd01179f1aa8faa2f648ab6ae0f70b6c3fe57a03249aea2303"},
    {file = "numpy-2.5.0-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1a7569a7b53c77716f036bb28cb1c91f166a26ec7d9502cd1e4bdfe502fdec22"},
    {file = "numpy-2.5.0-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:39a0433bd4086ebd462960cf375e19195bb07b53dc1d87dd5fcf47ad78576f03"},
    {file = "numpy-2.5.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:929f0c79ac38bcbd7154fe631dc907abfeddbcc5027a896bd1f7767323271e7a"},
    {file = "numpy-2.5.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:cc4f247a47bbf070bfd70be53ccdcf47b800af563535e7bbe172322197c30e21"},
    {file = "numpy-2.5.0-cp314-cp314-win32.whl", hash = "sha256:5dc71423499fab3f46f7a7201155ade1669ea101f2f429d332df9e72f8161731"},
    {file = "numpy-2.5.0-cp314-cp314-win_amd64.whl", hash = "sha256:ebb81d9d5443e0309d6c54894c3fbed74ad7da0714352a67b6d773cd189eae73"},
    {file = "numpy-2.5.0-cp314-cp314-win_arm64.whl", hash = "sha256:3b94d0d0deceebfad3e67ae5c0e5eb87371e8f7a0581cd04a779928c2450cf1e"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:22f3d43e362d650bc39db1f17851302874a148ca95ba6981c1dfb5fa6862f35b"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:243563efb4cd7528a264567e9fd206c87826457322521d06206a00bfa316c927"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:84881d825ca75249b189bbee875fcfe3238aa5c479e6100893cda566e8e86826"},
    {file = "numpy-2.5.0-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:cda12aa4779d42b8771180aba759c96f527d43446d8f380ab59e2b35e8489efd"},
    {file = "numpy-2.5.0-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c0121101093d2bd74981b10f8837d78e794a8ff57834eb27179f49e1ba11ac6"},
    {file = "numpy-2.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d371c92cfa09da00022f501ab67fafaea813d752eb30ac44336d45b1e5b0268a"},
    {file = "numpy-2.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:9990713e9c38154c6861e7547f1e3fc7a87e75ff09bab24ef1cc81d81c2835e9"},
    {file = "numpy-2.5.0-cp314-cp314t-win32.whl", hash = "sha256:edadfbd4794b1086c0d822f81863e8a68fc129d132fd0bb9e31e955d7fbbbdb7"},
    {file = "numpy-2.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:f7e5fa4382967ae6548bd2f174219afb908e294b0d5f625af01166edd5f7d9aa"},
    {file = "numpy-2.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:016623417bb330d719d579daf2d6b9a01ddc52e41a9ed61a47f39fde46dcd865"},
    {file = "numpy-2.5.0.tar.gz", hash = "sha256:5a129578019311b6e56bdd714250f19b518f7dceeeb8d1af5490f4942d3f891c"},
]

[[package]]
name = "packaging"
version = "26.2"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "packaging-26.2-py3-none-any.whl", hash = "sha256:5fc45236b9446107ff2415ce77c807cee2862cb6fac22b8a73826d0693b0980e"},
    {file = "packaging-26.2.tar.gz", hash = "sha256:ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"},
]

[[package]]
name = "pathspec"
version = "1.1.1"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pathspec-1.1.1-py3-none-any.whl", hash = "sha256:a00ce642f577bf7f473932318056212bc4f8bfdf53128c78bbd5af0b9b20b189"},
    {file = "pathspec-1.1.1.tar.gz", hash = "sha256:17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]

[[package]]
name = "pep8-naming"
version = "0.15.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.10.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "platformdirs-4.10.0-py3-none-any.whl", hash = "sha256:fb516cdb12eb0d857d0cd85a7c57cea4d060bee4578d6cf5a14dfdf8cbf8784a"},
    {file = "platformdirs-4.10.0.tar.gz", hash = "sha256:31e761a6a0ca04faf7353ea759bdba55652be214725111e5aac52dfa29d4bef7"},
]

[[package]]
name = "protobuf"
version = "4.25.9"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main"]
markers = "python_version <= \"3.12\""
files = [
    {file = "protobuf-4.25.9-cp310-abi3-win32.whl", hash = "sha256:bde396f568b0b46fc8fbfe9f02facf25b6755b2578a3b8ac61e74b9d69499e03"},
    {file = "protobuf-4.25.9-cp310-abi3-win_amd64.whl", hash = "sha256:3683c05154252206f7cb2d371626514b3708199d9bcf683b503dabf3a2e38e06"},
    {file = "protobuf-4.25.9-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:9560813560e6ee72c11ca8873878bdb7ee003c96a57ebb013245fe84e2540904"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_aarch64.whl", hash = "sha256:999146ef02e7fa6a692477badd1528bcd7268df211852a3df2d834ba2b480791"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl", hash = "sha256:438c636de8fb706a0de94a12a268ef1ae8f5ba5ae655a7671fcda5968ba3c9be"},
    {file = "protobuf-4.25.9-cp38-cp38-win32.whl", hash = "sha256:7f7c1abcea3fc215918fba67a2d2a80fbcccc0f84159610eb187e9bbe6f939ee"},
    {file = "protobuf-4.25.9-cp38-cp38-win_amd64.whl", hash = "sha256:79faf4e5a80b231d94dcf3a0a2917ccbacf0f586f12c9b9c91794b41b913a853"},
    {file = "protobuf-4.25.9-cp39-cp39-win32.whl", hash = "sha256:9481e80e8cffb1c492c68e7c4e6726f4ad02eebc4fa97ead7beebeaa3639511d"},
    {file = "protobuf-4.25.9-cp39-cp39-win_amd64.whl", hash = "sha256:b1d467352de666dc1b6d5740b6319d9c08cab7b21b452501e4ee5b0ac5156780"},
    {file = "protobuf-4.25.9-py3-none-any.whl", hash = "sha256:d49b615e7c935194ac161f0965699ac84df6112c378e05ec53da65d2e4cbb6d4"},
    {file = "protobuf-4.25.9.tar.gz", hash = "sha256:b0dc7e7c68de8b1ce831dacb12fb407e838edbb8b6cc0dc3a2a6b4cbf6de9cff"},
]

[[package]]
name = "protobuf"
version = "5.29.6"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main"]
markers = "python_version == \"3.13\""
files = [
    {file = "protobuf-5.29.6-cp310-abi3-win32.whl", hash = "sha256:62e8a3114992c7c647bce37dcc93647575fc52d50e48de30c6fcb28a6a291eb1"},
    {file = "protobuf-5.29.6-cp310-abi3-win_amd64.whl", hash = "sha256:7e6ad413275be172f67fdee0f43484b6de5a904cc1c3ea9804cb6fe2ff366eda"},
    {file = "protobuf-5.29.6-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:b5a169e664b4057183a34bdc424540e86eea47560f3c123a0d64de4e137f9269"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_aarch64.whl", hash = "sha256:a8866b2cff111f0f863c1b3b9e7572dc7eaea23a7fae27f6fc613304046483e6"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_x86_64.whl", hash = "sha256:e3387f44798ac1106af0233c04fb8abf543772ff241169946f698b3a9a3d3ab9"},
    {file = "protobuf-5.29.6-cp38-cp38-win32.whl", hash = "sha256:36ade6ff88212e91aef4e687a971a11d7d24d6948a66751abc1b3238648f5d05"},
    {file = "protobuf-5.29.6-cp38-cp38-win_amd64.whl", hash = "sha256:831e2da16b6cc9d8f1654c041dd594eda43391affd3c03a91bea7f7f6da106d6"},
    {file = "protobuf-5.29.6-cp39-cp39-win32.whl", hash = "sha256:cb4c86de9cd8a7f3a256b9744220d87b847371c6b2f10bde87768918ef33ba49"},
    {file = "protobuf-5.29.6-cp39-cp39-win_amd64.whl", hash = "sha256:76e07e6567f8baf827137e8d5b8204b6c7b6488bbbff1bf0a72b383f77999c18"},
    {file = "protobuf-5.29.6-py3-none-any.whl", hash = "sha256:6b9edb641441b2da9fa8f428760fc136a49cf97a52076010cf22a2ff73438a86"},
    {file = "protobuf-5.29.6.tar.gz", hash = "sha256:da9ee6a5424b6b30fd5e45c5ea663aef540ca95f9ad99d1e887e819cdf9b8723"},
]

[[package]]
name = "protobuf"
version = "6.33.6"
description = ""
optional = false
python-versions = ">=3.9"
groups = ["main"]
markers = "python_version >= \"3.14\""
files = [
    {file = "protobuf-6.33.6-cp310-abi3-win32.whl", hash = "sha256:7d29d9b65f8afef196f8334e80d6bc1d5d4adedb449971fefd3723824e6e77d3"},
    {file = "protobuf-6.33.6-cp310-abi3-win_amd64.whl", hash = "sha256:0cd27b587afca21b7cfa59a74dcbd48a50f0a6400cfb59391340ad729d91d326"},
    {file = "protobuf-6.33.6-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:9720e6961b251bde64edfdab7d500725a2af5280f3f4c87e57c0208376aa8c3a"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_aarch64.whl", hash = "sha256:e2afbae9b8e1825e3529f88d514754e094278bb95eadc0e199751cdd9a2e82a2"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_s390x.whl", hash = "sha256:c96c37eec15086b79762ed265d59ab204dabc53056e3443e702d2681f4b39ce3"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl", hash = "sha256:e9db7e292e0ab79dd108d7f1a94fe31601ce1ee3f7b79e0692043423020b0593"},
    {file = "protobuf-6.33.6-cp39-cp39-win32.whl", hash = "sha256:bd56799fb262994b2c2faa1799693c95cc2e22c62f56fb43af311cae45d26f0e"},
    {file = "protobuf-6.33.6-cp39-cp39-win_amd64.whl", hash = "sha256:f443a394af5ed23672bc6c486be138628fbe5c651ccbc536873d7da23d1868cf"},
    {file = "protobuf-6.33.6-py3-none-any.whl", hash = "sha256:77179e006c476e69bf8e8ce866640091ec42e1beb80b213c3900006ecfba6901"},
    {file = "protobuf-6.33.6.tar.gz", hash = "sha256:a6768d25248312c297558af96a9f9c929e8c4cee0659cb07e780731095f38135"},
]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3) ; python_version < \"3.11\""]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pytokens"
version = "0.4.1"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "pytokens-0.4.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2a44ed93ea23415c54f3face3b65ef2b844d96aeb3455b8a69b3df6beab6acc5"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:add8bf86b71a5d9fb5b89f023a80b791e04fba57960aa790cc6125f7f1d39dfe"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:670d286910b531c7b7e3c0b453fd8156f250adb140146d234a82219459b9640c"},
    {file = "pytokens-0.4.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4e691d7f5186bd2842c14813f79f8884bb03f5995f0575272009982c5ac6c0f7"},
    {file = "pytokens-0.4.1-cp310-cp310-win_amd64.whl", hash = "sha256:27b83ad28825978742beef057bfe406ad6ed524b2d28c252c5de7b4a6dd48fa2"},
    {file = "pytokens-0.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d70e77c55ae8380c91c0c18dea05951482e263982911fc7410b1ffd1dadd3440"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4a58d057208cb9075c144950d789511220b07636dd2e4708d5645d24de666bdc"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b49750419d300e2b5a3813cf229d4e5a4c728dae470bcc89867a9ad6f25a722d"},
    {file = "pytokens-0.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:d9907d61f15bf7261d7e775bd5d7ee4d2930e04424bab1972591918497623a16"},
    {file = "pytokens-0.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:ee44d0f85b803321710f9239f335aafe16553b39106384cef8e6de40cb4ef2f6"},
    {file = "pytokens-0.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:140709331e846b728475786df8aeb27d24f48cbcf7bcd449f8de75cae7a45083"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d6c4268598f762bc8e91f5dbf2ab2f61f7b95bdc07953b602db879b3c8c18e1"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:24afde1f53d95348b5a0eb19488661147285ca4dd7ed752bbc3e1c6242a304d1"},
    {file = "pytokens-0.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5ad948d085ed6c16413eb5fec6b3e02fa00dc29a2534f088d3302c47eb59adf9"},
    {file = "pytokens-0.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:3f901fe783e06e48e8cbdc82d631fca8f118333798193e026a50ce1b3757ea68"},
    {file = "pytokens-0.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8bdb9d0ce90cbf99c525e75a2fa415144fd570a1ba987380190e8b786bc6ef9b"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5502408cab1cb18e128570f8d598981c68a50d0cbd7c61312a90507cd3a1276f"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29d1d8fb1030af4d231789959f21821ab6325e463f0503a61d204343c9b355d1"},
    {file = "pytokens-0.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b08dd6b86058b6dc07efe9e98414f5102974716232d10f32ff39701e841c4"},
    {file = "pytokens-0.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:9bd7d7f544d362576be74f9d5901a22f317efc20046efe2034dced238cbbfe78"},
    {file = "pytokens-0.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4a14d5f5fc78ce85e426aa159489e2d5961acf0e47575e08f35584009178e321"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97f50fd18543be72da51dd505e2ed20d2228c74e0464e4262e4899797803d7fa"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dc74c035f9bfca0255c1af77ddd2d6ae8419012805453e4b0e7513e17904545d"},
    {file = "pytokens-0.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f66a6bbe741bd431f6d741e617e0f39ec7257ca1f89089593479347cc4d13324"},
    {file = "pytokens-0.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:b35d7e5ad269804f6697727702da3c517bb8a5228afa450ab0fa787732055fc9"},
    {file = "pytokens-0.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:8fcb9ba3709ff77e77f1c7022ff11d13553f3c30299a9fe246a166903e9091eb"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79fc6b8699564e1f9b521582c35435f1bd32dd06822322ec44afdeba666d8cb3"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d31b97b3de0f61571a124a00ffe9a81fb9939146c122c11060725bd5aea79975"},
    {file = "pytokens-0.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:967cf6e3fd4adf7de8fc73cd3043754ae79c36475c1c11d514fc72cf5490094a"},
    {file = "pytokens-0.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:584c80c24b078eec1e227079d56dc22ff755e0ba8654d8383b2c549107528918"},
    {file = "pytokens-0.4.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:da5baeaf7116dced9c6bb76dc31ba04a2dc3695f3d9f74741d7910122b456edc"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:11edda0942da80ff58c4408407616a310adecae1ddd22eef8c692fe266fa5009"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0fc71786e629cef478cbf29d7ea1923299181d0699dbe7c3c0f4a583811d9fc1"},
    {file = "pytokens-0.4.1-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:dcafc12c30dbaf1e2af0490978352e0c4041a7cde31f4f81435c2a5e8b9cabb6"},
    {file = "pytokens-0.4.1-cp38-cp38-win_amd64.whl", hash = "sha256:42f144f3aafa5d92bad964d471a581651e28b24434d184871bd02e3a0d956037"},
    {file = "pytokens-0.4.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:34bcc734bd2f2d5fe3b34e7b3c0116bfb2397f2d9666139988e7a3eb5f7400e3"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941d4343bf27b605e9213b26bfa1c4bf197c9c599a9627eb7305b0defcfe40c1"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3ad72b851e781478366288743198101e5eb34a414f1d5627cdd585ca3b25f1db"},
    {file = "pytokens-0.4.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:682fa37ff4d8e95f7df6fe6fe6a431e8ed8e788023c6bcc0f0880a12eab80ad1"},
    {file = "pytokens-0.4.1-cp39-cp39-win_amd64.whl", hash = "sha256:30f51edd9bb7f85c748979384165601d028b84f7bd13fe14d3e065304093916a"},
    {file = "pytokens-0.4.1-py3-none-any.whl", hash = "sha256:26cef14744a8385f35d0e095dc8b3a7583f6c953c2e3d269c7f82484bf5ad2de"},
    {file = "pytokens-0.4.1.tar.gz", hash = "sha256:292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "312"
description = "Python for Windows Extensions"
optional = false
python-versions = ">=3.9"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-312-cp310-cp310-win32.whl", hash = "sha256:772235332b5d1024c696f11cea1ae4be7930f0a8b894bb43db14e3f435f1ff7e"},
    {file = "pywin32-312-cp310-cp310-win_amd64.whl", hash = "sha256:5dbc35d2b5320dc07f25fa31269cfb767471002b17de5eb067d03da68c7cb2db"},
    {file = "pywin32-312-cp310-cp310-win_arm64.whl", hash = "sha256:3020656e34f1cf7faeb7bccd2b84653a607c6ff0c55ada85e6487d61716deabd"},
    {file = "pywin32-312-cp311-cp311-win32.whl", hash = "sha256:17948aeadbdb091f0ced6ef0841620794e68327b94ee415571c1203594b7215c"},
    {file = "pywin32-312-cp311-cp311-win_amd64.whl", hash = "sha256:d11417d84412f859b722fad0841b3614459ed0047f7542d8362e77884f6b6e8a"},
    {file = "pywin32-312-cp311-cp311-win_arm64.whl", hash = "sha256:b2200a054ca6d6625c4842fc56a4976a4b47f96b73dbe5538c3f813a80359f47"},
    {file = "pywin32-312-cp312-cp312-win32.whl", hash = "sha256:dab4f65ac9c4e48400a2a0530c46c3c579cd5905ecd11b80692373915269208b"},
    {file = "pywin32-312-cp312-cp312-win_amd64.whl", hash = "sha256:b457f6d628a47e8a7346ce22acb7e1a46a4a78b52e1d17e1af56871bd19a93bc"},
    {file = "pywin32-312-cp312-cp312-win_arm64.whl", hash = "sha256:6017c58e12f6809fbb0555b75df144c2922a9ffd18e4b9b5afa863b6c1a9d950"},
    {file = "pywin32-312-cp313-cp313-win32.whl", hash = "sha256:7a27df850933d16a8eabfbaeb73d52b273e2da667f80d70b01a89d1f6828d02c"},
    {file = "pywin32-312-cp313-cp313-win_amd64.whl", hash = "sha256:c53e878d15a1c44788082bfe712a905433473aa38f86375b7cf8b45e3acbaaf9"},
    {file = "pywin32-312-cp313-cp313-win_arm64.whl", hash = "sha256:59aba5d5940842075343a5ddc6b11f1cdf0d1567fe745290359dfbcc7c2eb831"},
    {file = "pywin32-312-cp314-cp314-win32.whl", hash = "sha256:a77a90fbb6881238d2ca9c6fd797b25817f3768fe78d214a90137ff055a75f5b"},
    {file = "pywin32-312-cp314-cp314-win_amd64.whl", hash = "sha256:a4dd3a848290ef724347b19f301045831d8e802fa4464f491b98b1e0a081432e"},
    {file = "pywin32-312-cp314-cp314-win_arm64.whl", hash = "sha256:9fce94568364e0155e6dfb781ac5d95903be8baf28670632beab1b523f300daa"},
    {file = "pywin32-312-cp315-cp315-win32.whl", hash = "sha256:5c1fbe4a937a73ae9297384a3da38518cbc694c68ad8a809b2e19acd350f03ed"},
    {file = "pywin32-312-cp315-cp315-win_amd64.whl", hash = "sha256:c2f03a0f73f804a13c2735b99392b0cd426bb4f2c4d0178e5ac966a0f21618d5"},
    {file = "pywin32-312-cp315-cp315-win_arm64.whl", hash = "sha256:a8597d28f267b39074aef51fa593530082b39cbe5a074226096857b1fed2dfb9"},
    {file = "pywin32-312-cp39-cp39-win32.whl", hash = "sha256:d620900033cc7531e50727c3c8333091df5dd3ffe6d68cdca38c03f5821408d5"},
    {file = "pywin32-312-cp39-cp39-win_amd64.whl", hash = "sha256:dc90147579a905b8635e1b0ec6514967dcb07e6e0d9c42f1477feef14cac23bb"},
    {file = "pywin32-312-cp39-cp39-win_arm64.whl", hash = "sha256:02ebca0f0242b75292e218065004310d6a477407c09fa449bfe4f6022bc0c0fc"},
]

[[package]]
name = "setuptools"
version = "81.0.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["main", "lint"]
files = [
    {file = "setuptools-81.0.0-py3-none-any.whl", hash = "sha256:fdd925d5c5d9f62e4b74b30d6dd7828ce236fd6ed998a08d81de62ce5a6310d6"},
    {file = "setuptools-81.0.0.tar.gz", hash = "sha256:487b53915f52501f0a79ccfd0c02c165ffe06631443a886740b91af4b7a5845a"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.13.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.18.*)", "pytest-mypy"]

[[package]]
name = "snowballstemmer"
version = "3.1.1"
description = "This package provides 36 stemmers for 34 languages generated from Snowball algorithms."
optional = false
python-versions = ">=3.3"
groups = ["lint"]
files = [
    {file = "snowballstemmer-3.1.1-py3-none-any.whl", hash = "sha256:7e207fa178741da09cdee59d3ecec3827ad5f92b1fc5c9ff3755b639f71f5752"},
    {file = "snowballstemmer-3.1.1.tar.gz", hash = "sha256:e07bbc54a0d798fe6010a12398422e62a8bfbba95c394fd0956ef58cb4d3e260"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["lint"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.4.1"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f8f0fc26ec2cc2b965b7a3b87cd19c5c6b8c5e5f436b984e85f486d652285c30"},
    {file = "tomli-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ab97e64ccda8756376892c53a72bd1f964e519c77236368527f758fbc36a53a"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:96481a5786729fd470164b47cdb3e0e58062a496f455ee41b4403be77cb5a076"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a881ab208c0baf688221f8cecc5401bd291d67e38a1ac884d6736cbcd8247e9"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:47149d5bd38761ac8be13a84864bf0b7b70bc051806bc3669ab1cbc56216b23c"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ec9bfaf3ad2df51ace80688143a6a4ebc09a248f6ff781a9945e51937008fcbc"},
    {file = "tomli-2.4.1-cp311-cp311-win32.whl", hash = "sha256:ff2983983d34813c1aeb0fa89091e76c3a22889ee83ab27c5eeb45100560c049"},
    {file = "tomli-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:5ee18d9ebdb417e384b58fe414e8d6af9f4e7a0ae761519fb50f721de398dd4e"},
    {file = "tomli-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:c2541745709bad0264b7d4705ad453b76ccd191e64aa6f0fc66b69a293a45ece"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:c742f741d58a28940ce01d58f0ab2ea3ced8b12402f162f4d534dfe18ba1cd6a"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7f86fd587c4ed9dd76f318225e7d9b29cfc5a9d43de44e5754db8d1128487085"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ff18e6a727ee0ab0388507b89d1bc6a22b138d1e2fa56d1ad494586d61d2eae9"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:136443dbd7e1dee43c68ac2694fde36b2849865fa258d39bf822c10e8068eac5"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5e262d41726bc187e69af7825504c933b6794dc3fbd5945e41a79bb14c31f585"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5cb41aa38891e073ee49d55fbc7839cfdb2bc0e600add13874d048c94aadddd1"},
    {file = "tomli-2.4.1-cp312-cp312-win32.whl", hash = "sha256:da25dc3563bff5965356133435b757a795a17b17d01dbc0f42fb32447ddfd917"},
    {file = "tomli-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:52c8ef851d9a240f11a88c003eacb03c31fc1c9c4ec64a99a0f922b93874fda9"},
    {file = "tomli-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:f758f1b9299d059cc3f6546ae2af89670cb1c4d48ea29c3cacc4fe7de3058257"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:36d2bd2ad5fb9eaddba5226aa02c8ec3fa4f192631e347b3ed28186d43be6b54"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:eb0dc4e38e6a1fd579e5d50369aa2e10acfc9cace504579b2faabb478e76941a"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c7f2c7f2b9ca6bdeef8f0fa897f8e05085923eb091721675170254cbc5b02897"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3c6818a1a86dd6dca7ddcaaf76947d5ba31aecc28cb1b67009a5877c9a64f3f"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d312ef37c91508b0ab2cee7da26ec0b3ed2f03ce12bd87a588d771ae15dcf82d"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:51529d40e3ca50046d7606fa99ce3956a617f9b36380da3b7f0dd3dd28e68cb5"},
    {file = "tomli-2.4.1-cp313-cp313-win32.whl", hash = "sha256:2190f2e9dd7508d2a90ded5ed369255980a1bcdd58e52f7fe24b8162bf9fedbd"},
    {file = "tomli-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:8d65a2fbf9d2f8352685bc1364177ee3923d6baf5e7f43ea4959d7d8bc326a36"},
    {file = "tomli-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:4b605484e43cdc43f0954ddae319fb75f04cc10dd80d830540060ee7cd0243cd"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fd0409a3653af6c147209d267a0e4243f0ae46b011aa978b1080359fddc9b6cf"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:a120733b01c45e9a0c34aeef92bf0cf1d56cfe81ed9d47d562f9ed591a9828ac"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:559db847dc486944896521f68d8190be1c9e719fced785720d2216fe7022b662"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01f520d4f53ef97964a240a035ec2a869fe1a37dde002b57ebc4417a27ccd853"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7f94b27a62cfad8496c8d2513e1a222dd446f095fca8987fceef261225538a15"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ede3e6487c5ef5d28634ba3f31f989030ad6af71edfb0055cbbd14189ff240ba"},
    {file = "tomli-2.4.1-cp314-cp314-win32.whl", hash = "sha256:3d48a93ee1c9b79c04bb38772ee1b64dcf18ff43085896ea460ca8dec96f35f6"},
    {file = "tomli-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:88dceee75c2c63af144e456745e10101eb67361050196b0b6af5d717254dddf7"},
    {file = "tomli-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:b8c198f8c1805dc42708689ed6864951fd2494f924149d3e4bce7710f8eb5232"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:d4d8fe59808a54658fcc0160ecfb1b30f9089906c50b23bcb4c69eddc19ec2b4"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7008df2e7655c495dd12d2a4ad038ff878d4ca4b81fccaf82b714e07eae4402c"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1d8591993e228b0c930c4bb0db464bdad97b3289fb981255d6c9a41aedc84b2d"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:734e20b57ba95624ecf1841e72b53f6e186355e216e5412de414e3c51e5e3c41"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8a650c2dbafa08d42e51ba0b62740dae4ecb9338eefa093aa5c78ceb546fcd5c"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:504aa796fe0569bb43171066009ead363de03675276d2d121ac1a4572397870f"},
    {file = "tomli-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:b1d22e6e9387bf4739fbe23bfa80e93f6b0373a7f1b96c6227c32bef95a4d7a8"},
    {file = "tomli-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:2c1c351919aca02858f740c6d33adea0c5deea37f9ecca1cc1ef9e884a619d26"},
    {file = "tomli-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:eab21f45c7f66c13f2a9e0e1535309cee140182a9cdae1e041d02e47291e8396"},
    {file = "tomli-2.4.1-py3-none-any.whl", hash = "sha256:0d85819802132122da43cb86656f8d1f8c6587d54ae7dcaf30e90533028b49fe"},
    {file = "tomli-2.4.1.tar.gz", hash = "sha256:7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f"},
]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "types-grpcio"
version = "1.0.0.20260614"
description = "Typing stubs for grpcio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_grpcio-1.0.0.20260614-py3-none-any.whl", hash = "sha256:050472cb4ef329ae8fe20278c62bc0da5b961aad3dd889cc35f6e0c70d368dae"},
    {file = "types_grpcio-1.0.0.20260614.tar.gz", hash = "sha256:e86d1aabb7e7eedae487c3ac10e010a13d5db1fd350e766562053af557366aab"},
]

[[package]]
name = "types-protobuf"
version = "7.34.1.20260518"
description = "Typing stubs for protobuf"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_protobuf-7.34.1.20260518-py3-none-any.whl", hash = "sha256:a0a5337413347166439c0e07cbc26c6164d091401c6f01b1dfd8cdb966c4dd8f"},
    {file = "types_protobuf-7.34.1.20260518.tar.gz", hash = "sha256:28cfaded25889cb83ebfb63cfb0a43628f0b6f3785767bec17287dc6468795f2"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "lint"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "e83ffbce072edf9ce9fd71b57b75d0c073dafd002bd41de1cbef3a7d04b7efba"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/overview/poetry.toml

- repository: `ni/datastore-python`
- source_path: `examples/overview/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/pyproject.toml sha256=ea72c03d2de6a2804a7080689a9c38067c676e01baa1ca0139ad7b3ba876ac32 bytes=2365 -->
## FILE: examples/overview/pyproject.toml

- repository: `ni/datastore-python`
- source_path: `examples/overview/pyproject.toml`
- sha256: `ea72c03d2de6a2804a7080689a9c38067c676e01baa1ca0139ad7b3ba876ac32`
- bytes: 2365

````toml
[project]
name = "overview_example"
version = "1.0.0"
license = "MIT"
description = "Overview of how to use the NI Measurement Data Store APIs for publishing and reading data"
maintainers = [
  {name = "Johann Scholtz", email = "johann.scholtz@emerson.com"},
  {name = "Joel Dixon", email = "joel.dixon@emerson.com"}
]
readme = "README.md"
repository = "https://github.com/ni/datastore-python"
keywords = ["overview", "example"]
classifiers = [
  "Development Status :: 5 - Production/Stable",
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
]
dynamic = ["dependencies"]
requires-python = '>=3.10,<4.0'

[[tool.poetry.packages]]
include = "src"

[project.scripts]
overview = "src.overview:main"

[tool.poetry]
requires-poetry = '>=2.1,<3.0'

[tool.poetry.dependencies]
python = "^3.10"
ni-datastore = { version=">=2.0.0.dev0", allow-prereleases = true }
protobuf = { version=">=4.21" }
ni-protobuf-types = { version = ">=1.1.0" }
hightime = { version = ">=1.0.0" }
grpcio-tools = [
  { version = "1.49.1", python = ">=3.9,<3.12" },
  { version = "1.59.0", python = ">=3.12,<3.13" },
  { version = "1.67.0", python = ">=3.13,<3.14" },
  { version = "1.75.1", python = "^3.14" },
]

[tool.poetry.group.dev.dependencies]
types-grpcio = ">=1.0"
types-protobuf = ">=4.21"
# Uncomment to use local ni-datastore code
# ni-datastore = {path = "../..", develop = true}
datastore-utilities = { path = "../../utilities", develop = true }

[tool.poetry.group.lint.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"

[build-system]
requires = ["poetry-core>=1.8"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 100

[tool.mypy]
mypy_path = "src"
files = "."
namespace_packages = true
strict = true
explicit_package_bases = true
exclude = ["docs"]
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/README.md sha256=c2da6d7daf957a33e5732c3c37d3a40bbb614346a14d8ee1156fc5da16c5a373 bytes=261 -->
## FILE: examples/overview/README.md

- repository: `ni/datastore-python`
- source_path: `examples/overview/README.md`
- sha256: `c2da6d7daf957a33e5732c3c37d3a40bbb614346a14d8ee1156fc5da16c5a373`
- bytes: 261

````markdown
# Overview Example

`overview` contains sample Python code for writing to and reading from
the NI Measurement Data Store.

## Required Software

`overview` requires Python 3.10 or greater

## Usage

```python
poetry install
poetry run overview
```
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/src/__init__.py sha256=6b50f118465e2944d24b7ac14c5a1016c9d2577e02bc0b91f6104cdc9cbe98c8 bytes=60 -->
## FILE: examples/overview/src/__init__.py

- repository: `ni/datastore-python`
- source_path: `examples/overview/src/__init__.py`
- sha256: `6b50f118465e2944d24b7ac14c5a1016c9d2577e02bc0b91f6104cdc9cbe98c8`
- bytes: 60

````python
"""Overview example of NI Measurement Data Store usage."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/overview/src/overview.py sha256=6787698ceaf6953ed6003b1d2d31d54e376be668802f210cf3b85241957a068d bytes=4915 -->
## FILE: examples/overview/src/overview.py

- repository: `ni/datastore-python`
- source_path: `examples/overview/src/overview.py`
- sha256: `6787698ceaf6953ed6003b1d2d31d54e376be668802f210cf3b85241957a068d`
- bytes: 4915

````python
"""Overview example demonstrating data publishing and querying."""

from datetime import timezone

import hightime as ht
import numpy as np
from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)
from ni.datastore.metadata import (
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    TestStation,
    Uut,
    UutInstance,
)
from nitypes.waveform import AnalogWaveform, Timing
from utilities import DataStoreContext


def main() -> None:
    """Main function to demonstrate data publishing and querying."""
    # The DataStoreContext sets up and tears down the example environment.
    # It is not used in production code.
    with DataStoreContext():
        published_measurement_id = publish_data()
        query_data(published_measurement_id)


def publish_data() -> str:
    """Demonstrate data publishing of an AnalogWaveform."""
    with MetadataStoreClient() as metadata_store_client, DataStoreClient() as data_store_client:
        # Create UUT instance
        uut = Uut(model_name="NI-6508", family="Digital")
        uut_id = metadata_store_client.create_uut(uut)
        uut_instance = UutInstance(uut_id=uut_id, serial_number="A861-42367")
        uut_instance_id = metadata_store_client.create_uut_instance(uut_instance=uut_instance)

        # Create Operator metadata
        operator = Operator(name="James Bowery", role="Test Operator")
        operator_id = metadata_store_client.create_operator(operator)
        print(f"created operator_id: {operator_id}")

        # Create TestStation metadata
        test_station = TestStation(name="TestStation_12")
        test_station_id = metadata_store_client.create_test_station(test_station)
        print(f"created test_station_id: {test_station_id}")

        # Create SoftwareItem metadata
        software_item = SoftwareItem(product="Windows", version="10.0.19044")
        software_item_id = metadata_store_client.create_software_item(software_item)
        print(f"created software_item_id: {software_item_id}")
        software_item_2 = SoftwareItem(product="Python", version="3.12")
        software_item_2_id = metadata_store_client.create_software_item(software_item_2)
        print(f"created software_item_2_id: {software_item_2_id}")

        # Create TestResult metadata
        test_result = TestResult(
            name="sample test result",
            operator_id=operator_id,
            test_station_id=test_station_id,
            software_item_ids=[software_item_id, software_item_2_id],
            uut_instance_id=uut_instance_id,
        )
        test_result_id = data_store_client.create_test_result(test_result)
        print(f"created test_result_id: {test_result_id}")

        name = "data publish sample"
        # Create waveform data to publish
        waveform = AnalogWaveform(
            sample_count=3,
            raw_data=np.array([1.0, 2.0, 3.0]),
            timing=Timing.create_with_regular_interval(
                ht.timedelta(seconds=1e-3), ht.datetime.now(timezone.utc)
            ),
        )

        # Publish the test step with the waveform data
        step = Step(name="Initial step", test_result_id=test_result_id)
        step_id = data_store_client.create_step(step)
        published_measurement_id = data_store_client.publish_measurement(
            name=name,
            value=waveform,
            step_id=step_id,
        )
        published_measurement = data_store_client.get_measurement(published_measurement_id)
        print(
            f"Published measurement: '{published_measurement.name}' with id {published_measurement.id}"
        )

    return published_measurement_id


def query_data(published_measurement_id: str) -> None:
    """Demonstrate querying a published AnalogWaveform measurement."""
    with MetadataStoreClient() as metadata_store_client, DataStoreClient() as data_store_client:
        published_measurements = data_store_client.query_measurements(
            odata_query=f"$filter=id eq {published_measurement_id}"
        )
        found_measurement = next(iter(published_measurements), None)

        if found_measurement is not None:
            print(
                f"Found published measurement: '{found_measurement.name}' with id {found_measurement.id}"
            )
            test_result = data_store_client.get_test_result(found_measurement.test_result_id)
            print(f"test_result: {test_result.name}")
            operator = metadata_store_client.get_operator(test_result.operator_id)
            print(f"operator: {operator}")

            waveform = data_store_client.read_measurement_value(
                found_measurement, expected_type=AnalogWaveform
            )
            print(f"published data is: {waveform.raw_data}")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/poetry.lock sha256=e5b946c48bbc6f27d290b4818dedad7732c044da2ebcdf30bf9f2cfd891fba47 bytes=99524 -->
## FILE: examples/system/poetry.lock

- repository: `ni/datastore-python`
- source_path: `examples/system/poetry.lock`
- sha256: `e5b946c48bbc6f27d290b4818dedad7732c044da2ebcdf30bf9f2cfd891fba47`
- bytes: 99524

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "ast-serialize"
version = "0.5.0"
description = "Python bindings for mypy AST serialization"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8f5c14f169eb0972c0c21bada5358b23d6047c76583b005234f865b11f1fa00a"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7d1a2de9de5be04652f0ed60738356ef94f66db37924a9499fffe98dc491aa0b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:be5173fb66f9b49026d9d5a2ff0fc7c7009077107c0eb285b2d60fdf1fe10bd1"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f8015cd071ac1339924ee2b8098c93e00e155f30a16f40ec9816fcf84f4753f6"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5499e8797edff2a9186aa313ed382c6b422e798e9332d9953badcee6e69a88f2"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6848f2a093fb5548751a9a09bff8fcd229e2bbeb0e3331f391b6ae6d26cd9903"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:832d4c998e0b091fd60a6d6bceee535483c4d490de9ba85003af835225719261"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:16db7c62ec0b8efe1d7afd283a388d8f74f2605d56032e5a37747d2de8dba027"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:baf5eb061eb5bccade4128ad42da33787d72f6013809cd1b590376ece8b3c937"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:104e4a35bd7c124173c41760ef9aaea17ddb3f86c65cb643671d59afbe3ee94c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:36be371028fc1675acb38a331bde160dbab7ff907fdf00b67eb6911aa106951b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:061ee58bdb52341c8201a6df41182a977736bae3b7ded87ca7176ca25a8a47ab"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b15219e9cdc9f53f6f4cb51c009203507228226148c05c5e8fe451c28b435eb3"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win32.whl", hash = "sha256:842d1c004bb466c7df036f95fabef789570541922b10976b12f5592a69cf0b38"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b0c06d760909b095cc466356dfccd05a1c7233a6ca191c020dca2c6a6f16c24c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:787baedb0262cc49e8ce37cc15c00ae818e46a165a3b36f5e21ed174998104cb"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:0668aa9459cfa8c9c49ddd2163ebcf43088ba045ef7492af6fe22e0098303101"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:bf683d6363edf2b39eed6b6d4fe22d34b6203867a67e27134d9e2a2680c4bc4a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9cc22cf0c9be65e71cf88fda130af60d61eb4a79370ad4cfe7900d48a4aa2211"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f66173891548c9f2726bf27957b41cabce12fa679dc6da505ddbde4d4b3b31cf"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e42d729ef2be96a14efbad355093284739e3670ece3e534f82cc8832790911d9"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b725026bafa801dbd7310eb13a75f0a2e370e7e51b2cb225f9d21fcfadf919ee"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b54f60c1d78767a53b67eaa663f0dfac3afe606aa07f1301572f588b73d64809"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_31_riscv64.whl", hash = "sha256:27d51654fc240a1e87e742d353d98eb45b75f62f129086b3596ab53df2ac2a43"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c36237c46dd1674542f2109740ea5ea485a169bf1431939ada0434e17934"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:1943db345233cc7194a470f13afa9c59772c0b123dea0c9414c4d4ca54369759"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:df1c00022cbbcb064bfaa505aa9c9295362443ce5dacb459d1331d3da353f887"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:cae65289fc456fde04af979a2be09302ef5d8ab92ef23e596d6746dc267ada27"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:239a4c354e8d676e9d94631d1d4a64edc6b266f86ff3a5a80aedd344f342c01d"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win32.whl", hash = "sha256:143a4ef63285a075871908fda3672dc21864b83a8ec3ee12304aa3e4c5387b9a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_amd64.whl", hash = "sha256:cf25572c526add400f26a4750dc6ce0c3bb93fc1f75e7ae0cad4ce4f2cd5c590"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_arm64.whl", hash = "sha256:92a31c9c20d25a076edaeec76b128a3535d74a24f340b9a8a7e96c9b86dc9642"},
    {file = "ast_serialize-0.5.0.tar.gz", hash = "sha256:5880091bfe6f4f986f22866375c2e884843e7a0b6343ae41aeea659613d879b6"},
]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["lint"]
files = [
    {file = "better_diff-0.1.4-py3-none-any.whl", hash = "sha256:06e63358b2047ae2695abd96316f47c6d3c38b9e641f53012279878d66d8792e"},
    {file = "better_diff-0.1.4.tar.gz", hash = "sha256:920ca76bdbcd2f0c361fa5d9a2d4727624a3545d6cb467b1b6616cad8a634de7"},
]

[[package]]
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "black-25.12.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f85ba1ad15d446756b4ab5f3044731bf68b777f8f9ac9cdabd2425b97cd9c4e8"},
    {file = "black-25.12.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:546eecfe9a3a6b46f9d69d8a642585a6eaf348bcbbc4d87a19635570e02d9f4a"},
    {file = "black-25.12.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:17dcc893da8d73d8f74a596f64b7c98ef5239c2cd2b053c0f25912c4494bf9ea"},
    {file = "black-25.12.0-cp310-cp310-win_amd64.whl", hash = "sha256:09524b0e6af8ba7a3ffabdfc7a9922fb9adef60fed008c7cd2fc01f3048e6e6f"},
    {file = "black-25.12.0-cp310-cp310-win_arm64.whl", hash = "sha256:b162653ed89eb942758efeb29d5e333ca5bb90e5130216f8369857db5955a7da"},
    {file = "black-25.12.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d0cfa263e85caea2cff57d8f917f9f51adae8e20b610e2b23de35b5b11ce691a"},
    {file = "black-25.12.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a2f578ae20c19c50a382286ba78bfbeafdf788579b053d8e4980afb079ab9be"},
    {file = "black-25.12.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e1b65634b0e471d07ff86ec338819e2ef860689859ef4501ab7ac290431f9b"},
    {file = "black-25.12.0-cp311-cp311-win_amd64.whl", hash = "sha256:a3fa71e3b8dd9f7c6ac4d818345237dfb4175ed3bf37cd5a581dbc4c034f1ec5"},
    {file = "black-25.12.0-cp311-cp311-win_arm64.whl", hash = "sha256:51e267458f7e650afed8445dc7edb3187143003d52a1b710c7321aef22aa9655"},
    {file = "black-25.12.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:31f96b7c98c1ddaeb07dc0f56c652e25bdedaac76d5b68a059d998b57c55594a"},
    {file = "black-25.12.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:05dd459a19e218078a1f98178c13f861fe6a9a5f88fc969ca4d9b49eb1809783"},
    {file = "black-25.12.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1f68c5eff61f226934be6b5b80296cf6939e5d2f0c2f7d543ea08b204bfaf59"},
    {file = "black-25.12.0-cp312-cp312-win_amd64.whl", hash = "sha256:274f940c147ddab4442d316b27f9e332ca586d39c85ecf59ebdea82cc9ee8892"},
    {file = "black-25.12.0-cp312-cp312-win_arm64.whl", hash = "sha256:169506ba91ef21e2e0591563deda7f00030cb466e747c4b09cb0a9dae5db2f43"},
    {file = "black-25.12.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a05ddeb656534c3e27a05a29196c962877c83fa5503db89e68857d1161ad08a5"},
    {file = "black-25.12.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9ec77439ef3e34896995503865a85732c94396edcc739f302c5673a2315e1e7f"},
    {file = "black-25.12.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e509c858adf63aa61d908061b52e580c40eae0dfa72415fa47ac01b12e29baf"},
    {file = "black-25.12.0-cp313-cp313-win_amd64.whl", hash = "sha256:252678f07f5bac4ff0d0e9b261fbb029fa530cfa206d0a636a34ab445ef8ca9d"},
    {file = "black-25.12.0-cp313-cp313-win_arm64.whl", hash = "sha256:bc5b1c09fe3c931ddd20ee548511c64ebf964ada7e6f0763d443947fd1c603ce"},
    {file = "black-25.12.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:0a0953b134f9335c2434864a643c842c44fba562155c738a2a37a4d61f00cad5"},
    {file = "black-25.12.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2355bbb6c3b76062870942d8cc450d4f8ac71f9c93c40122762c8784df49543f"},
    {file = "black-25.12.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9678bd991cc793e81d19aeeae57966ee02909877cb65838ccffef24c3ebac08f"},
    {file = "black-25.12.0-cp314-cp314-win_amd64.whl", hash = "sha256:97596189949a8aad13ad12fcbb4ae89330039b96ad6742e6f6b45e75ad5cfd83"},
    {file = "black-25.12.0-cp314-cp314-win_arm64.whl", hash = "sha256:778285d9ea197f34704e3791ea9404cd6d07595745907dd2ce3da7a13627b29b"},
    {file = "black-25.12.0-py3-none-any.whl", hash = "sha256:48ceb36c16dbc84062740049eef990bb2ce07598272e673c17d1a7720c71c828"},
    {file = "black-25.12.0.tar.gz", hash = "sha256:8d3dd9cea14bff7ddc0eb243c811cdb1a011ebb4800a5f0335a01a68654796a7"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "click"
version = "8.4.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "click-8.4.1-py3-none-any.whl", hash = "sha256:482be17c6991b8c19c5429a1e995d9b0efdbb63172824c41f99965dc0ade8ec2"},
    {file = "click-8.4.1.tar.gz", hash = "sha256:918b5633eddf6b41c32d4f454bf0de810065c74e3f7dbf8ee5452f8be88d3e96"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["lint"]
markers = "platform_system == \"Windows\""
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "datastore-utilities"
version = "0.1.0.dev0"
description = "Development utilities for datastore-python"
optional = false
python-versions = "^3.10"
groups = ["dev"]
files = []
develop = true

[package.source]
type = "directory"
url = "../../utilities"

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "flake8-6.1.0-py2.py3-none-any.whl", hash = "sha256:ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5"},
    {file = "flake8-6.1.0.tar.gz", hash = "sha256:d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.11.0,<2.12.0"
pyflakes = ">=3.1.0,<3.2.0"

[[package]]
name = "flake8-black"
version = "0.4.0"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_black-0.4.0-py3-none-any.whl", hash = "sha256:288762d0c9ea065782d87eeecbcc20c69079d17fe1d0f0445f0eb0b0ffb80c39"},
    {file = "flake8_black-0.4.0.tar.gz", hash = "sha256:bf226868f695dee48d55ff6d7747e900709bfd6f605b7a378c70e711e3fc26cb"},
]

[package.dependencies]
black = ">=22.1.0"
flake8 = ">=3"
tomli = {version = "*", markers = "python_version < \"3.11\""}

[package.extras]
develop = ["build", "twine"]

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["lint"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "flake8-tidy-imports"
version = "4.12.0"
description = "A flake8 plugin that helps you write tidier imports."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "grpcio"
version = "1.81.1"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "grpcio-1.81.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:6f9a0c9c1cc15c112d1c053064fd032b64917062292c3d70aea280e02ae10b77"},
    {file = "grpcio-1.81.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:69ef28e54fc85397f91b8c19592b8ef3d81952080366914823bd8572a2958120"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:15641444eca4a29358107b3dceb74c1c6305c55c822fd199b458aaea4068a7fb"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:d4b2dddfc219f54f956ccd53cf76a1d338ffe68fc7f2849ec9c7feb9927ff692"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ca1cc11d82677b9662082e5478b7528e2b7db7beaa6bdff42bd62789d81be399"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:aa2ba7d2ad6df4d80127cea65e5b8d5e2c3adbf153ff4804452836328aca7c54"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:592b5fee597faa91cce2dd294dd7d9a1c83d76c4dbf877e33ec1adb866b2fbed"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:62481553b1793a27e9b9c3cf9e5bd483ef045ca72462592074b46d42b0c4d9b9"},
    {file = "grpcio-1.81.1-cp310-cp310-win32.whl", hash = "sha256:bb693b1e3d9a2f3fd228e2110daf4b5aeedb36761ca1e4282f74725f6d89f611"},
    {file = "grpcio-1.81.1-cp310-cp310-win_amd64.whl", hash = "sha256:88268ca418cacea64cecb0d1d600d3c6b3a8038fcba02e1e205178c5b1f47661"},
    {file = "grpcio-1.81.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:d71d30f2d92f67d944631c523713934fee37292469e182ebcd2c1dd8a64ce53f"},
    {file = "grpcio-1.81.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:b137f4bf3ada9dc44d411478decc6ff09a79ed30b306cd2abaa98408c3588137"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a3acb384427816dd5d470f47e62137b87f74da694faa8a50147012cf40df276a"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f9a0ebbe45c29b5e5866593c12b78bd9035f0f0f0d4bc8361680cd580d99db49"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:0a37165cc80b1a368384b383e63a4c38116a10467ae44c904d2d7468c4470ec2"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:6282caffb41ec326d4cb67ca9cf53b739d1b2f975a2acb498c7418e9f7d9a416"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:a35009284d0d3d5c2c9601c164a911b8b4331608d98a9a66d47d97bb2f522b70"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1b22c80559854b789a01fd89e8929b3798a156c0829b5282a8939f33ad4115ad"},
    {file = "grpcio-1.81.1-cp311-cp311-win32.whl", hash = "sha256:428bec0161b48d8cf583c068591bc0016d0d9cfff52462b72b3884861ea768c5"},
    {file = "grpcio-1.81.1-cp311-cp311-win_amd64.whl", hash = "sha256:30e825f6848d9f18bba350ed6c75c1b02a0b5184474a31db9a32b1fa66fd8c79"},
    {file = "grpcio-1.81.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:8b39472beafc0bdcafc4c8c73ad082ebfdb449d566897a61e7acb4fa88089115"},
    {file = "grpcio-1.81.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:12b7524c88d4026d3dcb7b0ebe16b6714f3b4af402ddd0f0639ab064a00c87c3"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1e123f9b37edb8375fd74130d1f69c944bbf0a7b06761ae7211154b8759e94d2"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:2c2e2ae6867c2966b8daccc836d54a13218e0007e9a490aeb81dd05be64d22d7"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:766bc7c9a9c340342f4c864ccbda8e78111e4751f13b895812b9c148fb79e9d0"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b259a04a737cb3496be0901328eb8b7552ed8df4865d8c8f1cf1bffcfc0776a3"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:85b10a45b8993d195c4f3ff57025b8d1e11834909ee475c403bfa60cb4caefaf"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8ea1936c26b99999b27479853039a7f34713f56c49375ad52b38535ec93a796c"},
    {file = "grpcio-1.81.1-cp312-cp312-win32.whl", hash = "sha256:a185a04039df6cae8648bc8ab6d6fde7bf94f7188ecf7828e76ac52eef1e41d6"},
    {file = "grpcio-1.81.1-cp312-cp312-win_amd64.whl", hash = "sha256:3ad74f8bb1a18963914c5452d289422830b39459e8776ebbcd207be1fbfb1d94"},
    {file = "grpcio-1.81.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:b10e1ff4756ed27d5a29d7fc79cfce7ef1ff56ad20025b89bac7cf79e09abbbe"},
    {file = "grpcio-1.81.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:819edbdcb42ab8598b494bcf0222684bbb7a3c772bd1b1f0be7e029a6063c28e"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c5bf2dc311127d91230cc79b92188c082634a06cf66c5234db49a43b910183b0"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:e8ca6a1fcdb2943c9cbc1804a1baf3acb6071d72a471591678ded84218006e14"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e64dd101d380a115cc5a0c7856788adb535f1a4e21fc543775602f8be95180ae"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:98a07f9bf591e3a8919797bee1c53f026ba4acd587e5a4404c8e57c9ec36b2a5"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:c261d74b1a945cf895a9d6eccd1685a8e837531beaab782da4d630a8d12deffb"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:58ad1131c300d3c9b933802b3cc4dc69d380822935ba50b28703156ea826fbf7"},
    {file = "grpcio-1.81.1-cp313-cp313-win32.whl", hash = "sha256:78e29211f26da2fdd0e9c6d2b79f489476140cf7029b6a64808ade7ca4156a42"},
    {file = "grpcio-1.81.1-cp313-cp313-win_amd64.whl", hash = "sha256:edb59506291b647a30884b1d51a599d605f40b20af4a7dc3d33786a47a31de60"},
    {file = "grpcio-1.81.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:506f48f2f9c29b143fca3dad7b0d518c188b6c9648c75a2ae6e2d9f2c13a060b"},
    {file = "grpcio-1.81.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:d865db4a6318e1c1bea83292e0ed231090538fc4ca45425b0f0480eb338bbc6e"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:e2aa72e3ce1770317ef534f63d397b55e130725f5149bd36077c3b539019db27"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:0490c30c261eded63f3f354979f9dc4502a9fb944cccb60cd9dc85f5a7349854"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:410482da976329fe5f4067270401b12cf2bd552ff8020f054ecfaddb5475f9d6"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e3657301562ac3cb8018d30d0d3ebfa39932239f7b5703422057ef14b69949f5"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:24c8e57504c8f45b237e40b99262d181071e5099a07053695b75d97bb53053a0"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b427c19380991a4eaab2f6144b64b99b412043314c6bf4ab544f97bb31ee4190"},
    {file = "grpcio-1.81.1-cp314-cp314-win32.whl", hash = "sha256:61233fe8951e5c85dff81c2458b6528624760166946b5b47ea150a589168411f"},
    {file = "grpcio-1.81.1-cp314-cp314-win_amd64.whl", hash = "sha256:3768a5ff1b2125e6f552e561b6b2dca0e64982d8949689b4df145cf8b98d7821"},
    {file = "grpcio-1.81.1.tar.gz", hash = "sha256:6fa10a767143a5e82e8eaab53918af0cd8909a57a27f8cb2288b80a613ac671b"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.81.1)"]

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "isort"
version = "8.0.1"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["lint"]
files = [
    {file = "isort-8.0.1-py3-none-any.whl", hash = "sha256:28b89bc70f751b559aeca209e6120393d43fbe2490de0559662be7a9787e3d75"},
    {file = "isort-8.0.1.tar.gz", hash = "sha256:171ac4ff559cdc060bcfff550bc8404a486fee0caab245679c2abe7cb253c78d"},
]

[package.extras]
colors = ["colorama"]

[[package]]
name = "librt"
version = "0.11.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.11.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:6e94ebfcfa2d5e9926d6c3b9aa4617ffc42a845b4321fb84021b872358c82a0f"},
    {file = "librt-0.11.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:ae627397a2f351560440d872d6f7c8dbb4072e57868e7b2fc5b8b430fe489d45"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:dc329359321b67d24efdf4bc69012b0597001649544db662c001db5a0184794c"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:7e82e642ab0f7608ce2fe53d76ca2280a9ee33a1b06556142c7c6fe80a86fc33"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:88145c15c67731d54283d135b03244028c750cc9edc334a96a4f5950ebdb2884"},
    {file = "librt-0.11.0-cp310-cp310-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9d36a51b3d93320b686588e27123f4995804dbf1bce81df78c02fc3c6eea9280"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d00f3ac06a2a8b246327f11e186a53a100a4d5c7ed52346367e5ec751d51586c"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:461bbceede621f1ffb8839755f8663e886087ee7af16294cab7fb4d782c62eeb"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0cad8a4d6a8ff03c9b76f9414caccd78e7cfbc8a2e12fa334d8e1d9932753783"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f37aa505b3cf60701562eddb32df74b12a9e380c207fd8b06dd157a943ac7ea0"},
    {file = "librt-0.11.0-cp310-cp310-win32.whl", hash = "sha256:94663a21534637f0e787ec2a2a756022df6e5b7b2335a5cdd7d8e33d68a2af89"},
    {file = "librt-0.11.0-cp310-cp310-win_amd64.whl", hash = "sha256:dec7db73758c2b54953fd8b7fe348c45188fe26b39ee18446196edd08453a5d4"},
    {file = "librt-0.11.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:93d95bd45b7d58343d8b90d904450a545144eec19a002511163426f8ab1fae29"},
    {file = "librt-0.11.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ee278c769a713638cdacd4c0436d72156e75df3ebc0166ab2b9dc43acc386c9"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f230cb1cbc9faaa616f9a678f530ebcf186e414b6bcbd88b960e4ba1b92428d5"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:5d63c855d86938d9de93e265c9bd8c705b51ec494de5738340ee93767a686e4b"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:993f028be9e96a08d31df3479ac80d99be374d17f3b78e4796b3fd3c913d4e89"},
    {file = "librt-0.11.0-cp311-cp311-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:258d73a0aa66a055e65b2e4d1b8cdb23b9d132c5bb915d9547d804fcaed116cc"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0827efe7854718f04aaddf6496e96960a956e676fe1d0f04eb41511fd8ad06d5"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:7753e57d6e12d019c0d8786f1c09c709f4c3fcc57c3887b24e36e6c06ec938b7"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:11bd19822431cc21af9f27374e7ae2e58103c7d98bda823536a6c47f6bb2bb3d"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:22bdf239b219d3993761a148ffa134b19e52e9989c84f845d5d7b71d70a17412"},
    {file = "librt-0.11.0-cp311-cp311-win32.whl", hash = "sha256:46c60b61e308eb535fbd6fa622b1ee1bb2815691c1ad9c98bf7b84952ec3bc8d"},
    {file = "librt-0.11.0-cp311-cp311-win_amd64.whl", hash = "sha256:902e546ff044f579ff1c953ff5fce97b636fe9e3943996b2177710c6ef076f73"},
    {file = "librt-0.11.0-cp311-cp311-win_arm64.whl", hash = "sha256:65ac3bc20f78aa0ee5ae84baa68917f89fef4af63e941084dd019a0d0e749f0c"},
    {file = "librt-0.11.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b87504f1690a23b9a2cca841191a04f83895d4fc2dd04df91d82b1a04ca2ad46"},
    {file = "librt-0.11.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:40071fc5fe0ce8daa6de616702314a01e1250711682b0523d6ab8d4525910cb3"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:137e79445c896a0ea7b265f52d23954e05b64222ee1af69e2cb34219067cbb67"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:cca6644054e78746d8d4ef238681f9c34ff8b584fe6b988ecebb8db3b15e622a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5b0eea49f5562861ee8d757a32ef7d559c1d35be2aaaa1ec28941d74c9ffc8a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0d1029d7e1ae1a7e647ed6fb5df8c4ce2dffefb7a9f5fd1376a4554d96dac09f"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:bc3ce6b33c5828d9e80592011a5c584cb2ce86edbc4088405f70da47dc1d1b3b"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:936c5995f3514a42111f20099397d8177c79b4d7e70961e396c6f5a0a3566766"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:9bc0ca6ad9381cbe8e4aa6e5726e4c80c78115a6e9723c599ed1d73e092bc49d"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:070aa8c26c0a74774317a72df8851facc7f0f012a5b406557ac56992d92e1ec8"},
    {file = "librt-0.11.0-cp312-cp312-win32.whl", hash = "sha256:6bf14feb84b05ae945277395451998c89c54d0def4070eb5c08de544930b245a"},
    {file = "librt-0.11.0-cp312-cp312-win_amd64.whl", hash = "sha256:75672f0bc524ede266287d532d7923dbce94c7514ad07627bac3d0c6d92cc4d9"},
    {file = "librt-0.11.0-cp312-cp312-win_arm64.whl", hash = "sha256:2f10cf143e4a9bb0f4f5af568a00df94a2d69ef41c2579584454bb0fe5cc642c"},
    {file = "librt-0.11.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:78dc31f7fdfe9c9d0eb0e8f42d139db230e826415bbcabd9f0e9faaaee909894"},
    {file = "librt-0.11.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:fa475675db22290c3158e1d42326d0f5a65f04f44a0e68c3630a25b53560fb9c"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:621db29691044bdeda22e789e482e1b0f3a985d90e3426c9c6d17606416205ea"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:a9010e2ed5b3a9e158c5fd966b3ab7e834bb3d3aacc8f66c91dd4b57a3799230"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7c39513d8b7477a2e1ed8c43fc21c524e8d5a0f8d4e8b7b074dbdbe7820a08e2"},
    {file = "librt-0.11.0-cp313-cp313-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7aef3cf1d5af86e770ab04bfd993dfc4ae8b8c17f66fb77dd4a7d50de7bbb1a3"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:557183ddc36babe46b27dd60facbd5adb4492181a5be887587d57cda6e092f21"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:83d3e1f72bd42f6c5c0b7daec530c3f829bd02db42c70b8ddf0c2d90a2459930"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:4ce1f21fbe589bc1afd7872dece84fb0e1144f794a288e58a10d2c54a55c43be"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b09f7044ea2b64c9da42fd3d335666518cfd1c6e8a182c95da73d0214b41e"},
    {file = "librt-0.11.0-cp313-cp313-win32.whl", hash = "sha256:78fddc31cd4d3caa897ad5d31f856b1faadc9474021ad6cb182b9018793e254e"},
    {file = "librt-0.11.0-cp313-cp313-win_amd64.whl", hash = "sha256:8ca8aa88751a775870b764e93bad5135385f563cb8dcee399abf034ea4d3cb47"},
    {file = "librt-0.11.0-cp313-cp313-win_arm64.whl", hash = "sha256:96f044bb325fd9cf1a723015638c219e9143f0dfbc0ca54c565df2b7fc748b44"},
    {file = "librt-0.11.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:4a017a95e5837dc15a8c5661d60e05daa96b90908b1aa6b7acdf443cd25c8ebd"},
    {file = "librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:b1ecbd9819deccc39b7542bf4d2a740d8a620694d39989e58661d3763458f8d4"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7da327dacd7be8f8ec36547373550744a3cc0e536d54665cd83f8bcd961200e8"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:0dc56b1f8d06e60db362cc3fdae206681817f86ce4725d34511473487f12a34b"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:05fb8fb2ab90e21c8d12ea240d744ad514da9baf381ebfa70d91d20d21713175"},
    {file = "librt-0.11.0-cp314-cp314-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cae74872be221df4374d10fec61f93ed1513b9546ea84f2c0bf73ab3e9bd0b03"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:32bcc918c0148eb7e3d57385125bac7e5f9e4359d05f07448b09f6f778c2f31c"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f9743fc99135d5f78d2454435615f6dec0473ca507c26ce9d92b10b562a280d3"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:5ba067f4aadae8fda802d91d2124c90c42195ff32d9161d3549e6d05cfe26f96"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:de3bf945454d032f9e390b85c4072e0a0570bf825421c8be0e71209fa65e1abe"},
    {file = "librt-0.11.0-cp314-cp314-win32.whl", hash = "sha256:d2277a05f6dcb9fd13db9566aac4fabd68c3ea1ea46ee5567d4eef8efa495a2f"},
    {file = "librt-0.11.0-cp314-cp314-win_amd64.whl", hash = "sha256:ab73e8db5e3f564d812c1f5c3a175930a5f9bc96ccb5e3b22a34d7858b401cf7"},
    {file = "librt-0.11.0-cp314-cp314-win_arm64.whl", hash = "sha256:aea3caa317752e3a466fa8af45d91ee0ea8c7fdd96e42b0a8dd9b76a7931eba1"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:d1b36540d7aaf9b9101b3a6f376c8d8e9f7a9aec93ed05918f2c69d493ffef72"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:efbb343ab2ce3540f4ecbe6315d677ed70f37cd9a72b1e58066c918ca83acbaa"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:aa0dd688aab3f7914d3e6e5e3554978e0383312fb8e771d84be008a35b9ee548"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:f5fb36b8c6c63fdcbb1d526d94c0d1331610d43f4118cc1beb4efef4f3faacb2"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4a9a237d13addb93715b6fee74023d5ee3469b53fce527626c0e088aa585805f"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5ddd17bd87b2c56ddd60e546a7984a2e64c4e8eab92fb4cf3830a48ad5469d51"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:bd43992b4473d42f12ff9e68326079f0696d9d4e6000e8f39a0238d482ba6ee2"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:f8e3e8056dd674e279741485e2e512d6e9a751c7455809d0114e6ebf8d781085"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:c1f708d8ae9c56cf38a903c44297243d2ec83fd82b396b977e0144a3e76217e3"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0add982e0e7b9fc14cf4b33789d5f13f66581889b88c2f58099f6ce8f92617bd"},
    {file = "librt-0.11.0-cp314-cp314t-win32.whl", hash = "sha256:2b481d846ac894c4e8403c5fd0e87c5d11d6499e404b474602508a224ff531c8"},
    {file = "librt-0.11.0-cp314-cp314t-win_amd64.whl", hash = "sha256:28edb433edde181112a908c78907af28f964eabc15f4dd16c9d66c834302677c"},
    {file = "librt-0.11.0-cp314-cp314t-win_arm64.whl", hash = "sha256:dee008f20b542e3cd162ba338a7f9ec0f6d23d395f66fe8aeeec3c9d067ea253"},
    {file = "librt-0.11.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6bd72d903911d995ab666dbd1871f8b1e80925a699af8063fbf50053329fb05f"},
    {file = "librt-0.11.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0ef69ac715f3cd8e5cd252cb2aebfa72c015492aacc339d5d7bf8fef3c62c677"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:624a40c4a4ad7773315c287276cd024509b2c66ff5904f504bfc08d2c70293ab"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:41dc19fe150b69716c8ece4f76773a9e8813fe3e35e032a58b4d46423fb8d7c0"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4e8bd98ea9c47ae90b319a087ab28dac493f1ffbc1ecd1f28fcdbf3b7e1108d1"},
    {file = "librt-0.11.0-cp39-cp39-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:84308fc49423ce6475d1c5d1985cd69a8ca9f0325fc7d5f81bb690a3f3625d4e"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:ff0fbaf5f44a21beeb0110f2ab64f45135a9536a834b79c0d1ef018f2786bbfa"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9c028a9442a18e266955d364ce42259136e79a7ba14d773e0d778d5f70cd56f1"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:9f1692105a02bcf853f355032a5fdc5494358ef83d8fd22d16de375c85cec3f5"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7a80a71e1fda83cc752a9141e87aae7fef279538597564d670e9ce513f286192"},
    {file = "librt-0.11.0-cp39-cp39-win32.whl", hash = "sha256:140695816ddf3c86eb972981a26f35efd871c44b0c3aed44c8cd01749386617f"},
    {file = "librt-0.11.0-cp39-cp39-win_amd64.whl", hash = "sha256:92f7ff819c197fc30473190a12c2856f325ac90aabfccbeb2072d28cc2e234e3"},
    {file = "librt-0.11.0.tar.gz", hash = "sha256:075dc3ef4458a278e0195cbf6ac9d38808d9b906c5a6c7f7f79c3888276a3fb1"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mypy"
version = "2.1.0"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "mypy-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:11a6beb180257a805961aea9ec591bbd0bd17f1e18d35b8456d57aee5bedfedc"},
    {file = "mypy-2.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8ef78c1d306bbf9a8a12f526c44902c9c28dffd6c52c52bf6a72641ce18d3849"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c209a90853081ff01d01ee895cafe10f7db1474e0d95beaeef0f6c1db9119bbd"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:47cebf61abde7c088a4e27718a8b13a81655686b2e9c251f5c0915a802248166"},
    {file = "mypy-2.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:d57a90ae5e872138a425ec328edbc9b235d1934c4377881a33ec05b341acc9a8"},
    {file = "mypy-2.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:aea7f7a8a55b459c34275fc468ada6ca7c173a5e43a68f5dbe588a563d8a06b8"},
    {file = "mypy-2.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:c989640253f0d76843e9c6c1bbf4bd48c5e85ada61bde4beb37cb3eca035685e"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a683016b16fe2f572dc04c72be7ee0504ac1605a265d0200f5cea695fb788f41"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a293c534adb55271fef24a26da04b855540a8c13cc07bc5917b9fd2c394f2ca"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7406f4d048e71e576f5356d317e5b0a9e666dfd966bd99f9d14ca06e1a341538"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0210d626fc8b31ccc90233754c7bc90e1f43205e85d96387f7db1285b55c398"},
    {file = "mypy-2.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3712c20deed54e814eaaa825603bada8ea1c390670a397c95b98405347acc563"},
    {file = "mypy-2.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fcaa0e479066e31f7cceb6a3bea39cb22b2ff51a6b2f24f193d19179ba17c389"},
    {file = "mypy-2.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:0b1a5260c95aa443083f9ed3592662941951bca3d4ca224a5dc517c38b7cf666"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:244358bf1c0da7722230bce60683d52e8e9fd030554926f15b747a84efb5b3af"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4ec7c57657493c7a75534df2751c8ae2cda383c16ecc55d2106c54476b1b16f6"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8161b6ff4392410023224f0969d17db93e1e154bc3e4ba62598e720723ae211"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bf03e12003084a67395184d3eb8cbd6a489dc3655b5664b28c210a9e2403ab0b"},
    {file = "mypy-2.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:20509760fd791c51579d573153407d226385ec1f8bcce55d730b354f3336bc22"},
    {file = "mypy-2.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:6753d0c1fdd6b1a23b9e4f283ce80b2153b724adcb2653b20b85a8a28ac6436b"},
    {file = "mypy-2.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:98ebb6589bb3b6d0c6f0c459d53ca55b8091fbc13d277c4041c885392e8195e8"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:35aac3bb114e03888f535d5eb51b8bafbb3266586b599da1940f9b1be3ec5bd5"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8de55a8c861f2a49331f807be98d90caeceeef520bde13d43a160207f8af613e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5fdf2941a07434af755837d9880f7d7d25f1dacb1af9dcd4b9b66f2220a3024e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e195b817c13f02352a9c124301f9f30f078405444679b6753c1b96b6eed37285"},
    {file = "mypy-2.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5431d42af987ebd92ba2f71d45c85ed41d8e6ca9f5fd209a69f68f707d2469e5"},
    {file = "mypy-2.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:767fe8c66dc3e01e19e1737d4c38ebefead16125e1b8e58ad421903b376f5c65"},
    {file = "mypy-2.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:ecfe70d43775ab99562ab128ce49854a362044c9f894961f68f898c23cb7429d"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:7354c5a7f69d9345c3d6e69921d57088eea3ddeeb6b20d34c1b3855b02c36ec2"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:49890d4f76ac9e06ec117f9e09f3174da70a620a0c300953d8595c926e80947f"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:761be68e023ef5d94678772396a8af1220030f80837a3afd8d0aef3b419666f4"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c90345fc182dc363b891350457ec69c35140858538f38b4540845afcc32b1aef"},
    {file = "mypy-2.1.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b84802e7b5a6daf1f5e15bc9fcd7ddae77be13981ffab037f1c67bb84d67d135"},
    {file = "mypy-2.1.0-cp314-cp314-win_amd64.whl", hash = "sha256:022c771234936ceac541ebaf836fe9e2abeb3f5e09aff21588fe543ff006fe21"},
    {file = "mypy-2.1.0-cp314-cp314-win_arm64.whl", hash = "sha256:498207db725cec88829a6a5c2fc771205fd043719ef98bc49aba8fb9fc4e6d57"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:7d5e5cad0efeba72b93cd17490cc0d69c5ac9ca132994fe3fb0314808aeeb83e"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ff715050c127d724fd260a2e666e7747fdd83511c0c47d449d98238970aef780"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:82208da9e09414d520e912d3e462d454854bed0810b71540bb016dcbca7308fd"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e79ebc1b904b84f0310dff7469655a9c36c7a68bddb37bdd42b67a332df61d08"},
    {file = "mypy-2.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e583edc957cfb0deb142079162ae826f58449b116c1d442f2d91c69d9fced081"},
    {file = "mypy-2.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b33b6cd332695bba180d55e717a79d3038e479a2c49cc5eb3d53603409b9a5d7"},
    {file = "mypy-2.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:4f910fe825376a7b66ef7ca8c98e5a149e8cd64c19ae71d84047a74ee060d4e6"},
    {file = "mypy-2.1.0-py3-none-any.whl", hash = "sha256:a663814603a5c563fb87a4f96fb473eeb30d1f5a4885afcf44f9db000a366289"},
    {file = "mypy-2.1.0.tar.gz", hash = "sha256:81e76ad12c2d804512e9b13240d1588316531bfba07558286078bfbce9613633"},
]

[package.dependencies]
ast-serialize = ">=0.3.0,<1.0.0"
librt = {version = ">=0.11.0", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=1.0.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = [
    {version = ">=4.6.0", markers = "python_version < \"3.15\""},
    {version = ">=4.14.0", markers = "python_version >= \"3.15\""},
]

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
reports = ["lxml"]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "ni-datamonikers-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI data moniker gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_datamonikers_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:77d078d810656b3e90152a065047c6203140e0998e8cbdf9d2dbb6e9f477840e"},
    {file = "ni_datamonikers_v1_proto-1.0.0.tar.gz", hash = "sha256:2e4cf30f9dee343af4a5f328fb785320d2eb30705abc15f0695057177afd5f00"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-datastore"
version = "2.0.0.dev1"
description = "APIs for publishing and retrieving data from NI Measurement Data Services"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_datastore-2.0.0.dev1-py3-none-any.whl", hash = "sha256:31236c2ad091b11617553cec93671a4d8c45fca9e9364583092bd6b19ca716fc"},
    {file = "ni_datastore-2.0.0.dev1.tar.gz", hash = "sha256:254437977771517a379c1327958364cbda6cd3ad2a6cb2c28d42d145b0b9923e"},
]

[package.dependencies]
hightime = ">=1.0.0"
ni-measurements-data-v1-client = ">=1.1.0"
ni-measurements-metadata-v1-client = ">=1.0.0"
ni-protobuf-types = ">=1.2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-data-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Data Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:dfc38d56fdd710a930fbc05383d43ab96f64aee545937f9ef605a3bb6f88cc31"},
    {file = "ni_measurements_data_v1_client-1.1.0.tar.gz", hash = "sha256:16b1ac8b82277e41719aa8b1aeae3f1040dba47e63651f83e30fe115cd036278"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-data-v1-proto = ">=1.1.0"

[[package]]
name = "ni-measurements-data-v1-proto"
version = "1.1.0"
description = "Protobuf data types and service stubs for NI data store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:06096cea733717b60281c92d0a1b44eac97194781507ba4fd9b3aa080a4450df"},
    {file = "ni_measurements_data_v1_proto-1.1.0.tar.gz", hash = "sha256:df1ca7ce3603dd5a0adc8795f0844da9a78ddc026f219bf596957cf3ed08da3d"},
]

[package.dependencies]
ni-datamonikers-v1-proto = ">=1.0.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"
ni-protobuf-types = ">=1.2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-metadata-v1-client"
version = "1.0.0"
description = "gRPC Client for NI Metadata Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_client-1.0.0-py3-none-any.whl", hash = "sha256:c697ce4e98105b810f4da844a598e86e359ff6c90ca7a832e1e23a70327551a7"},
    {file = "ni_measurements_metadata_v1_client-1.0.0.tar.gz", hash = "sha256:9f9a10810c4c6693239081abbc026414a18df3e3d04daa3cd59010b1eed07f51"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"

[[package]]
name = "ni-measurements-metadata-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI metadata store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:8844806d6775ac65144100fcd03099aea0c17ed55de696683d0663166f45cee3"},
    {file = "ni_measurements_metadata_v1_proto-1.0.0.tar.gz", hash = "sha256:3283cf7f0c452812a311b2b9274b5ba1e549f994f6a978a125f1746b85746e6f"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.2.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_protobuf_types-1.2.0-py3-none-any.whl", hash = "sha256:461c4825571d0054fd5427664403c3d69fcd180c9c00868ac1911693dd9bf901"},
    {file = "ni_protobuf_types-1.2.0.tar.gz", hash = "sha256:e8226f8ef44b104ffb1b1f6e416511c416be4d91bf5c2633db7ab58294e037bb"},
]

[package.dependencies]
nitypes = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["lint"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "nisyscfg"
version = "0.2.1"
description = "NI System Configuration Python API"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "nisyscfg-0.2.1-py3-none-any.whl", hash = "sha256:47e95ae72e4265407a145ede09099e3b1dbbb62be232c2f59d92ff1288a49184"},
]

[package.dependencies]
hightime = "*"
six = "*"

[[package]]
name = "nitypes"
version = "1.1.0"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "nitypes-1.1.0-py3-none-any.whl", hash = "sha256:b43ac7027e1cceeca7ceffa58f31ffadd03feeb1788ca5cb8f9d105e73893b14"},
    {file = "nitypes-1.1.0.tar.gz", hash = "sha256:f273b5131ef0d5b848c37a0a63452626caf5c2938f7744c324f7991b76fa0b60"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main"]
markers = "python_version < \"3.12\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.5.0"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.12"
groups = ["main"]
markers = "python_version >= \"3.12\""
files = [
    {file = "numpy-2.5.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:489780423903667933b4ed6197b6ec3b75ea5dd17d1d8f0f38d798feb6921561"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ece55976ced6bca95a03ae2839e2e5ccffe8eb6a3e7022415645eb154a81e4e6"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:c83b664b0e6eee9594fa920cf0639d8af796606d3fad6cc70180c87e4b97c7be"},
    {file = "numpy-2.5.0-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:bf80333980bf37f523341ddd72c783f39d6829ec7736b9eb99086388a2d52cc2"},
    {file = "numpy-2.5.0-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a1a4874217b36d5ac8fc876f52e39df56f8182c88463e9e2dceabf7ca8b7efb8"},
    {file = "numpy-2.5.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:aaa760137137e8d3c920d27927748215b56014f92667dc9b6c27dfc61249255a"},
    {file = "numpy-2.5.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:7174ce8265fc7f7417d171c9ea8fe905220748893ea67a2a7abe726ec331c4b0"},
    {file = "numpy-2.5.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b8c3daaf99de52415d20b42f8e8155c78642cb04207d02f9d317a0dcf1b3fb54"},
    {file = "numpy-2.5.0-cp312-cp312-win32.whl", hash = "sha256:6206db0af545d73d068add6d992279145f158428d1da6cc49adc4b630c5d6ee5"},
    {file = "numpy-2.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:6f2d6873e2940c860a309d21e25b1e69af6aaffdd80aa056b04c16380db1c4f2"},
    {file = "numpy-2.5.0-cp312-cp312-win_arm64.whl", hash = "sha256:a55e1eb2bca2cfd17a16b213c99dfc8502d47b0d494224d2122277d0400935ca"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:520e6b8be0a4b65840ac8090d4f51cef4bed66e2b0894d5a520f099adc24a9b2"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:146b81cdd3967fdb6beca8ba25f00c58741d8f3cbd797f55af0fbe0bfec3469c"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:126b88d95e8ff9b00c9e717aa540469f21d6180162f84c0caec51b16215d49cd"},
    {file = "numpy-2.5.0-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:d4313cef1594c5ce46c31b6e54e918338f63f16ee9322304e8c9114d6d81c8bd"},
    {file = "numpy-2.5.0-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:750fb097caf26fa878746d9d119f6f9da12dedcbff1eea966c3e3447647c4a9e"},
    {file = "numpy-2.5.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3893adc2dc7c0412ba76777db55a049215d99c9aa3113003be8f49f4f1290ab9"},
    {file = "numpy-2.5.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:835e454dd99b238cdc5a3f63bce2371296f5ebc53ca1e0f8e6ddbb6d92a29aab"},
    {file = "numpy-2.5.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6f9836778081a0a3c02a6a21493f3e9f5b311f8d2541934f31f05583dc999ea4"},
    {file = "numpy-2.5.0-cp313-cp313-win32.whl", hash = "sha256:0b525be4744b60bb0557ac872d53ef07d085b5f39622bc579c98d3809d05b988"},
    {file = "numpy-2.5.0-cp313-cp313-win_amd64.whl", hash = "sha256:44353e2878930039db472b99dc353d749826e4010bd4d2a7f835e94a97a5c748"},
    {file = "numpy-2.5.0-cp313-cp313-win_arm64.whl", hash = "sha256:48f54b00711f83a5f796b70c518e8c2b3c5848dda03a54911f23eb68519b9b60"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:f27582c55ba4c750b7c58c8faf021d2cd9324a662b466229db8a417b41368af9"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:28e7137057d551e4a83c4ae414e3451f50568409db7569aacc7f9811ee06a446"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:e1da54b53e75cd9fcfc23efcc7edab2c6aecf97b6037566d8a0fe804af8ec57c"},
    {file = "numpy-2.5.0-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:694d8f74e156f7fd01179f1aa8faa2f648ab6ae0f70b6c3fe57a03249aea2303"},
    {file = "numpy-2.5.0-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1a7569a7b53c77716f036bb28cb1c91f166a26ec7d9502cd1e4bdfe502fdec22"},
    {file = "numpy-2.5.0-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:39a0433bd4086ebd462960cf375e19195bb07b53dc1d87dd5fcf47ad78576f03"},
    {file = "numpy-2.5.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:929f0c79ac38bcbd7154fe631dc907abfeddbcc5027a896bd1f7767323271e7a"},
    {file = "numpy-2.5.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:cc4f247a47bbf070bfd70be53ccdcf47b800af563535e7bbe172322197c30e21"},
    {file = "numpy-2.5.0-cp314-cp314-win32.whl", hash = "sha256:5dc71423499fab3f46f7a7201155ade1669ea101f2f429d332df9e72f8161731"},
    {file = "numpy-2.5.0-cp314-cp314-win_amd64.whl", hash = "sha256:ebb81d9d5443e0309d6c54894c3fbed74ad7da0714352a67b6d773cd189eae73"},
    {file = "numpy-2.5.0-cp314-cp314-win_arm64.whl", hash = "sha256:3b94d0d0deceebfad3e67ae5c0e5eb87371e8f7a0581cd04a779928c2450cf1e"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:22f3d43e362d650bc39db1f17851302874a148ca95ba6981c1dfb5fa6862f35b"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:243563efb4cd7528a264567e9fd206c87826457322521d06206a00bfa316c927"},
    {file = "numpy-2.5.0-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:84881d825ca75249b189bbee875fcfe3238aa5c479e6100893cda566e8e86826"},
    {file = "numpy-2.5.0-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:cda12aa4779d42b8771180aba759c96f527d43446d8f380ab59e2b35e8489efd"},
    {file = "numpy-2.5.0-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c0121101093d2bd74981b10f8837d78e794a8ff57834eb27179f49e1ba11ac6"},
    {file = "numpy-2.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d371c92cfa09da00022f501ab67fafaea813d752eb30ac44336d45b1e5b0268a"},
    {file = "numpy-2.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:9990713e9c38154c6861e7547f1e3fc7a87e75ff09bab24ef1cc81d81c2835e9"},
    {file = "numpy-2.5.0-cp314-cp314t-win32.whl", hash = "sha256:edadfbd4794b1086c0d822f81863e8a68fc129d132fd0bb9e31e955d7fbbbdb7"},
    {file = "numpy-2.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:f7e5fa4382967ae6548bd2f174219afb908e294b0d5f625af01166edd5f7d9aa"},
    {file = "numpy-2.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:016623417bb330d719d579daf2d6b9a01ddc52e41a9ed61a47f39fde46dcd865"},
    {file = "numpy-2.5.0.tar.gz", hash = "sha256:5a129578019311b6e56bdd714250f19b518f7dceeeb8d1af5490f4942d3f891c"},
]

[[package]]
name = "packaging"
version = "26.2"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "packaging-26.2-py3-none-any.whl", hash = "sha256:5fc45236b9446107ff2415ce77c807cee2862cb6fac22b8a73826d0693b0980e"},
    {file = "packaging-26.2.tar.gz", hash = "sha256:ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"},
]

[[package]]
name = "pathspec"
version = "1.1.1"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pathspec-1.1.1-py3-none-any.whl", hash = "sha256:a00ce642f577bf7f473932318056212bc4f8bfdf53128c78bbd5af0b9b20b189"},
    {file = "pathspec-1.1.1.tar.gz", hash = "sha256:17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]

[[package]]
name = "pep8-naming"
version = "0.15.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.10.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "platformdirs-4.10.0-py3-none-any.whl", hash = "sha256:fb516cdb12eb0d857d0cd85a7c57cea4d060bee4578d6cf5a14dfdf8cbf8784a"},
    {file = "platformdirs-4.10.0.tar.gz", hash = "sha256:31e761a6a0ca04faf7353ea759bdba55652be214725111e5aac52dfa29d4bef7"},
]

[[package]]
name = "protobuf"
version = "7.35.1"
description = ""
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "protobuf-7.35.1-cp310-abi3-macosx_10_9_universal2.whl", hash = "sha256:24f857477359a85c0c235261b8ba905fd51b2562f4a64ca1df5473f29850cbf6"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_aarch64.whl", hash = "sha256:11d6b0ec246892d85215b0a13ca6e0233cf5284b68f0ac02646427f4ff88a799"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_s390x.whl", hash = "sha256:b73f9489a4b8b1c9cb1f8ed951c736392592edb24b9d6819f36d2e10b171d5b4"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl", hash = "sha256:74758715c53d7158fb76caf4f0cfdacc5329a4b1bb994f865d6cf302d413a1c4"},
    {file = "protobuf-7.35.1-cp310-abi3-win32.whl", hash = "sha256:353652e4efd0bca5b5fc2656abf8307ef351f0cf938c9eba09f0e09c20a25c30"},
    {file = "protobuf-7.35.1-cp310-abi3-win_amd64.whl", hash = "sha256:230a75ddfc2de4806e56696ce9640c1cdfdb6543b7cfce98d42a4c0a0e7bdb87"},
    {file = "protobuf-7.35.1-py3-none-any.whl", hash = "sha256:4bc97768d8fe4ad6743c8a19403e314511ed9f6d13205b687e52421c023ac1b9"},
    {file = "protobuf-7.35.1.tar.gz", hash = "sha256:ce115a26fe0c39a2c29973d914d327e516a6455464489fe3cd1e51a1b354f81a"},
]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3) ; python_version < \"3.11\""]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pytokens"
version = "0.4.1"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "pytokens-0.4.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2a44ed93ea23415c54f3face3b65ef2b844d96aeb3455b8a69b3df6beab6acc5"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:add8bf86b71a5d9fb5b89f023a80b791e04fba57960aa790cc6125f7f1d39dfe"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:670d286910b531c7b7e3c0b453fd8156f250adb140146d234a82219459b9640c"},
    {file = "pytokens-0.4.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4e691d7f5186bd2842c14813f79f8884bb03f5995f0575272009982c5ac6c0f7"},
    {file = "pytokens-0.4.1-cp310-cp310-win_amd64.whl", hash = "sha256:27b83ad28825978742beef057bfe406ad6ed524b2d28c252c5de7b4a6dd48fa2"},
    {file = "pytokens-0.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d70e77c55ae8380c91c0c18dea05951482e263982911fc7410b1ffd1dadd3440"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4a58d057208cb9075c144950d789511220b07636dd2e4708d5645d24de666bdc"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b49750419d300e2b5a3813cf229d4e5a4c728dae470bcc89867a9ad6f25a722d"},
    {file = "pytokens-0.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:d9907d61f15bf7261d7e775bd5d7ee4d2930e04424bab1972591918497623a16"},
    {file = "pytokens-0.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:ee44d0f85b803321710f9239f335aafe16553b39106384cef8e6de40cb4ef2f6"},
    {file = "pytokens-0.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:140709331e846b728475786df8aeb27d24f48cbcf7bcd449f8de75cae7a45083"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d6c4268598f762bc8e91f5dbf2ab2f61f7b95bdc07953b602db879b3c8c18e1"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:24afde1f53d95348b5a0eb19488661147285ca4dd7ed752bbc3e1c6242a304d1"},
    {file = "pytokens-0.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5ad948d085ed6c16413eb5fec6b3e02fa00dc29a2534f088d3302c47eb59adf9"},
    {file = "pytokens-0.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:3f901fe783e06e48e8cbdc82d631fca8f118333798193e026a50ce1b3757ea68"},
    {file = "pytokens-0.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8bdb9d0ce90cbf99c525e75a2fa415144fd570a1ba987380190e8b786bc6ef9b"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5502408cab1cb18e128570f8d598981c68a50d0cbd7c61312a90507cd3a1276f"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29d1d8fb1030af4d231789959f21821ab6325e463f0503a61d204343c9b355d1"},
    {file = "pytokens-0.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b08dd6b86058b6dc07efe9e98414f5102974716232d10f32ff39701e841c4"},
    {file = "pytokens-0.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:9bd7d7f544d362576be74f9d5901a22f317efc20046efe2034dced238cbbfe78"},
    {file = "pytokens-0.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4a14d5f5fc78ce85e426aa159489e2d5961acf0e47575e08f35584009178e321"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97f50fd18543be72da51dd505e2ed20d2228c74e0464e4262e4899797803d7fa"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dc74c035f9bfca0255c1af77ddd2d6ae8419012805453e4b0e7513e17904545d"},
    {file = "pytokens-0.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f66a6bbe741bd431f6d741e617e0f39ec7257ca1f89089593479347cc4d13324"},
    {file = "pytokens-0.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:b35d7e5ad269804f6697727702da3c517bb8a5228afa450ab0fa787732055fc9"},
    {file = "pytokens-0.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:8fcb9ba3709ff77e77f1c7022ff11d13553f3c30299a9fe246a166903e9091eb"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79fc6b8699564e1f9b521582c35435f1bd32dd06822322ec44afdeba666d8cb3"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d31b97b3de0f61571a124a00ffe9a81fb9939146c122c11060725bd5aea79975"},
    {file = "pytokens-0.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:967cf6e3fd4adf7de8fc73cd3043754ae79c36475c1c11d514fc72cf5490094a"},
    {file = "pytokens-0.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:584c80c24b078eec1e227079d56dc22ff755e0ba8654d8383b2c549107528918"},
    {file = "pytokens-0.4.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:da5baeaf7116dced9c6bb76dc31ba04a2dc3695f3d9f74741d7910122b456edc"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:11edda0942da80ff58c4408407616a310adecae1ddd22eef8c692fe266fa5009"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0fc71786e629cef478cbf29d7ea1923299181d0699dbe7c3c0f4a583811d9fc1"},
    {file = "pytokens-0.4.1-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:dcafc12c30dbaf1e2af0490978352e0c4041a7cde31f4f81435c2a5e8b9cabb6"},
    {file = "pytokens-0.4.1-cp38-cp38-win_amd64.whl", hash = "sha256:42f144f3aafa5d92bad964d471a581651e28b24434d184871bd02e3a0d956037"},
    {file = "pytokens-0.4.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:34bcc734bd2f2d5fe3b34e7b3c0116bfb2397f2d9666139988e7a3eb5f7400e3"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941d4343bf27b605e9213b26bfa1c4bf197c9c599a9627eb7305b0defcfe40c1"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3ad72b851e781478366288743198101e5eb34a414f1d5627cdd585ca3b25f1db"},
    {file = "pytokens-0.4.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:682fa37ff4d8e95f7df6fe6fe6a431e8ed8e788023c6bcc0f0880a12eab80ad1"},
    {file = "pytokens-0.4.1-cp39-cp39-win_amd64.whl", hash = "sha256:30f51edd9bb7f85c748979384165601d028b84f7bd13fe14d3e065304093916a"},
    {file = "pytokens-0.4.1-py3-none-any.whl", hash = "sha256:26cef14744a8385f35d0e095dc8b3a7583f6c953c2e3d269c7f82484bf5ad2de"},
    {file = "pytokens-0.4.1.tar.gz", hash = "sha256:292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "312"
description = "Python for Windows Extensions"
optional = false
python-versions = ">=3.9"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-312-cp310-cp310-win32.whl", hash = "sha256:772235332b5d1024c696f11cea1ae4be7930f0a8b894bb43db14e3f435f1ff7e"},
    {file = "pywin32-312-cp310-cp310-win_amd64.whl", hash = "sha256:5dbc35d2b5320dc07f25fa31269cfb767471002b17de5eb067d03da68c7cb2db"},
    {file = "pywin32-312-cp310-cp310-win_arm64.whl", hash = "sha256:3020656e34f1cf7faeb7bccd2b84653a607c6ff0c55ada85e6487d61716deabd"},
    {file = "pywin32-312-cp311-cp311-win32.whl", hash = "sha256:17948aeadbdb091f0ced6ef0841620794e68327b94ee415571c1203594b7215c"},
    {file = "pywin32-312-cp311-cp311-win_amd64.whl", hash = "sha256:d11417d84412f859b722fad0841b3614459ed0047f7542d8362e77884f6b6e8a"},
    {file = "pywin32-312-cp311-cp311-win_arm64.whl", hash = "sha256:b2200a054ca6d6625c4842fc56a4976a4b47f96b73dbe5538c3f813a80359f47"},
    {file = "pywin32-312-cp312-cp312-win32.whl", hash = "sha256:dab4f65ac9c4e48400a2a0530c46c3c579cd5905ecd11b80692373915269208b"},
    {file = "pywin32-312-cp312-cp312-win_amd64.whl", hash = "sha256:b457f6d628a47e8a7346ce22acb7e1a46a4a78b52e1d17e1af56871bd19a93bc"},
    {file = "pywin32-312-cp312-cp312-win_arm64.whl", hash = "sha256:6017c58e12f6809fbb0555b75df144c2922a9ffd18e4b9b5afa863b6c1a9d950"},
    {file = "pywin32-312-cp313-cp313-win32.whl", hash = "sha256:7a27df850933d16a8eabfbaeb73d52b273e2da667f80d70b01a89d1f6828d02c"},
    {file = "pywin32-312-cp313-cp313-win_amd64.whl", hash = "sha256:c53e878d15a1c44788082bfe712a905433473aa38f86375b7cf8b45e3acbaaf9"},
    {file = "pywin32-312-cp313-cp313-win_arm64.whl", hash = "sha256:59aba5d5940842075343a5ddc6b11f1cdf0d1567fe745290359dfbcc7c2eb831"},
    {file = "pywin32-312-cp314-cp314-win32.whl", hash = "sha256:a77a90fbb6881238d2ca9c6fd797b25817f3768fe78d214a90137ff055a75f5b"},
    {file = "pywin32-312-cp314-cp314-win_amd64.whl", hash = "sha256:a4dd3a848290ef724347b19f301045831d8e802fa4464f491b98b1e0a081432e"},
    {file = "pywin32-312-cp314-cp314-win_arm64.whl", hash = "sha256:9fce94568364e0155e6dfb781ac5d95903be8baf28670632beab1b523f300daa"},
    {file = "pywin32-312-cp315-cp315-win32.whl", hash = "sha256:5c1fbe4a937a73ae9297384a3da38518cbc694c68ad8a809b2e19acd350f03ed"},
    {file = "pywin32-312-cp315-cp315-win_amd64.whl", hash = "sha256:c2f03a0f73f804a13c2735b99392b0cd426bb4f2c4d0178e5ac966a0f21618d5"},
    {file = "pywin32-312-cp315-cp315-win_arm64.whl", hash = "sha256:a8597d28f267b39074aef51fa593530082b39cbe5a074226096857b1fed2dfb9"},
    {file = "pywin32-312-cp39-cp39-win32.whl", hash = "sha256:d620900033cc7531e50727c3c8333091df5dd3ffe6d68cdca38c03f5821408d5"},
    {file = "pywin32-312-cp39-cp39-win_amd64.whl", hash = "sha256:dc90147579a905b8635e1b0ec6514967dcb07e6e0d9c42f1477feef14cac23bb"},
    {file = "pywin32-312-cp39-cp39-win_arm64.whl", hash = "sha256:02ebca0f0242b75292e218065004310d6a477407c09fa449bfe4f6022bc0c0fc"},
]

[[package]]
name = "setuptools"
version = "81.0.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "setuptools-81.0.0-py3-none-any.whl", hash = "sha256:fdd925d5c5d9f62e4b74b30d6dd7828ce236fd6ed998a08d81de62ce5a6310d6"},
    {file = "setuptools-81.0.0.tar.gz", hash = "sha256:487b53915f52501f0a79ccfd0c02c165ffe06631443a886740b91af4b7a5845a"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.13.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.18.*)", "pytest-mypy"]

[[package]]
name = "six"
version = "1.17.0"
description = "Python 2 and 3 compatibility utilities"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["main"]
files = [
    {file = "six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274"},
    {file = "six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81"},
]

[[package]]
name = "snowballstemmer"
version = "3.1.1"
description = "This package provides 36 stemmers for 34 languages generated from Snowball algorithms."
optional = false
python-versions = ">=3.3"
groups = ["lint"]
files = [
    {file = "snowballstemmer-3.1.1-py3-none-any.whl", hash = "sha256:7e207fa178741da09cdee59d3ecec3827ad5f92b1fc5c9ff3755b639f71f5752"},
    {file = "snowballstemmer-3.1.1.tar.gz", hash = "sha256:e07bbc54a0d798fe6010a12398422e62a8bfbba95c394fd0956ef58cb4d3e260"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["lint"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.4.1"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f8f0fc26ec2cc2b965b7a3b87cd19c5c6b8c5e5f436b984e85f486d652285c30"},
    {file = "tomli-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ab97e64ccda8756376892c53a72bd1f964e519c77236368527f758fbc36a53a"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:96481a5786729fd470164b47cdb3e0e58062a496f455ee41b4403be77cb5a076"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a881ab208c0baf688221f8cecc5401bd291d67e38a1ac884d6736cbcd8247e9"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:47149d5bd38761ac8be13a84864bf0b7b70bc051806bc3669ab1cbc56216b23c"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ec9bfaf3ad2df51ace80688143a6a4ebc09a248f6ff781a9945e51937008fcbc"},
    {file = "tomli-2.4.1-cp311-cp311-win32.whl", hash = "sha256:ff2983983d34813c1aeb0fa89091e76c3a22889ee83ab27c5eeb45100560c049"},
    {file = "tomli-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:5ee18d9ebdb417e384b58fe414e8d6af9f4e7a0ae761519fb50f721de398dd4e"},
    {file = "tomli-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:c2541745709bad0264b7d4705ad453b76ccd191e64aa6f0fc66b69a293a45ece"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:c742f741d58a28940ce01d58f0ab2ea3ced8b12402f162f4d534dfe18ba1cd6a"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7f86fd587c4ed9dd76f318225e7d9b29cfc5a9d43de44e5754db8d1128487085"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ff18e6a727ee0ab0388507b89d1bc6a22b138d1e2fa56d1ad494586d61d2eae9"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:136443dbd7e1dee43c68ac2694fde36b2849865fa258d39bf822c10e8068eac5"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5e262d41726bc187e69af7825504c933b6794dc3fbd5945e41a79bb14c31f585"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5cb41aa38891e073ee49d55fbc7839cfdb2bc0e600add13874d048c94aadddd1"},
    {file = "tomli-2.4.1-cp312-cp312-win32.whl", hash = "sha256:da25dc3563bff5965356133435b757a795a17b17d01dbc0f42fb32447ddfd917"},
    {file = "tomli-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:52c8ef851d9a240f11a88c003eacb03c31fc1c9c4ec64a99a0f922b93874fda9"},
    {file = "tomli-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:f758f1b9299d059cc3f6546ae2af89670cb1c4d48ea29c3cacc4fe7de3058257"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:36d2bd2ad5fb9eaddba5226aa02c8ec3fa4f192631e347b3ed28186d43be6b54"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:eb0dc4e38e6a1fd579e5d50369aa2e10acfc9cace504579b2faabb478e76941a"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c7f2c7f2b9ca6bdeef8f0fa897f8e05085923eb091721675170254cbc5b02897"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3c6818a1a86dd6dca7ddcaaf76947d5ba31aecc28cb1b67009a5877c9a64f3f"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d312ef37c91508b0ab2cee7da26ec0b3ed2f03ce12bd87a588d771ae15dcf82d"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:51529d40e3ca50046d7606fa99ce3956a617f9b36380da3b7f0dd3dd28e68cb5"},
    {file = "tomli-2.4.1-cp313-cp313-win32.whl", hash = "sha256:2190f2e9dd7508d2a90ded5ed369255980a1bcdd58e52f7fe24b8162bf9fedbd"},
    {file = "tomli-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:8d65a2fbf9d2f8352685bc1364177ee3923d6baf5e7f43ea4959d7d8bc326a36"},
    {file = "tomli-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:4b605484e43cdc43f0954ddae319fb75f04cc10dd80d830540060ee7cd0243cd"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fd0409a3653af6c147209d267a0e4243f0ae46b011aa978b1080359fddc9b6cf"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:a120733b01c45e9a0c34aeef92bf0cf1d56cfe81ed9d47d562f9ed591a9828ac"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:559db847dc486944896521f68d8190be1c9e719fced785720d2216fe7022b662"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01f520d4f53ef97964a240a035ec2a869fe1a37dde002b57ebc4417a27ccd853"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7f94b27a62cfad8496c8d2513e1a222dd446f095fca8987fceef261225538a15"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ede3e6487c5ef5d28634ba3f31f989030ad6af71edfb0055cbbd14189ff240ba"},
    {file = "tomli-2.4.1-cp314-cp314-win32.whl", hash = "sha256:3d48a93ee1c9b79c04bb38772ee1b64dcf18ff43085896ea460ca8dec96f35f6"},
    {file = "tomli-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:88dceee75c2c63af144e456745e10101eb67361050196b0b6af5d717254dddf7"},
    {file = "tomli-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:b8c198f8c1805dc42708689ed6864951fd2494f924149d3e4bce7710f8eb5232"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:d4d8fe59808a54658fcc0160ecfb1b30f9089906c50b23bcb4c69eddc19ec2b4"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7008df2e7655c495dd12d2a4ad038ff878d4ca4b81fccaf82b714e07eae4402c"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1d8591993e228b0c930c4bb0db464bdad97b3289fb981255d6c9a41aedc84b2d"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:734e20b57ba95624ecf1841e72b53f6e186355e216e5412de414e3c51e5e3c41"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8a650c2dbafa08d42e51ba0b62740dae4ecb9338eefa093aa5c78ceb546fcd5c"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:504aa796fe0569bb43171066009ead363de03675276d2d121ac1a4572397870f"},
    {file = "tomli-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:b1d22e6e9387bf4739fbe23bfa80e93f6b0373a7f1b96c6227c32bef95a4d7a8"},
    {file = "tomli-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:2c1c351919aca02858f740c6d33adea0c5deea37f9ecca1cc1ef9e884a619d26"},
    {file = "tomli-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:eab21f45c7f66c13f2a9e0e1535309cee140182a9cdae1e041d02e47291e8396"},
    {file = "tomli-2.4.1-py3-none-any.whl", hash = "sha256:0d85819802132122da43cb86656f8d1f8c6587d54ae7dcaf30e90533028b49fe"},
    {file = "tomli-2.4.1.tar.gz", hash = "sha256:7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f"},
]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "lint"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[metadata]
lock-version = "2.1"
python-versions = ">=3.10,<4.0"
content-hash = "4259da191802ade59c8b07abe86d8f66dd628c5074cd6597a604cac4576f0cab"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/system/poetry.toml

- repository: `ni/datastore-python`
- source_path: `examples/system/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/pyproject.toml sha256=99b69d2a691230d2e079596dd844907a40513eedcbceb6f3d52a594173434d93 bytes=2281 -->
## FILE: examples/system/pyproject.toml

- repository: `ni/datastore-python`
- source_path: `examples/system/pyproject.toml`
- sha256: `99b69d2a691230d2e079596dd844907a40513eedcbceb6f3d52a594173434d93`
- bytes: 2281

````toml
[project]
name = "system_example"
version = "1.0.0"
license = "MIT"
description = "Example demonstrating how to detect, publish, and query system hardware and software resources"
authors = [{name = "NI", email = "opensource@ni.com"}]
maintainers = [
  {name = "Johann Scholtz", email = "johann.scholtz@emerson.com"},
  {name = "Joel Dixon", email = "joel.dixon@emerson.com"}
]
readme = "README.md"
keywords = ["system", "example"]
classifiers = [
  "Development Status :: 5 - Production/Stable",
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
]
dynamic = ["dependencies"]
requires-python = ">=3.10,<4.0"

[project.urls]
repository = "https://github.com/ni/datastore-python"

[project.scripts]
system = "src.system:main"

[tool.poetry]
requires-poetry = ">=2.1,<3.0"

[[tool.poetry.packages]]
include = "src"

[tool.poetry.dependencies]
ni-datastore = { version=">=2.0.0.dev0", allow-prereleases = true }
nisyscfg = { version = ">=0.2.1" }

[tool.poetry.group.dev.dependencies]
# Uncomment to use local ni-datastore code
# ni-datastore = {path = "../..", develop = true}
datastore-utilities = { path = "../../utilities", develop = true }

[tool.poetry.group.lint.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"

[tool.black]
line-length = 100

[tool.mypy]
mypy_path = "src"
files = "."
namespace_packages = true
strict = true
explicit_package_bases = true
warn_unused_ignores = true

[[tool.mypy.overrides]]
module = [
    "nisyscfg",
    "nisyscfg.component_info",
    "nisyscfg.hardware_resource",
]
ignore_missing_imports = true  # no library stubs or py.typed marker

[build-system]
requires = ["poetry-core>=2.1.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/README.md sha256=7ae6ea0b95e217f361e9f0915c0b8296b4022e3519e8e44332796306b30c2747 bytes=508 -->
## FILE: examples/system/README.md

- repository: `ni/datastore-python`
- source_path: `examples/system/README.md`
- sha256: `7ae6ea0b95e217f361e9f0915c0b8296b4022e3519e8e44332796306b30c2747`
- bytes: 508

````markdown
# System Example

`system` contains sample Python code for detecting system hardware
and software resources and publishing their metadata to the
NI Measurement Data Store.

## Required Software

`system` requires Python 3.10 or greater and the
[NI System Configuration API](https://www.ni.com/en/support/downloads/drivers/download.system-configuration.html).
Alternatively, install at least one NI driver like NI-DAQmx or NI-SCOPE.

## Usage

```python
poetry install
poetry run system
```
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/src/__init__.py sha256=a9cd2fef099e88c9012b0999ffaef55b1baad131df123a224f32cbee5ae163b2 bytes=74 -->
## FILE: examples/system/src/__init__.py

- repository: `ni/datastore-python`
- source_path: `examples/system/src/__init__.py`
- sha256: `a9cd2fef099e88c9012b0999ffaef55b1baad131df123a224f32cbee5ae163b2`
- bytes: 74

````python
"""Detect, publish, and query system hardware and software resources."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=examples/system/src/system.py sha256=5282759d1006a7e5a736ffa5f14db703c105a6cee7ab7dee0b5e01ff31024039 bytes=5653 -->
## FILE: examples/system/src/system.py

- repository: `ni/datastore-python`
- source_path: `examples/system/src/system.py`
- sha256: `5282759d1006a7e5a736ffa5f14db703c105a6cee7ab7dee0b5e01ff31024039`
- bytes: 5653

````python
"""How to detect, publish, and query system hardware and software resources."""

import os
import platform
from dataclasses import dataclass

import nisyscfg
import nisyscfg.component_info
import nisyscfg.hardware_resource
from ni.datastore.data import (
    DataStoreClient,
    TestResult,
)
from ni.datastore.metadata import (
    HardwareItem,
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    TestStation,
)
from utilities import DataStoreContext


@dataclass(frozen=True)
class SystemMetadata:
    """Represents the available resources on a system."""

    operator: Operator
    test_station: TestStation
    hardware_items: list[HardwareItem]
    software_items: list[SoftwareItem]


def main() -> None:
    """Detect, publish, and query hardware and software resources from the local system."""
    # The DataStoreContext sets up and tears down the example environment.
    # It is not used in production code.
    with DataStoreContext():
        print("Scanning system for metadata...")
        system_metadata = detect_system_resources()

        print("Publishing detected system metadata...")
        test_result_id = publish_empty_test_result(system_metadata)

        print("Querying system metadata...")
        test_result = query_test_result(test_result_id)

        print()
        print(f"TestResult ID: {test_result.id}")
        print(f"- Operator: {test_result.operator_id}")
        print(f"- Test Station: {test_result.test_station_id}")
        print(f"- Installed Software: {len(test_result.software_item_ids)} packages")
        print(f"- Available Hardware: {len(test_result.hardware_item_ids)} devices")


def detect_system_resources(system_target: str = "localhost") -> SystemMetadata:
    """Scan the specified system_target and return SystemMetadata describing the system."""
    with nisyscfg.Session(target=system_target) as session:
        ni_device_filter = session.create_filter()
        ni_device_filter.is_ni_product = True
        ni_device_filter.is_device = True
        ni_device_filter.is_present = True

        operator = create_operator()
        test_station = create_test_station(session)
        hardware = [
            create_hardware_item(entry) for entry in session.find_hardware(ni_device_filter)
        ]
        software = [
            create_software_item(entry) for entry in session.get_installed_software_components()
        ]
        system_metadata = SystemMetadata(operator, test_station, hardware, software)
    return system_metadata


def create_hardware_item(
    hardware_entry: nisyscfg.hardware_resource.HardwareResource,
) -> HardwareItem:
    """Create a new HardwareItem instance from the specified nisyscfg entry."""
    manufacturer = hardware_entry.vendor_name
    model = hardware_entry.product_name
    serial_number = hardware_entry.serial_number
    new_instance = HardwareItem(manufacturer=manufacturer, model=model, serial_number=serial_number)
    return new_instance


def create_software_item(software_entry: nisyscfg.component_info.ComponentInfo) -> SoftwareItem:
    """Create a new SoftwareItem instance from the specified nisyscfg entry."""
    new_instance = SoftwareItem(product=software_entry.title, version=software_entry.version)
    return new_instance


def create_test_station(session: nisyscfg.Session) -> TestStation:
    """Create a new TestStation instance from the specified nisyscfg session."""
    new_instance = TestStation(name=session.hostname)
    return new_instance


def create_operator(name: str = "") -> Operator:
    """Create a new Operator instance using the specified name. Otherwise, use the active user."""
    if not name:
        host_os = platform.system()
        if host_os == "Windows":
            username_variable = "USERNAME"
        elif host_os == "Linux":
            username_variable = "USER"
        else:
            raise NotImplementedError(f"{host_os} support not implemented")
        name = os.environ.get(username_variable, "Unknown operator")

    new_instance = Operator(name=name)
    return new_instance


def publish_empty_test_result(system_metadata: SystemMetadata) -> str:
    """Publish a TestResult with the specified system_metadata and return its ID."""
    with MetadataStoreClient() as metadata_store_client:
        operator_id = metadata_store_client.create_operator(system_metadata.operator)
        test_station_id = metadata_store_client.create_test_station(system_metadata.test_station)
        hardware_item_ids = [
            metadata_store_client.create_hardware_item(entry)
            for entry in system_metadata.hardware_items
        ]
        software_item_ids = [
            metadata_store_client.create_software_item(entry)
            for entry in system_metadata.software_items
        ]

    empty_result = TestResult(
        name="system metadata result",
        operator_id=operator_id,
        test_station_id=test_station_id,
        software_item_ids=software_item_ids,
        hardware_item_ids=hardware_item_ids,
    )

    with DataStoreClient() as datastore_client:
        test_result_id = datastore_client.create_test_result(empty_result)

    return test_result_id


def query_test_result(test_result_id: str) -> TestResult:
    """Query the NI DataStore Service for the specified TestResult and return it."""
    with DataStoreClient() as datastore_client:
        test_result = datastore_client.get_test_result(test_result_id)
    return test_result


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=datastore-python path=LICENSE sha256=6e595989aca245ed04f25b4dd8ab762fadf202b928da28a6f424bda1351b6c05 bytes=1080 -->
## FILE: LICENSE

- repository: `ni/datastore-python`
- source_path: `LICENSE`
- sha256: `6e595989aca245ed04f25b4dd8ab762fadf202b928da28a6f424bda1351b6c05`
- bytes: 1080

````text
MIT License

Copyright (c) 2025 NI

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

<!--NI_OSS_SOURCE repo=datastore-python path=poetry.lock sha256=2e1368c71787930cc6c91c29513f0334f3e45b4e6fe2afd2d18ec26fa51f3724 bytes=346682 -->
## FILE: poetry.lock

- repository: `ni/datastore-python`
- source_path: `poetry.lock`
- sha256: `2e1368c71787930cc6c91c29513f0334f3e45b4e6fe2afd2d18ec26fa51f3724`
- bytes: 346682

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "alabaster"
version = "1.0.0"
description = "A light, configurable Sphinx theme"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
files = [
    {file = "alabaster-1.0.0-py3-none-any.whl", hash = "sha256:fc6786402dc3fcb2de3cabd5fe455a2db534b371124f1f21de8731783dec828b"},
    {file = "alabaster-1.0.0.tar.gz", hash = "sha256:c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e"},
]

[[package]]
name = "anyio"
version = "4.13.0"
description = "High-level concurrency and networking framework on top of asyncio or Trio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "anyio-4.13.0-py3-none-any.whl", hash = "sha256:08b310f9e24a9594186fd75b4f73f4a4152069e3853f1ed8bfbf58369f4ad708"},
    {file = "anyio-4.13.0.tar.gz", hash = "sha256:334b70e641fd2221c1505b3890c69882fe4a2df910cba14d97019b90b24439dc"},
]

[package.dependencies]
exceptiongroup = {version = ">=1.0.2", markers = "python_version < \"3.11\""}
idna = ">=2.8"
typing_extensions = {version = ">=4.5", markers = "python_version < \"3.13\""}

[package.extras]
trio = ["trio (>=0.32.0)"]

[[package]]
name = "appnope"
version = "0.1.4"
description = "Disable App Nap on macOS >= 10.9"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
markers = "platform_system == \"Darwin\""
files = [
    {file = "appnope-0.1.4-py2.py3-none-any.whl", hash = "sha256:502575ee11cd7a28c0205f379b525beefebab9d161b7c964670864014ed7213c"},
    {file = "appnope-0.1.4.tar.gz", hash = "sha256:1de3860566df9caf38f01f86f65e0e13e379af54f9e4bee1e66b48f2efffd1ee"},
]

[[package]]
name = "argon2-cffi"
version = "25.1.0"
description = "Argon2 for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "argon2_cffi-25.1.0-py3-none-any.whl", hash = "sha256:fdc8b074db390fccb6eb4a3604ae7231f219aa669a2652e0f20e16ba513d5741"},
    {file = "argon2_cffi-25.1.0.tar.gz", hash = "sha256:694ae5cc8a42f4c4e2bf2ca0e64e51e23a040c6a517a85074683d3959e1346c1"},
]

[package.dependencies]
argon2-cffi-bindings = "*"

[[package]]
name = "argon2-cffi-bindings"
version = "25.1.0"
description = "Low-level CFFI bindings for Argon2"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-macosx_10_13_universal2.whl", hash = "sha256:3d3f05610594151994ca9ccb3c771115bdb4daef161976a266f0dd8aa9996b8f"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:8b8efee945193e667a396cbc7b4fb7d357297d6234d30a489905d96caabde56b"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:3c6702abc36bf3ccba3f802b799505def420a1b7039862014a65db3205967f5a"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a1c70058c6ab1e352304ac7e3b52554daadacd8d453c1752e547c76e9c99ac44"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e2fd3bfbff3c5d74fef31a722f729bf93500910db650c925c2d6ef879a7e51cb"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:c4f9665de60b1b0e99bcd6be4f17d90339698ce954cfd8d9cf4f91c995165a92"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:ba92837e4a9aa6a508c8d2d7883ed5a8f6c308c89a4790e1e447a220deb79a85"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-win32.whl", hash = "sha256:84a461d4d84ae1295871329b346a97f68eade8c53b6ed9a7ca2d7467f3c8ff6f"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b55aec3565b65f56455eebc9b9f34130440404f27fe21c3b375bf1ea4d8fbae6"},
    {file = "argon2_cffi_bindings-25.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:87c33a52407e4c41f3b70a9c2d3f6056d88b10dad7695be708c5021673f55623"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:aecba1723ae35330a008418a91ea6cfcedf6d31e5fbaa056a166462ff066d500"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-macosx_10_9_x86_64.whl", hash = "sha256:2630b6240b495dfab90aebe159ff784d08ea999aa4b0d17efa734055a07d2f44"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:7aef0c91e2c0fbca6fc68e7555aa60ef7008a739cbe045541e438373bc54d2b0"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1e021e87faa76ae0d413b619fe2b65ab9a037f24c60a1e6cc43457ae20de6dc6"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e924cfc503018a714f94a49a149fdc0b644eaead5d1f089330399134fa028a"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:c87b72589133f0346a1cb8d5ecca4b933e3c9b64656c9d175270a000e73b288d"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:1db89609c06afa1a214a69a462ea741cf735b29a57530478c06eb81dd403de99"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-win32.whl", hash = "sha256:473bcb5f82924b1becbb637b63303ec8d10e84c8d241119419897a26116515d2"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-win_amd64.whl", hash = "sha256:a98cd7d17e9f7ce244c0803cad3c23a7d379c301ba618a5fa76a67d116618b98"},
    {file = "argon2_cffi_bindings-25.1.0-cp39-abi3-win_arm64.whl", hash = "sha256:b0fdbcf513833809c882823f98dc2f931cf659d9a1429616ac3adebb49f5db94"},
    {file = "argon2_cffi_bindings-25.1.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:6dca33a9859abf613e22733131fc9194091c1fa7cb3e131c143056b4856aa47e"},
    {file = "argon2_cffi_bindings-25.1.0-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:21378b40e1b8d1655dd5310c84a40fc19a9aa5e6366e835ceb8576bf0fea716d"},
    {file = "argon2_cffi_bindings-25.1.0-pp310-pypy310_pp73-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5d588dec224e2a83edbdc785a5e6f3c6cd736f46bfd4b441bbb5aa1f5085e584"},
    {file = "argon2_cffi_bindings-25.1.0-pp310-pypy310_pp73-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5acb4e41090d53f17ca1110c3427f0a130f944b896fc8c83973219c97f57b690"},
    {file = "argon2_cffi_bindings-25.1.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:da0c79c23a63723aa5d782250fbf51b768abca630285262fb5144ba5ae01e520"},
    {file = "argon2_cffi_bindings-25.1.0.tar.gz", hash = "sha256:b957f3e6ea4d55d820e40ff76f450952807013d361a65d7f28acc0acbf29229d"},
]

[package.dependencies]
cffi = [
    {version = ">=1.0.1", markers = "python_version < \"3.14\""},
    {version = ">=2.0.0b1", markers = "python_version >= \"3.14\""},
]

[[package]]
name = "arrow"
version = "1.4.0"
description = "Better dates & times for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "arrow-1.4.0-py3-none-any.whl", hash = "sha256:749f0769958ebdc79c173ff0b0670d59051a535fa26e8eba02953dc19eb43205"},
    {file = "arrow-1.4.0.tar.gz", hash = "sha256:ed0cc050e98001b8779e84d461b0098c4ac597e88704a655582b21d116e526d7"},
]

[package.dependencies]
python-dateutil = ">=2.7.0"
tzdata = {version = "*", markers = "python_version >= \"3.9\""}

[package.extras]
doc = ["doc8", "sphinx (>=7.0.0)", "sphinx-autobuild", "sphinx-autodoc-typehints", "sphinx_rtd_theme (>=1.3.0)"]
test = ["dateparser (==1.*)", "pre-commit", "pytest", "pytest-cov", "pytest-mock", "pytz (==2025.2)", "simplejson (==3.*)"]

[[package]]
name = "ast-serialize"
version = "0.5.0"
description = "Python bindings for mypy AST serialization"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8f5c14f169eb0972c0c21bada5358b23d6047c76583b005234f865b11f1fa00a"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7d1a2de9de5be04652f0ed60738356ef94f66db37924a9499fffe98dc491aa0b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:be5173fb66f9b49026d9d5a2ff0fc7c7009077107c0eb285b2d60fdf1fe10bd1"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f8015cd071ac1339924ee2b8098c93e00e155f30a16f40ec9816fcf84f4753f6"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5499e8797edff2a9186aa313ed382c6b422e798e9332d9953badcee6e69a88f2"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6848f2a093fb5548751a9a09bff8fcd229e2bbeb0e3331f391b6ae6d26cd9903"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:832d4c998e0b091fd60a6d6bceee535483c4d490de9ba85003af835225719261"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:16db7c62ec0b8efe1d7afd283a388d8f74f2605d56032e5a37747d2de8dba027"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:baf5eb061eb5bccade4128ad42da33787d72f6013809cd1b590376ece8b3c937"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:104e4a35bd7c124173c41760ef9aaea17ddb3f86c65cb643671d59afbe3ee94c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:36be371028fc1675acb38a331bde160dbab7ff907fdf00b67eb6911aa106951b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:061ee58bdb52341c8201a6df41182a977736bae3b7ded87ca7176ca25a8a47ab"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b15219e9cdc9f53f6f4cb51c009203507228226148c05c5e8fe451c28b435eb3"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win32.whl", hash = "sha256:842d1c004bb466c7df036f95fabef789570541922b10976b12f5592a69cf0b38"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b0c06d760909b095cc466356dfccd05a1c7233a6ca191c020dca2c6a6f16c24c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:787baedb0262cc49e8ce37cc15c00ae818e46a165a3b36f5e21ed174998104cb"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:0668aa9459cfa8c9c49ddd2163ebcf43088ba045ef7492af6fe22e0098303101"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:bf683d6363edf2b39eed6b6d4fe22d34b6203867a67e27134d9e2a2680c4bc4a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9cc22cf0c9be65e71cf88fda130af60d61eb4a79370ad4cfe7900d48a4aa2211"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f66173891548c9f2726bf27957b41cabce12fa679dc6da505ddbde4d4b3b31cf"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e42d729ef2be96a14efbad355093284739e3670ece3e534f82cc8832790911d9"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b725026bafa801dbd7310eb13a75f0a2e370e7e51b2cb225f9d21fcfadf919ee"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b54f60c1d78767a53b67eaa663f0dfac3afe606aa07f1301572f588b73d64809"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_31_riscv64.whl", hash = "sha256:27d51654fc240a1e87e742d353d98eb45b75f62f129086b3596ab53df2ac2a43"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c36237c46dd1674542f2109740ea5ea485a169bf1431939ada0434e17934"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:1943db345233cc7194a470f13afa9c59772c0b123dea0c9414c4d4ca54369759"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:df1c00022cbbcb064bfaa505aa9c9295362443ce5dacb459d1331d3da353f887"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:cae65289fc456fde04af979a2be09302ef5d8ab92ef23e596d6746dc267ada27"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:239a4c354e8d676e9d94631d1d4a64edc6b266f86ff3a5a80aedd344f342c01d"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win32.whl", hash = "sha256:143a4ef63285a075871908fda3672dc21864b83a8ec3ee12304aa3e4c5387b9a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_amd64.whl", hash = "sha256:cf25572c526add400f26a4750dc6ce0c3bb93fc1f75e7ae0cad4ce4f2cd5c590"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_arm64.whl", hash = "sha256:92a31c9c20d25a076edaeec76b128a3535d74a24f340b9a8a7e96c9b86dc9642"},
    {file = "ast_serialize-0.5.0.tar.gz", hash = "sha256:5880091bfe6f4f986f22866375c2e884843e7a0b6343ae41aeea659613d879b6"},
]

[[package]]
name = "astroid"
version = "4.1.2"
description = "An abstract syntax tree for Python with inference support."
optional = false
python-versions = ">=3.10.0"
groups = ["docs"]
files = [
    {file = "astroid-4.1.2-py3-none-any.whl", hash = "sha256:21312e682c0866dc5a309ee57e4b88ea92751b9955a58b1c31371cbbeb088707"},
    {file = "astroid-4.1.2.tar.gz", hash = "sha256:d6c4a52bfcda4bbeb7359dead642b0248b90f7d9a07e690230bd86fefd6d37f1"},
]

[package.dependencies]
typing-extensions = {version = ">=4", markers = "python_version < \"3.11\""}

[[package]]
name = "asttokens"
version = "3.0.1"
description = "Annotate AST trees with source code positions"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "asttokens-3.0.1-py3-none-any.whl", hash = "sha256:15a3ebc0f43c2d0a50eeafea25e19046c68398e487b9f1f5b517f7c0f40f976a"},
    {file = "asttokens-3.0.1.tar.gz", hash = "sha256:71a4ee5de0bde6a31d64f6b13f2293ac190344478f081c3d1bccfcf5eacb0cb7"},
]

[package.extras]
astroid = ["astroid (>=2,<5)"]
test = ["astroid (>=2,<5)", "pytest (<9.0)", "pytest-cov", "pytest-xdist"]

[[package]]
name = "async-lru"
version = "2.3.0"
description = "Simple LRU cache for asyncio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "async_lru-2.3.0-py3-none-any.whl", hash = "sha256:eea27b01841909316f2cc739807acea1c623df2be8c5cfad7583286397bb8315"},
    {file = "async_lru-2.3.0.tar.gz", hash = "sha256:89bdb258a0140d7313cf8f4031d816a042202faa61d0ab310a0a538baa1c24b6"},
]

[package.dependencies]
typing_extensions = {version = ">=4.0.0", markers = "python_version < \"3.11\""}

[[package]]
name = "attrs"
version = "26.1.0"
description = "Classes Without Boilerplate"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "attrs-26.1.0-py3-none-any.whl", hash = "sha256:c647aa4a12dfbad9333ca4e71fe62ddc36f4e63b2d260a37a8b83d2f043ac309"},
    {file = "attrs-26.1.0.tar.gz", hash = "sha256:d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32"},
]

[[package]]
name = "babel"
version = "2.18.0"
description = "Internationalization utilities"
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs"]
files = [
    {file = "babel-2.18.0-py3-none-any.whl", hash = "sha256:e2b422b277c2b9a9630c1d7903c2a00d0830c409c59ac8cae9081c92f1aeba35"},
    {file = "babel-2.18.0.tar.gz", hash = "sha256:b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d"},
]

[package.extras]
dev = ["backports.zoneinfo ; python_version < \"3.9\"", "freezegun (>=1.0,<2.0)", "jinja2 (>=3.0)", "pytest (>=6.0)", "pytest-cov", "pytz", "setuptools", "tzdata ; sys_platform == \"win32\""]

[[package]]
name = "bandit"
version = "1.9.4"
description = "Security oriented static analyser for python code."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "bandit-1.9.4-py3-none-any.whl", hash = "sha256:f89ffa663767f5a0585ea075f01020207e966a9c0f2b9ef56a57c7963a3f6f8e"},
    {file = "bandit-1.9.4.tar.gz", hash = "sha256:b589e5de2afe70bd4d53fa0c1da6199f4085af666fde00e8a034f152a52cd628"},
]

[package.dependencies]
colorama = {version = ">=0.3.9", markers = "platform_system == \"Windows\""}
PyYAML = ">=5.3.1"
rich = "*"
stevedore = ">=1.20.0"
tomli = {version = ">=1.1.0", optional = true, markers = "python_version < \"3.11\" and extra == \"toml\""}

[package.extras]
baseline = ["GitPython (>=3.1.30)"]
sarif = ["jschema-to-python (>=1.2.3)", "sarif-om (>=1.0.4)"]
test = ["beautifulsoup4 (>=4.8.0)", "coverage (>=4.5.4)", "fixtures (>=3.0.0)", "flake8 (>=4.0.0)", "pylint (==1.9.4)", "stestr (>=2.5.0)", "testscenarios (>=0.5.0)", "testtools (>=2.3.0)"]
toml = ["tomli (>=1.1.0) ; python_version < \"3.11\""]
yaml = ["PyYAML"]

[[package]]
name = "beautifulsoup4"
version = "4.15.0"
description = "Screen-scraping library"
optional = false
python-versions = ">=3.7.0"
groups = ["dev"]
files = [
    {file = "beautifulsoup4-4.15.0-py3-none-any.whl", hash = "sha256:d6f88de62e1d4e38ecb1077eb9724cd0eff29d2a08ca16a401e9b9e93f117cf9"},
    {file = "beautifulsoup4-4.15.0.tar.gz", hash = "sha256:288e3ca7d54b06f2ac191970bc275c1939cb46d450b255bf6718b04aa37ab4f7"},
]

[package.dependencies]
soupsieve = ">=1.6.1"
typing-extensions = ">=4.0.0"

[package.extras]
cchardet = ["cchardet"]
chardet = ["chardet"]
charset-normalizer = ["charset-normalizer"]
html5lib = ["html5lib"]
lxml = ["lxml"]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["lint"]
files = [
    {file = "better_diff-0.1.4-py3-none-any.whl", hash = "sha256:06e63358b2047ae2695abd96316f47c6d3c38b9e641f53012279878d66d8792e"},
    {file = "better_diff-0.1.4.tar.gz", hash = "sha256:920ca76bdbcd2f0c361fa5d9a2d4727624a3545d6cb467b1b6616cad8a634de7"},
]

[[package]]
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "black-25.12.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f85ba1ad15d446756b4ab5f3044731bf68b777f8f9ac9cdabd2425b97cd9c4e8"},
    {file = "black-25.12.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:546eecfe9a3a6b46f9d69d8a642585a6eaf348bcbbc4d87a19635570e02d9f4a"},
    {file = "black-25.12.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:17dcc893da8d73d8f74a596f64b7c98ef5239c2cd2b053c0f25912c4494bf9ea"},
    {file = "black-25.12.0-cp310-cp310-win_amd64.whl", hash = "sha256:09524b0e6af8ba7a3ffabdfc7a9922fb9adef60fed008c7cd2fc01f3048e6e6f"},
    {file = "black-25.12.0-cp310-cp310-win_arm64.whl", hash = "sha256:b162653ed89eb942758efeb29d5e333ca5bb90e5130216f8369857db5955a7da"},
    {file = "black-25.12.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d0cfa263e85caea2cff57d8f917f9f51adae8e20b610e2b23de35b5b11ce691a"},
    {file = "black-25.12.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a2f578ae20c19c50a382286ba78bfbeafdf788579b053d8e4980afb079ab9be"},
    {file = "black-25.12.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e1b65634b0e471d07ff86ec338819e2ef860689859ef4501ab7ac290431f9b"},
    {file = "black-25.12.0-cp311-cp311-win_amd64.whl", hash = "sha256:a3fa71e3b8dd9f7c6ac4d818345237dfb4175ed3bf37cd5a581dbc4c034f1ec5"},
    {file = "black-25.12.0-cp311-cp311-win_arm64.whl", hash = "sha256:51e267458f7e650afed8445dc7edb3187143003d52a1b710c7321aef22aa9655"},
    {file = "black-25.12.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:31f96b7c98c1ddaeb07dc0f56c652e25bdedaac76d5b68a059d998b57c55594a"},
    {file = "black-25.12.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:05dd459a19e218078a1f98178c13f861fe6a9a5f88fc969ca4d9b49eb1809783"},
    {file = "black-25.12.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1f68c5eff61f226934be6b5b80296cf6939e5d2f0c2f7d543ea08b204bfaf59"},
    {file = "black-25.12.0-cp312-cp312-win_amd64.whl", hash = "sha256:274f940c147ddab4442d316b27f9e332ca586d39c85ecf59ebdea82cc9ee8892"},
    {file = "black-25.12.0-cp312-cp312-win_arm64.whl", hash = "sha256:169506ba91ef21e2e0591563deda7f00030cb466e747c4b09cb0a9dae5db2f43"},
    {file = "black-25.12.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a05ddeb656534c3e27a05a29196c962877c83fa5503db89e68857d1161ad08a5"},
    {file = "black-25.12.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9ec77439ef3e34896995503865a85732c94396edcc739f302c5673a2315e1e7f"},
    {file = "black-25.12.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e509c858adf63aa61d908061b52e580c40eae0dfa72415fa47ac01b12e29baf"},
    {file = "black-25.12.0-cp313-cp313-win_amd64.whl", hash = "sha256:252678f07f5bac4ff0d0e9b261fbb029fa530cfa206d0a636a34ab445ef8ca9d"},
    {file = "black-25.12.0-cp313-cp313-win_arm64.whl", hash = "sha256:bc5b1c09fe3c931ddd20ee548511c64ebf964ada7e6f0763d443947fd1c603ce"},
    {file = "black-25.12.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:0a0953b134f9335c2434864a643c842c44fba562155c738a2a37a4d61f00cad5"},
    {file = "black-25.12.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2355bbb6c3b76062870942d8cc450d4f8ac71f9c93c40122762c8784df49543f"},
    {file = "black-25.12.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9678bd991cc793e81d19aeeae57966ee02909877cb65838ccffef24c3ebac08f"},
    {file = "black-25.12.0-cp314-cp314-win_amd64.whl", hash = "sha256:97596189949a8aad13ad12fcbb4ae89330039b96ad6742e6f6b45e75ad5cfd83"},
    {file = "black-25.12.0-cp314-cp314-win_arm64.whl", hash = "sha256:778285d9ea197f34704e3791ea9404cd6d07595745907dd2ce3da7a13627b29b"},
    {file = "black-25.12.0-py3-none-any.whl", hash = "sha256:48ceb36c16dbc84062740049eef990bb2ce07598272e673c17d1a7720c71c828"},
    {file = "black-25.12.0.tar.gz", hash = "sha256:8d3dd9cea14bff7ddc0eb243c811cdb1a011ebb4800a5f0335a01a68654796a7"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "bleach"
version = "6.4.0"
description = "An easy safelist-based HTML-sanitizing tool."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "bleach-6.4.0-py3-none-any.whl", hash = "sha256:4b6b6a54fff2e69a3dde9d21cc6301220bee3c3cb792187d11403fd795031081"},
    {file = "bleach-6.4.0.tar.gz", hash = "sha256:4202482733d85cedd04e59fcb2f89f4e4c7c385a78d3c3c23c30446843a37452"},
]

[package.dependencies]
tinycss2 = {version = ">=1.1.0", optional = true, markers = "extra == \"css\""}
webencodings = "*"

[package.extras]
css = ["tinycss2 (>=1.1.0)"]

[[package]]
name = "certifi"
version = "2026.5.20"
description = "Python package for providing Mozilla's CA Bundle."
optional = false
python-versions = ">=3.7"
groups = ["dev", "docs"]
files = [
    {file = "certifi-2026.5.20-py3-none-any.whl", hash = "sha256:3c52e209ba0a4ad7aebe60436a4ab349c39e1e602e8c134221e546902ad25897"},
    {file = "certifi-2026.5.20.tar.gz", hash = "sha256:69dea482ab64caa7b9f6aba1c6bf48bb6a5448d1c0f1b17ab42ad8c763a5344d"},
]

[[package]]
name = "cffi"
version = "2.0.0"
description = "Foreign Function Interface for Python calling C code."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "cffi-2.0.0-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:0cf2d91ecc3fcc0625c2c530fe004f82c110405f101548512cce44322fa8ac44"},
    {file = "cffi-2.0.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f73b96c41e3b2adedc34a7356e64c8eb96e03a3782b535e043a986276ce12a49"},
    {file = "cffi-2.0.0-cp310-cp310-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:53f77cbe57044e88bbd5ed26ac1d0514d2acf0591dd6bb02a3ae37f76811b80c"},
    {file = "cffi-2.0.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:3e837e369566884707ddaf85fc1744b47575005c0a229de3327f8f9a20f4efeb"},
    {file = "cffi-2.0.0-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:5eda85d6d1879e692d546a078b44251cdd08dd1cfb98dfb77b670c97cee49ea0"},
    {file = "cffi-2.0.0-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9332088d75dc3241c702d852d4671613136d90fa6881da7d770a483fd05248b4"},
    {file = "cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:fc7de24befaeae77ba923797c7c87834c73648a05a4bde34b3b7e5588973a453"},
    {file = "cffi-2.0.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:cf364028c016c03078a23b503f02058f1814320a56ad535686f90565636a9495"},
    {file = "cffi-2.0.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e11e82b744887154b182fd3e7e8512418446501191994dbf9c9fc1f32cc8efd5"},
    {file = "cffi-2.0.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8ea985900c5c95ce9db1745f7933eeef5d314f0565b27625d9a10ec9881e1bfb"},
    {file = "cffi-2.0.0-cp310-cp310-win32.whl", hash = "sha256:1f72fb8906754ac8a2cc3f9f5aaa298070652a0ffae577e0ea9bd480dc3c931a"},
    {file = "cffi-2.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:b18a3ed7d5b3bd8d9ef7a8cb226502c6bf8308df1525e1cc676c3680e7176739"},
    {file = "cffi-2.0.0-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:b4c854ef3adc177950a8dfc81a86f5115d2abd545751a304c5bcf2c2c7283cfe"},
    {file = "cffi-2.0.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:2de9a304e27f7596cd03d16f1b7c72219bd944e99cc52b84d0145aefb07cbd3c"},
    {file = "cffi-2.0.0-cp311-cp311-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:baf5215e0ab74c16e2dd324e8ec067ef59e41125d3eade2b863d294fd5035c92"},
    {file = "cffi-2.0.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:730cacb21e1bdff3ce90babf007d0a0917cc3e6492f336c2f0134101e0944f93"},
    {file = "cffi-2.0.0-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:6824f87845e3396029f3820c206e459ccc91760e8fa24422f8b0c3d1731cbec5"},
    {file = "cffi-2.0.0-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9de40a7b0323d889cf8d23d1ef214f565ab154443c42737dfe52ff82cf857664"},
    {file = "cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8941aaadaf67246224cee8c3803777eed332a19d909b47e29c9842ef1e79ac26"},
    {file = "cffi-2.0.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:a05d0c237b3349096d3981b727493e22147f934b20f6f125a3eba8f994bec4a9"},
    {file = "cffi-2.0.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:94698a9c5f91f9d138526b48fe26a199609544591f859c870d477351dc7b2414"},
    {file = "cffi-2.0.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:5fed36fccc0612a53f1d4d9a816b50a36702c28a2aa880cb8a122b3466638743"},
    {file = "cffi-2.0.0-cp311-cp311-win32.whl", hash = "sha256:c649e3a33450ec82378822b3dad03cc228b8f5963c0c12fc3b1e0ab940f768a5"},
    {file = "cffi-2.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:66f011380d0e49ed280c789fbd08ff0d40968ee7b665575489afa95c98196ab5"},
    {file = "cffi-2.0.0-cp311-cp311-win_arm64.whl", hash = "sha256:c6638687455baf640e37344fe26d37c404db8b80d037c3d29f58fe8d1c3b194d"},
    {file = "cffi-2.0.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6d02d6655b0e54f54c4ef0b94eb6be0607b70853c45ce98bd278dc7de718be5d"},
    {file = "cffi-2.0.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8eca2a813c1cb7ad4fb74d368c2ffbbb4789d377ee5bb8df98373c2cc0dee76c"},
    {file = "cffi-2.0.0-cp312-cp312-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:21d1152871b019407d8ac3985f6775c079416c282e431a4da6afe7aefd2bccbe"},
    {file = "cffi-2.0.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:b21e08af67b8a103c71a250401c78d5e0893beff75e28c53c98f4de42f774062"},
    {file = "cffi-2.0.0-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:1e3a615586f05fc4065a8b22b8152f0c1b00cdbc60596d187c2a74f9e3036e4e"},
    {file = "cffi-2.0.0-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:81afed14892743bbe14dacb9e36d9e0e504cd204e0b165062c488942b9718037"},
    {file = "cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:3e17ed538242334bf70832644a32a7aae3d83b57567f9fd60a26257e992b79ba"},
    {file = "cffi-2.0.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3925dd22fa2b7699ed2617149842d2e6adde22b262fcbfada50e3d195e4b3a94"},
    {file = "cffi-2.0.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:2c8f814d84194c9ea681642fd164267891702542f028a15fc97d4674b6206187"},
    {file = "cffi-2.0.0-cp312-cp312-win32.whl", hash = "sha256:da902562c3e9c550df360bfa53c035b2f241fed6d9aef119048073680ace4a18"},
    {file = "cffi-2.0.0-cp312-cp312-win_amd64.whl", hash = "sha256:da68248800ad6320861f129cd9c1bf96ca849a2771a59e0344e88681905916f5"},
    {file = "cffi-2.0.0-cp312-cp312-win_arm64.whl", hash = "sha256:4671d9dd5ec934cb9a73e7ee9676f9362aba54f7f34910956b84d727b0d73fb6"},
    {file = "cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb"},
    {file = "cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca"},
    {file = "cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b"},
    {file = "cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b"},
    {file = "cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2"},
    {file = "cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3"},
    {file = "cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26"},
    {file = "cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c"},
    {file = "cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b"},
    {file = "cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27"},
    {file = "cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75"},
    {file = "cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91"},
    {file = "cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5"},
    {file = "cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13"},
    {file = "cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b"},
    {file = "cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c"},
    {file = "cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef"},
    {file = "cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775"},
    {file = "cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205"},
    {file = "cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1"},
    {file = "cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f"},
    {file = "cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25"},
    {file = "cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad"},
    {file = "cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9"},
    {file = "cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d"},
    {file = "cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c"},
    {file = "cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8"},
    {file = "cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc"},
    {file = "cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592"},
    {file = "cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512"},
    {file = "cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4"},
    {file = "cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e"},
    {file = "cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6"},
    {file = "cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9"},
    {file = "cffi-2.0.0-cp39-cp39-macosx_10_13_x86_64.whl", hash = "sha256:fe562eb1a64e67dd297ccc4f5addea2501664954f2692b69a76449ec7913ecbf"},
    {file = "cffi-2.0.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:de8dad4425a6ca6e4e5e297b27b5c824ecc7581910bf9aee86cb6835e6812aa7"},
    {file = "cffi-2.0.0-cp39-cp39-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:4647afc2f90d1ddd33441e5b0e85b16b12ddec4fca55f0d9671fef036ecca27c"},
    {file = "cffi-2.0.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:3f4d46d8b35698056ec29bca21546e1551a205058ae1a181d871e278b0b28165"},
    {file = "cffi-2.0.0-cp39-cp39-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:e6e73b9e02893c764e7e8d5bb5ce277f1a009cd5243f8228f75f842bf937c534"},
    {file = "cffi-2.0.0-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:cb527a79772e5ef98fb1d700678fe031e353e765d1ca2d409c92263c6d43e09f"},
    {file = "cffi-2.0.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:61d028e90346df14fedc3d1e5441df818d095f3b87d286825dfcbd6459b7ef63"},
    {file = "cffi-2.0.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:0f6084a0ea23d05d20c3edcda20c3d006f9b6f3fefeac38f59262e10cef47ee2"},
    {file = "cffi-2.0.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:1cd13c99ce269b3ed80b417dcd591415d3372bcac067009b6e0f59c7d4015e65"},
    {file = "cffi-2.0.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:89472c9762729b5ae1ad974b777416bfda4ac5642423fa93bd57a09204712322"},
    {file = "cffi-2.0.0-cp39-cp39-win32.whl", hash = "sha256:2081580ebb843f759b9f617314a24ed5738c51d2aee65d31e02f6f7a2b97707a"},
    {file = "cffi-2.0.0-cp39-cp39-win_amd64.whl", hash = "sha256:b882b3df248017dba09d6b16defe9b5c407fe32fc7c65a9c69798e6175601be9"},
    {file = "cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529"},
]

[package.dependencies]
pycparser = {version = "*", markers = "implementation_name != \"PyPy\""}

[[package]]
name = "charset-normalizer"
version = "3.4.7"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
optional = false
python-versions = ">=3.7"
groups = ["dev", "docs"]
files = [
    {file = "charset_normalizer-3.4.7-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:cdd68a1fb318e290a2077696b7eb7a21a49163c455979c639bf5a5dcdc46617d"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e17b8d5d6a8c47c85e68ca8379def1303fd360c3e22093a807cd34a71cd082b8"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:511ef87c8aec0783e08ac18565a16d435372bc1ac25a91e6ac7f5ef2b0bff790"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:007d05ec7321d12a40227aae9e2bc6dca73f3cb21058999a1df9e193555a9dcc"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:cf29836da5119f3c8a8a70667b0ef5fdca3bb12f80fd06487cfa575b3909b393"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux_2_31_armv7l.whl", hash = "sha256:12d8baf840cc7889b37c7c770f478adea7adce3dcb3944d02ec87508e2dcf153"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:d560742f3c0d62afaccf9f41fe485ed69bd7661a241f86a3ef0f0fb8b1a397af"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:b14b2d9dac08e28bb8046a1a0434b1750eb221c8f5b87a68f4fa11a6f97b5e34"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:bc17a677b21b3502a21f66a8cc64f5bfad4df8a0b8434d661666f8ce90ac3af1"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:750e02e074872a3fad7f233b47734166440af3cdea0add3e95163110816d6752"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:4e5163c14bffd570ef2affbfdd77bba66383890797df43dc8b4cc7d6f500bf53"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:6ed74185b2db44f41ef35fd1617c5888e59792da9bbc9190d6c7300617182616"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:94e1885b270625a9a828c9793b4d52a64445299baa1fea5a173bf1d3dd9a1a5a"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-win32.whl", hash = "sha256:6785f414ae0f3c733c437e0f3929197934f526d19dfaa75e18fdb4f94c6fb374"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-win_amd64.whl", hash = "sha256:6696b7688f54f5af4462118f0bfa7c1621eeb87154f77fa04b9295ce7a8f2943"},
    {file = "charset_normalizer-3.4.7-cp310-cp310-win_arm64.whl", hash = "sha256:66671f93accb62ed07da56613636f3641f1a12c13046ce91ffc923721f23c008"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:7641bb8895e77f921102f72833904dcd9901df5d6d72a2ab8f31d04b7e51e4e7"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:202389074300232baeb53ae2569a60901f7efadd4245cf3a3bf0617d60b439d7"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:30b8d1d8c52a48c2c5690e152c169b673487a2a58de1ec7393196753063fcd5e"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:532bc9bf33a68613fd7d65e4b1c71a6a38d7d42604ecf239c77392e9b4e8998c"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2fe249cb4651fd12605b7288b24751d8bfd46d35f12a20b1ba33dea122e690df"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux_2_31_armv7l.whl", hash = "sha256:65bcd23054beab4d166035cabbc868a09c1a49d1efe458fe8e4361215df40265"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:08e721811161356f97b4059a9ba7bafb23ea5ee2255402c42881c214e173c6b4"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:e060d01aec0a910bdccb8be71faf34e7799ce36950f8294c8bf612cba65a2c9e"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:38c0109396c4cfc574d502df99742a45c72c08eff0a36158b6f04000043dbf38"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:1c2a768fdd44ee4a9339a9b0b130049139b8ce3c01d2ce09f67f5a68048d477c"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:1a87ca9d5df6fe460483d9a5bbf2b18f620cbed41b432e2bddb686228282d10b"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:d635aab80466bc95771bb78d5370e74d36d1fe31467b6b29b8b57b2a3cd7d22c"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ae196f021b5e7c78e918242d217db021ed2a6ace2bc6ae94c0fc596221c7f58d"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-win32.whl", hash = "sha256:adb2597b428735679446b46c8badf467b4ca5f5056aae4d51a19f9570301b1ad"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-win_amd64.whl", hash = "sha256:8e385e4267ab76874ae30db04c627faaaf0b509e1ccc11a95b3fc3e83f855c00"},
    {file = "charset_normalizer-3.4.7-cp311-cp311-win_arm64.whl", hash = "sha256:d4a48e5b3c2a489fae013b7589308a40146ee081f6f509e047e0e096084ceca1"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:eca9705049ad3c7345d574e3510665cb2cf844c2f2dcfe675332677f081cbd46"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6178f72c5508bfc5fd446a5905e698c6212932f25bcdd4b47a757a50605a90e2"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:e1421b502d83040e6d7fb2fb18dff63957f720da3d77b2fbd3187ceb63755d7b"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:edac0f1ab77644605be2cbba52e6b7f630731fc42b34cb0f634be1a6eface56a"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5649fd1c7bade02f320a462fdefd0b4bd3ce036065836d4f42e0de958038e116"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux_2_31_armv7l.whl", hash = "sha256:203104ed3e428044fd943bc4bf45fa73c0730391f9621e37fe39ecf477b128cb"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:298930cec56029e05497a76988377cbd7457ba864beeea92ad7e844fe74cd1f1"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:708838739abf24b2ceb208d0e22403dd018faeef86ddac04319a62ae884c4f15"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:0f7eb884681e3938906ed0434f20c63046eacd0111c4ba96f27b76084cd679f5"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:4dc1e73c36828f982bfe79fadf5919923f8a6f4df2860804db9a98c48824ce8d"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:aed52fea0513bac0ccde438c188c8a471c4e0f457c2dd20cdbf6ea7a450046c7"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:fea24543955a6a729c45a73fe90e08c743f0b3334bbf3201e6c4bc1b0c7fa464"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:bb6d88045545b26da47aa879dd4a89a71d1dce0f0e549b1abcb31dfe4a8eac49"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-win32.whl", hash = "sha256:2257141f39fe65a3fdf38aeccae4b953e5f3b3324f4ff0daf9f15b8518666a2c"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-win_amd64.whl", hash = "sha256:5ed6ab538499c8644b8a3e18debabcd7ce684f3fa91cf867521a7a0279cab2d6"},
    {file = "charset_normalizer-3.4.7-cp312-cp312-win_arm64.whl", hash = "sha256:56be790f86bfb2c98fb742ce566dfb4816e5a83384616ab59c49e0604d49c51d"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:f496c9c3cc02230093d8330875c4c3cdfc3b73612a5fd921c65d39cbcef08063"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0ea948db76d31190bf08bd371623927ee1339d5f2a0b4b1b4a4439a65298703c"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a277ab8928b9f299723bc1a2dabb1265911b1a76341f90a510368ca44ad9ab66"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:3bec022aec2c514d9cf199522a802bd007cd588ab17ab2525f20f9c34d067c18"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e044c39e41b92c845bc815e5ae4230804e8e7bc29e399b0437d64222d92809dd"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux_2_31_armv7l.whl", hash = "sha256:f495a1652cf3fbab2eb0639776dad966c2fb874d79d87ca07f9d5f059b8bd215"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e712b419df8ba5e42b226c510472b37bd57b38e897d3eca5e8cfd410a29fa859"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:7804338df6fcc08105c7745f1502ba68d900f45fd770d5bdd5288ddccb8a42d8"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:481551899c856c704d58119b5025793fa6730adda3571971af568f66d2424bb5"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f59099f9b66f0d7145115e6f80dd8b1d847176df89b234a5a6b3f00437aa0832"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:f59ad4c0e8f6bba240a9bb85504faa1ab438237199d4cce5f622761507b8f6a6"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:3dedcc22d73ec993f42055eff4fcfed9318d1eeb9a6606c55892a26964964e48"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:64f02c6841d7d83f832cd97ccf8eb8a906d06eb95d5276069175c696b024b60a"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-win32.whl", hash = "sha256:4042d5c8f957e15221d423ba781e85d553722fc4113f523f2feb7b188cc34c5e"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-win_amd64.whl", hash = "sha256:3946fa46a0cf3e4c8cb1cc52f56bb536310d34f25f01ca9b6c16afa767dab110"},
    {file = "charset_normalizer-3.4.7-cp313-cp313-win_arm64.whl", hash = "sha256:80d04837f55fc81da168b98de4f4b797ef007fc8a79ab71c6ec9bc4dd662b15b"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:c36c333c39be2dbca264d7803333c896ab8fa7d4d6f0ab7edb7dfd7aea6e98c0"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1c2aed2e5e41f24ea8ef1590b8e848a79b56f3a5564a65ceec43c9d692dc7d8a"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:54523e136b8948060c0fa0bc7b1b50c32c186f2fceee897a495406bb6e311d2b"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:715479b9a2802ecac752a3b0efa2b0b60285cf962ee38414211abdfccc233b41"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bd6c2a1c7573c64738d716488d2cdd3c00e340e4835707d8fdb8dc1a66ef164e"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux_2_31_armv7l.whl", hash = "sha256:c45e9440fb78f8ddabcf714b68f936737a121355bf59f3907f4e17721b9d1aae"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:3534e7dcbdcf757da6b85a0bbf5b6868786d5982dd959b065e65481644817a18"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e8ac484bf18ce6975760921bb6148041faa8fef0547200386ea0b52b5d27bf7b"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:a5fe03b42827c13cdccd08e6c0247b6a6d4b5e3cdc53fd1749f5896adcdc2356"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:2d6eb928e13016cea4f1f21d1e10c1cebd5a421bc57ddf5b1142ae3f86824fab"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:e74327fb75de8986940def6e8dee4f127cc9752bee7355bb323cc5b2659b6d46"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:d6038d37043bced98a66e68d3aa2b6a35505dc01328cd65217cefe82f25def44"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:7579e913a5339fb8fa133f6bbcfd8e6749696206cf05acdbdca71a1b436d8e72"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-win32.whl", hash = "sha256:5b77459df20e08151cd6f8b9ef8ef1f961ef73d85c21a555c7eed5b79410ec10"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-win_amd64.whl", hash = "sha256:92a0a01ead5e668468e952e4238cccd7c537364eb7d851ab144ab6627dbbe12f"},
    {file = "charset_normalizer-3.4.7-cp314-cp314-win_arm64.whl", hash = "sha256:67f6279d125ca0046a7fd386d01b311c6363844deac3e5b069b514ba3e63c246"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:effc3f449787117233702311a1b7d8f59cba9ced946ba727bdc329ec69028e24"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:fbccdc05410c9ee21bbf16a35f4c1d16123dcdeb8a1d38f33654fa21d0234f79"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:733784b6d6def852c814bce5f318d25da2ee65dd4839a0718641c696e09a2960"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a89c23ef8d2c6b27fd200a42aa4ac72786e7c60d40efdc76e6011260b6e949c4"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6c114670c45346afedc0d947faf3c7f701051d2518b943679c8ff88befe14f8e"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux_2_31_armv7l.whl", hash = "sha256:a180c5e59792af262bf263b21a3c49353f25945d8d9f70628e73de370d55e1e1"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:3c9a494bc5ec77d43cea229c4f6db1e4d8fe7e1bbffa8b6f0f0032430ff8ab44"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8d828b6667a32a728a1ad1d93957cdf37489c57b97ae6c4de2860fa749b8fc1e"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:cf1493cd8607bec4d8a7b9b004e699fcf8f9103a9284cc94962cb73d20f9d4a3"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:0c96c3b819b5c3e9e165495db84d41914d6894d55181d2d108cc1a69bfc9cce0"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:752a45dc4a6934060b3b0dab47e04edc3326575f82be64bc4fc293914566503e"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:8778f0c7a52e56f75d12dae53ae320fae900a8b9b4164b981b9c5ce059cd1fcb"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:ce3412fbe1e31eb81ea42f4169ed94861c56e643189e1e75f0041f3fe7020abe"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-win32.whl", hash = "sha256:c03a41a8784091e67a39648f70c5f97b5b6a37f216896d44d2cdcb82615339a0"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-win_amd64.whl", hash = "sha256:03853ed82eeebbce3c2abfdbc98c96dc205f32a79627688ac9a27370ea61a49c"},
    {file = "charset_normalizer-3.4.7-cp314-cp314t-win_arm64.whl", hash = "sha256:c35abb8bfff0185efac5878da64c45dafd2b37fb0383add1be155a763c1f083d"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:e5f4d355f0a2b1a31bc3edec6795b46324349c9cb25eed068049e4f472fb4259"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:16d971e29578a5e97d7117866d15889a4a07befe0e87e703ed63cd90cb348c01"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:dca4bbc466a95ba9c0234ef56d7dd9509f63da22274589ebd4ed7f1f4d4c54e3"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:e80c8378d8f3d83cd3164da1ad2df9e37a666cdde7b1cb2298ed0b558064be30"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:36836d6ff945a00b88ba1e4572d721e60b5b8c98c155d465f56ad19d68f23734"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux_2_31_armv7l.whl", hash = "sha256:bd9b23791fe793e4968dba0c447e12f78e425c59fc0e3b97f6450f4781f3ee60"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:aef65cd602a6d0e0ff6f9930fcb1c8fec60dd2cfcb6facaf4bdb0e5873042db0"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:82b271f5137d07749f7bf32f70b17ab6eaabedd297e75dce75081a24f76eb545"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_armv7l.whl", hash = "sha256:1efde3cae86c8c273f1eb3b287be7d8499420cf2fe7585c41d370d3e790054a5"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_ppc64le.whl", hash = "sha256:c593052c465475e64bbfe5dbd81680f64a67fdc752c56d7a0ae205dc8aeefe0f"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_riscv64.whl", hash = "sha256:af21eb4409a119e365397b2adbaca4c9ccab56543a65d5dbd9f920d6ac29f686"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_s390x.whl", hash = "sha256:84c018e49c3bf790f9c2771c45e9313a08c2c2a6342b162cd650258b57817706"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:dd915403e231e6b1809fe9b6d9fc55cf8fb5e02765ac625d9cd623342a7905d7"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-win32.whl", hash = "sha256:320ade88cfb846b8cd6b4ddf5ee9e80ee0c1f52401f2456b84ae1ae6a1a5f207"},
    {file = "charset_normalizer-3.4.7-cp38-cp38-win_amd64.whl", hash = "sha256:1dc8b0ea451d6e69735094606991f32867807881400f808a106ee1d963c46a83"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:177a0ba5f0211d488e295aaf82707237e331c24788d8d76c96c5a41594723217"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6e0d51f618228538a3e8f46bd246f87a6cd030565e015803691603f55e12afb5"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:14265bfe1f09498b9d8ec91e9ec9fa52775edf90fcbde092b25f4a33d444fea9"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:87fad7d9ba98c86bcb41b2dc8dbb326619be2562af1f8ff50776a39e55721c5a"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f22dec1690b584cea26fade98b2435c132c1b5f68e39f5a0b7627cd7ae31f1dc"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux_2_31_armv7l.whl", hash = "sha256:d61f00a0869d77422d9b2aba989e2d24afa6ffd552af442e0e58de4f35ea6d00"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:6370e8686f662e6a3941ee48ed4742317cafbe5707e36406e9df792cdb535776"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:a6c5863edfbe888d9eff9c8b8087354e27618d9da76425c119293f11712a6319"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:ed065083d0898c9d5b4bbec7b026fd755ff7454e6e8b73a67f8c744b13986e24"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:2cd4a60d0e2fb04537162c62bbbb4182f53541fe0ede35cdf270a1c1e723cc42"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:813c0e0132266c08eb87469a642cb30aaff57c5f426255419572aaeceeaa7bf4"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:07d9e39b01743c3717745f4c530a6349eadbfa043c7577eef86c502c15df2c67"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:c0f081d69a6e58272819b70288d3221a6ee64b98df852631c80f293514d3b274"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-win32.whl", hash = "sha256:8751d2787c9131302398b11e6c8068053dcb55d5a8964e114b6e196cf16cb366"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-win_amd64.whl", hash = "sha256:12a6fff75f6bc66711b73a2f0addfc4c8c15a20e805146a02d147a318962c444"},
    {file = "charset_normalizer-3.4.7-cp39-cp39-win_arm64.whl", hash = "sha256:bb8cc7534f51d9a017b93e3e85b260924f909601c3df002bcdb58ddb4dc41a5c"},
    {file = "charset_normalizer-3.4.7-py3-none-any.whl", hash = "sha256:3dce51d0f5e7951f8bb4900c257dad282f49190fdbebecd4ba99bcc41fef404d"},
    {file = "charset_normalizer-3.4.7.tar.gz", hash = "sha256:ae89db9e5f98a11a4bf50407d4363e7b09b31e55bc117b4f7d80aab97ba009e5"},
]

[[package]]
name = "click"
version = "8.4.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "click-8.4.1-py3-none-any.whl", hash = "sha256:482be17c6991b8c19c5429a1e995d9b0efdbb63172824c41f99965dc0ade8ec2"},
    {file = "click-8.4.1.tar.gz", hash = "sha256:918b5633eddf6b41c32d4f454bf0de810065c74e3f7dbf8ee5452f8be88d3e96"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["dev", "docs", "lint", "test"]
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]
markers = {dev = "sys_platform == \"win32\"", docs = "sys_platform == \"win32\"", lint = "platform_system == \"Windows\"", test = "sys_platform == \"win32\""}

[[package]]
name = "comm"
version = "0.2.3"
description = "Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "comm-0.2.3-py3-none-any.whl", hash = "sha256:c615d91d75f7f04f095b30d1c1711babd43bdc6419c1be9886a85f2f4e489417"},
    {file = "comm-0.2.3.tar.gz", hash = "sha256:2dc8048c10962d55d7ad693be1e7045d891b7ce8d999c97963a5e3e99c055971"},
]

[package.extras]
test = ["pytest"]

[[package]]
name = "coverage"
version = "7.14.1"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.10"
groups = ["test"]
files = [
    {file = "coverage-7.14.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:3e3680291c4a1d0dadfa84a2c459576a4af5133abb617905714339a0c73138cf"},
    {file = "coverage-7.14.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:a5274669f37f2343635a347b91a60777621341ab3378e9c6ac9335eee704bddf"},
    {file = "coverage-7.14.1-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:cfe5a5fec635799ef33428f1e5e61bafa45a92a96190ba731561ba558ccc214d"},
    {file = "coverage-7.14.1-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:62a9f70b52e0b5a95cfef4a5c5641b06983cadc5e538a3feeb5c00211f523ac2"},
    {file = "coverage-7.14.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3c18ebc343e15be53049b3a2dce38fe82d58f37e20ab9094b3a39c0aa4f6bb47"},
    {file = "coverage-7.14.1-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:b84ffdf877644e7096aa936991efeed873f7f3df57b9cd001312b7668ab08550"},
    {file = "coverage-7.14.1-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e854312c4103f2ad4c0dc023b69b77ebfd2c89db5f86c4c94dc2353f9a92167e"},
    {file = "coverage-7.14.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:c643734307300234fafa36bf2a040a7235f8f177ea1fd6ec1423aea6fb7b929f"},
    {file = "coverage-7.14.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:84ac9499e48700399a5dd0ea7085b5091961fec52c68d66b4ec0d3cf7f4441b1"},
    {file = "coverage-7.14.1-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:7f02d09f70776579b926d889a4c9c235070a1f47c40458aeaca563fae5acfdb5"},
    {file = "coverage-7.14.1-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:ce66d8e46da2bb5ee313a745cbd2e391d319176c1f7a9451bfcd3a2fb920859b"},
    {file = "coverage-7.14.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:c912c259304cfb5ee584481cfb7ce1ff932b4d61e6c9140b8f19cb7b5ed82332"},
    {file = "coverage-7.14.1-cp310-cp310-win32.whl", hash = "sha256:1238cb94638e610e972c60dac68e813f868dc7d6e982535270558443058d9d59"},
    {file = "coverage-7.14.1-cp310-cp310-win_amd64.whl", hash = "sha256:fc459e5d73be2d6332fcfe8dbf3d8994671fe33c700f4565988ecfa511547253"},
    {file = "coverage-7.14.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:478b5bcd63c2e1357c5c7e16c070690df7b07f676b1c114d7b93e533c664309f"},
    {file = "coverage-7.14.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:a24a81f9715ee42ef59a316cc11611c98fe23920f7c81861315c9f3ff4a230f4"},
    {file = "coverage-7.14.1-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:196a13319ad88d6d8ef5ab489ec4f44ddde2143c0c7d5b27786f6c3ffd56a7e1"},
    {file = "coverage-7.14.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:3d452fd08b5c72c5167c93e6867b5c08500bd40f2a21e1e854a500550b6cc36f"},
    {file = "coverage-7.14.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:23bf7fa51ac02e07fc7c96849b82946da47ae862dc8f86d183b2a4864fc38129"},
    {file = "coverage-7.14.1-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:bcaa50684dcaadfa599ac48f81103c756d791cfd85c97203d2217c593d48b860"},
    {file = "coverage-7.14.1-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:4ea1c034f95c9b056e856b794630b17f9fa3d57e4800ff1e503d3be0f9c9078c"},
    {file = "coverage-7.14.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c7e057326434e441306226fbeb5d1aaf14a2637efe97ba668306635835f32ad7"},
    {file = "coverage-7.14.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:59baf88468dbc8d63b1887afd92bda52e40bb1561696e5819670601403810cec"},
    {file = "coverage-7.14.1-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:d34d75f892b3ab73ba11cab5442cce7b3e168fd64162b16f0e1e0d09c508edef"},
    {file = "coverage-7.14.1-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:3a56abc20a472baf0304c455721bc601477440d28ecfde8a03dde79ede07e0df"},
    {file = "coverage-7.14.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:6a3cb83d1552c0cd1b4906655b6a33fd4a8473229633a901c6b73bf86914dee9"},
    {file = "coverage-7.14.1-cp311-cp311-win32.whl", hash = "sha256:10274a1fbeb8ec5d72966e17bb198a3104257aca4ac09d98667c5f8aca8c8548"},
    {file = "coverage-7.14.1-cp311-cp311-win_amd64.whl", hash = "sha256:87ebdf787d4888e3f3f2d523eadc6e18c6d18c6d0eb173801a189641627fb37e"},
    {file = "coverage-7.14.1-cp311-cp311-win_arm64.whl", hash = "sha256:dd34767fa19848d35659ffc0a75314f58c7af3f1cd87ec521e8292a1238398a3"},
    {file = "coverage-7.14.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:a06c76364a9360e33d6d23769aefdf7f66f38e2ffb60ceb1baaa4989d83b695c"},
    {file = "coverage-7.14.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fad54e871165f6ec2f536063ac74c3104508a12963e64072ba44bd822de52b0c"},
    {file = "coverage-7.14.1-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:84b535f00655ecafe1d929d1fb00ed5d6fa3051ea643ab2c161a3887b86f294b"},
    {file = "coverage-7.14.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:6b6b0853b895fe0e98cbfc580d1ec3393d9302b4b1e96a77b3f5c91fdab899e6"},
    {file = "coverage-7.14.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:442cc9c952b2df400cda54bb04ab87330cf2cd08a8692cbbea36773531eb6f37"},
    {file = "coverage-7.14.1-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:8270544c361ed405a27a060dbc9ed2c124b084d96dfdc2d9a2510482aef981ad"},
    {file = "coverage-7.14.1-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:48b283b1dd6372e8de2a7a9a4c4d5dc06f4d4fd209b876f3c88a7a205a0c8f84"},
    {file = "coverage-7.14.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5b0c99ba93a07d56f6df340bb79be53202a082b2fdb81bfe6190b741a3470d54"},
    {file = "coverage-7.14.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:e471bc5769ff073b058cfadb0d736b56ce067c8560eabeb0da88462df98c23e7"},
    {file = "coverage-7.14.1-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:f497a1ea81d4cd7c10ddcaa685135b9aabd291af3d55775a9ddf3cb7a364cdd9"},
    {file = "coverage-7.14.1-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:2222be86d0b54f5dd5a38f45f17f315f737245e857bf0bdedc70734f84a13c02"},
    {file = "coverage-7.14.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:85e85586565842f6932abebd4c18bcb1074223dc0b3576e7d173ca710622813a"},
    {file = "coverage-7.14.1-cp312-cp312-win32.whl", hash = "sha256:4a28fd227808366b196a75476dced2eb35b351d6766ba9c858dc93319e87f4f1"},
    {file = "coverage-7.14.1-cp312-cp312-win_amd64.whl", hash = "sha256:54acdb6674a4661768d7bf7db32dfb9f46ab1d764f8aba6df75ce1a6a088724e"},
    {file = "coverage-7.14.1-cp312-cp312-win_arm64.whl", hash = "sha256:99cd41ff91afd94896fea3bc002706b6ae4ce95727d06e4a0f39c0a8d8bd8b1a"},
    {file = "coverage-7.14.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:be9f2c802dcfce3f71298303aa5dad0dce440a76c52f2f60dacd8656dab78793"},
    {file = "coverage-7.14.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:6223a72fd0e4c7156353ec0f08a5f93623e1d3034d0e2683b9bb8ea674131b1d"},
    {file = "coverage-7.14.1-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:7279d2110a28cebc738b6459ecda2771735a4c18465fbbd36b3288fe5ed92247"},
    {file = "coverage-7.14.1-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:9eeb3fcbc13ba40dfbdb22d01d196a28e9cef9ed4c29b60061a1e0e823a9929d"},
    {file = "coverage-7.14.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5f0cfc27c539f07cf5c0a4cfe211d0b6cae039f8f40526dbaa71944e64b50a7b"},
    {file = "coverage-7.14.1-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:221c70f316241a78e77e607c227cefc8808d4e08f28d99c04f35694690e940be"},
    {file = "coverage-7.14.1-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:da028256b04ec30e5e0114b6f76172938c313991f0a2d3d894271315cf5d5e43"},
    {file = "coverage-7.14.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:76a085d7005236a767e3426148b2c407e53ad61695c562f8a81da2d373324901"},
    {file = "coverage-7.14.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:b553d04b5e778a8e56d57eb134aff42a92718ecba45e79c4764ecfa40efd92ff"},
    {file = "coverage-7.14.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:46f714d2fb8ae2f4f29f23ada7f1e79b759fff5a70f94a1dac23af204c3ec9e4"},
    {file = "coverage-7.14.1-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:1896f5e19ff3f0431c7ce2172adc54890fd97f86b59ced8ca1649145d9ffe35d"},
    {file = "coverage-7.14.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:62fd185ef9df3c33d1c8178c5af105f762afbad96038de9a4ae100aa6297ca33"},
    {file = "coverage-7.14.1-cp313-cp313-win32.whl", hash = "sha256:ab4af6352741a604c431c6072fce5bee33bf0f20dc7a56618d6bf6bb89e9810c"},
    {file = "coverage-7.14.1-cp313-cp313-win_amd64.whl", hash = "sha256:7af486dabe8954d03b087f0021540897afe084f04e16ff5579e08cc46f871416"},
    {file = "coverage-7.14.1-cp313-cp313-win_arm64.whl", hash = "sha256:2224f89ffd0c5605ccce1ed7a584da162bc7c55f601ab1c946bc9de31a486b42"},
    {file = "coverage-7.14.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:de286598cc65d2b489411174b1faec2f5a7775fb3201fd925db2a76b4030f37d"},
    {file = "coverage-7.14.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:042c46ded7c288aeb07cf14a28b6c1e10b78fcba40171c3fa1e939377eeef0b5"},
    {file = "coverage-7.14.1-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:f4ddbe407477f04c45115d1a4e5bc480f753553b534d338d4c3358b1cdd0ea52"},
    {file = "coverage-7.14.1-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:d13e6725992e2d2fd7d81d4f5241952d13740121dfd501da09201be39b2c003a"},
    {file = "coverage-7.14.1-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f747dc8edcfe740130f28f32f3995e955494285717e86ee25af51db2219df08a"},
    {file = "coverage-7.14.1-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:ced2f09ef276fd58611a1ef502164ad266d2b75174e5a40cabbdb4033f9f6cf2"},
    {file = "coverage-7.14.1-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b84800013769a78ccb9ef4659402e26d06867e337b61ec365f77ad008adea80e"},
    {file = "coverage-7.14.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:ea8cd6ca0ee9f616aaef3afc6882e32c2cbf18b00d96313ffd76af650574034d"},
    {file = "coverage-7.14.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:aa5e304a873fabddc11e484e9b6b738bd38bd7bed17b09aa84eecf5332e8b8bb"},
    {file = "coverage-7.14.1-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:5a1c5215be81035e629d5bc756650634d0bf31991038db7a0eccb90f025ce16d"},
    {file = "coverage-7.14.1-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:79058c47dae6788504b5effb319961bcd72d7240551464b91d474bc0ed186d69"},
    {file = "coverage-7.14.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:370c5afae3fa0658e11694a32b24c2778f6bc2d17718121f94ee185e69f26b54"},
    {file = "coverage-7.14.1-cp313-cp313t-win32.whl", hash = "sha256:3758dd0a7f1fa57365ef2e781df0f0731d38b6e3772259d13dae4bd8a958d4b1"},
    {file = "coverage-7.14.1-cp313-cp313t-win_amd64.whl", hash = "sha256:6ff665fb023a77386fe11685190cee1f60a7d635994a30d9b0a061533d470fce"},
    {file = "coverage-7.14.1-cp313-cp313t-win_arm64.whl", hash = "sha256:17a5a241e5997621a956a7f402a7433ef4221e5152809b785bec79e2323799f1"},
    {file = "coverage-7.14.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:d5ed429d0b8edaac649e889b4ffcedb6c80b06629a3f93050e3dddfb99235bee"},
    {file = "coverage-7.14.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:8011224a62280e50dab346960c03cf47aca1a1e09e608c0fb33fd6e0cc8e9500"},
    {file = "coverage-7.14.1-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:12c42ec1e14f553c4f817e989365982e646e27211f10a0f717855b94a79c8906"},
    {file = "coverage-7.14.1-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:06144cd511cf2624873a035c5069cf297144f6e77a73ee3d7a55b605ec5efb42"},
    {file = "coverage-7.14.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a311d8e1da24be5c1ccf85cbfb06315dbaa1703d5a1eab3f6432c72b837917c8"},
    {file = "coverage-7.14.1-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:c79cead5b5bc584d9c71451cb984d0e3a84e0c0937379c8efcbf27c8d661b851"},
    {file = "coverage-7.14.1-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:dcbf65f1f66a26cdd88c35cf68fb4729c5d1cd2e88added72420541dfb212034"},
    {file = "coverage-7.14.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:fd86572566fb40189a8260446158235159bc7a82dfbc87a3b39cf4fb57fcec1c"},
    {file = "coverage-7.14.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:7771b601718fdde84832c3a434ca9bbf4ae9adbc49d84198b4110700c3c77c36"},
    {file = "coverage-7.14.1-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:39b21e212c55af06fa375e3dbf90a8a8e38792f3a910c580066d23563830ddd5"},
    {file = "coverage-7.14.1-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:f2302660e32562a532b442480121aef8aa61a5bdb20b30bf0adab29f10a5a4b4"},
    {file = "coverage-7.14.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:03a6f93c1ec3b7f2e77b5dbcc5573a2c21f12529a5c6bbe0f16f72303cc2fa4d"},
    {file = "coverage-7.14.1-cp314-cp314-win32.whl", hash = "sha256:8a3ce026d73290f42f08dafecbd82c193a74df280461fbf97300fec51fd133ee"},
    {file = "coverage-7.14.1-cp314-cp314-win_amd64.whl", hash = "sha256:114c95ef29302423b87d159075805f4ab973254a2638a5d7d046c94887cc87d7"},
    {file = "coverage-7.14.1-cp314-cp314-win_arm64.whl", hash = "sha256:a07891c3f4805442b31b71e84ba3cf29ed1aa9a428284e06deeb4b23e5b46343"},
    {file = "coverage-7.14.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:1101a5ebb083aecb625ebb6209d4105b58f647b093cb2dc8122d7b33f743cfe1"},
    {file = "coverage-7.14.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:851b9e1e4e8a4608e77c79714b2e77c0970d2ed7202a05e92ae407817481887b"},
    {file = "coverage-7.14.1-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:d5b89cdfb2ee051b71e8c3c70bd81a9eff81100f736a269136fe1a68efe00474"},
    {file = "coverage-7.14.1-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:0177614a0370f227888b4e436a7c55686d6a9f90eb1ade2b624ba685a1686e86"},
    {file = "coverage-7.14.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2d69af5dea2de76fc485a83032a630523f985198b7e25be901ec60181587b01e"},
    {file = "coverage-7.14.1-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:35ab22d91de736e8966b980dc355cbcdd2c6dbbcfe275f9a2991bc8a91b3df65"},
    {file = "coverage-7.14.1-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:357d4e32935c36588aaba057d734fa32428c360c9fc2e4442afbf1b646beee6e"},
    {file = "coverage-7.14.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:51bd64741cc6fa065abd300ede1afe5a5291ece9c31da8b24884deda48bcc3f8"},
    {file = "coverage-7.14.1-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:9132cd363a68a4c3daa7c8704a654b1e39d3360f6f5b8ddd470608a945236c07"},
    {file = "coverage-7.14.1-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:07c6290b1697b862c0478eab545eec949a0d0e4d6d03497f446d706da3b4f2de"},
    {file = "coverage-7.14.1-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:5ea0c297e27133853b4d8a3eb799bff5a2dbd9f2f41537a240d337ac9b4df890"},
    {file = "coverage-7.14.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:01b7733daad0237daa01ef80fe2dfceffc911e6a17fa7b55d14aa8214eaaaecd"},
    {file = "coverage-7.14.1-cp314-cp314t-win32.whl", hash = "sha256:6adc5a36984624a70bf11d7184e20fa0a49aa7c47ffab43804106a1a695ea22e"},
    {file = "coverage-7.14.1-cp314-cp314t-win_amd64.whl", hash = "sha256:ddf799247318f34dbcd2efa8c95a8d0642674e926bb1774cf9b63dfd2a389d1c"},
    {file = "coverage-7.14.1-cp314-cp314t-win_arm64.whl", hash = "sha256:145986fe66647eb489f18d9a997567a3fd358584c4b5a808769113abc07466af"},
    {file = "coverage-7.14.1-py3-none-any.whl", hash = "sha256:a252f21c27e38347e60111a3266b03827422a7d5525951aceee313aa68bab1d2"},
    {file = "coverage-7.14.1.tar.gz", hash = "sha256:30c08f7d90415aa98b3c990385dea2939b0da55f38515e5b369b83655f8523be"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "datastore-utilities"
version = "0.1.0.dev0"
description = "Development utilities for datastore-python"
optional = false
python-versions = "^3.10"
groups = ["dev"]
files = []
develop = true

[package.source]
type = "directory"
url = "utilities"

[[package]]
name = "debugpy"
version = "1.8.21"
description = "An implementation of the Debug Adapter Protocol for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "debugpy-1.8.21-cp310-cp310-macosx_15_0_x86_64.whl", hash = "sha256:8eeab7b5462f683452c57c0126aaa5ec4e974ddb705f39ba87dff8818c8e08f9"},
    {file = "debugpy-1.8.21-cp310-cp310-manylinux_2_34_x86_64.whl", hash = "sha256:0fddfdc130ac6d8bfc0415b0409822fa901c8f310e5c945ac5653a0352532344"},
    {file = "debugpy-1.8.21-cp310-cp310-win32.whl", hash = "sha256:72b5d676c4cbfac3bac5bb01c138a4656e843f93f03ce2a5f4e394ad49fbee73"},
    {file = "debugpy-1.8.21-cp310-cp310-win_amd64.whl", hash = "sha256:a7fe47fd23da57b9e0bec3f4a8ee65a2dc55782455ed7f2141d75ab5d2eaeef5"},
    {file = "debugpy-1.8.21-cp311-cp311-macosx_15_0_universal2.whl", hash = "sha256:da456226c7b4c69e35dbe35dcee6623d912000a77816db7856a41af1c72a0264"},
    {file = "debugpy-1.8.21-cp311-cp311-manylinux_2_34_x86_64.whl", hash = "sha256:f68b891688e61bdc08b8d364d919ff0051e0b94657b39dcd027bc3173edb7cdc"},
    {file = "debugpy-1.8.21-cp311-cp311-win32.whl", hash = "sha256:f843a8b08c2edeaf9b1582eed4f25441af21a297c22ff16bf76a662557aa9c9e"},
    {file = "debugpy-1.8.21-cp311-cp311-win_amd64.whl", hash = "sha256:84c564d8cc701d41843b29a92814c1f1bef6798724ca9d675c284ad9f6a547d7"},
    {file = "debugpy-1.8.21-cp312-cp312-macosx_15_0_universal2.whl", hash = "sha256:9f96713896f39c3dff0ee841f47320c3f2983d33c341e009361bb0ebc79adc4e"},
    {file = "debugpy-1.8.21-cp312-cp312-manylinux_2_34_x86_64.whl", hash = "sha256:c193d474f0a211191f2b4449d2d06157c689013035bd952f3b617e0ef422b176"},
    {file = "debugpy-1.8.21-cp312-cp312-win32.whl", hash = "sha256:4743373c1cac7f9e74a1b9915bf1dbe0e900eca657ffb170ae07ac8363205ae9"},
    {file = "debugpy-1.8.21-cp312-cp312-win_amd64.whl", hash = "sha256:bd7ba9dd3daa7c2f942c6ca8d4695a16bf9ac16b63615261c7982bc74f7ed20c"},
    {file = "debugpy-1.8.21-cp313-cp313-macosx_15_0_universal2.whl", hash = "sha256:13678151fc401e2d68c9880b91e28714f797d40422994572b24560ef80910a88"},
    {file = "debugpy-1.8.21-cp313-cp313-manylinux_2_34_x86_64.whl", hash = "sha256:ecbd158386c31ffe71d46f72d44d56e66331ab9b16cad649156d514368f23ab2"},
    {file = "debugpy-1.8.21-cp313-cp313-win32.whl", hash = "sha256:2c2ae706dec41d99a9ca1f7ebc987a83e65578363be6f6b3ac9067504917fae1"},
    {file = "debugpy-1.8.21-cp313-cp313-win_amd64.whl", hash = "sha256:aa648733047443eb1d07682c4ef287d36a54507b643ffdf38b09a3ef002c72a0"},
    {file = "debugpy-1.8.21-cp314-cp314-macosx_15_0_universal2.whl", hash = "sha256:9bb2a685287a2ac9b181cde89edcec64845cb51de7faaa75badb9a698bc24782"},
    {file = "debugpy-1.8.21-cp314-cp314-manylinux_2_34_x86_64.whl", hash = "sha256:3d6922439bf33fd38a3e2c447869ebc7b97da5cd3d329ff1ef9bc06c4903437e"},
    {file = "debugpy-1.8.21-cp314-cp314-win32.whl", hash = "sha256:15d4963bd5ffa48f0da0947fd06757fa7621945048a14ad7705431566d3c0e7c"},
    {file = "debugpy-1.8.21-cp314-cp314-win_amd64.whl", hash = "sha256:fe0744a12353406de0ae8ccff0d0a4a666f00801a3db8fd04e7a5f761cd520e8"},
    {file = "debugpy-1.8.21-cp38-cp38-macosx_15_0_x86_64.whl", hash = "sha256:0042da0ecd0a8b50dc4a54395ecd870d258d73fa18776f50c91fdcabdcad2675"},
    {file = "debugpy-1.8.21-cp38-cp38-manylinux_2_34_x86_64.whl", hash = "sha256:ffd932c6796afadab6993ec96745918a8cb2444dbd392074f769db5ea40ab440"},
    {file = "debugpy-1.8.21-cp38-cp38-win32.whl", hash = "sha256:4e7c2d784d78ad4b71a5f8cd7b59c167719ec8a7a0211dbb3eb1bfeda78bc4e2"},
    {file = "debugpy-1.8.21-cp38-cp38-win_amd64.whl", hash = "sha256:aa9d941d6dfe3d0407e4b3ca0b9ec466030e260fbf1174094f68785680f66db6"},
    {file = "debugpy-1.8.21-cp39-cp39-macosx_15_0_x86_64.whl", hash = "sha256:9f5171176a0084b95d2ebe55a4d1f7b2a75b74c5dbec577ebd3a85c740551c36"},
    {file = "debugpy-1.8.21-cp39-cp39-manylinux_2_34_x86_64.whl", hash = "sha256:f15c10084f9861b5e8414a48f18f8e4aadf51a98a59e72c16aa28281ca994672"},
    {file = "debugpy-1.8.21-cp39-cp39-win32.whl", hash = "sha256:4e70cc8b5079f885cb43910924ee0aab73b8b6b2a14eff23afdd9895d86e79eb"},
    {file = "debugpy-1.8.21-cp39-cp39-win_amd64.whl", hash = "sha256:e935f9dc0501be523c8a8e1853c39432e1354e9ece717ae5998fd2371c4542c3"},
    {file = "debugpy-1.8.21-py2.py3-none-any.whl", hash = "sha256:b1e37d333663c8851516a47364ef473da127f9caebe4417e6df6f5825a7e9a92"},
    {file = "debugpy-1.8.21.tar.gz", hash = "sha256:a3c53278e84c94e11bd87c53970ec391d1a67396c8b22609fcac576520e611a6"},
]

[[package]]
name = "decorator"
version = "5.3.1"
description = "Decorators for Humans"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "decorator-5.3.1-py3-none-any.whl", hash = "sha256:f47fe6fdbd2edd623ecfe36875d37aba411624e2670dd395dddae1358689bb3c"},
    {file = "decorator-5.3.1.tar.gz", hash = "sha256:4cbcdd55a6efadb9dbea26b858f4fb3264567b52d69ca0d25b721b553f60ea82"},
]

[[package]]
name = "defusedxml"
version = "0.7.1"
description = "XML bomb protection for Python stdlib modules"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"
groups = ["dev"]
files = [
    {file = "defusedxml-0.7.1-py2.py3-none-any.whl", hash = "sha256:a352e7e428770286cc899e2542b6cdaedb2b4953ff269a210103ec58f6198a61"},
    {file = "defusedxml-0.7.1.tar.gz", hash = "sha256:1bb3032db185915b62d7c6209c5a8792be6a32ab2fedacc84e01b52c51aa3e69"},
]

[[package]]
name = "docutils"
version = "0.21.2"
description = "Docutils -- Python Documentation Utilities"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "docutils-0.21.2-py3-none-any.whl", hash = "sha256:dafca5b9e384f0e419294eb4d2ff9fa826435bf15f15b7bd45723e8ad76811b2"},
    {file = "docutils-0.21.2.tar.gz", hash = "sha256:3a6b18732edf182daa3cd12775bbb338cf5691468f91eeeb109deff6ebfa986f"},
]

[[package]]
name = "docutils"
version = "0.22.4"
description = "Docutils -- Python Documentation Utilities"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "docutils-0.22.4-py3-none-any.whl", hash = "sha256:d0013f540772d1420576855455d050a2180186c91c15779301ac2ccb3eeb68de"},
    {file = "docutils-0.22.4.tar.gz", hash = "sha256:4db53b1fde9abecbb74d91230d32ab626d94f6badfc575d6db9194a49df29968"},
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
groups = ["dev", "test"]
markers = "python_version == \"3.10\""
files = [
    {file = "exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598"},
    {file = "exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219"},
]

[package.dependencies]
typing-extensions = {version = ">=4.6.0", markers = "python_version < \"3.13\""}

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "executing"
version = "2.2.1"
description = "Get the currently executing AST node of a frame, and other information"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "executing-2.2.1-py2.py3-none-any.whl", hash = "sha256:760643d3452b4d777d295bb167ccc74c64a81df23fb5e08eff250c425a4b2017"},
    {file = "executing-2.2.1.tar.gz", hash = "sha256:3632cc370565f6648cc328b32435bd120a1e4ebb20c77e3fdde9a13cd1e533c4"},
]

[package.extras]
tests = ["asttokens (>=2.1.0)", "coverage", "coverage-enable-subprocess", "ipython", "littleutils", "pytest", "rich ; python_version >= \"3.11\""]

[[package]]
name = "fastjsonschema"
version = "2.21.2"
description = "Fastest Python implementation of JSON schema"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "fastjsonschema-2.21.2-py3-none-any.whl", hash = "sha256:1c797122d0a86c5cace2e54bf4e819c36223b552017172f32c5c024a6b77e463"},
    {file = "fastjsonschema-2.21.2.tar.gz", hash = "sha256:b1eb43748041c880796cd077f1a07c3d94e93ae84bba5ed36800a33554ae05de"},
]

[package.extras]
devel = ["colorama", "json-spec", "jsonschema", "pylint", "pytest", "pytest-benchmark", "pytest-cache", "validictory"]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "flake8-6.1.0-py2.py3-none-any.whl", hash = "sha256:ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5"},
    {file = "flake8-6.1.0.tar.gz", hash = "sha256:d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.11.0,<2.12.0"
pyflakes = ">=3.1.0,<3.2.0"

[[package]]
name = "flake8-black"
version = "0.4.0"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_black-0.4.0-py3-none-any.whl", hash = "sha256:288762d0c9ea065782d87eeecbcc20c69079d17fe1d0f0445f0eb0b0ffb80c39"},
    {file = "flake8_black-0.4.0.tar.gz", hash = "sha256:bf226868f695dee48d55ff6d7747e900709bfd6f605b7a378c70e711e3fc26cb"},
]

[package.dependencies]
black = ">=22.1.0"
flake8 = ">=3"
tomli = {version = "*", markers = "python_version < \"3.11\""}

[package.extras]
develop = ["build", "twine"]

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["lint"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "flake8-tidy-imports"
version = "4.12.0"
description = "A flake8 plugin that helps you write tidier imports."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "fqdn"
version = "1.5.1"
description = "Validates fully-qualified domain names against RFC 1123, so that they are acceptable to modern bowsers"
optional = false
python-versions = ">=2.7, !=3.0, !=3.1, !=3.2, !=3.3, !=3.4, <4"
groups = ["dev"]
files = [
    {file = "fqdn-1.5.1-py3-none-any.whl", hash = "sha256:3a179af3761e4df6eb2e026ff9e1a3033d3587bf980a0b1b2e1e5d08d7358014"},
    {file = "fqdn-1.5.1.tar.gz", hash = "sha256:105ed3677e767fb5ca086a0c1f4bb66ebc3c100be518f0e0d755d9eae164d89f"},
]

[[package]]
name = "grpcio"
version = "1.81.0"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "grpcio-1.81.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:b4108e5d9d0f651b7eea749116181fe6c315b145661a80ec31f05ec2dbe21af7"},
    {file = "grpcio-1.81.0-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:b76ea9d55cd08fcdbda25d28e0f76679536710acb7fbd5b1f70cb4ac49317265"},
    {file = "grpcio-1.81.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:4e032feb3bfb4e2749b140a2302a6baa8ead1b9781ff5cf7094e4402b5e9372e"},
    {file = "grpcio-1.81.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:725801c7086d7e4cd160e42bb2f54e0aeb976b9568df3cc6f843b15d29b79fb1"},
    {file = "grpcio-1.81.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:f750a091fff3a3991731abc1f818bdc64874bb3528162732cb4d45f2e07821a6"},
    {file = "grpcio-1.81.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:8226ba097eed660ef14d36c6a69b85038552bb8b6d17b44a5aa6f9abf48b8e08"},
    {file = "grpcio-1.81.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:40edffb4ec3689373825d367c4457727047a6e554f03245265ecc8cc03215f22"},
    {file = "grpcio-1.81.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f85570a016d794c29b1e76cf22f67af4486ddbe779e0f30674f138fa4e1769ec"},
    {file = "grpcio-1.81.0-cp310-cp310-win32.whl", hash = "sha256:3755c9669307cad18e7e009860fdea98118978d2300451bd8530a53048e741e7"},
    {file = "grpcio-1.81.0-cp310-cp310-win_amd64.whl", hash = "sha256:909bb3222b53235498d2c5817a0596d82b0aaea490ba93fdf1b060e2938a543c"},
    {file = "grpcio-1.81.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:794e6aa648e8df47d8f908dc8c3b42347d04ec58438f1dcd4e445f09b4f6b0ce"},
    {file = "grpcio-1.81.0-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:cd78145b7f7784661c524624f3526c9c6f891b30a4b54cb93a40806d0d0d61e9"},
    {file = "grpcio-1.81.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:638ccc1b86f7540170a169cb900799b9296a1381e47879ce60b0de9d3db73d33"},
    {file = "grpcio-1.81.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:21ec30b9ea320c8207ea7cd05873ad64aa69fdd0e81b6758b3347983ba20b50a"},
    {file = "grpcio-1.81.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:dbdb99986548a7e87f8343805ef315fd4eb50ffaabf4fb1206e42f2542bb805d"},
    {file = "grpcio-1.81.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c36f5d5e97944cbda2d4096b4ae262e6e68506246b61582acf1b8591607f3ccc"},
    {file = "grpcio-1.81.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:9f355384e5543ab77a755a7085225ecc19f32b76032e851cbd8145715d79dec8"},
    {file = "grpcio-1.81.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:77eb4e9fe61486bd1198cc7236ebb0f70e66234e63c0348f40bc2553ed16a88b"},
    {file = "grpcio-1.81.0-cp311-cp311-win32.whl", hash = "sha256:7915a2e63acdc05264a206e1bddfd8e1fb8a29e406c18d72d30f8c124e021374"},
    {file = "grpcio-1.81.0-cp311-cp311-win_amd64.whl", hash = "sha256:5e925a70fe99fe5794f7beca0ea034c75f068afcc356d79047e73f99cdcca34c"},
    {file = "grpcio-1.81.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:57b3b0e73a518fa286959b40c3eddd02703504ca186e8b7b2945954519bd8b2c"},
    {file = "grpcio-1.81.0-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:8bb1789c94322a13336a2b6c58d9c14d68f8628b6e24205a799c69f5bf8516ce"},
    {file = "grpcio-1.81.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:e4d053900a0d24b75d7521139a3872150301b3d6bde3bed5e12318fb25791e4d"},
    {file = "grpcio-1.81.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:db217c2e52931719f9937bd12082cd4d7b495b35803d5760686975c285924bf8"},
    {file = "grpcio-1.81.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:19f201da7b4e5c0559198abe5a97157e726f3abe6e8f5e832d4a50740f6dcc22"},
    {file = "grpcio-1.81.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:275144b0115353339dbb8a6f28a9cf8997b5bf40e37f8f66ac0b0ea57e95b43f"},
    {file = "grpcio-1.81.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:5192857589f223e5a98ff0e31f6e551b19040e647d17bfe10116c8a2ce3b8696"},
    {file = "grpcio-1.81.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:c6ff087cb1f563f47b504b4e29e684129fc5ae4863faf3ebca08a327764ee6cb"},
    {file = "grpcio-1.81.0-cp312-cp312-win32.whl", hash = "sha256:98c6240f563178fc5877bd50e6ff274463e53e1472128f4110742450739659fa"},
    {file = "grpcio-1.81.0-cp312-cp312-win_amd64.whl", hash = "sha256:87e33b7afcfb3585121b5f007d2c52b8c534104d18f556e840d35193ca2a9141"},
    {file = "grpcio-1.81.0-cp313-cp313-linux_armv7l.whl", hash = "sha256:62bbe463c9f0f2ff24e31bd25f8dd8b4bae78900e315915a3195a0ef1471a855"},
    {file = "grpcio-1.81.0-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:43c121e135ae44d1559b430db2b2dfad7421cbbe40e1deba506c7dc62b439719"},
    {file = "grpcio-1.81.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:f345de40ef2e65f63645d53d251824e6070e07804827c5b00ec2e44555f9f901"},
    {file = "grpcio-1.81.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:8c0855a350886f713b9e458e2a10d208009dcaa849f574e39cd6067db1fe1279"},
    {file = "grpcio-1.81.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:a524cd530900bd24511fcb7f2ed144da4ea37711c4b094475d0bceca7a93a170"},
    {file = "grpcio-1.81.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e7746ba3e6efc9e2b748eff59470a2b8684d5a9ec607c6580bcaa5be175820bc"},
    {file = "grpcio-1.81.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:aaaa4f7f2057d795952e4eacf3f342be8b5b156992f6ac85023c8b98794ebd47"},
    {file = "grpcio-1.81.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:0fba53cb96004b2b7fb758b46b2288cb49d0b658316a4e73f3ef67230616ee65"},
    {file = "grpcio-1.81.0-cp313-cp313-win32.whl", hash = "sha256:c197e2ef75a442528072b29e9755da299110e8610e8bcbb59a6b4cf55384f005"},
    {file = "grpcio-1.81.0-cp313-cp313-win_amd64.whl", hash = "sha256:194eddfacc84d80f50512e9fd4ee851d5f2499f18f299c95aa8fb4748f0537e0"},
    {file = "grpcio-1.81.0-cp314-cp314-linux_armv7l.whl", hash = "sha256:a9351055f52660b58f3d4890ea66188b5134399f82b11aa0c55bd4b99eff5390"},
    {file = "grpcio-1.81.0-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:300f3337b6425fd16ead9a4f9b2ac25801acb64aa5bc0b99eb69901645b2b1d2"},
    {file = "grpcio-1.81.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:97bbd623f7ded558fd4f7cb5a4f600c4d4de65c5dd364c83a5b14b2a10a2d3b5"},
    {file = "grpcio-1.81.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:ff83d889e3ebf6341c8c7864ad8031591ad5ca61599072fc511644d1eb962d2b"},
    {file = "grpcio-1.81.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c4fe218c5a35e1d87a5a26544237f1fa41dfd9cbd3c856b0810a30061f8b0aaf"},
    {file = "grpcio-1.81.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b8b025b6af43ee0ad4a70307025d77bcab5adde7c4597786010d802c203e9fc5"},
    {file = "grpcio-1.81.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:3d4e0ce5a40a998cf608c8ba60ecfe18fdf364a9aa193ae4ac3faeecd0e86757"},
    {file = "grpcio-1.81.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:aa948712c8e5fa40ec250870bda14bc7578e1bb832a8912d9d2a0f720518edbe"},
    {file = "grpcio-1.81.0-cp314-cp314-win32.whl", hash = "sha256:fbbe81314a9d92156abce8b62c09364eb8bafc0ca2a19919a45ec64b5c6cb664"},
    {file = "grpcio-1.81.0-cp314-cp314-win_amd64.whl", hash = "sha256:b93cee313cae4e113fbb3a0ce1ea5633db6f63cfde2b2dc1d817429026b2a50b"},
    {file = "grpcio-1.81.0.tar.gz", hash = "sha256:a5acd7efd3b1fe9b4eb0bcaaa1507eed68a0ad0678b654c3f7b464df9ba9dca5"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.81.0)"]

[[package]]
name = "h11"
version = "0.16.0"
description = "A pure-Python, bring-your-own-I/O implementation of HTTP/1.1"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86"},
    {file = "h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1"},
]

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "httpcore"
version = "1.0.9"
description = "A minimal low-level HTTP client."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55"},
    {file = "httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8"},
]

[package.dependencies]
certifi = "*"
h11 = ">=0.16"

[package.extras]
asyncio = ["anyio (>=4.0,<5.0)"]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (==1.*)"]
trio = ["trio (>=0.22.0,<1.0)"]

[[package]]
name = "httpx"
version = "0.28.1"
description = "The next generation HTTP client."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad"},
    {file = "httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc"},
]

[package.dependencies]
anyio = "*"
certifi = "*"
httpcore = "==1.*"
idna = "*"

[package.extras]
brotli = ["brotli ; platform_python_implementation == \"CPython\"", "brotlicffi ; platform_python_implementation != \"CPython\""]
cli = ["click (==8.*)", "pygments (==2.*)", "rich (>=10,<14)"]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (==1.*)"]
zstd = ["zstandard (>=0.18.0)"]

[[package]]
name = "idna"
version = "3.18"
description = "Internationalized Domain Names in Applications (IDNA)"
optional = false
python-versions = ">=3.9"
groups = ["dev", "docs"]
files = [
    {file = "idna-3.18-py3-none-any.whl", hash = "sha256:7f952cbe720b688055e3f87de14f5c3e5fdaa8bc3928985c4077ca689de849a2"},
    {file = "idna-3.18.tar.gz", hash = "sha256:ffb385a7e039654cef1ab9ef32c6fafe283c0c0467bba1d9029738ce4a14a848"},
]

[package.extras]
all = ["mypy (>=1.11.2)", "pytest (>=8.3.2)", "ruff (>=0.6.2)"]

[[package]]
name = "imagesize"
version = "1.5.0"
description = "Getting image size from png/jpeg/jpeg2000/gif file"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,>=2.7"
groups = ["docs"]
markers = "python_version >= \"3.15\""
files = [
    {file = "imagesize-1.5.0-py2.py3-none-any.whl", hash = "sha256:32677681b3f434c2cb496f00e89c5a291247b35b1f527589909e008057da5899"},
    {file = "imagesize-1.5.0.tar.gz", hash = "sha256:8bfc5363a7f2133a89f0098451e0bcb1cd71aba4dc02bbcecb39d99d40e1b94f"},
]

[[package]]
name = "imagesize"
version = "2.0.0"
description = "Get image size from headers (BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Netpbm/WebP/AVIF/HEIC/HEIF)"
optional = false
python-versions = "<3.15,>=3.10"
groups = ["docs"]
markers = "python_version < \"3.15\""
files = [
    {file = "imagesize-2.0.0-py2.py3-none-any.whl", hash = "sha256:5667c5bbb57ab3f1fa4bc366f4fbc971db3d5ed011fd2715fd8001f782718d96"},
    {file = "imagesize-2.0.0.tar.gz", hash = "sha256:8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3"},
]

[[package]]
name = "iniconfig"
version = "2.3.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.10"
groups = ["test"]
files = [
    {file = "iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12"},
    {file = "iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730"},
]

[[package]]
name = "ipykernel"
version = "7.3.0"
description = "IPython Kernel for Jupyter"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "ipykernel-7.3.0-py3-none-any.whl", hash = "sha256:897eb64da762549ef610698fca5e9675195ec6ac8ec7f19d81ce1ca20c876057"},
    {file = "ipykernel-7.3.0.tar.gz", hash = "sha256:9acaaaf97d16355166e4085afe9d225bfbdf2b7ef520f9df3be8f2b248275e09"},
]

[package.dependencies]
appnope = {version = ">=0.1.2", markers = "platform_system == \"Darwin\""}
comm = ">=0.1.1"
debugpy = ">=1.6.5"
ipython = ">=7.23.1"
jupyter-client = ">=8.9.0"
jupyter-core = ">=5.1,<6.0.dev0 || >=6.1.dev0"
matplotlib-inline = ">=0.1"
nest-asyncio2 = ">=1.7.0"
packaging = ">=22"
psutil = ">=5.7"
pyzmq = ">=25"
tornado = ">=6.4.1"
traitlets = ">=5.4.0"

[package.extras]
cov = ["coverage[toml]", "matplotlib", "pytest-cov", "trio"]
docs = ["intersphinx-registry", "myst-parser", "pydata-sphinx-theme", "sphinx", "sphinx-autodoc-typehints", "sphinxcontrib-github-alt", "sphinxcontrib-spelling", "trio"]
pyqt5 = ["pyqt5"]
pyside6 = ["pyside6"]
test = ["flaky", "ipyparallel", "pre-commit", "pytest (>=7.0,<10)", "pytest-asyncio (>=0.23.5)", "pytest-cov", "pytest-timeout"]

[[package]]
name = "ipython"
version = "8.39.0"
description = "IPython: Productive Interactive Computing"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "ipython-8.39.0-py3-none-any.whl", hash = "sha256:bb3c51c4fa8148ab1dea07a79584d1c854e234ea44aa1283bcb37bc75054651f"},
    {file = "ipython-8.39.0.tar.gz", hash = "sha256:4110ae96012c379b8b6db898a07e186c40a2a1ef5d57a7fa83166047d9da7624"},
]

[package.dependencies]
colorama = {version = "*", markers = "sys_platform == \"win32\""}
decorator = "*"
exceptiongroup = {version = "*", markers = "python_version < \"3.11\""}
jedi = ">=0.16"
matplotlib-inline = "*"
pexpect = {version = ">4.3", markers = "sys_platform != \"win32\" and sys_platform != \"emscripten\""}
prompt_toolkit = ">=3.0.41,<3.1.0"
pygments = ">=2.4.0"
stack_data = "*"
traitlets = ">=5.13.0"
typing_extensions = {version = ">=4.6", markers = "python_version < \"3.12\""}

[package.extras]
all = ["ipython[black,doc,kernel,matplotlib,nbconvert,nbformat,notebook,parallel,qtconsole]", "ipython[test,test-extra]"]
black = ["black"]
doc = ["docrepr", "exceptiongroup", "intersphinx_registry", "ipykernel", "ipython[test]", "matplotlib", "setuptools (>=18.5)", "sphinx (>=1.3)", "sphinx-rtd-theme", "sphinxcontrib-jquery", "tomli ; python_version < \"3.11\"", "typing_extensions"]
kernel = ["ipykernel"]
matplotlib = ["matplotlib"]
nbconvert = ["nbconvert"]
nbformat = ["nbformat"]
notebook = ["ipywidgets", "notebook"]
parallel = ["ipyparallel"]
qtconsole = ["qtconsole"]
test = ["packaging", "pickleshare", "pytest", "pytest-asyncio (<0.22)", "testpath"]
test-extra = ["curio", "ipython[test]", "jupyter_ai", "matplotlib (!=3.2.0)", "nbformat", "numpy (>=1.23)", "pandas", "trio"]

[[package]]
name = "ipython"
version = "9.15.0"
description = "IPython: Productive Interactive Computing"
optional = false
python-versions = ">=3.11"
groups = ["dev"]
markers = "python_version >= \"3.11\""
files = [
    {file = "ipython-9.15.0-py3-none-any.whl", hash = "sha256:515ad9c3cdf0c932a5a9f6245419e8aba706b7bd03c3e1d3a1c83d9351d6aa6e"},
    {file = "ipython-9.15.0.tar.gz", hash = "sha256:da2819ce2aa83135257df830660b1176d986c3d2876db24df01974fa955b2756"},
]

[package.dependencies]
colorama = {version = ">=0.4.4", markers = "sys_platform == \"win32\""}
decorator = ">=5.1.0"
ipython-pygments-lexers = ">=1.0.0"
jedi = ">=0.18.2"
matplotlib-inline = ">=0.1.6"
pexpect = {version = ">4.6", markers = "sys_platform != \"win32\" and sys_platform != \"emscripten\""}
prompt_toolkit = ">=3.0.41,<3.1.0"
psutil = {version = ">=7", markers = "sys_platform != \"emscripten\" and sys_platform != \"cygwin\""}
pygments = ">=2.14.0"
stack_data = ">=0.6.0"
traitlets = ">=5.13.0"
typing_extensions = {version = ">=4.6", markers = "python_version < \"3.12\""}

[package.extras]
all = ["argcomplete (>=3.0)", "ipython[doc,matplotlib,terminal,test,test-extra]", "types-decorator"]
black = ["black"]
doc = ["docrepr", "exceptiongroup", "intersphinx_registry", "ipykernel", "ipython[matplotlib,test]", "setuptools (>=80.0)", "sphinx (>=8.0)", "sphinx-rtd-theme (>=0.1.8)", "sphinx_toml (==0.0.4)", "typing_extensions"]
matplotlib = ["matplotlib (>3.9)"]
test = ["packaging (>=23.0.0)", "pytest (>=7.0.0)", "pytest-asyncio (>=1.0.0)", "setuptools (>=80.0)", "testpath (>=0.2)"]
test-extra = ["curio", "ipykernel (>6.30)", "ipython[matplotlib]", "ipython[test]", "jupyter_ai", "nbclient", "nbformat", "numpy (>=2.0)", "pandas (>2.1)", "trio (>=0.22.0)"]

[[package]]
name = "ipython-pygments-lexers"
version = "1.1.1"
description = "Defines a variety of Pygments lexers for highlighting IPython code."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version >= \"3.11\""
files = [
    {file = "ipython_pygments_lexers-1.1.1-py3-none-any.whl", hash = "sha256:a9462224a505ade19a605f71f8fa63c2048833ce50abc86768a0d81d876dc81c"},
    {file = "ipython_pygments_lexers-1.1.1.tar.gz", hash = "sha256:09c0138009e56b6854f9535736f4171d855c8c08a563a0dcd8022f78355c7e81"},
]

[package.dependencies]
pygments = "*"

[[package]]
name = "ipywidgets"
version = "8.1.8"
description = "Jupyter interactive widgets"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "ipywidgets-8.1.8-py3-none-any.whl", hash = "sha256:ecaca67aed704a338f88f67b1181b58f821ab5dc89c1f0f5ef99db43c1c2921e"},
    {file = "ipywidgets-8.1.8.tar.gz", hash = "sha256:61f969306b95f85fba6b6986b7fe45d73124d1d9e3023a8068710d47a22ea668"},
]

[package.dependencies]
comm = ">=0.1.3"
ipython = ">=6.1.0"
jupyterlab_widgets = ">=3.0.15,<3.1.0"
traitlets = ">=4.3.1"
widgetsnbextension = ">=4.0.14,<4.1.0"

[package.extras]
test = ["ipykernel", "jsonschema", "pytest (>=3.6.0)", "pytest-cov", "pytz"]

[[package]]
name = "isoduration"
version = "20.11.0"
description = "Operations with ISO 8601 durations"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "isoduration-20.11.0-py3-none-any.whl", hash = "sha256:b2904c2a4228c3d44f409c8ae8e2370eb21a26f7ac2ec5446df141dde3452042"},
    {file = "isoduration-20.11.0.tar.gz", hash = "sha256:ac2f9015137935279eac671f94f89eb00584f940f5dc49462a0c4ee692ba1bd9"},
]

[package.dependencies]
arrow = ">=0.15.0"

[[package]]
name = "isort"
version = "8.0.1"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["lint"]
files = [
    {file = "isort-8.0.1-py3-none-any.whl", hash = "sha256:28b89bc70f751b559aeca209e6120393d43fbe2490de0559662be7a9787e3d75"},
    {file = "isort-8.0.1.tar.gz", hash = "sha256:171ac4ff559cdc060bcfff550bc8404a486fee0caab245679c2abe7cb253c78d"},
]

[package.extras]
colors = ["colorama"]

[[package]]
name = "jedi"
version = "0.20.0"
description = "An autocompletion tool for Python that can be used for text editors."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jedi-0.20.0-py2.py3-none-any.whl", hash = "sha256:7bdd9c2634f56713299976f4cbd59cb3fa92165cc5e05ea811fb253480728b67"},
    {file = "jedi-0.20.0.tar.gz", hash = "sha256:c3f4ccbd276696f4b19c54618d4fb18f9fc24b0aef02acf704b23f487daa1011"},
]

[package.dependencies]
parso = ">=0.8.6,<0.9.0"

[package.extras]
dev = ["Django", "attrs", "colorama", "docopt", "flake8 (==7.1.2)", "pytest (<9.0.0)", "types-setuptools (==80.9.0.20250529)", "typing-extensions", "zuban (==0.7.0)"]
docs = ["Jinja2 (==3.1.6)", "MarkupSafe (==3.0.3)", "Pygments (==2.20.0)", "Sphinx (==9.1.0)", "alabaster (==1.0.0)", "babel (==2.18.0)", "certifi (==2026.4.22)", "charset-normalizer (==3.4.7)", "docutils (==0.22.4)", "idna (==3.13)", "imagesize (==2.0.0)", "iniconfig (==2.3.0)", "packaging (==26.2)", "pluggy (==1.6.0)", "pytest (==9.0.3)", "requests (==2.33.1)", "roman-numerals (==4.1.0)", "snowballstemmer (==3.0.1)", "sphinx-rtd-theme (==3.1.0)", "sphinxcontrib-applehelp (==2.0.0)", "sphinxcontrib-devhelp (==2.0.0)", "sphinxcontrib-htmlhelp (==2.1.0)", "sphinxcontrib-jquery (==4.1)", "sphinxcontrib-jsmath (==1.0.1)", "sphinxcontrib-qthelp (==2.0.0)", "sphinxcontrib-serializinghtml (==2.0.0)", "urllib3 (==2.6.3)"]

[[package]]
name = "jinja2"
version = "3.1.6"
description = "A very fast and expressive template engine."
optional = false
python-versions = ">=3.7"
groups = ["dev", "docs"]
files = [
    {file = "jinja2-3.1.6-py3-none-any.whl", hash = "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67"},
    {file = "jinja2-3.1.6.tar.gz", hash = "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d"},
]

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "json5"
version = "0.14.0"
description = "A Python implementation of the JSON5 data format."
optional = false
python-versions = ">=3.8.0"
groups = ["dev"]
files = [
    {file = "json5-0.14.0-py3-none-any.whl", hash = "sha256:56cf861bab076b1178eb8c92e1311d273a9b9acea2ccc82c276abf839ebaef3a"},
    {file = "json5-0.14.0.tar.gz", hash = "sha256:b3f492fad9f6cdbced8b7d40b28b9b1c9701c5f561bef0d33b81c2ff433fefcb"},
]

[[package]]
name = "jsonpointer"
version = "3.1.1"
description = "Identify specific nodes in a JSON document (RFC 6901) "
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jsonpointer-3.1.1-py3-none-any.whl", hash = "sha256:8ff8b95779d071ba472cf5bc913028df06031797532f08a7d5b602d8b2a488ca"},
    {file = "jsonpointer-3.1.1.tar.gz", hash = "sha256:0b801c7db33a904024f6004d526dcc53bbb8a4a0f4e32bfd10beadf60adf1900"},
]

[[package]]
name = "jsonschema"
version = "4.26.0"
description = "An implementation of JSON Schema validation for Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jsonschema-4.26.0-py3-none-any.whl", hash = "sha256:d489f15263b8d200f8387e64b4c3a75f06629559fb73deb8fdfb525f2dab50ce"},
    {file = "jsonschema-4.26.0.tar.gz", hash = "sha256:0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326"},
]

[package.dependencies]
attrs = ">=22.2.0"
fqdn = {version = "*", optional = true, markers = "extra == \"format-nongpl\""}
idna = {version = "*", optional = true, markers = "extra == \"format-nongpl\""}
isoduration = {version = "*", optional = true, markers = "extra == \"format-nongpl\""}
jsonpointer = {version = ">1.13", optional = true, markers = "extra == \"format-nongpl\""}
jsonschema-specifications = ">=2023.3.6"
referencing = ">=0.28.4"
rfc3339-validator = {version = "*", optional = true, markers = "extra == \"format-nongpl\""}
rfc3986-validator = {version = ">0.1.0", optional = true, markers = "extra == \"format-nongpl\""}
rfc3987-syntax = {version = ">=1.1.0", optional = true, markers = "extra == \"format-nongpl\""}
rpds-py = ">=0.25.0"
uri-template = {version = "*", optional = true, markers = "extra == \"format-nongpl\""}
webcolors = {version = ">=24.6.0", optional = true, markers = "extra == \"format-nongpl\""}

[package.extras]
format = ["fqdn", "idna", "isoduration", "jsonpointer (>1.13)", "rfc3339-validator", "rfc3987", "uri-template", "webcolors (>=1.11)"]
format-nongpl = ["fqdn", "idna", "isoduration", "jsonpointer (>1.13)", "rfc3339-validator", "rfc3986-validator (>0.1.0)", "rfc3987-syntax (>=1.1.0)", "uri-template", "webcolors (>=24.6.0)"]

[[package]]
name = "jsonschema-specifications"
version = "2025.9.1"
description = "The JSON Schema meta-schemas and vocabularies, exposed as a Registry"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "jsonschema_specifications-2025.9.1-py3-none-any.whl", hash = "sha256:98802fee3a11ee76ecaca44429fda8a41bff98b00a0f2838151b113f210cc6fe"},
    {file = "jsonschema_specifications-2025.9.1.tar.gz", hash = "sha256:b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d"},
]

[package.dependencies]
referencing = ">=0.31.0"

[[package]]
name = "jupyter"
version = "1.1.1"
description = "Jupyter metapackage. Install all the Jupyter components in one go."
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "jupyter-1.1.1-py2.py3-none-any.whl", hash = "sha256:7a59533c22af65439b24bbe60373a4e95af8f16ac65a6c00820ad378e3f7cc83"},
    {file = "jupyter-1.1.1.tar.gz", hash = "sha256:d55467bceabdea49d7e3624af7e33d59c37fff53ed3a350e1ac957bed731de7a"},
]

[package.dependencies]
ipykernel = "*"
ipywidgets = "*"
jupyter-console = "*"
jupyterlab = "*"
nbconvert = "*"
notebook = "*"

[[package]]
name = "jupyter-client"
version = "8.9.1"
description = "Jupyter protocol implementation and client libraries"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jupyter_client-8.9.1-py3-none-any.whl", hash = "sha256:0b7a295bc46e8751e9adae84781f726c851c1d911bd793edc4a3bde942e3da81"},
    {file = "jupyter_client-8.9.1.tar.gz", hash = "sha256:a58f730dd9e728ba16ba1d62ebccf7ffe1ebbdbce4e95cfae941b7321ae1f4fa"},
]

[package.dependencies]
jupyter-core = ">=5.1"
python-dateutil = ">=2.8.2"
pyzmq = ">=25.0"
tornado = ">=6.4.1"
traitlets = ">=5.3"
typing-extensions = ">=4.13.0"

[package.extras]
docs = ["ipykernel", "myst-parser", "pydata-sphinx-theme", "sphinx (>=4)", "sphinx-autodoc-typehints", "sphinxcontrib-github-alt", "sphinxcontrib-spelling"]
orjson = ["orjson"]
test = ["anyio", "coverage", "ipykernel (>=6.14)", "msgpack", "mypy ; platform_python_implementation != \"PyPy\"", "paramiko ; sys_platform == \"win32\"", "pre-commit", "pytest", "pytest-cov", "pytest-jupyter[client] (>=0.6.2)", "pytest-timeout"]

[[package]]
name = "jupyter-console"
version = "6.6.3"
description = "Jupyter terminal console"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "jupyter_console-6.6.3-py3-none-any.whl", hash = "sha256:309d33409fcc92ffdad25f0bcdf9a4a9daa61b6f341177570fdac03de5352485"},
    {file = "jupyter_console-6.6.3.tar.gz", hash = "sha256:566a4bf31c87adbfadf22cdf846e3069b59a71ed5da71d6ba4d8aaad14a53539"},
]

[package.dependencies]
ipykernel = ">=6.14"
ipython = "*"
jupyter-client = ">=7.0.0"
jupyter-core = ">=4.12,<5.0.dev0 || >=5.1.dev0"
prompt-toolkit = ">=3.0.30"
pygments = "*"
pyzmq = ">=17"
traitlets = ">=5.4"

[package.extras]
test = ["flaky", "pexpect", "pytest"]

[[package]]
name = "jupyter-core"
version = "5.9.1"
description = "Jupyter core package. A base package on which Jupyter projects rely."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jupyter_core-5.9.1-py3-none-any.whl", hash = "sha256:ebf87fdc6073d142e114c72c9e29a9d7ca03fad818c5d300ce2adc1fb0743407"},
    {file = "jupyter_core-5.9.1.tar.gz", hash = "sha256:4d09aaff303b9566c3ce657f580bd089ff5c91f5f89cf7d8846c3cdf465b5508"},
]

[package.dependencies]
platformdirs = ">=2.5"
traitlets = ">=5.3"

[package.extras]
docs = ["intersphinx-registry", "myst-parser", "pydata-sphinx-theme", "sphinx-autodoc-typehints", "sphinxcontrib-spelling", "traitlets"]
test = ["ipykernel", "pre-commit", "pytest (<9)", "pytest-cov", "pytest-timeout"]

[[package]]
name = "jupyter-events"
version = "0.12.1"
description = "Jupyter Event System library"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "jupyter_events-0.12.1-py3-none-any.whl", hash = "sha256:c366585253f537a627da52fa7ca7410c5b5301fe893f511e7b077c2d93ec8bcf"},
    {file = "jupyter_events-0.12.1.tar.gz", hash = "sha256:faff25f77218335752f35f23c5fe6e4a392a7bd99a5939ccb9b8fbf594636cf3"},
]

[package.dependencies]
jsonschema = {version = ">=4.18.0", extras = ["format-nongpl"]}
packaging = "*"
python-json-logger = ">=2.0.4"
pyyaml = ">=5.3"
referencing = "*"
rfc3339-validator = "*"
rfc3986-validator = ">=0.1.1"
traitlets = ">=5.3"

[package.extras]
cli = ["click", "rich"]
docs = ["jupyterlite-sphinx", "myst-parser", "pydata-sphinx-theme (>=0.16)", "sphinx (>=8)", "sphinxcontrib-spelling"]
test = ["click", "pre-commit", "pytest (>=7.0)", "pytest-asyncio (>=0.19.0)", "pytest-console-scripts", "rich"]

[[package]]
name = "jupyter-lsp"
version = "2.3.1"
description = "Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "jupyter_lsp-2.3.1-py3-none-any.whl", hash = "sha256:71b954d834e85ff3096400554f2eefaf7fe37053036f9a782b0f7c5e42dadb81"},
    {file = "jupyter_lsp-2.3.1.tar.gz", hash = "sha256:fdf8a4aa7d85813976d6e29e95e6a2c8f752701f926f2715305249a3829805a6"},
]

[package.dependencies]
jupyter_server = ">=1.1.2"

[[package]]
name = "jupyter-server"
version = "2.20.0"
description = "The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "jupyter_server-2.20.0-py3-none-any.whl", hash = "sha256:c3b67c93c471e947c18b5026f04f21614218adb706df8f48227d3ee8e0a7cdcc"},
    {file = "jupyter_server-2.20.0.tar.gz", hash = "sha256:b5778ba337d8015a3dc2b80803ecdd5ac18d3797fddf61a50ea5fb472b4ebe14"},
]

[package.dependencies]
anyio = ">=3.1.0"
argon2-cffi = ">=21.1"
jinja2 = ">=3.0.3"
jupyter-client = ">=7.4.4"
jupyter-core = ">=4.12,<5.0.dev0 || >=5.1.dev0"
jupyter-events = ">=0.11.0"
jupyter-server-terminals = ">=0.4.4"
nbconvert = ">=6.4.4"
nbformat = ">=5.3.0"
overrides = {version = ">=5.0", markers = "python_version < \"3.12\""}
packaging = ">=22.0"
prometheus-client = ">=0.9"
pywinpty = {version = ">=2.0.1,<3.0.4 || >3.0.4", markers = "os_name == \"nt\""}
pyzmq = ">=24"
send2trash = ">=1.8.2"
terminado = ">=0.8.3"
tornado = ">=6.2.0"
traitlets = ">=5.6.0"
websocket-client = ">=1.7"

[package.extras]
docs = ["ipykernel", "jinja2", "jupyter-client", "myst-parser", "nbformat", "prometheus-client", "pydata-sphinx-theme", "send2trash", "sphinx (<9.0)", "sphinx-autodoc-typehints", "sphinxcontrib-github-alt", "sphinxcontrib-openapi (>=0.8.0)", "sphinxcontrib-spelling", "sphinxemoji", "tornado", "typing-extensions"]
test = ["flaky", "ipykernel", "pre-commit", "pytest (>=7.0,<10)", "pytest-console-scripts", "pytest-jupyter[server] (>=0.7)", "pytest-timeout", "requests"]

[[package]]
name = "jupyter-server-terminals"
version = "0.5.4"
description = "A Jupyter Server Extension Providing Terminals."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "jupyter_server_terminals-0.5.4-py3-none-any.whl", hash = "sha256:55be353fc74a80bc7f3b20e6be50a55a61cd525626f578dcb66a5708e2007d14"},
    {file = "jupyter_server_terminals-0.5.4.tar.gz", hash = "sha256:bbda128ed41d0be9020349f9f1f2a4ab9952a73ed5f5ac9f1419794761fb87f5"},
]

[package.dependencies]
pywinpty = {version = ">=2.0.3", markers = "os_name == \"nt\""}
terminado = ">=0.8.3"

[package.extras]
docs = ["jinja2", "jupyter-server", "mistune (<4.0)", "myst-parser", "nbformat", "packaging", "pydata-sphinx-theme", "sphinxcontrib-github-alt", "sphinxcontrib-openapi", "sphinxcontrib-spelling", "sphinxemoji", "tornado"]
test = ["jupyter-server (>=2.0.0)", "pytest (>=7.0)", "pytest-jupyter[server] (>=0.5.3)", "pytest-timeout"]

[[package]]
name = "jupyterlab"
version = "4.5.9"
description = "JupyterLab computational environment"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "jupyterlab-4.5.9-py3-none-any.whl", hash = "sha256:5ff0f908e8ac0afbed32b106fdef360f101c0a6654d1bf4a81e98a293ae1b336"},
    {file = "jupyterlab-4.5.9.tar.gz", hash = "sha256:dd79a073fecae7a39066ea99e4627ed6c76269ac926e95a810e1e1df6358d865"},
]

[package.dependencies]
async-lru = ">=1.0.0"
httpx = ">=0.25.0,<1"
ipykernel = ">=6.5.0,<6.30.0 || >6.30.0"
jinja2 = ">=3.0.3"
jupyter-core = "*"
jupyter-lsp = ">=2.0.0"
jupyter-server = ">=2.4.0,<3"
jupyterlab-server = ">=2.28.0,<3"
notebook-shim = ">=0.2"
packaging = ">=23.2"
setuptools = ">=41.1.0"
tomli = {version = ">=1.2.2", markers = "python_version < \"3.11\""}
tornado = ">=6.2.0"
traitlets = "*"

[package.extras]
dev = ["build", "bump2version", "coverage", "hatch", "pre-commit", "pytest-cov", "ruff (==0.11.12)"]
docs = ["jsx-lexer", "myst-parser", "pydata-sphinx-theme (>=0.13.0)", "pytest", "pytest-check-links", "pytest-jupyter", "sphinx (>=1.8,<8.2.0)", "sphinx-copybutton"]
docs-screenshots = ["altair (==6.0.0)", "ipython (==8.16.1)", "ipywidgets (==8.1.5)", "jupyterlab-geojson (==3.4.0)", "jupyterlab-language-pack-zh-cn (==4.3.post1)", "matplotlib (==3.10.0)", "nbconvert (>=7.0.0)", "pandas (==2.2.3)", "scipy (==1.15.1)"]
test = ["coverage", "pytest (>=7.0)", "pytest-check-links (>=0.7)", "pytest-console-scripts", "pytest-cov", "pytest-jupyter (>=0.5.3)", "pytest-timeout", "pytest-tornasync", "requests", "requests-cache", "virtualenv"]
upgrade-extension = ["copier (>=9,<10)", "jinja2-time (<0.3)", "pydantic (<3.0)", "pyyaml-include (<3.0)", "tomli-w (<2.0)"]

[[package]]
name = "jupyterlab-pygments"
version = "0.3.0"
description = "Pygments theme using JupyterLab CSS variables"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "jupyterlab_pygments-0.3.0-py3-none-any.whl", hash = "sha256:841a89020971da1d8693f1a99997aefc5dc424bb1b251fd6322462a1b8842780"},
    {file = "jupyterlab_pygments-0.3.0.tar.gz", hash = "sha256:721aca4d9029252b11cfa9d185e5b5af4d54772bb8072f9b7036f4170054d35d"},
]

[[package]]
name = "jupyterlab-server"
version = "2.28.0"
description = "A set of server components for JupyterLab and JupyterLab like applications."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "jupyterlab_server-2.28.0-py3-none-any.whl", hash = "sha256:e4355b148fdcf34d312bbbc80f22467d6d20460e8b8736bf235577dd18506968"},
    {file = "jupyterlab_server-2.28.0.tar.gz", hash = "sha256:35baa81898b15f93573e2deca50d11ac0ae407ebb688299d3a5213265033712c"},
]

[package.dependencies]
babel = ">=2.10"
jinja2 = ">=3.0.3"
json5 = ">=0.9.0"
jsonschema = ">=4.18.0"
jupyter-server = ">=1.21,<3"
packaging = ">=21.3"
requests = ">=2.31"

[package.extras]
docs = ["autodoc-traits", "jinja2 (<3.2.0)", "mistune (<4)", "myst-parser", "pydata-sphinx-theme", "sphinx", "sphinx-copybutton", "sphinxcontrib-openapi (>0.8)"]
openapi = ["openapi-core (>=0.18.0,<0.19.0)", "ruamel-yaml"]
test = ["hatch", "ipykernel", "openapi-core (>=0.18.0,<0.19.0)", "openapi-spec-validator (>=0.6.0,<0.8.0)", "pytest (>=7.0,<8)", "pytest-console-scripts", "pytest-cov", "pytest-jupyter[server] (>=0.6.2)", "pytest-timeout", "requests-mock", "ruamel-yaml", "sphinxcontrib-spelling", "strict-rfc3339", "werkzeug"]

[[package]]
name = "jupyterlab-widgets"
version = "3.0.16"
description = "Jupyter interactive widgets for JupyterLab"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "jupyterlab_widgets-3.0.16-py3-none-any.whl", hash = "sha256:45fa36d9c6422cf2559198e4db481aa243c7a32d9926b500781c830c80f7ecf8"},
    {file = "jupyterlab_widgets-3.0.16.tar.gz", hash = "sha256:423da05071d55cf27a9e602216d35a3a65a3e41cdf9c5d3b643b814ce38c19e0"},
]

[[package]]
name = "lark"
version = "1.3.1"
description = "a modern parsing library"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "lark-1.3.1-py3-none-any.whl", hash = "sha256:c629b661023a014c37da873b4ff58a817398d12635d3bbb2c5a03be7fe5d1e12"},
    {file = "lark-1.3.1.tar.gz", hash = "sha256:b426a7a6d6d53189d318f2b6236ab5d6429eaf09259f1ca33eb716eed10d2905"},
]

[package.extras]
atomic-cache = ["atomicwrites"]
interegular = ["interegular (>=0.3.1,<0.4.0)"]
nearley = ["js2py"]
regex = ["regex"]

[[package]]
name = "librt"
version = "0.11.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.11.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:6e94ebfcfa2d5e9926d6c3b9aa4617ffc42a845b4321fb84021b872358c82a0f"},
    {file = "librt-0.11.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:ae627397a2f351560440d872d6f7c8dbb4072e57868e7b2fc5b8b430fe489d45"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:dc329359321b67d24efdf4bc69012b0597001649544db662c001db5a0184794c"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:7e82e642ab0f7608ce2fe53d76ca2280a9ee33a1b06556142c7c6fe80a86fc33"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:88145c15c67731d54283d135b03244028c750cc9edc334a96a4f5950ebdb2884"},
    {file = "librt-0.11.0-cp310-cp310-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9d36a51b3d93320b686588e27123f4995804dbf1bce81df78c02fc3c6eea9280"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d00f3ac06a2a8b246327f11e186a53a100a4d5c7ed52346367e5ec751d51586c"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:461bbceede621f1ffb8839755f8663e886087ee7af16294cab7fb4d782c62eeb"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0cad8a4d6a8ff03c9b76f9414caccd78e7cfbc8a2e12fa334d8e1d9932753783"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f37aa505b3cf60701562eddb32df74b12a9e380c207fd8b06dd157a943ac7ea0"},
    {file = "librt-0.11.0-cp310-cp310-win32.whl", hash = "sha256:94663a21534637f0e787ec2a2a756022df6e5b7b2335a5cdd7d8e33d68a2af89"},
    {file = "librt-0.11.0-cp310-cp310-win_amd64.whl", hash = "sha256:dec7db73758c2b54953fd8b7fe348c45188fe26b39ee18446196edd08453a5d4"},
    {file = "librt-0.11.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:93d95bd45b7d58343d8b90d904450a545144eec19a002511163426f8ab1fae29"},
    {file = "librt-0.11.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ee278c769a713638cdacd4c0436d72156e75df3ebc0166ab2b9dc43acc386c9"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f230cb1cbc9faaa616f9a678f530ebcf186e414b6bcbd88b960e4ba1b92428d5"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:5d63c855d86938d9de93e265c9bd8c705b51ec494de5738340ee93767a686e4b"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:993f028be9e96a08d31df3479ac80d99be374d17f3b78e4796b3fd3c913d4e89"},
    {file = "librt-0.11.0-cp311-cp311-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:258d73a0aa66a055e65b2e4d1b8cdb23b9d132c5bb915d9547d804fcaed116cc"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0827efe7854718f04aaddf6496e96960a956e676fe1d0f04eb41511fd8ad06d5"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:7753e57d6e12d019c0d8786f1c09c709f4c3fcc57c3887b24e36e6c06ec938b7"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:11bd19822431cc21af9f27374e7ae2e58103c7d98bda823536a6c47f6bb2bb3d"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:22bdf239b219d3993761a148ffa134b19e52e9989c84f845d5d7b71d70a17412"},
    {file = "librt-0.11.0-cp311-cp311-win32.whl", hash = "sha256:46c60b61e308eb535fbd6fa622b1ee1bb2815691c1ad9c98bf7b84952ec3bc8d"},
    {file = "librt-0.11.0-cp311-cp311-win_amd64.whl", hash = "sha256:902e546ff044f579ff1c953ff5fce97b636fe9e3943996b2177710c6ef076f73"},
    {file = "librt-0.11.0-cp311-cp311-win_arm64.whl", hash = "sha256:65ac3bc20f78aa0ee5ae84baa68917f89fef4af63e941084dd019a0d0e749f0c"},
    {file = "librt-0.11.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b87504f1690a23b9a2cca841191a04f83895d4fc2dd04df91d82b1a04ca2ad46"},
    {file = "librt-0.11.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:40071fc5fe0ce8daa6de616702314a01e1250711682b0523d6ab8d4525910cb3"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:137e79445c896a0ea7b265f52d23954e05b64222ee1af69e2cb34219067cbb67"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:cca6644054e78746d8d4ef238681f9c34ff8b584fe6b988ecebb8db3b15e622a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5b0eea49f5562861ee8d757a32ef7d559c1d35be2aaaa1ec28941d74c9ffc8a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0d1029d7e1ae1a7e647ed6fb5df8c4ce2dffefb7a9f5fd1376a4554d96dac09f"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:bc3ce6b33c5828d9e80592011a5c584cb2ce86edbc4088405f70da47dc1d1b3b"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:936c5995f3514a42111f20099397d8177c79b4d7e70961e396c6f5a0a3566766"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:9bc0ca6ad9381cbe8e4aa6e5726e4c80c78115a6e9723c599ed1d73e092bc49d"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:070aa8c26c0a74774317a72df8851facc7f0f012a5b406557ac56992d92e1ec8"},
    {file = "librt-0.11.0-cp312-cp312-win32.whl", hash = "sha256:6bf14feb84b05ae945277395451998c89c54d0def4070eb5c08de544930b245a"},
    {file = "librt-0.11.0-cp312-cp312-win_amd64.whl", hash = "sha256:75672f0bc524ede266287d532d7923dbce94c7514ad07627bac3d0c6d92cc4d9"},
    {file = "librt-0.11.0-cp312-cp312-win_arm64.whl", hash = "sha256:2f10cf143e4a9bb0f4f5af568a00df94a2d69ef41c2579584454bb0fe5cc642c"},
    {file = "librt-0.11.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:78dc31f7fdfe9c9d0eb0e8f42d139db230e826415bbcabd9f0e9faaaee909894"},
    {file = "librt-0.11.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:fa475675db22290c3158e1d42326d0f5a65f04f44a0e68c3630a25b53560fb9c"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:621db29691044bdeda22e789e482e1b0f3a985d90e3426c9c6d17606416205ea"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:a9010e2ed5b3a9e158c5fd966b3ab7e834bb3d3aacc8f66c91dd4b57a3799230"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7c39513d8b7477a2e1ed8c43fc21c524e8d5a0f8d4e8b7b074dbdbe7820a08e2"},
    {file = "librt-0.11.0-cp313-cp313-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7aef3cf1d5af86e770ab04bfd993dfc4ae8b8c17f66fb77dd4a7d50de7bbb1a3"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:557183ddc36babe46b27dd60facbd5adb4492181a5be887587d57cda6e092f21"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:83d3e1f72bd42f6c5c0b7daec530c3f829bd02db42c70b8ddf0c2d90a2459930"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:4ce1f21fbe589bc1afd7872dece84fb0e1144f794a288e58a10d2c54a55c43be"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b09f7044ea2b64c9da42fd3d335666518cfd1c6e8a182c95da73d0214b41e"},
    {file = "librt-0.11.0-cp313-cp313-win32.whl", hash = "sha256:78fddc31cd4d3caa897ad5d31f856b1faadc9474021ad6cb182b9018793e254e"},
    {file = "librt-0.11.0-cp313-cp313-win_amd64.whl", hash = "sha256:8ca8aa88751a775870b764e93bad5135385f563cb8dcee399abf034ea4d3cb47"},
    {file = "librt-0.11.0-cp313-cp313-win_arm64.whl", hash = "sha256:96f044bb325fd9cf1a723015638c219e9143f0dfbc0ca54c565df2b7fc748b44"},
    {file = "librt-0.11.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:4a017a95e5837dc15a8c5661d60e05daa96b90908b1aa6b7acdf443cd25c8ebd"},
    {file = "librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:b1ecbd9819deccc39b7542bf4d2a740d8a620694d39989e58661d3763458f8d4"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7da327dacd7be8f8ec36547373550744a3cc0e536d54665cd83f8bcd961200e8"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:0dc56b1f8d06e60db362cc3fdae206681817f86ce4725d34511473487f12a34b"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:05fb8fb2ab90e21c8d12ea240d744ad514da9baf381ebfa70d91d20d21713175"},
    {file = "librt-0.11.0-cp314-cp314-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cae74872be221df4374d10fec61f93ed1513b9546ea84f2c0bf73ab3e9bd0b03"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:32bcc918c0148eb7e3d57385125bac7e5f9e4359d05f07448b09f6f778c2f31c"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f9743fc99135d5f78d2454435615f6dec0473ca507c26ce9d92b10b562a280d3"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:5ba067f4aadae8fda802d91d2124c90c42195ff32d9161d3549e6d05cfe26f96"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:de3bf945454d032f9e390b85c4072e0a0570bf825421c8be0e71209fa65e1abe"},
    {file = "librt-0.11.0-cp314-cp314-win32.whl", hash = "sha256:d2277a05f6dcb9fd13db9566aac4fabd68c3ea1ea46ee5567d4eef8efa495a2f"},
    {file = "librt-0.11.0-cp314-cp314-win_amd64.whl", hash = "sha256:ab73e8db5e3f564d812c1f5c3a175930a5f9bc96ccb5e3b22a34d7858b401cf7"},
    {file = "librt-0.11.0-cp314-cp314-win_arm64.whl", hash = "sha256:aea3caa317752e3a466fa8af45d91ee0ea8c7fdd96e42b0a8dd9b76a7931eba1"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:d1b36540d7aaf9b9101b3a6f376c8d8e9f7a9aec93ed05918f2c69d493ffef72"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:efbb343ab2ce3540f4ecbe6315d677ed70f37cd9a72b1e58066c918ca83acbaa"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:aa0dd688aab3f7914d3e6e5e3554978e0383312fb8e771d84be008a35b9ee548"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:f5fb36b8c6c63fdcbb1d526d94c0d1331610d43f4118cc1beb4efef4f3faacb2"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4a9a237d13addb93715b6fee74023d5ee3469b53fce527626c0e088aa585805f"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5ddd17bd87b2c56ddd60e546a7984a2e64c4e8eab92fb4cf3830a48ad5469d51"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:bd43992b4473d42f12ff9e68326079f0696d9d4e6000e8f39a0238d482ba6ee2"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:f8e3e8056dd674e279741485e2e512d6e9a751c7455809d0114e6ebf8d781085"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:c1f708d8ae9c56cf38a903c44297243d2ec83fd82b396b977e0144a3e76217e3"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0add982e0e7b9fc14cf4b33789d5f13f66581889b88c2f58099f6ce8f92617bd"},
    {file = "librt-0.11.0-cp314-cp314t-win32.whl", hash = "sha256:2b481d846ac894c4e8403c5fd0e87c5d11d6499e404b474602508a224ff531c8"},
    {file = "librt-0.11.0-cp314-cp314t-win_amd64.whl", hash = "sha256:28edb433edde181112a908c78907af28f964eabc15f4dd16c9d66c834302677c"},
    {file = "librt-0.11.0-cp314-cp314t-win_arm64.whl", hash = "sha256:dee008f20b542e3cd162ba338a7f9ec0f6d23d395f66fe8aeeec3c9d067ea253"},
    {file = "librt-0.11.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6bd72d903911d995ab666dbd1871f8b1e80925a699af8063fbf50053329fb05f"},
    {file = "librt-0.11.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0ef69ac715f3cd8e5cd252cb2aebfa72c015492aacc339d5d7bf8fef3c62c677"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:624a40c4a4ad7773315c287276cd024509b2c66ff5904f504bfc08d2c70293ab"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:41dc19fe150b69716c8ece4f76773a9e8813fe3e35e032a58b4d46423fb8d7c0"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4e8bd98ea9c47ae90b319a087ab28dac493f1ffbc1ecd1f28fcdbf3b7e1108d1"},
    {file = "librt-0.11.0-cp39-cp39-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:84308fc49423ce6475d1c5d1985cd69a8ca9f0325fc7d5f81bb690a3f3625d4e"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:ff0fbaf5f44a21beeb0110f2ab64f45135a9536a834b79c0d1ef018f2786bbfa"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9c028a9442a18e266955d364ce42259136e79a7ba14d773e0d778d5f70cd56f1"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:9f1692105a02bcf853f355032a5fdc5494358ef83d8fd22d16de375c85cec3f5"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7a80a71e1fda83cc752a9141e87aae7fef279538597564d670e9ce513f286192"},
    {file = "librt-0.11.0-cp39-cp39-win32.whl", hash = "sha256:140695816ddf3c86eb972981a26f35efd871c44b0c3aed44c8cd01749386617f"},
    {file = "librt-0.11.0-cp39-cp39-win_amd64.whl", hash = "sha256:92f7ff819c197fc30473190a12c2856f325ac90aabfccbeb2072d28cc2e234e3"},
    {file = "librt-0.11.0.tar.gz", hash = "sha256:075dc3ef4458a278e0195cbf6ac9d38808d9b906c5a6c7f7f79c3888276a3fb1"},
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.8"
groups = ["docs", "lint"]
markers = "python_version == \"3.10\""
files = [
    {file = "markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb"},
    {file = "markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1"},
]

[package.dependencies]
mdurl = ">=0.1,<1.0"

[package.extras]
benchmarking = ["psutil", "pytest", "pytest-benchmark"]
code-style = ["pre-commit (>=3.0,<4.0)"]
compare = ["commonmark (>=0.9,<1.0)", "markdown (>=3.4,<4.0)", "mistletoe (>=1.0,<2.0)", "mistune (>=2.0,<3.0)", "panflute (>=2.3,<3.0)"]
linkify = ["linkify-it-py (>=1,<3)"]
plugins = ["mdit-py-plugins"]
profiling = ["gprof2dot"]
rtd = ["jupyter_sphinx", "mdit-py-plugins", "myst-parser", "pyyaml", "sphinx", "sphinx-copybutton", "sphinx-design", "sphinx_book_theme"]
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions"]

[[package]]
name = "markdown-it-py"
version = "4.2.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.10"
groups = ["docs", "lint"]
markers = "python_version >= \"3.11\""
files = [
    {file = "markdown_it_py-4.2.0-py3-none-any.whl", hash = "sha256:9f7ebbcd14fe59494226453aed97c1070d83f8d24b6fc3a3bcf9a38092641c4a"},
    {file = "markdown_it_py-4.2.0.tar.gz", hash = "sha256:04a21681d6fbb623de53f6f364d352309d4094dd4194040a10fd51833e418d49"},
]

[package.dependencies]
mdurl = ">=0.1,<1.0"

[package.extras]
benchmarking = ["psutil", "pytest", "pytest-benchmark"]
compare = ["commonmark (>=0.9,<1.0)", "markdown (>=3.4,<4.0)", "markdown-it-pyrs", "mistletoe (>=1.0,<2.0)", "mistune (>=3.0,<4.0)", "panflute (>=2.3,<3.0)"]
linkify = ["linkify-it-py (>=1,<3)"]
plugins = ["mdit-py-plugins (>=0.5.0)"]
profiling = ["gprof2dot"]
rtd = ["ipykernel", "jupyter_sphinx", "mdit-py-plugins (>=0.5.0)", "myst-parser", "pyyaml", "sphinx", "sphinx-book-theme (>=1.0,<2.0)", "sphinx-copybutton", "sphinx-design"]
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions", "pytest-timeout", "requests"]

[[package]]
name = "markupsafe"
version = "3.0.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.9"
groups = ["dev", "docs"]
files = [
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559"},
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1"},
    {file = "markupsafe-3.0.3-cp310-cp310-win32.whl", hash = "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a"},
    {file = "markupsafe-3.0.3-cp311-cp311-win32.whl", hash = "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b"},
    {file = "markupsafe-3.0.3-cp312-cp312-win32.whl", hash = "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12"},
    {file = "markupsafe-3.0.3-cp313-cp313-win32.whl", hash = "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win32.whl", hash = "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe"},
    {file = "markupsafe-3.0.3-cp314-cp314-win32.whl", hash = "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win32.whl", hash = "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:15d939a21d546304880945ca1ecb8a039db6b4dc49b2c5a400387cdae6a62e26"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:f71a396b3bf33ecaa1626c255855702aca4d3d9fea5e051b41ac59a9c1c41edc"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f4b68347f8c5eab4a13419215bdfd7f8c9b19f2b25520968adfad23eb0ce60c"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e8fc20152abba6b83724d7ff268c249fa196d8259ff481f3b1476383f8f24e42"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:949b8d66bc381ee8b007cd945914c721d9aba8e27f71959d750a46f7c282b20b"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:3537e01efc9d4dccdf77221fb1cb3b8e1a38d5428920e0657ce299b20324d758"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:591ae9f2a647529ca990bc681daebdd52c8791ff06c2bfa05b65163e28102ef2"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a320721ab5a1aba0a233739394eb907f8c8da5c98c9181d1161e77a0c8e36f2d"},
    {file = "markupsafe-3.0.3-cp39-cp39-win32.whl", hash = "sha256:df2449253ef108a379b8b5d6b43f4b1a8e81a061d6537becd5582fba5f9196d7"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:7c3fb7d25180895632e5d3148dbdc29ea38ccb7fd210aa27acbd1201a1902c6e"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_arm64.whl", hash = "sha256:38664109c14ffc9e7437e86b4dceb442b0096dfe3541d7864d9cbe1da4cf36c8"},
    {file = "markupsafe-3.0.3.tar.gz", hash = "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698"},
]

[[package]]
name = "matplotlib-inline"
version = "0.2.2"
description = "Inline Matplotlib backend for Jupyter"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "matplotlib_inline-0.2.2-py3-none-any.whl", hash = "sha256:3c821cf1c209f59fb2d2d64abbf5b23b67bcb2210d663f9918dd851c6da1fcf6"},
    {file = "matplotlib_inline-0.2.2.tar.gz", hash = "sha256:72f3fe8fce36b70d4a5b612f899090cd0401deddc4ea90e1572b9f4bfb058c79"},
]

[package.dependencies]
traitlets = "*"

[package.extras]
test = ["flake8", "matplotlib", "nbdime", "nbval", "notebook", "pytest"]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mdit-py-plugins"
version = "0.6.1"
description = "Collection of plugins for markdown-it-py"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
files = [
    {file = "mdit_py_plugins-0.6.1-py3-none-any.whl", hash = "sha256:214c82fb2ac524472ab6a5bcab1de80f73b50443e187f401bfd77efbc7c6481d"},
    {file = "mdit_py_plugins-0.6.1.tar.gz", hash = "sha256:a2bca0f039f39dbd35fb74ae1b5f998608c437463371f0ff7f49a19a17a114d0"},
]

[package.dependencies]
markdown-it-py = ">=2.0.0,<5.0.0"

[package.extras]
code-style = ["pre-commit"]
rtd = ["myst-parser", "sphinx-book-theme"]
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions", "pytest-timeout"]

[[package]]
name = "mdurl"
version = "0.1.2"
description = "Markdown URL utilities"
optional = false
python-versions = ">=3.7"
groups = ["docs", "lint"]
files = [
    {file = "mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8"},
    {file = "mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba"},
]

[[package]]
name = "mistune"
version = "3.2.1"
description = "A sane and fast Markdown parser with useful plugins and renderers"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "mistune-3.2.1-py3-none-any.whl", hash = "sha256:78cdb0ba5e938053ccf63651b352508d2efa9411dc8810bfb05f2dc5140c0048"},
    {file = "mistune-3.2.1.tar.gz", hash = "sha256:7c8e5501d38bac1582e067e46c8343f17d57ea1aaa735823f3aba1fd59c88a28"},
]

[package.dependencies]
typing-extensions = {version = "*", markers = "python_version < \"3.11\""}

[[package]]
name = "mypy"
version = "2.1.0"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "mypy-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:11a6beb180257a805961aea9ec591bbd0bd17f1e18d35b8456d57aee5bedfedc"},
    {file = "mypy-2.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8ef78c1d306bbf9a8a12f526c44902c9c28dffd6c52c52bf6a72641ce18d3849"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c209a90853081ff01d01ee895cafe10f7db1474e0d95beaeef0f6c1db9119bbd"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:47cebf61abde7c088a4e27718a8b13a81655686b2e9c251f5c0915a802248166"},
    {file = "mypy-2.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:d57a90ae5e872138a425ec328edbc9b235d1934c4377881a33ec05b341acc9a8"},
    {file = "mypy-2.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:aea7f7a8a55b459c34275fc468ada6ca7c173a5e43a68f5dbe588a563d8a06b8"},
    {file = "mypy-2.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:c989640253f0d76843e9c6c1bbf4bd48c5e85ada61bde4beb37cb3eca035685e"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a683016b16fe2f572dc04c72be7ee0504ac1605a265d0200f5cea695fb788f41"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a293c534adb55271fef24a26da04b855540a8c13cc07bc5917b9fd2c394f2ca"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7406f4d048e71e576f5356d317e5b0a9e666dfd966bd99f9d14ca06e1a341538"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0210d626fc8b31ccc90233754c7bc90e1f43205e85d96387f7db1285b55c398"},
    {file = "mypy-2.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3712c20deed54e814eaaa825603bada8ea1c390670a397c95b98405347acc563"},
    {file = "mypy-2.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fcaa0e479066e31f7cceb6a3bea39cb22b2ff51a6b2f24f193d19179ba17c389"},
    {file = "mypy-2.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:0b1a5260c95aa443083f9ed3592662941951bca3d4ca224a5dc517c38b7cf666"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:244358bf1c0da7722230bce60683d52e8e9fd030554926f15b747a84efb5b3af"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4ec7c57657493c7a75534df2751c8ae2cda383c16ecc55d2106c54476b1b16f6"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8161b6ff4392410023224f0969d17db93e1e154bc3e4ba62598e720723ae211"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bf03e12003084a67395184d3eb8cbd6a489dc3655b5664b28c210a9e2403ab0b"},
    {file = "mypy-2.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:20509760fd791c51579d573153407d226385ec1f8bcce55d730b354f3336bc22"},
    {file = "mypy-2.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:6753d0c1fdd6b1a23b9e4f283ce80b2153b724adcb2653b20b85a8a28ac6436b"},
    {file = "mypy-2.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:98ebb6589bb3b6d0c6f0c459d53ca55b8091fbc13d277c4041c885392e8195e8"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:35aac3bb114e03888f535d5eb51b8bafbb3266586b599da1940f9b1be3ec5bd5"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8de55a8c861f2a49331f807be98d90caeceeef520bde13d43a160207f8af613e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5fdf2941a07434af755837d9880f7d7d25f1dacb1af9dcd4b9b66f2220a3024e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e195b817c13f02352a9c124301f9f30f078405444679b6753c1b96b6eed37285"},
    {file = "mypy-2.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5431d42af987ebd92ba2f71d45c85ed41d8e6ca9f5fd209a69f68f707d2469e5"},
    {file = "mypy-2.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:767fe8c66dc3e01e19e1737d4c38ebefead16125e1b8e58ad421903b376f5c65"},
    {file = "mypy-2.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:ecfe70d43775ab99562ab128ce49854a362044c9f894961f68f898c23cb7429d"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:7354c5a7f69d9345c3d6e69921d57088eea3ddeeb6b20d34c1b3855b02c36ec2"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:49890d4f76ac9e06ec117f9e09f3174da70a620a0c300953d8595c926e80947f"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:761be68e023ef5d94678772396a8af1220030f80837a3afd8d0aef3b419666f4"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c90345fc182dc363b891350457ec69c35140858538f38b4540845afcc32b1aef"},
    {file = "mypy-2.1.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b84802e7b5a6daf1f5e15bc9fcd7ddae77be13981ffab037f1c67bb84d67d135"},
    {file = "mypy-2.1.0-cp314-cp314-win_amd64.whl", hash = "sha256:022c771234936ceac541ebaf836fe9e2abeb3f5e09aff21588fe543ff006fe21"},
    {file = "mypy-2.1.0-cp314-cp314-win_arm64.whl", hash = "sha256:498207db725cec88829a6a5c2fc771205fd043719ef98bc49aba8fb9fc4e6d57"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:7d5e5cad0efeba72b93cd17490cc0d69c5ac9ca132994fe3fb0314808aeeb83e"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ff715050c127d724fd260a2e666e7747fdd83511c0c47d449d98238970aef780"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:82208da9e09414d520e912d3e462d454854bed0810b71540bb016dcbca7308fd"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e79ebc1b904b84f0310dff7469655a9c36c7a68bddb37bdd42b67a332df61d08"},
    {file = "mypy-2.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e583edc957cfb0deb142079162ae826f58449b116c1d442f2d91c69d9fced081"},
    {file = "mypy-2.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b33b6cd332695bba180d55e717a79d3038e479a2c49cc5eb3d53603409b9a5d7"},
    {file = "mypy-2.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:4f910fe825376a7b66ef7ca8c98e5a149e8cd64c19ae71d84047a74ee060d4e6"},
    {file = "mypy-2.1.0-py3-none-any.whl", hash = "sha256:a663814603a5c563fb87a4f96fb473eeb30d1f5a4885afcf44f9db000a366289"},
    {file = "mypy-2.1.0.tar.gz", hash = "sha256:81e76ad12c2d804512e9b13240d1588316531bfba07558286078bfbce9613633"},
]

[package.dependencies]
ast-serialize = ">=0.3.0,<1.0.0"
librt = {version = ">=0.11.0", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=1.0.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = [
    {version = ">=4.6.0", markers = "python_version < \"3.15\""},
    {version = ">=4.14.0", markers = "python_version >= \"3.15\""},
]

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
reports = ["lxml"]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "myst-parser"
version = "4.0.1"
description = "An extended [CommonMark](https://spec.commonmark.org/) compliant parser,"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "myst_parser-4.0.1-py3-none-any.whl", hash = "sha256:9134e88959ec3b5780aedf8a99680ea242869d012e8821db3126d427edc9c95d"},
    {file = "myst_parser-4.0.1.tar.gz", hash = "sha256:5cfea715e4f3574138aecbf7d54132296bfd72bb614d31168f48c477a830a7c4"},
]

[package.dependencies]
docutils = ">=0.19,<0.22"
jinja2 = "*"
markdown-it-py = ">=3.0,<4.0"
mdit-py-plugins = ">=0.4.1,<1.0"
pyyaml = "*"
sphinx = ">=7,<9"

[package.extras]
code-style = ["pre-commit (>=4.0,<5.0)"]
linkify = ["linkify-it-py (>=2.0,<3.0)"]
rtd = ["ipython", "sphinx (>=7)", "sphinx-autodoc2 (>=0.5.0,<0.6.0)", "sphinx-book-theme (>=1.1,<2.0)", "sphinx-copybutton", "sphinx-design", "sphinx-pyscript", "sphinx-tippy (>=0.4.3)", "sphinx-togglebutton", "sphinxext-opengraph (>=0.9.0,<0.10.0)", "sphinxext-rediraffe (>=0.2.7,<0.3.0)"]
testing = ["beautifulsoup4", "coverage[toml]", "defusedxml", "pygments (<2.19)", "pytest (>=8,<9)", "pytest-cov", "pytest-param-files (>=0.6.0,<0.7.0)", "pytest-regressions", "sphinx-pytest"]
testing-docutils = ["pygments", "pytest (>=8,<9)", "pytest-param-files (>=0.6.0,<0.7.0)"]

[[package]]
name = "myst-parser"
version = "5.1.0"
description = "An extended [CommonMark](https://spec.commonmark.org/) compliant parser,"
optional = false
python-versions = ">=3.11"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "myst_parser-5.1.0-py3-none-any.whl", hash = "sha256:9c91c52b3cdb4d94a6506e4fab4e2f296c7623a0da0dcbe6de1565c3dad67a8a"},
    {file = "myst_parser-5.1.0.tar.gz", hash = "sha256:ab69322dc6719dcc7f296479dbb70181b66df6ed315064f92dbc85c0e1bf2f02"},
]

[package.dependencies]
docutils = ">=0.20,<0.23"
jinja2 = "*"
markdown-it-py = ">=4.2,<5.0"
mdit-py-plugins = ">=0.6.1,<1.0"
pyyaml = "*"
sphinx = ">=8,<10"

[package.extras]
code-style = ["pre-commit (>=4.0,<5.0)"]
linkify = ["linkify-it-py (>=2.0,<3.0)"]
rtd = ["ipython", "sphinx (>=8)", "sphinx-autodoc2 (>=0.5.0,<0.6.0)", "sphinx-book-theme (>=1.1,<2.0)", "sphinx-copybutton", "sphinx-design", "sphinx-pyscript", "sphinx-tippy (>=0.4.3)", "sphinx-togglebutton", "sphinxext-opengraph (>=0.13.0,<0.14.0)", "sphinxext-rediraffe (>=0.3.0,<0.4.0)"]
testing = ["beautifulsoup4", "coverage[toml]", "defusedxml", "pygments (<2.21)", "pytest (>=9,<10)", "pytest-cov", "pytest-param-files (>=0.6.0,<0.7.0)", "pytest-regressions", "sphinx-pytest (>=0.3.0,<0.4.0)"]
testing-docutils = ["pygments", "pytest (>=9,<10)", "pytest-param-files (>=0.6.0,<0.7.0)"]

[[package]]
name = "narwhals"
version = "2.22.1"
description = "Extremely lightweight compatibility layer between dataframe libraries"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "narwhals-2.22.1-py3-none-any.whl", hash = "sha256:60567d774edf77db53906f89d9fbd164e66e56d66d388e1e6990f17ac33cfb53"},
    {file = "narwhals-2.22.1.tar.gz", hash = "sha256:d62920805a0a43b7ff8b54b0c0d3142d796f8a9301836ada37e573d6a33cbcd9"},
]

[package.extras]
cudf = ["cudf-cu12 (>=24.10.0) ; sys_platform == \"linux\""]
dask = ["dask[dataframe] (>=2024.8)"]
duckdb = ["duckdb (>=1.1)"]
ibis = ["ibis-framework (>=6.0.0)", "packaging (>=21.3)", "pyarrow-hotfix (>=0.7)", "rich (>=12.4.4)"]
modin = ["modin (>=0.22.0)"]
pandas = ["pandas (>=1.3.4)"]
polars = ["polars (>=0.20.4)"]
pyarrow = ["pyarrow (>=13.0.0)"]
pyspark = ["pyspark (>=3.5.0)"]
pyspark-connect = ["pyspark[connect] (>=3.5.0)"]
sql = ["narwhals[duckdb]", "sqlparse (>=0.5.5)"]
sqlframe = ["sqlframe (>=3.22.0,!=3.39.3)"]

[[package]]
name = "nbclient"
version = "0.11.0"
description = "A client library for executing notebooks. Formerly nbconvert's ExecutePreprocessor."
optional = false
python-versions = ">=3.10.0"
groups = ["dev"]
files = [
    {file = "nbclient-0.11.0-py3-none-any.whl", hash = "sha256:ef7fa0d59d6e1d41103933d8a445a18d5de860ca6b613b87b8574accdb3c2895"},
    {file = "nbclient-0.11.0.tar.gz", hash = "sha256:04a134a5b087f2c5887f228aca155db50169b8cd9334dee6942c8e927e56081a"},
]

[package.dependencies]
jupyter-client = ">=7.0.0"
jupyter-core = ">=5.4.0"
nbformat = ">=5.2.0"
traitlets = ">=5.13"

[package.extras]
dev = ["pre-commit"]
docs = ["autodoc-traits", "flaky", "ipykernel (>=6.19.3)", "ipython", "ipywidgets", "mock", "moto", "myst-parser", "nbconvert (>=7.1.0)", "pytest (>=9.0.1,<10)", "pytest-asyncio (>=1.3.0)", "pytest-cov (>=4.0)", "sphinx (>=1.7)", "sphinx-book-theme", "sphinxcontrib-spelling", "testpath", "xmltodict"]
test = ["flaky", "ipykernel (>=6.19.3)", "ipython", "ipywidgets", "nbconvert (>=7.1.0)", "pytest (>=9.0.1,<10)", "pytest-asyncio (>=1.3.0)", "pytest-cov (>=4.0)", "testpath", "xmltodict"]

[[package]]
name = "nbconvert"
version = "7.17.1"
description = "Convert Jupyter Notebooks (.ipynb files) to other formats."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "nbconvert-7.17.1-py3-none-any.whl", hash = "sha256:aa85c087b435e7bf1ffd03319f658e285f2b89eccab33bc1ba7025495ab3e7c8"},
    {file = "nbconvert-7.17.1.tar.gz", hash = "sha256:34d0d0a7e73ce3cbab6c5aae8f4f468797280b01fd8bd2ca746da8569eddd7d2"},
]

[package.dependencies]
beautifulsoup4 = "*"
bleach = {version = "!=5.0.0", extras = ["css"]}
defusedxml = "*"
jinja2 = ">=3.0"
jupyter-core = ">=4.7"
jupyterlab-pygments = "*"
markupsafe = ">=2.0"
mistune = ">=2.0.3,<4"
nbclient = ">=0.5.0"
nbformat = ">=5.7"
packaging = "*"
pandocfilters = ">=1.4.1"
pygments = ">=2.4.1"
traitlets = ">=5.1"

[package.extras]
all = ["flaky", "intersphinx-registry", "ipykernel", "ipython", "ipywidgets (>=7.5)", "myst-parser", "nbsphinx (>=0.2.12)", "playwright", "pydata-sphinx-theme", "pyqtwebengine (>=5.15)", "pytest (>=7)", "sphinx (>=5.0.2)", "sphinxcontrib-spelling", "tornado (>=6.1)"]
docs = ["intersphinx-registry", "ipykernel", "ipython", "myst-parser", "nbsphinx (>=0.2.12)", "pydata-sphinx-theme", "sphinx (>=5.0.2)", "sphinxcontrib-spelling"]
qtpdf = ["pyqtwebengine (>=5.15)"]
qtpng = ["pyqtwebengine (>=5.15)"]
serve = ["tornado (>=6.1)"]
test = ["flaky", "ipykernel", "ipywidgets (>=7.5)", "pytest (>=7)"]
webpdf = ["playwright"]

[[package]]
name = "nbformat"
version = "5.10.4"
description = "The Jupyter Notebook format"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "nbformat-5.10.4-py3-none-any.whl", hash = "sha256:3b48d6c8fbca4b299bf3982ea7db1af21580e4fec269ad087b9e81588891200b"},
    {file = "nbformat-5.10.4.tar.gz", hash = "sha256:322168b14f937a5d11362988ecac2a4952d3d8e3a2cbeb2319584631226d5b3a"},
]

[package.dependencies]
fastjsonschema = ">=2.15"
jsonschema = ">=2.6"
jupyter-core = ">=4.12,<5.0.dev0 || >=5.1.dev0"
traitlets = ">=5.1"

[package.extras]
docs = ["myst-parser", "pydata-sphinx-theme", "sphinx", "sphinxcontrib-github-alt", "sphinxcontrib-spelling"]
test = ["pep440", "pre-commit", "pytest", "testpath"]

[[package]]
name = "nest-asyncio2"
version = "1.7.2"
description = "Patch asyncio to allow nested event loops"
optional = false
python-versions = ">=3.5"
groups = ["dev"]
files = [
    {file = "nest_asyncio2-1.7.2-py3-none-any.whl", hash = "sha256:f5dfa702f3f81f6a03857e9a19e2ba578c0946a4ad417b4c50a24d7ba641fe01"},
    {file = "nest_asyncio2-1.7.2.tar.gz", hash = "sha256:1921d70b92cc4612c374928d081552efb59b83d91b2b789d935c665fa01729a8"},
]

[[package]]
name = "ni-datamonikers-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI data moniker gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_datamonikers_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:77d078d810656b3e90152a065047c6203140e0998e8cbdf9d2dbb6e9f477840e"},
    {file = "ni_datamonikers_v1_proto-1.0.0.tar.gz", hash = "sha256:2e4cf30f9dee343af4a5f328fb785320d2eb30705abc15f0695057177afd5f00"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-data-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Data Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:dfc38d56fdd710a930fbc05383d43ab96f64aee545937f9ef605a3bb6f88cc31"},
    {file = "ni_measurements_data_v1_client-1.1.0.tar.gz", hash = "sha256:16b1ac8b82277e41719aa8b1aeae3f1040dba47e63651f83e30fe115cd036278"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-data-v1-proto = ">=1.1.0"

[[package]]
name = "ni-measurements-data-v1-proto"
version = "1.1.0"
description = "Protobuf data types and service stubs for NI data store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_data_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:06096cea733717b60281c92d0a1b44eac97194781507ba4fd9b3aa080a4450df"},
    {file = "ni_measurements_data_v1_proto-1.1.0.tar.gz", hash = "sha256:df1ca7ce3603dd5a0adc8795f0844da9a78ddc026f219bf596957cf3ed08da3d"},
]

[package.dependencies]
ni-datamonikers-v1-proto = ">=1.0.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"
ni-protobuf-types = ">=1.2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurements-metadata-v1-client"
version = "1.0.0"
description = "gRPC Client for NI Metadata Store Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_client-1.0.0-py3-none-any.whl", hash = "sha256:c697ce4e98105b810f4da844a598e86e359ff6c90ca7a832e1e23a70327551a7"},
    {file = "ni_measurements_metadata_v1_client-1.0.0.tar.gz", hash = "sha256:9f9a10810c4c6693239081abbc026414a18df3e3d04daa3cd59010b1eed07f51"},
]

[package.dependencies]
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurements-metadata-v1-proto = ">=1.0.0"

[[package]]
name = "ni-measurements-metadata-v1-proto"
version = "1.0.0"
description = "Protobuf data types and service stub for NI metadata store gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurements_metadata_v1_proto-1.0.0-py3-none-any.whl", hash = "sha256:8844806d6775ac65144100fcd03099aea0c17ed55de696683d0663166f45cee3"},
    {file = "ni_measurements_metadata_v1_proto-1.0.0.tar.gz", hash = "sha256:3283cf7f0c452812a311b2b9274b5ba1e549f994f6a978a125f1746b85746e6f"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.2.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_protobuf_types-1.2.0-py3-none-any.whl", hash = "sha256:461c4825571d0054fd5427664403c3d69fcd180c9c00868ac1911693dd9bf901"},
    {file = "ni_protobuf_types-1.2.0.tar.gz", hash = "sha256:e8226f8ef44b104ffb1b1f6e416511c416be4d91bf5c2633db7ab58294e037bb"},
]

[package.dependencies]
nitypes = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["lint"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "nitypes"
version = "1.1.0"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "nitypes-1.1.0-py3-none-any.whl", hash = "sha256:b43ac7027e1cceeca7ceffa58f31ffadd03feeb1788ca5cb8f9d105e73893b14"},
    {file = "nitypes-1.1.0.tar.gz", hash = "sha256:f273b5131ef0d5b848c37a0a63452626caf5c2938f7744c324f7991b76fa0b60"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "nodeenv"
version = "1.10.0"
description = "Node.js virtual environment builder"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["lint"]
files = [
    {file = "nodeenv-1.10.0-py2.py3-none-any.whl", hash = "sha256:5bb13e3eed2923615535339b3c620e76779af4cb4c6a90deccc9e36b274d3827"},
    {file = "nodeenv-1.10.0.tar.gz", hash = "sha256:996c191ad80897d076bdfba80a41994c2b47c68e224c542b48feba42ba00f8bb"},
]

[[package]]
name = "nodejs-wheel-binaries"
version = "24.16.0"
description = "unoffical Node.js package"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-macosx_13_0_arm64.whl", hash = "sha256:d9f8f677dcf30e37ac244f07869726abe043f01eb0f45722b1df31cc2af7093c"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-macosx_13_0_x86_64.whl", hash = "sha256:3d0370fe7120ce9697a4f60d40480d2bd8808d9f30131458d5afc0040d4e5a51"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-manylinux_2_28_aarch64.whl", hash = "sha256:85dc92bbb79c851569c5925dcc2a4c915a034efab375f99e4e7e6bbe9cca8342"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-manylinux_2_28_x86_64.whl", hash = "sha256:2f3036292811514ba847b3708492644764f88a833ac425c5f55007014308ddfd"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:db8a8a76ebd2b28ecbfc9ad464baa3707241b9e050a30e2efdf6f60c0f886502"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:f1a3d8f7b4491cbbd023ba3fc4e901fcca2d9fb80d57f24ba3890de8b1dbac03"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-win_amd64.whl", hash = "sha256:bb136be9944f0662dcf1120f45193a6b75b13fac378971a95cc42c9f879a81aa"},
    {file = "nodejs_wheel_binaries-24.16.0-py2.py3-none-win_arm64.whl", hash = "sha256:8308940b5edd0a50dc5267ea36ba21c9f668e83fe0d9f293937174d3a7e31c36"},
    {file = "nodejs_wheel_binaries-24.16.0.tar.gz", hash = "sha256:c973cb69dc5fd16e6f6dc6e579e2c3d5534e2a1f57619dddf5ba070efa7dde37"},
]

[[package]]
name = "notebook"
version = "7.5.7"
description = "Jupyter Notebook - A web-based notebook environment for interactive computing"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "notebook-7.5.7-py3-none-any.whl", hash = "sha256:1f95f79d117e47d20b5555b5c85a397d2cfecf136978aaab767cf0314b09165b"},
    {file = "notebook-7.5.7.tar.gz", hash = "sha256:d6d59288a25303b25e1dcb71e9b017ec3a785f7d92f38b9bc288ca1970d5b0a8"},
]

[package.dependencies]
jupyter-server = ">=2.4.0,<3"
jupyterlab = ">=4.5.8,<4.6"
jupyterlab-server = ">=2.28.0,<3"
notebook-shim = ">=0.2,<0.3"
tornado = ">=6.2.0"

[package.extras]
dev = ["hatch", "pre-commit"]
docs = ["myst-parser", "nbsphinx", "pydata-sphinx-theme", "sphinx (>=1.3.6)", "sphinxcontrib-github-alt", "sphinxcontrib-spelling"]
test = ["importlib-resources (>=5.0) ; python_version < \"3.10\"", "ipykernel", "jupyter-server[test] (>=2.4.0,<3)", "jupyterlab-server[test] (>=2.28.0,<3)", "nbval", "pytest (>=7.0)", "pytest-console-scripts", "pytest-timeout", "pytest-tornasync", "requests"]

[[package]]
name = "notebook-shim"
version = "0.2.4"
description = "A shim layer for notebook traits and config"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "notebook_shim-0.2.4-py3-none-any.whl", hash = "sha256:411a5be4e9dc882a074ccbcae671eda64cceb068767e9a3419096986560e1cef"},
    {file = "notebook_shim-0.2.4.tar.gz", hash = "sha256:b4b2cfa1b65d98307ca24361f5b30fe785b53c3fd07b7a47e89acb5e6ac638cb"},
]

[package.dependencies]
jupyter-server = ">=1.8,<3"

[package.extras]
test = ["pytest", "pytest-console-scripts", "pytest-jupyter", "pytest-tornasync"]

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main"]
markers = "python_version == \"3.10\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.4.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main"]
markers = "python_version >= \"3.11\""
files = [
    {file = "numpy-2.4.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0280e0356c0829a18d9de1cb7eee50ec22ca639878d7240307ca0943d73cd2c4"},
    {file = "numpy-2.4.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:110f8b71aacb688ec69062bb7f6938a0f8acb01b7c1c4beb453c65b6d234584d"},
    {file = "numpy-2.4.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:4cfe66903cc32a9921a6733d96b19bb6abf310397581bbad89c228f5abaf0ee8"},
    {file = "numpy-2.4.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:8155154c7c691289fe18f510b5d4657c68c67989f293f0535a91360392ff6538"},
    {file = "numpy-2.4.6-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0ab0a9c4ffb1a6d95ef519fe4247dba8eb6b18ad93999f76b7f657039acabd47"},
    {file = "numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:89cd468399cfd2504718f0ba50e410dca55a170b61a02ad92bb18c8a65186e93"},
    {file = "numpy-2.4.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c2d37ab77531417474168eb79d6d80b14f821a966818505d03013d0833edb7a8"},
    {file = "numpy-2.4.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f407cb6b8e9d6d8c626bc73c945db1706035af8fd632295547bf1c9e46d092d6"},
    {file = "numpy-2.4.6-cp311-cp311-win32.whl", hash = "sha256:ddea102b48f9e339f3948bf22040944184627a30fdf7f858667673b9c5f033c8"},
    {file = "numpy-2.4.6-cp311-cp311-win_amd64.whl", hash = "sha256:1e254a00cdf42b1e4d5b3d68d33af63268d41340d8885df2ab6470f2e1500147"},
    {file = "numpy-2.4.6-cp311-cp311-win_arm64.whl", hash = "sha256:ed9749eef4cbd126da3dc1d6bcb3a57f5eb7ac6a6484146bdbf743f552dfc577"},
    {file = "numpy-2.4.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:001fbb8e08d942dd57599e781f2472269ee7f2755fae407b4f67b2f0b17da3f1"},
    {file = "numpy-2.4.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ebfb099f8dcf083deef3ac1ca4c1503f387cf76296fcb3816b66f5ecb5f54fdb"},
    {file = "numpy-2.4.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:3213d622a0283a39a93d188f3cf72b26862df52fbb4ca3697f51705016523d41"},
    {file = "numpy-2.4.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:357cc07a6d7b0b182ff02249616a03742827ebb1277546b5c7cd7f7620a45698"},
    {file = "numpy-2.4.6-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5f9fb9157b4ce2971008323afe46053787b526ef624fea915b261468a8421a0f"},
    {file = "numpy-2.4.6-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:90f9849678c75fe7afa2d348ac842c168b0a4d3d61919687216dfc547976d853"},
    {file = "numpy-2.4.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:c1a2af6c6ef86344a6b0db6b97834208bf598db514f2b155042439b62605601a"},
    {file = "numpy-2.4.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e5805d5a22fd19c8ccff10a9561f9df94436b0545619ea579db2d3c35294bce2"},
    {file = "numpy-2.4.6-cp312-cp312-win32.whl", hash = "sha256:e3eeb0aabd6bd5ce64faae67e9935203a6991b4bc2a485a767fbafb2c5125f45"},
    {file = "numpy-2.4.6-cp312-cp312-win_amd64.whl", hash = "sha256:d8e8286dd7cea7895157318d1b91cdacac64c479f3cbc8dce548331728484751"},
    {file = "numpy-2.4.6-cp312-cp312-win_arm64.whl", hash = "sha256:4081eb135ac24158bd51cdfbef16f1c64df7063b1143f24731387137c092bec8"},
    {file = "numpy-2.4.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:511dbaf848decaaaf4b4ca48032619fb3138710c4bf7da7617765edad1ef96b0"},
    {file = "numpy-2.4.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:bf162abab1c1a736333192707cef898e735a5ca00f38f27eeedf44b39d9e85eb"},
    {file = "numpy-2.4.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:043191bfa8eab18c776647b62723ac9dddece59743b13f49b2016094129c2b3f"},
    {file = "numpy-2.4.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:6180d8b35af935aed8ece3a85e0a43f87393ae0ac87c8d2c8bd2c993f7270ef3"},
    {file = "numpy-2.4.6-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:72fbe16c6fac95aedf5937fa873445cec2110be35d8a4e9433d7501fd98dae6b"},
    {file = "numpy-2.4.6-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a7830bab239b79cda9c08c2da014761cafb48da6150e1da17ac06283f43b6089"},
    {file = "numpy-2.4.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ef4aea96ce4d3b074422cb4f2f64e216bf9e213004bb58ecfdf50ea02ea8eb9a"},
    {file = "numpy-2.4.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:dfa20cc6ca228e6b155b11da03825975ce66aea520985dbbddf0f2a5a495c605"},
    {file = "numpy-2.4.6-cp313-cp313-win32.whl", hash = "sha256:56b39e5e0622a09a25bf5baf62f4bcf0cb8a41ae6e2819cf49bbc5a74c083f91"},
    {file = "numpy-2.4.6-cp313-cp313-win_amd64.whl", hash = "sha256:c4fc99836233ea196540b17ab0983aff60ed07941751930f5f4d05bc3b3b7359"},
    {file = "numpy-2.4.6-cp313-cp313-win_arm64.whl", hash = "sha256:a7c711e21628b52034bb5ab8d1bce291f752fcc5e92accc615778acee1ff4778"},
    {file = "numpy-2.4.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:112b06a867b235ef466ed3508ddf0238050df9c727cafb5301ac385b899189a1"},
    {file = "numpy-2.4.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:eaf7fa2de5c0be8ae6ff8e9bea2ccd725e980541244521d8d4b5f3354a27babe"},
    {file = "numpy-2.4.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:7265a2f3d436e54ef9f2b52b5c937e6be778781bd97a590319d7348f1c1ca997"},
    {file = "numpy-2.4.6-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f74a575920ab21fe304421a3fc28793d82e299cae9eccb37084e9fc7f3617c20"},
    {file = "numpy-2.4.6-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ede83e07a75dd06bc501566c1eca2afc0d61677c1472ac9ad93fdee6e638a48d"},
    {file = "numpy-2.4.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:68bb27509ac1b9a3443094260f6326150663b06abe40b73a2f81160623da5b67"},
    {file = "numpy-2.4.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:a0df0043bdb289bde1f62da130d20df23d58b45429f752bc7a8fc5325a225ecd"},
    {file = "numpy-2.4.6-cp313-cp313t-win32.whl", hash = "sha256:29a287e0cf63ff528da061de6b9f64a4618da591ca1046aafc54062e40ca7eab"},
    {file = "numpy-2.4.6-cp313-cp313t-win_amd64.whl", hash = "sha256:25c692919ac5a01f170a3bfcd62d745b24fd095c353d50812637d6fcab442e75"},
    {file = "numpy-2.4.6-cp313-cp313t-win_arm64.whl", hash = "sha256:1e978ec1e8bd0e0e4de6bb75de9d30cbb74db6b6a2bb727618613703ca0167dd"},
    {file = "numpy-2.4.6-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:06ca2f61ec4385a07a6977c55ba998a4466c123642b4a32694d3128fce18c079"},
    {file = "numpy-2.4.6-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:38efbc8de75c7a0fc1ac190162d892787f3f47b57cc291231aafee36b80982b7"},
    {file = "numpy-2.4.6-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:d581b735e177fdcdce6fed8e7e8880a3fb6ee4e3653a3ac6af01c6f4c03effc5"},
    {file = "numpy-2.4.6-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:0a041d3d761dc3c35cc56ce0351506a02bcbc25f7b169f652435141a17db9096"},
    {file = "numpy-2.4.6-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:40fdc1ae7125e518ea98e53e69a4ebc27e1fd50510c47b7ea130cf21e5e1d42b"},
    {file = "numpy-2.4.6-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a2c306dea656c12c68f51f4cea133cbe78ca7435eb28c735eac1d3ebe73be6e8"},
    {file = "numpy-2.4.6-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:33111801a01c12a8a1e3721f0a9232f8cfc8ae2c6b7098167e6f623c6073f402"},
    {file = "numpy-2.4.6-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ae506e6902902557576a26ff33eda8695e7ecb3cb36c3b573a0765dee114ebdb"},
    {file = "numpy-2.4.6-cp314-cp314-win32.whl", hash = "sha256:aaf159caa35993cb1f56fb9b8e4610d35758e7ca005412eb1daa856a78c9c4b1"},
    {file = "numpy-2.4.6-cp314-cp314-win_amd64.whl", hash = "sha256:b507f5c4c1d508876d1819b6bf9a49d365b96320b5d4993426b33a23ca4b8261"},
    {file = "numpy-2.4.6-cp314-cp314-win_arm64.whl", hash = "sha256:6f41ae150c4e32db4f3310cdaf64b1593a03dbabe29eec77fc9b50fe64061df6"},
    {file = "numpy-2.4.6-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ece3d2cfe132e7d51f44a832b303895e6f2d499c5e74dfbdb06ee246147a304a"},
    {file = "numpy-2.4.6-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:e3e5193ef5a3dc73bceee50f7fdc2c90dbb76c42df8d8fae3d1067a583df579e"},
    {file = "numpy-2.4.6-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:17f9ade344e7d9b464a084d69bcf18fc691cb1db67c62ed80820bf4926d78f0e"},
    {file = "numpy-2.4.6-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9cd5ffd25db4e7ba6a375693b3fc0fc1791ec636c17db3720da19bde7180ec43"},
    {file = "numpy-2.4.6-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7d92c3819208a60205a12a245c91ad70cb0a85336659b19b834205573ac8456e"},
    {file = "numpy-2.4.6-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e85b752a1e912b70eaad4fafbd4d1238007ab221de2009b9a2f5ae7461239895"},
    {file = "numpy-2.4.6-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:29cb7f67d10b479ff07c17d33e39f78c07f71c40ef30d63c153d340e96cd3fb4"},
    {file = "numpy-2.4.6-cp314-cp314t-win32.whl", hash = "sha256:260a5d70215b61ab4fadf5c7baacd64821842975eea312125ed3c39a6391b063"},
    {file = "numpy-2.4.6-cp314-cp314t-win_amd64.whl", hash = "sha256:81a1cca95ed5bb92aa8b10dd2cdc9a0d3853a50fad926c28b5d7e8ea54389627"},
    {file = "numpy-2.4.6-cp314-cp314t-win_arm64.whl", hash = "sha256:0c9136e14ed34a9e343a31c533d78a9813a69a3148332bce5e9821cb2f996e66"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:55cced7c52e981362f708ad635198e97a752dfba412cc03c23bbf3bd8d5cd662"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:d6da64deb6b8ed903e7560180a92f2d804ee1ba5eeb849ac2748b8c1aba1f6d7"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:68a5124b13fa6cc2086764a20005d30bc0548146f7f5322f02fce212ca14317f"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:948424b06129ce883307e8cff868c31396d8dc7630a59c61d70d98dbe70f222c"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5dbbdb29840ca3d91ee0fece42fc29278886d908280bfec0a5846c6f901a3eb0"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8ad03c0965fb3c692200e74d458ca28c1dbb4ce96f9a479a8aa041ad5fabca02"},
    {file = "numpy-2.4.6-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:2803abfebfc990042cd494d8ce2d5f82e9d847af6d35ec486923aa19dbad5e73"},
    {file = "numpy-2.4.6.tar.gz", hash = "sha256:f3a3570c4a2a16746ac2c31a7c7c7b0c186b95ce902e33db6f28094ed7387dda"},
]

[[package]]
name = "overrides"
version = "7.7.0"
description = "A decorator to automatically detect mismatch when overriding a method."
optional = false
python-versions = ">=3.6"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "overrides-7.7.0-py3-none-any.whl", hash = "sha256:c7ed9d062f78b8e4c1a7b70bd8796b35ead4d9f510227ef9c5dc7626c60d7e49"},
    {file = "overrides-7.7.0.tar.gz", hash = "sha256:55158fa3d93b98cc75299b1e67078ad9003ca27945c76162c1c0766d6f91820a"},
]

[[package]]
name = "packaging"
version = "26.2"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs", "lint", "test"]
files = [
    {file = "packaging-26.2-py3-none-any.whl", hash = "sha256:5fc45236b9446107ff2415ce77c807cee2862cb6fac22b8a73826d0693b0980e"},
    {file = "packaging-26.2.tar.gz", hash = "sha256:ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"},
]

[[package]]
name = "pandocfilters"
version = "1.5.1"
description = "Utilities for writing pandoc filters in python"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
groups = ["dev"]
files = [
    {file = "pandocfilters-1.5.1-py2.py3-none-any.whl", hash = "sha256:93be382804a9cdb0a7267585f157e5d1731bbe5545a85b268d6f5fe6232de2bc"},
    {file = "pandocfilters-1.5.1.tar.gz", hash = "sha256:002b4a555ee4ebc03f8b66307e287fa492e4a77b4ea14d3f934328297bb4939e"},
]

[[package]]
name = "parso"
version = "0.8.7"
description = "A Python Parser"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "parso-0.8.7-py2.py3-none-any.whl", hash = "sha256:a8926eb2a1b915486941fdbd31e86a4baf88fe8c210f25f2f35ecec5b574ca1c"},
    {file = "parso-0.8.7.tar.gz", hash = "sha256:eaaac4c9fdd5e9e8852dc778d2d7405897ec510f2a298071453e5e3a07914bb1"},
]

[package.extras]
qa = ["flake8 (==5.0.4)", "types-setuptools (==67.2.0.1)", "zuban (==0.5.1)"]
testing = ["docopt", "pytest"]

[[package]]
name = "pathspec"
version = "1.1.1"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pathspec-1.1.1-py3-none-any.whl", hash = "sha256:a00ce642f577bf7f473932318056212bc4f8bfdf53128c78bbd5af0b9b20b189"},
    {file = "pathspec-1.1.1.tar.gz", hash = "sha256:17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]

[[package]]
name = "pep8-naming"
version = "0.15.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "pexpect"
version = "4.9.0"
description = "Pexpect allows easy control of interactive console applications."
optional = false
python-versions = "*"
groups = ["dev"]
markers = "sys_platform != \"win32\" and sys_platform != \"emscripten\""
files = [
    {file = "pexpect-4.9.0-py2.py3-none-any.whl", hash = "sha256:7236d1e080e4936be2dc3e326cec0af72acf9212a7e1d060210e70a47e253523"},
    {file = "pexpect-4.9.0.tar.gz", hash = "sha256:ee7d41123f3c9911050ea2c2dac107568dc43b2d3b0c7557a33212c398ead30f"},
]

[package.dependencies]
ptyprocess = ">=0.5"

[[package]]
name = "platformdirs"
version = "4.10.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["dev", "lint"]
files = [
    {file = "platformdirs-4.10.0-py3-none-any.whl", hash = "sha256:fb516cdb12eb0d857d0cd85a7c57cea4d060bee4578d6cf5a14dfdf8cbf8784a"},
    {file = "platformdirs-4.10.0.tar.gz", hash = "sha256:31e761a6a0ca04faf7353ea759bdba55652be214725111e5aac52dfa29d4bef7"},
]

[[package]]
name = "plotly"
version = "6.8.0"
description = "An open-source interactive data visualization library for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "plotly-6.8.0-py3-none-any.whl", hash = "sha256:13c5c4a0f70b74cab1913eda0de49b826df5931708eb6f9c3010040614700ec8"},
    {file = "plotly-6.8.0.tar.gz", hash = "sha256:e088e7ddc68d4f70e3d66659224727a45296d71d2b8284181862d3d8f1f0d88f"},
]

[package.dependencies]
narwhals = ">=1.15.1"
packaging = "*"

[package.extras]
dev = ["anywidget", "build", "colorcet", "fiona (<=1.9.6) ; python_version <= \"3.8\"", "geopandas", "inflect", "jupyterlab", "kaleido (>=1.3.0)", "numpy (>=1.22)", "orjson", "pandas", "pdfrw", "pillow", "plotly-geo", "polars[timezone]", "pyarrow", "pyshp", "pytest", "pytz", "requests", "ruff (==0.11.12)", "scikit-image", "scipy", "shapely", "statsmodels", "vaex ; python_version <= \"3.9\"", "xarray"]
dev-build = ["build", "jupyterlab", "pytest", "requests", "ruff (==0.11.12)"]
dev-core = ["pytest", "requests", "ruff (==0.11.12)"]
dev-optional = ["anywidget", "build", "colorcet", "fiona (<=1.9.6) ; python_version <= \"3.8\"", "geopandas", "inflect", "jupyterlab", "kaleido (>=1.3.0)", "numpy (>=1.22)", "orjson", "pandas", "pdfrw", "pillow", "plotly-geo", "polars[timezone]", "pyarrow", "pyshp", "pytest", "pytz", "requests", "ruff (==0.11.12)", "scikit-image", "scipy", "shapely", "statsmodels", "vaex ; python_version <= \"3.9\"", "xarray"]
dev-pandas1 = ["numpy (>=1,<2)", "pandas (>=1,<2)", "setuptools (<82)"]
dev-pandas2 = ["pandas (>=2,<3)"]
dev-pandas3 = ["pandas (>=3) ; python_version >= \"3.11\""]
express = ["numpy (>=1.22)"]
kaleido = ["kaleido (>=1.3.0)"]

[[package]]
name = "pluggy"
version = "1.6.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.9"
groups = ["test"]
files = [
    {file = "pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746"},
    {file = "pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["coverage", "pytest", "pytest-benchmark"]

[[package]]
name = "prometheus-client"
version = "0.25.0"
description = "Python client for the Prometheus monitoring system."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "prometheus_client-0.25.0-py3-none-any.whl", hash = "sha256:d5aec89e349a6ec230805d0df882f3807f74fd6c1a2fa86864e3c2279059fed1"},
    {file = "prometheus_client-0.25.0.tar.gz", hash = "sha256:5e373b75c31afb3c86f1a52fa1ad470c9aace18082d39ec0d2f918d11cc9ba28"},
]

[package.extras]
aiohttp = ["aiohttp"]
django = ["django"]
twisted = ["twisted"]

[[package]]
name = "prompt-toolkit"
version = "3.0.52"
description = "Library for building powerful interactive command lines in Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "prompt_toolkit-3.0.52-py3-none-any.whl", hash = "sha256:9aac639a3bbd33284347de5ad8d68ecc044b91a762dc39b7c21095fcd6a19955"},
    {file = "prompt_toolkit-3.0.52.tar.gz", hash = "sha256:28cde192929c8e7321de85de1ddbe736f1375148b02f2e17edd840042b1be855"},
]

[package.dependencies]
wcwidth = "*"

[[package]]
name = "protobuf"
version = "7.35.1"
description = ""
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "protobuf-7.35.1-cp310-abi3-macosx_10_9_universal2.whl", hash = "sha256:24f857477359a85c0c235261b8ba905fd51b2562f4a64ca1df5473f29850cbf6"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_aarch64.whl", hash = "sha256:11d6b0ec246892d85215b0a13ca6e0233cf5284b68f0ac02646427f4ff88a799"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_s390x.whl", hash = "sha256:b73f9489a4b8b1c9cb1f8ed951c736392592edb24b9d6819f36d2e10b171d5b4"},
    {file = "protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl", hash = "sha256:74758715c53d7158fb76caf4f0cfdacc5329a4b1bb994f865d6cf302d413a1c4"},
    {file = "protobuf-7.35.1-cp310-abi3-win32.whl", hash = "sha256:353652e4efd0bca5b5fc2656abf8307ef351f0cf938c9eba09f0e09c20a25c30"},
    {file = "protobuf-7.35.1-cp310-abi3-win_amd64.whl", hash = "sha256:230a75ddfc2de4806e56696ce9640c1cdfdb6543b7cfce98d42a4c0a0e7bdb87"},
    {file = "protobuf-7.35.1-py3-none-any.whl", hash = "sha256:4bc97768d8fe4ad6743c8a19403e314511ed9f6d13205b687e52421c023ac1b9"},
    {file = "protobuf-7.35.1.tar.gz", hash = "sha256:ce115a26fe0c39a2c29973d914d327e516a6455464489fe3cd1e51a1b354f81a"},
]

[[package]]
name = "psutil"
version = "7.2.2"
description = "Cross-platform lib for process and system monitoring."
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "psutil-7.2.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:2edccc433cbfa046b980b0df0171cd25bcaeb3a68fe9022db0979e7aa74a826b"},
    {file = "psutil-7.2.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:e78c8603dcd9a04c7364f1a3e670cea95d51ee865e4efb3556a3a63adef958ea"},
    {file = "psutil-7.2.2-cp313-cp313t-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1a571f2330c966c62aeda00dd24620425d4b0cc86881c89861fbc04549e5dc63"},
    {file = "psutil-7.2.2-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:917e891983ca3c1887b4ef36447b1e0873e70c933afc831c6b6da078ba474312"},
    {file = "psutil-7.2.2-cp313-cp313t-win_amd64.whl", hash = "sha256:ab486563df44c17f5173621c7b198955bd6b613fb87c71c161f827d3fb149a9b"},
    {file = "psutil-7.2.2-cp313-cp313t-win_arm64.whl", hash = "sha256:ae0aefdd8796a7737eccea863f80f81e468a1e4cf14d926bd9b6f5f2d5f90ca9"},
    {file = "psutil-7.2.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:eed63d3b4d62449571547b60578c5b2c4bcccc5387148db46e0c2313dad0ee00"},
    {file = "psutil-7.2.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7b6d09433a10592ce39b13d7be5a54fbac1d1228ed29abc880fb23df7cb694c9"},
    {file = "psutil-7.2.2-cp314-cp314t-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fa4ecf83bcdf6e6c8f4449aff98eefb5d0604bf88cb883d7da3d8d2d909546a"},
    {file = "psutil-7.2.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e452c464a02e7dc7822a05d25db4cde564444a67e58539a00f929c51eddda0cf"},
    {file = "psutil-7.2.2-cp314-cp314t-win_amd64.whl", hash = "sha256:c7663d4e37f13e884d13994247449e9f8f574bc4655d509c3b95e9ec9e2b9dc1"},
    {file = "psutil-7.2.2-cp314-cp314t-win_arm64.whl", hash = "sha256:11fe5a4f613759764e79c65cf11ebdf26e33d6dd34336f8a337aa2996d71c841"},
    {file = "psutil-7.2.2-cp36-abi3-macosx_10_9_x86_64.whl", hash = "sha256:ed0cace939114f62738d808fdcecd4c869222507e266e574799e9c0faa17d486"},
    {file = "psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl", hash = "sha256:1a7b04c10f32cc88ab39cbf606e117fd74721c831c98a27dc04578deb0c16979"},
    {file = "psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:076a2d2f923fd4821644f5ba89f059523da90dc9014e85f8e45a5774ca5bc6f9"},
    {file = "psutil-7.2.2-cp36-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b0726cecd84f9474419d67252add4ac0cd9811b04d61123054b9fb6f57df6e9e"},
    {file = "psutil-7.2.2-cp36-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:fd04ef36b4a6d599bbdb225dd1d3f51e00105f6d48a28f006da7f9822f2606d8"},
    {file = "psutil-7.2.2-cp36-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:b58fabe35e80b264a4e3bb23e6b96f9e45a3df7fb7eed419ac0e5947c61e47cc"},
    {file = "psutil-7.2.2-cp37-abi3-win_amd64.whl", hash = "sha256:eb7e81434c8d223ec4a219b5fc1c47d0417b12be7ea866e24fb5ad6e84b3d988"},
    {file = "psutil-7.2.2-cp37-abi3-win_arm64.whl", hash = "sha256:8c233660f575a5a89e6d4cb65d9f938126312bca76d8fe087b947b3a1aaac9ee"},
    {file = "psutil-7.2.2.tar.gz", hash = "sha256:0746f5f8d406af344fd547f1c8daa5f5c33dbc293bb8d6a16d80b4bb88f59372"},
]

[package.extras]
dev = ["abi3audit", "black", "check-manifest", "colorama ; os_name == \"nt\"", "coverage", "packaging", "psleak", "pylint", "pyperf", "pypinfo", "pyreadline3 ; os_name == \"nt\"", "pytest", "pytest-cov", "pytest-instafail", "pytest-xdist", "pywin32 ; os_name == \"nt\" and implementation_name != \"pypy\"", "requests", "rstcheck", "ruff", "setuptools", "sphinx", "sphinx_rtd_theme", "toml-sort", "twine", "validate-pyproject[all]", "virtualenv", "vulture", "wheel", "wheel ; os_name == \"nt\" and implementation_name != \"pypy\"", "wmi ; os_name == \"nt\" and implementation_name != \"pypy\""]
test = ["psleak", "pytest", "pytest-instafail", "pytest-xdist", "pywin32 ; os_name == \"nt\" and implementation_name != \"pypy\"", "setuptools", "wheel ; os_name == \"nt\" and implementation_name != \"pypy\"", "wmi ; os_name == \"nt\" and implementation_name != \"pypy\""]

[[package]]
name = "ptyprocess"
version = "0.7.0"
description = "Run a subprocess in a pseudo terminal"
optional = false
python-versions = "*"
groups = ["dev"]
markers = "sys_platform != \"win32\" and sys_platform != \"emscripten\" or os_name != \"nt\""
files = [
    {file = "ptyprocess-0.7.0-py2.py3-none-any.whl", hash = "sha256:4b41f3967fce3af57cc7e94b888626c18bf37a083e3651ca8feeb66d492fef35"},
    {file = "ptyprocess-0.7.0.tar.gz", hash = "sha256:5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220"},
]

[[package]]
name = "pure-eval"
version = "0.2.3"
description = "Safely evaluate AST nodes without side effects"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "pure_eval-0.2.3-py3-none-any.whl", hash = "sha256:1db8e35b67b3d218d818ae653e27f06c3aa420901fa7b081ca98cbedc874e0d0"},
    {file = "pure_eval-0.2.3.tar.gz", hash = "sha256:5f4e983f40564c576c7c8635ae88db5956bb2229d7e9237d03b3c0b0190eaf42"},
]

[package.extras]
tests = ["pytest"]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pycparser"
version = "3.0"
description = "C parser in Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
markers = "implementation_name != \"PyPy\""
files = [
    {file = "pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992"},
    {file = "pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3) ; python_version < \"3.11\""]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pygments"
version = "2.20.0"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.9"
groups = ["dev", "docs", "lint", "test"]
files = [
    {file = "pygments-2.20.0-py3-none-any.whl", hash = "sha256:81a9e26dd42fd28a23a2d169d86d7ac03b46e2f8b59ed4698fb4785f946d0176"},
    {file = "pygments-2.20.0.tar.gz", hash = "sha256:6757cd03768053ff99f3039c1a36d6c0aa0b263438fcab17520b30a303a82b5f"},
]

[package.extras]
windows-terminal = ["colorama (>=0.4.6)"]

[[package]]
name = "pyright"
version = "1.1.411"
description = "Command line wrapper for pyright"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "pyright-1.1.411-py3-none-any.whl", hash = "sha256:dc7c72a8e2700c55baa127554040e067041ea53ccfd50bf96308cc4291c7d5d9"},
    {file = "pyright-1.1.411.tar.gz", hash = "sha256:d885a0551f2e763b089a02702174e7f4ba77548cddabc972ab86d1f7f1b0f998"},
]

[package.dependencies]
nodeenv = ">=1.6.0"
nodejs-wheel-binaries = {version = "*", optional = true, markers = "extra == \"nodejs\""}
typing-extensions = ">=4.1"

[package.extras]
all = ["nodejs-wheel-binaries", "twine (>=3.4.1)"]
dev = ["twine (>=3.4.1)"]
nodejs = ["nodejs-wheel-binaries"]

[[package]]
name = "pytest"
version = "9.1.1"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.10"
groups = ["test"]
files = [
    {file = "pytest-9.1.1-py3-none-any.whl", hash = "sha256:37a86b45efb9a47a61a36449063e8e18d0cab3161329fc099eb21783169c4f0c"},
    {file = "pytest-9.1.1.tar.gz", hash = "sha256:1088fbde8f2b49d95a549a195707afa7a76a3ce9bcadc26b6d71f0ffda5fe313"},
]

[package.dependencies]
colorama = {version = ">=0.4", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1", markers = "python_version < \"3.11\""}
iniconfig = ">=1.0.1"
packaging = ">=22"
pluggy = ">=1.5,<2"
pygments = ">=2.7.2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "requests", "setuptools", "xmlschema"]

[[package]]
name = "pytest-cov"
version = "7.1.0"
description = "Pytest plugin for measuring coverage."
optional = false
python-versions = ">=3.9"
groups = ["test"]
files = [
    {file = "pytest_cov-7.1.0-py3-none-any.whl", hash = "sha256:a0461110b7865f9a271aa1b51e516c9a95de9d696734a2f71e3e78f46e1d4678"},
    {file = "pytest_cov-7.1.0.tar.gz", hash = "sha256:30674f2b5f6351aa09702a9c8c364f6a01c27aae0c1366ae8016160d1efc56b2"},
]

[package.dependencies]
coverage = {version = ">=7.10.6", extras = ["toml"]}
pluggy = ">=1.2"
pytest = ">=7"

[package.extras]
testing = ["process-tests", "pytest-xdist", "virtualenv"]

[[package]]
name = "pytest-doctestplus"
version = "1.7.1"
description = "Pytest plugin with advanced doctest features."
optional = false
python-versions = ">=3.10"
groups = ["test"]
files = [
    {file = "pytest_doctestplus-1.7.1-py3-none-any.whl", hash = "sha256:18c0ff78d7ad08a15f415b153b3c407078c8a8c055ceb9055b5c7be5eb7c80be"},
    {file = "pytest_doctestplus-1.7.1.tar.gz", hash = "sha256:64ae16dbda66c3db775ef596828d8d7adda09c6f34dd85099c119e4ff8cfe5b6"},
]

[package.dependencies]
packaging = ">=17.0"
pytest = ">=7.0"

[package.extras]
test = ["numpy", "pytest-remotedata (>=0.3.2)", "setuptools (>=30.3.0)", "sphinx"]

[[package]]
name = "pytest-mock"
version = "3.15.1"
description = "Thin-wrapper around the mock package for easier use with pytest"
optional = false
python-versions = ">=3.9"
groups = ["test"]
files = [
    {file = "pytest_mock-3.15.1-py3-none-any.whl", hash = "sha256:0a25e2eb88fe5168d535041d09a4529a188176ae608a6d249ee65abc0949630d"},
    {file = "pytest_mock-3.15.1.tar.gz", hash = "sha256:1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f"},
]

[package.dependencies]
pytest = ">=6.2.5"

[package.extras]
dev = ["pre-commit", "pytest-asyncio", "tox"]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
description = "Extensions to the standard Python datetime module"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["dev"]
files = [
    {file = "python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3"},
    {file = "python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427"},
]

[package.dependencies]
six = ">=1.5"

[[package]]
name = "python-json-logger"
version = "4.1.0"
description = "JSON Log Formatter for the Python Logging Package"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "python_json_logger-4.1.0-py3-none-any.whl", hash = "sha256:132994765cf75bf44554be9aa49b06ef2345d23661a96720262716438141b6b2"},
    {file = "python_json_logger-4.1.0.tar.gz", hash = "sha256:b396b9e3ed782b09ff9d6e4f1683d46c83ad0d35d2e407c09a9ebbf038f88195"},
]

[package.extras]
dev = ["black", "build", "freezegun", "mdx_truly_sane_lists", "mike", "mkdocs", "mkdocs-awesome-pages-plugin", "mkdocs-gen-files", "mkdocs-literate-nav", "mkdocs-material (>=8.5)", "mkdocstrings[python]", "msgspec ; implementation_name != \"pypy\"", "mypy", "orjson ; implementation_name != \"pypy\"", "pylint", "pytest", "tzdata", "validate-pyproject[all]"]

[[package]]
name = "pytokens"
version = "0.4.1"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "pytokens-0.4.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2a44ed93ea23415c54f3face3b65ef2b844d96aeb3455b8a69b3df6beab6acc5"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:add8bf86b71a5d9fb5b89f023a80b791e04fba57960aa790cc6125f7f1d39dfe"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:670d286910b531c7b7e3c0b453fd8156f250adb140146d234a82219459b9640c"},
    {file = "pytokens-0.4.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4e691d7f5186bd2842c14813f79f8884bb03f5995f0575272009982c5ac6c0f7"},
    {file = "pytokens-0.4.1-cp310-cp310-win_amd64.whl", hash = "sha256:27b83ad28825978742beef057bfe406ad6ed524b2d28c252c5de7b4a6dd48fa2"},
    {file = "pytokens-0.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d70e77c55ae8380c91c0c18dea05951482e263982911fc7410b1ffd1dadd3440"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4a58d057208cb9075c144950d789511220b07636dd2e4708d5645d24de666bdc"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b49750419d300e2b5a3813cf229d4e5a4c728dae470bcc89867a9ad6f25a722d"},
    {file = "pytokens-0.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:d9907d61f15bf7261d7e775bd5d7ee4d2930e04424bab1972591918497623a16"},
    {file = "pytokens-0.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:ee44d0f85b803321710f9239f335aafe16553b39106384cef8e6de40cb4ef2f6"},
    {file = "pytokens-0.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:140709331e846b728475786df8aeb27d24f48cbcf7bcd449f8de75cae7a45083"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d6c4268598f762bc8e91f5dbf2ab2f61f7b95bdc07953b602db879b3c8c18e1"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:24afde1f53d95348b5a0eb19488661147285ca4dd7ed752bbc3e1c6242a304d1"},
    {file = "pytokens-0.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5ad948d085ed6c16413eb5fec6b3e02fa00dc29a2534f088d3302c47eb59adf9"},
    {file = "pytokens-0.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:3f901fe783e06e48e8cbdc82d631fca8f118333798193e026a50ce1b3757ea68"},
    {file = "pytokens-0.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8bdb9d0ce90cbf99c525e75a2fa415144fd570a1ba987380190e8b786bc6ef9b"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5502408cab1cb18e128570f8d598981c68a50d0cbd7c61312a90507cd3a1276f"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29d1d8fb1030af4d231789959f21821ab6325e463f0503a61d204343c9b355d1"},
    {file = "pytokens-0.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b08dd6b86058b6dc07efe9e98414f5102974716232d10f32ff39701e841c4"},
    {file = "pytokens-0.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:9bd7d7f544d362576be74f9d5901a22f317efc20046efe2034dced238cbbfe78"},
    {file = "pytokens-0.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4a14d5f5fc78ce85e426aa159489e2d5961acf0e47575e08f35584009178e321"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97f50fd18543be72da51dd505e2ed20d2228c74e0464e4262e4899797803d7fa"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dc74c035f9bfca0255c1af77ddd2d6ae8419012805453e4b0e7513e17904545d"},
    {file = "pytokens-0.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f66a6bbe741bd431f6d741e617e0f39ec7257ca1f89089593479347cc4d13324"},
    {file = "pytokens-0.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:b35d7e5ad269804f6697727702da3c517bb8a5228afa450ab0fa787732055fc9"},
    {file = "pytokens-0.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:8fcb9ba3709ff77e77f1c7022ff11d13553f3c30299a9fe246a166903e9091eb"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79fc6b8699564e1f9b521582c35435f1bd32dd06822322ec44afdeba666d8cb3"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d31b97b3de0f61571a124a00ffe9a81fb9939146c122c11060725bd5aea79975"},
    {file = "pytokens-0.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:967cf6e3fd4adf7de8fc73cd3043754ae79c36475c1c11d514fc72cf5490094a"},
    {file = "pytokens-0.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:584c80c24b078eec1e227079d56dc22ff755e0ba8654d8383b2c549107528918"},
    {file = "pytokens-0.4.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:da5baeaf7116dced9c6bb76dc31ba04a2dc3695f3d9f74741d7910122b456edc"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:11edda0942da80ff58c4408407616a310adecae1ddd22eef8c692fe266fa5009"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0fc71786e629cef478cbf29d7ea1923299181d0699dbe7c3c0f4a583811d9fc1"},
    {file = "pytokens-0.4.1-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:dcafc12c30dbaf1e2af0490978352e0c4041a7cde31f4f81435c2a5e8b9cabb6"},
    {file = "pytokens-0.4.1-cp38-cp38-win_amd64.whl", hash = "sha256:42f144f3aafa5d92bad964d471a581651e28b24434d184871bd02e3a0d956037"},
    {file = "pytokens-0.4.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:34bcc734bd2f2d5fe3b34e7b3c0116bfb2397f2d9666139988e7a3eb5f7400e3"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941d4343bf27b605e9213b26bfa1c4bf197c9c599a9627eb7305b0defcfe40c1"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3ad72b851e781478366288743198101e5eb34a414f1d5627cdd585ca3b25f1db"},
    {file = "pytokens-0.4.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:682fa37ff4d8e95f7df6fe6fe6a431e8ed8e788023c6bcc0f0880a12eab80ad1"},
    {file = "pytokens-0.4.1-cp39-cp39-win_amd64.whl", hash = "sha256:30f51edd9bb7f85c748979384165601d028b84f7bd13fe14d3e065304093916a"},
    {file = "pytokens-0.4.1-py3-none-any.whl", hash = "sha256:26cef14744a8385f35d0e095dc8b3a7583f6c953c2e3d269c7f82484bf5ad2de"},
    {file = "pytokens-0.4.1.tar.gz", hash = "sha256:292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "312"
description = "Python for Windows Extensions"
optional = false
python-versions = ">=3.9"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-312-cp310-cp310-win32.whl", hash = "sha256:772235332b5d1024c696f11cea1ae4be7930f0a8b894bb43db14e3f435f1ff7e"},
    {file = "pywin32-312-cp310-cp310-win_amd64.whl", hash = "sha256:5dbc35d2b5320dc07f25fa31269cfb767471002b17de5eb067d03da68c7cb2db"},
    {file = "pywin32-312-cp310-cp310-win_arm64.whl", hash = "sha256:3020656e34f1cf7faeb7bccd2b84653a607c6ff0c55ada85e6487d61716deabd"},
    {file = "pywin32-312-cp311-cp311-win32.whl", hash = "sha256:17948aeadbdb091f0ced6ef0841620794e68327b94ee415571c1203594b7215c"},
    {file = "pywin32-312-cp311-cp311-win_amd64.whl", hash = "sha256:d11417d84412f859b722fad0841b3614459ed0047f7542d8362e77884f6b6e8a"},
    {file = "pywin32-312-cp311-cp311-win_arm64.whl", hash = "sha256:b2200a054ca6d6625c4842fc56a4976a4b47f96b73dbe5538c3f813a80359f47"},
    {file = "pywin32-312-cp312-cp312-win32.whl", hash = "sha256:dab4f65ac9c4e48400a2a0530c46c3c579cd5905ecd11b80692373915269208b"},
    {file = "pywin32-312-cp312-cp312-win_amd64.whl", hash = "sha256:b457f6d628a47e8a7346ce22acb7e1a46a4a78b52e1d17e1af56871bd19a93bc"},
    {file = "pywin32-312-cp312-cp312-win_arm64.whl", hash = "sha256:6017c58e12f6809fbb0555b75df144c2922a9ffd18e4b9b5afa863b6c1a9d950"},
    {file = "pywin32-312-cp313-cp313-win32.whl", hash = "sha256:7a27df850933d16a8eabfbaeb73d52b273e2da667f80d70b01a89d1f6828d02c"},
    {file = "pywin32-312-cp313-cp313-win_amd64.whl", hash = "sha256:c53e878d15a1c44788082bfe712a905433473aa38f86375b7cf8b45e3acbaaf9"},
    {file = "pywin32-312-cp313-cp313-win_arm64.whl", hash = "sha256:59aba5d5940842075343a5ddc6b11f1cdf0d1567fe745290359dfbcc7c2eb831"},
    {file = "pywin32-312-cp314-cp314-win32.whl", hash = "sha256:a77a90fbb6881238d2ca9c6fd797b25817f3768fe78d214a90137ff055a75f5b"},
    {file = "pywin32-312-cp314-cp314-win_amd64.whl", hash = "sha256:a4dd3a848290ef724347b19f301045831d8e802fa4464f491b98b1e0a081432e"},
    {file = "pywin32-312-cp314-cp314-win_arm64.whl", hash = "sha256:9fce94568364e0155e6dfb781ac5d95903be8baf28670632beab1b523f300daa"},
    {file = "pywin32-312-cp315-cp315-win32.whl", hash = "sha256:5c1fbe4a937a73ae9297384a3da38518cbc694c68ad8a809b2e19acd350f03ed"},
    {file = "pywin32-312-cp315-cp315-win_amd64.whl", hash = "sha256:c2f03a0f73f804a13c2735b99392b0cd426bb4f2c4d0178e5ac966a0f21618d5"},
    {file = "pywin32-312-cp315-cp315-win_arm64.whl", hash = "sha256:a8597d28f267b39074aef51fa593530082b39cbe5a074226096857b1fed2dfb9"},
    {file = "pywin32-312-cp39-cp39-win32.whl", hash = "sha256:d620900033cc7531e50727c3c8333091df5dd3ffe6d68cdca38c03f5821408d5"},
    {file = "pywin32-312-cp39-cp39-win_amd64.whl", hash = "sha256:dc90147579a905b8635e1b0ec6514967dcb07e6e0d9c42f1477feef14cac23bb"},
    {file = "pywin32-312-cp39-cp39-win_arm64.whl", hash = "sha256:02ebca0f0242b75292e218065004310d6a477407c09fa449bfe4f6022bc0c0fc"},
]

[[package]]
name = "pywinpty"
version = "3.0.3"
description = "Pseudo terminal support for Windows from Python."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
markers = "os_name == \"nt\""
files = [
    {file = "pywinpty-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:ff05f12d775b142b11c6fe085129bdd759b61cf7d41da6c745e78e3a1ef5bf40"},
    {file = "pywinpty-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:340ccacb4d74278a631923794ccd758471cfc8eeeeee4610b280420a17ad1e82"},
    {file = "pywinpty-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:dff25a9a6435f527d7c65608a7e62783fc12076e7d44487a4911ee91be5a8ac8"},
    {file = "pywinpty-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:fbc1e230e5b193eef4431cba3f39996a288f9958f9c9f092c8a961d930ee8f68"},
    {file = "pywinpty-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:c9081df0e49ffa86d15db4a6ba61530630e48707f987df42c9d3313537e81fc0"},
    {file = "pywinpty-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:15e79d870e18b678fb8a5a6105fd38496b55697c66e6fc0378236026bc4d59e9"},
    {file = "pywinpty-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9c91dbb026050c77bdcef964e63a4f10f01a639113c4d3658332614544c467ab"},
    {file = "pywinpty-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:fe1f7911805127c94cf51f89ab14096c6f91ffdcacf993d2da6082b2142a2523"},
    {file = "pywinpty-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:3f07a6cf1c1d470d284e614733c3d0f726d2c85e78508ea10a403140c3c0c18a"},
    {file = "pywinpty-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:15c7c0b6f8e9d87aabbaff76468dabf6e6121332c40fc1d83548d02a9d6a3759"},
    {file = "pywinpty-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:d4b6b7b0fe0cdcd02e956bd57cfe9f4e5a06514eecf3b5ae174da4f951b58be9"},
    {file = "pywinpty-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:34789d685fc0d547ce0c8a65e5a70e56f77d732fa6e03c8f74fefb8cbb252019"},
    {file = "pywinpty-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:0c37e224a47a971d1a6e08649a1714dac4f63c11920780977829ed5c8cadead1"},
    {file = "pywinpty-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:c4e9c3dff7d86ba81937438d5819f19f385a39d8f592d4e8af67148ceb4f6ab5"},
    {file = "pywinpty-3.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:0f10e81d52d7f2c4d927f645f247028e64eaf205a3ed9e64dbd998122108a218"},
    {file = "pywinpty-3.0.3.tar.gz", hash = "sha256:523441dc34d231fb361b4b00f8c99d3f16de02f5005fd544a0183112bcc22412"},
]

[[package]]
name = "pyyaml"
version = "6.0.3"
description = "YAML parser and emitter for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs", "lint"]
files = [
    {file = "PyYAML-6.0.3-cp38-cp38-macosx_10_13_x86_64.whl", hash = "sha256:c2514fceb77bc5e7a2f7adfaa1feb2fb311607c9cb518dbc378688ec73d8292f"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c57bb8c96f6d1808c030b1687b9b5fb476abaa47f0db9c0101f5e9f394e97f4"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:efd7b85f94a6f21e4932043973a7ba2613b059c4a000551892ac9f1d11f5baf3"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:22ba7cfcad58ef3ecddc7ed1db3409af68d023b7f940da23c6c2a1890976eda6"},
    {file = "PyYAML-6.0.3-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:6344df0d5755a2c9a276d4473ae6b90647e216ab4757f8426893b5dd2ac3f369"},
    {file = "PyYAML-6.0.3-cp38-cp38-win32.whl", hash = "sha256:3ff07ec89bae51176c0549bc4c63aa6202991da2d9a6129d7aef7f1407d3f295"},
    {file = "PyYAML-6.0.3-cp38-cp38-win_amd64.whl", hash = "sha256:5cf4e27da7e3fbed4d6c3d8e797387aaad68102272f8f9752883bc32d61cb87b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:214ed4befebe12df36bcc8bc2b64b396ca31be9304b8f59e25c11cf94a4c033b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:02ea2dfa234451bbb8772601d7b8e426c2bfa197136796224e50e35a78777956"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b30236e45cf30d2b8e7b3e85881719e98507abed1011bf463a8fa23e9c3e98a8"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:66291b10affd76d76f54fad28e22e51719ef9ba22b29e1d7d03d6777a9174198"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c7708761fccb9397fe64bbc0395abcae8c4bf7b0eac081e12b809bf47700d0b"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:418cf3f2111bc80e0933b2cd8cd04f286338bb88bdc7bc8e6dd775ebde60b5e0"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5e0b74767e5f8c593e8c9b5912019159ed0533c70051e9cce3e8b6aa699fcd69"},
    {file = "pyyaml-6.0.3-cp310-cp310-win32.whl", hash = "sha256:28c8d926f98f432f88adc23edf2e6d4921ac26fb084b028c733d01868d19007e"},
    {file = "pyyaml-6.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:bdb2c67c6c1390b63c6ff89f210c8fd09d9a1217a465701eac7316313c915e4c"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:44edc647873928551a01e7a563d7452ccdebee747728c1080d881d68af7b997e"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:652cb6edd41e718550aad172851962662ff2681490a8a711af6a4d288dd96824"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:10892704fc220243f5305762e276552a0395f7beb4dbf9b14ec8fd43b57f126c"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:850774a7879607d3a6f50d36d04f00ee69e7fc816450e5f7e58d7f17f1ae5c00"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b8bb0864c5a28024fac8a632c443c87c5aa6f215c0b126c449ae1a150412f31d"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37d57ad971609cf3c53ba6a7e365e40660e3be0e5175fa9f2365a379d6095a"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:37503bfbfc9d2c40b344d06b2199cf0e96e97957ab1c1b546fd4f87e53e5d3e4"},
    {file = "pyyaml-6.0.3-cp311-cp311-win32.whl", hash = "sha256:8098f252adfa6c80ab48096053f512f2321f0b998f98150cea9bd23d83e1467b"},
    {file = "pyyaml-6.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f3bfb4965eb874431221a3ff3fdcddc7e74e3b07799e0e84ca4a0f867d449bf"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea"},
    {file = "pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be"},
    {file = "pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_10_13_x86_64.whl", hash = "sha256:b865addae83924361678b652338317d1bd7e79b1f4596f96b96c77a5a34b34da"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c3355370a2c156cffb25e876646f149d5d68f5e0a3ce86a5084dd0b64a994917"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3c5677e12444c15717b902a5798264fa7909e41153cdf9ef7ad571b704a63dd9"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5ed875a24292240029e4483f9d4a4b8a1ae08843b9c54f43fcc11e404532a8a5"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0150219816b6a1fa26fb4699fb7daa9caf09eb1999f3b70fb6e786805e80375a"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:fa160448684b4e94d80416c0fa4aac48967a969efe22931448d853ada8baf926"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:27c0abcb4a5dac13684a37f76e701e054692a9b2d3064b70f5e4eb54810553d7"},
    {file = "pyyaml-6.0.3-cp39-cp39-win32.whl", hash = "sha256:1ebe39cb5fc479422b83de611d14e2c0d3bb2a18bbcb01f229ab3cfbd8fee7a0"},
    {file = "pyyaml-6.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:2e71d11abed7344e42a8849600193d15b6def118602c4c176f748e4583246007"},
    {file = "pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f"},
]

[[package]]
name = "pyzmq"
version = "27.1.0"
description = "Python bindings for 0MQ"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pyzmq-27.1.0-cp310-cp310-macosx_10_15_universal2.whl", hash = "sha256:508e23ec9bc44c0005c4946ea013d9317ae00ac67778bd47519fdf5a0e930ff4"},
    {file = "pyzmq-27.1.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:507b6f430bdcf0ee48c0d30e734ea89ce5567fd7b8a0f0044a369c176aa44556"},
    {file = "pyzmq-27.1.0-cp310-cp310-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:bf7b38f9fd7b81cb6d9391b2946382c8237fd814075c6aa9c3b746d53076023b"},
    {file = "pyzmq-27.1.0-cp310-cp310-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:03ff0b279b40d687691a6217c12242ee71f0fba28bf8626ff50e3ef0f4410e1e"},
    {file = "pyzmq-27.1.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:677e744fee605753eac48198b15a2124016c009a11056f93807000ab11ce6526"},
    {file = "pyzmq-27.1.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:dd2fec2b13137416a1c5648b7009499bcc8fea78154cd888855fa32514f3dad1"},
    {file = "pyzmq-27.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:08e90bb4b57603b84eab1d0ca05b3bbb10f60c1839dc471fc1c9e1507bef3386"},
    {file = "pyzmq-27.1.0-cp310-cp310-win32.whl", hash = "sha256:a5b42d7a0658b515319148875fcb782bbf118dd41c671b62dae33666c2213bda"},
    {file = "pyzmq-27.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:c0bb87227430ee3aefcc0ade2088100e528d5d3298a0a715a64f3d04c60ba02f"},
    {file = "pyzmq-27.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:9a916f76c2ab8d045b19f2286851a38e9ac94ea91faf65bd64735924522a8b32"},
    {file = "pyzmq-27.1.0-cp311-cp311-macosx_10_15_universal2.whl", hash = "sha256:226b091818d461a3bef763805e75685e478ac17e9008f49fce2d3e52b3d58b86"},
    {file = "pyzmq-27.1.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:0790a0161c281ca9723f804871b4027f2e8b5a528d357c8952d08cd1a9c15581"},
    {file = "pyzmq-27.1.0-cp311-cp311-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c895a6f35476b0c3a54e3eb6ccf41bf3018de937016e6e18748317f25d4e925f"},
    {file = "pyzmq-27.1.0-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5bbf8d3630bf96550b3be8e1fc0fea5cbdc8d5466c1192887bd94869da17a63e"},
    {file = "pyzmq-27.1.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:15c8bd0fe0dabf808e2d7a681398c4e5ded70a551ab47482067a572c054c8e2e"},
    {file = "pyzmq-27.1.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:bafcb3dd171b4ae9f19ee6380dfc71ce0390fefaf26b504c0e5f628d7c8c54f2"},
    {file = "pyzmq-27.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:e829529fcaa09937189178115c49c504e69289abd39967cd8a4c215761373394"},
    {file = "pyzmq-27.1.0-cp311-cp311-win32.whl", hash = "sha256:6df079c47d5902af6db298ec92151db82ecb557af663098b92f2508c398bb54f"},
    {file = "pyzmq-27.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:190cbf120fbc0fc4957b56866830def56628934a9d112aec0e2507aa6a032b97"},
    {file = "pyzmq-27.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:eca6b47df11a132d1745eb3b5b5e557a7dae2c303277aa0e69c6ba91b8736e07"},
    {file = "pyzmq-27.1.0-cp312-abi3-macosx_10_15_universal2.whl", hash = "sha256:452631b640340c928fa343801b0d07eb0c3789a5ffa843f6e1a9cee0ba4eb4fc"},
    {file = "pyzmq-27.1.0-cp312-abi3-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:1c179799b118e554b66da67d88ed66cd37a169f1f23b5d9f0a231b4e8d44a113"},
    {file = "pyzmq-27.1.0-cp312-abi3-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3837439b7f99e60312f0c926a6ad437b067356dc2bc2ec96eb395fd0fe804233"},
    {file = "pyzmq-27.1.0-cp312-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:43ad9a73e3da1fab5b0e7e13402f0b2fb934ae1c876c51d0afff0e7c052eca31"},
    {file = "pyzmq-27.1.0-cp312-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:0de3028d69d4cdc475bfe47a6128eb38d8bc0e8f4d69646adfbcd840facbac28"},
    {file = "pyzmq-27.1.0-cp312-abi3-musllinux_1_2_i686.whl", hash = "sha256:cf44a7763aea9298c0aa7dbf859f87ed7012de8bda0f3977b6fb1d96745df856"},
    {file = "pyzmq-27.1.0-cp312-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:f30f395a9e6fbca195400ce833c731e7b64c3919aa481af4d88c3759e0cb7496"},
    {file = "pyzmq-27.1.0-cp312-abi3-win32.whl", hash = "sha256:250e5436a4ba13885494412b3da5d518cd0d3a278a1ae640e113c073a5f88edd"},
    {file = "pyzmq-27.1.0-cp312-abi3-win_amd64.whl", hash = "sha256:9ce490cf1d2ca2ad84733aa1d69ce6855372cb5ce9223802450c9b2a7cba0ccf"},
    {file = "pyzmq-27.1.0-cp312-abi3-win_arm64.whl", hash = "sha256:75a2f36223f0d535a0c919e23615fc85a1e23b71f40c7eb43d7b1dedb4d8f15f"},
    {file = "pyzmq-27.1.0-cp313-cp313-android_24_arm64_v8a.whl", hash = "sha256:93ad4b0855a664229559e45c8d23797ceac03183c7b6f5b4428152a6b06684a5"},
    {file = "pyzmq-27.1.0-cp313-cp313-android_24_x86_64.whl", hash = "sha256:fbb4f2400bfda24f12f009cba62ad5734148569ff4949b1b6ec3b519444342e6"},
    {file = "pyzmq-27.1.0-cp313-cp313t-macosx_10_15_universal2.whl", hash = "sha256:e343d067f7b151cfe4eb3bb796a7752c9d369eed007b91231e817071d2c2fec7"},
    {file = "pyzmq-27.1.0-cp313-cp313t-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:08363b2011dec81c354d694bdecaef4770e0ae96b9afea70b3f47b973655cc05"},
    {file = "pyzmq-27.1.0-cp313-cp313t-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d54530c8c8b5b8ddb3318f481297441af102517602b569146185fa10b63f4fa9"},
    {file = "pyzmq-27.1.0-cp313-cp313t-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6f3afa12c392f0a44a2414056d730eebc33ec0926aae92b5ad5cf26ebb6cc128"},
    {file = "pyzmq-27.1.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c65047adafe573ff023b3187bb93faa583151627bc9c51fc4fb2c561ed689d39"},
    {file = "pyzmq-27.1.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:90e6e9441c946a8b0a667356f7078d96411391a3b8f80980315455574177ec97"},
    {file = "pyzmq-27.1.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:add071b2d25f84e8189aaf0882d39a285b42fa3853016ebab234a5e78c7a43db"},
    {file = "pyzmq-27.1.0-cp313-cp313t-win32.whl", hash = "sha256:7ccc0700cfdf7bd487bea8d850ec38f204478681ea02a582a8da8171b7f90a1c"},
    {file = "pyzmq-27.1.0-cp313-cp313t-win_amd64.whl", hash = "sha256:8085a9fba668216b9b4323be338ee5437a235fe275b9d1610e422ccc279733e2"},
    {file = "pyzmq-27.1.0-cp313-cp313t-win_arm64.whl", hash = "sha256:6bb54ca21bcfe361e445256c15eedf083f153811c37be87e0514934d6913061e"},
    {file = "pyzmq-27.1.0-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:ce980af330231615756acd5154f29813d553ea555485ae712c491cd483df6b7a"},
    {file = "pyzmq-27.1.0-cp314-cp314t-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:1779be8c549e54a1c38f805e56d2a2e5c009d26de10921d7d51cfd1c8d4632ea"},
    {file = "pyzmq-27.1.0-cp314-cp314t-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7200bb0f03345515df50d99d3db206a0a6bee1955fbb8c453c76f5bf0e08fb96"},
    {file = "pyzmq-27.1.0-cp314-cp314t-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01c0e07d558b06a60773744ea6251f769cd79a41a97d11b8bf4ab8f034b0424d"},
    {file = "pyzmq-27.1.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:80d834abee71f65253c91540445d37c4c561e293ba6e741b992f20a105d69146"},
    {file = "pyzmq-27.1.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:544b4e3b7198dde4a62b8ff6685e9802a9a1ebf47e77478a5eb88eca2a82f2fd"},
    {file = "pyzmq-27.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:cedc4c68178e59a4046f97eca31b148ddcf51e88677de1ef4e78cf06c5376c9a"},
    {file = "pyzmq-27.1.0-cp314-cp314t-win32.whl", hash = "sha256:1f0b2a577fd770aa6f053211a55d1c47901f4d537389a034c690291485e5fe92"},
    {file = "pyzmq-27.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:19c9468ae0437f8074af379e986c5d3d7d7bfe033506af442e8c879732bedbe0"},
    {file = "pyzmq-27.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:dc5dbf68a7857b59473f7df42650c621d7e8923fb03fa74a526890f4d33cc4d7"},
    {file = "pyzmq-27.1.0-cp38-cp38-macosx_10_15_universal2.whl", hash = "sha256:18339186c0ed0ce5835f2656cdfb32203125917711af64da64dbaa3d949e5a1b"},
    {file = "pyzmq-27.1.0-cp38-cp38-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:753d56fba8f70962cd8295fb3edb40b9b16deaa882dd2b5a3a2039f9ff7625aa"},
    {file = "pyzmq-27.1.0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:b721c05d932e5ad9ff9344f708c96b9e1a485418c6618d765fca95d4daacfbef"},
    {file = "pyzmq-27.1.0-cp38-cp38-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7be883ff3d722e6085ee3f4afc057a50f7f2e0c72d289fd54df5706b4e3d3a50"},
    {file = "pyzmq-27.1.0-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:b2e592db3a93128daf567de9650a2f3859017b3f7a66bc4ed6e4779d6034976f"},
    {file = "pyzmq-27.1.0-cp38-cp38-musllinux_1_2_i686.whl", hash = "sha256:ad68808a61cbfbbae7ba26d6233f2a4aa3b221de379ce9ee468aa7a83b9c36b0"},
    {file = "pyzmq-27.1.0-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:e2687c2d230e8d8584fbea433c24382edfeda0c60627aca3446aa5e58d5d1831"},
    {file = "pyzmq-27.1.0-cp38-cp38-win32.whl", hash = "sha256:a1aa0ee920fb3825d6c825ae3f6c508403b905b698b6460408ebd5bb04bbb312"},
    {file = "pyzmq-27.1.0-cp38-cp38-win_amd64.whl", hash = "sha256:df7cd397ece96cf20a76fae705d40efbab217d217897a5053267cd88a700c266"},
    {file = "pyzmq-27.1.0-cp39-cp39-macosx_10_15_universal2.whl", hash = "sha256:96c71c32fff75957db6ae33cd961439f386505c6e6b377370af9b24a1ef9eafb"},
    {file = "pyzmq-27.1.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:49d3980544447f6bd2968b6ac913ab963a49dcaa2d4a2990041f16057b04c429"},
    {file = "pyzmq-27.1.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:849ca054d81aa1c175c49484afaaa5db0622092b5eccb2055f9f3bb8f703782d"},
    {file = "pyzmq-27.1.0-cp39-cp39-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3970778e74cb7f85934d2b926b9900e92bfe597e62267d7499acc39c9c28e345"},
    {file = "pyzmq-27.1.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:da96ecdcf7d3919c3be2de91a8c513c186f6762aa6cf7c01087ed74fad7f0968"},
    {file = "pyzmq-27.1.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9541c444cfe1b1c0156c5c86ece2bb926c7079a18e7b47b0b1b3b1b875e5d098"},
    {file = "pyzmq-27.1.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:e30a74a39b93e2e1591b58eb1acef4902be27c957a8720b0e368f579b82dc22f"},
    {file = "pyzmq-27.1.0-cp39-cp39-win32.whl", hash = "sha256:b1267823d72d1e40701dcba7edc45fd17f71be1285557b7fe668887150a14b78"},
    {file = "pyzmq-27.1.0-cp39-cp39-win_amd64.whl", hash = "sha256:0c996ded912812a2fcd7ab6574f4ad3edc27cb6510349431e4930d4196ade7db"},
    {file = "pyzmq-27.1.0-cp39-cp39-win_arm64.whl", hash = "sha256:346e9ba4198177a07e7706050f35d733e08c1c1f8ceacd5eb6389d653579ffbc"},
    {file = "pyzmq-27.1.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:c17e03cbc9312bee223864f1a2b13a99522e0dc9f7c5df0177cd45210ac286e6"},
    {file = "pyzmq-27.1.0-pp310-pypy310_pp73-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f328d01128373cb6763823b2b4e7f73bdf767834268c565151eacb3b7a392f90"},
    {file = "pyzmq-27.1.0-pp310-pypy310_pp73-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c1790386614232e1b3a40a958454bdd42c6d1811837b15ddbb052a032a43f62"},
    {file = "pyzmq-27.1.0-pp310-pypy310_pp73-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:448f9cb54eb0cee4732b46584f2710c8bc178b0e5371d9e4fc8125201e413a74"},
    {file = "pyzmq-27.1.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:05b12f2d32112bf8c95ef2e74ec4f1d4beb01f8b5e703b38537f8849f92cb9ba"},
    {file = "pyzmq-27.1.0-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:18770c8d3563715387139060d37859c02ce40718d1faf299abddcdcc6a649066"},
    {file = "pyzmq-27.1.0-pp311-pypy311_pp73-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:ac25465d42f92e990f8d8b0546b01c391ad431c3bf447683fdc40565941d0604"},
    {file = "pyzmq-27.1.0-pp311-pypy311_pp73-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:53b40f8ae006f2734ee7608d59ed661419f087521edbfc2149c3932e9c14808c"},
    {file = "pyzmq-27.1.0-pp311-pypy311_pp73-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f605d884e7c8be8fe1aa94e0a783bf3f591b84c24e4bc4f3e7564c82ac25e271"},
    {file = "pyzmq-27.1.0-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:c9f7f6e13dff2e44a6afeaf2cf54cee5929ad64afaf4d40b50f93c58fc687355"},
    {file = "pyzmq-27.1.0-pp38-pypy38_pp73-macosx_10_15_x86_64.whl", hash = "sha256:50081a4e98472ba9f5a02850014b4c9b629da6710f8f14f3b15897c666a28f1b"},
    {file = "pyzmq-27.1.0-pp38-pypy38_pp73-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:510869f9df36ab97f89f4cff9d002a89ac554c7ac9cadd87d444aa4cf66abd27"},
    {file = "pyzmq-27.1.0-pp38-pypy38_pp73-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:1f8426a01b1c4098a750973c37131cf585f61c7911d735f729935a0c701b68d3"},
    {file = "pyzmq-27.1.0-pp38-pypy38_pp73-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:726b6a502f2e34c6d2ada5e702929586d3ac948a4dbbb7fed9854ec8c0466027"},
    {file = "pyzmq-27.1.0-pp38-pypy38_pp73-win_amd64.whl", hash = "sha256:bd67e7c8f4654bef471c0b1ca6614af0b5202a790723a58b79d9584dc8022a78"},
    {file = "pyzmq-27.1.0-pp39-pypy39_pp73-macosx_10_15_x86_64.whl", hash = "sha256:722ea791aa233ac0a819fc2c475e1292c76930b31f1d828cb61073e2fe5e208f"},
    {file = "pyzmq-27.1.0-pp39-pypy39_pp73-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:01f9437501886d3a1dd4b02ef59fb8cc384fa718ce066d52f175ee49dd5b7ed8"},
    {file = "pyzmq-27.1.0-pp39-pypy39_pp73-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4a19387a3dddcc762bfd2f570d14e2395b2c9701329b266f83dd87a2b3cbd381"},
    {file = "pyzmq-27.1.0-pp39-pypy39_pp73-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4c618fbcd069e3a29dcd221739cacde52edcc681f041907867e0f5cc7e85f172"},
    {file = "pyzmq-27.1.0-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:ff8d114d14ac671d88c89b9224c63d6c4e5a613fe8acd5594ce53d752a3aafe9"},
    {file = "pyzmq-27.1.0.tar.gz", hash = "sha256:ac0765e3d44455adb6ddbf4417dcce460fc40a05978c08efdf2948072f6db540"},
]

[package.dependencies]
cffi = {version = "*", markers = "implementation_name == \"pypy\""}

[[package]]
name = "referencing"
version = "0.37.0"
description = "JSON Referencing + Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "referencing-0.37.0-py3-none-any.whl", hash = "sha256:381329a9f99628c9069361716891d34ad94af76e461dcb0335825aecc7692231"},
    {file = "referencing-0.37.0.tar.gz", hash = "sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8"},
]

[package.dependencies]
attrs = ">=22.2.0"
rpds-py = ">=0.7.0"
typing-extensions = {version = ">=4.4.0", markers = "python_version < \"3.13\""}

[[package]]
name = "requests"
version = "2.34.2"
description = "Python HTTP for Humans."
optional = false
python-versions = ">=3.10"
groups = ["dev", "docs"]
files = [
    {file = "requests-2.34.2-py3-none-any.whl", hash = "sha256:2a0d60c172f83ac6ab31e4554906c0f3b3588d37b5cb939b1c061f4907e278e0"},
    {file = "requests-2.34.2.tar.gz", hash = "sha256:f288924cae4e29463698d6d60bc6a4da69c89185ad1e0bcc4104f584e960b9ed"},
]

[package.dependencies]
certifi = ">=2023.5.7"
charset_normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.26,<3"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use-chardet-on-py3 = ["chardet (>=3.0.2,<8)"]

[[package]]
name = "rfc3339-validator"
version = "0.1.4"
description = "A pure python RFC3339 validator"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"
groups = ["dev"]
files = [
    {file = "rfc3339_validator-0.1.4-py2.py3-none-any.whl", hash = "sha256:24f6ec1eda14ef823da9e36ec7113124b39c04d50a4d3d3a3c2859577e7791fa"},
    {file = "rfc3339_validator-0.1.4.tar.gz", hash = "sha256:138a2abdf93304ad60530167e51d2dfb9549521a836871b88d7f4695d0022f6b"},
]

[package.dependencies]
six = "*"

[[package]]
name = "rfc3986-validator"
version = "0.1.1"
description = "Pure python rfc3986 validator"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"
groups = ["dev"]
files = [
    {file = "rfc3986_validator-0.1.1-py2.py3-none-any.whl", hash = "sha256:2f235c432ef459970b4306369336b9d5dbdda31b510ca1e327636e01f528bfa9"},
    {file = "rfc3986_validator-0.1.1.tar.gz", hash = "sha256:3d44bde7921b3b9ec3ae4e3adca370438eccebc676456449b145d533b240d055"},
]

[[package]]
name = "rfc3987-syntax"
version = "1.1.0"
description = "Helper functions to syntactically validate strings according to RFC 3987."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "rfc3987_syntax-1.1.0-py3-none-any.whl", hash = "sha256:6c3d97604e4c5ce9f714898e05401a0445a641cfa276432b0a648c80856f6a3f"},
    {file = "rfc3987_syntax-1.1.0.tar.gz", hash = "sha256:717a62cbf33cffdd16dfa3a497d81ce48a660ea691b1ddd7be710c22f00b4a0d"},
]

[package.dependencies]
lark = ">=1.2.2"

[package.extras]
testing = ["pytest (>=8.3.5)"]

[[package]]
name = "rich"
version = "15.0.0"
description = "Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal"
optional = false
python-versions = ">=3.9.0"
groups = ["lint"]
files = [
    {file = "rich-15.0.0-py3-none-any.whl", hash = "sha256:33bd4ef74232fb73fe9279a257718407f169c09b78a87ad3d296f548e27de0bb"},
    {file = "rich-15.0.0.tar.gz", hash = "sha256:edd07a4824c6b40189fb7ac9bc4c52536e9780fbbfbddf6f1e2502c31b068c36"},
]

[package.dependencies]
markdown-it-py = ">=2.2.0"
pygments = ">=2.13.0,<3.0.0"

[package.extras]
jupyter = ["ipywidgets (>=7.5.1,<9)"]

[[package]]
name = "roman-numerals"
version = "4.1.0"
description = "Manipulate well-formed Roman numerals"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "roman_numerals-4.1.0-py3-none-any.whl", hash = "sha256:647ba99caddc2cc1e55a51e4360689115551bf4476d90e8162cf8c345fe233c7"},
    {file = "roman_numerals-4.1.0.tar.gz", hash = "sha256:1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2"},
]

[[package]]
name = "rpds-py"
version = "0.30.0"
description = "Python bindings to Rust's persistent data structures (rpds)"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "rpds_py-0.30.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:679ae98e00c0e8d68a7fda324e16b90fd5260945b45d3b824c892cec9eea3288"},
    {file = "rpds_py-0.30.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4cc2206b76b4f576934f0ed374b10d7ca5f457858b157ca52064bdfc26b9fc00"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:389a2d49eded1896c3d48b0136ead37c48e221b391c052fba3f4055c367f60a6"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:32c8528634e1bf7121f3de08fa85b138f4e0dc47657866630611b03967f041d7"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f207f69853edd6f6700b86efb84999651baf3789e78a466431df1331608e5324"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:67b02ec25ba7a9e8fa74c63b6ca44cf5707f2fbfadae3ee8e7494297d56aa9df"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c0e95f6819a19965ff420f65578bacb0b00f251fefe2c8b23347c37174271f3"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_31_riscv64.whl", hash = "sha256:a452763cc5198f2f98898eb98f7569649fe5da666c2dc6b5ddb10fde5a574221"},
    {file = "rpds_py-0.30.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e0b65193a413ccc930671c55153a03ee57cecb49e6227204b04fae512eb657a7"},
    {file = "rpds_py-0.30.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:858738e9c32147f78b3ac24dc0edb6610000e56dc0f700fd5f651d0a0f0eb9ff"},
    {file = "rpds_py-0.30.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:da279aa314f00acbb803da1e76fa18666778e8a8f83484fba94526da5de2cba7"},
    {file = "rpds_py-0.30.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:7c64d38fb49b6cdeda16ab49e35fe0da2e1e9b34bc38bd78386530f218b37139"},
    {file = "rpds_py-0.30.0-cp310-cp310-win32.whl", hash = "sha256:6de2a32a1665b93233cde140ff8b3467bdb9e2af2b91079f0333a0974d12d464"},
    {file = "rpds_py-0.30.0-cp310-cp310-win_amd64.whl", hash = "sha256:1726859cd0de969f88dc8673bdd954185b9104e05806be64bcd87badbe313169"},
    {file = "rpds_py-0.30.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a2bffea6a4ca9f01b3f8e548302470306689684e61602aa3d141e34da06cf425"},
    {file = "rpds_py-0.30.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:dc4f992dfe1e2bc3ebc7444f6c7051b4bc13cd8e33e43511e8ffd13bf407010d"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:422c3cb9856d80b09d30d2eb255d0754b23e090034e1deb4083f8004bd0761e4"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:07ae8a593e1c3c6b82ca3292efbe73c30b61332fd612e05abee07c79359f292f"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:12f90dd7557b6bd57f40abe7747e81e0c0b119bef015ea7726e69fe550e394a4"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:99b47d6ad9a6da00bec6aabe5a6279ecd3c06a329d4aa4771034a21e335c3a97"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:33f559f3104504506a44bb666b93a33f5d33133765b0c216a5bf2f1e1503af89"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_31_riscv64.whl", hash = "sha256:946fe926af6e44f3697abbc305ea168c2c31d3e3ef1058cf68f379bf0335a78d"},
    {file = "rpds_py-0.30.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:495aeca4b93d465efde585977365187149e75383ad2684f81519f504f5c13038"},
    {file = "rpds_py-0.30.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d9a0ca5da0386dee0655b4ccdf46119df60e0f10da268d04fe7cc87886872ba7"},
    {file = "rpds_py-0.30.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8d6d1cc13664ec13c1b84241204ff3b12f9bb82464b8ad6e7a5d3486975c2eed"},
    {file = "rpds_py-0.30.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3896fa1be39912cf0757753826bc8bdc8ca331a28a7c4ae46b7a21280b06bb85"},
    {file = "rpds_py-0.30.0-cp311-cp311-win32.whl", hash = "sha256:55f66022632205940f1827effeff17c4fa7ae1953d2b74a8581baaefb7d16f8c"},
    {file = "rpds_py-0.30.0-cp311-cp311-win_amd64.whl", hash = "sha256:a51033ff701fca756439d641c0ad09a41d9242fa69121c7d8769604a0a629825"},
    {file = "rpds_py-0.30.0-cp311-cp311-win_arm64.whl", hash = "sha256:47b0ef6231c58f506ef0b74d44e330405caa8428e770fec25329ed2cb971a229"},
    {file = "rpds_py-0.30.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:a161f20d9a43006833cd7068375a94d035714d73a172b681d8881820600abfad"},
    {file = "rpds_py-0.30.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:6abc8880d9d036ecaafe709079969f56e876fcf107f7a8e9920ba6d5a3878d05"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ca28829ae5f5d569bb62a79512c842a03a12576375d5ece7d2cadf8abe96ec28"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:a1010ed9524c73b94d15919ca4d41d8780980e1765babf85f9a2f90d247153dd"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f8d1736cfb49381ba528cd5baa46f82fdc65c06e843dab24dd70b63d09121b3f"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:d948b135c4693daff7bc2dcfc4ec57237a29bd37e60c2fabf5aff2bbacf3e2f1"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47f236970bccb2233267d89173d3ad2703cd36a0e2a6e92d0560d333871a3d23"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_31_riscv64.whl", hash = "sha256:2e6ecb5a5bcacf59c3f912155044479af1d0b6681280048b338b28e364aca1f6"},
    {file = "rpds_py-0.30.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a8fa71a2e078c527c3e9dc9fc5a98c9db40bcc8a92b4e8858e36d329f8684b51"},
    {file = "rpds_py-0.30.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:73c67f2db7bc334e518d097c6d1e6fed021bbc9b7d678d6cc433478365d1d5f5"},
    {file = "rpds_py-0.30.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:5ba103fb455be00f3b1c2076c9d4264bfcb037c976167a6047ed82f23153f02e"},
    {file = "rpds_py-0.30.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7cee9c752c0364588353e627da8a7e808a66873672bcb5f52890c33fd965b394"},
    {file = "rpds_py-0.30.0-cp312-cp312-win32.whl", hash = "sha256:1ab5b83dbcf55acc8b08fc62b796ef672c457b17dbd7820a11d6c52c06839bdf"},
    {file = "rpds_py-0.30.0-cp312-cp312-win_amd64.whl", hash = "sha256:a090322ca841abd453d43456ac34db46e8b05fd9b3b4ac0c78bcde8b089f959b"},
    {file = "rpds_py-0.30.0-cp312-cp312-win_arm64.whl", hash = "sha256:669b1805bd639dd2989b281be2cfd951c6121b65e729d9b843e9639ef1fd555e"},
    {file = "rpds_py-0.30.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:f83424d738204d9770830d35290ff3273fbb02b41f919870479fab14b9d303b2"},
    {file = "rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e7536cd91353c5273434b4e003cbda89034d67e7710eab8761fd918ec6c69cf8"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2771c6c15973347f50fece41fc447c054b7ac2ae0502388ce3b6738cd366e3d4"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0a59119fc6e3f460315fe9d08149f8102aa322299deaa5cab5b40092345c2136"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:76fec018282b4ead0364022e3c54b60bf368b9d926877957a8624b58419169b7"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:692bef75a5525db97318e8cd061542b5a79812d711ea03dbc1f6f8dbb0c5f0d2"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9027da1ce107104c50c81383cae773ef5c24d296dd11c99e2629dbd7967a20c6"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_31_riscv64.whl", hash = "sha256:9cf69cdda1f5968a30a359aba2f7f9aa648a9ce4b580d6826437f2b291cfc86e"},
    {file = "rpds_py-0.30.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a4796a717bf12b9da9d3ad002519a86063dcac8988b030e405704ef7d74d2d9d"},
    {file = "rpds_py-0.30.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5d4c2aa7c50ad4728a094ebd5eb46c452e9cb7edbfdb18f9e1221f597a73e1e7"},
    {file = "rpds_py-0.30.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ba81a9203d07805435eb06f536d95a266c21e5b2dfbf6517748ca40c98d19e31"},
    {file = "rpds_py-0.30.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:945dccface01af02675628334f7cf49c2af4c1c904748efc5cf7bbdf0b579f95"},
    {file = "rpds_py-0.30.0-cp313-cp313-win32.whl", hash = "sha256:b40fb160a2db369a194cb27943582b38f79fc4887291417685f3ad693c5a1d5d"},
    {file = "rpds_py-0.30.0-cp313-cp313-win_amd64.whl", hash = "sha256:806f36b1b605e2d6a72716f321f20036b9489d29c51c91f4dd29a3e3afb73b15"},
    {file = "rpds_py-0.30.0-cp313-cp313-win_arm64.whl", hash = "sha256:d96c2086587c7c30d44f31f42eae4eac89b60dabbac18c7669be3700f13c3ce1"},
    {file = "rpds_py-0.30.0-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:eb0b93f2e5c2189ee831ee43f156ed34e2a89a78a66b98cadad955972548be5a"},
    {file = "rpds_py-0.30.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:922e10f31f303c7c920da8981051ff6d8c1a56207dbdf330d9047f6d30b70e5e"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cdc62c8286ba9bf7f47befdcea13ea0e26bf294bda99758fd90535cbaf408000"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:47f9a91efc418b54fb8190a6b4aa7813a23fb79c51f4bb84e418f5476c38b8db"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1f3587eb9b17f3789ad50824084fa6f81921bbf9a795826570bda82cb3ed91f2"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:39c02563fc592411c2c61d26b6c5fe1e51eaa44a75aa2c8735ca88b0d9599daa"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:51a1234d8febafdfd33a42d97da7a43f5dcb120c1060e352a3fbc0c6d36e2083"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_31_riscv64.whl", hash = "sha256:eb2c4071ab598733724c08221091e8d80e89064cd472819285a9ab0f24bcedb9"},
    {file = "rpds_py-0.30.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:6bdfdb946967d816e6adf9a3d8201bfad269c67efe6cefd7093ef959683c8de0"},
    {file = "rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c77afbd5f5250bf27bf516c7c4a016813eb2d3e116139aed0096940c5982da94"},
    {file = "rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:61046904275472a76c8c90c9ccee9013d70a6d0f73eecefd38c1ae7c39045a08"},
    {file = "rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:4c5f36a861bc4b7da6516dbdf302c55313afa09b81931e8280361a4f6c9a2d27"},
    {file = "rpds_py-0.30.0-cp313-cp313t-win32.whl", hash = "sha256:3d4a69de7a3e50ffc214ae16d79d8fbb0922972da0356dcf4d0fdca2878559c6"},
    {file = "rpds_py-0.30.0-cp313-cp313t-win_amd64.whl", hash = "sha256:f14fc5df50a716f7ece6a80b6c78bb35ea2ca47c499e422aa4463455dd96d56d"},
    {file = "rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:68f19c879420aa08f61203801423f6cd5ac5f0ac4ac82a2368a9fcd6a9a075e0"},
    {file = "rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:ec7c4490c672c1a0389d319b3a9cfcd098dcdc4783991553c332a15acf7249be"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f251c812357a3fed308d684a5079ddfb9d933860fc6de89f2b7ab00da481e65f"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ac98b175585ecf4c0348fd7b29c3864bda53b805c773cbf7bfdaffc8070c976f"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3e62880792319dbeb7eb866547f2e35973289e7d5696c6e295476448f5b63c87"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4e7fc54e0900ab35d041b0601431b0a0eb495f0851a0639b6ef90f7741b39a18"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47e77dc9822d3ad616c3d5759ea5631a75e5809d5a28707744ef79d7a1bcfcad"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_31_riscv64.whl", hash = "sha256:b4dc1a6ff022ff85ecafef7979a2c6eb423430e05f1165d6688234e62ba99a07"},
    {file = "rpds_py-0.30.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:4559c972db3a360808309e06a74628b95eaccbf961c335c8fe0d590cf587456f"},
    {file = "rpds_py-0.30.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:0ed177ed9bded28f8deb6ab40c183cd1192aa0de40c12f38be4d59cd33cb5c65"},
    {file = "rpds_py-0.30.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:ad1fa8db769b76ea911cb4e10f049d80bf518c104f15b3edb2371cc65375c46f"},
    {file = "rpds_py-0.30.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:46e83c697b1f1c72b50e5ee5adb4353eef7406fb3f2043d64c33f20ad1c2fc53"},
    {file = "rpds_py-0.30.0-cp314-cp314-win32.whl", hash = "sha256:ee454b2a007d57363c2dfd5b6ca4a5d7e2c518938f8ed3b706e37e5d470801ed"},
    {file = "rpds_py-0.30.0-cp314-cp314-win_amd64.whl", hash = "sha256:95f0802447ac2d10bcc69f6dc28fe95fdf17940367b21d34e34c737870758950"},
    {file = "rpds_py-0.30.0-cp314-cp314-win_arm64.whl", hash = "sha256:613aa4771c99f03346e54c3f038e4cc574ac09a3ddfb0e8878487335e96dead6"},
    {file = "rpds_py-0.30.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:7e6ecfcb62edfd632e56983964e6884851786443739dbfe3582947e87274f7cb"},
    {file = "rpds_py-0.30.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a1d0bc22a7cdc173fedebb73ef81e07faef93692b8c1ad3733b67e31e1b6e1b8"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0d08f00679177226c4cb8c5265012eea897c8ca3b93f429e546600c971bcbae7"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:5965af57d5848192c13534f90f9dd16464f3c37aaf166cc1da1cae1fd5a34898"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9a4e86e34e9ab6b667c27f3211ca48f73dba7cd3d90f8d5b11be56e5dbc3fb4e"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e5d3e6b26f2c785d65cc25ef1e5267ccbe1b069c5c21b8cc724efee290554419"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:626a7433c34566535b6e56a1b39a7b17ba961e97ce3b80ec62e6f1312c025551"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:acd7eb3f4471577b9b5a41baf02a978e8bdeb08b4b355273994f8b87032000a8"},
    {file = "rpds_py-0.30.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:fe5fa731a1fa8a0a56b0977413f8cacac1768dad38d16b3a296712709476fbd5"},
    {file = "rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:74a3243a411126362712ee1524dfc90c650a503502f135d54d1b352bd01f2404"},
    {file = "rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:3e8eeb0544f2eb0d2581774be4c3410356eba189529a6b3e36bbbf9696175856"},
    {file = "rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:dbd936cde57abfee19ab3213cf9c26be06d60750e60a8e4dd85d1ab12c8b1f40"},
    {file = "rpds_py-0.30.0-cp314-cp314t-win32.whl", hash = "sha256:dc824125c72246d924f7f796b4f63c1e9dc810c7d9e2355864b3c3a73d59ade0"},
    {file = "rpds_py-0.30.0-cp314-cp314t-win_amd64.whl", hash = "sha256:27f4b0e92de5bfbc6f86e43959e6edd1425c33b5e69aab0984a72047f2bcf1e3"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:c2262bdba0ad4fc6fb5545660673925c2d2a5d9e2e0fb603aad545427be0fc58"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:ee6af14263f25eedc3bb918a3c04245106a42dfd4f5c2285ea6f997b1fc3f89a"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3adbb8179ce342d235c31ab8ec511e66c73faa27a47e076ccc92421add53e2bb"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:250fa00e9543ac9b97ac258bd37367ff5256666122c2d0f2bc97577c60a1818c"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9854cf4f488b3d57b9aaeb105f06d78e5529d3145b1e4a41750167e8c213c6d3"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:993914b8e560023bc0a8bf742c5f303551992dcb85e247b1e5c7f4a7d145bda5"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58edca431fb9b29950807e301826586e5bbf24163677732429770a697ffe6738"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_31_riscv64.whl", hash = "sha256:dea5b552272a944763b34394d04577cf0f9bd013207bc32323b5a89a53cf9c2f"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:ba3af48635eb83d03f6c9735dfb21785303e73d22ad03d489e88adae6eab8877"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_aarch64.whl", hash = "sha256:dff13836529b921e22f15cb099751209a60009731a68519630a24d61f0b1b30a"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_i686.whl", hash = "sha256:1b151685b23929ab7beec71080a8889d4d6d9fa9a983d213f07121205d48e2c4"},
    {file = "rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_x86_64.whl", hash = "sha256:ac37f9f516c51e5753f27dfdef11a88330f04de2d564be3991384b2f3535d02e"},
    {file = "rpds_py-0.30.0.tar.gz", hash = "sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84"},
]

[[package]]
name = "rpds-py"
version = "2026.5.1"
description = "Python bindings to Rust's persistent data structures (rpds)"
optional = false
python-versions = ">=3.11"
groups = ["dev"]
markers = "python_version >= \"3.11\""
files = [
    {file = "rpds_py-2026.5.1-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:3397a5ed7174dc2786bb214030232fc36fe8e5584fec43a9952cc542b1a12036"},
    {file = "rpds_py-2026.5.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:99ab6ba7bfa2cb0f96a04e3652355bf04e3f51aceb1e943b8541dab7ba4828cc"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d0efbe45632665e53e3db8fe1e5692db58fc5cb9bab4459d570b83efefe11164"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:01d17b29c0c23d82b1f4751147ec49cf451f1fc2554eb9ef5f957e55d2656ead"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7559f72b94ae52659086c595dfa017cde03155f7832071d30959049052cb3ece"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9e25b7088f9ccbfc0dfcaa52bf969300ca229e10ecf758974ebcbb080a4b37bb"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:613fc4ee9eaef26dc5840666214dd6fbcebcf32f46e76f4abc473059f4e13dda"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_31_riscv64.whl", hash = "sha256:85264a90ff4c05c1568dd65f5921c837614b67c60358fb4c17df3b7f2e90690a"},
    {file = "rpds_py-2026.5.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:fe71bca7d547acb17027c7fd1624ff8aae623499c498d3e7011182c4de5c25e0"},
    {file = "rpds_py-2026.5.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:a05fa4f41f37ec97c9c260441a940450a192f78d774d2b097eee1379f1e1246a"},
    {file = "rpds_py-2026.5.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:df1d2a1996755b24b9ecee92cb4d36c28f86f464a6a173349c26bab41e94b8c2"},
    {file = "rpds_py-2026.5.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:8895840ac4809e5f60c88fd07617cd71326e73d6e5a8aa783c5c0f7c24985de2"},
    {file = "rpds_py-2026.5.1-cp311-cp311-win32.whl", hash = "sha256:3684a59b158a7683aaeb8e25352e9a9dd2122cec78f2d8530266e4f91b4c7b3f"},
    {file = "rpds_py-2026.5.1-cp311-cp311-win_amd64.whl", hash = "sha256:7bd530e6a530bb3ea892f194fafa455f3516ac25ecf7143fd33c09be62b0470a"},
    {file = "rpds_py-2026.5.1-cp311-cp311-win_arm64.whl", hash = "sha256:0a5ae4dbe43c1076983b72616496919872ae7bbe7a1e21cc48336bc3154d130b"},
    {file = "rpds_py-2026.5.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:3abe24a66e57adcfa645d718063a5fa5103ecc71ddbf26d78af8f9368018ff1d"},
    {file = "rpds_py-2026.5.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:58b1d94308ddf0b1982f61f2eb54bf92997c9ece8a8093ef014250f4a517906c"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0fa92420128dadce7f54bd73ba1825a273e9268fe9e35dbf7e6362890efa4e08"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ca653c6546386227cd9800d1bef6a348099acf8db4250341da6d90f663d6dfcb"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:66c93681c4729e4e3ecba31b8179fae083ff3118841672835140338b4b9867c1"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:40ff257542e04796880e011e15cd4dc21c2599975df2aaa8f2c8495ca574e1a5"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b6825cc329b290e93c5f6a9be2393118a763f6ccf6abd83704e0c102ca583644"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_31_riscv64.whl", hash = "sha256:de42116e69cb53b911cc34aee5ab98f36c597b822545045d49e938818b99e5e4"},
    {file = "rpds_py-2026.5.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c0f920015df2a504bebaba6d4c31ccf3fcf942f92655c086da30b671aad19aa6"},
    {file = "rpds_py-2026.5.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:0408a24e44feb919423dc6d9da677cb5cddb894d2ca9e763967d156d9c60fab4"},
    {file = "rpds_py-2026.5.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:cea68bcd53467561ae2f96a6bdad1544299ba97b5b0ddcd5ac3d376e5c781c24"},
    {file = "rpds_py-2026.5.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:4be8b1d2a705cc37d08256004e1d07de143fa0075c8e85a3df020b776f62b732"},
    {file = "rpds_py-2026.5.1-cp312-cp312-win32.whl", hash = "sha256:6736718bd4fc49cbcb538ba30516fdbef161522acefb739657d48b97bd864fed"},
    {file = "rpds_py-2026.5.1-cp312-cp312-win_amd64.whl", hash = "sha256:0a7d1eec967df0e9b22614a5e177622e0c89611d03727fa0cb48e45028907870"},
    {file = "rpds_py-2026.5.1-cp312-cp312-win_arm64.whl", hash = "sha256:1841d067089e117142d79b98aa0df2f08b52f2ecc1819dd2700636c0db74a473"},
    {file = "rpds_py-2026.5.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:efef4ac29c6ff495531eb17ee705b62841ecaa291b7c7077e848ea03e237164d"},
    {file = "rpds_py-2026.5.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:c39f5b67a8a2e67179ada2a954227d670fe65fa9098457f698f56ddf248709b3"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b5c30f3f04eef4fbd362226a6f31d7c8895ca4fbb6e0b790f6890a98d8da8559"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:277f6c82f0580848796c7ecc8a7173aa3bfb928e4ff831261c2f60a81dc270db"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:63c2c4c213f1a4e3f3de28ecab029dbdee976324e729c0d7a55211be72576b02"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3350ec808fb538fe71a1f94dfaa0e29c598dfad805ce49f0caec5ae3183c652b"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b1b964e3ab599e718dc46c018d104b1ebc007cbc6567d827c94a687fca56d77e"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_31_riscv64.whl", hash = "sha256:19cb09fab7b7fc96b2a6e28f2e34b72a3705ff27b37edb77455316e5d3f3dc9b"},
    {file = "rpds_py-2026.5.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:abe76bcdba31e576cb83eeb8797aa0d882b738fef6dc65d0601fc753806a5b46"},
    {file = "rpds_py-2026.5.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:8bff7073db3899158fff55ebf57b113a67030af26f80a18978f9f0aa60250ddf"},
    {file = "rpds_py-2026.5.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:8ba264fa49be666cd9cc56bf34ec7002fb3d27a4aee5bcb4d43d0d18feb1bb6f"},
    {file = "rpds_py-2026.5.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4860b603ddda0475a8885499b3729e90229d480105b42651962a5397d995fa89"},
    {file = "rpds_py-2026.5.1-cp313-cp313-win32.whl", hash = "sha256:7944270ae71383f6e2657dd7d5ce4eeb4ac2d0059a6738f0510583d462ab4842"},
    {file = "rpds_py-2026.5.1-cp313-cp313-win_amd64.whl", hash = "sha256:88647f43a73c4e01be19b04ceef0c8d3a1958153604d13c773becd8016f2a0cf"},
    {file = "rpds_py-2026.5.1-cp313-cp313-win_arm64.whl", hash = "sha256:453895624ecf7db7063b1004e44037522bbaef9ff6a945e59bc71662d7a03abd"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:b4e4bc98639ec915f512fde3aa7a95e0041d95d9c3cc86eea841fa63cb1e8600"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:cacedb7a6e167680acba45ad5716e89067d225dc80da0d7040cae8c81d4572fa"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:68700371c5d7ae1412862ddfa719090925c93ecf351c566d66f09d04b136ea00"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:296c799becfa849c779c8725494fe9ed94959ed886787df4364b058465bad7f0"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d3858b908218ee108d0bbfb2095ccc237648053c9bf98affad7cb079acaf1d97"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4fb8d2e7cb2f850b169806d61d1b991738acec96500a75c30f49caf064ce7cef"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:27b74c10ed6a8f190f4287f53bcfea348b92a84a9c9f70d30183d1e6172d580d"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_31_riscv64.whl", hash = "sha256:b9a6528956191c48c52294a592dbd4a8386d7048bdb25c0efcb6b966466c6d83"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:af03e34e860047bc7a352b842856fcf78798fbb81132cc98bd2f907ab4eb9cd2"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:fea6e836d10abbe191d557d33bd58bd5987725fe63aa1eefe557d230209855bd"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:fc0c0f878ea770a0a8a462456c5ad36fc9fe6358e6b76fdadc7f17575e0b8bf1"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:e0b360f316d966b048b085857630b3cc51f3db2f07b06f440eac8f695374d1e3"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-win32.whl", hash = "sha256:a2999883eedf72fdfb7520b92c7d4ec2572a71ff40239377aa604cc529eecafc"},
    {file = "rpds_py-2026.5.1-cp313-cp313t-win_amd64.whl", hash = "sha256:e07be2a9d7122bd6e82dea89814ef8dc893feb1aae97fec1630f3263bbb30e55"},
    {file = "rpds_py-2026.5.1-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:1f2c391c3059798093b65df23aca2cac150460ae9c630d99dec83d703d9485b9"},
    {file = "rpds_py-2026.5.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:413b424f7c4ee65ab5e5be91f5731be0f8b41a1ee2b12dfe810d716312e95a78"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2c595a1d9255dce0599e13130d1440ab2506654f2b50294226ee06402f8fef63"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:1c27c5f6102eac8c03e7595a00827a53b271ba40a53b59ff8709170e0855ea4a"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6c7fcf61d44cacecaf3aea542b0e053db77972a4573e7ceda16fb2b399161195"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2c817a189d4ee14290420e5ff051e4dd6baa13f3edf84685071dee07a6d538ee"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:21846aac0ed2e0589f38c12dc44e77bb64e494b771eadbcf169cba00566ba7ba"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_31_riscv64.whl", hash = "sha256:b317c87a13f769a4e787819bd508aaa5d69aa09b0880de9af6d3a8a54571cdec"},
    {file = "rpds_py-2026.5.1-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:ce87129d9f2c14fa6c4a8601fb80eb4488c80d38a20cd13758ef11123e14995d"},
    {file = "rpds_py-2026.5.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:9cdddb6c1207d284d94fd1530adf57fbd797fe7c4b8704ba85f49414f2557e7d"},
    {file = "rpds_py-2026.5.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:4e237e139f94d3c036fd28eb9f564c99055476ff4ff05cd42be55ce349b5aa02"},
    {file = "rpds_py-2026.5.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ed0954b524873214369184a9c82b0eaa45a3fbb9a798cd95b17e0d98499e7ea0"},
    {file = "rpds_py-2026.5.1-cp314-cp314-win32.whl", hash = "sha256:2d88621d6a7d4dfa633d21abe90f280bb205274e16b1d1e61c6ad4640b2453b7"},
    {file = "rpds_py-2026.5.1-cp314-cp314-win_amd64.whl", hash = "sha256:cef8ac28d26f4dda3533060c20fbf80a325458fa9fd23ea72a73cdfa8e978838"},
    {file = "rpds_py-2026.5.1-cp314-cp314-win_arm64.whl", hash = "sha256:eaaea962c68cdc68d4a533ba985ab8e9484277910bbfaa2ab3ef7732667bfed8"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:21942f52dbbd5f8758bf021213d28bd45c39e873e65e2407faf5f1846f5761ad"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:f414556f6e3958300ff941e40c9f97e3dc9774ddd1b3434c475d73dd354bbed3"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ef1013a8625c74043210190b246f5b1551e09757c1f356c6e4160ef96c5bc081"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:cc68e231a77a5f0d774ae278a1f8e55c0456501820847c1e4efb3829f3441df6"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9baffb505aff33acc69b422a19f77806680f3c8632227d79f48de8a810d1c2c5"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b8d2f912928d426e8cfa396f7f3f8d29a59e6689c86dcca3c420730c1096322b"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:90f628283be835db980c941767d41c9a27b5239e54ba0a9c1335247e82406964"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:1ebb2f0ab7e16132995a72de805170e0203df0c3dd22e1ef1cd1fdd90bd7a131"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:f3df3d16ded76f1f8c9cdebd0e1ea55fdf4c23b812de189814da7cf229c22a81"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:9af8905b8f854990e40d5206aa5ac58d9b0fe0b7f351ff2bb086c20f6c8c6a47"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:036a36a87fb1cd3b214d11c4b3c4f7d2ddad933625dca1c900b56a057c07740a"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:62ae3853454fe9ef283a03c96c2d835d39e84b14643a9d62c82ef0fb87d702ca"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-win32.whl", hash = "sha256:6c3d771a46ec18b12af06ce36243a9a80b07a5d0515236332d90863ca8bb326a"},
    {file = "rpds_py-2026.5.1-cp314-cp314t-win_amd64.whl", hash = "sha256:c93c629be4636cf54337bd5f06c104d55e42ced54d681f6fe21ae510a65116f6"},
    {file = "rpds_py-2026.5.1-cp315-cp315-macosx_10_12_x86_64.whl", hash = "sha256:3574b55c604b8f75dacb007136508bbc0db406e626301778096a133327e7f2fb"},
    {file = "rpds_py-2026.5.1-cp315-cp315-macosx_11_0_arm64.whl", hash = "sha256:94068eb3ae6d43f5a786b7db96a406a34e6d5c24489feef32fd6e8946ea7b291"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f3a5b10e8ce894825f380a8f1b6444cf73c294dfea62afbb2d13e3a9e630cec1"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:fc09f82e63d4bcd58149572f857a431bae851dc747e313c3b5bdf7abb907fda8"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e10464d17df3b582745c25cec695cb9558bca2cb6ddb631aee1787fc72c767b2"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ba05adbf15d994c38ec0b7ab32e858e5110c21e9009a00a86545fd220f84e038"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:77c004fdc7b891967106f78ddfd7b076bfe6813c6139c6fff6aed3bcaa960b26"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_31_riscv64.whl", hash = "sha256:83bcf894486c9d78dd290d3c0124ff6dd8875d3025e2090a8ec49fcc37c55fdd"},
    {file = "rpds_py-2026.5.1-cp315-cp315-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c3df104083952a0e0c6f10de33e440eabe98fb6317d23e1a58c68f6df08d01b9"},
    {file = "rpds_py-2026.5.1-cp315-cp315-musllinux_1_2_aarch64.whl", hash = "sha256:980450826cf22e133c57e0835070bdd0dd3f73b9b708c3ce223def2cb9469e14"},
    {file = "rpds_py-2026.5.1-cp315-cp315-musllinux_1_2_i686.whl", hash = "sha256:205dde846f24332ab0c1188699a043b8d165b79bb84529ce272c45048ff6be01"},
    {file = "rpds_py-2026.5.1-cp315-cp315-musllinux_1_2_x86_64.whl", hash = "sha256:3966b82dd563176396df030f3dd52a6e54cb69b718e95e78bd555ed3d1e0185d"},
    {file = "rpds_py-2026.5.1-cp315-cp315-win32.whl", hash = "sha256:7818f8d0a415be74d2be3590b0a1c1f463a642f4d0217e7d10602dceef5b79aa"},
    {file = "rpds_py-2026.5.1-cp315-cp315-win_amd64.whl", hash = "sha256:b3cc20c0d800af78fd0fac68086e28c1856cec51ea528bb81ea851aa40d39325"},
    {file = "rpds_py-2026.5.1-cp315-cp315-win_arm64.whl", hash = "sha256:3609e9939a8a76cd904cf98a3f1f13b5dc7e150adeaee89e0ea09652ea213e16"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-macosx_10_12_x86_64.whl", hash = "sha256:5d333a7127d4b307601ac37792bee01bb95c867cbfacf21b6375b804d6bbd723"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-macosx_11_0_arm64.whl", hash = "sha256:b5f077b44a4f7808520f66dae234988d867deb9aed9be5da057ce9ba831b2a41"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:55d8f9b7b78c9538fc9e04e82ec0e888ff0c3cffcfad152c77e57cd09351a98a"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e3a8ae58895ac107ed934a6bf51e5846f95c53b9b940c2c6d310838fd5846358"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0957cf3c2b8632ec7aaebffebea8005b353cc2a237b6e2ae3c2cac0820704cfb"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c396c1304de421050b3681ea70f371874b54d41b0151e96109758144c231e30b"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:aad1bff7f666b9598e573815affd666aac6a13a585dde336f843e33350c7fadc"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_31_riscv64.whl", hash = "sha256:656a042550878f12d45752452d47094b7cfe5ad1e9d7b87b5a22ad3ae5ff8015"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:73c4bd4f70294737b5206a3e8e30ccadbf8a60301831c8ea23eec5dbeea1ecfa"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-musllinux_1_2_aarch64.whl", hash = "sha256:43bca78665423cabae77146f2fe7ce55272b6c8d55d82cca83effd42c7e13972"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-musllinux_1_2_i686.whl", hash = "sha256:42d0f20e85e549c870749d0e247f0c10d318a45b7e9676d575d2dcb04a1b2e66"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-musllinux_1_2_x86_64.whl", hash = "sha256:b1be5c35683684d5331b93600c210e8367c254683d8a6df6bd21bd2da3a334fb"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-win32.whl", hash = "sha256:75808f6c38ce7749bb68cc2770161aae5045e6c6f6781a9782e74b93304399df"},
    {file = "rpds_py-2026.5.1-cp315-cp315t-win_amd64.whl", hash = "sha256:90bd6630002a1c7f09e7843dd79f0d24f3d2897cc25a753480917865d14f15b3"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:edf2765d84e42447f112ad877af8fe1db0089aaec5b28e88d6eab45e7fe99cea"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:ad3773236e95f7f33991eb125224b7da66f206504d032a253a02da7e134519fb"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a04df86b3f0fade39ec8fd0e0aab089b1da9fbd2b48df778a57ef96f5e7d38df"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:6142dbd80c4df62a5d899f0d616d417f84e0bc8d32526c8e5589019d75d028a7"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0b35217adefe87f2fe4db7e9766cabe84744bfe9616d9667be18988928c7f2dc"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b95d5e11fc712b752081183a55a244c03cd00570489edd7014d8899f8ceb8162"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:141c9498daf2ace9eda35d2b0e376f9ea8b058d84f2aef4f96fccfd449a2f251"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_31_riscv64.whl", hash = "sha256:6f249f8b860a200ad35193af961183ebe9132710484e6f6ce0cf89fd83c63a9a"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e4abbf391a70be864920858bf360f4fb380577c9a0f732438a1996726e2c195b"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-musllinux_1_2_aarch64.whl", hash = "sha256:c74005a7bb87752acf351c93897ec63ad77a07a0da7ecad9c050e32e7286ba34"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-musllinux_1_2_i686.whl", hash = "sha256:8213afbe8a3a906fb9acb2014423fe3359ee783d0bf90995f70623a3217bfa6c"},
    {file = "rpds_py-2026.5.1-pp311-pypy311_pp73-musllinux_1_2_x86_64.whl", hash = "sha256:8c43a8a973270fd173bf48cdf80bbe66312421cba68d40845034f174f2389049"},
    {file = "rpds_py-2026.5.1.tar.gz", hash = "sha256:07b24fea40541e28570e5b795a4a38fbdcd12550c06bd0748005ecc8116ca256"},
]

[[package]]
name = "send2trash"
version = "2.1.0"
description = "Send file to trash natively under Mac OS X, Windows and Linux"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "send2trash-2.1.0-py3-none-any.whl", hash = "sha256:0da2f112e6d6bb22de6aa6daa7e144831a4febf2a87261451c4ad849fe9a873c"},
    {file = "send2trash-2.1.0.tar.gz", hash = "sha256:1c72b39f09457db3c05ce1d19158c2cbef4c32b8bedd02c155e49282b7ea7459"},
]

[package.extras]
nativelib = ["pyobjc (>=9.0) ; sys_platform == \"darwin\"", "pywin32 (>=305) ; sys_platform == \"win32\""]
test = ["pytest (>=8)"]

[[package]]
name = "setuptools"
version = "81.0.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["dev", "lint"]
files = [
    {file = "setuptools-81.0.0-py3-none-any.whl", hash = "sha256:fdd925d5c5d9f62e4b74b30d6dd7828ce236fd6ed998a08d81de62ce5a6310d6"},
    {file = "setuptools-81.0.0.tar.gz", hash = "sha256:487b53915f52501f0a79ccfd0c02c165ffe06631443a886740b91af4b7a5845a"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.13.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.18.*)", "pytest-mypy"]

[[package]]
name = "six"
version = "1.17.0"
description = "Python 2 and 3 compatibility utilities"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["dev"]
files = [
    {file = "six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274"},
    {file = "six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81"},
]

[[package]]
name = "snowballstemmer"
version = "3.1.1"
description = "This package provides 36 stemmers for 34 languages generated from Snowball algorithms."
optional = false
python-versions = ">=3.3"
groups = ["docs", "lint"]
files = [
    {file = "snowballstemmer-3.1.1-py3-none-any.whl", hash = "sha256:7e207fa178741da09cdee59d3ecec3827ad5f92b1fc5c9ff3755b639f71f5752"},
    {file = "snowballstemmer-3.1.1.tar.gz", hash = "sha256:e07bbc54a0d798fe6010a12398422e62a8bfbba95c394fd0956ef58cb4d3e260"},
]

[[package]]
name = "soupsieve"
version = "2.8.4"
description = "A modern CSS selector implementation for Beautiful Soup."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "soupsieve-2.8.4-py3-none-any.whl", hash = "sha256:e7e6b0769c8f51ed59acab6e994b00621096cfb1c640a7509295987388fbaf65"},
    {file = "soupsieve-2.8.4.tar.gz", hash = "sha256:e121fd02e975c695e4e9e8774a5ee35d74714b59307868dcc5319ad2d9e3328e"},
]

[[package]]
name = "sphinx"
version = "8.1.3"
description = "Python documentation generator"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "sphinx-8.1.3-py3-none-any.whl", hash = "sha256:09719015511837b76bf6e03e42eb7595ac8c2e41eeb9c29c5b755c6b677992a2"},
    {file = "sphinx-8.1.3.tar.gz", hash = "sha256:43c1911eecb0d3e161ad78611bc905d1ad0e523e4ddc202a58a821773dc4c927"},
]

[package.dependencies]
alabaster = ">=0.7.14"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.20,<0.22"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = ">=1.0.7"
sphinxcontrib-devhelp = ">=1.0.6"
sphinxcontrib-htmlhelp = ">=2.0.6"
sphinxcontrib-jsmath = ">=1.0.1"
sphinxcontrib-qthelp = ">=1.0.6"
sphinxcontrib-serializinghtml = ">=1.1.9"
tomli = {version = ">=2", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["sphinxcontrib-websupport"]
lint = ["flake8 (>=6.0)", "mypy (==1.11.1)", "pyright (==1.1.384)", "pytest (>=6.0)", "ruff (==0.6.9)", "sphinx-lint (>=0.9)", "tomli (>=2)", "types-Pillow (==10.2.0.20240822)", "types-Pygments (==2.18.0.20240506)", "types-colorama (==0.4.15.20240311)", "types-defusedxml (==0.7.0.20240218)", "types-docutils (==0.21.0.20241005)", "types-requests (==2.32.0.20240914)", "types-urllib3 (==1.26.25.14)"]
test = ["cython (>=3.0)", "defusedxml (>=0.7.1)", "pytest (>=8.0)", "setuptools (>=70.0)", "typing_extensions (>=4.9)"]

[[package]]
name = "sphinx"
version = "9.0.4"
description = "Python documentation generator"
optional = false
python-versions = ">=3.11"
groups = ["docs"]
markers = "python_version == \"3.11\""
files = [
    {file = "sphinx-9.0.4-py3-none-any.whl", hash = "sha256:5bebc595a5e943ea248b99c13814c1c5e10b3ece718976824ffa7959ff95fffb"},
    {file = "sphinx-9.0.4.tar.gz", hash = "sha256:594ef59d042972abbc581d8baa577404abe4e6c3b04ef61bd7fc2acbd51f3fa3"},
]

[package.dependencies]
alabaster = ">=0.7.14"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.20,<0.23"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
roman-numerals = ">=1.0.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = ">=1.0.7"
sphinxcontrib-devhelp = ">=1.0.6"
sphinxcontrib-htmlhelp = ">=2.0.6"
sphinxcontrib-jsmath = ">=1.0.1"
sphinxcontrib-qthelp = ">=1.0.6"
sphinxcontrib-serializinghtml = ">=1.1.9"

[[package]]
name = "sphinx"
version = "9.1.0"
description = "Python documentation generator"
optional = false
python-versions = ">=3.12"
groups = ["docs"]
markers = "python_version >= \"3.12\""
files = [
    {file = "sphinx-9.1.0-py3-none-any.whl", hash = "sha256:c84fdd4e782504495fe4f2c0b3413d6c2bf388589bb352d439b2a3bb99991978"},
    {file = "sphinx-9.1.0.tar.gz", hash = "sha256:7741722357dd75f8190766926071fed3bdc211c74dd2d7d4df5404da95930ddb"},
]

[package.dependencies]
alabaster = ">=0.7.14"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.21,<0.23"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
roman-numerals = ">=1.0.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = ">=1.0.7"
sphinxcontrib-devhelp = ">=1.0.6"
sphinxcontrib-htmlhelp = ">=2.0.6"
sphinxcontrib-jsmath = ">=1.0.1"
sphinxcontrib-qthelp = ">=1.0.6"
sphinxcontrib-serializinghtml = ">=1.1.9"

[[package]]
name = "sphinx-autoapi"
version = "3.8.0"
description = "Sphinx API documentation generator"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
files = [
    {file = "sphinx_autoapi-3.8.0-py3-none-any.whl", hash = "sha256:245aefdeab85609ae4aa3576b0d99f69676aa6333dda438761bd125755b3c42d"},
    {file = "sphinx_autoapi-3.8.0.tar.gz", hash = "sha256:9f8ac7d43baf28a0831ac0e392fab6a095b875af07e52d135a5f716cc3cf1142"},
]

[package.dependencies]
astroid = ">=3.0"
Jinja2 = "*"
PyYAML = "*"
sphinx = ">=7.4.0"

[[package]]
name = "sphinx-rtd-theme"
version = "3.1.0"
description = "Read the Docs theme for Sphinx"
optional = false
python-versions = ">=3.8"
groups = ["docs"]
files = [
    {file = "sphinx_rtd_theme-3.1.0-py2.py3-none-any.whl", hash = "sha256:1785824ae8e6632060490f67cf3a72d404a85d2d9fc26bce3619944de5682b89"},
    {file = "sphinx_rtd_theme-3.1.0.tar.gz", hash = "sha256:b44276f2c276e909239a4f6c955aa667aaafeb78597923b1c60babc76db78e4c"},
]

[package.dependencies]
docutils = ">0.18,<0.23"
sphinx = ">=6,<10"
sphinxcontrib-jquery = ">=4,<5"

[package.extras]
dev = ["bump2version", "transifex-client", "twine", "wheel"]

[[package]]
name = "sphinxcontrib-applehelp"
version = "2.0.0"
description = "sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help books"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_applehelp-2.0.0-py3-none-any.whl", hash = "sha256:4cd3f0ec4ac5dd9c17ec65e9ab272c9b867ea77425228e68ecf08d6b28ddbdb5"},
    {file = "sphinxcontrib_applehelp-2.0.0.tar.gz", hash = "sha256:2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-devhelp"
version = "2.0.0"
description = "sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp documents"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_devhelp-2.0.0-py3-none-any.whl", hash = "sha256:aefb8b83854e4b0998877524d1029fd3e6879210422ee3780459e28a1f03a8a2"},
    {file = "sphinxcontrib_devhelp-2.0.0.tar.gz", hash = "sha256:411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-htmlhelp"
version = "2.1.0"
description = "sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_htmlhelp-2.1.0-py3-none-any.whl", hash = "sha256:166759820b47002d22914d64a075ce08f4c46818e17cfc9470a9786b759b19f8"},
    {file = "sphinxcontrib_htmlhelp-2.1.0.tar.gz", hash = "sha256:c9e2916ace8aad64cc13a0d233ee22317f2b9025b9cf3295249fa985cc7082e9"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["html5lib", "pytest"]

[[package]]
name = "sphinxcontrib-jquery"
version = "4.1"
description = "Extension to include jQuery on newer Sphinx releases"
optional = false
python-versions = ">=2.7"
groups = ["docs"]
files = [
    {file = "sphinxcontrib-jquery-4.1.tar.gz", hash = "sha256:1620739f04e36a2c779f1a131a2dfd49b2fd07351bf1968ced074365933abc7a"},
    {file = "sphinxcontrib_jquery-4.1-py2.py3-none-any.whl", hash = "sha256:f936030d7d0147dd026a4f2b5a57343d233f1fc7b363f68b3d4f1cb0993878ae"},
]

[package.dependencies]
Sphinx = ">=1.8"

[[package]]
name = "sphinxcontrib-jsmath"
version = "1.0.1"
description = "A sphinx extension which renders display math in HTML via JavaScript"
optional = false
python-versions = ">=3.5"
groups = ["docs"]
files = [
    {file = "sphinxcontrib-jsmath-1.0.1.tar.gz", hash = "sha256:a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8"},
    {file = "sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl", hash = "sha256:2ec2eaebfb78f3f2078e73666b1415417a116cc848b72e5172e596c871103178"},
]

[package.extras]
test = ["flake8", "mypy", "pytest"]

[[package]]
name = "sphinxcontrib-qthelp"
version = "2.0.0"
description = "sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_qthelp-2.0.0-py3-none-any.whl", hash = "sha256:b18a828cdba941ccd6ee8445dbe72ffa3ef8cbe7505d8cd1fa0d42d3f2d5f3eb"},
    {file = "sphinxcontrib_qthelp-2.0.0.tar.gz", hash = "sha256:4fe7d0ac8fc171045be623aba3e2a8f613f8682731f9153bb2e40ece16b9bbab"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["defusedxml (>=0.7.1)", "pytest"]

[[package]]
name = "sphinxcontrib-serializinghtml"
version = "2.0.0"
description = "sphinxcontrib-serializinghtml is a sphinx extension which outputs \"serialized\" HTML files (json and pickle)"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_serializinghtml-2.0.0-py3-none-any.whl", hash = "sha256:6e2cb0eef194e10c27ec0023bfeb25badbbb5868244cf5bc5bdc04e4464bf331"},
    {file = "sphinxcontrib_serializinghtml-2.0.0.tar.gz", hash = "sha256:e9d912827f872c029017a53f0ef2180b327c3f7fd23c87229f7a8e8b70031d4d"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "stack-data"
version = "0.6.3"
description = "Extract data from python stack frames and tracebacks for informative displays"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "stack_data-0.6.3-py3-none-any.whl", hash = "sha256:d5558e0c25a4cb0853cddad3d77da9891a08cb85dd9f9f91b9f8cd66e511e695"},
    {file = "stack_data-0.6.3.tar.gz", hash = "sha256:836a778de4fec4dcd1dcd89ed8abff8a221f58308462e1c4aa2a3cf30148f0b9"},
]

[package.dependencies]
asttokens = ">=2.1.0"
executing = ">=1.2.0"
pure-eval = "*"

[package.extras]
tests = ["cython", "littleutils", "pygments", "pytest", "typeguard"]

[[package]]
name = "stevedore"
version = "5.8.0"
description = "Manage dynamic plugins for Python applications"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "stevedore-5.8.0-py3-none-any.whl", hash = "sha256:88eede9e66ca80e34085b9174e2327da2c61ac91f24f70e41c3ad76e4bb4872b"},
    {file = "stevedore-5.8.0.tar.gz", hash = "sha256:b49867b32ca3016e94100e68dbf26e72aa7b8708d0a3f73c08aeb220370ac715"},
]

[[package]]
name = "terminado"
version = "0.18.1"
description = "Tornado websocket backend for the Xterm.js Javascript terminal emulator library."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "terminado-0.18.1-py3-none-any.whl", hash = "sha256:a4468e1b37bb318f8a86514f65814e1afc977cf29b3992a4500d9dd305dcceb0"},
    {file = "terminado-0.18.1.tar.gz", hash = "sha256:de09f2c4b85de4765f7714688fff57d3e75bad1f909b589fde880460c753fd2e"},
]

[package.dependencies]
ptyprocess = {version = "*", markers = "os_name != \"nt\""}
pywinpty = {version = ">=1.1.0", markers = "os_name == \"nt\""}
tornado = ">=6.1.0"

[package.extras]
docs = ["myst-parser", "pydata-sphinx-theme", "sphinx"]
test = ["pre-commit", "pytest (>=7.0)", "pytest-timeout"]
typing = ["mypy (>=1.6,<2.0)", "traitlets (>=5.11.1)"]

[[package]]
name = "tinycss2"
version = "1.5.1"
description = "A tiny CSS parser"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "tinycss2-1.5.1-py3-none-any.whl", hash = "sha256:3415ba0f5839c062696996998176c4a3751d18b7edaaeeb658c9ce21ec150661"},
    {file = "tinycss2-1.5.1.tar.gz", hash = "sha256:d339d2b616ba90ccce58da8495a78f46e55d4d25f9fd71dfd526f07e7d53f957"},
]

[package.dependencies]
webencodings = ">=0.4"

[package.extras]
doc = ["furo", "sphinx"]
test = ["pytest", "ruff"]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["docs", "lint"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.4.1"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs", "lint", "test"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f8f0fc26ec2cc2b965b7a3b87cd19c5c6b8c5e5f436b984e85f486d652285c30"},
    {file = "tomli-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ab97e64ccda8756376892c53a72bd1f964e519c77236368527f758fbc36a53a"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:96481a5786729fd470164b47cdb3e0e58062a496f455ee41b4403be77cb5a076"},
    {file = "tomli-2.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a881ab208c0baf688221f8cecc5401bd291d67e38a1ac884d6736cbcd8247e9"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:47149d5bd38761ac8be13a84864bf0b7b70bc051806bc3669ab1cbc56216b23c"},
    {file = "tomli-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ec9bfaf3ad2df51ace80688143a6a4ebc09a248f6ff781a9945e51937008fcbc"},
    {file = "tomli-2.4.1-cp311-cp311-win32.whl", hash = "sha256:ff2983983d34813c1aeb0fa89091e76c3a22889ee83ab27c5eeb45100560c049"},
    {file = "tomli-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:5ee18d9ebdb417e384b58fe414e8d6af9f4e7a0ae761519fb50f721de398dd4e"},
    {file = "tomli-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:c2541745709bad0264b7d4705ad453b76ccd191e64aa6f0fc66b69a293a45ece"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:c742f741d58a28940ce01d58f0ab2ea3ced8b12402f162f4d534dfe18ba1cd6a"},
    {file = "tomli-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7f86fd587c4ed9dd76f318225e7d9b29cfc5a9d43de44e5754db8d1128487085"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ff18e6a727ee0ab0388507b89d1bc6a22b138d1e2fa56d1ad494586d61d2eae9"},
    {file = "tomli-2.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:136443dbd7e1dee43c68ac2694fde36b2849865fa258d39bf822c10e8068eac5"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5e262d41726bc187e69af7825504c933b6794dc3fbd5945e41a79bb14c31f585"},
    {file = "tomli-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5cb41aa38891e073ee49d55fbc7839cfdb2bc0e600add13874d048c94aadddd1"},
    {file = "tomli-2.4.1-cp312-cp312-win32.whl", hash = "sha256:da25dc3563bff5965356133435b757a795a17b17d01dbc0f42fb32447ddfd917"},
    {file = "tomli-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:52c8ef851d9a240f11a88c003eacb03c31fc1c9c4ec64a99a0f922b93874fda9"},
    {file = "tomli-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:f758f1b9299d059cc3f6546ae2af89670cb1c4d48ea29c3cacc4fe7de3058257"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:36d2bd2ad5fb9eaddba5226aa02c8ec3fa4f192631e347b3ed28186d43be6b54"},
    {file = "tomli-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:eb0dc4e38e6a1fd579e5d50369aa2e10acfc9cace504579b2faabb478e76941a"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c7f2c7f2b9ca6bdeef8f0fa897f8e05085923eb091721675170254cbc5b02897"},
    {file = "tomli-2.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3c6818a1a86dd6dca7ddcaaf76947d5ba31aecc28cb1b67009a5877c9a64f3f"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d312ef37c91508b0ab2cee7da26ec0b3ed2f03ce12bd87a588d771ae15dcf82d"},
    {file = "tomli-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:51529d40e3ca50046d7606fa99ce3956a617f9b36380da3b7f0dd3dd28e68cb5"},
    {file = "tomli-2.4.1-cp313-cp313-win32.whl", hash = "sha256:2190f2e9dd7508d2a90ded5ed369255980a1bcdd58e52f7fe24b8162bf9fedbd"},
    {file = "tomli-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:8d65a2fbf9d2f8352685bc1364177ee3923d6baf5e7f43ea4959d7d8bc326a36"},
    {file = "tomli-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:4b605484e43cdc43f0954ddae319fb75f04cc10dd80d830540060ee7cd0243cd"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fd0409a3653af6c147209d267a0e4243f0ae46b011aa978b1080359fddc9b6cf"},
    {file = "tomli-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:a120733b01c45e9a0c34aeef92bf0cf1d56cfe81ed9d47d562f9ed591a9828ac"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:559db847dc486944896521f68d8190be1c9e719fced785720d2216fe7022b662"},
    {file = "tomli-2.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01f520d4f53ef97964a240a035ec2a869fe1a37dde002b57ebc4417a27ccd853"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7f94b27a62cfad8496c8d2513e1a222dd446f095fca8987fceef261225538a15"},
    {file = "tomli-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ede3e6487c5ef5d28634ba3f31f989030ad6af71edfb0055cbbd14189ff240ba"},
    {file = "tomli-2.4.1-cp314-cp314-win32.whl", hash = "sha256:3d48a93ee1c9b79c04bb38772ee1b64dcf18ff43085896ea460ca8dec96f35f6"},
    {file = "tomli-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:88dceee75c2c63af144e456745e10101eb67361050196b0b6af5d717254dddf7"},
    {file = "tomli-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:b8c198f8c1805dc42708689ed6864951fd2494f924149d3e4bce7710f8eb5232"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:d4d8fe59808a54658fcc0160ecfb1b30f9089906c50b23bcb4c69eddc19ec2b4"},
    {file = "tomli-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7008df2e7655c495dd12d2a4ad038ff878d4ca4b81fccaf82b714e07eae4402c"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1d8591993e228b0c930c4bb0db464bdad97b3289fb981255d6c9a41aedc84b2d"},
    {file = "tomli-2.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:734e20b57ba95624ecf1841e72b53f6e186355e216e5412de414e3c51e5e3c41"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8a650c2dbafa08d42e51ba0b62740dae4ecb9338eefa093aa5c78ceb546fcd5c"},
    {file = "tomli-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:504aa796fe0569bb43171066009ead363de03675276d2d121ac1a4572397870f"},
    {file = "tomli-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:b1d22e6e9387bf4739fbe23bfa80e93f6b0373a7f1b96c6227c32bef95a4d7a8"},
    {file = "tomli-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:2c1c351919aca02858f740c6d33adea0c5deea37f9ecca1cc1ef9e884a619d26"},
    {file = "tomli-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:eab21f45c7f66c13f2a9e0e1535309cee140182a9cdae1e041d02e47291e8396"},
    {file = "tomli-2.4.1-py3-none-any.whl", hash = "sha256:0d85819802132122da43cb86656f8d1f8c6587d54ae7dcaf30e90533028b49fe"},
    {file = "tomli-2.4.1.tar.gz", hash = "sha256:7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f"},
]

[[package]]
name = "tornado"
version = "6.5.7"
description = "Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "tornado-6.5.7-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:148b2eb15c2c765a50796172c1e499649b35f30d2e3c3d3e15913cfa56bfb163"},
    {file = "tornado-6.5.7-cp39-abi3-macosx_10_9_x86_64.whl", hash = "sha256:9da38de27f1da3b78a966f0dae12b5a1ea9afe72ca805d84ff06508272ddf100"},
    {file = "tornado-6.5.7-cp39-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:8d759e71906ee783f8867b93bf26a265743da4c1e2f4a018464c1ba019862972"},
    {file = "tornado-6.5.7-cp39-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:8a46347a18f23fb92b396beebe0fb78f61dda0cc302445202c16203d8a18848b"},
    {file = "tornado-6.5.7-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:7778b30bef919231265e91c69963ce0f49a1e9c07ac900bbe75b19ce2575ba92"},
    {file = "tornado-6.5.7-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:e726f0c75da7726eec023aa62751ff8878bd2737e34fbdd33b1ae5897d2200f5"},
    {file = "tornado-6.5.7-cp39-abi3-win32.whl", hash = "sha256:f8de3bf12d3efdd0cbe7c8887868198f8a91415e3f29fcf258d9b8eb7b1d9ae4"},
    {file = "tornado-6.5.7-cp39-abi3-win_amd64.whl", hash = "sha256:de942f843533a039ef9fa3d9c88c7cd8a7c94553fb5ad0154270989b3d99a2c4"},
    {file = "tornado-6.5.7-cp39-abi3-win_arm64.whl", hash = "sha256:ff934fce95643af5f11efdae618eaa73d469dc588641e5c8d19295a0c65c4796"},
    {file = "tornado-6.5.7.tar.gz", hash = "sha256:66c513a76cda70d53907bc27cf1447557699c2e95aa48ba27a442ff61c3ddfc2"},
]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "traitlets"
version = "5.15.1"
description = "Traitlets Python configuration system"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "traitlets-5.15.1-py3-none-any.whl", hash = "sha256:770a53705f84b81ac107e83a1b3328ff2dae16094d8fc3cfc004e4b22dfd8e92"},
    {file = "traitlets-5.15.1.tar.gz", hash = "sha256:7b1c07854fe25acb39e009bae49f11b79ff6cbb2f27999104e9110e7a6b53722"},
]

[package.extras]
docs = ["myst-parser", "pydata-sphinx-theme", "sphinx"]
test = ["argcomplete (>=3.0.3)", "mypy (>=1.17.0,<1.19)", "pre-commit", "pytest (>=7.0,<8.2)", "pytest-mock", "pytest-mypy-testing"]

[[package]]
name = "types-grpcio"
version = "1.0.0.20260614"
description = "Typing stubs for grpcio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_grpcio-1.0.0.20260614-py3-none-any.whl", hash = "sha256:050472cb4ef329ae8fe20278c62bc0da5b961aad3dd889cc35f6e0c70d368dae"},
    {file = "types_grpcio-1.0.0.20260614.tar.gz", hash = "sha256:e86d1aabb7e7eedae487c3ac10e010a13d5db1fd350e766562053af557366aab"},
]

[[package]]
name = "types-protobuf"
version = "7.34.1.20260518"
description = "Typing stubs for protobuf"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_protobuf-7.34.1.20260518-py3-none-any.whl", hash = "sha256:a0a5337413347166439c0e07cbc26c6164d091401c6f01b1dfd8cdb966c4dd8f"},
    {file = "types_protobuf-7.34.1.20260518.tar.gz", hash = "sha256:28cfaded25889cb83ebfb63cfb0a43628f0b6f3785767bec17287dc6468795f2"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev", "docs", "lint", "test"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]
markers = {docs = "python_version == \"3.10\"", test = "python_version == \"3.10\""}

[[package]]
name = "tzdata"
version = "2026.2"
description = "Provider of IANA time zone data"
optional = false
python-versions = ">=2"
groups = ["dev"]
files = [
    {file = "tzdata-2026.2-py2.py3-none-any.whl", hash = "sha256:bbe9af844f658da81a5f95019480da3a89415801f6cc966806612cc7169bffe7"},
    {file = "tzdata-2026.2.tar.gz", hash = "sha256:9173fde7d80d9018e02a662e168e5a2d04f87c41ea174b139fbef642eda62d10"},
]

[[package]]
name = "uri-template"
version = "1.3.0"
description = "RFC 6570 URI Template Processor"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "uri-template-1.3.0.tar.gz", hash = "sha256:0e00f8eb65e18c7de20d595a14336e9f337ead580c70934141624b6d1ffdacc7"},
    {file = "uri_template-1.3.0-py3-none-any.whl", hash = "sha256:a44a133ea12d44a0c0f06d7d42a52d71282e77e2f937d8abd5655b8d56fc1363"},
]

[package.extras]
dev = ["flake8", "flake8-annotations", "flake8-bandit", "flake8-bugbear", "flake8-commas", "flake8-comprehensions", "flake8-continuation", "flake8-datetimez", "flake8-docstrings", "flake8-import-order", "flake8-literal", "flake8-modern-annotations", "flake8-noqa", "flake8-pyproject", "flake8-requirements", "flake8-typechecking-import", "flake8-use-fstring", "mypy", "pep8-naming", "types-PyYAML"]

[[package]]
name = "urllib3"
version = "2.7.0"
description = "HTTP library with thread-safe connection pooling, file post, and more."
optional = false
python-versions = ">=3.10"
groups = ["dev", "docs"]
files = [
    {file = "urllib3-2.7.0-py3-none-any.whl", hash = "sha256:9fb4c81ebbb1ce9531cce37674bbc6f1360472bc18ca9a553ede278ef7276897"},
    {file = "urllib3-2.7.0.tar.gz", hash = "sha256:231e0ec3b63ceb14667c67be60f2f2c40a518cb38b03af60abc813da26505f4c"},
]

[package.extras]
brotli = ["brotli (>=1.2.0) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=1.2.0.0) ; platform_python_implementation != \"CPython\""]
h2 = ["h2 (>=4,<5)"]
socks = ["pysocks (>=1.5.6,!=1.5.7,<2.0)"]
zstd = ["backports-zstd (>=1.0.0) ; python_version < \"3.14\""]

[[package]]
name = "wcwidth"
version = "0.8.1"
description = "Measures the displayed width of unicode strings in a terminal"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "wcwidth-0.8.1-py3-none-any.whl", hash = "sha256:f453740b1e4a4f3291faa37944c555d71056c4da08d59809b307ef4feba695c8"},
    {file = "wcwidth-0.8.1.tar.gz", hash = "sha256:faf5b4a5366a72dc49cad48cdf21f52bdf63bdda995178e483ba247ff79089b9"},
]

[[package]]
name = "webcolors"
version = "25.10.0"
description = "A library for working with the color formats defined by HTML and CSS."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "webcolors-25.10.0-py3-none-any.whl", hash = "sha256:032c727334856fc0b968f63daa252a1ac93d33db2f5267756623c210e57a4f1d"},
    {file = "webcolors-25.10.0.tar.gz", hash = "sha256:62abae86504f66d0f6364c2a8520de4a0c47b80c03fc3a5f1815fedbef7c19bf"},
]

[[package]]
name = "webencodings"
version = "0.5.1"
description = "Character encoding aliases for legacy web content"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "webencodings-0.5.1-py2.py3-none-any.whl", hash = "sha256:a0af1213f3c2226497a97e2b3aa01a7e4bee4f403f95be16fc9acd2947514a78"},
    {file = "webencodings-0.5.1.tar.gz", hash = "sha256:b36a1c245f2d304965eb4e0a82848379241dc04b865afcc4aab16748587e1923"},
]

[[package]]
name = "websocket-client"
version = "1.9.0"
description = "WebSocket client for Python with low level API options"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "websocket_client-1.9.0-py3-none-any.whl", hash = "sha256:af248a825037ef591efbf6ed20cc5faa03d3b47b9e5a2230a529eeee1c1fc3ef"},
    {file = "websocket_client-1.9.0.tar.gz", hash = "sha256:9e813624b6eb619999a97dc7958469217c3176312b3a16a4bd1bc7e08a46ec98"},
]

[package.extras]
docs = ["Sphinx (>=6.0)", "myst-parser (>=2.0.0)", "sphinx_rtd_theme (>=1.1.0)"]
optional = ["python-socks", "wsaccel"]
test = ["pytest", "websockets"]

[[package]]
name = "widgetsnbextension"
version = "4.0.15"
description = "Jupyter interactive widgets for Jupyter Notebook"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "widgetsnbextension-4.0.15-py3-none-any.whl", hash = "sha256:8156704e4346a571d9ce73b84bee86a29906c9abfd7223b7228a28899ccf3366"},
    {file = "widgetsnbextension-4.0.15.tar.gz", hash = "sha256:de8610639996f1567952d763a5a41af8af37f2575a41f9852a38f947eb82a3b9"},
]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "1bda39cb633d744840c96991f1bcb283cf0e1faddfa49db451bf942399a31ee8"
````

<!--NI_OSS_SOURCE repo=datastore-python path=poetry.toml sha256=e7e2538881e506da8dde570405c8b73573626e1ed4d97c3a5e65f9226369aa3f bytes=378 -->
## FILE: poetry.toml

- repository: `ni/datastore-python`
- source_path: `poetry.toml`
- sha256: `e7e2538881e506da8dde570405c8b73573626e1ed4d97c3a5e65f9226369aa3f`
- bytes: 378

````toml
[virtualenvs]
in-project = true

[solver]
# Set min-release-age to 2 weeks, same as in https://github.com/ni/python-renovate-config
min-release-age = 14
min-release-age-exclude = [
    "jupyter-server",
    "jupyterlab",
    "ni-python-styleguide",
    "ni-measurements-data-v1-client",
    "ni-measurements-data-v1-proto",
    "ni-protobuf-types",
    "nitypes"
]
````

<!--NI_OSS_SOURCE repo=datastore-python path=pyproject.toml sha256=158610cf5229652d7123dc0c415d120f699dd42f26e5e9bbc4d2d7c05c784f7a bytes=3577 -->
## FILE: pyproject.toml

- repository: `ni/datastore-python`
- source_path: `pyproject.toml`
- sha256: `158610cf5229652d7123dc0c415d120f699dd42f26e5e9bbc4d2d7c05c784f7a`
- bytes: 3577

````toml
[project]
name = "ni.datastore"
version = "2.1.0.dev0"
license = "MIT"
description = "APIs for publishing and retrieving data from NI Measurement Data Services"
authors = [{name = "NI", email = "opensource@ni.com"}]
maintainers = [
  {name = "Johann Scholtz", email = "johann.scholtz@emerson.com"},
  {name = "Joel Dixon", email = "joel.dixon@emerson.com"}
]
readme = "README.md"
keywords = ["datastore"]
classifiers = [
  "Development Status :: 5 - Production/Stable",
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
]
dynamic = ["dependencies"]
requires-python = '>=3.10,<4.0'

[project.urls]
repository = "https://github.com/ni/datastore-python"
documentation = "https://datastorepython.readthedocs.io/en/latest/"

[tool.poetry]
packages = [{include = "ni", from = "src"}]
requires-poetry = '>=2.1,<3.0'

[tool.poetry.dependencies]
python = "^3.10"
protobuf = {version=">=4.21"}
ni-measurements-data-v1-client = { version = ">=1.1.0", allow-prereleases = true }
ni-measurements-metadata-v1-client = { version = ">=1.0.0" }
ni-protobuf-types = { version = ">=1.2.0", allow-prereleases = true }
hightime = { version = ">=1.0.0" }

[tool.poetry.group.dev.dependencies]
types-grpcio = ">=1.0"
types-protobuf = ">=4.21"
ipykernel = ">=6.0"
plotly = ">=5.0"
nbformat = ">=4.2.0"
ipython = ">=7.0"
jupyter = ">=1.0"
datastore-utilities = { path = "./utilities", develop = true }

[tool.poetry.group.lint.dependencies]
bandit = { version = ">=1.7", extras = ["toml"] }
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
pyright = { version = ">=1.1.400", extras = ["nodejs"] }

[tool.poetry.group.test.dependencies]
pytest = ">=7.2"
pytest-cov = ">=4.0"
pytest-doctestplus = ">=1.4"
pytest-mock = ">=3.0"

[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
# The latest Sphinx requires a recent Python version.
Sphinx = [
  { version = ">=8.1", python = ">=3.10,<3.11" },
  { version = ">=8.2", python = "^3.11" },
]
sphinx-rtd-theme = ">=1.0.0"
sphinx-autoapi = ">=1.8.4"
myst-parser = ">=4.0.1"
toml = ">=0.10.2"

[build-system]
requires = ["poetry-core>=1.8"]
build-backend = "poetry.core.masonry.api"


[tool.bandit]
skips = [
  "B101", # assert_used
]

[tool.ni-python-styleguide]
extend_exclude = "docs,examples,utilities"

[tool.black]
extend-exclude = 'docs/|examples/|_pb2(_grpc)?\.(py|pyi)$'
line-length = 100

[tool.mypy]
mypy_path = "src"
files = "."
namespace_packages = true
strict = true
explicit_package_bases = true
exclude = ["docs", "examples", "utilities"]

[tool.pyright]
include = ["src/", "tests/"]
exclude = ["**/*_pb2_grpc.py", "**/*_pb2_grpc.pyi", "**/*_pb2.py", "**/*_pb2.pyi", "src/ni/measurements/data/v1/**/__init__.py*"]

[tool.pytest.ini_options]
addopts = "--doctest-modules --doctest-plus --strict-markers"
testpaths = ["tests"]
norecursedirs = [".venv"]
filterwarnings = [
  "ignore:cannot collect test class.*because it has a __init__ constructor:pytest.PytestCollectionWarning",
]
````

<!--NI_OSS_SOURCE repo=datastore-python path=README.md sha256=a4b2c642eb6a08c98aac26d1e3a86222795999f8f404679ddb283e9a055d0903 bytes=1362 -->
## FILE: README.md

- repository: `ni/datastore-python`
- source_path: `README.md`
- sha256: `a4b2c642eb6a08c98aac26d1e3a86222795999f8f404679ddb283e9a055d0903`
- bytes: 1362

````markdown
# Table of Contents

- [Table of Contents](#table-of-contents)
- [Measurement Data Services API for Python](#measurement-data-services-api-for-python)
- [About](#about)
  - [Operating System Support](#operating-system-support)
  - [Python Version Support](#python-version-support)
  - [Installation](#installation)

# Measurement Data Services API for Python

`datastore-python` contains Python code for writing to and reading from
NI Measurement Data Store. It will include examples of how to use the Python API.

# About

`ni.datastore` is the main Python package in this repo that
provides APIs for publishing and retrieving data from the NI
Measurement Data Services

NI created and supports this package.

## Operating System Support

`ni.datastore` supports Windows and Linux operating systems.

## Python Version Support

`ni.datastore` supports CPython 3.10+.

## Installation

As a prerequisite to using the `ni.datastore` module, you must install Measurement Data Services
Software 2026 Q3 or later on your system. You can download and install this software using
[NI Package Manager](https://www.ni.com/en/support/downloads/software-products/download.package-manager.html).

You can directly install the `ni.datastore` package using `pip` or by listing it as a
dependency in your project's `pyproject.toml` file.
````

<!--NI_OSS_SOURCE repo=datastore-python path=renovate.json sha256=60909f4835c7ec398d2e67ef80b54755d8288f94e525c80d00865267c91128c2 bytes=153 -->
## FILE: renovate.json

- repository: `ni/datastore-python`
- source_path: `renovate.json`
- sha256: `60909f4835c7ec398d2e67ef80b54755d8288f94e525c80d00865267c91128c2`
- bytes: 153

````json
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "extends": [
        "local>ni/python-renovate-config:recommended"
    ]
}
````

<!--NI_OSS_SOURCE repo=datastore-python path=SECURITY.md sha256=902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11 bytes=1330 -->
## FILE: SECURITY.md

- repository: `ni/datastore-python`
- source_path: `SECURITY.md`
- sha256: `902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11`
- bytes: 1330

````markdown
<!-- Begin NI SECURITY.md V1.0 -->

# Security

NI views the security of our software products as an important part of our commitment to our users.  This includes source code repositories managed through the [NI](https://github.com/ni) GitHub organization.

## Reporting Security Issues

We encourage you to report security vulnerabilities to us privately so we can follow the principle of [Coordinated Vulnerability Disclosure (CVD)](https://vuls.cert.org/confluence/display/CVD).  This allows us time to thoroughly investigate security issues and publicly disclose them when appropriate.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them by sending an email to [security@ni.com](mailto:security@ni.com) with sufficient details about the type of issue, the impact of the issue, and how to reproduce the issue.  You may use the [NI PGP key](https://www.ni.com/en/support/security/pgp.html) to encrypt any sensitive communications you send to us. When you notify us of a potential security issue, our remediation process includes acknowledging receipt and coordinating any necessary response activities with you. 

## Learn More

To learn more about NI Security, please see [https://ni.com/security](https://ni.com/security)

<!-- End NI SECURITY.md -->
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/__init__.py sha256=da8a6567418c15bf9173547307904d689b07b2986e43cd5a76ef636e412bc446 bytes=61 -->
## FILE: src/ni/datastore/__init__.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/__init__.py`
- sha256: `da8a6567418c15bf9173547307904d689b07b2986e43cd5a76ef636e412bc446`
- bytes: 61

````python
"""Public API for accessing the NI Data/Metadata Stores."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/__init__.py sha256=f58763aceb62989eeff382a558340d52a150feef5fd7210249ef0c5196f2118a bytes=1008 -->
## FILE: src/ni/datastore/data/__init__.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/__init__.py`
- sha256: `f58763aceb62989eeff382a558340d52a150feef5fd7210249ef0c5196f2118a`
- bytes: 1008

````python
"""Public API for accessing the NI Data Store."""

from ni.datastore.data._data_store_client import DataStoreClient
from ni.datastore.data._types._error_information import ErrorInformation
from ni.datastore.data._types._outcome import Outcome
from ni.datastore.data._types._published_condition import PublishedCondition
from ni.datastore.data._types._published_measurement import PublishedMeasurement
from ni.datastore.data._types._step import Step
from ni.datastore.data._types._test_result import TestResult

__all__ = [
    "DataStoreClient",
    "ErrorInformation",
    "Outcome",
    "PublishedCondition",
    "PublishedMeasurement",
    "Step",
    "TestResult",
]

# Hide that it was not defined in this top-level package
DataStoreClient.__module__ = __name__
ErrorInformation.__module__ = __name__
Outcome.__module__ = __name__
PublishedCondition.__module__ = __name__
PublishedMeasurement.__module__ = __name__
Step.__module__ = __name__
TestResult.__module__ = __name__
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_data_store_client.py sha256=1b3455c439159e7ff02989802e8b4cf5ce5413312f8d79976276b4c6f3f8f8d6 bytes=26907 -->
## FILE: src/ni/datastore/data/_data_store_client.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_data_store_client.py`
- sha256: `1b3455c439159e7ff02989802e8b4cf5ce5413312f8d79976276b4c6f3f8f8d6`
- bytes: 26907

````python
"""Data store client for publishing and reading data."""

from __future__ import annotations

import logging
import sys
from collections.abc import Iterable, Sequence
from threading import Lock
from types import TracebackType
from typing import overload, Type, TYPE_CHECKING, TypeVar

import hightime as ht
from grpc import Channel
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurements.data.v1.client import DataStoreClient as DataStoreServiceClient
from ni.measurements.data.v1.data_store_service_pb2 import (
    CreateStepRequest,
    CreateTestResultRequest,
    GetConditionRequest,
    GetMeasurementRequest,
    GetStepRequest,
    GetTestResultRequest,
    PublishConditionBatchRequest,
    PublishConditionRequest,
    PublishMeasurementBatchRequest,
    PublishMeasurementRequest,
    QueryConditionsRequest,
    QueryMeasurementsRequest,
    QueryStepsRequest,
    QueryTestResultsRequest,
    ReadConditionValueRequest,
    ReadMeasurementValueRequest,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_to_protobuf,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool

from ni.datastore.data._grpc_conversion import (
    convert_measurement_timestamp_to_protobuf,
    convert_read_condition_response_from_protobuf,
    convert_read_measurement_response_from_protobuf,
    populate_publish_condition_batch_request_values,
    populate_publish_condition_request_value,
    populate_publish_measurement_batch_request_values,
    populate_publish_measurement_request_value,
)
from ni.datastore.data._types._error_information import ErrorInformation
from ni.datastore.data._types._outcome import Outcome
from ni.datastore.data._types._published_condition import PublishedCondition
from ni.datastore.data._types._published_measurement import PublishedMeasurement
from ni.datastore.data._types._step import Step
from ni.datastore.data._types._test_result import TestResult

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

TRead = TypeVar("TRead")

_logger = logging.getLogger(__name__)


class DataStoreClient:
    """Data store client for publishing and reading data."""

    __slots__ = (
        "_closed",
        "_discovery_client",
        "_grpc_channel",
        "_grpc_channel_pool",
        "_data_store_client",
        "_data_store_client_lock",
    )

    _DATA_STORE_CLIENT_CLOSED_ERROR = (
        "This DataStoreClient has been closed. Create a new DataStoreClient for further "
        "interaction with the data store."
    )

    _closed: bool
    _discovery_client: DiscoveryClient | None
    _grpc_channel: Channel | None
    _grpc_channel_pool: GrpcChannelPool | None
    _data_store_client: DataStoreServiceClient | None
    _data_store_client_lock: Lock

    def __init__(
        self,
        discovery_client: DiscoveryClient | None = None,
        grpc_channel: Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ) -> None:
        """Initialize the DataStoreClient.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional data store gRPC channel. Providing this channel will bypass
                discovery service resolution of the data store.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        """
        self._discovery_client = discovery_client
        self._grpc_channel = grpc_channel
        self._grpc_channel_pool = grpc_channel_pool

        self._data_store_client = None

        self._data_store_client_lock = Lock()

        self._closed = False

    def __enter__(self) -> Self:
        """Enter the runtime context of the data store client."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the runtime context of the data store client."""
        self.close()

    def close(self) -> None:
        """Close the data store client and clean up resources that it owns."""
        self._closed = True

        with self._data_store_client_lock:
            if self._data_store_client is not None:
                self._data_store_client.close()
                self._data_store_client = None

    def publish_condition(
        self,
        name: str,
        condition_type: str,
        value: object,
        step_id: str,
    ) -> str:
        """Publish a condition value to the data store.

        Args:
            name: An identifier describing the condition value.
                For example, "Voltage" or "Temperature".

            condition_type: The type of this condition. For example, "Upper Limit",
                "Environment", or "Setup".

            value: The single value for this condition to publish on the test
                step. This should be a scalar value that can be converted to
                the appropriate protobuf scalar type.

            step_id: The ID of the step associated with this condition. This
                value is expected to be a parsable GUID.

        Returns:
            str: The condition id - the unique ID of the condition for
                referencing in queries
        """
        publish_request = PublishConditionRequest(
            name=name,
            condition_type=condition_type,
            step_id=step_id,
        )
        populate_publish_condition_request_value(publish_request, value)
        publish_response = self._get_data_store_client().publish_condition(publish_request)
        return publish_response.condition_id

    def publish_condition_batch(
        self, name: str, condition_type: str, values: object, step_id: str
    ) -> str:
        """Publish a batch of N values for a condition to the data store.

        Args:
            name: An identifier describing the condition values.
                For example, "Voltage" or "Temperature".

            condition_type: The type of this condition. For example, "Upper Limit",
                "Environment", or "Setup".

            values: The values for this condition across all publishes on the
                test step. This should be a Vector of N values.

            step_id: The ID of the step associated with this batch of condition
                values. This value is expected to be a parsable GUID.

        Returns:
            str: The condition id - the unique ID of the condition for
                referencing in queries
        """
        publish_request = PublishConditionBatchRequest(
            name=name,
            condition_type=condition_type,
            step_id=step_id,
        )
        populate_publish_condition_batch_request_values(publish_request, values)
        publish_response = self._get_data_store_client().publish_condition_batch(publish_request)
        return publish_response.condition_id

    def publish_measurement(
        self,
        name: str,
        value: object,  # More strongly typed Union[bool, AnalogWaveform] can be used if needed
        step_id: str,
        timestamp: ht.datetime | None = None,
        outcome: Outcome = Outcome.UNSPECIFIED,
        error_information: ErrorInformation | None = None,
        hardware_item_ids: Iterable[str] = tuple(),
        test_adapter_ids: Iterable[str] = tuple(),
        software_item_ids: Iterable[str] = tuple(),
        notes: str = "",
    ) -> str:
        """Publish a single measurement value associated with a test step.

        Args:
            name: The name used for associating/grouping
                conceptually alike measurements across multiple publish
                iterations. For example, "Temperature" can be used for
                associating temperature readings across multiple iterations.

            value: The value of the measurement being published. Supported types:

                - Scalar: Single float, int, str or boolean
                - Vector: Array of float, int, str or boolean values
                - DoubleAnalogWaveform: Analog waveform with double precision
                - DoubleXYData: XY coordinate data with double precision
                - I16AnalogWaveform: Analog waveform with 16-bit integer precision
                - DoubleComplexWaveform: Complex waveform with double precision
                - I16ComplexWaveform: Complex waveform with 16-bit integer precision
                - DoubleSpectrum: Frequency spectrum data with double precision
                - DigitalWaveform: Digital waveform data

            step_id: The ID of the step associated with this measurement. This
                value is expected to be a parsable GUID.

            timestamp: The timestamp of the measurement. If None, no timestamp
                will be specified.

            outcome: The outcome of the measurement (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).

            error_information: Error or exception information in case of
                measurement failure.

            hardware_item_ids: The IDs of the hardware items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            test_adapter_ids: The IDs of the test adapters associated with this
                measurement. These values are expected to be parsable GUIDs or
                aliases.

            software_item_ids: The IDs of the software items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            notes: Any notes to be associated with the captured measurement.

        Returns:
            str: The published measurement id.
        """
        publish_request = PublishMeasurementRequest(
            name=name,
            step_id=step_id,
            outcome=outcome.to_protobuf(),
            error_information=(
                error_information.to_protobuf() if error_information is not None else None
            ),
            hardware_item_ids=hardware_item_ids,
            test_adapter_ids=test_adapter_ids,
            software_item_ids=software_item_ids,
            notes=notes,
            timestamp=convert_measurement_timestamp_to_protobuf(timestamp),
        )
        populate_publish_measurement_request_value(publish_request, value)
        publish_response = self._get_data_store_client().publish_measurement(publish_request)
        return publish_response.measurement_id

    def publish_measurement_batch(
        self,
        name: str,
        values: object,
        step_id: str,
        timestamps: Iterable[ht.datetime] = tuple(),
        outcomes: Iterable[Outcome] = tuple(),
        error_information: Iterable[ErrorInformation] = tuple(),
        hardware_item_ids: Iterable[str] = tuple(),
        test_adapter_ids: Iterable[str] = tuple(),
        software_item_ids: Iterable[str] = tuple(),
        notes: str = "",
    ) -> Sequence[str]:
        """Publish multiple measurements at once for parametric sweeps.

        Args:
            name: The name used for associating/grouping
                conceptually alike measurements across multiple publish
                iterations. For example, "Temperature" can be used for
                associating temperature readings across multiple iterations.

            values: The values of the measurement being published
                across N iterations.

            step_id: The ID of the step associated with this measurement. This
                value is expected to be a parsable GUID.

            timestamps: The timestamps corresponding to the N iterations of
                batched measurement being published. Can be empty (no timestamp
                info), single value (applied to all), or N values (one per
                measurement).

            outcomes: The outcomes corresponding to the N iterations of batched
                measurement being published. Can be empty (no outcome info),
                single value (applied to all), or N values (one per
                measurement).

            error_information: The error information corresponding to the N
                iterations of batched measurement being published. Can be empty
                (no error info), single value (applied to all), or N values
                (one per measurement).

            hardware_item_ids: The IDs of the hardware items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            test_adapter_ids: The IDs of the test adapters associated with this
                measurement. These values are expected to be parsable GUIDs or
                aliases.

            software_item_ids: The IDs of the software items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            notes: Any notes to be associated with the published measurements.

        Returns:
            Sequence[str]: The IDs of the corresponding PublishedMeasurements. A single
            ID will be returned when publishing scalar measurement values.
            N IDs will be returned when publishing (N) non-scalar measurement values.
        """
        publish_request = PublishMeasurementBatchRequest(
            name=name,
            step_id=step_id,
            timestamps=[hightime_datetime_to_protobuf(ts) for ts in timestamps],
            outcomes=[outcome.to_protobuf() for outcome in outcomes],
            error_information=(
                [ei.to_protobuf() for ei in (error_information or [])] if error_information else []
            ),
            hardware_item_ids=hardware_item_ids,
            test_adapter_ids=test_adapter_ids,
            software_item_ids=software_item_ids,
            notes=notes,
        )
        populate_publish_measurement_batch_request_values(publish_request, values)
        publish_response = self._get_data_store_client().publish_measurement_batch(publish_request)
        return publish_response.measurement_ids

    @overload
    def read_condition_value(
        self,
        read_source: PublishedCondition,
        expected_type: Type[TRead],
    ) -> TRead: ...

    @overload
    def read_condition_value(
        self,
        read_source: PublishedCondition,
    ) -> object: ...

    def read_condition_value(
        self,
        read_source: PublishedCondition,
        expected_type: Type[TRead] | None = None,
    ) -> TRead | object:
        """Read data published to the data store.

        Args:
            read_source: The source from which to read data (PublishedCondition).

            expected_type: Optional type to validate the returned data against.
                If provided, a TypeError will be raised if the actual data type
                doesn't match.

        Returns:
            The data retrieved from the data store. The return type depends on
            what was originally published:
            - Scalar conditions return as Vectors
            - Other types are returned as originally published
            If expected_type is specified, the return value is guaranteed to be
            of that type.

        Raises:
            TypeError: If expected_type is provided and the actual data type
                doesn't match.
        """
        read_value = self._read_condition(read_source)
        if expected_type is not None and not isinstance(read_value, expected_type):
            raise TypeError(f"Expected type {expected_type}, got {type(read_value)}")

        return read_value

    @overload
    def read_measurement_value(
        self,
        read_source: PublishedMeasurement,
        expected_type: Type[TRead],
    ) -> TRead: ...

    @overload
    def read_measurement_value(
        self,
        read_source: PublishedMeasurement,
    ) -> object: ...

    def read_measurement_value(
        self,
        read_source: PublishedMeasurement,
        expected_type: Type[TRead] | None = None,
    ) -> TRead | object:
        """Read data published to the data store.

        Args:
            read_source: The source from which to read data (PublishedMeasurement).

            expected_type: Optional type to validate the returned data against.
                If provided, a TypeError will be raised if the actual data type
                doesn't match.

        Returns:
            The data retrieved from the data store. The return type depends on
            what was originally published:
            - Scalar measurements return as Vectors
            - Other types are returned as originally published
            If expected_type is specified, the return value is guaranteed to be
            of that type.

        Raises:
            TypeError: If expected_type is provided and the actual data type
                doesn't match.
        """
        read_value = self._read_measurement(read_source)
        if expected_type is not None and not isinstance(read_value, expected_type):
            raise TypeError(f"Expected type {expected_type}, got {type(read_value)}")

        return read_value

    def create_step(self, step: Step) -> str:
        """Create a new step in the data store.

        A step is owned by a test result and is a logical grouping of published
        measurements and conditions. All measurements and conditions must be
        associated with a step.

        Args:
            step: The metadata of the step to be created.

        Returns:
            str: The identifier of the created step.
        """
        create_request = CreateStepRequest(step=step.to_protobuf())
        create_response = self._get_data_store_client().create_step(create_request)
        return create_response.step_id

    def get_step(self, step_id: str) -> Step:
        """Get the step associated with the given identifier.

        Args:
            step_id: The identifier of the desired step.

        Returns:
            Step: The metadata of the requested step.
        """
        get_request = GetStepRequest(step_id=step_id)
        get_response = self._get_data_store_client().get_step(get_request)
        return Step.from_protobuf(get_response.step)

    def get_measurement(self, measurement_id: str) -> PublishedMeasurement:
        """Get the measurement associated with the given identifier.

        Args:
            measurement_id: The identifier of the desired measurement.

        Returns:
            PublishedMeasurement: The metadata of the requested measurement.
        """
        get_request = GetMeasurementRequest(measurement_id=measurement_id)
        get_response = self._get_data_store_client().get_measurement(get_request)
        return PublishedMeasurement.from_protobuf(get_response.published_measurement)

    def get_condition(self, condition_id: str) -> PublishedCondition:
        """Get the condition associated with the given identifier.

        Args:
            condition_id: The identifier of the desired condition.

        Returns:
            PublishedCondition: The metadata of the requested condition.
        """
        get_request = GetConditionRequest(condition_id=condition_id)
        get_response = self._get_data_store_client().get_condition(get_request)
        return PublishedCondition.from_protobuf(get_response.published_condition)

    def create_test_result(self, test_result: TestResult) -> str:
        """Create a test result object for publishing measurements.

        Once a test result is created, you can publish an arbitrary number of
        measurements and conditions to a step which is owned by the test result.

        Args:
            test_result: The metadata of the test result to be created.

        Returns:
            str: The test result ID. Generated if not specified in the request.
        """
        create_request = CreateTestResultRequest(test_result=test_result.to_protobuf())
        create_response = self._get_data_store_client().create_test_result(create_request)
        return create_response.test_result_id

    def get_test_result(self, test_result_id: str) -> TestResult:
        """Get the test result associated with the given identifier.

        Args:
            test_result_id: The ID of the desired test result. This value is
                expected to be a parsable GUID.

        Returns:
            TestResult: The TestResult object that corresponds to the
                requested ID.
        """
        get_request = GetTestResultRequest(test_result_id=test_result_id)
        get_response = self._get_data_store_client().get_test_result(get_request)
        return TestResult.from_protobuf(get_response.test_result)

    def query_conditions(self, odata_query: str = "") -> Sequence[PublishedCondition]:
        """Query conditions using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all conditions. $expand,
                $count, and $select are not supported. For more information,
                see https://learn.microsoft.com/en-us/odata/concepts/
                queryoptions-overview.

        Returns:
            Sequence[PublishedCondition]: The list of matching conditions. Each
                item contains an id for retrieving the condition
                measurements, as well as the metadata associated with the
                condition.
        """
        query_request = QueryConditionsRequest(odata_query=odata_query)
        query_response = self._get_data_store_client().query_conditions(query_request)
        return [
            PublishedCondition.from_protobuf(published_condition)
            for published_condition in query_response.published_conditions
        ]

    def query_measurements(self, odata_query: str = "") -> Sequence[PublishedMeasurement]:
        """Query measurements using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all measurements.
                $expand, $count, and $select are not supported. For more
                information, see https://learn.microsoft.com/en-us/odata/
                concepts/queryoptions-overview.

        Returns:
            Sequence[PublishedMeasurement]: The list of matching measurements.
                Each item contains an id for retrieving the measurement, as
                well as the metadata associated with the measurement.
        """
        query_request = QueryMeasurementsRequest(odata_query=odata_query)
        query_response = self._get_data_store_client().query_measurements(query_request)
        return [
            PublishedMeasurement.from_protobuf(published_measurement)
            for published_measurement in query_response.published_measurements
        ]

    def query_test_results(self, odata_query: str = "") -> Sequence[TestResult]:
        """Query test results using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all test results.
                $expand, $count, and $select are not supported. For more
                information, see https://learn.microsoft.com/en-us/odata/
                concepts/queryoptions-overview.

        Returns:
            Sequence[TestResult]: The list of matching test results. Each
                item contains the metadata associated with the test result,
                including test result ID, name, timestamps, and other
                properties.
        """
        query_request = QueryTestResultsRequest(odata_query=odata_query)
        query_response = self._get_data_store_client().query_test_results(query_request)
        return [
            TestResult.from_protobuf(test_result) for test_result in query_response.test_results
        ]

    def query_steps(self, odata_query: str = "") -> Sequence[Step]:
        """Query for steps matching the given OData query.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all steps. $expand,
                $count, and $select are not supported. For more information,
                see https://learn.microsoft.com/en-us/odata/concepts/
                queryoptions-overview.

        Returns:
            Sequence[Step]: The list of steps that match the query.
        """
        query_request = QueryStepsRequest(odata_query=odata_query)
        query_response = self._get_data_store_client().query_steps(query_request)
        return [Step.from_protobuf(step) for step in query_response.steps]

    def _get_data_store_client(self) -> DataStoreServiceClient:
        if self._closed:
            raise RuntimeError(self._DATA_STORE_CLIENT_CLOSED_ERROR)

        if self._data_store_client is None:
            with self._data_store_client_lock:
                if self._data_store_client is None:
                    self._data_store_client = self._instantiate_data_store_client()
        return self._data_store_client

    def _instantiate_data_store_client(self) -> DataStoreServiceClient:
        return DataStoreServiceClient(
            discovery_client=self._discovery_client,
            grpc_channel=self._grpc_channel,
            grpc_channel_pool=self._grpc_channel_pool,
        )

    def _read_measurement(self, published_measurement: PublishedMeasurement) -> object:
        request = ReadMeasurementValueRequest(measurement_id=published_measurement.id)
        response = self._get_data_store_client().read_measurement_value(request)
        return convert_read_measurement_response_from_protobuf(response)

    def _read_condition(self, published_condition: PublishedCondition) -> object:
        request = ReadConditionValueRequest(condition_id=published_condition.id)
        response = self._get_data_store_client().read_condition_value(request)
        return convert_read_condition_response_from_protobuf(response)
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_grpc_conversion.py sha256=584684ab193b1855282d723084f26948fb0c0cc3f5b612d11c6ba31eff23940e bytes=15706 -->
## FILE: src/ni/datastore/data/_grpc_conversion.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_grpc_conversion.py`
- sha256: `584684ab193b1855282d723084f26948fb0c0cc3f5b612d11c6ba31eff23940e`
- bytes: 15706

````python
"""Helper methods to convert between python and protobuf types."""

from __future__ import annotations

import logging
from itertools import chain
from typing import Any, Callable, cast, Iterable

import hightime as ht
import numpy as np
from ni.measurements.data.v1.data_store_service_pb2 import (
    PublishConditionBatchRequest,
    PublishConditionRequest,
    PublishMeasurementBatchRequest,
    PublishMeasurementRequest,
    ReadConditionValueResponse,
    ReadMeasurementValueResponse,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_to_protobuf,
)
from ni.protobuf.types.precision_timestamp_pb2 import PrecisionTimestamp
from ni.protobuf.types.scalar_conversion import scalar_to_protobuf
from ni.protobuf.types.vector_conversion import vector_from_protobuf, vector_to_protobuf
from ni.protobuf.types.waveform_conversion import (
    digital_waveform_from_protobuf,
    digital_waveform_to_protobuf,
    float64_analog_waveform_from_protobuf,
    float64_analog_waveform_to_protobuf,
    float64_complex_waveform_from_protobuf,
    float64_complex_waveform_to_protobuf,
    float64_spectrum_from_protobuf,
    float64_spectrum_to_protobuf,
    int16_analog_waveform_from_protobuf,
    int16_analog_waveform_to_protobuf,
    int16_complex_waveform_from_protobuf,
    int16_complex_waveform_to_protobuf,
)
from ni.protobuf.types.xydata_conversion import (
    float64_xydata_from_protobuf,
    float64_xydata_to_protobuf,
)
from nitypes.complex import ComplexInt32DType
from nitypes.scalar import Scalar
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform, ComplexWaveform, DigitalWaveform, Spectrum
from nitypes.xy_data import XYData

_logger = logging.getLogger(__name__)


def _copy_batch_values(
    repeated_field: Any,
    batch_values: Iterable[object],
    is_supported: Callable[[object], bool],
    convert_value: Callable[[Any], Any],
    error_message: str,
) -> None:
    for value in batch_values:
        if not is_supported(value):
            raise TypeError(error_message)
        repeated_field.add().CopyFrom(convert_value(value))


def _populate_vector_batch_values(
    publish_request: PublishMeasurementBatchRequest, values: Iterable[object]
) -> None:
    _copy_batch_values(
        publish_request.vector_values.vectors,
        values,
        lambda value: isinstance(value, Vector),
        vector_to_protobuf,
        "Unsupported iterable: all values must be Vector.",
    )


def _populate_analog_waveform_batch_values(
    publish_request: PublishMeasurementBatchRequest,
    first_value: AnalogWaveform[Any],
    values: Iterable[object],
) -> None:
    if first_value.dtype == np.float64:
        _copy_batch_values(
            publish_request.double_analog_waveform_values.waveforms,
            values,
            lambda value: isinstance(value, AnalogWaveform) and value.dtype == np.float64,
            float64_analog_waveform_to_protobuf,
            "Unsupported iterable: all values must be float64 AnalogWaveform.",
        )
        return
    elif first_value.dtype == np.int16:
        _copy_batch_values(
            publish_request.i16_analog_waveform_values.waveforms,
            values,
            lambda value: isinstance(value, AnalogWaveform) and value.dtype == np.int16,
            int16_analog_waveform_to_protobuf,
            "Unsupported iterable: all values must be int16 AnalogWaveform.",
        )
        return
    raise TypeError(f"Unsupported AnalogWaveform dtype: {first_value.dtype}")


def _populate_complex_waveform_batch_values(
    publish_request: PublishMeasurementBatchRequest,
    first_value: ComplexWaveform[Any],
    values: Iterable[object],
) -> None:
    if first_value.dtype == np.complex128:
        _copy_batch_values(
            publish_request.double_complex_waveform_values.waveforms,
            values,
            lambda value: isinstance(value, ComplexWaveform) and value.dtype == np.complex128,
            float64_complex_waveform_to_protobuf,
            "Unsupported iterable: all values must be complex128 ComplexWaveform.",
        )
        return
    if first_value.dtype == ComplexInt32DType:
        _copy_batch_values(
            publish_request.i16_complex_waveform_values.waveforms,
            values,
            lambda value: isinstance(value, ComplexWaveform) and value.dtype == ComplexInt32DType,
            int16_complex_waveform_to_protobuf,
            "Unsupported iterable: all values must be ComplexWaveform with ComplexInt32DType.",
        )
        return
    raise TypeError(f"Unsupported ComplexWaveform dtype: {first_value.dtype}")


def _populate_spectrum_batch_values(
    publish_request: PublishMeasurementBatchRequest,
    first_value: Spectrum[Any],
    values: Iterable[object],
) -> None:
    if first_value.dtype != np.float64:
        raise TypeError(f"Unsupported Spectrum dtype: {first_value.dtype}")

    _copy_batch_values(
        publish_request.double_spectrum_values.waveforms,
        values,
        lambda value: isinstance(value, Spectrum) and value.dtype == np.float64,
        float64_spectrum_to_protobuf,
        "Unsupported iterable: all values must be float64 Spectrum.",
    )


def _populate_digital_waveform_batch_values(
    publish_request: PublishMeasurementBatchRequest, values: Iterable[object]
) -> None:
    _copy_batch_values(
        publish_request.digital_waveform_values.waveforms,
        values,
        lambda value: isinstance(value, DigitalWaveform),
        digital_waveform_to_protobuf,
        "Unsupported iterable: all values must be DigitalWaveform.",
    )


def _populate_xydata_batch_values(
    publish_request: PublishMeasurementBatchRequest,
    first_value: XYData[Any],
    values: Iterable[object],
) -> None:
    if first_value.dtype != np.float64:
        raise TypeError(f"Unsupported XYData dtype: {first_value.dtype}")

    _copy_batch_values(
        publish_request.x_y_data_values.x_y_data,
        values,
        lambda value: isinstance(value, XYData) and value.dtype == np.float64,
        float64_xydata_to_protobuf,
        "Unsupported iterable: all values must be float64 XYData.",
    )


def populate_publish_condition_request_value(
    publish_request: PublishConditionRequest, value: object
) -> None:
    """Assign a value to the scalar member of PublishConditionRequest."""
    if isinstance(value, bool):
        publish_request.scalar.bool_value = value
    elif isinstance(value, int):
        publish_request.scalar.sint32_value = value
    elif isinstance(value, float):
        publish_request.scalar.double_value = value
    elif isinstance(value, str):
        publish_request.scalar.string_value = value
    elif isinstance(value, Scalar):
        publish_request.scalar.CopyFrom(scalar_to_protobuf(value))
    else:
        raise TypeError(
            f"Unsupported condition value type: {type(value)}. Please consult the documentation."
        )


def populate_publish_condition_batch_request_values(
    publish_request: PublishConditionBatchRequest, values: object
) -> None:
    """Assign a value to the scalar_values vector member of PublishConditionBatchRequest."""
    if isinstance(values, Vector):
        publish_request.scalar_values.CopyFrom(vector_to_protobuf(values))
    elif isinstance(values, Iterable):
        values_iterator = iter(values)
        try:
            first_value = next(values_iterator)
        except StopIteration as exc:
            raise ValueError("Cannot publish an empty Iterable.") from exc

        all_values = chain([first_value], values_iterator)
        try:
            vector = Vector(cast(Iterable[bool | int | float | str], all_values))
        except (TypeError, ValueError):
            raise TypeError(
                f"Unsupported iterable: {values}. Subtype must be bool, float, int, or string."
            )

        publish_request.scalar_values.CopyFrom(vector_to_protobuf(vector))
    else:
        raise TypeError(
            f"Unsupported condition values type: {type(values)}. Please consult the documentation."
        )


def populate_publish_measurement_request_value(
    publish_request: PublishMeasurementRequest, value: object
) -> None:
    """Assign a value to the appropriate field of a PublishMeasurementRequest object."""
    if isinstance(value, bool):
        publish_request.scalar.bool_value = value
    elif isinstance(value, int):
        publish_request.scalar.sint32_value = value
    elif isinstance(value, float):
        publish_request.scalar.double_value = value
    elif isinstance(value, str):
        publish_request.scalar.string_value = value
    elif isinstance(value, Scalar):
        publish_request.scalar.CopyFrom(scalar_to_protobuf(value))
    elif isinstance(value, Vector):
        publish_request.vector.CopyFrom(vector_to_protobuf(value))
    elif isinstance(value, AnalogWaveform):
        if value.dtype == np.float64:
            publish_request.double_analog_waveform.CopyFrom(
                float64_analog_waveform_to_protobuf(value)
            )
        elif value.dtype == np.int16:
            publish_request.i16_analog_waveform.CopyFrom(int16_analog_waveform_to_protobuf(value))
        else:
            raise TypeError(f"Unsupported AnalogWaveform dtype: {value.dtype}")
    elif isinstance(value, ComplexWaveform):
        if value.dtype == np.complex128:
            publish_request.double_complex_waveform.CopyFrom(
                float64_complex_waveform_to_protobuf(value)
            )
        elif value.dtype == ComplexInt32DType:
            publish_request.i16_complex_waveform.CopyFrom(int16_complex_waveform_to_protobuf(value))
        else:
            raise TypeError(f"Unsupported ComplexWaveform dtype: {value.dtype}")
    elif isinstance(value, Spectrum):
        if value.dtype == np.float64:
            publish_request.double_spectrum.CopyFrom(float64_spectrum_to_protobuf(value))
        else:
            raise TypeError(f"Unsupported Spectrum dtype: {value.dtype}")
    elif isinstance(value, DigitalWaveform):
        publish_request.digital_waveform.CopyFrom(digital_waveform_to_protobuf(value))
    elif isinstance(value, XYData):
        if value.dtype == np.float64:
            publish_request.x_y_data.CopyFrom(float64_xydata_to_protobuf(value))
        else:
            raise TypeError(f"Unsupported XYData dtype: {value.dtype}")
    elif isinstance(value, Iterable):
        value_iterator = iter(value)
        try:
            first_item = next(value_iterator)
        except StopIteration as exc:
            raise ValueError("Cannot publish an empty Iterable.") from exc

        all_items = chain([first_item], value_iterator)
        try:
            vector = Vector(cast(Iterable[bool | int | float | str], all_items))
        except (TypeError, ValueError):
            raise TypeError(
                f"Unsupported iterable: {value}. Subtype must be bool, float, int, or string."
            )

        publish_request.vector.CopyFrom(vector_to_protobuf(vector))
    else:
        raise TypeError(
            f"Unsupported measurement value type: {type(value)}. Please consult the documentation."
        )


def populate_publish_measurement_batch_request_values(
    publish_request: PublishMeasurementBatchRequest, values: object
) -> None:
    """Assign a value to the appropriate field of the PublishMeasurementBatchRequest object."""
    if isinstance(values, Vector):
        publish_request.scalar_values.CopyFrom(vector_to_protobuf(values))
    elif isinstance(values, Iterable):
        values_iterator = iter(values)
        try:
            first_value = next(values_iterator)
        except StopIteration as exc:
            raise ValueError("Cannot publish an empty Iterable.") from exc

        all_values = chain([first_value], values_iterator)
        if isinstance(first_value, Vector):
            _populate_vector_batch_values(publish_request, all_values)
        elif isinstance(first_value, AnalogWaveform):
            _populate_analog_waveform_batch_values(publish_request, first_value, all_values)
        elif isinstance(first_value, ComplexWaveform):
            _populate_complex_waveform_batch_values(publish_request, first_value, all_values)
        elif isinstance(first_value, Spectrum):
            _populate_spectrum_batch_values(publish_request, first_value, all_values)
        elif isinstance(first_value, DigitalWaveform):
            _populate_digital_waveform_batch_values(publish_request, all_values)
        elif isinstance(first_value, XYData):
            _populate_xydata_batch_values(publish_request, first_value, all_values)
        else:
            try:
                vector = Vector(cast(Iterable[bool | int | float | str], all_values))
            except (TypeError, ValueError):
                raise TypeError(
                    f"Unsupported iterable. Subtype must be bool, float, int, string, Vector, "
                    "AnalogWaveform, ComplexWaveform, Spectrum, DigitalWaveform, or XYData."
                )
            publish_request.scalar_values.CopyFrom(vector_to_protobuf(vector))
    else:
        raise TypeError(
            f"Unsupported measurement values type: {type(values)}. Please consult the documentation."
        )


def convert_read_measurement_response_from_protobuf(
    response: ReadMeasurementValueResponse,
) -> object:
    """Convert the value in the ReadMeasurementValueResponse from protobuf and return it."""
    read_data_type = response.WhichOneof("value")
    if read_data_type == "digital_waveform":
        return digital_waveform_from_protobuf(response.digital_waveform)
    elif read_data_type == "double_analog_waveform":
        return float64_analog_waveform_from_protobuf(response.double_analog_waveform)
    elif read_data_type == "double_complex_waveform":
        return float64_complex_waveform_from_protobuf(response.double_complex_waveform)
    elif read_data_type == "double_spectrum":
        return float64_spectrum_from_protobuf(response.double_spectrum)
    elif read_data_type == "i16_analog_waveform":
        return int16_analog_waveform_from_protobuf(response.i16_analog_waveform)
    elif read_data_type == "i16_complex_waveform":
        return int16_complex_waveform_from_protobuf(response.i16_complex_waveform)
    elif read_data_type == "vector":
        return vector_from_protobuf(response.vector)
    elif read_data_type == "x_y_data":
        return float64_xydata_from_protobuf(response.x_y_data)
    else:
        raise TypeError(f"Invalid read type: {read_data_type}")


def convert_read_condition_response_from_protobuf(response: ReadConditionValueResponse) -> object:
    """Convert the value in the ReadConditionValueResponse from protobuf and return it."""
    read_data_type = response.WhichOneof("value")
    if read_data_type == "vector":
        return vector_from_protobuf(response.vector)
    else:
        raise TypeError(f"Invalid read type: {read_data_type}")


def convert_measurement_timestamp_to_protobuf(
    client_provided_timestamp: ht.datetime | None,
) -> PrecisionTimestamp | None:
    """Convert the provided timestamp to PrecisionTimestamp if it's not None."""
    if client_provided_timestamp is not None:
        return hightime_datetime_to_protobuf(client_provided_timestamp)
    else:
        return None
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/__init__.py sha256=0d379bb2cc4b873a9ef55245c293cc8acd47901b78bbc45f6c4f2325b725b244 bytes=53 -->
## FILE: src/ni/datastore/data/_types/__init__.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/__init__.py`
- sha256: `0d379bb2cc4b873a9ef55245c293cc8acd47901b78bbc45f6c4f2325b725b244`
- bytes: 53

````python
"""Types for use in accessing the NI Data Store."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_error_information.py sha256=a65cfa3a117f5857dadec06229616e04c9de38840f24b1eb302e6783c36f64ab bytes=2361 -->
## FILE: src/ni/datastore/data/_types/_error_information.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_error_information.py`
- sha256: `a65cfa3a117f5857dadec06229616e04c9de38840f24b1eb302e6783c36f64ab`
- bytes: 2361

````python
"""Error Information data type for the Data Store Client."""

from __future__ import annotations

from ni.measurements.data.v1.data_store_pb2 import (
    ErrorInformation as ErrorInformationProto,
)


class ErrorInformation:
    """Represents error or exception information in case of measurement failure.

    An ErrorInformation contains an error code, descriptive message, and
    source information to help identify and diagnose issues during measurement
    execution.
    """

    __slots__ = (
        "error_code",
        "message",
        "source",
    )

    def __init__(
        self,
        *,
        error_code: int = 0,
        message: str = "",
        source: str = "",
    ) -> None:
        """Initialize an ErrorInformation instance.

        Args:
            error_code: The numeric error code associated with the error.
            message: A descriptive message explaining the error.
            source: The source or location where the error occurred.
        """
        self.error_code = error_code
        self.message = message
        self.source = source

    @staticmethod
    def from_protobuf(
        error_information_proto: ErrorInformationProto,
    ) -> "ErrorInformation":
        """Create an ErrorInformation instance from a protobuf ErrorInformation message."""
        return ErrorInformation(
            error_code=error_information_proto.error_code,
            message=error_information_proto.message,
            source=error_information_proto.source,
        )

    def to_protobuf(self) -> ErrorInformationProto:
        """Convert this ErrorInformation instance to a protobuf ErrorInformation message."""
        return ErrorInformationProto(
            error_code=self.error_code,
            message=self.message,
            source=self.source,
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, ErrorInformation):
            return NotImplemented
        return (
            self.error_code == other.error_code
            and self.message == other.message
            and self.source == other.source
        )

    def __str__(self) -> str:
        """Return a string representation of the ErrorInformation."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_outcome.py sha256=a1b5d98fa84a155c3c96d9509ba7ab80aab54d8777085eaffdd1b97021556fb5 bytes=1710 -->
## FILE: src/ni/datastore/data/_types/_outcome.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_outcome.py`
- sha256: `a1b5d98fa84a155c3c96d9509ba7ab80aab54d8777085eaffdd1b97021556fb5`
- bytes: 1710

````python
"""Outcome data type for the Data Store Client."""

from __future__ import annotations

from enum import IntEnum

from ni.measurements.data.v1.data_store_pb2 import Outcome as OutcomeProto


class Outcome(IntEnum):
    """Represents the outcome of a measurement or test operation.

    The Outcome enum indicates whether a measurement or test passed, failed,
    or had an indeterminate result.
    """

    UNSPECIFIED = OutcomeProto.OUTCOME_UNSPECIFIED
    """The outcome is not specified or unknown."""

    PASSED = OutcomeProto.OUTCOME_PASSED
    """The measurement or test passed successfully."""

    FAILED = OutcomeProto.OUTCOME_FAILED
    """The measurement or test failed."""

    INDETERMINATE = OutcomeProto.OUTCOME_INDETERMINATE
    """The measurement or test result is indeterminate or inconclusive."""

    @classmethod
    def from_protobuf(cls, outcome_proto: OutcomeProto.ValueType) -> "Outcome":
        """Create an Outcome instance from a protobuf Outcome value.

        Args:
            outcome_proto: The protobuf Outcome value.

        Returns:
            The corresponding Outcome enum value.

        Raises:
            ValueError: If the protobuf value doesn't correspond to a known Outcome.
        """
        try:
            return cls(outcome_proto)
        except ValueError as e:
            raise ValueError(f"Unknown outcome value: {outcome_proto}") from e

    def to_protobuf(self) -> OutcomeProto.ValueType:
        """Convert this Outcome instance to a protobuf Outcome value.

        Returns:
            The corresponding protobuf Outcome value.
        """
        return OutcomeProto.ValueType(self.value)
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_published_condition.py sha256=413737fce6d02269077c02425f2008b853c7ebc2fe0e98f6f7213d85ebe249f1 bytes=3191 -->
## FILE: src/ni/datastore/data/_types/_published_condition.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_published_condition.py`
- sha256: `413737fce6d02269077c02425f2008b853c7ebc2fe0e98f6f7213d85ebe249f1`
- bytes: 3191

````python
"""Published Condition data type for the Data Store Client."""

from __future__ import annotations

from ni.measurements.data.v1.data_store_pb2 import (
    PublishedCondition as PublishedConditionProto,
)


class PublishedCondition:
    """Represents a condition that has been published to the data store.

    A published condition contains metadata about a condition value that was
    published, including an id for data retrieval and associated metadata
    like condition name, type, and associated step/test result IDs.
    """

    __slots__ = (
        "id",
        "name",
        "condition_type",
        "step_id",
        "test_result_id",
    )

    def __init__(
        self,
        *,
        id: str = "",
        name: str = "",
        condition_type: str = "",
        step_id: str = "",
        test_result_id: str = "",
    ) -> None:
        """Initialize a PublishedCondition instance.

        Args:
            id: The unique identifier of the condition. This
                can be used to reference and find the condition in the data store.
            name: The name of the condition.
            condition_type: The type of the condition. For example, "Setup" or
                "Environment".
            step_id: The ID of the step with which this condition is associated.
            test_result_id: The ID of the test result with which this condition
                is associated.
        """
        self.id = id
        self.name = name
        self.condition_type = condition_type
        self.step_id = step_id
        self.test_result_id = test_result_id

    @staticmethod
    def from_protobuf(published_condition_proto: PublishedConditionProto) -> "PublishedCondition":
        """Create a PublishedCondition instance from a protobuf PublishedCondition message."""
        return PublishedCondition(
            id=published_condition_proto.id,
            name=published_condition_proto.name,
            condition_type=published_condition_proto.condition_type,
            step_id=published_condition_proto.step_id,
            test_result_id=published_condition_proto.test_result_id,
        )

    def to_protobuf(self) -> PublishedConditionProto:
        """Convert this PublishedCondition instance to a protobuf PublishedCondition message."""
        return PublishedConditionProto(
            id=self.id,
            name=self.name,
            condition_type=self.condition_type,
            step_id=self.step_id,
            test_result_id=self.test_result_id,
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, PublishedCondition):
            return NotImplemented
        return (
            self.id == other.id
            and self.name == other.name
            and self.condition_type == other.condition_type
            and self.step_id == other.step_id
            and self.test_result_id == other.test_result_id
        )

    def __str__(self) -> str:
        """Return a string representation of the PublishedCondition."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_published_measurement.py sha256=59c99622bfa68d529c1741068e515fd79d8d65a76122c6ac8ebe3b312a0e9a88 bytes=10028 -->
## FILE: src/ni/datastore/data/_types/_published_measurement.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_published_measurement.py`
- sha256: `59c99622bfa68d529c1741068e515fd79d8d65a76122c6ac8ebe3b312a0e9a88`
- bytes: 10028

````python
"""Published Measurement data type for the Data Store Client."""

from __future__ import annotations

from typing import Iterable, MutableSequence

import hightime as ht
from ni.measurements.data.v1.data_store_pb2 import (
    PublishedMeasurement as PublishedMeasurementProto,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_from_protobuf,
    hightime_datetime_to_protobuf,
)

from ni.datastore.data._types._error_information import ErrorInformation
from ni.datastore.data._types._outcome import Outcome
from ni.datastore.data._types._published_condition import PublishedCondition


class PublishedMeasurement:
    """Represents a measurement that has been published to the data store.

    A published measurement contains the measurement data and the associated
    metadata (name, type, timestamps, outcome, hardware, software, and test
    adapter IDs).
    """

    __slots__ = (
        "_published_conditions",
        "id",
        "test_result_id",
        "step_id",
        "_software_item_ids",
        "_hardware_item_ids",
        "_test_adapter_ids",
        "name",
        "value_type",
        "notes",
        "start_date_time",
        "end_date_time",
        "outcome",
        "parametric_index",
        "error_information",
    )

    @property
    def published_conditions(self) -> MutableSequence[PublishedCondition]:
        """The published conditions associated with the published measurement."""
        return self._published_conditions

    @property
    def software_item_ids(self) -> MutableSequence[str]:
        """The software item IDs associated with the published measurement."""
        return self._software_item_ids

    @property
    def hardware_item_ids(self) -> MutableSequence[str]:
        """The hardware item IDs associated with the published measurement."""
        return self._hardware_item_ids

    @property
    def test_adapter_ids(self) -> MutableSequence[str]:
        """The test adapter IDs associated with the published measurement."""
        return self._test_adapter_ids

    def __init__(
        self,
        *,
        published_conditions: Iterable[PublishedCondition] | None = None,
        id: str = "",
        test_result_id: str = "",
        step_id: str = "",
        software_item_ids: Iterable[str] | None = None,
        hardware_item_ids: Iterable[str] | None = None,
        test_adapter_ids: Iterable[str] | None = None,
        name: str = "",
        value_type: str = "",
        notes: str = "",
        start_date_time: ht.datetime | None = None,
        end_date_time: ht.datetime | None = None,
        outcome: Outcome = Outcome.UNSPECIFIED,
        parametric_index: int = 0,
        error_information: ErrorInformation | None = None,
    ) -> None:
        """Initialize a PublishedMeasurement instance.

        Args:
            published_conditions: The published conditions associated with this
                measurement from the test step.
            id: The unique identifier of the measurement.
                This can be used to reference and find the measurement in the
                data store.
            test_result_id: The ID of the test result with which this
                measurement is associated.
            step_id: The ID of the step with which this measurement is
                associated.
            software_item_ids: The IDs of the software items associated with
                this measurement.
            hardware_item_ids: The IDs of the hardware items associated with
                this measurement.
            test_adapter_ids: The IDs of the test adapters associated with this
                measurement.
            name: The name of the measurement.
            value_type: The data type of the measurement value.
            notes: Additional notes or comments about the
                measurement.
            start_date_time: The start timestamp of the measurement.
            end_date_time: The end timestamp of the measurement.
            outcome: The outcome of the measurement (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).
            parametric_index: The index of this measurement in a parametric
                sweep operation.
            error_information: Error or exception information in case of
                measurement failure.
        """
        self._published_conditions: MutableSequence[PublishedCondition] = (
            list(published_conditions) if published_conditions is not None else []
        )
        self.id = id
        self.test_result_id = test_result_id
        self.step_id = step_id
        self._software_item_ids: MutableSequence[str] = (
            list(software_item_ids) if software_item_ids is not None else []
        )
        self._hardware_item_ids: MutableSequence[str] = (
            list(hardware_item_ids) if hardware_item_ids is not None else []
        )
        self._test_adapter_ids: MutableSequence[str] = (
            list(test_adapter_ids) if test_adapter_ids is not None else []
        )
        self.name = name
        self.value_type = value_type
        self.notes = notes
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.outcome = outcome
        self.parametric_index = parametric_index
        self.error_information = error_information

    @staticmethod
    def from_protobuf(
        published_measurement_proto: PublishedMeasurementProto,
    ) -> "PublishedMeasurement":
        """Create a PublishedMeasurement instance from a protobuf PublishedMeasurement message."""
        return PublishedMeasurement(
            published_conditions=[
                PublishedCondition.from_protobuf(cond)
                for cond in published_measurement_proto.published_conditions
            ],
            id=published_measurement_proto.id,
            test_result_id=published_measurement_proto.test_result_id,
            step_id=published_measurement_proto.step_id,
            software_item_ids=published_measurement_proto.software_item_ids,
            hardware_item_ids=published_measurement_proto.hardware_item_ids,
            test_adapter_ids=published_measurement_proto.test_adapter_ids,
            name=published_measurement_proto.name,
            value_type=published_measurement_proto.value_type,
            notes=published_measurement_proto.notes,
            start_date_time=(
                hightime_datetime_from_protobuf(published_measurement_proto.start_date_time)
                if published_measurement_proto.HasField("start_date_time")
                else None
            ),
            end_date_time=(
                hightime_datetime_from_protobuf(published_measurement_proto.end_date_time)
                if published_measurement_proto.HasField("end_date_time")
                else None
            ),
            outcome=Outcome.from_protobuf(published_measurement_proto.outcome),
            parametric_index=published_measurement_proto.parametric_index,
            error_information=(
                ErrorInformation.from_protobuf(published_measurement_proto.error_information)
                if published_measurement_proto.HasField("error_information")
                else None
            ),
        )

    def to_protobuf(self) -> PublishedMeasurementProto:
        """Convert this PublishedMeasurement instance to a protobuf PublishedMeasurement message."""
        return PublishedMeasurementProto(
            published_conditions=[
                condition.to_protobuf() for condition in self.published_conditions
            ],
            id=self.id,
            test_result_id=self.test_result_id,
            step_id=self.step_id,
            software_item_ids=self.software_item_ids,
            hardware_item_ids=self.hardware_item_ids,
            test_adapter_ids=self.test_adapter_ids,
            name=self.name,
            value_type=self.value_type,
            notes=self.notes,
            start_date_time=(
                hightime_datetime_to_protobuf(self.start_date_time)
                if self.start_date_time is not None
                else None
            ),
            end_date_time=(
                hightime_datetime_to_protobuf(self.end_date_time)
                if self.end_date_time is not None
                else None
            ),
            outcome=self.outcome.to_protobuf(),
            parametric_index=self.parametric_index,
            error_information=(
                self.error_information.to_protobuf() if self.error_information is not None else None
            ),
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, PublishedMeasurement):
            return NotImplemented
        return (
            self.published_conditions == other.published_conditions
            and self.id == other.id
            and self.test_result_id == other.test_result_id
            and self.step_id == other.step_id
            and self.software_item_ids == other.software_item_ids
            and self.hardware_item_ids == other.hardware_item_ids
            and self.test_adapter_ids == other.test_adapter_ids
            and self.name == other.name
            and self.value_type == other.value_type
            and self.notes == other.notes
            and self.start_date_time == other.start_date_time
            and self.end_date_time == other.end_date_time
            and self.outcome == other.outcome
            and self.parametric_index == other.parametric_index
            and self.error_information == other.error_information
        )

    def __str__(self) -> str:
        """Return a string representation of the PublishedMeasurement."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_step.py sha256=dfedab77d85c539ad2b3f89adc1e581f6b8e4f8b16ffcdd646f75974f8b272d1 bytes=7482 -->
## FILE: src/ni/datastore/data/_types/_step.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_step.py`
- sha256: `dfedab77d85c539ad2b3f89adc1e581f6b8e4f8b16ffcdd646f75974f8b272d1`
- bytes: 7482

````python
"""Step data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

import hightime as ht
from ni.measurements.data.v1.data_store_pb2 import Step as StepProto
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_from_protobuf,
    hightime_datetime_to_protobuf,
)

from ni.datastore.data._types._error_information import ErrorInformation
from ni.datastore.data._types._outcome import Outcome
from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class Step:
    """Information about a step into which measurements and conditions are published.

    Represents a hierarchical execution step within a test result that can
    contain measurements and conditions. Steps are linked to a test result and
    can be organized into hierarchical structures using parent_step_id. Each
    step has test execution time, metadata, and optional extensions for custom
    metadata.
    """

    __slots__ = (
        "name",
        "id",
        "parent_step_id",
        "test_result_id",
        "test_id",
        "step_type",
        "notes",
        "start_date_time",
        "end_date_time",
        "link",
        "_extension",
        "schema_id",
        "error_information",
        "outcome",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the step."""
        return self._extension

    def __init__(
        self,
        name: str,
        *,
        id: str = "",
        parent_step_id: str = "",
        test_result_id: str = "",
        test_id: str = "",
        step_type: str = "",
        notes: str = "",
        start_date_time: ht.datetime | None = None,
        end_date_time: ht.datetime | None = None,
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
        error_information: ErrorInformation | None = None,
        outcome: Outcome = Outcome.UNSPECIFIED,
    ) -> None:
        """Initialize a Step instance.

        Args:
            name: Human-readable name of the step.
            id (optional): Unique identifier for the step.
            parent_step_id (optional): ID of the parent step if this is a nested step.
            test_result_id (optional): ID of the test result this step belongs to.
            test_id (optional): ID of the test associated with this step.
            step_type (optional): Type or category of the step.
            notes (optional): Additional notes or comments about the step.
            start_date_time (optional): The start date and time of the step execution.
            end_date_time (optional): The end date and time of the step execution.
            link (optional): Optional link to external resources for this step.
            extension (optional): Additional extension attributes as key-value pairs.
            schema_id (optional): ID of the extension schema for validating extensions.
            error_information (optional): Error or exception information in case of
                step failure.
            outcome (optional): The outcome of the step (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).
        """
        self.name = name
        self.id = id
        self.parent_step_id = parent_step_id
        self.test_result_id = test_result_id
        self.test_id = test_id
        self.step_type = step_type
        self.notes = notes
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id
        self.error_information = error_information
        self.outcome = outcome

    @staticmethod
    def from_protobuf(step_proto: StepProto) -> "Step":
        """Create a Step instance from a protobuf Step message."""
        step = Step(
            name=step_proto.name,
            id=step_proto.id,
            parent_step_id=step_proto.parent_step_id,
            test_result_id=step_proto.test_result_id,
            test_id=step_proto.test_id,
            step_type=step_proto.step_type,
            notes=step_proto.notes,
            start_date_time=(
                hightime_datetime_from_protobuf(step_proto.start_date_time)
                if step_proto.HasField("start_date_time")
                else None
            ),
            end_date_time=(
                hightime_datetime_from_protobuf(step_proto.end_date_time)
                if step_proto.HasField("end_date_time")
                else None
            ),
            link=step_proto.link,
            schema_id=step_proto.schema_id,
            error_information=(
                ErrorInformation.from_protobuf(step_proto.error_information)
                if step_proto.HasField("error_information")
                else None
            ),
            outcome=Outcome.from_protobuf(step_proto.outcome),
        )
        populate_from_extension_value_message_map(step.extension, step_proto.extension)
        return step

    def to_protobuf(self) -> StepProto:
        """Convert this Step to a protobuf Step message."""
        step_proto = StepProto(
            id=self.id,
            parent_step_id=self.parent_step_id,
            test_result_id=self.test_result_id,
            test_id=self.test_id,
            name=self.name,
            step_type=self.step_type,
            notes=self.notes,
            start_date_time=(
                hightime_datetime_to_protobuf(self.start_date_time)
                if self.start_date_time
                else None
            ),
            end_date_time=(
                hightime_datetime_to_protobuf(self.end_date_time) if self.end_date_time else None
            ),
            link=self.link,
            schema_id=self.schema_id,
            error_information=(
                self.error_information.to_protobuf() if self.error_information is not None else None
            ),
            outcome=self.outcome.to_protobuf(),
        )
        populate_extension_value_message_map(step_proto.extension, self.extension)
        return step_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, Step):
            return NotImplemented
        return (
            self.id == other.id
            and self.parent_step_id == other.parent_step_id
            and self.test_result_id == other.test_result_id
            and self.test_id == other.test_id
            and self.name == other.name
            and self.step_type == other.step_type
            and self.notes == other.notes
            and self.start_date_time == other.start_date_time
            and self.end_date_time == other.end_date_time
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
            and self.error_information == other.error_information
            and self.outcome == other.outcome
        )

    def __str__(self) -> str:
        """Return a string representation of the Step."""
        return str(self.to_protobuf())
````
