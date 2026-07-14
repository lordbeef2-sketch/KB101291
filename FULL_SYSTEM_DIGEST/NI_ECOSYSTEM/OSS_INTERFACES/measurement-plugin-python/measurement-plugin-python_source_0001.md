# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/CODEOWNERS sha256=6f3e4d4505ac2e0b26be5559011a98fbea8f49dc4767ba572bb5bb01db7f9a4c bytes=332 -->
## FILE: .github/CODEOWNERS

- repository: `ni/measurement-plugin-python`
- source_path: `.github/CODEOWNERS`
- sha256: `6f3e4d4505ac2e0b26be5559011a98fbea8f49dc4767ba572bb5bb01db7f9a4c`
- bytes: 332

````text
# Default code owner for the repository
* @csjall @dixonjoel @bkeryan

# Add mshafer-ni and nstokes-nati for Python files
*.py @csjall @dixonjoel @bkeryan @mshafer-ni @nstokes-nati

# Add nstokes-nati for documentation
*.md @csjall @dixonjoel @bkeryan @nstokes-nati
/_docs_source/ @csjall @dixonjoel @bkeryan @nstokes-nati
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/ISSUE_TEMPLATE/bug_report.md sha256=d3c0eb0231f00837a49f2f26f052624d636bde9ac84c66335f9e04d1c38ec436 bytes=1515 -->
## FILE: .github/ISSUE_TEMPLATE/bug_report.md

- repository: `ni/measurement-plugin-python`
- source_path: `.github/ISSUE_TEMPLATE/bug_report.md`
- sha256: `d3c0eb0231f00837a49f2f26f052624d636bde9ac84c66335f9e04d1c38ec436`
- bytes: 1515

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

* OS & Device: [e.g. macOS, Windows, Linux] on [Mac, PC]
* `ni-measurement-plugin-sdk-service` version [e.g. 2.0.0]
* InstrumentStudio version [e.g. 24.8.0d123]
* Python version [e.g. 3.10]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/ISSUE_TEMPLATE/feature_request.md sha256=e00ddb5b02a84de7f991b8a86a1bc750d91141603aad727f2a85d4c0bc8be6b1 bytes=712 -->
## FILE: .github/ISSUE_TEMPLATE/feature_request.md

- repository: `ni/measurement-plugin-python`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/ISSUE_TEMPLATE/tech_debt.md sha256=a80e6afbbd5f723466dab578104fedfe7d38413e65714a4e5ccb40d1d35389d0 bytes=164 -->
## FILE: .github/ISSUE_TEMPLATE/tech_debt.md

- repository: `ni/measurement-plugin-python`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/ISSUE_TEMPLATE/user_story.md sha256=db24cb4a5576436f0dd3e0fbfd2d95a20336d2aa1c5d68cddbd5a717dc993012 bytes=321 -->
## FILE: .github/ISSUE_TEMPLATE/user_story.md

- repository: `ni/measurement-plugin-python`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=8587f13ae0ce4663eee9bbdf284c1adbba632b8ca98e97b9e25b72359482f74d bytes=670 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/measurement-plugin-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `8587f13ae0ce4663eee9bbdf284c1adbba632b8ca98e97b9e25b72359482f74d`
- bytes: 670

````markdown
<!-- TODO: Check the below box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/measurement-plugin-python/blob/main/CONTRIBUTING.md) -->
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/measurement-plugin-python/blob/main/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/renovate.json sha256=562305ca950291a9d78bbc9413c52d7372f653351cf64f88b38b020405e0a95d bytes=558 -->
## FILE: .github/renovate.json

- repository: `ni/measurement-plugin-python`
- source_path: `.github/renovate.json`
- sha256: `562305ca950291a9d78bbc9413c52d7372f653351cf64f88b38b020405e0a95d`
- bytes: 558

````json
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "extends": [
        "local>ni/python-renovate-config:recommended",
        "local>ni/python-renovate-config//presets/enableGitSubmodules"
    ],
    "packageRules": [
        {
            "description": "Update ni-apis on early Monday mornings.",
            "matchDepNames": [
                "third_party/ni-apis"
            ],
            "extends": [
                "schedule:monthly"
            ],
            "minimumReleaseAge": "1 day"
        }
    ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/check_examples.yml sha256=8e805b7817853aafe3bff3a2490651c2a56210870dabd148bb428610c62d98ee bytes=2945 -->
## FILE: .github/workflows/check_examples.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/check_examples.yml`
- sha256: `8e805b7817853aafe3bff3a2490651c2a56210870dabd148bb428610c62d98ee`
- bytes: 2945

````yaml
name: Check examples

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_examples:
    name: Check examples
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
      # Updating poetry.lock for all of the examples takes over 6 minutes, so it's worth caching.
      - name: Cache poetry.lock
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: cache-poetry-lock
        with:
          path: 'examples/**/poetry.lock'
          # Include the main project's poetry.lock in the hash to detect upstream dependency updates.
          key: examples-poetry-lock-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('examples/**/pyproject.toml', 'packages/service/poetry.lock') }}
      - name: Lock examples
        if: steps.cache-poetry-lock.outputs.cache-hit != 'true'
        run: |
          for example in examples/*/; do
            echo "::group::$example"
            pushd $example
            poetry lock
            popd
            echo "::endgroup::"
          done
      - name: Cache virtualenvs
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: cache-venv
        with:
          path: 'examples/**/.venv'
          key: examples-venv-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('examples/**/poetry.lock') }}
      - name: Install examples
        run: |
          for example in examples/*/; do
            echo "::group::$example"
            pushd $example
            poetry install -v
            popd
            echo "::endgroup::"
          done
      - name: Lint examples
        run: |
          for example in examples/*/; do
            echo "::group::$example"
            pushd $example
            poetry run ni-python-styleguide lint
            popd
            echo "::endgroup::"
          done
      - name: Mypy static analysis (examples, Linux)
        run: |
          for example in examples/*/; do
            echo "::group::$example"
            pushd $example
            poetry run mypy .
            popd
            echo "::endgroup::"
          done
      - name: Mypy static analysis (examples, Windows)
        run: |
          for example in examples/*/; do
            echo "::group::$example"
            pushd $example
            poetry run mypy . --platform win32
            popd
            echo "::endgroup::"
          done
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/check_nimg.yml sha256=53c48a8d0812202f4b367f949ff5a0ecb46b4ac5e7c7708598290834355a8346 bytes=2154 -->
## FILE: .github/workflows/check_nimg.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/check_nimg.yml`
- sha256: `53c48a8d0812202f4b367f949ff5a0ecb46b4ac5e7c7708598290834355a8346`
- bytes: 2154

````yaml
name: Check NIMG

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_nimg:
    name: Check NIMG
    env:
      oldest-python-version: '3.10'
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        python-version: ['3.10', 3.14]
    runs-on: ${{ matrix.os }}
    defaults:
      run:
        # Set the working-directory for all steps in this job.
        working-directory: ./packages/generator
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
      - name: Analyze generator
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: packages/generator
      - name: Bandit security checks (ni-measurement-plugin-sdk-generator, example_renders)
        run:  poetry run bandit -c pyproject.toml -r ni_measurement_plugin_sdk_generator tests/test_assets/example_renders
      - name: Generate gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run: |
          find tests/utilities/measurements/non_streaming_data_measurement/_stubs -name \*_pb2.py\* -o -name \*_pb2_grpc.py\* -delete
          poetry run python scripts/generate_grpc_stubs.py
      - name: Check for out-of-date gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run:  git diff --exit-code
      - name: Revert gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run: |
          git clean -dfx tests/utilities/measurements/non_streaming_data_measurement/_stubs
          git restore tests/utilities/measurements/non_streaming_data_measurement/_stubs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/check_nims.yml sha256=41728fc361dddc9a23166674a47255c5141d88a475aa0aff96198f087d84a945 bytes=2029 -->
## FILE: .github/workflows/check_nims.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/check_nims.yml`
- sha256: `41728fc361dddc9a23166674a47255c5141d88a475aa0aff96198f087d84a945`
- bytes: 2029

````yaml
name: Check NIMS

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_nims:
    name: Check NIMS
    env:
      oldest-python-version: '3.10'
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        python-version: ['3.10', 3.14]
    runs-on: ${{ matrix.os }}
    defaults:
      run:
        # Set the working-directory for all steps in this job.
        working-directory: ./packages/service
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Analyze generator
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: packages/service
          install-args: --all-extras
      - name: Bandit security checks (ni-measurement-plugin-sdk-service)
        run:  poetry run bandit -c pyproject.toml -r ni_measurement_plugin_sdk_service
      - name: Generate gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run: |
          find tests/utilities/stubs/ -name \*_pb2.py\* -o -name \*_pb2_grpc.py\* -delete
          poetry run python scripts/generate_grpc_stubs.py
      - name: Check for out-of-date gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run:  git diff --exit-code
      - name: Revert gRPC stubs
        if: matrix.python-version == env.oldest-python-version
        run: |
          git clean -dfx tests/utilities/stubs/
          git restore tests/utilities/stubs/
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/check_nims_docs.yml sha256=e8a63666a342a907d6ebb566ca506dea421f1063b9a036bb3c349a7b597c2c65 bytes=1161 -->
## FILE: .github/workflows/check_nims_docs.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/check_nims_docs.yml`
- sha256: `e8a63666a342a907d6ebb566ca506dea421f1063b9a036bb3c349a7b597c2c65`
- bytes: 1161

````yaml
name: Check NIMS Docs

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  check_nims:
    name: Check NIMS Docs
    runs-on: ubuntu-latest
    defaults:
      run:
        # Set the working-directory for all steps in this job.
        working-directory: ./packages/service
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Install ni-measurement-plugin-sdk-service (all extras, docs)
        run: poetry install -v --all-extras --with docs
      - name: Build docs and check for errors/warnings
        run: |
          rm -rf docs
          mkdir -p docs   
          poetry run sphinx-build _docs_source docs -b html -W
      - name: Revert docs
        run:  rm -rf docs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/check_workflows.yml sha256=e00c7fb6d0a5207cb751edb5b39eeb643512d2e4de96419e8fc6cbdbbd9601c1 bytes=498 -->
## FILE: .github/workflows/check_workflows.yml

- repository: `ni/measurement-plugin-python`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/CI.yml sha256=68234518f433781fa7a7cf9aa5ccfd4a07149d91ac5bf1d0dd3eab9e13d25ef6 bytes=1324 -->
## FILE: .github/workflows/CI.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/CI.yml`
- sha256: `68234518f433781fa7a7cf9aa5ccfd4a07149d91ac5bf1d0dd3eab9e13d25ef6`
- bytes: 1324

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
  check_nims:
    name: Check NIMS
    uses: ./.github/workflows/check_nims.yml
  check_nims_docs:
    name: Check NIMS docs
    uses: ./.github/workflows/check_nims_docs.yml
  check_nimg:
    name: Check NIMG
    uses: ./.github/workflows/check_nimg.yml
  check_workflows:
    name: Check workflows
    uses: ./.github/workflows/check_workflows.yml
    permissions:
      security-events: write
  checks_succeeded:
    name: Checks succeeded
    needs: [check_nims, check_nims_docs, check_nimg, check_workflows]
    runs-on: ubuntu-latest
    steps:
      - run: exit 0
  check_examples:
    name: Check examples
    uses: ./.github/workflows/check_examples.yml
  run_unit_tests:
    name: Run unit tests
    uses: ./.github/workflows/run_unit_tests.yml
    needs: [check_nims]
  run_system_tests:
    name: Run system tests
    uses: ./.github/workflows/run_system_tests.yml
    needs: [run_unit_tests]
  report_test_results:
    name: Report test results
    uses: ./.github/workflows/report_test_results.yml
    needs: [run_unit_tests, run_system_tests]
    if: always()
    permissions:
      checks: write
      pull-requests: write
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/PR.yml sha256=f56ab1c82743b483c1244f373760add8fbb6f45b260dcdb3b6d3c895da06fedb bytes=447 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/PR.yml`
- sha256: `f56ab1c82743b483c1244f373760add8fbb6f45b260dcdb3b6d3c895da06fedb`
- bytes: 447

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
      checks: write
      pull-requests: write
      security-events: write
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/publish.yml sha256=2486d4530ac571b3e68fdb9d08768335284e751769e4f8f06113c0e3b70994ad bytes=7139 -->
## FILE: .github/workflows/publish.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/publish.yml`
- sha256: `2486d4530ac571b3e68fdb9d08768335284e751769e4f8f06113c0e3b70994ad`
- bytes: 7139

````yaml
name: Publish NIMS

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
  package-name: |
    {
      "generator": "ni_measurement_plugin_sdk_generator",
      "sdk": "ni_measurement_plugin_sdk",
      "service": "ni_measurement_plugin_sdk_service"
    }

permissions: {}

jobs:
  # Do not call check_examples.yml because the examples may depend on the version we are releasing.
  check_nimg:
    name: Check generator
    uses: ./.github/workflows/check_nimg.yml
  check_nims:
    name: Check service
    uses: ./.github/workflows/check_nims.yml
  check_nims_docs:
    name: Check NIMS docs
    uses: ./.github/workflows/check_nims_docs.yml
  build_package:
    name: Build ${{ matrix.package }}
    runs-on: ubuntu-latest
    needs: [check_nimg, check_nims, check_nims_docs]
    strategy:
      matrix:
        package: [generator, sdk, service]
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
        with:
          project-directory: ./packages/${{ matrix.package }}
      - name: Build distribution packages
        run: poetry build
        working-directory: ./packages/${{ matrix.package }}
      - name: Upload build artifacts
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: ${{ matrix.package }}-distribution-packages
          path: ./packages/${{ matrix.package }}/dist/*
  publish_package:
    name: Publish ${{ matrix.package }} to PyPI
    if: github.event_name == 'release' || inputs.environment != 'none'
    runs-on: ubuntu-latest
    needs: [build_package]
    environment:
      # This logic is duplicated because `name` doesn't support the `env` context.
      name: ${{ github.event_name == 'release' && 'pypi' || inputs.environment }}
      url: ${{ fromJson(env.environment-info)[env.environment].base-url }}/p/${{ fromJson(env.package-name)[matrix.package] }}
    permissions:
      id-token: write
    strategy:
      matrix:
        package: [generator, sdk, service]
    steps:
    - name: Download build artifacts
      uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
      with:
        name: ${{ matrix.package }}-distribution-packages
        path: dist/
    - run: ls -lR
    - name: Upload to ${{ env.environment }}
      uses: pypa/gh-action-pypi-publish@cef221092ed1bacb1cc03d23a2d87d1d172e277b # v1.14.0
      with:
        repository-url: ${{ fromJson(env.environment-info)[env.environment].upload-url }}
  publish_examples:
    name: Publish examples
    runs-on: ubuntu-latest
    needs: [check_nimg, check_nims]
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
      - name: Get version
        id: get-version
        run: echo "version=$(poetry version --short)" >> "$GITHUB_OUTPUT"
        working-directory: ./packages/service
      - name: Create archives of the examples
        env:
          EXAMPLE_ARCHIVE: measurement-plugin-python-examples-${{ steps.get-version.outputs.version }}
        run: |
          # Use --prefix for the tarball but not the zip file. Windows zip tools often create a directory automatically.
          rm -rf dist
          mkdir -p dist
          git archive -o dist/${EXAMPLE_ARCHIVE}.zip ${GITHUB_REF}:examples/
          git archive -o dist/${EXAMPLE_ARCHIVE}.tar.gz --prefix ${EXAMPLE_ARCHIVE}/ ${GITHUB_REF}:examples/
      - name: Upload release assets # zizmor: ignore[superfluous-actions]
        if: ${{ startsWith(github.event.release.target_commitish, 'main') || startsWith(github.event.release.target_commitish, 'releases/') }}
        uses: ncipollo/release-action@339a81892b84b4eeb0f6e744e4574d79d0d9b8dd # v1.21.0
        with:
          artifacts: "dist/measurement-plugin-python-examples-*"
          allowUpdates: true
          omitBodyDuringUpdate: true
          omitDraftDuringUpdate: true
          omitNameDuringUpdate: true
          omitPrereleaseDuringUpdate: true
          updateOnlyUnreleased: false
  update_versions:
    name: Update package versions
    runs-on: ubuntu-latest
    needs: [build_package]
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
      # Create one pull request that updates all three packages.
      - name: Update generator project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: ./packages/generator
          create-pull-request: false
      - name: Update sdk project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: ./packages/sdk
          create-pull-request: false
      - name: Update service project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          project-directory: ./packages/service
          create-pull-request: true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/report_test_results.yml sha256=ac2fd3c2054c377a0bf6042de71806e1554ff52bb85ba9fc556d8286d728b94f bytes=949 -->
## FILE: .github/workflows/report_test_results.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/report_test_results.yml`
- sha256: `ac2fd3c2054c377a0bf6042de71806e1554ff52bb85ba9fc556d8286d728b94f`
- bytes: 949

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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/run_system_tests.yml sha256=7fa73c19cc1799bf3550a1cd25d282acaa610458d60c94398bb13b91175a8a1f bytes=2658 -->
## FILE: .github/workflows/run_system_tests.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/run_system_tests.yml`
- sha256: `7fa73c19cc1799bf3550a1cd25d282acaa610458d60c94398bb13b91175a8a1f`
- bytes: 2658

````yaml
name: Run system tests

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  run_system_tests:
    name: Run system tests
    runs-on: 
      - self-hosted
      - windows
      - x64
      - rdss-measlinkbot-win-10-${{ matrix.configuration }}
    strategy:
      matrix:
        configuration: ["py32", "py64"]
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    timeout-minutes: 90
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Copy and rename .env.simulation to .env
        run: cp examples/.env.simulation .env

      # ni-measurement-plugin-sdk-service  
      - name: Cache virtualenv (ni-measurement-plugin-sdk-service)
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: cache-nims
        with:
          path: |
            packages/service/.venv
            packages/service/.tox
          key: run-system-tests-nims-${{ runner.os }}-${{ matrix.configuration }}-${{ hashFiles('packages/service/poetry.lock') }}
      - name: Install dependencies (ni-measurement-plugin-sdk-service)
        run: poetry install -v
        working-directory: ./packages/service
      - name: Run system tests (ni-measurement-plugin-sdk-service)
        run: poetry run tox
        working-directory: ./packages/service

      # ni-measurement-plugin-sdk-generator
      - name: Cache virtualenv (ni-measurement-plugin-sdk-generator)
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: cache-nimg
        with:
          path: |
            packages/generator/.venv
            packages/generator/.tox
          key: run-system-tests-nimg-${{ runner.os }}-${{ matrix.configuration }}-${{ hashFiles('packages/generator/poetry.lock') }}
      - name: Install dependencies (ni-measurement-plugin-sdk-generator)
        run: poetry install -v
        working-directory: ./packages/generator
      - name: Run system tests (ni-measurement-plugin-sdk-generator)
        run: poetry run tox
        working-directory: ./packages/generator

      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_system_${{ matrix.configuration }}
          path: |
            ./packages/generator/test_results/*.xml
            ./packages/service/test_results/*.xml
        if: always()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/run_unit_tests.yml sha256=195d36716d7f604ec8be2b36d221acd26cd1bdb66e66f0499c7c319d1878ca67 bytes=4068 -->
## FILE: .github/workflows/run_unit_tests.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/run_unit_tests.yml`
- sha256: `195d36716d7f604ec8be2b36d221acd26cd1bdb66e66f0499c7c319d1878ca67`
- bytes: 4068

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
        os: [windows-latest, ubuntu-latest]
        # grpcio does not have binary wheels for pypy or free-threading, as of version 1.75.1.
        python-version: ['3.10', 3.11, 3.12, 3.13, 3.14]
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

      # ni-measurement-plugin-sdk-service, no extras
      - name: Restore cached virtualenv (ni-measurement-plugin-sdk-service, no extras)
        uses: actions/cache/restore@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: restore-nims-no-extras
        with:
          path: packages/service/.venv
          key: ni-measurement-plugin-sdk-service-no-extras-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('packages/service/poetry.lock') }}
      - name: Install ni-measurement-plugin-sdk-service (no extras)
        run: poetry install -v
        working-directory: ./packages/service
      - name: Save cached virtualenv (ni-measurement-plugin-sdk-service, no extras)
        uses: actions/cache/save@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        if: steps.restore-nims-no-extras.outputs.cache-hit != 'true'
        with:
          path: packages/service/.venv
          key: ${{ steps.restore-nims-no-extras.outputs.cache-primary-key }}
      - name: Run unit tests and code coverage (ni-measurement-plugin-sdk-service, no extras)
        run: poetry run pytest ./tests/unit -v --cov=ni_measurement_plugin_sdk_service --junitxml=test_results/nims-${{ matrix.os }}-py${{ matrix.python-version}}-no-extras.xml
        working-directory: ./packages/service

      # ni-measurement-plugin-sdk-service, all extras
      - name: Restore cached virtualenv (ni-measurement-plugin-sdk-service, all extras)
        uses: actions/cache/restore@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: restore-nims-all-extras
        with:
          path: packages/service/.venv
          key: ni-measurement-plugin-sdk-service-all-extras-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('packages/service/poetry.lock') }}
      - name: Install ni-measurement-plugin-sdk-service (all extras)
        run: poetry install -v --all-extras
        working-directory: ./packages/service
      - name: Save cached ni-measurement-plugin-sdk-service virtualenv (all extras)
        uses: actions/cache/save@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        if: steps.restore-nims-all-extras.outputs.cache-hit != 'true'
        with:
          path: packages/service/.venv
          key: ${{ steps.restore-nims-all-extras.outputs.cache-primary-key }}
      - name: Run unit tests and code coverage (ni-measurement-plugin-sdk-service, all extras)
        run: poetry run pytest ./tests/unit -v --cov=ni_measurement_plugin_sdk_service --junitxml=test_results/nims-${{ matrix.os }}-py${{ matrix.python-version}}-all-extras.xml
        working-directory: ./packages/service

      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_unit_${{ matrix.os }}_py${{ matrix.python-version }}
          path: ./packages/service/test_results/*.xml
        if: always()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.github/workflows/sync_github_issues_to_azdo.yml sha256=57638a589eea6ece062a49cfae561bed11bf890cba013768f98557dd1e4a37b3 bytes=1397 -->
## FILE: .github/workflows/sync_github_issues_to_azdo.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.github/workflows/sync_github_issues_to_azdo.yml`
- sha256: `57638a589eea6ece062a49cfae561bed11bf890cba013768f98557dd1e4a37b3`
- bytes: 1397

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
          ado_area_path: "DevCentral\\Product RnD\\Platform HW and SW\\SW New Invest and Tech\\ETW\\InstrumentStudio\\Core\\Platform"
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.gitignore sha256=7cc020b50a74b8fb42bc6eeb6c1a8c7dad1987e206ca6a977fdbab6d98d367a3 bytes=3042 -->
## FILE: .gitignore

- repository: `ni/measurement-plugin-python`
- source_path: `.gitignore`
- sha256: `7cc020b50a74b8fb42bc6eeb6c1a8c7dad1987e206ca6a977fdbab6d98d367a3`
- bytes: 3042

````text
#VS Code 
.vscode/

# VS
.vs/

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
share/python-wheels/
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
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/
test_results/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# Don't lock dependencies for example services.
/examples/**/poetry.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

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
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintainted in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.gitmodules sha256=bc64a236366fe63e09e578e7b969ac257e587513dcd45b994882dd37cc4dbee3 bytes=106 -->
## FILE: .gitmodules

- repository: `ni/measurement-plugin-python`
- source_path: `.gitmodules`
- sha256: `bc64a236366fe63e09e578e7b969ac257e587513dcd45b994882dd37cc4dbee3`
- bytes: 106

````text
[submodule "third_party/ni-apis"]
	path = third_party/ni-apis
	url = https://github.com/ni/ni-apis.git
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.readthedocs.yml sha256=bf32de1a0b59226cd1546ec29f22c481941bac4a53304a05b524e8acfdc54777 bytes=328 -->
## FILE: .readthedocs.yml

- repository: `ni/measurement-plugin-python`
- source_path: `.readthedocs.yml`
- sha256: `bf32de1a0b59226cd1546ec29f22c481941bac4a53304a05b524e8acfdc54777`
- bytes: 328

````yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.11"
  jobs:
    post_create_environment:
      - pip install poetry==1.8.2
    post_install:
      - VIRTUAL_ENV=$READTHEDOCS_VIRTUALENV_PATH poetry -C packages/service/ install --with docs

sphinx:
  configuration: packages/service/_docs_source/conf.py
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=.rgignore sha256=d6491addeb39ce28f4f78677a07b6b19980f007f725dc0665d4d26d242447ca1 bytes=7 -->
## FILE: .rgignore

- repository: `ni/measurement-plugin-python`
- source_path: `.rgignore`
- sha256: `d6491addeb39ce28f4f78677a07b6b19980f007f725dc0665d4d26d242447ca1`
- bytes: 7

````text
/docs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=CONTRIBUTING.md sha256=925a3dfe78b062e465ff9c58a12de3298708fed9f226b15844e0a181ec017151 bytes=10576 -->
## FILE: CONTRIBUTING.md

- repository: `ni/measurement-plugin-python`
- source_path: `CONTRIBUTING.md`
- sha256: `925a3dfe78b062e465ff9c58a12de3298708fed9f226b15844e0a181ec017151`
- bytes: 10576

````markdown
# Contributing to Measurement Plug-In SDK for Python

Contributions to Measurement Plug-In SDK for Python are welcome from all!

Measurement Plug-In SDK for Python is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/measurement-plugin-python/). The repo contains templates and examples for developing measurement plug-ins in Python.

Measurement Plug-In SDK for Python follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

Please remember to sign off your commits (e.g., by using `git commit -s` if you
are using the command-line client). This amends your git commit message with a line
of the form `Signed-off-by: Name LastName <name.lastmail@emailaddress.com>`. Please
include all authors of any given commit into the commit message with a
`Signed-off-by` line. This indicates that you have read and signed the Developer
Certificate of Origin (see below) and can legally submit your code to
this repository.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

## Prerequisites

- (Optional) Install [Visual Studio Code](https://code.visualstudio.com/download).
- Install Git.
- Install Python and add it to the `PATH`. For the recommended Python version,
  see [Dependencies](README.md#dependencies).
- Install [Poetry](https://python-poetry.org/docs/#installation). Version >= 1.8.2

## Clone or Update the Git Repository

To download the Measurement Plug-In SDK for Python source, clone its Git
repository to your local PC.

```cmd
git clone --recurse-submodules https://github.com/ni/measurement-plugin-python.git
```

Specifying `--recurse-submodules` includes the
[ni-apis](https://github.com/ni/ni-apis) repository. This is required for the
[update gRPC stubs](#update-grpc-stubs-if-needed)
workflow.

If you already have the Git repository on your local PC, you can update it and
its submodules.

```cmd
git checkout main
git pull
git submodule update --init --recursive
```

## Select a Package to Develop

The Measurement Plug-In SDK for Python includes multiple Python packages:
- [ni_measurement_plugin_sdk_generator](/packages/generator/): Code generator
  for creating new Measurement Plug-In services and clients
- [ni_measurement_plugin_sdk_service](/packages/service/): Shared code used by
  Measurement Plug-In services and clients
- [ni_measurement_plugin_sdk](/packages/sdk/): Meta-package for installing both
  `ni_measurement_plugin_sdk_generator` and `ni_measurement_plugin_sdk_service`

Open a terminal window and `cd` to the package that you want to develop.

```cmd
cd packages\service
```

## Install the Package and Its Dependencies

From the package's subdirectory, run the [`poetry install`](https://python-poetry.org/docs/cli/#install) 
command. This creates an in-project virtual environment (`.venv`) and installs
the package's dependencies and dev-dependencies, as specified in its
`pyproject.toml` and `poetry.lock` files.

```cmd
poetry install
```

For `ni_measurement_plugin_sdk_service`, you may also want to install the
package's extra dependencies. This will install the NI driver API packages that
are supported for session management.

```cmd
poetry install --all-extras
```

## Activate the Virtual Environment (If Needed)

- (Preferred) Prefix commands with `poetry run`, e.g. `poetry run python measurement.py`
- In the command prompt: `poetry shell`
- In VS Code ([link](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment))

# Update gRPC Stubs (If Needed)

The `packages/service/ni_measurement_plugin_sdk_service/_internal/stubs` directory contains the
auto-generated Python files based on Measurement Plug-In protobuf (`.proto`) files. The file needs
to be replaced whenever there is a change to these `.proto` files:

- `ni/measurementlink/**/*.proto`
- `ni/grpcdevice/v1/session.proto`

The latest `.proto` files are available in the [ni-apis](https://github.com/ni/ni-apis) repo. This
repo includes the `ni-apis` repo as a Git submodule in `third_party/ni-apis`.

To regenerate the gRPC stubs, `cd` to the `packages/service` directory, install
it with `poetry install`, and run `poetry run python scripts/generate_grpc_stubs.py`. 
This generates the required `.py` files for the listed `.proto` files. The
required `grpcio-tools` package is already added as a development dependency in
`pyproject.toml`.

# Lint and Build Code

## Lint Code for Style and Formatting

Use [ni-python-styleguide](https://github.com/ni/python-styleguide) to lint the
code for style and formatting. This runs other tools such as `flake8`,
`pycodestyle`, and `black`.

```cmd
poetry run ni-python-styleguide lint
```

If there are any failures, try using `ni-python-styleguide` to fix them, then
lint the code again. If `ni-python-styleguide` doesn't fix the failures, you
will have to manually fix them.

```cmd
poetry run ni-python-styleguide fix
poetry run ni-python-styleguide lint
```

## Mypy Type Checking

Use [Mypy](https://pypi.org/project/mypy/) to type check the code.

```cmd
poetry run mypy
```

## Bandit Security Checks

Use [Bandit](https://pypi.org/project/bandit/) to check for common security issues.

```cmd
poetry run bandit -c pyproject.toml -r ni_measurement_plugin_sdk_service
```

For the exact command line for each package, see the corresponding Github workflows: [check_nimg.yml](/.github/workflows/check_nimg.yml) [check_nims.yml](/.github/workflows/check_nims.yml)

## Build Distribution Packages

To build distribution packages, run `poetry build`. This generates installable
distribution packages (source distributions and wheels) in the `dist`
subdirectory.

```cmd
poetry build
```

## Build Documentation

The `ni_measurement_plugin_sdk_service` package uses Sphinx to build API
reference documentation.

```cmd
poetry run sphinx-build _docs_source docs -b html -W
```

The generated documentation is at `docs/index.html`.

# Testing

`ni-measurement-plugin-sdk-service` includes regression tests under the `tests/`
directory. The GitHub CI runs these tests for PRs targeting the main branch. It
is recommended that during development you run the tests locally before creating
a PR.

Some of the regression tests require InstrumentStudio and NI drivers to be
installed. 

In order to run the `ni-measurement-plugin-sdk-service` tests locally:

## Using Command Line

1. Install production dependencies and development dependencies into a venv by
running `poetry install --all-extras`.
2. Some tests will be skipped if the required components included with
InstrumentStudio are not installed. Install the latest version of
InstrumentStudio to run all tests.
3. Some tests require simulated hardware. Copy `examples\.env.simulation`
to the root measurement-plugin-python directory and rename it to `.env` to simulate
the required devices.

    ```ps
    cp .\examples\.env.simulation .env
    ```
4. Some DAQmx tests require persistent simulated devices created using `NI MAX` or
the `NI Hardware Configuration Utility`. They require a DAQmx device that supports
AI voltage measurements (e.g. PCIe-6363 or other X Series device). To simulate a
DAQmx device in software: open `NI MAX`, right-click `Devices and Interfaces`,
select `Create New...`, and select `Simulated NI-DAQmx Device or Modular
Instrument`. For the DAQmx tests to pass, you will need two DAQmx devices named 'Dev1'
and 'Dev2'.
5. Execute the command `poetry run pytest -v` to run the tests, from the repo's
   root directory.

    ``` ps
    (.venv) PS D:\git\measurement-plugin-python> poetry run pytest -v
    ```

## Using VS Code Test Explorer extension (UI)

Install and configure the `Python Test Explorer for Visual Studio Code`
extension to execute/debug the tests using UI. For more details related to the
extension, refer
[here](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter).

## Generate a Code Coverage Report

- Install the required dependency by running `poetry install`
- Run the command `poetry run pytest --cov=ni_measurement_plugin_sdk_service` to
  print a test coverage summary in the console window.
- Run the command `poetry run pytest --cov-report html:cov_html --cov=ni_measurement_plugin_sdk_service` 
  to generate detailed HTML based coverage report. Upon running, the coverage
  reports will be created under `<repo_root>\cov_html` directory.

# Adding Dependencies

You can add new dependencies using `poetry add` or by editing the `pyproject.toml` file.

When adding new dependencies, use a `>=` version constraint (instead of `^`)
unless the dependency uses semantic versioning.

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open-source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open-source license (unless I am
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

See [LICENSE](https://github.com/ni/measurement-plugin-python/blob/master/LICENSE)
for details about how Measurement Plug-In SDK for Python is licensed.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=docs/CNAME sha256=3e7207f5b60b8737447bbef01c913c5da5c6a465fe7591968f595d4f5cfc37c0 bytes=40 -->
## FILE: docs/CNAME

- repository: `ni/measurement-plugin-python`
- source_path: `docs/CNAME`
- sha256: `3e7207f5b60b8737447bbef01c913c5da5c6a465fe7591968f595d4f5cfc37c0`
- bytes: 40

````text
measurement-plugin-python.readthedocs.io
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/.env.sample sha256=3af38f66c7604c0168cc8c062d7efb61918b4245bb0327daf4a859063ccf00ea bytes=3142 -->
## FILE: examples/.env.sample

- repository: `ni/measurement-plugin-python`
- source_path: `examples/.env.sample`
- sha256: `3af38f66c7604c0168cc8c062d7efb61918b4245bb0327daf4a859063ccf00ea`
- bytes: 3142

````text
# This is a sample ni-measurement-plugin-sdk-service configuration file.
#
# To use it:
# - Copy this file to your service's directory or one of its parent directories
#   (such as the root of your Git repository or `C:\ProgramData\National
#   Instruments\Plug-Ins\Measurements` for statically registered measurement services).
# - Rename it to `.env`.
# - Uncomment and edit the options you want to change.
# - Restart any affected services.

#----------------------------------------------------------------------
# NI Modular Instrument Options
#----------------------------------------------------------------------

# By default, measurement services expect a real device or a simulated device
# configured in NI MAX.
#
# For NI modular instrument drivers, you can also enable simulation via the
# driver's option string. To do this, specify the `options` parameter when
# calling reservation.create_session(s) or uncomment the following options:

# MEASUREMENT_PLUGIN_NIDCPOWER_SIMULATE=1
# MEASUREMENT_PLUGIN_NIDCPOWER_BOARD_TYPE=PXIe
# MEASUREMENT_PLUGIN_NIDCPOWER_MODEL=4141

# MEASUREMENT_PLUGIN_NIDIGITAL_SIMULATE=1
# MEASUREMENT_PLUGIN_NIDIGITAL_BOARD_TYPE=PXIe
# MEASUREMENT_PLUGIN_NIDIGITAL_MODEL=6570

# MEASUREMENT_PLUGIN_NIDMM_SIMULATE=1
# MEASUREMENT_PLUGIN_NIDMM_BOARD_TYPE=PXIe
# MEASUREMENT_PLUGIN_NIDMM_MODEL=4081

# MEASUREMENT_PLUGIN_NIFGEN_SIMULATE=1
# MEASUREMENT_PLUGIN_NIFGEN_BOARD_TYPE=PXIe
# MEASUREMENT_PLUGIN_NIFGEN_MODEL=5423 (2CH)

# MEASUREMENT_PLUGIN_NISCOPE_SIMULATE=1
# MEASUREMENT_PLUGIN_NISCOPE_BOARD_TYPE=PXIe
# MEASUREMENT_PLUGIN_NISCOPE_MODEL=5162 (4CH)

# MEASUREMENT_PLUGIN_NISWITCH_SIMULATE=1
# MEASUREMENT_PLUGIN_NISWITCH_TOPOLOGY=2567/Independent

# MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE=1
# MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY=2529/2-Wire Dual 4x16 Matrix

#----------------------------------------------------------------------
# VISA Example Measurement Options
#----------------------------------------------------------------------

# To enable simulation with the VISA example measurements, uncomment the
# following line.

# MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE=1

#----------------------------------------------------------------------
# NI gRPC Device Server Configuration
#----------------------------------------------------------------------

# By default, measurement services use the NI Discovery Service to
# activate the NI gRPC Device Server. You probably don't want to change this,
# but if you do, you can uncomment the following options to override this
# behavior:
#
# MEASUREMENT_PLUGIN_USE_GRPC_DEVICE_SERVER=1
# MEASUREMENT_PLUGIN_GRPC_DEVICE_SERVER_ADDRESS=http://localhost:31763

#----------------------------------------------------------------------
# Feature Toggles
#----------------------------------------------------------------------

# Enable all features with a code readiness of "incomplete" or "next-release"
# MEASUREMENT_PLUGIN_ALLOW_INCOMPLETE=1

# Enable all features with a code readiness of "next-release"
# MEASUREMENT_PLUGIN_ALLOW_NEXT_RELEASE=1
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/.env.simulation sha256=090ed8ba720148352fa06787d4ed3bcc4f45934c7096560821d152acbaf7e44f bytes=1462 -->
## FILE: examples/.env.simulation

- repository: `ni/measurement-plugin-python`
- source_path: `examples/.env.simulation`
- sha256: `090ed8ba720148352fa06787d4ed3bcc4f45934c7096560821d152acbaf7e44f`
- bytes: 1462

````text
# This is a sample ni-measurement-plugin-sdk-service configuration file that enables
# simulated devices for NI modular instrument drivers and VISA example
# measurements.
#
# To use it:
# - Copy this file to your service's directory or one of its parent directories
#   (such as the root of your Git repository or `C:\ProgramData\National
#   Instruments\Plug-Ins\Measurements` for statically registered measurement services).
# - Rename it to `.env`.
# - Comment out or edit the options you want to change.
# - Restart any affected services.

MEASUREMENT_PLUGIN_NIDCPOWER_SIMULATE=1
MEASUREMENT_PLUGIN_NIDCPOWER_BOARD_TYPE=PXIe
MEASUREMENT_PLUGIN_NIDCPOWER_MODEL=4141

MEASUREMENT_PLUGIN_NIDIGITAL_SIMULATE=1
MEASUREMENT_PLUGIN_NIDIGITAL_BOARD_TYPE=PXIe
MEASUREMENT_PLUGIN_NIDIGITAL_MODEL=6570

MEASUREMENT_PLUGIN_NIDMM_SIMULATE=1
MEASUREMENT_PLUGIN_NIDMM_BOARD_TYPE=PXIe
MEASUREMENT_PLUGIN_NIDMM_MODEL=4081

MEASUREMENT_PLUGIN_NIFGEN_SIMULATE=1
MEASUREMENT_PLUGIN_NIFGEN_BOARD_TYPE=PXIe
MEASUREMENT_PLUGIN_NIFGEN_MODEL=5423 (2CH)

MEASUREMENT_PLUGIN_NISCOPE_SIMULATE=1
MEASUREMENT_PLUGIN_NISCOPE_BOARD_TYPE=PXIe
MEASUREMENT_PLUGIN_NISCOPE_MODEL=5162 (4CH)

MEASUREMENT_PLUGIN_NISWITCH_SIMULATE=1
MEASUREMENT_PLUGIN_NISWITCH_TOPOLOGY=2567/Independent

MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE=1
MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY=2529/2-Wire Dual 4x16 Matrix

MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE=1
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/game_of_life/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/game_of_life/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/game_of_life.measproj sha256=7d6e313a645280616fe5c8cede06eeb90e8d207587c4cd025ac0a05c9376ba5d bytes=3318 -->
## FILE: examples/game_of_life/game_of_life.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/game_of_life.measproj`
- sha256: `7d6e313a645280616fe5c8cede06eeb90e8d207587c4cd025ac0a05c9376ba5d`
- bytes: 3318

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="121A60F5866041B0BCAD49CA464A46A94C010DD923808FE10A01EDFAAE04919B162194A3EC229557E353B4943C3CDAD0B8D17A214DD517C7DC38AE720410E54D" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.8.0.1666" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1665" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1665" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1665" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1665" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.8.0.1667" Name="MeasurementLink UI Editor" Version="23.8.0.1667" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="6a601cfa53834724b3e46aa0445e25a0" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="3f1bd45184744d6595d6d7b008662efc" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="a7e9c36db3194f71869079e48ac6397e" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="7d137e4ffec6485693839b2b92093077" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="game_of_life.measui" StoragePath="game_of_life.measui" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="4f988f0de5304ec89c060e4b1bb24c1e" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="1b44a28c6bd14460a4cd8f96fbc881f4" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="c26d5ae187024520902f924055095319" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="c5afb693e3ea4e05ad880909ab8ab03c" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="8459c7bd003c4500813344612c88dc09" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="826605ecacd64c828db547987a07ba33" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3c34fd9154f449229b87d6010d59a8ac" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/game_of_life.measui sha256=4bfff4694ddae49013ec4d762c1868c91bf8b9ae8a453432214f2f072eec4565 bytes=16004 -->
## FILE: examples/game_of_life/game_of_life.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/game_of_life.measui`
- sha256: `4bfff4694ddae49013ec4d762c1868c91bf8b9ae8a453432214f2f072eec4565`
- bytes: 16004

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FB00DE5760DC4C8BCA404570F539CB0045732580AB19CFD375457EAE5FD2BFFBD6504BD8E888CFA0CDD4F96C18746E292668574BBCDE0DED2C1CA9014155E2A4" Timestamp="1DB006D00129863" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.14.0.2316" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2316" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.8.0.2316" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="24.8.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2316" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2316" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.8.0.2316" Name="Measurement Plug-in UI Editor" Version="24.8.0.2316" />
	</SourceModelFeatureSet>
	<Screen DisplayName="Conway's Game of Life (Py)" Id="96739123b04f4da5aab63f7b09eb6655" ServiceClass="ni.examples.GameOfLife_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]665" Id="3fd569328bb14d969962e036a6890b5d" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]798" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]526" Id="a195c6ada9394c68b3f01238d59258e0" Label="[UIModel]43398146ddc04e6ca07ee780372f6507" Left="[float]132" MinWidth="[float]230" PlotAreaMargin="[SMThickness]41,26,20,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]30" Width="[float]649">
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="47588ac02a284a3eb9b22b58b332203f" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]66435bc7d0bc45ae828e2455ee232fea" MajorGridLines="[UIModel]7332ced07b1149fd9f0cd156f241e534" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]-1, 101, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="66435bc7d0bc45ae828e2455ee232fea" LabelVisibility="[SMVisibility]Visible" Mode="[RangeDivisionsMode]Auto" TickVisibility="[SMVisibility]Visible" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
					<GridLines Color="[SMColor]#00ffffff" Id="7332ced07b1149fd9f0cd156f241e534" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ArrayGraphAxis>
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="3723e2d0c993443693f33dfe4056930b" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]1f76a5849b9449bbb1b15f9f6909af8c" Orientation="[SMOrientation]Vertical" Range="[IRange]-1, 101, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="1f76a5849b9449bbb1b15f9f6909af8c" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
				</ArrayGraphAxis>
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="a99a87f009d74d6db6c5b80fc233465f" PointFill="[SMSolidColorBrush]#ff962428" PointShape="[PointShape]Ellipse" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="5e5a5f718e5b4e86a8a0c4601166b6dc" PointFill="[SMSolidColorBrush]#ff008ee4" PointShape="[PointShape]Rectangle" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="cd3389803bf04358b1d3082814be6177" PointFill="[SMSolidColorBrush]#ffe2b683" PointShape="[PointShape]Diamond" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="a2cd32c393a24c3b91fa0fb0a29bf806" PointFill="[SMSolidColorBrush]#ffb7ac1f" PointShape="[PointShape]Cross" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="4ef8e57be1bf45e5ba485426c4b46fb3" PointFill="[SMSolidColorBrush]#ffaedcef" PointShape="[PointShape]Ellipse" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="a8ab81312dc44ba79aaa6f0bd4638311" PointFill="[SMSolidColorBrush]#ffa08bb0" PointShape="[PointShape]Rectangle" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="8e6d2058f5264da782653ac2e504d779" PointFill="[SMSolidColorBrush]#ff7f7f7f" PointShape="[PointShape]Diamond" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="31cae3c70d5a44bda76a92809b0df15c" PointFill="[SMSolidColorBrush]#ff91685c" PointShape="[PointShape]Cross" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<HmiGraphPlot Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Output/game_of_life" HorizontalScale="[UIModel]47588ac02a284a3eb9b22b58b332203f" Id="d8135274d68e4040ba9e73dafcd964bc" IsDefaultPlot="[bool]False" Label="[string]game_of_life" VerticalScale="[UIModel]3723e2d0c993443693f33dfe4056930b">
					<PlotRenderer Id="9b18f852f145411e9d6a8310e5de68e1" LineThickness="[double]1" PointFill="[SMSolidColorBrush]#ff865ea8" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
			</ArrayGraph>
			<HmiChartPlotLegend Graph="[UIModel]a195c6ada9394c68b3f01238d59258e0" Height="[float]28" Id="be4c8c11f02142d99cedc899cf7161d8" Left="[float]788" LegendHeightFollowsGraph="[bool]False" Top="[float]48" Visible="[bool]False" />
			<HmiChartCursorLegend Graph="[UIModel]a195c6ada9394c68b3f01238d59258e0" Height="[float]80" Id="c3f85f09183b4fb18779f63278f331eb" Left="[float]137" MinHeight="[float]80" Top="[float]585" Visible="[bool]False" Width="[float]316" />
			<HmiChartScaleLegend Graph="[UIModel]a195c6ada9394c68b3f01238d59258e0" Height="[float]52" Id="4767b1b23ed14aafa34af2b397b768d0" Left="[float]706" Top="[float]563" Visible="[bool]False" />
			<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]a195c6ada9394c68b3f01238d59258e0" Height="[float]26" Id="eb446917a8b3480f91844fd1a7dc6abc" Left="[float]627" OffsetX="[float]495" OffsetY="[float]0" Top="[float]30" Width="[float]122">
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]356dfc69f6514fe38b1f721a5ae98ceb" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="f274616f95184e83ab4fc0d55228ba21" IsMomentary="[bool]False" Label="[UIModel]326667befaa543b5aa47269ba168e350" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="356dfc69f6514fe38b1f721a5ae98ceb" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]375b4ee60bbd45c3b4aa8d7cd7cbd441" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="41253e7c6af442128b5657e303549860" IsMomentary="[bool]False" Label="[UIModel]61ec7df9787a478396e904b73fe096c6" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="375b4ee60bbd45c3b4aa8d7cd7cbd441" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]737b9a6385cd45b1aee3e9f7437dc8e8" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="f265861e11c346158079138df240ef2b" IsMomentary="[bool]False" Label="[UIModel]fe346c4eecce4eb798f48d81a2cfedf6" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="737b9a6385cd45b1aee3e9f7437dc8e8" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]a0ef30f8a70b4aca8982973d5ff4ab3b" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="a41e5c3a0f7c4bc591a110d77463aca1" IsMomentary="[bool]True" Label="[UIModel]9e117b3eaf5c4d4292930d1d0b46f7b0" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="a0ef30f8a70b4aca8982973d5ff4ab3b" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<Label Id="326667befaa543b5aa47269ba168e350" LabelOwner="[UIModel]f274616f95184e83ab4fc0d55228ba21" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="61ec7df9787a478396e904b73fe096c6" LabelOwner="[UIModel]41253e7c6af442128b5657e303549860" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="fe346c4eecce4eb798f48d81a2cfedf6" LabelOwner="[UIModel]f265861e11c346158079138df240ef2b" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="9e117b3eaf5c4d4292930d1d0b46f7b0" LabelOwner="[UIModel]a41e5c3a0f7c4bc591a110d77463aca1" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
			</ArrayGraphTools>
			<Label Height="[float]0" Id="43398146ddc04e6ca07ee780372f6507" LabelOwner="[UIModel]a195c6ada9394c68b3f01238d59258e0" Left="[float]132" Text="[string]Game Of Life" Top="[float]10" Visible="[bool]False" Width="[float]0" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Configuration/width" Enabled="[bool]True" Height="[float]24" Id="344f9801219140729f4d1f35dfabe173" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]dff64149668d4c6cbf2b82b658961071" Left="[float]26" TabIndex="[int]0" Top="[float]45" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
			<Label Height="[float]16" Id="dff64149668d4c6cbf2b82b658961071" LabelOwner="[UIModel]344f9801219140729f4d1f35dfabe173" Left="[float]26" Text="[string]Board width" Top="[float]25" Width="[float]64" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Configuration/height" Enabled="[bool]True" Height="[float]24" Id="c12cc470211945d4a472f7cce056e9a5" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]a334b80dc834cd8b2a95d4d98c8b3de" Left="[float]26" TabIndex="[int]1" Top="[float]125" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
			<Label Height="[float]16" Id="a334b80dc834cd8b2a95d4d98c8b3de" LabelOwner="[UIModel]c12cc470211945d4a472f7cce056e9a5" Left="[float]26" Text="[string]Board height" Top="[float]105" Width="[float]70" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Output/generation" Height="[float]24" Id="4a187afaf81c47988b80730a9548b9e0" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]7a7ff144ff3f42d793d356c838475d25" Left="[float]26" TabIndex="[int]2" Top="[float]365" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
			<Label Height="[float]16" Id="7a7ff144ff3f42d793d356c838475d25" LabelOwner="[UIModel]4a187afaf81c47988b80730a9548b9e0" Left="[float]26" Text="[string]Generation" Top="[float]345" Width="[float]59" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Configuration/update_interval_msec" Enabled="[bool]True" Height="[float]24" Id="be0c33f0b3564f8ab236406ed28f13e6" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]46d4ea54705544d29860eef507add0c7" Left="[float]26" TabIndex="[int]3" Top="[float]205" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
			<Label Height="[float]16" Id="46d4ea54705544d29860eef507add0c7" LabelOwner="[UIModel]be0c33f0b3564f8ab236406ed28f13e6" Left="[float]26" Text="[string]Update interval (ms)" Top="[float]185" Width="[float]108" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{0c4443be-04e8-4557-902d-9d6c2cc5ae36}/Configuration/max_generations" Enabled="[bool]True" Height="[float]24" Id="868c277df4bf43f786a929cc24354224" Interval="[int]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9669d738649e4e02914cbc21c49b4aa8" Left="[float]26" TabIndex="[int]4" Top="[float]285" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]70" />
			<Label Height="[float]16" Id="9669d738649e4e02914cbc21c49b4aa8" LabelOwner="[UIModel]868c277df4bf43f786a929cc24354224" Left="[float]26" Text="[string]Max generations" Top="[float]265" Width="[float]88" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/game_of_life.serviceconfig sha256=a18fab69362e3ea6d7635328e05becf3a32a14505dd49ae94eb050f2e8681fd2 bytes=614 -->
## FILE: examples/game_of_life/game_of_life.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/game_of_life.serviceconfig`
- sha256: `a18fab69362e3ea6d7635328e05becf3a32a14505dd49ae94eb050f2e8681fd2`
- bytes: 614

````json
{
  "services": [
    {
      "displayName": "Conway's Game of Life (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.GameOfLife_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that displays Conway's Game of Life simulation in a graph.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/GameOfLife.instudioproj sha256=d6753b4a9a98d8fe492ec294b3a64bdc17c7a3ee225cbe1634fa671abc121479 bytes=1706 -->
## FILE: examples/game_of_life/GameOfLife.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/GameOfLife.instudioproj`
- sha256: `d6753b4a9a98d8fe492ec294b3a64bdc17c7a3ee225cbe1634fa671abc121479`
- bytes: 1706

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="6B4C9DB5386095A6B18DBAA320B85A65E020F855F07CBCF658C9084BDA2B1E9D8888795A38791F923DF21D64C847AEE10CA4F34284452183B3DB73A2E8378A30" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.14.0.2657" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.8.0.2657" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.8.0.2657" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="ec69f4193c6b47178af959e7fb3313d8" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="9e77bddbbea74f6ba6b629bf8f91824f" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="6e16cde12ef3477184f2e01b29d7c9ca" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Bindings="EnvoyManager" Id="3ddcebe30d614851942b0b92040acd2b" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="GameOfLife.sfp" StoragePath="GameOfLife.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework">
		<p.ProjectProperties>
			<Kind Name="plugin.reference">
				<Item Name="ni.examples.GameOfLife_Python" Value="1.0.0" />
			</Kind>
		</p.ProjectProperties>
	</ProjectInformation>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/GameOfLife.sfp sha256=fb4ee75e3d7834098553a51b5400917ffa79dd255fd41e867653db9fca44c1e2 bytes=19104 -->
## FILE: examples/game_of_life/GameOfLife.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/GameOfLife.sfp`
- sha256: `fb4ee75e3d7834098553a51b5400917ffa79dd255fd41e867653db9fca44c1e2`
- bytes: 19104

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="9D9114CDA11543D64AAC4CCC1C944FA8A1D00DC4A0D24B4DE41AAE7E19EC9590B95924DDF547556AE56E949F60329A5A33E0A3366079AF0B1C06AE9AA6AC7A1B" Timestamp="1DB0DF6BBA4BC9D" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.14.0.2657" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2657" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.8.0.2657" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="24.8.0.2657" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="24.8.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2657" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.2657" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.8.0.2657" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.8.0.2657" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="424e64524a0a4944a4c591fe955755be" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:24.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:2,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:1,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task&quot;,&quot;Container Instrument Name&quot;:&quot;Conway's Game of Life (Py)&quot;,&quot;Layout Information Name&quot;:&quot;Conway's Game of Life (Py) 1&quot;,&quot;Layout Information Index&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;NI.Examples&quot;,&quot;Panel Type&quot;:&quot;Conway's Game of Life (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.GameOfLife_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="dae35744891e4b7cba1bc63887a52321" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f4b9e9477db1468b9d43e4a3b018f6f2" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="1b469867c381444c8d15f5c03a4e8103" Name="GameOfLife.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="77d6b903dcf044bc8d7a7f71b1ef3cd7" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task">
			<Screen ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v2.MeasurementConfigurations&quot;,&quot;width&quot;:100,&quot;height&quot;:100,&quot;updateIntervalMsec&quot;:100,&quot;maxGenerations&quot;:-1}" DisplayName="Conway's Game of Life (Py)" Id="15564f129d174c3ea3526b4e9e49b3cd" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.GameOfLife_Python" Version="1.0.0" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]665" Id="d577297bb9d24c1fb669adac149a4475" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]798" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]526" Id="e20234a9b78d4a26a5c8ad3f3700eefe" Label="[UIModel]b69a927788ac48c3b01c479a2687e722" Left="[float]132" MinWidth="[float]230" PlotAreaMargin="[SMThickness]41,26,20,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]30" Width="[float]649">
						<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="b68afd6f35944e1ebbea5b91fc088e55" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]4109b37e04734c6288841e4975f07310" MajorGridLines="[UIModel]1dd55106f7b64eb7a70261f3e9c7742f" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]-1, 101, System.Double" ValueType="[Type]Double">
							<RangeLabeledDivisions Id="4109b37e04734c6288841e4975f07310" LabelVisibility="[SMVisibility]Visible" Mode="[RangeDivisionsMode]Auto" TickVisibility="[SMVisibility]Visible" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
								<p.LabelPresenter Format="G6" />
							</RangeLabeledDivisions>
							<GridLines Color="[SMColor]#00ffffff" Id="1dd55106f7b64eb7a70261f3e9c7742f" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ArrayGraphAxis>
						<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="d460c1b15a14055ae04e021c0bb03d1" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]8b99e47fe6eb438a89486d5d79cc9822" Orientation="[SMOrientation]Vertical" Range="[IRange]-1, 101, System.Double" ValueType="[Type]Double">
							<RangeLabeledDivisions Id="8b99e47fe6eb438a89486d5d79cc9822" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
								<p.LabelPresenter Format="G6" />
							</RangeLabeledDivisions>
						</ArrayGraphAxis>
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="72009ba8e6b546cb944ea30cf338ad75" PointFill="[SMSolidColorBrush]#ff962428" PointShape="[PointShape]Ellipse" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="4257058e707478b8af44aaf496bba8e" PointFill="[SMSolidColorBrush]#ff008ee4" PointShape="[PointShape]Rectangle" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="8f77c2630f174378b23bd7e1b074a140" PointFill="[SMSolidColorBrush]#ffe2b683" PointShape="[PointShape]Diamond" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="fc6b4c957a27446c9c90d83a8b4f2c61" PointFill="[SMSolidColorBrush]#ffb7ac1f" PointShape="[PointShape]Cross" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="7a95f17cc08f4c1ea730c18b5728b538" PointFill="[SMSolidColorBrush]#ffaedcef" PointShape="[PointShape]Ellipse" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="bb15bb01bf7143d48b1e6bec0400238a" PointFill="[SMSolidColorBrush]#ffa08bb0" PointShape="[PointShape]Rectangle" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="2b7e7cc7934348c8be843140452bbfef" PointFill="[SMSolidColorBrush]#ff7f7f7f" PointShape="[PointShape]Diamond" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<PlotRenderer AreaBaseline="[FillBaseline]Zero" BarBaseline="[FillBaseline]Zero" Id="b3af970b987244759a307c6a7666ba4f" PointFill="[SMSolidColorBrush]#ff91685c" PointShape="[PointShape]Cross" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						<HmiGraphPlot Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Output/game_of_life" HorizontalScale="[UIModel]b68afd6f35944e1ebbea5b91fc088e55" Id="5c9335e419714662ba3bdcd978be0214" IsDefaultPlot="[bool]False" Label="[string]game_of_life" VerticalScale="[UIModel]d460c1b15a14055ae04e021c0bb03d1">
							<PlotRenderer Id="83c7b1305e884c978d22ab27ad34eda0" LineThickness="[double]1" PointFill="[SMSolidColorBrush]#ff865ea8" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</HmiGraphPlot>
					</ArrayGraph>
					<HmiChartPlotLegend Graph="[UIModel]e20234a9b78d4a26a5c8ad3f3700eefe" Height="[float]28" Id="87f8808798a74425b696ecf96fbcbc34" Left="[float]788" LegendHeightFollowsGraph="[bool]False" Top="[float]48" Visible="[bool]False" />
					<HmiChartCursorLegend Graph="[UIModel]e20234a9b78d4a26a5c8ad3f3700eefe" Height="[float]80" Id="e81b72bca16042939aef07b864203206" Left="[float]137" MinHeight="[float]80" Top="[float]585" Visible="[bool]False" Width="[float]316" />
					<HmiChartScaleLegend Graph="[UIModel]e20234a9b78d4a26a5c8ad3f3700eefe" Height="[float]52" Id="4373e0cf46b74d73826b1775016ada6a" Left="[float]706" Top="[float]563" Visible="[bool]False" />
					<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]e20234a9b78d4a26a5c8ad3f3700eefe" Height="[float]26" Id="b3bbddba65e44aa6b63329ade8943b30" Left="[float]627" OffsetX="[float]495" OffsetY="[float]0" Top="[float]30" Width="[float]122">
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]f6238242e37e4daf9c486fb22bbdaf78" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="6f8fb54913b64a6f9ad80f6b61effae6" IsMomentary="[bool]False" Label="[UIModel]5ae72ca85969444cb9afddc3a5cfecd7" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="f6238242e37e4daf9c486fb22bbdaf78" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]5c2bf3d5430547cab05df50a3d53ed9a" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="e53fcedf522f402283e2c86b9b94ab5f" IsMomentary="[bool]False" Label="[UIModel]d24db174259140dc8e55200edee158cb" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="5c2bf3d5430547cab05df50a3d53ed9a" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]b04098969e91436a87e13da62e05ec70" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="a68a472609b64f33b9ad833de46b60ad" IsMomentary="[bool]False" Label="[UIModel]bd670b5afd3e4eb194724877fbf3f33d" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="b04098969e91436a87e13da62e05ec70" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]6dc0019bb9f34cad924163c13d6eb45e" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="a2fba0fa8b894e4da4a9f07f38a424de" IsMomentary="[bool]True" Label="[UIModel]ffb951aca4244e4facc517f388aee1a2" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="6dc0019bb9f34cad924163c13d6eb45e" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<Label Id="5ae72ca85969444cb9afddc3a5cfecd7" LabelOwner="[UIModel]6f8fb54913b64a6f9ad80f6b61effae6" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="d24db174259140dc8e55200edee158cb" LabelOwner="[UIModel]e53fcedf522f402283e2c86b9b94ab5f" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="bd670b5afd3e4eb194724877fbf3f33d" LabelOwner="[UIModel]a68a472609b64f33b9ad833de46b60ad" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="ffb951aca4244e4facc517f388aee1a2" LabelOwner="[UIModel]a2fba0fa8b894e4da4a9f07f38a424de" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
					</ArrayGraphTools>
					<Label Height="[float]0" Id="b69a927788ac48c3b01c479a2687e722" LabelOwner="[UIModel]e20234a9b78d4a26a5c8ad3f3700eefe" Left="[float]132" Text="[string]Game Of Life" Top="[float]10" Visible="[bool]False" Width="[float]0" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Configuration/width" Enabled="[bool]True" Height="[float]24" Id="11ae9258aff345c4af473d32f5b2e7c6" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]be762bb1605e4341b5810c724a6eb65c" Left="[float]26" TabIndex="[int]0" Top="[float]45" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
					<Label Height="[float]16" Id="be762bb1605e4341b5810c724a6eb65c" LabelOwner="[UIModel]11ae9258aff345c4af473d32f5b2e7c6" Left="[float]26" Text="[string]Board width" Top="[float]25" Width="[float]64" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Configuration/height" Enabled="[bool]True" Height="[float]24" Id="99104e924a5c4d0d923c56da60c3c2e8" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d6462d2a047b49f0b28bac56b38fbe75" Left="[float]26" TabIndex="[int]1" Top="[float]125" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
					<Label Height="[float]16" Id="d6462d2a047b49f0b28bac56b38fbe75" LabelOwner="[UIModel]99104e924a5c4d0d923c56da60c3c2e8" Left="[float]26" Text="[string]Board height" Top="[float]105" Width="[float]70" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Output/generation" Height="[float]24" Id="61cc420094eb43e5b7b8ec366461ba9d" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]e1a91dd8c0c42eba51e5a21bc8a8ab6" Left="[float]26" TabIndex="[int]2" Top="[float]365" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
					<Label Height="[float]16" Id="e1a91dd8c0c42eba51e5a21bc8a8ab6" LabelOwner="[UIModel]61cc420094eb43e5b7b8ec366461ba9d" Left="[float]26" Text="[string]Generation" Top="[float]345" Width="[float]59" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Configuration/update_interval_msec" Enabled="[bool]True" Height="[float]24" Id="e52b1d821f9042179a4b289bca30054b" Interval="[uint]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e7490bda1dec46e9b6287c0a65908c81" Left="[float]26" TabIndex="[int]3" Top="[float]205" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt32" Width="[float]70" />
					<Label Height="[float]16" Id="e7490bda1dec46e9b6287c0a65908c81" LabelOwner="[UIModel]e52b1d821f9042179a4b289bca30054b" Left="[float]26" Text="[string]Update interval (ms)" Top="[float]185" Width="[float]108" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{274cd5d0-99fb-432b-b70b-e959c7517998}/Configuration/max_generations" Enabled="[bool]True" Height="[float]24" Id="e3a89ad119594e8e8d811ea92853fb2a" Interval="[int]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]66e168426af4f43bfd03789dd3cd5d5" Left="[float]26" TabIndex="[int]4" Top="[float]285" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]70" />
					<Label Height="[float]16" Id="66e168426af4f43bfd03789dd3cd5d5" LabelOwner="[UIModel]e3a89ad119594e8e8d811ea92853fb2a" Left="[float]26" Text="[string]Max generations" Top="[float]265" Width="[float]88" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/game_of_life/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/measurement.py sha256=405ab3edaa67c7c2dd789a11e4b1d12fef6952ba84e6015e7567ed44f61baa1f bytes=4594 -->
## FILE: examples/game_of_life/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/measurement.py`
- sha256: `405ab3edaa67c7c2dd789a11e4b1d12fef6952ba84e6015e7567ed44f61baa1f`
- bytes: 4594

````python
"""Source the XY data for Conway's Game of Life."""

import pathlib
import random
import threading
import time
from collections.abc import Generator
from typing import Any

import click
import grpc
import ni_measurement_plugin_sdk_service as nims
from _helpers import configure_logging, verbosity_option
from ni.protobuf.types import xydata_pb2


service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "game_of_life.serviceconfig",
    ui_file_paths=[service_directory / "game_of_life.measui"],
)

Grid = list[list[bool]]

INFINITE_GENERATIONS = -1


@measurement_service.register_measurement
@measurement_service.configuration("width", nims.DataType.UInt32, 100)
@measurement_service.configuration("height", nims.DataType.UInt32, 100)
@measurement_service.configuration("update_interval_msec", nims.DataType.UInt32, 100)
@measurement_service.configuration("max_generations", nims.DataType.Int32, INFINITE_GENERATIONS)
@measurement_service.output("game_of_life", nims.DataType.DoubleXYData)
@measurement_service.output("generation", nims.DataType.UInt32)
def measure(
    width: int, height: int, update_interval_msec: int, max_generations: int
) -> Generator[tuple[xydata_pb2.DoubleXYData, int], None, None]:
    """Streaming measurement that returns Conway's Game of Life grid as DoubleXYData."""
    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)
    grid = _initialize_grid_with_seeded_data(width, height)
    update_interval_sec = update_interval_msec / 1000
    generation = 0
    while max_generations == INFINITE_GENERATIONS or generation < max_generations:
        iteration_start_time = time.monotonic()
        generation += 1

        xydata = _initialize_xydata_and_frame(width, height)
        row_index = 0
        for row in grid:
            col_index = 0
            for cell in row:
                if cell:
                    xydata.x_data.append(row_index)
                    xydata.y_data.append(col_index)
                col_index += 1
            row_index += 1
        grid = _update_grid(grid)
        xydata_out = xydata
        delay = max(0.0, update_interval_sec - (time.monotonic() - iteration_start_time))
        yield (xydata_out, generation)

        if cancellation_event.wait(delay):
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )


def _initialize_xydata_and_frame(width: int, height: int) -> xydata_pb2.DoubleXYData:
    xydata = xydata_pb2.DoubleXYData()

    # Frame To keep the graph stable
    xydata.x_data.append(-1)
    xydata.y_data.append(-1)
    xydata.x_data.append(-1)
    xydata.y_data.append(height + 1)
    xydata.x_data.append(width + 1)
    xydata.y_data.append(-1)
    xydata.x_data.append(width + 1)
    xydata.y_data.append(height + 1)
    return xydata


def _initialize_grid_with_seeded_data(rows: int, cols: int, probability: float = 0.6) -> Grid:
    return [[random.random() < probability for _ in range(cols)] for _ in range(rows)]


def _initialize_grid(rows: int, cols: int) -> Grid:
    return [[False for _ in range(cols)] for _ in range(rows)]


def _count_neighbors(grid: Grid, row: int, col: int) -> int:
    count = 0
    neighbors = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]
    for r, c in neighbors:
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
            count += 1
    return count


def _update_grid(grid: Grid) -> Grid:
    new_grid = _initialize_grid(len(grid), len(grid[0]))
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbors = _count_neighbors(grid, row, col)
            if grid[row][col]:
                new_grid[row][col] = neighbors == 2 or neighbors == 3
            else:
                new_grid[row][col] = neighbors == 3
    return new_grid


@click.command
@verbosity_option
def main(verbosity: int, **kwargs: Any) -> None:
    """Source the XY data for Conway's Game of Life."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/game_of_life/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/pyproject.toml sha256=d8ddc1c82dc54be0f36e8f60cda4e8a67ae1b346b6cddbdb75542c71f7e9f11c bytes=915 -->
## FILE: examples/game_of_life/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/pyproject.toml`
- sha256: `d8ddc1c82dc54be0f36e8f60cda4e8a67ae1b346b6cddbdb75542c71f7e9f11c`
- bytes: 915

````toml
[tool.poetry]
name = "game_of_life"
version = "1.0.0"
package-mode = false
description = "Measurement plug-in example that displays Conway's Game of Life in a graph."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
ni-protobuf-types = { version = ">=0.1.0dev2", allow-prereleases = true }

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
types-protobuf = ">=4.21"
# Uncomment to use prerelease dependencies.
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[tool.mypy]
disallow_untyped_defs = true

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/README.md sha256=cdd6e9d0c6ac0734f9b85a32cc2acc520795867c9825d23807f545f22e8d9b16 bytes=531 -->
## FILE: examples/game_of_life/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/README.md`
- sha256: `cdd6e9d0c6ac0734f9b85a32cc2acc520795867c9825d23807f545f22e8d9b16`
- bytes: 531

````markdown
## Game of Life

This is a measurement plug-in example that displays Conway's Game of Life
in a graph.

### Features

- Demonstrates a measurement service returning XY data.
- Demonstrates how to update a measurement UI while the measurement is
  running.
- Demonstrates cancellation tokens and deadlines.
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files.

### Required Software

- InstrumentStudio 2025 Q1 or later

### Required Hardware

This example does not require any hardware.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/game_of_life/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/game_of_life/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/game_of_life/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nidaqmx_analog_input/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nidaqmx_analog_input/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nidaqmx_analog_input/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/measurement.py sha256=797d6c5fd11a6fad02c416ae4bee253c961b52e4e7d7aa25fbb7dc987d3a4bbb bytes=3477 -->
## FILE: examples/nidaqmx_analog_input/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/measurement.py`
- sha256: `797d6c5fd11a6fad02c416ae4bee253c961b52e4e7d7aa25fbb7dc987d3a4bbb`
- bytes: 3477

````python
"""Perform a finite analog input measurement with NI-DAQmx."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims
from _helpers import (
    configure_logging,
    verbosity_option,
)
from nidaqmx.constants import TaskMode

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDAQmxAnalogInput.serviceconfig",
    ui_file_paths=[service_directory / "NIDAQmxAnalogInput.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_name",
    nims.DataType.IOResource,
    "Pin1",
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DAQMX,
)
@measurement_service.configuration("sample_rate", nims.DataType.Double, 1000.0)
@measurement_service.configuration("number_of_samples", nims.DataType.UInt64, 100)
@measurement_service.output("acquired_samples", nims.DataType.DoubleArray1D)
def measure(pin_name: str, sample_rate: float, number_of_samples: int) -> tuple[list[float]]:
    """Perform a finite analog input measurement with NI-DAQmx."""
    logging.info(
        "Executing measurement: pin_name=%s sample_rate=%g number_of_samples=%d",
        pin_name,
        sample_rate,
        number_of_samples,
    )
    with measurement_service.context.reserve_session(pin_name) as reservation:
        with reservation.create_nidaqmx_task() as session_info:
            task = session_info.session

            def cancel_callback() -> None:
                logging.info("Canceling measurement")
                if (task_to_abort := task) is not None:
                    task_to_abort.control(TaskMode.TASK_ABORT)

            measurement_service.context.add_cancel_callback(cancel_callback)

            # If we created a new DAQmx task, we must also add channels to it.
            if not session_info.session_exists:
                task.ai_channels.add_ai_voltage_chan(session_info.channel_list)

            task.timing.cfg_samp_clk_timing(
                rate=sample_rate,
                samps_per_chan=number_of_samples,
            )

            timeout = min(measurement_service.context.time_remaining, 10.0)
            voltage_values = task.read(number_of_samples, timeout)
            task = None  # Don't abort after this point

    _log_measured_values(voltage_values)
    logging.info("Completed measurement")
    return (voltage_values,)


def _log_measured_values(samples: list[float], max_samples_to_display: int = 5) -> None:
    """Log the measured values."""
    if len(samples) > max_samples_to_display:
        for index, value in enumerate(samples[0 : max_samples_to_display - 1]):
            logging.info("Sample %d: %f", index, value)
        logging.info("...")
        logging.info("Sample %d: %f", len(samples) - 1, samples[-1])
    else:
        for index, value in enumerate(samples):
            logging.info("Sample %d: %f", index, value)


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Perform a finite analog input measurement with NI-DAQmx."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.instudioproj sha256=881de62882a25bd6831c474a6d857b5f91966a5476f4d7cf3fdb62d9a9e2e872 bytes=2019 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.instudioproj`
- sha256: `881de62882a25bd6831c474a6d857b5f91966a5476f4d7cf3fdb62d9a9e2e872`
- bytes: 2019

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="140C0262EC1163FCD9CB6684F353BC02F2EBBC884A64A3E78839A8199CAE13CA9B3C04867D54F63345403E67AE98BB9231E34F53626F4E6654A55503437E1BBA" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.3.0.1870" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.1870" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.1870" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.3.0.1870" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Bindings="EnvoyManager" Id="72ee6b30240d4ad08157c1165340d00c" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIDAQmxAnalogInput.sfp" StoragePath="NIDAQmxAnalogInput.sfp" />
			<FileReference Id="29a5487da33d41a58d7ef7592cdbd6cb" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDAQmxAnalogInput.pinmap" StoragePath="NIDAQmxAnalogInput.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measproj sha256=3602abd56335cf5d963d242ba85579ba2284604f393d09132fa547cf20be9d68 bytes=3816 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measproj`
- sha256: `3602abd56335cf5d963d242ba85579ba2284604f393d09132fa547cf20be9d68`
- bytes: 3816

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4EE13EA57A506B34E89F9EA3DCE855CB42DDD03CA2058542AE2717FB30542BF7520D95A91C8BE7CD82810ACD1674D945B55A9024D420E037A473F0E9BB40E359" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.50004" Name="MeasurementLink UI Editor" Version="23.3.0.50004" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="91bcda54ca2d44728e1fadacc394016e" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="996d011bd1934b02a8dfc6d5e5a89be5" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="2eeb856ee34444e1a4cab4208186ecf5" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="21c24b60a2fa4fc0a61b412c3484eaf2" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="75ef959f36344af79e96cdde6045ca5d" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="c93a3eb46b744106b712f9aafe556252" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="da85de41098b4fc5911a22d5ec540058" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="9ce0dfde6bd4970bac08304a67997de" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="2449b274942d4dd0960c503bd18f98b5" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="ab6e3c571b8f4b21abeb510e0bda6520" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="2c80fa9b822147cca4d37064ae04c0eb" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIDAQmxAnalogInput.measui" StoragePath="NIDAQmxAnalogInput.measui" />
			<FileReference Id="de4787bd282e42a5b4630318938fe41d" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDAQmxAnalogInput.pinmap" StoragePath="NIDAQmxAnalogInput.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measui sha256=7e6c972d58575ba5be1c9e114fbc70c6a96fdf706d558ddeabb89ff36b68df8e bytes=12744 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.measui`
- sha256: `7e6c972d58575ba5be1c9e114fbc70c6a96fdf706d558ddeabb89ff36b68df8e`
- bytes: 12744

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="F43E3539B81294B67EE75F729C06594ACB55053241EAE754A8E5363B57ECC60944FC5E3493CED4ADCDE8A2B42371A215DFF104A9E540338FDB8CFC25FFD7D57F" Timestamp="1D982601841E111" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.50004" Name="MeasurementLink UI Editor" Version="23.3.0.50004" />
	</SourceModelFeatureSet>
	<Screen ClientId="{5f88d1ec-4b12-4bf9-b28f-707b534a0575}" DisplayName="NI-DAQmx Analog Input (Py)" Id="ce8cc70d4b0b487db029384b996c0e8a" ServiceClass="ni.examples.NIDAQmxAnalogInput_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]676" Id="1224789d85bd4cdfa59e83e724ab737e" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]1957" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]140" Id="60cc49b2dae7482a8f7cc701d9314d26" Label="[UIModel]a17050b1220f41568f979d8d35dc8161" Left="[float]40" Top="[float]122" Width="[float]157">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/sample_rate" Height="[float]24" Id="30e574a2d3c74504aa1739b486500f2d" IsLabelBoundToChannel="[bool]False" Label="[UIModel]72e900b49f9d428c8ad78b47fd1bea09" Left="[float]22" Top="[float]41" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="72e900b49f9d428c8ad78b47fd1bea09" LabelOwner="[UIModel]30e574a2d3c74504aa1739b486500f2d" Left="[float]22" Text="[string]Sample Rate (S/s)" Top="[float]21" Width="[float]93" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/number_of_samples" Height="[float]24" Id="7fd7ce5a9b894509b20c747513a043cc" Interval="[ulong]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3779544d50944588b32e1398eeedd486" Left="[float]22" RadixBase="[RadixBase]Decimal" RadixVisibility="[SMVisibility]Collapsed" Top="[float]98" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Decimal:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt64" Width="[float]70" />
				<Label Height="[float]16" Id="3779544d50944588b32e1398eeedd486" LabelOwner="[UIModel]7fd7ce5a9b894509b20c747513a043cc" Left="[float]22" Text="[string]Number of Samples" Top="[float]78" Width="[float]105" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="a17050b1220f41568f979d8d35dc8161" LabelOwner="[UIModel]60cc49b2dae7482a8f7cc701d9314d26" Left="[float]40" Text="[string]Measurement Configurations" Top="[float]102" Width="[float]156" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]257" Id="3507d01be4bc4a26abc81ac1e2385674" Label="[UIModel]82dfa849cb640f9bdcd4d7c1256e976" Left="[float]215" Top="[float]122" Width="[float]564">
				<ArrayGraph BaseName="[string]Array Graph" Height="[float]224" Id="1038f1f785834b068ae033f7220d5089" Label="[UIModel]e04632237a7740d49b79e7dde2cc6f37" Left="[float]14" MinWidth="[float]230" PlotAreaMargin="[SMThickness]28,26,7,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]27" Width="[float]535">
					<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="85e339f99854551aae9bd9a4557aefe" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]753fe08f076f484d85e26b768259f0cd" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 10, System.Double" ValueType="[Type]Double">
						<RangeLabeledDivisions Id="753fe08f076f484d85e26b768259f0cd" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
							<p.LabelPresenter Format="G6" />
						</RangeLabeledDivisions>
					</ArrayGraphAxis>
					<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="724c3bc0b0334daaa1fbcb45f277b91d" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]8d724132dfd7408e90e261ccabea7971" Orientation="[SMOrientation]Vertical" Range="[IRange]0, 10, System.Double" ValueType="[Type]Double">
						<RangeLabeledDivisions Id="8d724132dfd7408e90e261ccabea7971" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
							<p.LabelPresenter Format="G6" />
						</RangeLabeledDivisions>
					</ArrayGraphAxis>
					<HmiGraphPlot Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Output/acquired_samples" HorizontalScale="[UIModel]85e339f99854551aae9bd9a4557aefe" Id="3ec5076105648c1a667efa4f1db1770" IsDefaultPlot="[bool]False" Label="[string]acquired_samples" VerticalScale="[UIModel]724c3bc0b0334daaa1fbcb45f277b91d">
						<PlotRenderer Id="3051f7e3c25e4adca1976688a4e2cf04" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					</HmiGraphPlot>
				</ArrayGraph>
				<HmiChartPlotLegend Graph="[UIModel]1038f1f785834b068ae033f7220d5089" Height="[float]28" Id="de2eaaf02d064db498ad613ba983b860" Left="[float]556" Top="[float]27" Visible="[bool]False" />
				<HmiChartCursorLegend Graph="[UIModel]1038f1f785834b068ae033f7220d5089" Height="[float]80" Id="a251fbd52594ce3b5ef300e249b2a30" Left="[float]19" MinHeight="[float]80" Top="[float]280" Visible="[bool]False" Width="[float]316" />
				<HmiChartScaleLegend Graph="[UIModel]1038f1f785834b068ae033f7220d5089" Height="[float]52" Id="c46b164665404108a3d7bdf3c73fc0d1" Left="[float]474" Top="[float]258" Visible="[bool]False" />
				<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]1038f1f785834b068ae033f7220d5089" Height="[float]26" Id="3a2673ce615f482fb2b58fc7dd768b46" Left="[float]395" OffsetX="[float]381" OffsetY="[float]0" Top="[float]27" Width="[float]122">
					<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]6aa83d5b7c4f48ce8452fde7386e4493" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="44ae529d638046a486c34b13407fbafd" IsMomentary="[bool]False" Label="[UIModel]95e1ae5b4ee94b4981476dbf70bfc49c" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
						<Image BaseName="[string]Image" Id="6aa83d5b7c4f48ce8452fde7386e4493" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
					</ComposableButton>
					<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]6463d05ffe7c4c26933d379c09ed9bd0" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="3112fd0088fd4e3e9a73e3b23938bf47" IsMomentary="[bool]False" Label="[UIModel]96c7df4ccf024ecfa3a780e1c19b6d64" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
						<Image BaseName="[string]Image" Id="6463d05ffe7c4c26933d379c09ed9bd0" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
					</ComposableButton>
					<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]19ea4deef04143d1812ed44a4b13a825" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="79382fe82b494c85b2116d1f32378077" IsMomentary="[bool]False" Label="[UIModel]9002e938f4e740398bf91a6bd6fc24bb" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
						<Image BaseName="[string]Image" Id="19ea4deef04143d1812ed44a4b13a825" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
					</ComposableButton>
					<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]850a6eb30e6142efbf12a8e60dbb7d96" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="59258176c5304a90a11314d9644bb20b" IsMomentary="[bool]True" Label="[UIModel]29f18a563b0f4863b7882888c1e343b3" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
						<Image BaseName="[string]Image" Id="850a6eb30e6142efbf12a8e60dbb7d96" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
					</ComposableButton>
					<Label Id="95e1ae5b4ee94b4981476dbf70bfc49c" LabelOwner="[UIModel]44ae529d638046a486c34b13407fbafd" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
					<Label Id="96c7df4ccf024ecfa3a780e1c19b6d64" LabelOwner="[UIModel]3112fd0088fd4e3e9a73e3b23938bf47" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
					<Label Id="9002e938f4e740398bf91a6bd6fc24bb" LabelOwner="[UIModel]79382fe82b494c85b2116d1f32378077" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
					<Label Id="29f18a563b0f4863b7882888c1e343b3" LabelOwner="[UIModel]59258176c5304a90a11314d9644bb20b" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				</ArrayGraphTools>
				<Label Height="[float]16" Id="e04632237a7740d49b79e7dde2cc6f37" LabelOwner="[UIModel]1038f1f785834b068ae033f7220d5089" Left="[float]14" Text="[string]Acquired Samples (V)" Top="[float]7" Width="[float]113" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="82dfa849cb640f9bdcd4d7c1256e976" LabelOwner="[UIModel]3507d01be4bc4a26abc81ac1e2385674" Left="[float]215" Text="[string]Measurement Results" Top="[float]102" Width="[float]114" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/pin_name" DataType="[Type]String" Height="[float]24" Id="8a69e63f38ee4dd898776b94b73f1c3a" Label="[UIModel]e6f904f62ae646a08d361dabb989446f" Left="[float]40" Top="[float]46" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="e6f904f62ae646a08d361dabb989446f" LabelOwner="[UIModel]8a69e63f38ee4dd898776b94b73f1c3a" Left="[float]40" Text="[string]pin_name" Top="[float]26" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.pinmap sha256=266c5eab44e18126654a54f5bba498a6a6081952986ba198e515a789619cab38 bytes=652 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.pinmap`
- sha256: `266c5eab44e18126654a54f5bba498a6a6081952986ba198e515a789619cab38`
- bytes: 652

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.4">
	<Instruments>
		<NIDAQmxTask name="Dev1" taskType="AnalogInput" channelList="Dev1/ai0, Dev1/ai1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Relays></Relays>
	<RelayGroups></RelayGroups>
	<RelayConfigurations></RelayConfigurations>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="Dev1" channel="Dev1/ai0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.serviceconfig sha256=e76e193231f909f76a2838f2d145b2707b23b5644e429d71a6260a76da19273e bytes=691 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.serviceconfig`
- sha256: `e76e193231f909f76a2838f2d145b2707b23b5644e429d71a6260a76da19273e`
- bytes: 691

````json
{
  "services": [
    {
      "displayName": "NI-DAQmx Analog Input (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIDAQmxAnalogInput_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that performs a finite analog input measurement with NI-DAQmx.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput.sfp sha256=d3eb50c62bd768d9e898f96ea2f8e19eb4e5c508c41d968bbde051ea95ef1b1a bytes=15899 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput.sfp`
- sha256: `d3eb50c62bd768d9e898f96ea2f8e19eb4e5c508c41d968bbde051ea95ef1b1a`
- bytes: 15899

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="A62F907DE2CD793F1E9DDF98B1CB369955BFAEF92CD2D6BE958869B8861B6AEE946C79DA893F1019553A851669A210462BD1AB3BF34EE29460BC1890AA679485" Timestamp="1D9831E09D88778" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.1870" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.1870" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.1870" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.1870" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.1870" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.3.0.1870" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="d3ba16cf54654e3f8fd4dfe07a2fd06b" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-DAQmx Analog Input (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-DAQmx Analog Input (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-DAQmx Analog Input (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIDAQmxAnalogInput_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="56820b2903b4b46919a0363a00603a4" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="8d9b8198085f448a9bc78f823b8b321c" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="1abb22a9b09482cb56c23b8d09fbca9" Name="NIDAQmxAnalogInput.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="c6f194dd2f5142fab4ac7ff66812faca" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{e7e5202f-6a5e-4509-940a-f9ec4f0f693d}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;pinName&quot;:&quot;Pin1&quot;,&quot;sampleRate&quot;:1000.0,&quot;numberOfSamples&quot;:&quot;100&quot;}" DisplayName="NI-DAQmx Analog Input (Py)" Id="6a2b0bf22cc643208cb20358bccf2dc2" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIDAQmxAnalogInput_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]676" Id="18bbc126fd4c4bbfa514ba007224a1a5" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]1957" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]140" Id="a0a9ec613469419b8b22e054c14ea081" Label="[UIModel]6597244856194d43bf3b4a6e2d0deefa" Left="[float]40" Top="[float]122" Width="[float]157">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{e7e5202f-6a5e-4509-940a-f9ec4f0f693d}/Configuration/sample_rate" Enabled="[bool]True" Height="[float]24" Id="a666bcceb86f4a48b9b1f2f97bb074a7" IsLabelBoundToChannel="[bool]False" Label="[UIModel]f51ea0ebbb374064bd964a26dd12f411" Left="[float]22" Top="[float]41" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="f51ea0ebbb374064bd964a26dd12f411" LabelOwner="[UIModel]a666bcceb86f4a48b9b1f2f97bb074a7" Left="[float]22" Text="[string]Sample Rate (S/s)" Top="[float]21" Width="[float]93" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{e7e5202f-6a5e-4509-940a-f9ec4f0f693d}/Configuration/number_of_samples" Enabled="[bool]True" Height="[float]24" Id="4825c16529ee4da283652822b53f3a19" Interval="[ulong]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7da75e193c794b49810b2c1c9d27ad58" Left="[float]22" RadixBase="[RadixBase]Decimal" RadixVisibility="[SMVisibility]Collapsed" Top="[float]98" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Decimal:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]UInt64" Width="[float]70" />
						<Label Height="[float]16" Id="7da75e193c794b49810b2c1c9d27ad58" LabelOwner="[UIModel]4825c16529ee4da283652822b53f3a19" Left="[float]22" Text="[string]Number of Samples" Top="[float]78" Width="[float]105" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="6597244856194d43bf3b4a6e2d0deefa" LabelOwner="[UIModel]a0a9ec613469419b8b22e054c14ea081" Left="[float]40" Text="[string]Measurement Configurations" Top="[float]102" Width="[float]156" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]257" Id="c05c5ed32e6e4651be749e14d2915aa5" Label="[UIModel]c843cffbda5f44fab93f75ead1c033e7" Left="[float]215" Top="[float]122" Width="[float]564">
						<ArrayGraph BaseName="[string]Array Graph" Height="[float]224" Id="55832a03a09840c7bcc02e73ffc7c969" Label="[UIModel]45cb453d017b46fb9cd8ba884ab400b5" Left="[float]14" MinWidth="[float]230" PlotAreaMargin="[SMThickness]28,26,7,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]27" Width="[float]535">
							<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="d099f65198864d548064e251111a194e" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]18d2df10dc33455991eb975825530816" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 10, System.Double" ValueType="[Type]Double">
								<RangeLabeledDivisions Id="18d2df10dc33455991eb975825530816" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
									<p.LabelPresenter Format="G6" />
								</RangeLabeledDivisions>
							</ArrayGraphAxis>
							<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="1b0cbb2985b54fcab5151e167e79d04c" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]f4c64bc9857a4a298b49d25d511133d5" Orientation="[SMOrientation]Vertical" Range="[IRange]0, 10, System.Double" ValueType="[Type]Double">
								<RangeLabeledDivisions Id="f4c64bc9857a4a298b49d25d511133d5" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
									<p.LabelPresenter Format="G6" />
								</RangeLabeledDivisions>
							</ArrayGraphAxis>
							<HmiGraphPlot Channel="[string]{e7e5202f-6a5e-4509-940a-f9ec4f0f693d}/Output/acquired_samples" HorizontalScale="[UIModel]d099f65198864d548064e251111a194e" Id="d7d5cfa4f7a543c3bdcdb492954214e0" IsDefaultPlot="[bool]False" Label="[string]acquired_samples" VerticalScale="[UIModel]1b0cbb2985b54fcab5151e167e79d04c">
								<PlotRenderer Id="4d3fba49ed2d4722a438a4360a541c6f" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							</HmiGraphPlot>
						</ArrayGraph>
						<HmiChartPlotLegend Graph="[UIModel]55832a03a09840c7bcc02e73ffc7c969" Height="[float]28" Id="54a5a948f72a473b868f939b5d6ba659" Left="[float]556" Top="[float]27" Visible="[bool]False" />
						<HmiChartCursorLegend Graph="[UIModel]55832a03a09840c7bcc02e73ffc7c969" Height="[float]80" Id="fdd05f59ba074c65adc28c52b2178dc1" Left="[float]19" MinHeight="[float]80" Top="[float]280" Visible="[bool]False" Width="[float]316" />
						<HmiChartScaleLegend Graph="[UIModel]55832a03a09840c7bcc02e73ffc7c969" Height="[float]52" Id="dc93298dfcfb4ea88c72a244fec09a88" Left="[float]474" Top="[float]258" Visible="[bool]False" />
						<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]55832a03a09840c7bcc02e73ffc7c969" Height="[float]26" Id="314dfd715fb647938581a7fe547e2bb8" Left="[float]395" OffsetX="[float]381" OffsetY="[float]0" Top="[float]27" Width="[float]122">
							<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]c1c6048e6cd5485bbdf8a6533e68e846" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="e36593c7f66349c281e94883062769d3" IsMomentary="[bool]False" Label="[UIModel]a1e2db370a4347a1b7b4f7ec608bf49b" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
								<Image BaseName="[string]Image" Id="c1c6048e6cd5485bbdf8a6533e68e846" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
							</ComposableButton>
							<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]757a5f8e01324de5bd6188b0c5f9bc9f" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="d896a0d607a04392880cefa3e057f3d1" IsMomentary="[bool]False" Label="[UIModel]f1ed624ee93d4a0fa18ef9b0fd37c26b" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
								<Image BaseName="[string]Image" Id="757a5f8e01324de5bd6188b0c5f9bc9f" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
							</ComposableButton>
							<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]72ee2fb71b604337bb8b52aef33c6a7c" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="72e435fda6ef4ac7bfab54ad26bc5fbb" IsMomentary="[bool]False" Label="[UIModel]a05c22e0968b4692ac617c5a9843ca6d" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
								<Image BaseName="[string]Image" Id="72ee2fb71b604337bb8b52aef33c6a7c" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
							</ComposableButton>
							<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]3ad74d3320914bd684fee1d78b291ce9" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="ece6d081649c45cdac6ff275da9ad8ac" IsMomentary="[bool]True" Label="[UIModel]2a3510ad2c1f484b8588b3402c17a7cf" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
								<Image BaseName="[string]Image" Id="3ad74d3320914bd684fee1d78b291ce9" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
							</ComposableButton>
							<Label Id="a1e2db370a4347a1b7b4f7ec608bf49b" LabelOwner="[UIModel]e36593c7f66349c281e94883062769d3" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
							<Label Id="f1ed624ee93d4a0fa18ef9b0fd37c26b" LabelOwner="[UIModel]d896a0d607a04392880cefa3e057f3d1" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
							<Label Id="a05c22e0968b4692ac617c5a9843ca6d" LabelOwner="[UIModel]72e435fda6ef4ac7bfab54ad26bc5fbb" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
							<Label Id="2a3510ad2c1f484b8588b3402c17a7cf" LabelOwner="[UIModel]ece6d081649c45cdac6ff275da9ad8ac" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						</ArrayGraphTools>
						<Label Height="[float]16" Id="45cb453d017b46fb9cd8ba884ab400b5" LabelOwner="[UIModel]55832a03a09840c7bcc02e73ffc7c969" Left="[float]14" Text="[string]Acquired Samples (V)" Top="[float]7" Width="[float]113" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="c843cffbda5f44fab93f75ead1c033e7" LabelOwner="[UIModel]c05c5ed32e6e4651be749e14d2915aa5" Left="[float]215" Text="[string]Measurement Results" Top="[float]102" Width="[float]114" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{e7e5202f-6a5e-4509-940a-f9ec4f0f693d}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="966f8d6f7b43474ab68419ebb3866f4a" Label="[UIModel]895320af1fa64147a503382c11446a36" Left="[float]40" Top="[float]46" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="895320af1fa64147a503382c11446a36" LabelOwner="[UIModel]966f8d6f7b43474ab68419ebb3866f4a" Left="[float]40" Text="[string]pin_name" Top="[float]26" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/NIDAQmxAnalogInput_example.seq sha256=ef072e832a2b2683b59b3726e3877dc6cb9ed4f3a3b0b49a867af96a995a89eb bytes=175015 -->
## FILE: examples/nidaqmx_analog_input/NIDAQmxAnalogInput_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/NIDAQmxAnalogInput_example.seq`
- sha256: `ef072e832a2b2683b59b3726e3877dc6cb9ed4f3a3b0b49a867af96a995a89eb`
- bytes: 175015

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.1.0.49154' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='20'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='19'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDG=_C@0@m;K9ooPKNaRe=jBhe@3;94XEKY&lt;BFBL@&lt;i]aScT_]W^33W_WlFASWS0Ji7d_VTmik5k[=^cEQa003:MBOH`@BdfHQ0&gt;;Q]A8d982Hd5i6B957794BKQLYKED4LBURJ0AE_Y3N_&lt;Ilae[=oC\elZKMP2\5XVHY2G4TWX@XAn2B@VDhk\Cg^3Ya6Di^@J3&gt;KCR4L6H7T5A^1&gt;T:J0LRHD@F2&gt;cWoFI4PdhoO_Zf1XTiQSbcf47CkAde65BUOi@?NFiaGU&gt;6D=5JHW5HOF`ZF[?PiIDE`X[&lt;lV;[oW\ZMV;=g&gt;gg[gK]?7GmanI3OoW?5^gAdPm&lt;^mX[&lt;?nBk0KQ35n&lt;&gt;l;ajNjL4HO^jOOkkGfaJ7]EYGU7CHQKKHc_T@6OjQFlne7dOAR93BE]3QYAaXh6^?D1N[RmJLQZi^R[;AEEQ5mDN5eH;J9UBSQX2C=:hY?bWnXf[S?fejE`&gt;]`OY^36:Ml8&gt;5=8edN^YoSdd@]NoeY_`blioV?[j=f=jmPkN1&lt;N8EbWZ?\\m;dHA:GH:=1&gt;;2ZN]SkE[VVd&lt;&gt;hcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX3R?_6&lt;Tn5_WM4Oc^CSZK3JMWMokkOWQ&gt;KL6kg\PXgM`dE0V</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AOfkIjf;oeo][I[[g8alkF7&gt;d&lt;:A2eiaSaRiA`Tk;D&lt;dD\SUHKoiMH`S`&gt;8R&lt;miAf9L^@G:dRd4XNZ4?H5P&gt;`2GX:\M5BmoJ_GeJMg&gt;Ng3`]g8N5A]F[X_kCNOY]\k]dKUI@&gt;2D_29YM=4:d?gKkM_d42ieGQVe4;el;cScZ^o^^]JekkiM\&gt;CKmlH9&lt;V:aJn=Hl`_dk3No6]Kf[eM`cZ2dnk]jjeml[\f^=&gt;TNkCNWNIo?^OF&lt;nM3OkX`nk_Jn&gt;n_K7?HoMO`NON7NloAC;oog;c]GkG9WmVA9cS;B]^LaJbe:n_lejX[J4^_Bd0@I@^RLhA7a]&lt;m17UQ8RB_7]6o78m&lt;n]g9jEZKiBlmJa80[WeRL5Qn[SV`eW8jGfkaOnhR6k`XAW5Uhe2JgJgK6Ao[N@8&gt;CK7oMM&gt;d1fSh2mgU9agAWIkWM^WaPP_6iL;hT[G`GXJl5QoXOL?T&gt;7gkG3co15h@^dNNLM=dokeOhb_B6US2oHMBN?_o63;Z;k;oSc1WCoeRJYIVlYJMLK@Q]fcEFNlW1[n[]eJHIJ93fIC7`5FQ9G&lt;iN=R;W&lt;9jh&lt;ZQ3fLS[:=SBo3]U:mdP?o&gt;i_LI7AlUlLj;^:6A1VJJ6DF`QT8_lej9`I;\i&gt;0@HG5j&gt;AoPRDgQOk9:b]jeEd:o^;kXgDTn\D2TC&gt;Mbo4=MFgAJ61[EdIFAFCB9GFD^E;Ua_m^Q@C7\^2]AMnH&lt;URI4liRYTNnH&gt;U=HSdP436l=_`d2E3fRBnl2H=^g7ghj_KkeQh`2^NgI4`L1:Z]oTjc^EW40R1=^Z&lt;BRQiPPUCjHh=oG1hVJ3Rf&lt;e\mS0R&lt;FCDideh:lZib5&lt;F;LUceKYR9?WUXDZb[JgC&lt;m7RGZV\ACPlWMI7QbXl:16fCSPj26SfbGYhgn1:O7N]o]_eV[ka:KodOC@EZ6a]4lU3&lt;MXIBQFEYjbT&lt;Veo1:n@_dXfB`=bT@el2cWU9GWT\B=UmE2GUoHo7gg_g1nlnNlj^WmomjBoMlgWod]k_^?kLG2TM9cLbb&lt;V1^_7^g9C3jOb9XSnC6kDSkf3h&gt;25Th=&gt;cRSjR6KHHJ=9ChVO7jCE7jhEWcCjLM__eJh11VV=VN:?;EPeRjZ\SLGUWd83;LRM6^2&lt;]CNb=oQ9_d^hlRnNNhL&lt;7IgIJ59Z&lt;o4T[mKJV3kQ]18ISO&gt;];XLBEdGQYJofOmBD&lt;AXA9M9;Wd=?ZZZHg=5BO8hYk=fd9PC@7&gt;[JQYl]G]^o^2WKJ3ojnfD3Q@h4D7]F801DhI7;k:Db[mf5ZRQ@d][PKaB5:@PkaBfWbW9O0HEl8BDiW[4UE\]A_5V]N1b1:LLQEH[Qc0hYAS0AJ;B&gt;@cdkY6`=;;H=ED4\DUS@gg0V]XQD39NjY&gt;f3N&gt;K4DMP\8YVbTc3iU3SOC@YI3kMQ[If=`N[i=j4\DWZ?FKV`fRT5&gt;b3iVYUdJ71a0e&gt;:hXWdEmLk^^ddLd7?YM492MFBPj^RHWoXY`d2lJoElC[Z4U6WjF:PEjZLA6QKSk5NY88@@XGEHK6G;^dVj@co]T3j1l8TXnI8:VAeNDXI@D9M@@8JBlGDAT6RSUMJFZ;n;8kO4\ZH&gt;42G7A:NPT9h3n?=9BdEf[bBW1[_f07NGhgE]NN[;F7cEe&gt;953\KklXhKFfmEH;XaceCUjeG[HHb`ZVLUULdi&lt;A]&lt;ild:aVc\ibmbUF=:0e;f[ZB64C7Yj5;3efQ75mDBU1DcG8BZad1=hNQY^af&lt;UVo:ZVf^@0d_M5ObRQ2PIHR9bbbG][HZ\KEfEYI=E];E@9j1kZ@2@FIkf9:\CYe5KNCANXH7R@eMa2M;Pm]PZG]@4h2Q7OY:5QFk@\Y6]E6X1bL6mjS77a`ZS=H=XQReG6Djb7[c&lt;h@S9UC[4`ABLQ4:ZZ7=JF9JejC5\[T:meE5[[:`Qm=DfI0EDQLRJ2o]Q@o1FhU9oA7hi??EPmHoZhA11dfjSE;aYISGCSD5ChjcQWk3eLIH6mg&gt;X_6k5ScmijD1:\]6jkV2OHJBbHXFV=RIibbaX5_jV^PSGHFK901\5D;@f@6aV4ecHA\_8c:5JUTf]RP@dJaD^Q5mgghUa4?dKcBOP@BIh4J:;?4:=heLolo&gt;mDcPFYYaJPQaC[DhBcm779BiUBG9?=Vh8ZHhd\hCK[N:SkYicVdi1R61k0=7foTQ=o\]_U7W8elK:MO6dhEY@1n[N=_SRI\X4TP[7IMJY1H&lt;`fko@8PLGC9`2H:i9H7JiPYI6B8Y5K0A8`C6H&lt;d34UZo2O&lt;&lt;1H54JTEA34`dBGbMV:0;VGY0@2_DQP880H7RKdi:03?e02&gt;e5lie\01lU`@;4&lt;5PTQN0G1^kP]G`N@IEMe=:ViEY3fZ=E\:]UCB^LAFb?Xe\A9McEBQ=c:Lj1eMiR[5En:neQe0fZdUOCZiF1B:T0gdc^ohlH[d8ARdJXR9kOcAdkTAXl66\A2Qe]nL=T4N5j&gt;DDaKH[R:VORK22O6Q4dLSB0iOEBb@g_[`]9ViUnT0jMin6j[FBoSc?NFn4^XVjanK=\7=6AeK[:f1;YaYG&lt;QIF_KZ=@h@h3]S2RVCMn26J&lt;V2&gt;?Ca`87g?a8OlI4CE8&lt;iOUmV6VH=o`amSW&gt;YiAKgn4hcmGPhPi1ACEUc`B_[k=agB09FNl`nC\eQBE_Mo4Jlho6ml^NcoYU&lt;lP`R\I9f06jOViFeZJ5@_44Tb6[Ya\I4G0okM_QO&gt;RDCHhb@kYI_cGZ\FL`^78QjN7?dIE8V9K\FTbDh]\;@iNFF?&gt;KQB=CSdR=TBfan9K]LIJjSeK:;=7naRo93XhAO`fS8R950ogH[BPdh]ohPRk&lt;1_eLkXZjAfU[@TFcOkIQlbQlnjd_&gt;h&gt;7Kl1=ibmRZM6^AX1EnCR=W61Lgd&gt;3LW49RLl?3n^Z6Yg&lt;[7[A3iIQWhVbIF5U5n6@Po=c;S&lt;WOj_=:B@S;De=m9c^PBaT6HnUHRU]@SZcc6n6I_`LIRaGBYab3@[`9Kg1@TcFH7^=?2Z`?8a3oA47&lt;dFVS65TW]CP67?CMe`i2lW\3fQRB:N\jIfSjKIQ@A42Z`Lf2iGJCU:[T0V:\2H?5DVWg[7XVM4HcF0iEAaeaF]G=d595=n4X&lt;2\&gt;KjSDC]CDY;Cm3YACED]C&lt;][dhSkmP&gt;^AAkJLT&gt;3GOm3VjS`D4PkCnSg?HfdN_@25I4AmBU3H5a[c8hY8h&lt;&lt;m9Bo?M^:9;j[EOU47fABBC@\on6mZ0F;E5TAH:4gfMo?mMQXa5@RLeF0k^d:8Tb66&lt;j6&lt;&lt;e0AMKoN:V8`dU3=&lt;P2iElNOQXZcnhmB&gt;4g5h@nJgDj&lt;S9@KHf9IJ:2N3RYKO7bfH=J\bBb0W8lDCf41\_hQ;Q@Y3=IPO:4IUaKK[P:2c8A&lt;7I\j&gt;S7nF5iMK1ALc6ERR15XHY8gbdhMUh5&gt;BFKL:^l@5LL@B[:2GlB8oRgi^]8h;l2m`:&gt;QG3@LSVEbn4YFUE5Qn\M=&lt;3YoY;f61;N6N966Tmg2lg[2^_JUeEC\JO`KoOh207^MlX871jfcBGKW5cLE7^WB&gt;2d6Da]Z&gt;a[ETS1233XEL6@AVTl`RiIR?3X3iX6H?nYfJ;:YAj;fYnIV]P=Q3??IgPJD[UP8bk1NhRP0CNEo4kT[P13:?X8d6j87jQh2RS]E\d02go;UW9D9R:7eRej4SRek0NRG8NLZ;gkLcQ8LE0aUNTd:K4XE?1d;ZS`LkSZj019Yn0n6eI1Le8jnHGlRA^6AajoXj:FFEC0eCTAi^0S[b2iT=dE[:c\JN:`2aZPb`F5QYZaiLN5iS\[CWjFNcjfLe`WZOFJk^WB_]7i[?GIk&gt;gJcF^NKd0mWfkIZ5=01`jg=Z09l\n?PNdd1H;6QlMKITgFS3d4eQK42h4`&gt;n_?VZ01SiSfGa7VG_AbbI[5Q6iAD2L\5Qh;LPoOiPZ9mTmEIDGn7;aTNi`anFZNL22`NSZ?JK[W2c0K55&lt;f[dBH\ZSCYAZMVV&gt;Fc0G2QAadLH^I0omB0f&lt;;kR&gt;1Im9Al:D@9^G;FJeU?m]DPloDimg]IkOfoToUbfoWP]o1I1_7hD5n:P2OUXDD4XmAGec=Ke]KXCHj8HFoUO4WPhHoB;fOZf[nmo\]JNlfngek@12MQn[i[N3fbkJCR[\D8nDI@DTc?FO\I;jNB_e]U_lfj]A@PkkIKEQf_JmK\UN_fb2g]E`EOojfbg&lt;dGnMI`5j5bn\a7;\bk7O\X:X6^&lt;3SEf`Y2Kh?ZGi?b?6GlAc1\kJd1=OVIhX2=_OD:JJXFd\DEf&gt;K=R]:HXYF=Vna\ofnXFKmj06nM`bYhPNm4P\@MnDRPO&gt;a@]W8m4WPFXYQ6?@_Oa_X[&lt;oI[[;[EmE[OO@_OaU`JP3OaH`\S6VbcS`f=3jk61hN4WSiJBUnQPbO`PLhIg&lt;&lt;\K&lt;6f=&gt;3k6B1=F`f=3ik61[fHI3g&lt;\0K6&lt;&gt;Gk6W1m3G00NUnQPcO`@gX9kV61U&lt;?\K&lt;6f=Y3]\LLHg0&lt;d3inBX[omcDFSKG1_om2NiN[_l_UiJ5k_C?Bf&gt;GKkWF]IZ;N:FdNi[_O[dJVjojPMgbf=37][?nYbcjfLehW\mNW]iJZU]7mW]Si\GfJcJW=UO9`@oWmUO&gt;`HbA_HDLeWcWoQ0ol65dCg92:J9[6&gt;anhd`^i8eC^Si;jk8\WKnm\^f&lt;&gt;hKLnfjoM&gt;1M1ITWINdoA&lt;1GehUhLoN4&gt;^_Gnni@7eUgoijKjHomijTdWR`1^b66?&gt;hX\TlGm:oIl=ooOU2hW9oW&gt;?f;kRDR3FGAJT`e]DYQFRIiCGL\WId6l&gt;QS[Yd?a;KR@^6CgE_XBj=\9;bfa&lt;1Ag\dGmAAQ`BhYO6^XWHZfPXJIiHRfBRONB7IFDhA?RgAf0_D8i&lt;BO?AL@54GF@]WL@^=f2^P^noWPaK9GhlJR^NdC:0&gt;YMAGEWX?n:lh@eLhY9aShVbImK7b?W=@;k[1NMR?D9\IQi7VfXjYY?O;QL]m0_;lC2UfU[PCTLEmCMG:TXg0WW9KGKB&lt;9;0o94HSIB?8aT:a[F7L`iQ_J4E[djh`gdWdHJNU5`6W8SahGV1XgjA\ahC4UN1jdFYoXS]?SnjbH7Uh:UYn9DUj1TZ[NeZbV2OXWogLN90ol75l&gt;N5m5K5@&gt;PP[IA2&lt;KjdQoLl55XA[IU?6&gt;ebd`Pm:F3gJgKbk_Mm^HNW=Qof5XgC^gf8@c2LRA83\HT0c6B0&lt;]d@5Lj0R9QV825WB9S9H8@A9Dn86:MBQT6d1M3PT&gt;=141dA2]bi:S&lt;;BQ349dMiQ4@8;83TPa;SoD&lt;1oT2Q2E1mdAAnPC062ofX3CjD=910iMZPh&lt;4=RL1_H40gTCj=2DeZPCe4bL;`ihePi@BNRH0&gt;97F7B@&gt;`2A7Ol=3jf?`T64&lt;]372]T0HKCIh=l1Z311eJh3JIHJ10RcA0@a8YbQ`I3i4&lt;XS]GS@T&lt;Q3b2210`60OCS\P9SAQd1=`bV5E2ODdA_LZBlhFU6a&lt;5X3=0LCB7G62`0`@\j@0FUT654AOa0Q^84=FPEH&lt;PZ405fV`_8B=a4ZU084DC`P:I&gt;:56PIXP?&lt;T6&lt;S7iAZ6K8AmCV?6@6ZG8XHaXB6C09X0P8I6R6U@D2oi]MFf[oa3kiKIjfa26SG&lt;dQ7U:j:lXT96N4R;;84RI?K0R5@K7fXR=HXA&lt;C20W2?m1ODF^X4&lt;Y9a38]J6OdHNWFE6LkiTZ7Hfo^3BbMN__fFf9\17&gt;NBd&gt;NEefg\[2E]OA\Q=RcDhnQM2BE3A4=Q8gLRfRcG@ZQB_&lt;&gt;BZ2W1dg`C0CL&lt;1AoRF95DM5k47VKAR`]EPC\o;hP0UHc96&gt;KjZMdBDNb:DO_1djJ1YoE1Ym@LIW\TUT3F5kcP\@J0llY1kgYEbTBbS&lt;AjTPTa1I9hhH:ChbBe`@TP=]OgIA8ee&gt;1F:_]3emkNHSX_IZ4]SaQd7JbH8?hF:_[ACM\3dnCSXj&gt;SXl9FXnKWc8Sj0S;QB]6bA&gt;_gfI5_jK:SLHjR7Ce&gt;fR5C7B1WM65G14a4I4P1XP0\BD0VAHS`4JUaFXQib]AHR=BI[DH\S4J4UK6H692?&gt;1cTW1@[m;Q5Mc&lt;P6LAN8V_&gt;Q9Pn?8`3i@`E1dH;X=7oi8SVSBjCVAcER]FbFQSb:Uaka\8cj?CglAS:METE^3oi6O;=BeIcIJBLn:jTW8@U3E4KAmTFHi[1[h[S&gt;CU9MEPEJ:eG8nCHJ@UD\&lt;8EPQAT3STPhHN9BS4c38V0g&gt;3QS9oAAPOX4PGNa\CX1j0:XGecJNJ9:QBCPL&lt;R6i;`PbiKBVD`8dQ]K\Xd=TbF0\=IXXE3Ae9hV4oHaFhSAa7dimONCT;C8_B:m;BISA&gt;A=cJ`WfEVSKacF;jP4i8ND\YclI^B]5`H2e&lt;foFg8LD7;jnW:X:L?iW?ZHL2VV8XdLZCRbR7bjhL9W;CbRf]mWbFJ8aiAmg&lt;_?cD8EnPl0V`[a0JTGL;BR15[Q]WC;g2Y:YlTdmcmdSWBhd1\g3E4&lt;D&gt;PfYDY4cBbke[[PZ1P`_B=mIk&lt;VW87&lt;^H6GGTL:Yc_K5UB4UMigYI5T;TA;UV6HK\aGTc`Adi=mjooloR`^</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
										<PinMapId classname='Str'>
											<value/>
										</PinMapId>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Create analog input channel and read samples'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:W65BBITt7RG/aYRpk281PB</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIDAQmxAnalogInput_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[3]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_name</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Pin1"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>sample_rate</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>1000</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>number_of_samples</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>100ui64</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeUint64</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>acquired_samples</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:ecs1KueU7hGhxWDjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>"NIDAQmxAnalogInput.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DAQmx Tasks'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:t3JO4YPt7RG/aYRpk281PB</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidaqmx.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nidaqmx_tasks</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DAQmx tasks'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:wPUc94Pt7RG/aYRpk281PB</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidaqmx.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nidaqmx_tasks</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nidaqmx_analog_input/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/pyproject.toml sha256=7bd5f6a5c17cb48e7f7d9328e4e9309e4336636b9ed54d3dbb2521b274bbe0a7 bytes=1085 -->
## FILE: examples/nidaqmx_analog_input/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/pyproject.toml`
- sha256: `7bd5f6a5c17cb48e7f7d9328e4e9309e4336636b9ed54d3dbb2521b274bbe0a7`
- bytes: 1085

````toml
[tool.poetry]
name = "nidaqmx_analog_input"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that performs a finite analog input measurement with NI-DAQmx."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nidaqmx = { version = ">=0.8.0", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidaqmx = { git = "https://github.com/ni/nidaqmx-python.git", branch = "master", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "nidaqmx.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/README.md sha256=c5551f81b0fb08656ebdc8e61f631d2c9a0ce085ee827d8a6b5d4e5e67b4552f bytes=1608 -->
## FILE: examples/nidaqmx_analog_input/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/README.md`
- sha256: `c5551f81b0fb08656ebdc8e61f631d2c9a0ce085ee827d8a6b5d4e5e67b4552f`
- bytes: 1608

````markdown
## NI-DAQmx Analog Input Measurement

This is a measurement plug-in example that performs a finite analog input
measurement with NI-DAQmx.

### Features

- Uses the `nidaqmx-python` package to access NI-DAQmx from Python
- Pin-aware, supporting one session, one pin, and one selected site
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and session
    registration and unregistration in the `Setup` and `Cleanup` sections of the main
    sequence. For **Test UUTs** and batch process model use cases, these steps should
    be moved to the `ProcessSetup` and `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other measurement
  services when running measurements from TestStand.

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-DAQmx
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires a DAQmx device that supports AI voltage measurements (e.g.
PCIe-6363 or other X Series device).

To simulate a DAQmx device in software: open `NI MAX`, right-click `Devices and Interfaces`,
select `Create New...`, and select `Simulated NI-DAQmx Device or Modular Instrument`.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nidaqmx_analog_input/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidaqmx_analog_input/teststand_nidaqmx.py sha256=7094ed5f0316b36a301bf5ca60619ce84517b1a1c012284af6f5182973aa333c bytes=2739 -->
## FILE: examples/nidaqmx_analog_input/teststand_nidaqmx.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidaqmx_analog_input/teststand_nidaqmx.py`
- sha256: `7094ed5f0316b36a301bf5ca60619ce84517b1a1c012284af6f5182973aa333c`
- bytes: 2739

````python
"""Functions to set up and tear down sessions of NI-DAQmx devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DAQMX,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidaqmx_tasks(sequence_context: Any) -> None:
    """Create and register all NI-DAQmx tasks.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()

        if not pin_map_id:
            return

        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )

        with session_management_client.reserve_sessions(
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_DAQMX
        ) as reservation:
            with reservation.create_nidaqmx_tasks(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ) as tasks:
                for task in tasks:
                    task.session.ai_channels.add_ai_voltage_chan(task.channel_list)

            session_management_client.register_sessions(reservation.session_info)


def destroy_nidaqmx_tasks() -> None:
    """Destroy and unregister all NI-DAQmx tasks."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DAQMX,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.create_nidaqmx_tasks(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nidcpower_source_dc_voltage/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nidcpower_source_dc_voltage/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nidcpower_source_dc_voltage/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/measurement.py sha256=2922ca2bd554a8dabd4a9a704dadfa1e88099c022c63e928ab05f3b94ae0b553 bytes=8697 -->
## FILE: examples/nidcpower_source_dc_voltage/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/measurement.py`
- sha256: `2922ca2bd554a8dabd4a9a704dadfa1e88099c022c63e928ab05f3b94ae0b553`
- bytes: 8697

````python
"""Source and measure a DC voltage with an NI SMU."""

from __future__ import annotations

import logging
import pathlib
import sys
import threading
import time
from collections.abc import Iterable
from contextlib import ExitStack
from typing import TYPE_CHECKING, NamedTuple

import click
import grpc
import hightime
import ni_measurement_plugin_sdk_service as nims
import nidcpower
import nidcpower.session
from _helpers import configure_logging, verbosity_option

_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059
_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933
_NIDCPOWER_TIMEOUT_ERROR_CODES = [
    _NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE,
    _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE,
]

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDCPowerSourceDCVoltage.serviceconfig",
    ui_file_paths=[
        service_directory / "NIDCPowerSourceDCVoltage.measui",
        service_directory / "NIDCPowerSourceDCVoltageUI.vi",
    ],
)

if TYPE_CHECKING:
    # The nidcpower Measurement named tuple doesn't support type annotations:
    # https://github.com/ni/nimi-python/issues/1885
    class _Measurement(NamedTuple):
        voltage: float
        current: float
        in_compliance: bool
        channel: str


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_names",
    nims.DataType.IOResourceArray1D,
    ["Pin1"],
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DCPOWER,
)
@measurement_service.configuration("voltage_level", nims.DataType.Double, 6.0)
@measurement_service.configuration("voltage_level_range", nims.DataType.Double, 6.0)
@measurement_service.configuration("current_limit", nims.DataType.Double, 0.01)
@measurement_service.configuration("current_limit_range", nims.DataType.Double, 0.01)
@measurement_service.configuration("source_delay", nims.DataType.Double, 0.0)
@measurement_service.output("measurement_sites", nims.DataType.Int32Array1D)
@measurement_service.output("measurement_pin_names", nims.DataType.StringArray1D)
@measurement_service.output("voltage_measurements", nims.DataType.DoubleArray1D)
@measurement_service.output("current_measurements", nims.DataType.DoubleArray1D)
@measurement_service.output("in_compliance", nims.DataType.BooleanArray1D)
def measure(
    pin_names: Iterable[str],
    voltage_level: float,
    voltage_level_range: float,
    current_limit: float,
    current_limit_range: float,
    source_delay: float,
) -> tuple[list[int], list[str], list[float], list[float], list[bool]]:
    """Source and measure a DC voltage with an NI SMU."""
    logging.info("Executing measurement: pin_names=%s voltage_level=%g", pin_names, voltage_level)

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    with measurement_service.context.reserve_sessions(pin_names) as reservation:
        with reservation.initialize_nidcpower_sessions() as session_infos:
            # Configure the same channel settings for all of the sessions corresponding
            # to the selected pins and sites.
            for session_info in session_infos:
                channels = session_info.session.channels[session_info.channel_list]
                channels.source_mode = nidcpower.SourceMode.SINGLE_POINT
                channels.output_function = nidcpower.OutputFunction.DC_VOLTAGE
                channels.current_limit = current_limit
                channels.voltage_level_range = voltage_level_range
                channels.current_limit_range = current_limit_range
                channels.source_delay = hightime.timedelta(seconds=source_delay)
                channels.voltage_level = voltage_level

            with ExitStack() as stack:
                # Initiate the channels to start sourcing the outputs. initiate()
                # returns a context manager that aborts the measurement when the
                # function returns or raises an exception.
                for session_info in session_infos:
                    channels = session_info.session.channels[session_info.channel_list]
                    stack.enter_context(channels.initiate())

                # Wait for the outputs to settle.
                for session_info in session_infos:
                    channels = session_info.session.channels[session_info.channel_list]
                    timeout = source_delay + 10.0
                    _wait_for_event(
                        channels, cancellation_event, nidcpower.enums.Event.SOURCE_COMPLETE, timeout
                    )

                measurements: list[_Measurement] = []
                measured_sites, measured_pins = [], []
                for session_info in session_infos:
                    channels = session_info.session.channels[session_info.channel_list]
                    # Measure the voltage and current for each output of the session.
                    session_measurements: list[_Measurement] = channels.measure_multiple()

                    for measurement, channel_mapping in zip(
                        session_measurements, session_info.channel_mappings
                    ):
                        measured_sites.append(channel_mapping.site)
                        measured_pins.append(channel_mapping.pin_or_relay_name)
                        # Determine whether the outputs are in compliance.
                        in_compliance = session_info.session.channels[
                            channel_mapping.channel
                        ].query_in_compliance()
                        measurements.append(measurement._replace(in_compliance=in_compliance))

                # Reset the channels to a known state
                for session_info in session_infos:
                    session_info.session.channels[session_info.channel_list].reset()

    _log_measurements(measured_sites, measured_pins, measurements)
    logging.info("Completed measurement")
    return (
        measured_sites,
        measured_pins,
        [measurement.voltage for measurement in measurements],
        [measurement.current for measurement in measurements],
        [measurement.in_compliance for measurement in measurements],
    )


def _wait_for_event(
    channels: nidcpower.session._SessionBase,
    cancellation_event: threading.Event,
    event_id: nidcpower.enums.Event,
    timeout: float,
) -> None:
    """Wait for a NI-DCPower event or until error/cancellation occurs."""
    grpc_deadline = time.time() + measurement_service.context.time_remaining
    user_deadline = time.time() + timeout

    while True:
        if time.time() > user_deadline:
            raise TimeoutError("User timeout expired.")
        if time.time() > grpc_deadline:
            measurement_service.context.abort(
                grpc.StatusCode.DEADLINE_EXCEEDED, "Deadline exceeded."
            )
        if cancellation_event.is_set():
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

        # Wait for the NI-DCPower event. If this takes more than 100 ms, check
        # whether the measurement was canceled and try again. NI-DCPower does
        # not support canceling a call to wait_for_event().
        try:
            channels.wait_for_event(event_id, timeout=100e-3)
            break
        except nidcpower.errors.DriverError as e:
            if e.code in _NIDCPOWER_TIMEOUT_ERROR_CODES:
                pass
            raise


def _log_measurements(
    measured_sites: Iterable[int],
    measured_pins: Iterable[str],
    measured_values: Iterable[_Measurement],
) -> None:
    """Log the measured values."""
    for site, pin, measurement in zip(measured_sites, measured_pins, measured_values):
        logging.info("site%s/%s:", site, pin)
        logging.info("  Voltage: %g V", measurement.voltage)
        logging.info("  Current: %g A", measurement.current)
        logging.info("  In compliance: %s", str(measurement.in_compliance))


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Source and measure a DC voltage with an NI SMU."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.instudioproj sha256=3630d67935fbffa35b0239af406759db8a25b9a1a1725da38859f1b29a37c190 bytes=2371 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.instudioproj`
- sha256: `3630d67935fbffa35b0239af406759db8a25b9a1a1725da38859f1b29a37c190`
- bytes: 2371

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4C6BECCA0D21294BCE52F31331FDB216364768CDB4966FE4D62971BA26D86B19F3E10E460E1285D771F77F7BD4C939CE9DF677F54DCC8F9AA86636187BB48246" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.49209" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Bindings="EnvoyManager" Id="f1ebf300716a4e8981e7787fd3952439" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIDCPowerSourceDCVoltage.sfp" StoragePath="NIDCPowerSourceDCVoltage.sfp" />
			<FileReference Id="4397ed0e27a5481ab8c036e349785f8b" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltage.pinmap" StoragePath="NIDCPowerSourceDCVoltage.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<FileReference Id="b46168340401481b8a80bed868847f07" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltageMultiSite.pinmap" StoragePath="NIDCPowerSourceDCVoltageMultiSite.pinmap" p4:IsActive="False" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measproj sha256=df679c2f02b5caf91e9ed6f78559d31d5cc95274641b3324eb9fcacddb54c6b7 bytes=4163 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measproj`
- sha256: `df679c2f02b5caf91e9ed6f78559d31d5cc95274641b3324eb9fcacddb54c6b7`
- bytes: 4163

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="0C2EB814D8491B6A34EEA0D1628817D40020EB63070FC49F6D971076EBCDB8DF7DD90E6E46EDC4D63A8AD40A4DB861B56908A423842625F6A16EDE51CD416085" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="MeasurementLink UI Editor" Version="23.0.0.49209" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="fbc7425437e74709a87389750d4ee99c" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="3465fdfd72c44abaad0599621bd6c6f9" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="680a32f2c4b248a4a615cf8eeaffee0e" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="5512fcab475b463488357fb0d38af2e8" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="875ab222a6a348baa083d8ac871eed14" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="d90a253c17d546b9a38926745fad77e8" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="9cc9e23567d4c3cbe6a91cfaa10b772" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="cce43756a09e455ca4a22e97b9903eac" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="ddfe85c7feb34c34ae3a5c7b958ed764" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="25f25c7dd8a48e4846a48452fa47c09" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="7c869e6a42a8474d86779ed686991145" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIDCPowerSourceDCVoltage.measui" StoragePath="NIDCPowerSourceDCVoltage.measui" />
			<FileReference Id="4bacc157c73d4873a743b1a055f4db93" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltage.pinmap" StoragePath="NIDCPowerSourceDCVoltage.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<FileReference Id="15a41629700344d2923b6759febdc0c8" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltageMultiSite.pinmap" StoragePath="NIDCPowerSourceDCVoltageMultiSite.pinmap" p4:IsActive="False" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measui sha256=76eb5913a68ca45218907229c8b741bafad06c145e4c78d988d6b9bc9105372e bytes=9990 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.measui`
- sha256: `76eb5913a68ca45218907229c8b741bafad06c145e4c78d988d6b9bc9105372e`
- bytes: 9990

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D2B5B58C60BCC4B987EFD881E5AA548727861346ECD03CB1B808E5D5F41E3ABA8873F66A1DB3F7748EB310E9C413EB4D96CEAD4B6BD04F286C635F86DD1979B0" Timestamp="1D92FDBE7FEA2F3" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.49409" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49409" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49409" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49409" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49409" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49409" Name="MeasurementLink UI Editor" Version="23.0.0.49409" />
	</SourceModelFeatureSet>
	<Screen ClientId="{5f88d1ec-4b12-4bf9-b28f-707b534a0575}" DisplayName="NI-DCPower Source DC Voltage (Py)" Id="ce8cc70d4b0b487db029384b996c0e8a" ServiceClass="ni.examples.NIDCPowerSourceDCVoltage_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]430" Id="1224789d85bd4cdfa59e83e724ab737e" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]965" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="4b93ed01d79049dc8d2c3ef426384b35" Label="[UIModel]2f53b6c7f87b41879b8d84f4fb87c844" Left="[float]40" Top="[float]100" Width="[float]200">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="53ab9fe640e341c9b5aa585471c4663a" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d1dfd1838e5a4868b62e7cdf74391ee8" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="7b7ddd28c1b44bd28cfbc5dc5341cef6" IsLabelBoundToChannel="[bool]False" Label="[UIModel]cfd32e3f5ee34b34a17ce4b52396c18b" Left="[float]20" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="daf74d9eb82c4002bdbb9a9bfa6c4de1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]a6828bc2eff448d7ac8a62a35d6f7e58" Left="[float]20" Top="[float]136" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="7440e0cbaa914daf82d80ba5f43ba2b2" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7fdce012e2a44ac4b5370b7ddcb210cb" Left="[float]20" Top="[float]186" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="47497842bba8443594fb99159509f596" IsLabelBoundToChannel="[bool]False" Label="[UIModel]8180acb567174824aa1b4126e857ad96" Left="[float]20" Top="[float]236" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<Label Height="[float]16" Id="d1dfd1838e5a4868b62e7cdf74391ee8" LabelOwner="[UIModel]53ab9fe640e341c9b5aa585471c4663a" Left="[float]20" Text="[string]Voltage level (V)" Top="[float]16" Width="[float]87" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="cfd32e3f5ee34b34a17ce4b52396c18b" LabelOwner="[UIModel]7b7ddd28c1b44bd28cfbc5dc5341cef6" Left="[float]20" Text="[string]Current limit (A)" Top="[float]66" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="a6828bc2eff448d7ac8a62a35d6f7e58" LabelOwner="[UIModel]daf74d9eb82c4002bdbb9a9bfa6c4de1" Left="[float]20" Text="[string]Voltage level range (V)" Top="[float]116" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="7fdce012e2a44ac4b5370b7ddcb210cb" LabelOwner="[UIModel]7440e0cbaa914daf82d80ba5f43ba2b2" Left="[float]20" Text="[string]Current limit range (A)" Top="[float]166" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="8180acb567174824aa1b4126e857ad96" LabelOwner="[UIModel]47497842bba8443594fb99159509f596" Left="[float]20" Text="[string]Source delay (s)" Top="[float]216" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="3507d01be4bc4a26abc81ac1e2385674" Label="[UIModel]82dfa849cb640f9bdcd4d7c1256e976" Left="[float]280" Top="[float]100" Width="[float]200">
				<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]6e8992aae57c44c5812a2427f6b854a0" BaseName="[string]Numeric Array Output" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Output/voltage_measurements" Columns="[int]1" Dimensions="[int]1" Height="[float]92" Id="b04aec8bf54647c38292530477837acb" IndexVisibility="[Visibility]Collapsed" IsLabelBoundToChannel="[bool]False" Label="[UIModel]bde6e8dbce014cbebf66e1e5b206804d" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]3" Top="[float]36" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
					<p.DefaultElementValue>0x0</p.DefaultElementValue>
					<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="6e8992aae57c44c5812a2427f6b854a0" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
				</ChannelArrayViewer>
				<Label Height="[float]16" Id="bde6e8dbce014cbebf66e1e5b206804d" LabelOwner="[UIModel]b04aec8bf54647c38292530477837acb" Left="[float]20" Text="[string]Voltage measurements (V)" Top="[float]16" Width="[float]140" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]ad4e0ff072b74611af269b485ed3f644" BaseName="[string]Numeric Array Output" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Output/current_measurements" Columns="[int]1" Dimensions="[int]1" FirstIndex="[ArrayElementIndex]0" Height="[float]92" Id="da3d64c6b9394feabc127efbd1386fd8" IndexVisibility="[Visibility]Collapsed" IsLabelBoundToChannel="[bool]False" Label="[UIModel]45bb3e7755f4599a6c968bca57a9391" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]3" Top="[float]171" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
					<p.DefaultElementValue>0x0</p.DefaultElementValue>
					<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="ad4e0ff072b74611af269b485ed3f644" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
				</ChannelArrayViewer>
				<Label Height="[float]16" Id="45bb3e7755f4599a6c968bca57a9391" LabelOwner="[UIModel]da3d64c6b9394feabc127efbd1386fd8" Left="[float]20" Text="[string]Current measurements (A)" Top="[float]151" Width="[float]139" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="2f53b6c7f87b41879b8d84f4fb87c844" LabelOwner="[UIModel]4b93ed01d79049dc8d2c3ef426384b35" Left="[float]40" Text="[string]Configuration" Top="[float]80" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
			<Label Height="[float]16" Id="82dfa849cb640f9bdcd4d7c1256e976" LabelOwner="[UIModel]3507d01be4bc4a26abc81ac1e2385674" Left="[float]280" Text="[string]Results" Top="[float]80" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="40b7c7768512477fb2d939ac81f1bb10" IsLabelBoundToChannel="[bool]False" Label="[UIModel]2104dc3428074997846caee906febdd6" Left="[float]40" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]36" Width="[float]200" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="2104dc3428074997846caee906febdd6" LabelOwner="[UIModel]40b7c7768512477fb2d939ac81f1bb10" Left="[float]40" Text="[string]Pin name" Top="[float]16" Width="[float]50" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.pinmap sha256=07416f2eee975531815fdb9687dd07c100c4f72fe8b95b50cf96cc72afd3e898 bytes=608 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.pinmap`
- sha256: `07416f2eee975531815fdb9687dd07c100c4f72fe8b95b50cf96cc72afd3e898`
- bytes: 608

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.serviceconfig sha256=adcd4508aab2a63b8332214d83ac869105b9bae25d062bad216669abc5188882 bytes=696 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.serviceconfig`
- sha256: `adcd4508aab2a63b8332214d83ac869105b9bae25d062bad216669abc5188882`
- bytes: 696

````json
{
  "services": [
    {
      "displayName": "NI-DCPower Source DC Voltage (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIDCPowerSourceDCVoltage_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that sources and measures a DC voltage with an NI SMU.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.sfp sha256=a0beade2192bb8acbb4ae9532c12635214be0ac40a52a38312db8673d1d871ed bytes=13167 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage.sfp`
- sha256: `a0beade2192bb8acbb4ae9532c12635214be0ac40a52a38312db8673d1d871ed`
- bytes: 13167

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="36F959EF63BA90E12A0DC2DA58C1B936C2C9E5B07047F0A0DA94E89AEF7D0985AB75268A8E24519F09ACC424177E67CDC8AF5FDBBE934E688D0035E3BF04F38F" Timestamp="1D924527585402E" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.49209" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="de80792c888340ee9ab7524fd0fca95e" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:4,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:3,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-DCPower Source DC Voltage (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-DCPower Source DC Voltage (Py) 1&quot;,&quot;Layout Information Index&quot;:3,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-DCPower Source DC Voltage (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIDCPowerSourceDCVoltage_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="ae40c536bb27440181886c8942f31ac0" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="50bb751ca274205a2259f40e289ea9f" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="79f6a6905bd742cf8c465a642408b366" Name="NIDCPowerSourceDCVoltage.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="e6d9f59a5bb54334b73a3fc80f1d77f7" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task">
			<Screen ClientId="{58402dff-3d3e-4d33-9cc1-dee5a551e29c}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;pinNames&quot;:[&quot;Pin1&quot;],&quot;voltageLevel&quot;:6.0,&quot;voltageLevelRange&quot;:6.0,&quot;currentLimit&quot;:0.01,&quot;currentLimitRange&quot;:0.01,&quot;sourceDelay&quot;:0.0}" DisplayName="NI-DCPower Source DC Voltage (Py)" Id="13885e67841e4dc0a414f8ea3f03eb29" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIDCPowerSourceDCVoltage_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]430" Id="dc2b482d0b3a4abca83779438a477344" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]965" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="78cec7548b0b426e9f637b2b24ae870e" Label="[UIModel]824ed723016148588abd6d52e1b438ed" Left="[float]40" Top="[float]100" Width="[float]200">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="90ca367c0ba349308a15780f5262e6b3" IsLabelBoundToChannel="[bool]False" Label="[UIModel]fa513e66ed794b8485fa0e9385bb84ec" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="897518a606404d82a9e65f324344d70c" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d2073489d4864607a3c46fe22ee6be47" Left="[float]20" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="1540a19a387e4005b1a5258c3c2d64fb" IsLabelBoundToChannel="[bool]False" Label="[UIModel]a981ee6dac1a4aec93bb2a74f15178ab" Left="[float]20" Top="[float]136" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="c43c5cabe1ed4e4788b3e1d9ae6a3222" IsLabelBoundToChannel="[bool]False" Label="[UIModel]5f19ff7a89cd4eff82133c074edb6f65" Left="[float]20" Top="[float]186" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="a7897bbe485648469b6130b8c752dc67" IsLabelBoundToChannel="[bool]False" Label="[UIModel]35c086ba15db4e929e11503a9b8febb2" Left="[float]20" Top="[float]236" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<Label Height="[float]16" Id="fa513e66ed794b8485fa0e9385bb84ec" LabelOwner="[UIModel]90ca367c0ba349308a15780f5262e6b3" Left="[float]20" Text="[string]Voltage level (V)" Top="[float]16" Width="[float]86" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="d2073489d4864607a3c46fe22ee6be47" LabelOwner="[UIModel]897518a606404d82a9e65f324344d70c" Left="[float]20" Text="[string]Current limit (A)" Top="[float]66" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="a981ee6dac1a4aec93bb2a74f15178ab" LabelOwner="[UIModel]1540a19a387e4005b1a5258c3c2d64fb" Left="[float]20" Text="[string]Voltage level range (V)" Top="[float]116" Width="[float]119" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="5f19ff7a89cd4eff82133c074edb6f65" LabelOwner="[UIModel]c43c5cabe1ed4e4788b3e1d9ae6a3222" Left="[float]20" Text="[string]Current limit range (A)" Top="[float]166" Width="[float]118" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="35c086ba15db4e929e11503a9b8febb2" LabelOwner="[UIModel]a7897bbe485648469b6130b8c752dc67" Left="[float]20" Text="[string]Source delay (s)" Top="[float]216" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="c8d1a85f127c4589b8b202590e896ea5" Label="[UIModel]80a851e3b2e541308f94ee31f938e656" Left="[float]280" Top="[float]100" Width="[float]200">
						<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]e4b098f6d28b499a94586b4638f610b5" BaseName="[string]Numeric Array Output" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Output/voltage_measurements" Columns="[int]1" Dimensions="[int]1" Height="[float]92" Id="efb8cf20b08f4658b0888399ca0f4a58" IndexVisibility="[Visibility]Collapsed" IsLabelBoundToChannel="[bool]False" Label="[UIModel]8dadc6c46e82465d8f8ecade5f6da695" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]3" Top="[float]36" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
							<p.DefaultElementValue>0x0</p.DefaultElementValue>
							<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="e4b098f6d28b499a94586b4638f610b5" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
						</ChannelArrayViewer>
						<Label Height="[float]16" Id="8dadc6c46e82465d8f8ecade5f6da695" LabelOwner="[UIModel]efb8cf20b08f4658b0888399ca0f4a58" Left="[float]20" Text="[string]Voltage measurements (V)" Top="[float]16" Width="[float]139" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]4b1f12b10b4446d589435dfd18a68927" BaseName="[string]Numeric Array Output" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Output/current_measurements" Columns="[int]1" Dimensions="[int]1" FirstIndex="[ArrayElementIndex]0" Height="[float]92" Id="675564c8a2c146f9a22469635eb36ef6" IndexVisibility="[Visibility]Collapsed" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3b5b186bdf7543ec90c98693a4304a09" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]3" Top="[float]171" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
							<p.DefaultElementValue>0x0</p.DefaultElementValue>
							<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="4b1f12b10b4446d589435dfd18a68927" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
						</ChannelArrayViewer>
						<Label Height="[float]16" Id="3b5b186bdf7543ec90c98693a4304a09" LabelOwner="[UIModel]675564c8a2c146f9a22469635eb36ef6" Left="[float]20" Text="[string]Current measurements (V)" Top="[float]151" Width="[float]139" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="824ed723016148588abd6d52e1b438ed" LabelOwner="[UIModel]78cec7548b0b426e9f637b2b24ae870e" Left="[float]40" Text="[string]Configuration" Top="[float]80" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
					<Label Height="[float]16" Id="80a851e3b2e541308f94ee31f938e656" LabelOwner="[UIModel]c8d1a85f127c4589b8b202590e896ea5" Left="[float]280" Text="[string]Results" Top="[float]80" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{58402dff-3d3e-4d33-9cc1-dee5a551e29c}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="40f69fa409284b3c8f6b35105d08c9a0" IsLabelBoundToChannel="[bool]False" Label="[UIModel]b57bec42023a446ebd251c991c08fb1e" Left="[float]40" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]36" Width="[float]200" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="b57bec42023a446ebd251c991c08fb1e" LabelOwner="[UIModel]40f69fa409284b3c8f6b35105d08c9a0" Left="[float]40" Text="[string]Pin name" Top="[float]16" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage_example.seq sha256=50caedc01cb1cf1e4cd1042a04e6e5effa1db1449667296e8c210c2fbda7aaf8 bytes=185700 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltage_example.seq`
- sha256: `50caedc01cb1cf1e4cd1042a04e6e5effa1db1449667296e8c210c2fbda7aaf8`
- bytes: 185700

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.1.0.49154' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN2&lt;dfASB`]CF^aUXa]Y\4WmD]203VfR;kS;KgdGgF285WU]RaSJgcjNlM7MFC4LiX=a48\7dW:L403mZ4BUAT82I&gt;KQH8\T8QFE`DA2\LAVbMD5YRMT13fTiE^i&lt;boIle7[=C_LeZbKM2QXhVTH;?4hTX]A[17:2T;Dh\^Co3kY9PA5QK23^C]l262h09La1?5^k3J0BQZ@@EeDRZTO=\cKd?XKjmGb1N\X&lt;J[IS9OXJj22Qc=R\WEEn\IKCaHCAUNi97;EVjaJCX4&gt;UU36B3oib::mkjjIJFOY^^C_gK;?Ngamc6b1^HOM^Rl@oHoiaG802US0o36;lHiif[]oe&lt;FRliGlo^CMk69OeFDNDnIQUXNS=iA3JmW&lt;KbcFOCL6bWF;DdY7d2\SSH4mB7[^9gAb5EgM5G;l^DR5mXURj&lt;_=4b_aTDS965fd7ACLdkeA7kamDL&gt;;lWi[PA07_B@&gt;cR[mGK`_XMGdK4NmjkVR8?micjQcMS=oX^9@cW^5\93S[[2ZkFbBiZ=Q@AM0FkKdo:gUd&lt;lVVcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX34oO2LYb;J&gt;k9nWLWBEg6Tk&gt;koggGTQ&gt;kL6kJL@dKQ2_E0Z</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWeomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^;g[CAF?o9BS9X&lt;V_06oLo]n`VOa[dMZmhLlJ^=?^T^nMbojKJkCSoWN4WIgV\ckgWCOWb7&gt;jno&gt;;[OS_oVacNOW7jg77?7OooD2OombloUnEI9_InB&lt;HI4[kZLf&lt;]bOKRmn::VQk1Tm`8F4;5W&gt;TA&lt;Kcd`aI[R8DKQka6aboN?k=I&gt;UJRNToCflBd:9=GW1XijhYcm92_e]^Rg?N[eOQO^9B&lt;2LjSQk=KKS8Eo?8kT9]m3^^fWPk?AQN^K4hZkc&lt;Vm&gt;gFc`@RgL^O5bET;[D_=R`WO?&gt;&gt;77S_K[1miPR@lgJ;?^^n6om3JliJgSBbAO&lt;J&gt;_7OGSQoU5Mo5ainP9oNj=DL&lt;NdI=^]VXFK0i[_\n0emoFJc]\=:4K&lt;HYHRl[4;=V_6SaC6ETl6dE1KV^E5NV9OgQBU&gt;n`WYOLgi&gt;S84nN^1mG5`SPC1]S:d;`B=4NjKmH&lt;UULW:0\;?2W8FOA:^K?M9TIFdMZj?UgUemK:5BfZf19WV&gt;o2K6[k;XS0HEj\8[[9QY;;_Z:UlBgN&gt;g897SGQPF^OS\Ba8&lt;Nl5AB?;oWBQ6aJP@1SQNGhXj:1DK9OHN&lt;6lGSkolg=dM`l2hG?AKRH2^5E7fbmmi:cJ2A056EVl9@Ll@B9;Ml6POPlacQAcKJf4N0AbVYZdLjl=5el2I6[[UbiSJdAiTCbBdeiYEk9g6Sa7[CFB8`Nkc\S4`dNB53K4Y@M`QAkbIdlgkPUJ??fmoGj]cMHcUoJH_X:heHfm2bQ96d\&gt;Y;:5diBn6JoC0O8DGdkT9VIPBjN^1cB`TcbjfVBJNQ[?b\onSkg@kON1onmnGNoOnYOo&gt;kc^Ofm]G7mB&gt;Qba^I&gt;6iVCm0GSnGTYgQ_Ig4AOR9MZMAk1Il1RgBV7TIAM`A=\k&lt;V4O9c?_3Y:O3l:dCYMk^gg;jl0L0CVKCUWH5`j7aeFkA[b&gt;CTQ95a^731VBF_IoV`TDggl4NO?G?^6Y3k&lt;P]4e7VRbee]]ZcM@Jf4&lt;;aWfGU&gt;9^:[`SDoKE?YZ:Vd8[TTU\cVW7EE&lt;cK2Y;_LD3MKjVT98S3E]O@NF=[GoXgC=`=OMNoZQ@@l2P:F[`T0:[LS53m:IMEkRTe@8gJE`&lt;]Y2:U`M8HkClI4_aPZN:4ZLOC2BoZFX8GCf8_I0;U^`[:e@:ILD&lt;808A]97NXjMJdHVK5&lt;6@ZRfV:AX6kPcgf@:31?M9dKQa?=RA:`f5TCI^bQLjbA?jYd&lt;_1^@Iek6[helE6RFL:EWA[cHLkB2l7QLeCBJX]0hDPWUWlCJ=:^m5gJjn&gt;SW9DRT1Q[Y5`gAf&lt;OdDdj1YNo:`NeELR3c2mU`G:e&gt;j8@]gAR?Ad48]8;:;&lt;S;EUJcjMiOVF1m50TbUD\Tl58jH?d\X8T^08T=W9[Z683aTA&gt;]W[5Oi5M?52E\:71[03U?V`4l_1WVH4j:GKI9hcEGRk3?_;k:;F_ej5SiN:WT:RF=Gmdl:=knc:UD^Hj9obj;AE\I7HC&gt;FB&gt;jYl8f56nJ&lt;UcI=fiN&lt;i;VXUJ55KE9jS9S_DR5N1k`PSNZVY0Z0iTYNej0?V_@UDHkL6Co5UCKBGPJYGR_Ti@1C@\A6TiIe;E\]e=ZZKd\ZVfURZTM50e8JQ[&lt;TMTUjFdJKR_9CXd\N38JN&gt;Q&gt;\UNF]@;FB8LQX@?dbU@[8mfDU3:S0dI&gt;?SmaPSHhfe6&lt;gV@A0JSZnmSECILX[AB98eHXQ9`R?5E3I6[4N=mYUREb_5jZURE5lhN6VZ\P`:`^;AQONF8O:Plbm4XSolW7VZN&lt;?OL8@0JK^m:5oh&lt;AR[a:BRlMniCM&lt;Q^\X\Nkg7G3ZMAi7nm:9PFFe3mCA1\]DY\Df;6aG&lt;iI]h2G6MG`BA\[I]008f:U6XXSNH2jcIXFSGI5Q2bBEKA`&lt;X]h_:@RfNklLbR7Sji9F_895&lt;R=Q572IULj=^noMWZiZ`ddKH`@`He:jliNb34YNl9[QT6cAlE&lt;6LflQ9e?nUMDFlcJBlA3?PP6fSobc@Of_fBSccJNY=&gt;?N3lZRDPO[EVgdA&lt;FBDB`XE&lt;^e]0&lt;&gt;VkM0OT@X&gt;YTBh&lt;5IL&lt;3?]`D2\9TbD=P9XH933VJR1BePO?6H6&lt;2;Rb:@82Hbj[IF&gt;5Pl5;dH0QG4:@48T&lt;39AjLjU172J17:JNl=j0P6NHX8U6RT@@_R0PglmF;;HX\i:jV^ULZBDKEBVfUTf9YQgX[9IDjjfT&gt;:iY`4VU&gt;jmJ&gt;^lE2G:UodJJ0?kJBH?eL@[95RbKJUIOlaNeJ04aJ?]A4YMiXMjb8EdSS:FQ@7jO^6V2_52W:f:]&lt;6e5Cd?=1I1S`LR^aZ9L?2:i8gKEhKfCL5bbPaMloUSe;o9aiAW[oE2DcNMo=]V3VZ3j=;eK0o5HDY[@\W;=e@Vl8XLFANQC9E&gt;QSA=CQY79hkh3K&lt;7T?;nR9;Z6LT?Nc&gt;S&lt;VnOhN&gt;A7dhl]K:oLi0N`lo`P8XYbiZhgEiMHkPY4;7?ho]9J`Z9g^0o=n=LSnOn?ieOB64nHAQFTK8PM_MC[JSeR8@G2bZIEdgH&lt;RZ;OM]&gt;@_LW:9G&lt;i8_M&lt;G0iefC[hgQ3@MR?7jB\Tc1Tf;FbZLgF5X3L[[i7=`i99aTj6Bf9hoc4f&gt;K\mAKJU5HVOhmaTQmdX?THaTcA20&lt;o\eFYJL5Fl`OaV0Lg^m=dM8dKEXZbi_aM`N4iNOTmgWYL3]hN6L7iae8^GXbD:O\Y6CH3&gt;KSj1^`C4a]&gt;WQ7OESNDVeoS81il`C&lt;lI\h;BR2o8`kOIUYaC_UM6UhYa5^:Vn4Tg@DYb3U\b\fAFX]aIIO3S\LG^&lt;VA[9&lt;di1?XH4d]PXFb[&lt;mS6WM1H7n4QOPX3V8JcaJ3Bc2f`3kS9^djl1&lt;NFQDkA93Ufmf&lt;amc=`80X1e3HkQ:L]YabEBD05fi1W2^:CkBEDcH^&lt;iZ;L:\8jH][;VZj4R5VRdB6F7g=a:g99Z[d9NoQ89XZfYU6Ej\lMNK`GXE8]&gt;kb1[e?Qc4mH:lRM9\OK7F\j_JGQ2X&lt;8nV91\\ReIUTd4;L6nZ4o7O&gt;5To5e:L?2S2kY98YfOPONej0UZd28\R5Kk_&gt;WnN^DH2Ra&gt;8JPmDGUT4BS3E6S6N6PXQ^o?DU4hlJ1V&gt;V1L?:__=@EIUOn9X7KR2Lo=2KmV9A8=\\T\C=1?n1D=@?IkA\=f2ii0CCN:&lt;9RPOFL`NU8DSQ&lt;`;_2&lt;nB]=6e51SI8613fMTW3Oj[L^R]8&gt;Pi:a`A2D=\4K&gt;il^UBR7P9]^G5NXA2^X7951G[YT\OKLGG4l=UQn;H7@B;8&gt;da:ibOD[XBR`]o&gt;VZ6DOCdK3AP?3A_33UbkQTneQOg=b`jYf;]h]AolQHPG^On43=0kIj9]cNR^:eSCY@7J3d:fE\We:Vb01HQD:H^8XDCNhWA\A:WD1Gl3&lt;U7dkK=5DgXUKgD\cnF6@[17\Fk=:4E@TUiP?Fl@0i9ZoM2bEb`155W4J=3T3DML1\aF:FfPQ_KUbIc:4Ya3JFAmR\aJMI0a[C4^ef5m^Fi4&gt;XZHB6?JU:=DZ87J56eH&gt;DmEMhP4D2oO3SJP&gt;1jMO2&lt;naOX3XeHoDCM;;J:PJlY8lXGAERILBl6Ze45f=C_H1EH@IjHR`mDHLk&gt;RloAEY7C[?GIk&gt;fJcE8?]mNG9gjfLehW\mLW]iM[?]hJNCWK\EIR0P]hk6`E4NUFW`L?jP9&lt;3@in]\&gt;b[aNQRj1@R1@lHWUO7cje0A&gt;LK;JhC[BgiI]\2@eSX:;QfRU@U&gt;]@_lm`4NmBZ\:ZoSFUb?TlhO5;?&gt;B1H?gA7=g=C1ji=292Ke0J\FnE9DeX&gt;CIC;iJ0Q`DXj&gt;W\&lt;PEOYPYk5m[A0\aN8N8UXTPGU[n]bW5n:`?nZlnnf\Imkoebbigkc`ofP\eP3l@ZOUX`?B@DZR_DX[^jV=gj=d1Ym4Z&lt;ob`?C`SLo9T5_eOKONeoF]7?koVKmXXP&gt;@mOLEB_KIcmYAEE:TPO\X\:IW;;f\GU_9nGfb7gkm2FX@_m\=LZKGW]]fQbgkjIKFn:Z?7OkIIKJ[SO\hURRIoOHS?5Im13fdEU3GX6A:fkd1W=WEW;WIRW;nf8PFKmj0I6c\Ol161GZUA]d;MJ:ZYK=VEA5\=d;6WchfDOoda;nMHPO^dHdLa@nRM@8^2Oa`S?HXLF4nDR@[gd@3ZWg?=HDeoV\ekeE:jne_Z_g?4HH]X`?HL\fA&gt;3IiNAk6W1m3G0_2TCL=LYO`T`_HK@l\3K6f3=3kY61mh3P6N;k6W1m37PK&lt;`\K6`f=3Y6;mn30n@QPPL_O`T`_HNXdTNm3PcB7f3=3k]61F3f^\2K6J51o9_dONJi[aZ=PgGoQ_YlegmNBlj]Mg1Y9kjW]mhcf\AE?5N[_l]E?eCjcMOO`&gt;NKk6j1FegWdiGIk&gt;gJcF[NcfKLeBjFNcffLFL[]in=6bC_H8^oNbA_H\`Ig&lt;[Zjc\IO`GPnSnRYk245=G437EhljgHLTJJgAIlMMmTC]5Ofg3k7l1=okWM^WiPP\Tb&lt;_gjXVbPjlMb^O2?7g2GoojlSJ\BolCmm&lt;eolmTbca0HGIPS7WELFBRNnUKon6]o_boQc4&lt;O7WakMAfZ1;@;]BVhfZ6d;A]\Y;]^C\2JNWl@EDkjHUD]8Gj3k:Gg9M]64UVIhV`0kFZjnXDXH9Ul?3UgC&lt;4E`da=l&lt;6aYaK?YSB&lt;ZlK8AkLXPga:L6Y9WXb^R2:;XfCCXg46QgO@OonCH=04lnD]G?@JU0oW&gt;8R[cd5WUn`Lj&gt;_L4H7acI]&lt;]SYiCVkXMEcP^ab7Tf\&lt;L36cdmoD7?&gt;U&gt;FXnG58NQBfkE`&gt;Y&gt;ZXN^;LUDk^0CT`]]YcV503o2&lt;9aY76Tb5=h;3n^l@;GR:DEml&lt;HjcCj]?2BHSYcAH8LcPLdmXLfl9&lt;R?P&gt;m[d_OAF47OMiiSBYLBDIO:B2mBEQejeLI1_lDOkc^TPmOSR;N?RhN=R3X@`aEX13VmJG`^nJRDXYeb7QSJiLJ`NX5Qkf=]imm&gt;nKg_CV6OK]RK94GkTDXQ&gt;HaT13fb00I9PG6JX1RmPQA@CXT2Ci9A4;\8804oTS3&gt;9F@3jQ0Q`Yb6PH2J8=QIl&lt;U65fY12^T^l2@8TQ51B^@UA:oVP&lt;O1`X1PnPjXO0`P3GQkdBQm:cV001le`9l2VYAPg8&lt;0k8Bm6`QjeP@j2ciUhWLj@0LY?3AP784;S@YWHX1S?Qn1m1kHbJS6f811fJb&lt;=99l6:nE1PPJ=8l=&lt;a\P0dAX0LXTD&gt;iH&lt;5QR6^dF;Bab60@I1@Q0HZS?9?A@TRA`J1PHiRc:Q:_jX1GeY=N[B&lt;3V2Pd60J^Y3@[1hD0XF2MP;&lt;B3RX2_H4PG43R;`1ZV@8E0R&lt;KHgh4VHe2B0H4:Y&lt;H5&lt;Q723C@d@1WBS^63LMX3=h4n91c3XeS;4aDhDR99PE40@14SA4S8Z_QlfJ^kenOQMQl\MFkQ32aVj``BUAmNDAB3?\R55J4A\37PAhR]3=KA6W&lt;86890Ck1NP@_[g:D6dV4Q49fS?IJ_C2;S^7mbE9SkO2G9Ii^ggHKkT`F370_j7b?jkWkEQ]:?XVf6A2ilo3@QYRZ82LV4K6^KABIXe``g6B7e1HCJK8hP9k^0X&gt;O;4j2^RRM3c2=aH8f`YUfUlb`B&lt;3I37=]e&gt;@JZ?KI:?@GJMZ]DOXZDNYX\cVFBbZ1RmDIF82=NNZDMK0dibVYa6E8b@nBP&lt;5Tl&lt;05lIDYhX^b6F\?\XfTjW:PUgjFJNIm\aeD&lt;eoRAhT`S]9IT7:LUghEY&gt;2fJODYDMFWDNBTdof=ITOaPAL59FVSX7NGk\MRM]DU&gt;&lt;nm39CJKab2S9fP&gt;SbRPR`h&lt;R0@D@5P9ZV08\FAR=6B[D?`iF9Xa6Q9e:U\ARX=B]93S4;17PliCP_8N5h`&gt;i6V3&gt;38TciG@Te@WT`HL8`hPj;\D6gSlTdaAYJMc8Hiaf&gt;[[@NAUBeHhFNTm7NYnXia&gt;:JBgQ?oS?;U9jT\\=AYoUTMCT\81ZYRXNJb\lbEEL&gt;e79ib&gt;:2`]U2jToCY]80BfV:4``\X1a4BL&lt;9?9ATRQ4bcK7^1A4RoX@7_2@S;hfe90M;0D;DJ]?I]5@0Y`&gt;NV3LF5`I1LYCFZTJU@=fTdVb2IPfC6dDZZ8JGTc2QOh;^L8HnSlnS?YbH5TGiYN5i9a8XWVIV]cK^:A]LH[5Lm2L34ZfLDn&lt;hgf2IHQJV6o[CK&gt;:33MOAcD5k&gt;LcEW&lt;&gt;D1CTFD^e69IAD3mLk&gt;C56YaKeFci;[THhLnK]V7iaZ:O5@PcUHH0f];^:5a0o2@FhcUKMQ5D&gt;nJn?Ija2clJo0KQ0:6Z&lt;7KD=:2I^YmJGE@ELPHG[9N\9mCc046gh\;[KBUd_I=RJbRBo&gt;kD8\BUXbUB8c&lt;]fF[BViXJSLNm=oWLlRY</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
										<PinMapId classname='Str'>
											<value/>
										</PinMapId>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Source DC voltage and measure voltage/current'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:1m8fotxw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIDCPowerSourceDCVoltage_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[10]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>{"Pin1"}</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_level</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_level_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_limit</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_limit_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>5</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>source_delay</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>6</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>measurement_sites</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeInt32</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>measurement_pin_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_measurements</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_measurements</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>in_compliance</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeBool</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>5</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:v3cHTx+U7hGhw2DjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>"NIDCPowerSourceDCVoltage.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DCPower Sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:c5USoqlx7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidcpower.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nidcpower_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DCPower sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:syCDFOVw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidcpower.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nidcpower_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltageMultiSite.pinmap sha256=3a6f63d827c2879a325facd19d187f659b4b958b33225ec7d63ab72501d93d3b bytes=1089 -->
## FILE: examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltageMultiSite.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/NIDCPowerSourceDCVoltageMultiSite.pinmap`
- sha256: `3a6f63d827c2879a325facd19d187f659b4b958b33225ec7d63ab72501d93d3b`
- bytes: 1089

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="ChannelGroup1" channels="0" />
			<ChannelGroup name="ChannelGroup2" channels="1" />
			<ChannelGroup name="ChannelGroup3" channels="2" />
			<ChannelGroup name="ChannelGroup4" channels="3" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin1" siteNumber="1" instrument="DCPower1" channel="1" />
		<Connection pin="Pin1" siteNumber="2" instrument="DCPower1" channel="2" />
		<Connection pin="Pin1" siteNumber="3" instrument="DCPower1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nidcpower_source_dc_voltage/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/pyproject.toml sha256=7327e3a69aa3edd14fd15839d65a7c972c3a984e202cf14e8694c79ec60d5f6b bytes=1139 -->
## FILE: examples/nidcpower_source_dc_voltage/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/pyproject.toml`
- sha256: `7327e3a69aa3edd14fd15839d65a7c972c3a984e202cf14e8694c79ec60d5f6b`
- bytes: 1139

````toml
[tool.poetry]
name = "nidcpower_source_dc_voltage"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that sources and measures a DC voltage with an NI SMU."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nidcpower = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidcpower = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nidcpower", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "hightime.*",
    "nidcpower.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/README.md sha256=ec3fdd36858e64e2382b58f867467862745b312586b3b96c2b00cd3a5dcab914 bytes=2558 -->
## FILE: examples/nidcpower_source_dc_voltage/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/README.md`
- sha256: `ec3fdd36858e64e2382b58f867467862745b312586b3b96c2b00cd3a5dcab914`
- bytes: 2558

````markdown
## NI-DCPower Source DC Voltage

This is a measurement plug-in example that sources and measures a DC voltage with an
NI SMU.

### Features

- Uses the `nidcpower` package to access NI-DCPower from Python
- Demonstrates how to cancel a running measurement by breaking a long wait into
  multiple short waits
- Pin-aware, supporting multiple sessions, multiple pins, and multiple selected
  sites
  - Sources the same DC voltage level on all selected pin/site combinations
  - Measures the DC voltage and current for each selected pin/site combination
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes multiple UI files. Note: InstrumentStudio only displays the 1st UI
  file. To change the UI file used for the example, simply switch the order of
  the `ui_file_paths` array in `measurement.py`
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
    session registration and unregistration in the `Setup` and `Cleanup`
    sections of the main sequence. For **Test UUTs** and batch process model use
    cases, these steps should be moved to the `ProcessSetup` and
    `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-DCPower
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI SMU that is supported by NI-DCPower (e.g.
PXIe-4141).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string:

  ```
  MEASUREMENT_PLUGIN_NIDCPOWER_SIMULATE=1
  MEASUREMENT_PLUGIN_NIDCPOWER_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIDCPOWER_MODEL=4141
  ```

> **Note**
>
> The multi-site pin map, `NIDCPowerSourceDCVoltageMultiSite.pinmap`, requires
> an NI SMU with 4 or more channels.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nidcpower_source_dc_voltage/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/teststand_nidcpower.py sha256=c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea bytes=2623 -->
## FILE: examples/nidcpower_source_dc_voltage/teststand_nidcpower.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage/teststand_nidcpower.py`
- sha256: `c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea`
- bytes: 2623

````python
"""Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DCPOWER,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidcpower_sessions(sequence_context: Any) -> None:
    """Create and register all NI-DCPower sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_sessions(
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER
        ) as reservation:
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nidcpower_sessions() -> None:
    """Destroy and unregister all NI-DCPower sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/measurement.py sha256=7f6b31aa4f8d7009f00aea013e757dba7690563f426cfad3ee7d7e8ef3ee3212 bytes=6834 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/measurement.py`
- sha256: `7f6b31aa4f8d7009f00aea013e757dba7690563f426cfad3ee7d7e8ef3ee3212`
- bytes: 6834

````python
"""Source and measure a DC voltage with an NI SMU via an NI-SWITCH multiplexer."""

from __future__ import annotations

import logging
import pathlib
import sys
import threading
import time
from typing import TYPE_CHECKING, NamedTuple

import click
import grpc
import hightime
import ni_measurement_plugin_sdk_service as nims
import nidcpower
import nidcpower.session
import niswitch.session
from _helpers import configure_logging, verbosity_option

_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059
_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933
_NIDCPOWER_TIMEOUT_ERROR_CODES = [
    _NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE,
    _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE,
]

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDCPowerSourceDCVoltageWithMultiplexer.serviceconfig",
    ui_file_paths=[service_directory / "NIDCPowerSourceDCVoltageWithMultiplexer.measui"],
)

if TYPE_CHECKING:
    # The nidcpower Measurement named tuple doesn't support type annotations:
    # https://github.com/ni/nimi-python/issues/1885
    class _Measurement(NamedTuple):
        voltage: float
        current: float
        in_compliance: bool
        channel: str


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_name",
    nims.DataType.IOResource,
    "Pin1",
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DCPOWER,
)
@measurement_service.configuration("voltage_level", nims.DataType.Double, 6.0)
@measurement_service.configuration("voltage_level_range", nims.DataType.Double, 6.0)
@measurement_service.configuration("current_limit", nims.DataType.Double, 0.01)
@measurement_service.configuration("current_limit_range", nims.DataType.Double, 0.01)
@measurement_service.configuration("source_delay", nims.DataType.Double, 0.0)
@measurement_service.output("voltage_measurement", nims.DataType.Double)
@measurement_service.output("current_measurement", nims.DataType.Double)
def measure(
    pin_name: str,
    voltage_level: float,
    voltage_level_range: float,
    current_limit: float,
    current_limit_range: float,
    source_delay: float,
) -> tuple[float, float]:
    """Source and measure a DC voltage with an NI SMU connected via an NI-SWITCH multiplexer."""
    logging.info("Executing measurement: pin_name=%s voltage_level=%g", pin_name, voltage_level)

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    with measurement_service.context.reserve_session(pin_name) as reservation:
        with reservation.initialize_nidcpower_session(), reservation.initialize_niswitch_multiplexer_session():
            # Configure the SMU channel connected to the input pin.
            connection = reservation.get_nidcpower_connection_with_multiplexer(
                niswitch.Session, pin_name
            )
            source_channel = connection.session.channels[connection.channel_name]
            source_channel.source_mode = nidcpower.SourceMode.SINGLE_POINT
            source_channel.output_function = nidcpower.OutputFunction.DC_VOLTAGE
            source_channel.current_limit = current_limit
            source_channel.voltage_level_range = voltage_level_range
            source_channel.current_limit_range = current_limit_range
            source_channel.source_delay = hightime.timedelta(seconds=source_delay)
            source_channel.voltage_level = voltage_level

            # Connect the route in the NI-SWITCH multiplexer for the pin.
            connection.multiplexer_session.connect_multiple(connection.multiplexer_route)
            connection.multiplexer_session.wait_for_debounce()

            # Initiate the channels to start sourcing the outputs. initiate()
            # returns a context manager that aborts the measurement when the
            # function returns or raises an exception.
            with source_channel.initiate():
                # Wait for the outputs to settle.
                timeout = source_delay + 10.0
                _wait_for_nidcpower_event(
                    source_channel,
                    cancellation_event,
                    nidcpower.enums.Event.SOURCE_COMPLETE,
                    timeout,
                )

                measurement: _Measurement = source_channel.measure_multiple()[0]

            # Reset the channel to a known state
            source_channel.reset()

            # Disconnect the connected route.
            connection.multiplexer_session.disconnect_multiple(connection.multiplexer_route)
            connection.multiplexer_session.wait_for_debounce()

    logging.info(
        "Completed measurement measured voltage=%g measured current=%g",
        measurement.voltage,
        measurement.current,
    )
    return (
        measurement.voltage,
        measurement.current,
    )


def _wait_for_nidcpower_event(
    channels: nidcpower.session._SessionBase,
    cancellation_event: threading.Event,
    event_id: nidcpower.enums.Event,
    timeout: float,
) -> None:
    """Wait for a NI-DCPower event or until error/cancellation occurs."""
    grpc_deadline = time.time() + measurement_service.context.time_remaining
    user_deadline = time.time() + timeout

    while True:
        if time.time() > user_deadline:
            raise TimeoutError("User timeout expired.")
        if time.time() > grpc_deadline:
            measurement_service.context.abort(
                grpc.StatusCode.DEADLINE_EXCEEDED, "Deadline exceeded."
            )
        if cancellation_event.is_set():
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

        # Wait for the NI-DCPower event. If this takes more than 100 ms, check
        # whether the measurement was canceled and try again. NI-DCPower does
        # not support canceling a call to wait_for_event().
        try:
            channels.wait_for_event(event_id, timeout=100e-3)
            break
        except nidcpower.errors.DriverError as e:
            if e.code in _NIDCPOWER_TIMEOUT_ERROR_CODES:
                pass
            raise


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Source and measure a DC voltage with an NI SMU connected via an NI-SWITCH multiplexer."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.instudioproj sha256=11ffb93ed9868ee5aca7ea9ae2ad54808ef473ec59c29f585a5cd85eec87cf5b bytes=2108 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.instudioproj`
- sha256: `11ffb93ed9868ee5aca7ea9ae2ad54808ef473ec59c29f585a5cd85eec87cf5b`
- bytes: 2108

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="0943E9837233DF81A4783AC589C563F712B9AB511BBFE0A4F2544AD9A69F975A6D349FA0DA165B8F09FC80C12D52F7B906FF254B222C88AEA1688B0FCF98326B" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="24.0.0.49505" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49505" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.0.0.49505" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="f36fcf6fc964442d80b0def5bafff9e3" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltageWithMultiplexer.pinmap" StoragePath="NIDCPowerSourceDCVoltageWithMultiplexer.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="c815b74408b54dd08baf8b974710297f" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIDCPowerSourceDCVoltageWithMultiplexer.sfp" StoragePath="NIDCPowerSourceDCVoltageWithMultiplexer.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measproj sha256=1299ce0ec2e0183b23bcd55ed2447fbc1b52874ba6e2a88123be07c8fb5298a7 bytes=3903 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measproj`
- sha256: `1299ce0ec2e0183b23bcd55ed2447fbc1b52874ba6e2a88123be07c8fb5298a7`
- bytes: 3903

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="A59872EAEF9C535B9328AA0D9B48D1D054BC2BDD2383853392C40074B8FF0F6757676376998CCCADBC6B28180EE1EB0B79F668F8967F676393EB1F89519B051B" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49428" Name="MeasurementLink UI Editor" Version="24.0.0.49428" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="fbc7425437e74709a87389750d4ee99c" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="3465fdfd72c44abaad0599621bd6c6f9" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="680a32f2c4b248a4a615cf8eeaffee0e" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="5512fcab475b463488357fb0d38af2e8" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="875ab222a6a348baa083d8ac871eed14" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="d90a253c17d546b9a38926745fad77e8" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="9cc9e23567d4c3cbe6a91cfaa10b772" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="cce43756a09e455ca4a22e97b9903eac" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="ddfe85c7feb34c34ae3a5c7b958ed764" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="25f25c7dd8a48e4846a48452fa47c09" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="7c869e6a42a8474d86779ed686991145" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIDCPowerSourceDCVoltageWithMultiplexer.measui" StoragePath="NIDCPowerSourceDCVoltageWithMultiplexer.measui" />
			<FileReference Id="4bacc157c73d4873a743b1a055f4db93" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDCPowerSourceDCVoltageWithMultiplexer.pinmap" StoragePath="NIDCPowerSourceDCVoltageWithMultiplexer.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measui sha256=cd1aebf0cb67b55ac4ebab4929436fc6d42fb6f2df91cb06a9bbabad77020519 bytes=9109 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.measui`
- sha256: `cd1aebf0cb67b55ac4ebab4929436fc6d42fb6f2df91cb06a9bbabad77020519`
- bytes: 9109

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D1BA922D570356EA749A6ED6DF9A50541FE44CA3DDB860964B3BA4A6ED23EF96DFBDA50FE95D39641BAA674D9C9E43C9D35BC2EEEDC4CD1E99415ED181E73C09" Timestamp="1DA69602A755916" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49428" Name="MeasurementLink UI Editor" Version="24.0.0.49428" />
	</SourceModelFeatureSet>
	<Screen ClientId="{5f88d1ec-4b12-4bf9-b28f-707b534a0575}" DisplayName="NI-DCPower Source DC Voltage With Multiplexer (Py)" Id="ce8cc70d4b0b487db029384b996c0e8a" ServiceClass="ni.examples.NIDCPowerSourceDCVoltageWithMultiplexer_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]519" Id="1224789d85bd4cdfa59e83e724ab737e" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]1007" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="4b93ed01d79049dc8d2c3ef426384b35" Label="[UIModel]2f53b6c7f87b41879b8d84f4fb87c844" Left="[float]40" Top="[float]100" Width="[float]200">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="53ab9fe640e341c9b5aa585471c4663a" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d1dfd1838e5a4868b62e7cdf74391ee8" Left="[float]20" TabIndex="[int]0" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="7b7ddd28c1b44bd28cfbc5dc5341cef6" IsLabelBoundToChannel="[bool]False" Label="[UIModel]cfd32e3f5ee34b34a17ce4b52396c18b" Left="[float]20" TabIndex="[int]1" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="daf74d9eb82c4002bdbb9a9bfa6c4de1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]a6828bc2eff448d7ac8a62a35d6f7e58" Left="[float]20" TabIndex="[int]2" Top="[float]136" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="7440e0cbaa914daf82d80ba5f43ba2b2" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7fdce012e2a44ac4b5370b7ddcb210cb" Left="[float]20" TabIndex="[int]3" Top="[float]186" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="47497842bba8443594fb99159509f596" IsLabelBoundToChannel="[bool]False" Label="[UIModel]8180acb567174824aa1b4126e857ad96" Left="[float]20" TabIndex="[int]4" Top="[float]236" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<Label Height="[float]16" Id="d1dfd1838e5a4868b62e7cdf74391ee8" LabelOwner="[UIModel]53ab9fe640e341c9b5aa585471c4663a" Left="[float]20" Text="[string]Voltage level (V)" Top="[float]16" Width="[float]87" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="cfd32e3f5ee34b34a17ce4b52396c18b" LabelOwner="[UIModel]7b7ddd28c1b44bd28cfbc5dc5341cef6" Left="[float]20" Text="[string]Current limit (A)" Top="[float]66" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="a6828bc2eff448d7ac8a62a35d6f7e58" LabelOwner="[UIModel]daf74d9eb82c4002bdbb9a9bfa6c4de1" Left="[float]20" Text="[string]Voltage level range (V)" Top="[float]116" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="7fdce012e2a44ac4b5370b7ddcb210cb" LabelOwner="[UIModel]7440e0cbaa914daf82d80ba5f43ba2b2" Left="[float]20" Text="[string]Current limit range (A)" Top="[float]166" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="8180acb567174824aa1b4126e857ad96" LabelOwner="[UIModel]47497842bba8443594fb99159509f596" Left="[float]20" Text="[string]Source delay (s)" Top="[float]216" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="2f53b6c7f87b41879b8d84f4fb87c844" LabelOwner="[UIModel]4b93ed01d79049dc8d2c3ef426384b35" Left="[float]40" Text="[string]Configuration" Top="[float]80" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="40b7c7768512477fb2d939ac81f1bb10" IsLabelBoundToChannel="[bool]False" Label="[UIModel]2104dc3428074997846caee906febdd6" Left="[float]40" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]36" Width="[float]200" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="2104dc3428074997846caee906febdd6" LabelOwner="[UIModel]40b7c7768512477fb2d939ac81f1bb10" Left="[float]40" Text="[string]Pin name" Top="[float]16" Width="[float]50" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]140" Id="4b84220d7ef9408998da8e4d1419e910" Label="[UIModel]f07f22cdda40412ebac20356285fadcf" Left="[float]270" Top="[float]100" Width="[float]200">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Output/voltage_measurement" Height="[float]24" Id="56509ae3afc0439195af8dcd7bb18d8e" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]9ed249b2dff8443ea212450b659c555b" Left="[float]22" TabIndex="[int]0" Top="[float]38" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="9ed249b2dff8443ea212450b659c555b" LabelOwner="[UIModel]56509ae3afc0439195af8dcd7bb18d8e" Left="[float]22" Text="[string]Voltage measurement (V)" Top="[float]18" Width="[float]135" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{5f88d1ec-4b12-4bf9-b28f-707b534a0575}/Output/current_measurement" Height="[float]24" Id="e1adbb848f114b8ea756362db8ccb954" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]2141adc5d274440b9f9cffc6dcecda67" Left="[float]22" TabIndex="[int]1" Top="[float]93" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="2141adc5d274440b9f9cffc6dcecda67" LabelOwner="[UIModel]e1adbb848f114b8ea756362db8ccb954" Left="[float]22" Text="[string]Current measurement (A)" Top="[float]73" Width="[float]135" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="f07f22cdda40412ebac20356285fadcf" LabelOwner="[UIModel]4b84220d7ef9408998da8e4d1419e910" Left="[float]270" Text="[string]Results" Top="[float]80" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.pinmap sha256=888826b446fa0e006ee856c720025b8ee933a6bf0c9cad99e2065b39e0c1d45d bytes=910 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.pinmap`
- sha256: `888826b446fa0e006ee856c720025b8ee933a6bf0c9cad99e2065b39e0c1d45d`
- bytes: 910

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<Multiplexer name="SWITCH1" multiplexerTypeId="" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<MultiplexedConnection instrument="DCPower1" channel="0">
			<MultiplexedDUTPinRoute pin="Pin1" siteNumber="0" multiplexer="SWITCH1" routeName="b0c0-&gt;b0r0" />
			<MultiplexedDUTPinRoute pin="Pin2" siteNumber="0" multiplexer="SWITCH1" routeName="b0c0-&gt;b0r1" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.serviceconfig sha256=16f5b4dcd07c194b080a5d676a4d6fc6a57650b3710595910d920f05fd75ad88 bytes=757 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.serviceconfig`
- sha256: `16f5b4dcd07c194b080a5d676a4d6fc6a57650b3710595910d920f05fd75ad88`
- bytes: 757

````json
{
  "services": [
    {
      "displayName": "NI-DCPower Source DC Voltage With Multiplexer (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIDCPowerSourceDCVoltageWithMultiplexer_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that sources and measures a DC voltage with an NI SMU via an NI-SWITCH multiplexer.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.sfp sha256=7af5aa5d3d8542bf3129f56b5d572c32e3bc6adc10433f0610e2e148e7fbd20e bytes=12342 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer.sfp`
- sha256: `7af5aa5d3d8542bf3129f56b5d572c32e3bc6adc10433f0610e2e148e7fbd20e`
- bytes: 12342

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E38A023EC8F270BBF7B6EAA791F9765A7C4529ACA71953F62C792B99058FDB39F16046DDF4B5B3D641955486E1207D1BBC31B9D3F8599B0B1A37085DB5FB7A87" Timestamp="1DA696214210992" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49505" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49505" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.0.0.49505" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="438fbd161b8e4c40aa13023ee84128ee" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:24.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-DCPower Source DC Voltage With Multiplexer (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-DCPower Source DC Voltage With Multiplexer (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;NI.Examples&quot;,&quot;Panel Type&quot;:&quot;NI-DCPower Source DC Voltage With Multiplexer (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIDCPowerSourceDCVoltageWithMultiplexer_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:24.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="90896b06682243a7942a2e0acbad79c3" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="61360b88731b4d939f655b90f1c26b0e" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="9312e256239944ffa32c614540014899" Name="NIDCPowerSourceDCVoltageWithMultiplexer.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="a81350c5b4c44248999e0038a07829e2" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{9410ca5a-4136-4c0c-823c-a1df1a26a17a}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v2.MeasurementConfigurations&quot;,&quot;pinName&quot;:&quot;Pin1&quot;,&quot;voltageLevel&quot;:6.0,&quot;voltageLevelRange&quot;:6.0,&quot;currentLimit&quot;:0.01,&quot;currentLimitRange&quot;:0.01,&quot;sourceDelay&quot;:0.0}" DisplayName="NI-DCPower Source DC Voltage With Multiplexer (Py)" Id="ca31b76bd31940c1be685e494537ebe9" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIDCPowerSourceDCVoltageWithMultiplexer_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]519" Id="18e3e67ef75147eda746f07d0de0745a" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]1007" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]280" Id="74469a6786414a87ae53e0354a42326f" Label="[UIModel]1bcc86ef31b741158ab498aa2e8123be" Left="[float]40" Top="[float]100" Width="[float]200">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="d63b70f2e61248efa09e4d3e3cc7deb5" IsLabelBoundToChannel="[bool]False" Label="[UIModel]8b22a1eba4894d7c8244877bb82f6553" Left="[float]20" TabIndex="[int]0" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="6f229e7b4c414e48aeba8647e1a13546" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7024ce9aaa1845f1b58a17b80647208b" Left="[float]20" TabIndex="[int]1" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="e145dec6ab544868ab9f9724d66b2d78" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3bbf7af9325f4b048b4fd168f8c39de0" Left="[float]20" TabIndex="[int]2" Top="[float]136" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="80eb3b98a9b042978ec43adb4e74520e" IsLabelBoundToChannel="[bool]False" Label="[UIModel]4e869ed9a1b74426bcad3df5721262fe" Left="[float]20" TabIndex="[int]3" Top="[float]186" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="cd01f9b3986548b5af2488ac9800bfb5" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9a8f5d5e43684ae2a1603bc77a96e368" Left="[float]20" TabIndex="[int]4" Top="[float]236" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<Label Height="[float]16" Id="8b22a1eba4894d7c8244877bb82f6553" LabelOwner="[UIModel]d63b70f2e61248efa09e4d3e3cc7deb5" Left="[float]20" Text="[string]Voltage level (V)" Top="[float]16" Width="[float]87" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="7024ce9aaa1845f1b58a17b80647208b" LabelOwner="[UIModel]6f229e7b4c414e48aeba8647e1a13546" Left="[float]20" Text="[string]Current limit (A)" Top="[float]66" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="3bbf7af9325f4b048b4fd168f8c39de0" LabelOwner="[UIModel]e145dec6ab544868ab9f9724d66b2d78" Left="[float]20" Text="[string]Voltage level range (V)" Top="[float]116" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="4e869ed9a1b74426bcad3df5721262fe" LabelOwner="[UIModel]80eb3b98a9b042978ec43adb4e74520e" Left="[float]20" Text="[string]Current limit range (A)" Top="[float]166" Width="[float]120" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="9a8f5d5e43684ae2a1603bc77a96e368" LabelOwner="[UIModel]cd01f9b3986548b5af2488ac9800bfb5" Left="[float]20" Text="[string]Source delay (s)" Top="[float]216" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="1bcc86ef31b741158ab498aa2e8123be" LabelOwner="[UIModel]74469a6786414a87ae53e0354a42326f" Left="[float]40" Text="[string]Configuration" Top="[float]80" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="d046d1269255403092bb0d178a7a39ed" IsLabelBoundToChannel="[bool]False" Label="[UIModel]83276825f5324e94ac92f0338d361cb8" Left="[float]40" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]36" Width="[float]200" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="83276825f5324e94ac92f0338d361cb8" LabelOwner="[UIModel]d046d1269255403092bb0d178a7a39ed" Left="[float]40" Text="[string]Pin name" Top="[float]16" Width="[float]50" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]140" Id="e5b036d2df8446b3803be101786b5500" Label="[UIModel]f742e6704654462e98a822de01f10264" Left="[float]270" Top="[float]100" Width="[float]200">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Output/voltage_measurement" Height="[float]24" Id="47fd340ed784f55b6a5bd3a9c1a3cf0" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]2ebe3305711d4f499831ae05b6788962" Left="[float]22" TabIndex="[int]0" Top="[float]38" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="2ebe3305711d4f499831ae05b6788962" LabelOwner="[UIModel]47fd340ed784f55b6a5bd3a9c1a3cf0" Left="[float]22" Text="[string]Voltage measurement (V)" Top="[float]18" Width="[float]135" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{9410ca5a-4136-4c0c-823c-a1df1a26a17a}/Output/current_measurement" Height="[float]24" Id="73441afb52804857871a5de22da3f93e" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]ea95b654283f4ca0bb837815a25ee415" Left="[float]22" TabIndex="[int]1" Top="[float]93" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="ea95b654283f4ca0bb837815a25ee415" LabelOwner="[UIModel]73441afb52804857871a5de22da3f93e" Left="[float]22" Text="[string]Current measurement (A)" Top="[float]73" Width="[float]135" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="f742e6704654462e98a822de01f10264" LabelOwner="[UIModel]e5b036d2df8446b3803be101786b5500" Left="[float]270" Text="[string]Results" Top="[float]80" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer_example.seq sha256=6300da971339915b7fda881062940b2ad4722a00055486077e73d12fd3166d35 bytes=216734 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/NIDCPowerSourceDCVoltageWithMultiplexer_example.seq`
- sha256: `6300da971339915b7fda881062940b2ad4722a00055486077e73d12fd3166d35`
- bytes: 216734

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.1.0.49154' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN2&lt;dfASB`]CF^aUXa]Y\4WmD]203VfR;kS;KgdGgF285WU]RaSJgcjNlM7MFC4LiX=a48\7dW:L403mZ4BUAT82I&gt;KQH8\T8QFE`DA2\LAVbMD5YRMT13fTiE^i&lt;boIle7[=C_LeZbKM2QXhVTH;?4hTX]A[17:2T;Dh\^Co3kY9PA5QK23^C]l262h09La1?5^k3J0BQZ@@EeDRZTO=\cKd?XKjmGb1N\X&lt;J[IS9OXJj22Qc=R\WEEn\IKCaHCAUNi97;EVjaJCX4&gt;UU36B3oib::mkjjIJFOY^^C_gK;?Ngamc6b1^HOM^Rl@oHoiaG802US0o36;lHiif[]oe&lt;FRliGlo^CMk69OeFDNDnIQUXNS=iA3JmW&lt;KbcFOCL6bWF;DdY7d2\SSH4mB7[^9gAb5EgM5G;l^DR5mXURj&lt;_=4b_aTDS965fd7ACLdkeA7kamDL&gt;;lWi[PA07_B@&gt;cR[mGK`_XMGdK4NmjkVR8?micjQcMS=oX^9@cW^5\93S[[2ZkFbBiZ=Q@AM0FkKdo:gUd&lt;lVVcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX34oO2LYb;J&gt;k9nWLWBEg6Tk&gt;koggGTQ&gt;kL6kJL@dKQ2_E0Z</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWeomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^;g[CAF?o9BS9X&lt;V_06oLo]n`VOa[dMZmhLlJ^=?^T^nMbojKJkCSoWN4WIgV\ckgWCOWb7&gt;jno&gt;;[OS_oVacNOW7jg77?7OooD2OombloUnEI9_InB&lt;HI4[kZLf&lt;]bOKRmn::VQk1Tm`8F4;5W&gt;TA&lt;Kcd`aI[R8DKQka6aboN?k=I&gt;UJRNToCflBd:9=GW1XijhYcm92_e]^Rg?N[eOQO^9B&lt;2LjSQk=KKS8Eo?8kT9]m3^^fWPk?AQN^K4hZkc&lt;Vm&gt;gFc`@RgL^O5bET;[D_=R`WO?&gt;&gt;77S_K[1miPR@lgJ;?^^n6om3JliJgSBbAO&lt;J&gt;_7OGSQoU5Mo5ainP9oNj=DL&lt;NdI=^]VXFK0i[_\n0emoFJc]\=:4K&lt;HYHRl[4;=V_6SaC6ETl6dE1KV^E5NV9OgQBU&gt;n`WYOLgi&gt;S84nN^1mG5`SPC1]S:d;`B=4NjKmH&lt;UULW:0\;?2W8FOA:^K?M9TIFdMZj?UgUemK:5BfZf19WV&gt;o2K6[k;XS0HEj\8[[9QY;;_Z:UlBgN&gt;g897SGQPF^OS\Ba8&lt;Nl5AB?;oWBQ6aJP@1SQNGhXj:1DK9OHN&lt;6lGSkolg=dM`l2hG?AKRH2^5E7fbmmi:cJ2A056EVl9@Ll@B9;Ml6POPlacQAcKJf4N0AbVYZdLjl=5el2I6[[UbiSJdAiTCbBdeiYEk9g6Sa7[CFB8`Nkc\S4`dNB53K4Y@M`QAkbIdlgkPUJ??fmoGj]cMHcUoJH_X:heHfm2bQ96d\&gt;Y;:5diBn6JoC0O8DGdkT9VIPBjN^1cB`TcbjfVBJNQ[?b\onSkg@kON1onmnGNoOnYOo&gt;kc^Ofm]G7mB&gt;Qba^I&gt;6iVCm0GSnGTYgQ_Ig4AOR9MZMAk1Il1RgBV7TIAM`A=\k&lt;V4O9c?_3Y:O3l:dCYMk^gg;jl0L0CVKCUWH5`j7aeFkA[b&gt;CTQ95a^731VBF_IoV`TDggl4NO?G?^6Y3k&lt;P]4e7VRbee]]ZcM@Jf4&lt;;aWfGU&gt;9^:[`SDoKE?YZ:Vd8[TTU\cVW7EE&lt;cK2Y;_LD3MKjVT98S3E]O@NF=[GoXgC=`=OMNoZQ@@l2P:F[`T0:[LS53m:IMEkRTe@8gJE`&lt;]Y2:U`M8HkClI4_aPZN:4ZLOC2BoZFX8GCf8_I0;U^`[:e@:ILD&lt;808A]97NXjMJdHVK5&lt;6@ZRfV:AX6kPcgf@:31?M9dKQa?=RA:`f5TCI^bQLjbA?jYd&lt;_1^@Iek6[helE6RFL:EWA[cHLkB2l7QLeCBJX]0hDPWUWlCJ=:^m5gJjn&gt;SW9DRT1Q[Y5`gAf&lt;OdDdj1YNo:`NeELR3c2mU`G:e&gt;j8@]gAR?Ad48]8;:;&lt;S;EUJcjMiOVF1m50TbUD\Tl58jH?d\X8T^08T=W9[Z683aTA&gt;]W[5Oi5M?52E\:71[03U?V`4l_1WVH4j:GKI9hcEGRk3?_;k:;F_ej5SiN:WT:RF=Gmdl:=knc:UD^Hj9obj;AE\I7HC&gt;FB&gt;jYl8f56nJ&lt;UcI=fiN&lt;i;VXUJ55KE9jS9S_DR5N1k`PSNZVY0Z0iTYNej0?V_@UDHkL6Co5UCKBGPJYGR_Ti@1C@\A6TiIe;E\]e=ZZKd\ZVfURZTM50e8JQ[&lt;TMTUjFdJKR_9CXd\N38JN&gt;Q&gt;\UNF]@;FB8LQX@?dbU@[8mfDU3:S0dI&gt;?SmaPSHhfe6&lt;gV@A0JSZnmSECILX[AB98eHXQ9`R?5E3I6[4N=mYUREb_5jZURE5lhN6VZ\P`:`^;AQONF8O:Plbm4XSolW7VZN&lt;?OL8@0JK^m:5oh&lt;AR[a:BRlMniCM&lt;Q^\X\Nkg7G3ZMAi7nm:9PFFe3mCA1\]DY\Df;6aG&lt;iI]h2G6MG`BA\[I]008f:U6XXSNH2jcIXFSGI5Q2bBEKA`&lt;X]h_:@RfNklLbR7Sji9F_895&lt;R=Q572IULj=^noMWZiZ`ddKH`@`He:jliNb34YNl9[QT6cAlE&lt;6LflQ9e?nUMDFlcJBlA3?PP6fSobc@Of_fBSccJNY=&gt;?N3lZRDPO[EVgdA&lt;FBDB`XE&lt;^e]0&lt;&gt;VkM0OT@X&gt;YTBh&lt;5IL&lt;3?]`D2\9TbD=P9XH933VJR1BePO?6H6&lt;2;Rb:@82Hbj[IF&gt;5Pl5;dH0QG4:@48T&lt;39AjLjU172J17:JNl=j0P6NHX8U6RT@@_R0PglmF;;HX\i:jV^ULZBDKEBVfUTf9YQgX[9IDjjfT&gt;:iY`4VU&gt;jmJ&gt;^lE2G:UodJJ0?kJBH?eL@[95RbKJUIOlaNeJ04aJ?]A4YMiXMjb8EdSS:FQ@7jO^6V2_52W:f:]&lt;6e5Cd?=1I1S`LR^aZ9L?2:i8gKEhKfCL5bbPaMloUSe;o9aiAW[oE2DcNMo=]V3VZ3j=;eK0o5HDY[@\W;=e@Vl8XLFANQC9E&gt;QSA=CQY79hkh3K&lt;7T?;nR9;Z6LT?Nc&gt;S&lt;VnOhN&gt;A7dhl]K:oLi0N`lo`P8XYbiZhgEiMHkPY4;7?ho]9J`Z9g^0o=n=LSnOn?ieOB64nHAQFTK8PM_MC[JSeR8@G2bZIEdgH&lt;RZ;OM]&gt;@_LW:9G&lt;i8_M&lt;G0iefC[hgQ3@MR?7jB\Tc1Tf;FbZLgF5X3L[[i7=`i99aTj6Bf9hoc4f&gt;K\mAKJU5HVOhmaTQmdX?THaTcA20&lt;o\eFYJL5Fl`OaV0Lg^m=dM8dKEXZbi_aM`N4iNOTmgWYL3]hN6L7iae8^GXbD:O\Y6CH3&gt;KSj1^`C4a]&gt;WQ7OESNDVeoS81il`C&lt;lI\h;BR2o8`kOIUYaC_UM6UhYa5^:Vn4Tg@DYb3U\b\fAFX]aIIO3S\LG^&lt;VA[9&lt;di1?XH4d]PXFb[&lt;mS6WM1H7n4QOPX3V8JcaJ3Bc2f`3kS9^djl1&lt;NFQDkA93Ufmf&lt;amc=`80X1e3HkQ:L]YabEBD05fi1W2^:CkBEDcH^&lt;iZ;L:\8jH][;VZj4R5VRdB6F7g=a:g99Z[d9NoQ89XZfYU6Ej\lMNK`GXE8]&gt;kb1[e?Qc4mH:lRM9\OK7F\j_JGQ2X&lt;8nV91\\ReIUTd4;L6nZ4o7O&gt;5To5e:L?2S2kY98YfOPONej0UZd28\R5Kk_&gt;WnN^DH2Ra&gt;8JPmDGUT4BS3E6S6N6PXQ^o?DU4hlJ1V&gt;V1L?:__=@EIUOn9X7KR2Lo=2KmV9A8=\\T\C=1?n1D=@?IkA\=f2ii0CCN:&lt;9RPOFL`NU8DSQ&lt;`;_2&lt;nB]=6e51SI8613fMTW3Oj[L^R]8&gt;Pi:a`A2D=\4K&gt;il^UBR7P9]^G5NXA2^X7951G[YT\OKLGG4l=UQn;H7@B;8&gt;da:ibOD[XBR`]o&gt;VZ6DOCdK3AP?3A_33UbkQTneQOg=b`jYf;]h]AolQHPG^On43=0kIj9]cNR^:eSCY@7J3d:fE\We:Vb01HQD:H^8XDCNhWA\A:WD1Gl3&lt;U7dkK=5DgXUKgD\cnF6@[17\Fk=:4E@TUiP?Fl@0i9ZoM2bEb`155W4J=3T3DML1\aF:FfPQ_KUbIc:4Ya3JFAmR\aJMI0a[C4^ef5m^Fi4&gt;XZHB6?JU:=DZ87J56eH&gt;DmEMhP4D2oO3SJP&gt;1jMO2&lt;naOX3XeHoDCM;;J:PJlY8lXGAERILBl6Ze45f=C_H1EH@IjHR`mDHLk&gt;RloAEY7C[?GIk&gt;fJcE8?]mNG9gjfLehW\mLW]iM[?]hJNCWK\EIR0P]hk6`E4NUFW`L?jP9&lt;3@in]\&gt;b[aNQRj1@R1@lHWUO7cje0A&gt;LK;JhC[BgiI]\2@eSX:;QfRU@U&gt;]@_lm`4NmBZ\:ZoSFUb?TlhO5;?&gt;B1H?gA7=g=C1ji=292Ke0J\FnE9DeX&gt;CIC;iJ0Q`DXj&gt;W\&lt;PEOYPYk5m[A0\aN8N8UXTPGU[n]bW5n:`?nZlnnf\Imkoebbigkc`ofP\eP3l@ZOUX`?B@DZR_DX[^jV=gj=d1Ym4Z&lt;ob`?C`SLo9T5_eOKONeoF]7?koVKmXXP&gt;@mOLEB_KIcmYAEE:TPO\X\:IW;;f\GU_9nGfb7gkm2FX@_m\=LZKGW]]fQbgkjIKFn:Z?7OkIIKJ[SO\hURRIoOHS?5Im13fdEU3GX6A:fkd1W=WEW;WIRW;nf8PFKmj0I6c\Ol161GZUA]d;MJ:ZYK=VEA5\=d;6WchfDOoda;nMHPO^dHdLa@nRM@8^2Oa`S?HXLF4nDR@[gd@3ZWg?=HDeoV\ekeE:jne_Z_g?4HH]X`?HL\fA&gt;3IiNAk6W1m3G0_2TCL=LYO`T`_HK@l\3K6f3=3kY61mh3P6N;k6W1m37PK&lt;`\K6`f=3Y6;mn30n@QPPL_O`T`_HNXdTNm3PcB7f3=3k]61F3f^\2K6J51o9_dONJi[aZ=PgGoQ_YlegmNBlj]Mg1Y9kjW]mhcf\AE?5N[_l]E?eCjcMOO`&gt;NKk6j1FegWdiGIk&gt;gJcF[NcfKLeBjFNcffLFL[]in=6bC_H8^oNbA_H\`Ig&lt;[Zjc\IO`GPnSnRYk245=G437EhljgHLTJJgAIlMMmTC]5Ofg3k7l1=okWM^WiPP\Tb&lt;_gjXVbPjlMb^O2?7g2GoojlSJ\BolCmm&lt;eolmTbca0HGIPS7WELFBRNnUKon6]o_boQc4&lt;O7WakMAfZ1;@;]BVhfZ6d;A]\Y;]^C\2JNWl@EDkjHUD]8Gj3k:Gg9M]64UVIhV`0kFZjnXDXH9Ul?3UgC&lt;4E`da=l&lt;6aYaK?YSB&lt;ZlK8AkLXPga:L6Y9WXb^R2:;XfCCXg46QgO@OonCH=04lnD]G?@JU0oW&gt;8R[cd5WUn`Lj&gt;_L4H7acI]&lt;]SYiCVkXMEcP^ab7Tf\&lt;L36cdmoD7?&gt;U&gt;FXnG58NQBfkE`&gt;Y&gt;ZXN^;LUDk^0CT`]]YcV503o2&lt;9aY76Tb5=h;3n^l@;GR:DEml&lt;HjcCj]?2BHSYcAH8LcPLdmXLfl9&lt;R?P&gt;m[d_OAF47OMiiSBYLBDIO:B2mBEQejeLI1_lDOkc^TPmOSR;N?RhN=R3X@`aEX13VmJG`^nJRDXYeb7QSJiLJ`NX5Qkf=]imm&gt;nKg_CV6OK]RK94GkTDXQ&gt;HaT13fb00I9PG6JX1RmPQA@CXT2Ci9A4;\8804oTS3&gt;9F@3jQ0Q`Yb6PH2J8=QIl&lt;U65fY12^T^l2@8TQ51B^@UA:oVP&lt;O1`X1PnPjXO0`P3GQkdBQm:cV001le`9l2VYAPg8&lt;0k8Bm6`QjeP@j2ciUhWLj@0LY?3AP784;S@YWHX1S?Qn1m1kHbJS6f811fJb&lt;=99l6:nE1PPJ=8l=&lt;a\P0dAX0LXTD&gt;iH&lt;5QR6^dF;Bab60@I1@Q0HZS?9?A@TRA`J1PHiRc:Q:_jX1GeY=N[B&lt;3V2Pd60J^Y3@[1hD0XF2MP;&lt;B3RX2_H4PG43R;`1ZV@8E0R&lt;KHgh4VHe2B0H4:Y&lt;H5&lt;Q723C@d@1WBS^63LMX3=h4n91c3XeS;4aDhDR99PE40@14SA4S8Z_QlfJ^kenOQMQl\MFkQ32aVj``BUAmNDAB3?\R55J4A\37PAhR]3=KA6W&lt;86890Ck1NP@_[g:D6dV4Q49fS?IJ_C2;S^7mbE9SkO2G9Ii^ggHKkT`F370_j7b?jkWkEQ]:?XVf6A2ilo3@QYRZ82LV4K6^KABIXe``g6B7e1HCJK8hP9k^0X&gt;O;4j2^RRM3c2=aH8f`YUfUlb`B&lt;3I37=]e&gt;@JZ?KI:?@GJMZ]DOXZDNYX\cVFBbZ1RmDIF82=NNZDMK0dibVYa6E8b@nBP&lt;5Tl&lt;05lIDYhX^b6F\?\XfTjW:PUgjFJNIm\aeD&lt;eoRAhT`S]9IT7:LUghEY&gt;2fJODYDMFWDNBTdof=ITOaPAL59FVSX7NGk\MRM]DU&gt;&lt;nm39CJKab2S9fP&gt;SbRPR`h&lt;R0@D@5P9ZV08\FAR=6B[D?`iF9Xa6Q9e:U\ARX=B]93S4;17PliCP_8N5h`&gt;i6V3&gt;38TciG@Te@WT`HL8`hPj;\D6gSlTdaAYJMc8Hiaf&gt;[[@NAUBeHhFNTm7NYnXia&gt;:JBgQ?oS?;U9jT\\=AYoUTMCT\81ZYRXNJb\lbEEL&gt;e79ib&gt;:2`]U2jToCY]80BfV:4``\X1a4BL&lt;9?9ATRQ4bcK7^1A4RoX@7_2@S;hfe90M;0D;DJ]?I]5@0Y`&gt;NV3LF5`I1LYCFZTJU@=fTdVb2IPfC6dDZZ8JGTc2QOh;^L8HnSlnS?YbH5TGiYN5i9a8XWVIV]cK^:A]LH[5Lm2L34ZfLDn&lt;hgf2IHQJV6o[CK&gt;:33MOAcD5k&gt;LcEW&lt;&gt;D1CTFD^e69IAD3mLk&gt;C56YaKeFci;[THhLnK]V7iaZ:O5@PcUHH0f];^:5a0o2@FhcUKMQ5D&gt;nJn?Ija2clJo0KQ0:6Z&lt;7KD=:2I^YmJGE@ELPHG[9N\9mCc046gh\;[KBUd_I=RJbRBo&gt;kD8\BUXbUB8c&lt;]fF[BViXJSLNm=oWLlRY</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
										<PinMapId classname='Str'>
											<value/>
										</PinMapId>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Source DC voltage and measure voltage/current via multiplexer'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:1m8fotxw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIDCPowerSourceDCVoltageWithMultiplexer_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[7]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_name</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Pin1"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_level</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_level_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_limit</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_limit_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>5</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>source_delay</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>6</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>voltage_measurement</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>current_measurement</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[2]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:v3cHTx+U7hGhw2DjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>"NIDCPowerSourceDCVoltageWithMultiplexer.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DCPower sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:c5USoqlx7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidcpower.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nidcpower_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-SWITCH multiplexer sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:pcneL8bQ7hGxiVAoSqomQC</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_niswitch.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_niswitch_multiplexer_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DCPower sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:syCDFOVw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidcpower.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nidcpower_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-SWITCH multiplexer sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:EUHSk8bQ7hGxiVAoSqomQC</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_niswitch.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_niswitch_multiplexer_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/pyproject.toml sha256=8ef0f02f4b852d45f16be5846efecde479a9f3f54ae66905ac8cb5b73e294773 bytes=1389 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/pyproject.toml`
- sha256: `8ef0f02f4b852d45f16be5846efecde479a9f3f54ae66905ac8cb5b73e294773`
- bytes: 1389

````toml
[tool.poetry]
name = "nidcpower_source_dc_voltage_with_multiplexer"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that sources and measures a DC voltage with an NI SMU connected via an NI-SWITCH multiplexer."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nidcpower = { version = ">=1.4.4", extras = ["grpc"] }
niswitch = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidcpower = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nidcpower", extras = ["grpc"] }
# niswitch = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/niswitch", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "hightime.*",
    "nidcpower.*",
    "niswitch.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/README.md sha256=a3ba055821d4fd1ff59150e5eb6475a598e56ffb7fa7492d4553a25836045e8d bytes=2382 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/README.md`
- sha256: `a3ba055821d4fd1ff59150e5eb6475a598e56ffb7fa7492d4553a25836045e8d`
- bytes: 2382

````markdown
## NI-DCPower Source DC Voltage with Multiplexer

This is a measurement plug-in example that sources and measures a DC voltage with an
NI SMU via an NI-SWITCH multiplexer.

### Features

- Uses the `nidcpower` package to access NI-DCPower from Python
- Uses the `niswitch` package to access NI-SWITCH from Python
- Pin-aware, supporting single session, one pin and one selected site
  - Sources the same DC voltage level on all selected pin/site combinations
  - Measures the DC voltage and current for each selected pin/site combination
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
    session registration and unregistration in the `Setup` and `Cleanup`
    sections of the main sequence. For **Test UUTs** and batch process model use
    cases, these steps should be moved to the `ProcessSetup` and
    `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-DCPower
- NI-SWITCH
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI SMU that is supported by NI-DCPower (e.g. PXIe-4141)
and an NI-SWITCH (e.g. PXIe-2529).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string:

  ```
  MEASUREMENT_PLUGIN_NIDCPOWER_SIMULATE=1
  MEASUREMENT_PLUGIN_NIDCPOWER_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIDCPOWER_MODEL=4141
  MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE=1
  MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY=2529/2-Wire Dual 4x16 Matrix
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_nidcpower.py sha256=c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea bytes=2623 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_nidcpower.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_nidcpower.py`
- sha256: `c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea`
- bytes: 2623

````python
"""Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DCPOWER,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidcpower_sessions(sequence_context: Any) -> None:
    """Create and register all NI-DCPower sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_sessions(
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER
        ) as reservation:
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nidcpower_sessions() -> None:
    """Destroy and unregister all NI-DCPower sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_niswitch.py sha256=5fd65a15b479e1d99d22c3a40d03247a908dfd3283f030c42905ae1751379a0f bytes=4902 -->
## FILE: examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_niswitch.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_niswitch.py`
- sha256: `5fd65a15b479e1d99d22c3a40d03247a908dfd3283f030c42905ae1751379a0f`
- bytes: 4902

````python
"""Functions to set up and tear down sessions of NI-Switch devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_RELAY_DRIVER,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_niswitch_sessions(sequence_context: Any) -> None:
    """Create and register all NI-Switch sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_sessions(
            pin_map_context,
            instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER,
        ) as reservation:
            with reservation.initialize_niswitch_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_niswitch_sessions() -> None:
    """Destroy and unregister all NI-Switch sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)

            with reservation.initialize_niswitch_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass


def create_niswitch_multiplexer_sessions(sequence_context: Any) -> None:
    """Create and register all NI-SWITCH multiplexer sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.get_multiplexer_sessions(
            pin_map_context
        ) as session_container:
            with session_container.initialize_niswitch_multiplexer_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_multiplexer_sessions(
                session_container.multiplexer_session_info
            )


def destroy_niswitch_multiplexer_sessions() -> None:
    """Destroy and unregister all NI-SWITCH multiplexer sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.get_all_registered_multiplexer_sessions() as session_container:
            if not session_container.multiplexer_session_info:
                return

            session_management_client.unregister_multiplexer_sessions(
                session_container.multiplexer_session_info
            )
            with session_container.initialize_niswitch_multiplexer_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nidigital_spi/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nidigital_spi/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nidigital_spi/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/measurement.py sha256=51bb72f48ae93b7172cb955ea112dba62f2bd7bfa46ed6f17d1428622da17750 bytes=4570 -->
## FILE: examples/nidigital_spi/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/measurement.py`
- sha256: `51bb72f48ae93b7172cb955ea112dba62f2bd7bfa46ed6f17d1428622da17750`
- bytes: 4570

````python
"""Test a SPI device using an NI Digital Pattern instrument."""

from __future__ import annotations

import logging
import pathlib
import sys
from collections.abc import Iterable

import click
import ni_measurement_plugin_sdk_service as nims
import nidigital
from _helpers import configure_logging, verbosity_option

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDigitalSPI.serviceconfig",
    ui_file_paths=[service_directory / "NIDigitalSPI.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_names",
    nims.DataType.IOResourceArray1D,
    ["SPI_PINS"],
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DIGITAL_PATTERN,
)
@measurement_service.configuration(
    "specification_file_path", nims.DataType.Path, "Specifications.specs"
)
@measurement_service.configuration("levels_file_path", nims.DataType.Path, "PinLevels.digilevels")
@measurement_service.configuration("timing_file_path", nims.DataType.Path, "Timing.digitiming")
@measurement_service.configuration("pattern_file_path", nims.DataType.Path, "Pattern.digipat")
@measurement_service.configuration("load_files", nims.DataType.Boolean, True)
# TODO: Measurement Plug-In UI Editor doesn't support arrays of Booleans
@measurement_service.output("passing_sites", nims.DataType.Int32Array1D)
@measurement_service.output("failing_sites", nims.DataType.Int32Array1D)
def measure(
    pin_names: Iterable[str],
    specifications_file_path: str,
    levels_file_path: str,
    timing_file_path: str,
    pattern_file_path: str,
    load_files: bool,
) -> tuple:
    """Test a SPI device using an NI Digital Pattern instrument."""
    logging.info("Starting test: pin_names=%s", pin_names)

    with measurement_service.context.reserve_session(pin_names) as reservation:
        with reservation.initialize_nidigital_session() as session_info:
            session = session_info.session
            pin_map_context = measurement_service.context.pin_map_context
            selected_sites_string = ",".join(f"site{i}" for i in pin_map_context.sites or [])
            selected_sites = session.sites[selected_sites_string]

            if load_files:
                # When running the measurement from TestStand, teststand_fixture.py should have
                # already loaded the pin map, specifications, levels, timing, and patterns.
                session.load_pin_map(pin_map_context.pin_map_id)
                session.load_specifications_levels_and_timing(
                    str(_resolve_relative_path(service_directory, specifications_file_path)),
                    str(_resolve_relative_path(service_directory, levels_file_path)),
                    str(_resolve_relative_path(service_directory, timing_file_path)),
                )
                session.load_pattern(
                    str(_resolve_relative_path(service_directory, pattern_file_path)),
                )

            levels_file_name = pathlib.Path(levels_file_path).stem
            timing_file_name = pathlib.Path(timing_file_path).stem
            selected_sites.apply_levels_and_timing(levels_file_name, timing_file_name)
            selected_sites.burst_pattern(start_label="SPI_Pattern")
            site_pass_fail = selected_sites.get_site_pass_fail()
            passing_sites = [site for site, pass_fail in site_pass_fail.items() if pass_fail]
            failing_sites = [site for site, pass_fail in site_pass_fail.items() if not pass_fail]
            session.selected_function = nidigital.SelectedFunction.DISCONNECT

    logging.info("Completed test: passing_sites=%s failing_sites=%s", passing_sites, failing_sites)
    return (passing_sites, failing_sites)


def _resolve_relative_path(
    directory_path: pathlib.Path, file_path: str | pathlib.Path
) -> pathlib.Path:
    file_path = pathlib.Path(file_path)
    if file_path.is_absolute():
        return file_path
    else:
        return (directory_path / file_path).resolve()


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Test a SPI device using an NI Digital Pattern instrument."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI.instudioproj sha256=c676a8b4c4148c17dc90cf6053e1447fd2c332f30563de60d3ff287285d18200 bytes=1987 -->
## FILE: examples/nidigital_spi/NIDigitalSPI.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI.instudioproj`
- sha256: `c676a8b4c4148c17dc90cf6053e1447fd2c332f30563de60d3ff287285d18200`
- bytes: 1987

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="06D070622FC1073D0FB91E2B7C687E7D8B82DD4599F318CBF3B5C02AD7DBF98939E3DD2F80562C603E07A8544BD83758D89BD2E0177C36FE1589272AFE72F00B" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.3.0.50000" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50000" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.50000" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.3.0.50000" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="3ab61632b377479790b6875be7d84284" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="4439f7348b124e6993b98bd28e606ecf" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="6142403156074b2393d0153d4f3d79d6" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Bindings="EnvoyManager" Id="bce8ab87cdf3473d81772fb9beabad92" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIDigitalSPI.sfp" StoragePath="NIDigitalSPI.sfp" />
			<FileReference Id="60a4c6fdc0d7486c837ec504fc4148a2" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="PinMap.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI.measproj sha256=5ebbeeaa83f98795d58bd8dc938a295b7958ce29668f0c04aaf0df6d9ca08ba1 bytes=3781 -->
## FILE: examples/nidigital_spi/NIDigitalSPI.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI.measproj`
- sha256: `5ebbeeaa83f98795d58bd8dc938a295b7958ce29668f0c04aaf0df6d9ca08ba1`
- bytes: 3781

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4A796EE5DE526AB74EF8CF756B9490864D08A34A821E22EE3D9AC5434EB78A795F0AA851D1F5176B2187F4011767CA957B1D5CE348D34FBF2CCBAC5356E61492" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.50004" Name="MeasurementLink UI Editor" Version="23.3.0.50004" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="5c3bb209a1d34ba9a30a9b9b34c3aa8c" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="f5bdc8b928da421d8d8630ef36c4295b" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="44aefe1a91aa4283b994fbb30f4880be" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="a5a7d9fce4214cfdbcef4e8e546a95d3" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="d08461a7f3b840b68b5349d1d12658cb" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="ef1d728f2a084bc3a7c9c9100859c198" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="b89b8a4781804327a2b92264b09e7486" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="ee89b89ded4447b2a136d5d18e227ac7" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="759927b35d004465a4169daa6ad28c44" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="5e6cdaeda7394fe8ba2b9a0203512773" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="5261d3f269984bd593ecfe17d33c337c" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIDigitalSPI.measui" StoragePath="NIDigitalSPI.measui" />
			<FileReference Id="5b94aa2212244f42802d6777f1fabef5" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="PinMap.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI.measui sha256=acd882f7aeb0c58accd318a3bacf7148a48ed238fdc14a45dca5c0cfbf098146 bytes=10471 -->
## FILE: examples/nidigital_spi/NIDigitalSPI.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI.measui`
- sha256: `acd882f7aeb0c58accd318a3bacf7148a48ed238fdc14a45dca5c0cfbf098146`
- bytes: 10471

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="BB79F6564BFDCFF1B2A8E5F5F65F84F7D0DD8925606495AE2DD1821E11F3553F71F9E711863AECED0954F9063EE3B8CB746266DF821CDEF8E0D5F44A9C83F4B1" Timestamp="1DAB1E6787BC133" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.13.0.1981" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.13.0.1981" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.5.0.1981" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.13.0.1981" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.13.0.1981" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.5.0.1981" Name="MeasurementLink UI Editor" Version="24.5.0.1981" />
	</SourceModelFeatureSet>
	<Screen ClientId="{fe5ceb75-86d0-450f-9e97-b09144fe3866}" DisplayName="NI-Digital SPI (Py)" Id="b6a6fffc82e44c57915dbaba1f0d609d" ServiceClass="ni.examples.NIDigitalSPI_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]425" Id="6a6c436b22f45d8a0fafe5ea6643c07" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]775" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="3532ab18927248a7a439e21b367dcc7f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]aea94067a4614941b84fbfe7ff96e0fa" Left="[float]22" MultipleSelectionMode="[MultipleSelectionModes]List" Top="[float]278" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="aea94067a4614941b84fbfe7ff96e0fa" LabelOwner="[UIModel]3532ab18927248a7a439e21b367dcc7f" Left="[float]22" Text="[string]Pin names" Top="[float]258" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]a841617b7e014ff885e60ce05018caeb" BaseName="[string]Numeric Array Output" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Output/passing_sites" Columns="[int]1" Dimensions="[int]1" FirstIndex="[ArrayElementIndex]0" Height="[float]120" Id="bbd8f68043274454a4f97f5689410ecd" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e1968262429145cea05374dd781dcb80" Left="[float]187" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]0" Top="[float]278" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
				<p.DefaultElementValue>0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="a841617b7e014ff885e60ce05018caeb" Interval="[int]1" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="e1968262429145cea05374dd781dcb80" LabelOwner="[UIModel]bbd8f68043274454a4f97f5689410ecd" Left="[float]187" Text="[string]Passing sites" Top="[float]258" Width="[float]68" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]77a6678e6d684f60a06c1454b7fa3946" BaseName="[string]Numeric Array Output" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Output/failing_sites" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="347640288840a48c72be70fe98ed00" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ad342cdedf494e188074140736759fcc" Left="[float]320" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]1" Top="[float]278" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
				<p.DefaultElementValue>0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="77a6678e6d684f60a06c1454b7fa3946" Interval="[int]1" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="ad342cdedf494e188074140736759fcc" LabelOwner="[UIModel]347640288840a48c72be70fe98ed00" Left="[float]320" Text="[string]Failing sites" Top="[float]258" Width="[float]61" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]185" Id="eb0610ebe90f4e2fa65269a4b1f6f579" Label="[UIModel]6af501959cf647d68a582ee37af08d8f" Left="[float]12" Top="[float]33" Width="[float]730" />
			<Label Height="[float]16" Id="6af501959cf647d68a582ee37af08d8f" LabelOwner="[UIModel]eb0610ebe90f4e2fa65269a4b1f6f579" Left="[float]12" Text="[string]One Time Setup" Top="[float]13" Width="[float]86" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPathSelector BaseName="[string]Path" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/specification_file_path" Enabled="[bool]True" FilterLabel="[null]" FilterPatterns="[null]" Height="[float]24" Id="6ce0084c76d1496bbc8f9cc521aa95e3" InteractionMode="[PathSelectorInteractionModes]BrowseDialog, TextInput" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9119b2189608477f86b089c72a815ca8" Left="[float]22" Top="[float]170" Width="[float]136" WrapText="[bool]False" />
			<Label Height="[float]16" Id="9119b2189608477f86b089c72a815ca8" LabelOwner="[UIModel]6ce0084c76d1496bbc8f9cc521aa95e3" Left="[float]22" Text="[string]Specifications file" Top="[float]150" Width="[float]92" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPathSelector BaseName="[string]Path" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/levels_file_path" Enabled="[bool]True" FilterLabel="[null]" FilterPatterns="[null]" Height="[float]24" Id="32db9560c8ca43778932f6cfce4509df" InteractionMode="[PathSelectorInteractionModes]BrowseDialog, TextInput" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ccb9c27f248042c79c52ed43812c057b" Left="[float]177" Top="[float]170" Width="[float]136" WrapText="[bool]False" />
			<Label Height="[float]16" Id="ccb9c27f248042c79c52ed43812c057b" LabelOwner="[UIModel]32db9560c8ca43778932f6cfce4509df" Left="[float]177" Text="[string]Levels file" Top="[float]150" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPathSelector BaseName="[string]Path" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/timing_file_path" Enabled="[bool]True" FilterLabel="[null]" FilterPatterns="[null]" Height="[float]24" Id="9e3a6051563945b6b07e5f513e2a649b" InteractionMode="[PathSelectorInteractionModes]BrowseDialog, TextInput" IsLabelBoundToChannel="[bool]False" Label="[UIModel]b0575bbf18854786ab26549a7a0afa31" Left="[float]332" Top="[float]170" Width="[float]136" WrapText="[bool]False" />
			<Label Height="[float]16" Id="b0575bbf18854786ab26549a7a0afa31" LabelOwner="[UIModel]9e3a6051563945b6b07e5f513e2a649b" Left="[float]332" Text="[string]Timing file" Top="[float]150" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPathSelector BaseName="[string]Path" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/pattern_file_path" Enabled="[bool]True" FilterLabel="[null]" FilterPatterns="[null]" Height="[float]24" Id="db2aa43731944814ad0daed8f2278f15" InteractionMode="[PathSelectorInteractionModes]BrowseDialog, TextInput" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3634487cbf7340e8b5d75890e011732b" Left="[float]487" Top="[float]170" Width="[float]136" WrapText="[bool]False" />
			<Label Height="[float]16" Id="3634487cbf7340e8b5d75890e011732b" LabelOwner="[UIModel]db2aa43731944814ad0daed8f2278f15" Left="[float]487" Text="[string]Pattern file" Top="[float]150" Width="[float]57" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{fe5ceb75-86d0-450f-9e97-b09144fe3866}/Configuration/load_files" Content="[string]Off/On" ContentVisibility="[Visibility]Collapsed" Enabled="[bool]True" Height="[float]16" Id="84739f1ef61e4e7f82cc893fe3edf311" IsLabelBoundToChannel="[bool]False" Label="[UIModel]86b339d898e24ccba05ac027acc5455e" Left="[float]22" MinHeight="[float]16" MinWidth="[float]16" Top="[float]85" Width="[float]16" />
			<Label Height="[float]16" Id="86b339d898e24ccba05ac027acc5455e" LabelOwner="[UIModel]84739f1ef61e4e7f82cc893fe3edf311" Left="[float]22" Text="[string]Load Files" Top="[float]65" Width="[float]53" xmlns="http://www.ni.com/PanelCommon" />
			<Text Height="[float]80" Id="4f4e0497e4664287989ef6fde08ee38c" Left="[float]142" Text="[string]NOTE: This determines if the measurement will do one-time required setup - loading the Specifications,&#xD;&#xA;Levels, Timing, and Pattern files. It should be true when running from InstrumentStudio. It should be false when&#xD;&#xA;running from a TestStand sequence where there are previous steps that load these files before running the&#xD;&#xA;measurement step. In the InstrumentStudio sequencer, the first NI-Digital SPI step should set this to true and&#xD;&#xA;subsequent steps should set it to false." TextWrapping="[TextWrapping]Wrap" Top="[float]53" Width="[float]588" xmlns="http://www.ni.com/PlatformFramework" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI.serviceconfig sha256=acc76f3651fe45c948ba15154cebfb893368b18cb1f350e54653eaa26467097d bytes=679 -->
## FILE: examples/nidigital_spi/NIDigitalSPI.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI.serviceconfig`
- sha256: `acc76f3651fe45c948ba15154cebfb893368b18cb1f350e54653eaa26467097d`
- bytes: 679

````json
{
  "services": [
    {
      "displayName": "NI-Digital SPI (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIDigitalSPI_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that tests a SPI device using an NI Digital Pattern instrument.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````
