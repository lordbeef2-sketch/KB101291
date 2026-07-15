# NI OSS SOURCE SNAPSHOT: nisystemlink-clients-python

<!--NI_OSS_SNAPSHOT repo=ni/nisystemlink-clients-python commit=0bed315df7e0dd210396f3669d42211c96a641d5 -->

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.flake8 sha256=0da9774692421323ed8ad3ed121ea6b02e019b05d7dc17c21080e05cbe4d0d4b bytes=555 -->
## FILE: .flake8

- repository: `ni/nisystemlink-clients-python`
- source_path: `.flake8`
- sha256: `0da9774692421323ed8ad3ed121ea6b02e019b05d7dc17c21080e05cbe4d0d4b`
- bytes: 555

````text
[flake8]

max-line-length = 119
# but keep line length to 88 in general
# - use "black" to auto-format

# D400 and D205 are because we sometimes split the first line of the docstring
# F821 is temporary, until code is complete and stuff like ObjectDisposedException is gone
ignore =
    E203,
    W503,
    D100,
    D101,
    D102,
    D105,
    D106,
    D107,
    D400,
    D205,
    D415,
    F821

# Config for flake8-docstrings
docstring-convention = google

# Config for flake8-import-order
import-order-style = smarkets
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.github/CODEOWNERS sha256=7aef8e9fa292887cf4f2317711c24f4cebf8dd85993aad92b3f33cba9ee77aba bytes=117 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nisystemlink-clients-python`
- source_path: `.github/CODEOWNERS`
- sha256: `7aef8e9fa292887cf4f2317711c24f4cebf8dd85993aad92b3f33cba9ee77aba`
- bytes: 117

````text
* @rbell517 @spanglerco @cameronwaterman

/.snyk @ni/security-scanning-owners
/.wiz @ni/security-scanning-owners
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=624cd2c56e079c51f49c42997a7ea7cabc60742c6c69f462acced0decf89ac22 bytes=674 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nisystemlink-clients-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `624cd2c56e079c51f49c42997a7ea7cabc60742c6c69f462acced0decf89ac22`
- bytes: 674

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nisystemlink-clients-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/nisystemlink-clients-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.github/workflows/python-package.yml sha256=4139164f510f6695a43226a659ff39b9d3d3aa4457fd8a9b59eab927ad2c8144 bytes=2902 -->
## FILE: .github/workflows/python-package.yml

- repository: `ni/nisystemlink-clients-python`
- source_path: `.github/workflows/python-package.yml`
- sha256: `4139164f510f6695a43226a659ff39b9d3d3aa4457fd8a9b59eab927ad2c8144`
- bytes: 2902

````yaml
name: Python package

on:
  push:
    branches: [master, main]
  pull_request:
    branches: [master, main]

jobs:
  build-lint-unit-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12', '3.13', '3.14']
    steps:
      - uses: actions/checkout@v4
      - name: Install poetry
        run: pipx install poetry
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "poetry"
      - run: poetry install
      - run: poetry run poe test
      - run: poetry run poe check
      - run: poetry run poe lint
      - run: poetry run poe types
  integration-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12', '3.13', '3.14']
      # Do not run in parallel to limit parallel integration tests stomping on each other
      max-parallel: 1
    steps:
      - uses: actions/checkout@v4
      - name: Install poetry
        run: pipx install poetry
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "poetry"
      - run: poetry install
      - run: >
          poetry run pytest
          -m integration
          --cloud-api-key "${{ secrets.CLOUD_API_KEY }}"
          --enterprise-uri "https://test-api.lifecyclesolutions.ni.com" --enterprise-api-key "${{ secrets.ENTERPRISE_API_KEY }}"
  release:
    runs-on: ubuntu-latest
    needs: [build-lint-unit-test, integration-test]
    if: github.event_name == 'push' && (github.ref == 'refs/heads/master' || github.ref == 'refs/heads/main')
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          token: ${{ secrets.GH_TOKEN }}
      - name: Install poetry
        run: pipx install poetry
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
          cache: "poetry"
      - run: poetry install
      - name: Semantic release
        run: |
          pip install python-semantic-release==7.34.6
          git config --global user.name "github-actions"
          git config --global user.email "action@github.com"
          semantic-release publish
        env:
          # To generate a new token use the following guide, providing access to the "repo" scope.
          # https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
          # Once you update the secret on the repo, ensure you update the master/main protected branch policy
          # to allow your user permission to "bypass required pull requests".
          GH_TOKEN: ${{secrets.GH_TOKEN}}
          REPOSITORY_USERNAME: ${{secrets.REPOSITORY_USERNAME}}
          REPOSITORY_PASSWORD: ${{secrets.PYPI_PASSWORD}}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.gitignore sha256=fcd30a4036e14f18a3c5d872bcf2a07ca6355b721f8ee8a17ec8b66c42d9c172 bytes=112 -->
## FILE: .gitignore

- repository: `ni/nisystemlink-clients-python`
- source_path: `.gitignore`
- sha256: `fcd30a4036e14f18a3c5d872bcf2a07ca6355b721f8ee8a17ec8b66c42d9c172`
- bytes: 112

````text
*.orig
*.swp
*.swo
/_*.py
/*.egg-info/
/.tox
/.venv
/.vscode
__pycache__/
.mypy_cache/
build/
dist/
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.readthedocs.yaml sha256=20dc0d5620c94a5fc89230beeb636894963878f51b6cd54d3455227301301a08 bytes=640 -->
## FILE: .readthedocs.yaml

- repository: `ni/nisystemlink-clients-python`
- source_path: `.readthedocs.yaml`
- sha256: `20dc0d5620c94a5fc89230beeb636894963878f51b6cd54d3455227301301a08`
- bytes: 640

````yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-lts-latest
  tools:
    python: "3.10"

# Build documentation in the docs/ directory with Sphinx
sphinx:
   configuration: docs/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
   - pdf
   - epub

# Optionally declare the Python requirements required to build your docs
python:
   install:
   - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.snyk sha256=652f414303b30e580cd7e541e872c9f2d7b1d2cede3c7ed332641144d1c507ce bytes=135 -->
## FILE: .snyk

- repository: `ni/nisystemlink-clients-python`
- source_path: `.snyk`
- sha256: `652f414303b30e580cd7e541e872c9f2d7b1d2cede3c7ed332641144d1c507ce`
- bytes: 135

````text
# Snyk (https://snyk.io) policy file, patches or ignores known vulnerabilities.
exclude: {}
version: v1.25.1
ignore: {}
patch: {}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=.wiz sha256=2155b67a2ff975bd59a5fda3d0c4d12d4041451e1ef73d916e15f8b2d4a9ab6b bytes=388 -->
## FILE: .wiz

- repository: `ni/nisystemlink-clients-python`
- source_path: `.wiz`
- sha256: `2155b67a2ff975bd59a5fda3d0c4d12d4041451e1ef73d916e15f8b2d4a9ab6b`
- bytes: 388

````text
# Wiz Code global path exclusions for this repository.
#
# NOTE: Both /* and /**/* patterns are required per directory due to a known
# Wiz glob bug (WZ-81029) where /**/* does not match direct children of a
# directory. The /* pattern catches direct children while /**/* catches nested
# files. This duplication can be removed once the bug is fixed.

ignore:
  global_paths: {}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=CHANGELOG.md sha256=4dbadea18154f15c2893d196674918fbf85f34227423921392d967510941e26e bytes=25332 -->
## FILE: CHANGELOG.md

- repository: `ni/nisystemlink-clients-python`
- source_path: `CHANGELOG.md`
- sha256: `4dbadea18154f15c2893d196674918fbf85f34227423921392d967510941e26e`
- bytes: 25332

````markdown
# Changelog

<!--next-version-placeholder-->

## v2.32.1 (2026-05-29)

### Fix

* Fix bad requests when retrying with streams in multi-part requests ([#212](https://github.com/ni/nisystemlink-clients-python/issues/212)) ([`4e34914`](https://github.com/ni/nisystemlink-clients-python/commit/4e3491475ec7ce63d63ea12816b3ba6998795d49))

## v2.32.0 (2026-05-28)

### Feature

* Execute work item API ([#199](https://github.com/ni/nisystemlink-clients-python/issues/199)) ([`fa61f4e`](https://github.com/ni/nisystemlink-clients-python/commit/fa61f4e6bdcdf275f3a615720ef53c02c2533c34))

### Fix

* Align FileClient.search_files docstring with Swagger API documentation ([#205](https://github.com/ni/nisystemlink-clients-python/issues/205)) ([`81d7bf4`](https://github.com/ni/nisystemlink-clients-python/commit/81d7bf4e61dd37db6dc2526b2ca2e1f01ad7926e))

## v2.31.1 (2026-03-12)

### Fix

* Align FileClient.query_files_linq docstring with Swagger API documentation ([#201](https://github.com/ni/nisystemlink-clients-python/issues/201)) ([`378c54d`](https://github.com/ni/nisystemlink-clients-python/commit/378c54dd11b236ace0d937e302da85ee5279cbe6))

## v2.31.0 (2026-02-02)

### Feature

* Example to append pandas df to SystemLink Data Frame Service ([#196](https://github.com/ni/nisystemlink-clients-python/issues/196)) ([`23977c8`](https://github.com/ni/nisystemlink-clients-python/commit/23977c865cb2fd65f2e4c0419a112472a3911e8c))

## v2.30.0 (2026-02-02)

### Feature

* Add Notification Client ([#195](https://github.com/ni/nisystemlink-clients-python/issues/195)) ([`ae4e9c1`](https://github.com/ni/nisystemlink-clients-python/commit/ae4e9c19bfdacdc330f67c9487bd4074559ada7f))

## v2.29.1 (2026-01-22)

### Fix

* Deprecate TestPlanClient as Test Plans APIs are deprecated ([#190](https://github.com/ni/nisystemlink-clients-python/issues/190)) ([`c3092a6`](https://github.com/ni/nisystemlink-clients-python/commit/c3092a6c9eccc323e8fd7e97aa834c25408d25c8))

## v2.29.0 (2026-01-20)

### Feature

* Upload Large File API Methods ([#181](https://github.com/ni/nisystemlink-clients-python/issues/181)) ([`a44feb9`](https://github.com/ni/nisystemlink-clients-python/commit/a44feb9d1f0735e102897cc8c89c81919bec41ec))

## v2.28.0 (2026-01-16)

### Feature

* Add Client for Work Item and Work Item Template APIs ([#189](https://github.com/ni/nisystemlink-clients-python/issues/189)) ([`b34eb60`](https://github.com/ni/nisystemlink-clients-python/commit/b34eb6094d89173de662a86b6c7b959db9a51840))

## v2.27.0 (2026-01-09)

### Feature

* Elastic Search (search-files) API Endpoint ([#180](https://github.com/ni/nisystemlink-clients-python/issues/180)) ([`db1b5d9`](https://github.com/ni/nisystemlink-clients-python/commit/db1b5d9882e529e7b703d102f4b5f24ed4c04b12))

## v2.26.2 (2026-01-08)

### Fix

* Standardize HttpConfiguration use within examples ([#188](https://github.com/ni/nisystemlink-clients-python/issues/188)) ([`990a1b6`](https://github.com/ni/nisystemlink-clients-python/commit/990a1b6b99d440fbed291e96c43687838c266ae6))

## v2.26.1 (2026-01-08)

### Fix

* Bump urllib3 from 2.6.0 to 2.6.3 ([#187](https://github.com/ni/nisystemlink-clients-python/issues/187)) ([`663c6b3`](https://github.com/ni/nisystemlink-clients-python/commit/663c6b33171f35bae8b154235666aef335dcc78c))

## v2.26.0 (2026-01-07)

### Feature

* Pagination helper ([#185](https://github.com/ni/nisystemlink-clients-python/issues/185)) ([`1479b6f`](https://github.com/ni/nisystemlink-clients-python/commit/1479b6f3defdafe8023b29d89548d11527a69d96))

## v2.25.1 (2025-12-23)

### Fix

* Alarm Client Severity Level Documentation Changes ([#184](https://github.com/ni/nisystemlink-clients-python/issues/184)) ([`9282075`](https://github.com/ni/nisystemlink-clients-python/commit/9282075f9ec01d614ec2c21f884f7c8940f856c9))

## v2.25.0 (2025-12-22)

### Feature

* Asset Utilization API methods ([#178](https://github.com/ni/nisystemlink-clients-python/issues/178)) ([`83b5f45`](https://github.com/ni/nisystemlink-clients-python/commit/83b5f45db8a5c45507cf0b8a1bae8d6ff5a539de))

## v2.24.0 (2025-12-22)

### Feature

* Add Client for Alarm API ([#173](https://github.com/ni/nisystemlink-clients-python/issues/173)) ([`722b849`](https://github.com/ni/nisystemlink-clients-python/commit/722b849d6c1eef504f216dba196b9e797a6e4b83))

## v2.23.0 (2025-12-22)

### Feature

* Read Minion ID from Client's salt conf ([#179](https://github.com/ni/nisystemlink-clients-python/issues/179)) ([`c8c05b3`](https://github.com/ni/nisystemlink-clients-python/commit/c8c05b37d33b6f6a91fc2508d5dd25ddb0e699c7))

## v2.22.0 (2025-12-10)

### Feature

* Add optional take to DataFrame Service export table data request model ([#177](https://github.com/ni/nisystemlink-clients-python/issues/177)) ([`2932991`](https://github.com/ni/nisystemlink-clients-python/commit/293299130297ef1ef800ebd94c4d0ab97ae06977))

## v2.21.0 (2025-12-10)

### Feature

* Rev minimum python version to 3.10 and add python 3.14 ([#168](https://github.com/ni/nisystemlink-clients-python/issues/168)) ([`d414904`](https://github.com/ni/nisystemlink-clients-python/commit/d4149043ac2f1eff97cb7cf6e65b771839bd6e3c))

## v2.20.0 (2025-12-01)

### Feature

* DFS support for test result ID, column name queries, and interactive queries ([#164](https://github.com/ni/nisystemlink-clients-python/issues/164)) ([`468ab06`](https://github.com/ni/nisystemlink-clients-python/commit/468ab06efd30179b5c2e0873c417afffe824292d))

## v2.19.5 (2025-12-01)

### Fix

* Fix Test Monitor examples ([#169](https://github.com/ni/nisystemlink-clients-python/issues/169)) ([`b3588b1`](https://github.com/ni/nisystemlink-clients-python/commit/b3588b14821758c685b2bd3efbb05007b4c9f4a2))

## v2.19.4 (2025-10-24)

### Fix

* Update python client example ([#167](https://github.com/ni/nisystemlink-clients-python/issues/167)) ([`561d81f`](https://github.com/ni/nisystemlink-clients-python/commit/561d81f19c51b0781840767b2b86554daad9ee76))

## v2.19.3 (2025-10-22)

### Fix

* Fix typing in examples and tests ([#166](https://github.com/ni/nisystemlink-clients-python/issues/166)) ([`9a846e6`](https://github.com/ni/nisystemlink-clients-python/commit/9a846e6ae3b1348df12b6be1080c002f3a6e7dc1))

## v2.19.2 (2025-09-30)

### Fix

* Rendering of DFS append_table_data doc string ([#161](https://github.com/ni/nisystemlink-clients-python/issues/161)) ([`0c0d92f`](https://github.com/ni/nisystemlink-clients-python/commit/0c0d92fa32cb808757ae6a8aa304f8db8d8be2e3))

## v2.19.1 (2025-09-29)

### Fix

* DFS Arrow example datatypes ([#160](https://github.com/ni/nisystemlink-clients-python/issues/160)) ([`0f9abf7`](https://github.com/ni/nisystemlink-clients-python/commit/0f9abf7543bdebd7143e8215699dae3d9f8cba85))

## v2.19.0 (2025-09-24)

### Feature

* DataFrame client binary ingestion support ([#155](https://github.com/ni/nisystemlink-clients-python/issues/155)) ([`5c9e062`](https://github.com/ni/nisystemlink-clients-python/commit/5c9e062470f1fa4186730957caf716898fe833a0))

## v2.18.1 (2025-09-22)

### Fix

* Revert #158 ([#159](https://github.com/ni/nisystemlink-clients-python/issues/159)) ([`3eddcab`](https://github.com/ni/nisystemlink-clients-python/commit/3eddcab1ae5c77293bef677acb5ecc8dd7f6d9ff))

## v2.18.0 (2025-07-31)

### Feature

* File Client | Linq file query API ([#149](https://github.com/ni/nisystemlink-clients-python/issues/149)) ([`4e2a589`](https://github.com/ni/nisystemlink-clients-python/commit/4e2a5898a6845600d0f4d52d33fb9a040cde5583))

## v2.17.1 (2025-07-23)

### Fix

* Upgrade uplink to v0.10.0 for python 3.10+ to resolve pkg_resources deprecation ([#150](https://github.com/ni/nisystemlink-clients-python/issues/150)) ([`c613a78`](https://github.com/ni/nisystemlink-clients-python/commit/c613a7824f19e25e162b2e8376a066fe63a56981))

## v2.17.0 (2025-07-23)

### Feature

* Add DUT filter and DUT serial number fields in test plans models ([#151](https://github.com/ni/nisystemlink-clients-python/issues/151)) ([`d6b9d68`](https://github.com/ni/nisystemlink-clients-python/commit/d6b9d68c36f5b6089c5d378214a4f54097b87e03))

## v2.16.0 (2025-06-13)

### Feature

* Spec client | Add Get Spec API ([#147](https://github.com/ni/nisystemlink-clients-python/issues/147)) ([`b1ebf7c`](https://github.com/ni/nisystemlink-clients-python/commit/b1ebf7cb77f0be84e1e9a76afe52413c720bf0ea))

## v2.15.0 (2025-06-11)

### Feature

* Add delete API for Artifact client ([#142](https://github.com/ni/nisystemlink-clients-python/issues/142)) ([`22f6515`](https://github.com/ni/nisystemlink-clients-python/commit/22f6515bac2b298fb18468095d9a02c782f4f6fb))

## v2.14.0 (2025-05-30)

### Feature

* Add link files API route in Asset Management Client ([#141](https://github.com/ni/nisystemlink-clients-python/issues/141)) ([`f791138`](https://github.com/ni/nisystemlink-clients-python/commit/f7911380871b9c718c10da697c116b4b90909795))

## v2.13.0 (2025-05-28)

### Feature

* Add Client for Workorders service Test plans and Test plan template APIs ([#137](https://github.com/ni/nisystemlink-clients-python/issues/137)) ([`953686c`](https://github.com/ni/nisystemlink-clients-python/commit/953686c0c98cb23a18491355faa2a47a07e253f1))

## v2.12.0 (2025-05-27)

### Feature

* Added clients for systems management service create virtual system, remove systems and query system API ([#138](https://github.com/ni/nisystemlink-clients-python/issues/138)) ([`f73c04f`](https://github.com/ni/nisystemlink-clients-python/commit/f73c04f944943ae642140e03600b08588f34e195))
* Add Client for Asset Management (Asset) create, delete and query API ([#134](https://github.com/ni/nisystemlink-clients-python/issues/134)) ([`dd9907f`](https://github.com/ni/nisystemlink-clients-python/commit/dd9907fa3618e6b1630e478154e280fa27aa78af))

## v2.11.0 (2025-05-15)

### Feature

* Add retry handling to DataFrameClient ([#116](https://github.com/ni/nisystemlink-clients-python/issues/116)) ([`5f8e096`](https://github.com/ni/nisystemlink-clients-python/commit/5f8e096bf735aab97c9927ab71920b5d770e891f))

## v2.10.0 (2025-05-05)

### Feature

* Upgrade to Pydantic 2.11 ([#129](https://github.com/ni/nisystemlink-clients-python/issues/129)) ([`66eada6`](https://github.com/ni/nisystemlink-clients-python/commit/66eada66ff6d05bdca1e777e288a96a7b89af9ed))

### Fix

* Correct missing None default value for spec condition_type ([#133](https://github.com/ni/nisystemlink-clients-python/issues/133)) ([`be48c7d`](https://github.com/ni/nisystemlink-clients-python/commit/be48c7d90322bc41a74456490d7a6f1b9c96d35e))

## v2.9.1 (2025-04-30)

### Fix

* Bump h11 from 0.14.0 to 0.16.0 ([#132](https://github.com/ni/nisystemlink-clients-python/issues/132)) ([`2e918d6`](https://github.com/ni/nisystemlink-clients-python/commit/2e918d6b8c6daaa7ca1956bff72f0dc41d8be989))
* Prevent string discrete values which are string of numbers from passing as numeric condition values. ([#130](https://github.com/ni/nisystemlink-clients-python/issues/130)) ([`40b68af`](https://github.com/ni/nisystemlink-clients-python/commit/40b68af4f60d779f90748e50c88366c7d6501b63))

## v2.9.0 (2025-04-22)

### Feature

* Make TLS/SSL certificate verification optional ([#126](https://github.com/ni/nisystemlink-clients-python/issues/126)) ([`f8063f9`](https://github.com/ni/nisystemlink-clients-python/commit/f8063f9da81b57298ae0d48aee2f11e59f497b19))

### Fix

* Ignore extra fields in Json Model ([#131](https://github.com/ni/nisystemlink-clients-python/issues/131)) ([`4e835bb`](https://github.com/ni/nisystemlink-clients-python/commit/4e835bbbb8bd5c286acee6757d844f03957e5f05))

## v2.8.0 (2025-03-26)

### Feature

* Update TestMonitorClient, ProductClient, and SpecsClient with retry handling ([#124](https://github.com/ni/nisystemlink-clients-python/issues/124)) ([`4714ec1`](https://github.com/ni/nisystemlink-clients-python/commit/4714ec139fbc224263c392286383895100c86583))

### Fix

* Make condition type optional while querying specs ([#123](https://github.com/ni/nisystemlink-clients-python/issues/123)) ([`9d0d923`](https://github.com/ni/nisystemlink-clients-python/commit/9d0d9239bc769801590ba8a507c0e3cd5f87e12d))

## v2.7.4 (2025-03-25)

### Fix

* Handle none values and column grouping in results/steps dataframe utility ([#119](https://github.com/ni/nisystemlink-clients-python/issues/119)) ([`9eb2087`](https://github.com/ni/nisystemlink-clients-python/commit/9eb20876ffc4bfc02ce5b4712b65a56085b70029))

## v2.7.3 (2025-03-24)

### Fix

* Make testmonitor step examples show up in docs and fix `update_results` example ([#120](https://github.com/ni/nisystemlink-clients-python/issues/120)) ([`dacfdfb`](https://github.com/ni/nisystemlink-clients-python/commit/dacfdfb6864473fd935986edc8d2562df1e28f9a))

## v2.7.2 (2025-03-21)

### Fix

* Error in converting results/steps to dataframe when status is none ([#115](https://github.com/ni/nisystemlink-clients-python/issues/115)) ([`e67d935`](https://github.com/ni/nisystemlink-clients-python/commit/e67d935586f7d2e58c49b865bd8cc3c0d74ead08))

## v2.7.1 (2025-03-19)

### Fix

* Add 429 retries to notebook client ([#109](https://github.com/ni/nisystemlink-clients-python/issues/109)) ([`00e529a`](https://github.com/ni/nisystemlink-clients-python/commit/00e529a25d3fad535c2e54421c98d98b839f85fa))

## v2.7.0 (2025-03-18)

### Feature

* Add client for Notebook & Notebook Execution APIs ([#105](https://github.com/ni/nisystemlink-clients-python/issues/105)) ([`9e2d348`](https://github.com/ni/nisystemlink-clients-python/commit/9e2d348b73850a6b6ff2bf0e4814058d4f0cde1f))

## v2.6.0 (2025-03-14)

### Feature

* Export steps as dataframe ([#103](https://github.com/ni/nisystemlink-clients-python/issues/103)) ([`5535a89`](https://github.com/ni/nisystemlink-clients-python/commit/5535a8949bf9203b2947f109b8dc54e01fd7535d))

## v2.5.1 (2025-03-13)

### Fix

* Delete product created during result client test fixture ([#104](https://github.com/ni/nisystemlink-clients-python/issues/104)) ([`86b0759`](https://github.com/ni/nisystemlink-clients-python/commit/86b07594d64ad92da85e1e8d91e711071eb24ded))

## v2.5.0 (2025-03-13)

### Feature

* Export Specs as Dataframe ([#98](https://github.com/ni/nisystemlink-clients-python/issues/98)) ([`ae1b608`](https://github.com/ni/nisystemlink-clients-python/commit/ae1b608e02ccf349d9e0bcf3ccf036383395759b))

## v2.4.0 (2025-03-11)

### Feature

* Export Results as Dataframe ([#100](https://github.com/ni/nisystemlink-clients-python/issues/100)) ([`1faa54a`](https://github.com/ni/nisystemlink-clients-python/commit/1faa54aae16a6090f20639b42d760af47bb9adc7))

## v2.3.0 (2025-03-07)

### Feature

* Add steps APIs to the testmonitor client ([#96](https://github.com/ni/nisystemlink-clients-python/issues/96)) ([`85a676d`](https://github.com/ni/nisystemlink-clients-python/commit/85a676d000b68233b03339a943834d1054fbf2ab))

## v2.2.0 (2025-03-07)

### Feature

* Export products as dataframe ([#102](https://github.com/ni/nisystemlink-clients-python/issues/102)) ([`e5a41c0`](https://github.com/ni/nisystemlink-clients-python/commit/e5a41c0839cbd2412d613e78ac698f7000c32e99))

## v2.1.0 (2025-03-06)

### Feature

* Add client for SystemLink results API ([#82](https://github.com/ni/nisystemlink-clients-python/issues/82)) ([`53f1188`](https://github.com/ni/nisystemlink-clients-python/commit/53f1188b4c4806819dbd20011c4b69d6f51487f9))

### Fix

* Enable null value for results properties ([#99](https://github.com/ni/nisystemlink-clients-python/issues/99)) ([`cba5106`](https://github.com/ni/nisystemlink-clients-python/commit/cba510629a142bffc8d9c5872d2f7a27bca2e8c3))

## v2.0.0 (2025-03-05)

### Feature

* Add and resolve query projection for products and specs respectively ([#97](https://github.com/ni/nisystemlink-clients-python/issues/97)) ([`e9feff6`](https://github.com/ni/nisystemlink-clients-python/commit/e9feff6dc3e473dd34cbb53739f1c96eb7a8db0e))

### Breaking

* Product and Specification models have been updated to support projections.  - Product client changes--    - `models.Product` now defines all fields as Optional.    - `ProductClient.create_product`'s `products` parameter is now typed      as `models.CreateProductRequest`    - `ProductClient.update_product`'s `products` parameter is now typed      as `models.UpdateProductRequest`  - Specifications client changes--    - `models.Specification` and `models.SpecificationDefinition` now      define all fields as Optional.    - `models.QuerySpecifications` has been renamed `models.PagedSpecifications`      to better align to other clients.    - `models.CreateSpecificationeRequest.specs` is now typed as `models.CreateSpecificationsRequestObject`      instead of `models.SpecificationDefinition`    - `models.UpdateSpecificationeRequest.specs` is now typed as `models.UpdateSpecificationsRequestObject`      instead of `models.Specification` ([`e9feff6`](https://github.com/ni/nisystemlink-clients-python/commit/e9feff6dc3e473dd34cbb53739f1c96eb7a8db0e))

## v1.10.0 (2025-02-13)

### Feature

* Example to upload file to SystemLink ([#81](https://github.com/ni/nisystemlink-clients-python/issues/81)) ([`67bfe2d`](https://github.com/ni/nisystemlink-clients-python/commit/67bfe2dc69565f744a36248cbda15026018d7ad6))

## v1.9.0 (2025-02-06)

### Feature

* Add minimal client implementation for Feeds API ([#73](https://github.com/ni/nisystemlink-clients-python/issues/73)) ([`35d32b5`](https://github.com/ni/nisystemlink-clients-python/commit/35d32b580488b1365165f8c6e0a96e8148169b1d))

## v1.8.1 (2025-02-05)

### Fix

* Update to the latest httpx version ([#88](https://github.com/ni/nisystemlink-clients-python/issues/88)) ([`09e6e59`](https://github.com/ni/nisystemlink-clients-python/commit/09e6e59e1025d0046da08dd9743d0ac3fc0872f2))

## v1.8.0 (2024-11-08)

### Feature

* Add client for SystemLink products API ([#69](https://github.com/ni/nisystemlink-clients-python/issues/69)) ([`d53a9f4`](https://github.com/ni/nisystemlink-clients-python/commit/d53a9f43aee5abbf1e9db084b091390b148478a5))

## v1.7.2 (2024-11-05)

### Fix

* Some spelling errors file tests ([#79](https://github.com/ni/nisystemlink-clients-python/issues/79)) ([`770545e`](https://github.com/ni/nisystemlink-clients-python/commit/770545e6cbb9d90d48f9633dff979cff5c71dc67))

## v1.7.1 (2024-11-04)

### Fix

* Remove SL Cloud from readme and add SLE ([#78](https://github.com/ni/nisystemlink-clients-python/issues/78)) ([`ae12825`](https://github.com/ni/nisystemlink-clients-python/commit/ae12825912ddefa871e81ca7a4e5ee16de216a9b))

## v1.7.0 (2024-10-25)

### Feature

* Add workspace field to httpconfiguration ([#64](https://github.com/ni/nisystemlink-clients-python/issues/64)) ([`b81c84a`](https://github.com/ni/nisystemlink-clients-python/commit/b81c84ada616df9cfe72e7d63e41ae17801af474))

## v1.6.0 (2024-09-17)

### Feature

* Add Client for File Service ([#65](https://github.com/ni/nisystemlink-clients-python/issues/65)) ([`ebdc4c1`](https://github.com/ni/nisystemlink-clients-python/commit/ebdc4c1adf50f71498d0ce3446402dff55eef6ca))

## v1.5.0 (2024-09-09)

### Feature

* Add client for Artifacts API ([#70](https://github.com/ni/nisystemlink-clients-python/issues/70)) ([`0ada3d7`](https://github.com/ni/nisystemlink-clients-python/commit/0ada3d7c765e1b5d7fabfa4661f15d38c71c7295))

## v1.4.3 (2024-08-08)

### Fix

* Make SpecClient() work with default values for optional args ([#68](https://github.com/ni/nisystemlink-clients-python/issues/68)) ([`fb60801`](https://github.com/ni/nisystemlink-clients-python/commit/fb60801d4093ef66c92e7b2c6e4e1f5fe45bb2f6))

## v1.4.2 (2024-07-15)

### Fix

* Bump setuptools from 67.6.0 to 70.0.0 ([#67](https://github.com/ni/nisystemlink-clients-python/issues/67)) ([`39b13f0`](https://github.com/ni/nisystemlink-clients-python/commit/39b13f0c4b3ed3377e54dd6c4a3237c7e9304e48))

## v1.4.1 (2024-07-08)

### Fix

* Bump certifi from 2023.7.22 to 2024.7.4 ([#66](https://github.com/ni/nisystemlink-clients-python/issues/66)) ([`0fc4ff7`](https://github.com/ni/nisystemlink-clients-python/commit/0fc4ff766895a70be4c0e518ba98db0e69beab43))

## v1.4.0 (2024-06-18)

### Feature

* Make DataFrame and Spec clients compatible with SystemLink Client http configuration ([#61](https://github.com/ni/nisystemlink-clients-python/issues/61)) ([`7954e14`](https://github.com/ni/nisystemlink-clients-python/commit/7954e1479a0e421cfe3e44c741e69186e2f0c45f))

## v1.3.1 (2024-05-21)

### Fix

* Bump requests from 2.31.0 to 2.32.0 ([#60](https://github.com/ni/nisystemlink-clients-python/issues/60)) ([`fe9060b`](https://github.com/ni/nisystemlink-clients-python/commit/fe9060b1783e4022cb493a96bd42bb052526c487))

## v1.3.0 (2024-04-19)

### Feature

* Test monitor API information routes client ([#57](https://github.com/ni/nisystemlink-clients-python/issues/57)) ([`4b9cc61`](https://github.com/ni/nisystemlink-clients-python/commit/4b9cc6135c0fa4d99e8c93201f83d3a17a817239))

## v1.2.1 (2024-04-12)

### Fix

* Bump idna from 3.4 to 3.7 ([#56](https://github.com/ni/nisystemlink-clients-python/issues/56)) ([`008f523`](https://github.com/ni/nisystemlink-clients-python/commit/008f523063b1c8afd559cc0d14e2199137814584))

## v1.2.0 (2024-04-04)

### Feature

* Add spec client, examples, and docs ([#53](https://github.com/ni/nisystemlink-clients-python/issues/53)) ([`7c88535`](https://github.com/ni/nisystemlink-clients-python/commit/7c8853587cbe1ae21b5039e59d3f1d125f851288))

## v1.1.2 (2023-10-03)

### Fix

* Bump urllib3 from 1.26.15 to 1.26.17 ([#49](https://github.com/ni/nisystemlink-clients-python/issues/49)) ([`8d86216`](https://github.com/ni/nisystemlink-clients-python/commit/8d86216d760bfc860a9e504b04ee62d4cada193f))

## v1.1.1 (2023-09-22)

### Fix

* Bump certifi from 2022.12.7 to 2023.7.22 ([#47](https://github.com/ni/nisystemlink-clients-python/issues/47)) ([`79f6aad`](https://github.com/ni/nisystemlink-clients-python/commit/79f6aadcbe545143051386f7fcc7b7d38613a36e))

## v1.1.0 (2023-04-06)
### Feature
* Add CSV export capability to DataFrameClient ([#45](https://github.com/ni/nisystemlink-clients-python/issues/45)) ([`5cc2d01`](https://github.com/ni/nisystemlink-clients-python/commit/5cc2d01c0655fdd8ab1d5e1895d5be38020c9cd0))

## v1.0.2 (2023-03-08)
### Fix
* Correct spelling for model class TableMetadataModification ([#44](https://github.com/ni/nisystemlink-clients-python/issues/44)) ([`30c760c`](https://github.com/ni/nisystemlink-clients-python/commit/30c760c2eb9af8e17ddb8c6730f6ef5aae20e973))

## v1.0.1 (2023-01-26)
### Fix
* Fix various documentation issues ([#42](https://github.com/ni/nisystemlink-clients-python/issues/42)) ([`872e9ac`](https://github.com/ni/nisystemlink-clients-python/commit/872e9accdc959e8fc8a400518bb74ba8fb0cf30c))

## v1.0.0 (2022-12-15)
### Breaking
* Preparation for 1.0.0 release. ([`c61925c`](https://github.com/ni/nisystemlink-clients-python/commit/c61925c902ebcdf6e1e4c8c24905caf0c304cb31))

### Documentation
* Add examples and update getting started ([#40](https://github.com/ni/nisystemlink-clients-python/issues/40)) ([`1d76480`](https://github.com/ni/nisystemlink-clients-python/commit/1d76480f6bf3eddf0017f467d68473131e4850a0))

## v0.9.0 (2022-12-06)
### Feature
* Query for data ([#37](https://github.com/ni/nisystemlink-clients-python/issues/37)) ([`7f0acbe`](https://github.com/ni/nisystemlink-clients-python/commit/7f0acbec9c9033a088259172712e9c2532594d2e))

## v0.8.0 (2022-12-05)
### Feature
* Read and append table data ([#36](https://github.com/ni/nisystemlink-clients-python/issues/36)) ([`d7a7642`](https://github.com/ni/nisystemlink-clients-python/commit/d7a7642f12543be4c1393435c9fd11604288a17f))

## v0.7.0 (2022-12-02)
### Feature
* Add modify_tables method ([#35](https://github.com/ni/nisystemlink-clients-python/issues/35)) ([`7be03be`](https://github.com/ni/nisystemlink-clients-python/commit/7be03be811d7c7d239e69883e00b765f8a316881))

## v0.6.0 (2022-12-01)
### Feature
* Table multi-delete + refactoring core libs ([#34](https://github.com/ni/nisystemlink-clients-python/issues/34)) ([`ebe9ce3`](https://github.com/ni/nisystemlink-clients-python/commit/ebe9ce3c4d6a84049d38806b2966637ca318629d))

## v0.5.0 (2022-11-30)
### Feature
* Method to update table metadata ([#33](https://github.com/ni/nisystemlink-clients-python/issues/33)) ([`6e72835`](https://github.com/ni/nisystemlink-clients-python/commit/6e7283512d9d02fed8238811247d3d0e706a2c4b))

## v0.4.0 (2022-11-28)
### Feature
* Add query-tables method ([#32](https://github.com/ni/nisystemlink-clients-python/issues/32)) ([`8b8afef`](https://github.com/ni/nisystemlink-clients-python/commit/8b8afef8ae5ccd9f93017ff3e5629d6cbeec3f58))

## v0.3.0 (2022-11-19)
### Feature
* Implement create/get/delete/list table metadata methods ([#28](https://github.com/ni/nisystemlink-clients-python/issues/28)) ([`7cbf7e8`](https://github.com/ni/nisystemlink-clients-python/commit/7cbf7e8f9f46ece55ceddd8f48f55a91c79a2e24))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=conftest.py sha256=3921923ac3bc27f2450b1d46ad2a82b1cc38adb640af03d82625661ea2c30907 bytes=3677 -->
## FILE: conftest.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `conftest.py`
- sha256: `3921923ac3bc27f2450b1d46ad2a82b1cc38adb640af03d82625661ea2c30907`
- bytes: 3677

````python
# -*- coding: utf-8 -*-

import pytest  # type: ignore
from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Extra


def pytest_addoption(parser):
    """Register command line flags that tell us how to connect to the web server.

    Note that command line flags can also be added to the ``[pytest]`` section of
    ``tox.ini``, in an ``addopts`` setting.
    """
    parser.addoption("--cloud-api-key", help="The cloud API key", type=str)
    parser.addoption("--enterprise-uri", help="The enterprise URI", type=str)
    parser.addoption("--enterprise-api-key", help="The enterprise API key", type=str)
    parser.addoption("--web-server-url", help="The web server's URL", type=str)
    parser.addoption("--web-server-user", help="The web server's user", type=str)
    parser.addoption(
        "--web-server-password", help="The web server's password", type=str
    )


def pytest_collection_modifyitems(items):
    """Modify the collected tests."""
    for item in items:
        # The integration tests are explicitly marked; everything else is a unit test.
        if not list(item.iter_markers("integration")):
            item.add_marker(pytest.mark.unit)


@pytest.fixture(scope="class")
def cloud_config(pytestconfig):
    """Fixture to get a CloudHttpConfiguration for testing.

    This requires the --cloud-api-key command line flag, or else skips the test.
    """
    api_key = pytestconfig.getoption("cloud_api_key", default=None)
    if api_key:
        return core.CloudHttpConfiguration(api_key)
    else:
        pytest.skip("--cloud-api-key setting not found")


@pytest.fixture(scope="class")
def server_config(pytestconfig):
    """Fixture to get an HttpConfiguration for testing.

    This uses the --web-server-url, --web-server-user, and --web-server-password command
    line options, if any are given. If none of them are given, this will try to get the
    default localhost configuration stored in the local Skyline/HttpConfigurations/
    directory. If that is missing, too, the test is skipped.
    """
    settings = {}
    for setting in ("url", "user", "password"):
        val = pytestconfig.getoption("web_server_" + setting, default=None)
        if val:
            settings[setting] = val
    if settings:
        return core.HttpConfiguration(
            settings.get("url", "http://localhost"),
            username=settings.get("user", "admin"),
            password=settings.get("password", "admin"),
        )
    try:
        return core.HttpConfigurationManager.get_configuration(
            core.HttpConfigurationManager.HTTP_LOCALHOST_CONFIGURATION_ID, False
        )
    except core.ApiException:
        pytest.skip("--web-server-* settings not found, nor localhost config file")


@pytest.fixture(scope="class")
def enterprise_config(pytestconfig):
    """Fixture to get a HttpConfiguration for testing Enterprise integration.

    This requires the --enterprise-uri and --enterprise-api-key command line flag, or else skips the test.
    """
    uri = pytestconfig.getoption("enterprise_uri", default=None)
    api_key = pytestconfig.getoption("enterprise_api_key", default=None)
    if uri and api_key:
        return core.HttpConfiguration(uri, api_key)
    else:
        pytest.skip("--enterprise-uri or --enterprise-api-key setting not found")


@pytest.fixture(scope="session", autouse=True)
def pydantic_forbid_extra_fields():
    """Fixture to disable allowing extra fields in our Pydantic models."""
    JsonModel.model_config.update(extra='forbid')
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=CONTRIBUTING.md sha256=fabd162b35aa8bf9fa68dd66bc54e1d7c3f2dd5e80358397667eeaa739fc3191 bytes=5201 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nisystemlink-clients-python`
- source_path: `CONTRIBUTING.md`
- sha256: `fabd162b35aa8bf9fa68dd66bc54e1d7c3f2dd5e80358397667eeaa739fc3191`
- bytes: 5201

````markdown
# Contributing to *nisystemlink-clients-python*

Contributions to *nisystemlink-clients-python* are welcome from all!

*nisystemlink-clients-python* is managed via [git](https://git-scm.com), with
the canonical upstream repository hosted on
[GitHub](https://github.com/ni/nisystemlink-clients-python/).

*nisystemlink-clients-python* follows a pull-request model for development.  If
you wish to contribute, you will need to create a GitHub account, fork this
project, push a branch with your changes to your project, and then submit a
pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/)
for more details.

**Important:** Commit titles and messages should adhere to the
[Conventional Commits style](https://www.conventionalcommits.org/en/v1.0.0/#summary)
to ensure proper semantic versioning.

## Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Run the unit tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   [GitHub issues page](https://github.com/ni/nisystemlink-clients-python/issues).
3. Write new tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
4. Make your change.
5. Run all the unit tests again (which include the tests you just added),
   and confirm that they all pass.
6. Send a GitHub Pull Request to the main repository's master branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.

## Testing

Before running any tests, you must have a supported version of Python (3.10+) and [Poetry](https://python-poetry.org/docs/) installed locally.

It is also helpful to install SystemLink Server and configure the NI Web Server
to run on localhost.

To install all development dependencies required:

```
poetry install
```

To run commands and scripts, spawn a shell within the virtual environment managed by Poetry:

```sh
poetry shell
# Alternatively, you can prefix commands with "poetry run"
poetry run pytest
```

There are a handful of helpful tasks in the `[tool.poe.tasks]` section of the `pyproject.toml` file. These can be run using [Poe](https://github.com/nat-n/poethepoet) like so:

```
poe types
```

To run all tests in place with your current python environment setup:

```
pytest
```

To only run the tests in one particular folder, run

```
pytest tests/myfolder
```

To run the SystemLink Cloud tests,
[create an API key](https://www.ni.com/documentation/en/systemlink-cloud/latest/manual/creating-an-api-key/)
and then run

```
pytest -m cloud --cloud-api-key XXXXX
```

To run the SystemLink Enterprise tests, obtain a session API key from the
[main-test](https://test.lifecyclesolutions.ni.com/) cluster and then run

```
pytest -m enterprise --enterprise-uri "https://test-api.lifecyclesolutions.ni.com" --enterprise-api-key XXXXX
```

It is important to note that depending on the terminal you are using,
you may need to escape special characters in the API key.

## Security scanning

**Contributors within NI/Emerson**: See the [security scanning reference](https://dev.azure.com/ni/DevCentral/_wiki/wikis/Stratus/160265/Security-scanning-reference) for information on security scanning tools, workflows, and best practices.

**Contributors outside of NI/Emerson**: If you are having issues resolving a vulnerability identified on your PR, consult with a code owner to understand your options for resolution.

## Developer Certificate of Origin (DCO)

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

See [LICENSE](https://github.com/ni/nisystemlink-clients-python/blob/master/LICENSE)
for details about how *nisystemlink-clients-python* is licensed.
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/alarm.rst sha256=37e07eaa937643a1ce8ae8d9789c83a8843bf949af38b698dde22c8f869bb0ac bytes=500 -->
## FILE: docs/api_reference/alarm.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/alarm.rst`
- sha256: `37e07eaa937643a1ce8ae8d9789c83a8843bf949af38b698dde22c8f869bb0ac`
- bytes: 500

````rst
.. _api_alarm_page:

nisystemlink.clients.alarm
==========================

.. autoclass:: nisystemlink.clients.alarm.AlarmClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_or_update_alarm
   .. automethod:: get_alarm
   .. automethod:: delete_alarm
   .. automethod:: delete_alarms
   .. automethod:: acknowledge_alarms
   .. automethod:: query_alarms

.. automodule:: nisystemlink.clients.alarm.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/artifact.rst sha256=78ee1372dc6a11e9055460256d4d016dc77a9418cd3bd697d31efe6b3592e950 bytes=402 -->
## FILE: docs/api_reference/artifact.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/artifact.rst`
- sha256: `78ee1372dc6a11e9055460256d4d016dc77a9418cd3bd697d31efe6b3592e950`
- bytes: 402

````rst
.. _api_tag_page:

nisystemlink.clients.artifact
======================

.. autoclass:: nisystemlink.clients.artifact.ArtifactClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: upload_artifact
   .. automethod:: download_artifact
   .. automethod:: delete_artifact

.. automodule:: nisystemlink.clients.artifact.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/assetmanagement.rst sha256=d27cc0fa9da9f1d1ab3c57b738f063f78ba36d42ca279cbefeec1b9bd600fc51 bytes=620 -->
## FILE: docs/api_reference/assetmanagement.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/assetmanagement.rst`
- sha256: `d27cc0fa9da9f1d1ab3c57b738f063f78ba36d42ca279cbefeec1b9bd600fc51`
- bytes: 620

````rst
.. _api_tag_page:

nisystemlink.clients.assetmanagement
======================

.. autoclass:: nisystemlink.clients.assetmanagement.AssetManagementClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_assets
   .. automethod:: query_assets
   .. automethod:: delete_assets
   .. automethod:: link_files
   .. automethod:: start_utilization
   .. automethod:: utilization_heartbeat
   .. automethod:: end_utilization
   .. automethod:: query_asset_utilization_history

.. automodule:: nisystemlink.clients.assetmanagement.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/core.rst sha256=ba46919c3ea016c2aae8e955843cccdb623c227ee813447fdc65dfe4b6f6cb04 bytes=273 -->
## FILE: docs/api_reference/core.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/core.rst`
- sha256: `ba46919c3ea016c2aae8e955843cccdb623c227ee813447fdc65dfe4b6f6cb04`
- bytes: 273

````rst
.. _api_core_page:

nisystemlink.clients.core
=======================

.. automodule:: nisystemlink.clients.core
   :members:
   :inherited-members:
   :imported-members:
   
.. automodule:: nisystemlink.clients.core.helpers
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/dataframe.rst sha256=f7dc30ad0544c7f6189db1705211f1d7f009c04a38c5eed32244ace5ba70d767 bytes=1803 -->
## FILE: docs/api_reference/dataframe.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/dataframe.rst`
- sha256: `f7dc30ad0544c7f6189db1705211f1d7f009c04a38c5eed32244ace5ba70d767`
- bytes: 1803

````rst
.. _api_tag_page:

nisystemlink.clients.dataframe
======================

.. autoclass:: nisystemlink.clients.dataframe.DataFrameClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: api_info
   .. automethod:: list_tables
   .. automethod:: create_table
   .. automethod:: query_tables
   .. automethod:: get_table_metadata
   .. automethod:: modify_table
   .. automethod:: delete_table
   .. automethod:: delete_tables
   .. automethod:: modify_tables
   .. automethod:: get_table_data
   .. automethod:: append_table_data
   .. automethod:: query_table_data
   .. automethod:: export_table_data
   .. automethod:: query_decimated_data

.. automodule:: nisystemlink.clients.dataframe.models
   :members:
   :imported-members:

Arrow / JSON Ingestion Notes
----------------------------
``append_table_data`` accepts multiple data forms:

* ``AppendTableDataRequest`` (JSON)
* ``DataFrame`` model (JSON)
* Single ``pyarrow.RecordBatch`` (Arrow IPC)
* Iterable of ``pyarrow.RecordBatch`` (Arrow IPC)
* ``None`` with ``end_of_data`` (flush only)

Arrow support is optional and requires installing the ``pyarrow`` extra::

   pip install "nisystemlink-clients[pyarrow]"

If ``pyarrow`` is not installed and a RecordBatch (or iterable) is passed, a
``RuntimeError`` is raised. When Arrow is used, the batches are serialized into
an IPC stream and sent with content type
``application/vnd.apache.arrow.stream``; the ``end_of_data`` flag is sent as a
query parameter. JSON ingestion places ``endOfData`` in the request body.

If the target SystemLink DataFrame Service does not yet support Arrow and
responds with HTTP 400, the client raises an explanatory ``ApiException``
advising to upgrade or fall back to JSON ingestion.
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/feeds.rst sha256=dbe8419160620009d140322884b79656c319d5998801c5a2db7d60a9d9fc989d bytes=454 -->
## FILE: docs/api_reference/feeds.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/feeds.rst`
- sha256: `dbe8419160620009d140322884b79656c319d5998801c5a2db7d60a9d9fc989d`
- bytes: 454

````rst
.. _api_tag_page:

nisystemlink.clients.feeds
======================

.. autoclass:: nisystemlink.clients.feeds.FeedsClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_feed
   .. automethod:: query_feeds
   .. automethod:: upload_package
   .. automethod:: upload_package_content
   .. automethod:: delete_feed

.. automodule:: nisystemlink.clients.feeds.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/file.rst sha256=4bc5fa1432bbe0030fb5906b956e1e7a4a7726ee02d62a70c95689a8dd48025c bytes=700 -->
## FILE: docs/api_reference/file.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/file.rst`
- sha256: `4bc5fa1432bbe0030fb5906b956e1e7a4a7726ee02d62a70c95689a8dd48025c`
- bytes: 700

````rst
.. _api_tag_page:

nisystemlink.clients.file
======================

.. autoclass:: nisystemlink.clients.file.FileClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: api_info
   .. automethod:: get_files
   .. automethod:: query_files_linq
   .. automethod:: search_files
   .. automethod:: delete_file
   .. automethod:: delete_files
   .. automethod:: upload_file
   .. automethod:: download_file
   .. automethod:: update_metadata
   .. automethod:: start_upload_session
   .. automethod:: append_to_upload_session
   .. automethod:: finish_upload_session

.. automodule:: nisystemlink.clients.file.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/notebook.rst sha256=88bc4b487c7a39f3be3b3846f4ee1cedb592a2b808735891aa27e30a8a6db5c3 bytes=631 -->
## FILE: docs/api_reference/notebook.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/notebook.rst`
- sha256: `88bc4b487c7a39f3be3b3846f4ee1cedb592a2b808735891aa27e30a8a6db5c3`
- bytes: 631

````rst
.. _api_tag_page:

nisystemlink.clients.notebook
======================

.. autoclass:: nisystemlink.clients.notebook.NotebookClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: get_notebook
   .. automethod:: update_notebook
   .. automethod:: delete_notebook
   .. automethod:: create_notebook
   .. automethod:: query_notebooks
   .. automethod:: get_notebook_content
   .. automethod:: create_executions
   .. automethod:: get_execution_by_id
   .. automethod:: query_executions


.. automodule:: nisystemlink.clients.notebook.models
    :members:
    :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/notification.rst sha256=1915a592031618d783e2110a542695aac5eb5ce40b35123c8eb4ab4463b31cfc bytes=377 -->
## FILE: docs/api_reference/notification.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/notification.rst`
- sha256: `1915a592031618d783e2110a542695aac5eb5ce40b35123c8eb4ab4463b31cfc`
- bytes: 377

````rst
.. _api_notification_page:

nisystemlink.clients.notification
==========================

.. autoclass:: nisystemlink.clients.notification.NotificationClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: apply_dynamic_notification_strategy

.. automodule:: nisystemlink.clients.notification.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/product.rst sha256=42f2d77f4bdae91053406d9bf06426b1b0afaa4d82fe7a3c8d3dd7e31d986c5f bytes=612 -->
## FILE: docs/api_reference/product.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/product.rst`
- sha256: `42f2d77f4bdae91053406d9bf06426b1b0afaa4d82fe7a3c8d3dd7e31d986c5f`
- bytes: 612

````rst
.. _api_tag_page:

nisystemlink.clients.product
======================

.. autoclass:: nisystemlink.clients.product.ProductClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_products
   .. automethod:: get_products
   .. automethod:: query_products
   .. automethod:: query_product_values
   .. automethod:: update_products
   .. automethod:: delete_product
   .. automethod:: delete_products

.. automodule:: nisystemlink.clients.product.models
   :members:
   :imported-members:

.. automodule:: nisystemlink.clients.product.utilities
   :members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/spec.rst sha256=0c446f3f136e713251970055bd2abe5824af20f6436f3fdd2a7fe6a62472aadc bytes=467 -->
## FILE: docs/api_reference/spec.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/spec.rst`
- sha256: `0c446f3f136e713251970055bd2abe5824af20f6436f3fdd2a7fe6a62472aadc`
- bytes: 467

````rst
.. _api_tag_page:

nisystemlink.clients.spec
======================

.. autoclass:: nisystemlink.clients.spec.SpecClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: api_info
   .. automethod:: create_specs
   .. automethod:: delete_specs
   .. automethod:: query_specs
   .. automethod:: update_specs
   .. automethod:: get_spec

.. automodule:: nisystemlink.clients.spec.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/systems.rst sha256=033598f76bbfa8674d01719bd1d767c1c7b15c0de4ae756c313b42feede1324e bytes=398 -->
## FILE: docs/api_reference/systems.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/systems.rst`
- sha256: `033598f76bbfa8674d01719bd1d767c1c7b15c0de4ae756c313b42feede1324e`
- bytes: 398

````rst
.. _api_tag_page:

nisystemlink.clients.systems
======================

.. autoclass:: nisystemlink.clients.spec.SystemsClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_virtual_system
   .. automethod:: remove_systems
   .. automethod:: query_systems

.. automodule:: nisystemlink.clients.systems.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/tag.rst sha256=2198fc07e25755210dc284c2c6a4c9719e9e1becfdea8b5d1e9e328049f9ccb8 bytes=176 -->
## FILE: docs/api_reference/tag.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/tag.rst`
- sha256: `2198fc07e25755210dc284c2c6a4c9719e9e1becfdea8b5d1e9e328049f9ccb8`
- bytes: 176

````rst
.. _api_tag_page:

nisystemlink.clients.tag
======================

.. automodule:: nisystemlink.clients.tag
   :members:
   :inherited-members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/test_plan.rst sha256=5683c3d2ef930c0b43e37e0b25c9757aa0d2d13f458a87a71b745945d9186641 bytes=814 -->
## FILE: docs/api_reference/test_plan.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/test_plan.rst`
- sha256: `5683c3d2ef930c0b43e37e0b25c9757aa0d2d13f458a87a71b745945d9186641`
- bytes: 814

````rst
.. _api_tag_page:

nisystemlink.clients.test_plan
======================

.. deprecated:: 2.29.1
   The Test Plans API will be removed in the future. 
   Use :class:`~nisystemlink.clients.work_item.WorkItemClient` instead.

.. autoclass:: nisystemlink.clients.test_plan.TestPlanClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_test_plans
   .. automethod:: delete_test_plans
   .. automethod:: query_test_plans
   .. automethod:: schedule_test_plans
   .. automethod:: update_test_plans
   .. automethod:: get_test_plan
   .. automethod:: create_test_plan_templates
   .. automethod:: query_test_plan_templates
   .. automethod:: delete_test_plan_templates

.. automodule:: nisystemlink.clients.test_plan.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/testmonitor.rst sha256=c3e0c95cd4332656a708c80fe639553045c58fd448f5a4115b76111246fe6075 bytes=809 -->
## FILE: docs/api_reference/testmonitor.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/testmonitor.rst`
- sha256: `c3e0c95cd4332656a708c80fe639553045c58fd448f5a4115b76111246fe6075`
- bytes: 809

````rst
.. _api_tag_page:

nisystemlink.clients.testmonitor
======================

.. autoclass:: nisystemlink.clients.testmonitor.TestMonitorClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_results
   .. automethod:: get_results
   .. automethod:: query_results
   .. automethod:: query_result_values
   .. automethod:: update_results
   .. automethod:: delete_result
   .. automethod:: delete_results
   .. automethod:: create_steps
   .. automethod:: query_steps
   .. automethod:: query_step_values
   .. automethod:: delete_steps
   .. automethod:: delete_step
   .. automethod:: update_steps
   .. automethod:: get_steps
   .. automethod:: get_step

.. automodule:: nisystemlink.clients.testmonitor.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference/work_item.rst sha256=892562d341171896579b4813adcc331f0daf3946e6f15e33a75cf9b17d7f9819 bytes=761 -->
## FILE: docs/api_reference/work_item.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference/work_item.rst`
- sha256: `892562d341171896579b4813adcc331f0daf3946e6f15e33a75cf9b17d7f9819`
- bytes: 761

````rst
.. _api_work_item_page:

nisystemlink.clients.work_item
==============================

.. autoclass:: nisystemlink.clients.work_item.WorkItemClient
   :exclude-members: __init__

   .. automethod:: __init__
   .. automethod:: create_work_items
   .. automethod:: query_work_items
   .. automethod:: get_work_item
   .. automethod:: update_work_items
   .. automethod:: schedule_work_items
   .. automethod:: delete_work_items
   .. automethod:: execute_work_item
   .. automethod:: create_work_item_templates
   .. automethod:: query_work_item_templates
   .. automethod:: update_work_item_templates
   .. automethod:: delete_work_item_templates

.. automodule:: nisystemlink.clients.work_item.models
   :members:
   :imported-members:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/api_reference.rst sha256=787718e59eb8e901e4a2e0e082a2fde0f986ff4261f8497532dd9504b2b9d5eb bytes=631 -->
## FILE: docs/api_reference.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/api_reference.rst`
- sha256: `787718e59eb8e901e4a2e0e082a2fde0f986ff4261f8497532dd9504b2b9d5eb`
- bytes: 631

````rst
.. _api_reference_page:

API Reference
==============

.. toctree::
   :maxdepth: 4
   :caption: Table of Contents

   api_reference/core
   api_reference/alarm
   api_reference/tag
   api_reference/product
   api_reference/testmonitor
   api_reference/dataframe
   api_reference/spec
   api_reference/file
   api_reference/notebook
   api_reference/feeds
   api_reference/assetmanagement
   api_reference/systems
   api_reference/work_item
   api_reference/test_plan
   api_reference/artifact
   api_reference/notification

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/cleanup.py sha256=6d863cbf891957b2d4b4226640f8a33ca2750c4351605149d3235b297cd11af7 bytes=4024 -->
## FILE: docs/cleanup.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/cleanup.py`
- sha256: `6d863cbf891957b2d4b4226640f8a33ca2750c4351605149d3235b297cd11af7`
- bytes: 4024

````python
# -*- coding: utf-8 -*-

"""Sphinx extension to clean up autodoc output."""

import inspect
import re

import docutils.nodes as nodes


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
        line = modify_systemlink_paths(line)

        # Sphinx errors if it tries to reference a TypeVar variable.
        # (https://github.com/agronholm/sphinx-autodoc-typehints/issues/39)
        # So for now we'll need to handle them ourselves.
        line = line.replace("\\[\\~_Any]", "")
        line = re.sub(r"\b_Any\b", "typing.Any", line)

        # Don't abbreviate external classes (via "~"), except typing.* classes.
        line = re.sub(r"~(?!typing\.|systemlink\.)(?=[a-z]\w*\.)", "", line)

        lines[i] = line


def modify_systemlink_paths(s: str) -> str:
    """Modify nisystemlink.* paths in the given string to hide implementation modules.

    Examples:
        >>> # Basic usage
        >>> modify_systemlink_paths("nisystemlink.foo._abc.Abc")
        'nisystemlink.foo.Abc'

        >>> # Modify all paths in the string
        >>> modify_systemlink_paths(" nisystemlink.f._abc.Abc nisystemlink.f._xyz.Xyz ")
        ' nisystemlink.f.Abc nisystemlink.f.Xyz '

        >>> # Don't change _internal or _core paths
        >>> modify_systemlink_paths("nisystemlink.foo._internal._abc.Abc")
        'nisystemlink.foo._internal._abc.Abc'
        >>> modify_systemlink_paths("nisystemlink.foo._core._abc.Abc")
        'nisystemlink.foo._core._abc.Abc'
    """
    return re.sub(r"(?<!\._internal)(?<!\._core)\._(?!internal|core)\w+.", ".", s)


def _missing_reference(app, env, node, contnode):
    target = node["reftarget"]
    if target.startswith("nisystemlink."):
        # For types that are parameters of overloaded functions, the process-docstring
        # code above will not have seen them; so do the appropriate string replacements
        # here, too.
        refid = modify_systemlink_paths(target)
        if refid == target:
            # If the rename didn't change the string, there must be some other issue.
            # Let the calling code raise a warning/error.
            return None

        # Use just the class name (as if the "~" prefix were applied).
        name = target.rsplit(".", 1)[1]

        return nodes.reference(contnode.rawsource, name, refid=refid)


def setup(app):
    """Entry point for Sphinx extensions."""
    app.connect("autodoc-skip-member", _skip_member)
    app.connect("autodoc-process-docstring", _process_docstring)
    app.connect("missing-reference", _missing_reference, priority=1000)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/conf.py sha256=cbd66e53dcf1525fd9752222e7060930bd4c2c20e91fb7871ff8df487cefa3b3 bytes=1748 -->
## FILE: docs/conf.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/conf.py`
- sha256: `cbd66e53dcf1525fd9752222e7060930bd4c2c20e91fb7871ff8df487cefa3b3`
- bytes: 1748

````python
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# --------------------------------------------------------------------------------------

project = "nisystemlink"
copyright = "2020, National Instruments"
author = "National Instruments"

# The short X.Y version
version = "0.1"
# The full version, including alpha/beta/rc tags
release = "0.1.4"

# --------------------------------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.autodoc_pydantic",
    "docs.cleanup",
]
master_doc = "index"

html_theme = "sphinx_rtd_theme"
html_extra_path = [
    "../LICENSE",
]
nitpicky = True
nitpick_ignore = [
    ("py:class", "datetime.datetime"),
    ("py:class", "datetime.timedelta"),
    ("py:class", "pathlib.Path"),
    ("py:data", "typing.Any"),
    ("py:data", "typing.Awaitable"),
    ("py:data", "typing.Dict"),
    ("py:data", "typing.Iterable"),
    ("py:data", "typing.List"),
    ("py:data", "typing.Optional"),
    ("py:data", "typing.Sequence"),
    ("py:data", "typing.Tuple"),
    ("py:data", "typing.Union"),
]
autodoc_default_options = {
    "special-members": "__init__",
    "no-private-members": True,
}
# Don't let napoleon force methods to be included in the docs; use autodoc flags and our
# own docs.cleanup module for that.
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

# Configuration for https://autodoc-pydantic.readthedocs.io
autodoc_pydantic_model_show_config_summary = False
autodoc_pydantic_field_show_alias = False
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/getting_started.rst sha256=439e26d057bf88e527762b992abd3e55b237cdd86f1e6cfc84000bd5df5572e2 bytes=15356 -->
## FILE: docs/getting_started.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/getting_started.rst`
- sha256: `439e26d057bf88e527762b992abd3e55b237cdd86f1e6cfc84000bd5df5572e2`
- bytes: 15356

````rst
.. _getting_started:

Getting Started
===============

Alarm API
---------

Overview
~~~~~~~~

The :class:`.AlarmClient` class is the primary entry point of the Alarm API.

When constructing an :class:`.AlarmClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.AlarmClient` use the
default connection. The default connection depends on your environment.

With an :class:`.AlarmClient` object, you can:

* Create and update alarm instances using :meth:`~.AlarmClient.create_or_update_alarm`

  * Alarms have two key identifiers:
  
    * ``alarm_id``: A user-defined identifier for the alarm type
    * ``instance_id``: A server-generated unique identifier for each alarm occurrence
  
  * Create alarm transitions (SET, CLEAR) to track alarm state changes

* Query alarms with :meth:`~.AlarmClient.query_alarms`

  * Filter alarms using Dynamic LINQ expressions
  * Control which transitions are returned (most recent only or all)
  * Sort and paginate results

* Get a specific alarm by its instance_id using :meth:`~.AlarmClient.get_alarm`

* Acknowledge alarms by its instance_id using :meth:`~.AlarmClient.acknowledge_alarms`

  * Optionally force-clear alarms when acknowledging

* Delete alarms using :meth:`~.AlarmClient.delete_alarm` or 
  :meth:`~.AlarmClient.delete_alarms`

Examples
~~~~~~~~

Create, query, acknowledge, and delete alarms

.. literalinclude:: ../examples/alarm/alarm.py
   :language: python
   :linenos:


Tag API
-------

Overview
~~~~~~~~

The :class:`.TagManager` class is the primary entry point of the Tag API.

When constructing a :class:`.TagManager`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.TagManager` use the
default connection. The default connection depends on your SystemLink Client
settings.

With a :class:`.TagManager` object, you can:

* Query, create, modify, and delete tags from the server

  * Use :meth:`~.TagManager.open()` to get a tag's :class:`.TagData` from the
    server when you know the tag's ``path``.
  * Use :meth:`~.TagManager.query()` to get a :class:`collection
    <.TagQueryResultCollection>` of :class:`.TagData` objects based on the
    tags' ``paths``, ``keywords``, and/or ``properties``.
  * Use :meth:`~.TagManager.refresh()` to update a list of :class:`.TagData`
    objects with fresh metadata from the server.
  * Use :meth:`~.TagManager.update()` to modify the server metadata for a list
    of tags, using either :class:`.TagData` objects to overwrite the server's
    tag data or :class:`.TagDataUpdate` objects to selectively update specific
    fields.
  * Use :meth:`~.TagManager.delete()` to delete one or more tags from the
    server.

* Read and write tag values

  * Use :meth:`~.TagManager.read()` to get a tag's current value. Via method
    parameters, you can also request the timestamp indicating when that value
    was last written and/or the aggregate data stored for the tag (if the tag's
    :attr:`~.TagData.collect_aggregates` attribute is enabled on the server).
  * Use :meth:`~.TagManager.create_writer()` to get a
    :class:`.BufferedTagWriter` that will buffer a set of writes, and
    automatically send the writes when a given ``buffer_size`` is reached or
    when ``max_buffer_time`` has elapsed (or when
    :meth:`~.BufferedTagWriter.send_buffered_writes()` is called).

* Get a :class:`.TagSelection` that can help perform several of the above
  operations on several tags at once

  * Use :meth:`.TagManager.create_selection` if you already have a list of
    :class:`.TagData` objects that you want to perform a set of operations on.
  * Use :meth:`.TagManager.open_selection` if you just have a list of ``paths``
    -- optionally including glob-style wildcards! -- with which to create the
    selection.

If you have a :class:`.TagSelection`, you can use it to :meth:`create
<.TagSelection.create_subscription>` a :class:`.TagSubscription` that will
trigger a :attr:`~.TagSubscription.tag_changed` event any time one of the tags'
values is changed.

Examples
~~~~~~~~

Read and write individual tags

.. literalinclude:: ../examples/tag/read_write_one_tag.py
   :language: python
   :linenos:

Subscribe to tag changes

.. literalinclude:: ../examples/tag/subscribe_to_tag_changes.py
   :language: python
   :linenos:


Product API
-------

Overview
~~~~~~~~

The :class:`.ProductClient` class is the primary entry point of the Product API.

When constructing a :class:`.ProductClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.ProductClient` use the
default connection. The default connection depends on your environment.

With a :class:`.ProductClient` object, you can:

* Create, update, query, and delete Products

Examples
~~~~~~~~

Create, query, update, and delete some products

.. literalinclude:: ../examples/product/products.py
   :language: python
   :linenos:


DataFrame API
-------
Overview
~~~~~~~~

The :class:`.DataFrameClient` class is the primary entry point of the DataFrame API.

When constructing a :class:`.DataFrameClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.DataFrameClient` use the
default connection. The default connection depends on your environment.

With a :class:`.DataFrameClient` object, you can:

* Create and delete data tables.

* Modify table metadata and query for tables by their metadata.

* Append rows of data to a table, query for rows of data from a table, and
  decimate table data.

* Export table data in a comma-separated values (CSV) format.

Examples
~~~~~~~~

Create and write data to a table

.. literalinclude:: ../examples/dataframe/create_write_data.py
   :language: python
   :linenos:

Query and read data from a table

.. literalinclude:: ../examples/dataframe/query_read_data.py
   :language: python
   :linenos:

Export data from a table

.. literalinclude:: ../examples/dataframe/export_data.py
   :language: python
   :linenos:

Spec API
-------

Overview
~~~~~~~~


The :class:`.SpecClient` class is the primary entry point of the Specification Compliance API.

When constructing a :class:`.SpecClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.SpecClient` use the
default connection. The default connection depends on your environment.

With a :class:`.SpecClient` object, you can: 

* Create and delete specifications under a product.

* Modify any fields of an existing specification

* Query for specifications on any fields using DynamicLinq syntax.

* Get a specification using an Id.

Examples
~~~~~~~~

Create, Get and Query Specifications

.. literalinclude:: ../examples/spec/get_and_query_specs.py
   :language: python
   :linenos:

Update and Delete Specifications

.. literalinclude:: ../examples/spec/update_and_delete_specs.py
   :language: python
   :linenos:


File API
-------

Overview
~~~~~~~~

The :class:`.FileClient` class is the primary entry point of the File API.

When constructing a :class:`.FileClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.FileClient` use the
default connection. The default connection depends on your environment.

With a :class:`.FileClient` object, you can:

* Get the list of files, query and search for files, download and delete files.
* Start upload sessions, upload file chunks, and finish sessions for large file uploads.

Examples
~~~~~~~~

Get the metadata of a File using its Id and download it.

.. literalinclude:: ../examples/file/download_file.py
   :language: python
   :linenos:

Upload a File from disk or memory to SystemLink

.. literalinclude:: ../examples/file/upload_file.py
   :language: python
   :linenos:

Search for files with filtering and pagination

.. literalinclude:: ../examples/file/search_files.py
   :language: python
   :linenos:

Feeds API
-------

Overview
~~~~~~~~

The :class:`.FeedsClient` class is the primary entry point of the Feeds API.

When constructing a :class:`.FeedsClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.FeedsClient` use the
default connection. The default connection depends on your environment.

With a :class:`.FeedsClient` object, you can:

* Get the list of feeds, create feed, upload package to feed and delete feed.

Examples
~~~~~~~~

Create a new feed.

.. literalinclude:: ../examples/feeds/create_feed.py
   :language: python
   :linenos:

Query feeds and upload a package to feed.

.. literalinclude:: ../examples/feeds/query_and_upload_feeds.py
   :language: python
   :linenos:

Delete a feed.

.. literalinclude:: ../examples/feeds/delete_feed.py
   :language: python
   :linenos:

TestMonitor API (Results and Steps)
-------

Overview
~~~~~~~~

The :class:`.TestMonitorClient` class is the primary entry point of the Test Monitor API
used to interact with test results (Results) and test steps (Steps).

When constructing a :class:`.TestMonitorClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.TestMonitorClient` use the
default connection. The default connection depends on your environment.

With a :class:`.TestMonitorClient` object, you can:

* Create, update, query, and delete results
* Create, update, query, and delete steps

Examples
~~~~~~~~

Create, query, update, and delete some results

.. literalinclude:: ../examples/testmonitor/results.py
   :language: python
   :linenos:

Create, update, query, and delete steps

.. literalinclude:: ../examples/testmonitor/steps.py
   :language: python
   :linenos:

Notebook API
-------

Overview
~~~~~~~~

The :class:`.NotebookClient` class is the primary entry point of the Notebook API.

When constructing a :class:`.NotebookClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.NotebookClient` use the
default connection. The default connection depends on your environment.

With a :class:`.NotebookClient` object, you can:

* Create, update, query, and delete Notebooks
* Create, get and query Notebook Executions

Examples
~~~~~~~~

Create, query, update, and delete some notebooks.

.. literalinclude:: ../examples/notebook/notebook.py
   :language: python
   :linenos:

Create, query, retry, and cancel notebook executions.

.. literalinclude:: ../examples/notebook/notebook_execution.py
   :language: python
   :linenos:

Asset Management API
-------

Overview
~~~~~~~~

The :class:`.AssetManagementClient` class is the primary entry point of the Asset Management API.

When constructing a :class:`.AssetManagementClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.AssetManagementClient` use the
default connection. The default connection depends on your environment.

With a :class:`.AssetManagementClient` object, you can:

* Create, delete, query assets and link files to assets.

* Track asset utilization with start, heartbeat, end, and query history operations.

Examples
~~~~~~~~

Create, delete, and query assets and link files to assets.

.. literalinclude:: ../examples/assetmanagement/assets.py
   :language: python
   :linenos:

Track asset utilization.

.. literalinclude:: ../examples/assetmanagement/asset_utilization.py
   :language: python
   :linenos:

Systems API
-------

Overview
~~~~~~~~

The :class:`.SystemsClient` class is the primary entry point of the Systems API.

When constructing a :class:`.SystemsClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.SystemsClient` use the
default connection. The default connection depends on your environment.

With a :class:`.SystemsClient` object, you can:

* Create, query, and remove systems.

Examples
~~~~~~~~

Create, query, and remove some systems.

.. literalinclude:: ../examples/systems/systems.py
   :language: python
   :linenos:

WorkItem API
-------

Overview
~~~~~~~~

The :class:`.WorkItemClient` class is the primary entry point of the WorkItem API.

When constructing a :class:`.WorkItemClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.WorkItemClient` use the
default connection. The default connection depends on your environment.

With a :class:`.WorkItemClient` object, you can:

* Create, query, get, update, schedule, delete and execute work items
* Create, query, update and delete work item templates

Examples
~~~~~~~~

Create, query, get, update, schedule, delete and execute work items

.. literalinclude:: ../examples/work_item/work_items.py
   :language: python
   :linenos:

Create, query, update and delete work item templates.

.. literalinclude:: ../examples/work_item/work_item_templates.py
   :language: python
   :linenos:

TestPlan API
-------

Overview
~~~~~~~~

The :class:`.TestPlanClient` class is the primary entry point of the TestPlan API.

When constructing a :class:`.TestPlanClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.TestPlanClient` use the
default connection. The default connection depends on your environment.

With a :class:`.TestPlanClient` object, you can:

* Create, query, get, update, schedule and delete TestPlans
* Create, query and delete test plan templates

Examples
~~~~~~~~

Create, query, get, update, schedule and delete TestPlans

.. literalinclude:: ../examples/test_plan/test_plans.py
   :language: python
   :linenos:

Create, query and delete test plan templates.

.. literalinclude:: ../examples/test_plan/test_plan_templates.py
   :language: python
   :linenos:

Notification API
----------------

Overview
~~~~~~~~

The :class:`.NotificationClient` class is the primary entry point of the Notification API.

When constructing a :class:`.NotificationClient`, you can pass an
:class:`.HttpConfiguration` (like one retrieved from the
:class:`.HttpConfigurationManager`), or let :class:`.NotificationClient` use the
default connection. The default connection depends on your environment.

With a :class:`.NotificationClient` object, you can:

* Apply dynamic notification strategy using :meth:`~.NotificationClient.apply_dynamic_notification_strategy`

Examples
~~~~~~~~

Apply a notification strategy

.. literalinclude:: ../examples/notification/notification.py
   :language: python
   :linenos:
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/index.rst sha256=62f0a1be9f045f210ac500da8f59c544c5d61edb952dbea9aad432d02b691869 bytes=248 -->
## FILE: docs/index.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/index.rst`
- sha256: `62f0a1be9f045f210ac500da8f59c544c5d61edb952dbea9aad432d02b691869`
- bytes: 248

````rst
nisystemlink.clients
####################

.. contents::
   :local:

User Documentation
******************

.. toctree::
   :maxdepth: 2

   getting_started
   api_reference

Package Info
************

.. include:: ../README.rst
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=docs/requirements.txt sha256=211c38abee2cfaa14a06b90d8f1a7d469d89b01be0c400b830e01549d88c3352 bytes=115 -->
## FILE: docs/requirements.txt

- repository: `ni/nisystemlink-clients-python`
- source_path: `docs/requirements.txt`
- sha256: `211c38abee2cfaa14a06b90d8f1a7d469d89b01be0c400b830e01549d88c3352`
- bytes: 115

````text
sphinx >= 2.1
sphinx-autodoc-typehints
sphinx-rtd-theme
docutils==0.16
autodoc_pydantic
pyarrow >= 21.0.0
.
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/alarm/alarm.py sha256=4bd5c1a74ca195e7e966176907008975ed927147da3928ec82aa9ba2db066996 bytes=4767 -->
## FILE: examples/alarm/alarm.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/alarm/alarm.py`
- sha256: `4bd5c1a74ca195e7e966176907008975ed927147da3928ec82aa9ba2db066996`
- bytes: 4767

````python
import uuid
from datetime import datetime

from nisystemlink.clients.alarm import AlarmClient
from nisystemlink.clients.alarm.models import (
    AlarmOrderBy,
    AlarmSeverityLevel,
    ClearAlarmTransition,
    CreateOrUpdateAlarmRequest,
    QueryAlarmsWithFilterRequest,
    SetAlarmTransition,
    TransitionInclusionOption,
)
from nisystemlink.clients.core import ApiException, HttpConfiguration

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = AlarmClient(configuration=server_configuration)

# Create a unique alarm ID for this example
# alarm_id is a user-defined identifier for this alarm
alarm_id = f"example_alarm_{uuid.uuid1().hex}"

# Create an alarm with a SET transition
create_request = CreateOrUpdateAlarmRequest(
    alarm_id=alarm_id,
    transition=SetAlarmTransition(
        occurred_at=datetime.now(),
        severity_level=AlarmSeverityLevel.HIGH,
        value="85",
        condition="Greater than 80",
        short_text="Temperature is high",
        detail_text="Temperature sensor reading is 85°C (higher than the configured threshold of 80°C)",
    ),
)
# Returns instance_id - a server-generated unique identifier for this specific alarm occurrence
id = client.create_or_update_alarm(create_request)

# Get the alarm by its instance ID (the unique occurrence identifier)
alarm = client.get_alarm(instance_id=id)
print(f"Retrieved alarm: {alarm.alarm_id}, Condition: {alarm.condition}")

# Update the alarm with a higher severity (same alarm_id, updates the same instance)
update_request = CreateOrUpdateAlarmRequest(
    alarm_id=alarm_id,
    transition=SetAlarmTransition(
        occurred_at=datetime.now(),
        severity_level=AlarmSeverityLevel.CRITICAL,
        value="95",
        condition="Greater than 90",
        short_text="Temperature is critical",
        detail_text="Temperature sensor reading is 95°C (higher than the configured threshold of 90°C)",
    ),
)
client.create_or_update_alarm(update_request)

# Query alarms with a filter (can filter by alarm_id to find all instances)
# Include all transitions to see the full alarm history
query_request = QueryAlarmsWithFilterRequest(
    filter="alarmId=@0",
    substitutions=[alarm_id],
    order_by=AlarmOrderBy.UPDATED_AT,
    order_by_descending=True,
    transition_inclusion_option=TransitionInclusionOption.ALL,
    return_count=True,
)
query_response = client.query_alarms(query_request)

# Display query results
print(f"Total alarms found: {query_response.total_count}")
for alarm in query_response.alarms:
    print(f"  Alarm ID: {alarm.alarm_id}, Transitions: {len(alarm.transitions)}")
    for transition in alarm.transitions:
        print(f"- {transition.transition_type}: {transition.condition}")

# Acknowledge the alarm
client.acknowledge_alarms(instance_ids=[id])

# Clear the alarm with 409 conflict handling - Method 1: Manual exception handling
# A 409 Conflict response indicates that the requested transition would not change the alarm's state.
# This allows stateless applications to simply attempt state transitions without first checking
# the current state. For example, a monitoring system can repeatedly try to CLEAR an alarm
# when conditions return to normal, and the API will return 409 if already cleared.
clear_request = CreateOrUpdateAlarmRequest(
    alarm_id=alarm_id,
    transition=ClearAlarmTransition(
        occurred_at=datetime.now(),
        condition="Temperature returned to normal",
    ),
)
try:
    client.create_or_update_alarm(clear_request)
    print("Alarm cleared successfully")
except ApiException as e:
    if e.http_status_code == 409:
        print("Alarm is already in the requested state (409 Conflict)")
    else:
        raise

# Clear the alarm with 409 conflict handling - Method 2: Using ignore_conflict parameter
# This approach is cleaner for stateless applications that don't care about 409 errors.
# Returns None if the alarm is already in the requested state.
result = client.create_or_update_alarm(clear_request, ignore_conflict=True)
if result is None:
    print("No state change needed (alarm already in requested state)")
else:
    print(f"Alarm cleared successfully: {result}")

# Delete the alarm by its instance ID
client.delete_alarm(instance_id=id)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/artifact/artifacts.py sha256=0973c8cb7cb5d5512908b19b4402a0e7600a728fb173ebddcf0d26b243465d23 bytes=1367 -->
## FILE: examples/artifact/artifacts.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/artifact/artifacts.py`
- sha256: `0973c8cb7cb5d5512908b19b4402a0e7600a728fb173ebddcf0d26b243465d23`
- bytes: 1367

````python
import io

from nisystemlink.clients.artifact import ArtifactClient
from nisystemlink.clients.core import HttpConfiguration

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = ArtifactClient(configuration=server_configuration)

# Define the workspace and artifact content
workspace = "your workspace ID"
artifact_stream = io.BytesIO(b"test content")

# Upload the artifact
upload_response = client.upload_artifact(workspace=workspace, artifact=artifact_stream)
if upload_response and upload_response.id:
    print(f"Uploaded artifact ID: {upload_response.id}")

# Download the artifact using the ID from the upload response
artifact_id = upload_response.id
download_response = client.download_artifact(artifact_id)
if download_response:
    downloaded_content = download_response.read()
    print(f"Downloaded artifact content: {downloaded_content.decode('utf-8')}")

# Delete the artifact
client.delete_artifact(artifact_id)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/assetmanagement/asset_utilization.py sha256=93e0bf765dc806eb3b85638df1ad38e13b202fa66da3f70ed3be7062b5a4c072 bytes=6232 -->
## FILE: examples/assetmanagement/asset_utilization.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/assetmanagement/asset_utilization.py`
- sha256: `93e0bf765dc806eb3b85638df1ad38e13b202fa66da3f70ed3be7062b5a4c072`
- bytes: 6232

````python
import threading
import time
from datetime import datetime
from uuid import uuid4

from nisystemlink.clients.assetmanagement import AssetManagementClient
from nisystemlink.clients.assetmanagement.models import (
    AssetBusType,
    AssetIdentification,
    AssetLocationForCreate,
    AssetPresence,
    AssetPresenceStatus,
    CreateAssetRequest,
    StartUtilizationRequest,
)
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.core.helpers import read_minion_id

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = AssetManagementClient(configuration=server_configuration)

# Generate a unique identifier for this utilization session
utilization_id = str(uuid4())

# Create the assets first
# Define the assets to be created and used in the test
create_assets_request = [
    CreateAssetRequest(
        model_name="NI PXIe-6368",
        model_number=4000,
        serial_number="01BB877A",
        vendor_name="NI",
        vendor_number=4244,
        bus_type=AssetBusType.ACCESSORY,
        name="DAQ Device - 01BB877A",
        location=AssetLocationForCreate(
            state=AssetPresence(asset_presence=AssetPresenceStatus.PRESENT)
        ),
    ),
    CreateAssetRequest(
        model_name="NI PXIe-5163",
        model_number=5000,
        serial_number="02CC988B",
        vendor_name="NI",
        vendor_number=4244,
        bus_type=AssetBusType.ACCESSORY,
        name="Oscilloscope - 02CC988B",
        location=AssetLocationForCreate(
            state=AssetPresence(asset_presence=AssetPresenceStatus.PRESENT)
        ),
    ),
]

# Create the assets in SystemLink
create_assets_response = client.create_assets(assets=create_assets_request)

if create_assets_response.assets:
    print(f"Created {len(create_assets_response.assets)} asset(s)")
    created_asset_ids = [
        asset.id for asset in create_assets_response.assets if asset.id
    ]
else:
    print("Failed to create assets")
    exit(1)

# Define the asset identifications for utilization tracking
test_assets = [
    AssetIdentification(
        model_name="NI PXIe-6368",
        model_number=4000,
        serial_number="01BB877A",
        vendor_name="NI",
        vendor_number=4244,
        bus_type=AssetBusType.ACCESSORY,
    ),
    AssetIdentification(
        model_name="NI PXIe-5163",
        model_number=5000,
        serial_number="02CC988B",
        vendor_name="NI",
        vendor_number=4244,
        bus_type=AssetBusType.ACCESSORY,
    ),
]

# Start asset utilization tracking
# This marks the assets as "in use" in the SystemLink UI
# Read the minion ID from the Salt configuration
minion_id = read_minion_id() or "test-station-01"  # Fallback minion ID if not found

start_utilization_request = StartUtilizationRequest(
    utilization_identifier=utilization_id,
    minion_id=minion_id,
    asset_identifications=test_assets,
    utilization_category="Automated Testing",
    task_name="DUT Validation Suite",
    user_name="automation_user",
    utilization_timestamp=datetime.now(),
)

start_utilization_response = client.start_utilization(request=start_utilization_request)

print(start_utilization_response)

# Verify utilization started successfully
if start_utilization_response.assets_with_started_utilization:
    print(
        f"Utilization started for {len(start_utilization_response.assets_with_started_utilization)} asset(s)"
    )
else:
    print("Failed to start utilization")


# Heartbeat mechanism using a background thread
# IMPORTANT: Heartbeats are for UI purposes only, to keep assets visually
# marked as "in use" in the SystemLink UI. This applies only to utilizations
# that have not been ended. While the standard heartbeat interval is 5 minutes,
# the UI requires heartbeats at least every 10 minutes to continue showing
# assets as actively utilized. If heartbeats stop, the assets will no longer
# appear as "in use" in the UI.
heartbeat_interval = 300  # 5 minutes in seconds
stop_event = threading.Event()


def heartbeat_loop():
    """Background thread that sends periodic heartbeats.

    This keeps the asset visually marked as "in use" in the SystemLink UI
    (for UI purposes only). Applies only to utilizations that have not been ended.
    The UI requires heartbeats at least every 10 minutes to continue displaying
    the asset as actively utilized.
    """
    while not stop_event.wait(heartbeat_interval):
        heartbeat_response = client.utilization_heartbeat(
            ids=[utilization_id],
            timestamp=datetime.now(),
        )

        if heartbeat_response.updated_utilization_ids:
            print(
                f"Heartbeat sent at {datetime.now().strftime('%H:%M:%S')} - asset remains 'in use'"
            )


# Start the heartbeat thread
heartbeat_thread = threading.Thread(target=heartbeat_loop, daemon=True)
heartbeat_thread.start()

# Simulate a long-running operation where assets are in use
# In a real scenario, this would be your actual test or operation
print("\nAssets are now in use. Heartbeats will be sent every 5 minutes...")
print("Waiting for 10 minutes to demonstrate heartbeats...\n")

time.sleep(600)  # Wait 10 minutes

# Stop the heartbeat thread
stop_event.set()
heartbeat_thread.join()

# End asset utilization tracking
end_utilization_response = client.end_utilization(
    ids=[utilization_id],
    timestamp=datetime.now(),
)

if end_utilization_response.updated_utilization_ids:
    print("\nUtilization ended - asset(s) released")

# Clean up: delete the created assets
if created_asset_ids:
    client.delete_assets(ids=created_asset_ids)
    print(f"Deleted {len(created_asset_ids)} asset(s)")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/assetmanagement/assets.py sha256=9bb166281c41f7e06f16730ef9d48db67b71a96597f47b908592fd1316554d30 bytes=3555 -->
## FILE: examples/assetmanagement/assets.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/assetmanagement/assets.py`
- sha256: `9bb166281c41f7e06f16730ef9d48db67b71a96597f47b908592fd1316554d30`
- bytes: 3555

````python
from datetime import datetime, timezone

from nisystemlink.clients.assetmanagement import AssetManagementClient
from nisystemlink.clients.assetmanagement.models import (
    AssetBusType,
    AssetDiscoveryType,
    AssetLocationForCreate,
    AssetPresence,
    AssetPresenceStatus,
    AssetType,
    CreateAssetRequest,
    ExternalCalibration,
    QueryAssetsRequest,
    SelfCalibration,
    TemperatureSensor,
)
from nisystemlink.clients.core import HttpConfiguration

# workspace where the asset will be created
workspace_id = "yourWorkspaceId"

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = AssetManagementClient(configuration=server_configuration)

create_asset_request = CreateAssetRequest(
    model_number=4000,
    model_name="NI PXIe-6368",
    serial_number="01BB877A",
    vendor_name="NI",
    vendor_number=4244,
    bus_type=AssetBusType.ACCESSORY,
    name="PCISlot2",
    asset_type=AssetType.DEVICE_UNDER_TEST,
    firmware_version="A1",
    hardware_version="12A",
    visa_resource_name="vs-3144",
    temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
    supports_self_calibration=True,
    supports_external_calibration=True,
    custom_calibration_interval=24,
    self_calibration=SelfCalibration(
        temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
        is_limited=False,
        date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
    ),
    is_NI_asset=True,
    workspace=workspace_id,
    location=AssetLocationForCreate(
        state=AssetPresence(asset_presence=AssetPresenceStatus.PRESENT)
    ),
    external_calibration=ExternalCalibration(
        temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
        date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
        recommended_interval=10,
        next_recommended_date=datetime(
            2023, 11, 14, 20, 42, 11, 583000, tzinfo=timezone.utc
        ),
        next_custom_due_date=datetime(
            2024, 11, 14, 20, 42, 11, 583000, tzinfo=timezone.utc
        ),
        resolved_due_date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
    ),
    properties={"Key1": "Value1"},
    keywords=["Keyword1"],
    discovery_type=AssetDiscoveryType.MANUAL,
    file_ids=["608a5684800e325b48837c2a"],
    supports_self_test=True,
    supports_reset=True,
    part_number="A1234 B5",
)

# Create an asset.
created_asset = client.create_asset(asset=create_asset_request)
created_asset_id = str(created_asset.id)

# Query assets using id.
query_asset_request = QueryAssetsRequest(
    filter=f'AssetIdentifier = "{created_asset_id}"',
    skip=0,
    take=1,
    descending=False,
    return_count=False,
)
client.query_assets(query=query_asset_request)

# Link files to the created asset.
file_ids = ["sample-file-id"]
if created_asset_id:
    link_files_response = client.link_files(
        asset_id=created_asset_id, file_ids=file_ids
    )

# Delete the created asset.
if created_asset_id is not None:
    client.delete_assets(ids=[created_asset_id])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/dataframe/create_write_data.py sha256=6f9f92c69acfa6dc8f218c293c0d7c52ce8aaf00f6b6262ed72b29fedc4380a0 bytes=3889 -->
## FILE: examples/dataframe/create_write_data.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/dataframe/create_write_data.py`
- sha256: `6f9f92c69acfa6dc8f218c293c0d7c52ce8aaf00f6b6262ed72b29fedc4380a0`
- bytes: 3889

````python
import random
from datetime import datetime

try:
    import pyarrow as pa  # type: ignore
except Exception:
    pa = None  # type: ignore[assignment]
try:
    import pandas as pd  # type: ignore
except Exception:
    pd = None
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.dataframe import DataFrameClient
from nisystemlink.clients.dataframe.models import (
    AppendTableDataRequest,
    Column,
    ColumnType,
    CreateTableRequest,
    DataFrame,
    DataType,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = DataFrameClient(configuration=server_configuration)

# Create table
table_id = client.create_table(
    CreateTableRequest(
        name="Example Table",
        columns=[
            Column(name="ix", data_type=DataType.Int32, column_type=ColumnType.Index),
            Column(name="Float_Column", data_type=DataType.Float32),
            Column(name="Timestamp_Column", data_type=DataType.Timestamp),
        ],
    )
)


print(f"Created table with ID: {table_id}")

print("Appending data to table...")

# Append via explicit AppendTableDataRequest (JSON)
frame_request = DataFrame(
    data=[[str(i), str(random.random()), datetime.now().isoformat()] for i in range(3)]
)
client.append_table_data(table_id, AppendTableDataRequest(frame=frame_request))

# Append via DataFrame model directly (JSON)
frame_direct = DataFrame(
    data=[
        [str(i + 3), str(random.random()), datetime.now().isoformat()] for i in range(3)
    ]
)
client.append_table_data(table_id, frame_direct)

if pa is not None:
    print("Appending data to table via Arrow RecordBatches...")
    # Append via single RecordBatch (Arrow)
    batch_single = pa.record_batch(
        [
            pa.array([6, 7, 8], type=pa.int32()),
            pa.array([0.1, 0.2, 0.3], type=pa.float32()),
            pa.array([datetime.now() for _ in range(3)], pa.timestamp("ms")),
        ],
        names=["ix", "Float_Column", "Timestamp_Column"],
    )
    client.append_table_data(table_id, batch_single)

    # Append via iterable of RecordBatches (Arrow)
    batch_list = [
        pa.record_batch(
            [
                pa.array([9, 10], type=pa.int32()),
                pa.array([0.4, 0.5], type=pa.float32()),
                pa.array([datetime.now() for _ in range(2)], pa.timestamp("ms")),
            ],
            names=["ix", "Float_Column", "Timestamp_Column"],
        )
    ]
    client.append_table_data(table_id, batch_list)

if pa is not None and pd is not None:
    print("Appending data to table via Pandas DataFrame...")
    # Append via DataFrame (Pandas)
    df = pd.DataFrame(
        {
            "ix": [11, 12, 13],
            "Float_Column": [0.6, 0.7, 0.8],
            "Timestamp_Column": [datetime.now() for _ in range(3)],
        }
    )

    # Optional - coerce df types to the dataframe table schema
    df = df.astype(
        {
            "ix": "Int32",
            "Float_Column": "float32",
            "Timestamp_Column": "datetime64[ns]",
        }
    )

    # convert Pandas DataFrame to Arrow RecordBatch and append
    record_batch = pa.RecordBatch.from_pandas(df)
    client.append_table_data(table_id, record_batch)

# Mark end_of_data for the table
# Supply `None` and `end_of_data=True`
print("Finished appending data.")
client.append_table_data(table_id, None, end_of_data=True)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/dataframe/export_data.py sha256=56381823df3fc5270717f5ddce37c2fa8acef09679ca3bc4e37512d39623414f bytes=2003 -->
## FILE: examples/dataframe/export_data.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/dataframe/export_data.py`
- sha256: `56381823df3fc5270717f5ddce37c2fa8acef09679ca3bc4e37512d39623414f`
- bytes: 2003

````python
from shutil import copyfileobj

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.dataframe import DataFrameClient
from nisystemlink.clients.dataframe.models import (
    ColumnFilter,
    ColumnOrderBy,
    ColumnType,
    DataType,
    ExportFormat,
    ExportTableDataRequest,
    FilterOperation,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = DataFrameClient(configuration=server_configuration)

# List a table
response = client.list_tables(take=1)
table = response.tables[0]
index_column = next(
    (col for col in table.columns if col.column_type == ColumnType.Index)
)
order_column = next(
    (col for col in table.columns if col.name != index_column.name), index_column
)
filter_value = (
    "0001-01-01T00:00:00Z" if index_column.data_type == DataType.Timestamp else "0"
)

# Export the first 100,000 rows of table data with query options
request = ExportTableDataRequest(
    columns=[index_column.name],
    order_by=[ColumnOrderBy(column=order_column.name, descending=True)],
    filters=[
        ColumnFilter(
            column=index_column.name,
            operation=FilterOperation.NotEquals,
            value=filter_value,
        )
    ],
    take=100000,
    response_format=ExportFormat.CSV,
)

data = client.export_table_data(id=table.id, query=request)

# Write the export data to a file
with open(f"{table.name}.csv", "wb") as f:
    copyfileobj(data, f)

# Alternatively, load the export data into a pandas dataframe
# import pandas as pd
# df = pd.read_csv(data)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/dataframe/query_read_data.py sha256=32453435835ba224d29a64b3f729ddad7b5f5438e2a82ab0efc0794f24147d32 bytes=1394 -->
## FILE: examples/dataframe/query_read_data.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/dataframe/query_read_data.py`
- sha256: `32453435835ba224d29a64b3f729ddad7b5f5438e2a82ab0efc0794f24147d32`
- bytes: 1394

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.dataframe import DataFrameClient
from nisystemlink.clients.dataframe.models import (
    ColumnType,
    DecimationMethod,
    DecimationOptions,
    QueryDecimatedDataRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = DataFrameClient(configuration=server_configuration)

# List a table
response = client.list_tables(take=1)
table = response.tables[0]
y_column = next(
    (col for col in table.columns if col.column_type != ColumnType.Index),
    table.columns[0],
)

# Get table metadata by table id
client.get_table_metadata(table.id)

# Query decimated table data
request = QueryDecimatedDataRequest(
    decimation=DecimationOptions(
        x_column=None,
        y_columns=[y_column.name],
        intervals=1,
        method=DecimationMethod.MaxMin,
    )
)
rows = client.query_decimated_data(table.id, request)
print(rows.frame.model_dump())
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/feeds/create_feed.py sha256=b062e3ba145a67efd32699b0110712d24f126457d5ded6bd3c3a595075024521 bytes=1415 -->
## FILE: examples/feeds/create_feed.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/feeds/create_feed.py`
- sha256: `b062e3ba145a67efd32699b0110712d24f126457d5ded6bd3c3a595075024521`
- bytes: 1415

````python
"""Functionality of creating feeds APIs."""

from nisystemlink.clients.core import ApiException, HttpConfiguration
from nisystemlink.clients.feeds import FeedsClient
from nisystemlink.clients.feeds.models import (
    CreateFeedRequest,
    Platform,
)

# Update the constants.
FEED_NAME = ""
FEED_DESCRIPTION = ""
PLATFORM = Platform.WINDOWS
WORKSPACE_ID = (
    None  # None uses Default workspace. Replace with Systemlink workspace id.
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FeedsClient(configuration=server_configuration)

# Creating Feeds.
try:
    feed_request = CreateFeedRequest(
        name=FEED_NAME,
        description=FEED_DESCRIPTION,
        platform=PLATFORM,
        workspace=WORKSPACE_ID,
    )
    feed_details = client.create_feed(feed=feed_request)

    print("Feed created Successfully.")
    print(f"Created feed details: {feed_details}")

except ApiException as exp:
    print(exp)
except Exception as exp:
    print(exp)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/feeds/delete_feed.py sha256=f11a153d236b987022dc072eda810ea8f22e748037a6b7ec0b5d647da76bde83 bytes=1448 -->
## FILE: examples/feeds/delete_feed.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/feeds/delete_feed.py`
- sha256: `f11a153d236b987022dc072eda810ea8f22e748037a6b7ec0b5d647da76bde83`
- bytes: 1448

````python
"""Functionality of deleting feed API."""

from nisystemlink.clients.core import ApiException, HttpConfiguration
from nisystemlink.clients.feeds import FeedsClient
from nisystemlink.clients.feeds.models import Platform
from nisystemlink.clients.feeds.utilities import get_feed_by_name

# Update the constants.
FEED_NAME = ""
PLATFORM = Platform.WINDOWS
WORKSPACE_ID = (
    None  # None uses Default workspace. Replace with Systemlink workspace id.
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FeedsClient(configuration=server_configuration)

# Deleting Feed.
try:
    # Get ID of the Feed to delete by name
    feeds = client.query_feeds(platform=PLATFORM, workspace=WORKSPACE_ID)
    feed = get_feed_by_name(feeds=feeds, name=FEED_NAME)
    feed_id = feed.id if feed else None

    # Delete the Feed by ID
    if feed_id:
        client.delete_feed(id=feed_id)
        print("Feed deleted successfully.")

except ApiException as exp:
    print(exp)
except Exception as exp:
    print(exp)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/feeds/query_and_upload_feeds.py sha256=9a52baf1bf64e7e58f6e28794e1b43cf632c0fe5a8173864aa86f58dad3b4c5e bytes=1658 -->
## FILE: examples/feeds/query_and_upload_feeds.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/feeds/query_and_upload_feeds.py`
- sha256: `9a52baf1bf64e7e58f6e28794e1b43cf632c0fe5a8173864aa86f58dad3b4c5e`
- bytes: 1658

````python
"""Functionality of uploading & querying feeds APIs."""

from nisystemlink.clients.core import ApiException, HttpConfiguration
from nisystemlink.clients.feeds import FeedsClient
from nisystemlink.clients.feeds.models import Platform
from nisystemlink.clients.feeds.utilities import get_feed_by_name

# Update the constants.
FEED_NAME = ""
PLATFORM = None
FEED_DESCRIPTION = ""
PLATFORM = Platform.WINDOWS
WORKSPACE_ID = (
    None  # None uses Default workspace. Replace with Systemlink workspace id.
)
PACKAGE_PATH = ""

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FeedsClient(configuration=server_configuration)

# To upload a package to feed.
try:
    # Get ID of the Feed to upload by name
    feeds = client.query_feeds(platform=PLATFORM, workspace=WORKSPACE_ID)
    feed = get_feed_by_name(feeds=feeds, name=FEED_NAME)
    feed_id = feed.id if feed else None

    # Upload the package to Feed by ID
    if feed_id:
        client.upload_package(
            feed_id=feed_id,
            overwrite=True,
            package_file_path=PACKAGE_PATH,
        )
        print("Package uploaded sucessfully.")

except ApiException as exp:
    print(exp)

except Exception as exp:
    print(exp)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/file/download_file.py sha256=d384f1fbf1dbb3e43606c71ffa74070881f4fae1a3527504e82cbac13cb361a6 bytes=1281 -->
## FILE: examples/file/download_file.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/file/download_file.py`
- sha256: `d384f1fbf1dbb3e43606c71ffa74070881f4fae1a3527504e82cbac13cb361a6`
- bytes: 1281

````python
"""Example to download a file from SystemLink."""

from shutil import copyfileobj

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.file import FileClient

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FileClient(configuration=server_configuration)

file_id = "a55adc7f-5068-4202-9d70-70ca6a06bee9"

# Fetch the file metadata to get the name
files = client.get_files(ids=[file_id])

if not files.available_files:
    raise Exception(f"File ID {file_id} not found.")


file_name = "Untitled"

file_properties = files.available_files[0].properties

if file_properties:
    file_name = file_properties["Name"]

# Download the file using FileId with content inline
content = client.download_file(id=file_id)

# Write the content to a file
with open(file_name, "wb") as f:
    copyfileobj(content, f)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/file/query_files_linq.py sha256=45f671c749b05911a448aca0be2cb66c9c5721903da478354d49def6e9ffcfb2 bytes=2558 -->
## FILE: examples/file/query_files_linq.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/file/query_files_linq.py`
- sha256: `45f671c749b05911a448aca0be2cb66c9c5721903da478354d49def6e9ffcfb2`
- bytes: 2558

````python
"""Example to query files using LINQ filters in SystemLink."""

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.file import FileClient
from nisystemlink.clients.file.models import FileLinqQueryOrderBy, FileLinqQueryRequest

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FileClient(configuration=server_configuration)


# Example 1: Basic query to find files by name
query_request = FileLinqQueryRequest(filter='name == "example_file.txt"')
response = client.query_files_linq(query=query_request)

print(f"Found {response.total_count.value} files matching the filter")
for file in response.available_files:
    file_name = file.properties.get("Name", "Unknown") if file.properties else "Unknown"
    print(f"- File ID: {file.id}, Name: {file_name}")


# Example 2: Query with ordering and pagination
query_request = FileLinqQueryRequest(
    filter='name.Contains("test")',  # Find files with "test" in the name
    order_by=FileLinqQueryOrderBy.CREATED,
    order_by_descending=True,  # Most recent first
    take=5,  # Limit to 5 results
)
response = client.query_files_linq(query=query_request)

print(
    f"\nFound {len(response.available_files)} files (limited to {query_request.take}) with 'test' in name"
)
for file in response.available_files:
    file_name = file.properties.get("Name", "Unknown") if file.properties else "Unknown"
    print(f"- File ID: {file.id}, Name: {file_name}")
    print(f"  Created: {file.created}")


# Example 3: Query files by size
query_request = FileLinqQueryRequest(
    filter="size > 1024",  # Files larger than 1KB
    order_by=FileLinqQueryOrderBy.SIZE,
    order_by_descending=True,  # Largest first
    take=3,
)
response = client.query_files_linq(query=query_request)

print(
    f"\nFound {len(response.available_files)} files (limited to {query_request.take}) larger than 1KB"
)
for file in response.available_files:
    file_name = file.properties.get("Name", "Unknown") if file.properties else "Unknown"
    print(f"- File ID: {file.id}, Name: {file_name}")
    print(f"  Size: {file.size} bytes")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/file/search_files.py sha256=6ee765cebbab70875cd37ae5814baf4c2ec8083d4e24fa2dca6195c5145317eb bytes=4850 -->
## FILE: examples/file/search_files.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/file/search_files.py`
- sha256: `6ee765cebbab70875cd37ae5814baf4c2ec8083d4e24fa2dca6195c5145317eb`
- bytes: 4850

````python
"""Example demonstrating how to search for files using the File API.

Note:
    This example requires Elasticsearch to be configured in the SystemLink cluster.
    If Elasticsearch is not configured, this example will fail with an ApiException.
    For deployments without Elasticsearch, use query_files_linq() instead.
"""

import io
import time

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.file import FileClient, models
from nisystemlink.clients.file.models import SearchFilesOrderBy, UpdateMetadataRequest

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FileClient(configuration=server_configuration)

# Upload a test file first
print("Uploading test file...")
test_file_content = b"This is a test file for search demonstration."
test_file = io.BytesIO(test_file_content)
test_file.name = "search-example-test-file.txt"

file_id = client.upload_file(file=test_file)
print(f"Uploaded test file with ID: {file_id}")

# Wait for the file to be indexed for search
# Note: Files may take a few seconds to appear in search results after upload
time.sleep(5)
print()

# Example 1: Basic file search with filter - search for the uploaded file
print("Example 1: Search for the uploaded test file")
search_request = models.SearchFilesRequest(
    filter='name:("search-example-test-file.txt")',
    skip=0,
    take=10,
)

response = client.search_files(search_request)
print(
    f"Found {response.total_count.value if response.total_count else 0} file(s) matching the filter"
)
if response.available_files:
    for file in response.available_files:
        if file.properties:
            print(
                f"- {file.properties.get('Name')} (ID: {file.id}, Size: {file.size} bytes)"
            )

# Example 2: Search with wildcard pattern
print("\nExample 2: Search with wildcard pattern")
search_request = models.SearchFilesRequest(
    filter='name:("search-example*")',
    skip=0,
    take=20,
    order_by=SearchFilesOrderBy.CREATED,
    order_by_descending=True,
)

response = client.search_files(search_request)
print(
    f"Found {response.total_count.value if response.total_count else 0} file(s) starting with 'search-example'"
)
if response.available_files:
    for file in response.available_files:
        if file.properties:
            print(
                f"- {file.properties.get('Name')} created at {file.created} (Size: {file.size} bytes)"
            )

# Example 3: Search by size range
print("\nExample 3: Search by size range")
search_request = models.SearchFilesRequest(
    filter="size:([1 TO 1000])",
    skip=0,
    take=10,
)

response = client.search_files(search_request)
print(
    f"Found {response.total_count.value if response.total_count else 0} file(s) between 1 and 1000 bytes"
)
if response.available_files:
    for file in response.available_files:
        if file.properties:
            print(f"- {file.properties.get('Name')} (Size: {file.size} bytes)")

# Example 4: Search by multiple custom properties
print("\nExample 4: Search by multiple custom properties")
print("Adding custom properties to existing file...")

# Update the existing file with custom properties
custom_metadata = UpdateMetadataRequest(
    replace_existing=False,
    properties={
        "TestProperty1": "TestValue1",
        "TestProperty2": "TestValue2",
    },
)
client.update_metadata(metadata=custom_metadata, id=file_id)

# Wait for indexing
time.sleep(5)

# Search by multiple custom properties using AND operator
search_request = models.SearchFilesRequest(
    filter='(properties.TestProperty1:"TestValue1") AND (properties.TestProperty2:"TestValue2")',
    skip=0,
    take=10,
)

response = client.search_files(search_request)
print(
    f"Found {response.total_count.value if response.total_count else 0} file(s) with "
    "TestProperty1=TestValue1 AND TestProperty2=TestValue2"
)
if response.available_files:
    for file in response.available_files:
        if file.properties:
            print(f"- {file.properties.get('Name')}")
            print(f"  TestProperty1: {file.properties.get('TestProperty1')}")
            print(f"  TestProperty2: {file.properties.get('TestProperty2')}")

# Clean up: delete the test file
print("\nCleaning up...")
client.delete_file(id=file_id)
print(f"Deleted test file with ID: {file_id}")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/file/upload_file.py sha256=aba60eb2bd345061901b7fb0e5a8945f70fce8cdaaf2b27d29f8107b7b990d04 bytes=1302 -->
## FILE: examples/file/upload_file.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/file/upload_file.py`
- sha256: `aba60eb2bd345061901b7fb0e5a8945f70fce8cdaaf2b27d29f8107b7b990d04`
- bytes: 1302

````python
"""Example to upload a file to SystemLink."""

import io

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.file import FileClient

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = FileClient(configuration=server_configuration)

workspace_id = None  # Upload to default workspace of the auth key

# Upload file from disk
file_path = "path/to/your/file"
with open(file_path, "rb") as fp:
    file_id = client.upload_file(file=fp, workspace=workspace_id)
    print(f"Uploaded file from {file_path} to SystemLink with FileID - {file_id}")

# Upload file-like object from memory
test_file = io.BytesIO(b"This is an example file content.")
test_file.name = "File_From_Memory.txt"  # assign a name to the file object
file_id = client.upload_file(file=test_file)
print(f"Uploaded file from memory to SystemLink with FileID - {file_id}")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/general/disable_cert_verify.py sha256=cb26d16b9c662b2d4f85d443b0544c2695ff2d715456f508ed11b35410972d26 bytes=431 -->
## FILE: examples/general/disable_cert_verify.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/general/disable_cert_verify.py`
- sha256: `cb26d16b9c662b2d4f85d443b0544c2695ff2d715456f508ed11b35410972d26`
- bytes: 431

````python
"""Example to demonstrate disabling TLS/SSL certificate verification for connections"""

from nisystemlink.clients.core import HttpConfigurationManager
from nisystemlink.clients.file import FileClient

# explicitly get the http config and set the verify option
http_config = HttpConfigurationManager.get_configuration()
http_config.verify = False

client = FileClient(configuration=http_config)
print(client.api_info())
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/general/pagination_helper.py sha256=b8594229b36f1779d835cc0b62a75973e66556c52ebbc1d1f83ffda410790286 bytes=2239 -->
## FILE: examples/general/pagination_helper.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/general/pagination_helper.py`
- sha256: `b8594229b36f1779d835cc0b62a75973e66556c52ebbc1d1f83ffda410790286`
- bytes: 2239

````python
"""Example demonstrating the paginate helper for iterating through paginated API results.

This example shows how to use the paginate() helper function to automatically
handle continuation tokens when fetching all results from a paginated API.
"""

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.core.helpers import paginate
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.testmonitor.models import Result

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = TestMonitorClient(configuration=server_configuration)

# Example 1: Basic usage - iterate through all results automatically
print("Example 1: Iterating through all results")
print("-" * 50)
result: Result
for result in paginate(client.get_results, items_field="results", take=100):
    print(f"Result ID: {result.id}, Status: {result.status.status_type}")  # type: ignore[union-attr]

# Example 2: Collect all results into a list
print("\nExample 2: Collecting all results into a list")
print("-" * 50)
all_results: list[Result] = list(
    paginate(client.get_results, items_field="results", take=100)
)
print(f"Total results retrieved: {len(all_results)}")

# Example 3: Process in chunks while still using automatic pagination
print("\nExample 3: Processing results in batches")
print("-" * 50)
batch: list[Result] = []
batch_size = 50
for i, result in enumerate(
    paginate(client.get_results, items_field="results", take=100), start=1
):
    batch.append(result)
    if len(batch) >= batch_size:
        # Process batch
        print(f"Processing batch of {len(batch)} results...")
        # Do something with batch
        batch = []

# Process remaining items
if batch:
    print(f"Processing final batch of {len(batch)} results...")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/general/read_minion_id.py sha256=59e746d0d77b765e69bf23f362418ac9c128b073b75c9d7070476749ade7275d bytes=409 -->
## FILE: examples/general/read_minion_id.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/general/read_minion_id.py`
- sha256: `59e746d0d77b765e69bf23f362418ac9c128b073b75c9d7070476749ade7275d`
- bytes: 409

````python
"""Example to demonstrate reading the minion ID from the Salt configuration."""

from nisystemlink.clients.core.helpers import read_minion_id

# Read the minion ID from the Salt configuration file
minion_id = read_minion_id()

if minion_id:
    print(f"Minion ID: {minion_id}")
else:
    print(
        "Minion ID not found. Please ensure the SystemLink client is connected to the Server."
    )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/notebook/notebook.py sha256=0cdf242d933495a3b3a811ad08adc5e9265a15f7dd30c2d76af6001c073356ef bytes=2164 -->
## FILE: examples/notebook/notebook.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/notebook/notebook.py`
- sha256: `0cdf242d933495a3b3a811ad08adc5e9265a15f7dd30c2d76af6001c073356ef`
- bytes: 2164

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.notebook import NotebookClient
from nisystemlink.clients.notebook.models import NotebookMetadata, QueryNotebookRequest

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = NotebookClient(configuration=server_configuration)

# Create a notebook with metadata and content
metadata = NotebookMetadata(
    name="Example Notebook",
    parameters={"param1": "value1"},
    properties={"property1": "value1"},
)

with open("example.ipynb", "rb") as file:
    notebook_response = client.create_notebook(metadata=metadata, content=file)

# Get the notebook by ID
notebook = client.get_notebook("your_notebook_id")

# Update the notebook with new metadata and content
metadata = NotebookMetadata(
    name="Updated Example Notebook",
    parameters={"param1": "value2"},
    properties={"property1": "value2"},
)

with open("example_updated.ipynb", "rb") as file:
    notebook_response = client.update_notebook(
        id="your_notebook_id",
        metadata=metadata,
        content=file,
    )

# Get notebook content by ID
notebook_content = client.get_notebook_content("your_notebook_id")

# Query notebook by name
query_request = QueryNotebookRequest(
    filter='name="Example Notebook"',
)

query_response = client.query_notebooks(query_request)

# Query notebooks by take
query_request = QueryNotebookRequest(take=2)
query_response = client.query_notebooks(query_request)

query_request = QueryNotebookRequest(
    continuation_token=query_response.continuation_token,
    take=1,
)
query_response = client.query_notebooks(query_request)

# Delete the notebook by ID
client.delete_notebook("your_notebook_id")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/notebook/notebook_execution.py sha256=3d4f4480e9bf42a26e5b0482287c4554d5dc2b034a00adb5cd76bfcf855f0a80 bytes=2340 -->
## FILE: examples/notebook/notebook_execution.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/notebook/notebook_execution.py`
- sha256: `3d4f4480e9bf42a26e5b0482287c4554d5dc2b034a00adb5cd76bfcf855f0a80`
- bytes: 2340

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.notebook import NotebookClient
from nisystemlink.clients.notebook.models import (
    CreateExecutionRequest,
    ExecutionField,
    ExecutionPriority,
    ExecutionResourceProfile,
    ExecutionSortField,
    ExecutionStatus,
    QueryExecutionsRequest,
    ReportSettings,
    ReportType,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = NotebookClient(configuration=server_configuration)


# Create a notebook execution
execution_request = CreateExecutionRequest(
    notebook_id="your_notebook_id",
    parameters={"param1": "value1"},
    workspace_id="your_workspace_id",
    timeout=300,
    result_cache_period=3600,
    report_settings=ReportSettings(
        format=ReportType.HTML,
        exclude_code=False,
    ),
    client_requests_id="your_client_request_id",
    priority=ExecutionPriority.HIGH,
    resource_profile=ExecutionResourceProfile.DEFAULT,
)

# Pass the list of execution requests to the create_executions method
create_execution_response = client.create_executions([execution_request])

# Get the execution by ID
execution = client.get_execution_by_id("your_execution_id")

# Query executions
query_request = QueryExecutionsRequest(
    filter=f"(status = {ExecutionStatus.FAILED.value}))",
    order_by=ExecutionSortField.COMPLETED_AT,
    descending=True,
    projection=[
        ExecutionField.ID,
        ExecutionField.NOTEBOOK_ID,
        ExecutionField.STATUS,
    ],
)

query_executions_response = client.query_executions(query_request)

# Cancel execution
cancel_execution_response = client.cancel_executions(["your_execution_id"])

# Retry execution
retry_execution_response = client.retry_executions(["your_execution_id"])

# Create execution from existing one
run_new = client.create_executions_from_existing(["your_execution_id"])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/notification/notification.py sha256=a9db517630deff5c71171e0d62795351544c92e0902c2343684a03bcb415fbe6 bytes=4424 -->
## FILE: examples/notification/notification.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/notification/notification.py`
- sha256: `a9db517630deff5c71171e0d62795351544c92e0902c2343684a03bcb415fbe6`
- bytes: 4424

````python
import uuid
from datetime import datetime

from nisystemlink.clients.alarm import AlarmClient
from nisystemlink.clients.alarm.models._alarm import Alarm, AlarmSeverityLevel
from nisystemlink.clients.alarm.models._create_or_update_alarm_request import (
    CreateOrUpdateAlarmRequest,
    SetAlarmTransition,
)
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.notification import NotificationClient
from nisystemlink.clients.notification.models import (
    DynamicNotificationConfiguration,
    DynamicNotificationStrategy,
    DynamicStrategyRequest,
    SmtpAddressFields,
    SmtpAddressGroup,
    SmtpMessageTemplate,
    SmtpMessageTemplateFields,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )


# Create request for applying strategy
def create_notification_request_for_alarm(
    alarm: Alarm,
    address_group: SmtpAddressGroup,
    message_template: SmtpMessageTemplate,
) -> DynamicStrategyRequest:
    """Creates and returns a dynamic strategy request."""
    occurred_at = alarm.most_recent_transition_occurred_at

    return DynamicStrategyRequest(
        message_template_substitution_fields={
            "alarm_id": alarm.alarm_id,
            "alarm_condition": alarm.condition,
            "alarm_description": alarm.description,
            "alarm_severity": str(alarm.current_severity_level),
            "alarm_occurred_at": occurred_at.isoformat() if occurred_at else "",
        },
        notification_strategy=DynamicNotificationStrategy(
            notification_configurations=[
                DynamicNotificationConfiguration(
                    address_group=address_group,
                    message_template=message_template,
                )
            ]
        ),
    )


# Create clients for Notification and Alarm services
notification_client = NotificationClient(configuration=server_configuration)
alarm_client = AlarmClient(configuration=server_configuration)

# Create a unique alarm ID for this example
alarm_id = f"example_alarm_{uuid.uuid1().hex}"

# Create an alarm with a SET transition
create_alarm_request = CreateOrUpdateAlarmRequest(
    alarm_id=alarm_id,
    transition=SetAlarmTransition(
        occurred_at=datetime.now(),
        severity_level=AlarmSeverityLevel.HIGH,
        value="85",
        condition="Greater than 80",
        short_text="Temperature is high",
        detail_text="Temperature sensor reading is 85°C (higher than the configured threshold of 80°C)",
    ),
    description="Example alarm for notification",
)
id = alarm_client.create_or_update_alarm(create_alarm_request)
print("Alarm created successfully")

# Get the alarm by its instance ID (the unique occurrence identifier)
retrieved_alarm = alarm_client.get_alarm(instance_id=id)

# Define recipients to notify
recipients = SmtpAddressFields(to_addresses=["sample1@example.com"])

# Create address group
address_group = SmtpAddressGroup(
    display_name="Alarm Notification Recipients",
    properties={"address group": "Alarm"},
    fields=recipients,
)

# Create mail template for alarm creation notification
alarm_creation_template = SmtpMessageTemplate(
    display_name="Alarm Creation Template",
    fields=SmtpMessageTemplateFields(
        subject_template="Alarm Created: <alarm_id>",
        body_template="An alarm with ID <alarm_id> has been created.\n"
        "Condition: <alarm_condition>\n"
        "Description: <alarm_description>\n"
        "Current severity: <alarm_severity>\n"
        "Occurred At: <alarm_occurred_at>",
    ),
)

# Send notification for alarm creation
notification_for_alarm_creation = create_notification_request_for_alarm(
    alarm=retrieved_alarm,
    address_group=address_group,
    message_template=alarm_creation_template,
)
notification_client.apply_dynamic_notification_strategy(
    request=notification_for_alarm_creation
)
print("Notification sent for alarm creation")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/product/products.py sha256=ae22c97a9db47e55197d5d26839849a76aa1d41716439b4af4f2e64f621e1954 bytes=3238 -->
## FILE: examples/product/products.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/product/products.py`
- sha256: `ae22c97a9db47e55197d5d26839849a76aa1d41716439b4af4f2e64f621e1954`
- bytes: 3238

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.product import ProductClient
from nisystemlink.clients.product.models import (
    CreateProductRequest,
    ProductField,
    ProductOrderBy,
    QueryProductsRequest,
    QueryProductValuesRequest,
)

name = "Example Name"
family = "Example Family"


def create_some_products():
    """Create two example products on your server."""
    new_products = [
        CreateProductRequest(
            part_number="Example 123 AA",
            name=name,
            family=family,
            keywords=["original keyword"],
            properties={"original property key": "yes"},
        ),
        CreateProductRequest(
            part_number="Example 123 AA1",
            name=name,
            family=family,
            keywords=["original keyword"],
            properties={"original property key": "original"},
        ),
    ]
    create_response = client.create_products(new_products)
    return create_response


# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = ProductClient(configuration=server_configuration)

# Get all the products using the continuation token in batches of 100 at a time.
response = client.get_products_paged(take=100, return_count=True)
all_products = response.products
while response.continuation_token:
    response = client.get_products_paged(
        take=100, continuation_token=response.continuation_token, return_count=True
    )
    all_products.extend(response.products)

create_response = create_some_products()

# use get for first product created
created_product = client.get_product(create_response.products[0].id)

# Query products without continuation
query_request = QueryProductsRequest(
    filter=f'family="{family}" && name="{name}"',
    return_count=True,
    order_by=ProductOrderBy.FAMILY,
)
query_response = client.query_products_paged(query_request)

# Update the first product that you just created and replace the keywords
updated_product = create_response.products[0]
updated_product.keywords = ["new keyword"]
updated_product.properties = {"new property key": "new value"}
update_response = client.update_products([create_response.products[0]], replace=True)

# Query for just the ids of products that match the family
values_query = QueryProductValuesRequest(
    filter=f'family="{family}"', field=ProductField.ID
)
values_response = client.query_product_values(query=values_query)

# delete each created product individually by id
for product in create_response.products:
    client.delete_product(product.id)

# Create some more and delete them with a single call to delete.
create_response = create_some_products()
client.delete_products([product.id for product in create_response.products])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/spec/get_and_query_specs.py sha256=fe447a7554996674565f04876deacf54ed271989295bb6022ae0362d4cc4e359 bytes=3567 -->
## FILE: examples/spec/get_and_query_specs.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/spec/get_and_query_specs.py`
- sha256: `fe447a7554996674565f04876deacf54ed271989295bb6022ae0362d4cc4e359`
- bytes: 3567

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.spec import SpecClient
from nisystemlink.clients.spec.models import (
    Condition,
    ConditionRange,
    ConditionType,
    CreateSpecificationsRequest,
    CreateSpecificationsRequestObject,
    NumericConditionValue,
    QuerySpecificationsRequest,
    SpecificationLimit,
    SpecificationType,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = SpecClient(configuration=server_configuration)

# Create the spec requests
product = "Amplifier"
spec_requests = [
    CreateSpecificationsRequestObject(
        product_id=product,
        spec_id="spec1",
        type=SpecificationType.PARAMETRIC,
        category="Parametric Specs",
        name="output voltage",
        limit=SpecificationLimit(min=1.2, max=1.5),
        unit="mV",
    ),
    CreateSpecificationsRequestObject(
        product_id=product,
        spec_id="spec2",
        type=SpecificationType.PARAMETRIC,
        category="Parametric Specs",
        name="input voltage",
        limit=SpecificationLimit(min=0.02, max=0.15),
        unit="mV",
        conditions=[
            Condition(
                name="Temperature",
                value=NumericConditionValue(
                    condition_type=ConditionType.NUMERIC,
                    range=[ConditionRange(min=-25, step=20, max=85)],
                    unit="C",
                ),
            ),
            Condition(
                name="Supply Voltage",
                value=NumericConditionValue(
                    condition_type=ConditionType.NUMERIC,
                    discrete=[1.3, 1.5, 1.7],
                    unit="mV",
                ),
            ),
        ],
    ),
    CreateSpecificationsRequestObject(
        product_id=product,
        spec_id="spec3",
        type=SpecificationType.FUNCTIONAL,
        category="Noise Thresholds",
        name="noise",
    ),
]

# Create the specs on the server
created_response = client.create_specs(CreateSpecificationsRequest(specs=spec_requests))

# use get for first spec created
if created_response.created_specs and len(created_response.created_specs) > 0:
    created_spec = client.get_spec(created_response.created_specs[0].id)

# You can query specs based on any field using DynamicLinq syntax.
# These are just some representative examples.

response = client.query_specs(QuerySpecificationsRequest(product_ids=[product]))
all_product_specs = response.specs

# Query based on spec id
response = client.query_specs(
    QuerySpecificationsRequest(product_ids=[product], filter='specId == "spec2"')
)
if response.specs:
    spec2 = response.specs[0]

# Query based on name
response = client.query_specs(
    QuerySpecificationsRequest(product_ids=[product], filter='name.Contains("voltage")')
)
voltage_specs = response.specs

# Query based on Category
response = client.query_specs(
    QuerySpecificationsRequest(
        product_ids=[product], filter='category == "Noise Thresholds"'
    )
)
noise_category = response.specs
print(noise_category)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/spec/update_and_delete_specs.py sha256=14258d2692c0329f43b0f78fcd3534c535fc96a344ec13bdb508c12c9315d6e1 bytes=2583 -->
## FILE: examples/spec/update_and_delete_specs.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/spec/update_and_delete_specs.py`
- sha256: `14258d2692c0329f43b0f78fcd3534c535fc96a344ec13bdb508c12c9315d6e1`
- bytes: 2583

````python
from typing import cast

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.spec import SpecClient
from nisystemlink.clients.spec.models import (
    QuerySpecificationsRequest,
    SpecificationType,
    UpdateSpecificationsRequest,
    UpdateSpecificationsRequestObject,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = SpecClient(configuration=server_configuration)

# The query and delete examples assume you have created the specs from the query_specs example
product = "Amplifier"

# update spec1 to change the block to "modifiedBlock"
# query the original spec
response = client.query_specs(
    QuerySpecificationsRequest(product_ids=[product], filter='specId == "spec1"')
)
if response.specs:
    original_spec1 = response.specs[0]
    print(f"Original spec1 block: {original_spec1.block}")
    print(f"Original spec1 version: {original_spec1.version}")

    # make the modifications
    modified_spec = UpdateSpecificationsRequestObject(
        id=cast(str, original_spec1.id),
        product_id=cast(str, original_spec1.product_id),
        spec_id=cast(str, original_spec1.spec_id),
        type=SpecificationType.FUNCTIONAL,
        keywords=["work", "reviewed"],
        block="modifiedBlock",
        version=cast(int, original_spec1.version),
        workspace=cast(str, original_spec1.workspace),
    )
    update_response = client.update_specs(
        specs=UpdateSpecificationsRequest(specs=[modified_spec])
    )
    if update_response and update_response.updated_specs:
        print(f"New spec1 version: {update_response.updated_specs[0].version}")

# query again to see new version
response = client.query_specs(
    QuerySpecificationsRequest(product_ids=[product], filter='specId == "spec1"')
)
if response.specs:
    original_spec1 = response.specs[0]
    print(f"Modified spec1 block: {original_spec1.block}")

# delete all the specs for the product
# query all specs
response = client.query_specs(QuerySpecificationsRequest(product_ids=[product]))
if response.specs:
    client.delete_specs(ids=[spec.id for spec in response.specs if spec.id])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/systems/systems.py sha256=0d2d3dc20d2b9c861bb3d427a7a50ce6ebf1bdddf3d545a31010ba91db2785bf bytes=1607 -->
## FILE: examples/systems/systems.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/systems/systems.py`
- sha256: `0d2d3dc20d2b9c861bb3d427a7a50ce6ebf1bdddf3d545a31010ba91db2785bf`
- bytes: 1607

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.systems import SystemsClient
from nisystemlink.clients.systems.models import (
    CreateVirtualSystemRequest,
    QuerySystemsRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = SystemsClient(configuration=server_configuration)

# Systems request metadata.
create_virtual_system_request: CreateVirtualSystemRequest = CreateVirtualSystemRequest(
    alias="Python integration virtual system",
    workspace="your-workspace-id",
)

# Create a virtual system.
create_virtual_system_response = client.create_virtual_system(
    create_virtual_system_request=create_virtual_system_request
)

minion_id = None

if create_virtual_system_response and create_virtual_system_response.minionId:
    minion_id = create_virtual_system_response.minionId

# Query systems using id.
query_systems_request = QuerySystemsRequest(
    filter=f'id="{minion_id}"', projection="new(id, alias)"
)

client.query_systems(query=query_systems_request)

# Delete the created systems.
if minion_id is not None:
    remove_systems = [minion_id]
    client.remove_systems(tgt=remove_systems)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/tag/read_write_one_tag.py sha256=95946bfe1d31a19cede1884e0484322bb19bf95a97a4b3b10c0b508e54fce62d bytes=507 -->
## FILE: examples/tag/read_write_one_tag.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/tag/read_write_one_tag.py`
- sha256: `95946bfe1d31a19cede1884e0484322bb19bf95a97a4b3b10c0b508e54fce62d`
- bytes: 507

````python
from datetime import timedelta

from nisystemlink.clients.tag import DataType, TagManager

mgr = TagManager()
tag = mgr.open("MyTags.Example Tag", DataType.DOUBLE, create=True)

with mgr.create_writer(buffer_size=10, max_buffer_time=timedelta(seconds=3)) as writer:
    writer.write(tag.path, tag.data_type, 3.5)
# Note: Exiting the "with" block automatically calls writer.send_buffered_writes()

read_result = mgr.read(tag.path)
assert read_result is not None
assert read_result.value == 3.5
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/tag/subscribe_to_tag_changes.py sha256=8884b361e90e9a8e0224f533275d2afdd6fef281992e4d72273eba454d4aeba2 bytes=2534 -->
## FILE: examples/tag/subscribe_to_tag_changes.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/tag/subscribe_to_tag_changes.py`
- sha256: `8884b361e90e9a8e0224f533275d2afdd6fef281992e4d72273eba454d4aeba2`
- bytes: 2534

````python
from contextlib import ExitStack
from time import sleep

from nisystemlink.clients.tag import DataType, TagData, TagManager, TagValueReader

SIMULATE_EXTERNAL_TAG_CHANGES = True


def on_tag_changed(tag: TagData, reader: TagValueReader) -> None:
    """Callback for tag_changed events."""
    path = tag.path
    data_type = tag.data_type.name

    if reader is not None:
        read_result = reader.read()
        # A read_result of None means that the tag has no value, but it *must*
        # have a value, because we got a tag_changed event!
        assert read_result is not None
        value = read_result.value
    else:
        value = "???"  # tag has unknown data type

    print(f'Tag changed: "{path}" = {value} ({data_type})')


mgr = TagManager()
if SIMULATE_EXTERNAL_TAG_CHANGES:
    mgr.open("MyTags.Example Tag", DataType.DOUBLE, create=True)
    writer = mgr.create_writer(buffer_size=1)

with ExitStack() as stack:
    # Notes:
    # 1. The tags are assumed to already exist before this example is run, but
    #    setting SIMULATE_EXTERNAL_TAG_CHANGES to True will ensure there is one.
    # 2. Any tags that get added later will NOT automatically appear in the
    #    selection just because the path matches the wildcard used below; you
    #    must call one of the selection's refresh methods to update the tag list
    #    from the server. But even if you do that:
    # 3. The subscription will only contain the tags that were in the selection
    #    when the subscription was created. If you want the subscription to add
    #    new tags that were added to the selection, you must recreate it.
    paths = ["MyTags.*"]
    selection = stack.enter_context(mgr.open_selection(paths))
    if not selection.metadata:
        print(f"Found no tags that match {paths}")
    else:
        print("Matching tags:")
        for path in selection.metadata.keys():
            print(f" - {path}")
        print()

        subscription = stack.enter_context(selection.create_subscription())
        subscription.tag_changed += on_tag_changed

        # Wait forever, until a KeyboardInterrupt (Ctrl+C)
        print("Watching for tag changes; hit Ctrl+C to stop")
        try:
            i = 0
            while True:
                sleep(1)
                if SIMULATE_EXTERNAL_TAG_CHANGES:
                    writer.write("MyTags.Example Tag", DataType.DOUBLE, i)
                    i += 1
        except KeyboardInterrupt:
            pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/test_plan/test_plan_templates.py sha256=99c5ae08ba692a2aa1ca586c1022d7665671f82fa7d17d85a19a854eb74daeb4 bytes=3215 -->
## FILE: examples/test_plan/test_plan_templates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/test_plan/test_plan_templates.py`
- sha256: `99c5ae08ba692a2aa1ca586c1022d7665671f82fa7d17d85a19a854eb74daeb4`
- bytes: 3215

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.test_plan import TestPlanClient
from nisystemlink.clients.test_plan.models import (
    CreateTestPlanTemplateRequest,
    Dashboard,
    Job,
    JobExecution,
    ManualExecution,
    QueryTestPlanTemplatesRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = TestPlanClient(configuration=server_configuration)

# Test plan template request metadata
create_test_plan_template_request = [
    CreateTestPlanTemplateRequest(
        name="Python integration test plan template",
        template_group="sample template group",
        product_families=["FamilyA", "FamilyB"],
        part_numbers=["PN-1001", "PN-1002"],
        summary="Template for running integration test plans",
        description="This template defines execution steps for integration workflows.",
        test_program="TP-INT-002",
        estimated_duration_in_seconds=86400,
        system_filter="os:linux AND arch:x64",
        dut_filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
        execution_actions=[
            ManualExecution(action="boot", type="MANUAL"),
            JobExecution(
                action="run",
                type="JOB",
                jobs=[
                    Job(
                        functions=["run_test_suite"],
                        arguments=[["test_suite.py"]],
                        metadata={"env": "staging"},
                    )
                ],
                systemId="system-001",
            ),
        ],
        file_ids=["file1", "file2"],
        workspace="your_workspace_id",
        properties={"env": "staging", "priority": "high"},
        dashboard=Dashboard(
            id="DashBoardId", variables={"product": "PXIe-4080", "location": "Lab1"}
        ),
    )
]

# Create a test plan template
create_test_plan_template_response = client.create_test_plan_templates(
    test_plan_templates=create_test_plan_template_request
)

create_test_plan_template_id = None

if (
    create_test_plan_template_response.created_test_plan_templates
    and create_test_plan_template_response.created_test_plan_templates[0].id
):
    create_test_plan_template_id = str(
        create_test_plan_template_response.created_test_plan_templates[0].id
    )

# Query test plan templates using id
query_test_plan_template_request = QueryTestPlanTemplatesRequest(
    filter=f'id="{create_test_plan_template_id}"', take=1
)

client.query_test_plan_templates(
    query_test_plan_templates=query_test_plan_template_request
)

# Delete the created test plan template.
if create_test_plan_template_id is not None:
    client.delete_test_plan_templates(ids=[create_test_plan_template_id])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/test_plan/test_plans.py sha256=147693e1ecabe791c4b5d74ecc1315e63e2ae596f07b3cb2ec8fc846f200bdd8 bytes=3895 -->
## FILE: examples/test_plan/test_plans.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/test_plan/test_plans.py`
- sha256: `147693e1ecabe791c4b5d74ecc1315e63e2ae596f07b3cb2ec8fc846f200bdd8`
- bytes: 3895

````python
from datetime import datetime

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.test_plan import TestPlanClient
from nisystemlink.clients.test_plan.models import (
    CreateTestPlanRequest,
    Dashboard,
    Job,
    JobExecution,
    ManualExecution,
    QueryTestPlansRequest,
    ScheduleTestPlanRequest,
    ScheduleTestPlansRequest,
    UpdateTestPlanRequest,
    UpdateTestPlansRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = TestPlanClient(configuration=server_configuration)

create_test_plans_request = [
    CreateTestPlanRequest(
        name="Python integration test plan",
        state="NEW",
        description="Test plan for verifying integration flow",
        assigned_to="test.user@example.com",
        estimated_duration_in_seconds=86400,
        properties={"env": "staging", "priority": "high"},
        part_number="px40482",
        dut_id="Sample-Dut_Id",
        dut_serial_number="serial_number_123",
        test_program="TP-Integration-001",
        system_filter="os:linux AND arch:x64",
        dut_filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
        workspace="your_workspace_id",
        file_ids_from_template=["file1", "file2"],
        dashboard=Dashboard(
            id="DashBoardId", variables={"product": "PXIe-4080", "location": "Lab1"}
        ),
        execution_actions=[
            ManualExecution(action="boot", type="MANUAL"),
            JobExecution(
                action="run",
                type="JOB",
                jobs=[
                    Job(
                        functions=["run_test_suite"],
                        arguments=[["test_suite.py"]],
                        metadata={"env": "staging"},
                    )
                ],
                systemId="system-001",
            ),
        ],
    )
]

# create a test plan
created_test_plans_response = client.create_test_plans(
    test_plans=create_test_plans_request
)

if created_test_plans_response.created_test_plans:
    created_test_plan_id = created_test_plans_response.created_test_plans[0].id

# Query test plan using id.
query_test_plans_request = QueryTestPlansRequest(
    take=1, descending=False, return_count=False
)
client.query_test_plans(query_request=query_test_plans_request)

# Get test plan
get_test_plan = client.get_test_plan(test_plan_id=created_test_plan_id)

# Update test plan
update_test_plans_request = UpdateTestPlansRequest(
    test_plans=[
        UpdateTestPlanRequest(
            id=created_test_plan_id,
            name="Updated Test Plan",
        )
    ]
)
updated_test_plan = client.update_test_plans(update_request=update_test_plans_request)

# Schedule the test plan
schedule_test_plans_request = ScheduleTestPlansRequest(
    test_plans=[
        ScheduleTestPlanRequest(
            id=created_test_plan_id,
            planned_start_date_time=datetime.strptime(
                "2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            estimated_end_date_time=datetime.strptime(
                "2025-05-22T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            system_id="fake-system",
        )
    ]
)
schedule_test_plan_response = client.schedule_test_plans(
    schedule_request=schedule_test_plans_request
)

# Delete test plan
client.delete_test_plans(ids=[created_test_plan_id])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/testmonitor/results.py sha256=736479cf41c62f244ee39f06468c3920ffe0c281920465e60b0e51032c9f7294 bytes=3440 -->
## FILE: examples/testmonitor/results.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/testmonitor/results.py`
- sha256: `736479cf41c62f244ee39f06468c3920ffe0c281920465e60b0e51032c9f7294`
- bytes: 3440

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.testmonitor.models import (
    CreateResultRequest,
    QueryResultsRequest,
    QueryResultValuesRequest,
    ResultField,
    Status,
    StatusType,
    UpdateResultRequest,
)

program_name = "Example Name"
host_name = "Example Host"
status_type = StatusType.PASSED


def create_some_results():
    """Create two example results on your server."""
    new_results = [
        CreateResultRequest(
            part_number="Example 123 AA",
            program_name=program_name,
            host_name=host_name,
            status=Status.PASSED(),
            keywords=["original keyword"],
            properties={"original property key": "yes"},
        ),
        CreateResultRequest(
            part_number="Example 123 AA1",
            program_name=program_name,
            host_name=host_name,
            status=Status(status_type=StatusType.CUSTOM, status_name="Custom"),
            keywords=["original keyword"],
            properties={"original property key": "original"},
        ),
    ]
    create_response = client.create_results(new_results)
    return create_response


# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = TestMonitorClient(configuration=server_configuration)

create_response = create_some_results()

# Get all the results using the continuation token in batches of 100 at a time.
response = client.get_results(take=100, return_count=True)
all_results = response.results
while response.continuation_token:
    response = client.get_results(
        take=100, continuation_token=response.continuation_token, return_count=True
    )
    all_results.extend(response.results)

# use get for first result created
created_result = client.get_result(create_response.results[0].id)

# Query results without continuation
query_request = QueryResultsRequest(
    filter=f'status.statusType="{status_type.value}"', return_count=True
)
response = client.query_results(query_request)

# Update the first result that you just created and replace the keywords
updated_result = create_response.results[0]
updated_result = UpdateResultRequest(
    id=create_response.results[0].id,
    keywords=["new keyword"],
    properties={"new property key": "new value"},
)
update_response = client.update_results([updated_result], replace=True)

# Query for just the ids of results that match the family
values_query = QueryResultValuesRequest(
    filter=f'programName="{program_name}"', field=ResultField.ID
)
values_response = client.query_result_values(query=values_query)

# delete each created result individually by id
for result in create_response.results:
    client.delete_result(result.id)

# Create some more and delete them with a single call to delete.
create_response = create_some_results()
client.delete_results([result.id for result in create_response.results])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/testmonitor/steps.py sha256=b8d6c2164e7892257ec04bcf8d2c283cfa54f970458c1dd77d4ae9672214dc5f bytes=4059 -->
## FILE: examples/testmonitor/steps.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/testmonitor/steps.py`
- sha256: `b8d6c2164e7892257ec04bcf8d2c283cfa54f970458c1dd77d4ae9672214dc5f`
- bytes: 4059

````python
from typing import cast

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.testmonitor.models import (
    CreateResultRequest,
    CreateStepRequest,
    Measurement,
    NamedValue,
    QueryStepsRequest,
    QueryStepValuesRequest,
    Status,
    StepData,
    StepField,
    StepIdResultIdPair,
    UpdateStepRequest,
)


def create_test_result():
    """Create example result on your server."""
    new_results = [
        CreateResultRequest(
            part_number="Example 123 AA",
            program_name="Example Name",
            host_name="Example Host",
            status=Status.PASSED(),
            keywords=["original keyword"],
            properties={"original property key": "yes"},
        )
    ]
    create_response = client.create_results(new_results)
    return create_response


# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = TestMonitorClient(configuration=server_configuration)

# create a result to attach the steps to
create_response = create_test_result()

# Create the step requests
result_id = cast(str, create_response.results[0].id)
step_requests = [
    CreateStepRequest(
        step_id="step1",
        name="step1",
        result_id=result_id,
        inputs=[
            NamedValue(name="Temperature", value="35"),
            NamedValue(name="Voltage", value="5"),
        ],
    ),
    CreateStepRequest(
        step_id="step2",
        name="step2",
        result_id=result_id,
    ),
]

# Create the steps
create_response = client.create_steps(steps=step_requests)
created_steps = create_response.steps
print(create_response)

# You can query steps based on any field using DynamicLinq syntax.
# These are just some representative examples.
# Query based on result id
query_response = client.query_steps(
    QueryStepsRequest(filter=f'resultId == "{result_id}"')
)
queried_steps = query_response.steps

# query step name using query step values
query_values_response = client.query_step_values(
    QueryStepValuesRequest(
        filter=f'resultId == "{result_id}"',
        field=StepField.NAME,
    )
)

# update the data of the step
# extra properties of the measurements will be converted to string if not already a string
update_response = client.update_steps(
    steps=[
        UpdateStepRequest(
            step_id=step.step_id,
            result_id=cast(str, step.result_id),
            data=StepData(
                text="My output string",
                parameters=[
                    Measurement(
                        name="Temperature",
                        status="Passed",
                        measurement="35",
                        lowLimit="30",
                        highLimit="40",
                        units="C",
                        comparisonType="Numeric",
                        spec_id="spec1",
                    )
                ],
            ),
        )
        for step in created_steps
    ]
)

# delete all steps at once
delete_response = client.delete_steps(
    steps=[
        StepIdResultIdPair(
            step_id=cast(str, step.step_id), result_id=cast(str, step.result_id)
        )
        for step in queried_steps
    ]
)

create_response = client.create_steps(steps=step_requests)
created_steps = create_response.steps

# delete steps one by one
for step in created_steps:
    if step.step_id and step.result_id:
        client.delete_step(result_id=step.result_id, step_id=step.step_id)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/work_item/work_item_templates.py sha256=584532212f36787fab6b80fe447c756d7719c66f863b2e26abd0c1a24fb8a639 bytes=4877 -->
## FILE: examples/work_item/work_item_templates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/work_item/work_item_templates.py`
- sha256: `584532212f36787fab6b80fe447c756d7719c66f863b2e26abd0c1a24fb8a639`
- bytes: 4877

````python
from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.work_item import WorkItemClient
from nisystemlink.clients.work_item.models import (
    CreateWorkItemTemplateRequest,
    Dashboard,
    Job,
    JobExecution,
    ManualExecution,
    QueryWorkItemTemplatesRequest,
    TemplateResourceDefinition,
    TemplateResourcesDefinition,
    TemplateTimelineDefinition,
    UpdateWorkItemTemplateRequest,
    UpdateWorkItemTemplatesRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = WorkItemClient(configuration=server_configuration)

create_work_item_template_request = [
    CreateWorkItemTemplateRequest(
        name="Python integration work item template",
        template_group="sample template group",
        type="testplan",
        product_families=["FamilyA", "FamilyB"],
        part_numbers=["PN-1001", "PN-1002"],
        summary="Template for running integration work items",
        description="This template defines execution steps for integration workflows.",
        test_program="TP-INT-002",
        timeline=TemplateTimelineDefinition(estimated_duration_in_seconds=86400),
        resources=TemplateResourcesDefinition(
            systems=TemplateResourceDefinition(
                filter='properties.data["Lab"] = "Battery Pack Lab" && state = "Available"'
            ),
            duts=TemplateResourceDefinition(
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"'
            ),
            assets=TemplateResourceDefinition(
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"'
            ),
            fixtures=TemplateResourceDefinition(
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"'
            ),
        ),
        execution_actions=[
            ManualExecution(action="boot", type="MANUAL"),
            JobExecution(
                action="run",
                type="JOB",
                jobs=[
                    Job(
                        functions=["run_test_suite"],
                        arguments=[["test_suite.py"]],
                        metadata={"env": "staging"},
                    )
                ],
                systemId="system-001",
            ),
        ],
        file_ids=["file1", "file2"],
        workspace="your_workspace_id",
        properties={"env": "staging", "priority": "high"},
        dashboard=Dashboard(
            id="DashboardId", variables={"product": "PXIe-4080", "location": "Lab1"}
        ),
    )
]

# Create work item template
create_work_item_templates_response = client.create_work_item_templates(
    work_item_templates=create_work_item_template_request
)

if create_work_item_templates_response.created_work_item_templates:
    create_work_item_template_id = (
        create_work_item_templates_response.created_work_item_templates[0].id
    )
    print(f"Created work item template: {create_work_item_template_id}")

# Query work item templates using id
query_work_item_template_request = QueryWorkItemTemplatesRequest(
    filter=f'id="{create_work_item_template_id}"', take=1
)
query_work_item_templates_response = client.query_work_item_templates(
    query_work_item_templates=query_work_item_template_request
)
if query_work_item_templates_response.work_item_templates:
    print(
        f"Found work item template: {query_work_item_templates_response.work_item_templates[0].name}"
    )

# Update work item template
if create_work_item_template_id is not None:
    update_work_item_template_request = UpdateWorkItemTemplatesRequest(
        work_item_templates=[
            UpdateWorkItemTemplateRequest(
                id=create_work_item_template_id, name="Updated work item template"
            )
        ]
    )
    update_work_item_templates_response = client.update_work_item_templates(
        update_work_item_templates=update_work_item_template_request
    )
    if update_work_item_templates_response.updated_work_item_templates:
        print(
            "Work item template name updated to: "
            f"{update_work_item_templates_response.updated_work_item_templates[0].name}"
        )

# Delete work item template
if create_work_item_template_id is not None:
    client.delete_work_item_templates(ids=[create_work_item_template_id])
    print("Work item template deleted successfully.")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=examples/work_item/work_items.py sha256=f5396a6d98ecc9c43a40ce4a720caae5152520b82a8600eb26349fc123467693 bytes=8880 -->
## FILE: examples/work_item/work_items.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `examples/work_item/work_items.py`
- sha256: `f5396a6d98ecc9c43a40ce4a720caae5152520b82a8600eb26349fc123467693`
- bytes: 8880

````python
from datetime import datetime

from nisystemlink.clients.core import HttpConfiguration
from nisystemlink.clients.work_item import WorkItemClient, WorkItemExecuteApiException
from nisystemlink.clients.work_item.models import (
    CreateWorkItemRequest,
    Dashboard,
    Job,
    JobExecution,
    ManualExecution,
    QueryWorkItemsRequest,
    ResourceDefinition,
    ResourcesDefinition,
    ResourceSelectionDefinition,
    ScheduleDefinition,
    ScheduleResourcesDefinition,
    ScheduleSystemResourceDefinition,
    ScheduleWorkItemRequest,
    ScheduleWorkItemsRequest,
    SystemResourceDefinition,
    SystemResourceSelectionDefinition,
    TimelineDefinition,
    UpdateWorkItemRequest,
    UpdateWorkItemsRequest,
)

# Server configuration is not required when used with SystemLink Client or run through Jupyter on SystemLink
server_configuration: HttpConfiguration | None = None

# To set up the server configuration to point to your instance of SystemLink Enterprise, uncomment
# the following lines and provide your server URI and API key.
# server_configuration = HttpConfiguration(
#     server_uri="https://yourserver.yourcompany.com",
#     api_key="",
# )

client = WorkItemClient(configuration=server_configuration)

create_work_items_request = [
    CreateWorkItemRequest(
        name="Python integration work item",
        type="testplan",
        state="NEW",
        description="Work item for verifying integration flow",
        assigned_to="test.user@example.com",
        requested_by="test.manager@example.com",
        properties={"env": "staging", "priority": "high"},
        part_number="px40482",
        test_program="TP-Integration-001",
        workspace="your_workspace_id",
        timeline=TimelineDefinition(
            earliest_start_date_time=datetime.strptime(
                "2024-01-15T08:00:00Z", "%Y-%m-%dT%H:%M:%SZ"
            ),
            due_date_time=datetime.strptime(
                "2024-01-20T17:00:00Z", "%Y-%m-%dT%H:%M:%SZ"
            ),
            estimated_duration_in_seconds=86400,
        ),
        resources=ResourcesDefinition(
            systems=SystemResourceDefinition(
                selections=[
                    SystemResourceSelectionDefinition(
                        id="system-001",
                        target_location_id="location-001",
                    ),
                ],
                filter='properties.data["Lab"] = "Battery Pack Lab"',
            ),
            duts=ResourceDefinition(
                selections=[
                    ResourceSelectionDefinition(
                        id="dut-001",
                        target_location_id="location-001",
                        target_system_id="system-001",
                        target_parent_id="parent-001",
                    ),
                ],
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"',
            ),
            assets=ResourceDefinition(
                selections=[
                    ResourceSelectionDefinition(
                        id="asset-001",
                        target_location_id="location-001",
                        target_system_id="system-001",
                        target_parent_id="parent-001",
                    ),
                ],
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"',
            ),
            fixtures=ResourceDefinition(
                selections=[
                    ResourceSelectionDefinition(
                        id="fixture-001",
                        target_location_id="location-001",
                        target_system_id="system-001",
                        target_parent_id="parent-001",
                    ),
                ],
                filter='modelName = "cRIO-9045" && serialNumber = "01E82ED0"',
            ),
        ),
        file_ids_from_template=["file1", "file2"],
        dashboard=Dashboard(
            id="DashboardId", variables={"product": "PXIe-4080", "location": "Lab1"}
        ),
        workflow_id="example-workflow-id",
        execution_actions=[
            ManualExecution(action="boot", type="MANUAL"),
            JobExecution(
                action="run",
                type="JOB",
                jobs=[
                    Job(
                        functions=["run_test_suite"],
                        arguments=[["test_suite.py"]],
                        metadata={"env": "staging"},
                    )
                ],
                systemId="system-001",
            ),
        ],
    )
]

# create work item
create_work_items_response = client.create_work_items(
    work_items=create_work_items_request
)

if create_work_items_response.created_work_items:
    created_work_item_id = create_work_items_response.created_work_items[0].id
    print(f"Created work item: {created_work_item_id}")

# Query work items using id.
query_work_items_request = QueryWorkItemsRequest(
    filter=f'id = "{created_work_item_id}"',
    take=1,
    descending=False,
    return_count=False,
)
query_work_items_response = client.query_work_items(
    query_work_items=query_work_items_request
)
if query_work_items_response.work_items:
    print(f"Found work item: {query_work_items_response.work_items[0].name}")

# Get work item
if created_work_item_id is not None:
    get_work_item_response = client.get_work_item(work_item_id=created_work_item_id)
    print(f"Retrieved work item: {get_work_item_response.name}")

# Update work item
if created_work_item_id is not None:
    update_work_items_request = UpdateWorkItemsRequest(
        work_items=[
            UpdateWorkItemRequest(id=created_work_item_id, name="Updated work item")
        ]
    )
    update_work_items_response = client.update_work_items(
        update_work_items=update_work_items_request
    )
    if update_work_items_response.updated_work_items:
        print(
            f"Work item name updated to: {update_work_items_response.updated_work_items[0].name}"
        )

# Schedule work item
if created_work_item_id is not None:
    schedule_work_items_request = ScheduleWorkItemsRequest(
        work_items=[
            ScheduleWorkItemRequest(
                id=created_work_item_id,
                schedule=ScheduleDefinition(
                    planned_start_date_time=datetime.strptime(
                        "2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    planned_end_date_time=datetime.strptime(
                        "2025-05-22T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    planned_duration_in_seconds=172800,
                ),
                resources=ScheduleResourcesDefinition(
                    systems=ScheduleSystemResourceDefinition(
                        selections=[
                            SystemResourceSelectionDefinition(
                                id="system-123",
                                target_location_id="location-456",
                            )
                        ]
                    )
                ),
            )
        ],
        replace=True,
    )
    schedule_work_items_response = client.schedule_work_items(
        schedule_work_items=schedule_work_items_request
    )
    if schedule_work_items_response.scheduled_work_items:
        print(
            f"Scheduled work item with ID: {schedule_work_items_response.scheduled_work_items[0].id}"
        )

# Execute work item action
if created_work_item_id is not None:
    try:
        execute_response = client.execute_work_item(
            work_item_id=created_work_item_id, action="START"
        )
        if execute_response.result is not None:
            print(f"Executed action successfully. Type: {execute_response.result.type}")

            # Use type narrowing to access type-specific fields
            if execute_response.result.type == "NOTEBOOK":
                print(f"Notebook execution ID: {execute_response.result.execution_id}")
            elif execute_response.result.type == "JOB":
                if execute_response.result.job_ids:
                    print(f"Job IDs: {', '.join(execute_response.result.job_ids)}")
    except WorkItemExecuteApiException as e:
        print(f"Execution failed (HTTP {e.http_status_code}): {e.error}")
        if e.result is not None:
            print(f"Partial result: {e.result.type}")
    except Exception as e:
        print(f"Could not execute action: {e}")

# Delete work item
if created_work_item_id is not None:
    client.delete_work_items(ids=[created_work_item_id])
    print("Work item deleted successfully.")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=LICENSE sha256=ff8ec728889ff6c79f9054f7d14e369ac3a31da5dd14d48e64a660ed81eab9d7 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/nisystemlink-clients-python`
- source_path: `LICENSE`
- sha256: `ff8ec728889ff6c79f9054f7d14e369ac3a31da5dd14d48e64a660ed81eab9d7`
- bytes: 1091

````text
Copyright (c) 2020, National Instruments Corp.

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

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=mypy.ini sha256=663baeaeea5b258a77e76469c612878d65cb654265b29dcb204900165af21222 bytes=549 -->
## FILE: mypy.ini

- repository: `ni/nisystemlink-clients-python`
- source_path: `mypy.ini`
- sha256: `663baeaeea5b258a77e76469c612878d65cb654265b29dcb204900165af21222`
- bytes: 549

````ini
[mypy]
mypy_path=nisystemlink/stubs
files=nisystemlink,tests
warn_unused_configs=True
plugins = pydantic.mypy
ignore_missing_imports=True

[pydantic-mypy]
init_typed=True
warn_required_dynamic_aliases=True
warn_untyped_fields=True

[mypy-nisystemlink.*]
disallow_untyped_calls=True
disallow_untyped_defs=True
disallow_incomplete_defs=True
disallow_untyped_decorators=True
disable_error_code=empty-body

strict_equality=True

[mypy-tests.*]
disallow_untyped_calls=True
disallow_untyped_decorators=True

strict_equality=True
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: nisystemlink/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: nisystemlink/clients/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/__init__.py sha256=b087ced1b8d241be5a5d1d05eaa15ca3d4b8ed57bc137fafd010bf39fd75b3e0 bytes=154 -->
## FILE: nisystemlink/clients/alarm/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/__init__.py`
- sha256: `b087ced1b8d241be5a5d1d05eaa15ca3d4b8ed57bc137fafd010bf39fd75b3e0`
- bytes: 154

````python
"""Start here with AlarmClient for alarm management."""

from nisystemlink.clients.alarm._alarm_client import AlarmClient

__all__ = ["AlarmClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/_alarm_client.py sha256=efee56ea7ca9abbb8454a6136d571f35a0fa58ff308eb94ff265a34b0455cf0c bytes=7955 -->
## FILE: nisystemlink/clients/alarm/_alarm_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/_alarm_client.py`
- sha256: `efee56ea7ca9abbb8454a6136d571f35a0fa58ff308eb94ff265a34b0455cf0c`
- bytes: 7955

````python
"""Implementation of Alarm Client"""

from typing import List, Literal, overload

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import delete, get, post
from uplink import Field, Path, retry

from . import models


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class AlarmClient(BaseClient):

    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/nialarm/v1/")

    @post(
        "acknowledge-instances-by-instance-id",
        args=[Field("instanceIds"), Field("forceClear")],
    )
    def acknowledge_alarms(
        self, instance_ids: List[str], *, force_clear: bool = False
    ) -> models.AcknowledgeAlarmsResponse:
        """Acknowledges one or more alarm instances by their instance IDs.

        Args:
            instance_ids: List of instance IDs (unique occurrence identifiers) of the alarms to acknowledge.
                 These are the server-generated IDs returned when creating/updating alarms,
                 not the user-defined alarm_id.
            force_clear: Whether or not the affected alarms should have their clear field set to true.
                         Defaults to False.

        Returns:
            A response containing the instance IDs that were successfully acknowledged,
            the instance IDs that failed, and error details for failures.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        """
        ...

    @overload
    def create_or_update_alarm(  # noqa: E704
        self,
        request: models.CreateOrUpdateAlarmRequest,
        *,
        ignore_conflict: Literal[False] = False,
    ) -> str: ...

    @overload
    def create_or_update_alarm(  # noqa: E704
        self,
        request: models.CreateOrUpdateAlarmRequest,
        *,
        ignore_conflict: Literal[True],
    ) -> str | None: ...

    def create_or_update_alarm(
        self,
        request: models.CreateOrUpdateAlarmRequest,
        *,
        ignore_conflict: bool = False,
    ) -> str | None:
        """Creates or updates an instance, or occurrence, of an alarm.

        Creates or updates an alarm based on the requested transition and the state
        of the current active alarm with the given alarm_id (specified in the request).
        Multiple calls with the same alarm_id will update the same alarm instance.

        Args:
            request: The request containing alarm_id (user-defined identifier),
                    transition details, and other alarm properties.
            ignore_conflict: If True, 409 Conflict errors will be ignored and None will be returned.
                           If False (default), 409 errors will raise an ApiException.
                           Setting this to True is useful for stateless applications that want to
                           attempt state transitions without checking the current alarm state first.

        Returns:
            The instance_id (unique occurrence identifier) of the created or modified alarm.
            Use this ID for operations like get_alarm(), delete_alarm(), or acknowledge.
            Returns None if ignore_conflict is True and a 409 Conflict occurs.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
                A 409 Conflict error occurs when the request does not represent a valid transition
                for an existing alarm, such as attempting to clear an alarm which is already clear,
                or attempting to set an alarm which is already set at the given severity level.
                This error can be suppressed by setting ignore_conflict=True.
        """
        try:
            return self._create_or_update_alarm(request)
        except core.ApiException as e:
            if ignore_conflict and e.http_status_code == 409:
                return None
            raise

    @post("instances", return_key="instanceId")
    def _create_or_update_alarm(
        self, request: models.CreateOrUpdateAlarmRequest
    ) -> str:
        """Internal implementation of create_or_update_alarm."""
        ...

    @get("instances/{instance_id}", args=[Path("instance_id")])
    def get_alarm(self, instance_id: str) -> models.Alarm:
        """Gets an alarm by its instance_id.

        Args:
            instance_id: The unique instance ID (occurrence identifier) of the alarm to retrieve.
                This is the server-generated ID returned from create_or_update_alarm(),
                not the user-defined alarm_id.

        Returns:
            The alarm with the specified instance_id.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        """
        ...

    @delete("instances/{instance_id}", args=[Path("instance_id")])
    def delete_alarm(self, instance_id: str) -> None:
        """Deletes an alarm by its instance_id.

        Args:
            instance_id: The unique instance ID (occurrence identifier) of the alarm to delete.
                This is the server-generated ID returned from create_or_update_alarm(),
                not the user-defined alarm_id.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        """
        ...

    @post("delete-instances-by-instance-id", args=[Field("instanceIds")])
    def delete_alarms(self, instance_ids: List[str]) -> models.DeleteAlarmsResponse:
        """Deletes multiple alarm instances by their instance IDs.

        Args:
            instance_ids: List of instance IDs (unique occurrence identifiers) of the alarms to delete.
                 These are the server-generated IDs returned when creating/updating alarms,
                 not the user-defined alarm_id.

        Returns:
            A response containing lists of successfully deleted and failed instance IDs,
            along with error information for failures.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        """
        ...

    @post("query-instances-with-filter")
    def query_alarms(
        self, request: models.QueryAlarmsWithFilterRequest
    ) -> models.QueryAlarmsWithFilterResponse:
        """Queries for instances, or occurrences, of alarms using Dynamic LINQ.

        Specifying an empty JSON object in the request body will result in all alarms being returned.

        Args:
            request: The request containing filter information and query options.

        Returns:
            A response containing the list of alarms that match the query, along with
            optional total count and continuation token for pagination.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/__init__.py sha256=9ac6dbdf24dc9650af7d474c5b28ed7c302c2043e3f6693eb613071bf5a2211e bytes=589 -->
## FILE: nisystemlink/clients/alarm/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/__init__.py`
- sha256: `9ac6dbdf24dc9650af7d474c5b28ed7c302c2043e3f6693eb613071bf5a2211e`
- bytes: 589

````python
from ._acknowledge_alarms_response import AcknowledgeAlarmsResponse
from ._alarm import Alarm, AlarmSeverityLevel, AlarmTransition, AlarmTransitionType
from ._create_or_update_alarm_request import (
    ClearAlarmTransition,
    CreateAlarmTransition,
    CreateOrUpdateAlarmRequest,
    SetAlarmTransition,
)
from ._delete_alarms_response import DeleteAlarmsResponse
from ._query_alarms_request import (
    AlarmOrderBy,
    QueryAlarmsWithFilterRequest,
    TransitionInclusionOption,
)
from ._query_alarms_response import QueryAlarmsWithFilterResponse

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_acknowledge_alarms_response.py sha256=5eb5b4a6e5da8e9b673abe0725c7ed6cc9421c0a7d61b33b36ac3f43471a49b0 bytes=394 -->
## FILE: nisystemlink/clients/alarm/models/_acknowledge_alarms_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_acknowledge_alarms_response.py`
- sha256: `5eb5b4a6e5da8e9b673abe0725c7ed6cc9421c0a7d61b33b36ac3f43471a49b0`
- bytes: 394

````python
from typing import List

from nisystemlink.clients.alarm.models._alarm_instances_partial_success import (
    AlarmInstancesPartialSuccess,
)


class AcknowledgeAlarmsResponse(AlarmInstancesPartialSuccess):
    """Contains information about which alarms were acknowledged."""

    acknowledged: List[str]
    """The instanceIds of the alarms that were successfully acknowledged."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_alarm.py sha256=6c441bb9f1eb61ea05c91f7cfbcd90418bf7472d8fecc42e5311f4ca431a4666 bytes=8241 -->
## FILE: nisystemlink/clients/alarm/models/_alarm.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_alarm.py`
- sha256: `6c441bb9f1eb61ea05c91f7cfbcd90418bf7472d8fecc42e5311f4ca431a4666`
- bytes: 8241

````python
from datetime import datetime
from enum import Enum, IntEnum
from typing import Any, Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class AlarmSeverityLevel(IntEnum):
    """Well-known alarm severity levels.

    The service supports custom severity levels greater than 4, but it is generally discouraged.
    The SystemLink Alarm UI only has display strings for severity levels in the range [1, 4].
    """

    CLEAR = -1
    """Severity level for cleared alarms."""

    LOW = 1
    """Low severity level."""

    MODERATE = 2
    """Moderate severity level."""

    HIGH = 3
    """High severity level."""

    CRITICAL = 4
    """Critical severity level."""


class AlarmTransitionType(str, Enum):
    """Specifies a type of alarm transition."""

    CLEAR = "CLEAR"
    """The transition corresponds to the clearing of the condition tracked by the alarm."""

    SET = "SET"
    """The transition corresponds to the condition tracked by the alarm entering into the triggered state."""


class AlarmTransition(JsonModel):
    """A transition within an instance, or occurrence, of an alarm.

    Alarm transitions record changes to an alarm's clear field as well as an alarm
    increasing or decreasing in severity.
    """

    transition_type: AlarmTransitionType
    """Specifies a type of alarm transition: CLEAR or SET."""

    occurred_at: datetime
    """The date and time when the transition occurred."""

    severity_level: int
    """The severity of the transition.

    Valid values for CLEAR transitions are [-1, -1].
    Valid values for SET transitions are [1, 2147483647].
    Note that the SystemLink Alarm UI only has display strings for SET severities in the range [1, 4].
    The :class:`AlarmSeverityLevel` enum provides values for standard severity levels.
    """

    value: str
    """The value that caused the alarm to transition."""

    condition: str
    """A description of the condition associated with the transition."""

    short_text: str
    """A short description of the condition."""

    detail_text: str
    """A detailed description of the condition."""

    keywords: List[str]
    """Words or phrases associated with a transition.

    Useful for attaching metadata to a transition which could aid in an investigation
    into an alarm's root cause in the future.
    """

    properties: Dict[str, str]
    """Key-value pair metadata associated with a transition.

    Useful for attaching additional metadata to a transition which could aid in an investigation
    into an alarm's root cause in the future. Property keys must be between 1 and 255 characters.
    """


class Alarm(JsonModel):
    """An individual instance, or occurrence, of an alarm.

    The lifecycle of an alarm begins the first time it is triggered and ends when it has been
    both acknowledged and cleared. The service enforces the invariant that there can be at most
    one active=True alarm with the same alarmId.
    """

    instance_id: str
    """The unique identifier for the instance, or occurrence, of the alarm."""

    alarm_id: str
    """A value meant to uniquely identify the particular process or condition tracked by the alarm.

    For example, alarms created by a tag rule engine might have their alarmIds set to the
    concatenation of the path of the tag which caused the rule to be triggered and the ID of the rule.
    """

    workspace: str
    """The workspace the alarm belongs to."""

    active: bool
    """Whether or not the alarm is active.

    An active alarm deserves human or automated attention. Alarms always begin life with active=True.
    This field will be automatically set to false when the clear and acknowledged fields are set to true.
    """

    clear: bool
    """When set to true, the condition that triggered the alarm no longer matches the trigger condition.

    When an alarm is created, clear is initially set to false. The creator of the alarm (typically a
    rule engine or application element of some sort) may determine that the trigger condition no longer
    applies, and may send an update, clearing the alarm. Clearing the alarm does not deactivate the alarm,
    unless the alarm had previously been acknowledged. As long as the alarm is active=true, the alarm may
    transition from clear=True to clear=False (or vice versa) multiple times.
    """

    acknowledged: bool
    """When set to true, the alarm has been acknowledged by an alarm handler, which is typically a human.

    Alarms always begin life with acknowledged=False. Acknowledging an alarm will not affect the active
    flag unless clear is also true. When clear and acknowledged are true, the alarm will become inactive
    (active=False). This field is automatically reset to false when the alarm's highestSeverityLevel field increases.
    """

    acknowledged_at: datetime | None
    """The date and time when the alarm instance was acknowledged.

    This field will be cleared when the alarm's highestSeverityLevel field increases.
    """

    acknowledged_by: str | None
    """The userId of the individual who acknowledged the alarm.

    This field will be cleared when the alarm's highestSeverityLevel field increases.
    """

    occurred_at: datetime
    """The date and time when the alarm was created/first occurred."""

    updated_at: datetime
    """The date and time when the alarm was last updated or modified."""

    created_by: str
    """An identifier for who or what created the alarm.

    This is usually used to identify the particular rule engine which requested that the alarm be created.
    """

    transitions: List[AlarmTransition]
    """A collection of AlarmTransitions for the alarm.

    The service stores the first transition and the most recent 99 other transitions by default.
    The configuration for the service determines the total number of stored transitions per alarm.
    """

    transition_overflow_count: int
    """The number of transitions which overflowed the transitions field for the alarm.

    For example, if the alarm transitioned 250 times, transitionOverflowCount is set to 150 and
    transitions contains the first and most recent 99 transitions. The configuration for the service
    determines the total number of stored transitions per alarm.
    """

    notification_strategy_ids: List[str]
    """The IDs of the notification strategies which will be triggered.

    These are triggered when the alarm is first created and when its highestSeverityLevel increases.
    """

    current_severity_level: int
    """The current severity level of the alarm."""

    highest_severity_level: int
    """The highest severity level that the alarm has ever been in."""

    most_recent_set_occurred_at: datetime | None
    """The date and time of the most recent occurrence of a SET transition.

    This property only considers transitions that cause an alarm state change.
    """

    most_recent_transition_occurred_at: datetime | None
    """The date and time of the most recent occurrence of a transition.

    This property only considers transitions that cause an alarm state change.
    """

    channel: str
    """An identifier for the tag or resource associated with the alarm."""

    condition: str
    """A description of the condition associated with the alarm."""

    display_name: str
    """Optional display name for the alarm. Display names do not need to be unique."""

    description: str
    """Optional description text for the alarm."""

    keywords: List[str]
    """Words or phrases associated with the alarm.

    Alarms can be tagged with keywords to make it easier to find them with queries.
    """

    notes: List[Any]
    """A collection of notes for a given alarm instance.

    Notes are not currently supported and this will always be an empty list.
    """

    properties: Dict[str, str]
    """The alarm's custom properties."""

    resource_type: str
    """The type of resource associated with the alarm."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_alarm_instances_partial_success.py sha256=26d341145930df78ae77f62e1010abe482191f9ef245a34df62c7368a0e42822 bytes=477 -->
## FILE: nisystemlink/clients/alarm/models/_alarm_instances_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_alarm_instances_partial_success.py`
- sha256: `26d341145930df78ae77f62e1010abe482191f9ef245a34df62c7368a0e42822`
- bytes: 477

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class AlarmInstancesPartialSuccess(JsonModel):
    """Base class for partial success responses containing success/failure lists and error information."""

    failed: List[str]
    """The instanceIds that failed the operation."""

    error: ApiError | None = None
    """The error that occurred during the operation."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_create_or_update_alarm_request.py sha256=e0263fe2dbb39cdc4360b4de944f9d18022e742b8fed400f332235553ef358d5 bytes=5512 -->
## FILE: nisystemlink/clients/alarm/models/_create_or_update_alarm_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_create_or_update_alarm_request.py`
- sha256: `e0263fe2dbb39cdc4360b4de944f9d18022e742b8fed400f332235553ef358d5`
- bytes: 5512

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import model_validator

from ._alarm import AlarmSeverityLevel, AlarmTransitionType


class CreateAlarmTransition(JsonModel):
    """Contains information about a transition used to create or update an instance of an alarm."""

    transition_type: AlarmTransitionType
    """Specifies a type of alarm transition: CLEAR or SET."""

    occurred_at: datetime | None = None
    """The date and time when the transition occurred."""

    severity_level: int | None = 2
    """The severity of the transition.

    Valid values for CLEAR transitions are [-1, -1].
    Valid values for SET transitions are [1, 2147483647].
    Note that the SystemLink Alarm UI only has display strings for SET severities in the range [1, 4].
    The :class:`AlarmSeverityLevel` enum provides values for standard severity levels.
    """

    value: str | None = None
    """The value that caused the alarm to transition."""

    condition: str | None = None
    """A description of the condition associated with the transition."""

    short_text: str | None = None
    """A short description of the condition."""

    detail_text: str | None = None
    """A detailed description of the condition."""

    keywords: List[str] | None = None
    """Words or phrases associated with a transition.

    Useful for attaching metadata to a transition which could aid in an investigation
    into an alarm's root cause in the future.
    """

    properties: Dict[str, str] | None = None
    """Key-value pair metadata associated with a transition.

    Useful for attaching additional metadata to a transition which could aid in an investigation
    into an alarm's root cause in the future. Property keys must be between 1 and 255 characters.
    Property values can be up to 1000 characters.
    """


class SetAlarmTransition(CreateAlarmTransition):
    """Contains information about a SET transition used to create or update an instance of an alarm.

    This is a convenience class that automatically sets transition_type to SET.
    """

    transition_type: AlarmTransitionType = AlarmTransitionType.SET

    @model_validator(mode="after")
    def _set_transition_type(self) -> "SetAlarmTransition":
        self.transition_type = AlarmTransitionType.SET
        return self


class ClearAlarmTransition(CreateAlarmTransition):
    """Contains information about a CLEAR transition used to clear an instance of an alarm.

    This is a convenience class that automatically sets transition_type to CLEAR
    and severity_level to -1 (CLEAR severity).
    """

    transition_type: AlarmTransitionType = AlarmTransitionType.CLEAR
    severity_level: int | None = AlarmSeverityLevel.CLEAR

    @model_validator(mode="after")
    def _set_clear_defaults(self) -> "ClearAlarmTransition":
        self.transition_type = AlarmTransitionType.CLEAR
        self.severity_level = AlarmSeverityLevel.CLEAR
        return self


class CreateOrUpdateAlarmRequest(JsonModel):
    """Contains information about the alarm to create or update.

    If an alarm is being updated, only alarmId, workspace, and transition are applied.
    """

    alarm_id: str
    """A value meant to uniquely identify the particular process or condition tracked by the alarm.

    For example, alarms created by a tag rule engine might have their alarmIds set to the
    concatenation of the path of the tag which caused the rule to be triggered and the ID of the rule.
    """

    workspace: str | None = None
    """The ID of the workspace in which to create or update the alarm.

    When not specified, the default workspace is used based on the requesting user.
    """

    transition: CreateAlarmTransition
    """Contains information about a transition used to create or update an instance of an alarm.

    Consider using SetAlarmTransition to trigger an alarm or ClearAlarmTransition to clear an alarm.
    These convenience classes automatically set the appropriate transition type and severity level.
    """

    notification_strategy_ids: List[str] | None = None
    """The IDs of the notification strategies which should be triggered.

    These are triggered if this request results in an alarm being created or
    transitioning to a new highest severity.
    """

    created_by: str | None = None
    """An identifier for who or what created the alarm.

    This is usually used to identify the particular rule engine which requested
    that the alarm be created.
    """

    channel: str | None = None
    """An identifier for the tag or resource associated with the alarm."""

    resource_type: str | None = None
    """The type of resource associated with the alarm."""

    display_name: str | None = None
    """Optional display name for the alarm. Display names do not need to be unique."""

    description: str | None = None
    """Optional description text for the alarm."""

    keywords: List[str] | None = None
    """Words or phrases associated with the alarm.

    Alarms can be tagged with keywords to make it easier to find them with queries.
    """

    properties: Dict[str, str] | None = None
    """The alarm's custom properties. Property keys must be between 1 and 255 characters.
    Property values can be up to 1000 characters."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_delete_alarms_response.py sha256=abd6b26a84188fae4166b88c28aaa401017a78996aeb8112d5bd3d86cafea5ae bytes=373 -->
## FILE: nisystemlink/clients/alarm/models/_delete_alarms_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_delete_alarms_response.py`
- sha256: `abd6b26a84188fae4166b88c28aaa401017a78996aeb8112d5bd3d86cafea5ae`
- bytes: 373

````python
from typing import List

from nisystemlink.clients.alarm.models._alarm_instances_partial_success import (
    AlarmInstancesPartialSuccess,
)


class DeleteAlarmsResponse(AlarmInstancesPartialSuccess):
    """Contains information about alarms that were deleted."""

    deleted: List[str]
    """The instanceIds of the alarms that were successfully deleted."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_query_alarms_request.py sha256=e9e32e2c1d37a87ccddf31095991208a34f2113d94121c48b5ba35e603d6c221 bytes=5444 -->
## FILE: nisystemlink/clients/alarm/models/_query_alarms_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_query_alarms_request.py`
- sha256: `e9e32e2c1d37a87ccddf31095991208a34f2113d94121c48b5ba35e603d6c221`
- bytes: 5444

````python
from datetime import datetime
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class TransitionInclusionOption(str, Enum):
    """Determines which transitions to include in the query results."""

    NONE = "NONE"
    """No transitions are included."""

    MOST_RECENT_ONLY = "MOST_RECENT_ONLY"
    """The most recent transition is included."""

    ALL = "ALL"
    """All transitions are included."""


class AlarmOrderBy(str, Enum):
    """The sort order of the returned list of alarms."""

    UPDATED_AT = "UPDATED_AT"
    """The date and time the alarm was last updated."""


class QueryAlarmsWithFilterRequest(JsonModel):
    """Contains filter information for querying alarms."""

    filter: str | None = None
    """The alarm query filter in `Dynamic LINQ`_ format.

    .. _Dynamic LINQ: https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language

    Allowed properties in the filter are:

    * ``acknowledged``: Boolean value that indicates an alarm acknowledgment
    * ``acknowledgedAt``: DateTime value that represents when the alarm was acknowledged
    * ``active``: Boolean value that indicates an active alarm
    * ``alarmId``: String value that identifies the process or condition tracked by the alarm
    * ``channel``: String value that identifies the tag or resource associated with the alarm
    * ``clear``: Boolean value that indicates an alarm clearance
    * ``createdBy``: String value that identifies the user that created the alarm
    * ``currentSeverityLevel``: Int32 value that represents the severity level of the alarm
    * ``description``: String value that describes the alarm
    * ``displayName``: String value that represents the alarm name in the user interface
    * ``highestSeverityLevel``: Int32 value that represents the highest severity level of the alarm
    * ``keywords``: List of string values associated with the alarm
    * ``mostRecentSetOccurredAt``: DateTime value that represents when the most recent set transition occurred
    * ``mostRecentTransitionOccurredAt``: DateTime value that represents when the most recent transition occurred
    * ``occurredAt``: DateTime value that represents when the alarm was created or first occurred
    * ``occurredWithin``: TimeSpan value that represents when the alarm was created or first occurred
    * ``properties``: Dictionary that contains the string keys and values representing alarm metadata
    * ``resourceType``: String value that represents the resource type of the alarm
    * ``workspace``: String ID of the workspace to use in the query
    * ``workspaceName``: String name of the workspace of the alarm

    Allowed constants in the filter are:

    * ``RelativeTime.CurrentDay``: TimeSpan representing the elapsed time between now and
      the start of the current day
    * ``RelativeTime.CurrentWeek``: TimeSpan representing the elapsed time between now and
      the start of the current week
    * ``RelativeTime.CurrentMonth``: TimeSpan representing the elapsed time between now and
      the start of the current month
    * ``RelativeTime.CurrentYear``: TimeSpan representing the elapsed time between now and
      the start of the current year
    """

    substitutions: List[bool | int | str | None] | None = None
    """Makes substitutions in the query filter expression.

    Substitutions for the query expression are indicated by non-negative integers that are
    prefixed with the @ symbol. Each substitution in the given expression will be replaced by
    the element at the corresponding index (zero-based) in this list.
    """

    return_most_recently_occurred_only: bool = False
    """Whether or not the Alarm Service should group the alarms matched by this query by alarmId.

    When true, only return the most recent alarm for each grouping. In this context, recency is
    based on when the alarm occurred, not when it was last updated.
    """

    transition_inclusion_option: TransitionInclusionOption | None = None
    """Determines which transitions to include in the query results, if any."""

    reference_time: datetime | None = None
    """The date and time to use as the reference point for RelativeTime filters.

    Includes time zone information. Defaults to the current time in UTC.
    """

    take: int | None = 1000
    """Limits the returned list to the specified number of results. Maximum is 1000."""

    order_by: AlarmOrderBy | None = None
    """The sort order of the returned list of alarms.

    By default, alarms are sorted in ascending order based on the specified value.
    """

    order_by_descending: bool = False
    """Whether to sort descending instead of ascending.

    The elements in the list are sorted ascending by default. If true, sorts descending.
    """

    continuation_token: str | None = None
    """A token which allows the user to resume a query at the next item in the matching results.

    When querying, a token will be returned if a query may be continued. To obtain the next page
    of results, pass the token to the service on a subsequent request.
    """

    return_count: bool = False
    """Whether to return the total number of alarms that match the provided filter.

    This disregards the take value.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_query_alarms_response.py sha256=62463459471dbc4bb06539f206caec4f8eb13427e0b421dcd497169e626c0c59 bytes=445 -->
## FILE: nisystemlink/clients/alarm/models/_query_alarms_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/alarm/models/_query_alarms_response.py`
- sha256: `62463459471dbc4bb06539f206caec4f8eb13427e0b421dcd497169e626c0c59`
- bytes: 445

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._alarm import Alarm


class QueryAlarmsWithFilterResponse(WithPaging):
    """Contains information about the alarms matched by a query."""

    alarms: List[Alarm]
    """The list of alarms returned by the query."""

    total_count: int | None = None
    """The total number of alarms which matched the query, if requested."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/__init__.py sha256=2114832ed720768e5520b605e20c3912271cc26900435efb67e1d28cf5db4ac7 bytes=143 -->
## FILE: nisystemlink/clients/artifact/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/artifact/__init__.py`
- sha256: `2114832ed720768e5520b605e20c3912271cc26900435efb67e1d28cf5db4ac7`
- bytes: 143

````python
"""Start here with ArtifactClient for artifact management."""

from ._artifact_client import ArtifactClient

__all__ = ["ArtifactClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/_artifact_client.py sha256=7c70c102ab2170ae4f2e483a6c15d8b12a8be71ede0e04a64a12b270849b59e0 bytes=3314 -->
## FILE: nisystemlink/clients/artifact/_artifact_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/artifact/_artifact_client.py`
- sha256: `7c70c102ab2170ae4f2e483a6c15d8b12a8be71ede0e04a64a12b270849b59e0`
- bytes: 3314

````python
"""Implementation of ArtifactClient"""

from typing import BinaryIO

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import (
    delete,
    get,
    post,
    response_handler,
)
from nisystemlink.clients.core._uplink._multipart_retry import (
    retryable_multipart_request,
)
from nisystemlink.clients.core.helpers._iterator_file_like import IteratorFileLike
from requests.models import Response
from uplink import Part, Path, retry

from . import models


def _iter_content_filelike_wrapper(response: Response) -> IteratorFileLike:
    return IteratorFileLike(response.iter_content(chunk_size=4096))


@retry(when=retry.when.status(429), stop=retry.stop.after_attempt(5))
class ArtifactClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the  Notebook execution Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/ninbartifact/v1/")

    @retryable_multipart_request()
    @post("artifacts", args=[Part("workspace"), Part("artifact")])
    def __upload_artifact(
        self, workspace: str, artifact: BinaryIO
    ) -> models.UploadArtifactResponse:
        """Uploads an artifact  using multipart/form-data headers to send the file payload in the HTTP body.

        Args:
            workspace: The workspace containing the artifact.
            artifact: The artifact to upload.

        Returns:
            UploadArtifactResponse: The response containing the artifact ID.

        """
        ...

    def upload_artifact(
        self, workspace: str, artifact: BinaryIO
    ) -> models.UploadArtifactResponse:
        """Uploads an artifact.

        Args:
            workspace: The workspace containing the artifact.
            artifact: The artifact to upload.

        Returns:
            UploadArtifactResponse: The response containing the artifact ID.

        """
        response = self.__upload_artifact(
            workspace=workspace,
            artifact=artifact,
        )

        return response

    @response_handler(_iter_content_filelike_wrapper)
    @get("artifacts/{id}")
    def download_artifact(self, id: Path) -> IteratorFileLike:
        """Downloads an artifact.

        Args:
            id: The ID of the artifact to download.

        Returns:
            A file-like object for reading the artifact content.

        """
        ...

    @delete("artifacts/{id}", args=[Path("id")])
    def delete_artifact(self, id: str) -> None:
        """Deletes an artifact.

        Args:
            id: The ID of the artifact to delete.

        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/models/__init__.py sha256=e3166fcc203c264876c6e967b2bfdd3698f2d3e61f06c5e51d634f50cf79d5ee bytes=81 -->
## FILE: nisystemlink/clients/artifact/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/artifact/models/__init__.py`
- sha256: `e3166fcc203c264876c6e967b2bfdd3698f2d3e61f06c5e51d634f50cf79d5ee`
- bytes: 81

````python
from ._upload_artifact_response import UploadArtifactResponse

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/models/_upload_artifact_response.py sha256=892a4bfecde7a3e1209461211296bb80b2b6ef4fb0276050ca6841fe0476334a bytes=234 -->
## FILE: nisystemlink/clients/artifact/models/_upload_artifact_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/artifact/models/_upload_artifact_response.py`
- sha256: `892a4bfecde7a3e1209461211296bb80b2b6ef4fb0276050ca6841fe0476334a`
- bytes: 234

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class UploadArtifactResponse(JsonModel):
    """Response for an artifact upload request."""

    id: str
    """Information about the uploaded artifact."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/__init__.py sha256=1276ef574611376965dd98fe6ff2d7f26a7b37161b1b6e4e9e6c8256cda152fa bytes=216 -->
## FILE: nisystemlink/clients/assetmanagement/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/__init__.py`
- sha256: `1276ef574611376965dd98fe6ff2d7f26a7b37161b1b6e4e9e6c8256cda152fa`
- bytes: 216

````python
"""Start here with AssetManagementClient for asset management."""

from nisystemlink.clients.assetmanagement._asset_management_client import (
    AssetManagementClient,
)

__all__ = ["AssetManagementClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/_asset_management_client.py sha256=ba66ef5cf1372208294c2b6db52b028977f29bbe93b22dc329e4547309a2ebde bytes=10947 -->
## FILE: nisystemlink/clients/assetmanagement/_asset_management_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/_asset_management_client.py`
- sha256: `ba66ef5cf1372208294c2b6db52b028977f29bbe93b22dc329e4547309a2ebde`
- bytes: 10947

````python
"""Implementation of AssetManagementClient."""

from datetime import datetime
from typing import List, Optional

from nisystemlink.clients import core
from nisystemlink.clients.assetmanagement.models._update_utilization_request import (
    _UpdateUtilizationRequest,
)
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import post
from uplink import Field, Path, retry

from . import models
from ..core.helpers._partial_success import unwrap_single_item_partial_success


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class AssetManagementClient(BaseClient):
    def __init__(self, configuration: HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: If unable to communicate with the asset management Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/niapm/v1/")

    @post("assets", args=[Field("assets")])
    def create_assets(
        self, assets: List[models.CreateAssetRequest]
    ) -> models.CreateAssetsPartialSuccessResponse:
        """Create Assets.

        Args:
            assets: Array of assets that should be created.

        Returns:
            CreateAssetsPartialSuccessResponse: Array of created assets and array of failed.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        """
        ...

    def create_asset(self, asset: models.CreateAssetRequest) -> models.Asset:
        """Create a single asset.

        Args:
            asset: The asset to create.

        Returns:
            The created asset.

        Raises:
            ApiException: if the asset could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_assets([asset])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.assets,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to create asset.",
            empty_message="Server returned no created assets.",
        )

    @post("query-assets")
    def __query_assets(
        self, query: models._QueryAssetsRequest
    ) -> models.QueryAssetsResponse:
        """Query Assets.

        Args:
            query: Object containing filters to apply when retrieving assets.

        Returns:
            QueryAssetsResponse: Assets Response containing the assets satisfying the query and
            the total count of matching assets.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        """
        ...

    def query_assets(
        self, query: models.QueryAssetsRequest
    ) -> models.QueryAssetsResponse:
        """Query Assets.

        Args:
            query: Object containing filters to apply when retrieving assets.

        Returns:
            QueryAssetsResponse: Assets Response containing the assets satisfying the query and
            the total count of matching assets.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        """
        projection_str = (
            f"new({', '.join(projection.name for projection in query.projection)})"
            if query.projection
            else None
        )
        query_params = {
            "filter": query.filter,
            "take": query.take,
            "skip": query.skip,
            "return_count": query.return_count,
            "order_by": query.order_by,
            "descending": query.descending,
            "projection": projection_str,
        }

        query_params = {k: v for k, v in query_params.items() if v is not None}

        query_request = models._QueryAssetsRequest(**query_params)  # type: ignore

        return self.__query_assets(query=query_request)

    @post("delete-assets", args=[Field("ids")])
    def delete_assets(self, ids: List[str]) -> models.DeleteAssetsResponse:
        """Delete Assets.

        Args:
            ids: List of IDs of the assets to delete.

        Returns:
            DeleteAssetsResponse: Response containing the IDs of the assets that were deleted.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        ...

    @post("assets/{assetId}/file", args=[Path("assetId"), Field("fileIds")])
    def link_files(
        self, asset_id: str, file_ids: List[str]
    ) -> models.LinkFilesPartialSuccessResponse | None:
        """Link files to an asset.

        Args:
            asset_id: The ID of the asset to which files should be linked.
            file_ids: The list of file IDs to link.

        Returns:
            None if all link files succeed, otherwise a response containing the IDs of files that were
            successfully linked and those that failed.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        ...

    @post("query-asset-utilization-history")
    def query_asset_utilization_history(
        self, request: models.QueryAssetUtilizationHistoryRequest
    ) -> models.AssetUtilizationHistoryResponse:
        """Query asset utilization history.

        Args:
            request: Object containing filters for asset utilization and assets, including
                    utilization_filter, asset_filter, date range, and pagination options.

        Returns:
            AssetUtilizationHistoryResponse: Response containing the list of asset utilization
            history records that match the query, along with optional continuation token for pagination.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        ...

    @post("assets/start-utilization")
    def start_utilization(
        self, request: models.StartUtilizationRequest
    ) -> models.StartUtilizationPartialSuccessResponse:
        """Start asset utilization tracking.

        Args:
            request: Object containing the utilization identifier, minion ID, asset identifications,
                    utilization category, task name, user name, and utilization timestamp.

        Returns:
            StartUtilizationPartialSuccessResponse: Response containing arrays of assets that successfully
            started utilization and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        ...

    @post("assets/end-utilization")
    def __end_utilization(
        self, request: _UpdateUtilizationRequest
    ) -> models.UpdateUtilizationPartialSuccessResponse:
        """End asset utilization tracking.

        Args:
            request: The request object containing utilization identifiers and timestamp.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing updated utilization IDs.
        """
        ...

    def end_utilization(
        self,
        ids: List[str],
        timestamp: Optional[datetime] = None,
    ) -> models.UpdateUtilizationPartialSuccessResponse:
        """End asset utilization tracking.

        Args:
            ids: Array of utilization identifiers representing the unique identifier
                of asset utilization history records to end.
            timestamp: The timestamp to use when ending the utilization.
                If not provided, the current server time will be used.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing arrays of utilization IDs that were
            successfully updated and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        request = _UpdateUtilizationRequest(
            utilization_identifiers=ids,
            utilization_timestamp=timestamp,
        )
        return self.__end_utilization(request)

    @post("assets/utilization-heartbeat")
    def __utilization_heartbeat(
        self, request: _UpdateUtilizationRequest
    ) -> models.UpdateUtilizationPartialSuccessResponse:
        """Send utilization heartbeat.

        Args:
            request: The request object containing utilization identifiers and timestamp.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing updated utilization IDs.
        """
        ...

    def utilization_heartbeat(
        self,
        ids: List[str],
        timestamp: Optional[datetime] = None,
    ) -> models.UpdateUtilizationPartialSuccessResponse:
        """Send utilization heartbeat to update asset utilization tracking.

        Args:
            ids: Array of utilization identifiers representing the unique identifier
                of asset utilization history records to update.
            timestamp: The timestamp to use for the heartbeat.
                If not provided, the current server time will be used.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing arrays of utilization IDs that were
            successfully updated and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        """
        request = _UpdateUtilizationRequest(
            utilization_identifiers=ids,
            utilization_timestamp=timestamp,
        )
        return self.__utilization_heartbeat(request)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/__init__.py sha256=637d202005cac18f36433cae901d6a6fe7949848497712b23280ea6576763b58 bytes=1552 -->
## FILE: nisystemlink/clients/assetmanagement/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/__init__.py`
- sha256: `637d202005cac18f36433cae901d6a6fe7949848497712b23280ea6576763b58`
- bytes: 1552

````python
from ._query_assets_response import QueryAssetsResponse
from ._asset import Asset
from ._create_asset_request import CreateAssetRequest
from ._create_assets_partial_success_response import CreateAssetsPartialSuccessResponse
from ._delete_assets_response import DeleteAssetsResponse
from ._query_assets_request import AssetField, QueryAssetsRequest, _QueryAssetsRequest
from ._query_assets_response import QueryAssetsResponse
from ._asset_location import (
    AssetLocation,
    AssetLocationForCreate,
    AssetPresence,
    AssetPresenceWithSystemConnection,
    AssetPresenceStatus,
)
from ._asset_calibration import (
    CalibrationMode,
    CalibrationStatus,
    SelfCalibration,
    TemperatureSensor,
    ExternalCalibration,
)
from ._asset_types import AssetBusType, AssetDiscoveryType, AssetType
from ._link_files_partial_success_response import LinkFilesPartialSuccessResponse
from ._query_asset_utilization_history_request import (
    QueryAssetUtilizationHistoryRequest,
    UtilizationOrderBy,
)
from ._asset_utilization_history_item import AssetUtilizationHistoryItem
from ._asset_utilization_history_response import AssetUtilizationHistoryResponse
from ._asset_identification import AssetIdentification
from ._start_utilization_request import StartUtilizationRequest
from ._start_utilization_partial_success_response import (
    StartUtilizationPartialSuccessResponse,
)
from ._update_utilization_partial_success_response import (
    UpdateUtilizationPartialSuccessResponse,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset.py sha256=c6af1b365c9a6900903ced09e4a705fdc039be1cbd166a82fd5988223c8eae1b bytes=4277 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset.py`
- sha256: `c6af1b365c9a6900903ced09e4a705fdc039be1cbd166a82fd5988223c8eae1b`
- bytes: 4277

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field

from ._asset_calibration import (
    CalibrationStatus,
    ExternalCalibration,
    SelfCalibration,
    TemperatureSensor,
)
from ._asset_location import AssetLocation
from ._asset_types import AssetBusType, AssetDiscoveryType, AssetType


class Asset(JsonModel):
    """Model for an object describing an asset with all of its properties."""

    model_name: str | None = None
    """Gets or sets model name of the asset."""

    model_number: int | None = None
    """Gets or sets model number of the asset."""

    serial_number: str | None = None
    """Gets or sets serial number of the asset."""

    vendor_name: str | None = None
    """Gets or sets vendor name of the asset."""

    vendor_number: int | None = None
    """Gets or sets vendor number of the asset."""

    bus_type: AssetBusType | None = None
    """Gets or sets all supported bus types for an asset."""

    name: str | None = None
    """Gets or sets name of the asset."""

    asset_type: AssetType | None = None
    """Gets or sets all supported asset types."""

    discovery_type: AssetDiscoveryType | None = None
    """Gets or sets the discovery type."""

    firmware_version: str | None = None
    """Gets or sets firmware version of the asset."""

    hardware_version: str | None = None
    """Gets or sets hardware version of the asset."""

    visa_resource_name: str | None = None
    """Gets or sets VISA resource name of the asset."""

    temperature_sensors: List[TemperatureSensor] | None = None
    """Gets or sets an array of temperature sensor information."""

    supports_self_calibration: bool | None = None
    """Gets or sets whether the asset supports self-calibration."""

    supports_external_calibration: bool | None = None
    """Gets or sets whether the asset supports external calibration."""

    custom_calibration_interval: int | None = None
    """Gets or sets the interval represented in months used for computing calibration due date."""

    self_calibration: SelfCalibration | None = None
    """Gets or sets the last self-calibration of the asset."""

    is_ni_asset: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("is_ni_asset", "is_NI_asset", "isNIAsset"),
        serialization_alias="isNIAsset",
    )
    """Gets or sets whether this asset is an NI asset (true) or a third-party asset (false)."""

    id: str | None = None
    """Gets or sets unique identifier of the asset."""

    location: AssetLocation | None = None
    """Model for information about the asset location, presence,
    and the connection status of the system.
    """

    calibration_status: CalibrationStatus | None = None
    """Gets or sets the calibration category the asset belongs to
    based on the next due calibration date.
    """

    is_system_controller: bool | None = None
    """Gets or sets whether this asset represents a System Controller."""

    external_calibration: ExternalCalibration | None = None
    """Gets or sets the last external calibration of the asset."""

    workspace: str | None = None
    """Gets or sets the ID of the workspace."""

    properties: Dict[str, str] | None = None
    """	Gets or sets key-value-pair metadata associated with an asset."""

    keywords: List[str] | None = None
    """Gets or sets words or phrases associated with an asset."""

    last_updated_timestamp: datetime | None = None
    """Gets or sets an ISO-8601 timestamp for the last date
    that the asset had a property update.
    """

    file_ids: List[str] | None = None
    """Gets or sets all files linked to the asset."""

    supports_self_test: bool | None = None
    """Gets or sets whether the asset supports self-test."""

    supports_reset: bool | None = None
    """Gets or sets whether the asset supports reset."""

    part_number: str | None = None
    """Gets or sets part number of the asset."""

    out_for_calibration: bool | None = None
    """Get or set whether the asset is out for calibration."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_calibration.py sha256=165452bef885c302cf798f9cb7760009809af7cd1f7cbab2bfe5c69749220b69 bytes=2689 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_calibration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_calibration.py`
- sha256: `165452bef885c302cf798f9cb7760009809af7cd1f7cbab2bfe5c69749220b69`
- bytes: 2689

````python
from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class CalibrationStatus(Enum):
    """Calibration category the asset belongs to based on the next due calibration date."""

    OK = "OK"
    APPROACHING_RECOMMENDED_DUE_DATE = "APPROACHING_RECOMMENDED_DUE_DATE"
    PAST_RECOMMENDED_DUE_DATE = "PAST_RECOMMENDED_DUE_DATE"
    OUT_FOR_CALIBRATION = "OUT_FOR_CALIBRATION"


class TemperatureSensor(JsonModel):
    """Temperature sensor information."""

    name: str | None = None
    """Gets or sets sensor name."""

    reading: float
    """Gets or sets sensor reading."""


class SelfCalibration(JsonModel):
    temperature_sensors: List[TemperatureSensor] | None = None
    """Gets or sets an array of temperature sensor information."""

    is_limited: bool | None = None
    """Gets or sets whether the last self-calibration of the asset was a limited calibration."""

    date: datetime
    """Gets or sets ISO-8601 formatted timestamp specifying the last date the asset was self-calibrated."""


class CalibrationMode(Enum):
    """Whether SystemLink automatically discovered the calibration data for an asset or if it was manually entered."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


class ExternalCalibration(JsonModel):
    temperature_sensors: List[TemperatureSensor] | None = None
    """Gets or sets an array of temperature sensor information."""

    is_limited: bool | None = None
    """Gets or sets whether the last external calibration of the asset was a limited calibration."""

    date: datetime
    """Gets or sets ISO-8601 formatted timestamp specifying the last date the asset was externally calibrated."""

    recommended_interval: int
    """Gets or sets the manufacturer's recommended calibration interval in months."""

    next_recommended_date: datetime
    """Gets or sets ISO-8601 formatted timestamp specifying the recommended date for the next external calibration."""

    next_custom_due_date: datetime | None = None
    """Gets or sets ISO-8601 formatted timestamp specifying the date for the next external calibration."""

    resolved_due_date: datetime | None = None
    """Gets ISO-8601 formatted timestamp specifying the resolved due date for external calibration."""

    comments: str | None = None
    """Gets or sets calibration comments provided by an operator."""

    entry_type: CalibrationMode | None = None
    """Gets or sets whether automatically discovered the calibration data for an asset or manually entered."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_identification.py sha256=5d5f2fa44e06ec2b55efa6f67a0e21629be177a4099b6e5fff49afe8b4981087 bytes=931 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_identification.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_identification.py`
- sha256: `5d5f2fa44e06ec2b55efa6f67a0e21629be177a4099b6e5fff49afe8b4981087`
- bytes: 931

````python
"""Model for asset identification."""

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._asset_types import AssetBusType


class AssetIdentification(JsonModel):
    """Model for object containing properties which identify an asset.

    An asset is uniquely identified by a combination of:

    * ``bus_type``
    * ``model_name`` or ``model_number``
    * ``vendor_name`` or ``vendor_number``
    * ``serial_number``
    """

    model_name: str | None = None
    """Model name of the asset."""

    model_number: int | None = None
    """Model number of the asset."""

    serial_number: str | None = None
    """Serial number of the asset."""

    vendor_name: str | None = None
    """Vendor name of the asset."""

    vendor_number: int | None = None
    """Vendor number of the asset."""

    bus_type: AssetBusType | None = None
    """Bus type for the asset."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_location.py sha256=10cacd6ac444c7172f3491cbc66d69ea26e41286e373cc7e8ddb328753cb21fc bytes=2599 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_location.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_location.py`
- sha256: `10cacd6ac444c7172f3491cbc66d69ea26e41286e373cc7e8ddb328753cb21fc`
- bytes: 2599

````python
from enum import Enum

from nisystemlink.clients.core._uplink._json_model import JsonModel


class AssetPresenceStatus(Enum):
    """Status of an asset's presence in a system."""

    INITIALIZING = "INITIALIZING"
    UNKNOWN = "UNKNOWN"
    NOT_PRESENT = "NOT_PRESENT"
    PRESENT = "PRESENT"


class SystemConnection(Enum):
    """Whether the minion is connected to the server.

    For backward compatibility, APPROVED, UNSUPPORTED, and ACTIVATED are
    treated as DISCONNECTED. CONNECTED_UPDATE_PENDING,
    CONNECTED_UPDATE_SUCCESSFUL, and CONNECTED_UPDATE_FAILED are treated
    as CONNECTED.
    """

    APPROVED = "APPROVED"
    DISCONNECTED = "DISCONNECTED"
    CONNECTED_UPDATE_PENDING = "CONNECTED_UPDATE_PENDING"
    CONNECTED = "CONNECTED"
    CONNECTED_UPDATE_FAILED = "CONNECTED_UPDATE_FAILED"
    UNSUPPORTED = "UNSUPPORTED"
    ACTIVATED = "ACTIVATED"
    CONNECTED_UPDATE_SUCCESSFUL = "CONNECTED_UPDATE_SUCCESSFUL"


class AssetPresenceWithSystemConnection(JsonModel):
    """Asset presence and system connection information."""

    asset_presence: AssetPresenceStatus
    """Gets or sets the status of an asset's presence in a system."""

    system_connection: SystemConnection | None = None
    """Gets or sets whether the minion is connected to the server
    and has updated it with its data.
    """


class AssetPresence(JsonModel):
    """Model for the presence of an asset."""

    asset_presence: AssetPresenceStatus
    """Gets or sets the status of an asset's presence in a system."""


class _AssetLocation(JsonModel):
    """Local model for asset location and presence information."""

    minion_id: str | None = None
    """Gets or sets identifier of the minion where the asset is located."""

    physical_location: str | None = None
    """Gets or sets the physical location of the asset."""

    parent: str | None = None
    """Gets or sets the parent of the asset."""

    resource_uri: str | None = None
    """Gets or sets identifier of a resource."""

    slot_number: int | None = None
    """Gets or sets the number of the slot in which the asset is located."""


class AssetLocation(_AssetLocation):
    """Asset location and system connection information."""

    state: AssetPresenceWithSystemConnection
    """Presence of an asset and the connection of the system in which it resides."""


class AssetLocationForCreate(_AssetLocation):
    """Asset presence information used during create."""

    state: AssetPresence
    """Model for the presence of an asset."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_types.py sha256=34df66b44f693cd622195f865777e780c3ad705f849e5664c8b50ff59e493d67 bytes=831 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_types.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_types.py`
- sha256: `34df66b44f693cd622195f865777e780c3ad705f849e5664c8b50ff59e493d67`
- bytes: 831

````python
from enum import Enum


class AssetBusType(Enum):
    """All supported bus types for an asset."""

    BUILT_IN_SYSTEM = "BUILT_IN_SYSTEM"
    PCI_PXI = "PCI_PXI"
    USB = "USB"
    GPIB = "GPIB"
    VXI = "VXI"
    SERIAL = "SERIAL"
    TCP_IP = "TCP_IP"
    CRIO = "CRIO"
    SCXI = "SCXI"
    CDAQ = "CDAQ"
    SWITCH_BLOCK = "SWITCH_BLOCK"
    SCC = "SCC"
    FIRE_WIRE = "FIRE_WIRE"
    ACCESSORY = "ACCESSORY"
    CAN = "CAN"
    SWITCH_BLOCK_DEVICE = "SWITCH_BLOCK_DEVICE"
    SLSC = "SLSC"


class AssetType(Enum):
    """All supported asset types."""

    GENERIC = "GENERIC"
    DEVICE_UNDER_TEST = "DEVICE_UNDER_TEST"
    FIXTURE = "FIXTURE"
    SYSTEM = "SYSTEM"


class AssetDiscoveryType(Enum):
    """All discovery types."""

    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_utilization_history_item.py sha256=f27f57ef7d318ef399acaa88c360d009e65236d72bc5b951d8194967bee6d1eb bytes=1279 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_utilization_history_item.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_utilization_history_item.py`
- sha256: `f27f57ef7d318ef399acaa88c360d009e65236d72bc5b951d8194967bee6d1eb`
- bytes: 1279

````python
from datetime import datetime

from nisystemlink.clients.core._uplink._json_model import JsonModel


class AssetUtilizationHistoryItem(JsonModel):
    """Model representing an asset utilization history record."""

    utilization_identifier: str | None = None
    """String representing the unique identifier of an asset utilization history record."""

    asset_identifier: str | None = None
    """String representing the unique identifier of an asset."""

    minion_id: str | None = None
    """Identifier of the minion where the asset is located."""

    category: str | None = None
    """String representing the utilization task category."""

    task_name: str | None = None
    """String representing the name of the task."""

    user_name: str | None = None
    """String representing the name of the operator who utilized the asset."""

    start_timestamp: datetime | None = None
    """A date time value which can be used to specify the start of an utilization."""

    end_timestamp: datetime | None = None
    """A date time value which can be used to specify the end of an utilization."""

    heartbeat_timestamp: datetime | None = None
    """A date time value which can be used to specify the heartbeat of an utilization."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_utilization_history_response.py sha256=201cc89b7fe1101b9d07e59deda2771890e74f3d6c929091f5456f5cf0d30dd2 bytes=408 -->
## FILE: nisystemlink/clients/assetmanagement/models/_asset_utilization_history_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_asset_utilization_history_response.py`
- sha256: `201cc89b7fe1101b9d07e59deda2771890e74f3d6c929091f5456f5cf0d30dd2`
- bytes: 408

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._asset_utilization_history_item import AssetUtilizationHistoryItem


class AssetUtilizationHistoryResponse(WithPaging):
    """Response model for asset utilization history query."""

    asset_utilizations: List[AssetUtilizationHistoryItem] | None = None
    """Array of asset utilizations."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_create_asset_request.py sha256=f215f05d802727f3ab3f06ae9d6d49c32f67f4f749a059b27cec37efa6b6f1e1 bytes=3551 -->
## FILE: nisystemlink/clients/assetmanagement/models/_create_asset_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_create_asset_request.py`
- sha256: `f215f05d802727f3ab3f06ae9d6d49c32f67f4f749a059b27cec37efa6b6f1e1`
- bytes: 3551

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field

from ._asset import (
    AssetBusType,
    AssetDiscoveryType,
    AssetType,
    ExternalCalibration,
    SelfCalibration,
    TemperatureSensor,
)
from ._asset_location import AssetLocationForCreate


class CreateAssetRequest(JsonModel):
    """Model for an object describing the properties for creating an asset."""

    model_name: str | None = None
    """Gets or sets model name of the asset."""

    model_number: int | None = None
    """Gets or sets model number of the asset."""

    serial_number: str | None = None
    """Gets or sets serial number of the asset."""

    vendor_name: str | None = None
    """Gets or sets vendor name of the asset."""

    vendor_number: int | None = None
    """Gets or sets vendor number of the asset."""

    bus_type: AssetBusType | None = None
    """Gets or sets all supported bus types for an asset."""

    name: str | None = None
    """Gets or sets name of the asset."""

    asset_type: AssetType | None = None
    """Gets or sets all supported asset types."""

    firmware_version: str | None = None
    """Gets or sets firmware version of the asset."""

    hardware_version: str | None = None
    """Gets or sets hardware version of the asset."""

    visa_resource_name: str | None = None
    """Gets or sets VISA resource name of the asset."""

    temperature_sensors: List[TemperatureSensor] | None = None
    """Gets or sets an array of temperature sensor information."""

    supports_self_calibration: bool | None = None
    """Gets or sets whether the asset supports self-calibration."""

    supports_external_calibration: bool | None = None
    """Gets or sets whether the asset supports external calibration."""

    custom_calibration_interval: int | None = None
    """Gets or sets the interval represented in months used for computing calibration due date."""

    self_calibration: SelfCalibration | None = None
    """Gets or sets the last self-calibration of the asset."""

    is_ni_asset: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("is_ni_asset", "is_NI_asset", "isNIAsset"),
        serialization_alias="isNIAsset",
    )
    """Gets or sets whether this asset is an NI asset (true) or a third-party asset (false)."""

    workspace: str | None = None
    """Gets or sets the ID of the workspace."""

    location: AssetLocationForCreate
    """Model for information about the asset location, presence,
    and the connection status of the system.
    """

    external_calibration: ExternalCalibration | None = None
    """Gets or sets the last external calibration of the asset."""

    properties: Dict[str, str] | None = None
    """	Gets or sets key-value-pair metadata associated with an asset."""

    keywords: List[str] | None = None
    """Gets or sets words or phrases associated with an asset."""

    discovery_type: AssetDiscoveryType | None = None
    """Gets or sets the discovery type."""

    file_ids: List[str] | None = None
    """Gets or sets all files linked to the asset."""

    supports_self_test: bool | None = None
    """Gets or sets whether the asset supports self-test."""

    supports_reset: bool | None = None
    """Gets or sets whether the asset supports reset."""

    part_number: str | None = None
    """Gets or sets part number of the asset."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_create_assets_partial_success_response.py sha256=a4830255a092b82f085c1046846b12fa312cde427828eda84fc142db3e455688 bytes=670 -->
## FILE: nisystemlink/clients/assetmanagement/models/_create_assets_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_create_assets_partial_success_response.py`
- sha256: `a4830255a092b82f085c1046846b12fa312cde427828eda84fc142db3e455688`
- bytes: 670

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._asset import Asset
from ._create_asset_request import CreateAssetRequest


class CreateAssetsPartialSuccessResponse(JsonModel):
    """Model for create Assets Partial Success Response."""

    assets: List[Asset] | None = None
    """Gets or sets array of created assets."""

    failed: List[CreateAssetRequest] | None = None
    """Gets or sets array of assets create requests that failed."""

    error: ApiError | None = None
    """Gets or sets error if the create operation failed."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_delete_assets_response.py sha256=79286d34036079dbc56dcff8beff8ef36416929a803122790cba2b805a7bb5db bytes=614 -->
## FILE: nisystemlink/clients/assetmanagement/models/_delete_assets_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_delete_assets_response.py`
- sha256: `79286d34036079dbc56dcff8beff8ef36416929a803122790cba2b805a7bb5db`
- bytes: 614

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteAssetsResponse(JsonModel):
    """Model for delete Assets Response containing the ids of the assets which were deleted"""

    ids: List[str] | None = None
    """Gets or sets array of asset identifiers which were deleted."""

    failed: List[str] | None = None
    """Gets or sets array of asset identifiers that failed to delete."""

    error: ApiError | None = None
    """Gets or sets error if the delete operation failed."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_link_files_partial_success_response.py sha256=cf35c2c54cf12eaaf49b2e1fbdaf4d1ff10848f87979843f03e54c947c6645ce bytes=609 -->
## FILE: nisystemlink/clients/assetmanagement/models/_link_files_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_link_files_partial_success_response.py`
- sha256: `cf35c2c54cf12eaaf49b2e1fbdaf4d1ff10848f87979843f03e54c947c6645ce`
- bytes: 609

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class LinkFilesPartialSuccessResponse(JsonModel):
    """Model for a Link Files Partial Success Response."""

    succeeded: List[str] | None = None
    """Gets or sets array of file IDs that were successfully linked to assets."""

    failed: List[str] | None = None
    """Gets or sets array of file IDs that failed to link to assets."""

    error: ApiError | None = None
    """Gets or sets error if the link file operation failed."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_asset_utilization_history_request.py sha256=280b8f7de7e3ee4c0ccb9ebf317133a93dc31ac9d52479182a69650e406c90ea bytes=1586 -->
## FILE: nisystemlink/clients/assetmanagement/models/_query_asset_utilization_history_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_query_asset_utilization_history_request.py`
- sha256: `280b8f7de7e3ee4c0ccb9ebf317133a93dc31ac9d52479182a69650e406c90ea`
- bytes: 1586

````python
from datetime import datetime
from enum import Enum

from nisystemlink.clients.core._uplink._with_paging import WithPaging


class UtilizationOrderBy(Enum):
    """Field by which asset utilization history records can be ordered/sorted."""

    START_TIMESTAMP = "START_TIMESTAMP"


class QueryAssetUtilizationHistoryRequest(WithPaging):
    """Model for object containing filters for asset utilization and assets."""

    utilization_filter: str | None = None
    """
    The filter criteria for asset utilization. Consists of a string of queries
    composed using AND/OR operators. Valid properties: MinionId, Category, UserName, TaskName,
    StartTimestamp, EndTimestamp.
    """

    asset_filter: str | None = None
    """
    The filter criteria for assets. Consists of a string of queries composed
    using AND/OR operators. Valid properties include AssetIdentifier, SerialNumber, ModelName,
    VendorName, Location.MinionId, and many others.
    """

    take: int | None = None
    """The maximum number of asset utilization history records to return."""

    order_by: UtilizationOrderBy | None = None
    """
    The field to order results by. If not provided, default ordering is applied.
    """

    order_by_descending: bool | None = None
    """Whether to return the asset utilization history records in descending order."""

    start_time: datetime | None = None
    """Start of the date range. Defaults to 90 days ago."""

    end_time: datetime | None = None
    """End of the date range. Defaults to current time."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_assets_request.py sha256=ad74189f773e2284742f9bbade0952557409ef8dc4558ba40aa3dc99a534068b bytes=4121 -->
## FILE: nisystemlink/clients/assetmanagement/models/_query_assets_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_query_assets_request.py`
- sha256: `ad74189f773e2284742f9bbade0952557409ef8dc4558ba40aa3dc99a534068b`
- bytes: 4121

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class OrderBy(Enum):
    """Field by which assets can be ordered/sorted. If OrderBy is not specified, no sorting will applied."""

    LAST_UPDATED_TIMESTAMP = "LAST_UPDATED_TIMESTAMP"


class AssetField(str, Enum):
    """Model for an object describing an asset with all of its properties."""

    MODEL_NAME = "MODEL_NAME"
    MODEL_NUMBER = "MODEL_NUMBER"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    VENDOR_NAME = "VENDOR_NAME"
    VENDOR_NUMBER = "VENDOR_NUMBER"
    BUS_TYPE = "BUS_TYPE"
    NAME = "NAME"
    ASSET_TYPE = "ASSET_TYPE"
    DISCOVERY_TYPE = "DISCOVERY_TYPE"
    FIRMWARE_VERSION = "FIRMWARE_VERSION"
    HARDWARE_VERSION = "HARDWARE_VERSION"
    VISA_RESOURCE_NAME = "VISA_RESOURCE_NAME"
    TEMPERATURE_SENSORS = "TEMPERATURE_SENSORS"
    SUPPORTS_SELF_CALIBRATION = "SUPPORTS_SELF_CALIBRATION"
    SUPPORTS_EXTERNAL_CALIBRATION = "SUPPORTS_EXTERNAL_CALIBRATION"
    CUSTOM_CALIBRATION_INTERVAL = "CUSTOM_CALIBRATION_INTERVAL"
    SELF_CALIBRATION = "SELF_CALIBRATION"
    IS_NI_ASSET = "IS_NI_ASSET"
    ID = "ID"
    LOCATION = "LOCATION"
    CALIBRATION_STATUS = "CALIBRATION_STATUS"
    IS_SYSTEM_CONTROLLER = "IS_SYSTEM_CONTROLLER"
    EXTERNAL_CALIBRATION = "EXTERNAL_CALIBRATION"
    WORKSPACE = "WORKSPACE"
    PROPERTIES = "PROPERTIES"
    KEYWORDS = "KEYWORDS"
    LAST_UPDATE = "LAST_UPDATE"
    FILES_IDS = "FILES_IDS"
    SUPPORTS_SELF_RESET = "SUPPORTS_SELF_RESET"
    SUPPORTS_RESET = "SUPPORTS_RESET"
    PART_NUMBER = "PART_NUMBER"
    OUT_FOR_CALIBRATION = "OUT_FOR_CALIBRATION"


class QueryAssetsRequest(JsonModel):
    """Model for object containing filters to apply when retrieving assets."""

    projection: List[AssetField] | None = None
    """
    Gets or sets the projection to be used when retrieving the assets. If not specified,
    all properties will be returned.
    """

    skip: int | None = None
    """Gets or sets the number of resources to skip in the result when paging."""

    take: int | None = None
    """Gets or sets how many resources to return in the result, or -1 to use a default defined by the service."""

    order_by: OrderBy | None = None
    """Field by which assets can be ordered/sorted. If OrderBy is not specified, no sorting will applied."""

    descending: bool | None = None
    """Whether to return the assets in the descending order. If OrderBy is not specified, this property is ignored."""

    return_count: bool | None = None
    """
    Gets or sets Whether to return the total number of assets which match the provided filter,
    disregarding the take value.
    """

    filter: str | None = None
    """Gets or sets the filter criteria for assets. Consists of a string of queries composed using AND/OR operators."""


class _QueryAssetsRequest(JsonModel):
    """Model for object containing filters to apply when retrieving assets."""

    projection: str | None = None
    """
    Gets or sets the projection to be used when retrieving the assets. If not specified,
    all properties will be returned.
    """

    skip: int | None = None
    """Gets or sets the number of resources to skip in the result when paging."""

    take: int | None = None
    """Gets or sets how many resources to return in the result, or -1 to use a default defined by the service."""

    order_by: OrderBy | None = None
    """Field by which assets can be ordered/sorted. If OrderBy is not specified, no sorting will applied."""

    descending: bool | None = None
    """Whether to return the assets in the descending order. If OrderBy is not specified, this property is ignored."""

    return_count: bool | None = None
    """
    Gets or sets Whether to return the total number of assets which match the provided filter,
    disregarding the take value.
    """

    filter: str | None = None
    """Gets or sets the filter criteria for assets. Consists of a string of queries composed using AND/OR operators."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_assets_response.py sha256=8ddece575ff69a01bca0a6fe3921b8b051a942fd8b388584f21cf678844a3c89 bytes=482 -->
## FILE: nisystemlink/clients/assetmanagement/models/_query_assets_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_query_assets_response.py`
- sha256: `8ddece575ff69a01bca0a6fe3921b8b051a942fd8b388584f21cf678844a3c89`
- bytes: 482

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._asset import Asset


class QueryAssetsResponse(JsonModel):
    """Model for assets Response containing the assets satisfying the query and the total count of matching assets."""

    assets: List[Asset] | None = None
    """Gets or sets array of assets."""

    total_count: int | None = None
    """Gets or sets the total number of Assets which match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_start_utilization_partial_success_response.py sha256=bec3dc97a08873a8e0e5ebcc850ebad31ba77493e346a1b320852c21ee4bd63f bytes=854 -->
## FILE: nisystemlink/clients/assetmanagement/models/_start_utilization_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_start_utilization_partial_success_response.py`
- sha256: `bec3dc97a08873a8e0e5ebcc850ebad31ba77493e346a1b320852c21ee4bd63f`
- bytes: 854

````python
"""Model for start utilization partial success response."""

from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._asset_identification import AssetIdentification


class StartUtilizationPartialSuccessResponse(JsonModel):
    """Response model for start utilization operation with partial success support."""

    error: ApiError | None = None
    """Error information if any failures occurred."""

    assets_with_started_utilization: List[AssetIdentification] | None = None
    """Array containing the asset identification data for the assets that started being utilized."""

    failed: List[AssetIdentification] | None = None
    """Array containing the asset identification data for the assets that failed to start being utilized."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_start_utilization_request.py sha256=598c6e88ee8657b318c74fd0d0082cf32af6e6d85506e848f76f042901b250e0 bytes=1279 -->
## FILE: nisystemlink/clients/assetmanagement/models/_start_utilization_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_start_utilization_request.py`
- sha256: `598c6e88ee8657b318c74fd0d0082cf32af6e6d85506e848f76f042901b250e0`
- bytes: 1279

````python
"""Model for start utilization request."""

from datetime import datetime
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._asset_identification import AssetIdentification


class StartUtilizationRequest(JsonModel):
    """Request model for starting asset utilization tracking."""

    utilization_identifier: str | None = None
    """String representing the unique identifier of an asset utilization history record."""

    minion_id: str | None = None
    """Identifier of the minion where the utilized assets are located."""

    asset_identifications: List[AssetIdentification] | None = None
    """Array of the identification information for the assets which are utilized.
    The maximum number of asset identifications allowed per request is 100."""

    utilization_category: str | None = None
    """String representing the utilization category."""

    task_name: str | None = None
    """String representing the name of the task."""

    user_name: str | None = None
    """String representing the name of the operator who utilized the asset."""

    utilization_timestamp: datetime | None = None
    """A date time value which can be used to specify the start of an utilization."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_update_utilization_partial_success_response.py sha256=29e7a3a5dcac8290fbd000f55f5aaa6b0bdefc32dc65f717017a619d9f37c311 bytes=709 -->
## FILE: nisystemlink/clients/assetmanagement/models/_update_utilization_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_update_utilization_partial_success_response.py`
- sha256: `29e7a3a5dcac8290fbd000f55f5aaa6b0bdefc32dc65f717017a619d9f37c311`
- bytes: 709

````python
"""Model for update utilization partial success response."""

from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class UpdateUtilizationPartialSuccessResponse(JsonModel):
    """Response model for update utilization operation with partial success support."""

    error: ApiError | None = None
    """Error information if any failures occurred."""

    updated_utilization_ids: List[str] | None = None
    """Array of utilization identifiers for the entries that were updated."""

    failed: List[str] | None = None
    """Array of utilization identifiers for the entries that failed to update."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_update_utilization_request.py sha256=2121097d901bb7cb5c49f3bfd0c2f4128a2add969191a872a60732c8294ab0d5 bytes=590 -->
## FILE: nisystemlink/clients/assetmanagement/models/_update_utilization_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/assetmanagement/models/_update_utilization_request.py`
- sha256: `2121097d901bb7cb5c49f3bfd0c2f4128a2add969191a872a60732c8294ab0d5`
- bytes: 590

````python
"""Model for updating utilization (heartbeat or end)."""

from datetime import datetime
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class _UpdateUtilizationRequest(JsonModel):
    """Request model for updating utilization (heartbeat or end)."""

    utilization_identifiers: List[str] | None = None
    """Array representing the unique identifier of an asset utilization history record."""

    utilization_timestamp: datetime | None = None
    """A date time value which can be used to specify the heartbeat timestamp."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/__init__.py sha256=66abb5ca686905f889311aa638c2a94e14f433c5e588aaf9949efd4af8253b9d bytes=370 -->
## FILE: nisystemlink/clients/core/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/__init__.py`
- sha256: `66abb5ca686905f889311aa638c2a94e14f433c5e588aaf9949efd4af8253b9d`
- bytes: 370

````python
# -*- coding: utf-8 -*-

from ._api_error import ApiError
from ._api_exception import ApiException
from ._http_configuration import HttpConfiguration
from ._cloud_http_configuration import CloudHttpConfiguration
from ._jupyter_http_configuration import JupyterHttpConfiguration
from ._http_configuration_manager import HttpConfigurationManager

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_error.py sha256=9d2bcb3f7fdd57f7ee6dee4fbd8062c6c9ce299cb10d27e862b99877bbebb118 bytes=842 -->
## FILE: nisystemlink/clients/core/_api_error.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_api_error.py`
- sha256: `9d2bcb3f7fdd57f7ee6dee4fbd8062c6c9ce299cb10d27e862b99877bbebb118`
- bytes: 842

````python
# -*- coding: utf-8 -*-

"""Implementation of ApiError."""

from typing import List

from ._uplink._json_model import JsonModel


class ApiError(JsonModel):
    """Represents the standard error structure for SystemLink API responses."""

    name: str | None = None
    """String error code."""

    code: int | None = None
    """Numeric error code."""

    message: str | None = None
    """Complete error message."""

    args: List[str] = []
    """Positional arguments for the error code."""

    resource_type: str | None = None
    """Type of resource associated with the error."""

    resource_id: str | None = None
    """Identifier of the resource associated with the error."""

    inner_errors: List["ApiError"] = []
    """Inner errors when the top-level error represents more than one error."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_exception.py sha256=5be8d03270d73ca3dd7a4f040bf199b584d7bc1a9a30511273e437fc6db80f34 bytes=3423 -->
## FILE: nisystemlink/clients/core/_api_exception.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_api_exception.py`
- sha256: `5be8d03270d73ca3dd7a4f040bf199b584d7bc1a9a30511273e437fc6db80f34`
- bytes: 3423

````python
# -*- coding: utf-8 -*-

"""Implementation of ApiException."""

import typing
from typing import Any, Dict

from nisystemlink.clients import core


class ApiException(Exception):
    """Represents errors that occur when calling SystemLink APIs."""

    def __init__(
        self,
        message: str | None = None,
        error: core.ApiError | None = None,
        http_status_code: int | None = None,
        inner: Exception | None = None,
        response_data: Dict[str, Any] | None = None,
    ) -> None:
        """Initialize an exception.

        Args:
            message: The message describing the error.
            error: The error returned by the API.
            http_status_code: The HTTP status code, if this exception was the result of
                an HTTP error.
            inner: The inner exception that caused the error.
            response_data: The full parsed JSON response body, if the server returned
                one. Useful when an error response still contains actionable data.
        """
        self._message = message
        self._error = error
        self._http_status_code = http_status_code
        self._inner = inner
        self._response_data = response_data

    @property
    def message(self) -> str | None:  # noqa:D401
        """The error message."""
        return self._message

    @property
    def error(self) -> core.ApiError | None:  # noqa: D401
        """The error information returned by the SystemLink API, or None if the API did
        not return one or the error occurred trying to call the API.
        """
        if self._error is None:
            return None
        else:
            return self._error.model_copy()

    @property
    def http_status_code(self) -> int | None:  # noqa: D401
        """The HTTP status code, if this exception was the result of an HTTP error."""
        return self._http_status_code

    @property
    def inner_exception(self) -> Exception | None:  # noqa: D401
        """The exception that caused this failure, if any."""
        return self._inner

    @property
    def response_data(self) -> Dict[str, Any] | None:  # noqa: D401
        """The full parsed JSON response body returned by the server, or None.

        This is populated for HTTP error responses that include a JSON body.
        It allows callers to recover structured data from error responses — for
        example, a partial-failure response may contain result data alongside the error details.
        """
        return dict(self._response_data) if self._response_data is not None else None

    def __str__(self) -> str:
        txt = self._message or "API exception occurred"
        if self._error:
            txt += "\n\n" + str(self._error)
        return txt

    def __eq__(self, other: object) -> bool:
        other_ = typing.cast(ApiException, other)
        return all(
            (
                isinstance(other, ApiException),
                self._message == other_._message,
                self._error == other_._error,
                self._http_status_code == other_._http_status_code,
                self._inner == other_._inner,
                self._response_data == other_._response_data,
            )
        )

    def __hash__(self) -> int:
        return hash((self._message, self._error, self._inner))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_info.py sha256=051995d4e7dbc7007465764b91124cd55f4ac86b111396f0f7b8a92fdf37c69b bytes=364 -->
## FILE: nisystemlink/clients/core/_api_info.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_api_info.py`
- sha256: `051995d4e7dbc7007465764b91124cd55f4ac86b111396f0f7b8a92fdf37c69b`
- bytes: 364

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class Operation(JsonModel):
    """Represents an operation that can be performed on a data frame."""

    available: bool
    """Whether or not the operation is available to the caller (e.g. due to permissions)."""

    version: int
    """The version of the available operation."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_cloud_http_configuration.py sha256=f558fab8572760132ef0a15bbf811687263324c06b6c607522762e860e298da5 bytes=676 -->
## FILE: nisystemlink/clients/core/_cloud_http_configuration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_cloud_http_configuration.py`
- sha256: `f558fab8572760132ef0a15bbf811687263324c06b6c607522762e860e298da5`
- bytes: 676

````python
# -*- coding: utf-8 -*-

"""Implementation of CloudHttpConfiguration."""

from nisystemlink.clients import core


class CloudHttpConfiguration(core.HttpConfiguration):
    """An :class:`HttpConfiguration` specifically for use with SystemLink Cloud."""

    _CLOUD_URI = "https://api.systemlinkcloud.com"

    def __init__(self, api_key: str) -> None:
        """Initialize a configuration for SystemLink Cloud using API key-based authentication.

        Args:
            api_key: The API key to send with requests.

        Raises:
            ValueError: if ``api_key`` is empty.
        """
        super().__init__(self._CLOUD_URI, api_key=api_key)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_http_configuration.py sha256=9bf0bb96bb9c788e0ae57efc8326d90d5db003b4f03162579a0ac5bb7ea545b1 bytes=5622 -->
## FILE: nisystemlink/clients/core/_http_configuration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_http_configuration.py`
- sha256: `9bf0bb96bb9c788e0ae57efc8326d90d5db003b4f03162579a0ac5bb7ea545b1`
- bytes: 5622

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpConfiguration."""

import pathlib
import urllib.parse
from typing import Dict


class HttpConfiguration:
    """Represents the configuration for accessing a SystemLink service over HTTP."""

    DEFAULT_TIMEOUT_MILLISECONDS = 60000
    """The default value of :attr:`timeout_milliseconds` to use when making API calls."""

    _SYSTEM_LINK_API_KEY_HEADER = "x-ni-api-key"

    def __init__(
        self,
        server_uri: str,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        cert_path: pathlib.Path | None = None,
        workspace: str | None = None,
        verify: bool = True,
    ) -> None:
        """Initialize a configuration.

        If neither ``api_key`` nor ``username`` and ``password`` are set, the
        configuration will use anonymous access, and any API calls that require
        authorization will fail.

        Args:
            server_uri: The scheme, host, and port (if not default) of the web server
                hosting the SystemLink service to connect to. Additional Uri properties
                such as ``urllib.parse.urlparse().path`` and
                ``urllib.parse.urlparse().query`` are ignored.
            api_key: The API key to send with requests.
            username: The name of the user to use when authorization is required.
            password: The user's password to use when authorization is required.
            cert_path: Local path to an SSL certificate file.
            workspace: ID of workspace to use for client operations.
            verify: Verify the security certificate for connection

        Raises:
            ValueError: if ``server_uri`` is missing scheme or host information.
            ValueError: if ``username`` or ``password`` is set, but not both.
        """
        uri = urllib.parse.urlsplit(server_uri)
        if not uri.scheme:
            raise ValueError(
                "Scheme (e.g. http) not included in server_uri: '{}'".format(uri)
            )
        if not uri.hostname:
            raise ValueError(
                "Host (e.g. foo.com) not included in server_uri: '{}'".format(uri)
            )
        self._server_uri = urllib.parse.urlunsplit(uri[:2] + ("", "", ""))

        self._api_keys: Dict[str, str] | None = None
        self._username: str | None = None
        self._password: str | None = None
        if api_key:
            self._api_keys = {self._SYSTEM_LINK_API_KEY_HEADER: api_key}
        elif username or password:
            if not username or not password:
                raise ValueError("If username or password is set, both must be set")
            self._username = username
            self._password = password

        self._cert_path = cert_path

        self._user_agent: str | None = ""

        self._timeout_ms = self.DEFAULT_TIMEOUT_MILLISECONDS

        self._workspace = workspace

        self._verify = verify

    @property
    def verify(self) -> bool:
        """Verify the security certificate for connection."""
        return self._verify

    @verify.setter
    def verify(self, value: bool) -> None:
        self._verify = value

    @property
    def timeout_milliseconds(self) -> int:  # noqa: D401
        """The number of milliseconds before a request times out with an error.

        Changing the timeout will not affect APIs that have already read the
        configuration.
        """
        return self._timeout_ms

    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: int) -> None:
        self._timeout_ms = value

    @property
    def user_agent(self) -> str | None:  # noqa: D401
        """The string to pass the web server as the product name or names making the
        request, or None to use a library-specific default.

        Changing the user-agent will not affect APIs that have already read the
        configuration.
        """
        return self._user_agent or None

    @user_agent.setter
    def user_agent(self, value: str | None) -> None:
        self._user_agent = value

    @property
    def api_keys(self) -> Dict[str, str] | None:  # noqa: D401
        """The available API keys to use for authorization, or None if none were provided."""
        return dict(self._api_keys) if self._api_keys else None

    @property
    def server_uri(self) -> str:  # noqa: D401
        """The ``urllib.parse.urlparse().scheme``, ``urllib.parse.urlparse().hostname``,
        and ``urllib.parse.urlparse().port`` of the web server hosting the SystemLink
        service to connect to.

        Additional Uri properties such as ``urllib.parse.urlparse().path`` and
        ``urllib.parse.urlparse().query`` are ignored.
        """
        return self._server_uri

    @property
    def username(self) -> str | None:  # noqa: D401
        """The username to use for HTTP authentication, or None if none was provided."""
        return self._username

    @property
    def password(self) -> str | None:  # noqa: D401
        """The password to use for HTTP authentication, or None if none was provided."""
        return self._password

    @property
    def cert_path(self) -> pathlib.Path | None:
        """Local path to an SSL certificate file."""
        return self._cert_path

    @property
    def workspace(self) -> str | None:  # noqa: D401
        """ID of workspace to use for Client operations."""
        return self._workspace
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_http_configuration_manager.py sha256=d67e685d1ec17e5c58921603597240a27ccc1c90d88c16af36049929b2d74ec4 bytes=9634 -->
## FILE: nisystemlink/clients/core/_http_configuration_manager.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_http_configuration_manager.py`
- sha256: `d67e685d1ec17e5c58921603597240a27ccc1c90d88c16af36049929b2d74ec4`
- bytes: 9634

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpConfigurationManager."""

import json
import pathlib
from typing import Dict

import yaml
from nisystemlink.clients import core
from nisystemlink.clients.core._internal._http_configuration_file import (
    HttpConfigurationFile,
)
from nisystemlink.clients.core._internal._path_constants import PathConstants


class HttpConfigurationManager:
    """Factory for :class:`HttpConfiguration` objects."""

    HTTP_MASTER_CONFIGURATION_ID = "SYSTEMLINK_MASTER"
    """The default ID of the SystemLink Server's configuration on systems registered using SystemLink Client."""

    HTTP_LOCALHOST_CONFIGURATION_ID = "SYSTEMLINK_LOCALHOST"
    """The default ID of the SystemLink Server's configuration on the SystemLink Server itself."""

    _HTTP_JUPYTER_CONFIGURATION_ID = "SYSTEMLINK_VIRTUAL_JUPYTER"
    """Virtual ID of SystemLink Server's configuration for Jupyter Notebook execution on SLE."""

    _SALT_GRAINS_WORKSPACE_KEY = "systemlink_workspace"
    """Key of Workspace ID stored in the salt grains config file."""

    _configs: Dict[str, core.HttpConfiguration] | None = None
    _virtual_configs: Dict[str, core.HttpConfiguration] | None = None

    @classmethod
    def get_configuration(
        cls, id: str | None = None, enable_fallbacks: bool | None = True
    ) -> core.HttpConfiguration:
        """Get the requested or default configuration.

        Args:
            id: The ID of the configuration to find.
            enable_fallbacks: Whether or not to fallback to other known configurations,
                if ``id`` is unavailable.

        Returns:
            The configuration.

        Raises:
            ValueError: if ``id`` is None and ``enable_fallbacks`` is False.
            ApiException: if the specified (or default) configuration is not found.
        """
        if id is not None:
            id = id.upper()
        else:
            if not enable_fallbacks:
                raise ValueError("id cannot be None if enable_fallbacks is False")
            fallback_configuration = cls._fallback()
            if fallback_configuration is None:
                raise core.ApiException("No SystemLink configurations available")
            return fallback_configuration

        if cls._configs is None:
            cls._configs = cls._read_configurations()
        config = cls._configs.get(id)
        if config is not None:
            return config
        if enable_fallbacks:
            fallback_configuration = cls._fallback()
            if fallback_configuration is None:
                raise core.ApiException(
                    "Configuration with ID {!r} was not found, and no ".format(id)
                    + "fallback configurations were available."
                )
            return fallback_configuration
        raise core.ApiException("Configuration with ID {!r} was not found.".format(id))

    @classmethod
    def _fallback(cls) -> core.HttpConfiguration | None:
        """Attempt to acquire fallback HTTP configurations.

        Returns:
            The best available fallback configuration, or None if no such
            configurations are available.
        """
        if cls._configs is None:
            cls._configs = cls._read_configurations()
        if cls._virtual_configs is None:
            cls._virtual_configs = cls._read_virtual_configurations()

        master_config = cls._configs.get(cls.HTTP_MASTER_CONFIGURATION_ID)
        if master_config is not None:
            return master_config
        localhost_config = cls._configs.get(cls.HTTP_LOCALHOST_CONFIGURATION_ID)
        if localhost_config is not None:
            return localhost_config

        jupyter_config = cls._virtual_configs.get(cls._HTTP_JUPYTER_CONFIGURATION_ID)
        if jupyter_config is not None:
            return jupyter_config

        return None

    @classmethod
    def _read_virtual_configurations(cls) -> Dict[str, core.HttpConfiguration]:
        """Loads the virtual HTTP configurations.

        Returns:
            A dictionary mapping each loaded configuration ID to its corresponding
            :class:`HttpConfiguration`.
        """
        configurations: Dict[str, core.HttpConfiguration] = {}
        try:
            configurations[cls._HTTP_JUPYTER_CONFIGURATION_ID] = (
                core.JupyterHttpConfiguration()
            )
        except KeyError:
            # Env variables for Jupyter notebook execution are not available.
            pass

        return configurations

    @classmethod
    def _read_configurations(cls) -> Dict[str, core.HttpConfiguration]:
        """Discover and loads the HTTP configuration files.

        Returns:
            A dictionary mapping each loaded configuration ID to its corresponding
            :class:`HttpConfiguration`.

        Raises:
            ApiException: if multiple configurations with the same ID are simultaneously
                present.
            ApiException: if an OS or permission error prevents reading the directory
                that contains HTTP configurations.
        """
        configurations: Dict[str, core.HttpConfiguration] = {}
        path = cls._http_configurations_directory()
        if not path.exists():
            return configurations
        try:
            json_files = path.glob("*.json")
        except PermissionError as e:
            raise core.ApiException(
                "Not authorized to access HTTP configurations directory: " + str(e)
            )
        except OSError as e:
            raise core.ApiException(
                "Error while accessing HTTP configurations directory: " + str(e)
            )

        workspace = cls._read_system_workspace()

        for json_file in json_files:
            try:
                config_file = cls._read_configuration_file(json_file)
                if config_file is None or config_file.id is None:
                    continue
                if config_file.id in configurations:
                    raise core.ApiException("Duplicate configuration IDs detected.")
                if not config_file.uri:
                    continue

                cert_path: pathlib.Path | None = None
                if config_file.cert_path:
                    cert_path = (
                        PathConstants.application_data_directory
                        / "Certificates"
                        / config_file.cert_path
                    )
                    if not cert_path.exists():
                        cert_path = None
                configurations[config_file.id] = core.HttpConfiguration(
                    config_file.uri,
                    config_file.api_key,
                    cert_path=cert_path,
                    workspace=workspace,
                )
            except PermissionError:
                pass
            except OSError:
                # The individual file is inaccessible or badly formatted, so just skip it
                pass
            except json.JSONDecodeError:
                pass
            except ValueError:
                pass
        return configurations

    @classmethod
    def _read_configuration_file(
        cls, path: pathlib.Path
    ) -> HttpConfigurationFile | None:
        """Parse a single SystemLink HTTP configuration file.

        Args:
            path: The path of the file.

        Returns:
            The parsed file, or None if there is no valid configuration present at the
            given path.

        Raises:
            OSError: if an error occurs while accessing the file.
            PermissionError: if the current application does not have permission to
                access the configuration file.
            json.decoder.JSONDecodeError: if the file does not contain valid JSON.
        """
        if not path.exists():
            raise OSError("HTTP configuration file was not found: " + str(path))
        with path.open() as f:
            config_dict = json.load(f)
        config = HttpConfigurationFile.from_json_dict(config_dict)
        if not config.id:
            return None

        config.id = config.id.upper()
        return config

    @classmethod
    def _http_configurations_directory(cls) -> pathlib.Path:
        """Get the platform-specific path to the HTTP Configurations directory.

        Returns:
            pathlib.Path: The path of the HTTP Configurations directory.
        """
        return PathConstants.application_data_directory / "HttpConfigurations"

    @classmethod
    def _salt_grains_path(cls) -> pathlib.Path:
        """Get the SALT grains config file path.

        Returns:
            pathlib.Path: The path of SALT grains config file
        """
        return PathConstants.salt_data_directory / "conf" / "grains"

    @classmethod
    def _read_system_workspace(cls) -> str | None:
        """Get the workspace of the connected remote system.

        Reads workspace from `grains` file of SystemLink Client.

        Returns:
            str: Workspace Id of the remote system.
        """
        salt_grain_file_path = cls._salt_grains_path()

        if salt_grain_file_path.exists():
            with open(salt_grain_file_path, "r", encoding="utf-8") as fp:
                grain_data: Dict = yaml.safe_load(fp)
            return grain_data.get(cls._SALT_GRAINS_WORKSPACE_KEY)

        return None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: nisystemlink/clients/core/_internal/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_classproperty_support.py sha256=bb26a563a7ed1d89d098839e1b965255d491dfbc36a393ebcee674d922c00f75 bytes=1305 -->
## FILE: nisystemlink/clients/core/_internal/_classproperty_support.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_classproperty_support.py`
- sha256: `bb26a563a7ed1d89d098839e1b965255d491dfbc36a393ebcee674d922c00f75`
- bytes: 1305

````python
# -*- coding: utf-8 -*-

"""Implementation of ClasspropertySupport."""

import abc
import typing
from typing import Any, Callable, Dict, Tuple, TypeVar

_T = TypeVar("_T")


class ClasspropertySupport(abc.ABCMeta):
    """Meta class for classes that cannot be subclassed."""

    class _ClassProperty:
        def __init__(self, func: Callable[[Any], Any]):
            self.func = func

    def __new__(
        meta, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]
    ) -> "ClasspropertySupport":
        class ClasspropertySupport_(meta):  # type: ignore
            pass

        for k, v in dct.items():
            # Promote all instance properties to be class properties
            if isinstance(v, meta._ClassProperty):
                setattr(ClasspropertySupport_, k, property(v.func))

        return typing.cast(
            ClasspropertySupport,
            super().__new__(ClasspropertySupport_, name, bases, dct),
        )

    @classmethod
    def classproperty(cls, f: Callable[[Any], _T]) -> _T:
        """Make a classproperty."""
        # Cast to preserve the original function's return type for the type checker.
        # It'll get wrapped in a property in the __new__ method.
        return typing.cast(_T, cls._ClassProperty(f))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_http_client.py sha256=802ff69729e5d0b297c6757978160e5fe29a61ab1a249f809643f8d9803ed2e8 bytes=11036 -->
## FILE: nisystemlink/clients/core/_internal/_http_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_http_client.py`
- sha256: `802ff69729e5d0b297c6757978160e5fe29a61ab1a249f809643f8d9803ed2e8`
- bytes: 11036

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpClient."""

import json.decoder
import sys
import threading
import typing
import urllib.parse
from typing import Any, Awaitable, Dict, Iterable, Tuple

from nisystemlink.clients import core

if sys.version_info >= (3, 6):
    from httpx import AsyncClient, Client, Response as HttpResponse
else:
    from requests import Session as Client, Response as HttpResponse

    AsyncClient = None  # type: Any


class HttpClient:
    """Base client for HTTP connections."""

    def __init__(self, configuration: core.HttpConfiguration) -> None:
        self._server = configuration.server_uri.rstrip("/")

        self._kwargs = {}  # type: Dict[str, Any]
        self._kwargs["headers"] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if configuration.api_keys is not None:
            self._kwargs["headers"].update(configuration.api_keys)
        elif configuration.username is not None and configuration.password is not None:
            self._kwargs["auth"] = (configuration.username, configuration.password)
        if configuration.cert_path:
            self._kwargs["verify"] = str(configuration.cert_path)

        # Keep a client per thread
        # - https://toolbelt.readthedocs.io/en/latest/threading.html
        # - "there are still a couple corner cases where it isn't perfectly threadsafe"
        self._clients = {}  # type: Dict[int, Client]
        self._aclients = {}  # type: Dict[int, AsyncClient]

    def at_uri(self, uri: str) -> "_HttpClientAtUri":
        """Get a client interface for which all queries are relative to ``uri``."""
        return _HttpClientAtUri(self, self._server + uri)

    @property
    def _client(self) -> Client:
        thread_id = threading.get_ident()
        if thread_id not in self._clients:
            if sys.version_info >= (3, 6):
                client = Client(**self._kwargs)
            else:
                client = Client()
                for k, v in self._kwargs.items():
                    setattr(client, k, v)
            self._clients[thread_id] = client
        return self._clients[thread_id]

    @property
    def _async_client(self) -> AsyncClient:
        thread_id = threading.get_ident()
        if thread_id not in self._clients:
            if sys.version_info < (3, 6):
                raise RuntimeError("async support is only available for python 3.6+")
            self._aclients[thread_id] = AsyncClient(**self._kwargs)
        return self._aclients[thread_id]


class _HttpClientAtUri:
    """Interface to HttpClient for while all queries are relative to a given uri."""

    def __init__(self, client: HttpClient, uri: str) -> None:
        self._client = client
        self._base_uri = uri

    @property
    def as_async(self) -> "_AsyncHttpClientAtUri":
        """An async version of the client."""
        if sys.version_info < (3, 6):
            raise RuntimeError("async support is only available for python 3.6+")
        return _AsyncHttpClientAtUri(self._client, self._base_uri)

    def _request(
        self,
        method: str,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Tuple[Any, HttpResponse]:
        client = self._client._client
        uri, params2 = _expand_uri_params(uri, params)
        response = client.request(method, uri, json=data, params=params2)
        return _handle_response(response, method, uri), response

    def get(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a GET request."""
        return self._request("GET", self._base_uri + uri, params=params)

    def head(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a HEAD request."""
        return self._request("HEAD", self._base_uri + uri, params=params)

    def delete(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a DELETE request."""
        return self._request("DELETE", self._base_uri + uri, params=params)

    def post(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a POST request."""
        return self._request("POST", self._base_uri + uri, params=params, data=data)

    def put(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a PUT request."""
        return self._request("PUT", self._base_uri + uri, params=params, data=data)

    def patch(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Tuple[Any, HttpResponse]:
        """Perform a PATCH request."""
        return self._request("PATCH", self._base_uri + uri, params=params, data=data)

    @property
    def base_uri(self) -> str:
        return self._base_uri


class _AsyncHttpClientAtUri:
    """Interface to HttpClient for while all queries are relative to a given uri."""

    def __init__(self, client: HttpClient, uri: str) -> None:
        self._client = client
        self._base_uri = uri

    async def _request(
        self,
        method: str,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Tuple[Any, HttpResponse]:
        client = self._client._async_client
        uri, params2 = _expand_uri_params(uri, params)
        response = await client.request(method, uri, json=data, params=params2)
        return _handle_response(response, method, uri), response

    def get(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a GET request."""
        return self._request("GET", self._base_uri + uri, params=params)

    def head(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a HEAD request."""
        return self._request("HEAD", self._base_uri + uri, params=params)

    def delete(
        self, uri: str, *, params: Dict[str, str | None] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a DELETE request."""
        return self._request("DELETE", self._base_uri + uri, params=params)

    def post(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a POST request."""
        return self._request("POST", self._base_uri + uri, params=params, data=data)

    def put(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a PUT request."""
        return self._request("PUT", self._base_uri + uri, params=params, data=data)

    def patch(
        self,
        uri: str,
        *,
        params: Dict[str, str | None] | None = None,
        data: Dict[str, Any] | Iterable[Any] | None = None
    ) -> Awaitable[Tuple[Any, HttpResponse]]:
        """Perform a PATCH request."""
        return self._request("PATCH", self._base_uri + uri, params=params, data=data)

    @property
    def base_uri(self) -> str:
        return self._base_uri


def _expand_uri_params(
    uri: str, params: Dict[str, str | None] | None
) -> Tuple[str, Dict[str, str] | None]:
    """Expand any params in uri with a url-encoded version of the corresponding value in ``params``.

    Any matched params will be removed from params. Any unmatched params will be left
    as-is in the uri.

    For example, uri can be "/tags/{path}" and params can be {"path": "foo/bar"},
    resulting in the uri "/tags/foo%2Fbar" and params={}.
    """
    if params is None:
        return uri, params
    params2 = {k: v for k, v in params.items() if v is not None}
    if "{" not in uri:
        return uri, params2
    for param, value in params.items():
        param_match = "{" + param + "}"
        if param_match in uri:
            uri = uri.replace(param_match, urllib.parse.quote(value or "", safe=""))
            del params2[param]
    return uri, params2


def _handle_response(response: HttpResponse, method: str, uri: str) -> Any:
    try:
        data = response.json() if len(response.text) > 0 else None
        non_json_error = None
    except json.decoder.JSONDecodeError as ex:
        # For error statuses (e.g. 403), if the body isn't JSON, raise an ApiException
        # with the body text as a message
        data = None
        non_json_error = response.text

        # But if this was supposed to be a non-error, raise the decode error
        if 200 <= response.status_code < 300:
            # TODO: This works around Bug 369006 where SystemLink Cloud returns non-JSON
            # text for some APIs (but only those for which no response is necessary)
            if response.status_code == 200 and response.text in ("Success", "OK"):
                data = None
            elif response.status_code == 201 and response.text.startswith("Created"):
                data = None
            else:
                raise json.decoder.JSONDecodeError(
                    "Error from <{} {}>: {}\n\nResponse text:\n  {}".format(
                        method, uri, ex.args[0], response.text.replace("\n", "\n  ")
                    ),
                    ex.doc,
                    ex.pos,
                ) from None

    if not 200 <= response.status_code < 300:
        msg = "Server responded with <{} {}> when calling {} ({})".format(
            response.status_code,
            getattr(response, "reason_phrase", None) or getattr(response, "reason"),
            method,
            uri,
        )
        if non_json_error:
            msg += ":\n\n" + non_json_error

        if data:
            err_dict = typing.cast(Dict[str, Any], data).get("error", {})
            err_obj = core.ApiError.parse_obj(err_dict) if err_dict else None
        else:
            err_obj = None

        raise core.ApiException(
            msg, error=err_obj, http_status_code=response.status_code
        )

    return data
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_http_configuration_file.py sha256=f64678489eab81b44f002ad93f1b32a41713d071340acf9ed28db56c76aa1e86 bytes=2989 -->
## FILE: nisystemlink/clients/core/_internal/_http_configuration_file.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_http_configuration_file.py`
- sha256: `f64678489eab81b44f002ad93f1b32a41713d071340acf9ed28db56c76aa1e86`
- bytes: 2989

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpConfigurationFile."""

from typing import Any, Dict

from typing_extensions import final


@final
class HttpConfigurationFile:
    """Represents a SystemLink HTTP configuration JSON file."""

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'HttpConfigurationFile' is not an acceptable base type")

    __slots__ = [
        "_id",
        "_display_name",
        "_connection_type",
        "_uri",
        "_api_key",
        "_cert_path",
    ]

    def __init__(self) -> None:
        self._id = None  # type: str | None
        self._display_name = None  # type: str | None
        self._connection_type = None  # type: str | None
        self._uri = None  # type: str | None
        self._api_key = None  # type: str | None
        self._cert_path = None  # type: str | None

    @staticmethod
    def from_json_dict(d: Dict[str, Any]) -> "HttpConfigurationFile":
        """Create from the dictionary format that is stored as JSON in the file."""
        self = HttpConfigurationFile()
        self.id = d.get("Id")
        self.display_name = d.get("DisplayName")
        self.connection_type = d.get("ConnectionType")
        self.uri = d.get("Uri")
        self.api_key = d.get("ApiKey")
        self.cert_path = d.get("CertPath")
        return self

    @property
    def id(self) -> str | None:  # noqa: D401
        """The ID of this configuration."""
        return self._id

    @id.setter
    def id(self, value: str | None) -> None:
        self._id = value

    @property
    def display_name(self) -> str | None:  # noqa: D401
        """A user-friendly display name for this configuration."""
        return self._display_name

    @display_name.setter
    def display_name(self, value: str | None) -> None:
        self._display_name = value

    @property
    def connection_type(self) -> str | None:  # noqa: D401
        """The type of connection to use."""
        return self._connection_type

    @connection_type.setter
    def connection_type(self, value: str | None) -> None:
        self._connection_type = value

    @property
    def uri(self) -> str | None:  # noqa: D401
        """The URI of the SystemLink server."""
        return self._uri

    @uri.setter
    def uri(self, value: str | None) -> None:
        self._uri = value

    @property
    def api_key(self) -> str | None:  # noqa: D401
        """The API key of this client."""
        return self._api_key

    @api_key.setter
    def api_key(self, value: str | None) -> None:
        self._api_key = value

    @property
    def cert_path(self) -> str | None:  # noqa: D401
        """The path to the server's HTTPS certificate, relative to the Skyline Certificates directory."""
        return self._cert_path

    @cert_path.setter
    def cert_path(self, value: str | None) -> None:
        self._cert_path = value
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_path_constants.py sha256=a76910c62784faf2090b825782fc63dffaa71c0d5eb63d2eac7d328f16fd969b bytes=4524 -->
## FILE: nisystemlink/clients/core/_internal/_path_constants.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_path_constants.py`
- sha256: `a76910c62784faf2090b825782fc63dffaa71c0d5eb63d2eac7d328f16fd969b`
- bytes: 4524

````python
# -*- coding: utf-8 -*-

"""Implementation of PathConstants."""

import os
import pathlib
import typing

from nisystemlink.clients.core._internal._classproperty_support import (
    ClasspropertySupport,
)
from typing_extensions import final


@final
class PathConstants(metaclass=ClasspropertySupport):
    """Provides file and directory paths for the SystemLink client APIs."""

    COMPANY_NAME = "National Instruments"

    PRODUCT_NAME = "Skyline"

    _application_data_directory: pathlib.Path | None = None

    _salt_data_directory: pathlib.Path | None = None

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'PathConstants' is not an acceptable base type")

    def __init__(self) -> None:
        raise TypeError("Can't instantiate static class 'PathConstants'")

    @ClasspropertySupport.classproperty
    def application_data_directory(self) -> pathlib.Path:  # noqa: D401
        """Get the platform-specific path to the common NI Application Data directory.

        Returns:
            The platform-specific path to the common NI Application Data directory.
        """
        if self._application_data_directory is None:
            if os.name == "nt":
                PathConstants._application_data_directory = (
                    self._windows_application_data_directory()
                )
            else:
                PathConstants._application_data_directory = pathlib.Path(
                    "/etc/natinst/niskyline"
                )
        return typing.cast(pathlib.Path, self._application_data_directory)

    @ClasspropertySupport.classproperty
    def salt_data_directory(self) -> pathlib.Path:  # noqa: D401
        """Get the platform-specific path to the salt minion Data directory.

        Returns:
            The platform-specific path to the salt minion Data directory.
        """
        if self._salt_data_directory is None:
            if os.name == "nt":
                PathConstants._salt_data_directory = self._windows_salt_data_directory()

        return typing.cast(pathlib.Path, self._salt_data_directory)

    @classmethod
    def _windows_programdata_directory(cls) -> pathlib.Path:
        """Get the path of Windows PROGRAMDATA directory.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.

        Returns:
            pathlib.Path: Windows PROGRAMDATA directory path.
        """
        if os.name != "nt":
            raise RuntimeError("This function is for Windows only")

        programdata_dir = None

        try:
            from . import _winpaths

            programdata_dir = pathlib.Path(
                _winpaths.get_path(_winpaths.FOLDERID.ProgramData)
            )
        except Exception:
            env_programdata_dir = os.getenv("PROGRAMDATA")

            if env_programdata_dir:
                programdata_dir = pathlib.Path(env_programdata_dir)

        if programdata_dir is not None and programdata_dir.exists():
            return programdata_dir

        # Last fallback option, assume that it is in C:/
        programdata_dir = pathlib.Path("C:/ProgramData")

        if not programdata_dir.exists():
            raise RuntimeError("Cannot find ProgramData folder")

        return programdata_dir

    @classmethod
    def _windows_application_data_directory(cls) -> pathlib.Path:
        """Get the NI Application Data directory on Windows.

        Returns:
            pathlib.Path: The NI Application Data directory on Windows.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.
        """
        programdata_dir = cls._windows_programdata_directory()

        return programdata_dir / cls.COMPANY_NAME / cls.PRODUCT_NAME

    @classmethod
    def _windows_salt_data_directory(cls) -> pathlib.Path:
        """Get the salt minion Data directory on Windows.

        Returns:
            pathlib.Path: The salt minion Data directory on Windows.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.
        """
        programdata_dir = cls._windows_programdata_directory()
        return programdata_dir / cls.COMPANY_NAME / "salt"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_timestamp_utilities.py sha256=f157f9363b77b8e921088f7868637a03fe69c2943df7b45e7ba86a1c3f8cb276 bytes=2422 -->
## FILE: nisystemlink/clients/core/_internal/_timestamp_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_timestamp_utilities.py`
- sha256: `f157f9363b77b8e921088f7868637a03fe69c2943df7b45e7ba86a1c3f8cb276`
- bytes: 2422

````python
# -*- coding: utf-8 -*-

"""Implementation of TimestampUtilities."""

import datetime

from typing_extensions import final


@final
class TimestampUtilities:
    """Provides utilities for reading and writing timestamps as strings.

    Clients do not typically need to call methods on this class.
    """

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TimestampUtilities' is not an acceptable base type")

    def __init__(self) -> None:
        raise TypeError("Can't instantiate static class 'TimestampUtilities'")

    @classmethod
    def datetime_to_str(cls, value: datetime.datetime) -> str:
        """Convert the given ``datetime.datetime`` into a string timestamp in the standard format used in SystemLink.

        Args:
            value: The date and time to convert.

        Returns:
            The string representation of the timestamp.
        """
        # Use timezone-aware conversion to avoid deprecated utcfromtimestamp usage and
        # preserve exact UTC semantics (value assumed either naive UTC or aware).
        if value.tzinfo is None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        else:
            value = value.astimezone(datetime.timezone.utc)
        return value.isoformat().replace("+00:00", "Z")

    @classmethod
    def str_to_datetime(cls, timestamp: str) -> datetime.datetime:
        """Attempt to parse a SystemLink-formatted timestamp string into a ``datetime.datetime``.

        Args:
            timestamp: The timestamp to parse, in the standard format used in
                SystemLink.

        Returns:
            The parsed datetime.

        Raises:
            ValueError: if the timestamp format is not as expected
        """
        # Python's supported ISO format requires exactly 6 digits after the
        # decimal, and doesn't support "Z" as the timezone
        # Valid format is: YYYY-MM-DDThh:mm:ss.ssssss+NN:NN
        if not timestamp.endswith("Z"):
            raise ValueError(
                "Given timestamp doesn't end with 'Z': '{}'".format(timestamp)
            )
        timestamp = timestamp[:-1].ljust(26, "0")[:26] + "+0000"
        # Note to users: this will be in UTC time; to get a local datetime, you
        # can use value.astimezone()
        return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_winpaths.py sha256=63c2582419d1084ea3bdaef0ed433c42df5a717df82d572b53fcaef45c1cb0af bytes=10971 -->
## FILE: nisystemlink/clients/core/_internal/_winpaths.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_winpaths.py`
- sha256: `63c2582419d1084ea3bdaef0ed433c42df5a717df82d572b53fcaef45c1cb0af`
- bytes: 10971

````python
# -*- coding: utf-8 -*-
# From https://gist.github.com/mkropat/7550097
# fmt: off
# flake8: noqa

LICENSE = """
The MIT License (MIT)

Copyright (c) 2014 Michael Kropat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import ctypes, sys
from ctypes import windll, wintypes
from uuid import UUID

class GUID(ctypes.Structure):   # [1]
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8)
    ]

    def __init__(self, uuid_):
        ctypes.Structure.__init__(self)
        self.Data1, self.Data2, self.Data3, self.Data4[0], self.Data4[1], rest = uuid_.fields
        for i in range(2, 8):
            self.Data4[i] = rest>>(8 - i - 1)*8 & 0xff

class FOLDERID:     # [2]
    AccountPictures         = UUID('{008ca0b1-55b4-4c56-b8a8-4de4b299d3be}')
    AdminTools              = UUID('{724EF170-A42D-4FEF-9F26-B60E846FBA4F}')
    ApplicationShortcuts    = UUID('{A3918781-E5F2-4890-B3D9-A7E54332328C}')
    CameraRoll              = UUID('{AB5FB87B-7CE2-4F83-915D-550846C9537B}')
    CDBurning               = UUID('{9E52AB10-F80D-49DF-ACB8-4330F5687855}')
    CommonAdminTools        = UUID('{D0384E7D-BAC3-4797-8F14-CBA229B392B5}')
    CommonOEMLinks          = UUID('{C1BAE2D0-10DF-4334-BEDD-7AA20B227A9D}')
    CommonPrograms          = UUID('{0139D44E-6AFE-49F2-8690-3DAFCAE6FFB8}')
    CommonStartMenu         = UUID('{A4115719-D62E-491D-AA7C-E74B8BE3B067}')
    CommonStartup           = UUID('{82A5EA35-D9CD-47C5-9629-E15D2F714E6E}')
    CommonTemplates         = UUID('{B94237E7-57AC-4347-9151-B08C6C32D1F7}')
    Contacts                = UUID('{56784854-C6CB-462b-8169-88E350ACB882}')
    Cookies                 = UUID('{2B0F765D-C0E9-4171-908E-08A611B84FF6}')
    Desktop                 = UUID('{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}')
    DeviceMetadataStore     = UUID('{5CE4A5E9-E4EB-479D-B89F-130C02886155}')
    Documents               = UUID('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}')
    DocumentsLibrary        = UUID('{7B0DB17D-9CD2-4A93-9733-46CC89022E7C}')
    Downloads               = UUID('{374DE290-123F-4565-9164-39C4925E467B}')
    Favorites               = UUID('{1777F761-68AD-4D8A-87BD-30B759FA33DD}')
    Fonts                   = UUID('{FD228CB7-AE11-4AE3-864C-16F3910AB8FE}')
    GameTasks               = UUID('{054FAE61-4DD8-4787-80B6-090220C4B700}')
    History                 = UUID('{D9DC8A3B-B784-432E-A781-5A1130A75963}')
    ImplicitAppShortcuts    = UUID('{BCB5256F-79F6-4CEE-B725-DC34E402FD46}')
    InternetCache           = UUID('{352481E8-33BE-4251-BA85-6007CAEDCF9D}')
    Libraries               = UUID('{1B3EA5DC-B587-4786-B4EF-BD1DC332AEAE}')
    Links                   = UUID('{bfb9d5e0-c6a9-404c-b2b2-ae6db6af4968}')
    LocalAppData            = UUID('{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}')
    LocalAppDataLow         = UUID('{A520A1A4-1780-4FF6-BD18-167343C5AF16}')
    LocalizedResourcesDir   = UUID('{2A00375E-224C-49DE-B8D1-440DF7EF3DDC}')
    Music                   = UUID('{4BD8D571-6D19-48D3-BE97-422220080E43}')
    MusicLibrary            = UUID('{2112AB0A-C86A-4FFE-A368-0DE96E47012E}')
    NetHood                 = UUID('{C5ABBF53-E17F-4121-8900-86626FC2C973}')
    OriginalImages          = UUID('{2C36C0AA-5812-4b87-BFD0-4CD0DFB19B39}')
    PhotoAlbums             = UUID('{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}')
    PicturesLibrary         = UUID('{A990AE9F-A03B-4E80-94BC-9912D7504104}')
    Pictures                = UUID('{33E28130-4E1E-4676-835A-98395C3BC3BB}')
    Playlists               = UUID('{DE92C1C7-837F-4F69-A3BB-86E631204A23}')
    PrintHood               = UUID('{9274BD8D-CFD1-41C3-B35E-B13F55A758F4}')
    Profile                 = UUID('{5E6C858F-0E22-4760-9AFE-EA3317B67173}')
    ProgramData             = UUID('{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}')
    ProgramFiles            = UUID('{905e63b6-c1bf-494e-b29c-65b732d3d21a}')
    ProgramFilesX64         = UUID('{6D809377-6AF0-444b-8957-A3773F02200E}')
    ProgramFilesX86         = UUID('{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}')
    ProgramFilesCommon      = UUID('{F7F1ED05-9F6D-47A2-AAAE-29D317C6F066}')
    ProgramFilesCommonX64   = UUID('{6365D5A7-0F0D-45E5-87F6-0DA56B6A4F7D}')
    ProgramFilesCommonX86   = UUID('{DE974D24-D9C6-4D3E-BF91-F4455120B917}')
    Programs                = UUID('{A77F5D77-2E2B-44C3-A6A2-ABA601054A51}')
    Public                  = UUID('{DFDF76A2-C82A-4D63-906A-5644AC457385}')
    PublicDesktop           = UUID('{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}')
    PublicDocuments         = UUID('{ED4824AF-DCE4-45A8-81E2-FC7965083634}')
    PublicDownloads         = UUID('{3D644C9B-1FB8-4f30-9B45-F670235F79C0}')
    PublicGameTasks         = UUID('{DEBF2536-E1A8-4c59-B6A2-414586476AEA}')
    PublicLibraries         = UUID('{48DAF80B-E6CF-4F4E-B800-0E69D84EE384}')
    PublicMusic             = UUID('{3214FAB5-9757-4298-BB61-92A9DEAA44FF}')
    PublicPictures          = UUID('{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}')
    PublicRingtones         = UUID('{E555AB60-153B-4D17-9F04-A5FE99FC15EC}')
    PublicUserTiles         = UUID('{0482af6c-08f1-4c34-8c90-e17ec98b1e17}')
    PublicVideos            = UUID('{2400183A-6185-49FB-A2D8-4A392A602BA3}')
    QuickLaunch             = UUID('{52a4f021-7b75-48a9-9f6b-4b87a210bc8f}')
    Recent                  = UUID('{AE50C081-EBD2-438A-8655-8A092E34987A}')
    RecordedTVLibrary       = UUID('{1A6FDBA2-F42D-4358-A798-B74D745926C5}')
    ResourceDir             = UUID('{8AD10C31-2ADB-4296-A8F7-E4701232C972}')
    Ringtones               = UUID('{C870044B-F49E-4126-A9C3-B52A1FF411E8}')
    RoamingAppData          = UUID('{3EB685DB-65F9-4CF6-A03A-E3EF65729F3D}')
    RoamedTileImages        = UUID('{AAA8D5A5-F1D6-4259-BAA8-78E7EF60835E}')
    RoamingTiles            = UUID('{00BCFC5A-ED94-4e48-96A1-3F6217F21990}')
    SampleMusic             = UUID('{B250C668-F57D-4EE1-A63C-290EE7D1AA1F}')
    SamplePictures          = UUID('{C4900540-2379-4C75-844B-64E6FAF8716B}')
    SamplePlaylists         = UUID('{15CA69B3-30EE-49C1-ACE1-6B5EC372AFB5}')
    SampleVideos            = UUID('{859EAD94-2E85-48AD-A71A-0969CB56A6CD}')
    SavedGames              = UUID('{4C5C32FF-BB9D-43b0-B5B4-2D72E54EAAA4}')
    SavedSearches           = UUID('{7d1d3a04-debb-4115-95cf-2f29da2920da}')
    Screenshots             = UUID('{b7bede81-df94-4682-a7d8-57a52620b86f}')
    SearchHistory           = UUID('{0D4C3DB6-03A3-462F-A0E6-08924C41B5D4}')
    SearchTemplates         = UUID('{7E636BFE-DFA9-4D5E-B456-D7B39851D8A9}')
    SendTo                  = UUID('{8983036C-27C0-404B-8F08-102D10DCFD74}')
    SidebarDefaultParts     = UUID('{7B396E54-9EC5-4300-BE0A-2482EBAE1A26}')
    SidebarParts            = UUID('{A75D362E-50FC-4fb7-AC2C-A8BEAA314493}')
    SkyDrive                = UUID('{A52BBA46-E9E1-435f-B3D9-28DAA648C0F6}')
    SkyDriveCameraRoll      = UUID('{767E6811-49CB-4273-87C2-20F355E1085B}')
    SkyDriveDocuments       = UUID('{24D89E24-2F19-4534-9DDE-6A6671FBB8FE}')
    SkyDrivePictures        = UUID('{339719B5-8C47-4894-94C2-D8F77ADD44A6}')
    StartMenu               = UUID('{625B53C3-AB48-4EC1-BA1F-A1EF4146FC19}')
    Startup                 = UUID('{B97D20BB-F46A-4C97-BA10-5E3608430854}')
    System                  = UUID('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}')
    SystemX86               = UUID('{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}')
    Templates               = UUID('{A63293E8-664E-48DB-A079-DF759E0509F7}')
    UserPinned              = UUID('{9E3995AB-1F9C-4F13-B827-48B24B6C7174}')
    UserProfiles            = UUID('{0762D272-C50A-4BB0-A382-697DCD729B80}')
    UserProgramFiles        = UUID('{5CD7AEE2-2219-4A67-B85D-6C9CE15660CB}')
    UserProgramFilesCommon  = UUID('{BCBD3057-CA5C-4622-B42D-BC56DB0AE516}')
    Videos                  = UUID('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}')
    VideosLibrary           = UUID('{491E922F-5643-4AF4-A7EB-4E7A138D8174}')
    Windows                 = UUID('{F38BF404-1D43-42F2-9305-67DE0B28FC23}')

class UserHandle:   # [3]
    current = wintypes.HANDLE(0)
    common  = wintypes.HANDLE(-1)

_CoTaskMemFree = windll.ole32.CoTaskMemFree     # [4]
_CoTaskMemFree.restype= None
_CoTaskMemFree.argtypes = [ctypes.c_void_p]

_SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath     # [5] [3]
_SHGetKnownFolderPath.argtypes = [
    ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
]

class PathNotFoundException(Exception): pass

def get_path(folderid, user_handle=UserHandle.common):
    fid = GUID(folderid)
    pPath = ctypes.c_wchar_p()
    S_OK = 0
    if _SHGetKnownFolderPath(ctypes.byref(fid), 0, user_handle, ctypes.byref(pPath)) != S_OK:
        raise PathNotFoundException()
    path = pPath.value
    _CoTaskMemFree(pPath)
    return path

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ['-?', '/?']:
        print('python knownpaths.py FOLDERID {current|common}')
        sys.exit(0)

    try:
        folderid = getattr(FOLDERID, sys.argv[1])
    except AttributeError:
        print('Unknown folder id "%s"' % sys.argv[1], file=sys.stderr)
        sys.exit(1)

    try:
        if len(sys.argv) == 2:
            print(get_path(folderid))
        else:
            print(get_path(folderid, getattr(UserHandle, sys.argv[2])))
    except PathNotFoundException:
        print('Folder not found "%s"' % ' '.join(sys.argv[1:]), file=sys.stderr)
        sys.exit(1)

# [1] http://msdn.microsoft.com/en-us/library/windows/desktop/aa373931.aspx
# [2] http://msdn.microsoft.com/en-us/library/windows/desktop/dd378457.aspx
# [3] http://msdn.microsoft.com/en-us/library/windows/desktop/bb762188.aspx
# [4] http://msdn.microsoft.com/en-us/library/windows/desktop/ms680722.aspx
# [5] http://www.themacaque.com/?p=954
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_winpaths.pyi sha256=836ff86c95af2c1e741f80f0238abea31b3ceb0fbae29df086b32dfed2aaf38a bytes=3873 -->
## FILE: nisystemlink/clients/core/_internal/_winpaths.pyi

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_internal/_winpaths.pyi`
- sha256: `836ff86c95af2c1e741f80f0238abea31b3ceb0fbae29df086b32dfed2aaf38a`
- bytes: 3873

````python
# -*- coding: utf-8 -*-

import ctypes
from ctypes import wintypes
from uuid import UUID


class GUID(ctypes.Structure):
    def __init__(self, uuid_: UUID) -> None: ...


class FOLDERID:
    AccountPictures = ...  # type: UUID
    AdminTools = ...  # type: UUID
    ApplicationShortcuts = ...  # type: UUID
    CameraRoll = ...  # type: UUID
    CDBurning = ...  # type: UUID
    CommonAdminTools = ...  # type: UUID
    CommonOEMLinks = ...  # type: UUID
    CommonPrograms = ...  # type: UUID
    CommonStartMenu = ...  # type: UUID
    CommonStartup = ...  # type: UUID
    CommonTemplates = ...  # type: UUID
    Contacts = ...  # type: UUID
    Cookies = ...  # type: UUID
    Desktop = ...  # type: UUID
    DeviceMetadataStore = ...  # type: UUID
    Documents = ...  # type: UUID
    DocumentsLibrary = ...  # type: UUID
    Downloads = ...  # type: UUID
    Favorites = ...  # type: UUID
    Fonts = ...  # type: UUID
    GameTasks = ...  # type: UUID
    History = ...  # type: UUID
    ImplicitAppShortcuts = ...  # type: UUID
    InternetCache = ...  # type: UUID
    Libraries = ...  # type: UUID
    Links = ...  # type: UUID
    LocalAppData = ...  # type: UUID
    LocalAppDataLow = ...  # type: UUID
    LocalizedResourcesDir = ...  # type: UUID
    Music = ...  # type: UUID
    MusicLibrary = ...  # type: UUID
    NetHood = ...  # type: UUID
    OriginalImages = ...  # type: UUID
    PhotoAlbums = ...  # type: UUID
    PicturesLibrary = ...  # type: UUID
    Pictures = ...  # type: UUID
    Playlists = ...  # type: UUID
    PrintHood = ...  # type: UUID
    Profile = ...  # type: UUID
    ProgramData = ...  # type: UUID
    ProgramFiles = ...  # type: UUID
    ProgramFilesX64 = ...  # type: UUID
    ProgramFilesX86 = ...  # type: UUID
    ProgramFilesCommon = ...  # type: UUID
    ProgramFilesCommonX64 = ...  # type: UUID
    ProgramFilesCommonX86 = ...  # type: UUID
    Programs = ...  # type: UUID
    Public = ...  # type: UUID
    PublicDesktop = ...  # type: UUID
    PublicDocuments = ...  # type: UUID
    PublicDownloads = ...  # type: UUID
    PublicGameTasks = ...  # type: UUID
    PublicLibraries = ...  # type: UUID
    PublicMusic = ...  # type: UUID
    PublicPictures = ...  # type: UUID
    PublicRingtones = ...  # type: UUID
    PublicUserTiles = ...  # type: UUID
    PublicVideos = ...  # type: UUID
    QuickLaunch = ...  # type: UUID
    Recent = ...  # type: UUID
    RecordedTVLibrary = ...  # type: UUID
    ResourceDir = ...  # type: UUID
    Ringtones = ...  # type: UUID
    RoamingAppData = ...  # type: UUID
    RoamedTileImages = ...  # type: UUID
    RoamingTiles = ...  # type: UUID
    SampleMusic = ...  # type: UUID
    SamplePictures = ...  # type: UUID
    SamplePlaylists = ...  # type: UUID
    SampleVideos = ...  # type: UUID
    SavedGames = ...  # type: UUID
    SavedSearches = ...  # type: UUID
    Screenshots = ...  # type: UUID
    SearchHistory = ...  # type: UUID
    SearchTemplates = ...  # type: UUID
    SendTo = ...  # type: UUID
    SidebarDefaultParts = ...  # type: UUID
    SidebarParts = ...  # type: UUID
    SkyDrive = ...  # type: UUID
    SkyDriveCameraRoll = ...  # type: UUID
    SkyDriveDocuments = ...  # type: UUID
    SkyDrivePictures = ...  # type: UUID
    StartMenu = ...  # type: UUID
    Startup = ...  # type: UUID
    System = ...  # type: UUID
    SystemX86 = ...  # type: UUID
    Templates = ...  # type: UUID
    UserPinned = ...  # type: UUID
    UserProfiles = ...  # type: UUID
    UserProgramFiles = ...  # type: UUID
    UserProgramFilesCommon = ...  # type: UUID
    Videos = ...  # type: UUID
    VideosLibrary = ...  # type: UUID
    Windows = ...  # type: UUID


def get_path(folderid: UUID, user_handle: wintypes.HANDLE = ...) -> str: ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_jupyter_http_configuration.py sha256=43e6de095be5e98c6e3824516913752346e12706375aa9c775a5a2a322d39f4c bytes=797 -->
## FILE: nisystemlink/clients/core/_jupyter_http_configuration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_jupyter_http_configuration.py`
- sha256: `43e6de095be5e98c6e3824516913752346e12706375aa9c775a5a2a322d39f4c`
- bytes: 797

````python
# -*- coding: utf-8 -*-

"""Implementation of JupyterHttpConfiguration."""

import os

from nisystemlink.clients import core


class JupyterHttpConfiguration(core.HttpConfiguration):
    """An :class:`HttpConfiguration` for Jupyter notebooks running in a SystemLink environment."""

    _HTTP_URI_ENV_VAR = "SYSTEMLINK_HTTP_URI"
    _HTTP_API_KEY_ENV_VAR = "SYSTEMLINK_API_KEY"

    def __init__(self) -> None:
        """Initialize a configuration for SystemLink using API key-based
        authentication provided through environment variables.

        Raises:
            KeyError: if the expected environment variables are not set.
        """
        super().__init__(
            os.environ[self._HTTP_URI_ENV_VAR], os.environ[self._HTTP_API_KEY_ENV_VAR]
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: nisystemlink/clients/core/_uplink/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_base_client.py sha256=f71069c45cbe47fa3224be02764dcf34e5d29164758f8e9dfc60e437090348e6 bytes=4392 -->
## FILE: nisystemlink/clients/core/_uplink/_base_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_base_client.py`
- sha256: `f71069c45cbe47fa3224be02764dcf34e5d29164758f8e9dfc60e437090348e6`
- bytes: 4392

````python
# mypy: disable-error-code = misc

from types import UnionType
from typing import Any, Callable, Dict, get_origin, Type, Union

import requests
from nisystemlink.clients import core
from pydantic import TypeAdapter
from requests import JSONDecodeError, Response
from uplink import commands, Consumer, converters, response_handler, utils
from uplink.auth import BasicAuth

from ._json_model import JsonModel


@response_handler
def _handle_http_status(response: Response) -> Response | None:
    """Checks an HTTP response's status code and raises an exception if necessary."""
    if 200 <= response.status_code < 300:
        # Return None for "204 No Content" responses.
        if response.status_code == 204:
            return None
        return response

    msg = "Server responded with <{} {}> ({}).".format(
        response.status_code, response.reason, response.url
    )

    try:
        content = response.json()
        if content and "error" in content:
            err_obj = core.ApiError.model_validate(content["error"])
        else:
            err_obj = None

        raise core.ApiException(
            msg,
            error=err_obj,
            http_status_code=response.status_code,
            response_data=content,
        )
    except JSONDecodeError:
        if response.text:
            msg += ":\n\n" + response.text
        raise core.ApiException(msg, http_status_code=response.status_code)


_type_adapters: Dict[Type, TypeAdapter] = dict()


class _JsonModelConverter(converters.Factory):
    """A converter that converts between JSON and Pydantic models."""

    def __init__(self) -> None:
        super().__init__()

    def create_request_body_converter(
        self, _class: Type, _: commands.RequestDefinition
    ) -> Callable[[JsonModel], Dict] | None:
        def encoder(model: JsonModel) -> Dict:
            return model.model_dump(mode="json", by_alias=True, exclude_unset=True)

        if utils.is_subclass(_class, JsonModel):
            return encoder
        else:
            return None

    def create_response_body_converter(
        self, _class: Type, _: commands.RequestDefinition
    ) -> Callable[[Response], Any] | None:
        def decoder(response: Response | Any) -> Any:
            if response is None:
                return None

            adapter = _type_adapters[_class]
            if isinstance(response, Response):
                if response.status_code == 204:
                    return None
                return adapter.validate_json(response.text, by_alias=True, strict=True)
            else:
                # In cases where a return_key is specified, the response will already be parsed into a dict
                return adapter.validate_python(response, by_alias=True, strict=True)

        origin = get_origin(_class)
        modelable_origin = (
            origin is Union or origin is UnionType or origin is dict or origin is list
        )
        if modelable_origin or utils.is_subclass(_class, JsonModel):
            if _type_adapters.get(_class) is None:
                _type_adapters[_class] = TypeAdapter(_class)
            return decoder
        else:
            return None


class BaseClient(Consumer):
    """Base class for SystemLink clients, built on top of `Uplink <https://github.com/prkumar/uplink>`_."""

    def __init__(self, configuration: core.HttpConfiguration, base_path: str = ""):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about how to connect.
            base_path: The base path for all API calls.
        """
        session = requests.Session()
        session.verify = configuration.verify
        auth: BasicAuth | None = None
        if (configuration.username is not None) and (
            configuration.password is not None
        ):
            auth = BasicAuth(configuration.username, configuration.password)

        super().__init__(
            base_url=configuration.server_uri + base_path,
            converter=_JsonModelConverter(),
            hooks=[_handle_http_status],
            client=session,
            auth=auth,
        )
        if configuration.api_keys:
            self.session.headers.update(configuration.api_keys)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_file_like_response.py sha256=b941df2b97422a1781cced67333e9f9808396e02b25e53db727bb35d3dea8364 bytes=299 -->
## FILE: nisystemlink/clients/core/_uplink/_file_like_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_file_like_response.py`
- sha256: `b941df2b97422a1781cced67333e9f9808396e02b25e53db727bb35d3dea8364`
- bytes: 299

````python
from nisystemlink.clients.core.helpers import IteratorFileLike
from requests.models import Response


def file_like_response_handler(response: Response) -> IteratorFileLike:
    """Response handler for File-Like content."""
    return IteratorFileLike(response.iter_content(chunk_size=4096))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_json_model.py sha256=a436a95a07b2fd3ad93fa2195aed4c1ce47e074036f7dad44f472824cf3b772e bytes=886 -->
## FILE: nisystemlink/clients/core/_uplink/_json_model.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_json_model.py`
- sha256: `a436a95a07b2fd3ad93fa2195aed4c1ce47e074036f7dad44f472824cf3b772e`
- bytes: 886

````python
from pydantic import AliasChoices, AliasGenerator, BaseModel, ConfigDict


def _camelcase(s: str) -> str:
    """Convert a snake case string to camelCase."""
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def _validation_aliases(s: str) -> str | AliasChoices:
    """Accept both Python snake_case and wire-format camelCase inputs."""
    camelcase = _camelcase(s)
    if camelcase == s:
        return s
    return AliasChoices(s, camelcase)


class JsonModel(BaseModel):
    """Base class for models that are serialized to and from JSON."""

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=_validation_aliases,
            serialization_alias=_camelcase,
        ),
        validate_by_name=True,
        validate_by_alias=True,
        extra="ignore",
    )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_methods.py sha256=8cfad8e2f1a4f157fafbb3de3016a5b77b7196fd05ce61f9fb014970ed4b7767 bytes=2596 -->
## FILE: nisystemlink/clients/core/_uplink/_methods.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_methods.py`
- sha256: `8cfad8e2f1a4f157fafbb3de3016a5b77b7196fd05ce61f9fb014970ed4b7767`
- bytes: 2596

````python
"""Wrappers around uplink HTTP decorators with proper type annotations."""

from typing import Any, Callable, Sequence, Tuple, TypeVar

from uplink import (
    Body,
    commands,
    headers,
    json,
    response_handler as uplink_response_handler,
    returns,
)

F = TypeVar("F", bound=Callable[..., Any])


def get(path: str, args: Sequence[Any] | None = None) -> Callable[[F], F]:
    """Annotation for a GET request."""

    def decorator(func: F) -> F:
        return commands.get(path, args=args)(func)  # type: ignore

    return decorator


def post(
    path: str,
    args: Sequence[Any] | None = None,
    return_key: str | Tuple[str, ...] | None = None,
    content_type: str | None = None,
) -> Callable[[F], F]:
    """Annotation for a POST request with a JSON request body. If args is not
    specified, defaults to a single argument that represents the request body.
    """

    def decorator(func: F) -> F:
        result = commands.post(path, args=args or (Body,))(func)
        if content_type:
            result = headers({"Content-Type": content_type})(result)
        else:
            result = json(result)  # type: ignore
        if return_key:
            result = returns.json(key=return_key)(result)
        return result  # type: ignore

    return decorator


def put(path: str, args: Sequence[Any] | None = None) -> Callable[[F], F]:
    """Annotation for a PUT request with a JSON request body. If args is not
    specified, defaults to a single argument that represents the request body.
    """

    def decorator(func: F) -> F:
        return json(commands.put(path, args=args or (Body,))(func))  # type: ignore

    return decorator


def patch(path: str, args: Sequence[Any] | None = None) -> Callable[[F], F]:
    """Annotation for a PATCH request with a JSON request body."""

    def decorator(func: F) -> F:
        return json(commands.patch(path, args=args)(func))  # type: ignore

    return decorator


def delete(path: str, args: Sequence[Any] | None = None) -> Callable[[F], F]:
    """Annotation for a DELETE request."""

    def decorator(func: F) -> F:
        return commands.delete(path, args=args)(func)  # type: ignore

    return decorator


def response_handler(
    handler: Any, requires_consumer: bool | None = False
) -> Callable[[F], F]:
    """Annotation for creating custom response handlers."""

    def decorator(func: F) -> F:
        return uplink_response_handler(handler, requires_consumer)(func)  # type: ignore

    return decorator
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_multipart_retry.py sha256=60e8ad9a56bf4cf7e57562497d8af0e2908776001e37e623455ac06a93a22166 bytes=7355 -->
## FILE: nisystemlink/clients/core/_uplink/_multipart_retry.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_multipart_retry.py`
- sha256: `60e8ad9a56bf4cf7e57562497d8af0e2908776001e37e623455ac06a93a22166`
- bytes: 7355

````python
"""Helpers for multipart requests that need retry-safe stream handling.

The decorator exported by this module is intended for multipart requests that may
be retried by Uplink. It preserves the caller's stream position on the initial
send, rewinds seekable multipart parts only on retry attempts, and aborts the
retry if any part cannot be rewound.

When a retry is aborted because a part cannot be rewound, the original response
or exception that triggered the retry is surfaced back through Uplink's normal
response and error handling pipeline instead of sending a malformed follow-up
request.
"""

import io
from enum import auto, Enum
from typing import Any, Callable, cast, TypeVar

from requests import Response
from uplink import decorators
from uplink.clients.io import transitions
from uplink.clients.io.interfaces import RequestTemplate

F = TypeVar("F", bound=Callable[..., Any])


class _RewindResult(Enum):
    REWOUND = auto()
    FAILED = auto()
    NOT_NEEDED = auto()


def _rewind_retryable_part(part: object) -> _RewindResult:
    """Rewind the first seekable multipart payload contained in ``part``.

    Returns ``_RewindResult.REWOUND`` when a multipart payload was successfully
    rewound to the start of the stream. Returns
    ``_RewindResult.FAILED`` when a stream payload appears to need rewinding but
    rejects it. Returns ``_RewindResult.NOT_NEEDED`` when the part contains no
    stream payload that requires rewinding, such as simple string fields.
    """
    if hasattr(part, "seek"):
        seekable = getattr(part, "seekable", None)
        if callable(seekable):
            try:
                if not cast(Any, seekable)():
                    return _RewindResult.FAILED
            except (OSError, io.UnsupportedOperation):
                return _RewindResult.FAILED

        try:
            cast(Any, part).seek(0)
        except (OSError, io.UnsupportedOperation):
            return _RewindResult.FAILED
        return _RewindResult.REWOUND

    if isinstance(part, tuple):
        for item in part:
            rewind_result = _rewind_retryable_part(item)
            if rewind_result is not _RewindResult.NOT_NEEDED:
                return rewind_result

    return _RewindResult.NOT_NEEDED


def _get_saved_retry_action(
    response: Response | None,
    exception_info: tuple[type[BaseException], BaseException, Any] | None,
) -> Any:
    """Return the original retry-triggering failure as an Uplink transition."""
    if response is not None:
        return transitions.finish(response)

    if exception_info is not None:
        return transitions.fail(*exception_info)

    return None


class _RetryableMultipartRequestTemplate(RequestTemplate):
    """Track multipart retry state and rewind streams only for retry sends.

    The first request attempt is left untouched so callers can intentionally
    provide streams positioned away from offset 0. On later attempts, each file
    part must be rewound to the beginning before the request is sent again.

    If rewinding fails for any part, the retry is cancelled and the original
    response or exception that caused the retry is returned to Uplink so normal
    error handling can surface it to the caller.
    """

    def __init__(self) -> None:
        self._attempted_request_ids: set[int] = set()
        self._responses_by_request_id: dict[int, Response] = {}
        self._exceptions_by_request_id: dict[
            int, tuple[type[BaseException], BaseException, Any]
        ] = {}

    def _clear_request_state(self, request_id: int) -> None:
        self._attempted_request_ids.discard(request_id)
        self._responses_by_request_id.pop(request_id, None)
        self._exceptions_by_request_id.pop(request_id, None)

    def before_request(self, request: tuple[str, str, dict[str, Any]]) -> Any:
        _, _, extras = request
        request_id = id(request)
        if request_id not in self._attempted_request_ids:
            self._attempted_request_ids.add(request_id)
            return None

        for part in extras.get("files", {}).values():
            if _rewind_retryable_part(part) is _RewindResult.FAILED:
                retry_action = _get_saved_retry_action(
                    self._responses_by_request_id.get(request_id),
                    self._exceptions_by_request_id.get(request_id),
                )
                self._clear_request_state(request_id)
                return retry_action
        return None

    def after_response(
        self, request: tuple[str, str, dict[str, Any]], response: Response
    ) -> None:
        request_id = id(request)
        self._responses_by_request_id[request_id] = response
        self._exceptions_by_request_id.pop(request_id, None)
        return None

    def after_exception(
        self,
        request: tuple[str, str, dict[str, Any]],
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: Any,
    ) -> None:
        request_id = id(request)
        self._exceptions_by_request_id[request_id] = (exc_type, exc_val, exc_tb)
        self._responses_by_request_id.pop(request_id, None)
        return None


class _RetryableMultipartCleanupTemplate(RequestTemplate):
    def __init__(self, retry_template: _RetryableMultipartRequestTemplate) -> None:
        self._retry_template = retry_template

    def after_response(
        self, request: tuple[str, str, dict[str, Any]], response: Response
    ) -> None:
        self._retry_template._clear_request_state(id(request))
        return None

    def after_exception(
        self,
        request: tuple[str, str, dict[str, Any]],
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: Any,
    ) -> None:
        self._retry_template._clear_request_state(id(request))
        return None


class _RetryableMultipartRequest(decorators.MethodAnnotation):
    def modify_request(self, request_builder: Any) -> None:
        retryable_template = _RetryableMultipartRequestTemplate()
        # Insert ahead of Uplink's retry template so this helper can see the
        # original retry-triggering response/exception and short-circuit future
        # attempts when a multipart stream cannot be rewound safely.
        request_builder._request_templates.insert(0, retryable_template)
        request_builder._request_templates.append(
            _RetryableMultipartCleanupTemplate(retryable_template)
        )


def retryable_multipart_request() -> Callable[[F], F]:
    """Create a decorator for multipart requests with retry-safe stream handling.

    Behavior:
    - The initial send preserves the caller-provided stream position.
        - Retry attempts rewind seekable multipart payloads back to offset 0.
        - Multipart fields that do not contain streams, such as simple strings, are
            left alone and do not block retries.
    - If a retry attempt cannot rewind a payload, the retry is cancelled and the
      original retry-triggering response or exception is surfaced.
    """

    def decorator(func: F) -> F:
        return _RetryableMultipartRequest()(func)  # type: ignore[return-value]

    return decorator
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_with_paging.py sha256=78f81c68c13afc250a62d522af891f4329875d22e1dbf6fc7fdd55e6207fe062 bytes=596 -->
## FILE: nisystemlink/clients/core/_uplink/_with_paging.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/_uplink/_with_paging.py`
- sha256: `78f81c68c13afc250a62d522af891f4329875d22e1dbf6fc7fdd55e6207fe062`
- bytes: 596

````python
from ._json_model import JsonModel


class WithPaging(JsonModel):
    continuation_token: str | None = None
    """A token which allows the user to resume a query at the next item in the matching results.

    When querying, a token will be returned if a query may be
    continued. To obtain the next page of results, pass the token to the service
    on a subsequent request. The service will respond with a new continuation
    token. To paginate results, continue sending requests with the newest
    continuation token provided by the service, until this value is null.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/__init__.py sha256=62495a5899a040971c8f7f0e4ec162780f5dc0a19ec736fd6da02412c16c8d40 bytes=144 -->
## FILE: nisystemlink/clients/core/helpers/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/helpers/__init__.py`
- sha256: `62495a5899a040971c8f7f0e4ec162780f5dc0a19ec736fd6da02412c16c8d40`
- bytes: 144

````python
from ._iterator_file_like import IteratorFileLike
from ._minion_id import read_minion_id
from ._pagination import paginate

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_iterator_file_like.py sha256=219850f0b39bc3fe8c72b297c0c085610b8f1d8ffec41931a994e0bf60d18fdf bytes=1011 -->
## FILE: nisystemlink/clients/core/helpers/_iterator_file_like.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/helpers/_iterator_file_like.py`
- sha256: `219850f0b39bc3fe8c72b297c0c085610b8f1d8ffec41931a994e0bf60d18fdf`
- bytes: 1011

````python
from typing import Any, Iterator


class IteratorFileLike:
    """A file-like object adapter that wraps a python iterator, providing a way to
    read from the iterator as if it was a file.
    """

    def __init__(self, iterator: Iterator[Any]):
        self._iterator = iterator
        self._buffer = b""

    def read(self, size: int = -1) -> bytes:
        """Read at most `size` bytes from the file-like object. If `size` is not
        specified or is negative, read until the iterator is exhausted and
        returns all bytes or characters read.
        """
        while size < 0 or len(self._buffer) < size:
            try:
                chunk = next(self._iterator)
                self._buffer += chunk
            except StopIteration:
                break
        if size < 0:
            data = self._buffer
            self._buffer = b""
        else:
            data = self._buffer[:size]
            self._buffer = self._buffer[size:]
        return data
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_minion_id.py sha256=442fa9648cb0fd548b912bc7b71bf3a1bf1fdddabea0e80425ba0ab2f5cd7df3 bytes=689 -->
## FILE: nisystemlink/clients/core/helpers/_minion_id.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/helpers/_minion_id.py`
- sha256: `442fa9648cb0fd548b912bc7b71bf3a1bf1fdddabea0e80425ba0ab2f5cd7df3`
- bytes: 689

````python
# -*- coding: utf-8 -*-

"""Helper function to get minion ID from Salt configuration."""

from nisystemlink.clients.core._internal._path_constants import PathConstants


def read_minion_id() -> str | None:
    """Read the minion ID from the Salt configuration.

    Returns:
        str | None: The minion ID content if the file exists, None otherwise.
    """
    minion_id_path = PathConstants.salt_data_directory / "conf" / "minion_id"

    if not minion_id_path.exists():
        return None

    try:
        with open(minion_id_path, "r", encoding="utf-8") as fp:
            return fp.read().strip()
    except (OSError, PermissionError):
        return None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_pagination.py sha256=1a24c6618beb8212393060c26a363f6dacf3a356766a3cc3702b3baf738b9e2b bytes=2406 -->
## FILE: nisystemlink/clients/core/helpers/_pagination.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/helpers/_pagination.py`
- sha256: `1a24c6618beb8212393060c26a363f6dacf3a356766a3cc3702b3baf738b9e2b`
- bytes: 2406

````python
# -*- coding: utf-8 -*-
from typing import Any, Callable, Generator

from nisystemlink.clients.core._uplink._with_paging import WithPaging


def paginate(
    fetch_function: Callable[..., WithPaging],
    items_field: str,
    **fetch_kwargs: Any,
) -> Generator[Any, None, None]:
    """Generate items from paginated API responses using continuation tokens.

    This helper function provides a convenient way to iterate over all items
    from a paginated API endpoint that uses continuation tokens. It automatically
    handles fetching subsequent pages until all items are retrieved.

    Args:
        fetch_function: The API function to call to fetch each page of items.
            Must accept a ``continuation_token`` parameter and return a response
            that derives from ``WithPaging``.
        items_field: The name of the field in the response object that contains
            the list of items to yield.
        **fetch_kwargs: Additional keyword arguments to pass to the fetch function
            on every call (e.g., filters, take limits, etc.).

    Yields:
        Individual items from each page of results.

    Note:
        The fetch function will be called with the `continuation_token` parameter
        set to `None` on the first call, then with each subsequent token until
        the response contains a `None` continuation token.
    """
    continuation_token = None

    while True:
        # Set the continuation token parameter for this page
        fetch_kwargs["continuation_token"] = continuation_token

        # Fetch the current page
        response = fetch_function(**fetch_kwargs)

        # Get the items from the response using the specified field name
        items = getattr(response, items_field, [])

        # Yield each item individually
        for item in items:
            yield item

        # Get the continuation token for the next page
        next_continuation_token = response.continuation_token

        # Stop if there are no more pages
        if next_continuation_token is None:
            break

        # Guard against infinite loop if continuation token doesn't change
        if next_continuation_token == continuation_token:
            raise RuntimeError("Continuation token did not change between iterations.")

        continuation_token = next_continuation_token
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_partial_success.py sha256=03b97ac94a14c5fdb7c3a2511ae8e2070efb5e8e0c751a9c597eaf57b26f9676 bytes=1751 -->
## FILE: nisystemlink/clients/core/helpers/_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/core/helpers/_partial_success.py`
- sha256: `03b97ac94a14c5fdb7c3a2511ae8e2070efb5e8e0c751a9c597eaf57b26f9676`
- bytes: 1751

````python
from typing import Any, Sequence, TypeVar

from nisystemlink.clients import core

_ItemT = TypeVar("_ItemT")
_ONE_OR_MORE_ERRORS_OCCURRED_NAME = "Skyline.OneOrMoreErrorsOccurred"
_ONE_OR_MORE_ERRORS_OCCURRED_CODE = -251041


def _unwrap_single_inner_error(error: core.ApiError | None) -> core.ApiError | None:
    if error is None:
        return None

    if len(error.inner_errors) != 1:
        return error

    if (
        error.name == _ONE_OR_MORE_ERRORS_OCCURRED_NAME
        or error.code == _ONE_OR_MORE_ERRORS_OCCURRED_CODE
    ):
        return error.inner_errors[0]

    return error


def unwrap_single_item_partial_success(
    *,
    response: Any | None,
    items: Sequence[_ItemT] | None,
    failed: Sequence[Any] | None,
    error: core.ApiError | None,
    failure_message: str,
    empty_message: str,
) -> _ItemT:
    """Return the first successful item from a partial-success response.

    Raises:
        ApiException: if the response reports a failure or contains no successful item.
    """
    response_data = (
        response.model_dump(mode="json", by_alias=True)
        if response is not None
        else None
    )

    if failed or error:
        raise core.ApiException(
            failure_message,
            error=_unwrap_single_inner_error(error),
            response_data=response_data,
        )

    if not items:
        raise core.ApiException(
            empty_message,
            response_data=response_data,
        )

    if len(items) != 1:
        raise core.ApiException(
            f"Expected exactly one successful item but received {len(items)}.",
            response_data=response_data,
        )

    return items[0]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/__init__.py sha256=4912ab6b402b4b8358ad9d55c9d37124264ef9d3e62583f76ecdf6abf566d02c bytes=149 -->
## FILE: nisystemlink/clients/dataframe/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/__init__.py`
- sha256: `4912ab6b402b4b8358ad9d55c9d37124264ef9d3e62583f76ecdf6abf566d02c`
- bytes: 149

````python
"""Start here with DataFrameClient for dataframe operations."""

from ._data_frame_client import DataFrameClient

__all__ = ["DataFrameClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/_data_frame_client.py sha256=e0be16af155380259c742891f208e7b0343b493d650cb513a65df0c137784f6e bytes=18285 -->
## FILE: nisystemlink/clients/dataframe/_data_frame_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/_data_frame_client.py`
- sha256: `e0be16af155380259c742891f208e7b0343b493d650cb513a65df0c137784f6e`
- bytes: 18285

````python
"""Implementation of DataFrameClient."""

from collections.abc import Iterable
from io import BytesIO
from typing import List, Union

try:
    import pyarrow as pa  # type: ignore
except Exception:
    pa = None  # type: ignore[assignment]
from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import (
    delete,
    get,
    patch,
    post,
    response_handler,
)
from nisystemlink.clients.core.helpers import IteratorFileLike
from requests.models import Response
from uplink import Body, Field, Path, Query, retry

from . import models

# retry for common http status codes and any Connection error


@retry(
    when=retry.when.status([429, 502, 503, 504]),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class DataFrameClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, "/nidataframe/v1/")

    @get("")
    def api_info(self) -> models.ApiInfo:
        """Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        """
        ...

    @get(
        "tables",
        args=[
            Query("take"),
            Query("id"),
            Query("orderBy"),
            Query("orderByDescending"),
            Query("continuationToken"),
            Query("workspace"),
        ],
    )
    def list_tables(
        self,
        take: int | None = None,
        id: List[str] | None = None,
        order_by: models.OrderBy | None = None,
        order_by_descending: bool | None = None,
        continuation_token: str | None = None,
        workspace: List[str] | None = None,
    ) -> models.PagedTables:
        """Lists available tables on the SystemLink DataFrame service.

        Args:
            take: Limits the returned list to the specified number of results. Defaults to 1000.
            id: List of table IDs to filter by.
            order_by: The sort order of the returned list of tables.
            order_by_descending: Whether to sort descending instead of ascending. Defaults to false.
            continuation_token: The token used to paginate results.
            workspace: List of workspace IDs to filter by.

        Returns:
            The list of tables with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("tables", return_key="id")
    def create_table(self, table: models.CreateTableRequest) -> str:
        """Create a new table with the provided metadata and column definitions.

        Args:
            table: The request to create the table.

        Returns:
            The ID of the newly created table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("query-tables")
    def query_tables(self, query: models.QueryTablesRequest) -> models.PagedTables:
        """Queries available tables on the SystemLink DataFrame service and returns their metadata.

        Args:
            query: The request to query tables.

        Returns:
            The list of tables with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @get("tables/{id}")
    def get_table_metadata(self, id: str) -> models.TableMetadata:
        """Retrieves the metadata and column information for a single table identified by its ID.

        Args:
            id (str): Unique ID of a data table.

        Returns:
            The metadata for the table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @patch("tables/{id}", args=[Path, Body])
    def modify_table(self, id: str, update: models.ModifyTableRequest) -> None:
        """Modify properties of a table or its columns.

        Args:
            id: Unique ID of a data table.
            update: The metadata to update.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @delete("tables/{id}")
    def delete_table(self, id: str) -> None:
        """Deletes a table.

        Args:
            id (str): Unique ID of a data table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("delete-tables", args=[Field("ids")])
    def delete_tables(self, ids: List[str]) -> models.DeleteTablesPartialSuccess | None:
        """Deletes multiple tables.

        Args:
            ids (List[str]): List of unique IDs of data tables.

        Returns:
            A partial success if any tables failed to delete, or None if all
            tables were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("modify-tables")
    def modify_tables(
        self, updates: models.ModifyTablesRequest
    ) -> models.ModifyTablesPartialSuccess | None:
        """Modify the properties associated with the tables identified by their IDs.

        Args:
            updates: The table modifications to apply.

        Returns:
            A partial success if any tables failed to be modified, or None if all
            tables were modified successfully.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @get(
        "tables/{id}/data",
        args=[
            Path("id"),
            Query("columns"),
            Query("orderBy"),
            Query("orderByDescending"),
            Query("take"),
            Query("continuationToken"),
        ],
    )
    def get_table_data(
        self,
        id: str,
        columns: List[str] | None = None,
        order_by: List[str] | None = None,
        order_by_descending: bool | None = None,
        take: int | None = None,
        continuation_token: str | None = None,
    ) -> models.PagedTableRows:
        """Reads raw data from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            columns: Columns to include in the response. Data will be returned in the same order as
                the columns. If not specified, all columns are returned.
            order_by: List of columns to sort by. Multiple columns may be specified to order rows
                that have the same value for prior columns. The columns used for ordering do not
                need to be included in the columns list, in which case they are not returned. If
                not specified, then the order in which results are returned is undefined.
            order_by_descending: Whether to sort descending instead of ascending. Defaults to false.
            take: Limits the returned list to the specified number of results. Defaults to 500.
            continuation_token: The token used to paginate results.

        Returns:
            The table data and total number of rows with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("tables/{id}/data", args=[Path, Body])
    def _append_table_data_json(
        self, id: str, data: models.AppendTableDataRequest
    ) -> None:
        """Internal uplink-implemented JSON append call."""
        ...

    @post(
        "tables/{id}/data",
        args=[Path, Body, Query("endOfData")],
        content_type="application/vnd.apache.arrow.stream",
    )
    def _append_table_data_arrow(
        self, id: str, data: Iterable[bytes], end_of_data: bool | None = None
    ) -> None:
        """Internal uplink-implemented Arrow (binary) append call."""
        ...

    def append_table_data(
        self,
        id: str,
        data: (
            Union[
                models.AppendTableDataRequest,
                models.DataFrame,
                "pa.RecordBatch",  # type: ignore[name-defined]
                Iterable["pa.RecordBatch"],  # type: ignore[name-defined]
            ]
            | None
        ),
        *,
        end_of_data: bool | None = None,
    ) -> None:
        """Appends one or more rows of data to the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            data: The data to append.

                Supported forms:

                * ``AppendTableDataRequest``: Sent as-is via JSON; ``end_of_data`` must be ``None``.
                * ``DataFrame`` (service model): Wrapped into an
                  ``AppendTableDataRequest`` (``end_of_data`` optional) and sent as JSON.
                * Single ``pyarrow.RecordBatch``: Treated the same as an iterable containing one
                  batch and streamed as Arrow IPC. ``end_of_data`` (if provided) is sent as a
                  query parameter.
                * ``Iterable[pyarrow.RecordBatch]``: Streamed as Arrow IPC. ``end_of_data`` (if
                  provided) is sent as a query parameter. If the iterator yields no batches, it is
                  treated as ``None`` and requires ``end_of_data``.
                * ``None``: ``end_of_data`` must be provided; sends JSON containing only the
                  ``endOfData`` flag (useful for closing a table without appending rows).
            end_of_data: Whether additional rows may be appended in future requests. Required when
                ``data`` is ``None`` or the RecordBatch iterator is empty; must be omitted when
                passing an ``AppendTableDataRequest`` (include it inside that model instead).

        Raises:
            ValueError: If parameter constraints are violated.
            ApiException: If unable to communicate with the DataFrame Service or an
                invalid argument is provided.
        """
        if isinstance(data, models.AppendTableDataRequest):
            if end_of_data is not None:
                raise ValueError(
                    "end_of_data must not be provided separately when passing an AppendTableDataRequest."
                )
            self._append_table_data_json(id, data)
            return

        if isinstance(data, models.DataFrame):
            if end_of_data is None:
                request_model = models.AppendTableDataRequest(frame=data)
            else:
                request_model = models.AppendTableDataRequest(
                    frame=data, end_of_data=end_of_data
                )
            self._append_table_data_json(id, request_model)
            return

        if pa is not None and isinstance(data, pa.RecordBatch):
            data = [data]

        if isinstance(data, Iterable):
            iterator = iter(data)
            try:
                first_batch = next(iterator)
            except StopIteration:
                if end_of_data is None:
                    raise ValueError(
                        "end_of_data must be provided when data iterator is empty."
                    )
                self._append_table_data_json(
                    id,
                    models.AppendTableDataRequest(end_of_data=end_of_data),
                )
                return

            if pa is None:
                raise RuntimeError(
                    "pyarrow is not installed. Install to stream RecordBatches."
                )

            if not isinstance(first_batch, pa.RecordBatch):
                raise ValueError(
                    "Iterable provided to data must yield pyarrow.RecordBatch objects."
                )

            def _generate_body() -> Iterable[memoryview]:
                batch = first_batch
                with BytesIO() as buf:
                    options = pa.ipc.IpcWriteOptions(compression="zstd")
                    writer = pa.ipc.new_stream(buf, batch.schema, options=options)

                    while True:
                        writer.write_batch(batch)
                        with buf.getbuffer() as view, view[0 : buf.tell()] as slice:
                            yield slice
                        buf.seek(0)
                        try:
                            batch = next(iterator)
                        except StopIteration:
                            break

                    writer.close()
                    with buf.getbuffer() as view, view[0 : buf.tell()] as slice:
                        yield slice

            try:
                self._append_table_data_arrow(
                    id,
                    _generate_body(),
                    end_of_data,
                )
            except core.ApiException as ex:
                if ex.http_status_code == 400:
                    wrap = True
                    try:
                        write_op = getattr(
                            self.api_info().operations, "write_data", None
                        )
                        if (
                            write_op is not None
                            and getattr(write_op, "version", 0) >= 2
                        ):
                            wrap = False
                    except Exception:
                        pass
                    if wrap:
                        raise core.ApiException(
                            (
                                "Arrow ingestion request was rejected. The target "
                                "DataFrame Service doesn't support Arrow streaming. "
                                "Install a DataFrame Service version with Arrow support "
                                "or fall back to JSON ingestion."
                            ),
                            error=ex.error,
                            http_status_code=ex.http_status_code,
                            inner=ex,
                        ) from ex
                raise
            return

        if data is None:
            if end_of_data is None:
                raise ValueError(
                    "end_of_data must be provided when data is None (no rows to append)."
                )
            self._append_table_data_json(
                id, models.AppendTableDataRequest(end_of_data=end_of_data)
            )
            return

        raise ValueError(
            "Unsupported type for data. Expected AppendTableDataRequest, DataFrame, Iterable[RecordBatch], or None."
        )

    @post("tables/{id}/query-data", args=[Path, Body])
    def query_table_data(
        self, id: str, query: models.QueryTableDataRequest
    ) -> models.PagedTableRows:
        """Reads rows of data that match a filter from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering and sorting to apply when reading data.

        Returns:
            The table data and total number of rows with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    @post("tables/{id}/query-decimated-data", args=[Path, Body])
    def query_decimated_data(
        self, id: str, query: models.QueryDecimatedDataRequest
    ) -> models.TableRows:
        """Reads decimated rows of data from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering and decimation options to apply when reading data.

        Returns:
            The decimated table data.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...

    def _iter_content_filelike_wrapper(response: Response) -> IteratorFileLike:
        return IteratorFileLike(response.iter_content(chunk_size=4096))

    @response_handler(_iter_content_filelike_wrapper)
    @post("tables/{id}/export-data", args=[Path, Body])
    def export_table_data(
        self, id: str, query: models.ExportTableDataRequest
    ) -> IteratorFileLike:
        """Exports rows of data that match a filter from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering, sorting, and export format to apply when exporting data.

        Returns:
            A file-like object for reading the exported data.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/__init__.py sha256=4eb4e0c631f97d367efd57df8f074dbd642a859715d61e557bf4e0bfff3b0b3d bytes=1396 -->
## FILE: nisystemlink/clients/dataframe/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/__init__.py`
- sha256: `4eb4e0c631f97d367efd57df8f074dbd642a859715d61e557bf4e0bfff3b0b3d`
- bytes: 1396

````python
from ._append_table_data_request import AppendTableDataRequest
from ._api_info import ApiInfo, Operation, OperationsV1
from ._create_table_request import CreateTableRequest
from ._column import Column
from ._column_filter import FilterOperation, ColumnFilter
from ._column_order_by import ColumnOrderBy
from ._column_type import ColumnType
from ._data_frame import DataFrame
from ._data_type import DataType
from ._delete_tables_partial_success import DeleteTablesPartialSuccess
from ._export_table_data_request import ExportTableDataRequest, ExportFormat
from ._modify_tables_partial_success import ModifyTablesPartialSuccess
from ._modify_table_request import ColumnMetadataPatch, ModifyTableRequest
from ._modify_tables_request import ModifyTablesRequest, TableMetadataModification
from ._order_by import OrderBy
from ._paged_tables import PagedTables
from ._paged_table_rows import PagedTableRows
from ._query_decimated_data_request import (
    DecimationMethod,
    DecimationOptions,
    QueryDecimatedDataRequest,
)
from ._query_table_data_request import QueryTableDataRequest
from ._query_tables_request import QueryTablesRequest
from ._table_metadata import TableMetadata
from ._table_rows import TableRows

# Alias to provide backwards compatibility for misnamed class, fixed in 1.0.2
TableMetdataModification = TableMetadataModification

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_api_info.py sha256=4ffc4d36e7426c535687fe8623bba080713d1c17b6049d95def17f40089fc6c5 bytes=896 -->
## FILE: nisystemlink/clients/dataframe/models/_api_info.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_api_info.py`
- sha256: `4ffc4d36e7426c535687fe8623bba080713d1c17b6049d95def17f40089fc6c5`
- bytes: 896

````python
from nisystemlink.clients.core._api_info import Operation
from nisystemlink.clients.core._uplink._json_model import JsonModel


class OperationsV1(JsonModel):
    """The operations available in the routes provided by the v1 HTTP API."""

    create_tables: Operation
    """The ability to create new data tables."""

    delete_tables: Operation
    """The ability to delete tables and all of their data."""

    modify_metadata: Operation
    """The ability to modify metadata for tables."""

    list_tables: Operation
    """The ability to locate and read metadata for tables."""

    read_data: Operation
    """The ability to query and read data from tables."""

    write_data: Operation
    """The ability to append rows of data to tables."""


class ApiInfo(JsonModel):
    """Information about the available API operations."""

    operations: OperationsV1
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_append_table_data_request.py sha256=948685b5c39ba5521d6764bc3443f13bac547b031f1f2be92d1a13993850be4d bytes=517 -->
## FILE: nisystemlink/clients/dataframe/models/_append_table_data_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_append_table_data_request.py`
- sha256: `948685b5c39ba5521d6764bc3443f13bac547b031f1f2be92d1a13993850be4d`
- bytes: 517

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._data_frame import DataFrame


class AppendTableDataRequest(JsonModel):
    """Contains the rows to append and optional flags. The ``frame`` field is
    required unless ``endOfData`` is true.
    """

    frame: DataFrame | None = None
    """The data frame containing the rows to append."""

    end_of_data: bool | None = None
    """Whether the table should expect any additional rows to be appended in future requests."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column.py sha256=84725a2d34a4ba3d8abc60218162baef2e4f4005d7b33cfbc7f0531015642c00 bytes=634 -->
## FILE: nisystemlink/clients/dataframe/models/_column.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_column.py`
- sha256: `84725a2d34a4ba3d8abc60218162baef2e4f4005d7b33cfbc7f0531015642c00`
- bytes: 634

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._column_type import ColumnType
from ._data_type import DataType


class Column(JsonModel):
    """Defines a single column in a table."""

    name: str
    """The column name, which must be unique across all columns in the table."""

    data_type: DataType
    """The data type of the column."""

    column_type: ColumnType = ColumnType.Normal
    """The column type. Defaults to ColumnType.Normal."""

    properties: Dict[str, str] | None = None
    """User-defined properties associated with the column."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_filter.py sha256=a17fd80f24fca5200bc623c9f7de5d69f9a03f3bf940729073fb385e0012733b bytes=1380 -->
## FILE: nisystemlink/clients/dataframe/models/_column_filter.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_column_filter.py`
- sha256: `a17fd80f24fca5200bc623c9f7de5d69f9a03f3bf940729073fb385e0012733b`
- bytes: 1380

````python
from enum import Enum

from nisystemlink.clients.core._uplink._json_model import JsonModel


class FilterOperation(str, Enum):
    """Represents the different operations that can be used in a filter."""

    Equals = "EQUALS"
    NotEquals = "NOT_EQUALS"
    LessThan = "LESS_THAN"
    LessThanEquals = "LESS_THAN_EQUALS"
    GreaterThan = "GREATER_THAN"
    GreaterThanEquals = "GREATER_THAN_EQUALS"
    Contains = "CONTAINS"
    NotContains = "NOT_CONTAINS"


class ColumnFilter(JsonModel):
    """A filter to apply to the table data."""

    column: str
    """The name of the column to use for filtering."""

    operation: FilterOperation
    """How to compare the column's value with the specified value.

    An error is returned if the column's data type does not support the specified operation:
    * String columns only support ``EQUALS``, ``NOT_EQUALS``, ``CONTAINS``, and ``NOT_CONTAINS``.
    * Non-string columns do not support ``CONTAINS`` or ``NOT_CONTAINS``.
    * When ``value`` is ``None``, the operation must be ``EQUALS`` or ``NOT_EQUALS``.
    * When ``value`` is ``NaN`` for a floating-point column, the operation must be ``NOT_EQUALS``.
    """

    value: str | None = None
    """The comparison value to use for filtering. An error will be returned if
    the value cannot be converted to the column's data type."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_order_by.py sha256=0daf685c6436dc71ada15326c0f130fd62b6db4294e3986ebb8e9ab1b21c5b01 bytes=343 -->
## FILE: nisystemlink/clients/dataframe/models/_column_order_by.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_column_order_by.py`
- sha256: `0daf685c6436dc71ada15326c0f130fd62b6db4294e3986ebb8e9ab1b21c5b01`
- bytes: 343

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class ColumnOrderBy(JsonModel):
    """Specifies a column to order by and the ordering direction."""

    column: str
    """The name of the column to order by."""

    descending: bool | None = None
    """Whether the ordering should be in descending order."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_type.py sha256=6725b68580256e43734f59219618a5f4ee3f877d2bdb3b96090625e7596c56d8 bytes=663 -->
## FILE: nisystemlink/clients/dataframe/models/_column_type.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_column_type.py`
- sha256: `6725b68580256e43734f59219618a5f4ee3f877d2bdb3b96090625e7596c56d8`
- bytes: 663

````python
from enum import Enum


class ColumnType(str, Enum):
    """Represents the different column types for a table column."""

    Normal = "NORMAL"
    """The column has no special properties. This is the default."""

    Index = "INDEX"
    """The column provides a unique value per row. Each table must provide
    exactly one INDEX column. The column's :class:`.DataType` must be INT32,
    INT64, or TIMESTAMP."""

    Nullable = "NULLABLE"
    """Rows may contain null values for this column. When appending rows,
    NULLABLE columns may be left out entirely, in which case all rows being
    appended will use null values for that column."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_create_table_request.py sha256=31abb3ee20b0784bbd0cac452f81ac05473541c11ffa63d75ffd85a286a804a0 bytes=1184 -->
## FILE: nisystemlink/clients/dataframe/models/_create_table_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_create_table_request.py`
- sha256: `31abb3ee20b0784bbd0cac452f81ac05473541c11ffa63d75ffd85a286a804a0`
- bytes: 1184

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._column import Column


class CreateTableRequest(JsonModel):
    """Contains information needed to create a table, including its properties and column definitions."""

    columns: List[Column]
    """The list of columns in the table. Exactly one column must have a :class:`.ColumnType` of INDEX."""

    name: str | None = None
    """The name to associate with the table. When not specified, a name will be
    assigned from the table's ID."""

    properties: Dict[str, str] | None = None
    """User-defined properties to associate with the table."""

    test_result_id: str | None = None
    """The ID of the test result associated with the table. A value of ``None`` or an empty string
    indicates there is no associated test result. Added in version 2 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.create_tables` operation. Older
    versions of the service will ignore this value."""

    workspace: str | None = None
    """The workspace to create the table in. Uses the default workspace when not specified."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_data_frame.py sha256=aaf520a3530edcad9aa486a3e2c64b71dda2b6dced7d1a6dedeb8a57a69e5769 bytes=3106 -->
## FILE: nisystemlink/clients/dataframe/models/_data_frame.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_data_frame.py`
- sha256: `aaf520a3530edcad9aa486a3e2c64b71dda2b6dced7d1a6dedeb8a57a69e5769`
- bytes: 3106

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class DataFrame(JsonModel):
    """Data read from or to be written to a table.

    Values may be ``None`` (if the column is of type ``NULLABLE``) or encoded as
    a string in a format according to each column's datatype:

    * BOOL: One of ``"true"`` or ``"false"``, case-insensitive.
    * INT32: Any integer number in the range [-2147483648, 2147483647],
      surrounded by quotes.
    * INT64: Any integer number in the range [-9223372036854775808,
      9223372036854775807], surrounded by quotes.
    * FLOAT32: A decimal number using a period for the decimal point, optionally
      in scientific notation, in the range [-3.40282347E+38, 3.40282347E+38],
      surrounded by quotes. Not all values within the range can be represented
      with 32 bits. To preserve the exact binary encoding of the value when
      converting to a string, clients should serialize 9 digits after the
      decimal. Instead of a number, the value may be ``"NaN"`` (not a number),
      ``"Infinity"`` (positive infinity), or ``"-Infinity"`` (negative
      infinity), case-sensitive.
    * FLOAT64: A decimal number using a period for the decimal point, optionally
      in scientific notation, in the range [-1.7976931348623157E+308,
      1.7976931348623157E+308], surrounded by quotes. Not all values within the
      range can be represented with 64 bits. To preserve the exact binary
      encoding of the value when converting to a string, clients should
      serialize 17 digits after the decimal. Instead of a number, the value may
      be ``"NaN"`` (not a number), ``"Infinity"`` (positive infinity), or
      ``"-Infinity"`` (negative infinity), case-sensitive.
    * STRING: Any quoted string.
    * TIMESTAMP: A date and time with millisecond precision in ISO-8601 format
      and time zone. For example: ``"2022-08-19T16:17:30.123Z"``. If a time zone
      is not provided, UTC is assumed. If a time zone other than UTC is
      provided, the value will be converted to UTC. If more than three digits of
      fractional seconds are provided, the time will be truncated to three
      digits (i.e. milliseconds).

    The format is the same as a serialized Pandas DataFrame with orient="split"
    and index=False. See
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html.

    When providing a DataFrame for appending rows, any of the table's columns
    not specified will receive a value of ``None``. If any such columns aren't
    nullable, an error will be returned. If the entire columns property is left
    out, each row is assumed to contain all columns in the order specified when
    the table was created.
    """

    columns: List[str] | None = None
    """The names and order of the columns included in the data frame."""

    data: List[List[str | None]]
    """The data for each row with the order specified in the columns property.
    Must contain a value for each column in the columns property."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_data_type.py sha256=ab112d911449d3da66914af44a58d663ad36ab97d6a45c890059f52600b5eb49 bytes=625 -->
## FILE: nisystemlink/clients/dataframe/models/_data_type.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_data_type.py`
- sha256: `ab112d911449d3da66914af44a58d663ad36ab97d6a45c890059f52600b5eb49`
- bytes: 625

````python
from enum import Enum


class DataType(str, Enum):
    """Represents the different data types for a table column."""

    Bool = "BOOL"
    """32-bit IEEE 754 floating-point number."""

    Float32 = "FLOAT32"
    """32-bit IEEE 754 floating-point number."""

    Float64 = "FLOAT64"
    """64-bit IEEE 754 floating-point number."""

    Int32 = "INT32"
    """32-bit signed integers."""

    Int64 = "INT64"
    """64-bit signed integers."""

    String = "STRING"
    """Arbitrary string data."""

    Timestamp = "TIMESTAMP"
    """Date and time represented in UTC with millisecond precision."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py sha256=5d3cfbadbe3e59ca6bc0b92815eba98b7463c6bbfba42d2bf4e45cc54494645f bytes=570 -->
## FILE: nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py`
- sha256: `5d3cfbadbe3e59ca6bc0b92815eba98b7463c6bbfba42d2bf4e45cc54494645f`
- bytes: 570

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteTablesPartialSuccess(JsonModel):
    """The result of deleting multiple tables when one or more tables could not be deleted."""

    deleted_table_ids: List[str]
    """The IDs of the tables that were successfully deleted."""

    failed_table_ids: List[str]
    """The IDs of the tables that could not be deleted."""

    error: ApiError
    """The error that occurred when deleting the tables."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_export_table_data_request.py sha256=752462f3bb79bc72aaf6fd57ecef387fea73bd0b409835072969fd8ffa4a22c3 bytes=1930 -->
## FILE: nisystemlink/clients/dataframe/models/_export_table_data_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_export_table_data_request.py`
- sha256: `752462f3bb79bc72aaf6fd57ecef387fea73bd0b409835072969fd8ffa4a22c3`
- bytes: 1930

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._column_filter import ColumnFilter
from ._column_order_by import ColumnOrderBy


class ExportFormat(str, Enum):
    """The format of the exported data."""

    CSV = "CSV"
    """Comma-separated values."""


class ExportTableDataRequest(JsonModel):
    """Specifies the parameters for a data export with ordering and filtering."""

    columns: List[str] | None = None
    """The names of columns to include in the export. The export will
    include the columns in the same order specified in this parameter. All
    columns are included in the order specified at table creation if this
    property is excluded."""

    order_by: List[ColumnOrderBy] | None = None
    """A list of columns to order the results by. Multiple columns may be
    specified to order rows that have the same value for prior columns. The
    columns used for sorting do not need to be included in the columns list, in
    which case they are not included in the export."""

    filters: List[ColumnFilter] | None = None
    """A list of columns to filter by. Only rows whose columns contain values
    matching all of the specified filters are returned. The columns used for
    filtering do not need to be included in the columns list, in which case
    they are not included in the export."""

    take: int | None = None
    """The maximum number of rows to include in the export. If ``None``
    (the default), all rows are included. Added in version 3 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.read_data`
    operation. Older versions of the service will ignore this value and
    always include all rows."""

    response_format: ExportFormat
    """The format of the exported data. The only response format
    currently supported is ``CSV``."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_table_request.py sha256=beb6c1ac953c7c4cf5d24b7c8d772b1ffa96f4bd0f3b2d0df33fbabce76c64f1 bytes=2275 -->
## FILE: nisystemlink/clients/dataframe/models/_modify_table_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_modify_table_request.py`
- sha256: `beb6c1ac953c7c4cf5d24b7c8d772b1ffa96f4bd0f3b2d0df33fbabce76c64f1`
- bytes: 2275

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class ColumnMetadataPatch(JsonModel):
    """Specifies column properties to add, modify, or delete when editing table metadata."""

    name: str
    """The name of the column to modify."""

    properties: Dict[str, str | None]
    """The properties to modify. A map of key value properties containing the metadata
    to be added or modified. Set a property value to ``None`` to delete the property."""


class ModifyTableRequest(JsonModel):
    """Contains the metadata properties to modify. Values not included will remain unchanged."""

    metadata_revision: int | None = None
    """When specified, this is an integer that must match the last known
    revision number of the table, incremented by one. If it doesn't match the
    current ``metadataRevision`` incremented by one at the time of execution, the
    modify request will be rejected with a 409 Conflict. This is used to ensure
    that changes to this table's metadata are based on a known, previous
    state."""

    name: str | None = None
    """The new name of the table. Set to ``None`` to reset the name to the table's ID."""

    test_result_id: str | None = None
    """The new test result ID associated with the table. Set to ``None`` or an empty string to
    remove the test result ID. Added in version 2 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.modify_metadata` operation. Older
    versions of the service will ignore this value."""

    workspace: str | None = None
    """The new workspace for the table. Set to ``None`` to reset to the
    default workspace. Changing the workspace requires permission to delete the
    table in its current workspace and permission to create the table in its new
    workspace."""

    properties: Dict[str, str | None] | None = None
    """The properties to modify. A map of key value properties containing the
    metadata to be added or modified. Set a property value to ``None`` to
    delete the property."""

    columns: List[ColumnMetadataPatch] | None = None
    """Updates to the column properties. Cannot add or remove columns, or change the name of a column."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py sha256=7474cd3c08c5a8be1b2fa1f068d9ba1ecc7c2371601274c20e41258c1b2c7103 bytes=672 -->
## FILE: nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py`
- sha256: `7474cd3c08c5a8be1b2fa1f068d9ba1ecc7c2371601274c20e41258c1b2c7103`
- bytes: 672

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._modify_tables_request import TableMetadataModification


class ModifyTablesPartialSuccess(JsonModel):
    """The result of modifying multiple tables when one or more tables could not be modified."""

    modified_table_ids: List[str]
    """The IDs of the tables that were successfully modified."""

    failed_modifications: List[TableMetadataModification]
    """The requested modifications that could not be applied."""

    error: ApiError
    """The error that occurred when modifying the tables."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_tables_request.py sha256=1808a3c8a07189c5298b0d8cf5657813cb711ae86cb62b3b54eabf1318b1729a bytes=2176 -->
## FILE: nisystemlink/clients/dataframe/models/_modify_tables_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_modify_tables_request.py`
- sha256: `1808a3c8a07189c5298b0d8cf5657813cb711ae86cb62b3b54eabf1318b1729a`
- bytes: 2176

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class TableMetadataModification(JsonModel):
    """Contains the metadata properties to modify. Values not included in the
    request or included with a ``None`` value will remain unchanged.
    """

    id: str
    """The ID of the table to modify."""

    metadata_revision: int | None = None
    """When specified, this is an integer that must match the last known
    revision number of the table, incremented by one. If it doesn't match the
    current ``metadataRevision`` incremented by one at the time of execution, the
    modify request will be rejected with a conflict error. This is used to
    ensure that changes to this table's metadata are based on a known, previous
    state."""

    name: str | None = None
    """The new name of the table."""

    test_result_id: str | None = None
    """The new test result ID associated with the table. Set to an empty string to remove
    the test result ID. Added in version 2 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.modify_metadata` operation. Older
    versions of the service will ignore this value."""

    workspace: str | None = None
    """The new workspace for the table. Changing the workspace requires
    permission to delete the table in its current workspace and permission to
    create the table in its new workspace."""

    properties: Dict[str, str | None] | None = None
    """The properties to modify. A map of key value properties containing the
    metadata to be added or modified. Setting a property value to ``None`` will
    delete the property. Existing properties not included in the map are
    unaffected unless replace is true in the top-level request object."""


class ModifyTablesRequest(JsonModel):
    """Contains one or more table modifications to apply."""

    tables: List[TableMetadataModification]
    """The table modifications to apply. Each table may only appear once in the list."""

    replace: bool | None = None
    """When true, existing properties are replaced instead of merged."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_order_by.py sha256=b2252c98f31329d0c9243ff2ee44e80f63ae673fdc64d75354708b333f132334 bytes=641 -->
## FILE: nisystemlink/clients/dataframe/models/_order_by.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_order_by.py`
- sha256: `b2252c98f31329d0c9243ff2ee44e80f63ae673fdc64d75354708b333f132334`
- bytes: 641

````python
from typing import Literal

# TODO: Migrate to Enum when this change is released: https://github.com/prkumar/uplink/pull/282
OrderBy = Literal[
    "CREATED_AT", "METADATA_MODIFIED_AT", "NAME", "NUMBER_OF_ROWS", "ROWS_MODIFIED_AT"
]
"""Possible options for sorting when querying tables.

* ``CREATED_AT``: The date and time the table was created.
* ``METADATA_MODIFIED_AT``: The date and time the table's metadata properties were modified.
* ``NAME``: The name of the table.
* ``NUMBER_OF_ROWS``: The number of rows of data in the table.
* ``ROWS_MODIFIED_AT``: Date and time rows were most recently appended to the table.
"""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_paged_table_rows.py sha256=ca7d57e791872da9bc048fc626f24e36c4b3ee28118ae78038573c10a14ae5b6 bytes=401 -->
## FILE: nisystemlink/clients/dataframe/models/_paged_table_rows.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_paged_table_rows.py`
- sha256: `ca7d57e791872da9bc048fc626f24e36c4b3ee28118ae78038573c10a14ae5b6`
- bytes: 401

````python
from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._data_frame import DataFrame


class PagedTableRows(WithPaging):
    """Contains the result of a query for rows of data."""

    frame: DataFrame
    """The data frame containing the rows of data."""

    total_row_count: int
    """The total number of rows matched by the query across all pages of results."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_paged_tables.py sha256=da791f41a2e2df0705616957a855e67bf063740f4bd3b1c5fcc7b336d6c4fdbe bytes=341 -->
## FILE: nisystemlink/clients/dataframe/models/_paged_tables.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_paged_tables.py`
- sha256: `da791f41a2e2df0705616957a855e67bf063740f4bd3b1c5fcc7b336d6c4fdbe`
- bytes: 341

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._table_metadata import TableMetadata


class PagedTables(WithPaging):
    """The response for a table query containing the matched tables."""

    tables: List[TableMetadata]
    """The list of tables returned by the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_decimated_data_request.py sha256=a22abd59cb4f8b1d7f1572b934b851310adff68f35770cf22387ecad0719b11f bytes=2480 -->
## FILE: nisystemlink/clients/dataframe/models/_query_decimated_data_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_query_decimated_data_request.py`
- sha256: `a22abd59cb4f8b1d7f1572b934b851310adff68f35770cf22387ecad0719b11f`
- bytes: 2480

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._query_table_data_base import QueryTableDataBase


class DecimationMethod(str, Enum):
    """Represents the different methods that can be used to decimate data."""

    Lossy = "LOSSY"
    """Creates an ``x_column`` ordered set and returns an uniformly distributed
    sample of rows with as many rows as the number specified as ``intervals.``"""

    MaxMin = "MAX_MIN"
    """Creates an ``x_column`` ordered set which will be divided in the number of
    ``intervals`` specified. For each of the intervals, the maximum and minimum
    values for all the columns specified in ``y_columns`` will be returned."""

    EntryExit = "ENTRY_EXIT"
    """Creates an ``x_column`` ordered set which will be divided in the number of
    ``intervals`` specified. For each of the intervals, the first and last row
    within the interval will be returned in addition to the maximum and minimum
    values for all the columns specified in ``y_columns``."""


class DecimationOptions(JsonModel):
    """Contains the parameters to use for data decimation."""

    x_column: str | None = None
    """The name of the column that will be used as the x-axis for decimating the
    data. The column in the table that was specified as Index will be used if
    this field is excluded. Only numeric columns are supported. i.e. ``INT32``,
    ``INT64``, ``FLOAT32``, ``FLOAT64`` and ``TIMESTAMP``."""

    y_columns: List[str] | None = None
    """A list of columns to decimate by. This property is only needed when the
    specified method is ``MAX_MIN`` or ``ENTRY_EXIT``. Only numeric columns are
    supported. i.e. ``INT32``, ``INT64``, ``FLOAT32``, ``FLOAT64`` and
    ``TIMESTAMP``."""

    intervals: int | None = None
    """Number of intervals to use for decimation. Defaults to 1000."""

    method: DecimationMethod | None = None
    """Specifies the method used to decimate the data. Defaults to
    :class:`DecimationMethod.Lossy`"""


class QueryDecimatedDataRequest(QueryTableDataBase):
    """Specifies the columns, filters and decimation parameters for a query."""

    decimation: DecimationOptions | None = None
    """The decimation options to use when querying data. If not specified, the
    default is to use :class:`DecimationMethod.Lossy` with 1000 intervals over
    the table's index column."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_table_data_base.py sha256=b684d732b93bd08afbe2e2c92fc22b2d1142803fd0cb9e76eef20badcadb213e bytes=899 -->
## FILE: nisystemlink/clients/dataframe/models/_query_table_data_base.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_query_table_data_base.py`
- sha256: `b684d732b93bd08afbe2e2c92fc22b2d1142803fd0cb9e76eef20badcadb213e`
- bytes: 899

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._column_filter import ColumnFilter


class QueryTableDataBase(JsonModel):
    """Contains the common set of options when querying table data."""

    columns: List[str] | None = None
    """The names of columns to include in the response. The response will
    include the columns in the same order specified in this parameter. All
    columns are included in the order specified at table creation if this
    property is excluded."""

    filters: List[ColumnFilter] | None = None
    """A list of columns to filter by. Only rows whose columns contain values
    matching all of the specified filters are returned. The columns used for
    filtering do not need to be included in the columns list. When reading
    decimated data, the filters are applied before decimation."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_table_data_request.py sha256=1c6a058ba17866847170b182aeebef9b120775e08f57764bccd3b22a54b948c3 bytes=881 -->
## FILE: nisystemlink/clients/dataframe/models/_query_table_data_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_query_table_data_request.py`
- sha256: `1c6a058ba17866847170b182aeebef9b120775e08f57764bccd3b22a54b948c3`
- bytes: 881

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._column_order_by import ColumnOrderBy
from ._query_table_data_base import QueryTableDataBase


class QueryTableDataRequest(QueryTableDataBase, WithPaging):
    """Contains the filtering and sorting options to use when querying table data."""

    order_by: List[ColumnOrderBy] | None = None
    """A list of columns to order the results by. Multiple columns may be
    specified to order rows that have the same value for prior columns. The
    columns used for sorting do not need to be included in the columns list, in
    which case they are not returned. If ``order_by`` is not specified, then the
    order in which results are returned is undefined."""

    take: int | None = None
    """Limits the returned list to the specified number of results."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_tables_request.py sha256=ac35a48e73f5521359ee6365c13599ae9a72a03e79046e691c9e27d04bedbf35 bytes=4372 -->
## FILE: nisystemlink/clients/dataframe/models/_query_tables_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_query_tables_request.py`
- sha256: `ac35a48e73f5521359ee6365c13599ae9a72a03e79046e691c9e27d04bedbf35`
- bytes: 4372

````python
from datetime import datetime
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging
from pydantic import StrictBool, StrictInt

from ._order_by import OrderBy


class QueryTablesRequest(WithPaging):
    """Request parameters for querying tables."""

    filter: str
    """The table query filter in `Dynamic LINQ`_ format.

    .. _Dynamic LINQ: https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language

    Allowed properties in the filter are:

    * ``columns``: List of columns in the table (see below; requires version 2 of the
      :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.list_tables` operation)
    * ``createdAt``: DateTime the table was created
    * ``createdWithin``: TimeSpan in which the table was created
    * ``id``: String value uniquely identifying the table
    * ``name``: String name for the table
    * ``metadataModifiedAt``: DateTime the table's metadata was last modified
    * ``metadataModifiedWithin``: TimeSpan in which the table's metadata was
      last modified
    * ``properties``: Dictionary with string keys and values representing table
      metadata
    * ``rowsModifiedAt``: DateTime rows were last appended to the table
    * ``rowsModifiedWithin``: TimeSpan within rows were last appended to the
      table
    * ``rowCount``: Int32 number of rows in the table
    * ``supportsAppend``: Boolean indicating whether or not the table supports
      appending additional rows of data
    * ``testResultId``: String ID of the test result associated with the table (requires version 2
      of the :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.list_tables` operation)
    * ``workspace``: String ID of the workspace the table belongs to
    * ``workspaceName``: String name of the workspace the table belongs to

    Allowed properties in the ``columns`` list are:

    * ``name``: String name of the column (requires a ``testResultId`` filter)

    Allowed constants in the filter are:

    * ``RelativeTime.CurrentDay``: TimeSpan representing the elapsed time
      between now and the start of the current day
    * ``RelativeTime.CurrentWeek``: TimeSpan representing the elapsed time
      between now and the start of the current week
    * ``RelativeTime.CurrentMonth``: TimeSpan representing the elapsed time
      between now and the start of the current month
    * ``RelativeTime.CurrentYear``: TimeSpan representing the elapsed time
      between now and the start of the current year
    """

    substitutions: List[StrictInt | StrictBool | str | None] | None = None
    """Make substitutions in the query filter expression.

    Substitutions for the query expression are indicated by non-negative
    integers that are prefixed with the ``@`` symbol. Each substitution in the given
    expression will be replaced by the element at the corresponding index
    (zero-based) in this list. For example, ``@0`` in the filter expression will be
    replaced with the element at the zeroth index of the substitutions list.
    """

    reference_time: datetime | None = None
    """The date and time to use as the reference point for `RelativeTime` filters,
    including time zone information. Defaults to the time on the server in UTC."""

    take: int | None = None
    """Limits the returned list to the specified number of results."""

    order_by: OrderBy | None = None
    """The sort order of the returned list of tables."""

    order_by_descending: bool | None = None
    """Whether to sort descending instead of ascending.

    The elements in the list are sorted ascending by default. If the
    orderByDescending parameter is specified, the elements in the list are
    sorted based on it's value. The orderByDescending value must be a boolean
    string. The elements in the list are sorted ascending if false and
    descending if true.
    """

    interactive: bool | None = None
    """Whether the query is being made within an interactive context, such as a web UI.
    Interactive queries receive faster feedback for slow queries. Added in version 2 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.list_tables` operation.
    Older versions of the service will ignore this value."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_table_metadata.py sha256=58932d19f0824cbe90f7ebd6200cd985576a70eb8b050145b6172c5f0f9ef27d bytes=1554 -->
## FILE: nisystemlink/clients/dataframe/models/_table_metadata.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_table_metadata.py`
- sha256: `58932d19f0824cbe90f7ebd6200cd985576a70eb8b050145b6172c5f0f9ef27d`
- bytes: 1554

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._column import Column


class TableMetadata(JsonModel):
    """Contains information about a table, including its properties and column definitions."""

    columns: List[Column]
    """The list of columns in the table."""

    created_at: datetime
    """The date and time the table was created."""

    id: str
    """The table's unique identifier."""

    metadata_modified_at: datetime
    """The date and time the table's metadata was last modified."""

    metadata_revision: int
    """The table's metadata revision number, incremented each time the metadata is modified."""

    name: str
    """The name associated with the table."""

    properties: Dict[str, str]
    """User-defined properties associated with the table."""

    row_count: int
    """The number of rows in the table."""

    rows_modified_at: datetime
    """The date and time the table's data was last modified."""

    supports_append: bool
    """Whether the table supports appending additional rows of data."""

    test_result_id: str | None = None
    """The ID of the test result associated with the table. Added in version 2 of the
    :py:attr:`nisystemlink.clients.dataframe.models.OperationsV1.list_tables` operation. This
    value will always be ``None`` when communicating with older versions of the service."""

    workspace: str
    """The workspace the table belongs to."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_table_rows.py sha256=0ce30e0ea4379a24029a9ab6d376ba16bfa8cc039f433e883aa090f9449ecb6e bytes=289 -->
## FILE: nisystemlink/clients/dataframe/models/_table_rows.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/dataframe/models/_table_rows.py`
- sha256: `0ce30e0ea4379a24029a9ab6d376ba16bfa8cc039f433e883aa090f9449ecb6e`
- bytes: 289

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._data_frame import DataFrame


class TableRows(JsonModel):
    """Contains the result of a query for rows of decimated data."""

    frame: DataFrame
    """The data frame containing the rows of data."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/__init__.py sha256=86a03867eb04e231fa60eefdafbcab05bb6e8d3fc70ad034e1cf9bc8c92aca2b bytes=127 -->
## FILE: nisystemlink/clients/feeds/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/__init__.py`
- sha256: `86a03867eb04e231fa60eefdafbcab05bb6e8d3fc70ad034e1cf9bc8c92aca2b`
- bytes: 127

````python
"""Start here with FeedsClient for feed management."""

from ._feeds_client import FeedsClient

__all__ = ["FeedsClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/_feeds_client.py sha256=3bc9d32abe16fca2299b8301345c7836bd49d36ea3fda4df943455a26ee17ed8 bytes=6208 -->
## FILE: nisystemlink/clients/feeds/_feeds_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/_feeds_client.py`
- sha256: `3bc9d32abe16fca2299b8301345c7836bd49d36ea3fda4df943455a26ee17ed8`
- bytes: 6208

````python
"""Implementation of SystemLink Feeds Client."""

from typing import BinaryIO, List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import delete, get, post
from nisystemlink.clients.core._uplink._multipart_retry import (
    retryable_multipart_request,
)
from uplink import Part, Path, Query, retry

from . import models


@retry(when=retry.when.status(429), stop=retry.stop.after_attempt(5))
class FeedsClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/nifeed/v1/")

    @post("feeds")
    def create_feed(self, feed: models.CreateFeedRequest) -> models.Feed:
        """Create a new feed with the provided feed details.

        Args:
            feeds (models.CreateFeedsRequest): Request to create the feed.

        Returns:
            models.Feed: Details of the created feed.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        ...

    @get("feeds", args=[Query, Query])
    def __query_feeds(
        self,
        platform: str | None = None,
        workspace: str | None = None,
    ) -> models.QueryFeedsResponse:
        """Lists available feeds for the Platform `platform` under the Workspace `workspace`.

        Args:
            platform (str | None): Information about system platform. Defaults to None.
            workspace (str | None): Workspace id. Defaults to None.

        Returns:
            models.QueryFeedsResponse: List of feeds.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        ...

    def query_feeds(
        self,
        platform: models.Platform | None = None,
        workspace: str | None = None,
    ) -> List[models.Feed]:
        """Lists available feeds for the Platform `platform` under the Workspace `workspace`.

        Args:
            platform (models.Platform | None): Information about system platform.
                Defaults to None.
            workspace (str | None): Workspace id. Defaults to None.

        Returns:
            List[models.Feed]: List of feeds.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        platform_by_str = platform.value if platform is not None else None
        response = self.__query_feeds(
            platform=platform_by_str,
            workspace=workspace,
        ).feeds

        return response

    @retryable_multipart_request()
    @post(
        "feeds/{feedId}/packages",
        args=[Path(name="feedId"), Part(), Query(name="shouldOverwrite")],
    )
    def __upload_package(
        self,
        feed_id: str,
        package: Part,
        overwrite: Query = False,
    ) -> models.Package:
        """Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package (Part): Package file to be uploaded.
            overwrite (Query): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        ...

    def upload_package(
        self,
        feed_id: str,
        package_file_path: str,
        overwrite: bool = False,
    ) -> models.Package:
        """Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package_file_path (str): File path of the package to be uploaded.
            overwrite (bool): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
            OSError: if the file does not exist or cannot be opened.
        """
        response = self.__upload_package(
            feed_id=feed_id,
            overwrite=overwrite,
            package=open(package_file_path, "rb"),
        )

        return response

    def upload_package_content(
        self,
        feed_id: str,
        package: BinaryIO,
        overwrite: bool = False,
    ) -> models.Package:
        """Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package (BinaryIO): Package file to be uploaded.
            overwrite (bool): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        response = self.__upload_package(
            feed_id=feed_id,
            overwrite=overwrite,
            package=package,
        )

        return response

    @delete(
        "feeds/{feedId}",
        args=[Path(name="feedId")],
    )
    def delete_feed(self, id: str) -> None:
        """Delete feed and its packages.

        Args:
            id (str): ID of the feed to be deleted.

        Returns:
            None.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/__init__.py sha256=8f29829be9c8d5ae3a83084f31311ea56de7efd091d9374bdf4bf2cefed5c564 bytes=198 -->
## FILE: nisystemlink/clients/feeds/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/__init__.py`
- sha256: `8f29829be9c8d5ae3a83084f31311ea56de7efd091d9374bdf4bf2cefed5c564`
- bytes: 198

````python
from ._create_feed import CreateFeedRequest
from ._feed import Feed
from ._package import Package
from ._platform import Platform
from ._query_feeds import QueryFeedsResponse

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_create_feed.py sha256=7574e8bd55a0858a7e57a468939d9dd5bb2274f142481e192a0bee2dfa2e6b94 bytes=678 -->
## FILE: nisystemlink/clients/feeds/models/_create_feed.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/_create_feed.py`
- sha256: `7574e8bd55a0858a7e57a468939d9dd5bb2274f142481e192a0bee2dfa2e6b94`
- bytes: 678

````python
from __future__ import annotations

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._platform import Platform


class CreateFeedRequest(JsonModel):
    """Create Feed Request."""

    name: str
    """The name of the feed."""
    description: str | None = None
    """The description of the feed."""
    platform: Platform
    """The platform of the feed, the following package extensions are available: .nipkg for
    windows feeds, .ipk and .deb for ni-linux-rt feeds."""
    workspace: str | None = None
    """The ID of the workspace this feed belongs to. If the workspace is not defined,
    the default workspace is used."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_feed.py sha256=de6039b38853d38c129f09d99d70b5930a9729290b9b136795a63e532c8b0c46 bytes=1108 -->
## FILE: nisystemlink/clients/feeds/models/_feed.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/_feed.py`
- sha256: `de6039b38853d38c129f09d99d70b5930a9729290b9b136795a63e532c8b0c46`
- bytes: 1108

````python
from __future__ import annotations

from datetime import datetime
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._platform import Platform


class Feed(JsonModel):
    """Feed model."""

    id: str | None = None
    """The auto-generated ID of the feed."""
    name: str | None = None
    """The name of the feed."""
    description: str | None = None
    """The description of the feed."""
    platform: Platform | None = None
    """The platform of the feed, the following package extensions are available: .nipkg for
    windows feeds, .ipk and .deb for ni-linux-rt feeds.
    """
    workspace: str | None = None
    """The ID of the workspace this feed belongs to."""
    updated_at: datetime | None = None
    """The date of the latest feed update"""
    created_at: datetime | None = None
    """The date when the feed was created at."""
    package_sources: List[str] | None = None
    """The package sources list of the feed."""
    deleted: bool | None = None
    """Whether the feed deletion was requested."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_package.py sha256=03ded8eaa6801ef5d346618b25e7cd3f3f7bbffa12621691347c583a7fd9c5db bytes=3463 -->
## FILE: nisystemlink/clients/feeds/models/_package.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/_package.py`
- sha256: `03ded8eaa6801ef5d346618b25e7cd3f3f7bbffa12621691347c583a7fd9c5db`
- bytes: 3463

````python
from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class PackageMetadata(JsonModel):
    """Package Meta data."""

    package_name: str | None = None
    """The name of the package."""
    version: str | None = None
    """The version number of the package."""
    architecture: str | None = None
    """The architecture of the package."""
    breaks: List[str] | None = None
    """Information about other packages this package breaks."""
    conflicts: List[str] | None = None
    """Information about other packages this package conflicts with."""
    depends: List[str] | None = None
    """Information about other packages this package depends on."""
    description: str | None = None
    """The description of the package."""
    enhances: List[str] | None = None
    """Information about other packages this package enchances."""
    essential: bool | None = None
    """True if the package is essential."""
    file_name: str | None = None
    """The file name of the package. Depending on the selected platform,
    the following package extensions are available:
    .nipkg for windows feeds, .ipk and .deb for ni-linux-rt feeds."""
    homepage: str | None = None
    """The website of the maintainers for the package."""
    installed_size: int | None = None
    """The size of the package after install."""
    maintainer: str | None = None
    """The maintainer of the package (name and email address)."""
    predepends: List[str] | None = None
    """Information about other packages this package predepends."""
    priority: int | None = None
    """The priority of the package."""
    provides: List[str] | None = None
    """Information about other packages that this package provides."""
    recommends: List[str] | None = None
    """Information about other packages this package recommends."""
    release_notes: str | None = None
    """The release notes of the package."""
    replaces: List[str] | None = None
    """Information about other packages this package replaces."""
    section: str | None = None
    """The application area of the package."""
    size: int | None = None
    """The size (in bytes) of the package."""
    source: str | None = None
    """The source of the package."""
    suggests: List[str] | None = None
    """Information about other packages this package suggests."""
    tags: str | None = None
    """The tags of the package."""
    attributes: Dict[str, str] | None = None
    """The attributes of the package."""


class Package(JsonModel):
    """Package model."""

    id: str | None = None
    """Gets or sets the ID of this package. This is used to reference this package in the service."""
    file_name: str | None = None
    """The name of the file in this package."""
    feed_id: str | None = None
    """The ID of the feed this package is associated with."""
    workspace: str | None = None
    """The ID of the workspace this package belongs to.
    The workspace of a package is the workspace of feed this package is associated with."""
    updated_at: datetime | None = None
    """The date of the latest package update."""
    created_at: datetime | None = None
    """The date when the package was created at."""
    metadata: PackageMetadata | None = None
    """Package meta data."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_platform.py sha256=3b6ad4904bd3c3f5c38601fdf23ffc396906b7bb8d10962ebdcd355863ab3806 bytes=169 -->
## FILE: nisystemlink/clients/feeds/models/_platform.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/_platform.py`
- sha256: `3b6ad4904bd3c3f5c38601fdf23ffc396906b7bb8d10962ebdcd355863ab3806`
- bytes: 169

````python
from __future__ import annotations

from enum import Enum


class Platform(Enum):
    """Platform."""

    WINDOWS = "WINDOWS"
    NI_LINUX_RT = "NI_LINUX_RT"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_query_feeds.py sha256=7d7ddaf821393af584e9f57a1524969c65fa5341cbb738fde7dbd3dfb4cb4f2a bytes=294 -->
## FILE: nisystemlink/clients/feeds/models/_query_feeds.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/models/_query_feeds.py`
- sha256: `7d7ddaf821393af584e9f57a1524969c65fa5341cbb738fde7dbd3dfb4cb4f2a`
- bytes: 294

````python
from __future__ import annotations

from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._feed import Feed


class QueryFeedsResponse(JsonModel):
    """Query Feeds response."""

    feeds: List[Feed]
    """A collection of feeds"""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/utilities/__init__.py sha256=2948693d97fade8d59f9c749b264d412233066e5846e0386980f90d050fe9576 bytes=67 -->
## FILE: nisystemlink/clients/feeds/utilities/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/utilities/__init__.py`
- sha256: `2948693d97fade8d59f9c749b264d412233066e5846e0386980f90d050fe9576`
- bytes: 67

````python
from ._get_feed_details import get_feed_by_name

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/utilities/_get_feed_details.py sha256=0b1efd8fac04b66c9cd7eb7e37522956cfa38679ae27ffa36a1aa405bdc75972 bytes=539 -->
## FILE: nisystemlink/clients/feeds/utilities/_get_feed_details.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/feeds/utilities/_get_feed_details.py`
- sha256: `0b1efd8fac04b66c9cd7eb7e37522956cfa38679ae27ffa36a1aa405bdc75972`
- bytes: 539

````python
"""Utilities for getting feed details."""

from typing import List

from nisystemlink.clients.feeds.models import Feed


def get_feed_by_name(
    feeds: List[Feed],
    name: str,
) -> Feed | None:
    """Get feed information from the list of feeds using `name`.

    Args:
        feeds (List[Feed]): List of feeds.
        name (str): Feed name.

    Returns:
        Feed | None: Feed information.
    """
    for feed in feeds:
        if feed.name == name and feed.id:
            return feed
    return None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/__init__.py sha256=6aa8b3199f2cf1a93f270806dce9df5d0627a56d5ed13f6dcd3b3e3bd2c630d8 bytes=123 -->
## FILE: nisystemlink/clients/file/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/__init__.py`
- sha256: `6aa8b3199f2cf1a93f270806dce9df5d0627a56d5ed13f6dcd3b3e3bd2c630d8`
- bytes: 123

````python
"""Start here with FileClient for file operations."""

from ._file_client import FileClient

__all__ = ["FileClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/_file_client.py sha256=d5961a279dc35d92e5ff7dcaea7f4da5e364d8de9f647373162c517cee96624c bytes=19688 -->
## FILE: nisystemlink/clients/file/_file_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/_file_client.py`
- sha256: `d5961a279dc35d92e5ff7dcaea7f4da5e364d8de9f647373162c517cee96624c`
- bytes: 19688

````python
"""Implementation of FileClient."""

import json
from typing import BinaryIO, Dict, List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._file_like_response import (
    file_like_response_handler,
)
from nisystemlink.clients.core._uplink._methods import (
    delete,
    get,
    post,
    response_handler,
)
from nisystemlink.clients.core._uplink._multipart_retry import (
    retryable_multipart_request,
)
from nisystemlink.clients.core.helpers import IteratorFileLike
from requests.models import Response
from uplink import Body, Field, params, Part, Path, Query, retry

from . import models


def _file_uri_response_handler(response: Response) -> str:
    """Response handler for File URI response. Extracts ID from URI."""
    resp = response.json()
    uri: str = resp["uri"]
    # Split the uri by '/' and get the last part
    parts = uri.split("/")
    return parts[-1]


@retry(when=retry.when.status(429), stop=retry.stop.after_attempt(5))
class FileClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, "/nifile/v1/")

    @get("")
    def api_info(self) -> models.V1Operations:
        """Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @get(
        "service-groups/Default/files",
        args=[
            Query,
            Query,
            Query(name="orderBy"),
            Query(name="orderByDescending"),
            Query(name="id"),
        ],
    )
    def __get_files(
        self,
        skip: int = 0,
        take: int = 0,
        order_by: str | None = None,
        order_by_descending: str | None = "false",
        ids: str | None = None,
    ) -> models.FileQueryResponse:
        """Lists available files on the SystemLink File service.
        Use the skip and take parameters to return paged responses.
        The orderBy and orderByDescending fields can be used to manage sorting the list by metadata objects.

        Args:
            skip: How many files to skip in the result when paging. Defaults to 0.
            take: How many files to return in the result, or 0 to use a default defined by the service.
              Defaults to 0.
            order_by: The name of the metadata key to sort by. Defaults to None.
            order_by_descending: The elements in the list are sorted ascending if "false"
              and descending if "true". Defaults to "false".
            ids: Comma-separated list of file IDs to search by. Defaults to None.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    def get_files(
        self,
        skip: int = 0,
        take: int = 0,
        order_by: models.FileQueryOrderBy | None = None,
        order_by_descending: bool | None = False,
        ids: List[str] | None = None,
    ) -> models.FileQueryResponse:
        """Lists available files on the SystemLink File service.
        Use the skip and take parameters to return paged responses.
        The orderBy and orderByDescending fields can be used to manage sorting the list by metadata objects.

        Args:
            skip: How many files to skip in the result when paging. Defaults to 0.
            take: How many files to return in the result, or 0 to use a default defined by the service.
            Defaults to 0.
            order_by: The name of the metadata key to sort by. Defaults to None.
            order_by_descending: The elements in the list are sorted ascending if False
            and descending if True. Defaults to False.
            ids: List of file IDs to search by. Defaults to None.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        """
        # Uplink does not support enum serializing into str
        # workaround as the service expects lower case `true` and `false`
        # uplink serializes bools to `True` and `False`
        order_by_str = order_by.value if order_by is not None else None
        order_by_desc_str = "true" if order_by_descending else "false"

        if ids:
            ids_str = ",".join(ids)
        else:
            ids_str = ""

        resp = self.__get_files(
            skip=skip,
            take=take,
            order_by=order_by_str,
            order_by_descending=order_by_desc_str,
            ids=ids_str,
        )

        return resp

    @post("service-groups/Default/query-files-linq")
    def query_files_linq(
        self, query: models.FileLinqQueryRequest
    ) -> models.FileLinqQueryResponse:
        """Queries file using LINQ filters.

        Args:
            query: The LINQ query request containing the following parameters:

                - **filter** (:class:`str`, optional): The filter criteria for files. Consists of a
                  string of queries composed using AND/OR operators. String values and date strings
                  need to be enclosed in double quotes. Parentheses can be used around filters to
                  better define the order of operations.

                  Filter syntax: ``[property name][operator][operand] and [property name][operator][operand]``

                  Operators:

                  - Equals: ``x = y``
                  - Not equal: ``x != y``
                  - Greater than: ``x > y``
                  - Greater than or equal: ``x >= y``
                  - Less than: ``x < y``
                  - Less than or equal: ``x <= y``
                  - Logical AND: ``x and y`` or ``x && y``
                  - Logical OR: ``x or y`` or ``x || y``
                  - Contains: ``x.Contains(y)`` — checks if a list contains an element
                  - Not Contains: ``!x.Contains(y)`` — checks if a list does not contain an element

                  Valid file properties for filtering:

                  - ``created``: ISO timestamp string (e.g. ``"2023-01-01T08:00:00.000Z"``)
                  - ``updated``: ISO timestamp string (e.g. ``"2023-01-01T08:00:00.000Z"``)
                  - ``extension``: File extension (e.g. ``png``, ``txt``, ``pdf``)
                  - ``size``: File size in bytes (e.g. ``1024``)
                  - ``userId``: User ID that created the file (e.g. ``"8abc4b87-07d4-4f84-b54f-48eec89b07d4"``)
                  - ``properties``: File properties (e.g. ``properties['x'] = 'y'``)
                  - ``workspace``: The workspace of the files (e.g. ``"88974b87-07d4-4f84-b54f-48eec89b11ed"``)

                  Example::

                      '(name = "myfile.txt" OR extension = "png")'
                      ' and (DateTime(created) >'
                      ' DateTime.parse("2023-01-01T08:00:00.000Z"))'
                      ' and (size < 1024)'

                - **order_by** (:class:`~nisystemlink.clients.file.models.FileLinqQueryOrderBy`, optional):
                  The file property to order results by. One of ``created``, ``updated``,
                  ``extension``, ``size``, or ``workspace``. Defaults to ``updated``.

                - **order_by_descending** (:class:`bool`, optional): Whether to return the files in
                  descending order. Defaults to ``True``.

                - **skip** (:class:`int`, optional): How many files to skip in the result when paging.
                  For example, a list of 100 files with a skip value of 50 will return entries
                  starting from the 51st file. Defaults to ``0``.

                - **take** (:class:`int`, optional): Maximum number of files to return.
                  Defaults to ``1000``.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        """
        ...

    @post("service-groups/Default/search-files")
    def search_files(
        self, request: models.SearchFilesRequest
    ) -> models.SearchFilesResponse:
        """Search for files based on filter criteria.

        Note:
            This endpoint requires Elasticsearch to be configured in the SystemLink cluster.
            If Elasticsearch is not configured, this method will fail with an ApiException.
            For deployments without Elasticsearch, use `query_files_linq()` instead.
            You can call `api_info()` to check if the `search_files` operation is available
            in your deployment.

        Args:
            request: The search request containing filter, pagination, and sorting parameters.

                - **filter** (:class:`str`, optional): The filter criteria for files using Lucene
                  query syntax. The default search field is the file name. All searches are
                  case-insensitive.

                  Filter syntax: ``[property name][operator][operand] AND [property name][operator][operand]``

                  Operators:

                  - Logical AND: ``AND``. Example: ``Name: "name" AND Extension: "json"``
                  - Logical OR: ``OR``. Example: ``Name: "name" OR Extension: "json"``
                  - Negation: ``NOT``. Example: ``Name: (NOT MyFile)``
                  - Wildcard: ``*`` — matches any sequence of characters. Example: ``Name: "file*"``
                  - Exists: ``_exists_`` — matches files where a field has any value.
                    Example: ``_exists_: "Properties.property key"``
                  - Range brackets: matches values between two bounds for numeric and date fields.
                    Square brackets ``[`` and ``]`` denote inclusive bounds, curly braces ``{`` and
                    ``}`` denote exclusive bounds, and ``*`` denotes no bound (infinity).
                    Example: ``size: [100 TO 200]`` matches ``100 <= size <= 200``.
                    Example: ``created: [* TO "2024-01-01T00:00:00Z"]`` matches files
                    created on or before January 1st, 2024.

                  Valid file properties for filtering:

                  - ``created``: ISO timestamp string (e.g. ``"2018-05-15T18:54:27.519Z"``)
                  - ``extension``: File extension (e.g. ``png``, ``txt``, ``pdf``)
                  - ``id``: File ID (e.g. ``"5afb2ce3741fe11d88838cc9"``)
                  - ``name``: File name within the service group
                  - ``properties``: Key-value pairs of file metadata, filtered using the syntax
                    ``"properties.[key]": "[value]"``. Example: ``"properties.owner": "admin"``
                  - ``size``: File size in bytes (e.g. ``32``)
                  - ``workspace``: Workspace name (e.g. ``"MyWorkspace"``)

                  Example::

                      'name: "myfile*" AND size: [* TO 1024000000] AND workspace: "MyWorkspace"'

                - **order_by** (:class:`~nisystemlink.clients.file.models.SearchFilesOrderBy`,
                  optional): The file property to order results by. When not specified, results
                  are ordered by relevance score. One of ``name``, ``created``, ``id``, ``size``,
                  or ``updated``.

                - **order_by_descending** (:class:`bool`, optional): Whether to return the files
                  in descending order. Defaults to ``False``.

                - **skip** (:class:`int`, optional): How many files to skip in the result when
                  paging. For example, a list of 100 files with a skip value of 50 will return
                  entries starting from the 51st file. Defaults to ``0``.

                - **take** (:class:`int`, optional): Maximum number of files to return.
                  Defaults to ``1000``. Maximum allowed value is ``1000``.

        Returns:
            SearchFilesResponse: Response containing matching files and total count.

        Raises:
            ApiException: if unable to communicate with the File Service or if Elasticsearch
                is not configured in the cluster.
        """
        ...

    @params({"force": True})  # type: ignore
    @delete("service-groups/Default/files/{id}", args=[Path])
    def delete_file(self, id: str) -> None:
        """Deletes the file indicated by the `file_id`.

        Args:
            id: The ID of the file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @params({"force": True})  # type: ignore
    @post("service-groups/Default/delete-files", args=[Field])
    def delete_files(self, ids: List[str]) -> None:
        """Delete multiple files.

        Args:
            ids: List of unique IDs of Files.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @params({"inline": True})  # type: ignore
    @response_handler(file_like_response_handler)
    @get("service-groups/Default/files/{id}/data", args=[Path])
    def download_file(self, id: str) -> IteratorFileLike:
        """Downloads a file from the SystemLink File service.

        Args:
            id: The ID of the file.

        Yields:
            A file-like object for reading the exported data.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @response_handler(_file_uri_response_handler)
    @retryable_multipart_request()
    @post("service-groups/Default/upload-files")
    def __upload_file(
        self,
        file: Part,
        metadata: Part = None,
        id: Part = None,
        workspace: Query = None,
    ) -> str:
        """Uploads a file using multipart/form-data headers to send the file payload in the HTTP body.

        Args:
            file: The file to upload.
            metadata: Multipart part for file metadata, typically ``None`` or a
                ``(None, json_string, "application/json")`` tuple where
                ``json_string`` contains the metadata key/value pairs.
            id: Specify an unique (among all file) 24-digit Hex string ID of the file once it is uploaded.
                Defaults to None.
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            ID of uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    def upload_file(
        self,
        file: BinaryIO,
        metadata: Dict[str, str] | None = None,
        id: str | None = None,
        workspace: str | None = None,
    ) -> str:
        """Uploads a file to the File Service.

        Args:
            file: The file to upload.
            metadata: File Metadata as dictionary.
            id: Specify an unique (among all file) 24-digit Hex string ID of the file once it is uploaded.
                Defaults to None.
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            ID of uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """
        if metadata:
            metadata_part = (None, json.dumps(metadata), "application/json")
        else:
            metadata_part = None

        file_id = self.__upload_file(
            file=file,
            metadata=metadata_part,
            id=id,
            workspace=workspace,
        )

        return file_id

    @post("service-groups/Default/files/{id}/update-metadata", args=[Body, Path])
    def update_metadata(self, metadata: models.UpdateMetadataRequest, id: str) -> None:
        """Updates an existing file's metadata with the specified metadata properties.

        Args:
            metadata: File's metadata and options for updating it.
            id: ID of the file to update Metadata.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @post(
        "service-groups/Default/upload-sessions/start", args=[Query(name="workspace")]
    )
    def start_upload_session(
        self, workspace: str | None = None
    ) -> models.UploadSessionStartResponse:
        """Start an upload session for uploading a file in chunks.

        Args:
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            Upload session information including the session ID.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @post(
        "service-groups/Default/upload-sessions/append",
        args=[
            Query(name="sessionId"),
            Query(name="chunk"),
            Part(name="file"),
            Query(name="close"),
        ],
    )
    @response_handler(lambda response: None)
    @retryable_multipart_request()
    def append_to_upload_session(
        self,
        session_id: str,
        chunk_index: int,
        chunk: BinaryIO,
        close: bool = False,
    ) -> None:
        """Append a chunk to an upload session.

        The chunk needs to be 10485760 bytes (10 MB), unless the close parameter is true,
        which means that it is the last chunk of the file content. The chunks can be uploaded
        concurrently, as long as all chunk uploads are completed before finalizing.

        Args:
            session_id: The id of the upload session.
            chunk_index: The 1-based index of the chunk to be uploaded.
            file: The chunk data to upload.
            close: Set the current chunk as the last chunk to be uploaded. Defaults to False.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """

    @response_handler(_file_uri_response_handler)
    @post(
        "service-groups/Default/upload-sessions/finish",
        args=[Query(name="sessionId"), Field(name="name"), Field(name="properties")],
    )
    def finish_upload_session(
        self,
        session_id: str,
        name: str,
        properties: Dict[str, str],
    ) -> str:
        """Finish an upload session and make the file visible in SystemLink.

        This will trigger file events, such as routines.

        Args:
            session_id: The id of the upload session.
            name: The name of the file.
            properties: The properties of the file.

        Returns:
            ID of the uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/__init__.py sha256=900cd7f0da9a24c9ea8a7f78f51dbd575ba50da1ba4cc401381562a70276773d bytes=736 -->
## FILE: nisystemlink/clients/file/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/__init__.py`
- sha256: `900cd7f0da9a24c9ea8a7f78f51dbd575ba50da1ba4cc401381562a70276773d`
- bytes: 736

````python
from ._file_metadata import FileMetadata
from ._file_query_order_by import (
    FileQueryOrderBy,
    FileLinqQueryOrderBy,
    SearchFilesOrderBy,
)
from ._file_query_response import FileQueryResponse
from ._link import Link
from ._operations import V1Operations
from ._update_metadata import UpdateMetadataRequest
from ._file_linq_query import FileLinqQueryRequest, FileLinqQueryResponse
from ._search_files_request import SearchFilesRequest
from ._search_files_response import SearchFilesResponse
from ._base_file_response import BaseFileResponse, TotalCount, TotalCountRelation
from ._base_file_request import BaseFileRequest
from ._upload_session_start_response import UploadSessionStartResponse

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_base_file_request.py sha256=92d599f3bfbbf64c3588306f4baad740f9bfb46d3147554b8e9d4da8f15a8981 bytes=496 -->
## FILE: nisystemlink/clients/file/models/_base_file_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_base_file_request.py`
- sha256: `92d599f3bfbbf64c3588306f4baad740f9bfb46d3147554b8e9d4da8f15a8981`
- bytes: 496

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class BaseFileRequest(JsonModel):
    """Base class for file request models containing common query parameters."""

    skip: int | None = None
    """
    How many files to skip in the result when paging.
    """

    take: int | None = None
    """
    How many files to return in the result.
    """

    order_by_descending: bool | None = False
    """
    Whether to sort in descending order.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_base_file_response.py sha256=38388525000bda497a59872de64175f1d33b2b09cba348426d9996db0eeb302f bytes=1389 -->
## FILE: nisystemlink/clients/file/models/_base_file_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_base_file_response.py`
- sha256: `38388525000bda497a59872de64175f1d33b2b09cba348426d9996db0eeb302f`
- bytes: 1389

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._file_metadata import LinqQueryFileMetadata


class TotalCountRelation(str, Enum):
    """Describes the relation the returned total count value has with respect to the total number of files."""

    EQUALS = "eq"
    """Equals, meaning that the returned items are all the items that matched the filter."""

    GREATER_THAN_OR_EQUAL = "gte"
    """Greater or equal, meaning that the take limit has been hit, but there are further items that match the query."""


class TotalCount(JsonModel):
    """The total number of files that match the query regardless of skip and take values"""

    relation: TotalCountRelation
    """
    Describes the relation the returned total count value has with respect to the total number of
    files matched by the query.
    """

    value: int
    """Describes the number of files that were returned as a result of the query in the database"""


class BaseFileResponse(JsonModel):
    """Base class for file response models containing a list of files and total count."""

    available_files: List[LinqQueryFileMetadata]
    """The list of files returned by the query"""

    total_count: TotalCount
    """The total number of files that match the query regardless of skip and take values"""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_linq_query.py sha256=c7fe40ac04cf41b3dd04ba4b50ff253c77af3554ffd0e4e9d44d0b66c9bc540b bytes=1020 -->
## FILE: nisystemlink/clients/file/models/_file_linq_query.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_file_linq_query.py`
- sha256: `c7fe40ac04cf41b3dd04ba4b50ff253c77af3554ffd0e4e9d44d0b66c9bc540b`
- bytes: 1020

````python
from nisystemlink.clients.file.models._base_file_request import BaseFileRequest
from nisystemlink.clients.file.models._base_file_response import BaseFileResponse
from nisystemlink.clients.file.models._file_query_order_by import FileLinqQueryOrderBy


class FileLinqQueryRequest(BaseFileRequest):
    """Request model for LINQ query operations."""

    filter: str | None = None
    """
    The filter criteria for files. Consists of a string of queries composed using AND/OR operators.
    String values and date strings need to be enclosed in double quotes. Parentheses can be used
    around filters to better define the order of operations.
    Example Filter syntax: '[property name][operator][operand] and [property name][operator][operand]'
    """

    order_by: FileLinqQueryOrderBy | None = None
    """
    The property by which to order the files in the response.
    """


class FileLinqQueryResponse(BaseFileResponse):
    """Response model for LINQ query operations."""

    pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_metadata.py sha256=2d7c7aa68fb687f7602cefcda6d24824120e61297bb2406c0c3902b6d40bd7df bytes=2714 -->
## FILE: nisystemlink/clients/file/models/_file_metadata.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_file_metadata.py`
- sha256: `2d7c7aa68fb687f7602cefcda6d24824120e61297bb2406c0c3902b6d40bd7df`
- bytes: 2714

````python
from datetime import datetime
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field

from ._link import Link


class BaseFileMetadata(JsonModel):
    """Base class for file metadata."""

    created: datetime | None = None
    """
    The date and time the file was created in the file service.

    example :2018-05-15T18:54:27.519Z
    """

    id: str | None = None
    """
    The file's ID within the service group.

    example: "5afb2ce3741fe11d88838cc9"
    """

    properties: Dict[str, str] | None = None
    """
    The file's properties
    Example - {"Name": "myfile.txt", "MyProperty": "Value"}
    """

    service_group: str | None = None
    """
    The service group that owns the file
    """

    size: int | None = None
    """
    The 32-bit file size in bytes. If the value is larger than a 32-bit integer,
    this value is -1 and the size64 parameter contains the correct value.
    """

    size64: int | None = None
    """
    The 64-bit file size in bytes
    """

    workspace: str | None = None
    """
    The workspace the file belongs to
    """


class FileMetadata(BaseFileMetadata):
    """Metadata for a file."""

    field_links: Dict[str, Link] | None = Field(
        None,
        validation_alias=AliasChoices("field_links", "_links"),
        serialization_alias="_links",
    )
    """
    The links to access and manipulate the file:
    - data: Link to download the file using a GET request
    - delete: Link to delete the file using a DELETE request
    - self: Link to the file's metadata
    - updateMetadata: Link to update the file's metadata using a POST request
    """

    path: str | None = None
    """
    The path to the file on the server.  This field is returned only if
    the user has associated privileges to view file paths.

    example: C:\temp\4afb2ce3741fe11d88838cc9.txt
    """

    meta_data_revision: int | None = None
    """
    The file's properties revision number. When a file is uploaded, the revision number starts at 1.
    Every time metadata is updated, the revision number is incremented by 1.
    """

    last_updated_timestamp: datetime | None = None
    """
    The date and time the file was last updated in the file service.

    example: 2018-05-15T18:54:27.519Z
    """


class LinqQueryFileMetadata(BaseFileMetadata):
    """Metadata for a file returned by a LINQ query."""

    updated: datetime | None = None
    """
    The date and time the file was last updated in the file service.

    example :2018-05-15T18:54:27.519Z
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_query_order_by.py sha256=1082ee885d71156da8a1f3851397ffe04fe395c0f658716f8e6c6e50b8a0d9ab bytes=787 -->
## FILE: nisystemlink/clients/file/models/_file_query_order_by.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_file_query_order_by.py`
- sha256: `1082ee885d71156da8a1f3851397ffe04fe395c0f658716f8e6c6e50b8a0d9ab`
- bytes: 787

````python
from enum import Enum


class FileQueryOrderBy(Enum):
    """Order Files Query Response by Metadata for GET /files endpoint."""

    CREATED = "created"
    ID = "id"
    SIZE = "size"
    LAST_UPDATED_TIMESTAMP = "lastUpdatedTimestamp"


class FileLinqQueryOrderBy(str, Enum):
    """Order Files LINQ Query by Metadata for POST /query-files-linq endpoint."""

    NAME = "name"
    CREATED = "created"
    UPDATED = "updated"
    EXTENSION = "extension"
    SIZE = "size"
    WORKSPACE = "workspace"


class SearchFilesOrderBy(str, Enum):
    """Order Files Search by Metadata for POST /search-files endpoint."""

    NAME = "name"
    CREATED = "created"
    UPDATED = "updated"
    EXTENSION = "extension"
    SIZE = "size"
    WORKSPACE = "workspace"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_query_response.py sha256=053cff4b6201657ab7372df3840f4ed1175f62178b11ab2802a7a4bee88d5589 bytes=1159 -->
## FILE: nisystemlink/clients/file/models/_file_query_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_file_query_response.py`
- sha256: `053cff4b6201657ab7372df3840f4ed1175f62178b11ab2802a7a4bee88d5589`
- bytes: 1159

````python
from __future__ import annotations

from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field

from ._file_metadata import FileMetadata
from ._link import Link


class FileQueryResponse(JsonModel):
    """The result of a file query."""

    field_links: Dict[str, Link] = Field(
        validation_alias=AliasChoices("field_links", "_links"),
        serialization_alias="_links",
    )
    """The links that apply to the collection of files for a service group:
    - deleteFiles: Link to delete multiple files from the service group using a POST
    - query: Link to query for available files in the service group using a POST
    - search: Link to retrieve a filtered list of files in the service group using a GET
    - self: Link to the current service group
    - upload: Link to upload files to the service group using a POST
    """

    available_files: List[FileMetadata]
    """The list of files returned by the query"""

    total_count: int
    """The total number of files that match the query regardless of skip and take values"""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_link.py sha256=d8d766c30513b13b6075191882bd248760d00a63ca5d8628286ea53cbb9417b5 bytes=232 -->
## FILE: nisystemlink/clients/file/models/_link.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_link.py`
- sha256: `d8d766c30513b13b6075191882bd248760d00a63ca5d8628286ea53cbb9417b5`
- bytes: 232

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field


class Link(JsonModel):
    href: str = Field(..., examples=["/nifile/v1/service-groups"])
    """
    URI of the link
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_operations.py sha256=68746fc6e9a37213f76bcadfb0f2b4ff4c55f6d1f893e7e17e78dd392d20bb0e bytes=1066 -->
## FILE: nisystemlink/clients/file/models/_operations.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_operations.py`
- sha256: `68746fc6e9a37213f76bcadfb0f2b4ff4c55f6d1f893e7e17e78dd392d20bb0e`
- bytes: 1066

````python
from nisystemlink.clients.core._api_info import Operation
from nisystemlink.clients.core._uplink._json_model import JsonModel


class Operations(JsonModel):
    delete_files: Operation | None = None
    download_data: Operation | None = None
    list_files: Operation | None = None
    query_files: Operation | None = None
    search_files: Operation | None = None
    update_metadata: Operation | None = None
    upload_files: Operation | None = None


class V1Operations(JsonModel):
    operations: Operations | None = None
    """
    Available operations in the v1 version of the API:
    - deleteFiles: The ability to delete uploaded files
    - downloadData: The ability to download file data
    - listFiles: The ability to list available files and service groups
    - queryFiles: The ability to query available files and service groups
    - searchFiles: The ability to search for files using Elasticsearch
    - updateMetadata: The ability to update file metadata properties
    - uploadFiles: The ability to upload files
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_search_files_request.py sha256=bcc95f38aab2c93b00343308ec2d2b8bf73cde1747259c8dc8e91ae5c6eaf8b3 bytes=816 -->
## FILE: nisystemlink/clients/file/models/_search_files_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_search_files_request.py`
- sha256: `bcc95f38aab2c93b00343308ec2d2b8bf73cde1747259c8dc8e91ae5c6eaf8b3`
- bytes: 816

````python
from nisystemlink.clients.file.models._base_file_request import BaseFileRequest
from nisystemlink.clients.file.models._file_query_order_by import SearchFilesOrderBy


class SearchFilesRequest(BaseFileRequest):
    """Request model for searching files."""

    filter: str | None = None
    """
    The filter criteria for files using Lucene query syntax. Consists of a string of queries composed
    using AND/OR operators. String values and date strings need to be enclosed in double quotes.
    Parentheses can be used around filters to better define the order of operations.
    Example Filter syntax: '[property name]:[operand] AND [property name]:[operand]'
    """

    order_by: SearchFilesOrderBy | None = None
    """
    The property by which to order the files in the response.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_search_files_response.py sha256=175feed0f36e4e42db5fa48aeaddad8575a38b0684c7469794f6e611dbf23df5 bytes=167 -->
## FILE: nisystemlink/clients/file/models/_search_files_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_search_files_response.py`
- sha256: `175feed0f36e4e42db5fa48aeaddad8575a38b0684c7469794f6e611dbf23df5`
- bytes: 167

````python
from ._base_file_response import BaseFileResponse


class SearchFilesResponse(BaseFileResponse):
    """Response model for search files operation."""

    pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_update_metadata.py sha256=3e821ac26113f1379759d02db36aa0fade935c2df75b2e6e98e8f220bf1cbe0a bytes=1129 -->
## FILE: nisystemlink/clients/file/models/_update_metadata.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_update_metadata.py`
- sha256: `3e821ac26113f1379759d02db36aa0fade935c2df75b2e6e98e8f220bf1cbe0a`
- bytes: 1129

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel


class UpdateMetadataRequest(JsonModel):
    """The file's metadata and options for updating it."""

    replace_existing: bool
    """Determines whether the current list should be entirely replaced by the specified list
        or merged with the existing list."""

    expected_revision: int | None = None
    """When specified, this is an integer that should be set to match the last known revision number of the metadata.
    If it doesn't match at the time of execution, the update request will be rejected.
    This is used to ensure that changes to this file metadata are correctly using the previous state."""

    properties: Dict[str, str]
    """The properties to set. A map of key value properties containing the metadata to be attached.

        Predefined:
            Name: This is an optional property for renaming the file. When specified, the file will be renamed."""

    workspace: str | None = None
    """When specified, the workspace of the metadata will be updated to the new value."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_upload_session_start_response.py sha256=e866abbdfbafbc84fca4c74d0d7d2771779737321e722dbb1420119b9f48ee9c bytes=549 -->
## FILE: nisystemlink/clients/file/models/_upload_session_start_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/models/_upload_session_start_response.py`
- sha256: `e866abbdfbafbc84fca4c74d0d7d2771779737321e722dbb1420119b9f48ee9c`
- bytes: 549

````python
from datetime import datetime

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field


class UploadSessionStartResponse(JsonModel):
    """Response model for starting an upload session."""

    session_id: str = Field(
        validation_alias=AliasChoices("session_id", "id"),
        serialization_alias="id",
    )
    """
    The id created for the upload session.
    """

    created_at: datetime
    """
    The date and time the upload session has started.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/file/utilities.py sha256=84c93b09e0659139c6d53424d39c708a764859e5ff6dd8b4ad4a449b47da06f8 bytes=649 -->
## FILE: nisystemlink/clients/file/utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/file/utilities.py`
- sha256: `84c93b09e0659139c6d53424d39c708a764859e5ff6dd8b4ad4a449b47da06f8`
- bytes: 649

````python
"""Utilities for FileClient."""

from nisystemlink.clients.file import FileClient
from nisystemlink.clients.file.models import UpdateMetadataRequest


def rename_file(client: FileClient, file_id: str, name: str) -> None:
    """Rename a file identified by `file_id` to `name`.

    Args:
        client: The FileClient to use for the rename.
        file_id: ID of file to rename.
        name: New name for the File.
    """
    new_metadata = {"Name": name}
    rename_request = UpdateMetadataRequest(
        replace_existing=False, properties=new_metadata
    )
    client.update_metadata(metadata=rename_request, id=file_id)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/__init__.py sha256=57f3c1dc1c68fe9f2bdd72ebac78af65fb08023847226542ed6a31f7cfb754d6 bytes=143 -->
## FILE: nisystemlink/clients/notebook/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/__init__.py`
- sha256: `57f3c1dc1c68fe9f2bdd72ebac78af65fb08023847226542ed6a31f7cfb754d6`
- bytes: 143

````python
"""Start here with NotebookClient for notebook management."""

from ._notebook_client import NotebookClient

__all__ = ["NotebookClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/_notebook_client.py sha256=4ce3f71eb3b5ed2821ae7482bd346c4829ccb45ae069f24aea19b7365b2374dc bytes=11164 -->
## FILE: nisystemlink/clients/notebook/_notebook_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/_notebook_client.py`
- sha256: `4ce3f71eb3b5ed2821ae7482bd346c4829ccb45ae069f24aea19b7365b2374dc`
- bytes: 11164

````python
import io
from typing import BinaryIO, List

from nisystemlink.clients import core
from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._file_like_response import (
    file_like_response_handler,
)
from nisystemlink.clients.core._uplink._methods import (
    delete,
    get,
    post,
    put,
    response_handler,
)
from nisystemlink.clients.core._uplink._multipart_retry import (
    retryable_multipart_request,
)
from nisystemlink.clients.core.helpers._iterator_file_like import IteratorFileLike
from uplink import Part, Path, retry

from . import models


@retry(when=retry.when.status(429), stop=retry.stop.after_attempt(5))
class NotebookClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Notebook Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()
        super().__init__(configuration, base_path="/")

    @get("ninotebook/v1/notebook/{id}")
    def get_notebook(self, id: str) -> models.NotebookMetadata:
        """Gets a notebook metadata by ID.

        Args:
            id: The ID of the notebook to read.

        Returns:
            The notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    @retryable_multipart_request()
    @put(
        "ninotebook/v1/notebook/{id}",
        args=[Path("id"), Part("metadata"), Part("content")],
    )
    def __update_notebook(
        self,
        id: str,
        metadata: io.BytesIO | None = None,
        content: BinaryIO | None = None,
    ) -> models.NotebookMetadata:
        """Updates a notebook metadata by ID.

        Args:
            id: The ID of the notebook to update.
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The updated notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    def update_notebook(
        self,
        id: str,
        metadata: models.NotebookMetadata | None = None,
        content: BinaryIO | None = None,
    ) -> models.NotebookMetadata:
        """Updates a notebook metadata by ID.

        Args:
            id: The ID of the notebook to update.
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The updated notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        metadata_io = None
        if metadata is not None:
            metadata_str = metadata.model_dump_json(by_alias=True, exclude_unset=True)
            metadata_io = io.BytesIO(metadata_str.encode("utf-8"))

        return self.__update_notebook(
            id=id,
            metadata=metadata_io,
            content=content,
        )

    @delete("ninotebook/v1/notebook/{id}")
    def delete_notebook(self, id: str) -> None:
        """Deletes a notebook by ID.

        Args:
            id: The ID of the notebook to delete.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    @retryable_multipart_request()
    @post(
        "ninotebook/v1/notebook",
        args=[Part("metadata"), Part("content")],
    )
    def __create_notebook(
        self,
        metadata: io.BytesIO,
        content: BinaryIO,
    ) -> models.NotebookMetadata:
        """Creates a new notebook.

        Args:
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The created notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    def create_notebook(
        self,
        metadata: models.NotebookMetadata,
        content: BinaryIO,
    ) -> models.NotebookMetadata:
        """Creates a new notebook.

        Args:
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The created notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        metadata_str = metadata.model_dump_json()

        metadata_io = io.BytesIO(metadata_str.encode("utf-8"))
        return self.__create_notebook(
            metadata=metadata_io,
            content=content,
        )

    @post("ninotebook/v1/notebook/query")
    def query_notebooks(
        self, query: models.QueryNotebookRequest
    ) -> models.PagedNotebooks:
        """Queries notebooks.

        Args:
            query: The query parameters.

        Returns:
            The paged notebooks.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    @response_handler(file_like_response_handler)
    @get("ninotebook/v1/notebook/{id}/content")
    def get_notebook_content(self, id: str) -> IteratorFileLike:
        """Gets a notebook content by ID.

        Args:
            id: The ID of the notebook to read.

        Returns:
            A file-like object for reading the notebook content.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        """
        ...

    @post("ninbexecution/v1/executions")
    def create_executions(
        self, executions: List[models.CreateExecutionRequest]
    ) -> models.CreateExecutionsResponse:
        """Create one or more executions of Jupyter notebooks.

        Args:
            execution: information about an execution of a Jupyter notebook.

        Returns:
            A response to a request to create executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...

    @get("ninbexecution/v1/executions/{id}")
    def get_execution_by_id(self, id: str) -> models.Execution:
        """Get information about the specified execution of a Jupyter notebook.

        Args:
            id: the ID of the execution.

        Returns:
            Information about the execution of a Jupyter notebook fetched using it's Id.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...

    @post("ninbexecution/v1/query-executions")
    def __query_executions(
        self, query: models._QueryExecutionsRequest
    ) -> List[models.Execution]:
        """Query executions of Jupyter notebooks.

        Args:
            query: query for executions of Jupyter notebooks.

        Returns:
            A response to a request to query executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...

    def query_executions(
        self, query: models.QueryExecutionsRequest
    ) -> List[models.Execution]:
        """Query executions of Jupyter notebooks.

        Args:
            query: query for executions of Jupyter notebooks.

        Returns:
            A response to a request to query executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        projection = ",".join(query.projection)
        projection_str = f"new({projection})" if projection else None

        query_params = {
            "filter": query.filter,
            "order_by": query.order_by,
            "descending": query.descending,
            "projection": projection_str,
        }

        query_params = {k: v for k, v in query_params.items() if v is not None}

        query_request = models._QueryExecutionsRequest(**query_params)  # type: ignore

        return self.__query_executions(query=query_request)

    @post("ninbexecution/v1/retry-executions", return_key="error")
    def retry_executions(self, ids: List[str]) -> ApiError | None:
        """Retries existing executions based on failed, canceled or timed-out executions.

        Args:
            ids: List of execution IDs to retry.

        Returns:
            An ApiError object if executions could not be retried.
            None if executions were retried successfully.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...

    @post("ninbexecution/v1/cancel-executions", return_key="error")
    def cancel_executions(self, ids: List[str]) -> ApiError | None:
        """Cancel queued and in-progress executions.

        Args:
            ids: List of execution IDs to cancel.

        Returns:
            An ApiError object if executions could not be canceled.
            None if executions were canceled successfully.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...

    @post("ninbexecution/v1/create-executions-from-existing")
    def create_executions_from_existing(
        self, ids: List[str]
    ) -> models.CreateExecutionsResponse:
        """Create new executions based on already existing succeeded executions.

        Args:
            ids: List of execution IDs to run again.

        Returns:
            A response to a request to create executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/__init__.py sha256=759cc5389765546386f6d1229cc39bd31b3de1ee72dd883a4e7c08a1e6bc2003 bytes=707 -->
## FILE: nisystemlink/clients/notebook/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/__init__.py`
- sha256: `759cc5389765546386f6d1229cc39bd31b3de1ee72dd883a4e7c08a1e6bc2003`
- bytes: 707

````python
from ._notebook_metadata import NotebookMetadata
from ._query_notebook_request import QueryNotebookRequest
from ._query_notebook_response import PagedNotebooks
from ._query_execution_request import (
    ExecutionField,
    ExecutionSortField,
    _QueryExecutionsRequest,
    QueryExecutionsRequest,
)
from ._create_execution_request import (
    CreateExecutionRequest,
)
from ._create_execution_response import (
    CreatedExecution,
    CreateExecutionsResponse,
)
from ._execution import (
    Execution,
    SourceType,
    ReportType,
    ReportSettings,
    ExecutionPriority,
    ExecutionResourceProfile,
    ExecutionStatus,
    ExecutionErrorCode,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_create_execution_request.py sha256=c260ab53152425a86595c1eb84c2aba7cbbb0e2323b6bf85125d1fb3fbb42a1d bytes=2088 -->
## FILE: nisystemlink/clients/notebook/models/_create_execution_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_create_execution_request.py`
- sha256: `c260ab53152425a86595c1eb84c2aba7cbbb0e2323b6bf85125d1fb3fbb42a1d`
- bytes: 2088

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field

from ._execution import (
    ExecutionPriority,
    ExecutionResourceProfile,
    ReportSettings,
)


class CreateExecutionRequest(JsonModel):
    """Creation information about an execution of a Jupyter notebook."""

    notebook_id: str = Field(..., min_length=1)
    """The ID of the notebook to execute."""

    parameters: Dict[str, str | None] | None = None
    """The input parameters for this execution of the notebook. The keys are strings and the values can be of any
    valid JSON type."""

    workspace_id: str = Field(..., min_length=1)
    """The ID of the workspace this execution belongs to."""

    timeout: int | None = None
    """The number of seconds the execution runs before it aborts if uncompleted. The timer starts once status
    is IN_PROGRESS. 0 means infinite."""

    result_cache_period: int | None = None
    """The period of time, in seconds, when the result of a previous notebook execution can be used as the
    result of the current notebook execution. Results will only be reused if the notebook and input parameters match.
    A value of 0 means do not reuse results from any previous executions. A value of -1 means always reuse results if
    possible and return an error if not possible. This prevents actual execution of a notebook."""

    report_settings: ReportSettings | None = None
    """Settings of the Report"""

    client_requests_id: str | None = None
    """The client request ID unique for each execution to be created. This is provided by the caller to be able
    to track executions that could not be created. The error response will contain this in the resourceId field.
    If not provided, the notebookId is used as the resourceId."""

    priority: ExecutionPriority | None = None
    """Execution priority. Can be one of Low, Medium or High."""

    resource_profile: ExecutionResourceProfile | None = None
    """Resource profile of the execution."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_create_execution_response.py sha256=bc3e3d9ed3e5b40485c55d04f04c32ddbe703eab50c7ad89cb8e5aaf3d708fdc bytes=657 -->
## FILE: nisystemlink/clients/notebook/models/_create_execution_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_create_execution_response.py`
- sha256: `bc3e3d9ed3e5b40485c55d04f04c32ddbe703eab50c7ad89cb8e5aaf3d708fdc`
- bytes: 657

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._execution import Execution


class CreatedExecution(Execution):
    cached_result: bool
    """Returns true if the execution is returned from cache"""


class CreateExecutionsResponse(JsonModel):
    """Model for response to a request to create an execution."""

    error: ApiError | None = None
    """The error that occurred during the request, if any."""

    executions: List[CreatedExecution] | None = None
    """Gets or sets the collection of authorized executions."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_execution.py sha256=73f48b243c19be5df73666f55d0e8ff6bae13d71f5f3e9fb0597096535610fdc bytes=5055 -->
## FILE: nisystemlink/clients/notebook/models/_execution.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_execution.py`
- sha256: `73f48b243c19be5df73666f55d0e8ff6bae13d71f5f3e9fb0597096535610fdc`
- bytes: 5055

````python
from datetime import datetime
from enum import Enum
from typing import Any, Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field


class SourceType(str, Enum):
    """Source type of an execution."""

    MANUAL = "MANUAL"

    TRIGGERED = "TRIGGERED"


class Source(JsonModel):
    """An object that defines properties set by routine service."""

    type: SourceType
    """Source type of an execution"""

    routine_id: str | None = None
    """ID of the routine that triggered the execution"""

    event_id: str | None = None
    """Unique identifier of event that triggered the execution"""


class ReportType(str, Enum):
    """Available types for a report that is going to be generated."""

    NO_REPORT = "NO_REPORT"

    HTML = "HTML"

    PDF = "PDF"


class ReportSettings(JsonModel):
    """A class that defines settings of the Report."""

    format: ReportType
    """Type for the report that is going to be generated."""

    exclude_code: bool
    """Whether the source code should be included in the report."""


class ExecutionPriority(str, Enum):
    """Execution priority. Can be one of Low, Medium or High."""

    LOW = "LOW"

    MEDIUM = "MEDIUM"

    HIGH = "HIGH"


class ExecutionResourceProfile(str, Enum):
    """Resource profile of the execution. Can be one of Low, Medium, High or Default."""

    DEFAULT = "DEFAULT"

    LOW = "LOW"

    MEDIUM = "MEDIUM"

    HIGH = "HIGH"


class ExecutionStatus(str, Enum):
    """Status of an execution."""

    IN_PROGRESS = "IN_PROGRESS"

    QUEUED = "QUEUED"

    FAILED = "FAILED"

    SUCCEEDED = "SUCCEEDED"

    CANCELED = "CANCELED"

    TIMED_OUT = "TIMED_OUT"


class ExecutionErrorCode(str, Enum):
    """Execution error code."""

    NO_ERROR = "NO_ERROR"

    NOTEBOOK_ERROR = "NOTEBOOK_ERROR"

    NOTEBOOK_TIMEOUT_ERROR = "NOTEBOOK_TIMEOUT_ERROR"

    NOTEBOOK_NOT_FOUND_ERROR = "NOTEBOOK_NOT_FOUND_ERROR"

    NOTEBOOK_RESULT_TOO_BIG_ERROR = "NOTEBOOK_RESULT_TOO_BIG_ERROR"

    NOT_PUBLISHED_ERROR = "NOT_PUBLISHED_ERROR"

    OUT_OF_MEMORY_ERROR = "OUT_OF_MEMORY_ERROR"

    UNKNOWN_ERROR = "UNKNOWN_ERROR"

    DEAD_KERNEL_ERROR = "DEAD_KERNEL_ERROR"

    EXECUTION_COULD_NOT_BE_RETRIED = "EXECUTION_COULD_NOT_BE_RETRIED"


class Execution(JsonModel):
    """Jupyter notebook execution information.

    Includes the cachedResult field.
    """

    id: str | None = None
    """The ID of the execution."""

    notebook_id: str | None = None
    """The ID of the executed notebook."""

    organization_id: str | None = Field(
        None,
        validation_alias=AliasChoices("organization_id", "orgId"),
        serialization_alias="orgId",
    )
    """The org ID of the user creating the request."""

    user_id: str | None = None
    """The user ID of the user creating the request."""

    parameters: Dict[str, Any] | None = None
    """The input parameters for this execution.

    The keys are strings and the values can be any valid JSON type.
    """

    workspace_id: str | None = None
    """The ID of the workspace this execution belongs to."""

    timeout: int | None = None
    """The number of seconds the execution runs before it aborts.

    The timer starts once status is IN_PROGRESS. 0 means infinite.
    """

    status: ExecutionStatus | None = None
    """Status of an execution."""

    queued_at: datetime | None = None
    """Timestamp of when the notebook execution was queued."""

    started_at: datetime | None = None
    """Timestamp of when the notebook execution was started."""

    completed_at: datetime | None = None
    """Timestamp of when the notebook execution was completed."""

    last_updated_timestamp: datetime | None = None
    """Timestamp of when the notebook execution was last updated."""

    last_updated_by: str | None = None
    """"The user ID of the user who last updated the execution."""

    retry_count: int | None = None
    """The number of manually retried attempts of the notebook execution."""

    exception: str | None = None
    """Exception that occured during the execution. This is used only when status is FAILED."""

    error_code: ExecutionErrorCode | None = None
    """Execution error code."""

    report_id: str | None = None
    """The ID of the report this execution generates."""

    report_settings: ReportSettings | None = None
    """Settings of the Report"""

    result: Dict[str, object | None] | None = None
    """Result of the execution. This is used only when status is SUCCEEDED."""

    source: Source | None = None
    """An object that defines properties set by routine service"""

    priority: ExecutionPriority | None = None
    """Execution priority. Can be one of Low, Medium or High."""

    resource_profile: ExecutionResourceProfile | None = None
    """Resource profile of the execution."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_notebook_metadata.py sha256=958b224de91026be78c5e6984ba283d0773d9bca500d8282059a011198174aa5 bytes=1117 -->
## FILE: nisystemlink/clients/notebook/models/_notebook_metadata.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_notebook_metadata.py`
- sha256: `958b224de91026be78c5e6984ba283d0773d9bca500d8282059a011198174aa5`
- bytes: 1117

````python
from datetime import datetime
from typing import Any, Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel


class NotebookMetadata(JsonModel):
    """Metadata for a notebook."""

    id: str | None = None
    """The ID of the notebook."""

    name: str | None = None
    """The name of the notebook."""

    workspace: str | None = None
    """The Id of the workspace containing the notebook."""

    created_by: str | None = None
    """The Id of the user that created the notebook."""

    updated_by: str | None = None
    """The Id of the user that last updated the notebook."""

    created_at: datetime | None = None
    """The created timestamp (ISO8601 format)."""

    updated_at: datetime | None = None
    """The last updated timestamp (ISO8601 format)."""

    properties: Dict[str, str] | None = None
    """A map of key value properties associated with the notebook."""

    metadata: Dict[str, Any] | None = None
    """The metadata of the notebook."""

    parameters: Dict[str, Any] | None = None
    """The parameters of the notebook."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_execution_request.py sha256=aa448d72c5e3c39c70c8588dde7b59db3601db8dd1f850df6e8b9d441192dbd3 bytes=2136 -->
## FILE: nisystemlink/clients/notebook/models/_query_execution_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_query_execution_request.py`
- sha256: `aa448d72c5e3c39c70c8588dde7b59db3601db8dd1f850df6e8b9d441192dbd3`
- bytes: 2136

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class ExecutionSortField(str, Enum):
    """Possible fields used to sort executions."""

    NOTEBOOK_ID = "NOTEBOOK_ID"

    EXECUTION_HASH = "EXECUTION_HASH"

    TIMEOUT = "TIMEOUT"

    QUEUED_AT = "QUEUED_AT"

    STARTED_AT = "STARTED_AT"

    COMPLETED_AT = "COMPLETED_AT"

    STATUS = "STATUS"


class ExecutionField(str, Enum):
    """Possible fields in executions."""

    ID = "id"

    NOTEBOOK_ID = "notebookId"

    ORGANIZATION_ID = "orgId"

    USER_ID = "userId"

    PARAMETERS = "parameters"

    WORKSPACE_ID = "workspaceId"

    TIMEOUT = "timeout"

    STATUS = "status"

    QUEUED_AT = "queuedAt"

    STARTED_AT = "startedAt"

    COMPLETED_AT = "completedAt"

    LAST_UPDATED_AT = "lastUpdatedTimestamp"

    EXCEPTION = "exception"

    ERROR_CODE = "errorCode"

    REPORT_ID = "reportId"

    REPORT_SETTINGS = "reportSettings"

    RESULT = "result"

    SOURCE = "source"

    PRIORITY = "priority"

    RESOURCE_PROFILE = "resourceProfile"


class QueryExecutionsRequest(JsonModel):
    """Query for executions of Jupyter notebooks."""

    filter: str | None = None
    """The query filter in Dynamic LINQ."""

    order_by: ExecutionSortField | None = None
    """Possible fields used to sort executions."""

    descending: bool = False
    """Whether to return the executions in descending order."""

    projection: List[ExecutionField] = []
    """The projection to be applied for the items in the provider."""


class _QueryExecutionsRequest(JsonModel):
    """Query for executions of Jupyter notebooks."""

    filter: str | None = None
    """The query filter in Dynamic LINQ."""

    order_by: ExecutionSortField | None = None
    """Possible fields used to sort executions."""

    descending: bool = False
    """Whether to return the executions in descending order."""

    projection: str | None = None
    """The projection to be applied for the items in the provider."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_notebook_request.py sha256=f6f389f002434a75be634b6b4394c1f8451f7455c2b907e0e8d6eff5c280a818 bytes=1812 -->
## FILE: nisystemlink/clients/notebook/models/_query_notebook_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_query_notebook_request.py`
- sha256: `f6f389f002434a75be634b6b4394c1f8451f7455c2b907e0e8d6eff5c280a818`
- bytes: 1812

````python
from nisystemlink.clients.core._uplink._with_paging import WithPaging


class QueryNotebookRequest(WithPaging):
    """Model for a query notebooks request."""

    filter: str | None = None
    """
    The filter criteria for notebook, consisting of a string of queries composed using AND/OR operators.
    String values need to be enclosed in double quotes. Parenthesis can be used within the filter
    to better define the order of operations.
    Filter syntax: '[property name][operator][operand] and [property name][operator][operand]' Operators:

      Equals operator '='. Example: 'x = y'
      Not equal operator '!='. Example: 'x != y'
      Greater than operator '>'. Example: 'x > y'
      Greater than or equal operator '>='. Example: 'x >= y'
      Less than operator '<'. Example: 'x < y'
      Less than or equal operator '<='. Example: 'x <= y'
      Logical AND operator 'and'. Example: 'x and y'
      Logical OR operator 'or'. Example: 'x or y'
      Starts with operator '.StartsWith()', used to check whether a string starts with another string.
      Example: 'x.StartsWith(y)'
      Does not start with operator '!.StartsWith()', used to check whether a string does not start with another string.
      Example: '!x.StartsWith(y)'
      String null or empty 'string.IsNullOrEmpty()', used to check whether a string is null or empty.
      Example: 'string.IsNullOrEmpty(x)'
      String is not null or empty '!string.IsNullOrEmpty()', used to check whether a string is not null or empty.
      Example: '!string.IsNullOrEmpty(x)'
        Valid notebook properties that can be used in the filter:
      id
      name
      properties.interface
      workspace
    """

    take: int | None = None
    """The maximum number of notebooks to return."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_notebook_response.py sha256=b50d56d0ac43003bcb3f2cfb811872e643d32f466095275264fe64124d244e8c bytes=327 -->
## FILE: nisystemlink/clients/notebook/models/_query_notebook_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notebook/models/_query_notebook_response.py`
- sha256: `b50d56d0ac43003bcb3f2cfb811872e643d32f466095275264fe64124d244e8c`
- bytes: 327

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._notebook_metadata import NotebookMetadata


class PagedNotebooks(WithPaging):
    """Model for a query notebooks response."""

    notebooks: List[NotebookMetadata] | None = None
    """The list of notebooks."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/__init__.py sha256=813554a0845bb67c68d379d724d02a09b6be617446f21b2a4ea508c1fa6b4408 bytes=163 -->
## FILE: nisystemlink/clients/notification/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/__init__.py`
- sha256: `813554a0845bb67c68d379d724d02a09b6be617446f21b2a4ea508c1fa6b4408`
- bytes: 163

````python
"""Start here with NotificationClient for notification management."""

from ._notification_client import NotificationClient

__all__ = ["NotificationClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/_notification_client.py sha256=bd717a036d7cc7fc5abd4d0b4247f0f27e427034bbb0ee7ab8b2995095455413 bytes=1743 -->
## FILE: nisystemlink/clients/notification/_notification_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/_notification_client.py`
- sha256: `bd717a036d7cc7fc5abd4d0b4247f0f27e427034bbb0ee7ab8b2995095455413`
- bytes: 1743

````python
"""Implementation of Notification Client"""

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import post
from uplink import retry

from . import models


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(1),
    on_exception=retry.CONNECTION_ERROR,
)
class NotificationClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the `/ninotification` service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/ninotification/v1/")

    @post("apply-dynamic-strategy")
    def apply_dynamic_notification_strategy(
        self, request: models.DynamicStrategyRequest
    ) -> None:
        """Applies the notification strategy from the given request.

        Args:
            request: Request with message template substitution fields and notification strategies.

        Returns:
            None.

        Raises:
            ApiException: if unable to communicate with the `/ninotification` service or provided invalid arguments.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/__init__.py sha256=e1ef7daa2cd671f3b9843627fe9d39acd128a4944e8f3e6ed55e28289b76ea7b bytes=481 -->
## FILE: nisystemlink/clients/notification/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/__init__.py`
- sha256: `e1ef7daa2cd671f3b9843627fe9d39acd128a4944e8f3e6ed55e28289b76ea7b`
- bytes: 481

````python
from ._address_group import AddressGroup
from ._dynamic_strategy_request import DynamicStrategyRequest
from ._message_template import MessageTemplate
from ._dynamic_notification_configuration import DynamicNotificationConfiguration
from ._dynamic_notification_strategy import DynamicNotificationStrategy
from ._smtp_address_group import SmtpAddressFields, SmtpAddressGroup
from ._smtp_message_template import SmtpMessageTemplateFields, SmtpMessageTemplate

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_address_group.py sha256=a21e5ab725a22137d9530fa7170675b30b4087d2d41f573a1bc1ca7f7f2b2c8f bytes=415 -->
## FILE: nisystemlink/clients/notification/models/_address_group.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_address_group.py`
- sha256: `a21e5ab725a22137d9530fa7170675b30b4087d2d41f573a1bc1ca7f7f2b2c8f`
- bytes: 415

````python
from typing import Dict, List

from ._base_notification_metadata import BaseNotificationMetadata


class AddressGroup(BaseNotificationMetadata):
    """Model defining notification recipients for generic service."""

    interpreting_service_name: str
    """Name of the interpreting service."""

    fields: Dict[str, List[str]]
    """Address group's fields. Requires at least one valid recipient."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_base_notification_metadata.py sha256=811ba6c397262f9bc20e53ba14216eec5a004c7f610463e42491a5d2c46a1ce3 bytes=634 -->
## FILE: nisystemlink/clients/notification/models/_base_notification_metadata.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_base_notification_metadata.py`
- sha256: `811ba6c397262f9bc20e53ba14216eec5a004c7f610463e42491a5d2c46a1ce3`
- bytes: 634

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class BaseNotificationMetadata(JsonModel):
    id: str | None = None
    """Identifier of the notification metadata"""

    display_name: str | None = None
    """Display name of the object.

    Example: "name"
    """

    properties: Dict[str, str] | None = None
    """Additional properties for the base metadata.

    Example: { "property": "value" }
    """

    referencing_notification_strategies: List[str] | None = None
    """List of notification strategies referencing the notification metadata"""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_notification_configuration.py sha256=85098ecfd1813fb536a84314192db66a56316d3c03e9593e25a277930a9480b2 bytes=2040 -->
## FILE: nisystemlink/clients/notification/models/_dynamic_notification_configuration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_dynamic_notification_configuration.py`
- sha256: `85098ecfd1813fb536a84314192db66a56316d3c03e9593e25a277930a9480b2`
- bytes: 2040

````python
from __future__ import annotations

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.notification.models._address_group import AddressGroup
from nisystemlink.clients.notification.models._message_template import MessageTemplate
from nisystemlink.clients.notification.models._smtp_address_group import (
    SmtpAddressGroup,
)
from nisystemlink.clients.notification.models._smtp_message_template import (
    SmtpMessageTemplate,
)
from pydantic import Field, model_validator


class DynamicNotificationConfiguration(JsonModel):
    """Model for notification configuration defining address groups and message template for the notification.

    Requires at least one of addressGroupId or addressGroup, and one of messageTemplateId or messageTemplate.
    """

    address_group_id: str | None = None
    """ID referencing the associated address group."""

    message_template_id: str | None = None
    """ID referencing the associated message template."""

    address_group: AddressGroup | SmtpAddressGroup | None = Field(default=None)
    """Address group defining notification recipients."""

    message_template: MessageTemplate | SmtpMessageTemplate | None = Field(default=None)
    """Message template defining notification content structure"""

    @model_validator(mode="after")
    def validate_required_pairs(self) -> DynamicNotificationConfiguration:
        """Validator to check at least one of address_group_id or address_group, and
        one of message_template_id or message_template is present.
        """
        if self.address_group_id is None and self.address_group is None:
            raise ValueError(
                "One of either AddressGroupId or AddressGroup is required."
            )

        if self.message_template_id is None and self.message_template is None:
            raise ValueError(
                "One of either MessageTemplateId or MessageTemplate is required."
            )

        return self
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_notification_strategy.py sha256=3fe25602684c87c7ff3a178b052ca77d0f7e7a80e6a94d94c0275275c593cd3d bytes=528 -->
## FILE: nisystemlink/clients/notification/models/_dynamic_notification_strategy.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_dynamic_notification_strategy.py`
- sha256: `3fe25602684c87c7ff3a178b052ca77d0f7e7a80e6a94d94c0275275c593cd3d`
- bytes: 528

````python
from typing import Annotated, List


from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field

from ._dynamic_notification_configuration import DynamicNotificationConfiguration


class DynamicNotificationStrategy(JsonModel):
    """Model for the notification strategy to be applied."""

    notification_configurations: Annotated[
        List[DynamicNotificationConfiguration], Field(min_length=1)
    ]
    """Notification configurations associated with this strategy."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_strategy_request.py sha256=6e96178c1940caf8a88df0a3978d67589afd1d99efb02b3cc4dbc8161b055bc6 bytes=654 -->
## FILE: nisystemlink/clients/notification/models/_dynamic_strategy_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_dynamic_strategy_request.py`
- sha256: `6e96178c1940caf8a88df0a3978d67589afd1d99efb02b3cc4dbc8161b055bc6`
- bytes: 654

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dynamic_notification_strategy import DynamicNotificationStrategy


class DynamicStrategyRequest(JsonModel):
    """Request model for applying a dynamic notification strategy."""

    message_template_substitution_fields: Dict[str, str] | None = None
    """Defines the fields used for substituting values in the message template.

    Example: { "replacement": "value" }
    """

    notification_strategy: DynamicNotificationStrategy
    """Notification strategy containing configurations for address groups and message templates."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_message_template.py sha256=92f0fe5e9f491e910837e18e1a1129a3032bbe20dd400887d762db2a65c8b58f bytes=362 -->
## FILE: nisystemlink/clients/notification/models/_message_template.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_message_template.py`
- sha256: `92f0fe5e9f491e910837e18e1a1129a3032bbe20dd400887d762db2a65c8b58f`
- bytes: 362

````python
from typing import Dict

from ._base_notification_metadata import BaseNotificationMetadata


class MessageTemplate(BaseNotificationMetadata):
    """Model defining the notification content structure."""

    interpreting_service_name: str
    """Name of the interpreting service"""

    fields: Dict[str, str]
    """Template fields for message."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_smtp_address_group.py sha256=a3840214981be5e18d3a12195bb0ad5e8d176b5b207ea1aa8597813265a83c19 bytes=1617 -->
## FILE: nisystemlink/clients/notification/models/_smtp_address_group.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_smtp_address_group.py`
- sha256: `a3840214981be5e18d3a12195bb0ad5e8d176b5b207ea1aa8597813265a83c19`
- bytes: 1617

````python
from typing import List, Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.notification.models._base_notification_metadata import (
    BaseNotificationMetadata,
)
from pydantic import model_validator


class SmtpAddressFields(JsonModel):
    """Recipient address fields used in SMTP messaging."""

    to_addresses: List[str] | None = None
    """List of primary recipient addresses."""

    cc_addresses: List[str] | None = None
    """List of carbon copy recipient addresses."""

    bcc_addresses: List[str] | None = None
    """List of blind carbon copy recipient addresses."""


class SmtpAddressGroup(BaseNotificationMetadata):
    """Model defining notification recipients for SMTP service."""

    interpreting_service_name: Literal["smtp"] = "smtp"
    """Service name for SMTP-based interpretation."""

    fields: SmtpAddressFields
    """Recipient address fields used for SMTP notifications.

    Valid fields:
        - to_addresses
        - cc_addresses
        - bcc_addresses

    Example:
        {
            to_addresses: [ "address1@example.com" ],
            cc_addresses: [ "address2@example.com" ],
            bcc_addresses: [ "address3@example.com" ]
        }
    """

    @model_validator(mode="before")
    @classmethod
    def set_interpreting_service_name(
        cls, data: "SmtpAddressGroup"
    ) -> "SmtpAddressGroup":
        if isinstance(data, dict) and "interpreting_service_name" not in data:
            data["interpreting_service_name"] = "smtp"
        return data
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_smtp_message_template.py sha256=f221f7e1d19b58df27b94f8674bfeae7963a3959f9a0b643160a10be4a18e343 bytes=1180 -->
## FILE: nisystemlink/clients/notification/models/_smtp_message_template.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/notification/models/_smtp_message_template.py`
- sha256: `f221f7e1d19b58df27b94f8674bfeae7963a3959f9a0b643160a10be4a18e343`
- bytes: 1180

````python
from typing import Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.notification.models._base_notification_metadata import (
    BaseNotificationMetadata,
)
from pydantic import model_validator


class SmtpMessageTemplateFields(JsonModel):
    """Template fields to construct an SMTP message."""

    subject_template: str
    """Subject template of the message."""

    body_template: str | None = None
    """Body template of the message."""


class SmtpMessageTemplate(BaseNotificationMetadata):
    """Model defining message template for SMTP service"""

    interpreting_service_name: Literal["smtp"] = "smtp"
    """Service name for SMTP-based interpretation."""

    fields: SmtpMessageTemplateFields
    """Subject and body template fields for SMTP messages."""

    @model_validator(mode="before")
    @classmethod
    def set_interpreting_service_name(
        cls, data: "SmtpMessageTemplate"
    ) -> "SmtpMessageTemplate":
        if isinstance(data, dict) and "interpreting_service_name" not in data:
            data["interpreting_service_name"] = "smtp"
        return data
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/__init__.py sha256=325f59d8c5c05c86e021c3e8eda295f9bab050093db77f65958f1c3a35699784 bytes=138 -->
## FILE: nisystemlink/clients/product/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/__init__.py`
- sha256: `325f59d8c5c05c86e021c3e8eda295f9bab050093db77f65958f1c3a35699784`
- bytes: 138

````python
"""Start here with ProductClient for product management."""

from ._product_client import ProductClient

__all__ = ["ProductClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/_product_client.py sha256=a443cbb2804e2b6bbb83b5b331977ce8eb8401fc3cae2761cd7aae865cf26ce4 bytes=8409 -->
## FILE: nisystemlink/clients/product/_product_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/_product_client.py`
- sha256: `a443cbb2804e2b6bbb83b5b331977ce8eb8401fc3cae2761cd7aae865cf26ce4`
- bytes: 8409

````python
"""Implementation of Product Client"""

from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import delete, get, post
from uplink import Field, Query, retry, returns

from . import models
from ..core.helpers._partial_success import unwrap_single_item_partial_success


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class ProductClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Product Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()
        super().__init__(configuration, base_path="/nitestmonitor/v2/")

    @post("products", args=[Field("products")])
    def create_products(
        self, products: List[models.CreateProductRequest]
    ) -> models.CreateProductsPartialSuccess:
        """Creates one or more products and returns errors for failed creations.

        Args:
            products: A list of products to attempt to create.

        Returns: A list of created products, products that failed to create, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` service of provided invalid
                arguments.
        """
        ...

    def create_product(self, product: models.CreateProductRequest) -> models.Product:
        """Creates a single product.

        Args:
            product: The product to create.

        Returns:
            The created product.

        Raises:
            ApiException: if the product could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_products([product])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.products,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to create product.",
            empty_message="Server returned no created products.",
        )

    @get(
        "products",
        args=[Query("continuationToken"), Query("take"), Query("returnCount")],
    )
    def get_products_paged(
        self,
        continuation_token: str | None = None,
        take: int | None = None,
        return_count: bool | None = None,
    ) -> models.PagedProducts:
        """Reads a list of products.

        Args:
            continuation_token: The token used to paginate results.
            take: The number of products to get in this request.
            return_count: Whether or not to return the total number of products available.

        Returns:
            A list of products.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @get("products/{id}")
    def get_product(self, id: str) -> models.Product:
        """Retrieves a single product by id.

        Args:
            id (str): Unique ID of a products.

        Returns:
            The single product matching `id`

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @post("query-products")
    def query_products_paged(
        self, query: models.QueryProductsRequest
    ) -> models.PagedProducts:
        """Queries for products that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of products.

        Returns:
            A paged list of products with a continuation token to get the next page.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided invalid
                arguments.
        """
        ...

    @returns.json  # type: ignore
    @post("query-product-values")
    def query_product_values(
        self, query: models.QueryProductValuesRequest
    ) -> List[str]:
        """Queries for products that match the query and returns a list of the requested field.

        Args:
            query : The query for the fields you want.

        Returns:
            A list of the values of the field you requested.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided
            invalid arguments.
        """
        ...

    @post("update-products", args=[Field("products"), Field("replace")])
    def update_products(
        self, products: List[models.UpdateProductRequest], replace: bool = False
    ) -> models.CreateProductsPartialSuccess:
        """Updates a list of products with optional field replacement.

        Args:
            `products`: A list of products to update. Products are matched for update by id.
            `replace`: Replace the existing fields instead of merging them. Defaults to `False`.
                If this is `True`, then `keywords` and `properties` for the product will be
                    replaced by what is in the `products` provided in this request.
                If this is `False`, then the `keywords` and `properties` in this request will
                    merge with what is already present in the server resource.

        Returns: A list of updates products, products that failed to update, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    def update_product(
        self, product: models.UpdateProductRequest, replace: bool = False
    ) -> models.Product:
        """Updates a single product.

        Args:
            product: The product to update.
            replace: Replace the existing fields instead of merging them.

        Returns:
            The updated product.

        Raises:
            ApiException: if the product could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_products([product], replace=replace)

        return unwrap_single_item_partial_success(
            response=response,
            items=response.products,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to update product.",
            empty_message="Server returned no updated products.",
        )

    @delete("products/{id}")
    def delete_product(self, id: str) -> None:
        """Deletes a single product by id.

        Args:
            id (str): Unique ID of a product.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @post("delete-products", args=[Field("ids")])
    def delete_products(
        self, ids: List[str]
    ) -> models.DeleteProductsPartialSuccess | None:
        """Deletes multiple products.

        Args:
            ids (List[str]): List of unique IDs of products.

        Returns:
            A partial success if any products failed to delete, or None if all
            products were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/__init__.py sha256=5e43230812af10e86f51d825f6c041f5e6ffab9b2e405dd40d8c4ee1b8fee116 bytes=485 -->
## FILE: nisystemlink/clients/product/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/__init__.py`
- sha256: `5e43230812af10e86f51d825f6c041f5e6ffab9b2e405dd40d8c4ee1b8fee116`
- bytes: 485

````python
from ._create_products_partial_success import CreateProductsPartialSuccess
from ._delete_products_partial_success import DeleteProductsPartialSuccess
from ._paged_products import PagedProducts
from ._query_products_request import (
    ProductField,
    ProductOrderBy,
    ProductProjection,
    QueryProductsRequest,
    QueryProductValuesRequest,
)
from ._product import Product
from ._product_request import CreateProductRequest, UpdateProductRequest

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_create_products_partial_success.py sha256=872d426d31405e4a104ad9ae16581cb0d295a61147cff9520f920be7b818e84b bytes=806 -->
## FILE: nisystemlink/clients/product/models/_create_products_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_create_products_partial_success.py`
- sha256: `872d426d31405e4a104ad9ae16581cb0d295a61147cff9520f920be7b818e84b`
- bytes: 806

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.product.models._product import Product
from nisystemlink.clients.product.models._product_request import CreateProductRequest


class CreateProductsPartialSuccess(JsonModel):
    products: List[Product]
    """The list of products that were successfully created."""

    failed: List[CreateProductRequest] | None = None
    """The list of products that were not created.

    If this is `None`, then all products were successfully created.
    """

    error: ApiError | None = None
    """Error messages for products that were not created.

    If this is `None`, then all products were successfully created.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_delete_products_partial_success.py sha256=dd6197527c8f1f609d79e762cb80288891a230d8c99bc97e44767bc63f129a55 bytes=586 -->
## FILE: nisystemlink/clients/product/models/_delete_products_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_delete_products_partial_success.py`
- sha256: `dd6197527c8f1f609d79e762cb80288891a230d8c99bc97e44767bc63f129a55`
- bytes: 586

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteProductsPartialSuccess(JsonModel):
    """The result of deleting multiple products when one or more products could not be deleted."""

    ids: List[str]
    """The IDs of the products that were successfully deleted."""

    failed: List[str] | None = None
    """The IDs of the products that could not be deleted."""

    error: ApiError | None = None
    """The error that occurred when deleting the products."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_paged_products.py sha256=b535ea00e9282d6fa70dfe01af9a7ad5fa6cee01aae701a92e8c4bfdfc00c169 bytes=519 -->
## FILE: nisystemlink/clients/product/models/_paged_products.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_paged_products.py`
- sha256: `b535ea00e9282d6fa70dfe01af9a7ad5fa6cee01aae701a92e8c4bfdfc00c169`
- bytes: 519

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging
from nisystemlink.clients.product.models._product import Product


class PagedProducts(WithPaging):
    """The response containing the list of products, total count of products and the continuation
    token if applicable.
    """

    products: List[Product]
    """A list of all the products in this page."""

    total_count: int | None = None
    """The total number of products that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_product.py sha256=efed211089d49342865812d0e06433f3980541d51a04b8f6f12c62bb3abd6981 bytes=1443 -->
## FILE: nisystemlink/clients/product/models/_product.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_product.py`
- sha256: `efed211089d49342865812d0e06433f3980541d51a04b8f6f12c62bb3abd6981`
- bytes: 1443

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class Product(JsonModel):
    """Contains information about a product."""

    id: str | None = None
    """The globally unique id of the product."""

    part_number: str | None = None
    """The part number is the unique identifier of a product within a single org.

    Usually the part number refers to a specific revision or version of a given product."""

    name: str | None = None
    """The name of the product.

    Usually the name is used to refer to several part numbers that all have the same name but
    different revisions or versions.
    """

    family: str | None = None
    """The family that that this product belongs to.

    Usually the family is a grouping above product name. A family usually has multiple product
    names within it.
    """

    updated_at: datetime | None = None
    """The last time that this product was updated."""

    file_ids: List[str] | None = None
    """A list of file ids that are attached to this product."""

    keywords: List[str] | None = None
    """A list of keywords that categorize this product."""

    properties: Dict[str, str] | None = None
    """A list of custom properties for this product."""

    workspace: str | None = None
    """The id of the workspace that this product belongs to."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_product_request.py sha256=bb96955423bc468be4fe99f3b748bf88a9c5c1a0e56b16c6bcbbf63b49bfe525 bytes=1461 -->
## FILE: nisystemlink/clients/product/models/_product_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_product_request.py`
- sha256: `bb96955423bc468be4fe99f3b748bf88a9c5c1a0e56b16c6bcbbf63b49bfe525`
- bytes: 1461

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class BaseProductRequest(JsonModel):
    """Contains information about a product."""

    name: str | None = None
    """The name of the product.

    Usually the name is used to refer to several part numbers that all have the same name but
    different revisions or versions.
    """

    family: str | None = None
    """The family that that this product belongs to.

    Usually the family is a grouping above product name. A family usually has multiple product
    names within it.
    """

    file_ids: List[str] | None = None
    """A list of file ids that are attached to this product."""

    keywords: List[str] | None = None
    """A list of keywords that categorize this product."""

    properties: Dict[str, str] | None = None
    """A list of custom properties for this product."""

    workspace: str | None = None
    """The id of the workspace that this product belongs to."""


class CreateProductRequest(BaseProductRequest):

    part_number: str
    """The part number is the unique identifier of a product within a single org.

    Usually the part number refers to a specific revision or version of a given product."""


class UpdateProductRequest(BaseProductRequest):
    """This is the request model to update a product."""

    id: str
    """The globally unique id of the product."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_query_products_request.py sha256=a3b0e575945f3f14a63605606ef89cc6ec04035f5663e2d001f0eea279d3f938 bytes=4957 -->
## FILE: nisystemlink/clients/product/models/_query_products_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/models/_query_products_request.py`
- sha256: `a3b0e575945f3f14a63605606ef89cc6ec04035f5663e2d001f0eea279d3f938`
- bytes: 4957

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field


class ProductOrderBy(str, Enum):
    """The valid ways to order a product query."""

    ID = "ID"
    FAMILY = "FAMILY"
    PART_NUMBER = "PART_NUMBER"
    NAME = "NAME"
    UPDATED_AT = "UPDATED_AT"


class ProductField(str, Enum):
    """An enumeration of product fields for which the values can be queried for."""

    ID = "ID"
    FAMILY = "FAMILY"
    PART_NUMBER = "PART_NUMBER"
    NAME = "NAME"
    UPDATED_AT = "UPDATED_AT"


class ProductProjection(str, Enum):
    """An enumeration of all fields in a Product.

    These are used to project the required fields from the API response.
    """

    ID = "ID"
    FAMILY = "FAMILY"
    PART_NUMBER = "PART_NUMBER"
    NAME = "NAME"
    UPDATED_AT = "UPDATED_AT"
    WORKSPACE = "WORKSPACE"
    KEYWORDS = "KEYWORDS"
    PROPERTIES = "PROPERTIES"
    FILE_IDS = "FILE_IDS"


class QueryProductsBase(JsonModel):
    """Base class for product query requests."""

    filter: str | None = None
    """
    The product query filter in Dynamic Linq format.

    Allowed properties in the filter are:
    - `id`: String for the global identifier of the product
    - `partNumber`: String representing the part number of the product
    - `name`: String of the product name
    - `family`: String for the product family
    - `updatedAt`: ISO-8601 formatted UTC timestamp indicating when the product was last updated.
    - `keywords`: A list of keyword strings
    - `properties`: A dictionary of additional string to string properties
    - `fileIds`: A list of string ids for files stored in the file service (`/nifile`)

    See the Dynamic Linq query language documentation:
    https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language

    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable.
    """

    substitutions: List[str] | None = None
    """String substitutions into the `filter`.

    Makes substitutions in the query filter expression. Substitutions for the query expression are
    indicated by non-negative integers that are prefixed with the "at" symbol. Each substitution in
    the given expression will be replaced by the element at the corresponding index (zero-based) in
    this list. For example, "@0" in the filter expression will be replaced with the element at the
    zeroth index of the substitutions list.
    """


class QueryProductsRequest(QueryProductsBase):
    """Request model for querying products."""

    order_by: ProductOrderBy | None = Field(
        None,
        validation_alias=AliasChoices("order_by", "orderBy"),
        serialization_alias="orderBy",
    )
    """Specifies the fields to use to sort the products.

    By default, products are sorted by `id`
    """

    descending: bool | None = None
    """Specifies whether to return the products in descending order.

    By default, this value is `false` and products are sorted in ascending order.
    """

    projection: List[ProductProjection] | None = None
    """Specifies the product fields to project.

    When a field value is given here, the corresponding field will be
    present in all returned products, and all unspecified fields will
    be excluded. If no projection is specified, all product fields
    will be returned.
    """

    take: int | None = None
    """Maximum number of products to return in the current API response.

    Uses the default if the specified value is negative. The default value is `1000` products.
    """

    continuation_token: str | None = None
    """Allows users to continue the query at the next product that matches the given criteria.

    To retrieve the next page of products, pass the continuation token from the previous
    page in the next request. The service responds with the next page of data and provides a new
    continuation token. To paginate results, continue sending requests with the newest continuation
    token provided in each response.
    """

    return_count: bool | None = None
    """If true, the response will include a count of all products matching the filter.

    By default, this value is `False` and count is not returned. Note that returning the count may
    incur performance penalties as the service may have to do a complete walk of the database to
    compute count. """


class QueryProductValuesRequest(QueryProductsBase):
    """Request model for querying product values."""

    field: ProductField | None = None
    """The product field to return for this query."""

    starts_with: str | None = None
    """Only return string parameters prefixed by this value (case sensitive)."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/utilities/__init__.py sha256=c03b8c96523f002891e103f463ca7f3f9f182731d65cafead78b26a0c7bb46d4 bytes=141 -->
## FILE: nisystemlink/clients/product/utilities/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/utilities/__init__.py`
- sha256: `c03b8c96523f002891e103f463ca7f3f9f182731d65cafead78b26a0c7bb46d4`
- bytes: 141

````python
from ._dataframe_utilities import convert_products_to_dataframe
from ._file_utilities import get_products_linked_to_file

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/utilities/_dataframe_utilities.py sha256=06b7d9691170d6b58b5b33b30ee0ed2188870c6a817d7fef555852ed3727ef76 bytes=984 -->
## FILE: nisystemlink/clients/product/utilities/_dataframe_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/utilities/_dataframe_utilities.py`
- sha256: `06b7d9691170d6b58b5b33b30ee0ed2188870c6a817d7fef555852ed3727ef76`
- bytes: 984

````python
from typing import List

import pandas as pd
from nisystemlink.clients.product.models import Product
from pandas import DataFrame


def convert_products_to_dataframe(products: List[Product]) -> DataFrame:
    """Converts a list of products into a normalized dataframe.

    Args:
        products (List[Product]): A list of products

    Returns:
        DataFrame:
            - A Pandas DataFrame containing the product data. The DataFrame would consist of all the
            fields in the input products.
            - A new column would be created for unique properties across all products. The property
            columns would be named in the format `properties.property_name`.
    """
    products_dict_representation = [
        product.model_dump(exclude_none=True) for product in products
    ]
    normalized_products_dataframe = pd.json_normalize(
        products_dict_representation, sep="."
    )

    return normalized_products_dataframe
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/product/utilities/_file_utilities.py sha256=0720bab1124c97556f095cb87893b48e3ca3f5f1a3ed7ccc63f9abe02dabe9ef bytes=1235 -->
## FILE: nisystemlink/clients/product/utilities/_file_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/product/utilities/_file_utilities.py`
- sha256: `0720bab1124c97556f095cb87893b48e3ca3f5f1a3ed7ccc63f9abe02dabe9ef`
- bytes: 1235

````python
from typing import List

from nisystemlink.clients.product._product_client import ProductClient
from nisystemlink.clients.product.models._paged_products import PagedProducts
from nisystemlink.clients.product.models._product import (
    Product,
)
from nisystemlink.clients.product.models._query_products_request import (
    QueryProductsRequest,
)


def get_products_linked_to_file(client: ProductClient, file_id: str) -> List[Product]:
    """Gets a list of all the products that are linked to the file.

    Args:
        `client` : The `ProductClient` to use for the request.
        `file_id`: The id of the file to query links for.

    Returns:
        `List[Product]`: A list of all the products that are linked to the file with `file_id`
    """
    query_request = QueryProductsRequest(
        filter=f'fileIds.Contains("{file_id}")', take=100
    )
    response: PagedProducts = client.query_products_paged(query_request)
    products = response.products
    while response.continuation_token:
        query_request.continuation_token = response.continuation_token
        response = client.query_products_paged(query_request)
        products.extend(response.products)
    return products
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/__init__.py sha256=73e0e456d3d2ab890ae15bf899f9b22009dc50ddd3a949ace0714ccada42caf7 bytes=132 -->
## FILE: nisystemlink/clients/spec/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/__init__.py`
- sha256: `73e0e456d3d2ab890ae15bf899f9b22009dc50ddd3a949ace0714ccada42caf7`
- bytes: 132

````python
"""Start here with SpecClient for specification management."""

from ._spec_client import SpecClient

__all__ = ["SpecClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/_spec_client.py sha256=9478ad54106e6823d3905b159854f8fd46dc91053b3d2008ecfab819445fe412 bytes=6324 -->
## FILE: nisystemlink/clients/spec/_spec_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/_spec_client.py`
- sha256: `9478ad54106e6823d3905b159854f8fd46dc91053b3d2008ecfab819445fe412`
- bytes: 6324

````python
"""Implementation of SpecClient"""

from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import get, post
from uplink import Field, retry

from . import models
from ..core.helpers._partial_success import unwrap_single_item_partial_success


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class SpecClient(BaseClient):
    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Spec Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/nispec/v1/")

    @get("")
    def api_info(self) -> models.V1Operations:
        """Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        """
        ...

    @post("specs")
    def create_specs(
        self, specs: models.CreateSpecificationsRequest
    ) -> models.CreateSpecificationsPartialSuccess:
        """Creates one or more specifications.

        Args:
            specs: A list of specifications to create.

        Returns:
            A list of specs that were successfully created and ones that failed to be created.

        Raises:
            ApiException: if unable to communicate with the `/nispec` service or if there are
            invalid arguments.
        """
        ...

    def create_spec(
        self, spec: models.CreateSpecificationsRequestObject
    ) -> models.CreatedSpecification:
        """Creates a single specification.

        Args:
            spec: The specification to create.

        Returns:
            The created specification.

        Raises:
            ApiException: if the specification could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_specs(models.CreateSpecificationsRequest(specs=[spec]))

        return unwrap_single_item_partial_success(
            response=response,
            items=response.created_specs,
            failed=response.failed_specs,
            error=response.error,
            failure_message="Failed to create spec.",
            empty_message="Server returned no created specs.",
        )

    @post("delete-specs", args=[Field("ids")])
    def delete_specs(
        self, ids: List[str]
    ) -> models.DeleteSpecificationsPartialSuccess | None:
        """Deletes one or more specifications by global id.

        Args:
            ids: a list of specification ids. Note that these are the global ids and not the
            `specId` that is local to a product and workspace.

        Returns:
            None if all deletes succeed otherwise a list of which ids failed and which succeeded.

        Raises:
            ApiException: if unable to communicate with the `nispec` service or if there are invalid
            arguments.
        """
        ...

    @post("query-specs")
    def query_specs(
        self, query: models.QuerySpecificationsRequest
    ) -> models.PagedSpecifications:
        """Queries for specs that match the filters.

        Args:
            query: The query contains a product id as well as a filter for specs under that product.

        Returns:
            A list of specifications that match the filter.
        """
        ...

    @get("specs/{id}")
    def get_spec(self, id: str) -> models.Specification:
        """Retrieves a single spec by id.

        Args:
            id (str): Unique ID of a specification.

        Returns:
            The single spec matching `id`

        Raises:
            ApiException: if unable to communicate with the `nispec` service or if there are invalid
            arguments.
        """
        ...

    @post("update-specs")
    def update_specs(
        self, specs: models.UpdateSpecificationsRequest
    ) -> models.UpdateSpecificationsPartialSuccess | None:
        """Updates one or more specifications.

        Update requires that the version field matches the version being updated from.

        Args:
            specs: a list of specifications that are to be updated. Must include the global id and
            each spec being updated must match the version currently on the server.

        Returns
            A list of specs that were successfully updated and a list of ones that were not along
            with error messages for updates that failed.
        """
        ...

    def update_spec(
        self, spec: models.UpdateSpecificationsRequestObject
    ) -> models.UpdatedSpecification:
        """Updates a single specification.

        Args:
            spec: The specification to update.

        Returns:
            The updated specification.

        Raises:
            ApiException: if the specification could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_specs(models.UpdateSpecificationsRequest(specs=[spec]))

        return unwrap_single_item_partial_success(
            response=response,
            items=response.updated_specs if response is not None else None,
            failed=response.failed_specs if response is not None else None,
            error=response.error if response is not None else None,
            failure_message="Failed to update spec.",
            empty_message="Server returned no updated specs.",
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/__init__.py sha256=80a53fa140e6cce125142f89d543a69c617f039a93dc699eec65d712fa5ae683 bytes=899 -->
## FILE: nisystemlink/clients/spec/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/__init__.py`
- sha256: `80a53fa140e6cce125142f89d543a69c617f039a93dc699eec65d712fa5ae683`
- bytes: 899

````python
from ._api_info import Operation, V1Operations
from ._condition import (
    Condition,
    ConditionRange,
    ConditionType,
    NumericConditionValue,
    StringConditionValue,
)
from ._create_specs_request import (
    CreatedSpecification,
    CreateSpecificationsPartialSuccess,
    CreateSpecificationsRequest,
    CreateSpecificationsRequestObject,
)
from ._delete_specs_request import DeleteSpecificationsPartialSuccess
from ._query_specs import (
    QuerySpecificationsRequest,
    PagedSpecifications,
    SpecificationProjection,
)
from ._specification import (
    Specification,
    SpecificationDefinition,
    SpecificationLimit,
    SpecificationType,
)
from ._update_specs_request import (
    UpdatedSpecification,
    UpdateSpecificationsPartialSuccess,
    UpdateSpecificationsRequest,
    UpdateSpecificationsRequestObject,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_api_info.py sha256=02751b7d110379d122a1cfba3259122d6a53e4d9698d4da51dcfe938c1bc2c67 bytes=601 -->
## FILE: nisystemlink/clients/spec/models/_api_info.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_api_info.py`
- sha256: `02751b7d110379d122a1cfba3259122d6a53e4d9698d4da51dcfe938c1bc2c67`
- bytes: 601

````python
from nisystemlink.clients.core._api_info import Operation
from nisystemlink.clients.core._uplink._json_model import JsonModel


class V1Operations(JsonModel):
    """The operations available in the routes provided by the v1 HTTP API."""

    create_specifications: Operation
    """The ability to create new specifications."""

    query_specifications: Operation
    """The ability to query specifications."""

    update_specifications: Operation
    """The ability to update specifications."""

    delete_specifications: Operation
    """The ability to delete specifications."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_condition.py sha256=3af35fe555bad54763cd4ef33da3e3bbc4a2df0d91eb6e8bfa4b55a5ec404c5c bytes=2804 -->
## FILE: nisystemlink/clients/spec/models/_condition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_condition.py`
- sha256: `3af35fe555bad54763cd4ef33da3e3bbc4a2df0d91eb6e8bfa4b55a5ec404c5c`
- bytes: 2804

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import StrictFloat, StrictInt, StrictStr


class ConditionType(Enum):
    """Conditions are either numeric or string type."""

    NUMERIC = "NUMERIC"
    """Numeric condition."""

    STRING = "STRING"
    """String condition."""


class ConditionRange(JsonModel):
    """Specifies the range of values that the condition must cover."""

    min: float | None = None
    """Minimum value of the condition range."""

    max: float | None = None
    """Maximum value of the condition range."""

    step: float | None = None
    """Step value of the condition range."""


class ConditionValueBase(JsonModel):
    """The base type for conditions that can be represented in several styles."""

    condition_type: ConditionType | None = None
    """Type of the Condition."""


class NumericConditionValue(ConditionValueBase):
    """A numeric condition.

    Numeric conditions can contain a combination of ranges and discrete lists.
    """

    range: List[ConditionRange] | None = None
    """List of condition range values."""

    # StrictFloat and StrictInt are used here because discrete is a common property for
    # NumericConditionValue and StringConditionValue.
    # If float/int is used, pydantic converts string of number into float/int by default
    # when deserializing a StringCondition JSON and misinterprets it as NumericConditionValue type.
    discrete: List[StrictFloat | StrictInt | None] | None = None
    """List of condition discrete values."""

    unit: str | None = None
    """Unit of the condition."""


class StringConditionValue(ConditionValueBase):
    """A string condition.

    String conditions may only contain discrete lists of values.
    """

    # StrictStr is used here because discrete is a common property for
    # NumericConditionValue and StringConditionValue.
    # If str is used, pydantic converts any datatype into string by default when deserializing a
    # NumericCondition JSON and misinterprets it as StringConditionValue type.
    discrete: List[StrictStr] | None = None
    """List of condition discrete values."""


class Condition(JsonModel):
    """A single condition."""

    name: str | None = None
    """Name of the condition."""

    # Ideal approach is to set the dtype here as ConditionValue and use pydantic discriminator to
    # deserialize/serialize the JSON into correct ConditionValue sub types. But Union of dtypes is
    # used here as the discriminator field could be none when projection is used in query API.
    value: NumericConditionValue | StringConditionValue | None = None
    """Value of the condition."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_create_specs_request.py sha256=81d86b9520fc303ff4a78d0c96ec96d6bc478253cdd47f37327c1e887d4e2615 bytes=2500 -->
## FILE: nisystemlink/clients/spec/models/_create_specs_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_create_specs_request.py`
- sha256: `81d86b9520fc303ff4a78d0c96ec96d6bc478253cdd47f37327c1e887d4e2615`
- bytes: 2500

````python
from datetime import datetime
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.spec.models._specification import (
    SpecificationDefinition,
    SpecificationType,
)


class CreateSpecificationsRequestObject(SpecificationDefinition):
    product_id: str
    """Id of the product to which the specification will be associated."""

    spec_id: str
    """User provided value using which the specification will be identified.

    This should be unique for a product and workspace combination.
    """

    type: SpecificationType
    """Type of the specification."""


class CreateSpecificationsRequest(JsonModel):
    """Create multiple specifications."""

    specs: List[CreateSpecificationsRequestObject] | None = None
    """List of specifications to be created."""


class BaseSpecificationResponse(JsonModel):
    """Base Response Model for create specs response and update specs response."""

    id: str
    """The global Id of the specification."""

    product_id: str
    """Id of the product to which the specification will be associated."""

    spec_id: str
    """User provided value using which the specification will be identified.

    This should be unique for a product and workspace combination.
    """

    workspace: str
    """Id of the workspace to which the specification will be associated.

    Default workspace will be taken if the value is not given.
    """

    version: int
    """
    Current version of the specification.

    When an update is applied, the version is automatically incremented.
    """


class CreatedSpecification(BaseSpecificationResponse):
    """A specification successfully created on the server."""

    created_at: datetime
    """ISO-8601 formatted timestamp indicating when the specification was created."""

    created_by: str
    """Id of the user who created the specification."""


class CreateSpecificationsPartialSuccess(JsonModel):
    """When some specs can not be created, this contains the list that was and was not created."""

    created_specs: List[CreatedSpecification] | None = None
    """Information about the created specification(s)"""

    failed_specs: List[CreateSpecificationsRequestObject] | None = None
    """List of specification requests that failed during creation."""

    error: ApiError | None = None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_delete_specs_request.py sha256=1b968d98a3b12dc49096b6d26bc0e6bfde411f9a0a2a70cb9723ab4ef578da9c bytes=520 -->
## FILE: nisystemlink/clients/spec/models/_delete_specs_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_delete_specs_request.py`
- sha256: `1b968d98a3b12dc49096b6d26bc0e6bfde411f9a0a2a70cb9723ab4ef578da9c`
- bytes: 520

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteSpecificationsPartialSuccess(JsonModel):
    """The results of deleting multiple specs when one or more of the specs could not be deleted."""

    deleted_spec_ids: List[str]
    """Global IDs of the deleted specifications."""

    failed_spec_ids: List[str]
    """Global IDs of the specifications that could not be deleted."""

    error: ApiError
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_query_specs.py sha256=a7db78e15f5c38371b960475cd78f11d27ee34348672c74d024b0857b088383f bytes=4357 -->
## FILE: nisystemlink/clients/spec/models/_query_specs.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_query_specs.py`
- sha256: `a7db78e15f5c38371b960475cd78f11d27ee34348672c74d024b0857b088383f`
- bytes: 4357

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.core._uplink._with_paging import WithPaging
from nisystemlink.clients.spec.models._specification import Specification


class SpecificationProjection(str, Enum):
    """The allowed projections for query.

    When using projection, only the fields specified by the projection element will be included in
    the response.
    """

    ID = "ID"
    PRODUCT_ID = "PRODUCT_ID"
    SPEC_ID = "SPEC_ID"
    NAME = "NAME"
    CATEGORY = "CATEGORY"
    TYPE = "TYPE"
    SYMBOL = "SYMBOL"
    BLOCK = "BLOCK"
    LIMIT = "LIMIT"
    UNIT = "UNIT"
    CONDITION_NAME = "CONDITION_NAME"
    CONDITION_VALUES = "CONDITION_VALUES"
    CONDITION_UNIT = "CONDITION_UNIT"
    CONDITION_TYPE = "CONDITION_TYPE"
    KEYWORDS = "KEYWORDS"
    PROPERTIES = "PROPERTIES"
    WORKSPACE = "WORKSPACE"
    CREATED_AT = "CREATED_AT"
    CREATED_BY = "CREATED_BY"


class SpecificationOrderBy(Enum):
    """The valid ways to order the response to a spec query."""

    ID = "ID"
    SPEC_ID = "SPEC_ID"


class QuerySpecificationsRequest(JsonModel):
    """The request to query specifications."""

    product_ids: List[str]
    """IDs of the products to query the specifications for."""

    take: int | None = None
    """Maximum number of specifications to return in the current API response.

    Uses the default if the specified value is negative. The default value is `1000` specs.
    """

    continuation_token: str | None = None
    """Allows users to continue the query at the next specification that matches the given criteria.

    To retrieve the next batch of specifications, pass the continuation token from the previous
    batch in the next request. The service responds with the next batch of data and provides a new
    continuation token. To paginate results, continue sending requests with the newest continuation
    token provided in each response.
    """

    filter: str | None = None
    """
    The specification query filter in Dynamic Linq format.

    Allowed properties in the filter are:
    - `specId`: String representing the SpecID of a specification.
    - `name`: String representing the name of a specification.
    - `category`: String representing the category of a specification.
    - `type`: String enumeration representing the type of the specification.
        Possible values are : PARAMETRIC, FUNCTIONAL
    - `block`: String representing the block of a specification.
    - `symbol`: String representing the symbol of a specification.
    - `unit`: String representing the unit of a specification.
    - `workspace`: String representing the ID of the workspace the specification belongs to.
    - `createdBy`: String representing the ID of the user who created the specification.
    - `createdAt`: ISO-8601 formatted UTC timestamp indicating when the specification was created.
    - `updatedBy`: String representing the ID of the user who updated the specification.
    - `updatedAt`: ISO-8601 formatted UTC timestamp indicating when the specification was updated.

    See [Dynamic Linq](https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language)
    documentation for more details.
    """

    projection: List[SpecificationProjection] | None = None
    """Specifies the fields to include in the returned specifications.

    Fields you do not specify are excluded. Returns all fields if no value is specified.
    """

    order_by: SpecificationOrderBy | None = None
    """Specifies the field to use to sort specifications.

    By default, specifications are sorted by `ID`.
    """
    order_by_descending: bool | None = None
    """Specifies whether to return the specifications in descending order.

    By default, this value is `false` and specifications are sorted in ascending order.
    """


class PagedSpecifications(WithPaging):
    """The list of matching specifications and a continuation token to get the next items."""

    specs: List[Specification] | None = None
    """List of queried specifications.

    An empty list indicates that there are no specifications meeting the criteria provided in the
    request.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_specification.py sha256=cf36d83273f0ff23d57d2e0838f4b0f2b72652eb22d4012dbcc1f3ffaaaf816f bytes=3420 -->
## FILE: nisystemlink/clients/spec/models/_specification.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_specification.py`
- sha256: `cf36d83273f0ff23d57d2e0838f4b0f2b72652eb22d4012dbcc1f3ffaaaf816f`
- bytes: 3420

````python
from datetime import datetime
from enum import Enum
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._condition import Condition


class SpecificationLimit(JsonModel):
    """A limit for a specification.

    The limit is the value that a measurement should be compared against during analysis to
    determine the health or pass/fail status of that measurement.
    """

    min: float | None = None
    """Minimum limit of the specification.

    All measurements that map to this specification should be > this limit.
    """

    typical: float | None = None
    """Typical value of the specification."""

    max: float | None = None
    """Maximum value of the specification.

    All measurements that map to this specification should be < this limit.
    """


class SpecificationType(Enum):
    """The overall type of the specification."""

    PARAMETRIC = "PARAMETRIC"
    """Parametric specs have limits."""

    FUNCTIONAL = "FUNCTIONAL"
    """Functional specs only have pass/fail status."""


class SpecificationDefinition(JsonModel):

    product_id: str | None = None
    """Id of the product to which the specification will be associated."""

    spec_id: str | None = None
    """User provided value using which the specification will be identified.

    This should be unique for a product and workspace combination.
    """

    name: str | None = None
    """Name of the specification."""

    category: str | None = None
    """Category of the specification."""

    type: SpecificationType | None = None
    """Type of the specification."""

    symbol: str | None = None
    """Short form identifier of the specification."""

    block: str | None = None
    """Block name of the specification.

    Typically a block is one of the subsystems of the overall product being specified.
    """

    limit: SpecificationLimit | None = None
    """The limits for this spec."""

    unit: str | None = None
    """Unit of the specification."""

    conditions: List[Condition] | None = None
    """Conditions associated with the specification."""

    keywords: List[str] | None = None
    """Keywords or phrases associated with the specification."""

    properties: Dict[str, str] | None = None
    """Additional properties associated with the specification."""

    workspace: str | None = None
    """Id of the workspace to which the specification will be associated.

    Default workspace will be taken if the value is not given.
    """


class Specification(SpecificationDefinition):
    """The complete definition of a specification."""

    id: str | None = None
    """The global Id of the specification."""

    created_at: datetime | None = None
    """ISO-8601 formatted timestamp indicating when the specification was created."""

    created_by: str | None = None
    """Id of the user who created the specification."""

    updated_at: datetime | None = None
    """ISO-8601 formatted timestamp indicating when the specification was last updated."""

    updated_by: str | None = None
    """Id of the user who last updated the specification."""

    version: int | None = None
    """
    Current version of the specification.

    When an update is applied, the version is automatically incremented.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_update_specs_request.py sha256=acbc8bff7cb3e83662465f18ca13d6ce3179ce3ce1e39cf9bece7c74cfa4421e bytes=2131 -->
## FILE: nisystemlink/clients/spec/models/_update_specs_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/models/_update_specs_request.py`
- sha256: `acbc8bff7cb3e83662465f18ca13d6ce3179ce3ce1e39cf9bece7c74cfa4421e`
- bytes: 2131

````python
from datetime import datetime
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.spec.models._create_specs_request import (
    BaseSpecificationResponse,
)
from nisystemlink.clients.spec.models._specification import (
    SpecificationDefinition,
    SpecificationType,
)


class UpdateSpecificationsRequestObject(SpecificationDefinition):
    id: str
    """The global Id of the specification."""

    product_id: str
    """Id of the product to which the specification will be associated."""

    spec_id: str
    """User provided value using which the specification will be identified.

    This should be unique for a product and workspace combination.
    """

    type: SpecificationType
    """Type of the specification."""

    workspace: str
    """Id of the workspace to which the specification will be associated.

    Default workspace will be taken if the value is not given.
    """

    version: int
    """
    Current version of the specification.

    When an update is applied, the version is automatically incremented.
    """


class UpdateSpecificationsRequest(JsonModel):

    specs: List[UpdateSpecificationsRequestObject] | None = None
    """List of specifications to be updated."""


class UpdatedSpecification(BaseSpecificationResponse):
    """A specification that was updated on the server."""

    updated_at: datetime
    """ISO-8601 formatted timestamp indicating when the specification was last updated."""

    updated_by: str
    """Id of the user who last updated the specification."""


class UpdateSpecificationsPartialSuccess(JsonModel):

    updated_specs: List[UpdatedSpecification] | None = None
    """Information about each of the updated specification(s)."""

    failed_specs: List[UpdateSpecificationsRequestObject] | None = None
    """Information about each of the specification request(s) that failed during the update."""

    error: ApiError | None = None
    """Any errors that occurred."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/utilities/__init__.py sha256=2221a31e31d0e26362001d65ebee197431256648b7c56dfdb235f37e746a69f0 bytes=203 -->
## FILE: nisystemlink/clients/spec/utilities/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/utilities/__init__.py`
- sha256: `2221a31e31d0e26362001d65ebee197431256648b7c56dfdb235f37e746a69f0`
- bytes: 203

````python
from ._dataframe_utilities import (
    convert_specs_to_dataframe,
    summarize_conditions_as_a_string,
    normalize_conditions_per_column,
    normalize_conditions_per_row,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/utilities/_constants.py sha256=632d4720de661cc55ded001a4834c484d5cfdafab6493c68716241162f3aaa08 bytes=172 -->
## FILE: nisystemlink/clients/spec/utilities/_constants.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/utilities/_constants.py`
- sha256: `632d4720de661cc55ded001a4834c484d5cfdafab6493c68716241162f3aaa08`
- bytes: 172

````python
class DataFrameHeaders:
    CONDITION_COLUMN_HEADER_PREFIX = "condition_"

    PROPERTY_COLUMN_HEADER_PREFIX = "properties."

    KEYWORDS_COLUMN_HEADER = "keywords"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/spec/utilities/_dataframe_utilities.py sha256=9a078cbf1be43c6034c6442dff773b51d76ebdb0a5262ab0a3d08c5ad626aae1 bytes=12740 -->
## FILE: nisystemlink/clients/spec/utilities/_dataframe_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/spec/utilities/_dataframe_utilities.py`
- sha256: `9a078cbf1be43c6034c6442dff773b51d76ebdb0a5262ab0a3d08c5ad626aae1`
- bytes: 12740

````python
from typing import Any, Callable, Dict, List

import pandas as pd
from nisystemlink.clients.spec.models._condition import (
    Condition,
    NumericConditionValue,
    StringConditionValue,
)
from nisystemlink.clients.spec.models._specification import (
    Specification,
    SpecificationLimit,
    SpecificationType,
)
from nisystemlink.clients.spec.utilities._constants import DataFrameHeaders


def summarize_conditions_as_a_string(
    conditions: List[Condition],
) -> List[Dict[str, str]]:
    """Converts the condition values to an easily readable string format that summarizes
    either of numeric or string condition.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The dictionary key will be
        "condition_<conditionName>(<conditionUnit>)".
        The dictionary value will be "[min: num; max: num, step: num], num, num"
        where data within the '[]' is numeric condition range and other num
        values are numeric condition discrete values.
        The dictionary value will be "str, str, str" - where str values are the
        condition discrete values for a string condition. If the condition doesn't
        have a name and value, it will be skipped.
    """
    return [
        {
            __generate_condition_column_header(condition): ", ".join(
                __serialize_condition_value(condition)
            )
            for condition in conditions
            if condition.name and condition.value
        }
    ]


def normalize_conditions_per_column(
    conditions: List[Condition],
) -> List[Dict[str, Any]]:
    """Convert conditions into list of dictionaries where dictionary key will be condition name
    and dictionary value will be condition value.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The key will be
        the condition name and the value will be the condition value which is
        either Numeric Condition Value, String Condition Value or None. If the condition doesn't
        have a name and value, it will be skipped.
    """
    return [
        {
            f"{DataFrameHeaders.CONDITION_COLUMN_HEADER_PREFIX}{condition.name}": condition.value
            for condition in conditions
            if condition.name and condition.value
        }
    ]


def normalize_conditions_per_row(
    conditions: List[Condition],
) -> List[Dict[str, Any]]:
    """Convert conditions into list of dictionaries where dictionary keys will be 'condition.name'
    and 'condition.value' and dictionary values will be condition name and condition value respectively.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The keys will be
        the 'condition.name' and 'condition.values' and the values will be the condition name and
        condition value which is either Numeric Condition Value, String Condition Value or None.
        If the condition doesn't have a name and value, it will be skipped.
        Each condition data will be logged as separate dictionary entry in the list which translates to
        separate row in the dataframe.
    """
    return [
        {"condition.name": condition.name, "condition.value": condition.value}
        for condition in conditions
        if condition.name and condition.value
    ]


def convert_specs_to_dataframe(
    specs: List[Specification],
    condition_format: (
        Callable[[List[Condition]], List[Dict[str, Any]]] | None
    ) = normalize_conditions_per_column,
) -> pd.DataFrame:
    """Creates a Pandas DataFrame for the specs.

    Args:
        specs: List of specs.
        condition_format: A callback function which takes in a list of condition of a spec and returns
                          a list of dictionary of condition and its values. The dictionary keys
                          should be the condition name and the values should be the condition
                          value in any format you need. Dataframe rows will be constructed based on
                          these list of dictionaries. Each dictionary in the list indicates a row.
                          If there is more than one dictionary in the list, it will be considered as a new
                          row and other spec column data will be duplicated.  Keys will be used as the dataframe
                          column header and values will be used as the row cells for the
                          respective column header.
                          If not passed, condition column header will be condition name and
                          corresponding row value will be condition value.
                          For all the condition columns to be grouped together in the dataframe,
                          the dictionary key should have the prefix "condition_".
                          If condition is needed as condition per row, the public method `normalize_conditions_per_row`
                          can be provided as the callback function.
                          If condition value is needed as a string summary of condition data, the public method
                          `summarize_conditions_as_a_string` can be provided as this callback function.
                          If None is passed, conditions will not be included in the dataframe.

    Returns:
        A Pandas DataFrame with the each spec fields having a separate column.
        Following fields are split into sub-columns.
            - conditions: format of the condition columns are decided by the  `condition_format`
            argument of this function.
            - Properties: All the unique properties across all specs will be split into separate columns.
            For example, properties.property1, properties.property2, etc.
    """
    specs_dict = [
        __convert_spec_to_dict(spec=spec, condition=condition)
        for spec in specs
        for condition in (
            condition_format(spec.conditions)
            if (spec.conditions and condition_format)
            else [{}]
        )
    ]

    specs_dataframe = pd.json_normalize(specs_dict)
    specs_dataframe = __format_specs_columns(specs_dataframe=specs_dataframe)
    specs_dataframe.dropna(axis="columns", how="all", inplace=True)

    return specs_dataframe


def __convert_spec_to_dict(
    spec: Specification, condition: Dict[str, Any]
) -> Dict[str, Any]:
    """Converts a spec into dictionary.

    Args:
        spec: Spec object.
        condition: Condition as a dictionary which is added to the output spec dictionary.

    Returns:
        Spec as a dictionary with the provided condition dictionary included.
    """
    return {
        **{
            key: value
            for key, value in vars(spec).items()
            if key not in ["type", "limit", "conditions"]
        },
        **(__serialize_type(spec.type) if spec.type else {}),
        **(__serialize_limits(spec.limit) if spec.limit else {}),
        **{key: value for key, value in condition.items()},
    }


def __serialize_limits(limit: SpecificationLimit) -> Dict[str, str]:
    """Serialize limit into limit.min, limit.typical and limit.max.

    Args:
        limit: Limit of a spec.

    Returns:
        Limit as a dictionary.
    """
    return {f"limit.{key}": value for key, value in vars(limit).items()}


def __serialize_type(type: SpecificationType) -> Dict[str, str]:
    """Serialize type into it's string value.

    Args:
        type: Type of a spec.

    Returns:
        Type as a dictionary.
    """
    return {"type": type.name}


def __format_specs_columns(specs_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Format specs column to group conditions and keep properties and keywords at the end.

    Args:
        specs_dataframe: Dataframe of specs.

    Returns:
        Formatted dataframe of specs.
    """
    column_headers = specs_dataframe.columns.to_list()
    standard_column_headers = [
        header for header in column_headers if __is_standard_column_header(header)
    ]
    condition_headers = [
        header for header in column_headers if __is_condition_header(header=header)
    ]
    properties_headers = [
        header for header in column_headers if __is_property_header(header=header)
    ]
    formatted_column_headers = (
        standard_column_headers
        + condition_headers
        + (["keywords"] if "keywords" in column_headers else [])
        + properties_headers
    )

    return specs_dataframe.reindex(columns=formatted_column_headers, copy=False)


def __is_standard_column_header(header: str) -> bool:
    """Check if column header is not a condition, property or keywords.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header doesn't start with condition_, properties. or keywords. Else returns false.

    """
    return not (
        __is_condition_header(header=header)
        or __is_property_header(header=header)
        or __is_keywords_header(header=header)
    )


def __is_condition_header(header: str) -> bool:
    """Check if column header is not a condition.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header contains 'condition_'. Else returns false.

    """
    return header.startswith(DataFrameHeaders.CONDITION_COLUMN_HEADER_PREFIX)


def __is_property_header(header: str) -> bool:
    """Check if column header is not a property.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header contains 'properties.'. Else returns false.

    """
    return header.startswith(DataFrameHeaders.PROPERTY_COLUMN_HEADER_PREFIX)


def __is_keywords_header(header: str) -> bool:
    """Check if column header is not a keywords.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header equals 'keywords'. Else returns false.

    """
    return header == DataFrameHeaders.KEYWORDS_COLUMN_HEADER


def __generate_condition_column_header(condition: Condition) -> str:
    """Generate column header for a condition.

    Args:
        condition: Condition object for generating column header.

    Returns:
        The column header for the given condition.
    """
    name = condition.name or ""
    unit = (
        f"({condition.value.unit})"
        if isinstance(condition.value, NumericConditionValue) and condition.value.unit
        else ""
    )

    return f"{DataFrameHeaders.CONDITION_COLUMN_HEADER_PREFIX}{name}{unit}"


def __serialize_condition_value(condition: Condition) -> List[str]:
    """Get ranges and discrete values of a condition.

    Args:
        condition: Condition for getting values.

    Returns:
        The list of values of the given condition in a specific format.
    """
    if not condition.value:
        return []

    values = []

    if isinstance(condition.value, NumericConditionValue):
        values.extend(__serialize_numeric_condition_range(value=condition.value))

    values.extend(__serialize_condition_discrete_values(value=condition.value))

    return values


def __serialize_numeric_condition_range(value: NumericConditionValue) -> List[str]:
    """Serialize ranges of a numeric condition value.

    Args:
        value: A condition's value with NumericConditionValue type.

    Returns:
        The list of ranges of the given condition where each range will be in
        string format `[min: <value>; max: <value>; step: <value>]` if the corresponding
        fields are not none.
    """
    if not value.range:
        return []

    return [
        "["
        + "; ".join(
            f"{range_key}: {range_value}"
            for range_key, range_value in vars(value_range).items()
            if range_value is not None
        )
        + "]"
        for value_range in value.range
    ]


def __serialize_condition_discrete_values(
    value: NumericConditionValue | StringConditionValue,
) -> List[str]:
    """Serialize discrete values of a value.

    Args:
        value: A condition's value with either NumericConditionValue type or StringConditionValue type.

    Returns:
        The list of discrete values of the given value in a string format.
    """
    return [str(discrete) for discrete in (value.discrete or [])]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/__init__.py sha256=c5a0b5193685a7a10115c554673a76dcd763534fbc6d02acc1e2f10bfb39144e bytes=165 -->
## FILE: nisystemlink/clients/systems/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/__init__.py`
- sha256: `c5a0b5193685a7a10115c554673a76dcd763534fbc6d02acc1e2f10bfb39144e`
- bytes: 165

````python
"""Start here with SystemsClient for system management."""

from nisystemlink.clients.systems._systems_client import SystemsClient

__all__ = ["SystemsClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/_systems_client.py sha256=d073cd49c3b8a9329e0278c6e5579ea52ae3ba3258e7e96da643b5e49aee79e8 bytes=2975 -->
## FILE: nisystemlink/clients/systems/_systems_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/_systems_client.py`
- sha256: `d073cd49c3b8a9329e0278c6e5579ea52ae3ba3258e7e96da643b5e49aee79e8`
- bytes: 2975

````python
"""Implementation of SystemsClient"""

from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import post
from uplink import Field, retry

from . import models


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class SystemsClient(BaseClient):

    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Systems Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/nisysmgmt/v1/")

    @post("virtual")
    def create_virtual_system(
        self, create_virtual_system_request: models.CreateVirtualSystemRequest
    ) -> models.CreateVirtualSystemResponse:
        """Creates a virtual system.

        Args:
            alias: The alias of the virtual system.
            workspace: The workspace to create the virtual system in.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` service or provided invalid
                arguments.
        """
        ...

    @post("query-systems")
    def query_systems(
        self, query: models.QuerySystemsRequest
    ) -> models.QuerySystemsResponse:
        """Queries for systems that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of systems.

        Returns:
            Response containing the list of systems that match the filter.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` Service or provided invalid
                arguments.
        """
        ...

    @post("remove-systems", args=[Field("tgt")])
    def remove_systems(self, tgt: List[str]) -> models.RemoveSystemsResponse:
        """Removes multiple systems.

        Args:
            virtual_system_to_remove : List of unique IDs of systems.

        Returns:
            A partial success if any systems failed to remove, or None if all
            systems were removed successfully.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` Service
                or provided an invalid argument.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/__init__.py sha256=35b3e858df8221da51fede4334b2b4f4e4ba29b6a9f45bcbb4f134467df2eccd bytes=573 -->
## FILE: nisystemlink/clients/systems/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/__init__.py`
- sha256: `35b3e858df8221da51fede4334b2b4f4e4ba29b6a9f45bcbb4f134467df2eccd`
- bytes: 573

````python
from nisystemlink.clients.systems.models._create_virtual_systems_request import (
    CreateVirtualSystemRequest,
)
from nisystemlink.clients.systems.models._create_virtual_systems_response import (
    CreateVirtualSystemResponse,
)
from nisystemlink.clients.systems.models._query_systems_request import (
    QuerySystemsRequest,
)
from nisystemlink.clients.systems.models._query_systems_response import (
    QuerySystemsResponse,
)
from nisystemlink.clients.systems.models._remove_systems_response import (
    RemoveSystemsResponse,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_create_virtual_systems_request.py sha256=1e29da406938bc073ef7f8492b09f3ab0b81b7933ccf7028fbc57d5761476b5c bytes=362 -->
## FILE: nisystemlink/clients/systems/models/_create_virtual_systems_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/_create_virtual_systems_request.py`
- sha256: `1e29da406938bc073ef7f8492b09f3ab0b81b7933ccf7028fbc57d5761476b5c`
- bytes: 362

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class CreateVirtualSystemRequest(JsonModel):
    """Model for create virtual system response containing the minion ID of the system which is created."""

    alias: str
    """Alias of the virtual system."""

    workspace: str
    """Workspace to create the virtual system in."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_create_virtual_systems_response.py sha256=c098957e583b15bb3d1f215db12b56b6229cb4e0a1e5c05dc6cf763684569d87 bytes=320 -->
## FILE: nisystemlink/clients/systems/models/_create_virtual_systems_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/_create_virtual_systems_response.py`
- sha256: `c098957e583b15bb3d1f215db12b56b6229cb4e0a1e5c05dc6cf763684569d87`
- bytes: 320

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class CreateVirtualSystemResponse(JsonModel):
    """Model for create virtual system response containing the minion ID of the system which is created."""

    minionId: str | None = None
    """The minion ID of the created virtual system."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_query_systems_request.py sha256=53562b90fbde0b70fc9beed10a7aa02556bdec405a1df671ed59d9376585ccb8 bytes=3522 -->
## FILE: nisystemlink/clients/systems/models/_query_systems_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/_query_systems_request.py`
- sha256: `53562b90fbde0b70fc9beed10a7aa02556bdec405a1df671ed59d9376585ccb8`
- bytes: 3522

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel


class QuerySystemsRequest(JsonModel):
    """Model for query systems request."""

    skip: int | None = None
    """Gets or sets the number of systems to skip."""

    take: int | None = None
    """Gets or sets number of systems to return maximum value is 1000."""

    filter: str | None = None
    """The systems query filter is dynamic LINQ format.

    `id` : String representing the ID of the system.
    `createdTimestamp`: ISO-8601 formatted timestamp string specifying the
    date when the system was registered.
    `lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system was updated.
    `alias`: String representing the alias of the system.
    `activation.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system activation was updated.
    `activation.data.activated`: Boolean representing whether the system is
    activated or not.
    `activation.data.licenseName`: String representing the name of the license.
    `activation.data.licenseVersion`: String representing the license version.
    `connected.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system connection was updated.
    `connected.data.state`: String representing the state of the system.
    `grains.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system grains were updated.
    `grains.data`: Dictionary of string to object representing general
    information about the system. Example: grains.data.os == "Windows"
    `packages.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system installed packages were updated.
    `packages.data`: Dictionary representing software packages installed on the
    system.
    Example: packages.data.ni-package-manager-upgrader.version: String
    representing the installed version of ni-package-manager-upgrader package.
    `feeds.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system configured feeds were updated.
    `feeds.data`: Dictionary representing the feeds configured on the system.
    `keywords.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system keywords were updated.
    `keywords.data`: Array of strings representing the keywords of the system.
    Example: keywords.data.Contains("test")
    `properties.lastUpdatedTimestamp`: ISO-8601 formatted timestamp string
    specifying the last date the system properties were updated.
    `properties.data`: Dictionary of string to string representing metadata
    information about a system. Example: properties.data.owner == "admin"
    `status.data.http_connected`: Boolean representing the status of the http
    connection to the master.

    See [Dynamic Linq](https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language)
    documentation for more details.

    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable."""

    projection: str | None = None
    """Gets or sets specifies the projection for resources.
    Use this field to receive specific properties of the model."""

    order_by: str | None = None
    """Gets or sets the order in which data returns."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_query_systems_response.py sha256=4c6d8572e6197b7bc6ab226088664c2bc7565670170c20019a46d583708b38b4 bytes=370 -->
## FILE: nisystemlink/clients/systems/models/_query_systems_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/_query_systems_response.py`
- sha256: `4c6d8572e6197b7bc6ab226088664c2bc7565670170c20019a46d583708b38b4`
- bytes: 370

````python
from typing import Any, Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class QuerySystemsResponse(JsonModel):
    """Model for query systems request."""

    count: int | None = None
    """Number of systems match the query."""

    data: List[Dict[str, Any]] | None = None
    """Contains info of the queried systems."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_remove_systems_response.py sha256=2dbc857b09149e7605a9e42b01609fab7e631c4edb926e5be9b2140087910f8b bytes=539 -->
## FILE: nisystemlink/clients/systems/models/_remove_systems_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/systems/models/_remove_systems_response.py`
- sha256: `2dbc857b09149e7605a9e42b01609fab7e631c4edb926e5be9b2140087910f8b`
- bytes: 539

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class RemoveSystemsResponse(JsonModel):
    """Model for remove systems response containing the IDs of the systems which were deleted."""

    jid: str | None = None
    """The job ID of the remove systems operation."""

    removed_ids: List[str] | None = None
    """The IDs of the systems that were successfully removed."""

    failed_ids: List[str] | None = None
    """The IDs of the systems that could not be removed."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/__init__.py sha256=9ab3fab1394598e5a89188082c710ae6d6896c5a31422c4b4152a178ef65a5ed bytes=1430 -->
## FILE: nisystemlink/clients/tag/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/__init__.py`
- sha256: `9ab3fab1394598e5a89188082c710ae6d6896c5a31422c4b4152a178ef65a5ed`
- bytes: 1430

````python
# -*- coding: utf-8 -*-

"""Start here with TagManager for tag operations and helper types."""

from ._data_type import DataType
from ._retention_type import RetentionType
from ._tag_data import TagData
from ._tag_with_aggregates import TagWithAggregates  # noqa: I100
from ._async_tag_query_result_collection import (  # noqa: I100
    AsyncTagQueryResultCollection,
)
from ._itag_reader import ITagReader
from ._itag_writer import ITagWriter
from ._buffered_tag_writer import BufferedTagWriter  # noqa: I100
from ._tag_value_reader import TagValueReader
from ._tag_value_writer import TagValueWriter
from ._tag_update_fields import TagUpdateFields  # noqa: I100
from ._tag_data_update import TagDataUpdate  # noqa: I100
from ._tag_path_utilities import TagPathUtilities
from ._tag_query_result_collection import TagQueryResultCollection
from ._tag_subscription import TagSubscription
from ._tag_selection import TagSelection  # noqa: I100
from ._tag_manager import TagManager  # noqa: I100

__all__ = [
    "DataType",
    "RetentionType",
    "TagData",
    "TagWithAggregates",
    "AsyncTagQueryResultCollection",
    "ITagReader",
    "ITagWriter",
    "BufferedTagWriter",
    "TagValueReader",
    "TagValueWriter",
    "TagUpdateFields",
    "TagDataUpdate",
    "TagPathUtilities",
    "TagQueryResultCollection",
    "TagSubscription",
    "TagSelection",
    "TagManager",
]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_async_tag_query_result_collection.py sha256=4d098b9dd82d1f692e108cc819ea05f3609d9bf3dceaccc3250c147003d06d8c bytes=3928 -->
## FILE: nisystemlink/clients/tag/_async_tag_query_result_collection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_async_tag_query_result_collection.py`
- sha256: `4d098b9dd82d1f692e108cc819ea05f3609d9bf3dceaccc3250c147003d06d8c`
- bytes: 3928

````python
# -*- coding: utf-8 -*-

"""Implementation of AsyncTagQueryResultCollection."""

import abc
from typing import List

from nisystemlink.clients import core, tag as tbase


class AsyncTagQueryResultCollection(abc.ABC):
    """Represents a paginated list of tags returned by an asynchronous query."""

    def __init__(
        self, first_page: List[tbase.TagData], total_count: int, skip: int
    ) -> None:
        """Initialize an instance with the first page of query results.

        Args:
            first_page: The first page of results, or None if there are no results.
            total_count: The total number of results in the query.
            skip: The skip used for the first page of results.
        """
        self._total_count = total_count
        self._current_page: List[tbase.TagData] | None = None
        if first_page:
            if skip >= total_count:
                raise core.ApiException(
                    "skip is >= totalCount, but the tag list isn't empty"
                )
            self._current_page = first_page
        else:
            pass  # leave it as None, even if passed in as []
        self._skip = skip
        self._current_skip = skip

    @property
    def current_page(self) -> List[tbase.TagData] | None:  # noqa: D401
        """The current page of tag results that were last retrieved from the server, or
        None if there are no more results.

        Use :meth:`move_next_page_async()` to get the next page of results.
        """
        return self._current_page

    @property
    def total_count(self) -> int:  # noqa: D401
        """The total number of tags matched by the query at the time the query was made."""
        return self._total_count

    async def move_next_page_async(self) -> List[tbase.TagData] | None:
        """Asynchronously retrieve the next page of query results from the server,
        returning them and updating :attr:`current_page`.

        Does nothing if the last page has already been retrieved. Use
        :meth:`reset_async()` to start again from the first page.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            next page of results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        """
        if self._current_page is None:
            return None

        new_skip = self._current_skip + len(self._current_page)
        if new_skip < self.total_count:
            self._current_page = await self._query_page_async(new_skip)
        else:
            self._current_page = None

        self._current_skip = new_skip
        return self._current_page

    async def reset_async(self) -> List[tbase.TagData]:
        """Asynchronously query the server for a fresh set of results, returning the
        first page and updating :attr:`current_page` and :attr:`total_count`.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            first page of results, or None if there are no results.

        Raises:
            ApiException: if the API call fails.
        """
        self._current_skip = self._skip
        self._current_page = await self._query_page_async(self._current_skip)
        return self._current_page

    @abc.abstractmethod
    async def _query_page_async(self, skip: int) -> List[tbase.TagData]:
        """Asynchronously query for a single page of results and updates :attr:`total_count`.

        Args:
            skip: The skip to use in the query.

        Returns:
            A task representing the asynchronous operation. On completion, the page of
            results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_buffered_tag_writer.py sha256=ac224864091a9d312dedb35ed39e39d6f2f2892926d41d5315ba821da0c22af7 bytes=13502 -->
## FILE: nisystemlink/clients/tag/_buffered_tag_writer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_buffered_tag_writer.py`
- sha256: `ac224864091a9d312dedb35ed39e39d6f2f2892926d41d5315ba821da0c22af7`
- bytes: 13502

````python
# -*- coding: utf-8 -*-

"""Implementation of BufferedTagWriter."""

import abc
import datetime
import sys
import threading
from types import TracebackType
from typing import Any, Callable, Type

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.tag._core._itime_stamper import ITimeStamper
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer


class BufferedTagWriter(tbase.ITagWriter):
    """Represents an :class:`ITagWriter` that buffers tag writes instead of sending them immediately.

    Writes that utilize automatic timestamps are based on the system time when buffered.
    Implementations may provide automatic sending of buffered writes based on different
    conditions. Unsent writes are discarded when the instance is deleted.

    Note that :class:`BufferedTagWriter` objects support using the ``with`` statement
    (or the ``async with`` statement), to automatically :meth:`send
    <send_buffered_writes>` any remaining buffered writes on exit.
    """

    def __init__(
        self, stamper: ITimeStamper, buffer_size: int, flush_timer: ManualResetTimer
    ) -> None:
        """Initialize the writer.

        Args:
            stamper: An object for time-stamping tag writes.
            buffer_size: The maximum number of tag writes to buffer before automatically
                sending them to the server.
            flush_timer: A timer that, once started, elapses whenever buffered writes
                should be sent automatically. Does not have to be a configured timer.
        """
        self._lock = threading.Lock()
        self._buffer_limit = buffer_size
        self._flush_timer = flush_timer
        self._stamper = stamper

        self._closed = False
        self._num_buffered = 0
        self._send_error: core.ApiException | None = None
        self._timer_generation = 0
        self._timer_handler: Callable[[], None] | None = None

    @abc.abstractmethod
    def _buffer_value(self, path: str, value: Any) -> None:
        """Add a value to the buffer.

        Args:
            path: The tag path being written.
            value: The value being written.
        """
        ...

    @abc.abstractmethod
    def _clear_buffer(self) -> None:
        """Clear the buffer of writes."""
        ...

    @abc.abstractmethod
    def _copy_buffer(self) -> Any:
        """Return the contents of the buffer and clears or replaces the buffer used for future writes.

        Returns:
            The buffered data.
        """
        ...

    @abc.abstractmethod
    def _create_item(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> Any:
        """Return an item that can be placed into the buffer.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: The timestamp represented as a nullable ``datetime.datetime``.

        Returns:
            The created item.

        Raises:
            ValueError: if ``data_type`` is not supported for writing.
        """
        ...

    @abc.abstractmethod
    def _send_writes(self, updates: Any) -> None:
        """Send the writes stored in ``updates`` to the server.

        Args:
            updates: The writes to send.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _send_writes_async(self, updates: Any) -> None:
        """Asynchronously send the writes stored in ``updates`` to the server.

        Args:
            updates: The writes to send.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    def clear_buffered_writes(self) -> None:
        """Clear any pending writes from :meth:`write()`.

        Raises:
            ReferenceError: if the writer has been closed.
        """
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        with self._lock:
            self._stop_timer_while_locked()
            self._clear_buffer()
            self._num_buffered = 0

    def send_buffered_writes(self) -> None:
        """Write all of the pending writes from :meth:`write()` to the server.

        Does nothing if there are no pending writes.

        Raises:
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        with self._lock:
            updates = self._retrieve_buffered_values_while_locked()

        if updates is not None:
            self._send_writes(updates)

    async def send_buffered_writes_async(self) -> None:
        """Asynchronously write all of the pending writes from :meth:`write()` to the server.

        Does nothing if there are no pending writes.

        Raises:
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        with self._lock:
            updates = self._retrieve_buffered_values_while_locked()

        if updates is not None:
            await self._send_writes_async(updates)

    def __enter__(self) -> "BufferedTagWriter":
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        self._flush_timer.__enter__()
        return self

    async def __aenter__(self) -> "BufferedTagWriter":
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        await self._flush_timer.__aenter__()
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        if self._closed:
            return False

        self.send_buffered_writes()
        self._closed = True

        suppress = self._flush_timer.__exit__(exc_type, exc_val, exc_tb)
        return suppress

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        if self._closed:
            return False

        await self.send_buffered_writes_async()
        self._closed = True

        suppress = await self._flush_timer.__aexit__(exc_type, exc_val, exc_tb)
        return suppress

    def _write(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> None:
        """Write a tag's value that's been serialized to a string.

        Clients do not typically call this method directly. Use a
        :class:`.TagValueWriter` instead.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if `path` is empty or invalid.
            ValueError: if `path` or `value` is None.
            ValueError: if `data_type` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        timestamped_value = self._prepare_write(path, data_type, value, timestamp)

        pending_error = None
        updates = None
        with self._lock:
            self._buffer_value(path, timestamped_value)
            self._num_buffered += 1

            if self._num_buffered == self._buffer_limit:
                updates = self._retrieve_buffered_values_while_locked()
            elif self._num_buffered == 1:
                self._start_timer_while_locked()

            if self._send_error is not None:
                pending_error = self._send_error
                self._send_error = None

        if updates is not None:
            self._send_writes(updates)

        if pending_error:
            raise pending_error

    async def _write_async(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> None:
        """Asynchronously write a tag's value that's been serialized to a string.

        Clients do not typically call this method directly. Use a
        :class:`.TagValueWriter` instead.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if `path` is empty or invalid.
            ValueError: if `path` or `value` is None.
            ValueError: if `data_type` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        timestamped_value = self._prepare_write(path, data_type, value, timestamp)

        pending_error = None
        updates = None
        with self._lock:
            self._buffer_value(path, timestamped_value)
            self._num_buffered += 1

            if self._num_buffered == self._buffer_limit:
                updates = self._retrieve_buffered_values_while_locked()
            elif self._num_buffered == 1:
                self._start_timer_while_locked()

            if self._send_error is not None:
                pending_error = self._send_error
                self._send_error = None

        if updates is not None:
            await self._send_writes_async(updates)

        if pending_error:
            raise pending_error

    def _prepare_write(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> Any:
        if self._closed:
            raise ReferenceError("BufferedTagWriter")

        if value is None:
            raise ValueError("value is None")

        if data_type == tbase.DataType.UNKNOWN:
            raise ValueError("data_type is UNKNOWN")

        if timestamp is None:
            timestamp = self._stamper.timestamp
        else:
            if timestamp.tzinfo is None and sys.version_info < (3, 6):
                # python 3.5's .astimezone fails if given a naive datetime, so use a
                # roundabout method; python 3.6+ allow naive datetimes and assume a
                # local timezone, so allow the same here
                timestamp = datetime.datetime.fromtimestamp(
                    timestamp.timestamp(), datetime.timezone.utc
                )
            else:
                timestamp = timestamp.astimezone(datetime.timezone.utc)
        return self._create_item(
            tbase.TagPathUtilities.validate(path), data_type, value, timestamp
        )

    def _retrieve_buffered_values_while_locked(self) -> Any:
        """Return the buffered values, if any, and clears the buffer.

        Must hold :attr:`_lock`.

        Returns:
            The buffered values, or None if there aren't any.
        """
        self._stop_timer_while_locked()

        if self._num_buffered == 0:
            return None

        buffer = self._copy_buffer()
        self._num_buffered = 0
        return buffer

    def _start_timer_while_locked(self) -> None:
        """Start the flush timer, if configured.

        Must hold :attr:`_lock`.
        """
        if not self._flush_timer.can_start:
            return

        handler_generation = self._timer_generation
        self._flush_timer.elapsed -= self._timer_handler
        self._timer_handler = lambda: self._timer_expired(handler_generation)
        self._flush_timer.elapsed += self._timer_handler
        self._flush_timer.start()

    def _stop_timer_while_locked(self) -> None:
        """Stop the flush timer, if configured.

        Must hold :attr:`_lock`.
        """
        self._flush_timer.stop()
        self._timer_generation += 1

    def _timer_expired(self, generation: int) -> None:
        if self._closed:
            return

        with self._lock:
            if generation != self._timer_generation:
                # The timer was canceled after we were already queued.
                return

            updates = self._retrieve_buffered_values_while_locked()

        if updates is not None:
            try:
                self._send_writes(updates)
            except core.ApiException as ex:
                with self._lock:
                    self._send_error = ex
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: nisystemlink/clients/tag/_core/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_itime_stamper.py sha256=51e99ce869192630ce942bc0d61465dc6d0ade8801e01cb23e5f8bc87de01d09 bytes=507 -->
## FILE: nisystemlink/clients/tag/_core/_itime_stamper.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/_itime_stamper.py`
- sha256: `51e99ce869192630ce942bc0d61465dc6d0ade8801e01cb23e5f8bc87de01d09`
- bytes: 507

````python
# -*- coding: utf-8 -*-

"""Implementation of ITimeStamper."""

import abc
import datetime


class ITimeStamper(abc.ABC):
    """Represents an object for time-stamping objects or actions such that no two
    timestamps returned by the instance are within the same microsecond.
    """

    @property
    @abc.abstractmethod
    def timestamp(self) -> datetime.datetime:  # noqa: D401
        """A unique UTC ``datetime.datetime`` that is close to the current date and time."""
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_manual_reset_timer.py sha256=d73f6bba3a5072e0a267f3d9568e2c08b5d5b7d39e2eb141cf06969e15b23309 bytes=5918 -->
## FILE: nisystemlink/clients/tag/_core/_manual_reset_timer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/_manual_reset_timer.py`
- sha256: `d73f6bba3a5072e0a267f3d9568e2c08b5d5b7d39e2eb141cf06969e15b23309`
- bytes: 5918

````python
# -*- coding: utf-8 -*-

"""Implementation of ManualResetTimer."""

import datetime
import threading
import traceback
from types import TracebackType
from typing import Any, Callable, List, Type

import events
from nisystemlink.clients.core._internal._classproperty_support import (
    ClasspropertySupport,
)
from typing_extensions import final, Literal


@final
class ManualResetTimer(events.Events, metaclass=ClasspropertySupport):
    """Represents a timer for periodic background operations such that :meth:`start()`
    must be called to restart the timer each time the :attr:`elapsed` event is raised.

    Attributes:
        elapsed: An event that is triggered when the timer has elapsed.

    Example::

        def timer_elapsed():
            print("The timer elapsed!")

        my_timer.elapsed += timer_elapsed
    """

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'ManualResetTimer' is not an acceptable base type")

    __events__ = ["elapsed"]
    # Under certain circumstances, mypy complains about the event not having a type hint
    # unless we specify it explicitly. (But we also need to delete the attribute so that
    # Events.__getattr__ can do its magic.)
    elapsed = None  # type: events._EventSlot
    del elapsed

    __null_timer_impl: "ManualResetTimer | None" = None

    @ClasspropertySupport.classproperty
    def null_timer(cls) -> "ManualResetTimer":
        """A timer that never fires."""
        if cls.__null_timer_impl is None:
            # Bypass the ManualResetTimer constructor, to make a timerless timer
            obj = cls.__new__(ManualResetTimer)
            super(ManualResetTimer, obj).__init__()  # but call the base constructor

            obj._thread = None
            obj._running = []  # used as mutable boolean; empty is False

            cls.__null_timer_impl = obj
        return cls.__null_timer_impl

    def __init__(self, interval: datetime.timedelta) -> None:
        """Initialize a timer that fires at the given interval a single time once
        :meth:`start()` has been called and then automatically stops.

        Args:
            interval: The amount of time after calling :meth:`start()` before
                :attr:`elapsed` is raised.

        Raises:
            ValueError: if ``interval`` is less than or equal to zero.
        """
        super().__init__()
        interval_secs = interval.total_seconds()
        if interval_secs <= 0:
            raise ValueError("interval cannot be <= 0")

        # Note: This _running flag means that the *thread* is running, not the timer
        self._running = [None]  # used as mutable boolean; non-empty is True
        self._timer_start = threading.Event()
        self._timer_cancel = threading.Event()
        self._thread: threading.Thread | None = threading.Thread(
            target=self._run,
            args=[
                self._running,
                interval_secs,
                self._timer_start,
                self._timer_cancel,
                self.elapsed,
            ],
        )
        self._thread.daemon = True
        self._thread.start()

    @property
    def can_start(self) -> bool:  # noqa: D401
        """Whether or not the timer is configured and can be started.

        A timer that isn't configured will never raise :attr:`elapsed`, even when
        :meth:`start()` is called.
        """
        return self._thread is not None

    def start(self) -> None:
        """Start the timer."""
        if self._running:
            self._timer_cancel.clear()
            self._timer_start.set()

    def stop(self) -> None:
        """Stop the timer."""
        if self._running:
            self._timer_cancel.set()

    @staticmethod
    def _run(
        running: List[None],
        interval: int,
        timer_start: threading.Event,
        timer_cancel: threading.Event,
        elapsed: Callable[[], None],
    ) -> None:
        while running:
            timer_start.wait()
            timer_start.clear()
            if running and not timer_cancel.wait(interval):
                try:
                    elapsed()
                except Exception:
                    traceback.print_exc()

    def __enter__(self) -> "ManualResetTimer":
        return self

    async def __aenter__(self) -> "ManualResetTimer":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[False]:
        self.stop()
        for handler in list(self.elapsed):
            self.elapsed -= handler
        return False

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[False]:
        self.stop()
        for handler in list(self.elapsed):
            self.elapsed -= handler
        return False

    def __del__(self) -> None:
        self.stop()
        for handler in list(self.elapsed):
            self.elapsed -= handler

        # Stop the thread
        if self._running:
            self._running.clear()  # set our "mutable boolean" to False
            self._thread = None
            self._timer_cancel.set()
            self._timer_start.set()

    # Work around https://github.com/pyeve/events/issues/17
    def __getattr__(self, name: str) -> Any:
        if name in self.__events__:
            return super().__getattr__(name)
        else:
            return object.__getattribute__(self, name)

    # Fake method to tell mypy the type of our events
    def __type_hinting__(self) -> None:
        self.elapsed = type(self).elapsed  # type: events._EventSlot
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py sha256=553e8205aab59d5a4bcfe4cf9db1e7ed7f68742e9cb5ad1d8ea261466f92c031 bytes=3989 -->
## FILE: nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py`
- sha256: `553e8205aab59d5a4bcfe4cf9db1e7ed7f68742e9cb5ad1d8ea261466f92c031`
- bytes: 3989

````python
# -*- coding: utf-8 -*-

"""Implementation of SerializedTagWithAggregates."""

import datetime

from nisystemlink.clients import tag as tbase
from typing_extensions import final


@final
class SerializedTagWithAggregates:
    """Represents a generic tag value serialized to a string with optional aggregate
    values also serialized to a string.

    Clients typically do not interact with this instances of this class directly. Use a
    :class:`.TagValueReader` instead.
    """

    def __init_subclass__(cls) -> None:
        raise TypeError(
            "type 'SerializedTagWithAggregates' is not an acceptable base type"
        )

    def __init__(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
        count: int | None = None,
        min: str | None = None,
        max: str | None = None,
        mean: float | None = None,
    ) -> None:
        """Initialize an instance.

        Args:
            path: The path of the tag associated with the value.
            data_type: The data type of the value serialized as a string.
            value: The value serialized as a string.
            timestamp: The timestamp associated with the value.
            count: The number of times the tag has been written, or None if the tag is
                not collecting aggregates.
            min: The minimum value of the tag serialized to a string, or None if the tag
                is not collecting aggregates or the data type of the tag does not track
                a minimum value.
            max: The maximum value of the tag serialized to a string, or None if the tag
                is not collecting aggregates or the data type of the tag does not track
                a maximum value.
            mean: The mean value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a mean value.
        """
        self._path = path
        self._data_type = data_type
        self._value = value
        self._timestamp = timestamp
        self._count = count
        self._min = min
        self._max = max
        self._mean = mean

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type of the value that was serialized as a string."""
        return self._data_type

    @property
    def path(self) -> str:  # noqa: D401
        """The path of the tag associated with the value."""
        return self._path

    @property
    def value(self) -> str:  # noqa: D401
        """The value of the tag serialized as a string."""
        return self._value

    @property
    def timestamp(self) -> datetime.datetime | None:  # noqa: D401
        """The timestamp associated with the value, if available."""
        return self._timestamp

    @property
    def count(self) -> int | None:  # noqa: D401
        """The number of times the tag has been written, or None if the tag is not collecting aggregates."""
        return self._count

    @property
    def min(self) -> str | None:  # noqa: D401
        """The minimum value of the tag serialized to a string, or None if the tag is
        not collecting aggregates or the data type of the tag does not track a minimum
        value.
        """
        return self._min

    @property
    def max(self) -> str | None:  # noqa: D401
        """The maximum value of the tag serialized to a string, or None if the tag is
        not collecting aggregates or the data type of the tag does not track a maximum
        value.
        """
        return self._max

    @property
    def mean(self) -> float | None:  # noqa: D401
        """The mean value of the tag, or None if the tag is not collecting aggregates or
        the data type of the tag does not track a mean value.
        """
        return self._mean
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py sha256=8627c7f30df6ac31e440bfe0dde6b0039d30ed91dc5c1b13d6192ee59a01a7b7 bytes=3100 -->
## FILE: nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py`
- sha256: `8627c7f30df6ac31e440bfe0dde6b0039d30ed91dc5c1b13d6192ee59a01a7b7`
- bytes: 3100

````python
# -*- coding: utf-8 -*-

"""Implementation of SerializedTagWithAggregatesReader."""

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)
from typing_extensions import final


@final
class SerializedTagWithAggregatesReader(tbase.ITagReader):
    """Represents an :class:`.ITagReader` wrapping a single :class:`SerializedTagWithAggregates`."""

    def __init_subclass__(cls) -> None:
        raise TypeError(
            "type 'SerializedTagWithAggregatesReader' is not an acceptable base type"
        )

    def __init__(self, value: SerializedTagWithAggregates) -> None:
        """Initialize a reader instance for the given value.

        Args:
            value: The value to wrap in a reader.

        Raises:
            ValueError: if ``value`` is None.
        """
        if value is None:
            raise ValueError("value cannot be None")
        self._value = value

    def _read(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.
        """
        if self._value.path == path:
            return self._value
        else:
            return None

    async def _read_async(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.
        """
        if self._value.path == path:
            return self._value
        else:
            return None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_system_time_stamper.py sha256=94a09414984daa5098a4cff3d0949fe124e85562b638bb67018a338cec37d31b bytes=1100 -->
## FILE: nisystemlink/clients/tag/_core/_system_time_stamper.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_core/_system_time_stamper.py`
- sha256: `94a09414984daa5098a4cff3d0949fe124e85562b638bb67018a338cec37d31b`
- bytes: 1100

````python
# -*- coding: utf-8 -*-

"""Implementation of SystemTimeStamper."""

import datetime
import threading

from nisystemlink.clients.tag._core._itime_stamper import ITimeStamper
from typing_extensions import final


@final
class SystemTimeStamper(ITimeStamper):
    """A :class:`ITimeStamper` that uses the system clock."""

    _increment = datetime.timedelta(microseconds=1)

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'SystemTimeStamper' is not an acceptable base type")

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._last = datetime.datetime.now(datetime.timezone.utc)

    @property
    def timestamp(self) -> datetime.datetime:  # noqa: D401
        """A unique UTC ``datetime.datetime`` that is close to the current date and time."""
        timestamp = datetime.datetime.now(datetime.timezone.utc)

        with self._lock:
            if timestamp > self._last:
                self._last = timestamp
            else:
                self._last += self._increment
            return self._last
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_data_type.py sha256=18183b408ce8b1305da249b66038d66b3c8d7abee637f7c4139f1d75bd1d3b49 bytes=2131 -->
## FILE: nisystemlink/clients/tag/_data_type.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_data_type.py`
- sha256: `18183b408ce8b1305da249b66038d66b3c8d7abee637f7c4139f1d75bd1d3b49`
- bytes: 2131

````python
# -*- coding: utf-8 -*-

"""Implementation of DataType."""

import enum


class DataType(enum.Enum):
    """Represents the different data types for a SystemLink tag."""

    UNKNOWN = 0
    """An unknown or invalid data type.

    Not a valid input to API calls, but used to represent tags whose data type isn't
    recognized.
    """

    DOUBLE = 1
    """A 64-bit floating-point tag following the IEEE standard.

    Double tags support collecting aggregate values for the min, max, mean, and count.
    """

    INT32 = 2
    """A 32-bit signed integer tag.

    Int32 tags support collecting aggregate values for the min, max, mean, and count.
    The mean is represented as a double.
    """

    STRING = 3
    """A string tag for arbitrary values.

    String tags support collecting aggregate values for the count.
    """

    BOOLEAN = 4
    """A boolean tag.

    Bool tags support collecting aggregate values for the count.
    """

    UINT64 = 5
    """A 64-bit unsigned integer tag.

    UInt64 tags support collecting aggregate values for the min, max, mean, and count.
    The mean is represented as a double value and will truncate large values.
    """

    DATE_TIME = 6
    """A date and time tag that stores values in UTC ISO 8601 format.

    DateTime tags support collecting aggregate values for the count.
    """

    @property
    def api_name(self) -> str:
        """Web API name of the enum value."""
        return _API_NAME[self]

    @classmethod
    def from_api_name(cls, name: str) -> "DataType":
        return cls(_FROM_API_NAME.get(name, cls.UNKNOWN))


_API_NAME = {
    DataType.UNKNOWN: "UNKNOWN",
    DataType.DOUBLE: "DOUBLE",
    DataType.INT32: "INT",
    DataType.STRING: "STRING",
    DataType.BOOLEAN: "BOOLEAN",
    DataType.UINT64: "U_INT64",
    DataType.DATE_TIME: "DATE_TIME",
}

_FROM_API_NAME = {
    "DOUBLE": DataType.DOUBLE,
    "INT": DataType.INT32,
    "STRING": DataType.STRING,
    "BOOLEAN": DataType.BOOLEAN,
    "U_INT64": DataType.UINT64,
    "DATE_TIME": DataType.DATE_TIME,
}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: nisystemlink/clients/tag/_http/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py sha256=11382575865e88b12022e0b94da2a94645fffd3366e7bedc98555b3d5db061c5 bytes=2647 -->
## FILE: nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py`
- sha256: `11382575865e88b12022e0b94da2a94645fffd3366e7bedc98555b3d5db061c5`
- bytes: 2647

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpAsyncTagQueryResultCollection."""

from typing import Any, Awaitable, Dict, List, Tuple

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient, HttpResponse
from typing_extensions import final


@final
class HttpAsyncTagQueryResultCollection(tbase.AsyncTagQueryResultCollection):
    def __init_subclass__(cls) -> None:
        raise TypeError(
            "type 'HttpAsyncTagQueryResultCollection' is not an acceptable base type"
        )

    def __init__(
        self,
        client: HttpClient,
        paths: str | None,
        keywords: str | None,
        properties: str | None,
        skip: int,
        take: int | None,
        tag_query_result: Dict[str, Any],
        http_response: HttpResponse,
    ) -> None:
        first_page, total_count = self.__handle_query_response(
            tag_query_result, http_response
        )
        super().__init__(first_page, total_count, skip)

        api = client.at_uri("/nitag/v2")
        base_params = {
            "path": paths,
            "keywords": keywords,
            "properties": properties,
            "skip": "0",
            "take": str(take) if take is not None else None,
        }
        for k, v in list(base_params.items()):
            if v is None:
                del base_params[k]

        def query(s: int) -> Awaitable[Tuple[Dict[str, Any], HttpResponse]]:
            params = dict(base_params)
            params["skip"] = str(s)
            return api.as_async.get("/tags", params=params)

        self._query = query

    async def _query_page_async(self, skip: int) -> List[tbase.TagData]:
        page, self._total_count = self.__handle_query_response(
            *(await self._query(skip))
        )
        return page

    def __handle_query_response(
        self, response: Dict[str, Any], http_response: HttpResponse
    ) -> Tuple[List[tbase.TagData], int]:
        if response.get("totalCount") is None:
            raise tbase.TagManager.invalid_response(http_response)

        tags = []
        for t in response["tags"]:
            tags.append(
                tbase.TagData(
                    t["path"],
                    tbase.DataType.from_api_name(t["type"]) if t["type"] else None,
                    t.get("keywords"),
                    t.get("properties"),
                )
            )
            if t.get("collectAggregates"):
                tags[-1].collect_aggregates = True
        return tags, response["totalCount"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py sha256=2cd472dc594b48c4c4f48aa40f0d3f114decd5df4164563e83646d7e2d83cace bytes=2349 -->
## FILE: nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py`
- sha256: `2cd472dc594b48c4c4f48aa40f0d3f114decd5df4164563e83646d7e2d83cace`
- bytes: 2349

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpBufferedTagWriter."""

import datetime
from collections import OrderedDict
from typing import Any, Dict

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._itime_stamper import ITimeStamper
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from typing_extensions import final


@final
class HttpBufferedTagWriter(tbase.BufferedTagWriter):
    def __init_subclass__(cls) -> None:
        raise TypeError("type 'HttpBufferedTagWriter' is not an acceptable base type")

    def __init__(
        self,
        client: HttpClient,
        stamper: ITimeStamper,
        buffer_size: int,
        flush_timer: ManualResetTimer,
    ) -> None:
        super().__init__(stamper, buffer_size, flush_timer)
        self._api = client.at_uri("/nitag/v2")
        self._buffer: OrderedDict[str, Dict[str, Any]] = OrderedDict()

    def _buffer_value(self, path: str, value: Dict[str, Any]) -> None:
        if path not in self._buffer:
            self._buffer.setdefault(path, {"path": path, "updates": []})
        self._buffer[path]["updates"].append(value)

    def _clear_buffer(self) -> None:
        self._buffer.clear()

    def _copy_buffer(self) -> Dict[str, Dict[str, Any]]:
        updates = self._buffer
        self._buffer = OrderedDict()
        return updates

    def _create_item(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> Dict[str, Any]:
        item: Dict[str, Any] = {"value": {"value": value, "type": data_type.api_name}}
        if timestamp is not None:
            item["timestamp"] = TimestampUtilities.datetime_to_str(timestamp)
        return item

    def _send_writes(self, updates: Dict[str, Dict[str, Any]]) -> None:
        self._api.post("/update-current-values", data=list(updates.values()))

    async def _send_writes_async(self, updates: Dict[str, Any]) -> None:
        await self._api.as_async.post(
            "/update-current-values", data=list(updates.values())
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py sha256=92eade5e55c5c7bdbe1b445320dcf6a3de3be303ce90d1d4a320c5691d5ac7c1 bytes=2552 -->
## FILE: nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py`
- sha256: `92eade5e55c5c7bdbe1b445320dcf6a3de3be303ce90d1d4a320c5691d5ac7c1`
- bytes: 2552

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpTagQueryResultCollection."""

from typing import Any, Dict, List, Tuple

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient, HttpResponse
from typing_extensions import final


@final
class HttpTagQueryResultCollection(tbase.TagQueryResultCollection):
    def __init_subclass__(cls) -> None:
        raise TypeError(
            "type 'HttpTagQueryResultCollection' is not an acceptable base type"
        )

    def __init__(
        self,
        client: HttpClient,
        paths: str | None,
        keywords: str | None,
        properties: str | None,
        skip: int,
        take: int | None,
        tag_query_result: Dict[str, Any],
        http_response: HttpResponse,
    ) -> None:
        first_page, total_count = self.__handle_query_response(
            tag_query_result, http_response
        )
        super().__init__(first_page, total_count, skip)

        api = client.at_uri("/nitag/v2")
        base_params = {
            "path": paths,
            "keywords": keywords,
            "properties": properties,
            "skip": "0",
            "take": str(take) if take is not None else None,
        }
        for k, v in list(base_params.items()):
            if v is None:
                del base_params[k]

        def query(s: int) -> Tuple[Dict[str, Any], HttpResponse]:
            params = dict(base_params)
            params["skip"] = str(s)
            return api.get("/tags", params=params)

        self._query = query

    def _query_page(self, skip: int) -> List[tbase.TagData]:
        page, self._total_count = self.__handle_query_response(*self._query(skip))
        return page

    def __handle_query_response(
        self, response: Dict[str, Any], http_response: HttpResponse
    ) -> Tuple[List[tbase.TagData], int]:
        if response.get("totalCount") is None:
            raise tbase.TagManager.invalid_response(http_response)

        tags = []
        for t in response["tags"]:
            tags.append(
                tbase.TagData(
                    t["path"],
                    tbase.DataType.from_api_name(t["type"]) if t["type"] else None,
                    t.get("keywords"),
                    t.get("properties"),
                )
            )
            if t.get("collectAggregates"):
                tags[-1].collect_aggregates = True
        return tags, response["totalCount"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_selection.py sha256=7ee36a076714d3e3a61b5f50a91f54574d6da971babc8b330f4a6bb0f1f8b61a bytes=15750 -->
## FILE: nisystemlink/clients/tag/_http/_http_tag_selection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_http_tag_selection.py`
- sha256: `7ee36a076714d3e3a61b5f50a91f54574d6da971babc8b330f4a6bb0f1f8b61a`
- bytes: 15750

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpTagSelection."""

import datetime
from typing import Any, Awaitable, Callable, List, Sequence, Tuple, TypeVar

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient, HttpResponse
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)
from nisystemlink.clients.tag._http._http_tag_subscription import HttpTagSubscription
from typing_extensions import final

T = TypeVar("T")


@final
class HttpTagSelection(tbase.TagSelection):
    def __init_subclass__(cls) -> None:
        raise TypeError("type 'HttpTagSelection' is not an acceptable base type")

    def __init__(
        self,
        client: HttpClient,
        tags: Sequence[tbase.TagData],
        *,
        _paths: Sequence[str] | None = None
    ) -> None:
        """Initialize a selection using existing data.

        Args:
            client: The HTTP client object for communicating with the server.
            tags: The tags to store in the selection.

        Raises:
            ValueError: if ``tags`` contains tags that are None or have invalid paths.
            ValueError: if ``tags`` contains duplicate tags.
            ValueError: if ``tags`` is None.
        """
        super().__init__(tags, _paths)
        self._client = client
        self._api = client.at_uri("/nitag/v2/selections")
        self._selection_stale = False
        self._token = None  # str | None

    @classmethod
    def open(cls, client: HttpClient, paths: Sequence[str]) -> "HttpTagSelection":
        """Initialize a selection using queried data.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The paths used in the query.

        Returns:
            The created selection.

        Raises:
            ValueError: if ``paths`` is None.
            ValueError: if ``paths`` contains duplicate paths.
            ApiException: if the API call fails.
        """
        api = client.at_uri("/nitag/v2/selections")

        selection, http_response = api.post("", data={"searchPaths": list(paths)})

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        token = selection["id"]

        try:
            tags, http_response = api.get("/{id}/tags", params={"id": token})

            if tags is None:
                raise tbase.TagManager.invalid_response(http_response)

            selection = HttpTagSelection(
                client, [tbase.TagData.from_json_dict(t) for t in tags], _paths=paths
            )
            selection._token = token
            return selection
        except core.ApiException:
            try:
                api.delete("/{id}", params={"id": token})
            except core.ApiException:
                pass

            raise

    @classmethod
    async def open_async(
        cls, client: HttpClient, paths: Sequence[str]
    ) -> "HttpTagSelection":
        """Asynchronously initialize a selection using queried data.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The paths used in the query.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created selection.

        Raises:
            ValueError: if ``paths`` is None.
            ValueError: if ``paths`` contains duplicate paths.
            ApiException: if the API call fails.
        """
        api = client.at_uri("/nitag/v2/selections").as_async

        selection, http_response = await api.post("", data={"searchPaths": list(paths)})

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        token = selection["id"]

        try:
            tags, http_response = await api.get("/{id}/tags", params={"id": token})

            if tags is None:
                raise tbase.TagManager.invalid_response(http_response)

            selection = HttpTagSelection(
                client, [tbase.TagData.from_json_dict(t) for t in tags], _paths=paths
            )
            selection._token = token
            return selection
        except core.ApiException:
            try:
                await api.delete("/{id}", params={"id": token})
            except core.ApiException:
                pass

            raise

    def _on_paths_changed(self) -> None:
        self._selection_stale = True

    def _close_internal(self) -> None:
        if self._token is None:
            return

        try:
            self._api.delete("/{id}", params={"id": self._token})
        except core.ApiException:
            pass

    async def _close_internal_async(self) -> None:
        if self._token is None:
            return

        try:
            await self._api.as_async.delete("/{id}", params={"id": self._token})
        except core.ApiException:
            pass

    def _create_subscription_internal(
        self, update_interval: datetime.timedelta | None = None
    ) -> tbase.TagSubscription:
        update_timer: ManualResetTimer | None = None
        if update_interval is not None:
            update_timer = ManualResetTimer(update_interval)
        paths = set(self.paths).union(self.metadata.keys())
        return HttpTagSubscription.create(
            self._client, paths, update_timer, heartbeat_timer=None
        )

    async def _create_subscription_internal_async(
        self, update_interval: datetime.timedelta | None = None
    ) -> tbase.TagSubscription:
        update_timer: ManualResetTimer | None = None
        if update_interval is not None:
            update_timer = ManualResetTimer(update_interval)
        paths = set(self.paths).union(self.metadata.keys())
        return await HttpTagSubscription.create_async(
            self._client, paths, update_timer, heartbeat_timer=None
        )

    def _delete_tags_from_server_internal(self) -> None:
        def fn(token: str) -> None:
            self._api.delete("/{id}/tags", params={"id": token})

        self._ensure_selection_and_call(fn)

    async def _delete_tags_from_server_internal_async(self) -> None:
        def fn(token: str) -> Awaitable[Tuple[None, HttpResponse]]:
            return self._api.as_async.delete("/{id}/tags", params={"id": token})

        await self._ensure_selection_and_call_async(fn)

    def _read_tag_metadata(self) -> List[tbase.TagData]:
        def fn(token: str) -> Tuple[Any, HttpResponse]:
            return self._api.get("/{id}/tags", params={"id": token})

        response, http_response = self._ensure_selection_and_call(fn)
        return self._handle_read_tags_metadata(response, http_response)

    async def _read_tag_metadata_async(self) -> List[tbase.TagData]:
        def fn(token: str) -> Awaitable[Tuple[Any, HttpResponse]]:
            return self._api.as_async.get("/{id}/tags", params={"id": token})

        response, http_response = await self._ensure_selection_and_call_async(fn)
        return self._handle_read_tags_metadata(response, http_response)

    def _handle_read_tags_metadata(
        self, response: List[Any], http_response: HttpResponse
    ) -> List[tbase.TagData]:
        if response is None or any(t is None for t in response):
            raise tbase.TagManager.invalid_response(http_response)

        return [tbase.TagData.from_json_dict(t) for t in response]

    def _read_tag_values(self) -> List[SerializedTagWithAggregates | None]:
        def fn(token: str) -> Tuple[Any, HttpResponse]:
            return self._api.get("/{id}/values", params={"id": token})

        response, http_response = self._ensure_selection_and_call(fn)
        return self._handle_read_tags_values(response, http_response)

    async def _read_tag_values_async(
        self,
    ) -> List[SerializedTagWithAggregates | None]:
        def fn(token: str) -> Awaitable[Tuple[Any, HttpResponse]]:
            return self._api.as_async.get("/{id}/values", params={"id": token})

        response, http_response = await self._ensure_selection_and_call_async(fn)
        return self._handle_read_tags_values(response, http_response)

    def _handle_read_tags_values(
        self,
        response: List[Any],
        http_response: HttpResponse,
        paths: List[str] | None = None,
    ) -> List[SerializedTagWithAggregates | None]:
        if response is None or any(t is None for t in response):
            raise tbase.TagManager.invalid_response(http_response)

        result: List[SerializedTagWithAggregates | None] = []
        for i, t in enumerate(response):
            path = paths[i] if paths else t.get("path")
            if path is None:
                raise tbase.TagManager.invalid_response(http_response)

            if not t.get("current"):
                result.append(None)
                continue

            v = t["current"].get("value", {})
            value = v.get("value")
            data_type = v.get("type")
            aggregates = t.get("aggregates") or {}
            timestamp = None  # type: datetime.datetime | None
            if t["current"].get("timestamp"):
                timestamp = TimestampUtilities.str_to_datetime(
                    t["current"]["timestamp"]
                )
            if value is None or data_type is None:
                raise tbase.TagManager.invalid_response(http_response)

            result.append(
                SerializedTagWithAggregates(
                    path,
                    tbase.DataType.from_api_name(data_type),
                    value,
                    timestamp,
                    aggregates.get("count"),
                    aggregates.get("min"),
                    aggregates.get("max"),
                    (
                        float(aggregates["avg"])
                        if aggregates.get("avg") is not None
                        else None
                    ),
                )
            )
        return result

    def _read_tag_metadata_and_values(
        self,
    ) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]:
        def fn(token: str) -> Tuple[Any, HttpResponse]:
            return self._api.get("/{id}/tags-with-values", params={"id": token})

        response, http_response = self._ensure_selection_and_call(fn)
        return self._handle_read_tags_metadata_and_values(response, http_response)

    async def _read_tag_metadata_and_values_async(
        self,
    ) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]:
        def fn(token: str) -> Awaitable[Tuple[Any, HttpResponse]]:
            return self._api.as_async.get(
                "/{id}/tags-with-values", params={"id": token}
            )

        response, http_response = await self._ensure_selection_and_call_async(fn)
        return self._handle_read_tags_metadata_and_values(response, http_response)

    def _handle_read_tags_metadata_and_values(
        self, response: Any, http_response: HttpResponse
    ) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]:
        if (
            response is None
            or response.get("tagsWithValues") is None
            or any(
                t is None or t.get("tag") is None for t in response["tagsWithValues"]
            )
        ):
            raise tbase.TagManager.invalid_response(http_response)

        return (
            self._handle_read_tags_metadata(
                [t["tag"] for t in response["tagsWithValues"]], http_response
            ),
            self._handle_read_tags_values(
                response["tagsWithValues"],
                http_response,
                [t["tag"]["path"] for t in response["tagsWithValues"]],
            ),
        )

    def _reset_aggregates_internal(self) -> None:
        def fn(token: str) -> None:
            self._api.post("/{id}/reset-aggregates", params={"id": token})

        self._ensure_selection_and_call(fn)

    async def _reset_aggregates_internal_async(self) -> None:
        def fn(token: str) -> Awaitable[Tuple[None, HttpResponse]]:
            return self._api.as_async.post(
                "/{id}/reset-aggregates", params={"id": token}
            )

        await self._ensure_selection_and_call_async(fn)

    def _create_selection_on_server(self) -> None:
        selection, http_response = self._api.post(
            "", data={"searchPaths": list(self.paths)}
        )

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        self._token = selection["id"]
        self._selection_stale = False

    async def _create_selection_on_server_async(self) -> None:
        selection, http_response = await self._api.as_async.post(
            "", data={"searchPaths": list(self.paths)}
        )

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        self._token = selection["id"]
        self._selection_stale = False

    def _update_selection_on_server_if_needed(self) -> None:
        if self._selection_stale:
            self._api.put(
                "/{id}",
                data={"searchPaths": list(self.paths), "id": self._token},
                params={"id": self._token},
            )
            self._selection_stale = False

    async def _update_selection_on_server_if_needed_async(self) -> None:
        if self._selection_stale:
            await self._api.as_async.put(
                "/{id}",
                data={"searchPaths": list(self.paths), "id": self._token},
                params={"id": self._token},
            )
            self._selection_stale = False

    def _ensure_selection_and_call(self, api_call: Callable[[str], T]) -> T:
        if self._token is not None:
            try:
                self._update_selection_on_server_if_needed()
                return api_call(self._token)
            except core.ApiException as ex:
                if ex.http_status_code == 404:
                    # The server must have deleted it for inactivity. Recreate it below.
                    self._token = None
                else:
                    raise

        self._create_selection_on_server()
        assert self._token is not None
        return api_call(self._token)

    async def _ensure_selection_and_call_async(
        self, api_call: Callable[[str], Awaitable[T]]
    ) -> T:
        if self._token is not None:
            try:
                await self._update_selection_on_server_if_needed_async()
                return await api_call(self._token)
            except core.ApiException as ex:
                if ex.http_status_code == 404:
                    # The server must have deleted it for inactivity. Recreate it below.
                    self._token = None
                else:
                    raise

        await self._create_selection_on_server_async()
        assert self._token is not None
        return await api_call(self._token)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_subscription.py sha256=c5b45141da9a193e7f666b8812df2548d01121ddc74c32ec0458ef1de3e41558 bytes=10213 -->
## FILE: nisystemlink/clients/tag/_http/_http_tag_subscription.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_http_tag_subscription.py`
- sha256: `c5b45141da9a193e7f666b8812df2548d01121ddc74c32ec0458ef1de3e41558`
- bytes: 10213

````python
# -*- coding: utf-8 -*-

"""Implementation of HttpTagSubscription."""

import datetime
import weakref
from typing import Iterable, List

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates_reader import (
    SerializedTagWithAggregatesReader,
)
from typing_extensions import final


@final
class HttpTagSubscription(tbase.TagSubscription):
    _DEFAULT_POLLING_INTERVAL_MILLISECONDS = 5000.0

    __MAGIC = object()

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'HttpTagSubscription' is not an acceptable base type")

    @classmethod
    def create(
        cls,
        client: HttpClient,
        paths: Iterable[str],
        update_timer: ManualResetTimer | None = None,
        heartbeat_timer: ManualResetTimer | None = None,
    ) -> "HttpTagSubscription":
        """Create an :class:`HttpTagSubscription` with a custom heartbeat timer for testing purposes.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag path queries to include in the subscription.
            update_timer: A timer for polling for updates on the server, or None to use
                a default timer.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive, or None to use a default timer.

        Returns:
            The created subscription.

        Raises:
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        """
        subscription = HttpTagSubscription(
            cls.__MAGIC, client, paths, update_timer, heartbeat_timer
        )
        subscription._initialize()
        return subscription

    @classmethod
    async def create_async(
        cls,
        client: HttpClient,
        paths: Iterable[str],
        update_timer: ManualResetTimer | None = None,
        heartbeat_timer: ManualResetTimer | None = None,
    ) -> "HttpTagSubscription":
        """Asynchronously create an :class:`HttpTagSubscription` with a custom heartbeat timer for testing purposes.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag path queries to include in the subscription.
            update_timer: A timer for polling for updates on the server, or None to use
                a default timer.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive, or None to use a default timer.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created subscription.

        Raises:
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        """
        subscription = HttpTagSubscription(
            cls.__MAGIC, client, paths, update_timer, heartbeat_timer
        )
        await subscription._initialize_async()
        return subscription

    def __init__(
        self,
        magic: object,
        client: HttpClient,
        paths: Iterable[str],
        update_timer: ManualResetTimer | None = None,
        heartbeat_timer: ManualResetTimer | None = None,
    ) -> None:
        assert (
            magic is self.__MAGIC
        ), "Do not construct an HttpTagSubscription directly. Use create() instead."
        super().__init__(paths, heartbeat_timer)
        self._api = client.at_uri("/nitag/v2/subscriptions")
        if update_timer is not None:
            self._update_timer = update_timer
        else:
            self._update_timer = ManualResetTimer(
                datetime.timedelta(
                    milliseconds=self._DEFAULT_POLLING_INTERVAL_MILLISECONDS
                )
            )
            # _exit_stack is instantiated in the base class
            self._exit_stack.enter_context(self._update_timer)

        callback_ref = weakref.WeakMethod(self._update_timer_elapsed)  # type: ignore

        def callback() -> None:
            actual_callback = callback_ref()  # type: ignore
            if actual_callback:
                actual_callback()

        self._update_timer_handler = callback
        self._update_timer.elapsed += self._update_timer_handler
        self._token: str | None = None

    # Base class implementation is sufficient:
    #   def __enter__(self):
    #   async def __aenter__(self):
    #   def __exit__(self, exc_type, exc, traceback):
    #   async def __aexit__(self, exc_type, exc, traceback):

    def _close_internal(self) -> None:
        if self._token is None:
            return

        try:
            self._update_timer.stop()
            self._update_timer.elapsed -= self._update_timer_handler
            self._api.delete("/{id}", params={"id": self._token})
            self._token = None
        except core.ApiException:
            pass

    async def _close_internal_async(self) -> None:
        if self._token is None:
            return

        try:
            self._update_timer.stop()
            self._update_timer.elapsed -= self._update_timer_handler
            await self._api.as_async.delete("/{id}", params={"id": self._token})
            self._token = None
        except core.ApiException:
            pass

    def _create_subscription_on_server(self, paths: List[str]) -> None:
        response, http_response = self._api.post(
            "", data={"updatesOnly": True, "tags": paths}
        )

        if response is None or response.get("subscriptionId") is None:
            raise tbase.TagManager.invalid_response(http_response)

        token = response["subscriptionId"]

        # We only want to expose real changes to tags, but the subscription service
        # initially sends metadata and current values for every tag in the subscription.
        # For our API, we want clients to query using a selection prior to creating the
        # subscription if they want current information.
        self._api.get("/{id}/values/current", params={"id": token})
        self._token = token
        self._update_timer.start()

    async def _create_subscription_on_server_async(self, paths: List[str]) -> None:
        response, http_response = await self._api.as_async.post(
            "", data={"updatesOnly": True, "tags": paths}
        )

        if response is None or response.get("subscriptionId") is None:
            raise tbase.TagManager.invalid_response(http_response)

        token = response["subscriptionId"]

        # We only want to expose real changes to tags, but the subscription service
        # initially sends metadata and current values for every tag in the subscription.
        # For our API, we want clients to query using a selection prior to creating the
        # subscription if they want current information.
        await self._api.as_async.get("/{id}/values/current", params={"id": token})
        self._token = token
        self._update_timer.start()

    def _send_heartbeat(self) -> None:
        assert self._token is not None
        self._api.put("/{id}/heartbeat", params={"id": self._token})

    def _update_timer_elapsed(self) -> None:
        try:
            token = self._token
            if token is None:
                return

            try:
                response, _ = self._api.get(
                    "/{id}/values/current", params={"id": token}
                )
            except core.ApiException:
                return

            if response is None:
                return

            subscriptions = response.get("subscriptionUpdates")
            if subscriptions is None:
                return

            for subscription in subscriptions:
                if subscription is None:
                    continue

                updates = subscription.get("updates")
                if updates is None:
                    continue

                for update in updates:
                    if update is None:
                        continue

                    tag = update.get("tag")
                    timestamp = update.get("timestamp")
                    if tag is None or timestamp is None:
                        continue

                    tag = tbase.TagData.from_json_dict(tag)
                    try:
                        tag.validate_path()
                    except ValueError:
                        continue
                    aggregates = update.get("aggregates") or {}
                    if tag.data_type == tbase.DataType.UNKNOWN:
                        self._on_tag_changed(tag, None)
                    else:
                        value = SerializedTagWithAggregates(
                            tag.path,
                            tag.data_type,
                            update.get("value"),
                            TimestampUtilities.str_to_datetime(timestamp),
                            aggregates.get("count"),
                            aggregates.get("min"),
                            aggregates.get("max"),
                            (
                                float(aggregates["avg"])
                                if aggregates.get("avg") is not None
                                else None
                            ),
                        )
                        reader = tbase.TagValueReader(
                            SerializedTagWithAggregatesReader(value), tag
                        )  # type: tbase.TagValueReader
                        self._on_tag_changed(tag, reader)
        finally:
            self._update_timer.start()
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_temporary_tag_selection.py sha256=4dd2b5c703c3ae19be1a8f4f8b927fad4046e96db70133c5ab703428dc95db2f bytes=4684 -->
## FILE: nisystemlink/clients/tag/_http/_temporary_tag_selection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_http/_temporary_tag_selection.py`
- sha256: `4dd2b5c703c3ae19be1a8f4f8b927fad4046e96db70133c5ab703428dc95db2f`
- bytes: 4684

````python
# -*- coding: utf-8 -*-

"""Implementation of TemporaryTagSelection."""

from types import TracebackType
from typing import Awaitable, List, Type

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient
from typing_extensions import final


@final
class TemporaryTagSelection:
    """Manages the lifetime of short-lived tag selections that are used within a single API call.

    Closing the instance deletes the selection.
    """

    _TEMPORARY_SELECTION_TIMEOUT_SECONDS = 30
    """Inactivity timeout for short-lived selections created within a single API call."""

    __MAGIC = object()

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TemporaryTagSelection' is not an acceptable base type")

    @classmethod
    def create(cls, client: HttpClient, paths: List[str]) -> "TemporaryTagSelection":
        """Create a temporary tag selection containing the given paths.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag search paths to include in the selection.
        """
        selection = TemporaryTagSelection(cls.__MAGIC, client)
        selection._create(paths)
        return selection

    @classmethod
    async def create_async(
        cls, client: HttpClient, paths: List[str]
    ) -> "TemporaryTagSelection":
        """Asynchronously create a temporary tag selection containing the given paths.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag search paths to include in the selection.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created selection.
        """
        selection = TemporaryTagSelection(cls.__MAGIC, client)
        await selection._create_async(paths)
        return selection

    def __init__(self, magic: object, client: HttpClient) -> None:
        assert (
            magic == self.__MAGIC
        ), "Do not construct a TemporaryTagSelection directly. Use create() instead."
        self._api = client.at_uri("/nitag/v2/selections")
        self._id: str | None = None

    @property
    def id(self) -> str | None:  # noqa: D401
        """The ID of the selection."""
        return self._id

    def close(self) -> None:
        """Close the selection."""
        if self._id is None:
            return

        try:
            self._api.delete("/{id}", params={"id": self._id})
        except core.ApiException:
            pass

        self._id = None

    async def close_async(self) -> None:
        """Asynchronously close the selection.

        Returns:
            A task representing the asynchronous operation.
        """
        if self._id is None:
            return

        try:
            await self._api.as_async.delete("/{id}", params={"id": self._id})
        except core.ApiException:
            pass

        self._id = None

    def __enter__(self) -> "TemporaryTagSelection":
        return self

    async def __aenter__(self) -> "TemporaryTagSelection":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Awaitable[None]:
        return self.close_async()

    def __del__(self) -> None:
        self.close()

    def _create(self, paths: List[str]) -> None:
        selection, http_response = self._api.post(
            "",
            data={
                "searchPaths": paths,
                "inactivityTimeout": self._TEMPORARY_SELECTION_TIMEOUT_SECONDS,
            },
        )

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        self._id = selection["id"]

    async def _create_async(self, paths: List[str]) -> None:
        selection, http_response = await self._api.as_async.post(
            "",
            data={
                "searchPaths": paths,
                "inactivityTimeout": self._TEMPORARY_SELECTION_TIMEOUT_SECONDS,
            },
        )

        if selection is None or selection.get("id") is None:
            raise tbase.TagManager.invalid_response(http_response)

        self._id = selection["id"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_itag_reader.py sha256=3f5c1dfaddcfb3fa09c07a960c2fd6d8c986e39aca24032083ecee5d72d2cc49 bytes=10171 -->
## FILE: nisystemlink/clients/tag/_itag_reader.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_itag_reader.py`
- sha256: `3f5c1dfaddcfb3fa09c07a960c2fd6d8c986e39aca24032083ecee5d72d2cc49`
- bytes: 10171

````python
# -*- coding: utf-8 -*-

"""Implementation of ITagReader."""

import abc
import datetime
import typing
from typing import Any, Callable, Dict

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)
from typing_extensions import Literal

_DESERIALIZERS: Dict[tbase.DataType, Callable[[str], Any]] = {
    tbase.DataType.BOOLEAN: {"True": True, "False": False}.get,
    tbase.DataType.DATE_TIME: TimestampUtilities.str_to_datetime,
    tbase.DataType.DOUBLE: float,
    tbase.DataType.INT32: int,
    tbase.DataType.UINT64: int,
    tbase.DataType.STRING: str,
}


class _ITagReaderOverloads(abc.ABC):
    """Contains the overloaded methods of ITagReader.

    These overloads exist so that ``mypy`` can validate proper data types are used when
    reading tag values, as long as a literal DataType enum value is given when calling
    :meth:`get_tag_reader`. But they are hidden away in a base class so that they aren't
    documented by Sphinx, because Sphinx doesn't properly recognize the type annotations
    of overloads. See also: https://github.com/sphinx-doc/sphinx/issues/7901
    """

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.BOOLEAN]
    ) -> "tbase.TagValueReader[bool]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.DATE_TIME]
    ) -> "tbase.TagValueReader[datetime.datetime]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.DOUBLE]
    ) -> "tbase.TagValueReader[float]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.INT32]
    ) -> "tbase.TagValueReader[int]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.UINT64]
    ) -> "tbase.TagValueReader[int]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: Literal[tbase.DataType.STRING]
    ) -> "tbase.TagValueReader[str]":
        pass

    @typing.overload
    def get_tag_reader(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueReader[Any]":
        pass

    def get_tag_reader(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueReader":
        """Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the tag to read.
        """
        return self._get_tag_reader(path, data_type)

    @abc.abstractmethod
    def _get_tag_reader(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueReader":
        """Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the value to read.
        """
        ...


class ITagReader(_ITagReaderOverloads):
    """Provides an interface for reading the current and aggregate values of a single SystemLink tag."""

    def read(
        self,
        path: str,
        *,
        include_timestamp: bool = False,
        include_aggregates: bool = False
    ) -> tbase.TagWithAggregates | None:
        """Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        """
        data = self._read(path, include_timestamp, include_aggregates)
        if data is None or data.value is None:
            return None

        value = self._deserialize_value(data.value, data.data_type)
        if value is None:
            # TODO: Error information
            raise core.ApiException()

        return tbase.TagWithAggregates(
            data.path,
            data.data_type,
            value,
            data.timestamp,
            data.count,
            self._deserialize_value(data.min, data.data_type),
            self._deserialize_value(data.max, data.data_type),
            data.mean,
        )

    async def read_async(
        self,
        path: str,
        *,
        include_timestamp: bool = False,
        include_aggregates: bool = False
    ) -> tbase.TagWithAggregates | None:
        """Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        """
        data = await self._read_async(path, include_timestamp, include_aggregates)
        if data is None or data.value is None:
            return None

        value = self._deserialize_value(data.value, data.data_type)
        if value is None:
            # TODO: Error information
            raise core.ApiException()

        return tbase.TagWithAggregates(
            data.path,
            data.data_type,
            value,
            data.timestamp,
            data.count,
            self._deserialize_value(data.min, data.data_type),
            self._deserialize_value(data.max, data.data_type),
            data.mean,
        )

    @abc.abstractmethod
    def _read(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _read_async(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        """
        ...

    @classmethod
    def _deserialize_value(cls, value: str | None, data_type: tbase.DataType) -> Any:
        if value is None:
            return None
        try:
            deserializer = _DESERIALIZERS[data_type]
        except KeyError:
            raise ValueError("data_type is unknown")
        try:
            return deserializer(value)
        except ValueError:
            return None

    def _get_tag_reader(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueReader":
        """Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the value to read.
        """
        return tbase.TagValueReader(self, tbase.TagData(path, data_type))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_itag_writer.py sha256=928e35a59d6f7588f005650b47c2e811423cea6a87ce34814ef259f5a9f07be8 bytes=9617 -->
## FILE: nisystemlink/clients/tag/_itag_writer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_itag_writer.py`
- sha256: `928e35a59d6f7588f005650b47c2e811423cea6a87ce34814ef259f5a9f07be8`
- bytes: 9617

````python
# -*- coding: utf-8 -*-

"""Implementation of ITagWriter."""

import abc
import datetime
import typing
from typing import Any, Awaitable

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from typing_extensions import Literal

_VALID_TYPES: typing.Dict[tbase.DataType, type | typing.Tuple[type, type]] = {
    tbase.DataType.BOOLEAN: bool,
    tbase.DataType.DATE_TIME: datetime.datetime,
    tbase.DataType.DOUBLE: (float, int),
    tbase.DataType.INT32: int,
    tbase.DataType.UINT64: int,
    tbase.DataType.STRING: str,
}


class _ITagWriterOverloads(abc.ABC):
    """Contains the overloaded methods of ITagWriter.

    These overloads exist so that ``mypy`` can validate proper data types are used when
    writing tag values, as long as a literal DataType enum value is given when calling
    :meth:`get_tag_writer`. But they are hidden away in a base class so that they aren't
    documented by Sphinx, because Sphinx doesn't properly recognize the type annotations
    of overloads. See also: https://github.com/sphinx-doc/sphinx/issues/7901
    """

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.BOOLEAN]
    ) -> "tbase.TagValueWriter[bool]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.DATE_TIME]
    ) -> "tbase.TagValueWriter[datetime.datetime]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.DOUBLE]
    ) -> "tbase.TagValueWriter[float]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.INT32]
    ) -> "tbase.TagValueWriter[int]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.UINT64]
    ) -> "tbase.TagValueWriter[int]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: Literal[tbase.DataType.STRING]
    ) -> "tbase.TagValueWriter[str]":
        pass

    @typing.overload
    def get_tag_writer(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueWriter[Any]":
        pass

    def get_tag_writer(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueWriter":
        """Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        """
        return self._get_tag_writer(path, data_type)

    @abc.abstractmethod
    def _get_tag_writer(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueWriter":
        """Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        """
        ...


class ITagWriter(_ITagWriterOverloads):
    """Provides an interface for writing the current value of a single SystemLink tag."""

    def write(
        self,
        path: str,
        data_type: tbase.DataType,
        value: bool | int | float | str | datetime.datetime,
        *,
        timestamp: datetime.datetime | None = None
    ) -> None:
        """Write a tag's value.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``value`` has the wrong data type.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        self._validate_type(value, data_type)

        if data_type == tbase.DataType.DATE_TIME:
            value = TimestampUtilities.datetime_to_str(
                typing.cast(datetime.datetime, value)
            )

        self._write(path, data_type, str(value), timestamp)

    def write_async(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        *,
        timestamp: datetime.datetime | None = None
    ) -> Awaitable[None]:
        """Asynchronously write a tag's value.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``value`` has the wrong data type.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        self._validate_type(value, data_type)

        if data_type == tbase.DataType.DATE_TIME:
            value = TimestampUtilities.datetime_to_str(
                typing.cast(datetime.datetime, value)
            )

        return self._write_async(path, data_type, str(value), timestamp)

    @classmethod
    def _validate_type(
        cls,
        value: bool | int | float | str | datetime.datetime,
        data_type: tbase.DataType,
    ) -> None:
        if data_type == tbase.DataType.UNKNOWN:
            raise ValueError("data_type is UNKNOWN")

        if not isinstance(value, _VALID_TYPES[data_type]):
            raise ValueError(
                "value has wrong python data type ({}) for SystemLink data type {}".format(
                    type(value).__name__, data_type.name
                )
            )

        # python's bool is a subclass of int, so the above check won't catch some cases
        if isinstance(value, bool) and data_type != tbase.DataType.BOOLEAN:
            raise ValueError(
                "value has wrong python data type ({}) for SystemLink data type {}".format(
                    type(value).__name__, data_type.name
                )
            )

        if data_type == tbase.DataType.INT32:
            assert isinstance(value, int)
            if not -(2**31) <= value < 2**31:
                raise ValueError(
                    "value {} is not the valid range of an INT32".format(value)
                )
        elif data_type == tbase.DataType.UINT64:
            assert isinstance(value, int)
            if not 0 <= value < 2**64:
                raise ValueError(
                    "value {} is not the valid range of a UINT64".format(value)
                )

    @abc.abstractmethod
    def _write(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> None:
        """Write a tag's value that's been serialized to a string.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _write_async(
        self,
        path: str,
        data_type: tbase.DataType,
        value: str,
        timestamp: datetime.datetime | None = None,
    ) -> None:
        """Asynchronously write a tag's value that's been serialized to a string.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        """
        ...

    def _get_tag_writer(
        self, path: str, data_type: tbase.DataType
    ) -> "tbase.TagValueWriter":
        """Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        """
        return tbase.TagValueWriter(self, tbase.TagData(path, data_type))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_retention_type.py sha256=9dca9456b61ae1a72d38b44cbb54c49482655399b36ba13d4a1d3a2f64e0e03e bytes=772 -->
## FILE: nisystemlink/clients/tag/_retention_type.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_retention_type.py`
- sha256: `9dca9456b61ae1a72d38b44cbb54c49482655399b36ba13d4a1d3a2f64e0e03e`
- bytes: 772

````python
# -*- coding: utf-8 -*-

"""Implementation of RetentionType."""

import enum


class RetentionType(enum.Enum):
    """Represents the different ways for the SystemLink tag historian to retain the history of tag values."""

    INVALID = 0
    """An unknown or invalid tag retention type.

    Not a valid input to API calls, but used to represent tags whose retention type
    isn't recognized.
    """

    NONE = 1
    """No history for the tag's value is retained."""

    DURATION = 2
    """Historical values for the tag are retained for a set number of days."""

    COUNT = 3
    """A set number of historical values for the tag are retained."""

    PERMANENT = 4
    """All of the tag's values are retained until the tag is deleted."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_data.py sha256=4432bc13c307b0e5e5b53dee2fec3e790335535734909dbfc5d1e9a239566b7a bytes=11759 -->
## FILE: nisystemlink/clients/tag/_tag_data.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_data.py`
- sha256: `4432bc13c307b0e5e5b53dee2fec3e790335535734909dbfc5d1e9a239566b7a`
- bytes: 11759

````python
# -*- coding: utf-8 -*-

"""Implementation of TagData."""

from typing import Any, Dict, Iterable, List

from nisystemlink.clients import tag as tbase
from typing_extensions import final


@final
class TagData:
    """Contains the metadata for a SystemLink tag."""

    _RETENTION_TYPE_PROP = "nitagRetention"

    _RETENTION_TYPE_NONE = "NONE"

    _RETENTION_TYPE_DURATION = "DURATION"

    _RETENTION_TYPE_COUNT = "COUNT"

    _RETENTION_TYPE_PERMANENT = "PERMANENT"

    _HISTORY_TTL_DAYS_PROP = "nitagHistoryTTLDays"

    _MAX_HISTORY_COUNT_PROP = "nitagMaxHistoryCount"

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TagData' is not an acceptable base type")

    def __init__(
        self,
        path: str,
        data_type: tbase.DataType | None = None,
        keywords: Iterable[str] | None = None,
        properties: Dict[str, str] | None = None,
    ) -> None:
        """Initialize an instance.

        Args:
            path: The tag's path, which uses a dot-separated hierarchy to uniquely
                identify the tag on the server.
            data_type: The data type for the tag's values.
            keywords: The tag's keywords.
            properties: The tag's properties.
        """
        self._path = path
        self._data_type = tbase.DataType.UNKNOWN if data_type is None else data_type
        self._keywords = list(keywords) if keywords else []
        self._properties: Dict[str, str] = {}
        self._collect_aggregates = False
        self._retention_type = tbase.RetentionType.NONE
        self._retention_count: int | None = None
        self._retention_days: int | None = None
        if properties:
            self.replace_properties(properties)

    @classmethod
    def from_json_dict(cls, data: Dict[str, Any]) -> "TagData":
        data_type_str = data.get("type") or "UNKNOWN"
        data_type = tbase.DataType.from_api_name(data_type_str)
        tag = cls(data["path"], data_type, data.get("keywords"), data.get("properties"))
        if data.get("collectAggregates"):
            tag.collect_aggregates = True
        return tag

    def to_json_dict(self) -> Dict[str, Any]:
        self.validate_path()
        if self.data_type == tbase.DataType.UNKNOWN:
            raise ValueError("Invalid tag data type")

        data: Dict[str, Any] = {}
        data["path"] = self._path
        data["type"] = self._data_type.api_name
        data["collectAggregates"] = self.collect_aggregates

        if self._keywords:
            data["keywords"] = self._keywords

        data["properties"] = dict(self._properties) if self._properties else {}
        self._copy_retention_properties(data["properties"])
        if not data["properties"]:
            del data["properties"]

        return data

    @property
    def collect_aggregates(self) -> bool:  # noqa: D401
        """Whether the server should keep aggregate information for the tag.

        The information collected depends on the tag's :attr:`data_type`.
        """
        return self._collect_aggregates

    @collect_aggregates.setter
    def collect_aggregates(self, value: bool) -> None:
        self._collect_aggregates = value

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type for the tag's values.

        Changing the data type of an existing tag requires deleting the tag and creating
        a new one of a different data type.
        """
        return self._data_type

    @data_type.setter
    def data_type(self, value: tbase.DataType) -> None:
        self._data_type = value

    @property
    def keywords(self) -> List[str]:  # noqa: D401
        """The list of keywords associated with the tag."""
        return self._keywords

    @property
    def path(self) -> str:  # noqa: D401
        """The tag's path, which uses a dot-separated hierarchy to uniquely identify the tag on the server."""
        return self._path

    @property
    def properties(self) -> Dict[str, str]:  # noqa: D401
        """The properties associated with the tag."""
        return self._properties

    @property
    def retention_type(self) -> tbase.RetentionType:  # noqa: D401
        """How the tag's historical values are retained by the tag historian, if available.

        The :attr:`retention_count` and :attr:`retention_days` properties can further
        customize when values are removed from the historian.

        The tag historian is an optional component for SystemLink Server installations,
        and is not available in SystemLink Cloud. The tag's historical values are not
        retained when the tag historian is not available, regardless of the retention
        type.
        """
        return self._retention_type

    @retention_type.setter
    def retention_type(self, value: tbase.RetentionType) -> None:
        self._retention_type = value

    @property
    def retention_count(self) -> int | None:  # noqa: D401
        """The number of historical values to retain when :attr:`retention_type` is
        :attr:`RetentionType.COUNT`, or None to use the server-specified default of
        10000.
        """
        return self._retention_count

    @retention_count.setter
    def retention_count(self, value: int | None) -> None:
        self._retention_count = value

    @property
    def retention_days(self) -> int | None:  # noqa: D401
        """The number of days to keep a tag's historical values when
        :attr:`retention_type` is :attr:`RetentionType.DURATION`, or None to use the
        server-specified default of 30 days.
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, value: int | None) -> None:
        self._retention_days = value

    def replace_keywords(self, keywords: Iterable[str]) -> None:
        """Replace all of the tag's :attr:`keywords` with those in ``keywords``.

        Args:
            keywords: The tag's new keywords, or None to clear all keywords.
        """
        self._keywords[:] = keywords

    def replace_properties(self, properties: Dict[str, str]) -> None:
        """Replace all of the tag's :attr:`properties` with those in ``properties``.

        Args:
            properties: The tag's new properties, or None to clear all properties.
        """
        self._properties.clear()

        if properties is None:
            return

        for key, value in properties.items():
            # Check for special properties to parse.
            if key == self._RETENTION_TYPE_PROP:
                if value == self._RETENTION_TYPE_COUNT:
                    self._retention_type = tbase.RetentionType.COUNT
                elif value == self._RETENTION_TYPE_DURATION:
                    self._retention_type = tbase.RetentionType.DURATION
                elif value == self._RETENTION_TYPE_NONE:
                    self._retention_type = tbase.RetentionType.NONE
                elif value == self._RETENTION_TYPE_PERMANENT:
                    self._retention_type = tbase.RetentionType.PERMANENT
                else:
                    self._retention_type = tbase.RetentionType.INVALID
            elif key == self._HISTORY_TTL_DAYS_PROP:
                try:
                    self._retention_days = int(value)
                except ValueError:
                    self._retention_days = None
            elif key == self._MAX_HISTORY_COUNT_PROP:
                try:
                    self._retention_count = int(value)
                except ValueError:
                    self._retention_count = None
            else:
                # Not a special property. Preserve it in the dictionary.
                self._properties[key] = value

    def _copy_retention_properties(self, destination: Dict[str, str]) -> None:
        """Copy the tag's retention settings into ``destination``.

        Clients do not typically call this method directly.

        Args:
            destination: The dictionary to copy into. Existing properties with names in
                common with the retention properties will be overwritten.

        Raises:
            ValueError: if ``destination`` is None.
        """
        if destination is None:
            raise ValueError("destination cannot be None")

        if self._retention_type == tbase.RetentionType.NONE:
            destination[self._RETENTION_TYPE_PROP] = self._RETENTION_TYPE_NONE
        elif self._retention_type == tbase.RetentionType.DURATION:
            destination[self._RETENTION_TYPE_PROP] = self._RETENTION_TYPE_DURATION
        elif self._retention_type == tbase.RetentionType.COUNT:
            destination[self._RETENTION_TYPE_PROP] = self._RETENTION_TYPE_COUNT
        elif self._retention_type == tbase.RetentionType.PERMANENT:
            destination[self._RETENTION_TYPE_PROP] = self._RETENTION_TYPE_PERMANENT

        if self._retention_count is not None:
            destination[self._MAX_HISTORY_COUNT_PROP] = str(self._retention_count)

        if self._retention_days is not None:
            destination[self._HISTORY_TTL_DAYS_PROP] = str(self._retention_days)

    def clear_retention(self) -> None:
        """Clear all retention settings, setting it to use a
        :attr:`TagData.retention_type` of :attr:`RetentionType.NONE`.

        Args:
            tag: The tag whose retention will be cleared.
        """
        self.retention_type = tbase.RetentionType.NONE
        self.retention_count = None
        self.retention_days = None

    def set_retention_count(self, count: int) -> None:
        """Set the number of historical values to retain.

        Args:
            count: The number of historical values to retain.
        """
        self.retention_type = tbase.RetentionType.COUNT
        self.retention_count = count
        self.retention_days = None

    def set_retention_days(self, days: int) -> None:
        """Set the historical values to be retained for the specified number of days.

        Args:
            days: The number of days a historical value will be kept.
        """
        self.retention_type = tbase.RetentionType.DURATION
        self.retention_count = None
        self.retention_days = days

    def validate_type(self, required_type: tbase.DataType) -> None:
        """Validate that the tag's data type matches ``required_type``.

        Clients do not typically call this method directly.

        Args:
            required_type: The data type required by the API.

        Raises:
            ValueError: if this is not a tag of the required type with a valid path.
            ValueError: if ``required_type`` is :attr:`DataType.UNKNOWN`.
        """
        if required_type == tbase.DataType.UNKNOWN:
            raise ValueError("required_type is not a valid data type")

        if self.data_type != required_type:
            raise ValueError(
                "Tag must be a {} type but is a {} tag".format(
                    required_type.name, self.data_type.name
                )
            )

    def validate_path(self) -> str:
        """Validate the path as an input and returns it.

        Clients do not typically call this method directly.

        Returns:
            The validated path.

        Raises:
            ValueError: if the tag's path is invalid.
        """
        if self.path is None:
            raise ValueError("Tag path cannot be None")

        return tbase.TagPathUtilities.validate(self.path)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_data_update.py sha256=c69f1c59c1ee2144a4637234153c96d9d8bd881a82f003246190d48ff042f9e8 bytes=5956 -->
## FILE: nisystemlink/clients/tag/_tag_data_update.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_data_update.py`
- sha256: `c69f1c59c1ee2144a4637234153c96d9d8bd881a82f003246190d48ff042f9e8`
- bytes: 5956

````python
# -*- coding: utf-8 -*-

"""Implementation of TagDataUpdate."""

from typing import Any, Dict, Iterable, Tuple

from nisystemlink.clients import tag as tbase
from typing_extensions import final


@final
class TagDataUpdate:
    """Contains information for updating parts of a tag's metadata on the server when
    used with the :meth:`TagManager.update()` method.

    The update can add keywords, add new properties, change the value of existing
    properties, modify the collect aggregates setting, and modify retention settings. To
    remove a keyword or property, pass the entire :class:`TagData` to the
    :meth:`TagManager.update()` method instead.
    """

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TagDataUpdate' is not an acceptable base type")

    def __init__(
        self,
        path: str,
        data_type: tbase.DataType,
        keywords: Iterable[str] | None = None,
        properties: Dict[str, str] | None = None,
    ) -> None:
        """Initialize an update of a tag's keywords and/or properties.

        Keywords and properties included in the update that are missing from the tag's
        metadata on the server are added, and properties that exist with a different
        value are replaced. At least one of ``keywords`` or ``properties`` must be
        specified.

        Args:
            path: The path of the tag to update.
            data_type: The data type of the tag to update.
            keywords: The list of keywords that will be added to the tag's metadata on
                the server, or None to not add any keywords.
            properties: The properties that will be added to or replaced in the tag's
                metadata on the server, or None to not modify any properties.

        Raises:
            ValueError: if ``path`` is None.
            ValueError: if both ``keywords`` and ``properties`` are None.
        """
        if path is None:
            raise ValueError("path cannot be None")
        self._path = path
        self._data_type = data_type

        if keywords is None and properties is None:
            raise ValueError(
                "Must specify at least one of keywords or properties to update"
            )
        self._keywords = list(keywords) if keywords is not None else None
        self._properties: Dict[str, str] | None = None
        if properties is not None:
            self._properties = dict(properties)

        self._collect_aggregates: bool | None = None

    @classmethod
    def from_tagdata(
        cls, data: tbase.TagData, fields: tbase.TagUpdateFields
    ) -> "TagDataUpdate":
        """Create an update by taking one or more fields from a :class:`TagData`.

        Args:
            data: The metadata to send to the server in the update.
            fields: One or more fields to include in the update.

        Raises:
            ValueError: if ``data`` is None.
            ValueError: if ``fields`` has no fields or invalid fields.
        """
        if data is None:
            raise ValueError("data cannot be None")

        if fields == 0:
            raise ValueError("Must specify at least one field to update")

        if (tbase.TagUpdateFields.ALL & fields) != fields:
            raise ValueError("Invalid field specified")

        obj = cls.__new__(cls)
        obj._path = data.path
        obj._data_type = data.data_type
        obj._keywords = None
        obj._properties = None
        obj._collect_aggregates = None

        if fields & tbase.TagUpdateFields.KEYWORDS and data.keywords:
            obj._keywords = list(data.keywords)

        if fields & tbase.TagUpdateFields.PROPERTIES and data.properties:
            obj._properties = dict(data.properties)
        if fields & tbase.TagUpdateFields.RETENTION:
            if obj._properties is None:
                obj._properties = {}
            data._copy_retention_properties(obj._properties)

        if fields & tbase.TagUpdateFields.COLLECT_AGGREGATES:
            obj._collect_aggregates = data.collect_aggregates

        return obj

    def to_json_dict(self) -> Dict[str, Any]:
        if self.data_type == tbase.DataType.UNKNOWN:
            raise ValueError("Invalid tag data type")

        data: Dict[str, Any] = {
            "path": tbase.TagPathUtilities.validate(self._path),
            "type": self._data_type.api_name,
        }

        if self._keywords is not None:
            data["keywords"] = self._keywords
        if self._properties is not None:
            data["properties"] = self._properties
        if self._collect_aggregates is not None:
            data["collectAggregates"] = self._collect_aggregates
        return data

    @property
    def collect_aggregates(self) -> bool | None:  # noqa: D401
        """The :attr:`TagData.collect_aggregates` setting to send with the update, or None to not send a value."""
        return self._collect_aggregates

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type for the tag's values."""
        return self._data_type

    @property
    def keywords(self) -> Tuple[str, ...] | None:  # noqa: D401
        """The list of keywords to send with the update, or None to not send any keywords."""
        return tuple(self._keywords) if self._keywords is not None else None

    @property
    def path(self) -> str:  # noqa: D401
        """The tag's path, which uses a dot-separated hierarchy to uniquely identify the tag on the server."""
        return self._path

    @property
    def properties(self) -> Dict[str, str] | None:  # noqa: D401
        """The properties send with the update, or None to not send any properties."""
        if self._properties:
            return dict(self._properties)
        else:
            return None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_manager.py sha256=6d777e736257a6ee80cc526b596b8abd3b2c6aac1a43e4b8b219b9c928c12162 bytes=33854 -->
## FILE: nisystemlink/clients/tag/_tag_manager.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_manager.py`
- sha256: `6d777e736257a6ee80cc526b596b8abd3b2c6aac1a43e4b8b219b9c928c12162`
- bytes: 33854

````python
# -*- coding: utf-8 -*-

"""Implementation of TagManager."""

import asyncio
import datetime
from typing import Any, Awaitable, Dict, Iterable, List, Sequence, Tuple

from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient, HttpResponse
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)
from nisystemlink.clients.tag._core._system_time_stamper import SystemTimeStamper
from nisystemlink.clients.tag._http._http_async_tag_query_result_collection import (
    HttpAsyncTagQueryResultCollection,
)
from nisystemlink.clients.tag._http._http_buffered_tag_writer import (
    HttpBufferedTagWriter,
)
from nisystemlink.clients.tag._http._http_tag_query_result_collection import (
    HttpTagQueryResultCollection,
)
from nisystemlink.clients.tag._http._http_tag_selection import HttpTagSelection
from nisystemlink.clients.tag._http._temporary_tag_selection import (
    TemporaryTagSelection,
)
from typing_extensions import final


@final
class TagManager(tbase.ITagReader):
    """Represents common ways to create, read, and query SystemLink tags for a specific server connection."""

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TagManager' is not an acceptable base type")

    def __init__(self, configuration: core.HttpConfiguration | None = None) -> None:
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect.

        Raises:
            ApiException: if the current system cannot communicate with a SystemLink
                Server, or if the configuration provided by SystemLink Client cannot be
                found.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        self._http_client = HttpClient(configuration)
        self._api = self._http_client.at_uri("/nitag/v2")

    def create_selection(self, tags: List[tbase.TagData]) -> tbase.TagSelection:
        """Create an :class:`TagSelection` that initially contains the given ``tags``
        without retrieving any additional data from the server.

        Args:
            tags: The tags to include in the selection.

        Returns:
            The created selection.

        Raises:
            ValueError: if any of the given ``tags`` is None or has an invalid path.
            ValueError: if ``tags`` is None.
        """
        return HttpTagSelection(self._http_client, tags)

    def open_selection(self, paths: List[str]) -> tbase.TagSelection:
        """Query the server for the metadata for the given tag ``paths`` and return the
        results in a :class:`TagSelection`.

        Args:
            paths: The paths of the tags to include in the selection. May include
                glob-style wildcards.

        Returns:
            The created selection with :attr:`TagSelection.metadata` containing the
            metadata.

        Raises:
            ValueError: if any of the given ``paths`` is None or invalid.
            ValueError: if ``paths`` contains duplicate paths.
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        """
        return HttpTagSelection.open(self._http_client, paths)

    def open_selection_async(self, paths: List[str]) -> Awaitable[tbase.TagSelection]:
        """Asynchronously query the server for the metadata for the given tag ``paths``
        and return the results in a :class:`TagSelection`.

        Args:
            paths: The paths of the tags to include in the selection. May include
                glob-style wildcards.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created selection with :attr:`TagSelection.metadata` containing the
            metadata.

        Raises:
            ValueError: if any of the given ``paths`` is None or invalid.
            ValueError: if ``paths`` contains duplicate paths.
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        """
        return HttpTagSelection.open_async(self._http_client, paths)

    def open(
        self,
        path: str,
        data_type: tbase.DataType | None = None,
        *,
        create: bool | None = None
    ) -> tbase.TagData:
        """Query the server for the metadata of a tag, optionally creating it if it doesn't already exist.

        If ``data_type`` is provided, ``create`` defaults to True. If ``data_type`` is
        not provided, ``create`` cannot be set to True.

        The call fails if the tag already exists as a different data type than specified
        or if it doesn't exist and ``create`` is False.

        Args:
            path: The path of the tag to open.
            data_type: The expected data type of the tag.
            create: True to create the tag if it doesn't already exist, False to fail if
                it doesn't exist.

        Returns:
            Information about the tag.

        Raises:
            ValueError: if ``path`` is None or empty.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``create`` is True, but ``data_type`` is None.
            ApiException: if the API call fails.
        """
        if create is None:
            create = data_type is not None
        elif create is True:
            if data_type is None:
                raise ValueError("Cannot create if data_type is not specified")

        if data_type == tbase.DataType.UNKNOWN:
            raise ValueError("Must specify a valid data type")

        tag: Dict[str, Any] | None = None
        try:
            tag, _ = self._api.get(
                "/tags/{path}", params={"path": tbase.TagPathUtilities.validate(path)}
            )
        except core.ApiException as ex:
            error_name = None if ex.error is None else ex.error.name
            if create and (error_name or "").startswith("Tag.NoSuchTag"):
                pass  # continue on and create the tag
            else:
                raise

        if tag is not None:
            if data_type is not None and tag["type"] != data_type.api_name:
                raise core.ApiException("Tag exists with a conflicting data type")

            return tbase.TagData.from_json_dict(tag)
        else:
            if data_type is None:
                raise ValueError("data_type cannot be None when create is True")

            # Tag didn't already exist, so try to create it.
            self._api.post("/tags", data={"type": data_type.api_name, "path": path})
            return tbase.TagData(path, data_type)

    async def open_async(
        self,
        path: str,
        data_type: tbase.DataType | None = None,
        *,
        create: bool | None = None
    ) -> tbase.TagData:
        """Asynchronously query the server for the metadata of a tag, optionally
        creating it if it doesn't already exist.

        The call fails if the tag already exists as a different data type than specified
        or if it doesn't exist and ``create`` is False.

        Args:
            path: The path of the tag to open.
            data_type: The expected data type of the tag.
            create: True to create the tag if it doesn't already exist, False to fail if
                it doesn't exist.

        Returns:
            A task representing the asynchronous operation. On success, contains
            information about the tag.

        Raises:
            ValueError: if ``path`` is None or empty.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``create`` is True, but ``data_type`` is None.
            ApiException: if the API call fails.
        """
        if create is None:
            create = data_type is not None
        elif create is True:
            if data_type is None:
                raise ValueError("Cannot create if data_type is not specified")

        if data_type == tbase.DataType.UNKNOWN:
            raise ValueError("Must specify a valid data type")

        tag: Dict[str, Any] | None = None
        try:
            tag, _ = await self._api.as_async.get(
                "/tags/{path}", params={"path": tbase.TagPathUtilities.validate(path)}
            )
        except core.ApiException as ex:
            error_name = None if ex.error is None else ex.error.name
            if create and (error_name or "").startswith("Tag.NoSuchTag"):
                pass  # continue on and create the tag
            else:
                raise

        if tag is not None:
            if data_type is not None and tag["type"] != data_type.api_name:
                raise core.ApiException("Tag exists with a conflicting data type")

            return tbase.TagData.from_json_dict(tag)
        else:
            if data_type is None:
                raise ValueError("data_type cannot be None when create is True")

            # Tag didn't already exist, so try to create it.
            await self._api.as_async.post(
                "/tags", data={"type": data_type.api_name, "path": path}
            )
            return tbase.TagData(path, data_type)

    def refresh(self, tags: List[tbase.TagData]) -> None:
        """Populate the given ``tags`` with the latest metadata from the server.

        Only the :attr:`TagData.path` needs to be initialized. Tags that don't exist on
        the server will have their :attr:`TagData.data_type` set to
        :attr:`DataType.UNKNOWN`.

        Args:
            tags: The tags to refresh.

        Raises:
            ValueError: if any ``tags`` are None or have invalid paths.
            ValueError: if ``tags`` is None.
            ApiException: if the API call fails.
        """
        paths = self._prepare_refresh(tags)
        response, http_response = self._api.get(
            "/tags", params={"path": paths, "take": str(len(tags))}
        )
        self._handle_refresh(tags, response, http_response)

    async def refresh_async(self, tags: List[tbase.TagData]) -> None:
        """Asynchronously populate the given ``tags`` with the latest metadata from the server.

        Only the :attr:`TagData.path` needs to be initialized. Tags that don't exist on
        the server will have their :attr:`TagData.data_type` set to
        :attr:`DataType.UNKNOWN`.

        Args:
            tags: The tags to refresh.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if any ``tags`` are None or have invalid paths.
            ValueError: if ``tags`` is None.
            ApiException: if the API call fails.
        """
        paths = self._prepare_refresh(tags)
        response, http_response = await self._api.as_async.get(
            "/tags", params={"path": paths, "take": str(len(tags))}
        )
        self._handle_refresh(tags, response, http_response)

    def _prepare_refresh(self, tags: List[tbase.TagData]) -> str:
        if tags is None:
            raise ValueError("tags cannot be None")
        elif any(t is None for t in tags):
            raise ValueError("Tags cannot contain None")

        return ",".join(t.validate_path() for t in tags)

    def _handle_refresh(
        self,
        tags: List[tbase.TagData],
        refresh_result: Dict[str, Any],
        http_response: HttpResponse,
    ) -> None:
        if refresh_result is None or refresh_result.get("tags") is None:
            raise self.invalid_response(http_response)

        read_tags = {t["path"]: t for t in refresh_result["tags"]}

        for data in tags:
            tag = read_tags.get(data.path)
            if tag is not None:
                data.clear_retention()
                data.data_type = tbase.DataType.from_api_name(
                    tag.get("type") or "UNKNOWN"
                )
                data.replace_keywords(tag.get("keywords") or [])
                data.replace_properties(tag.get("properties") or {})
                data.collect_aggregates = tag.get("collectAggregates") or False
            else:
                data.data_type = tbase.DataType.UNKNOWN

    def query(
        self,
        paths: Sequence[str] | None = None,
        keywords: Iterable[str] | None = None,
        properties: Dict[str, str] | None = None,
        *,
        skip: int = 0,
        take: int | None = None
    ) -> tbase.TagQueryResultCollection:
        """Query the server for available tags matching the given criteria.

        Args:
            paths: List of tag paths to include in the result. May include glob-style
                wildcards.
            keywords: List of keywords that tags must have, or None.
            properties: Mapping of properties and their values that tags must have, or
                None.
            skip: The number of tags to initially skip in the results.
            take: The number of tags to include in each page of results.

        Returns:
            A :class:`TagQueryResultCollection` containing the first page of results.
            Enumerating the collection will retrieve additional pages according to the
            ``take`` parameter.

        Raises:
            ValueError: if ``skip`` or ``take`` is negative.
            ValueError: if ``paths`` is an empty list.
            ValueError: if any of ``paths`` are None.
            ApiException: if the API call fails.
        """
        path_str, keyword_str, prop_str = self._prepare_query(
            paths, keywords, properties, skip, take
        )
        params = {
            "path": path_str,
            "keywords": keyword_str,
            "properties": prop_str,
            "skip": str(skip) if skip is not None else None,
            "take": str(take) if take is not None else None,
        }
        for k, v in list(params.items()):
            if v is None:
                del params[k]
        first_page, http_response = self._api.get("/tags", params=params)
        return HttpTagQueryResultCollection(
            self._http_client,
            path_str,
            keyword_str,
            prop_str,
            skip,
            take,
            first_page,
            http_response,
        )

    async def query_async(
        self,
        paths: Sequence[str] | None = None,
        keywords: Iterable[str] | None = None,
        properties: Dict[str, str] | None = None,
        *,
        skip: int = 0,
        take: int | None = None
    ) -> tbase.AsyncTagQueryResultCollection:
        """Asynchronously query the server for available tags matching the given criteria.

        Args:
            paths: List of tag paths to include in the result. May include glob-style
                wildcards.
            keywords: List of keywords that tags must have, or None.
            properties: Mapping of properties and their values that tags must have, or
                None.
            skip: The number of tags to initially skip in the results.
            take: The number of tags to include in each page of results.

        Returns:
            A task representing the asynchronous operation. On success, contains a
            :class:`TagQueryResultCollection` containing the first page of results.
            Enumerating the collection will retrieve additional pages according to the
            ``take`` parameter.

        Raises:
            ValueError: if ``skip`` is negative.
            ValueError: if ``take`` is negative.
            ApiException: if the API call fails.
        """
        path_str, keyword_str, prop_str = self._prepare_query(
            paths, keywords, properties, skip, take
        )
        params = {
            "path": path_str,
            "keywords": keyword_str,
            "properties": prop_str,
            "skip": str(skip) if skip is not None else None,
            "take": str(take) if take is not None else None,
        }
        for k, v in list(params.items()):
            if v is None:
                del params[k]
        first_page, http_response = await self._api.as_async.get("/tags", params=params)
        return HttpAsyncTagQueryResultCollection(
            self._http_client,
            path_str,
            keyword_str,
            prop_str,
            skip,
            take,
            first_page,
            http_response,
        )

    def _prepare_query(
        self,
        paths: Sequence[str] | None,
        keywords: Iterable[str] | None,
        properties: Dict[str, str] | None,
        skip: int | None,
        take: int | None = None,
    ) -> Tuple[str | None, str | None, str | None]:
        if paths is not None and len(paths) == 0:
            raise ValueError("paths cannot be empty an empty list")
        if paths is not None and any(p is None for p in paths):
            raise ValueError("paths cannot contain None")
        if skip is not None and skip < 0:
            raise ValueError("skip cannot be negative")
        if take is not None and take < 0:
            raise ValueError("take cannot be negative")

        path_str = None
        keyword_str = None
        prop_str = None

        if paths is not None:
            path_str = ",".join(tbase.TagPathUtilities.validate_query(p) for p in paths)
        if keywords:
            keyword_str = ",".join(keywords)
        if properties:
            prop_str = ",".join("{}={}".format(k, v) for k, v in properties.items())

        return path_str, keyword_str, prop_str

    def update(
        self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]
    ) -> None:
        """Update the metadata of one or more tags on the server, creating tags that don't exist.

        If ``updates`` contains :class:`TagData` objects, existing metadata will be
        replaced. If ``updates`` contains :class:`TagDataUpdate` objects instead, tags
        that already exist will have their existing keywords, properties, and settings
        merged with those specified in the corresponding :class:`TagDataUpdate`.

        The call fails if any of the tags already exist as a different data type.

        Args:
            updates: The tags to update (if :class:`TagData` objects are given), or the
                tag metadata updates to send (if :class:`TagDataUpdate` objects are
                given).

        Raises:
            ValueError: if ``updates`` is None or empty.
            ValueError: if ``updates`` contains any invalid tags.
            ValueError: if ``updates`` contains both ``TagData`` objects and
                ``TagDataUpdate`` objects.
            ApiException: if the API call fails.
        """
        tag_models, merge = self._prepare_update(updates)
        partial_success, _ = self._api.post(
            "/update-tags", data={"tags": tag_models, "merge": merge}
        )

        if partial_success is not None:
            err_dict = partial_success.get("error")
            if err_dict is None and "code" in partial_success:
                # SystemLink Cloud has a bug in which it returns the error directly
                # instead of under the "error" key
                err_dict = partial_success
            err_obj = core.ApiError.model_validate(err_dict) if err_dict else None
            if err_dict is None:
                assert False, partial_success
            raise core.ApiException(error=err_obj)

    async def update_async(
        self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]
    ) -> None:
        """Asynchronously update the metadata of one or more tags on the server, creating tags that don't exist.

        If ``updates`` contains :class:`TagData` objects, existing metadata will be
        replaced. If ``updates`` contains :class:`TagDataUpdate` objects instead, tags
        that already exist will have their existing keywords, properties, and settings
        merged with those specified in the corresponding :class:`TagDataUpdate`.

        Args:
            updates: The tags to update (if :class:`TagData` objects are given), or the
                tag metadata updates to send (if :class:`TagDataUpdate` objects are
                given).

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``updates`` is None or empty.
            ValueError: if ``updates`` contains any invalid tags.
            ValueError: if ``updates`` contains both ``TagData`` objects and
                ``TagDataUpdate`` objects.
            ApiException: if the API call fails.
        """
        tag_models, merge = self._prepare_update(updates)
        partial_success, _ = await self._api.as_async.post(
            "/update-tags", data={"tags": tag_models, "merge": merge}
        )

        if partial_success is not None:
            err_dict = partial_success.get("error")
            if err_dict is None and "code" in partial_success:
                # SystemLink Cloud has a bug in which it returns the error directly
                # instead of under the "error" key
                err_dict = partial_success
            err_obj = core.ApiError.model_validate(err_dict) if err_dict else None
            if err_dict is None:
                assert False, partial_success
            raise core.ApiException(error=err_obj)

    def _prepare_update(
        self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]
    ) -> Tuple[List[Dict[str, Any]], bool]:
        if updates is None:
            raise ValueError("updates cannot be None")
        if not updates:
            raise ValueError("updates cannot be empty")
        if not all(isinstance(u, type(updates[0])) for u in updates):
            raise ValueError(
                "updates must contain only TagData objects or TagDataUpdate objects, not both"
            )

        merge = isinstance(updates[0], tbase.TagDataUpdate)

        return [u.to_json_dict() for u in updates], merge

    def delete(self, tags: Iterable[tbase.TagData | str]) -> None:
        """Delete one or more tags from the server.

        Args:
            tags: The tags (or tag paths) to delete.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if ``tags`` contains any invalid tags.
            ApiException: if the API call fails.
        """
        if tags is None:
            raise ValueError("tags cannot be None")
        if any(t is None for t in tags):
            raise ValueError("tags cannot contain None")

        validated_paths = [
            (
                tbase.TagPathUtilities.validate(t)
                if isinstance(t, str)
                else t.validate_path()
            )
            for t in tags
        ]

        self._perform_delete(validated_paths)

    def delete_async(self, tags: Iterable[tbase.TagData | str]) -> Awaitable[None]:
        """Asynchronously delete one or more tags from the server.

        Args:
            tags: The tags (or tag paths) to delete.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if ``tags`` contains any invalid tags.
            ApiException: if the API call fails.
        """
        try:
            if tags is None:
                raise ValueError("tags cannot be None")
            if any(t is None for t in tags):
                raise ValueError("tags cannot contain None")

            validated_paths = [
                (
                    tbase.TagPathUtilities.validate(t)
                    if isinstance(t, str)
                    else t.validate_path()
                )
                for t in tags
            ]
        except Exception as ex:
            f = asyncio.get_event_loop().create_future()
            f.set_exception(ex)
            return f

        return self._perform_delete_async(validated_paths)

    def _perform_delete(self, paths: List[str]) -> None:
        if len(paths) < 4:
            # Few enough to make multiple, single deletes rather than creating a selection.
            exceptions = []

            for path in paths:
                try:
                    self._api.delete(
                        "/tags/{path}",
                        params={"path": tbase.TagPathUtilities.validate(path)},
                    )
                except core.ApiException as ex:
                    exceptions.append(ex)

            if exceptions:
                raise exceptions[0] from None
        else:
            with TemporaryTagSelection.create(self._http_client, paths) as selection:
                self._api.delete("/selections/{id}/tags", params={"id": selection.id})

    async def _perform_delete_async(self, paths: List[str]) -> None:
        if len(paths) < 4:
            # Few enough to make multiple, single deletes rather than creating a selection.
            await asyncio.gather(
                *[
                    self._api.as_async.delete(
                        "/tags/{path}",
                        params={"path": tbase.TagPathUtilities.validate(p)},
                    )
                    for p in paths
                ]
            )
        else:
            async with await TemporaryTagSelection.create_async(
                self._http_client, paths
            ) as selection:
                await self._api.as_async.delete(
                    "/selections/{id}/tags", params={"id": selection.id}
                )

    def create_writer(
        self,
        *,
        buffer_size: int | None = None,
        max_buffer_time: datetime.timedelta | None = None
    ) -> tbase.BufferedTagWriter:
        """Create a tag writer that buffers tag values until
        :meth:`~BufferedTagWriter.send_buffered_writes()` is called on the returned
        object, ``buffer_size`` writes have been buffered, or ``max_buffer_time`` time
        has past since buffering a value, at which point the writes will be sent
        automatically.

        Args:
            buffer_size: The maximum number of tag writes to buffer before automatically
                sending them to the server.
            max_buffer_time: The amount of time before writes are sent.

        Returns:
            The created writer. Close the writer to free resources.

        Raises:
            ValueError: if ``buffer_size`` and ``max_buffer_time`` are both None.
            ValueError: if ``buffer_size`` is less than one.
        """
        if buffer_size is None and max_buffer_time is None:
            raise ValueError("must provide either buffer_size or max_buffer_time")

        if buffer_size is not None:
            if buffer_size < 1:
                raise ValueError("buffer_size cannot be 0 or negative")
        else:
            buffer_size = 0

        if max_buffer_time is not None:
            if max_buffer_time.total_seconds() < 0.001:
                raise ValueError("max_buffer_time must be at least 1 millisecond")
            timer = ManualResetTimer(max_buffer_time)
        else:
            timer = ManualResetTimer.null_timer

        return HttpBufferedTagWriter(
            self._http_client, SystemTimeStamper(), buffer_size, timer
        )

    def _read(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, along with timestamp and/or aggregates, if
            requested, or None if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ApiException: if the API call fails.
        """
        path = tbase.TagPathUtilities.validate(path)

        if include_aggregates:
            response, http_response = self._api.get(
                "/tags/{path}/values", params={"path": path}
            )
            return self._handle_read(
                path, response, http_response, include_timestamp, True
            )
        elif include_timestamp:
            response2, http_response = self._api.get(
                "/tags/{path}/values/current", params={"path": path}
            )
            return self._handle_read(
                path, response2, http_response, include_timestamp, False
            )
        else:
            response3, http_response = self._api.get(
                "/tags/{path}/values/current/value", params={"path": path}
            )
            return self._handle_read(path, response3, http_response)

    async def _read_async(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        """Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ApiException: if the API call fails.
        """
        path = tbase.TagPathUtilities.validate(path)

        if include_aggregates:
            response, http_response = await self._api.as_async.get(
                "/tags/{path}/values", params={"path": path}
            )
            return self._handle_read(
                path, response, http_response, include_timestamp, True
            )
        elif include_timestamp:
            response2, http_response = await self._api.as_async.get(
                "/tags/{path}/values/current", params={"path": path}
            )
            return self._handle_read(
                path, response2, http_response, include_timestamp, False
            )
        else:
            response3, http_response = await self._api.as_async.get(
                "/tags/{path}/values/current/value", params={"path": path}
            )
            return self._handle_read(path, response3, http_response)

    def _handle_read(
        self,
        path: str,
        response: Dict[str, Any],
        http_response: HttpResponse,
        include_timestamp: bool | None = False,
        include_aggregates: bool | None = False,
    ) -> SerializedTagWithAggregates | None:
        if response is None:
            return None

        agg: Dict[str, Any] = response.get("aggregates") or {}
        current: Dict[str, Any] = response.get("current", response)
        if current is None:
            return None

        if "type" in response:
            val = response
        else:
            val = current["value"]
        if val is None:
            return None

        assert "value" in val

        timestamp: datetime.datetime | None = None
        if include_timestamp:
            if current.get("timestamp") is None:
                raise self.invalid_response(http_response)

            timestamp = TimestampUtilities.str_to_datetime(current["timestamp"])

        return SerializedTagWithAggregates(
            path,
            tbase.DataType.from_api_name(val["type"]),
            val["value"],
            timestamp,
            agg.get("count"),
            agg.get("min"),
            agg.get("max"),
            float(agg["avg"]) if agg.get("avg") is not None else None,
        )

    @classmethod
    def invalid_response(cls, response: HttpResponse) -> core.ApiException:
        request = response.request
        return core.ApiException(
            "Invalid response from {} {}".format(request.method, request.url)
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_path_utilities.py sha256=964e8dadd9ecaa16d33fa992d7f10a052e9b4034bf2072bcb3ae99ea2e144266 bytes=1763 -->
## FILE: nisystemlink/clients/tag/_tag_path_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_path_utilities.py`
- sha256: `964e8dadd9ecaa16d33fa992d7f10a052e9b4034bf2072bcb3ae99ea2e144266`
- bytes: 1763

````python
# -*- coding: utf-8 -*-

"""Implementation of TagPathUtilities."""

from typing_extensions import final


@final
class TagPathUtilities:
    """Contains helper methods for interacting with tag paths."""

    def __init_subclass__(cls) -> None:
        raise TypeError("type 'TagPathUtilities' is not an acceptable base type")

    def __init__(self) -> None:
        raise TypeError("Can't instantiate static class 'TagPathUtilities'")

    @classmethod
    def validate(cls, path: str) -> str:
        """Validate ``path`` as an input tag path.

        Clients do not typically need to call this method directly.

        Args:
            path: The tag path to validate.

        Returns:
            The validated path.

        Raises:
            ValueError: if the path is invalid.
            ValueError: if ``path`` is None.
        """
        if path is None or path.lstrip() == "":
            raise ValueError("Tag path cannot be None or empty")

        if "*" in path:
            raise ValueError("Tag path cannot contain a *")

        return path

    @classmethod
    def validate_query(cls, path: str) -> str:
        """Validate ``path`` as a tag path query.

        Clients do not typically need to call this method directly.

        Args:
            path: The tag path to validate.

        Returns:
            The validated path.

        Raises:
            ValueError: if the path is invalid.
            ValueError: if ``path`` is None.
        """
        if path is None or path.lstrip() == "":
            raise ValueError("Tag path cannot be None or empty")

        if "," in path:
            raise ValueError("Tag path cannot contain a ,")

        return path
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_query_result_collection.py sha256=d63857511e776ce4f54146426e8cb7f7bd2ebd239869c68ae8a9540ebb787c3e bytes=2807 -->
## FILE: nisystemlink/clients/tag/_tag_query_result_collection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_query_result_collection.py`
- sha256: `d63857511e776ce4f54146426e8cb7f7bd2ebd239869c68ae8a9540ebb787c3e`
- bytes: 2807

````python
# -*- coding: utf-8 -*-

"""Implementation of TagQueryResultCollection."""

import abc
from typing import Iterable, List

from nisystemlink.clients import core, tag as tbase


class TagQueryResultCollection(abc.ABC):
    """Represents a paginated list of tags returned by a query.

    Iterating over the collection makes additional server requests to retrieve pages
    after the first.
    """

    def __init__(
        self, first_page: List[tbase.TagData], total_count: int, skip: int
    ) -> None:
        """Initialize an instance with the first page of query results.

        Args:
            first_page: The first page of results, or None if there are no results.
            total_count: The total number of results in the query.
            skip: The skip used for the first page of results.
        """
        self._first_page: List[tbase.TagData] | None = None
        if first_page:
            if skip >= total_count:
                raise core.ApiException(
                    "skip is >= totalCount, but the tag list isn't empty"
                )
            self._first_page = first_page
        else:
            pass  # leave it as None, even if passed in as []
        self._use_cached_page = True
        self._total_count = total_count
        self._skip = skip

    @property
    def total_count(self) -> int:  # noqa: D401
        """The total number of tags matched by the query at the time the query was made."""
        return self._total_count

    def __iter__(self) -> Iterable[List[tbase.TagData]]:
        """Enumerate over the pages of tag query results.

        Calls to ``next(iter())`` may throw :class:`.ApiException`.

        Returns:
            The created enumerator.
        """
        skip = self._skip

        if self._use_cached_page:
            self._use_cached_page = False
            page = self._first_page
            self._first_page = None

            if not page:
                return

            skip += len(page)
            yield page

            if skip >= self._total_count:
                return

        while True:
            page = self._query_page(skip)

            if not page:
                return

            skip += len(page)
            yield page

            if skip >= self._total_count:
                break

    @abc.abstractmethod
    def _query_page(self, skip: int) -> List[tbase.TagData]:
        """Query for a single page of results and updates :attr:`total_count`.

        Args:
            skip: The skip to use in the query.

        Returns:
            The page of results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_selection.py sha256=ea2dc29e7bcfb1ce6be05e33b2710fc08fe478a8de10812d23b6837c2bf2616f bytes=31575 -->
## FILE: nisystemlink/clients/tag/_tag_selection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_selection.py`
- sha256: `ea2dc29e7bcfb1ce6be05e33b2710fc08fe478a8de10812d23b6837c2bf2616f`
- bytes: 31575

````python
# -*- coding: utf-8 -*-

"""Implementation of TagSelection."""

import abc
import asyncio
import datetime
from types import TracebackType
from typing import Awaitable, Dict, List, Sequence, Tuple, Type

from nisystemlink.clients import tag as tbase
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)


class TagSelection(tbase.ITagReader):
    """Represents a set of tags that can be read, written, or deleted together.

    Tags may be specified using glob-style wildcards to include multiple tags with a
    common path. Call :meth:`close()` to free resources. Tag reads are buffered, and the
    latest values are only retrieved on first read or by calling
    :meth:`refresh_values()`. Reads for tags that aren't in the selection return None,
    even if the tag exists on the server.

    Note that :class:`TagSelection` objects support using the ``with`` statement (or the
    ``async with`` statement), to :meth:`close()` the selection automatically on exit.
    """

    def __init__(
        self, tags: Sequence[tbase.TagData], paths: Sequence[str] | None = None
    ) -> None:
        """Initialize a selection using queried or existing tag data.

        Args:
            tags: The tags to store in the selection.
            paths: The paths used to query the tags. If left as None, the paths will be
                extracted from ``tags``.

        Raises:
            ValueError: if ``tags`` is None or empty.
            ValueError: if ``tags`` or ``paths`` contains duplicate tags.
        """
        self._closed = False

        if tags is None:
            raise ValueError("tags cannot be None")
        if any(t is None for t in tags):
            raise ValueError("tags cannot contain None")
        if any(not t.path for t in tags):
            raise ValueError("tags cannot contain a tag with an empty path")

        self._metadata = {m.path: m for m in tags}
        if len(self._metadata) != len(tags):
            raise ValueError("tags contains duplicate paths")

        if paths is None:
            self._paths = set(self._metadata.keys())
        else:
            if any(p is None for p in paths):
                raise ValueError("paths cannot contain None")
            self._paths = set(paths)
            if len(self._paths) != len(paths):
                raise ValueError("paths contains duplicates")

        self._readers = {
            r.path: r
            for r in (self._create_value_reader(m) for m in self._metadata.values())
            if r is not None
        }

        self._values: Dict[str, SerializedTagWithAggregates] | None = None

    @property
    def paths(self) -> Tuple[str, ...]:  # noqa: D401
        """The paths of all tags in the selection, including those that do not exist on the server.

        When using wildcards, the original paths with the wildcards are included in the
        list, not the paths matched by the wildcards.
        """
        return tuple(self._paths)

    @property
    def metadata(self) -> Dict[str, tbase.TagData]:  # noqa: D401
        """The most recently retrieved metadata for tags in the selection, indexed by :attr:`TagData.path`.

        Tags in the selection that do not exist on the server will not appear in the
        collection. Call :meth:`refresh_metadata()` to update the data contained in the
        collection.
        """
        return dict(self._metadata)

    @property
    def values(self) -> Dict[str, tbase.TagValueReader]:  # noqa: D401
        """A :class:`.TagValueReader` for reading the most recently retrieved value for
        tags in the selection, indexed by :attr:`.TagValueReader.path`.

        Tags in the selection that do not exist on the server will not appear in the
        collection. Readers for tags without values on the server will return None when
        read. Call :meth:`refresh_values()` to update the values returned by the readers
        in the dictionary.
        """
        return dict(self._readers)

    @abc.abstractmethod
    def _close_internal(self) -> None:
        """Clean up server resources associated with the selection."""
        ...

    @abc.abstractmethod
    async def _close_internal_async(self) -> None:
        """Asynchronously clean up server resources associated with the selection.

        Returns:
            A task representing the asynchronous operation.
        """
        ...

    @abc.abstractmethod
    def _create_subscription_internal(
        self, update_interval: datetime.timedelta | None = None
    ) -> tbase.TagSubscription:
        """Subscribe to receive events when tags in the selection are written to using the specified update interval.

        Args:
            update_interval: How often to receive tag update notifications from the
                server, or None to use the default.

        Returns:
            The created subscription.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _create_subscription_internal_async(
        self, update_interval: datetime.timedelta | None = None
    ) -> tbase.TagSubscription:
        """Asynchronously subscribe to receive events when tags in the selection are
        written to using the specified update interval.

        Args:
            update_interval: How often to receive tag update notifications from the
                server, or None to use the default.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created subscription.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _delete_tags_from_server_internal(self) -> None:
        """Delete all tags in the selection from the server.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _delete_tags_from_server_internal_async(self) -> None:
        """Asynchronously delete all tags in the selection from the server.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _read_tag_metadata(self) -> List[tbase.TagData]:
        """Retrieve the metadata of all tags in the selection.

        Returns:
            The list of tag metadata.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _read_tag_values(self) -> List[SerializedTagWithAggregates | None]:
        """Retrieve the values of all tags in the selection.

        Returns:
            The list of the tag values.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _read_tag_metadata_and_values(
        self,
    ) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]:
        """Retrieve the metadata and values of all tags in the selection.

        Returns:
            A tuple with the list of tag metadata and the list of tag values.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _read_tag_metadata_async(self) -> List[tbase.TagData]:
        """Asynchronously retrieve the metadata of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains the
            list of tag metadata.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _read_tag_values_async(
        self,
    ) -> List[SerializedTagWithAggregates | None]:
        """Asynchronously retrieve the values of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains the
            list of the tag values.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _read_tag_metadata_and_values_async(
        self,
    ) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]:
        """Asynchronously retrieve the metadata and values of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains a
            tuple with the list of tag metadata and the list of tag values.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _reset_aggregates_internal(self) -> None:
        """Reset the aggregate values of tags in the selection.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _reset_aggregates_internal_async(self) -> None:
        """Asynchronously reset the aggregate values of tags in the selection.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    def _on_paths_changed(self) -> None:
        """Note when the contents of :attr:`paths` is modified.

        The default implementation does nothing.
        """
        pass

    def add_tags(self, tags: List[tbase.TagData]) -> None:
        """Add one or more tags to the selection.

        Tags that are already in the selection are ignored. The tags as given are
        immediately available in the :attr:`metadata` collection. Use
        :meth:`refresh_metadata()` to get the latest data for the tags. The tags will be
        available in the :attr:`values` collection but won't have latest a latest value
        until :meth:`refresh_values()` is called.

        Args:
            tags: The tags to add to the selection.

        Raises:
            ValueError: if any of the given tags are None or have an invalid path.
            ValueError: if ``tags`` is None.
            ReferenceError: if the selection has been closed.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        for tag in self._validate_tags(tags):
            self._paths.add(tag.path)

            # Don't overwrite existing.
            if tag.path not in self._metadata:
                self._metadata[tag.path] = tag
                reader = self._create_value_reader(tag)
                if reader is not None:
                    self._readers[tag.path] = reader

        self._on_paths_changed()

    def clear_tags(self) -> None:
        """Remove all tags from the selection.

        Raises:
            ReferenceError: if the selection has been closed.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        self._paths.clear()
        self._metadata.clear()
        self._readers.clear()

        self._on_paths_changed()

    def close(self) -> None:
        """Clean up server resources associated with the selection."""
        if self._closed:
            return

        self._close_internal()
        self._closed = True
        paths = getattr(self, "_paths", None)
        if paths is not None:
            paths.clear()
        metadata = getattr(self, "_metadata", None)
        if metadata is not None:
            metadata.clear()
        readers = getattr(self, "_readers", None)
        if readers is not None:
            readers.clear()
        values = getattr(self, "_values", None)
        if values is not None:
            values.clear()

    async def close_async(self) -> None:
        """Asynchronously clean up server resources associated with the selection.

        Returns:
            A task representing the asynchronous operation.
        """
        if self._closed:
            return

        await self._close_internal_async()
        self._closed = True
        self._paths.clear()
        self._metadata.clear()
        self._readers.clear()
        if self._values is not None:
            self._values.clear()

    def create_subscription(
        self, *, update_interval: datetime.timedelta | None = None
    ) -> tbase.TagSubscription:
        """Subscribe to receive events when tags in the selection are written to.

        Updates will be queried from the server using the specified or default update
        interval.

        The subscription will include any tags that are currently included in the
        selection when the subscription is created. That list can be seen via the
        :attr:`metadata` property. The subscription will also attempt to include any
        non-wildcard paths that are in the selection's current list of :attr:`paths`.
        Often, the list of :attr:`paths` directly coincides with the :attr:`metadata`,
        but the former may contain paths that did not exist when the selection's
        metadata was last updated from the server, e.g. via :meth:`refresh()`.

        Closing, adding tags, or removing tags from the selection will not affect
        previously created subscriptions.

        Args:
            update_interval: How often to receive tag updates notifications from the
                server. Default is ``datetime.timedelta(seconds=30)``.

        Returns:
            The created subscription.

        Raises:
            ValueError: if update_interval is negative.
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        if update_interval is not None and update_interval.total_seconds() < 0:
            raise ValueError("update_interval cannot be negative")

        return self._create_subscription_internal(update_interval)

    def create_subscription_async(
        self, *, update_interval: datetime.timedelta | None = None
    ) -> Awaitable[tbase.TagSubscription]:
        """Asynchronously subscribe to receive events when tags in the selection are written to.

        Updates will be queried from the server using the specified or default update
        interval.

        Closing, adding tags, or removing tags from the selection will not affect
        previously created subscriptions.

        Args:
            update_interval: How often to receive tag updates notifications from the
                server. Depending on the :class:`TagManager` implementation in use, this
                may involve polling the server or have a minimum value.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created subscription.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            f = asyncio.get_event_loop().create_future()
            f.set_exception(ReferenceError("TagSelection"))
            return f

        if update_interval and update_interval.total_seconds() < 0:
            f = asyncio.get_event_loop().create_future()
            f.set_exception(ValueError("update_interval cannot be negative"))
            return f

        return self._create_subscription_internal_async(update_interval)

    def delete_tags_from_server(self) -> None:
        """Delete all tags in the selection from the server.

        The tags are not removed from the selection but are removed from
        :attr:`metadata` and :attr:`values`. If any of the tags are recreated, a call to
        :meth:`refresh_metadata()` will restore them in the collection of tags.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        self._delete_tags_from_server_internal()
        self._metadata.clear()
        self._readers.clear()
        if self._values is not None:
            self._values.clear()

    async def delete_tags_from_server_async(self) -> None:
        """Asynchronously delete all tags in the selection from the server.

        The tags are not removed from the selection but are removed from
        :attr:`metadata` and :attr:`values`. If any of the tags are recreated, a call to
        :meth:`refresh_metadata()` will restore them in the collection of tags.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        await self._delete_tags_from_server_internal_async()
        self._metadata.clear()
        self._readers.clear()
        if self._values is not None:
            self._values.clear()

    def open_tags(self, paths: List[str]) -> None:
        """Add one or more tags to the selection by path.

        Tags that are already in the selection are ignored. The tags will not be
        available in the :attr:`metadata` collection until :meth:`refresh_metadata()` is
        called or the :attr:`values` collection until :meth:`refresh_values()` is
        called.

        Args:
            paths: The tag paths to add to the selection. May include glob-style
                wildcards.

        Raises:
            ValueError: if any of the given paths are None or invalid.
            ValueError: if ``paths`` is None.
            ReferenceError: if the selection has been closed.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        self._paths.update(self._validate_paths(paths))
        self._on_paths_changed()

    def refresh(self) -> None:
        """Refresh both :class:`TagData` and current values for all tags in the
        selection, updating :attr:`metadata` and :attr:`values` accordingly.

        Call :meth:`refresh_metadata()` or :meth:`refresh_values()` to only partially
        refresh.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        metadata, values = self._read_tag_metadata_and_values()
        self._update_metadata(metadata)
        self._update_values(values)

    async def refresh_async(self) -> None:
        """Asynchronously refresh both the :class:`TagData` and current values for all
        tags in the selection, updating :attr:`metadata` and :attr:`values` accordingly.

        Call :meth:`refresh_metadata_async()` or :meth:`refresh_values_async()` to only
        partially refresh.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        metadata, values = await self._read_tag_metadata_and_values_async()
        self._update_metadata(metadata)
        self._update_values(values)

    def refresh_metadata(self) -> None:
        """Refresh the :class:`TagData` for all tags in the selection, updating :attr:`metadata` accordingly.

        :attr:`values` will also be updated with new and removed tags, but those readers
        will continue to return previously available values until
        :meth:`refresh_values()` is called.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        metadata = self._read_tag_metadata()
        self._update_metadata(metadata)

    async def refresh_metadata_async(self) -> None:
        """Asynchronously refresh the :class:`TagData` for all tags in the selection,
        updating :attr:`metadata` accordingly.

        :attr:`values` will also be updated with new and removed tags, but those readers
        will continue to return previously available values until
        :meth:`refresh_values()` is called.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        metadata = await self._read_tag_metadata_async()
        self._update_metadata(metadata)

    def refresh_values(self) -> None:
        """Refresh the current value of tags in the selection returned by the readers in the :attr:`values` collection.

        Readers will return None for tags that no longer exist on the server, or exist
        but haven't yet been written to. New readers will be added to the collection for
        tags that have values but have not yet been added to :attr:`metadata` by a call
        to :meth:`refresh_metadata()`.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        values = self._read_tag_values()
        self._update_values(values)

    async def refresh_values_async(self) -> None:
        """Asynchronously refresh the current value of tags in the selection returned by
        the readers in the :attr:`values` collection.

        Readers will return None for tags that no longer exist on the server, or exist
        but haven't yet been written to. New readers will be added to the collection for
        tags that have values but have not yet been added to :attr:`metadata` by a call
        to :meth:`refresh_metadata()`.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        values = await self._read_tag_values_async()
        self._update_values(values)

    def remove_tags(self, tags: List[tbase.TagData | str]) -> None:
        """Remove one or more tags from the selection.

        The tags are not removed from the :attr:`metadata` and :attr:`values`
        collections until the next :meth:`refresh_metadata()`.

        Tags not in the selection are ignored. Tags that were added to the selection
        using wildcard paths can only be removed by including the same wildcard paths.
        Tags matched by multiple wildcard paths remain in the selection until all of the
        paths are removed.

        Args:
            tags: The tags to remove from the selection. Either strings (paths) or
                :class:`TagData` objects can be given. For :class:`TagData` objects,
                only the :attr:`TagData.path` is used.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if any of the given tags are None or have an invalid path.
            ReferenceError: if the selection has been closed.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        if tags is None:
            raise ValueError("tags cannot be None")

        paths = [t for t in tags if isinstance(t, str)]
        tags_ = [t for t in tags if not isinstance(t, str)]

        self._paths.difference_update(self._validate_paths(paths))
        self._paths.difference_update(t.path for t in self._validate_tags(tags_))

        self._on_paths_changed()

    def reset_aggregates(self) -> None:
        """Reset tag value aggregates on the server for all tags in the selection.

        Tag historical values are not modified. Has no effect on tags that are not set
        to :attr:`TagData.collect_aggregates`. Use :meth:`refresh_values()` to retrieve
        the new aggregates.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            raise ReferenceError("TagSelection")

        self._reset_aggregates_internal()

    def reset_aggregates_async(self) -> Awaitable[None]:
        """Asynchronously reset tag value aggregates on the server for all tags in the selection.

        Tag historical values are not modified. Has no effect on tags that are not set
        to :attr:`TagData.collect_aggregates`. Use :meth:`refresh_values()` to retrieve
        the new aggregates.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        """
        if self._closed:
            f = asyncio.get_event_loop().create_future()
            f.set_exception(ReferenceError("TagSelection"))
            return f

        return self._reset_aggregates_internal_async()

    def __enter__(self) -> "TagSelection":
        return self

    async def __aenter__(self) -> "TagSelection":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Clean up resources associated with the selection."""
        self.close()

    def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Awaitable[None]:
        """Asynchronously clean up resources associated with the selection."""
        return self.close_async()

    def __del__(self) -> None:
        """Finalize resources associated with the selection."""
        self.close()

    def _read(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        if self._closed:
            raise ReferenceError("TagSelection")

        if path is None:
            raise ValueError("path cannot be None")

        if self._values is None:
            self.refresh_values()
            assert self._values is not None

        if path in self._values:
            return self._values[path]
        elif path in self._readers:
            return None
        else:
            raise ValueError("Cannot read a tag that is not in the selection")

    async def _read_async(
        self, path: str, include_timestamp: bool, include_aggregates: bool
    ) -> SerializedTagWithAggregates | None:
        if self._closed:
            raise ReferenceError("TagSelection")

        if path is None:
            raise ValueError("path cannot be None")

        if self._values is None:
            await self.refresh_values_async()
            assert self._values is not None

        if path in self._values:
            return self._values[path]
        elif path in self._readers:
            return None
        else:
            raise ValueError("Cannot read a tag that is not in the selection")

    def _create_value_reader(self, tag: tbase.TagData) -> tbase.TagValueReader | None:
        if tag is None:
            raise ValueError("tag cannot be None")

        if tag.data_type == tbase.DataType.UNKNOWN:
            return None
        else:
            return tbase.TagValueReader(self, tag)

    def _update_metadata(self, metadata: List[tbase.TagData]) -> None:
        missing_paths = set(self._metadata.keys()).difference(t.path for t in metadata)
        for missing_path in missing_paths:
            del self._metadata[missing_path]
            if missing_path in self._readers:
                del self._readers[missing_path]
            if self._values is not None and missing_path in self._values:
                del self._values[missing_path]

        for tag in metadata:
            old_tag = self._metadata.get(tag.path)
            if old_tag is None or old_tag.data_type != tag.data_type:
                reader = self._create_value_reader(tag)
                if reader is not None:
                    self._readers[tag.path] = reader

            self._metadata[tag.path] = tag

    def _update_values(self, values: List[SerializedTagWithAggregates | None]) -> None:
        if self._values is None:
            self._values = {}

        missing_values = set(self._values.keys()).difference(
            v.path for v in values if v is not None
        )
        for missing_path in missing_values:
            del self._values[missing_path]

        for value in values:
            if value is None:
                continue

            self._values[value.path] = value

            tag = self._metadata.get(value.path)
            if tag is None:
                tag = tbase.TagData(value.path, value.data_type)
                self._metadata[value.path] = tag
            elif tag.data_type != value.data_type:
                tag.data_type = value.data_type
            else:
                continue

            reader = self._create_value_reader(tag)
            if reader is not None:
                self._readers[value.path] = reader

    @classmethod
    def _validate_paths(cls, paths: List[str]) -> List[str]:
        """Validate that the given tag paths are valid for queries.

        Args:
            paths: The paths to validate.

        Returns:
            The validated paths.

        Raises:
            ValueError: if any of the given paths are None or invalid.
            ValueError: if ``paths`` is None.
        """
        ...
        if paths is None:
            raise ValueError("paths cannot be None")

        for path in paths:
            if path is None:
                raise ValueError("paths cannot contain None")
            tbase.TagPathUtilities.validate_query(path)

        return paths

    @classmethod
    def _validate_tags(cls, tags: List[tbase.TagData]) -> List[tbase.TagData]:
        """Validate that the given tags have valid paths.

        Args:
            tags: The tags to validate.

        Returns:
            The validated tags.

        Raises:
            ValueError: if any of the given tags are None or have an invalid path.
            ValueError: if ``tags`` is None.
        """
        ...
        if tags is None:
            raise ValueError("tags cannot be None")

        for tag in tags:
            if tag is None:
                raise ValueError("tags cannot contain None")
            tag.validate_path()

        return tags
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_subscription.py sha256=b202e32f71edea5b2970a7307ff98832bb01e0dab44ce6ebcf5fde081224ff3d bytes=8955 -->
## FILE: nisystemlink/clients/tag/_tag_subscription.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_subscription.py`
- sha256: `b202e32f71edea5b2970a7307ff98832bb01e0dab44ce6ebcf5fde081224ff3d`
- bytes: 8955

````python
# -*- coding: utf-8 -*-

"""Implementation of TagSubscription."""

import abc
import contextlib
import datetime
import weakref
from types import TracebackType
from typing import Iterable, List, Type

import events
from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer


class TagSubscription(events.Events, abc.ABC):
    """Represents a subscription for changes to one or more tags' values.

    Call :meth:`close()` to stop receiving events.

    Note that :class:`TagSubscription` objects support using the ``with`` statement (or
    the ``async with`` statement), to :meth:`close()` the subsription automatically on
    exit.

    Attributes:
        tag_changed: An event that is triggered when one of the subscription's tag
            changes. The callback will receive a :class:`TagData` parameter and an
            :class:`Optional` [:class:`TagValueReader`] parameter.

            Example::

                def my_callback(tag: TagData, reader: TagValueReader | None):
                    print("{} changed".format(tag.path))
                    if reader is None:
                        print(" - unknown data type")
                    else:
                        value = reader.read()
                        assert value is not None
                        print(" - new value: {}".format(value.value))

                subscription.tag_changed += my_callback
    """

    __events__ = ["tag_changed"]
    # Under certain circumstances, mypy complains about the event not having a type hint
    # unless we specify it explicitly. (But we also need to delete the attribute so that
    # Events.__getattr__ can do its magic.)
    tag_changed = None  # type: events._EventSlot
    del tag_changed

    _HEARTBEAT_INTERVAL_MILLISECONDS = 30000.0
    """Send a heartbeat every 30 seconds based on a server-side expiration of 60 seconds."""

    def __init__(
        self, paths: Iterable[str], heartbeat_timer: ManualResetTimer | None
    ) -> None:
        """Initialize the instance.

        Derived types must call :meth:`_initialize()` or :meth:`_initialize_async()`
        after construction.

        Args:
            paths: The tag path queries to include in the subscription.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive for testing purposes, or None to use a default timer.

        Raises:
            ValueError: if ``paths`` is None.
        """
        if paths is None:
            raise ValueError("paths cannot be None")

        super().__init__()
        self._paths = list(paths)
        if heartbeat_timer is not None:
            self._heartbeat_timer = heartbeat_timer
        else:
            self._heartbeat_timer = ManualResetTimer(
                datetime.timedelta(milliseconds=self._HEARTBEAT_INTERVAL_MILLISECONDS)
            )
        self._exit_stack = contextlib.ExitStack()
        self._exit_stack.enter_context(self._heartbeat_timer)

        callback_ref = weakref.WeakMethod(self._heartbeat_timer_elapsed)  # type: ignore

        def callback() -> None:
            actual_callback = callback_ref()  # type: ignore
            if actual_callback:
                actual_callback()

        self._heartbeat_timer_handler = callback
        self._heartbeat_timer.elapsed += self._heartbeat_timer_handler
        self._closed = False

    def __del__(self) -> None:
        self._exit_stack.close()

    def _initialize(self) -> None:
        """Create and initialize the subscription.

        Derived types must call this method or :meth:`_initialize_async()` after
        construction to create and keep the subscription alive.

        Raises:
            ApiException: if the API call fails.
        """
        self._create_subscription_on_server(self._paths)
        self._heartbeat_timer.start()

    async def _initialize_async(self) -> None:
        """Asynchronously create and initializes the subscription.

        Derived types must call this method or :meth:`_initialize()` after construction
        to create and keep the subscription alive.

        Raises:
            ApiException: if the API call fails.
        """
        await self._create_subscription_on_server_async(self._paths)
        self._heartbeat_timer.start()

    @abc.abstractmethod
    def _create_subscription_on_server(self, paths: List[str]) -> None:
        """Create the subscription on the server.

        Implementations should retrieve and throw away the first set of updates before
        returning.

        Args:
            paths: The tag path queries to include in the subscription.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    async def _create_subscription_on_server_async(self, paths: List[str]) -> None:
        """Asynchronously create the subscription on the server.

        Implementations should retrieve and throw away the first set of updates before
        returning.

        Args:
            paths: The tag path queries to include in the subscription.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _send_heartbeat(self) -> None:
        """Send a heartbeat for the subscription to keep it active.

        Raises:
            ApiException: if the API call fails.
        """
        ...

    @abc.abstractmethod
    def _close_internal(self) -> None:
        """Clean up server resources associated with the subscription."""
        ...

    @abc.abstractmethod
    async def _close_internal_async(self) -> None:
        """Asynchronously clean up server resources associated with the subscription.

        Returns:
            A task representing the asynchronous operation.
        """
        ...

    def close(self) -> None:
        """Close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        """
        if self._closed:
            return

        self._close_internal()
        self._heartbeat_timer.elapsed -= self._heartbeat_timer_handler
        self._closed = True

    async def close_async(self) -> None:
        """Asynchronously close server resources associated with the subscription.

        Further tag writes will not trigger new events.

        Returns:
            A task representing the asynchronous operation.
        """
        if self._closed:
            return

        await self._close_internal_async()
        self._heartbeat_timer.elapsed -= self._heartbeat_timer_handler
        self._closed = True

    def __enter__(self) -> "TagSubscription":
        return self

    async def __aenter__(self) -> "TagSubscription":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        """Close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        """
        suppress: bool | None = False
        try:
            self.close()
        finally:
            suppress = self._exit_stack.__exit__(exc_type, exc_val, exc_tb)
        return suppress

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        """Asynchronously close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        """
        suppress: bool | None = False
        try:
            await self.close_async()
        finally:
            suppress = self._exit_stack.__exit__(exc_type, exc_val, exc_tb)
        return suppress

    def _on_tag_changed(
        self, tag: tbase.TagData, value: tbase.TagValueReader | None
    ) -> None:
        """Raise the :attr:`tag_changed` event.

        Args:
            tag: The tag that was changed.
            value: The new value and any associated information, or None if the tag has
                an unknown data type.
        """
        self.tag_changed(tag, value)

    def _heartbeat_timer_elapsed(self) -> None:
        try:
            self._send_heartbeat()
        except core.ApiException:
            try:
                self._create_subscription_on_server(self._paths)
            except core.ApiException:
                # Ignore, we'll try again later
                pass

        self._heartbeat_timer.start()
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_update_fields.py sha256=3cb4564c4ce086a7e5ce7078c873301d813d8d77fca87011b9ebbd98ea62a36e bytes=1390 -->
## FILE: nisystemlink/clients/tag/_tag_update_fields.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_update_fields.py`
- sha256: `3cb4564c4ce086a7e5ce7078c873301d813d8d77fca87011b9ebbd98ea62a36e`
- bytes: 1390

````python
# -*- coding: utf-8 -*-

"""Implementation of TagUpdateFields."""

import sys

if sys.version_info < (3, 6):
    import aenum as enum  # type: ignore
else:
    import enum


class TagUpdateFields(enum.IntFlag):
    """Represents the various :class:`TagData` fields that may be included in a :class:`TagDataUpdate`.

    Fields that aren't included are left unmodified when updates are sent to the server.
    """

    KEYWORDS = 1
    """Specify that entries in the :attr:`TagData.keywords` that are missing from the
    tag's metadata on the server will be added.
    """

    PROPERTIES = 2
    """Specify that entries in the :attr:`TagData.properties` that are missing from or
    different in the tag's metadata on the server will be added or replaced.
    """

    COLLECT_AGGREGATES = 4
    """Specify that the tag's :attr:`TagData.collect_aggregates` setting will be modified on the server."""

    RETENTION = 8
    """Specify that the tag's :attr:`TagData.retention_type`,
    :attr:`TagData.retention_count`, and :attr:`TagData.retention_days` settings will be
    modified on the server.
    """

    ALL = 15
    """Specify that all fields in the :class:`TagData` should be included in the update.

    Keywords and properties that already exist on the server will not be removed, even
    if they are missing from the update.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_value_reader.py sha256=8bdcffc2078b6eec018f89c2f304346661f465563fb43af49552a16fb0683caf bytes=3893 -->
## FILE: nisystemlink/clients/tag/_tag_value_reader.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_value_reader.py`
- sha256: `8bdcffc2078b6eec018f89c2f304346661f465563fb43af49552a16fb0683caf`
- bytes: 3893

````python
# -*- coding: utf-8 -*-

"""Implementation of TagValueReader."""

from typing import Generic, TypeVar

from nisystemlink.clients import core, tag as tbase

_Any = TypeVar("_Any")


class TagValueReader(Generic[_Any]):
    """Represents the ability to read a single tag's value using an :class:`ITagReader`."""

    def __init__(self, reader: tbase.ITagReader, tag: tbase.TagData) -> None:
        """Initialize an instance.

        Args:
            reader: The :class:`ITagReader` to use when reading values.
            tag: The tag whose values will be read.
            path: The path of the tag whose values will be read.

        Raises:
            ValueError: if ``tag`` is not a tag of a valid data type and with a valid
                path.
        """
        if tag.data_type == tbase.DataType.UNKNOWN:
            raise ValueError("tag.data_type cannot be UNKNOWN")

        self._path = tag.validate_path()
        self._data_type = tag.data_type
        self.__reader = reader

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type of the tag associated with the value."""
        return self._data_type

    @property
    def path(self) -> str:  # noqa: D401
        """The path of the tag associated with the value."""
        return self._path

    @property
    def _reader(self) -> tbase.ITagReader:  # noqa: D401
        """The underlying :class:`ITagReader` for reading values."""
        return self.__reader

    def read(
        self, *, include_timestamp: bool = False, include_aggregates: bool = False
    ) -> tbase.TagWithAggregates[_Any] | None:
        """Read the current value of the tag.

        Args:
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ReferenceError: if the underlying reader has been closed.
            ApiException: if the API call fails.
        """
        ret = self._reader.read(
            self._path,
            include_timestamp=include_timestamp,
            include_aggregates=include_aggregates,
        )
        if ret is None:
            return None
        if ret.data_type != self.data_type:
            raise core.ApiException("Tag data type does not match")

        return ret

    async def read_async(
        self, *, include_timestamp: bool = False, include_aggregates: bool = False
    ) -> tbase.TagWithAggregates[_Any] | None:
        """Read the current value of the tag.

        Args:
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ReferenceError: if the underlying reader has been closed.
            ApiException: if the API call fails.
        """
        ret = await self._reader.read_async(
            self._path,
            include_timestamp=include_timestamp,
            include_aggregates=include_aggregates,
        )
        if ret is None:
            return None
        if ret.data_type != self.data_type:
            raise core.ApiException("Tag data type does not match")

        return ret
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_value_writer.py sha256=8561e813c37d7957c347527cceca16b20355bac161c4f573f3596c31c968d3cf bytes=2805 -->
## FILE: nisystemlink/clients/tag/_tag_value_writer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_value_writer.py`
- sha256: `8561e813c37d7957c347527cceca16b20355bac161c4f573f3596c31c968d3cf`
- bytes: 2805

````python
# -*- coding: utf-8 -*-

"""Implementation of TagValueWriter."""

import datetime
import typing
from typing import Any, Awaitable, Generic, TypeVar

from nisystemlink.clients import tag as tbase

_Any = TypeVar("_Any")


class TagValueWriter(Generic[_Any]):
    """Represents the ability to write a single tag's value using an :class:`ITagWriter`."""

    def __init__(self, writer: tbase.ITagWriter, tag: tbase.TagData) -> None:
        """Initialize an instance.

        Args:
            writer: The :class:`ITagWriter` to use when writing values.
            tag: The tag whose values will be written.
            path: The path of the tag whose values will be written.

        Raises:
            ValueError: if ``tag`` is not a tag of a valid type and with a valid path.
        """
        if tag.data_type == tbase.DataType.UNKNOWN:
            raise ValueError("tag.type cannot be UNKNOWN")

        self._path = tag.validate_path()
        self._data_type = tag.data_type
        self.__writer = writer

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type of the tag associated with the value."""
        return self._data_type

    @property
    def path(self) -> str:  # noqa: D401
        """The path of the tag associated with the value."""
        return self._path

    @property
    def _writer(self) -> tbase.ITagWriter:  # noqa: D401
        """The underlying :class:`ITagWriter` for writing values."""
        return self.__writer

    def write(self, value: _Any, *, timestamp: datetime.datetime | None = None) -> None:
        """Write the tag's value.

        Args:
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ReferenceError: if the underlying writer has been closed.
            ApiException: if the API call fails.
        """
        self._writer.write(
            self._path, self._data_type, typing.cast(Any, value), timestamp=timestamp
        )

    def write_async(
        self, value: _Any, *, timestamp: datetime.datetime | None = None
    ) -> Awaitable[None]:
        """Write the tag's value.

        Args:
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ReferenceError: if the underlying writer has been closed.
            ApiException: if the API call fails.
        """
        return self._writer.write_async(
            self._path, self._data_type, typing.cast(Any, value), timestamp=timestamp
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_with_aggregates.py sha256=c05885350071d8441ba749d46e6a1f163d5badffb4d888c77d8d68313173fcd6 bytes=4475 -->
## FILE: nisystemlink/clients/tag/_tag_with_aggregates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/tag/_tag_with_aggregates.py`
- sha256: `c05885350071d8441ba749d46e6a1f163d5badffb4d888c77d8d68313173fcd6`
- bytes: 4475

````python
# -*- coding: utf-8 -*-

"""Implementation of TagWithAggregates."""

import datetime
import math
from typing import Generic, TypeVar

from nisystemlink.clients import core, tag as tbase

_NUMERIC_TYPES = set(
    (tbase.DataType.DOUBLE, tbase.DataType.INT32, tbase.DataType.UINT64)
)

_Any = TypeVar("_Any")


class TagWithAggregates(Generic[_Any]):
    """Represents a generic tag value with optional timestamp and optional aggregate values."""

    def __init__(
        self,
        path: str,
        data_type: tbase.DataType,
        value: _Any,
        timestamp: datetime.datetime | None = None,
        count: int | None = None,
        min: int | float | None = None,
        max: int | float | None = None,
        mean: float | None = None,
    ) -> None:
        """Initialize an instance.

        Args:
            path: The path of the tag associated with the value.
            data_type: The data type of the value.
            value: The value.
            timestamp: The timestamp associated with the value.
            count: The number of times the tag has been written, or None if the tag is
                not collecting aggregates.
            min: The minimum value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a minimum value.
            max: The maximum value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a maximum value.
            mean: The mean value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a mean value.

        Raises:
            ApiException: if min, max, or mean is None when it shouldn't be or non-None
                when it should be

        :meta private:
        """
        if data_type in _NUMERIC_TYPES:
            if count is not None:
                if mean is None or min is None or max is None:
                    # TODO: Error information
                    raise core.ApiException()
            elif min is not None or max is not None or mean is not None:
                # TODO: Error information: only valid if count is set
                raise core.ApiException()
        else:
            if (
                min is not None
                or max is not None
                or (mean is not None and not math.isnan(mean))
            ):
                # TODO: Error information: not supported for non-numerics
                raise core.ApiException()

        self._path = path
        self._data_type = data_type
        self._value = value
        self._timestamp = timestamp
        self._count = count
        self._min = min
        self._max = max
        self._mean = mean

    @property
    def data_type(self) -> tbase.DataType:  # noqa: D401
        """The data type of the value."""
        return self._data_type

    @property
    def path(self) -> str:  # noqa: D401
        """The path of the tag associated with the value."""
        return self._path

    @property
    def value(self) -> _Any:  # noqa: D401
        """The value of the tag."""
        return self._value

    @property
    def timestamp(self) -> datetime.datetime | None:  # noqa: D401
        """The timestamp associated with the value, if available."""
        return self._timestamp

    @property
    def count(self) -> int | None:  # noqa: D401
        """The number of times the tag has been written, or None if the tag is not collecting aggregates."""
        return self._count

    @property
    def min(self) -> int | float | None:  # noqa: D401
        """The minimum value of the tag, or None if the tag is not collecting aggregates
        or the data type of the tag does not track a minimum value.
        """
        return self._min

    @property
    def max(self) -> int | float | None:  # noqa: D401
        """The maximum value of the tag, or None if the tag is not collecting aggregates
        or the data type of the tag does not track a maximum value.
        """
        return self._max

    @property
    def mean(self) -> float | None:  # noqa: D401
        """The mean value of the tag, or None if the tag is not collecting aggregates or
        the data type of the tag does not track a mean value.
        """
        return self._mean
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/__init__.py sha256=97787c6cd0e9ba4d05211037f5a115cbf094d0f5763c056e156e564c0801e014 bytes=145 -->
## FILE: nisystemlink/clients/test_plan/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/__init__.py`
- sha256: `97787c6cd0e9ba4d05211037f5a115cbf094d0f5763c056e156e564c0801e014`
- bytes: 145

````python
"""Start here with TestPlanClient for test plan management."""

from ._test_plan_client import TestPlanClient

__all__ = ["TestPlanClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/_test_plan_client.py sha256=414bcdfb04ad3d016bad6055d69f148b7772b7b64c51c8edb95ab1a0396d2070 bytes=9723 -->
## FILE: nisystemlink/clients/test_plan/_test_plan_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/_test_plan_client.py`
- sha256: `414bcdfb04ad3d016bad6055d69f148b7772b7b64c51c8edb95ab1a0396d2070`
- bytes: 9723

````python
import warnings
from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import get, post
from nisystemlink.clients.test_plan import models
from uplink import Field, retry

from ..core.helpers._partial_success import unwrap_single_item_partial_success


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class TestPlanClient(BaseClient):
    __test__ = False

    def __init__(self, configuration: HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the WorkOrder Service.
        """
        warnings.warn(
            "TestPlanClient is deprecated and will be removed in the future. "
            "Use WorkItemClient instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/niworkorder/v1/")

    @get("testplans/{test_plan_id}")
    def get_test_plan(self, test_plan_id: str) -> models.TestPlan:
        """Retrieve a test plan by its ID.

        Args:
            test_plan_id: The ID of the test plan to retrieve.

        Returns:
            The TestPlan object corresponding to the given ID.
        """
        ...

    @post("testplans", args=[Field("testPlans")])
    def create_test_plans(
        self, test_plans: List[models.CreateTestPlanRequest]
    ) -> models.CreateTestPlansPartialSuccessResponse:
        """Create a new test plan.

        Args:
            test_plan: The test plans to create.

        Returns:
            The created test plan object.
        """
        ...

    def create_test_plan(
        self, test_plan: models.CreateTestPlanRequest
    ) -> models.TestPlan:
        """Create a single test plan.

        Args:
            test_plan: The test plan to create.

        Returns:
            The created test plan.

        Raises:
            ApiException: if the test plan could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_test_plans([test_plan])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.created_test_plans,
            failed=response.failed_test_plans,
            error=response.error,
            failure_message="Failed to create test plan.",
            empty_message="Server returned no created test plans.",
        )

    @post("delete-testplans", args=[Field("ids")])
    def delete_test_plans(self, ids: List[str]) -> None:
        """Delete test plans by IDs.

        Args:
            test_plan_ids: A list of test plan IDs to delete.

        Returns:
            None
        """
        ...

    @post("query-testplans")
    def query_test_plans(
        self, query_request: models.QueryTestPlansRequest
    ) -> models.PagedTestPlans:
        """Query test plans.

        Args:
            query: The query to execute.

        Returns:
            A PagedTestPlans object containing test plans that match the query.
        """
        ...

    @post("schedule-testplans")
    def schedule_test_plans(
        self, schedule_request: models.ScheduleTestPlansRequest
    ) -> models.ScheduleTestPlansResponse:
        """Schedule a test plan.

        Args:
            schedule: The schedule to apply to the test plan.

        Returns:
            A ScheduleTestPlansResponse object containing the scheduled test plan.
        """
        ...

    def schedule_test_plan(
        self,
        test_plan: models.ScheduleTestPlanRequest,
        replace: bool | None = None,
    ) -> models.TestPlan:
        """Schedule a single test plan.

        Args:
            test_plan: The test plan schedule request.
            replace: Whether to replace the existing scheduled test plan.

        Returns:
            The scheduled test plan.

        Raises:
            ApiException: if the test plan could not be scheduled or the service returns an
                unexpected partial-success payload.
        """
        response = self.schedule_test_plans(
            models.ScheduleTestPlansRequest(test_plans=[test_plan], replace=replace)
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.scheduled_test_plans,
            failed=response.failed_test_plans,
            error=response.error,
            failure_message="Failed to schedule test plan.",
            empty_message="Server returned no scheduled test plans.",
        )

    @post("update-testplans")
    def update_test_plans(
        self, update_request: models.UpdateTestPlansRequest
    ) -> models.UpdateTestPlansResponse:
        """Update a test plan.

        Args:
            test_plan: The test plan to update.

        Returns:
            The updated test plan object.
        """
        ...

    def update_test_plan(
        self, test_plan: models.UpdateTestPlanRequest, replace: bool | None = None
    ) -> models.TestPlan:
        """Update a single test plan.

        Args:
            test_plan: The test plan to update.
            replace: Whether to replace the existing test plan instead of merging updates.

        Returns:
            The updated test plan.

        Raises:
            ApiException: if the test plan could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_test_plans(
            models.UpdateTestPlansRequest(test_plans=[test_plan], replace=replace)
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.updated_test_plans,
            failed=response.failed_test_plans,
            error=response.error,
            failure_message="Failed to update test plan.",
            empty_message="Server returned no updated test plans.",
        )

    @post("testplan-templates", args=[Field("testPlanTemplates")])
    def create_test_plan_templates(
        self, test_plan_templates: List[models.CreateTestPlanTemplateRequest]
    ) -> models.CreateTestPlanTemplatePartialSuccessResponse:
        """Creates one or more test plan template and return errors for failed creations.

        Args:
            test_plan_templates: A list of test plan templates to attempt to create.

        Returns: A list of created test plan templates, test plan templates that failed to create, and errors for
                 failures.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
                arguments.
        """
        ...

    def create_test_plan_template(
        self, test_plan_template: models.CreateTestPlanTemplateRequest
    ) -> models.TestPlanTemplate:
        """Creates a single test plan template.

        Args:
            test_plan_template: The test plan template to create.

        Returns:
            The created test plan template.

        Raises:
            ApiException: if the test plan template could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_test_plan_templates([test_plan_template])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.created_test_plan_templates,
            failed=response.failed_test_plan_templates,
            error=response.error,
            failure_message="Failed to create test plan template.",
            empty_message="Server returned no created test plan templates.",
        )

    @post("query-testplan-templates")
    def query_test_plan_templates(
        self, query_test_plan_templates: models.QueryTestPlanTemplatesRequest
    ) -> models.PagedTestPlanTemplates:
        """Queries one or more test plan templates and return errors for failed queries.

        Returns: A list of test plan templates, based on the query and errors for the wrong query.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
                arguments.
        """
        ...

    @post("delete-testplan-templates", args=[Field("ids")])
    def delete_test_plan_templates(
        self, ids: List[str]
    ) -> models.DeleteTestPlanTemplatesPartialSuccessResponse | None:
        """Deletes one or more test plan templates and return errors for failed deletion.

        Returns:
            A partial success if any test plan templates failed to delete, or None if all
            test plan templates were deleted successfully.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
            arguments.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/__init__.py sha256=ac8117f5bad876188e513427356fb64587eb9cfe43814c3d9ce4ae64a0cbd8ad bytes=1762 -->
## FILE: nisystemlink/clients/test_plan/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/__init__.py`
- sha256: `ac8117f5bad876188e513427356fb64587eb9cfe43814c3d9ce4ae64a0cbd8ad`
- bytes: 1762

````python
from ._create_test_plan_request import CreateTestPlanRequest
from ._create_test_plans_partial_success_response import (
    CreateTestPlansPartialSuccessResponse,
)
from ._dashboard import Dashboard, DashboardUrl
from ._update_test_plan_request import UpdateTestPlanRequest
from ._update_test_plans_request import UpdateTestPlansRequest
from ._update_test_plans_response import UpdateTestPlansResponse
from ._query_test_plans_request import QueryTestPlansRequest, TestPlanField
from ._paged_test_plans import PagedTestPlans
from ._execution_event import (
    ExecutionEvent,
    NotebookExecutionEvent,
    JobExecutionEvent,
    ManualExecutionEvent,
)
from ._order_by import OrderBy
from ._test_plan import TestPlan
from ._state import State
from ._execution_definition import (
    ExecutionDefinition,
    ManualExecution,
    JobExecution,
    NoneExecution,
    NotebookExecution,
    Job,
)
from ._schedule_test_plans_request import ScheduleTestPlansRequest
from ._schedule_test_plan_request import ScheduleTestPlanRequest
from ._schedule_test_plans_response import ScheduleTestPlansResponse

from ._test_plan_templates import TestPlanTemplateBase, TestPlanTemplate
from ._create_test_plan_templates_partial_success_response import (
    CreateTestPlanTemplatePartialSuccessResponse,
)
from ._delete_test_plan_templates_partial_success_response import (
    DeleteTestPlanTemplatesPartialSuccessResponse,
)
from ._query_test_plan_templates_request import (
    QueryTestPlanTemplatesRequest,
    TestPlanTemplateField,
    TestPlanTemplateOrderBy,
)
from ._paged_test_plan_templates import PagedTestPlanTemplates
from ._create_test_plan_template_request import CreateTestPlanTemplateRequest

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_request.py sha256=961e3df8b013eb4380a5ab80865c9634e8105137782de7c635fe88c303034002 bytes=1979 -->
## FILE: nisystemlink/clients/test_plan/models/_create_test_plan_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_create_test_plan_request.py`
- sha256: `961e3df8b013eb4380a5ab80865c9634e8105137782de7c635fe88c303034002`
- bytes: 1979

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import Dashboard
from ._execution_definition import ExecutionDefinition


class CreateTestPlanRequest(JsonModel):
    """Represents the request body content for creating a test plan."""

    name: str | None = None
    """The name of the test plan."""

    state: str | None = None
    """The state of the test plan."""

    template_id: str | None = None
    """The ID of the template to use for the test plan."""

    description: str | None = None
    """A description of the test plan."""

    assigned_to: str | None = None
    """The user or group assigned to the test plan."""

    part_number: str | None = None
    """The part number associated with the test plan."""

    dut_id: str | None = None
    """The Device Under Test (DUT) ID."""

    dut_serial_number: str | None = None
    """The Device Under Test (DUT) serial number."""

    test_program: str | None = None
    """The test program associated with the test plan."""

    work_order_id: str | None = None
    """The work order ID associated with the test plan."""

    estimated_duration_in_seconds: int | None = None
    """The estimated duration of the test plan in seconds."""

    system_filter: str | None = None
    """The system filter to apply."""

    dut_filter: str | None = None
    """The DUT filter to apply."""

    execution_actions: List[ExecutionDefinition] | None = None
    """List of execution actions for the test plan."""

    file_ids_from_template: List[str] | None = None
    """List of file IDs from the template."""

    workspace: str | None = None
    """The workspace associated with the test plan."""

    properties: Dict[str, str] | None = None
    """Additional properties for the test plan."""

    dashboard: Dashboard | None = None
    """The dashboard associated with the test plan."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_template_request.py sha256=d712556b522495714d04591f3ffc4bdecf8e60c2be46d917cdfac84836cb1958 bytes=326 -->
## FILE: nisystemlink/clients/test_plan/models/_create_test_plan_template_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_create_test_plan_template_request.py`
- sha256: `d712556b522495714d04591f3ffc4bdecf8e60c2be46d917cdfac84836cb1958`
- bytes: 326

````python
from ._test_plan_templates import TestPlanTemplateBase


class CreateTestPlanTemplateRequest(TestPlanTemplateBase):
    """Contains information about a test plan template request."""

    name: str
    """Name of the test plan template."""

    template_group: str
    """The template group defined by the user."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_templates_partial_success_response.py sha256=c28e1241756e1bc6ca569870347342fbf642af29f419001d142f36f8c3fed229 bytes=941 -->
## FILE: nisystemlink/clients/test_plan/models/_create_test_plan_templates_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_create_test_plan_templates_partial_success_response.py`
- sha256: `c28e1241756e1bc6ca569870347342fbf642af29f419001d142f36f8c3fed229`
- bytes: 941

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._create_test_plan_template_request import CreateTestPlanTemplateRequest
from ._test_plan_templates import TestPlanTemplate


class CreateTestPlanTemplatePartialSuccessResponse(JsonModel):

    created_test_plan_templates: List[TestPlanTemplate] | None = None
    """The list of test plan templates that were successfully created."""

    failed_test_plan_templates: List[CreateTestPlanTemplateRequest] | None = None
    """The list of test plan templates that were not created.

    If this is `None`, then all test plan templates were successfully created.
    """

    error: ApiError | None = None
    """Error messages for test plan templates that were not created.

    If this is `None`, then all test plan templates were successfully created.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plans_partial_success_response.py sha256=46e7619a734c3e4699535e71156dcf03a4e1581f91686f3da1ab2080f996f440 bytes=842 -->
## FILE: nisystemlink/clients/test_plan/models/_create_test_plans_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_create_test_plans_partial_success_response.py`
- sha256: `46e7619a734c3e4699535e71156dcf03a4e1581f91686f3da1ab2080f996f440`
- bytes: 842

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._create_test_plan_request import CreateTestPlanRequest
from ._test_plan import TestPlan


class CreateTestPlansPartialSuccessResponse(JsonModel):
    """Represents the response from creating test plans, including successfully created,
    failed test plans, and any associated errors.
    """

    created_test_plans: List[TestPlan] | None = None
    """List of test plans that were successfully created."""

    failed_test_plans: List[CreateTestPlanRequest] | None = None
    """List of test plans that failed to be created, with their request body content."""

    error: ApiError | None = None
    """The error that occurred when creating the test plans."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_dashboard.py sha256=852dfd16810d77b07df3009f7747ed6bfafa477d905a6849ad9a3d7a430b942d bytes=549 -->
## FILE: nisystemlink/clients/test_plan/models/_dashboard.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_dashboard.py`
- sha256: `852dfd16810d77b07df3009f7747ed6bfafa477d905a6849ad9a3d7a430b942d`
- bytes: 549

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel


class Dashboard(JsonModel):
    """Represents a dashboard reference."""

    id: str | None = None
    """ID of the dashboard"""

    variables: Dict[str, str] | None = None
    """Variables for the dashboard"""


class DashboardUrl(Dashboard):
    """Definition and URL of the dashboard reference associated with this test plan."""

    url: str | None = None
    """URL of the dashboard reference associated with this test plan."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_delete_test_plan_templates_partial_success_response.py sha256=84cd5b45c0040af58276800bc927e9afaee245199b1fc717cb0505ed8eda1870 bytes=722 -->
## FILE: nisystemlink/clients/test_plan/models/_delete_test_plan_templates_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_delete_test_plan_templates_partial_success_response.py`
- sha256: `84cd5b45c0040af58276800bc927e9afaee245199b1fc717cb0505ed8eda1870`
- bytes: 722

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteTestPlanTemplatesPartialSuccessResponse(JsonModel):
    """The result of deleting multiple test plan templates
    when one or more test plan templates could not be deleted.
    """

    deleted_test_plan_template_ids: List[str]
    """The IDs of the test plan template that could not be deleted."""

    failed_test_plan_template_ids: List[str] | None = None
    """The IDs of the test plan template that could not be deleted."""

    error: ApiError | None = None
    """The error that occurred when deleting the test plan template."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_execution_definition.py sha256=ce89844e9dc9ba95e69718aee66effb6e11695776a88afa1ace95bc748115471 bytes=2188 -->
## FILE: nisystemlink/clients/test_plan/models/_execution_definition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_execution_definition.py`
- sha256: `ce89844e9dc9ba95e69718aee66effb6e11695776a88afa1ace95bc748115471`
- bytes: 2188

````python
from typing import Annotated, Any, Dict, List, Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field


class Job(JsonModel):
    """Represents a job to be executed, including its functions, arguments, and metadata."""

    functions: List[str]
    """List of function names to execute."""

    arguments: List[List[Any]]
    """List of argument lists for each function."""

    metadata: Dict[str, Any]
    """Additional metadata for the job."""


class NotebookExecution(JsonModel):
    """Defines the execution of a notebook."""

    action: str
    """User defined action to perform in workflow (user defined)."""

    type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")
    """Type of execution, default is 'NOTEBOOK'."""

    notebookId: str
    """ID of the notebook to execute."""

    parameters: Dict[str, str] | None = None
    """	Dictionary of parameters that will be passed to the notebook when the execution is run."""


class ManualExecution(JsonModel):
    """Represents a manual execution definition."""

    action: str
    """User defined action to perform in workflow (user defined)."""

    type: Literal["MANUAL"] = Field(default="MANUAL")
    """Type of execution, default is 'MANUAL'."""


class JobExecution(JsonModel):
    """Defines the execution of one or more jobs."""

    action: str
    """User defined action to perform in workflow (user defined)."""

    type: Literal["JOB"] = Field(default="JOB")
    """Type of execution, default is 'JOB'."""

    jobs: List[Job] | None = None
    """List of jobs to execute."""

    systemId: str | None = None
    """Optional system ID where jobs will run."""


class NoneExecution(JsonModel):
    """Represents a definition where no execution is specified."""

    action: str
    """User defined action to perform in workflow (user defined)."""

    type: Literal["NONE"] = Field(default="NONE")
    """Type of execution, default is 'NONE'."""


ExecutionDefinition = Annotated[
    NotebookExecution | ManualExecution | JobExecution | NoneExecution,
    Field(discriminator="type"),
]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_execution_event.py sha256=4467aaea88150f8b6ff30730716572e8263c01c25e019eb80920fe6329c82f74 bytes=1720 -->
## FILE: nisystemlink/clients/test_plan/models/_execution_event.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_execution_event.py`
- sha256: `4467aaea88150f8b6ff30730716572e8263c01c25e019eb80920fe6329c82f74`
- bytes: 1720

````python
from datetime import datetime
from typing import Annotated, List, Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field


class ExecutionEventBase(JsonModel):
    """Base class for execution events, containing common attributes such as action."""

    action: str | None = None
    """The user-defined action that initiated the event."""

    triggered_at: datetime | None = None
    """The time the event was triggered."""

    triggered_by: str | None = None
    """The user who triggered the event."""


class NotebookExecutionEvent(ExecutionEventBase):
    """Represents an execution event that was triggered by a notebook execution."""

    type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")
    """Represents an execution event triggered by a notebook."""

    execution_id: str | None = None
    """Includes the type identifier and the execution ID."""


class JobExecutionEvent(ExecutionEventBase):
    """A concrete execution event that represents an event triggered by a job."""

    type: Literal["JOB"] = Field(default="JOB")
    """Represents an execution event triggered by a job."""

    job_ids: List[str] | None = None
    """Includes the type identifier and a list of job IDs."""


class ManualExecutionEvent(ExecutionEventBase):
    """A concrete execution event that represents an event triggered manually."""

    type: Literal["MANUAL"] = Field(default="MANUAL")
    """Represents an execution event triggered manually. Includes only the type identifier."""


ExecutionEvent = Annotated[
    NotebookExecutionEvent | ManualExecutionEvent | JobExecutionEvent,
    Field(discriminator="type"),
]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_order_by.py sha256=2f424dc42a8b2fe79a6de478409593151561758f4f8b0f9c354ad8db403c9358 bytes=134 -->
## FILE: nisystemlink/clients/test_plan/models/_order_by.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_order_by.py`
- sha256: `2f424dc42a8b2fe79a6de478409593151561758f4f8b0f9c354ad8db403c9358`
- bytes: 134

````python
from enum import Enum


class OrderBy(Enum):
    """The state of the test plan."""

    ID = "ID"
    UPDATE_AT = "UPDATE_AT"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_paged_test_plan_templates.py sha256=23e792ddc46eddda14de545bed70c385e1f39d45d249e8bfa40a5318b8d73ce9 bytes=536 -->
## FILE: nisystemlink/clients/test_plan/models/_paged_test_plan_templates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_paged_test_plan_templates.py`
- sha256: `23e792ddc46eddda14de545bed70c385e1f39d45d249e8bfa40a5318b8d73ce9`
- bytes: 536

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._test_plan_templates import TestPlanTemplate


class PagedTestPlanTemplates(WithPaging):
    """The response containing the list of products, total count of products and the continuation
    token if applicable.
    """

    test_plan_templates: List[TestPlanTemplate]
    """A list of all the products in this page."""

    total_count: int | None = None
    """The total number of products that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_paged_test_plans.py sha256=d531d906033f80520eb319b665eb53967d0612c202ac83591038c90464de27a0 bytes=493 -->
## FILE: nisystemlink/clients/test_plan/models/_paged_test_plans.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_paged_test_plans.py`
- sha256: `d531d906033f80520eb319b665eb53967d0612c202ac83591038c90464de27a0`
- bytes: 493

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._test_plan import TestPlan


class PagedTestPlans(WithPaging):
    """The response containing the list of products, total count of products and the continuation
    token if applicable.
    """

    test_plans: List[TestPlan]
    """A list of all the products in this page."""

    total_count: int | None = None
    """The total number of products that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_query_test_plan_templates_request.py sha256=0bba659460b5559a9dc1c03ca8ed0368008064e3780733c38a0065f39a9e88b4 bytes=4495 -->
## FILE: nisystemlink/clients/test_plan/models/_query_test_plan_templates_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_query_test_plan_templates_request.py`
- sha256: `0bba659460b5559a9dc1c03ca8ed0368008064e3780733c38a0065f39a9e88b4`
- bytes: 4495

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging


class TestPlanTemplateOrderBy(str, Enum):
    """An enumeration by which test plan templates can be ordered/sorted."""

    ID = "ID"
    NAME = "NAME"
    TEMPLATE_GROUP = "TEMPLATE_GROUP"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"


class TestPlanTemplateField(str, Enum):
    """Model for an object describing an test plan template with all of its properties."""

    __test__ = False

    ID = "ID"
    NAME = "NAME"
    TEMPLATE_GROUP = "TEMPLATE_GROUP"
    PRODUCT_FAMILIES = "PRODUCT_FAMILIES"
    PART_NUMBERS = "PART_NUMBERS"
    SUMMARY = "SUMMARY"
    DESCRIPTION = "DESCRIPTION"
    TEST_PROGRAM = "TEST_PROGRAM"
    ESTIMATED_DURATION_IN_SECONDS = "ESTIMATED_DURATION_IN_SECONDS"
    SYSTEM_FILTER = "SYSTEM_FILTER"
    DUT_FILTER = "DUT_FILTER"
    EXECUTION_ACTIONS = "EXECUTION_ACTIONS"
    FILE_IDS = "FILE_IDS"
    WORKSPACE = "WORKSPACE"
    PROPERTIES = "PROPERTIES"
    DASHBOARD = "DASHBOARD"
    CREATED_BY = "CREATED_BY"
    UPDATED_BY = "UPDATED_BY"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"


class QueryTestPlanTemplatesRequest(WithPaging):
    """Request information for the query test plan templates API."""

    filter: str | None = None
    """The test plan template query filter in dynamic LINQ format.

    `id`: String representing the ID of a test plan template. Field supports only equals '=' and not
    equal '!=' operators for filtering.
    `productFamilies`: Array of strings representing the product families to which the test plan
    template belongs.
    `partNumbers`: Array of strings representing the part numbers of the products to which the test
    plan template belongs.
    `fileIds`: The array of file IDs associated with the test plan template.
    `name`: String representing the name of a test plan template.
    `summary`: String representing the summary of a test plan template.
    `description`: String representing description of the test plan created from this template.
    `templateGroup`: String representing the template group defined by the user.
    `testProgram`: String representing the test program name of the test plan created from this
    template.
    `systemFilter`: String representing the LINQ filter used to filter the potential list of systems
    `dutFilter`: String representing the LINQ filter used to filter the potential list of DUTs
    capable of executing test plans created from this template.
    `workspace`: String representing the workspace where the test plan template belongs.
    `createdBy`: String representing the user who created the test plan template.
    `updatedBy`: String representing the user who updated the test plan template.
    `createdAt`: ISO-8601 formatted timestamp indicating when the test plan template was created.
    `updatedAt`: ISO-8601 formatted timestamp indicating when the test plan template was most
    recently updated.
    `properties`: Collection of key-value pairs related to a test plan created from this template.
    Example: properties.Any(key == "Location" & value == "Austin")

    See [Dynamic Linq](https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language)
    documentation for more details.

    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable."""

    take: int | None = None
    """The maximum number of test plan templates to return."""

    order_by: TestPlanTemplateOrderBy | None = None
    """Field by which test plan templates can be ordered/sorted."""

    substitutions: List[str] | None = None
    """Makes substitutions in the query filter expression
    using non-negative integers. These integers
    use the @ symbol as a prefix. The filter
    expression replaces each substitution
    with the element at the corresponding
    index in this list. The index is zero-based."""

    descending: bool | None = None
    """Whether to return the test plan templates in the descending order. By default, test plan
    templates are sorted in the ascending order."""

    projection: List[TestPlanTemplateField] | None = None
    """
    Gets or sets the projection to be used when retrieving the assets. If not specified,
    all properties will be returned.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_query_test_plans_request.py sha256=794efba0031b44a3ab9512621d1f51d2093aeecc5ad83423dafca613d06f7682 bytes=2346 -->
## FILE: nisystemlink/clients/test_plan/models/_query_test_plans_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_query_test_plans_request.py`
- sha256: `794efba0031b44a3ab9512621d1f51d2093aeecc5ad83423dafca613d06f7682`
- bytes: 2346

````python
import enum
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._order_by import OrderBy


class TestPlanField(enum.Enum):
    """Model for an object describing an test plan with all of its properties."""

    __test__ = False

    ID = "ID"
    TEMPLATE_ID = "TEMPLATE_ID"
    NAME = "NAME"
    STATE = "STATE"
    SUBSTATE = "SUBSTATE"
    DESCRIPTION = "DESCRIPTION"
    ASSIGNED_TO = "ASSIGNED_TO"
    WORK_ORDER_ID = "WORK_ORDER_ID"
    WORK_ORDER_NAME = "WORK_ORDER_NAME"
    PART_NUMBER = "PART_NUMBER"
    DUT_ID = "DUT_ID"
    DUT_SERIAL_NUMBER = "DUT_SERIAL_NUMBER"
    TEST_PROGRAM = "TEST_PROGRAM"
    WORKSPACE = "WORKSPACE"
    CREATED_BY = "CREATED_BY"
    UPDATED_BY = "UPDATED_BY"
    SYSTEM_ID = "SYSTEM_ID"
    FIXTURE_IDS = "FIXTURE_IDS"
    PLANNED_START_DATE_TIME = "PLANNED_START_DATE_TIME"
    ESTIMATED_END_DATE_TIME = "ESTIMATED_END_DATE_TIME"
    ESTIMATED_DURATION_IN_SECONDS = "ESTIMATED_DURATION_IN_SECONDS"
    SYSTEM_FILTER = "SYSTEM_FILTER"
    DUT_FILTER = "DUT_FILTER"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"
    PROPERTIES = "PROPERTIES"
    FILE_IDS_FROM_TEMPLATE = "FILE_IDS_FROM_TEMPLATE"
    DASHBOARD = "DASHBOARD"
    EXECUTION_ACTIONS = "EXECUTION_ACTIONS"
    EXECUTION_HISTORY = "EXECUTION_HISTORY"
    DASHBOARD_URL = "DASHBOARD_URL"
    WORKFLOW = "WORKFLOW"


class QueryTestPlansRequest(WithPaging):
    """Represents the request body for querying test plans.
    Allows filtering, sorting, and pagination of test plan results.
    """

    filter: str | None = None
    """A string expression to filter the test plans returned by the query."""

    take: int | None = None
    """The maximum number of test plans to return in the response."""

    order_by: OrderBy | None = None
    """The field name to use for sorting the test plans."""

    descending: bool | None = None
    """Whether to sort the test plans in descending order."""

    return_count: bool | None = None
    """Whether to include the total count of matching test plans in the response."""

    projection: List[TestPlanField] | None = None
    """
    Gets or sets the projection to be used when retrieving the assets. If not specified,
    all properties will be returned.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plan_request.py sha256=4879f07397d05b99032e35e005b61ceff5e878e3622528cffc7642bea242efff bytes=1216 -->
## FILE: nisystemlink/clients/test_plan/models/_schedule_test_plan_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_schedule_test_plan_request.py`
- sha256: `4879f07397d05b99032e35e005b61ceff5e878e3622528cffc7642bea242efff`
- bytes: 1216

````python
from datetime import datetime
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class ScheduleTestPlanRequest(JsonModel):
    """Represents the request body content for scheduling a test plan."""

    id: str
    """Unique identifier for the test plan to be scheduled."""

    assigned_to: str | None = None
    """(Optional) User or entity to whom the test plan is assigned."""

    dut_id: str | None = None
    """(Optional) Identifier for the Device Under Test (DUT)."""

    system_id: str | None = None
    """(Optional) Identifier for the system where the test plan will run."""

    planned_start_date_time: datetime | None = None
    """(Optional) Planned start date and time for the test plan execution (ISO 8601 format)."""

    estimated_end_date_time: datetime | None = None
    """(Optional) Estimated end date and time for the test plan execution (ISO 8601 format)."""

    estimated_duration_in_seconds: int | None = None
    """(Optional) Estimated duration of the test plan execution in seconds."""

    fixture_ids: List[str] | None = None
    """(Optional) List of fixture identifiers associated with the test plan."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plans_request.py sha256=d76cc363f5142f87a8ea5e60590d8d4f0fd70a5fbf9c660424bf643269555fee bytes=499 -->
## FILE: nisystemlink/clients/test_plan/models/_schedule_test_plans_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_schedule_test_plans_request.py`
- sha256: `d76cc363f5142f87a8ea5e60590d8d4f0fd70a5fbf9c660424bf643269555fee`
- bytes: 499

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._schedule_test_plan_request import ScheduleTestPlanRequest


class ScheduleTestPlansRequest(JsonModel):
    """Represents the request body for scheduling multiple test plans."""

    test_plans: List[ScheduleTestPlanRequest]
    """List of test plan scheduling content objects."""

    replace: bool | None = None
    """(Optional) If true, replaces existing scheduled test plans."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plans_response.py sha256=f94c6e2bcbafe4c0ca6f0d14f53e5cec29e2655d5a1d2d5fc504f248bc23e2f2 bytes=774 -->
## FILE: nisystemlink/clients/test_plan/models/_schedule_test_plans_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_schedule_test_plans_response.py`
- sha256: `f94c6e2bcbafe4c0ca6f0d14f53e5cec29e2655d5a1d2d5fc504f248bc23e2f2`
- bytes: 774

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._schedule_test_plan_request import ScheduleTestPlanRequest
from ._test_plan import TestPlan


class ScheduleTestPlansResponse(JsonModel):
    """Represents the response returned after attempting to schedule one or more test plans."""

    scheduled_test_plans: List[TestPlan] | None = None
    """(Optional) List of successfully scheduled test plans."""

    failed_test_plans: List[ScheduleTestPlanRequest] | None = None
    """(Optional) List of test plan requests that failed to schedule."""

    error: ApiError | None = None
    """The error that occurred when scheduling the test plans."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_state.py sha256=f8631473ee0eb98600c020665175b2d6e3428af2e01b7842249fb99198762019 bytes=312 -->
## FILE: nisystemlink/clients/test_plan/models/_state.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_state.py`
- sha256: `f8631473ee0eb98600c020665175b2d6e3428af2e01b7842249fb99198762019`
- bytes: 312

````python
from enum import Enum


class State(Enum):
    """The state of the test plan."""

    NEW = "NEW"
    DEFINED = "DEFINED"
    REVIEWED = "REVIEWED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    CLOSED = "CLOSED"
    CANCELED = "CANCELED"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_test_plan.py sha256=bdcf1b48c8775b0e847059c20a84fa57a27f8c17208738fb70208a3e585b8ff5 bytes=3514 -->
## FILE: nisystemlink/clients/test_plan/models/_test_plan.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_test_plan.py`
- sha256: `bdcf1b48c8775b0e847059c20a84fa57a27f8c17208738fb70208a3e585b8ff5`
- bytes: 3514

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import DashboardUrl
from ._execution_definition import ExecutionDefinition
from ._execution_event import ExecutionEvent
from ._state import State


class TestPlan(JsonModel):
    """Contains information about a test plan."""

    __test__ = False

    id: str
    """The unique identifier of the test plan."""

    template_id: str | None = None
    """The identifier of the template used to create the test plan."""

    name: str | None = None
    """The name of the test plan."""

    state: State | None = None
    """The current state of the test plan."""

    substate: str | None = None
    """The substate of the test plan, if any."""

    description: str | None = None
    """The description of the test plan."""

    assigned_to: str | None = None
    """The user or group assigned to the test plan."""

    work_order_id: str | None = None
    """The identifier of the associated work order."""

    work_order_name: str | None = None
    """The name of the associated work order."""

    part_number: str | None = None
    """The part number associated with the test plan."""

    dut_id: str | None = None
    """The identifier of the device under test (DUT)."""

    dut_serial_number: str | None = None
    """The serial number of the device under test (DUT)."""

    test_program: str | None = None
    """The test program associated with the test plan."""

    workspace: str | None = None
    """The workspace to which the test plan belongs."""

    created_by: str | None = None
    """The user who created the test plan."""

    updated_by: str | None = None
    """The user who last updated the test plan."""

    system_id: str | None = None
    """The identifier of the system used for the test plan."""

    fixture_ids: List[str] | None = None
    """The list of fixture identifiers associated with the test plan."""

    planned_start_date_time: datetime | None = None
    """The planned start date and time for the test plan."""

    estimated_end_date_time: datetime | None = None
    """The estimated end date and time for the test plan."""

    estimated_duration_in_seconds: float | None = None
    """The estimated duration of the test plan in seconds."""

    system_filter: str | None = None
    """The filter used to select systems for the test plan."""

    dut_filter: str | None = None
    """The filter used to select DUTs for the test plan."""

    created_at: datetime | None = None
    """The date and time when the test plan was created."""

    updated_at: datetime | None = None
    """The date and time when the test plan was last updated."""

    properties: Dict[str, str] | None = None
    """Additional properties associated with the test plan."""

    file_ids_from_template: List[str] | None = None
    """The list of file identifiers inherited from the template."""

    dashboard: DashboardUrl | None = None
    """The dashboard data related to the test plan."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the test plan."""

    execution_history: List[ExecutionEvent] | None = None
    """The execution history of the test plan."""

    dashboard_url: Dict[str, str] | None = None
    """The URLs for dashboards related to the test plan."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_test_plan_templates.py sha256=e66241c81ad6393a09147025e671862ec6ffaafbc8b1236972c1869d274d98ea bytes=3096 -->
## FILE: nisystemlink/clients/test_plan/models/_test_plan_templates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_test_plan_templates.py`
- sha256: `e66241c81ad6393a09147025e671862ec6ffaafbc8b1236972c1869d274d98ea`
- bytes: 3096

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import Dashboard
from ._execution_definition import ExecutionDefinition


class TestPlanTemplateBase(JsonModel):
    """Contains information about a test plan template."""

    name: str | None = None
    """Name of the test plan template."""

    template_group: str | None = None
    """The template group defined by the user."""

    product_families: List[str] | None = None
    """Array of product families to which the test plan template belongs."""

    part_numbers: List[str] | None = None
    """Array of part numbers of the products to which the test plan template belongs."""

    summary: str | None = None
    """Summary of the test plan template."""

    description: str | None = None
    """Description of the test plan created from this template."""

    test_program: str | None = None
    """Test program name of the test plan created from this template."""

    estimated_duration_in_seconds: int | None = None
    """The estimated time in seconds for executing the test plan created from this template."""

    system_filter: str | None = None
    """The LINQ filter string is used to filter the potential list of
    systems capable of executing test plans created from this template.
    """

    dut_filter: str | None = None
    """The LINQ filter string is used to filter the potential list of
    DUTs capable of executing test plans created from this template.
    """

    execution_actions: List[ExecutionDefinition] | None = None
    """Defines the executions that will be used for test plan actions
    created from this template.
    """

    file_ids: List[str] | None = None
    """Array of file IDs associated with the test plan template."""

    workspace: str | None = None
    """ID of the workspace where the test plan template belongs.
    Default workspace will be taken if the value is not given.
    """

    properties: Dict[str, str] | None = None
    """Properties of the test plan created from this template as key-value pairs."""

    dashboard: Dashboard | None = None
    """Defines a dashboard reference for a test plan."""


class TestPlanTemplate(TestPlanTemplateBase):
    """Contains response information for test plan template."""

    __test__ = False

    id: str | None = None
    """The globally unique id of the test plan template."""

    name: str | None = None
    """Name of the test plan template."""

    created_by: str | None = None
    """ID of the user who created the test plan template."""

    updated_by: str | None = None
    """ID of the user who most recently updated the test plan template."""

    created_at: datetime | None = None
    """ISO-8601 formatted timestamp indicating when the
    test plan template was created."""

    updated_at: datetime | None = None
    """ISO-8601 formatted timestamp indicating when the
    test plan template was most recently updated."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plan_request.py sha256=3ec99af5d13388fbb0618d6518af46b5392d3332bf97e5a1ecb86221f489a5df bytes=1353 -->
## FILE: nisystemlink/clients/test_plan/models/_update_test_plan_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_update_test_plan_request.py`
- sha256: `3ec99af5d13388fbb0618d6518af46b5392d3332bf97e5a1ecb86221f489a5df`
- bytes: 1353

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class UpdateTestPlanRequest(JsonModel):
    """Represents the content for updating a single test plan."""

    id: str
    """The unique identifier of the test plan to update."""

    name: str | None = None
    """The new name for the test plan."""

    state: str | None = None
    """The new state of the test plan."""

    description: str | None = None
    """The new description for the test plan."""

    dut_id: str | None = None
    """The device under test (DUT) identifier."""

    part_number: str | None = None
    """The part number associated with the test plan."""

    assigned_to: str | None = None
    """The user or group assigned to the test plan."""

    test_program: str | None = None
    """The test program associated with the test plan."""

    properties: Dict[str, str] | None = None
    """Additional properties for the test plan as key-value pairs."""

    workspace: str | None = None
    """The workspace to which the test plan belongs."""

    work_order_id: str | None = None
    """The work order identifier associated with the test plan."""

    file_ids_from_template: List[str] | None = None
    """List of file IDs from the template to associate with the test plan."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plans_request.py sha256=b583ccbed14f3fa246989eada0b4d6fb100c33366852786c321e8b92438a9579 bytes=474 -->
## FILE: nisystemlink/clients/test_plan/models/_update_test_plans_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_update_test_plans_request.py`
- sha256: `b583ccbed14f3fa246989eada0b4d6fb100c33366852786c321e8b92438a9579`
- bytes: 474

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._update_test_plan_request import UpdateTestPlanRequest


class UpdateTestPlansRequest(JsonModel):
    """Represents the request body for updating multiple test plans."""

    test_plans: List[UpdateTestPlanRequest]
    """A list of test plans to update."""

    replace: bool | None = None
    """Whether to replace the existing test plans or update them."""
````
