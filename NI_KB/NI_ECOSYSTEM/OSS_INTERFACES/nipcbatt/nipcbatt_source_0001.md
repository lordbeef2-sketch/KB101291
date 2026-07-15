# NI OSS SOURCE SNAPSHOT: nipcbatt

<!--NI_OSS_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_OSS_SOURCE repo=nipcbatt path=.github/CODEOWNERS sha256=a6da648bdfa450ad5effc49fa557f05c0768807bd14dfc96cdd9d215816f849b bytes=42 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nipcbatt`
- source_path: `.github/CODEOWNERS`
- sha256: `a6da648bdfa450ad5effc49fa557f05c0768807bd14dfc96cdd9d215816f849b`
- bytes: 42

````text
@SJayaraman-NI, @adityas-ni, @ankitan-ni
````

<!--NI_OSS_SOURCE repo=nipcbatt path=.github/PULL_REQUEST_TEMPLATE.md sha256=38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7 bytes=363 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nipcbatt`
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

<!--NI_OSS_SOURCE repo=nipcbatt path=.github/workflows/CI.yml sha256=3e4a0ef28195683307ddd896de2858c94a552c056a5e479c91dc1a5e71fa6279 bytes=1889 -->
## FILE: .github/workflows/CI.yml

- repository: `ni/nipcbatt`
- source_path: `.github/workflows/CI.yml`
- sha256: `3e4a0ef28195683307ddd896de2858c94a552c056a5e479c91dc1a5e71fa6279`
- bytes: 1889

````yaml
name: CI

on:
  push:
    branches:
      - main
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

env:
      PYTHON_VERSION: '3.10'
      POETRY_VERSION: 1.8.4
      ARCHITECTURE: 'x64'

jobs:
  build:
    runs-on: [windows-latest]

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          architecture: ${{ env.ARCHITECTURE }}
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Check Windows architecture
        shell: pwsh
        run:  |
          Write-Host "OS Architecture: $((Get-CimInstance Win32_OperatingSystem).OSArchitecture)" 

      - uses: Gr1N/setup-poetry@v9
        with:
          poetry-version: ${{ env.POETRY_VERSION }}
      - name: Check Poetry version
        run: poetry --version

      - name: Install the Package
        run: poetry install -vvv
      - name: Check Poetry version
        run: poetry --version

      - name: Lint the Code
        continue-on-error: true
        run: poetry run ni-python-styleguide lint

      - name: Run tests
        run: poetry run pytest --verbose --doctest-modules --junitxml=junit/test-results-${{ env.PYTHON_VERSION }}.xml
      - name: Upload pytest test results
        uses: actions/upload-artifact@v4
        with:
          name: pytest-results-${{env.PYTHON_VERSION }}
          path: junit/test-results-${{ env.PYTHON_VERSION }}.xml
        # Use always() to always run this step to publish test results when there are test failures
        if: ${{ always() }}

      - name: Build Python package
        run: poetry build

      - name: Archive production artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: |
            dist
            !dist/**/*.md
````

<!--NI_OSS_SOURCE repo=nipcbatt path=.github/workflows/PR.yml sha256=963d0bf234eb104ac1a896f9773e8eb0dbe4fd565a59de38bb57792c210d0be3 bytes=331 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/nipcbatt`
- source_path: `.github/workflows/PR.yml`
- sha256: `963d0bf234eb104ac1a896f9773e8eb0dbe4fd565a59de38bb57792c210d0be3`
- bytes: 331

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
````

<!--NI_OSS_SOURCE repo=nipcbatt path=.github/workflows/Publish-Package.yml sha256=6cf2dbbeff19761ba05dc14598e3104b4ca7bac5ab505f86b6b2705284fc268a bytes=3049 -->
## FILE: .github/workflows/Publish-Package.yml

- repository: `ni/nipcbatt`
- source_path: `.github/workflows/Publish-Package.yml`
- sha256: `6cf2dbbeff19761ba05dc14598e3104b4ca7bac5ab505f86b6b2705284fc268a`
- bytes: 3049

````yaml
name: Publish Package

on:
  release:
    types: [released]


env:
      PYTHON_VERSION: '3.10'
      POETRY_VERSION: 1.8.4
      ARCHITECTURE: 'x64'

jobs:
  publish:
    runs-on: [windows-latest]

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.release.target_commitish }} # This is the branch the release was created from. Normally main, but can be a dev branch
          persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
          fetch-depth: 0 # otherwise, you will failed to push refs to dest repo

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          architecture: ${{ env.ARCHITECTURE }}
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Check Windows architecture
        shell: pwsh
        run:  |
          Write-Host "OS Architecture: $((Get-CimInstance Win32_OperatingSystem).OSArchitecture)"   
          
      - name: Check Python architecture
        run: python -c "import platform; print('Platform architecture:', platform.architecture())"

      - uses: Gr1N/setup-poetry@v9
        with:
          poetry-version: ${{ env.POETRY_VERSION }}
      - name: Check Poetry version
        run: poetry --version

      - name: Install the Package
        run: poetry install -vvv
      - name: Check Poetry version
        run: poetry --version

      - name: Lint the Code
        continue-on-error: true
        run: poetry run ni-python-styleguide lint

      - name: Run tests
        run: poetry run pytest --verbose --doctest-modules --junitxml=junit/test-results-${{ env.PYTHON_VERSION }}.xml
      - name: Upload pytest test results
        uses: actions/upload-artifact@v4
        with:
          name: pytest-results-${{env.PYTHON_VERSION }}
          path: junit/test-results-${{ env.PYTHON_VERSION }}.xml
        # Use always() to always run this step to publish test results when there are test failures
        if: ${{ always() }}

      - name: Build Python package and publish to PyPI
        if: ${{ github.event.release.target_commitish == 'main' }}
        run: |
          poetry publish --build --username __token__ --password ${{ secrets.PYPI_TOKEN}}

# Uncomment this part to merge the release branch into main automatically
      # - name: Commit files
      #   if: ${{ github.event.release.target_commitish == 'main' }}
      #   run: |
      #     git config --local user.email "action@github.com"
      #     git config --local user.name "GitHub Action"
      #     git pull --tags -f
      #     git commit -m "Bump package version" -a

      # - name: Push changes
      #   if: ${{ github.event.release.target_commitish == 'main' }}
      #   uses: CasperWA/push-protected@v2
      #   with:
      #     token: ${{ secrets.ADMIN_PAT }}
      #     branch: ${{ github.event.release.target_commitish }}
      #     unprotect_reviews: true
````

<!--NI_OSS_SOURCE repo=nipcbatt path=.gitignore sha256=b80d925f208effbde075de81e4c6478a98e39cea2a0b5a08b1f1dea6ffb9e70a bytes=817 -->
## FILE: .gitignore

- repository: `ni/nipcbatt`
- source_path: `.gitignore`
- sha256: `b80d925f208effbde075de81e4c6478a98e39cea2a0b5a08b1f1dea6ffb9e70a`
- bytes: 817

````text
*.xml
*.thmx
*.htm
*.html
*.jpg


dist/
**/obj/**
**/bin/**
**/.vs/**


# Pyhon byte-compiled / optimized files
__pycache__/
*.py[cod]
*$py.class

# Log files
*.log

# Package files
*.jar


# Maven
target/
dist/

# JetBrains IDE
.idea/

# Unit test reports
TEST*.xml

# Generated by MacOS
.DS_Store

# Generated by Windows
Thumbs.db

# Applications
*.app
*.exe
*.war

# Large media files
*.mp4
*.tiff
*.avi
*.flv
*.mov
*.wmv


# Compiled Java class files
*.class

# Compiled Python bytecode
*.py[cod]

# Log files
*.log



# venv related elements
venvs/
venv/
.venv
site-packages
*pyvenv.cfg
*activate
*deactivate
*man

# python build related elements
*egg-info*

Release
x64
/pcbatt.python/build
*.aps
.vscode/
.vs/
tests_outputs
````

<!--NI_OSS_SOURCE repo=nipcbatt path=CONTRIBUTING.md sha256=53dca8208363ac80a59f46a7c4905c23f055e795836e9db34b6a6e06638c3c74 bytes=2990 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nipcbatt`
- source_path: `CONTRIBUTING.md`
- sha256: `53dca8208363ac80a59f46a7c4905c23f055e795836e9db34b6a6e06638c3c74`
- bytes: 2990

````markdown
# Contributing to nipcbatt 

Contributions to **nipcbatt** are welcome from all!

**nipcbatt** is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/<reponame>/).

**nipcbatt** follows a pull-request model for development.  If you wish to
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

<!-- # Getting Started -->

## 📝 Making a Code Contribution 📝

All code contributions should be in the form of [Pull Requests](https://guides.github.com/activities/forking/).

Please follow these steps to have your contribution considered by the maintainers:

1. Follow the styleguide
1. After you submit your pull request, verify that all status checks are passing

<!-- # Testing

- TODO: include testing steps here. -->

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

See [LICENSE](https://github.com/ni/nipcbatt/blob/main/LICENSE)
for details about how **nipcbatt** is licensed.
````

<!--NI_OSS_SOURCE repo=nipcbatt path=libs/readme.txt sha256=4c3498964ab0672a6f724f1bde005dc00ccf5d07a7c9f03a948e8bcb290c58d6 bytes=70 -->
## FILE: libs/readme.txt

- repository: `ni/nipcbatt`
- source_path: `libs/readme.txt`
- sha256: `4c3498964ab0672a6f724f1bde005dc00ccf5d07a7c9f03a948e8bcb290c58d6`
- bytes: 70

````text
here put external native code libraries, need to define whl descriptor
````

<!--NI_OSS_SOURCE repo=nipcbatt path=LICENSE sha256=0fca155a64809c466de6a207f549c41e985f5badc3c90e4d71694eaafe043b0e bytes=1165 -->
## FILE: LICENSE

- repository: `ni/nipcbatt`
- source_path: `LICENSE`
- sha256: `0fca155a64809c466de6a207f549c41e985f5badc3c90e4d71694eaafe043b0e`
- bytes: 1165

````text
This is the MIT license: http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2026, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=nipcbatt path=poetry.lock sha256=42d58efaf619f53567c7da0849db8a01bea95baedc79b9d1c4500b813deb63e6 bytes=128890 -->
## FILE: poetry.lock

- repository: `ni/nipcbatt`
- source_path: `poetry.lock`
- sha256: `42d58efaf619f53567c7da0849db8a01bea95baedc79b9d1c4500b813deb63e6`
- bytes: 128890

````text
# This file is automatically @generated by Poetry 2.3.4 and should not be changed by hand.

[[package]]
name = "appnope"
version = "0.1.4"
description = "Disable App Nap on macOS >= 10.9"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
markers = "sys_platform == \"darwin\""
files = [
    {file = "appnope-0.1.4-py2.py3-none-any.whl", hash = "sha256:502575ee11cd7a28c0205f379b525beefebab9d161b7c964670864014ed7213c"},
    {file = "appnope-0.1.4.tar.gz", hash = "sha256:1de3860566df9caf38f01f86f65e0e13e379af54f9e4bee1e66b48f2efffd1ee"},
]

[[package]]
name = "asttokens"
version = "2.4.1"
description = "Annotate AST trees with source code positions"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "asttokens-2.4.1-py2.py3-none-any.whl", hash = "sha256:051ed49c3dcae8913ea7cd08e46a606dba30b79993209636c4875bc1d637bc24"},
    {file = "asttokens-2.4.1.tar.gz", hash = "sha256:b03869718ba9a6eb027e134bfdf69f38a236d681c83c160d510768af11254ba0"},
]

[package.dependencies]
six = ">=1.12.0"

[package.extras]
astroid = ["astroid (>=1,<2) ; python_version < \"3\"", "astroid (>=2,<4) ; python_version >= \"3\""]
test = ["astroid (>=1,<2) ; python_version < \"3\"", "astroid (>=2,<4) ; python_version >= \"3\"", "pytest"]

[[package]]
name = "black"
version = "23.12.1"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "black-23.12.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:e0aaf6041986767a5e0ce663c7a2f0e9eaf21e6ff87a5f95cbf3675bfd4c41d2"},
    {file = "black-23.12.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c88b3711d12905b74206227109272673edce0cb29f27e1385f33b0163c414bba"},
    {file = "black-23.12.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a920b569dc6b3472513ba6ddea21f440d4b4c699494d2e972a1753cdc25df7b0"},
    {file = "black-23.12.1-cp310-cp310-win_amd64.whl", hash = "sha256:3fa4be75ef2a6b96ea8d92b1587dd8cb3a35c7e3d51f0738ced0781c3aa3a5a3"},
    {file = "black-23.12.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:8d4df77958a622f9b5a4c96edb4b8c0034f8434032ab11077ec6c56ae9f384ba"},
    {file = "black-23.12.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:602cfb1196dc692424c70b6507593a2b29aac0547c1be9a1d1365f0d964c353b"},
    {file = "black-23.12.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9c4352800f14be5b4864016882cdba10755bd50805c95f728011bcb47a4afd59"},
    {file = "black-23.12.1-cp311-cp311-win_amd64.whl", hash = "sha256:0808494f2b2df923ffc5723ed3c7b096bd76341f6213989759287611e9837d50"},
    {file = "black-23.12.1-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:25e57fd232a6d6ff3f4478a6fd0580838e47c93c83eaf1ccc92d4faf27112c4e"},
    {file = "black-23.12.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:2d9e13db441c509a3763a7a3d9a49ccc1b4e974a47be4e08ade2a228876500ec"},
    {file = "black-23.12.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6d1bd9c210f8b109b1762ec9fd36592fdd528485aadb3f5849b2740ef17e674e"},
    {file = "black-23.12.1-cp312-cp312-win_amd64.whl", hash = "sha256:ae76c22bde5cbb6bfd211ec343ded2163bba7883c7bc77f6b756a1049436fbb9"},
    {file = "black-23.12.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:1fa88a0f74e50e4487477bc0bb900c6781dbddfdfa32691e780bf854c3b4a47f"},
    {file = "black-23.12.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:a4d6a9668e45ad99d2f8ec70d5c8c04ef4f32f648ef39048d010b0689832ec6d"},
    {file = "black-23.12.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b18fb2ae6c4bb63eebe5be6bd869ba2f14fd0259bda7d18a46b764d8fb86298a"},
    {file = "black-23.12.1-cp38-cp38-win_amd64.whl", hash = "sha256:c04b6d9d20e9c13f43eee8ea87d44156b8505ca8a3c878773f68b4e4812a421e"},
    {file = "black-23.12.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:3e1b38b3135fd4c025c28c55ddfc236b05af657828a8a6abe5deec419a0b7055"},
    {file = "black-23.12.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:4f0031eaa7b921db76decd73636ef3a12c942ed367d8c3841a0739412b260a54"},
    {file = "black-23.12.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:97e56155c6b737854e60a9ab1c598ff2533d57e7506d97af5481141671abf3ea"},
    {file = "black-23.12.1-cp39-cp39-win_amd64.whl", hash = "sha256:dd15245c8b68fe2b6bd0f32c1556509d11bb33aec9b5d0866dd8e2ed3dba09c2"},
    {file = "black-23.12.1-py3-none-any.whl", hash = "sha256:78baad24af0f033958cad29731e27363183e140962595def56423e626f4bee3e"},
    {file = "black-23.12.1.tar.gz", hash = "sha256:4ce3ef14ebe8d9509188014d96af1c456a910d5b5cbf434a09fef7e024b3d0d5"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.7.4) ; sys_platform != \"win32\" or implementation_name != \"pypy\"", "aiohttp (>=3.7.4,!=3.9.0) ; sys_platform == \"win32\" and implementation_name == \"pypy\""]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "build"
version = "1.0.3"
description = "A simple, correct Python build frontend"
optional = false
python-versions = ">= 3.7"
groups = ["dev"]
files = [
    {file = "build-1.0.3-py3-none-any.whl", hash = "sha256:589bf99a67df7c9cf07ec0ac0e5e2ea5d4b37ac63301c4986d1acb126aa83f8f"},
    {file = "build-1.0.3.tar.gz", hash = "sha256:538aab1b64f9828977f84bc63ae570b060a8ed1be419e7870b8b4fc5e6ea553b"},
]

[package.dependencies]
colorama = {version = "*", markers = "os_name == \"nt\""}
packaging = ">=19.0"
pyproject_hooks = "*"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["furo (>=2023.8.17)", "sphinx (>=7.0,<8.0)", "sphinx-argparse-cli (>=1.5)", "sphinx-autodoc-typehints (>=1.10)", "sphinx-issues (>=3.0.0)"]
test = ["filelock (>=3)", "pytest (>=6.2.4)", "pytest-cov (>=2.12)", "pytest-mock (>=2)", "pytest-rerunfailures (>=9.1)", "pytest-xdist (>=1.34)", "setuptools (>=42.0.0) ; python_version < \"3.10\"", "setuptools (>=56.0.0) ; python_version == \"3.10\"", "setuptools (>=56.0.0) ; python_version == \"3.11\"", "setuptools (>=67.8.0) ; python_version >= \"3.12\"", "wheel (>=0.36.0)"]
typing = ["importlib-metadata (>=5.1)", "mypy (>=1.5.0,<1.6.0)", "tomli", "typing-extensions (>=3.7.4.3)"]
virtualenv = ["virtualenv (>=20.0.35)"]

[[package]]
name = "click"
version = "8.1.7"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "click-8.1.7-py3-none-any.whl", hash = "sha256:ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28"},
    {file = "click-8.1.7.tar.gz", hash = "sha256:ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["main", "dev"]
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "contourpy"
version = "1.3.0"
description = "Python library for calculating contours of 2D quadrilateral grids"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "contourpy-1.3.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:880ea32e5c774634f9fcd46504bf9f080a41ad855f4fef54f5380f5133d343c7"},
    {file = "contourpy-1.3.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:76c905ef940a4474a6289c71d53122a4f77766eef23c03cd57016ce19d0f7b42"},
    {file = "contourpy-1.3.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:92f8557cbb07415a4d6fa191f20fd9d2d9eb9c0b61d1b2f52a8926e43c6e9af7"},
    {file = "contourpy-1.3.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:36f965570cff02b874773c49bfe85562b47030805d7d8360748f3eca570f4cab"},
    {file = "contourpy-1.3.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:cacd81e2d4b6f89c9f8a5b69b86490152ff39afc58a95af002a398273e5ce589"},
    {file = "contourpy-1.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:69375194457ad0fad3a839b9e29aa0b0ed53bb54db1bfb6c3ae43d111c31ce41"},
    {file = "contourpy-1.3.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7a52040312b1a858b5e31ef28c2e865376a386c60c0e248370bbea2d3f3b760d"},
    {file = "contourpy-1.3.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:3faeb2998e4fcb256542e8a926d08da08977f7f5e62cf733f3c211c2a5586223"},
    {file = "contourpy-1.3.0-cp310-cp310-win32.whl", hash = "sha256:36e0cff201bcb17a0a8ecc7f454fe078437fa6bda730e695a92f2d9932bd507f"},
    {file = "contourpy-1.3.0-cp310-cp310-win_amd64.whl", hash = "sha256:87ddffef1dbe5e669b5c2440b643d3fdd8622a348fe1983fad7a0f0ccb1cd67b"},
    {file = "contourpy-1.3.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0fa4c02abe6c446ba70d96ece336e621efa4aecae43eaa9b030ae5fb92b309ad"},
    {file = "contourpy-1.3.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:834e0cfe17ba12f79963861e0f908556b2cedd52e1f75e6578801febcc6a9f49"},
    {file = "contourpy-1.3.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dbc4c3217eee163fa3984fd1567632b48d6dfd29216da3ded3d7b844a8014a66"},
    {file = "contourpy-1.3.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4865cd1d419e0c7a7bf6de1777b185eebdc51470800a9f42b9e9decf17762081"},
    {file = "contourpy-1.3.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:303c252947ab4b14c08afeb52375b26781ccd6a5ccd81abcdfc1fafd14cf93c1"},
    {file = "contourpy-1.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:637f674226be46f6ba372fd29d9523dd977a291f66ab2a74fbeb5530bb3f445d"},
    {file = "contourpy-1.3.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:76a896b2f195b57db25d6b44e7e03f221d32fe318d03ede41f8b4d9ba1bff53c"},
    {file = "contourpy-1.3.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:e1fd23e9d01591bab45546c089ae89d926917a66dceb3abcf01f6105d927e2cb"},
    {file = "contourpy-1.3.0-cp311-cp311-win32.whl", hash = "sha256:d402880b84df3bec6eab53cd0cf802cae6a2ef9537e70cf75e91618a3801c20c"},
    {file = "contourpy-1.3.0-cp311-cp311-win_amd64.whl", hash = "sha256:6cb6cc968059db9c62cb35fbf70248f40994dfcd7aa10444bbf8b3faeb7c2d67"},
    {file = "contourpy-1.3.0-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:570ef7cf892f0afbe5b2ee410c507ce12e15a5fa91017a0009f79f7d93a1268f"},
    {file = "contourpy-1.3.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:da84c537cb8b97d153e9fb208c221c45605f73147bd4cadd23bdae915042aad6"},
    {file = "contourpy-1.3.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0be4d8425bfa755e0fd76ee1e019636ccc7c29f77a7c86b4328a9eb6a26d0639"},
    {file = "contourpy-1.3.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9c0da700bf58f6e0b65312d0a5e695179a71d0163957fa381bb3c1f72972537c"},
    {file = "contourpy-1.3.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:eb8b141bb00fa977d9122636b16aa67d37fd40a3d8b52dd837e536d64b9a4d06"},
    {file = "contourpy-1.3.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3634b5385c6716c258d0419c46d05c8aa7dc8cb70326c9a4fb66b69ad2b52e09"},
    {file = "contourpy-1.3.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:0dce35502151b6bd35027ac39ba6e5a44be13a68f55735c3612c568cac3805fd"},
    {file = "contourpy-1.3.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:aea348f053c645100612b333adc5983d87be69acdc6d77d3169c090d3b01dc35"},
    {file = "contourpy-1.3.0-cp312-cp312-win32.whl", hash = "sha256:90f73a5116ad1ba7174341ef3ea5c3150ddf20b024b98fb0c3b29034752c8aeb"},
    {file = "contourpy-1.3.0-cp312-cp312-win_amd64.whl", hash = "sha256:b11b39aea6be6764f84360fce6c82211a9db32a7c7de8fa6dd5397cf1d079c3b"},
    {file = "contourpy-1.3.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:3e1c7fa44aaae40a2247e2e8e0627f4bea3dd257014764aa644f319a5f8600e3"},
    {file = "contourpy-1.3.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:364174c2a76057feef647c802652f00953b575723062560498dc7930fc9b1cb7"},
    {file = "contourpy-1.3.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:32b238b3b3b649e09ce9aaf51f0c261d38644bdfa35cbaf7b263457850957a84"},
    {file = "contourpy-1.3.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d51fca85f9f7ad0b65b4b9fe800406d0d77017d7270d31ec3fb1cc07358fdea0"},
    {file = "contourpy-1.3.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:732896af21716b29ab3e988d4ce14bc5133733b85956316fb0c56355f398099b"},
    {file = "contourpy-1.3.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d73f659398a0904e125280836ae6f88ba9b178b2fed6884f3b1f95b989d2c8da"},
    {file = "contourpy-1.3.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:c6c7c2408b7048082932cf4e641fa3b8ca848259212f51c8c59c45aa7ac18f14"},
    {file = "contourpy-1.3.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f317576606de89da6b7e0861cf6061f6146ead3528acabff9236458a6ba467f8"},
    {file = "contourpy-1.3.0-cp313-cp313-win32.whl", hash = "sha256:31cd3a85dbdf1fc002280c65caa7e2b5f65e4a973fcdf70dd2fdcb9868069294"},
    {file = "contourpy-1.3.0-cp313-cp313-win_amd64.whl", hash = "sha256:4553c421929ec95fb07b3aaca0fae668b2eb5a5203d1217ca7c34c063c53d087"},
    {file = "contourpy-1.3.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:345af746d7766821d05d72cb8f3845dfd08dd137101a2cb9b24de277d716def8"},
    {file = "contourpy-1.3.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3bb3808858a9dc68f6f03d319acd5f1b8a337e6cdda197f02f4b8ff67ad2057b"},
    {file = "contourpy-1.3.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:420d39daa61aab1221567b42eecb01112908b2cab7f1b4106a52caaec8d36973"},
    {file = "contourpy-1.3.0-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4d63ee447261e963af02642ffcb864e5a2ee4cbfd78080657a9880b8b1868e18"},
    {file = "contourpy-1.3.0-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:167d6c890815e1dac9536dca00828b445d5d0df4d6a8c6adb4a7ec3166812fa8"},
    {file = "contourpy-1.3.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:710a26b3dc80c0e4febf04555de66f5fd17e9cf7170a7b08000601a10570bda6"},
    {file = "contourpy-1.3.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:75ee7cb1a14c617f34a51d11fa7524173e56551646828353c4af859c56b766e2"},
    {file = "contourpy-1.3.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:33c92cdae89ec5135d036e7218e69b0bb2851206077251f04a6c4e0e21f03927"},
    {file = "contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:a11077e395f67ffc2c44ec2418cfebed032cd6da3022a94fc227b6faf8e2acb8"},
    {file = "contourpy-1.3.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:e8134301d7e204c88ed7ab50028ba06c683000040ede1d617298611f9dc6240c"},
    {file = "contourpy-1.3.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e12968fdfd5bb45ffdf6192a590bd8ddd3ba9e58360b29683c6bb71a7b41edca"},
    {file = "contourpy-1.3.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:fd2a0fc506eccaaa7595b7e1418951f213cf8255be2600f1ea1b61e46a60c55f"},
    {file = "contourpy-1.3.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4cfb5c62ce023dfc410d6059c936dcf96442ba40814aefbfa575425a3a7f19dc"},
    {file = "contourpy-1.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:68a32389b06b82c2fdd68276148d7b9275b5f5cf13e5417e4252f6d1a34f72a2"},
    {file = "contourpy-1.3.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:94e848a6b83da10898cbf1311a815f770acc9b6a3f2d646f330d57eb4e87592e"},
    {file = "contourpy-1.3.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:d78ab28a03c854a873787a0a42254a0ccb3cb133c672f645c9f9c8f3ae9d0800"},
    {file = "contourpy-1.3.0-cp39-cp39-win32.whl", hash = "sha256:81cb5ed4952aae6014bc9d0421dec7c5835c9c8c31cdf51910b708f548cf58e5"},
    {file = "contourpy-1.3.0-cp39-cp39-win_amd64.whl", hash = "sha256:14e262f67bd7e6eb6880bc564dcda30b15e351a594657e55b7eec94b6ef72843"},
    {file = "contourpy-1.3.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:fe41b41505a5a33aeaed2a613dccaeaa74e0e3ead6dd6fd3a118fb471644fd6c"},
    {file = "contourpy-1.3.0-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eca7e17a65f72a5133bdbec9ecf22401c62bcf4821361ef7811faee695799779"},
    {file = "contourpy-1.3.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:1ec4dc6bf570f5b22ed0d7efba0dfa9c5b9e0431aeea7581aa217542d9e809a4"},
    {file = "contourpy-1.3.0-pp39-pypy39_pp73-macosx_10_15_x86_64.whl", hash = "sha256:00ccd0dbaad6d804ab259820fa7cb0b8036bda0686ef844d24125d8287178ce0"},
    {file = "contourpy-1.3.0-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8ca947601224119117f7c19c9cdf6b3ab54c5726ef1d906aa4a69dfb6dd58102"},
    {file = "contourpy-1.3.0-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:c6ec93afeb848a0845a18989da3beca3eec2c0f852322efe21af1931147d12cb"},
    {file = "contourpy-1.3.0.tar.gz", hash = "sha256:7ffa0db17717a8ffb127efd0c95a4362d996b892c2904db72428d5b52e1938a4"},
]

[package.dependencies]
numpy = ">=1.23"

[package.extras]
bokeh = ["bokeh", "selenium"]
docs = ["furo", "sphinx (>=7.2)", "sphinx-copybutton"]
mypy = ["contourpy[bokeh,docs]", "docutils-stubs", "mypy (==1.11.1)", "types-Pillow"]
test = ["Pillow", "contourpy[test-no-images]", "matplotlib"]
test-no-images = ["pytest", "pytest-cov", "pytest-rerunfailures", "pytest-xdist", "wurlitzer"]

[[package]]
name = "coverage"
version = "7.6.4"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "coverage-7.6.4-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:5f8ae553cba74085db385d489c7a792ad66f7f9ba2ee85bfa508aeb84cf0ba07"},
    {file = "coverage-7.6.4-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8165b796df0bd42e10527a3f493c592ba494f16ef3c8b531288e3d0d72c1f6f0"},
    {file = "coverage-7.6.4-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c7c8b95bf47db6d19096a5e052ffca0a05f335bc63cef281a6e8fe864d450a72"},
    {file = "coverage-7.6.4-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8ed9281d1b52628e81393f5eaee24a45cbd64965f41857559c2b7ff19385df51"},
    {file = "coverage-7.6.4-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0809082ee480bb8f7416507538243c8863ac74fd8a5d2485c46f0f7499f2b491"},
    {file = "coverage-7.6.4-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d541423cdd416b78626b55f123412fcf979d22a2c39fce251b350de38c15c15b"},
    {file = "coverage-7.6.4-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:58809e238a8a12a625c70450b48e8767cff9eb67c62e6154a642b21ddf79baea"},
    {file = "coverage-7.6.4-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:c9b8e184898ed014884ca84c70562b4a82cbc63b044d366fedc68bc2b2f3394a"},
    {file = "coverage-7.6.4-cp310-cp310-win32.whl", hash = "sha256:6bd818b7ea14bc6e1f06e241e8234508b21edf1b242d49831831a9450e2f35fa"},
    {file = "coverage-7.6.4-cp310-cp310-win_amd64.whl", hash = "sha256:06babbb8f4e74b063dbaeb74ad68dfce9186c595a15f11f5d5683f748fa1d172"},
    {file = "coverage-7.6.4-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:73d2b73584446e66ee633eaad1a56aad577c077f46c35ca3283cd687b7715b0b"},
    {file = "coverage-7.6.4-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:51b44306032045b383a7a8a2c13878de375117946d68dcb54308111f39775a25"},
    {file = "coverage-7.6.4-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0b3fb02fe73bed561fa12d279a417b432e5b50fe03e8d663d61b3d5990f29546"},
    {file = "coverage-7.6.4-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ed8fe9189d2beb6edc14d3ad19800626e1d9f2d975e436f84e19efb7fa19469b"},
    {file = "coverage-7.6.4-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b369ead6527d025a0fe7bd3864e46dbee3aa8f652d48df6174f8d0bac9e26e0e"},
    {file = "coverage-7.6.4-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:ade3ca1e5f0ff46b678b66201f7ff477e8fa11fb537f3b55c3f0568fbfe6e718"},
    {file = "coverage-7.6.4-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:27fb4a050aaf18772db513091c9c13f6cb94ed40eacdef8dad8411d92d9992db"},
    {file = "coverage-7.6.4-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:4f704f0998911abf728a7783799444fcbbe8261c4a6c166f667937ae6a8aa522"},
    {file = "coverage-7.6.4-cp311-cp311-win32.whl", hash = "sha256:29155cd511ee058e260db648b6182c419422a0d2e9a4fa44501898cf918866cf"},
    {file = "coverage-7.6.4-cp311-cp311-win_amd64.whl", hash = "sha256:8902dd6a30173d4ef09954bfcb24b5d7b5190cf14a43170e386979651e09ba19"},
    {file = "coverage-7.6.4-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:12394842a3a8affa3ba62b0d4ab7e9e210c5e366fbac3e8b2a68636fb19892c2"},
    {file = "coverage-7.6.4-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:2b6b4c83d8e8ea79f27ab80778c19bc037759aea298da4b56621f4474ffeb117"},
    {file = "coverage-7.6.4-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1d5b8007f81b88696d06f7df0cb9af0d3b835fe0c8dbf489bad70b45f0e45613"},
    {file = "coverage-7.6.4-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b57b768feb866f44eeed9f46975f3d6406380275c5ddfe22f531a2bf187eda27"},
    {file = "coverage-7.6.4-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5915fcdec0e54ee229926868e9b08586376cae1f5faa9bbaf8faf3561b393d52"},
    {file = "coverage-7.6.4-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:0b58c672d14f16ed92a48db984612f5ce3836ae7d72cdd161001cc54512571f2"},
    {file = "coverage-7.6.4-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:2fdef0d83a2d08d69b1f2210a93c416d54e14d9eb398f6ab2f0a209433db19e1"},
    {file = "coverage-7.6.4-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8cf717ee42012be8c0cb205dbbf18ffa9003c4cbf4ad078db47b95e10748eec5"},
    {file = "coverage-7.6.4-cp312-cp312-win32.whl", hash = "sha256:7bb92c539a624cf86296dd0c68cd5cc286c9eef2d0c3b8b192b604ce9de20a17"},
    {file = "coverage-7.6.4-cp312-cp312-win_amd64.whl", hash = "sha256:1032e178b76a4e2b5b32e19d0fd0abbce4b58e77a1ca695820d10e491fa32b08"},
    {file = "coverage-7.6.4-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:023bf8ee3ec6d35af9c1c6ccc1d18fa69afa1cb29eaac57cb064dbb262a517f9"},
    {file = "coverage-7.6.4-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:b0ac3d42cb51c4b12df9c5f0dd2f13a4f24f01943627120ec4d293c9181219ba"},
    {file = "coverage-7.6.4-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f8fe4984b431f8621ca53d9380901f62bfb54ff759a1348cd140490ada7b693c"},
    {file = "coverage-7.6.4-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5fbd612f8a091954a0c8dd4c0b571b973487277d26476f8480bfa4b2a65b5d06"},
    {file = "coverage-7.6.4-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dacbc52de979f2823a819571f2e3a350a7e36b8cb7484cdb1e289bceaf35305f"},
    {file = "coverage-7.6.4-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:dab4d16dfef34b185032580e2f2f89253d302facba093d5fa9dbe04f569c4f4b"},
    {file = "coverage-7.6.4-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:862264b12ebb65ad8d863d51f17758b1684560b66ab02770d4f0baf2ff75da21"},
    {file = "coverage-7.6.4-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5beb1ee382ad32afe424097de57134175fea3faf847b9af002cc7895be4e2a5a"},
    {file = "coverage-7.6.4-cp313-cp313-win32.whl", hash = "sha256:bf20494da9653f6410213424f5f8ad0ed885e01f7e8e59811f572bdb20b8972e"},
    {file = "coverage-7.6.4-cp313-cp313-win_amd64.whl", hash = "sha256:182e6cd5c040cec0a1c8d415a87b67ed01193ed9ad458ee427741c7d8513d963"},
    {file = "coverage-7.6.4-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:a181e99301a0ae128493a24cfe5cfb5b488c4e0bf2f8702091473d033494d04f"},
    {file = "coverage-7.6.4-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:df57bdbeffe694e7842092c5e2e0bc80fff7f43379d465f932ef36f027179806"},
    {file = "coverage-7.6.4-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0bcd1069e710600e8e4cf27f65c90c7843fa8edfb4520fb0ccb88894cad08b11"},
    {file = "coverage-7.6.4-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:99b41d18e6b2a48ba949418db48159d7a2e81c5cc290fc934b7d2380515bd0e3"},
    {file = "coverage-7.6.4-cp313-cp313t-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a6b1e54712ba3474f34b7ef7a41e65bd9037ad47916ccb1cc78769bae324c01a"},
    {file = "coverage-7.6.4-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:53d202fd109416ce011578f321460795abfe10bb901b883cafd9b3ef851bacfc"},
    {file = "coverage-7.6.4-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:c48167910a8f644671de9f2083a23630fbf7a1cb70ce939440cd3328e0919f70"},
    {file = "coverage-7.6.4-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:cc8ff50b50ce532de2fa7a7daae9dd12f0a699bfcd47f20945364e5c31799fef"},
    {file = "coverage-7.6.4-cp313-cp313t-win32.whl", hash = "sha256:b8d3a03d9bfcaf5b0141d07a88456bb6a4c3ce55c080712fec8418ef3610230e"},
    {file = "coverage-7.6.4-cp313-cp313t-win_amd64.whl", hash = "sha256:f3ddf056d3ebcf6ce47bdaf56142af51bb7fad09e4af310241e9db7a3a8022e1"},
    {file = "coverage-7.6.4-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:9cb7fa111d21a6b55cbf633039f7bc2749e74932e3aa7cb7333f675a58a58bf3"},
    {file = "coverage-7.6.4-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:11a223a14e91a4693d2d0755c7a043db43d96a7450b4f356d506c2562c48642c"},
    {file = "coverage-7.6.4-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a413a096c4cbac202433c850ee43fa326d2e871b24554da8327b01632673a076"},
    {file = "coverage-7.6.4-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:00a1d69c112ff5149cabe60d2e2ee948752c975d95f1e1096742e6077affd376"},
    {file = "coverage-7.6.4-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1f76846299ba5c54d12c91d776d9605ae33f8ae2b9d1d3c3703cf2db1a67f2c0"},
    {file = "coverage-7.6.4-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:fe439416eb6380de434886b00c859304338f8b19f6f54811984f3420a2e03858"},
    {file = "coverage-7.6.4-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:0294ca37f1ba500667b1aef631e48d875ced93ad5e06fa665a3295bdd1d95111"},
    {file = "coverage-7.6.4-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:6f01ba56b1c0e9d149f9ac85a2f999724895229eb36bd997b61e62999e9b0901"},
    {file = "coverage-7.6.4-cp39-cp39-win32.whl", hash = "sha256:bc66f0bf1d7730a17430a50163bb264ba9ded56739112368ba985ddaa9c3bd09"},
    {file = "coverage-7.6.4-cp39-cp39-win_amd64.whl", hash = "sha256:c481b47f6b5845064c65a7bc78bc0860e635a9b055af0df46fdf1c58cebf8e8f"},
    {file = "coverage-7.6.4-pp39.pp310-none-any.whl", hash = "sha256:3c65d37f3a9ebb703e710befdc489a38683a5b152242664b973a7b7b22348a4e"},
    {file = "coverage-7.6.4.tar.gz", hash = "sha256:29fc0f17b1d3fea332f8001d4558f8214af7f1d87a345f3a133c901d60347c73"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "cycler"
version = "0.12.1"
description = "Composable style cycles"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "cycler-0.12.1-py3-none-any.whl", hash = "sha256:85cef7cff222d8644161529808465972e51340599459b8ac3ccbac5a854e0d30"},
    {file = "cycler-0.12.1.tar.gz", hash = "sha256:88bb128f02ba341da8ef447245a9e138fae777f6a23943da4540077d3601eb1c"},
]

[package.extras]
docs = ["ipython", "matplotlib", "numpydoc", "sphinx"]
tests = ["pytest", "pytest-cov", "pytest-xdist"]

[[package]]
name = "decorator"
version = "5.1.1"
description = "Decorators for Humans"
optional = false
python-versions = ">=3.5"
groups = ["dev"]
files = [
    {file = "decorator-5.1.1-py3-none-any.whl", hash = "sha256:b8c3f85900b9dc423225913c5aace94729fe1fa9763b38939a95226f02d37186"},
    {file = "decorator-5.1.1.tar.gz", hash = "sha256:637996211036b6385ef91435e4fae22989472f9d571faba8927ba8253acbc330"},
]

[[package]]
name = "deprecation"
version = "2.1.0"
description = "A library to handle automated deprecations"
optional = false
python-versions = "*"
groups = ["main", "dev"]
files = [
    {file = "deprecation-2.1.0-py2.py3-none-any.whl", hash = "sha256:a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a"},
    {file = "deprecation-2.1.0.tar.gz", hash = "sha256:72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff"},
]

[package.dependencies]
packaging = "*"

[[package]]
name = "exceptiongroup"
version = "1.2.2"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "exceptiongroup-1.2.2-py3-none-any.whl", hash = "sha256:3111b9d131c238bec2f8f516e123e14ba243563fb135d3fe885990585aa7795b"},
    {file = "exceptiongroup-1.2.2.tar.gz", hash = "sha256:47c2edf7c6738fafb49fd34290706d1a1a2f4d1c6df275526b62cbb4aa5393cc"},
]

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "executing"
version = "2.0.1"
description = "Get the currently executing AST node of a frame, and other information"
optional = false
python-versions = ">=3.5"
groups = ["main", "dev"]
files = [
    {file = "executing-2.0.1-py2.py3-none-any.whl", hash = "sha256:eac49ca94516ccc753f9fb5ce82603156e590b27525a8bc32cce8ae302eb61bc"},
    {file = "executing-2.0.1.tar.gz", hash = "sha256:35afe2ce3affba8ee97f2d69927fa823b08b472b7b994e36a52a964b93d16147"},
]

[package.extras]
tests = ["asttokens (>=2.1.0)", "coverage", "coverage-enable-subprocess", "ipython", "littleutils", "pytest", "rich ; python_version >= \"3.11\""]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["dev"]
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
groups = ["dev"]
markers = "python_version == \"3.12\""
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
version = "0.3.6"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "flake8-black-0.3.6.tar.gz", hash = "sha256:0dfbca3274777792a5bcb2af887a4cad72c72d0e86c94e08e3a3de151bb41c34"},
    {file = "flake8_black-0.3.6-py3-none-any.whl", hash = "sha256:fe8ea2eca98d8a504f22040d9117347f6b367458366952862ac3586e7d4eeaca"},
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
groups = ["dev"]
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
groups = ["dev"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "fonttools"
version = "4.54.1"
description = "Tools to manipulate font files"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "fonttools-4.54.1-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:7ed7ee041ff7b34cc62f07545e55e1468808691dddfd315d51dd82a6b37ddef2"},
    {file = "fonttools-4.54.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:41bb0b250c8132b2fcac148e2e9198e62ff06f3cc472065dff839327945c5882"},
    {file = "fonttools-4.54.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7965af9b67dd546e52afcf2e38641b5be956d68c425bef2158e95af11d229f10"},
    {file = "fonttools-4.54.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:278913a168f90d53378c20c23b80f4e599dca62fbffae4cc620c8eed476b723e"},
    {file = "fonttools-4.54.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0e88e3018ac809b9662615072dcd6b84dca4c2d991c6d66e1970a112503bba7e"},
    {file = "fonttools-4.54.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4aa4817f0031206e637d1e685251ac61be64d1adef111060df84fdcbc6ab6c44"},
    {file = "fonttools-4.54.1-cp310-cp310-win32.whl", hash = "sha256:7e3b7d44e18c085fd8c16dcc6f1ad6c61b71ff463636fcb13df7b1b818bd0c02"},
    {file = "fonttools-4.54.1-cp310-cp310-win_amd64.whl", hash = "sha256:dd9cc95b8d6e27d01e1e1f1fae8559ef3c02c76317da650a19047f249acd519d"},
    {file = "fonttools-4.54.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:5419771b64248484299fa77689d4f3aeed643ea6630b2ea750eeab219588ba20"},
    {file = "fonttools-4.54.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:301540e89cf4ce89d462eb23a89464fef50915255ece765d10eee8b2bf9d75b2"},
    {file = "fonttools-4.54.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:76ae5091547e74e7efecc3cbf8e75200bc92daaeb88e5433c5e3e95ea8ce5aa7"},
    {file = "fonttools-4.54.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:82834962b3d7c5ca98cb56001c33cf20eb110ecf442725dc5fdf36d16ed1ab07"},
    {file = "fonttools-4.54.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d26732ae002cc3d2ecab04897bb02ae3f11f06dd7575d1df46acd2f7c012a8d8"},
    {file = "fonttools-4.54.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:58974b4987b2a71ee08ade1e7f47f410c367cdfc5a94fabd599c88165f56213a"},
    {file = "fonttools-4.54.1-cp311-cp311-win32.whl", hash = "sha256:ab774fa225238986218a463f3fe151e04d8c25d7de09df7f0f5fce27b1243dbc"},
    {file = "fonttools-4.54.1-cp311-cp311-win_amd64.whl", hash = "sha256:07e005dc454eee1cc60105d6a29593459a06321c21897f769a281ff2d08939f6"},
    {file = "fonttools-4.54.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:54471032f7cb5fca694b5f1a0aaeba4af6e10ae989df408e0216f7fd6cdc405d"},
    {file = "fonttools-4.54.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8fa92cb248e573daab8d032919623cc309c005086d743afb014c836636166f08"},
    {file = "fonttools-4.54.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0a911591200114969befa7f2cb74ac148bce5a91df5645443371aba6d222e263"},
    {file = "fonttools-4.54.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:93d458c8a6a354dc8b48fc78d66d2a8a90b941f7fec30e94c7ad9982b1fa6bab"},
    {file = "fonttools-4.54.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5eb2474a7c5be8a5331146758debb2669bf5635c021aee00fd7c353558fc659d"},
    {file = "fonttools-4.54.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:c9c563351ddc230725c4bdf7d9e1e92cbe6ae8553942bd1fb2b2ff0884e8b714"},
    {file = "fonttools-4.54.1-cp312-cp312-win32.whl", hash = "sha256:fdb062893fd6d47b527d39346e0c5578b7957dcea6d6a3b6794569370013d9ac"},
    {file = "fonttools-4.54.1-cp312-cp312-win_amd64.whl", hash = "sha256:e4564cf40cebcb53f3dc825e85910bf54835e8a8b6880d59e5159f0f325e637e"},
    {file = "fonttools-4.54.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:6e37561751b017cf5c40fce0d90fd9e8274716de327ec4ffb0df957160be3bff"},
    {file = "fonttools-4.54.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:357cacb988a18aace66e5e55fe1247f2ee706e01debc4b1a20d77400354cddeb"},
    {file = "fonttools-4.54.1-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f8e953cc0bddc2beaf3a3c3b5dd9ab7554677da72dfaf46951e193c9653e515a"},
    {file = "fonttools-4.54.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:58d29b9a294573d8319f16f2f79e42428ba9b6480442fa1836e4eb89c4d9d61c"},
    {file = "fonttools-4.54.1-cp313-cp313-win32.whl", hash = "sha256:9ef1b167e22709b46bf8168368b7b5d3efeaaa746c6d39661c1b4405b6352e58"},
    {file = "fonttools-4.54.1-cp313-cp313-win_amd64.whl", hash = "sha256:262705b1663f18c04250bd1242b0515d3bbae177bee7752be67c979b7d47f43d"},
    {file = "fonttools-4.54.1-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:ed2f80ca07025551636c555dec2b755dd005e2ea8fbeb99fc5cdff319b70b23b"},
    {file = "fonttools-4.54.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:9dc080e5a1c3b2656caff2ac2633d009b3a9ff7b5e93d0452f40cd76d3da3b3c"},
    {file = "fonttools-4.54.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1d152d1be65652fc65e695e5619e0aa0982295a95a9b29b52b85775243c06556"},
    {file = "fonttools-4.54.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8583e563df41fdecef31b793b4dd3af8a9caa03397be648945ad32717a92885b"},
    {file = "fonttools-4.54.1-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:0d1d353ef198c422515a3e974a1e8d5b304cd54a4c2eebcae708e37cd9eeffb1"},
    {file = "fonttools-4.54.1-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:fda582236fee135d4daeca056c8c88ec5f6f6d88a004a79b84a02547c8f57386"},
    {file = "fonttools-4.54.1-cp38-cp38-win32.whl", hash = "sha256:e7d82b9e56716ed32574ee106cabca80992e6bbdcf25a88d97d21f73a0aae664"},
    {file = "fonttools-4.54.1-cp38-cp38-win_amd64.whl", hash = "sha256:ada215fd079e23e060157aab12eba0d66704316547f334eee9ff26f8c0d7b8ab"},
    {file = "fonttools-4.54.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:f5b8a096e649768c2f4233f947cf9737f8dbf8728b90e2771e2497c6e3d21d13"},
    {file = "fonttools-4.54.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:4e10d2e0a12e18f4e2dd031e1bf7c3d7017be5c8dbe524d07706179f355c5dac"},
    {file = "fonttools-4.54.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:31c32d7d4b0958600eac75eaf524b7b7cb68d3a8c196635252b7a2c30d80e986"},
    {file = "fonttools-4.54.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c39287f5c8f4a0c5a55daf9eaf9ccd223ea59eed3f6d467133cc727d7b943a55"},
    {file = "fonttools-4.54.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:a7a310c6e0471602fe3bf8efaf193d396ea561486aeaa7adc1f132e02d30c4b9"},
    {file = "fonttools-4.54.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:d3b659d1029946f4ff9b6183984578041b520ce0f8fb7078bb37ec7445806b33"},
    {file = "fonttools-4.54.1-cp39-cp39-win32.whl", hash = "sha256:e96bc94c8cda58f577277d4a71f51c8e2129b8b36fd05adece6320dd3d57de8a"},
    {file = "fonttools-4.54.1-cp39-cp39-win_amd64.whl", hash = "sha256:e8a4b261c1ef91e7188a30571be6ad98d1c6d9fa2427244c545e2fa0a2494dd7"},
    {file = "fonttools-4.54.1-py3-none-any.whl", hash = "sha256:37cddd62d83dc4f72f7c3f3c2bcf2697e89a30efb152079896544a93907733bd"},
    {file = "fonttools-4.54.1.tar.gz", hash = "sha256:957f669d4922f92c171ba01bef7f29410668db09f6c02111e22b2bce446f3285"},
]

[package.extras]
all = ["brotli (>=1.0.1) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=0.8.0) ; platform_python_implementation != \"CPython\"", "fs (>=2.2.0,<3)", "lxml (>=4.0)", "lz4 (>=1.7.4.2)", "matplotlib", "munkres ; platform_python_implementation == \"PyPy\"", "pycairo", "scipy ; platform_python_implementation != \"PyPy\"", "skia-pathops (>=0.5.0)", "sympy", "uharfbuzz (>=0.23.0)", "unicodedata2 (>=15.1.0) ; python_version <= \"3.12\"", "xattr ; sys_platform == \"darwin\"", "zopfli (>=0.1.4)"]
graphite = ["lz4 (>=1.7.4.2)"]
interpolatable = ["munkres ; platform_python_implementation == \"PyPy\"", "pycairo", "scipy ; platform_python_implementation != \"PyPy\""]
lxml = ["lxml (>=4.0)"]
pathops = ["skia-pathops (>=0.5.0)"]
plot = ["matplotlib"]
repacker = ["uharfbuzz (>=0.23.0)"]
symfont = ["sympy"]
type1 = ["xattr ; sys_platform == \"darwin\""]
ufo = ["fs (>=2.2.0,<3)"]
unicode = ["unicodedata2 (>=15.1.0) ; python_version <= \"3.12\""]
woff = ["brotli (>=1.0.1) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=0.8.0) ; platform_python_implementation != \"CPython\"", "zopfli (>=0.1.4)"]

[[package]]
name = "hightime"
version = "0.2.2"
description = "Hightime Python API"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "hightime-0.2.2-py3-none-any.whl", hash = "sha256:5109a449bb3a75dbf305147777de71634c91b943d47cfbee18ed2f34a8307e0b"},
]

[[package]]
name = "iniconfig"
version = "2.0.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "iniconfig-2.0.0-py3-none-any.whl", hash = "sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374"},
    {file = "iniconfig-2.0.0.tar.gz", hash = "sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"},
]

[[package]]
name = "ipython"
version = "8.17.2"
description = "IPython: Productive Interactive Computing"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "ipython-8.17.2-py3-none-any.whl", hash = "sha256:1e4d1d666a023e3c93585ba0d8e962867f7a111af322efff6b9c58062b3e5444"},
    {file = "ipython-8.17.2.tar.gz", hash = "sha256:126bb57e1895594bb0d91ea3090bbd39384f6fe87c3d57fd558d0670f50339bb"},
]

[package.dependencies]
appnope = {version = "*", markers = "sys_platform == \"darwin\""}
colorama = {version = "*", markers = "sys_platform == \"win32\""}
decorator = "*"
exceptiongroup = {version = "*", markers = "python_version < \"3.11\""}
jedi = ">=0.16"
matplotlib-inline = "*"
pexpect = {version = ">4.3", markers = "sys_platform != \"win32\""}
prompt-toolkit = ">=3.0.30,<3.0.37 || >3.0.37,<3.1.0"
pygments = ">=2.4.0"
stack-data = "*"
traitlets = ">=5"

[package.extras]
all = ["black", "curio", "docrepr", "exceptiongroup", "ipykernel", "ipyparallel", "ipywidgets", "matplotlib", "matplotlib (!=3.2.0)", "nbconvert", "nbformat", "notebook", "numpy (>=1.22)", "pandas", "pickleshare", "pytest (<7)", "pytest (<7.1)", "pytest-asyncio (<0.22)", "qtconsole", "setuptools (>=18.5)", "sphinx (>=1.3)", "sphinx-rtd-theme", "stack-data", "testpath", "trio", "typing-extensions"]
black = ["black"]
doc = ["docrepr", "exceptiongroup", "ipykernel", "matplotlib", "pickleshare", "pytest (<7)", "pytest (<7.1)", "pytest-asyncio (<0.22)", "setuptools (>=18.5)", "sphinx (>=1.3)", "sphinx-rtd-theme", "stack-data", "testpath", "typing-extensions"]
kernel = ["ipykernel"]
nbconvert = ["nbconvert"]
nbformat = ["nbformat"]
notebook = ["ipywidgets", "notebook"]
parallel = ["ipyparallel"]
qtconsole = ["qtconsole"]
test = ["pickleshare", "pytest (<7.1)", "pytest-asyncio (<0.22)", "testpath"]
test-extra = ["curio", "matplotlib (!=3.2.0)", "nbformat", "numpy (>=1.22)", "pandas", "pickleshare", "pytest (<7.1)", "pytest-asyncio (<0.22)", "testpath", "trio"]

[[package]]
name = "isort"
version = "5.13.2"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.8.0"
groups = ["dev"]
files = [
    {file = "isort-5.13.2-py3-none-any.whl", hash = "sha256:8ca5e72a8d85860d5a3fa69b8745237f2939afe12dbf656afbcb47fe72d947a6"},
    {file = "isort-5.13.2.tar.gz", hash = "sha256:48fdfcb9face5d58a4f6dde2e72a1fb8dcaf8ab26f95ab49fab84c2ddefb0109"},
]

[package.extras]
colors = ["colorama (>=0.4.6)"]

[[package]]
name = "jedi"
version = "0.19.1"
description = "An autocompletion tool for Python that can be used for text editors."
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "jedi-0.19.1-py2.py3-none-any.whl", hash = "sha256:e983c654fe5c02867aef4cdfce5a2fbb4a50adc0af145f70504238f18ef5e7e0"},
    {file = "jedi-0.19.1.tar.gz", hash = "sha256:cf0496f3651bc65d7174ac1b7d043eff454892c708a87d1b683e57b569927ffd"},
]

[package.dependencies]
parso = ">=0.8.3,<0.9.0"

[package.extras]
docs = ["Jinja2 (==2.11.3)", "MarkupSafe (==1.1.1)", "Pygments (==2.8.1)", "alabaster (==0.7.12)", "babel (==2.9.1)", "chardet (==4.0.0)", "commonmark (==0.8.1)", "docutils (==0.17.1)", "future (==0.18.2)", "idna (==2.10)", "imagesize (==1.2.0)", "mock (==1.0.1)", "packaging (==20.9)", "pyparsing (==2.4.7)", "pytz (==2021.1)", "readthedocs-sphinx-ext (==2.1.4)", "recommonmark (==0.5.0)", "requests (==2.25.1)", "six (==1.15.0)", "snowballstemmer (==2.1.0)", "sphinx (==1.8.5)", "sphinx-rtd-theme (==0.4.3)", "sphinxcontrib-serializinghtml (==1.1.4)", "sphinxcontrib-websupport (==1.2.4)", "urllib3 (==1.26.4)"]
qa = ["flake8 (==5.0.4)", "mypy (==0.971)", "types-setuptools (==67.2.0.1)"]
testing = ["Django", "attrs", "colorama", "docopt", "pytest (<7.0.0)"]

[[package]]
name = "kiwisolver"
version = "1.4.7"
description = "A fast implementation of the Cassowary constraint solver"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "kiwisolver-1.4.7-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:8a9c83f75223d5e48b0bc9cb1bf2776cf01563e00ade8775ffe13b0b6e1af3a6"},
    {file = "kiwisolver-1.4.7-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:58370b1ffbd35407444d57057b57da5d6549d2d854fa30249771775c63b5fe17"},
    {file = "kiwisolver-1.4.7-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:aa0abdf853e09aff551db11fce173e2177d00786c688203f52c87ad7fcd91ef9"},
    {file = "kiwisolver-1.4.7-cp310-cp310-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:8d53103597a252fb3ab8b5845af04c7a26d5e7ea8122303dd7a021176a87e8b9"},
    {file = "kiwisolver-1.4.7-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:88f17c5ffa8e9462fb79f62746428dd57b46eb931698e42e990ad63103f35e6c"},
    {file = "kiwisolver-1.4.7-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:88a9ca9c710d598fd75ee5de59d5bda2684d9db36a9f50b6125eaea3969c2599"},
    {file = "kiwisolver-1.4.7-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f4d742cb7af1c28303a51b7a27aaee540e71bb8e24f68c736f6f2ffc82f2bf05"},
    {file = "kiwisolver-1.4.7-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e28c7fea2196bf4c2f8d46a0415c77a1c480cc0724722f23d7410ffe9842c407"},
    {file = "kiwisolver-1.4.7-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:e968b84db54f9d42046cf154e02911e39c0435c9801681e3fc9ce8a3c4130278"},
    {file = "kiwisolver-1.4.7-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:0c18ec74c0472de033e1bebb2911c3c310eef5649133dd0bedf2a169a1b269e5"},
    {file = "kiwisolver-1.4.7-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:8f0ea6da6d393d8b2e187e6a5e3fb81f5862010a40c3945e2c6d12ae45cfb2ad"},
    {file = "kiwisolver-1.4.7-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:f106407dda69ae456dd1227966bf445b157ccc80ba0dff3802bb63f30b74e895"},
    {file = "kiwisolver-1.4.7-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:84ec80df401cfee1457063732d90022f93951944b5b58975d34ab56bb150dfb3"},
    {file = "kiwisolver-1.4.7-cp310-cp310-win32.whl", hash = "sha256:71bb308552200fb2c195e35ef05de12f0c878c07fc91c270eb3d6e41698c3bcc"},
    {file = "kiwisolver-1.4.7-cp310-cp310-win_amd64.whl", hash = "sha256:44756f9fd339de0fb6ee4f8c1696cfd19b2422e0d70b4cefc1cc7f1f64045a8c"},
    {file = "kiwisolver-1.4.7-cp310-cp310-win_arm64.whl", hash = "sha256:78a42513018c41c2ffd262eb676442315cbfe3c44eed82385c2ed043bc63210a"},
    {file = "kiwisolver-1.4.7-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:d2b0e12a42fb4e72d509fc994713d099cbb15ebf1103545e8a45f14da2dfca54"},
    {file = "kiwisolver-1.4.7-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:2a8781ac3edc42ea4b90bc23e7d37b665d89423818e26eb6df90698aa2287c95"},
    {file = "kiwisolver-1.4.7-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:46707a10836894b559e04b0fd143e343945c97fd170d69a2d26d640b4e297935"},
    {file = "kiwisolver-1.4.7-cp311-cp311-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ef97b8df011141c9b0f6caf23b29379f87dd13183c978a30a3c546d2c47314cb"},
    {file = "kiwisolver-1.4.7-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3ab58c12a2cd0fc769089e6d38466c46d7f76aced0a1f54c77652446733d2d02"},
    {file = "kiwisolver-1.4.7-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:803b8e1459341c1bb56d1c5c010406d5edec8a0713a0945851290a7930679b51"},
    {file = "kiwisolver-1.4.7-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f9a9e8a507420fe35992ee9ecb302dab68550dedc0da9e2880dd88071c5fb052"},
    {file = "kiwisolver-1.4.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:18077b53dc3bb490e330669a99920c5e6a496889ae8c63b58fbc57c3d7f33a18"},
    {file = "kiwisolver-1.4.7-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:6af936f79086a89b3680a280c47ea90b4df7047b5bdf3aa5c524bbedddb9e545"},
    {file = "kiwisolver-1.4.7-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:3abc5b19d24af4b77d1598a585b8a719beb8569a71568b66f4ebe1fb0449460b"},
    {file = "kiwisolver-1.4.7-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:933d4de052939d90afbe6e9d5273ae05fb836cc86c15b686edd4b3560cc0ee36"},
    {file = "kiwisolver-1.4.7-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:65e720d2ab2b53f1f72fb5da5fb477455905ce2c88aaa671ff0a447c2c80e8e3"},
    {file = "kiwisolver-1.4.7-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3bf1ed55088f214ba6427484c59553123fdd9b218a42bbc8c6496d6754b1e523"},
    {file = "kiwisolver-1.4.7-cp311-cp311-win32.whl", hash = "sha256:4c00336b9dd5ad96d0a558fd18a8b6f711b7449acce4c157e7343ba92dd0cf3d"},
    {file = "kiwisolver-1.4.7-cp311-cp311-win_amd64.whl", hash = "sha256:929e294c1ac1e9f615c62a4e4313ca1823ba37326c164ec720a803287c4c499b"},
    {file = "kiwisolver-1.4.7-cp311-cp311-win_arm64.whl", hash = "sha256:e33e8fbd440c917106b237ef1a2f1449dfbb9b6f6e1ce17c94cd6a1e0d438376"},
    {file = "kiwisolver-1.4.7-cp312-cp312-macosx_10_9_universal2.whl", hash = "sha256:5360cc32706dab3931f738d3079652d20982511f7c0ac5711483e6eab08efff2"},
    {file = "kiwisolver-1.4.7-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:942216596dc64ddb25adb215c3c783215b23626f8d84e8eff8d6d45c3f29f75a"},
    {file = "kiwisolver-1.4.7-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:48b571ecd8bae15702e4f22d3ff6a0f13e54d3d00cd25216d5e7f658242065ee"},
    {file = "kiwisolver-1.4.7-cp312-cp312-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ad42ba922c67c5f219097b28fae965e10045ddf145d2928bfac2eb2e17673640"},
    {file = "kiwisolver-1.4.7-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:612a10bdae23404a72941a0fc8fa2660c6ea1217c4ce0dbcab8a8f6543ea9e7f"},
    {file = "kiwisolver-1.4.7-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9e838bba3a3bac0fe06d849d29772eb1afb9745a59710762e4ba3f4cb8424483"},
    {file = "kiwisolver-1.4.7-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:22f499f6157236c19f4bbbd472fa55b063db77a16cd74d49afe28992dff8c258"},
    {file = "kiwisolver-1.4.7-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:693902d433cf585133699972b6d7c42a8b9f8f826ebcaf0132ff55200afc599e"},
    {file = "kiwisolver-1.4.7-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:4e77f2126c3e0b0d055f44513ed349038ac180371ed9b52fe96a32aa071a5107"},
    {file = "kiwisolver-1.4.7-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:657a05857bda581c3656bfc3b20e353c232e9193eb167766ad2dc58b56504948"},
    {file = "kiwisolver-1.4.7-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:4bfa75a048c056a411f9705856abfc872558e33c055d80af6a380e3658766038"},
    {file = "kiwisolver-1.4.7-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:34ea1de54beef1c104422d210c47c7d2a4999bdecf42c7b5718fbe59a4cac383"},
    {file = "kiwisolver-1.4.7-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:90da3b5f694b85231cf93586dad5e90e2d71b9428f9aad96952c99055582f520"},
    {file = "kiwisolver-1.4.7-cp312-cp312-win32.whl", hash = "sha256:18e0cca3e008e17fe9b164b55735a325140a5a35faad8de92dd80265cd5eb80b"},
    {file = "kiwisolver-1.4.7-cp312-cp312-win_amd64.whl", hash = "sha256:58cb20602b18f86f83a5c87d3ee1c766a79c0d452f8def86d925e6c60fbf7bfb"},
    {file = "kiwisolver-1.4.7-cp312-cp312-win_arm64.whl", hash = "sha256:f5a8b53bdc0b3961f8b6125e198617c40aeed638b387913bf1ce78afb1b0be2a"},
    {file = "kiwisolver-1.4.7-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:2e6039dcbe79a8e0f044f1c39db1986a1b8071051efba3ee4d74f5b365f5226e"},
    {file = "kiwisolver-1.4.7-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a1ecf0ac1c518487d9d23b1cd7139a6a65bc460cd101ab01f1be82ecf09794b6"},
    {file = "kiwisolver-1.4.7-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7ab9ccab2b5bd5702ab0803676a580fffa2aa178c2badc5557a84cc943fcf750"},
    {file = "kiwisolver-1.4.7-cp313-cp313-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f816dd2277f8d63d79f9c8473a79fe54047bc0467754962840782c575522224d"},
    {file = "kiwisolver-1.4.7-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cf8bcc23ceb5a1b624572a1623b9f79d2c3b337c8c455405ef231933a10da379"},
    {file = "kiwisolver-1.4.7-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dea0bf229319828467d7fca8c7c189780aa9ff679c94539eed7532ebe33ed37c"},
    {file = "kiwisolver-1.4.7-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7c06a4c7cf15ec739ce0e5971b26c93638730090add60e183530d70848ebdd34"},
    {file = "kiwisolver-1.4.7-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:913983ad2deb14e66d83c28b632fd35ba2b825031f2fa4ca29675e665dfecbe1"},
    {file = "kiwisolver-1.4.7-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5337ec7809bcd0f424c6b705ecf97941c46279cf5ed92311782c7c9c2026f07f"},
    {file = "kiwisolver-1.4.7-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:4c26ed10c4f6fa6ddb329a5120ba3b6db349ca192ae211e882970bfc9d91420b"},
    {file = "kiwisolver-1.4.7-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:c619b101e6de2222c1fcb0531e1b17bbffbe54294bfba43ea0d411d428618c27"},
    {file = "kiwisolver-1.4.7-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:073a36c8273647592ea332e816e75ef8da5c303236ec0167196793eb1e34657a"},
    {file = "kiwisolver-1.4.7-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:3ce6b2b0231bda412463e152fc18335ba32faf4e8c23a754ad50ffa70e4091ee"},
    {file = "kiwisolver-1.4.7-cp313-cp313-win32.whl", hash = "sha256:f4c9aee212bc89d4e13f58be11a56cc8036cabad119259d12ace14b34476fd07"},
    {file = "kiwisolver-1.4.7-cp313-cp313-win_amd64.whl", hash = "sha256:8a3ec5aa8e38fc4c8af308917ce12c536f1c88452ce554027e55b22cbbfbff76"},
    {file = "kiwisolver-1.4.7-cp313-cp313-win_arm64.whl", hash = "sha256:76c8094ac20ec259471ac53e774623eb62e6e1f56cd8690c67ce6ce4fcb05650"},
    {file = "kiwisolver-1.4.7-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:5d5abf8f8ec1f4e22882273c423e16cae834c36856cac348cfbfa68e01c40f3a"},
    {file = "kiwisolver-1.4.7-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:aeb3531b196ef6f11776c21674dba836aeea9d5bd1cf630f869e3d90b16cfade"},
    {file = "kiwisolver-1.4.7-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:b7d755065e4e866a8086c9bdada157133ff466476a2ad7861828e17b6026e22c"},
    {file = "kiwisolver-1.4.7-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:08471d4d86cbaec61f86b217dd938a83d85e03785f51121e791a6e6689a3be95"},
    {file = "kiwisolver-1.4.7-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7bbfcb7165ce3d54a3dfbe731e470f65739c4c1f85bb1018ee912bae139e263b"},
    {file = "kiwisolver-1.4.7-cp38-cp38-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5d34eb8494bea691a1a450141ebb5385e4b69d38bb8403b5146ad279f4b30fa3"},
    {file = "kiwisolver-1.4.7-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:9242795d174daa40105c1d86aba618e8eab7bf96ba8c3ee614da8302a9f95503"},
    {file = "kiwisolver-1.4.7-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:a0f64a48bb81af7450e641e3fe0b0394d7381e342805479178b3d335d60ca7cf"},
    {file = "kiwisolver-1.4.7-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:8e045731a5416357638d1700927529e2b8ab304811671f665b225f8bf8d8f933"},
    {file = "kiwisolver-1.4.7-cp38-cp38-musllinux_1_2_i686.whl", hash = "sha256:4322872d5772cae7369f8351da1edf255a604ea7087fe295411397d0cfd9655e"},
    {file = "kiwisolver-1.4.7-cp38-cp38-musllinux_1_2_ppc64le.whl", hash = "sha256:e1631290ee9271dffe3062d2634c3ecac02c83890ada077d225e081aca8aab89"},
    {file = "kiwisolver-1.4.7-cp38-cp38-musllinux_1_2_s390x.whl", hash = "sha256:edcfc407e4eb17e037bca59be0e85a2031a2ac87e4fed26d3e9df88b4165f92d"},
    {file = "kiwisolver-1.4.7-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:4d05d81ecb47d11e7f8932bd8b61b720bf0b41199358f3f5e36d38e28f0532c5"},
    {file = "kiwisolver-1.4.7-cp38-cp38-win32.whl", hash = "sha256:b38ac83d5f04b15e515fd86f312479d950d05ce2368d5413d46c088dda7de90a"},
    {file = "kiwisolver-1.4.7-cp38-cp38-win_amd64.whl", hash = "sha256:d83db7cde68459fc803052a55ace60bea2bae361fc3b7a6d5da07e11954e4b09"},
    {file = "kiwisolver-1.4.7-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:3f9362ecfca44c863569d3d3c033dbe8ba452ff8eed6f6b5806382741a1334bd"},
    {file = "kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:e8df2eb9b2bac43ef8b082e06f750350fbbaf2887534a5be97f6cf07b19d9583"},
    {file = "kiwisolver-1.4.7-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:f32d6edbc638cde7652bd690c3e728b25332acbadd7cad670cc4a02558d9c417"},
    {file = "kiwisolver-1.4.7-cp39-cp39-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:e2e6c39bd7b9372b0be21456caab138e8e69cc0fc1190a9dfa92bd45a1e6e904"},
    {file = "kiwisolver-1.4.7-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:dda56c24d869b1193fcc763f1284b9126550eaf84b88bbc7256e15028f19188a"},
    {file = "kiwisolver-1.4.7-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:79849239c39b5e1fd906556c474d9b0439ea6792b637511f3fe3a41158d89ca8"},
    {file = "kiwisolver-1.4.7-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5e3bc157fed2a4c02ec468de4ecd12a6e22818d4f09cde2c31ee3226ffbefab2"},
    {file = "kiwisolver-1.4.7-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3da53da805b71e41053dc670f9a820d1157aae77b6b944e08024d17bcd51ef88"},
    {file = "kiwisolver-1.4.7-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:8705f17dfeb43139a692298cb6637ee2e59c0194538153e83e9ee0c75c2eddde"},
    {file = "kiwisolver-1.4.7-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:82a5c2f4b87c26bb1a0ef3d16b5c4753434633b83d365cc0ddf2770c93829e3c"},
    {file = "kiwisolver-1.4.7-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:ce8be0466f4c0d585cdb6c1e2ed07232221df101a4c6f28821d2aa754ca2d9e2"},
    {file = "kiwisolver-1.4.7-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:409afdfe1e2e90e6ee7fc896f3df9a7fec8e793e58bfa0d052c8a82f99c37abb"},
    {file = "kiwisolver-1.4.7-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:5b9c3f4ee0b9a439d2415012bd1b1cc2df59e4d6a9939f4d669241d30b414327"},
    {file = "kiwisolver-1.4.7-cp39-cp39-win32.whl", hash = "sha256:a79ae34384df2b615eefca647a2873842ac3b596418032bef9a7283675962644"},
    {file = "kiwisolver-1.4.7-cp39-cp39-win_amd64.whl", hash = "sha256:cf0438b42121a66a3a667de17e779330fc0f20b0d97d59d2f2121e182b0505e4"},
    {file = "kiwisolver-1.4.7-cp39-cp39-win_arm64.whl", hash = "sha256:764202cc7e70f767dab49e8df52c7455e8de0df5d858fa801a11aa0d882ccf3f"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:94252291e3fe68001b1dd747b4c0b3be12582839b95ad4d1b641924d68fd4643"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5b7dfa3b546da08a9f622bb6becdb14b3e24aaa30adba66749d38f3cc7ea9706"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bd3de6481f4ed8b734da5df134cd5a6a64fe32124fe83dde1e5b5f29fe30b1e6"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a91b5f9f1205845d488c928e8570dcb62b893372f63b8b6e98b863ebd2368ff2"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:40fa14dbd66b8b8f470d5fc79c089a66185619d31645f9b0773b88b19f7223c4"},
    {file = "kiwisolver-1.4.7-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:eb542fe7933aa09d8d8f9d9097ef37532a7df6497819d16efe4359890a2f417a"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-macosx_10_9_x86_64.whl", hash = "sha256:bfa1acfa0c54932d5607e19a2c24646fb4c1ae2694437789129cf099789a3b00"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-macosx_11_0_arm64.whl", hash = "sha256:eee3ea935c3d227d49b4eb85660ff631556841f6e567f0f7bda972df6c2c9935"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-manylinux_2_12_i686.manylinux2010_i686.whl", hash = "sha256:f3160309af4396e0ed04db259c3ccbfdc3621b5559b5453075e5de555e1f3a1b"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:a17f6a29cf8935e587cc8a4dbfc8368c55edc645283db0ce9801016f83526c2d"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:10849fb2c1ecbfae45a693c070e0320a91b35dd4bcf58172c023b994283a124d"},
    {file = "kiwisolver-1.4.7-pp38-pypy38_pp73-win_amd64.whl", hash = "sha256:ac542bf38a8a4be2dc6b15248d36315ccc65f0743f7b1a76688ffb6b5129a5c2"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-macosx_10_15_x86_64.whl", hash = "sha256:8b01aac285f91ca889c800042c35ad3b239e704b150cfd3382adfc9dcc780e39"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-macosx_11_0_arm64.whl", hash = "sha256:48be928f59a1f5c8207154f935334d374e79f2b5d212826307d072595ad76a2e"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f37cfe618a117e50d8c240555331160d73d0411422b59b5ee217843d7b693608"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:599b5c873c63a1f6ed7eead644a8a380cfbdf5db91dcb6f85707aaab213b1674"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:801fa7802e5cfabe3ab0c81a34c323a319b097dfb5004be950482d882f3d7225"},
    {file = "kiwisolver-1.4.7-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:0c6c43471bc764fad4bc99c5c2d6d16a676b1abf844ca7c8702bdae92df01ee0"},
    {file = "kiwisolver-1.4.7.tar.gz", hash = "sha256:9893ff81bd7107f7b685d3017cc6583daadb4fc26e4a888350df530e41980a60"},
]

[[package]]
name = "matplotlib"
version = "3.9.2"
description = "Python plotting package"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "matplotlib-3.9.2-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:9d78bbc0cbc891ad55b4f39a48c22182e9bdaea7fc0e5dbd364f49f729ca1bbb"},
    {file = "matplotlib-3.9.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c375cc72229614632c87355366bdf2570c2dac01ac66b8ad048d2dabadf2d0d4"},
    {file = "matplotlib-3.9.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1d94ff717eb2bd0b58fe66380bd8b14ac35f48a98e7c6765117fe67fb7684e64"},
    {file = "matplotlib-3.9.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ab68d50c06938ef28681073327795c5db99bb4666214d2d5f880ed11aeaded66"},
    {file = "matplotlib-3.9.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:65aacf95b62272d568044531e41de26285d54aec8cb859031f511f84bd8b495a"},
    {file = "matplotlib-3.9.2-cp310-cp310-win_amd64.whl", hash = "sha256:3fd595f34aa8a55b7fc8bf9ebea8aa665a84c82d275190a61118d33fbc82ccae"},
    {file = "matplotlib-3.9.2-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:d8dd059447824eec055e829258ab092b56bb0579fc3164fa09c64f3acd478772"},
    {file = "matplotlib-3.9.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c797dac8bb9c7a3fd3382b16fe8f215b4cf0f22adccea36f1545a6d7be310b41"},
    {file = "matplotlib-3.9.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d719465db13267bcef19ea8954a971db03b9f48b4647e3860e4bc8e6ed86610f"},
    {file = "matplotlib-3.9.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8912ef7c2362f7193b5819d17dae8629b34a95c58603d781329712ada83f9447"},
    {file = "matplotlib-3.9.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:7741f26a58a240f43bee74965c4882b6c93df3e7eb3de160126d8c8f53a6ae6e"},
    {file = "matplotlib-3.9.2-cp311-cp311-win_amd64.whl", hash = "sha256:ae82a14dab96fbfad7965403c643cafe6515e386de723e498cf3eeb1e0b70cc7"},
    {file = "matplotlib-3.9.2-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:ac43031375a65c3196bee99f6001e7fa5bdfb00ddf43379d3c0609bdca042df9"},
    {file = "matplotlib-3.9.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:be0fc24a5e4531ae4d8e858a1a548c1fe33b176bb13eff7f9d0d38ce5112a27d"},
    {file = "matplotlib-3.9.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:bf81de2926c2db243c9b2cbc3917619a0fc85796c6ba4e58f541df814bbf83c7"},
    {file = "matplotlib-3.9.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f6ee45bc4245533111ced13f1f2cace1e7f89d1c793390392a80c139d6cf0e6c"},
    {file = "matplotlib-3.9.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:306c8dfc73239f0e72ac50e5a9cf19cc4e8e331dd0c54f5e69ca8758550f1e1e"},
    {file = "matplotlib-3.9.2-cp312-cp312-win_amd64.whl", hash = "sha256:5413401594cfaff0052f9d8b1aafc6d305b4bd7c4331dccd18f561ff7e1d3bd3"},
    {file = "matplotlib-3.9.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:18128cc08f0d3cfff10b76baa2f296fc28c4607368a8402de61bb3f2eb33c7d9"},
    {file = "matplotlib-3.9.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:4876d7d40219e8ae8bb70f9263bcbe5714415acfdf781086601211335e24f8aa"},
    {file = "matplotlib-3.9.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6d9f07a80deab4bb0b82858a9e9ad53d1382fd122be8cde11080f4e7dfedb38b"},
    {file = "matplotlib-3.9.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f7c0410f181a531ec4e93bbc27692f2c71a15c2da16766f5ba9761e7ae518413"},
    {file = "matplotlib-3.9.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:909645cce2dc28b735674ce0931a4ac94e12f5b13f6bb0b5a5e65e7cea2c192b"},
    {file = "matplotlib-3.9.2-cp313-cp313-win_amd64.whl", hash = "sha256:f32c7410c7f246838a77d6d1eff0c0f87f3cb0e7c4247aebea71a6d5a68cab49"},
    {file = "matplotlib-3.9.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:37e51dd1c2db16ede9cfd7b5cabdfc818b2c6397c83f8b10e0e797501c963a03"},
    {file = "matplotlib-3.9.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:b82c5045cebcecd8496a4d694d43f9cc84aeeb49fe2133e036b207abe73f4d30"},
    {file = "matplotlib-3.9.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f053c40f94bc51bc03832a41b4f153d83f2062d88c72b5e79997072594e97e51"},
    {file = "matplotlib-3.9.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dbe196377a8248972f5cede786d4c5508ed5f5ca4a1e09b44bda889958b33f8c"},
    {file = "matplotlib-3.9.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:5816b1e1fe8c192cbc013f8f3e3368ac56fbecf02fb41b8f8559303f24c5015e"},
    {file = "matplotlib-3.9.2-cp39-cp39-macosx_10_12_x86_64.whl", hash = "sha256:cef2a73d06601437be399908cf13aee74e86932a5ccc6ccdf173408ebc5f6bb2"},
    {file = "matplotlib-3.9.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:e0830e188029c14e891fadd99702fd90d317df294c3298aad682739c5533721a"},
    {file = "matplotlib-3.9.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:03ba9c1299c920964e8d3857ba27173b4dbb51ca4bab47ffc2c2ba0eb5e2cbc5"},
    {file = "matplotlib-3.9.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1cd93b91ab47a3616b4d3c42b52f8363b88ca021e340804c6ab2536344fad9ca"},
    {file = "matplotlib-3.9.2-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:6d1ce5ed2aefcdce11904fc5bbea7d9c21fff3d5f543841edf3dea84451a09ea"},
    {file = "matplotlib-3.9.2-cp39-cp39-win_amd64.whl", hash = "sha256:b2696efdc08648536efd4e1601b5fd491fd47f4db97a5fbfd175549a7365c1b2"},
    {file = "matplotlib-3.9.2-pp39-pypy39_pp73-macosx_10_15_x86_64.whl", hash = "sha256:d52a3b618cb1cbb769ce2ee1dcdb333c3ab6e823944e9a2d36e37253815f9556"},
    {file = "matplotlib-3.9.2-pp39-pypy39_pp73-macosx_11_0_arm64.whl", hash = "sha256:039082812cacd6c6bec8e17a9c1e6baca230d4116d522e81e1f63a74d01d2e21"},
    {file = "matplotlib-3.9.2-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6758baae2ed64f2331d4fd19be38b7b4eae3ecec210049a26b6a4f3ae1c85dcc"},
    {file = "matplotlib-3.9.2-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:050598c2b29e0b9832cde72bcf97627bf00262adbc4a54e2b856426bb2ef0697"},
    {file = "matplotlib-3.9.2.tar.gz", hash = "sha256:96ab43906269ca64a6366934106fa01534454a69e471b7bf3d79083981aaab92"},
]

[package.dependencies]
contourpy = ">=1.0.1"
cycler = ">=0.10"
fonttools = ">=4.22.0"
kiwisolver = ">=1.3.1"
numpy = ">=1.23"
packaging = ">=20.0"
pillow = ">=8"
pyparsing = ">=2.3.1"
python-dateutil = ">=2.7"

[package.extras]
dev = ["meson-python (>=0.13.1)", "numpy (>=1.25)", "pybind11 (>=2.6)", "setuptools (>=64)", "setuptools_scm (>=7)"]

[[package]]
name = "matplotlib-inline"
version = "0.1.6"
description = "Inline Matplotlib backend for Jupyter"
optional = false
python-versions = ">=3.5"
groups = ["dev"]
files = [
    {file = "matplotlib-inline-0.1.6.tar.gz", hash = "sha256:f887e5f10ba98e8d2b150ddcf4702c1e5f8b3a20005eb0f74bfdbd360ee6f304"},
    {file = "matplotlib_inline-0.1.6-py3-none-any.whl", hash = "sha256:f1f41aab5328aa5aaea9b16d083b128102f8712542f819fe7e6a420ff581b311"},
]

[package.dependencies]
traitlets = "*"

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mock"
version = "5.1.0"
description = "Rolling backport of unittest.mock for all Pythons"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "mock-5.1.0-py3-none-any.whl", hash = "sha256:18c694e5ae8a208cdb3d2c20a993ca1a7b0efa258c247a1e565150f477f83744"},
    {file = "mock-5.1.0.tar.gz", hash = "sha256:5e96aad5ccda4718e0a229ed94b2024df75cc2d55575ba5762d31f5767b8767d"},
]

[package.extras]
build = ["blurb", "twine", "wheel"]
docs = ["sphinx"]
test = ["pytest", "pytest-cov"]

[[package]]
name = "mypy-extensions"
version = "1.0.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.5"
groups = ["dev"]
files = [
    {file = "mypy_extensions-1.0.0-py3-none-any.whl", hash = "sha256:4392f6c0eb8a5668a69e23d168ffa70f0be9ccfd32b5cc2d26a34ae5b844552d"},
    {file = "mypy_extensions-1.0.0.tar.gz", hash = "sha256:75dbf8955dc00442a438fc4d0666508a9a97b6bd41aa2f0ffe9d2f2725af0782"},
]

[[package]]
name = "ni-python-styleguide"
version = "0.4.6"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.7"
groups = ["dev"]
files = [
    {file = "ni_python_styleguide-0.4.6-py3-none-any.whl", hash = "sha256:0ffa8bd5de38d96779ad0e83e49a3db3620a31742247be10f6471961ab6fa246"},
    {file = "ni_python_styleguide-0.4.6.tar.gz", hash = "sha256:26d7ebd5acce0b29a6209ef9950f369327cbfd7ffd8404ade3e9a7c0f0aa6bcb"},
]

[package.dependencies]
black = ">=23.1"
click = ">=7.1.2"
flake8 = [
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.7\" and python_version < \"3.12\""},
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.7\" and python_version < \"3.12\""},
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
]
toml = ">=0.10.1"

[[package]]
name = "nidaqmx"
version = "0.9.0"
description = "NI-DAQmx Python API"
optional = false
python-versions = ">=3.8,<4.0"
groups = ["main"]
files = [
    {file = "nidaqmx-0.9.0-py3-none-any.whl", hash = "sha256:8f79c4929f19f8dca3c19d517ccb7f9a76850e4c80a78ac2a9e7f5f5743cc700"},
    {file = "nidaqmx-0.9.0.tar.gz", hash = "sha256:08e3f5f3369fb71116df8fb1e5577ecbbda1530058b16bf4b8be3145c2ffcd96"},
]

[package.dependencies]
deprecation = ">=2.1"
hightime = ">=0.2.1,<0.3.0"
numpy = [
    {version = ">=1.22", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
    {version = ">=1.26", markers = "python_version == \"3.12\""},
]

[package.extras]
docs = ["Sphinx (>=4.3,<5.0)", "sphinx_rtd_theme (>=1.0,<2.0)"]
grpc = ["grpcio (>=1.49.0,<2.0)", "protobuf (>=4.21,<5.0)"]

[[package]]
name = "nidcpower"
version = "1.5.0"
description = "NI-DCPower Python API"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "nidcpower-1.5.0-py3-none-any.whl", hash = "sha256:04e42b5af98dd5df1eccd4859a039cfaa541719b5532d395e922cf60833b8c53"},
    {file = "nidcpower-1.5.0.tar.gz", hash = "sha256:fd09a3fa118ea44dfc0e6f91995fc0ab0a24d724b5e93ddb93d723a248d62246"},
]

[package.dependencies]
hightime = ">=0.2.0"

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "nidmm"
version = "1.4.7"
description = "NI-DMM Python API"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "nidmm-1.4.7-py3-none-any.whl", hash = "sha256:b6616977647dff55b93a1087355a1775fbd4b085716d6e51b65cc91ca41a7ccb"},
    {file = "nidmm-1.4.7.tar.gz", hash = "sha256:9b688403d3b74304d666ba5123a9bd0cd76bf18e9b5eae210baec2b91d8fcaa7"},
]

[package.dependencies]
hightime = ">=0.2.0"

[package.extras]
grpc = ["grpcio (>=1.49.1,<2.0)", "protobuf (>=4.21,<5.0)"]

[[package]]
name = "niswitch"
version = "1.4.7"
description = "NI-SWITCH Python API"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "niswitch-1.4.7-py3-none-any.whl", hash = "sha256:6bb2e24d1358c0a852e38976ae2040bda7d24de516dab50b217961aeb6ec8440"},
    {file = "niswitch-1.4.7.tar.gz", hash = "sha256:9d82e28f6f3c5c5e1e032c3bd31bc9e0f58630368c671b6a021b672c5cbe19bc"},
]

[package.dependencies]
hightime = ">=0.2.0"

[package.extras]
grpc = ["grpcio (>=1.49.1,<2.0)", "protobuf (>=4.21,<5.0)"]

[[package]]
name = "numpy"
version = "1.26.4"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "numpy-1.26.4-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:9ff0f4f29c51e2803569d7a51c2304de5554655a60c5d776e35b4a41413830d0"},
    {file = "numpy-1.26.4-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2e4ee3380d6de9c9ec04745830fd9e2eccb3e6cf790d39d7b98ffd19b0dd754a"},
    {file = "numpy-1.26.4-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d209d8969599b27ad20994c8e41936ee0964e6da07478d6c35016bc386b66ad4"},
    {file = "numpy-1.26.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ffa75af20b44f8dba823498024771d5ac50620e6915abac414251bd971b4529f"},
    {file = "numpy-1.26.4-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:62b8e4b1e28009ef2846b4c7852046736bab361f7aeadeb6a5b89ebec3c7055a"},
    {file = "numpy-1.26.4-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:a4abb4f9001ad2858e7ac189089c42178fcce737e4169dc61321660f1a96c7d2"},
    {file = "numpy-1.26.4-cp310-cp310-win32.whl", hash = "sha256:bfe25acf8b437eb2a8b2d49d443800a5f18508cd811fea3181723922a8a82b07"},
    {file = "numpy-1.26.4-cp310-cp310-win_amd64.whl", hash = "sha256:b97fe8060236edf3662adfc2c633f56a08ae30560c56310562cb4f95500022d5"},
    {file = "numpy-1.26.4-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:4c66707fabe114439db9068ee468c26bbdf909cac0fb58686a42a24de1760c71"},
    {file = "numpy-1.26.4-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:edd8b5fe47dab091176d21bb6de568acdd906d1887a4584a15a9a96a1dca06ef"},
    {file = "numpy-1.26.4-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7ab55401287bfec946ced39700c053796e7cc0e3acbef09993a9ad2adba6ca6e"},
    {file = "numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:666dbfb6ec68962c033a450943ded891bed2d54e6755e35e5835d63f4f6931d5"},
    {file = "numpy-1.26.4-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:96ff0b2ad353d8f990b63294c8986f1ec3cb19d749234014f4e7eb0112ceba5a"},
    {file = "numpy-1.26.4-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:60dedbb91afcbfdc9bc0b1f3f402804070deed7392c23eb7a7f07fa857868e8a"},
    {file = "numpy-1.26.4-cp311-cp311-win32.whl", hash = "sha256:1af303d6b2210eb850fcf03064d364652b7120803a0b872f5211f5234b399f20"},
    {file = "numpy-1.26.4-cp311-cp311-win_amd64.whl", hash = "sha256:cd25bcecc4974d09257ffcd1f098ee778f7834c3ad767fe5db785be9a4aa9cb2"},
    {file = "numpy-1.26.4-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:b3ce300f3644fb06443ee2222c2201dd3a89ea6040541412b8fa189341847218"},
    {file = "numpy-1.26.4-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:03a8c78d01d9781b28a6989f6fa1bb2c4f2d51201cf99d3dd875df6fbd96b23b"},
    {file = "numpy-1.26.4-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9fad7dcb1aac3c7f0584a5a8133e3a43eeb2fe127f47e3632d43d677c66c102b"},
    {file = "numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed"},
    {file = "numpy-1.26.4-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:ab47dbe5cc8210f55aa58e4805fe224dac469cde56b9f731a4c098b91917159a"},
    {file = "numpy-1.26.4-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:1dda2e7b4ec9dd512f84935c5f126c8bd8b9f2fc001e9f54af255e8c5f16b0e0"},
    {file = "numpy-1.26.4-cp312-cp312-win32.whl", hash = "sha256:50193e430acfc1346175fcbdaa28ffec49947a06918b7b92130744e81e640110"},
    {file = "numpy-1.26.4-cp312-cp312-win_amd64.whl", hash = "sha256:08beddf13648eb95f8d867350f6a018a4be2e5ad54c8d8caed89ebca558b2818"},
    {file = "numpy-1.26.4-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:7349ab0fa0c429c82442a27a9673fc802ffdb7c7775fad780226cb234965e53c"},
    {file = "numpy-1.26.4-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:52b8b60467cd7dd1e9ed082188b4e6bb35aa5cdd01777621a1658910745b90be"},
    {file = "numpy-1.26.4-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d5241e0a80d808d70546c697135da2c613f30e28251ff8307eb72ba696945764"},
    {file = "numpy-1.26.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f870204a840a60da0b12273ef34f7051e98c3b5961b61b0c2c1be6dfd64fbcd3"},
    {file = "numpy-1.26.4-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:679b0076f67ecc0138fd2ede3a8fd196dddc2ad3254069bcb9faf9a79b1cebcd"},
    {file = "numpy-1.26.4-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:47711010ad8555514b434df65f7d7b076bb8261df1ca9bb78f53d3b2db02e95c"},
    {file = "numpy-1.26.4-cp39-cp39-win32.whl", hash = "sha256:a354325ee03388678242a4d7ebcd08b5c727033fcff3b2f536aea978e15ee9e6"},
    {file = "numpy-1.26.4-cp39-cp39-win_amd64.whl", hash = "sha256:3373d5d70a5fe74a2c1bb6d2cfd9609ecf686d47a2d7b1d37a8f3b6bf6003aea"},
    {file = "numpy-1.26.4-pp39-pypy39_pp73-macosx_10_9_x86_64.whl", hash = "sha256:afedb719a9dcfc7eaf2287b839d8198e06dcd4cb5d276a3df279231138e83d30"},
    {file = "numpy-1.26.4-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:95a7476c59002f2f6c590b9b7b998306fba6a5aa646b1e22ddfeaf8f78c3a29c"},
    {file = "numpy-1.26.4-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:7e50d0a0cc3189f9cb0aeb3a6a6af18c16f59f004b866cd2be1c14b36134a4a0"},
    {file = "numpy-1.26.4.tar.gz", hash = "sha256:2a02aba9ed12e4ac4eb3ea9421c420301a0c6460d9830d74a9df87efa4912010"},
]

[[package]]
name = "packaging"
version = "23.2"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.7"
groups = ["main", "dev"]
files = [
    {file = "packaging-23.2-py3-none-any.whl", hash = "sha256:8c491190033a9af7e1d931d0b5dacc2ef47509b34dd0de67ed209b5203fc88c7"},
    {file = "packaging-23.2.tar.gz", hash = "sha256:048fb0e9405036518eaaf48a55953c750c11e1a1b68e0dd1a9d62ed0c092cfc5"},
]

[[package]]
name = "pandas"
version = "2.2.2"
description = "Powerful data structures for data analysis, time series, and statistics"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pandas-2.2.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:90c6fca2acf139569e74e8781709dccb6fe25940488755716d1d354d6bc58bce"},
    {file = "pandas-2.2.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c7adfc142dac335d8c1e0dcbd37eb8617eac386596eb9e1a1b77791cf2498238"},
    {file = "pandas-2.2.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4abfe0be0d7221be4f12552995e58723c7422c80a659da13ca382697de830c08"},
    {file = "pandas-2.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8635c16bf3d99040fdf3ca3db669a7250ddf49c55dc4aa8fe0ae0fa8d6dcc1f0"},
    {file = "pandas-2.2.2-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:40ae1dffb3967a52203105a077415a86044a2bea011b5f321c6aa64b379a3f51"},
    {file = "pandas-2.2.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:8e5a0b00e1e56a842f922e7fae8ae4077aee4af0acb5ae3622bd4b4c30aedf99"},
    {file = "pandas-2.2.2-cp310-cp310-win_amd64.whl", hash = "sha256:ddf818e4e6c7c6f4f7c8a12709696d193976b591cc7dc50588d3d1a6b5dc8772"},
    {file = "pandas-2.2.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:696039430f7a562b74fa45f540aca068ea85fa34c244d0deee539cb6d70aa288"},
    {file = "pandas-2.2.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8e90497254aacacbc4ea6ae5e7a8cd75629d6ad2b30025a4a8b09aa4faf55151"},
    {file = "pandas-2.2.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:58b84b91b0b9f4bafac2a0ac55002280c094dfc6402402332c0913a59654ab2b"},
    {file = "pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6d2123dc9ad6a814bcdea0f099885276b31b24f7edf40f6cdbc0912672e22eee"},
    {file = "pandas-2.2.2-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:2925720037f06e89af896c70bca73459d7e6a4be96f9de79e2d440bd499fe0db"},
    {file = "pandas-2.2.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:0cace394b6ea70c01ca1595f839cf193df35d1575986e484ad35c4aeae7266c1"},
    {file = "pandas-2.2.2-cp311-cp311-win_amd64.whl", hash = "sha256:873d13d177501a28b2756375d59816c365e42ed8417b41665f346289adc68d24"},
    {file = "pandas-2.2.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:9dfde2a0ddef507a631dc9dc4af6a9489d5e2e740e226ad426a05cabfbd7c8ef"},
    {file = "pandas-2.2.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:e9b79011ff7a0f4b1d6da6a61aa1aa604fb312d6647de5bad20013682d1429ce"},
    {file = "pandas-2.2.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1cb51fe389360f3b5a4d57dbd2848a5f033350336ca3b340d1c53a1fad33bcad"},
    {file = "pandas-2.2.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eee3a87076c0756de40b05c5e9a6069c035ba43e8dd71c379e68cab2c20f16ad"},
    {file = "pandas-2.2.2-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:3e374f59e440d4ab45ca2fffde54b81ac3834cf5ae2cdfa69c90bc03bde04d76"},
    {file = "pandas-2.2.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:43498c0bdb43d55cb162cdc8c06fac328ccb5d2eabe3cadeb3529ae6f0517c32"},
    {file = "pandas-2.2.2-cp312-cp312-win_amd64.whl", hash = "sha256:d187d355ecec3629624fccb01d104da7d7f391db0311145817525281e2804d23"},
    {file = "pandas-2.2.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:0ca6377b8fca51815f382bd0b697a0814c8bda55115678cbc94c30aacbb6eff2"},
    {file = "pandas-2.2.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:9057e6aa78a584bc93a13f0a9bf7e753a5e9770a30b4d758b8d5f2a62a9433cd"},
    {file = "pandas-2.2.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:001910ad31abc7bf06f49dcc903755d2f7f3a9186c0c040b827e522e9cef0863"},
    {file = "pandas-2.2.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:66b479b0bd07204e37583c191535505410daa8df638fd8e75ae1b383851fe921"},
    {file = "pandas-2.2.2-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:a77e9d1c386196879aa5eb712e77461aaee433e54c68cf253053a73b7e49c33a"},
    {file = "pandas-2.2.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:92fd6b027924a7e178ac202cfbe25e53368db90d56872d20ffae94b96c7acc57"},
    {file = "pandas-2.2.2-cp39-cp39-win_amd64.whl", hash = "sha256:640cef9aa381b60e296db324337a554aeeb883ead99dc8f6c18e81a93942f5f4"},
    {file = "pandas-2.2.2.tar.gz", hash = "sha256:9e79019aba43cb4fda9e4d983f8e88ca0373adbb697ae9c6c43093218de28b54"},
]

[package.dependencies]
numpy = [
    {version = ">=1.22.4", markers = "python_version < \"3.11\""},
    {version = ">=1.23.2", markers = "python_version == \"3.11\""},
    {version = ">=1.26.0", markers = "python_version >= \"3.12\""},
]
python-dateutil = ">=2.8.2"
pytz = ">=2020.1"
tzdata = ">=2022.7"

[package.extras]
all = ["PyQt5 (>=5.15.9)", "SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "adbc-driver-sqlite (>=0.8.0)", "beautifulsoup4 (>=4.11.2)", "bottleneck (>=1.3.6)", "dataframe-api-compat (>=0.1.7)", "fastparquet (>=2022.12.0)", "fsspec (>=2022.11.0)", "gcsfs (>=2022.11.0)", "html5lib (>=1.1)", "hypothesis (>=6.46.1)", "jinja2 (>=3.1.2)", "lxml (>=4.9.2)", "matplotlib (>=3.6.3)", "numba (>=0.56.4)", "numexpr (>=2.8.4)", "odfpy (>=1.4.1)", "openpyxl (>=3.1.0)", "pandas-gbq (>=0.19.0)", "psycopg2 (>=2.9.6)", "pyarrow (>=10.0.1)", "pymysql (>=1.0.2)", "pyreadstat (>=1.2.0)", "pytest (>=7.3.2)", "pytest-xdist (>=2.2.0)", "python-calamine (>=0.1.7)", "pyxlsb (>=1.0.10)", "qtpy (>=2.3.0)", "s3fs (>=2022.11.0)", "scipy (>=1.10.0)", "tables (>=3.8.0)", "tabulate (>=0.9.0)", "xarray (>=2022.12.0)", "xlrd (>=2.0.1)", "xlsxwriter (>=3.0.5)", "zstandard (>=0.19.0)"]
aws = ["s3fs (>=2022.11.0)"]
clipboard = ["PyQt5 (>=5.15.9)", "qtpy (>=2.3.0)"]
compression = ["zstandard (>=0.19.0)"]
computation = ["scipy (>=1.10.0)", "xarray (>=2022.12.0)"]
consortium-standard = ["dataframe-api-compat (>=0.1.7)"]
excel = ["odfpy (>=1.4.1)", "openpyxl (>=3.1.0)", "python-calamine (>=0.1.7)", "pyxlsb (>=1.0.10)", "xlrd (>=2.0.1)", "xlsxwriter (>=3.0.5)"]
feather = ["pyarrow (>=10.0.1)"]
fss = ["fsspec (>=2022.11.0)"]
gcp = ["gcsfs (>=2022.11.0)", "pandas-gbq (>=0.19.0)"]
hdf5 = ["tables (>=3.8.0)"]
html = ["beautifulsoup4 (>=4.11.2)", "html5lib (>=1.1)", "lxml (>=4.9.2)"]
mysql = ["SQLAlchemy (>=2.0.0)", "pymysql (>=1.0.2)"]
output-formatting = ["jinja2 (>=3.1.2)", "tabulate (>=0.9.0)"]
parquet = ["pyarrow (>=10.0.1)"]
performance = ["bottleneck (>=1.3.6)", "numba (>=0.56.4)", "numexpr (>=2.8.4)"]
plot = ["matplotlib (>=3.6.3)"]
postgresql = ["SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "psycopg2 (>=2.9.6)"]
pyarrow = ["pyarrow (>=10.0.1)"]
spss = ["pyreadstat (>=1.2.0)"]
sql-other = ["SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "adbc-driver-sqlite (>=0.8.0)"]
test = ["hypothesis (>=6.46.1)", "pytest (>=7.3.2)", "pytest-xdist (>=2.2.0)"]
xml = ["lxml (>=4.9.2)"]

[[package]]
name = "parameterized"
version = "0.8.1"
description = "Parameterized testing with any Python test framework"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "parameterized-0.8.1-py2.py3-none-any.whl", hash = "sha256:9cbb0b69a03e8695d68b3399a8a5825200976536fe1cb79db60ed6a4c8c9efe9"},
    {file = "parameterized-0.8.1.tar.gz", hash = "sha256:41bbff37d6186430f77f900d777e5bb6a24928a1c46fb1de692f8b52b8833b5c"},
]

[package.extras]
dev = ["jinja2"]

[[package]]
name = "parso"
version = "0.8.3"
description = "A Python Parser"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "parso-0.8.3-py2.py3-none-any.whl", hash = "sha256:c001d4636cd3aecdaf33cbb40aebb59b094be2a74c556778ef5576c175e19e75"},
    {file = "parso-0.8.3.tar.gz", hash = "sha256:8c07be290bb59f03588915921e29e8a50002acaf2cdc5fa0e0114f91709fafa0"},
]

[package.extras]
qa = ["flake8 (==3.8.3)", "mypy (==0.782)"]
testing = ["docopt", "pytest (<6.0.0)"]

[[package]]
name = "pathspec"
version = "0.12.1"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pathspec-0.12.1-py3-none-any.whl", hash = "sha256:a0d503e138a4c123b27490a4f7beda6a01c6f288df0e4a8b79c7eb0dc7b4cc08"},
    {file = "pathspec-0.12.1.tar.gz", hash = "sha256:a482d51503a1ab33b1c67a6c3813a26953dbdc71c31dacaef9a838c4e29f5712"},
]

[[package]]
name = "pep8-naming"
version = "0.14.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pep8-naming-0.14.1.tar.gz", hash = "sha256:1ef228ae80875557eb6c1549deafed4dabbf3261cfcafa12f773fe0db9be8a36"},
    {file = "pep8_naming-0.14.1-py3-none-any.whl", hash = "sha256:63f514fc777d715f935faf185dedd679ab99526a7f2f503abb61587877f7b1c5"},
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
markers = "sys_platform != \"win32\""
files = [
    {file = "pexpect-4.9.0-py2.py3-none-any.whl", hash = "sha256:7236d1e080e4936be2dc3e326cec0af72acf9212a7e1d060210e70a47e253523"},
    {file = "pexpect-4.9.0.tar.gz", hash = "sha256:ee7d41123f3c9911050ea2c2dac107568dc43b2d3b0c7557a33212c398ead30f"},
]

[package.dependencies]
ptyprocess = ">=0.5"

[[package]]
name = "pillow"
version = "11.0.0"
description = "Python Imaging Library (Fork)"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pillow-11.0.0-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:6619654954dc4936fcff82db8eb6401d3159ec6be81e33c6000dfd76ae189947"},
    {file = "pillow-11.0.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:b3c5ac4bed7519088103d9450a1107f76308ecf91d6dabc8a33a2fcfb18d0fba"},
    {file = "pillow-11.0.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a65149d8ada1055029fcb665452b2814fe7d7082fcb0c5bed6db851cb69b2086"},
    {file = "pillow-11.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:88a58d8ac0cc0e7f3a014509f0455248a76629ca9b604eca7dc5927cc593c5e9"},
    {file = "pillow-11.0.0-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:c26845094b1af3c91852745ae78e3ea47abf3dbcd1cf962f16b9a5fbe3ee8488"},
    {file = "pillow-11.0.0-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:1a61b54f87ab5786b8479f81c4b11f4d61702830354520837f8cc791ebba0f5f"},
    {file = "pillow-11.0.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:674629ff60030d144b7bca2b8330225a9b11c482ed408813924619c6f302fdbb"},
    {file = "pillow-11.0.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:598b4e238f13276e0008299bd2482003f48158e2b11826862b1eb2ad7c768b97"},
    {file = "pillow-11.0.0-cp310-cp310-win32.whl", hash = "sha256:9a0f748eaa434a41fccf8e1ee7a3eed68af1b690e75328fd7a60af123c193b50"},
    {file = "pillow-11.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:a5629742881bcbc1f42e840af185fd4d83a5edeb96475a575f4da50d6ede337c"},
    {file = "pillow-11.0.0-cp310-cp310-win_arm64.whl", hash = "sha256:ee217c198f2e41f184f3869f3e485557296d505b5195c513b2bfe0062dc537f1"},
    {file = "pillow-11.0.0-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:1c1d72714f429a521d8d2d018badc42414c3077eb187a59579f28e4270b4b0fc"},
    {file = "pillow-11.0.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:499c3a1b0d6fc8213519e193796eb1a86a1be4b1877d678b30f83fd979811d1a"},
    {file = "pillow-11.0.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c8b2351c85d855293a299038e1f89db92a2f35e8d2f783489c6f0b2b5f3fe8a3"},
    {file = "pillow-11.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6f4dba50cfa56f910241eb7f883c20f1e7b1d8f7d91c750cd0b318bad443f4d5"},
    {file = "pillow-11.0.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:5ddbfd761ee00c12ee1be86c9c0683ecf5bb14c9772ddbd782085779a63dd55b"},
    {file = "pillow-11.0.0-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:45c566eb10b8967d71bf1ab8e4a525e5a93519e29ea071459ce517f6b903d7fa"},
    {file = "pillow-11.0.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:b4fd7bd29610a83a8c9b564d457cf5bd92b4e11e79a4ee4716a63c959699b306"},
    {file = "pillow-11.0.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:cb929ca942d0ec4fac404cbf520ee6cac37bf35be479b970c4ffadf2b6a1cad9"},
    {file = "pillow-11.0.0-cp311-cp311-win32.whl", hash = "sha256:006bcdd307cc47ba43e924099a038cbf9591062e6c50e570819743f5607404f5"},
    {file = "pillow-11.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:52a2d8323a465f84faaba5236567d212c3668f2ab53e1c74c15583cf507a0291"},
    {file = "pillow-11.0.0-cp311-cp311-win_arm64.whl", hash = "sha256:16095692a253047fe3ec028e951fa4221a1f3ed3d80c397e83541a3037ff67c9"},
    {file = "pillow-11.0.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d2c0a187a92a1cb5ef2c8ed5412dd8d4334272617f532d4ad4de31e0495bd923"},
    {file = "pillow-11.0.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:084a07ef0821cfe4858fe86652fffac8e187b6ae677e9906e192aafcc1b69903"},
    {file = "pillow-11.0.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8069c5179902dcdce0be9bfc8235347fdbac249d23bd90514b7a47a72d9fecf4"},
    {file = "pillow-11.0.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f02541ef64077f22bf4924f225c0fd1248c168f86e4b7abdedd87d6ebaceab0f"},
    {file = "pillow-11.0.0-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:fcb4621042ac4b7865c179bb972ed0da0218a076dc1820ffc48b1d74c1e37fe9"},
    {file = "pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:00177a63030d612148e659b55ba99527803288cea7c75fb05766ab7981a8c1b7"},
    {file = "pillow-11.0.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8853a3bf12afddfdf15f57c4b02d7ded92c7a75a5d7331d19f4f9572a89c17e6"},
    {file = "pillow-11.0.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:3107c66e43bda25359d5ef446f59c497de2b5ed4c7fdba0894f8d6cf3822dafc"},
    {file = "pillow-11.0.0-cp312-cp312-win32.whl", hash = "sha256:86510e3f5eca0ab87429dd77fafc04693195eec7fd6a137c389c3eeb4cfb77c6"},
    {file = "pillow-11.0.0-cp312-cp312-win_amd64.whl", hash = "sha256:8ec4a89295cd6cd4d1058a5e6aec6bf51e0eaaf9714774e1bfac7cfc9051db47"},
    {file = "pillow-11.0.0-cp312-cp312-win_arm64.whl", hash = "sha256:27a7860107500d813fcd203b4ea19b04babe79448268403172782754870dac25"},
    {file = "pillow-11.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:bcd1fb5bb7b07f64c15618c89efcc2cfa3e95f0e3bcdbaf4642509de1942a699"},
    {file = "pillow-11.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:0e038b0745997c7dcaae350d35859c9715c71e92ffb7e0f4a8e8a16732150f38"},
    {file = "pillow-11.0.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0ae08bd8ffc41aebf578c2af2f9d8749d91f448b3bfd41d7d9ff573d74f2a6b2"},
    {file = "pillow-11.0.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d69bfd8ec3219ae71bcde1f942b728903cad25fafe3100ba2258b973bd2bc1b2"},
    {file = "pillow-11.0.0-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:61b887f9ddba63ddf62fd02a3ba7add935d053b6dd7d58998c630e6dbade8527"},
    {file = "pillow-11.0.0-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:c6a660307ca9d4867caa8d9ca2c2658ab685de83792d1876274991adec7b93fa"},
    {file = "pillow-11.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:73e3a0200cdda995c7e43dd47436c1548f87a30bb27fb871f352a22ab8dcf45f"},
    {file = "pillow-11.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:fba162b8872d30fea8c52b258a542c5dfd7b235fb5cb352240c8d63b414013eb"},
    {file = "pillow-11.0.0-cp313-cp313-win32.whl", hash = "sha256:f1b82c27e89fffc6da125d5eb0ca6e68017faf5efc078128cfaa42cf5cb38798"},
    {file = "pillow-11.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:8ba470552b48e5835f1d23ecb936bb7f71d206f9dfeee64245f30c3270b994de"},
    {file = "pillow-11.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:846e193e103b41e984ac921b335df59195356ce3f71dcfd155aa79c603873b84"},
    {file = "pillow-11.0.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:4ad70c4214f67d7466bea6a08061eba35c01b1b89eaa098040a35272a8efb22b"},
    {file = "pillow-11.0.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:6ec0d5af64f2e3d64a165f490d96368bb5dea8b8f9ad04487f9ab60dc4bb6003"},
    {file = "pillow-11.0.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c809a70e43c7977c4a42aefd62f0131823ebf7dd73556fa5d5950f5b354087e2"},
    {file = "pillow-11.0.0-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:4b60c9520f7207aaf2e1d94de026682fc227806c6e1f55bba7606d1c94dd623a"},
    {file = "pillow-11.0.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:1e2688958a840c822279fda0086fec1fdab2f95bf2b717b66871c4ad9859d7e8"},
    {file = "pillow-11.0.0-cp313-cp313t-win32.whl", hash = "sha256:607bbe123c74e272e381a8d1957083a9463401f7bd01287f50521ecb05a313f8"},
    {file = "pillow-11.0.0-cp313-cp313t-win_amd64.whl", hash = "sha256:5c39ed17edea3bc69c743a8dd3e9853b7509625c2462532e62baa0732163a904"},
    {file = "pillow-11.0.0-cp313-cp313t-win_arm64.whl", hash = "sha256:75acbbeb05b86bc53cbe7b7e6fe00fbcf82ad7c684b3ad82e3d711da9ba287d3"},
    {file = "pillow-11.0.0-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:2e46773dc9f35a1dd28bd6981332fd7f27bec001a918a72a79b4133cf5291dba"},
    {file = "pillow-11.0.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:2679d2258b7f1192b378e2893a8a0a0ca472234d4c2c0e6bdd3380e8dfa21b6a"},
    {file = "pillow-11.0.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:eda2616eb2313cbb3eebbe51f19362eb434b18e3bb599466a1ffa76a033fb916"},
    {file = "pillow-11.0.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:20ec184af98a121fb2da42642dea8a29ec80fc3efbaefb86d8fdd2606619045d"},
    {file = "pillow-11.0.0-cp39-cp39-manylinux_2_28_aarch64.whl", hash = "sha256:8594f42df584e5b4bb9281799698403f7af489fba84c34d53d1c4bfb71b7c4e7"},
    {file = "pillow-11.0.0-cp39-cp39-manylinux_2_28_x86_64.whl", hash = "sha256:c12b5ae868897c7338519c03049a806af85b9b8c237b7d675b8c5e089e4a618e"},
    {file = "pillow-11.0.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:70fbbdacd1d271b77b7721fe3cdd2d537bbbd75d29e6300c672ec6bb38d9672f"},
    {file = "pillow-11.0.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:5178952973e588b3f1360868847334e9e3bf49d19e169bbbdfaf8398002419ae"},
    {file = "pillow-11.0.0-cp39-cp39-win32.whl", hash = "sha256:8c676b587da5673d3c75bd67dd2a8cdfeb282ca38a30f37950511766b26858c4"},
    {file = "pillow-11.0.0-cp39-cp39-win_amd64.whl", hash = "sha256:94f3e1780abb45062287b4614a5bc0874519c86a777d4a7ad34978e86428b8dd"},
    {file = "pillow-11.0.0-cp39-cp39-win_arm64.whl", hash = "sha256:290f2cc809f9da7d6d622550bbf4c1e57518212da51b6a30fe8e0a270a5b78bd"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:1187739620f2b365de756ce086fdb3604573337cc28a0d3ac4a01ab6b2d2a6d2"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:fbbcb7b57dc9c794843e3d1258c0fbf0f48656d46ffe9e09b63bbd6e8cd5d0a2"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5d203af30149ae339ad1b4f710d9844ed8796e97fda23ffbc4cc472968a47d0b"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:21a0d3b115009ebb8ac3d2ebec5c2982cc693da935f4ab7bb5c8ebe2f47d36f2"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-manylinux_2_28_aarch64.whl", hash = "sha256:73853108f56df97baf2bb8b522f3578221e56f646ba345a372c78326710d3830"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:e58876c91f97b0952eb766123bfef372792ab3f4e3e1f1a2267834c2ab131734"},
    {file = "pillow-11.0.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:224aaa38177597bb179f3ec87eeefcce8e4f85e608025e9cfac60de237ba6316"},
    {file = "pillow-11.0.0-pp39-pypy39_pp73-macosx_11_0_arm64.whl", hash = "sha256:5bd2d3bdb846d757055910f0a59792d33b555800813c3b39ada1829c372ccb06"},
    {file = "pillow-11.0.0-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:375b8dd15a1f5d2feafff536d47e22f69625c1aa92f12b339ec0b2ca40263273"},
    {file = "pillow-11.0.0-pp39-pypy39_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:daffdf51ee5db69a82dd127eabecce20729e21f7a3680cf7cbb23f0829189790"},
    {file = "pillow-11.0.0-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:7326a1787e3c7b0429659e0a944725e1b03eeaa10edd945a86dead1913383944"},
    {file = "pillow-11.0.0.tar.gz", hash = "sha256:72bacbaf24ac003fea9bff9837d1eedb6088758d41e100c1552930151f677739"},
]

[package.extras]
docs = ["furo", "olefile", "sphinx (>=8.1)", "sphinx-copybutton", "sphinx-inline-tabs", "sphinxext-opengraph"]
fpx = ["olefile"]
mic = ["olefile"]
tests = ["check-manifest", "coverage", "defusedxml", "markdown2", "olefile", "packaging", "pyroma", "pytest", "pytest-cov", "pytest-timeout"]
typing = ["typing-extensions ; python_version < \"3.10\""]
xmp = ["defusedxml"]

[[package]]
name = "platformdirs"
version = "4.3.6"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "platformdirs-4.3.6-py3-none-any.whl", hash = "sha256:73e575e1408ab8103900836b97580d5307456908a03e92031bab39e4554cc3fb"},
    {file = "platformdirs-4.3.6.tar.gz", hash = "sha256:357fb2acbc885b0419afd3ce3ed34564c13c9b95c89360cd9563f73aa5e2b907"},
]

[package.extras]
docs = ["furo (>=2024.8.6)", "proselint (>=0.14)", "sphinx (>=8.0.2)", "sphinx-autodoc-typehints (>=2.4)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.3.2)", "pytest-cov (>=5)", "pytest-mock (>=3.14)"]
type = ["mypy (>=1.11.2)"]

[[package]]
name = "pluggy"
version = "1.5.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pluggy-1.5.0-py3-none-any.whl", hash = "sha256:44e1ad92c8ca002de6377e165f3e0f1be63266ab4d554740532335b9d75ea669"},
    {file = "pluggy-1.5.0.tar.gz", hash = "sha256:2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["pytest", "pytest-benchmark"]

[[package]]
name = "prompt-toolkit"
version = "3.0.40"
description = "Library for building powerful interactive command lines in Python"
optional = false
python-versions = ">=3.7.0"
groups = ["dev"]
files = [
    {file = "prompt_toolkit-3.0.40-py3-none-any.whl", hash = "sha256:99ba3dfb23d5b5af89712f89e60a5f3d9b8b67a9482ca377c5771d0e9047a34b"},
    {file = "prompt_toolkit-3.0.40.tar.gz", hash = "sha256:a371c06bb1d66cd499fecd708e50c0b6ae00acba9822ba33c586e2f16d1b739e"},
]

[package.dependencies]
wcwidth = "*"

[[package]]
name = "ptyprocess"
version = "0.7.0"
description = "Run a subprocess in a pseudo terminal"
optional = false
python-versions = "*"
groups = ["dev"]
markers = "sys_platform != \"win32\""
files = [
    {file = "ptyprocess-0.7.0-py2.py3-none-any.whl", hash = "sha256:4b41f3967fce3af57cc7e94b888626c18bf37a083e3651ca8feeb66d492fef35"},
    {file = "ptyprocess-0.7.0.tar.gz", hash = "sha256:5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220"},
]

[[package]]
name = "pure-eval"
version = "0.2.2"
description = "Safely evaluate AST nodes without side effects"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "pure_eval-0.2.2-py3-none-any.whl", hash = "sha256:01eaab343580944bc56080ebe0a674b39ec44a945e6d09ba7db3cb8cec289350"},
    {file = "pure_eval-0.2.2.tar.gz", hash = "sha256:2b45320af6dfaa1750f543d714b6d1c520a1688dec6fd24d339063ce0aaa9ac3"},
]

[package.extras]
tests = ["pytest"]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
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
groups = ["dev"]
markers = "python_version == \"3.12\""
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
groups = ["dev"]
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
groups = ["dev"]
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
groups = ["dev"]
markers = "python_version == \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pygments"
version = "2.16.1"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "Pygments-2.16.1-py3-none-any.whl", hash = "sha256:13fc09fa63bc8d8671a6d247e1eb303c4b343eaee81d861f3404db2935653692"},
    {file = "Pygments-2.16.1.tar.gz", hash = "sha256:1daff0494820c69bc8941e407aa20f577374ee88364ee10a98fdbe0aece96e29"},
]

[package.extras]
plugins = ["importlib-metadata ; python_version < \"3.8\""]

[[package]]
name = "pyparsing"
version = "3.2.0"
description = "pyparsing module - Classes and methods to define and execute parsing grammars"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pyparsing-3.2.0-py3-none-any.whl", hash = "sha256:93d9577b88da0bbea8cc8334ee8b918ed014968fd2ec383e868fb8afb1ccef84"},
    {file = "pyparsing-3.2.0.tar.gz", hash = "sha256:cbf74e27246d595d9a74b186b810f6fbb86726dbf3b9532efb343f6d7294fe9c"},
]

[package.extras]
diagrams = ["jinja2", "railroad-diagrams"]

[[package]]
name = "pyproject-hooks"
version = "1.0.0"
description = "Wrappers to call pyproject.toml-based build backend hooks."
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "pyproject_hooks-1.0.0-py3-none-any.whl", hash = "sha256:283c11acd6b928d2f6a7c73fa0d01cb2bdc5f07c57a2eeb6e83d5e56b97976f8"},
    {file = "pyproject_hooks-1.0.0.tar.gz", hash = "sha256:f271b298b97f5955d53fb12b72c1fb1948c22c1a6b70b315c54cedaca0264ef5"},
]

[package.dependencies]
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}

[[package]]
name = "pytest"
version = "8.3.3"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pytest-8.3.3-py3-none-any.whl", hash = "sha256:a6853c7375b2663155079443d2e45de913a911a11d669df02a50814944db57b2"},
    {file = "pytest-8.3.3.tar.gz", hash = "sha256:70b98107bd648308a7952b06e6ca9a50bc660be218d53c257cc1fc94fda10181"},
]

[package.dependencies]
colorama = {version = "*", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1.0.0rc8", markers = "python_version < \"3.11\""}
iniconfig = "*"
packaging = "*"
pluggy = ">=1.5,<2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "pygments (>=2.7.2)", "requests", "setuptools", "xmlschema"]

[[package]]
name = "pytest-cov"
version = "4.1.0"
description = "Pytest plugin for measuring coverage."
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "pytest-cov-4.1.0.tar.gz", hash = "sha256:3904b13dfbfec47f003b8e77fd5b589cd11904a21ddf1ab38a64f204d6a10ef6"},
    {file = "pytest_cov-4.1.0-py3-none-any.whl", hash = "sha256:6ba70b9e97e69fcc3fb45bfeab2d0a138fb65c4d0d6a41ef33983ad114be8c3a"},
]

[package.dependencies]
coverage = {version = ">=5.2.1", extras = ["toml"]}
pytest = ">=4.6"

[package.extras]
testing = ["fields", "hunter", "process-tests", "pytest-xdist", "six", "virtualenv"]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
description = "Extensions to the standard Python datetime module"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["main"]
files = [
    {file = "python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3"},
    {file = "python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427"},
]

[package.dependencies]
six = ">=1.5"

[[package]]
name = "pytz"
version = "2024.2"
description = "World timezone definitions, modern and historical"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "pytz-2024.2-py2.py3-none-any.whl", hash = "sha256:31c7c1817eb7fae7ca4b8c7ee50c72f93aa2dd863de768e1ef4245d426aa0725"},
    {file = "pytz-2024.2.tar.gz", hash = "sha256:2aa355083c50a0f93fa581709deac0c9ad65cca8a9e9beac660adcbd493c798a"},
]

[[package]]
name = "pyvisa"
version = "1.14.1"
description = "Python VISA bindings for GPIB, RS232, TCPIP and USB instruments"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "PyVISA-1.14.1-py3-none-any.whl", hash = "sha256:6e4dfc9b6029b4f00d0d4960348c4889c2747aa7f83276950d48a349eab36a45"},
    {file = "PyVISA-1.14.1.tar.gz", hash = "sha256:71030041ed4c5dad77687454cf44b8be4d1642e9d1aaa22019248d41d8ed7a79"},
]

[package.dependencies]
typing-extensions = "*"

[[package]]
name = "scipy"
version = "1.13.0"
description = "Fundamental algorithms for scientific computing in Python"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "scipy-1.13.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:ba419578ab343a4e0a77c0ef82f088238a93eef141b2b8017e46149776dfad4d"},
    {file = "scipy-1.13.0-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:22789b56a999265431c417d462e5b7f2b487e831ca7bef5edeb56efe4c93f86e"},
    {file = "scipy-1.13.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:05f1432ba070e90d42d7fd836462c50bf98bd08bed0aa616c359eed8a04e3922"},
    {file = "scipy-1.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b8434f6f3fa49f631fae84afee424e2483289dfc30a47755b4b4e6b07b2633a4"},
    {file = "scipy-1.13.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:dcbb9ea49b0167de4167c40eeee6e167caeef11effb0670b554d10b1e693a8b9"},
    {file = "scipy-1.13.0-cp310-cp310-win_amd64.whl", hash = "sha256:1d2f7bb14c178f8b13ebae93f67e42b0a6b0fc50eba1cd8021c9b6e08e8fb1cd"},
    {file = "scipy-1.13.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0fbcf8abaf5aa2dc8d6400566c1a727aed338b5fe880cde64907596a89d576fa"},
    {file = "scipy-1.13.0-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:5e4a756355522eb60fcd61f8372ac2549073c8788f6114449b37e9e8104f15a5"},
    {file = "scipy-1.13.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b5acd8e1dbd8dbe38d0004b1497019b2dbbc3d70691e65d69615f8a7292865d7"},
    {file = "scipy-1.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9ff7dad5d24a8045d836671e082a490848e8639cabb3dbdacb29f943a678683d"},
    {file = "scipy-1.13.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:4dca18c3ffee287ddd3bc8f1dabaf45f5305c5afc9f8ab9cbfab855e70b2df5c"},
    {file = "scipy-1.13.0-cp311-cp311-win_amd64.whl", hash = "sha256:a2f471de4d01200718b2b8927f7d76b5d9bde18047ea0fa8bd15c5ba3f26a1d6"},
    {file = "scipy-1.13.0-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:d0de696f589681c2802f9090fff730c218f7c51ff49bf252b6a97ec4a5d19e8b"},
    {file = "scipy-1.13.0-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:b2a3ff461ec4756b7e8e42e1c681077349a038f0686132d623fa404c0bee2551"},
    {file = "scipy-1.13.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6bf9fe63e7a4bf01d3645b13ff2aa6dea023d38993f42aaac81a18b1bda7a82a"},
    {file = "scipy-1.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1e7626dfd91cdea5714f343ce1176b6c4745155d234f1033584154f60ef1ff42"},
    {file = "scipy-1.13.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:109d391d720fcebf2fbe008621952b08e52907cf4c8c7efc7376822151820820"},
    {file = "scipy-1.13.0-cp312-cp312-win_amd64.whl", hash = "sha256:8930ae3ea371d6b91c203b1032b9600d69c568e537b7988a3073dfe4d4774f21"},
    {file = "scipy-1.13.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:5407708195cb38d70fd2d6bb04b1b9dd5c92297d86e9f9daae1576bd9e06f602"},
    {file = "scipy-1.13.0-cp39-cp39-macosx_12_0_arm64.whl", hash = "sha256:ac38c4c92951ac0f729c4c48c9e13eb3675d9986cc0c83943784d7390d540c78"},
    {file = "scipy-1.13.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:09c74543c4fbeb67af6ce457f6a6a28e5d3739a87f62412e4a16e46f164f0ae5"},
    {file = "scipy-1.13.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:28e286bf9ac422d6beb559bc61312c348ca9b0f0dae0d7c5afde7f722d6ea13d"},
    {file = "scipy-1.13.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:33fde20efc380bd23a78a4d26d59fc8704e9b5fd9b08841693eb46716ba13d86"},
    {file = "scipy-1.13.0-cp39-cp39-win_amd64.whl", hash = "sha256:45c08bec71d3546d606989ba6e7daa6f0992918171e2a6f7fbedfa7361c2de1e"},
    {file = "scipy-1.13.0.tar.gz", hash = "sha256:58569af537ea29d3f78e5abd18398459f195546bb3be23d16677fb26616cc11e"},
]

[package.dependencies]
numpy = ">=1.22.4,<2.3"

[package.extras]
dev = ["cython-lint (>=0.12.2)", "doit (>=0.36.0)", "mypy", "pycodestyle", "pydevtool", "rich-click", "ruff", "types-psutil", "typing_extensions"]
doc = ["jupyterlite-pyodide-kernel", "jupyterlite-sphinx (>=0.12.0)", "jupytext", "matplotlib (>=3.5)", "myst-nb", "numpydoc", "pooch", "pydata-sphinx-theme (>=0.15.2)", "sphinx (>=5.0.0)", "sphinx-design (>=0.4.0)"]
test = ["array-api-strict", "asv", "gmpy2", "hypothesis (>=6.30)", "mpmath", "pooch", "pytest", "pytest-cov", "pytest-timeout", "pytest-xdist", "scikit-umfpack", "threadpoolctl"]

[[package]]
name = "setuptools"
version = "75.5.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "setuptools-75.5.0-py3-none-any.whl", hash = "sha256:87cb777c3b96d638ca02031192d40390e0ad97737e27b6b4fa831bea86f2f829"},
    {file = "setuptools-75.5.0.tar.gz", hash = "sha256:5c4ccb41111392671f02bb5f8436dfc5a9a7185e80500531b133f5775c4163ef"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.7.0) ; sys_platform != \"cygwin\""]
core = ["importlib-metadata (>=6) ; python_version < \"3.10\"", "jaraco.collections", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more-itertools", "more-itertools (>=8.8)", "packaging", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.2.0)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib-metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (>=1.12,<1.14)", "pytest-mypy"]

[[package]]
name = "six"
version = "1.16.0"
description = "Python 2 and 3 compatibility utilities"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["main", "dev"]
files = [
    {file = "six-1.16.0-py2.py3-none-any.whl", hash = "sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"},
    {file = "six-1.16.0.tar.gz", hash = "sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"},
]

[[package]]
name = "snowballstemmer"
version = "2.2.0"
description = "This package provides 29 stemmers for 28 languages generated from Snowball algorithms."
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "snowballstemmer-2.2.0-py2.py3-none-any.whl", hash = "sha256:c8e1716e83cc398ae16824e5572ae04e0d9fc2c6b985fb0f900f5f0c96ecba1a"},
    {file = "snowballstemmer-2.2.0.tar.gz", hash = "sha256:09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1"},
]

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
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["dev"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.1.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.1.0-py3-none-any.whl", hash = "sha256:a5c57c3d1c56f5ccdf89f6523458f60ef716e210fc47c4cfb188c5ba473e0391"},
    {file = "tomli-2.1.0.tar.gz", hash = "sha256:3f646cae2aec94e17d04973e4249548320197cfabdf130015d023de4b74d8ab8"},
]

[[package]]
name = "traitlets"
version = "5.13.0"
description = "Traitlets Python configuration system"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "traitlets-5.13.0-py3-none-any.whl", hash = "sha256:baf991e61542da48fe8aef8b779a9ea0aa38d8a54166ee250d5af5ecf4486619"},
    {file = "traitlets-5.13.0.tar.gz", hash = "sha256:9b232b9430c8f57288c1024b34a8f0251ddcc47268927367a0dd3eeaca40deb5"},
]

[package.extras]
docs = ["myst-parser", "pydata-sphinx-theme", "sphinx"]
test = ["argcomplete (>=3.0.3)", "mypy (>=1.6.0)", "pre-commit", "pytest (>=7.0,<7.5)", "pytest-mock", "pytest-mypy-testing"]

[[package]]
name = "typing-extensions"
version = "4.12.2"
description = "Backported and Experimental Type Hints for Python 3.8+"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "typing_extensions-4.12.2-py3-none-any.whl", hash = "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d"},
    {file = "typing_extensions-4.12.2.tar.gz", hash = "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8"},
]
markers = {dev = "python_version == \"3.10\""}

[[package]]
name = "tzdata"
version = "2024.2"
description = "Provider of IANA time zone data"
optional = false
python-versions = ">=2"
groups = ["main"]
files = [
    {file = "tzdata-2024.2-py2.py3-none-any.whl", hash = "sha256:a48093786cdcde33cad18c2555e8532f34422074448fbc874186f0abd79565cd"},
    {file = "tzdata-2024.2.tar.gz", hash = "sha256:7d85cc416e9382e69095b7bdf4afd9e3880418a2413feec7069d533d6b4e31cc"},
]

[[package]]
name = "varname"
version = "0.12.0"
description = "Dark magics about variable names in python."
optional = false
python-versions = ">=3.8,<4.0"
groups = ["main", "dev"]
files = [
    {file = "varname-0.12.0-py3-none-any.whl", hash = "sha256:fc0d056072918efc76375237cbbaa49402f22cc06ed61e893ac71c272d3b3f4d"},
    {file = "varname-0.12.0.tar.gz", hash = "sha256:ca0c7c974a1a9382144eeee21ab429286c9de8259248ce40a9f48bcf08adb223"},
]

[package.dependencies]
executing = ">=2.0,<3.0"

[package.extras]
all = ["asttokens (==2.*)", "pure_eval (==0.*)"]

[[package]]
name = "wcwidth"
version = "0.2.9"
description = "Measures the displayed width of unicode strings in a terminal"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "wcwidth-0.2.9-py2.py3-none-any.whl", hash = "sha256:9a929bd8380f6cd9571a968a9c8f4353ca58d7cd812a4822bba831f8d685b223"},
    {file = "wcwidth-0.2.9.tar.gz", hash = "sha256:a675d1a4a2d24ef67096a04b85b02deeecd8e226f57b5e3a72dbb9ed99d27da8"},
]

[[package]]
name = "wheel"
version = "0.45.0"
description = "A built-package format for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "wheel-0.45.0-py3-none-any.whl", hash = "sha256:52f0baa5e6522155090a09c6bd95718cc46956d1b51d537ea5454249edb671c7"},
    {file = "wheel-0.45.0.tar.gz", hash = "sha256:a57353941a3183b3d5365346b567a260a0602a0f8a635926a7dede41b94c674a"},
]

[package.extras]
test = ["pytest (>=6.0.0)", "setuptools (>=65)"]

[metadata]
lock-version = "2.1"
python-versions = ">=3.10,<3.13"
content-hash = "f3724c2b86db60108f801900e716a96d9f7a4ca270e33a3d73c68df4636d8e73"
````

<!--NI_OSS_SOURCE repo=nipcbatt path=poetry.toml sha256=1240de1104b41b90fac11de710f992aeaeb5d60516f95c44e57147801d5fb285 bytes=47 -->
## FILE: poetry.toml

- repository: `ni/nipcbatt`
- source_path: `poetry.toml`
- sha256: `1240de1104b41b90fac11de710f992aeaeb5d60516f95c44e57147801d5fb285`
- bytes: 47

````toml
[virtualenvs]
create = true
in-project = true
````

<!--NI_OSS_SOURCE repo=nipcbatt path=pyproject.toml sha256=1ce51af26074e16cfffac4e11bce1847605462e5b6c8bb8f77560898f0f5e749 bytes=2588 -->
## FILE: pyproject.toml

- repository: `ni/nipcbatt`
- source_path: `pyproject.toml`
- sha256: `1ce51af26074e16cfffac4e11bce1847605462e5b6c8bb8f77560898f0f5e749`
- bytes: 2588

````toml
[tool.poetry]
name = "nipcbatt"
version = "2.0.0"
license = "MIT"
description = "Python PCB Assembly Test Toolkit"
authors = ["NI <opensource@ni.com>"]
maintainers = ["Emmanuel ROSET <emmanuel.roset@emerson.com>", "Srinivasan J <srinivasan.j@emerson.com>", "Aditya Saxena <adityasaxena@emerson.com>", "Ankit Singh <ankitsingh@emerson.com>"]
include = ["requirements.txt", "requirements_for_packaging.txt"]
readme = "README.rst"
repository = "https://github.com/ni/nipcbatt"
keywords = ["nipcbatt", "pcbatt", "pcba", "pcb"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Science/Research",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
packages = [{ include = "nipcbatt", from = "src" }]

[tool.poetry.dependencies]
python = ">=3.10,<3.13"
numpy = "1.26.4"
scipy = "1.13.0"
nidaqmx = "0.9.0"
nidmm = "1.4.7"
niswitch = "1.4.7"
nidcpower = "1.5.0"
pyvisa = "1.14.1"
colorama = "0.4.6"
varname = "0.12.0"
executing = "2.0.1"
pandas = "2.2.2"
matplotlib = "3.9.2"

[tool.poetry.group.dev.dependencies]
setuptools = "*"
wheel = "*"
asttokens = "2.4.1"
build = "1.0.3"
colorama = "0.4.6"
decorator = "5.1.1"
deprecation = "2.1.0"
executing = "2.0.1"
ipython = "8.17.2"
jedi = "0.19.1"
matplotlib-inline = "0.1.6"
packaging = "23.2"
parso = "0.8.3"
prompt-toolkit = "3.0.40"
pure-eval = "0.2.2"
Pygments = "2.16.1"
pyproject_hooks = "1.0.0"
six = "1.16.0"
stack-data = "0.6.3"
toml = "0.10.2"
traitlets = "5.13.0"
varname = "0.12.0"
wcwidth = "0.2.9"
pytest = ">=6.2.3"
pytest-cov = "^4.1.0"
mock = ">=4.0.3"
pep8-naming = ">=0.13.2"
parameterized = "^0.8.1"
ni-python-styleguide = ">=0.4.6"
black = "^23.3.0"
flake8 = ">=5.0.4"


[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.setuptools.package-data]
"*" = [ "win_amd64/NI.*.dll",]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = "src"
# Skipping the tests as they require NI DAQmx
norecursedirs = [
    "tests/nipcbatt_tests/*"
]

[tool.distutils.bdist_wheel]
plat-name = "win_amd64"

[tool.black]
line-length = 100
extend_exclude = "src/docs"

[tool.ni-python-styleguide]
extend_exclude = "src/docs,src/nipcbatt/pcbatt_automation,src/nipcbatt/pcbatt_ft_demo_test_sequence,src/nipcbatt/pcbatt_validation_examples"
````

<!--NI_OSS_SOURCE repo=nipcbatt path=README.rst sha256=e00354bd15267533924cb1f1acd248aeda5f21b26c8a6c4d96f49df3d77530b2 bytes=12688 -->
## FILE: README.rst

- repository: `ni/nipcbatt`
- source_path: `README.rst`
- sha256: `e00354bd15267533924cb1f1acd248aeda5f21b26c8a6c4d96f49df3d77530b2`
- bytes: 12688

````rst
+------------+------------------------------------------------------------------------------------+
| **Info**   | A python based package providing a set of generation, measurement and              | 
|            | communication building blocks, that can be used to perform PCB Assembly tests.     |
+------------+------------------------------------------------------------------------------------+
| **Author** | National Instruments                                                               |
+------------+------------------------------------------------------------------------------------+

.. contents:: Table of Contents
   :depth: 1
   :backlinks: none

About
=====

The **nipcbatt** package provides APIs (Application Programming Interface) for interacting with 
the NI_DMM, NI-SWITCH, NI-DAQmx driver and with LabVIEW runtime to perform measurement, generation and communication 
operations. The package is implemented in Python, as a highly object-oriented package.

Python PCB Assembly Test Toolkit or **nipcbatt** is a collection of Measurement Library, Automation Examples,
Test Demo Example developed in Python along with Documentation for PCB Assembly electrical functional test.

**nipcbatt** package is focused on NI DAQ, DMM, and SWITCH devices, and compatible with NI PC Based DAQ, CompactDAQ, NI-DMM,
TestScale and high level enough to be applicable or scalable for other instruments with similar functionality and 
resources on any platform.

Documentation
-------------

Refer to the `Python PCB Assembly Test Toolkit - Getting Started <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20Getting%20Started.pdf>`_ guide for
getting started steps including installation and setup procedures, and steps to run example test sequences. 
Refer to the `User Manual <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/Python%20PCB%20Assembly%20Test%20Toolkit%20-%20User%20Manual.pdf>`_ for an overview of Toolkit concepts and measurement 
fundamentals, including a brief overview of each library and automation sequences.

Supported Features
------------------

.. list-table::
   :widths: 25 55 20
   :header-rows: 0

   * - Feature name
     - Description
     - Acronym
   * - `DMM Measurement Libraries <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_library/dmm>`_
     - A collection of methods to perform DMM measurements using NI-DMM driver.
     - dmm
   * - `DAQ Measurement Libraries <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_library/daq>`_
     - A collection of methods to perform measurements using NI-DAQmx driver.
     - daq
   * - `SWITCH Measurement Libraries <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_library/switch>`_
     - A collection of methods to control Switch hardware, and switch paths using the NI-SWITCH driver.
     - switch
   * - `DMM Scan Measurement Libraries <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_library/dmm_scan>`_
     - A collection of methods to perform measurements using NI-DMM and NI-SWITCH driver.
     - dmm_scan
   * - `Communication Libraries <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_library/communications>`_
     - A collection of methods to perform communication operations (for example I2C, SPI, and serial) using NI-845x and NI-VISA drivers.
     - comm


Library imports and migrations
-------------------------------

    In this release the instrument-specific measurement libraries are exposed as subpackages under the top-level
    `nipcbatt` package. Example usage:

    .. code-block:: python

      from nipcbatt import daq
      drvg = daq.DcVoltageGeneration()
      drvg.initialize(analog_output_channel_expression="Sim_PC_basedDAQ/ao0")

    Few classes remain accessible directly from `nipcbatt` (for
    example `nipcbatt.MeasurementExecutionType`). However, explicit subpackage imports are the recommended approach 
    for all new code. To migrate existing code, update imports and references from:

    .. code-block:: python

      # Not recommended ❌
      import nipcbatt
      drvg = nipcbatt.DcVoltageGeneration()

    to the explicit subpackage form:

    .. code-block:: python

      # Recommended ✅
      from nipcbatt import daq
      drvg = daq.DcVoltageGeneration()

    See `Migration Guide for nipcbatt 2.0.0 <https://github.com/ni/nipcbatt/blob/main/src/nipcbatt/docs/Migration%20Guide%20for%20nipcbatt%202.0.0.md>`_ 
    for a complete list of class mappings, and all available subpackage classes.


Required Drivers
-----------------


- NI-DMM: 2023 Q4 and above
- NI-SWITCH: 2023 Q4 and above 
- NI-DAQmx: 2023 Q3 and above 
- LabVIEW Runtime: 2022 Q3 and above (64 bit) 
- NI-845x: 2022 Q3 and above 
- NI-VISA: 2023 Q2 and above 
- NI-Serial: 2023 Q2 and above 
  
Visit `ni.com/downloads <http://www.ni.com/downloads/>`_  or visit `NI Package Manager <https://www.ni.com/en/support/downloads/software-products/download.package-manager.html>`_ to download the Required Drivers.


Supported Hardware
------------------

- DMM devices compatible with the NI-DMM driver
- Switch devices compatible with the NI-SWITCH driver
- Any DAQmx devices with similar functionality and resources
- NI PC-Based DAQ
- CompactDAQ
- TestScale


Operating System Support
------------------------

**nipcbatt** supports Windows 10 and 11 systems where the supported drivers are 
installed. Refer to `NI Hardware and Operating System Compatibility <https://www.ni.com/r/hw-support>`_ for 
which versions of the driver support your hardware on a given operating system.

Python Version Support
----------------------

**nipcbatt** supports Python 3.9 to 3.12 (64 bit)

Installation
============

You can use `pip <http://pypi.python.org/pypi/pip>`_ to download **nipcbatt** from
`PyPI <https://pypi.org/project/nipcbatt/>`_ and install it::

  $ python -m pip install nipcbatt


Getting Started
===============

In order to use the **nipcbatt package**, you must have at least one DAQ (`Data Acquisition <https://www.ni.com/en/shop/data-acquisition.html>`_)
device installed on your system. Both physical and simulated devices are supported. The examples below use PC 
based DAQ device (PCIe-6353). You can use NI MAX or NI Hardware 
Configuration Utility to verify and configure your devices.


Finding and configuring device name in **NI MAX**:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/NI-MAX.png
  :alt: NI-MAX
  :align: center
  :width: 800px

Finding and configuring device name in **NI Hardware Configuration Utility**:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/Hardware%20Configuration%20Utility.png
  :alt: Hardware Config
  :align: center
  :width: 800px

Then refer to the Validation examples and Automation sequences to start testing. Refer to the Getting Started Guide for information.


Key Concepts in Python PCBATT
=============================

1. Libraries
-------------

All the measurement libraries consist of three main methods which have to be used in the following order:

- Initialize:
 
   Used to initialize a measurement instance (for DAQmx use either physical or global virtual channels to perform the respective task).

   This is done by calling the initialize() method on the class instance.

Example code to initialize an instance of DC RMS voltage measurement:

.. code-block:: python

  >>> from nipcbatt import dmm
  >>> dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()
  >>> dmm_voltage_measurement.initialize("Sim_DMM", 50)


- Configure and Generate/Configure and Measure:
 
   Configures and executes measurement or generation tasks. For measurements, 
   this method can return both raw data for custom analysis and processed results 
   from built-in analysis functions (configurable via measurement options).
 
   This is done by calling the
   configure_and_measure()/configure_and_generate() method on the class instance.

Example code to configure and measure DC voltage using the class instance:

.. code-block:: python

  >>> measurement = dmm_voltage_measurement.configure_and_measure(
  >>>   configuration=dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
  >>> )
  ... # Default voltage measurement configuration 


- Close:
 
   Closes the measurement or generation session and releases hardware resources.

   This is done by calling the close() method on the class instance.
  
Example code to close the session and clear resources:

.. code-block:: python

  >>> dmm_voltage_measurement.close()


1. Features and Utilities
-------------------------

- Virtual Channels 

   Virtual channels, or sometimes referred to generically as channels, are software entities that encapsulate the physical channel along with 
   other channel specific information (e.g.: range, terminal configuration, and custom scaling) that formats the data. A physical channel is a 
   terminal or pin at which you can measure or generate an analog or digital signal. A single physical channel can include more than one 
   terminal, as in the case of a differential analog input channel or a digital port of eight lines. Every physical channel on a device has a unique 
   name (for instance, cDAQ1Mod4/ai0, Dev2/ao5, and Dev6/ctr3) that follows the NI-DAQmx physical channel naming convention. 
   Refer to `NI-DAQmx Channel <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/chans.html>`_ for more information.

- Logger

   The logger is a feature which comes along with the package as a part of PCBATT Utilities and helps in 
   storing configuration details and results for every run of the sequences. It can be used to store results 
   in the *.txt* or *.csv* file formats. The logger stores results for every run in the same file. Example usage of the logger can be found 
   in the automation sequences.

- Save Traces

   This Utility works in a similar manner as the logger but it saves configuration settings and results for each run in separate files.
   Example usage of the save_traces module can be found in the validation examples.



Usage
=============
 
1. Validation Examples
---------------------------
 
Validation examples are created as examples for testing and validating a pair of
libraries together, where one library is used for generation and another for measurement.
The validation examples can be found in this location `pcbatt_validation_examples <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_validation_examples>`_.

The following images shows sample results for Signal Voltage Generation to Frequency Domain Voltage Measurement Validation example which
is located at *"/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py"*:

.. image:: https://raw.githubusercontent.com/ni/nipcbatt/main/src/nipcbatt/docs/images/SVG_to_FDVM_Results.png
  :alt: SVG_to_FDVM_Results
  :align: center
  :width: 600px

2. Automation Sequences
-----------------------

Automation sequences are examples of using libraries for real time
scenarios like microphone tests, LED tests and so on. Automation sequences are tested in simulation mode.

Following is the list of Automation Sequences provided as a part of the package.

a. action_button_tests

b. audio_tests

c. communication_tests

d. digital_io_tests

e. led_tests

f. microphone_tests

g. power_supply_tests

h. sensor_tests

i. synchronization_tests

The Automation Sequences can be found in this location `pcbatt_automation <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_automation>`_.

 
3. Functional Test Demo Sequence
---------------------------------
 
FT demo sequence is an example for creating a test sequence using
libraries with applying test limits on the results to determine whether the test is a pass or a fail.

Please refer to the FT Demo Sequence in the location `pcbatt_ft_demo_test_sequence <https://github.com/ni/nipcbatt/tree/main/src/nipcbatt/pcbatt_ft_demo_test_sequence>`_.



Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use GitHub `Issues  <https://github.com/ni/nipcbatt/issues>`_.


License
========
**nipcbatt** is licensed under an MIT-style license. Other incorporated projects may be licensed under different licenses. All 
licenses allow for non-commercial and commercial use.
````

<!--NI_OSS_SOURCE repo=nipcbatt path=requirements.txt sha256=d3705cf3c99e1f8891246f66c39da22f9f9f0428b7d8c9c7f2c1da067d02ba65 bytes=213 -->
## FILE: requirements.txt

- repository: `ni/nipcbatt`
- source_path: `requirements.txt`
- sha256: `d3705cf3c99e1f8891246f66c39da22f9f9f0428b7d8c9c7f2c1da067d02ba65`
- bytes: 213

````text
numpy==1.26.4
scipy==1.13.0
nidaqmx==0.9.0
nidmm==1.4.7
nidcpower==1.5.0
niswitch==1.4.7
nidcpower==1.5.0
pyvisa==1.14.1
colorama==0.4.6
varname==0.12.0
executing==2.0.1
pandas==2.2.2
matplotlib==3.9.2
````

<!--NI_OSS_SOURCE repo=nipcbatt path=requirements_for_packaging.txt sha256=cffb1305fc4df487b21583eed791eb8a4e7abe2b11b030a9cb9f5c9e44e4eb04 bytes=385 -->
## FILE: requirements_for_packaging.txt

- repository: `ni/nipcbatt`
- source_path: `requirements_for_packaging.txt`
- sha256: `cffb1305fc4df487b21583eed791eb8a4e7abe2b11b030a9cb9f5c9e44e4eb04`
- bytes: 385

````text
asttokens==2.4.1
build==1.0.3
colorama==0.4.6
decorator==5.1.1
deprecation==2.1.0
executing==2.0.1
ipython==8.17.2
jedi==0.19.1
matplotlib-inline==0.1.6
packaging==23.2
parso==0.8.3
prompt-toolkit==3.0.40
pure-eval==0.2.2
Pygments==2.16.1
pyproject_hooks==1.0.0
six==1.16.0
stack-data==0.6.3
toml==0.10.2
traitlets==5.13.0
varname==0.12.0
wcwidth==0.2.9
setuptools
````

<!--NI_OSS_SOURCE repo=nipcbatt path=requirements_for_unittests.txt sha256=6c8072cccd355be9cef8903e8d5880a7611679802b33098d8f900c37ed0c5ab7 bytes=136 -->
## FILE: requirements_for_unittests.txt

- repository: `ni/nipcbatt`
- source_path: `requirements_for_unittests.txt`
- sha256: `6c8072cccd355be9cef8903e8d5880a7611679802b33098d8f900c37ed0c5ab7`
- bytes: 136

````text
numpy
scipy
nidaqmx
nidmm
nidcpower
niswitch
nidcpower
pyvisa
colorama
varname
executing
pandas
parameterized
matplotlib
.
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/clean_dll_files.py sha256=d28b0015b094894c0789ca9d6cd27ee4724d225bc4b3bc02c53218fa476a5e3d bytes=1868 -->
## FILE: scripts/clean_dll_files.py

- repository: `ni/nipcbatt`
- source_path: `scripts/clean_dll_files.py`
- sha256: `d28b0015b094894c0789ca9d6cd27ee4724d225bc4b3bc02c53218fa476a5e3d`
- bytes: 1868

````python
"""Cleans the dll files present in python src folders"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

from varname import nameof

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent.parent

    logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

    x64_dlls_destination_folder_path = os.path.join(
        repository_dir_path,
        "pcbatt.python",
        "src",
        "nipcbatt",
        "pcbatt_analysis",
        "win_amd64",
    )

    win32_dlls_destination_folder_path = os.path.join(
        repository_dir_path,
        "pcbatt.python",
        "src",
        "nipcbatt",
        "pcbatt_analysis",
        "win32",
    )

    if os.path.exists(x64_dlls_destination_folder_path):
        logging.debug("delete dlls folder: %s", x64_dlls_destination_folder_path)
        x64_dll_files_list = [
            f for f in os.listdir(x64_dlls_destination_folder_path) if f.endswith(".dll")
        ]

        for dll_file in x64_dll_files_list:
            os.remove(os.path.join(x64_dlls_destination_folder_path, dll_file))

    if os.path.exists(win32_dlls_destination_folder_path):
        logging.debug("delete dlls folder: %s", win32_dlls_destination_folder_path)
        win32_dll_files_list = [
            f for f in os.listdir(win32_dlls_destination_folder_path) if f.endswith(".dll")
        ]

        for dll_file in win32_dll_files_list:
            os.remove(os.path.join(win32_dlls_destination_folder_path, dll_file))
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/clean_py_cache.bat sha256=905d40e26dd170c46a29748a37bb2d7c9d8b341caefac5d57d2dfc03c48cddca bytes=179 -->
## FILE: scripts/clean_py_cache.bat

- repository: `ni/nipcbatt`
- source_path: `scripts/clean_py_cache.bat`
- sha256: `905d40e26dd170c46a29748a37bb2d7c9d8b341caefac5d57d2dfc03c48cddca`
- bytes: 179

````batch
@echo off
cd %~dp0



cd "..\"
echo "Delete cache folders in python folder ..."
for /d /r . %%d in (__pycache__) do @if exist "%%d" echo "%%d" && rd /s/q "%%d"
echo "Done"
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/create_venvs_tree.py sha256=92c95a4f14187a05520836dd9d8f57de199896753d3bef5022055ef607058fcd bytes=619 -->
## FILE: scripts/create_venvs_tree.py

- repository: `ni/nipcbatt`
- source_path: `scripts/create_venvs_tree.py`
- sha256: `92c95a4f14187a05520836dd9d8f57de199896753d3bef5022055ef607058fcd`
- bytes: 619

````python
"""Script that should be used to create venvs tree near src folder"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

import logging
import sys

import venv_tools

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # create empty folders tree
    venv_tools.create_venvs_root_folder()

    # fill content of folders tree
    venv_tools.create_venvs_folders_content()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/filesystem_utils.py sha256=a03042b08017b40d794e8d8f93ee1961fea9fdf31c8af59192faf9ef926a10e8 bytes=1058 -->
## FILE: scripts/filesystem_utils.py

- repository: `ni/nipcbatt`
- source_path: `scripts/filesystem_utils.py`
- sha256: `a03042b08017b40d794e8d8f93ee1961fea9fdf31c8af59192faf9ef926a10e8`
- bytes: 1058

````python
"""Defines a set of filesystem utility functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)

import os
import shutil


def safe_copy_dll_file(
    dlls_source_folder_path: str,
    dlls_destination_folder_path: str,
    dll_file_name: str,
):
    """Copies dll file from a given source folder into a destination folder.

    Args:
        dlls_source_folder_path (str): source folder from where dll file should be copied.
        dlls_destination_folder_path (str): destination folder where dll files
        should be copied into.
        dll_file_name (str): name of the dll file
    """
    destination_file_path = os.path.join(dlls_destination_folder_path, dll_file_name)

    if os.path.exists(destination_file_path):
        os.remove(destination_file_path)

    shutil.copy(
        src=os.path.join(dlls_source_folder_path, dll_file_name),
        dst=destination_file_path,
    )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/install_vscode_extensions.py sha256=2b49acd0a3bdda573090ccee696920a2d97ecfa5a882294e13eae8cc1d77f83b bytes=1358 -->
## FILE: scripts/install_vscode_extensions.py

- repository: `ni/nipcbatt`
- source_path: `scripts/install_vscode_extensions.py`
- sha256: `2b49acd0a3bdda573090ccee696920a2d97ecfa5a882294e13eae8cc1d77f83b`
- bytes: 1358

````python
"""Script that should be used to install visual code extensions 
for python development during PBCATT project"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (340 > 100 characters) (auto-generated noqa)

import os
from pathlib import Path

EXTENSIONS_FILE_NAME = "vscode.extensions.txt"


def main():
    """Executes vscode extensions installation from vscode.extensions.txt"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
    extensions_list_file_path = os.path.join(Path(__file__).parent, EXTENSIONS_FILE_NAME)

    with open(extensions_list_file_path, encoding="utf-16") as vscode_extensions_file:
        lines = vscode_extensions_file.readlines()

        for line in lines:
            print(f"Install of {line}")
            command = f"cmd.exe /c code --force --install-extension {line}"
            os.system(command)


# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/label_pyproject_with_build_number.py sha256=303f7a5d33dca8dc591102e97f7dbd03bfdfb0159acb228a000887171e3e6209 bytes=3353 -->
## FILE: scripts/label_pyproject_with_build_number.py

- repository: `ni/nipcbatt`
- source_path: `scripts/label_pyproject_with_build_number.py`
- sha256: `303f7a5d33dca8dc591102e97f7dbd03bfdfb0159acb228a000887171e3e6209`
- bytes: 3353

````python
"""Script that should be used to label pyproject file with build number"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

import toml
from colorama import Fore, Style
from varname import nameof

PROJECT_TOML_FILE_NAME = "pyproject.toml"
PROJECT_PY_ENTRY_NAME_PROJECT = "project"
PROJECT_PY_ENTRY_NAME_VERSION = "version"


def transform_toml_pkg_version(build_number: int, pyproject_file_path: str):
    """Parses pyproject.toml and replaces last digit of version entry with build number

    Args:
        build_number (int): build counter value to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add build number into it
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    parsed_data = toml.load(f=pyproject_file_path)

    logging.debug("pyproject: %s", parsed_data)

    project_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_PROJECT)

    if project_entry is not None:
        version_entry = project_entry.get("version")

        if version_entry is not None:
            logging.debug("found version:")
            logging.debug("%s: %s", nameof(version_entry), version_entry)

            package_version = parsed_data[PROJECT_PY_ENTRY_NAME_PROJECT][
                PROJECT_PY_ENTRY_NAME_VERSION
            ]
            str_tokens = package_version.split(sep=".")

            logging.debug("%s = %s", nameof(str_tokens), str_tokens)

            if str_tokens is not None and len(str_tokens) == 4:
                parsed_data[PROJECT_PY_ENTRY_NAME_PROJECT][
                    PROJECT_PY_ENTRY_NAME_VERSION
                ] = f"{str_tokens[0]}.{str_tokens[1]}.{str_tokens[2]}.{build_number}"

    return parsed_data


def label_pyproject(build_number: int) -> None:
    """Applies build number labeling to project toml file.

    Args:
        build_number (int): build counter value
    """
    print(f"Labeling project toml with build number {build_number}:")
    pyproject_file_path = os.path.join(Path(__file__).parent.parent, PROJECT_TOML_FILE_NAME)

    if os.path.exists(pyproject_file_path):
        print(f"Transform file located at {pyproject_file_path} ...")

        transformed_toml_data = transform_toml_pkg_version(build_number, pyproject_file_path)

        with open(pyproject_file_path, "w", encoding="utf8") as f:
            print(f"Write toml transformed data into {pyproject_file_path} ...")
            toml.dump(transformed_toml_data, f)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("args: %s", args)

        if len(args) == 1:
            label_pyproject(build_number=int(args[0]))
        else:
            label_pyproject(build_number=0)
    except:  # noqa: E722 - do not use bare 'except' (auto-generated noqa)
        print(Fore.RED + "Failure: " + str(sys.exc_info()[0]))
        raise
    finally:
        print(Style.RESET_ALL)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/label_pyproject_with_platform_architecture.py sha256=d8fedc191850bd1b33a26b0ec843d1876d05f2aef21e219c5788c9271dea5cad bytes=5108 -->
## FILE: scripts/label_pyproject_with_platform_architecture.py

- repository: `ni/nipcbatt`
- source_path: `scripts/label_pyproject_with_platform_architecture.py`
- sha256: `d8fedc191850bd1b33a26b0ec843d1876d05f2aef21e219c5788c9271dea5cad`
- bytes: 5108

````python
"""Script that should be used to label pyproject file with specific plateform architecture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (204 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

import toml
from colorama import Fore, Style
from varname import nameof

PROJECT_TOML_FILE_NAME = "pyproject.toml"
PROJECT_PY_ENTRY_NAME_PROJECT = "project"
PROJECT_PY_ENTRY_NAME_BDIST_WHEEL = ("tool", "distutils", "bdist_wheel")
PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME = "plat-name"
PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA = ("tool", "setuptools", "package-data")
PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA_PCBATT_ANALYSIS = "pcbatt_analysis"

PLATFORM_TAG_WIN32 = "win32"
PLATFORM_TAG_WIN_AMD64 = "win_amd64"
SUPPORTED_PLATFORM_TAGS = [PLATFORM_TAG_WIN32, PLATFORM_TAG_WIN_AMD64]
SUPPORTED_PLATFORM_TAGS_DLL_PATHS = {
    PLATFORM_TAG_WIN32: [f"{PLATFORM_TAG_WIN32}/NI.*.dll"],
    PLATFORM_TAG_WIN_AMD64: [f"{PLATFORM_TAG_WIN_AMD64}/NI.*.dll"],
}


def transform_toml_pkg_plateform_architecture(
    plateform_architecture_tag: str, pyproject_file_path: str
):
    """Parses pyproject.toml and replaces plat-name entry

    Args:
        plateform_architecture_tag (str): platform architecture tag to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add platform architecture tag into it
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    logging.debug("Apply platform tag: %s", plateform_architecture_tag)

    parsed_data = toml.load(f=pyproject_file_path)

    # parse PACKAGE DATA PART
    tool_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[0])
    if tool_entry is not None:
        setuptools_entry = tool_entry.get(PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[1])

        if setuptools_entry is not None:
            logging.debug(
                "%s: %s",
                nameof(setuptools_entry),
                setuptools_entry,
            )

            package_data_entry = setuptools_entry.get(
                PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[2]
            )

            package_data_entry["*"] = SUPPORTED_PLATFORM_TAGS_DLL_PATHS[plateform_architecture_tag]

    # parse BDIST WHEEL PART
    tool_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[0])

    if tool_entry is not None:
        distutils_entry = tool_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[1])

        if distutils_entry is not None:
            logging.debug(
                "%s: %s",
                nameof(distutils_entry),
                distutils_entry,
            )

            bdist_wheel_entry = distutils_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[2])

            platename_entry = bdist_wheel_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME)

            if platename_entry is not None:
                logging.debug("%s: %s", nameof(platename_entry), platename_entry)
                bdist_wheel_entry[
                    PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME
                ] = plateform_architecture_tag

    return parsed_data


def label_pyproject(plateform_architecture_tag: str) -> None:
    """Applies plateform architecture tag labeling to project toml file.

    Args:
        plateform_architecture_tag (str): architecture tag value
    """
    print(f"Labeling project toml with architecture tag {plateform_architecture_tag}:")
    pyproject_file_path = os.path.join(Path(__file__).parent.parent, PROJECT_TOML_FILE_NAME)

    if os.path.exists(pyproject_file_path):
        print(f"Transform file located at {pyproject_file_path} ...")

        transformed_toml_data = transform_toml_pkg_plateform_architecture(
            plateform_architecture_tag, pyproject_file_path
        )

        with open(pyproject_file_path, "w", encoding="utf8") as f:
            print(f"Write toml transformed data into {pyproject_file_path} ...")
            toml.dump(transformed_toml_data, f)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("args: %s", args)

        if len(args) == 1:
            arg0 = args[0]
            if arg0 in SUPPORTED_PLATFORM_TAGS:
                label_pyproject(arg0)
            else:
                raise RuntimeError(f"Platform tag {arg0} is not supported!")

        else:
            print("Usage: label_pyproject_with_platform_architecture.py platform_tag")
            print(f"Supported platform tags = {SUPPORTED_PLATFORM_TAGS}")
    except:  # noqa: E722 - do not use bare 'except' (auto-generated noqa)
        print(Fore.RED + "Failure: " + str(sys.exc_info()[0]))
        raise
    finally:
        print(Style.RESET_ALL)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/list_supported_venvs.py sha256=56c794b4b91e9de8a570e5ebbb1db38b2e100dd44c1e5877d23b74c64ab395f9 bytes=1077 -->
## FILE: scripts/list_supported_venvs.py

- repository: `ni/nipcbatt`
- source_path: `scripts/list_supported_venvs.py`
- sha256: `56c794b4b91e9de8a570e5ebbb1db38b2e100dd44c1e5877d23b74c64ab395f9`
- bytes: 1077

````python
"""Lists venvs variables environment"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (150 > 100 characters) (auto-generated noqa)

import venv_tools

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    venvs_entries = venv_tools.get_supported_venvs_paths_table()

    print("Supported venvs environ variables:")
    for venv_entry in zip(list(venvs_entries.items()), range(1, len(venvs_entries) + 1)):
        print(f" {venv_entry[1]}- os.env['{venv_entry[0][0]}'] = {venv_entry[0][1]}")

    print("----")
    print("Found venvs environ variables:")

    found_env_variables_list = list(venv_tools.get_python_present_env_variable_names())

    if not found_env_variables_list:
        print(" There is no configured python environ variable")

    for venv_entry in zip(found_env_variables_list, range(1, len(found_env_variables_list) + 1)):
        print(f" {venv_entry[1]}- os.env['{venv_entry[0][0]}'] = {venv_entry[0][1]}")
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/prepare_package_win32.py sha256=3b6f9ea9105b74b23671be5569be746e7b8a0b2ba182f6043c96690ed9586f70 bytes=3555 -->
## FILE: scripts/prepare_package_win32.py

- repository: `ni/nipcbatt`
- source_path: `scripts/prepare_package_win32.py`
- sha256: `3b6f9ea9105b74b23671be5569be746e7b8a0b2ba182f6043c96690ed9586f70`
- bytes: 3555

````python
"""Builds x86 native DLLs then copies them into python src structure"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import logging
import os
import subprocess
import sys
from pathlib import Path

import filesystem_utils
from varname import nameof

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent.parent

    logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)
    # build native code using x86 scripts
    build_script_path = os.path.join(
        repository_dir_path,
        "pcbatt.native",
        "scripts",
        "build_x86_release.bat",
    )

    if os.path.exists(build_script_path):
        # build cpp source files
        process_result = subprocess.run(
            args=[build_script_path],
            check=True,
        )

        # move x86 release DLLs into python src
        x86_dlls_source_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.native",
            "PCBATT.Native.Libraries",
            "Release",
        )

        x86_dlls_destination_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.python",
            "src",
            "nipcbatt",
            "pcbatt_analysis",
            "win32",
        )

        if os.path.exists(x86_dlls_source_folder_path):
            logging.debug("copy dlls folder: %s", x86_dlls_source_folder_path)

            # DLL 1
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.PCBATT.InteropApi.dll",
            )

            # DLL 2
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.PCBATT.Analysis.LabVIEW.dll",
            )

            # DLL 3
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.BasicDcRms.dll",
            )

            # DLL 4
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.AmplitudeAndLevels.dll",
            )

            # DLL 5
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.PulseMeasurements.dll",
            )

            # DLL 6
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.FFTSpectrumAmplitudePhase.dll",
            )

            # DLL 7
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.ExtractMultipleToneInformation.dll",
            )

        else:
            print(f"x86 dlls folder is not found: {x86_dlls_source_folder_path}")

    else:
        print(f"Script file is not found: {build_script_path}")
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/prepare_package_win_amd64.py sha256=e31d3ee1b037ddecc3718a712f7359227ca560e07965b8dd8452e8377a071e6e bytes=3579 -->
## FILE: scripts/prepare_package_win_amd64.py

- repository: `ni/nipcbatt`
- source_path: `scripts/prepare_package_win_amd64.py`
- sha256: `e31d3ee1b037ddecc3718a712f7359227ca560e07965b8dd8452e8377a071e6e`
- bytes: 3579

````python
"""Builds x64 native DLLs then copies them into python src structure"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import logging
import os
import subprocess
import sys
from pathlib import Path

import filesystem_utils
from varname import nameof

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent.parent

    logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)
    # build native code using x64 scripts
    build_script_path = os.path.join(
        repository_dir_path,
        "pcbatt.native",
        "scripts",
        "build_x64_release.bat",
    )

    if os.path.exists(build_script_path):
        # build cpp source files
        process_result = subprocess.run(
            args=[build_script_path],
            check=True,
        )

        # move x64 release DLLs into python src
        x64_dlls_source_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.native",
            "PCBATT.Native.Libraries",
            "x64",
            "Release",
        )

        x64_dlls_destination_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.python",
            "src",
            "nipcbatt",
            "pcbatt_analysis",
            "win_amd64",
        )

        if os.path.exists(x64_dlls_source_folder_path):
            logging.debug("copy dlls folder: %s", x64_dlls_source_folder_path)

            # DLL 1
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.PCBATT.InteropApi.dll",
            )

            # DLL 2
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.PCBATT.Analysis.LabVIEW.dll",
            )

            # DLL 3
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.LabVIEW.BasicDcRms.dll",
            )

            # DLL 4
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.LabVIEW.AmplitudeAndLevels.dll",
            )

            # DLL 5
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.LabVIEW.PulseMeasurements.dll",
            )

            # DLL 6
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.LabVIEW.FFTSpectrumAmplitudePhase.dll",
            )

            # DLL 7
            filesystem_utils.safe_copy_dll_file(
                x64_dlls_source_folder_path,
                x64_dlls_destination_folder_path,
                "NI.LabVIEW.ExtractMultipleToneInformation.dll",
            )

        else:
            print(f"x64 dlls folder is not found: {x64_dlls_source_folder_path}")

    else:
        print(f"Script file is not found: {build_script_path}")
````

<!--NI_OSS_SOURCE repo=nipcbatt path=scripts/run_unittests.py sha256=6bdd8e6a6577331380dfe177d80b1cb1f3174f3d33f30a929ea8b798e43ffea7 bytes=597 -->
## FILE: scripts/run_unittests.py

- repository: `ni/nipcbatt`
- source_path: `scripts/run_unittests.py`
- sha256: `6bdd8e6a6577331380dfe177d80b1cb1f3174f3d33f30a929ea8b798e43ffea7`
- bytes: 597

````python
"""Provides unit tests execution script."""

import logging
import subprocess
import sys
from pathlib import Path

from varname import nameof

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent
    tests_directory_path = repository_dir_path / "tests"

    logging.debug("%s = %s", nameof(tests_directory_path), tests_directory_path)

    process_result = subprocess.run(
        args=[sys.executable, "-m", "unittest", "discover", tests_directory_path],
        check=True,
    )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=SECURITY.md sha256=902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11 bytes=1330 -->
## FILE: SECURITY.md

- repository: `ni/nipcbatt`
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

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/__init__.py sha256=07b138e8407b5b2a9d8e3f65c208a19ff7746f219509a111f9a7c16fc8e907c6 bytes=4343 -->
## FILE: src/nipcbatt/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/__init__.py`
- sha256: `07b138e8407b5b2a9d8e3f65c208a19ff7746f219509a111f9a7c16fc8e907c6`
- bytes: 4343

````python
# pylint: disable=C0301
"""Provides a set of modules built on top of nidaqmx to perform PCBA electrical tests."""

# All classes inherited from PCBATestToolkitData, BuildingBlockUsingInstrument
# shall be imported here. By this way, the use of blocks in PCBA Test Toolkit
# is greatly facilitated. for that "import nipcbatt" imports all classes used
# for measurements, generations and device communications.
# Excample:
#
# import nipcbatt
#
# measurement = nipcbatt.DcRmsCurrentMeasurement()
# measurement.initialize()
# results = measurement.configure_and_measure(configuration=nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION)  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
# measurement.close()

from nipcbatt.pcbatt_library import daq
from nipcbatt.pcbatt_library import dmm
from nipcbatt.pcbatt_library import dcpower
from nipcbatt.pcbatt_library import communications
from nipcbatt.pcbatt_library import switch
from nipcbatt.pcbatt_library import dmm_scan
from nipcbatt.pcbatt_library import dcpower

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
    PCBATTAnalysisException,
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
    AmplitudeAndLevelsProcessingResult,
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingResult,
    DcRmsProcessingWindow,
    LabViewBasicDcRms,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumAmplitudePhase,
    LabViewFftSpectrumWindow,
    LabViewFrequencyDomainProcessing,
    LabViewMultipleTonesMeasurement,
    LabViewTonesSortingMode,
    MultipleTonesAmplitudePhaseSpectrumProcessingResult,
    MultipleTonesProcessingResult,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevels,
    PulseAnalogProcessingReferenceLevelsUnit,
    PulseAnalogProcessingResult,
    WaveformPeriodicityAnalogProcessingResult,
)
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    AmplitudeSpectrum,
    AnalogWaveform,
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)

from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
    BuildingBlockUsingVisa,
)

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryChannelNotCompatibleWithGenerationException,
    PCBATTLibraryChannelNotCompatibleWithMeasurementException,
    PCBATTLibraryException,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/docs/Migration Guide for nipcbatt 2.0.0.md sha256=cef1d3d32b0755a820eda89a3f06aa68b4a0cac3c103d37f0c7b01bf271e5b9e bytes=7089 -->
## FILE: src/nipcbatt/docs/Migration Guide for nipcbatt 2.0.0.md

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/docs/Migration Guide for nipcbatt 2.0.0.md`
- sha256: `cef1d3d32b0755a820eda89a3f06aa68b4a0cac3c103d37f0c7b01bf271e5b9e`
- bytes: 7089

````markdown
# Migration Guide for nipcbatt 2.0.0

## Overview: Breaking Change in 2.0.0

nipcbatt 2.0.0 introduces a **breaking change**: all classes must now be imported from **instrument-specific subpackages** instead of the top-level `nipcbatt` namespace.

### Organization by Instrument Type
- **`nipcbatt.daq`** — DAQmx-based generation/measurement (voltage, digital, temperature)
- **`nipcbatt.dmm`** — NI-DMM digital multimeter measurements
- **`nipcbatt.switch`** — NI-SWITCH relay control
- **`nipcbatt.dmm_scan`** — Multi-channel DMM + SWITCH scanning
- **`nipcbatt.communications`** — I2C, SPI, Serial communication

This change makes dependencies explicit and prevents naming conflicts.

---

## Quick Migration: Before and After

### ❌ Old format (Broken in 2.x)
```python
import nipcbatt

gen = nipcbatt.DcVoltageGeneration()
meas = nipcbatt.TimeDomainMeasurement()
dmm = nipcbatt.DcRmsVoltageMeasurement()
config = nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

### ✅ Fix Required (2.x Onwards)
```python
from nipcbatt import daq, dmm

gen = daq.DcVoltageGeneration()
meas = daq.TimeDomainMeasurement()
dmm_meas = dmm.DcRmsVoltageMeasurement()
config = daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

---

## Common Migration Patterns

### DAQ: Generation and Measurement

| Module | Before 2.x | 2.x Onwards |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import daq` |
| **DC Voltage Generation** | `nipcbatt.DcVoltageGeneration()` | `daq.DcVoltageGeneration()` |
| **Signal Voltage Generation** | `nipcbatt.SignalVoltageGeneration()` | `daq.SignalVoltageGeneration()` |
| **DC RMS Voltage Measurement** | `nipcbatt.DcRmsVoltageMeasurement()` | `daq.DcRmsVoltageMeasurement()` |
| **DC RMS Current Measurement** | `nipcbatt.DcRmsCurrentMeasurement()` | `daq.DcRmsCurrentMeasurement()` |
| **Time Domain Measurement** | `nipcbatt.TimeDomainMeasurement()` | `daq.TimeDomainMeasurement()` |
| **Frequency Domain Measurement** | `nipcbatt.FrequencyDomainMeasurement()` | `daq.FrequencyDomainMeasurement()` |
| **Temperature Measurement** | `nipcbatt.TemperatureMeasurement()` | `daq.TemperatureMeasurement()` |
| **Power Supply Source and Measure** | `nipcbatt.PowerSupplySourceAndMeasure()` | `daq.PowerSupplySourceAndMeasure()` |
| **Digital PWM Measurement** | `nipcbatt.DigitalPwmMeasurement()` | `daq.DigitalPwmMeasurement()` |
| **Digital Clock Generation** | `nipcbatt.DigitalClockGeneration()` | `daq.DigitalClockGeneration()` |
| **Digital Pulse Generation** | `nipcbatt.DigitalPulseGeneration()` | `daq.DigitalPulseGeneration()` |
| **Static Digital State Generation** | `nipcbatt.StaticDigitalStateGeneration()` | `daq.StaticDigitalStateGeneration()` |
| **Static Digital State Measurement** | `nipcbatt.StaticDigitalStateMeasurement()` | `daq.StaticDigitalStateMeasurement()` |
| **Dynamic Digital Pattern Generation** | `nipcbatt.DynamicDigitalPatternGeneration()` | `daq.DynamicDigitalPatternGeneration()` |
| **Dynamic Digital Pattern Measurement** | `nipcbatt.DynamicDigitalPatternMeasurement()` | `daq.DynamicDigitalPatternMeasurement()` |
| **Default Config** | `nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` | `daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` |


### Communications: I2C, SPI, and Serial

| Module | Before 2.x | 2.x Onwards |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import communications as comm` |
| **I2C Read** | `nipcbatt.I2cReadCommunication()` | `comm.I2cReadCommunication()` |
| **I2C Write** | `nipcbatt.I2cWriteCommunication()` | `comm.I2cWriteCommunication()` |
| **SPI Read** | `nipcbatt.SpiReadCommunication()` | `comm.SpiReadCommunication()` |
| **SPI Write** | `nipcbatt.SpiWriteCommunication()` | `comm.SpiWriteCommunication()` |
| **Serial** | `nipcbatt.SerialCommunication()` | `comm.SerialCommunication()` |
| **I2C Default Config** | `nipcbatt.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION` | `comm.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION` |
| **SPI Default Config** | `nipcbatt.DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION` | `comm.DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION` |

---

## What Still Works: Backward Compatibility Exceptions

Some core utilities and exceptions remain directly accessible from `nipcbatt` for backward compatibility, for example:

```python
from nipcbatt import (
    # Core exceptions (still available)
    PCBATTLibraryException,
    PCBATTAnalysisException,
    PCBATTCommunicationException,
    
    # Core data types (still available)
    PCBATestToolkitData,
    MeasurementOptions,
    MeasurementExecutionType,
    MeasurementAnalysisRequirement,
    
    # Building blocks (still available)
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
    BuildingBlockUsingVisa,
)
```

However, **all measurement, generation, and communication classes MUST use instrument-specific imports.** refer "src\nipcbatt\__init__.py" for more info on available methods from nipcbatt.

---

## Best Practices

1. **Use explicit module imports** to make dependencies clear
2. **Use module aliases** for readability: `from nipcbatt import communications as comm`
3. **Handle name collisions** explicitly: `daq.DcRmsVoltageMeasurement()` vs. `dmm.DcRmsVoltageMeasurement()`
4. **Group related imports** for organization
5. **Never use** `from nipcbatt.daq import *` — be explicit about what you import

---

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ImportError: cannot import name 'DcVoltageGeneration' from 'nipcbatt'` | Using top-level import | Use `from nipcbatt.daq import DcVoltageGeneration` |
| `AttributeError: module 'nipcbatt' has no attribute 'DcRmsVoltageMeasurement'` | Wrong import path | Use `from nipcbatt import daq` then `daq.DcRmsVoltageMeasurement()` |
| Cannot find configuration constant | Constants moved to submodules | Use `daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` |
| Name collision between `daq` and `dmm` versions | Same class name in multiple modules | Be explicit: `daq.DcRmsVoltageMeasurement()` vs. `dmm.DcRmsVoltageMeasurement()` |

---

## Import Reference

```python
# DAQmx
from nipcbatt import daq
gen = daq.DcVoltageGeneration()
meas = daq.TimeDomainMeasurement()

# DMM
from nipcbatt import dmm
volt_meas = dmm.DcRmsVoltageMeasurement()
res_meas = dmm.DcRmsResistanceMeasurement()

# Switch
from nipcbatt import switch
relay = switch.StaticDigitalPathGeneration()

# Communications
from nipcbatt import communications as comm
i2c = comm.I2cReadCommunication()
serial = comm.SerialCommunication()

# DMM Scan
from nipcbatt import dmm_scan
scan = dmm_scan.DmmScanPMPS()
```

---

## Migration Checklist

- Update all `import nipcbatt` to `from nipcbatt import <module>`
- Update all class instantiations to use module prefix
- Update all default configuration imports
- Verify backward-compatible exceptions still import from `nipcbatt`
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/__init__.py sha256=f09cee1107263b17a41ac7f050fa16c2361b0a26300f1af33e0e0d21c7ab2347 bytes=472 -->
## FILE: src/nipcbatt/pcbatt_analysis/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/__init__.py`
- sha256: `f09cee1107263b17a41ac7f050fa16c2361b0a26300f1af33e0e0d21c7ab2347`
- bytes: 472

````python
"""Provides a set of measurement analysis modules using LabVIEW libraries 
and python written functions"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (324 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/__init__.py sha256=461fbd12f09112505cde0b9e5ca0d5946944f71d8e8ba170fc3d8e0363ee7b35 bytes=240 -->
## FILE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/__init__.py`
- sha256: `461fbd12f09112505cde0b9e5ca0d5946944f71d8e8ba170fc3d8e0363ee7b35`
- bytes: 240

````python
"""Provides private modules of pcbatt_analysis package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_info.py sha256=e73cfc1b72c780a3af8ba0854e0205190753ebe29b0a6c344df51ae85e42e8da bytes=10237 -->
## FILE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_info.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_info.py`
- sha256: `e73cfc1b72c780a3af8ba0854e0205190753ebe29b0a6c344df51ae85e42e8da`
- bytes: 10237

````python
"""Provides private functions of analysis_library_info module."""

from ctypes import POINTER, byref, c_char_p, c_int, c_size_t, create_string_buffer

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)

NATIVE_FUNCTION_GET_LIBRARY_VERSION = "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion"

NATIVE_FUNCTION_IS_LABVIEW_RUNTIME_AVAILABLE = (
    "NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable"
)

NATIVE_FUNCTION_ARE_TRACES_ENABLED = "NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled"

NATIVE_FUNCTION_ENABLE_TRACES = "NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces"


def get_labview_analysis_traces_folder_path_impl() -> str:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' fails for some reason.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath.argtypes = [
            # char* path output
            c_char_p,
            # size_t path length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath"
        ) from e


def call_interop_api_labview_analysis_enable_traces(traces_status: bool) -> None:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' fails for some reason.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces.argtypes = [c_int]

        # call native code
        traces_status_in = c_int()

        if traces_status is True:
            traces_status_in = c_int(1)
        else:
            traces_status_in = c_int(0)

        return_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces(
            traces_status_in
        )

        if return_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + f"{NATIVE_FUNCTION_ENABLE_TRACES}, status code = {return_status}"
            )

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_ENABLE_TRACES}"
        ) from e


def call_interop_api_labview_analysis_are_traces_enabled() -> bool:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' fails for some reason.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled.argtypes = [
            POINTER(c_int)
        ]

        # call native code
        traces_status_out = c_int()

        return_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled(
            byref(traces_status_out)
        )

        if return_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + f"{NATIVE_FUNCTION_ARE_TRACES_ENABLED}, status code = {return_status}"
            )

        return traces_status_out.value > 0
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_ARE_TRACES_ENABLED}"
        ) from e


def call_interop_api_labview_analysis_lv_runtime_available():
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' fails for some reason.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable.argtypes = []

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable()

        return res_status == 0
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_IS_LABVIEW_RUNTIME_AVAILABLE}"
        ) from e


def call_interop_api_labview_analysis_get_library_version():
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' located in DLL
       'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' fails for some reason.

    Returns:
        tuple[Any, int, int, int, int]: status code and library version numbers.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion.argtypes = [
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]

        # call native code
        major_number_out = c_int()
        minor_number_out = c_int()
        patch_number_out = c_int()
        build_number_out = c_int()

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion(
            byref(major_number_out),
            byref(minor_number_out),
            byref(patch_number_out),
            byref(build_number_out),
        )

        return (
            res_status,
            major_number_out.value,
            minor_number_out.value,
            patch_number_out.value,
            build_number_out.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_GET_LIBRARY_VERSION}"
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_interop.py sha256=dcd35781a255e0695c4db21626e2ffd11faad62a6ba5b999cd8a3720daaf63aa bytes=1534 -->
## FILE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_interop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_interop.py`
- sha256: `dcd35781a255e0695c4db21626e2ffd11faad62a6ba5b999cd8a3720daaf63aa`
- bytes: 1534

````python
"""Provides private module of native interop helper functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

import os
from ctypes import CDLL, cdll

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def load_windows_shared_library_entries(native_library_path: str) -> CDLL:
    """Load content of DLL file into CDLL object

    Args:
        native_library_path (str): path into window file dll.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException: Occurs when loading
        of shared library fails for some reason.

    Returns:
        CDLL: An object holding windows shared library entries.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    try:
        dll_entries = cdll.LoadLibrary(native_library_path)
        # print(dll_entries)
        return dll_entries
    except Exception as e:
        raise PCBATTAnalysisLoadNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_LOAD_FAILED}"
            + f"{os.path.basename(native_library_path)}: {str(e)}"
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_exceptions.py sha256=dd50197b8b2793e9dff61865cfa5b3601249b7fbc89fbbb3802a6db5c37b36a7 bytes=1952 -->
## FILE: src/nipcbatt/pcbatt_analysis/analysis_library_exceptions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/analysis_library_exceptions.py`
- sha256: `dd50197b8b2793e9dff61865cfa5b3601249b7fbc89fbbb3802a6db5c37b36a7`
- bytes: 1952

````python
"""Defines a set of exceptions that can be raised by analysis module."""


class PCBATTAnalysisException(  # noqa: N818 - exception name 'PCBATTAnalysisException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by nipcatt.pcbatt_analysis modules."""

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)


class PCBATTAnalysisLoadNativeLibraryFailedException(  # noqa: N818 - exception name 'PCBATTAnalysisLoadNativeLibraryFailedException' should be named with an Error suffix (auto-generated noqa)
    PCBATTAnalysisException
):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when loading native library file fails for any reason."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (354 > 100 characters) (auto-generated noqa)


class PCBATTAnalysisCallNativeLibraryFailedException(  # noqa: N818 - exception name 'PCBATTAnalysisCallNativeLibraryFailedException' should be named with an Error suffix (auto-generated noqa)
    PCBATTAnalysisException
):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when calling native library function fails for any reason."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_info.py sha256=4c5cb07b6a83ba7754aed50c92dbdec2805d50e5c6f0064fe36ac4b711200ba8 bytes=2846 -->
## FILE: src/nipcbatt/pcbatt_analysis/analysis_library_info.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/analysis_library_info.py`
- sha256: `4c5cb07b6a83ba7754aed50c92dbdec2805d50e5c6f0064fe36ac4b711200ba8`
- bytes: 2846

````python
"""Defines pcbatt analysis library information elements."""

import logging

from nipcbatt.pcbatt_analysis._pcbatt_analysis_internal import _analysis_library_info
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def get_labview_analysis_traces_folder_path() -> str:
    """Gets the path of traces produced by analysis library.

    Returns:
        str: string path.
    """
    return _analysis_library_info.get_labview_analysis_traces_folder_path_impl()


def is_labview_runtime_available() -> bool:
    """Indicates if current machine has labview runtime available.

    Returns:
        bool: True, labview runtime is available elsewhere it returns False.
    """
    return _analysis_library_info.call_interop_api_labview_analysis_lv_runtime_available()


def are_traces_enabled() -> bool:
    """Indicates whether current analysis library traces are enabled or not.

    Returns:
        bool: True, traces are enabled elsewhere it returns False.
    """
    return _analysis_library_info.call_interop_api_labview_analysis_are_traces_enabled()


def enable_traces(traces_status: bool) -> None:
    """Forces current analysis library to produce traces.

    Args:
        trace_status (bool): True, verbose traces are recorded, False, no traces are recorded.
    """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
    _analysis_library_info.call_interop_api_labview_analysis_enable_traces(traces_status)


def get_labview_analysis_available_functions_names_list() -> list[str]:
    """Gets the list of exported labview functions."""
    return ["BasicDcRms"]


def get_labview_analysis_library_version_numbers() -> tuple[int, int, int, int]:
    """Gets the version information elements of labview analysis library."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)

    logging.debug("current script path = %s", __file__)

    call_result_tuple = (
        _analysis_library_info.call_interop_api_labview_analysis_get_library_version()
    )

    # handle status code returned by native code
    if call_result_tuple[0] == 0:
        return (
            call_result_tuple[1],
            call_result_tuple[2],
            call_result_tuple[3],
            call_result_tuple[4],
        )
    else:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}: "
            + _analysis_library_info.NATIVE_FUNCTION_GET_LIBRARY_VERSION
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_interop.py sha256=bc98ae04d32d4f58d400359403d62be18cb26f59b3d6932a7a57f86d42267701 bytes=4855 -->
## FILE: src/nipcbatt/pcbatt_analysis/analysis_library_interop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/analysis_library_interop.py`
- sha256: `bc98ae04d32d4f58d400359403d62be18cb26f59b3d6932a7a57f86d42267701`
- bytes: 4855

````python
"""Provides a set of function helpers for native interop usage."""

import os
import platform
from ctypes import CDLL
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_analysis._pcbatt_analysis_internal import _analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_utilities import platform_utilities


def get_native_libraries_folder_name_for_windows() -> str:
    """Gets the name of folder containing native libraries when running
       on windows operating system.

    Raises:
        RuntimeError: Occurs when executing envrionment is not supported by current
        analysis library.

    Returns:
        str: folder name containing native libraries, win_amd64 or win32.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if platform_utilities.is_python_windows_64bits():
        return "win_amd64"

    if platform_utilities.is_python_windows_32bits():
        return "win32"

    raise RuntimeError(
        f"{AnalysisLibraryExceptionMessage.NATIVE_INTEROP_IS_NOT_SUPPORTED_ON_CURRENT_PLATFORM}:"
        + f"{platform.architecture()}"
    )


def load_interop_api_library_entries() -> CDLL:
    """Loads content of 'NI.PCBATT.InteropApi.dll' into a CDLL object
       that can be used to perform dynamic function invokation.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException:
        occurs when loading interop api entries fails for some reason.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    native_libraries_folder_name = get_native_libraries_folder_name_for_windows()

    # entry point DLL
    entry_point_dll_path = os.path.join(
        Path(__file__).parent, native_libraries_folder_name, "NI.PCBATT.InteropApi.dll"
    )

    # labview wrapper DLL
    analysis_labview_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.PCBATT.Analysis.LabVIEW.dll",
    )

    # VIs DLL
    analysis_labview_basic_dc_rms_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.BasicDcRms.dll",
    )

    analysis_labview_amplitude_and_levels_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.AmplitudeAndLevels.dll",
    )

    analysis_labview_pulse_measurements_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.PulseMeasurements.dll",
    )

    analysis_labview_fft_spectrum_mag_phase_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.FFTSpectrumAmplitudePhase.dll",
    )

    analysis_labview_multitones_measurements_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.ExtractMultipleToneInformation.dll",
    )

    required_dlls_paths = [
        entry_point_dll_path,
        analysis_labview_dll_path,
        analysis_labview_basic_dc_rms_dll_path,
        analysis_labview_amplitude_and_levels_dll_path,
        analysis_labview_pulse_measurements_dll_path,
        analysis_labview_fft_spectrum_mag_phase_dll_path,
        analysis_labview_multitones_measurements_dll_path,
    ]

    required_dlls_files_names = ", ".join(
        map(lambda file_path: f"'{os.path.basename(file_path)}'", required_dlls_paths)
    )

    # Check existence of dll files
    if any(map(lambda dll_path: not os.path.exists(dll_path), required_dlls_paths)):
        raise PCBATTAnalysisLoadNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_IS_MISSING}: "
            + f"{nameof(required_dlls_paths)} = {required_dlls_paths}"
            + os.linesep
            + os.linesep
            + f"{nameof(required_dlls_files_names)} = {required_dlls_files_names}"
        )

    dll_entries = _analysis_library_interop.load_windows_shared_library_entries(
        entry_point_dll_path
    )

    return dll_entries
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_messages.py sha256=8ed5a013c387a88016bf40ff90e125f3920b2148bf4c5288074cbb25a761612c bytes=2262 -->
## FILE: src/nipcbatt/pcbatt_analysis/analysis_library_messages.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/analysis_library_messages.py`
- sha256: `8ed5a013c387a88016bf40ff90e125f3920b2148bf4c5288074cbb25a761612c`
- bytes: 2262

````python
"""Defines analysis library different kinds of messages."""

import dataclasses


@dataclasses.dataclass
class AnalysisLibraryExceptionMessage:
    """Defines analysis library exceptions messages content."""

    NATIVE_LIBRARY_LOAD_FAILED = "Failed to load native library"
    NATIVE_LIBRARY_FUNCTION_CALL_FAILED = "Failed to call function of native library"
    NATIVE_LIBRARY_IS_MISSING = "Native libray element is missing"
    NATIVE_INTEROP_IS_NOT_SUPPORTED_ON_CURRENT_PLATFORM = (
        "Native interop is not supported for current platform"
    )

    DC_RMS_PROCESSING_FAILED_FOR_SOME_REASON = "DC-RMS processing failed for some reason!"

    AMPLITUDE_AND_LEVELS_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Amplitude and levels processing failed for some reason!"
    )

    AMPLITUDE_AND_PHASE_SPECTRUM_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Amplitude and phase spectrum processing failed for some reason!"
    )

    FREQUENCY_DOMAIN_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Frequency domain processing failed for some reason!"
    )

    MULTIPLE_TONES_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Multiple tones processing failed for some reason!"
    )

    PULSE_MEASUREMENTS_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Pulse measurements processing failed for some reason!"
    )

    PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_IS_NOT_SUPPORTED = (
        "Pulse measurements processing does not support selected reference levels unit!"
    )

    PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_PERCENT_REQUIRES_STATES_SETTINGS = (
        "Pulse measurements processing using reference levels in percent requires states settings!"
    )

    SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = "Sine waveform creation failed for some reason!"

    SQUARE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = (
        "Square waveform creation failed for some reason!"
    )

    MULTIPLE_TONES_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = (
        "Multi-tones waveform creation failed for some reason!"
    )

    SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON = (
        "Scale and offset waveform transformations failed for some reason!"
    )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/common/base_types.py sha256=2826fa14fedda033a502408ed17f12d38df4984771cbe00c85e340f93ce971f4 bytes=1465 -->
## FILE: src/nipcbatt/pcbatt_analysis/common/base_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/common/base_types.py`
- sha256: `2826fa14fedda033a502408ed17f12d38df4984771cbe00c85e340f93ce971f4`
- bytes: 1465

````python
"""Holds base types of the package nipcbatt.pcbatt_analysis"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import json

from nipcbatt.pcbatt_utilities.reflection_utilities import (
    convert_for_json_serialization,
)


class AnalysisLibraryElement:
    """Defines base class of analysis library elements."""

    def __repr__(self) -> str:
        """Called when repr() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: JSON string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        return json.dumps(
            convert_for_json_serialization(self),
            indent=4,
        ).replace("\\n", "\n")

    def __str__(self) -> str:
        """Called when str() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: line string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        cls = self.__class__
        return f"<{cls.__module__}.{cls.__qualname__} object at {id(self)}>"
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/common/common_types.py sha256=63901b53d602d5a87a2196d56eca3a366138f1c6be120e15e5ed882c565de78b bytes=9285 -->
## FILE: src/nipcbatt/pcbatt_analysis/common/common_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/common/common_types.py`
- sha256: `63901b53d602d5a87a2196d56eca3a366138f1c6be120e15e5ed882c565de78b`
- bytes: 9285

````python
"""Holds common types of the package nipcbatt.pcbatt_analysis"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

import math
from enum import IntEnum

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpectrumPhaseUnit(IntEnum):
    """Defines all supported phase units of `fft spectrum processing`"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)

    RADIAN = 0
    "Default unit, radian"

    DEGREE = 1
    "Degree"


class SpectrumAmplitudeType(IntEnum):
    """Defines all supported amplitude kinds of `fft spectrum processing`"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)

    PEAK = 0
    """`Peak` amplitude, ie, sqrt(2) * magnitude spectrum"""
    RMS = 1
    """`RMS` amplitude, ie, magnitude spectrum"""


class AmplitudePhaseSpectrum(AnalysisLibraryElement):
    """Defines Amplitude and phase spectrum processing results,
    amplitude can be `PEAK` or `RMS`"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (332 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        f0: float,
        df: float,
        frequencies_amplitudes: numpy.ndarray[float],
        spectrum_amplitude_type: SpectrumAmplitudeType,
        spectrum_amplitude_unit_is_db: bool,
        frequencies_phases: numpy.ndarray[float],
        spectrum_phase_unit: SpectrumPhaseUnit,
    ) -> None:
        """Initialize an instance of `AmplitudePhaseSpectrum`.

        Args:
            f0 (`float`): start frequency of the spectrum.
            df (`float`): frequency resolution of the spectrum.
            frequencies_amplitudes (`numpy.ndarray[float]`): amplitudes of the spectrum.
            spectrum_amplitude_type (`SpectrumAmplitudeType`): spectrum amplitude type.
            spectrum_amplitude_unit_is_db (`bool`): spectrum amplitude is expressed as gain (db).
            frequencies_phases (`numpy.ndarray[float]`):phases of the spectrum.
            spectrum_phase_unit(`SpectrumPhaseUnit`): unit of the spectrum phases.

        Raises:
            ValueError: occurs when input arrays `frequencies_amplitudes`,
            `frequencies_phases` are none or empty.
            occurs when `f0` is less than zero, `df` is less or equal zero.
            occurs when `frequencies_amplitudes` and `frequencies_phases` have not same size.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        Guard.is_greater_than_or_equal_to_zero(f0, nameof(f0))
        Guard.is_greater_than_zero(df, nameof(df))

        Guard.is_not_none(frequencies_amplitudes, nameof(frequencies_amplitudes))
        Guard.is_not_empty(frequencies_amplitudes, nameof(frequencies_amplitudes))

        Guard.is_not_none(frequencies_phases, nameof(frequencies_phases))
        Guard.is_not_empty(frequencies_phases, nameof(frequencies_phases))

        Guard.have_same_size(
            first_iterable_instance=frequencies_amplitudes,
            first_iterable_name=nameof(frequencies_amplitudes),
            second_iterable_instance=frequencies_phases,
            second_iterable_name=nameof(frequencies_phases),
        )

        self._spectrum_start_frequency = f0
        self._spectrum_frequency_resolution = df
        self._spectrum_amplitudes = frequencies_amplitudes
        self._spectrum_amplitude_type = spectrum_amplitude_type
        self._spectrum_amplitude_unit_is_db = spectrum_amplitude_unit_is_db
        self._spectrum_phases = frequencies_phases
        self._spectrum_phase_unit = spectrum_phase_unit

    @property
    def spectrum_start_frequency(self) -> float:
        """Gets spectrum start frequency.

        Returns:
            float: start element of the frequency range.
        """
        return self._spectrum_start_frequency

    @property
    def spectrum_frequency_resolution(self) -> float:
        """Gets spectrum frequency resolution.

        Returns:
            float: resolution of the frequency range.
        """
        return self._spectrum_frequency_resolution

    @property
    def spectrum_frequencies(self) -> numpy.ndarray[float]:
        """Gets the array of frequencies axis of spectrum.

        Returns:
            `numpy.ndarray[float]`: X axis of the spectrum.
        """
        frequency_bins_count = self._spectrum_amplitudes.size

        frequencies_array = numpy.fromiter(
            map(
                lambda frequency_bin_index: self.spectrum_start_frequency
                + frequency_bin_index * self._spectrum_frequency_resolution,
                range(0, frequency_bins_count),
            ),
            dtype=float,
        )

        return frequencies_array

    @property
    def spectrum_amplitudes(self) -> numpy.ndarray[float]:
        """Gets the array of amplitude axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the amplitude spectrum.
        """
        return self._spectrum_amplitudes

    @property
    def spectrum_phases(self) -> numpy.ndarray[float]:
        """Gets the array of phases axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the phase spectrum.
        """
        return self._spectrum_phases

    @property
    def spectrum_amplitude_unit_is_db(self) -> bool:
        """Gets a boolean indicating if spectrum amplitudes are expressed in db.

        Returns:
            bool: True if amplitudes are expressed in db.
        """
        return self._spectrum_amplitude_unit_is_db

    @property
    def spectrum_amplitude_type(self) -> SpectrumAmplitudeType:
        """Gets an enumeration value indicating kind of the spectrum amplitudes,
        `RMS` or `PEAK`.

        Returns:
            SpectrumAmplitudeType:
            `RMS`, spectrum amplitudes are RMS amplitude ie complexe magnitude,
            `PEAK` spectrum amplitudes are PEAK amplitude ie sqrt(2) * RMS amplitude
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._spectrum_amplitude_type

    @property
    def spectrum_phase_unit(self) -> SpectrumPhaseUnit:
        """Gets an enumeration value indicating unit of the spectrum phases.

        Returns:
            SpectrumPhaseUnit: `RADIAN` or `DEGREE`
        """
        return self._spectrum_phase_unit


class WaveformTone(AnalysisLibraryElement):
    """Defines waveform tone characteristics."""

    def __init__(
        self,
        frequency: float,
        amplitude: float,
        phase_radians: float,
    ) -> None:
        """Initialize an instance of `WaveformTone`.

        Raises:
            ValueError: occurs when frequency is less or equal zero,
                and occurs when amplitude is less or equal zero.

        Args:
            frequency (float): tone frequency, must be greater than zero.
            amplitude (float): tone amplitude, must be greater than zero.
            phase_radians (float): tone phase, in radians.
        """
        Guard.is_greater_than_zero(amplitude, nameof(amplitude))
        Guard.is_greater_than_zero(frequency, nameof(frequency))

        self._amplitude = amplitude
        self._frequency = frequency
        self._phase_radians = phase_radians

    @property
    def frequency(self) -> float:
        """Gets the frequency of the tone."""
        return self._frequency

    @property
    def amplitude(self) -> float:
        """Gets the amplitude of the tone."""
        return self._amplitude

    @property
    def phase_radians(self) -> float:
        """Gets waveform tone phase expressed in radian"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        return self._phase_radians

    @property
    def phase_degrees(self) -> float:
        """Gets waveform tone phase expressed in degree"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        return math.degrees(self.phase_radians)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/__init__.py sha256=2c980d74f487f9641a22e34e917ca336640ada2e97ee22a6eb0a8f4d6528cea8 bytes=469 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/__init__.py`
- sha256: `2c980d74f487f9641a22e34e917ca336640ada2e97ee22a6eb0a8f4d6528cea8`
- bytes: 469

````python
"""Provides a set of waveform analysis modules using LabVIEW libraries 
and python written functions"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (324 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/__init__.py sha256=3d0f561cbf23a1a6379f001679da7491ee0f43090d7d02bbe6518c9813b8cd32 bytes=242 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/__init__.py`
- sha256: `3d0f561cbf23a1a6379f001679da7491ee0f43090d7d02bbe6518c9813b8cd32`
- bytes: 242

````python
"""Provides private modules of waveform analysis package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_amplitude_and_levels_analysis.py sha256=5ceaafd0cad7e9dbf3dd9b75b19b1f0a7b18ade5df01b2d9851cf8228515137b bytes=7633 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_amplitude_and_levels_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_amplitude_and_levels_analysis.py`
- sha256: `5ceaafd0cad7e9dbf3dd9b75b19b1f0a7b18ade5df01b2d9851cf8228515137b`
- bytes: 7633

````python
"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (365 > 100 characters) (auto-generated noqa)

from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def labview_get_last_error_message_impl() -> str:
    """Gets last error message hold by labview Amplitude and Levels VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_amplitude_and_levels_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    amplitude_and_levels_processing_method: int,
    histogram_size: int,
) -> tuple[float, float, float]:
    """Invokes native library Amplitude and Levels processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native dll call fails for some reason.

    Returns:
        tuple[float, float, float]: Tuple gathering, amplitude, high state and low state levels.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int histogramSize,
    # const double* inputWaveformSamplesArray,
    # double* outputProcessedAmplitudeValue,
    # double* outputProcessedHighStateLevelValue,
    # double* outputProcessedLowStateLevelValue)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int histogramSize
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputProcessedAmplitudeValue
            POINTER(c_double),
            # double* outputProcessedHighStateLevelValue
            POINTER(c_double),
            # double* outputProcessedLowStateLevelValue
            POINTER(c_double),
        ]

        # call native code
        amplitude_value_out = c_double()
        high_state_level_value_out = c_double()
        low_state_level_value_out = c_double()

        amplitude_and_levels_processing_method_in = c_int(amplitude_and_levels_processing_method)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))
        histogram_size_in = c_int(histogram_size)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement(
            amplitude_and_levels_processing_method_in,
            waveform_sampling_period_in,
            waveform_length_in,
            histogram_size_in,
            waveform_samples_array_in,
            byref(amplitude_value_out),
            byref(high_state_level_value_out),
            byref(low_state_level_value_out),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        return (
            amplitude_value_out.value,
            high_state_level_value_out.value,
            low_state_level_value_out.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement"
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_dc_rms_analysis.py sha256=94a7636ec67c7cea23b0afd638af0ce09893a2a1cf3750091e28700f34a8749f bytes=6835 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_dc_rms_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_dc_rms_analysis.py`
- sha256: `94a7636ec67c7cea23b0afd638af0ce09893a2a1cf3750091e28700f34a8749f`
- bytes: 6835

````python
"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.dc_rms_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (351 > 100 characters) (auto-generated noqa)

from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def labview_get_last_error_message_impl() -> str:
    """Gets last error message hold by labview DC-RMS VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: occurs when native call fails for some reason.

    Returns:
        str: last error message
    """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_dc_rms_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    dc_rms_processing_window: int,
) -> tuple[float, float]:
    """Invokes native library DC-RMS processing LabVIEW VI.

    Args:
        dc_rms_processing_window (int): 0 for Rectangular, 1 for Hann or 2 for LowSideLobe.
        waveform_samples (numpy.ndarray[float]): An array of 64bites floating points
        that will be passed to native code library.
        waveform_sampling_period_seconds (float): Sampling period of the input array of samples.

    Returns:
        tuple[float, float]: DC value and RMS value gathered in a tuple.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement(
    # DcRmsProcessingWindowEnum inputDcRmsProcessingWindow,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputProcessedDcValue,
    # double* outputProcessedRmsValue)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement.argtypes = [
            # DcRmsProcessingWindowEnum inputDcRmsProcessingWindow
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputProcessedDcValue
            POINTER(c_double),
            # double* outputProcessedRmsValue
            POINTER(c_double),
        ]

        # call native code
        dc_value_out = c_double()
        rms_value_out = c_double()

        dc_rms_processing_window_in = c_int(dc_rms_processing_window)
        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        res_status = (
            dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement(
                dc_rms_processing_window_in,
                waveform_sampling_period_in,
                waveform_length_in,
                waveform_samples_array_in,
                byref(dc_value_out),
                byref(rms_value_out),
            )
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        return (dc_value_out.value, rms_value_out.value)
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement"
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_frequency_domain_analysis.py sha256=09710872090edfa15d676fae51b0b90da129d3c40c13274ba3e04a1b05149c0a bytes=23950 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_frequency_domain_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_frequency_domain_analysis.py`
- sha256: `09710872090edfa15d676fae51b0b90da129d3c40c13274ba3e04a1b05149c0a`
- bytes: 23950

````python
"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.frequency_domain_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (361 > 100 characters) (auto-generated noqa)

import math
from ctypes import (
    POINTER,
    byref,
    c_bool,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy
import scipy.signal

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_transformation import scale_and_offset_waveform


def labview_multiple_tones_measurement_get_last_error_message_impl() -> str:
    """Gets LabVIEW VI last error message."""
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage"
        ) from e


def labview_fft_spectrum_amplitude_phase_get_last_error_message_impl() -> str:
    """Gets LabVIEW VI last error message."""
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_amplitude_phase_spectrum_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    spectrum_amplitude_must_be_db: bool,
    spectrum_amplitude_type: SpectrumAmplitudeType,
    spectrum_phase_unit: SpectrumPhaseUnit,
    fft_spectrum_window: int,
    fft_spectrum_window_advanced_parameter: float = None,
) -> AmplitudePhaseSpectrum:
    """Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
        be expressed as db gain, instead of nominal unit.
        spectrum_amplitude_type (`FftSpectrumAmplitudeType`): can be `RMS` or `PEAK`.
        spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
        fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
        fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
        only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.

    Raises:
        PCBATTAnalysisException:
            Occurs when multiple tones processing fails for some reason.

    Returns:
        AmplitudePhaseSpectrum: An object that holds result of fft spectrum
        processing result using LabVIEW VI.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement(
    # FftSpectrumWindowEnum inputFftWindow,
    # bool inputViewSettingsAmplitudeUnitIsdDb,
    # bool inputViewSettingsPhaseMustUnwrap,
    # bool inputViewSettingsPhaseUnitIsDegree,
    # double inputAdvancedFftWindowParameter,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputSpectrumResolution,
    # double* outputSpectrumStartFrequency,
    # double* outputSpectrumEndFrequency,
    # double* outputSpectrumMagnitudesArray,
    # double* outputSpectrumPhasesArray);
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement.argtypes = [
            # FftSpectrumWindowEnum inputFftWindow
            c_int,
            # bool inputViewSettingsAmplitudeUnitIsdDb
            c_bool,
            # inputViewSettingsPhaseMustUnwrap
            c_bool,
            # bool inputViewSettingsPhaseUnitIsDegree
            c_bool,
            # double inputAdvancedFftWindowParameter
            c_double,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputSpectrumResolution,
            POINTER(c_double),
            # double* outputSpectrumStartFrequency,
            POINTER(c_double),
            # double* outputSpectrumEndFrequency,
            POINTER(c_double),
            # double* outputSpectrumMagnitudesArray,
            POINTER(c_double),
            # double* outputSpectrumPhasesArray
            POINTER(c_double),
        ]

        # fill function arguements
        input_fft_window = c_int(fft_spectrum_window)
        input_view_settings_amplitude_unit_isd_db = c_bool(spectrum_amplitude_must_be_db)

        input_view_settings_phase_must_unwrap = c_bool(False)
        input_view_settings_phase_unit_is_degree = c_bool(
            spectrum_phase_unit == SpectrumPhaseUnit.DEGREE
        )

        input_advanced_fft_window_parameter = c_double(fft_spectrum_window_advanced_parameter or 0)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        output_spectrum_resolution = c_double(0)
        output_spectrum_start_frequency = c_double(0)
        output_spectrum_end_frequency = c_double(0)

        fft_spectrum_size = math.ceil(waveform_samples.size / 2)
        output_spectrum_magnitudes_array = numpy.zeros(
            fft_spectrum_size, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_spectrum_phases_array = numpy.zeros(
            fft_spectrum_size, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement(
            input_fft_window,
            input_view_settings_amplitude_unit_isd_db,
            input_view_settings_phase_must_unwrap,
            input_view_settings_phase_unit_is_degree,
            input_advanced_fft_window_parameter,
            waveform_sampling_period_in,
            waveform_length_in,
            waveform_samples_array_in,
            byref(output_spectrum_resolution),
            byref(output_spectrum_start_frequency),
            byref(output_spectrum_end_frequency),
            output_spectrum_magnitudes_array,
            output_spectrum_phases_array,
        )

        if res_status != 0:
            error_message = labview_fft_spectrum_amplitude_phase_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        frequencies_amplitudes_result = numpy.ctypeslib.as_array(
            obj=output_spectrum_magnitudes_array, shape=(fft_spectrum_size,)
        )

        if spectrum_amplitude_type == SpectrumAmplitudeType.PEAK:
            scale_and_offset_waveform.scale_inplace(
                waveform_samples=frequencies_amplitudes_result,
                scale_factor=math.sqrt(2),
            )

        spectrum_final_result = AmplitudePhaseSpectrum(
            f0=output_spectrum_start_frequency.value,
            df=output_spectrum_resolution.value,
            frequencies_amplitudes=frequencies_amplitudes_result,
            spectrum_amplitude_type=spectrum_amplitude_type,
            spectrum_amplitude_unit_is_db=spectrum_amplitude_must_be_db,
            frequencies_phases=numpy.ctypeslib.as_array(
                obj=output_spectrum_phases_array, shape=(fft_spectrum_size,)
            ),
            spectrum_phase_unit=spectrum_phase_unit,
        )

        return spectrum_final_result
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement"
        ) from e


def labview_process_single_waveform_multiple_tones_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    tones_selection_threshold: float,
    tones_max_count: int,
    tones_sorting_mode: int,
) -> tuple[list[WaveformTone], SpectrumAmplitudeType]:
    """Processes multiple tones of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        tones_selection_threshold (`float`): minimum amplitude peak of tone to be selected.
        tones_max_count (`int`): maximum tones count to extract from analyzed waveform.
        tones_sorting_mode (`TonesSortingMode`): sorting of the output tones list.

    Raises:
        PCBATTAnalysisException:
            Occurs when multiple tones processing fails for some reason.

    Returns:
        MultipleTonesMeasurementResult: An object that holds result of multiple tones
        processing result using LabVIEW VI.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement(
    # TonesSortingModeEnum inputTonesSortingMode,
    # size_t inputTonesResultsMaxCount,
    # double inputTonesSelectionAmplitudeThreshold,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputTonesResultActualCount,
    # double* outputTonesFrequenciesArray,
    # double* outputTonesPeakAmplitudesArray,
    # double* outputTonesPhasesDegreeArray);
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement.argtypes = [
            # TonesSortingModeEnum inputTonesSortingMode
            c_int,
            # size_t inputTonesResultsMaxCount
            c_size_t,
            # double inputTonesSelectionAmplitudeThreshold
            c_double,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # size_t* outputTonesResultActualCount
            POINTER(c_size_t),
            # double* outputTonesFrequenciesArray
            POINTER(c_double),
            # outputTonesPeakAmplitudesArray
            POINTER(c_double),
            # outputTonesPhasesDegreeArray
            POINTER(c_double),
        ]

        # call native code
        input_tones_sorting_mode = c_int(tones_sorting_mode)
        input_tones_results_max_count = c_size_t(tones_max_count)
        input_tones_selection_amplitude_threshold = c_double(tones_selection_threshold)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        output_tones_result_actual_count = c_size_t(0)
        output_tones_frequencies_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_tones_peak_amplitudes_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_tones_phases_degree_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        # labview returns phases in degree, amplitudes are peak amplitudes
        res_status = (
            dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement(
                input_tones_sorting_mode,
                input_tones_results_max_count,
                input_tones_selection_amplitude_threshold,
                waveform_sampling_period_in,
                waveform_length_in,
                waveform_samples_array_in,
                byref(output_tones_result_actual_count),
                output_tones_frequencies_array,
                output_tones_peak_amplitudes_array,
                output_tones_phases_degree_array,
            )
        )

        if res_status != 0:
            error_message = labview_multiple_tones_measurement_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        output_tones_result_actual_count_value = min(
            tones_max_count, output_tones_result_actual_count.value
        )
        tones_final_result_list: list[WaveformTone] = []

        for tone_index in range(0, output_tones_result_actual_count_value):
            if output_tones_peak_amplitudes_array[tone_index] >= tones_selection_threshold:
                tones_final_result_list.append(
                    WaveformTone(
                        frequency=output_tones_frequencies_array[tone_index],
                        amplitude=output_tones_peak_amplitudes_array[tone_index],
                        phase_radians=math.radians(output_tones_phases_degree_array[tone_index]),
                    )
                )

        return (tones_final_result_list, SpectrumAmplitudeType.PEAK)

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement"
        ) from e


def labview_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    spectrum_amplitude_must_be_db: bool,
    spectrum_phase_unit: SpectrumPhaseUnit,
    fft_spectrum_window: int,
    tones_sorting_mode: int,
    tones_selection_threshold_peak_amplitude: float,
    tones_max_count: int = None,
    fft_spectrum_window_advanced_parameter: float = None,
):
    """Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
        be expressed as db gain, instead of nominal unit.
        spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
        fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
        fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
        only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.
        tones_selection_threshold_peak_amplitude (`float`): minimum amplitude peak of tone to be selected.
        tones_max_count (`int`): maximum tones count to extract from analyzed waveform,
        when not set, all tones will be extracted.

    Raises:
        PCBATTAnalysisException:
            Occurs when frequency domain processing fails for some reason.

    Returns:
        FrequencyDomainProcessingResult: An object that holds result of fft spectrum
        processing result and multiple tones processing result using LabVIEW VIs.
    """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)

    # process spectrum magnitude and phase
    rms_spectrum_result = labview_process_single_waveform_amplitude_phase_spectrum_impl(
        waveform_samples,
        waveform_sampling_period_seconds,
        spectrum_amplitude_must_be_db,
        SpectrumAmplitudeType.RMS,
        spectrum_phase_unit,
        fft_spectrum_window,
        fft_spectrum_window_advanced_parameter,
    )

    # if tones_max_count is not provided,
    # we will resolve automatic value for it, using peak detection algorithm
    if tones_max_count is None:
        rms_to_peak_sale_factor = math.sqrt(2)
        spectrum_rms_amplitudes = rms_spectrum_result.spectrum_amplitudes
        amplitude_spectrum_peaks_indices = scipy.signal.find_peaks(x=spectrum_rms_amplitudes)[0]

        tones_selection_threshold_rms_amplitude = 0
        if spectrum_amplitude_must_be_db:
            tones_selection_threshold_rms_amplitude = 20 * numpy.log10(
                tones_selection_threshold_peak_amplitude / rms_to_peak_sale_factor
            )
        else:
            tones_selection_threshold_rms_amplitude = (
                tones_selection_threshold_peak_amplitude / rms_to_peak_sale_factor
            )

        amplitude_spectrum_peaks_values_above_threhold = list(
            filter(
                lambda rms_amplitude_value: rms_amplitude_value
                >= tones_selection_threshold_rms_amplitude,
                map(
                    lambda indice: spectrum_rms_amplitudes[indice],
                    amplitude_spectrum_peaks_indices,
                ),
            )
        )
        tones_max_count = len(amplitude_spectrum_peaks_values_above_threhold)

    # process multiple tones
    multiple_tones_result: tuple[list[WaveformTone], SpectrumAmplitudeType] = None

    if tones_max_count > 0:
        multiple_tones_result = labview_process_single_waveform_multiple_tones_impl(
            waveform_samples,
            waveform_sampling_period_seconds,
            tones_selection_threshold_peak_amplitude,
            tones_max_count,
            tones_sorting_mode,
        )
    else:
        multiple_tones_result = [], SpectrumAmplitudeType.PEAK

    return rms_spectrum_result, multiple_tones_result[0], multiple_tones_result[1]
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_pulse_analog_analysis.py sha256=1e81adedb7d0ff474d4566c8ad799313e0404ddea79edaf1eb68ad1682ebc761 bytes=30906 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_pulse_analog_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_pulse_analog_analysis.py`
- sha256: `1e81adedb7d0ff474d4566c8ad799313e0404ddea79edaf1eb68ad1682ebc761`
- bytes: 30906

````python
"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.pulse_analog_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (357 > 100 characters) (auto-generated noqa)

from collections import namedtuple
from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def labview_get_last_error_message_impl() -> str:
    """Gets last error message hold by labview Pulse Measurements VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage"
        ) from e


TuplePulseReferenceLevels = namedtuple(
    typename="PulseReferenceLevels",
    field_names=[
        "reference_level_high",
        "reference_level_middle",
        "reference_level_low",
    ],
)

TuplePulseResultsExportAll = namedtuple(
    typename="PulseResultsExportedAll",
    field_names=[
        "pulse_center",
        "pulse_duration",
        "pulse_reference_level_high",
        "pulse_reference_level_middle",
        "pulse_reference_level_low",
        "period",
        "duty_cycle",
    ],
)

TuplePulseResultsExportIgnorePeriodicity = namedtuple(
    typename="PulseResultsExportIgnorePeriodicity",
    field_names=[
        "pulse_center",
        "pulse_duration",
        "pulse_reference_level_high",
        "pulse_reference_level_middle",
        "pulse_reference_level_low",
    ],
)


def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_all_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportAll:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputProcessedPeriod,
    # double* outputProcessedDutyCycle,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll.argtypes = [
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputProcessedPeriod,
            POINTER(c_double),
            # double* outputProcessedDutyCycle,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_processed_period = c_double()
        output_processed_duty_cycle = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_processed_period),
            byref(output_processed_duty_cycle),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportAll(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
            period=output_processed_period.value,
            duty_cycle=output_processed_duty_cycle.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_all_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    amplitude_and_levels_processing_method: int,
    amplitude_and_levels_processing_histogram_size: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportAll:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # int inputHistogramSize,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputProcessedPeriod,
    # double* outputProcessedDutyCycle,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # int inputHistogramSize,
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputProcessedPeriod,
            POINTER(c_double),
            # double* outputProcessedDutyCycle,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_processed_period = c_double()
        output_processed_duty_cycle = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_amplitude_and_levels_processing_method = c_int(amplitude_and_levels_processing_method)
        input_histogram_size = c_int(amplitude_and_levels_processing_histogram_size)
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
            input_amplitude_and_levels_processing_method,
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_histogram_size,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_processed_period),
            byref(output_processed_duty_cycle),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportAll(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
            period=output_processed_period.value,
            duty_cycle=output_processed_duty_cycle.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_no_periodicity_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportIgnorePeriodicity:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels.argtypes = [
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels(
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportIgnorePeriodicity(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_no_periodicity_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    amplitude_and_levels_processing_method: int,
    amplitude_and_levels_processing_histogram_size: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportIgnorePeriodicity:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        TuplePulseResultsExportIgnorePeriodicity: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # int inputHistogramSize,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # int inputHistogramSize,
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_amplitude_and_levels_processing_method = c_int(amplitude_and_levels_processing_method)
        input_histogram_size = c_int(amplitude_and_levels_processing_histogram_size)
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels(
            input_amplitude_and_levels_processing_method,
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_histogram_size,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportIgnorePeriodicity(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels"
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/amplitude_and_levels_analysis.py sha256=7bbabd07741c9fd584f5fedc1d6d2a2f6b8f77f549832403c09f95e006fb4151 bytes=9021 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/amplitude_and_levels_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/amplitude_and_levels_analysis.py`
- sha256: `7bbabd07741c9fd584f5fedc1d6d2a2f6b8f77f549832403c09f95e006fb4151`
- bytes: 9021

````python
"""Provides Amplitude And Levels analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

from enum import IntEnum
from typing import Iterable

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _amplitude_and_levels_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class AmplitudeAndLevelsProcessingResult(AnalysisLibraryElement):
    """Defines Amplitude and Levels processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)

    def __init__(self, amplitude: float, high_state_level: float, low_state_level: float) -> None:
        """Initialize an instance of Amplitude and Levels processing result.

        Args:
            amplitude (float): Amplitude value obtained after processing waveform.
            high_state_level (float): High state level obtained after processing waveform.
            low_state_level (float): Low state level obtained after processing waveform.
        """
        self._amplitude = amplitude
        self._high_state_level = high_state_level
        self._low_state_level = low_state_level

    @property
    def amplitude(self) -> float:
        """Gets amplitude value obtained after processing waveform.

        Returns:
            float: amplitude is the difference between high state level and low state level.
        """
        return self._amplitude

    @property
    def high_state_level(self) -> float:
        """Gets high state level value obtained after processing waveform.

        Returns:
            float: High state level value.
        """
        return self._high_state_level

    @property
    def low_state_level(self) -> float:
        """Gets low state level value obtained after processing waveform.

        Returns:
            float: Low state level value.
        """
        return self._low_state_level


class AmplitudeAndLevelsProcessingMethod(IntEnum):
    """Defines Amplitude and levels processing method"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

    HISTOGRAM = 0
    """Strategy is based on histogram analysis to estimate waveform states."""

    PEAK = 1
    """Strategy is based on maximum/minimum analysis to estimate waveform states."""

    AUTO_SELECT = 2
    """Strategy is automatically selected by labview, 
    it is a combination of histogram and peak strategies."""


class LabViewAmplitudeAndLevels(AnalysisLibraryElement):
    """Provides Amplitude and Levels processing based on LabVIEW Amplitude and Levels VI"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        `Amplitude and levels` processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return _amplitude_and_levels_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_amplitude_and_levels(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> AmplitudeAndLevelsProcessingResult:
        """Processes amplitude and levels of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): samples of the waveform to process.
            waveform_sampling_period_seconds (float): sampling period of the waveform to process.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                amplitude and levels processing method.
            histogram_size (int):
                histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            AmplitudeAndLevelsProcessingResult: An object that holds result of amplitude and levels
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )
        Guard.is_greater_than_zero(histogram_size, nameof(histogram_size))
        try:
            tuple_result = _amplitude_and_levels_analysis.labview_process_single_waveform_amplitude_and_levels_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                amplitude_and_levels_processing_method,
                histogram_size,
            )

            # Build object from tuple
            return AmplitudeAndLevelsProcessingResult(
                tuple_result[0], tuple_result[1], tuple_result[2]
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.AMPLITUDE_AND_LEVELS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_amplitude_and_levels(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> Iterable[AmplitudeAndLevelsProcessingResult]:
        """Processes amplitude and levels of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod): amplitude and levels processing method.
            histogram_size (int): histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            Iterable[AmplitudeAndLevelsProcessingResult]: An iterable of objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.

        Yields:
            Iterator[Iterable[AmplitudeAndLevelsProcessingResult]]: objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.
        """  # noqa: W505, D415 - doc line too long (113 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )
        Guard.is_greater_than_zero(histogram_size, nameof(histogram_size))

        for waveform_samples in waveforms_samples:
            yield LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples,
                waveforms_sampling_period_seconds,
                amplitude_and_levels_processing_method,
                histogram_size,
            )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/dc_rms_analysis.py sha256=b132da8b858f79ddb5ffa02e6c0d77e40f2a2d704dbdbabef73e725e30ef30b9 bytes=6599 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/dc_rms_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/dc_rms_analysis.py`
- sha256: `b132da8b858f79ddb5ffa02e6c0d77e40f2a2d704dbdbabef73e725e30ef30b9`
- bytes: 6599

````python
"""Provides DC-RMS analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

from enum import IntEnum
from typing import Iterable

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _dc_rms_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsProcessingResult(AnalysisLibraryElement):
    """Defines DC-RMS processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

    def __init__(self, dc_value: float, rms_value: float) -> None:
        """Initialize an instance of DC-RMS processing result.

        Args:
            dc_value (float): DC value obtained after processing waveform.
            rms_value (float): RMS value obtained after processing waveform.
        """
        self._dc_value = dc_value
        self._rms_value = rms_value

    @property
    def dc_value(self) -> float:
        """Gets DC value obtained after processing waveform.

        Returns:
            float: DC value.
        """
        return self._dc_value

    @property
    def rms_value(self) -> float:
        """Gets RMS value obtained after processing waveform.

        Returns:
            float: RMS value.
        """
        return self._rms_value


class DcRmsProcessingWindow(IntEnum):
    """Defines DC-RMS processing window"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

    RECTANGULAR = 0
    """No windows is applied."""

    HANN = 1
    """Hann window is applied."""

    LOW_SIDE_LOBE = 2
    """Low side lobe window is applied, see LabVIEW documentation for more details."""


class LabViewBasicDcRms(AnalysisLibraryElement):
    """Provides DC-RMS processing based on LabVIEW Basic DC-RMS VI"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occured error of
        DC-RMS processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return _dc_rms_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_dc_rms(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        dc_rms_processing_window: DcRmsProcessingWindow,
    ) -> DcRmsProcessingResult:
        """Processes DC-RMS of a given waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveforms_sampling_period_seconds (float): sampling rate of the single waveform.
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window.

        Returns:
            DcRmsProcessingResult: An object that holds result of DC-RMS
            processing result using LabVIEW VI.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            tuple_result = _dc_rms_analysis.labview_process_single_waveform_dc_rms_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                dc_rms_processing_window,
            )

            # Build object from tuple
            return DcRmsProcessingResult(tuple_result[0], tuple_result[1])
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.DC_RMS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_dc_rms(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        dc_rms_processing_window: DcRmsProcessingWindow,
    ) -> Iterable[DcRmsProcessingResult]:
        """Processes DC-RMS of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window

        Returns:
            Iterable[DcRmsProcessingResult]: An iterable of objects that hold result of
            DC-RMS processing of each input waveform using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )
        for waveform_samples in waveforms_samples:
            yield LabViewBasicDcRms.process_single_waveform_dc_rms(
                waveform_samples,
                waveforms_sampling_period_seconds,
                dc_rms_processing_window,
            )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/frequency_domain_analysis.py sha256=8dfad1999c56727d5742acf253c1ccfd8bd2339d84a510673ef638426ecc3695 bytes=20762 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/frequency_domain_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/frequency_domain_analysis.py`
- sha256: `8dfad1999c56727d5742acf253c1ccfd8bd2339d84a510673ef638426ecc3695`
- bytes: 20762

````python
"""Provides frequency domain analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)

from enum import IntEnum

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _frequency_domain_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class LabViewTonesSortingMode(IntEnum):
    """Defines how should be sorted tone analysis results."""

    INCREASING_FREQUENCIES = 0
    """Tone analysis results are sorted according to frequency (X axis)."""
    DECREASING_AMPLITUDES = 1
    """Tone analysis results are sorted according to amplitude (Y axis)."""


class LabViewFftSpectrumWindow(IntEnum):
    """Defines all supported signal `fft processing` time windows."""

    RECTANGLE = (0,)
    """`Rectangle` window."""

    HANNING = (1,)
    """`Hanning` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/hanning_window.html"""

    HAMMING = (2,)
    """`Hamming` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/hamming_window.html"""

    BLACKMAN_HARRIS = (3,)
    """`Blackman-Harris` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_harris_window.html"""

    BLACKMAN_EXACT = (4,)
    """`Blackman exact window`, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/exact_blackman_window.html"""

    BLACKMAN = (5,)
    """`Blackman` window; for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_window.html"""

    FLAT_TOP = (6,)
    """`Flat top profile` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/flat_top_window.html"""

    BHARRIS_4TERMS = (7,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    BHARRIS_7TERMS = (8,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    LOW_LATERAL_LOBE = (9,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    BLACKMAN_NUTTALL = (11,)
    """`Blackman-Nuttall` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_nuttall_window.html"""

    TRIANGLE = (30,)
    """`Triangle` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/triangle_window.html"""

    BARTLETT_HANNING = (31,)
    """`Bartlett-Hanning` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/modbhw.html"""

    BOHMAN = (32,)
    """`Bohman` window, For more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/bohman.html"""

    PARZEN = (33,)
    """`Parzen` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/parzen.html"""

    WELCH = (34,)
    """Welch window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/welch.html"""

    KAISER = (60,)
    """`Kaiser` (requires to provide beta parameter):
    The Kaiser window function allows you to control the stop band
    attenuation via the β parameter, the higher the value of β, the more the attenuation is.
    The more attenuation you have the wider the main lobe and hence the wider the transition band,
    for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/rfmx-waveform-creator/page/rfwfmcreator/kaiserwindow.html"""  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)

    DOLPH_TCHEBYCHEV = (61,)
    """`DolphTchebychev` (requires to provider lobes ratio parameter), for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/chebyshev_window.html"""

    GAUSSIAN = 62
    """Gaussian (requires to provide standard deviation parameter), for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/gaussian_window.html"""


class MultipleTonesProcessingResult(AnalysisLibraryElement):
    """Defines multiple tones processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        detected_tones: list[WaveformTone],
        amplitude_type: SpectrumAmplitudeType,
    ) -> None:
        """Initializes an instance of `MultipleTonesProcessingResult`

        Args:
            detected_tones (`list[WaveformTone]`): list of waveform tones.
            amplitude_type (`SpectrumAmplitudeType`): amplitude type of the waveform tones.

        Raises:
            ValueError: Occurs when input `detected_tones` list is none.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(instance=detected_tones, instance_name=nameof(detected_tones))
        self._detected_tones = detected_tones
        self._amplitude_type = amplitude_type

    @property
    def detected_tones(self) -> list[WaveformTone]:
        """Gets the list of the tones detected in analyzed waveform.

        Returns:
            list[WaveformTone]: list of waveform tones.
        """
        return self._detected_tones

    @property
    def amplitude_type(self) -> SpectrumAmplitudeType:
        """Gets the kind amplitudes of the tones detected in analyzed waveform.

        Returns:
            SpectrumAmplitudeType: amplitude type `RMS` or `PEAK`.
        """
        return self._amplitude_type


class MultipleTonesAmplitudePhaseSpectrumProcessingResult(AnalysisLibraryElement):
    """Defines multiple tones and spectrum processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        multiple_tones_result: MultipleTonesProcessingResult,
        amplitude_phase_spectrum: AmplitudePhaseSpectrum,
    ) -> None:
        """Initialize an instance of `MultipleTonesAmplitudePhaseSpectrumProcessingResult`.

        Args:
            multiple_tones_result (`MultipleTonesProcessingResult`):
                holds multiple tones processing results.
            amplitude_phase_spectrum (`AmplitudePhaseSpectrum`):
                holds fft spectrum processing results.

        Raises:
            ValueError: Occurs when input `multiple_tones_result` or
            `amplitude_phase_spectrum` are none.
        """
        Guard.is_not_none(
            instance=multiple_tones_result, instance_name=nameof(multiple_tones_result)
        )

        Guard.is_not_none(
            instance=amplitude_phase_spectrum,
            instance_name=nameof(amplitude_phase_spectrum),
        )

        self._multiple_tones_result = multiple_tones_result
        self._amplitude_phase_spectrum = amplitude_phase_spectrum

    @property
    def multiple_tones_result(self) -> MultipleTonesProcessingResult:
        """Gets multiple tones processing results of analyzed waveform.

        Returns:
            MultipleTonesProcessingResult: multiple tones processing result.
        """
        return self._multiple_tones_result

    @property
    def amplitude_phase_spectrum(self) -> AmplitudePhaseSpectrum:
        """Gets fft spectrum processing results of analyzed waveform.

        Returns:
            AmplitudePhaseSpectrum: fft spectrum processing result.
        """
        return self._amplitude_phase_spectrum


class LabViewFrequencyDomainProcessing(AnalysisLibraryElement):
    """Defines frequency domain analysis functions such
    fft spectrum and multiple tones processing."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (343 > 100 characters) (auto-generated noqa)

    @staticmethod
    def process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        spectrum_amplitude_must_be_db: bool,
        spectrum_phase_unit: SpectrumPhaseUnit,
        fft_spectrum_window: LabViewFftSpectrumWindow,
        tones_sorting_mode: LabViewTonesSortingMode,
        tones_selection_threshold_peak_amplitude: float,
        tones_max_count: int = None,
        fft_spectrum_window_advanced_parameter: float = None,
    ) -> MultipleTonesAmplitudePhaseSpectrumProcessingResult:
        """Processes `RMS` amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`LabViewFftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.
            tones_selection_threshold_peak_amplitude (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform,
            when not set, all tones will be extracted.

        Raises:
            PCBATTAnalysisException:
                Occurs when frequency domain processing fails for some reason.

        Returns:
            FrequencyDomainProcessingResult: An object that holds result of fft spectrum
            processing result and multiple tones processing result using LabVIEW VIs.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        try:
            results_tuple = _frequency_domain_analysis.labview_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                spectrum_amplitude_must_be_db,
                spectrum_phase_unit,
                fft_spectrum_window,
                tones_sorting_mode,
                tones_selection_threshold_peak_amplitude,
                tones_max_count,
                fft_spectrum_window_advanced_parameter,
            )

            return MultipleTonesAmplitudePhaseSpectrumProcessingResult(
                multiple_tones_result=MultipleTonesProcessingResult(
                    detected_tones=results_tuple[1], amplitude_type=results_tuple[2]
                ),
                amplitude_phase_spectrum=results_tuple[0],
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.FREQUENCY_DOMAIN_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e


class LabViewFftSpectrumAmplitudePhase(AnalysisLibraryElement):
    """Provides Amplitude/Phase spectrum processing based on
    `LabVIEW FFT Spectrum Magnitude Phase VI`"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        ``FFT Spectrum Magnitude and Phase`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        return (
            _frequency_domain_analysis.labview_fft_spectrum_amplitude_phase_get_last_error_message_impl()
        )

    @staticmethod
    def process_single_waveform_amplitude_phase_spectrum(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        spectrum_amplitude_must_be_db: bool,
        spectrum_amplitude_type: SpectrumAmplitudeType,
        spectrum_phase_unit: SpectrumPhaseUnit,
        fft_spectrum_window: LabViewFftSpectrumWindow,
        fft_spectrum_window_advanced_parameter: float = None,
    ) -> AmplitudePhaseSpectrum:
        """Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_amplitude_type (`FftSpectrumAmplitudeType`): can be `RMS` or `PEAK`.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            AmplitudePhaseSpectrum: An object that holds result of fft spectrum
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            return _frequency_domain_analysis.labview_process_single_waveform_amplitude_phase_spectrum_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                spectrum_amplitude_must_be_db,
                spectrum_amplitude_type,
                spectrum_phase_unit,
                fft_spectrum_window,
                fft_spectrum_window_advanced_parameter,
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.AMPLITUDE_AND_PHASE_SPECTRUM_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e


class LabViewMultipleTonesMeasurement(AnalysisLibraryElement):
    """Provides multiple tones processing based on
    `LabVIEW Multiple Tone Information VI`"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (338 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        ``Multiple Tones Measurements`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        return (
            _frequency_domain_analysis.labview_multiple_tones_measurement_get_last_error_message_impl()
        )

    @staticmethod
    def process_single_waveform_multiple_tones(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        tones_selection_threshold: float,
        tones_max_count: int,
        tones_sorting_mode: LabViewTonesSortingMode,
    ) -> MultipleTonesProcessingResult:
        """Processes multiple tones of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            tones_selection_threshold (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform.
            tones_sorting_mode (`TonesSortingMode`): sorting of the output tones list.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            MultipleTonesMeasurementResult: An object that holds result of multiple tones
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        Guard.is_greater_than_zero(tones_selection_threshold, nameof(tones_selection_threshold))

        if tones_max_count is not None:
            Guard.is_greater_than_zero(tones_max_count, nameof(tones_max_count))

        try:
            tuple_result = (
                _frequency_domain_analysis.labview_process_single_waveform_multiple_tones_impl(
                    waveform_samples,
                    waveform_sampling_period_seconds,
                    tones_selection_threshold,
                    tones_max_count,
                    tones_sorting_mode,
                )
            )

            return MultipleTonesProcessingResult(
                detected_tones=tuple_result[0], amplitude_type=tuple_result[1]
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.MULTIPLE_TONES_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/pulse_analog_analysis.py sha256=b07e571fd0dbae9e1a652811473eb7882c020f09a3f157272e24f13f55aa8363 bytes=29568 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_analysis/pulse_analog_analysis.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_analysis/pulse_analog_analysis.py`
- sha256: `b07e571fd0dbae9e1a652811473eb7882c020f09a3f157272e24f13f55aa8363`
- bytes: 29568

````python
"""Provides pulse analog analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

from enum import IntEnum
from typing import Iterable, Optional

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _pulse_analog_analysis,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_utilities import numeric_utilities
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class WaveformPeriodicityAnalogProcessingResult(AnalysisLibraryElement):
    """Defines pulse periodicity related measurements analog processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)

    def __init__(self, period: float, duty_cycle: float) -> None:
        """Initialize an instance of waveform periodicty processing result.

        Args:
            period (float): period value obtained after processing waveform.
            duty_cycle (float): duty cycle value obtained after processing waveform,
                expressed as ratio [0,1].
        """
        Guard.is_greater_than_zero(period, nameof(period))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle, nameof(duty_cycle))

        self._period = period
        self._duty_cycle = duty_cycle

    @property
    def period(self) -> float:
        """Gets period value obtained after processing waveform.

        Returns:
            float: period value.
        """
        return self._period

    @property
    def frequency(self) -> float:
        """Gets frequency value obtained after processing waveform.

        Returns:
            float: period value.
        """
        return numeric_utilities.invert_value(self._period)

    @property
    def duty_cycle(self) -> float:
        """Gets duty cycle value obtained after processing waveform expressed as ratio in [0,1].

        Returns:
            float: duty cycle ratio value.
        """
        return self._duty_cycle

    @property
    def duty_cycle_percent(self) -> float:
        """Gets duty cycle value obtained after processing waveform expressed as percentage.

        Returns:
            float: duty cycle ratio value.
        """
        return self._duty_cycle * 100


class PulseAnalogProcessingResult(AnalysisLibraryElement):
    """Defines pulse measurements analog processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        pulse_center: float,
        pulse_duration: float,
        pulse_reference_level_high: float,
        pulse_reference_level_middle: float,
        pulse_reference_level_low: float,
        period: float = None,
        duty_cycle: float = None,
    ) -> None:
        """Initialize an instance of pulse analog processing result.

        Args:
            pulse_center (float): pulse center is defined as (Tr+Tf)/2
            pulse_duration (float): pulse duration is the time difference in seconds between
                the first two mid ref level crossings of the analyzed pulse,
                pulse duration is also known as pulse width.
            pulse_reference_level_high (float):
                absolute high reference level used to evaluate pulse center.
            pulse_reference_level_middle (float):
                absolute middle reference level used to evaluate pulse center.
            pulse_reference_level_low (float):
                absolute low reference level used to evaluate pulse center.
            period (float, optional):
                time between adjacent mid ref level crossings the same direction in seconds.
                Defaults to None.
            duty_cycle (float, optional): fraction of period according to analyzed pulse.
                Defaults to None.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        Guard.is_greater_than_or_equal_to_zero(pulse_duration, nameof(pulse_duration))

        self._pulse_center = pulse_center
        self._pulse_duration = pulse_duration
        self._pulse_reference_level_high = pulse_reference_level_high
        self._pulse_reference_level_middle = pulse_reference_level_middle
        self._pulse_reference_level_low = pulse_reference_level_low

        if duty_cycle is not None and period is not None:
            self._periodicity_processing_result = WaveformPeriodicityAnalogProcessingResult(
                period, duty_cycle
            )
        else:
            self._periodicity_processing_result = None

    @property
    def pulse_center(self) -> float:
        """Gets center date obtained after processing waveform pulse.

        Returns:
            float: Pulse center date expressed in seconds.
        """
        return self._pulse_center

    @property
    def pulse_duration(self) -> float:
        """Gets pulse width obtained after processing waveform pulse.

        Returns:
            float: Pulse width expressed in seconds.
        """
        return self._pulse_duration

    @property
    def pulse_reference_level_high(self) -> float:
        """Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        """
        return self._pulse_reference_level_high

    @property
    def pulse_reference_level_middle(self) -> float:
        """Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        """
        return self._pulse_reference_level_middle

    @property
    def pulse_reference_level_low(self) -> float:
        """Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        """
        return self._pulse_reference_level_low

    @property
    def waveform_periodicity_processing_result(
        self,
    ) -> Optional[WaveformPeriodicityAnalogProcessingResult]:
        """Gets periodicity analysis results obtained when processed waveform pulses, can be None.

        Returns:
            Optional[WaveformPeriodicityAnalogProcessingResult]:
                periodicity analysis results obtained when processed waveform
        """
        return self._periodicity_processing_result


class PulseAnalogProcessingPolarity(IntEnum):
    """Defines pulse analog processing polarity."""

    LOW = 0
    """Pulse state is defined by low level."""

    HIGH = 1
    """Pulse state is defined by high level."""


class PulseAnalogProcessingReferenceLevelsUnit(IntEnum):
    """Defines pulse analog processing reference levels unit."""

    ABSOLUTE = 0
    """The waveform level is an absolute value, for example, 5V."""

    RELATIVE_PERCENT = 1
    """The waveform level is a relative value, for example, 
        90% of maximum value contained in waveform."""


class PulseAnalogProcessingExportMode(IntEnum):
    """Defines labview pulse processing export mode."""

    ALL = 0
    """All pulse characteristics are processed."""

    IGNORE_WAVEFORM_PERIODICITY_ANALYSIS = 1
    """All pulse characteristics are processed, except period, frequency and duty cycle elements."""


class PulseAnalogProcessingReferenceLevels(AnalysisLibraryElement):
    """Defines reference levels that will be used to locate pulse when
    analyzing waveform.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        reference_level_high: float,
        reference_level_middle: float,
        reference_level_low: float,
    ):
        self._reference_level_high = reference_level_high
        self._reference_level_middle = reference_level_middle
        self._reference_level_low = reference_level_low

    @property
    def reference_level_high(self) -> float:
        """Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        """
        return self._reference_level_high

    @property
    def reference_level_middle(self) -> float:
        """Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        """
        return self._reference_level_middle

    @property
    def reference_level_low(self) -> float:
        """Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        """
        return self._reference_level_low


class PulseAnalogMeasurementPercentLevelsSettings(AnalysisLibraryElement):
    """Defines settings to use when reference levels
    required for pulse analysis are expressed as percentage."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> None:
        """Initialize an instance of `PulseAnalogMeasurementPercentLevelsSettings`.

        Args:
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                Amplitude and levels processing method.
            histogram_size (int):
                Number of bins of the histogram when amplitude and levels processing choose to use
                histogram based algorithm.
        """
        Guard.is_greater_than_zero(value=histogram_size, value_name=nameof(histogram_size))

        self._amplitude_and_levels_processing_method = amplitude_and_levels_processing_method
        self._histogram_size = histogram_size

    @property
    def amplitude_and_levels_processing_method(self) -> int:
        """Gets method that will be used when processing waveform states.

        Returns:
            int: Amplitude and levels processing method.
        """
        return self._amplitude_and_levels_processing_method

    @property
    def histogram_size(self) -> int:
        """Gets histogram size, ie, bins count, that will be used when processing waveform states.

        Returns:
            int: histogram bins count.
        """
        return self._histogram_size


class LabViewPulseAnalogMeasurements(AnalysisLibraryElement):
    """Provides pulse analog processing based on ``LabVIEW Pulse Measurements`` VI"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (196 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occured error of
        ``Pulse Measurements`` labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        return _pulse_analog_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_multiple_pulse_measurements(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        waveform_t0: float,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> Iterable[PulseAnalogProcessingResult]:
        """Processes multiple pulse measurements of a
        given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            Iterable[PulseAnalogProcessingResult]: an object that holds multiple results of pulse
            processing result using LabVIEW VI.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))

        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        pulse_number = 0
        stop_pulse_analysis = False

        while not stop_pulse_analysis:
            pulse_number = pulse_number + 1
            try:
                yield LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                    waveform_samples,
                    waveform_sampling_period_seconds,
                    waveform_t0,
                    pulse_number,
                    export_mode,
                    processing_polarity,
                    reference_levels_unit,
                    reference_levels,
                    percent_levels_settings,
                )
            except PCBATTAnalysisException:
                stop_pulse_analysis = True

    @staticmethod
    def process_single_waveform_pulse_measurements(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        waveform_t0: float,
        pulse_number: int,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> PulseAnalogProcessingResult:
        """Processes pulse measurements of a given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            PulseAnalogProcessingResult: An object that holds result of pulse
            processing result using LabVIEW VI.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(pulse_number, nameof(pulse_number))

        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            if reference_levels_unit == PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE:
                # hold absolute levels based analysis, percent settings is not required
                if export_mode == PulseAnalogProcessingExportMode.ALL:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_all_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        reference_levels=_pulse_analog_analysis.TuplePulseReferenceLevels(
                            reference_level_high=reference_levels.reference_level_high,
                            reference_level_middle=reference_levels.reference_level_middle,
                            reference_level_low=reference_levels.reference_level_low,
                        ),
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                        processing_result_as_tuple.period,
                        processing_result_as_tuple.duty_cycle,
                    )

                processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_no_periodicity_impl(
                    waveform_samples=waveform_samples,
                    waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                    pulse_number=pulse_number,
                    processing_polarity=processing_polarity,
                    reference_levels=_pulse_analog_analysis.TuplePulseReferenceLevels(
                        reference_level_high=reference_levels.reference_level_high,
                        reference_level_middle=reference_levels.reference_level_middle,
                        reference_level_low=reference_levels.reference_level_low,
                    ),
                )
                return PulseAnalogProcessingResult(
                    processing_result_as_tuple.pulse_center + waveform_t0,
                    processing_result_as_tuple.pulse_duration,
                    processing_result_as_tuple.pulse_reference_level_high,
                    processing_result_as_tuple.pulse_reference_level_middle,
                    processing_result_as_tuple.pulse_reference_level_low,
                )
            elif reference_levels_unit == PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT:
                # check reference levels are percent values
                # hold relative percent levels based analysis
                # percent settings is required
                if percent_levels_settings is None:
                    raise PCBATTAnalysisException(
                        AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_PERCENT_REQUIRES_STATES_SETTINGS
                    )

                # hold relative levels based analysis, percent settings is not required
                if export_mode == PulseAnalogProcessingExportMode.ALL:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_all_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        amplitude_and_levels_processing_method=percent_levels_settings.amplitude_and_levels_processing_method,
                        amplitude_and_levels_processing_histogram_size=percent_levels_settings.histogram_size,
                        reference_levels=reference_levels,
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center + waveform_t0,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                        processing_result_as_tuple.period,
                        processing_result_as_tuple.duty_cycle,
                    )
                else:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_no_periodicity_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        amplitude_and_levels_processing_method=percent_levels_settings.amplitude_and_levels_processing_method,
                        amplitude_and_levels_processing_histogram_size=percent_levels_settings.histogram_size,
                        reference_levels=reference_levels,
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center + waveform_t0,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                    )

            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_IS_NOT_SUPPORTED
            )

        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_pulse_measurements(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        waveforms_t0: Iterable[float],
        pulse_number: int,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> Iterable[PulseAnalogProcessingResult]:
        """Processes pulse measurement of a given multiple waveforms samples using LabVIEW VI.

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): multiple waveforms samples.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            waveforms_t0 (Iterable[float]): for each waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode): pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity): pulse polarity that will
                be analyzed (high or low).
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveforms.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Returns:
            Iterable[PulseAnalogProcessingResult]: An iterable of objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Yields:
            Iterator[Iterable[PulseAnalogProcessingResult]]: objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.
        """
        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )

        Guard.have_same_size(
            first_iterable_instance=waveforms_samples,
            first_iterable_name=nameof(waveforms_samples),
            second_iterable_instance=waveforms_t0,
            second_iterable_name=nameof(waveforms_t0),
        )
        Guard.is_greater_than_zero(pulse_number, nameof(pulse_number))

        for waveform_samples, waveform_t0 in zip(waveforms_samples, waveforms_t0):
            yield LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples,
                waveforms_sampling_period_seconds,
                waveform_t0,
                pulse_number,
                export_mode,
                processing_polarity,
                reference_levels_unit,
                reference_levels,
                percent_levels_settings,
            )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/__init__.py sha256=2dc469917b741553da4d41396f3bd7815ee20bce6677a4bfbd109908d27d0937 bytes=263 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/__init__.py`
- sha256: `2dc469917b741553da4d41396f3bd7815ee20bce6677a4bfbd109908d27d0937`
- bytes: 263

````python
"""Provides a set of waveform creation modules using python written functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (191 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/__init__.py sha256=dd632475ff253e4316518a6371cdb23e3aa99f650977a5c1771ea1467a174c99 bytes=242 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/__init__.py`
- sha256: `dd632475ff253e4316518a6371cdb23e3aa99f650977a5c1771ea1467a174c99`
- bytes: 242

````python
"""Provides private modules of waveform creation package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_multitones_waveform.py sha256=8fec7145a59add15d949e61ce6309122daa08378432664a7fbbbb0d318b9ee24 bytes=2429 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_multitones_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_multitones_waveform.py`
- sha256: `8fec7145a59add15d949e61ce6309122daa08378432664a7fbbbb0d318b9ee24`
- bytes: 2429

````python
"""Private module that provides a set of helper functions 
   for `multitones_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (332 > 100 characters) (auto-generated noqa)

import math

import numpy

from nipcbatt.pcbatt_analysis.common.common_types import WaveformTone
from nipcbatt.pcbatt_analysis.waveform_transformation import (  # noqa: F401 - 'nipcbatt.pcbatt_analysis.waveform_transformation.scale_and_offset_waveform' imported but unused (auto-generated noqa)
    scale_and_offset_waveform,
)
from nipcbatt.pcbatt_utilities import (  # noqa: F401 - 'nipcbatt.pcbatt_utilities.numeric_utilities' imported but unused (auto-generated noqa)
    numeric_utilities,
)


def create_multitones_waveform_impl(
    amplitude: float,
    waveform_tones: list[WaveformTone],
    samples_count: int,
    sampling_rate: float,
    amplitude_normalization_threshold: float = 0.000001,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a multitones waveform described through its characteristics."""
    result_waveform: numpy.ndarray[numpy.float64] = numpy.zeros(shape=samples_count)

    # fill sum of sine waves
    for waveform_tone in waveform_tones:
        for sample_index in range(0, samples_count):
            numerator = 2.0 * numpy.pi * waveform_tone.frequency / sampling_rate
            result_waveform[sample_index] = result_waveform[sample_index] + (
                waveform_tone.amplitude
                * math.sin(waveform_tone.phase_radians + sample_index * numerator)
            )

    # normalize resulting sum waveform
    # samples_max: numpy.float64 = result_waveform.max()

    # if samples_max > amplitude_normalization_threshold:
    #     wanted_samples_max = amplitude
    #     actual_samples_max = samples_max
    #     normalization_factor = numeric_utilities.absolute_value(
    #         wanted_samples_max
    #     ) / numeric_utilities.absolute_value(actual_samples_max)

    #     scale_and_offset_waveform.scale_inplace(
    #         waveform_samples=result_waveform, scale_factor=normalization_factor
    #     )

    return result_waveform
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_sine_waveform.py sha256=18fd16efd409297c6ee2371f1c7187d9c135fca62d774f9806c6d0c649cfd871 bytes=1802 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_sine_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_sine_waveform.py`
- sha256: `18fd16efd409297c6ee2371f1c7187d9c135fca62d774f9806c6d0c649cfd871`
- bytes: 1802

````python
"""Private module that provides a set of helper functions
   for `sine_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)

import math

import numpy


def create_cosine_waveform_impl(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a cosine waveform described through its characteristics."""
    phase = phase % (2.0 * numpy.pi)
    samples_array = numpy.zeros(shape=samples_count)

    numerator = 2.0 * numpy.pi * frequency / sampling_rate

    for sample_index in range(0, samples_count):
        samples_array[sample_index] = offset + amplitude * math.cos(
            phase + sample_index * numerator
        )

    return samples_array


def create_sine_waveform_impl(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics."""
    phase = phase % (2.0 * numpy.pi)
    samples_array = numpy.zeros(shape=samples_count)

    numerator = 2.0 * numpy.pi * frequency / sampling_rate

    for sample_index in range(0, samples_count):
        samples_array[sample_index] = offset + amplitude * math.sin(
            phase + sample_index * numerator
        )

    return samples_array
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_square_waveform.py sha256=27cc08244ad790e508162bdfb634f6f1b53b6c08ee611ecb5efe72c915be0786 bytes=1797 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_square_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_square_waveform.py`
- sha256: `27cc08244ad790e508162bdfb634f6f1b53b6c08ee611ecb5efe72c915be0786`
- bytes: 1797

````python
"""Private module that provides a set of helper functions 
   for `square_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (328 > 100 characters) (auto-generated noqa)

import math

import numpy
import scipy.signal

from nipcbatt.pcbatt_utilities import numeric_utilities


def create_square_waveform_impl(
    amplitude: float,
    frequency: float,
    duty_cycle: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a square waveform described through its characteristics."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)

    sampling_period = numeric_utilities.invert_value(sampling_rate)
    waveform_period = numeric_utilities.invert_value(frequency)

    square_waveform_phase_rounded = phase % (2 * numpy.pi)
    square_wave_delay_from_phase = math.floor(
        sampling_rate * (square_waveform_phase_rounded * waveform_period / (2 * numpy.pi))
    )

    x = numpy.fromiter(
        map(lambda sample_index: sample_index * sampling_period, range(0, samples_count)),
        dtype=numpy.float64,
    )
    y = scipy.signal.square(t=(2 * numpy.pi * frequency) * x, duty=duty_cycle)

    for sample_index in range(0, y.size):
        y[sample_index] = amplitude * y[sample_index] + offset

    return numpy.roll(y, square_wave_delay_from_phase)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/multitones_waveform.py sha256=3fcb522ef99af107cb245e511386b20a1daf791fbe014a5470f806b9737bf729 bytes=2738 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/multitones_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/multitones_waveform.py`
- sha256: `3fcb522ef99af107cb245e511386b20a1daf791fbe014a5470f806b9737bf729`
- bytes: 2738

````python
"""Provides multiple tones waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.common_types import WaveformTone
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _multitones_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_multitones_waveform(
    multitones_amplitude: float,
    waveform_tones: list[WaveformTone],
    samples_count: int,
    sampling_rate: float,
    amplitude_normalization_threshold: float = 0.000001,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a multi-tones waveform described through its characteristics.

    Args:
        multitones_amplitude (float): amplitude of the multi-tones waveform,
        must be greater than zero.
        waveform_tones (list[WaveformTone]): describes the distribution of tones
        that will be contained in the created waveform.
        samples_count (int): number of samples that will be created for the multi-tones waveform.
        sampling_rate (float): sampling rate of the multi-tones waveform.
        amplitude_normalization_threshold(float): when waveform maximum is greater than it,
            normalization of the amplitude is applied to match input `multitones_amplitude`.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when samples_count is less or equal zero,
            when sampling_rate is less or equal zero,
            and when amplitude_normalization_threshold is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created multi-tones waveform.
    """
    Guard.is_greater_than_zero(multitones_amplitude, nameof(multitones_amplitude))
    Guard.is_greater_than_zero(samples_count, nameof(samples_count))
    Guard.is_greater_than_zero(sampling_rate, nameof(sampling_rate))
    Guard.is_greater_than_zero(
        amplitude_normalization_threshold, nameof(amplitude_normalization_threshold)
    )

    try:
        return _multitones_waveform.create_multitones_waveform_impl(
            multitones_amplitude,
            waveform_tones,
            samples_count,
            sampling_rate,
            amplitude_normalization_threshold,
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.MULTIPLE_TONES_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/sine_waveform.py sha256=4a9ddc4226a374146ed209fbf14d3f0c8fe95060f1ad14434db41070b3b22cb4 bytes=4330 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/sine_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/sine_waveform.py`
- sha256: `4a9ddc4226a374146ed209fbf14d3f0c8fe95060f1ad14434db41070b3b22cb4`
- bytes: 4330

````python
"""Provides sine waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _sine_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_cosine_waveform(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics, using math.cos.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _sine_waveform.create_cosine_waveform_impl(
            amplitude, frequency, phase, offset, samples_count, sampling_rate
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e


def create_sine_waveform(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics, using math.sin.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            and occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _sine_waveform.create_sine_waveform_impl(
            amplitude, frequency, phase, offset, samples_count, sampling_rate
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/square_waveform.py sha256=062d2ad18b991bc13414b57c00c77ee13330e7060bdae4247c5a34e41f577828 bytes=2752 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_creation/square_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_creation/square_waveform.py`
- sha256: `062d2ad18b991bc13414b57c00c77ee13330e7060bdae4247c5a34e41f577828`
- bytes: 2752

````python
"""Provides square waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _square_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_square_waveform(
    amplitude: float,
    frequency: float,
    duty_cycle: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a square waveform described through its characteristics.

    Args:
        amplitude (float): amplitude of the square wave, must be greater than zero.
        frequency (float): frequency of the square wave, must be greater than zero.
        duty_cycle (float): duty cycle of the square wave, must be in [0,1].
        phase (float): phase of the square wave, will be rounded modulo 2*PI.
        offset (float): vertical offset of the square wave,
        will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the square wave.
        sampling_rate (float): sampling rate of the square wave.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when `frequency` is less or equal zero,
            occurs when `samples_count` is less or equal zero,
            and occurs when `sampling_rate` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created square waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_within_limits_included(
        value=duty_cycle, lower_limit=0, upper_limit=1, value_name=nameof(duty_cycle)
    )
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _square_waveform.create_square_waveform_impl(
            amplitude,
            frequency,
            duty_cycle,
            phase,
            offset,
            samples_count,
            sampling_rate,
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SQUARE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/__init__.py sha256=5bda38b435652128e009e16789f5dc81c50c48211caacf5157f4becf40fc0793 bytes=269 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_transformation/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_transformation/__init__.py`
- sha256: `5bda38b435652128e009e16789f5dc81c50c48211caacf5157f4becf40fc0793`
- bytes: 269

````python
"""Provides a set of waveform transformation modules using python written functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (197 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/_waveform_transformation_internal/_scale_and_offset_waveform.py sha256=dfe951def6986524bee39b115a323916baeb90573a2fb446d380dceb03d32323 bytes=1362 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_transformation/_waveform_transformation_internal/_scale_and_offset_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_transformation/_waveform_transformation_internal/_scale_and_offset_waveform.py`
- sha256: `dfe951def6986524bee39b115a323916baeb90573a2fb446d380dceb03d32323`
- bytes: 1362

````python
"""Private module that provides a set of helper functions
   for `scale_and_offset_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (338 > 100 characters) (auto-generated noqa)

import numpy


def scale_and_apply_offset_impl(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Implementation of scale and offset waveform."""
    result_array = numpy.fromiter(
        iter=map(
            lambda waveform_sample: scale_factor * waveform_sample + offset,
            waveform_samples,
        ),
        dtype=numpy.float64,
    )

    return result_array


def scale_and_apply_offset_inplace_impl(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Implementation of scale and offset waveform in place."""
    for sample_index in range(0, waveform_samples.size):
        waveform_samples[sample_index] = scale_factor * waveform_samples[sample_index] + offset
    return waveform_samples
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/scale_and_offset_waveform.py sha256=17e658b1ad56fefa871810e161b84e6a674d24a5fd946e610cf1ceac2b3ea7b4 bytes=7604 -->
## FILE: src/nipcbatt/pcbatt_analysis/waveform_transformation/scale_and_offset_waveform.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/waveform_transformation/scale_and_offset_waveform.py`
- sha256: `17e658b1ad56fefa871810e161b84e6a674d24a5fd946e610cf1ceac2b3ea7b4`
- bytes: 7604

````python
"""Provides scale and offset waveform transformation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_transformation._waveform_transformation_internal import (
    _scale_and_offset_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def scale(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(
            waveform_samples, scale_factor, 0
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def apply_offset(
    waveform_samples: numpy.ndarray[numpy.float64], offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a vertical offset to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(waveform_samples, 1, offset)
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """
    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, scale_factor, 0
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def apply_offset_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a vertical offset to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """
    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, 1, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_and_apply_offset(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor and vertical offset to given waveform samples,
    and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(
            waveform_samples, scale_factor, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_and_apply_offset_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor and vertical offset to given waveform samples,
    and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    Guard.is_not_none(instance=waveform_samples, instance_name=nameof(waveform_samples))
    Guard.is_not_empty(iterable_instance=waveform_samples, instance_name=nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, scale_factor, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/win32/readme.txt sha256=76fdea80ff7c8d11aa6b3d825d8b3bf6c1715cb19844ef9a1911bc7a79f35a53 bytes=30 -->
## FILE: src/nipcbatt/pcbatt_analysis/win32/readme.txt

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/win32/readme.txt`
- sha256: `76fdea80ff7c8d11aa6b3d825d8b3bf6c1715cb19844ef9a1911bc7a79f35a53`
- bytes: 30

````text
put windows x86 dll files here
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/win_amd64/readme.txt sha256=4a6363f249617d4a229246ad303bdaadb3978ae06306052f8f386735175b48c7 bytes=30 -->
## FILE: src/nipcbatt/pcbatt_analysis/win_amd64/readme.txt

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_analysis/win_amd64/readme.txt`
- sha256: `4a6363f249617d4a229246ad303bdaadb3978ae06306052f8f386735175b48c7`
- bytes: 30

````text
put windows x64 dll files here
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/__init__.py sha256=b0d2f3120cd3e7bc5cc9d7ff5b1c28b03144ec298c300247c19680d183c969f9 bytes=242 -->
## FILE: src/nipcbatt/pcbatt_automation/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/__init__.py`
- sha256: `b0d2f3120cd3e7bc5cc9d7ff5b1c28b03144ec298c300247c19680d183c969f9`
- bytes: 242

````python
"""Contains all automation tests using nipcbatt.library."""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/__init__.py sha256=6c015ce4be88123650af5a5868acbab4a4b963e85cc2886589d7c2f02f8235e4 bytes=64 -->
## FILE: src/nipcbatt/pcbatt_automation/action_button_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/action_button_tests/__init__.py`
- sha256: `6c015ce4be88123650af5a5868acbab4a4b963e85cc2886589d7c2f02f8235e4`
- bytes: 64

````python
"""Includes files for running aciton button test sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/action_button_main_sequence.py sha256=021b40e5e06b145495b48f39be8814ee5ea37d0b040b30d898a35d37f5df6922 bytes=1010 -->
## FILE: src/nipcbatt/pcbatt_automation/action_button_tests/action_button_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/action_button_tests/action_button_main_sequence.py`
- sha256: `021b40e5e06b145495b48f39be8814ee5ea37d0b040b30d898a35d37f5df6922`
- bytes: 1010

````python
"""Main Sequence for executing Action Button Test"""  

# import functions
from nipcbatt.pcbatt_automation.action_button_tests.action_button_test import (
    action_button_test,
)
from nipcbatt.pcbatt_automation.action_button_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

"""Complete DC-RMS Voltage Measurements by performing button actions 
   (generating DC Voltages) on specific test points"""

action_button_test()

######## CLEAN UP ####################

# Turn off all configured AO channels by configuring to 0V
power_down_all_ao_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/action_button_test.py sha256=821150115404740f2bf322432156101bcf9b5337d0ca8ad89ced339b401f1fff bytes=6766 -->
## FILE: src/nipcbatt/pcbatt_automation/action_button_tests/action_button_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/action_button_tests/action_button_test.py`
- sha256: `821150115404740f2bf322432156101bcf9b5337d0ca8ad89ced339b401f1fff`
- bytes: 6766

````python
"""Example demonstrates DC-RMS Voltage Measurements by performing button actions 
   (generating DC Voltages) on specific test points"""  

from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
BUTTON_CHANNEL = "TS_ButtonEnable0"  # physical channel = Sim_PC_basedDAQ/ao0
DC_RMS_VOLTAGE_TEST_POINT_CHANNEL = "TP_LineOut0:1"  # physical channel = Sim_PC_basedDAQ/ai0:1

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\action_button_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    button_channel=BUTTON_CHANNEL,
    voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL,
):
    """Creates the necessary objects for the simulation and measurement of the action button"""  

    # Create the instances of generation and measurement classes required for the test.
    button_instance = daq.DcVoltageGeneration()
    dc_rms_voltage_test_point = daq.DcRmsVoltageMeasurement()

    # Initialize Action Button
    """Initializes the configured channels of AO module to perform action button functionality"""
    button_instance.initialize(analog_output_channel_expression=button_channel)

    # Initialize TP
    """Initializes the configured channels of AI module to perform DC-RMS voltage measuerement"""
    dc_rms_voltage_test_point.initialize(analog_input_channel_expression=voltage_channel)

    return button_instance, dc_rms_voltage_test_point


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    button_instance: daq.DcVoltageGeneration,
    dc_rms_voltage_test_point: daq.DcRmsVoltageMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\action_button_test_results.txt
    """  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(button_instance)
        logger.attach(dc_rms_voltage_test_point)

    """Button ON Action"""

    # create a configuration that will generate 3.3V to simulate a button press
    button_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        output_voltages=[3.3],  # ON voltage = 3.3V
    )

    """Note to run with Hardware: Update DC Voltage for Action Button ON condition  # noqa: W505 - doc line too long (176 > 100 characters) (auto-generated noqa)
       This step can be replaced with actual button action"""

    # Turn ON the simulated button using CONFIGURE_AND_GENERATE method
    button_instance.configure_and_generate(configuration=button_configuration)

    """To ensure the DUT can detect the action button changes, you can add
    a short software delay after the voltage is generated:"""

    # uncomment the next two lines to create a 100 millisecond delay after 3.3V signal is generated
    # import time
    # time.sleep(.1)

    # Acquire the data from the test points using CONFIGURE_AND_MEASURE (button should be on)
    test_point_result_data_after_button_on = dc_rms_voltage_test_point.configure_and_measure(
        configuration=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    )

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["on"] = test_point_result_data_after_button_on

    """ Button OFF Action """
    """ Note to run with Hardware: Update DC Voltage for Action Button OFF condition 
        This step can be replaced with actual button action"""

    # Reconfigure the button object with 0V to prepare it to turn off in next step
    button_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        output_voltages=[0.0],  # OFF voltage = 0V
    )

    # Run CONFIGURE_AND_GENERATE again with 0V setting to ensure the button is turned OFF
    button_instance.configure_and_generate(configuration=button_configuration)

    # Acquire the data from the test points again using CONFIGURE_AND_MEASURE (button should be off)
    test_point_result_data_after_button_off = dc_rms_voltage_test_point.configure_and_measure(
        configuration=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    )

    # record intermediate result
    results_map["off"] = test_point_result_data_after_button_off

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(button_instance, dc_rms_voltage_test_point):
    """Closes out the created objects used in the generation and measurement"""  
    button_instance.close()  # Close Action Button
    dc_rms_voltage_test_point.close()  # Close TP


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def action_button_test(
    button_channel=BUTTON_CHANNEL,
    voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    button, voltage_test_point = setup(button_channel, voltage_channel)

    # Run main function
    main(button, voltage_test_point, write_to_file, filepath)

    # Run cleanup function
    cleanup(button, voltage_test_point)


####################################################################################################
# endregion test 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/turn_off_all_ao_channels.py sha256=e36a7683b60c839e975738782e28123b3a701e2d795b9e2c7a5e9e5890257a9d bytes=1767 -->
## FILE: src/nipcbatt/pcbatt_automation/action_button_tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/action_button_tests/turn_off_all_ao_channels.py`
- sha256: `e36a7683b60c839e975738782e28123b3a701e2d795b9e2c7a5e9e5890257a9d`
- bytes: 1767

````python
"""This example resets all configured Analog output channels to 0 volts"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0:3"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (250 > 100 characters) (auto-generated noqa)

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0, 0.0, 0.0, 0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/__init__.py sha256=039e02948e794862d8c0bf7da504f91f6cf3a0ca17bd7a43741228c43def206f bytes=48 -->
## FILE: src/nipcbatt/pcbatt_automation/audio_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/audio_tests/__init__.py`
- sha256: `039e02948e794862d8c0bf7da504f91f6cf3a0ca17bd7a43741228c43def206f`
- bytes: 48

````python
"""Contains files for audio test sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_filter_check.py sha256=a40c24430b225034bc0046643e7f82d97c5dcb8d7188158b276849ca9e84ef9a bytes=9205 -->
## FILE: src/nipcbatt/pcbatt_automation/audio_tests/audio_filter_check.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/audio_tests/audio_filter_check.py`
- sha256: `a40c24430b225034bc0046643e7f82d97c5dcb8d7188158b276849ca9e84ef9a`
- bytes: 9205

````python
"""Example demonstrates Frequency domain measurements(extraction of tones) of captured 
   Analog(Audio) signal generated by Analog Output(generates multi tones) module 
   with Hardware Trigger"""  

# pylint: disable=W0105

# import functions

# Note to run with Hardware: Update Virtual/Physical Channels Info based
# on NI MAX in the below Initialize Steps

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Default channels
GEN_CHANNEL = "TS_AudioLineIn0"  # Virtual Channel for TS Analog Out
MEAS_CHANNEL = "TP_AudioLineOut0"  # Virtual Channel for Test Points

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\audio_filter_check_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup():
    """Creates the necessary objects for signal generation and measurement"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.SignalVoltageGeneration()
    measurement_instance = daq.FrequencyDomainMeasurement()

    # Initialize generation
    generation_instance.initialize(channel_expression=GEN_CHANNEL)

    # Initialize measurement
    measurement_instance.initialize(analog_input_channel_expression=MEAS_CHANNEL)

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################

"""Note to run with Hardware: Review the configuration & update Trigger Source settings 
   based on NI MAX"""


def main(
    generation_instance: daq.SignalVoltageGeneration,
    measurement_instance: daq.FrequencyDomainMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling audio_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\audio_filter_check_test_results.txt""" 

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure Freq Domain Measurement setting to wait for Hardware Trigger"""
    # This creates an instrument measurment configuration to stand by for generation
    spec_chan_params = []
    meas_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    glob_chan_params = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10.0,
        range_max_volts=10.0,
    )

    timing_params = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        number_of_samples_per_channel=10000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    meas_config_configure_only = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=glob_chan_params,
        specific_channels_parameters=spec_chan_params,
        measurement_options=meas_options,
        sample_clock_timing_parameters=timing_params,
        digital_start_trigger_parameters=trigger_params,
    )

    # configure measurement and wait for generation
    measurement_instance.configure_and_measure(configuration=meas_config_configure_only)

    # generate multi-tone wave and trigger to initiate measurement
    vol_gen_range_params = daq.VoltageGenerationChannelParameters(
        range_min_volts=-10.0, range_max_volts=10.0
    )

    tone_params0 = daq.ToneParameters(
        tone_frequency_hertz=10.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    tone_params1 = daq.ToneParameters(
        tone_frequency_hertz=100.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    tone_params2 = daq.ToneParameters(
        tone_frequency_hertz=1000.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    tone_params3 = daq.ToneParameters(
        tone_frequency_hertz=10000.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    multi_tone_params = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_offset_volts=0.0,
        generated_signal_amplitude_volts=1.0,
        multiple_tones_parameters=[tone_params0, tone_params1, tone_params2, tone_params3],
    )

    gen_timing_params = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=0.1,
    )

    gen_trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    gen_config = daq.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=vol_gen_range_params,
        waveform_parameters=multi_tone_params,
        timing_parameters=gen_timing_params,
        digital_start_trigger_parameters=gen_trigger_params,
    )

    # start generation
    generation_instance.configure_and_generate_multiple_tones_waveform(configuration=gen_config)

    # Measures the analog input voltage waveforms (Started measure when signal voltage generation
    # sends Trigger after source) and returns Freq Domain

    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    trigger_params_postgen = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    meas_config_postgen = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=glob_chan_params,
        specific_channels_parameters=spec_chan_params,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=timing_params,
        digital_start_trigger_parameters=trigger_params_postgen,
    )

    # fetch TP measurements
    audio_filter_data = measurement_instance.configure_and_measure(
        configuration=meas_config_postgen
    )

    """Storing results -- create both a Python dictionary (hashmap)  
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["FILTER DATA"] = audio_filter_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(generation_instance, measurement_instance):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def audio_filter_check(
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    generation_instance, measurement_instance = setup()

    # Run main function
    main(generation_instance, measurement_instance, write_to_file, filepath)

    # Run cleanup function
    cleanup(generation_instance, measurement_instance)


####################################################################################################
# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_line_check.py sha256=1fb2b65e4900f2a2f0b9aa359e8421b6f7963eaab6ce3680bd9eadec7813f105 bytes=8503 -->
## FILE: src/nipcbatt/pcbatt_automation/audio_tests/audio_line_check.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/audio_tests/audio_line_check.py`
- sha256: `1fb2b65e4900f2a2f0b9aa359e8421b6f7963eaab6ce3680bd9eadec7813f105`
- bytes: 8503

````python
"""Example demonstrates Frequency domain measurements(extraction of tones) of captured
   Analog(Audio) signal generated by Analog Output(generates sine wave tones) module 
   with Hardware Trigger"""  


# Note to run with Hardware: Update Virtual/Physical Channels Info based on NI MAX
# in the below Initialize Steps

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Default channels
GEN_CHANNEL = "TS_AudioLineIn0"  # Virtual Channel for TS Analog Out
MEAS_CHANNEL = "TP_AudioLineOut0"  # Virtual Channel for Test Points

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\audio_line_check_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup():
    """Creates the necessary objects for signal generation and measurement"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.SignalVoltageGeneration()
    measurement_instance = daq.FrequencyDomainMeasurement()

    # Initialize generation
    generation_instance.initialize(channel_expression=GEN_CHANNEL)

    # Initialize measurement
    measurement_instance.initialize(analog_input_channel_expression=MEAS_CHANNEL)

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################

"""Note to run with Hardware: Review the configuration & update Trigger Source settings 
   based on NI MAX"""


def main(
    generation_instance: daq.SignalVoltageGeneration,
    measurement_instance: daq.FrequencyDomainMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling audio_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\audio_line_check_test_results.txt""" 

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure Freq Domain Measurement setting to wait for Hardware Trigger"""
    glob_chan_params = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10.0,
        range_max_volts=10.0,
    )

    spec_chan_params = []
    meas_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    timing_params = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    meas_config_configure_only = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=glob_chan_params,
        specific_channels_parameters=spec_chan_params,
        measurement_options=meas_options,
        sample_clock_timing_parameters=timing_params,
        digital_start_trigger_parameters=trigger_params,
    )

    # configure measurement and wait for generation
    measurement_instance.configure_and_measure(configuration=meas_config_configure_only)

    # generate sine wave and trigger to initiate measurement
    vol_gen_range_params = daq.VoltageGenerationChannelParameters(
        range_min_volts=-2.0, range_max_volts=2.0
    )

    tone_params = daq.ToneParameters(
        tone_frequency_hertz=1000.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    waveform_params = daq.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0.0, generated_signal_tone_parameters=tone_params
    )

    gen_timing_params = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=0.1,
    )

    gen_trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    gen_config = daq.SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=vol_gen_range_params,
        waveform_parameters=waveform_params,
        timing_parameters=gen_timing_params,
        digital_start_trigger_parameters=gen_trigger_params,
    )

    # start generation
    generation_instance.configure_and_generate_sine_waveform(configuration=gen_config)

    # Measures the analog input voltage waveforms (Started measure when signal voltage generation
    # sends Trigger after source) and returns Freq Domain

    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    trigger_params_measure_only = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    meas_config_postgen = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=glob_chan_params,
        specific_channels_parameters=spec_chan_params,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=timing_params,
        digital_start_trigger_parameters=trigger_params_measure_only,
    )

    # fetch TP measurements
    audio_data = measurement_instance.configure_and_measure(configuration=meas_config_postgen)

    """Storing results -- create both a Python dictionary (hashmap) 
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["FREQ DATA"] = audio_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(generation_instance, measurement_instance):
    """Closes out the created objects used in the generation and measurement""" 
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def audio_line_check(
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    generation_instance, measurement_instance = setup()

    # Run main function
    main(generation_instance, measurement_instance, write_to_file, filepath)

    # Run cleanup function
    cleanup(generation_instance, measurement_instance)


####################################################################################################
# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_test_main_sequence.py sha256=59b287bbb17284f8e4a645f4e4325e85cf2109ff35b7ee7cea4d7a61159c410f bytes=1232 -->
## FILE: src/nipcbatt/pcbatt_automation/audio_tests/audio_test_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/audio_tests/audio_test_main_sequence.py`
- sha256: `59b287bbb17284f8e4a645f4e4325e85cf2109ff35b7ee7cea4d7a61159c410f`
- bytes: 1232

````python
"""Main sequence for executing audio test sequence""" 


# import functions
from nipcbatt.pcbatt_automation.audio_tests.audio_filter_check import audio_filter_check
from nipcbatt.pcbatt_automation.audio_tests.audio_line_check import audio_line_check
from nipcbatt.pcbatt_automation.audio_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

""" Demonstrates extraction of tones (Frequency domain measurement) from the captured 
    Audio Signal (Single tone sine wave)"""

audio_line_check()

"""Example 2 - Demonstrates extraction of tones (Frequency domain measurement) from 
   the captured Multi tone Audio Signal"""

audio_filter_check()

######## CLEAN UP #####################

# Turn off all configured AO channels by configuring to 0V
power_down_all_ao_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/turn_off_all_ao_channels.py sha256=e36a7683b60c839e975738782e28123b3a701e2d795b9e2c7a5e9e5890257a9d bytes=1767 -->
## FILE: src/nipcbatt/pcbatt_automation/audio_tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/audio_tests/turn_off_all_ao_channels.py`
- sha256: `e36a7683b60c839e975738782e28123b3a701e2d795b9e2c7a5e9e5890257a9d`
- bytes: 1767

````python
"""This example resets all configured Analog output channels to 0 volts"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0:3"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (250 > 100 characters) (auto-generated noqa)

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0, 0.0, 0.0, 0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/__init__.py sha256=fd99214e6156fc84336823f539d9e020528d4a10a9a145541a91bac7e47396ea bytes=68 -->
## FILE: src/nipcbatt/pcbatt_automation/communication_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/communication_tests/__init__.py`
- sha256: `fd99214e6156fc84336823f539d9e020528d4a10a9a145541a91bac7e47396ea`
- bytes: 68

````python
"""Contains all files necessary to run communication sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/communication_test_main_sequence.py sha256=d9dc3c34ce211e44bbfe447a4a00c360f77ded71c77fd624af670e672b60a730 bytes=898 -->
## FILE: src/nipcbatt/pcbatt_automation/communication_tests/communication_test_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/communication_tests/communication_test_main_sequence.py`
- sha256: `d9dc3c34ce211e44bbfe447a4a00c360f77ded71c77fd624af670e672b60a730`
- bytes: 898

````python
"""Main sequence for executing communication test sequence"""  


# import functions
from nipcbatt.pcbatt_automation.communication_tests.i2c_comm_test import i2c_comm_test
from nipcbatt.pcbatt_automation.communication_tests.serial_comm_test import (
    serial_comm_test,
)
from nipcbatt.pcbatt_automation.communication_tests.spi_comm_test import spi_comm_test

"""Note to run with simulation: Test sequence cannot be executed in simulation mode"""

############# MAIN ####################

# Example demonstrates simple read and write data operations through I2C protocol
# communication using NI 845x Device

i2c_comm_test()

# Example demonstrates simple read and write data operations through SPI protocol
# communication using NI 845x Device

spi_comm_test()

## Example demonstrates simple read and write data operations through Serial COM port

serial_comm_test()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/i2c_comm_test.py sha256=2c11eba8087d7600042b20261c7962f8320aa6d011cc4d87ab8207755159dc28 bytes=5942 -->
## FILE: src/nipcbatt/pcbatt_automation/communication_tests/i2c_comm_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/communication_tests/i2c_comm_test.py`
- sha256: `2c11eba8087d7600042b20261c7962f8320aa6d011cc4d87ab8207755159dc28`
- bytes: 5942

````python
"""Example demonstrates simple read and write data operations through I2C protocol
communication using NI 845x Device""" 


import numpy as np

# import functions
import nipcbatt
from nipcbatt import communications
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Note to run with Hardware: Update Device ID of the connected
# I2C Interface Device (Ex: NI USB-8452 Device)

DEVICE_ID = "DeviceA"
SESSION_NUMBER = 0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\i2c_comm_test_results.txt"


# region initialize
######## INITIALIZE ################################################################################
def setup():
    """Creates and initializes I2C communication objects"""  

    reader = communications.I2cReadCommunication()
    reader.initialize(device_name=DEVICE_ID)

    writer = communications.I2cWriteCommunication()
    writer.initialize(device_name=DEVICE_ID)

    return reader, writer


# endregion initialize


# region configure
####### CONFIGURE/READ & CONFIGURE/WRITE DATA ######################################################
def main(
    reader: communications.I2cReadCommunication,
    writer: communications.I2cWriteCommunication,
    write_to_file: bool,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling i2c_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\i2c_comm_test_results.txt""" 

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=DEFAULT_FILEPATH)
        logger.attach(reader)
        logger.attach(writer)

    """Note to run with Hardware: Update Read data settings for I2C communication"""
    read_dev_params = communications.I2cDeviceParameters(
        enable_i2c_pullup_resistor=False, voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    read_comm_params = communications.I2cCommunicationParameters(
        device_address=80,  # 0x50
        addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_7_BIT,
        clock_rate_kilohertz=100,
        ack_poll_timeout_milliseconds=10000,
    )

    read_mem_params = communications.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    read_params = communications.I2cReadParameters(
        number_of_bytes_to_read=128, memory_address_parameters=read_mem_params
    )

    read_config = communications.I2cReadCommunicationConfiguration(
        device_parameters=read_dev_params,
        communication_parameters=read_comm_params,
        read_parameters=read_params,
    )

    read_data = reader.configure_and_read_data(configuration=read_config)

    # Note to run with Hardware: Update Write data settings for I2C communication
    write_dev_params = communications.I2cDeviceParameters(
        enable_i2c_pullup_resistor=False, voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    write_comm_params = communications.I2cCommunicationParameters(
        device_address=80,  # 0x50
        addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_7_BIT,
        clock_rate_kilohertz=100,
        ack_poll_timeout_milliseconds=10000,
    )

    data = [np.ubyte(0xAB), np.ubyte(0x1D), np.ubyte(0x11), np.ubyte(0xFF)]
    data_to_write = np.array(data)

    write_mem_params = communications.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    write_params = communications.I2cWriteParameters(
        number_of_bytes_per_page=128,
        delay_between_page_write_operations_milliseconds=4,
        data_to_be_written=data_to_write,
        memory_address_parameters=write_mem_params,
    )

    write_config = communications.I2cWriteCommunicationConfiguration(
        device_parameters=write_dev_params,
        communication_parameters=write_comm_params,
        write_parameters=write_params,
    )

    writer.configure_and_write_data(configuration=write_config)

    """Storing results -- create both a Python dictionary (hashmap) 
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["I2C DATA"] = read_data

    return read_data


# endregion configure


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    reader: communications.I2cReadCommunication,
    writer: communications.I2cWriteCommunication,
):
    """Closes out the created objects used in the communication"""  
    reader.close()
    writer.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def i2c_comm_test():
    """Execute all steps in the sequence"""  

    # Run setup function
    i2c_reader, i2c_writer = setup()

    # Run main function
    main(reader=i2c_reader, writer=i2c_writer, write_to_file=True)

    # run cleanup function
    cleanup(i2c_reader, i2c_writer)


####################################################################################################
# endregion test 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/serial_comm_test.py sha256=337ed329c143bc0c5846a7e850e945d43fdce561745d744f3e43bb80af944e36 bytes=3779 -->
## FILE: src/nipcbatt/pcbatt_automation/communication_tests/serial_comm_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/communication_tests/serial_comm_test.py`
- sha256: `337ed329c143bc0c5846a7e850e945d43fdce561745d744f3e43bb80af944e36`
- bytes: 3779

````python
"""Example demonstrates simple read and write data operations through Serial COM port"""  

# pylint: disable=W0105

import pyvisa
import pyvisa.constants

# import functions
from nipcbatt import communications
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Note to run with Hardware: Update Serial VISA for the COM port

DEVICE_ID = "DeviceB"
SESSION_NUMBER = 0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\serial_comm_test_results.txt"


# region initialize
######## INITIALIZE ################################################################################
def setup():
    """Creates and initializes serial communication object""" 
    resource = communications.SerialCommunication()
    resource.initialize(serial_device_name=DEVICE_ID)
    return resource


# endregion initialize


# region configure
####### CONFIGURE & READ/WRITE DATA ###############################################################
def main(
    resource: communications.SerialCommunication,
    write_to_file: bool,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling i2c_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\serial_comm_test_results.txt"""  

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=DEFAULT_FILEPATH)
        logger.attach(resource)

    """Note to run with Hardware: Update Serial comm settings for write-read operation"""

    # Update the Serial Write Command based on the usecase

    comm_params = communications.SerialCommunicationParameters(
        data_rate_bauds=9600,
        number_of_bits_in_data_frame=8,
        delay_before_receive_response_milliseconds=500,
        parity=pyvisa.constants.Parity.none,
        stop_bits=pyvisa.constants.StopBits.one,
        flow_control=pyvisa.constants.ControlFlow,
    )

    command = "IDN?\n"  # Update the command to send

    config = communications.SerialCommunicationConfiguration(
        communication_parameters=comm_params, command_to_send=command
    )

    response_data = resource.configure_then_send_command_and_receive_response(configuration=config)

    """Storing results -- create both a Python dictionary (hashmap) 
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["SERIAL DATA"] = response_data.received_response()

    return response_data


# endregion configure


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(resource: communications.SerialCommunication):
    """Closes out the created objects used in the communication""" 
    resource.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def serial_comm_test():
    """Execute all steps in the sequence"""  

    # Run setup function
    serial_resource = setup()

    # Run main function
    main(resource=serial_resource, write_to_file=True)

    # run cleanup function
    cleanup(serial_resource)


####################################################################################################
# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/spi_comm_test.py sha256=cb8043303b08ebb4d5dbe82106ceb798bf52ec4a6aff16870598cdcedaf9ec31 bytes=5934 -->
## FILE: src/nipcbatt/pcbatt_automation/communication_tests/spi_comm_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/communication_tests/spi_comm_test.py`
- sha256: `cb8043303b08ebb4d5dbe82106ceb798bf52ec4a6aff16870598cdcedaf9ec31`
- bytes: 5934

````python
"""Example demonstrates simple read and write data operations through SPI 
   protocol communication using NI 845x Device """ 


import numpy as np

# import functions
import nipcbatt
from nipcbatt import communications
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Note to run with Hardware: Update Device ID of the connected SPI Interface Device
# (Ex: NI USB-8452 Device)

DEVICE_ID = "DeviceA"
SESSION_NUMBER = 0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\spi_comm_test_results.txt"


# region initialize
######## INITIALIZE ################################################################################
def setup():
    """Creates and initializes SPI communication objects"""  

    reader = communications.SpiReadCommunication()
    reader.initialize(device_name=DEVICE_ID)

    writer = communications.SpiWriteCommunication()
    writer.initialize(device_name=DEVICE_ID)

    return reader, writer


# endregion initialize


# region configure
####### CONFIGURE/READ & CONFIGURE/WRITE DATA ######################################################
def main(
    reader: communications.SpiReadCommunication,
    writer: communications.SpiWriteCommunication,
    write_to_file: bool,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling spi_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\spi_comm_test_results.txt""" 

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=DEFAULT_FILEPATH)
        logger.attach(reader)
        logger.attach(writer)

    """Note to run with Hardware: Update Read data settings for SPI communication"""
    read_dev_params = communications.SpiDeviceParameters(
        voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    read_comm_params =communications.SpiCommunicationParameters(
        chip_select=0,
        clock_rate_kilohertz=1000,
        clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
        clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
    )

    read_mem_params = communications.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    read_params = communications.SpiReadParameters(
        number_of_bytes_to_read=32, memory_address_parameters=read_mem_params
    )

    read_config =communications.SpiReadCommunicationConfiguration(
        device_parameters=read_dev_params,
        communication_parameters=read_comm_params,
        read_parameters=read_params,
    )

    read_data = reader.configure_and_read_data(configuration=read_config)

    # Note to run with Hardware: Update Write data settings for SPI communication
    write_dev_params = communications.SpiDeviceParameters(
        voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    write_comm_params = communications.SpiCommunicationParameters(
        chip_select=0,
        clock_rate_kilohertz=1000,
        clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
        clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
    )

    data = [np.ubyte(0xAB), np.ubyte(0x1D), np.ubyte(0x11), np.ubyte(0xFF)]
    data_to_write = np.array(data)

    write_mem_params = communications.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    write_params = communications.SpiWriteParameters(
        number_of_bytes_per_page=32,
        delay_between_page_write_operations_milliseconds=5,
        data_to_be_written=data_to_write,
        memory_address_parameters=write_mem_params,
    )

    write_config = communications.SpiWriteCommunicationConfiguration(
        device_parameters=write_dev_params,
        communication_parameters=write_comm_params,
        write_parameters=write_params,
    )

    writer.configure_and_write_data(configuration=write_config)

    """Storing results -- create both a Python dictionary (hashmap) 
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["SPI DATA"] = read_data

    return read_data


# endregion configure

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    reader: communications.SpiReadCommunication,
    writer: communications.SpiWriteCommunication,
):
    """Closes out the created objects used in the communication""" 
    reader.close()
    writer.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def spi_comm_test():
    """Execute all steps in the sequence"""  

    # Run setup function
    spi_reader, spi_writer = setup()

    # Run main function
    main(reader=spi_reader, writer=spi_writer, write_to_file=True)

    # run cleanup
    cleanup(spi_reader, spi_writer)


####################################################################################################
# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/__init__.py sha256=40eb93f9bc580135e633464ff34d1b814fd4b5b14b608fab8a577f96172414b4 bytes=51 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/__init__.py`
- sha256: `40eb93f9bc580135e633464ff34d1b814fd4b5b14b608fab8a577f96172414b4`
- bytes: 51

````python
"""Contains files for digital test automation""" 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_clock_test.py sha256=571cd8109f0b496ef3e5232ea9b32cff84ccaf3a3b314aec39d2223babea47a0 bytes=7210 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_clock_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_clock_test.py`
- sha256: `571cd8109f0b496ef3e5232ea9b32cff84ccaf3a3b314aec39d2223babea47a0`
- bytes: 7210

````python
"""Demonstrates digital clock generation and frequency measurement through 
   counter-based measurements using Digital IO lines or Modules.""" 

import time  # noqa: F401 - 'time' imported but unused (auto-generated noqa)

from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Please note that usage of TestScale PFI7 and PFI3 for digital clock is arbitary, but in
   TestScale the same core module can only be divided into 4 Inputs / 4 Outputs"""

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX
   in the below initialize step"""


# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # input terminal to measure the digital clock
MEAS_PHYSICAL_CHANNEL_COUNTER = "Simulated_Core/ctr1"  # counter used for digital clock measurement

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_clock_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of digital clock"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.DigitalClockGeneration()
    measurement_instance = daq.DigitalFrequencyMeasurement()

    # Initialize generation object
    """Initializes the channels of the DCG module to prepare for generation"""
    generation_instance.initialize(
        counter_channel_expression=gen_counter_channel,
        output_terminal_name=output_terminal,
    )

    # Initialize measurement object
    """Initializes the channels of the DFM module to prepare for measurement"""
    measurement_instance.initialize(
        channel_expression=meas_counter_channel, input_terminal_name=input_terminal
    )

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.DigitalClockGeneration,
    measurement_instance: daq.DigitalFrequencyMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_clock_test_results.txt""" 
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Update the digital clock settings based on the required pulse  
    train to be generated in the below step"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # initialize instances of counter channel parameters and timing parameters for generation
    # then initialize an instance of 'DigitalClockGenerationConfiguration' with the settings
    frequency, duty_cycle, duration = 1000.0, 0.5, 0.5
    gen_channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
        frequency_hertz=frequency, duty_cycle_ratio=duty_cycle
    )

    gen_timing_parameters = daq.DigitalClockGenerationTimingParameters(
        clock_duration_seconds=duration
    )

    gen_configuration = daq.DigitalClockGenerationConfiguration(
        counter_channel_parameters=gen_channel_parameters, timing_parameters=gen_timing_parameters
    )

    # launch generation with configure_and_generate
    generation_instance.configure_and_generate(configuration=gen_configuration)

    ## initialize instances of range and counter channel parameters for measuremennt
    # then initialize an instance of 'DigitalFrequencyMeasurementConfiguration' with the settings
    minimum, maximum, divisor, measurement_time = 2, 100, 4, 0.001
    meas_range_parameters = daq.DigitalFrequencyRangeParameters(
        frequency_minimum_value_hertz=minimum, frequency_maximum_value_hertz=maximum
    )

    meas_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        input_divisor_for_frequency_measurement=divisor,
        measurement_duration_seconds=measurement_time,
    )

    meas_configuration = daq.DigitalFrequencyMeasurementConfiguration(
        counter_channel_configuration_parameters=meas_channel_parameters
    )

    # launch measurement with configure_and_measure
    freq_data = measurement_instance.configure_and_measure(configuration=meas_configuration)

    # record results
    results_map["FREQUENCY DATA"] = freq_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DigitalClockGeneration,
    measurement_instance: daq.DigitalFrequencyMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_clock_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence""" 

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        meas_counter_channel=measurement_counter_channel,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_hw_timed.py sha256=fc8a851af2da701000c4f6c42ae08e73bce4e63105df6c32672ee51474411999 bytes=8171 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_hw_timed.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_hw_timed.py`
- sha256: `fc8a851af2da701000c4f6c42ae08e73bce4e63105df6c32672ee51474411999`
- bytes: 8171

````python
"""This example demonstrates digital pattern generation and digital edge count measurement through
   counter-based measurements using Digital IO Lines or Modules. Digital edge counting is 
   performed at Hardware timed using with Trigger to create a measurement window for 
   fixed duration"""  

import nidaqmx
import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_library.common.helper_functions import (
    digital_ramp_pattern_generator,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminals and Global/Physical Channels based on NI MAX 
   in the below initialize step"""

# Default channels
GENERATION_CHANNEL = "TS_DIn1"  # global channel to use for digital pattern generation
SESSION_NUMBER = 0

INPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI0"
EDGE_COUNTER = "Sim_PC_basedDAQ/ctr0"
COUNTER_TIMER = "Sim_PC_basedDAQ/ctr1"

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_edge_count_hw_timed_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup():
    """Creates the necessary objects for the generation and measurement of digital edge count"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.DynamicDigitalPatternGeneration()
    measurement_instance = daq.DigitalEdgeCountMeasurementUsingHardwareTimer()

    # initialize generation object
    generation_instance.initialize(channel_expression=GENERATION_CHANNEL)

    # initialize measurement object
    measurement_instance.initialize(
        measurement_channel_expression=EDGE_COUNTER,
        measurement_input_terminal_name=INPUT_TERMINAL,
        timer_channel_expression=COUNTER_TIMER,
    )

    # return initialzied objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################


def main(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DigitalEdgeCountMeasurementUsingHardwareTimer,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_edge_count_hw_timed_test_results.txt""" 
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Review the Configurations and update the Trigger &  # noqa: W505 - doc line too long (358 > 100 characters) (auto-generated noqa)
    Counter configurations"""

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # configure trigger
    trig_type = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
    trig_source = "/Sim_PC_basedDAQ/do/StartTrigger"  # Update trigger source according to hw setup
    trig_edge = nidaqmx.constants.Edge.RISING
    trig_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=trig_type,
        digital_start_trigger_source=trig_source,
        digital_start_trigger_edge=trig_edge,
    )

    # configure timing

    configure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    channel_params = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
        edge_type=daq.ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE
    )

    timing_params = daq.DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.1)

    # create configuration out of trigger and timing configs
    init_config = daq.DigitalEdgeCountHardwareTimerConfiguration(
        measurement_options=configure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
        trigger_parameters=trig_params,
    )

    # apply configuration to measurement instance
    # configures and arms to measure digital edges on rising edge of trigger
    measurement_instance.configure_and_measure(configuration=init_config)

    """Note to run with Hardware: Review & update the "Number of Digital Lines" and 
       "Number of Samples" required to be generated"""

    # create ramp pattern
    num_lines, num_samples = 1, 50
    data = digital_ramp_pattern_generator(num_lines, num_samples)

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
    )

    # create generation configuration
    gen_config = daq.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=trig_params,
        pulse_signal=digital_port_data,
    )

    # configure and generate the digital pattern
    generation_instance.configure_and_generate(
        configuration=gen_config, pulse_signal=digital_port_data
    )

    # configuration for measure only
    measure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # create configuration from post trigger option settings
    config_meas_only = daq.DigitalEdgeCountHardwareTimerConfiguration(
        measurement_options=measure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
        trigger_parameters=trig_params,
    )

    # read the digital edge counts
    result_data = measurement_instance.configure_and_measure(configuration=config_meas_only)

    # record results
    results_map["HW TIMED COUNT DATA"] = result_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DigitalEdgeCountMeasurementUsingHardwareTimer,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_count_events_sw_timed_test(
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    gen, meas = setup()

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_sw_timed.py sha256=0afac02014cadf65ea27cc8a7093f9c7eaa8e6e259c4615de2544f77e4bb6bc6 bytes=7683 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_sw_timed.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_sw_timed.py`
- sha256: `0afac02014cadf65ea27cc8a7093f9c7eaa8e6e259c4615de2544f77e4bb6bc6`
- bytes: 7683

````python
"""This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait"""  

import time  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX 
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # terminal to measure the digital edge count measurements
EDGE_COUNTER = "Simulated_Core/ctr1"  # counter used for digital edge count ceasurements

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_edge_count_sw_timed_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    edge_count_channel=EDGE_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of digital edge count"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.DigitalPulseGeneration()
    measurement_instance = daq.DigitalEdgeCountMeasurementUsingSoftwareTimer()

    # Initialize generation object
    generation_instance.initialize(
        channel_expression=gen_counter_channel, output_terminal_name=output_terminal
    )

    # Initialize measurement object
    measurement_instance.initialize(
        measurement_channel_expression=edge_count_channel,
        measurement_input_terminal_name=input_terminal,
    )

    # return initialzied objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################


def main(
    generation_instance: daq.DigitalPulseGeneration,
    measurement_instance: daq.DigitalEdgeCountMeasurementUsingSoftwareTimer,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_edge_count_sw_timed_test_results.txt"""  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure and generate/measure signals"""

    """Storing results -- create both a Python dictionary (hashmap) 
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs
    configure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    channel_params = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
        edge_type=daq.ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE
    )

    timing_params = daq.DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.1)
    init_config = daq.DigitalEdgeCountSoftwareTimerConfiguration(
        measurement_options=configure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
    )

    # configures to measure digital edges
    measurement_instance.configure_and_measure(configuration=init_config)

    """Note to run with Hardware: Update the Digital pulse settings in the below step based 
       on the required digital signal to be generated"""

    # create constants needed to create generation configuration
    low_time, high_time, num_pulses = 0.0003, 0.0005, 2000
    level = daq.ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

    gen_counter_parameters = daq.DigitalPulseGenerationCounterChannelParameters(
        pulse_idle_state=level, low_time_seconds=low_time, high_time_seconds=high_time
    )

    gen_timing_parameters = daq.DigitalPulseGenerationTimingParameters(pulses_count=num_pulses)

    gen_config = daq.DigitalPulseGenerationConfiguration(
        counter_channel_parameters=gen_counter_parameters, timing_parameters=gen_timing_parameters
    )

    # generates digital pulse signals
    generation_instance.configure_and_generate(configuration=gen_config)

    """Note to run with Hardware: Update and uncomment the software wait time in the below step 
       based on the measurement window to be captured"""

    # time.sleep(0.1) #100 ms

    # create new configuration to read edge counts
    measure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_config = daq.DigitalEdgeCountSoftwareTimerConfiguration(
        measurement_options=measure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
    )

    # read the digital edge counts
    sw_count_data = measurement_instance.configure_and_measure(configuration=meas_config)

    # record results
    results_map["SW TIMED COUNT DATA"] = sw_count_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DigitalPulseGeneration,
    measurement_instance: daq.DigitalEdgeCountMeasurementUsingSoftwareTimer,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_count_events_sw_timed_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    edge_counter=EDGE_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        edge_count_channel=edge_counter,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_io_main_sequence.py sha256=c88fe1e661ec38c1799f23d2d36f8ce18bbfb6a39442d9cb90be5b934bbb709d bytes=2867 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_io_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_io_main_sequence.py`
- sha256: `c88fe1e661ec38c1799f23d2d36f8ce18bbfb6a39442d9cb90be5b934bbb709d`
- bytes: 2867

````python
"""Main sequence for executing Digital IO Test"""  

# import functions
from nipcbatt.pcbatt_automation.digital_io_tests.digital_clock_test import (
    digital_clock_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_count_events_sw_timed import (
    digital_count_events_sw_timed_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_pattern_test import (
    digital_pattern_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_pwm_test import (
    digital_pwm_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_state_test import (
    digital_state_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.turn_off_all_do_channels import (
    power_down_all_do_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################

"""Example 1 - Demonstrates static digital state generation and measurement using Digital 
   output and input lines or modules"""

digital_state_test()

"""Example 2 - Demonstrates digital pattern generation and measurement using Digital input 
   and output lines or modules, Hardware Trigger is used for synchronization between generate 
   and capture."""

digital_pattern_test()

"""Example 3 - Demonstrates digital clock generation and frequency measurement through 
   counter-based measurements using Digital IO lines or Modules."""

digital_clock_test()

"""Example 4 - Demonstrates digital pulse generation and PWM measurement through counter-based 
   measurements using Core Digital IO Modules."""

digital_pwm_test()

"""Example 5 - Demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait."""

digital_count_events_sw_timed_test()

#### Note to run with Hardware: Enable the below example for HW Run #####
"""Example 6 - Demonstrates digital pattern generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Hardware timed using with Trigger to create a measurement window for fixed duration."""

# the below test is disabled as hw timed count digital events will throw errors during simulation
# digital_count_events_tests_hw_timed()


######## CLEAN UP ####################

"""Turn off all configured DO channels by setting Digital LOW state"""

power_down_all_do_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pattern_test.py sha256=8d43ebab7d71785d72bb31f35b6db258639e800c9464b2edc548a61e0c3389e3 bytes=9118 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pattern_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pattern_test.py`
- sha256: `8d43ebab7d71785d72bb31f35b6db258639e800c9464b2edc548a61e0c3389e3`
- bytes: 9118

````python
"""This example demonstrates the digital pattern generation and capture using digital input and 
   output modules with trigger for synchronization"""  


import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_library.common.helper_functions import (
    digital_ramp_pattern_generator,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_DIn0:1"  # physical channel = Sim_PC_basedDAQ/port0/line0:1
MEASUREMENT_CHANNEL = "TP_DOut2:3"  # physical channel = Sim_PC_basedDAQ/port0/line2:3

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_pattern_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL):
    """Creates the necessary objects for the generation and measurement of digital patterns"""  

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = daq.DynamicDigitalPatternGeneration()
    measurement_instance = daq.DynamicDigitalPatternMeasurement()

    # Initialize generation object
    """Initializes the channel(s) of the DDPG module to prepare for generation"""
    generation_instance.initialize(channel_expression=generation_channel)

    # Initialize measurement object
    """Initializes the channel(s) of the DDPM module to prepare for measurement"""
    measurement_instance.initialize(channel_expression=measurement_channel)

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DynamicDigitalPatternMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_pattern_test_results.txt"""  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Review the configurations and update the trigger configurations"""

    """Note to run with Hardware: Sampling rate at measurement end should be same as the sampling  
       rate at generation end (Onboard Clock for same backplane or external PFI signals)"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    #### Create a configuration for measurement
    #### First configuration option will configure only

    # initialize an instance of 'MeasurementOptions' with options to configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    meas_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        digital_start_trigger_source="/Sim_PC_basedDAQ/do/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' to configure only
    meas_config_configure_only = daq.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_configure_only,
        timing_parameters=meas_timing_parameters,
        trigger_parameters=meas_trigger_parameters,
    )

    # use the config object to execute configure_and_measure and wait for generation
    measurement_instance.configure_and_measure(configuration=meas_config_configure_only)

    """Note to run with Hardware: Review & update the "number_of_digital_lines" and 
       "number_of_samples" required to be generated"""

    # create ramp data to output on digital port
    num_lines, num_samples = 2, 50
    data = digital_ramp_pattern_generator(
        number_of_digital_lines=num_lines, number_of_samples=num_samples
    )

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    """Note to run with Hardware: Sampling rate at generation and measurement should be same 
       (Onboard Clock for same Backplane or external PFI signals)"""

    # create a generation instance for DynamicDigitalPatternTimingParameters
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sample_clock_source="OnboardClock", sampling_rate_hertz=10000.0
    )

    # create a generation instance for DigitalStartTriggerParameters
    gen_trigger_parameters = daq.DynamicDigitalStartTriggerParameters(
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
    )

    # create an instance of DynamicDigitalPatternGenerationConfiguration
    generation_config = daq.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
        pulse_signal=digital_port_data,
    )

    # generate the configured digital pattern from the digital module
    generation_instance.configure_and_generate(configuration=generation_config)

    #### Second measurement configuration will skip configuring and go straight to measurement
    # initialize an instance of 'MeasurementOptions' with options to go measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for measure only
    meas_config_measure_only = daq.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_measure_only,
        timing_parameters=meas_timing_parameters,
        trigger_parameters=meas_trigger_parameters,
    )

    # read digital pattern stored in buffer (capture starts as soon as start
    # trigger is received from the digital output module)
    # use post trigger configuration
    result_data = measurement_instance.configure_and_measure(meas_config_measure_only)

    # record results
    results_map["DIGITAL DATA"] = result_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DynamicDigitalPatternMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_pattern_test(
    generation_channel=GENERATION_CHANNEL,
    measurement_channel=MEASUREMENT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence""" 

    # Run setup function
    gen, meas = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pwm_test.py sha256=fac13d684a530e62903bd26b26b9a2bccc6c2174ef9d3c20d0261e81763d385a bytes=8029 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pwm_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pwm_test.py`
- sha256: `fac13d684a530e62903bd26b26b9a2bccc6c2174ef9d3c20d0261e81763d385a`
- bytes: 8029

````python
"""This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait""" 


import time  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX 
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # input terminal to measure the digital clock
MEAS_PHYSICAL_CHANNEL_COUNTER = "Simulated_Core/ctr1"  # counter used for digital clock measurement
COUNTER_TIMER = ""  # No timer operation is performed in SW timed mode

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_pwm_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################

"""Note to run with Hardware: Update the Cycles to capture value in the below step based on the 
   digital signals to be measured"""


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of PWM""" 

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.DigitalPulseGeneration()
    measurement_instance = daq.DigitalPwmMeasurement()

    # Initialize generation object
    generation_instance.initialize(
        channel_expression=gen_counter_channel, output_terminal_name=output_terminal
    )

    # initialize measurement object
    measurement_instance.initialize(
        channel_expression=meas_counter_channel, input_terminal_name=input_terminal
    )

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.DigitalPulseGeneration,
    measurement_instance: daq.DigitalPwmMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_pwm_test_results.txt
    """ 
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Update the Cycles to capture value in the below step based on the  # noqa: W505 - doc line too long (176 > 100 characters) (auto-generated noqa)
    digital signals to be measured"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # create constants needed for measurement configuration objects
    min_semiperiod, max_semiperiod, cycles_count = 2.5e-8, 53.68709, 2
    edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
    execution_type_cfg_only = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

    # create configuration sub-objects
    meas_range_parameters = daq.DigitalPwmMeasurementRangeParameters(
        semi_period_minimum_value_seconds=min_semiperiod,
        semi_period_maximum_value_seconds=max_semiperiod,
    )

    meas_timing_parameters = daq.DigitalPwmMeasurementTimingParameters(
        semi_period_counter_wanted_cycles_count=cycles_count
    )

    meas_counter_parameters = daq.DigitalPwmMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        timing_parameters=meas_timing_parameters,
        semi_period_counter_starting_edge=edge,
    )

    # create configuration object to configure only
    meas_cfg_config_only = daq.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters, measurement_option=execution_type_cfg_only
    )

    # configure measurement instance
    measurement_instance.configure_and_measure(configuration=meas_cfg_config_only)

    """Note to run with Hardware: Update the digital pulse settings in the below step 
       based on the required digital signal to be generated"""

    # create constants needed to create generation configuration
    low_time, high_time, num_pulses = 0.003, 0.001, 100
    level = daq.ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

    gen_counter_parameters = daq.DigitalPulseGenerationCounterChannelParameters(
        pulse_idle_state=level, low_time_seconds=low_time, high_time_seconds=high_time
    )

    gen_timing_parameters = daq.DigitalPulseGenerationTimingParameters(pulses_count=num_pulses)

    gen_config = daq.DigitalPulseGenerationConfiguration(
        counter_channel_parameters=gen_counter_parameters, timing_parameters=gen_timing_parameters
    )

    # configure and generate generation instance
    generation_instance.configure_and_generate(configuration=gen_config)

    # create separate configuration to be used to measure only after generation has started
    execution_type_measure_only = nipcbatt.MeasurementExecutionType.MEASURE_ONLY
    meas_cfg_measure_only = daq.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters, measurement_option=execution_type_measure_only
    )

    # configure_and_measure with measure only
    pwm_data = measurement_instance.configure_and_measure(configuration=meas_cfg_measure_only)

    # record results
    results_map["PWM DATA"] = pwm_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DigitalPulseGeneration,
    measurement_instance: daq.DigitalPwmMeasurement,
):
    """Closes out the created objects used in the generation and measurement""" 
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close

# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_pwm_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        meas_counter_channel=measurement_counter_channel,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_state_test.py sha256=8e203fd08e6c2e0b95d67678b64375c4a50405d2c0d0e4bf1ffea03677dfe5b6 bytes=5726 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_state_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/digital_state_test.py`
- sha256: `8e203fd08e6c2e0b95d67678b64375c4a50405d2c0d0e4bf1ffea03677dfe5b6`
- bytes: 5726

````python
"""This example demonstrates how to set Digital High & Low states using digital output modules and 
   measure the digital states of test points using digital input modules""" 

import time  

from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_DIn0:1"  # physical channel = Sim_PC_basedDAQ/port0/line0:1
MEASUREMENT_CHANNEL = "TP_DOut2:3"  # physical channel = Sim_PC_basedDAQ/port0/line0:1

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_state_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL):
    """Creates the necessary objects for the generation and measurement of digital states""" 

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = daq.StaticDigitalStateGeneration()
    measurement_instance = daq.StaticDigitalStateMeasurement()

    # Initialze generation object
    """Intializes the channel(s) of the SDSG module to prepare for generation"""
    generation_instance.initialize(channel_expression=generation_channel)

    # Initialize measurement object
    """Initializes the channel(s) of the SDSM module to prepare for measurement"""
    measurement_instance.initialize(channel_expression=measurement_channel)

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.StaticDigitalStateGeneration,
    measurement_instance: daq.StaticDigitalStateMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_state_test_results.txt
    """  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with hardware: review the configurations for the intended use case"""

    """Storing results -- create both a Python dictionary (hashmap) 
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    """Sequence to set static state HIGH and measure the test points: """

    # create a generation configuration that will implement HIGH digital state(s)
    gen_data_high = [True] * generation_instance.task.number_of_channels
    gen_configuration = daq.StaticDigitalStateGenerationConfiguration(gen_data_high)

    # Generate digital states with the HIGH configuration
    lines = generation_instance.configure_and_generate(configuration=gen_configuration)

    # measure the digital states
    measurement_data_high = measurement_instance.configure_and_measure()

    # record the measurement into the dictionary
    results_map["HIGH"] = measurement_data_high

    """Sequence to set static state low and measure the test points: """

    # create a generation configuration that will implement LOW digital state(s)
    gen_data_low = [False] * generation_instance.task.number_of_channels
    gen_configuration = daq.StaticDigitalStateGenerationConfiguration(gen_data_low)

    # Generate digital state with the LOW configuration
    lines = generation_instance.configure_and_generate( 
        configuration=gen_configuration
    )

    # measure the digital states
    measurement_data_low = measurement_instance.configure_and_measure()

    # store digital LOW data in the results_map with corresponding keys
    results_map["LOW"] = measurement_data_low

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.StaticDigitalStateGeneration,
    measurement_instance: daq.StaticDigitalStateMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_state_test(
    generation_channel=GENERATION_CHANNEL,
    measurement_channel=MEASUREMENT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence""" 

    # Run setup function
    gen, meas = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/turn_off_all_do_channels.py sha256=a9f5d5bdc141bcde99a63235546aaab9533136faa43bbc5f7b4b99b5d7c0fb8e bytes=1556 -->
## FILE: src/nipcbatt/pcbatt_automation/digital_io_tests/turn_off_all_do_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/digital_io_tests/turn_off_all_do_channels.py`
- sha256: `a9f5d5bdc141bcde99a63235546aaab9533136faa43bbc5f7b4b99b5d7c0fb8e`
- bytes: 1556

````python
"""This example resets all configured Digital output channels voltage to 0 Volts"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

from nipcbatt import daq

# Note to run with Hardware: Update Virtual/Physical Channels Info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
DIGITAL_OUT_CHANNELS = "Sim_PC_basedDAQ/port0/line0:7"


def power_down_all_do_channels():
    """Set digital state to LOW on all digital output channels"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (253 > 100 characters) (auto-generated noqa)

    # declare list to hold boolean false values
    low_values = [False, False, False, False, False, False, False, False]

    # Static Digital State Generation -- Initialize DO channels
    generation = daq.StaticDigitalStateGeneration()
    generation.initialize(channel_expression=DIGITAL_OUT_CHANNELS)

    # create configuration for output
    output_config = daq.StaticDigitalStateGenerationConfiguration(data_to_write=low_values)

    # set digital state LOW for all Digital Output channels
    generation.configure_and_generate(configuration=output_config)

    # closes the Static Digital State Generation Task for Digital output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/Hardware Config.ini sha256=37571443e0c509c195ffc8c0d8371dcbb6a9c118628944aa12085399c816202c bytes=12184 -->
## FILE: src/nipcbatt/pcbatt_automation/Hardware Config.ini

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/Hardware Config.ini`
- sha256: `37571443e0c509c195ffc8c0d8371dcbb6a9c118628944aa12085399c816202c`
- bytes: 12184

````ini
[DAQmx]
MajorVersion = 25
MinorVersion = 8

[DAQmxChannel TP_Analog0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_Analog1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ1/ai0
Descr = 

[DAQmxChannel TP_AudioLineOut0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_Digital0]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxChannel TP_Digital1]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TP_Digital2]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ1/port0/line0
Descr = 

[DAQmxChannel TP_Digital3]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ1/port0/line1
Descr = 

[DAQmxChannel TP_DOut0]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxChannel TP_DOut1]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TP_DOut2]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line2
Descr = 

[DAQmxChannel TP_DOut3]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line3
Descr = 

[DAQmxChannel TP_LED0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_LineOut0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_LineOut1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai1
Descr = 

[DAQmxChannel TP_MIC0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_MIC1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai1
Descr = 

[DAQmxChannel TP_MIC2]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai2
Descr = 

[DAQmxChannel TP_Power0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai0
Descr = 

[DAQmxChannel TP_Power1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai1
Descr = 

[DAQmxChannel TP_Power2]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai2
Descr = 

[DAQmxChannel TP_PWM_LED0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = RSE
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai1
Descr = 

[DAQmxChannel TP_RTD]
AI.MeasType = Temperature:RTD
AI.RTD.R0 = 100
AI.RTD.Type = Pt3750
AI.Temp.Units = Deg C
AI.Max = 100
AI.Min = 0
AI.Excit.Src = Internal
AI.Excit.Val = 0.001
ChanType = Analog Input
AI.ResistanceCfg = 4-Wire
PhysicalChanName = Simulated_cDAQ_9217/ai0
Descr = 
AI.ADCTimingMode = High Resolution

[DAQmxChannel TP_Rth0]
AI.MeasType = Temperature:Thermistor
AI.Temp.Units = Deg C
AI.Thrmstr.R1 = 5000
AI.Max = 100
AI.Min = 0
AI.Excit.Src = External
AI.Excit.Val = 1
AI.Excit.VoltageOrCurrent = Voltage
ChanType = Analog Input
AI.ResistanceCfg = 4-Wire
AI.Thrmstr.A = 0.001295361
AI.Thrmstr.C = 1.018703E-07
AI.Thrmstr.B = 0.0002343159
PhysicalChanName = Simulated_AI/ai0
Descr = 

[DAQmxChannel TP_TC]
AI.MeasType = Temperature:Thermocouple
AI.Temp.Units = Deg C
AI.Thrmcpl.CJCChan = 
AI.Thrmcpl.CJCSrc = Built-In
AI.Thrmcpl.CJCVal = 25
AI.Thrmcpl.Type = J
AI.AutoZeroMode = Once
AI.Max = 100
AI.Min = 0
ChanType = Analog Input
PhysicalChanName = Simulated_cDAQ_9211/ai0
Descr = 

[DAQmxChannel TP_TH0]
AI.MeasType = Temperature:Thermistor
AI.Temp.Units = Deg C
AI.Thrmstr.R1 = 5000
AI.Max = 100
AI.Min = 0
AI.Excit.Src = External
AI.Excit.Val = 1
AI.Excit.VoltageOrCurrent = Voltage
ChanType = Analog Input
AI.ResistanceCfg = 4-Wire
AI.Thrmstr.A = 0.001295361
AI.Thrmstr.C = 1.018703E-07
AI.Thrmstr.B = 0.0002343159
PhysicalChanName = Simulated_cDAQ_9215/ai0
Descr = 

[DAQmxChannel TP_TH1]
AI.MeasType = Temperature:Thermistor
AI.Temp.Units = Deg C
AI.Max = 100
AI.Min = 0
AI.Excit.Src = External
AI.Excit.Val = 0.00015
AI.Excit.VoltageOrCurrent = Current
ChanType = Analog Input
AI.ResistanceCfg = 4-Wire
AI.Thrmstr.A = 0.001295361
AI.Thrmstr.C = 1.018703E-07
AI.Thrmstr.B = 0.0002343159
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_TH2]
AI.MeasType = Temperature:Thermistor
AI.Temp.Units = Deg C
AI.Thrmstr.R1 = 5000
AI.Max = 100
AI.Min = 0
AI.Excit.Src = External
AI.Excit.Val = 2.5
AI.Excit.VoltageOrCurrent = Voltage
ChanType = Analog Input
AI.ResistanceCfg = 4-Wire
AI.Thrmstr.A = 0.001295361
AI.Thrmstr.C = 1.018703E-07
AI.Thrmstr.B = 0.0002343159
PhysicalChanName = Simulated_AI/ai0
Descr = 

[DAQmxChannel TS_Analog0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_AudioLineIn0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_ButtonEnable0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_Digital0]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxChannel TS_Digital1]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TS_Digital2]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line2
Descr = 

[DAQmxChannel TS_Digital3]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line3
Descr = 

[DAQmxChannel TS_DIn0]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxChannel TS_DIn1]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TS_PWM_LED0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_Speaker0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_THEX]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Simulated_cDAQ_9263/ao0
Descr = 

[DAQmxDevice Dev1]
ProductType = USB-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74FB
BusType = USB

[DAQmxDevice Dev2]
ProductType = USB-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74FB
BusType = USB

[DAQmxDevice Sim_DMM]
ProductType = PXI-4065
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7357
BusType = PXI
PXI.ChassisNum = 1
PXI.SlotNum = 5

[DAQmxDevice Sim_MUX]
ProductType = PXI-2527
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x9040
BusType = PXI
PXI.ChassisNum = 1
PXI.SlotNum = 4
DefaultSwitchTopology = 1

[DAQmxDevice Sim_PC_basedDAQ]
ProductType = PCIe-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7431C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice Sim_PC_basedDAQ1]
ProductType = PCIe-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7431C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice Sim_SHUNT]
ProductType = PXI-2568
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x708C
BusType = PXI
PXI.ChassisNum = 1
PXI.SlotNum = 6
DefaultSwitchTopology = 0

[DAQmxDevice Sim_PXIeDAQ]
ProductType = PXIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7434C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 2

[DAQmxCDAQChassis Sim_cDAQ1]
ProductType = cDAQ-9178
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQChassis Sim_TS]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQChassis Sim_TS1]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule Simulated_AI]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule Simulated_AO]
ProductType = TS-15110
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule Simulated_cDAQ_9211]
ProductType = NI 9211
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_cDAQ1
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule Simulated_cDAQ_9215]
ProductType = NI 9215
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_cDAQ1
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule Simulated_cDAQ_9217]
ProductType = NI 9217
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_cDAQ1
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule Simulated_cDAQ_9263]
ProductType = NI 9263
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_cDAQ1
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule Simulated_Core]
ProductType = TS-15050 DIO P0
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule Simulated_DIO]
ProductType = TS-15120
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 5

[DAQmxCDAQModule Simulated_DO]
ProductType = TS-15130
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 6

[DAQmxCDAQModule Simulated_Power]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule Simulated_TS1_AI]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule Simulated_TS1_AO]
ProductType = TS-15110
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule Simulated_TS1_Core]
ProductType = TS-15050 DIO P0
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule Simulated_TS1_DIO]
ProductType = TS-15120
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 5

[DAQmxCDAQModule Simulated_TS1_DO]
ProductType = TS-15130
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 6

[DAQmxCDAQModule Simulated_TS1_Power]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 2
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/__init__.py sha256=76d74153c2ba95e79588292cd24376a02ccd7e7e7c622bdb09dd5460cd93635a bytes=54 -->
## FILE: src/nipcbatt/pcbatt_automation/LED_Tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/LED_Tests/__init__.py`
- sha256: `76d74153c2ba95e79588292cd24376a02ccd7e7e7c622bdb09dd5460cd93635a`
- bytes: 54

````python
"""Includes files for running LED Test sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/analog_pwm_test.py sha256=bb1144447a5e1b614cb993f208d5e9ad50243cdf0a19b57f66f54c11db1659e2 bytes=8430 -->
## FILE: src/nipcbatt/pcbatt_automation/LED_Tests/analog_pwm_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/LED_Tests/analog_pwm_test.py`
- sha256: `bb1144447a5e1b614cb993f208d5e9ad50243cdf0a19b57f66f54c11db1659e2`
- bytes: 8430

````python
"""Demonstrates Analog PWM Signal Generation and Time Domain Measurement using 
   AO and AI channels or Modules""" 

import os
import sys

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# To use save_traces and plotter from utils folder

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)


"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
   in the below initialize step"""
# Default channels
OUTPUT_TERMINAL = "TS_PWM_LED0"

INPUT_TERMINAL = "TP_PWM_LED0"

DIGITAL_TRIGGER_SOURCE = "/Sim_PC_basedDAQ/ao/StartTrigger"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Analog_PWM_Test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
# Initialize region
def setup(
    output_terminal=OUTPUT_TERMINAL,
    input_terminal=INPUT_TERMINAL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates necessary objects for the generation of Analog PWM siganl and
    Time Domain Measurement"""  
    # Creates instance of the generation class required for the test
    svg = daq.SignalVoltageGeneration()
    """Initializes the channels for signal volatge generaion"""
    svg.initialize(channel_expression=output_terminal)
    # Creates instance for the measurement class required for the test
    tdvm = daq.TimeDomainMeasurement()
    """Initializes the channels for tdvm module to prepare for measurement"""
    tdvm.initialize(analog_input_channel_expression=input_terminal)

    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(svg)
    logger.attach(tdvm)
    # returns the initialized objects
    return svg, tdvm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Generate/Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(  
    svg: daq.SignalVoltageGeneration,
    tdvm: daq.TimeDomainMeasurement,
    digital_trigger_source=DIGITAL_TRIGGER_SOURCE,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # Set the maximum and minimum range for tdvm measurement
    global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )
    # Set the Sampling rate and the Number of Samples per Channel as required
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    specific_channels_parameters = []

    # Specify the Measurement Execution Type
    meas_config_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Digital Trigger Type, Digital Trigger Source and Digital Trigger Edge
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=digital_trigger_source,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    tdvm_config = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_config_configure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion tdvm configure only
    tdvm.configure_and_measure(configuration=tdvm_config)

    # region configure SVG

    # Set the Signal Voltage generation range
    voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
        range_min_volts=-10, range_max_volts=10
    )
    # Set the Sampling rate hertz and the generated siganl duration
    gen_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=0.1,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # Set the PWM signal parameters
    waveform_parameters = daq.SignalVoltageGenerationSquareWaveParameters(
        generated_signal_amplitude_volts=0.5,
        generated_signal_duty_cycle_percent=80.00,
        generated_signal_frequency_hertz=100,
        generated_signal_phase_radians=0,
        generated_signal_offset_volts=0.5,
    )

    svg_config = daq.SignalVoltageGenerationSquareWaveConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion
    svg.configure_and_generate_square_waveform(svg_config)

    # region tdvm measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    tdvm_config = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion tdvm configure and measure
    #################################################################################################### 
    # end region configure and measure
    tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

    print("TDVM result :\n")
    print(tdvm_result_data)
    # record results
    results_map["TDVM data"] = tdvm_result_data

    # return results
    return results_map


# region close


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    svg: daq.SignalVoltageGeneration,
    tdvm: daq.TimeDomainMeasurement,
):
    svg.close()
    tdvm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def analog_pwm_test(
    generation_output_channel=OUTPUT_TERMINAL,
    measurement_input_channel=INPUT_TERMINAL,
    trigger_source=DIGITAL_TRIGGER_SOURCE,
):
    """Executes all steps in the sequence"""  

    # Runs the Setup Function
    svg, tdvm = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Runs the Main Function
    main(svg, tdvm, digital_trigger_source=trigger_source)
    # Runs the cleanup Function
    cleanup(svg, tdvm)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/analog_voltage_measurement_test.py sha256=6ce4186d5d1520a6859183c5ad1748aacf1174e9ac46a95a2cdc8cb7798f0b82 bytes=4866 -->
## FILE: src/nipcbatt/pcbatt_automation/LED_Tests/analog_voltage_measurement_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/LED_Tests/analog_voltage_measurement_test.py`
- sha256: `6ce4186d5d1520a6859183c5ad1748aacf1174e9ac46a95a2cdc8cb7798f0b82`
- bytes: 4866

````python
"""Demonstrates DC RMS Voltage Measurement using AI lines""" 

import os
import sys
from enum import Enum  

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# To use save_traces and plotter from utils folder
# from pcbatt_logger import PcbattLogger
parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""
# Default Channel
INPUT_TERMINAL = "Sim_PC_basedDAQ/ai1"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\DRVM_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH):
    """Creates the necessary objects for measurement of Voltage""" 

    # Creates the instance of measurement class required for the test
    drvm = daq.DcRmsVoltageMeasurement()
    """Initializes the channels for drvm module to prepare for measurement"""
    drvm.initialize(analog_input_channel_expression=input_terminal)

    # Sets the logger function
    logger = PcbattLogger(file_path)
    logger.attach(drvm)

    # returns the initialized objects
    return drvm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main(  
    drvm: daq.DcRmsVoltageMeasurement,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # Set the minimum and maximum voltage range
    global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
        range_min_volts=-10,
        range_max_volts=10,
    )

    specific_channels_parameters = []

    # Set the Measurement Execution Type
    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # Set the Sampling rate and the Number of Samples per Channel
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    drvm_config = daq.DcRmsVoltageMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion drvm configure and measure
    ####################################################################################################  
    # end region configure and measure

    drvm_result_data = drvm.configure_and_measure(drvm_config)
    print("DRVM result :\n")
    print(drvm_result_data)
    # region close
    # record results
    results_map["DRVM data"] = drvm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    drvm: daq.DcRmsVoltageMeasurement,
):
    drvm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def analog_voltage_measurement(
    generation_input_channel=INPUT_TERMINAL,
):
    # Runs setup function
    drvm = setup(input_terminal=generation_input_channel)
    # Runs the main function
    main(drvm)
    # Runs the cleanup function
    cleanup(drvm)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/led_test_main_sequence.py sha256=ad6ba11138852ec4f3401de49c0052e924dace5b39011aeee18fd1aa12f59c18 bytes=1084 -->
## FILE: src/nipcbatt/pcbatt_automation/LED_Tests/led_test_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/LED_Tests/led_test_main_sequence.py`
- sha256: `ad6ba11138852ec4f3401de49c0052e924dace5b39011aeee18fd1aa12f59c18`
- bytes: 1084

````python
"""Main sequence for Analog PWM test"""  

# Import Functions
from analog_pwm_test import analog_pwm_test
from analog_voltage_measurement_test import analog_voltage_measurement
from turn_off_all_ao_channels import power_down_all_ao_channels

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################
"""Example 1 - Demonstrates DC RMS Voltage Measurement using the Analog Input 
   Channels or Modules"""
analog_voltage_measurement()

"""Example 2 - Demonstrates the Analog PWM Signal Voltage Generation and 
   Time Domain Voltage Measurement"""
analog_pwm_test()

######## CLEAN UP ####################
"""Turns off all configured AO channels by setting the output voltage to 0"""
power_down_all_ao_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/turn_off_all_ao_channels.py sha256=e6bf902867f4e7bf18b58c568de49210e40e67ccf461fbfcad1d0348e7b4cb43 bytes=1315 -->
## FILE: src/nipcbatt/pcbatt_automation/LED_Tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/LED_Tests/turn_off_all_ao_channels.py`
- sha256: `e6bf902867f4e7bf18b58c568de49210e40e67ccf461fbfcad1d0348e7b4cb43`
- bytes: 1315

````python
"""This example resets all configured Analog output channels to 0 volts"""  

from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/__init__.py sha256=4b4e5f6d355a4087eea86ec040b78b5eabb0ead59c7867b110ff1a7641a26fec bytes=60 -->
## FILE: src/nipcbatt/pcbatt_automation/microphone_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/microphone_tests/__init__.py`
- sha256: `4b4e5f6d355a4087eea86ec040b78b5eabb0ead59c7867b110ff1a7641a26fec`
- bytes: 60

````python
"""Includes files for running Microphone Test sequence""" 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/microphone_main_sequence.py sha256=b783e4c900f4e407876dc6f06e8ab1da400571c0b4a22ce7767b21c30c43fcae bytes=982 -->
## FILE: src/nipcbatt/pcbatt_automation/microphone_tests/microphone_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/microphone_tests/microphone_main_sequence.py`
- sha256: `b783e4c900f4e407876dc6f06e8ab1da400571c0b4a22ce7767b21c30c43fcae`
- bytes: 982

````python
"""Main Sequence for executing Microphone Test""" 


# import functions
from microphone_test import signal_voltage_generation_and_measurement
from turn_off_all_ao_channels import power_down_all_ao_channels

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################
"""Example demonstrates Frequency domain measurements of captured Analog(Audio) signal 
generated by Analog Output(generates sine wave tones) module with Hardware Trigger"""

signal_voltage_generation_and_measurement()

######## CLEAN UP ####################

# Turn off all configured AO channels by configuring to 0V
power_down_all_ao_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/microphone_test.py sha256=8e91652529729007531e7257c92d638fae610d74ea947741c579b1d7a1a3599a bytes=9300 -->
## FILE: src/nipcbatt/pcbatt_automation/microphone_tests/microphone_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/microphone_tests/microphone_test.py`
- sha256: `8e91652529729007531e7257c92d638fae610d74ea947741c579b1d7a1a3599a`
- bytes: 9300

````python
"""This example demonstrates Sine Wave Generation and Frequency Domain 
   Measurement using AO and AI channels or Modules"""  


import os 

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
SIGNAL_VOLTAGE_GEN_CHANNEL = "TS_Speaker0"  # physical channel = Sim_PC_basedDAQ/ao0
FREQ_DOMAIN_MEAS_CHANNEL = "TP_MIC0:2"  # physical channel = Sim_PC_basedDAQ/ai0:1
DIGITAL_STATRT_TRIGGER = "/Sim_PC_basedDAQ/ao/StartTrigger"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Signal_Generation_and_Frequency_Domain_Analysis.txt"

generation_time = 0.1


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(
    svg_channel=SIGNAL_VOLTAGE_GEN_CHANNEL,
    fdvm_channel=FREQ_DOMAIN_MEAS_CHANNEL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates the necessary objects for generation of sine wave and Frequency
    Domain Measurement""" 

    # Create the instances of generation and measurement classes required for the test.
    microphone_instance = daq.SignalVoltageGeneration()
    freq_domain_meas_test_point = daq.FrequencyDomainMeasurement()

    # Initialize Microphone
    """Initializes the configured channels of AO module to perform microphone functionality"""
    microphone_instance.initialize(channel_expression=svg_channel)

    # Initialize TP
    """Initializes the configured channels of AI module to perform DC-RMS voltage measurement"""
    freq_domain_meas_test_point.initialize(analog_input_channel_expression=fdvm_channel)

    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(microphone_instance)
    logger.attach(freq_domain_meas_test_point)
    # returns the initialized objects
    return microphone_instance, freq_domain_meas_test_point


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main( 
    microphone_instance: daq.SignalVoltageGeneration,
    freq_domain_meas_test_point: daq.FrequencyDomainMeasurement,
    digital_start_trigger=DIGITAL_STATRT_TRIGGER,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Configure Freq Domain Measurement settings to wait for Hardware Trigger"""
    # Set the maximum and minimum range for FDVM measurement
    global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )
    # Set the sampling rate and number of samples per channel as required
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    specific_channels_parameters = []
    # Specify the Measurement Execution Type
    meas_config_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Digital Trigger Type, Digital Trigger Source and Digital Trigger Edge
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=digital_start_trigger,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    fdvm_config = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_config_configure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )
    # endregion fdvm configure only
    freq_domain_meas_test_point.configure_and_measure(configuration=fdvm_config)

    # Region Configure Signal Voltage Generation

    """Generates Sine wave and Trigger to Initiate measurement"""

    # region configure SVG

    # Set the Siganl Voltage Generation Range
    voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
        range_min_volts=-2, range_max_volts=2
    )
    # Set the Sampling rate hertz and the generated siganl duration
    gen_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=generation_time,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # Set the Sine wave Parameters
    generated_signal_tone_parameters = daq.ToneParameters(
        tone_frequency_hertz=1000, tone_amplitude_volts=1, tone_phase_radians=0
    )

    waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0,
        generated_signal_tone_parameters=generated_signal_tone_parameters,
    )

    svg_config = daq.SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion
    microphone_instance.configure_and_generate_sine_waveform(svg_config)

    """Measures the Analog Input voltage waveforms (Started measure when Signal Voltage generation sends Trigger after source) and returns Freq Domain Analysis""" 
    # Region FDVM Measure Only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    fdvm_config = daq.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion fdvm configure and measure
    ####################################################################################################  
    # end region configure and measure
    fdvm_result_data = freq_domain_meas_test_point.configure_and_measure(configuration=fdvm_config)

    print(fdvm_result_data)
    # region close

    # record results
    results_map["FDVM data"] = fdvm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    microphone_instance: daq.SignalVoltageGeneration,
    freq_domain_meas_test_point: daq.TimeDomainMeasurement,
):
    microphone_instance.close()
    freq_domain_meas_test_point.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def signal_voltage_generation_and_measurement(
    generation_channel=SIGNAL_VOLTAGE_GEN_CHANNEL,
    measurement_channel=FREQ_DOMAIN_MEAS_CHANNEL,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    microphone_instance, freq_domain_meas_test_point = setup(
        generation_channel, measurement_channel
    )

    # Run main function
    main(
        microphone_instance,
        freq_domain_meas_test_point,
        digital_start_trigger=DIGITAL_STATRT_TRIGGER,
    )

    # Run cleanup function
    cleanup(microphone_instance, freq_domain_meas_test_point)


####################################################################################################
# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/turn_off_all_ao_channels.py sha256=e6bf902867f4e7bf18b58c568de49210e40e67ccf461fbfcad1d0348e7b4cb43 bytes=1315 -->
## FILE: src/nipcbatt/pcbatt_automation/microphone_tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/microphone_tests/turn_off_all_ao_channels.py`
- sha256: `e6bf902867f4e7bf18b58c568de49210e40e67ccf461fbfcad1d0348e7b4cb43`
- bytes: 1315

````python
"""This example resets all configured Analog output channels to 0 volts"""  

from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/__init__.py sha256=7f73ac819e8043386f19ea0b999a78177129622d54ae43fc08d479576405a7c4 bytes=63 -->
## FILE: src/nipcbatt/pcbatt_automation/power_supply_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/power_supply_tests/__init__.py`
- sha256: `7f73ac819e8043386f19ea0b999a78177129622d54ae43fc08d479576405a7c4`
- bytes: 63

````python
"""Includes files for running power supply test sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_down_all_power_channels.py sha256=c3ae2c32a0a755a2cadc6fda1a1c68770e0a34a7f6332bfbdc76bb676fd5a28c bytes=1027 -->
## FILE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_down_all_power_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/power_supply_tests/power_down_all_power_channels.py`
- sha256: `c3ae2c32a0a755a2cadc6fda1a1c68770e0a34a7f6332bfbdc76bb676fd5a28c`
- bytes: 1027

````python
"""This example resets and closes configured Power channels"""  

from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
POWER_CHANNEL = "Simulated_power/power"

# Default configuration for Power channel
CONFIGURATION = daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION


def power_down_all_power_channels(
    channel_name=POWER_CHANNEL,
    config: daq.PowerSupplySourceAndMeasureConfiguration = CONFIGURATION,
):
    """Configure power channel with default parameters and close""" 

    # Initialize Power Channels
    generation = daq.PowerSupplySourceAndMeasure()
    generation.initialize(power_channel_name=channel_name)

    # Use the configure_and_measure method for power channel with default configuration
    generation.configure_and_measure(configuration=config)

    # Close the 'PowerSupplySourceAndMeasure' Task for power channel
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_main_sequence.py sha256=64d8387bb8cd8d5d97d52bd9c32cb573503eb24089d8de8f61e387ed6b51ad31 bytes=1230 -->
## FILE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_main_sequence.py`
- sha256: `64d8387bb8cd8d5d97d52bd9c32cb573503eb24089d8de8f61e387ed6b51ad31`
- bytes: 1230

````python
"""Main Sequence for executing Power Supply Tests"""  

# import functions
from nipcbatt.pcbatt_automation.power_supply_tests.power_down_all_power_channels import (
    power_down_all_power_channels,
)
from nipcbatt.pcbatt_automation.power_supply_tests.power_supply_test_with_trigger import (
    power_supply_test_with_trigger,
)
from nipcbatt.pcbatt_automation.power_supply_tests.power_supply_test_without_trigger import (
    power_supply_test_without_trigger,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

"""Synchronization using analog libraries"""

power_supply_test_with_trigger()

"""Synchronziation using digital libraries"""

power_supply_test_without_trigger()

"""Synchronization using digital counter libraries"""

######## CLEAN UP ####################

# Power down all Power Supplies
power_down_all_power_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_with_trigger.py sha256=93c30159a28bd0911b7210f54df4fd1d07e2e2691652a564b5d6ea885997ab93 bytes=10636 -->
## FILE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_with_trigger.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_with_trigger.py`
- sha256: `93c30159a28bd0911b7210f54df4fd1d07e2e2691652a564b5d6ea885997ab93`
- bytes: 10636

````python
"""This example demostrates Power Supply Source(VDD) and Time Domain Analysis of 
Measured Analog input voltage in TestPoints. Data capture in Analog Input(TP) starts when 
the Trigger is sent from Power Supply after starting the source."""  

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
POWER_CHANNEL = "Simulated_power/power"
ANALOG_INPUT_CHANNEL = "TP_Power0:2"  # physical channel = Simulated_AI/ai0:2

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\power_supply_test_with_trigger_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    power_channel=POWER_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
):
    """Creates the necessary objects for the generation and measurement of the power supply"""  

    # Create the instances of generation and measurement classes required for the test.
    power_supply_test_source_instance = daq.PowerSupplySourceAndMeasure()
    analog_input_test_point_instance = daq.TimeDomainMeasurement()

    # Initialize Power Supply
    """Initializes the configured channels of Power supply module"""
    power_supply_test_source_instance.initialize(power_channel_name=power_channel)

    # Initialize Test Point
    """Initializes the configured channels of AI module to perform Time domain measuerement"""
    analog_input_test_point_instance.initialize(analog_input_channel_expression=measurement_channel)

    return power_supply_test_source_instance, analog_input_test_point_instance


####################################################################################################
# endregion initialize


# region configure_and_measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: daq.TimeDomainMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Note to run with Hardware: Review the configurations and update the trigger configurations"""  

    """ If write_to_file is True, the Logger is used to output the results to a file.
        The Logger can be used to store configurations and outputs in a .txt or .csv file.
        The default file path is C:\\Windows\\Temp\\power_supply_test_with_trigger_results.txt"""
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(power_supply_test_source_instance)
        logger.attach(analog_input_test_point_instance)

    #### Create two different configurations for measurement using 'TimeDomainMeasurementConfiguration'  

    #### Initially measurement_options is set to CONFIGURE_ONLY
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'VoltageRangeAndTerminalParameters'
    meas_global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    # initialize an instance of 'List[VoltageMeasurementChannelAndTerminalRangeParameters]'
    meas_specific_channels_parameters = []

    # initialize an instance of 'SampleClockTimingParameters'
    meas_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.TE1,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source="/Sim_TS/te0/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration' for Configure only
    meas_config_configure_only = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_configure_only,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure and wait for trigger
    meas_result_data_after_configuring = analog_input_test_point_instance.configure_and_measure(
        configuration=meas_config_configure_only
    )

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["tdvm_configure_only"] = meas_result_data_after_configuring

    ### Configure and measure test source using 'PowerSupplySourceAndMeasureConfiguration'

    # initialize an instance of 'PowerSupplySourceAndMeasureTerminalParameters'
    gen_terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=5,
        current_setpoint_amperes=1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
        enable_output=True,
    )

    # initialize an instance of 'MeasurementOptions'
    meas_options_configure_and_measure = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'SampleClockTimingParameters'
    gen_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    gen_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'PowerSupplySourceAndMeasureConfiguration'
    meas_config_configure_and_measure = daq.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=gen_terminal_parameters,
        measurement_options=meas_options_configure_and_measure,
        sample_clock_timing_parameters=gen_sample_clock_timing_parameters,
        digital_start_trigger_parameters=gen_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure
    gen_result_data_after_configure_and_measure = (
        power_supply_test_source_instance.configure_and_measure(
            configuration=meas_config_configure_and_measure
        )
    )

    # record intermediate result
    results_map["pssm_configure_and_measure"] = gen_result_data_after_configure_and_measure

    #### Second configuration will skip configuring and go straight to measurement

    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration' for Measure only
    meas_config_measure_only = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use Measure only configuration
    meas_result_data_after_measuring = analog_input_test_point_instance.configure_and_measure(
        configuration=meas_config_measure_only
    )

    # record results
    results_map["tdvm_measure_only"] = meas_result_data_after_measuring

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: daq.TimeDomainMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    power_supply_test_source_instance.close()  # Close TS
    analog_input_test_point_instance.close()  # Close TP


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def power_supply_test_with_trigger(
    power_channel=POWER_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence""" 
    
    # Run setup function
    gen, meas = setup(power_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


####################################################################################################
# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_without_trigger.py sha256=84cd706cf37c8cc816c2be05e8a161aced1f07f015b5412be5864575081abdeb bytes=9240 -->
## FILE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_without_trigger.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_without_trigger.py`
- sha256: `84cd706cf37c8cc816c2be05e8a161aced1f07f015b5412be5864575081abdeb`
- bytes: 9240

````python
"""This example demonstrates Power Supply source and Voltage Measurement without trigger"""  

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
POWER_CHANNEL = "Simulated_power/power"
ANALOG_INPUT_CHANNEL = "TP_Power0:2"  # physical channel = Simulated_AI/ai0:2

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\power_supply_test_without_trigger_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    power_channel=POWER_CHANNEL,
    voltage_channel=ANALOG_INPUT_CHANNEL,
):
    """Creates the necessary objects for the generation and measurement of the power supply"""  

    # Create the instances of generation and measurement classes required for the test.
    power_supply_test_source_instance = daq.PowerSupplySourceAndMeasure()
    analog_input_test_point_instance = daq.DcRmsVoltageMeasurement()

    # Initialize Power Supply
    """Initializes the configured channels of Power supply module"""
    power_supply_test_source_instance.initialize(power_channel_name=power_channel)

    # Initialize Test Point
    """Initializes the configured channels of AI module to perform Voltage measuerement"""
    analog_input_test_point_instance.initialize(analog_input_channel_expression=voltage_channel)

    return power_supply_test_source_instance, analog_input_test_point_instance


####################################################################################################
# endregion initialize


# region configure_and_measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: daq.DcRmsVoltageMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Note to run with Hardware: Review the configurations and update the trigger configurations"""  

    """ If write_to_file is True, the Logger is used to output the results to a file.
        The Logger can be used to store configurations and outputs in a .txt or .csv file.
        The default file path is C:\\Windows\\Temp\\power_supply_test_with_trigger_results.txt"""
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(power_supply_test_source_instance)
        logger.attach(analog_input_test_point_instance)

    ### Configure and measure VDD using 'PowerSupplySourceAndMeasureConfiguration'

    # initialize an instance of 'PowerSupplySourceAndMeasureTerminalParameters'
    gen_terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=5,
        current_setpoint_amperes=1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
        enable_output=True,
    )

    # initialize an instance of 'MeasurementOptions'
    gen_measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'SampleClockTimingParameters'
    gen_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    gen_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'PowerSupplySourceAndMeasureConfiguration'
    gen_result_data_after_configure_and_measure = daq.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=gen_terminal_parameters,
        measurement_options=gen_measurement_options,
        sample_clock_timing_parameters=gen_sample_clock_timing_parameters,
        digital_start_trigger_parameters=gen_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure
    gen_result_data_after_configure_and_measure = (
        power_supply_test_source_instance.configure_and_measure(
            configuration=gen_result_data_after_configure_and_measure
        )
    )

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["pssm_configure_and_measure"] = gen_result_data_after_configure_and_measure

    #### Configure and measure an instance of 'DcRmsVoltageMeasurementConfiguration'

    # initialize an an instance of 'MeasurementOptions'
    meas_measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # intialize an instance of 'VoltageRangeAndTerminalParameters'
    meas_global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    # initialize an instance of 'List[VoltageMeasurementChannelAndTerminalRangeParameters]'
    meas_specific_channels_parameters = []

    # initialize an instance of 'SampleClockTimingParameters'
    meas_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'DcRmsVoltageMeasurementConfiguration'
    meas_measurement_config = daq.DcRmsVoltageMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_measurement_options,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure
    meas_result_data_after_configuring = analog_input_test_point_instance.configure_and_measure(
        configuration=meas_measurement_config
    )

    # record intermediate result
    results_map["drvm_configure_and_measure"] = meas_result_data_after_configuring

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: daq.DcRmsVoltageMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    power_supply_test_source_instance.close()  # Close TS
    analog_input_test_point_instance.close()  # Close TP


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def power_supply_test_without_trigger(
    power_channel=POWER_CHANNEL,
    voltage_channel=ANALOG_INPUT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  
    
    # Run setup function
    gen, meas = setup(power_channel, voltage_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


####################################################################################################
# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/__init__.py sha256=3ded2c20038707114e26f27c4c1911d8b0a11fa9b1cdbe013afae9b1e9d399e7 bytes=55 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/__init__.py`
- sha256: `3ded2c20038707114e26f27c4c1911d8b0a11fa9b1cdbe013afae9b1e9d399e7`
- bytes: 55

````python
"""Includes files for running Sensor Test sequence"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/rtd_test.py sha256=690fbf445d6681990a4a98cdc1904c0bc388137e0afbb64b62030211ffb4482d bytes=5647 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/rtd_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/rtd_test.py`
- sha256: `690fbf445d6681990a4a98cdc1904c0bc388137e0afbb64b62030211ffb4482d`
- bytes: 5647

````python
"""Demonstrates temprature measurement using RTD using AI lines or Modules"""  

import os  
import sys  

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# ignore:
"""To use the specific channel change the use_specific_channel to True"""
# Global variable
use_specific_channel = False

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""

# Default channels
INPUT_TERMINAL = "TP_RTD"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\RTD_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH):
    """Creates the necessary objects for the measurement of Temprature"""  

    # Creates the instances of measurement class required for the test
    trtdm = daq.TemperatureMeasurementUsingRtd()

    # Initialize measurement object
    """Initializes the channels of the trtdm module to prepare for measurement"""
    trtdm.initialize(input_terminal)
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(trtdm)
    # returns initializated objects
    return trtdm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main( 
    trtdm: daq.TemperatureMeasurementUsingRtd, input_terminal=INPUT_TERMINAL
):
    results_map = {}  # this structure will hold results in key-value pairs

    # region TRTDM configure and measure
    global_channel_parameters = daq.TemperatureRtdMeasurementTerminalParameters(
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        current_excitation_value_amperes=0.001,
        sensor_resistance_ohms=100,
        rtd_type=nidaqmx.constants.RTDType.PT_3750,
        excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
        resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
        adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
    )

    # region specific_channels_parameters
    channel0 = daq.TemperatureRtdMeasurementChannelParameters(
        channel_name=input_terminal,
        sensor_resistance_ohms=100,
        current_excitation_value_amperes=0.001,
        rtd_type=nidaqmx.constants.RTDType.PT_3750,
        resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
        excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
    )

    # endregion specific_channels_parameters

    specific_channels_parameters = []
    if use_specific_channel:
        specific_channels_parameters.append(channel0)

    # Configure the sampling rate and the number of sample per channel according to requirement
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100,
        number_of_samples_per_channel=10,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    trtdm_config = daq.TemperatureRtdMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion TRTDM configure and measure
    ####################################################################################################  

    trtdm_result_data = trtdm.configure_and_measure(configuration=trtdm_config)
    print("TRTDM result :\n")
    print(trtdm_result_data)
    # region close

    # record results
    results_map["RTD data"] = trtdm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    trtdm: daq.TemperatureMeasurementUsingRtd,
):
    trtdm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def rtd_test(
    measurement_input_channel=INPUT_TERMINAL,
):
    """Execute all steps in the sequence"""  
    
    # Run setup function
    trtdm = setup(
        input_terminal=measurement_input_channel,
    )
    # Run main function
    main(trtdm, input_terminal=measurement_input_channel)
    # Run cleanup function
    cleanup(trtdm)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/sensor_tests_main_sequence.py sha256=9551c1b17ceb8fabc5e327ce11b8b18234f04add232cede8d23cbec994c56d58 bytes=1563 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/sensor_tests_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/sensor_tests_main_sequence.py`
- sha256: `9551c1b17ceb8fabc5e327ce11b8b18234f04add232cede8d23cbec994c56d58`
- bytes: 1563

````python
"""Main sequence forr executing the Sensor Test"""  

from rtd_test import rtd_test
from thermistor_test_cdaq import thermistor_test_cdaq
from thermistor_test_testscale import thermistor_test_testscale
from thermocouple_test import thermocouple_test
from turn_off_all_ao_channels import power_down_all_ao_channels
from turn_off_power_channels import close_power_supply

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################
"""Example 1 - Demonstrates the DC Voltgae generaion and Temperature measurement 
   with Thermistor using the Output and Input lines of cDAQ"""

thermistor_test_cdaq()

"""Example 2 - Demonstrates the DC Voltgae generaion and Temperature measurement 
   with Thermistor using the Power Module and Analog Input Module of TestScale """

thermistor_test_testscale()


"""Example 3 - Demonstrates Temprature measurement with RTD using AI lines or
   Module of cDAQ"""

rtd_test()

"""Example 4 - Demonstrates Temprature measurement with Thermocouple using AI 
   lines or Module of cDAQ"""
thermocouple_test()

######## CLEAN UP ####################
"""Turn of all the Power lines and AO channels """
power_down_all_ao_channels()
close_power_supply()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_cdaq.py sha256=544b5e6b65ddf0cebcdb785282e123072432f9f1e2305a11651508c5668eed93 bytes=7422 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_cdaq.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_cdaq.py`
- sha256: `544b5e6b65ddf0cebcdb785282e123072432f9f1e2305a11651508c5668eed93`
- bytes: 7422

````python
"""Demonstrates DC Voltage Generation using AO lines or Modules and Temprature
   measurement with Thermistor using AI lines or Modules of cDAQ"""  

import os
import sys

import nidaqmx
import numpy as np  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "TS_THEX"
# Physical Channel name is Simulated_cDAQ_9263_ao0

INPUT_TERMINAL = "TP_TH0"
# Physical channel name is Simulated_cDAQ_9211/ai0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermistor_test_cDAQ.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(
    output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH
):
    """Creates the necessary objects for DC voltage generation
    and the Temprature Measurement"""  

    # Create the instances of generation class required for the test
    drvg = daq.DcVoltageGeneration()

    """Initializes the channels for the drvg module to prepare 
       for DC voltage generation"""
    drvg.initialize(analog_output_channel_expression=output_terminal)
    # Creates the necessary instances of measurement class required for the test
    ttr = daq.TemperatureMeasurementUsingThermistor()

    # Initialize the measurement objective
    """Initializes the channels of ttr module to prepare for temprature
       measuremnt"""
    ttr.initialize(input_terminal)
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(drvg)
    logger.attach(ttr)

    # returns initialized objects
    return drvg, ttr


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(  
    drvg: daq.DcVoltageGeneration,
    ttr: daq.TemperatureMeasurementUsingThermistor,
    input_terminal=INPUT_TERMINAL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Set up the minimum and maximum range for the generation of voltage"""
    range_settings = daq.VoltageGenerationChannelParameters(
        range_min_volts=-10.0, range_max_volts=10.0
    )

    # Set the volatge that has to be generated
    output_voltages = [5.00]

    drvg_config = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
    )

    # endregion drvg configure and generate

    drvg.configure_and_generate(drvg_config)

    # region TTR configure and measure

    # Set the parameters for the Thermistor
    coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
        coefficient_steinhart_hart_a=1.29536e-3,
        coefficient_steinhart_hart_b=234.31590e-6,
        coefficient_steinhart_hart_c=101.87030e-9,
    )

    beta_coefficient_and_sensor_resistance_parameters = (
        daq.BetaCoefficientAndSensorResistanceParameters(
            coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
        )
    )

    global_channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        voltage_excitation_value_volts=5.0,
        thermistor_resistor_ohms=1000,
        steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
        coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
        beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
    )

    specific_channels_parameters = []

    # endregion specific_channels_parameters

    # Set the Sampling rate and the Number of Samples to read per channel as required
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    ttr_config = daq.TemperatureThermistorMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion TTR configure and measure
    #################################################################################################### 

    ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

    # Set DC Voltage to 0 to turn off the DC voltage generation
    output_voltages = [0.0]

    drvg_config1 = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
    )

    drvg.configure_and_generate(drvg_config1)

    print("TTR result :\n")
    print(ttr_result_data)
    # close region
    # record results
    results_map["Thermistor data"] = ttr_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup( 
    drvg: daq.DcVoltageGeneration,
    ttr: daq.TemperatureMeasurementUsingThermistor,
):
    drvg.close()
    ttr.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermistor_test_cdaq(
    generation_output_channel=OUTPUT_TERMINAL,
    measurement_input_channel=INPUT_TERMINAL,
):
    """Execute all the steps in sequence"""  
    
    # Run the setup function
    drvg, ttr = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Run the main function
    main(drvg, ttr, input_terminal=measurement_input_channel)
    # Run the cleanup function
    cleanup(drvg, ttr)


# endregion
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_testscale.py sha256=23992ae8f4c03f26b261a0f857d6dc286d201abdc02ec226083c7e52e18c53ac bytes=8067 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_testscale.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_testscale.py`
- sha256: `23992ae8f4c03f26b261a0f857d6dc286d201abdc02ec226083c7e52e18c53ac`
- bytes: 8067

````python
"""Demonstrates Voltage Generation using Power Module and Temprature 
   measurement with Thermistor using AI lines or Modules of Testscale"""  

import os
import sys

import nidaqmx
import numpy as np  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)


"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "Simulated_Power/power"

INPUT_TERMINAL = "TP_TH2"
# Physical channel name is "Simulated_TS1_AI/ai0"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermistor_test_TestScale.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(
    output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH
):
    """Creates the necessary objects for voltage generation
    and the Temprature Measurement"""  
    # Create the instances of generation class required for the test
    pssm = daq.PowerSupplySourceAndMeasure()

    """Initializes the channels for the pssm module to prepare 
       for voltage generation"""
    pssm.initialize(output_terminal)
    # Creates the necessary instances of measurement class required for the test
    ttr = daq.TemperatureMeasurementUsingThermistor()
    """Initializes the channels of ttr module to prepare for temprature
       measuremnt"""
    ttr.initialize(input_terminal)

    # Sets the logger Function
    logger = PcbattLogger(file_path)
    logger.attach(pssm)
    logger.attach(ttr)
    # returns initialized objects
    return pssm, ttr


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main( 
    pssm: daq.PowerSupplySourceAndMeasure,
    ttr: daq.TemperatureMeasurementUsingThermistor,
    input_terminal=INPUT_TERMINAL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Sets up the volatge and current to be generated and whether
    to enable the output or not"""
    terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=5.0,
        current_setpoint_amperes=0.1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
        enable_output=True,
    )

    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Sampling rate and the Number of Samples to per channel as required
    gen_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    pssm_config = daq.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=terminal_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion PSSM configure and measure

    pssm.configure_and_measure(configuration=pssm_config)

    # region TTR configure and measure

    # Set the parameters for Thermistor
    coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
        coefficient_steinhart_hart_a=0,
        coefficient_steinhart_hart_b=0,
        coefficient_steinhart_hart_c=0,
    )

    beta_coefficient_and_sensor_resistance_parameters = (
        daq.BetaCoefficientAndSensorResistanceParameters(
            coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
        )
    )

    global_channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        voltage_excitation_value_volts=5,
        thermistor_resistor_ohms=1000,
        steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
        coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
        beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
    )

    # region specific_channels_parameters
    specific_channels_parameters = []

    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    ttr_config = daq.TemperatureThermistorMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion TTR configure and measure
    #################################################################################################### 

    ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

    print("TTR result :\n")
    print(ttr_result_data)
    # close region
    # record results
    results_map["Thermistor data"] = ttr_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup( 
    ttr: daq.TemperatureMeasurementUsingThermistor, pssm: daq.PowerSupplySourceAndMeasure
):
    ttr.close()
    pssm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermistor_test_testscale(
    generation_output_channel=OUTPUT_TERMINAL, measurement_input_channel=INPUT_TERMINAL
):
    """Execute all the steps in sequence"""  
    # Runs the Setup function
    pssm, ttr = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Runs the main function
    main(pssm, ttr, input_terminal=measurement_input_channel)
    # Runs the cleanup function
    cleanup(ttr, pssm)


# endregion
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermocouple_test.py sha256=f9007321101f5052bb3662ff5d9b929d9ee3b8a80435f44258b38f9b3422a35e bytes=6132 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/thermocouple_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/thermocouple_test.py`
- sha256: `f9007321101f5052bb3662ff5d9b929d9ee3b8a80435f44258b38f9b3422a35e`
- bytes: 6132

````python
"""Demonstrates temprature measurement using Thermocouple using AI lines or Modules"""  

import os
import sys

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# To use save_traces and plotter from utils folder
parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""
# Default channels
INPUT_TERMINAL = "TP_TC"
COLD_JUNCTION_CHANNEL = "Simulated_cDAQ_9217/ai0"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermocouple_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ###################################################
def setup(
    input_terminal=INPUT_TERMINAL,
    cold_junction_terminal=COLD_JUNCTION_CHANNEL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates the necessary objects for the measurement of Temprature"""  

    # Creates the instance of measurement class required for the test
    ttcm = daq.TemperatureMeasurementUsingThermocouple()

    """Initializes the channels of the ttcm module to prepare for measurement"""
    ttcm.initialize(
        channel_expression=input_terminal,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
        cold_junction_compensation_channel=cold_junction_terminal,
    )
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(ttcm)
    # returns initializated objects
    return ttcm


############################################################################################################################
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main(  
    ttcm: daq.TemperatureMeasurementUsingThermocouple,
    input_terminal=INPUT_TERMINAL,
    cold_junction_terminal=COLD_JUNCTION_CHANNEL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # region ttcm configure and measure
    global_channel_parameters = daq.TemperatureThermocoupleMeasurementTerminalParameters(
        temperature_minimum_value_celsius_degrees=0.0,
        temperature_maximum_value_celsius_degrees=100.0,
        thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
        cold_junction_compensation_temperature=25.0,
        perform_auto_zero_mode=False,
        auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
    )

    # region specific_channels_parameters

    channel_parameters = daq.TemperatureThermocoupleRangeAndTerminalParameters(
        temperature_minimum_value_celsius_degrees=0.0,
        temperature_maximum_value_celsius_degrees=100.0,
        thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
        cold_junction_compensation_temperature=25.0,
        cold_junction_compensation_channel_name=cold_junction_terminal,
        perform_auto_zero_mode=False,
        auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
    )

    channel1 = daq.TemperatureThermocoupleChannelRangeAndTerminalParameters(  
        channel_name=input_terminal, channel_parameters=channel_parameters
    )

    # endregion specific_channels_parameters

    specific_channels_parameters = []
    # Configure the sampling rate and the number of sample per channel according to requirement
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    ttcm_config = daq.TemperatureThermocoupleMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion ttcm configure and measure
    #################################################################################################
    # end region configure and measure

    ttcm_result_data = ttcm.configure_and_measure(configuration=ttcm_config)
    print("ttcm result :\n")
    print(ttcm_result_data)
    # region close

    # record results
    results_map["TTCM data"] = ttcm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    ttcm: daq.TemperatureMeasurementUsingThermocouple,
):
    ttcm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermocouple_test(
    generation_input_channel=INPUT_TERMINAL,
    cold_input_channel=COLD_JUNCTION_CHANNEL,
):
    """Execute all steps in the sequence""" 
    
    # Runs setup function
    ttcm = setup(input_terminal=generation_input_channel, cold_junction_terminal=cold_input_channel)
    # Runs main function
    main(ttcm, input_terminal=generation_input_channel, cold_junction_terminal=cold_input_channel)
    # Runs cleanup function
    cleanup(ttcm)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_all_ao_channels.py sha256=a9bdaa5fa276f8ef02ec689c16d53f56ba789752448247a3aad77ee054411963 bytes=1370 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_all_ao_channels.py`
- sha256: `a9bdaa5fa276f8ef02ec689c16d53f56ba789752448247a3aad77ee054411963`
- bytes: 1370

````python
"""This example resets all configured Analog output channels to 0 volts"""  

import nipcbatt
from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Simulated_cDAQ_9263/ao0"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()


power_down_all_ao_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_power_channels.py sha256=ca6e04d5e49da48f74a32b17852ea261ed71301319e65de2249154fb3cbe7389 bytes=3928 -->
## FILE: src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_power_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_power_channels.py`
- sha256: `ca6e04d5e49da48f74a32b17852ea261ed71301319e65de2249154fb3cbe7389`
- bytes: 3928

````python
"""This example resets all the configured Power Channels to 0 volts and 0 amps"""  

import os
import sys

import nidaqmx
import nidaqmx.constants
import numpy as np  

import nipcbatt
from nipcbatt import daq

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with hardware: update virtual/physical channels info based
on NI MAX in the below Initialize Steps"""
# Default Channel
OUTPUT_TERMINAL = "Simulated_Power/power"


# Initialize Region
########################################   INITIALIZATION FUNCTION   #########################################################
def setup(output_terminal=OUTPUT_TERMINAL):
    """Creates the necessary objects for voltage generation""" 
    pssm = daq.PowerSupplySourceAndMeasure()
    # Create the instances of generation class reuired for the test
    pssm.initialize(output_terminal)
    # returns the initialized object
    return pssm


################################################################################################################################
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(pssm: daq.PowerSupplySourceAndMeasure):
    """Sets up the volatge and current to be generated."""  
    terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=0.1,
        current_setpoint_amperes=0.1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
        enable_output=True,
    )

    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    gen_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    pssm_config = daq.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=terminal_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion PSSM configure and measure
    ###################################################################################################

    pssm.configure_and_measure(configuration=pssm_config)


# pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)
# close region


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    pssm: daq.PowerSupplySourceAndMeasure,
):
    pssm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def close_power_supply(generation_output_channel=OUTPUT_TERMINAL):
    """Executes all steps in Sequence"""  
    
    # Runs the Setup Function
    pssm = setup(output_terminal=generation_output_channel)

    # Runs the main function
    main(pssm)

    # Runs the cleanup function
    cleanup(pssm)


# endregion
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/__init__.py sha256=0e2cf9359528b1e77d07fc4f382bff172d09aa19045d2e090fb2dfe67bc71109 bytes=84 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/__init__.py`
- sha256: `0e2cf9359528b1e77d07fc4f382bff172d09aa19045d2e090fb2dfe67bc71109`
- bytes: 84

````python
"""Contains files used for automation testing of pcbatt synchronization classes"""  
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/digital_clock_generation_and_pwm_measurement.py sha256=b45d04fb0755e2a13d1cca953aa4bdea1f68d3d76a40c9f21d28f35e5f259fcc bytes=7288 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/digital_clock_generation_and_pwm_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/digital_clock_generation_and_pwm_measurement.py`
- sha256: `b45d04fb0755e2a13d1cca953aa4bdea1f68d3d76a40c9f21d28f35e5f259fcc`
- bytes: 7288

````python
"""This example demonstrates generation of Digital Clock signal using Digital Clock Generation 
   Library and measurement of the same signal using Digital PWM Measurement Library"""  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Physical Channel (Counter) and its Terminals  
   based on NI MAX in the below initialize step"""

# Default channels
PHYSICAL_CHANNEL_OUT = "/Sim_PC_basedDAQ/ctr0"
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI0"

PHYSICAL_CHANNEL_IN = "/Sim_PC_basedDAQ1/ctr0"
INPUT_TERMINAL = "/Sim_PC_basedDAQ1/PFI0"
GLOBAL_CHANNEL_COUNTER = ""

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_clock_generation_and_pwm_measurement_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=PHYSICAL_CHANNEL_OUT,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=PHYSICAL_CHANNEL_IN,
):
    """Creates the necessary objects for the generation and measurement of digital clock"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = daq.DigitalClockGeneration()
    measurement_instance = daq.DigitalPwmMeasurement()

    # Initialize generation object
    """Initializes the channels of the DCG module to prepare for generation"""
    generation_instance.initialize(
        counter_channel_expression=gen_counter_channel,
        output_terminal_name=output_terminal,
    )

    # Initialize measurement object
    """Initializes the channels of the DFM module to prepare for measurement"""
    measurement_instance.initialize(
        channel_expression=meas_counter_channel, input_terminal_name=input_terminal
    )

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.DigitalClockGeneration,
    measurement_instance: daq.DigitalPwmMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_clock_generation_and_pwm_measurement_results.txt
    """  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """1. Configure PWM Measurement settings to wait for Digital PWM Signal from Digital Clock Generation
    2. Generate PWM waveform from digital IO module
    3. Fetch and Validate Digital PWM Signal""" 

    # create configuration sub-objects
    meas_range_parameters = daq.DigitalPwmMeasurementRangeParameters(
        semi_period_minimum_value_seconds=25e-9,  # default minimum semiperiod (s)
        semi_period_maximum_value_seconds=53.68709,  # default maximum semiperiod (s)
    )

    meas_timing_parameters = daq.DigitalPwmMeasurementTimingParameters(
        semi_period_counter_wanted_cycles_count=100
    )

    meas_counter_parameters = daq.DigitalPwmMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        timing_parameters=meas_timing_parameters,
        semi_period_counter_starting_edge=daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE,
    )

    # create configuration object to configure only
    meas_cfg_config_only = daq.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters,
        measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    )

    # configure measurement instance
    measurement_instance.configure_and_measure(configuration=meas_cfg_config_only)

    # initialize instances of counter channel parameters and timing parameters for generation
    # then initialize an instance of 'DigitalClockGenerationConfiguration' with the settings
    gen_channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
        frequency_hertz=1000.0, duty_cycle_ratio=0.5
    )

    gen_timing_parameters = daq.DigitalClockGenerationTimingParameters(
        clock_duration_seconds=0.1
    )

    gen_configuration = daq.DigitalClockGenerationConfiguration(
        counter_channel_parameters=gen_channel_parameters, timing_parameters=gen_timing_parameters
    )

    # launch generation with configure_and_generate
    generation_instance.configure_and_generate(configuration=gen_configuration)

    # create separate measurement configuration to be used to measure only
    meas_cfg_measure_only = daq.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters,
        measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    )

    # configure_and_measure with measure only
    pwm_data = measurement_instance.configure_and_measure(configuration=meas_cfg_measure_only)

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record results
    results_map["PWM DATA"] = pwm_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# Close all tasks
def cleanup(
    generation_instance: daq.DigitalClockGeneration,
    measurement_instance: daq.DigitalPwmMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_clock_generation_and_pwm_measurement(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=PHYSICAL_CHANNEL_OUT,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=PHYSICAL_CHANNEL_IN,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        meas_counter_channel=measurement_counter_channel,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test 
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/dynamic_digital_pattern_generation_and_measurement.py sha256=e6ef2f6fed4458b44bfded03dc397d727f9c8a891f94e925eab17c4144f8a93f bytes=10545 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/dynamic_digital_pattern_generation_and_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/dynamic_digital_pattern_generation_and_measurement.py`
- sha256: `e6ef2f6fed4458b44bfded03dc397d727f9c8a891f94e925eab17c4144f8a93f`
- bytes: 10545

````python
"""This example demonstrates synchronization using Dynamic Digital Pattern Generation Library to 
   generate Digital Pattern from one Backplane and capture it using Dynamic Digital Pattern 
   Measuerment library in another Backplane"""  

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_library.common.helper_functions import (
    digital_ramp_pattern_generator,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Global Channel Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_Digital0,TS_Digital1"
MEASUREMENT_CHANNEL = "TP_Digital2,TP_Digital3"

# Default signal lines
SAMPLE_CLOCK_LINE = "/Sim_PC_basedDAQ/PFI0"  # Exporting Sample Clock to PFI0 Terminal
START_TRIGGER_LINE = "/Sim_PC_basedDAQ/PFI1"  # Exporting Start Trigger to PFI1 Terminal

# Default test results location
DEFAULT_FILEPATH = (
    "C:\\Windows\\Temp\\dynamic_digital_pattern_generation_and_measurement_results.txt"
)


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL):
    """Creates the necessary objects for the generation and measurement of digital patterns"""  

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = daq.DynamicDigitalPatternGeneration()
    measurement_instance = daq.DynamicDigitalPatternMeasurement()

    # Initialize generation object
    """Initializes the channel(s) of the DDPG module to prepare for generation"""
    generation_instance.initialize(channel_expression=generation_channel)

    # Initialize measurement object
    """Initializes the channel(s) of the DDPM module to prepare for measurement"""
    measurement_instance.initialize(channel_expression=measurement_channel)

    # Export signals to PFI lines
    sync_signals = daq.SynchronizationSignalRouting()
    sync_signals.route_sample_clock_signal_to_terminal(terminal_name=SAMPLE_CLOCK_LINE)
    sync_signals.route_start_trigger_signal_to_terminal(terminal_name=START_TRIGGER_LINE)

    # return initialized objects
    return generation_instance, measurement_instance, sync_signals


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DynamicDigitalPatternMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path for the results of this sequence is:
    C:\\Windows\\Temp\\dynamic_digital_pattern_generation_and_measurement_results.txt"""  

    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure test point"""

    # Note to run with Hardware: Review the Configurations & update the Sample Clock Source and
    # Digital Start Trigger Settings based on NI MAX and Setup Connections

    """Consider below items when measuring Digital patterns 
       1. Sampling rate at measurement end should be same as the sampling rate at generation end
       2. Configure Trigger to start capture as soon as pattern generated using Dynamic 
       digital pattern measurement"""

    # initialize an instance of 'MeasurementOptions' with options to configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    timing_parameters_configure_only = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,  # Provide exact sample clock rate set in Generation for the
        # shared clock. Note: external clock signals cannot be divided down to lesser rates
        number_of_samples_per_channel=1000,
        active_edge=nidaqmx.constants.Edge.FALLING,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    trigger_parameters_configure_only = nipcbatt.DigitalStartTriggerParameters(
        digital_start_trigger_source=START_TRIGGER_LINE,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for configure only
    pre_trigger_measurement_config = daq.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_configure_only,
        timing_parameters=timing_parameters_configure_only,
        trigger_parameters=trigger_parameters_configure_only,
    )

    # use the config object to execute configure_and_measure to configure only
    measurement_instance.configure_and_measure(configuration=pre_trigger_measurement_config)

    # Note to run with Hardware: Review & update "Number of Digital Line" initialized in
    # Generation Task in the below step

    # create ramp data to output on digital port
    data = digital_ramp_pattern_generator(number_of_digital_lines=2, number_of_samples=100)

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    # create a generation instance for DynamicDigitalPatternTimingParameters
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000.0,
        active_edge=nidaqmx.constants.Edge.RISING,
    )

    # create a generation instance for DigitalStartTriggerParameters
    gen_trigger_parameters = daq.DynamicDigitalStartTriggerParameters(
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # create an instance of DynamicDigitalPatternGenerationConfiguration
    generation_config = daq.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
        pulse_signal=digital_port_data,
    )

    # generate the configured digital pattern from the digital module
    generation_instance.configure_and_generate(configuration=generation_config)

    # Create second measurement configuration to configure only
    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    timing_parameters_measure_only = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
        active_edge=nidaqmx.constants.Edge.RISING,
    )

    # create an instance for DigitalStartTriggerParameters
    trigger_parameters_measure_only = daq.DynamicDigitalStartTriggerParameters(
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'MeasurementOptions' for measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for post-generation
    post_gen_measurement_config = daq.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_measure_only,
        timing_parameters=timing_parameters_measure_only,
        trigger_parameters=trigger_parameters_measure_only,
    )

    # read digital pattern stored in buffer using postgeneration configuration
    result_data = measurement_instance.configure_and_measure(post_gen_measurement_config)

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record results
    results_map["DIGITAL DATA"] = result_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.DynamicDigitalPatternGeneration,
    measurement_instance: daq.DynamicDigitalPatternMeasurement,
    sync_signals: daq.SynchronizationSignalRouting,
):
    """Closes out the created objects used in the generation and measurement."""
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement
    sync_signals.close()  # Close signal synchronization


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def dynamic_digital_pattern_generation_and_measurement(
    generation_channel=GENERATION_CHANNEL,
    measurement_channel=MEASUREMENT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence."""
    # Run setup function
    gen, meas, sync = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas, sync)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/signal_voltage_and_time_domain_measure.py sha256=07423d14bda376b5a4b55097ec452df42ae7d2b6188768bb0edfb765d9d1caab bytes=11307 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/signal_voltage_and_time_domain_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/signal_voltage_and_time_domain_measure.py`
- sha256: `07423d14bda376b5a4b55097ec452df42ae7d2b6188768bb0edfb765d9d1caab`
- bytes: 11307

````python
"""This example demonstrates synchronization using Signal Voltage Generation Library to generate 
   a Analog Sine waveform from one Backplane and capture it using Time Domain Measuerment 
   library in another Backplane"""  

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update the Global Channel Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
SIGNAL_CHANNEL = "TS_Analog0"
ANALOG_INPUT_CHANNEL = "TP_Analog1"

# Default signal lines
SAMPLE_CLOCK_LINE = "/Sim_PC_basedDAQ/PFI0"  # Exporting Sample Clock to PFI0 Terminal
START_TRIGGER_LINE = "/Sim_PC_basedDAQ/PFI1"  # Exporting Start Trigger to PFI1 Terminal

# Default test results location
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\signal_voltage_and_time_domain_measurement_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    signal_channel=SIGNAL_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
):
    """Creates the necessary objects for the generation and measurement of the signal"""  

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = daq.SignalVoltageGeneration()
    measurement_instance = daq.TimeDomainMeasurement()

    # Initialize Generation
    """Initializes the configured channels of signal voltage generation module"""
    generation_instance.initialize(channel_expression=signal_channel)

    # Initialize Test Point
    """Initializes the configured channels of AI module to perform Time domain measuerement"""
    measurement_instance.initialize(analog_input_channel_expression=measurement_channel)

    """Note to run with Hardware: Update the routing paths based on NI MAX and 
       Setup Connections in the below step"""

    # Export signals to PFI lines
    sync_signals = daq.SynchronizationSignalRouting()
    sync_signals.route_sample_clock_signal_to_terminal(terminal_name=SAMPLE_CLOCK_LINE)
    sync_signals.route_start_trigger_signal_to_terminal(terminal_name=START_TRIGGER_LINE)

    return generation_instance, measurement_instance, sync_signals


####################################################################################################
# endregion initialize


# region configure_and_measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: daq.SignalVoltageGeneration,
    measurement_instance: daq.TimeDomainMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Note to run with Hardware: Review the Configurations & update the Sample Clock Source
    and Digital Start Trigger Settings based on NI MAX and Setup Connections""" 

    # Configure Time Domain Measurement settings to wait for Hardware Trigger and Sample Clock
    # from Signal generation. Configure exact sample clock rate set in generation for the shared
    # clock. Note: external clock signals cannot be diveded down to lesser rates

    """Configure test point"""
    """ If write_to_file is True, the Logger is used to output the results to a file.
        The Logger can be used to store configurations and outputs in a .txt or .csv file.
        The default file path is C:\\Windows\\Temp\\signal_voltage_and_time_domain_measurement_results.txt"""  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    #### First configuration option will configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'VoltageRangeAndTerminalParameters'
    meas_global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    # initialize an instance of 'List[VoltageMeasurementChannelAndTerminalRangeParameters]'
    meas_specific_channels_parameters = []

    # initialize an instance of 'SampleClockTimingParameters'
    meas_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source=SAMPLE_CLOCK_LINE,
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=START_TRIGGER_LINE,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration'
    pre_trigger_measurement_config = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_configure_only,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use theconfig object to execute configure_and_measure and wait for generation
    test_point_result_data_after_configuring = measurement_instance.configure_and_measure(
        configuration=pre_trigger_measurement_config
    )

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["tdvm_configure_only"] = test_point_result_data_after_configuring

    ### MOVE TO SIGNAL GENERATION ###

    """Generate sine wave from analog module"""
    range_params = daq.VoltageGenerationChannelParameters(
        range_min_volts=-10.0, range_max_volts=10.0
    )

    tone_params = daq.ToneParameters(
        tone_frequency_hertz=100.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    waveform_params = daq.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0.0, generated_signal_tone_parameters=tone_params
    )

    timing_parms = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        generated_signal_duration_seconds=0.1,
    )

    trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="OnboardClock",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    sine_wave_configuration = daq.SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=range_params,
        waveform_parameters=waveform_params,
        timing_parameters=timing_parms,
        digital_start_trigger_parameters=trigger_params,
    )

    # Generate sine wave
    sine_wave_source_generation = generation_instance.configure_and_generate_sine_waveform(
        configuration=sine_wave_configuration
    )

    # record intermediate generation result
    results_map["sine_wave_generation"] = sine_wave_source_generation

    ### Prepare Second Measurement Configuration  ###

    """Note to run with Hardware: Update "Periodic Waveform" input to "True" to calculate 
       all Time Domain Measurements"""

    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'SampleClockTimingParameters'
    timing_parameters_measure_only = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    trigger_parameters_measure_only = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="OnboardClock",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration' for measure only
    measurement_config_measure_only = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=timing_parameters_measure_only,
        digital_start_trigger_parameters=trigger_parameters_measure_only,
    )

    # Fetch and Validate Sine waveform via analog buffer
    # execute using measure only configuration
    test_point_result_data_after_measurement = measurement_instance.configure_and_measure(
        configuration=measurement_config_measure_only
    )

    # record results
    results_map["post_gen_measurement"] = test_point_result_data_after_measurement

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: daq.SignalVoltageGeneration,
    measurement_instance: daq.TimeDomainMeasurement,
    sync_signals: daq.SynchronizationSignalRouting,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close TS
    measurement_instance.close()  # Close TP
    sync_signals.close()  # Close sync


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def signal_voltage_and_time_domain_measurement(
    generation_channel=SIGNAL_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  #
    
    # Run setup function
    gen, meas, sync = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas, sync)


# endregion test
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/synchronization_main_sequence.py sha256=cdf287c5c7749aec2fbd1fa15a44314d8a2d816e2e44b7f97c68fd88dc6eeef5 bytes=1887 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/synchronization_main_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/synchronization_main_sequence.py`
- sha256: `cdf287c5c7749aec2fbd1fa15a44314d8a2d816e2e44b7f97c68fd88dc6eeef5`
- bytes: 1887

````python
"""Main Sequence for executing Power Supply Tests"""  

# import functions
from nipcbatt.pcbatt_automation.synchronization_tests.digital_clock_generation_and_pwm_measurement import (
    digital_clock_generation_and_pwm_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.dynamic_digital_pattern_generation_and_measurement import (
    dynamic_digital_pattern_generation_and_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.signal_voltage_and_time_domain_measure import (
    signal_voltage_and_time_domain_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)
from nipcbatt.pcbatt_automation.synchronization_tests.turn_off_all_do_channels import (
    power_down_all_do_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""


############# MAIN ####################

"""Example demonstrates synchronization with two TestScale backplane 
   using Analog and Digital Libraries"""

# Synchronization using Analog Libraries

signal_voltage_and_time_domain_measurement()

# Synchronization using Digital Libraries

dynamic_digital_pattern_generation_and_measurement()

# Synchronization using Digital Counter Libraries

digital_clock_generation_and_pwm_measurement()


######## CLEAN UP ####################

# Turn off all configured AO channels by configuring to 0V

power_down_all_ao_channels()

# Turn off all configured DO channels by setting digital low state

power_down_all_do_channels()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_ao_channels.py sha256=4deb5627f41cd79b34272bda464c909c54048c7e7bb8f80065e086d66e798051 bytes=1353 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_ao_channels.py`
- sha256: `4deb5627f41cd79b34272bda464c909c54048c7e7bb8f80065e086d66e798051`
- bytes: 1353

````python
"""This example resets all configured Analog output channels to 0 volts"""  

import nipcbatt
from nipcbatt import daq

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0:3"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  
    
    # declare constant to hold output voltage of 0V
    off_voltages = [0.0, 0.0, 0.0, 0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = daq.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = daq.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_do_channels.py sha256=97068916fd2fb51aa39e09aba2217e5d3da272ea8a3be806e53ed0a8fcb3c442 bytes=1125 -->
## FILE: src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_do_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_do_channels.py`
- sha256: `97068916fd2fb51aa39e09aba2217e5d3da272ea8a3be806e53ed0a8fcb3c442`
- bytes: 1125

````python
"""This example resets all configured Digital output channels voltage to 0 Volts"""  

from nipcbatt import daq

# Note to run with Hardware: Update Virtual/Physical Channels Info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
DIGITAL_OUT_CHANNELS = "Sim_PC_basedDAQ/port0/line0:7"


def power_down_all_do_channels():
    """Set digital state to LOW on all digital output channels"""  
    
    # declare list to hold boolean false values
    low_values = [False, False, False, False, False, False, False, False]

    # Static Digital State Generation -- Initialize DO channels
    generation = daq.StaticDigitalStateGeneration()
    generation.initialize(channel_expression=DIGITAL_OUT_CHANNELS)

    # create configuration for output
    output_config = daq.StaticDigitalStateGenerationConfiguration(data_to_write=low_values)

    # set digital state LOW for all Digital Output channels
    generation.configure_and_generate(configuration=output_config)

    # closes the Static Digital State Generation Task for Digital output module
    generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/__init__.py sha256=c496be58150d54326509c3ac9b78070d34d916a131d3ff7fc0f777568a8d876d bytes=274 -->
## FILE: src/nipcbatt/pcbatt_communication_library/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/__init__.py`
- sha256: `c496be58150d54326509c3ac9b78070d34d916a131d3ff7fc0f777568a8d876d`
- bytes: 274

````python
"""Provides a set of protocol based communciation modules using python written functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/__init__.py sha256=9158af65c5e24203fb4417b2962d6fdbf330e9a86684e61f4da24b202614c50b bytes=256 -->
## FILE: src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/__init__.py`
- sha256: `9158af65c5e24203fb4417b2962d6fdbf330e9a86684e61f4da24b202614c50b`
- bytes: 256

````python
"""Provides private modules related to ni 845x communication protocols"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/_ni_845x_functions.py sha256=d6bd2f5a63a99c2e756ab161262d64dba9b4bc310e9839a27c89ba6e1897584e bytes=56878 -->
## FILE: src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/_ni_845x_functions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/_ni_845x_functions.py`
- sha256: `d6bd2f5a63a99c2e756ab161262d64dba9b4bc310e9839a27c89ba6e1897584e`
- bytes: 56878

````python
"""Private module that provides a set of ni-845x functions
used in pcbatt_communication library modules."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)

from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_int32,
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64,
    create_string_buffer,
)
from typing import Dict, List, Type, Union

import numpy
from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    DevicesFindResultData,
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.native_interop_utilities import (
    check_dll_availability,
    create_native_stdcall_win_function,
)
from nipcbatt.pcbatt_utilities.platform_utilities import (
    is_python_windows_32bits,
    is_python_windows_64bits,
)


class _Ni845xFunctionsNames:
    """Constants defining NI-845X functions names"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    NI_845X_OPEN = "ni845xOpen"
    NI_845X_CLOSE = "ni845xClose"
    NI_845X_DEVICE_LOCK = "ni845xDeviceLock"
    NI_845X_DEVICE_UNLOCK = "ni845xDeviceUnlock"
    NI_845X_SET_IO_VOLTAGE_LEVEL = "ni845xSetIoVoltageLevel"
    NI_845X_SET_TIMEOUT = "ni845xSetTimeout"
    NI_845X_FIND_DEVICE = "ni845xFindDevice"
    NI_845X_FIND_DEVICE_NEXT = "ni845xFindDeviceNext"
    NI_845X_CLOSE_FIND_DEVICE_HANDLE = "ni845xCloseFindDeviceHandle"
    NI_845X_I2C_CONFIGURATION_OPEN = "ni845xI2cConfigurationOpen"
    NI_845X_I2C_CONFIGURATION_CLOSE = "ni845xI2cConfigurationClose"
    NI_845X_SPI_CONFIGURATION_OPEN = "ni845xSpiConfigurationOpen"
    NI_845X_SPI_CONFIGURATION_CLOSE = "ni845xSpiConfigurationClose"
    NI_845X_I2C_READ = "ni845xI2cRead"
    NI_845X_I2C_WRITE = "ni845xI2cWrite"
    NI_845X_I2C_WRITE_READ = "ni845xI2cWriteRead"
    NI_845X_SPI_WRITE_READ = "ni845xSpiWriteRead"
    NI_845X_I2C_SET_PULLUP_ENABLE = "ni845xI2cSetPullupEnable"
    NI_845X_I2C_CONFIGURATION_SET_ADDRESS = "ni845xI2cConfigurationSetAddress"
    NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE = "ni845xI2cConfigurationSetClockRate"
    NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE = "ni845xI2cConfigurationSetAddressSize"
    NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT = "ni845xI2cConfigurationSetAckPollTimeout"
    NI_845X_I2C_CONFIGURATION_GET_ADDRESS = "ni845xI2cConfigurationGetAddress"
    NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE = "ni845xI2cConfigurationGetClockRate"
    NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE = "ni845xI2cConfigurationGetAddressSize"
    NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT = "ni845xI2cConfigurationGetAckPollTimeout"
    NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT = "ni845xSpiConfigurationSetChipSelect"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE = "ni845xSpiConfigurationSetClockRate"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE = "ni845xSpiConfigurationSetClockPhase"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY = "ni845xSpiConfigurationSetClockPolarity"
    NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT = "ni845xSpiConfigurationGetChipSelect"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE = "ni845xSpiConfigurationGetClockRate"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE = "ni845xSpiConfigurationGetClockPhase"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY = "ni845xSpiConfigurationGetClockPolarity"
    NI_845X_STATUS_TO_STRING = "ni845xStatusToString"


NI_845X_DLL = "Ni845x.dll"

MAX_BYTE_VALUE = 255
WRITE_INSTRUCTION = 0x2
READ_INSTRUCTION = 0x3
FIRST_FOUR_BYTES_MASK = 0xF


def ni_845x_open_impl(device_name: str) -> int:
    """Opens the specific NI-845x device.

    Args:
        device_name (str): The name of the device to be opened.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    device_name_buffer = create_string_buffer(device_name.encode("ascii"))
    handle_type = _get_handle_type()
    device_handle = handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_OPEN, device_name_buffer, byref(device_handle)
    )

    return device_handle.value


def ni_845x_close_impl(device_handle: int):
    """Closes a previously opened device.

    Args:
        device_handle (int):
            The device handle to be closed.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_CLOSE, handle_type(device_handle))


def ni_845x_device_lock_impl(device_handle: int):
    """Locks NI 845x devices for access by a single thread.

    Args:
        device_handle (int):
            The device handle to be locked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xDeviceLock`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_DEVICE_LOCK, handle_type(device_handle))


def ni_845x_device_unlock_impl(device_handle: int):
    """Unlocks NI 845x devices.

    Args:
        device_handle (int):
            The device handle to be unlocked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xUnlock` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_DEVICE_UNLOCK, handle_type(device_handle))


def ni_845x_set_io_voltage_level_impl(
    device_handle: int,
    voltage_level: Ni845xVoltageLevel,
):
    """Modifies the voltage output from a DIO port on an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        voltage_level (_Ni845xVoltageLevel):
            The desired voltage level.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetIoVoltageLevel`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL,
        handle_type(device_handle),
        c_uint8(voltage_level),
    )


def ni_845x_set_timeout_impl(device_handle: int, timeout_milliseconds: int):
    """Modifies the global timeout for operations when using an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        timeout_milliseconds (int):
            The timeout value in milliseconds.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetTimeout`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SET_TIMEOUT,
        handle_type(device_handle),
        timeout_milliseconds,
    )


def ni_845x_find_device_impl() -> DevicesFindResultData:
    """Finds an NI 845x device and returns the total number of NI 845x devices present.

    Returns:
        DevicesFindResultData: Tuple representing
            the name of the first device found,
            the handle identifying this search session (this handle is used as an input in
            ni845xFindDeviceNext and ni845xCloseFindDeviceHandle)
            and the total number of NI-845x devices found in the system.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDevice`
            function from `ni845x.dll`.
    """
    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)
    handle_type = _get_handle_type()
    find_device_handle = handle_type()
    number_of_devices_found = c_uint32()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE,
        string_buffer,
        byref(find_device_handle),
        byref(number_of_devices_found),
    )

    return DevicesFindResultData(
        str(string_buffer.value.decode()),
        find_device_handle.value,
        number_of_devices_found.value,
    )


def ni_845x_find_device_next_impl(find_device_handle: int) -> str:
    """Finds subsequent devices after `ni845xFindDevice` has been called.

    Args:
        find_device_handle (int):
            The device handle returned from `ni845xFindDevice`.

    Returns:
        str: The name of the next NI-845x device found.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDeviceNext`
            function from `ni845x.dll`.
    """
    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)
    handle_type = _get_handle_type()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE_NEXT,
        handle_type(find_device_handle),
        string_buffer,
    )

    return str(string_buffer.value.decode())


def ni_845x_close_find_device_handle_impl(find_device_handle: int):
    """Closes the handles created by `ni845xFindDevice`.

        Args:
            find_device_handle (int):
                The find device handle to be closed.
    (
        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xCloseFindDeviceHandle`
                function from `ni845x.dll`.
    """  # noqa: D214 - Section is over-indented (auto-generated noqa)
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_CLOSE_FIND_DEVICE_HANDLE,
        handle_type(find_device_handle),
    )


def ni_845x_i2c_configuration_open_impl() -> int:
    """Creates a new NI-845x I2C configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationOpen`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    configuration_handle = handle_type()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_OPEN,
        byref(configuration_handle),
    )

    return configuration_handle.value


def ni_845x_i2c_configuration_close_impl(configuration_handle: int):
    """Closes an I2C I/O configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationClose`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_CLOSE,
        handle_type(configuration_handle),
    )


def ni_845x_spi_configuration_open_impl() -> int:
    """Creates a new NI-845x SPI configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationOpen`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    configuration_handle = handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_OPEN,
        byref(configuration_handle),
    )

    return configuration_handle.value


def ni_845x_spi_configuration_close_impl(configuration_handle: int):
    """Closes an SPI configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationClose`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_CLOSE,
        handle_type(configuration_handle),
    )


def ni_845x_i2c_read_impl(
    device_handle: int,
    configuration_handle: int,
    read_data_array: numpy.ndarray,
):
    """Reads an array of data from an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cRead` function from `ni845x.dll`.
    """
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    read_data_array_buffer = read_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()
    number_of_data_read = c_uint32()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(read_data_array.size),
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_i2c_write_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
):
    """Writes an array of data to an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWrite` function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
    )


def ni_845x_i2c_write_read_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
    read_data_array: numpy.ndarray,
):
    """Performs a write followed by read (combined format) on an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWriteRead`
            function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    read_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()

    number_of_data_read = c_uint32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
        c_uint32(read_data_array.size),
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_spi_write_read_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
    read_data_array: numpy.ndarray,
):
    """Exchanges an array of data with an SPI slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to SPI device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from SPI device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiWriteRead`
            function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    read_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()

    number_of_data_read = c_uint32(read_data_array.size)

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_WRITE_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_i2c_set_pullup_enable_impl(
    device_handle: int,
    pullup_status: Ni845xPullupStatus,
):
    """Enables or disables the onboard pullup resistors for I2C operations.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        pullup_status (_Ni845xPullupStatus):
            The status for the pullup resistors.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cSetPullupEnable`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_SET_PULLUP_ENABLE,
        handle_type(device_handle),
        c_uint8(pullup_status),
    )


def ni_845x_i2c_configuration_set_address_impl(
    configuration_handle: int,
    address: int,
):
    """Sets the configuration's I2C slave address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        address (int):
            Specifies the address of the I2C Slave device.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddress` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS,
        handle_type(configuration_handle),
        c_uint16(address),
    )


def ni_845x_i2c_configuration_set_clock_rate_impl(
    configuration_handle: int,
    clock_rate_kilohertz: int,
):
    """Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the I2C clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE,
        handle_type(configuration_handle),
        c_uint16(clock_rate_kilohertz),
    )


def ni_845x_i2c_configuration_set_addressing_type_impl(
    configuration_handle: int,
    addressing_type: Ni845xI2cAddressingType,
):
    """Sets the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        addressing_type (_Ni845xI2cAddressingType):
            The addressing scheme to use when addressing
            the I2C slave device this configuration describes.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddressSize` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE,
        handle_type(configuration_handle),
        c_int32(addressing_type),
    )


def ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
    configuration_handle: int,
    timeout_milliseconds: int,
):
    """Sets the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        timeout_milliseconds (int):
            Specifies the I2C ACK poll timeout in milliseconds.
            When this value is zero, ACK polling is disabled.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAckPollTimeout` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT,
        handle_type(configuration_handle),
        c_uint16(timeout_milliseconds),
    )


def ni_845x_i2c_configuration_get_address_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The configuration address

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddress` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    address = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS,
        handle_type(configuration_handle),
        byref(address),
    )

    return address.value


def ni_845x_i2c_configuration_get_clock_rate_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_rate = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE,
        handle_type(configuration_handle),
        byref(clock_rate),
    )

    return clock_rate.value


def ni_845x_i2c_configuration_get_addressing_type_impl(
    configuration_handle: int,
) -> Ni845xI2cAddressingType:
    """Retrieves the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        Ni845xI2cAddressingType: the configuration addressing type.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddressSize` function from `ni845x.dll`.
    """  # noqa: D410, D411, W505 - Missing blank line after section (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)
    handle_type = _get_handle_type()

    addressing_type = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE,
        handle_type(configuration_handle),
        byref(addressing_type),
    )

    return Ni845xI2cAddressingType(addressing_type.value)


def ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The ACK poll timeout, in milliseconds.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAckPollTimeout` function from `ni845x.dll`.
    """  # noqa: D410, D411, W505 - Missing blank line after section (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)
    handle_type = _get_handle_type()

    timeout = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT,
        handle_type(configuration_handle),
        byref(timeout),
    )

    return timeout.value


def ni_845x_spi_configuration_set_chip_select_impl(
    configuration_handle: int,
    chip_select: int,
):
    """Sets the configuration chip select.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        chip_select (int):
            The chip select line for this configuration.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetChipSelect` function from `ni845x.dll`.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT,
        handle_type(configuration_handle),
        c_uint32(chip_select),
    )


def ni_845x_spi_configuration_set_clock_rate_impl(
    configuration_handle: int,
    clock_rate_kilohertz: int,
):
    """Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the SPI clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE,
        handle_type(configuration_handle),
        c_uint16(clock_rate_kilohertz),
    )


def ni_845x_spi_configuration_set_clock_phase_impl(
    configuration_handle: int,
    clock_phase: SpiConfigurationClockPhase,
):
    """Sets the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_phase (SpiConfigurationClockPhase):
            The positioning of the data bits relative to the clock edges for the SPI Port.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE,
        handle_type(configuration_handle),
        c_int32(clock_phase),
    )


def ni_845x_spi_configuration_set_clock_polarity_impl(
    configuration_handle: int,
    clock_polarity: SpiConfigurationClockPolarity,
):
    """Sets the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_polarity (SpiConfigurationClockPolarity):
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPolarity` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY,
        handle_type(configuration_handle),
        c_int32(clock_polarity),
    )


def ni_845x_spi_configuration_get_chip_select_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration chip select value.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The chip select.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetChipSelect` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    chip_select = c_uint32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT,
        handle_type(configuration_handle),
        byref(chip_select),
    )

    return chip_select.value


def ni_845x_spi_configuration_get_clock_rate_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_rate = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE,
        handle_type(configuration_handle),
        byref(clock_rate),
    )

    return clock_rate.value


def ni_845x_spi_configuration_get_clock_phase_impl(
    configuration_handle: int,
) -> SpiConfigurationClockPhase:
    """Retrieves the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPhase:
            The positioning of the data bits relative to
            the clock edges for the SPI Port (clock phase).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_phase = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE,
        handle_type(configuration_handle),
        byref(clock_phase),
    )

    return SpiConfigurationClockPhase(clock_phase.value)


def ni_845x_spi_configuration_get_clock_polarity_impl(
    configuration_handle: int,
) -> SpiConfigurationClockPolarity:
    """Retrieves the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPolarity:
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockPolarity` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_polarity = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY,
        handle_type(configuration_handle),
        byref(clock_polarity),
    )

    return SpiConfigurationClockPolarity(clock_polarity.value)


def invoke_ni_845x_function(function_name: str, *args):
    """Invokes a function from `ni845x.dll`.

    Args:
        function_name (str): the name of function from `ni845x.dll`.

    Raises:
        ValueError:
            Raised if `function_name` is None, empty or whitespace.
        PCBATTCommunicationException:
            Raised if `function_name` does not exist.
            Raised when an error occured while calling
            the function with `function_name` from `ni845x.dll`.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))
    function_arguments_types = []
    handle_type = _get_handle_type()
    functions_argument_types = _create_ni_845x_functions_arguments_types(handle_type)

    try:
        function_arguments_types = functions_argument_types[function_name]
    except Exception as e:
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, str(e)
            )
        ) from e

    status = None
    try:
        function_to_call = create_native_stdcall_win_function(
            dll_path=NI_845X_DLL,
            function_name=function_name,
            return_value_type=c_int32,
            arguments_types=function_arguments_types,
        )
        status = function_to_call(
            *args,
        )
    except Exception as e:
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, str(e)
            )
        ) from e

    if status is None:
        return

    if status != 0:
        status_description = _get_status_description(status)
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, status_description
            )
        )


def is_ni_845x_installed() -> bool:
    """Checks whether NI-845x drivers are installed on local system."""
    try:
        check_dll_availability("ni845x.dll")
        return True
    except FileNotFoundError:
        return False


def ni_845x_device_exists() -> bool:
    """Checks whether at least a NI-845x device is present on local system."""
    try:
        find_results = ni_845x_find_device_impl()
        ni_845x_close_impl(find_results.device_handle)
        return find_results.number_of_devices_found != 0
    except PCBATTCommunicationException:
        return False


def convert_memory_address_to_data_bytes_array(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
) -> List[int]:
    """Convert the memory address to an array of bytes used for
    device communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.

    Returns:
        List[int]: The array of bytes.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if address_type == DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE:
        return _create_one_byte_array(memory_address)

    if address_endianness == DataMemoryAddressEndianness.LITTLE_ENDIAN:
        return _create_two_bytes_array_little_endian(memory_address)

    return _create_two_bytes_array_big_endian(memory_address)


def create_command_for_spi_read_communication_impl(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
    number_of_bytes_to_read: int,
) -> List[int]:
    """Create an array of data bytes representing
    the read command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_read:
            The number of bytes to read.
    Returns:
        List[int]: The created array.
    """  # noqa: D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)
    instruction_value = _compute_spi_communication_command(
        READ_INSTRUCTION,
        memory_address,
        address_type,
    )

    spi_read_instruction_array = [instruction_value]
    spi_read_instruction_array.extend(
        convert_memory_address_to_data_bytes_array(memory_address, address_type, address_endianness)
    )
    spi_read_instruction_array.extend([0] * number_of_bytes_to_read)

    return spi_read_instruction_array


def create_command_for_spi_write_communication_impl(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
    number_of_bytes_to_write: int,
) -> List[int]:
    """Create an array of data bytes representing
    the write command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_write:
            The number of bytes to write.

    Returns:
        List[int]: The created array.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    instruction_value = _compute_spi_communication_command(
        WRITE_INSTRUCTION,
        memory_address,
        address_type,
    )

    spi_write_instruction_array = [instruction_value]
    spi_write_instruction_array.extend(
        convert_memory_address_to_data_bytes_array(memory_address, address_type, address_endianness)
    )
    spi_write_instruction_array.extend([0] * number_of_bytes_to_write)

    return spi_write_instruction_array


def _get_status_description(status: int) -> str:
    """Converts a status code into a descriptive string.

    Args:
        status (int): Status code returned from an NI-845x function from `ni845x.dll`.

    Returns:
        str: The description of the status code.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)

    function_to_call = create_native_stdcall_win_function(
        dll_path=NI_845X_DLL,
        function_name=_Ni845xFunctionsNames.NI_845X_STATUS_TO_STRING,
        return_value_type=None,
        arguments_types=[
            # int32, status code returned from an NI-845x function from `ni845x.dll`.
            c_int32,
            # uint32, Size of the buffer that receives
            # the description of the status code (in bytes).
            c_uint32,
            # c_char_p, buffer that receives the description of the status code.
            c_char_p,
        ],
    )

    function_to_call(
        c_int32(status),
        c_uint32(string_buffer_length),
        string_buffer,
    )
    return str(string_buffer.value.decode())


def _get_handle_type() -> Union[c_uint32, c_uint64]:
    """Retrieves the type of handle used by NI-845x functions
    according to the platform on which the Python executable runs.."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
    if is_python_windows_64bits():
        return c_uint64
    if is_python_windows_32bits():
        return c_uint32

    raise PCBATTCommunicationException(
        PCBATTCommunicationExceptionMessages.INVALID_OS_ENVIRONMENT_FOR_PYTHON
    )


def _create_one_byte_array(memory_address: int) -> List[int]:
    """creates an array with one byte element.

    Args:
        value (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The less significant byte of a short value.
        numpy.ubyte(memory_address & MAX_BYTE_VALUE),
    ]


def _create_two_bytes_array_little_endian(
    memory_address: int,
) -> List[int]:
    """creates an array with two bytes with little endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The most significant byte of a short value.
        (memory_address >> 8) & MAX_BYTE_VALUE,
        # The less significant byte of a short value.
        memory_address & MAX_BYTE_VALUE,
    ]


def _create_two_bytes_array_big_endian(
    memory_address: int,
) -> List[int]:
    """creates an array with two bytes with big endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The less significant byte of a short value.
        memory_address & MAX_BYTE_VALUE,
        # The most significant byte of a short value.
        (memory_address >> 8) & MAX_BYTE_VALUE,
    ]


def _compute_spi_communication_command(
    command_code: int, memory_address: int, address_type: DataMemoryAddressType
) -> int:
    """Computes the value of command used for SPI communications

    Args:
        command_code (int): The code of the command.
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.

    Returns:
        int: the computed value for the command.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    if address_type == DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE:
        # For address encoded on one byte,
        # some SPI devices require that the 4th bit
        # should be set with the 9th bit of memory address.
        return command_code + ((memory_address >> 5) & FIRST_FOUR_BYTES_MASK)

    return command_code


def _create_ni_845x_functions_arguments_types(
    handle_type: Union[c_uint32, c_uint64]
) -> Dict[str, List[Type]]:
    "Creates a dictionary containing the names of functions with the list of types of arguments."
    return {
        _Ni845xFunctionsNames.NI_845X_OPEN: [
            # c_char_p, resource name string corresponding to the NI 845x device to be opened.
            c_char_p,
            # POINTER(c_uint32 | c_uint64), pointer to the device handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_CLOSE: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_DEVICE_LOCK: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_DEVICE_UNLOCK: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint8, the voltage level.
            c_uint8,
        ],
        _Ni845xFunctionsNames.NI_845X_SET_TIMEOUT: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint32, the timeout value.
            c_uint32,
        ],
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE: [
            # c_char_p, buffer that receives the name of NI-845x device.
            c_char_p,
            # POINTER(c_uint32 | c_uint64), pointer on the find device handle.
            POINTER(handle_type),
            # c_uint8, the voltage level.
            POINTER(c_uint32),
        ],
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE_NEXT: [
            # c_uint32 | c_uint64, the find device handle.
            handle_type,
            # c_char_p, buffer that receives the name of NI-845x device.
            c_char_p,
        ],
        _Ni845xFunctionsNames.NI_845X_CLOSE_FIND_DEVICE_HANDLE: [
            # c_uint32 | c_uint64, the find device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_OPEN: [
            # POINTER(c_uint32 | c_uint64), pointer to the I2C configuration handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_CLOSE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_OPEN: [
            # POINTER(c_uint32 | c_uint64), pointer to the I2C configuration handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_CLOSE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array.
            c_uint32,
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
            # c_uint32, the size of the data array to read.
            c_uint32,
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_WRITE_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_SET_PULLUP_ENABLE: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint8, the voltage level.
            c_uint8,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the address.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the addressing type.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the ACK poll timeout.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the addressing type.
            POINTER(c_int32),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the ACK poll timeout.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint32, the chip select.
            c_uint32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the clock phase.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the clock polarity.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint32, pointer on the clock rate.
            POINTER(c_uint32),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the clock phase.
            POINTER(c_int32),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the clock polarity.
            POINTER(c_int32),
        ],
    }
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_data_types.py sha256=602ac490d52109cdd34823362238cbc2a64fb715aad0893d8f087d16b823d2a4 bytes=3303 -->
## FILE: src/nipcbatt/pcbatt_communication_library/ni_845x_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/ni_845x_data_types.py`
- sha256: `602ac490d52109cdd34823362238cbc2a64fb715aad0893d8f087d16b823d2a4`
- bytes: 3303

````python
"""Defines datatypes related to NI-845x modules."""

from collections import namedtuple
from enum import IntEnum


class DataMemoryAddressType(IntEnum):
    """Defines on which the size, in bytes,
    the memory address of the communication device is addressed."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (360 > 100 characters) (auto-generated noqa)

    ADDRESS_ENCODED_ON_ONE_BYTE = 1
    """The address is encoded on 1 byte."""

    ADDRESS_ENCODED_ON_TWO_BYTES = 2
    """The address is encoded on 2 bytes."""


class DataMemoryAddressEndianness(IntEnum):
    """Defines the endianness of the memory address
    in a device communication using I2C/SPI protocols."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (350 > 100 characters) (auto-generated noqa)

    LITTLE_ENDIAN = 0
    """Little Endian."""

    BIG_ENDIAN = 1
    """Big Endian."""


class Ni845xPullupStatus(IntEnum):
    """Defines the status of pullup resistor."""

    PULLUP_DISABLE = 0
    """Pullups are disabled."""

    PULLUP_ENABLE = 1
    """Pullups are enabled."""


class Ni845xI2cAddressingType(IntEnum):
    """Defines the addressing type used for configuration of I2C communication."""

    ADDRESSING_7_BIT = 0
    """The NI 845x hardware uses the standard 7-bit
    addressing when communicating with the I2C slave device."""

    ADDRESSING_10_BIT = 1
    """The NI 845x hardware uses the extended 10-bit 
    addressing when communicating with the I2C slave device."""


class Ni845xVoltageLevel(IntEnum):
    """Defines the voltage levels supported by NI-845x devices."""

    VOLTAGE_LEVEL_33 = 33
    """The output I/O high level is 3.3 V."""

    VOLTAGE_LEVEL_25 = 25
    """The output I/O high level is 2.5 V."""

    VOLTAGE_LEVEL_18 = 18
    """The output I/O high level is 1.8 V."""

    VOLTAGE_LEVEL_15 = 15
    """The output I/O high level is 1.5 V."""

    VOLTAGE_LEVEL_12 = 12
    """The output I/O high level is 1.2 V."""


class SpiConfigurationClockPhase(IntEnum):
    """Defines the clock phase used for configuration of SPI communication."""

    CLOCK_PHASE_FIRST_EDGE = 0
    """Data is centered on the first edge of the clock period."""

    CLOCK_PHASE_SECOND_EDGE = 1
    """Data is centered on the second edge of the clock period."""


class SpiConfigurationClockPolarity(IntEnum):
    """Defines the clock polarity used for configuration of SPI communication."""

    CLOCK_POLARITY_IDLE_LOW = 0
    """Clock is low in the idle state."""

    CLOCK_POLARITY_IDLE_HIGH = 1
    """Clock is high in the idle state."""


DevicesFindResultData = namedtuple(
    "DevicesFindResultData", ("device_name", "device_handle", "number_of_devices_found")
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_devices.py sha256=94ec2d52156ab154b966242ecf116c4f4076c149cc851cf2f9a048da14a17737 bytes=5110 -->
## FILE: src/nipcbatt/pcbatt_communication_library/ni_845x_devices.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/ni_845x_devices.py`
- sha256: `94ec2d52156ab154b966242ecf116c4f4076c149cc851cf2f9a048da14a17737`
- bytes: 5110

````python
"""Provides communication with NI-845x devices."""

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xVoltageLevel
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
)


class Ni845xDevicesHandler:
    """Defines methods used to handle NI-845x devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xI2cDevicesHandler` object"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
        self._devices_handler = None

    def is_initialized(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        return self._devices_handler is not None

    def open(self, device_name: str):
        """Opens the specific NI-845x device.

        Args:
            device_name (str): The name of the device to be opened.

        Raises:
            PCBATTLibraryException:
                Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`
        """
        self._devices_handler = _ni_845x_functions.ni_845x_open_impl(device_name)

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_close_impl(self._devices_handler)
        self._devices_handler = None

    def lock(self):
        """Locks the device for access by a single thread.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xLock` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_device_lock_impl(self._devices_handler)

    def unlock(self):
        """Unlocks the device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xUnlock` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_device_unlock_impl(self._devices_handler)

    def set_input_output_voltage_level(self, voltage_level: Ni845xVoltageLevel):
        """Sets the I/O voltage level supported by the device.

        Args:
            voltage_level (Ni845xVoltageLevel): The voltage level.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetIoVoltageLevel` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_set_io_voltage_level_impl(self._devices_handler, voltage_level)

    def set_timeout(self, timeout_milliseconds: int):
        """_summary_

        Args:
            timeout_milliseconds (int): _description_

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetTimeout` function from `ni845x.dll`
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_set_timeout_impl(self._devices_handler, timeout_milliseconds)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_i2c_communication_devices.py sha256=3bb9b77ad255734c912fcbb6c7cec153120a43ab1f2729301c8e8381af0cf6b1 bytes=12335 -->
## FILE: src/nipcbatt/pcbatt_communication_library/ni_845x_i2c_communication_devices.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/ni_845x_i2c_communication_devices.py`
- sha256: `3bb9b77ad255734c912fcbb6c7cec153120a43ab1f2729301c8e8381af0cf6b1`
- bytes: 12335

````python
"""Provides I2C communication with NI-845x devices."""

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
)
from nipcbatt.pcbatt_communication_library.ni_845x_devices import Ni845xDevicesHandler
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)


class Ni845xI2cDevicesHandler(Ni845xDevicesHandler):
    """Defines handler on I2C communication devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xI2cDevicesHandler` object."""
        super().__init__()
        self._configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(self._configuration_handle)
        super().close()

    @property
    def configuration(self):
        """Gets an instance of `Ni845xI2cConfiguration` used to configure I2C communication."""
        return Ni845xI2cConfiguration(self._configuration_handle)

    def read_data(self, number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]:
        """Reads a collection of data bytes from an I2C slave device.

        Args:
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_i2c_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array

    def write_data(self, data_bytes_to_be_written: numpy.ndarray[numpy.ubyte]):
        """Writes a collection of data bytes to an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                the type of numpy array is not `numpy.ubyte` or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_i2c_write_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
        )

    def write_and_read_data(
        self,
        data_bytes_to_be_written: numpy.ndarray[numpy.ubyte],
        number_of_bytes_to_read: int,
    ) -> numpy.ndarray[numpy.ubyte]:
        """Performs a write followed by read (combined format) on an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_i2c_write_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array

    def enable_pullup_resistors(self, enable: bool):
        """Enable or disables the on-board pullup resistors for I2C operations.

        Args:
            enable (bool):
               `False`: Pullup resistors are disabled.
               `True`: Pullup resistors are enabled.


        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cSetPullupEnable`
                function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_i2c_set_pullup_enable_impl(
            device_handle=self._devices_handler,
            pullup_status=(
                Ni845xPullupStatus.PULLUP_ENABLE if enable else Ni845xPullupStatus.PULLUP_DISABLE
            ),
        )


class Ni845xI2cConfiguration:
    """Defines methods used to configure I2C communication on a I2C device."""

    def __init__(self, configuration_handle: int) -> None:
        """Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._configuration_handle = configuration_handle

    @property
    def address(self) -> int:
        """Gets the configuration address.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cConfigurationGetAddress`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_address_impl(
            configuration_handle=self._configuration_handle
        )

    @address.setter
    def address(self, val: int):
        """Sets the configuration's I2C slave address.

        Args:
            val (int): Specifies the address of the I2C Slave device.
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_address_impl(
            configuration_handle=self._configuration_handle, address=val
        )

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate of the configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_clock_rate_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_rate_kilohertz.setter
    def clock_rate_kilohertz(self, val: int):
        """Sets the clock rate of the configuration.

        Args:
            val (int): Specifies the I2C clock rate in kilohertz.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSetClockRate`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_clock_rate_impl(
            configuration_handle=self._configuration_handle, clock_rate_kilohertz=val
        )

    @property
    def addressing_type(self) -> Ni845xI2cAddressingType:
        """Gets the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAddressSize`
                function from `ni845x.dll`

        Returns:
            int: the type of address used for configuration.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_addressing_type_impl(
            configuration_handle=self._configuration_handle
        )

    @addressing_type.setter
    def addressing_type(self, val: Ni845xI2cAddressingType):
        """Sets the type of address used for configuration.

        Args:
            val (int): the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSnoetAddressSize`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_addressing_type_impl(
            configuration_handle=self._configuration_handle, addressing_type=val
        )

    @property
    def ack_poll_timeout_milliseconds(self) -> int:
        """Gets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAckPollTimeout`
                function from `ni845x.dll`

        Returns:
            int: The I2C ACK (acknowledge) polling timeout in milliseconds.
        """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
        return _ni_845x_functions.ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
            configuration_handle=self._configuration_handle
        )

    @ack_poll_timeout_milliseconds.setter
    def ack_poll_timeout_milliseconds(self, val: int):
        """Sets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Args:
            val (int): the I2C ACK (acknowledge) polling timeout in milliseconds.
        """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
        _ni_845x_functions.ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
            configuration_handle=self._configuration_handle, timeout_milliseconds=val
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_spi_communication_devices.py sha256=958577378eaf0ad09836df6e143c3849b6d9dcdc27977ba5b32c4437a212aee1 bytes=8644 -->
## FILE: src/nipcbatt/pcbatt_communication_library/ni_845x_spi_communication_devices.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/ni_845x_spi_communication_devices.py`
- sha256: `958577378eaf0ad09836df6e143c3849b6d9dcdc27977ba5b32c4437a212aee1`
- bytes: 8644

````python
"""Provides SPI communication with NI-845x devices."""

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.ni_845x_devices import Ni845xDevicesHandler
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)


class Ni845xSpiDevicesHandler(Ni845xDevicesHandler):
    """Defines handler on SPI devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xSpiDevicesHandler` object"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
        super().__init__()
        self._configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(self._configuration_handle)
        super().close()

    @property
    def configuration(self):
        """Gets an instance of `` used to configure I2C communication.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before.
        """
        return Ni845xSpiConfiguration(self._configuration_handle)

    def write_and_read_data(
        self,
        data_bytes_to_be_written: numpy.ndarray[numpy.ubyte],
        number_of_bytes_to_read: int,
    ) -> numpy.ndarray[numpy.ubyte]:
        """Performs a write followed by read (combined format) on an SPI slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_spi_write_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array


class Ni845xSpiConfiguration:
    """Defines methods used to configure SPI communication on a SPI device."""

    def __init__(self, configuration_handle: int) -> None:
        """Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._configuration_handle = configuration_handle

    @property
    def chip_select(self) -> int:
        """Gets the chip select value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetChipSelect`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_chip_select_impl(
            configuration_handle=self._configuration_handle
        )

    @chip_select.setter
    def chip_select(self, val: int):
        """Sets the chip select value for SPI configuration.

        Args:
            val (int): the chip select value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_chip_select_impl(
            configuration_handle=self._configuration_handle, chip_select=val
        )

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: the clock rate of the SPI configuration.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_rate_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_rate_kilohertz.setter
    def clock_rate_kilohertz(self, val: int):
        """Sets the clock rate of the SPI configuration.

        Args:
            val (int): the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetClockRate`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_rate_impl(
            configuration_handle=self._configuration_handle, clock_rate_kilohertz=val
        )

    @property
    def clock_phase(self) -> SpiConfigurationClockPhase:
        """Gets the clock phase value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPhase`
                function from `ni845x.dll`

        Returns:
            SpiConfigurationClockPhase: The configuration address.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_phase_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_phase.setter
    def clock_phase(self, val: SpiConfigurationClockPhase):
        """Sets the clock phase value for SPI configuration.

        Args:
            val (int): the clock phase value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_phase_impl(
            configuration_handle=self._configuration_handle, clock_phase=val
        )

    @property
    def clock_polarity(self) -> SpiConfigurationClockPolarity:
        """Gets the clock polarity value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPolarity`
                function from `ni845x.dll`

        Returns:
            int: The clock polarity value for SPI configuration.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_polarity_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_polarity.setter
    def clock_polarity(self, val: SpiConfigurationClockPolarity):
        """Sets the clock polarity value for SPI configuration.

        Args:
            val (int): the clock polarity value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_polarity_impl(
            configuration_handle=self._configuration_handle, clock_polarity=val
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/pcbatt_communication_exceptions.py sha256=26f046c9d5deb1e251eb09ad2267d5658a31c67330dbb320bdd393bae5a9df6c bytes=1079 -->
## FILE: src/nipcbatt/pcbatt_communication_library/pcbatt_communication_exceptions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/pcbatt_communication_exceptions.py`
- sha256: `26f046c9d5deb1e251eb09ad2267d5658a31c67330dbb320bdd393bae5a9df6c`
- bytes: 1079

````python
"""Defines a set of exceptions that can be raised by pcbatt communication module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)


class PCBATTCommunicationException(  # noqa: N818 - exception name 'PCBATTCommunicationException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by
    nipcatt.pcbatt_communication_library package."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/pcbatt_communication_messages.py sha256=8df192bca89e30ab5ef8632297b1f076f028480528b478afc847401c3aeea865 bytes=1208 -->
## FILE: src/nipcbatt/pcbatt_communication_library/pcbatt_communication_messages.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_communication_library/pcbatt_communication_messages.py`
- sha256: `8df192bca89e30ab5ef8632297b1f076f028480528b478afc847401c3aeea865`
- bytes: 1208

````python
"""Module containing message strings."""


class PCBATTCommunicationExceptionMessages:
    """Messages used in exception classes."""

    ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog input channel is not compatible with the specific measurement ({})."
    )

    CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2 = "The class {} does not implement the method {}."

    VISA_SERIAL_DEVICE_NOT_INITIALIZED = "VISA serial instrument not initialized"

    SECOND_ARGUMENT_OF_TYPE_INT_FLOAT_OR_STRING = (
        "Second argument must be a int or float value"
        + " for cold-junction compensation value,"
        + " or a string for cold-junction compensation channel name"
    )

    INVALID_OS_ENVIRONMENT_FOR_PYTHON = (
        "Current Python interpreter is not running under Windows os "
        + "with 32bit or 64bit architecture."
    )

    LIBRARY_LOAD_FAILED_ARGS_2 = "Failed to load native library {}: {}."

    FUNCTION_CALL_FAILED_ARGS_2 = "Failed to call function {}: {}."

    INVALID_NUMPY_ARRAY_TYPE_ARGS_1 = "the type of the numpy array is not of {}."

    OPEN_METHOD_MUST_BE_CALLED_FIRST = "Open method must be called first."
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/animation_and_sound_user_input_test.py sha256=24c0dc72227d453841bae3fe27e411369f851cee8d97e11b2f489bacd44f2eca bytes=9393 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/animation_and_sound_user_input_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/animation_and_sound_user_input_test.py`
- sha256: `24c0dc72227d453841bae3fe27e411369f851cee8d97e11b2f489bacd44f2eca`
- bytes: 9393

````python
"""Animation and Sound User Input Test"""  

import os  
import sys  
from time import sleep

import nidaqmx.constants
from limit_exception import ( 
    LimitException,
)

import nipcbatt
from nipcbatt import daq


class AnimationAndSoundUserInputTest: 
    def __init__(self): 
        self.digital_state_gen_task = None
        self.time_domain_meas_task = None
        self.dyn_digit_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(self):  
        self.initialize_push_user_button(channel_expression="TS_BUTTON0")
        self.initialize_tp_tweeter(channel_expression="TP_TWEET0")
        self.initialize_leds_pattern(channel_expression="TP_AN_LED0:2")

    def initialize_push_user_button(  
        self, channel_expression: str
    ) -> None:
        self.digital_state_gen_task = daq.StaticDigitalStateGeneration()
        self.digital_state_gen_task.initialize(channel_expression=channel_expression)

    def initialize_tp_tweeter( 
        self, channel_expression: str
    ) -> None:
        self.time_domain_meas_task = daq.TimeDomainMeasurement()
        self.time_domain_meas_task.initialize(analog_input_channel_expression=channel_expression)

    def initialize_leds_pattern(  
        self, channel_expression: str
    ) -> None:
        self.dyn_digit_meas_task = daq.DynamicDigitalPatternMeasurement()
        self.dyn_digit_meas_task.initialize(channel_expression=channel_expression)

    def main(self): 
        self.configure_tweeter_meas()
        self.configure_dig_pattern()
        self.turn_on_dut_user_button()
        self.wait_for_500_ms_seconds_push_button()
        self.turn_off_dut_user_button()
        self.measure_and_check_leds_pattern()
        self.fetch_tweeter_sound()

    def configure_tweeter_meas( 
        self,
    ) -> None:
        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=1000,
            number_of_samples_per_channel=2500,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.time_domain_meas_task.configure_and_measure(configuration=configuration)

    def configure_dig_pattern(  
        self,
    ) -> None:
        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100.0,
            number_of_samples_per_channel=200,
            active_edge=nidaqmx.constants.Edge.RISING,
        )

        trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=measurement_options,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

        self.dyn_digit_meas_task.configure_and_measure(configuration=configuration)

    def turn_on_dut_user_button(  
        self,
    ) -> None:
        configuration = daq.StaticDigitalStateGenerationConfiguration(data_to_write=[True])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def wait_for_500_ms_seconds_push_button(  
        self,
    ) -> None:
        sleep(0.5)

    def turn_off_dut_user_button( 
        self,
    ) -> None:
        configuration = daq.StaticDigitalStateGenerationConfiguration(data_to_write=[False])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def measure_and_check_leds_pattern( 
        self,
    ) -> None:
        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000.0,
            number_of_samples_per_channel=1000,
            active_edge=nidaqmx.constants.Edge.RISING,
        )

        trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=measurement_options,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

        self.dyn_digit_meas_task.configure_and_measure(configuration=configuration)

    def fetch_tweeter_sound(  
        self,
    ) -> None:
        # Fetches the measured DC Voltage (measured after Button action) and returns Time Domain Analysis Frequency 
        # NOTE: This Step errors outs for non-periodic waveform captures.

        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.time_domain_meas_task.configure_and_measure(configuration=configuration)

        lower_limit = 990
        upper_limit = 1010
        if result_data.voltage_waveforms_frequencies_hertz:
            tested_value = result_data.voltage_waveforms_frequencies_hertz[0]
        else:
            tested_value = lower_limit  # default for test purposes

        print("\n\n1. Measure Tweeter Frequency")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail  -- Measure frequency:", tested_value)
            print("Measured value must between 990 and 1010 Hz", "\n")
        else:
            print("Status: Pass", "\n")

    def cleanup(  
        self,
    ) -> None:
        self.close_tweeter_meas()
        self.close_leds_pattern()
        self.close_push_button()

    def close_tweeter_meas(  
        self,
    ) -> None:
        self.time_domain_meas_task.close()

    def close_leds_pattern(  
        self,
    ) -> None:
        self.dyn_digit_meas_task.close()

    def close_push_button( 
        self,
    ) -> None:
        self.digital_state_gen_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/audio_filter_test.py sha256=d7aed17f772d7bd22900439f0fcd80c9034c39738d68dab7a55707ff60a5e1ea bytes=11042 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/audio_filter_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/audio_filter_test.py`
- sha256: `d7aed17f772d7bd22900439f0fcd80c9034c39738d68dab7a55707ff60a5e1ea`
- bytes: 11042

````python
"""Audio Filter Test""" 

import os  
import sys  
from time import sleep  

import nidaqmx.constants
from limit_exception import (  
    LimitException,
)

import nipcbatt
from nipcbatt import daq

class AudioFilterTest:  
    def __init__(self):  
        self.signal_voltage_gen_task = None
        self.freq_domain_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(  
        self,
    ) -> None:
        self.initialize_multi_tone_audio_signal_gen()
        self.initialize_audio_meas()

    def initialize_multi_tone_audio_signal_gen( 
        self,
    ) -> None:
        self.signal_voltage_gen_task = daq.SignalVoltageGeneration()
        self.signal_voltage_gen_task.initialize("TS_LINE_IN0")

    def initialize_audio_meas(  
        self,
    ) -> None:
        self.freq_domain_meas_task = daq.FrequencyDomainMeasurement()
        self.freq_domain_meas_task.initialize("TP_LINE_OUT0")

    def main(self) -> None:  
        self.configure_audio_meas()
        self.send_multi_tone_audio_signal()
        self.measure_tone()

    def configure_audio_meas( 
        self,
    ) -> None:
        # Configure Freq Domain Measurement settings to wait for Hardware Trigger from Audio Signal Generation  

        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100000,
            number_of_samples_per_channel=10000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.freq_domain_meas_task.configure_and_measure(configuration=configuration)

    def send_multi_tone_audio_signal(  
        self,
    ) -> None:
        voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=-10, range_max_volts=10
        )

        tone1 = daq.ToneParameters(
            tone_frequency_hertz=10, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone2 = daq.ToneParameters(
            tone_frequency_hertz=100, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone3 = daq.ToneParameters(
            tone_frequency_hertz=1000, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone4 = daq.ToneParameters(
            tone_frequency_hertz=10000, tone_amplitude_volts=1, tone_phase_radians=0
        )

        multiple_tones_parameters = [tone1, tone2, tone3, tone4]

        waveform_parameters = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_amplitude_volts=1,
            multiple_tones_parameters=multiple_tones_parameters,
        )

        timing_parameters = daq.SignalVoltageGenerationTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100000,
            generated_signal_duration_seconds=0.1,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.SignalVoltageGenerationMultipleTonesConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.signal_voltage_gen_task.configure_and_generate_multiple_tones_waveform(
            configuration=configuration
        )

    def measure_tone( 
        self,
    ) -> None:
        # Fetches the Analog Input voltage waveforms (Started measure when Signal Voltage generation sends Trigger) and returns Freq Domain Analysis 

        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.freq_domain_meas_task.configure_and_measure(configuration=configuration)

        print("\n\n -- Measure Tone Frequencies -- \n")

        lower_limit = 9
        upper_limit = 11
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[0]

        print("Tone 0:")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Failed  -- Measured frequency: ", tested_value)
            print("Measured frequency must be between 9 and 11 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 90
        val_max = 110
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[1]

        print("Tone 1:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 90 and 110 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 900
        val_max = 1100
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[2]

        print("Tone 2:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 900 and 1100 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 9000
        val_max = 11000
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[3]

        print("Tone 3:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 9000 and 11000 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        print("\n -- Measure Tone Amplitudes -- \n")

        val_min = 0.9
        val_max = 1.2
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[0]

        print("Tone 0:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.2 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[1]

        print("Tone 1:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[2]
        print("Tone 2:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[3]
        print("Tone 3:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

    def cleanup(  
        self,
    ) -> None:
        self.close_multi_tone_audio_signal_gen()
        self.close_audio_meas()

    def close_multi_tone_audio_signal_gen(  
        self,
    ) -> None:
        self.signal_voltage_gen_task.close()

    def close_audio_meas(  
        self,
    ) -> None:
        self.freq_domain_meas_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/Hardware_Config_Demo.ini sha256=409745add6e285ad3cd162920070a3bc365c2f4ee1165de53c1772800a7869a1 bytes=4975 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/Hardware_Config_Demo.ini

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/Hardware_Config_Demo.ini`
- sha256: `409745add6e285ad3cd162920070a3bc365c2f4ee1165de53c1772800a7869a1`
- bytes: 4975

````ini
[DAQmx]
MajorVersion = 23
MinorVersion = 5

[DAQmxChannel TP_ACT_LED0]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TP_AN_LED0]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line1
Descr = 

[DAQmxChannel TP_AN_LED1]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line2
Descr = 

[DAQmxChannel TP_AN_LED2]
DI.InvertLines = 0
ChanType = Digital Input
PhysicalChanName = Sim_PC_basedDAQ/port0/line3
Descr = 

[DAQmxChannel TP_LINE_OUT0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_POWER0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai0
Descr = 

[DAQmxChannel TP_POWER1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai1
Descr = 

[DAQmxChannel TP_POWER2]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Simulated_AI/ai2
Descr = 

[DAQmxChannel TP_REG0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TP_REG1]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai1
Descr = 

[DAQmxChannel TP_TWEET0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = Sim_PC_basedDAQ/ai0
Descr = 

[DAQmxChannel TS_BUTTON0]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxChannel TS_LINE_IN0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 10
AO.Min = -10
ChanType = Analog Output
AO.TermCfg = RSE
PhysicalChanName = Sim_PC_basedDAQ/ao0
Descr = 

[DAQmxChannel TS_RESET0]
DO.InvertLines = 0
ChanType = Digital Output
PhysicalChanName = Sim_PC_basedDAQ/port0/line0
Descr = 

[DAQmxDevice Sim_PC_basedDAQ]
ProductType = PCIe-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7431C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice Sim_PC_basedDAQ1]
ProductType = PCIe-6353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7431C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxCDAQChassis Sim_TS]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQChassis Sim_TS1]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule Simulated_AI]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule Simulated_AO]
ProductType = TS-15110
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule Simulated_Core]
ProductType = TS-15050 DIO P0
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule Simulated_DIO]
ProductType = TS-15120
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 5

[DAQmxCDAQModule Simulated_DO]
ProductType = TS-15130
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 6

[DAQmxCDAQModule Simulated_Power]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule Simulated_TS1_AI]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule Simulated_TS1_AO]
ProductType = TS-15110
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule Simulated_TS1_Core]
ProductType = TS-15050 DIO P0
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule Simulated_TS1_DIO]
ProductType = TS-15120
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 5

[DAQmxCDAQModule Simulated_TS1_DO]
ProductType = TS-15130
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 6

[DAQmxCDAQModule Simulated_TS1_Power]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = Sim_TS1
CompactDAQ.SlotNum = 2
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/limit_exception.py sha256=311bff15a8beec9dbcd8f6b01a864df3916e5c425d8a9656997b55c2aa48b910 bytes=613 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/limit_exception.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/limit_exception.py`
- sha256: `311bff15a8beec9dbcd8f6b01a864df3916e5c425d8a9656997b55c2aa48b910`
- bytes: 613

````python
class LimitException(  
    BaseException
):
    def __init__( 
        self,
        called_class: str,
        called_method: str,
        test: str,
        lower_limit: float,
        upper_limit: float,
        unit: str,
        value: float,
    ) -> None:
        self.caller = "Sequence : " + called_class + ", method : " + called_method
        self.message = (
            test
            + " should be between "
            + str(lower_limit)
            + " and "
            + str(upper_limit)
            + unit
            + ", Result "
            + str(value)
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/pcba_ft_demo_test_sequence.py sha256=e83940846036cd594e2a1c1edda5b0ab19c63b865fd98bbcb579bba4f582d1f4 bytes=1659 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/pcba_ft_demo_test_sequence.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/pcba_ft_demo_test_sequence.py`
- sha256: `e83940846036cd594e2a1c1edda5b0ab19c63b865fd98bbcb579bba4f582d1f4`
- bytes: 1659

````python
"""
PCBA FT Demo Test Sequences demonstrates testing of PCBA DUTs using PCIe DAQ and TestScale Hardware. 
These example sequences can be executed in hardware simulation using the Python pcbatt 
measurement libraries and can be built off of for a custom sequencer.

Limits suggested will return a FAIL test with DAQ simulation and they need to be changed 
to match your physical hardware.
"""  

from animation_and_sound_user_input_test import AnimationAndSoundUserInputTest
from audio_filter_test import AudioFilterTest
from limit_exception import LimitException
from power_diagnostics import PowerDiagnostics
from reset_and_self_test import ResetAndSelfTest
from turn_off_all_ao_channels import TurnOffAllAOChannels


class MainSequence:
    """Sequence for testing different systems"""  

    def __init__(self) -> None:  
        self.main()
        self.cleanup()

    def main(self) -> None:
        """Main method"""  
        try:
            print("\n\n------Power Diagnostics------\n")
            PowerDiagnostics()
            print("\n\n------Reset and Self Test------\n\n")
            ResetAndSelfTest()
            print("\n\n------Animation and Sound User Input Test------\n")
            AnimationAndSoundUserInputTest()
            print("\n\n------Audio Filter Test------\n")
            AudioFilterTest()
        except LimitException as e:
            print(e.caller)
            print(e.message)
        except ValueError as e:
            print(e)

    def cleanup(self) -> None:
        """turn everything off"""  
        t = TurnOffAllAOChannels()
        t.cleanup()


MainSequence()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/power_diagnostics.py sha256=79fe3c6ba26ae792001dbb0e4fbcc864006384d2e0839c720dc819e221f3dfee bytes=8534 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/power_diagnostics.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/power_diagnostics.py`
- sha256: `79fe3c6ba26ae792001dbb0e4fbcc864006384d2e0839c720dc819e221f3dfee`
- bytes: 8534

````python
"""Power Diagnostics"""  

import os  
import sys  
from time import sleep 

import nidaqmx.constants
from limit_exception import ( 
    LimitException,
)

import nipcbatt
from nipcbatt import daq


class PowerDiagnostics:  
    def __init__(self):  
        self.ps_task = None
        self.dc_voltage_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup( 
        self,
    ) -> None:
        # Power up and Validate Start-up, Transition Max Current, Idle Power Consumption and DC Regulators  
        self.initialize_power_supply()
        self.initialize_dc_regulator_tps()

    def initialize_power_supply(  
        self,
    ) -> None:
        self.ps_task = daq.PowerSupplySourceAndMeasure()
        self.ps_task.initialize("Simulated_Power/power")

    def initialize_dc_regulator_tps( 
        self,
    ) -> None:
        self.dc_voltage_meas_task = daq.DcRmsVoltageMeasurement()
        self.dc_voltage_meas_task.initialize("TP_REG0:1")

    def main(self) -> None:   
        self.power_on_and_measure_startup_max_current()
        self.measure_idle_power_consumption()
        self.measure_dc_regulator_voltages()

    def power_on_and_measure_startup_max_current(   
        self,
    ) -> None:
        terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=6,
            current_setpoint_amperes=3,
            power_sense=nidaqmx.constants.Sense.REMOTE,
            idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
            enable_output=True,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=terminal_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.ps_task.configure_and_measure(configuration=configuration)

        lower_limit = 0
        upper_limit = 1
        tested_value = result_data.max_current_level_amperes

        print("\n\n1. Power On & Maximum Current Measurement")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail  -- Measured current:", tested_value)
            print("Maximum current must be between 0.0 and 1.0 ", "\n")
        else:
            print("Status: Pass", "\n")

    def measure_idle_power_consumption(   
        self,
    ) -> None:
        terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=6,
            current_setpoint_amperes=3,
            power_sense=nidaqmx.constants.Sense.REMOTE,
            idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
            enable_output=True,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=terminal_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.ps_task.configure_and_measure(configuration=configuration)

        lower_limit = 4.5
        upper_limit = 5.5
        tested_value = result_data.average_power_value_watts

        print("2. Measure Idle Power Consumption")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail -- Measured power:", tested_value)
            print("Average power value must be between 4.5 and 5.5 watts", "\n")
        else:
            print("Status: Pass", "\n")

    def measure_dc_regulator_voltages( 
        self,
    ) -> None:
        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = daq.DcRmsVoltageMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.dc_voltage_meas_task.configure_and_measure(configuration=configuration)

        lower_limit = 4.9
        upper_limit = 5.2
        tested_value = result_data.dc_values_volts[0]

        print("\n\n3. Measure DC Regulator Voltages")

        print("TP_REG0:")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail -- Measured voltage:", tested_value)
            print("TP_REG0 must be between 4.9 and 5.2 volts", "\n")
        else:
            print("Status: Pass", "\n")

        lower_limit = 3.1
        upper_limit = 3.4
        tested_value = result_data.dc_values_volts[1]

        print("TP_REG1:")
        if tested_value < lower_limit or tested_value > upper_limit:
            if tested_value < lower_limit or tested_value > upper_limit:
                print("Status: Fail -- Measured voltage:", tested_value)
                print("TP_REG1 must be between 3.1 and 3.4 volts", "\n")
            else:
                print("Status: Pass", "\n")

    def cleanup(   
        self,
    ) -> None:
        self.close_power_supply()
        self.close_dc_regulators_meas()

    def close_power_supply(   
        self,
    ) -> None:
        self.ps_task.close()

    def close_dc_regulators_meas(   
        self,
    ) -> None:
        self.dc_voltage_meas_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/reset_and_self_test.py sha256=7745a12d34a7fe6e80b98d9e2843b33076db17834b9c6e463096dffb63a84dc1 bytes=3563 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/reset_and_self_test.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/reset_and_self_test.py`
- sha256: `7745a12d34a7fe6e80b98d9e2843b33076db17834b9c6e463096dffb63a84dc1`
- bytes: 3563

````python
"""Reset and Self-Test"""  

import os  
import sys
from time import sleep, time

import nidaqmx.constants  

import nipcbatt
from nipcbatt import daq

class ResetAndSelfTest:  
    def __init__(self) -> None: 
        self.digital_state_meas_task = None
        self.digital_state_gen_task = None

        self.start_time = None
        self.elasped_time = 0

        self.led = [False]

        self.setup()
        self.main()
        self.cleanup()

    def setup(  
        self,
    ) -> None:
        self.initialize_reset_button()
        self.initialize_led_status()

    def initialize_reset_button(   
        self,
    ) -> None:
        self.digital_state_gen_task = daq.StaticDigitalStateGeneration()
        self.digital_state_gen_task.initialize("TS_RESET0")

    def initialize_led_status(   
        self,
    ) -> None:
        self.digital_state_meas_task = daq.StaticDigitalStateMeasurement()
        self.digital_state_meas_task.initialize("TP_ACT_LED0")

    def main(self) -> None:   
        self.turn_on_dut_reset_button()
        self.wait_for_100_ms_seconds_in_reset_enabled_state()
        self.turn_off_dut_reset_button()
        self.get_start_time()
        while self.led[0] is False and self.elasped_time < 30:
            self.wait_led_activity()
            self.led_state_status()
            self.get_current_time()
        self.dut_elasped_time_validation_or_timeout()

    def turn_on_dut_reset_button(   
        self,
    ) -> None:
        configuration = daq.StaticDigitalStateGenerationConfiguration(data_to_write=[True])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def wait_for_100_ms_seconds_in_reset_enabled_state(   
        self,
    ) -> None:
        sleep(0.1)

    def turn_off_dut_reset_button(   
        self,
    ) -> None:
        configuration = daq.StaticDigitalStateGenerationConfiguration(data_to_write=[False])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def get_start_time(   
        self,
    ) -> None:
        self.start_time = time()

    def wait_led_activity(   
        self,
    ) -> None:
        sleep(0.1)

    def led_state_status(   
        self,
    ) -> None:
        result_data = self.digital_state_meas_task.configure_and_measure()
        self.led = result_data.digital_states

    def get_current_time(   
        self,
    ) -> None:
        self.elasped_time = time() - self.start_time

    def dut_elasped_time_validation_or_timeout(   
        self,
    ) -> None:
        if self.elasped_time >= 30:
            # Gather the name of the class and the method where the exception was raised
            exception_message = (
                "Sequence : "
                + self.__class__.__name__
                + ", Method : "
                + sys._getframe().f_code.co_name
                + "\n"
            )
            exception_message += "DUT wasn't able to start in 30 seconds"
            raise ValueError(exception_message)
        else:
            print("Status: Pass -- Elapsed time: ", self.elasped_time)

    def cleanup(   
        self,
    ) -> None:
        self.close_led_status()
        self.close_reset_button()

    def close_led_status(   
        self,
    ) -> None:
        self.digital_state_meas_task.close()

    def close_reset_button(   
        self,
    ) -> None:
        self.digital_state_gen_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/turn_off_all_ao_channels.py sha256=2c4ec330548810816d1a96946451e6bc8ad735a9c5c2980fc86afa2facd297ef bytes=1506 -->
## FILE: src/nipcbatt/pcbatt_ft_demo_test_sequence/turn_off_all_ao_channels.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_ft_demo_test_sequence/turn_off_all_ao_channels.py`
- sha256: `2c4ec330548810816d1a96946451e6bc8ad735a9c5c2980fc86afa2facd297ef`
- bytes: 1506

````python
"""Turn Off all AO Channels""" 

import nipcbatt
from nipcbatt import daq


class TurnOffAllAOChannels: 
    def __init__(self) -> None: 
        self.dc_voltage_gen_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(   
        self,
    ) -> None:
        self.dc_voltage_generation_initialize_ao_channels()

    def dc_voltage_generation_initialize_ao_channels(   
        self,
    ) -> None:
        self.dc_voltage_gen_task = daq.DcVoltageGeneration()
        self.dc_voltage_gen_task.initialize("Sim_PC_basedDAQ/ao0:3")

    def main(self) -> None:   
        self.dc_voltage_generation_configure_initiate_and_sources_dc_voltage()

    def dc_voltage_generation_configure_initiate_and_sources_dc_voltage(   
        self,
    ) -> None:
        voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
            range_min_volts=-10, range_max_volts=10
        )

        configuration = daq.DcVoltageGenerationConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            output_voltages=[0.0, 0.0, 0.0, 0.0],
        )

        self.dc_voltage_gen_task.configure_and_generate(configuration=configuration)

    def cleanup(   
        self,
    ) -> None:
        self.dc_voltage_generation_close_ao_channels()

    def dc_voltage_generation_close_ao_channels(   
        self,
    ) -> None:
        self.dc_voltage_gen_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/__init__.py sha256=eaa47bd118f977f375c63ed0cb8916b0fed591788cd795f2dc5505d2e524aaa9 bytes=267 -->
## FILE: src/nipcbatt/pcbatt_library/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/__init__.py`
- sha256: `eaa47bd118f977f375c63ed0cb8916b0fed591788cd795f2dc5505d2e524aaa9`
- bytes: 267

````python
"""Provides nipcbatt library of measurement, generation and communication modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (195 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/__init__.py sha256=cf978a656543bd6053f4a9d04eff4209d0c5a7e71630639484284c66a0a98dc8 bytes=229 -->
## FILE: src/nipcbatt/pcbatt_library/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/common/__init__.py`
- sha256: `cf978a656543bd6053f4a9d04eff4209d0c5a7e71630639484284c66a0a98dc8`
- bytes: 229

````python
"""Provides nipcbatt library common modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/common_data_types.py sha256=8f4f44719d8d0fc686f3825d21f7357188a65c744cb3868113d758b79d8ac758 bytes=18074 -->
## FILE: src/nipcbatt/pcbatt_library/common/common_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/common/common_data_types.py`
- sha256: `8f4f44719d8d0fc686f3825d21f7357188a65c744cb3868113d758b79d8ac758`
- bytes: 18074

````python
"""Defines datatypes that are common to all pcba test toolkit building blocks."""

from enum import Enum
from typing import Iterable

import nidaqmx.constants
import numpy
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

MAXIMUM_NUMBER_OF_DIMENSIONS_IN_NUMPY_ARRAY = 2


class MeasurementExecutionType(Enum):
    """Defines the way the measurement is executed."""

    CONFIGURE_AND_MEASURE = 0
    """Configuration and procedure to measurement."""

    CONFIGURE_ONLY = 1
    """Configuration only."""

    MEASURE_ONLY = 2
    """Measurement procedure only."""


class MeasurementAnalysisRequirement(Enum):
    """Defines the way analysis is proceeded during measurement."""

    SKIP_ANALYSIS = 0
    """Skip analysis, analysis step is not required."""

    PROCEED_TO_ANALYSIS = 1
    """Proceed to analysis; analysis step is required."""


class SampleTimingEngine(Enum):
    """Defines which timing engine to use for the task."""

    TE0 = 0
    """TE0 engine."""

    TE1 = 1
    """TE1 engine."""

    AI = 2
    """AI engine."""

    AUTO = 3
    """Auto"""


class StartTriggerType(Enum):
    """Define the types used for start trigger during measurement."""

    NO_TRIGGER = 0
    """No trigger configured."""

    DIGITAL_TRIGGER = 1
    """Digital Start trigger."""


class MeasurementOptions(PCBATestToolkitData):
    """Defines the options for execution of measurement."""

    def __init__(
        self,
        execution_option: MeasurementExecutionType,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> None:
        """Used to initialize an instance of `MeasurementOptions`.

        Args:
            execution_option (MeasurementExecutionType):
               The type of measurement execution selected by user.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
               The measurement analysis requirement selected by user.
        """
        self._execution_option = execution_option
        self._measurement_analysis_requirement = measurement_analysis_requirement

    @property
    def execution_option(self) -> MeasurementExecutionType:
        """Gets the type of measurement execution selected by user."""
        return self._execution_option

    @property
    def measurement_analysis_requirement(self) -> MeasurementAnalysisRequirement:
        """Gets the measurement analysis requirement selected by user."""
        return self._measurement_analysis_requirement


class SampleClockTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock timing for measurement."""

    def __init__(
        self,
        sample_clock_source: str,
        sampling_rate_hertz: int,
        number_of_samples_per_channel: int,
        sample_timing_engine: SampleTimingEngine,
    ) -> None:
        """Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            sample_timing_engine (SampleTimingEngine): The engine for sample timing.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_greater_than_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._number_of_samples_per_channel = number_of_samples_per_channel
        self._sample_timing_engine = sample_timing_engine

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def number_of_samples_per_channel(self) -> int:
        """Gets the number of samples per channel."""
        return self._number_of_samples_per_channel

    @property
    def sample_timing_engine(self) -> SampleTimingEngine:
        """Gets the engine for sample timing."""
        return self._sample_timing_engine


class DynamicDigitalPatternTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock edge for measurement."""

    def __init__(
        self,
        sample_clock_source: str = "OnboardClock",
        sampling_rate_hertz: float = 10000.0,
        number_of_samples_per_channel: int = 50,
        active_edge: nidaqmx.constants.Edge = nidaqmx.constants.Edge.RISING,
    ) -> None:
        """Used to initialize an instance of `DynamicDigitalPatternTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (float): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            active_edge (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse to start acquiring samples.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is None or less than zero,
                if 'number_of_samples_per_channel' is None or less than zero,
                if 'active_edge' is None.
        """  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        # Input validation
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_not_none(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_float(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_greater_than_or_equal_to_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_not_none(number_of_samples_per_channel, nameof(number_of_samples_per_channel))
        Guard.is_greater_than_or_equal_to_zero(
            number_of_samples_per_channel, nameof(number_of_samples_per_channel)
        )
        Guard.is_not_none(active_edge, nameof(active_edge))

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._number_of_samples_per_channel = number_of_samples_per_channel
        self._active_edge = active_edge

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> float:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def number_of_samples_per_channel(self) -> int:
        """Gets the number of samples per channel."""
        return self._number_of_samples_per_channel

    @property
    def active_edge(self) -> nidaqmx.constants.Edge:
        """Gets the engine for sample timing."""
        return self._active_edge


class DigitalStartTriggerParameters(PCBATestToolkitData):
    """Defines the settings of triggers for measurement."""

    def __init__(
        self,
        trigger_select: StartTriggerType,
        digital_start_trigger_source: str,
        digital_start_trigger_edge: nidaqmx.constants.Edge,
    ) -> None:
        """Initializes an instance of `DigitalStartTriggerParameters`.

        Args:
            trigger_select (StartTriggerType): The type of trigger
            digital_start_trigger_source (str): The source of digital start trigger.
            digital_start_trigger_edge (nidaqmx.constants.Edge):
                The `nidaqmx.constants.Edge` value that specifies on which edge
                of a digital pulse to start acquiring or generating samples.

        Raises:
            ValueError:
                Raised if `digital_start_trigger_source` is None or empty or white space.
        """
        if trigger_select == StartTriggerType.DIGITAL_TRIGGER:
            # Check argument digital_start_trigger_source
            # if trigger_select is StartTriggerType.DIGITAL_TRIGGER
            Guard.is_not_none_nor_empty_nor_whitespace(
                digital_start_trigger_source, nameof(digital_start_trigger_source)
            )
        self._trigger_select = trigger_select
        self._digital_start_trigger_source = digital_start_trigger_source
        self._digital_start_trigger_edge = digital_start_trigger_edge

    @property
    def trigger_select(self) -> StartTriggerType:
        """Gets the type of trigger."""
        return self._trigger_select

    @property
    def digital_start_trigger_source(self) -> str:
        """Gets the source of digital start trigger."""
        return self._digital_start_trigger_source

    @property
    def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge:
        """Gets the `nidaqmx.constants.Edge` value
        that specifies on which edge
        of a digital pulse to start acquiring or generating samples."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_edge


class MeasurementData(PCBATestToolkitData):
    """Defines the data captured for measurement."""

    def __init__(self, data_samples: numpy.ndarray) -> None:
        """Initializes an instance of `MeasurementData`.

        Args:
            samples (numpy.ndarray):
                The array containing the samples captured for measurement.
        Raises:
            ValueError:
                Raised when `samples` is None or empty.
        """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
        Guard.is_not_none(data_samples, nameof(data_samples))
        Guard.is_not_empty(data_samples, nameof(data_samples))
        Guard.size_is_less_than_or_equal(
            data_samples.shape,
            MAXIMUM_NUMBER_OF_DIMENSIONS_IN_NUMPY_ARRAY,
            nameof(data_samples.shape),
        )

        self._data_samples = data_samples

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `MeasurementData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return numpy.allclose(self._data_samples, value_to_compare._data_samples)

        return False

    @property
    def samples_per_channel(self) -> Iterable[numpy.ndarray[numpy.float64]]:
        """Gets a iterable instance on the samples array per channel."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)

        if len(self._data_samples.shape) <= 1:
            yield self._data_samples
            return

        for samples_per_channel in self._data_samples:
            yield samples_per_channel


class AnalogWaveform(PCBATestToolkitData):
    """Define the structure of a waveform."""

    def __init__(
        self,
        channel_name: str,
        delta_time_seconds: float,
        samples: numpy.ndarray[float],
    ) -> None:
        """Used to initialize an instance of `AnalogWaveform`.

        Args:
            channel_name (str): The name of physical channel where samples were captured from.
            delta_time_seconds (float): The time between two samples (in seconds).
            samples (numpy.ndarray): The array of samples.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `delta_time_seconds` if less than or equal to zero
            or if `samples` is none or empty.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_greater_than_zero(delta_time_seconds, nameof(delta_time_seconds))
        Guard.is_not_none(samples, nameof(samples))
        Guard.is_not_empty(samples, nameof(samples))

        self._channel_name = channel_name
        self._delta_time_seconds = delta_time_seconds
        self._samples = samples

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `AnalogWaveform` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return (
                self._channel_name == value_to_compare._channel_name
                and self._delta_time_seconds == value_to_compare._delta_time_seconds
                and numpy.allclose(self._samples, value_to_compare._samples)
            )

        return False

    @property
    def channel_name(self) -> str:
        """Gets the name of physical channel where samples were captured from."""
        return self._channel_name

    @property
    def delta_time_seconds(self) -> float:
        """Gets the time between two samples (in seconds)."""
        return self._delta_time_seconds

    @property
    def samples(self) -> numpy.ndarray[float]:
        """Gets the array of samples."""
        return self._samples


class AmplitudeSpectrum(PCBATestToolkitData):
    """Defines the structure of a frequency spectrum."""

    def __init__(
        self,
        channel_name: str,
        spectrum_start_frequency_hertz: float,
        spectrum_frequency_resolution_hertz: float,
        amplitudes: numpy.ndarray[float],
    ) -> None:
        """Used to initialize an instance of `AmplitudeSpectrum`.

        Args:
            channel_name (`str`): The name of physical channel where samples were captured from.
            spectrum_start_frequency_hertz (`float`):
                The frequency of start of spectrum, expressed in Hertz.
            spectrum_frequency_resolution_hertz (`float`):
                The frequency interval between two amplitude values, expressed in Hertz.
            amplitudes (`numpy.ndarray[float]`): The array of amplitudes.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `spectrum_frequency_resolution_hertz` if less than or equal to zero
            or if `amplitudes` is None or empty.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_greater_than_zero(
            spectrum_frequency_resolution_hertz,
            nameof(spectrum_frequency_resolution_hertz),
        )
        Guard.is_not_none(amplitudes, nameof(amplitudes))
        Guard.is_not_empty(amplitudes, nameof(amplitudes))

        self._amplitudes = amplitudes
        self._spectrum_start_frequency_hertz = spectrum_start_frequency_hertz
        self._spectrum_frequency_resolution_hertz = spectrum_frequency_resolution_hertz
        self._channel_name = channel_name

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `AmplitudeSpectrum` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return (
                self._channel_name == value_to_compare._channel_name
                and self._spectrum_start_frequency_hertz
                == value_to_compare._spectrum_start_frequency_hertz
                and self._spectrum_frequency_resolution_hertz
                == value_to_compare._spectrum_frequency_resolution_hertz
                and numpy.allclose(self._amplitudes, value_to_compare._amplitudes)
            )

        return False

    @property
    def channel_name(self) -> str:
        """Gets the name of physical channel where samples were captured from."""
        return self._channel_name

    @property
    def spectrum_frequency_resolution_hertz(self) -> float:
        """Gets the frequency interval between two amplitude values, expressed in Hertz."""
        return self._spectrum_frequency_resolution_hertz

    @property
    def spectrum_start_frequency_hertz(self) -> float:
        """Gets the frequency of start of spectrum, expressed in Hertz."""
        return self._spectrum_start_frequency_hertz

    @property
    def amplitudes(self) -> numpy.ndarray[float]:
        """Gets the array of amplitudes."""
        return self._amplitudes
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/helper_functions.py sha256=9533b19326bf4ca3e0126ff442bd4f3bf10d5ed9b1a01946935fb2634efb9733 bytes=3282 -->
## FILE: src/nipcbatt/pcbatt_library/common/helper_functions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/common/helper_functions.py`
- sha256: `9533b19326bf4ca3e0126ff442bd4f3bf10d5ed9b1a01946935fb2634efb9733`
- bytes: 3282

````python
"""Various helper functions usable by any module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)


def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]:
    """Formats a value in engineering notation with an SI prefix.

    Args:
        measured_value: The numerical value to format.
        total_digits: Total number of significant digits to display.

    Returns:
        tuple: (formatted_number, si_prefix)
            - formatted_number: The scaled value as a string with appropriate decimal places.
            - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'u', 'm') or exponential notation.

    How it works:
        1. Convert measured_value to scientific notation.
        2. Transform to engineering notation (exponent divisible by 3).
        3. Scale the mantissa accordingly to match engineering exponent.
        4. Determine decimal places needed to maintain significant figures.
        5. Map engineering exponent to SI prefix (m, k, M, G, etc.).
        6. Return formatted number and SI prefix.
    """
    sci_str = f"{measured_value:.{total_digits-1}e}"
    mantissa_str, exp_str = sci_str.split("e")
    mantissa = float(mantissa_str)
    exponent = int(exp_str)

    eng_exponent = 3 * (exponent // 3)
    scaled_value = mantissa * (10 ** (exponent - eng_exponent))

    decimal_places = total_digits - len(str(int(abs(scaled_value))))
    decimal_places = max(0, decimal_places)
    formatted_number = f"{scaled_value:.{decimal_places}f}"

    si_prefixes = {
        -24: "y",
        -21: "z",
        -18: "a",
        -15: "f",
        -12: "p",
        -9: "n",
        -6: "u",
        -3: "m",
        0: "",
        3: "k",
        6: "M",
        9: "G",
        12: "T",
        15: "P",
        18: "E",
        21: "Z",
        24: "Y",
    }
    prefix = si_prefixes.get(eng_exponent, f"e{eng_exponent}")

    return (formatted_number, prefix)


# Helper function to generate ramp data
def digital_ramp_pattern_generator(
    number_of_samples: int = None, number_of_digital_lines: int = None
):
    """Generates Ramp based Digital Output Data couting from 0 upto (2^N)-1 where "N" represents the
    Number of Digital Lines."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (324 > 100 characters) (auto-generated noqa)
    if number_of_samples is (0 or None):
        raise ValueError("number_of_samples must be >= 1")
    if number_of_digital_lines is (0 or None):
        raise ValueError("number_of_digital lines must be >= 1")

    # create variables for holding data
    total_lines = 2**number_of_digital_lines
    port_digital_data = [0] * number_of_samples

    # populate array with values
    for i in range(number_of_samples):
        port_digital_data[i] = i % total_lines

    return port_digital_data
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/__init__.py sha256=4bdb9774296053b5994634baf5aff8da314533d23fed041c299718a96b2a5f6e bytes=3236 -->
## FILE: src/nipcbatt/pcbatt_library/communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/__init__.py`
- sha256: `4bdb9774296053b5994634baf5aff8da314533d23fed041c299718a96b2a5f6e`
- bytes: 3236

````python
"Provides commnuncations modules for pcbatt"
from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
    MemoryPageCharacteristics,
)
from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_i2c_communications,
    create_command_for_spi_read_communication,
    create_command_for_spi_write_communication,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_communication_constants import (
    DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    DEFAULT_I2C_DEVICE_PARAMETERS,
    DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_I2C_READ_PARAMETERS,
    DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION,
    DEFAULT_I2C_WRITE_PARAMETERS,
    ConstantsForI2cCommunication,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_read_communication import (
    I2cReadCommunication,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadCommunicationData,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_write_communication import (
    I2cWriteCommunication,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)

from nipcbatt.pcbatt_library.communications.serial_communications.serial_communication import (
    SerialCommunication,
)
from nipcbatt.pcbatt_library.communications.serial_communications.serial_communication_constants import (
    ConstantsForSerialCommunication,
)
from nipcbatt.pcbatt_library.communications.serial_communications.serial_data_types import (
    SerialCommunicationConfiguration,
    SerialCommunicationData,
    SerialCommunicationParameters,
)

from nipcbatt.pcbatt_library.communications.spi_communications.spi_communication_constants import (
    DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    DEFAULT_SPI_DEVICE_PARAMETERS,
    DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_READ_PARAMETERS,
    DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_WRITE_PARAMETERS,
    ConstantsForSpiCommunication,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_read_communication import (
    SpiReadCommunication,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadCommunicationData,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_write_communication import (
    SpiWriteCommunication,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/__init__.py sha256=3e1d496b1bfca92a6009afe39bf5a923d11c7e945c60a83e19eb9e507599c133 bytes=79 -->
## FILE: src/nipcbatt/pcbatt_library/communications/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/common/__init__.py`
- sha256: `3e1d496b1bfca92a6009afe39bf5a923d11c7e945c60a83e19eb9e507599c133`
- bytes: 79

````python
"Provides common data types and functions for communication building blocks."
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/communication_data_types.py sha256=05b4b132185e99d939994aeb31b70b90afb07d11a5b9d13713b85bcbdae5a9a8 bytes=5167 -->
## FILE: src/nipcbatt/pcbatt_library/communications/common/communication_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/common/communication_data_types.py`
- sha256: `05b4b132185e99d939994aeb31b70b90afb07d11a5b9d13713b85bcbdae5a9a8`
- bytes: 5167

````python
"""Defines datatypes that are common to communication building blocks based on I2C/SPI protocols."""

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class MemoryAddressParameters(PCBATestToolkitData):
    """Defines the settings used to specify data
    memory address format in communication device."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (346 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        memory_address: int,
        address_type: DataMemoryAddressType,
        address_endianness: DataMemoryAddressEndianness,
    ):
        """Initializes an instance of
        `MemoryAddressSettings` with specific values.

        Args:
            memory_address (int):
                The address where data are stored in device memory.
            address_type (DataMemoryAddressType):
                The type of address in device memory.
            address_endianness (DataMemoryAddressEndianness):
                The address endianness.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._memory_address = memory_address
        self._address_type = address_type
        self._address_endianness = address_endianness

    @property
    def memory_address(self) -> int:
        """Gets the address where data are stored in device memory."""
        return self._memory_address

    @property
    def address_type(self) -> DataMemoryAddressType:
        """Gets the type of address in device memory."""
        return self._address_type

    @property
    def address_endianness(self) -> DataMemoryAddressEndianness:
        """Gets the address endianness."""
        return self._address_endianness


class MemoryPageCharacteristics(PCBATestToolkitData):
    """Characteristics of a page in the device memory.
    A page is a sub-collection of the data bytes
    starting at specific index in the data collection and a specific length."""  # noqa: D205, D209, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), doc line too long (270 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        index_in_data_bytes_array: int,
        number_of_bytes_in_page: int,
        data_memory_address: int,
    ) -> None:
        """Initializes an instance of
        `MemoryPageCharacteristics` with specific values.

        Args:
            index_in_data_bytes_array (int):
                The index of first byte of the page in the data bytes array.
            number_of_bytes_in_page (int):
                The number of data bytes in a page.
            data_memory_address (int):
                The address value where the page will be stored.

        Raises:
            ValueError:
                Raised when
                `index_in_data_bytes_array` is negative,
                `number_of_bytes_in_page` is negative or equal to zero,
                `data_memory_address` is negative.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_or_equal_to_zero(
            index_in_data_bytes_array, nameof(index_in_data_bytes_array)
        )
        Guard.is_greater_than_zero(number_of_bytes_in_page, nameof(number_of_bytes_in_page))
        Guard.is_greater_than_or_equal_to_zero(data_memory_address, nameof(data_memory_address))

        self._index_in_data_bytes_array = index_in_data_bytes_array
        self._number_of_bytes_in_page = number_of_bytes_in_page
        self._data_memory_address = data_memory_address

    @property
    def index_in_data_bytes_array(self) -> int:
        """Gets the index of first byte of the page in the data collection."""
        return self._index_in_data_bytes_array

    @property
    def number_of_bytes_in_page(self) -> int:
        """Gets The number of data bytes in a page."""
        return self._number_of_bytes_in_page

    @property
    def data_memory_address(self) -> int:
        """Gets The address value where the page will be stored."""
        return self._data_memory_address
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/communication_functions.py sha256=cb0e63a1b49d0ecaa6c9b53cdad17b562b74beeb7a403f24e48c740c96e39678 bytes=6488 -->
## FILE: src/nipcbatt/pcbatt_library/communications/common/communication_functions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/common/communication_functions.py`
- sha256: `cb0e63a1b49d0ecaa6c9b53cdad17b562b74beeb7a403f24e48c740c96e39678`
- bytes: 6488

````python
"""Defines functions that are common to communication building blocks based on I2C/SPI protocols."""

from typing import List

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
    MemoryPageCharacteristics,
)


def create_command_for_i2c_communications(
    address_parameters: MemoryAddressParameters,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the command for I2C communications.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.convert_memory_address_to_data_bytes_array(
            address_parameters.memory_address,
            address_parameters.address_type,
            address_parameters.address_endianness,
        ),
        dtype=numpy.ubyte,
    )


def create_command_for_spi_read_communication(
    address_parameters: MemoryAddressParameters,
    number_of_bytes_to_read: int,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the command for SPI read communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_to_read (int):
            The number of bytes to read from SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.create_command_for_spi_read_communication_impl(
            memory_address=address_parameters.memory_address,
            address_type=address_parameters.address_type,
            address_endianness=address_parameters.address_endianness,
            number_of_bytes_to_read=number_of_bytes_to_read,
        ),
        dtype=numpy.ubyte,
    )


def create_command_for_spi_write_communication(
    address_parameters: MemoryAddressParameters,
    number_of_bytes_to_write: int,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the instruction for SPI write communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_for_access (int):
            The number of bytes to write to SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the instruction.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.create_command_for_spi_write_communication_impl(
            address_parameters.memory_address,
            address_parameters.address_type,
            address_parameters.address_endianness,
            number_of_bytes_to_write,
        ),
        dtype=numpy.ubyte,
    )


def compute_pages_characteristics(
    data_memory_start_address: int,
    number_of_bytes_to_write: int,
    number_of_bytes_per_page: int,
) -> List[MemoryPageCharacteristics]:
    """Computes the list of contiguous pages that will contain data bytes to write to device.

    Args:
        data_memory_start_address (int):
            The address where data bytes will be written.
            This is also the address of the first page.
        number_of_bytes_to_write (int):
            The total number of bytes to write to device.
        number_of_bytes_per_page (int):
            The number of bytes in a memory page.
    Returns:
        List[MemoryPageCharacteristics]:
            A list of `MemoryPageCharacteristics` representing
            the zone of memory pages where data will be written.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    pages_characteristics = []

    current_page_address = data_memory_start_address
    current_index_in_data_bytes_array = 0

    # The first page contains enough data bytes to fit at start EEPROM address.
    # So that, Data Memory Address + Current Number Of Bytes In Page =>
    # Start Address of the next Page.
    current_number_of_bytes_in_page = (
        data_memory_start_address // number_of_bytes_per_page + 1
    ) * number_of_bytes_per_page - data_memory_start_address

    while current_index_in_data_bytes_array < number_of_bytes_to_write:
        # if this is the last page to add,
        # the number of bytes is the number of bytes to write - the current index
        number_ob_bytes_in_page = (
            current_number_of_bytes_in_page
            if (current_index_in_data_bytes_array + current_number_of_bytes_in_page)
            < number_of_bytes_to_write
            else number_of_bytes_to_write - current_index_in_data_bytes_array
        )
        page_chatacteristics = MemoryPageCharacteristics(
            index_in_data_bytes_array=current_index_in_data_bytes_array,
            number_of_bytes_in_page=number_ob_bytes_in_page,
            data_memory_address=current_page_address,
        )
        pages_characteristics.append(page_chatacteristics)

        current_index_in_data_bytes_array += current_number_of_bytes_in_page
        current_page_address += current_number_of_bytes_in_page
        current_number_of_bytes_in_page = number_of_bytes_per_page

    return pages_characteristics
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/__init__.py sha256=96c653b68c348c2bb35a14727cf2c218dbc15d2b978a6d6409578810808d5e1b bytes=240 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/__init__.py`
- sha256: `96c653b68c348c2bb35a14727cf2c218dbc15d2b978a6d6409578810808d5e1b`
- bytes: 240

````python
"""Provides nipcbatt library I2C communication modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_communication_constants.py sha256=2ef33abf2002d609c4ab2166df22e7676b385ffb82f9bc88654fb3f4b9f3e387 bytes=3976 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_communication_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_communication_constants.py`
- sha256: `2ef33abf2002d609c4ab2166df22e7676b385ffb82f9bc88654fb3f4b9f3e387`
- bytes: 3976

````python
""" Constants data types for I2C communications."""

import dataclasses

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    Ni845xVoltageLevel,
)
from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)


@dataclasses.dataclass
class ConstantsForI2cCommunication:
    """Constants used for I2C communication."""

    DEFAULT_ENABLE_I2C_PULLUP_RESISTOR = False
    DEFAULT_VOLTAGE_LEVEL = Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    DEFAULT_DEVICE_ADDRESS = 0x50
    DEFAULT_CLOCK_RATE_KILOHERTZ = 100
    DEFAULT_ADDRESSING_TYPE = Ni845xI2cAddressingType.ADDRESSING_7_BIT
    DEFAULT_ACK_POLL_TIMEOUT_MILLISECONDS = 0
    DEFAULT_NUMBER_OF_BYTES_TO_READ = 128
    DEFAULT_MEMORY_ADDRESS = 0
    DEFAULT_MEMORY_ADDRESS_TYPE = DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
    DEFAULT_MEMORY_ADDRESS_ENDIANNESS = DataMemoryAddressEndianness.BIG_ENDIAN
    DEFAULT_NUMBER_OF_BYTES_PER_PAGE = 128
    DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS = 4


DEFAULT_I2C_DEVICE_PARAMETERS = I2cDeviceParameters(
    enable_i2c_pullup_resistor=ConstantsForI2cCommunication.DEFAULT_ENABLE_I2C_PULLUP_RESISTOR,
    voltage_level=ConstantsForI2cCommunication.DEFAULT_VOLTAGE_LEVEL,
)

DEFAULT_I2C_COMMUNICATION_PARAMETERS = I2cCommunicationParameters(
    device_address=ConstantsForI2cCommunication.DEFAULT_DEVICE_ADDRESS,
    addressing_type=ConstantsForI2cCommunication.DEFAULT_ADDRESSING_TYPE,
    clock_rate_kilohertz=ConstantsForI2cCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ,
    ack_poll_timeout_milliseconds=(
        ConstantsForI2cCommunication.DEFAULT_ACK_POLL_TIMEOUT_MILLISECONDS
    ),
)

DEFAULT_I2C_READ_PARAMETERS = I2cReadParameters(
    number_of_bytes_to_read=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ,
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_I2C_WRITE_PARAMETERS = I2cWriteParameters(
    number_of_bytes_per_page=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE,
    delay_between_page_write_operations_milliseconds=(
        ConstantsForI2cCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS
    ),
    data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte),
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION = I2cReadCommunicationConfiguration(
    device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    read_parameters=DEFAULT_I2C_READ_PARAMETERS,
)

DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION = I2cWriteCommunicationConfiguration(
    device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    write_parameters=DEFAULT_I2C_WRITE_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_data_types.py sha256=40179f25c9254b47028f77b3e547c4a3380da8908cb5dd45444066c6180db351 bytes=5213 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_data_types.py`
- sha256: `40179f25c9254b47028f77b3e547c4a3380da8908cb5dd45444066c6180db351`
- bytes: 5213

````python
""" I2C communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xI2cAddressingType,
    Ni845xVoltageLevel,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cDeviceParameters(PCBATestToolkitData):
    """Defines the parameters used to configure I2C device for communications."""

    def __init__(self, enable_i2c_pullup_resistor: bool, voltage_level: Ni845xVoltageLevel):
        """Initializes an instance of
        `I2cDeviceParameters` with specific values.

        Args:
            enable_i2c_pullup_resistor (bool):
                A boolean value that indicates whether
                the on-board pullup resistors for I2C operations are enabled.
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during I2C communications.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._enable_i2c_pullup_resistor = enable_i2c_pullup_resistor
        self._voltage_level = voltage_level

    @property
    def enable_i2c_pullup_resistor(self) -> bool:
        """Gets whether the on-board pullup resistors for I2C operations are enabled."""
        return self._enable_i2c_pullup_resistor

    @property
    def voltage_level(self) -> Ni845xVoltageLevel:
        """Gets the `Ni845xVoltageLevel` value."""
        return self._voltage_level


class I2cCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure I2C communications."""

    def __init__(
        self,
        device_address: int,
        addressing_type: Ni845xI2cAddressingType,
        clock_rate_kilohertz: int,
        ack_poll_timeout_milliseconds: int,
    ):
        """Initializes an instance of
        `I2cCommunicationParameters` with specific values.

        Args:
            device_address (int):
                The address of the device.
            addressing_type (Ni845xI2cAddressingType):
                The addressing type used for configuration of I2C communication.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            ack_poll_timeout_milliseconds (int):
                The I2C ACK (acknowledge) polling timeout
                to apply to the device communication, in milliseconds.

        Raises:
            ValueError:
                Raised when
                `device_address` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
                `ack_poll_timeout_milliseconds` is negative.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_or_equal_to_zero(device_address, nameof(device_address))
        Guard.is_greater_than_zero(clock_rate_kilohertz, nameof(clock_rate_kilohertz))
        Guard.is_greater_than_or_equal_to_zero(
            ack_poll_timeout_milliseconds, nameof(ack_poll_timeout_milliseconds)
        )

        self._device_address = device_address
        self._addressing_type = addressing_type
        self._clock_rate_kilohertz = clock_rate_kilohertz
        self._ack_poll_timeout_milliseconds = ack_poll_timeout_milliseconds

    @property
    def device_address(self) -> int:
        """Gets the address of the device."""
        return self._device_address

    @property
    def addressing_type(self) -> Ni845xI2cAddressingType:
        """Gets the addressing type used for configuration of I2C communication."""
        return self._addressing_type

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate to apply to the device communication."""
        return self._clock_rate_kilohertz

    @property
    def ack_poll_timeout_milliseconds(self) -> int:
        """Gets the I2C ACK (acknowledge) polling timeout
        to apply to the device communication, in milliseconds."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._ack_poll_timeout_milliseconds
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_communication.py sha256=7986c3818b44a264892dc7a701e9c423fd366040556abb7ba2136760aa2e00d9 bytes=4828 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_communication.py`
- sha256: `7986c3818b44a264892dc7a701e9c423fd366040556abb7ba2136760aa2e00d9`
- bytes: 4828

````python
""" Defines class used for I2C read communication on PCB points. """

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xPullupStatus
from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    create_command_for_i2c_communications,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadCommunicationData,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xI2cDevice,
)


class I2cReadCommunication(BuildingBlockUsingNi845xI2cDevice):
    """Defines a way that allows you to perform a read operation from I2C device."""

    def initialize(self, device_name: str):
        """Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        """
        if self.is_devices_handler_initialized:
            return

        self.devices_handler.open(device_name=device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_devices_handler_initialized:
            return

        self.devices_handler.close()

    def configure_and_read_data(
        self,
        configuration: I2cReadCommunicationConfiguration,
    ) -> I2cReadCommunicationData:
        """Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (I2cReadCommunicationConfiguration):
                An instance of `I2cReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        """
        # Configuration of the device for I2C communications.
        self.configure_device_for_i2c_communications(parameters=configuration.device_parameters)

        # Configuration of I2C communication.
        self.configure_i2c_communication(parameters=configuration.communication_parameters)

        # Read of data bytes from I2C device.
        return self.read_data(parameters=configuration.read_parameters)

    def configure_device_for_i2c_communications(self, parameters: I2cDeviceParameters) -> None:
        """Configures the device for I2C communications.

        Args:
            parameters (I2cDeviceParameters):
                A `I2cDeviceParameters` object used to configure the device for I2C communications.
        """
        self.devices_handler.set_input_output_voltage_level(voltage_level=parameters.voltage_level)
        self.devices_handler.enable_pullup_resistors = (
            Ni845xPullupStatus.PULLUP_ENABLE
            if parameters.enable_i2c_pullup_resistor
            else Ni845xPullupStatus.PULLUP_DISABLE
        )

    def configure_i2c_communication(self, parameters: I2cCommunicationParameters) -> None:
        """Configures the I2C communication.

        Args:
            parameters (I2cCommunicationParameters):
                A `I2cCommunicationParameters` object used to configure I2C communications.
        """
        self.devices_handler.configuration.address = parameters.device_address
        self.devices_handler.configuration.addressing_type = parameters.addressing_type
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.ack_poll_timeout_milliseconds = (
            parameters.ack_poll_timeout_milliseconds
        )

    def read_data(self, parameters: I2cReadParameters) -> I2cReadCommunicationData:
        """Reads data bytes from an I2C device.

        Args:
            parameters (I2cReadParameters):
                A `I2cReadParameters` object used
                to perform read operations on I2C device.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        """
        data_to_be_writtten = create_command_for_i2c_communications(
            address_parameters=parameters.memory_address_parameters
        )
        data_bytes_read = self.devices_handler.write_and_read_data(
            data_bytes_to_be_written=data_to_be_writtten,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )
        return I2cReadCommunicationData(data_bytes_read=data_bytes_read)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_data_types.py sha256=ed67546c4ee2e9ba646f7f9ce1b7bd783413e80b095cd95d2874175bb38eae18 bytes=8628 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_data_types.py`
- sha256: `ed67546c4ee2e9ba646f7f9ce1b7bd783413e80b095cd95d2874175bb38eae18`
- bytes: 8628

````python
""" I2C read communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (152 > 100 characters) (auto-generated noqa)

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cReadParameters(PCBATestToolkitData):
    """Defines the parameters used to perform read operations on I2C device."""

    def __init__(
        self,
        number_of_bytes_to_read: int,
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `I2cReadParameters` with specific values.

        Args:
            number_of_bytes_to_read (int):
                The number of bytes to read.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            ValueError:
                Raised when
                `number_of_bytes_to_read` is negative or equal to zero,
                `memory_address_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(number_of_bytes_to_read, nameof(number_of_bytes_to_read))
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))

        self._number_of_bytes_to_read = number_of_bytes_to_read
        self._memory_address_parameters = memory_address_parameters

    @property
    def number_of_bytes_to_read(self) -> int:
        """Gets thhe number of bytes to read."""
        return self._number_of_bytes_to_read

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        return self._memory_address_parameters


class I2cReadCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the I2C Read communication."""

    def __init__(
        self,
        device_parameters: I2cDeviceParameters,
        communication_parameters: I2cCommunicationParameters,
        read_parameters: I2cReadParameters,
    ):
        """Initializes an instance of
        `I2cReadCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2CCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            read_parameters (I2cReadParameters):
                An instance of `I2cReadParameters` that represents
                the parameters used for settings of I2C Read communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `communication_read_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(read_parameters, nameof(read_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._read_parameters = read_parameters

    @property
    def device_parameters(self) -> I2cDeviceParameters:
        """Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (370 > 100 characters) (auto-generated noqa)
        return self._device_parameters

    @property
    def communication_parameters(self) -> I2cCommunicationParameters:
        """Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def read_parameters(self) -> I2cReadParameters:
        """Gets an instance of `I2cReadParameters` that represents
        the parameters used for settings of I2C Read communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
        return self._read_parameters


class I2cReadCommunicationData(PCBATestToolkitData):
    """Defines data obtained after I2C read communication on I2C device."""

    def __init__(self, data_bytes_read: numpy.ndarray[numpy.ubyte]):
        """Initializes an instance of
        `I2cReadCommunicationData` with specific values.

        Args:
            data_bytes_read (numpy.ndarray):
                The array of data bytes read from I2C Device.

        Raises:
            ValueError:
                Raised when `data_bytes_read` is None or empty,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(data_bytes_read, nameof(data_bytes_read))
        Guard.is_not_empty(data_bytes_read, nameof(data_bytes_read))

        self._data_bytes_read = data_bytes_read

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `I2CReadCommunicationData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return numpy.allclose(self._data_bytes_read, value_to_compare._data_bytes_read)

        return False

    @property
    def data_bytes_read(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the array of data bytes read from I2C Device."""
        return self._data_bytes_read
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_communication.py sha256=02febbb123241978a46fc47db3943fa40386d0b5960c6eca5ca92ae4e20362df bytes=6052 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_communication.py`
- sha256: `02febbb123241978a46fc47db3943fa40386d0b5960c6eca5ca92ae4e20362df`
- bytes: 6052

````python
""" Defines class used for I2C write communication on PCB points. """

import time

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xPullupStatus
from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_i2c_communications,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xI2cDevice,
)


class I2cWriteCommunication(BuildingBlockUsingNi845xI2cDevice):
    """Defines a way that allows you to perform a write operation to I2C device,"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def initialize(self, device_name: str):
        """Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        """
        if self.is_devices_handler_initialized:
            return

        self.devices_handler.open(device_name=device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_devices_handler_initialized:
            return

        self.devices_handler.close()

    def configure_and_write_data(self, configuration: I2cWriteCommunicationConfiguration) -> None:
        """Defines class used for I2C write communication on PCB points.

        Args:
            configuration (I2cWriteCommunicationConfiguration):
                An instance of `I2cWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Configuration of the device for I2C communications.
        self.configure_device_for_i2c_communications(parameters=configuration.device_parameters)

        # Configuration of I2C communication.
        self.configure_i2c_communication(parameters=configuration.communication_parameters)

        # Write of data bytes to I2C device.
        self.write_data(parameters=configuration.write_parameters)

    def configure_device_for_i2c_communications(self, parameters: I2cDeviceParameters) -> None:
        """Configures the device for I2C communications.

        Args:
            parameters (I2cDeviceParameters):
                A `I2cDeviceParameters` object used to configure the device for I2C communications.
        """
        self.devices_handler.set_input_output_voltage_level(voltage_level=parameters.voltage_level)
        self.devices_handler.enable_pullup_resistors = (
            Ni845xPullupStatus.PULLUP_ENABLE
            if parameters.enable_i2c_pullup_resistor
            else Ni845xPullupStatus.PULLUP_DISABLE
        )

    def configure_i2c_communication(self, parameters: I2cCommunicationParameters) -> None:
        """Configures the I2C communication.

        Args:
            parameters (I2cCommunicationParameters):
                A `I2cCommunicationParameters` object used to configure I2C communications.
        """
        self.devices_handler.configuration.address = parameters.device_address
        self.devices_handler.configuration.addressing_type = parameters.addressing_type
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.ack_poll_timeout_milliseconds = (
            parameters.ack_poll_timeout_milliseconds
        )

    def write_data(self, parameters: I2cWriteParameters) -> None:
        """Reads data bytes from an I2C device.

        Args:
            parameters (I2cWriteParameters):
                A `I2cWriteParameters` object used
                to perform read operations on I2C device.
        """
        pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=parameters.memory_address_parameters.memory_address,
            number_of_bytes_to_write=len(parameters.data_to_be_written),
            number_of_bytes_per_page=parameters.number_of_bytes_per_page,
        )

        for page_characteristics in pages_characteristics:
            # Compute the address of the page as a data bytes collection.
            address_parameters = MemoryAddressParameters(
                memory_address=page_characteristics.data_memory_address,
                address_type=parameters.memory_address_parameters.address_type,
                address_endianness=parameters.memory_address_parameters.address_endianness,
            )

            data_to_be_written = create_command_for_i2c_communications(
                address_parameters=address_parameters
            )

            # After the address where data will be stored, append the data bytes themselves.
            numpy.append(
                data_to_be_written,
                parameters.data_to_be_written[
                    page_characteristics.index_in_data_bytes_array : (
                        page_characteristics.index_in_data_bytes_array
                        + page_characteristics.number_of_bytes_in_page
                    )
                ],
            )

            # Write the data.
            self.devices_handler.write_data(data_bytes_to_be_written=data_to_be_written)

            time.sleep(seconds=parameters.delay_between_page_write_operations_milliseconds / 1000.0)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_data_types.py sha256=f7770daf5696f709e37e038e2877e4a39fbeec6e2839dbb68d99687822b517b9 bytes=9725 -->
## FILE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_data_types.py`
- sha256: `f7770daf5696f709e37e038e2877e4a39fbeec6e2839dbb68d99687822b517b9`
- bytes: 9725

````python
""" I2C communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.i2c_communications.i2c_read_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cWriteParameters(PCBATestToolkitData):
    """Defines the parameters used to perform write operations on I2C device."""

    def __init__(
        self,
        number_of_bytes_per_page: int,
        delay_between_page_write_operations_milliseconds: int,
        data_to_be_written: numpy.ndarray[numpy.ubyte],
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `I2cWriteParameters` with specific values.

        Args:
            number_of_bytes_per_page (int):
                The number of bytes per page.
            delay_between_page_write_operations_milliseconds (int):
                The delay time between two page write operations, in ms.
            data_to_be_written (numpy.ndarray[numpy.ubyte]):
                A numpy array containing the data to be written to I2C device.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            TypeError:
                raised if the type of numpy array is not `numpy.ubyte`.
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `delay_between_page_write_operations_milliseconds` is negative,
                `memory_address_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(number_of_bytes_per_page, nameof(number_of_bytes_per_page))
        Guard.is_greater_than_or_equal_to_zero(
            delay_between_page_write_operations_milliseconds,
            nameof(delay_between_page_write_operations_milliseconds),
        )
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))
        Guard.is_not_none(data_to_be_written, nameof(data_to_be_written))
        Guard.is_not_empty(data_to_be_written, nameof(data_to_be_written))

        if data_to_be_written.dtype != numpy.ubyte:
            raise TypeError(
                PCBATTLibraryExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
            )

        self._number_of_bytes_per_page = number_of_bytes_per_page
        self._delay_between_page_write_operations_milliseconds = (
            delay_between_page_write_operations_milliseconds
        )
        self._data_to_be_written = data_to_be_written
        self._memory_address_parameters = memory_address_parameters

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `I2cWriteParameters` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return (
                self._number_of_bytes_per_page == value_to_compare._number_of_bytes_per_page
                or self._delay_between_page_write_operations_milliseconds
                == value_to_compare._delay_between_page_write_operations_milliseconds
                or numpy.array_equal(self._data_to_be_written, value_to_compare._data_to_be_written)
                or self._memory_address_parameters == value_to_compare._memory_address_parameters
            )

        return False

    @property
    def number_of_bytes_per_page(self) -> int:
        """Gets the number of bytes per page."""
        return self._number_of_bytes_per_page

    @property
    def delay_between_page_write_operations_milliseconds(self) -> int:
        """Gets the delay time between two page write operations, in ms."""
        return self._delay_between_page_write_operations_milliseconds

    @property
    def data_to_be_written(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the numpy array containing the data to be written to I2C device."""
        return self._data_to_be_written

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        return self._memory_address_parameters


class I2cWriteCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the I2C Write communication."""

    def __init__(
        self,
        device_parameters: I2cDeviceParameters,
        communication_parameters: I2cCommunicationParameters,
        write_parameters: I2cWriteParameters,
    ):
        """Initializes an instance of
        `I2cWriteCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2cCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            write_parameters (I2cWriteParameters):
                An instance of `I2cWriteParameters` that represents
                the parameters used for settings of I2C Write communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `write_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(write_parameters, nameof(write_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._write_parameters = write_parameters

    @property
    def device_parameters(self) -> I2cDeviceParameters:
        """Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (370 > 100 characters) (auto-generated noqa)
        return self._device_parameters

    @property
    def communication_parameters(self) -> I2cCommunicationParameters:
        """Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def write_parameters(self) -> I2cWriteParameters:
        """Gets an instance of `I2cWriteParameters` that represents
        the parameters used for settings of I2C Write communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
        return self._write_parameters
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/__init__.py sha256=d61308d43bd374c3997330ffc4ddaa97509f648d9254701b98d1fe4a1083d150 bytes=243 -->
## FILE: src/nipcbatt/pcbatt_library/communications/serial_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/serial_communications/__init__.py`
- sha256: `d61308d43bd374c3997330ffc4ddaa97509f648d9254701b98d1fe4a1083d150`
- bytes: 243

````python
"""Provides nipcbatt library serial communication modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication.py sha256=af1758f79133519dbf00abadf078340786bb48706a809be02a3255eebe39e18f bytes=3729 -->
## FILE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication.py`
- sha256: `af1758f79133519dbf00abadf078340786bb48706a809be02a3255eebe39e18f`
- bytes: 3729

````python
""" Defines class used for serial communication on serial devices. """

from nipcbatt.pcbatt_library.communications.serial_communications.serial_data_types import (
    SerialCommunicationConfiguration,
    SerialCommunicationData,
    SerialCommunicationParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingVisa


class SerialCommunication(BuildingBlockUsingVisa):
    """Defines a way that allows you to perform operations on serial device."""

    def initialize(self, serial_device_name: str):
        """Initializes the communication with the specific serial device.

        Args:
            serial_device_name (str): The name of a serial device.
        """
        if self.is_serial_device_handler_initialized:
            return

        self.open_serial_device(serial_device_name=serial_device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_serial_device_handler_initialized:
            return

        self.close_serial_device()

    def configure_then_send_command_and_receive_response(
        self, configuration: SerialCommunicationConfiguration
    ) -> SerialCommunicationData:
        """Configures then performs serial communication operations
        according to specific configuration parameters.

        Args:
            configuration (SerialCommunicationConfiguration):
                An instance of `SerialCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SerialCommunicationData:
                An instance of `SerialCommunicationData`
                encapsulating the received response.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Configuration of the device for serial communications.
        self.configure_serial_communication(parameters=configuration.communication_parameters)

        # Send command and receive response.
        return SerialCommunicationData(
            received_response=self.send_command_and_receive_response(configuration.command_to_send)
        )

    def configure_serial_communication(self, parameters: SerialCommunicationParameters):
        """Configures the serial communication.

        Args:
            parameters (SerialCommunicationParameters):
                A `SerialCommunicationParameters` object used
                to configure the device for serial communications.
        """
        self.serial_device_handler.baud_rate = parameters.data_rate_bauds
        self.serial_device_handler.data_bits = parameters.number_of_bits_in_data_frame

        self.serial_device_handler.query_delay = (
            parameters.delay_before_receive_response_milliseconds / 1000.0
        )

        self.serial_device_handler.parity = parameters.parity
        self.serial_device_handler.stop_bits = parameters.stop_bits
        self.serial_device_handler.flow_control = parameters.flow_control

    def send_command_and_receive_response(self, command_to_send: str) -> str:
        """Sends a command to a serial device and receive response from it.

        Args:
            command_to_send (str): The string representing the command to send.

        Returns:
            str: The response sent back by the serial communication.
        """
        return self.serial_device_handler.query(message=command_to_send)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication_constants.py sha256=26c11b4d1bc491fe45cd2a68a5a1cb1c2bc0f21cb50ff36f8cca9ea21d79a8af bytes=462 -->
## FILE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication_constants.py`
- sha256: `26c11b4d1bc491fe45cd2a68a5a1cb1c2bc0f21cb50ff36f8cca9ea21d79a8af`
- bytes: 462

````python
""" Constants data types for serial communications."""

import dataclasses

import pyvisa.constants


@dataclasses.dataclass
class ConstantsForSerialCommunication:
    """Constants used for serial communication."""

    DEFAULT_PARITY = pyvisa.constants.Parity.none
    DEFAULT_DELAY_BEFORE_RECEIVE_RESPONSE_MILLISECONDS = 500
    DEFAULT_STOP_BITS = pyvisa.constants.StopBits.one
    DEFAULT_FLOW_CONTROL_MODE = pyvisa.constants.ControlFlow.none
````
