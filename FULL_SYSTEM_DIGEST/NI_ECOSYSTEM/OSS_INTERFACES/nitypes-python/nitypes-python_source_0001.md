# NI OSS SOURCE SNAPSHOT: nitypes-python

<!--NI_OSS_SNAPSHOT repo=ni/nitypes-python commit=2744270de1437c671fecc48b9f8ebc17a8343cda -->

<!--NI_OSS_SOURCE repo=nitypes-python path=.devcontainer/devcontainer.json sha256=44d60a78d4235d38465dc824bf9f54fb8d746049bb42b46f03f89fb953ef3a33 bytes=1019 -->
## FILE: .devcontainer/devcontainer.json

- repository: `ni/nitypes-python`
- source_path: `.devcontainer/devcontainer.json`
- sha256: `44d60a78d4235d38465dc824bf9f54fb8d746049bb42b46f03f89fb953ef3a33`
- bytes: 1019

````json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
	"name": "Python 3",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/python:2-3.11-trixie",
	"features": {
		"ghcr.io/devcontainers-extra/features/poetry:2": {
			"version": "2.1.4"
		}
	}
	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},
	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],
	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "pip3 install --user -r requirements.txt",
	// Configure tool-specific properties.
	// "customizations": {},
	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.gitattributes sha256=f80dcc94402f38c7b9be9d27d83a5f3010189ba041cdc5f27094480b4f909d0d bytes=13 -->
## FILE: .gitattributes

- repository: `ni/nitypes-python`
- source_path: `.gitattributes`
- sha256: `f80dcc94402f38c7b9be9d27d83a5f3010189ba041cdc5f27094480b4f909d0d`
- bytes: 13

````text
* text=auto
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/CODEOWNERS sha256=81d9deca13feb38fe4e1bd7b49e69a90d135a534feaa063a0776f591b56728ac bytes=53 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nitypes-python`
- source_path: `.github/CODEOWNERS`
- sha256: `81d9deca13feb38fe4e1bd7b49e69a90d135a534feaa063a0776f591b56728ac`
- bytes: 53

````text
# Default code owner for nitypes
* @bkeryan @csjall 
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/ISSUE_TEMPLATE/bug_report.md sha256=7e8b4f8b75ee0d305e84ec4d1d9dfcf950e689a903e1a66b248cb0710c08d35b bytes=1358 -->
## FILE: .github/ISSUE_TEMPLATE/bug_report.md

- repository: `ni/nitypes-python`
- source_path: `.github/ISSUE_TEMPLATE/bug_report.md`
- sha256: `7e8b4f8b75ee0d305e84ec4d1d9dfcf950e689a903e1a66b248cb0710c08d35b`
- bytes: 1358

````markdown
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: 'bug,triage'
---

<!---
Thanks for filing an issue! Before you submit, please read the following:

Search open/closed issues before submitting. Someone may have reported the same issue before.
-->

# Bug Report

<!--- Provide a general summary of the issue here -->

## Repro or Code Sample

<!-- Please provide steps to reproduce the issue and/or a code repository, gist, code snippet or sample files -->

## Expected Behavior

<!--- Tell us what should happen -->

## Current Behavior

<!--- Tell us what happens instead of the expected behavior -->
<!--- If you are seeing an error, please include the full error message and stack trace -->
<!--- If applicable, provide screenshots -->

## Possible Solution

<!--- Not obligatory, but suggest a fix/reason for the bug -->
<!--- Please let us know if you'd be willing to contribute the fix; we'd be happy to work with you -->

## Context

<!--- How has this issue affected you? What are you trying to accomplish? -->
<!--- Providing context helps us come up with a solution that is most useful in the real world -->

## Your Environment

<!--- Include as many relevant details as possible about the environment you experienced the bug in -->

* `nitypes` version
* Python version
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/ISSUE_TEMPLATE/feature_request.md sha256=e00ddb5b02a84de7f991b8a86a1bc750d91141603aad727f2a85d4c0bc8be6b1 bytes=712 -->
## FILE: .github/ISSUE_TEMPLATE/feature_request.md

- repository: `ni/nitypes-python`
- source_path: `.github/ISSUE_TEMPLATE/feature_request.md`
- sha256: `e00ddb5b02a84de7f991b8a86a1bc750d91141603aad727f2a85d4c0bc8be6b1`
- bytes: 712

````markdown
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: 'enhancement,triage'
---

<!---
Thanks for filing an issue! Before you submit, please read the following:

Search open/closed issues before submitting. Someone may have requested the same feature before.
-->

## Problem to Solve

<!--- Provide a clear and concise description of why this feature is wanted or what problem it solves. -->

## Proposed Solution

<!--- Provide a clear and concise description of the feature you're proposing. -->

<!--- The implementing team may build a list of tasks/sub-issues here:
## Tasks
- [ ] This is a subtask of the feature. (It can be converted to an issue.)
-->
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/ISSUE_TEMPLATE/tech_debt.md sha256=a80e6afbbd5f723466dab578104fedfe7d38413e65714a4e5ccb40d1d35389d0 bytes=164 -->
## FILE: .github/ISSUE_TEMPLATE/tech_debt.md

- repository: `ni/nitypes-python`
- source_path: `.github/ISSUE_TEMPLATE/tech_debt.md`
- sha256: `a80e6afbbd5f723466dab578104fedfe7d38413e65714a4e5ccb40d1d35389d0`
- bytes: 164

````markdown
---
name: Tech debt
about: (DEV TEAM ONLY) Non-user-visible improvement to code or development process
title: ''
labels: 'tech debt,triage'
---
## Tech Debt
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/ISSUE_TEMPLATE/user_story.md sha256=db24cb4a5576436f0dd3e0fbfd2d95a20336d2aa1c5d68cddbd5a717dc993012 bytes=321 -->
## FILE: .github/ISSUE_TEMPLATE/user_story.md

- repository: `ni/nitypes-python`
- source_path: `.github/ISSUE_TEMPLATE/user_story.md`
- sha256: `db24cb4a5576436f0dd3e0fbfd2d95a20336d2aa1c5d68cddbd5a717dc993012`
- bytes: 321

````markdown
---
name: User story
about: (DEV TEAM ONLY) A small chunk of work to be done
title: '(Fully descriptive title)'
labels: 'user story,triage'
---

<!-- Ensure the title can be understood without the parent item's context, e.g. "nimble-button Angular wrapper" rather than just "Angular wrapper" -->

## User Story
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=5e70acb945fc6d020969c4b67a799a47f216beba568bc5c540f7b578f19e6b1e bytes=484 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nitypes-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `5e70acb945fc6d020969c4b67a799a47f216beba568bc5c540f7b578f19e6b1e`
- bytes: 484

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nitypes-python/blob/main/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/renovate.json sha256=60909f4835c7ec398d2e67ef80b54755d8288f94e525c80d00865267c91128c2 bytes=153 -->
## FILE: .github/renovate.json

- repository: `ni/nitypes-python`
- source_path: `.github/renovate.json`
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

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/check_docs.yml sha256=821b71110ff3a862a6ea9c87e8cd36697a7e3652cd483ee02e1477b930f4d49b bytes=1366 -->
## FILE: .github/workflows/check_docs.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/check_docs.yml`
- sha256: `821b71110ff3a862a6ea9c87e8cd36697a7e3652cd483ee02e1477b930f4d49b`
- bytes: 1366

````yaml
name: Check docs

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_docs:
    name: Check docs
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
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
          key: nitypes-with-docs-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install nitypes (with docs)
        run: poetry install -v --only main,docs
      - name: Generate docs
        run:  poetry run sphinx-build docs docs/_build -b html -W
      - name: Upload docs artifact
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: nitypes-docs
          path: docs/_build/
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/check_nitypes.yml sha256=9d6f338450f04566af1f761509372864bee438c69303a73552121b2239982cb6 bytes=1148 -->
## FILE: .github/workflows/check_nitypes.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/check_nitypes.yml`
- sha256: `9d6f338450f04566af1f761509372864bee438c69303a73552121b2239982cb6`
- bytes: 1148

````yaml
name: Check nitypes

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_nitypes:
    name: Check nitypes
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        # Type checking requires an up-to-date NumPy.
        # The latest NumPy only supports 3.11 and later
        python-version: [3.11, 3.14]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Analyze Python project
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Bandit security checks
        run:  poetry run bandit -c pyproject.toml -r src/nitypes
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/check_workflows.yml sha256=e00c7fb6d0a5207cb751edb5b39eeb643512d2e4de96419e8fc6cbdbbd9601c1 bytes=498 -->
## FILE: .github/workflows/check_workflows.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/check_workflows.yml`
- sha256: `e00c7fb6d0a5207cb751edb5b39eeb643512d2e4de96419e8fc6cbdbbd9601c1`
- bytes: 498

````yaml
name: Check workflows

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  zizmor:
    name: Run zizmor
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Run zizmor
        uses: zizmorcore/zizmor-action@192e21d79ab29983730a13d1382995c2307fbcaa # v0.5.7
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/CI.yml sha256=e51cd4b0a5283a266ae5da27a509d2a029cf33923e61cfb4238250e1f9d547f5 bytes=1196 -->
## FILE: .github/workflows/CI.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/CI.yml`
- sha256: `e51cd4b0a5283a266ae5da27a509d2a029cf33923e61cfb4238250e1f9d547f5`
- bytes: 1196

````yaml
name: CI

on:
  push:
    branches:
      - main
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_nitypes:
    name: Check nitypes
    uses: ./.github/workflows/check_nitypes.yml
  check_docs:
    name: Check docs
    uses: ./.github/workflows/check_docs.yml
  check_workflows:
    name: Check workflows
    uses: ./.github/workflows/check_workflows.yml
    permissions:
      security-events: write
  checks_succeeded:
    name: Checks succeeded
    needs: [check_nitypes, check_docs, check_workflows]
    runs-on: ubuntu-latest
    steps:
      - run: exit 0
  run_unit_tests:
    name: Run unit tests
    uses: ./.github/workflows/run_unit_tests.yml
    needs: [checks_succeeded]
  run_unit_tests_oldest_deps:
    name: Run unit tests (oldest deps)
    uses: ./.github/workflows/run_unit_tests_oldest_deps.yml
    needs: [checks_succeeded]
  report_test_results:
    name: Report test results
    uses: ./.github/workflows/report_test_results.yml
    needs: [run_unit_tests, run_unit_tests_oldest_deps]
    if: always()
    permissions:
      contents: read
      checks: write
      pull-requests: write
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/PR.yml sha256=db1b0e1a26bae8ca03a1b3fc5dc1ab53c9cf097fd9a7d6cdbe78862cae7f7952 bytes=469 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/PR.yml`
- sha256: `db1b0e1a26bae8ca03a1b3fc5dc1ab53c9cf097fd9a7d6cdbe78862cae7f7952`
- bytes: 469

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

permissions: {}

jobs:
  run_ci:
    name: Run CI
    uses: ./.github/workflows/CI.yml
    permissions:
      contents: read
      checks: write
      pull-requests: write
      security-events: write
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/publish.yml sha256=2b469c679c9525bd3892f978885bb16709162a54f28746ccc06b7fdb92297cd7 bytes=3785 -->
## FILE: .github/workflows/publish.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/publish.yml`
- sha256: `2b469c679c9525bd3892f978885bb16709162a54f28746ccc06b7fdb92297cd7`
- bytes: 3785

````yaml
name: Publish nitypes

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
  dist-artifact-name: nitypes-distribution-packages
  environment: ${{ case(github.event_name == 'release', 'pypi', inputs.environment) }}
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

permissions: {}

jobs:
  check_nitypes:
    name: Check nitypes
    uses: ./.github/workflows/check_nitypes.yml
  check_docs:
    name: Check docs
    uses: ./.github/workflows/check_docs.yml
  build_nitypes:
    name: Build nitypes
    runs-on: ubuntu-latest
    needs: [check_nitypes, check_docs]
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          use-cache: false
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
    name: Publish nitypes to PyPI
    if: github.event_name == 'release' || inputs.environment != 'none'
    runs-on: ubuntu-latest
    needs: [build_nitypes]
    environment:
      # This logic is duplicated because `name` doesn't support the `env` context.
      name: ${{ case(github.event_name == 'release', 'pypi', inputs.environment) }}
      url: ${{ fromJson(env.environment-info)[env.environment].base-url }}/p/nitypes
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
    name: Update nitypes version
    runs-on: ubuntu-latest
    needs: [build_nitypes]
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          use-cache: false
      - name: Update project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/report_test_results.yml sha256=36ff8e3fd865b65486ae8d5237d84df53e4834528ceba26d93fa8d4763d77dac bytes=971 -->
## FILE: .github/workflows/report_test_results.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/report_test_results.yml`
- sha256: `36ff8e3fd865b65486ae8d5237d84df53e4834528ceba26d93fa8d4763d77dac`
- bytes: 971

````yaml
name: Report test results

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  report_test_results:
    name: Report test results
    runs-on: ubuntu-latest
    permissions:
      contents: read
      checks: write
      pull-requests: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Download test results
        uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          path: test_results
          pattern: test_results_*
          merge-multiple: true
      - name: List downloaded files
        run: ls -lR
      - name: Publish test results
        uses: EnricoMi/publish-unit-test-result-action@d0a4676d0e0b938bc201470d88276b7c74c712b3 # v2.24.0
        with:
          files: "test_results/**/*.xml"
        if: always()
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/run_unit_tests.yml sha256=f435021b27ee0665c1ec95e7c1957f6c1aeb90f2b5dd77b75d96287eb9055f69 bytes=2086 -->
## FILE: .github/workflows/run_unit_tests.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/run_unit_tests.yml`
- sha256: `f435021b27ee0665c1ec95e7c1957f6c1aeb90f2b5dd77b75d96287eb9055f69`
- bytes: 2086

````yaml
name: Run unit tests

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  run_unit_tests:
    name: Run unit tests
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: [3.9, '3.10', 3.11, 3.12, 3.13, 3.14, 3.14t, pypy3.11]
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenv
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: .venv
          key: nitypes-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install nitypes
        run: poetry install -v
      - name: Display installed dependency versions
        run: poetry run pip list
      - name: Run unit/acceptance/doc tests and code coverage
        run: poetry run pytest -v --cov=nitypes --junitxml=test_results/nitypes-${{ matrix.os }}-py${{ matrix.python-version }}.xml
      - name: Run benchmarks
        run: poetry run pytest ./tests/benchmark -v --junitxml=test_results/nitypes-benchmarks-${{ matrix.os }}-py${{ matrix.python-version }}.xml
      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_unit_${{ matrix.os }}_py${{ matrix.python-version }}
          path: ./test_results/*.xml
        if: always()
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/run_unit_tests_oldest_deps.yml sha256=46058e697540ae2abb53b980b35d1e27a147cc6baf640f82e1a197fed54b8544 bytes=2605 -->
## FILE: .github/workflows/run_unit_tests_oldest_deps.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/run_unit_tests_oldest_deps.yml`
- sha256: `46058e697540ae2abb53b980b35d1e27a147cc6baf640f82e1a197fed54b8544`
- bytes: 2605

````yaml
name: Run unit tests (oldest deps)

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  run_unit_tests_oldest_deps:
    name: Run unit tests (oldest deps)
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        python-version: [3.9]
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenv
        id: cache-virtualenv
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: .venv
          key: nitypes-oldest-deps-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install nitypes (latest deps)
        if: steps.cache-virtualenv.outputs.cache-hit != 'true'
        run: poetry install -v
      - name: Pin oldest compatible dependencies
        if: steps.cache-virtualenv.outputs.cache-hit != 'true'
        run: |
          poetry run python scripts/pin_oldest_deps.py pyproject.toml
          poetry lock
      - name: Install nitypes (oldest deps)
        if: steps.cache-virtualenv.outputs.cache-hit != 'true'
        run: poetry install -v
      - name: Display installed dependency versions
        run: poetry run pip list
      - name: Run unit tests and code coverage
        # Skip test___pickled_value___unpickle___is_compatible because this test's pickle data was saved with NumPy 2.x and cannot be loaded in NumPy 1.x.
        run: poetry run pytest ./tests/unit -v --cov=nitypes --junitxml=test_results/nitypes-oldest-deps-${{ matrix.os }}-py${{ matrix.python-version }}.xml -k "not test___pickled_value___unpickle___is_compatible"
      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_unit_oldest_deps_${{ matrix.os }}_py${{ matrix.python-version }}
          path: ./test_results/*.xml
        if: always()
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.github/workflows/sync_github_issues_to_azdo.yml sha256=26845475d14d8ec4814a8b078d70636dbe2104766cff260958ec8efffef8a1b9 bytes=1379 -->
## FILE: .github/workflows/sync_github_issues_to_azdo.yml

- repository: `ni/nitypes-python`
- source_path: `.github/workflows/sync_github_issues_to_azdo.yml`
- sha256: `26845475d14d8ec4814a8b078d70636dbe2104766cff260958ec8efffef8a1b9`
- bytes: 1379

````yaml
name: Sync issue to Azure DevOps work item

on:
  issues:
    # Omit "labeled" and "unlabeled" to work around https://github.com/danhellem/github-actions-issue-to-work-item/issues/70
    types:
      [opened, edited, deleted, closed, reopened, assigned]
  issue_comment:
    types: [created, edited, deleted]

permissions: {}

jobs:
  alert:
    if: ${{ !github.event.issue.pull_request && github.event.issue.title != 'Dependency Dashboard' }}
    runs-on: ubuntu-latest
    steps:
      - uses: danhellem/github-actions-issue-to-work-item@45eb3b46e684f2acd2954f02ef70350c835ee4bb # v2.4
        env:
          ado_token: "${{ secrets.AZDO_WORK_ITEM_TOKEN }}"
          github_token: "${{ secrets.GH_REPO_TOKEN }}"
          ado_organization: "ni"
          ado_project: "DevCentral"
          ado_area_path: "DevCentral\\Product RnD\\Platform HW and SW\\SW New Invest and Tech\\ETW\\Python CodeGen"
          ado_wit: "${{ case(
            contains(github.event.issue.labels.*.name, 'enhancement') || contains(github.event.issue.labels.*.name, 'user story'), 'User Story',
            contains(github.event.issue.labels.*.name, 'tech debt'), 'Technical Debt',
            'Bug') }}"
          ado_new_state: "New"
          ado_active_state: "Active"
          ado_close_state: "Closed"
          ado_bypassrules: true
          log_level: 100
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.gitignore sha256=4d6a958af2e3f9d012dc623e7ac93b1ac6612b411665fa1b69dc16597ef06ad9 bytes=275 -->
## FILE: .gitignore

- repository: `ni/nitypes-python`
- source_path: `.gitignore`
- sha256: `4d6a958af2e3f9d012dc623e7ac93b1ac6612b411665fa1b69dc16597ef06ad9`
- bytes: 275

````text
# Byte-compiled / optimized / DLL files
__pycache__/

# Unit tests
.tox/
test_results/
.benchmarks/

# Coverage output
.coverage
htmlcov/

# Environments
.env
.venv

# Built artifacts
dist/
docs/_build/
docs/autoapi/

# Common editor metadata
.vscode/
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.markdownlint.yml sha256=3e90afac6553ac688869bec800766c06de4fe1a6bc9f48e153cb95a8cf68b1d3 bytes=91 -->
## FILE: .markdownlint.yml

- repository: `ni/nitypes-python`
- source_path: `.markdownlint.yml`
- sha256: `3e90afac6553ac688869bec800766c06de4fe1a6bc9f48e153cb95a8cf68b1d3`
- bytes: 91

````yaml
# MD013/line-length
MD013:
  line_length: 100

# MD041/first-line-heading
MD041: false
````

<!--NI_OSS_SOURCE repo=nitypes-python path=.readthedocs.yml sha256=b4966721183d74555a5563ce9cec2bc74e251791b41b9e63d02fc6f355e135b6 bytes=309 -->
## FILE: .readthedocs.yml

- repository: `ni/nitypes-python`
- source_path: `.readthedocs.yml`
- sha256: `b4966721183d74555a5563ce9cec2bc74e251791b41b9e63d02fc6f355e135b6`
- bytes: 309

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
      - VIRTUAL_ENV=$READTHEDOCS_VIRTUALENV_PATH poetry install --only main,docs

sphinx:
  configuration: docs/conf.py
````

<!--NI_OSS_SOURCE repo=nitypes-python path=CONTRIBUTING.md sha256=150586eb7af776266d9f1c3c45eeaa5cd1b7f4c5886071ec4e4c920fa8cdfe04 bytes=9803 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nitypes-python`
- source_path: `CONTRIBUTING.md`
- sha256: `150586eb7af776266d9f1c3c45eeaa5cd1b7f4c5886071ec4e4c920fa8cdfe04`
- bytes: 9803

````markdown
# Contributing to `nitypes`

Contributions to `nitypes` are welcome from all!

`nitypes` is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/nitypes-python/).

`nitypes` follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

## Signing Off Commits

Please remember to sign off your commits (e.g., by using `git commit -s` if you
are using the command line client). This amends your git commit message with a line
of the form `Signed-off-by: Name Lastname <name.lastmail@emailaddress.com>`. Please
include all authors of any given commit into the commit message with a
`Signed-off-by` line. This indicates that you have read and signed the Developer
Certificate of Origin (see below) and are able to legally submit your code to
this repository.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Ensure you have [python](https://www.python.org) version 3.11.9 or newer [installed](https://www.python.org/downloads/).
1. Ensure you have [poetry](https://python-poetry.org/)
   version 2.1.3 or newer [installed](https://python-poetry.org/docs/#installation).
1. If you do not have write access to the repo, fork the repository on GitHub.
1. Install `nitypes` dependencies using `poetry install --with docs`.
1. Perform [Tests and Checks](#tests-and-checks)
1. If all the tests and checks pass, proceed to the next step.
   If you encounter any failures do not begin development. Instead, try to resolve
   those failures, and go back to the previous step. If you are unable to resolve the failures,
   report an issue through our [GitHub issues page](http://github.com/ni/nitypes-python/issues).
1. Write new tests that demonstrate your bug or feature. Run regression tests.
   Ensure that the new tests fail.
1. Make your change. Remember to sign off your commits as described
   [above](#signing-off-commits).
1. Perform [Tests and Checks](#tests-and-checks)
1. If all of the tests and checks pass, proceed to the next step.
   Otherwise, fix the failures and go back to the previous step where the problem was introduced.
1. Send a GitHub Pull Request to the main repository's `main` branch. GitHub Pull Requests are
   the expected method of code collaboration on this project.
1. Look at the test and check results on the Conversation tab in the PR.

   Note that if you are using a fork of the repo, the `Test Results` check will not complete due to a known issue (#243).

   If any of the tests or checks fails, attempt to fix the failures by changing the code.

## Tests and Checks

As a contributor, you are expected to perform the following tests and checks:
1. Perform regression tests per [Regression Tests](#regression-tests) section below.
1. Perform static analysis checks per [Static Analysis Checks](#static-analysis-checks)
section below.
1. If your changes will cover documentation generated from the code, generate that
   documentation per
   [Documentation Generated from the Code](#documentation-generated-from-the-code) section.
1. If you are concerned that your changes may have negative impact on performance,
   perform benchmark test per [Benchmark Tests](#benchmark-tests)

## Regression Tests

In order to be able to run the `nitypes` regression tests, your setup should meet the following minimum
requirements:

- Machine has a supported version of CPython or PyPy installed.
- Machine has [poetry](https://python-poetry.org/) installed.

To perform regression tests, run `poetry run pytest -v` in the root of the distribution.

## Static Analysis Checks

Static analysis is performed in several steps, as set forth below. Run each of the commands listed below in the root of the distribution.

1. Run `poetry run ni-python-styleguide lint` to check that the updated code follows NI's Python
   coding conventions. If this reports errors, first run `poetry run ni-python-styleguide fix`
   to sort imports and format the code with Black, then manually fix any ring errors.
1. Run `poetry run mypy`. If there are any failures, fix them.
1. Run `poetry run pyright`. If there are any failures, fix them.
1. Run `poetry run bandit -c pyproject.toml -r src/nitypes`. If there are any failures, fix them.

# Special Considerations

## Documentation Generated from the Code

The following information is relevant if you are making changes that
will impact documentation generated from the code.

To generate documentation from the code, run `poetry run sphinx-build docs docs/_build --builder html --fail-on-warning` in the root of the distribution.

If there are any failures, fix them.

To review generated documentation, run `start docs\_build\index.html` from the
root of the distribution.

## Benchmark Tests

The PR pipeline will perform benchmark tests. The following information
is provided in case you expect that your change will impact performance,
or in case benchmark checks performed by the PR pipeline fail.

To perform benchmark tests do the following:
   * For the first run, prior to making any changes, run the
   command `poetry run pytest -v tests/benchmark --benchmark-save=base`
   * For the second and subsequent runs, after making changes, run the
   command `poetry run pytest -v tests/benchmark --benchmark-compare=0001`

   To learn more about benchmark tests, refer
   to https://pytest-benchmark.readthedocs.io/en/latest/comparing.html

# Example Development Workflow
The example belows applies when you are making changes that will
not impact documentation generated from code and that will not impact
code performance. If your situation is different, add appropriate
steps per documentation above.

```
# Create a fork
# Create a new branch
git fetch
git switch --create users/{username}/{branch-purpose} origin/main

# Install the project dependencies
poetry install --with docs

# Run regression tests
poetry run pytest -v

# Run static analysis checks
poetry run nps lint
poetry run mypy
poetry run pyright
poetry run bandit -c pyproject.toml -r src/nitypes

# ✍ Add regression tests.
# Run regression tests
poetry run pytest -v

# ✍ Make source changes
# Remember to sign off commits

# Run regression tests
poetry run pytest -v

# Run static analysis checks
poetry run nps lint
poetry run mypy
poetry run pyright
poetry run bandit -c pyproject.toml -r src/nitype
```

# Publishing on PyPI

You can publish the `nitypes` package by creating a GitHub release
in the `nitypes-python` repo. Here are the steps to follow to publish the package:

1. From the main GitHub repo page, select "Create a new release".
2. On the "New Release" page, create a new tag using the "Select Tag" drop down. The tag must be the package version, matching the
value found in pyproject.toml. Example: `0.1.0-dev0`.
3. Enter a title in the "Release title" field. The title should contain the package name and
version in the format `nitypes <package-version>`. For example: `nitypes 0.1.0-dev0`.
4. Click "Generate release notes" and edit the release notes.
  - Delete entries for PRs that do not affect users, such as "chore(deps):" and "fix(deps):" PRs.
  - Consider grouping related entries.
  - Reformat entries to be more readable. For example, change "Blah blah by so-and-so in \#123" to "Blah blah (\#123)".
5. If this is a pre-release release, check the "Set as a pre-release" checkbox.
6. Click "Publish release".
7. Creating a release will start the publish workflow. You can track the
progress of this workflow in the "Actions" page of the GitHub repo.
8. The workflow job that publishes a package to PyPI requires code owner approval. This job will automatically send code owners a notification email, then it will wait for them to log in and approve the deployment.
9. After receiving code owner approval, the publish workflow will resume.
10. Once the publish workflow has finished, you should see your release on PyPI.

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

See [LICENSE](https://github.com/ni/nitypes-python/blob/main/LICENSE)
for details about how `nitypes` is licensed.
````

<!--NI_OSS_SOURCE repo=nitypes-python path=docs/conf.py sha256=b68ca2d7e9078dcc33c44c0391baca4707bc90b052ac074a289a53bb9052ac84 bytes=3303 -->
## FILE: docs/conf.py

- repository: `ni/nitypes-python`
- source_path: `docs/conf.py`
- sha256: `b68ca2d7e9078dcc33c44c0391baca4707bc90b052ac074a289a53bb9052ac84`
- bytes: 3303

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
    "m2r2",
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
copyright = f"2025-%Y, {company}"
if datetime.datetime.now().year == 2025:
    copyright = f"%Y, {company}"


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
autoapi_options.append("inherited-members")
autoapi_dirs = [root_path / "src" / "nitypes"]
autoapi_own_page_level = "class"
autoapi_type = "python"
autodoc_typehints = "both"
# Uncomment for debugging
# autoapi_keep_files = True

# TODO: https://github.com/ni/nitypes-python/issues/47 - _numpy.py helper module generates autoapi
# import warnings
suppress_warnings = ["autoapi.python_import_resolution"]


# TODO: https://github.com/ni/nitypes-python/issues/16 - Update nitypes-python docs to use
# :canonical: to resolve aliases (once supported by sphinx-autoapi)
def skip_aliases(app, what, name, obj, skip, options):
    """Skip documentation for classes that are exported from multiple modules."""
    # For names that are defined in a private sub-module and aliased into a
    # public package, hide the definition.
    if (
        name.startswith("nitypes.complex._")
        or name.startswith("nitypes.time._")
        or name.startswith("nitypes.waveform._")
    ):
        skip = True

    return skip


def setup(sphinx):
    """Sphinx setup callback."""
    sphinx.connect("autoapi-skip-member", skip_aliases)


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


intersphinx_mapping = {
    "hightime": ("https://hightime.readthedocs.io/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3", None),
}


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": -1,
}

# Napoleon settings
napoleon_numpy_docstring = False
````

<!--NI_OSS_SOURCE repo=nitypes-python path=docs/index.rst sha256=dcd3eb73395672de050319d8591347858c0c0a2db3752501a7aa6994aff8ce60 bytes=309 -->
## FILE: docs/index.rst

- repository: `ni/nitypes-python`
- source_path: `docs/index.rst`
- sha256: `dcd3eb73395672de050319d8591347858c0c0a2db3752501a7aa6994aff8ce60`
- bytes: 309

````rst
#############################
Data Types for NI Python APIs
#############################

.. include:: intro.inc

Table of Contents
=================

.. toctree::
   :maxdepth: 4

   autoapi/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nitypes-python path=docs/intro.inc sha256=d3b6c4d7b28996e82c7f37a4d2f19794340314b8aabd312758295181c1691f30 bytes=3500 -->
## FILE: docs/intro.inc

- repository: `ni/nitypes-python`
- source_path: `docs/intro.inc`
- sha256: `d3b6c4d7b28996e82c7f37a4d2f19794340314b8aabd312758295181c1691f30`
- bytes: 3500

````text
Introduction
============

About
-----

The ``nitypes`` Python package defines data types for NI Python APIs:

- Analog, complex, and digital waveforms
- Frequency spectrums
- Complex integers
- Time conversion

NI created and supports this package.

Operating System Support
------------------------

``nitypes`` supports Windows and Linux operating systems.

Python Version Support
----------------------

``nitypes`` supports CPython 3.9+ and PyPy3.

Installation
------------

Installing NI driver Python APIs that support waveforms will automatically install ``nitypes``.

You can also directly install the ``nitypes`` package using ``pip`` or by listing it as a dependency in
your project's ``pyproject.toml`` file.

Waveforms
---------

Analog Waveforms
^^^^^^^^^^^^^^^^

The :class:`AnalogWaveform` class represents a single analog signal with timing
information and extended properties (such as channel name and units).
Multi-channel analog data is represented using a collection of waveforms, such
as ``list[AnalogWaveform]``.

Complex Waveforms
^^^^^^^^^^^^^^^^^

The :class:`ComplexWaveform` class represents a complex-number signal, such as I/Q
data, with timing information and extended properties (such as channel name and
units).

Digital Waveforms
^^^^^^^^^^^^^^^^^

The :class:`DigitalWaveform` class represents one or more digital signals with
timing information and extended properties (such as channel name and signal
names).

Frequency Spectrums
^^^^^^^^^^^^^^^^^^^

The :class:`Spectrum` class represents a frequency spectrum with frequency range
information and extended properties (such as channel name and units).

Complex Numbers
---------------

Complex Integers
^^^^^^^^^^^^^^^^

:any:`ComplexInt32DType` is a NumPy structured data type object representing a
complex integer with 16-bit ``real`` and ``imag`` fields. This structured data
type has the same memory layout as the NIComplexI16 C struct used by NI driver
APIs.

Complex Number Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the :any:`convert_complex` function to convert complex-number NumPy
arrays between :any:`ComplexInt32DType` and the standard :any:`numpy.complex64`
and :any:`numpy.complex128` data types.

Time
----

Time Conversion
^^^^^^^^^^^^^^^

You can use the :any:`convert_datetime` and :any:`convert_timedelta` functions
to convert time values between the standard :class:`DateTime` library, the
high-precision :any:`hightime` library, and :any:`bintime`.

Binary Time
^^^^^^^^^^^

The :any:`bintime` module implements the NI Binary Time Format (NI-BTF), a
high-resolution time format used by NI software. An NI-BTF time value is a
128-bit fixed point number consisting of a 64-bit whole seconds part and a
64-bit fractional seconds part.

Scalar Values
-------------

Scalar
^^^^^^

:class:`Scalar` is a data type that represents a single scalar value with units
information. Valid types for the scalar value are :any:`bool`, :any:`int`,
:any:`float`, and :any:`str`.

Vector
^^^^^^

:class:`Vector` is a data type that represents an array of scalar values with units
information. Valid types for the scalar values are :any:`bool`, :any:`int`,
:any:`float`, and :any:`str`.

XYData
^^^^^^

:class:`XYData` is a data type that represents a two axes (sequences) of numeric values with
units information. Valid types for the numeric values are :any:`int` and :any:`float`.
````

<!--NI_OSS_SOURCE repo=nitypes-python path=examples/placeholder.py sha256=cec26998eff8579e6e54876caec51f7fabfd7736e9d84a1f5c6d9379d39483c4 bytes=38 -->
## FILE: examples/placeholder.py

- repository: `ni/nitypes-python`
- source_path: `examples/placeholder.py`
- sha256: `cec26998eff8579e6e54876caec51f7fabfd7736e9d84a1f5c6d9379d39483c4`
- bytes: 38

````python
"""Temporary placeholder example."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=LICENSE sha256=b88b611e4e0f4464fd041edcf886c2ea842ec88cd710711c234e917495eaeb4e bytes=1091 -->
## FILE: LICENSE

- repository: `ni/nitypes-python`
- source_path: `LICENSE`
- sha256: `b88b611e4e0f4464fd041edcf886c2ea842ec88cd710711c234e917495eaeb4e`
- bytes: 1091

````text
Copyright (c) 2025, National Instruments Corp.

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

<!--NI_OSS_SOURCE repo=nitypes-python path=poetry.lock sha256=95f13e2938407bd90c46c92cc0b259371daeb9153dced427f63d08c64d0982cc bytes=225563 -->
## FILE: poetry.lock

- repository: `ni/nitypes-python`
- source_path: `poetry.lock`
- sha256: `95f13e2938407bd90c46c92cc0b259371daeb9153dced427f63d08c64d0982cc`
- bytes: 225563

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "alabaster"
version = "0.7.16"
description = "A light, configurable Sphinx theme"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.9\""
files = [
    {file = "alabaster-0.7.16-py3-none-any.whl", hash = "sha256:b46733c07dce03ae4e150330b975c75737fa60f0a7c591b6c8bf4928a28e2c92"},
    {file = "alabaster-0.7.16.tar.gz", hash = "sha256:75a8b99c28a5dad50dd7f8ccdd447a121ddb3892da9e53d1ca5cca3106d58d65"},
]

[[package]]
name = "alabaster"
version = "1.0.0"
description = "A light, configurable Sphinx theme"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version >= \"3.10\""
files = [
    {file = "alabaster-1.0.0-py3-none-any.whl", hash = "sha256:fc6786402dc3fcb2de3cabd5fe455a2db534b371124f1f21de8731783dec828b"},
    {file = "alabaster-1.0.0.tar.gz", hash = "sha256:c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e"},
]

[[package]]
name = "ast-serialize"
version = "0.3.0"
description = "Python bindings for mypy AST serialization"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
markers = "implementation_name != \"pypy\" and python_version >= \"3.10\""
files = [
    {file = "ast_serialize-0.3.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:3a867927df59f76a18dc1d874a0b2c079b42c58972dca637905576deb0912e14"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a6fb063bf040abf8321e7b8113a0554eda445ffc508aa51287f8808886a5ae22"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5075cd8482573d743586779e5f9b652a015e37d4e95132d7e5a9bc5c8f483d8f"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:41560b27794f4553b0f77811e9fb325b77db4a2b39018d437e09932275306e66"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:b967c01ca74909c5d90e0fe4393401e2cc5da5ebd9a6262a19e45ffd3757dec8"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:424ebb8f46cd993f7cec4009d119312d8433dd90e6b0df0499cd2c91bdcc5af9"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d14b1d566b56e2ee70b11fec1de7e0b94ec7cd83717ec7d189967841a361190e"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7ba30b18735f047ec11103d1ab92f4789cf1fea1e0dc89b04a2f5a0632fd79de"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e6ea0754cb7b0f682ebb005ffb0d18f8d17993490d9c289863cd69cacc4ab8df"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:a0c5aa1073a5ba7b2abaa4b54abe8b8d75c4d1e2d54a2ff70b0ca6222fea5728"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:4e52650d834c1ea7791969a361de2c54c13b2fb4c519ec79445fa8b9021a147d"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:15bd6af3f136c61dae27805eb6b8f3269e85a545c4c27ffe9e530ead78d2b36d"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-win32.whl", hash = "sha256:d188bfe37b674b49708497683051d4b571366a668799c9b8e8a94513694969d9"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-win_amd64.whl", hash = "sha256:5832c2fdf8f8a6cf682b4cfcf677f5eaf39b4ddbc490f5480cfccdd1e7ce8fa1"},
    {file = "ast_serialize-0.3.0-cp314-cp314t-win_arm64.whl", hash = "sha256:670f177188d128fb7f9f15b5ad0e1b553d22c34e3f584dcb83eb8077600437f0"},
    {file = "ast_serialize-0.3.0-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:2ec2fafa5e4313cc8feed96e436ebe19ac7bc6fa41fbc2827e826c48b9e4c3a9"},
    {file = "ast_serialize-0.3.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:ef6d3c08b7b4cd29b48410338e134764a00e76d25841eb02c1084e868c888ecc"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3d841424f41b886e98044abc80769c14a956e6e5ccd5fb5b0d9f5ead72be18a4"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:d21453734ad39367ede5d37efe4f59f830ce1c09f432fc72a90e368f77a4a3e7"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f5e110cdce2a347e1dd987529c88ef54d26f67848dce3eba1b3b2cc2cf085c94"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b6e23a98e57560a055f5c4b68700a0fd5ce483d2814c23140b3638c7f5d1e61"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c1c9e763d70293d65ce1e1ea8c943140c68d0953f0268c7ee0998f2e07f77dd0"},
    {file = "ast_serialize-0.3.0-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:4388a1796c228f1ce5c391426f7d21a0003ad3b47f677dbeded9bd1a85c7209f"},
    {file = "ast_serialize-0.3.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:5283cdcc0c64c3d8b9b688dc6aaa012d9c0cf1380a7f774a6bae6a1c01b3205a"},
    {file = "ast_serialize-0.3.0-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:f5ef88cc5842a5d7a6ac09dc0d5fc2c98f5d276c1f076f866d55047ce886785b"},
    {file = "ast_serialize-0.3.0-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:cc14bf402bdc0978594ecce783793de2c7470cd4f5cd7eb286ca97ed8ff7cba9"},
    {file = "ast_serialize-0.3.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:11eae0cf1b7b3e0678133cc2daa974ea972caf02eb4b3aa062af6fa9acd52c57"},
    {file = "ast_serialize-0.3.0-cp39-abi3-win32.whl", hash = "sha256:2db3dd99de5e6a5a11d7dda73de8750eb6e5baaf25245adf7bdcfe64b6108ae2"},
    {file = "ast_serialize-0.3.0-cp39-abi3-win_amd64.whl", hash = "sha256:a2cd125adccf7969470621905d302750cd25951f22ea430d9a25b7be031e5549"},
    {file = "ast_serialize-0.3.0-cp39-abi3-win_arm64.whl", hash = "sha256:0dd00da29985f15f50dc35728b7e1e7c84507bccfea1d9914738530f1c72238a"},
    {file = "ast_serialize-0.3.0.tar.gz", hash = "sha256:1bc3ca09a63a021376527c4e938deedd11d11d675ce850e6f9c7487f5889992b"},
]

[[package]]
name = "astroid"
version = "3.3.11"
description = "An abstract syntax tree for Python with inference support."
optional = false
python-versions = ">=3.9.0"
groups = ["docs"]
markers = "python_version == \"3.9\""
files = [
    {file = "astroid-3.3.11-py3-none-any.whl", hash = "sha256:54c760ae8322ece1abd213057c4b5bba7c49818853fc901ef09719a60dbf9dec"},
    {file = "astroid-3.3.11.tar.gz", hash = "sha256:1e5a5011af2920c7c67a53f65d536d65bfa7116feeaf2354d8b94f29573bb0ce"},
]

[package.dependencies]
typing-extensions = {version = ">=4", markers = "python_version < \"3.11\""}

[[package]]
name = "astroid"
version = "4.0.3"
description = "An abstract syntax tree for Python with inference support."
optional = false
python-versions = ">=3.10.0"
groups = ["docs"]
markers = "python_version >= \"3.10\""
files = [
    {file = "astroid-4.0.3-py3-none-any.whl", hash = "sha256:864a0a34af1bd70e1049ba1e61cee843a7252c826d97825fcee9b2fcbd9e1b14"},
    {file = "astroid-4.0.3.tar.gz", hash = "sha256:08d1de40d251cc3dc4a7a12726721d475ac189e4e583d596ece7422bc176bda3"},
]

[package.dependencies]
typing-extensions = {version = ">=4", markers = "python_version < \"3.11\""}

[[package]]
name = "babel"
version = "2.18.0"
description = "Internationalization utilities"
optional = false
python-versions = ">=3.8"
groups = ["docs"]
files = [
    {file = "babel-2.18.0-py3-none-any.whl", hash = "sha256:e2b422b277c2b9a9630c1d7903c2a00d0830c409c59ac8cae9081c92f1aeba35"},
    {file = "babel-2.18.0.tar.gz", hash = "sha256:b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d"},
]

[package.extras]
dev = ["backports.zoneinfo ; python_version < \"3.9\"", "freezegun (>=1.0,<2.0)", "jinja2 (>=3.0)", "pytest (>=6.0)", "pytest-cov", "pytz", "setuptools", "tzdata ; sys_platform == \"win32\""]

[[package]]
name = "bandit"
version = "1.8.6"
description = "Security oriented static analyser for python code."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "bandit-1.8.6-py3-none-any.whl", hash = "sha256:3348e934d736fcdb68b6aa4030487097e23a501adf3e7827b63658df464dddd0"},
    {file = "bandit-1.8.6.tar.gz", hash = "sha256:dbfe9c25fc6961c2078593de55fd19f2559f9e45b99f1272341f5b95dea4e56b"},
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
name = "bandit"
version = "1.9.4"
description = "Security oriented static analyser for python code."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
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
version = "25.11.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "black-25.11.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:ec311e22458eec32a807f029b2646f661e6859c3f61bc6d9ffb67958779f392e"},
    {file = "black-25.11.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:1032639c90208c15711334d681de2e24821af0575573db2810b0763bcd62e0f0"},
    {file = "black-25.11.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0c0f7c461df55cf32929b002335883946a4893d759f2df343389c4396f3b6b37"},
    {file = "black-25.11.0-cp310-cp310-win_amd64.whl", hash = "sha256:f9786c24d8e9bd5f20dc7a7f0cdd742644656987f6ea6947629306f937726c03"},
    {file = "black-25.11.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:895571922a35434a9d8ca67ef926da6bc9ad464522a5fe0db99b394ef1c0675a"},
    {file = "black-25.11.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:cb4f4b65d717062191bdec8e4a442539a8ea065e6af1c4f4d36f0cdb5f71e170"},
    {file = "black-25.11.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d81a44cbc7e4f73a9d6ae449ec2317ad81512d1e7dce7d57f6333fd6259737bc"},
    {file = "black-25.11.0-cp311-cp311-win_amd64.whl", hash = "sha256:7eebd4744dfe92ef1ee349dc532defbf012a88b087bb7ddd688ff59a447b080e"},
    {file = "black-25.11.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:80e7486ad3535636657aa180ad32a7d67d7c273a80e12f1b4bfa0823d54e8fac"},
    {file = "black-25.11.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:6cced12b747c4c76bc09b4db057c319d8545307266f41aaee665540bc0e04e96"},
    {file = "black-25.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6cb2d54a39e0ef021d6c5eef442e10fd71fcb491be6413d083a320ee768329dd"},
    {file = "black-25.11.0-cp312-cp312-win_amd64.whl", hash = "sha256:ae263af2f496940438e5be1a0c1020e13b09154f3af4df0835ea7f9fe7bfa409"},
    {file = "black-25.11.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0a1d40348b6621cc20d3d7530a5b8d67e9714906dfd7346338249ad9c6cedf2b"},
    {file = "black-25.11.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:51c65d7d60bb25429ea2bf0731c32b2a2442eb4bd3b2afcb47830f0b13e58bfd"},
    {file = "black-25.11.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:936c4dd07669269f40b497440159a221ee435e3fddcf668e0c05244a9be71993"},
    {file = "black-25.11.0-cp313-cp313-win_amd64.whl", hash = "sha256:f42c0ea7f59994490f4dccd64e6b2dd49ac57c7c84f38b8faab50f8759db245c"},
    {file = "black-25.11.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:35690a383f22dd3e468c85dc4b915217f87667ad9cce781d7b42678ce63c4170"},
    {file = "black-25.11.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:dae49ef7369c6caa1a1833fd5efb7c3024bb7e4499bf64833f65ad27791b1545"},
    {file = "black-25.11.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5bd4a22a0b37401c8e492e994bce79e614f91b14d9ea911f44f36e262195fdda"},
    {file = "black-25.11.0-cp314-cp314-win_amd64.whl", hash = "sha256:aa211411e94fdf86519996b7f5f05e71ba34835d8f0c0f03c00a26271da02664"},
    {file = "black-25.11.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:a3bb5ce32daa9ff0605d73b6f19da0b0e6c1f8f2d75594db539fdfed722f2b06"},
    {file = "black-25.11.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:9815ccee1e55717fe9a4b924cae1646ef7f54e0f990da39a34fc7b264fcf80a2"},
    {file = "black-25.11.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:92285c37b93a1698dcbc34581867b480f1ba3a7b92acf1fe0467b04d7a4da0dc"},
    {file = "black-25.11.0-cp39-cp39-win_amd64.whl", hash = "sha256:43945853a31099c7c0ff8dface53b4de56c41294fa6783c0441a8b1d9bf668bc"},
    {file = "black-25.11.0-py3-none-any.whl", hash = "sha256:e3f562da087791e96cefcd9dda058380a442ab322a02e222add53736451f604b"},
    {file = "black-25.11.0.tar.gz", hash = "sha256:9a323ac32f5dc75ce7470501b887250be5005a01602e931a15e45593f70f6e08"},
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
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
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
name = "certifi"
version = "2026.1.4"
description = "Python package for providing Mozilla's CA Bundle."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "certifi-2026.1.4-py3-none-any.whl", hash = "sha256:9943707519e4add1115f44c2bc244f782c0249876bf51b6599fee1ffbedd685c"},
    {file = "certifi-2026.1.4.tar.gz", hash = "sha256:ac726dd470482006e014ad384921ed6438c457018f4b3d204aea4281258b2120"},
]

[[package]]
name = "charset-normalizer"
version = "3.4.4"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "charset_normalizer-3.4.4-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:e824f1492727fa856dd6eda4f7cee25f8518a12f3c4a56a74e8095695089cf6d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4bd5d4137d500351a30687c2d3971758aac9a19208fc110ccb9d7188fbe709e8"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:027f6de494925c0ab2a55eab46ae5129951638a49a34d87f4c3eda90f696b4ad"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f820802628d2694cb7e56db99213f930856014862f3fd943d290ea8438d07ca8"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:798d75d81754988d2565bff1b97ba5a44411867c0cf32b77a7e8f8d84796b10d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9d1bb833febdff5c8927f922386db610b49db6e0d4f4ee29601d71e7c2694313"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9cd98cdc06614a2f768d2b7286d66805f94c48cde050acdbbb7db2600ab3197e"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:077fbb858e903c73f6c9db43374fd213b0b6a778106bc7032446a8e8b5b38b93"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:244bfb999c71b35de57821b8ea746b24e863398194a4014e4c76adc2bbdfeff0"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:64b55f9dce520635f018f907ff1b0df1fdc31f2795a922fb49dd14fbcdf48c84"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:faa3a41b2b66b6e50f84ae4a68c64fcd0c44355741c6374813a800cd6695db9e"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:6515f3182dbe4ea06ced2d9e8666d97b46ef4c75e326b79bb624110f122551db"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:cc00f04ed596e9dc0da42ed17ac5e596c6ccba999ba6bd92b0e0aef2f170f2d6"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win32.whl", hash = "sha256:f34be2938726fc13801220747472850852fe6b1ea75869a048d6f896838c896f"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win_amd64.whl", hash = "sha256:a61900df84c667873b292c3de315a786dd8dac506704dea57bc957bd31e22c7d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win_arm64.whl", hash = "sha256:cead0978fc57397645f12578bfd2d5ea9138ea0fac82b2f63f7f7c6877986a69"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:6e1fcf0720908f200cd21aa4e6750a48ff6ce4afe7ff5a79a90d5ed8a08296f8"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5f819d5fe9234f9f82d75bdfa9aef3a3d72c4d24a6e57aeaebba32a704553aa0"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:a59cb51917aa591b1c4e6a43c132f0cdc3c76dbad6155df4e28ee626cc77a0a3"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:8ef3c867360f88ac904fd3f5e1f902f13307af9052646963ee08ff4f131adafc"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d9e45d7faa48ee908174d8fe84854479ef838fc6a705c9315372eacbc2f02897"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:840c25fb618a231545cbab0564a799f101b63b9901f2569faecd6b222ac72381"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:ca5862d5b3928c4940729dacc329aa9102900382fea192fc5e52eb69d6093815"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d9c7f57c3d666a53421049053eaacdd14bbd0a528e2186fcb2e672effd053bb0"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:277e970e750505ed74c832b4bf75dac7476262ee2a013f5574dd49075879e161"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:31fd66405eaf47bb62e8cd575dc621c56c668f27d46a61d975a249930dd5e2a4"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:0d3d8f15c07f86e9ff82319b3d9ef6f4bf907608f53fe9d92b28ea9ae3d1fd89"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:9f7fcd74d410a36883701fafa2482a6af2ff5ba96b9a620e9e0721e28ead5569"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ebf3e58c7ec8a8bed6d66a75d7fb37b55e5015b03ceae72a8e7c74495551e224"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win32.whl", hash = "sha256:eecbc200c7fd5ddb9a7f16c7decb07b566c29fa2161a16cf67b8d068bd21690a"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win_amd64.whl", hash = "sha256:5ae497466c7901d54b639cf42d5b8c1b6a4fead55215500d2f486d34db48d016"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win_arm64.whl", hash = "sha256:65e2befcd84bc6f37095f5961e68a6f077bf44946771354a28ad434c2cce0ae1"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:0a98e6759f854bd25a58a73fa88833fba3b7c491169f86ce1180c948ab3fd394"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b5b290ccc2a263e8d185130284f8501e3e36c5e02750fc6b6bdeb2e9e96f1e25"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:74bb723680f9f7a6234dcf67aea57e708ec1fbdf5699fb91dfd6f511b0a320ef"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f1e34719c6ed0b92f418c7c780480b26b5d9c50349e9a9af7d76bf757530350d"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:2437418e20515acec67d86e12bf70056a33abdacb5cb1655042f6538d6b085a8"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:11d694519d7f29d6cd09f6ac70028dba10f92f6cdd059096db198c283794ac86"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:ac1c4a689edcc530fc9d9aa11f5774b9e2f33f9a0c6a57864e90908f5208d30a"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:21d142cc6c0ec30d2efee5068ca36c128a30b0f2c53c1c07bd78cb6bc1d3be5f"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:5dbe56a36425d26d6cfb40ce79c314a2e4dd6211d51d6d2191c00bed34f354cc"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:5bfbb1b9acf3334612667b61bd3002196fe2a1eb4dd74d247e0f2a4d50ec9bbf"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:d055ec1e26e441f6187acf818b73564e6e6282709e9bcb5b63f5b23068356a15"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:af2d8c67d8e573d6de5bc30cdb27e9b95e49115cd9baad5ddbd1a6207aaa82a9"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:780236ac706e66881f3b7f2f32dfe90507a09e67d1d454c762cf642e6e1586e0"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win32.whl", hash = "sha256:5833d2c39d8896e4e19b689ffc198f08ea58116bee26dea51e362ecc7cd3ed26"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win_amd64.whl", hash = "sha256:a79cfe37875f822425b89a82333404539ae63dbdddf97f84dcbc3d339aae9525"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win_arm64.whl", hash = "sha256:376bec83a63b8021bb5c8ea75e21c4ccb86e7e45ca4eb81146091b56599b80c3"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:e1f185f86a6f3403aa2420e815904c67b2f9ebc443f045edd0de921108345794"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b39f987ae8ccdf0d2642338faf2abb1862340facc796048b604ef14919e55ed"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:3162d5d8ce1bb98dd51af660f2121c55d0fa541b46dff7bb9b9f86ea1d87de72"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:81d5eb2a312700f4ecaa977a8235b634ce853200e828fbadf3a9c50bab278328"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5bd2293095d766545ec1a8f612559f6b40abc0eb18bb2f5d1171872d34036ede"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a8a8b89589086a25749f471e6a900d3f662d1d3b6e2e59dcecf787b1cc3a1894"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc7637e2f80d8530ee4a78e878bce464f70087ce73cf7c1caf142416923b98f1"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f8bf04158c6b607d747e93949aa60618b61312fe647a6369f88ce2ff16043490"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:554af85e960429cf30784dd47447d5125aaa3b99a6f0683589dbd27e2f45da44"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:74018750915ee7ad843a774364e13a3db91682f26142baddf775342c3f5b1133"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:c0463276121fdee9c49b98908b3a89c39be45d86d1dbaa22957e38f6321d4ce3"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:362d61fd13843997c1c446760ef36f240cf81d3ebf74ac62652aebaf7838561e"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9a26f18905b8dd5d685d6d07b0cdf98a79f3c7a918906af7cc143ea2e164c8bc"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win32.whl", hash = "sha256:9b35f4c90079ff2e2edc5b26c0c77925e5d2d255c42c74fdb70fb49b172726ac"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win_amd64.whl", hash = "sha256:b435cba5f4f750aa6c0a0d92c541fb79f69a387c91e61f1795227e4ed9cece14"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win_arm64.whl", hash = "sha256:542d2cee80be6f80247095cc36c418f7bddd14f4a6de45af91dfad36d817bba2"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:da3326d9e65ef63a817ecbcc0df6e94463713b754fe293eaa03da99befb9a5bd"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:8af65f14dc14a79b924524b1e7fffe304517b2bff5a58bf64f30b98bbc5079eb"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:74664978bb272435107de04e36db5a9735e78232b85b77d45cfb38f758efd33e"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:752944c7ffbfdd10c074dc58ec2d5a8a4cd9493b314d367c14d24c17684ddd14"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d1f13550535ad8cff21b8d757a3257963e951d96e20ec82ab44bc64aeb62a191"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ecaae4149d99b1c9e7b88bb03e3221956f68fd6d50be2ef061b2381b61d20838"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cb6254dc36b47a990e59e1068afacdcd02958bdcce30bb50cc1700a8b9d624a6"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:c8ae8a0f02f57a6e61203a31428fa1d677cbe50c93622b4149d5c0f319c1d19e"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:47cc91b2f4dd2833fddaedd2893006b0106129d4b94fdb6af1f4ce5a9965577c"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:82004af6c302b5d3ab2cfc4cc5f29db16123b1a8417f2e25f9066f91d4411090"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:2b7d8f6c26245217bd2ad053761201e9f9680f8ce52f0fcd8d0755aeae5b2152"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:799a7a5e4fb2d5898c60b640fd4981d6a25f1c11790935a44ce38c54e985f828"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:99ae2cffebb06e6c22bdc25801d7b30f503cc87dbd283479e7b606f70aff57ec"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win32.whl", hash = "sha256:f9d332f8c2a2fcbffe1378594431458ddbef721c1769d78e2cbc06280d8155f9"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win_amd64.whl", hash = "sha256:8a6562c3700cce886c5be75ade4a5db4214fda19fede41d9792d100288d8f94c"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win_arm64.whl", hash = "sha256:de00632ca48df9daf77a2c65a484531649261ec9f25489917f09e455cb09ddb2"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:ce8a0633f41a967713a59c4139d29110c07e826d131a316b50ce11b1d79b4f84"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:eaabd426fe94daf8fd157c32e571c85cb12e66692f15516a83a03264b08d06c3"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:c4ef880e27901b6cc782f1b95f82da9313c0eb95c3af699103088fa0ac3ce9ac"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:2aaba3b0819274cc41757a1da876f810a3e4d7b6eb25699253a4effef9e8e4af"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:778d2e08eda00f4256d7f672ca9fef386071c9202f5e4607920b86d7803387f2"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f155a433c2ec037d4e8df17d18922c3a0d9b3232a396690f17175d2946f0218d"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:a8bf8d0f749c5757af2142fe7903a9df1d2e8aa3841559b2bad34b08d0e2bcf3"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:194f08cbb32dc406d6e1aea671a68be0823673db2832b38405deba2fb0d88f63"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_armv7l.whl", hash = "sha256:6aee717dcfead04c6eb1ce3bd29ac1e22663cdea57f943c87d1eab9a025438d7"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_ppc64le.whl", hash = "sha256:cd4b7ca9984e5e7985c12bc60a6f173f3c958eae74f3ef6624bb6b26e2abbae4"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_riscv64.whl", hash = "sha256:b7cf1017d601aa35e6bb650b6ad28652c9cd78ee6caff19f3c28d03e1c80acbf"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_s390x.whl", hash = "sha256:e912091979546adf63357d7e2ccff9b44f026c075aeaf25a52d0e95ad2281074"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:5cb4d72eea50c8868f5288b7f7f33ed276118325c1dfd3957089f6b519e1382a"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-win32.whl", hash = "sha256:837c2ce8c5a65a2035be9b3569c684358dfbf109fd3b6969630a87535495ceaa"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-win_amd64.whl", hash = "sha256:44c2a8734b333e0578090c4cd6b16f275e07aa6614ca8715e6c038e865e70576"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:a9768c477b9d7bd54bc0c86dbaebdec6f03306675526c9927c0e8a04e8f94af9"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1bee1e43c28aa63cb16e5c14e582580546b08e535299b8b6158a7c9c768a1f3d"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:fd44c878ea55ba351104cb93cc85e74916eb8fa440ca7903e57575e97394f608"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:0f04b14ffe5fdc8c4933862d8306109a2c51e0704acfa35d51598eb45a1e89fc"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:cd09d08005f958f370f539f186d10aec3377d55b9eeb0d796025d4886119d76e"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4fe7859a4e3e8457458e2ff592f15ccb02f3da787fcd31e0183879c3ad4692a1"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fa09f53c465e532f4d3db095e0c55b615f010ad81803d383195b6b5ca6cbf5f3"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:7fa17817dc5625de8a027cb8b26d9fefa3ea28c8253929b8d6649e705d2835b6"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:5947809c8a2417be3267efc979c47d76a079758166f7d43ef5ae8e9f92751f88"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:4902828217069c3c5c71094537a8e623f5d097858ac6ca8252f7b4d10b7560f1"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:7c308f7e26e4363d79df40ca5b2be1c6ba9f02bdbccfed5abddb7859a6ce72cf"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:2c9d3c380143a1fedbff95a312aa798578371eb29da42106a29019368a475318"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:cb01158d8b88ee68f15949894ccc6712278243d95f344770fa7593fa2d94410c"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win32.whl", hash = "sha256:2677acec1a2f8ef614c6888b5b4ae4060cc184174a938ed4e8ef690e15d3e505"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win_amd64.whl", hash = "sha256:f8e160feb2aed042cd657a72acc0b481212ed28b1b9a95c0cee1621b524e1966"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win_arm64.whl", hash = "sha256:b5d84d37db046c5ca74ee7bb47dd6cbc13f80665fdde3e8040bdd3fb015ecb50"},
    {file = "charset_normalizer-3.4.4-py3-none-any.whl", hash = "sha256:7a32c560861a02ff789ad905a2fe94e3f840803362c84fecf1851cb4cf3dc37f"},
    {file = "charset_normalizer-3.4.4.tar.gz", hash = "sha256:94537985111c35f28720e43603b8e7b43a6ecfb2ce1d3058bbe955b73404e21a"},
]

[[package]]
name = "click"
version = "8.1.8"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "click-8.1.8-py3-none-any.whl", hash = "sha256:63c132bbbed01578a06712a2d1f497bb62d9c1c0d329b7903a866228027263b2"},
    {file = "click-8.1.8.tar.gz", hash = "sha256:ed53c9d8990d83c2a27deae68e4ee337473f6330c040a31d4225c9574d16096a"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "click"
version = "8.3.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
files = [
    {file = "click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6"},
    {file = "click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["docs", "lint", "test"]
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]
markers = {docs = "sys_platform == \"win32\"", lint = "platform_system == \"Windows\"", test = "sys_platform == \"win32\""}

[[package]]
name = "coverage"
version = "7.10.7"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.9"
groups = ["test"]
markers = "python_version == \"3.9\""
files = [
    {file = "coverage-7.10.7-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:fc04cc7a3db33664e0c2d10eb8990ff6b3536f6842c9590ae8da4c614b9ed05a"},
    {file = "coverage-7.10.7-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e201e015644e207139f7e2351980feb7040e6f4b2c2978892f3e3789d1c125e5"},
    {file = "coverage-7.10.7-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:240af60539987ced2c399809bd34f7c78e8abe0736af91c3d7d0e795df633d17"},
    {file = "coverage-7.10.7-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:8421e088bc051361b01c4b3a50fd39a4b9133079a2229978d9d30511fd05231b"},
    {file = "coverage-7.10.7-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6be8ed3039ae7f7ac5ce058c308484787c86e8437e72b30bf5e88b8ea10f3c87"},
    {file = "coverage-7.10.7-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e28299d9f2e889e6d51b1f043f58d5f997c373cc12e6403b90df95b8b047c13e"},
    {file = "coverage-7.10.7-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:c4e16bd7761c5e454f4efd36f345286d6f7c5fa111623c355691e2755cae3b9e"},
    {file = "coverage-7.10.7-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:b1c81d0e5e160651879755c9c675b974276f135558cf4ba79fee7b8413a515df"},
    {file = "coverage-7.10.7-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:606cc265adc9aaedcc84f1f064f0e8736bc45814f15a357e30fca7ecc01504e0"},
    {file = "coverage-7.10.7-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:10b24412692df990dbc34f8fb1b6b13d236ace9dfdd68df5b28c2e39cafbba13"},
    {file = "coverage-7.10.7-cp310-cp310-win32.whl", hash = "sha256:b51dcd060f18c19290d9b8a9dd1e0181538df2ce0717f562fff6cf74d9fc0b5b"},
    {file = "coverage-7.10.7-cp310-cp310-win_amd64.whl", hash = "sha256:3a622ac801b17198020f09af3eaf45666b344a0d69fc2a6ffe2ea83aeef1d807"},
    {file = "coverage-7.10.7-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a609f9c93113be646f44c2a0256d6ea375ad047005d7f57a5c15f614dc1b2f59"},
    {file = "coverage-7.10.7-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:65646bb0359386e07639c367a22cf9b5bf6304e8630b565d0626e2bdf329227a"},
    {file = "coverage-7.10.7-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:5f33166f0dfcce728191f520bd2692914ec70fac2713f6bf3ce59c3deacb4699"},
    {file = "coverage-7.10.7-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:35f5e3f9e455bb17831876048355dca0f758b6df22f49258cb5a91da23ef437d"},
    {file = "coverage-7.10.7-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4da86b6d62a496e908ac2898243920c7992499c1712ff7c2b6d837cc69d9467e"},
    {file = "coverage-7.10.7-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:6b8b09c1fad947c84bbbc95eca841350fad9cbfa5a2d7ca88ac9f8d836c92e23"},
    {file = "coverage-7.10.7-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:4376538f36b533b46f8971d3a3e63464f2c7905c9800db97361c43a2b14792ab"},
    {file = "coverage-7.10.7-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:121da30abb574f6ce6ae09840dae322bef734480ceafe410117627aa54f76d82"},
    {file = "coverage-7.10.7-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:88127d40df529336a9836870436fc2751c339fbaed3a836d42c93f3e4bd1d0a2"},
    {file = "coverage-7.10.7-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ba58bbcd1b72f136080c0bccc2400d66cc6115f3f906c499013d065ac33a4b61"},
    {file = "coverage-7.10.7-cp311-cp311-win32.whl", hash = "sha256:972b9e3a4094b053a4e46832b4bc829fc8a8d347160eb39d03f1690316a99c14"},
    {file = "coverage-7.10.7-cp311-cp311-win_amd64.whl", hash = "sha256:a7b55a944a7f43892e28ad4bc0561dfd5f0d73e605d1aa5c3c976b52aea121d2"},
    {file = "coverage-7.10.7-cp311-cp311-win_arm64.whl", hash = "sha256:736f227fb490f03c6488f9b6d45855f8e0fd749c007f9303ad30efab0e73c05a"},
    {file = "coverage-7.10.7-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7bb3b9ddb87ef7725056572368040c32775036472d5a033679d1fa6c8dc08417"},
    {file = "coverage-7.10.7-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:18afb24843cbc175687225cab1138c95d262337f5473512010e46831aa0c2973"},
    {file = "coverage-7.10.7-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:399a0b6347bcd3822be369392932884b8216d0944049ae22925631a9b3d4ba4c"},
    {file = "coverage-7.10.7-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:314f2c326ded3f4b09be11bc282eb2fc861184bc95748ae67b360ac962770be7"},
    {file = "coverage-7.10.7-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c41e71c9cfb854789dee6fc51e46743a6d138b1803fab6cb860af43265b42ea6"},
    {file = "coverage-7.10.7-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc01f57ca26269c2c706e838f6422e2a8788e41b3e3c65e2f41148212e57cd59"},
    {file = "coverage-7.10.7-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a6442c59a8ac8b85812ce33bc4d05bde3fb22321fa8294e2a5b487c3505f611b"},
    {file = "coverage-7.10.7-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:78a384e49f46b80fb4c901d52d92abe098e78768ed829c673fbb53c498bef73a"},
    {file = "coverage-7.10.7-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:5e1e9802121405ede4b0133aa4340ad8186a1d2526de5b7c3eca519db7bb89fb"},
    {file = "coverage-7.10.7-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:d41213ea25a86f69efd1575073d34ea11aabe075604ddf3d148ecfec9e1e96a1"},
    {file = "coverage-7.10.7-cp312-cp312-win32.whl", hash = "sha256:77eb4c747061a6af8d0f7bdb31f1e108d172762ef579166ec84542f711d90256"},
    {file = "coverage-7.10.7-cp312-cp312-win_amd64.whl", hash = "sha256:f51328ffe987aecf6d09f3cd9d979face89a617eacdaea43e7b3080777f647ba"},
    {file = "coverage-7.10.7-cp312-cp312-win_arm64.whl", hash = "sha256:bda5e34f8a75721c96085903c6f2197dc398c20ffd98df33f866a9c8fd95f4bf"},
    {file = "coverage-7.10.7-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:981a651f543f2854abd3b5fcb3263aac581b18209be49863ba575de6edf4c14d"},
    {file = "coverage-7.10.7-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:73ab1601f84dc804f7812dc297e93cd99381162da39c47040a827d4e8dafe63b"},
    {file = "coverage-7.10.7-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:a8b6f03672aa6734e700bbcd65ff050fd19cddfec4b031cc8cf1c6967de5a68e"},
    {file = "coverage-7.10.7-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:10b6ba00ab1132a0ce4428ff68cf50a25efd6840a42cdf4239c9b99aad83be8b"},
    {file = "coverage-7.10.7-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c79124f70465a150e89340de5963f936ee97097d2ef76c869708c4248c63ca49"},
    {file = "coverage-7.10.7-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:69212fbccdbd5b0e39eac4067e20a4a5256609e209547d86f740d68ad4f04911"},
    {file = "coverage-7.10.7-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:7ea7c6c9d0d286d04ed3541747e6597cbe4971f22648b68248f7ddcd329207f0"},
    {file = "coverage-7.10.7-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:b9be91986841a75042b3e3243d0b3cb0b2434252b977baaf0cd56e960fe1e46f"},
    {file = "coverage-7.10.7-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:b281d5eca50189325cfe1f365fafade89b14b4a78d9b40b05ddd1fc7d2a10a9c"},
    {file = "coverage-7.10.7-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:99e4aa63097ab1118e75a848a28e40d68b08a5e19ce587891ab7fd04475e780f"},
    {file = "coverage-7.10.7-cp313-cp313-win32.whl", hash = "sha256:dc7c389dce432500273eaf48f410b37886be9208b2dd5710aaf7c57fd442c698"},
    {file = "coverage-7.10.7-cp313-cp313-win_amd64.whl", hash = "sha256:cac0fdca17b036af3881a9d2729a850b76553f3f716ccb0360ad4dbc06b3b843"},
    {file = "coverage-7.10.7-cp313-cp313-win_arm64.whl", hash = "sha256:4b6f236edf6e2f9ae8fcd1332da4e791c1b6ba0dc16a2dc94590ceccb482e546"},
    {file = "coverage-7.10.7-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:a0ec07fd264d0745ee396b666d47cef20875f4ff2375d7c4f58235886cc1ef0c"},
    {file = "coverage-7.10.7-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:dd5e856ebb7bfb7672b0086846db5afb4567a7b9714b8a0ebafd211ec7ce6a15"},
    {file = "coverage-7.10.7-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:f57b2a3c8353d3e04acf75b3fed57ba41f5c0646bbf1d10c7c282291c97936b4"},
    {file = "coverage-7.10.7-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:1ef2319dd15a0b009667301a3f84452a4dc6fddfd06b0c5c53ea472d3989fbf0"},
    {file = "coverage-7.10.7-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:83082a57783239717ceb0ad584de3c69cf581b2a95ed6bf81ea66034f00401c0"},
    {file = "coverage-7.10.7-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:50aa94fb1fb9a397eaa19c0d5ec15a5edd03a47bf1a3a6111a16b36e190cff65"},
    {file = "coverage-7.10.7-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2120043f147bebb41c85b97ac45dd173595ff14f2a584f2963891cbcc3091541"},
    {file = "coverage-7.10.7-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:2fafd773231dd0378fdba66d339f84904a8e57a262f583530f4f156ab83863e6"},
    {file = "coverage-7.10.7-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:0b944ee8459f515f28b851728ad224fa2d068f1513ef6b7ff1efafeb2185f999"},
    {file = "coverage-7.10.7-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:4b583b97ab2e3efe1b3e75248a9b333bd3f8b0b1b8e5b45578e05e5850dfb2c2"},
    {file = "coverage-7.10.7-cp313-cp313t-win32.whl", hash = "sha256:2a78cd46550081a7909b3329e2266204d584866e8d97b898cd7fb5ac8d888b1a"},
    {file = "coverage-7.10.7-cp313-cp313t-win_amd64.whl", hash = "sha256:33a5e6396ab684cb43dc7befa386258acb2d7fae7f67330ebb85ba4ea27938eb"},
    {file = "coverage-7.10.7-cp313-cp313t-win_arm64.whl", hash = "sha256:86b0e7308289ddde73d863b7683f596d8d21c7d8664ce1dee061d0bcf3fbb4bb"},
    {file = "coverage-7.10.7-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:b06f260b16ead11643a5a9f955bd4b5fd76c1a4c6796aeade8520095b75de520"},
    {file = "coverage-7.10.7-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:212f8f2e0612778f09c55dd4872cb1f64a1f2b074393d139278ce902064d5b32"},
    {file = "coverage-7.10.7-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:3445258bcded7d4aa630ab8296dea4d3f15a255588dd535f980c193ab6b95f3f"},
    {file = "coverage-7.10.7-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:bb45474711ba385c46a0bfe696c695a929ae69ac636cda8f532be9e8c93d720a"},
    {file = "coverage-7.10.7-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:813922f35bd800dca9994c5971883cbc0d291128a5de6b167c7aa697fcf59360"},
    {file = "coverage-7.10.7-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:93c1b03552081b2a4423091d6fb3787265b8f86af404cff98d1b5342713bdd69"},
    {file = "coverage-7.10.7-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:cc87dd1b6eaf0b848eebb1c86469b9f72a1891cb42ac7adcfbce75eadb13dd14"},
    {file = "coverage-7.10.7-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:39508ffda4f343c35f3236fe8d1a6634a51f4581226a1262769d7f970e73bffe"},
    {file = "coverage-7.10.7-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:925a1edf3d810537c5a3abe78ec5530160c5f9a26b1f4270b40e62cc79304a1e"},
    {file = "coverage-7.10.7-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2c8b9a0636f94c43cd3576811e05b89aa9bc2d0a85137affc544ae5cb0e4bfbd"},
    {file = "coverage-7.10.7-cp314-cp314-win32.whl", hash = "sha256:b7b8288eb7cdd268b0304632da8cb0bb93fadcfec2fe5712f7b9cc8f4d487be2"},
    {file = "coverage-7.10.7-cp314-cp314-win_amd64.whl", hash = "sha256:1ca6db7c8807fb9e755d0379ccc39017ce0a84dcd26d14b5a03b78563776f681"},
    {file = "coverage-7.10.7-cp314-cp314-win_arm64.whl", hash = "sha256:097c1591f5af4496226d5783d036bf6fd6cd0cbc132e071b33861de756efb880"},
    {file = "coverage-7.10.7-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:a62c6ef0d50e6de320c270ff91d9dd0a05e7250cac2a800b7784bae474506e63"},
    {file = "coverage-7.10.7-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:9fa6e4dd51fe15d8738708a973470f67a855ca50002294852e9571cdbd9433f2"},
    {file = "coverage-7.10.7-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:8fb190658865565c549b6b4706856d6a7b09302c797eb2cf8e7fe9dabb043f0d"},
    {file = "coverage-7.10.7-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:affef7c76a9ef259187ef31599a9260330e0335a3011732c4b9effa01e1cd6e0"},
    {file = "coverage-7.10.7-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6e16e07d85ca0cf8bafe5f5d23a0b850064e8e945d5677492b06bbe6f09cc699"},
    {file = "coverage-7.10.7-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:03ffc58aacdf65d2a82bbeb1ffe4d01ead4017a21bfd0454983b88ca73af94b9"},
    {file = "coverage-7.10.7-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:1b4fd784344d4e52647fd7857b2af5b3fbe6c239b0b5fa63e94eb67320770e0f"},
    {file = "coverage-7.10.7-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:0ebbaddb2c19b71912c6f2518e791aa8b9f054985a0769bdb3a53ebbc765c6a1"},
    {file = "coverage-7.10.7-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:a2d9a3b260cc1d1dbdb1c582e63ddcf5363426a1a68faa0f5da28d8ee3c722a0"},
    {file = "coverage-7.10.7-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:a3cc8638b2480865eaa3926d192e64ce6c51e3d29c849e09d5b4ad95efae5399"},
    {file = "coverage-7.10.7-cp314-cp314t-win32.whl", hash = "sha256:67f8c5cbcd3deb7a60b3345dffc89a961a484ed0af1f6f73de91705cc6e31235"},
    {file = "coverage-7.10.7-cp314-cp314t-win_amd64.whl", hash = "sha256:e1ed71194ef6dea7ed2d5cb5f7243d4bcd334bfb63e59878519be558078f848d"},
    {file = "coverage-7.10.7-cp314-cp314t-win_arm64.whl", hash = "sha256:7fe650342addd8524ca63d77b2362b02345e5f1a093266787d210c70a50b471a"},
    {file = "coverage-7.10.7-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:fff7b9c3f19957020cac546c70025331113d2e61537f6e2441bc7657913de7d3"},
    {file = "coverage-7.10.7-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:bc91b314cef27742da486d6839b677b3f2793dfe52b51bbbb7cf736d5c29281c"},
    {file = "coverage-7.10.7-cp39-cp39-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:567f5c155eda8df1d3d439d40a45a6a5f029b429b06648235f1e7e51b522b396"},
    {file = "coverage-7.10.7-cp39-cp39-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:2af88deffcc8a4d5974cf2d502251bc3b2db8461f0b66d80a449c33757aa9f40"},
    {file = "coverage-7.10.7-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c7315339eae3b24c2d2fa1ed7d7a38654cba34a13ef19fbcb9425da46d3dc594"},
    {file = "coverage-7.10.7-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:912e6ebc7a6e4adfdbb1aec371ad04c68854cd3bf3608b3514e7ff9062931d8a"},
    {file = "coverage-7.10.7-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:f49a05acd3dfe1ce9715b657e28d138578bc40126760efb962322c56e9ca344b"},
    {file = "coverage-7.10.7-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:cce2109b6219f22ece99db7644b9622f54a4e915dad65660ec435e89a3ea7cc3"},
    {file = "coverage-7.10.7-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:f3c887f96407cea3916294046fc7dab611c2552beadbed4ea901cbc6a40cc7a0"},
    {file = "coverage-7.10.7-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:635adb9a4507c9fd2ed65f39693fa31c9a3ee3a8e6dc64df033e8fdf52a7003f"},
    {file = "coverage-7.10.7-cp39-cp39-win32.whl", hash = "sha256:5a02d5a850e2979b0a014c412573953995174743a3f7fa4ea5a6e9a3c5617431"},
    {file = "coverage-7.10.7-cp39-cp39-win_amd64.whl", hash = "sha256:c134869d5ffe34547d14e174c866fd8fe2254918cc0a95e99052903bc1543e07"},
    {file = "coverage-7.10.7-py3-none-any.whl", hash = "sha256:f7941f6f2fe6dd6807a1208737b8a0cbcf1cc6d7b07d24998ad2d63590868260"},
    {file = "coverage-7.10.7.tar.gz", hash = "sha256:f4ab143ab113be368a3e9b795f9cd7906c5ef407d6173fe9675a902e1fffc239"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "coverage"
version = "7.13.3"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.10"
groups = ["test"]
markers = "python_version >= \"3.10\""
files = [
    {file = "coverage-7.13.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:0b4f345f7265cdbdb5ec2521ffff15fa49de6d6c39abf89fc7ad68aa9e3a55f0"},
    {file = "coverage-7.13.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:96c3be8bae9d0333e403cc1a8eb078a7f928b5650bae94a18fb4820cc993fb9b"},
    {file = "coverage-7.13.3-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:d6f4a21328ea49d38565b55599e1c02834e76583a6953e5586d65cb1efebd8f8"},
    {file = "coverage-7.13.3-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:fc970575799a9d17d5c3fafd83a0f6ccf5d5117cdc9ad6fbd791e9ead82418b0"},
    {file = "coverage-7.13.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:87ff33b652b3556b05e204ae20793d1f872161b0fa5ec8a9ac76f8430e152ed6"},
    {file = "coverage-7.13.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7df8759ee57b9f3f7b66799b7660c282f4375bef620ade1686d6a7b03699e75f"},
    {file = "coverage-7.13.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:f45c9bcb16bee25a798ccba8a2f6a1251b19de6a0d617bb365d7d2f386c4e20e"},
    {file = "coverage-7.13.3-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:318b2e4753cbf611061e01b6cc81477e1cdfeb69c36c4a14e6595e674caadb56"},
    {file = "coverage-7.13.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:24db3959de8ee394eeeca89ccb8ba25305c2da9a668dd44173394cbd5aa0777f"},
    {file = "coverage-7.13.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:be14d0622125edef21b3a4d8cd2d138c4872bf6e38adc90fd92385e3312f406a"},
    {file = "coverage-7.13.3-cp310-cp310-win32.whl", hash = "sha256:53be4aab8ddef18beb6188f3a3fdbf4d1af2277d098d4e618be3a8e6c88e74be"},
    {file = "coverage-7.13.3-cp310-cp310-win_amd64.whl", hash = "sha256:bfeee64ad8b4aae3233abb77eb6b52b51b05fa89da9645518671b9939a78732b"},
    {file = "coverage-7.13.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:5907605ee20e126eeee2abe14aae137043c2c8af2fa9b38d2ab3b7a6b8137f73"},
    {file = "coverage-7.13.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:a88705500988c8acad8b8fd86c2a933d3aa96bec1ddc4bc5cb256360db7bbd00"},
    {file = "coverage-7.13.3-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:7bbb5aa9016c4c29e3432e087aa29ebee3f8fda089cfbfb4e6d64bd292dcd1c2"},
    {file = "coverage-7.13.3-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:0c2be202a83dde768937a61cdc5d06bf9fb204048ca199d93479488e6247656c"},
    {file = "coverage-7.13.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f45e32ef383ce56e0ca099b2e02fcdf7950be4b1b56afaab27b4ad790befe5b"},
    {file = "coverage-7.13.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:6ed2e787249b922a93cd95c671cc9f4c9797a106e81b455c83a9ddb9d34590c0"},
    {file = "coverage-7.13.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:05dd25b21afffe545e808265897c35f32d3e4437663923e0d256d9ab5031fb14"},
    {file = "coverage-7.13.3-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:46d29926349b5c4f1ea4fca95e8c892835515f3600995a383fa9a923b5739ea4"},
    {file = "coverage-7.13.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:fae6a21537519c2af00245e834e5bf2884699cc7c1055738fd0f9dc37a3644ad"},
    {file = "coverage-7.13.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:c672d4e2f0575a4ca2bf2aa0c5ced5188220ab806c1bb6d7179f70a11a017222"},
    {file = "coverage-7.13.3-cp311-cp311-win32.whl", hash = "sha256:fcda51c918c7a13ad93b5f89a58d56e3a072c9e0ba5c231b0ed81404bf2648fb"},
    {file = "coverage-7.13.3-cp311-cp311-win_amd64.whl", hash = "sha256:d1a049b5c51b3b679928dd35e47c4a2235e0b6128b479a7596d0ef5b42fa6301"},
    {file = "coverage-7.13.3-cp311-cp311-win_arm64.whl", hash = "sha256:79f2670c7e772f4917895c3d89aad59e01f3dbe68a4ed2d0373b431fad1dcfba"},
    {file = "coverage-7.13.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:ed48b4170caa2c4420e0cd27dc977caaffc7eecc317355751df8373dddcef595"},
    {file = "coverage-7.13.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8f2adf4bcffbbec41f366f2e6dffb9d24e8172d16e91da5799c9b7ed6b5716e6"},
    {file = "coverage-7.13.3-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:01119735c690786b6966a1e9f098da4cd7ca9174c4cfe076d04e653105488395"},
    {file = "coverage-7.13.3-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:8bb09e83c603f152d855f666d70a71765ca8e67332e5829e62cb9466c176af23"},
    {file = "coverage-7.13.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b607a40cba795cfac6d130220d25962931ce101f2f478a29822b19755377fb34"},
    {file = "coverage-7.13.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:44f14a62f5da2e9aedf9080e01d2cda61df39197d48e323538ec037336d68da8"},
    {file = "coverage-7.13.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:debf29e0b157769843dff0981cc76f79e0ed04e36bb773c6cac5f6029054bd8a"},
    {file = "coverage-7.13.3-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:824bb95cd71604031ae9a48edb91fd6effde669522f960375668ed21b36e3ec4"},
    {file = "coverage-7.13.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:8f1010029a5b52dc427c8e2a8dbddb2303ddd180b806687d1acd1bb1d06649e7"},
    {file = "coverage-7.13.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:cd5dee4fd7659d8306ffa79eeaaafd91fa30a302dac3af723b9b469e549247e0"},
    {file = "coverage-7.13.3-cp312-cp312-win32.whl", hash = "sha256:f7f153d0184d45f3873b3ad3ad22694fd73aadcb8cdbc4337ab4b41ea6b4dff1"},
    {file = "coverage-7.13.3-cp312-cp312-win_amd64.whl", hash = "sha256:03a6e5e1e50819d6d7436f5bc40c92ded7e484e400716886ac921e35c133149d"},
    {file = "coverage-7.13.3-cp312-cp312-win_arm64.whl", hash = "sha256:51c4c42c0e7d09a822b08b6cf79b3c4db8333fffde7450da946719ba0d45730f"},
    {file = "coverage-7.13.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:853c3d3c79ff0db65797aad79dee6be020efd218ac4510f15a205f1e8d13ce25"},
    {file = "coverage-7.13.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f75695e157c83d374f88dcc646a60cb94173304a9258b2e74ba5a66b7614a51a"},
    {file = "coverage-7.13.3-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:2d098709621d0819039f3f1e471ee554f55a0b2ac0d816883c765b14129b5627"},
    {file = "coverage-7.13.3-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:16d23d6579cf80a474ad160ca14d8b319abaa6db62759d6eef53b2fc979b58c8"},
    {file = "coverage-7.13.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:00d34b29a59d2076e6f318b30a00a69bf63687e30cd882984ed444e753990cc1"},
    {file = "coverage-7.13.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:ab6d72bffac9deb6e6cb0f61042e748de3f9f8e98afb0375a8e64b0b6e11746b"},
    {file = "coverage-7.13.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e129328ad1258e49cae0123a3b5fcb93d6c2fa90d540f0b4c7cdcdc019aaa3dc"},
    {file = "coverage-7.13.3-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2213a8d88ed35459bda71597599d4eec7c2ebad201c88f0bfc2c26fd9b0dd2ea"},
    {file = "coverage-7.13.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:00dd3f02de6d5f5c9c3d95e3e036c3c2e2a669f8bf2d3ceb92505c4ce7838f67"},
    {file = "coverage-7.13.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f9bada7bc660d20b23d7d312ebe29e927b655cf414dadcdb6335a2075695bd86"},
    {file = "coverage-7.13.3-cp313-cp313-win32.whl", hash = "sha256:75b3c0300f3fa15809bd62d9ca8b170eb21fcf0100eb4b4154d6dc8b3a5bbd43"},
    {file = "coverage-7.13.3-cp313-cp313-win_amd64.whl", hash = "sha256:a2f7589c6132c44c53f6e705e1a6677e2b7821378c22f7703b2cf5388d0d4587"},
    {file = "coverage-7.13.3-cp313-cp313-win_arm64.whl", hash = "sha256:123ceaf2b9d8c614f01110f908a341e05b1b305d6b2ada98763b9a5a59756051"},
    {file = "coverage-7.13.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:cc7fd0f726795420f3678ac82ff882c7fc33770bd0074463b5aef7293285ace9"},
    {file = "coverage-7.13.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:d358dc408edc28730aed5477a69338e444e62fba0b7e9e4a131c505fadad691e"},
    {file = "coverage-7.13.3-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:5d67b9ed6f7b5527b209b24b3df9f2e5bf0198c1bbf99c6971b0e2dcb7e2a107"},
    {file = "coverage-7.13.3-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:59224bfb2e9b37c1335ae35d00daa3a5b4e0b1a20f530be208fff1ecfa436f43"},
    {file = "coverage-7.13.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ae9306b5299e31e31e0d3b908c66bcb6e7e3ddca143dea0266e9ce6c667346d3"},
    {file = "coverage-7.13.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:343aaeb5f8bb7bcd38620fd7bc56e6ee8207847d8c6103a1e7b72322d381ba4a"},
    {file = "coverage-7.13.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:b2182129f4c101272ff5f2f18038d7b698db1bf8e7aa9e615cb48440899ad32e"},
    {file = "coverage-7.13.3-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:94d2ac94bd0cc57c5626f52f8c2fffed1444b5ae8c9fc68320306cc2b255e155"},
    {file = "coverage-7.13.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:65436cde5ecabe26fb2f0bf598962f0a054d3f23ad529361326ac002c61a2a1e"},
    {file = "coverage-7.13.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:db83b77f97129813dbd463a67e5335adc6a6a91db652cc085d60c2d512746f96"},
    {file = "coverage-7.13.3-cp313-cp313t-win32.whl", hash = "sha256:dfb428e41377e6b9ba1b0a32df6db5409cb089a0ed1d0a672dc4953ec110d84f"},
    {file = "coverage-7.13.3-cp313-cp313t-win_amd64.whl", hash = "sha256:5badd7e596e6b0c89aa8ec6d37f4473e4357f982ce57f9a2942b0221cd9cf60c"},
    {file = "coverage-7.13.3-cp313-cp313t-win_arm64.whl", hash = "sha256:989aa158c0eb19d83c76c26f4ba00dbb272485c56e452010a3450bdbc9daafd9"},
    {file = "coverage-7.13.3-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:c6f6169bbdbdb85aab8ac0392d776948907267fcc91deeacf6f9d55f7a83ae3b"},
    {file = "coverage-7.13.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2f5e731627a3d5ef11a2a35aa0c6f7c435867c7ccbc391268eb4f2ca5dbdcc10"},
    {file = "coverage-7.13.3-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:9db3a3285d91c0b70fab9f39f0a4aa37d375873677efe4e71e58d8321e8c5d39"},
    {file = "coverage-7.13.3-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:06e49c5897cb12e3f7ecdc111d44e97c4f6d0557b81a7a0204ed70a8b038f86f"},
    {file = "coverage-7.13.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:fb25061a66802df9fc13a9ba1967d25faa4dae0418db469264fd9860a921dde4"},
    {file = "coverage-7.13.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:99fee45adbb1caeb914da16f70e557fb7ff6ddc9e4b14de665bd41af631367ef"},
    {file = "coverage-7.13.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:318002f1fd819bdc1651c619268aa5bc853c35fa5cc6d1e8c96bd9cd6c828b75"},
    {file = "coverage-7.13.3-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:71295f2d1d170b9977dc386d46a7a1b7cbb30e5405492529b4c930113a33f895"},
    {file = "coverage-7.13.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:5b1ad2e0dc672625c44bc4fe34514602a9fd8b10d52ddc414dc585f74453516c"},
    {file = "coverage-7.13.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b2beb64c145593a50d90db5c7178f55daeae129123b0d265bdb3cbec83e5194a"},
    {file = "coverage-7.13.3-cp314-cp314-win32.whl", hash = "sha256:3d1aed4f4e837a832df2f3b4f68a690eede0de4560a2dbc214ea0bc55aabcdb4"},
    {file = "coverage-7.13.3-cp314-cp314-win_amd64.whl", hash = "sha256:9f9efbbaf79f935d5fbe3ad814825cbce4f6cdb3054384cb49f0c0f496125fa0"},
    {file = "coverage-7.13.3-cp314-cp314-win_arm64.whl", hash = "sha256:31b6e889c53d4e6687ca63706148049494aace140cffece1c4dc6acadb70a7b3"},
    {file = "coverage-7.13.3-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:c5e9787cec750793a19a28df7edd85ac4e49d3fb91721afcdc3b86f6c08d9aa8"},
    {file = "coverage-7.13.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:e5b86db331c682fd0e4be7098e6acee5e8a293f824d41487c667a93705d415ca"},
    {file = "coverage-7.13.3-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:edc7754932682d52cf6e7a71806e529ecd5ce660e630e8bd1d37109a2e5f63ba"},
    {file = "coverage-7.13.3-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:d3a16d6398666510a6886f67f43d9537bfd0e13aca299688a19daa84f543122f"},
    {file = "coverage-7.13.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:303d38b19626c1981e1bb067a9928236d88eb0e4479b18a74812f05a82071508"},
    {file = "coverage-7.13.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:284e06eadfe15ddfee2f4ee56631f164ef897a7d7d5a15bca5f0bb88889fc5ba"},
    {file = "coverage-7.13.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d401f0864a1d3198422816878e4e84ca89ec1c1bf166ecc0ae01380a39b888cd"},
    {file = "coverage-7.13.3-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:3f379b02c18a64de78c4ccdddf1c81c2c5ae1956c72dacb9133d7dd7809794ab"},
    {file = "coverage-7.13.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:7a482f2da9086971efb12daca1d6547007ede3674ea06e16d7663414445c683e"},
    {file = "coverage-7.13.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:562136b0d401992118d9b49fbee5454e16f95f85b120a4226a04d816e33fe024"},
    {file = "coverage-7.13.3-cp314-cp314t-win32.whl", hash = "sha256:ca46e5c3be3b195098dd88711890b8011a9fa4feca942292bb84714ce5eab5d3"},
    {file = "coverage-7.13.3-cp314-cp314t-win_amd64.whl", hash = "sha256:06d316dbb3d9fd44cca05b2dbcfbef22948493d63a1f28e828d43e6cc505fed8"},
    {file = "coverage-7.13.3-cp314-cp314t-win_arm64.whl", hash = "sha256:299d66e9218193f9dc6e4880629ed7c4cd23486005166247c283fb98531656c3"},
    {file = "coverage-7.13.3-py3-none-any.whl", hash = "sha256:90a8af9dba6429b2573199622d72e0ebf024d6276f16abce394ad4d181bb0910"},
    {file = "coverage-7.13.3.tar.gz", hash = "sha256:f7f6182d3dfb8802c1747eacbfe611b669455b69b7c037484bb1efbbb56711ac"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "docutils"
version = "0.21.2"
description = "Docutils -- Python Documentation Utilities"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version < \"3.11\""
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
groups = ["test"]
markers = "python_version < \"3.11\""
files = [
    {file = "exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598"},
    {file = "exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219"},
]

[package.dependencies]
typing-extensions = {version = ">=4.6.0", markers = "python_version < \"3.13\""}

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["lint"]
markers = "python_version < \"3.13\" and python_version != \"3.12\" and (python_version < \"3.12\" or implementation_name != \"pypy\")"
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
name = "idna"
version = "3.11"
description = "Internationalized Domain Names in Applications (IDNA)"
optional = false
python-versions = ">=3.8"
groups = ["docs"]
files = [
    {file = "idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea"},
    {file = "idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902"},
]

[package.extras]
all = ["flake8 (>=7.1.1)", "mypy (>=1.11.2)", "pytest (>=8.3.2)", "ruff (>=0.6.2)"]

[[package]]
name = "imagesize"
version = "1.4.1"
description = "Getting image size from png/jpeg/jpeg2000/gif file"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
groups = ["docs"]
files = [
    {file = "imagesize-1.4.1-py2.py3-none-any.whl", hash = "sha256:0d8d18d08f840c19d0ee7ca1fd82490fdc3729b7ac93f49870406ddde8ef8d8b"},
    {file = "imagesize-1.4.1.tar.gz", hash = "sha256:69150444affb9cb0d5cc5a92b3676f0b2fb7cd9ae39e947a5e11a36b4497cd4a"},
]

[[package]]
name = "importlib-metadata"
version = "8.7.1"
description = "Read metadata from Python packages"
optional = false
python-versions = ">=3.9"
groups = ["docs", "lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "importlib_metadata-8.7.1-py3-none-any.whl", hash = "sha256:5a1f80bf1daa489495071efbb095d75a634cf28a8bc299581244063b53176151"},
    {file = "importlib_metadata-8.7.1.tar.gz", hash = "sha256:49fef1ae6440c182052f407c8d34a68f72efc36db9ca90dc0113398f2fdde8bb"},
]

[package.dependencies]
zipp = ">=3.20"

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\""]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-lint"]
enabler = ["pytest-enabler (>=3.4)"]
perf = ["ipython"]
test = ["flufl.flake8", "jaraco.test (>=5.4)", "packaging", "pyfakefs", "pytest (>=6,!=8.1.*)", "pytest-perf (>=0.9.2)"]
type = ["mypy (<1.19) ; platform_python_implementation == \"PyPy\"", "pytest-mypy (>=1.0.1)"]

[[package]]
name = "iniconfig"
version = "2.1.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.8"
groups = ["test"]
markers = "python_version == \"3.9\""
files = [
    {file = "iniconfig-2.1.0-py3-none-any.whl", hash = "sha256:9deba5723312380e77435581c6bf4935c94cbfab9b1ed33ef8d238ea168eb760"},
    {file = "iniconfig-2.1.0.tar.gz", hash = "sha256:3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7"},
]

[[package]]
name = "iniconfig"
version = "2.3.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.10"
groups = ["test"]
markers = "python_version >= \"3.10\""
files = [
    {file = "iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12"},
    {file = "iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730"},
]

[[package]]
name = "isort"
version = "6.1.0"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.9.0"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "isort-6.1.0-py3-none-any.whl", hash = "sha256:58d8927ecce74e5087aef019f778d4081a3b6c98f15a80ba35782ca8a2097784"},
    {file = "isort-6.1.0.tar.gz", hash = "sha256:9b8f96a14cfee0677e78e941ff62f03769a06d412aabb9e2a90487b3b7e8d481"},
]

[package.dependencies]
importlib-metadata = {version = ">=4.6.0", markers = "python_version < \"3.10\""}

[package.extras]
colors = ["colorama"]
plugins = ["setuptools"]

[[package]]
name = "isort"
version = "7.0.0"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["lint"]
markers = "python_version >= \"3.10\""
files = [
    {file = "isort-7.0.0-py3-none-any.whl", hash = "sha256:1bcabac8bc3c36c7fb7b98a76c8abb18e0f841a3ba81decac7691008592499c1"},
    {file = "isort-7.0.0.tar.gz", hash = "sha256:5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187"},
]

[package.extras]
colors = ["colorama"]
plugins = ["setuptools"]

[[package]]
name = "jinja2"
version = "3.1.6"
description = "A very fast and expressive template engine."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "jinja2-3.1.6-py3-none-any.whl", hash = "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67"},
    {file = "jinja2-3.1.6.tar.gz", hash = "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d"},
]

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "librt"
version = "0.11.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "implementation_name != \"pypy\" and platform_python_implementation != \"PyPy\""
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
name = "m2r2"
version = "0.3.4"
description = "Markdown and reStructuredText in a single file."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "m2r2-0.3.4-py3-none-any.whl", hash = "sha256:1a445514af8a229496bfb1380c52da8dd38313e48600359ee92b2c9d2e4df34a"},
    {file = "m2r2-0.3.4.tar.gz", hash = "sha256:e278f5f337e9aa7b2080fcc3e94b051bda9615b02e36c6fb3f23ff019872f043"},
]

[package.dependencies]
docutils = ">=0.19"
mistune = "0.8.4"

[[package]]
name = "markdown-it-py"
version = "3.0.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version == \"3.9\""
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
version = "4.0.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
files = [
    {file = "markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147"},
    {file = "markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3"},
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
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions", "requests"]

[[package]]
name = "markupsafe"
version = "3.0.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.9"
groups = ["docs"]
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
name = "mdurl"
version = "0.1.2"
description = "Markdown URL utilities"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8"},
    {file = "mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba"},
]

[[package]]
name = "mistune"
version = "0.8.4"
description = "The fastest markdown parser in pure Python"
optional = false
python-versions = "*"
groups = ["docs"]
files = [
    {file = "mistune-0.8.4-py2.py3-none-any.whl", hash = "sha256:88a1051873018da288eee8538d476dffe1262495144b33ecb586c4ab266bb8d4"},
    {file = "mistune-0.8.4.tar.gz", hash = "sha256:59a3429db53c50b5c6bcc8a07f8848cb00d7dc8bdb431a4ab41920d201d4756e"},
]

[[package]]
name = "mypy"
version = "1.19.1"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "python_version == \"3.9\" and implementation_name != \"pypy\""
files = [
    {file = "mypy-1.19.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:5f05aa3d375b385734388e844bc01733bd33c644ab48e9684faa54e5389775ec"},
    {file = "mypy-1.19.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:022ea7279374af1a5d78dfcab853fe6a536eebfda4b59deab53cd21f6cd9f00b"},
    {file = "mypy-1.19.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee4c11e460685c3e0c64a4c5de82ae143622410950d6be863303a1c4ba0e36d6"},
    {file = "mypy-1.19.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:de759aafbae8763283b2ee5869c7255391fbc4de3ff171f8f030b5ec48381b74"},
    {file = "mypy-1.19.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ab43590f9cd5108f41aacf9fca31841142c786827a74ab7cc8a2eacb634e09a1"},
    {file = "mypy-1.19.1-cp310-cp310-win_amd64.whl", hash = "sha256:2899753e2f61e571b3971747e302d5f420c3fd09650e1951e99f823bc3089dac"},
    {file = "mypy-1.19.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d8dfc6ab58ca7dda47d9237349157500468e404b17213d44fc1cb77bce532288"},
    {file = "mypy-1.19.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:e3f276d8493c3c97930e354b2595a44a21348b320d859fb4a2b9f66da9ed27ab"},
    {file = "mypy-1.19.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2abb24cf3f17864770d18d673c85235ba52456b36a06b6afc1e07c1fdcd3d0e6"},
    {file = "mypy-1.19.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a009ffa5a621762d0c926a078c2d639104becab69e79538a494bcccb62cc0331"},
    {file = "mypy-1.19.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f7cee03c9a2e2ee26ec07479f38ea9c884e301d42c6d43a19d20fb014e3ba925"},
    {file = "mypy-1.19.1-cp311-cp311-win_amd64.whl", hash = "sha256:4b84a7a18f41e167f7995200a1d07a4a6810e89d29859df936f1c3923d263042"},
    {file = "mypy-1.19.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:a8174a03289288c1f6c46d55cef02379b478bfbc8e358e02047487cad44c6ca1"},
    {file = "mypy-1.19.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ffcebe56eb09ff0c0885e750036a095e23793ba6c2e894e7e63f6d89ad51f22e"},
    {file = "mypy-1.19.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b64d987153888790bcdb03a6473d321820597ab8dd9243b27a92153c4fa50fd2"},
    {file = "mypy-1.19.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c35d298c2c4bba75feb2195655dfea8124d855dfd7343bf8b8c055421eaf0cf8"},
    {file = "mypy-1.19.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:34c81968774648ab5ac09c29a375fdede03ba253f8f8287847bd480782f73a6a"},
    {file = "mypy-1.19.1-cp312-cp312-win_amd64.whl", hash = "sha256:b10e7c2cd7870ba4ad9b2d8a6102eb5ffc1f16ca35e3de6bfa390c1113029d13"},
    {file = "mypy-1.19.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e3157c7594ff2ef1634ee058aafc56a82db665c9438fd41b390f3bde1ab12250"},
    {file = "mypy-1.19.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:bdb12f69bcc02700c2b47e070238f42cb87f18c0bc1fc4cdb4fb2bc5fd7a3b8b"},
    {file = "mypy-1.19.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f859fb09d9583a985be9a493d5cfc5515b56b08f7447759a0c5deaf68d80506e"},
    {file = "mypy-1.19.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c9a6538e0415310aad77cb94004ca6482330fece18036b5f360b62c45814c4ef"},
    {file = "mypy-1.19.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:da4869fc5e7f62a88f3fe0b5c919d1d9f7ea3cef92d3689de2823fd27e40aa75"},
    {file = "mypy-1.19.1-cp313-cp313-win_amd64.whl", hash = "sha256:016f2246209095e8eda7538944daa1d60e1e8134d98983b9fc1e92c1fc0cb8dd"},
    {file = "mypy-1.19.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:06e6170bd5836770e8104c8fdd58e5e725cfeb309f0a6c681a811f557e97eac1"},
    {file = "mypy-1.19.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:804bd67b8054a85447c8954215a906d6eff9cabeabe493fb6334b24f4bfff718"},
    {file = "mypy-1.19.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:21761006a7f497cb0d4de3d8ef4ca70532256688b0523eee02baf9eec895e27b"},
    {file = "mypy-1.19.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:28902ee51f12e0f19e1e16fbe2f8f06b6637f482c459dd393efddd0ec7f82045"},
    {file = "mypy-1.19.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:481daf36a4c443332e2ae9c137dfee878fcea781a2e3f895d54bd3002a900957"},
    {file = "mypy-1.19.1-cp314-cp314-win_amd64.whl", hash = "sha256:8bb5c6f6d043655e055be9b542aa5f3bdd30e4f3589163e85f93f3640060509f"},
    {file = "mypy-1.19.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:7bcfc336a03a1aaa26dfce9fff3e287a3ba99872a157561cbfcebe67c13308e3"},
    {file = "mypy-1.19.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:b7951a701c07ea584c4fe327834b92a30825514c868b1f69c30445093fdd9d5a"},
    {file = "mypy-1.19.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b13cfdd6c87fc3efb69ea4ec18ef79c74c3f98b4e5498ca9b85ab3b2c2329a67"},
    {file = "mypy-1.19.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4f28f99c824ecebcdaa2e55d82953e38ff60ee5ec938476796636b86afa3956e"},
    {file = "mypy-1.19.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:c608937067d2fc5a4dd1a5ce92fd9e1398691b8c5d012d66e1ddd430e9244376"},
    {file = "mypy-1.19.1-cp39-cp39-win_amd64.whl", hash = "sha256:409088884802d511ee52ca067707b90c883426bd95514e8cfda8281dc2effe24"},
    {file = "mypy-1.19.1-py3-none-any.whl", hash = "sha256:f1235f5ea01b7db5468d53ece6aaddf1ad0b88d9e7462b86ef96fe04995d7247"},
    {file = "mypy-1.19.1.tar.gz", hash = "sha256:19d88bb05303fe63f71dd2c6270daca27cb9401c4ca8255fe50d1d920e0eb9ba"},
]

[package.dependencies]
librt = {version = ">=0.6.2", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=0.9.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = ">=4.6.0"

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
reports = ["lxml"]

[[package]]
name = "mypy"
version = "2.1.0"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "implementation_name != \"pypy\" and python_version >= \"3.10\""
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
version = "24.13.0"
description = "unoffical Node.js package"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-macosx_13_0_arm64.whl", hash = "sha256:356654baa37bfd894e447e7e00268db403ea1d223863963459a0fbcaaa1d9d48"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-macosx_13_0_x86_64.whl", hash = "sha256:92fdef7376120e575f8b397789bafcb13bbd22a1b4d21b060d200b14910f22a5"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-manylinux_2_28_aarch64.whl", hash = "sha256:3f619ac140e039ecd25f2f71d6e83ad1414017a24608531851b7c31dc140cdfd"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-manylinux_2_28_x86_64.whl", hash = "sha256:dfb31ebc2c129538192ddb5bedd3d63d6de5d271437cd39ea26bf3fe229ba430"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:fdd720d7b378d5bb9b2710457bbc880d4c4d1270a94f13fbe257198ac707f358"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:9ad6383613f3485a75b054647a09f1cd56d12380d7459184eebcf4a5d403f35c"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-win_amd64.whl", hash = "sha256:605be4763e3ef427a3385a55da5a1bcf0a659aa2716eebbf23f332926d7e5f23"},
    {file = "nodejs_wheel_binaries-24.13.0-py2.py3-none-win_arm64.whl", hash = "sha256:2e3431d869d6b2dbeef1d469ad0090babbdcc8baaa72c01dd3cc2c6121c96af5"},
    {file = "nodejs_wheel_binaries-24.13.0.tar.gz", hash = "sha256:766aed076e900061b83d3e76ad48bfec32a035ef0d41bd09c55e832eb93ef7a4"},
]

[[package]]
name = "numpy"
version = "2.0.2"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "numpy-2.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:51129a29dbe56f9ca83438b706e2e69a39892b5eda6cedcb6b0c9fdc9b0d3ece"},
    {file = "numpy-2.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f15975dfec0cf2239224d80e32c3170b1d168335eaedee69da84fbe9f1f9cd04"},
    {file = "numpy-2.0.2-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:8c5713284ce4e282544c68d1c3b2c7161d38c256d2eefc93c1d683cf47683e66"},
    {file = "numpy-2.0.2-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:becfae3ddd30736fe1889a37f1f580e245ba79a5855bff5f2a29cb3ccc22dd7b"},
    {file = "numpy-2.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2da5960c3cf0df7eafefd806d4e612c5e19358de82cb3c343631188991566ccd"},
    {file = "numpy-2.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:496f71341824ed9f3d2fd36cf3ac57ae2e0165c143b55c3a035ee219413f3318"},
    {file = "numpy-2.0.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:a61ec659f68ae254e4d237816e33171497e978140353c0c2038d46e63282d0c8"},
    {file = "numpy-2.0.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d731a1c6116ba289c1e9ee714b08a8ff882944d4ad631fd411106a30f083c326"},
    {file = "numpy-2.0.2-cp310-cp310-win32.whl", hash = "sha256:984d96121c9f9616cd33fbd0618b7f08e0cfc9600a7ee1d6fd9b239186d19d97"},
    {file = "numpy-2.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:c7b0be4ef08607dd04da4092faee0b86607f111d5ae68036f16cc787e250a131"},
    {file = "numpy-2.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:49ca4decb342d66018b01932139c0961a8f9ddc7589611158cb3c27cbcf76448"},
    {file = "numpy-2.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:11a76c372d1d37437857280aa142086476136a8c0f373b2e648ab2c8f18fb195"},
    {file = "numpy-2.0.2-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:807ec44583fd708a21d4a11d94aedf2f4f3c3719035c76a2bbe1fe8e217bdc57"},
    {file = "numpy-2.0.2-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:8cafab480740e22f8d833acefed5cc87ce276f4ece12fdaa2e8903db2f82897a"},
    {file = "numpy-2.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a15f476a45e6e5a3a79d8a14e62161d27ad897381fecfa4a09ed5322f2085669"},
    {file = "numpy-2.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:13e689d772146140a252c3a28501da66dfecd77490b498b168b501835041f951"},
    {file = "numpy-2.0.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:9ea91dfb7c3d1c56a0e55657c0afb38cf1eeae4544c208dc465c3c9f3a7c09f9"},
    {file = "numpy-2.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c1c9307701fec8f3f7a1e6711f9089c06e6284b3afbbcd259f7791282d660a15"},
    {file = "numpy-2.0.2-cp311-cp311-win32.whl", hash = "sha256:a392a68bd329eafac5817e5aefeb39038c48b671afd242710b451e76090e81f4"},
    {file = "numpy-2.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:286cd40ce2b7d652a6f22efdfc6d1edf879440e53e76a75955bc0c826c7e64dc"},
    {file = "numpy-2.0.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:df55d490dea7934f330006d0f81e8551ba6010a5bf035a249ef61a94f21c500b"},
    {file = "numpy-2.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8df823f570d9adf0978347d1f926b2a867d5608f434a7cff7f7908c6570dcf5e"},
    {file = "numpy-2.0.2-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:9a92ae5c14811e390f3767053ff54eaee3bf84576d99a2456391401323f4ec2c"},
    {file = "numpy-2.0.2-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:a842d573724391493a97a62ebbb8e731f8a5dcc5d285dfc99141ca15a3302d0c"},
    {file = "numpy-2.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c05e238064fc0610c840d1cf6a13bf63d7e391717d247f1bf0318172e759e692"},
    {file = "numpy-2.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0123ffdaa88fa4ab64835dcbde75dcdf89c453c922f18dced6e27c90d1d0ec5a"},
    {file = "numpy-2.0.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:96a55f64139912d61de9137f11bf39a55ec8faec288c75a54f93dfd39f7eb40c"},
    {file = "numpy-2.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:ec9852fb39354b5a45a80bdab5ac02dd02b15f44b3804e9f00c556bf24b4bded"},
    {file = "numpy-2.0.2-cp312-cp312-win32.whl", hash = "sha256:671bec6496f83202ed2d3c8fdc486a8fc86942f2e69ff0e986140339a63bcbe5"},
    {file = "numpy-2.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:cfd41e13fdc257aa5778496b8caa5e856dc4896d4ccf01841daee1d96465467a"},
    {file = "numpy-2.0.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:9059e10581ce4093f735ed23f3b9d283b9d517ff46009ddd485f1747eb22653c"},
    {file = "numpy-2.0.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:423e89b23490805d2a5a96fe40ec507407b8ee786d66f7328be214f9679df6dd"},
    {file = "numpy-2.0.2-cp39-cp39-macosx_14_0_arm64.whl", hash = "sha256:2b2955fa6f11907cf7a70dab0d0755159bca87755e831e47932367fc8f2f2d0b"},
    {file = "numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl", hash = "sha256:97032a27bd9d8988b9a97a8c4d2c9f2c15a81f61e2f21404d7e8ef00cb5be729"},
    {file = "numpy-2.0.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1e795a8be3ddbac43274f18588329c72939870a16cae810c2b73461c40718ab1"},
    {file = "numpy-2.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f26b258c385842546006213344c50655ff1555a9338e2e5e02a0756dc3e803dd"},
    {file = "numpy-2.0.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:5fec9451a7789926bcf7c2b8d187292c9f93ea30284802a0ab3f5be8ab36865d"},
    {file = "numpy-2.0.2-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:9189427407d88ff25ecf8f12469d4d39d35bee1db5d39fc5c168c6f088a6956d"},
    {file = "numpy-2.0.2-cp39-cp39-win32.whl", hash = "sha256:905d16e0c60200656500c95b6b8dca5d109e23cb24abc701d41c02d74c6b3afa"},
    {file = "numpy-2.0.2-cp39-cp39-win_amd64.whl", hash = "sha256:a3f4ab0caa7f053f6797fcd4e1e25caee367db3112ef2b6ef82d749530768c73"},
    {file = "numpy-2.0.2-pp39-pypy39_pp73-macosx_10_9_x86_64.whl", hash = "sha256:7f0a0c6f12e07fa94133c8a67404322845220c06a9e80e85999afe727f7438b8"},
    {file = "numpy-2.0.2-pp39-pypy39_pp73-macosx_14_0_x86_64.whl", hash = "sha256:312950fdd060354350ed123c0e25a71327d3711584beaef30cdaa93320c392d4"},
    {file = "numpy-2.0.2-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:26df23238872200f63518dd2aa984cfca675d82469535dc7162dc2ee52d9dd5c"},
    {file = "numpy-2.0.2-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:a46288ec55ebbd58947d31d72be2c63cbf839f0a63b49cb755022310792a3385"},
    {file = "numpy-2.0.2.tar.gz", hash = "sha256:883c987dee1880e2a864ab0dc9892292582510604156762362d9326444636e78"},
]
markers = {main = "python_version == \"3.9\"", dev = "python_version == \"3.9\" and implementation_name != \"pypy\""}

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
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
version = "2.4.2"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main", "dev"]
markers = "python_version >= \"3.11\""
files = [
    {file = "numpy-2.4.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:e7e88598032542bd49af7c4747541422884219056c268823ef6e5e89851c8825"},
    {file = "numpy-2.4.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7edc794af8b36ca37ef5fcb5e0d128c7e0595c7b96a2318d1badb6fcd8ee86b1"},
    {file = "numpy-2.4.2-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:6e9f61981ace1360e42737e2bae58b27bf28a1b27e781721047d84bd754d32e7"},
    {file = "numpy-2.4.2-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:cb7bbb88aa74908950d979eeaa24dbdf1a865e3c7e45ff0121d8f70387b55f73"},
    {file = "numpy-2.4.2-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4f069069931240b3fc703f1e23df63443dbd6390614c8c44a87d96cd0ec81eb1"},
    {file = "numpy-2.4.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c02ef4401a506fb60b411467ad501e1429a3487abca4664871d9ae0b46c8ba32"},
    {file = "numpy-2.4.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:2653de5c24910e49c2b106499803124dde62a5a1fe0eedeaecf4309a5f639390"},
    {file = "numpy-2.4.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1ae241bbfc6ae276f94a170b14785e561cb5e7f626b6688cf076af4110887413"},
    {file = "numpy-2.4.2-cp311-cp311-win32.whl", hash = "sha256:df1b10187212b198dd45fa943d8985a3c8cf854aed4923796e0e019e113a1bda"},
    {file = "numpy-2.4.2-cp311-cp311-win_amd64.whl", hash = "sha256:b9c618d56a29c9cb1c4da979e9899be7578d2e0b3c24d52079c166324c9e8695"},
    {file = "numpy-2.4.2-cp311-cp311-win_arm64.whl", hash = "sha256:47c5a6ed21d9452b10227e5e8a0e1c22979811cad7dcc19d8e3e2fb8fa03f1a3"},
    {file = "numpy-2.4.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:21982668592194c609de53ba4933a7471880ccbaadcc52352694a59ecc860b3a"},
    {file = "numpy-2.4.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:40397bda92382fcec844066efb11f13e1c9a3e2a8e8f318fb72ed8b6db9f60f1"},
    {file = "numpy-2.4.2-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:b3a24467af63c67829bfaa61eecf18d5432d4f11992688537be59ecd6ad32f5e"},
    {file = "numpy-2.4.2-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:805cc8de9fd6e7a22da5aed858e0ab16be5a4db6c873dde1d7451c541553aa27"},
    {file = "numpy-2.4.2-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d82351358ffbcdcd7b686b90742a9b86632d6c1c051016484fa0b326a0a1548"},
    {file = "numpy-2.4.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9e35d3e0144137d9fdae62912e869136164534d64a169f86438bc9561b6ad49f"},
    {file = "numpy-2.4.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:adb6ed2ad29b9e15321d167d152ee909ec73395901b70936f029c3bc6d7f4460"},
    {file = "numpy-2.4.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8906e71fd8afcb76580404e2a950caef2685df3d2a57fe82a86ac8d33cc007ba"},
    {file = "numpy-2.4.2-cp312-cp312-win32.whl", hash = "sha256:ec055f6dae239a6299cace477b479cca2fc125c5675482daf1dd886933a1076f"},
    {file = "numpy-2.4.2-cp312-cp312-win_amd64.whl", hash = "sha256:209fae046e62d0ce6435fcfe3b1a10537e858249b3d9b05829e2a05218296a85"},
    {file = "numpy-2.4.2-cp312-cp312-win_arm64.whl", hash = "sha256:fbde1b0c6e81d56f5dccd95dd4a711d9b95df1ae4009a60887e56b27e8d903fa"},
    {file = "numpy-2.4.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:25f2059807faea4b077a2b6837391b5d830864b3543627f381821c646f31a63c"},
    {file = "numpy-2.4.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:bd3a7a9f5847d2fb8c2c6d1c862fa109c31a9abeca1a3c2bd5a64572955b2979"},
    {file = "numpy-2.4.2-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:8e4549f8a3c6d13d55041925e912bfd834285ef1dd64d6bc7d542583355e2e98"},
    {file = "numpy-2.4.2-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:aea4f66ff44dfddf8c2cffd66ba6538c5ec67d389285292fe428cb2c738c8aef"},
    {file = "numpy-2.4.2-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c3cd545784805de05aafe1dde61752ea49a359ccba9760c1e5d1c88a93bbf2b7"},
    {file = "numpy-2.4.2-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d0d9b7c93578baafcbc5f0b83eaf17b79d345c6f36917ba0c67f45226911d499"},
    {file = "numpy-2.4.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f74f0f7779cc7ae07d1810aab8ac6b1464c3eafb9e283a40da7309d5e6e48fbb"},
    {file = "numpy-2.4.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:c7ac672d699bf36275c035e16b65539931347d68b70667d28984c9fb34e07fa7"},
    {file = "numpy-2.4.2-cp313-cp313-win32.whl", hash = "sha256:8e9afaeb0beff068b4d9cd20d322ba0ee1cecfb0b08db145e4ab4dd44a6b5110"},
    {file = "numpy-2.4.2-cp313-cp313-win_amd64.whl", hash = "sha256:7df2de1e4fba69a51c06c28f5a3de36731eb9639feb8e1cf7e4a7b0daf4cf622"},
    {file = "numpy-2.4.2-cp313-cp313-win_arm64.whl", hash = "sha256:0fece1d1f0a89c16b03442eae5c56dc0be0c7883b5d388e0c03f53019a4bfd71"},
    {file = "numpy-2.4.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:5633c0da313330fd20c484c78cdd3f9b175b55e1a766c4a174230c6b70ad8262"},
    {file = "numpy-2.4.2-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:d9f64d786b3b1dd742c946c42d15b07497ed14af1a1f3ce840cce27daa0ce913"},
    {file = "numpy-2.4.2-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:b21041e8cb6a1eb5312dd1d2f80a94d91efffb7a06b70597d44f1bd2dfc315ab"},
    {file = "numpy-2.4.2-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:00ab83c56211a1d7c07c25e3217ea6695e50a3e2f255053686b081dc0b091a82"},
    {file = "numpy-2.4.2-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2fb882da679409066b4603579619341c6d6898fc83a8995199d5249f986e8e8f"},
    {file = "numpy-2.4.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:66cb9422236317f9d44b67b4d18f44efe6e9c7f8794ac0462978513359461554"},
    {file = "numpy-2.4.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:0f01dcf33e73d80bd8dc0f20a71303abbafa26a19e23f6b68d1aa9990af90257"},
    {file = "numpy-2.4.2-cp313-cp313t-win32.whl", hash = "sha256:52b913ec40ff7ae845687b0b34d8d93b60cb66dcee06996dd5c99f2fc9328657"},
    {file = "numpy-2.4.2-cp313-cp313t-win_amd64.whl", hash = "sha256:5eea80d908b2c1f91486eb95b3fb6fab187e569ec9752ab7d9333d2e66bf2d6b"},
    {file = "numpy-2.4.2-cp313-cp313t-win_arm64.whl", hash = "sha256:fd49860271d52127d61197bb50b64f58454e9f578cb4b2c001a6de8b1f50b0b1"},
    {file = "numpy-2.4.2-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:444be170853f1f9d528428eceb55f12918e4fda5d8805480f36a002f1415e09b"},
    {file = "numpy-2.4.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:d1240d50adff70c2a88217698ca844723068533f3f5c5fa6ee2e3220e3bdb000"},
    {file = "numpy-2.4.2-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:7cdde6de52fb6664b00b056341265441192d1291c130e99183ec0d4b110ff8b1"},
    {file = "numpy-2.4.2-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:cda077c2e5b780200b6b3e09d0b42205a3d1c68f30c6dceb90401c13bff8fe74"},
    {file = "numpy-2.4.2-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d30291931c915b2ab5717c2974bb95ee891a1cf22ebc16a8006bd59cd210d40a"},
    {file = "numpy-2.4.2-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bba37bc29d4d85761deed3954a1bc62be7cf462b9510b51d367b769a8c8df325"},
    {file = "numpy-2.4.2-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b2f0073ed0868db1dcd86e052d37279eef185b9c8db5bf61f30f46adac63c909"},
    {file = "numpy-2.4.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:7f54844851cdb630ceb623dcec4db3240d1ac13d4990532446761baede94996a"},
    {file = "numpy-2.4.2-cp314-cp314-win32.whl", hash = "sha256:12e26134a0331d8dbd9351620f037ec470b7c75929cb8a1537f6bfe411152a1a"},
    {file = "numpy-2.4.2-cp314-cp314-win_amd64.whl", hash = "sha256:068cdb2d0d644cdb45670810894f6a0600797a69c05f1ac478e8d31670b8ee75"},
    {file = "numpy-2.4.2-cp314-cp314-win_arm64.whl", hash = "sha256:6ed0be1ee58eef41231a5c943d7d1375f093142702d5723ca2eb07db9b934b05"},
    {file = "numpy-2.4.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:98f16a80e917003a12c0580f97b5f875853ebc33e2eaa4bccfc8201ac6869308"},
    {file = "numpy-2.4.2-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:20abd069b9cda45874498b245c8015b18ace6de8546bf50dfa8cea1696ed06ef"},
    {file = "numpy-2.4.2-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:e98c97502435b53741540a5717a6749ac2ada901056c7db951d33e11c885cc7d"},
    {file = "numpy-2.4.2-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:da6cad4e82cb893db4b69105c604d805e0c3ce11501a55b5e9f9083b47d2ffe8"},
    {file = "numpy-2.4.2-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9e4424677ce4b47fe73c8b5556d876571f7c6945d264201180db2dc34f676ab5"},
    {file = "numpy-2.4.2-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:2b8f157c8a6f20eb657e240f8985cc135598b2b46985c5bccbde7616dc9c6b1e"},
    {file = "numpy-2.4.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5daf6f3914a733336dab21a05cdec343144600e964d2fcdabaac0c0269874b2a"},
    {file = "numpy-2.4.2-cp314-cp314t-win32.whl", hash = "sha256:8c50dd1fc8826f5b26a5ee4d77ca55d88a895f4e4819c7ecc2a9f5905047a443"},
    {file = "numpy-2.4.2-cp314-cp314t-win_amd64.whl", hash = "sha256:fcf92bee92742edd401ba41135185866f7026c502617f422eb432cfeca4fe236"},
    {file = "numpy-2.4.2-cp314-cp314t-win_arm64.whl", hash = "sha256:1f92f53998a17265194018d1cc321b2e96e900ca52d54c7c77837b71b9465181"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:89f7268c009bc492f506abd6f5265defa7cb3f7487dc21d357c3d290add45082"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:e6dee3bb76aa4009d5a912180bf5b2de012532998d094acee25d9cb8dee3e44a"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:cd2bd2bbed13e213d6b55dc1d035a4f91748a7d3edc9480c13898b0353708920"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:cf28c0c1d4c4bf00f509fa7eb02c58d7caf221b50b467bcb0d9bbf1584d5c821"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e04ae107ac591763a47398bb45b568fc38f02dbc4aa44c063f67a131f99346cb"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:602f65afdef699cda27ec0b9224ae5dc43e328f4c24c689deaf77133dbee74d0"},
    {file = "numpy-2.4.2-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:be71bf1edb48ebbbf7f6337b5bfd2f895d1902f6335a5830b20141fc126ffba0"},
    {file = "numpy-2.4.2.tar.gz", hash = "sha256:659a6107e31a83c4e33f763942275fd278b21d095094044eb35569e86a21ddae"},
]

[[package]]
name = "packaging"
version = "26.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["docs", "lint", "test"]
files = [
    {file = "packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529"},
    {file = "packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4"},
]

[[package]]
name = "pathspec"
version = "1.0.4"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pathspec-1.0.4-py3-none-any.whl", hash = "sha256:fb6ae2fd4e7c921a165808a552060e722767cfa526f99ca5156ed2ce45a5c723"},
    {file = "pathspec-1.0.4.tar.gz", hash = "sha256:0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]
tests = ["pytest (>=9)", "typing-extensions (>=4.15)"]

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
version = "4.4.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "platformdirs-4.4.0-py3-none-any.whl", hash = "sha256:abd01743f24e5287cd7a5db3752faf1a2d65353f38ec26d98e25a6db65958c85"},
    {file = "platformdirs-4.4.0.tar.gz", hash = "sha256:ca753cf4d81dc309bc67b0ea38fd15dc97bc30ce419a7f58d13eb3bf14c4febf"},
]

[package.extras]
docs = ["furo (>=2024.8.6)", "proselint (>=0.14)", "sphinx (>=8.1.3)", "sphinx-autodoc-typehints (>=3)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.3.4)", "pytest-cov (>=6)", "pytest-mock (>=3.14)"]
type = ["mypy (>=1.14.1)"]

[[package]]
name = "platformdirs"
version = "4.5.1"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
files = [
    {file = "platformdirs-4.5.1-py3-none-any.whl", hash = "sha256:d03afa3963c806a9bed9d5125c8f4cb2fdaf74a55ab60e5d59b3fde758104d31"},
    {file = "platformdirs-4.5.1.tar.gz", hash = "sha256:61d5cdcc6065745cdd94f0f878977f8de9437be93de97c1c12f853c9c0cdcbda"},
]

[package.extras]
docs = ["furo (>=2025.9.25)", "proselint (>=0.14)", "sphinx (>=8.2.3)", "sphinx-autodoc-typehints (>=3.2)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)"]
type = ["mypy (>=1.18.2)"]

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
name = "py-cpuinfo"
version = "9.0.0"
description = "Get CPU info with pure Python"
optional = false
python-versions = "*"
groups = ["test"]
files = [
    {file = "py-cpuinfo-9.0.0.tar.gz", hash = "sha256:3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690"},
    {file = "py_cpuinfo-9.0.0-py3-none-any.whl", hash = "sha256:859625bc251f64e21f077d099d4162689c762b5d6a4c3c97553d56241c9674d5"},
]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.13\" and python_version != \"3.12\" and (python_version < \"3.12\" or implementation_name != \"pypy\")"
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
markers = "python_version < \"3.13\" and python_version != \"3.12\" and (python_version < \"3.12\" or implementation_name != \"pypy\")"
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
version = "2.19.2"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.8"
groups = ["docs", "lint", "test"]
files = [
    {file = "pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b"},
    {file = "pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887"},
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
version = "8.4.2"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.9"
groups = ["test"]
markers = "python_version == \"3.9\""
files = [
    {file = "pytest-8.4.2-py3-none-any.whl", hash = "sha256:872f880de3fc3a5bdc88a11b39c9710c3497a547cfa9320bc3c5e62fbf272e79"},
    {file = "pytest-8.4.2.tar.gz", hash = "sha256:86c0d0b93306b961d58d62a4db4879f27fe25513d4b969df351abdddb3c30e01"},
]

[package.dependencies]
colorama = {version = ">=0.4", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1", markers = "python_version < \"3.11\""}
iniconfig = ">=1"
packaging = ">=20"
pluggy = ">=1.5,<2"
pygments = ">=2.7.2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "requests", "setuptools", "xmlschema"]

[[package]]
name = "pytest"
version = "9.1.1"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.10"
groups = ["test"]
markers = "python_version >= \"3.10\""
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
name = "pytest-benchmark"
version = "5.2.3"
description = "A ``pytest`` fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer."
optional = false
python-versions = ">=3.9"
groups = ["test"]
files = [
    {file = "pytest_benchmark-5.2.3-py3-none-any.whl", hash = "sha256:bc839726ad20e99aaa0d11a127445457b4219bdb9e80a1afc4b51da7f96b0803"},
    {file = "pytest_benchmark-5.2.3.tar.gz", hash = "sha256:deb7317998a23c650fd4ff76e1230066a76cb45dcece0aca5607143c619e7779"},
]

[package.dependencies]
py-cpuinfo = "*"
pytest = ">=8.1"

[package.extras]
aspect = ["aspectlib"]
elasticsearch = ["elasticsearch"]
histogram = ["pygal", "pygaljs", "setuptools"]

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
version = "1.6.0"
description = "Pytest plugin with advanced doctest features."
optional = false
python-versions = ">=3.9"
groups = ["test"]
markers = "python_version == \"3.9\""
files = [
    {file = "pytest_doctestplus-1.6.0-py3-none-any.whl", hash = "sha256:7ea003abfd62a787fee4cae674b0efc77c2fb73518ae60da662dc3b3ec2a47ed"},
    {file = "pytest_doctestplus-1.6.0.tar.gz", hash = "sha256:f893d68370d19b418d58da0047d36a4feedac7ed28bc236858f484e994f1ac66"},
]

[package.dependencies]
packaging = ">=17.0"
pytest = ">=4.6"

[package.extras]
test = ["numpy", "pytest-remotedata (>=0.3.2)", "setuptools (>=30.3.0)", "sphinx"]

[[package]]
name = "pytest-doctestplus"
version = "1.7.1"
description = "Pytest plugin with advanced doctest features."
optional = false
python-versions = ">=3.10"
groups = ["test"]
markers = "python_version >= \"3.10\""
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
name = "pyyaml"
version = "6.0.3"
description = "YAML parser and emitter for Python"
optional = false
python-versions = ">=3.8"
groups = ["docs", "lint"]
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
name = "requests"
version = "2.32.5"
description = "Python HTTP for Humans."
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6"},
    {file = "requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf"},
]

[package.dependencies]
certifi = ">=2017.4.17"
charset_normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.21.1,<3"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use-chardet-on-py3 = ["chardet (>=3.0.2,<6)"]

[[package]]
name = "rich"
version = "14.3.2"
description = "Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal"
optional = false
python-versions = ">=3.8.0"
groups = ["lint"]
files = [
    {file = "rich-14.3.2-py3-none-any.whl", hash = "sha256:08e67c3e90884651da3239ea668222d19bea7b589149d8014a21c633420dbb69"},
    {file = "rich-14.3.2.tar.gz", hash = "sha256:e712f11c1a562a11843306f5ed999475f09ac31ffb64281f73ab29ffdda8b3b8"},
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
name = "setuptools"
version = "80.10.2"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "setuptools-80.10.2-py3-none-any.whl", hash = "sha256:95b30ddfb717250edb492926c92b5221f7ef3fbcc2b07579bcd4a27da21d0173"},
    {file = "setuptools-80.10.2.tar.gz", hash = "sha256:8b0e9d10c784bf7d262c4e5ec5d4ec94127ce206e8738f29a437945fbc219b70"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.8.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.14.*)", "pytest-mypy"]

[[package]]
name = "snowballstemmer"
version = "3.0.1"
description = "This package provides 32 stemmers for 30 languages generated from Snowball algorithms."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*"
groups = ["docs", "lint"]
files = [
    {file = "snowballstemmer-3.0.1-py3-none-any.whl", hash = "sha256:6cd7b3897da8d6c9ffb968a6781fa6532dce9c3618a4b127d920dab764a19064"},
    {file = "snowballstemmer-3.0.1.tar.gz", hash = "sha256:6d5eeeec8e9f84d4d56b847692bacf79bc2c8e90c7f80ca4444ff8b6f2e52895"},
]

[[package]]
name = "sphinx"
version = "7.4.7"
description = "Python documentation generator"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.9\""
files = [
    {file = "sphinx-7.4.7-py3-none-any.whl", hash = "sha256:c2419e2135d11f1951cd994d6eb18a1835bd8fdd8429f9ca375dc1f3281bd239"},
    {file = "sphinx-7.4.7.tar.gz", hash = "sha256:242f92a7ea7e6c5b406fdc2615413890ba9f699114a9c09192d7dfead2ee9cfe"},
]

[package.dependencies]
alabaster = ">=0.7.14,<0.8.0"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.20,<0.22"
imagesize = ">=1.3"
importlib-metadata = {version = ">=6.0", markers = "python_version < \"3.10\""}
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = "*"
sphinxcontrib-devhelp = "*"
sphinxcontrib-htmlhelp = ">=2.0.0"
sphinxcontrib-jsmath = "*"
sphinxcontrib-qthelp = "*"
sphinxcontrib-serializinghtml = ">=1.1.9"
tomli = {version = ">=2", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["sphinxcontrib-websupport"]
lint = ["flake8 (>=6.0)", "importlib-metadata (>=6.0)", "mypy (==1.10.1)", "pytest (>=6.0)", "ruff (==0.5.2)", "sphinx-lint (>=0.9)", "tomli (>=2)", "types-docutils (==0.21.0.20240711)", "types-requests (>=2.30.0)"]
test = ["cython (>=3.0)", "defusedxml (>=0.7.1)", "pytest (>=8.0)", "setuptools (>=70.0)", "typing_extensions (>=4.9)"]

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
markers = "python_version == \"3.11\" or python_version < \"3.13\" and python_version != \"3.12\" and implementation_name != \"pypy\" and python_version >= \"3.11\""
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
version = "3.6.1"
description = "Sphinx API documentation generator"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.9\""
files = [
    {file = "sphinx_autoapi-3.6.1-py3-none-any.whl", hash = "sha256:6b7af0d5650f6eac1f4b85c1eb9f9a4911160ec7138bdc4451c77a5e94d5832c"},
    {file = "sphinx_autoapi-3.6.1.tar.gz", hash = "sha256:1ff2992b7d5e39ccf92413098a376e0f91e7b4ca532c4f3e71298dbc8a4a9900"},
]

[package.dependencies]
astroid = {version = ">=3.0,<4.0", markers = "python_version < \"3.12\""}
Jinja2 = "*"
PyYAML = "*"
sphinx = ">=7.4.0"
stdlib_list = {version = "*", markers = "python_version < \"3.10\""}

[[package]]
name = "sphinx-autoapi"
version = "3.8.0"
description = "Sphinx API documentation generator"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version >= \"3.10\""
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
name = "stdlib-list"
version = "0.12.0"
description = "A list of Python Standard Libraries (2.7 through 3.14)."
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.9\""
files = [
    {file = "stdlib_list-0.12.0-py3-none-any.whl", hash = "sha256:df2d11e97f53812a1756fb5510393a11e3b389ebd9239dc831c7f349957f62f2"},
    {file = "stdlib_list-0.12.0.tar.gz", hash = "sha256:517824f27ee89e591d8ae7c1dd9ff34f672eae50ee886ea31bb8816d77535675"},
]

[package.extras]
dev = ["build", "stdlib-list[doc,lint,test]"]
doc = ["furo", "sphinx"]
lint = ["mypy", "ruff"]
support = ["sphobjinv"]
test = ["coverage[toml]", "pytest", "pytest-cov"]

[[package]]
name = "stevedore"
version = "5.5.0"
description = "Manage dynamic plugins for Python applications"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "stevedore-5.5.0-py3-none-any.whl", hash = "sha256:18363d4d268181e8e8452e71a38cd77630f345b2ef6b4a8d5614dac5ee0d18cf"},
    {file = "stevedore-5.5.0.tar.gz", hash = "sha256:d31496a4f4df9825e1a1e4f1f74d19abb0154aff311c3b376fcc89dae8fccd73"},
]

[[package]]
name = "stevedore"
version = "5.6.0"
description = "Manage dynamic plugins for Python applications"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
markers = "python_version >= \"3.10\""
files = [
    {file = "stevedore-5.6.0-py3-none-any.whl", hash = "sha256:4a36dccefd7aeea0c70135526cecb7766c4c84c473b1af68db23d541b6dc1820"},
    {file = "stevedore-5.6.0.tar.gz", hash = "sha256:f22d15c6ead40c5bbfa9ca54aa7e7b4a07d59b36ae03ed12ced1a54cf0b51945"},
]

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
version = "2.4.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["docs", "lint", "test"]
markers = "python_version < \"3.11\""
files = [
    {file = "tomli-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:b5ef256a3fd497d4973c11bf142e9ed78b150d36f5773f1ca6088c230ffc5867"},
    {file = "tomli-2.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5572e41282d5268eb09a697c89a7bee84fae66511f87533a6f88bd2f7b652da9"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:551e321c6ba03b55676970b47cb1b73f14a0a4dce6a3e1a9458fd6d921d72e95"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e3f639a7a8f10069d0e15408c0b96a2a828cfdec6fca05296ebcdcc28ca7c76"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1b168f2731796b045128c45982d3a4874057626da0e2ef1fdd722848b741361d"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:133e93646ec4300d651839d382d63edff11d8978be23da4cc106f5a18b7d0576"},
    {file = "tomli-2.4.0-cp311-cp311-win32.whl", hash = "sha256:b6c78bdf37764092d369722d9946cb65b8767bfa4110f902a1b2542d8d173c8a"},
    {file = "tomli-2.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:d3d1654e11d724760cdb37a3d7691f0be9db5fbdaef59c9f532aabf87006dbaa"},
    {file = "tomli-2.4.0-cp311-cp311-win_arm64.whl", hash = "sha256:cae9c19ed12d4e8f3ebf46d1a75090e4c0dc16271c5bce1c833ac168f08fb614"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:920b1de295e72887bafa3ad9f7a792f811847d57ea6b1215154030cf131f16b1"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7d6d9a4aee98fac3eab4952ad1d73aee87359452d1c086b5ceb43ed02ddb16b8"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36b9d05b51e65b254ea6c2585b59d2c4cb91c8a3d91d0ed0f17591a29aaea54a"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c8a885b370751837c029ef9bc014f27d80840e48bac415f3412e6593bbc18c1"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8768715ffc41f0008abe25d808c20c3d990f42b6e2e58305d5da280ae7d1fa3b"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b438885858efd5be02a9a133caf5812b8776ee0c969fea02c45e8e3f296ba51"},
    {file = "tomli-2.4.0-cp312-cp312-win32.whl", hash = "sha256:0408e3de5ec77cc7f81960c362543cbbd91ef883e3138e81b729fc3eea5b9729"},
    {file = "tomli-2.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:685306e2cc7da35be4ee914fd34ab801a6acacb061b6a7abca922aaf9ad368da"},
    {file = "tomli-2.4.0-cp312-cp312-win_arm64.whl", hash = "sha256:5aa48d7c2356055feef06a43611fc401a07337d5b006be13a30f6c58f869e3c3"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84d081fbc252d1b6a982e1870660e7330fb8f90f676f6e78b052ad4e64714bf0"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9a08144fa4cba33db5255f9b74f0b89888622109bd2776148f2597447f92a94e"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c73add4bb52a206fd0c0723432db123c0c75c280cbd67174dd9d2db228ebb1b4"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fb2945cbe303b1419e2706e711b7113da57b7db31ee378d08712d678a34e51e"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:bbb1b10aa643d973366dc2cb1ad94f99c1726a02343d43cbc011edbfac579e7c"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4cbcb367d44a1f0c2be408758b43e1ffb5308abe0ea222897d6bfc8e8281ef2f"},
    {file = "tomli-2.4.0-cp313-cp313-win32.whl", hash = "sha256:7d49c66a7d5e56ac959cb6fc583aff0651094ec071ba9ad43df785abc2320d86"},
    {file = "tomli-2.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:3cf226acb51d8f1c394c1b310e0e0e61fecdd7adcb78d01e294ac297dd2e7f87"},
    {file = "tomli-2.4.0-cp313-cp313-win_arm64.whl", hash = "sha256:d20b797a5c1ad80c516e41bc1fb0443ddb5006e9aaa7bda2d71978346aeb9132"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:26ab906a1eb794cd4e103691daa23d95c6919cc2fa9160000ac02370cc9dd3f6"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:20cedb4ee43278bc4f2fee6cb50daec836959aadaf948db5172e776dd3d993fc"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:39b0b5d1b6dd03684b3fb276407ebed7090bbec989fa55838c98560c01113b66"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a26d7ff68dfdb9f87a016ecfd1e1c2bacbe3108f4e0f8bcd2228ef9a766c787d"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:20ffd184fb1df76a66e34bd1b36b4a4641bd2b82954befa32fe8163e79f1a702"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:75c2f8bbddf170e8effc98f5e9084a8751f8174ea6ccf4fca5398436e0320bc8"},
    {file = "tomli-2.4.0-cp314-cp314-win32.whl", hash = "sha256:31d556d079d72db7c584c0627ff3a24c5d3fb4f730221d3444f3efb1b2514776"},
    {file = "tomli-2.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:43e685b9b2341681907759cf3a04e14d7104b3580f808cfde1dfdb60ada85475"},
    {file = "tomli-2.4.0-cp314-cp314-win_arm64.whl", hash = "sha256:3d895d56bd3f82ddd6faaff993c275efc2ff38e52322ea264122d72729dca2b2"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:5b5807f3999fb66776dbce568cc9a828544244a8eb84b84b9bafc080c99597b9"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c084ad935abe686bd9c898e62a02a19abfc9760b5a79bc29644463eaf2840cb0"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f2e3955efea4d1cfbcb87bc321e00dc08d2bcb737fd1d5e398af111d86db5df"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e0fe8a0b8312acf3a88077a0802565cb09ee34107813bba1c7cd591fa6cfc8d"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:413540dce94673591859c4c6f794dfeaa845e98bf35d72ed59636f869ef9f86f"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0dc56fef0e2c1c470aeac5b6ca8cc7b640bb93e92d9803ddaf9ea03e198f5b0b"},
    {file = "tomli-2.4.0-cp314-cp314t-win32.whl", hash = "sha256:d878f2a6707cc9d53a1be1414bbb419e629c3d6e67f69230217bb663e76b5087"},
    {file = "tomli-2.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:2add28aacc7425117ff6364fe9e06a183bb0251b03f986df0e78e974047571fd"},
    {file = "tomli-2.4.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2b1e3b80e1d5e52e40e9b924ec43d81570f0e7d09d11081b797bc4692765a3d4"},
    {file = "tomli-2.4.0-py3-none-any.whl", hash = "sha256:1f776e7d669ebceb01dee46484485f43a4048746235e683bcdffacdf1fb4785a"},
    {file = "tomli-2.4.0.tar.gz", hash = "sha256:aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c"},
]

[[package]]
name = "tomlkit"
version = "0.15.0"
description = "Style preserving TOML library"
optional = false
python-versions = ">=3.9"
groups = ["docs", "test"]
files = [
    {file = "tomlkit-0.15.0-py3-none-any.whl", hash = "sha256:4dbc8f0fc024412b57ced8757ac7461305126a648ff8c2c807fcb8e133a78738"},
    {file = "tomlkit-0.15.0.tar.gz", hash = "sha256:7d1a9ecba3086638211b13814ea79c90dd54dd11993564376f3aa92271f5c7a3"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "docs", "lint", "test"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]
markers = {docs = "python_version < \"3.11\"", test = "python_version < \"3.11\""}

[[package]]
name = "tzdata"
version = "2025.3"
description = "Provider of IANA time zone data"
optional = false
python-versions = ">=2"
groups = ["test"]
markers = "platform_system == \"Windows\""
files = [
    {file = "tzdata-2025.3-py2.py3-none-any.whl", hash = "sha256:06a47e5700f3081aab02b2e513160914ff0694bce9947d6b76ebd6bf57cfc5d1"},
    {file = "tzdata-2025.3.tar.gz", hash = "sha256:de39c2ca5dc7b0344f2eba86f49d614019d29f060fc4ebc8a417896a620b56a7"},
]

[[package]]
name = "tzlocal"
version = "5.3.1"
description = "tzinfo object for the local timezone"
optional = false
python-versions = ">=3.9"
groups = ["test"]
markers = "python_version == \"3.9\""
files = [
    {file = "tzlocal-5.3.1-py3-none-any.whl", hash = "sha256:eb1a66c3ef5847adf7a834f1be0800581b683b5608e74f86ecbcef8ab91bb85d"},
    {file = "tzlocal-5.3.1.tar.gz", hash = "sha256:cceffc7edecefea1f595541dbd6e990cb1ea3d19bf01b2809f362a03dd7921fd"},
]

[package.dependencies]
tzdata = {version = "*", markers = "platform_system == \"Windows\""}

[package.extras]
devenv = ["check-manifest", "pytest (>=4.3)", "pytest-cov", "pytest-mock (>=3.3)", "zest.releaser"]

[[package]]
name = "tzlocal"
version = "5.4.4"
description = "tzinfo object for the local timezone"
optional = false
python-versions = ">=3.10"
groups = ["test"]
markers = "python_version >= \"3.10\""
files = [
    {file = "tzlocal-5.4.4-py3-none-any.whl", hash = "sha256:aae09f0126a8a86fa736be266eb4a471380d26a0de3bc14844e7821fee3e2a15"},
    {file = "tzlocal-5.4.4.tar.gz", hash = "sha256:8dbb8660838688a7b6ba4fed31d18dedf842afb4d47ca050d6d891c2c15f3be4"},
]

[package.dependencies]
tzdata = {version = "*", markers = "platform_system == \"Windows\""}

[package.extras]
devenv = ["zest.releaser"]
testing = ["check_manifest", "pyroma", "pytest (>=4.3)", "pytest-cov", "pytest-mock (>=3.3)", "ruff"]

[[package]]
name = "urllib3"
version = "2.6.3"
description = "HTTP library with thread-safe connection pooling, file post, and more."
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4"},
    {file = "urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed"},
]

[package.extras]
brotli = ["brotli (>=1.2.0) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=1.2.0.0) ; platform_python_implementation != \"CPython\""]
h2 = ["h2 (>=4,<5)"]
socks = ["pysocks (>=1.5.6,!=1.5.7,<2.0)"]
zstd = ["backports-zstd (>=1.0.0) ; python_version < \"3.14\""]

[[package]]
name = "zipp"
version = "3.23.0"
description = "Backport of pathlib-compatible object wrapper for zip files"
optional = false
python-versions = ">=3.9"
groups = ["docs", "lint"]
markers = "python_version == \"3.9\""
files = [
    {file = "zipp-3.23.0-py3-none-any.whl", hash = "sha256:071652d6115ed432f5ce1d34c336c0adfd6a884660d1e9712a256d3d3bd4b14e"},
    {file = "zipp-3.23.0.tar.gz", hash = "sha256:a07157588a12518c9d4034df3fbbee09c814741a33ff63c05fa29d26a2404166"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\""]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-lint"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["big-O", "jaraco.functools", "jaraco.itertools", "jaraco.test", "more_itertools", "pytest (>=6,!=8.1.*)", "pytest-ignore-flaky"]
type = ["pytest-mypy"]

[metadata]
lock-version = "2.1"
python-versions = ">=3.9,<4.0"
content-hash = "7b70988ed8e3d51feb1518ac84c638bdcb228e9a55c020e7ccb9df7389933bd2"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=poetry.toml sha256=2ec969a99df289026424fb2d50b49e4d7d4fb1328e280f9593d29b25f56f5dd9 bytes=223 -->
## FILE: poetry.toml

- repository: `ni/nitypes-python`
- source_path: `poetry.toml`
- sha256: `2ec969a99df289026424fb2d50b49e4d7d4fb1328e280f9593d29b25f56f5dd9`
- bytes: 223

````toml
[virtualenvs]
in-project = true

[solver]
# Set min-release-age to 2 weeks, same as in https://github.com/ni/python-renovate-config
min-release-age = 14
min-release-age-exclude = ["hightime", "ni-python-styleguide"]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=pyproject.toml sha256=337d10bde177656087f9ae88ffafcec49192d7371e4291f7c0c10d8e40be1db6 bytes=4223 -->
## FILE: pyproject.toml

- repository: `ni/nitypes-python`
- source_path: `pyproject.toml`
- sha256: `337d10bde177656087f9ae88ffafcec49192d7371e4291f7c0c10d8e40be1db6`
- bytes: 4223

````toml
[project]
name = "nitypes"
description = "Data types for NI Python APIs"
license = "MIT"
keywords = ["nitypes"]
version = "1.2.0.dev0"
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Intended Audience :: Manufacturing",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Operating System :: POSIX",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: 3.14",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dynamic = ["dependencies"]
readme = "README.md"
authors = [{name = "NI", email = "opensource@ni.com"}]
maintainers = [{name = "Brad Keryan", email = "brad.keryan@ni.com"}]
requires-python = '>=3.9,<4.0'

[project.urls]
repository = "https://github.com/ni/nitypes-python"
documentation = "https://nitypes.readthedocs.io/"

[tool.poetry]
packages = [{ include = "nitypes", from = "src" }]
requires-poetry = '>=2.1,<3.0'

[tool.poetry.dependencies]
# NumPy 2.0.x is the last version that supports Python 3.9, but it crashes with Python 3.13.
numpy = [
  { version = ">=1.22", python = ">=3.9,<3.13" },
  { version = ">=2.1", python = "^3.13" }
]
hightime = { version = ">=0.2.2", allow-prereleases = true }
typing-extensions = ">=4.13.2"

[tool.poetry.group.dev.dependencies]
# Specify additional NumPy version constraints to speed up locking and test with binary wheels that support PyPy.
numpy = [
  { version = ">=1.22", python = ">=3.9,<3.12", markers = "implementation_name != 'pypy'" },
  { version = ">=1.26", python = ">=3.12,<3.13", markers = "implementation_name != 'pypy'" },
  { version = ">=2.1", python = "^3.13", markers = "implementation_name != 'pypy'" },
  { version = ">=2.1", python = ">=3.10,<3.11", markers = "implementation_name == 'pypy'" },
  { version = ">=2.3", python = "^3.11", markers = "implementation_name == 'pypy'" },
]

[tool.poetry.group.lint.dependencies]
bandit = { version = ">=1.7", extras = ["toml"] }
ni-python-styleguide = ">=0.4.1"
mypy = { version = ">=1.18.1", markers = "implementation_name != 'pypy'" }
pyright = { version = ">=1.1.400", extras = ["nodejs"] }

[tool.poetry.group.test.dependencies]
pytest = ">=7.2"
pytest-benchmark = ">=5.1"
pytest-cov = ">=4.0"
pytest-doctestplus = ">=1.4"
pytest-mock = ">=3.0"
# Uncomment to use an unreleased version of hightime for testing.
# hightime = { git = "https://github.com/ni/hightime.git" }
tomlkit = ">=0.11.0"
tzlocal = ">=5.0"

[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
# The latest Sphinx requires a recent Python version.
Sphinx = [
  { version = ">=7.4", python = ">=3.9,<3.10" },
  { version = ">=8.1", python = ">=3.10,<3.11" },
  { version = ">=8.2", python = "^3.11" },
]
sphinx-rtd-theme = ">=1.0.0"
sphinx-autoapi = ">=1.8.4"
m2r2 = ">=0.3.2"
toml = ">=0.10.2"
tomlkit = ">=0.11.0"

[tool.ni-python-styleguide]
extend_exclude = "docs"
application-import-names = "nitypes,tests"

[tool.black]
line-length = 100

[tool.pytest.ini_options]
addopts = "--doctest-modules --doctest-plus --strict-markers"
filterwarnings = [
  "error::DeprecationWarning",
  "error::PendingDeprecationWarning",
]
# Exclude tests/benchmark by default.
testpaths = ["src/nitypes", "tests/acceptance", "tests/unit"]

[build-system]
requires = ["poetry-core>=2.1.0,<3.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
files = "examples/,scripts/,src/,tests/"
namespace_packages = true
strict = true

[[tool.mypy.overrides]]
module = [
  # https://github.com/ionelmc/pytest-benchmark/issues/212 - Add type annotations
  "pytest_benchmark.*",
]
ignore_missing_imports = true

[tool.bandit]
skips = [
  "B101", # assert_used
]

[tool.pyright]
include = ["examples/", "scripts/", "src/", "tests/"]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=README.md sha256=8097221233a6454575744e0e7015507e2538a0d93f25b51c42880fe61c75ec32 bytes=6059 -->
## FILE: README.md

- repository: `ni/nitypes-python`
- source_path: `README.md`
- sha256: `8097221233a6454575744e0e7015507e2538a0d93f25b51c42880fe61c75ec32`
- bytes: 6059

````markdown
| **Info**      | Data types for NI Python APIs |
| :------------ | :-----------------------------|
| **Author**    | National Instruments          |

# Table of Contents

- [Table of Contents](#table-of-contents)
- [About](#about)
  - [Documentation](#documentation)
  - [Operating System Support](#operating-system-support)
  - [Python Version Support](#python-version-support)
- [Installation](#installation)
- [Waveforms](#waveforms)
  - [Analog Waveforms](#analog-waveforms)
  - [Complex Waveforms](#complex-waveforms)
  - [Digital Waveforms](#digital-waveforms)
  - [Frequency Spectrums](#frequency-spectrums)
- [Complex Numbers](#complex-numbers)
  - [Complex Integers](#complex-integers)
  - [Complex Number Conversion](#complex-number-conversion)
- [Time](#time)
  - [Time Conversion](#time-conversion)
  - [Binary Time](#binary-time)
- [Scalar Values](#scalar-values)
  - [Scalar](#scalar)
  - [Vector](#vector)
  - [XYData](#xydata)

# About

The `nitypes` Python package defines data types for NI Python APIs:

- Analog, complex, and digital waveforms
- Frequency spectrums
- Complex integers
- Time conversion

NI created and supports this package.

## Documentation

See the [API Reference](https://nitypes.readthedocs.io/).

## Operating System Support

`nitypes` supports Windows and Linux operating systems.

## Python Version Support

`nitypes` supports CPython 3.9+ and PyPy3.

# Installation

Installing NI driver Python APIs that support waveforms will automatically install `nitypes`.

You can also directly install the `nitypes` package using `pip` or by listing it as a dependency in
your project's `pyproject.toml` file.

# Waveforms

## Analog Waveforms

The `nitypes.waveform.AnalogWaveform` class represents a single analog signal with timing
information and extended properties (such as channel name and units). Multi-channel analog data is
represented using a collection of waveforms, such as `list[nitypes.waveform.AnalogWaveform]`. For
more details, see [Analog
Waveforms](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/waveform/index.html#analog-waveforms)
in the API Reference.

## Complex Waveforms

The `nitypes.waveform.ComplexWaveform` class represents a complex-number signal, such as I/Q data,
with timing information and extended properties (such as channel name and units). For more details,
see [Complex
Waveforms](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/waveform/index.html#complex-waveforms)
in the API Reference.

## Digital Waveforms

The `nitypes.waveform.DigitalWaveform` class represents one or more digital signals with timing
information and extended properties (such as channel name and signal names). For more details, see
[Digital
Waveforms](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/waveform/index.html#complex-waveforms)
in the API Reference.

## Frequency Spectrums

The `nitypes.waveform.Spectrum` class represents a frequency spectrum with frequency range
information and extended properties (such as channel name and units). For more details, see
[Frequency
Spectrums](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/waveform/index.html#frequency-spectrums)
in the API Reference.

# Complex Numbers

## Complex Integers

`nitypes.complex.ComplexInt32DType` is a NumPy structured data type object representing a complex
integer with 16-bit `real` and `imag` fields. This structured data type has the same memory layout
as the NIComplexI16 C struct used by NI driver APIs. For more details, see [Complex
Integers](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/complex/index.html#complex-integers)
in the API Reference.

## Complex Number Conversion

You can use the `nitypes.complex.convert_complex()` function to convert complex-number NumPy arrays
between `nitypes.complex.ComplexInt32DType` and the standard `np.complex64` and `np.complex128` data
types. For more details, see [Complex >>
Conversion](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/complex/index.html#conversion)
in the API Reference.

# Time

## Time Conversion

You can use the `nitypes.time.convert_datetime()` and `nitypes.time.convert_timedelta()` functions
to convert time values between the standard `datetime` library, the high-precision `hightime`
library, and `bintime`. For more details, see [Time >>
Conversion](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/time/index.html#conversion) in
the API Reference.

## Binary Time

The `nitypes.bintime` module implements the NI Binary Time Format (NI-BTF), a high-resolution time
format used by NI software. An NI-BTF time value is a 128-bit fixed point number consisting of a
64-bit whole seconds part and a 64-bit fractional seconds part. For more details, see [NI Binary
Time Format](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/bintime/index.html#ni-binary-time-format)
in the API Reference.

# Scalar Values

## Scalar

`nitypes.scalar.Scalar` is a data type that represents a single scalar value with units
information and extended properties. Valid types for the scalar value are `bool`, `int`, `float`,
and `str`. For more details, see
[Scalar](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/scalar/index.html#scalar) in the
API Reference.

## Vector

`nitypes.vector.Vector` is a data type that represents an array of scalar values with units
information and extended properties. Valid types for the scalar values are `bool`, `int`, `float`,
and `str`. For more details, see
[Scalar](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/vector/index.html#vector) in the
API Reference.

## XYData

`nitypes.xy_data.XYData` is a data type that represents a two axes (sequences) of numeric values
with units information. Valid types for the numeric values are `int` and `float`. For more details,
see [XYData](https://nitypes.readthedocs.io/en/latest/autoapi/nitypes/xy_data/index.html) in the
API Reference.
````

<!--NI_OSS_SOURCE repo=nitypes-python path=scripts/pin_oldest_deps.py sha256=de5b7a50b35b9b5f1f2db39d54d140b155dfceaba41378d3fe9b8b370967ed2d bytes=2028 -->
## FILE: scripts/pin_oldest_deps.py

- repository: `ni/nitypes-python`
- source_path: `scripts/pin_oldest_deps.py`
- sha256: `de5b7a50b35b9b5f1f2db39d54d140b155dfceaba41378d3fe9b8b370967ed2d`
- bytes: 2028

````python
"""Pin dependencies to the oldest compatible version for testing."""

from __future__ import annotations

import sys
from pathlib import Path

import tomlkit
from tomlkit.items import AbstractTable, Array


def main(args: list[str]) -> int | str | None:
    """Pin dependencies to the oldest compatible version for testing."""
    pyproject_path = Path(args.pop())
    if args:
        return f"Unsupported arguments: {args!r}"
    pyproject = tomlkit.loads(pyproject_path.read_text())

    poetry_deps = pyproject["tool"]["poetry"]["dependencies"]
    assert isinstance(poetry_deps, AbstractTable)
    _pin_oldest_for_deps_list(poetry_deps)

    dev_deps = pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"]
    assert isinstance(dev_deps, AbstractTable)
    _remove_duplicate_dev_deps(poetry_deps, dev_deps)

    pyproject_path.write_text(tomlkit.dumps(pyproject))
    print("Updated pyproject.toml with pinned dependencies.")
    return None


def _pin_oldest_for_deps_list(deps_list: AbstractTable) -> None:
    for dep, value in deps_list.items():
        if dep == "python":
            continue
        if isinstance(value, str) and (
            value.startswith("^") or value.startswith("~") or value.startswith(">=")
        ):
            deps_list[dep] = "==" + value.lstrip("^~>=")
        elif isinstance(value, Array):
            for constraint in value:
                if "version" in constraint and (
                    constraint["version"].startswith("^")
                    or constraint["version"].startswith("~")
                    or constraint["version"].startswith(">=")
                ):
                    constraint["version"] = "==" + constraint["version"].lstrip("^~>=")


def _remove_duplicate_dev_deps(poetry_deps: AbstractTable, dev_deps: AbstractTable) -> None:
    for dep, _ in poetry_deps.items():
        if dep in dev_deps:
            del dev_deps[dep]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
````

<!--NI_OSS_SOURCE repo=nitypes-python path=SECURITY.md sha256=902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11 bytes=1330 -->
## FILE: SECURITY.md

- repository: `ni/nitypes-python`
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

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/__init__.py sha256=f58f6dfb75d7bd60c54699af75f437216c6fe1ab07729303da8e76642ed9e64e bytes=148 -->
## FILE: src/nitypes/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/__init__.py`
- sha256: `f58f6dfb75d7bd60c54699af75f437216c6fe1ab07729303da8e76642ed9e64e`
- bytes: 148

````python
"""Data types for NI Python APIs."""

from importlib.metadata import version


__version__ = version(__name__)
"""nitypes version string."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/_arguments.py sha256=feebdba120920c4df30556126f350cb4e04319ee10f1776d8aa2780a62729f98 bytes=6712 -->
## FILE: src/nitypes/_arguments.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/_arguments.py`
- sha256: `feebdba120920c4df30556126f350cb4e04319ee10f1776d8aa2780a62729f98`
- bytes: 6712

````python
from __future__ import annotations

import operator
from typing import SupportsFloat, SupportsIndex

import numpy as np
import numpy.typing as npt

from nitypes._exceptions import (
    invalid_arg_type,
    invalid_arg_value,
    unsupported_arg,
    unsupported_dtype,
)
from nitypes._numpy import isdtype as _np_isdtype

# Some of these doctests use types introduced in NumPy 2.0 (np.long and np.ulong) or highlight
# formatting differences between NumPy 1.x and 2.x (e.g. dtype=int32, 1.23 vs. np.float64(1.23)).
__doctest_requires__ = {("arg_to_float", "is_dtype", "validate_dtype"): ["numpy>=2.0"]}


def arg_to_float(
    arg_description: str, value: SupportsFloat | None, default_value: float | None = None
) -> float:
    """Convert an argument to a float.

    >>> arg_to_float("xyz", 1.234)
    1.234
    >>> arg_to_float("xyz", 1234)
    1234.0
    >>> arg_to_float("xyz", np.float64(1.234))
    np.float64(1.234)
    >>> arg_to_float("xyz", np.float32(1.234))  # doctest: +ELLIPSIS
    1.233999...
    >>> arg_to_float("xyz", 1.234, 5.0)
    1.234
    >>> arg_to_float("xyz", None, 5.0)
    5.0
    >>> arg_to_float("xyz", None)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be a floating point number.
    <BLANKLINE>
    Provided value: None
    >>> arg_to_float("xyz", "1.234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be a floating point number.
    <BLANKLINE>
    Provided value: '1.234'
    """
    if value is None:
        if default_value is None:
            raise invalid_arg_type(arg_description, "floating point number", value)
        value = default_value

    if not isinstance(value, float):
        try:
            # Use value.__float__() because float(value) also accepts strings.
            return value.__float__()
        except Exception:
            raise invalid_arg_type(arg_description, "floating point number", value) from None

    return value


def arg_to_int(
    arg_description: str, value: SupportsIndex | None, default_value: int | None = None
) -> int:
    """Convert an argument to a signed integer.

    >>> arg_to_int("xyz", 1234)
    1234
    >>> arg_to_int("xyz", 1234, -1)
    1234
    >>> arg_to_int("xyz", None, -1)
    -1
    >>> arg_to_int("xyz", None)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: None
    >>> arg_to_int("xyz", 1.234)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: 1.234
    >>> arg_to_int("xyz", "1234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: '1234'
    """
    if value is None:
        if default_value is None:
            raise invalid_arg_type(arg_description, "integer", value)
        value = default_value

    if not isinstance(value, int):
        try:
            return operator.index(value)
        except Exception:
            raise invalid_arg_type(arg_description, "integer", value) from None

    return value


def arg_to_uint(
    arg_description: str, value: SupportsIndex | None, default_value: int | None = None
) -> int:
    """Convert an argument to an unsigned integer.

    >>> arg_to_uint("xyz", 1234)
    1234
    >>> arg_to_uint("xyz", 1234, 5000)
    1234
    >>> arg_to_uint("xyz", None, 5000)
    5000
    >>> arg_to_uint("xyz", -1234)
    Traceback (most recent call last):
    ...
    ValueError: The xyz must be a non-negative integer.
    <BLANKLINE>
    Provided value: -1234
    >>> arg_to_uint("xyz", "1234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: '1234'
    """
    value = arg_to_int(arg_description, value, default_value)
    if value < 0:
        raise invalid_arg_value(arg_description, "non-negative integer", value)
    return value


def is_dtype(dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]) -> bool:
    """Check a dtype-like object against a tuple of supported dtype-like objects.

    Unlike :any:`numpy.isdtype`, this function supports structured data types.

    >>> is_dtype(np.float64, (np.float64, np.intc, np.long,))
    True
    >>> is_dtype("float64", (np.float64, np.intc, np.long,))
    True
    >>> is_dtype(np.float64, (np.byte, np.short, np.intc, np.int_, np.long, np.longlong))
    False
    >>> a_type = np.dtype([('a', np.int32)])
    >>> b_type = np.dtype([('b', np.int32)])
    >>> is_dtype(a_type, (np.float64, np.int32, a_type,))
    True
    >>> is_dtype(b_type, (np.float64, np.int32, a_type,))
    False
    >>> is_dtype("i2, i2", (np.float64, np.int32, a_type,))
    False
    >>> is_dtype("i4", (np.float64, np.int32, a_type,))
    True
    """
    if not isinstance(dtype, (type, np.dtype)):
        dtype = np.dtype(dtype)

    if isinstance(dtype, np.dtype) and dtype.fields:
        return dtype in supported_dtypes

    return _np_isdtype(dtype, supported_dtypes)


def validate_dtype(dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]) -> None:
    """Validate a dtype-like object against a tuple of supported dtype-like objects.

    >>> validate_dtype(np.float64, (np.float64, np.intc, np.long,))
    >>> validate_dtype("float64", (np.float64, np.intc, np.long,))
    >>> validate_dtype(np.float64, (np.byte, np.short, np.intc, np.int_, np.long, np.longlong))
    Traceback (most recent call last):
    ...
    TypeError: The requested data type is not supported.
    <BLANKLINE>
    Data type: float64
    Supported data types: int8, int16, int32, int64
    >>> a_type = np.dtype([('a', np.int32)])
    >>> b_type = np.dtype([('b', np.int32)])
    >>> validate_dtype(a_type, (np.float64, np.int32, a_type,))
    >>> validate_dtype(b_type, (np.float64, np.int32, a_type,))
    Traceback (most recent call last):
    ...
    TypeError: The requested data type is not supported.
    <BLANKLINE>
    Data type: [('b', '<i4')]
    Supported data types: float64, int32, void32
    """
    if not is_dtype(dtype, supported_dtypes):
        if not isinstance(dtype, (type, np.dtype)):
            dtype = np.dtype(dtype)
        raise unsupported_dtype("requested data type", dtype, supported_dtypes)


def validate_unsupported_arg(arg_description: str, value: object) -> None:
    """Validate that an unsupported argument is None."""
    if value is not None:
        raise unsupported_arg(arg_description, value)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/_exceptions.py sha256=bce7d9f9419e3d229cde5df0c1fa7efbe608c72890bf4b26c251559a7b5202ce bytes=3569 -->
## FILE: src/nitypes/_exceptions.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/_exceptions.py`
- sha256: `bce7d9f9419e3d229cde5df0c1fa7efbe608c72890bf4b26c251559a7b5202ce`
- bytes: 3569

````python
from __future__ import annotations

import reprlib
import sys

import numpy as np
import numpy.typing as npt


def add_note(exception: Exception, note: str) -> None:
    """Add a note to an exception.

    >>> try:
    ...     raise ValueError("Oh no")
    ... except Exception as e:
    ...     add_note(e, "p.s. This is bad")
    ...     raise
    Traceback (most recent call last):
    ...
    ValueError: Oh no
    p.s. This is bad
    """
    if sys.version_info >= (3, 11):
        exception.add_note(note)
    else:
        message = exception.args[0] + "\n" + note
        exception.args = (message,) + exception.args[1:]


def invalid_arg_value(
    arg_description: str, valid_value_description: str, value: object
) -> ValueError:
    """Create a ValueError for an invalid argument value."""
    return ValueError(
        f"The {arg_description} must be {_a(valid_value_description)}.\n\n"
        f"Provided value: {reprlib.repr(value)}"
    )


def invalid_arg_type(arg_description: str, type_description: str, value: object) -> TypeError:
    """Create a TypeError for an invalid argument type."""
    return TypeError(
        f"The {arg_description} must be {_a(type_description)}.\n\n"
        f"Provided value: {reprlib.repr(value)}"
    )


def invalid_array_ndim(arg_description: str, valid_value_description: str, ndim: int) -> ValueError:
    """Create a ValueError for an array with an invalid number of dimensions."""
    return ValueError(
        f"The {arg_description} must be {_a(valid_value_description)}.\n\n"
        f"Number of dimensions: {ndim}"
    )


def invalid_requested_type(type_description: str, requested_type: type) -> TypeError:
    """Create a TypeError for an invalid requested type."""
    return TypeError(
        f"The requested type must be {_a(type_description)} type.\n\n"
        f"Requested type: {requested_type}"
    )


def unsupported_arg(arg_description: str, value: object) -> ValueError:
    """Create a ValueError for an unsupported argument."""
    return ValueError(
        f"The {arg_description} argument is not supported.\n\n"
        f"Provided value: {reprlib.repr(value)}"
    )


def unsupported_dtype(
    arg_description: str, dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]
) -> TypeError:
    """Create a TypeError for an unsupported dtype."""
    # Remove duplicate names because distinct types (e.g. int vs. long) may have the same name
    # ("int32").
    supported_dtype_names = {np.dtype(d).name: None for d in supported_dtypes}.keys()
    return TypeError(
        f"The {arg_description} is not supported.\n\n"
        f"Data type: {np.dtype(dtype)}\n"
        f"Supported data types: {', '.join(supported_dtype_names)}"
    )


def int_out_of_range(value: int, min: int, max: int) -> OverflowError:
    """Create an OverflowError when an int is out of the specified range."""
    raise OverflowError(
        "The input value is out of range.\n\n"
        f"Requested value: {value}\n"
        f"Minimum value: {min}\n",
        f"Maximum value: {max}",
    )


# English-specific hack. This is why we prefer "Key: value" for localizable errors. TODO: consider
# moving the full strings into a string table instead of building them out of English noun phrases.
def _a(noun: str) -> str:
    indefinite_article = "an" if noun[0] in "AEIOUaeiou" else "a"
    if noun.startswith("one-"):
        indefinite_article = "a"
    return f"{indefinite_article} {noun}"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/_numpy.py sha256=835ba419f0a07426fb6611b8bfb67082d5869977597c0619697e860168413535 bytes=730 -->
## FILE: src/nitypes/_numpy.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/_numpy.py`
- sha256: `835ba419f0a07426fb6611b8bfb67082d5869977597c0619697e860168413535`
- bytes: 730

````python
"""NumPy 1.x compatibility shims."""

from __future__ import annotations

import numpy as np

from nitypes._version import parse_version

numpy_version_info = parse_version(np.__version__)
"""The NumPy version as a tuple."""

if numpy_version_info >= (2, 0, 0):
    from numpy import asarray, bool, isdtype, long, ulong
else:
    # mypy warns about this when checking with --platform win32 on Linux, but not on Windows.
    from nitypes._numpy1x import (  # type: ignore[assignment,no-redef,unused-ignore]
        asarray,
        bool,
        isdtype,
        long,
        ulong,
    )


__all__ = [
    "asarray",
    "bool",
    "isdtype",
    "long",
    "numpy_version_info",
    "ulong",
]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/_numpy1x.py sha256=f146dcd8f700af0f5a8bde3037f20770ac2a14b773a6ccc5d7ce8a1faf26def3 bytes=1858 -->
## FILE: src/nitypes/_numpy1x.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/_numpy1x.py`
- sha256: `f146dcd8f700af0f5a8bde3037f20770ac2a14b773a6ccc5d7ce8a1faf26def3`
- bytes: 1858

````python
"""NumPy 1.x compatibility shim implementations."""

from __future__ import annotations

import builtins
import sys
from typing import Any

import numpy as np
import numpy.typing as npt
from numpy import bool_ as bool

# In NumPy 2.x, np.long and np.ulong are equivalent to long and unsigned long in C, following
# the platform's data model.
#
# In NumPy 1.x, np.long is an alias for int and np.ulong does not exist.
# https://numpy.org/doc/1.22/release/1.20.0-notes.html#using-the-aliases-of-builtin-types-like-np-int-is-deprecated
if sys.platform == "win32":
    # 32-bit Windows has an ILP32 data model and 64-bit Windows has an LLP64 data model, so
    # long is 32-bit.
    from numpy import (  # type: ignore[assignment,unused-ignore]
        int32 as long,
        uint32 as ulong,
    )
else:
    # Assume other 32-bit platforms have an ILP32 data model and other 64-bit platforms have an
    # LP64 data model, so long is pointer-sized.
    from numpy import intp as long, uintp as ulong


__all__ = ["asarray", "bool", "isdtype", "long", "ulong"]


def asarray(  # noqa: D103 - missing docstring in public function
    a: npt.ArrayLike, dtype: npt.DTypeLike | None = None, *, copy: builtins.bool | None = None
) -> npt.NDArray[Any]:
    b = np.asarray(a, dtype)
    made_copy = b is not a and b.base is None
    if copy is True and not made_copy:
        b = np.copy(b)
    if copy is False and made_copy:
        raise ValueError("Unable to avoid copy while creating an array as requested.")
    return b


def isdtype(  # noqa: D103 - missing docstring in public function
    dtype: type[Any] | np.dtype[Any], kind: npt.DTypeLike | tuple[npt.DTypeLike, ...]
) -> builtins.bool:
    if isinstance(kind, tuple):
        return any(dtype == k for k in kind)
    else:
        return dtype == kind
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/_version.py sha256=0d1995aeae1cde4241e1d937d660116a92edf6d9997d1db67d1f4b10fa4f9636 bytes=778 -->
## FILE: src/nitypes/_version.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/_version.py`
- sha256: `0d1995aeae1cde4241e1d937d660116a92edf6d9997d1db67d1f4b10fa4f9636`
- bytes: 778

````python
from __future__ import annotations

import re


def parse_version(version: str) -> tuple[int, int, int]:
    """Parse a version number into a major/minor/update tuple, ignoring suffixes.

    This is a minimal version parser to avoid requiring the ``packaging`` package.

    >>> parse_version("1.2.3")
    (1, 2, 3)
    >>> parse_version("123.456.789")
    (123, 456, 789)
    >>> parse_version("1.0")
    (1, 0, 0)
    >>> parse_version("1")
    (1, 0, 0)
    >>> parse_version("1.2.3-dev0")
    (1, 2, 3)
    """
    match = re.match(r"^(\d+)(?:\.(\d+)(?:\.(\d+))?)?", version)
    if match is None:
        raise ValueError(f"Invalid version number: {version}")
    return int(match.group(1)), int(match.group(2) or "0"), int(match.group(3) or "0")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/__init__.py sha256=d96c2bd6c5847c9e886bb8516bfac19d06ebca86ead23ea1385f08f681616f8b bytes=4150 -->
## FILE: src/nitypes/bintime/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/__init__.py`
- sha256: `d96c2bd6c5847c9e886bb8516bfac19d06ebca86ead23ea1385f08f681616f8b`
- bytes: 4150

````python
r"""Binary time data types for NI Python APIs.

NI Binary Time Format
=====================

This module implements the NI Binary Time Format (`NI-BTF`_), a high-resolution time format used by
NI software.

An NI-BTF time value is a 128-bit fixed point number consisting of a 64-bit whole seconds part and a
64-bit fractional seconds part. There are two types of NI-BTF time values:

* An NI-BTF absolute time represents a point in time as the number of seconds after midnight,
  January 1, 1904, UTC.
* An NI-BTF time interval represents a difference between two points in time.

NI-BTF time types are also supported in LabVIEW, LabWindows/CVI, and .NET. You can use NI-BTF time
to efficiently share high-resolution date-time information with other NI application development
environments.

.. _ni-btf: https://www.ni.com/docs/en-US/bundle/labwindows-cvi/page/cvi/libref/ni-btf.htm

NI-BTF Python Data Types
========================

* :class:`DateTime`: represents an NI-BTF absolute time as a Python object.
* :class:`DateTimeArray`: an array of :class:`DateTime` values.
* :class:`TimeDelta`: represents a NI-BTF time interval as a Python object.
* :class:`TimeDeltaArray`: an array of :class:`TimeDelta` values.

NI-BTF NumPy Structured Data Types
==================================

:any:`CVIAbsoluteTimeDType` and :any:`CVITimeIntervalDType` are NumPy structured data type objects
representing the ``CVIAbsoluteTime`` and ``CVITimeInterval`` C structs. These structured data types
can be used to efficiently represent NI-BTF time values in NumPy arrays or pass them to/from C DLLs.

.. warning::
    :any:`CVIAbsoluteTimeDType` and :any:`CVITimeIntervalDType` have the same layout and field
    names, so NumPy and type checkers such as Mypy currently treat them as the same type.

NI-BTF versus ``hightime``
==========================

NI also provides the ``hightime`` Python package, which extends the standard Python :mod:`datetime`
module to support up to yoctosecond precision.

``nitypes.bintime`` is not a replacement for ``hightime``. The two time formats have different
strengths and weaknesses.

* ``hightime`` supports local time zones and time-zone-naive times. ``bintime`` only supports UTC.
* ``hightime`` classes supports the same operations as the standard ``datetime`` classes.
  ``bintime`` classes support a subset of the standard ``datetime`` operations.
* ``hightime`` has a larger memory footprint than NI-BTF. ``hightime`` objects are separately
  allocated from the heap. ``bintime`` offers the choice of separately allocated Python objects or
  a more compact NumPy representation that can store multiple timestamps in a single block of
  memory.
* ``hightime`` requires conversion to/from NI-BTF when calling the NI driver C APIs from Python.
  ``nitypes.bintime`` includes reusable conversion routines for NI driver Python APIs to use.

NI-BTF versus :any:`numpy.datetime64`
=====================================

NumPy provides the :any:`numpy.datetime64` data type, which is even more compact than NI-BTF.
However, it has lower resolution than NI-BTF and is not interoperable with NI driver C APIs that use
NI-BTF.
"""

from __future__ import annotations

from nitypes.bintime._datetime import DateTime
from nitypes.bintime._datetime_array import DateTimeArray
from nitypes.bintime._dtypes import (
    CVIAbsoluteTimeBase,
    CVIAbsoluteTimeDType,
    CVITimeIntervalBase,
    CVITimeIntervalDType,
)
from nitypes.bintime._time_value_tuple import TimeValueTuple
from nitypes.bintime._timedelta import TimeDelta
from nitypes.bintime._timedelta_array import TimeDeltaArray

__all__ = [
    "DateTime",
    "DateTimeArray",
    "CVIAbsoluteTimeBase",
    "CVIAbsoluteTimeDType",
    "CVITimeIntervalBase",
    "CVITimeIntervalDType",
    "TimeDelta",
    "TimeDeltaArray",
    "TimeValueTuple",
]

# Hide that it was defined in a helper file
DateTime.__module__ = __name__
DateTimeArray.__module__ = __name__
TimeDelta.__module__ = __name__
TimeDeltaArray.__module__ = __name__
TimeValueTuple.__module__ = __name__
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_datetime.py sha256=52fc83f68b4233ac31e7c38415ab48f3f3140e20476866ca1820e6e40259e20c bytes=19274 -->
## FILE: src/nitypes/bintime/_datetime.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_datetime.py`
- sha256: `52fc83f68b4233ac31e7c38415ab48f3f3140e20476866ca1820e6e40259e20c`
- bytes: 19274

````python
from __future__ import annotations

import datetime as dt
from functools import singledispatchmethod
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    SupportsIndex,
    Union,
    cast,
    final,
    overload,
)

import hightime as ht
from typing_extensions import Self, TypeAlias

from nitypes._exceptions import invalid_arg_type, invalid_arg_value
from nitypes.bintime._timedelta import _OTHER_TIMEDELTA_TUPLE, _OtherTimeDelta

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.bintime import TimeDelta, TimeValueTuple
else:
    from nitypes.bintime._time_value_tuple import TimeValueTuple
    from nitypes.bintime._timedelta import TimeDelta

_DT_EPOCH_1904 = dt.datetime(1904, 1, 1, tzinfo=dt.timezone.utc)
_HT_EPOCH_1904 = ht.datetime(1904, 1, 1, tzinfo=dt.timezone.utc)

_OtherDateTime: TypeAlias = Union[dt.datetime, ht.datetime]
_OTHER_DATETIME_TUPLE = (dt.datetime, ht.datetime)


@final
class DateTime:
    """An absolute time in NI Binary Time Format (NI-BTF).

    DateTime represents time as a 128-bit fixed point number with 64-bit whole seconds and
    64-bit fractional seconds.

    .. warning::
        The fractional seconds are represented as a binary fraction, which is a sum of inverse
        powers of 2. Values that are not exactly representable as binary fractions will display
        rounding error or "bruising" similar to a floating point number.

    DateTime instances are duck typing compatible with a subset of the method and properties
    supported by :any:`datetime.datetime` and :any:`hightime.datetime`.

    This class only supports the UTC time zone and does not support timezone-naive times.

    This class does not support the ``fold`` property for disambiguating repeated times for daylight
    saving time and time zone changes.

    Constructing
    ^^^^^^^^^^^^

    As with :any:`datetime.datetime`, you can construct a :class:`DateTime` by specifying the year,
    month, day, etc.:

    >>> import datetime
    >>> DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)

    .. note::
        :class:`DateTime` only supports :any:`datetime.timezone.utc`. It does not support time-zone-naive
        objects or time zones other than UTC.

    You can also construct a :class:`DateTime` from a :any:`datetime.datetime` or
    :any:`hightime.datetime`:

    >>> DateTime(datetime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)
    >>> import hightime
    >>> DateTime(hightime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)

    You can get the current time of day by calling :any:`DateTime.now`:

    >>> DateTime.now(datetime.timezone.utc) # doctest: +ELLIPSIS
    nitypes.bintime.DateTime(...)

    Properties
    ^^^^^^^^^^

    Like other ``datetime`` objects, :class:`DateTime` has properties for the year, month, day, hour,
    minute, second, and microsecond.

    >>> import datetime
    >>> x = DateTime(datetime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    >>> (x.year, x.month, x.day)
    (2025, 5, 25)
    >>> (x.hour, x.minute, x.second, x.microsecond)
    (16, 45, 0, 0)

    Like :any:`hightime.datetime`, it also supports the femtosecond and yoctosecond properties.

    >>> (x.femtosecond, x.yoctosecond)
    (0, 0)

    Resolution
    ^^^^^^^^^^

    NI-BTF is a high-resolution time format, so it has significantly higher resolution than
    :any:`datetime.datetime`. However, :any:`hightime.datetime` has even higher resolution:

    ========================   ================================
    Class                      Smallest Time Increment
    ========================   ================================
    :any:`datetime.datetime`   1 microsecond (1e-6 sec)
    :class:`DateTime`            54210 yoctoseconds (5.4e-20 sec)
    :any:`hightime.datetime`   1 yoctosecond (1e-24 sec)
    ========================   ================================

    As a result, :any:`hightime.datetime` can represent the time down to the exact yoctosecond, but
    :class:`DateTime` rounds the yoctosecond field.

    >>> import hightime
    >>> x = hightime.datetime(2025, 1, 1, yoctosecond=123456789, tzinfo=datetime.timezone.utc)
    >>> x
    hightime.datetime(2025, 1, 1, 0, 0, 0, 0, 0, 123456789, tzinfo=datetime.timezone.utc)
    >>> DateTime(x) # doctest: +NORMALIZE_WHITESPACE
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 0, 0, 123436417, tzinfo=datetime.timezone.utc)

    Rounding
    ^^^^^^^^

    NI-BTF represents fractional seconds as a binary fraction, which is a sum of inverse
    powers of 2. Values that are not exactly representable as binary fractions will display
    rounding error or "bruising" similar to a floating point number.

    For example, it may round 100 microseconds down to 99.9999... microseconds.

    >>> x = hightime.datetime(2025, 1, 1, microsecond=100, tzinfo=datetime.timezone.utc)
    >>> x
    hightime.datetime(2025, 1, 1, 0, 0, 0, 100, tzinfo=datetime.timezone.utc)
    >>> DateTime(x) # doctest: +NORMALIZE_WHITESPACE
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 99, 999999999, 999991239,
        tzinfo=datetime.timezone.utc)

    Class members
    ^^^^^^^^^^^^^
    """  # noqa: W505 - doc line too long

    min: ClassVar[DateTime]
    """The earliest supported :class:`DateTime` object, midnight on Jan 1, 0001, UTC."""

    max: ClassVar[DateTime]
    """The latest supported :class:`DateTime` object, before midnight on Dec 31, 9999, UTC."""

    __slots__ = ["_offset", "_hightime_cache"]

    _offset: TimeDelta
    _hightime_cache: ht.datetime | None

    @overload
    def __init__(self) -> None: ...  # noqa: D107 - missing docstring in __init__

    @overload
    def __init__(  # noqa: D107 - missing docstring in __init__
        self, value: _OtherDateTime, /
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - missing docstring in __init__
        self,
        year: SupportsIndex,
        month: SupportsIndex,
        day: SupportsIndex,
        hour: SupportsIndex = ...,
        minute: SupportsIndex = ...,
        second: SupportsIndex = ...,
        microsecond: SupportsIndex = ...,
        femtosecond: SupportsIndex = ...,
        yoctosecond: SupportsIndex = ...,
        tzinfo: dt.tzinfo | None = None,
    ) -> None: ...

    def __init__(
        self,
        year: SupportsIndex | _OtherDateTime | None = None,
        month: SupportsIndex | None = None,
        day: SupportsIndex | None = None,
        hour: SupportsIndex = 0,
        minute: SupportsIndex = 0,
        second: SupportsIndex = 0,
        microsecond: SupportsIndex = 0,
        femtosecond: SupportsIndex = 0,
        yoctosecond: SupportsIndex = 0,
        tzinfo: dt.tzinfo | None = None,
    ) -> None:
        """Initialize a DateTime."""
        if isinstance(year, SupportsIndex):
            self._offset = self.__class__._to_offset(
                ht.datetime(
                    year,
                    cast(SupportsIndex, month),
                    cast(SupportsIndex, day),
                    hour,
                    minute,
                    second,
                    microsecond,
                    femtosecond,
                    yoctosecond,
                    tzinfo,
                )
            )
        else:
            self._offset = self.__class__._to_offset(year)

        # Do not cache the passed-in ht.datetime because that would hide the rounding error
        # caused by using a binary fraction.
        self._hightime_cache = None

    @singledispatchmethod
    @classmethod
    def _to_offset(cls, value: object) -> TimeDelta:
        raise invalid_arg_type("value", "datetime", value)

    # Python 3.9: pass the type to register() in order to work around
    # https://github.com/python/cpython/issues/86153 - singledispatchmethod raises an error when
    # relying on a forward declaration
    @_to_offset.register(ht.datetime)
    @classmethod
    def _(cls, value: ht.datetime) -> TimeDelta:
        if value.tzinfo != dt.timezone.utc:
            raise ValueError("The tzinfo must be datetime.timezone.utc.")
        return TimeDelta(value - _HT_EPOCH_1904)

    @_to_offset.register(dt.datetime)
    @classmethod
    def _(cls, value: dt.datetime) -> TimeDelta:
        if value.tzinfo != dt.timezone.utc:
            raise ValueError("The tzinfo must be datetime.timezone.utc.")
        return TimeDelta(value - _DT_EPOCH_1904)

    @_to_offset.register(type(None))
    @classmethod
    def _(cls, value: None) -> TimeDelta:
        return TimeDelta()

    @classmethod
    def from_ticks(cls, ticks: SupportsIndex) -> Self:
        """Create an DateTime from a 128-bit fixed point number expressed as an integer."""
        self = cls.__new__(cls)
        self._offset = TimeDelta.from_ticks(ticks)
        self._hightime_cache = None
        return self

    @classmethod
    def from_tuple(cls, value: TimeValueTuple) -> Self:
        """Create a DateTime from whole and fractional seconds as 64-bit ints."""
        self = cls.__new__(cls)
        self._offset = TimeDelta.from_tuple(value)
        self._hightime_cache = None
        return self

    @classmethod
    def from_offset(cls, offset: TimeDelta) -> Self:
        """Create an DateTime from a TimeValue offset from the epoch, Jan 1, 1904."""
        self = cls.__new__(cls)
        self._offset = offset
        self._hightime_cache = None
        return self

    def _to_datetime_datetime(self) -> dt.datetime:
        """Return self as a :any:`datetime.datetime`."""
        return _DT_EPOCH_1904 + self._offset._to_datetime_timedelta()

    def _to_hightime_datetime(self) -> ht.datetime:
        """Return self as a :any:`hightime.datetime`."""
        if self._hightime_cache is None:
            self._hightime_cache = _HT_EPOCH_1904 + self._offset._to_hightime_timedelta()
        return self._hightime_cache

    # Calculating the year/month/day requires knowledge of leap years, days per month, etc., so
    # defer to hightime.datetime.
    @property
    def year(self) -> int:
        """The year."""
        return self._to_hightime_datetime().year

    @property
    def month(self) -> int:
        """The month, between 1 and 12 inclusive."""
        return self._to_hightime_datetime().month

    @property
    def day(self) -> int:
        """The day of the month, between 1 and 31 inclusive."""
        return self._to_hightime_datetime().day

    # The hour/minute/second properties currently assume that tzinfo.utcoffset() == 0, which is
    # true because this class only supports UTC.
    @property
    def hour(self) -> int:
        """The hour, between 0 and 23 inclusive."""
        return self._offset.seconds // 3600

    @property
    def minute(self) -> int:
        """The minute, between 0 and 59 inclusive."""
        return (self._offset.seconds // 60) % 60

    @property
    def second(self) -> int:
        """The second, between 0 and 59 inclusive."""
        return self._offset.seconds % 60

    @property
    def microsecond(self) -> int:
        """The microsecond, between 0 and 999_999 inclusive."""
        return self._offset.microseconds

    @property
    def femtosecond(self) -> int:
        """The femtosecond, between 0 and 999_999_999 inclusive."""
        return self._offset.femtoseconds

    @property
    def yoctosecond(self) -> int:
        """The yoctosecond, between 0 and 999_999_999 inclusive.

        .. warning::
            Because this class uses a 64-bit binary fraction, the smallest time increment it can
            represent is ``1.0 / (1 << 64)`` seconds, which is about 54210 yoctoseconds.
        """
        return self._offset.yoctoseconds

    @property
    def ticks(self) -> int:
        """The number of ticks since the epoch, Jan 1, 1904."""
        return self._offset.ticks

    @property
    def tzinfo(self) -> dt.tzinfo | None:
        """The time zone."""
        return dt.timezone.utc

    def to_tuple(self) -> TimeValueTuple:
        """Convert to the number of whole and fractional seconds since the epoch, Jan 1, 1904."""
        return self._offset.to_tuple()

    @classmethod
    def now(cls, tz: dt.tzinfo | None = None) -> Self:
        """Return the current absolute time."""
        if tz != dt.timezone.utc:
            raise invalid_arg_value("tz", "datetime.timezone.utc", tz)
        return cls(ht.datetime.now(tz))

    def __add__(self, value: TimeDelta | _OtherTimeDelta, /) -> DateTime:
        """Return self+value."""
        if isinstance(value, TimeDelta):
            return self.__class__.from_offset(self._offset + value)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self + TimeDelta(value)
        else:
            return NotImplemented

    __radd__ = __add__

    @overload
    def __sub__(  # noqa: D105 - missing docstring for magic method
        self, value: DateTime | _OtherDateTime, /
    ) -> TimeDelta: ...
    @overload
    def __sub__(  # noqa: D105 - missing docstring for magic method
        self, value: TimeDelta | _OtherTimeDelta, /
    ) -> DateTime: ...

    def __sub__(
        self, value: DateTime | _OtherDateTime | TimeDelta | _OtherTimeDelta, /
    ) -> TimeDelta | DateTime:
        """Return self-value."""
        if isinstance(value, DateTime):
            return self._offset - value._offset
        elif isinstance(value, _OTHER_DATETIME_TUPLE):
            return self - self.__class__(value)
        elif isinstance(value, TimeDelta):
            return self.__class__.from_offset(self._offset - value)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self - TimeDelta(value)
        else:
            return NotImplemented

    @overload
    def __rsub__(  # noqa: D105 - missing docstring for magic method
        self, value: DateTime | _OtherDateTime, /
    ) -> TimeDelta: ...
    @overload
    def __rsub__(  # noqa: D105 - missing docstring for magic method
        self, value: TimeDelta | _OtherTimeDelta, /
    ) -> DateTime: ...

    def __rsub__(
        self, value: DateTime | _OtherDateTime | TimeDelta | _OtherTimeDelta, /
    ) -> TimeDelta | DateTime:
        """Return value-self."""
        if isinstance(value, DateTime):
            return value._offset - self._offset
        elif isinstance(value, _OTHER_DATETIME_TUPLE):
            return self.__class__(value) - self
        elif isinstance(value, TimeDelta):
            return self.__class__.from_offset(value - self._offset)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return TimeDelta(value) - self
        else:
            return NotImplemented

    # In comparison operators, always promote to the more precise data type (dt -> bt, bt -> ht).
    def __lt__(self, value: DateTime | _OtherDateTime, /) -> bool:
        """Return self<value."""
        if isinstance(value, self.__class__):
            return self._offset < value._offset
        elif isinstance(value, ht.datetime):
            return self._to_hightime_datetime() < value
        elif isinstance(value, dt.datetime):
            return self < self.__class__(value)
        else:
            return NotImplemented

    def __le__(self, value: DateTime | _OtherDateTime, /) -> bool:
        """Return self<=value."""
        if isinstance(value, self.__class__):
            return self._offset <= value._offset
        elif isinstance(value, ht.datetime):
            return self._to_hightime_datetime() <= value
        elif isinstance(value, dt.datetime):
            return self <= self.__class__(value)
        else:
            return NotImplemented

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if isinstance(value, self.__class__):
            return self._offset == value._offset
        elif isinstance(value, ht.datetime):
            return self._to_hightime_datetime() == value
        elif isinstance(value, dt.datetime):
            return self == self.__class__(value)
        else:
            return NotImplemented

    def __gt__(self, value: DateTime | _OtherDateTime, /) -> bool:
        """Return self<value."""
        if isinstance(value, self.__class__):
            return self._offset > value._offset
        elif isinstance(value, ht.datetime):
            return self._to_hightime_datetime() > value
        elif isinstance(value, dt.datetime):
            return self > self.__class__(value)
        else:
            return NotImplemented

    def __ge__(self, value: DateTime | _OtherDateTime, /) -> bool:
        """Return self>=value."""
        if isinstance(value, self.__class__):
            return self._offset >= value._offset
        elif isinstance(value, ht.datetime):
            return self._to_hightime_datetime() >= value
        elif isinstance(value, dt.datetime):
            return self >= self.__class__(value)
        else:
            return NotImplemented

    def __hash__(self) -> int:
        """Return hash(self)."""
        return hash(self._offset)

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        return (self.__class__.from_ticks, (self._offset._ticks,))

    def __str__(self) -> str:
        """Return repr(self)."""
        return str(self._to_hightime_datetime())

    def __repr__(self) -> str:
        """Return repr(self)."""
        args: list[int | str] = [self.year, self.month, self.day, self.hour, self.minute]
        # Only display sub-minute fields if they aren't 0.
        if self.yoctosecond:
            args.extend([self.second, self.microsecond, self.femtosecond, self.yoctosecond])
        elif self.femtosecond:
            args.extend([self.second, self.microsecond, self.femtosecond])
        elif self.microsecond:
            args.extend([self.second, self.microsecond])
        elif self.second:
            args.append(self.second)
        args.append("tzinfo=datetime.timezone.utc")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(map(str, args))})"


# These have to be within dt.datetime.max/min or else delegating to dt.datetime or ht.datetime for
# year/month/day, str(), repr(), etc. will fail. Use ticks to specify the maximum fractional second
# without rounding up to MAXYEAR+1.
DateTime.max = DateTime(
    dt.MAXYEAR,
    12,
    31,
    23,
    59,
    59,
    tzinfo=dt.timezone.utc,
) + TimeDelta.from_ticks(0xFFFF_FFFF_FFFF_FFFF)
DateTime.min = DateTime(dt.MINYEAR, 1, 1, tzinfo=dt.timezone.utc)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_datetime_array.py sha256=93d0fcde0b3d10411c04e42989de21a68446a2cc66efb51fa78da18c0324b314 bytes=7767 -->
## FILE: src/nitypes/bintime/_datetime_array.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_datetime_array.py`
- sha256: `93d0fcde0b3d10411c04e42989de21a68446a2cc66efb51fa78da18c0324b314`
- bytes: 7767

````python
from __future__ import annotations

from collections.abc import Iterable, MutableSequence
from typing import (
    TYPE_CHECKING,
    Any,
    final,
    overload,
)

import numpy as np
import numpy.typing as npt

from nitypes._exceptions import invalid_arg_value, invalid_arg_type

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.bintime import CVIAbsoluteTimeDType, DateTime, TimeValueTuple
else:
    from nitypes.bintime._dtypes import CVIAbsoluteTimeDType
    from nitypes.bintime._datetime import DateTime
    from nitypes.bintime._time_value_tuple import TimeValueTuple


@final
class DateTimeArray(MutableSequence[DateTime]):
    """A mutable array of :class:`DateTime` values in NI Binary Time Format (NI-BTF).

    Raises:
        TypeError: If any item in value is not a DateTime instance.
    """

    __slots__ = ["_array"]

    _array: npt.NDArray[np.void]

    def __init__(
        self,
        value: Iterable[DateTime] | None = None,
    ) -> None:
        """Initialize a new DateTimeArray."""
        value = [] if value is None else list(value)
        if not all(isinstance(item, DateTime) for item in value):
            raise invalid_arg_type("value", "iterable of DateTime", value)
        self._array = np.fromiter(
            (entry.to_tuple().to_cvi() for entry in value),
            dtype=CVIAbsoluteTimeDType,
            count=len(value),
        )

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int
    ) -> DateTime: ...

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> DateTimeArray: ...

    def __getitem__(self, index: int | slice) -> DateTime | DateTimeArray:
        """Return self[index].

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        """
        if isinstance(index, int):
            entry = self._array[index].item()
            as_tuple = TimeValueTuple.from_cvi(*entry)
            return DateTime.from_tuple(as_tuple)
        elif isinstance(index, slice):
            sliced_entries = self._array[index]
            new_array = DateTimeArray()
            new_array._array = sliced_entries
            return new_array
        else:
            raise invalid_arg_type("index", "int or slice", index)

    def __len__(self) -> int:
        """Return len(self)."""
        return len(self._array)

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int, value: DateTime
    ) -> None: ...

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice, value: Iterable[DateTime]
    ) -> None: ...

    def __setitem__(self, index: int | slice, value: DateTime | Iterable[DateTime]) -> None:
        """Set a new value for DateTime at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type, or slice value is not iterable.
            ValueError: If slice assignment length doesn't match the selected range.
            IndexError: If index is out of range.
        """
        if isinstance(index, int):
            if not isinstance(value, DateTime):
                raise invalid_arg_type("value", "DateTime", value)
            self._array[index] = value.to_tuple().to_cvi()
        elif isinstance(index, slice):
            if not isinstance(value, Iterable):
                raise invalid_arg_type("value", "iterable of DateTime", value)
            values = list(value)
            if not all(isinstance(item, DateTime) for item in values):
                raise invalid_arg_type("value", "iterable of DateTime", value)

            start, stop, step = index.indices(len(self))
            selected_count = len(range(start, stop, step))
            new_entry_count = len(values)
            if step > 1 and new_entry_count != selected_count:
                raise invalid_arg_value(
                    "value", "iterable with the same length as the slice", value
                )

            if new_entry_count < selected_count:
                # Shrink
                replaced = slice(start, start + new_entry_count)
                removed = slice(start + new_entry_count, stop)
                self._array[replaced] = [item.to_tuple().to_cvi() for item in values]
                del self[removed]
            elif new_entry_count > selected_count:
                # Grow
                replaced = slice(start, stop)
                self._array[replaced] = [
                    item.to_tuple().to_cvi() for item in values[:selected_count]
                ]
                self._array = np.insert(
                    self._array,
                    stop,
                    [item.to_tuple().to_cvi() for item in values[selected_count:]],
                )
            else:
                # Replace, accounting for strides
                self._array[index] = [item.to_tuple().to_cvi() for item in values]
        else:
            raise invalid_arg_type("index", "int or slice", index)

    @overload
    def __delitem__(self, index: int) -> None: ...  # noqa: D105 - missing docstring in magic method

    @overload
    def __delitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> None: ...

    def __delitem__(self, index: int | slice) -> None:
        """Delete the value at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        """
        if isinstance(index, (int, slice)):
            self._array = np.delete(self._array, index)
        else:
            raise invalid_arg_type("index", "int or slice", index)

    def insert(self, index: int, value: DateTime) -> None:
        """Insert the DateTime value before the specified index.

        Raises:
            TypeError: If index is not int or value is not DateTime.
        """
        if not isinstance(index, int):
            raise invalid_arg_type("index", "int", index)
        if not isinstance(value, DateTime):
            raise invalid_arg_type("value", "DateTime", value)
        lower = -len(self._array)
        upper = len(self._array)
        index = min(max(index, lower), upper)
        as_cvi = value.to_tuple().to_cvi()
        self._array = np.insert(self._array, index, as_cvi)

    def extend(self, values: Iterable[DateTime]) -> None:
        """Extend the array by appending the elements from values."""
        if values is None:
            raise invalid_arg_type("values", "iterable of DateTime", values)
        new_array = DateTimeArray(values)
        self._array = np.append(self._array, new_array._array)

    def __eq__(self, other: object) -> bool:
        """Return self == other."""
        if not isinstance(other, DateTimeArray):
            return NotImplemented
        return np.array_equal(self._array, other._array)

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        return (self.__class__, (list(iter(self)),))

    def __repr__(self) -> str:
        """Return repr(self)."""
        ctor_args = list(iter(self))
        return f"{self.__class__.__module__}.{self.__class__.__name__}({ctor_args})"

    def __str__(self) -> str:
        """Return str(self)."""
        values = list(iter(self))
        return f"[{'; '.join(str(v) for v in values)}]"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_dtypes.py sha256=0f5b200e4663fc63236f0d03c6835e749da1048376fddc0c02deb78c4aa82c3a bytes=717 -->
## FILE: src/nitypes/bintime/_dtypes.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_dtypes.py`
- sha256: `0f5b200e4663fc63236f0d03c6835e749da1048376fddc0c02deb78c4aa82c3a`
- bytes: 717

````python
from __future__ import annotations

import numpy as np
from typing_extensions import TypeAlias

CVIAbsoluteTimeBase: TypeAlias = np.void
"""Type alias for the base type of :any:`CVIAbsoluteTimeDType`, which is :any:`numpy.void`."""

CVIAbsoluteTimeDType = np.dtype((CVIAbsoluteTimeBase, [("lsb", np.uint64), ("msb", np.int64)]))
"""NumPy structured data type for a ``CVIAbsoluteTime`` C struct."""

CVITimeIntervalBase: TypeAlias = np.void
"""Type alias for the base type of :any:`CVITimeIntervalDType`, which is :any:`numpy.void`."""

CVITimeIntervalDType = np.dtype((CVITimeIntervalBase, [("lsb", np.uint64), ("msb", np.int64)]))
"""NumPy structured data type for a ``CVITimeInterval`` C struct."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_time_value_tuple.py sha256=beca077ece7d723072965220828b3ee2a1d15d987d09116df69acdfd301a1bb4 bytes=854 -->
## FILE: src/nitypes/bintime/_time_value_tuple.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_time_value_tuple.py`
- sha256: `beca077ece7d723072965220828b3ee2a1d15d987d09116df69acdfd301a1bb4`
- bytes: 854

````python
from __future__ import annotations

from typing import NamedTuple


class TimeValueTuple(NamedTuple):
    """A named tuple containing the whole seconds and fractional seconds parts of a time value."""

    whole_seconds: int
    """The whole seconds portion of a binary time value. This should be an int64."""

    fractional_seconds: int
    """The fractional seconds portion of a binary time value. This should be a uint64."""

    @staticmethod
    def from_cvi(lsb: int, msb: int) -> TimeValueTuple:
        """Create a :class:`TimeValueTuple` from a ``CVIAbsoluteTime`` representation."""
        return TimeValueTuple(whole_seconds=msb, fractional_seconds=lsb)

    def to_cvi(self) -> tuple[int, int]:
        """Return a representation as ``CVIAbsoluteTime``."""
        return (self.fractional_seconds, self.whole_seconds)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_timedelta.py sha256=f8127fe64f84d8414014800ba0825057f1e086787a072265b99e2aff93b3c5aa bytes=22982 -->
## FILE: src/nitypes/bintime/_timedelta.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_timedelta.py`
- sha256: `f8127fe64f84d8414014800ba0825057f1e086787a072265b99e2aff93b3c5aa`
- bytes: 22982

````python
from __future__ import annotations

import datetime as dt
import decimal
import math
import operator
from decimal import Decimal
from functools import singledispatchmethod
from typing import TYPE_CHECKING, Any, ClassVar, SupportsIndex, Union, final, overload

import hightime as ht
from typing_extensions import Self, TypeAlias

from nitypes._arguments import arg_to_int
from nitypes._exceptions import int_out_of_range, invalid_arg_type

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.bintime import TimeValueTuple
else:
    from nitypes.bintime._time_value_tuple import TimeValueTuple


_INT64_MAX = (1 << 63) - 1
_INT64_MIN = -(1 << 63)
_UINT64_MAX = (1 << 64) - 1
_UINT64_MIN = 0
_INT128_MAX = (1 << 127) - 1
_INT128_MIN = -(1 << 127)

_BITS_PER_SECOND = 64
_TICKS_PER_SECOND = 1 << _BITS_PER_SECOND
_FRACTIONAL_SECONDS_MASK = _TICKS_PER_SECOND - 1

_SECONDS_PER_DAY = 86400

_MICROSECONDS_PER_SECOND = 10**6
_FEMTOSECONDS_PER_SECOND = 10**15
_YOCTOSECONDS_PER_SECOND = 10**24

_FEMTOSECONDS_PER_MICROSECOND = _FEMTOSECONDS_PER_SECOND // _MICROSECONDS_PER_SECOND
_YOCTOSECONDS_PER_FEMTOSECOND = _YOCTOSECONDS_PER_SECOND // _FEMTOSECONDS_PER_SECOND

_DECIMAL_DIGITS = 64
_REPR_TICKS = False


_OtherTimeDelta: TypeAlias = Union[dt.timedelta, ht.timedelta]
_OTHER_TIMEDELTA_TUPLE = (dt.timedelta, ht.timedelta)

_OtherDateTime: TypeAlias = Union[dt.datetime, ht.datetime]


@final
class TimeDelta:
    """A duration, represented in NI Binary Time Format (NI-BTF).

    TimeDelta represents time as a 128-bit fixed point number with 64-bit whole seconds and 64-bit
    fractional seconds.

    .. warning::
        The fractional seconds are represented as a binary fraction, which is a sum of inverse
        powers of 2. Values that are not exactly representable as binary fractions will display
        rounding error or "bruising" similar to a floating point number.

    TimeDelta instances are duck typing compatible with :any:`datetime.timedelta` and
    :any:`hightime.timedelta`.

    Constructing
    ^^^^^^^^^^^^

    You can construct a :class:`TimeDelta` from a number of seconds, expressed as an :any:`int`,
    :any:`float`, or :any:`decimal.Decimal`.

    >>> TimeDelta(100)
    nitypes.bintime.TimeDelta(Decimal('100'))
    >>> TimeDelta(100.125)
    nitypes.bintime.TimeDelta(Decimal('100.125'))
    >>> from decimal import Decimal
    >>> TimeDelta(Decimal("100.125"))
    nitypes.bintime.TimeDelta(Decimal('100.125'))

    :class:`TimeDelta` has the same resolution and rounding behavior as :class:`DateTime`.

    >>> TimeDelta(Decimal("100.01234567890123456789"))
    nitypes.bintime.TimeDelta(Decimal('100.012345678901234567889'))

    Unlike other ``timedelta`` objects, you cannot construct a :class:`TimeDelta` from separate weeks,
    days, hours, etc. If you want to do that, construct a :any:`datetime.timedelta` or
    :any:`hightime.timedelta` and then use it to construct a :class:`TimeDelta`.

    >>> import datetime, hightime
    >>> TimeDelta(datetime.timedelta(days=1, microseconds=1))
    nitypes.bintime.TimeDelta(Decimal('86400.0000010000000000000'))
    >>> TimeDelta(hightime.timedelta(days=1, femtoseconds=1))
    nitypes.bintime.TimeDelta(Decimal('86400.0000000000000010000'))

    Math Operations
    ^^^^^^^^^^^^^^^

    :class:`DateTime` and :class:`TimeDelta` support the same math operations as :any:`datetime.datetime`
    and :any:`datetime.timedelta`.

    For example, you can add or subtract :class:`TimeDelta` objects together:

    >>> TimeDelta(100.5) + TimeDelta(0.5)
    nitypes.bintime.TimeDelta(Decimal('101'))
    >>> TimeDelta(100.5) - TimeDelta(0.5)
    nitypes.bintime.TimeDelta(Decimal('100'))

    Or add/subtract a :class:`DateTime` with a :class:`TimeDelta`, :any:`datetime.timedelta`, or
    :any:`hightime.timedelta`:

    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + TimeDelta(86400)
    nitypes.bintime.DateTime(2025, 1, 2, 0, 0, tzinfo=datetime.timezone.utc)
    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + datetime.timedelta(days=1)
    nitypes.bintime.DateTime(2025, 1, 2, 0, 0, tzinfo=datetime.timezone.utc)
    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + hightime.timedelta(femtoseconds=1)
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 0, 1, 13873, tzinfo=datetime.timezone.utc)

    Class members
    ^^^^^^^^^^^^^
    """  # noqa: W505 - doc line too long

    min: ClassVar[TimeDelta]
    """The most negative :class:`TimeDelta` object, approximately -292 million years."""

    max: ClassVar[TimeDelta]
    """The most positive :class:`TimeDelta` object, approximately 292 million years."""

    __slots__ = ["_ticks"]

    _ticks: int

    @overload
    def __init__(self) -> None: ...  # noqa: D107 - missing docstring in __init__

    @overload
    def __init__(  # noqa: D107 - missing docstring in __init__
        self, value: _OtherTimeDelta, /
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - missing docstring in __init__
        self, seconds: SupportsIndex | Decimal | float
    ) -> None: ...

    def __init__(
        self,
        seconds: SupportsIndex | Decimal | float | _OtherTimeDelta | None = None,
    ) -> None:
        """Initialize a TimeDelta."""
        ticks = self.__class__._to_ticks(seconds)
        if not (_INT128_MIN <= ticks <= _INT128_MAX):
            raise OverflowError(
                "The seconds value is out of range.\n\n"
                f"Requested value: {seconds}\n"
                f"Minimum value: {self.__class__.min.precision_total_seconds()}\n"
                f"Maximum value: {self.__class__.max.precision_total_seconds()}"
            )
        self._ticks = ticks

    @singledispatchmethod
    @classmethod
    def _to_ticks(cls, seconds: object) -> int:
        raise invalid_arg_type("seconds", "number or timedelta", seconds)

    # Python 3.9: pass the type to register() in order to work around
    # https://github.com/python/cpython/issues/86153 - singledispatchmethod raises an error when
    # relying on a forward declaration
    @_to_ticks.register(SupportsIndex)
    @classmethod
    def _(cls, seconds: SupportsIndex) -> int:
        return operator.index(seconds) << _BITS_PER_SECOND

    @_to_ticks.register(Decimal)
    @classmethod
    def _(cls, seconds: Decimal) -> int:
        with decimal.localcontext() as ctx:
            ctx.prec = _DECIMAL_DIGITS
            whole_seconds, fractional_seconds = divmod(seconds, 1)
            ticks = int(whole_seconds) * _TICKS_PER_SECOND
            ticks += round(fractional_seconds * _TICKS_PER_SECOND)
            return ticks

    @_to_ticks.register(float)
    @classmethod
    def _(cls, seconds: float) -> int:
        fractional_seconds, whole_seconds = math.modf(seconds)
        ticks = int(whole_seconds) * _TICKS_PER_SECOND
        ticks += round(fractional_seconds * _TICKS_PER_SECOND)
        return ticks

    @_to_ticks.register(ht.timedelta)
    @classmethod
    def _(cls, seconds: ht.timedelta) -> int:
        return cls._to_ticks(seconds.precision_total_seconds())

    @_to_ticks.register(dt.timedelta)
    @classmethod
    def _(cls, seconds: dt.timedelta) -> int:
        # Do not use total_seconds() because it loses precision.
        ticks = (seconds.days * _SECONDS_PER_DAY) << _BITS_PER_SECOND
        ticks += seconds.seconds << _BITS_PER_SECOND
        ticks += (seconds.microseconds << _BITS_PER_SECOND) // _MICROSECONDS_PER_SECOND
        return ticks

    @_to_ticks.register(type(None))
    @classmethod
    def _(cls, seconds: None) -> int:
        return 0

    @classmethod
    def from_ticks(cls, ticks: SupportsIndex) -> Self:
        """Create a TimeDelta from a 128-bit fixed point number expressed as an integer."""
        ticks = arg_to_int("ticks", ticks)
        if not (_INT128_MIN <= ticks <= _INT128_MAX):
            raise int_out_of_range(ticks, _INT128_MIN, _INT128_MAX)
        self = cls.__new__(cls)
        self._ticks = ticks
        return self

    @classmethod
    def from_tuple(cls, value: TimeValueTuple) -> Self:
        """Create a TimeDelta from 64-bit whole seconds and fractional seconds ints."""
        if not (_INT64_MIN <= value.whole_seconds <= _INT64_MAX):
            raise int_out_of_range(value.whole_seconds, _INT64_MIN, _INT64_MAX)
        if not (_UINT64_MIN <= value.fractional_seconds <= _UINT64_MAX):
            raise int_out_of_range(value.fractional_seconds, _UINT64_MIN, _UINT64_MAX)
        ticks = value.whole_seconds << _BITS_PER_SECOND
        ticks = ticks | value.fractional_seconds
        return cls.from_ticks(ticks)

    def _to_datetime_timedelta(self) -> dt.timedelta:
        """Return self as a :any:`datetime.timedelta`."""
        whole_seconds = self._ticks >> _BITS_PER_SECOND
        microseconds = (
            _MICROSECONDS_PER_SECOND * (self._ticks & _FRACTIONAL_SECONDS_MASK)
        ) >> _BITS_PER_SECOND
        return dt.timedelta(seconds=whole_seconds, microseconds=microseconds)

    def _to_hightime_timedelta(self) -> ht.timedelta:
        """Return self as a :any:`hightime.timedelta`."""
        whole_seconds = self._ticks >> _BITS_PER_SECOND
        yoctoseconds = (
            _YOCTOSECONDS_PER_SECOND * (self._ticks & _FRACTIONAL_SECONDS_MASK)
        ) >> _BITS_PER_SECOND
        return ht.timedelta(seconds=whole_seconds, yoctoseconds=yoctoseconds)

    @property
    def days(self) -> int:
        """The number of days in the time delta."""
        return (self._ticks >> _BITS_PER_SECOND) // _SECONDS_PER_DAY

    @property
    def seconds(self) -> int:
        """The number of seconds in the time delta, up to the nearest day."""
        return (self._ticks >> _BITS_PER_SECOND) % _SECONDS_PER_DAY

    @property
    def microseconds(self) -> int:
        """The number of microseconds in the time delta, up to the nearest second."""
        return (
            _MICROSECONDS_PER_SECOND * (self._ticks & _FRACTIONAL_SECONDS_MASK)
        ) >> _BITS_PER_SECOND

    @property
    def femtoseconds(self) -> int:
        """The number of femtoseconds in the time delta, up to the nearest microsecond."""
        value = (
            _FEMTOSECONDS_PER_SECOND * (self._ticks & _FRACTIONAL_SECONDS_MASK) >> _BITS_PER_SECOND
        )
        return value % _FEMTOSECONDS_PER_MICROSECOND

    @property
    def yoctoseconds(self) -> int:
        """The number of yoctoseconds in the time delta, up to the nearest femtosecond.

        .. warning::
            Because this class uses a 64-bit binary fraction, the smallest value it can represent
            is ``1.0 / (1 << 64)`` seconds, which is about 54210 yoctoseconds.
        """
        value = (
            _YOCTOSECONDS_PER_SECOND * (self._ticks & _FRACTIONAL_SECONDS_MASK)
        ) >> _BITS_PER_SECOND
        return value % _YOCTOSECONDS_PER_FEMTOSECOND

    @property
    def ticks(self) -> int:
        """The total ticks in the time delta as a 128-bit integer."""
        return self._ticks

    def to_tuple(self) -> TimeValueTuple:
        """The whole seconds and fractional seconds parts of the time delta as 64-bit ints."""
        whole_seconds = self._ticks >> _BITS_PER_SECOND
        fractional_seconds = self._ticks & _FRACTIONAL_SECONDS_MASK
        return TimeValueTuple(whole_seconds, fractional_seconds)

    def total_seconds(self) -> float:
        """The total seconds in the time delta.

        .. warning::
            Converting a time value to a floating point number loses precision. Consider using
            :any:`precision_total_seconds` instead.
        """
        seconds = float(self._ticks >> _BITS_PER_SECOND)
        seconds += float((self._ticks & _FRACTIONAL_SECONDS_MASK) / _TICKS_PER_SECOND)
        return seconds

    def precision_total_seconds(self) -> Decimal:
        """The precise total seconds in the time delta.

        Note: up to 64 significant digits are used in computation.
        """
        with decimal.localcontext() as ctx:
            ctx.prec = _DECIMAL_DIGITS
            seconds = Decimal(self._ticks >> _BITS_PER_SECOND)
            seconds += Decimal(self._ticks & _FRACTIONAL_SECONDS_MASK) / Decimal(_TICKS_PER_SECOND)
            return seconds

    def __neg__(self) -> TimeDelta:
        """Return -self."""
        return self.__class__.from_ticks(-self._ticks)

    def __pos__(self) -> TimeDelta:
        """Return +self."""
        return self

    def __abs__(self) -> TimeDelta:
        """Return abs(self)."""
        return -self if self._ticks < 0 else self

    @overload
    def __add__(  # noqa: D105 - missing docstring in magic method
        self, value: TimeDelta | _OtherTimeDelta, /
    ) -> TimeDelta: ...

    @overload
    def __add__(  # noqa: D105 - missing docstring in magic method
        self, value: ht.datetime, /
    ) -> ht.datetime: ...

    @overload
    def __add__(  # noqa: D105 - missing docstring in magic method
        self, value: dt.datetime, /
    ) -> dt.datetime: ...

    def __add__(
        self, value: TimeDelta | _OtherTimeDelta | _OtherDateTime, /
    ) -> TimeDelta | _OtherDateTime:
        """Return self+value."""
        if isinstance(value, TimeDelta):
            return self.__class__.from_ticks(self._ticks + value._ticks)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self + self.__class__(value)
        elif isinstance(value, ht.datetime):
            return self._to_hightime_timedelta() + value
        # Handle dt.datetime separately to round to the nearest microsecond instead of truncating.
        elif isinstance(value, dt.datetime):
            return self._to_datetime_timedelta() + value
        else:
            return NotImplemented

    __radd__ = __add__

    # __sub__ doesn't support _TOtherDateTime because it doesn't make sense to negate a datetime.
    def __sub__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta:
        """Return self-value."""
        if isinstance(value, TimeDelta):
            return self.__class__.from_ticks(self._ticks - value._ticks)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self - self.__class__(value)
        else:
            return NotImplemented

    # __rsub__ supports _TOtherDateTime in order to support subtracting a bintime.TimeDelta from a
    # datetime.datetime or hightime.datetime.
    @overload
    def __rsub__(  # noqa: D105 - missing docstring in magic method
        self, value: TimeDelta | _OtherTimeDelta, /
    ) -> TimeDelta: ...

    @overload
    def __rsub__(  # noqa: D105 - missing docstring in magic method
        self, value: ht.datetime, /
    ) -> ht.datetime: ...

    @overload
    def __rsub__(  # noqa: D105 - missing docstring in magic method
        self, value: dt.datetime, /
    ) -> dt.datetime: ...

    def __rsub__(
        self, value: TimeDelta | _OtherTimeDelta | _OtherDateTime, /
    ) -> TimeDelta | _OtherDateTime:
        """Return value-self."""
        if isinstance(value, TimeDelta):
            return self.__class__.from_ticks(value._ticks - self._ticks)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self.__class__(value) - self
        elif isinstance(value, ht.datetime):
            return value - self._to_hightime_timedelta()
        # Handle dt.datetime separately to round to the nearest microsecond instead of truncating.
        elif isinstance(value, dt.datetime):
            return value - self._to_datetime_timedelta()
        else:
            return NotImplemented

    def __mul__(self, value: int | float | Decimal, /) -> TimeDelta:
        """Return self*value."""
        if isinstance(value, int):
            return self.__class__.from_ticks(self._ticks * value)
        elif isinstance(value, float):
            # Using floating point math on 128-bit numbers loses precision, so use Decimal math.
            return self * Decimal(value)
        elif isinstance(value, Decimal):
            with decimal.localcontext() as ctx:
                ctx.prec = _DECIMAL_DIGITS
                return self.__class__(self.precision_total_seconds() * value)
        else:
            return NotImplemented

    __rmul__ = __mul__

    @overload
    def __floordiv__(  # noqa: D105 - missing docstring in magic method
        self, value: TimeDelta, /
    ) -> int: ...
    @overload
    def __floordiv__(  # noqa: D105 - missing docstring in magic method
        self, value: int, /
    ) -> TimeDelta: ...

    def __floordiv__(self, value: TimeDelta | int, /) -> int | TimeDelta:
        """Return self//value."""
        if isinstance(value, TimeDelta):
            return self._ticks // value._ticks
        elif isinstance(value, int):
            return self.__class__.from_ticks(self._ticks // value)
        else:
            return NotImplemented

    @overload
    def __truediv__(  # noqa: D105 - missing docstring in magic method
        self, value: TimeDelta, /
    ) -> float: ...
    @overload
    def __truediv__(  # noqa: D105 - missing docstring in magic method
        self, value: float, /
    ) -> TimeDelta: ...

    def __truediv__(self, value: TimeDelta | float, /) -> float | TimeDelta:
        """Return self/value."""
        if isinstance(value, TimeDelta):
            return self.total_seconds() / value.total_seconds()
        elif isinstance(value, float):
            return self.__class__(self.total_seconds() / value)
        else:
            return NotImplemented

    def __mod__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta:
        """Return self%value."""
        if isinstance(value, TimeDelta):
            return self.__class__.from_ticks(self._ticks % value._ticks)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return self % self.__class__(value)
        else:
            return NotImplemented

    def __divmod__(self, value: TimeDelta | _OtherTimeDelta, /) -> tuple[int, TimeDelta]:
        """Return (self//value, self%value)."""
        if isinstance(value, TimeDelta):
            return (self // value, self % value)
        elif isinstance(value, _OTHER_TIMEDELTA_TUPLE):
            return divmod(self, self.__class__(value))
        else:
            return NotImplemented

    # In comparison operators, always promote to the more precise data type (dt -> bt, bt -> ht).
    def __lt__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool:
        """Return self<value."""
        if isinstance(value, self.__class__):
            return self._ticks < value._ticks
        elif isinstance(value, ht.timedelta):
            return self._to_hightime_timedelta() < value
        elif isinstance(value, dt.timedelta):
            return self < self.__class__(value)
        else:
            return NotImplemented

    def __le__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool:
        """Return self<=value."""
        if isinstance(value, self.__class__):
            return self._ticks <= value._ticks
        elif isinstance(value, ht.timedelta):
            return self._to_hightime_timedelta() <= value
        elif isinstance(value, dt.timedelta):
            return self <= self.__class__(value)
        else:
            return NotImplemented

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if isinstance(value, self.__class__):
            return self._ticks == value._ticks
        elif isinstance(value, ht.timedelta):
            return self._to_hightime_timedelta() == value
        elif isinstance(value, dt.timedelta):
            return self == self.__class__(value)
        else:
            return NotImplemented

    def __gt__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool:
        """Return self<value."""
        if isinstance(value, self.__class__):
            return self._ticks > value._ticks
        elif isinstance(value, ht.timedelta):
            return self._to_hightime_timedelta() > value
        elif isinstance(value, dt.timedelta):
            return self > self.__class__(value)
        else:
            return NotImplemented

    def __ge__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool:
        """Return self>=value."""
        if isinstance(value, self.__class__):
            return self._ticks >= value._ticks
        elif isinstance(value, ht.timedelta):
            return self._to_hightime_timedelta() >= value
        elif isinstance(value, dt.timedelta):
            return self >= self.__class__(value)
        else:
            return NotImplemented

    def __bool__(self) -> bool:
        """Return bool(self)."""
        return self._ticks != 0

    def __hash__(self) -> int:
        """Return hash(self)."""
        return hash(self._ticks)

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        return (self.__class__.from_ticks, (self._ticks,))

    def __str__(self) -> str:
        """Return repr(self)."""
        days = self.days
        seconds = self.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        # Display up to 18 digits of fractional seconds, rounded to the nearest digit.
        fractional_seconds = 10**18 * (self._ticks & _FRACTIONAL_SECONDS_MASK)
        fractional_seconds = (fractional_seconds + _TICKS_PER_SECOND // 2) // _TICKS_PER_SECOND
        s = f"{days} day, " if abs(days) == 1 else f"{days} days, " if days else ""
        s += f"{hours}:{minutes:02}:{seconds:02}"
        if fractional_seconds != 0:
            s += f".{fractional_seconds:018}".rstrip("0")  # strip trailing zeroes
        return s

    def __repr__(self) -> str:
        """Return repr(self)."""
        if _REPR_TICKS:
            return (
                f"{self.__class__.__module__}.{self.__class__.__name__}"
                f".from_ticks({self._ticks})"
            )
        # Display up to 24 decimal digits (yoctoseconds), like hightime does. The smallest time
        # increment representable with NI-BTF is 54210 yoctoseconds, so if all 24 decimal digits are
        # displayed, the last few are due to rounding error.
        return (
            f"{self.__class__.__module__}.{self.__class__.__name__}"
            f"(Decimal('{self.precision_total_seconds():.24}'))"
        )


TimeDelta.max = TimeDelta.from_ticks(_INT128_MAX)
TimeDelta.min = TimeDelta.from_ticks(_INT128_MIN)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/bintime/_timedelta_array.py sha256=f156b8e5c01a2ad294e34bc2123cec005ffe977b52d965d38cf4f6875ee4874d bytes=7802 -->
## FILE: src/nitypes/bintime/_timedelta_array.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/bintime/_timedelta_array.py`
- sha256: `f156b8e5c01a2ad294e34bc2123cec005ffe977b52d965d38cf4f6875ee4874d`
- bytes: 7802

````python
from __future__ import annotations

from collections.abc import Iterable, MutableSequence
from typing import (
    TYPE_CHECKING,
    Any,
    final,
    overload,
)

import numpy as np
import numpy.typing as npt

from nitypes._exceptions import invalid_arg_value, invalid_arg_type

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.bintime import CVITimeIntervalDType, TimeDelta, TimeValueTuple
else:
    from nitypes.bintime._dtypes import CVITimeIntervalDType
    from nitypes.bintime._timedelta import TimeDelta
    from nitypes.bintime._time_value_tuple import TimeValueTuple


@final
class TimeDeltaArray(MutableSequence[TimeDelta]):
    """A mutable array of :class:`TimeDelta` values in NI Binary Time Format (NI-BTF).

    Raises:
        TypeError: If any item in value is not a TimeDelta instance.
    """

    __slots__ = ["_array"]

    _array: npt.NDArray[np.void]

    def __init__(
        self,
        value: Iterable[TimeDelta] | None = None,
    ) -> None:
        """Initialize a new TimeDeltaArray."""
        value = [] if value is None else list(value)
        if not all(isinstance(item, TimeDelta) for item in value):
            raise invalid_arg_type("value", "iterable of TimeDelta", value)
        self._array = np.fromiter(
            (entry.to_tuple().to_cvi() for entry in value),
            dtype=CVITimeIntervalDType,
            count=len(value),
        )

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int
    ) -> TimeDelta: ...

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> TimeDeltaArray: ...

    def __getitem__(self, index: int | slice) -> TimeDelta | TimeDeltaArray:
        """Return self[index].

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        """
        if isinstance(index, int):
            entry = self._array[index].item()
            as_tuple = TimeValueTuple.from_cvi(*entry)
            return TimeDelta.from_tuple(as_tuple)
        elif isinstance(index, slice):
            sliced_entries = self._array[index]
            new_array = TimeDeltaArray()
            new_array._array = sliced_entries
            return new_array
        else:
            raise invalid_arg_type("index", "int or slice", index)

    def __len__(self) -> int:
        """Return len(self)."""
        return len(self._array)

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int, value: TimeDelta
    ) -> None: ...

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice, value: Iterable[TimeDelta]
    ) -> None: ...

    def __setitem__(self, index: int | slice, value: TimeDelta | Iterable[TimeDelta]) -> None:
        """Set a new value for TimeDelta at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type, or slice value is not iterable.
            ValueError: If slice assignment length doesn't match the selected range.
            IndexError: If index is out of range.
        """
        if isinstance(index, int):
            if not isinstance(value, TimeDelta):
                raise invalid_arg_type("value", "TimeDelta", value)
            self._array[index] = value.to_tuple().to_cvi()
        elif isinstance(index, slice):
            if not isinstance(value, Iterable):
                raise invalid_arg_type("value", "iterable of TimeDelta", value)
            values = list(value)
            if not all(isinstance(item, TimeDelta) for item in values):
                raise invalid_arg_type("value", "iterable of TimeDelta", value)

            start, stop, step = index.indices(len(self))
            selected_count = len(range(start, stop, step))
            new_entry_count = len(values)
            if step > 1 and new_entry_count != selected_count:
                raise invalid_arg_value(
                    "value", "iterable with the same length as the slice", value
                )

            if new_entry_count < selected_count:
                # Shrink
                replaced = slice(start, start + new_entry_count)
                removed = slice(start + new_entry_count, stop)
                self._array[replaced] = [item.to_tuple().to_cvi() for item in values]
                del self[removed]
            elif new_entry_count > selected_count:
                # Grow
                replaced = slice(start, stop)
                self._array[replaced] = [
                    item.to_tuple().to_cvi() for item in values[:selected_count]
                ]
                self._array = np.insert(
                    self._array,
                    stop,
                    [item.to_tuple().to_cvi() for item in values[selected_count:]],
                )
            else:
                # Replace, accounting for strides
                self._array[index] = [item.to_tuple().to_cvi() for item in values]
        else:
            raise invalid_arg_type("index", "int or slice", index)

    @overload
    def __delitem__(self, index: int) -> None: ...  # noqa: D105 - missing docstring in magic method

    @overload
    def __delitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> None: ...

    def __delitem__(self, index: int | slice) -> None:
        """Delete the value at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        """
        if isinstance(index, (int, slice)):
            self._array = np.delete(self._array, index)
        else:
            raise invalid_arg_type("index", "int or slice", index)

    def insert(self, index: int, value: TimeDelta) -> None:
        """Insert the TimeDelta value before the specified index.

        Raises:
            TypeError: If index is not int or value is not TimeDelta.
        """
        if not isinstance(index, int):
            raise invalid_arg_type("index", "int", index)
        if not isinstance(value, TimeDelta):
            raise invalid_arg_type("value", "TimeDelta", value)
        lower = -len(self._array)
        upper = len(self._array)
        index = min(max(index, lower), upper)
        as_cvi = value.to_tuple().to_cvi()
        self._array = np.insert(self._array, index, as_cvi)

    def extend(self, values: Iterable[TimeDelta]) -> None:
        """Extend the array by appending the elements from values."""
        if values is None:
            raise invalid_arg_type("values", "iterable of DateTime", values)
        new_array = TimeDeltaArray(values)
        self._array = np.append(self._array, new_array._array)

    def __eq__(self, other: object) -> bool:
        """Return self == other."""
        if not isinstance(other, TimeDeltaArray):
            return NotImplemented
        return np.array_equal(self._array, other._array)

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        return (self.__class__, (list(iter(self)),))

    def __repr__(self) -> str:
        """Return repr(self)."""
        ctor_args = list(iter(self))
        return f"{self.__class__.__module__}.{self.__class__.__name__}({ctor_args})"

    def __str__(self) -> str:
        """Return str(self)."""
        values = list(iter(self))
        return f"[{'; '.join(str(v) for v in values)}]"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/complex/__init__.py sha256=157ffd85ae9660d129c0f0f7902b9af4e374541507e793a8a900bf976b89456e bytes=4852 -->
## FILE: src/nitypes/complex/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/complex/__init__.py`
- sha256: `157ffd85ae9660d129c0f0f7902b9af4e374541507e793a8a900bf976b89456e`
- bytes: 4852

````python
"""Complex number data types for NI Python APIs.

================
Complex Integers
================

Some NI driver APIs (such as NI-FGEN, NI-SCOPE, NI-RFSA, and NI-RFSG) use complex numbers to
represent I/Q data. Python and NumPy have native support for complex floating-point numbers, but
not complex integers, so the :mod:`nitypes.complex` submodule provides a NumPy representation of
complex integers.

:any:`ComplexInt32DType` is a NumPy structured data type object representing a complex integer with
16-bit ``real`` and ``imag`` fields. This structured data type has the same memory layout as the
``NIComplexI16`` C struct used by NI driver APIs.

For more information about NumPy structured data types, see the
:ref:`NumPy documentation on structured arrays <numpy:structured_arrays>`.

.. note::
   In ``NIComplexI16``, the number 16 refers to the number of bits in each field. In
   :any:`ComplexInt32DType`, the number 32 refers to the total number of bits, following the
   precedent set by NumPy's other complex types. For example, :any:`numpy.complex128` contains
   64-bit ``real`` and ``imag`` fields.

Constructing arrays of complex integers
---------------------------------------

You can construct an array of complex integers from a sequence of tuples using :func:`numpy.array`:

>>> import numpy as np
>>> np.array([(1, 2), (3, 4)], dtype=ComplexInt32DType)
array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])

Likewise, you can construct an array of complex integer zeros using :func:`numpy.zeros`:

>>> np.zeros(3, dtype=ComplexInt32DType)
array([(0, 0), (0, 0), (0, 0)], dtype=[('real', '<i2'), ('imag', '<i2')])

Indexing and slicing
--------------------

Indexing the array gives you a complex integer structured scalar:

>>> x = np.array([(1, 2), (3, 4), (5, 6)], dtype=ComplexInt32DType)
>>> x[0]
np.void((1, 2), dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[1]
np.void((3, 4), dtype=[('real', '<i2'), ('imag', '<i2')])

.. note:
    NumPy displays :any:`numpy.void` because the :any:`ComplexInt32DType` structured data type has
    a base type of :any:`numpy.void`. Using a different base type such as :any:`numpy.int32`
    would have benefits, such as making it easier to convert array elements to/from
    :any:`numpy.int32`, but it would also have drawbacks, such as making it harder to initialize
    the array using a sequence of tuples.

You can index a complex integer structured scalar to get the real and imaginary parts:

>>> x[0][0]
np.int16(1)
>>> x[0][1]
np.int16(2)

You can also index by the field names ``real`` and ``imag``:

>>> x[0]['real']
np.int16(1)
>>> x[0]['imag']
np.int16(2)

Or you can index the entire array by the field names ``real`` and ``imag``:

>>> x['real']
array([1, 3, 5], dtype=int16)
>>> x['imag']
array([2, 4, 6], dtype=int16)

Arrays of complex integers support slicing and negative indices like any other array:

>>> x[0:2]
array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[1:]
array([(3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[-1]
np.void((5, 6), dtype=[('real', '<i2'), ('imag', '<i2')])

Conversion
----------

To convert a complex integer structured scalar to a tuple, use the :any:`numpy.ndarray.item`
method:

>>> x[0].item()
(1, 2)
>>> [y.item() for y in x]
[(1, 2), (3, 4), (5, 6)]

To convert NumPy arrays between between different complex number data types, use the
:func:`convert_complex` function:

>>> convert_complex(np.complex128, x)
array([1.+2.j, 3.+4.j, 5.+6.j])
>>> convert_complex(ComplexInt32DType, np.array([1.23+4.56j]))
array([(1, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])

You can also use :func:`convert_complex` with NumPy scalars:

>>> convert_complex(np.complex128, x[0])
np.complex128(1+2j)
>>> convert_complex(ComplexInt32DType, np.complex128(3+4j))
np.void((3, 4), dtype=[('real', '<i2'), ('imag', '<i2')])

.. note::
    As of NumPy 2.2, shape typing is still under development, so its type hints do not reflect that
    many operations coerce zero-dimensional arrays to :any:`numpy.generic`. The type hints for the
    scalar overloads of :func:`convert_complex` follow this precedent and return an
    :any:`numpy.ndarray`. This behavior may change in a future release.

Mathematical operations
-----------------------

Structured arrays of complex integers do not support mathematical operations. Convert
them to arrays of complex floating-point numbers before doing any sort of math or analysis.
"""

from nitypes.complex._conversion import convert_complex
from nitypes.complex._dtypes import ComplexInt32Base, ComplexInt32DType

__all__ = ["convert_complex", "ComplexInt32DType", "ComplexInt32Base"]
__doctest_requires__ = {".": ["numpy>=2.0"]}
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/complex/_conversion.py sha256=ac5c082d563b84f68c1e6d3a4ede7c1b834add2b68ce8af631b1d773080bb718 bytes=3849 -->
## FILE: src/nitypes/complex/_conversion.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/complex/_conversion.py`
- sha256: `ac5c082d563b84f68c1e6d3a4ede7c1b834add2b68ce8af631b1d773080bb718`
- bytes: 3849

````python
from __future__ import annotations

from typing import Any, TypeVar, cast, overload

import numpy as np
import numpy.typing as npt

from nitypes._arguments import validate_dtype
from nitypes._exceptions import unsupported_dtype
from nitypes.complex._dtypes import ComplexInt32DType

_Item_co = TypeVar("_Item_co", bound=Any)
_ScalarType = TypeVar("_ScalarType", bound=np.generic)
_Shape = TypeVar("_Shape", bound=tuple[int, ...])

_COMPLEX_DTYPES = (
    np.complex64,
    np.complex128,
    ComplexInt32DType,
)

_FIELD_DTYPE = {
    np.dtype(np.complex64): np.float32,
    np.dtype(np.complex128): np.float64,
    ComplexInt32DType: np.int16,
}


@overload
def convert_complex(
    requested_dtype: type[_ScalarType] | np.dtype[_ScalarType],
    value: np.ndarray[_Shape, Any],
) -> np.ndarray[_Shape, np.dtype[_ScalarType]]: ...


@overload
def convert_complex(
    requested_dtype: npt.DTypeLike, value: np.ndarray[_Shape, Any]
) -> np.ndarray[_Shape, Any]: ...


# https://numpy.org/doc/2.2/reference/typing.html#d-arrays
# "While thus not strictly correct, all operations are that can potentially perform a 0D-array ->
# scalar cast are currently annotated as exclusively returning an ndarray."
@overload
def convert_complex(
    requested_dtype: type[_ScalarType] | np.dtype[_ScalarType],
    value: np.generic[Any],
) -> np.ndarray[tuple[()], np.dtype[_ScalarType]]: ...


@overload
def convert_complex(
    requested_dtype: npt.DTypeLike,
    value: np.generic[Any],
) -> np.ndarray[tuple[()], Any]: ...


def convert_complex(
    requested_dtype: npt.DTypeLike, value: np.ndarray[_Shape, Any] | np.generic[Any]
) -> np.ndarray[_Shape, Any]:
    """Convert a NumPy array or scalar of complex numbers to the specified dtype.

    Args:
        requested_dtype: The NumPy data type to convert to. Supported data types:
            :any:`numpy.complex64`, :any:`numpy.complex128`, :any:`ComplexInt32DType`.
        value: The NumPy array or scalar to convert.

    Returns:
        The value converted to the specified dtype.
    """
    validate_dtype(requested_dtype, _COMPLEX_DTYPES)
    if requested_dtype == value.dtype:
        return cast(np.ndarray[_Shape, Any], value)
    elif requested_dtype == ComplexInt32DType or value.dtype == ComplexInt32DType:
        # ndarray.view on scalars requires the source and destination types to have the same size,
        # so reshape the scalar into an 1-element array before converting and index it afterwards.
        # shape == () means this is either a scalar (np.generic) or a 0-dimension array, but mypy
        # doesn't know that.
        if value.shape == ():
            return cast(
                np.ndarray[_Shape, Any],
                _convert_complexint32_array(requested_dtype, value.reshape(1))[0],
            )
        else:
            return _convert_complexint32_array(
                requested_dtype, cast(np.ndarray[_Shape, Any], value)
            )
    else:
        return value.astype(requested_dtype)


def _convert_complexint32_array(
    requested_dtype: npt.DTypeLike | type[_ScalarType] | np.dtype[_ScalarType],
    value: np.ndarray[_Shape, Any],
) -> np.ndarray[_Shape, np.dtype[_ScalarType]]:
    if not isinstance(requested_dtype, np.dtype):
        requested_dtype = np.dtype(requested_dtype)

    requested_field_dtype = _FIELD_DTYPE.get(requested_dtype)
    if requested_field_dtype is None:
        raise unsupported_dtype("requested data type", requested_dtype, _COMPLEX_DTYPES)

    value_field_dtype = _FIELD_DTYPE.get(value.dtype)
    if value_field_dtype is None:
        raise unsupported_dtype("array data type", value.dtype, _COMPLEX_DTYPES)

    return value.view(value_field_dtype).astype(requested_field_dtype).view(requested_dtype)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/complex/_dtypes.py sha256=ecc7aa63168917476551ed8c20bb0e0d9474f1054d2d2ce3d65e7131097a8e4e bytes=425 -->
## FILE: src/nitypes/complex/_dtypes.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/complex/_dtypes.py`
- sha256: `ecc7aa63168917476551ed8c20bb0e0d9474f1054d2d2ce3d65e7131097a8e4e`
- bytes: 425

````python
from __future__ import annotations

import numpy as np
from typing_extensions import TypeAlias

ComplexInt32Base: TypeAlias = np.void
"""Type alias for the base type of :any:`ComplexInt32DType`, which is :any:`numpy.void`."""

ComplexInt32DType = np.dtype((ComplexInt32Base, [("real", np.int16), ("imag", np.int16)]))
"""NumPy structured data type for a complex integer with 16-bit ``real`` and ``imag`` fields."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/nitypes/py.typed

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/scalar.py sha256=a2422bef5521904e73941652a13dbfcf3c0f1bd4458fc15bdbf315dc839312c1 bytes=11907 -->
## FILE: src/nitypes/scalar.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/scalar.py`
- sha256: `a2422bef5521904e73941652a13dbfcf3c0f1bd4458fc15bdbf315dc839312c1`
- bytes: 11907

````python
"""Scalar data types for NI Python APIs.

Scalar Data Type
=================

:class:`Scalar`: A scalar data object represents a single scalar value with units information.
Valid types for the scalar value are :any:`bool`, :any:`int`, :any:`float`, and :any:`str`.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Generic, Union

from typing_extensions import Self, TypeVar, final

from nitypes._exceptions import invalid_arg_type
from nitypes.waveform._extended_properties import UNIT_DESCRIPTION
from nitypes.waveform.typing import ExtendedPropertyValue

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ExtendedPropertyDictionary
else:
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary

TScalar_co = TypeVar("TScalar_co", bound=Union[bool, int, float, str], covariant=True)
_NUMERIC = (bool, int, float)


@final
class Scalar(Generic[TScalar_co]):
    """A scalar data class, which encapsulates scalar data and units information.

    Constructing
    ^^^^^^^^^^^^

    To construct a scalar data object, use the :class:`Scalar` class:

    >>> Scalar(False)
    nitypes.scalar.Scalar(value=False)
    >>> Scalar(0)
    nitypes.scalar.Scalar(value=0)
    >>> Scalar(5.0, 'volts')
    nitypes.scalar.Scalar(value=5.0, units='volts')
    >>> Scalar("value", "volts")
    nitypes.scalar.Scalar(value='value', units='volts')

    Comparing Scalar Objects
    ^^^^^^^^^^^^^^^^^^^^^^^^

    You can compare scalar objects using standard comparison
    operators: ``<``, ``<=``, ``>``, ``>=``, ``==``, and ``!=``.
    Detailed descriptions of operator behaviors are provided below.

    Equality Comparison Operators
    -----------------------------

    Equality comparison operators (``==`` and ``!=``) are always supported and behave as follows:

    - Comparison of scalar objects with compatible types and identical units results
      in ``True`` or ``False`` based on the comparison of scalar object values.
    - Comparison of scalar objects with incompatible types (such as numeric and string)
      results in inequality.
    - Comparison of scalar objects with different units results in inequality.

    Here are a few examples:

    >>> Scalar(5.0, 'V') == Scalar(5.0, 'V') # Numeric scalars with identical values and units
    True
    >>> Scalar(5.0, 'V') == Scalar(12.3, 'V') # Numeric scalars with identical units
    False
    >>> Scalar(5.0, 'V') != Scalar(12.3, 'V') # Numeric scalars with identical units
    True
    >>> Scalar("apple") == Scalar("banana") # String scalars
    False
    >>> Scalar("apple") == Scalar("Apple") # String scalars - note case sensitivity
    False
    >>> Scalar(0.5, 'V') == Scalar(500, 'mV') # Numeric scalars with different units
    False
    >>> Scalar(5.0, 'V') == Scalar("5.0", 'V') # Comparison of a numeric and a string scalar
    False

    Order Comparison Operators
    --------------------------

    Order comparison operators (``<``, ``<=``, ``>``, and ``>=``) behave as follows:

    - Comparison of scalar objects with compatible types and identical units results
      in ``True`` or ``False`` based on the comparison of scalar object values.
    - Comparison of scalar objects with incompatible types (such as numeric and string)
      is not permitted and will raise a ``TypeError`` exception.
    - Comparison of scalar objects with compatible types and different units
      is not permitted and will raise a ``ValueError`` exception.

    Here are a few examples:

    >>> Scalar(5.0, 'V') < Scalar(10.0, 'V') # Numeric scalars with identical units
    True
    >>> Scalar(5.0, 'V') >= Scalar(10.0, 'V') # Numeric scalars with identical units
    False
    >>> Scalar("apple") < Scalar("banana") # String scalars
    True
    >>> Scalar("apple") < Scalar("Banana") # String scalars - note case sensitivity
    False
    >>> Scalar(5.0, 'V') < Scalar("5.0", 'V') # Comparison of a numeric and a string scalar
    Traceback (most recent call last):
        ...
    TypeError: Comparing Scalar objects of numeric and string types is not permitted.
    >>> Scalar(0.5, 'V') < Scalar(500, 'mV') # Numeric scalars with different units
    Traceback (most recent call last):
        ...
    ValueError: Comparing Scalar objects with different units is not permitted.

    Class Members
    ^^^^^^^^^^^^^
    """

    __slots__ = [
        "_value",
        "_extended_properties",
    ]

    _value: TScalar_co
    _extended_properties: ExtendedPropertyDictionary

    def __init__(
        self,
        value: TScalar_co,
        units: str = "",
        *,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
    ) -> None:
        """Initialize a new scalar.

        Args:
            value: The scalar data to store in this object.
            units: The units string associated with this data.
            extended_properties: The extended properties of the Scalar.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A scalar data object.
        """
        if not isinstance(value, (bool, int, float, str)):
            raise invalid_arg_type("scalar input data", "bool, int, float, or str", value)

        if not isinstance(units, str):
            raise invalid_arg_type("units", "str", units)

        self._value = value
        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties

        # If units are not already in extended properties, set them.
        if UNIT_DESCRIPTION not in self._extended_properties:
            self._extended_properties[UNIT_DESCRIPTION] = units
        elif units and units != self._extended_properties.get(UNIT_DESCRIPTION):
            raise ValueError(
                "The specified units input does not match the units specified in "
                "extended_properties."
            )

    @property
    def value(self) -> TScalar_co:
        """The scalar value."""
        return self._value

    @property
    def units(self) -> str:
        """The unit of measurement, such as volts, of the scalar."""
        value = self._extended_properties.get(UNIT_DESCRIPTION, "")
        assert isinstance(value, str)
        return value

    @units.setter
    def units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("units", "str", value)
        self._extended_properties[UNIT_DESCRIPTION] = value

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the scalar.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        """
        return self._extended_properties

    def __eq__(self, other: object, /) -> bool:
        """Return self == other."""
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.value == other.value and self.units == other.units

    def __gt__(self, other: Scalar[TScalar_co], /) -> bool:
        """Return self > other."""
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_units_equal_for_comparison(other.units)
        if isinstance(self.value, _NUMERIC) and isinstance(other.value, _NUMERIC):
            return self.value > other.value  # type: ignore[no-any-return,operator]  # https://github.com/python/mypy/issues/19454
        elif isinstance(self.value, str) and isinstance(other.value, str):
            return self.value > other.value
        else:
            raise _comparing_numeric_and_string_not_permitted()

    def __ge__(self, other: Scalar[TScalar_co], /) -> bool:
        """Return self >= other."""
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_units_equal_for_comparison(other.units)
        if isinstance(self.value, _NUMERIC) and isinstance(other.value, _NUMERIC):
            return self.value >= other.value  # type: ignore[no-any-return,operator]  # https://github.com/python/mypy/issues/19454
        elif isinstance(self.value, str) and isinstance(other.value, str):
            return self.value >= other.value
        else:
            raise _comparing_numeric_and_string_not_permitted()

    def __lt__(self, other: Scalar[TScalar_co], /) -> bool:
        """Return self < other."""
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_units_equal_for_comparison(other.units)
        if isinstance(self.value, _NUMERIC) and isinstance(other.value, _NUMERIC):
            return self.value < other.value  # type: ignore[no-any-return,operator]  # https://github.com/python/mypy/issues/19454
        elif isinstance(self.value, str) and isinstance(other.value, str):
            return self.value < other.value
        else:
            raise _comparing_numeric_and_string_not_permitted()

    def __le__(self, other: Scalar[TScalar_co], /) -> bool:
        """Return self <= other."""
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_units_equal_for_comparison(other.units)
        if isinstance(self.value, _NUMERIC) and isinstance(other.value, _NUMERIC):
            return self.value <= other.value  # type: ignore[no-any-return,operator]  # https://github.com/python/mypy/issues/19454
        elif isinstance(self.value, str) and isinstance(other.value, str):
            return self.value <= other.value
        else:
            raise _comparing_numeric_and_string_not_permitted()

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self.value,)
        ctor_kwargs: dict[str, Any] = {
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"value={self.value!r}"]

        if self.units:
            args.append(f"units={self.units!r}")

        # Only display the extended properties if non-units entries are specified.
        if any(key for key in self.extended_properties.keys() if key != UNIT_DESCRIPTION):
            args.append(f"extended_properties={self.extended_properties!r}")

        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"

    def __str__(self) -> str:
        """Return str(self)."""
        value_str = str(self.value)
        if self.units:
            value_str += f" {self.units}"

        return value_str

    def _check_units_equal_for_comparison(self, other_units: str) -> None:
        if self.units != other_units:
            raise ValueError("Comparing Scalar objects with different units is not permitted.")


def _comparing_numeric_and_string_not_permitted() -> TypeError:
    return TypeError("Comparing Scalar objects of numeric and string types is not permitted.")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/time/__init__.py sha256=d6c2cf954c46eaf5dd862ce24ebbc9cea3a02dfe5ef2397deb27fdf2cd1beeb4 bytes=188 -->
## FILE: src/nitypes/time/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/time/__init__.py`
- sha256: `d6c2cf954c46eaf5dd862ce24ebbc9cea3a02dfe5ef2397deb27fdf2cd1beeb4`
- bytes: 188

````python
"""Time data types for NI Python APIs."""

from nitypes.time._conversion import convert_datetime, convert_timedelta

__all__ = [
    "convert_datetime",
    "convert_timedelta",
]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/time/_conversion.py sha256=9b9428aa57ede0de0ec9876eb2ae9f25ed8b6cb518476a146e39ee59df90d52e bytes=5049 -->
## FILE: src/nitypes/time/_conversion.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/time/_conversion.py`
- sha256: `9b9428aa57ede0de0ec9876eb2ae9f25ed8b6cb518476a146e39ee59df90d52e`
- bytes: 5049

````python
from __future__ import annotations

import datetime as dt
from collections.abc import Callable
from functools import singledispatch
from typing import Any, cast

import hightime as ht

import nitypes.bintime as bt
from nitypes._exceptions import invalid_arg_type, invalid_requested_type
from nitypes.time.typing import AnyDateTime, AnyTimeDelta, TDateTime, TTimeDelta


def convert_datetime(requested_type: type[TDateTime], value: AnyDateTime, /) -> TDateTime:
    """Convert a datetime object to the specified type."""
    convert_func = _CONVERT_DATETIME_FOR_TYPE.get(requested_type)
    if convert_func is None:
        raise invalid_requested_type("datetime", requested_type)
    return cast(TDateTime, convert_func(value))


@singledispatch
def _convert_to_bt_absolute_time(value: object, /) -> bt.DateTime:
    raise invalid_arg_type("value", "datetime", value)


@_convert_to_bt_absolute_time.register
def _(value: bt.DateTime, /) -> bt.DateTime:
    return value


@_convert_to_bt_absolute_time.register
def _(value: dt.datetime, /) -> bt.DateTime:
    return bt.DateTime(value)


@_convert_to_bt_absolute_time.register
def _(value: ht.datetime, /) -> bt.DateTime:
    return bt.DateTime(value)


@singledispatch
def _convert_to_dt_datetime(value: object, /) -> dt.datetime:
    raise invalid_arg_type("value", "datetime", value)


@_convert_to_dt_datetime.register
def _(value: bt.DateTime, /) -> dt.datetime:
    return value._to_datetime_datetime()


@_convert_to_dt_datetime.register
def _(value: dt.datetime, /) -> dt.datetime:
    return value


@_convert_to_dt_datetime.register
def _(value: ht.datetime, /) -> dt.datetime:
    return dt.datetime(
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
        value.tzinfo,
        fold=value.fold,
    )


@singledispatch
def _convert_to_ht_datetime(value: object, /) -> ht.datetime:
    raise invalid_arg_type("value", "datetime", value)


@_convert_to_ht_datetime.register
def _(value: bt.DateTime, /) -> ht.datetime:
    return value._to_hightime_datetime()


@_convert_to_ht_datetime.register
def _(value: dt.datetime, /) -> ht.datetime:
    return ht.datetime(
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
        value.tzinfo,
        fold=value.fold,
    )


@_convert_to_ht_datetime.register
def _(value: ht.datetime, /) -> ht.datetime:
    return value


_CONVERT_DATETIME_FOR_TYPE: dict[type[Any], Callable[[object], object]] = {
    bt.DateTime: _convert_to_bt_absolute_time,
    dt.datetime: _convert_to_dt_datetime,
    ht.datetime: _convert_to_ht_datetime,
}


def convert_timedelta(requested_type: type[TTimeDelta], value: AnyTimeDelta, /) -> TTimeDelta:
    """Convert a timedelta object to the specified type."""
    convert_func = _CONVERT_TIMEDELTA_FOR_TYPE.get(requested_type)
    if convert_func is None:
        raise invalid_requested_type("timedelta", requested_type)
    return cast(TTimeDelta, convert_func(value))


@singledispatch
def _convert_to_bt_timedelta(value: object, /) -> bt.TimeDelta:
    raise invalid_arg_type("value", "timedelta", value)


@_convert_to_bt_timedelta.register
def _(value: bt.TimeDelta, /) -> bt.TimeDelta:
    return value


@_convert_to_bt_timedelta.register
def _(value: dt.timedelta, /) -> bt.TimeDelta:
    return bt.TimeDelta(value)


@_convert_to_bt_timedelta.register
def _(value: ht.timedelta, /) -> bt.TimeDelta:
    return bt.TimeDelta(value)


@singledispatch
def _convert_to_dt_timedelta(value: object, /) -> dt.timedelta:
    raise invalid_arg_type("value", "timedelta", value)


@_convert_to_dt_timedelta.register
def _(value: bt.TimeDelta, /) -> dt.timedelta:
    return value._to_datetime_timedelta()


@_convert_to_dt_timedelta.register
def _(value: dt.timedelta, /) -> dt.timedelta:
    return value


@_convert_to_dt_timedelta.register
def _(value: ht.timedelta, /) -> dt.timedelta:
    return dt.timedelta(value.days, value.seconds, value.microseconds)


@singledispatch
def _convert_to_ht_timedelta(value: object, /) -> ht.timedelta:
    raise invalid_arg_type("value", "timedelta", value)


@_convert_to_ht_timedelta.register
def _(value: bt.TimeDelta, /) -> ht.timedelta:
    return value._to_hightime_timedelta()


@_convert_to_ht_timedelta.register
def _(value: dt.timedelta, /) -> ht.timedelta:
    return ht.timedelta(
        value.days,
        value.seconds,
        value.microseconds,
    )


@_convert_to_ht_timedelta.register
def _(value: ht.timedelta, /) -> ht.timedelta:
    return value


_CONVERT_TIMEDELTA_FOR_TYPE: dict[type[Any], Callable[[object], object]] = {
    bt.TimeDelta: _convert_to_bt_timedelta,
    dt.timedelta: _convert_to_dt_timedelta,
    ht.timedelta: _convert_to_ht_timedelta,
}
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/time/_types.py sha256=997be1c4f5f959384e0263320ef7a6681108daf6bf1aa0b5bb71149404b64962 bytes=369 -->
## FILE: src/nitypes/time/_types.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/time/_types.py`
- sha256: `997be1c4f5f959384e0263320ef7a6681108daf6bf1aa0b5bb71149404b64962`
- bytes: 369

````python
from __future__ import annotations

import datetime as dt

import hightime as ht

import nitypes.bintime as bt

ANY_DATETIME_TUPLE = (bt.DateTime, dt.datetime, ht.datetime)
"""Tuple of types corresponding to :any:`AnyDateTime`."""

ANY_TIMEDELTA_TUPLE = (bt.TimeDelta, dt.timedelta, ht.timedelta)
"""Tuple of types corresponding to :any:`AnyTimeDelta`."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/time/typing.py sha256=0485671b5d7096d1b55b5d48ae5a2bcd787102a2c450e123f8ef167681ef3907 bytes=1035 -->
## FILE: src/nitypes/time/typing.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/time/typing.py`
- sha256: `0485671b5d7096d1b55b5d48ae5a2bcd787102a2c450e123f8ef167681ef3907`
- bytes: 1035

````python
"""Type aliases and type variables for time types."""

from __future__ import annotations

import datetime as dt
from typing import TypeVar, Union

import hightime as ht
from typing_extensions import TypeAlias

import nitypes.bintime as bt

AnyDateTime: TypeAlias = Union[bt.DateTime, dt.datetime, ht.datetime]
"""Type alias for any ``datetime`` class.

This type alias is a union of the following types:

* :class:`nitypes.bintime.DateTime`
* :class:`datetime.datetime`
* :class:`hightime.datetime`
"""

TDateTime = TypeVar("TDateTime", bound=AnyDateTime)
"""Type variable with a bound of :any:`AnyDateTime`."""

AnyTimeDelta: TypeAlias = Union[bt.TimeDelta, dt.timedelta, ht.timedelta]
"""Type alias for any ``timedelta`` class.

This type alias is a union of the following types:

* :class:`nitypes.bintime.TimeDelta`
* :class:`datetime.timedelta`
* :class:`hightime.timedelta`
"""

TTimeDelta = TypeVar("TTimeDelta", bound=AnyTimeDelta)
"""Type variable with a bound of :any:`AnyTimeDelta`."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/vector.py sha256=949895aa2aaaf4effd6ebf036650ce91cc974850389904c99e4695e21a542b5e bytes=10133 -->
## FILE: src/nitypes/vector.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/vector.py`
- sha256: `949895aa2aaaf4effd6ebf036650ce91cc974850389904c99e4695e21a542b5e`
- bytes: 10133

````python
"""Vector data type for NI Python APIs.

Vector Data Type
=================
:class:`Vector`: A vector data object represents an array of scalar values with units information.
Valid types for the scalar value are :any:`bool`, :any:`int`, :any:`float`, and :any:`str`.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, MutableSequence, Sequence
from typing import TYPE_CHECKING, Any, Union, overload

from typing_extensions import Self, TypeVar, final, override

from nitypes._exceptions import invalid_arg_type
from nitypes.waveform._extended_properties import UNIT_DESCRIPTION
from nitypes.waveform.typing import ExtendedPropertyValue

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ExtendedPropertyDictionary
else:
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary

TScalar = TypeVar("TScalar", bound=Union[bool, int, float, str])


@final
class Vector(MutableSequence[TScalar]):
    """A sequence of scalar values with units information.

    Constructing
    ^^^^^^^^^^^^

    To construct a vector data object, use the :class:`Vector` class:

    >>> Vector([False, True])
    nitypes.vector.Vector(values=[False, True])
    >>> Vector([0, 1, 2])
    nitypes.vector.Vector(values=[0, 1, 2])
    >>> Vector([5.0, 6.0], 'volts')
    nitypes.vector.Vector(values=[5.0, 6.0], units='volts')
    >>> Vector(["one", "two"], "volts")
    nitypes.vector.Vector(values=['one', 'two'], units='volts')
    """

    __slots__ = [
        "_values",
        "_value_type",
        "_extended_properties",
    ]

    _values: list[TScalar]
    _value_type: type[TScalar]
    _extended_properties: ExtendedPropertyDictionary

    def __init__(
        self,
        values: Iterable[TScalar],
        units: str = "",
        *,
        value_type: type[TScalar] | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
    ) -> None:
        """Initialize a new vector.

        Args:
            values: The scalar values to store in this object.
            units: The units string associated with this data.
            value_type: The type of values that will be added to this Vector.
                This parameter should only be used when creating a Vector with
                an empty Iterable.
            extended_properties: The extended properties of the Vector.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A vector data object.
        """
        backing_values = list(values)
        if not backing_values:
            if not value_type:
                raise TypeError("You must specify values as non-empty or specify value_type.")
            self._value_type = value_type
        else:
            self._value_type = type(backing_values[0])
            # Validate the values input
            for value in backing_values:
                if not isinstance(value, (bool, int, float, str)):
                    raise invalid_arg_type(
                        "vector input data", "bool, int, float, or str", backing_values
                    )

                if not isinstance(value, self._value_type):
                    raise TypeError("All values in the values input must be of the same type.")

        if not isinstance(units, str):
            raise invalid_arg_type("units", "str", units)

        self._values = backing_values
        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties

        # If units are not already in extended properties, set them.
        if UNIT_DESCRIPTION not in self._extended_properties:
            self._extended_properties[UNIT_DESCRIPTION] = units
        elif units and units != self._extended_properties.get(UNIT_DESCRIPTION):
            raise ValueError(
                "The specified units input does not match the units specified in "
                "extended_properties."
            )

    @property
    def units(self) -> str:
        """The unit of measurement, such as volts, of the vector."""
        value = self._extended_properties.get(UNIT_DESCRIPTION, "")
        assert isinstance(value, str)
        return value

    @units.setter
    def units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("units", "str", value)
        self._extended_properties[UNIT_DESCRIPTION] = value

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the vector.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        """
        return self._extended_properties

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int
    ) -> TScalar: ...

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> MutableSequence[TScalar]: ...

    @override
    def __getitem__(self, index: int | slice) -> TScalar | MutableSequence[TScalar]:
        """Return the TimeDelta at the specified location."""
        return self._values[index]

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int, value: TScalar
    ) -> None: ...

    @overload
    def __setitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice, value: Iterable[TScalar]
    ) -> None: ...

    @override
    def __setitem__(self, index: int | slice, value: TScalar | Iterable[TScalar]) -> None:
        """Set value(s) at the specified location."""
        if isinstance(index, int):
            if isinstance(value, Iterable) and not isinstance(value, str):
                raise TypeError("You cannot assign an Iterable to a vector index.")
            elif not isinstance(value, self._value_type):
                raise self._create_value_mismatch_exception(value)

            self._values[index] = value
        else:  # slice
            if not isinstance(value, Iterable):
                raise TypeError("You must assign an Iterable to a Vector slice.")
            elif isinstance(value, str):  # Narrow the type to exclude string.
                raise TypeError("You cannot assign a string to Vector slice.")

            if isinstance(value, Sequence):
                # A Sequence can be iterated over multiple times, so no need for a wrapper list.
                replacement_values = value
            else:
                replacement_values = list(value)

            # Assigning an empty Iterable to a slice is valid, so we don't check for empty.
            # If an empty Iterable is assigned to a slice, that slice is deleted.
            for subval in replacement_values:
                if not isinstance(subval, self._value_type):
                    raise self._create_value_mismatch_exception(subval)

            self._values[index] = replacement_values

    def __delitem__(self, index: int | slice) -> None:
        """Delete item(s) from the specified location."""
        del self._values[index]

    def __len__(self) -> int:
        """Return the length of the Vector."""
        return len(self._values)

    def insert(self, index: int, value: TScalar) -> None:
        """Insert a value at the specified location."""
        if not isinstance(value, self._value_type):
            raise self._create_value_mismatch_exception(value)
        self._values.insert(index, value)

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self._values == value._values and self.units == value.units

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._values,)
        ctor_kwargs: dict[str, Any] = {
            "value_type": self._value_type,
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"values={self._values!r}"]

        if self.units:
            args.append(f"units={self.units!r}")

        # Only display the extended properties if non-units entries are specified.
        if any(key for key in self.extended_properties.keys() if key != UNIT_DESCRIPTION):
            args.append(f"extended_properties={self.extended_properties!r}")

        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"

    def __str__(self) -> str:
        """Return str(self)."""
        if self.units:
            values_with_units = [f"{value} {self.units}" for value in self._values]
            comma_delimited_str = ", ".join(values_with_units)
        else:
            values = [f"{value}" for value in self._values]
            comma_delimited_str = ", ".join(values)

        return f"[{comma_delimited_str}]"

    def _create_value_mismatch_exception(self, value: object) -> TypeError:
        return TypeError(
            f"Input type does not match existing type. Input Type: {type(value)} "
            f"Existing Type: {self._value_type}"
        )
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/__init__.py sha256=7ccd01c1d8a310c43fe39c6029d8816ec79e7414e33c6b874ed83b53a6a67b98 bytes=2594 -->
## FILE: src/nitypes/waveform/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/__init__.py`
- sha256: `7ccd01c1d8a310c43fe39c6029d8816ec79e7414e33c6b874ed83b53a6a67b98`
- bytes: 2594

````python
"""Waveform data types for NI Python APIs.

Waveform Data Types
===================

* :class:`AnalogWaveform`: An analog waveform represents a single analog signal with timing
  information and extended properties such as units.
* :class:`ComplexWaveform`: A complex waveform represents a single complex-number signal, such as
  I/Q data, with timing information and extended properties such as units.
* :class:`DigitalWaveform`: A digital waveform represents one or more digital signals with timing
  information and extended properties such as channel name and signal names.
* :class:`Spectrum`: A frequency spectrum represents an analog signal with frequency information
  and extended properties such as units.
"""

from nitypes.waveform._analog import AnalogWaveform
from nitypes.waveform._complex import ComplexWaveform
from nitypes.waveform._digital import (
    DigitalState,
    DigitalWaveform,
    DigitalWaveformFailure,
    DigitalWaveformSignal,
    DigitalWaveformSignalCollection,
    DigitalWaveformTestResult,
)
from nitypes.waveform._extended_properties import ExtendedPropertyDictionary
from nitypes.waveform._numeric import NumericWaveform
from nitypes.waveform._scaling import (
    NO_SCALING,
    LinearScaleMode,
    NoneScaleMode,
    ScaleMode,
)
from nitypes.waveform._spectrum import Spectrum
from nitypes.waveform._timing import SampleIntervalMode, Timing

__all__ = [
    "AnalogWaveform",
    "ComplexWaveform",
    "DigitalState",
    "DigitalWaveform",
    "DigitalWaveformFailure",
    "DigitalWaveformSignal",
    "DigitalWaveformSignalCollection",
    "DigitalWaveformTestResult",
    "ExtendedPropertyDictionary",
    "LinearScaleMode",
    "NO_SCALING",
    "NoneScaleMode",
    "NumericWaveform",
    "SampleIntervalMode",
    "ScaleMode",
    "Spectrum",
    "Timing",
]


# Hide that it was defined in a helper file
AnalogWaveform.__module__ = __name__
ComplexWaveform.__module__ = __name__
DigitalState.__module__ = __name__
DigitalWaveform.__module__ = __name__
DigitalWaveformFailure.__module__ = __name__
DigitalWaveformSignal.__module__ = __name__
DigitalWaveformSignalCollection.__module__ = __name__
DigitalWaveformTestResult.__module__ = __name__
ExtendedPropertyDictionary.__module__ = __name__
LinearScaleMode.__module__ = __name__
# NO_SCALING is a constant
NoneScaleMode.__module__ = __name__
NumericWaveform.__module__ = __name__
SampleIntervalMode.__module__ = __name__
ScaleMode.__module__ = __name__
Spectrum.__module__ = __name__
Timing.__module__ = __name__
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_analog.py sha256=351f330469f34fe701fa3852ebe27d6d3e95d0cf63ce6c04ce66f0b52e962a89 bytes=21029 -->
## FILE: src/nitypes/waveform/_analog.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_analog.py`
- sha256: `351f330469f34fe701fa3852ebe27d6d3e95d0cf63ce6c04ce66f0b52e962a89`
- bytes: 21029

````python
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, SupportsIndex, Union, overload

import numpy as np
import numpy.typing as npt
from typing_extensions import TYPE_CHECKING, TypeVar, final, override

from nitypes._numpy import long as _np_long, ulong as _np_ulong
from nitypes.time.typing import AnyDateTime, AnyTimeDelta
from nitypes.waveform._numeric import _TOtherScaled
from nitypes.waveform.typing import ExtendedPropertyValue

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import NumericWaveform, ScaleMode, Timing
else:
    from nitypes.waveform._numeric import NumericWaveform
    from nitypes.waveform._scaling import ScaleMode
    from nitypes.waveform._timing import Timing


# _TRaw specifies the type of the raw_data array. AnalogWaveform accepts a narrower set of types
# than NumericWaveform.
_TRaw = TypeVar("_TRaw", bound=Union[np.floating, np.integer])
_TOtherRaw = TypeVar("_TOtherRaw", bound=Union[np.floating, np.integer])

# Use the C types here because np.isdtype() considers some of them to be distinct types, even when
# they have the same size (e.g. np.intc vs. np.int_).
_RAW_DTYPES = (
    # Floating point
    np.single,
    np.double,
    # Signed integers
    np.byte,
    np.short,
    np.intc,
    np.int_,
    _np_long,
    np.longlong,
    # Unsigned integers
    np.ubyte,
    np.ushort,
    np.uintc,
    np.uint,
    _np_ulong,
    np.ulonglong,
)

_SCALED_DTYPES = (
    # Floating point
    np.single,
    np.double,
)


@final
class AnalogWaveform(NumericWaveform[_TRaw, np.float64]):
    """An analog waveform, which encapsulates analog data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct an analog waveform, use the :class:`AnalogWaveform` class:

    >>> AnalogWaveform()
    nitypes.waveform.AnalogWaveform(0)
    >>> AnalogWaveform(5)
    nitypes.waveform.AnalogWaveform(5, raw_data=array([0., 0., 0., 0., 0.]))

    To construct an analog waveform from a NumPy array, use the :any:`AnalogWaveform.from_array_1d`
    method.

    >>> import numpy as np
    >>> AnalogWaveform.from_array_1d(np.array([1.0, 2.0, 3.0]))
    nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.]))

    You can also use :any:`AnalogWaveform.from_array_1d` to construct an analog waveform from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> AnalogWaveform.from_array_1d([1.0, 2.0, 3.0], np.float64)
    nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.]))

    The 2D version, :any:`AnalogWaveform.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    >>> AnalogWaveform.from_array_2d(nested_list, np.float64)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.])),
    nitypes.waveform.AnalogWaveform(3, raw_data=array([4., 5., 6.]))]

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Analog waveforms include timing information, such as the start time and sample interval, to support
    analyzing and visualizing the data.

    You can specify timing information by constructing a :class:`Timing` object and passing it to the
    waveform constructor or factory method:

    >>> import datetime as dt
    >>> wfm = AnalogWaveform(timing=Timing.create_with_regular_interval(
    ...     dt.timedelta(seconds=1e-3), dt.datetime(2024, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc)
    ... ))
    >>> wfm.timing  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))

    You can query the waveform's timing information using the :class:`Timing` object's properties:

    >>> wfm.timing.start_time
    datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc)
    >>> wfm.timing.sample_interval
    datetime.timedelta(microseconds=1000)

    Timing objects are immutable, so you cannot directly set their properties:

    >>> wfm.timing.sample_interval = dt.timedelta(seconds=10e-3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AttributeError: ...

    Instead, if you want to modify the timing information for an existing waveform, you can create a new
    timing object and set the :any:`NumericWaveform.timing` property:

    >>> wfm.timing = Timing.create_with_regular_interval(
    ...     dt.timedelta(seconds=1e-3), dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc)
    ... )
    >>> wfm.timing  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))

    Timing objects support time types from the :class:`DateTime`, :any:`hightime`, and
    :any:`nitypes.bintime` modules. If you need the timing information in a specific representation, use
    the conversion methods:

    >>> wfm.timing.to_datetime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))
    >>> wfm.timing.to_hightime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=hightime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=hightime.timedelta(microseconds=1000))
    >>> wfm.timing.to_bintime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=nitypes.bintime.TimeDelta(Decimal('0.000999999999999999966606573')))

    If :any:`NumericWaveform.timing` is not specified for a given waveform, it defaults to the
    :any:`Timing.empty` singleton object.

    >>> AnalogWaveform().timing
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE)
    >>> AnalogWaveform().timing is Timing.empty
    True

    Accessing unspecified properties of the timing object raises an exception:

    >>> Timing.empty.sample_interval
    Traceback (most recent call last):
    ...
    RuntimeError: The waveform timing does not have a sample interval.

    You can use :any:`Timing.sample_interval_mode` and ``has_*`` properties such as
    :any:`Timing.has_timestamp` to query which properties of the timing object were specified:

    >>> wfm.timing.sample_interval_mode
    <SampleIntervalMode.REGULAR: 1>
    >>> (wfm.timing.has_timestamp, wfm.timing.has_sample_interval)
    (True, True)
    >>> Timing.empty.sample_interval_mode
    <SampleIntervalMode.NONE: 0>
    >>> (Timing.empty.has_timestamp, Timing.empty.has_sample_interval)
    (False, False)

    Scaling analog data
    ^^^^^^^^^^^^^^^^^^^

    By default, analog waveforms contain floating point data in :any:`numpy.float64` format, but they
    can also be used to scale raw integer data to floating-point:

    >>> import numpy as np
    >>> scale_mode = LinearScaleMode(gain=2.0, offset=0.5)
    >>> wfm = AnalogWaveform.from_array_1d([1, 2, 3], np.int32, scale_mode=scale_mode)
    >>> wfm  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3], dtype=int32),
        scale_mode=nitypes.waveform.LinearScaleMode(2.0, 0.5))
    >>> wfm.raw_data
    array([1, 2, 3], dtype=int32)
    >>> wfm.scaled_data
    array([2.5, 4.5, 6.5])

    Class members
    ^^^^^^^^^^^^^
    """  # noqa: W505 - doc line too long

    @override
    @staticmethod
    def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]:
        return np.float64

    @override
    @staticmethod
    def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]:
        return np.float64

    @override
    @staticmethod
    def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]:
        return _RAW_DTYPES

    @override
    @staticmethod
    def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]:
        return _SCALED_DTYPES

    # Override from_array_1d, from_array_2d, and __init__ in order to use overloads to control type
    # inference.
    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[_TOtherRaw],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> AnalogWaveform[_TOtherRaw]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> AnalogWaveform[_TOtherRaw]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> AnalogWaveform[Any]: ...

    @override
    @classmethod
    def from_array_1d(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> AnalogWaveform[Any]:
        """Construct an analog waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            An analog waveform containing the specified data.
        """
        return super().from_array_1d(
            array,
            dtype,
            copy=copy,
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[_TOtherRaw],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[AnalogWaveform[_TOtherRaw]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[AnalogWaveform[_TOtherRaw]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[AnalogWaveform[Any]]: ...

    @override
    @classmethod
    def from_array_2d(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> Sequence[AnalogWaveform[Any]]:
        """Construct multiple analog waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing an analog waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        """
        return super().from_array_2d(
            array,
            dtype,
            copy=copy,
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    __slots__ = ()

    # If neither dtype nor raw_data is specified, _TRaw defaults to np.float64.
    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: AnalogWaveform[np.float64],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        raw_data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: AnalogWaveform[_TOtherRaw],
        sample_count: SupportsIndex | None = ...,
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw] = ...,
        *,
        raw_data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: AnalogWaveform[_TOtherRaw],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        raw_data: npt.NDArray[_TOtherRaw] = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: AnalogWaveform[Any],
        sample_count: SupportsIndex | None = ...,
        dtype: npt.DTypeLike | None = ...,
        *,
        raw_data: npt.NDArray[Any] | None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    def __init__(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        raw_data: npt.NDArray[Any] | None = None,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> None:
        """Initialize a new analog waveform.

        Args:
            sample_count: The number of samples in the analog waveform.
            dtype: The NumPy data type for the analog waveform data. If not specified, the data
                type defaults to np.float64.
            raw_data: A NumPy ndarray to use for sample storage. The analog waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the analog waveform data begins.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the analog waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the analog waveform.
            scale_mode: The scale mode of the analog waveform.

        Returns:
            An analog waveform.
        """
        return super().__init__(
            sample_count,
            dtype,
            raw_data=raw_data,
            start_index=start_index,
            capacity=capacity,
            extended_properties=extended_properties,
            copy_extended_properties=copy_extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    @override
    def _convert_data(
        self,
        dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled],
        raw_data: npt.NDArray[_TRaw],
    ) -> npt.NDArray[_TOtherScaled]:
        return raw_data.astype(dtype)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_complex.py sha256=6701930ba280883eb19f7b5dae5063fff618212b9de973c9df3bc9e9252031c5 bytes=16998 -->
## FILE: src/nitypes/waveform/_complex.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_complex.py`
- sha256: `6701930ba280883eb19f7b5dae5063fff618212b9de973c9df3bc9e9252031c5`
- bytes: 16998

````python
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, SupportsIndex, Union, overload

import numpy as np
import numpy.typing as npt
from typing_extensions import TYPE_CHECKING, TypeVar, final, override

from nitypes.complex import ComplexInt32Base, ComplexInt32DType, convert_complex
from nitypes.time.typing import AnyDateTime, AnyTimeDelta
from nitypes.waveform._numeric import _TOtherScaled
from nitypes.waveform.typing import ExtendedPropertyValue

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import NumericWaveform, ScaleMode, Timing
else:
    from nitypes.waveform._numeric import NumericWaveform
    from nitypes.waveform._scaling import ScaleMode
    from nitypes.waveform._timing import Timing

# _TRaw specifies the type of the raw_data array. ComplexWaveform accepts a narrower set of types
# than NumericWaveform. Note that ComplexInt32Base is an alias for np.void, but other structured
# data types are rejected at run time.
_TRaw = TypeVar("_TRaw", bound=Union[np.complexfloating, ComplexInt32Base])
_TOtherRaw = TypeVar("_TOtherRaw", bound=Union[np.complexfloating, ComplexInt32Base])

_RAW_DTYPES = (
    # Complex floating point
    np.csingle,
    np.cdouble,
    # Complex integers
    ComplexInt32DType,
)

_SCALED_DTYPES = (
    # Complex floating point
    np.csingle,
    np.cdouble,
)


@final
class ComplexWaveform(NumericWaveform[_TRaw, np.complex128]):
    """A complex waveform, which encapsulates complex data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct a complex waveform, use the :class:`ComplexWaveform` class:

    >>> ComplexWaveform()
    nitypes.waveform.ComplexWaveform(0)
    >>> ComplexWaveform(5)
    nitypes.waveform.ComplexWaveform(5, raw_data=array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]))

    To construct a complex waveform from a NumPy array, use the :any:`ComplexWaveform.from_array_1d`
    method.

    >>> import numpy as np
    >>> ComplexWaveform.from_array_1d(np.array([1+2j, 3+4j, 5+6j]))
    nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j]))

    You can also use :any:`ComplexWaveform.from_array_1d` to construct a complex waveform from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> ComplexWaveform.from_array_1d([1+2j, 3+4j, 5+6j], np.complex128)
    nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j]))

    The 2D version, :any:`ComplexWaveform.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1+2j, 3+4j, 5+6j], [7+8j, 9+10j, 11+12j]]
    >>> ComplexWaveform.from_array_2d(nested_list, np.complex128)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j])),
    nitypes.waveform.ComplexWaveform(3, raw_data=array([ 7. +8.j,  9.+10.j, 11.+12.j]))]

    Scaling complex-number data
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Complex waveforms support scaling raw integer data to floating-point. Python and NumPy do not have
    native support for complex integers, so this uses the :any:`ComplexInt32DType` structured data type.

    >>> from nitypes.complex import ComplexInt32DType
    >>> scale_mode = LinearScaleMode(gain=2.0, offset=0.5)
    >>> wfm = ComplexWaveform.from_array_1d([(1, 2), (3, 4)], ComplexInt32DType, scale_mode=scale_mode)
    >>> wfm  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.ComplexWaveform(2, void32, raw_data=array([(1, 2), (3, 4)],
        dtype=[('real', '<i2'), ('imag', '<i2')]),
        scale_mode=nitypes.waveform.LinearScaleMode(2.0, 0.5))
    >>> wfm.raw_data
    array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])
    >>> wfm.scaled_data
    array([2.5+4.j, 6.5+8.j])

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Complex waveforms have the same timing information as analog waveforms. For more details, see
    :class:`AnalogWaveform`.

    Class members
    ^^^^^^^^^^^^^
    """  # noqa: W505 - doc line too long

    @override
    @staticmethod
    def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]:
        return np.complex128

    @override
    @staticmethod
    def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]:
        return np.complex128

    @override
    @staticmethod
    def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]:
        return _RAW_DTYPES

    @override
    @staticmethod
    def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]:
        return _SCALED_DTYPES

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[_TOtherRaw],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> ComplexWaveform[_TOtherRaw]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> ComplexWaveform[_TOtherRaw]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> ComplexWaveform[Any]: ...

    @override
    @classmethod
    def from_array_1d(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> ComplexWaveform[Any]:
        """Construct a complex waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A complex waveform containing the specified data.
        """
        return super().from_array_1d(
            array,
            dtype,
            copy=copy,
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[_TOtherRaw],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[ComplexWaveform[_TOtherRaw]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[ComplexWaveform[_TOtherRaw]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> Sequence[ComplexWaveform[Any]]: ...

    @override
    @classmethod
    def from_array_2d(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> Sequence[ComplexWaveform[Any]]:
        """Construct multiple complex waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing a complex waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        """
        return super().from_array_2d(
            array,
            dtype,
            copy=copy,
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    __slots__ = ()

    # If neither dtype nor raw_data is specified, _TRaw defaults to np.complex128.
    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: ComplexWaveform[np.complex128],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        raw_data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: ComplexWaveform[_TOtherRaw],
        sample_count: SupportsIndex | None = ...,
        dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw] = ...,
        *,
        raw_data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: ComplexWaveform[_TOtherRaw],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        raw_data: npt.NDArray[_TOtherRaw] = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: ComplexWaveform[Any],
        sample_count: SupportsIndex | None = ...,
        dtype: npt.DTypeLike | None = ...,
        *,
        raw_data: npt.NDArray[Any] | None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
        scale_mode: ScaleMode | None = ...,
    ) -> None: ...

    def __init__(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        raw_data: npt.NDArray[Any] | None = None,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> None:
        """Initialize a new complex waveform.

        Args:
            sample_count: The number of samples in the waveform.
            dtype: The NumPy data type for the waveform data. If not specified, the data
                type defaults to np.complex128.
            raw_data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A complex waveform.
        """
        return super().__init__(
            sample_count,
            dtype,
            raw_data=raw_data,
            start_index=start_index,
            capacity=capacity,
            extended_properties=extended_properties,
            copy_extended_properties=copy_extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    @override
    def _convert_data(
        self,
        dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled],
        raw_data: npt.NDArray[_TRaw],
    ) -> npt.NDArray[_TOtherScaled]:
        return convert_complex(dtype, raw_data)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/__init__.py sha256=a5d19937f9591a47bf9a91cb0ab2456e149b9f514aad1d665f91046a8de7583f bytes=591 -->
## FILE: src/nitypes/waveform/_digital/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/__init__.py`
- sha256: `a5d19937f9591a47bf9a91cb0ab2456e149b9f514aad1d665f91046a8de7583f`
- bytes: 591

````python
"""Digital waveform data types."""

from nitypes.waveform._digital._signal import DigitalWaveformSignal
from nitypes.waveform._digital._signal_collection import DigitalWaveformSignalCollection
from nitypes.waveform._digital._state import DigitalState
from nitypes.waveform._digital._waveform import (
    DigitalWaveform,
    DigitalWaveformFailure,
    DigitalWaveformTestResult,
)

__all__ = [
    "DigitalState",
    "DigitalWaveform",
    "DigitalWaveformFailure",
    "DigitalWaveformSignal",
    "DigitalWaveformSignalCollection",
    "DigitalWaveformTestResult",
]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/_port.py sha256=d0b5c6ea0e49b8bc31a2d3f988e9c22fa4f0190c33a9d0ac11aebec7c3970e2e bytes=5713 -->
## FILE: src/nitypes/waveform/_digital/_port.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/_port.py`
- sha256: `d0b5c6ea0e49b8bc31a2d3f988e9c22fa4f0190c33a9d0ac11aebec7c3970e2e`
- bytes: 5713

````python
from __future__ import annotations

import sys
from collections.abc import Sequence
from typing import Literal

import numpy as np
import numpy.typing as npt

from nitypes.waveform.typing import AnyDigitalPort


def bit_mask(n: int, /) -> int:
    """Return the bit mask with the lower n bits set.

    >>> bit_mask(0)
    0
    >>> bit_mask(4)
    15
    >>> bit_mask(9)
    511
    >>> bit_mask(32)
    4294967295
    >>> bit_mask(-1)
    Traceback (most recent call last):
    ...
    ValueError: The number of bits must be a non-negative integer.
    <BLANKLINE>
    Number of bits: -1
    """
    if n < 0:
        raise ValueError(
            "The number of bits must be a non-negative integer.\n\n" f"Number of bits: {n}"
        )
    return (1 << n) - 1


def get_port_dtype(mask: int | Sequence[int]) -> np.dtype[AnyDigitalPort]:
    """Return the NumPy port dtype for the given mask.

    >>> get_port_dtype(0xF)
    dtype('uint8')
    >>> get_port_dtype(0x100)
    dtype('uint16')
    >>> get_port_dtype(0xDEADBEEF)
    dtype('uint32')
    >>> get_port_dtype(0x1_0000_0000)
    Traceback (most recent call last):
    ...
    ValueError: The mask must be an unsigned 8-, 16-, or 32-bit integer.
    <BLANKLINE>
    Mask: 4294967296
    >>> get_port_dtype([0x0F, 0xF0])
    dtype('uint8')
    >>> get_port_dtype([0x100, 0x01])
    dtype('uint16')
    >>> get_port_dtype([0x01, 0x100])
    dtype('uint16')
    >>> get_port_dtype([0xDEADBEEF])
    dtype('uint32')
    """
    if isinstance(mask, Sequence):
        return max((_get_port_dtype(m) for m in mask), key=lambda d: d.itemsize)
    else:
        return _get_port_dtype(mask)


def _get_port_dtype(mask: int) -> np.dtype[AnyDigitalPort]:
    if (mask & 0xFF) == mask:
        return np.dtype(np.uint8)
    elif (mask & 0xFFFF) == mask:
        return np.dtype(np.uint16)
    elif (mask & 0xFFFFFFFF) == mask:
        return np.dtype(np.uint32)
    else:
        raise ValueError(
            "The mask must be an unsigned 8-, 16-, or 32-bit integer.\n\n" f"Mask: {mask}"
        )


def port_to_line_data(
    port_data: npt.NDArray[AnyDigitalPort], mask: int, bitorder: Literal["big", "little"] = "big"
) -> npt.NDArray[np.uint8]:
    """Convert a 1D array of port data to a 2D array of line data, using the specified mask.

    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0xFF)
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8)

    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0xFF, bitorder="little")
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x3)
    array([[0, 0],
           [0, 1],
           [1, 0],
           [1, 1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x3, bitorder="little")
    array([[0, 0],
           [1, 0],
           [0, 1],
           [1, 1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x2)
    array([[0],
           [0],
           [1],
           [1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0)
    array([], shape=(4, 0), dtype=uint8)
    >>> port_to_line_data(np.array([0x12000000,0xFE000000], np.uint32), 0xFF000000)
    array([[0, 0, 0, 1, 0, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1, 0]], dtype=uint8)
    """
    port_size = port_data.dtype.itemsize * 8
    # Convert to big-endian byte order to ensure MSB comes first when bitorder='big'
    # For multi-byte types on little-endian systems, we need to byteswap
    if bitorder != sys.byteorder and port_data.dtype.itemsize > 1:
        port_data = port_data.byteswap()

    line_data_1d = np.unpackbits(port_data.view(np.uint8), bitorder=bitorder)
    line_data_2d = line_data_1d.reshape(len(port_data), port_size)

    if mask == bit_mask(port_size):
        return line_data_2d
    else:
        return line_data_2d[:, _mask_to_column_indices(mask, port_size, bitorder)]


def _mask_to_column_indices(
    mask: int, port_size: int, bitorder: Literal["big", "little"], /
) -> list[int]:
    """Return the column indices for the given mask.

    >>> _mask_to_column_indices(0xF, 8, "big")
    [4, 5, 6, 7]
    >>> _mask_to_column_indices(0x100, 16, "big")
    [7]
    >>> _mask_to_column_indices(0xDEADBEEF, 32, "big")
    [0, 1, 3, 4, 5, 6, 8, 10, 12, 13, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30, 31]
    >>> _mask_to_column_indices(0xF, 8, "little")
    [0, 1, 2, 3]
    >>> _mask_to_column_indices(0x100, 16, "little")
    [8]
    >>> _mask_to_column_indices(0xDEADBEEF, 32, "little")
    [0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 18, 19, 21, 23, 25, 26, 27, 28, 30, 31]
    >>> _mask_to_column_indices(-1, 8, "little")
    Traceback (most recent call last):
    ...
    ValueError: The mask must be a non-negative integer.
    <BLANKLINE>
    Mask: -1
    """
    if mask < 0:
        raise ValueError("The mask must be a non-negative integer.\n\n" f"Mask: {mask}")
    column_indices = []
    bit_position = 0
    while mask != 0:
        if mask & 1:
            if bitorder == "big":
                column_indices.append(port_size - 1 - bit_position)
            else:  # little
                column_indices.append(bit_position)
        bit_position += 1
        mask >>= 1

    if bitorder == "big":
        column_indices.reverse()

    return column_indices
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/_signal.py sha256=7bc17eb826209bb06b622d16a5623ee85d4095bcedfc7786d9854f32113ec978 bytes=3899 -->
## FILE: src/nitypes/waveform/_digital/_signal.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/_signal.py`
- sha256: `7bc17eb826209bb06b622d16a5623ee85d4095bcedfc7786d9854f32113ec978`
- bytes: 3899

````python
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, SupportsIndex

import numpy as np
import numpy.typing as npt

from nitypes._arguments import arg_to_uint
from nitypes.waveform.typing import TDigitalState

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import DigitalWaveform
else:
    # DigitalWaveform is a circular import.
    pass


class DigitalWaveformSignal(Generic[TDigitalState]):
    """A signal of a digital waveform.

    To construct this object, use the :any:`DigitalWaveform.signals` property and index the returned
    collection, e.g. ``waveform.signals[0]`` or ``waveform.signals["Dev1/port0/line0"]``.
    """

    __slots__ = ["_owner", "_signal_index", "_column_index", "__weakref__"]

    _owner: DigitalWaveform[TDigitalState]
    _column_index: int
    _signal_index: int

    def __init__(
        self,
        owner: DigitalWaveform[TDigitalState],
        signal_index: SupportsIndex,
        column_index: SupportsIndex | None = None,
    ) -> None:
        """Initialize a new digital waveform signal."""
        if column_index is None:
            # when unpickling an old version, column_index may not be provided
            column_index = signal_index

        self._owner = owner
        self._signal_index = arg_to_uint("signal index", signal_index)
        self._column_index = arg_to_uint("column index", column_index)

    @property
    def owner(self) -> DigitalWaveform[TDigitalState]:
        """The waveform that owns this signal."""
        return self._owner

    @property
    def signal_index(self) -> int:
        """The signal's position in the DigitalWaveform.signals collection (0-based)."""
        return self._signal_index

    @property
    def column_index(self) -> int:
        """The signal's position in the DigitalWaveform.data array's second dimension (0-based).

        This index is used to access the signal's data within the waveform's data array:
        `waveform.data[:, column_index]`.

        Note: The column_index is reversed compared to the signal_index. column_index 0 (the
        leftmost column) corresponds to the highest signal_index and highest line number. The
        highest column_index (the rightmost column) corresponds to signal_index 0 and line 0. This
        matches industry conventions where line 0 is the LSB and appears as the rightmost bit.
        """
        return self._column_index

    @property
    def data(self) -> npt.NDArray[TDigitalState]:
        """The signal data, indexed by sample."""
        return self._owner.data[:, self._column_index]

    @property
    def name(self) -> str:
        """The signal name."""
        return self._owner._get_line_name(self._column_index)

    @name.setter
    def name(self, value: str) -> None:
        self._owner._set_line_name(self._column_index, value)

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        # Do not compare the index or name.
        return np.array_equal(self.data, value.data)

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._owner, self._signal_index, self._column_index)
        return (self.__class__, ctor_args)

    def __repr__(self) -> str:
        """Return repr(self)."""
        # This is not the same as the constructor arguments.
        args = []
        if self.name:
            args.append(f"name={self.name!r}")
        if self._owner._sample_count > 0:
            args.append(f"data={self.data!r}")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/_signal_collection.py sha256=eeea87ad53707ecb980ffccf30e1b2f3c11de4b322cbf8f0fad36fdb5fac3659 bytes=2887 -->
## FILE: src/nitypes/waveform/_digital/_signal_collection.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/_signal_collection.py`
- sha256: `eeea87ad53707ecb980ffccf30e1b2f3c11de4b322cbf8f0fad36fdb5fac3659`
- bytes: 2887

````python
from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Generic, overload

from nitypes._exceptions import invalid_arg_type
from nitypes.waveform.typing import TDigitalState

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import DigitalWaveform, DigitalWaveformSignal
else:
    # DigitalWaveform is a circular import.
    from nitypes.waveform._digital._signal import DigitalWaveformSignal


class DigitalWaveformSignalCollection(
    Generic[TDigitalState], Sequence[DigitalWaveformSignal[TDigitalState]]
):
    """A collection of digital waveform signals.

    To construct this object, use the :any:`DigitalWaveform.signals` property.
    """

    __slots__ = ["_owner", "_signals", "__weakref__"]

    _owner: DigitalWaveform[TDigitalState]
    _signals: list[DigitalWaveformSignal[TDigitalState] | None]

    def __init__(self, owner: DigitalWaveform[TDigitalState]) -> None:
        """Initialize a new DigitalWaveformSignalCollection."""
        self._owner = owner
        self._signals = [None] * owner.signal_count

    def __len__(self) -> int:
        """Return len(self)."""
        return len(self._signals)

    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: int | str
    ) -> DigitalWaveformSignal[TDigitalState]: ...
    @overload
    def __getitem__(  # noqa: D105 - missing docstring in magic method
        self, index: slice
    ) -> Sequence[DigitalWaveformSignal[TDigitalState]]: ...

    def __getitem__(
        self, index: int | str | slice
    ) -> DigitalWaveformSignal[TDigitalState] | Sequence[DigitalWaveformSignal[TDigitalState]]:
        """Get self[index]."""
        if isinstance(index, int):  # index is the signal index
            if index < 0:
                index += len(self._signals)
            value = self._signals[index]
            if value is None:
                column_index = self._owner._reverse_index(index)
                value = self._signals[index] = DigitalWaveformSignal(
                    self._owner, index, column_index
                )
            return value
        elif isinstance(index, str):  # index is the line name
            line_names = self._owner._get_line_names()
            try:
                column_index = line_names.index(index)
            except ValueError:
                raise IndexError(index)
            signal_index = self._owner._reverse_index(column_index)
            return self[signal_index]
        elif isinstance(index, slice):  # index is a slice of signal indices
            return [self[i] for i in range(*index.indices(len(self)))]
        else:
            raise invalid_arg_type("index", "int or str", index)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/_state.py sha256=613c2ea1e680419a1f0b5d506c6804afdf2c1bd29379c62de392dcf6fd6870a5 bytes=3845 -->
## FILE: src/nitypes/waveform/_digital/_state.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/_state.py`
- sha256: `613c2ea1e680419a1f0b5d506c6804afdf2c1bd29379c62de392dcf6fd6870a5`
- bytes: 3845

````python
from __future__ import annotations

from enum import IntEnum

from nitypes._exceptions import invalid_arg_value

_CHAR_TABLE = "01ZLHXTV"

_STATE_TEST_TABLE = [
    # 0  1  Z  L  H  X  T  V
    [1, 0, 0, 1, 0, 1, 0, 1],  # 0
    [0, 1, 0, 0, 1, 1, 0, 1],  # 1
    [0, 0, 1, 0, 0, 1, 1, 0],  # Z
    [1, 0, 0, 1, 0, 1, 0, 0],  # L
    [0, 1, 0, 0, 1, 1, 0, 0],  # H
    [1, 1, 1, 1, 1, 1, 1, 1],  # X
    [0, 0, 1, 0, 0, 1, 1, 0],  # T
    [1, 1, 0, 0, 0, 1, 0, 1],  # V
]


class DigitalState(IntEnum):
    """An IntEnum of the different digital states that a digital signal can represent.

    You can use :class:`DigitalState` in place of an :any:`int`:

    >>> DigitalState.FORCE_OFF
    <DigitalState.FORCE_OFF: 2>
    >>> DigitalState.FORCE_OFF == 2
    True

    Use :meth:`from_char` and :meth:`to_char` to convert between states and characters:

    >>> DigitalState.from_char("Z")
    <DigitalState.FORCE_OFF: 2>
    >>> DigitalState.to_char(2)
    'Z'

    Use :meth:`test` to compare actual vs. expected states, returning True on failure.

    >>> DigitalState.test(DigitalState.FORCE_DOWN, DigitalState.COMPARE_LOW)
    False
    >>> DigitalState.test(DigitalState.FORCE_UP, DigitalState.COMPARE_LOW)
    True
    """

    _value_: int

    FORCE_DOWN = 0
    """Force logic low (``0``). Drive to the low voltage level (VIL)."""

    FORCE_UP = 1
    """Force logic high (``1``). Drive to the high voltage level (VIH)."""

    FORCE_OFF = 2
    """Force logic high impedance (``Z``). Turn the driver off."""

    COMPARE_LOW = 3
    """Compare logic low (edge) (``L``). Compare for a voltage level lower than the low voltage
    threshold (VOL)."""

    COMPARE_HIGH = 4
    """Compare logic high (edge) (``H``). Compare for a voltage level higher than the high voltage
    threshold (VOH)."""

    COMPARE_UNKNOWN = 5
    """Compare logic unknown (``X``). Don't compare."""

    COMPARE_OFF = 6
    """Compare logic high impedance (edge) (``T``). Compare for a voltage level between the low
    voltage threshold (VOL) and the high voltage threshold (VOH)."""

    COMPARE_VALID = 7
    """Compare logic valid level (edge) (``V``). Compare for a voltage level either lower than the
    low voltage threshold (VOL) or higher than the high voltage threshold (VOH)."""

    @property
    def char(self) -> str:
        """The character representing the digital state."""
        return _CHAR_TABLE[self]

    @classmethod
    def from_char(cls, char: str) -> DigitalState:
        """Look up the digital state for the corresponding character."""
        try:
            return DigitalState(_CHAR_TABLE.index(char))
        except ValueError:
            raise KeyError(char)

    @classmethod
    def to_char(cls, state: DigitalState, errors: str = "strict") -> str:
        """Get a character representing the digital state.

        Args:
            state: The digital state.
            errors: Specifies how to handle errors.

                * "strict": raise ``KeyError``
                * "replace": return "?"

        Returns:
            A character representing the digital state.
        """
        if errors not in ("strict", "replace"):
            raise invalid_arg_value("errors argument", "supported value", errors)
        try:
            return DigitalState(state).char
        except ValueError:
            if errors == "strict":
                raise KeyError(state)
            elif errors == "replace":
                return "?"
            raise

    @staticmethod
    def test(state1: DigitalState, state2: DigitalState) -> bool:
        """Test two digital states and return True if the test failed."""
        return not _STATE_TEST_TABLE[DigitalState(state1)][DigitalState(state2)]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_digital/_waveform.py sha256=ecd185d31dd531d323bd936b9e6163b2a477b96534f84757e80975586bc5b4d8 bytes=61388 -->
## FILE: src/nitypes/waveform/_digital/_waveform.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_digital/_waveform.py`
- sha256: `ecd185d31dd531d323bd936b9e6163b2a477b96534f84757e80975586bc5b4d8`
- bytes: 61388

````python
from __future__ import annotations

import datetime as dt
import sys
import weakref
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, Literal, SupportsIndex, overload

import hightime as ht
import numpy as np
import numpy.typing as npt
from typing_extensions import Self

from nitypes._arguments import arg_to_uint, validate_dtype, validate_unsupported_arg
from nitypes._exceptions import invalid_arg_type, invalid_array_ndim
from nitypes._numpy import asarray as _np_asarray
from nitypes.time.typing import AnyDateTime, AnyTimeDelta
from nitypes.waveform._digital._port import bit_mask, get_port_dtype, port_to_line_data
from nitypes.waveform._exceptions import (
    create_capacity_mismatch_error,
    create_capacity_too_small_error,
    create_datatype_mismatch_error,
    create_irregular_timestamp_count_mismatch_error,
    create_signal_count_mismatch_error,
    create_start_index_or_sample_count_too_large_error,
    create_start_index_too_large_error,
)
from nitypes.waveform._extended_properties import CHANNEL_NAME, LINE_NAMES
from nitypes.waveform._types import DIGITAL_PORT_DTYPES, DIGITAL_STATE_DTYPES
from nitypes.waveform.typing import (
    ExtendedPropertyValue,
    TDigitalState,
    TOtherDigitalState,
)

if sys.version_info < (3, 10):
    import array as std_array

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import (
        DigitalState,
        DigitalWaveformSignalCollection,
        ExtendedPropertyDictionary,
        Timing,
    )
else:
    from nitypes.waveform._digital._signal_collection import (
        DigitalWaveformSignalCollection,
    )
    from nitypes.waveform._digital._state import DigitalState
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary
    from nitypes.waveform._timing import Timing


@dataclass(frozen=True)
class DigitalWaveformFailure:
    """A test failure, indicating where the actual waveform did not match the expected waveform."""

    sample_index: int
    """The sample index into the compared waveform where the test failure occurred."""

    expected_sample_index: int
    """The sample index into the expected waveform where the test failure occurred."""

    signal_index: int
    """The signal index where the test failure occurred."""

    actual_state: DigitalState
    """The state from the compared waveform where the test failure occurred."""

    expected_state: DigitalState
    """The state from the expected waveform where the test failure occurred."""


@dataclass(frozen=True)
class DigitalWaveformTestResult:
    """A test result from comparing a digital waveform against an expected digital waveform."""

    @property
    def success(self) -> bool:
        """True if the test is successful, False if the test failed."""
        return len(self.failures) == 0

    failures: Sequence[DigitalWaveformFailure]
    """A collection of test failure information."""


class DigitalWaveform(Generic[TDigitalState]):
    """A digital waveform, which encapsulates digital data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct a digital waveform, use the :class:`DigitalWaveform` class:

    >>> DigitalWaveform()
    nitypes.waveform.DigitalWaveform(0, 1)
    >>> DigitalWaveform(sample_count=5, signal_count=3)  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.DigitalWaveform(5, 3, data=array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
    [0, 0, 0]], dtype=uint8))

    When displaying a digital waveform as a string, the first number is the sample count and the second
    number is the signal count.

    To construct a digital waveform from a NumPy array of line data, use the
    :any:`DigitalWaveform.from_lines` method. Each array element represents a digital state, such as 1
    for "on" or 0 for "off". The line data should be in a 1D array indexed by sample or a 2D array
    indexed by (sample, signal). *(Note, signal indices are reversed! See "Signal index vs. column index"
    below for details.)* The digital waveform displays the line data as a 2D array.

    >>> import numpy as np
    >>> DigitalWaveform.from_lines(np.array([0, 1, 0], np.uint8))
    nitypes.waveform.DigitalWaveform(3, 1, data=array([[0], [1], [0]], dtype=uint8))
    >>> DigitalWaveform.from_lines(np.array([[0, 0], [1, 0], [0, 1], [1, 1]], np.uint8))
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=uint8))

    You can also use :any:`DigitalWaveform.from_lines` to construct a digital waveform from a sequence,
    such as a list.

    >>> DigitalWaveform.from_lines([[0, 0], [1, 0], [0, 1], [1, 1]])
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=uint8))

    To construct a digital waveform from a NumPy array of port data, use the
    :any:`DigitalWaveform.from_port` method. Each element of the port data array represents a digital
    sample taken over a port of signals. Each bit in the sample is a signal value, either 1 for "on" or
    0 for "off". *(Note, signal indices are reversed! See "Signal index vs. column index" below for
    details.)*

    >>> DigitalWaveform.from_port(np.array([0, 1, 2, 3], np.uint8))  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.DigitalWaveform(4, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8))

    You can use a mask to specify which lines in the port to include in the waveform.

    >>> DigitalWaveform.from_port(np.array([0, 1, 2, 3], np.uint8), 0x3)
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8))

    You can also use a non-NumPy sequence such as a list, but you must specify a mask so the waveform
    knows how many bits are in each list element.

    >>> DigitalWaveform.from_port([0, 1, 2, 3], 0x3)
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8))

    The 2D version, :any:`DigitalWaveform.from_ports`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[0, 1, 2, 3], [3, 0, 3, 0]]
    >>> DigitalWaveform.from_ports(nested_list, [0x3, 0x3])  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8)),
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[1, 1], [0, 0], [1, 1], [0, 0]], dtype=uint8))]

    Digital signals
    ^^^^^^^^^^^^^^^

    You can access individual signals using the :any:`DigitalWaveform.signals` property.

    >>> wfm = DigitalWaveform.from_port([0, 1, 2, 3], 0x3)
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(data=array([0, 1, 0, 1], dtype=uint8))
    >>> wfm.signals[1]
    nitypes.waveform.DigitalWaveformSignal(data=array([0, 0, 1, 1], dtype=uint8))

    The :any:`DigitalWaveformSignal.data` property returns a view of the data for that signal.

    >>> wfm.signals[0].data
    array([0, 1, 0, 1], dtype=uint8)

    Signal index vs. column index
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Each :class:`DigitalWaveformSignal` has two index properties:

    * :attr:`DigitalWaveformSignal.signal_index` - The position in the :attr:`DigitalWaveform.signals`
      collection (0-based from the first signal). signal_index 0 is the rightmost column in the data.
    * :attr:`DigitalWaveformSignal.column_index` - The column in the :attr:`DigitalWaveform.data`
      array, e.g. `waveform.data[:, column_index]`. column_index 0 is the leftmost column in the data.

    These indices are reversed with respect to each other. signal_index 0 (line 0) corresponds to
    the highest column_index, and the highest signal_index (the highest line) corresponds to
    column_index 0. This ordering follows industry conventions where line 0 is the least
    significant bit and appears last (in the rightmost column) of the data array.

    >>> wfm = DigitalWaveform.from_port([0, 1, 2, 3], 0x7)  # 3 signals
    >>> wfm.data
    array([[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 1, 1]], dtype=uint8)
    >>> wfm.signals[0].signal_index
    0
    >>> wfm.signals[0].column_index
    2
    >>> wfm.signals[0].data
    array([0, 1, 0, 1], dtype=uint8)
    >>> wfm.signals[2].signal_index
    2
    >>> wfm.signals[2].column_index
    0
    >>> wfm.signals[2].data
    array([0, 0, 0, 0], dtype=uint8)

    Digital signal names
    ^^^^^^^^^^^^^^^^^^^^

    The :any:`DigitalWaveformSignal.name` property allows you to get and set the signal names.

    >>> wfm.signals[0].name = "port0/line0"
    >>> wfm.signals[1].name = "port0/line1"
    >>> wfm.signals[2].name = "port0/line2"
    >>> wfm.signals[0].name
    'port0/line0'
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(name='port0/line0', data=array([0, 1, 0, 1], dtype=uint8))

    The signal names are stored in the ``NI_LineNames`` extended property on the digital waveform.
    Note that the order of the names in the string follows column_index order (highest line number
    first), which is reversed compared to signal_index order (lowest line first). This means line 0
    (signal_index 0) appears last in the NI_LineNames string. This matches industry conventions
    where line 0 appears in the rightmost column of the data array.

    >>> wfm.extended_properties["NI_LineNames"]
    'port0/line2, port0/line1, port0/line0'

    When creating a digital waveform, you can directly set the ``NI_LineNames`` extended property.

    >>> wfm = DigitalWaveform.from_port([2, 4], 0x7,
    ... extended_properties={"NI_LineNames": "Dev1/port1/line6, Dev1/port1/line5, Dev1/port1/line4"})
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line4', data=array([0, 0], dtype=uint8))
    >>> wfm.signals[1]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line5', data=array([1, 0], dtype=uint8))
    >>> wfm.signals[2]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line6', data=array([0, 1], dtype=uint8))

    Digital state types
    ^^^^^^^^^^^^^^^^^^^

    By default, digital waveforms use a NumPy ``dtype`` of :any:`numpy.uint8`, which uses a byte of
    memory for each digital state.

    Using ``np.uint8`` allows the waveform to contain digital states other than "on" or off", such as
    such as :any:`DigitalState.FORCE_OFF` (``X``) or :any:`DigitalState.COMPARE_HIGH` (``H``). This
    capability is used for digital pattern applications.

    You can also construct a digital waveform using a NumPy ``dtype`` of :any:`numpy.bool`. This also
    uses a byte of memory for each digital state, but it restricts the states to "on" and "off".

    Testing digital waveforms
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    You can use :meth:`DigitalWaveform.test` to compare an acquired waveform against an expected
    waveform. This returns a :class:`DigitalWaveformTestResult` object, which has a Boolean ``success``
    property and a ``failures`` property containing a collection of :class:`DigitalWaveformFailure`
    objects, which indicate the location of each test failure.

    Here is an example. The expected waveform counts in binary using ``COMPARE_LOW`` (``L``) and
    ``COMPARE_HIGH`` (``H``), but signal 0 of the actual waveform is stuck high.

    >>> actual = DigitalWaveform.from_lines([[0, 1], [1, 1], [0, 1], [1, 1]])
    >>> expected = DigitalWaveform.from_lines([[DigitalState.COMPARE_LOW, DigitalState.COMPARE_LOW],
    ... [DigitalState.COMPARE_HIGH, DigitalState.COMPARE_LOW],
    ... [DigitalState.COMPARE_LOW, DigitalState.COMPARE_HIGH],
    ... [DigitalState.COMPARE_HIGH, DigitalState.COMPARE_HIGH]])
    >>> result = actual.test(expected)
    >>> result.success
    False
    >>> len(result.failures)
    2

    The failures indicate the sample indices into the actual and expected waveforms, the signal index,
    and the digital state from the actual and expected waveforms:

    >>> result.failures[0]  # doctest: +NORMALIZE_WHITESPACE
    DigitalWaveformFailure(sample_index=0, expected_sample_index=0, signal_index=0,
    actual_state=<DigitalState.FORCE_UP: 1>, expected_state=<DigitalState.COMPARE_LOW: 3>)
    >>> result.failures[1]  # doctest: +NORMALIZE_WHITESPACE
    DigitalWaveformFailure(sample_index=1, expected_sample_index=1, signal_index=0,
    actual_state=<DigitalState.FORCE_UP: 1>, expected_state=<DigitalState.COMPARE_LOW: 3>)

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Digital waveforms have the same timing information as analog waveforms.

    Class members
    ^^^^^^^^^^^^^
    """  # noqa: W505 - doc line too long

    @overload
    @classmethod
    def from_lines(
        cls,
        array: npt.NDArray[TOtherDigitalState],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[TOtherDigitalState]: ...

    @overload
    @classmethod
    def from_lines(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[TOtherDigitalState]: ...

    @overload
    @classmethod
    def from_lines(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[Any]: ...

    @classmethod
    def from_lines(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        signal_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
    ) -> DigitalWaveform[Any]:
        """Construct a waveform from a one or two-dimensional array or sequence of line data.

        Each element of the line data array represents a digital state, such as 1 for "on" or 0
        for "off". The line data should be in a 1D array indexed by sample or a 2D array indexed
        by (sample, signal). The line data may also use digital state values from the
        :class:`DigitalState` enum.

        Note that signal indices are reversed with respect to this array's column indices.
        The first column in each sample corresponds to the highest line number and highest signal
        index. The last column in each sample corresponds to line 0 and signal index 0.

        Args:
            array: The line data as a one or two-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            signal_count: The number of signals in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        """
        if isinstance(array, np.ndarray):
            if array.ndim not in (1, 2):
                raise invalid_array_ndim(
                    "input array", "one or two-dimensional array or sequence", array.ndim
                )
            if dtype is not None and array.dtype != dtype:
                raise create_datatype_mismatch_error("input array", array.dtype, "requested", dtype)
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            if dtype is None:
                dtype = np.uint8
        else:
            raise invalid_arg_type("input array", "one or two-dimensional array or sequence", array)

        return cls(
            data=_np_asarray(array, dtype, copy=copy),
            start_index=start_index,
            sample_count=sample_count,
            signal_count=signal_count,
            extended_properties=extended_properties,
            timing=timing,
        )

    @overload
    @classmethod
    def from_port(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        mask: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[np.uint8]: ...

    @overload
    @classmethod
    def from_port(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        mask: SupportsIndex | None = ...,
        dtype: (
            type[TOtherDigitalState]  # pyright: ignore[reportInvalidTypeVarUse]
            | np.dtype[TOtherDigitalState]
        ) = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[TOtherDigitalState]: ...

    @overload
    @classmethod
    def from_port(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        mask: SupportsIndex | None = ...,
        dtype: npt.DTypeLike | None = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> DigitalWaveform[Any]: ...

    @classmethod
    def from_port(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        mask: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        bitorder: Literal["big", "little"] = "big",
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
    ) -> DigitalWaveform[Any]:
        """Construct a waveform from a one-dimensional array or sequence of port data.

        This method allocates a new array in order to convert the port data (integers) to line data
        (bits).

        Each element of the port data array represents a digital sample taken over a port of
        signals. Each bit in the sample represents a digital state, either 1 for "on" or 0 for
        "off".

        When bitorder='big' (default), the integers in the samples are big-endian. The most
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The least significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        When bitorder='little', the integers in the samples are little-endian. The least
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The most significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        If the input array is not a NumPy array, you must specify the mask.

        Args:
            array: The port data as a one-dimensional array or a sequence.
            mask: A bitmask specifying which lines to include in the waveform.
            dtype: The NumPy data type for the waveform (line) data.
            bitorder: The bit ordering to use when unpacking port data ('big' or 'little').
                Defaults to 'big'.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 1:
                raise invalid_array_ndim(
                    "input array", "one-dimensional array or sequence", array.ndim
                )
            validate_dtype(array.dtype, DIGITAL_PORT_DTYPES)
            default_mask = bit_mask(array.dtype.itemsize * 8)
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            # np.array([0,1]).dtype is np.int64 by default, so the user must specify the port size.
            if mask is None:
                raise ValueError(
                    "You must specify a mask when the input array is not a NumPy array."
                )
            default_mask = 0
        else:
            raise invalid_arg_type("input array", "one or two-dimensional array or sequence", array)

        if dtype is None:
            dtype = np.uint8
        validate_dtype(dtype, DIGITAL_STATE_DTYPES)

        mask = arg_to_uint("mask", mask, default_mask)

        if isinstance(array, np.ndarray):
            port_dtype = array.dtype
        else:
            port_dtype = get_port_dtype(mask)

        port_data = _np_asarray(array, port_dtype)
        line_data = port_to_line_data(port_data, mask, bitorder)
        if line_data.dtype != dtype:
            line_data = line_data.view(dtype)

        return cls(
            data=line_data,
            dtype=dtype,
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
        )

    @overload
    @classmethod
    def from_ports(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        masks: Sequence[SupportsIndex] | None = ...,
        dtype: None = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> Sequence[DigitalWaveform[np.uint8]]: ...

    @overload
    @classmethod
    def from_ports(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        masks: Sequence[SupportsIndex] | None = ...,
        dtype: (
            type[TOtherDigitalState]  # pyright: ignore[reportInvalidTypeVarUse]
            | np.dtype[TOtherDigitalState]
        ) = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> Sequence[DigitalWaveform[TOtherDigitalState]]: ...

    @overload
    @classmethod
    def from_ports(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        masks: Sequence[SupportsIndex] | None = ...,
        dtype: npt.DTypeLike | None = ...,
        *,
        bitorder: Literal["big", "little"] = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> Sequence[DigitalWaveform[Any]]: ...

    @classmethod
    def from_ports(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        masks: Sequence[SupportsIndex] | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        bitorder: Literal["big", "little"] = "big",
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
    ) -> Sequence[DigitalWaveform[Any]]:
        """Construct a waveform from a two-dimensional array or sequence of port data.

        This method allocates a new array in order to convert the port data to line data.

        Each row of the port data array corresponds to a resulting DigitalWaveform. Each element of
        the port data array represents a digital sample taken over a port of signals. Each bit in
        the sample represents a digital state, either 1 for "on" or 0 for "off".

        When bitorder='big' (default), the integers in the samples are big-endian. The most
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The least significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        When bitorder='little', the integers in the samples are little-endian. The least
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The most significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        If the input array is not a NumPy array, you must specify the masks.

        Args:
            array: The port data as a two-dimensional array or a sequence.
            masks: A sequence of bitmasks specifying which lines from each port to include in the
                corresponding waveform.
            dtype: The NumPy data type for the waveform (line) data.
            bitorder: The bit ordering to use when unpacking port data ('big' or 'little').
                Defaults to 'big'.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 2:
                raise invalid_array_ndim(
                    "input array", "two-dimensional array or sequence", array.ndim
                )
            validate_dtype(array.dtype, DIGITAL_PORT_DTYPES)
            default_masks = [bit_mask(array.dtype.itemsize * 8)] * array.shape[0]
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            # np.array([0,1]).dtype is np.int64 by default, so the user must specify the port size.
            if masks is None:
                raise ValueError(
                    "You must specify the masks when the input array is not a NumPy array."
                )
            default_masks = []
        else:
            raise invalid_arg_type("input array", "one or two-dimensional array or sequence", array)

        if dtype is None:
            dtype = np.uint8
        validate_dtype(dtype, DIGITAL_STATE_DTYPES)

        if not isinstance(masks, (type(None), Sequence)):
            raise invalid_arg_type("masks", "sequence of ints")
        if masks is not None:
            validated_masks = [arg_to_uint("mask", mask) for mask in masks]
        else:
            validated_masks = default_masks

        if isinstance(array, np.ndarray):
            port_dtype = array.dtype
        else:
            port_dtype = get_port_dtype(validated_masks)

        port_data = _np_asarray(array, port_dtype)
        waveforms = []
        for port_index in range(port_data.shape[0]):
            line_data = port_to_line_data(
                port_data[port_index, :], validated_masks[port_index], bitorder
            )
            if line_data.dtype != dtype:
                line_data = line_data.view(dtype)

            waveforms.append(
                cls(
                    data=line_data,
                    dtype=dtype,
                    start_index=start_index,
                    sample_count=sample_count,
                    extended_properties=extended_properties,
                    timing=timing,
                )
            )
        return waveforms

    __slots__ = [
        "_data",
        "_data_1d",
        "_start_index",
        "_sample_count",
        "_extended_properties",
        "_timing",
        "_signals",
        "_line_names",
        "__weakref__",
    ]

    _data: npt.NDArray[TDigitalState]
    _data_1d: npt.NDArray[TDigitalState] | None
    _start_index: int
    _sample_count: int
    _extended_properties: ExtendedPropertyDictionary
    _timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]
    _signals: DigitalWaveformSignalCollection[TDigitalState] | None
    _line_names: list[str] | None

    # If neither dtype nor data is specified, _TData defaults to np.uint8.
    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: DigitalWaveform[np.uint8],
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        dtype: None = ...,
        default_value: bool | int | DigitalState | None = ...,
        *,
        data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: DigitalWaveform[TOtherDigitalState],
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState] = ...,
        default_value: bool | int | DigitalState | None = ...,
        *,
        data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: DigitalWaveform[TOtherDigitalState],
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        dtype: None = ...,
        default_value: bool | int | DigitalState | None = ...,
        *,
        data: npt.NDArray[TOtherDigitalState] = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: DigitalWaveform[Any],
        sample_count: SupportsIndex | None = ...,
        signal_count: SupportsIndex | None = ...,
        dtype: npt.DTypeLike | None = ...,
        default_value: bool | int | DigitalState | None = ...,
        *,
        data: npt.NDArray[Any] | None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = ...,
    ) -> None: ...

    def __init__(
        self,
        sample_count: SupportsIndex | None = None,
        signal_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        default_value: bool | int | DigitalState | None = None,
        *,
        data: npt.NDArray[Any] | None = None,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
    ) -> None:
        """Initialize a new digital waveform.

        Args:
            sample_count: The number of samples in the waveform.
            signal_count: The number of signals in the waveform.
            dtype: The NumPy data type for the waveform data.
            default_value: The :class:`DigitalState` to initialize the waveform with.
            data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.

        Returns:
            A digital waveform.
        """
        if data is None:
            self._init_with_new_array(
                sample_count,
                signal_count,
                dtype,
                default_value,
                start_index=start_index,
                capacity=capacity,
            )
        elif isinstance(data, np.ndarray):
            self._init_with_provided_array(
                data,
                dtype,
                start_index=start_index,
                sample_count=sample_count,
                signal_count=signal_count,
                capacity=capacity,
            )
        else:
            raise invalid_arg_type("raw data", "NumPy ndarray", data)

        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties
        if not hasattr(self._extended_properties, "_on_key_changed"):
            # when unpickling an old version, _on_key_changed may not exist
            self._extended_properties._on_key_changed = []
        self._extended_properties._on_key_changed.append(
            weakref.WeakMethod(self._on_extended_property_changed)
        )

        if timing is None:
            timing = Timing.empty
        self._timing = timing

        self._signals = None
        self._line_names = None

    def _on_extended_property_changed(self, key: str) -> None:
        if key == LINE_NAMES:
            self._line_names = None

    def _init_with_new_array(
        self,
        sample_count: SupportsIndex | None = None,
        signal_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        default_value: bool | int | DigitalState | None = None,
        *,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, 0)
        signal_count = arg_to_uint("signal count", signal_count, 1)
        capacity = arg_to_uint("capacity", capacity, sample_count)

        if dtype is None:
            dtype = np.uint8
        validate_dtype(dtype, DIGITAL_STATE_DTYPES)

        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "capacity", capacity)
        if start_index + sample_count > capacity:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "capacity", capacity
            )

        if default_value is None:
            default_value = 0
        elif not isinstance(default_value, (bool, int, DigitalState)):
            raise invalid_arg_type("default value", "bool, int, or DigitalState", default_value)

        self._data = np.full((capacity, signal_count), default_value, dtype)
        self._data_1d = None
        self._start_index = start_index
        self._sample_count = sample_count

    def _init_with_provided_array(
        self,
        data: npt.NDArray[TDigitalState],
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = None,
        sample_count: SupportsIndex | None = None,
        signal_count: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        if not isinstance(data, np.ndarray):
            raise invalid_arg_type("input array", "one or two-dimensional array", data)

        if dtype is None:
            dtype = data.dtype
        if dtype != data.dtype:
            raise create_datatype_mismatch_error(
                "input array", data.dtype, "requested", np.dtype(dtype)
            )
        validate_dtype(dtype, DIGITAL_STATE_DTYPES)

        if data.ndim == 1:
            data_signal_count = 1
            data_1d = data
            data = data.reshape(len(data), 1)
        elif data.ndim == 2:
            data_signal_count = data.shape[1]
            data_1d = None
        else:
            raise invalid_array_ndim("input array", "one or two-dimensional array", data.ndim)

        capacity = arg_to_uint("capacity", capacity, len(data))
        if capacity != len(data):
            raise create_capacity_mismatch_error(capacity, len(data))

        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "input array length", capacity)

        sample_count = arg_to_uint("sample count", sample_count, len(data) - start_index)
        if start_index + sample_count > len(data):
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "input array length", len(data)
            )

        signal_count = arg_to_uint("signal count", signal_count, data_signal_count)
        if signal_count != data_signal_count:
            raise create_signal_count_mismatch_error(
                "provided", signal_count, "array", data_signal_count
            )

        self._data = data
        self._data_1d = data_1d
        self._start_index = start_index
        self._sample_count = sample_count

    @property
    def signals(self) -> DigitalWaveformSignalCollection[TDigitalState]:
        """A collection of objects representing waveform signals."""
        # Lazily allocate self._signals if the application needs it.
        #
        # https://github.com/ni/nitypes-python/issues/131 - DigitalWaveform.signals introduces a
        # reference cycle, which affects GC overhead.
        value = self._signals
        if value is None:
            value = self._signals = DigitalWaveformSignalCollection(self)
        return value

    @property
    def data(self) -> npt.NDArray[TDigitalState]:
        """The waveform data, indexed by (sample, signal)."""
        return self._data[self._start_index : self._start_index + self._sample_count]

    def get_data(
        self, start_index: SupportsIndex | None = 0, sample_count: SupportsIndex | None = None
    ) -> npt.NDArray[TDigitalState]:
        """Get a subset of the waveform data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the raw waveform data.
        """
        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > self.sample_count:
            raise create_start_index_too_large_error(
                start_index, "number of samples in the waveform", self.sample_count
            )

        sample_count = arg_to_uint("sample count", sample_count, self.sample_count - start_index)
        if start_index + sample_count > self.sample_count:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "number of samples in the waveform", self.sample_count
            )

        return self.data[start_index : start_index + sample_count]

    @property
    def sample_count(self) -> int:
        """The number of samples in the waveform."""
        return self._sample_count

    @sample_count.setter
    def sample_count(self, value: int) -> None:
        """Set the number of samples in the waveform."""
        value = arg_to_uint("sample count", value)
        if self._start_index + value > self.capacity:
            raise create_start_index_or_sample_count_too_large_error(
                self._start_index, value, "capacity", self.capacity
            )
        self._sample_count = value

    @property
    def signal_count(self) -> int:
        """The number of signals in the waveform."""
        # npt.NDArray[_ScalarT] currently has a shape type of _AnyShape, which is tuple[Any, ...]
        shape: tuple[int, ...] = self._data.shape
        return shape[1]

    @property
    def start_index(self) -> int:
        """The sample index of the underlying array at which the waveform data begins."""
        return self._start_index

    @property
    def capacity(self) -> int:
        """The total capacity available for waveform data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        """
        return len(self._data)

    @capacity.setter
    def capacity(self, value: int) -> None:
        value = arg_to_uint("capacity", value)
        min_capacity = self._start_index + self._sample_count
        if value < min_capacity:
            raise create_capacity_too_small_error(value, min_capacity, "waveform")
        if value != len(self._data):
            if self._data_1d is not None:
                # If _data is a 2D view of a 1D array, resize the base array and recreate the view.
                self._data_1d.resize(value, refcheck=False)
                self._data = self._data_1d.reshape(len(self._data_1d), 1)
            else:
                self._data.resize((value, self.signal_count), refcheck=False)

    @property
    def dtype(self) -> np.dtype[TDigitalState]:
        """The NumPy dtype for the waveform data."""
        return self._data.dtype

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the waveform."""
        return self._extended_properties

    @property
    def channel_name(self) -> str:
        """The name of the device channel from which the waveform was acquired."""
        value = self._extended_properties.get(CHANNEL_NAME, "")
        assert isinstance(value, str)
        return value

    @channel_name.setter
    def channel_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("channel name", "str", value)
        self._extended_properties[CHANNEL_NAME] = value

    def _get_line_names(self) -> list[str]:
        # Lazily allocate self._line_names if the application needs it.
        line_names = self._line_names
        if line_names is None:
            line_names_str = self._extended_properties.get(LINE_NAMES, "")
            assert isinstance(line_names_str, str)
            line_names = self._line_names = [name.strip() for name in line_names_str.split(",")]
            if len(line_names) < self.signal_count:
                line_names.extend([""] * (self.signal_count - len(line_names)))
        return line_names

    def _get_line_name(self, column_index: int) -> str:
        return self._get_line_names()[column_index]

    def _set_line_name(self, column_index: int, value: str) -> None:
        line_names = self._get_line_names()
        line_names[column_index] = value
        self._extended_properties[LINE_NAMES] = ", ".join(line_names)

    def _set_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if self._timing is not value:
            self._timing = value

    def _validate_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if value._timestamps is not None and len(value._timestamps) != self._sample_count:
            raise create_irregular_timestamp_count_mismatch_error(
                len(value._timestamps), "number of samples in the waveform", self._sample_count
            )

    @property
    def timing(self) -> Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]:
        """The timing information of the waveform.

        The default value is Timing.empty.
        """
        return self._timing

    @timing.setter
    def timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if not isinstance(value, Timing):
            raise invalid_arg_type("timing information", "Timing object", value)
        self._validate_timing(value)
        self._set_timing(value)

    def append(
        self,
        other: (
            npt.NDArray[TDigitalState]
            | DigitalWaveform[TDigitalState]
            | Sequence[DigitalWaveform[TDigitalState]]
        ),
        /,
        timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None = None,
    ) -> None:
        """Append data to the waveform.

        Args:
            other: The array or waveform(s) to append.
            timestamps: A sequence of timestamps. When the current waveform has
                SampleIntervalMode.IRREGULAR, you must provide a sequence of timestamps with the
                same length as the array.

        Raises:
            TimingMismatchError: The current and other waveforms have incompatible timing.
            TimingMismatchWarning: The sample intervals of the waveform(s) do not match.
            ValueError: The other array has the wrong number of dimensions or the length of the
                timestamps argument does not match the length of the other array.
            TypeError: The data types of the current waveform and other array or waveform(s) do not
                match, or an argument has the wrong data type.

        When appending waveforms:

        * Timing information is merged based on the sample interval mode of the current
          waveform:

          * SampleIntervalMode.NONE or SampleIntervalMode.REGULAR: The other waveform(s) must also
            have SampleIntervalMode.NONE or SampleIntervalMode.REGULAR. If the sample interval does
            not match, a TimingMismatchWarning is generated. Otherwise, the timing information of
            the other waveform(s) is discarded.

          * SampleIntervalMode.IRREGULAR: The other waveforms(s) must also have
            SampleIntervalMode.IRREGULAR. The timestamps of the other waveforms(s) are appended to
            the current waveform's timing information.

        * Extended properties of the other waveform(s) are merged into the current waveform if they
          are not already set in the current waveform.
        """
        if isinstance(other, np.ndarray):
            self._append_array(other, timestamps)
        elif isinstance(other, DigitalWaveform):
            validate_unsupported_arg("timestamps", timestamps)
            self._append_waveform(other)
        elif isinstance(other, Sequence) and all(isinstance(x, DigitalWaveform) for x in other):
            validate_unsupported_arg("timestamps", timestamps)
            self._append_waveforms(other)
        else:
            raise invalid_arg_type("input", "array or waveform(s)", other)

    def _append_array(
        self,
        array: npt.NDArray[TDigitalState],
        timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None = None,
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "waveform", self.dtype)

        if array.ndim == 1:
            array_signal_count = 1
            array = array.reshape(len(array), 1)
        elif array.ndim == 2:
            array_signal_count = array.shape[1]
        else:
            raise invalid_array_ndim("input array", "one or two-dimensional array", array.ndim)

        if array_signal_count != self.signal_count:
            raise create_signal_count_mismatch_error(
                "input array", array_signal_count, "waveform", self.signal_count
            )

        if timestamps is not None and len(array) != len(timestamps):
            raise create_irregular_timestamp_count_mismatch_error(
                len(timestamps), "input array length", len(array)
            )

        new_timing = self._timing._append_timestamps(timestamps)

        self._increase_capacity(len(array))
        self._set_timing(new_timing)

        offset = self._start_index + self._sample_count
        self._data[offset : offset + len(array)] = array
        self._sample_count += len(array)

    def _append_waveform(self, waveform: DigitalWaveform[TDigitalState]) -> None:
        self._append_waveforms([waveform])

    def _append_waveforms(self, waveforms: Sequence[DigitalWaveform[TDigitalState]]) -> None:
        for waveform in waveforms:
            if waveform.dtype != self.dtype:
                raise create_datatype_mismatch_error(
                    "input waveform", waveform.dtype, "waveform", self.dtype
                )

        new_timing = self._timing
        for waveform in waveforms:
            new_timing = new_timing._append_timing(waveform._timing)

        self._increase_capacity(sum(waveform.sample_count for waveform in waveforms))
        self._set_timing(new_timing)

        offset = self._start_index + self._sample_count
        for waveform in waveforms:
            self._data[offset : offset + waveform.sample_count] = waveform.data
            offset += waveform.sample_count
            self._sample_count += waveform.sample_count
            self._extended_properties._merge(waveform._extended_properties)

    def _increase_capacity(self, amount: int) -> None:
        new_capacity = self._start_index + self._sample_count + amount
        if new_capacity > self.capacity:
            self.capacity = new_capacity

    def load_data(
        self,
        array: npt.NDArray[TDigitalState],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> None:
        """Load new data into an existing waveform.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
        """
        if isinstance(array, np.ndarray):
            self._load_array(array, copy=copy, start_index=start_index, sample_count=sample_count)
        else:
            raise invalid_arg_type("input array", "array", array)

    def _load_array(
        self,
        array: npt.NDArray[TDigitalState],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        signal_count: SupportsIndex | None = None,
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "waveform", self.dtype)

        if array.ndim == 1:
            array_signal_count = 1
            array = array.reshape(len(array), 1)
        elif array.ndim == 2:
            array_signal_count = array.shape[1]
        else:
            raise invalid_array_ndim("input array", "one or two-dimensional array", array.ndim)

        if self._timing._timestamps is not None and len(array) != len(self._timing._timestamps):
            raise create_irregular_timestamp_count_mismatch_error(
                len(self._timing._timestamps), "input array length", len(array), reversed=True
            )

        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, len(array) - start_index)
        signal_count = arg_to_uint("signal count", signal_count, array_signal_count)

        if signal_count != array_signal_count:
            raise create_signal_count_mismatch_error(
                "input array", signal_count, "waveform", array_signal_count
            )

        if copy:
            if sample_count > len(self._data):
                self.capacity = sample_count
            self._data[0:sample_count] = array[start_index : start_index + sample_count]
            self._start_index = 0
            self._sample_count = sample_count
        else:
            self._data = array
            self._start_index = start_index
            self._sample_count = sample_count

    def test(
        self,
        expected_waveform: DigitalWaveform[TDigitalState],
        *,
        start_sample: SupportsIndex | None = 0,
        expected_start_sample: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> DigitalWaveformTestResult:
        """Test the digital waveform against an expected digital waveform.

        Args:
            expected_waveform: The expected digital waveform to compare against.
            start_sample: The beginning sample of ``self`` to compare.
            expected_start_sample: The beginning sample of ``expected_waveform`` to compare.
            sample_count: The number of samples to compare.

        Returns:
            The test result.
        """
        start_sample = arg_to_uint("start sample", start_sample, 0)
        expected_start_sample = arg_to_uint("expected start sample", expected_start_sample, 0)
        sample_count = arg_to_uint("sample count", sample_count, self.sample_count - start_sample)

        if self.signal_count != expected_waveform.signal_count:
            raise create_signal_count_mismatch_error(
                "expected waveform", expected_waveform.signal_count, "waveform", self.signal_count
            )
        if start_sample + sample_count > self.sample_count:
            raise create_start_index_or_sample_count_too_large_error(
                start_sample, sample_count, "number of samples in the waveform", self.sample_count
            )
        if expected_start_sample + sample_count > expected_waveform.sample_count:
            raise create_start_index_or_sample_count_too_large_error(
                expected_start_sample,
                sample_count,
                "number of samples in the expected waveform",
                expected_waveform.sample_count,
            )

        failures = []
        for _ in range(sample_count):
            for column_index in range(self.signal_count):
                signal_index = self._reverse_index(column_index)
                actual_state = DigitalState(self.data[start_sample, column_index])
                expected_state = DigitalState(
                    expected_waveform.data[expected_start_sample, column_index]
                )
                if DigitalState.test(actual_state, expected_state):
                    failures.append(
                        DigitalWaveformFailure(
                            start_sample,
                            expected_start_sample,
                            signal_index,
                            actual_state,
                            expected_state,
                        )
                    )
            start_sample += 1
            expected_start_sample += 1

        return DigitalWaveformTestResult(failures)

    def _reverse_index(self, index: int) -> int:
        """Convert a signal_index to a column_index, or vice versa."""
        assert 0 <= index < self.signal_count
        return self.signal_count - 1 - index

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return (
            self.dtype == value.dtype
            and np.array_equal(self.data, value.data)
            and self._extended_properties == value._extended_properties
            and self._timing == value._timing
        )

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._sample_count, self.signal_count, self.dtype)
        ctor_kwargs: dict[str, Any] = {
            "data": self.data,
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
            "timing": self._timing,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"{self._sample_count}, {self.signal_count}"]
        if self.dtype != np.uint8:
            args.append(f"{self.dtype.name}")
        # start_index and capacity are not shown because they are allocation details. data hides
        # the unused data before start_index and after start_index+sample_count.
        if self._sample_count > 0:
            # Hack: undo NumPy's line wrapping
            args.append(f"data={self.data!r}".replace("\n      ", ""))
        if self._extended_properties:
            args.append(f"extended_properties={self._extended_properties._properties!r}")
        if self._timing is not Timing.empty:
            args.append(f"timing={self._timing!r}")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_exceptions.py sha256=c90197836ccabd4d15e2e387aabca994244b4cb980a2a75fd53cc959267eab1c bytes=7132 -->
## FILE: src/nitypes/waveform/_exceptions.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_exceptions.py`
- sha256: `c90197836ccabd4d15e2e387aabca994244b4cb980a2a75fd53cc959267eab1c`
- bytes: 7132

````python
from __future__ import annotations

from typing_extensions import Literal

from nitypes.waveform.errors import (
    CapacityMismatchError,
    CapacityTooSmallError,
    DatatypeMismatchError,
    IrregularTimestampCountMismatchError,
    StartIndexTooLargeError,
    StartIndexOrSampleCountTooLargeError,
    NoTimestampInformationError,
    SampleIntervalModeMismatchError,
    SignalCountMismatchError,
)


def create_capacity_mismatch_error(capacity: int, array_length: int) -> CapacityMismatchError:
    """Create an error for a capacity-length mismatch."""
    message = (
        f"The capacity must match the input array length.\n\n"
        f"Capacity: {capacity}\n"
        f"Array length: {array_length}"
    )
    return CapacityMismatchError(message)


def create_capacity_too_small_error(
    capacity: int, min_capacity: int, object_description: str
) -> CapacityTooSmallError:
    """Create an error for when capacity is too small."""
    message = (
        f"The capacity must be equal to or greater than the number of samples in the {object_description}.\n\n"
        f"Capacity: {capacity}\n"
        f"Number of samples: {min_capacity}"
    )
    return CapacityTooSmallError(message)


def create_datatype_mismatch_error(
    arg_description: Literal["input array", "input spectrum", "input waveform"],
    arg_dtype: object,
    other_description: Literal["requested", "spectrum", "waveform"],
    other_dtype: object,
) -> DatatypeMismatchError:
    """Create an error for a data type mismatch."""
    arg_key = {
        "input array": "Input array data type",
        "input spectrum": "Input spectrum data type",
        "input waveform": "Input waveform data type",
    }
    other_key = {
        "requested": "Requested data type",
        "spectrum": "Spectrum data type",
        "waveform": "Waveform data type",
    }
    message = (
        f"The data type of the {arg_description} must match the {other_description} data type.\n\n"
        f"{arg_key[arg_description]}: {arg_dtype}\n"
        f"{other_key[other_description]}: {other_dtype}"
    )
    return DatatypeMismatchError(message)


def create_irregular_timestamp_count_mismatch_error(
    irregular_timestamp_count: int,
    other_description: Literal["input array length", "number of samples in the waveform"],
    other: int,
    *,
    reversed: bool = False,
) -> IrregularTimestampCountMismatchError:
    """Create an error for an irregular timestamp count mismatch."""
    other_key = {
        "input array length": "Array length",
        "number of samples in the waveform": "Number of samples",
    }
    if reversed:
        message = (
            "The input array length must be equal to the number of irregular timestamps.\n\n"
            f"{other_key[other_description]}: {other}\n"
            f"Number of timestamps: {irregular_timestamp_count}"
        )
    else:
        message = (
            f"The number of irregular timestamps must be equal to the {other_description}.\n\n"
            f"Number of timestamps: {irregular_timestamp_count}\n"
            f"{other_key[other_description]}: {other}"
        )
    return IrregularTimestampCountMismatchError(message)


def create_start_index_too_large_error(
    start_index: int,
    capacity_description: Literal[
        "capacity",
        "input array length",
        "number of samples in the spectrum",
        "number of samples in the waveform",
    ],
    capacity: int,
) -> StartIndexTooLargeError:
    """Create an error for an invalid start index argument."""
    capacity_key = {
        "capacity": "Capacity",
        "input array length": "Array length",
        "number of samples in the spectrum": "Number of samples",
        "number of samples in the waveform": "Number of samples",
    }
    message = (
        f"The start index must be less than or equal to the {capacity_description}.\n\n"
        f"Start index: {start_index}\n"
        f"{capacity_key[capacity_description]}: {capacity}"
    )
    return StartIndexTooLargeError(message)


def create_start_index_or_sample_count_too_large_error(
    start_index: int,
    sample_count: int,
    capacity_description: Literal[
        "capacity",
        "input array length",
        "number of samples in the expected waveform",
        "number of samples in the spectrum",
        "number of samples in the waveform",
    ],
    capacity: int,
) -> StartIndexOrSampleCountTooLargeError:
    """Create an error for an invalid start index or sample count argument."""
    capacity_key = {
        "capacity": "Capacity",
        "input array length": "Array length",
        "number of samples in the expected waveform": "Number of samples",
        "number of samples in the spectrum": "Number of samples",
        "number of samples in the waveform": "Number of samples",
    }
    message = (
        f"The sum of the start index and sample count must be less than or equal to the {capacity_description}.\n\n"
        f"Start index: {start_index}\n"
        f"Sample count: {sample_count}\n"
        f"{capacity_key[capacity_description]}: {capacity}"
    )
    return StartIndexOrSampleCountTooLargeError(message)


def create_no_timestamp_information_error() -> NoTimestampInformationError:
    """Create an error for waveform timing with no timestamp information."""
    message = (
        "The waveform timing does not have valid timestamp information. "
        "To obtain timestamps, the waveform must be irregular or must be initialized "
        "with a valid time stamp and sample interval."
    )
    return NoTimestampInformationError(message)


def create_sample_interval_mode_mismatch_error() -> SampleIntervalModeMismatchError:
    """Create an error for mixing none/regular with irregular timing."""
    message = (
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    return SampleIntervalModeMismatchError(message)


def create_signal_count_mismatch_error(
    arg_description: Literal["expected waveform", "input array", "input waveform", "provided"],
    arg_signal_count: int,
    other_description: Literal["array", "port", "waveform"],
    other_signal_count: int,
) -> SignalCountMismatchError:
    """Create an error for a mismatched signal count."""
    arg_key = {
        "expected waveform": "Expected waveform signal count",
        "input array": "Input array signal count",
        "input waveform": "Input waveform signal count",
        "provided": "Signal count",
    }
    other_key = {
        "array": "Array signal count",
        "port": "Port signal count",
        "waveform": "Waveform signal count",
    }
    message = (
        f"The {arg_description} signal count must match the {other_description} signal count.\n\n"
        f"{arg_key[arg_description]}: {arg_signal_count}\n"
        f"{other_key[other_description]}: {other_signal_count}"
    )
    return SignalCountMismatchError(message)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_extended_properties.py sha256=071d08b3ad6e3ef6aa012a336b4d263960d8334747ef4a5656c11b5530130075 bytes=2957 -->
## FILE: src/nitypes/waveform/_extended_properties.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_extended_properties.py`
- sha256: `071d08b3ad6e3ef6aa012a336b4d263960d8334747ef4a5656c11b5530130075`
- bytes: 2957

````python
from __future__ import annotations

import operator
import weakref
from collections.abc import Callable, Iterator, Mapping, MutableMapping
from typing import TYPE_CHECKING

from typing_extensions import TypeAlias

from nitypes.waveform.typing import ExtendedPropertyValue

# Extended property keys
CHANNEL_NAME = "NI_ChannelName"
LINE_NAMES = "NI_LineNames"
UNIT_DESCRIPTION = "NI_UnitDescription"

if TYPE_CHECKING:
    OnKeyChangedCallback: TypeAlias = Callable[[str], None]


class ExtendedPropertyDictionary(MutableMapping[str, ExtendedPropertyValue]):
    """A dictionary of extended properties.

    .. note::
        Data stored in the extended properties dictionary may not be encrypted when you send it
        over the network or write it to a TDMS file.
    """

    __slots__ = ["_properties", "_on_key_changed"]

    def __init__(self, properties: Mapping[str, ExtendedPropertyValue] | None = None, /) -> None:
        """Initialize a new ExtendedPropertyDictionary."""
        self._properties: dict[str, ExtendedPropertyValue] = {}
        self._on_key_changed: list[weakref.ref[OnKeyChangedCallback]] = []
        if properties is not None:
            self._properties.update(properties)

    def __len__(self) -> int:
        """Return len(self)."""
        return len(self._properties)

    def __iter__(self) -> Iterator[str]:
        """Implement iter(self)."""
        return iter(self._properties)

    def __contains__(self, value: object, /) -> bool:
        """Implement value in self."""
        return operator.contains(self._properties, value)

    def __getitem__(self, key: str, /) -> ExtendedPropertyValue:
        """Get self[key]."""
        return operator.getitem(self._properties, key)

    def __setitem__(self, key: str, value: ExtendedPropertyValue, /) -> None:
        """Set self[key] to value."""
        operator.setitem(self._properties, key, value)
        self._notify_on_key_changed(key)

    def __delitem__(self, key: str, /) -> None:
        """Delete self[key]."""
        operator.delitem(self._properties, key)
        self._notify_on_key_changed(key)

    def _notify_on_key_changed(self, key: str) -> None:
        for callback_ref in self._on_key_changed:
            callback = callback_ref()
            if callback:
                callback(key)

    def _merge(self, other: ExtendedPropertyDictionary) -> None:
        for key, value in other.items():
            self._properties.setdefault(key, value)

    def __reduce__(
        self,
    ) -> tuple[type[ExtendedPropertyDictionary], tuple[dict[str, ExtendedPropertyValue]]]:
        """Return object state for pickling, excluding the callback."""
        return (self.__class__, (self._properties,))

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"{self.__class__.__module__}.{self.__class__.__name__}({self._properties!r})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_numeric.py sha256=ece5c9deda7502320f08acd9bfa343a387714418801ec9a93fd5f54a27c974ed bytes=32610 -->
## FILE: src/nitypes/waveform/_numeric.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_numeric.py`
- sha256: `ece5c9deda7502320f08acd9bfa343a387714418801ec9a93fd5f54a27c974ed`
- bytes: 32610

````python
from __future__ import annotations

import datetime as dt
import sys
import warnings
from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Generic, SupportsIndex, overload

import hightime as ht
import numpy as np
import numpy.typing as npt
from typing_extensions import Self, TypeVar

from nitypes._arguments import arg_to_uint, validate_dtype, validate_unsupported_arg
from nitypes._exceptions import invalid_arg_type, invalid_array_ndim
from nitypes._numpy import asarray as _np_asarray
from nitypes.time.typing import AnyDateTime, AnyTimeDelta
from nitypes.waveform._exceptions import (
    create_capacity_mismatch_error,
    create_capacity_too_small_error,
    create_datatype_mismatch_error,
    create_irregular_timestamp_count_mismatch_error,
    create_start_index_or_sample_count_too_large_error,
    create_start_index_too_large_error,
)
from nitypes.waveform._extended_properties import CHANNEL_NAME, UNIT_DESCRIPTION
from nitypes.waveform._warnings import scale_mode_mismatch
from nitypes.waveform.typing import ExtendedPropertyValue

if sys.version_info < (3, 10):
    import array as std_array

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import (
        NO_SCALING,
        ExtendedPropertyDictionary,
        ScaleMode,
        Timing,
    )
else:
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary
    from nitypes.waveform._scaling import NO_SCALING, ScaleMode
    from nitypes.waveform._timing import Timing

# _TRaw specifies the type of the raw_data array. It is not limited to supported types. Requesting
# an unsupported type raises TypeError at run time. It is invariant because waveforms are mutable.
_TRaw = TypeVar("_TRaw", bound=np.generic)

# _TScaled specifies the type of the scaled_data property.
_TScaled = TypeVar("_TScaled", bound=np.generic)
_TOtherScaled = TypeVar("_TOtherScaled", bound=np.generic)


# Note about NumPy type hints:
# - At time of writing (April 2025), shape typing is still under development, so we do not
#   distinguish between 1D and 2D arrays in type hints.
# - npt.ArrayLike accepts some types that np.asarray() does not, such as buffers, so we are
#   explicitly using npt.NDArray | Sequence instead of npt.ArrayLike.
# - _TRaw is bound to np.generic, so Sequence[_TRaw] will not match list[int].
# - We are not using PEP 696 – Type Defaults for Type Parameters for type variables on functions
#   because it makes the type parameter default to np.float64 in some cases where it should be
#   inferred as Any, such as when dtype is specified as a str. PEP 696 seems more appropriate for
#   type variables on classes.


class NumericWaveform(ABC, Generic[_TRaw, _TScaled]):
    """A numeric waveform, which encapsulates numeric data and timing information.

    This is an abstract base class. To create a numeric waveform, use :class:`AnalogWaveform` or
    :class:`ComplexWaveform`.
    """

    @staticmethod
    @abstractmethod
    def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]:
        raise NotImplementedError

    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> Self:
        """Construct a waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A waveform containing the specified data.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 1:
                raise invalid_array_ndim(
                    "input array", "one-dimensional array or sequence", array.ndim
                )
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "one-dimensional array or sequence", array)

        return cls(
            raw_data=_np_asarray(array, dtype, copy=copy),
            start_index=start_index,
            sample_count=sample_count,
            extended_properties=extended_properties,
            timing=timing,
            scale_mode=scale_mode,
        )

    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> Sequence[Self]:
        """Construct multiple waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing a waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 2:
                raise invalid_array_ndim(
                    "input array", "two-dimensional array or nested sequence", array.ndim
                )
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "two-dimensional array or nested sequence", array)

        return [
            cls(
                raw_data=_np_asarray(array[i], dtype, copy=copy),
                start_index=start_index,
                sample_count=sample_count,
                extended_properties=extended_properties,
                timing=timing,
                scale_mode=scale_mode,
            )
            for i in range(len(array))
        ]

    __slots__ = [
        "_data",
        "_start_index",
        "_sample_count",
        "_extended_properties",
        "_timing",
        "_scale_mode",
        "__weakref__",
    ]

    _data: npt.NDArray[_TRaw]
    _start_index: int
    _sample_count: int
    _extended_properties: ExtendedPropertyDictionary
    _timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]
    _scale_mode: ScaleMode

    def __init__(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        raw_data: npt.NDArray[_TRaw] | None = None,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
        timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None = None,
        scale_mode: ScaleMode | None = None,
    ) -> None:
        """Initialize a new numeric waveform.

        Args:
            sample_count: The number of samples in the waveform.
            dtype: The NumPy data type for the waveform data.
            raw_data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A numeric waveform.
        """
        if raw_data is None:
            self._init_with_new_array(
                sample_count, dtype, start_index=start_index, capacity=capacity
            )
        elif isinstance(raw_data, np.ndarray):
            self._init_with_provided_array(
                raw_data,
                dtype,
                start_index=start_index,
                sample_count=sample_count,
                capacity=capacity,
            )
        else:
            raise invalid_arg_type("raw data", "NumPy ndarray", raw_data)

        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties

        if timing is None:
            timing = Timing.empty
        self._timing = timing

        if scale_mode is None:
            scale_mode = NO_SCALING
        self._scale_mode = scale_mode

    def _init_with_new_array(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, 0)
        capacity = arg_to_uint("capacity", capacity, sample_count)

        if dtype is None:
            dtype = self.__class__._get_default_raw_dtype()
        validate_dtype(dtype, self.__class__._get_supported_raw_dtypes())

        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "capacity", capacity)
        if start_index + sample_count > capacity:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "capacity", capacity
            )

        self._data = np.zeros(capacity, dtype)
        self._start_index = start_index
        self._sample_count = sample_count

    def _init_with_provided_array(
        self,
        data: npt.NDArray[_TRaw],
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = None,
        sample_count: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        if not isinstance(data, np.ndarray):
            raise invalid_arg_type("input array", "one-dimensional array", data)
        if data.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", data.ndim)

        if dtype is None:
            dtype = data.dtype
        if dtype != data.dtype:
            raise create_datatype_mismatch_error(
                "input array", data.dtype, "requested", np.dtype(dtype)
            )
        validate_dtype(dtype, self.__class__._get_supported_raw_dtypes())

        capacity = arg_to_uint("capacity", capacity, len(data))
        if capacity != len(data):
            raise create_capacity_mismatch_error(capacity, len(data))

        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "input array length", capacity)

        sample_count = arg_to_uint("sample count", sample_count, len(data) - start_index)
        if start_index + sample_count > len(data):
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "input array length", len(data)
            )

        self._data = data
        self._start_index = start_index
        self._sample_count = sample_count

    @property
    def raw_data(self) -> npt.NDArray[_TRaw]:
        """The raw waveform data."""
        return self._data[self._start_index : self._start_index + self._sample_count]

    def get_raw_data(
        self, start_index: SupportsIndex | None = 0, sample_count: SupportsIndex | None = None
    ) -> npt.NDArray[_TRaw]:
        """Get a subset of the raw waveform data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the raw waveform data.
        """
        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > self.sample_count:
            raise create_start_index_too_large_error(
                start_index, "number of samples in the waveform", self.sample_count
            )

        sample_count = arg_to_uint("sample count", sample_count, self.sample_count - start_index)
        if start_index + sample_count > self.sample_count:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "number of samples in the waveform", self.sample_count
            )

        return self.raw_data[start_index : start_index + sample_count]

    @property
    def scaled_data(self) -> npt.NDArray[_TScaled]:
        """The scaled waveform data.

        This property converts all of the waveform samples from the raw data type to the scaled
        data type and scales them using :attr:`scale_mode`. To scale a subset of the waveform or
        scale to single-precision floating point, use the :meth:`get_scaled_data` method
        instead.
        """
        return self.get_scaled_data()

    # If dtype is not specified, the dtype defaults to _TScaled.
    @overload
    def get_scaled_data(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        dtype: None = ...,
        *,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
    ) -> npt.NDArray[_TScaled]: ...

    @overload
    def get_scaled_data(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        dtype: type[_TOtherScaled] | np.dtype[_TOtherScaled],
        *,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
    ) -> npt.NDArray[_TOtherScaled]: ...

    @overload
    def get_scaled_data(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        dtype: npt.DTypeLike = ...,
        *,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
    ) -> npt.NDArray[Any]: ...

    def get_scaled_data(
        self,
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> npt.NDArray[Any]:
        """Get a subset of the scaled waveform data with the specified dtype.

        Args:
            dtype: The NumPy data type to use for scaled data.
            start_index: The sample index at which to start scaling.
            sample_count: The number of samples to scale.

        Returns:
            A subset of the scaled waveform data.
        """
        if dtype is None:
            dtype = self.__class__._get_default_scaled_dtype()
        validate_dtype(dtype, self.__class__._get_supported_scaled_dtypes())

        raw_data = self.get_raw_data(start_index, sample_count)
        converted_data: npt.NDArray[Any] = self._convert_data(dtype, raw_data)
        return self._scale_mode._transform_data(converted_data)

    @abstractmethod
    def _convert_data(
        self,
        dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled],
        raw_data: npt.NDArray[_TRaw],
    ) -> npt.NDArray[_TOtherScaled]:
        raise NotImplementedError

    @property
    def sample_count(self) -> int:
        """The number of samples in the waveform."""
        return self._sample_count

    @sample_count.setter
    def sample_count(self, value: int) -> None:
        """Set the number of samples in the waveform."""
        value = arg_to_uint("sample count", value)
        if self._start_index + value > self.capacity:
            raise create_start_index_or_sample_count_too_large_error(
                self._start_index, value, "capacity", self.capacity
            )
        self._sample_count = value

    @property
    def start_index(self) -> int:
        """The sample index of the underlying array at which the waveform data begins."""
        return self._start_index

    @property
    def capacity(self) -> int:
        """The total capacity available for waveform data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        """
        return len(self._data)

    @capacity.setter
    def capacity(self, value: int) -> None:
        value = arg_to_uint("capacity", value)
        min_capacity = self._start_index + self._sample_count
        if value < min_capacity:
            raise create_capacity_too_small_error(value, min_capacity, "waveform")
        if value != len(self._data):
            self._data.resize(value, refcheck=False)

    @property
    def dtype(self) -> np.dtype[_TRaw]:
        """The NumPy dtype for the waveform data."""
        return self._data.dtype

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the waveform.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        """
        return self._extended_properties

    @property
    def channel_name(self) -> str:
        """The name of the device channel from which the waveform was acquired."""
        value = self._extended_properties.get(CHANNEL_NAME, "")
        assert isinstance(value, str)
        return value

    @channel_name.setter
    def channel_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("channel name", "str", value)
        self._extended_properties[CHANNEL_NAME] = value

    @property
    def units(self) -> str:
        """The unit of measurement, such as volts, of the waveform."""
        value = self._extended_properties.get(UNIT_DESCRIPTION, "")
        assert isinstance(value, str)
        return value

    @units.setter
    def units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("units", "str", value)
        self._extended_properties[UNIT_DESCRIPTION] = value

    def _set_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if self._timing is not value:
            self._timing = value

    def _validate_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if value._timestamps is not None and len(value._timestamps) != self._sample_count:
            raise create_irregular_timestamp_count_mismatch_error(
                len(value._timestamps), "number of samples in the waveform", self._sample_count
            )

    @property
    def timing(self) -> Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]:
        """The timing information of the waveform.

        The default value is Timing.empty.
        """
        return self._timing

    @timing.setter
    def timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None:
        if not isinstance(value, Timing):
            raise invalid_arg_type("timing information", "Timing object", value)
        self._validate_timing(value)
        self._set_timing(value)

    @property
    def scale_mode(self) -> ScaleMode:
        """The scale mode of the waveform."""
        return self._scale_mode

    @scale_mode.setter
    def scale_mode(self, value: ScaleMode) -> None:
        if not isinstance(value, ScaleMode):
            raise invalid_arg_type("scale mode", "ScaleMode object", value)
        self._scale_mode = value

    def append(
        self,
        other: (
            npt.NDArray[_TRaw]
            | NumericWaveform[_TRaw, _TScaled]
            | Sequence[NumericWaveform[_TRaw, _TScaled]]
        ),
        /,
        timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None = None,
    ) -> None:
        """Append data to the waveform.

        Args:
            other: The array or waveform(s) to append.
            timestamps: A sequence of timestamps. When the current waveform has
                SampleIntervalMode.IRREGULAR, you must provide a sequence of timestamps with the
                same length as the array.

        Raises:
            TimingMismatchError: The current and other waveforms have incompatible timing.
            TimingMismatchWarning: The sample intervals of the waveform(s) do not match.
            ScalingMismatchWarning: The scale modes of the waveform(s) do not match.
            ValueError: The other array has the wrong number of dimensions or the length of the
                timestamps argument does not match the length of the other array.
            TypeError: The data types of the current waveform and other array or waveform(s) do not
                match, or an argument has the wrong data type.

        When appending waveforms:

        * Timing information is merged based on the sample interval mode of the current
          waveform:

          * SampleIntervalMode.NONE or SampleIntervalMode.REGULAR: The other waveform(s) must also
            have SampleIntervalMode.NONE or SampleIntervalMode.REGULAR. If the sample interval does
            not match, a TimingMismatchWarning is generated. Otherwise, the timing information of
            the other waveform(s) is discarded.

          * SampleIntervalMode.IRREGULAR: The other waveforms(s) must also have
            SampleIntervalMode.IRREGULAR. The timestamps of the other waveforms(s) are appended to
            the current waveform's timing information.

        * Extended properties of the other waveform(s) are merged into the current waveform if they
          are not already set in the current waveform.

        * If the scale mode of other waveform(s) does not match the scale mode of the current
          waveform, a ScalingMismatchWarning is generated. Otherwise, the scaling information of the
          other waveform(s) is discarded.
        """
        if isinstance(other, np.ndarray):
            self._append_array(other, timestamps)
        elif isinstance(other, NumericWaveform):
            validate_unsupported_arg("timestamps", timestamps)
            self._append_waveform(other)
        elif isinstance(other, Sequence) and all(isinstance(x, NumericWaveform) for x in other):
            validate_unsupported_arg("timestamps", timestamps)
            self._append_waveforms(other)
        else:
            raise invalid_arg_type("input", "array or waveform(s)", other)

    def _append_array(
        self,
        array: npt.NDArray[_TRaw],
        timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None = None,
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "waveform", self.dtype)
        if array.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", array.ndim)
        if timestamps is not None and len(array) != len(timestamps):
            raise create_irregular_timestamp_count_mismatch_error(
                len(timestamps), "input array length", len(array)
            )

        new_timing = self._timing._append_timestamps(timestamps)

        self._increase_capacity(len(array))
        self._set_timing(new_timing)

        offset = self._start_index + self._sample_count
        self._data[offset : offset + len(array)] = array
        self._sample_count += len(array)

    def _append_waveform(self, waveform: NumericWaveform[_TRaw, _TScaled]) -> None:
        self._append_waveforms([waveform])

    def _append_waveforms(self, waveforms: Sequence[NumericWaveform[_TRaw, _TScaled]]) -> None:
        for waveform in waveforms:
            if waveform.dtype != self.dtype:
                raise create_datatype_mismatch_error(
                    "input waveform", waveform.dtype, "waveform", self.dtype
                )
            if waveform._scale_mode != self._scale_mode:
                warnings.warn(scale_mode_mismatch())

        new_timing = self._timing
        for waveform in waveforms:
            new_timing = new_timing._append_timing(waveform._timing)

        self._increase_capacity(sum(waveform.sample_count for waveform in waveforms))
        self._set_timing(new_timing)

        offset = self._start_index + self._sample_count
        for waveform in waveforms:
            self._data[offset : offset + waveform.sample_count] = waveform.raw_data
            offset += waveform.sample_count
            self._sample_count += waveform.sample_count
            self._extended_properties._merge(waveform._extended_properties)

    def _increase_capacity(self, amount: int) -> None:
        new_capacity = self._start_index + self._sample_count + amount
        if new_capacity > self.capacity:
            self.capacity = new_capacity

    def load_data(
        self,
        array: npt.NDArray[_TRaw],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> None:
        """Load new data into an existing waveform.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
        """
        if isinstance(array, np.ndarray):
            self._load_array(array, copy=copy, start_index=start_index, sample_count=sample_count)
        else:
            raise invalid_arg_type("input array", "array", array)

    def _load_array(
        self,
        array: npt.NDArray[_TRaw],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "waveform", self.dtype)
        if array.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", array.ndim)
        if self._timing._timestamps is not None and len(array) != len(self._timing._timestamps):
            raise create_irregular_timestamp_count_mismatch_error(
                len(self._timing._timestamps), "input array length", len(array), reversed=True
            )

        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, len(array) - start_index)

        if copy:
            if sample_count > len(self._data):
                self.capacity = sample_count
            self._data[0:sample_count] = array[start_index : start_index + sample_count]
            self._start_index = 0
            self._sample_count = sample_count
        else:
            self._data = array
            self._start_index = start_index
            self._sample_count = sample_count

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return (
            self.dtype == value.dtype
            and np.array_equal(self.raw_data, value.raw_data)
            and self._extended_properties == value._extended_properties
            and self._timing == value._timing
            and self._scale_mode == value._scale_mode
        )

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._sample_count, self.dtype)
        ctor_kwargs: dict[str, Any] = {
            "raw_data": self.raw_data,
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
            "timing": self._timing,
            "scale_mode": self._scale_mode,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"{self._sample_count}"]
        if self.dtype != self.__class__._get_default_raw_dtype():
            args.append(f"{self.dtype.name}")
        # start_index and capacity are not shown because they are allocation details. raw_data hides
        # the unused data before start_index and after start_index+sample_count.
        if self._sample_count > 0:
            args.append(f"raw_data={self.raw_data!r}")
        if self._extended_properties:
            args.append(f"extended_properties={self._extended_properties._properties!r}")
        if self._timing is not Timing.empty:
            args.append(f"timing={self._timing!r}")
        if self._scale_mode is not NO_SCALING:
            args.append(f"scale_mode={self._scale_mode}")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_scaling/__init__.py sha256=311f007c4fa38d677f35ecc7b95e272781c947e17ce2612e7f8d8afcd28c0902 bytes=389 -->
## FILE: src/nitypes/waveform/_scaling/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_scaling/__init__.py`
- sha256: `311f007c4fa38d677f35ecc7b95e272781c947e17ce2612e7f8d8afcd28c0902`
- bytes: 389

````python
"""Waveform scaling data types for NI Python APIs."""

from nitypes.waveform._scaling._base import ScaleMode
from nitypes.waveform._scaling._linear import LinearScaleMode
from nitypes.waveform._scaling._none import NoneScaleMode

__all__ = ["LinearScaleMode", "NO_SCALING", "NoneScaleMode", "ScaleMode"]

NO_SCALING = NoneScaleMode()
"""A scale mode that does not scale data."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_scaling/_base.py sha256=14a70375094ef55ec9749a042df616cc7a5df1154456a2439ff91ed4329f17bf bytes=476 -->
## FILE: src/nitypes/waveform/_scaling/_base.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_scaling/_base.py`
- sha256: `14a70375094ef55ec9749a042df616cc7a5df1154456a2439ff91ed4329f17bf`
- bytes: 476

````python
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar

import numpy as np
import numpy.typing as npt


_ScalarType = TypeVar("_ScalarType", bound=np.generic)


class ScaleMode(ABC):
    """An object that specifies how the waveform is scaled."""

    __slots__ = ()

    @abstractmethod
    def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]:
        raise NotImplementedError
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_scaling/_linear.py sha256=7dd141e45a742c617f978a39f2d2f5a89b749472578fca949d75dd16782a5308 bytes=2130 -->
## FILE: src/nitypes/waveform/_scaling/_linear.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_scaling/_linear.py`
- sha256: `7dd141e45a742c617f978a39f2d2f5a89b749472578fca949d75dd16782a5308`
- bytes: 2130

````python
from __future__ import annotations

from typing import TYPE_CHECKING, SupportsFloat

import numpy.typing as npt

from nitypes._arguments import arg_to_float
from nitypes.waveform._scaling._base import _ScalarType

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ScaleMode
else:
    from nitypes.waveform._scaling._base import ScaleMode


class LinearScaleMode(ScaleMode):
    """A scale mode that scales data linearly."""

    __slots__ = ["_gain", "_offset", "__weakref__"]

    _gain: float
    _offset: float

    def __init__(self, gain: SupportsFloat, offset: SupportsFloat) -> None:
        """Initialize a new scale mode object that scales data linearly.

        Args:
            gain: The gain of the linear scale.
            offset: The offset of the linear scale.

        Returns:
            A scale mode that scales data linearly.
        """
        self._gain = arg_to_float("gain", gain)
        self._offset = arg_to_float("offset", offset)

    @property
    def gain(self) -> float:
        """The gain of the linear scale."""
        return self._gain

    @property
    def offset(self) -> float:
        """The offset of the linear scale."""
        return self._offset

    def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]:
        # https://github.com/numpy/numpy/issues/28805 - TYP: mypy infers that adding/multiplying a
        # npt.NDArray[np.float32] with a float promotes dtype to Any or np.float64
        return data * self._gain + self._offset  # type: ignore[operator,no-any-return]

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self._gain == value._gain and self._offset == value._offset

    def __repr__(
        self,
    ) -> str:
        """Return repr(self)."""
        return f"{self.__class__.__module__}.{self.__class__.__name__}({self.gain}, {self.offset})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_scaling/_none.py sha256=4ea15f978f9cd855e5a3989576fd207208a9ca4902a6fc88adf98f72442d5450 bytes=955 -->
## FILE: src/nitypes/waveform/_scaling/_none.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_scaling/_none.py`
- sha256: `4ea15f978f9cd855e5a3989576fd207208a9ca4902a6fc88adf98f72442d5450`
- bytes: 955

````python
from __future__ import annotations

from typing import TYPE_CHECKING

import numpy.typing as npt

from nitypes.waveform._scaling._base import _ScalarType

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ScaleMode
else:
    from nitypes.waveform._scaling._base import ScaleMode


class NoneScaleMode(ScaleMode):
    """A scale mode that does not scale data."""

    __slots__ = ()

    def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]:
        return data

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return True

    def __repr__(
        self,
    ) -> str:
        """Return repr(self)."""
        return f"{self.__class__.__module__}.{self.__class__.__name__}()"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_spectrum.py sha256=50b27d4294fb0c6d75fd392bc8e5b3aa19f8ffeab6c9847c32784c153244a980 bytes=31226 -->
## FILE: src/nitypes/waveform/_spectrum.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_spectrum.py`
- sha256: `50b27d4294fb0c6d75fd392bc8e5b3aa19f8ffeab6c9847c32784c153244a980`
- bytes: 31226

````python
from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import (
    TYPE_CHECKING,
    Any,
    Generic,
    SupportsFloat,
    SupportsIndex,
    Union,
    final,
    overload,
)

import numpy as np
import numpy.typing as npt
from typing_extensions import Self, TypeVar

from nitypes._arguments import arg_to_float, arg_to_uint, validate_dtype
from nitypes._exceptions import invalid_arg_type, invalid_array_ndim
from nitypes._numpy import asarray as _np_asarray, long as _np_long, ulong as _np_ulong
from nitypes.waveform._exceptions import (
    create_capacity_mismatch_error,
    create_capacity_too_small_error,
    create_datatype_mismatch_error,
    create_start_index_or_sample_count_too_large_error,
    create_start_index_too_large_error,
)
from nitypes.waveform._extended_properties import CHANNEL_NAME, UNIT_DESCRIPTION
from nitypes.waveform.typing import ExtendedPropertyValue

if sys.version_info < (3, 10):
    import array as std_array

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ExtendedPropertyDictionary
else:
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary

_TData = TypeVar("_TData", bound=Union[np.floating, np.integer])
_TOtherData = TypeVar("_TOtherData", bound=Union[np.floating, np.integer])

# Use the C types here because np.isdtype() considers some of them to be distinct types, even when
# they have the same size (e.g. np.intc vs. np.int_).
_DATA_DTYPES = (
    # Floating point
    np.single,
    np.double,
    # Signed integers
    np.byte,
    np.short,
    np.intc,
    np.int_,
    _np_long,
    np.longlong,
    # Unsigned integers
    np.ubyte,
    np.ushort,
    np.uintc,
    np.uint,
    _np_ulong,
    np.ulonglong,
)


@final
class Spectrum(Generic[_TData]):
    """A frequency spectrum, which encapsulates analog data and frequency information.

    Constructing
    ^^^^^^^^^^^^

    To construct a frequency spectrum, use the :class:`Spectrum` class:

    >>> Spectrum()
    nitypes.waveform.Spectrum(0)
    >>> Spectrum(5)
    nitypes.waveform.Spectrum(5, data=array([0., 0., 0., 0., 0.]))

    To construct a frequency spectrum from a NumPy array, use the :any:`Spectrum.from_array_1d`
    method.

    >>> import numpy as np
    >>> Spectrum.from_array_1d(np.array([1.0, 2.0, 3.0]))
    nitypes.waveform.Spectrum(3, data=array([1., 2., 3.]))

    You can also use :any:`Spectrum.from_array_1d` to construct a frequency spectrum from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> Spectrum.from_array_1d([1.0, 2.0, 3.0], np.float64)
    nitypes.waveform.Spectrum(3, data=array([1., 2., 3.]))

    The 2D version, :any:`Spectrum.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    >>> Spectrum.from_array_2d(nested_list, np.float64)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.Spectrum(3, data=array([1., 2., 3.])),
    nitypes.waveform.Spectrum(3, data=array([4., 5., 6.]))]

    Class members
    ^^^^^^^^^^^^^
    """

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[_TOtherData],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Spectrum[_TOtherData]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: type[_TOtherData] | np.dtype[_TOtherData],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Spectrum[_TOtherData]: ...

    @overload
    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Spectrum[Any]: ...

    @classmethod
    def from_array_1d(
        cls,
        array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        start_frequency: SupportsFloat | None = None,
        frequency_increment: SupportsFloat | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
    ) -> Spectrum[Any]:
        """Construct a spectrum from a one-dimensional array or sequence.

        Args:
            array: The spectrum data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the spectrum data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.

        Returns:
            A spectrum containing the specified data.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 1:
                raise invalid_array_ndim(
                    "input array", "one-dimensional array or sequence", array.ndim
                )
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "one-dimensional array or sequence", array)

        return cls(
            data=_np_asarray(array, dtype, copy=copy),
            start_index=start_index,
            sample_count=sample_count,
            start_frequency=start_frequency,
            frequency_increment=frequency_increment,
            extended_properties=extended_properties,
        )

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[_TOtherData],
        dtype: None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Sequence[Spectrum[_TOtherData]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: type[_TOtherData] | np.dtype[_TOtherData],
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Sequence[Spectrum[_TOtherData]]: ...

    @overload
    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = ...,
        *,
        copy: bool = ...,
        start_index: SupportsIndex | None = ...,
        sample_count: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> Sequence[Spectrum[Any]]: ...

    @classmethod
    def from_array_2d(
        cls,
        array: npt.NDArray[Any] | Sequence[Sequence[Any]],
        dtype: npt.DTypeLike | None = None,
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
        start_frequency: SupportsFloat | None = None,
        frequency_increment: SupportsFloat | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
    ) -> Sequence[Spectrum[Any]]:
        """Construct a list of spectrums from a two-dimensional array or nested sequence.

        Args:
            array: The spectrum data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the spectrum data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.

        Returns:
            A list containing a spectrum for each row of the specified data.

        When constructing multiple spectrums, the same extended properties, timing
        information, and scale mode are applied to all spectrums. Consider assigning
        these properties after construction.
        """
        if isinstance(array, np.ndarray):
            if array.ndim != 2:
                raise invalid_array_ndim(
                    "input array", "two-dimensional array or nested sequence", array.ndim
                )
        elif isinstance(array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "two-dimensional array or nested sequence", array)

        return [
            cls(
                data=_np_asarray(array[i], dtype, copy=copy),
                start_index=start_index,
                sample_count=sample_count,
                start_frequency=start_frequency,
                frequency_increment=frequency_increment,
                extended_properties=extended_properties,
            )
            for i in range(len(array))
        ]

    __slots__ = [
        "_data",
        "_start_index",
        "_sample_count",
        "_start_frequency",
        "_frequency_increment",
        "_extended_properties",
        "__weakref__",
    ]

    _data: npt.NDArray[_TData]
    _start_index: int
    _sample_count: int
    _start_frequency: float
    _frequency_increment: float
    _extended_properties: ExtendedPropertyDictionary

    # If neither dtype nor data is specified, _TData defaults to np.float64.
    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: Spectrum[np.float64],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: Spectrum[_TOtherData],
        sample_count: SupportsIndex | None = ...,
        dtype: type[_TOtherData] | np.dtype[_TOtherData] = ...,
        *,
        data: None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: Spectrum[_TOtherData],
        sample_count: SupportsIndex | None = ...,
        dtype: None = ...,
        *,
        data: npt.NDArray[_TOtherData] = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
    ) -> None: ...

    @overload
    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self: Spectrum[Any],
        sample_count: SupportsIndex | None = ...,
        dtype: npt.DTypeLike | None = ...,
        *,
        data: npt.NDArray[Any] | None = ...,
        start_index: SupportsIndex | None = ...,
        capacity: SupportsIndex | None = ...,
        start_frequency: SupportsFloat | None = ...,
        frequency_increment: SupportsFloat | None = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
        copy_extended_properties: bool = ...,
    ) -> None: ...

    def __init__(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        data: npt.NDArray[Any] | None = None,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
        start_frequency: SupportsFloat | None = None,
        frequency_increment: SupportsFloat | None = None,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
    ) -> None:
        """Initialize a new frequency spectrum.

        Args:
            sample_count: The number of samples in the spectrum.
            dtype: The NumPy data type for the spectrum data.
            data: A NumPy ndarray to use for sample storage. The spectrum takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A frequency spectrum.
        """
        if data is None:
            self._init_with_new_array(
                sample_count, dtype, start_index=start_index, capacity=capacity
            )
        elif isinstance(data, np.ndarray):
            self._init_with_provided_array(
                data,
                dtype,
                start_index=start_index,
                sample_count=sample_count,
                capacity=capacity,
            )
        else:
            raise invalid_arg_type("raw data", "NumPy ndarray", data)

        self._start_frequency = arg_to_float("start frequency", start_frequency, 0.0)
        self._frequency_increment = arg_to_float("frequency increment", frequency_increment, 0.0)

        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties

    def _init_with_new_array(
        self,
        sample_count: SupportsIndex | None = None,
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, 0)
        capacity = arg_to_uint("capacity", capacity, sample_count)

        if dtype is None:
            dtype = np.float64
        validate_dtype(dtype, _DATA_DTYPES)

        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "capacity", capacity)
        if start_index + sample_count > capacity:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "capacity", capacity
            )

        self._data = np.zeros(capacity, dtype)
        self._start_index = start_index
        self._sample_count = sample_count

    def _init_with_provided_array(
        self,
        data: npt.NDArray[_TData],
        dtype: npt.DTypeLike | None = None,
        *,
        start_index: SupportsIndex | None = None,
        sample_count: SupportsIndex | None = None,
        capacity: SupportsIndex | None = None,
    ) -> None:
        if not isinstance(data, np.ndarray):
            raise invalid_arg_type("input array", "one-dimensional array", data)
        if data.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", data.ndim)

        if dtype is None:
            dtype = data.dtype
        if dtype != data.dtype:
            raise create_datatype_mismatch_error(
                "input array", data.dtype, "requested", np.dtype(dtype)
            )
        validate_dtype(dtype, _DATA_DTYPES)

        capacity = arg_to_uint("capacity", capacity, len(data))
        if capacity != len(data):
            raise create_capacity_mismatch_error(capacity, len(data))

        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > capacity:
            raise create_start_index_too_large_error(start_index, "input array length", capacity)

        sample_count = arg_to_uint("sample count", sample_count, len(data) - start_index)
        if start_index + sample_count > len(data):
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "input array length", len(data)
            )

        self._data = data
        self._start_index = start_index
        self._sample_count = sample_count

    @property
    def data(self) -> npt.NDArray[_TData]:
        """The spectrum data."""
        return self._data[self._start_index : self._start_index + self._sample_count]

    def get_data(
        self, start_index: SupportsIndex | None = 0, sample_count: SupportsIndex | None = None
    ) -> npt.NDArray[_TData]:
        """Get a subset of the spectrum data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the spectrum data.
        """
        start_index = arg_to_uint("start index", start_index, 0)
        if start_index > self.sample_count:
            raise create_start_index_too_large_error(
                start_index, "number of samples in the spectrum", self.sample_count
            )

        sample_count = arg_to_uint("sample count", sample_count, self.sample_count - start_index)
        if start_index + sample_count > self.sample_count:
            raise create_start_index_or_sample_count_too_large_error(
                start_index, sample_count, "number of samples in the spectrum", self.sample_count
            )

        return self.data[start_index : start_index + sample_count]

    @property
    def sample_count(self) -> int:
        """The number of samples in the spectrum."""
        return self._sample_count

    @property
    def start_index(self) -> int:
        """The sample index of the underlying array at which the spectrum data begins."""
        return self._start_index

    @property
    def capacity(self) -> int:
        """The total capacity available for spectrum data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        """
        return len(self._data)

    @capacity.setter
    def capacity(self, value: int) -> None:
        value = arg_to_uint("capacity", value)
        min_capacity = self._start_index + self._sample_count
        if value < min_capacity:
            raise create_capacity_too_small_error(value, min_capacity, "spectrum")
        if value != len(self._data):
            self._data.resize(value, refcheck=False)

    @property
    def dtype(self) -> np.dtype[_TData]:
        """The NumPy dtype for the spectrum data."""
        return self._data.dtype

    @property
    def start_frequency(self) -> float:
        """The start frequency of the spectrum."""
        return self._start_frequency

    @start_frequency.setter
    def start_frequency(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise invalid_arg_type("start frequency", "float", value)
        self._start_frequency = value

    @property
    def frequency_increment(self) -> float:
        """The frequency increment of the spectrum."""
        return self._frequency_increment

    @frequency_increment.setter
    def frequency_increment(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise invalid_arg_type("frequency increment", "float", value)
        self._frequency_increment = value

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the spectrum."""
        return self._extended_properties

    @property
    def channel_name(self) -> str:
        """The name of the device channel from which the spectrum was acquired."""
        value = self._extended_properties.get(CHANNEL_NAME, "")
        assert isinstance(value, str)
        return value

    @channel_name.setter
    def channel_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("channel name", "str", value)
        self._extended_properties[CHANNEL_NAME] = value

    @property
    def units(self) -> str:
        """The unit of measurement, such as volts, of the spectrum."""
        value = self._extended_properties.get(UNIT_DESCRIPTION, "")
        assert isinstance(value, str)
        return value

    @units.setter
    def units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("units", "str", value)
        self._extended_properties[UNIT_DESCRIPTION] = value

    def append(
        self,
        other: npt.NDArray[_TData] | Spectrum[_TData] | Sequence[Spectrum[_TData]],
        /,
    ) -> None:
        """Append data to the spectrum.

        Args:
            other: The array or spectrum(s) to append.

        Raises:
            ValueError: The other array has the wrong number of dimensions.
            TypeError: The data types of the current spectrum and other array or spectrum(s) do not
                match, or an argument has the wrong data type.

        When appending spectrums:

        * Extended properties of the other spectrum(s) are merged into the current spectrum if they
          are not already set in the current spectrum.
        """
        if isinstance(other, np.ndarray):
            self._append_array(other)
        elif isinstance(other, Spectrum):
            self._append_spectrum(other)
        elif isinstance(other, Sequence) and all(isinstance(x, Spectrum) for x in other):
            self._append_spectrums(other)
        else:
            raise invalid_arg_type("input", "array or spectrum(s)", other)

    def _append_array(
        self,
        array: npt.NDArray[_TData],
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "spectrum", self.dtype)
        if array.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", array.ndim)

        self._increase_capacity(len(array))

        offset = self._start_index + self._sample_count
        self._data[offset : offset + len(array)] = array
        self._sample_count += len(array)

    def _append_spectrum(self, spectrum: Spectrum[_TData]) -> None:
        self._append_spectrums([spectrum])

    def _append_spectrums(self, spectrums: Sequence[Spectrum[_TData]]) -> None:
        for spectrum in spectrums:
            if spectrum.dtype != self.dtype:
                raise create_datatype_mismatch_error(
                    "input spectrum", spectrum.dtype, "spectrum", self.dtype
                )

        self._increase_capacity(sum(spectrum.sample_count for spectrum in spectrums))

        offset = self._start_index + self._sample_count
        for spectrum in spectrums:
            self._data[offset : offset + spectrum.sample_count] = spectrum.data
            offset += spectrum.sample_count
            self._sample_count += spectrum.sample_count
            self._extended_properties._merge(spectrum._extended_properties)

    def _increase_capacity(self, amount: int) -> None:
        new_capacity = self._start_index + self._sample_count + amount
        if new_capacity > self.capacity:
            self.capacity = new_capacity

    def load_data(
        self,
        array: npt.NDArray[_TData],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> None:
        """Load new data into an existing spectrum.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
        """
        if isinstance(array, np.ndarray):
            self._load_array(array, copy=copy, start_index=start_index, sample_count=sample_count)
        else:
            raise invalid_arg_type("input array", "array", array)

    def _load_array(
        self,
        array: npt.NDArray[_TData],
        *,
        copy: bool = True,
        start_index: SupportsIndex | None = 0,
        sample_count: SupportsIndex | None = None,
    ) -> None:
        if array.dtype != self.dtype:
            raise create_datatype_mismatch_error("input array", array.dtype, "spectrum", self.dtype)
        if array.ndim != 1:
            raise invalid_array_ndim("input array", "one-dimensional array", array.ndim)

        start_index = arg_to_uint("start index", start_index, 0)
        sample_count = arg_to_uint("sample count", sample_count, len(array) - start_index)

        if copy:
            if sample_count > len(self._data):
                self.capacity = sample_count
            self._data[0:sample_count] = array[start_index : start_index + sample_count]
            self._start_index = 0
            self._sample_count = sample_count
        else:
            self._data = array
            self._start_index = start_index
            self._sample_count = sample_count

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return (
            self.dtype == value.dtype
            and np.array_equal(self.data, value.data)
            and self.start_frequency == value.start_frequency
            and self.frequency_increment == value.frequency_increment
            and self._extended_properties == value._extended_properties
        )

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._sample_count, self.dtype)
        ctor_kwargs: dict[str, Any] = {
            "data": self.data,
            "start_frequency": self._start_frequency,
            "frequency_increment": self._frequency_increment,
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"{self._sample_count}"]
        if self.dtype != np.float64:
            args.append(f"{self.dtype.name}")
        # start_index and capacity are not shown because they are allocation details. data hides
        # the unused data before start_index and after start_index+sample_count.
        if self._sample_count > 0:
            args.append(f"data={self.data!r}")
        if self._start_frequency != 0.0:
            args.append(f"start_frequency={self.start_frequency!r}")
        if self._frequency_increment != 0.0:
            args.append(f"frequency_increment={self._frequency_increment!r}")
        if self._extended_properties:
            args.append(f"extended_properties={self._extended_properties._properties!r}")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/__init__.py sha256=e8f5a5aecf54514a9fae41af8c563ac9102e860ef4832106b7eb6d9ae3d1be0a bytes=243 -->
## FILE: src/nitypes/waveform/_timing/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/__init__.py`
- sha256: `e8f5a5aecf54514a9fae41af8c563ac9102e860ef4832106b7eb6d9ae3d1be0a`
- bytes: 243

````python
"""Waveform timing data types for NI Python APIs."""

from nitypes.waveform._timing._sample_interval import SampleIntervalMode
from nitypes.waveform._timing._timing import Timing

__all__ = [
    "SampleIntervalMode",
    "Timing",
]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/__init__.py sha256=9b78c655fe094fe9a40ca40d916096ae6399d96aef4dc50d1cddd9a26bbb4e62 bytes=1631 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/__init__.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/__init__.py`
- sha256: `9b78c655fe094fe9a40ca40d916096ae6399d96aef4dc50d1cddd9a26bbb4e62`
- bytes: 1631

````python
"""Sample interval strategies for waveform timing."""

from typing import Any

from nitypes._exceptions import invalid_arg_value
from nitypes.waveform._timing._sample_interval._base import SampleIntervalStrategy
from nitypes.waveform._timing._sample_interval._irregular import (
    IrregularSampleIntervalStrategy,
)
from nitypes.waveform._timing._sample_interval._mode import SampleIntervalMode
from nitypes.waveform._timing._sample_interval._none import NoneSampleIntervalStrategy
from nitypes.waveform._timing._sample_interval._regular import (
    RegularSampleIntervalStrategy,
)

__all__ = [
    "create_sample_interval_strategy",
    "IrregularSampleIntervalStrategy",
    "NoneSampleIntervalStrategy",
    "RegularSampleIntervalStrategy",
    "SampleIntervalMode",
    "SampleIntervalStrategy",
]


def create_sample_interval_strategy(
    sample_interval_mode: SampleIntervalMode,
) -> SampleIntervalStrategy[Any, Any, Any]:
    """Create a sample interval strategy for the specified mode."""
    strategy_type = _SAMPLE_INTERVAL_STRATEGY_TYPE_FOR_MODE.get(sample_interval_mode)
    if strategy_type is None:
        raise invalid_arg_value(
            "sample interval mode", "SampleIntervalMode object", sample_interval_mode
        )
    return strategy_type()


_SAMPLE_INTERVAL_STRATEGY_TYPE_FOR_MODE: dict[
    SampleIntervalMode, type[SampleIntervalStrategy[Any, Any, Any]]
] = {
    SampleIntervalMode.NONE: NoneSampleIntervalStrategy,
    SampleIntervalMode.REGULAR: RegularSampleIntervalStrategy,
    SampleIntervalMode.IRREGULAR: IrregularSampleIntervalStrategy,
}
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_base.py sha256=6b33833283732973bc63cd93147116a6cf2f4574301adb72264368518600117b bytes=2410 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/_base.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/_base.py`
- sha256: `6b33833283732973bc63cd93147116a6cf2f4574301adb72264368518600117b`
- bytes: 2410

````python
from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Generic

from nitypes.waveform._timing._sample_interval._mode import SampleIntervalMode
from nitypes.waveform.typing import TSampleInterval_co, TTimeOffset_co, TTimestamp_co

if TYPE_CHECKING:
    from nitypes.waveform._timing._timing import Timing  # circular import


class SampleIntervalStrategy(ABC, Generic[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]):
    """Implements SampleIntervalMode specific behavior."""

    # Note that timing is always passed as a parameter. The timing object has a reference to the
    # strategy, so saving a reference to the timing object would introduce a reference cycle.
    __slots__ = ()

    @abstractmethod
    def validate_init_args(
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        sample_interval_mode: SampleIntervalMode,
        timestamp: TTimestamp_co | None,
        time_offset: TTimeOffset_co | None,
        sample_interval: TSampleInterval_co | None,
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> None:
        """Validate the BaseTiming.__init__ arguments for this mode."""
        raise NotImplementedError

    @abstractmethod
    def get_timestamps(
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        start_index: int,
        count: int,
    ) -> Iterable[TTimestamp_co]:
        """Get or generate timestamps for the specified samples."""
        raise NotImplementedError

    @abstractmethod
    def append_timestamps(
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        """Append timestamps and return a new waveform timing if needed."""
        raise NotImplementedError

    @abstractmethod
    def append_timing(
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        """Append timing and return a new waveform timing if needed."""
        raise NotImplementedError
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_irregular.py sha256=7ed6a3a60ff660d85e53e1e42a50f68789e8844d8cb165ba7ca4393e873a1b1f bytes=5619 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/_irregular.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/_irregular.py`
- sha256: `7ed6a3a60ff660d85e53e1e42a50f68789e8844d8cb165ba7ca4393e873a1b1f`
- bytes: 5619

````python
from __future__ import annotations

from collections.abc import Iterable, Sequence
from enum import Enum
from typing import TYPE_CHECKING, final

from nitypes._arguments import validate_unsupported_arg
from nitypes._exceptions import invalid_arg_type
from nitypes.time._types import ANY_DATETIME_TUPLE
from nitypes.waveform._exceptions import create_sample_interval_mode_mismatch_error
from nitypes.waveform._timing._sample_interval._base import SampleIntervalStrategy
from nitypes.waveform._timing._sample_interval._mode import SampleIntervalMode
from nitypes.waveform.errors import TimingMismatchError
from nitypes.waveform.typing import (
    TSampleInterval_co,
    TTimeOffset_co,
    TTimestamp,
    TTimestamp_co,
)

if TYPE_CHECKING:
    from nitypes.waveform._timing._timing import Timing  # circular import


class _Direction(Enum):
    INCREASING = -1
    UNKNOWN = 0
    DECREASING = 1


def _are_timestamps_monotonic(timestamps: Sequence[TTimestamp_co]) -> bool:
    direction = _Direction.UNKNOWN
    for i in range(1, len(timestamps)):
        comparison = _get_direction(timestamps[i - 1], timestamps[i])
        if comparison == _Direction.UNKNOWN:
            continue

        if direction == _Direction.UNKNOWN:
            direction = comparison
        elif comparison != direction:
            return False
    return True


def _get_direction(left: TTimestamp, right: TTimestamp) -> _Direction:
    # Work around https://github.com/python/mypy/issues/18203
    if left < right:  # type: ignore[operator]
        return _Direction.INCREASING
    if right < left:  # type: ignore[operator]
        return _Direction.DECREASING
    return _Direction.UNKNOWN


@final
class IrregularSampleIntervalStrategy(
    SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]
):
    """Implements SampleIntervalMode.IRREGULAR specific behavior."""

    def validate_init_args(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        sample_interval_mode: SampleIntervalMode,
        timestamp: TTimestamp_co | None,
        time_offset: TTimeOffset_co | None,
        sample_interval: TSampleInterval_co | None,
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> None:
        validate_unsupported_arg("timestamp", timestamp)
        validate_unsupported_arg("time offset", time_offset)
        validate_unsupported_arg("sample interval", sample_interval)
        if not isinstance(timestamps, Sequence) or not all(
            isinstance(ts, ANY_DATETIME_TUPLE) for ts in timestamps
        ):
            raise invalid_arg_type("timestamps", "sequence of datetime objects", timestamps)
        if not _are_timestamps_monotonic(timestamps):
            raise ValueError("The timestamps must be in ascending or descending order.")

    def get_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        start_index: int,
        count: int,
    ) -> Iterable[TTimestamp_co]:
        assert timing._timestamps is not None
        if count > len(timing._timestamps):
            raise ValueError("The count must be less than or equal to the number of timestamps.")
        return timing._timestamps[start_index : start_index + count]

    def append_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        assert timing._timestamps is not None

        if timestamps is None:
            raise TimingMismatchError(
                "The timestamps argument is required when appending to a waveform with irregular timing."
            )

        datetime_type = type(timing._timestamps[0]) if timing._timestamps else ANY_DATETIME_TUPLE
        if not all(isinstance(ts, datetime_type) for ts in timestamps):
            raise TypeError(
                "The timestamp data type must match the timing information of the current waveform."
            )

        if len(timestamps) == 0:
            return timing
        else:
            if not isinstance(timestamps, list):
                timestamps = list(timestamps)

            return timing.__class__.create_with_irregular_interval(timing._timestamps + timestamps)

    def append_timing(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        if other._sample_interval_mode != SampleIntervalMode.IRREGULAR:
            raise create_sample_interval_mode_mismatch_error()

        assert timing._timestamps is not None and other._timestamps is not None

        if len(timing._timestamps) == 0:
            return other
        elif len(other._timestamps) == 0:
            return timing
        else:
            # The constructor will verify that the combined list of timestamps is monotonic. This is
            # not optimal for a large number of appends.
            return timing.__class__.create_with_irregular_interval(
                timing._timestamps + other._timestamps
            )
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_mode.py sha256=8148c886b9712bccce11fe025cb3dd032e72d4cdc3333b843b8bdf1d472ebb46 bytes=339 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/_mode.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/_mode.py`
- sha256: `8148c886b9712bccce11fe025cb3dd032e72d4cdc3333b843b8bdf1d472ebb46`
- bytes: 339

````python
from __future__ import annotations

from enum import Enum


class SampleIntervalMode(Enum):
    """The sample interval mode that specifies how the waveform is sampled."""

    NONE = 0
    """No sample interval."""

    REGULAR = 1
    """Regular sample interval."""

    IRREGULAR = 2
    """Irregular sample interval."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_none.py sha256=0c00a96886347739ebbf180cd6f11b97a21b0e6a0803557a5cd8dbf133fd70c2 bytes=3472 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/_none.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/_none.py`
- sha256: `0c00a96886347739ebbf180cd6f11b97a21b0e6a0803557a5cd8dbf133fd70c2`
- bytes: 3472

````python
from __future__ import annotations

import warnings
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, final

from nitypes._arguments import validate_unsupported_arg
from nitypes._exceptions import add_note, invalid_arg_type
from nitypes.time._types import ANY_DATETIME_TUPLE, ANY_TIMEDELTA_TUPLE
from nitypes.waveform._exceptions import (
    create_no_timestamp_information_error,
    create_sample_interval_mode_mismatch_error,
)
from nitypes.waveform._timing._sample_interval._base import SampleIntervalStrategy
from nitypes.waveform._timing._sample_interval._mode import SampleIntervalMode
from nitypes.waveform._warnings import sample_interval_mismatch
from nitypes.waveform.typing import TSampleInterval_co, TTimeOffset_co, TTimestamp_co

if TYPE_CHECKING:
    from nitypes.waveform._timing._timing import Timing  # circular import


@final
class NoneSampleIntervalStrategy(
    SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]
):
    """Implements SampleIntervalMode.NONE specific behavior."""

    def validate_init_args(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        sample_interval_mode: SampleIntervalMode,
        timestamp: TTimestamp_co | None,
        time_offset: TTimeOffset_co | None,
        sample_interval: TSampleInterval_co | None,
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> None:
        if not isinstance(timestamp, (ANY_DATETIME_TUPLE, type(None))):
            raise invalid_arg_type("timestamp", "datetime or None", timestamp)
        if not isinstance(time_offset, (ANY_TIMEDELTA_TUPLE, type(None))):
            raise invalid_arg_type("time offset", "timedelta or None", time_offset)
        validate_unsupported_arg("sample interval", sample_interval)
        validate_unsupported_arg("timestamps", timestamps)

    def get_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        start_index: int,
        count: int,
    ) -> Iterable[TTimestamp_co]:
        raise create_no_timestamp_information_error()

    def append_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        try:
            validate_unsupported_arg("timestamps", timestamps)
        except (TypeError, ValueError) as e:
            add_note(e, f"Sample interval mode: {timing.sample_interval_mode}")
            raise
        return timing

    def append_timing(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        if other._sample_interval_mode not in (SampleIntervalMode.NONE, SampleIntervalMode.REGULAR):
            raise create_sample_interval_mode_mismatch_error()
        if timing._sample_interval != other._sample_interval:
            warnings.warn(sample_interval_mismatch())
        return timing
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_regular.py sha256=7565325368505061ef0979238b08a25d3952ac0ba7ca0d70a3e81e46b732fdaf bytes=4300 -->
## FILE: src/nitypes/waveform/_timing/_sample_interval/_regular.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_sample_interval/_regular.py`
- sha256: `7565325368505061ef0979238b08a25d3952ac0ba7ca0d70a3e81e46b732fdaf`
- bytes: 4300

````python
from __future__ import annotations

import warnings
from collections.abc import Generator, Iterable, Sequence
from typing import TYPE_CHECKING, cast, final

from nitypes._arguments import validate_unsupported_arg
from nitypes._exceptions import add_note, invalid_arg_type
from nitypes.time._types import ANY_DATETIME_TUPLE, ANY_TIMEDELTA_TUPLE
from nitypes.waveform._exceptions import (
    create_no_timestamp_information_error,
    create_sample_interval_mode_mismatch_error,
)
from nitypes.waveform._timing._sample_interval._base import SampleIntervalStrategy
from nitypes.waveform._timing._sample_interval._mode import SampleIntervalMode
from nitypes.waveform._warnings import sample_interval_mismatch
from nitypes.waveform.typing import TSampleInterval_co, TTimeOffset_co, TTimestamp_co

if TYPE_CHECKING:
    from nitypes.waveform._timing._timing import Timing  # circular import


@final
class RegularSampleIntervalStrategy(
    SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]
):
    """Implements SampleIntervalMode.REGULAR specific behavior."""

    def validate_init_args(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        sample_interval_mode: SampleIntervalMode,
        timestamp: TTimestamp_co | None,
        time_offset: TTimeOffset_co | None,
        sample_interval: TSampleInterval_co | None,
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> None:
        if not isinstance(timestamp, (ANY_DATETIME_TUPLE, type(None))):
            raise invalid_arg_type("timestamp", "datetime or None", timestamp)
        if not isinstance(time_offset, (ANY_TIMEDELTA_TUPLE, type(None))):
            raise invalid_arg_type("time offset", "timedelta or None", time_offset)
        if not isinstance(sample_interval, ANY_TIMEDELTA_TUPLE):
            raise invalid_arg_type("sample interval", "timedelta", sample_interval)
        validate_unsupported_arg("timestamps", timestamps)

    def get_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        start_index: int,
        count: int,
    ) -> Iterable[TTimestamp_co]:
        if timing.has_timestamp:
            return self._generate_regular_timestamps(timing, start_index, count)
        raise create_no_timestamp_information_error()

    def _generate_regular_timestamps(
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        start_index: int,
        count: int,
    ) -> Generator[TTimestamp_co]:
        sample_interval = timing.sample_interval
        # Work around https://github.com/python/mypy/issues/18203
        timestamp = timing.start_time + start_index * sample_interval  # type: ignore[operator]
        for i in range(count):
            if i != 0:
                timestamp += sample_interval  # type: ignore[operator]
            yield cast(TTimestamp_co, timestamp)

    def append_timestamps(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        timestamps: Sequence[TTimestamp_co] | None,
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        try:
            validate_unsupported_arg("timestamps", timestamps)
        except (TypeError, ValueError) as e:
            add_note(e, f"Sample interval mode: {timing.sample_interval_mode}")
            raise
        return timing

    def append_timing(  # noqa: D102 - Missing docstring in public method - override
        self,
        timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
        other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co],
    ) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]:
        if other._sample_interval_mode not in (SampleIntervalMode.NONE, SampleIntervalMode.REGULAR):
            raise create_sample_interval_mode_mismatch_error()
        if timing._sample_interval != other._sample_interval:
            warnings.warn(sample_interval_mismatch())
        return timing
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_timing/_timing.py sha256=91ca1d128c0f5bbc5c327fcfc226940cc444d4976e21921dceb2adbb6eb09cac bytes=15832 -->
## FILE: src/nitypes/waveform/_timing/_timing.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_timing/_timing.py`
- sha256: `91ca1d128c0f5bbc5c327fcfc226940cc444d4976e21921dceb2adbb6eb09cac`
- bytes: 15832

````python
from __future__ import annotations

import datetime as dt
import operator
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, ClassVar, Generic, SupportsIndex, cast, final

import hightime as ht
from typing_extensions import Self

import nitypes.bintime as bt
from nitypes._exceptions import add_note
from nitypes.time import convert_datetime, convert_timedelta
from nitypes.waveform._timing._sample_interval import (
    SampleIntervalStrategy,
    create_sample_interval_strategy,
)
from nitypes.waveform.typing import (
    TOtherSampleInterval,
    TOtherTimeOffset,
    TOtherTimestamp,
    TSampleInterval,
    TSampleInterval_co,
    TTimeOffset,
    TTimeOffset_co,
    TTimestamp,
    TTimestamp_co,
)

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import SampleIntervalMode

else:
    from nitypes.waveform._timing._sample_interval import SampleIntervalMode


@final
class Timing(Generic[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]):
    """Waveform timing information.

    Waveform timing objects are immutable.
    """

    empty: ClassVar[Timing[dt.datetime, dt.timedelta, dt.timedelta]]
    """A waveform timing object with no timestamp, time offset, or sample interval."""

    # The typing for these named constructors is tricky:
    # - They can't use covariant type variables as parameter types. Instead, they use the
    #   non-covariant type variables, which are distinct. See
    #   https://github.com/python/mypy/issues/6178
    # - ``cls`` is implicitly ``type[Timing[_TTimestamp_co, _TTimeOffset_co, _TSampleInterval_co]]``
    #   and its type variables may already be solved. For example, we can infer the type of ``cls``
    #   from ``my_timing`` in ``my_timing.__class__.create_with_no_interval()``.
    # - Construct the object with ``Timing(...)`` not ``cls(...)`` to avoid conflicts between the
    #   the class's type variables and the argument type variables.
    # - For type variables that are not inferred from arguments, use the covariant type variables so
    #   that ``my_timing.__class__.create_with_no_interval()`` matches the type of ``my_timing``.

    @classmethod
    def create_with_no_interval(
        cls,
        timestamp: TTimestamp | None = None,
        time_offset: TTimeOffset | None = None,
    ) -> Timing[TTimestamp, TTimeOffset, TSampleInterval_co]:
        """Create a waveform timing object with no sample interval.

        Args:
            timestamp: A timestamp representing the start of an acquisition or a related
                occurrence.
            time_offset: The time difference between the timestamp and the time that the first
                sample was acquired.

        Returns:
            A waveform timing object.
        """
        return Timing(SampleIntervalMode.NONE, timestamp, time_offset)

    @classmethod
    def create_with_regular_interval(
        cls,
        sample_interval: TSampleInterval,
        timestamp: TTimestamp | None = None,
        time_offset: TTimeOffset | None = None,
    ) -> Timing[TTimestamp, TTimeOffset, TSampleInterval]:
        """Create a waveform timing object with a regular sample interval.

        Args:
            sample_interval: The time difference between samples.
            timestamp: A timestamp representing the start of an acquisition or a related
                occurrence.
            time_offset: The time difference between the timestamp and the time that the first
                sample was acquired.

        Returns:
            A waveform timing object.
        """
        return Timing(SampleIntervalMode.REGULAR, timestamp, time_offset, sample_interval)

    @classmethod
    def create_with_irregular_interval(
        cls,
        timestamps: Sequence[TTimestamp],
    ) -> Timing[TTimestamp, TTimeOffset_co, TSampleInterval_co]:
        """Create a waveform timing object with an irregular sample interval.

        Args:
            timestamps: A sequence containing a timestamp for each sample in the waveform,
                specifying the time that the sample was acquired.

        Returns:
            A waveform timing object.
        """
        return Timing(SampleIntervalMode.IRREGULAR, timestamps=timestamps)

    __slots__ = [
        "_sample_interval_strategy",
        "_sample_interval_mode",
        "_timestamp",
        "_time_offset",
        "_sample_interval",
        "_timestamps",
        "__weakref__",
    ]

    _sample_interval_strategy: SampleIntervalStrategy[
        TTimestamp_co, TTimeOffset_co, TSampleInterval_co
    ]
    _sample_interval_mode: SampleIntervalMode
    _timestamp: TTimestamp_co | None
    _time_offset: TTimeOffset_co | None
    _sample_interval: TSampleInterval_co | None
    _timestamps: list[TTimestamp_co] | None

    def __init__(
        self,
        sample_interval_mode: SampleIntervalMode,
        timestamp: TTimestamp_co | None = None,
        time_offset: TTimeOffset_co | None = None,
        sample_interval: TSampleInterval_co | None = None,
        timestamps: Sequence[TTimestamp_co] | None = None,
        *,
        copy_timestamps: bool = True,
    ) -> None:
        """Initialize a new waveform timing object.

        Args:
            sample_interval_mode: The sample interval mode of the waveform timing.
            timestamp: The timestamp of the waveform timing. This argument is optional for
                SampleIntervalMode.NONE and SampleIntervalMode.REGULAR and unsupported for
                SampleIntervalMode.IRREGULAR.
            time_offset: The time difference between the timestamp and the first sample. This
                argument is optional for SampleIntervalMode.NONE and SampleIntervalMode.REGULAR and
                unsupported for SampleIntervalMode.IRREGULAR.
            sample_interval: The time interval between samples. This argument is required for
                SampleIntervalMode.REGULAR and unsupported otherwise.
            timestamps: A sequence containing a timestamp for each sample in the waveform,
                specifying the time that the sample was acquired. This argument is required for
                SampleIntervalMode.IRREGULAR and unsupported otherwise.
            copy_timestamps: Specifies whether to copy the timestamps or take ownership.

        Most applications should use the named constructors instead:
        * :any:`create_with_no_interval`
        * :any:`create_with_regular_interval`
        * :any:`create_with_irregular_interval`
        """
        sample_interval_strategy = create_sample_interval_strategy(sample_interval_mode)
        try:
            sample_interval_strategy.validate_init_args(
                self, sample_interval_mode, timestamp, time_offset, sample_interval, timestamps
            )
        except (TypeError, ValueError) as e:
            add_note(e, f"Sample interval mode: {sample_interval_mode}")
            raise

        if timestamps is not None and (copy_timestamps or not isinstance(timestamps, list)):
            timestamps = list(timestamps)

        self._sample_interval_strategy = sample_interval_strategy
        self._sample_interval_mode = sample_interval_mode
        self._timestamp = timestamp
        self._time_offset = time_offset
        self._sample_interval = sample_interval
        self._timestamps = timestamps

    @property
    def has_timestamp(self) -> bool:
        """Indicates whether the waveform timing has a timestamp."""
        return self._timestamp is not None

    @property
    def timestamp(self) -> TTimestamp_co:
        """A timestamp representing the start of an acquisition or a related occurrence."""
        value = self._timestamp
        if value is None:
            raise RuntimeError("The waveform timing does not have a timestamp.")
        return value

    @property
    def has_start_time(self) -> bool:
        """Indicates whether the waveform timing has a start_time."""
        return self.has_timestamp

    @property
    def start_time(self) -> TTimestamp_co:
        """The time that the first sample in the waveform was acquired.

        This is equivalent to ``t0`` in a LabVIEW waveform.
        This value is derived from :attr:`timestamp` + :attr:`time_offset`.
        """
        value = self.timestamp
        if self.has_time_offset:
            # Work around https://github.com/python/mypy/issues/18203
            value += self.time_offset  # type: ignore[arg-type,operator]
        return value  # type: ignore[reportReturnType,unused-ignore]

    @property
    def has_time_offset(self) -> bool:
        """Indicates whether the waveform timing has a time offset."""
        return self._time_offset is not None

    @property
    def time_offset(self) -> TTimeOffset_co:
        """The time difference between the timestamp and the first sample."""
        value = self._time_offset
        if value is None:
            raise RuntimeError("The waveform timing does not have a time offset.")
        return value

    @property
    def has_sample_interval(self) -> bool:
        """Indicates whether the waveform timing has a sample interval."""
        return self._sample_interval is not None

    @property
    def sample_interval(self) -> TSampleInterval_co:
        """The time interval between samples.

        This is equivalent to ``dt`` in a LabVIEW waveform.
        """
        value = self._sample_interval
        if value is None:
            raise RuntimeError("The waveform timing does not have a sample interval.")
        return value

    @property
    def sample_interval_mode(self) -> SampleIntervalMode:
        """The sample interval mode that specifies how the waveform is sampled."""
        return self._sample_interval_mode

    def get_timestamps(
        self, start_index: SupportsIndex, count: SupportsIndex
    ) -> Iterable[TTimestamp_co]:
        """Retrieve the timestamps of the waveform samples.

        Args:
            start_index: The sample index of the first timestamp to retrieve.
            count: The number of timestamps to retrieve.

        Returns:
            An iterable containing the requested timestamps.
        """
        start_index = operator.index(start_index)
        count = operator.index(count)

        if start_index < 0:
            raise ValueError("The sample index must be a non-negative integer.")
        if count < 0:
            raise ValueError("The count must be a non-negative integer.")

        return self._sample_interval_strategy.get_timestamps(self, start_index, count)

    def to_bintime(self) -> Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta]:
        """Convert the timing information to use :any:`nitypes.bintime`."""
        return self._convert(bt.DateTime, bt.TimeDelta, bt.TimeDelta)

    def to_datetime(self) -> Timing[dt.datetime, dt.timedelta, dt.timedelta]:
        """Convert the timing information to use :class:`DateTime`."""
        return self._convert(dt.datetime, dt.timedelta, dt.timedelta)

    def to_hightime(self) -> Timing[ht.datetime, ht.timedelta, ht.timedelta]:
        """Convert the timing information to use :any:`hightime`."""
        return self._convert(ht.datetime, ht.timedelta, ht.timedelta)

    def _convert(
        self,
        timestamp_type: type[TOtherTimestamp],
        time_offset_type: type[TOtherTimeOffset],
        sample_interval_type: type[TOtherSampleInterval],
    ) -> Timing[TOtherTimestamp, TOtherTimeOffset, TOtherSampleInterval]:
        # If the runtime type is correct, cast to the requested static type. Not a workaround.
        if (
            isinstance(self._timestamp, (timestamp_type, type(None)))
            and isinstance(self._time_offset, (time_offset_type, type(None)))
            and isinstance(self._sample_interval, (sample_interval_type, type(None)))
            and (
                self._timestamps is None
                or all(isinstance(ts, timestamp_type) for ts in self._timestamps)
            )
        ):
            return cast(Timing[TOtherTimestamp, TOtherTimeOffset, TOtherSampleInterval], self)

        return Timing(
            self._sample_interval_mode,
            None if self._timestamp is None else convert_datetime(timestamp_type, self._timestamp),
            (
                None
                if self._time_offset is None
                else convert_timedelta(time_offset_type, self._time_offset)
            ),
            (
                None
                if self._sample_interval is None
                else convert_timedelta(sample_interval_type, self._sample_interval)
            ),
            (
                None
                if self._timestamps is None
                else [convert_datetime(timestamp_type, ts) for ts in self._timestamps]
            ),
        )

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return (
            self._timestamp == value._timestamp
            and self._time_offset == value._time_offset
            and self._sample_interval == value._sample_interval
            and self._sample_interval_mode == value._sample_interval_mode
            and self._timestamps == value._timestamps
        )

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (
            self._sample_interval_mode,
            self._timestamp,
            self._time_offset,
            self._sample_interval,
            self._timestamps,
        )
        ctor_kwargs: dict[str, Any] = {}
        if self._timestamps is not None:
            ctor_kwargs["copy_timestamps"] = False
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        # For Enum, __str__ is an unqualified ctor expression like E.V and __repr__ is <E.V: 0>.
        args = [f"{self.sample_interval_mode.__class__.__module__}.{self.sample_interval_mode}"]
        if self._timestamp is not None:
            args.append(f"timestamp={self._timestamp!r}")
        if self._time_offset is not None:
            args.append(f"time_offset={self._time_offset!r}")
        if self._sample_interval is not None:
            args.append(f"sample_interval={self._sample_interval!r}")
        if self._timestamps is not None:
            args.append(f"timestamps={self._timestamps!r}")
        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"

    def _append_timestamps(self, timestamps: Sequence[TTimestamp_co] | None) -> Self:
        new_timing = self._sample_interval_strategy.append_timestamps(self, timestamps)
        assert isinstance(new_timing, self.__class__)
        return new_timing

    def _append_timing(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            raise TypeError(
                "The input waveform(s) must have the same waveform timing type as the current waveform."
            )

        new_timing = self._sample_interval_strategy.append_timing(self, other)
        assert isinstance(new_timing, self.__class__)
        return new_timing


Timing.empty = Timing(SampleIntervalMode.NONE)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_types.py sha256=f4cbf48d93e95f8933fb9e35440779833644377d5b863f609b80218ea567999e bytes=344 -->
## FILE: src/nitypes/waveform/_types.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_types.py`
- sha256: `f4cbf48d93e95f8933fb9e35440779833644377d5b863f609b80218ea567999e`
- bytes: 344

````python
from __future__ import annotations

import numpy as np

from nitypes._numpy import bool as _np_bool

DIGITAL_PORT_DTYPES = (np.uint8, np.uint16, np.uint32)
"""Tuple of types corresponding to :any:`AnyDigitalPort`."""

DIGITAL_STATE_DTYPES = (_np_bool, np.int8, np.uint8)
"""Tuple of types corresponding to :any:`AnyDigitalState`."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/_warnings.py sha256=f63c68cb3fd1ec087520b6f7aaf6f079d644dd9b138c1a9f31fcfacf56d1133d bytes=750 -->
## FILE: src/nitypes/waveform/_warnings.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/_warnings.py`
- sha256: `f63c68cb3fd1ec087520b6f7aaf6f079d644dd9b138c1a9f31fcfacf56d1133d`
- bytes: 750

````python
from __future__ import annotations

from nitypes.waveform.warnings import TimingMismatchWarning, ScalingMismatchWarning


def sample_interval_mismatch() -> TimingMismatchWarning:
    """Create a TimingMismatchWarning about appending waveforms with mismatched sample intervals."""
    return TimingMismatchWarning(
        "The sample interval of one or more waveforms does not match the sample interval of the current waveform."
    )


def scale_mode_mismatch() -> ScalingMismatchWarning:
    """Create a ScalingMismatchwarning about appending waveforms with mismatched scale modes."""
    return ScalingMismatchWarning(
        "The scale mode of one or more waveforms does not match the scale mode of the current waveform."
    )
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/errors.py sha256=5b6a8a140d0ad960c2d0769d92cbb9afe779551cd0c00253c33ee1e1502431f7 bytes=1324 -->
## FILE: src/nitypes/waveform/errors.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/errors.py`
- sha256: `5b6a8a140d0ad960c2d0769d92cbb9afe779551cd0c00253c33ee1e1502431f7`
- bytes: 1324

````python
"""Custom error classes for waveforms."""

from __future__ import annotations


class TimingMismatchError(RuntimeError):
    """Exception used when appending waveforms with mismatched timing."""

    pass


class CapacityMismatchError(ValueError):
    """An error for an invalid capacity."""

    pass


class CapacityTooSmallError(ValueError):
    """An error for an invalid capacity argument."""

    pass


class DatatypeMismatchError(TypeError):
    """An error for a data type mismatch."""

    pass


class IrregularTimestampCountMismatchError(ValueError):
    """An error for an irregular timestamp count mismatch."""

    pass


class StartIndexTooLargeError(ValueError):
    """An error for an invalid start index argument."""

    pass


class StartIndexOrSampleCountTooLargeError(ValueError):
    """An error for an invalid start index or sample count argument."""

    pass


class NoTimestampInformationError(RuntimeError):
    """An error for waveform timing with no timestamp information."""

    pass


class SampleIntervalModeMismatchError(TimingMismatchError):
    """An error for mixing none/regular with irregular timing."""

    pass


class SignalCountMismatchError(ValueError):
    """An error for a mismatched signal count."""

    pass
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/typing.py sha256=1f78c04a3fd1125bbedd62e19e36fb0ece54eae710f7d40d655ad864ae538447 bytes=2868 -->
## FILE: src/nitypes/waveform/typing.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/typing.py`
- sha256: `1f78c04a3fd1125bbedd62e19e36fb0ece54eae710f7d40d655ad864ae538447`
- bytes: 2868

````python
"""Type aliases and type variables for waveforms."""

# These types are in a submodule so they don't show up in autocomplete for "nitypes.waveform." and
# overwhelm users.

from __future__ import annotations

import datetime as dt
from typing import Union

import numpy as np
from typing_extensions import TypeAlias, TypeVar

from nitypes._numpy import bool as _np_bool
from nitypes.time.typing import AnyDateTime, AnyTimeDelta

ExtendedPropertyValue: TypeAlias = Union[bool, float, int, str]
"""Type alias for an ExtendedPropertyDictionary value.

This type alias is a union of the following types:

* :class:`bool`
* :class:`float`
* :class:`int`
* :class:`str`
"""

AnyDigitalPort: TypeAlias = Union[np.uint8, np.uint16, np.uint32]
"""Type alias for any digital port data type.

This type alias is a union of the following types:

* :class:`numpy.uint8`
* :class:`numpy.uint16`
* :class:`numpy.uint32`
"""

# np.byte == np.int8, np.ubyte == np.uint8
AnyDigitalState: TypeAlias = Union[_np_bool, np.int8, np.uint8]
"""Type alias for any digital state data type.

This type alias is a union of the following types:

* :class:`numpy.bool` (NumPy 2.x) or :class:`numpy.bool_` (NumPy 1.x)
* :class:`numpy.int8`
* :class:`numpy.uint8`
"""

TDigitalState = TypeVar("TDigitalState", bound=AnyDigitalState)
"""Type variable with a bound of :any:`AnyDigitalState`."""

TOtherDigitalState = TypeVar("TOtherDigitalState", bound=AnyDigitalState)
"""Another type variable with a bound of :any:`AnyDigitalState`."""

TTimestamp = TypeVar("TTimestamp", bound=AnyDateTime, default=dt.datetime)
"""Type variable for a timestamp."""

TTimestamp_co = TypeVar(
    "TTimestamp_co",
    bound=AnyDateTime,
    covariant=True,
    default=dt.datetime,
)
"""Covariant type variable for a timestamp."""

TTimeOffset = TypeVar(
    "TTimeOffset",
    bound=AnyTimeDelta,
    default=dt.timedelta,
)
"""Type variable for a time offset."""

TTimeOffset_co = TypeVar(
    "TTimeOffset_co",
    bound=AnyTimeDelta,
    covariant=True,
    default=dt.timedelta,
)
"""Covariant type variable for a time offset."""

TSampleInterval = TypeVar(
    "TSampleInterval",
    bound=AnyTimeDelta,
    default=dt.timedelta,
)
"""Type variable for a sample interval."""

TSampleInterval_co = TypeVar(
    "TSampleInterval_co",
    bound=AnyTimeDelta,
    covariant=True,
    default=dt.timedelta,
)
"""Covariant type variable for a sample interval."""

TOtherTimestamp = TypeVar("TOtherTimestamp", bound=AnyDateTime)
"""Another type variable for a timestamp."""

TOtherTimeOffset = TypeVar("TOtherTimeOffset", bound=AnyTimeDelta)
"""Another type variable for a time offset."""

TOtherSampleInterval = TypeVar("TOtherSampleInterval", bound=AnyTimeDelta)
"""Another type variable for a sample interval."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/waveform/warnings.py sha256=f40943e3eabd1a008ae21e001d3f5c8dd5c204be2765427f533f4de9ce3cd7a9 bytes=379 -->
## FILE: src/nitypes/waveform/warnings.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/waveform/warnings.py`
- sha256: `f40943e3eabd1a008ae21e001d3f5c8dd5c204be2765427f533f4de9ce3cd7a9`
- bytes: 379

````python
"""Custom warning classes for waveforms."""

from __future__ import annotations


class ScalingMismatchWarning(RuntimeWarning):
    """Warning used when appending waveforms with mismatched scaling information."""

    pass


class TimingMismatchWarning(RuntimeWarning):
    """Warning used when appending waveforms with mismatched timing information."""

    pass
````

<!--NI_OSS_SOURCE repo=nitypes-python path=src/nitypes/xy_data.py sha256=33486b31f0e9fcf63eb281400ba1b20d3fe92009cceed380bbcd2c7fab231183 bytes=15508 -->
## FILE: src/nitypes/xy_data.py

- repository: `ni/nitypes-python`
- source_path: `src/nitypes/xy_data.py`
- sha256: `33486b31f0e9fcf63eb281400ba1b20d3fe92009cceed380bbcd2c7fab231183`
- bytes: 15508

````python
"""XYData type for NI Python APIs.

XYData Data Type
=================
:class:`XYData`: An XYData object represents two axes (sequences) of numeric values with units
information. Valid types for the numeric values are :any:`int` and :any:`float`.
"""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Generic, Union, overload

import numpy as np
import numpy.typing as npt
from typing_extensions import Self, TypeVar, final

from nitypes._arguments import validate_dtype
from nitypes._exceptions import invalid_arg_type, invalid_array_ndim
from nitypes._numpy import asarray as _np_asarray, long as _np_long, ulong as _np_ulong
from nitypes.waveform._exceptions import create_datatype_mismatch_error
from nitypes.waveform.typing import ExtendedPropertyValue

if sys.version_info < (3, 10):
    import array as std_array

if TYPE_CHECKING:
    # Import from the public package so the docs don't reference private submodules.
    from nitypes.waveform import ExtendedPropertyDictionary
else:
    from nitypes.waveform._extended_properties import ExtendedPropertyDictionary

# Extended property keys for X and Y units.
_UNIT_DESCRIPTION_X = "NI_UnitDescription_X"
_UNIT_DESCRIPTION_Y = "NI_UnitDescription_Y"

TData = TypeVar("TData", bound=Union[np.floating, np.integer])
TOtherData = TypeVar("TOtherData", bound=Union[np.floating, np.integer])

# Use the C types here because np.isdtype() considers some of them to be distinct types, even when
# they have the same size (e.g. np.intc vs. np.int_).
_DATA_DTYPES = (
    # Floating point
    np.single,
    np.double,
    # Signed integers
    np.byte,
    np.short,
    np.intc,
    np.int_,
    _np_long,
    np.longlong,
    # Unsigned integers
    np.ubyte,
    np.ushort,
    np.uintc,
    np.uint,
    _np_ulong,
    np.ulonglong,
)


@final
class XYData(Generic[TData]):
    """Two axes (sequences) of numeric values with units information.

    Constructing
    ^^^^^^^^^^^^

    To construct an XYData object, use the :class:`XYData` class:

    >>> XYData(np.array([1.1], np.float64), np.array([4.1], np.float64))
    nitypes.xy_data.XYData(x_data=array([1.1]), y_data=array([4.1]))
    >>> XYData(np.array([1, 2]), np.array([4, 5]), x_units="A", y_units="V")
    nitypes.xy_data.XYData(x_data=array([1, 2]), y_data=array([4, 5]), x_units='A', y_units='V')

    To construct an XYData object using built-in lists, use from_arrays_1d():

    >>> XYData.from_arrays_1d([1, 2], [5, 6], np.int32)
    nitypes.xy_data.XYData(x_data=array([1, 2], dtype=int32), y_data=array([5, 6], dtype=int32))
    >>> XYData.from_arrays_1d([1.0, 1.1], [1.2, 1.3], np.float64)
    nitypes.xy_data.XYData(x_data=array([1. , 1.1]), y_data=array([1.2, 1.3]))
    """

    __slots__ = [
        "_x_data",
        "_y_data",
        "_extended_properties",
    ]

    _x_data: npt.NDArray[TData]
    _y_data: npt.NDArray[TData]
    _extended_properties: ExtendedPropertyDictionary

    @overload
    @classmethod
    def from_arrays_1d(
        cls,
        x_array: npt.NDArray[TOtherData],
        y_array: npt.NDArray[TOtherData],
        dtype: None = ...,
        *,
        x_units: str = ...,
        y_units: str = ...,
        copy: bool = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> XYData[TOtherData]: ...

    @overload
    @classmethod
    def from_arrays_1d(
        cls,
        x_array: npt.NDArray[Any] | Sequence[Any],
        y_array: npt.NDArray[Any] | Sequence[Any],
        dtype: type[TOtherData] | np.dtype[TOtherData],
        *,
        x_units: str = ...,
        y_units: str = ...,
        copy: bool = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> XYData[TOtherData]: ...

    @overload
    @classmethod
    def from_arrays_1d(
        cls,
        x_array: npt.NDArray[Any] | Sequence[Any],
        y_array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = ...,
        *,
        x_units: str = ...,
        y_units: str = ...,
        copy: bool = ...,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = ...,
    ) -> XYData[Any]: ...

    @classmethod
    def from_arrays_1d(
        cls,
        x_array: npt.NDArray[Any] | Sequence[Any],
        y_array: npt.NDArray[Any] | Sequence[Any],
        dtype: npt.DTypeLike | None = None,
        *,
        x_units: str = "",
        y_units: str = "",
        copy: bool = True,
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
    ) -> XYData[Any]:
        """Construct an XYData from two one-dimensional arrays or sequences.

        Args:
            x_array: The x-axis data as a one-dimensional array or a sequence.
            y_array: The y-axis data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the XYdata axes. This argument is required
                when x_array and y_array are sequences.
            x_units: The units string associated with x_array.
            y_units: The units string associated with y_array
            copy: Specifies whether to copy the arrays or save references to them.
            extended_properties: The extended properties of the XYData.

        Returns:
            An XYData object containing the specified data.
        """
        if isinstance(x_array, np.ndarray):
            if x_array.ndim != 1:
                raise invalid_array_ndim(
                    "input array", "one-dimensional array or sequence", x_array.ndim
                )
        elif isinstance(x_array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(x_array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "one-dimensional array or sequence", x_array)

        if isinstance(y_array, np.ndarray):
            if y_array.ndim != 1:
                raise invalid_array_ndim(
                    "input array", "one-dimensional array or sequence", y_array.ndim
                )
        elif isinstance(y_array, Sequence) or (
            sys.version_info < (3, 10) and isinstance(y_array, std_array.array)
        ):
            if dtype is None:
                raise ValueError("You must specify a dtype when the input array is a sequence.")
        else:
            raise invalid_arg_type("input array", "one-dimensional array or sequence", y_array)

        return cls(
            x_data=_np_asarray(x_array, dtype, copy=copy),
            y_data=_np_asarray(y_array, dtype, copy=copy),
            x_units=x_units,
            y_units=y_units,
            extended_properties=extended_properties,
        )

    def __init__(
        self: XYData[TOtherData],
        x_data: npt.NDArray[TOtherData],
        y_data: npt.NDArray[TOtherData],
        *,
        x_units: str = "",
        y_units: str = "",
        extended_properties: Mapping[str, ExtendedPropertyValue] | None = None,
        copy_extended_properties: bool = True,
    ) -> None:
        """Initialize a new XYData.

        Args:
            x_data: A NumPy ndarray to use for x-axis data storage. The XYData takes ownership
                of this array. If not specified, an ndarray is created based on the specified
                dtype and capacity.
            y_data: A NumPy ndarray to use for y-axis data storage. The XYData takes ownership
                of this array. If not specified, an ndarray is created based on the specified
                dtype and capacity.
            x_units: The units string associated with x_data.
            y_units: The units string associated with y_data.
            extended_properties: The extended properties of the XYData.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            An XYData object.
        """
        if x_data.dtype != y_data.dtype:
            raise TypeError("x_data and y_data must have the same type.")

        if isinstance(x_data, np.ndarray) and isinstance(y_data, np.ndarray):
            self._init_with_provided_arrays(
                x_data,
                y_data,
                x_data.dtype,
            )
        else:
            raise invalid_arg_type("raw data", "NumPy ndarray", x_data)

        if copy_extended_properties or not isinstance(
            extended_properties, ExtendedPropertyDictionary
        ):
            extended_properties = ExtendedPropertyDictionary(extended_properties)
        self._extended_properties = extended_properties

        # If x_units are not already in extended properties, set them.
        if _UNIT_DESCRIPTION_X not in self._extended_properties:
            self._extended_properties[_UNIT_DESCRIPTION_X] = x_units
        elif x_units and x_units != self._extended_properties.get(_UNIT_DESCRIPTION_X):
            raise ValueError(
                "The specified x_units input does not match the units specified in "
                "extended_properties."
            )

        # If y_units are not already in extended properties, set them.
        if _UNIT_DESCRIPTION_Y not in self._extended_properties:
            self._extended_properties[_UNIT_DESCRIPTION_Y] = y_units
        elif y_units and y_units != self._extended_properties.get(_UNIT_DESCRIPTION_Y):
            raise ValueError(
                "The specified y_units input does not match the units specified in "
                "extended_properties."
            )

    def _init_with_provided_arrays(
        self,
        x_data: npt.NDArray[TData],
        y_data: npt.NDArray[TData],
        dtype: npt.DTypeLike | None = None,
    ) -> None:
        if not isinstance(x_data, np.ndarray):
            raise invalid_arg_type("x-axis input array", "one-dimensional array", x_data)
        if not isinstance(y_data, np.ndarray):
            raise invalid_arg_type("y-axis input array", "one-dimensional array", y_data)
        if x_data.ndim != 1:
            raise invalid_array_ndim("x-axis input array", "one-dimensional array", x_data.ndim)
        if y_data.ndim != 1:
            raise invalid_array_ndim("y-axis input array", "one-dimensional array", y_data.ndim)
        if len(x_data) != len(y_data):
            raise ValueError("x_data and y_data must be the same length.")

        if dtype is None:
            if x_data.dtype != y_data.dtype:
                raise TypeError("x_data and y_data must be the same type.")
            dtype = x_data.dtype

        validate_dtype(dtype, _DATA_DTYPES)
        if dtype != x_data.dtype:
            raise create_datatype_mismatch_error(
                "input array", x_data.dtype, "requested", np.dtype(dtype)
            )
        if dtype != y_data.dtype:
            raise create_datatype_mismatch_error(
                "input array", y_data.dtype, "requested", np.dtype(dtype)
            )

        self._x_data = x_data
        self._y_data = y_data

    @property
    def x_data(self) -> npt.NDArray[TData]:
        """The x-axis data of this XYData."""
        return self._x_data

    @property
    def y_data(self) -> npt.NDArray[TData]:
        """The y-axis data of this XYData."""
        return self._y_data

    @property
    def x_units(self) -> str:
        """The unit of measurement, such as volts, of x_data."""
        value = self._extended_properties.get(_UNIT_DESCRIPTION_X, "")
        assert isinstance(value, str)
        return value

    @x_units.setter
    def x_units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("x_units", "str", value)
        self._extended_properties[_UNIT_DESCRIPTION_X] = value

    @property
    def y_units(self) -> str:
        """The unit of measurement, such as volts, of y_data."""
        value = self._extended_properties.get(_UNIT_DESCRIPTION_Y, "")
        assert isinstance(value, str)
        return value

    @y_units.setter
    def y_units(self, value: str) -> None:
        if not isinstance(value, str):
            raise invalid_arg_type("y_units", "str", value)
        self._extended_properties[_UNIT_DESCRIPTION_Y] = value

    @property
    def dtype(self) -> np.dtype[TData]:
        """The NumPy dtype for the XYData."""
        return self._x_data.dtype

    @property
    def extended_properties(self) -> ExtendedPropertyDictionary:
        """The extended properties for the XYData.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        """
        return self._extended_properties

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        if not isinstance(value, self.__class__):
            return NotImplemented
        return (
            np.array_equal(self.x_data, value.x_data)
            and np.array_equal(self.y_data, value.y_data)
            and self.x_units == value.x_units
            and self.y_units == value.y_units
        )

    def __reduce__(self) -> tuple[Any, ...]:
        """Return object state for pickling."""
        ctor_args = (self._x_data, self._y_data)
        ctor_kwargs: dict[str, Any] = {
            "extended_properties": self._extended_properties,
            "copy_extended_properties": False,
        }
        return (self.__class__._unpickle, (ctor_args, ctor_kwargs))

    @classmethod
    def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self:
        return cls(*args, **kwargs)

    def __repr__(self) -> str:
        """Return repr(self)."""
        args = [f"x_data={self.x_data!r}", f"y_data={self.y_data!r}"]

        if self.x_units:
            args.append(f"x_units={self.x_units!r}")

        if self.y_units:
            args.append(f"y_units={self.y_units!r}")

        # Only display the extended properties if non-units entries are specified.
        if any(
            key
            for key in self.extended_properties.keys()
            if key not in [_UNIT_DESCRIPTION_X, _UNIT_DESCRIPTION_Y]
        ):
            args.append(f"extended_properties={self.extended_properties!r}")

        return f"{self.__class__.__module__}.{self.__class__.__name__}({', '.join(args)})"

    def __str__(self) -> str:
        """Return str(self)."""
        x_str = XYData._format_values_with_units(self.x_data, self.x_units)
        y_str = XYData._format_values_with_units(self.y_data, self.y_units)
        return f"[{x_str}, {y_str}]"

    @staticmethod
    def _format_values_with_units(values: npt.NDArray[TData], units: str) -> str:
        if units:
            values_with_units = [f"{value} {units}" for value in values]
            values_str = ", ".join(values_with_units)
        else:
            values_without_units = [f"{value}" for value in values]
            values_str = ", ".join(values_without_units)

        return f"[{values_str}]"
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/__init__.py sha256=1c651a0958d972493de06b0b0231946e63de946660436fc8202bf4fe86fed106 bytes=38 -->
## FILE: tests/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/__init__.py`
- sha256: `1c651a0958d972493de06b0b0231946e63de946660436fc8202bf4fe86fed106`
- bytes: 38

````python
"""Tests for the nitypes package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/acceptance/__init__.py sha256=9ee50f74fd05c3c7d6aa3e9898414970eca269c2f2d2e6ad4d8f4cc28cafb3da bytes=49 -->
## FILE: tests/acceptance/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/acceptance/__init__.py`
- sha256: `9ee50f74fd05c3c7d6aa3e9898414970eca269c2f2d2e6ad4d8f4cc28cafb3da`
- bytes: 49

````python
"""Acceptance tests for the nitypes package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/acceptance/waveform/__init__.py sha256=3006c868c8899b2242858ebfcd919725b18c64290119e32691bb6911b376fea0 bytes=58 -->
## FILE: tests/acceptance/waveform/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/acceptance/waveform/__init__.py`
- sha256: `3006c868c8899b2242858ebfcd919725b18c64290119e32691bb6911b376fea0`
- bytes: 58

````python
"""Acceptance tests for the nitypes.waveform package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/acceptance/waveform/test_memmap.py sha256=d5084d9fd55eeeb8ac8c6218b00e741e53b9cca4842e35681cc69a24aa2d4c84 bytes=2575 -->
## FILE: tests/acceptance/waveform/test_memmap.py

- repository: `ni/nitypes-python`
- source_path: `tests/acceptance/waveform/test_memmap.py`
- sha256: `d5084d9fd55eeeb8ac8c6218b00e741e53b9cca4842e35681cc69a24aa2d4c84`
- bytes: 2575

````python
from __future__ import annotations

import struct
from pathlib import Path

import numpy as np
import pytest

from nitypes.waveform import AnalogWaveform


@pytest.mark.parametrize("copy", [False, True])
def test___memmap_array_1d___create_waveform_from_array___waveform_contains_memmap_data(
    tmp_path: Path, copy: bool
) -> None:
    memmap_path = tmp_path / "memmap_array.bin"
    memmap_path.write_bytes(struct.pack("4d", 1.23, -4.56, 7e89, 1e-23))
    memmap_array = np.memmap(memmap_path, np.float64)

    waveform = AnalogWaveform.from_array_1d(memmap_array, copy=copy)

    assert list(waveform.raw_data) == [1.23, -4.56, 7e89, 1e-23]


@pytest.mark.parametrize("copy", [False, True])
def test___memmap_array_2d___create_waveforms_from_array___waveforms_contains_memmap_data(
    tmp_path: Path, copy: bool
) -> None:
    memmap_path = tmp_path / "memmap_array.bin"
    memmap_path.write_bytes(struct.pack("6d", 1.23, -4.56, 7e89, 1e-23, 456.0, 7.89))
    memmap_array = np.memmap(memmap_path, np.float64, shape=(2, 3))

    waveforms = AnalogWaveform.from_array_2d(memmap_array, copy=copy)

    assert len(waveforms) == 2
    assert list(waveforms[0].raw_data) == [1.23, -4.56, 7e89]
    assert list(waveforms[1].raw_data) == [1e-23, 456.0, 7.89]


def test___memmap_waveform___append___waveform_writes_to_memmap(tmp_path: Path) -> None:
    memmap_path = tmp_path / "memmap_array.bin"
    memmap_array = np.memmap(memmap_path, np.float64, "w+", shape=10)
    waveform = AnalogWaveform.from_array_1d(memmap_array, copy=False, sample_count=0)

    waveform.append(np.array([1.23, -4.56, 7e89, 1e-23]))
    memmap_array.flush()

    memmap_bytes = memmap_path.read_bytes()
    memmap_data = struct.unpack_from("4d", memmap_bytes)
    assert memmap_data == (1.23, -4.56, 7e89, 1e-23)


def test___memmap_waveforms___append___waveforms_write_to_memmap(tmp_path: Path) -> None:
    memmap_path = tmp_path / "memmap_array.bin"
    memmap_array = np.memmap(memmap_path, np.float64, "w+", shape=(2, 10))
    waveforms = AnalogWaveform.from_array_2d(memmap_array, copy=False, sample_count=0)

    waveforms[0].append(np.array([1.23, -4.56, 7e89]))
    waveforms[1].append(np.array([1e-23, 456.0, 7.89]))
    memmap_array.flush()

    memmap_bytes = memmap_path.read_bytes()
    memmap_data0 = struct.unpack_from("3d", memmap_bytes, offset=0)
    memmap_data1 = struct.unpack_from("3d", memmap_bytes, offset=80)
    assert memmap_data0 == (1.23, -4.56, 7e89)
    assert memmap_data1 == (1e-23, 456.0, 7.89)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/__init__.py sha256=563282a5e4a673437c7870f838b29568b8adc9496d5bf60cb6c0f4f92a26b16a bytes=43 -->
## FILE: tests/benchmark/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/__init__.py`
- sha256: `563282a5e4a673437c7870f838b29568b8adc9496d5bf60cb6c0f4f92a26b16a`
- bytes: 43

````python
"""Benchmarks for the nitypes package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/bintime/__init__.py sha256=b8dc75e999f016603a8832604839f9c7a9c1da7af66da6dc7914cc00656a2596 bytes=51 -->
## FILE: tests/benchmark/bintime/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/bintime/__init__.py`
- sha256: `b8dc75e999f016603a8832604839f9c7a9c1da7af66da6dc7914cc00656a2596`
- bytes: 51

````python
"""Benchmarks for the nitypes.bintime package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/bintime/test_datetime.py sha256=446da4a2cd56db658c24ddb5aaae68e4ed35f1f323c99a2e6072ca84f668e8a9 bytes=3370 -->
## FILE: tests/benchmark/bintime/test_datetime.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/bintime/test_datetime.py`
- sha256: `446da4a2cd56db658c24ddb5aaae68e4ed35f1f323c99a2e6072ca84f668e8a9`
- bytes: 3370

````python
from __future__ import annotations

import datetime as dt
import operator

import hightime as ht
import pytest
from pytest_benchmark.fixture import BenchmarkFixture

import nitypes.bintime as bt


# Note: constructing bt.DateTime from a fixed date is slow because it creates a
# ht.datetime behind the scenes and then converts it to ticks.
@pytest.mark.benchmark(group="datetime_construct")
def test___bt_datetime___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.DateTime, 2025, 1, 1, tzinfo=dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_construct")
def test___dt_datetime___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(dt.datetime, 2025, 1, 1, tzinfo=dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_construct")
def test___ht_datetime___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(ht.datetime, 2025, 1, 1, tzinfo=dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_construct")
def test___bt_datetime___from_ticks(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.DateTime.from_ticks, 1 << 60 | 1 << 31)


@pytest.mark.benchmark(group="datetime_construct")
def test___bt_datetime___from_tuple(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.DateTime.from_tuple, bt.TimeValueTuple(1 << 28, 1 << 31))


@pytest.mark.benchmark(group="datetime_now")
def test___bt_datetime___now(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.DateTime.now, dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_now")
def test___dt_datetime___now(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(dt.datetime.now, dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_now")
def test___ht_datetime___now(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(ht.datetime.now, dt.timezone.utc)


@pytest.mark.benchmark(group="datetime_lt")
def test___bt_datetime___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.DateTime.now(dt.timezone.utc)
    t2 = bt.DateTime.now(dt.timezone.utc)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="datetime_lt")
def test___dt_datetime___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.datetime.now(dt.timezone.utc)
    t2 = dt.datetime.now(dt.timezone.utc)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="datetime_lt")
def test___ht_datetime___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.datetime.now(dt.timezone.utc)
    t2 = ht.datetime.now(dt.timezone.utc)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="datetime_add")
def test___bt_datetime___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.DateTime.now(dt.timezone.utc)
    t2 = bt.TimeDelta(1e-3)
    benchmark(operator.add, t1, t2)


@pytest.mark.benchmark(group="datetime_add")
def test___dt_datetime___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.datetime.now(dt.timezone.utc)
    t2 = dt.timedelta(milliseconds=1)
    benchmark(operator.add, t1, t2)


@pytest.mark.benchmark(group="datetime_add")
def test___ht_datetime___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.datetime.now(dt.timezone.utc)
    t2 = ht.timedelta(milliseconds=1)
    benchmark(operator.add, t1, t2)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/bintime/test_datetime_array.py sha256=a234eae2797937d9d6a418b31c3bf457c60c511374de4e3409e9808f4dc03837 bytes=1771 -->
## FILE: tests/benchmark/bintime/test_datetime_array.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/bintime/test_datetime_array.py`
- sha256: `a234eae2797937d9d6a418b31c3bf457c60c511374de4e3409e9808f4dc03837`
- bytes: 1771

````python
from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pytest
from pytest_benchmark.fixture import BenchmarkFixture

import nitypes.bintime as bt


LIST_1 = [bt.DateTime.from_offset(bt.TimeDelta(0.3))]
LIST_10 = [bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 10, 0.3)]
LIST_100 = [
    bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 100, 0.3)
]
LIST_1000 = [
    bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 1000, 0.3)
]
LIST_10000 = [
    bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 10000, 0.3)
]

FAST_CASES = (LIST_1,)
BIG_O_CASES = (LIST_1, LIST_10, LIST_100, LIST_1000, LIST_10000)  # Useful for local measurements


benchmark_options: dict[str, Any] = {}
if sys.implementation.name == "pypy":
    # See #182 -- PR/CI workflows spend too much time on PyPy benchmarks
    benchmark_options["warmup"] = False
    benchmark_options["min_rounds"] = 1
    benchmark_options["max_time"] = 0.5


@pytest.mark.benchmark(group="datetime_array_construct", **benchmark_options)
@pytest.mark.parametrize("constructor_list", FAST_CASES)
def test___bt_datetime_array___construct(
    benchmark: BenchmarkFixture,
    constructor_list: list[bt.DateTime],
) -> None:
    benchmark(bt.DateTimeArray, constructor_list)


@pytest.mark.benchmark(group="datetime_array_extend", **benchmark_options)
@pytest.mark.parametrize("extend_list", FAST_CASES)
def test___bt_datetime_array___extend(
    benchmark: BenchmarkFixture,
    extend_list: list[bt.DateTime],
) -> None:
    empty_array = bt.DateTimeArray()
    benchmark(empty_array.extend, extend_list)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/bintime/test_timedelta.py sha256=e8dff4f2158c8ffa7c30937210d5204530e9fe2c976242bc5a67a4aec3b6f22e bytes=5053 -->
## FILE: tests/benchmark/bintime/test_timedelta.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/bintime/test_timedelta.py`
- sha256: `e8dff4f2158c8ffa7c30937210d5204530e9fe2c976242bc5a67a4aec3b6f22e`
- bytes: 5053

````python
from __future__ import annotations

import datetime as dt
import operator

import hightime as ht
import pytest
from pytest_benchmark.fixture import BenchmarkFixture

import nitypes.bintime as bt


@pytest.mark.benchmark(group="timedelta_construct")
def test___bt_timedelta___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.TimeDelta, 1e-3)


@pytest.mark.benchmark(group="timedelta_construct")
def test___dt_timedelta___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(dt.timedelta, milliseconds=1)


@pytest.mark.benchmark(group="timedelta_construct")
def test___ht_timedelta___construct(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(ht.timedelta, milliseconds=1)


@pytest.mark.benchmark(group="timedelta_construct")
def test___bt_timedelta___from_ticks(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.TimeDelta.from_ticks, 1 << 60 | 1 << 31)


@pytest.mark.benchmark(group="timedelta_construct")
def test___bt_timedelta___from_tuple(
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(bt.TimeDelta.from_tuple, bt.TimeValueTuple(1 << 28, 1 << 31))


@pytest.mark.benchmark(group="timedelta_eq")
def test___bt_timedelta___eq(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.TimeDelta(1e-3)
    t2 = bt.TimeDelta(2e-3)
    benchmark(operator.eq, t1, t2)


@pytest.mark.benchmark(group="timedelta_eq")
def test___dt_timedelta___eq(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.timedelta(milliseconds=1)
    t2 = dt.timedelta(milliseconds=2)
    benchmark(operator.eq, t1, t2)


@pytest.mark.benchmark(group="timedelta_eq")
def test___ht_timedelta___eq(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.timedelta(milliseconds=1)
    t2 = ht.timedelta(milliseconds=2)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="timedelta_lt")
def test___bt_timedelta___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.TimeDelta(1e-3)
    t2 = bt.TimeDelta(2e-3)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="timedelta_lt")
def test___dt_timedelta___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.timedelta(milliseconds=1)
    t2 = dt.timedelta(milliseconds=2)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="timedelta_lt")
def test___ht_timedelta___lt(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.timedelta(milliseconds=1)
    t2 = ht.timedelta(milliseconds=2)
    benchmark(operator.lt, t1, t2)


@pytest.mark.benchmark(group="timedelta_add")
def test___bt_timedelta___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.TimeDelta(1e-3)
    t2 = bt.TimeDelta(2e-3)
    benchmark(operator.add, t1, t2)


@pytest.mark.benchmark(group="timedelta_add")
def test___dt_timedelta___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.timedelta(milliseconds=1)
    t2 = dt.timedelta(milliseconds=2)
    benchmark(operator.add, t1, t2)


@pytest.mark.benchmark(group="timedelta_add")
def test___ht_timedelta___add(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.timedelta(milliseconds=1)
    t2 = ht.timedelta(milliseconds=2)
    benchmark(operator.add, t1, t2)


@pytest.mark.benchmark(group="timedelta_mul")
def test___bt_timedelta___mul(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = bt.TimeDelta(1e-3)
    t2 = 0.1
    benchmark(operator.mul, t1, t2)


@pytest.mark.benchmark(group="timedelta_mul")
def test___dt_timedelta___mul(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = dt.timedelta(milliseconds=1)
    t2 = 0.1
    benchmark(operator.mul, t1, t2)


@pytest.mark.benchmark(group="timedelta_mul")
def test___ht_timedelta___mul(
    benchmark: BenchmarkFixture,
) -> None:
    t1 = ht.timedelta(milliseconds=1)
    t2 = 0.1
    benchmark(operator.mul, t1, t2)


@pytest.mark.benchmark(group="timedelta_total_seconds")
def test___bt_timedelta___total_seconds(
    benchmark: BenchmarkFixture,
) -> None:
    t = bt.TimeDelta(1e-3)
    benchmark(t.total_seconds)


@pytest.mark.benchmark(group="timedelta_total_seconds")
def test___dt_timedelta___total_seconds(
    benchmark: BenchmarkFixture,
) -> None:
    t = dt.timedelta(milliseconds=1)
    benchmark(t.total_seconds)


@pytest.mark.benchmark(group="timedelta_total_seconds")
def test___ht_timedelta___total_seconds(
    benchmark: BenchmarkFixture,
) -> None:
    t = ht.timedelta(milliseconds=1)
    benchmark(t.total_seconds)


@pytest.mark.benchmark(group="timedelta_total_seconds")
def test___bt_timedelta___precision_total_seconds(
    benchmark: BenchmarkFixture,
) -> None:
    t = bt.TimeDelta(1e-3)
    benchmark(t.precision_total_seconds)


@pytest.mark.benchmark(group="timedelta_total_seconds")
def test___ht_timedelta___precision_total_seconds(
    benchmark: BenchmarkFixture,
) -> None:
    t = ht.timedelta(milliseconds=1)
    benchmark(t.precision_total_seconds)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/benchmark/bintime/test_timedelta_array.py sha256=076f3dc053480f0c593f69273527c6b81fa5e2f1f58b9583caaef2c37680422e bytes=1636 -->
## FILE: tests/benchmark/bintime/test_timedelta_array.py

- repository: `ni/nitypes-python`
- source_path: `tests/benchmark/bintime/test_timedelta_array.py`
- sha256: `076f3dc053480f0c593f69273527c6b81fa5e2f1f58b9583caaef2c37680422e`
- bytes: 1636

````python
from __future__ import annotations

import sys
from typing import Any

import numpy as np
import pytest
from pytest_benchmark.fixture import BenchmarkFixture

import nitypes.bintime as bt


LIST_1 = [bt.TimeDelta(0.3)]
LIST_10 = [bt.TimeDelta(float(value)) for value in np.arange(-10, 10, 0.3)]
LIST_100 = [bt.TimeDelta(float(value)) for value in np.arange(-100, 100, 0.3)]
LIST_1000 = [bt.TimeDelta(float(value)) for value in np.arange(-1000, 1000, 0.3)]
LIST_10000 = [bt.TimeDelta(float(value)) for value in np.arange(-10000, 10000, 0.3)]

FAST_CASES = (LIST_1,)
BIG_O_CASES = (LIST_1, LIST_10, LIST_100, LIST_1000, LIST_10000)  # Useful for local measurements


benchmark_options: dict[str, Any] = {}
if sys.implementation.name == "pypy":
    # See #182 -- PR/CI workflows spend too much time on PyPy benchmarks
    benchmark_options["warmup"] = False
    benchmark_options["min_rounds"] = 1
    benchmark_options["max_time"] = 0.5


@pytest.mark.benchmark(group="timedelta_array_construct", **benchmark_options)
@pytest.mark.parametrize("constructor_list", FAST_CASES)
def test___bt_timedelta_array___construct(
    benchmark: BenchmarkFixture,
    constructor_list: list[bt.TimeDelta],
) -> None:
    benchmark(bt.TimeDeltaArray, constructor_list)


@pytest.mark.benchmark(group="timedelta_array_extend", **benchmark_options)
@pytest.mark.parametrize("extend_list", FAST_CASES)
def test___bt_timedelta_array___extend(
    benchmark: BenchmarkFixture,
    extend_list: list[bt.TimeDelta],
) -> None:
    empty_array = bt.TimeDeltaArray()
    benchmark(empty_array.extend, extend_list)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/__init__.py sha256=7652aba78409d41f0bb56f36a3ecec5afed83303cb56ef7e844a405c9320342e bytes=43 -->
## FILE: tests/unit/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/__init__.py`
- sha256: `7652aba78409d41f0bb56f36a3ecec5afed83303cb56ef7e844a405c9320342e`
- bytes: 43

````python
"""Unit tests for the nitypes package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/bintime/__init__.py sha256=f55ee55f179fa28c76b488301e1a9136663866635f3c98acc19bb56ecb48a2a5 bytes=51 -->
## FILE: tests/unit/bintime/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/bintime/__init__.py`
- sha256: `f55ee55f179fa28c76b488301e1a9136663866635f3c98acc19bb56ecb48a2a5`
- bytes: 51

````python
"""Unit tests for the nitypes.bintime package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/bintime/test_datetime.py sha256=125dd325b723d529628bc5cfc9bc13143f64dadfc7e111cbb569cea37430186c bytes=19998 -->
## FILE: tests/unit/bintime/test_datetime.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/bintime/test_datetime.py`
- sha256: `125dd325b723d529628bc5cfc9bc13143f64dadfc7e111cbb569cea37430186c`
- bytes: 19998

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle

import hightime as ht
import pytest
from typing_extensions import assert_type
from tzlocal import get_localzone

from nitypes.bintime import DateTime, TimeDelta
from nitypes.bintime._time_value_tuple import TimeValueTuple
from nitypes.bintime._timedelta import _BITS_PER_SECOND, _FRACTIONAL_SECONDS_MASK


###############################################################################
# Constructor
###############################################################################
def test___no_args___construct___returns_epoch() -> None:
    value = DateTime()

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert value._offset._ticks == 0


def test___dt_datetime___construct___returns_datetime() -> None:
    # 0.015625 is an exact binary fraction.
    value = DateTime(dt.datetime(2025, 2, 14, 8, 15, 59, 15625, dt.timezone.utc))

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert (
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
    ) == (2025, 2, 14, 8, 15, 59, 15625)


def test___ht_datetime___construct___returns_nearest_datetime() -> None:
    # The microseconds are not exactly representable as a binary fraction, so they are rounded.
    value = DateTime(
        ht.datetime(2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_567_890, dt.timezone.utc)
    )

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert (
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
        value.femtosecond,
        value.yoctosecond,
    ) == (2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_569_278)


def test___unit_args___construct___returns_nearest_datetime() -> None:
    # The microseconds are not exactly representable as a binary fraction, so they are rounded.
    value = DateTime(2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_567_890, dt.timezone.utc)

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert (
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
        value.femtosecond,
        value.yoctosecond,
    ) == (2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_569_278)


def test___naive_dt_datetime___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(dt.datetime(2025, 2, 14, 8, 15, 59, 15625))

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


def test___naive_ht_datetime___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(ht.datetime(2025, 2, 14, 8, 15, 59, 15625))

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


def test___naive_unit_args___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_567_890)

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


def test___local_dt_datetime___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(dt.datetime(2025, 2, 14, 8, 15, 59, 15625, get_localzone()))

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


def test___local_ht_datetime___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(ht.datetime(2025, 2, 14, 8, 15, 59, 15625, tzinfo=get_localzone()))

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


def test___local_unit_args___construct___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = DateTime(2025, 2, 14, 8, 15, 59, 15625, 123_456_789, 234_567_890, get_localzone())

    assert exc.value.args[0].startswith("The tzinfo must be datetime.timezone.utc.")


###############################################################################
# from_ticks
###############################################################################
def test___int_ticks___from_ticks___returns_time_value() -> None:
    value = DateTime.from_ticks(0x12345678_90ABCDEF_FEDCBA09_87654321)

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert value._offset._ticks == 0x12345678_90ABCDEF_FEDCBA09_87654321


###############################################################################
# from_offset
###############################################################################
def test___time_value___from_offset___returns_time_value() -> None:
    value = DateTime.from_offset(TimeDelta.from_ticks(0x12345678_90ABCDEF_FEDCBA09_87654321))

    assert_type(value, DateTime)
    assert isinstance(value, DateTime)
    assert value._offset._ticks == 0x12345678_90ABCDEF_FEDCBA09_87654321


###############################################################################
# year, month, day, hour, minute, second, etc.
###############################################################################
@pytest.mark.parametrize(
    "other, expected",
    [
        (
            ht.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
            (dt.MINYEAR, 1, 1, 0, 0, 0, 0, 0, 0),
        ),
        (
            ht.datetime(
                1850, 12, 25, 8, 15, 30, 123_456, 234_567_789, 345_567_890, dt.timezone.utc
            ),
            (1850, 12, 25, 8, 15, 30, 123_456, 234_567_789, 345_578_196),
        ),
        (
            ht.datetime(
                1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_567_890, dt.timezone.utc
            ),
            (1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_578_196),
        ),
        (
            ht.datetime(1904, 1, 1, 0, 30, 0, 0, 0, 1_000_000, dt.timezone.utc),
            (1904, 1, 1, 0, 30, 0, 0, 0, 975_781),
        ),
        (
            ht.datetime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
            (2000, 1, 1, 0, 0, 0, 0, 0, 0),
        ),
        (
            ht.datetime(
                dt.MAXYEAR,
                12,
                31,
                23,
                59,
                59,
                999_999,
                999_999_999,
                999_000_000,  # with 999_999_999, binary fraction rounding pushes us to MAXYEAR + 1
                dt.timezone.utc,
            ),
            (dt.MAXYEAR, 12, 31, 23, 59, 59, 999_999, 999_999_999, 999_024_218),
        ),
    ],
)
def test___various_values___unit_properties___return_unit_values(
    other: ht.datetime, expected: tuple[int, ...]
) -> None:
    value = DateTime(other)
    assert (
        value.year,
        value.month,
        value.day,
        value.hour,
        value.minute,
        value.second,
        value.microsecond,
        value.femtosecond,
        value.yoctosecond,
    ) == expected


###############################################################################
# Binary arithmetic
###############################################################################
@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            TimeDelta(8 * 3600 + 15 * 60 + 30),
            DateTime(2025, 1, 1, 8, 15, 30, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___time_value___add___returns_datetime(
    left: DateTime, right: TimeDelta, expected: DateTime
) -> None:
    assert_type(left + right, DateTime)
    assert_type(right + left, DateTime)
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.timedelta(hours=8, minutes=15, seconds=30),
            DateTime(2025, 1, 1, 8, 15, 30, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___dt_timedelta___add___returns_datetime(
    left: DateTime, right: dt.timedelta, expected: DateTime
) -> None:
    assert_type(left + right, DateTime)
    assert_type(right + left, DateTime)
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            ht.timedelta(hours=8, minutes=15, seconds=30),
            DateTime(2025, 1, 1, 8, 15, 30, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___ht_timedelta___add___returns_datetime(
    left: DateTime, right: ht.timedelta, expected: DateTime
) -> None:
    assert_type(left + right, DateTime)
    assert_type(right + left, DateTime)
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            DateTime(2025, 1, 1, 8, 15, 30, tzinfo=dt.timezone.utc),
            TimeDelta(8 * 3600 + 15 * 60 + 30),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___time_value___sub___returns_datetime(
    left: DateTime, right: TimeDelta, expected: DateTime
) -> None:
    assert_type(left - right, DateTime)
    assert left - right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            DateTime(2025, 1, 1, 8, 15, 30, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            TimeDelta(8 * 3600 + 15 * 60 + 30),
        ),
    ],
)
def test___datetime___sub___returns_time_value(
    left: DateTime, right: DateTime, expected: TimeDelta
) -> None:
    assert_type(left - right, TimeDelta)
    assert left - right == expected


###############################################################################
# Comparison
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
        (
            dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
        (
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___same_value___comparison___equal(
    left: DateTime | dt.datetime | ht.datetime, right: DateTime | dt.datetime | ht.datetime
) -> None:
    assert not (left < right)
    assert left <= right
    assert left == right
    assert not (left != right)
    assert not (left > right)
    assert left >= right


@pytest.mark.parametrize(
    "left, right",
    [
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.datetime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            ht.datetime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            ht.datetime(2025, 1, 1, femtosecond=1, tzinfo=dt.timezone.utc),
        ),
        (
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            ht.datetime(2025, 1, 1, yoctosecond=1, tzinfo=dt.timezone.utc),
        ),
        (
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc) - ht.timedelta(femtoseconds=1),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ),
        (
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc) - ht.timedelta(yoctoseconds=1),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ),
    ],
)
def test___lesser_value___comparison___lesser(
    left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta
) -> None:
    assert left < right
    assert left <= right
    assert not (left == right)
    assert left != right
    assert not (left > right)
    assert not (left >= right)


###############################################################################
# Miscellaneous
###############################################################################
_VARIOUS_VALUES = [
    DateTime(dt.MINYEAR, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
    DateTime(1850, 12, 25, 8, 15, 30, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
    DateTime(1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
    DateTime(1904, 1, 1, 0, 30, 0, 0, 0, 1_000_000, dt.timezone.utc),
    DateTime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
    DateTime(
        dt.MAXYEAR,
        12,
        31,
        23,
        59,
        59,
        999_999,
        999_999_999,
        999_000_000,  # with 999_999_999, binary fraction rounding pushes us to MAXYEAR + 1
        dt.timezone.utc,
    ),
]


def test___various_values___hash___returns_probably_unique_int() -> None:
    hashes = {hash(x) for x in _VARIOUS_VALUES}
    assert len(hashes) == len(_VARIOUS_VALUES)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_copy(value: DateTime) -> None:
    new_value = copy.copy(value)
    assert new_value is not value
    assert new_value == value


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_copy(value: DateTime) -> None:
    new_value = pickle.loads(pickle.dumps(value))
    assert new_value is not value
    assert new_value == value


def test___time_value___pickle___references_public_modules() -> None:
    value = DateTime()
    value_bytes = pickle.dumps(value)

    assert b"nitypes.bintime" in value_bytes
    assert b"nitypes.bintime._datetime" not in value_bytes
    assert b"nitypes.bintime._time_value" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95W\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x0fnitypes.bintime\x94\x8c\x08DateTime\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\tN\xca\xb9\xf4\xe9\xd3\x9a\x1f\xff\x85\x94R\x94.",
            DateTime(1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
        ),
        (
            b"\x80\x04\x95[\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x0fnitypes.bintime\x94\x8c\x08DateTime\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x92\xb4\x00\x85\x94R\x94.",
            DateTime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: DateTime
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            DateTime.min,
            "0001-01-01 00:00:00+00:00",
        ),
        (
            DateTime(1850, 12, 25, 8, 15, 30, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
            "1850-12-25 08:15:30.123456234567789345578196+00:00",
        ),
        (
            DateTime(1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
            "1903-12-31 23:59:59.123456234567789345578196+00:00",
        ),
        (
            DateTime(1904, 1, 1, 0, 30, 0, 0, 0, 1_000_000, dt.timezone.utc),
            "1904-01-01 00:30:00.000000000000000000975781+00:00",
        ),
        (
            DateTime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
            "2000-01-01 00:00:00+00:00",
        ),
        (
            DateTime.max,
            "9999-12-31 23:59:59.999999999999999999945789+00:00",
        ),
    ],
)
def test___various_values___str___looks_ok(value: TimeDelta, expected: str) -> None:
    assert str(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            DateTime.min,
            "nitypes.bintime.DateTime(1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)",
        ),
        (
            DateTime(1850, 12, 25, 8, 15, 30, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
            "nitypes.bintime.DateTime(1850, 12, 25, 8, 15, 30, 123456, 234567789, 345578196, tzinfo=datetime.timezone.utc)",
        ),
        (
            DateTime(1903, 12, 31, 23, 59, 59, 123_456, 234_567_789, 345_567_890, dt.timezone.utc),
            "nitypes.bintime.DateTime(1903, 12, 31, 23, 59, 59, 123456, 234567789, 345578196, tzinfo=datetime.timezone.utc)",
        ),
        (
            DateTime(1904, 1, 1, 0, 30, 0, 0, 0, 1_000_000, dt.timezone.utc),
            "nitypes.bintime.DateTime(1904, 1, 1, 0, 30, 0, 0, 0, 975781, tzinfo=datetime.timezone.utc)",
        ),
        (
            DateTime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc),
            "nitypes.bintime.DateTime(2000, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)",
        ),
        (
            DateTime.max,
            "nitypes.bintime.DateTime(9999, 12, 31, 23, 59, 59, 999999, 999999999, 999945789, tzinfo=datetime.timezone.utc)",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: TimeDelta, expected: str) -> None:
    assert repr(value) == expected


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___get_ticks___returns_correct_value(seconds: float) -> None:
    ticks = TimeDelta._to_ticks(seconds)
    value = DateTime.from_ticks(ticks)

    assert value.ticks == ticks


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___to_tuple___returns_correct_values(seconds: float) -> None:
    ticks = TimeDelta._to_ticks(seconds)
    value = DateTime.from_ticks(ticks)

    whole_seconds, fractional_seconds = value.to_tuple()
    assert whole_seconds == ticks >> _BITS_PER_SECOND
    assert fractional_seconds == ticks & _FRACTIONAL_SECONDS_MASK


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___from_tuple___datetime_correct(seconds: float) -> None:
    ticks = TimeDelta._to_ticks(seconds)
    whole_seconds = ticks >> _BITS_PER_SECOND
    fractional_seconds = ticks & _FRACTIONAL_SECONDS_MASK

    value = DateTime.from_tuple(TimeValueTuple(whole_seconds, fractional_seconds))

    assert value.ticks == ticks
    assert value.to_tuple() == (whole_seconds, fractional_seconds)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/bintime/test_datetime_array.py sha256=e14cd1899e84e58180b79beca02e4a5f028f302e4fdc717f9f8d87de713892b6 bytes=43785 -->
## FILE: tests/unit/bintime/test_datetime_array.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/bintime/test_datetime_array.py`
- sha256: `e14cd1899e84e58180b79beca02e4a5f028f302e4fdc717f9f8d87de713892b6`
- bytes: 43785

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
from typing import Any, Sequence

import numpy as np
import pytest
from typing_extensions import assert_type

from nitypes.bintime import DateTime, DateTimeArray


###############################################################################
# Constructor
###############################################################################
def test___no_args___construct___returns_empty_array() -> None:
    value = DateTimeArray()

    assert_type(value, DateTimeArray)
    assert isinstance(value, DateTimeArray)
    assert len(value._array) == 0


@pytest.mark.parametrize(
    "constructor_arg",
    (
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ]
        ),
        (
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            )
        ),
    ),
)
def test___sequence_arg___construct___returns_matching_array(
    constructor_arg: Sequence[DateTime],
) -> None:
    value = DateTimeArray(constructor_arg)

    assert_type(value, DateTimeArray)
    assert isinstance(value, DateTimeArray)
    assert len(value._array) == len(constructor_arg)
    assert (value._array[0]["msb"], value._array[0]["lsb"]) == constructor_arg[0].to_tuple()
    assert (value._array[1]["msb"], value._array[1]["lsb"]) == constructor_arg[1].to_tuple()


@pytest.mark.parametrize(
    "constructor_arg",
    (
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc).to_tuple(),
            ]
        ),
        ([True, False]),
        ([1, 2]),
        ([10.0, 20.0]),
        (["abc", "xyz"]),
    ),
)
def test___mixed_arg___construct___raises(constructor_arg: list[Any]) -> None:
    with pytest.raises(TypeError):
        _ = DateTimeArray(constructor_arg)


###############################################################################
# len
###############################################################################
@pytest.mark.parametrize(
    "datetime_list, expected_length",
    (
        (None, 0),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 1),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            2,
        ),
    ),
)
def test___datetime_array___get_len___returns_length(
    datetime_list: list[DateTime] | None, expected_length: int
) -> None:
    value = DateTimeArray(datetime_list)

    length = len(value)

    assert length == expected_length


###############################################################################
# __getitem__
###############################################################################
@pytest.mark.parametrize(
    "datetime_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 0, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            0,
            None,
        ),
        # Last index
        (None, -1, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], -1, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            -1,
            None,
        ),
        # Out of bounds index
        (None, 10, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 10, IndexError()),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            10,
            IndexError(),
        ),
    ),
)
def test___datetime_array___index___returns_datetime(
    datetime_list: list[DateTime], indexer: int, raised_exception: BaseException | None
) -> None:
    value = DateTimeArray(datetime_list)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            _ = value[indexer]
    else:
        entry = value[indexer]
        assert entry == datetime_list[indexer]


def test___datetime_array___slice___returns_slice() -> None:
    value = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
        ]
    )

    selected = value[::2]

    expected = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
        ]
    )
    assert np.array_equal(selected._array, expected._array)


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___invalid_index___raises(indexer: Any) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        _ = value[indexer]


###############################################################################
# __setitem__
###############################################################################
@pytest.mark.parametrize(
    "datetime_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 0, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            0,
            None,
        ),
        # Last index
        (None, -1, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], -1, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            -1,
            None,
        ),
        # Out of bounds index
        (None, 10, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 10, IndexError()),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            10,
            IndexError(),
        ),
    ),
)
def test___datetime_array___set_by_index___updates_array(
    datetime_list: list[DateTime] | None, indexer: int, raised_exception: BaseException | None
) -> None:
    value = DateTimeArray(datetime_list)
    new_entry = DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            value[indexer] = new_entry
    else:
        value[indexer] = new_entry
        assert value[indexer] == new_entry


@pytest.mark.parametrize(
    "indexer, new_entries, expected_result",
    (
        # len(selected entries) == len(incoming entries)
        (  # Replaces one-for-one from list
            slice(1, 4),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
            ],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (  # Replaces one from length-1 list
            slice(3, 4),
            [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (  # With strided selection, replaces one-for-one from same-sized list
            slice(None, None, 2),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
            ],
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
                    DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        # len(selected entries) > len(incoming entries)
        (  # Shrinks array, replacing many from length-2 list
            slice(1, 4),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
            ],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (  # Shrinks array, replacing many from length-1 list
            slice(1, 4),
            [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (  # Shrinks array, deleting when assigning empty list
            slice(1, 4),
            [],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        # len(selected entries) < len(incoming entries)
        (  # Grows array, replacing then inserting when slice is too short for incoming values
            slice(1, 2),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
            ],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (  # Grows array, inserting when slice is empty
            slice(1, 1),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
            ],
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1992, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ),
)
def test___datetime_array___set_by_slice___updates_array(
    indexer: slice, new_entries: Sequence[DateTime], expected_result: DateTimeArray
) -> None:
    value = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
        ]
    )

    value[indexer] = new_entries

    assert np.array_equal(value._array, expected_result._array)


@pytest.mark.parametrize(
    "indexer, new_entries, raised_exception",
    (
        (  # Strided slice is too long for incoming values
            slice(None, None, 2),
            [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)],
            ValueError(),
        ),
        (  # Strided slice is too short for incoming values
            slice(None, None, 4),
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
            ],
            ValueError(),
        ),
        (  # Assigning empty requires step == 1
            slice(None, None, 2),
            [],
            ValueError(),
        ),
        (  # Cannot assign from scalar
            slice(None, None, 2),
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            TypeError(),
        ),
        (
            slice(1, None),
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            TypeError(),
        ),
    ),
)
def test___datetime_array___set_slice_wrong_value___raises(
    indexer: slice, new_entries: Sequence[DateTime] | DateTime, raised_exception: BaseException
) -> None:
    value = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
        ]
    )

    with pytest.raises(type(raised_exception)):
        value[indexer] = new_entries  # type: ignore # validating incompatible types


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___set_invalid_index___raises(indexer: Any) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )
    new_entry = DateTime(1999, 1, 1, tzinfo=dt.timezone.utc)

    with pytest.raises(TypeError):
        value[indexer] = new_entry


@pytest.mark.parametrize(
    "new_entry",
    (
        "0",
        1.0,
        True,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___set_invalid_value___raises(new_entry: Any) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        value[0] = new_entry


@pytest.mark.parametrize(
    "new_entries",
    (
        ["ab", "cd"],
        [1.0, 2.0],
        [True, False],
        [None, None],
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc).to_tuple(),
        ],
    ),
)
def test___datetime_array___set_mixed_slice___raises(new_entries: list[Any]) -> None:
    value = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
        ]
    )

    with pytest.raises(TypeError):
        value[::2] = new_entries


###############################################################################
# __delitem__
###############################################################################
@pytest.mark.parametrize(
    "datetime_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 0, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            0,
            None,
        ),
        # Last index
        (None, -1, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], -1, None),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            -1,
            None,
        ),
        # Out of bounds index
        (None, 10, IndexError()),
        ([DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)], 10, IndexError()),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ],
            10,
            IndexError(),
        ),
    ),
)
def test___datetime_array___delete_by_index___removes_item(
    datetime_list: list[DateTime] | None, indexer: int, raised_exception: BaseException | None
) -> None:
    value = DateTimeArray(datetime_list)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            del value[indexer]
    else:
        modified = datetime_list.copy() if datetime_list else []
        del modified[indexer]
        del value[indexer]
        expected = DateTimeArray(modified)
        assert np.array_equal(value._array, expected._array)


@pytest.mark.parametrize(
    "indexer, expected_result",
    (
        (
            slice(1, 4),
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
        (
            slice(None, None, 2),
            DateTimeArray(
                [
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ),
)
def test___datetime_array___delete_by_slice___removes_items(
    indexer: slice, expected_result: DateTimeArray
) -> None:
    value = DateTimeArray(
        [
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 4, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 5, tzinfo=dt.timezone.utc),
        ]
    )

    del value[indexer]

    assert np.array_equal(value._array, expected_result._array)


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___delete_invalid_index___raises(indexer: Any) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        del value[indexer]


###############################################################################
# insert
###############################################################################
@pytest.mark.parametrize(
    "initial_value, index",
    (
        # Empty array
        (None, 0),
        (None, 1),
        (None, 3),
        (None, 10),
        (None, -1),
        (None, -2),
        (None, -10),
        # Existing entries
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            0,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            1,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            3,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            10,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            -1,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            -3,
        ),
        (
            [
                DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
            ],
            -10,
        ),
    ),
)
def test___datetime_array___insert_value___inserts(
    initial_value: list[DateTime] | None, index: int
) -> None:
    value = DateTimeArray(initial_value)
    inserted_value = DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)

    value.insert(index, inserted_value)

    expected_value = initial_value.copy() if initial_value else []
    expected_value.insert(index, inserted_value)
    expected = DateTimeArray(expected_value)
    assert np.array_equal(value._array, expected._array)


@pytest.mark.parametrize(
    "index",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___insert_invalid_index___raises(index: int) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        value.insert(index, DateTime(1990, 1, 1, tzinfo=dt.timezone.utc))


@pytest.mark.parametrize(
    "value",
    (
        "0",
        1.0,
        True,
        None,
        [1, 2, 3],
    ),
)
def test___datetime_array___insert_invalid_value___raises(value: Any) -> None:
    value = DateTimeArray(
        [DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        value.insert(0, value)


###############################################################################
# MutableSequence
###############################################################################
@pytest.mark.parametrize(
    "array, item, expected_count",
    (
        (
            DateTimeArray(
                [
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            0,
        ),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            1,
        ),
        (
            DateTimeArray(
                [
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            2,
        ),
    ),
)
def test___datetime_array___count___returns_matching_count(
    array: DateTimeArray, item: DateTime, expected_count: int
) -> None:
    item_count = array.count(item)

    assert item_count == expected_count


@pytest.mark.parametrize(
    "array, item, expected_index",
    (
        (
            DateTimeArray(
                [
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            0,
        ),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            1,
        ),
    ),
)
def test___datetime_array___index___returns_matching_index(
    array: DateTimeArray, item: DateTime, expected_index: int
) -> None:
    item_index = array.index(item)

    assert item_index == expected_index


def test___datetime_array_no_item___index___raises() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(ValueError):
        _ = array.index(DateTime(2000, 1, 1, tzinfo=dt.timezone.utc))


def test___datetime_array___append___adds_to_end() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )
    new_entry = DateTime(2000, 1, 1, tzinfo=dt.timezone.utc)

    array.append(new_entry)

    expected = DateTimeArray(
        [
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
        ]
    )
    assert np.array_equal(array._array, expected._array)


@pytest.mark.parametrize(
    "new_entry",
    (
        (),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([]),
        ([DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)]),
    ),
)
def test___datetime_array___append_invalid_value___raises(new_entry: Any) -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        array.append(new_entry)


@pytest.mark.parametrize(
    "new_entries",
    (
        (),
        ([]),
        ([DateTime(2000, 1, 1, tzinfo=dt.timezone.utc)]),
        (
            [
                DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2001, 1, 1, tzinfo=dt.timezone.utc),
            ]
        ),
        (DateTimeArray()),
        (DateTimeArray([DateTime(2000, 1, 1, tzinfo=dt.timezone.utc)])),
        (
            DateTimeArray(
                [
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2001, 1, 1, tzinfo=dt.timezone.utc),
                ]
            )
        ),
    ),
)
def test___datetime_array___extend___adds_to_end(new_entries: Sequence[DateTime]) -> None:
    original_items = [
        DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
    ]
    array = DateTimeArray(original_items)

    array.extend(new_entries)

    assert len(array) == len(original_items) + len(new_entries)
    separate_items = [*original_items, *new_entries]
    expected_array = DateTimeArray(separate_items)
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "new_entries",
    (
        (),
        ([]),
        ([DateTime(2000, 1, 1, tzinfo=dt.timezone.utc)]),
        (
            [
                DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2001, 1, 1, tzinfo=dt.timezone.utc),
            ]
        ),
        (DateTimeArray()),
        (DateTimeArray([DateTime(2000, 1, 1, tzinfo=dt.timezone.utc)])),
        (
            DateTimeArray(
                [
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2001, 1, 1, tzinfo=dt.timezone.utc),
                ]
            )
        ),
    ),
)
def test___datetime_array___plus_equals___adds_to_end(new_entries: Sequence[DateTime]) -> None:
    original_items = [
        DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
    ]
    array = DateTimeArray(original_items)

    array += new_entries

    assert len(array) == len(original_items) + len(new_entries)
    separate_items = [*original_items, *new_entries]
    expected_array = DateTimeArray(separate_items)
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "new_entries",
    (
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([None]),
        ([True]),
        ([13]),
        ([12.34]),
        (["abc"]),
    ),
)
def test___datetime_array___extend_invalid_values___raises(new_entries: Any) -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        array.extend(new_entries)


@pytest.mark.parametrize(
    "new_entries",
    (
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([None]),
        ([True]),
        ([13]),
        ([12.34]),
        (["abc"]),
    ),
)
def test___datetime_array___plus_equals_invalid_values___raises(new_entries: Any) -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(TypeError):
        array += new_entries


def test___datetime_array___remove___removes_first_match() -> None:
    array = DateTimeArray(
        [
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ]
    )

    array.remove(DateTime(2025, 1, 2, tzinfo=dt.timezone.utc))

    assert len(array) == 2
    expected_array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "item_to_remove",
    (
        (),
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        (DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)),
    ),
)
def test___datetime_array_no_item___remove___raises(item_to_remove: Any) -> None:
    array = DateTimeArray(
        [
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
        ]
    )

    with pytest.raises(ValueError):
        array.remove(item_to_remove)


def test___datetime_array___pop___removes_from_location() -> None:
    original_values = [
        DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
    ]
    array = DateTimeArray(original_values)

    popped = array.pop()
    assert popped == original_values[-1]
    assert len(array) == 2
    assert np.array_equal(
        array._array,
        DateTimeArray(
            [
                DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            ]
        )._array,
    )

    popped = array.pop(0)
    assert popped == DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)
    assert len(array) == 1
    assert np.array_equal(
        array._array, DateTimeArray([DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)])._array
    )


def test___empty_datetime_array___pop___raises() -> None:
    array = DateTimeArray()

    with pytest.raises(IndexError):
        array.pop()


def test___datetime_array___pop_out_of_bounds___raises() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    with pytest.raises(IndexError):
        array.pop(10)


def test___datetime_array___reverse___reverses() -> None:
    original_values = [
        DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
    ]
    array = DateTimeArray(original_values)

    array.reverse()

    expected_order = original_values.copy()
    expected_order.reverse()
    expected_array = DateTimeArray(expected_order)
    assert np.array_equal(array._array, expected_array._array)


def test___datetime_array___clear___empties_array() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    array.clear()

    assert len(array) == 0


def test___datetime_array___iterate___visits_entries() -> None:
    original_values = [
        DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
        DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
    ]
    array = DateTimeArray(original_values)

    iterated = list(iter(array))

    assert original_values == iterated


def test___datetime_array___contains___returns_presence() -> None:
    array = DateTimeArray(
        [
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
        ]
    )

    assert DateTime(2025, 1, 2, tzinfo=dt.timezone.utc) in array
    assert DateTime(2000, 1, 1, tzinfo=dt.timezone.utc) not in array


###############################################################################
# Builtins
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ],
)
def test___same_value___equality___equal(left: DateTimeArray, right: DateTimeArray) -> None:
    assert left == right
    assert right == left


@pytest.mark.parametrize(
    "left, right",
    [
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            DateTimeArray(
                [
                    DateTime(1991, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2001, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: DateTimeArray, right: DateTimeArray
) -> None:
    assert left != right


def test___datetime_array___min___returns_minimum() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    assert min(array) == DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)


def test___datetime_array___max___returns_maximum() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    assert max(array) == DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)


def test___datetime_array___copy___returns_copy() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    copied = copy.copy(array)

    assert array == copied
    assert array is not copied
    assert array._array is not copied._array
    for original_entry, copied_entry in zip(array, copied):
        assert original_entry is not copied_entry


def test___datetime_array___deepcopy___returns_deepcopy() -> None:
    array = DateTimeArray(
        [DateTime(1990, 1, 1, tzinfo=dt.timezone.utc), DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)]
    )

    copied = copy.deepcopy(array)

    assert array == copied
    assert array is not copied
    assert array._array is not copied._array
    for original_entry, copied_entry in zip(array, copied):
        assert original_entry is not copied_entry


@pytest.mark.parametrize(
    "value, expected_str",
    (
        (DateTimeArray(), "[]"),
        (
            DateTimeArray([DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)]),
            "[1990-01-01 00:00:00+00:00]",
        ),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            "[1990-01-01 00:00:00+00:00; 2000-01-01 00:00:00+00:00]",
        ),
        (
            DateTimeArray(
                [
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            "[2000-01-01 00:00:00+00:00; 1990-01-01 00:00:00+00:00; 2025-01-01 00:00:00+00:00]",
        ),
    ),
)
def test___datetime_array___str___looks_ok(value: DateTimeArray, expected_str: str) -> None:
    assert str(value) == expected_str


@pytest.mark.parametrize(
    "value, expected_repr",
    (
        (DateTimeArray(), "nitypes.bintime.DateTimeArray([])"),
        (
            DateTimeArray([DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)]),
            "nitypes.bintime.DateTimeArray([nitypes.bintime.DateTime(1990, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)])",
        ),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            "nitypes.bintime.DateTimeArray([nitypes.bintime.DateTime(1990, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), nitypes.bintime.DateTime(2000, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)])",
        ),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
            "nitypes.bintime.DateTimeArray([nitypes.bintime.DateTime(1990, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), nitypes.bintime.DateTime(2000, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)])",
        ),
    ),
)
def test___datetime_array___repr___looks_ok(value: DateTimeArray, expected_repr: str) -> None:
    assert repr(value) == expected_repr


def test___datetime_array___pickle___references_public_modules() -> None:
    value = DateTimeArray(
        [
            DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
            DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        ]
    )

    pickled = pickle.dumps(value)

    assert b"nitypes.bintime" in pickled
    assert b"nitypes.bintime._datetime_array" not in pickled


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95\xb1\x00\x00\x00\x00\x00\x00\x00\x8c\x0fnitypes.bintime\x94\x8c\rDateTimeArray\x94\x93\x94]\x94(\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94h\x00\x8c\x08DateTime\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x92\xb4\x00\x85\x94R\x94h\x06h\x08h\t\x86\x94R\x94\x8a\r\x00\x00\x00\x00\x00\x00\x00\x00\x00N\xc4\xa1\x00\x85\x94R\x94h\x06h\x08h\t\x86\x94R\x94\x8a\r\x00\x00\x00\x00\x00\x00\x00\x00\x006\x9a\xe3\x00\x85\x94R\x94e\x85\x94R\x94.",
            DateTimeArray(
                [
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: DateTimeArray
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


@pytest.mark.parametrize(
    "value",
    (
        (DateTimeArray()),
        (DateTimeArray([DateTime(1990, 1, 1, tzinfo=dt.timezone.utc)])),
        (
            DateTimeArray(
                [
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                ]
            )
        ),
        (
            DateTimeArray(
                [
                    DateTime(2000, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(1990, 1, 1, tzinfo=dt.timezone.utc),
                    DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                ]
            )
        ),
    ),
)
def test___datetime_array___pickle_unpickle___makes_copy(value: DateTimeArray) -> None:
    new_value: DateTimeArray = pickle.loads(pickle.dumps(value))
    assert new_value == value
    assert new_value is not value
    assert new_value._array is not value._array
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/bintime/test_timedelta.py sha256=58a73a23d4ee5a8c8a414250d44769c18e0dfe7a2cdcb5cd5febdf8d533665df bytes=46619 -->
## FILE: tests/unit/bintime/test_timedelta.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/bintime/test_timedelta.py`
- sha256: `58a73a23d4ee5a8c8a414250d44769c18e0dfe7a2cdcb5cd5febdf8d533665df`
- bytes: 46619

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
import random
from collections.abc import Generator
from decimal import Decimal
from typing import Any

import hightime as ht
import pytest
from typing_extensions import assert_type

from nitypes.bintime import TimeDelta
from nitypes.bintime._time_value_tuple import TimeValueTuple
from nitypes.bintime._timedelta import (
    _BITS_PER_SECOND,
    _FRACTIONAL_SECONDS_MASK,
    _INT128_MAX,
    _INT128_MIN,
    _TICKS_PER_SECOND,
)

_BT_EPSILON = ht.timedelta(yoctoseconds=54210)
_DT_EPSILON = ht.timedelta(microseconds=1)


###############################################################################
# Constructor
###############################################################################
def test___no_args___construct___returns_zero_timedelta() -> None:
    value = TimeDelta()

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert value._ticks == 0


def test___int_seconds___construct___returns_timedelta() -> None:
    value = TimeDelta(0x12345678_90ABCDEF)

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert value._ticks == 0x12345678_90ABCDEF_00000000_00000000


def test___float_seconds___construct___returns_timedelta() -> None:
    value = TimeDelta(123456.789)

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert (value._ticks >> 64) == 123456
    assert (value._ticks & 0xFFFFFFFF_FFFFFFFF) == pytest.approx(0.789 * (1 << 64))


def test___decimal_seconds___construct___returns_timedelta() -> None:
    value = TimeDelta(Decimal("123456.789"))

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert (value._ticks >> 64) == 123456
    assert (value._ticks & 0xFFFFFFFF_FFFFFFFF) == pytest.approx(Decimal("0.789") * (1 << 64))


def test___dt_timedelta___construct___returns_nearest_timedelta() -> None:
    # The microseconds are not exactly representable as a binary fraction, so they are rounded.
    value = TimeDelta(dt.timedelta(days=12345, seconds=23456, microseconds=345_678))

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert (
        value.days,
        value.seconds,
        value.microseconds,
        value.femtoseconds,
        value.yoctoseconds,
    ) == (12345, 23456, 345_677, 999_999_999, 999_972_046)


def test___ht_timedelta___construct___returns_nearest_timedelta() -> None:
    # The yoctoseconds exceed the precision of NI-BTF, so they are rounded.
    value = TimeDelta(
        ht.timedelta(
            days=12345,
            seconds=23456,
            microseconds=345_678,
            femtoseconds=456_789_012,
            yoctoseconds=567_890_123,
        )
    )

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert (
        value.days,
        value.seconds,
        value.microseconds,
        value.femtoseconds,
        value.yoctoseconds,
    ) == (12345, 23456, 345_678, 456_789_012, 567_896_592)


@pytest.mark.parametrize(
    "seconds",
    [
        1 << 63,
        (-1 << 63) - 1,
        # Note that double-precision floating point cannot exactly represent 1<<63.
        1e19,
        -1e19,
        Decimal("9223372036854775808"),
        Decimal("-9223372036854775809"),
    ],
)
def test___out_of_range___construct___raises_overflow_error(seconds: int | float | Decimal) -> None:
    with pytest.raises(OverflowError) as exc:
        _ = TimeDelta(seconds)

    assert exc.value.args[0].startswith("The seconds value is out of range.")


def test___invalid_seconds_type___construct___raises_type_error() -> None:
    with pytest.raises(TypeError) as exc:
        _ = TimeDelta("0")  # type: ignore[call-overload]

    assert exc.value.args[0].startswith("The seconds must be a number or timedelta.")


###############################################################################
# from_ticks
###############################################################################
def test___int_ticks___from_ticks___returns_timedelta() -> None:
    value = TimeDelta.from_ticks(0x12345678_90ABCDEF_FEDCBA09_87654321)

    assert_type(value, TimeDelta)
    assert isinstance(value, TimeDelta)
    assert value._ticks == 0x12345678_90ABCDEF_FEDCBA09_87654321


@pytest.mark.parametrize("ticks", [1 << 127, -(1 << 127) - 1])
def test___out_of_range___from_ticks___raises_overflow_error(ticks: int) -> None:
    with pytest.raises(OverflowError) as exc:
        _ = TimeDelta.from_ticks(ticks)

    assert exc.value.args[0].startswith("The input value is out of range.")


def test___unsupported_type___from_ticks___raises_type_error() -> None:
    with pytest.raises(TypeError) as exc:
        _ = TimeDelta.from_ticks("0")  # type: ignore[arg-type]

    assert exc.value.args[0].startswith("The ticks must be an integer.")


###############################################################################
# days, seconds, microseconds, femtoseconds, yoctoseconds
###############################################################################
@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), (0, 0, 0, 0, 0)),
        (TimeDelta(1), (0, 1, 0, 0, 0)),
        (TimeDelta(60), (0, 60, 0, 0, 0)),
        (TimeDelta(3600), (0, 3600, 0, 0, 0)),
        (TimeDelta(86400), (1, 0, 0, 0, 0)),
        (TimeDelta(86400 * 365), (365, 0, 0, 0, 0)),
        (TimeDelta(86400 * 365 * 100), (36500, 0, 0, 0, 0)),
        (TimeDelta(-1), (-1, 86399, 0, 0, 0)),
        (TimeDelta(-60), (-1, 86400 - 60, 0, 0, 0)),
        (TimeDelta(-3600), (-1, 86400 - 3600, 0, 0, 0)),
        (TimeDelta(-86400), (-1, 0, 0, 0, 0)),
        (TimeDelta(-86400 * 365), (-365, 0, 0, 0, 0)),
        (TimeDelta(-86400 * 365 * 100), (-36500, 0, 0, 0, 0)),
        (TimeDelta(Decimal("0.5")), (0, 0, 500_000, 0, 0)),
        (TimeDelta(Decimal("0.005")), (0, 0, 4_999, 999_999_999, 999_995_663)),
        (TimeDelta(Decimal("0.000_005")), (0, 0, 5, 0, 13_114)),
        (TimeDelta(Decimal("0.000_000_000_000_005")), (0, 0, 0, 5, 15_158)),
        (TimeDelta(Decimal("0.000_000_000_000_000_005")), (0, 0, 0, 0, 4_987_329)),
        (TimeDelta(Decimal("-0.5")), (-1, 86399, 500_000, 0, 0)),
        (TimeDelta(Decimal("-0.005")), (-1, 86399, 995_000, 0, 4_336)),
        (TimeDelta(Decimal("-0.000_005")), (-1, 86399, 999_994, 999_999_999, 999_986_885)),
        (
            TimeDelta(Decimal("-0.000_000_000_000_005")),
            (-1, 86399, 999_999, 999_999_994, 999_984_841),
        ),
        (
            TimeDelta(Decimal("-0.000_000_000_000_000_005")),
            (-1, 86399, 999_999, 999_999_999, 995_012_670),
        ),
    ],
)
def test___various_values___unit_properties___return_unit_values(
    value: TimeDelta, expected: tuple[int, ...]
) -> None:
    assert (
        value.days,
        value.seconds,
        value.microseconds,
        value.femtoseconds,
        value.yoctoseconds,
    ) == expected


###############################################################################
# total_seconds
###############################################################################
@pytest.mark.parametrize(
    "seconds",
    [0.0, 1.0, 3.14159, -3.14159, 1.23456789e18, -1.23456789e18, 1.23456789e-18, -1.23456789e-18],
)
def test___float_seconds___total_seconds___approximate_match(seconds: float) -> None:
    value = TimeDelta(seconds)

    total_seconds = value.total_seconds()

    assert total_seconds == pytest.approx(seconds)


###############################################################################
# precision_total_seconds
###############################################################################
@pytest.mark.parametrize(
    "seconds",
    [
        Decimal("0.0"),
        Decimal("1.0"),
        Decimal("1.23456789e18"),
        Decimal("-1.23456789e18"),
        Decimal("9223372036854775807"),
        Decimal("-9223372036854775808"),
    ],
)
def test___whole_decimal_seconds___precision_total_seconds___exact_match(
    seconds: Decimal,
) -> None:
    value = TimeDelta(seconds)

    total_seconds = value.precision_total_seconds()

    assert total_seconds == seconds


# Decimal is precise, but fixed point "bruises" small values.
@pytest.mark.parametrize(
    "seconds",
    [
        Decimal("3.14159"),
        Decimal("-3.14159"),
        Decimal("1.23456789e-18"),
        Decimal("-1.23456789e-18"),
    ],
)
def test___fractional_decimal_seconds___precision_total_seconds___approximate_match(
    seconds: Decimal,
) -> None:
    value = TimeDelta(seconds)

    total_seconds = value.precision_total_seconds()

    assert total_seconds == pytest.approx(seconds)


@pytest.mark.parametrize(
    "ticks",
    [
        0,
        1,
        -1,
        1 << 64,
        -1 << 64,
        (1 << 64) + 2,
        (-1 << 64) + -2,
        (1 << 124) + (2 << 64) + 3,
        (-1 << 124) + (-2 << 64) + -3,
        0x12345678_12345678_12345678_12345678,
        -0x12345678_12345678_12345678_12345678,
        (1 << 126) + 1,
        (-1 << 126) - 1,
    ],
)
def test___round_trip___precision_total_seconds___exact_match(ticks: int) -> None:
    value = TimeDelta.from_ticks(ticks)

    total_seconds = value.precision_total_seconds()
    round_trip_value = TimeDelta(total_seconds)

    assert round_trip_value._ticks == ticks


def test___random_round_trip___precision_total_seconds___exact_match(
    _random_state: tuple[Any, ...],
) -> None:
    random.seed(1)
    for iteration in range(0, 1000):
        ticks = random.randint(_INT128_MIN, _INT128_MAX)
        value = TimeDelta.from_ticks(ticks)

        total_seconds = value.precision_total_seconds()
        round_trip_value = TimeDelta(total_seconds)

        assert round_trip_value._ticks == ticks


@pytest.fixture
def _random_state() -> Generator[tuple[Any, ...]]:
    state = random.getstate()
    try:
        yield state
    finally:
        random.setstate(state)


###############################################################################
# Unary arithmetic
###############################################################################
@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(-2)),
        (TimeDelta(-2), TimeDelta(2)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
        ),
    ],
)
def test___timedeltas___neg___returns_negation(value: TimeDelta, expected: TimeDelta) -> None:
    assert -value == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(2)),
        (TimeDelta(-2), TimeDelta(-2)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
        ),
    ],
)
def test___timedeltas___pos___returns_identity(value: TimeDelta, expected: TimeDelta) -> None:
    assert +value == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(2)),
        (TimeDelta(-2), TimeDelta(2)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
    ],
)
def test___timedeltas___abs___returns_absolute_value(value: TimeDelta, expected: TimeDelta) -> None:
    assert abs(value) == expected


###############################################################################
# Binary arithmetic
###############################################################################
@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), TimeDelta(0), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(2), TimeDelta(4)),
        (TimeDelta(2), TimeDelta(-2), TimeDelta(0)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((3 << 124) + (4 << 64) + 5),
            TimeDelta.from_ticks((4 << 124) + (6 << 64) + 8),
        ),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((-3 << 124) + (-4 << 64) + -5),
            TimeDelta.from_ticks((-2 << 124) + (-2 << 64) + -2),
        ),
    ],
)
def test___timedeltas___add___returns_sum(
    left: TimeDelta, right: TimeDelta, expected: TimeDelta
) -> None:
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), dt.timedelta(seconds=0), TimeDelta(0)),
        (TimeDelta(2), dt.timedelta(seconds=2), TimeDelta(4)),
        (TimeDelta(2), dt.timedelta(seconds=-2), TimeDelta(0)),
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(seconds=123),
            TimeDelta(Decimal("1_000_000_000_000_123")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            -dt.timedelta(seconds=1),
            TimeDelta(Decimal("999_999_999_999_999")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(microseconds=15625),  # exact binary fraction
            TimeDelta(Decimal("1_000_000_000_000_000.015_625")),
        ),
    ],
)
def test___dt_timedelta___add___returns_sum(
    left: TimeDelta, right: dt.timedelta, expected: TimeDelta
) -> None:
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(microseconds=314159),
            TimeDelta(Decimal("1_000_000_000_000_000.314_159")),
        ),
    ],
)
def test___dt_timedelta_inexact_result___add___returns_approximate_sum(
    left: TimeDelta, right: dt.timedelta, expected: TimeDelta
) -> None:
    assert (left + right).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )
    assert (right + left).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), ht.timedelta(seconds=0), TimeDelta(0)),
        (TimeDelta(2), ht.timedelta(seconds=2), TimeDelta(4)),
        (TimeDelta(2), ht.timedelta(seconds=-2), TimeDelta(0)),
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(seconds=123),
            TimeDelta(Decimal("1_000_000_000_000_123")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            -ht.timedelta(seconds=1),
            TimeDelta(Decimal("999_999_999_999_999")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(microseconds=15625),  # exact binary fraction
            TimeDelta(Decimal("1_000_000_000_000_000.015_625")),
        ),
    ],
)
def test___ht_timedelta___add___returns_sum(
    left: TimeDelta, right: ht.timedelta, expected: TimeDelta
) -> None:
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(femtoseconds=314159),
            TimeDelta(Decimal("1_000_000_000_000_000.000_000_000_314_159")),
        ),
    ],
)
def test___ht_timedelta_inexact_result___add___returns_approximate_sum(
    left: TimeDelta, right: ht.timedelta, expected: TimeDelta
) -> None:
    assert (left + right).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )
    assert (right + left).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (dt.datetime(2025, 1, 1), TimeDelta(0), dt.datetime(2025, 1, 1)),
        (dt.datetime(2025, 1, 1), TimeDelta(2), dt.datetime(2025, 1, 1, 0, 0, 2)),
        (dt.datetime(2025, 1, 1), TimeDelta(-2), dt.datetime(2024, 12, 31, 23, 59, 58)),
    ],
)
def test___dt_datetime___add___returns_sum(
    left: dt.datetime, right: TimeDelta, expected: dt.datetime
) -> None:
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (dt.datetime(2025, 1, 1), TimeDelta(1e-6), dt.datetime(2025, 1, 1, 0, 0, 0, 1)),
        (dt.datetime(2025, 1, 1), TimeDelta(-1e-6), dt.datetime(2024, 12, 31, 23, 59, 59, 999999)),
    ],
)
def test___dt_datetime_inexact_result___add___returns_approximate_sum(
    left: dt.datetime, right: TimeDelta, expected: dt.datetime
) -> None:
    assert abs((left + right) - expected) <= _DT_EPSILON
    assert abs((right + left) - expected) <= _DT_EPSILON


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (ht.datetime(2025, 1, 1), TimeDelta(0), ht.datetime(2025, 1, 1)),
        (ht.datetime(2025, 1, 1), TimeDelta(2), ht.datetime(2025, 1, 1, 0, 0, 2)),
        (ht.datetime(2025, 1, 1), TimeDelta(-2), ht.datetime(2024, 12, 31, 23, 59, 58)),
    ],
)
def test___ht_datetime___add___returns_sum(
    left: ht.datetime, right: TimeDelta, expected: ht.datetime
) -> None:
    assert left + right == expected
    assert right + left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (ht.datetime(2025, 1, 1), TimeDelta(1e-6), ht.datetime(2025, 1, 1, 0, 0, 0, 1)),
        (ht.datetime(2025, 1, 1), TimeDelta(-1e-6), ht.datetime(2024, 12, 31, 23, 59, 59, 999999)),
        (
            ht.datetime(2025, 1, 1),
            TimeDelta(Decimal("1e-15")),
            ht.datetime(2025, 1, 1, 0, 0, 0, 0, 1),
        ),
    ],
)
def test___ht_datetime_inexact_result___add___returns_approximate_sum(
    left: ht.datetime, right: TimeDelta, expected: ht.datetime
) -> None:
    assert abs((left + right) - expected) <= _BT_EPSILON
    assert abs((right + left) - expected) <= _BT_EPSILON


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), TimeDelta(0), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(2), TimeDelta(0)),
        (TimeDelta(2), TimeDelta(-2), TimeDelta(4)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((3 << 124) + (4 << 64) + 5),
            TimeDelta.from_ticks((-2 << 124) + (-2 << 64) + -2),
        ),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((-3 << 124) + (-4 << 64) + -5),
            TimeDelta.from_ticks((4 << 124) + (6 << 64) + 8),
        ),
    ],
)
def test___timedeltas___sub___returns_difference(
    left: TimeDelta, right: TimeDelta, expected: TimeDelta
) -> None:
    assert left - right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), dt.timedelta(seconds=0), TimeDelta(0)),
        (TimeDelta(2), dt.timedelta(seconds=2), TimeDelta(0)),
        (TimeDelta(2), dt.timedelta(seconds=-2), TimeDelta(4)),
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(seconds=123),
            TimeDelta(Decimal("999_999_999_999_877")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            -dt.timedelta(seconds=1),
            TimeDelta(Decimal("1_000_000_000_000_001")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(microseconds=15625),  # exact binary fraction
            TimeDelta(Decimal("999_999_999_999_999.984_375")),
        ),
    ],
)
def test___dt_timedelta___sub___returns_difference(
    left: TimeDelta, right: dt.timedelta, expected: TimeDelta
) -> None:
    assert left - right == expected
    assert right - left == -expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            TimeDelta(Decimal("1e15")),
            dt.timedelta(microseconds=314159),
            TimeDelta(Decimal("999_999_999_999_999.685_841")),
        ),
    ],
)
def test___dt_timedelta_inexact_result___sub___returns_approximate_difference(
    left: TimeDelta, right: dt.timedelta, expected: TimeDelta
) -> None:
    assert (left - right).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )
    assert (right - left).precision_total_seconds() == pytest.approx(
        -expected.precision_total_seconds()
    )


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), ht.timedelta(seconds=0), TimeDelta(0)),
        (TimeDelta(2), ht.timedelta(seconds=2), TimeDelta(0)),
        (TimeDelta(2), ht.timedelta(seconds=-2), TimeDelta(4)),
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(seconds=123),
            TimeDelta(Decimal("999_999_999_999_877")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            -ht.timedelta(seconds=1),
            TimeDelta(Decimal("1_000_000_000_000_001")),
        ),
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(microseconds=15625),  # exact binary fraction
            TimeDelta(Decimal("999_999_999_999_999.984_375")),
        ),
    ],
)
def test___ht_timedelta___sub___returns_difference(
    left: TimeDelta, right: ht.timedelta, expected: TimeDelta
) -> None:
    assert left - right == expected
    assert right - left == -expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (
            TimeDelta(Decimal("1e15")),
            ht.timedelta(femtoseconds=314159),
            TimeDelta(Decimal("999_999_999_999_999.999_999_999_685_800")),
        ),
    ],
)
def test___ht_timedelta_inexact_result___sub___returns_approximate_difference(
    left: TimeDelta, right: ht.timedelta, expected: TimeDelta
) -> None:
    assert (left - right).precision_total_seconds() == pytest.approx(
        expected.precision_total_seconds()
    )
    assert (right - left).precision_total_seconds() == pytest.approx(
        -expected.precision_total_seconds()
    )


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (dt.datetime(2025, 1, 1), TimeDelta(0), dt.datetime(2025, 1, 1)),
        (dt.datetime(2025, 1, 1), TimeDelta(2), dt.datetime(2024, 12, 31, 23, 59, 58)),
        (dt.datetime(2025, 1, 1), TimeDelta(-2), dt.datetime(2025, 1, 1, 0, 0, 2)),
    ],
)
def test___dt_datetime___sub___returns_sum(
    left: dt.datetime, right: TimeDelta, expected: dt.datetime
) -> None:
    assert left - right == expected
    # __sub__(timedelta, datetime) is not supported.


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (dt.datetime(2025, 1, 1), TimeDelta(1e-6), dt.datetime(2024, 12, 31, 23, 59, 59, 999999)),
        (dt.datetime(2025, 1, 1), TimeDelta(-1e-6), dt.datetime(2025, 1, 1, 0, 0, 0, 1)),
    ],
)
def test___dt_datetime_inexact_result___sub___returns_approximate_sum(
    left: dt.datetime, right: TimeDelta, expected: dt.datetime
) -> None:
    assert abs((left - right) - expected) <= _DT_EPSILON
    # __sub__(timedelta, datetime) is not supported.


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (ht.datetime(2025, 1, 1), TimeDelta(0), ht.datetime(2025, 1, 1)),
        (ht.datetime(2025, 1, 1), TimeDelta(2), ht.datetime(2024, 12, 31, 23, 59, 58)),
        (ht.datetime(2025, 1, 1), TimeDelta(-2), ht.datetime(2025, 1, 1, 0, 0, 2)),
    ],
)
def test___ht_datetime___sub___returns_sum(
    left: ht.datetime, right: TimeDelta, expected: ht.datetime
) -> None:
    assert left - right == expected
    # __sub__(timedelta, datetime) is not supported.


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (ht.datetime(2025, 1, 1), TimeDelta(1e-6), ht.datetime(2024, 12, 31, 23, 59, 59, 999999)),
        (ht.datetime(2025, 1, 1), TimeDelta(-1e-6), ht.datetime(2025, 1, 1, 0, 0, 0, 1)),
        (
            ht.datetime(2025, 1, 1),
            TimeDelta(Decimal("1e-15")),
            ht.datetime(2025, 1, 1) - ht.timedelta(femtoseconds=1),
        ),
    ],
)
def test___ht_datetime_inexact_result___sub___returns_approximate_sum(
    left: ht.datetime, right: TimeDelta, expected: ht.datetime
) -> None:
    assert abs((left - right) - expected) <= _BT_EPSILON
    # __sub__(timedelta, datetime) is not supported.


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), 0, TimeDelta(0)),
        (TimeDelta(1), 0, TimeDelta(0)),
        (TimeDelta(1), 1, TimeDelta(1)),
        (TimeDelta(1), -1, TimeDelta(-1)),
        (TimeDelta(100), 200, TimeDelta(20000)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            2,
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
        ),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -3,
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
        ),
    ],
)
def test___int___mul___returns_exact_product(
    left: TimeDelta, right: int, expected: TimeDelta
) -> None:
    assert left * right == expected
    assert right * left == expected


# Verify that multiplying by a float does not reduce the TimeValue's precision.
@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), 0.0, TimeDelta(0)),
        (TimeDelta(1), 0.0, TimeDelta(0)),
        (TimeDelta(1), 1.0, TimeDelta(1)),
        (TimeDelta(1), -1.0, TimeDelta(-1)),
        (TimeDelta(100), 200.0, TimeDelta(20000)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            1.0,
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -1.0,
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
        ),
    ],
)
def test___exact_float___mul___returns_exact_product(
    left: TimeDelta, right: float, expected: TimeDelta
) -> None:
    assert left * right == expected
    assert right * left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(100), 1.23456789, TimeDelta(123.456789)),
        (TimeDelta(1e18), 1.23456789, TimeDelta(1.23456789e18)),
        (TimeDelta(-1e18), 1.23456789, TimeDelta(-1.23456789e18)),
    ],
)
def test___inexact_float___mul___returns_approximate_product(
    left: TimeDelta, right: float, expected: TimeDelta
) -> None:
    assert (left * right).total_seconds() == pytest.approx(expected.total_seconds())
    assert (right * left).total_seconds() == pytest.approx(expected.total_seconds())


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(0), Decimal("0.0"), TimeDelta(0)),
        (TimeDelta(1), Decimal("0.0"), TimeDelta(0)),
        (TimeDelta(1), Decimal("1.0"), TimeDelta(1)),
        (TimeDelta(1), Decimal("-1.0"), TimeDelta(-1)),
        (TimeDelta(100), Decimal("200.0"), TimeDelta(20000)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            Decimal("2.0"),
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
        ),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            Decimal("-3.0"),
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
        ),
        (TimeDelta(100), Decimal("1.23456789"), TimeDelta(Decimal("123.456789"))),
        (TimeDelta(1e18), Decimal("1.23456789"), TimeDelta(Decimal("1.23456789e18"))),
        (TimeDelta(-1e18), Decimal("1.23456789"), TimeDelta(Decimal("-1.23456789e18"))),
    ],
)
def test___decimal___mul___returns_exact_product(
    left: TimeDelta, right: float, expected: TimeDelta
) -> None:
    assert left * right == expected
    assert right * left == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), TimeDelta(1), 1),
        (TimeDelta(20000), TimeDelta(200), 100),
        (
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            2,
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -3,
        ),
    ],
)
def test___timedelta___floordiv___returns_int(
    left: TimeDelta, right: TimeDelta, expected: int
) -> None:
    assert_type(left // right, int)
    assert left // right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), 1, TimeDelta(1)),
        (TimeDelta(20000), 100, TimeDelta(200)),
        (
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
            2,
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            -3,
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
    ],
)
def test___int___floordiv___returns_timedelta(
    left: TimeDelta, right: int, expected: TimeDelta
) -> None:
    assert_type(left // right, TimeDelta)
    assert left // right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), TimeDelta(1), 1.0),
        (TimeDelta(20000), TimeDelta(200), 100.0),
        (TimeDelta(200), TimeDelta(20000), 0.01),
        (
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            2.0,
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -3.0,
        ),
    ],
)
def test___timedelta___truediv___returns_float(
    left: TimeDelta, right: TimeDelta, expected: int
) -> None:
    assert_type(left / right, float)
    assert left / right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), 1.0, TimeDelta(1)),
        (TimeDelta(20000), 100.0, TimeDelta(200)),
        (TimeDelta(200), 0.01, TimeDelta(20000)),
        (
            TimeDelta.from_ticks((2 << 124) + (4 << 64) + 6),
            2.0,
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            -3.0,
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
    ],
)
def test___float___truediv___returns_approximate_timedelta(
    left: TimeDelta, right: float, expected: TimeDelta
) -> None:
    assert_type(left / right, TimeDelta)
    assert (left / right).total_seconds() == pytest.approx(expected.total_seconds())


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), TimeDelta(1), TimeDelta(0)),
        (TimeDelta(20042), TimeDelta(200), TimeDelta(42)),
        (
            TimeDelta.from_ticks((2 << 124) + (5 << 64) + 6),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks(1 << 64),
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks(0),
        ),
    ],
)
def test___timedelta___mod___returns_timedelta(
    left: TimeDelta, right: TimeDelta, expected: TimeDelta
) -> None:
    assert_type(left % right, TimeDelta)
    assert left % right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), dt.timedelta(seconds=1), TimeDelta(0)),
        (TimeDelta(20042), dt.timedelta(seconds=200), TimeDelta(42)),
    ],
)
def test___dt_timedelta___mod___returns_timedelta(
    left: TimeDelta, right: dt.timedelta, expected: TimeDelta
) -> None:
    assert_type(left % right, TimeDelta)
    assert left % right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), ht.timedelta(seconds=1), TimeDelta(0)),
        (TimeDelta(20042), ht.timedelta(seconds=200), TimeDelta(42)),
    ],
)
def test___ht_timedelta___mod___returns_timedelta(
    left: TimeDelta, right: ht.timedelta, expected: TimeDelta
) -> None:
    assert_type(left % right, TimeDelta)
    assert left % right == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), TimeDelta(1), (1, TimeDelta(0))),
        (TimeDelta(20042), TimeDelta(200), (100, TimeDelta(42))),
        (
            TimeDelta.from_ticks((2 << 124) + (5 << 64) + 6),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            (2, TimeDelta.from_ticks(1 << 64)),
        ),
        (
            TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            (-3, TimeDelta.from_ticks(0)),
        ),
    ],
)
def test___timedelta___divmod___returns_int_and_timedelta(
    left: TimeDelta, right: TimeDelta, expected: tuple[int, TimeDelta]
) -> None:
    assert_type(divmod(left, right), tuple[int, TimeDelta])
    assert divmod(left, right) == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), dt.timedelta(seconds=1), (1, TimeDelta(0))),
        (TimeDelta(20042), dt.timedelta(seconds=200), (100, TimeDelta(42))),
    ],
)
def test___dt_timedelta___divmod___returns_int_and_timedelta(
    left: TimeDelta, right: dt.timedelta, expected: tuple[int, TimeDelta]
) -> None:
    assert_type(divmod(left, right), tuple[int, TimeDelta])
    assert divmod(left, right) == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (TimeDelta(1), dt.timedelta(seconds=1), (1, TimeDelta(0))),
        (TimeDelta(20042), dt.timedelta(seconds=200), (100, TimeDelta(42))),
    ],
)
def test___ht_timedelta___divmod___returns_int_and_timedelta(
    left: TimeDelta, right: ht.timedelta, expected: tuple[int, TimeDelta]
) -> None:
    assert_type(divmod(left, right), tuple[int, TimeDelta])
    assert divmod(left, right) == expected


###############################################################################
# Comparison
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (TimeDelta(0), TimeDelta(0)),
        (TimeDelta(1), TimeDelta(1)),
        (TimeDelta(-1), TimeDelta(-1)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            -TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (TimeDelta(1), dt.timedelta(seconds=1)),
        (TimeDelta(1), ht.timedelta(seconds=1)),
        (dt.timedelta(seconds=1), TimeDelta(1)),
        (ht.timedelta(seconds=1), TimeDelta(1)),
    ],
)
def test___same_value___comparison___equal(
    left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta
) -> None:
    assert not (left < right)
    assert left <= right
    assert left == right
    assert not (left != right)
    assert not (left > right)
    assert left >= right


@pytest.mark.parametrize(
    "left, right",
    [
        (TimeDelta(0), TimeDelta(1)),
        (TimeDelta(1), TimeDelta(2)),
        (TimeDelta(-1), TimeDelta(0)),
        (
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 4),
        ),
        (
            -TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
            -TimeDelta.from_ticks((1 << 124) + (2 << 64) + 2),
        ),
        (TimeDelta(1), dt.timedelta(seconds=2)),
        (TimeDelta(1), ht.timedelta(seconds=2)),
        (TimeDelta(1), ht.timedelta(seconds=1, femtoseconds=1)),
        (TimeDelta(1), ht.timedelta(seconds=1, yoctoseconds=1)),
        (dt.timedelta(seconds=1), TimeDelta(2)),
        (ht.timedelta(seconds=1), TimeDelta(2)),
        (ht.timedelta(seconds=1) - ht.timedelta(femtoseconds=1), TimeDelta(1)),
        (ht.timedelta(seconds=1) - ht.timedelta(yoctoseconds=1), TimeDelta(1)),
    ],
)
def test___lesser_value___comparison___lesser(
    left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta
) -> None:
    assert left < right
    assert left <= right
    assert not (left == right)
    assert left != right
    assert not (left > right)
    assert not (left >= right)


###############################################################################
# Miscellaneous
###############################################################################
@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), False),
        (TimeDelta(1), True),
        (TimeDelta(20042), True),
        (
            TimeDelta.from_ticks((2 << 124) + (5 << 64) + 6),
            True,
        ),
        (TimeDelta.from_ticks((-3 << 124) + (-6 << 64) + -9), True),
    ],
)
def test___timedelta___bool___returns_not_zero(value: TimeDelta, expected: bool) -> None:
    assert bool(value) == expected
    assert (not value) == (not expected)


_VARIOUS_VALUES = [
    TimeDelta(0),
    TimeDelta(2),
    TimeDelta(-2),
    TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
    TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
    TimeDelta.min,
    TimeDelta.max,
]


def test___various_values___hash___returns_probably_unique_int() -> None:
    hashes = {hash(x) for x in _VARIOUS_VALUES}
    assert len(hashes) == len(_VARIOUS_VALUES)


@pytest.mark.parametrize(
    "value",
    [
        TimeDelta(0),
        TimeDelta(2),
        TimeDelta(-2),
        TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
    ],
)
def test___various_values___copy___makes_copy(value: TimeDelta) -> None:
    new_value = copy.copy(value)
    assert new_value is not value
    assert new_value == value


@pytest.mark.parametrize(
    "value",
    [
        TimeDelta(0),
        TimeDelta(2),
        TimeDelta(-2),
        TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
    ],
)
def test___various_values___pickle_unpickle___makes_copy(value: TimeDelta) -> None:
    new_value = pickle.loads(pickle.dumps(value))
    assert new_value is not value
    assert new_value == value


def test___timedelta___pickle___references_public_modules() -> None:
    value = TimeDelta(123)
    value_bytes = pickle.dumps(value)

    assert b"nitypes.bintime" in value_bytes
    assert b"nitypes.bintime._timedelta" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95_\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x0fnitypes.bintime\x94\x8c\tTimeDelta\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\x10\x03\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x10\x85\x94R\x94.",
            TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3),
        ),
        (
            b"\x80\x04\x95_\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x0fnitypes.bintime\x94\x8c\tTimeDelta\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xfd\xff\xff\xff\xff\xff\xff\xef\x85\x94R\x94.",
            TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: TimeDelta
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), "0:00:00"),
        (TimeDelta(1), "0:00:01"),
        (TimeDelta(60), "0:01:00"),
        (TimeDelta(3600), "1:00:00"),
        (TimeDelta(86400), "1 day, 0:00:00"),
        (TimeDelta(86400 * 3), "3 days, 0:00:00"),
        (TimeDelta(-1), "-1 day, 23:59:59"),
        (TimeDelta(-60), "-1 day, 23:59:00"),
        (TimeDelta(-3600), "-1 day, 23:00:00"),
        (TimeDelta(-86400), "-1 day, 0:00:00"),
        (TimeDelta(-86400 * 3), "-3 days, 0:00:00"),
        (TimeDelta(Decimal("0.5")), "0:00:00.5"),
        (TimeDelta(Decimal("0.005")), "0:00:00.005"),
        (TimeDelta(Decimal("0.000_005")), "0:00:00.000005"),
        (TimeDelta(Decimal("0.000_000_000_000_005")), "0:00:00.000000000000005"),
        (TimeDelta(Decimal("0.000_000_000_000_000_005")), "0:00:00.000000000000000005"),
        (TimeDelta(Decimal("-0.5")), "-1 day, 23:59:59.5"),
        (TimeDelta(Decimal("-0.005")), "-1 day, 23:59:59.995"),
        (TimeDelta(Decimal("-0.000_005")), "-1 day, 23:59:59.999995"),
        (TimeDelta(Decimal("-0.000_000_000_000_005")), "-1 day, 23:59:59.999999999999995"),
        (TimeDelta(Decimal("-0.000_000_000_000_000_005")), "-1 day, 23:59:59.999999999999999995"),
    ],
)
def test___various_values___str___looks_ok(value: TimeDelta, expected: str) -> None:
    assert str(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (TimeDelta(0), "nitypes.bintime.TimeDelta(Decimal('0'))"),
        (TimeDelta(1), "nitypes.bintime.TimeDelta(Decimal('1'))"),
        (TimeDelta(60), "nitypes.bintime.TimeDelta(Decimal('60'))"),
        (TimeDelta(3600), "nitypes.bintime.TimeDelta(Decimal('3600'))"),
        (TimeDelta(86400), "nitypes.bintime.TimeDelta(Decimal('86400'))"),
        (TimeDelta(86400 * 3), "nitypes.bintime.TimeDelta(Decimal('259200'))"),
        (TimeDelta(-1), "nitypes.bintime.TimeDelta(Decimal('-1'))"),
        (TimeDelta(-60), "nitypes.bintime.TimeDelta(Decimal('-60'))"),
        (TimeDelta(-3600), "nitypes.bintime.TimeDelta(Decimal('-3600'))"),
        (TimeDelta(-86400), "nitypes.bintime.TimeDelta(Decimal('-86400'))"),
        (TimeDelta(-86400 * 3), "nitypes.bintime.TimeDelta(Decimal('-259200'))"),
        (TimeDelta(Decimal("0.5")), "nitypes.bintime.TimeDelta(Decimal('0.5'))"),
        (
            TimeDelta(Decimal("0.25")),
            "nitypes.bintime.TimeDelta(Decimal('0.25'))",
        ),
        (
            TimeDelta(Decimal("0.125")),
            "nitypes.bintime.TimeDelta(Decimal('0.125'))",
        ),
        (TimeDelta(Decimal("-0.5")), "nitypes.bintime.TimeDelta(Decimal('-0.5'))"),
        (
            TimeDelta(Decimal("-0.25")),
            "nitypes.bintime.TimeDelta(Decimal('-0.25'))",
        ),
        (
            TimeDelta(Decimal("-0.125")),
            "nitypes.bintime.TimeDelta(Decimal('-0.125'))",
        ),
        # The fractional part gets bruised because 0.005 isn't expressible as 2^-N
        (
            TimeDelta(Decimal("0.005")),
            "nitypes.bintime.TimeDelta(Decimal('0.00499999999999999999566319'))",
        ),
        (
            TimeDelta(Decimal("-0.005")),
            "nitypes.bintime.TimeDelta(Decimal('-0.00499999999999999999566319'))",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: TimeDelta, expected: str) -> None:
    assert repr(value) == expected


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___get_ticks___returns_correct_value(seconds: float) -> None:
    value = TimeDelta(seconds)

    assert value.ticks == seconds * _TICKS_PER_SECOND


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___to_tuple___returns_correct_values(seconds: float) -> None:
    value = TimeDelta(seconds)

    whole_seconds, fractional_seconds = value.to_tuple()
    assert whole_seconds == value.ticks >> _BITS_PER_SECOND
    assert fractional_seconds == value.ticks & _FRACTIONAL_SECONDS_MASK


@pytest.mark.parametrize(
    "seconds",
    [
        0,
        2,
        -2,
        1.5,
        1234.5678,
    ],
)
def test___various_values___from_tuple___timedelta_correct(seconds: float) -> None:
    value = TimeDelta(seconds)
    whole_seconds, fractional_seconds = value.to_tuple()
    other_value = TimeDelta.from_tuple(TimeValueTuple(whole_seconds, fractional_seconds))

    assert value == other_value


def test___whole_seconds_too_large___from_tuple___throws_error() -> None:
    whole_seconds = 1 << 70
    fractional_seconds = 0

    with pytest.raises(OverflowError) as exc:
        _ = TimeDelta.from_tuple(TimeValueTuple(whole_seconds, fractional_seconds))

    assert exc.value.args[0].startswith("The input value is out of range")


def test___fractional_seconds_too_large___from_tuple___throws_error() -> None:
    whole_seconds = 0
    fractional_seconds = 1 << 70

    with pytest.raises(OverflowError) as exc:
        _ = TimeDelta.from_tuple(TimeValueTuple(whole_seconds, fractional_seconds))

    assert exc.value.args[0].startswith("The input value is out of range")


def test___fractional_seconds_negative___from_tuple___throws_error() -> None:
    whole_seconds = 0
    fractional_seconds = -1

    with pytest.raises(OverflowError) as exc:
        _ = TimeDelta.from_tuple(TimeValueTuple(whole_seconds, fractional_seconds))

    assert exc.value.args[0].startswith("The input value is out of range")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/bintime/test_timedelta_array.py sha256=cdc98c8c6f0d6bde647ecd3a95363ae5339189441963d0e0d0dd07d50942d7f5 bytes=29977 -->
## FILE: tests/unit/bintime/test_timedelta_array.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/bintime/test_timedelta_array.py`
- sha256: `cdc98c8c6f0d6bde647ecd3a95363ae5339189441963d0e0d0dd07d50942d7f5`
- bytes: 29977

````python
from __future__ import annotations

import copy
import pickle
from typing import Any, Sequence

import numpy as np
import pytest
from typing_extensions import assert_type

from nitypes.bintime import TimeDelta, TimeDeltaArray


###############################################################################
# Constructor
###############################################################################
def test___no_args___construct___returns_empty_array() -> None:
    value = TimeDeltaArray()

    assert_type(value, TimeDeltaArray)
    assert isinstance(value, TimeDeltaArray)
    assert len(value._array) == 0


@pytest.mark.parametrize(
    "constructor_arg",
    (
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]),
        (TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])),
    ),
)
def test___sequence_arg___construct___returns_matching_array(
    constructor_arg: Sequence[TimeDelta],
) -> None:
    value = TimeDeltaArray(constructor_arg)

    assert_type(value, TimeDeltaArray)
    assert isinstance(value, TimeDeltaArray)
    assert len(value._array) == len(constructor_arg)
    assert (value._array[0]["msb"], value._array[0]["lsb"]) == TimeDelta(-1).to_tuple()
    assert (value._array[1]["msb"], value._array[1]["lsb"]) == TimeDelta(20.26).to_tuple()
    assert (value._array[2]["msb"], value._array[2]["lsb"]) == TimeDelta(500).to_tuple()


@pytest.mark.parametrize(
    "constructor_arg",
    (
        ([TimeDelta(0), TimeDelta(15).to_tuple()]),
        ([True, False]),
        ([1, 2]),
        ([10.0, 20.0]),
        (["abc", "xyz"]),
    ),
)
def test___mixed_arg___construct___raises(constructor_arg: list[Any]) -> None:
    with pytest.raises(TypeError):
        _ = TimeDeltaArray(constructor_arg)


###############################################################################
# len
###############################################################################
@pytest.mark.parametrize(
    "timedelta_list, expected_length",
    (
        (None, 0),
        ([TimeDelta(3.14)], 1),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 3),
    ),
)
def test___timedelta_array___get_len___returns_length(
    timedelta_list: list[TimeDelta], expected_length: int
) -> None:
    value = TimeDeltaArray(timedelta_list)

    length = len(value)

    assert length == expected_length


###############################################################################
# __getitem__
###############################################################################
@pytest.mark.parametrize(
    "timedelta_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([TimeDelta(3.14)], 0, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 0, None),
        # Last index
        (None, -1, IndexError()),
        ([TimeDelta(3.14)], -1, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -1, None),
        # Out of bounds index
        (None, 10, IndexError()),
        ([TimeDelta(3.14)], 10, IndexError()),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 10, IndexError()),
    ),
)
def test___timedelta_array___index___returns_timedelta(
    timedelta_list: list[TimeDelta], indexer: int, raised_exception: BaseException | None
) -> None:
    value = TimeDeltaArray(timedelta_list)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            _ = value[indexer]
    else:
        entry = value[indexer]
        assert entry == timedelta_list[indexer]


def test___timedelta_array___slice___returns_slice() -> None:
    value = TimeDeltaArray(
        [
            TimeDelta(-1),
            TimeDelta(3.14),
            TimeDelta(20.26),
            TimeDelta(500),
            TimeDelta(0x12345678_90ABCDEF),
        ]
    )

    selected = value[::2]

    expected = TimeDeltaArray(
        [
            TimeDelta(-1),
            TimeDelta(20.26),
            TimeDelta(0x12345678_90ABCDEF),
        ]
    )
    assert np.array_equal(selected._array, expected._array)


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___invalid_index___raises(indexer: Any) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        _ = value[indexer]


###############################################################################
# __setitem__
###############################################################################
@pytest.mark.parametrize(
    "timedelta_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([TimeDelta(3.14)], 0, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 0, None),
        # Last index
        (None, -1, IndexError()),
        ([TimeDelta(3.14)], -1, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -1, None),
        # Out of bounds index
        (None, 10, IndexError()),
        ([TimeDelta(3.14)], 10, IndexError()),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 10, IndexError()),
    ),
)
def test___timedelta_array___set_by_index___updates_array(
    timedelta_list: list[TimeDelta] | None, indexer: int, raised_exception: BaseException | None
) -> None:
    value = TimeDeltaArray(timedelta_list)
    new_entry = TimeDelta(-123.456)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            value[indexer] = new_entry
    else:
        value[indexer] = new_entry
        assert value[indexer] == new_entry


@pytest.mark.parametrize(
    "indexer, new_entries, expected_result",
    (
        # len(selected entries) == len(incoming entries)
        (  # Replaces one-for-one from list
            slice(1, 4),
            [TimeDelta(0), TimeDelta(1), TimeDelta(2)],
            TimeDeltaArray(
                [
                    TimeDelta(-1),
                    TimeDelta(0),
                    TimeDelta(1),
                    TimeDelta(2),
                    TimeDelta(0x12345678_90ABCDEF),
                ]
            ),
        ),
        (  # Replaces one from length-1 list
            slice(3, 4),
            [TimeDelta(0)],
            TimeDeltaArray(
                [
                    TimeDelta(-1),
                    TimeDelta(3.14),
                    TimeDelta(20.26),
                    TimeDelta(0),
                    TimeDelta(0x12345678_90ABCDEF),
                ]
            ),
        ),
        (  # With strided selection, replaces one-for-one from same-sized list
            slice(None, None, 2),
            [TimeDelta(0), TimeDelta(1), TimeDelta(2)],
            TimeDeltaArray(
                [TimeDelta(0), TimeDelta(3.14), TimeDelta(1), TimeDelta(500), TimeDelta(2)]
            ),
        ),
        # len(selected entries) > len(incoming entries)
        (  # Shrinks array, replacing many from length-2 list
            slice(1, 4),
            [TimeDelta(0), TimeDelta(10)],
            TimeDeltaArray(
                [TimeDelta(-1), TimeDelta(0), TimeDelta(10), TimeDelta(0x12345678_90ABCDEF)]
            ),
        ),
        (  # Shrinks array, replacing many from length-1 list
            slice(1, 4),
            [TimeDelta(0)],
            TimeDeltaArray([TimeDelta(-1), TimeDelta(0), TimeDelta(0x12345678_90ABCDEF)]),
        ),
        (  # Shrinks array, deleting when assigning empty list
            slice(1, 4),
            [],
            TimeDeltaArray([TimeDelta(-1), TimeDelta(0x12345678_90ABCDEF)]),
        ),
        # len(selected entries) < len(incoming entries)
        (  # Grows array, replacing then inserting when slice is too short for incoming values
            slice(1, 2),
            [TimeDelta(0), TimeDelta(10), TimeDelta(100)],
            TimeDeltaArray(
                [
                    TimeDelta(-1),
                    TimeDelta(0),
                    TimeDelta(10),
                    TimeDelta(100),
                    TimeDelta(20.26),
                    TimeDelta(500),
                    TimeDelta(0x12345678_90ABCDEF),
                ]
            ),
        ),
        (  # Grows array, inserting when slice is empty
            slice(1, 1),
            [TimeDelta(0), TimeDelta(10), TimeDelta(100)],
            TimeDeltaArray(
                [
                    TimeDelta(-1),
                    TimeDelta(0),
                    TimeDelta(10),
                    TimeDelta(100),
                    TimeDelta(3.14),
                    TimeDelta(20.26),
                    TimeDelta(500),
                    TimeDelta(0x12345678_90ABCDEF),
                ]
            ),
        ),
    ),
)
def test___timedelta_array___set_by_slice___updates_array(
    indexer: slice, new_entries: Sequence[TimeDelta], expected_result: TimeDeltaArray
) -> None:
    value = TimeDeltaArray(
        [
            TimeDelta(-1),
            TimeDelta(3.14),
            TimeDelta(20.26),
            TimeDelta(500),
            TimeDelta(0x12345678_90ABCDEF),
        ]
    )

    value[indexer] = new_entries

    assert np.array_equal(value._array, expected_result._array)


@pytest.mark.parametrize(
    "indexer, new_entries, raised_exception",
    (
        (  # Strided slice is too long for incoming values
            slice(None, None, 2),
            [TimeDelta(0)],
            ValueError(),
        ),
        (  # Strided slice is too short for incoming values
            slice(None, None, 4),
            [TimeDelta(0), TimeDelta(10)],
            ValueError(),
        ),
        (  # Assigning empty requires step == 1
            slice(None, None, 2),
            [],
            ValueError(),
        ),
        (  # Cannot assign from scalar
            slice(None, None, 2),
            TimeDelta(0),
            TypeError(),
        ),
        (
            slice(1, None),
            TimeDelta(0),
            TypeError(),
        ),
    ),
)
def test___timedelta_array___set_slice_wrong_value___raises(
    indexer: slice, new_entries: Sequence[TimeDelta] | TimeDelta, raised_exception: BaseException
) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500), TimeDelta(3000.125)])

    with pytest.raises(type(raised_exception)):
        value[indexer] = new_entries  # type: ignore # validating incompatible types


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___set_invalid_index___raises(indexer: Any) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])
    new_entry = TimeDelta(-100)

    with pytest.raises(TypeError):
        value[indexer] = new_entry


@pytest.mark.parametrize(
    "new_entry",
    (
        "0",
        1.0,
        True,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___set_invalid_value___raises(new_entry: Any) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        value[0] = new_entry


@pytest.mark.parametrize(
    "new_entries",
    (
        ["ab", "cd"],
        [1.0, 2.0],
        [True, False],
        [None, None],
        [TimeDelta(0), TimeDelta(15).to_tuple()],
    ),
)
def test___timedelta_array___set_mixed_slice___raises(new_entries: list[Any]) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500), TimeDelta(3000.125)])

    with pytest.raises(TypeError):
        value[::2] = new_entries


###############################################################################
# __delitem__
###############################################################################
@pytest.mark.parametrize(
    "timedelta_list, indexer, raised_exception",
    (
        # First index
        (None, 0, IndexError()),
        ([TimeDelta(3.14)], 0, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 0, None),
        # Last index
        (None, -1, IndexError()),
        ([TimeDelta(3.14)], -1, None),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -1, None),
        # Out of bounds index
        (None, 10, IndexError()),
        ([TimeDelta(3.14)], 10, IndexError()),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 10, IndexError()),
    ),
)
def test___timedelta_array___delete_by_index___removes_item(
    timedelta_list: list[TimeDelta] | None, indexer: int, raised_exception: BaseException | None
) -> None:
    value = TimeDeltaArray(timedelta_list)

    if raised_exception:
        with pytest.raises(type(raised_exception)):
            del value[indexer]
    else:
        modified = timedelta_list.copy() if timedelta_list else []
        del modified[indexer]
        del value[indexer]
        expected = TimeDeltaArray(modified)
        assert np.array_equal(value._array, expected._array)


@pytest.mark.parametrize(
    "indexer, expected_result",
    (
        (
            slice(1, 4),
            TimeDeltaArray(
                [
                    TimeDelta(-1),
                    TimeDelta(0x12345678_90ABCDEF),
                ]
            ),
        ),
        (
            slice(None, None, 2),
            TimeDeltaArray(
                [
                    TimeDelta(3.14),
                    TimeDelta(500),
                ]
            ),
        ),
    ),
)
def test___timedelta_array___delete_by_slice___removes_items(
    indexer: slice, expected_result: TimeDeltaArray
) -> None:
    value = TimeDeltaArray(
        [
            TimeDelta(-1),
            TimeDelta(3.14),
            TimeDelta(20.26),
            TimeDelta(500),
            TimeDelta(0x12345678_90ABCDEF),
        ]
    )

    del value[indexer]

    assert np.array_equal(value._array, expected_result._array)


@pytest.mark.parametrize(
    "indexer",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___delete_invalid_index___raises(indexer: Any) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        del value[indexer]


###############################################################################
# insert
###############################################################################
@pytest.mark.parametrize(
    "initial_value, index",
    (
        # Empty array
        (None, 0),
        (None, 1),
        (None, 3),
        (None, 10),
        (None, -1),
        (None, -2),
        (None, -10),
        # Existing entries
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 0),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 1),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 3),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], 10),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -1),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -3),
        ([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)], -10),
    ),
)
def test___timedelta_array___insert_value___inserts(
    initial_value: list[TimeDelta], index: int
) -> None:
    value = TimeDeltaArray(initial_value)
    inserted_value = TimeDelta(0)

    value.insert(index, inserted_value)

    expected_value = initial_value.copy() if initial_value else []
    expected_value.insert(index, inserted_value)
    expected = TimeDeltaArray(expected_value)
    assert np.array_equal(value._array, expected._array)


@pytest.mark.parametrize(
    "index",
    (
        "0",
        1.0,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___insert_invalid_index___raises(index: int) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        value.insert(index, TimeDelta(0))


@pytest.mark.parametrize(
    "value",
    (
        "0",
        1.0,
        True,
        None,
        [1, 2, 3],
    ),
)
def test___timedelta_array___insert_invalid_value___raises(value: Any) -> None:
    value = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        value.insert(0, value)


###############################################################################
# MutableSequence
###############################################################################
@pytest.mark.parametrize(
    "array, item, expected_count",
    (
        (TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]), TimeDelta(12.34), 0),
        (TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]), TimeDelta(-1), 1),
        (TimeDeltaArray([TimeDelta(20.26), TimeDelta(20.26), TimeDelta(500)]), TimeDelta(20.26), 2),
    ),
)
def test___timedelta_array___count___returns_matching_count(
    array: TimeDeltaArray, item: TimeDelta, expected_count: int
) -> None:
    item_count = array.count(item)

    assert item_count == expected_count


@pytest.mark.parametrize(
    "array, item, expected_index",
    (
        (TimeDeltaArray([TimeDelta(20.26), TimeDelta(20.26), TimeDelta(500)]), TimeDelta(20.26), 0),
        (TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]), TimeDelta(20.26), 1),
    ),
)
def test___timedelta_array___index___returns_matching_index(
    array: TimeDeltaArray, item: TimeDelta, expected_index: int
) -> None:
    item_index = array.index(item)

    assert item_index == expected_index


def test___timedelta_array_no_item___index___raises() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(ValueError):
        _ = array.index(TimeDelta(12.34))


def test___timedelta_array___append___adds_to_end() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])
    new_entry = TimeDelta(12.34)

    array.append(new_entry)

    expected = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500), TimeDelta(12.34)])
    assert np.array_equal(array._array, expected._array)


@pytest.mark.parametrize(
    "new_entry",
    (
        (),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([]),
        ([TimeDelta(-100)]),
    ),
)
def test___timedelta_array___append_invalid_value___raises(new_entry: Any) -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        array.append(new_entry)


@pytest.mark.parametrize(
    "new_entries",
    (
        (),
        ([]),
        ([TimeDelta(12.34)]),
        ([TimeDelta(12.34), TimeDelta(55.77)]),
        (TimeDeltaArray()),
        (TimeDeltaArray([TimeDelta(12.34)])),
        (TimeDeltaArray([TimeDelta(12.34), TimeDelta(55.77)])),
    ),
)
def test___timedelta_array___extend___adds_to_end(new_entries: Sequence[TimeDelta]) -> None:
    original_items = [TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]
    array = TimeDeltaArray(original_items)

    array.extend(new_entries)

    assert len(array) == len(original_items) + len(new_entries)
    separate_items = [*original_items, *new_entries]
    expected_array = TimeDeltaArray(separate_items)
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "new_entries",
    (
        (),
        ([]),
        ([TimeDelta(12.34)]),
        ([TimeDelta(12.34), TimeDelta(55.77)]),
        (TimeDeltaArray()),
        (TimeDeltaArray([TimeDelta(12.34)])),
        (TimeDeltaArray([TimeDelta(12.34), TimeDelta(55.77)])),
    ),
)
def test___timedelta_array___plus_equals___adds_to_end(new_entries: Sequence[TimeDelta]) -> None:
    original_items = [TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]
    array = TimeDeltaArray(original_items)

    array += new_entries

    assert len(array) == len(original_items) + len(new_entries)
    separate_items = [*original_items, *new_entries]
    expected_array = TimeDeltaArray(separate_items)
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "new_entries",
    (
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([None]),
        ([True]),
        ([13]),
        ([12.34]),
        (["abc"]),
    ),
)
def test___timedelta_array___extend_invalid_values___raises(new_entries: Any) -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        array.extend(new_entries)


@pytest.mark.parametrize(
    "new_entries",
    (
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        ([None]),
        ([True]),
        ([13]),
        ([12.34]),
        (["abc"]),
    ),
)
def test___timedelta_array___plus_equals_invalid_values___raises(new_entries: Any) -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(TypeError):
        array += new_entries


def test___timedelta_array___remove___removes_first_match() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(20.26)])

    array.remove(TimeDelta(20.26))

    assert len(array) == 2
    expected_array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26)])
    assert np.array_equal(array._array, expected_array._array)


@pytest.mark.parametrize(
    "item_to_remove",
    (
        (),
        (None),
        (True),
        (13),
        (12.34),
        ("abc"),
        (TimeDelta(0)),
    ),
)
def test___timedelta_array_no_item___remove___raises(item_to_remove: Any) -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(ValueError):
        array.remove(item_to_remove)


def test___timedelta_array___pop___removes_from_location() -> None:
    original_values = [TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]
    array = TimeDeltaArray(original_values)

    popped = array.pop()
    assert popped == original_values[-1]
    assert len(array) == 2
    assert np.array_equal(array._array, TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26)])._array)

    popped = array.pop(0)
    assert popped == TimeDelta(-1)
    assert len(array) == 1
    assert np.array_equal(array._array, TimeDeltaArray([TimeDelta(20.26)])._array)


def test___empty_timedelta_array___pop___raises() -> None:
    array = TimeDeltaArray()

    with pytest.raises(IndexError):
        array.pop()


def test___timedelta_array___pop_out_of_bounds___raises() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    with pytest.raises(IndexError):
        array.pop(10)


def test___timedelta_array___reverse___reverses() -> None:
    original_values = [TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]
    array = TimeDeltaArray(original_values)

    array.reverse()

    expected_order = original_values.copy()
    expected_order.reverse()
    expected_array = TimeDeltaArray(expected_order)
    assert np.array_equal(array._array, expected_array._array)


def test___timedelta_array___clear___empties_array() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    array.clear()

    assert len(array) == 0


def test___timedelta_array___iterate___visits_entries() -> None:
    original_values = [TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]
    array = TimeDeltaArray(original_values)

    iterated = list(iter(array))

    assert original_values == iterated


def test___timedelta_array___contains___returns_presence() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    assert TimeDelta(20.26) in array
    assert TimeDelta(12.34) not in array


###############################################################################
# Builtins
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]),
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]),
        ),
    ],
)
def test___same_value___equality___equal(left: TimeDeltaArray, right: TimeDeltaArray) -> None:
    assert left == right
    assert right == left


@pytest.mark.parametrize(
    "left, right",
    [
        (
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]),
            TimeDeltaArray([TimeDelta(-10), TimeDelta(200.26), TimeDelta(1500)]),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: TimeDeltaArray, right: TimeDeltaArray
) -> None:
    assert left != right


def test___timedelta_array___min___returns_minimum() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    assert min(array) == TimeDelta(-1)


def test___timedelta_array___max___returns_maximum() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    assert max(array) == TimeDelta(500)


def test___timedelta_array___copy___returns_copy() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    copied = copy.copy(array)

    assert array == copied
    assert array is not copied
    assert array._array is not copied._array
    for original_entry, copied_entry in zip(array, copied):
        assert original_entry is not copied_entry


def test___timedelta_array___deepcopy___returns_deepcopy() -> None:
    array = TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)])

    copied = copy.deepcopy(array)

    assert array == copied
    assert array is not copied
    assert array._array is not copied._array
    for original_entry, copied_entry in zip(array, copied):
        assert original_entry is not copied_entry


@pytest.mark.parametrize(
    "value, expected_str",
    (
        (TimeDeltaArray(), "[]"),
        (TimeDeltaArray([TimeDelta(-1)]), "[-1 day, 23:59:59]"),
        (
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26)]),
            "[-1 day, 23:59:59; 0:00:20.260000000000001563]",
        ),
        (
            TimeDeltaArray([TimeDelta(20.26), TimeDelta(-1), TimeDelta(500)]),
            "[0:00:20.260000000000001563; -1 day, 23:59:59; 0:08:20]",
        ),
    ),
)
def test___timedelta_array___str___looks_ok(value: TimeDeltaArray, expected_str: str) -> None:
    assert str(value) == expected_str


@pytest.mark.parametrize(
    "value, expected_repr",
    (
        (TimeDeltaArray(), "nitypes.bintime.TimeDeltaArray([])"),
        (
            TimeDeltaArray([TimeDelta(-1)]),
            "nitypes.bintime.TimeDeltaArray([nitypes.bintime.TimeDelta(Decimal('-1'))])",
        ),
        (
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26)]),
            "nitypes.bintime.TimeDeltaArray([nitypes.bintime.TimeDelta(Decimal('-1')), nitypes.bintime.TimeDelta(Decimal('20.2600000000000015631940'))])",
        ),
        (
            TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26), TimeDelta(500)]),
            "nitypes.bintime.TimeDeltaArray([nitypes.bintime.TimeDelta(Decimal('-1')), nitypes.bintime.TimeDelta(Decimal('20.2600000000000015631940')), nitypes.bintime.TimeDelta(Decimal('500'))])",
        ),
    ),
)
def test___timedelta_array___repr___looks_ok(value: TimeDeltaArray, expected_repr: str) -> None:
    assert repr(value) == expected_repr


def test___timedelta_array___pickle___references_public_modules() -> None:
    value = TimeDeltaArray([TimeDelta(20.26), TimeDelta(-1), TimeDelta(500)])

    pickled = pickle.dumps(value)

    assert b"nitypes.bintime" in pickled
    assert b"nitypes.bintime._timedelta_array" not in pickled


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95\xa8\x00\x00\x00\x00\x00\x00\x00\x8c\x0fnitypes.bintime\x94\x8c\x0eTimeDeltaArray\x94\x93\x94]\x94(\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94h\x00\x8c\tTimeDelta\x94\x93\x94\x8c\nfrom_ticks\x94\x86\x94R\x94\x8a\t\x00\x00\xc3\xf5(\\\x8fB\x14\x85\x94R\x94h\x06h\x08h\t\x86\x94R\x94\x8a\t\x00\x00\x00\x00\x00\x00\x00\x00\xff\x85\x94R\x94h\x06h\x08h\t\x86\x94R\x94\x8a\n\x00\x00\x00\x00\x00\x00\x00\x00\xf4\x01\x85\x94R\x94e\x85\x94R\x94.",
            TimeDeltaArray([TimeDelta(20.26), TimeDelta(-1), TimeDelta(500)]),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: TimeDeltaArray
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


@pytest.mark.parametrize(
    "value",
    (
        (TimeDeltaArray()),
        (TimeDeltaArray([TimeDelta(-1)])),
        (TimeDeltaArray([TimeDelta(-1), TimeDelta(20.26)])),
        (TimeDeltaArray([TimeDelta(20.26), TimeDelta(-1), TimeDelta(500)])),
    ),
)
def test___timedelta_array___pickle_unpickle___makes_copy(value: TimeDeltaArray) -> None:
    new_value: TimeDeltaArray = pickle.loads(pickle.dumps(value))
    assert new_value == value
    assert new_value is not value
    assert new_value._array is not value._array
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/complex/__init__.py sha256=7f59bb2964d12d553f66ae8876b1f5b45cbdbb3b7dc5dd5470129615426e3c9c bytes=51 -->
## FILE: tests/unit/complex/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/complex/__init__.py`
- sha256: `7f59bb2964d12d553f66ae8876b1f5b45cbdbb3b7dc5dd5470129615426e3c9c`
- bytes: 51

````python
"""Unit tests for the nitypes.complex package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/complex/test_conversion.py sha256=4c30ad717b60c08562120d9f8c032b3a2182f8303771662a6b597c421d6d1a86 bytes=9088 -->
## FILE: tests/unit/complex/test_conversion.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/complex/test_conversion.py`
- sha256: `4c30ad717b60c08562120d9f8c032b3a2182f8303771662a6b597c421d6d1a86`
- bytes: 9088

````python
from __future__ import annotations

from typing import Any

import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

from nitypes.complex import ComplexInt32Base, ComplexInt32DType, convert_complex


###############################################################################
# convert arrays
###############################################################################
def test___complexint32_array_to_complex64_array___convert_complex___converts_array() -> None:
    value_in = np.array([(1, 2), (3, -4), (-5, 6), (-7, -8)], ComplexInt32DType)

    value_out = convert_complex(np.complex64, value_in)

    assert_type(value_out, npt.NDArray[np.complex64])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == np.complex64
    assert list(value_out) == [1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j]


def test___complexint32_array_to_complex128_array___convert_complex___converts_array() -> None:
    value_in = np.array([(1, 2), (3, -4), (-5, 6), (-7, -8)], ComplexInt32DType)

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, npt.NDArray[np.complex128])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == np.complex128
    assert list(value_out) == [1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j]


def test___complexint32_array_to_complexint32_array___convert_complex___returns_original_array() -> (
    None
):
    value_in = np.array([(1, 2), (3, -4), (-5, 6), (-7, -8)], ComplexInt32DType)

    value_out = convert_complex(ComplexInt32DType, value_in)

    assert_type(value_out, npt.NDArray[ComplexInt32Base])
    assert value_out is value_in


def test___complex64_array_to_complexint32_array___convert_complex___converts_array() -> None:
    value_in = np.array([1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j], np.complex64)

    value_out = convert_complex(ComplexInt32DType, value_in)

    assert_type(value_out, npt.NDArray[ComplexInt32Base])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == ComplexInt32DType
    assert [x.item() for x in value_out] == [(1, 2), (3, -4), (-5, 6), (-7, -8)]


def test___complex64_array_to_complex64_array___convert_complex___returns_original_array() -> None:
    value_in = np.array([1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j], np.complex64)

    value_out = convert_complex(np.complex64, value_in)

    assert_type(value_out, npt.NDArray[np.complex64])
    assert value_out is value_in


def test___complex64_array_to_complex128_array___convert_complex___converts_array() -> None:
    value_in = np.array([1.23 + 4.56j, 6.78 - 9.01j], np.complex64)

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, npt.NDArray[np.complex128])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == np.complex128
    assert list(value_out) == pytest.approx([1.23 + 4.56j, 6.78 - 9.01j])


def test___complex128_array_to_complexint32_array___convert_complex___converts_array() -> None:
    value_in = np.array([1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j], np.complex128)

    value_out = convert_complex(ComplexInt32DType, value_in)

    assert_type(value_out, npt.NDArray[ComplexInt32Base])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == ComplexInt32DType
    assert [x.item() for x in value_out] == [(1, 2), (3, -4), (-5, 6), (-7, -8)]


def test___complex128_array_to_complex64_array___convert_complex___converts_array() -> None:
    value_in = np.array([1.23 + 4.56j, 6.78 - 9.01j], np.complex128)

    value_out = convert_complex(np.complex64, value_in)

    assert_type(value_out, npt.NDArray[np.complex64])
    assert isinstance(value_out, np.ndarray) and value_out.dtype == np.complex64
    assert list(value_out) == pytest.approx([1.23 + 4.56j, 6.78 - 9.01j])


def test___complex128_array_to_complex128_array___convert_complex___returns_original_array() -> (
    None
):
    value_in = np.array([1.23 + 4.56j, 6.78 - 9.01j], np.complex128)

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, npt.NDArray[np.complex128])
    assert value_out is value_in


def test___2d_complexint32_array_to_complex128_array___convert_complex___preserves_shape() -> None:
    # As of NumPy 2.3, np.array() can't infer the array shape, but the return type of
    # np.ndarray.__iter__() is shape-dependent, returning Iterator[_ScalarT] for 1D arrays and
    # Iterator[NDArray[_ScalarT]] for 2D arrays.
    value_in: np.ndarray[tuple[int, int], np.dtype[np.void]] = np.array(
        [[(1, 2), (3, -4)], [(-5, 6), (-7, -8)], [(9, 10), (11, 12)]], ComplexInt32DType
    )

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, np.ndarray[tuple[int, int], np.dtype[np.complex128]])
    assert isinstance(value_out, np.ndarray) and value_out.shape == (3, 2)
    assert [list(x) for x in value_out] == [
        [1 + 2j, 3 - 4j],
        [-5 + 6j, -7 - 8j],
        [9 + 10j, 11 + 12j],
    ]


def test___2d_complex64_array_to_complex128_array___convert_complex___preserves_shape() -> None:
    # As of NumPy 2.3, np.array() can't infer the array shape, but the return type of
    # np.ndarray.__iter__() is shape-dependent, returning Iterator[_ScalarT] for 1D arrays and
    # Iterator[NDArray[_ScalarT]] for 2D arrays.
    value_in: np.ndarray[tuple[int, int], np.dtype[np.complex64]] = np.array(
        [[1 + 2j, 3 - 4j], [-5 + 6j, -7 - 8j], [9 + 10j, 11 + 12j]], np.complex64
    )

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, np.ndarray[tuple[int, int], np.dtype[np.complex128]])
    assert isinstance(value_out, np.ndarray) and value_out.shape == (3, 2)
    assert [list(x) for x in value_out] == [
        [1 + 2j, 3 - 4j],
        [-5 + 6j, -7 - 8j],
        [9 + 10j, 11 + 12j],
    ]


def test___arrays_with_static_shape___convert_complex___preserves_static_and_runtime_shape() -> (
    None
):
    # np.zeros() can infer the array shape when type checking because it takes a shape argument.
    value_in_1d = np.zeros(3, np.complex64)
    value_in_2d = np.zeros((4, 5), np.complex128)
    value_in_3d = np.zeros((6, 7, 8), ComplexInt32DType)

    value_out_1d = convert_complex(np.complex128, value_in_1d)
    value_out_2d = convert_complex(ComplexInt32DType, value_in_2d)
    value_out_3d = convert_complex(np.complex64, value_in_3d)

    assert_type(value_out_1d, np.ndarray[tuple[int], np.dtype[np.complex128]])
    assert_type(value_out_2d, np.ndarray[tuple[int, int], np.dtype[ComplexInt32Base]])
    assert_type(value_out_3d, np.ndarray[tuple[int, int, int], np.dtype[np.complex64]])
    assert isinstance(value_out_1d, np.ndarray) and value_out_1d.shape == (3,)
    assert isinstance(value_out_2d, np.ndarray) and value_out_2d.shape == (4, 5)
    assert isinstance(value_out_3d, np.ndarray) and value_out_3d.shape == (6, 7, 8)


###############################################################################
# convert scalars
###############################################################################
def test___complexint32_scalar_to_complex128_scalar___convert_complex___converts_scalar() -> None:
    value_in = np.array([(1, 2)], ComplexInt32DType)[0]
    assert_type(value_in, Any)  # ¯\_(ツ)_/¯

    value_out = convert_complex(np.complex128, value_in)

    # Mypy infers np.ndarray[Any, Any], which seems wrong.
    # Pyright infers np.ndarray[Any, np.dtype[np.complex128]], which seems right.
    assert_type(value_out, np.ndarray[Any, np.dtype[np.complex128]])  # type: ignore[assert-type]
    assert isinstance(value_out, np.complex128)
    assert value_out == (1 + 2j)


def test___complex128_scalar_to_complexint32_scalar___convert_complex___converts_scalar() -> None:
    value_in = np.complex128(1 + 2j)

    value_out = convert_complex(ComplexInt32DType, value_in)

    assert_type(value_out, np.ndarray[tuple[()], np.dtype[ComplexInt32Base]])
    assert isinstance(value_out, ComplexInt32Base)
    assert value_out.item() == (1, 2)


def test___complexint32_scalar_to_complexint32_scalar___convert_complex___returns_original_scalar() -> (
    None
):
    value_in = np.array([(1, 2)], ComplexInt32DType)[0]
    assert_type(value_in, Any)  # ¯\_(ツ)_/¯

    value_out = convert_complex(ComplexInt32DType, value_in)

    # Mypy infers np.ndarray[Any, Any], which seems wrong.
    # Pyright infers np.ndarray[Any, np.dtype[np.void]], which seems right.
    assert_type(value_out, np.ndarray[Any, np.dtype[np.void]])  # type: ignore[assert-type]
    assert value_out is value_in


def test___complex64_scalar_to_complex128_scalar___convert_complex___converts_scalar() -> None:
    value_in = np.complex64(1.23 + 4.56j)

    value_out = convert_complex(np.complex128, value_in)

    assert_type(value_out, np.ndarray[tuple[()], np.dtype[np.complex128]])
    assert isinstance(value_out, np.complex128)
    assert value_out == pytest.approx(1.23 + 4.56j)
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/complex/test_dtypes.py sha256=092c8f3b74df4b6cb6d05dea841e9105e1ad52651e2732dc43ba2999581625c2 bytes=2377 -->
## FILE: tests/unit/complex/test_dtypes.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/complex/test_dtypes.py`
- sha256: `092c8f3b74df4b6cb6d05dea841e9105e1ad52651e2732dc43ba2999581625c2`
- bytes: 2377

````python
from __future__ import annotations

from typing import Any

import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

from nitypes.complex import ComplexInt32Base, ComplexInt32DType


def test___complexint32_dtype___np_array___constructs_array_with_dtype() -> None:
    value = np.array([(1, 2), (3, -4), (-5, 6), (-7, -8)], ComplexInt32DType)

    assert_type(value, npt.NDArray[ComplexInt32Base])
    assert isinstance(value, np.ndarray) and value.dtype == ComplexInt32DType
    assert [x.item() for x in value] == [(1, 2), (3, -4), (-5, 6), (-7, -8)]


def test___complexint32_dtype___np_zeros___constructs_array_with_dtype() -> None:
    value = np.zeros(3, ComplexInt32DType)

    assert_type(value, np.ndarray[tuple[int], np.dtype[ComplexInt32Base]])
    assert isinstance(value, np.ndarray) and value.dtype == ComplexInt32DType
    assert [x.item() for x in value] == [(0, 0), (0, 0), (0, 0)]


def test___complexint32_array___index___returns_complexint32_scalar() -> None:
    array = np.array([(1, 2), (3, -4)], ComplexInt32DType)

    value = array[1]

    assert_type(value, Any)  # ¯\_(ツ)_/¯
    assert isinstance(value, ComplexInt32Base)  # alias for np.void
    assert value["real"] == 3
    assert value["imag"] == -4


def test___complexint32_arrays___add___raises_type_error() -> None:
    left = np.array([(1, 2), (3, -4)], ComplexInt32DType)
    right = np.array([(-5, 6), (-7, -8)], ComplexInt32DType)

    with pytest.raises(TypeError):
        _ = left + right  # type: ignore[operator]


def test___complexint32_array_and_int16_array___add___raises_type_error() -> None:
    left = np.array([(1, 2), (3, -4)], ComplexInt32DType)
    right = np.array([5, -6], np.int16)

    with pytest.raises(TypeError):
        _ = left + right  # type: ignore[operator]


def test___unknown_structured_dtype___equality___not_equal() -> None:
    dtype = np.dtype([("a", np.int16), ("b", np.int16)])

    assert dtype != ComplexInt32DType


def test___duplicate_structured_dtype___equality___equal() -> None:
    dtype = np.dtype([("real", np.int16), ("imag", np.int16)])

    assert dtype == ComplexInt32DType


def test___structured_dtype_str___equality___not_equal() -> None:
    dtype = np.dtype("i2, i2")

    assert dtype != ComplexInt32DType
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/scalar/__init__.py sha256=ad04208554f0b88183e338e83c48ffbde2617ad9e662923a5616e685a60260eb bytes=50 -->
## FILE: tests/unit/scalar/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/scalar/__init__.py`
- sha256: `ad04208554f0b88183e338e83c48ffbde2617ad9e662923a5616e685a60260eb`
- bytes: 50

````python
"""Unit tests for the nitypes.scalar package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/scalar/test_scalar.py sha256=b9c4544c95b2f7460cbda8cfb8c70fd50b07120ba33007c5bb43e9540c76b7cf bytes=10469 -->
## FILE: tests/unit/scalar/test_scalar.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/scalar/test_scalar.py`
- sha256: `b9c4544c95b2f7460cbda8cfb8c70fd50b07120ba33007c5bb43e9540c76b7cf`
- bytes: 10469

````python
from __future__ import annotations

import copy
import pickle
from typing import Any

import pytest
from typing_extensions import assert_type

from nitypes.scalar import Scalar, TScalar_co
from nitypes.waveform._extended_properties import (
    UNIT_DESCRIPTION,
    ExtendedPropertyDictionary,
)


###############################################################################
# create
###############################################################################
def test___bool_data_value___create___creates_scalar_data_with_data_and_default_units() -> None:
    data = Scalar(True)

    assert_type(data.value, bool)
    assert data.value is True
    assert data.units == ""


def test___int_data_value___create___creates_scalar_data_with_data_and_default_units() -> None:
    data = Scalar(10)

    assert_type(data.value, int)
    assert data.value == 10
    assert data.units == ""


def test___float_data_value___create___creates_scalar_data_with_data_and_default_units() -> None:
    data = Scalar(20.0)

    assert_type(data.value, float)
    assert data.value == 20.0
    assert data.units == ""


def test___str_data_value___create___creates_scalar_data_with_data_and_default_units() -> None:
    data = Scalar("value")

    assert_type(data.value, str)
    assert data.value == "value"
    assert data.units == ""


@pytest.mark.parametrize("data_value", [True, 10, 20.0, "value"])
@pytest.mark.parametrize("units", ["volts"])
def test___data_value_and_units___create___creates_scalar_data_with_data_and_units(
    data_value: Any, units: str
) -> None:
    data = Scalar(data_value, units)

    assert data.value == data_value
    assert data.units == units


@pytest.mark.parametrize("data_value", [[1.0, 2.0], {"key", "value"}])
def test___invalid_data_value___create___raises_type_error(data_value: Any) -> None:
    with pytest.raises(TypeError) as exc:
        _ = Scalar(data_value)

    assert exc.value.args[0].startswith("The scalar input data must be a bool, int, float, or str.")


def test___both_units_specified_unequal__create___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = Scalar(10, "Volts", extended_properties={UNIT_DESCRIPTION: "Amps"})

    assert exc.value.args[0].startswith(
        "The specified units input does not match the units specified in extended_properties."
    )


def test___units_only_specified_in_extended_properties__create___creates_with_units() -> None:
    data = Scalar(10, extended_properties={UNIT_DESCRIPTION: "Volts"})
    assert data.units == "Volts"


###############################################################################
# compare
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Scalar(False), Scalar(False)),
        (Scalar(1), Scalar(1)),
        (Scalar(10.0), Scalar(10.0)),
        (Scalar("value"), Scalar("value")),
    ],
)
def test___same_value___comparison___equal(
    left: Scalar[TScalar_co], right: Scalar[TScalar_co]
) -> None:
    assert not (left < right)
    assert left <= right
    assert left == right
    assert not (left != right)
    assert not (left > right)
    assert left >= right


@pytest.mark.parametrize(
    "left, right",
    [
        (Scalar(False), Scalar(True)),
        (Scalar(0), Scalar(1)),
        (Scalar(10.0), Scalar(20.0)),
        (Scalar("aaa"), Scalar("zzz")),
    ],
)
def test___lesser_value___comparison___lesser(
    left: Scalar[TScalar_co], right: Scalar[TScalar_co]
) -> None:
    assert left < right
    assert left <= right
    assert not (left == right)
    assert left != right
    assert not (left > right)
    assert not (left >= right)


@pytest.mark.parametrize(
    "left, right",
    [
        (Scalar(False), Scalar(10)),
        (Scalar(False), Scalar(10.0)),
        (Scalar(0), Scalar(1.0)),
    ],
)
def test___mixed_numeric_types___comparison___lesser(
    left: Scalar[TScalar_co], right: Scalar[TScalar_co]
) -> None:
    assert left < right
    assert left <= right
    assert not (left > right)
    assert not (left >= right)


@pytest.mark.parametrize(
    "left, right",
    [
        (Scalar(False), Scalar("value")),
        (Scalar(10), Scalar("value")),
        (Scalar(10.0), Scalar("value")),
    ],
)
def test___numeric_and_string___comparison___throws_exception(
    left: Scalar[TScalar_co], right: Scalar[TScalar_co]
) -> None:
    expected_message = "Comparing Scalar objects of numeric and string types is not permitted"

    with pytest.raises(TypeError) as exc1:
        _ = left < right
    with pytest.raises(TypeError) as exc2:
        _ = left <= right
    with pytest.raises(TypeError) as exc3:
        _ = left > right
    with pytest.raises(TypeError) as exc4:
        _ = left >= right

    assert exc1.value.args[0].startswith(expected_message)
    assert exc2.value.args[0].startswith(expected_message)
    assert exc3.value.args[0].startswith(expected_message)
    assert exc4.value.args[0].startswith(expected_message)


def test___different_units___comparison___throws_exception() -> None:
    left = Scalar(0, "volts")
    right = Scalar(0, "amps")
    expected_message = "Comparing Scalar objects with different units is not permitted."

    with pytest.raises(ValueError) as exc1:
        _ = left < right
    with pytest.raises(ValueError) as exc2:
        _ = left <= right
    with pytest.raises(ValueError) as exc3:
        _ = left > right
    with pytest.raises(ValueError) as exc4:
        _ = left >= right

    assert exc1.value.args[0].startswith(expected_message)
    assert exc2.value.args[0].startswith(expected_message)
    assert exc3.value.args[0].startswith(expected_message)
    assert exc4.value.args[0].startswith(expected_message)


###############################################################################
# other operators
###############################################################################
@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (Scalar(False), "nitypes.scalar.Scalar(value=False)"),
        (Scalar(10), "nitypes.scalar.Scalar(value=10)"),
        (Scalar(20.0), "nitypes.scalar.Scalar(value=20.0)"),
        (Scalar("value"), "nitypes.scalar.Scalar(value='value')"),
        (Scalar(False, "amps"), "nitypes.scalar.Scalar(value=False, units='amps')"),
        (Scalar(10, "volts"), "nitypes.scalar.Scalar(value=10, units='volts')"),
        (Scalar(20.0, "watts"), "nitypes.scalar.Scalar(value=20.0, units='watts')"),
        (Scalar("value", ""), "nitypes.scalar.Scalar(value='value')"),
        (
            Scalar(10, units="volts", extended_properties={"Prop1": "Value1"}),
            "nitypes.scalar.Scalar(value=10, units='volts', "
            "extended_properties=nitypes.waveform.ExtendedPropertyDictionary("
            "{'Prop1': 'Value1', 'NI_UnitDescription': 'volts'}))",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: Scalar[Any], expected_repr: str) -> None:
    assert repr(value) == expected_repr


@pytest.mark.parametrize(
    "value, expected_str",
    [
        (Scalar(False), "False"),
        (Scalar(10), "10"),
        (Scalar(20.0), "20.0"),
        (Scalar("value"), "value"),
        (Scalar(False, "amps"), "False amps"),
        (Scalar(10, "volts"), "10 volts"),
        (Scalar(20.0, "watts"), "20.0 watts"),
        (Scalar("value", ""), "value"),
    ],
)
def test___various_values___str___looks_ok(value: Scalar[Any], expected_str: str) -> None:
    assert str(value) == expected_str


###############################################################################
# other properties
###############################################################################
def test___scalar_with_units___get_extended_properties___returns_correct_dictionary() -> None:
    value = Scalar(20.0, "watts")

    prop_dict = value.extended_properties

    assert isinstance(prop_dict, ExtendedPropertyDictionary)
    assert prop_dict.get(UNIT_DESCRIPTION) == "watts"


def test___scalar_with_units___set_units___units_updated_correctly() -> None:
    value = Scalar(20.0, "watts")

    value.units = "volts"

    assert value.units == "volts"


@pytest.mark.parametrize(
    "value",
    [
        Scalar(False),
        Scalar(10),
        Scalar(20.0),
        Scalar("value"),
        Scalar(False, "amps"),
        Scalar(10, "volts"),
        Scalar(20.0, "watts"),
        Scalar("value", ""),
        Scalar(10, "Volts", extended_properties={"one": 1}),
    ],
)
def test___various_values___copy___makes_copy(value: Scalar[TScalar_co]) -> None:
    new_value = copy.copy(value)
    assert new_value is not value
    assert new_value == value
    assert new_value.extended_properties == value.extended_properties


@pytest.mark.parametrize(
    "value",
    [
        Scalar(False),
        Scalar(10),
        Scalar(20.0),
        Scalar("value"),
        Scalar(False, "amps"),
        Scalar(10, "volts"),
        Scalar(20.0, "watts"),
        Scalar("value", ""),
        Scalar(10, "Volts", extended_properties={"one": 1}),
    ],
)
def test___various_values___pickle_unpickle___makes_copy(value: Scalar[TScalar_co]) -> None:
    new_value = pickle.loads(pickle.dumps(value))
    assert isinstance(new_value, Scalar)
    assert new_value is not value
    assert new_value == value
    assert new_value.extended_properties == value.extended_properties


def test___scalar___pickle___references_public_modules() -> None:
    value = Scalar(123)
    value_bytes = pickle.dumps(value)

    assert b"nitypes.scalar" in value_bytes
    assert b"nitypes.scalar._scalar" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x952\x00\x00\x00\x00\x00\x00\x00\x8c\x0enitypes.scalar\x94\x8c\x06Scalar\x94\x93\x94G@4\x00\x00\x00\x00\x00\x00\x8c\x05watts\x94\x86\x94R\x94.",
            Scalar(20.0, "watts"),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: Scalar[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/test_placeholder.py sha256=ffeb29fc528112c44824330bc77bbc5eea2db21d7cea678f2937576f58a169da bytes=45 -->
## FILE: tests/unit/test_placeholder.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/test_placeholder.py`
- sha256: `ffeb29fc528112c44824330bc77bbc5eea2db21d7cea678f2937576f58a169da`
- bytes: 45

````python
def test___placeholder() -> None:
    pass
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/time/__init__.py sha256=fba3f8e974190700bd868cbdea84d48b6ee8d1819efb69d801508f643676a66b bytes=48 -->
## FILE: tests/unit/time/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/time/__init__.py`
- sha256: `fba3f8e974190700bd868cbdea84d48b6ee8d1819efb69d801508f643676a66b`
- bytes: 48

````python
"""Unit tests for the nitypes.time package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/time/test_conversion.py sha256=3c703be6dd97f188ac4576e75b168c2f10243a431e620b26089ca0599396ccf5 bytes=11505 -->
## FILE: tests/unit/time/test_conversion.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/time/test_conversion.py`
- sha256: `3c703be6dd97f188ac4576e75b168c2f10243a431e620b26089ca0599396ccf5`
- bytes: 11505

````python
from __future__ import annotations

import datetime as dt
from typing import Any

import hightime as ht
import pytest
from typing_extensions import assert_type

import nitypes.bintime as bt
from nitypes.time import convert_datetime, convert_timedelta

_BT_EPSILON = ht.timedelta(yoctoseconds=54210)
_DT_EPSILON = ht.timedelta(microseconds=1)


###############################################################################
# convert_datetime
###############################################################################
def test___bt_to_bt___convert_datetime___returns_original_object() -> None:
    value_in = bt.DateTime.now(dt.timezone.utc)

    value_out = convert_datetime(bt.DateTime, value_in)

    assert_type(value_out, bt.DateTime)
    assert value_out is value_in


def test___dt_to_dt___convert_datetime___returns_original_object() -> None:
    value_in = dt.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(dt.datetime, value_in)

    assert_type(value_out, dt.datetime)
    assert value_out is value_in


def test___ht_to_ht___convert_datetime___returns_original_object() -> None:
    value_in = ht.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(ht.datetime, value_in)

    assert_type(value_out, ht.datetime)
    assert value_out is value_in


def test___bt_to_dt___convert_datetime___returns_equivalent_dt_datetime() -> None:
    value_in = bt.DateTime.now(dt.timezone.utc)

    value_out = convert_datetime(dt.datetime, value_in)

    assert_type(value_out, dt.datetime)
    assert isinstance(value_out, dt.datetime)
    assert abs(value_out - value_in) <= _DT_EPSILON + _BT_EPSILON
    assert value_out.tzinfo is value_in.tzinfo
    assert value_out.fold == 0


def test___bt_to_ht___convert_datetime___returns_equivalent_ht_datetime() -> None:
    value_in = bt.DateTime.now(dt.timezone.utc)

    value_out = convert_datetime(ht.datetime, value_in)

    assert_type(value_out, ht.datetime)
    assert isinstance(value_out, ht.datetime)
    assert value_out == value_in
    assert value_out.tzinfo is value_in.tzinfo
    assert value_out.fold == 0


def test___dt_to_bt___convert_datetime___returns_equivalent_bt_datetime() -> None:
    value_in = dt.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(bt.DateTime, value_in)

    assert_type(value_out, bt.DateTime)
    assert isinstance(value_out, bt.DateTime)
    assert value_out == value_in
    assert value_out.tzinfo is value_in.tzinfo


def test___dt_to_ht___convert_datetime___returns_equivalent_ht_datetime() -> None:
    value_in = dt.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(ht.datetime, value_in)

    assert_type(value_out, ht.datetime)
    assert isinstance(value_out, ht.datetime)
    assert value_out == value_in
    assert value_out.tzinfo is value_in.tzinfo
    assert value_out.fold == value_in.fold


def test___ht_to_bt___convert_datetime___returns_equivalent_bt_datetime() -> None:
    value_in = ht.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(bt.DateTime, value_in)

    assert_type(value_out, bt.DateTime)
    assert isinstance(value_out, bt.DateTime)
    assert abs(value_out - value_in) <= _BT_EPSILON
    assert value_out.tzinfo is value_in.tzinfo


def test___ht_to_dt___convert_datetime___returns_equivalent_dt_datetime() -> None:
    value_in = ht.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(dt.datetime, value_in)

    assert_type(value_out, dt.datetime)
    assert isinstance(value_out, dt.datetime)
    assert value_out == value_in
    assert value_out.tzinfo is value_in.tzinfo
    assert value_out.fold == value_in.fold


def test___precise_ht_to_bt___convert_datetime___loses_precision() -> None:
    # ht.datetime.now always sets femtosecond and yoctosecond to 0, so add an offset.
    value_in = ht.datetime.now(dt.timezone.utc) + ht.timedelta(femtoseconds=1, yoctoseconds=2)

    value_out = convert_datetime(bt.DateTime, value_in)

    assert value_out != value_in
    assert abs(value_out - value_in) <= _BT_EPSILON


def test___precise_ht_to_dt___convert_datetime___loses_precision() -> None:
    # ht.datetime.now always sets femtosecond and yoctosecond to 0, so add an offset.
    value_in = ht.datetime.now(dt.timezone.utc) + ht.timedelta(femtoseconds=1, yoctoseconds=2)

    value_out = convert_datetime(dt.datetime, value_in)

    assert value_out != value_in
    assert abs(value_out - value_in) <= _DT_EPSILON


@pytest.mark.parametrize("requested_type", [bt.DateTime, dt.datetime, ht.datetime])
def test___variable_requested_type___convert_datetime___static_return_type_unknown(
    requested_type: type[Any],
) -> None:
    value_in = dt.datetime.now(dt.timezone.utc)

    value_out = convert_datetime(requested_type, value_in)

    # Mypy infers Any, which seems right.
    # Pyright infers dt.datetime, which seems wrong.
    assert_type(value_out, Any)  # pyright: ignore[reportAssertTypeFailure]
    assert isinstance(value_out, requested_type)


@pytest.mark.parametrize(
    "value_in",
    [
        bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
        dt.datetime(2025, 1, 1),
        ht.datetime(2025, 1, 1),
    ],
)
def test___invalid_requested_type___convert_datetime___raises_type_error(
    value_in: bt.DateTime | dt.datetime | ht.datetime,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = convert_datetime(str, value_in)  # type: ignore[type-var]

    assert exc.value.args[0].startswith("The requested type must be a datetime type.")


@pytest.mark.parametrize("requested_type", [bt.DateTime, dt.datetime, ht.datetime])
def test___invalid_value___convert_datetime___raises_type_error(requested_type: type[Any]) -> None:
    value_in = "10:30 a.m."

    with pytest.raises(TypeError) as exc:
        _ = convert_datetime(requested_type, value_in)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith("The value must be a datetime.")


###############################################################################
# convert_timedelta
###############################################################################
def test___bt_to_bt___convert_timedelta___returns_original_object() -> None:
    value_in = bt.TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3)

    value_out = convert_timedelta(bt.TimeDelta, value_in)

    assert_type(value_out, bt.TimeDelta)
    assert value_out is value_in


def test___dt_to_dt___convert_timedelta___returns_original_object() -> None:
    value_in = dt.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(dt.timedelta, value_in)

    assert_type(value_out, dt.timedelta)
    assert value_out is value_in


def test___ht_to_ht___convert_timedelta___returns_original_object() -> None:
    value_in = ht.timedelta(days=1, seconds=2, microseconds=3, femtoseconds=4, yoctoseconds=5)

    value_out = convert_timedelta(ht.timedelta, value_in)

    assert_type(value_out, ht.timedelta)
    assert value_out is value_in


def test___bt_to_dt___convert_timedelta___returns_equivalent_dt_timedelta() -> None:
    # 1 << 124 ticks is 1 << 60 seconds, which is too big for dt.timedelta.
    value_in = bt.TimeDelta.from_ticks((1 << 92) + (2 << 64) + 3)

    value_out = convert_timedelta(dt.timedelta, value_in)

    assert_type(value_out, dt.timedelta)
    assert isinstance(value_out, dt.timedelta)
    assert abs(value_out - value_in) <= _DT_EPSILON


def test___bt_to_ht___convert_timedelta___returns_equivalent_ht_timedelta() -> None:
    # 1 << 124 ticks is 1 << 60 seconds, which is too big for ht.timedelta too, apparently.
    value_in = bt.TimeDelta.from_ticks((1 << 92) + (2 << 64) + 3)

    value_out = convert_timedelta(ht.timedelta, value_in)

    assert_type(value_out, ht.timedelta)
    assert isinstance(value_out, ht.timedelta)
    assert abs(value_out - value_in) <= _BT_EPSILON


def test___dt_to_bt___convert_timedelta___returns_equivalent_bt_timedelta() -> None:
    value_in = dt.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(bt.TimeDelta, value_in)

    assert_type(value_out, bt.TimeDelta)
    assert isinstance(value_out, bt.TimeDelta)
    assert abs(value_out - value_in) <= _BT_EPSILON


def test___dt_to_ht___convert_timedelta___returns_equivalent_ht_timedelta() -> None:
    value_in = dt.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(ht.timedelta, value_in)

    assert_type(value_out, ht.timedelta)
    assert isinstance(value_out, ht.timedelta)
    assert value_out == value_in


def test___ht_to_bt___convert_timedelta___returns_equivalent_bt_timedelta() -> None:
    value_in = ht.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(bt.TimeDelta, value_in)

    assert_type(value_out, bt.TimeDelta)
    assert isinstance(value_out, bt.TimeDelta)
    assert abs(value_out - value_in) <= _BT_EPSILON


def test___ht_to_dt___convert_timedelta___returns_equivalent_dt_timedelta() -> None:
    value_in = ht.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(dt.timedelta, value_in)

    assert_type(value_out, dt.timedelta)
    assert isinstance(value_out, dt.timedelta)
    assert value_out == value_in


def test___precise_ht_to_bt___convert_timedelta___loses_precision() -> None:
    value_in = ht.timedelta(days=1, seconds=2, microseconds=3, femtoseconds=4, yoctoseconds=5)

    value_out = convert_timedelta(bt.TimeDelta, value_in)

    assert value_out != value_in
    assert abs(value_out - value_in) <= _BT_EPSILON


def test___precise_ht_to_dt___convert_timedelta___loses_precision() -> None:
    value_in = ht.timedelta(days=1, seconds=2, microseconds=3, femtoseconds=4, yoctoseconds=5)

    value_out = convert_timedelta(dt.timedelta, value_in)

    assert value_out != value_in
    assert abs(value_out - value_in) <= _DT_EPSILON


@pytest.mark.parametrize("requested_type", [dt.timedelta, ht.timedelta])
def test___variable_requested_type___convert_timedelta___static_return_type_unknown(
    requested_type: type[Any],
) -> None:
    value_in = dt.timedelta(days=1, seconds=2, microseconds=3)

    value_out = convert_timedelta(requested_type, value_in)

    # Mypy infers Any, which seems right.
    # Pyright infers dt.datetime, which seems wrong.
    assert_type(value_out, Any)  # pyright: ignore[reportAssertTypeFailure]
    assert isinstance(value_out, requested_type)


@pytest.mark.parametrize("value_in", [dt.timedelta(), ht.timedelta()])
def test___invalid_requested_type___convert_timedelta___raises_type_error(
    value_in: dt.timedelta | ht.timedelta,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = convert_timedelta(str, value_in)  # type: ignore[type-var]

    assert exc.value.args[0].startswith("The requested type must be a timedelta type.")


@pytest.mark.parametrize("requested_type", [dt.timedelta, ht.timedelta])
def test___invalid_value___convert_timedelta___raises_type_error(requested_type: type[Any]) -> None:
    value_in = "10:30 a.m."

    with pytest.raises(TypeError) as exc:
        _ = convert_timedelta(requested_type, value_in)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith("The value must be a timedelta.")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/vector/__init__.py sha256=edcedd1ab537d8a385df790546edafaea1f39d9d36d07ce119f52a1dd63bc6be bytes=50 -->
## FILE: tests/unit/vector/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/vector/__init__.py`
- sha256: `edcedd1ab537d8a385df790546edafaea1f39d9d36d07ce119f52a1dd63bc6be`
- bytes: 50

````python
"""Unit tests for the nitypes.vector package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/vector/test_vector.py sha256=10adc8ea3608929a5384e77720bb04e1e38e575be622d9759a4e8336039bb2b0 bytes=16007 -->
## FILE: tests/unit/vector/test_vector.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/vector/test_vector.py`
- sha256: `10adc8ea3608929a5384e77720bb04e1e38e575be622d9759a4e8336039bb2b0`
- bytes: 16007

````python
from __future__ import annotations

import copy
import pickle
from collections.abc import Generator
from typing import Any

import pytest
from typing_extensions import assert_type

from nitypes.vector import TScalar, Vector
from nitypes.waveform._extended_properties import (
    UNIT_DESCRIPTION,
    ExtendedPropertyDictionary,
)


###############################################################################
# create
###############################################################################
def test___no_data_values_no_type___create___raises_type_error() -> None:
    with pytest.raises(TypeError) as exc:
        _ = Vector([])

    assert exc.value.args[0].startswith(
        "You must specify values as non-empty or specify value_type."
    )


def test___no_data_values_bool_type___create___creates_with_bool_type() -> None:
    data = Vector([], value_type=bool)

    assert_type(data._values, list[bool])
    assert data._values == []
    assert data.units == ""
    assert data._value_type == bool


def test___bool_data_values___create___creates_with_bool_data_and_default_units() -> None:
    data = Vector([True, False])

    assert_type(data._values[0], bool)
    assert data._values == [True, False]
    assert data.units == ""


def test___int_data_values___create___creates_with_int_data_and_default_units() -> None:
    data = Vector([10, 20, 30])

    assert_type(data._values[0], int)
    assert data._values == [10, 20, 30]
    assert data.units == ""


def test___float_data_values___create___creates_with_float_data_and_default_units() -> None:
    data = Vector([20.2, 30.3, 40.4])

    assert_type(data._values[0], float)
    assert data._values == [20.2, 30.3, 40.4]
    assert data.units == ""


def test___str_data_values___create___creates_with_str_data_and_default_units() -> None:
    data = Vector(["one", "two"])

    assert_type(data._values[0], str)
    assert data._values == ["one", "two"]
    assert data.units == ""


def test___generator_data_values___create___creates_with_data_and_default_units() -> None:
    def get_values() -> Generator[float]:
        yield 20.2
        yield 30.3
        yield 40.4

    data = Vector(get_values())

    assert_type(data._values[0], float)
    assert data._values == [20.2, 30.3, 40.4]
    assert data.units == ""


@pytest.mark.parametrize("data_value", [True, 10, 20.0, "value"])
@pytest.mark.parametrize("units", ["volts"])
def test___data_value_and_units___create___creates_scalar_data_with_data_and_units(
    data_value: Any, units: str
) -> None:
    expected_data = [data_value] * 5
    data = Vector(expected_data, units)

    assert data._values == expected_data
    assert data.units == units


def test___both_units_specified_unequal__create___raises_value_error() -> None:
    with pytest.raises(ValueError) as exc:
        _ = Vector([10], "Volts", extended_properties={UNIT_DESCRIPTION: "Amps"})

    assert exc.value.args[0].startswith(
        "The specified units input does not match the units specified in extended_properties."
    )


def test___units_only_specified_in_extended_properties__create___creates_with_units() -> None:
    data = Vector([10], extended_properties={UNIT_DESCRIPTION: "Volts"})
    assert data.units == "Volts"


@pytest.mark.parametrize("data_value", [[[1.0, 2.0]], [{"key", "value"}]])
def test___invalid_data_value___create___raises_type_error(data_value: Any) -> None:
    with pytest.raises(TypeError) as exc:
        _ = Vector(data_value)

    assert exc.value.args[0].startswith("The vector input data must be a bool, int, float, or str.")


def test___invalid_generator_data_values___create___raises_type_error() -> None:
    def get_values() -> Generator[Any]:
        yield from [{"value_one", "value_two"}, 1.0, 2.0]

    with pytest.raises(TypeError) as exc:
        _ = Vector(get_values())

    assert exc.value.args[0].startswith("The vector input data must be a bool, int, float, or str.")
    assert "value_one" in exc.value.args[0]


def test___empty_generator_data_values___create___raises_type_error() -> None:
    def get_values() -> Generator[float]:
        yield from []

    with pytest.raises(TypeError) as exc:
        _ = Vector(get_values())

    assert exc.value.args[0].startswith(
        "You must specify values as non-empty or specify value_type."
    )


def test___mixed_data_values___create___raises_type_error() -> None:
    with pytest.raises(TypeError) as exc:
        _ = Vector([True, "string", 1.0])

    assert exc.value.args[0].startswith("All values in the values input must be of the same type.")


###############################################################################
# get_item
###############################################################################
def test___vector_with_data___get_item_at_index___returns_correct_value() -> None:
    vector = Vector([1, 2, 3], "volts")

    assert vector[0] == 1
    assert vector[1] == 2
    assert vector[2] == 3


def test___vector_with_data___get_item_at_slice___returns_correct_values() -> None:
    vector = Vector([1, 2, 3], "volts")

    assert vector[0:2] == [1, 2]
    assert vector[1:3] == [2, 3]
    assert vector[0:] == [1, 2, 3]
    assert vector[:1] == [1]


###############################################################################
# set_item
###############################################################################
def test___vector_with_data___set_item_at_index___value_set_correctly() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector[1] = 4

    assert vector._values == [1, 4, 3]


def test___vector_with_data___set_item_at_slice___values_set_correctly() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector[0:2] = [6, 7]

    assert vector._values == [6, 7, 3]


def test___vector_with_data___set_item_at_slice_with_generator___values_set_correctly() -> None:
    def get_values() -> Generator[int]:
        yield 6
        yield 7

    vector = Vector([1, 2, 3], "volts")

    vector[0:2] = get_values()

    assert vector._values == [6, 7, 3]


def test___vector_with_data___set_item_at_slice_to_empty_list___values_set_correctly() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector[0:2] = []

    assert vector._values == [3]


###############################################################################
# append
###############################################################################
def test___vector_with_data___append_same_type___values_appended() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector.append(4)

    assert vector._values == [1, 2, 3, 4]


def test___vector_with_data___append_different_type___raises_type_error() -> None:
    vector = Vector([1.0, 2.0, 3.0], "volts")

    with pytest.raises(TypeError) as exc:
        vector.append(True)

    assert exc.value.args[0].startswith("Input type does not match existing type.")


def test___no_data_values_bool_type___append___appends_bool_data() -> None:
    data = Vector([], value_type=bool)
    data.append(True)

    assert data._values == [True]


###############################################################################
# extend
###############################################################################
def test___vector_with_data___extend_same_type___values_extended() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector.extend([4, 5])

    assert vector._values == [1, 2, 3, 4, 5]


def test___vector_with_data___extend_different_type___raises_type_error() -> None:
    vector = Vector([1.0, 2.0, 3.0], "volts")

    with pytest.raises(TypeError) as exc:
        vector.extend([True, False])

    assert exc.value.args[0].startswith("Input type does not match existing type.")


def test___vector_with_data___extend_mixed_type___raises_type_error() -> None:
    vector = Vector([1.0, 2.0, 3.0], "volts")

    with pytest.raises(TypeError) as exc:
        vector.extend([4.0, False, 5.0])

    assert exc.value.args[0].startswith("Input type does not match existing type.")


def test___no_data_values_bool_type___extend___extends_bool_data() -> None:
    data = Vector([], value_type=bool)
    data.extend([True, False])

    assert data._values == [True, False]


def test___vector_with_data___extend_with_empty_list___values_unchanged() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector.extend([])

    assert vector._values == [1, 2, 3]


###############################################################################
# delete
###############################################################################
def test___vector_with_data___delete_at_index___value_deleted() -> None:
    vector = Vector([1, 2, 3], "volts")

    del vector[1]

    assert vector._values == [1, 3]


def test___vector_with_data___delete_at_slice___values_deleted() -> None:
    vector = Vector([1, 2, 3], "volts")

    del vector[1:3]

    assert vector._values == [1]


###############################################################################
# remove
###############################################################################
def test___vector_with_data___remove_value___value_removed() -> None:
    vector = Vector([1, 2, 3], "volts")

    vector.remove(2)

    assert vector._values == [1, 3]


###############################################################################
# length
###############################################################################
def test___vector_with_data___check_length___length_correct() -> None:
    vector = Vector([1, 2, 3], "volts")

    assert len(vector) == 3


###############################################################################
# compare
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Vector([False]), Vector([False])),
        (Vector([1]), Vector([1])),
        (Vector([10.0]), Vector([10.0])),
        (Vector(["value"]), Vector(["value"])),
    ],
)
def test___same_value___comparison___equal(left: Vector[TScalar], right: Vector[TScalar]) -> None:
    assert left == right


@pytest.mark.parametrize(
    "left, right",
    [
        (Vector([False]), Vector([True])),
        (Vector([1]), Vector([2])),
        (Vector([10.0]), Vector([20.0])),
        (Vector(["value"]), Vector(["other"])),
    ],
)
def test___different_values___comparison___not_equal(
    left: Vector[TScalar], right: Vector[TScalar]
) -> None:
    assert left != right


def test___different_units___comparison___not_equal() -> None:
    left = Vector([0], "volts")
    right = Vector([0], "amps")

    assert left != right


###############################################################################
# other operators
###############################################################################
@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (Vector([False, True]), "nitypes.vector.Vector(values=[False, True])"),
        (Vector([10, 20]), "nitypes.vector.Vector(values=[10, 20])"),
        (Vector([20.0, 20.1]), "nitypes.vector.Vector(values=[20.0, 20.1])"),
        (Vector(["a", "b"]), "nitypes.vector.Vector(values=['a', 'b'])"),
        (Vector([False, True], "f"), "nitypes.vector.Vector(values=[False, True], units='f')"),
        (Vector([10, 20], "volts"), "nitypes.vector.Vector(values=[10, 20], units='volts')"),
        (Vector([20.0, 20.1], "w"), "nitypes.vector.Vector(values=[20.0, 20.1], units='w')"),
        (Vector(["a", "b"], ""), "nitypes.vector.Vector(values=['a', 'b'])"),
        (
            Vector([10, 20], "volts", extended_properties={"Prop1": "Value1"}),
            "nitypes.vector.Vector(values=[10, 20], units='volts', "
            "extended_properties=nitypes.waveform.ExtendedPropertyDictionary("
            "{'Prop1': 'Value1', 'NI_UnitDescription': 'volts'}))",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: Vector[Any], expected_repr: str) -> None:
    assert repr(value) == expected_repr


@pytest.mark.parametrize(
    "value, expected_str",
    [
        (Vector([], value_type=bool), "[]"),
        (Vector([], "volts", value_type=int), "[]"),
        (Vector([10]), "[10]"),
        (Vector([False, True]), "[False, True]"),
        (Vector([10, 20]), "[10, 20]"),
        (Vector([20.0, 20.1]), "[20.0, 20.1]"),
        (Vector(["a", "b"]), "[a, b]"),
        (Vector([10], "volts"), "[10 volts]"),
        (Vector([False, True], "amps"), "[False amps, True amps]"),
        (Vector([10, 20], "volts"), "[10 volts, 20 volts]"),
        (Vector([20.0, 20.1], "watts"), "[20.0 watts, 20.1 watts]"),
        (Vector(["a", "b"], ""), "[a, b]"),
    ],
)
def test___various_values___str___looks_ok(value: Vector[Any], expected_str: str) -> None:
    assert str(value) == expected_str


###############################################################################
# other properties
###############################################################################
def test___vector_with_units___get_extended_properties___returns_correct_dictionary() -> None:
    value = Vector([20.0], "watts")

    prop_dict = value.extended_properties

    assert isinstance(prop_dict, ExtendedPropertyDictionary)
    assert prop_dict.get(UNIT_DESCRIPTION) == "watts"


def test___vector_with_units___set_units___units_updated_correctly() -> None:
    value = Vector([20.0], "watts")

    value.units = "volts"

    assert value.units == "volts"


@pytest.mark.parametrize(
    "value",
    [
        Vector([False, True]),
        Vector([10, 20]),
        Vector([20.0, 20.1]),
        Vector(["a", "b"]),
        Vector([False, True], "amps"),
        Vector([10, 20], "volts"),
        Vector([20.0, 20.1], "watts"),
        Vector(["a", "b"], ""),
        Vector([10, 20], "volts", extended_properties={"one": 1}),
    ],
)
def test___various_values___copy___makes_copy(value: Vector[TScalar]) -> None:
    new_value = copy.copy(value)
    assert new_value is not value
    assert new_value == value
    assert new_value.extended_properties == value.extended_properties


@pytest.mark.parametrize(
    "value",
    [
        Vector([False, True]),
        Vector([10, 20]),
        Vector([20.0, 20.1]),
        Vector(["a", "b"]),
        Vector([False, True], "amps"),
        Vector([10, 20], "volts"),
        Vector([20.0, 20.1], "watts"),
        Vector(["a", "b"], ""),
        Vector([10, 20], "volts", extended_properties={"one": 1}),
    ],
)
def test___various_values___pickle_unpickle___makes_copy(value: Vector[TScalar]) -> None:
    new_value = pickle.loads(pickle.dumps(value))
    assert isinstance(new_value, Vector)
    assert new_value is not value
    assert new_value == value
    assert new_value.extended_properties == value.extended_properties


def test___vector___pickle___references_public_modules() -> None:
    value = Vector([123, 234])
    value_bytes = pickle.dumps(value)

    assert b"nitypes.vector" in value_bytes
    assert b"nitypes.vector._vector" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95?\x00\x00\x00\x00\x00\x00\x00\x8c\x0enitypes.vector\x94\x8c\x06Vector\x94\x93\x94]\x94(G@4\x00\x00\x00\x00\x00\x00G@4\x19\x99\x99\x99\x99\x9ae\x8c\x05watts\x94\x86\x94R\x94.",
            Vector([20.0, 20.1], "watts"),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: Vector[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/__init__.py sha256=15abf677f553a570ac372a55c02742800840717e6ae76bf2dbdbe5bad837e7d2 bytes=52 -->
## FILE: tests/unit/waveform/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/__init__.py`
- sha256: `15abf677f553a570ac372a55c02742800840717e6ae76bf2dbdbe5bad837e7d2`
- bytes: 52

````python
"""Unit tests for the nitypes.waveform package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_scaling/__init__.py sha256=2ff66be0672e525e6ce3a946003c0a6f215ebd4c1623987d0e622a4311f1bc98 bytes=61 -->
## FILE: tests/unit/waveform/_scaling/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_scaling/__init__.py`
- sha256: `2ff66be0672e525e6ce3a946003c0a6f215ebd4c1623987d0e622a4311f1bc98`
- bytes: 61

````python
"""Unit tests for the nitypes.waveform._scaling package."""
````
