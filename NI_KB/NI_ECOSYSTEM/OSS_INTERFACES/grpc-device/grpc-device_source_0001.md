# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=.clang-format sha256=2f9b8e596b0d9f66e0b928a460ebb7c0a8715ab72513422a8f4d9318a653f147 bytes=248 -->
## FILE: .clang-format

- repository: `ni/grpc-device`
- source_path: `.clang-format`
- sha256: `2f9b8e596b0d9f66e0b928a460ebb7c0a8715ab72513422a8f4d9318a653f147`
- bytes: 248

````text
---
BasedOnStyle: Google
---
Language: Cpp
ColumnLimit: 0
AlignAfterOpenBracket: AlwaysBreak
BreakBeforeBraces: Stroustrup
DerivePointerAlignment: false
IndentPPDirectives: BeforeHash
PointerAlignment: Left
AlignOperands: DontAlign
---
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/azure-pipelines/azure-pipelines.yml sha256=2af6ee1dae447c59cfcf67f943cd1c0d8c4e4eb6ca0a7e13fd589c676b70e246 bytes=108 -->
## FILE: .github/azure-pipelines/azure-pipelines.yml

- repository: `ni/grpc-device`
- source_path: `.github/azure-pipelines/azure-pipelines.yml`
- sha256: `2af6ee1dae447c59cfcf67f943cd1c0d8c4e4eb6ca0a7e13fd589c676b70e246`
- bytes: 108

````yaml
pr:
  - main

pool:
  name: cjohnsto

steps:
  - checkout: none
  - script: echo "Hello, world!!!"
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/copilot-instructions.md sha256=24f27d245de07538230eec464a5497a0eb5c352366e66889228307e16c544497 bytes=2829 -->
## FILE: .github/copilot-instructions.md

- repository: `ni/grpc-device`
- source_path: `.github/copilot-instructions.md`
- sha256: `24f27d245de07538230eec464a5497a0eb5c352366e66889228307e16c544497`
- bytes: 2829

````markdown
# Copilot Instructions for grpc-device Repository

## Building the Project

This repository requires specific environment setup before building. **Always** follow these guidelines when running build commands.

### Prerequisites

1. **Visual Studio Build Tools**: Ensure Visual Studio Build Tools are installed with C++ development components
2. **CMake**: Make sure CMake is available in the system PATH

### Critical: Preferred Build Method

**Always use the copilot-build.ps1 script for all builds:**

```powershell
# Default Debug build
.\utils\copilot-build.ps1

# Release build
.\utils\copilot-build.ps1 --config Release

# RelWithDebInfo build
.\utils\copilot-build.ps1 --config RelWithDebInfo

# Other cmake arguments
.\utils\copilot-build.ps1 --target clean --config Debug
.\utils\copilot-build.ps1 --parallel 4 --config Release
```

This script automatically handles the Visual Studio environment setup and is much more Copilot-friendly since it avoids complex command chaining that often requires manual approval.
Any parameters you pass into this script will be passed along into the cmake command. However, you should prefer to do simple full builds instead of targeted builds. Ninja is good
at doing incremental builds quickly.

### Testing

To run tests after building:

```powershell
# Run unit tests
.\build\Debug\UnitTestsRunner.exe

# Run system tests
.\build\Debug\SystemTestsRunner.exe
```

Or use the build script to build first, then run tests:

```powershell
.\utils\copilot-build.ps1 --config Debug
.\build\Debug\UnitTestsRunner.exe
.\build\Debug\SystemTestsRunner.exe
```

### Clean Build

**WARNING: Never perform a clean build without asking the user first.** Full builds take a very long time and are almost never needed. Most issues can be resolved with a regular incremental build.

If a clean build is specifically requested:

```powershell
# Using the build script (preferred)
.\utils\copilot-build.ps1 --target clean --config Debug

# Or manually
cmd.exe /c "call `"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat`" && cd /d `"%cd%\build`" && cmake --build . --target clean && cmake --build . --config Debug"
```

## Repository Structure Notes

- Source code is in the `source/` directory
- Examples are in the `examples/` directory  
- Generated code is in the `generated/` directory
- Build artifacts go in the `build/` directory
- The project uses gRPC and Protocol Buffers for communication

## Python Components

This repository also contains Python components. When working with Python:

1. Use the virtual environment created by the build system
2. Install dependencies from `python_build_requirements.txt`
3. Python examples are located in the `examples/` directory
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/ISSUE_TEMPLATE/bug_report.md sha256=6881e8f930a856280f801891ea34a6ace1308f073f298f630d82b22adc3619d9 bytes=1535 -->
## FILE: .github/ISSUE_TEMPLATE/bug_report.md

- repository: `ni/grpc-device`
- source_path: `.github/ISSUE_TEMPLATE/bug_report.md`
- sha256: `6881e8f930a856280f801891ea34a6ace1308f073f298f630d82b22adc3619d9`
- bytes: 1535

````markdown
---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: 'bug,triage'
assignees: ''
---

# Bug Report

<!--- Provide a general summary of the issue here -->

> [!NOTE]
> grpc-device provides .proto files and a server to support calling NI driver APIs over gRPC. Can you reproduce your problem by calling the driver API directly?

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

* Operating system and version: [e.g. Windows 11 24H2, Ubuntu Linux 24.04, NI Linux RT 2024 Q4]
* All NI driver versions: [e.g. NI-DAQmx 2024 Q4, NI-FGEN 2024 Q4]
* `grpc-device` version: [e.g. 2.11.0]
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/pull_request_template.md sha256=38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7 bytes=363 -->
## FILE: .github/pull_request_template.md

- repository: `ni/grpc-device`
- source_path: `.github/pull_request_template.md`
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

<!--NI_OSS_SOURCE repo=grpc-device path=.github/update-linux-rt-template.md sha256=d7665daaef4a93c08858c89b4a35f305eb4448602734007ec688b04db04eb8ab bytes=414 -->
## FILE: .github/update-linux-rt-template.md

- repository: `ni/grpc-device`
- source_path: `.github/update-linux-rt-template.md`
- sha256: `d7665daaef4a93c08858c89b4a35f305eb4448602734007ec688b04db04eb8ab`
- bytes: 414

````markdown
---
title: Update Linux RT Feed to point to new release {{ env.NEW_RELEASE }}
---

Linux RT needs to be updated to point to the new grpc-device release.

Update the following lines in `recipes-ni/ni-grpc-device/ni-grpc-device_git.bb` in [ni/meta-nilrt](https://github.com/ni/meta-nilrt)
- PV = "{{ env.NEW_RELEASE }}"
- SRCBRANCH = "{{ env.GITHUB_BRANCH }}"
- SRCREV_grpc-device = "{{ env.GITHUB_SHA }}"
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/build_cmake.yml sha256=3d63742851e1bca497f3ed867f215bdbab1659ad305fb4e2cb8f1f3c76a99a99 bytes=8225 -->
## FILE: .github/workflows/build_cmake.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/build_cmake.yml`
- sha256: `3d63742851e1bca497f3ed867f215bdbab1659ad305fb4e2cb8f1f3c76a99a99`
- bytes: 8225

````yaml
name: Desktop OS Builds

on:
  workflow_call:
  workflow_dispatch:

jobs:
  build:
    name: ${{ matrix.config.name }}
    runs-on: ${{ matrix.config.os }}
    strategy:
      fail-fast: false
      matrix:
        config:
        - {
            name: "Windows Build", artifact: "Windows.tar.xz",
            os: windows-2022,
            cc: "cl", cxx: "cl",
            cmake_generator: '-G "Ninja Multi-Config"',
            build_type: RelWithDebInfo
          }
        - {
            name: "Ubuntu Build", artifact: "Linux.tar.xz",
            os: ubuntu-22.04,
            cc: "gcc-13", cxx: "g++-13",
            glibc_version: "2_38",
            cmake_generator: '-G "Ninja"',
            build_type: RelWithDebInfo
          }

    steps:
    - name: Free Disk Space (Ubuntu)
      if: ${{ runner.os == 'Linux' }}
      uses: insightsengineering/disk-space-reclaimer@v1
      with:
          tools-cache: false

    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install build dependencies (Ubuntu)
      if: ${{ runner.os == 'Linux' }}
      run: |
        sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
        sudo apt-get update
        sudo apt-get install -y gcc-13 g++-13

    - name: Install nasm
      if: ${{ runner.os == 'Windows' }}
      run: choco install nasm

    - name: Update Submodules
      run: git submodule update --init --recursive --depth=1

    - name: Setup Ninja
      uses: seanmiddleditch/gha-setup-ninja@v5
      with:
          version: 1.12.1

    - name: Setup MSVC for compilation
      if: ${{ runner.os == 'Windows' }}
      uses: ilammy/msvc-dev-cmd@v1
      with:
          arch: x64
          sdk: 10.0.22621.0
          vsversion: "2022"

    - name: Setup cmake
      uses: jwlawson/actions-setup-cmake@v2
      with:
          cmake-version: '3.18.x'

    - name: Get number of CPU cores
      uses: SimenB/github-actions-cpu-cores@v2
      id: cpu-cores

    - name: Configure
      env:
          CC: ${{ matrix.config.cc }}
          CXX: ${{ matrix.config.cxx }}
      run: >
        cmake
        -S .
        -B build
        -D CMAKE_BUILD_TYPE=${{ matrix.config.build_type }}
        ${{ matrix.config.cmake_generator }}

    # It is preferable to do a clean build to ensure all object files are
    # deleted and then rebuilt from scratch, which can help resolve
    # inconsistencies and errors.
    - name: Build
      run: >
        cmake
        --build build
        --clean-first
        --config ${{ matrix.config.build_type }}
        -j ${{ steps.cpu-cores.outputs.count }}

    # The generated source in git must match the output of workflow builds.
    # If this step fails, something is changing during build. Either:
    # 1. Fix non-deterministic codegen, OR
    # 2. Build locally to ensure generated files are up-to-date.
    - name: Check for files dirtied by codegen
      run: git diff --exit-code

    - name: Run Tests
      working-directory: build
      run: >
        ctest
        -j ${{ steps.cpu-cores.outputs.count }}
        -C ${{ matrix.config.build_type }}
        -E System
        --output-on-failure

    - name: Tar Linux Server Binaries
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Linux') }}
      run: >-
        tar -cvzf ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64.tar.gz
        -C ${GITHUB_WORKSPACE}/build
        ni_grpc_device_server
        server_config.json
        server_capabilities.json
        server_nitlsconfig.json
        ni-grpc-device.conf.yml
        ni-grpc-device.caps.yml
        -C ${GITHUB_WORKSPACE}
        LICENSE
        ThirdPartyNotices.txt

    - name: Tar Linux Server Debug Symbols
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Linux') }}
      run: >-
        tar -cvzf ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64-debug-symbols.tar.gz
        -C ${GITHUB_WORKSPACE}/build
        ni_grpc_device_server.dbg
        -C ${GITHUB_WORKSPACE}
        LICENSE
        ThirdPartyNotices.txt

    - name: Upload Linux Server Binaries Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Linux') }}
      with:
        name: ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64
        path: ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64.tar.gz
        retention-days: 5

    - name: Upload Linux Server Debug Symbols Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Linux') }}
      with:
        name: ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64-debug-symbols
        path: ni-grpc-device-server-linux-glibc${{ matrix.config.glibc_version }}-x64-debug-symbols.tar.gz
        retention-days: 5

    - name: Tar Linux Test Binaries
      if: ${{ runner.os == 'Linux' }}
      run: >-
        tar -cvzf ni-grpc-device-tests-linux-glibc${{ matrix.config.glibc_version }}-x64.tar.gz
        -C ${GITHUB_WORKSPACE}/build
        certs/
        IntegrationTestsRunner
        libTestApi.so
        SystemTestsRunner
        test_localhost_config.json
        test_mutual_tls_config.json
        UnitTestsRunner
        -C ${GITHUB_WORKSPACE}
        LICENSE
        ThirdPartyNotices.txt

    - name: Upload Linux Test Binaries Artifact
      uses: actions/upload-artifact@v4
      if: ${{ runner.os == 'Linux' }}
      with:
        name: ni-grpc-device-tests-linux-glibc${{ matrix.config.glibc_version }}-x64
        path: ni-grpc-device-tests-linux-glibc${{ matrix.config.glibc_version }}-x64.tar.gz
        retention-days: 5

    - name: Upload Windows Server Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Windows') }}
      with:
        name: ni-grpc-device-server-windows-x64
        path: |
          LICENSE
          ThirdPartyNotices.txt
          build/RelWithDebInfo/ni_grpc_device_server.exe
          build/RelWithDebInfo/server_config.json
          build/RelWithDebInfo/server_capabilities.json
          build/RelWithDebInfo/server_nitlsconfig.json
          build/RelWithDebInfo/ni-grpc-device.conf.yml
          build/RelWithDebInfo/ni-grpc-device.caps.yml
        retention-days: 5

    - name: Upload Windows Test Binaries Artifact
      uses: actions/upload-artifact@v4
      if: ${{ runner.os == 'Windows' }}
      with:
        name: ni-grpc-device-tests-windows-x64
        path: |
          build/RelWithDebInfo/certs/
          build/RelWithDebInfo/IntegrationTestsRunner.exe
          build/RelWithDebInfo/TestApi.dll
          build/RelWithDebInfo/SystemTestsRunner.exe
          build/RelWithDebInfo/LTE20MHz Waveform (Two Subframes).json
          build/RelWithDebInfo/NR_FR2_UL_SISO_CC-1_BW-50MHz_SCS-120kHz.json
          build/RelWithDebInfo/WLAN_80211n_20MHz_1Seg_2Chain_MIMO.json
          build/RelWithDebInfo/test_create_capture_waveform_serial/
          build/RelWithDebInfo/test_localhost_config.json
          build/RelWithDebInfo/test_mutual_tls_config.json
          build/RelWithDebInfo/UnitTestsRunner.exe
          LICENSE
          ThirdPartyNotices.txt
        retention-days: 5

    - name: Upload Windows Server Debug Symbols Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Windows') }}
      with:
        name: ni-grpc-device-server-windows-x64-debug-symbols
        path: |
          build/RelWithDebInfo/ni_grpc_device_server.pdb
        retention-days: 5
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/build_nilrt.yml sha256=1bda600663ae92413f77ac3f02f005382056b9003834b1279ffaed211a8e9d4f bytes=4986 -->
## FILE: .github/workflows/build_nilrt.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/build_nilrt.yml`
- sha256: `1bda600663ae92413f77ac3f02f005382056b9003834b1279ffaed211a8e9d4f`
- bytes: 4986

````yaml
name: NI Linux Real-Time Build

on:
  workflow_call:
  workflow_dispatch:

env:
  BUILD_TYPE: Release

jobs:
  build-nilrt:
    name: NILRT Cross Compile
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Setup Ninja
      uses: seanmiddleditch/gha-setup-ninja@v5
      with:
          version: 1.12.1

    - name: Setup cmake
      uses: jwlawson/actions-setup-cmake@v2
      with:
          cmake-version: '3.18.x'

    - name: Get number of CPU cores
      uses: SimenB/github-actions-cpu-cores@v2
      id: cpu-cores

    # The URL used to download this toolchain may change in the future as
    # improvements to hosting and exports of the NILRT toolchain are made.
    - name: Install NI Linux RT CC Toolchain
      run: |
        wget -nv https://download.ni.com/support/softlib/labview/labview_rt/2023Q4/LinuxToolchains/linux/oecore-x86_64-core2-64-toolchain-10.0.sh
        sudo chmod a+x ./oecore-x86_64-core2-64-toolchain-10.0.sh
        sudo ./oecore-x86_64-core2-64-toolchain-10.0.sh -y -d $GITHUB_WORKSPACE/nilrt-toolchain/
        echo "$GITHUB_WORKSPACE/nilrt-toolchain/sysroots/x86_64-nilrtsdk-linux/usr/bin/x86_64-nilrt-linux" >> $GITHUB_PATH

    - name: Update Submodules
      id: submodules
      run: |
        git submodule update --init --recursive
        echo "grpc-commit=$(git rev-parse --short @:./third_party/grpc)" >> $GITHUB_OUTPUT

    - name: Cache Host OS gRPC Support
      uses: actions/cache@v4
      id: hostgrpccache
      env:
        cache-name: hostgrpccache
      with:
        path: third_party/grpc/build/
        key: ${{ github.repository }}-${{ runner.os }}-${{ env.cache-name }}-${{ steps.submodules.outputs.grpc-commit }}

    - name: Configure Host OS gRPC Support
      if: steps.hostgrpccache.outputs.cache-hit != 'true'
      run: >
        cmake
        -S $GITHUB_WORKSPACE/third_party/grpc/
        -B $GITHUB_WORKSPACE/third_party/grpc/build
        -D CMAKE_BUILD_TYPE=$BUILD_TYPE
        -D gRPC_INSTALL=ON
        -D gRPC_BUILD_TESTS=OFF
        -G "Ninja"

    - name: Build Host OS gRPC Support
      if: steps.hostgrpccache.outputs.cache-hit != 'true'
      run: >
        cmake
        --build $GITHUB_WORKSPACE/third_party/grpc/build
        -j ${{ steps.cpu-cores.outputs.count }}

    - name: Install Host OS gRPC Support
      run: sudo cmake --install $GITHUB_WORKSPACE/third_party/grpc/build

    - name: Configure Cross Compile
      run: >
        cmake
        -S .
        -B build
        -D CMAKE_BUILD_TYPE=$BUILD_TYPE
        -D USE_NILRT_LEGACY_TOOLCHAIN=on
        -G "Ninja"

    - name: Cross Compile
      run: >
        cmake
        --build build
        -j ${{ steps.cpu-cores.outputs.count }}

    # The generated source in git must match the output of workflow builds.
    # If this step fails, something is changing during build. Either:
    # 1. Fix non-deterministic codegen, OR
    # 2. Build locally to ensure generated files are up-to-date.
    - name: Check for files dirtied by codegen
      run: git diff --exit-code

    - name: Tar Server Build Files
      if: ${{ github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases') }}
      run: >-
        tar -cvzf ni-grpc-device-server-ni-linux-rt-x64.tar.gz
        -C $GITHUB_WORKSPACE/build
        ni_grpc_device_server
        server_config.json
        server_capabilities.json
        server_nitlsconfig.json
        ni-grpc-device.conf.yml
        ni-grpc-device.caps.yml
        -C $GITHUB_WORKSPACE
        LICENSE
        ThirdPartyNotices.txt

    - name: Upload Server Artifact
      uses: actions/upload-artifact@v4
      if: ${{ github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases') }}
      with:
        name: ni-grpc-device-server-ni-linux-rt-x64
        path: ni-grpc-device-server-ni-linux-rt-x64.tar.gz
        retention-days: 5

    - name: Tar Test Build Files
      if: ${{ github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases') }}
      run: >-
        tar -cvzf ni-grpc-device-tests-ni-linux-rt-x64.tar.gz
        -C $GITHUB_WORKSPACE/build
        certs/
        IntegrationTestsRunner
        libTestApi.so
        SystemTestsRunner
        test_localhost_config.json
        test_mutual_tls_config.json
        UnitTestsRunner
        -C $GITHUB_WORKSPACE
        LICENSE
        ThirdPartyNotices.txt

    - name: Upload Tests Artifact
      uses: actions/upload-artifact@v4
      if: ${{ github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases') }}
      with:
        name: ni-grpc-device-tests-ni-linux-rt-x64
        path: ni-grpc-device-tests-ni-linux-rt-x64.tar.gz
        retention-days: 5
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/ci.yml sha256=1ed32eb1447dcfeef69986eb0ec1e71ed3ece5f5c1197268e16e5613490488ac bytes=1000 -->
## FILE: .github/workflows/ci.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/ci.yml`
- sha256: `1ed32eb1447dcfeef69986eb0ec1e71ed3ece5f5c1197268e16e5613490488ac`
- bytes: 1000

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
  validate_imported_protos:
    uses: ./.github/workflows/validate_imported_protos.yml
  validate_python:
    uses: ./.github/workflows/validate_python.yml
  build_desktop:
    needs:
      - validate_imported_protos
      - validate_python
    uses: ./.github/workflows/build_cmake.yml
  build_nilrt:
    needs:
      - validate_imported_protos
      - validate_python
    uses: ./.github/workflows/build_nilrt.yml
  run_win_system_tests:
    needs: build_desktop
    uses: ./.github/workflows/run_win_system_tests.yml
  create_client_artifacts:
    uses: ./.github/workflows/create_client_artifacts.yml
  create_release:
    if: ${{ startsWith(github.ref, 'refs/heads/releases') && github.event_name == 'push' }}
    needs:
      - build_desktop
      - build_nilrt
      - create_client_artifacts
    uses: ./.github/workflows/create_release.yml
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/create_client_artifacts.yml sha256=abbe6d2bfb98330877392807d68f3e6e57fb2b9137e955cff002a5ca0a573316 bytes=2477 -->
## FILE: .github/workflows/create_client_artifacts.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/create_client_artifacts.yml`
- sha256: `abbe6d2bfb98330877392807d68f3e6e57fb2b9137e955cff002a5ca0a573316`
- bytes: 2477

````yaml
name: Create Client Artifacts

on:
  workflow_call:
  workflow_dispatch:

jobs:
  build:
    name: ${{ matrix.config.name }}
    runs-on: ${{ matrix.config.os }}
    strategy:
      fail-fast: false
      matrix:
        config:
        - {
            name: "Windows Artifacts", artifact: "Windows.tar.xz",
            os: windows-latest,
          }
        - {
            name: "Linux Artifacts", artifact: "Linux.tar.xz",
            os: ubuntu-22.04,
          }

    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Initialize ni-apis submodule
      run: |
        git submodule update --init third_party/ni-apis
        
    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install build dependencies
      run: python -m pip install -r python_build_requirements.txt

    - name: Stage Client Files
      run: |
        python source/codegen/stage_client_files.py -o ${{ runner.temp }}/staging/

    - name: Stage Restricted Client Files
      run: |
        python source/codegen/stage_client_files.py --ignore-release-readiness -o ${{ runner.temp }}/staging_restricted/

    - name: Tar Linux Client Files
      if: ${{ (runner.os == 'Linux') }}
      run: |
        tar -cvzf ni-grpc-device-client.tar.gz -C ${{ runner.temp }}/staging/ .

    - name: Upload Linux Client Files Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Linux') }}
      with:
        name: ni-grpc-device-client-Linux
        path: ni-grpc-device-client.tar.gz
        retention-days: 5

    - name: Upload Windows Client Files Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Windows') }}
      with:
        name: ni-grpc-device-client
        path: |
          ${{ runner.temp }}/staging
        retention-days: 5

    - name: Upload Windows Restricted Client Files Artifact
      uses: actions/upload-artifact@v4
      if: ${{ (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/releases')) && (runner.os == 'Windows') }}
      with:
        name: ni-grpc-device-client-restricted
        path: |
          ${{ runner.temp }}/staging_restricted
        retention-days: 5
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/create_release.yml sha256=b9df45ac21d23c06fe5cce591b300698eb4992bc8e5f5129dd2c10f9bda9455c bytes=3674 -->
## FILE: .github/workflows/create_release.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/create_release.yml`
- sha256: `b9df45ac21d23c06fe5cce591b300698eb4992bc8e5f5129dd2c10f9bda9455c`
- bytes: 3674

````yaml
name: Create Release

on:
  workflow_call:
  workflow_dispatch:

jobs:
  create_release:
    name: Create Release
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-client
        path: downloads/ni-grpc-device-client

    - uses: vimtor/action-zip@v1
      with:
        files: downloads/ni-grpc-device-client
        dest: downloads/artifacts/ni-grpc-device-client.zip

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-client-Linux
        path: downloads/artifacts

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-server-linux-glibc2_38-x64
        path: downloads/artifacts

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-server-linux-glibc2_38-x64-debug-symbols
        path: downloads/artifacts

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-server-ni-linux-rt-x64
        path: downloads/artifacts

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-server-windows-x64
        path: downloads/ni-grpc-device-server-windows-x64

    - uses: vimtor/action-zip@v1
      with:
        files: downloads/ni-grpc-device-server-windows-x64
        dest: downloads/artifacts/ni-grpc-device-server-windows-x64.zip

    - uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-server-windows-x64-debug-symbols
        path: downloads/ni-grpc-device-server-windows-x64-debug-symbols

    - uses: vimtor/action-zip@v1
      with:
        files: downloads/ni-grpc-device-server-windows-x64-debug-symbols
        dest: downloads/artifacts/ni-grpc-device-server-windows-x64-debug-symbols.zip

    - name: "Get previous tag"
      id: previoustag
      run: >-
        echo "tag=$(
          git tag --list --sort=-version:refname | grep '^\(v[0-9]\+.[0-9]\+.[0-9]\+\)$' | head -1
        )" >> $GITHUB_OUTPUT

    - name: "Get next version"
      id: semvers
      uses: "WyriHaximus/github-action-next-semvers@v1"
      with:
        version: ${{ steps.previoustag.outputs.tag}}

    - name: "Create Draft Release"
      uses: ncipollo/release-action@v1
      with:
        artifacts: "downloads/artifacts/*"
        commit: ${{ github.sha }}
        draft: true
        generateReleaseNotes: true
        body: |
          Updates since release ${{ steps.previoustag.outputs.tag }}:
          * List any bug fixes or general updates for this release vs. the previous one.

          Breaking Changes:
          * List out any breaking changes introduced since the last release.

          This release contains the ni-grpc-device-server application for Windows, Linux Desktop, and Linux RT.

          It also contains client bundles that contain the proto files needed to build a gRPC client as well as several example clients.

          Documentation on using this release can be found in our [README](https://github.com/ni/grpc-device#downloading-a-release) and [wiki](https://github.com/ni/grpc-device/wiki).

          ⚠ Use the below generated release notes to populate the "Updates" and "Breaking Changes" sections above. Any PRs with a breaking change should be tagged with the 'breaking-change' label. ⚠
        name: "NI gRPC Device Server ${{ steps.semvers.outputs.patch }}"
        tag: ${{ steps.semvers.outputs.v_patch }}
        token: ${{ secrets.GITHUB_TOKEN }}
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/pr.yml sha256=cc899f129f79adda243a1a2c860881566709a89ad530e9061fbe1aa294949a2b bytes=323 -->
## FILE: .github/workflows/pr.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/pr.yml`
- sha256: `cc899f129f79adda243a1a2c860881566709a89ad530e9061fbe1aa294949a2b`
- bytes: 323

````yaml
name: PR
on:
  pull_request:
    types: [opened, synchronize, reopened]
  workflow_call:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  run_ci:
    name: Run CI
    uses: ./.github/workflows/ci.yml
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/run_ubuntu_system_tests.yml sha256=dc3496d904ad513d8ee427eb91af16b1183a729890666e5e150b867f26877267 bytes=743 -->
## FILE: .github/workflows/run_ubuntu_system_tests.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/run_ubuntu_system_tests.yml`
- sha256: `dc3496d904ad513d8ee427eb91af16b1183a729890666e5e150b867f26877267`
- bytes: 743

````yaml
name: Run Ubuntu System Tests

on:
  workflow_call:
  workflow_dispatch:

jobs:
  run-tests:
    name: Run Tests
    runs-on:
    - self-hosted
    - linux
    - x64
    - grpcbot-ubuntu2

    steps:
    - name: Download Tests Artifact
      uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-tests-linux-glibc2_38-x64

    - run: ls -R

    - name: Untar Test Build Files
      run: >-
        tar -xvzf ni-grpc-device-tests-linux-glibc2_38-x64.tar.gz

    - name: Run System Tests
      run: ./SystemTestsRunner --gtest_filter=-NiRFSA*:NiRFSG*:NiDCPower*CalSelfCalibrate*:NiXnetLINDriverApiTests.ConvertFramesToFromSignalsFromExample_CompareFrames_ValuesMatch
      timeout-minutes: 27
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/run_win_system_tests.yml sha256=6b298639b457e70fde2146089528c65f54d930ef4232b2aae4fdb8d98a472deb bytes=571 -->
## FILE: .github/workflows/run_win_system_tests.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/run_win_system_tests.yml`
- sha256: `6b298639b457e70fde2146089528c65f54d930ef4232b2aae4fdb8d98a472deb`
- bytes: 571

````yaml
name: Run Windows System Tests

on:
  workflow_call:
  workflow_dispatch:

jobs:
  run-tests:
    name: Run Tests
    runs-on:
    - self-hosted
    - windows
    - x64
    - grpcbot-win-10

    steps:
    - name: Download Tests Artifact
      uses: actions/download-artifact@v4
      with:
        name: ni-grpc-device-tests-windows-x64

    - run: ls -R
      working-directory: ./build/RelWithDebInfo

    - name: Run System Tests
      run: .\SystemTestsRunner.exe
      working-directory: ./build/RelWithDebInfo
      timeout-minutes: 50
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/sync_github_issues_to_azdo.yml sha256=eba484b33332d79fb0b67ab48a4bc2d0d7a49f691acf000dbd187addee687e38 bytes=1762 -->
## FILE: .github/workflows/sync_github_issues_to_azdo.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/sync_github_issues_to_azdo.yml`
- sha256: `eba484b33332d79fb0b67ab48a4bc2d0d7a49f691acf000dbd187addee687e38`
- bytes: 1762

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
          ado_area_path: "DevCentral\\Product RnD\\Platform HW and SW\\Core SW and Drivers\\Platform HW and Drivers\\Drivers\\Platform Drivers Ownership NIC"
          ado_wit: "${{ steps.choose_work_item_type.outputs.work_item_type }}"
          ado_new_state: "New"
          ado_active_state: "Active"
          ado_close_state: "Closed"
          ado_bypassrules: true
          log_level: 100
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/trigger_azdo_ci.yml sha256=c575c9b7d1fc3d1fb4dbd7b4272de7a5f3308232717a311c4ab10cc21e331c7e bytes=1335 -->
## FILE: .github/workflows/trigger_azdo_ci.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/trigger_azdo_ci.yml`
- sha256: `c575c9b7d1fc3d1fb4dbd7b4272de7a5f3308232717a311c4ab10cc21e331c7e`
- bytes: 1335

````yaml
name: Trigger AzDO CIs

on:
  workflow_run:
    workflows: [CI]
    types:
      - completed
    branches:
      - main
      - 'releases/**'
  workflow_dispatch:

jobs:
  trigger_azdo_ci:
    name: Trigger Main CI
    runs-on: windows-latest
    steps:
    - name: Trigger Main CI 
      uses: Azure/pipelines@v1.2
      if: ${{ github.repository == 'ni/grpc-device' && github.event.workflow_run.head_branch == 'main' }}
      with:
        azure-devops-project-url: 'https://dev.azure.com/ni/DevCentral'
        azure-pipeline-name: 'ni-central-grpc_device'
        azure-devops-token: ${{ secrets.AZDO_PIPELINE_TRIGGERS }}
        azure-pipeline-variables: '{"BRANCH": "main", "EXPORT_NAME": "ni-grpc-device", "PHASE": "d"}'
                                  
    - name: Trigger Release CI 
      uses: Azure/pipelines@v1.2
      if: ${{ github.repository == 'ni/grpc-device' && startsWith(github.event.workflow_run.head_branch, 'releases') }}
      with:
        azure-devops-project-url: 'https://dev.azure.com/ni/DevCentral'
        azure-pipeline-name: 'ni-central-grpc_device'
        azure-devops-token: ${{ secrets.AZDO_PIPELINE_TRIGGERS }}
        azure-pipeline-variables: '{"BRANCH": "releases", "EXPORT_NAME": "ni-grpc-device", "PHASE": "f", "RELEASE_BRANCH_OPTION": "--release-branch"}'
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/validate_imported_protos.yml sha256=50a588e26738513ee19234ba65b907056404ac5b4b07dad268aa461323ea0eca bytes=642 -->
## FILE: .github/workflows/validate_imported_protos.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/validate_imported_protos.yml`
- sha256: `50a588e26738513ee19234ba65b907056404ac5b4b07dad268aa461323ea0eca`
- bytes: 642

````yaml
name: Validate Imported Proto Files

on:
  workflow_call:
  workflow_dispatch:

jobs:
  validate:
    name: Validate Imported Proto Files
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install build dependencies
      run: python -m pip install -r python_build_requirements.txt

    - name: Validate imported proto files against generated
      run: |
        python source/codegen/validate_imported_protos.py -i source/codegen/metadata -g generated
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/validate_linux_rt.yml sha256=06216b07a8e17ef8f385a5690cf0fbc22df53fe2031f68da8c9c0f737df75c0d bytes=2602 -->
## FILE: .github/workflows/validate_linux_rt.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/validate_linux_rt.yml`
- sha256: `06216b07a8e17ef8f385a5690cf0fbc22df53fe2031f68da8c9c0f737df75c0d`
- bytes: 2602

````yaml
name: Validate Linux RT Feed Package Version
on:
  push:
    tags:
      - 'v[0-9]+.[0-9]+.[0-9]+'

jobs:
  validate_linux_rt:
    name: Validate Linux RT Feed Package Version
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Get the latest tag
      id: latesttag
      run: >-
        echo "tag=$(
          git tag --list --sort=-version:refname | grep '^\(v[0-9]\+.[0-9]\+.[0-9]\+\)$' | head -1
        )" >> $GITHUB_OUTPUT

    - name: Get latest tag without leading v
      id: latesttagwithoutv
      run: >-
        echo "tag=$(
          git tag --list --sort=-version:refname | grep '^\(v[0-9]\+.[0-9]\+.[0-9]\+\)$' | head -1 | cut -c2-
        )" >> $GITHUB_OUTPUT

    - name: Get the second latest tag
      id: secondlatesttag
      run: >-
        echo "tag=$(
          git tag --list --sort=-version:refname | grep '^\(v[0-9]\+.[0-9]\+.[0-9]\+\)$' | sed '1d' | head -1
        )" >> $GITHUB_OUTPUT

    - name: Fail if new tag is not latest tag
      if: ${{ github.ref_name != steps.latesttag.outputs.tag}}
      uses: actions/github-script@v6
      with:
        script: |
            core.setFailed(`The new release (${{ github.ref_name }}) is not a patch or update to the latest release (${{ steps.latesttag.outputs.tag }}). Checking if the Linux RT Feed needs updating doesn't make sense on a patch to a previous release.`)

    - name: Install build dependencies
      run: python -m pip install -r python_build_requirements.txt

    - name: Check if Linux RT needs updating
      run: |
        git diff --name-only ${{ steps.secondlatesttag.outputs.tag}}..${{ steps.latesttag.outputs.tag }} | python source/codegen/validate_linux_rt.py source/codegen/metadata

    - name: Get branch name
      id: getbranchname
      run: |
        raw=$(git branch -r --contains ${{ github.ref }})
        branch_sans_origin=${raw/origin\/}
        echo branch=$branch_sans_origin >> $GITHUB_OUTPUT

    - name: Create GitHub Issue
      if: ${{ env.SHOULD_UPDATE_LINUX_RT == 'True'}}
      uses: JasonEtco/create-an-issue@v2
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        NEW_RELEASE: ${{ steps.latesttagwithoutv.outputs.tag }}
        GITHUB_SHA: ${{ github.sha}}
        GITHUB_BRANCH: ${{ steps.getbranchname.outputs.branch }}
      with:
        filename: .github/update-linux-rt-template.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/validate_mi_mutation.yml sha256=3bc6bce19ac0b145ffd9b386b4c3919701c5de5fef3f43da1845e6f22bbda65b bytes=707 -->
## FILE: .github/workflows/validate_mi_mutation.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/validate_mi_mutation.yml`
- sha256: `3bc6bce19ac0b145ffd9b386b4c3919701c5de5fef3f43da1845e6f22bbda65b`
- bytes: 707

````yaml
name: Validate mi driver mutations

on:
  workflow_call:
  workflow_dispatch:

jobs:
  validate:
    name: Validate mi driver mutations
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install build dependencies
      run: python -m pip install -r python_build_requirements.txt

    - name: Validate mi driver metadata mutations 
      run: |
        python source/codegen/format_mi_metadata.py source/codegen/metadata
    
    - name: Check for files dirtied by codegen
      run: |
        git diff --exit-code
````

<!--NI_OSS_SOURCE repo=grpc-device path=.github/workflows/validate_python.yml sha256=7f784d146826ebfd3533061126d032ccabc200c069c5ff489eb01c4df1586bc0 bytes=979 -->
## FILE: .github/workflows/validate_python.yml

- repository: `ni/grpc-device`
- source_path: `.github/workflows/validate_python.yml`
- sha256: `7f784d146826ebfd3533061126d032ccabc200c069c5ff489eb01c4df1586bc0`
- bytes: 979

````yaml
name: Validate Python Code

on:
  workflow_call:
  workflow_dispatch:

jobs:
  validate:
    name: Validate Python Code
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Initialize ni-apis submodule
      run: |
        git submodule update --init third_party/ni-apis

    - name: Setup python3
      uses: actions/setup-python@v5
      with:
        python-version: '3.11.x'

    - name: Install build dependencies
      run: python -m pip install -r python_build_requirements.txt

    - name: Validate python style with ni-python-styleguide
      run: |
        ni-python-styleguide lint source/codegen/*.py examples

    - name: Install poetry for validate_examples.py
      uses: abatilo/actions-poetry@v3
      with:
        poetry-version: 1.8.2

    - name: Validate examples (except aio)
      run: |
        python source/codegen/validate_examples.py --exclude="-aio\.py$"
````

<!--NI_OSS_SOURCE repo=grpc-device path=.gitignore sha256=249554209a1b1a0ab05316200f2a9871bc80e5c6a96d600644a28924b554f0ca bytes=278 -->
## FILE: .gitignore

- repository: `ni/grpc-device`
- source_path: `.gitignore`
- sha256: `249554209a1b1a0ab05316200f2a9871bc80e5c6a96d600644a28924b554f0ca`
- bytes: 278

````text
/bin/
/build/
/third_party/
CMakeLists.txt.user
CMakeCache.txt
CMakeFiles
CMakeScripts
Testing
Makefile
cmake_install.cmake
install_manifest.txt
compile_commands.json
CTestTestfile.cmake
_deps
gens
*.orig
.vs
.vscode
__pycache__/
.venv
/generated/version.h
````

<!--NI_OSS_SOURCE repo=grpc-device path=.gitmodules sha256=1a396acb198521a1a3afa8e4d0afa5ef52691917c9ef351a95cc37473a703123 bytes=652 -->
## FILE: .gitmodules

- repository: `ni/grpc-device`
- source_path: `.gitmodules`
- sha256: `1a396acb198521a1a3afa8e4d0afa5ef52691917c9ef351a95cc37473a703123`
- bytes: 652

````text
[submodule "third_party/grpc"]
	path = third_party/grpc
	url = https://github.com/grpc/grpc.git
[submodule "third_party/json"]
	path = third_party/json
	url = https://github.com/nlohmann/json.git
[submodule "third_party/utfcpp"]
	path = third_party/utfcpp
	url = https://github.com/nemtrif/utfcpp
[submodule "third_party/grpc-sideband"]
	path = third_party/grpc-sideband
	url = https://github.com/ni/grpc-sideband.git
[submodule "third_party/googletest"]
	path = third_party/googletest
	url = https://github.com/google/googletest.git
[submodule "third_party/ni-apis"]
	path = third_party/ni-apis
	url = https://github.com/ni/ni-apis
	
````

<!--NI_OSS_SOURCE repo=grpc-device path=cmake/CreateVirtualEnvironment.cmake sha256=8e2ee5a9484dac6ff713691dc791de30e86b4c59d79a9d182d499d2e97b6763a bytes=3005 -->
## FILE: cmake/CreateVirtualEnvironment.cmake

- repository: `ni/grpc-device`
- source_path: `cmake/CreateVirtualEnvironment.cmake`
- sha256: `8e2ee5a9484dac6ff713691dc791de30e86b4c59d79a9d182d499d2e97b6763a`
- bytes: 3005

````text
#[=============================================================================[
------------------------
CreateVirtualEnvironment
------------------------
Function that creates a virtual Python environment with specific requirements.
Derived from https://schemingdeveloper.com/2020/07/02/how-to-create-a-new-python-virtual-environment-in-cmake/

Author: zoodinger
License: WTFPL

Required Arguments:
    TARGET (string):
        Target name of the virtual environment that can be used by other
        targets as a dependency.

Optional Arguments:
    REQUIREMENTS_TXT (string):
        Path to requirements.txt list to install with pip
    ENV_NAME (string)
        The name of the virtual environment. Unless otherwise specified, this
        is the same as TARGET.


Optional Output Arguments:
    OUT_PYTHON_EXE (output variable):
        Stores the path to the python executable of the virtual environment.

#]=============================================================================]

function(CreateVirtualEnvironment TARGET)
    set(KEYWORD_ARGS 
        REQUIREMENTS_TXT 
        ENV_NAME
        OUT_PYTHON_EXE
    )

    cmake_parse_arguments(ARG "" "${KEYWORD_ARGS}" "" ${ARGN})

    if (NOT ARG_ENV_NAME)
        set(ARG_ENV_NAME ${TARGET})
    endif ()

    if (NOT ARG_REQUIREMENTS_TXT)
        set(ARG_REQUIREMENTS_TXT "requirements.txt")
    endif()

    find_package(Python3 REQUIRED COMPONENTS Interpreter)

    set(VENV ${CMAKE_BINARY_DIR}/${ARG_ENV_NAME})

    if (WIN32)
        set(PYTHON_VENV_EXE ${VENV}/Scripts/python.exe)
    else ()
        set(PYTHON_VENV_EXE ${VENV}/bin/python)
    endif ()

    set(ENVIRONMENT_CREATED ${VENV}/environment.txt)
    add_custom_command(
        OUTPUT 
            ${ENVIRONMENT_CREATED}
        # Use --without-pip + ensurepip to create a venv with pip as separate steps.
        # Workaround for https://bugs.python.org/issue43749, which hopefully is fixed in cpython 3.11.
        # See also: https://github.com/actions/virtual-environments/issues/2690
        # The ensurepip in default venv creation uses the invoking python exe name. In some environments
        # this will be python3.exe instead of python.exe, which does not work in cpython venvs <=3.10.
        # This code will always use <venv>/Scripts/python.exe to call ensurepip.
        COMMAND 
            ${Python3_EXECUTABLE} -m venv --without-pip ${VENV}
        COMMAND
            ${PYTHON_VENV_EXE} -m ensurepip --upgrade --default-pip
        COMMAND
            ${PYTHON_VENV_EXE} -m pip install -r  ${ARG_REQUIREMENTS_TXT}
        COMMAND
            ${PYTHON_VENV_EXE} -m pip freeze > ${ENVIRONMENT_CREATED}
        DEPENDS 
            ${ARG_REQUIREMENTS_TXT}
        VERBATIM
    )

    add_custom_target(${TARGET} DEPENDS ${ENVIRONMENT_CREATED})

    if (ARG_OUT_PYTHON_EXE)
        set(${ARG_OUT_PYTHON_EXE} ${PYTHON_VENV_EXE} PARENT_SCOPE)
    endif ()

endfunction()
````

<!--NI_OSS_SOURCE repo=grpc-device path=cmake/nilrt-x86_64.cmake sha256=33b345c10ee8cbe18a9e34c9c1a03702671228b5806a0e10add31b4ba8c2715f bytes=1804 -->
## FILE: cmake/nilrt-x86_64.cmake

- repository: `ni/grpc-device`
- source_path: `cmake/nilrt-x86_64.cmake`
- sha256: `33b345c10ee8cbe18a9e34c9c1a03702671228b5806a0e10add31b4ba8c2715f`
- bytes: 1804

````text
#----------------------------------------------------------------------
# CMake toolchain file for cross-compiling for NI Linux Real-Time
#----------------------------------------------------------------------
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR x86_64)

#----------------------------------------------------------------------
# Path variables for toolchains
#----------------------------------------------------------------------
find_program(COMPILER_PATH x86_64-nilrt-linux-gcc)
get_filename_component(toolchain_path ${COMPILER_PATH}/../../../../.. REALPATH DIRECTORY)
set(include_path core2-64-nilrt-linux/usr/include/c++/6.3.0)

#----------------------------------------------------------------------
# Compilers
#----------------------------------------------------------------------
set(CMAKE_C_COMPILER x86_64-nilrt-linux-gcc)
set(CMAKE_CXX_COMPILER x86_64-nilrt-linux-g++)

#----------------------------------------------------------------------
# Default compiler flags
#----------------------------------------------------------------------
set(CMAKE_SYSROOT ${toolchain_path}/core2-64-nilrt-linux)
set(CMAKE_<LANG>_STANDARD_INCLUDE_DIRECTORIES ${toolchain_path}/${include_path} ${toolchain_path}/${include_path}/x86_64-nilrt-linux)
set(CMAKE_<LANG>_FLAGS "-Wall -fmessage-length=0")
set(CMAKE_<LANG>_FLAGS_DEBUG "-O0 -g3")
set(CMAKE_<LANG>_FLAGS_RELEASE "-O3")

#----------------------------------------------------------------------
# Define proper search behavior for cross compilation
#----------------------------------------------------------------------
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
````

<!--NI_OSS_SOURCE repo=grpc-device path=CMakeLists.txt sha256=8b33cde3adf17b273f663e0f1643313b7bc6e5c74cc3ce9119a59a2ebf58ad2a bytes=45359 -->
## FILE: CMakeLists.txt

- repository: `ni/grpc-device`
- source_path: `CMakeLists.txt`
- sha256: `8b33cde3adf17b273f663e0f1643313b7bc6e5c74cc3ce9119a59a2ebf58ad2a`
- bytes: 45359

````text
cmake_minimum_required(VERSION 3.18.0)

project(ni_grpc_device_server
  LANGUAGES C CXX
  VERSION 2.20.0)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# Workaround for: https://bugs.chromium.org/p/boringssl/issues/detail?id=423
if (CMAKE_SYSTEM_PROCESSOR STREQUAL "AMD64")
  set(CMAKE_SYSTEM_PROCESSOR "amd64")
endif()

if(MSVC)
  add_definitions(-D_WIN32_WINNT=0x600)
  add_definitions(-DNOMINMAX) # Disable ancient min and max macros in Windows.h
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /wd4267 /wd4244") # Disable possible loss of precision warnings
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /std:c17") # Needed for boringssl
endif()

# GCC-specific flags
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-var-tracking-assignments")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fno-var-tracking-assignments")
endif()

#----------------------------------------------------------------------
# Use C++17 (needed for shared_mutex support on Linux)
#----------------------------------------------------------------------
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Enforce consistent runtime library settings in case of MSVC
if (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
  if (POLICY CMP0091)
    cmake_policy(SET CMP0091 NEW)
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>" CACHE STRING "Use static runtime" FORCE)
    set(gRPC_MSVC_STATIC_RUNTIME ON CACHE BOOL "Use static runtime for gRPC" FORCE)
    set(libprotoc_MSVC_STATIC_RUNTIME ON CACHE BOOL "Use static runtime for libprotoc" FORCE)
    set(protobuf_MSVC_STATIC_RUNTIME ON CACHE BOOL "Use static runtime for protobuf" FORCE)
    set(ABSL_MSVC_STATIC_RUNTIME ON CACHE BOOL "Use static runtime for Abseil" FORCE)
    message("Setting policy CMP0091 and runtime library")
  else()
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MD")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")
    message("Using dynamic runtime library")
  endif()
endif()

#---
# Configuration options
#---
option(USE_NILRT_LEGACY_TOOLCHAIN "Enable to use tools and libraries from a NILRT compile toolchain." OFF)
option(USE_PYTHON_VIRTUALENV "Enable to use the automatically-generated python venv, local to this project source." ON)
option(USE_SUBMODULE_LIBS "Enable to link against the submodule libraries, rather than their native-OS equivalents." ON)
option(INCLUDE_SIDEBAND_RDMA "Include support for RDMA sideband transfers." OFF)
option(SIDEBAND_STATIC "Link grpc-sideband statically to current application." ON)

#----------------------------------------------------------------------
# Setup build dependencies, according to the toolchain options.
#----------------------------------------------------------------------
if(USE_SUBMODULE_LIBS)
  # The archetypical WIN32 build case
  # protobuf_INSTALL must be turned OFF whenever building it as a cmake subdir.
  set(protobuf_INSTALL OFF)

  add_subdirectory(third_party/grpc ${CMAKE_CURRENT_BINARY_DIR}/grpc)
  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
  add_subdirectory(third_party/googletest ${CMAKE_CURRENT_BINARY_DIR}/googletest EXCLUDE_FROM_ALL)
  add_subdirectory(third_party/json ${CMAKE_CURRENT_BINARY_DIR}/json)
  add_subdirectory(third_party/utfcpp ${CMAKE_CURRENT_BINARY_DIR}/utfcpp)
  add_subdirectory(third_party/grpc-sideband ${CMAKE_CURRENT_BINARY_DIR}/grpc-sideband)

  set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)
  set(_REFLECTION grpc++_reflection)
  set(_GRPC grpc)
  set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:grpc_cpp_plugin>)
  set(_GRPC_GRPCPP grpc++)
  set(_PROTOBUF_LIBPROTOBUF libprotobuf)
  set(_UTF8CPP utf8cpp)
  set(_GRPC_SIDEBAND ni_grpc_sideband)
else()
  find_program(_PROTOBUF_PROTOC protoc)
  find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin)
  find_library(_GRPC_GPR gpr)
  find_library(_ABSEIL_SYNC absl_synchronization REQUIRED)

  if(USE_NILRT_LEGACY_TOOLCHAIN)
    # The archetypical NILRT SDK toolchain build case
    add_subdirectory(third_party/grpc ${CMAKE_CURRENT_BINARY_DIR}/grpc EXCLUDE_FROM_ALL)
    set(_REFLECTION grpc++_reflection)
    set(_GRPC_GRPCPP grpc++)
    set(_PROTOBUF_LIBPROTOBUF libprotobuf)
  else()
    # The archetypical linux build case (including OpenEmbedded)
    find_library(_GRPC_GRPCPP grpc++)
    find_library(_PROTOBUF_LIBPROTOBUF protobuf)
    find_library(_REFLECTION grpc++_reflection)
    find_library(_GRPC_SIDEBAND ni_grpc_sideband REQUIRED)

    find_package(gRPC REQUIRED)
    find_package(GTest REQUIRED)
    find_package(nlohmann_json REQUIRED)
    find_package(utf8cpp REQUIRED)

    set(_GRPC gRPC::grpc)
    set(_UTF8CPP utf8cpp::utf8cpp)
  endif()
endif()

# Python3 Virtual Environment
if(USE_PYTHON_VIRTUALENV)
  include(CreateVirtualEnvironment)
  CreateVirtualEnvironment(virtual_environment
    REQUIREMENTS_TXT
      ${CMAKE_SOURCE_DIR}/python_build_requirements.txt
    ENV_NAME
      venv
    OUT_PYTHON_EXE
      PYTHON_EXE
  )
else()
  find_package(Python3 REQUIRED)
  set(PYTHON_EXE ${Python3_EXECUTABLE})
endif()

enable_testing()

#----------------------------------------------------------------------
# Include generated *.pb.h files
#----------------------------------------------------------------------
set(proto_srcs_dir "${CMAKE_CURRENT_BINARY_DIR}/proto")
file(MAKE_DIRECTORY ${proto_srcs_dir})
include_directories(
  "${proto_srcs_dir}"
  "./generated"
  "./imports/include"
  "./source"
)

if(USE_SUBMODULE_LIBS)
  include_directories(
    "./third_party/grpc-sideband/src"
    "./third_party/grpc-sideband/moniker_src"
  )
else()
  find_path(GRPC_SIDEBAND_INCLUDE_DIR ni-grpc-sideband REQUIRED)
  include_directories("${GRPC_SIDEBAND_INCLUDE_DIR}/ni-grpc-sideband")
endif()

if(WIN32)
  link_directories("./imports/lib/win64")
endif()

#----------------------------------------------------------------------
# Get list of NI Driver APIs and directories to generate from
#----------------------------------------------------------------------
set(metadata_dir ${CMAKE_SOURCE_DIR}/source/codegen/metadata)
set(service_output_dir ${CMAKE_SOURCE_DIR}/generated)
set(codegen_dir ${CMAKE_SOURCE_DIR}/source/codegen)
set(custom_dir ${CMAKE_SOURCE_DIR}/source/custom)
set(nidrivers "nidaqmx" "nidcpower" "nidigitalpattern" "nidmm" "nidmm_restricted" "nifake" "nifake_extension" "nifake_non_ivi" "nifgen" "nifpga" "nimxlcterminaladaptor_restricted" "nirfmxbluetooth" "nirfmxcdma2k" "nirfmxgsm" "nirfmxinstr" "nirfmxinstr_restricted" "nirfmxlte" "nirfmxnr" "nirfmxpulse" "nirfmxspecan" "nirfmxspecan_restricted" "nirfmxtdscdma" "nirfmxwcdma" "nirfmxdemod" "nirfmxwlan" "nirfmxvna" "nirfmxbluetoothgen" "nirfmxwlangen" "nirfmxwlan_restricted" "nirfsa" "nirfsg" "nirfsg_restricted" "niscope" "niscope_restricted" "niswitch" "nisync" "nitclk" "nixnet" "nixnetsocket" "visa")

#----------------------------------------------------------------------
# Create NI Driver APIs proto and server files
#----------------------------------------------------------------------
set(codegen_scripts
  "${codegen_dir}/client_helpers.py"
  "${codegen_dir}/common_helpers.py"
  "${codegen_dir}/generate_service.py"
  "${codegen_dir}/generate_shared_service_files.py"
  "${codegen_dir}/service_helpers.py"
  "${codegen_dir}/proto_helpers.py"
  "${codegen_dir}/metadata_mutation.py"
  "${codegen_dir}/metadata_validation.py"
  "${codegen_dir}/template_helpers.py"
  "${codegen_dir}/templates/client.cpp.mako"
  "${codegen_dir}/templates/client.h.mako"
  "${codegen_dir}/templates/client_helpers.mako"
  "${codegen_dir}/templates/library_interface.h.mako"
  "${codegen_dir}/templates/library.cpp.mako"
  "${codegen_dir}/templates/library.h.mako"
  "${codegen_dir}/templates/mock_library.h.mako"
  "${codegen_dir}/templates/proto.mako"
  "${codegen_dir}/templates/proto_helpers.mako"
  "${codegen_dir}/templates/register_all_services.h.mako"
  "${codegen_dir}/templates/register_all_services.cpp.mako"
  "${codegen_dir}/templates/service.cpp.mako"
  "${codegen_dir}/templates/service_helpers.mako"
  "${codegen_dir}/templates/service.h.mako"
  "${codegen_dir}/templates/service_registrar.h.mako"
  "${codegen_dir}/templates/service_registrar.cpp.mako"
  )

# Populated in the api loop below.
set(nidriver_service_library_hdrs "")
set(nidriver_service_srcs "")
set(nidriver_client_srcs "")

# We'll codegen all drivers, but some are not included in the server build.
set(nidrivers_to_build ${nidrivers})
# Fake drivers are not in the server and are added manually to the UnitTestRunner build.
list(FILTER nidrivers_to_build EXCLUDE REGEX "^nifake.*")
if (NOT WIN32)
  # None of the RFmx drivers support Linux and building against the headers fails.
  # Exclude them on Linux.
  list(FILTER nidrivers_to_build EXCLUDE REGEX "^nirfmx.*")
endif()

set(all_codegen_dependencies "")

if(USE_PYTHON_VIRTUALENV)
  list(APPEND all_codegen_dependencies virtual_environment)
endif()

foreach(api ${nidrivers})
  set(codegen_dependencies
    "${metadata_dir}/${api}/attributes.py"
    "${metadata_dir}/${api}/attributes_addon.py"
    "${metadata_dir}/${api}/config.py"
    "${metadata_dir}/${api}/config_addon.py"
    "${metadata_dir}/${api}/enums.py"
    "${metadata_dir}/${api}/enums_addon.py"
    "${metadata_dir}/${api}/functions.py"
    "${metadata_dir}/${api}/functions_addon.py"
    "${metadata_dir}/${api}/__init__.py")
  if (EXISTS "${metadata_dir}/${api}/custom_proto.mako")
    set(codegen_dependencies ${codegen_dependencies} "${metadata_dir}/${api}/custom_proto.mako")
  endif()
  set(all_codegen_dependencies
    ${all_codegen_dependencies}
    ${codegen_dependencies}
  )

  set(output_files
    ${service_output_dir}/${api}/${api}_client.cpp
    ${service_output_dir}/${api}/${api}_client.h
    ${service_output_dir}/${api}/${api}_compilation_test.cpp
    ${service_output_dir}/${api}/${api}_library_interface.h
    ${service_output_dir}/${api}/${api}_library.cpp
    ${service_output_dir}/${api}/${api}_library.h
    ${service_output_dir}/${api}/${api}_mock_library.h
    ${service_output_dir}/${api}/${api}.proto
    ${service_output_dir}/${api}/${api}_service.cpp
    ${service_output_dir}/${api}/${api}_service.h
    ${service_output_dir}/${api}/${api}_service_registrar.cpp
    ${service_output_dir}/${api}/${api}_service_registrar.h
  )
  set(nidriver_service_library_hdrs
    ${nidriver_service_library_hdrs}
    "${service_output_dir}/${api}/${api}_library.h"
    "${service_output_dir}/${api}/${api}_library_interface.h"
    "${service_output_dir}/${api}/${api}_mock_library.h")
  set(gen_command COMMAND ${PYTHON_EXE} ${codegen_dir}/generate_service.py ${metadata_dir}/${api}/ -o ${service_output_dir}/)
  if (api IN_LIST nidrivers_to_build)
    set(nidriver_service_srcs
      ${nidriver_service_srcs}
      "${service_output_dir}/${api}/${api}_service.cpp"
      "${service_output_dir}/${api}/${api}_service_registrar.cpp"
      "${service_output_dir}/${api}/${api}_library.cpp"
      "${custom_dir}/${api}_service.custom.cpp")
    set(nidriver_client_srcs
      ${nidriver_client_srcs}
      "${service_output_dir}/${api}/${api}_client.cpp")
  endif()
  set(proto_dependencies ${codegen_dependencies} ${codegen_scripts})
  if (USE_PYTHON_VIRTUALENV)
    list(APPEND proto_dependencies virtual_environment)
  endif()
  add_custom_command(OUTPUT ${output_files}
    ${gen_command}
    COMMENT "Generating proto file and service for ${api}"
    DEPENDS ${proto_dependencies})
  add_custom_target(generate_proto_and_service_target_for_${api}
    DEPENDS ${output_files})
endforeach()

add_custom_command(
  OUTPUT
    ${service_output_dir}/register_all_services.cpp
    ${service_output_dir}/register_all_services.h
  COMMAND
    ${PYTHON_EXE} ${codegen_dir}/generate_shared_service_files.py ${metadata_dir}/ -o ${service_output_dir}/
  COMMENT
    "Generating shared service files"
  DEPENDS
    ${all_codegen_dependencies}
    ${codegen_scripts}
)

set(nidriver_service_srcs
    ${nidriver_service_srcs}
    ${service_output_dir}/register_all_services.cpp
)

#----------------------------------------------------------------------
# Proto file
#----------------------------------------------------------------------
get_filename_component(session_proto "third_party/ni-apis/ni/grpcdevice/v1/session.proto" ABSOLUTE)
get_filename_component(session_utilities_proto "source/protobuf/session_utilities.proto" ABSOLUTE)
get_filename_component(nidevice_proto "imports/protobuf/nidevice.proto" ABSOLUTE)
get_filename_component(deviceid_restricted_proto "source/protobuf_restricted/deviceid_restricted.proto" ABSOLUTE)
get_filename_component(debugsessionproperties_restricted_proto "source/protobuf_restricted/debugsessionproperties_restricted.proto" ABSOLUTE)
get_filename_component(calibrationoperations_restricted_proto "source/protobuf_restricted/calibrationoperations_restricted.proto" ABSOLUTE)
get_filename_component(data_moniker_proto "imports/protobuf/data_moniker.proto" ABSOLUTE)
get_filename_component(precision_timestamp_proto "third_party/ni-apis/ni/protobuf/types/precision_timestamp.proto" ABSOLUTE)
get_filename_component(waveform_proto "third_party/ni-apis/ni/protobuf/types/waveform.proto" ABSOLUTE)
get_filename_component(session_proto_path "${session_proto}" PATH)

#----------------------------------------------------------------------
# Generate sources from proto files
# Usage: GenerateGrpcSources(PROTO <path> OUTPUT <path>...)
#----------------------------------------------------------------------
function(GenerateGrpcSources)
  set(oneValueArgs PROTO)
  set(multiValueArgs OUTPUT)
  cmake_parse_arguments(GENERATE_ARGS "" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})
  set(output_files "${GENERATE_ARGS_OUTPUT}")
  set(proto_file "${GENERATE_ARGS_PROTO}")
  if(USE_SUBMODULE_LIBS)
    set(protobuf_includes_arg
      -I ${CMAKE_SOURCE_DIR}/third_party/grpc/third_party/protobuf/src/)
  endif()
  list(APPEND protobuf_includes_arg
    -I ${CMAKE_SOURCE_DIR}/third_party/ni-apis/ni/grpcdevice/v1/ # for session.proto
    -I ${CMAKE_SOURCE_DIR}/third_party/ni-apis/)
  get_filename_component(proto_name "${proto_file}" NAME)
  get_filename_component(proto_path "${proto_file}" PATH)
  # Asssumption: all outputs are in the same directory: use the zero-th.
  list(GET output_files 0 proto_srcs)
  get_filename_component(proto_out_path "${proto_srcs}" PATH)
  string(FIND "${proto_name}" "nixnetsocket" generating_nixnetsocket)
  # If generating nixnetsocket on Windows apply the winsock2 compatibility fix after codegen.
  # Else do normal codegen.
  if(MSVC AND (NOT generating_nixnetsocket EQUAL -1))
    add_custom_command(
      OUTPUT ${output_files}
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out ${proto_out_path}
        --cpp_out ${proto_out_path}
        -I ${proto_path}
        ${protobuf_includes_arg}
        -I ${CMAKE_SOURCE_DIR}/imports/protobuf
        --plugin=protoc-gen-grpc=${_GRPC_CPP_PLUGIN_EXECUTABLE}
        ${proto_file}
      COMMAND ${CMAKE_COMMAND} -E echo \#include \"custom/xnetsocket_winsock2_compatibility.h\" > ${proto_srcs_dir}/nixnetsocket.pb.h.tmp
      COMMAND ${CMAKE_COMMAND} -E cat ${proto_srcs_dir}/nixnetsocket.pb.h >> ${proto_srcs_dir}/nixnetsocket.pb.h.tmp
      COMMAND ${CMAKE_COMMAND} -E cat ${proto_srcs_dir}/nixnetsocket.pb.h.tmp > ${proto_srcs_dir}/nixnetsocket.pb.h
      DEPENDS "${proto_file}" "${session_proto}"
      VERBATIM)
  else()
    add_custom_command(
      OUTPUT ${output_files}
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out ${proto_out_path}
        --cpp_out ${proto_out_path}
        -I ${proto_path}
        ${protobuf_includes_arg}
        -I ${CMAKE_SOURCE_DIR}/imports/protobuf
        --plugin=protoc-gen-grpc=${_GRPC_CPP_PLUGIN_EXECUTABLE}
        ${proto_file}
      DEPENDS "${proto_file}" "${session_proto}"
      VERBATIM)
  endif()
endfunction()

#----------------------------------------------------------------------
# Generate sources from ni-apis proto files
# Usage: GenerateNiApisProtoSources(PROTO_PATH <relative_path> OUTPUT_SRCS <var> OUTPUT_HDRS <var> [DEPENDS <dependency>...])
#----------------------------------------------------------------------
function(GenerateNiApisProtoSources)
  set(oneValueArgs PROTO_PATH OUTPUT_SRCS OUTPUT_HDRS)
  set(multiValueArgs DEPENDS)
  cmake_parse_arguments(GEN_ARGS "" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})
  
  set(proto_srcs "${proto_srcs_dir}/${GEN_ARGS_PROTO_PATH}.pb.cc")
  set(proto_hdrs "${proto_srcs_dir}/${GEN_ARGS_PROTO_PATH}.pb.h")
  
  add_custom_command(
    OUTPUT "${proto_srcs}" "${proto_hdrs}"
    COMMAND ${_PROTOBUF_PROTOC}
    ARGS --cpp_out ${proto_srcs_dir}
      -I ${CMAKE_SOURCE_DIR}/third_party/ni-apis/
      -I ${CMAKE_SOURCE_DIR}/third_party/grpc/third_party/protobuf/src/
      ${GEN_ARGS_PROTO_PATH}.proto
    DEPENDS "${CMAKE_SOURCE_DIR}/third_party/ni-apis/${GEN_ARGS_PROTO_PATH}.proto" ${GEN_ARGS_DEPENDS}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/third_party/ni-apis/
    VERBATIM
  )
  
  set(${GEN_ARGS_OUTPUT_SRCS} "${proto_srcs}" PARENT_SCOPE)
  set(${GEN_ARGS_OUTPUT_HDRS} "${proto_hdrs}" PARENT_SCOPE)
endfunction()

set(session_proto_srcs "${proto_srcs_dir}/session.pb.cc")
set(session_proto_hdrs "${proto_srcs_dir}/session.pb.h")
set(session_grpc_srcs "${proto_srcs_dir}/session.grpc.pb.cc")
set(session_grpc_hdrs "${proto_srcs_dir}/session.grpc.pb.h")
set(session_utilities_proto_srcs "${proto_srcs_dir}/session_utilities.pb.cc")
set(session_utilities_proto_hdrs "${proto_srcs_dir}/session_utilities.pb.h")
set(session_utilities_grpc_srcs "${proto_srcs_dir}/session_utilities.grpc.pb.cc")
set(session_utilities_grpc_hdrs "${proto_srcs_dir}/session_utilities.grpc.pb.h")
set(nidevice_proto_srcs "${proto_srcs_dir}/nidevice.pb.cc")
set(nidevice_proto_hdrs "${proto_srcs_dir}/nidevice.pb.h")
set(deviceid_restricted_proto_srcs "${proto_srcs_dir}/deviceid_restricted.pb.cc")
set(deviceid_restricted_proto_hdrs "${proto_srcs_dir}/deviceid_restricted.pb.h")
set(deviceid_restricted_grpc_srcs "${proto_srcs_dir}/deviceid_restricted.grpc.pb.cc")
set(deviceid_restricted_grpc_hdrs "${proto_srcs_dir}/deviceid_restricted.grpc.pb.h")
set(debugsessionproperties_restricted_proto_srcs "${proto_srcs_dir}/debugsessionproperties_restricted.pb.cc")
set(debugsessionproperties_restricted_proto_hdrs "${proto_srcs_dir}/debugsessionproperties_restricted.pb.h")
set(debugsessionproperties_restricted_grpc_srcs "${proto_srcs_dir}/debugsessionproperties_restricted.grpc.pb.cc")
set(debugsessionproperties_restricted_grpc_hdrs "${proto_srcs_dir}/debugsessionproperties_restricted.grpc.pb.h")
set(calibrationoperations_restricted_proto_srcs "${proto_srcs_dir}/calibrationoperations_restricted.pb.cc")
set(calibrationoperations_restricted_proto_hdrs "${proto_srcs_dir}/calibrationoperations_restricted.pb.h")
set(calibrationoperations_restricted_grpc_srcs "${proto_srcs_dir}/calibrationoperations_restricted.grpc.pb.cc")
set(calibrationoperations_restricted_grpc_hdrs "${proto_srcs_dir}/calibrationoperations_restricted.grpc.pb.h")
set(data_moniker_proto_srcs "${proto_srcs_dir}/data_moniker.pb.cc")
set(data_moniker_proto_hdrs "${proto_srcs_dir}/data_moniker.pb.h")
set(data_moniker_grpc_srcs "${proto_srcs_dir}/data_moniker.grpc.pb.cc")
set(data_moniker_grpc_hdrs "${proto_srcs_dir}/data_moniker.grpc.pb.h")
set(precision_timestamp_proto_srcs "${proto_srcs_dir}/ni/protobuf/types/precision_timestamp.pb.cc")
set(precision_timestamp_proto_hdrs "${proto_srcs_dir}/ni/protobuf/types/precision_timestamp.pb.h")
set(waveform_proto_srcs "${proto_srcs_dir}/ni/protobuf/types/waveform.pb.cc")
set(waveform_proto_hdrs "${proto_srcs_dir}/ni/protobuf/types/waveform.pb.h")

GenerateGrpcSources(
  PROTO
    ${session_proto}
  OUTPUT
    "${session_proto_srcs}"
    "${session_proto_hdrs}"
    "${session_grpc_srcs}"
    "${session_grpc_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${session_utilities_proto}
  OUTPUT
    "${session_utilities_proto_srcs}"
    "${session_utilities_proto_hdrs}"
    "${session_utilities_grpc_srcs}"
    "${session_utilities_grpc_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${nidevice_proto}
  OUTPUT
    "${nidevice_proto_srcs}"
    "${nidevice_proto_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${deviceid_restricted_proto}
  OUTPUT
    "${deviceid_restricted_proto_srcs}"
    "${deviceid_restricted_proto_hdrs}"
    "${deviceid_restricted_grpc_srcs}"
    "${deviceid_restricted_grpc_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${debugsessionproperties_restricted_proto}
  OUTPUT
    "${debugsessionproperties_restricted_proto_srcs}"
    "${debugsessionproperties_restricted_proto_hdrs}"
    "${debugsessionproperties_restricted_grpc_srcs}"
    "${debugsessionproperties_restricted_grpc_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${calibrationoperations_restricted_proto}
  OUTPUT
    "${calibrationoperations_restricted_proto_srcs}"
    "${calibrationoperations_restricted_proto_hdrs}"
    "${calibrationoperations_restricted_grpc_srcs}"
    "${calibrationoperations_restricted_grpc_hdrs}"
)

GenerateGrpcSources(
  PROTO
    ${data_moniker_proto}
  OUTPUT
    "${data_moniker_proto_srcs}"
    "${data_moniker_proto_hdrs}"
    "${data_moniker_grpc_srcs}"
    "${data_moniker_grpc_hdrs}"
)

GenerateNiApisProtoSources(
  PROTO_PATH "ni/protobuf/types/precision_timestamp"
  OUTPUT_SRCS precision_timestamp_proto_srcs
  OUTPUT_HDRS precision_timestamp_proto_hdrs
)

GenerateNiApisProtoSources(
  PROTO_PATH "ni/protobuf/types/waveform"
  OUTPUT_SRCS waveform_proto_srcs
  OUTPUT_HDRS waveform_proto_hdrs
  DEPENDS "${precision_timestamp_proto_hdrs}"
)

set(nidriver_service_library_hdrs
  ${nidriver_service_library_hdrs}
  "${session_proto_hdrs}"
  "${session_grpc_hdrs}"
  "${session_utilities_proto_hdrs}"
  "${session_utilities_grpc_hdrs}"
  "${nidevice_proto_hdrs}"
  "${deviceid_restricted_proto_hdrs}"
  "${deviceid_restricted_grpc_hdrs}"
  "${debugsessionproperties_restricted_proto_hdrs}"
  "${debugsessionproperties_restricted_grpc_hdrs}"
  "${calibrationoperations_restricted_proto_hdrs}"
  "${calibrationoperations_restricted_grpc_hdrs}"
  "${precision_timestamp_proto_hdrs}"
  "${waveform_proto_hdrs}"
)

foreach(api ${nidrivers})
  GenerateGrpcSources(
    PROTO
      ${service_output_dir}/${api}/${api}.proto
    OUTPUT
      "${proto_srcs_dir}/${api}.pb.cc"
      "${proto_srcs_dir}/${api}.pb.h"
      "${proto_srcs_dir}/${api}.grpc.pb.cc"
      "${proto_srcs_dir}/${api}.grpc.pb.h"
  )
  set(nidriver_service_library_hdrs
    ${nidriver_service_library_hdrs}
    "${proto_srcs_dir}/${api}.pb.h"
    "${proto_srcs_dir}/${api}.grpc.pb.h")
  if(api IN_LIST nidrivers_to_build)
    set(nidriver_service_srcs
      ${nidriver_service_srcs}
      "${proto_srcs_dir}/${api}.pb.cc"
      "${proto_srcs_dir}/${api}.grpc.pb.cc")
  endif()
endforeach()

add_executable(ni_grpc_device_server
   "imports/include/nierr_Status.cpp"
   "source/server/calibration_operations_restricted_service_registrar.cpp"
   "source/server/calibration_operations_restricted_service.cpp"
   "source/server/core_server.cpp"
   "source/server/core_services_registrar.cpp"
   "source/server/data_moniker_service.cpp"
   "source/server/debug_session_properties_restricted_service_registrar.cpp"
   "source/server/debug_session_properties_restricted_service.cpp"
   "source/server/device_enumerator.cpp"
   "source/server/feature_toggles.cpp"
   "source/server/logging.cpp"
   "source/server/tls_config_loader.cpp"
   "source/server/semaphore.cpp"
   "source/server/server_configuration_parser.cpp"
   "source/server/server_security_configuration.cpp"
   "source/server/session_repository.cpp"
   "source/server/session_utilities_service.cpp"
   "source/server/session_utilities_service_registrar.cpp"
   "source/server/shared_library.cpp"
   "source/server/software_enumerator.cpp"
   "source/server/syscfg_library.cpp"
   "source/server/syscfg_resource_accessor.cpp"
   "source/server/syscfg_session_handler.cpp"
   ${nidevice_proto_srcs}
   ${session_proto_srcs}
   ${session_grpc_srcs}
   ${session_utilities_proto_srcs}
   ${session_utilities_grpc_srcs}
   ${deviceid_restricted_proto_srcs}
   ${deviceid_restricted_grpc_srcs}
   ${debugsessionproperties_restricted_proto_srcs}
   ${debugsessionproperties_restricted_grpc_srcs}
   ${calibrationoperations_restricted_proto_srcs}
   ${calibrationoperations_restricted_grpc_srcs}
   ${data_moniker_proto_srcs}
   ${data_moniker_grpc_srcs}
   ${precision_timestamp_proto_srcs}
   ${waveform_proto_srcs}
   ${nidriver_service_srcs})

# Enable warnings only on source that we own, not generated code or dependencies
file(GLOB_RECURSE SOURCE_TO_ENABLE_WARNINGS "source/*.cpp")
if(WIN32)
  set_source_files_properties(
    ${SOURCE_TO_ENABLE_WARNINGS}
    APPEND
    PROPERTIES
    COMPILE_OPTIONS "/WX"
  )
else()
  set_source_files_properties(
    ${SOURCE_TO_ENABLE_WARNINGS}
    APPEND
    PROPERTIES
    COMPILE_OPTIONS "-Werror"
  )
endif()

if(WIN32)
  set(version_generated_dir "${CMAKE_CURRENT_BINARY_DIR}/version")
  file(MAKE_DIRECTORY ${version_generated_dir})

  # Generate version resource file for Windows
  configure_file(
    source/server/version.rc.in
    ${version_generated_dir}/version.rc
    @ONLY)

  target_sources(ni_grpc_device_server
    PRIVATE "${version_generated_dir}/version.rc"
  )
endif()

execute_process(
  COMMAND git rev-parse --abbrev-ref HEAD
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  OUTPUT_VARIABLE GIT_BRANCH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Generate version header file
# This file requires product name and version info that mako does not know, but CMake does
configure_file(
  source/server/version.h.in
  ${service_output_dir}/version.h
  @ONLY)

target_sources(ni_grpc_device_server
  PUBLIC "${service_output_dir}/version.h"
)


if(CMAKE_SYSTEM_NAME STREQUAL Linux)
  target_sources(ni_grpc_device_server
    PRIVATE "source/server/linux/syslog_logging.cpp"
    PRIVATE "source/server/linux/daemonize.cpp")
endif()
if(CMAKE_SYSTEM_NAME STREQUAL Windows)
  target_sources(ni_grpc_device_server
    PRIVATE "source/server/windows/console_ctrl_handler.cpp")
endif()

set(server_lib_deps
  ${_ABSEIL_SYNC}
  ${_GRPC_GPR}
  ${_GRPC_GRPCPP}
  ${_GRPC}
  ${_PROTOBUF_LIBPROTOBUF}
  ${_REFLECTION}
  ${_UTF8CPP}
  ${CMAKE_DL_LIBS}
  ${_GRPC_SIDEBAND}
  nlohmann_json::nlohmann_json
)

target_link_libraries(ni_grpc_device_server
  ${server_lib_deps}
)

set_target_properties(ni_grpc_device_server PROPERTIES BUILD_WITH_INSTALL_RPATH TRUE)

#----------------------------------------------------------------------
# Copy server_config.json to binary output directory
#----------------------------------------------------------------------
add_custom_command(
   TARGET ni_grpc_device_server POST_BUILD
   COMMAND  ${CMAKE_COMMAND} -E copy_if_different
            ${CMAKE_SOURCE_DIR}/source/config/localhost_config.json
            $<TARGET_FILE_DIR:ni_grpc_device_server>/server_config.json)

#----------------------------------------------------------------------
# Copy server_nitlsconfig.json to binary output directory
#----------------------------------------------------------------------
add_custom_command(
   TARGET ni_grpc_device_server POST_BUILD
   COMMAND  ${CMAKE_COMMAND} -E copy_if_different
            ${CMAKE_SOURCE_DIR}/source/config/server_nitlsconfig.json
            $<TARGET_FILE_DIR:ni_grpc_device_server>/server_nitlsconfig.json)

#----------------------------------------------------------------------
# Copy ni-grpc-device.conf.yml to binary output directory
#----------------------------------------------------------------------
add_custom_command(
   TARGET ni_grpc_device_server POST_BUILD
   COMMAND  ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_SOURCE_DIR}/source/config/ni-grpc-device.server.conf.yml
            $<TARGET_FILE_DIR:ni_grpc_device_server>/ni-grpc-device.conf.yml)

#----------------------------------------------------------------------
# Copy ni-grpc-device.caps.yml to binary output directory
#----------------------------------------------------------------------
add_custom_command(
   TARGET ni_grpc_device_server POST_BUILD
   COMMAND  ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_SOURCE_DIR}/source/config/ni-grpc-device.server.caps.yml
            $<TARGET_FILE_DIR:ni_grpc_device_server>/ni-grpc-device.caps.yml)

#----------------------------------------------------------------------
# Generate server_capabilities.json to binary output directory
#----------------------------------------------------------------------
add_custom_command(
   TARGET ni_grpc_device_server POST_BUILD
   COMMAND  ${PYTHON_EXE} ${codegen_dir}/generate_server_capabilities.py ${metadata_dir}/
            -o $<TARGET_FILE_DIR:ni_grpc_device_server>/)

#----------------------------------------------------------------------
# Split binary into release and debug symbols for Linux/GCC
#----------------------------------------------------------------------
if(CMAKE_SYSTEM_NAME STREQUAL Linux)
  add_custom_command(
     TARGET ni_grpc_device_server POST_BUILD
     COMMAND  ${CMAKE_OBJCOPY} ARGS --only-keep-debug $<TARGET_FILE:ni_grpc_device_server>
              $<TARGET_FILE:ni_grpc_device_server>.dbg
     COMMAND  ${CMAKE_OBJCOPY} ARGS --strip-debug $<TARGET_FILE:ni_grpc_device_server>
     COMMAND  ${CMAKE_OBJCOPY} ARGS --add-gnu-debuglink=$<TARGET_FILE:ni_grpc_device_server>.dbg
              $<TARGET_FILE:ni_grpc_device_server>
     DEPENDS  ni_grpc_device_server)
endif()

# Link test executable against gtest
add_executable(IntegrationTestsRunner
    "imports/include/nierr_Status.cpp"
    "source/tests/utilities/run_all_tests.cpp"
    "source/tests/integration/ni_fake_service_tests_endtoend.cpp"
    "source/tests/integration/ni_fake_non_ivi_service_tests_endtoend.cpp"
    "source/tests/integration/session_utilities_service_tests.cpp"
    "source/tests/integration/session_utilities_service_tests_endtoend.cpp"
    "source/tests/integration/visa_resource_manager_tests.cpp"
    "source/tests/integration/ni_fake_daqmx_streaming_tests.cpp"
    "source/tests/integration/ni_fake_fpga_streaming_tests.cpp"
    "source/server/calibration_operations_restricted_service_registrar.cpp"
    "source/server/calibration_operations_restricted_service.cpp"
    "source/server/core_services_registrar.cpp"
    "source/server/data_moniker_service.cpp"
    "source/server/debug_session_properties_restricted_service_registrar.cpp"
    "source/server/debug_session_properties_restricted_service.cpp"
    "source/server/device_enumerator.cpp"
    "source/server/feature_toggles.cpp"
    "source/server/semaphore.cpp"
    "source/server/session_repository.cpp"
    "source/server/session_utilities_service.cpp"
    "source/server/session_utilities_service_registrar.cpp"
    "source/server/shared_library.cpp"
    "source/server/software_enumerator.cpp"
    "source/server/syscfg_library.cpp"
    "source/server/syscfg_resource_accessor.cpp"
    "source/server/syscfg_session_handler.cpp"
    ${nidevice_proto_srcs}
    ${session_proto_srcs}
    ${session_grpc_srcs}
    ${session_utilities_proto_srcs}
    ${session_utilities_grpc_srcs}
    ${deviceid_restricted_proto_srcs}
    ${deviceid_restricted_grpc_srcs}
    ${debugsessionproperties_restricted_proto_srcs}
    ${debugsessionproperties_restricted_grpc_srcs}
    ${calibrationoperations_restricted_proto_srcs}
    ${calibrationoperations_restricted_grpc_srcs}
    ${data_moniker_proto_srcs}
    ${data_moniker_grpc_srcs}
    ${precision_timestamp_proto_srcs}
    ${waveform_proto_srcs}
    ${nidriver_service_srcs}
    "${proto_srcs_dir}/nifake.pb.cc"
    "${proto_srcs_dir}/nifake.grpc.pb.cc"
    "${proto_srcs_dir}/nifake_non_ivi.pb.cc"
    "${proto_srcs_dir}/nifake_non_ivi.grpc.pb.cc"
    "${service_output_dir}/nidaqmx/nidaqmx_client.cpp"
    "${service_output_dir}/nifake/nifake_client.cpp"
    "${service_output_dir}/nifake/nifake_service.cpp"
    "${service_output_dir}/nifpga/nifpga_client.cpp"
    "${service_output_dir}/nifake_non_ivi/nifake_non_ivi_client.cpp"
    "${service_output_dir}/nifake_non_ivi/nifake_non_ivi_service.cpp"
    "${custom_dir}/nifake_non_ivi_service.custom.cpp"
    "${custom_dir}/nifake_service.custom.cpp"
)

    set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
    set(THREADS_PREFER_PTHREAD_FLAG TRUE)
    find_package(Threads REQUIRED)

target_link_libraries(IntegrationTestsRunner
    ${server_lib_deps}
    gmock
    grpc
    gtest
    Threads::Threads
)

# Ignore the use of deprecated functions in test code
target_compile_definitions(IntegrationTestsRunner
    PRIVATE _CRT_SECURE_NO_WARNINGS _WINSOCK_DEPRECATED_NO_WARNINGS)

add_library(TestApi SHARED
    "source/tests/utilities/test_api.cpp")
add_compile_definitions(TestApi TEST_API_BUILDING)

# Ignore the use of deprecated functions in test code
target_compile_definitions(TestApi
    PRIVATE _CRT_SECURE_NO_WARNINGS)

add_executable(UnitTestsRunner
    "imports/include/nierr_Status.cpp"
    "source/tests/utilities/run_all_tests.cpp"
    "source/tests/unit/callback_router_tests.cpp"
    "source/tests/unit/converters_tests.cpp"
    "source/tests/unit/library_set_runtime_environment_tests.cpp"
    "source/tests/unit/session_resource_repository_tests.cpp"
    "source/tests/unit/session_repository_tests.cpp"
    "source/tests/unit/calibration_operations_tests.cpp"
    "source/tests/unit/debug_session_properties_tests.cpp"
    "source/tests/unit/device_enumerator_tests.cpp"
    "source/tests/unit/software_enumerator_tests.cpp"
    "source/tests/unit/server_configuration_parser_tests.cpp"
    "source/tests/unit/server_security_configuration_tests.cpp"
    "source/tests/unit/ni_fake_non_ivi_service_tests.cpp"
    "source/tests/unit/ni_fake_service_tests.cpp"
    "source/tests/unit/nimxlc_terminal_adaptor_converters_tests.cpp"
    "source/tests/unit/precision_timestamp_converter_tests.cpp"
    "source/tests/unit/shared_library_tests.cpp"
    "source/tests/unit/syscfg_library_tests.cpp"
    "source/tests/unit/syscfg_resource_accessor_tests.cpp"
    "source/tests/unit/xnet_converters_tests.cpp"
    "source/tests/unit/xnet_socket_converters_tests.cpp"
    "source/tests/unit/tls_config_loader_tests.cpp"
    "source/server/calibration_operations_restricted_service.cpp"
    "source/server/debug_session_properties_restricted_service.cpp"
    "source/server/device_enumerator.cpp"
    "source/server/feature_toggles.cpp"
    "source/server/tls_config_loader.cpp"
    "source/server/semaphore.cpp"
    "source/server/server_configuration_parser.cpp"
    "source/server/server_security_configuration.cpp"
    "source/server/session_repository.cpp"
    "source/server/shared_library.cpp"
    "source/server/software_enumerator.cpp"
    "source/server/syscfg_library.cpp"
    "source/server/syscfg_resource_accessor.cpp"
    "source/server/syscfg_session_handler.cpp"
    ${nidevice_proto_srcs}
    ${session_proto_srcs}
    ${session_grpc_srcs}
    ${session_utilities_proto_srcs}
    ${session_utilities_grpc_srcs}
    ${deviceid_restricted_proto_srcs}
    ${deviceid_restricted_grpc_srcs}
    ${debugsessionproperties_restricted_proto_srcs}
    ${debugsessionproperties_restricted_grpc_srcs}
    ${calibrationoperations_restricted_proto_srcs}
    ${calibrationoperations_restricted_grpc_srcs}
    ${data_moniker_proto_srcs}
    ${data_moniker_grpc_srcs}
    ${precision_timestamp_proto_srcs}
    ${waveform_proto_srcs}
    "${proto_srcs_dir}/nifake.pb.cc"
    "${proto_srcs_dir}/nifake.grpc.pb.cc"
    "${proto_srcs_dir}/nifake_extension.pb.cc"
    "${proto_srcs_dir}/nifake_extension.grpc.pb.cc"
    "${proto_srcs_dir}/nifake_non_ivi.pb.cc"
    "${proto_srcs_dir}/nifake_non_ivi.grpc.pb.cc"
    "${proto_srcs_dir}/nimxlcterminaladaptor_restricted.pb.cc"
    "${proto_srcs_dir}/nixnet.grpc.pb.cc"
    "${proto_srcs_dir}/nixnet.pb.cc"
    "${proto_srcs_dir}/nixnetsocket.pb.cc"
    "${service_output_dir}/nifake/nifake_service.cpp"
    "${service_output_dir}/nifake_extension/nifake_extension_service.cpp"
    "${service_output_dir}/nifake_non_ivi/nifake_non_ivi_service.cpp"
    "${service_output_dir}/niswitch/niswitch_library.cpp"
    "${service_output_dir}/nixnet/nixnet_service.cpp"
    "${custom_dir}/nifake_service.custom.cpp"
    "${custom_dir}/nifake_extension_service.custom.cpp"
    "${custom_dir}/nifake_non_ivi_service.custom.cpp"
    "${custom_dir}/nimxlcterminaladaptor_restricted_service.custom.cpp"
    "${custom_dir}/nixnet_service.custom.cpp"
)

# ni_fake_service_tests.cpp and several DAQ cpp files exceed the MSVC limit for the number of sections
# in an obj file defined by PE-COFF. This line disables the limit.
if(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /bigobj /D_SILENCE_CXX17_ITERATOR_BASE_CLASS_DEPRECATION_WARNING")
endif(MSVC)

# Ignore the use of deprecated functions in test code
target_compile_definitions(UnitTestsRunner
    PRIVATE _CRT_SECURE_NO_WARNINGS _WINSOCK_DEPRECATED_NO_WARNINGS)

target_include_directories(UnitTestsRunner
    PRIVATE "${service_output_dir}"
    PRIVATE "${service_output_dir}/nifake"
    PRIVATE "${service_output_dir}/nifake_extension"
    PRIVATE "${service_output_dir}/nifake_non_ivi"
    PRIVATE "source/server")

target_link_libraries(UnitTestsRunner
    ${CMAKE_DL_LIBS}
    ${server_lib_deps}
    gmock
    grpc
    gtest
    Threads::Threads
)

#----------------------------------------------------------------------
# Copy test asset certificates to binary output certs sub-directory
#----------------------------------------------------------------------
add_custom_command(
  TARGET UnitTestsRunner POST_BUILD
  COMMAND  ${CMAKE_COMMAND} -E copy_directory
           ${CMAKE_SOURCE_DIR}/source/tests/assets/
           $<TARGET_FILE_DIR:UnitTestsRunner>/)

foreach(api ${nidrivers_to_build})
  set(compilation_test_sources
    ${compilation_test_sources}
    "${service_output_dir}/${api}/${api}_compilation_test.cpp")
endforeach()
add_library(CompilationTests STATIC ${compilation_test_sources})

target_link_libraries(CompilationTests
    ${_GRPC_GRPCPP}
    ${_UTF8CPP}
)
add_custom_target(generated_nidriver_service_library_hdrs DEPENDS ${nidriver_service_library_hdrs})
add_dependencies(CompilationTests generated_nidriver_service_library_hdrs)

set(system_test_runner_sources
  "imports/include/nierr_Status.cpp"
  "source/tests/utilities/run_all_tests.cpp"
  "source/server/core_services_registrar.cpp"
  "source/tests/system/device_server.cpp"
  "source/tests/system/enumerate_devices.cpp"
  "source/tests/system/enumerate_software.cpp"
  "source/tests/system/session_utilities_service_tests.cpp"
  "source/tests/system/nidaqmx_driver_api_tests.cpp"
  "source/tests/system/nidaqmx_session_tests.cpp"
  "source/tests/system/nidcpower_driver_api_tests.cpp"
  "source/tests/system/nidcpower_session_tests.cpp"
  "source/tests/system/nidigital_driver_api_tests.cpp"
  "source/tests/system/nidigital_session_tests.cpp"
  "source/tests/system/nidmm_driver_api_tests.cpp"
  "source/tests/system/nidmm_session_tests.cpp"
  "source/tests/system/nifgen_driver_api_tests.cpp"
  "source/tests/system/nifgen_session_tests.cpp"
  "source/tests/system/nifpga_session_tests.cpp"
  "source/tests/system/nirfsa_driver_api_tests.cpp"
  "source/tests/system/nirfsg_driver_api_tests.cpp"
  "source/tests/system/nirfsg_restricted_driver_api_tests.cpp"
  "source/tests/system/nirfsg_session_tests.cpp"
  "source/tests/system/niscope_driver_api_tests.cpp"
  "source/tests/system/niscope_restricted_driver_api_tests.cpp"
  "source/tests/system/niscope_session_tests.cpp"
  "source/tests/system/niswitch_driver_api_tests.cpp"
  "source/tests/system/niswitch_session_tests.cpp"
  "source/tests/system/nisync_driver_api_tests.cpp"
  "source/tests/system/nisync_session_tests.cpp"
  "source/tests/system/nitclk_driver_api_tests.cpp"
  "source/tests/system/nixnet_lin_driver_api_tests.cpp"
  "source/tests/system/nixnet_can_driver_api_tests.cpp"
  "source/tests/system/nixnet_ethernet_driver_api_tests.cpp"
  "source/tests/system/nixnetsocket_driver_api_tests.cpp"
  "source/tests/system/visa_driver_api_tests.cpp"
  "source/tests/system/visa_session_tests.cpp"
  "source/server/calibration_operations_restricted_service_registrar.cpp"
  "source/server/calibration_operations_restricted_service.cpp"
  "source/server/data_moniker_service.cpp"
  "source/server/debug_session_properties_restricted_service_registrar.cpp"
  "source/server/debug_session_properties_restricted_service.cpp"
  "source/server/device_enumerator.cpp"
  "source/server/feature_toggles.cpp"
  "source/server/semaphore.cpp"
  "source/server/session_repository.cpp"
  "source/server/session_utilities_service.cpp"
  "source/server/session_utilities_service_registrar.cpp"
  "source/server/shared_library.cpp"
  "source/server/software_enumerator.cpp"
  "source/server/syscfg_library.cpp"
  "source/server/syscfg_resource_accessor.cpp"
  "source/server/syscfg_session_handler.cpp"
  ${nidevice_proto_srcs}
  ${session_proto_srcs}
  ${session_grpc_srcs}
  ${session_utilities_proto_srcs}
  ${session_utilities_grpc_srcs}
  ${deviceid_restricted_proto_srcs}
  ${deviceid_restricted_grpc_srcs}
  ${debugsessionproperties_restricted_proto_srcs}
  ${debugsessionproperties_restricted_grpc_srcs}
  ${calibrationoperations_restricted_proto_srcs}
  ${calibrationoperations_restricted_grpc_srcs}
  ${data_moniker_proto_srcs}
  ${data_moniker_grpc_srcs}
  ${precision_timestamp_proto_srcs}
  ${waveform_proto_srcs}
  ${nidriver_service_srcs}
  ${nidriver_client_srcs}
)

if(WIN32)
  list(
    APPEND
      system_test_runner_sources
        "source/tests/system/nimxlcterminaladaptor_restricted_driver_api_tests.cpp"
        "source/tests/system/nirfmxbluetooth_driver_api_tests.cpp"
        "source/tests/system/nirfmxbluetooth_session_tests.cpp"
        "source/tests/system/nirfmxcdma2k_driver_api_tests.cpp"
        "source/tests/system/nirfmxcdma2k_session_tests.cpp"
        "source/tests/system/nirfmxgsm_driver_api_tests.cpp"
        "source/tests/system/nirfmxgsm_session_tests.cpp"
        "source/tests/system/nirfmxinstr_driver_api_tests.cpp"
        "source/tests/system/nirfmxinstr_restricted_driver_api_tests.cpp"
        "source/tests/system/nirfmxlte_driver_api_tests.cpp"
        "source/tests/system/nirfmxlte_session_tests.cpp"
        "source/tests/system/nirfmxnr_driver_api_tests.cpp"
        "source/tests/system/nirfmxnr_session_tests.cpp"
        "source/tests/system/nirfmxpulse_driver_api_tests.cpp"
        "source/tests/system/nirfmxpulse_session_tests.cpp"
        "source/tests/system/nirfmxspecan_driver_api_tests.cpp"
        "source/tests/system/nirfmxspecan_restricted_driver_api_tests.cpp"
        "source/tests/system/nirfmxspecan_session_tests.cpp"
        "source/tests/system/nirfmxtdscdma_driver_api_tests.cpp"
        "source/tests/system/nirfmxtdscdma_session_tests.cpp"
        "source/tests/system/nirfmxwcdma_driver_api_tests.cpp"
        "source/tests/system/nirfmxwcdma_session_tests.cpp"
        "source/tests/system/nirfmxdemod_driver_api_tests.cpp"
        "source/tests/system/nirfmxdemod_session_tests.cpp"
        "source/tests/system/nirfmxvna_driver_api_tests.cpp"
        "source/tests/system/nirfmxvna_session_tests.cpp"
        "source/tests/system/nirfmxwlan_driver_api_tests.cpp"
        "source/tests/system/nirfmxwlan_restricted_driver_api_tests.cpp"
        "source/tests/system/nirfmxwlan_session_tests.cpp"
  )
endif()

add_executable(SystemTestsRunner ${system_test_runner_sources})

target_link_libraries(SystemTestsRunner
    ${CMAKE_DL_LIBS}
    ${server_lib_deps}
    gmock
    gtest
)

# Ignore the use of deprecated functions in test code
target_compile_definitions(SystemTestsRunner
    PRIVATE _CRT_SECURE_NO_WARNINGS _WINSOCK_DEPRECATED_NO_WARNINGS)

add_custom_command(
  TARGET SystemTestsRunner POST_BUILD
  COMMAND  ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_SOURCE_DIR}/source/tests/assets/data/
            $<TARGET_FILE_DIR:SystemTestsRunner>/)

if(USE_NILRT_LEGACY_TOOLCHAIN)
    target_link_libraries(SystemTestsRunner stdc++fs)
    target_compile_definitions(SystemTestsRunner PRIVATE FS_EXPERIMENTAL)
endif()


# Hook up different google test runners to CTest
# add_test( NAME UnitTests COMMAND UnitTestsRunner )
add_test( NAME UnitTests COMMAND UnitTestsRunner )
add_test( NAME IntegrationTests COMMAND IntegrationTestsRunner )
add_test( NAME SystemTests COMMAND SystemTestsRunner )
````

<!--NI_OSS_SOURCE repo=grpc-device path=CODEOWNERS sha256=9f1b226d91795100ae12288b96f3e0300a03325743480f775b70c90aedadf5cf bytes=455 -->
## FILE: CODEOWNERS

- repository: `ni/grpc-device`
- source_path: `CODEOWNERS`
- sha256: `9f1b226d91795100ae12288b96f3e0300a03325743480f775b70c90aedadf5cf`
- bytes: 455

````text
# Default code owner for the repository
* @astarche @reckenro @maxxboehme

# Owners for the build files
/CMakeLists.txt      @astarche @reckenro @maxxboehme
/.github/**/*.yml    @astarche @reckenro @maxxboehme
/scripts/            @astarche @reckenro @maxxboehme

# Codegen
/generated           @reckenro @astarche @maxxboehme
/source/codegen/     @reckenro @astarche @maxxboehme

# Test
/source/tests/       @reckenro @astarche @maxxboehme
````

<!--NI_OSS_SOURCE repo=grpc-device path=component.yml sha256=4d49b0f230d22d01ac4c7124e87dbce235cf6f83950401bae9c540a594e4921c bytes=219 -->
## FILE: component.yml

- repository: `ni/grpc-device`
- source_path: `component.yml`
- sha256: `4d49b0f230d22d01ac4c7124e87dbce235cf6f83950401bae9c540a594e4921c`
- bytes: 219

````yaml
component:
  sbom_info:
    - name: grpc-device
      version: 2.11.0
      identifiers:
        cpe: cpe:2.3:a:grpc-device:grpc-device:2.11.0:*:*:*:*:*:*:*
      licenses:
        - legal_package: grpc-device151
````

<!--NI_OSS_SOURCE repo=grpc-device path=CONTRIBUTING.md sha256=14b1dd4c5070613b016cf96bc536551ef1d8fc36c2196a5104738b287dbf4c17 bytes=9767 -->
## FILE: CONTRIBUTING.md

- repository: `ni/grpc-device`
- source_path: `CONTRIBUTING.md`
- sha256: `14b1dd4c5070613b016cf96bc536551ef1d8fc36c2196a5104738b287dbf4c17`
- bytes: 9767

````markdown
# Contributing to grpc-device

Contributions to grpc-device are welcome from all!

grpc-device is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/grpc-device/).

grpc-device follows a pull-request model for development.  If you wish to
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

## Building on Windows 64-bit

### Prerequisites
To prepare for cmake + Microsoft Visual C++ compiler build
- Install Visual Studio 2022 or newer (Visual C++ compiler will be used).
- Install [Git](https://git-scm.com/).
- Install [CMake](https://cmake.org/download/) 3.18.0 or newer and add it to the PATH.
  - Our github actions use 3.18.0 to build currently. 
  - [CMake Build Failure in grpc-device: Compatibility Update Required](https://github.com/ni/grpc-device/issues/1172) documents a known issue when using newer versions of CMake where you will see `Compatibility with CMake < 3.5 has been removed from CMake` with a workaround of using the flag `-DCMAKE_POLICY_VERSION_MINIMUM=3.5`.
- Install [Python](https://www.python.org/downloads/) and add it to the PATH.
- Install [NASM](https://nasm.us/) and add it to the PATH.
- Install [mako](https://www.makotemplates.org/download.html)

Launch "x64 Native Tools Command Prompt for Visual Studio" and change to a directory where you have write permissions. Alternatively, use Windows PowerShell in a directory where you have write permissions.

### Clone Repo

Clone the repo and update submodules, this will pull the gRPC components and all dependencies

```
> git clone https://github.com/ni/grpc-device.git
> cd grpc-device
> git submodule update --init --recursive
```

### Build Debug

Build a debug build if debugging symbols are required during development:

```
> mkdir build
> cd build
> cmake .. -A x64
> cmake --build .
```

### Build Release

Build a release build for use in a production environment:

```
> mkdir build
> cd build
> cmake .. -A x64
> cmake --build . --config Release
```

### Build with Ninja

Build faster by using Ninja:

```
> "C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat"
> mkdir build
> cd build
> cmake .. -G "Ninja Multi-Config"
> cmake --build .
```

## Building on Linux

### Prerequisites

For Debian/Ubuntu, install git, cmake (3.18.0 or newer), and mako:
```
> sudo apt-get update
> sudo apt-get install git
> sudo apt-get install cmake
> sudo apt-get install g++
> sudo apt-get install python3-venv  # for ensurepip
> sudo apt-get install ninja-build   # optional
```

For NI Linux RT, install packagegroup-core-buildessential, git, git-perltools, cmake (3.18.0 or newer), python3-utils, and mako:
```
> opkg update
> opkg install packagegroup-core-buildessential
> opkg install git
> opkg install git-perltools
> opkg install cmake
> opkg install python3-misc
# follow the latest instructions to install pip:
# https://pip.pypa.io/en/stable/installing/
> python -m pip install mako
```

**Note**: Depending on the version of NI Linux RT, installing a newer version of CMake
may be required. Follow the instructions to [install CMake](https://cmake.org/install/).
If this is required, make sure to install openssl-dev as well.
```
> opkg install openssl-dev
```

**Note**: When building on Linux RT if the compiler toolchain segfaults at any point
you might need to increase the default stack size before building again.
```
> ulimit -s 8192
```

### Clone Repo

Clone the repo and update submodules, this will pull the gRPC components and all dependencies

```
> git clone https://github.com/ni/grpc-device.git grpc-device
> cd grpc-device
> git submodule update --init --recursive
```

### Build Debug

Build a debug build if debugging symbols are required during development:

```
> mkdir -p cmake/build
> cd cmake/build
> cmake ../..
> make
```

### Build Release

Build a release build for use in a production environment:

```
> mkdir -p cmake/build
> cd cmake/build
> cmake -DCMAKE_BUILD_TYPE=Release ../..
> make
```

## C++ Coding Conventions

This project follows the Google style guidelines for all C++ and protobuf files with the exceptions documented below.

The C++ style is encoded in the `clang-format` file at the root of the repository.<br>
See https://clang.llvm.org/docs/ClangFormatStyleOptions.html

Setting | Google | Ours | Justification
--|--|--|--
`ColumnLimit` | `80` | `0` | Some times a long line is appropriate. We should police that in PRs, not with our tooling.
`AlignAfterOpenBracket` | `Align` | `AlwaysBreak` | Either all parameters should be on one line or all of them on separate lines. Without this the formatter would allow you to leave parameters on the first line and would align the other lines with the first parameter. This adds a lot of whitespace.
`BreakBeforeBraces` | `Attach` | `Stroustrup` | This puts function curly braces on the next line and puts `else` blocks on the next line. This helps with control flow readability.
`DerivePointerAlignment` | `true` | `false` | We should be consistent with our pointer alignment. Left alignment (`void* foo`) is more standard than right (`void *foo`) and is the default Google style.
`IndentPPDirectives` | `None` | `BeforeHash` | Indented `#include` directives inside `#defined` blocks improves readability.

# Testing

## C++ Code under Source
Changes made to the C++ code under the `source` directory should be accompanied with auto tests in one of the
following three test suites, all written using [Google Test/Mock](https://github.com/google/googletest):

### Unit
Unit tests should use mocks or fakes of any dependencies of the subject under test (SUT). These tests get run automatically
for Windows and Linux when a pull request is created that merges to `main`.

The test name should match the class being tested.

> Example:<br>
> A unit test for class `MyFoo` should be named `MyFooTests` and go in `/source/tests/unit/my_foo.cpp`

### Integration
Integration tests should be used when testing multiple components together, such as the client & server. Any dependencies
not being tested should be mocked or faked. These tests get run automatically for Windows and Linux when a pull request
is created that merges to `main`.

The test name should match the class being tested.

> Example:<br>
> An integration test for class `MyFoo` should be named `MyFooTests` and go in `/source/tests/integration/my_foo.cpp`

### System
A system test tests the server and client on a system with the supported NI device drivers installed. These tests are not
run automatically and should be run manually by executing the `SystemTestRunner` class in the build directory.

The test name should match the driver and the features being tested.

## Code generation scripts
The code generation scripts generate files into the `generated` directory which gets checked into source control. Before
pushing a change to the templates or helpers, first perform a local build and add the resulting generated files to your
commit. This will allow reviewers to see the effects of the change.

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

See [LICENSE](https://github.com/ni/grpc-device/blob/master/LICENSE)
for details about how grpc-device is licensed.

# Additional Info

If you're looking for additional info while working in the grpc-device repo, you can check out the [Internal Development](https://github.com/ni/grpc-device/wiki/internal-development) page of our Wiki. It hosts a collection of overviews and tips and tricks that might prove useful.
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/analog-input-every-n-samples-aio.py sha256=d97f2734d12a8dfe51a57b7ddc4b568ddd9253963ba75c83068f6d25548a35d8 bytes=8533 -->
## FILE: examples/nidaqmx/analog-input-every-n-samples-aio.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/analog-input-every-n-samples-aio.py`
- sha256: `d97f2734d12a8dfe51a57b7ddc4b568ddd9253963ba75c83068f6d25548a35d8`
- bytes: 8533

````python
r"""Acquire analog data using the grpc asyncio API and RegisterEveryNSamplesEvent.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input-every-n-samples-aio.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name.
"""  # noqa: W505 - doc line too long

import asyncio
import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
PHYSICAL_CHANNEL = "Dev1/ai0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    PHYSICAL_CHANNEL = sys.argv[3]


async def _main():
    async with grpc.aio.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}") as channel:
        client = grpc_nidaqmx.NiDAQmxStub(channel)
        task = None

        def check_for_warning(response):
            """Print to console if the status indicates a warning."""
            if response.status > 0:
                warning_message = client.GetErrorString(
                    nidaqmx_types.GetErrorStringRequest(error_code=response.status)
                )
                sys.stderr.write(
                    f"{warning_message.error_string}\nWarning status: {response.status}\n"
                )

        async def check_for_stream_error(stream):
            """Raise an exception if the stream was closed with an error."""
            if stream.done() and await stream.code() != grpc.StatusCode.OK:
                _ = await stream.read()

        try:
            create_task_response = await client.CreateTask(nidaqmx_types.CreateTaskRequest())
            task = create_task_response.task

            await client.CreateAIVoltageChan(
                nidaqmx_types.CreateAIVoltageChanRequest(
                    task=task,
                    physical_channel=PHYSICAL_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    terminal_config=nidaqmx_types.InputTermCfgWithDefault.INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT,
                    units=nidaqmx_types.VoltageUnits2.VOLTAGE_UNITS2_VOLTS,
                )
            )

            total_samples_per_channel = 1000
            samples_per_channel_per_read = 100
            await client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=task,
                    sample_mode=nidaqmx_types.AcquisitionType.ACQUISITION_TYPE_FINITE_SAMPS,
                    samps_per_chan=total_samples_per_channel,
                    active_edge=nidaqmx_types.Edge1.EDGE1_RISING,
                    rate=100,
                )
            )

            every_n_samples_stream = client.RegisterEveryNSamplesEvent(
                nidaqmx_types.RegisterEveryNSamplesEventRequest(
                    task=task,
                    n_samples=samples_per_channel_per_read,
                    every_n_samples_event_type=nidaqmx_types.EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER,
                )
            )

            # Wait for initial_metadata and check for stream errors to ensure that the callback is
            # registered successfully before starting the task.
            await every_n_samples_stream.initial_metadata()
            await check_for_stream_error(every_n_samples_stream)

            done_event_stream = client.RegisterDoneEvent(
                nidaqmx_types.RegisterDoneEventRequest(task=task)
            )

            await done_event_stream.initial_metadata()
            await check_for_stream_error(done_event_stream)

            start_task_response = await client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
            check_for_warning(start_task_response)

            get_num_chans_response = await client.GetTaskAttributeUInt32(
                nidaqmx_types.GetTaskAttributeUInt32Request(
                    task=task, attribute=nidaqmx_types.TASK_ATTRIBUTE_NUM_CHANS
                )
            )

            number_of_channels = get_num_chans_response.value

            async def read_data():
                samps_per_chan_read = 0

                try:
                    async for every_n_samples_response in every_n_samples_stream:
                        read_response = await client.ReadAnalogF64(
                            nidaqmx_types.ReadAnalogF64Request(
                                task=task,
                                num_samps_per_chan=samples_per_channel_per_read,
                                fill_mode=nidaqmx_types.GroupBy.GROUP_BY_GROUP_BY_CHANNEL,
                                array_size_in_samps=number_of_channels
                                * samples_per_channel_per_read,
                            )
                        )
                        check_for_warning(read_response)

                        print(
                            f"Acquired {len(read_response.read_array)} samples",
                            f"({read_response.samps_per_chan_read} samples per channel)",
                        )
                        print("Read Data:", read_response.read_array[:10])

                        # Unregister the event stream when all samples are read.
                        samps_per_chan_read += read_response.samps_per_chan_read
                        if samps_per_chan_read >= total_samples_per_channel:
                            every_n_samples_stream.cancel()
                except asyncio.CancelledError:
                    pass

            async def wait_for_done():
                try:
                    async for done_response in done_event_stream:
                        done_event_stream.cancel()
                        # Cancel the acquisition if there's an error, otherwise let it continue
                        # until all samples are read.
                        if done_response.status:
                            every_n_samples_stream.cancel()
                except asyncio.CancelledError:
                    pass

            await asyncio.gather(read_data(), wait_for_done())
            stop_task_response = await client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
            check_for_warning(stop_task_response)

        except grpc.RpcError as rpc_error:
            error_message = str(rpc_error.details() or "")
            for key, value in rpc_error.trailing_metadata() or []:
                if key == "ni-error":
                    details = value if isinstance(value, str) else value.decode("utf-8")
                    error_message += f"\nError status: {details}"
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
            elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    "The operation is not implemented or is not supported/enabled in this service"
                )
            print(f"{error_message}")
        finally:
            if client and task:
                await client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))


## Run main
futures = [_main()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/analog-input-every-n-samples.py sha256=3be2057cd781fdba08670c14a537c7a63cbf28bbeb20c1968355f31f3f5f36a5 bytes=8794 -->
## FILE: examples/nidaqmx/analog-input-every-n-samples.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/analog-input-every-n-samples.py`
- sha256: `3be2057cd781fdba08670c14a537c7a63cbf28bbeb20c1968355f31f3f5f36a5`
- bytes: 8794

````python
r"""Acquire analog data using futures and RegisterEveryNSamplesEvent.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input-every-n-samples.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name.
"""

import sys
from concurrent.futures import ThreadPoolExecutor

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
PHYSICAL_CHANNEL = "Dev1/ai0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    PHYSICAL_CHANNEL = sys.argv[3]


def _main():
    with grpc.insecure_channel(
        f"{SERVER_ADDRESS}:{SERVER_PORT}"
    ) as channel, ThreadPoolExecutor() as executor:
        client = grpc_nidaqmx.NiDAQmxStub(channel)
        task = None

        def check_for_warning(response):
            """Print to console if the status indicates a warning."""
            if response.status > 0:
                warning_message = client.GetErrorString(
                    nidaqmx_types.GetErrorStringRequest(error_code=response.status)
                )
                sys.stderr.write(
                    f"{warning_message.error_string}\nWarning status: {response.status}\n"
                )

        def check_for_stream_error(stream):
            """Raise an exception if the stream was closed with an error."""
            if stream.done() and stream.exception() is not None:
                raise stream.exception()

        try:
            create_task_response = client.CreateTask(nidaqmx_types.CreateTaskRequest())
            task = create_task_response.task

            client.CreateAIVoltageChan(
                nidaqmx_types.CreateAIVoltageChanRequest(
                    task=task,
                    physical_channel=PHYSICAL_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    terminal_config=nidaqmx_types.InputTermCfgWithDefault.INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT,
                    units=nidaqmx_types.VoltageUnits2.VOLTAGE_UNITS2_VOLTS,
                )
            )

            total_samples_per_channel = 1000
            samples_per_channel_per_read = 100
            client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=task,
                    sample_mode=nidaqmx_types.AcquisitionType.ACQUISITION_TYPE_FINITE_SAMPS,
                    samps_per_chan=total_samples_per_channel,
                    active_edge=nidaqmx_types.Edge1.EDGE1_RISING,
                    rate=100,
                )
            )

            every_n_samples_stream = client.RegisterEveryNSamplesEvent(
                nidaqmx_types.RegisterEveryNSamplesEventRequest(
                    task=task,
                    n_samples=samples_per_channel_per_read,
                    every_n_samples_event_type=nidaqmx_types.EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER,
                )
            )

            # Wait for initial_metadata and check for stream errors to ensure that the callback is
            # registered successfully before starting the task.
            every_n_samples_stream.initial_metadata()
            check_for_stream_error(every_n_samples_stream)

            done_event_stream = client.RegisterDoneEvent(
                nidaqmx_types.RegisterDoneEventRequest(task=task)
            )

            done_event_stream.initial_metadata()
            check_for_stream_error(done_event_stream)

            start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
            check_for_warning(start_task_response)

            get_num_chans_response = client.GetTaskAttributeUInt32(
                nidaqmx_types.GetTaskAttributeUInt32Request(
                    task=task, attribute=nidaqmx_types.TASK_ATTRIBUTE_NUM_CHANS
                )
            )

            number_of_channels = get_num_chans_response.value

            def read_data():
                samps_per_chan_read = 0

                try:
                    for every_n_samples_response in every_n_samples_stream:
                        read_response = client.ReadAnalogF64(
                            nidaqmx_types.ReadAnalogF64Request(
                                task=task,
                                num_samps_per_chan=samples_per_channel_per_read,
                                fill_mode=nidaqmx_types.GroupBy.GROUP_BY_GROUP_BY_CHANNEL,
                                array_size_in_samps=number_of_channels
                                * samples_per_channel_per_read,
                            )
                        )
                        check_for_warning(read_response)

                        print(
                            f"Acquired {len(read_response.read_array)} samples",
                            f"({read_response.samps_per_chan_read} samples per channel)",
                        )
                        print("Read Data:", read_response.read_array[:10])

                        # Unregister the event stream when all samples are read.
                        samps_per_chan_read += read_response.samps_per_chan_read
                        if samps_per_chan_read >= total_samples_per_channel:
                            every_n_samples_stream.cancel()
                except grpc.RpcError as rpc_error:
                    if rpc_error.code() == grpc.StatusCode.CANCELLED:
                        return
                    raise

            def wait_for_done():
                try:
                    for done_response in done_event_stream:
                        done_event_stream.cancel()
                        # Cancel the acquisition if there's an error, otherwise let it continue
                        # until all samples are read.
                        if done_response.status:
                            every_n_samples_stream.cancel()
                except grpc.RpcError as rpc_error:
                    if rpc_error.code() == grpc.StatusCode.CANCELLED:
                        return
                    raise

            read_data_future = executor.submit(read_data)
            wait_for_done_future = executor.submit(wait_for_done)

            read_data_future.result()
            wait_for_done_future.result()

            stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
            check_for_warning(stop_task_response)

        except grpc.RpcError as rpc_error:
            error_message = str(rpc_error.details() or "")
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == "ni-error":
                    value = (
                        entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
                    )
                    error_message += f"\nError status: {value}"
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
            elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    "The operation is not implemented or is not supported/enabled in this service"
                )
            print(f"{error_message}")
        finally:
            if client and task:
                client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))


if __name__ == "__main__":
    _main()
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/analog-input.py sha256=16d27c2d6cabc07c3ef2d26ff829c6baea0b142966a3bbd27aaea6e8e625ba42 bytes=5022 -->
## FILE: examples/nidaqmx/analog-input.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/analog-input.py`
- sha256: `16d27c2d6cabc07c3ef2d26ff829c6baea0b142966a3bbd27aaea6e8e625ba42`
- bytes: 5022

````python
r"""Acquire a finite amount of data using the DAQ device's internal clock.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name..
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
PHYSICAL_CHANNEL = "Dev1/ai0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    PHYSICAL_CHANNEL = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateAIVoltageChan(
        nidaqmx_types.CreateAIVoltageChanRequest(
            task=task,
            physical_channel=PHYSICAL_CHANNEL,
            terminal_config=nidaqmx_types.INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT,
            min_val=-10.0,
            max_val=10.0,
            units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
        )
    )

    client.CfgSampClkTiming(
        nidaqmx_types.CfgSampClkTimingRequest(
            task=task,
            rate=10000.0,
            active_edge=nidaqmx_types.EDGE1_RISING,
            sample_mode=nidaqmx_types.ACQUISITION_TYPE_FINITE_SAMPS,
            samps_per_chan=1000,
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    # Get the number of channels. This may be greater than 1 if the physical_channel
    # parameter is a list or range of channels.
    get_num_chans_response = client.GetTaskAttributeUInt32(
        nidaqmx_types.GetTaskAttributeUInt32Request(
            task=task, attribute=nidaqmx_types.TASK_ATTRIBUTE_NUM_CHANS
        )
    )
    number_of_channels = get_num_chans_response.value

    read_response = client.ReadAnalogF64(
        nidaqmx_types.ReadAnalogF64Request(
            task=task,
            num_samps_per_chan=1000,
            array_size_in_samps=number_of_channels * 1000,
            fill_mode=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
            timeout=10.0,
        )
    )

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(
        f"Acquired {len(read_response.read_array)} samples",
        f"({read_response.samps_per_chan_read} samples per channel)",
    )
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/analog-output.py sha256=d8df47e08b0f06265311f8ee8d94bcde0018374a127acb6d3bdae5df11f55db7 bytes=4066 -->
## FILE: examples/nidaqmx/analog-output.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/analog-output.py`
- sha256: `d8df47e08b0f06265311f8ee8d94bcde0018374a127acb6d3bdae5df11f55db7`
- bytes: 4066

````python
r"""Output a single Voltage Update (Sample) to an Analog Output Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-output.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ao0" as the physical channel name.
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
PHYSICAL_CHANNEL = "Dev1/ao0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    PHYSICAL_CHANNEL = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateAOVoltageChan(
        nidaqmx_types.CreateAOVoltageChanRequest(
            task=task,
            physical_channel=PHYSICAL_CHANNEL,
            min_val=-10.0,
            max_val=10.0,
            units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    write_response = client.WriteAnalogF64(
        nidaqmx_types.WriteAnalogF64Request(
            task=task,
            num_samps_per_chan=1,
            data_layout=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
            write_array=[1.0],
            timeout=10.0,
        )
    )
    check_for_warning(write_response)

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(f"Output was successfully written to {PHYSICAL_CHANNEL}.")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/counter-input.py sha256=83fddb179e721c9e214ad8f5c11e5cc706b67031b4429005f391c9f93abe82da bytes=4015 -->
## FILE: examples/nidaqmx/counter-input.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/counter-input.py`
- sha256: `83fddb179e721c9e214ad8f5c11e5cc706b67031b4429005f391c9f93abe82da`
- bytes: 4015

````python
r"""Measure frequency using one counter on a Counter Input Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and counter name can be passed as separate command line
arguments.
  > python counter-input.py <server_address> <port_number> <counter_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ctr0" as the counter name.
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
COUNTER_NAME = "Dev1/ctr0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    COUNTER_NAME = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateCIFreqChan(
        nidaqmx_types.CreateCIFreqChanRequest(
            task=task,
            counter=COUNTER_NAME,
            min_val=1.192093,
            max_val=10000000,
            units=nidaqmx_types.FREQUENCY_UNITS3_HZ,
            edge=nidaqmx_types.EDGE1_RISING,
            meas_method=nidaqmx_types.COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR,
            meas_time=0.001,
            divisor=4,
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    read_response = client.ReadCounterScalarF64(
        nidaqmx_types.ReadCounterScalarF64Request(task=task, timeout=10.0)
    )
    check_for_warning(read_response)

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(f"Frequency: {read_response.value} Hz")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/counter-output.py sha256=5255f20adf3c0706f7f8518336ec2015fbc9db71eff6b103e831b24ffa1f5668 bytes=3975 -->
## FILE: examples/nidaqmx/counter-output.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/counter-output.py`
- sha256: `5255f20adf3c0706f7f8518336ec2015fbc9db71eff6b103e831b24ffa1f5668`
- bytes: 3975

````python
r"""Generate a single digital pulse from a Counter Output Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and counter name can be passed as separate command line
arguments.
  > python counter-output.py <server_address> <port_number> <counter_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ctr0" as the counter name.
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
COUNTER_NAME = "Dev1/ctr0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    COUNTER_NAME = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateCOPulseChanTime(
        nidaqmx_types.CreateCOPulseChanTimeRequest(
            task=task,
            counter=COUNTER_NAME,
            units=nidaqmx_types.DIGITAL_WIDTH_UNITS3_SECONDS,
            idle_state=nidaqmx_types.LEVEL1_LOW,
            initial_delay=1.0,
            low_time=0.5,
            high_time=1.0,
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    wait_until_task_done_response = client.WaitUntilTaskDone(
        nidaqmx_types.WaitUntilTaskDoneRequest(task=task, time_to_wait=10.0)
    )
    check_for_warning(wait_until_task_done_response)

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(f"Output was successfully written to {COUNTER_NAME}.")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/digital-input.py sha256=b46b96373d978259ec9ae00cdbe93bb5f7722285aea28d1cbe8e0702f4f948fc bytes=3882 -->
## FILE: examples/nidaqmx/digital-input.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/digital-input.py`
- sha256: `b46b96373d978259ec9ae00cdbe93bb5f7722285aea28d1cbe8e0702f4f948fc`
- bytes: 3882

````python
r"""Read values from a digital input port.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and lines name can be passed as separate command line
arguments.
  > python digital-input.py <server_address> <port_number> <lines_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/port0" as the lines name.
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
LINES = "Dev1/port0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    LINES = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateDIChan(
        nidaqmx_types.CreateDIChanRequest(
            task=task, lines=LINES, line_grouping=nidaqmx_types.LINE_GROUPING_CHAN_FOR_ALL_LINES
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    read_response = client.ReadDigitalU32(
        nidaqmx_types.ReadDigitalU32Request(
            task=task,
            num_samps_per_chan=1,
            array_size_in_samps=1,
            fill_mode=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
            timeout=10.0,
        )
    )
    check_for_warning(read_response)

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(f"Data acquired: {hex(read_response.read_array[0])}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/digital-output.py sha256=7559086abdfb97a411ceb789a35664d02e87c36fac003eafc7da2c43a93214e9 bytes=3912 -->
## FILE: examples/nidaqmx/digital-output.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/digital-output.py`
- sha256: `7559086abdfb97a411ceb789a35664d02e87c36fac003eafc7da2c43a93214e9`
- bytes: 3912

````python
r"""Write values to a digital output port.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and lines name can be passed as separate command line
arguments.
  > python digital-output.py <server_address> <port_number> <lines_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/port0" as the lines name.
"""

import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
LINES = "Dev1/port0"

if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    LINES = sys.argv[3]

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    create_task_response = client.CreateTask(
        nidaqmx_types.CreateTaskRequest(session_name="my task")
    )
    task = create_task_response.task

    client.CreateDOChan(
        nidaqmx_types.CreateDOChanRequest(
            task=task, lines=LINES, line_grouping=nidaqmx_types.LINE_GROUPING_CHAN_FOR_ALL_LINES
        )
    )

    start_task_response = client.StartTask(nidaqmx_types.StartTaskRequest(task=task))
    check_for_warning(start_task_response)

    write_response = client.WriteDigitalU32(
        nidaqmx_types.WriteDigitalU32Request(
            task=task,
            num_samps_per_chan=1,
            auto_start=True,
            timeout=10.0,
            data_layout=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
            write_array=[0xFFFF],
        )
    )
    check_for_warning(write_response)

    stop_task_response = client.StopTask(nidaqmx_types.StopTaskRequest(task=task))
    check_for_warning(stop_task_response)
    print(f"Output was successfully written to {LINES}.")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if task:
        client.ClearTask(nidaqmx_types.ClearTaskRequest(task=task))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/dsa-shared-timebase-and-trig-analog-input-and-output-aio.py sha256=1d73c68f5a2a0bc0ece0269030dc3645b030a8b3f2dd51fa54fcc8dc674dc6e0 bytes=26752 -->
## FILE: examples/nidaqmx/dsa-shared-timebase-and-trig-analog-input-and-output-aio.py

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/dsa-shared-timebase-and-trig-analog-input-and-output-aio.py`
- sha256: `1d73c68f5a2a0bc0ece0269030dc3645b030a8b3f2dd51fa54fcc8dc674dc6e0`
- bytes: 26752

````python
r"""Configure a total of four tasks on two PXI Dynamic Signal Acquistion (DSA) devices.

Each device runs a task for analog input and another for analog output. This example illustrates
continuous analog input and output operations.

Instructions for Running:
  1. Select which type of Synchronization method you want to use.
  2. Select the physical channel corresponding to the input signal on the DAQ device.
  3. Enter the minimum and maximum expected voltage for the input and output operations on each
     device.
     Note: For optimal accuracy, match the input range to the expected voltage level of the
           measured signal (for input) and generated signal (for output).
  4. Set the number of samples to acquire per channel. This parameter determines how many points
     will be read and generated with each iteration.
  5. Set the rate of the acquisition and generation. The same sampling rate is employed for input
     and output operations on each device.
  Note: The sampling rate should be at least 2.2 times the maximum frequency component of the
        signal being acquired on analog input and the signal being generated on analog output.
        Frequency components beyond about 0.47 times the sampling rate will be eliminated by the
        alias and imaging protection on the DSA device.

Steps:
  1. Create a task.
  2. Create an analog input and output channel for both the leader and follower devices.
  3. Set timing parameters for a continuous acquisition. The sample rate and block size are set to
     the same values for each device.
  4. There are two types of synchronization available on DSA devices. The first method shares the
     Sample Clock Timebase across the PXI_Star bus. It also uses the Sync Pulse which is shared
     across the PXI_Trig / RTSI bus. The second method uses the Sync Pulse in conjunction with the
     PXI Reference clock 10 on the PXI backplane.
  5. Call the Get Terminal Name with Device Prefix utility function. This will take a Task and a
     terminal and create a properly formatted device + terminal name. This signal is then used as an
     output generation trigger on the leader as well as and acquisition start trigger and generation
     start trigger on the follower. The signal is shared along the PXI_Trig / RTSI bus.
  6. Synthesize a standard sine waveform and load this data into the output RAM buffer for each
     device.
  7. Call the Start function to start the acquisition.
  8. Read all of the data continuously. The 'Samples per Channel' control will specify how many
     samples per channel are read each time. If either device reports an error or the user presses
     Enter, the acquisition will stop.
  9. Call the Clear Task function to clear the task.
  10. Display an error if any.

I/O Connections Overview:
  Make sure your signal input and output terminals matches the Physical Channel I/O controls.

  It is important to ensure that your PXI chassis has been properly configured in MAX. If your
  chassis has not been configured in software before running the example, your devices may fail to
  synchronize properly.


The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

This example requires physical hardware.

Running from command line:

Server machine's IP address, port number, leader_device, and follower_device can be passed as
separate command line arguments.
  > python dsa-shared-timebase-and-trig-analog-input-and-output-aio.py <server_address> <port_number> <leader_device> <follower_device>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1" as the leader device and "Dev2" as the follower device.
"""  # noqa: W505

import asyncio
import math
import sys

import grpc
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx

# False = sample clock, True = reference clock
SYNCHRONIZATION_TYPE_IS_REFERENCE_CLOCK = False
SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
LEADER_DEVICE = "Dev1"
FOLLOWER_DEVICE = "Dev2"
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    LEADER_DEVICE = sys.argv[3]
if len(sys.argv) >= 5:
    FOLLOWER_DEVICE = sys.argv[4]

LEADER_INPUT_CHANNEL = f"{LEADER_DEVICE}/ai0"
LEADER_OUTPUT_CHANNEL = f"{LEADER_DEVICE}/ao0"
FOLLOWER_INPUT_CHANNEL = f"{FOLLOWER_DEVICE}/ai0"
FOLLOWER_OUTPUT_CHANNEL = f"{FOLLOWER_DEVICE}/ao0"

client = None
leader_input_task = None
leader_output_task = None
follower_input_task = None
follower_output_task = None


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    assert client is not None
    if response.status > 0:
        warning_message = client.GetErrorString(
            nidaqmx_types.GetErrorStringRequest(error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


async def _main():
    global client, leader_input_task, leader_output_task, follower_input_task, follower_output_task
    num_leader_samples_written = 0
    num_follower_samples_written = 0
    async with grpc.aio.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}") as channel:
        client = grpc_nidaqmx.NiDAQmxStub(channel)

        async def get_terminal_name_with_dev_prefix(task, terminal_name):
            assert client is not None
            num_devices_response = await client.GetTaskAttributeUInt32(
                nidaqmx_types.GetTaskAttributeUInt32Request(
                    task=task, attribute=nidaqmx_types.TASK_ATTRIBUTE_NUM_DEVICES
                )
            )
            num_devices = num_devices_response.value
            for i in range(num_devices):
                # devices are 1-indexed, so use i + 1 here
                device = (
                    await client.GetNthTaskDevice(
                        nidaqmx_types.GetNthTaskDeviceRequest(task=task, index=i + 1)
                    )
                ).buffer
                device_category = (
                    await client.GetDeviceAttributeInt32(
                        nidaqmx_types.GetDeviceAttributeInt32Request(
                            device_name=device,
                            attribute=nidaqmx_types.DEVICE_ATTRIBUTE_PRODUCT_CATEGORY,
                        )
                    )
                ).value
                if (
                    device_category != nidaqmx_types.DEVICE_INT32_PRODUCT_CATEGORY_C_SERIES_MODULE
                    and device_category != nidaqmx_types.DEVICE_INT32_PRODUCT_CATEGORY_SCXI_MODULE
                ):
                    return "/" + device + "/" + terminal_name
            raise Exception("Unable to get terminal name for timebase!")

        def generate_sinewave(elements, amplitude, frequency, phase):
            sinewave = [
                amplitude * math.sin(math.pi / 180.0 * (phase + 360.0 * frequency * i))
                for i in range(elements)
            ]
            new_phase = (phase + frequency * 360.0 * elements) % 360.0
            return (sinewave, new_phase)

        try:
            # DAQmx Configure Tasks code
            create_task_response = await client.CreateTask(
                nidaqmx_types.CreateTaskRequest(session_name="Leader input task")
            )
            leader_input_task = create_task_response.task
            await client.CreateAIVoltageChan(
                nidaqmx_types.CreateAIVoltageChanRequest(
                    task=leader_input_task,
                    physical_channel=LEADER_INPUT_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
                    terminal_config=nidaqmx_types.INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT,
                )
            )
            await client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=leader_input_task,
                    rate=10000,
                    active_edge=nidaqmx_types.EDGE1_RISING,
                    sample_mode=nidaqmx_types.ACQUISITION_TYPE_CONT_SAMPS,
                    samps_per_chan=1000,
                )
            )

            create_task_response = await client.CreateTask(
                nidaqmx_types.CreateTaskRequest(session_name="Leader output task")
            )
            leader_output_task = create_task_response.task
            await client.CreateAOVoltageChan(
                nidaqmx_types.CreateAOVoltageChanRequest(
                    task=leader_output_task,
                    physical_channel=LEADER_OUTPUT_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
                )
            )
            await client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=leader_output_task,
                    rate=10000,
                    active_edge=nidaqmx_types.EDGE1_RISING,
                    sample_mode=nidaqmx_types.ACQUISITION_TYPE_CONT_SAMPS,
                    samps_per_chan=1000,
                )
            )

            create_task_response = await client.CreateTask(
                nidaqmx_types.CreateTaskRequest(session_name="Follower input task")
            )
            follower_input_task = create_task_response.task
            await client.CreateAIVoltageChan(
                nidaqmx_types.CreateAIVoltageChanRequest(
                    task=follower_input_task,
                    physical_channel=FOLLOWER_INPUT_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
                    terminal_config=nidaqmx_types.INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT,
                )
            )
            await client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=follower_input_task,
                    rate=10000,
                    active_edge=nidaqmx_types.EDGE1_RISING,
                    sample_mode=nidaqmx_types.ACQUISITION_TYPE_CONT_SAMPS,
                    samps_per_chan=1000,
                )
            )

            create_task_response = await client.CreateTask(
                nidaqmx_types.CreateTaskRequest(session_name="Follower output task")
            )
            follower_output_task = create_task_response.task
            await client.CreateAOVoltageChan(
                nidaqmx_types.CreateAOVoltageChanRequest(
                    task=follower_output_task,
                    physical_channel=FOLLOWER_OUTPUT_CHANNEL,
                    min_val=-10.0,
                    max_val=10.0,
                    units=nidaqmx_types.VOLTAGE_UNITS2_VOLTS,
                )
            )
            await client.CfgSampClkTiming(
                nidaqmx_types.CfgSampClkTimingRequest(
                    task=follower_output_task,
                    rate=10000,
                    active_edge=nidaqmx_types.EDGE1_RISING,
                    sample_mode=nidaqmx_types.ACQUISITION_TYPE_CONT_SAMPS,
                    samps_per_chan=1000,
                )
            )

            # DAQmx Clock Synchronization code
            if SYNCHRONIZATION_TYPE_IS_REFERENCE_CLOCK:
                # Note: Not all DSA devices support reference clock synchronization. Refer to
                # your hardware device manual for further information on whether this method
                # of synchronization is supported for your particular device.
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=leader_input_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_REF_CLK_SRC,
                        value="PXI_Clk10",
                    )
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=leader_output_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_REF_CLK_SRC,
                        value="PXI_Clk10",
                    )
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=follower_input_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_REF_CLK_SRC,
                        value="PXI_Clk10",
                    )
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=follower_output_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_REF_CLK_SRC,
                        value="PXI_Clk10",
                    )
                )
            else:
                # Sample clock
                # Note: If you are using PXI DSA devices, the leader device must be in PXI Slot 2.
                timebase_source = await get_terminal_name_with_dev_prefix(
                    task=leader_input_task, terminal_name="SampleClockTimebase"
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=leader_output_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC,
                        value=timebase_source,
                    )
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=follower_input_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC,
                        value=timebase_source,
                    )
                )
                await client.SetTimingAttributeString(
                    nidaqmx_types.SetTimingAttributeStringRequest(
                        task=follower_output_task,
                        attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC,
                        value=timebase_source,
                    )
                )

            sync_pulse_source = await get_terminal_name_with_dev_prefix(
                task=leader_input_task, terminal_name="SyncPulse"
            )
            await client.SetTimingAttributeString(
                nidaqmx_types.SetTimingAttributeStringRequest(
                    task=leader_output_task,
                    attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SYNC_PULSE_SRC,
                    value=sync_pulse_source,
                )
            )
            await client.SetTimingAttributeString(
                nidaqmx_types.SetTimingAttributeStringRequest(
                    task=follower_input_task,
                    attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SYNC_PULSE_SRC,
                    value=sync_pulse_source,
                )
            )
            await client.SetTimingAttributeString(
                nidaqmx_types.SetTimingAttributeStringRequest(
                    task=follower_output_task,
                    attribute=nidaqmx_types.TimingStringAttribute.TIMING_ATTRIBUTE_SYNC_PULSE_SRC,
                    value=sync_pulse_source,
                )
            )

            # DAQmx Configure Start Trigger code
            start_trigger = await get_terminal_name_with_dev_prefix(
                task=leader_input_task, terminal_name="ai/StartTrigger"
            )
            await client.CfgDigEdgeStartTrig(
                nidaqmx_types.CfgDigEdgeStartTrigRequest(
                    task=leader_output_task,
                    trigger_source=start_trigger,
                    trigger_edge=nidaqmx_types.EDGE1_RISING,
                )
            )
            await client.CfgDigEdgeStartTrig(
                nidaqmx_types.CfgDigEdgeStartTrigRequest(
                    task=follower_input_task,
                    trigger_source=start_trigger,
                    trigger_edge=nidaqmx_types.EDGE1_RISING,
                )
            )
            await client.CfgDigEdgeStartTrig(
                nidaqmx_types.CfgDigEdgeStartTrigRequest(
                    task=follower_output_task,
                    trigger_source=start_trigger,
                    trigger_edge=nidaqmx_types.EDGE1_RISING,
                )
            )

            (leader_write_data, phase) = generate_sinewave(250, 1.0, 0.02, 0.0)
            (follower_write_data, phase) = generate_sinewave(250, 1.0, 0.02, phase)

            # DAQmx Write code
            write_response = await client.WriteAnalogF64(
                nidaqmx_types.WriteAnalogF64Request(
                    task=leader_output_task,
                    num_samps_per_chan=250,
                    auto_start=False,
                    timeout=10.0,
                    data_layout=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
                    write_array=leader_write_data,
                )
            )
            check_for_warning(write_response)
            num_leader_samples_written = write_response.samps_per_chan_written
            write_response = await client.WriteAnalogF64(
                nidaqmx_types.WriteAnalogF64Request(
                    task=follower_output_task,
                    num_samps_per_chan=250,
                    auto_start=False,
                    timeout=10.0,
                    data_layout=nidaqmx_types.GROUP_BY_GROUP_BY_CHANNEL,
                    write_array=follower_write_data,
                )
            )
            check_for_warning(write_response)
            num_follower_samples_written = write_response.samps_per_chan_written

            every_n_samples_stream = client.RegisterEveryNSamplesEvent(
                nidaqmx_types.RegisterEveryNSamplesEventRequest(
                    task=leader_input_task,
                    n_samples=100,
                    every_n_samples_event_type=nidaqmx_types.EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER,
                )
            )

            # Wait for initial_metadata to ensure that the callback is registered before starting
            # the task.
            await every_n_samples_stream.initial_metadata()

            done_event_stream_list = []
            done_event_stream_list.append(
                client.RegisterDoneEvent(
                    nidaqmx_types.RegisterDoneEventRequest(task=leader_input_task)
                )
            )
            done_event_stream_list.append(
                client.RegisterDoneEvent(
                    nidaqmx_types.RegisterDoneEventRequest(task=leader_output_task)
                )
            )
            done_event_stream_list.append(
                client.RegisterDoneEvent(
                    nidaqmx_types.RegisterDoneEventRequest(task=follower_input_task)
                )
            )
            done_event_stream_list.append(
                client.RegisterDoneEvent(
                    nidaqmx_types.RegisterDoneEventRequest(task=follower_output_task)
                )
            )
            for done_event_stream in done_event_stream_list:
                await done_event_stream.initial_metadata()

            # DAQmx Start code
            start_task_response = await client.StartTask(
                nidaqmx_types.StartTaskRequest(task=leader_output_task)
            )
            check_for_warning(start_task_response)
            start_task_response = await client.StartTask(
                nidaqmx_types.StartTaskRequest(task=follower_input_task)
            )
            check_for_warning(start_task_response)
            start_task_response = await client.StartTask(
                nidaqmx_types.StartTaskRequest(task=follower_output_task)
            )
            check_for_warning(start_task_response)
            # trigger task must be started last
            start_task_response = await client.StartTask(
                nidaqmx_types.StartTaskRequest(task=leader_input_task)
            )
            check_for_warning(start_task_response)

            async def read_data():
                assert client is not None
                nonlocal num_leader_samples_written, num_follower_samples_written
                async for every_n_samples_response in every_n_samples_stream:
                    leader_response = await client.ReadAnalogF64(
                        nidaqmx_types.ReadAnalogF64Request(
                            task=leader_input_task,
                            num_samps_per_chan=2000,
                            timeout=10.0,
                            fill_mode=nidaqmx_types.GroupBy.GROUP_BY_GROUP_BY_CHANNEL,
                            array_size_in_samps=2000,
                        )
                    )
                    check_for_warning(leader_response)
                    num_leader_samples_written += leader_response.samps_per_chan_read
                    follower_response = await client.ReadAnalogF64(
                        nidaqmx_types.ReadAnalogF64Request(
                            task=follower_input_task,
                            num_samps_per_chan=2000,
                            timeout=10.0,
                            fill_mode=nidaqmx_types.GroupBy.GROUP_BY_GROUP_BY_CHANNEL,
                            array_size_in_samps=2000,
                        )
                    )
                    num_follower_samples_written += follower_response.samps_per_chan_read
                    check_for_warning(follower_response)

                    print(
                        f"\t{leader_response.samps_per_chan_read}\t{follower_response.samps_per_chan_read}\t\t{num_leader_samples_written}\t{num_follower_samples_written}"
                    )

            async def wait_for_done(done_event_stream):
                async for done_response in done_event_stream:
                    every_n_samples_stream.cancel()
                    for stream in done_event_stream_list:
                        stream.cancel()

            async def wait_for_input():
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, sys.stdin.readline)
                raise Exception("Enter pressed, quitting")

            print("Acquiring samples continuously. Press Enter to interrupt")
            print("\nRead:\tLeader\tFollower\tTotal:\tLeader\tFollower")
            tasks = [read_data(), wait_for_input()] + [
                wait_for_done(stream) for stream in done_event_stream_list
            ]
            await asyncio.gather(*tasks)
            stop_task_response = await client.StopTask(
                nidaqmx_types.StopTaskRequest(task=leader_input_task)
            )
            check_for_warning(stop_task_response)
            stop_task_response = await client.StopTask(
                nidaqmx_types.StopTaskRequest(task=leader_output_task)
            )
            check_for_warning(stop_task_response)
            stop_task_response = await client.StopTask(
                nidaqmx_types.StopTaskRequest(task=follower_input_task)
            )
            check_for_warning(stop_task_response)
            stop_task_response = await client.StopTask(
                nidaqmx_types.StopTaskRequest(task=follower_output_task)
            )
            check_for_warning(stop_task_response)

        except grpc.RpcError as rpc_error:
            error_message = str(rpc_error.details() or "")
            for key, value in rpc_error.trailing_metadata() or []:
                if key == "ni-error":
                    details = value if isinstance(value, str) else value.decode("utf-8")
                    error_message += f"\nError status: {details}"
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
            elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    "The operation is not implemented or is not supported/enabled in this service"
                )
            print(f"{error_message}")

        finally:
            await _cleanup()


async def _cleanup():
    global leader_input_task, leader_output_task, follower_input_task, follower_output_task
    if client:
        if leader_input_task:
            await client.ClearTask(nidaqmx_types.ClearTaskRequest(task=leader_input_task))
            leader_input_task = None
        if leader_output_task:
            await client.ClearTask(nidaqmx_types.ClearTaskRequest(task=leader_output_task))
            leader_output_task = None
        if follower_input_task:
            await client.ClearTask(nidaqmx_types.ClearTaskRequest(task=follower_input_task))
            follower_input_task = None
        if follower_output_task:
            await client.ClearTask(nidaqmx_types.ClearTaskRequest(task=follower_output_task))
            follower_output_task = None


# Run main
try:
    futures = [_main()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
finally:
    # This handles cleanup if the user presses Ctrl+C
    cleanup_future = [_cleanup()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(cleanup_future))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/moniker-streaming/CMakeLists.txt sha256=4e7e4820d7dace7eae9e51417327153039e5b86980f15baa102b67f31d8cf09f bytes=3477 -->
## FILE: examples/nidaqmx/moniker-streaming/CMakeLists.txt

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/moniker-streaming/CMakeLists.txt`
- sha256: `4e7e4820d7dace7eae9e51417327153039e5b86980f15baa102b67f31d8cf09f`
- bytes: 3477

````text
# cmake build file for C++ MonikerStreamingClient example.
# Assumes protobuf and gRPC have been installed using cmake.

cmake_minimum_required(VERSION 3.16)

project(MonikerStreamingClient C CXX)

find_package(Protobuf CONFIG REQUIRED)
message(STATUS "Using protobuf ${Protobuf_VERSION}")

set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
find_program(_PROTOBUF_PROTOC protoc)
find_package(gRPC CONFIG REQUIRED)
message(STATUS "Using gRPC ${gRPC_VERSION}")
set(_GRPC_GRPCPP gRPC::grpc++)
find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /bigobj")

# Proto files
get_filename_component(daqmx_proto "${CMAKE_SOURCE_DIR}/../../../generated/nidaqmx/nidaqmx.proto" ABSOLUTE)
get_filename_component(daqmx_proto_path "${daqmx_proto}" PATH)
get_filename_component(session_proto "${CMAKE_SOURCE_DIR}/../../../third_party/ni-apis/ni/grpcdevice/v1/session.proto" ABSOLUTE)
get_filename_component(session_proto_path "${session_proto}" PATH)
get_filename_component(data_moniker_proto "${CMAKE_SOURCE_DIR}/../../../imports/protobuf/data_moniker.proto" ABSOLUTE)
get_filename_component(data_moniker_proto_path "${data_moniker_proto}" PATH)

message(STATUS "daqmx_proto_path: ${daqmx_proto_path}")
#----------------------------------------------------------------------
# Generate sources from proto files
# Usage: GenerateGrpcSources(<proto-file-name> <proto-file-path>)
#----------------------------------------------------------------------
function(GenerateGrpcSources)
set(proto_name ${ARGV0})
set(proto_absolute_path ${ARGV1})

set(proto_srcs "${CMAKE_CURRENT_BINARY_DIR}/${proto_name}.pb.cc")
set(proto_hdrs "${CMAKE_CURRENT_BINARY_DIR}/${proto_name}.pb.h")
set(grpc_srcs "${CMAKE_CURRENT_BINARY_DIR}/${proto_name}.grpc.pb.cc")
set(grpc_hdrs "${CMAKE_CURRENT_BINARY_DIR}/${proto_name}.grpc.pb.h")

add_custom_command(
      OUTPUT "${proto_srcs}" "${proto_hdrs}" "${grpc_srcs}" "${grpc_hdrs}"
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
        -I "${daqmx_proto_path}"
        -I "${session_proto_path}"
        -I "${data_moniker_proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        ${proto_absolute_path}
      DEPENDS ${proto_absolute_path})
endfunction()

# Generated sources
GenerateGrpcSources(nidaqmx ${daqmx_proto})
GenerateGrpcSources(session ${session_proto})
GenerateGrpcSources(data_moniker ${data_moniker_proto})

# Include generated *.pb.h files
include_directories("${CMAKE_CURRENT_BINARY_DIR}")

add_executable(MonikerStreamingClient
    "stream-read-analog-input-using-moniker-streaming.cpp"
    "${CMAKE_CURRENT_BINARY_DIR}/nidaqmx.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/nidaqmx.pb.h"
    "${CMAKE_CURRENT_BINARY_DIR}/nidaqmx.grpc.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/nidaqmx.grpc.pb.h"
    "${CMAKE_CURRENT_BINARY_DIR}/session.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/session.pb.h"
    "${CMAKE_CURRENT_BINARY_DIR}/session.grpc.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/session.grpc.pb.h"
    "${CMAKE_CURRENT_BINARY_DIR}/data_moniker.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/data_moniker.pb.h"
    "${CMAKE_CURRENT_BINARY_DIR}/data_moniker.grpc.pb.cc"
    "${CMAKE_CURRENT_BINARY_DIR}/data_moniker.grpc.pb.h"
    )
target_link_libraries(MonikerStreamingClient
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF})
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidaqmx/moniker-streaming/stream-read-analog-input-using-moniker-streaming.cpp sha256=ed2fedac5fc4509aa0649b9c851be39834c20ce1e03534f63ada1921d893c76a bytes=9513 -->
## FILE: examples/nidaqmx/moniker-streaming/stream-read-analog-input-using-moniker-streaming.cpp

- repository: `ni/grpc-device`
- source_path: `examples/nidaqmx/moniker-streaming/stream-read-analog-input-using-moniker-streaming.cpp`
- sha256: `ed2fedac5fc4509aa0649b9c851be39834c20ce1e03534f63ada1921d893c76a`
- bytes: 9513

````cpp
/*********************************************************************
* Acquire data continuously from an analog input channel using moniker based streaming
*
* The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
*   C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm
*
* Getting Started:
*
* To run this example, install "NI-DAQmx Driver" on the server machine:
*   https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html
*
* For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
* Client" wiki page:
*   https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client
*
* Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
*   https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference
*
* To run this example without hardware: create a simulated device in NI MAX on the server (Windows
* only).
*
* Build:
*
*   > mkdir build
*   > cd build
*   > cmake ..
*   > cmake --build .
*
* Running from command line:
*
* Server machine's IP address, port number, and physical channel name can be passed as separate
* command line arguments.
*   > MonikerStreamingClient <server_address> <port_number> <physical_channel_name>
* If they are not passed in as command line arguments, then by default the server address will be
* "localhost:31763", with "Dev1/ai0" as the physical channel name..
*********************************************************************/

#include <iostream>
#include <sstream>
#include <grpcpp/grpcpp.h>

#include "nidaqmx.grpc.pb.h"
#include "data_moniker.grpc.pb.h"

using namespace nidaqmx_grpc;
using StubPtr = std::unique_ptr<NiDAQmx::Stub>;

std::string SERVER_ADDRESS = "localhost";
std::string SERVER_PORT = "31763";
std::string PHYSICAL_CHANNEL = "Dev1/ai0";
int NUM_ITERATIONS = 5;

class grpc_driver_error : public std::runtime_error {
 private:
  ::grpc::StatusCode code_;
  std::multimap<std::string, std::string> trailers_;

 public:
  grpc_driver_error(const std::string& message, ::grpc::StatusCode code, const std::multimap<grpc::string_ref, grpc::string_ref>& trailers)
    : std::runtime_error(message), code_(code)
  {
    for (const auto& trailer : trailers) {
      trailers_.emplace(
        std::string(trailer.first.data(), trailer.first.length()),
        std::string(trailer.second.data(), trailer.second.length()));
    }
  }

  ::grpc::StatusCode StatusCode() const
  {
    return code_;
  }

  const std::multimap<std::string, std::string>& Trailers() const
  {
    return trailers_;
  }
};

inline void raise_if_error(const ::grpc::Status& status, const ::grpc::ClientContext& context)
{
  if (!status.ok()) {
    throw grpc_driver_error(status.error_message(), status.error_code(), context.GetServerTrailingMetadata());
  }
}

void print_array(const MonikerReadAnalogF64Response& data)
{
  std::cout << "[";
  for (int i = 0; i < data.read_array().size(); i++) {
    std::cout << data.read_array().Get(i) << " ";
  }
  std::cout << "]" << std::endl;
}

::nidevice_grpc::Session create_and_configure_read_task(NiDAQmx::Stub &client, const std::string &PHYSICAL_CHANNEL)
{
  ::grpc::ClientContext create_task_context;
  auto create_task_request = CreateTaskRequest{};
  create_task_request.set_session_name("my task");
  auto create_task_response = CreateTaskResponse{};
  raise_if_error(
    client.CreateTask(&create_task_context, create_task_request, &create_task_response),
    create_task_context);
  auto daqmx_read_task = create_task_response.task();

  ::grpc::ClientContext create_channel_context;
  auto create_channel_request = CreateAIVoltageChanRequest{};
  create_channel_request.mutable_task()->CopyFrom(daqmx_read_task);
  create_channel_request.set_physical_channel(PHYSICAL_CHANNEL);
  create_channel_request.set_terminal_config(InputTermCfgWithDefault::INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT);
  create_channel_request.set_min_val(-10.0);
  create_channel_request.set_max_val(10.0);
  create_channel_request.set_units(VoltageUnits2::VOLTAGE_UNITS2_VOLTS);
  auto create_channel_response = CreateAIVoltageChanResponse{};
  raise_if_error(
    client.CreateAIVoltageChan(&create_channel_context, create_channel_request, &create_channel_response),
    create_channel_context);

  ::grpc::ClientContext cfg_clk_context;
  auto cfg_clk_request = CfgSampClkTimingRequest{};
  cfg_clk_request.mutable_task()->CopyFrom(daqmx_read_task);
  cfg_clk_request.set_rate(100.0);
  cfg_clk_request.set_active_edge(Edge1::EDGE1_RISING);
  cfg_clk_request.set_sample_mode(AcquisitionType::ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT);
  cfg_clk_request.set_samps_per_chan(10);
  auto cfg_clk_response = CfgSampClkTimingResponse{};
  raise_if_error(
    client.CfgSampClkTiming(&cfg_clk_context, cfg_clk_request, &cfg_clk_response),
    cfg_clk_context);

  ::grpc::ClientContext set_read_attribute_context;
  auto set_read_attribute_request = SetReadAttributeInt32Request{};
  set_read_attribute_request.mutable_task()->CopyFrom(daqmx_read_task);
  set_read_attribute_request.set_attribute(ReadInt32Attribute::READ_ATTRIBUTE_WAIT_MODE);
  set_read_attribute_request.set_value(ReadInt32AttributeValues::READ_INT32_WAIT_MODE_POLL);
  auto set_read_attribute_response = SetReadAttributeInt32Response{};
  raise_if_error(
    client.SetReadAttributeInt32(&set_read_attribute_context, set_read_attribute_request, &set_read_attribute_response),
    set_read_attribute_context);

  ::grpc::ClientContext start_task_context;
  StartTaskRequest start_task_request;
  start_task_request.mutable_task()->CopyFrom(daqmx_read_task);
  StartTaskResponse start_task_response;
  raise_if_error(
    client.StartTask(&start_task_context, start_task_request, &start_task_response),
    start_task_context);

  return daqmx_read_task;
}

int main(int argc, char **argv)
{
  if (argc >= 2) {
    SERVER_ADDRESS = argv[1];
  }
  if (argc >= 3) {
    SERVER_PORT = argv[2];
  }
  if (argc >= 4) {
    PHYSICAL_CHANNEL = argv[3];
  }
  auto target_str = SERVER_ADDRESS + ":" + SERVER_PORT;
  auto channel = grpc::CreateChannel(target_str, grpc::InsecureChannelCredentials());
  NiDAQmx::Stub client(channel);
  ni::data_monikers::DataMoniker::Stub moniker_service(channel);

  try {
    auto daqmx_read_task = create_and_configure_read_task(client, PHYSICAL_CHANNEL);

    // Setup the read stream
    ::grpc::ClientContext begin_read_context;
    auto begin_read_request = BeginReadAnalogF64Request{};
    begin_read_request.mutable_task()->CopyFrom(daqmx_read_task);
    begin_read_request.set_num_samps_per_chan(10);
    begin_read_request.set_timeout(10.0);
    begin_read_request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    begin_read_request.set_array_size_in_samps(10);
    auto begin_read_response = BeginReadAnalogF64Response{};
    raise_if_error(
      client.BeginReadAnalogF64(&begin_read_context, begin_read_request, &begin_read_response),
      begin_read_context);
    auto daqmx_read_moniker = new ni::data_monikers::Moniker(begin_read_response.moniker());

    ::grpc::ClientContext stream_read_context;
    ni::data_monikers::MonikerList read_request;
    read_request.mutable_read_monikers()->AddAllocated(daqmx_read_moniker);
    auto read_stream = moniker_service.StreamRead(&stream_read_context, read_request);

    // Read data
    for (int i = 0; i < NUM_ITERATIONS; i++) {
      ni::data_monikers::MonikerReadResponse read_data_result;
      if (read_stream->Read(&read_data_result)) {
        google::protobuf::Any read_message = read_data_result.data().values(0);

        MonikerReadAnalogF64Response read_analog_f64_response;
        read_message.UnpackTo(&read_analog_f64_response);
        std::cout << "Read data..." << std::endl;
        print_array(read_analog_f64_response);
      }
      else {
          std::cout << "No data available." << std::endl;
      }
    }

    stream_read_context.TryCancel();

    std::cout << "Cleaning up." << std::endl;

    ::grpc::ClientContext stop_task_context;
    StopTaskRequest stop_task_request;
    stop_task_request.mutable_task()->CopyFrom(daqmx_read_task);
    StopTaskResponse stop_task_response;
    raise_if_error(
      client.StopTask(&stop_task_context, stop_task_request, &stop_task_response),
      stop_task_context);

    ::grpc::ClientContext clear_task_context;
    ClearTaskRequest clear_task_request;
    clear_task_request.mutable_task()->CopyFrom(daqmx_read_task);
    ClearTaskResponse clear_task_response;
    raise_if_error(
      client.ClearTask(&clear_task_context, clear_task_request, &clear_task_response),
      clear_task_context);
  }
  catch (const grpc_driver_error& e) {
    std::string error_message = e.what();

    for (const auto& entry : e.Trailers()) {
      if (entry.first == "ni-error") {
        error_message += "\nError status: " + entry.second;
      }
    }

    if (e.StatusCode() == grpc::StatusCode::UNAVAILABLE) {
      error_message = "Failed to connect to server on " + SERVER_ADDRESS + ":" + SERVER_PORT;
    }
    else if (e.StatusCode() == grpc::StatusCode::UNIMPLEMENTED) {
      error_message = "The operation is not implemented or is not supported/enabled in this service";
    }

    std::cout << "Exception: " << error_message << std::endl;
  }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidcpower/measure-record.py sha256=d5232b6c784dd29d94caa6c7e0f0c5de651407d3cd2d5b53ca50c6307cf4589f bytes=7841 -->
## FILE: examples/nidcpower/measure-record.py

- repository: `ni/grpc-device`
- source_path: `examples/nidcpower/measure-record.py`
- sha256: `d5232b6c784dd29d94caa6c7e0f0c5de651407d3cd2d5b53ca50c6307cf4589f`
- bytes: 7841

````python
r"""Perform continuous measure record.

The gRPC API is built from the C API. NI-DCPower documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDCPower\Documentation\NIDCPowerCref.chm

Getting Started:

To run this example, install "NI-DCPower Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-dcpower.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DCPOWER gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DCPOWER-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python measure-record.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDCPower" as the resource name.
"""

import math
import sys
import time

import grpc
import matplotlib.pyplot as plt
import nidcpower_pb2 as nidcpower_types
import nidcpower_pb2_grpc as grpc_nidcpower
import numpy as np

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-DCPower-Session"

# Resource name, channel name and options for a simulated 4147 client. Change them according to
# NI-DCPower model.
RESOURCE = "SimulatedDCPower"
OPTIONS = "Simulate=1,DriverSetup=Model:4147;BoardType:PXIe"
CHANNELS = "0"

# Parameters
RECORD_LENGTH = 10
BUFFER_MULTIPLIER = 10
VOLTAGE_LEVEL = 5.0

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nidcpower_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message}\nWarning status: {response.status}\n")


# Create the communication channel for the remote host and create connections to the NI-DCPower and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nidcpower.NiDCPowerStub(channel)

try:
    # Initialize the session.
    initialize_with_channels_response = client.InitializeWithChannels(
        nidcpower_types.InitializeWithChannelsRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            channels=CHANNELS,
            reset=False,
            option_string=OPTIONS,
        )
    )
    vi = initialize_with_channels_response.vi

    # Specify when the measure unit should acquire measurements.
    configure_measure_when = client.SetAttributeViInt32(
        nidcpower_types.SetAttributeViInt32Request(
            vi=vi,
            attribute_id=nidcpower_types.NiDCPowerAttribute.NIDCPOWER_ATTRIBUTE_MEASURE_WHEN,
            attribute_value=nidcpower_types.NiDCPowerInt32AttributeValues.NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE,
        )
    )

    # Set the voltage level.
    configure_voltage_level = client.ConfigureVoltageLevel(
        nidcpower_types.ConfigureVoltageLevelRequest(vi=vi, level=VOLTAGE_LEVEL)
    )

    # Specify how many measurements compose a measure record.
    configure_measure_record_length = client.SetAttributeViInt32(
        nidcpower_types.SetAttributeViInt32Request(
            vi=vi,
            attribute_id=nidcpower_types.NiDCPowerAttribute.NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH,
            attribute_value_raw=RECORD_LENGTH,
        )
    )

    # Specify whether to take continuous measurements. Set it to False for continuous measurement.
    configure_measure_record_length_is_finite = client.SetAttributeViBoolean(
        nidcpower_types.SetAttributeViBooleanRequest(
            vi=vi,
            attribute_id=nidcpower_types.NiDCPowerAttribute.NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE,
            attribute_value=False,
        )
    )

    # Commit the session.
    commit_response = client.Commit(
        nidcpower_types.CommitRequest(
            vi=vi,
        )
    )

    # Get measure_record_delta_time.
    get_measure_record_delta_time = client.GetAttributeViReal64(
        nidcpower_types.GetAttributeViReal64Request(
            vi=vi,
            attribute_id=nidcpower_types.NiDCPowerAttribute.NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_DELTA_TIME,
        )
    )

    # Initiate the session.
    initiate_response = client.Initiate(
        nidcpower_types.InitiateRequest(
            vi=vi,
        )
    )
    check_for_warning(initiate_response, vi)

    # Setup a plot to draw the captured waveform.
    fig = plt.figure("Waveform Graph")
    fig.show()
    fig.canvas.draw()

    # Handle closing of plot window.
    closed = False

    def _on_close(event):
        global closed
        closed = True

    fig.canvas.mpl_connect("close_event", _on_close)

    print("\nReading values in loop. CTRL+C or Close window to stop.\n")

    # Create a buffer for fetching the values.
    y_axis = [0.0] * (RECORD_LENGTH * BUFFER_MULTIPLIER)
    x_start = 0

    try:
        while not closed:
            # Clear the plot and setup the axis.
            plt.clf()
            plt.axis()
            plt.xlabel("Samples")
            plt.ylabel("Amplitude")

            fetch_multiple_response = client.FetchMultiple(
                nidcpower_types.FetchMultipleRequest(vi=vi, timeout=10, count=RECORD_LENGTH)
            )
            check_for_warning(fetch_multiple_response, vi)

            # Append the fetched values in the buffer.
            y_axis.extend(fetch_multiple_response.voltage_measurements)
            y_axis = y_axis[RECORD_LENGTH:]

            # Updating the precision of the fetched values.
            y_axis_new = []
            for y_value in y_axis:
                if y_value < VOLTAGE_LEVEL:
                    y_axis_new.append(math.floor(y_value * 100) / 100)
                else:
                    y_axis_new.append(math.ceil(y_value * 100) / 100)

            # Plotting
            y_axis = y_axis_new
            x_axis = np.arange(
                start=x_start, stop=x_start + RECORD_LENGTH * BUFFER_MULTIPLIER, step=1
            )
            x_start = x_start + RECORD_LENGTH
            plt.plot(x_axis, y_axis)
            plt.pause(0.001)
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    print(f"Effective measurement rate : {1 / get_measure_record_delta_time.attribute_value}")

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    if "vi" in vars() and vi.name != "":
        # Close the session.
        client.Close(nidcpower_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidigitalpattern/configure-voltage-levels-and-termination-voltage.py sha256=16473e09885361ea4ed25ffc2c71766416ebd614700fbc78fee727804902af9f bytes=10123 -->
## FILE: examples/nidigitalpattern/configure-voltage-levels-and-termination-voltage.py

- repository: `ni/grpc-device`
- source_path: `examples/nidigitalpattern/configure-voltage-levels-and-termination-voltage.py`
- sha256: `16473e09885361ea4ed25ffc2c71766416ebd614700fbc78fee727804902af9f`
- bytes: 10123

````python
r"""Create an instrument session, configure various voltage levels, and then burst a pattern.

The VOL, VOH, VIH, VIL, VTERM, IOL, IOH, and VCOM values are configurable parameters and the user
can select from High-Z (h), Active Load (a) and Three-Level Drive (t) termination options in
TERM_SELECT.

The gRPC API is built from the C API. NI-Digital Pattern Driver Pattern documentation is installed
with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-Digital-Pattern-Driver\Documentation\Digital Pattern Help.chm

Copy the .pinmap, .specs, .digitiming & .digipat files that come with this example to a folder on
the server machine & copy-paste the path of the folder to the DIRECTORY_PATH variable below.

Use the NI Digital Pattern Editor to create or modify pin or channel map files:
  https://www.ni.com/documentation/en/ni-digital/20.6/digital-pattern-editor/pin-channel-map-editor/

Getting Started:

To run this example, install "NI-Digital Pattern Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-digital-pattern-driver.html#367315

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-Digital Pattern Driver gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DIGITAL-PATTERN-DRIVER-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python configure-voltage-levels-and-termination-voltage.py <server_address> <port_number> <resource>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "PXI1Slot2" as the resource name.
"""  # noqa: W505

import os
import sys

import grpc
import nidigitalpattern_pb2 as nidigital_types
import nidigitalpattern_pb2_grpc as grpc_nidigital

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-Digital-Pattern-Driver-Session"

# Resource and options for a simulated 6570 client. Change them according to the NI-Digital Pattern
# Driver model.
RESOURCE = "PXI1Slot2"
OPTIONS = "Simulate=1, DriverSetup=Model:6570"
# Provide the absolute path to the folder on the server machine containing the .pinmap, .specs,
# .digitiming & .digipat files.
DIRECTORY_PATH = r""
if DIRECTORY_PATH == "":
    print(
        "\nProvide the absolute path to the folder on the server machine containing the .pinmap, .specs, .digitiming & .digipat files to the dirctory_path variable in the source code."
    )
    exit(1)
# Fixed parameters
CHANNEL_LIST = "PinGroup1"

# Configurable parameters
# The voltage that the instrument will apply to the DUT input pin when driving a logic low (0)
VIL = 0
# The voltage that the instrument will apply to the DUT input pin when driving a logic high (1)
VIH = 5
# The voltage below which the instrument pin comparator will interpret a logic low (L)
VOL = 3
# The voltage above which the instrument pin comparator will interpret a logic high (H)
VOH = 2
# The termination voltage the instrument applies during non-drive cycles when the termination mode
# is set to Vterm
VTERM = 5
# The maximum current (A) the DUT sinks while outputting a voltage below VCOM
IOL = 0.015
# The maximum current (A) the DUT sources while outputting a voltage above VCOM
IOH = -0.024
# The commutating voltage level at which the active load circuit switches between sourcing current
# and sinking current
VCOM = 2
# Device termination mode [High-Z (h), Active Load (a), Three-Level Drive (t)]
TERM_SELECT = "h"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create connections to the NI-Digital
# Pattern Driver and session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
nidigital_client = grpc_nidigital.NiDigitalStub(channel)


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nidigital_client.ErrorMessage(
            nidigital_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Open session to NI-Digital Pattern Driver with options
    init_with_options_response = nidigital_client.InitWithOptions(
        nidigital_types.InitWithOptionsRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            id_query=True,
            reset_device=True,
            option_string=OPTIONS,
        )
    )
    vi = init_with_options_response.vi

    load_pin_map_response = nidigital_client.LoadPinMap(
        nidigital_types.LoadPinMapRequest(
            vi=vi,
            file_path=os.path.join(DIRECTORY_PATH, "PinMap.pinmap"),
        )
    )

    load_specification_response = nidigital_client.LoadSpecifications(
        nidigital_types.LoadSpecificationsRequest(
            vi=vi,
            file_path=os.path.join(DIRECTORY_PATH, "Specifications.specs"),
        )
    )

    load_timing_response = nidigital_client.LoadTiming(
        nidigital_types.LoadTimingRequest(
            vi=vi,
            file_path=os.path.join(DIRECTORY_PATH, "Timing.digitiming"),
        )
    )

    load_apply_levels_and_timing_response = nidigital_client.ApplyLevelsAndTiming(
        nidigital_types.ApplyLevelsAndTimingRequest(
            vi=vi,
            site_list="",
            levels_sheet="",
            timing_sheet=os.path.join(DIRECTORY_PATH, "Timing.digitiming"),
            initial_state_high_pins="",
            initial_state_low_pins="",
            initial_state_tristate_pins="",
        )
    )

    load_pattern_response = nidigital_client.LoadPattern(
        nidigital_types.LoadPatternRequest(
            vi=vi,
            file_path=os.path.join(DIRECTORY_PATH, "Pattern.digipat"),
        )
    )

    configure_voltage_response = nidigital_client.ConfigureVoltageLevels(
        nidigital_types.ConfigureVoltageLevelsRequest(
            vi=vi,
            channel_list=CHANNEL_LIST,
            vil=VIL,
            vih=VIH,
            vol=VOL,
            voh=VOH,
            vterm=VTERM,
        )
    )

    if TERM_SELECT == "h":
        configure_termination_mode_response = nidigital_client.ConfigureTerminationMode(
            nidigital_types.ConfigureTerminationModeRequest(
                vi=vi,
                channel_list=CHANNEL_LIST,
                mode=nidigital_types.TerminationMode.TERMINATION_MODE_NIDIGITAL_VAL_HIGH_Z,
            )
        )

    if TERM_SELECT == "a":
        configure_termination_mode_response = nidigital_client.ConfigureTerminationMode(
            nidigital_types.ConfigureTerminationModeRequest(
                vi=vi,
                channel_list=CHANNEL_LIST,
                mode=nidigital_types.TerminationMode.TERMINATION_MODE_NIDIGITAL_VAL_ACTIVE_LOAD,
            )
        )

        configure_active_load_levels_response = nidigital_client.ConfigureActiveLoadLevels(
            nidigital_types.ConfigureActiveLoadLevelsRequest(
                vi=vi,
                channel_list=CHANNEL_LIST,
                iol=IOL,
                ioh=IOH,
                vcom=VCOM,
            )
        )

    if TERM_SELECT == "t":
        configure_termination_mode_response = nidigital_client.ConfigureTerminationMode(
            nidigital_types.ConfigureTerminationModeRequest(
                vi=vi,
                channel_list=CHANNEL_LIST,
                mode=nidigital_types.TerminationMode.TERMINATION_MODE_NIDIGITAL_VAL_VTERM,
            )
        )

    if TERM_SELECT != "h" and TERM_SELECT != "a" and TERM_SELECT != "t":
        print(
            "The value of TERM_SELECT is invalid. Please set it to one of 'h', 'a', or 't' values."
        )
        exit(0)

    burst_pattern_response = nidigital_client.BurstPattern(
        nidigital_types.BurstPatternRequest(
            vi=vi,
            site_list="",
            start_label="new_pattern",
            select_digital_function=True,
            wait_until_done=True,
            timeout=10,
        )
    )
    check_for_warning(burst_pattern_response, vi)

    select_function_response = nidigital_client.SelectFunction(
        nidigital_types.SelectFunctionRequest(
            vi=vi,
            channel_list=CHANNEL_LIST,
            function_raw=nidigital_types.SelectedFunction.SELECTED_FUNCTION_NIDIGITAL_VAL_DISCONNECT,
        )
    )
    check_for_warning(select_function_response, vi)

    print("The NI-Digital Pattern device was configured successfully.\n")

# If NI-Digital Pattern Driver API throws an exception, print the error message
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if "vi" in vars() and vi.name != "":
        # Close NI-Digital Pattern Driver session
        nidigital_client.Close(nidigital_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidigitalpattern/PinMap.pinmap sha256=969c84543eb270861053f8ab34f77d5e6f46801b9789277a18288d44a79ceda6 bytes=1668 -->
## FILE: examples/nidigitalpattern/PinMap.pinmap

- repository: `ni/grpc-device`
- source_path: `examples/nidigitalpattern/PinMap.pinmap`
- sha256: `969c84543eb270861053f8ab34f77d5e6f46801b9789277a18288d44a79ceda6`
- bytes: 1668

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<DUTPin name="DUTPin4" />
		<DUTPin name="DUTPin5" />
		<DUTPin name="DUTPin6" />
		<DUTPin name="DUTPin7" />
		<DUTPin name="DUTPin8" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
			<PinReference pin="DUTPin4" />
			<PinReference pin="DUTPin5" />
			<PinReference pin="DUTPin6" />
			<PinReference pin="DUTPin7" />
			<PinReference pin="DUTPin8" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="DUTPin4" siteNumber="0" instrument="PXI1Slot2" channel="3" />
		<Connection pin="DUTPin5" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="DUTPin6" siteNumber="0" instrument="PXI1Slot2" channel="5" />
		<Connection pin="DUTPin7" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="DUTPin8" siteNumber="0" instrument="PXI1Slot2" channel="7" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidigitalpattern/Specifications.specs sha256=82fcd2afa60bd93a85a9e0d1c43a4b074a33d9be0c8ab8c482e71eebb290a80a bytes=377 -->
## FILE: examples/nidigitalpattern/Specifications.specs

- repository: `ni/grpc-device`
- source_path: `examples/nidigitalpattern/Specifications.specs`
- sha256: `82fcd2afa60bd93a85a9e0d1c43a4b074a33d9be0c8ab8c482e71eebb290a80a`
- bytes: 377

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="timing">
    <f:Formula symbol="period">
      <f:Definition>1 µs</f:Definition>
    </f:Formula>
  </Section>
  <Description />
</Specifications>
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidigitalpattern/Timing.digitiming sha256=11f50499d9e80ba116299c58bdb5fe599cd3f92e74b9575ef7a7e93c7155eeb1 bytes=827 -->
## FILE: examples/nidigitalpattern/Timing.digitiming

- repository: `ni/grpc-device`
- source_path: `examples/nidigitalpattern/Timing.digitiming`
- sha256: `11f50499d9e80ba116299c58bdb5fe599cd3f92e74b9575ef7a7e93c7155eeb1`
- bytes: 827

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="tset0">
        <Period>timing.period</Period>
        <PinEdges>
          <PinEdge pin="PinGroup1">
            <DriveNonReturn>
              <On>0 µs</On>
              <Data>timing.period / 2</Data>
              <Off>timing.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * timing.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nidmm/continuous-acquire-graph-multiple-points.py sha256=96fc453a15cf7780ccd414dffe6538608213c31ac4d008cf65a45bcb6890cda3 bytes=7903 -->
## FILE: examples/nidmm/continuous-acquire-graph-multiple-points.py

- repository: `ni/grpc-device`
- source_path: `examples/nidmm/continuous-acquire-graph-multiple-points.py`
- sha256: `96fc453a15cf7780ccd414dffe6538608213c31ac4d008cf65a45bcb6890cda3`
- bytes: 7903

````python
r"""Perform continuous multipoint acquisition; print the number of points read and average value.

The gRPC API is built from the C API. NI-DMM documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDMM\Documentation\English\DMM.chm

Getting Started:

To run this example, install "NI-DMM Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DMM gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DMM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python continuous-acquire-graph-multiple-points.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDMM" as the resource name.
"""  # noqa: W505

import sys
import time

import grpc
import matplotlib.pyplot as plt
import nidmm_pb2 as nidmm_types
import nidmm_pb2_grpc as grpc_nidmm
import numpy as np

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-DMM-Session"

# Resource name and options for a simulated 4080 client. Change them according to the NI-DMM model.
RESOURCE = "SimulatedDMM"
OPTIONS = "Simulate=1, DriverSetup=Model:4080; BoardType:PXIe"

# parameters
MAX_PTS_TO_READ = 1000
CONFIG_RANGE = 10.0
RESOLUTION = 5.5
MEASUREMENT_TYPE = nidmm_types.Function.FUNCTION_NIDMM_VAL_DC_VOLTS
POWERLINE_FREQ = nidmm_types.PowerLineFrequencies.POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create connections to the NI-DMM and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
nidmm_client = grpc_nidmm.NiDmmStub(channel)


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nidmm_client.GetErrorMessage(
            nidmm_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Open session to NI-DMM with options
    init_with_options_response = nidmm_client.InitWithOptions(
        nidmm_types.InitWithOptionsRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            id_query=False,
            option_string=OPTIONS,
        )
    )
    vi = init_with_options_response.vi

    # Configure measurement
    config_measurement_response = nidmm_client.ConfigureMeasurementDigits(
        nidmm_types.ConfigureMeasurementDigitsRequest(
            vi=vi,
            measurement_function=MEASUREMENT_TYPE,
            range=CONFIG_RANGE,
            resolution_digits=RESOLUTION,
        )
    )

    # Configure a multipoint acquisition
    config_multipoint_response = nidmm_client.ConfigureMultiPoint(
        nidmm_types.ConfigureMultiPointRequest(
            vi=vi,
            trigger_count_raw=1,
            sample_count=nidmm_types.SampleCount.SAMPLE_COUNT_NIDMM_VAL_SAMPLE_COUNT_INFINITE,
            sample_trigger=nidmm_types.SampleTrigger.SAMPLE_TRIGGER_NIDMM_VAL_IMMEDIATE,
            sample_interval_raw=0.0,
        )
    )

    # Configure powerline frequency
    config_powlinefreq_response = nidmm_client.ConfigurePowerLineFrequency(
        nidmm_types.ConfigurePowerLineFrequencyRequest(
            vi=vi,
            power_line_frequency_hz=POWERLINE_FREQ,
        )
    )

    # Initiate Acquisition
    initiate_acquisition_response = nidmm_client.Initiate(nidmm_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_acquisition_response, vi)

    # Set while loop control
    stop_measurement = False

    # initialize variables
    num_measurements = 0
    sum_measurements = 0

    # Setup a plot to draw the captured waveform
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()
    fig.canvas.manager.set_window_title("Measurements")

    # Handle closing of plot window
    closed = False

    def _on_close(event):
        global closed
        closed = True

    fig.canvas.mpl_connect("close_event", _on_close)

    print("\nReading values in loop. CTRL+C or Close window to stop.\n")

    try:
        while not closed:
            pts_available = 0
            # Check available data
            read_status_response = nidmm_client.ReadStatus(nidmm_types.ReadStatusRequest(vi=vi))
            pts_available = read_status_response.acquisition_backlog

            # if there are more than MAX_PTS_TO_READ measurements available, set pts_available to
            # MAX_PTS_TO_READ in order to avoid reallocating the array for measurements
            pts_available = min(pts_available, MAX_PTS_TO_READ)
            if pts_available > 0:
                # Clear the plot and setup the axis
                plt.clf()
                plt.axis()
                plt.xlabel("Samples")
                plt.ylabel("Amplitude")

                # Fetch data
                fetch_multipoints_response = nidmm_client.FetchMultiPoint(
                    nidmm_types.FetchMultiPointRequest(
                        vi=vi,
                        maximum_time_raw=-1,
                        array_size=pts_available,
                    )
                )
                check_for_warning(fetch_multipoints_response, vi)
                num_pts_read = fetch_multipoints_response.actual_number_of_points
                measurements = np.array(fetch_multipoints_response.reading_array)

                # retain data to 2 decimals
                measurements = np.floor(measurements * 100) / 100.0

                # Update the plot with the new measurements
                plt.plot(measurements)
                fig.canvas.draw()
                plt.pause(0.001)

                # Increment number of measurements
                num_measurements += num_pts_read

                # Calculate sum
                for i in range(num_pts_read):
                    sum_measurements += measurements[i]

                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    print(f"Number of measurements = {num_measurements}")
    # Calculate average
    average = sum_measurements / num_measurements
    print(f"Average = {average}")

# If NI-DMM API throws an exception, print the error message
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if "vi" in vars() and vi.name != "":
        # Close NI-DMM session
        nidmm_client.Close(nidmm_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nifgen/basic-arbitrary-waveform.py sha256=39b333f3d2f7f3e2dafc21a84a68de31b0b7f78cdf04f30697fadb271424be37 bytes=6141 -->
## FILE: examples/nifgen/basic-arbitrary-waveform.py

- repository: `ni/grpc-device`
- source_path: `examples/nifgen/basic-arbitrary-waveform.py`
- sha256: `39b333f3d2f7f3e2dafc21a84a68de31b0b7f78cdf04f30697fadb271424be37`
- bytes: 6141

````python
r"""Generate a basic arbitrary waveform with Arbitrary Waveform Mode.

The gRPC API is built from the C API. NI-FGEN documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niFgen\documentation\English\SigGenHelp.chm

Getting Started:

To run this example, install "NI-FGEN Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python basic-arbitrary-waveform.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedFGEN" as the resource name.
"""

import math
import sys

import grpc
import matplotlib.pyplot as plt
import nifgen_pb2 as nifgen_types
import nifgen_pb2_grpc as grpc_nifgen

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-FGEN-Session"

# Resource name and options for a simulated 5441 client. Change them according to the NI-FGEN model.
RESOURCE = "SimulatedFGEN"
OPTIONS = "Simulate=1, DriverSetup=Model:5441; BoardType:PXI"

# parameters
CHANNEL_NAME = "0"
SAMPLE_RATE = 40e6
GAIN = 1.0
DC_OFFSET = 0.0
WAVEFORM_SIZE = 64

# initialize sine waveform data
SINE = [math.sin((i / WAVEFORM_SIZE) * 2 * math.pi) for i in range(WAVEFORM_SIZE)]

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create connections to the NI-FGEN and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
nifgen_client = grpc_nifgen.NiFgenStub(channel)


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nifgen_client.ErrorMessage(
            nifgen_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Initalize NI-FGEN session
    init_with_options_resp = nifgen_client.InitWithOptions(
        nifgen_types.InitWithOptionsRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    vi = init_with_options_resp.vi

    # Configure channels
    config_channels_resp = nifgen_client.ConfigureChannels(
        nifgen_types.ConfigureChannelsRequest(vi=vi, channels=CHANNEL_NAME)
    )

    # Configure output mode
    config_out_resp = nifgen_client.ConfigureOutputMode(
        nifgen_types.ConfigureOutputModeRequest(
            vi=vi,
            output_mode=nifgen_types.OutputMode.OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB,
        )
    )

    # Create waveform
    create_waveform_resp = nifgen_client.CreateWaveformF64(
        nifgen_types.CreateWaveformF64Request(
            vi=vi,
            channel_name=CHANNEL_NAME,
            waveform_data_array=SINE,
        )
    )
    waveform_handle = create_waveform_resp.waveform_handle

    # Configure arbitrary waveform
    config_waveform_resp = nifgen_client.ConfigureArbWaveform(
        nifgen_types.ConfigureArbWaveformRequest(
            vi=vi,
            channel_name=CHANNEL_NAME,
            waveform_handle=waveform_handle,
            gain=GAIN,
            offset=DC_OFFSET,
        )
    )

    # Configure clockmode to VAL_HIGH_RESOLUTION
    config_clckmode_resp = nifgen_client.ConfigureClockMode(
        nifgen_types.ConfigureClockModeRequest(
            vi=vi,
            clock_mode=nifgen_types.ClockMode.CLOCK_MODE_NIFGEN_VAL_HIGH_RESOLUTION,
        )
    )

    # Configure sample rate
    config_sample_rate_resp = nifgen_client.ConfigureSampleRate(
        nifgen_types.ConfigureSampleRateRequest(vi=vi, sample_rate=SAMPLE_RATE)
    )

    # Configure output enabled
    config_outenbl_resp = nifgen_client.ConfigureOutputEnabled(
        nifgen_types.ConfigureOutputEnabledRequest(vi=vi, channel_name=CHANNEL_NAME, enabled=True)
    )

    # Initiate generation
    init_gen_resp = nifgen_client.InitiateGeneration(nifgen_types.InitiateGenerationRequest(vi=vi))
    check_for_warning(init_gen_resp, vi)

    print(f"Generating sine wave at {SAMPLE_RATE} Hz...")
    print("Close the window or press Ctrl+C to stop generation")

    try:
        # Plot the sine wave
        fig = plt.gcf()
        fig.canvas.manager.set_window_title("Sample Waveform")
        plt.plot(SINE)
        plt.suptitle("Close the window to stop generation", fontsize=10)
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.show()
    except KeyboardInterrupt:
        pass

# If NI-FGEN API throws an exception, print the error message
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if "vi" in vars() and vi.name != "":
        # Close NI-FGEN session
        nifgen_client.Close(nifgen_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nifpga/read_write_array_example.py sha256=1196eafe02f20e885d5802da4a1cf0f9ccfab25f0e90b85fdb486af63560533a bytes=4506 -->
## FILE: examples/nifpga/read_write_array_example.py

- repository: `ni/grpc-device`
- source_path: `examples/nifpga/read_write_array_example.py`
- sha256: `1196eafe02f20e885d5802da4a1cf0f9ccfab25f0e90b85fdb486af63560533a`
- bytes: 4506

````python
r"""Read and Write to Arrays.

The gRPC API is built from the C API. NI-FPGA documentation is installed with the driver at:
    C:\Program Files (x86)\National Instruments\FPGA Interface C API\capi.chm

Getting Started:

To run this example with your VI, you need to configure the values below.
Additionally, ensure you have a VI that includes arrays and update the references for them below.
Make sure the R-Series drivers are installed on the system where the gRPC-device server is running.
You will also need LABVIEW and the LABVIEW FPGA module to configure the VIs.

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python read_write_example.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "FPGA" as the resource name.

This example attempts to read and write values to an array.
"""

import sys

import grpc
import nifpga_pb2 as nifpga_types
import nifpga_pb2_grpc as grpc_nifpga

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-FPGA-Session"
RESOURCE = "FPGA"

# Configure these values.
NI_FPGA_EXAMPLE_BITFILE_PATH = "C:\\DemoExample.lvbitx"
NI_FPGA_EXAMPLE_SIGNATURE = "11F1FF1D11F1FF1F1F111FF11F11F111"
EXAMPLE_ARRAY_CONTROL = 0x10004
EXAMPLE_ARRAY_CONTROL_SIZE = 4

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]

channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nifpga.NiFpgaStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        sys.stderr.write(f"Warning status: {response.status}\n")


new_session = None
try:
    open_session_response = client.Open(
        nifpga_types.OpenRequest(
            session_name=SESSION_NAME,
            bitfile=NI_FPGA_EXAMPLE_BITFILE_PATH,
            signature=NI_FPGA_EXAMPLE_SIGNATURE,
            resource=RESOURCE,
            attribute_mapped=nifpga_types.OpenAttribute.OPEN_ATTRIBUTE_NO_RUN,
        )
    )
    new_session = open_session_response.session
    check_for_warning(open_session_response)

    run_response = client.Run(
        nifpga_types.RunRequest(
            session=new_session, attribute=nifpga_types.RunAttribute.RUN_ATTRIBUTE_UNSPECIFIED
        )
    )
    check_for_warning(run_response)

    # Read and Write to an Array
    updated_array = [1, -221, -1111, -21]
    writei32_array_response = client.WriteArrayI32(
        nifpga_types.WriteArrayI32Request(
            session=new_session, control=EXAMPLE_ARRAY_CONTROL, array=updated_array
        )
    )
    check_for_warning(writei32_array_response)

    readi32_array_response = client.ReadArrayI32(
        nifpga_types.ReadArrayI32Request(
            session=new_session,
            indicator=EXAMPLE_ARRAY_CONTROL,
            size=EXAMPLE_ARRAY_CONTROL_SIZE,
        )
    )
    print(f"Updated array value: {readi32_array_response.array}\n")

    abort_response = client.Abort(nifpga_types.AbortRequest(session=new_session))
    check_for_warning(abort_response)

    close_response = client.Close(
        nifpga_types.CloseRequest(
            session=new_session,
            attribute=nifpga_types.CloseAttribute.CLOSE_ATTRIBUTE_UNSPECIFIED,
        )
    )
    check_for_warning(close_response)

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nifpga/read_write_fifo_example.py sha256=683f51059afe1e4c2cac406534187525f158171697243c944ee45fd0ded6e3b0 bytes=5911 -->
## FILE: examples/nifpga/read_write_fifo_example.py

- repository: `ni/grpc-device`
- source_path: `examples/nifpga/read_write_fifo_example.py`
- sha256: `683f51059afe1e4c2cac406534187525f158171697243c944ee45fd0ded6e3b0`
- bytes: 5911

````python
r"""Read and Write to controls and FIFO.

The gRPC API is built from the C API. NI-FPGA documentation is installed with the driver at:
    C:\Program Files (x86)\National Instruments\FPGA Interface C API\capi.chm

Getting Started:

To run this example with your VI, you need to configure the values below.
Additionally, you should have a VI that includes controls and FIFOs, and update the
references for them below. Ensure that the R-Series drivers are installed on the system
where the gRPC-device server is running. You will also need LABVIEW and the LABVIEW FPGA
module to configure the VIs.

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python read_write_example.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "FPGA" as the resource name.

In this example, we specify the number of elements to write to the FIFO and provide
a multiplier as input. We then read elements from another FIFO, which contains the multiplied
values of the elements from the first FIFO.
"""

import random
import sys

import grpc
import nifpga_pb2 as nifpga_types
import nifpga_pb2_grpc as grpc_nifpga

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-FPGA-Session"
RESOURCE = "FPGA"

# Configure these values.
EXAMPLE_BITFILE_PATH = "C:\\DemoExample.lvbitx"
EXAMPLE_SIGNATURE = "11F1FF1D11F1FF1F1F111FF11F11F111"
EXAMPLE_NUMERIC_CONTROL = 0x1000A
EXAMPLE_TARGET_TO_HOST_FIFO = 0
EXAMPLE_HOST_TO_TARGET_FIFO = 1

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]

channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nifpga.NiFpgaStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        sys.stderr.write(f"Warning status: {response.status}\n")


new_session = None
try:
    open_session_response = client.Open(
        nifpga_types.OpenRequest(
            session_name=SESSION_NAME,
            bitfile=EXAMPLE_BITFILE_PATH,
            signature=EXAMPLE_SIGNATURE,
            resource=RESOURCE,
            attribute_mapped=nifpga_types.OpenAttribute.OPEN_ATTRIBUTE_NO_RUN,
        )
    )
    new_session = open_session_response.session
    check_for_warning(open_session_response)

    run_response = client.Run(
        nifpga_types.RunRequest(
            session=new_session, attribute=nifpga_types.RunAttribute.RUN_ATTRIBUTE_UNSPECIFIED
        )
    )
    check_for_warning(run_response)

    # Read and Write to FIFO
    # These two FIFOs are configured such that we specify the number of elements
    # to add to the FIFO and the multiplier.
    # The other FIFO will contain the multiplied value of the elements of the firsts FIFO.
    user_input = int(
        input("Enter number of elements you want to add in the FIFO (between 1 and 20): ")
    )
    random_numbers = []
    if 1 <= user_input <= 20:
        for _ in range(user_input):
            random_number = random.randint(1, 100)
            random_numbers.append(random_number)
        print(f"Random numbers: {random_numbers}\n")
    else:
        print("Invalid input. Please enter a number between 1 and 20.")

    multiplier_input = int(
        input("Enter the multiplier you want the FIFO elements to get multplied with: ")
    )

    i16_write_response = client.WriteI16(
        nifpga_types.WriteI16Request(
            session=new_session,
            control=EXAMPLE_NUMERIC_CONTROL,
            value=multiplier_input,
        )
    )
    InfiniteTimeout = 0xFFFFFFFF
    writefifoi16_response = client.WriteFifoI16(
        nifpga_types.WriteFifoI16Request(
            session=new_session,
            fifo=EXAMPLE_HOST_TO_TARGET_FIFO,
            data=random_numbers,
            timeout=InfiniteTimeout,
        )
    )
    check_for_warning(writefifoi16_response)

    readfifoi16_response = client.ReadFifoI16(
        nifpga_types.ReadFifoI16Request(
            session=new_session,
            fifo=EXAMPLE_TARGET_TO_HOST_FIFO,
            number_of_elements=user_input,
            timeout=InfiniteTimeout,
        )
    )
    print(f"Elements in FIFO: {readfifoi16_response.data}\n")
    print(f"Elements remaining to read from FIFO: {readfifoi16_response.elements_remaining}\n")

    abort_response = client.Abort(nifpga_types.AbortRequest(session=new_session))
    check_for_warning(abort_response)

    close_response = client.Close(
        nifpga_types.CloseRequest(
            session=new_session,
            attribute=nifpga_types.CloseAttribute.CLOSE_ATTRIBUTE_UNSPECIFIED,
        )
    )
    check_for_warning(close_response)

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirf/rfsa-rfsg-NR-analysis-only-modacc.py sha256=d6b9b7e9689470f62f3c52e817da0e945425b94a4bcb66c52c7fe61f9c94868e bytes=16141 -->
## FILE: examples/nirf/rfsa-rfsg-NR-analysis-only-modacc.py

- repository: `ni/grpc-device`
- source_path: `examples/nirf/rfsa-rfsg-NR-analysis-only-modacc.py`
- sha256: `d6b9b7e9689470f62f3c52e817da0e945425b94a4bcb66c52c7fe61f9c94868e`
- bytes: 16141

````python
r"""Demonstration on how to use RFSA, RFSG and RFmx in Analysis Only mode.

This example shows how to generate a TDMS waveform using RFSG, to capture the raw IQ data using
RFSA and to demodulate it using RFmx Analysis Only mode.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSA.chm

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR", "RFSA" and "RFSG" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html


For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python rfsa-rfsg-NR-analysis-only-modacc.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nidevice_pb2 as nidevice_grpc
import nirfmxinstr_pb2 as nirfmxinstr_types
import nirfmxinstr_pb2_grpc as grpc_nirfmxinstr
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr
import nirfsa_pb2 as nirfsa_types
import nirfsa_pb2_grpc as grpc_nirfsa
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
RFMXSESSION_NAME = "RFmxNRSession"
RFSASESSION_NAME = "RfsaSession"
RFSGSESSION_NAME = "RfsgSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "5840_1"
RFMXOPTIONS = "AnalysisOnly=1"
RFSAOPTIONS = "DriverSetup=SFPSessionAccess:1"
RFSGOPTIONS = ""

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""
# Create a gRPC channel + client.
# Use a larger buffer for the messages as we are transferring the raw data from instrument.
# In this example up to 1.6M samples
options = [("grpc.max_receive_message_length", 2**21)]
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}", options=options)
rfmxclient = grpc_nirfmxnr.NiRFmxNRStub(channel)
rfsaclient = grpc_nirfsa.NiRFSAStub(channel)
rfsgclient = grpc_nirfsg.NiRFSGStub(channel)
instrclient = grpc_nirfmxinstr.NiRFmxInstrStub(channel)
rfsgsession = None
rfmxsession = None
rfsasession = None


def raise_if_initialization_error(response):
    """Raise an exception if an error was returned from Initialize."""
    if response.status < 0:
        raise RuntimeError(f"Error: {response.error_message or response.status}")
    if response.status > 0:
        sys.stderr.write(f"Warning: {response.error_message or response.status}\n")
    return response


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = rfmxclient.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    print(f"Initializing Instruments...", end="")
    initialize_rfmx_response = rfmxclient.Initialize(
        nirfmxnr_types.InitializeRequest(
            session_name=RFMXSESSION_NAME,
            resource_name=RESOURCE,
            option_string=RFMXOPTIONS,
        )
    )

    rfmxsession = initialize_rfmx_response.instrument

    initialize_rfsa_response = rfsaclient.InitWithOptions(
        nirfsa_types.InitWithOptionsRequest(
            session_name=RFSASESSION_NAME,
            resource_name=RESOURCE,
            option_string=RFSAOPTIONS,
        )
    )

    rfsasession = initialize_rfsa_response.vi

    initialize_rfsg_response = rfsgclient.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=RFSGSESSION_NAME,
            resource_name=RESOURCE,
            option_string=RFSGOPTIONS,
        )
    )

    rfsgsession = initialize_rfsg_response.vi
    print("Done")

    center_frequency = 3.5e9
    reference_level_dbm = 0
    power_level_dbm = -10
    rfsg_script = "script GenerateWaveform  repeat forever generate waveform end repeat end script"
    rfsg_waveform_name = "waveform"
    # The following waveform is installed with RFmx NR
    file_path = r"C:\Users\Public\Documents\National Instruments\NI-RFmx\NR\Examples\C\Support\NR_FR1_UL_BW-100MHz_SCS-30kHz.tdms"

    print(f"Configuring RFmx NR, RFSG and RFSA settings...", end="")
    ###### Configure RFSA Settings ######
    rfsaclient.ConfigureRefClock(
        nirfsa_types.ConfigureRefClockRequest(
            vi=rfsasession,
            clock_source_mapped=nirfsa_types.RefClockSource.REF_CLOCK_SOURCE_ONBOARD_CLOCK,
            ref_clock_rate=10e6,
        )
    )
    rfsaclient.ConfigureReferenceLevel(
        nirfsa_types.ConfigureReferenceLevelRequest(
            vi=rfsasession, reference_level=reference_level_dbm
        )
    )
    rfsaclient.ConfigureAcquisitionType(
        nirfsa_types.ConfigureAcquisitionTypeRequest(
            vi=rfsasession,
            acquisition_type=nirfsa_types.AcquisitionType.ACQUISITION_TYPE_IQ,
        )
    )
    rfsaclient.ConfigureIQCarrierFrequency(
        nirfsa_types.ConfigureIQCarrierFrequencyRequest(
            vi=rfsasession, carrier_frequency=center_frequency
        )
    )
    ###### Configure RFSG Settings ######
    rfsgclient.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=rfsgsession,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_POWER_LEVEL,
            value_raw=power_level_dbm,
        )
    )
    rfsgclient.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=rfsgsession,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_FREQUENCY,
            value_raw=center_frequency,
        )
    )
    rfsgclient.ConfigureGenerationMode(
        nirfsg_types.ConfigureGenerationModeRequest(
            vi=rfsgsession, generation_mode=nirfsg_types.GENERATION_MODE_SCRIPT
        )
    )
    rfsgclient.ReadAndDownloadWaveformFromFileTDMS(
        nirfsg_types.ReadAndDownloadWaveformFromFileTDMSRequest(
            vi=rfsgsession,
            waveform_name=rfsg_waveform_name,
            file_path=str(file_path),
            waveform_index=0,
        )
    )
    rfsgclient.WriteScript(nirfsg_types.WriteScriptRequest(vi=rfsgsession, script=rfsg_script))
    rfsgclient.ExportSignal(
        nirfsg_types.ExportSignalRequest(
            vi=rfsgsession,
            signal=nirfsg_types.ROUTED_SIGNAL_MARKER_EVENT,
            signal_identifier_mapped=nirfsg_types.SIGNAL_IDENTIFIER_MARKER0,
            output_terminal_mapped=nirfsg_types.OUTPUT_SIGNAL_PXI_TRIG1,
        )
    )

    ###### Configure NR Settings ######
    nr_frequency_range = nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1
    nr_carrier_bandwidth = 100e6
    nr_subcarrier_spacing = 30e3
    nr_auto_resource_block_detection_enabled = True
    nr_pusch_modulation_type = nirfmxnr_types.NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QAM64
    nr_measurement_length_unit = nirfmxnr_types.NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT
    nr_link_direction = nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK
    nr_measurement_offset = 0
    nr_measurement_length = 1
    rfmxclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val=nr_link_direction,
        )
    )
    rfmxclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
            attr_val=nr_frequency_range,
        )
    )
    rfmxclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
            attr_val=nr_carrier_bandwidth,
        )
    )
    rfmxclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
            attr_val=nr_subcarrier_spacing,
        )
    )
    rfmxclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_MODULATION_TYPE,
            attr_val=nr_pusch_modulation_type,
        )
    )
    rfmxclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT,
            attr_val=nr_measurement_length_unit,
        )
    )
    rfmxclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET,
            attr_val=nr_measurement_offset,
        )
    )
    rfmxclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=rfmxsession,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH,
            attr_val=nr_measurement_length,
        )
    )
    rfmxclient.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=rfmxsession,
            selector_string="",
            measurements=nirfmxnr_types.MEASUREMENT_TYPES_MODACC,
            enable_all_traces=False,
        )
    )
    rfmxclient.Commit(
        nirfmxnr_types.CommitRequest(
            instrument=rfmxsession,
            selector_string="",
        )
    )
    # Once commit is called, the recommended acquisition settings can be queried
    response = instrclient.GetAttributeF64(
        nirfmxinstr_types.GetAttributeF64Request(
            instrument=rfmxsession,
            channel_name="",
            attribute_id=nirfmxinstr_types.NIRFMXINSTR_ATTRIBUTE_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE,
        )
    )
    minimum_sample_rate = response.attr_val
    response = instrclient.GetAttributeF64(
        nirfmxinstr_types.GetAttributeF64Request(
            instrument=rfmxsession,
            channel_name="",
            attribute_id=nirfmxinstr_types.NIRFMXINSTR_ATTRIBUTE_RECOMMENDED_IQ_ACQUISITION_TIME,
        )
    )
    acquisition_time = response.attr_val
    number_of_samples = acquisition_time * minimum_sample_rate
    response = instrclient.GetAttributeF64(
        nirfmxinstr_types.GetAttributeF64Request(
            instrument=rfmxsession,
            channel_name="",
            attribute_id=nirfmxinstr_types.NIRFMXINSTR_ATTRIBUTE_RECOMMENDED_IQ_PRE_TRIGGER_TIME,
        )
    )
    pre_trigger_time = response.attr_val
    number_of_pre_samples = pre_trigger_time * minimum_sample_rate
    response32 = instrclient.GetAttributeI32(
        nirfmxinstr_types.GetAttributeI32Request(
            instrument=rfmxsession,
            channel_name="",
            attribute_id=nirfmxinstr_types.NIRFMXINSTR_ATTRIBUTE_RECOMMENDED_NUMBER_OF_RECORDS,
        )
    )
    number_of_records = response32.attr_val

    # Configure RFSA Acquisition Settings
    rfsaclient.ConfigureNumberOfSamples(
        nirfsa_types.ConfigureNumberOfSamplesRequest(
            vi=rfsasession,
            number_of_samples_is_finite=True,
            samples_per_record=int(number_of_samples),
        )
    )
    rfsaclient.ConfigureIQRate(
        nirfsa_types.ConfigureIQRateRequest(vi=rfsasession, iq_rate=minimum_sample_rate)
    )
    print(f"Done")
    print(f"Starting Generation...", end="")
    rfsgclient.Initiate(nirfsg_types.InitiateRequest(vi=rfsgsession))
    print("Generating")
    print("Starting Acquisition and Analysis Loop:")

    ###### Start Acquisition and AO Analyze ######
    rfsaclient.Initiate(nirfsa_types.InitiateRequest(vi=rfsasession))
    for record in range(number_of_records):
        read_response = rfsaclient.FetchIQSingleRecordComplexF32(
            nirfsa_types.FetchIQSingleRecordComplexF32Request(
                vi=rfsasession,
                channel_list="",
                record_number=record,
                number_of_samples=int(number_of_samples),
                timeout=10.0,
            )
        )

        iq = [
            nidevice_grpc.NIComplexNumberF32(real=sample.real, imaginary=sample.imaginary)
            for sample in read_response.data
        ]

        ###### Feed IQ Data to Analysis Only ######
        rfmxclient.AnalyzeIQ1Waveform(
            nirfmxnr_types.AnalyzeIQ1WaveformRequest(
                instrument=rfmxsession,
                selector_string="",
                result_name="",
                x0=read_response.wfm_info.relative_initial_x,
                dx=read_response.wfm_info.x_increment,
                iq=iq,
                reset=True,
            )
        )
    ###### Fetch ModAcc results ######
    modacc_fetch_measurement = rfmxclient.ModAccFetchCompositeEVM(
        nirfmxnr_types.ModAccFetchCompositeEVMRequest(
            instrument=rfmxsession, selector_string="", timeout=10.0
        )
    )
    print(modacc_fetch_measurement)
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if rfmxsession:
        rfmxclient.Close(nirfmxnr_types.CloseRequest(instrument=rfmxsession, force_destroy=True))
    if rfsasession:
        rfsaclient.Close(nirfsa_types.CloseRequest(vi=rfsasession))
    if rfsgsession:
        rfsgclient.Abort(nirfsg_types.AbortRequest(vi=rfsgsession))
        rfsgclient.Close(nirfsg_types.CloseRequest(vi=rfsgsession))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirf/specan-nr-txp-example.py sha256=ec7b4c2e0c41c5221ac8be9a6cae73ae885c31502b4881b2996a5ee3ccd31f65 bytes=12182 -->
## FILE: examples/nirf/specan-nr-txp-example.py

- repository: `ni/grpc-device`
- source_path: `examples/nirf/specan-nr-txp-example.py`
- sha256: `ec7b4c2e0c41c5221ac8be9a6cae73ae885c31502b4881b2996a5ee3ccd31f65`
- bytes: 12182

````python
r"""Multi Rfmx Personality Example with SpecAn and NR.

Steps:
  1. Open only one RFmx Session. No need to open every personality.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  5. Configure Link Direction, Frequency Range, Carrier Bandwidthand Subcarrier Spacing.
  6. Select NR TXP and SpecAn TXP measurement and enable Traces.
  7. Configure Measurement Offset & Measurement Length Parameters and Averaging Parameters for TXP
     measurement.
  9. Initiate NR Measurement.
  10. Fetch NR Measurements and Traces.
  11. Initiate SpecAn Measurement.
  12. Fetch SpecAn Measurements and Traces.
  13. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxinstr_pb2 as nirfmxinstr_types
import nirfmxinstr_pb2_grpc as grpc_nirfmxinstr
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr
import nirfmxspecan_pb2 as nirfmxspecan_types
import nirfmxspecan_pb2_grpc as grpc_nirfmxspecan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxNRSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "5840_1"
OPTIONS = ""

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""
# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
instrclient = grpc_nirfmxinstr.NiRFmxInstrStub(channel)
nrclient = grpc_nirfmxnr.NiRFmxNRStub(channel)
specanclient = grpc_nirfmxspecan.NiRFmxSpecAnStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nrclient.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Only one personality needs to be initialized. The return session, can be used across all
    # other personalities
    initialize_response = instrclient.Initialize(
        nirfmxinstr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    # Configure RfInstr reference clock
    instrclient.CfgFrequencyReference(
        nirfmxinstr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxinstr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    # Configure and test NR
    nrclient.SetAttributeString(
        nirfmxnr_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    nrclient.CfgRF(
        nirfmxnr_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=3.5e9,
            reference_level=0.0,
            external_attenuation=0.0,
        )
    )

    nrclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK,
        )
    )

    nrclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1,
        )
    )

    nrclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
            attr_val=20e6,
        )
    )

    nrclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
            attr_val=30e3,
        )
    )

    nrclient.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxnr_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    nrclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_INTERVAL,
            attr_val=1.0e-3,
        )
    )

    nrclient.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_OFFSET,
            attr_val=0.0,
        )
    )

    nrclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_TRUE,
        )
    )

    nrclient.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_COUNT,
            attr_val_raw=10,
        )
    )

    initiate_response = nrclient.Initiate(
        nirfmxnr_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)
    ### Fetch NR TXP results ###

    txp_fetch_measurement_response = nrclient.TXPFetchMeasurement(
        nirfmxnr_types.TXPFetchMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_measurement_response, instr)
    avearge_power_mean = txp_fetch_measurement_response.average_power_mean
    peak_power_maximum = txp_fetch_measurement_response.peak_power_maximum

    txp_fetch_power_trace_response = nrclient.TXPFetchPowerTrace(
        nirfmxnr_types.TXPFetchPowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_power_trace_response, instr)
    x0 = txp_fetch_power_trace_response.x0
    dx = txp_fetch_power_trace_response.dx
    power = txp_fetch_power_trace_response.power

    print("\n------------NR TXP Measurement------------\n")
    print(f"Average Power Mean (dBm) : {avearge_power_mean}")
    print(f"Peak Power Maximum (dBm) : {peak_power_maximum}")

    # Configure and test SpecAn TXP
    specanclient.SetAttributeString(
        nirfmxspecan_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxspecan_types.NIRFMXSPECAN_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    specanclient.CfgRF(
        nirfmxspecan_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )

    specanclient.TXPCfgMeasurementInterval(
        nirfmxspecan_types.TXPCfgMeasurementIntervalRequest(
            instrument=instr,
            selector_string="",
            measurement_interval=1e-3,
        )
    )

    specanclient.TXPCfgRBWFilter(
        nirfmxspecan_types.TXPCfgRBWFilterRequest(
            instrument=instr,
            selector_string="",
            rbw=100e3,
            rbw_filter_type=nirfmxspecan_types.TXP_RBW_FILTER_TYPE_GAUSSIAN,
            rrc_alpha=0.1,
        )
    )

    specanclient.TXPCfgAveraging(
        nirfmxspecan_types.TXPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxspecan_types.TXP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxspecan_types.TXP_AVERAGING_TYPE_RMS,
        )
    )

    ### Fetch SpecAn measurement data ###

    txp_read_response = specanclient.TXPRead(
        nirfmxspecan_types.TXPReadRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_read_response, instr)

    minimum_power = txp_read_response.minimum_power
    maximum_power = txp_read_response.maximum_power
    peak_to_average_ratio = txp_read_response.peak_to_average_ratio
    average_mean_power = txp_read_response.average_mean_power

    print("\n------------SpecAn TXP Measurement------------\n")
    print(f"Average Mean Power(dBm)    {average_mean_power}")
    print(f"Peak to Average Ratio(dB)  {peak_to_average_ratio}")
    print(f"Maximum Power(dBm)         {maximum_power}")
    print(f"Minimum Power(dBm)         {minimum_power}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        instrclient.Close(
            # Only one session can be closed and using any personality
            nirfmxinstr_types.CloseRequest(instrument=instr, force_destroy=False)
        )
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxbluetooth/acp-basic.py sha256=53b4b0c7a38e038e6ef11d5041a4bcef32666bcc4d0ceb5859bee4e70e6e3a9a bytes=13020 -->
## FILE: examples/nirfmxbluetooth/acp-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxbluetooth/acp-basic.py`
- sha256: `53b4b0c7a38e038e6ef11d5041a4bcef32666bcc4d0ceb5859bee4e70e6e3a9a`
- bytes: 13020

````python
r"""Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Packet Type.
  6. Configure Data Rate.
  7. Configure Payload Length.
  8. Select ACP measurement and enable Traces.
  9. Configure ACP Burst Sync Type.
  10. Configure Averaging Parameters for ACP measurement.
  11. Configure Number of Offsets or Channel Number depending on Offset Channel Mode.
  12. Initiate the Measurement.
  13. Fetch ACP Measurements and Trace.
  14. Close RFmx Session.

The gRPC API is built from the C API. RFmx Bluetooth documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\BT\Documentation\rfmxbtcvi.chm

Getting Started:

To run this example, install "RFmx Bluetooth" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-bluetooth.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxBluetooth gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxBluetooth-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxbluetooth_pb2 as nirfmxbluetooth_types
import nirfmxbluetooth_pb2_grpc as grpc_nirfmxbluetooth

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxBluetoothSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxbluetooth.NiRFmxBluetoothStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxbluetooth_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    offset_channel_mode = nirfmxbluetooth_types.ACP_OFFSET_CHANNEL_MODE_SYMMETRIC

    initialize_response = client.Initialize(
        nirfmxbluetooth_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxbluetooth_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxbluetooth_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgRF(
        nirfmxbluetooth_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.402e9,
            reference_level=0.0,
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxbluetooth_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxbluetooth_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxbluetooth_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=100e-6,
            iq_power_edge_level_type=nirfmxbluetooth_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=False,
        )
    )

    client.CfgPacketType(
        nirfmxbluetooth_types.CfgPacketTypeRequest(
            instrument=instr,
            selector_string="",
            packet_type=nirfmxbluetooth_types.PACKET_TYPE_DH1,
        )
    )

    client.CfgDataRate(
        nirfmxbluetooth_types.CfgDataRateRequest(
            instrument=instr, selector_string="", data_rate=1000000
        )
    )

    client.CfgPayloadLength(
        nirfmxbluetooth_types.CfgPayloadLengthRequest(
            instrument=instr,
            selector_string="",
            payload_length_mode=nirfmxbluetooth_types.PAYLOAD_LENGTH_MODE_AUTO,
            payload_length=10,
        )
    )

    client.SelectMeasurements(
        nirfmxbluetooth_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxbluetooth_types.MEASUREMENT_TYPES_ACP,
            enable_all_traces=True,
        )
    )

    client.ACPCfgBurstSynchronizationType(
        nirfmxbluetooth_types.ACPCfgBurstSynchronizationTypeRequest(
            instrument=instr,
            selector_string="",
            burst_synchronization_type=nirfmxbluetooth_types.ACP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE,
        )
    )

    client.ACPCfgAveraging(
        nirfmxbluetooth_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxbluetooth_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    client.ACPCfgOffsetChannelMode(
        nirfmxbluetooth_types.ACPCfgOffsetChannelModeRequest(
            instrument=instr,
            selector_string="",
            offset_channel_mode=offset_channel_mode,
        )
    )

    if offset_channel_mode == nirfmxbluetooth_types.ACP_OFFSET_CHANNEL_MODE_SYMMETRIC:
        client.ACPCfgNumberOfOffsets(
            nirfmxbluetooth_types.ACPCfgNumberOfOffsetsRequest(
                instrument=instr,
                selector_string="",
                number_of_offsets=5,
            )
        )

    elif offset_channel_mode == nirfmxbluetooth_types.ACP_OFFSET_CHANNEL_MODE_INBAND:
        client.CfgChannelNumber(
            nirfmxbluetooth_types.CfgChannelNumberRequest(
                instrument=instr,
                selector_string="",
                channel_number=0,
            )
        )

    initiate_response = client.Initiate(
        nirfmxbluetooth_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch Results ###
    acp_fetch_measurement_status_response = client.ACPFetchMeasurementStatus(
        nirfmxbluetooth_types.ACPFetchMeasurementStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_measurement_status_response, instr)
    measurement_status = acp_fetch_measurement_status_response.measurement_status

    if (
        measurement_status
        == nirfmxbluetooth_types.NIRFMXBLUETOOTH_INT32_ACP_RESULTS_MEASUREMENT_STATUS_NOT_APPLICABLE
    ):
        measurement_status_string = "Not Applicable"
    elif (
        measurement_status
        == nirfmxbluetooth_types.NIRFMXBLUETOOTH_INT32_ACP_RESULTS_MEASUREMENT_STATUS_PASS
    ):
        measurement_status_string = "Pass"
    else:
        measurement_status_string = "Fail"

    acp_fetch_reference_channel_power_response = client.ACPFetchReferenceChannelPower(
        nirfmxbluetooth_types.ACPFetchReferenceChannelPowerRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_reference_channel_power_response, instr)
    reference_channel_power = acp_fetch_reference_channel_power_response.reference_channel_power

    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxbluetooth_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)

    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power
    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_margin = acp_fetch_offset_measurement_array_response.lower_margin
    upper_margin = acp_fetch_offset_measurement_array_response.upper_margin

    acp_fetch_mask_trace_response = client.ACPFetchMaskTrace(
        nirfmxbluetooth_types.ACPFetchMaskTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_mask_trace_response, instr)

    x0 = acp_fetch_mask_trace_response.x0
    dx = acp_fetch_mask_trace_response.dx
    limit_with_exception_mask = acp_fetch_mask_trace_response.limit_with_exception_mask
    limit_without_exception_mask = acp_fetch_mask_trace_response.limit_without_exception_mask

    x0 = 0.0
    dx = 0.0
    acp_fetch_absolute_power_trace_response = client.ACPFetchAbsolutePowerTrace(
        nirfmxbluetooth_types.ACPFetchAbsolutePowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_absolute_power_trace_response, instr)
    x0 = acp_fetch_absolute_power_trace_response.x0
    dx = acp_fetch_absolute_power_trace_response.dx
    absolute_power = acp_fetch_absolute_power_trace_response.absolute_power

    x0 = 0.0
    dx = 0.0
    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxbluetooth_types.ACPFetchSpectrumRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    print("------------------ACP------------------")
    print(f"Measurement Status                   : {measurement_status_string}")
    print(f"Reference Channel Power (dBm)        : {reference_channel_power}\n")
    print("------------------Offset Measurements------------------")
    if len(lower_absolute_power) == 0:
        print("No data")
    for i in range(len(lower_absolute_power)):
        print(f"Offset {i}")
        print(f"Lower Absolute Powers (dBm)          : {lower_absolute_power[i]}")
        print(f"Upper Absolute Powers (dBm)          : {upper_absolute_power[i]}")
        print(f"Lower Relative Powers (dB)           : {lower_relative_power[i]}")
        print(f"Upper Relative Powers (dB)           : {upper_relative_power[i]}")
        # Lower and Upper margin results are not applicable for ACP_OFFSET_CHANNEL_MODE_SYMMETRIC.
        if offset_channel_mode != nirfmxbluetooth_types.ACP_OFFSET_CHANNEL_MODE_SYMMETRIC:
            print(f"Lower Margin (dB)                    : {lower_margin[i]}")
            print(f"Upper Margin (dB)                    : {upper_margin[i]}\n")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxbluetooth_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxbluetooth/txp-basic.py sha256=a02001d6ac7d5046472daedec4e026b7d5fe12c20895741687f172eaef4d03ce bytes=13293 -->
## FILE: examples/nirfmxbluetooth/txp-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxbluetooth/txp-basic.py`
- sha256: `a02001d6ac7d5046472daedec4e026b7d5fe12c20895741687f172eaef4d03ce`
- bytes: 13293

````python
r"""Fetch TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Packet Type.
  6. Configure Data Rate.
  7. Configure Payload Length.
  8. Configure Direction Finding.
  9. Configure Reference Level.
  10. Select TXP measurement and enable Traces.
  11. Configure TXP Burst Synchronization Type.
  12. Configure Averaging Parameters for TXP measurement.
  13. Initiate the Measurement.
  14. Fetch TXP Measurements and Trace.
  15. Close RFmx Session.

The gRPC API is built from the C API. RFmx Bluetooth documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\BT\Documentation\rfmxbtcvi.chm

Getting Started:

To run this example, install "RFmx Bluetooth" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-bluetooth.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxBluetooth gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxBluetooth-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxbluetooth_pb2 as nirfmxbluetooth_types
import nirfmxbluetooth_pb2_grpc as grpc_nirfmxbluetooth

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxBluetoothSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    resource = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxbluetooth.NiRFmxBluetoothStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxbluetooth_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True
    basic_rate_packets = True

    initialize_response = client.Initialize(
        nirfmxbluetooth_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxbluetooth_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxbluetooth_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxbluetooth_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.402000e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxbluetooth_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxbluetooth_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxbluetooth_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxbluetooth_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=100e-6,
            iq_power_edge_level_type=nirfmxbluetooth_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=False,
        )
    )

    client.CfgPacketType(
        nirfmxbluetooth_types.CfgPacketTypeRequest(
            instrument=instr,
            selector_string="",
            packet_type=nirfmxbluetooth_types.PACKET_TYPE_DH1,
        )
    )

    client.CfgDataRate(
        nirfmxbluetooth_types.CfgDataRateRequest(
            instrument=instr,
            selector_string="",
            data_rate=1000000,
        )
    )

    client.CfgPayloadLength(
        nirfmxbluetooth_types.CfgPayloadLengthRequest(
            instrument=instr,
            selector_string="",
            payload_length_mode=nirfmxbluetooth_types.PAYLOAD_LENGTH_MODE_AUTO,
            payload_length=10,
        )
    )

    client.CfgLEDirectionFinding(
        nirfmxbluetooth_types.CfgLEDirectionFindingRequest(
            instrument=instr,
            selector_string="",
            direction_finding_mode=nirfmxbluetooth_types.DIRECTION_FINDING_MODE_DISABLED,
            cte_length=160e-6,
            cte_slot_duration=1e-6,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxbluetooth_types.AutoLevelRequest(
                instrument=instr,
                selector_string="",
                measurement_interval=10e-3,
            )
        )
        reference_level = auto_level_response.reference_level
    else:
        client.CfgReferenceLevel(
            nirfmxbluetooth_types.CfgReferenceLevelRequest(
                instrument=instr,
                selector_string="",
                reference_level=0.0,
            )
        )

    client.SelectMeasurements(
        nirfmxbluetooth_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxbluetooth_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    client.TXPCfgBurstSynchronizationType(
        nirfmxbluetooth_types.TXPCfgBurstSynchronizationTypeRequest(
            instrument=instr,
            selector_string="",
            burst_synchronization_type=nirfmxbluetooth_types.TXP_BURST_SYNCHRONIZATION_TYPE_NONE,
        )
    )

    client.TXPCfgAveraging(
        nirfmxbluetooth_types.TXPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxbluetooth_types.TXP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxbluetooth_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch Results ###

    txp_fetch_powers_response = client.TXPFetchPowers(
        nirfmxbluetooth_types.TXPFetchPowersRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_powers_response, instr)
    average_power_mean = txp_fetch_powers_response.average_power_mean
    average_power_maximum = txp_fetch_powers_response.average_power_maximum
    average_power_minimum = txp_fetch_powers_response.average_power_minimum
    peak_to_average_power_ratio_maximum = (
        txp_fetch_powers_response.peak_to_average_power_ratio_maximum
    )

    txp_fetch_edr_powers_response = client.TXPFetchEDRPowers(
        nirfmxbluetooth_types.TXPFetchEDRPowersRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_edr_powers_response, instr)
    edrgfsk_average_power_mean = txp_fetch_edr_powers_response.edr_gfsk_average_power_mean
    edrdpsk_average_power_mean = txp_fetch_edr_powers_response.edr_dpsk_average_power_mean
    edr_dpsk_gfsk_average_power_ratio_mean = (
        txp_fetch_edr_powers_response.edr_dpsk_gfsk_average_power_ratio_mean
    )

    txp_fetch_lecte_reference_period_powers_response = client.TXPFetchLECTEReferencePeriodPowers(
        nirfmxbluetooth_types.TXPFetchLECTEReferencePeriodPowersRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_lecte_reference_period_powers_response, instr)
    reference_period_average_power_mean = (
        txp_fetch_lecte_reference_period_powers_response.reference_period_average_power_mean
    )
    reference_period_peak_absolute_power_deviation_maximum = (
        txp_fetch_lecte_reference_period_powers_response.reference_period_peak_absolute_power_deviation_maximum
    )

    txp_fetch_lecte_transmit_slot_powers_response = client.TXPFetchLECTETransmitSlotPowersArray(
        nirfmxbluetooth_types.TXPFetchLECTETransmitSlotPowersArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_lecte_transmit_slot_powers_response, instr)
    transmit_slot_average_power_mean = (
        txp_fetch_lecte_transmit_slot_powers_response.transmit_slot_average_power_mean
    )
    transmit_slot_peak_absolute_power_deviation_maximum = (
        txp_fetch_lecte_transmit_slot_powers_response.transmit_slot_peak_absolute_power_deviation_maximum
    )

    txp_fetch_power_trace_response = client.TXPFetchPowerTrace(
        nirfmxbluetooth_types.TXPFetchPowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_power_trace_response, instr)
    x0 = txp_fetch_power_trace_response.x0
    dx = txp_fetch_power_trace_response.dx
    power = txp_fetch_power_trace_response.power

    print("------------------Measurement------------------")
    print(f"Average Power Mean (dBm)                        : {average_power_mean}")
    print(f"Average Power Maximum (dBm)                     : {average_power_maximum}")
    print(f"Average Power Minimum (dBm)                     : {average_power_minimum}")
    print(
        f"Peak to Average Power Ratio Maximum (dB)        : {peak_to_average_power_ratio_maximum}"
    )

    # These results are invalid for basic rate packets.
    if not basic_rate_packets:
        print(f"EDR GFSK Average Power Mean (dBm)               : {edrgfsk_average_power_mean}")
        print(f"EDR DPSK Average Power Mean (dBm)               : {edrdpsk_average_power_mean}")
        print(
            f"EDR DPSK GFSK Average Power Ratio Mean (dB)     : {edr_dpsk_gfsk_average_power_ratio_mean}"
        )

    # These results are invalid for basic rate packets.
    if not basic_rate_packets:
        print("------------------LE CTE Reference Period Measurement------------------")
        print(
            f"Average Power Mean (dBm)                                         : {reference_period_average_power_mean}"
        )
        print(
            f"Peak Absolute Power Deviation Maximum (%)                        : {reference_period_peak_absolute_power_deviation_maximum}\n"
        )

    print("------------------LE CTE Transmit Slot Power Measurement------------------")
    if len(transmit_slot_average_power_mean) == 0:
        print("No data")
    for i in range(len(transmit_slot_average_power_mean)):
        print(
            f"Average Power Mean (dBm)[{i}]                     : {transmit_slot_average_power_mean[i]}\n"
        )
        print(
            f"Peak Absolute Power Deviation Maximum (%)[{i}]    : {transmit_slot_peak_absolute_power_deviation_maximum[i]}\n"
        )
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxbluetooth_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxcdma2k/acp.py sha256=0b88616d60849e096428a0e0d8be9bb18a6d6f77c3c6cf2e438763610160fecc bytes=10322 -->
## FILE: examples/nirfmxcdma2k/acp.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxcdma2k/acp.py`
- sha256: `0b88616d60849e096428a0e0d8be9bb18a6d6f77c3c6cf2e438763610160fecc`
- bytes: 10322

````python
r"""Fetch ACP data.

Steps:
1. Open a new RFmx session
2. Configure Reference Clock
3. Configure the basic signal properties  (Center Frequency, Reference Level and External
   Attenuation)
4. Configure RF Attenuation
5. Configure Trigger
6. Configure Band Class
7. Set Measurement to ACP
8. Configure Number of Offsets
9. Set Noise Compensation
10. Set Dynamic Range Mode
11. Configure Sweep Time
12. Configure Averaging Parameters
13. Commit Settings and Initiate Measurement
14. Fetch diverse ACP Measurement Results
15. Close the RFmx Session

The gRPC API is built from the C API. RFmx CDMA2k documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\CDMA2k\Documentation\cdma2kcvi.chm

Getting Started:

To run this example, install "RFmx CDMA2k" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-cdma2k.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxCDMA2k gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxCDMA2k-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxCdma2kAcp.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxcdma2k_pb2 as nirfmxcdma2k_types
import nirfmxcdma2k_pb2_grpc as grpc_nirfmxcdma2k

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxCDMA2kSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxcdma2k.NiRFmxCDMA2kStub(channel)
instr = None


NUMBER_OF_OFFSETS = 2


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxcdma2k_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Auto Level
    auto_level = 1

    # Create a new RFmx Session
    initialize_response = client.Initialize(
        nirfmxcdma2k_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    check_for_warning(initialize_response, instr)

    # Configure CDMA2k ACP measurement parameters
    client.CfgFrequencyReference(
        nirfmxcdma2k_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxcdma2k_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10.0e6,
        )
    )
    client.CfgExternalAttenuation(
        nirfmxcdma2k_types.CfgExternalAttenuationRequest(
            instrument=instr, selector_string="", external_attenuation=0.00
        )
    )
    client.CfgFrequency(
        nirfmxcdma2k_types.CfgFrequencyRequest(
            instrument=instr, selector_string="", center_frequency=833.490e6
        )
    )
    client.CfgRFAttenuation(
        nirfmxcdma2k_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxcdma2k_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.00,
        )
    )
    client.CfgDigitalEdgeTrigger(
        nirfmxcdma2k_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxcdma2k_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxcdma2k_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=False,
        )
    )
    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxcdma2k_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=0.02
            )
        )
        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)                    : {reference_level}")
    else:
        client.CfgReferenceLevel(
            nirfmxcdma2k_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.00
            )
        )
    client.CfgBandClass(
        nirfmxcdma2k_types.CfgBandClassRequest(instrument=instr, selector_string="", band_class=0)
    )
    client.SelectMeasurements(
        nirfmxcdma2k_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_array=[nirfmxcdma2k_types.MEASUREMENT_TYPES_ACP],
            enable_all_traces=True,
        )
    )
    client.ACPCfgNumberOfOffsets(
        nirfmxcdma2k_types.ACPCfgNumberOfOffsetsRequest(
            instrument=instr, selector_string="", number_of_offsets=NUMBER_OF_OFFSETS
        )
    )
    client.ACPCfgNoiseCompensationEnabled(
        nirfmxcdma2k_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxcdma2k_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )
    client.ACPCfgMeasurementMethod(
        nirfmxcdma2k_types.ACPCfgMeasurementMethodRequest(
            instrument=instr,
            selector_string="",
            measurement_method=nirfmxcdma2k_types.ACP_MEASUREMENT_METHOD_NORMAL,
        )
    )
    client.ACPCfgSweepTime(
        nirfmxcdma2k_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxcdma2k_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=1.67e-3,
        )
    )
    client.ACPCfgAveraging(
        nirfmxcdma2k_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxcdma2k_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxcdma2k_types.ACP_AVERAGING_TYPE_RMS,
        )
    )
    initiate_response = client.Initiate(
        nirfmxcdma2k_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )
    check_for_warning(initiate_response, instr)

    # Fetch diverse ACP Measurement Results

    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxcdma2k_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)
    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    acp_fetch_carrier_absolute_power_response = client.ACPFetchCarrierAbsolutePower(
        nirfmxcdma2k_types.ACPFetchCarrierAbsolutePowerRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(acp_fetch_carrier_absolute_power_response, instr)
    carrier_absolute_power = acp_fetch_carrier_absolute_power_response.carrier_absolute_power

    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxcdma2k_types.ACPFetchSpectrumRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    # Display ACP Measurement Results
    print(f"Carrier Absolute Power (dBm)             : {carrier_absolute_power}")

    print("\n-------------- Offset Channel Measurements --------------")

    for i in range(NUMBER_OF_OFFSETS):
        print(f"\nOFFSET {i}")
        print(f"Lower Relative Power (dB)                : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)                : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm)               : {upper_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm)               : {lower_absolute_power[i]}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxcdma2k_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxcdma2k/modacc.py sha256=64d3e698071cc52ec8c5490d728b19d72b93133ed1059da15797bac7f542e0d0 bytes=10950 -->
## FILE: examples/nirfmxcdma2k/modacc.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxcdma2k/modacc.py`
- sha256: `64d3e698071cc52ec8c5490d728b19d72b93133ed1059da15797bac7f542e0d0`
- bytes: 10950

````python
r"""Fetch ModAcc data.

Steps:
1. Open a new RFmx session
2. Configure Reference Clock
3. Configure the basic signal properties  (Center Frequency, Reference Level and External
   Attenuation)
4. Configure Trigger
5. Configure Radio Configuration
6. Configure Long Code Mask
7. Set Measurement to ModAcc
8. Configure Synchronization mode
9. Commit Settings and Initiate Measurement
10. Fetch diverse ModAcc Measurement Results
11. Close the RFmx Session

The gRPC API is built from the C API. RFmx CDMA2k documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\CDMA2k\Documentation\cdma2kcvi.chm

Getting Started:

To run this example, install "RFmx CDMA2k" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-cdma2k.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxCDMA2k gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxCDMA2k-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxCdma2kModAcc.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxcdma2k_pb2 as nirfmxcdma2k_types
import nirfmxcdma2k_pb2_grpc as grpc_nirfmxcdma2k

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxCDMA2kSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxcdma2k.NiRFmxCDMA2kStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxcdma2k_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Create new RFmx session
    initialize_response = client.Initialize(
        nirfmxcdma2k_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    check_for_warning(initialize_response, instr)
    client.CfgFrequencyReference(
        nirfmxcdma2k_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxcdma2k_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10.0e6,
        )
    )
    client.CfgRF(
        nirfmxcdma2k_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=833.490e6,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )
    client.CfgDigitalEdgeTrigger(
        nirfmxcdma2k_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxcdma2k_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxcdma2k_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.00,
            enable_trigger=False,
        )
    )
    client.CfgRadioConfiguration(
        nirfmxcdma2k_types.CfgRadioConfigurationRequest(
            instrument=instr,
            selector_string="",
            radio_configuration=nirfmxcdma2k_types.RADIO_CONFIGURATION_RC3,
        )
    )
    client.CfgUplinkSpreading(
        nirfmxcdma2k_types.CfgUplinkSpreadingRequest(
            instrument=instr, selector_string="", uplink_spreading_long_code_mask=0
        )
    )
    client.SelectMeasurements(
        nirfmxcdma2k_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_array=[nirfmxcdma2k_types.MEASUREMENT_TYPES_MODACC],
            enable_all_traces=True,
        )
    )
    client.ModAccCfgSynchronizationModeAndInterval(
        nirfmxcdma2k_types.ModAccCfgSynchronizationModeAndIntervalRequest(
            instrument=instr,
            selector_string="",
            synchronization_mode=nirfmxcdma2k_types.MODACC_SYNCHRONIZATION_MODE_SLOT,
            measurement_offset=0,
            measurement_length=1,
        )
    )
    client.Initiate(
        nirfmxcdma2k_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )

    # Retrieve results

    mod_acc_fetch_evm_response = client.ModAccFetchEVM(
        nirfmxcdma2k_types.ModAccFetchEVMRequest(instrument=instr, selector_string="", timeout=10.0)
    )
    check_for_warning(mod_acc_fetch_evm_response, instr)
    rms_evm = mod_acc_fetch_evm_response.rms_evm
    peak_evm = mod_acc_fetch_evm_response.peak_evm
    rho = mod_acc_fetch_evm_response.rho
    frequency_error = mod_acc_fetch_evm_response.frequency_error
    chip_rate_error = mod_acc_fetch_evm_response.chip_rate_error
    rms_magnitude_error = mod_acc_fetch_evm_response.rms_magnitude_error
    rms_phase_error = mod_acc_fetch_evm_response.rms_phase_error
    mod_acc_fetch_iq_impairments_response = client.ModAccFetchIQImpairments(
        nirfmxcdma2k_types.ModAccFetchIQImpairmentsRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_iq_impairments_response, instr)
    iq_origin_offset = mod_acc_fetch_iq_impairments_response.iq_origin_offset
    iq_gain_imbalance = mod_acc_fetch_iq_impairments_response.iq_gain_imbalance
    iq_quadrature_error = mod_acc_fetch_iq_impairments_response.iq_quadrature_error
    mod_acc_fetch_peak_cde_response = client.ModAccFetchPeakCDE(
        nirfmxcdma2k_types.ModAccFetchPeakCDERequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_peak_cde_response, instr)
    peak_cde = mod_acc_fetch_peak_cde_response.peak_cde
    peak_cde_walsh_code_number = mod_acc_fetch_peak_cde_response.peak_cde_walsh_code_number
    peak_cde_branch = mod_acc_fetch_peak_cde_response.peak_cde_branch
    mod_acc_fetch_peak_active_cde_response = client.ModAccFetchPeakActiveCDE(
        nirfmxcdma2k_types.ModAccFetchPeakActiveCDERequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_peak_active_cde_response, instr)
    peak_active_cde = mod_acc_fetch_peak_active_cde_response.peak_active_cde
    peak_active_cde_walsh_code_length = (
        mod_acc_fetch_peak_active_cde_response.peak_active_cde_walsh_code_length
    )
    peak_active_cde_walsh_code_number = (
        mod_acc_fetch_peak_active_cde_response.peak_active_cde_walsh_code_number
    )
    peak_active_cde_branch = mod_acc_fetch_peak_active_cde_response.peak_active_cde_branch

    mod_acc_fetch_constellation_trace_response = client.ModAccFetchConstellationTrace(
        nirfmxcdma2k_types.ModAccFetchConstellationTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_constellation_trace_response, instr)
    constellation = mod_acc_fetch_constellation_trace_response.constellation
    mod_acc_fetch_evm_trace_response = client.ModAccFetchEVMTrace(
        nirfmxcdma2k_types.ModAccFetchEVMTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_evm_trace_response, instr)
    x0 = mod_acc_fetch_evm_trace_response.x0
    dx = mod_acc_fetch_evm_trace_response.dx
    evm_trace = mod_acc_fetch_evm_trace_response.evm

    # Display results

    print("--------------EVM ------------------------------------------")
    print(f"RMS EVM (%%)                       : {rms_evm}")
    print(f"Peak EVM (%%)                      : {peak_evm}")
    print(f"Rho                               : {rho}")
    print(f"Frequency Error (Hz)              : {frequency_error}")
    print(f"Chip Rate Error (ppm)             : {chip_rate_error}")
    print(f"RMS Magnitude Error (%%)           : {rms_magnitude_error}")
    print(f"RMS Phase Error (deg)             : {rms_phase_error}")

    print("\n\n--------------Code Domain Error--------------------------")
    print(f"Peak CDE (dB)                     : {peak_cde}")
    print(f"Peak CDE Walsh Code Number        : {peak_cde_walsh_code_number}")
    print(f"Peak Active CDE (dB)              : {peak_active_cde}")
    print(f"Peak CDE Branch                   : {'Q' if peak_cde_branch else 'I'}")
    print(f"Peak Active CDE Walsh Code Length : {peak_active_cde_walsh_code_length}")
    print(f"Peak Active CDE Walsh Code Number : {peak_active_cde_walsh_code_number}")
    print(f"Peak Active CDE Branch            : {'Q' if peak_active_cde_branch else 'I'}")

    print("\n\n--------------I/Q Impairments----------------------------")
    print(f"I/Q Origin Offset (dB)            : {iq_origin_offset}")
    print(f"I/Q Gain Imbalance (dB)           : {iq_gain_imbalance}")
    print(f"I/Q Quadrature Error (deg)        : {iq_quadrature_error}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxcdma2k_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxdemod/ADemod-AM-basic.py sha256=1369e6d4f7e1923def707866d7c57e688ed187a26d23c5c70579909fbe6e59b3 bytes=6139 -->
## FILE: examples/nirfmxdemod/ADemod-AM-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxdemod/ADemod-AM-basic.py`
- sha256: `1369e6d4f7e1923def707866d7c57e688ed187a26d23c5c70579909fbe6e59b3`
- bytes: 6139

````python
r"""ADemod AM example.

Steps:
1. Open a new RFmxInstrMX session and create a Demod Signal
2. Configure Selected Ports
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation)
4. Configure ADemod rbw, Measurement Interval, AM Carrier Suppressed and Averaging
5. Read ADemod AM Measurement Results
6. Dispose Demod Signal and Close the RFmxInstrMX Session

The gRPC API is built from the C API. RFmx Demod documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\Demod\Documentation\demodcvi.chm

Getting Started:

To run this example, install "RFmx Demod" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-demod.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxDemod gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxDemod-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ADemod-AM-basic.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxdemod_pb2 as nirfmxdemod_types
import nirfmxdemod_pb2_grpc as grpc_nirfmxdemod

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxDemodSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxdemod.NiRFmxDemodStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxdemod_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Create a new RFmx Session
    initialize_response = client.Initialize(
        nirfmxdemod_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument

    # Configure ADemod measurement parameters
    client.SetAttributeString(
        nirfmxdemod_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxdemod_types.NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )
    client.CfgRF(
        nirfmxdemod_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )
    client.ADemodCfgRBWFilter(
        nirfmxdemod_types.ADemodCfgRBWFilterRequest(
            instrument=instr,
            selector_string="",
            rbw=100.00e3,
            rbw_filter_type=nirfmxdemod_types.A_DEMOD_RBW_FILTER_TYPE_FLAT,
            rbw_rrc_alpha=0.1,
        )
    )
    client.ADemodCfgMeasurementInterval(
        nirfmxdemod_types.ADemodCfgMeasurementIntervalRequest(
            instrument=instr, selector_string="", measurement_interval=10.00e-3
        )
    )
    client.ADemodCfgAMCarrierSuppressed(
        nirfmxdemod_types.ADemodCfgAMCarrierSuppressedRequest(
            instrument=instr,
            selector_string="",
            am_carrier_suppressed_enabled=nirfmxdemod_types.A_DEMOD_AM_CARRIER_SUPPRESSED_ENABLED_FALSE,
        )
    )
    client.ADemodCfgAveraging(
        nirfmxdemod_types.ADemodCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxdemod_types.A_DEMOD_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxdemod_types.A_DEMOD_AVERAGING_TYPE_LINEAR,
        )
    )

    # Retrieve results
    a_demod_read_am_response = client.ADemodReadAM(
        nirfmxdemod_types.ADemodReadAMRequest(instrument=instr, selector_string="", timeout=10.0)
    )
    check_for_warning(a_demod_read_am_response, instr)
    mean_carrier_power = a_demod_read_am_response.mean_carrier_power
    mean_modulation_depth = a_demod_read_am_response.mean_modulation_depth

    # Display results
    print(f"Mean Modulation Depth (%%)   : {mean_modulation_depth}")
    print(f"Mean Carrier Power (dBm)    : {mean_carrier_power}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxdemod_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxdemod/DDemod-QAM-basic.py sha256=a32e1a8f0ff9d4eed992388df660f7565a1313361eb72bf8884cb08d9b847c6c bytes=7218 -->
## FILE: examples/nirfmxdemod/DDemod-QAM-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxdemod/DDemod-QAM-basic.py`
- sha256: `a32e1a8f0ff9d4eed992388df660f7565a1313361eb72bf8884cb08d9b847c6c`
- bytes: 7218

````python
r"""DDemod QAM example.

Steps:
1. Open a new RFmxInstrMX session and create a Demod Signal
2. Configure Selected Ports
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation)
4. Select QAM Modulation and M
5. Configure DDemod Symbol Rate, Number of Symbols and Pulse Shaping Filter
6. Configure DDemod Measurement Filter Type as Auto
7. Configure DDemod Averaging
8. Read DDemod Measurement Results
9. Dispose Demod Signal and Close the RFmxInstrMX Session

The gRPC API is built from the C API. RFmx Demod documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\Demod\Documentation\demodcvi.chm

Getting Started:

To run this example, install "RFmx Demod" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-demod.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxDemod gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxDemod-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python DDemod-QAM-basic.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxdemod_pb2 as nirfmxdemod_types
import nirfmxdemod_pb2_grpc as grpc_nirfmxdemod

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxDemodSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxdemod.NiRFmxDemodStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxdemod_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Create a new RFmx Session
    initialize_response = client.Initialize(
        nirfmxdemod_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument

    # Configure DDemod measurement parameters
    client.SetAttributeString(
        nirfmxdemod_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxdemod_types.NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )
    client.CfgRF(
        nirfmxdemod_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )
    client.DDemodCfgModulationType(
        nirfmxdemod_types.DDemodCfgModulationTypeRequest(
            instrument=instr,
            selector_string="",
            modulation_type=nirfmxdemod_types.D_DEMOD_MODULATION_TYPE_QAM,
            m=nirfmxdemod_types.D_DEMOD_M_16,
            differential_enabled=nirfmxdemod_types.D_DEMOD_DIFFERENTIAL_ENABLED_FALSE,
        )
    )
    client.DDemodCfgSymbolRate(
        nirfmxdemod_types.DDemodCfgSymbolRateRequest(
            instrument=instr, selector_string="", symbol_rate=100.000e3
        )
    )
    client.DDemodCfgNumberOfSymbols(
        nirfmxdemod_types.DDemodCfgNumberOfSymbolsRequest(
            instrument=instr, selector_string="", number_of_symbols=1000
        )
    )
    client.DDemodCfgPulseShapingFilter(
        nirfmxdemod_types.DDemodCfgPulseShapingFilterRequest(
            instrument=instr,
            selector_string="",
            pulse_shaping_filter_type=nirfmxdemod_types.D_DEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE,
            pulse_shaping_filter_parameter=0.50,
            x0=0.0,
            dx=1.0,
            pulse_shaping_filter_custom_coefficients=None,
        )
    )
    client.DDemodCfgMeasurementFilter(
        nirfmxdemod_types.DDemodCfgMeasurementFilterRequest(
            instrument=instr,
            selector_string="",
            measurement_filter_type=nirfmxdemod_types.D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO,
            x0=0.0,
            dx=1.0,
            measurement_filter_custom_coefficients=None,
        )
    )
    client.DDemodCfgAveraging(
        nirfmxdemod_types.DDemodCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxdemod_types.D_DEMOD_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    # Retrieve results
    d_demod_read_response = client.DDemodRead(
        nirfmxdemod_types.DDemodReadRequest(instrument=instr, selector_string="", timeout=10.0)
    )
    check_for_warning(d_demod_read_response, instr)
    mean_modulation_error_ratio = d_demod_read_response.mean_modulation_error_ratio
    maximum_peak_evm = d_demod_read_response.maximum_peak_evm
    mean_rmsevm = d_demod_read_response.mean_rms_evm
    mean_frequency_offset = d_demod_read_response.mean_frequency_offset

    # Display results
    print(f"Mean Frequency Offset(Hz)        : {mean_frequency_offset}")
    print(f"Mean RMS EVM(%%)                  : {mean_rmsevm}")
    print(f"Maximum Peak EVM(%%)              : {maximum_peak_evm}")
    print(f"Mean Modulation Error Ratio(dB)  : {mean_modulation_error_ratio}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxdemod_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxgsm/evm.py sha256=ff5fadbb758e64635699a26ecfc05b54ba721342ccf7594419b41869c0f0f63e bytes=10782 -->
## FILE: examples/nirfmxgsm/evm.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxgsm/evm.py`
- sha256: `ff5fadbb758e64635699a26ecfc05b54ba721342ccf7594419b41869c0f0f63e`
- bytes: 10782

````python
r"""EVM example.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Parameters for IQ Power Edge Trigger.
5. Configure Number of Timeslots.
6. Configure Auto tsc Detection Enabled.
7. Configure Signal Type.
8. Configure tsc.
9. Select ModAcc measurement and enable Traces.
10. Configure Averaging Parameters for ModAcc measurement.
11. Initiate the Measurement.
12. Fetch ModAcc Measurements and Traces.
13. Close RFmx Session.

The gRPC API is built from the C API. RFmx GSM documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\GSM\Documentation\rfmxgsmcvi.chm

Getting Started:

To run this example, install "RFmx GSM" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-gsm-edge-.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmx GSM gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmx-GSM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python evm.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxgsm_pb2 as nirfmxgsm_types
import nirfmxgsm_pb2_grpc as grpc_nirfmxgsm

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxGSMSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxgsm.NiRFmxGSMStub(channel)
instr = None

NUMBER_OF_TIMESLOTS = 1


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxgsm_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    evm = None
    constellation_trace = None
    actual_array_size = 0

    initialize_response = client.Initialize(
        nirfmxgsm_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxgsm_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxgsm_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )
    client.CfgRF(
        nirfmxgsm_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=890.2e6,
            reference_level=0.0,
            external_attenuation=0.0,
        )
    )
    client.CfgIQPowerEdgeTrigger(
        nirfmxgsm_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxgsm_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.00,
            trigger_delay=0.0,
            minimum_quiet_time_mode=nirfmxgsm_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            minimum_quiet_time=582e-6,
            iq_power_edge_level_type=nirfmxgsm_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )
    client.CfgNumberOfTimeslots(
        nirfmxgsm_types.CfgNumberOfTimeslotsRequest(
            instrument=instr, selector_string="", number_of_timeslots=NUMBER_OF_TIMESLOTS
        )
    )
    client.CfgAutoTSCDetectionEnabled(
        nirfmxgsm_types.CfgAutoTSCDetectionEnabledRequest(
            instrument=instr,
            selector_string="",
            auto_tsc_detection_enabled=nirfmxgsm_types.AUTO_TSC_DETECTION_ENABLED_TRUE,
        )
    )
    client.CfgSignalType(
        nirfmxgsm_types.CfgSignalTypeRequest(
            instrument=instr,
            selector_string="slot::all",
            modulation_type=nirfmxgsm_types.MODULATION_TYPE_8PSK,
            burst_type=nirfmxgsm_types.BURST_TYPE_NB,
            hb_filter_width=nirfmxgsm_types.HB_FILTER_WIDTH_NARROW,
        )
    )
    client.CfgTSC(
        nirfmxgsm_types.CfgTSCRequest(
            instrument=instr, selector_string="slot::all", tsc=nirfmxgsm_types.TSC_TSC0
        )
    )
    client.SelectMeasurements(
        nirfmxgsm_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxgsm_types.MEASUREMENT_TYPES_MODACC,
            enable_all_traces=True,
        )
    )
    client.ModAccCfgAveraging(
        nirfmxgsm_types.ModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxgsm_types.MODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxgsm_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )
    check_for_warning(initiate_response, instr)

    mod_acc_fetch_evm_response = client.ModAccFetchEVM(
        nirfmxgsm_types.ModAccFetchEVMRequest(instrument=instr, selector_string="", timeout=10.0)
    )
    check_for_warning(mod_acc_fetch_evm_response, instr)
    mean_rmsevm = mod_acc_fetch_evm_response.mean_rms_evm
    maximum_rmsevm = mod_acc_fetch_evm_response.maximum_rms_evm
    mean_peak_evm = mod_acc_fetch_evm_response.mean_peak_evm
    maximum_peak_evm = mod_acc_fetch_evm_response.maximum_peak_evm
    ninety_fifth_percentile_evm = mod_acc_fetch_evm_response.ninety_fifth_percentile_evm
    mean_frequency_error = mod_acc_fetch_evm_response.mean_frequency_error
    peak_evm_symbol = mod_acc_fetch_evm_response.peak_evm_symbol

    mod_acc_fetch_iq_impairments_response = client.ModAccFetchIQImpairments(
        nirfmxgsm_types.ModAccFetchIQImpairmentsRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_iq_impairments_response, instr)
    mean_iq_gain_imbalance = mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance
    maximum_iq_gain_imbalance = mod_acc_fetch_iq_impairments_response.maximum_iq_gain_imbalance
    mean_iq_origin_offset = mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset
    maximum_iq_origin_offset = mod_acc_fetch_iq_impairments_response.maximum_iq_origin_offset

    mod_acc_fetch_detected_tsc_array_response = client.ModAccFetchDetectedTSCArray(
        nirfmxgsm_types.ModAccFetchDetectedTSCArrayRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_detected_tsc_array_response, instr)
    detected_tsc = mod_acc_fetch_detected_tsc_array_response.detected_tsc

    mod_acc_fetch_evm_trace_response = client.ModAccFetchEVMTrace(
        nirfmxgsm_types.ModAccFetchEVMTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_evm_trace_response, instr)
    x0 = mod_acc_fetch_evm_trace_response.x0
    dx = mod_acc_fetch_evm_trace_response.dx
    evm = mod_acc_fetch_evm_trace_response.evm

    mod_acc_fetch_constellation_trace_response = client.ModAccFetchConstellationTrace(
        nirfmxgsm_types.ModAccFetchConstellationTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(mod_acc_fetch_constellation_trace_response, instr)
    constellation_trace = mod_acc_fetch_constellation_trace_response.constellation_trace

    print("-----------------Measurement-----------------")
    print(f"Mean RMS evm (%%)                : {mean_rmsevm}")
    print(f"Maximum RMS evm (%%)             : {maximum_rmsevm}")
    print(f"Mean Peak evm (%%)               : {mean_peak_evm}")
    print(f"Maximum Peak evm (%%)            : {maximum_peak_evm}")
    print(f"95th Percentile evm (%%)         : {ninety_fifth_percentile_evm}")
    print(f"Mean Frequency Error (Hz)       : {mean_frequency_error}")
    print(f"Peak evm Symbol                 : {peak_evm_symbol}")

    print("\n----------------IQ Impairments-----------------")
    print(f"Mean IQ Origin Offset (dB)      : {mean_iq_origin_offset}")
    print(f"Maximum IQ Origin Offset (dB)   : {maximum_iq_origin_offset}")
    print(f"Mean IQ Gain Imbalance (dB)     : {mean_iq_gain_imbalance}")
    print(f"Maximum IQ Gain Imbalance (dB)  : {maximum_iq_gain_imbalance}")

    print("\n----------------Detected tsc-------------------")
    for i in range(NUMBER_OF_TIMESLOTS):
        if detected_tsc[i] < 0:
            print(f"Slot {i}                             : Unknown")
        else:
            print(f"Slot {i}                          : tsc{detected_tsc[i]}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxgsm_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxgsm/orfs.py sha256=b17034bab1956184c7fd92e376815f106ece37bf9c79ac5d11088dfb0a795f9a bytes=13658 -->
## FILE: examples/nirfmxgsm/orfs.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxgsm/orfs.py`
- sha256: `b17034bab1956184c7fd92e376815f106ece37bf9c79ac5d11088dfb0a795f9a`
- bytes: 13658

````python
r"""ORFS example.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure External Attenuation.
4. Configure Center Frequency.
5. Configure Link Direction.
6. Configure Trigger Parameters for IQ Power Edge Trigger.
7. Configure Number of Timeslots.
8. Configure Signal Type.
9. Configure Auto Level.
10. Configure Auto tsc Detection Enabled.
11. Configure tsc.
12. Select  ORFS  measurement and enable Traces.
13. Configure Noise Compensation Enabled.
14. Configure Measurement Type.
15. Configure Offset Frequency Mode.
16. Configure Evaluation Symbols.
17. Configure Averaging Parameters.
18. Initiate the Measurement.
19. Fetch ORFS Measurements and Traces.
20. Close RFmx Session.

The gRPC API is built from the C API. RFmx GSM documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\GSM\Documentation\rfmxgsmcvi.chm

Getting Started:

To run this example, install "RFmx GSM" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-gsm-edge-.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmx GSM gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmx-GSM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python orfs.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxgsm_pb2 as nirfmxgsm_types
import nirfmxgsm_pb2_grpc as grpc_nirfmxgsm

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxGSMSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxgsm.NiRFmxGSMStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxgsm_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    mod_lower_absolute_power = None
    mod_upper_absolute_power = None
    mod_lower_relative_power = None
    mod_upper_relative_power = None

    switch_lower_absolute_power = None
    switch_upper_absolute_power = None
    switch_lower_relative_power = None
    switch_upper_relative_power = None

    mod_offset_frequency = None
    mod_absolute_power = None
    mod_relative_power = None
    switch_offset_frequency = None
    switch_absolute_power = None
    switch_relative_power = None
    actual_array_size = 0

    initialize_response = client.Initialize(
        nirfmxgsm_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxgsm_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxgsm_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )
    client.CfgExternalAttenuation(
        nirfmxgsm_types.CfgExternalAttenuationRequest(
            instrument=instr, selector_string="", external_attenuation=0.0
        )
    )
    client.CfgFrequency(
        nirfmxgsm_types.CfgFrequencyRequest(
            instrument=instr, selector_string="", center_frequency=890.2e6
        )
    )
    client.CfgLinkDirection(
        nirfmxgsm_types.CfgLinkDirectionRequest(
            instrument=instr,
            selector_string="",
            link_direction=nirfmxgsm_types.LINK_DIRECTION_UPLINK,
        )
    )
    client.CfgIQPowerEdgeTrigger(
        nirfmxgsm_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxgsm_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            minimum_quiet_time_mode=nirfmxgsm_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            minimum_quiet_time=582e-6,
            iq_power_edge_level_type=nirfmxgsm_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )
    client.CfgNumberOfTimeslots(
        nirfmxgsm_types.CfgNumberOfTimeslotsRequest(
            instrument=instr, selector_string="", number_of_timeslots=1
        )
    )

    client.CfgSignalType(
        nirfmxgsm_types.CfgSignalTypeRequest(
            instrument=instr,
            selector_string="slot::all",
            modulation_type=nirfmxgsm_types.MODULATION_TYPE_8PSK,
            burst_type=nirfmxgsm_types.BURST_TYPE_NB,
            hb_filter_width=nirfmxgsm_types.HB_FILTER_WIDTH_NARROW,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxgsm_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=0.0046
            )
        )
        auto_reference_level = auto_level_response.reference_level
        print(f"Reference Level                     : {auto_reference_level}\n")
    else:
        client.CfgReferenceLevel(
            nirfmxgsm_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.0
            )
        )

    client.CfgAutoTSCDetectionEnabled(
        nirfmxgsm_types.CfgAutoTSCDetectionEnabledRequest(
            instrument=instr,
            selector_string="",
            auto_tsc_detection_enabled=nirfmxgsm_types.AUTO_TSC_DETECTION_ENABLED_TRUE,
        )
    )
    client.CfgTSC(
        nirfmxgsm_types.CfgTSCRequest(
            instrument=instr, selector_string="slot::all", tsc=nirfmxgsm_types.TSC_TSC0
        )
    )
    client.SelectMeasurements(
        nirfmxgsm_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxgsm_types.MEASUREMENT_TYPES_ORFS,
            enable_all_traces=True,
        )
    )
    client.ORFSCfgNoiseCompensationEnabled(
        nirfmxgsm_types.ORFSCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxgsm_types.ORFS_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )
    client.ORFSCfgMeasurementType(
        nirfmxgsm_types.ORFSCfgMeasurementTypeRequest(
            instrument=instr,
            selector_string="",
            measurement_type=nirfmxgsm_types.ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING,
        )
    )
    client.ORFSCfgOffsetFrequencyMode(
        nirfmxgsm_types.ORFSCfgOffsetFrequencyModeRequest(
            instrument=instr,
            selector_string="",
            offset_frequency_mode=nirfmxgsm_types.ORFS_OFFSET_FREQUENCY_MODE_STANDARD,
        )
    )
    client.ORFSCfgEvaluationSymbols(
        nirfmxgsm_types.ORFSCfgEvaluationSymbolsRequest(
            instrument=instr,
            selector_string="",
            evaluation_symbols_start=50.0,
            evaluation_symbols_include_tsc=nirfmxgsm_types.ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE,
            evaluation_symbols_stop=90.0,
        )
    )
    client.ORFSCfgAveraging(
        nirfmxgsm_types.ORFSCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxgsm_types.ORFS_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxgsm_types.ORFS_AVERAGING_TYPE_LOG,
        )
    )
    initiate_response = client.Initiate(
        nirfmxgsm_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )
    check_for_warning(initiate_response, instr)

    orfs_fetch_modulation_results_array_response = client.ORFSFetchModulationResultsArray(
        nirfmxgsm_types.ORFSFetchModulationResultsArrayRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(orfs_fetch_modulation_results_array_response, instr)
    modulation_carrier_power = orfs_fetch_modulation_results_array_response.modulation_carrier_power
    mod_lower_relative_power = orfs_fetch_modulation_results_array_response.lower_relative_power
    mod_upper_relative_power = orfs_fetch_modulation_results_array_response.upper_relative_power
    mod_lower_absolute_power = orfs_fetch_modulation_results_array_response.lower_absolute_power
    mod_upper_absolute_power = orfs_fetch_modulation_results_array_response.upper_absolute_power

    orfs_fetch_switching_results_array_response = client.ORFSFetchSwitchingResultsArray(
        nirfmxgsm_types.ORFSFetchSwitchingResultsArrayRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(orfs_fetch_switching_results_array_response, instr)
    switching_carrier_power = orfs_fetch_switching_results_array_response.switching_carrier_power
    switch_lower_relative_power = orfs_fetch_switching_results_array_response.lower_relative_power
    switch_upper_relative_power = orfs_fetch_switching_results_array_response.upper_relative_power
    switch_lower_absolute_power = orfs_fetch_switching_results_array_response.lower_absolute_power
    switch_upper_absolute_power = orfs_fetch_switching_results_array_response.upper_absolute_power

    orfs_fetch_modulation_power_trace_response = client.ORFSFetchModulationPowerTrace(
        nirfmxgsm_types.ORFSFetchModulationPowerTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(orfs_fetch_modulation_power_trace_response, instr)
    mod_offset_frequency = orfs_fetch_modulation_power_trace_response.offset_frequency
    mod_absolute_power = orfs_fetch_modulation_power_trace_response.absolute_power
    mod_relative_power = orfs_fetch_modulation_power_trace_response.relative_power

    orfs_fetch_switching_power_trace_response = client.ORFSFetchSwitchingPowerTrace(
        nirfmxgsm_types.ORFSFetchSwitchingPowerTraceRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(orfs_fetch_switching_power_trace_response, instr)
    switch_offset_frequency = orfs_fetch_switching_power_trace_response.offset_frequency
    switch_absolute_power = orfs_fetch_switching_power_trace_response.absolute_power
    switch_relative_power = orfs_fetch_switching_power_trace_response.relative_power

    print("---------Modulation Results---------")
    print(f"Modulation Carrier Power  (dBm)     : {modulation_carrier_power}\n")
    for i in range(len(mod_lower_absolute_power)):
        print(f"Offset : {i}")
        print(f"Lower Absolute Power (dBm)        : {mod_lower_absolute_power[i]}")
        print(f"Lower Relative Power (dB)        : {mod_lower_relative_power[i]}")
        print(f"Upper Absolute Power (dBm)        : {mod_upper_absolute_power[i]}")
        print(f"Upper Relative Power (dB)        : {mod_upper_relative_power[i]}")
    print("\n---------Switching Results---------")
    print(f"Switching Carrier Power  (dBm)      : {switching_carrier_power}\n")
    for i in range(len(switch_lower_absolute_power)):
        print(f"Offset : {i}")
        print(f"Lower Absolute Power (dBm)          : {switch_lower_absolute_power[i]}")
        print(f"Lower Relative Power (dB)           : {switch_lower_relative_power[i]}")
        print(f"Upper Absolute Power (dBm)          : {switch_upper_absolute_power[i]}")
        print(f"Upper Relative Power (dB)           : {switch_upper_relative_power[i]}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxgsm_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxlte/acp-single-carrier.py sha256=de1e5d8e0291e72fe9aac9fb215f5a369e4bc639b2f0aa9dcc408356f2eaeb04 bytes=12090 -->
## FILE: examples/nirfmxlte/acp-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxlte/acp-single-carrier.py`
- sha256: `de1e5d8e0291e72fe9aac9fb215f5a369e4bc639b2f0aa9dcc408356f2eaeb04`
- bytes: 12090

````python
r"""Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency, RF Attenuation and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Carrier Bandwidth.
  6. Configure Reference Level.
  7. Configure Duplex Mode.
  8. Configure Link Direction.
  9. Select ACP measurement and enable Traces.
  10. Configure Measurement Method.
  11. Configure Averaging Parameters for ACP measurement.
  12. Configure Sweep Time Parameters.
  13. Configure Noise Compensation Parameter.
  14. Initiate the Measurement.
  15. Fetch ACP Measurements and Traces.
  16. Close RFmx Session.

The gRPC API is built from the C API. RFmx LTE documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\LTE\Documentation\ltecvi.chm

Getting Started:

To run this example, install "RFmx LTE" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-lte.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxLTE gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxLTE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxlte_pb2 as nirfmxlte_types
import nirfmxlte_pb2_grpc as grpc_nirfmxlte

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxLTESession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

NUMBER_OF_OFFSETS = 3

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxlte.NiRFmxLTEStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxlte_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxlte_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxlte_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxlte_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxlte_types.CfgFrequencyRequest(
            instrument=instr, selector_string="", center_frequency=1.95e9
        )
    )

    client.CfgExternalAttenuation(
        nirfmxlte_types.CfgExternalAttenuationRequest(
            instrument=instr, selector_string="", external_attenuation=0.0
        )
    )

    client.CfgRFAttenuation(
        nirfmxlte_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxlte_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxlte_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxlte_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxlte_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=False,
        )
    )

    client.CfgComponentCarrier(
        nirfmxlte_types.CfgComponentCarrierRequest(
            instrument=instr,
            selector_string="",
            component_carrier_bandwidth=10e6,
            component_carrier_frequency=0.0,
            cell_id=0,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxlte_types.AutoLevelRequest(
                instrument=instr,
                selector_string="",
                measurement_interval=0.01,
            )
        )

        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)        : {reference_level}")
    else:
        client.CfgReferenceLevel(
            nirfmxlte_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.0
            )
        )

    client.CfgDuplexScheme(
        nirfmxlte_types.CfgDuplexSchemeRequest(
            instrument=instr,
            selector_string="",
            duplex_scheme=nirfmxlte_types.DUPLEX_SCHEME_FDD,
            uplink_downlink_configuration=nirfmxlte_types.UPLINK_DOWNLINK_CONFIGURATION_0,
        )
    )

    client.CfgLinkDirection(
        nirfmxlte_types.CfgLinkDirectionRequest(
            instrument=instr,
            selector_string="",
            link_direction=nirfmxlte_types.LINK_DIRECTION_UPLINK,
        )
    )

    client.SelectMeasurements(
        nirfmxlte_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxlte_types.MEASUREMENT_TYPES_ACP,
            enable_all_traces=True,
        )
    )

    client.ACPCfgMeasurementMethod(
        nirfmxlte_types.ACPCfgMeasurementMethodRequest(
            instrument=instr,
            selector_string="",
            measurement_method=nirfmxlte_types.ACP_MEASUREMENT_METHOD_NORMAL,
        )
    )

    client.ACPCfgAveraging(
        nirfmxlte_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxlte_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxlte_types.ACP_AVERAGING_TYPE_RMS,
        )
    )

    client.ACPCfgSweepTime(
        nirfmxlte_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxlte_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=0.001,
        )
    )

    client.ACPCfgNoiseCompensationEnabled(
        nirfmxlte_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxlte_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )

    initiate_response = client.Initiate(
        nirfmxlte_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch results ###

    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxlte_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)

    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    assert len(lower_relative_power) == NUMBER_OF_OFFSETS, len(lower_relative_power)
    assert len(upper_relative_power) == NUMBER_OF_OFFSETS, len(upper_relative_power)
    assert len(lower_absolute_power) == NUMBER_OF_OFFSETS, len(lower_absolute_power)
    assert len(upper_absolute_power) == NUMBER_OF_OFFSETS, len(upper_absolute_power)

    acp_fetch_component_carrier_measurement_response = client.ACPFetchComponentCarrierMeasurement(
        nirfmxlte_types.ACPFetchComponentCarrierMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_component_carrier_measurement_response, instr)

    absolute_power = acp_fetch_component_carrier_measurement_response.absolute_power
    relative_power = acp_fetch_component_carrier_measurement_response.relative_power

    for i in range(NUMBER_OF_OFFSETS):
        acp_fetch_absolute_powers_trace_response = client.ACPFetchAbsolutePowersTrace(
            nirfmxlte_types.ACPFetchAbsolutePowersTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
                trace_index=i,
            )
        )
        check_for_warning(acp_fetch_absolute_powers_trace_response, instr)

    for i in range(NUMBER_OF_OFFSETS):
        acp_fetch_relative_powers_trace_response = client.ACPFetchRelativePowersTrace(
            nirfmxlte_types.ACPFetchRelativePowersTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
                trace_index=i,
            )
        )
        check_for_warning(acp_fetch_relative_powers_trace_response, instr)

    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxlte_types.ACPFetchSpectrumRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    print(f"\nCarrier Absolute Power (dBm) : {absolute_power}")

    print("\n-----------Offset Channel Measurements----------- ")
    for i in range(NUMBER_OF_OFFSETS):
        print(f"Offset : {i}")
        print(f"Lower Relative Power (dB)    : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)    : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm)   : {lower_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm)   : {upper_absolute_power[i]}")
        print("------------------------------------------")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxlte_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxlte/ul-modacc-single-carrier.py sha256=3370a7091e27823944ddc7c60d8a0cc7f9435d5527de3d5fbea7148024ddd2ed bytes=11891 -->
## FILE: examples/nirfmxlte/ul-modacc-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxlte/ul-modacc-single-carrier.py`
- sha256: `3370a7091e27823944ddc7c60d8a0cc7f9435d5527de3d5fbea7148024ddd2ed`
- bytes: 11891

````python
r"""Fetch UL ModAcc data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Carrier Bandwidth.
  6. Configure operating Band.
  7. Configure Duplex Mode.
  8. Configure Auto DMRS Detection Enabled.
  9. Select ModAcc measurement and enable Traces.
  10. Configure Synchronization Mode and Measurement Interval.
  11. Configure EVM Unit.
  12. Configure In-Band Emission Mask Type.
  13. Configure Averaging Parameters for ModAcc measurement.
  14. Initiate the Measurement.
  15. Fetch ModAcc Measurements and Traces.
  16. Close RFmx Session.

The gRPC API is built from the C API. RFmx LTE documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\LTE\Documentation\ltecvi.chm

Getting Started:

To run this example, install "RFmx LTE" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-lte.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxLTE gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxLTE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ul-modacc-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxlte_pb2 as nirfmxlte_types
import nirfmxlte_pb2_grpc as grpc_nirfmxlte

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxLTESession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    resource = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxlte.NiRFmxLTEStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxlte_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = client.Initialize(
        nirfmxlte_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxlte_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxlte_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgRF(
        nirfmxlte_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1.95e9,
            reference_level=0.0,
            external_attenuation=0.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxlte_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxlte_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxlte_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=False,
        )
    )

    client.CfgComponentCarrier(
        nirfmxlte_types.CfgComponentCarrierRequest(
            instrument=instr,
            selector_string="",
            component_carrier_bandwidth=10e6,
            component_carrier_frequency=0.0,
            cell_id=0,
        )
    )

    client.CfgBand(
        nirfmxlte_types.CfgBandRequest(
            instrument=instr,
            selector_string="",
            band=1,
        )
    )

    client.CfgDuplexScheme(
        nirfmxlte_types.CfgDuplexSchemeRequest(
            instrument=instr,
            selector_string="",
            duplex_scheme=nirfmxlte_types.DUPLEX_SCHEME_FDD,
            uplink_downlink_configuration=nirfmxlte_types.UPLINK_DOWNLINK_CONFIGURATION_0,
        )
    )

    client.CfgAutoDMRSDetectionEnabled(
        nirfmxlte_types.CfgAutoDMRSDetectionEnabledRequest(
            instrument=instr,
            selector_string="",
            auto_dmrs_detection_enabled=nirfmxlte_types.AUTO_DMRS_DETECTION_ENABLED_TRUE,
        )
    )

    client.SelectMeasurements(
        nirfmxlte_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxlte_types.MEASUREMENT_TYPES_MODACC,
            enable_all_traces=True,
        )
    )

    client.ModAccCfgSynchronizationModeAndInterval(
        nirfmxlte_types.ModAccCfgSynchronizationModeAndIntervalRequest(
            instrument=instr,
            selector_string="",
            synchronization_mode=nirfmxlte_types.MODACC_SYNCHRONIZATION_MODE_SLOT,
            measurement_offset=0,
            measurement_length=1,
        )
    )

    client.ModAccCfgEVMUnit(
        nirfmxlte_types.ModAccCfgEVMUnitRequest(
            instrument=instr,
            selector_string="",
            evm_unit=nirfmxlte_types.MODACC_EVM_UNIT_PERCENTAGE,
        )
    )

    client.ModAccCfgInBandEmissionMaskType(
        nirfmxlte_types.ModAccCfgInBandEmissionMaskTypeRequest(
            instrument=instr,
            selector_string="",
            in_band_emission_mask_type=nirfmxlte_types.MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS,
        )
    )

    client.ModAccCfgAveraging(
        nirfmxlte_types.ModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxlte_types.MODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxlte_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    modacc_fetch_composite_evm_response = client.ModAccFetchCompositeEVM(
        nirfmxlte_types.ModAccFetchCompositeEVMRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(modacc_fetch_composite_evm_response, instr)

    mean_rms_composite_evm = modacc_fetch_composite_evm_response.mean_rms_composite_evm
    max_peak_composite_evm = modacc_fetch_composite_evm_response.maximum_peak_composite_evm
    mean_frequency_error = modacc_fetch_composite_evm_response.mean_frequency_error
    peak_composite_evm_symbol_index = (
        modacc_fetch_composite_evm_response.peak_composite_evm_symbol_index
    )
    peak_composite_evm_subcarrier_index = (
        modacc_fetch_composite_evm_response.peak_composite_evm_subcarrier_index
    )
    peak_composite_evm_slot_index = (
        modacc_fetch_composite_evm_response.peak_composite_evm_slot_index
    )
    modacc_fetch_iq_impairments_response = client.ModAccFetchIQImpairments(
        nirfmxlte_types.ModAccFetchIQImpairmentsRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(modacc_fetch_iq_impairments_response, instr)
    mean_iq_origin_offset = modacc_fetch_iq_impairments_response.mean_iq_origin_offset
    mean_iq_gain_imbalance = modacc_fetch_iq_impairments_response.mean_iq_gain_imbalance
    mean_iq_quadrature_error = modacc_fetch_iq_impairments_response.mean_iq_quadrature_error

    modacc_fetch_in_band_emission_margin_response = client.ModAccFetchInBandEmissionMargin(
        nirfmxlte_types.ModAccFetchInBandEmissionMarginRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(modacc_fetch_in_band_emission_margin_response, instr)

    in_band_emission_margin = modacc_fetch_in_band_emission_margin_response.in_band_emission_margin

    modacc_fetch_pusch_constellation_trace_response = client.ModAccFetchPUSCHConstellationTrace(
        nirfmxlte_types.ModAccFetchPUSCHConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(modacc_fetch_pusch_constellation_trace_response, instr)
    data_constellation = modacc_fetch_pusch_constellation_trace_response.data_constellation
    dmrs_constellation = modacc_fetch_pusch_constellation_trace_response.dmrs_constellation

    modacc_fetch_evm_per_subcarrier_trace_response = client.ModAccFetchEVMPerSubcarrierTrace(
        nirfmxlte_types.ModAccFetchEVMPerSubcarrierTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(modacc_fetch_evm_per_subcarrier_trace_response, instr)
    x0 = modacc_fetch_evm_per_subcarrier_trace_response.x0
    dx = modacc_fetch_evm_per_subcarrier_trace_response.dx
    mean_rmsevm_per_subcarrier = (
        modacc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier
    )

    print("------------------Measurement------------------")
    print(f"Mean RMS Composite EVM (% or dB)     : {mean_rms_composite_evm}")
    print(f"Max Peak Composite EVM (% or dB)     : {max_peak_composite_evm}")
    print(f"Peak Composite EVM Slot Index        : {peak_composite_evm_slot_index}")
    print(f"Peak Composite EVM Symbol Index      : {peak_composite_evm_symbol_index}")
    print(f"Peak Composite EVM Subcarrier Index  : {peak_composite_evm_subcarrier_index}")
    print(f"Mean Frequency Error (Hz)            : {mean_frequency_error}")
    print(f"Mean IQ Origin Offset (dBc)          : {mean_iq_origin_offset}")
    print(f"Mean IQ Gain Imbalance (dB)          : {mean_iq_gain_imbalance}")
    print(f"Mean IQ Quadrature Error (deg)       : {mean_iq_quadrature_error}")
    print(f"In Band Emission Margin (dB)         : {in_band_emission_margin}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxlte_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxnr/acp-single-carrier.py sha256=fcff36165e3af91eb5143a9a75f0be7bdca21e89db1da3f4ebe1f6ff05dd225f bytes=12527 -->
## FILE: examples/nirfmxnr/acp-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxnr/acp-single-carrier.py`
- sha256: `fcff36165e3af91eb5143a9a75f0be7bdca21e89db1da3f4ebe1f6ff05dd225f`
- bytes: 12527

````python
r"""Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation).
  5. Configure Trigger Parameters for IQ Power Edge Trigger.
  6. Configure Link Direction, Frequency Range and Carrier Bandwidth and Subcarrier Spacing.
  7. Configure Reference Level.
  8. Select ACP measurement and enable Traces.
  9. Configure Measurement Method.
  10. Configure Noise Compensation Parameter.
  11. Configure Sweep Time Parameters.
  12. Configure Averaging Parameters for ACP measurement.
  13. Initiate the Measurement.
  14. Fetch ACP Measurements and Traces.
  15. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxNRSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxnr.NiRFmxNRStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxnr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxnr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxnr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10.0e6,
        )
    )

    client.SetAttributeString(
        nirfmxnr_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgFrequency(
        nirfmxnr_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=3.5e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxnr_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgRFAttenuation(
        nirfmxnr_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxnr_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxnr_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxnr_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=8.0e-6,
            iq_power_edge_level_type=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=False,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
            attr_val=20e6,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
            attr_val=30e3,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxnr_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=10.0e-3
            )
        )
        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)        : {reference_level}")
    else:
        client.CfgReferenceLevel(
            nirfmxnr_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.0
            )
        )

    client.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxnr_types.MEASUREMENT_TYPES_ACP,
            enable_all_traces=True,
        )
    )

    client.ACPCfgMeasurementMethod(
        nirfmxnr_types.ACPCfgMeasurementMethodRequest(
            instrument=instr,
            selector_string="",
            measurement_method=nirfmxnr_types.ACP_MEASUREMENT_METHOD_NORMAL,
        )
    )

    client.ACPCfgNoiseCompensationEnabled(
        nirfmxnr_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxnr_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )

    client.ACPCfgSweepTime(
        nirfmxnr_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxnr_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=1.0e-3,
        )
    )

    client.ACPCfgAveraging(
        nirfmxnr_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxnr_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxnr_types.ACP_AVERAGING_TYPE_RMS,
        )
    )

    initiate_response = client.Initiate(
        nirfmxnr_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch results ###

    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxnr_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)
    array_size = len(acp_fetch_offset_measurement_array_response.lower_relative_power)
    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    acp_fetch_component_carrier_measurement_response = client.ACPFetchComponentCarrierMeasurement(
        nirfmxnr_types.ACPFetchComponentCarrierMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_component_carrier_measurement_response, instr)
    absolute_power = acp_fetch_component_carrier_measurement_response.absolute_power
    relative_power = acp_fetch_component_carrier_measurement_response.relative_power

    for i in range(array_size):
        acp_fetch_relative_powers_trace_response = client.ACPFetchRelativePowersTrace(
            nirfmxnr_types.ACPFetchRelativePowersTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
                trace_index=i,
            )
        )
        check_for_warning(acp_fetch_relative_powers_trace_response, instr)
        x0 = acp_fetch_relative_powers_trace_response.x0
        dx = acp_fetch_relative_powers_trace_response.dx
        relative_powers_trace = acp_fetch_relative_powers_trace_response.relative_powers_trace

    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxnr_types.ACPFetchSpectrumRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    print(f"\nCarrier Absolute Power (dBm or dBm/Hz) : {absolute_power}")

    print("\n-----------Offset Channel Measurements----------- \n")
    for i in range(array_size):
        print(f"Offset  {i}")
        print(f"Lower Relative Power (dB)              : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)              : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm or dBm/Hz)   : {lower_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm or dBm/Hz)   : {upper_absolute_power[i]}")
        print("-------------------------------------------------\n")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxnr_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxnr/acp-txp-modacc-single-carrier.py sha256=21119c901af4b267c15cba26e8dd585504511ae998017bb338cdb9fb62af2a76 bytes=17445 -->
## FILE: examples/nirfmxnr/acp-txp-modacc-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxnr/acp-txp-modacc-single-carrier.py`
- sha256: `21119c901af4b267c15cba26e8dd585504511ae998017bb338cdb9fb62af2a76`
- bytes: 17445

````python
r"""Fetch ACP, ModAcc, and TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation).
  5. Configure Trigger Type and Trigger Parameters.
  6. Configure Link Direction, Frequency Range and Carrier Bandwidth and Subcarrier Spacing.
  7. Configure Reference Level.
  8. Select ACP, ModAcc, and TXP measurements and enable Traces.
  9. Configure ACP Measurement Method.
  10. Configure ACP Noise Compensation Parameter.
  11. Configure ACP Sweep Time Parameters.
  12. Configure ACP Averaging Parameters.
  13. Configure TXP Measurement Interval.
  14. Configure TXP Averaging Parameters.
  15. Configure ModAcc Measurement Interval.
  16. Configure ModAcc Averaging Parameters.
  17. Initiate the Measurement.
  18. Fetch ACP, TXP, and ModAcc Measurements.
  19. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-txp-modacc-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxnr.NiRFmxNRStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxnr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxnr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxnr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10.0e6,
        )
    )

    client.SetAttributeString(
        nirfmxnr_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgFrequency(
        nirfmxnr_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=3.5e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxnr_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgRFAttenuation(
        nirfmxnr_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxnr_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxnr_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0,
            digital_edge=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=True,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxnr_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxnr_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=8.0e-6,
            iq_power_edge_level_type=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=False,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
            attr_val=20e6,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
            attr_val=30e3,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxnr_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=10.0e-3
            )
        )
        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)        : {reference_level}\n")
    else:
        client.CfgReferenceLevel(
            nirfmxnr_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.0
            )
        )

    client.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxnr_types.MEASUREMENT_TYPES_ACP
            | nirfmxnr_types.MEASUREMENT_TYPES_MODACC
            | nirfmxnr_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    client.ACPCfgMeasurementMethod(
        nirfmxnr_types.ACPCfgMeasurementMethodRequest(
            instrument=instr,
            selector_string="",
            measurement_method=nirfmxnr_types.ACP_MEASUREMENT_METHOD_NORMAL,
        )
    )

    client.ACPCfgNoiseCompensationEnabled(
        nirfmxnr_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxnr_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )

    client.ACPCfgSweepTime(
        nirfmxnr_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxnr_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=1.0e-3,
        )
    )

    client.ACPCfgAveraging(
        nirfmxnr_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxnr_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxnr_types.ACP_AVERAGING_TYPE_RMS,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_INTERVAL,
            attr_val=1.0e-3,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_TRUE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_COUNT,
            attr_val_raw=10,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET,
            attr_val=0.0,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH,
            attr_val=1.0,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_FALSE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_COUNT,
            attr_val_raw=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxnr_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    # Fetch results

    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxnr_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)
    array_size = len(acp_fetch_offset_measurement_array_response.lower_relative_power)
    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    acp_fetch_component_carrier_measurement_response = client.ACPFetchComponentCarrierMeasurement(
        nirfmxnr_types.ACPFetchComponentCarrierMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_component_carrier_measurement_response, instr)
    absolute_power = acp_fetch_component_carrier_measurement_response.absolute_power
    relative_power = acp_fetch_component_carrier_measurement_response.relative_power

    for i in range(array_size):
        acp_fetch_relative_powers_trace_response = client.ACPFetchRelativePowersTrace(
            nirfmxnr_types.ACPFetchRelativePowersTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
                trace_index=i,
            )
        )
        check_for_warning(acp_fetch_relative_powers_trace_response, instr)
        x0 = acp_fetch_relative_powers_trace_response.x0
        dx = acp_fetch_relative_powers_trace_response.dx
        relative_powers_trace = acp_fetch_relative_powers_trace_response.relative_powers_trace

    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxnr_types.ACPFetchSpectrumRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    # Fetch modacc results
    modacc_fetch_composite_evm = client.ModAccFetchCompositeEVM(
        nirfmxnr_types.ModAccFetchCompositeEVMRequest(
            instrument=instr, selector_string="", timeout=10.0
        )
    )
    check_for_warning(modacc_fetch_composite_evm, instr)
    composite_rms_evm_mean = modacc_fetch_composite_evm.composite_rms_evm_mean
    composite_peak_evm_maximum = modacc_fetch_composite_evm.composite_peak_evm_maximum

    # Fetch txp results
    txp_fetch_measurement_response = client.TXPFetchMeasurement(
        nirfmxnr_types.TXPFetchMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_measurement_response, instr)
    avearge_power_mean = txp_fetch_measurement_response.average_power_mean
    peak_power_maximum = txp_fetch_measurement_response.peak_power_maximum

    print("************************* ModAcc *************************")
    print(f"Composite RMS EVM Mean (%)               : {composite_rms_evm_mean}")
    print(f"Composite Peak EVM Maximum (%)           : {composite_peak_evm_maximum}\n")
    print("************************* TXP *************************")
    print(f"Average Power Mean (dBm) : {avearge_power_mean}")
    print(f"Peak Power Maximum (dBm) : {peak_power_maximum}\n")
    print("************************* ACP *************************")
    print(f"Carrier Absolute Power (dBm or dBm/Hz) : {absolute_power}")
    print("\n-----------Offset Channel Measurements----------- \n")
    for i in range(array_size):
        print(f"Offset  {i}")
        print(f"Lower Relative Power (dB)              : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)              : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm or dBm/Hz)   : {lower_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm or dBm/Hz)   : {upper_absolute_power[i]}")
        print("-------------------------------------------------\n")


except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxnr_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxnr/modacc-noncontiguous-multicarrier.py sha256=e6a5f927925c36616d84f256b6c0820c503db25349ad9abc8a07fc48018ad09d bytes=29798 -->
## FILE: examples/nirfmxnr/modacc-noncontiguous-multicarrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxnr/modacc-noncontiguous-multicarrier.py`
- sha256: `e6a5f927925c36616d84f256b6c0820c503db25349ad9abc8a07fc48018ad09d`
- bytes: 29798

````python
r"""Fetch ACP, ModAcc, and TXP data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure Selected Ports.
4. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
5. Configure Trigger Type and Trigger Parameters.
6. Configure Auto Increment Cell ID Enabled, Auto RB Detection Enabled and Number of Subblocks.
7. Configure Subblocks and Carriers.
8. Configure PUSCH for all Carriers in each Subblock.
9. Configure PUSCH DMRS for all Carriers in each Subblock.
10. Select ModAcc measurement and enable Traces.
11. Configure Synchronization Mode for ModAcc measurement.
12. Configure Measurement Interval.
13. Initiate the Measurement.
14. Fetch ModAcc Measurements.
15. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python modacc-noncontiguous-multicarrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Initialize variables
NUMBER_OF_SUBBLOCKS = 2
SUBBLOCK_FREQUENCY = [0, 200e6]
NUMBER_OF_COMPONENT_CARRIERS = 2
BAND = [78, 78]
COMPONENT_CARRIER_SPACING_TYPE = [
    nirfmxnr_types.NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL,
    nirfmxnr_types.NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL,
]
COMPONENT_CARRIER_AT_CENTER_FREQUENCY = [-1, -1]
CHANNEL_RASTER = [15e3, 15e3]
COMPONENT_CARRIER_BANDWIDTH = [[100e6, 100e6], [100e6, 100e6]]
COMPONENT_CARRIER_FREQUENCY = [[-49.98e6, 49.98e6], [-49.98e6, 49.98e6]]
CELL_ID = [[0, 1], [0, 1]]

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxnr.NiRFmxNRStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxnr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxnr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxnr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10.0e6,
        )
    )

    client.SetAttributeString(
        nirfmxnr_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgFrequency(
        nirfmxnr_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=3.5e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxnr_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgRFAttenuation(
        nirfmxnr_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxnr_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxnr_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0,
            digital_edge=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=True,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxnr_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxnr_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=8.0e-6,
            iq_power_edge_level_type=nirfmxnr_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=False,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_AUTO_INCREMENT_CELL_ID_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_AUTO_INCREMENT_CELL_ID_ENABLED_TRUE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_NUMBER_OF_SUBBLOCKS,
            attr_val_raw=NUMBER_OF_SUBBLOCKS,
        )
    )

    for i in range(NUMBER_OF_SUBBLOCKS):
        build_subblock_string_response = client.BuildSubblockString(
            nirfmxnr_types.BuildSubblockStringRequest(
                selector_string="",
                subblock_number=i,
            )
        )
        check_for_warning(build_subblock_string_response, instr)
        subblock_string = build_subblock_string_response.selector_string_out

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1,
            )
        )

        client.SetAttributeF64(
            nirfmxnr_types.SetAttributeF64Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SUBBLOCK_FREQUENCY,
                attr_val=SUBBLOCK_FREQUENCY[i],
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BAND,
                attr_val_raw=BAND[i],
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE,
                attr_val_raw=COMPONENT_CARRIER_SPACING_TYPE[i],
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY,
                attr_val_raw=COMPONENT_CARRIER_AT_CENTER_FREQUENCY[i],
            )
        )

        client.SetAttributeF64(
            nirfmxnr_types.SetAttributeF64Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER,
                attr_val=CHANNEL_RASTER[i],
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=subblock_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS,
                attr_val_raw=NUMBER_OF_COMPONENT_CARRIERS,
            )
        )

        for j in range(NUMBER_OF_COMPONENT_CARRIERS):
            build_carrier_string_response = client.BuildCarrierString(
                nirfmxnr_types.BuildCarrierStringRequest(
                    selector_string=subblock_string,
                    carrier_number=j,
                )
            )
            check_for_warning(build_carrier_string_response, instr)
            carrier_string = build_carrier_string_response.selector_string_out

            client.SetAttributeF64(
                nirfmxnr_types.SetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
                    attr_val=COMPONENT_CARRIER_BANDWIDTH[i][j],
                )
            )

            client.SetAttributeF64(
                nirfmxnr_types.SetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY,
                    attr_val=COMPONENT_CARRIER_FREQUENCY[i][j],
                )
            )

            client.SetAttributeI32(
                nirfmxnr_types.SetAttributeI32Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_CELL_ID,
                    attr_val_raw=CELL_ID[i][j],
                )
            )

        build_carrier_string_response = client.BuildCarrierString(
            nirfmxnr_types.BuildCarrierStringRequest(
                selector_string=subblock_string,
                carrier_number=-1,
            )
        )
        check_for_warning(build_carrier_string_response, instr)
        carrier_string = build_carrier_string_response.selector_string_out

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_TRANSFORM_PRECODING_ENABLED,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE,
            )
        )

        client.SetAttributeString(
            nirfmxnr_types.SetAttributeStringRequest(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_SLOT_ALLOCATION,
                attr_val_raw="0-Last",
            )
        )

        client.SetAttributeString(
            nirfmxnr_types.SetAttributeStringRequest(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_SYMBOL_ALLOCATION,
                attr_val_raw="0-Last",
            )
        )

        client.SetAttributeF64(
            nirfmxnr_types.SetAttributeF64Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
                attr_val=30e3,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER_MODE,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_DMRS_POWER_MODE_CDM_GROUPS,
            )
        )

        client.SetAttributeF64(
            nirfmxnr_types.SetAttributeF64Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER,
                attr_val=0.0,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_CONFIGURATION_TYPE,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_DMRS_CONFIGURATION_TYPE_1,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_MAPPING_TYPE,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_MAPPING_TYPE_A,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_TYPE_A_POSITION,
                attr_val_raw=2,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_DURATION,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_DMRS_DURATION_SINGLE_SYMBOL,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_DURATION,
                attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_PUSCH_DMRS_DURATION_SINGLE_SYMBOL,
            )
        )

        client.SetAttributeI32(
            nirfmxnr_types.SetAttributeI32Request(
                instrument=instr,
                selector_string=carrier_string,
                attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_ADDITIONAL_POSITIONS,
                attr_val_raw=0,
            )
        )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxnr_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=10.0e-3
            )
        )
        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)        : {reference_level}\n")
    else:
        client.CfgReferenceLevel(
            nirfmxnr_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.0
            )
        )

    client.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxnr_types.MEASUREMENT_TYPES_MODACC,
            enable_all_traces=True,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_SYNCHRONIZATION_MODE,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_SLOT,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET,
            attr_val=0.0,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH,
            attr_val=1.0,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_FALSE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_COUNT,
            attr_val_raw=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxnr_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    # Fetch results
    composite_rms_evm_mean = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    composite_peak_evm_maximum = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    composite_peak_evm_slot_index = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    composite_peak_evm_symbol_index = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    composite_peak_evm_subcarrier_index = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    component_carrier_frequency_error_mean = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    component_carrier_iq_origin_offset_mean = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    component_carrier_iq_gain_imbalance_mean = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    component_carrier_quadrature_error_mean = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]
    in_band_emission_margin = [
        [0.0] * NUMBER_OF_COMPONENT_CARRIERS for i in range(NUMBER_OF_SUBBLOCKS)
    ]

    for i in range(NUMBER_OF_SUBBLOCKS):
        build_subblock_string_response = client.BuildSubblockString(
            nirfmxnr_types.BuildSubblockStringRequest(
                selector_string="",
                subblock_number=i,
            )
        )
        check_for_warning(build_subblock_string_response, instr)
        subblock_string = build_subblock_string_response.selector_string_out

        for j in range(NUMBER_OF_COMPONENT_CARRIERS):
            build_carrier_string_response = client.BuildCarrierString(
                nirfmxnr_types.BuildCarrierStringRequest(
                    selector_string=subblock_string,
                    carrier_number=j,
                )
            )
            check_for_warning(build_carrier_string_response, instr)
            carrier_string = build_carrier_string_response.selector_string_out

            modacc_fetch_composite_evm = client.ModAccFetchCompositeEVM(
                nirfmxnr_types.ModAccFetchCompositeEVMRequest(
                    instrument=instr, selector_string=carrier_string, timeout=10.0
                )
            )
            check_for_warning(modacc_fetch_composite_evm, instr)
            composite_rms_evm_mean[i][j] = modacc_fetch_composite_evm.composite_rms_evm_mean
            composite_peak_evm_maximum[i][j] = modacc_fetch_composite_evm.composite_peak_evm_maximum

            modacc_fetch_composite_peak_evm_slot_index = client.GetAttributeI32(
                nirfmxnr_types.GetAttributeI32Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX,
                )
            )
            check_for_warning(modacc_fetch_composite_peak_evm_slot_index, instr)
            composite_peak_evm_slot_index[i][
                j
            ] = modacc_fetch_composite_peak_evm_slot_index.attr_val_raw

            modacc_fetch_composite_peak_evm_symbol_index = client.GetAttributeI32(
                nirfmxnr_types.GetAttributeI32Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX,
                )
            )
            check_for_warning(modacc_fetch_composite_peak_evm_symbol_index, instr)
            composite_peak_evm_symbol_index[i][
                j
            ] = modacc_fetch_composite_peak_evm_symbol_index.attr_val_raw

            modacc_fetch_composite_peak_evm_subcarrier_index = client.GetAttributeI32(
                nirfmxnr_types.GetAttributeI32Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SUBCARRIER_INDEX,
                )
            )
            check_for_warning(modacc_fetch_composite_peak_evm_subcarrier_index, instr)
            composite_peak_evm_subcarrier_index[i][
                j
            ] = modacc_fetch_composite_peak_evm_subcarrier_index.attr_val_raw

            modacc_fetch_component_carrier_frequency_error_mean = client.GetAttributeF64(
                nirfmxnr_types.GetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_FREQUENCY_ERROR_MEAN,
                )
            )
            check_for_warning(modacc_fetch_component_carrier_frequency_error_mean, instr)
            component_carrier_frequency_error_mean[i][
                j
            ] = modacc_fetch_component_carrier_frequency_error_mean.attr_val

            modacc_fetch_component_carrier_iq_origin_offset_mean = client.GetAttributeF64(
                nirfmxnr_types.GetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_ORIGIN_OFFSET_MEAN,
                )
            )
            check_for_warning(modacc_fetch_component_carrier_iq_origin_offset_mean, instr)
            component_carrier_iq_origin_offset_mean[i][
                j
            ] = modacc_fetch_component_carrier_iq_origin_offset_mean.attr_val

            modacc_fetch_component_carrier_iq_gain_imbalance_mean = client.GetAttributeF64(
                nirfmxnr_types.GetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_GAIN_IMBALANCE_MEAN,
                )
            )
            check_for_warning(modacc_fetch_component_carrier_iq_gain_imbalance_mean, instr)
            component_carrier_iq_gain_imbalance_mean[i][
                j
            ] = modacc_fetch_component_carrier_iq_gain_imbalance_mean.attr_val

            modacc_fetch_component_carrier_quadrature_error_mean = client.GetAttributeF64(
                nirfmxnr_types.GetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN,
                )
            )
            check_for_warning(modacc_fetch_component_carrier_quadrature_error_mean, instr)
            component_carrier_quadrature_error_mean[i][
                j
            ] = modacc_fetch_component_carrier_quadrature_error_mean.attr_val

            modacc_fetch_in_band_emission_margin = client.GetAttributeF64(
                nirfmxnr_types.GetAttributeF64Request(
                    instrument=instr,
                    selector_string=carrier_string,
                    attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_IN_BAND_EMISSION_MARGIN,
                )
            )
            check_for_warning(modacc_fetch_in_band_emission_margin, instr)
            in_band_emission_margin[i][j] = modacc_fetch_in_band_emission_margin.attr_val

    print("************************* ModAcc Results *************************")
    for i in range(NUMBER_OF_SUBBLOCKS):
        print(f"Subblock  :   {i}\n")
        for j in range(NUMBER_OF_COMPONENT_CARRIERS):
            print(f"Carrier  :   {j}")
            print(f"Composite RMS EVM Mean (%)                    : {composite_rms_evm_mean[i][j]}")
            print(
                f"Composite Peak EVM Maximum (%)                : {composite_peak_evm_maximum[i][j]}"
            )
            print(
                f"Composite Peak EVM Slot Index                 : {composite_peak_evm_slot_index[i][j]}"
            )
            print(
                f"Composite Peak EVM Symbol Index               : {composite_peak_evm_symbol_index[i][j]}"
            )
            print(
                f"Composite Peak EVM Subcarrier Index           : {composite_peak_evm_subcarrier_index[i][j]}\n"
            )
            print(
                f"Component Carrier Frequency Error Mean (Hz)   : {component_carrier_frequency_error_mean[i][j]}"
            )
            print(
                f"Component Carrier IQ Origin Offset Mean (dBc) : {component_carrier_iq_origin_offset_mean[i][j]}"
            )
            print(
                f"Component Carrier IQ Gain Imbalance Mean (dB) : {component_carrier_iq_gain_imbalance_mean[i][j]}"
            )
            print(
                f"Component Carrier Quadrature Error Mean (Hz)  : {component_carrier_quadrature_error_mean[i][j]}"
            )
            print(
                f"In-Band Emission Margin (dB)                  : {in_band_emission_margin[i][j]}\n"
            )
            print("******************************************************************\n")

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxnr_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxnr/txp-single-carrier.py sha256=f810c7bc96c3cd4c8e457297ec8586e9d6242d057bce79795ac4c7a19d009d18 bytes=9219 -->
## FILE: examples/nirfmxnr/txp-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxnr/txp-single-carrier.py`
- sha256: `f810c7bc96c3cd4c8e457297ec8586e9d6242d057bce79795ac4c7a19d009d18`
- bytes: 9219

````python
r"""Fetch TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  5. Configure Trigger Parameters for Digital Edge Trigger.
  6. Configure Link Direction, Frequency Range, Carrier Bandwidthand Subcarrier Spacing.
  7. Select TXP measurement and enable Traces.
  8. Configure Measurement Offset & Measurement Length Parameters and Averaging Parameters for TXP
     measurement.
  9. Initiate the Measurement.
  10. Fetch TXP Measurements and Traces.
  11. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxnr_pb2 as nirfmxnr_types
import nirfmxnr_pb2_grpc as grpc_nirfmxnr

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxNRSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxnr.NiRFmxNRStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxnr_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = client.Initialize(
        nirfmxnr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.CfgFrequencyReference(
        nirfmxnr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxnr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.SetAttributeString(
        nirfmxnr_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgRF(
        nirfmxnr_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=3.5e9,
            reference_level=0.0,
            external_attenuation=0.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxnr_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0,
            digital_edge=nirfmxnr_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.0,
            enable_trigger=False,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_LINK_DIRECTION,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_LINK_DIRECTION_UPLINK,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH,
            attr_val=20e6,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING,
            attr_val=30e3,
        )
    )

    client.SelectMeasurements(
        nirfmxnr_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxnr_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_INTERVAL,
            attr_val=1.0e-3,
        )
    )

    client.SetAttributeF64(
        nirfmxnr_types.SetAttributeF64Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_OFFSET,
            attr_val=0.0,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_ENABLED,
            attr_val_raw=nirfmxnr_types.NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_TRUE,
        )
    )

    client.SetAttributeI32(
        nirfmxnr_types.SetAttributeI32Request(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxnr_types.NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_COUNT,
            attr_val_raw=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxnr_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)
    ### Fetch results ###

    txp_fetch_measurement_response = client.TXPFetchMeasurement(
        nirfmxnr_types.TXPFetchMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_measurement_response, instr)
    avearge_power_mean = txp_fetch_measurement_response.average_power_mean
    peak_power_maximum = txp_fetch_measurement_response.peak_power_maximum

    txp_fetch_power_trace_response = client.TXPFetchPowerTrace(
        nirfmxnr_types.TXPFetchPowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_power_trace_response, instr)
    x0 = txp_fetch_power_trace_response.x0
    dx = txp_fetch_power_trace_response.dx
    power = txp_fetch_power_trace_response.power

    print("\n------------Measurement------------\n")
    print(f"Average Power Mean (dBm) : {avearge_power_mean}")
    print(f"Peak Power Maximum (dBm) : {peak_power_maximum}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxnr_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxspecan/acp-basic.py sha256=52752ac912639da520933b68680a2e83390f668951cd6dd691e7d86f64ec683d bytes=6352 -->
## FILE: examples/nirfmxspecan/acp-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxspecan/acp-basic.py`
- sha256: `52752ac912639da520933b68680a2e83390f668951cd6dd691e7d86f64ec683d`
- bytes: 6352

````python
r"""Fetch ACP data.

Steps:
  1. Open a new RFmx session
  2. Configure Selected Ports
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  4. Configure ACP Averaging Parameters
  5. Configure ACP Integration BW, Number of Offset Channels and Channel Spacing
     This function configures a Carrier Channel with Offset Channels as specified by the Number of
     Offsets.
  6. Read ACP Measurement Results
     This function returns Absolute Power for the Carrier Channel and Relative Powers for two Offset
     Channels.
  7. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxspecan_pb2 as nirfmxspecan_types
import nirfmxspecan_pb2_grpc as grpc_nirfmxspecan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxSpecAnSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxspecan.NiRFmxSpecAnStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxspecan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = client.Initialize(
        nirfmxspecan_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.SetAttributeString(
        nirfmxspecan_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxspecan_types.NIRFMXSPECAN_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgRF(
        nirfmxspecan_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )

    client.ACPCfgAveraging(
        nirfmxspecan_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxspecan_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxspecan_types.ACP_AVERAGING_TYPE_RMS,
        )
    )

    client.ACPCfgCarrierAndOffsets(
        nirfmxspecan_types.ACPCfgCarrierAndOffsetsRequest(
            instrument=instr,
            selector_string="",
            integration_bandwidth=1.0e6,
            number_of_offsets=2,
            channel_spacing=1.0e6,
        )
    )

    ### Read ACP measurements ###

    acp_read_response = client.ACPRead(
        nirfmxspecan_types.ACPReadRequest(
            instrument=instr,
            selector_string="",
            timeout=10,
        )
    )
    check_for_warning(acp_read_response, instr)

    off_ch1_upper_relative_power = acp_read_response.offset_ch1_upper_relative_power
    off_ch1_lower_relative_power = acp_read_response.offset_ch1_lower_relative_power
    off_ch0_upper_relative_power = acp_read_response.offset_ch0_upper_relative_power
    off_ch0_lower_relative_power = acp_read_response.offset_ch0_lower_relative_power
    carrier_abs_power = acp_read_response.carrier_absolute_power

    print(f"Carrier Absolute Power (dBm or dBm/Hz)  {carrier_abs_power}")
    print(f"Offset ch0 Lower Relative Power (dB)    {off_ch0_lower_relative_power}")
    print(f"Offset ch0 Upper Relative Power(dB)     {off_ch0_upper_relative_power}")
    print(f"Offset ch1 Lower Relative Power(dB)     {off_ch1_lower_relative_power}")
    print(f"Offset ch1 Upper Relative Power(dB)     {off_ch1_upper_relative_power}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxspecan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxspecan/spectrum-basic.py sha256=bd43ad6c8ab0211e0001b80b93676dc8692ae1f9f8e64aafff708008142095f5 bytes=6005 -->
## FILE: examples/nirfmxspecan/spectrum-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxspecan/spectrum-basic.py`
- sha256: `bd43ad6c8ab0211e0001b80b93676dc8692ae1f9f8e64aafff708008142095f5`
- bytes: 6005

````python
r"""Read a spectrum.

Steps:
  1. Open a new RFmx session
  2. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  3. Configure Spectrum Span
  4. Configure Spectrum RBW filter
  5. Configure Spectrum Averaging
  6. Read Spectrum Measurement Results
  7. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  # https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python spectrum-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the resource name.
"""

import sys
from math import floor

import grpc
import nirfmxspecan_pb2 as nirfmxspecan_types
import nirfmxspecan_pb2_grpc as grpc_nirfmxspecan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSASession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedRFSA"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxspecan.NiRFmxSpecAnStub(channel)
instr = None


def _format_frequency(f):
    # adapted from https://stackoverflow.com/a/1094933
    suffix = "Hz"
    for unit in ["", "k", "M", "G"]:
        if abs(f) < 1000.0:
            return f"{f:3.3f} {unit}{suffix}"
        f /= 1000.0
    return f"{f:.3f} G{suffix}"


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxspecan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    init_response = client.Initialize(
        nirfmxspecan_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = init_response.instrument

    client.CfgRF(
        nirfmxspecan_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0,
            external_attenuation=0,
        )
    )

    client.SpectrumCfgSpan(
        nirfmxspecan_types.SpectrumCfgSpanRequest(
            instrument=instr,
            selector_string="",
            span=1e6,
        )
    )

    client.SpectrumCfgRBWFilter(
        nirfmxspecan_types.SpectrumCfgRBWFilterRequest(
            instrument=instr,
            selector_string="",
            rbw_auto=nirfmxspecan_types.SPECTRUM_RBW_AUTO_BANDWIDTH_TRUE,
            rbw=100e3,
            rbw_filter_type=nirfmxspecan_types.SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN,
        )
    )

    client.SpectrumCfgAveraging(
        nirfmxspecan_types.SpectrumCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxspecan_types.SPECTRUM_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxspecan_types.SPECTRUM_AVERAGING_TYPE_RMS,
        )
    )

    read_response = client.SpectrumRead(
        nirfmxspecan_types.SpectrumReadRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(read_response, instr)

    print(
        f"min frequency: {_format_frequency(read_response.x0)}: {read_response.spectrum[0]:.1f} dBm"
    )
    midpoint_x = floor(read_response.actual_array_size / 2)
    print(
        f"midpoint frequency: {_format_frequency(read_response.x0 + read_response.dx * midpoint_x)}: {read_response.spectrum[midpoint_x]:.1f} dBm"
    )
    print(
        f"max frequency: {_format_frequency(read_response.x0 + read_response.dx * (read_response.actual_array_size - 1))}: {read_response.spectrum[-1]:.1f} dBm"
    )
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxspecan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxspecan/txp-basic.py sha256=faa79afa242db47b5978ff0d111bff2bdb82bdc1eb813b396a0fb482a5586db2 bytes=5975 -->
## FILE: examples/nirfmxspecan/txp-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxspecan/txp-basic.py`
- sha256: `faa79afa242db47b5978ff0d111bff2bdb82bdc1eb813b396a0fb482a5586db2`
- bytes: 5975

````python
r"""Fetch TXP data.

Steps:
  1. Open a new RFmx session
  2. Configure Selected Ports
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  4. Configure TXP rbw
  5. Configure TXP Measurement Interval
  6. Configure TXP Averaging
  7. Read TXP Measurement Results
  8. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxspecan_pb2 as nirfmxspecan_types
import nirfmxspecan_pb2_grpc as grpc_nirfmxspecan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxSpecAnSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxspecan.NiRFmxSpecAnStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxspecan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = client.Initialize(
        nirfmxspecan_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    client.SetAttributeString(
        nirfmxspecan_types.SetAttributeStringRequest(
            instrument=instr,
            selector_string="",
            attribute_id=nirfmxspecan_types.NIRFMXSPECAN_ATTRIBUTE_SELECTED_PORTS,
            attr_val_raw="",
        )
    )

    client.CfgRF(
        nirfmxspecan_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )

    client.TXPCfgMeasurementInterval(
        nirfmxspecan_types.TXPCfgMeasurementIntervalRequest(
            instrument=instr,
            selector_string="",
            measurement_interval=1e-3,
        )
    )

    client.TXPCfgRBWFilter(
        nirfmxspecan_types.TXPCfgRBWFilterRequest(
            instrument=instr,
            selector_string="",
            rbw=100e3,
            rbw_filter_type=nirfmxspecan_types.TXP_RBW_FILTER_TYPE_GAUSSIAN,
            rrc_alpha=0.1,
        )
    )

    client.TXPCfgAveraging(
        nirfmxspecan_types.TXPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxspecan_types.TXP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxspecan_types.TXP_AVERAGING_TYPE_RMS,
        )
    )

    ### Fetch measurement data ###

    txp_read_response = client.TXPRead(
        nirfmxspecan_types.TXPReadRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_read_response, instr)

    minimum_power = txp_read_response.minimum_power
    maximum_power = txp_read_response.maximum_power
    peak_to_average_ratio = txp_read_response.peak_to_average_ratio
    average_mean_power = txp_read_response.average_mean_power

    print(f"Average Mean Power(dBm)    {average_mean_power}")
    print(f"Peak to Average Ratio(dB)  {peak_to_average_ratio}")
    print(f"Maximum Power(dBm)         {maximum_power}")
    print(f"Minimum Power(dBm)         {minimum_power}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxspecan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxtdscdma/acp.py sha256=182194c6dc5a9e9d02bc438960411d071534d36c02931a00fcc6177f08303648 bytes=9420 -->
## FILE: examples/nirfmxtdscdma/acp.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxtdscdma/acp.py`
- sha256: `182194c6dc5a9e9d02bc438960411d071534d36c02931a00fcc6177f08303648`
- bytes: 9420

````python
r"""Acp example.

Steps:
1. Open a new RFmx session.
2. Configure Frequency Reference.
3. Configure External Attenuation.
4. Configure the Center Frequency directly or via Channel Number.
5. Configure Trigger Type and Trigger Parameters.
6. Configure the Reference Level directly or via Auto Level.
7. Select ACP measurement and enable traces.
8. Configure Averaging parameters.
9. Configure Sweep Time parameters.
10. Configure Noise Compensation parameter.
11. Configure Number of Offset Channels.
12. Initiate the Measurement.
13[A-E]. Fetch ACP Measurements and Traces.
14. Close the RFmx session.

The gRPC API is built from the C API. RFmx TDSCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\TDSCDMA\Documentation\tdscdmacvi.chm

Getting Started:

To run this example, install "RFmx TDSCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-tdscdma.html

For instructions on how to use protoc to generate gRPC client interfaces,
see our "Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxTDSCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxTDSCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxtdscdma_pb2 as nirfmxtdscdma_types
import nirfmxtdscdma_pb2_grpc as grpc_nirfmxtdscdma

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxTDSCDMASession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxtdscdma.NiRFmxTDSCDMAStub(channel)
instr = None


NUMBER_OF_OFFSETS = 2


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxtdscdma_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Initialize a session
    initialize_response = client.Initialize(
        nirfmxtdscdma_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxtdscdma_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxtdscdma_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )
    client.CfgExternalAttenuation(
        nirfmxtdscdma_types.CfgExternalAttenuationRequest(
            instrument=instr, selector_string="", external_attenuation=0.00
        )
    )
    client.CfgFrequency(
        nirfmxtdscdma_types.CfgFrequencyRequest(
            instrument=instr, selector_string="", center_frequency=1.91e9
        )
    )
    client.CfgIQPowerEdgeTrigger(
        nirfmxtdscdma_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxtdscdma_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.00,
            trigger_delay=0.00,
            minimum_quiet_time_mode=nirfmxtdscdma_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            minimum_quiet_time=16e-6,
            iq_power_edge_level_type=nirfmxtdscdma_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )
    auto_level = False
    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxtdscdma_types.AutoLevelRequest(
                instrument=instr, selector_string="", measurement_interval=0.005
            )
        )
        reference_level = auto_level_response.reference_level
        print(f"Reference Level (dBm)        : {reference_level}")
    else:
        client.CfgReferenceLevel(
            nirfmxtdscdma_types.CfgReferenceLevelRequest(
                instrument=instr, selector_string="", reference_level=0.00
            )
        )
    client.SelectMeasurements(
        nirfmxtdscdma_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxtdscdma_types.MEASUREMENT_TYPES_ACP,
            enable_all_traces=True,
        )
    )
    client.ACPCfgAveraging(
        nirfmxtdscdma_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxtdscdma_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxtdscdma_types.ACP_AVERAGING_TYPE_RMS,
        )
    )
    client.ACPCfgSweepTime(
        nirfmxtdscdma_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxtdscdma_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=0.000660,
        )
    )
    client.ACPCfgNoiseCompensationEnabled(
        nirfmxtdscdma_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxtdscdma_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )
    client.ACPCfgNumberOfOffsets(
        nirfmxtdscdma_types.ACPCfgNumberOfOffsetsRequest(
            instrument=instr, selector_string="", number_of_offsets=NUMBER_OF_OFFSETS
        )
    )
    client.Initiate(
        nirfmxtdscdma_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )

    # Fetch the measurements array
    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxtdscdma_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    acp_fetch_carrier_absolute_power_response = client.ACPFetchCarrierAbsolutePower(
        nirfmxtdscdma_types.ACPFetchCarrierAbsolutePowerRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    carrier_absolute_power = acp_fetch_carrier_absolute_power_response.carrier_absolute_power
    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxtdscdma_types.ACPFetchSpectrumRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    print(f"Carrier Absolute Power (dBm) : {carrier_absolute_power}")
    for i in range(NUMBER_OF_OFFSETS):
        print(f"\nOffset                       :  {i}")
        print(f"Lower Relative Power (dB)    : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)    : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm)   : {lower_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm)   : {upper_absolute_power[i]}")
        print("-------------------------------------------------")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxtdscdma_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxtdscdma/modacc.py sha256=de8ceca51813a335dae291f472fca1ff2901108303e5b2eb07742f4a24d975e6 bytes=12898 -->
## FILE: examples/nirfmxtdscdma/modacc.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxtdscdma/modacc.py`
- sha256: `de8ceca51813a335dae291f472fca1ff2901108303e5b2eb07742f4a24d975e6`
- bytes: 12898

````python
r"""ModAcc example.

Steps:
1. Open a new RFmx session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Type and Trigger Parameters..
5. Select ModAcc measurement and enable traces.
6. Configure Uplink Scrambling Code.
7. Configure Synchronization Mode and Measurement Interval.
8. Configure Midamble Parameters.
9. Initiate the Measurement.
10. Fetch ModAcc Measurements and Traces.
11. Close the RFmx session.

The gRPC API is built from the C API. RFmx TDSCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\TDSCDMA\Documentation\tdscdmacvi.chm

Getting Started:

To run this example, install "RFmx TDSCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-tdscdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxTDSCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxTDSCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python modacc.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxtdscdma_pb2 as nirfmxtdscdma_types
import nirfmxtdscdma_pb2_grpc as grpc_nirfmxtdscdma

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxTDSCDMASession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxtdscdma.NiRFmxTDSCDMAStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxtdscdma_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    # Initialize a session
    initialize_response = client.Initialize(
        nirfmxtdscdma_types.InitializeRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxtdscdma_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxtdscdma_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )
    client.CfgRF(
        nirfmxtdscdma_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1.91e9,
            reference_level=0.00,
            external_attenuation=0.00,
        )
    )
    client.CfgIQPowerEdgeTrigger(
        nirfmxtdscdma_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxtdscdma_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.00,
            trigger_delay=0.00,
            minimum_quiet_time_mode=nirfmxtdscdma_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            minimum_quiet_time=80e-6,
            iq_power_edge_level_type=nirfmxtdscdma_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )
    client.SelectMeasurements(
        nirfmxtdscdma_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxtdscdma_types.MEASUREMENT_TYPES_MODACC,
            enable_all_traces=True,
        )
    )
    client.ModAccCfgAveraging(
        nirfmxtdscdma_types.ModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxtdscdma_types.MODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )
    client.CfgUplinkScramblingCode(
        nirfmxtdscdma_types.CfgUplinkScramblingCodeRequest(
            instrument=instr, selector_string="", uplink_scrambling_code=0
        )
    )
    client.ModAccCfgSynchronizationModeAndInterval(
        nirfmxtdscdma_types.ModAccCfgSynchronizationModeAndIntervalRequest(
            instrument=instr,
            selector_string="",
            synchronization_mode=nirfmxtdscdma_types.MODACC_SYNCHRONIZATION_MODE_SLOT,
            measurement_offset=0,
            measurement_length=1,
        )
    )
    client.CfgMidambleShift(
        nirfmxtdscdma_types.CfgMidambleShiftRequest(
            instrument=instr,
            selector_string="",
            midamble_auto_detection_mode=nirfmxtdscdma_types.MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT,
            maximum_number_of_users=16,
            midamble_shift=8,
        )
    )

    initiate_response = client.Initiate(
        nirfmxtdscdma_types.InitiateRequest(instrument=instr, selector_string="", result_name="")
    )
    check_for_warning(initiate_response, instr)

    mod_acc_fetch_composite_evm_response = client.ModAccFetchCompositeEVM(
        nirfmxtdscdma_types.ModAccFetchCompositeEVMRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_composite_evm_response, instr)
    rms_composite_evm = mod_acc_fetch_composite_evm_response.rms_composite_evm
    peak_composite_evm = mod_acc_fetch_composite_evm_response.peak_composite_evm
    composite_rho = mod_acc_fetch_composite_evm_response.composite_rho
    frequency_error = mod_acc_fetch_composite_evm_response.frequency_error
    chip_rate_error = mod_acc_fetch_composite_evm_response.chip_rate_error
    rms_composite_magnitude_error = (
        mod_acc_fetch_composite_evm_response.rms_composite_magnitude_error
    )
    rms_composite_phase_error = mod_acc_fetch_composite_evm_response.rms_composite_phase_error

    mod_acc_fetch_data_evm_response = client.ModAccFetchDataEVM(
        nirfmxtdscdma_types.ModAccFetchDataEVMRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_data_evm_response, instr)
    rms_data_evm = mod_acc_fetch_data_evm_response.rms_data_evm
    peak_data_evm = mod_acc_fetch_data_evm_response.peak_data_evm
    data_rho = mod_acc_fetch_data_evm_response.data_rho
    rms_data_magnitude_error = mod_acc_fetch_data_evm_response.rms_data_magnitude_error
    rms_data_phase_error = mod_acc_fetch_data_evm_response.rms_data_phase_error

    mod_acc_fetch_iq_impairments_response = client.ModAccFetchIQImpairments(
        nirfmxtdscdma_types.ModAccFetchIQImpairmentsRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_iq_impairments_response, instr)
    iq_origin_offset = mod_acc_fetch_iq_impairments_response.iq_origin_offset
    iq_gain_imbalance = mod_acc_fetch_iq_impairments_response.iq_gain_imbalance
    iq_quadrature_error = mod_acc_fetch_iq_impairments_response.iq_quadrature_error

    mod_acc_fetch_constellation_trace_response = client.ModAccFetchConstellationTrace(
        nirfmxtdscdma_types.ModAccFetchConstellationTraceRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_constellation_trace_response, instr)
    constellation = mod_acc_fetch_constellation_trace_response.constellation

    mod_acc_fetch_midamble_evm_response = client.ModAccFetchMidambleEVM(
        nirfmxtdscdma_types.ModAccFetchMidambleEVMRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_midamble_evm_response, instr)
    rms_midamble_evm = mod_acc_fetch_midamble_evm_response.rms_midamble_evm
    peak_midamble_evm = mod_acc_fetch_midamble_evm_response.peak_midamble_evm
    midamble_rho = mod_acc_fetch_midamble_evm_response.midamble_rho
    rms_midamble_magnitude_error = mod_acc_fetch_midamble_evm_response.rms_midamble_magnitude_error
    rms_midamble_phase_error = mod_acc_fetch_midamble_evm_response.rms_midamble_phase_error

    mod_acc_fetch_midamble_and_data_power_response = client.ModAccFetchMidambleAndDataPower(
        nirfmxtdscdma_types.ModAccFetchMidambleAndDataPowerRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_midamble_and_data_power_response, instr)
    midamble_power = mod_acc_fetch_midamble_and_data_power_response.midamble_power
    data_field1_power = mod_acc_fetch_midamble_and_data_power_response.data_field1_power
    data_field2_power = mod_acc_fetch_midamble_and_data_power_response.data_field2_power

    mod_acc_fetch_evm_trace_response = client.ModAccFetchEVMTrace(
        nirfmxtdscdma_types.ModAccFetchEVMTraceRequest(
            instrument=instr, selector_string="", timeout=10.00
        )
    )
    check_for_warning(mod_acc_fetch_evm_trace_response, instr)
    x0 = mod_acc_fetch_evm_trace_response.x0
    dx = mod_acc_fetch_evm_trace_response.dx
    evm = mod_acc_fetch_evm_trace_response.evm

    print("Composite evm Results")
    print(f"RMS Composite evm  (%%)             : {rms_composite_evm}")
    print(f"Peak Composite evm  (%%)            : {peak_composite_evm}")
    print(f"Composite Rho                       : {composite_rho}")
    print(f"Frequency Error  (Hz)               : {frequency_error}")
    print(f"Chip Rate Error  (ppm)              : {chip_rate_error}")
    print(f"RMS Composite Phase Error  (deg)    : {rms_composite_phase_error}")
    print(f"RMS Composite Magnitude Error  (%%) : {rms_composite_magnitude_error}")

    print("\nData evm Results")
    print(f"RMS Data evm  (%%)                  : {rms_data_evm}")
    print(f"Peak Data evm  (%%)                 : {peak_data_evm}")
    print(f"Data Rho                            : {data_rho}")
    print(f"RMS Data Phase Error  (deg)         : {rms_data_phase_error}")
    print(f"RMS Data Magnitude Error  (%%)      : {rms_data_magnitude_error}")
    print(f"Data Field1 Power  (dBm)            : {data_field1_power}")
    print(f"Data Field2 Power  (dBm)            : {data_field2_power}")

    print("\nIQ Impairments")
    print(f"I/Q Origin Offset (dB)              : {iq_origin_offset}")
    print(f"I/Q Gain Imbalance (dB)             : {iq_gain_imbalance}")
    print(f"I/Q Quadrature Error (deg)          : {iq_quadrature_error}")

    print("\nMidamble evm")
    print(f"RMS Midamble evm  (%%)              : {rms_midamble_evm}")
    print(f"Peak Midamble evm  (%%)             : {peak_midamble_evm}")
    print(f"Midamble Rho                        : {midamble_rho}")
    print(f"RMS Midamble Phase Error  (deg)     : {rms_midamble_phase_error}")
    print(f"RMS Midamble Magnitude Error  (%%)  : {rms_midamble_magnitude_error}")
    print(f"Midamble Power  (dBm)               : {midamble_power}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxtdscdma_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwcdma/acp-single-carrier.py sha256=c0c54fc096810f7c1a6059b79a8951ad178187e447dd2c3adb35336d6773a672 bytes=10737 -->
## FILE: examples/nirfmxwcdma/acp-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwcdma/acp-single-carrier.py`
- sha256: `c0c54fc096810f7c1a6059b79a8951ad178187e447dd2c3adb35336d6773a672`
- bytes: 10737

````python
r"""Fetch ACP data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation)
4. Configure Trigger Type and Trigger Parameters.
5. Configure Reference Level.
6. Select ACP measurement and enable Traces.
7. Configure Measurement Method.
8. Configure Averaging Parameters for ACP measurement.
9. Configure Sweep Time Parameters.
10. Configure Noise Compensation Parameter.
11. Configure Number of offset channels.
12. Initiate the Measurement.
13. Fetch ACP Measurements and Traces.
14. Close RFmx Session.


The gRPC API is built from the C API. RFmx WCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\WCDMA\Documentation\wcdmacvi.chm

Getting Started:

To run this example, install "RFmx WCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wcdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxWCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxwcdma_pb2 as nirfmxwcdma_types
import nirfmxwcdma_pb2_grpc as grpc_nirfmxwcdma

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWCDMASession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwcdma.NiRFmxWCDMAStub(channel)
instr = None


NUMBER_OF_OFFSETS = 2


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwcdma_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    # Initialize a session
    initialize_response = client.Initialize(
        nirfmxwcdma_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    check_for_warning(initialize_response, instr)

    client.CfgFrequencyReference(
        nirfmxwcdma_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxwcdma_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwcdma_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1.95e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwcdma_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.000000,
        )
    )

    client.CfgRFAttenuation(
        nirfmxwcdma_types.CfgRFAttenuationRequest(
            instrument=instr,
            channel_name="",
            rf_attenuation_auto=nirfmxwcdma_types.RF_ATTENUATION_AUTO_TRUE,
            rf_attenuation_value=10.0,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxwcdma_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxwcdma_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxwcdma_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.000000,
            enable_trigger=False,
        )
    )

    if auto_level:
        auto_level_response = client.AutoLevel(
            nirfmxwcdma_types.AutoLevelRequest(
                instrument=instr,
                selector_string="",
                measurement_interval=0.010000,
            )
        )

        reference_level = auto_level_response.reference_level
        print(f"Reference level (dBm)          : {reference_level}")
    else:
        client.CfgReferenceLevel(
            nirfmxwcdma_types.CfgReferenceLevelRequest(
                instrument=instr,
                selector_string="",
                reference_level=0.000000,
            )
        )

    client.SelectMeasurements(
        nirfmxwcdma_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_array=[nirfmxwcdma_types.MEASUREMENT_TYPES_ACP],
            enable_all_traces=True,
        )
    )

    client.ACPCfgMeasurementMethod(
        nirfmxwcdma_types.ACPCfgMeasurementMethodRequest(
            instrument=instr,
            selector_string="",
            measurement_method=nirfmxwcdma_types.ACP_MEASUREMENT_METHOD_NORMAL,
        )
    )

    client.ACPCfgAveraging(
        nirfmxwcdma_types.ACPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwcdma_types.ACP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxwcdma_types.ACP_AVERAGING_TYPE_RMS,
        )
    )

    client.ACPCfgSweepTime(
        nirfmxwcdma_types.ACPCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxwcdma_types.ACP_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=0.000667,
        )
    )

    client.ACPCfgNoiseCompensationEnabled(
        nirfmxwcdma_types.ACPCfgNoiseCompensationEnabledRequest(
            instrument=instr,
            selector_string="",
            noise_compensation_enabled=nirfmxwcdma_types.ACP_NOISE_COMPENSATION_ENABLED_FALSE,
        )
    )

    client.ACPCfgNumberOfOffsets(
        nirfmxwcdma_types.ACPCfgNumberOfOffsetsRequest(
            instrument=instr,
            selector_string="",
            number_of_offsets=NUMBER_OF_OFFSETS,
        )
    )

    client.Initiate(
        nirfmxwcdma_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )

    # Fetch the measurements array
    acp_fetch_offset_measurement_array_response = client.ACPFetchOffsetMeasurementArray(
        nirfmxwcdma_types.ACPFetchOffsetMeasurementArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(acp_fetch_offset_measurement_array_response, instr)

    lower_relative_power = acp_fetch_offset_measurement_array_response.lower_relative_power
    upper_relative_power = acp_fetch_offset_measurement_array_response.upper_relative_power
    lower_absolute_power = acp_fetch_offset_measurement_array_response.lower_absolute_power
    upper_absolute_power = acp_fetch_offset_measurement_array_response.upper_absolute_power

    assert len(lower_relative_power) == NUMBER_OF_OFFSETS, len(lower_relative_power)
    assert len(upper_relative_power) == NUMBER_OF_OFFSETS, len(upper_relative_power)
    assert len(lower_absolute_power) == NUMBER_OF_OFFSETS, len(lower_absolute_power)
    assert len(upper_absolute_power) == NUMBER_OF_OFFSETS, len(upper_absolute_power)

    acp_fetch_carrier_measurement_response = client.ACPFetchCarrierMeasurement(
        nirfmxwcdma_types.ACPFetchCarrierMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(acp_fetch_carrier_measurement_response, instr)

    absolute_power = acp_fetch_carrier_measurement_response.absolute_power
    relative_power = acp_fetch_carrier_measurement_response.relative_power

    acp_fetch_spectrum_response = client.ACPFetchSpectrum(
        nirfmxwcdma_types.ACPFetchSpectrumRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(acp_fetch_spectrum_response, instr)

    x0 = acp_fetch_spectrum_response.x0
    dx = acp_fetch_spectrum_response.dx
    spectrum = acp_fetch_spectrum_response.spectrum

    print(f"\nCarrier Absolute Power  (dBm)  : {absolute_power}")

    print("\nOffset Channel Measurements: ")
    for i in range(NUMBER_OF_OFFSETS):
        print(f"Offset  :  {i}")
        print(f"Lower Relative Power (dB)      : {lower_relative_power[i]}")
        print(f"Upper Relative Power (dB)      : {upper_relative_power[i]}")
        print(f"Lower Absolute Power (dBm)     : {lower_absolute_power[i]}")
        print(f"Upper Absolute Power (dBm)     : {upper_absolute_power[i]}")
        print("-------------------------------------------------")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwcdma_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwcdma/modacc-single-carrier.py sha256=24280774f94e972cffe3cab9d3e8d45cd2916d2a81e05d9b25bf61f0f7e2dfe3 bytes=12012 -->
## FILE: examples/nirfmxwcdma/modacc-single-carrier.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwcdma/modacc-single-carrier.py`
- sha256: `24280774f94e972cffe3cab9d3e8d45cd2916d2a81e05d9b25bf61f0f7e2dfe3`
- bytes: 12012

````python
r"""Fetch ModAcc data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Type and Trigger Parameters.
5. Configure Uplink Scrambling.
6. Select ModAcc measurement and enable Traces.
7. Configure Synchronization Mode and Measurement Interval.
8. Initiate the Measurement.
9. Fetch ModAcc Measurements and Traces.
10. Close RFmx Session.


The gRPC API is built from the C API. RFmx WCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\WCDMA\Documentation\wcdmacvi.chm

Getting Started:

To run this example, install "RFmx WCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wcdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxWCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxWcdmaModAccSingleCarrier.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name
"""

import sys

import grpc
import nirfmxwcdma_pb2 as nirfmxwcdma_types
import nirfmxwcdma_pb2_grpc as grpc_nirfmxwcdma

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWCDMASession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwcdma.NiRFmxWCDMAStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwcdma_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    actual_array_size = 0

    evm = None  # (%)
    constellation = None

    # Initialize a session
    initialize_response = client.Initialize(
        nirfmxwcdma_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    check_for_warning(initialize_response, instr)

    client.CfgFrequencyReference(
        nirfmxwcdma_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxwcdma_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgRF(
        nirfmxwcdma_types.CfgRFRequest(
            instrument=instr,
            selector_string="",
            center_frequency=1.95e9,
            reference_level=0.000000,
            external_attenuation=0.000000,
        )
    )

    client.CfgDigitalEdgeTrigger(
        nirfmxwcdma_types.CfgDigitalEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            digital_edge_source_mapped=nirfmxwcdma_types.DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,
            digital_edge=nirfmxwcdma_types.DIGITAL_EDGE_TRIGGER_EDGE_RISING,
            trigger_delay=0.000000,
            enable_trigger=False,
        )
    )

    client.CfgUplinkScrambling(
        nirfmxwcdma_types.CfgUplinkScramblingRequest(
            instrument=instr,
            selector_string="",
            uplink_scrambling_code=0x0,
            uplink_scrambling_type=nirfmxwcdma_types.UPLINK_SCRAMBLING_TYPE_LONG,
        )
    )

    client.SelectMeasurements(
        nirfmxwcdma_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_array=[nirfmxwcdma_types.MEASUREMENT_TYPES_MODACC],
            enable_all_traces=True,
        )
    )

    client.ModAccCfgSynchronizationModeAndInterval(
        nirfmxwcdma_types.ModAccCfgSynchronizationModeAndIntervalRequest(
            instrument=instr,
            selector_string="",
            synchronization_mode=nirfmxwcdma_types.MODACC_SYNCHRONIZATION_MODE_SLOT,
            measurement_offset=0,
            measurement_length=1,
        )
    )

    client.Initiate(
        nirfmxwcdma_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )

    mod_acc_fetch_evm_response = client.ModAccFetchEVM(
        nirfmxwcdma_types.ModAccFetchEVMRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_evm_response, instr)

    rms_evm = mod_acc_fetch_evm_response.rms_evm
    peak_evm = mod_acc_fetch_evm_response.peak_evm
    rho = mod_acc_fetch_evm_response.rho
    frequency_error = mod_acc_fetch_evm_response.frequency_error
    chip_rate_error = mod_acc_fetch_evm_response.chip_rate_error
    rms_magnitude_error = mod_acc_fetch_evm_response.rms_magnitude_error
    rms_phase_error = mod_acc_fetch_evm_response.rms_phase_error

    mod_acc_fetch_iq_impairments_response = client.ModAccFetchIQImpairments(
        nirfmxwcdma_types.ModAccFetchIQImpairmentsRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_iq_impairments_response, instr)

    iq_origin_offset = mod_acc_fetch_iq_impairments_response.iq_origin_offset
    iq_gain_imbalance = mod_acc_fetch_iq_impairments_response.iq_gain_imbalance
    iq_quadrature_error = mod_acc_fetch_iq_impairments_response.iq_quadrature_error

    mod_acc_fetch_peak_cde_response = client.ModAccFetchPeakCDE(
        nirfmxwcdma_types.ModAccFetchPeakCDERequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_peak_cde_response, instr)

    peak_cde = mod_acc_fetch_peak_cde_response.peak_cde
    peak_cde_code = mod_acc_fetch_peak_cde_response.peak_cde_code
    peak_cde_branch = mod_acc_fetch_peak_cde_response.peak_cde_branch

    mod_acc_fetch_peak_active_cde_response = client.ModAccFetchPeakActiveCDE(
        nirfmxwcdma_types.ModAccFetchPeakActiveCDERequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_peak_active_cde_response, instr)

    peak_active_cde = mod_acc_fetch_peak_active_cde_response.peak_active_cde
    peak_active_cde_spreading_factor = (
        mod_acc_fetch_peak_active_cde_response.peak_active_cde_spreading_factor
    )
    peak_active_cde_code = mod_acc_fetch_peak_active_cde_response.peak_active_cde_code
    peak_active_cde_branch = mod_acc_fetch_peak_active_cde_response.peak_active_cde_branch

    mod_acc_fetch_rcde_response = client.ModAccFetchRCDE(
        nirfmxwcdma_types.ModAccFetchRCDERequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_rcde_response, instr)

    peak_rcde = mod_acc_fetch_rcde_response.peak_rcde
    peak_rcde_spreading_factor = mod_acc_fetch_rcde_response.peak_rcde_spreading_factor
    peak_rcde_code = mod_acc_fetch_rcde_response.peak_rcde_code
    peak_rcde_branch = mod_acc_fetch_rcde_response.peak_rcde_branch

    mod_acc_fetch_evm_trace_response = client.ModAccFetchEVMTrace(
        nirfmxwcdma_types.ModAccFetchEVMTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_evm_trace_response, instr)

    x0 = mod_acc_fetch_evm_trace_response.x0
    dx = mod_acc_fetch_evm_trace_response.dx
    evm = mod_acc_fetch_evm_trace_response.evm

    mod_acc_fetch_constellation_trace_response = client.ModAccFetchConstellationTrace(
        nirfmxwcdma_types.ModAccFetchConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.000000,
        )
    )
    check_for_warning(mod_acc_fetch_constellation_trace_response, instr)

    constellation = mod_acc_fetch_constellation_trace_response.constellation

    print("----------------------------EVM---------------------------")
    print(f"RMS EVM (%%)                            : {rms_evm}")
    print(f"Peak EVM (%%)                           : {peak_evm}")
    print(f"Rho                                     : {rho}")
    print(f"Frequency Error (Hz)                    : {frequency_error}")
    print(f"Chip Rate Error (ppm)                   : {chip_rate_error}")
    print(f"RMS Magnitude Error (%%)                : {rms_magnitude_error}")
    print(f"RMS Phase Error (deg)                   : {rms_phase_error}")

    print("\n----------------------IQ Impairments----------------------")
    print(f"I/Q Origin Offset (dB)                  : {iq_origin_offset}")
    print(f"I/Q Gain Imbalance (dB)                 : {iq_gain_imbalance}")
    print(f"I/Q Quadrature Error (deg)              : {iq_quadrature_error}")

    print("\n---------------------Code Domain Error--------------------")
    print(f"Peak CDE (dB)                           : {peak_cde}")
    print(f"Peak CDE Code                           : {peak_cde_code}")
    print(f"Peak CDE Branch                         : {'Q' if peak_cde_branch else 'I'}")
    print(f"Peak Active CDE (dB)                    : {peak_active_cde}")
    print(f"Peak Active CDE Code                    : {peak_active_cde_code}")
    print(f"Peak Active CDE Spreading Factor        : {peak_active_cde_spreading_factor}")
    print(f"Peak Active CDE Branch                  : {'Q' if peak_active_cde_branch else 'I'}")
    print(f"Peak RCDE (dB)                          : {peak_rcde}")
    print(f"Peak RCDE Code                          : {peak_rcde_code}")
    print(f"Peak RCDE Spreading Factor              : {peak_rcde_spreading_factor}")
    print(f"Peak RCDE Branch                        : {'Q' if peak_rcde_branch else 'I'}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwcdma_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc-evm-based-autolevel.py sha256=8615acf6b3711fc746a6b539e178b3b6e4e4417c77c042611d56ff6992b19d8d bytes=20097 -->
## FILE: examples/nirfmxwlan/ofdm-modacc-evm-based-autolevel.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwlan/ofdm-modacc-evm-based-autolevel.py`
- sha256: `8615acf6b3711fc746a6b539e178b3b6e4e4417c77c042611d56ff6992b19d8d`
- bytes: 20097

````python
r"""Fetch OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select OFDMModAcc measurement and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Frequency Error Estimation Method.
  9. Configure Amplitude Tracking Enabled.
  10. Configure Phase Tracking Enabled.
  11. Configure Symbol Clock Error Correction Enabled.
  12. Configure Channel Estimation Type.
  13. Configure Averaging parameters.
  14. Perform EVM-based Auto Level
  15. Initiate Measurement.
  16. Fetch OFDMModAcc Measurements.
  17. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc-evm-based_autoLevel.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxinstr_pb2 as nirfmxinstr_types
import nirfmxinstr_pb2_grpc as grpc_nirfmxinstr
import nirfmxwlan_pb2 as nirfmxwlan_types
import nirfmxwlan_pb2_grpc as grpc_nirfmxwlan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwlan.NiRFmxWLANStub(channel)
instr_client = grpc_nirfmxinstr.NiRFmxInstrStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwlan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = instr_client.Initialize(
        nirfmxinstr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    instr_client.CfgFrequencyReference(
        nirfmxinstr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxinstr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwlan_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.412e9,
        )
    )

    client.CfgReferenceLevel(
        nirfmxwlan_types.CfgReferenceLevelRequest(
            instrument=instr,
            selector_string="",
            reference_level=0.0,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwlan_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxwlan_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxwlan_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=5e-6,
            iq_power_edge_level_type=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )

    client.CfgStandard(
        nirfmxwlan_types.CfgStandardRequest(
            instrument=instr,
            selector_string="",
            standard=nirfmxwlan_types.STANDARD_802_11_AG,
        )
    )

    client.CfgChannelBandwidth(
        nirfmxwlan_types.CfgChannelBandwidthRequest(
            instrument=instr,
            selector_string="",
            channel_bandwidth=20e6,
        )
    )

    client.SelectMeasurements(
        nirfmxwlan_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxwlan_types.MEASUREMENT_TYPES_OFDMMODACC,
            enable_all_traces=True,
        )
    )

    client.OFDMModAccCfgMeasurementLength(
        nirfmxwlan_types.OFDMModAccCfgMeasurementLengthRequest(
            instrument=instr,
            selector_string="",
            measurement_offset=0,
            maximum_measurement_length=16,
        )
    )

    client.OFDMModAccCfgFrequencyErrorEstimationMethod(
        nirfmxwlan_types.OFDMModAccCfgFrequencyErrorEstimationMethodRequest(
            instrument=instr,
            selector_string="",
            frequency_error_estimation_method=nirfmxwlan_types.OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS,
        )
    )

    client.OFDMModAccCfgAmplitudeTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgAmplitudeTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            amplitude_tracking_enabled=nirfmxwlan_types.OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE,
        )
    )

    client.OFDMModAccCfgPhaseTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgPhaseTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            phase_tracking_enabled=nirfmxwlan_types.OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgSymbolClockErrorCorrectionEnabled(
        nirfmxwlan_types.OFDMModAccCfgSymbolClockErrorCorrectionEnabledRequest(
            instrument=instr,
            selector_string="",
            symbol_clock_error_correction_enabled=nirfmxwlan_types.OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgChannelEstimationType(
        nirfmxwlan_types.OFDMModAccCfgChannelEstimationTypeRequest(
            instrument=instr,
            selector_string="",
            channel_estimation_type=nirfmxwlan_types.OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE,
        )
    )

    client.OFDMModAccCfgAveraging(
        nirfmxwlan_types.OFDMModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.OFDMMODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    client.OFDMModAccAutoLevel(
        nirfmxwlan_types.OFDMModAccAutoLevelRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )

    initiate_response = client.Initiate(
        nirfmxwlan_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch Results ###

    fetch_composite_rmsevm_response = client.OFDMModAccFetchCompositeRMSEVM(
        nirfmxwlan_types.OFDMModAccFetchCompositeRMSEVMRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_composite_rmsevm_response, instr)
    composite_rmsevm_mean = fetch_composite_rmsevm_response.composite_rms_evm_mean
    composite_data_rmsevm_mean = fetch_composite_rmsevm_response.composite_data_rms_evm_mean
    composite_pilot_rmsevm_mean = fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean

    fetch_numberof_symbols_used_response = client.OFDMModAccFetchNumberofSymbolsUsed(
        nirfmxwlan_types.OFDMModAccFetchNumberofSymbolsUsedRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_numberof_symbols_used_response, instr)
    number_of_symbols_used = fetch_numberof_symbols_used_response.number_of_symbols_used

    fetch_frequency_error_mean_response = client.OFDMModAccFetchFrequencyErrorMean(
        nirfmxwlan_types.OFDMModAccFetchFrequencyErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_frequency_error_mean_response, instr)
    frequency_error_mean = fetch_frequency_error_mean_response.frequency_error_mean

    fetch_symbol_clock_error_mean_response = client.OFDMModAccFetchSymbolClockErrorMean(
        nirfmxwlan_types.OFDMModAccFetchSymbolClockErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_symbol_clock_error_mean_response, instr)
    symbol_clock_error_mean = fetch_symbol_clock_error_mean_response.symbol_clock_error_mean

    fetch_iq_impairments_response = client.OFDMModAccFetchIQImpairments(
        nirfmxwlan_types.OFDMModAccFetchIQImpairmentsRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_iq_impairments_response, instr)
    relative_iq_origin_offset_mean = fetch_iq_impairments_response.relative_iq_origin_offset_mean
    iq_gain_imbalance_mean = fetch_iq_impairments_response.iq_gain_imbalance_mean
    iq_quadrature_error_mean = fetch_iq_impairments_response.iq_quadrature_error_mean
    absolute_iq_origin_offset_mean = fetch_iq_impairments_response.absolute_iq_origin_offset_mean
    iq_timing_skew_mean = fetch_iq_impairments_response.iq_timing_skew_mean

    fetch_ppdu_type_response = client.OFDMModAccFetchPPDUType(
        nirfmxwlan_types.OFDMModAccFetchPPDUTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_ppdu_type_response, instr)
    ppdu_type = fetch_ppdu_type_response.ppdu_type

    fetch_mcs_index_response = client.OFDMModAccFetchMCSIndex(
        nirfmxwlan_types.OFDMModAccFetchMCSIndexRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_mcs_index_response, instr)
    mcs_index = fetch_mcs_index_response.mcs_index

    fetch_guard_interval_type_response = client.OFDMModAccFetchGuardIntervalType(
        nirfmxwlan_types.OFDMModAccFetchGuardIntervalTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_guard_interval_type_response, instr)
    guard_interval_type = fetch_guard_interval_type_response.guard_interval_type

    fetch_l_sig_parity_check_status_response = client.OFDMModAccFetchLSIGParityCheckStatus(
        nirfmxwlan_types.OFDMModAccFetchLSIGParityCheckStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_l_sig_parity_check_status_response, instr)
    l_sig_parity_check_status = fetch_l_sig_parity_check_status_response.l_sig_parity_check_status

    fetch_sigcrc_status_response = client.OFDMModAccFetchSIGCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigcrc_status_response, instr)
    sig_crc_status = fetch_sigcrc_status_response.sig_crc_status

    fetch_sigbcrc_status_response = client.OFDMModAccFetchSIGBCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGBCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigbcrc_status_response, instr)
    sig_b_crc_status = fetch_sigbcrc_status_response.sig_b_crc_status

    fetch_pilot_constellation_trace_response = client.OFDMModAccFetchPilotConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchPilotConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_pilot_constellation_trace_response, instr)
    pilot_constellation = fetch_pilot_constellation_trace_response.pilot_constellation

    fetch_data_constellation_trace_response = client.OFDMModAccFetchDataConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchDataConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_data_constellation_trace_response, instr)
    data_constellation = fetch_data_constellation_trace_response.data_constellation

    fetch_chain_rmsevm_per_subcarrier_mean_trace_response = (
        client.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace(
            nirfmxwlan_types.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
            )
        )
    )
    check_for_warning(fetch_chain_rmsevm_per_subcarrier_mean_trace_response, instr)
    x0 = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.x0
    dx = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.dx
    chain_rmsevm_per_subcarrier_mean = (
        fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean
    )

    print("------------------EVM------------------\n")
    print("------------------Composite EVM------------------")
    print(f"RMS EVM Mean (dB)                       : {composite_rmsevm_mean}")
    print(f"Data RMS EVM Mean (dB)                  : {composite_data_rmsevm_mean}")
    print(f"Pilot RMS EVM Mean (dB)                 : {composite_pilot_rmsevm_mean}\n")
    print(f"Number of Symbols Used                  : {number_of_symbols_used}\n")
    print("------------------Impairments & PPDU Info------------------\n")
    print(f"Frequency Error Mean (Hz)               : {frequency_error_mean}")
    print(f"Symbol Clock Error Mean (ppm)           : {symbol_clock_error_mean}\n")
    print("------------------IQ Impairments------------------")
    print(f"Relative I/Q Origin Offset Mean (dB)    : {relative_iq_origin_offset_mean}")
    print(f"Absolute I/Q Origin Offset Mean (dBm)   : {absolute_iq_origin_offset_mean}")
    print(f"I/Q Gain Imbalance Mean (dB)            : {iq_gain_imbalance_mean}")
    print(f"I/Q Quadrature Error Mean (deg)         : {iq_quadrature_error_mean}")
    print(f"I/Q Timing Skew Mean (s)                : {iq_timing_skew_mean}")
    print("\n------------------PPDU Info------------------")
    if ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_NON_HT:
        print("PPDU Type                               : Non-HT")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MIXED:
        print("PPDU Type                               : Mixed")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_GREENFIELD:
        print("PPDU Type                               : GreenField")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_SU:
        print("PPDU Type                               : SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MU:
        print("PPDU Type                               : MU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_EXTENDED_RANGE_SU:
        print("PPDU Type                               : Extended Range SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_TRIGGER_BASED:
        print("PPDU Type                               : Trigger-Based")
    print(f"MCS Index                               : {mcs_index}")
    if guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_4:
        print("Guard Interval Type                     : 1/4")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_8:
        print("Guard Interval Type                     : 1/8")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_16:
        print("Guard Interval Type                     : 1/16")
    if (
        l_sig_parity_check_status
        == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE
    ):
        print("L-SIG Parity Check Status               : Not Applicable")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL:
        print("L-SIG Parity Check Status               : Fail")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS:
        print("L-SIG Parity Check Status               : Pass")
    if sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE:
        print("SIG CRC Status                          : Not Applicable")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_FAIL:
        print("SIG CRC Status                          : Fail")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_PASS:
        print("SIG CRC Status                          : Pass")
    if sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE:
        print("SIG-B CRC Status                        : Not Applicable")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_FAIL:
        print("SIG-B CRC Status                        : Fail")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_PASS:
        print("SIG-B CRC Status                        : Pass")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwlan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc-txp-composite.py sha256=494c1674e1f2eb71aecfb60d629b0e58151e5036528906997213219d4dd0f6d9 bytes=21558 -->
## FILE: examples/nirfmxwlan/ofdm-modacc-txp-composite.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwlan/ofdm-modacc-txp-composite.py`
- sha256: `494c1674e1f2eb71aecfb60d629b0e58151e5036528906997213219d4dd0f6d9`
- bytes: 21558

````python
r"""Fetch TXP and OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select TXP and OFDMModAcc measurements and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Averaging.
  9. Configure Frequency Error Estimation Method.
  10. Configure Amplitude Tracking Enabled.
  11. Configure Phase Tracking Enabled.
  12. Configure Symbol Clock Error Correction Enabled.
  13. Configure Channel Estimation Type.
  14. Configure Averaging parameters.
  15. Initiate Measurement.
  16. Fetch TXP and OFDMModAcc Measurements.
  17. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc-txp-composite.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxinstr_pb2 as nirfmxinstr_types
import nirfmxinstr_pb2_grpc as grpc_nirfmxinstr
import nirfmxwlan_pb2 as nirfmxwlan_types
import nirfmxwlan_pb2_grpc as grpc_nirfmxwlan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwlan.NiRFmxWLANStub(channel)
instr_client = grpc_nirfmxinstr.NiRFmxInstrStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwlan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = instr_client.Initialize(
        nirfmxinstr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    instr_client.CfgFrequencyReference(
        nirfmxinstr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxinstr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwlan_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.412e9,
        )
    )

    client.CfgReferenceLevel(
        nirfmxwlan_types.CfgReferenceLevelRequest(
            instrument=instr,
            selector_string="",
            reference_level=0.0,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwlan_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxwlan_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxwlan_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=5e-6,
            iq_power_edge_level_type=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )

    client.CfgStandard(
        nirfmxwlan_types.CfgStandardRequest(
            instrument=instr,
            selector_string="",
            standard=nirfmxwlan_types.STANDARD_802_11_AG,
        )
    )

    client.CfgChannelBandwidth(
        nirfmxwlan_types.CfgChannelBandwidthRequest(
            instrument=instr,
            selector_string="",
            channel_bandwidth=20e6,
        )
    )

    client.SelectMeasurements(
        nirfmxwlan_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements_raw=nirfmxwlan_types.MEASUREMENT_TYPES_OFDMMODACC
            | nirfmxwlan_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    client.TXPCfgMaximumMeasurementInterval(
        nirfmxwlan_types.TXPCfgMaximumMeasurementIntervalRequest(
            instrument=instr,
            selector_string="",
            maximum_measurement_interval=1e-3,
        )
    )

    client.TXPCfgAveraging(
        nirfmxwlan_types.TXPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.TXP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    client.OFDMModAccCfgMeasurementLength(
        nirfmxwlan_types.OFDMModAccCfgMeasurementLengthRequest(
            instrument=instr,
            selector_string="",
            measurement_offset=0,
            maximum_measurement_length=16,
        )
    )

    client.OFDMModAccCfgFrequencyErrorEstimationMethod(
        nirfmxwlan_types.OFDMModAccCfgFrequencyErrorEstimationMethodRequest(
            instrument=instr,
            selector_string="",
            frequency_error_estimation_method=nirfmxwlan_types.OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS,
        )
    )

    client.OFDMModAccCfgAmplitudeTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgAmplitudeTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            amplitude_tracking_enabled=nirfmxwlan_types.OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE,
        )
    )

    client.OFDMModAccCfgPhaseTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgPhaseTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            phase_tracking_enabled=nirfmxwlan_types.OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgSymbolClockErrorCorrectionEnabled(
        nirfmxwlan_types.OFDMModAccCfgSymbolClockErrorCorrectionEnabledRequest(
            instrument=instr,
            selector_string="",
            symbol_clock_error_correction_enabled=nirfmxwlan_types.OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgChannelEstimationType(
        nirfmxwlan_types.OFDMModAccCfgChannelEstimationTypeRequest(
            instrument=instr,
            selector_string="",
            channel_estimation_type=nirfmxwlan_types.OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE,
        )
    )

    client.OFDMModAccCfgAveraging(
        nirfmxwlan_types.OFDMModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.OFDMMODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxwlan_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch Results ###

    txp_fetch_power_trace_response = client.TXPFetchPowerTrace(
        nirfmxwlan_types.TXPFetchPowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_power_trace_response, instr)
    x0 = txp_fetch_power_trace_response.x0
    dx = txp_fetch_power_trace_response.dx
    power = txp_fetch_power_trace_response.power
    txp_fetch_measurement_response = client.TXPFetchMeasurement(
        nirfmxwlan_types.TXPFetchMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_measurement_response, instr)
    average_power_mean = txp_fetch_measurement_response.average_power_mean
    peak_power_maximum = txp_fetch_measurement_response.peak_power_maximum
    fetch_composite_rmsevm_response = client.OFDMModAccFetchCompositeRMSEVM(
        nirfmxwlan_types.OFDMModAccFetchCompositeRMSEVMRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_composite_rmsevm_response, instr)
    composite_rmsevm_mean = fetch_composite_rmsevm_response.composite_rms_evm_mean
    composite_data_rmsevm_mean = fetch_composite_rmsevm_response.composite_data_rms_evm_mean
    composite_pilot_rmsevm_mean = fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean

    fetch_numberof_symbols_used_response = client.OFDMModAccFetchNumberofSymbolsUsed(
        nirfmxwlan_types.OFDMModAccFetchNumberofSymbolsUsedRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_numberof_symbols_used_response, instr)
    number_of_symbols_used = fetch_numberof_symbols_used_response.number_of_symbols_used

    fetch_frequency_error_mean_response = client.OFDMModAccFetchFrequencyErrorMean(
        nirfmxwlan_types.OFDMModAccFetchFrequencyErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_frequency_error_mean_response, instr)
    frequency_error_mean = fetch_frequency_error_mean_response.frequency_error_mean

    fetch_symbol_clock_error_mean_response = client.OFDMModAccFetchSymbolClockErrorMean(
        nirfmxwlan_types.OFDMModAccFetchSymbolClockErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_symbol_clock_error_mean_response, instr)
    symbol_clock_error_mean = fetch_symbol_clock_error_mean_response.symbol_clock_error_mean

    fetch_iq_impairments_response = client.OFDMModAccFetchIQImpairments(
        nirfmxwlan_types.OFDMModAccFetchIQImpairmentsRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_iq_impairments_response, instr)
    relative_iq_origin_offset_mean = fetch_iq_impairments_response.relative_iq_origin_offset_mean
    iq_gain_imbalance_mean = fetch_iq_impairments_response.iq_gain_imbalance_mean
    iq_quadrature_error_mean = fetch_iq_impairments_response.iq_quadrature_error_mean
    absolute_iq_origin_offset_mean = fetch_iq_impairments_response.absolute_iq_origin_offset_mean
    iq_timing_skew_mean = fetch_iq_impairments_response.iq_timing_skew_mean

    fetch_ppdu_type_response = client.OFDMModAccFetchPPDUType(
        nirfmxwlan_types.OFDMModAccFetchPPDUTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_ppdu_type_response, instr)
    ppdu_type = fetch_ppdu_type_response.ppdu_type

    fetch_mcs_index_response = client.OFDMModAccFetchMCSIndex(
        nirfmxwlan_types.OFDMModAccFetchMCSIndexRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_mcs_index_response, instr)
    mcs_index = fetch_mcs_index_response.mcs_index

    fetch_guard_interval_type_response = client.OFDMModAccFetchGuardIntervalType(
        nirfmxwlan_types.OFDMModAccFetchGuardIntervalTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_guard_interval_type_response, instr)
    guard_interval_type = fetch_guard_interval_type_response.guard_interval_type

    fetch_l_sig_parity_check_status_response = client.OFDMModAccFetchLSIGParityCheckStatus(
        nirfmxwlan_types.OFDMModAccFetchLSIGParityCheckStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_l_sig_parity_check_status_response, instr)
    l_sig_parity_check_status = fetch_l_sig_parity_check_status_response.l_sig_parity_check_status

    fetch_sigcrc_status_response = client.OFDMModAccFetchSIGCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigcrc_status_response, instr)
    sig_crc_status = fetch_sigcrc_status_response.sig_crc_status

    fetch_sigbcrc_status_response = client.OFDMModAccFetchSIGBCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGBCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigbcrc_status_response, instr)
    sig_b_crc_status = fetch_sigbcrc_status_response.sig_b_crc_status

    fetch_pilot_constellation_trace_response = client.OFDMModAccFetchPilotConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchPilotConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_pilot_constellation_trace_response, instr)
    pilot_constellation = fetch_pilot_constellation_trace_response.pilot_constellation

    fetch_data_constellation_trace_response = client.OFDMModAccFetchDataConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchDataConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_data_constellation_trace_response, instr)
    data_constellation = fetch_data_constellation_trace_response.data_constellation

    fetch_chain_rmsevm_per_subcarrier_mean_trace_response = (
        client.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace(
            nirfmxwlan_types.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
            )
        )
    )
    check_for_warning(fetch_chain_rmsevm_per_subcarrier_mean_trace_response, instr)
    x0 = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.x0
    dx = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.dx
    chain_rmsevm_per_subcarrier_mean = (
        fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean
    )

    print("------------------TXP------------------\n")
    print(f"Average Power Mean (dBm)          : {average_power_mean}")
    print(f"Peak Power Maximum (dBm)          : {peak_power_maximum}\n")
    print("------------------EVM------------------\n")
    print("------------------Composite EVM------------------")
    print(f"RMS EVM Mean (dB)                       : {composite_rmsevm_mean}")
    print(f"Data RMS EVM Mean (dB)                  : {composite_data_rmsevm_mean}")
    print(f"Pilot RMS EVM Mean (dB)                 : {composite_pilot_rmsevm_mean}\n")
    print(f"Number of Symbols Used                  : {number_of_symbols_used}\n")
    print("------------------Impairments & PPDU Info------------------\n")
    print(f"Frequency Error Mean (Hz)               : {frequency_error_mean}")
    print(f"Symbol Clock Error Mean (ppm)           : {symbol_clock_error_mean}\n")
    print("------------------IQ Impairments------------------")
    print(f"Relative I/Q Origin Offset Mean (dB)    : {relative_iq_origin_offset_mean}")
    print(f"Absolute I/Q Origin Offset Mean (dBm)   : {absolute_iq_origin_offset_mean}")
    print(f"I/Q Gain Imbalance Mean (dB)            : {iq_gain_imbalance_mean}")
    print(f"I/Q Quadrature Error Mean (deg)         : {iq_quadrature_error_mean}")
    print(f"I/Q Timing Skew Mean (s)                : {iq_timing_skew_mean}")
    print("\n------------------PPDU Info------------------")
    if ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_NON_HT:
        print("PPDU Type                               : Non-HT")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MIXED:
        print("PPDU Type                               : Mixed")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_GREENFIELD:
        print("PPDU Type                               : GreenField")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_SU:
        print("PPDU Type                               : SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MU:
        print("PPDU Type                               : MU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_EXTENDED_RANGE_SU:
        print("PPDU Type                               : Extended Range SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_TRIGGER_BASED:
        print("PPDU Type                               : Trigger-Based")
    print(f"MCS Index                               : {mcs_index}")
    if guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_4:
        print("Guard Interval Type                     : 1/4")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_8:
        print("Guard Interval Type                     : 1/8")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_16:
        print("Guard Interval Type                     : 1/16")
    if (
        l_sig_parity_check_status
        == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE
    ):
        print("L-SIG Parity Check Status               : Not Applicable")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL:
        print("L-SIG Parity Check Status               : Fail")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS:
        print("L-SIG Parity Check Status               : Pass")
    if sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE:
        print("SIG CRC Status                          : Not Applicable")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_FAIL:
        print("SIG CRC Status                          : Fail")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_PASS:
        print("SIG CRC Status                          : Pass")
    if sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE:
        print("SIG-B CRC Status                        : Not Applicable")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_FAIL:
        print("SIG-B CRC Status                        : Fail")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_PASS:
        print("SIG-B CRC Status                        : Pass")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwlan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc.py sha256=04eba611ca361a88b445076905ac55fbd7efc2fd320c0a80e324662af9e87784 bytes=19843 -->
## FILE: examples/nirfmxwlan/ofdm-modacc.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwlan/ofdm-modacc.py`
- sha256: `04eba611ca361a88b445076905ac55fbd7efc2fd320c0a80e324662af9e87784`
- bytes: 19843

````python
r"""Fetch OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select OFDMModAcc measurement and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Frequency Error Estimation Method.
  9. Configure Amplitude Tracking Enabled.
  10. Configure Phase Tracking Enabled.
  11. Configure Symbol Clock Error Correction Enabled.
  12. Configure Channel Estimation Type.
  13. Configure Averaging parameters.
  14. Initiate Measurement.
  15. Fetch OFDMModAcc Measurements.
  16. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxinstr_pb2 as nirfmxinstr_types
import nirfmxinstr_pb2_grpc as grpc_nirfmxinstr
import nirfmxwlan_pb2 as nirfmxwlan_types
import nirfmxwlan_pb2_grpc as grpc_nirfmxwlan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwlan.NiRFmxWLANStub(channel)
instr_client = grpc_nirfmxinstr.NiRFmxInstrStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwlan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    initialize_response = instr_client.Initialize(
        nirfmxinstr_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument

    instr_client.CfgFrequencyReference(
        nirfmxinstr_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxinstr_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwlan_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.412e9,
        )
    )

    client.CfgReferenceLevel(
        nirfmxwlan_types.CfgReferenceLevelRequest(
            instrument=instr,
            selector_string="",
            reference_level=0.0,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwlan_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxwlan_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxwlan_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=5e-6,
            iq_power_edge_level_type=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )

    client.CfgStandard(
        nirfmxwlan_types.CfgStandardRequest(
            instrument=instr,
            selector_string="",
            standard=nirfmxwlan_types.STANDARD_802_11_AG,
        )
    )

    client.CfgChannelBandwidth(
        nirfmxwlan_types.CfgChannelBandwidthRequest(
            instrument=instr,
            selector_string="",
            channel_bandwidth=20e6,
        )
    )

    client.SelectMeasurements(
        nirfmxwlan_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxwlan_types.MEASUREMENT_TYPES_OFDMMODACC,
            enable_all_traces=True,
        )
    )

    client.OFDMModAccCfgMeasurementLength(
        nirfmxwlan_types.OFDMModAccCfgMeasurementLengthRequest(
            instrument=instr,
            selector_string="",
            measurement_offset=0,
            maximum_measurement_length=16,
        )
    )

    client.OFDMModAccCfgFrequencyErrorEstimationMethod(
        nirfmxwlan_types.OFDMModAccCfgFrequencyErrorEstimationMethodRequest(
            instrument=instr,
            selector_string="",
            frequency_error_estimation_method=nirfmxwlan_types.OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS,
        )
    )

    client.OFDMModAccCfgAmplitudeTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgAmplitudeTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            amplitude_tracking_enabled=nirfmxwlan_types.OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE,
        )
    )

    client.OFDMModAccCfgPhaseTrackingEnabled(
        nirfmxwlan_types.OFDMModAccCfgPhaseTrackingEnabledRequest(
            instrument=instr,
            selector_string="",
            phase_tracking_enabled=nirfmxwlan_types.OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgSymbolClockErrorCorrectionEnabled(
        nirfmxwlan_types.OFDMModAccCfgSymbolClockErrorCorrectionEnabledRequest(
            instrument=instr,
            selector_string="",
            symbol_clock_error_correction_enabled=nirfmxwlan_types.OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE,
        )
    )

    client.OFDMModAccCfgChannelEstimationType(
        nirfmxwlan_types.OFDMModAccCfgChannelEstimationTypeRequest(
            instrument=instr,
            selector_string="",
            channel_estimation_type=nirfmxwlan_types.OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE,
        )
    )

    client.OFDMModAccCfgAveraging(
        nirfmxwlan_types.OFDMModAccCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.OFDMMODACC_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxwlan_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch Results ###

    fetch_composite_rmsevm_response = client.OFDMModAccFetchCompositeRMSEVM(
        nirfmxwlan_types.OFDMModAccFetchCompositeRMSEVMRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_composite_rmsevm_response, instr)
    composite_rmsevm_mean = fetch_composite_rmsevm_response.composite_rms_evm_mean
    composite_data_rmsevm_mean = fetch_composite_rmsevm_response.composite_data_rms_evm_mean
    composite_pilot_rmsevm_mean = fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean

    fetch_numberof_symbols_used_response = client.OFDMModAccFetchNumberofSymbolsUsed(
        nirfmxwlan_types.OFDMModAccFetchNumberofSymbolsUsedRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_numberof_symbols_used_response, instr)
    number_of_symbols_used = fetch_numberof_symbols_used_response.number_of_symbols_used

    fetch_frequency_error_mean_response = client.OFDMModAccFetchFrequencyErrorMean(
        nirfmxwlan_types.OFDMModAccFetchFrequencyErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_frequency_error_mean_response, instr)
    frequency_error_mean = fetch_frequency_error_mean_response.frequency_error_mean

    fetch_symbol_clock_error_mean_response = client.OFDMModAccFetchSymbolClockErrorMean(
        nirfmxwlan_types.OFDMModAccFetchSymbolClockErrorMeanRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_symbol_clock_error_mean_response, instr)
    symbol_clock_error_mean = fetch_symbol_clock_error_mean_response.symbol_clock_error_mean

    fetch_iq_impairments_response = client.OFDMModAccFetchIQImpairments(
        nirfmxwlan_types.OFDMModAccFetchIQImpairmentsRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_iq_impairments_response, instr)
    relative_iq_origin_offset_mean = fetch_iq_impairments_response.relative_iq_origin_offset_mean
    iq_gain_imbalance_mean = fetch_iq_impairments_response.iq_gain_imbalance_mean
    iq_quadrature_error_mean = fetch_iq_impairments_response.iq_quadrature_error_mean
    absolute_iq_origin_offset_mean = fetch_iq_impairments_response.absolute_iq_origin_offset_mean
    iq_timing_skew_mean = fetch_iq_impairments_response.iq_timing_skew_mean

    fetch_ppdu_type_response = client.OFDMModAccFetchPPDUType(
        nirfmxwlan_types.OFDMModAccFetchPPDUTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_ppdu_type_response, instr)
    ppdu_type = fetch_ppdu_type_response.ppdu_type

    fetch_mcs_index_response = client.OFDMModAccFetchMCSIndex(
        nirfmxwlan_types.OFDMModAccFetchMCSIndexRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_mcs_index_response, instr)
    mcs_index = fetch_mcs_index_response.mcs_index

    fetch_guard_interval_type_response = client.OFDMModAccFetchGuardIntervalType(
        nirfmxwlan_types.OFDMModAccFetchGuardIntervalTypeRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_guard_interval_type_response, instr)
    guard_interval_type = fetch_guard_interval_type_response.guard_interval_type

    fetch_l_sig_parity_check_status_response = client.OFDMModAccFetchLSIGParityCheckStatus(
        nirfmxwlan_types.OFDMModAccFetchLSIGParityCheckStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_l_sig_parity_check_status_response, instr)
    l_sig_parity_check_status = fetch_l_sig_parity_check_status_response.l_sig_parity_check_status

    fetch_sigcrc_status_response = client.OFDMModAccFetchSIGCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigcrc_status_response, instr)
    sig_crc_status = fetch_sigcrc_status_response.sig_crc_status

    fetch_sigbcrc_status_response = client.OFDMModAccFetchSIGBCRCStatus(
        nirfmxwlan_types.OFDMModAccFetchSIGBCRCStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_sigbcrc_status_response, instr)
    sig_b_crc_status = fetch_sigbcrc_status_response.sig_b_crc_status

    fetch_pilot_constellation_trace_response = client.OFDMModAccFetchPilotConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchPilotConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_pilot_constellation_trace_response, instr)
    pilot_constellation = fetch_pilot_constellation_trace_response.pilot_constellation

    fetch_data_constellation_trace_response = client.OFDMModAccFetchDataConstellationTrace(
        nirfmxwlan_types.OFDMModAccFetchDataConstellationTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(fetch_data_constellation_trace_response, instr)
    data_constellation = fetch_data_constellation_trace_response.data_constellation

    fetch_chain_rmsevm_per_subcarrier_mean_trace_response = (
        client.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace(
            nirfmxwlan_types.OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTraceRequest(
                instrument=instr,
                selector_string="",
                timeout=10.0,
            )
        )
    )
    check_for_warning(fetch_chain_rmsevm_per_subcarrier_mean_trace_response, instr)
    x0 = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.x0
    dx = fetch_chain_rmsevm_per_subcarrier_mean_trace_response.dx
    chain_rmsevm_per_subcarrier_mean = (
        fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean
    )

    print("------------------EVM------------------\n")
    print("------------------Composite EVM------------------")
    print(f"RMS EVM Mean (dB)                       : {composite_rmsevm_mean}")
    print(f"Data RMS EVM Mean (dB)                  : {composite_data_rmsevm_mean}")
    print(f"Pilot RMS EVM Mean (dB)                 : {composite_pilot_rmsevm_mean}\n")
    print(f"Number of Symbols Used                  : {number_of_symbols_used}\n")
    print("------------------Impairments & PPDU Info------------------\n")
    print(f"Frequency Error Mean (Hz)               : {frequency_error_mean}")
    print(f"Symbol Clock Error Mean (ppm)           : {symbol_clock_error_mean}\n")
    print("------------------IQ Impairments------------------")
    print(f"Relative I/Q Origin Offset Mean (dB)    : {relative_iq_origin_offset_mean}")
    print(f"Absolute I/Q Origin Offset Mean (dBm)   : {absolute_iq_origin_offset_mean}")
    print(f"I/Q Gain Imbalance Mean (dB)            : {iq_gain_imbalance_mean}")
    print(f"I/Q Quadrature Error Mean (deg)         : {iq_quadrature_error_mean}")
    print(f"I/Q Timing Skew Mean (s)                : {iq_timing_skew_mean}")
    print("\n------------------PPDU Info------------------")
    if ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_NON_HT:
        print("PPDU Type                               : Non-HT")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MIXED:
        print("PPDU Type                               : Mixed")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_GREENFIELD:
        print("PPDU Type                               : GreenField")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_SU:
        print("PPDU Type                               : SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_MU:
        print("PPDU Type                               : MU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_EXTENDED_RANGE_SU:
        print("PPDU Type                               : Extended Range SU")
    elif ppdu_type == nirfmxwlan_types.OFDM_PPDU_TYPE_TRIGGER_BASED:
        print("PPDU Type                               : Trigger-Based")
    print(f"MCS Index                               : {mcs_index}")
    if guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_4:
        print("Guard Interval Type                     : 1/4")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_8:
        print("Guard Interval Type                     : 1/8")
    elif guard_interval_type == nirfmxwlan_types.OFDM_GUARD_INTERVAL_TYPE_1_16:
        print("Guard Interval Type                     : 1/16")
    if (
        l_sig_parity_check_status
        == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE
    ):
        print("L-SIG Parity Check Status               : Not Applicable")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL:
        print("L-SIG Parity Check Status               : Fail")
    elif l_sig_parity_check_status == nirfmxwlan_types.OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS:
        print("L-SIG Parity Check Status               : Pass")
    if sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE:
        print("SIG CRC Status                          : Not Applicable")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_FAIL:
        print("SIG CRC Status                          : Fail")
    elif sig_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_CRC_STATUS_PASS:
        print("SIG CRC Status                          : Pass")
    if sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE:
        print("SIG-B CRC Status                        : Not Applicable")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_FAIL:
        print("SIG-B CRC Status                        : Fail")
    elif sig_b_crc_status == nirfmxwlan_types.OFDMMODACC_SIG_B_CRC_STATUS_PASS:
        print("SIG-B CRC Status                        : Pass")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwlan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwlan/sem.py sha256=295b27e944c14feae82afb7f1dedcb48ebadb60b472531f17244672ba964bc88 bytes=13287 -->
## FILE: examples/nirfmxwlan/sem.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwlan/sem.py`
- sha256: `295b27e944c14feae82afb7f1dedcb48ebadb60b472531f17244672ba964bc88`
- bytes: 13287

````python
r"""Fetch SEM data.

Steps:
  1. Open a new RFmx session.
  2. Configure the frequency reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties (Center Frequency and External Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Configure Reference Level.
  7. Select SEM measurement and enable the traces.
  8. Configure Averaging parameters.
  9. Configure Mask Type.
  10. Configure Sweep Time.
  11. Configure Span.
  12. Initiate the Measurement.
  13. Fetch SEM Measurements.
  14. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python sem
  .py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxwlan_pb2 as nirfmxwlan_types
import nirfmxwlan_pb2_grpc as grpc_nirfmxwlan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwlan.NiRFmxWLANStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwlan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxwlan_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxwlan_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxwlan_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwlan_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=6.412e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwlan_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxwlan_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxwlan_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=5.0e-6,
            iq_power_edge_level_type=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )

    client.CfgStandard(
        nirfmxwlan_types.CfgStandardRequest(
            instrument=instr,
            selector_string="",
            standard=nirfmxwlan_types.STANDARD_802_11_AG,
        )
    )

    client.CfgChannelBandwidth(
        nirfmxwlan_types.CfgChannelBandwidthRequest(
            instrument=instr,
            selector_string="",
            channel_bandwidth=20e6,
        )
    )

    if auto_level:
        client.AutoLevel(
            nirfmxwlan_types.AutoLevelRequest(
                instrument=instr,
                selector_string="",
                measurement_interval=10e-3,
            )
        )

    else:
        client.CfgReferenceLevel(
            nirfmxwlan_types.CfgReferenceLevelRequest(
                instrument=instr,
                selector_string="",
                reference_level=0.0,
            )
        )

    client.SelectMeasurements(
        nirfmxwlan_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxwlan_types.MEASUREMENT_TYPES_SEM,
            enable_all_traces=True,
        )
    )

    client.SEMCfgAveraging(
        nirfmxwlan_types.SEMCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.SEM_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
            averaging_type=nirfmxwlan_types.SEM_AVERAGING_TYPE_RMS,
        )
    )

    client.SEMCfgMaskType(
        nirfmxwlan_types.SEMCfgMaskTypeRequest(
            instrument=instr,
            selector_string="",
            mask_type=nirfmxwlan_types.SEM_MASK_TYPE_STANDARD,
        )
    )

    client.SEMCfgSweepTime(
        nirfmxwlan_types.SEMCfgSweepTimeRequest(
            instrument=instr,
            selector_string="",
            sweep_time_auto=nirfmxwlan_types.SEM_SWEEP_TIME_AUTO_TRUE,
            sweep_time_interval=1.0e-3,
        )
    )

    client.SEMCfgSpan(
        nirfmxwlan_types.SEMCfgSpanRequest(
            instrument=instr,
            selector_string="",
            span_auto=nirfmxwlan_types.SEM_SPAN_AUTO_TRUE,
            span=66.0e6,
        )
    )

    initiate_response = client.Initiate(
        nirfmxwlan_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch results ###

    sem_fetch_measurement_status_response = client.SEMFetchMeasurementStatus(
        nirfmxwlan_types.SEMFetchMeasurementStatusRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(sem_fetch_measurement_status_response, instr)
    measurement_status = sem_fetch_measurement_status_response.measurement_status

    sem_fetch_carrier_measurement_response = client.SEMFetchCarrierMeasurement(
        nirfmxwlan_types.SEMFetchCarrierMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(sem_fetch_carrier_measurement_response, instr)
    absolute_power = sem_fetch_carrier_measurement_response.absolute_power
    relative_power = sem_fetch_carrier_measurement_response.relative_power

    sem_fetch_lower_offset_margin_array_response = client.SEMFetchLowerOffsetMarginArray(
        nirfmxwlan_types.SEMFetchLowerOffsetMarginArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(sem_fetch_lower_offset_margin_array_response, instr)
    lower_offset_array_size = len(
        sem_fetch_lower_offset_margin_array_response.margin_absolute_power
    )
    lower_offset_measurement_status = (
        sem_fetch_lower_offset_margin_array_response.measurement_status
    )
    lower_offset_margin = sem_fetch_lower_offset_margin_array_response.margin
    lower_offset_margin_frequency = sem_fetch_lower_offset_margin_array_response.margin_frequency
    lower_offset_margin_absolute_power = (
        sem_fetch_lower_offset_margin_array_response.margin_absolute_power
    )
    lower_offset_margin_relative_power = (
        sem_fetch_lower_offset_margin_array_response.margin_relative_power
    )

    sem_fetch_upper_offset_margin_array_response = client.SEMFetchUpperOffsetMarginArray(
        nirfmxwlan_types.SEMFetchUpperOffsetMarginArrayRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(sem_fetch_upper_offset_margin_array_response, instr)
    upper_offset_array_size = len(
        sem_fetch_upper_offset_margin_array_response.margin_absolute_power
    )
    upper_offset_measurement_status = (
        sem_fetch_upper_offset_margin_array_response.measurement_status
    )
    upper_offset_margin = sem_fetch_upper_offset_margin_array_response.margin
    upper_offset_margin_frequency = sem_fetch_upper_offset_margin_array_response.margin_frequency
    upper_offset_margin_absolute_power = (
        sem_fetch_upper_offset_margin_array_response.margin_absolute_power
    )
    upper_offset_margin_relative_power = (
        sem_fetch_upper_offset_margin_array_response.margin_relative_power
    )

    sem_fetch_spectrum_response = client.SEMFetchSpectrum(
        nirfmxwlan_types.SEMFetchSpectrumRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(sem_fetch_spectrum_response, instr)

    print("\n----------SEM Results----------\n")
    if measurement_status == nirfmxwlan_types.SEM_MEASUREMENT_STATUS_PASS:
        print("Measurement Status               : PASS")
    elif measurement_status == nirfmxwlan_types.SEM_MEASUREMENT_STATUS_FAIL:
        print("Measurement Status               : FAIL")
    print(f"Carrier Absolute Power (dBm)     : {absolute_power}")
    print("\n-----------Lower Offset Measurements----------- \n")
    for i in range(lower_offset_array_size):
        print(f"Offset  {i}")
        if (
            lower_offset_measurement_status[i]
            == nirfmxwlan_types.SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS
        ):
            print("Measurement Status               : PASS")
        elif (
            lower_offset_measurement_status[i]
            == nirfmxwlan_types.SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL
        ):
            print("Measurement Status               : FAIL")
        print(f"Margin (dB)                      : {lower_offset_margin[i]}")
        print(f"Margin Frequency (Hz)            : {lower_offset_margin_frequency[i]}")
        print(f"Margin Absolute Power (dBm)      : {lower_offset_margin_absolute_power[i]}")
    print("\n-----------Upper Offset Measurements----------- \n")
    for i in range(upper_offset_array_size):
        print(f"Offset  {i}")
        if (
            upper_offset_measurement_status[i]
            == nirfmxwlan_types.SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS
        ):
            print("Measurement Status               : PASS")
        elif (
            upper_offset_measurement_status[i]
            == nirfmxwlan_types.SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL
        ):
            print("Measurement Status               : FAIL")
        print(f"Margin (dB)                      : {upper_offset_margin[i]}")
        print(f"Margin Frequency (Hz)            : {upper_offset_margin_frequency[i]}")
        print(f"Margin Absolute Power (dBm)      : {upper_offset_margin_absolute_power[i]}")

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwlan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfmxwlan/txp-basic.py sha256=f484ae3c1a16be7ee69e7bb92aee39ac93e5e0b662adc8da9f8210146c090d1a bytes=8528 -->
## FILE: examples/nirfmxwlan/txp-basic.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfmxwlan/txp-basic.py`
- sha256: `f484ae3c1a16be7ee69e7bb92aee39ac93e5e0b662adc8da9f8210146c090d1a`
- bytes: 8528

````python
r"""Fetch TXP data.

Steps:
  1. Open a new RFmx session.
  2. Configure the frequency reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties (Center Frequency and External Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Configure Reference Level.
  7. Select TXP measurement and enable the traces.
  8. Configure the Measurement Interval.
  9. Configure Averaging parameters.
  10. Initiate Measurement.
  11. Fetch TXP Traces and Measurements.
  12. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.
"""

import sys

import grpc
import nirfmxwlan_pb2 as nirfmxwlan_types
import nirfmxwlan_pb2_grpc as grpc_nirfmxwlan

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "RFmxWLANSession"

# Resource name and options for a simulated 5663 client.
RESOURCE = "SimulatedDevice"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfmxwlan.NiRFmxWLANStub(channel)
instr = None


def check_for_warning(response, instrument):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.GetErrorString(
            nirfmxwlan_types.GetErrorStringRequest(
                instrument=instrument,
                error_code=response.status,
            )
        )
        sys.stderr.write(
            f"{warning_message.error_description}\nWarning status: {response.status}\n"
        )


try:
    auto_level = True

    initialize_response = client.Initialize(
        nirfmxwlan_types.InitializeRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            option_string=OPTIONS,
        )
    )
    instr = initialize_response.instrument
    client.CfgFrequencyReference(
        nirfmxwlan_types.CfgFrequencyReferenceRequest(
            instrument=instr,
            channel_name="",
            frequency_reference_source_mapped=nirfmxwlan_types.FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK,
            frequency_reference_frequency=10e6,
        )
    )

    client.CfgFrequency(
        nirfmxwlan_types.CfgFrequencyRequest(
            instrument=instr,
            selector_string="",
            center_frequency=2.412e9,
        )
    )

    client.CfgExternalAttenuation(
        nirfmxwlan_types.CfgExternalAttenuationRequest(
            instrument=instr,
            selector_string="",
            external_attenuation=0.0,
        )
    )

    client.CfgIQPowerEdgeTrigger(
        nirfmxwlan_types.CfgIQPowerEdgeTriggerRequest(
            instrument=instr,
            selector_string="",
            iq_power_edge_source="0",
            iq_power_edge_slope=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_SLOPE_RISING,
            iq_power_edge_level=-20.0,
            trigger_delay=0.0,
            trigger_min_quiet_time_mode=nirfmxwlan_types.TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO,
            trigger_min_quiet_time_duration=5.0e-6,
            iq_power_edge_level_type=nirfmxwlan_types.IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE,
            enable_trigger=True,
        )
    )

    client.CfgStandard(
        nirfmxwlan_types.CfgStandardRequest(
            instrument=instr,
            selector_string="",
            standard=nirfmxwlan_types.STANDARD_802_11_AG,
        )
    )

    client.CfgChannelBandwidth(
        nirfmxwlan_types.CfgChannelBandwidthRequest(
            instrument=instr,
            selector_string="",
            channel_bandwidth=20e6,
        )
    )

    if auto_level:
        client.AutoLevel(
            nirfmxwlan_types.AutoLevelRequest(
                instrument=instr,
                selector_string="",
                measurement_interval=10e-3,
            )
        )

    else:
        client.CfgReferenceLevel(
            nirfmxwlan_types.CfgReferenceLevelRequest(
                instrument=instr,
                selector_string="",
                reference_level=0.0,
            )
        )

    client.SelectMeasurements(
        nirfmxwlan_types.SelectMeasurementsRequest(
            instrument=instr,
            selector_string="",
            measurements=nirfmxwlan_types.MEASUREMENT_TYPES_TXP,
            enable_all_traces=True,
        )
    )

    client.TXPCfgMaximumMeasurementInterval(
        nirfmxwlan_types.TXPCfgMaximumMeasurementIntervalRequest(
            instrument=instr,
            selector_string="",
            maximum_measurement_interval=1e-3,
        )
    )

    client.TXPCfgAveraging(
        nirfmxwlan_types.TXPCfgAveragingRequest(
            instrument=instr,
            selector_string="",
            averaging_enabled=nirfmxwlan_types.TXP_AVERAGING_ENABLED_FALSE,
            averaging_count=10,
        )
    )

    initiate_response = client.Initiate(
        nirfmxwlan_types.InitiateRequest(
            instrument=instr,
            selector_string="",
            result_name="",
        )
    )
    check_for_warning(initiate_response, instr)

    ### Fetch results ###

    txp_fetch_power_trace_response = client.TXPFetchPowerTrace(
        nirfmxwlan_types.TXPFetchPowerTraceRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_power_trace_response, instr)
    x0 = txp_fetch_power_trace_response.x0
    dx = txp_fetch_power_trace_response.dx
    power = txp_fetch_power_trace_response.power
    txp_fetch_measurement_response = client.TXPFetchMeasurement(
        nirfmxwlan_types.TXPFetchMeasurementRequest(
            instrument=instr,
            selector_string="",
            timeout=10.0,
        )
    )
    check_for_warning(txp_fetch_measurement_response, instr)
    average_power_mean = txp_fetch_measurement_response.average_power_mean
    peak_power_maximum = txp_fetch_measurement_response.peak_power_maximum

    print("\n----------Measurement----------\n")
    print(f"Average Power Mean (dBm)          : {average_power_mean}")
    print(f"Peak Power Maximum (dBm)          : {peak_power_maximum}")
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    sys.stderr.write(f"{error_message}\n")
finally:
    if instr:
        client.Close(nirfmxwlan_types.CloseRequest(instrument=instr, force_destroy=False))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsa/getting-started-iq.py sha256=029a53aadfc73eb66164f871362902dc096157ff9bb1d8d96bef9511ff848f85 bytes=5083 -->
## FILE: examples/nirfsa/getting-started-iq.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsa/getting-started-iq.py`
- sha256: `029a53aadfc73eb66164f871362902dc096157ff9bb1d8d96bef9511ff848f85`
- bytes: 5083

````python
r"""Configure I/Q parameters; read and print the I/Q data.

The following parameters of I/Q acquisition are configured:
 * reference clock, reference level, carrier frequency, I/Q rate, number of samples per record,
   and I/Q acquisition type.

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSA\documentation\English\nirfsa.chm

Getting Started:

To run this example, install "NI-RFSA Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSA gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-iq.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the physical channel name.
"""

import math
import sys

import grpc
import nirfsa_pb2 as nirfsa_types
import nirfsa_pb2_grpc as grpc_nirfsa

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSA-Session"

# Resource name, channel name and options for a simulated 5663 client.
RESOURCE = "SimulatedRFSA"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

NUMBER_OF_SAMPLES = 1000

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsa.NiRFSAStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsa_types.ErrorMessageRequest(vi=vi, status_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    init_response = client.InitWithOptions(
        nirfsa_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = init_response.vi

    client.ConfigureRefClock(
        nirfsa_types.ConfigureRefClockRequest(
            vi=vi,
            clock_source_mapped=nirfsa_types.RefClockSource.REF_CLOCK_SOURCE_ONBOARD_CLOCK,
            ref_clock_rate=10e6,
        )
    )
    client.ConfigureReferenceLevel(
        nirfsa_types.ConfigureReferenceLevelRequest(vi=vi, reference_level=0)
    )

    client.ConfigureAcquisitionType(
        nirfsa_types.ConfigureAcquisitionTypeRequest(
            vi=vi, acquisition_type=nirfsa_types.AcquisitionType.ACQUISITION_TYPE_IQ
        )
    )
    client.ConfigureIQCarrierFrequency(
        nirfsa_types.ConfigureIQCarrierFrequencyRequest(vi=vi, carrier_frequency=1e9)
    )
    client.ConfigureNumberOfSamples(
        nirfsa_types.ConfigureNumberOfSamplesRequest(
            vi=vi, number_of_samples_is_finite=True, samples_per_record=NUMBER_OF_SAMPLES
        )
    )
    read_response = client.ReadIQSingleRecordComplexF64(
        nirfsa_types.ReadIQSingleRecordComplexF64Request(
            vi=vi, timeout=10.0, data_array_size=NUMBER_OF_SAMPLES
        )
    )
    check_for_warning(read_response, vi)

    accumulator = 0.0
    for sample in read_response.data:
        magnitude_squared = sample.real**2 + sample.imaginary**2
        # We need to handle this because log(0) returns a range error.
        magnitude_squared = magnitude_squared or 1e-8
        accumulator += 10.0 * math.log10((magnitude_squared / (2.0 * 50.0)) * 1000.0)

    average_power = accumulator / NUMBER_OF_SAMPLES
    print(f"Average power = {average_power:.1f} dBm")


except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.Close(nirfsa_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsa/getting-started-spectrum.py sha256=9d96955a48c49cd56fb28667cd00475cfdf368b3cbbc29893a34d23038f444c0 bytes=5938 -->
## FILE: examples/nirfsa/getting-started-spectrum.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsa/getting-started-spectrum.py`
- sha256: `9d96955a48c49cd56fb28667cd00475cfdf368b3cbbc29893a34d23038f444c0`
- bytes: 5938

````python
r"""Configure a spectrum acquisition.

The following parameters of the spectrum acquisition are configured:
 * reference clock source, reference level, start and stop frequencies, resolution bandwidth, and
   the spectrum acquisition type.

If you configure the spectrum span (Stop Frequency - Start Frequency) to a value larger than the
instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into
one spectrum of the size you requested.

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSA\documentation\English\nirfsa.chm

Getting Started:

To run this example, install "NI-RFSA Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSA gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-spectrum.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the physical channel name.
"""

import math
import sys

import grpc
import nirfsa_pb2 as nirfsa_types
import nirfsa_pb2_grpc as grpc_nirfsa

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSA-Session"

# Resource name, channel name and options for a simulated 5663 client.
RESOURCE = "SimulatedRFSA"
OPTIONS = "Simulate=1,DriverSetup=Model:5663"

NUMBER_OF_SAMPLES = 1000

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsa.NiRFSAStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsa_types.ErrorMessageRequest(vi=vi, status_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    init_response = client.InitWithOptions(
        nirfsa_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = init_response.vi

    client.ConfigureRefClock(
        nirfsa_types.ConfigureRefClockRequest(
            vi=vi,
            clock_source_mapped=nirfsa_types.RefClockSource.REF_CLOCK_SOURCE_ONBOARD_CLOCK,
            ref_clock_rate=10e6,
        )
    )
    client.ConfigureReferenceLevel(
        nirfsa_types.ConfigureReferenceLevelRequest(vi=vi, reference_level=0)
    )
    client.ConfigureAcquisitionType(
        nirfsa_types.ConfigureAcquisitionTypeRequest(
            vi=vi, acquisition_type=nirfsa_types.AcquisitionType.ACQUISITION_TYPE_SPECTRUM
        )
    )
    client.ConfigureSpectrumFrequencyStartStop(
        nirfsa_types.ConfigureSpectrumFrequencyStartStopRequest(
            vi=vi, start_frequency=990e6, stop_frequency=1010e6
        )
    )
    client.ConfigureResolutionBandwidth(
        nirfsa_types.ConfigureResolutionBandwidthRequest(vi=vi, resolution_bandwidth=10e3)
    )
    spectral_lines_response = client.GetNumberOfSpectralLines(
        nirfsa_types.GetNumberOfSpectralLinesRequest(vi=vi)
    )
    read_response = client.ReadPowerSpectrumF64(
        nirfsa_types.ReadPowerSpectrumF64Request(
            vi=vi,
            timeout=10.0,
            data_array_size=spectral_lines_response.number_of_spectral_lines,
        )
    )
    check_for_warning(read_response, vi)

    # We will find the highest peak in a bin, which is not the actual highest
    # peak and frequency we could find in the acquisition.
    # For an accurate peak search, we can analyze the data with the Spectral Measurements Toolset.
    spectrum_data = read_response.power_spectrum_data
    spectrum_info = read_response.spectrum_info

    def _get_frequency_for_bin(bin):
        return spectrum_info.initial_frequency + spectrum_info.frequency_increment * bin

    greatest_peak_power = -math.inf
    for i, spectrum_data_point in enumerate(spectrum_data):
        if spectrum_data_point > greatest_peak_power:
            greatest_peak_power = spectrum_data_point
            greatest_peak_frequency = _get_frequency_for_bin(i)

    print(
        f"The highest peak in a bin is {greatest_peak_power:.1f} dBm at {greatest_peak_frequency/1e6:0.3f} MHz."
    )


except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.Close(nirfsa_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsg/attenuation-tables-generation.py sha256=b40aea45b9b292bbb2cb1f48e7b495ada9abe171f335f4a49d3a6804345d6a9f bytes=6153 -->
## FILE: examples/nirfsg/attenuation-tables-generation.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsg/attenuation-tables-generation.py`
- sha256: `b40aea45b9b292bbb2cb1f48e7b495ada9abe171f335f4a49d3a6804345d6a9f`
- bytes: 6153

````python
r"""Download S-parameters from an attenuation per frequency table.

The code shows how to convert attenuation into simple s-parameter table to be used with RFSG.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python attenuation-tables-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.
"""  # noqa: W505

import math
import sys

import grpc
import nidevice_pb2 as nidevice_grpc
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg
import numpy as np

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSG-Session"

# Resource name, channel name and options for a VST client.
RESOURCE = "5840_1"
OPTIONS = ""

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""
# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsg.NiRFSGStub(channel)
vi = None


def raise_if_error(response):
    """Raise an exception if an error was returned."""
    if response.status != 0:
        response = client.ErrorMessage(nirfsg_types.ErrorMessageRequest(error_code=response.status))
        raise Exception(f"Error: {response.error_string}")


def raise_if_initialization_error(response):
    """Raise an exception if an error was returned from Initialize."""
    if response.status < 0:
        raise RuntimeError(f"Error: {response.error_message or response.status}")
    if response.status > 0:
        sys.stderr.write(f"Warning: {response.error_message or response.status}\n")
    return response


try:
    response = client.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    raise_if_initialization_error(response)
    vi = response.vi

    client.ConfigureRefClock(
        nirfsg_types.ConfigureRefClockRequest(
            vi=vi,
            ref_clock_source_mapped=nirfsg_types.REF_CLOCK_SOURCE_ONBOARD_CLOCK,
            ref_clock_rate=10000000,
        )
    )

    client.SetAttributeViString(
        nirfsg_types.SetAttributeViStringRequest(
            vi=vi,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_REF_CLOCK_SOURCE,
            value_mapped=nirfsg_types.NIRFSG_STRING_REF_CLOCK_SOURCE_ONBOARD_CLOCK,
        )
    )

    raise_if_error(
        client.ConfigureRF(nirfsg_types.ConfigureRFRequest(vi=vi, frequency=1e9, power_level=-10))
    )

    # Having a table of attenuations per frequency, we demo how to convert them to S parameters
    # and download them to RFSG to be automatically set when we change the frequency
    frequency_table_hz = [1e9, 6e9]
    attenuation_table_db = [3, 3]

    # Convert to S parameters: Linear attenuation
    s = [math.pow(10, -x / 20) for x in attenuation_table_db]
    # We ned a table that it is frequencies x 2 x 2. Easier to fill it as a 3D matrix
    sparam = np.zeros(shape=(len(frequency_table_hz), 2, 2))
    for index in range(len(frequency_table_hz)):
        sparam[index, 0, 1] = s[index]  # S12
        sparam[index, 1, 0] = s[index]  # S21
    # Now flatten into a list
    sparam = sparam.reshape(np.prod(np.shape(sparam)))
    sparam = sparam.tolist()
    # Convert to NI datatype
    sparam_ni = [nidevice_grpc.NIComplexNumber(real=x, imaginary=0) for x in sparam]
    # Send them to the instrument
    client.CreateDeembeddingSparameterTableArray(
        nirfsg_types.CreateDeembeddingSparameterTableArrayRequest(
            vi=vi,
            port="",
            table_name="myTable",
            frequencies=frequency_table_hz,
            sparameter_table=sparam_ni,
            number_of_ports=2,
            sparameter_orientation=nirfsg_types.S_PARAMETER_ORIENTATION_PORT1_TOWARDS_DUT,
        )
    )

    raise_if_error(client.Initiate(nirfsg_types.InitiateRequest(vi=vi)))
    print("Generating tone...")
    # Wait for two seconds and change frequency
    input("Press any key to stop generation")
    raise_if_error(client.Abort(nirfsg_types.AbortRequest(vi=vi)))
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.ConfigureOutputEnabled(
            nirfsg_types.ConfigureOutputEnabledRequest(vi=vi, output_enabled=False)
        )
        client.Close(nirfsg_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsg/generate-from-tdms.py sha256=7b8b94812763c14010a99b9064bca0995de5e1f91f4f128d589d145807ef98fe bytes=5259 -->
## FILE: examples/nirfsg/generate-from-tdms.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsg/generate-from-tdms.py`
- sha256: `7b8b94812763c14010a99b9064bca0995de5e1f91f4f128d589d145807ef98fe`
- bytes: 5259

````python
r"""Generate a waveform from a TDMS file at a specified frequency and power.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.
"""

import sys

import grpc
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSG-Session"

# Resource name, channel name and options for a simulated 5652 client.
RESOURCE = "SimulatedRFSG"
OPTIONS = "Simulate=1,DriverSetup=Model:5652"

# Waveform filepath
FILE_PATH = "C:/Users/Public/Documents/National Instruments/NI-RFSG/Examples/Waveforms/FileWithSingleWaveform.tdms"
SCRIPT = (
    "script GenerateWfm "
    "repeat forever "
    "generate waveform marker0(0) "
    "end repeat "
    "end script"
)

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsg.NiRFSGStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsg_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


# Initialize RFSG
try:
    response = client.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = response.vi

    # Configure RFSG
    client.ConfigureRF(nirfsg_types.ConfigureRFRequest(vi=vi, frequency=3.5e9, power_level=-10))
    client.ConfigureRefClock(
        nirfsg_types.ConfigureRefClockRequest(
            vi=vi,
            ref_clock_source_mapped=nirfsg_types.REF_CLOCK_SOURCE_PXI_CLK,
            ref_clock_rate=10e6,
        )
    )

    client.ConfigurePowerLevelType(
        nirfsg_types.ConfigurePowerLevelTypeRequest(
            vi=vi, power_level_type=nirfsg_types.POWER_LEVEL_TYPE_PEAK_POWER
        )
    )

    client.ExportSignal(
        nirfsg_types.ExportSignalRequest(
            vi=vi,
            signal=nirfsg_types.ROUTED_SIGNAL_MARKER_EVENT,
            signal_identifier_mapped=nirfsg_types.SIGNAL_IDENTIFIER_MARKER0,
            output_terminal_mapped=nirfsg_types.OUTPUT_SIGNAL_PXI_TRIG0,
        )
    )

    client.ReadAndDownloadWaveformFromFileTDMS(
        nirfsg_types.ReadAndDownloadWaveformFromFileTDMSRequest(
            vi=vi, waveform_name="waveform", file_path=FILE_PATH, waveform_index=0
        )
    )

    client.ConfigureGenerationMode(
        nirfsg_types.ConfigureGenerationModeRequest(
            vi=vi, generation_mode=nirfsg_types.GENERATION_MODE_SCRIPT
        )
    )

    client.WriteScript(nirfsg_types.WriteScriptRequest(vi=vi, script=SCRIPT))

    initiate_response = client.Initiate(nirfsg_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_response, vi)
    print("Generating waveform... " "Press Enter to stop generation.")
    input()

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.ConfigureOutputEnabled(
            nirfsg_types.ConfigureOutputEnabledRequest(vi=vi, output_enabled=False)
        )
        client.Close(nirfsg_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsg/getting-started-single-tone-generation.py sha256=b36506c479d6638a69e7e13f791eb7f2946cb6634e241bf891e51a919d1d9f45 bytes=4193 -->
## FILE: examples/nirfsg/getting-started-single-tone-generation.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsg/getting-started-single-tone-generation.py`
- sha256: `b36506c479d6638a69e7e13f791eb7f2946cb6634e241bf891e51a919d1d9f45`
- bytes: 4193

````python
r"""Generate a single tone CW at a specified frequency and power.

The niRFSG_Abort function is used to quickly change from one configuration to another.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.
"""  # noqa: W505

import sys
import time

import grpc
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSG-Session"

# Resource name, channel name and options for a simulated 5652 client.
RESOURCE = "SimulatedRFSG"
OPTIONS = "Simulate=1,DriverSetup=Model:5652"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsg.NiRFSGStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsg_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    response = client.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = response.vi

    client.ConfigureRF(nirfsg_types.ConfigureRFRequest(vi=vi, frequency=1e9, power_level=-5))
    initiate_response = client.Initiate(nirfsg_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_response, vi)
    print("Generating tone...")
    # Wait for two seconds and change frequency
    time.sleep(2)
    print("Changing frequency")
    client.Abort(nirfsg_types.AbortRequest(vi=vi))
    client.ConfigureRF(nirfsg_types.ConfigureRFRequest(vi=vi, frequency=1.5e9, power_level=-5))
    initiate_response = client.Initiate(nirfsg_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_response, vi)

    print("Generating tone...")
    time.sleep(2)
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.ConfigureOutputEnabled(
            nirfsg_types.ConfigureOutputEnabledRequest(vi=vi, output_enabled=False)
        )
        client.Close(nirfsg_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsg/reference-clock.py sha256=cae7dbe8a85d40e0a41d50a8a34ad67283c388dbcbd89a498f960969ee033183 bytes=4188 -->
## FILE: examples/nirfsg/reference-clock.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsg/reference-clock.py`
- sha256: `cae7dbe8a85d40e0a41d50a8a34ad67283c388dbcbd89a498f960969ee033183`
- bytes: 4188

````python
r"""Route the reference clock source during a simple sine wave generation.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python reference-clock.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.
"""

import sys
import time

import grpc
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSG-Session"

# Resource name, channel name and options for a simulated 5652 client.
RESOURCE = "SimulatedRFSG"
OPTIONS = "Simulate=1,DriverSetup=Model:5652"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsg.NiRFSGStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsg_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    response = client.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = response.vi
    client.ConfigureRF(nirfsg_types.ConfigureRFRequest(vi=vi, frequency=1e9, power_level=-5))
    client.ConfigureGenerationMode(
        nirfsg_types.ConfigureGenerationModeRequest(
            vi=vi, generation_mode=nirfsg_types.GENERATION_MODE_CW
        )
    )
    client.ConfigureRefClock(
        nirfsg_types.ConfigureRefClockRequest(
            vi=vi,
            ref_clock_source_mapped=nirfsg_types.REF_CLOCK_SOURCE_ONBOARD_CLOCK,
            ref_clock_rate=10e6,
        )
    )
    print("Generating...")
    initiate_response = client.Initiate(nirfsg_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_response, vi)
    time.sleep(2)
    # Check the generation status
    client.CheckGenerationStatus(nirfsg_types.CheckGenerationStatusRequest(vi=vi))
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.ConfigureOutputEnabled(
            nirfsg_types.ConfigureOutputEnabledRequest(vi=vi, output_enabled=False)
        )
        client.Close(nirfsg_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nirfsg/rfsg-multitone-example.py sha256=e3a6dd395f6adc2a12cc538baf9700f164319d4d383a55c866d4bdd1b4245dd5 bytes=13209 -->
## FILE: examples/nirfsg/rfsg-multitone-example.py

- repository: `ni/grpc-device`
- source_path: `examples/nirfsg/rfsg-multitone-example.py`
- sha256: `e3a6dd395f6adc2a12cc538baf9700f164319d4d383a55c866d4bdd1b4245dd5`
- bytes: 13209

````python
r"""Generate any number and power of tones using RFSG.

At least one tone needs to be at 0 dB. Use Power level to set the power of all the tones relative to their selected power.
The minimum separation is mandated by a variable below. A smaller number needs more samples to meet the needs.
The maximum separation is mandated by the instrument used.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.
"""  # noqa: W505

import math
import sys

import grpc
import nidevice_pb2 as nidevice_grpc
import nirfsg_pb2 as nirfsg_types
import nirfsg_pb2_grpc as grpc_nirfsg
import numpy as np


SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
SESSION_NAME = "NI-RFSG-Session"

# Resource name, channel name and options for a simulated 5841 client.
RESOURCE = "5840_1"
OPTIONS = ""

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""
# Create a gRPC channel + client.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nirfsg.NiRFSGStub(channel)
vi = None


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.ErrorMessage(
            nirfsg_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


class Tone:
    """Class definition for tones.

    Define the tone with relative offset from the carrier frequency in Hz (relative to the
     generator center frequency).
    Relative power level in dBc (relative to the generator defined power level).
    """

    def __init__(self, offset_hz, gain_db):
        """Construct each tone using a relative offset in Hz and relative power in dBc."""
        self.offset_hz = offset_hz
        self.gain_db = gain_db

    def __repr__(self):
        """Make a string with Tones information."""
        return "Offset: {0} Hz and Gain: {1} dB".format(self.offset_hz, self.gain_db)


def gcd(my_list):
    """Return the greatest common denominator.

    Given a list of numbers find the smallest number that can divide them all.
    """
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


try:
    response = client.InitWithOptions(
        nirfsg_types.InitWithOptionsRequest(
            session_name=SESSION_NAME, resource_name=RESOURCE, option_string=OPTIONS
        )
    )
    vi = response.vi
    # tones to Generate
    # tones power is relative to the generated power.

    # Test Cases
    # tones = [Tone(0, 0)]
    tones = [Tone(-1e6, 0), Tone(1e6, 0)]
    # tones = [Tone(-1E6, 0), Tone(1E6, 0), Tone(-5E6, 0), Tone(5E6, 0), Tone(-10E6, 0)]
    # tones = [Tone(-1E6, 0), Tone(1E6, -5), Tone(2.5E6, -10), Tone(3.9E6, -20), Tone(-10E6, 0)]
    # tones = [Tone(100E3, 0), Tone(-835E3, -6)]
    # tones = [Tone(10E6, -3), Tone(-100.1E6, -6)]
    # tones = [Tone(1E6, 2.45), Tone(-50E6, -6)]
    # tones = [Tone(499E6, 0), Tone(-499E6, -6)]
    # tones = [Tone(1E6, 0), Tone(-50E6, -6)] + [Tone(499E6, 0), Tone(-499E6, -6)]
    # tones = [Tone(0, 0), Tone(-835E3, -6)]
    # tones = [Tone(2501200001-3e9, 0), Tone(3405200000-3e9, 0), Tone(3305300000-3e9, 0)]

    # Error Test Cases
    # tones = [Tone(0, -6)]
    # tones = [Tone(100E6, -10), Tone(-100E6, -10)]
    # tones = [Tone(1E9, 0), Tone(-100.1E6, -6)]
    # tones = [Tone(100E6, -20)]
    # tones = [Tone(1, 0), Tone(10E6, -6)]

    min_sampling_rate_hz = 4e6
    min_frequency_step_hz = 5000
    min_waveform_size = 100000
    print(tones)

    # Define the instrument and RF parameters
    print("Setting measurement parameters.. ", end="")
    center_frequency = 3e9
    rfsg_power_level_dbm = -10
    rfsg_resource_name = "5840_1"
    rfsg_selected_ports = ""
    rfsg_waveform_name = "wfm"
    rfsg_script = "script GenerateWaveform repeat forever generate wfm end repeat end script"
    rfsg_external_attenuation = 0.0
    rfsg_frequency_reference_source = nirfsg_types.REF_CLOCK_SOURCE_ONBOARD_CLOCK
    rfsg_automatic_shared_lo = nirfsg_types.NIRFSG_INT32_ENABLE_VALUES_DISABLE
    # Max rate 2.5x the max offset
    sampling_rate_hz = max([abs(tone.offset_hz) for tone in tones] + [min_sampling_rate_hz]) * 2.5
    # Greatest common denominator of the tones we need to make it divisible by Sampling Rate
    # thus we add it to the list it and then we divide it by a minimum resolution
    frequency_step_hz = max(
        gcd([abs(tone.offset_hz) for tone in tones] + [sampling_rate_hz]) / min_frequency_step_hz,
        sampling_rate_hz / min_waveform_size,
    )
    # Sum all the tones power for scaling on the SG power
    tones_power = 10 * math.log(sum([math.pow(10, tone.gain_db / 10) for tone in tones]), 10)
    print(
        "FrequencyStep = {} Hz and Sampling Frequency = {} Hz and Tone Total Power = {}".format(
            frequency_step_hz, sampling_rate_hz, tones_power
        )
    )

    client.SetAttributeViString(
        nirfsg_types.SetAttributeViStringRequest(
            vi=vi,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_SELECTED_PORTS,
            value_raw=rfsg_selected_ports,
        )
    )

    # We want the tones to be at a specific power, for that reason, we adjust
    # generator power to the desired power + whatever the tones constructive
    # interference. This was computed above as the "tones power"
    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_POWER_LEVEL,
            value_raw=rfsg_power_level_dbm + tones_power,
        )
    )

    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_EXTERNAL_GAIN,
            value_raw=-rfsg_external_attenuation,
        )
    )

    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_FREQUENCY,
            value_raw=center_frequency,
        )
    )

    # Coerce Settings
    for item in tones:
        item.offset_hz = np.floor(item.offset_hz / frequency_step_hz) * frequency_step_hz
        print(item)
    # Init initial waveform
    waveform = np.full(int(1 / frequency_step_hz * sampling_rate_hz), 0 + 0j)
    buffer = np.full(int(1 / frequency_step_hz * sampling_rate_hz), 1 + 0j)
    # Create tones on waveform
    for item in tones:
        phase_drif = item.offset_hz / sampling_rate_hz * 2 * np.pi
        offset_waveform = [1 * np.exp(i * phase_drif * 1j) for i in np.arange(0, len(waveform))]
        waveform = waveform + np.array(offset_waveform) * math.pow(10, item.gain_db / 20)
    # Waveform needs to normalize as we will use Peak Power Mode. This is easier to
    #  integrate with other pieces of code as it's the same mode.
    # This means that what we write magnitude (sqrt(I^2 + Q^2)) be larger than 1. 1 is
    #  the maximum and corresponds to the peak power setting.
    # If the power is set to -10 dBm, then a 1 means that the instantaneous power
    #  will be at -10 dBm.
    # To normalize, we divide all numbers by the peak to average ratio.
    # If the signal has gaps, then we should not use that section to compute power.

    waveform_papr = 10 * math.log(
        np.max(np.square(abs(waveform))) / np.mean(np.square(abs(waveform))), 10
    )
    waveform_normalized = waveform / math.pow(10, waveform_papr / 10)
    print(
        f"Previous max value is: {np.max(abs(waveform))} average value is: {np.mean(abs(waveform))} and new max value is: {np.max(abs(waveform_normalized))} and PAPR: {waveform_papr}"
    )
    # convert to NI complex datatype
    iq_ni_format = [
        nidevice_grpc.NIComplexNumberF32(real=sample.real, imaginary=sample.imag)
        for sample in waveform_normalized
    ]

    client.ConfigurePowerLevelType(
        nirfsg_types.ConfigurePowerLevelTypeRequest(
            vi=vi, power_level_type=nirfsg_types.POWER_LEVEL_TYPE_PEAK_POWER
        )
    )

    client.WriteArbWaveformComplexF32(
        nirfsg_types.WriteArbWaveformComplexF32Request(
            vi=vi, waveform_name="wfm", wfm_data=iq_ni_format, more_data_pending=False
        )
    )
    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="waveform::wfm",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_WAVEFORM_IQ_RATE,
            value_raw=sampling_rate_hz,
        )
    )

    # Example of how to set/get parameters of a waveform, the channel_name needs to have the
    #  prefix waveform:: before the name of the waveform
    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="waveform::wfm",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_WAVEFORM_PAPR,
            value_raw=waveform_papr,
        )
    )

    response_papr = client.GetAttributeViReal64(
        nirfsg_types.GetAttributeViReal64Request(
            vi=vi,
            channel_name="waveform::wfm",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_WAVEFORM_PAPR,
        )
    )
    waveform_papr = response_papr.value
    # The runtime scaling is to help reduce the chance of overflow the DAC by reducing
    #  the signal a bit more (1.5 dB). The driver compensates for this reduction and
    #  no need to compensate for this.
    runtime_scaling = 1.5
    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="waveform::wfm",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_WAVEFORM_RUNTIME_SCALING,
            value_raw=-runtime_scaling,
        )
    )
    client.SetAttributeViReal64(
        nirfsg_types.SetAttributeViReal64Request(
            vi=vi,
            channel_name="waveform::wfm",
            attribute_id=nirfsg_types.NIRFSG_ATTRIBUTE_WAVEFORM_SIGNAL_BANDWIDTH,
            value_raw=8e6,
        )
    )

    client.ConfigureGenerationMode(
        nirfsg_types.ConfigureGenerationModeRequest(
            vi=vi, generation_mode=nirfsg_types.GENERATION_MODE_SCRIPT
        )
    )

    client.WriteScript(nirfsg_types.WriteScriptRequest(vi=vi, script=rfsg_script))

    initiate_response = client.Initiate(nirfsg_types.InitiateRequest(vi=vi))
    check_for_warning(initiate_response, vi)
    print("Generating tone...")
    input("Press Any Key to Stop Generation")

    client.Abort(nirfsg_types.AbortRequest(vi=vi))
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
finally:
    if vi:
        client.ConfigureOutputEnabled(
            nirfsg_types.ConfigureOutputEnabledRequest(output_enabled=False)
        )
        client.Close(nirfsg_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niscope/fetch-continuous.py sha256=88b30c7e385b076feea66d7ef8e66d7ac67b7ae30023d09643a692bdf8b9a65d bytes=7013 -->
## FILE: examples/niscope/fetch-continuous.py

- repository: `ni/grpc-device`
- source_path: `examples/niscope/fetch-continuous.py`
- sha256: `88b30c7e385b076feea66d7ef8e66d7ac67b7ae30023d09643a692bdf8b9a65d`
- bytes: 7013

````python
r"""Initiate an acquisition and continuously fetches waveform samples per channel.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python fetch-continuous.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.
"""

import sys

import grpc
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_niscope
import numpy as np

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
RESOURCE = "SimulatedScope"
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe"

CHANNELS = "0,1"
TOTAL_ACQUISITION_TIME_IN_SECONDS = 10
SAMPLE_RATE_IN_HZ = 1000

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create a connection to the NI-SCOPE
# service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_niscope.NiScopeStub(channel)


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niscope_client.GetErrorMessage(
            niscope_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Open session to NI-SCOPE module with options.
    init_with_options_response = niscope_client.InitWithOptions(
        niscope_types.InitWithOptionsRequest(
            resource_name=RESOURCE,
            id_query=False,
            option_string=OPTIONS,
        )
    )
    vi = init_with_options_response.vi

    # Configure vertical.
    voltage = 10.0
    niscope_client.ConfigureVertical(
        niscope_types.ConfigureVerticalRequest(
            vi=vi,
            channel_list=CHANNELS,
            range=voltage,
            offset=0.0,
            coupling=niscope_types.VerticalCoupling.VERTICAL_COUPLING_NISCOPE_VAL_DC,
            probe_attenuation=1.0,
            enabled=True,
        )
    )

    # Configure horizontal timing.
    niscope_client.ConfigureHorizontalTiming(
        niscope_types.ConfigureHorizontalTimingRequest(
            vi=vi,
            min_sample_rate=SAMPLE_RATE_IN_HZ,
            min_num_pts=1,
            ref_position=0.0,
            num_records=1,
            enforce_realtime=True,
        )
    )

    # Configure software trigger, but never send the trigger.
    # This starts an infinite acquisition, until you call Abort or Close
    niscope_client.ConfigureTriggerSoftware(
        niscope_types.ConfigureTriggerSoftwareRequest(vi=vi, holdoff=0.0, delay=0.0)
    )

    # Initiate acquisition
    initiate_response = niscope_client.InitiateAcquisition(
        niscope_types.InitiateAcquisitionRequest(vi=vi)
    )
    check_for_warning(initiate_response, vi)

    # Allocate space for the waveform according to the max number of
    # points to fetch and the number of waveforms.
    channel_list = CHANNELS.split(",")
    total_samples = int(TOTAL_ACQUISITION_TIME_IN_SECONDS * SAMPLE_RATE_IN_HZ)
    waveforms = [np.ndarray(total_samples, dtype=np.float64) for c in channel_list]

    # Set fetch relative to attribute.
    niscope_client.SetAttributeViInt32(
        niscope_types.SetAttributeViInt32Request(
            vi=vi,
            channel_list="",
            attribute_id=niscope_types.NiScopeAttribute.NISCOPE_ATTRIBUTE_FETCH_RELATIVE_TO,
            value=niscope_types.NiScopeInt32AttributeValues.NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_READ_POINTER,
        )
    )

    # Fetch continuously until all samples are acquired.
    current_pos = 0
    samples_per_fetch = 100

    try:
        while current_pos < total_samples:
            # We fetch each channel at a time so we don't have to de-interleave afterwards.
            # We do not keep the wfm_info returned from fetch.
            for channel_name, waveform in zip(channel_list, waveforms):
                fetch_response = niscope_client.Fetch(
                    niscope_types.FetchRequest(
                        vi=vi,
                        channel_list=channel_name,
                        timeout=500000,
                        num_samples=samples_per_fetch,
                    )
                )
                check_for_warning(fetch_response, vi)
                waveform[current_pos : current_pos + samples_per_fetch] = fetch_response.waveform
                print(
                    f"Fetching channel {channel_name}'s waveform for indices {current_pos} to {current_pos + samples_per_fetch - 1}"
                )
            print()
            current_pos += samples_per_fetch

    except KeyboardInterrupt:
        pass

# If NI-SCOPE API throws an exception, print the error message.
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    if "vi" in vars() and vi.name != "":
        # close the session.
        niscope_client.Close(niscope_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niscope/fetch.py sha256=9f07bb078c14506382576f57cee5db21d699f0ee68f29dd447ade64615361060 bytes=5158 -->
## FILE: examples/niscope/fetch.py

- repository: `ni/grpc-device`
- source_path: `examples/niscope/fetch.py`
- sha256: `9f07bb078c14506382576f57cee5db21d699f0ee68f29dd447ade64615361060`
- bytes: 5158

````python
r"""Initiate an acquisition and fetch a waveform for each specified channel.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python fetch.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.
"""

import sys

import grpc
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_niscope

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
RESOURCE = "SimulatedScope"
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe"

CHANNELS = "0"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create a connection to the NI-SCOPE
# service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_niscope.NiScopeStub(channel)


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niscope_client.GetErrorMessage(
            niscope_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Open session to NI-SCOPE module with options.
    init_with_options_response = niscope_client.InitWithOptions(
        niscope_types.InitWithOptionsRequest(
            resource_name=RESOURCE,
            id_query=False,
            option_string=OPTIONS,
        )
    )
    vi = init_with_options_response.vi

    # Configure vertical.
    voltage = 10.0
    niscope_client.ConfigureVertical(
        niscope_types.ConfigureVerticalRequest(
            vi=vi,
            channel_list=CHANNELS,
            range=voltage,
            offset=0.0,
            coupling=niscope_types.VerticalCoupling.VERTICAL_COUPLING_NISCOPE_VAL_AC,
            probe_attenuation=1.0,
            enabled=True,
        )
    )

    # Configure horizontal timing.
    samples = 1000
    niscope_client.ConfigureHorizontalTiming(
        niscope_types.ConfigureHorizontalTimingRequest(
            vi=vi,
            min_sample_rate=50000000,
            min_num_pts=samples,
            ref_position=50.0,
            num_records=1,
            enforce_realtime=True,
        )
    )

    # Initiate acquisition.
    initiate_response = niscope_client.InitiateAcquisition(
        niscope_types.InitiateAcquisitionRequest(vi=vi)
    )
    check_for_warning(initiate_response, vi)

    # Fetch waveforms.
    fetch_response = niscope_client.Fetch(
        niscope_types.FetchRequest(vi=vi, channel_list=CHANNELS, timeout=10000, num_samples=samples)
    )
    check_for_warning(fetch_response, vi)
    waveforms = fetch_response.waveform

    # Print waveform results.
    for i in range(len(waveforms)):
        print(f"Waveform {i} information:")
        print(f"{waveforms[i]}\n")

# If NI-SCOPE API throws an exception, print the error message.
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    if "vi" in vars() and vi.name != "":
        # close the session.
        niscope_client.Close(niscope_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niscope/graph-measurement.py sha256=69ef4f307c0c413a88bc2bc40d8c47481cd2f19d4c4533934567c092c1fa7992 bytes=7371 -->
## FILE: examples/niscope/graph-measurement.py

- repository: `ni/grpc-device`
- source_path: `examples/niscope/graph-measurement.py`
- sha256: `69ef4f307c0c413a88bc2bc40d8c47481cd2f19d4c4533934567c092c1fa7992`
- bytes: 7371

````python
r"""Read waveforms from an NI-SCOPE device.

Tested with a 100 kHz tone input to channel 0.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python graph-measurement.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.
"""

import sys
import time

import grpc
import matplotlib.pyplot as plt
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_scope

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
RESOURCE = "SimulatedScope"
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe; MemorySize:1610612736"

CHANNELS = "0"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niscope_client.GetErrorMessage(
            niscope_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


# Create the communication channel for the remote host (in this case we are connecting to a local
# server) and create a connection to the NI-SCOPE service
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_scope.NiScopeStub(channel)

try:
    # Initialize the scope
    init_result = niscope_client.InitWithOptions(
        niscope_types.InitWithOptionsRequest(
            session_name="demo",
            resource_name=RESOURCE,
            id_query=False,
            option_string=OPTIONS,
        )
    )
    vi = init_result.vi

    # Configure Vertical
    vertical_result = niscope_client.ConfigureVertical(
        niscope_types.ConfigureVerticalRequest(
            vi=vi,
            channel_list=CHANNELS,
            range=10.0,
            offset=0,
            coupling=niscope_types.VerticalCoupling.VERTICAL_COUPLING_NISCOPE_VAL_DC,
            enabled=True,
            probe_attenuation=1,
        )
    )

    # Configure Horizontal Timing
    config_result = niscope_client.ConfigureHorizontalTiming(
        niscope_types.ConfigureHorizontalTimingRequest(
            vi=vi,
            min_sample_rate=1000000,
            min_num_pts=1000,
            ref_position=50,
            num_records=1,
            enforce_realtime=True,
        )
    )

    # Setup an Edge Trigger
    result = niscope_client.SetAttributeViInt32(
        niscope_types.SetAttributeViInt32Request(
            vi=vi,
            attribute_id=niscope_types.NiScopeAttribute.NISCOPE_ATTRIBUTE_TRIGGER_TYPE,
            value=niscope_types.NiScopeInt32AttributeValues.NISCOPE_INT32_TRIGGER_TYPE_VAL_EDGE_TRIGGER,
        )
    )

    conf_trigger_edge_result = niscope_client.ConfigureTriggerEdge(
        niscope_types.ConfigureTriggerEdgeRequest(
            vi=vi,
            trigger_source=CHANNELS,
            level=0.00,
            slope=niscope_types.TriggerSlope.TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE,
            trigger_coupling=niscope_types.TriggerCoupling.TRIGGER_COUPLING_NISCOPE_VAL_DC,
            holdoff=0.0,
        )
    )

    result = niscope_client.SetAttributeViInt32(
        niscope_types.SetAttributeViInt32Request(
            vi=vi,
            channel_list=CHANNELS,
            attribute_id=niscope_types.NiScopeAttribute.NISCOPE_ATTRIBUTE_MEAS_REF_LEVEL_UNITS,
            value=niscope_types.NiScopeInt32AttributeValues.NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_PERCENTAGE,
        )
    )

    # Setup a plot to draw the captured waveform
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()

    print("\nReading values in loop. CTRL+C to stop.\n")
    try:
        while True:
            # Clear the plot and setup the axis
            plt.clf()
            plt.axis([0, 100, -6, 6])
            # Read a waveform from the scope
            read_result = niscope_client.Read(
                niscope_types.ReadRequest(
                    vi=vi,
                    channel_list=CHANNELS,
                    timeout=1,
                    num_samples=10000,
                )
            )
            check_for_warning(read_result, vi)
            values = read_result.waveform[0:10]
            print(values)

            # Update the plot with the new waveform
            plt.plot(read_result.waveform[0:100])
            fig.canvas.draw()
            plt.pause(0.001)

            # Fetch the measured average frequency
            fetch_result = niscope_client.FetchMeasurementStats(
                niscope_types.FetchMeasurementStatsRequest(
                    vi=vi,
                    channel_list=CHANNELS,
                    timeout=1,
                    scalar_meas_function=niscope_types.ScalarMeasurement.SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY,
                )
            )
            check_for_warning(fetch_result, vi)
            print("Average Frequency: " + str("%.2f" % round(fetch_result.result[0], 2)) + " Hz")
            print("")

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    if "vi" in vars() and vi.name != "":
        # close the session.
        niscope_client.Close(niscope_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niscope/plot-read-waveform.py sha256=95d330a297553e25a68cff6b8e082200ae7406389c907b42f8f60af3e52bc5ea bytes=5591 -->
## FILE: examples/niscope/plot-read-waveform.py

- repository: `ni/grpc-device`
- source_path: `examples/niscope/plot-read-waveform.py`
- sha256: `95d330a297553e25a68cff6b8e082200ae7406389c907b42f8f60af3e52bc5ea`
- bytes: 5591

````python
r"""Continuously read and plot waveform data from an NI-SCOPE device.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python plot-read-waveform.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.
"""

import sys

import grpc
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_scope

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
RESOURCE = "SimulatedScope"
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe; MemorySize:1610612736"

CHANNELS = "0"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niscope_client.GetErrorMessage(
            niscope_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


# Create the communcation channel for the remote host (in this case we are connecting to a local
# server) and create a connection to the niScope service
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_scope.NiScopeStub(channel)

try:
    # Initialize the scope
    init_result = niscope_client.InitWithOptions(
        niscope_types.InitWithOptionsRequest(
            session_name="demo",
            resource_name=RESOURCE,
            id_query=False,
            option_string=OPTIONS,
        )
    )
    vi = init_result.vi

    # Configure horizontal timing
    config_result = niscope_client.ConfigureHorizontalTiming(
        niscope_types.ConfigureHorizontalTimingRequest(
            vi=vi,
            min_sample_rate=1000000,
            min_num_pts=100000,
            ref_position=50,
            num_records=1,
            enforce_realtime=True,
        )
    )

    # Configure vertical timing
    vertical_result = niscope_client.ConfigureVertical(
        niscope_types.ConfigureVerticalRequest(
            vi=vi,
            channel_list=CHANNELS,
            range=10.0,
            offset=0,
            coupling=niscope_types.VerticalCoupling.VERTICAL_COUPLING_NISCOPE_VAL_DC,
            enabled=True,
            probe_attenuation=1,
        )
    )

    conf_trigger_edge_result = niscope_client.ConfigureTriggerEdge(
        niscope_types.ConfigureTriggerEdgeRequest(
            vi=vi,
            trigger_source=CHANNELS,
            level=0.00,
            trigger_coupling=niscope_types.TriggerCoupling.TRIGGER_COUPLING_NISCOPE_VAL_DC,
            slope=niscope_types.TriggerSlope.TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE,
        )
    )

    result = niscope_client.SetAttributeViInt32(
        niscope_types.SetAttributeViInt32Request(
            vi=vi,
            channel_list=CHANNELS,
            attribute_id=niscope_types.NiScopeAttribute.NISCOPE_ATTRIBUTE_MEAS_REF_LEVEL_UNITS,
            value=niscope_types.NiScopeInt32AttributeValues.NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_VOLTAGE,
        )
    )

    # Read a waveform from the scope
    read_result = niscope_client.Read(
        niscope_types.ReadRequest(vi=vi, channel_list=CHANNELS, timeout=10000, num_samples=100000)
    )
    check_for_warning(read_result, vi)
    values = read_result.waveform[0:10]
    print(values)

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    if "vi" in vars() and vi.name != "":
        # close the session.
        niscope_client.Close(niscope_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niswitch/controlling-an-individual-relay.py sha256=8285f7f09ccc873b89960fcdd0f1f37386c9d0f6b1f162e54ba14266bb1b7153 bytes=4184 -->
## FILE: examples/niswitch/controlling-an-individual-relay.py

- repository: `ni/grpc-device`
- source_path: `examples/niswitch/controlling-an-individual-relay.py`
- sha256: `8285f7f09ccc873b89960fcdd0f1f37386c9d0f6b1f162e54ba14266bb1b7153`
- bytes: 4184

````python
r"""Control an individual relay on a module.

The gRPC API is built from the C API. NI-SWITCH documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niSwitch\Documentation\English\SWITCH.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/375472H-01/

Getting Started:

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SWITCH Help to determine topology, relay names, and resource names.

Refer to the NI-SWITCH gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-SWITCH-C-Function-Reference

Running from command line:

Server machine's IP address and port number can be passed as separate command line arguments.
  > python controlling-an-individual-relay.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".
To successfully run this example, the resource name, topology, and relay name must be hard coded
in this file.
"""

import sys

import grpc
import niswitch_pb2 as niswitch_types
import niswitch_pb2_grpc as grpc_niswitch

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name, topology string and relay name for a simulated 2529 module. Refer to NI-SWITCH help
# to find valid values for the device being used.
# If you are using real hardware device, use the appropriate resource name and set the SIMULATION
# variable to False.
RESOURCE = ""
TOPOLOGY_STRING = "2571/66-SPDT"
RELAY_NAME = "k15"
SIMULATION = True

# Set the maximimum time to wait for debounce.
MAX_DEBOUNCE_TIME = 1000
SESSION_NAME = "NI-Switch-Session-1"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]

# Create the communcation channel for the remote host and create a connection to the NI-SWITCH
# service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niswitch_client = grpc_niswitch.NiSwitchStub(channel)


try:
    # Open session to NI-SWITCH and set topology.
    init_with_topology_response = niswitch_client.InitWithTopology(
        niswitch_types.InitWithTopologyRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            topology=TOPOLOGY_STRING,
            simulate=SIMULATION,
            reset_device=False,
        )
    )
    vi = init_with_topology_response.vi
    print("Topology set to : ", TOPOLOGY_STRING)

    # Close the relay. Use values that are valid for the model being used.
    niswitch_client.RelayControl(
        niswitch_types.RelayControlRequest(
            vi=vi,
            relay_name=RELAY_NAME,
            relay_action=niswitch_types.RelayAction.RELAY_ACTION_NISWITCH_VAL_CLOSE_RELAY,
        )
    )
    print("Relay closed.")

    # Wait for debounce
    niswitch_client.WaitForDebounce(
        niswitch_types.WaitForDebounceRequest(vi=vi, maximum_time_ms=MAX_DEBOUNCE_TIME)
    )
    print("Wait for debounce to complete.")

# If NI-SWITCH API throws an exception, print the error message
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Close the session.
    if "vi" in vars() and vi.name != "":
        niswitch_client.Close(niswitch_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/niswitch/software-scanning.py sha256=c6c90f635271b8b23d0e09c9e47ec451f3395b30e82210140edcb94e491199cc bytes=5604 -->
## FILE: examples/niswitch/software-scanning.py

- repository: `ni/grpc-device`
- source_path: `examples/niswitch/software-scanning.py`
- sha256: `c6c90f635271b8b23d0e09c9e47ec451f3395b30e82210140edcb94e491199cc`
- bytes: 5604

````python
r"""Scan a series of channels on a module using software scanning.

The gRPC API is built from the C API. NI-SWITCH documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niSwitch\Documentation\English\SWITCH.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/375472H-01/

Getting Started:

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SWITCH Help to determine if your module supports scanning, the scan list syntax,
valid channel names and valid resource names.

Refer to the NI-SWITCH gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-SWITCH-C-Function-Reference

Running from command line:

Server machine's IP address and port numbercan be passed as separate command line arguments.
  > python software-scanning.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".
To successfully run this example, the resource name, topology, and scan list must be hard coded in
this file.
"""

import sys
import time

import grpc
import niswitch_pb2 as niswitch_types
import niswitch_pb2_grpc as grpc_niswitch

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name, topology string and scanlist for a simulated 2529 module. Refer to NI-SWITCH help
# to find valid values for the device being used.
# If you are using real hardware device, use the appropriate resource name and set the SIMULATION
# variable to False.
RESOURCE = ""
TOPOLOGY_STRING = "2529/2-Wire Dual 4x16 Matrix"
SCAN_LIST = "b0r1->b0c1;b0r1->b0c2;b0r2->b0c3"
SIMULATION = True

SESSION_NAME = "NI-Switch-Session-1"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]

# Create the communcation channel for the remote host and create a connection to the NI-SWITCH
# service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niswitch_client = grpc_niswitch.NiSwitchStub(channel)
number_of_triggers = 5


def check_for_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niswitch_client.ErrorMessage(
            niswitch_types.ErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


try:
    # Open session to NI-SWITCH and set topology.
    init_with_topology_response = niswitch_client.InitWithTopology(
        niswitch_types.InitWithTopologyRequest(
            session_name=SESSION_NAME,
            resource_name=RESOURCE,
            topology=TOPOLOGY_STRING,
            simulate=SIMULATION,
            reset_device=False,
        )
    )
    vi = init_with_topology_response.vi
    print("Topology set to : ", TOPOLOGY_STRING)

    # Configure the scan list.
    niswitch_client.ConfigureScanList(
        niswitch_types.ConfigureScanListRequest(
            vi=vi,
            scanlist=SCAN_LIST,
            scan_mode=niswitch_types.ScanMode.SCAN_MODE_NISWITCH_VAL_BREAK_BEFORE_MAKE,
        )
    )

    # Configures the trigger to be software trigger.
    niswitch_client.ConfigureScanTrigger(
        niswitch_types.ConfigureScanTriggerRequest(
            vi=vi,
            trigger_input=niswitch_types.TriggerInput.TRIGGER_INPUT_NISWITCH_VAL_SOFTWARE_TRIG,
            scan_advanced_output=niswitch_types.ScanAdvancedOutput.SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_NONE,
        )
    )
    print("Configured the trigger as Software Trigger")

    # Loop through scan list continuously
    niswitch_client.SetContinuousScan(
        niswitch_types.SetContinuousScanRequest(vi=vi, continuous_scan=True)
    )

    # Initiate scanning
    initiate_scan_response = niswitch_client.InitiateScan(niswitch_types.InitiateScanRequest(vi=vi))
    check_for_warning(initiate_scan_response, vi)
    print("Scanning initiated...")

    # Send software trigger to module in a loop
    for x in range(number_of_triggers):
        # Wait for 500 ms
        time.sleep(0.5)
        niswitch_client.SendSoftwareTrigger(niswitch_types.SendSoftwareTriggerRequest(vi=vi))
        number_of_triggers -= 1

    # Abort Scanning
    niswitch_client.AbortScan(niswitch_types.AbortScanRequest(vi=vi))
    print("Scanning completed.")

# If NI-SWITCH API throws an exception, print the error message
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Close the session.
    if "vi" in vars() and vi.name != "":
        niswitch_client.Close(niswitch_types.CloseRequest(vi=vi))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nitclk/multi-device-configured-acquisition-tclk.py sha256=c9645ffd493b67ea17146a101ed679f0e19a15ec4da5425993da6cbe6ceed668 bytes=11948 -->
## FILE: examples/nitclk/multi-device-configured-acquisition-tclk.py

- repository: `ni/grpc-device`
- source_path: `examples/nitclk/multi-device-configured-acquisition-tclk.py`
- sha256: `c9645ffd493b67ea17146a101ed679f0e19a15ec4da5425993da6cbe6ceed668`
- bytes: 11948

````python
r"""Read synchronized waveforms from multiple NI-SCOPE devices.

Tested with a 100 kHz tone input to channel 0.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Refer to the NI-TClk gRPC Wiki to determine the valid channel and resource names for your NI-TClk
module:
  https://github.com/ni/grpc-device/wiki/NI-TClk-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and multiple comma separated resource names can be
passed as separate command line arguments.
  > python multi-device-configured-acquisition-tclk.py <server_address> <port_number> <resource_name1,resource_name2>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope1" and "SimulatedScope2" as the resource names.
"""  # noqa: W505

import sys
import time

import grpc
import matplotlib.pyplot as plt
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_scope
import nitclk_pb2 as nitclk_types
import nitclk_pb2_grpc as grpc_tclk
import numpy as np

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe;"
RESOURCES = ["SimulatedScope1", "SimulatedScope2"]

# Parameters
CHANNELS = "0"
previous_max_input_frequency = -10.0
previous_min_sample_rate = -10
previous_min_record_length = -10
trigger_type = "-10"
max_input_frequency = 0.0
min_sample_rate = 1000000
num_records = 1

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCES = [r.strip() for r in sys.argv[3].split(",")]
    OPTIONS = ""

# Create the communication channel for the remote host (in this case we are connecting to a local
# server) and create a connection to the NI-SCOPE service and NI-TClk service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_scope.NiScopeStub(channel)
nitclk_client = grpc_tclk.NiTClkStub(channel)
sessions = []


def check_for_scope_warning(response, vi):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = niscope_client.GetErrorMessage(
            niscope_types.GetErrorMessageRequest(vi=vi, error_code=response.status)
        )
        sys.stderr.write(f"{warning_message.error_message}\nWarning status: {response.status}\n")


def check_for_tclk_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nitclk_client.GetExtendedErrorInfo(
            nitclk_types.GetExtendedErrorInfoRequest()
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    # Initialize the sessions
    for i, resource in enumerate(RESOURCES, start=1):
        init_result = niscope_client.InitWithOptions(
            niscope_types.InitWithOptionsRequest(
                session_name="session" + str(i),
                resource_name=resource,
                id_query=False,
                reset_device=False,
                option_string=OPTIONS,
            )
        )
        sessions.append(init_result.vi)

    for session in sessions:
        # Configure Acquisition Type
        niscope_client.ConfigureAcquisition(
            niscope_types.ConfigureAcquisitionRequest(
                vi=session, acquisition_type=0  # NISCOPE_VAL_NORMAL
            )
        )

        # Configure Vertical
        niscope_client.ConfigureVertical(
            niscope_types.ConfigureVerticalRequest(
                vi=session,
                channel_list=CHANNELS,
                range=10.0,
                offset=0.0,
                coupling=niscope_types.VerticalCoupling.VERTICAL_COUPLING_NISCOPE_VAL_DC,
                enabled=True,
                probe_attenuation=1.0,
            )
        )

        # Configure Channel Characteristics
        niscope_client.ConfigureChanCharacteristics(
            niscope_types.ConfigureChanCharacteristicsRequest(
                vi=session,
                channel_list=CHANNELS,
                input_impedance=1000000.0,
                max_input_frequency=0.0,
            )
        )

        # Configure Horizontal Timing
        niscope_client.ConfigureHorizontalTiming(
            niscope_types.ConfigureHorizontalTimingRequest(
                vi=session,
                min_sample_rate=100000000.0,
                min_num_pts=1000,
                ref_position=50,
                num_records=1,
                enforce_realtime=True,
            )
        )

    vi = sessions[0]
    # Get the trigger type from the user
    print("Type the trigger type\n")
    print("1 - Edge\n")
    print("2 - Hysteresis\n")
    print("3 - Digital\n")
    print("4 - Window\n")
    print("5 - Immediate\n")
    trigger_type = input("Option: ")

    # Assign the default values for the trigger attribute that depends on the trigger type
    if trigger_type == "1":
        niscope_client.ConfigureTriggerEdge(
            niscope_types.ConfigureTriggerEdgeRequest(
                vi=vi,
                trigger_source="0",
                level=0.0,
                slope=niscope_types.TriggerSlope.TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE,
                trigger_coupling=niscope_types.TriggerCoupling.TRIGGER_COUPLING_NISCOPE_VAL_DC,
                holdoff=0.0,
                delay=0.0,
            )
        )
    elif trigger_type == "2":
        niscope_client.ConfigureTriggerHysteresis(
            niscope_types.ConfigureTriggerHysteresisRequest(
                vi=vi,
                trigger_source="0",
                level=0.0,
                hysteresis=0.1,
                slope=niscope_types.TriggerSlope.TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE,
                trigger_coupling=niscope_types.TriggerCoupling.TRIGGER_COUPLING_NISCOPE_VAL_DC,
                holdoff=0.0,
                delay=0.0,
            )
        )
    elif trigger_type == "3":
        niscope_client.ConfigureTriggerDigital(
            niscope_types.ConfigureTriggerDigitalRequest(
                vi=vi,
                trigger_source="VAL_PFI_1",
                slope=niscope_types.TriggerSlope.TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE,
                holdoff=0.0,
                delay=0.0,
            )
        )
    elif trigger_type == "4":
        niscope_client.ConfigureTriggerWindow(
            niscope_types.ConfigureTriggerWindowRequest(
                vi=vi,
                trigger_source="0",
                low_level=-0.1,
                high_level=0.1,
                window_mode=niscope_types.TriggerWindowMode.TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_WINDOW,
                trigger_coupling=niscope_types.TriggerCoupling.TRIGGER_COUPLING_NISCOPE_VAL_DC,
                holdoff=0.0,
                delay=0.0,
            )
        )
    elif trigger_type == "5":
        niscope_client.ConfigureTriggerImmediate(
            niscope_types.ConfigureTriggerImmediateRequest(vi=vi)
        )
    else:
        raise Exception("Enter a Valid Input")

    if (
        previous_min_sample_rate != min_sample_rate
        or previous_max_input_frequency != max_input_frequency
        or previous_min_record_length != num_records
    ):
        # Use NI-TClk to configure appropriate parameters, synchronize digitizers, and initiate
        # operation.
        nitclk_client.ConfigureForHomogeneousTriggers(
            nitclk_types.ConfigureForHomogeneousTriggersRequest(sessions=sessions)
        )

        nitclk_client.Synchronize(
            nitclk_types.SynchronizeRequest(sessions=sessions, min_tclk_period=0.0)
        )
    previous_min_sample_rate = min_sample_rate
    previous_max_input_frequency = max_input_frequency
    previous_min_record_length = num_records

    initiate_result = nitclk_client.Initiate(nitclk_types.InitiateRequest(sessions=sessions))
    check_for_tclk_warning(initiate_result)

    # Setup a plot to draw the captured waveform
    fig = plt.figure("Waveform Graph")
    fig.show()
    fig.canvas.draw()

    # Handle closing of plot window.
    closed = False

    def _on_close(event):
        global closed
        closed = True

    fig.canvas.mpl_connect("close_event", _on_close)
    print("\nReading values in loop. CTRL+C to stop.\n")
    try:
        while not closed:
            # Clear the plot and setup the axis
            fig.clf()
            plt.axis([0, 500, -6, 6])
            # Fetch a waveform from the scope
            for i in range(len(sessions)):
                fetch_result = niscope_client.Fetch(
                    niscope_types.FetchRequest(
                        vi=sessions[i], channel_list=CHANNELS, timeout=1, num_samples=500
                    )
                )
                check_for_scope_warning(fetch_result, vi)
                plt.subplot(1, len(sessions), i + 1, label=str(i))
                # Round the array to 2 decimal places and Update the plot with the new waveform
                data = np.array(fetch_result.waveform[0:500])
                # Add labels for axes and legends
                plt.ylabel("Amplitude")
                plt.xlabel("Samples")
                plt.plot(np.round(data, 2))
                plt.title(label="$Scope{i}$".format(i=i))
            plt.subplots_adjust(wspace=0.5)
            plt.pause(0.001)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    for i in range(len(sessions)):
        sample_rate_result = niscope_client.SampleRate(niscope_types.SampleRateRequest(vi=session))
        record_length_result = niscope_client.ActualRecordLength(
            niscope_types.ActualRecordLengthRequest(vi=session)
        )
        print(RESOURCES[i])
        print("Actual Sample Rate = %f" % sample_rate_result.sample_rate)
        print("Actual Record Length = %f\n" % record_length_result.record_length)

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Close the NI-SCOPE sessions.
    for session in sessions:
        niscope_client.Close(niscope_types.CloseRequest(vi=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nitclk/synchronize-tclk.py sha256=1ac4050a3e01475bbff0895ef47ac0b2e379ac4c99b0c47a3770dcd772294b4c bytes=5726 -->
## FILE: examples/nitclk/synchronize-tclk.py

- repository: `ni/grpc-device`
- source_path: `examples/nitclk/synchronize-tclk.py`
- sha256: `1ac4050a3e01475bbff0895ef47ac0b2e379ac4c99b0c47a3770dcd772294b4c`
- bytes: 5726

````python
r"""Configure multiple NI Arbitrary Waveform Generators to generate synchronized waveforms.

The gRPC API is built from the C API. NI-FGEN documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niFgen\documentation\English\SigGenHelp.chm

NI-TClk documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niTClk\documentation\English\nitclk.chm

Getting Started:

To run this example, install "NI-FGEN Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and multiple comma separated resource names can be
passed as separate command line arguments.
  > python synchronize-tclk.py <server_address> <port_number> <resource_name1,resource_name2>
This example is not supported in simulation mode, hence these arguments are mandatory.
"""

import sys

import grpc
import matplotlib.pyplot as plt
import nifgen_pb2 as nifgen_types
import nifgen_pb2_grpc as grpc_nifgen
import nitclk_pb2 as nitclk_types
import nitclk_pb2_grpc as grpc_nitclk

# parameters
SAMPLE_RATE = 20000000.0
WAVEFORM_SIZE = 16
# Create waveform data
WAVEFORM_DATA = [0.0 if i < WAVEFORM_SIZE // 2 else 1.0 for i in range(WAVEFORM_SIZE)]

# Read in cmd args
if len(sys.argv) < 4:
    msg = "This example is not supported in simulation mode. "
    msg += "Please provide server address, server port and resource name as follows:\n"
    msg += "  python synchronize-tclk.py <server_address> <port_number> <resource_name1,resource_name2>\n"
    sys.stderr.write(msg)
    sys.exit(1)
else:
    SERVER_ADDRESS = sys.argv[1]
    SERVER_PORT = sys.argv[2]
    RESOURCES = [r.strip() for r in sys.argv[3].split(",")]

# Create the communication channel for the remote host and create connections to the NI-FGEN and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
nifgen_client = grpc_nifgen.NiFgenStub(channel)
nitclk_client = grpc_nitclk.NiTClkStub(channel)
sessions = []


def check_for_tclk_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = nitclk_client.GetExtendedErrorInfo(
            nitclk_types.GetExtendedErrorInfoRequest()
        )
        sys.stderr.write(f"{warning_message.error_string}\nWarning status: {response.status}\n")


try:
    for i, resource in enumerate(RESOURCES, start=1):
        # Initalize NI-FGEN session
        init_with_options_resp = nifgen_client.InitWithOptions(
            nifgen_types.InitWithOptionsRequest(
                session_name="session" + str(i), resource_name=resource, option_string=""
            )
        )
        vi = init_with_options_resp.vi
        sessions.append(vi)

        # Configure channels
        nifgen_client.ConfigureChannels(nifgen_types.ConfigureChannelsRequest(vi=vi, channels="0"))

        # Configure output mode
        nifgen_client.ConfigureOutputMode(
            nifgen_types.ConfigureOutputModeRequest(
                vi=vi, output_mode=nifgen_types.OutputMode.OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB
            )
        )

        # Configure sample rate
        nifgen_client.ConfigureSampleRate(
            nifgen_types.ConfigureSampleRateRequest(vi=vi, sample_rate=SAMPLE_RATE)
        )

        # Create waveform
        nifgen_client.CreateWaveformF64(
            nifgen_types.CreateWaveformF64Request(
                vi=vi, channel_name="0", waveform_data_array=WAVEFORM_DATA
            )
        )

    nitclk_client.ConfigureForHomogeneousTriggers(
        nitclk_types.ConfigureForHomogeneousTriggersRequest(sessions=sessions)
    )

    # Synchronize and start generation
    nitclk_client.Synchronize(nitclk_types.SynchronizeRequest(sessions=sessions, min_tclk_period=0))
    initiate_response = nitclk_client.Initiate(nitclk_types.InitiateRequest(sessions=sessions))
    check_for_tclk_warning(initiate_response)

    print(f"Generating square wave with sample rate {SAMPLE_RATE} on {RESOURCES}...")
    print("Close the graph or press Ctrl+C to stop generation")

    try:
        # Plot waveform
        fig = plt.gcf()
        fig.canvas.manager.set_window_title("Sample Waveform")
        plt.plot(WAVEFORM_DATA)
        plt.suptitle("Close the window to stop generation", fontsize=10)
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.show()
    except KeyboardInterrupt:
        pass

# If NI-FGEN API throws an exception, print the error message.
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(error_message)

finally:
    # Close the NI-FGEN sessions.
    for session in sessions:
        nifgen_client.Close(nifgen_types.CloseRequest(vi=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nixnet/can-signal-single-point-output.py sha256=69f7808f0807d9b55e7e8aad9f4b5902f92a1772c8f32b18e02c5b196fb6751f bytes=4770 -->
## FILE: examples/nixnet/can-signal-single-point-output.py

- repository: `ni/grpc-device`
- source_path: `examples/nixnet/can-signal-single-point-output.py`
- sha256: `69f7808f0807d9b55e7e8aad9f4b5902f92a1772c8f32b18e02c5b196fb6751f`
- bytes: 4770

````python
r"""Write Signal Data.

 This example writes a signal value for 10 times.
 This is used to demonstrate a signal single point output session.
 This example uses hardcoded signal names that use the NIXNET_example database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the transceivers are externally powered when using C Series modules.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm
Getting Started:

To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python can-signal-single-point-output.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"
"""

import sys

import grpc
import nixnet_pb2 as nixnet_types
import nixnet_pb2_grpc as grpc_nixnet

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
INTERFACE = "CAN1"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    INTERFACE = sys.argv[3]

# Parameters
DATABASE = "NIXNET_example"
CLUSTER = "CAN_Cluster"
SIGNAL_LIST = "CANEventSignal1,CANEventSignal2"
NUM_SIGNALS = 2


i = 0
value_buffer = [0.0] * NUM_SIGNALS
session = None

# Create the communication channel for the remote host and create connections to the NI-XNET and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nixnet.NiXnetStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.StatusToString(
            nixnet_types.StatusToStringRequest(status_id=response.status)
        )
        sys.stderr.write(
            f"{warning_message.status_description}\nWarning status: {response.status}\n"
        )


# Display parameters that will be used for the example.
print("Interface: " + INTERFACE, "Database: " + DATABASE, "Signal List: " + SIGNAL_LIST, sep="\n")

try:
    # Create an XNET session in SignalOutSinglePoint mode
    create_session_response = client.CreateSession(
        nixnet_types.CreateSessionRequest(
            database_name=DATABASE,
            cluster_name=CLUSTER,
            list=SIGNAL_LIST,
            interface_name=INTERFACE,
            mode=nixnet_types.CREATE_SESSION_MODE_SIGNAL_OUT_SINGLE_POINT,
        )
    )
    session = create_session_response.session
    print("Session Created Successfully.\n")

    print("Writing 10 values to CAN Interface.\n")

    while i < 10:
        value_buffer[0] = float(i)
        value_buffer[1] = float(i * 10)

        # Update the signal data
        write_signal_response = client.WriteSignalSinglePoint(
            nixnet_types.WriteSignalSinglePointRequest(session=session, value_buffer=value_buffer)
        )
        check_for_warning(write_signal_response)

        print("Signals sent:")
        print(f"Signal 1: {value_buffer[0]}")
        print(f"Signal 2: {value_buffer[1]}", end="\n\n")
        i = i + 1

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Clear the XNET session.
    if session:
        client.Clear(nixnet_types.ClearRequest(session=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nixnet/ethernet-frame-stream-input-reader.py sha256=78634f9d4250fce3fdd73fec7f5344e28d9f3cbdd45840b31492c60d8ccb6033 bytes=6935 -->
## FILE: examples/nixnet/ethernet-frame-stream-input-reader.py

- repository: `ni/grpc-device`
- source_path: `examples/nixnet/ethernet-frame-stream-input-reader.py`
- sha256: `78634f9d4250fce3fdd73fec7f5344e28d9f3cbdd45840b31492c60d8ccb6033`
- bytes: 6935

````python
r"""Reads all the frame on network.

  This example reads all the frames on the network and displays them.
  This is used to demonstrate a frame input stream session.
  Ensure that you have connected the selected interface to another Ethernet interface that is
  transmitting data.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python ethernet-frame-stream-input-reader.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"
"""

import sys
import time
from datetime import datetime

import grpc
import nixnet_pb2 as nixnet_types
import nixnet_pb2_grpc as grpc_nixnet


CHOOSE_MONITOR_OR_ENDPOINT_TEXT = (
    "\nPress 'm' followed by enter to configure the input stream session to use the monitor path"
    " to monitor all network traffic else press any other key followed by enter to use the"
    " endpoint path which filters traffic based on VLAN ID and priority. :"
)
FRAME_CHECK_SEQUENCE_SIZE = 4
MAX_ENET_FRAME_SIZE = 1518
NUM_OF_FRAMES = 1
MAX_PAYLOAD_PER_FRAME = MAX_ENET_FRAME_SIZE + FRAME_CHECK_SEQUENCE_SIZE

# Parameters
SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
INTERFACE = "ENET1"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    INTERFACE = sys.argv[3]


def check_for_error(status):
    """Raise an exception if the status indicates an error."""
    if status != 0:
        error_message_response = client.StatusToString(
            nixnet_types.StatusToStringRequest(status_id=status)
        )
        raise Exception(error_message_response.status_description)


def print_timestamp(timestamp):
    """Print a timestamp to console."""
    local_dt = datetime.fromtimestamp(timestamp / 1e9)
    print(local_dt.strftime("%m/%d/%Y %H:%M:%S.%f")[:-3], end=" ")


# Declare all variables for the function
count = 0
session = None

# Receive filter only applies for endpoint mode.
flag = 3
vid = 2
priority = 3
mac = "AA:BB:CC:DD:EE:FF"  # MAC Address filter is not enabled. Use random string.

# Create the communication channel for the remote host and create connections to the NI-XNET and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nixnet.NiXnetStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.StatusToString(
            nixnet_types.StatusToStringRequest(status_id=response.status)
        )
        sys.stderr.write(
            f"{warning_message.status_description}\nWarning status: {response.status}\n"
        )


print(CHOOSE_MONITOR_OR_ENDPOINT_TEXT)
if sys.stdin.read(1) == "m":
    INTERFACE += "/monitor"

# Display parameters that will be used for the example.
print(f"Interface: {INTERFACE}", end="\n")

try:
    # Create an XNET session in SignalOutSinglePoint mode
    create_session_response = client.CreateSession(
        nixnet_types.CreateSessionRequest(
            database_name="",
            cluster_name="",
            list="",
            interface_name=INTERFACE,
            mode=nixnet_types.CREATE_SESSION_MODE_FRAME_IN_STREAM,
        )
    )
    session = create_session_response.session
    print("Session created successfully.\n")

    rxfilter = nixnet_types.EptRxFilter(
        use_flags=flag, vid=vid, priority=priority, destination_mac=mac
    )

    ept_rxfilter_array = nixnet_types.EptRxFilterArray(ept_rx_filter=[rxfilter])

    # Set Receive Filter (Only applies for endpoint mode)
    set_property_response = client.SetProperty(
        nixnet_types.SetPropertyRequest(
            session=session,
            property_id=nixnet_types.PROPERTY_SESSION_INTF_ENET_EPT_RECEIVE_FILTER,
            ept_rx_filter_array=ept_rxfilter_array,
        )
    )

    print("Reading all received frames.\n")
    print("Local Timestamp", "Network Timestamp", "Data")

    while count < 10:
        # Read the received frames into the buffer
        read_frame_response = client.ReadFrame(
            nixnet_types.ReadFrameRequest(
                session=session,
                number_of_frames=NUM_OF_FRAMES,
                max_payload_per_frame=MAX_PAYLOAD_PER_FRAME,
                protocol=nixnet_types.PROTOCOL_ENET,
                timeout=nixnet_types.TIME_OUT_INFINITE,
            )
        )
        check_for_warning(read_frame_response)
        frame_buffer = read_frame_response.buffer

        for i in range(0, len(frame_buffer)):
            print_timestamp(frame_buffer[i].enet.device_timestamp)
            print_timestamp(frame_buffer[i].enet.network_timestamp)

            for j in range(0, len(frame_buffer[i].enet.frame_data)):
                # Prints frame data in 2-digit hexadecimal format without '0x'
                print(
                    "{:02x}".format(int(frame_buffer[i].enet.frame_data[j])).upper(),
                    end=" ",
                )
            print("\n\n")

        time.sleep(1)
        count = count + 1

    print("Frame capture stopped.\n")

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Clear the XNET session.
    if session:
        client.Clear(nixnet_types.ClearRequest(session=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nixnet/flexray-signal-single-point-input.py sha256=10ba49ffadc4ab57466adaa5797ab5ca922fff46cca360ae96fbbcf9cd0b1cb0 bytes=5180 -->
## FILE: examples/nixnet/flexray-signal-single-point-input.py

- repository: `ni/grpc-device`
- source_path: `examples/nixnet/flexray-signal-single-point-input.py`
- sha256: `10ba49ffadc4ab57466adaa5797ab5ca922fff46cca360ae96fbbcf9cd0b1cb0`
- bytes: 5180

````python
r"""Read Signal Data.

 This example reads a signal value for 10 times.
 This is used to demonstrate a signal single point input session.
 This example uses hardcoded signal names that use the NIXNET_example database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the bus is properly terminated as this example does not enable the on-board
 termination.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python flexray-signal-single-point-input.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"
"""

import sys

import grpc
import nixnet_pb2 as nixnet_types
import nixnet_pb2_grpc as grpc_nixnet

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
INTERFACE = "FlexRay2"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    INTERFACE = sys.argv[3]

# Parameters
DATABASE = "NIXNET_example"
CLUSTER = "FlexRay_Cluster"
SIGNAL_LIST = "FlexRayEventSignal1,FlexRayEventSignal2"
NUM_SIGNALS = 2


i = 0
keyslot_id = 1
session = None

# Create the communication channel for the remote host and create connections to the NI-XNET and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nixnet.NiXnetStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.StatusToString(
            nixnet_types.StatusToStringRequest(status_id=response.status)
        )
        sys.stderr.write(
            f"{warning_message.status_description}\nWarning status: {response.status}\n"
        )


# Display parameters that will be used for the example.
print("Interface: " + INTERFACE, "Database: " + DATABASE, "Signal List: " + SIGNAL_LIST, sep="\n")
print("KeySlotId:", keyslot_id)

try:
    # Create an XNET session in SignalOutSinglePoint mode
    create_session_response = client.CreateSession(
        nixnet_types.CreateSessionRequest(
            database_name=DATABASE,
            cluster_name=CLUSTER,
            list=SIGNAL_LIST,
            interface_name=INTERFACE,
            mode=nixnet_types.CREATE_SESSION_MODE_SIGNAL_IN_SINGLE_POINT,
        )
    )
    session = create_session_response.session
    print("Session Created Successfully.\n")

    # Set the Key Slot
    client.SetProperty(
        nixnet_types.SetPropertyRequest(
            session=session,
            property_id=nixnet_types.PROPERTY_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID,
            u32_scalar=keyslot_id,
        )
    )

    # If no values are being written on the FlexRay port, the signals read would contain the
    # default value of 0.0
    while i < 10:
        # Update the signal data
        read_signal_response = client.ReadSignalSinglePoint(
            nixnet_types.ReadSignalSinglePointRequest(
                session=session,
                number_of_signals=NUM_SIGNALS,
            )
        )
        check_for_warning(read_signal_response)
        value_buffer = read_signal_response.value_buffer

        print("Signals received:")
        print(f"Signal 1: {value_buffer[0]}")
        print(f"Signal 2: {value_buffer[1]}", end="\n\n")
        i = i + 1

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Clear the XNET session.
    if session:
        client.Clear(nixnet_types.ClearRequest(session=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/nixnet/lin-signal-single-point-output.py sha256=d36b98ece9c6f97dae895824cfd6db03b5997326a7a86b9d0a4a18ce53e3e77d bytes=5588 -->
## FILE: examples/nixnet/lin-signal-single-point-output.py

- repository: `ni/grpc-device`
- source_path: `examples/nixnet/lin-signal-single-point-output.py`
- sha256: `d36b98ece9c6f97dae895824cfd6db03b5997326a7a86b9d0a4a18ce53e3e77d`
- bytes: 5588

````python
r"""Write Signal Data.

 This example writes a signal value for 10 times.
 This is used to demonstrate a signal single point output session.
 This example uses hardcoded signal names that use the NIXNET_exampleLDF database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the transceivers are externally powered when using C Series modules.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python lin-signal-single-point-output.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"
"""

import sys

import grpc
import nixnet_pb2 as nixnet_types
import nixnet_pb2_grpc as grpc_nixnet

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"
INTERFACE = "LIN1"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    INTERFACE = sys.argv[3]

# Parameters
DATABASE = "NIXNET_exampleLDF"
CLUSTER = "Cluster"
SIGNAL_LIST = "MasterSignal1_U16,MasterSignal2_U16"
NUM_SIGNALS = 2


i = 0
session = None
value_buffer = [0.0] * NUM_SIGNALS

# Create the communication channel for the remote host and create connections to the NI-XNET and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_nixnet.NiXnetStub(channel)


def check_for_warning(response):
    """Print to console if the status indicates a warning."""
    if response.status > 0:
        warning_message = client.StatusToString(
            nixnet_types.StatusToStringRequest(status_id=response.status)
        )
        sys.stderr.write(
            f"{warning_message.status_description}\nWarning status: {response.status}\n"
        )


# Change this to set the interface to slave mode
IS_MASTER = 1

# The schedule is identified by its index. The index is mapped to
# the schedules in the database. Index 0 is the first schedule
# displayed in the Database Editor.
SCHEDULE_INDEX = 0

# Display parameters that will be used for the example.
print("Interface: " + INTERFACE, "Database: " + DATABASE, "Signal List: " + SIGNAL_LIST, sep="\n")

try:
    if IS_MASTER != 0:
        print("Master?: Yes\n")
    else:
        print("Master?: No\n")

    # Create an XNET session in SignalOutSinglePoint mode
    create_session_response = client.CreateSession(
        nixnet_types.CreateSessionRequest(
            database_name=DATABASE,
            cluster_name=CLUSTER,
            list=SIGNAL_LIST,
            interface_name=INTERFACE,
            mode=nixnet_types.CREATE_SESSION_MODE_SIGNAL_OUT_SINGLE_POINT,
        )
    )
    session = create_session_response.session
    print("Session Created Successfully. \n")

    if IS_MASTER != 0:
        # Set the schedule - this will also automatically enable master mode
        write_state_value = nixnet_types.WriteStateValue(lin_schedule_change=SCHEDULE_INDEX)
        client.WriteState(
            nixnet_types.WriteStateRequest(
                session=session,
                state_id=nixnet_types.WRITE_STATE_LIN_SCHEDULE_CHANGE,
                state_value=write_state_value,
            )
        )

    print("Writing 10 values to LIN Interface.\n")

    while i <= 10:
        value_buffer[0] = float(i)
        value_buffer[1] = float(i * 10)

        # Update the signal data
        write_signal_response = client.WriteSignalSinglePoint(
            nixnet_types.WriteSignalSinglePointRequest(session=session, value_buffer=value_buffer)
        )
        check_for_warning(write_signal_response)

        print("Signals sent:")
        print(f"Signal 1: {value_buffer[0]}")
        print(f"Signal 2: {value_buffer[1]}", end="\n\n")
        i = i + 1

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")

finally:
    # Clear the XNET session.
    if session:
        client.Clear(nixnet_types.ClearRequest(session=session))
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/poetry.lock sha256=7c2bc8a13e302177f8e420d0df0ee8c44b0e2056dcfdef1e8359d4198252eff8 bytes=65563 -->
## FILE: examples/poetry.lock

- repository: `ni/grpc-device`
- source_path: `examples/poetry.lock`
- sha256: `7c2bc8a13e302177f8e420d0df0ee8c44b0e2056dcfdef1e8359d4198252eff8`
- bytes: 65563

````text
# This file is automatically @generated by Poetry 1.8.2 and should not be changed by hand.

[[package]]
name = "black"
version = "25.11.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.9"
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
name = "click"
version = "8.1.8"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.7"
files = [
    {file = "click-8.1.8-py3-none-any.whl", hash = "sha256:63c132bbbed01578a06712a2d1f497bb62d9c1c0d329b7903a866228027263b2"},
    {file = "click-8.1.8.tar.gz", hash = "sha256:ed53c9d8990d83c2a27deae68e4ee337473f6330c040a31d4225c9574d16096a"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "grpcio"
version = "1.78.1"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.9"
files = [
    {file = "grpcio-1.78.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:4393bef64cf26dc07cd6f18eaa5170ae4eebaafd4418e7e3a59ca9526a6fa30b"},
    {file = "grpcio-1.78.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:917047c19cd120b40aab9a4b8a22e9ce3562f4a1343c0d62b3cd2d5199da3d67"},
    {file = "grpcio-1.78.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:ff7de398bb3528d44d17e6913a7cfe639e3b15c65595a71155322df16978c5e1"},
    {file = "grpcio-1.78.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:15f6e636d1152667ddb4022b37534c161c8477274edb26a0b65b215dd0a81e97"},
    {file = "grpcio-1.78.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:27b5cb669603efb7883a882275db88b6b5d6b6c9f0267d5846ba8699b7ace338"},
    {file = "grpcio-1.78.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:86edb3966778fa05bfdb333688fde5dc9079f9e2a9aa6a5c42e9564b7656ba04"},
    {file = "grpcio-1.78.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:849cc62eb989bc3be5629d4f3acef79be0d0ff15622201ed251a86d17fef6494"},
    {file = "grpcio-1.78.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:9a00992d6fafe19d648b9ccb4952200c50d8e36d0cce8cf026c56ed3fdc28465"},
    {file = "grpcio-1.78.1-cp310-cp310-win32.whl", hash = "sha256:f8759a1347f3b4f03d9a9d4ce8f9f31ad5e5d0144ba06ccfb1ffaeb0ba4c1e20"},
    {file = "grpcio-1.78.1-cp310-cp310-win_amd64.whl", hash = "sha256:e840405a3f1249509892be2399f668c59b9d492068a2cf326d661a8c79e5e747"},
    {file = "grpcio-1.78.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:3a8aa79bc6e004394c0abefd4b034c14affda7b66480085d87f5fbadf43b593b"},
    {file = "grpcio-1.78.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:8e1fcb419da5811deb47b7749b8049f7c62b993ba17822e3c7231e3e0ba65b79"},
    {file = "grpcio-1.78.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:b071dccac245c32cd6b1dd96b722283b855881ca0bf1c685cf843185f5d5d51e"},
    {file = "grpcio-1.78.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:d6fb962947e4fe321eeef3be1ba5ba49d32dea9233c825fcbade8e858c14aaf4"},
    {file = "grpcio-1.78.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:a6afd191551fd72e632367dfb083e33cd185bf9ead565f2476bba8ab864ae496"},
    {file = "grpcio-1.78.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:b2acd83186305c0802dbc4d81ed0ec2f3e8658d7fde97cfba2f78d7372f05b89"},
    {file = "grpcio-1.78.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:5380268ab8513445740f1f77bd966d13043d07e2793487e61fd5b5d0935071eb"},
    {file = "grpcio-1.78.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:389b77484959bdaad6a2b7dda44d7d1228381dd669a03f5660392aa0e9385b22"},
    {file = "grpcio-1.78.1-cp311-cp311-win32.whl", hash = "sha256:9dee66d142f4a8cca36b5b98a38f006419138c3c89e72071747f8fca415a6d8f"},
    {file = "grpcio-1.78.1-cp311-cp311-win_amd64.whl", hash = "sha256:43b930cf4f9c4a2262bb3e5d5bc40df426a72538b4f98e46f158b7eb112d2d70"},
    {file = "grpcio-1.78.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:41e4605c923e0e9a84a2718e4948a53a530172bfaf1a6d1ded16ef9c5849fca2"},
    {file = "grpcio-1.78.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:39da1680d260c0c619c3b5fa2dc47480ca24d5704c7a548098bca7de7f5dd17f"},
    {file = "grpcio-1.78.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:b5d5881d72a09b8336a8f874784a8eeffacde44a7bc1a148bce5a0243a265ef0"},
    {file = "grpcio-1.78.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:888ceb7821acd925b1c90f0cdceaed1386e69cfe25e496e0771f6c35a156132f"},
    {file = "grpcio-1.78.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8942bdfc143b467c264b048862090c4ba9a0223c52ae28c9ae97754361372e42"},
    {file = "grpcio-1.78.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:716a544969660ed609164aff27b2effd3ff84e54ac81aa4ce77b1607ca917d22"},
    {file = "grpcio-1.78.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:4d50329b081c223d444751076bb5b389d4f06c2b32d51b31a1e98172e6cecfb9"},
    {file = "grpcio-1.78.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7e836778c13ff70edada16567e8da0c431e8818eaae85b80d11c1ba5782eccbb"},
    {file = "grpcio-1.78.1-cp312-cp312-win32.whl", hash = "sha256:07eb016ea7444a22bef465cce045512756956433f54450aeaa0b443b8563b9ca"},
    {file = "grpcio-1.78.1-cp312-cp312-win_amd64.whl", hash = "sha256:02b82dcd2fa580f5e82b4cf62ecde1b3c7cc9ba27b946421200706a6e5acaf85"},
    {file = "grpcio-1.78.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:2b7ad2981550ce999e25ce3f10c8863f718a352a2fd655068d29ea3fd37b4907"},
    {file = "grpcio-1.78.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:409bfe22220889b9906739910a0ee4c197a967c21b8dd14b4b06dd477f8819ce"},
    {file = "grpcio-1.78.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:34b6cb16f4b67eeb5206250dc5b4d5e8e3db939535e58efc330e4c61341554bd"},
    {file = "grpcio-1.78.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:39d21fd30d38a5afb93f0e2e71e2ec2bd894605fb75d41d5a40060c2f98f8d11"},
    {file = "grpcio-1.78.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:09fbd4bcaadb6d8604ed1504b0bdf7ac18e48467e83a9d930a70a7fefa27e862"},
    {file = "grpcio-1.78.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:db681513a1bdd879c0b24a5a6a70398da5eaaba0e077a306410dc6008426847a"},
    {file = "grpcio-1.78.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:f81816faa426da461e9a597a178832a351d6f1078102590a4b32c77d251b71eb"},
    {file = "grpcio-1.78.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ffbb760df1cd49e0989f9826b2fd48930700db6846ac171eaff404f3cfbe5c28"},
    {file = "grpcio-1.78.1-cp313-cp313-win32.whl", hash = "sha256:1a56bf3ee99af5cf32d469de91bf5de79bdac2e18082b495fc1063ea33f4f2d0"},
    {file = "grpcio-1.78.1-cp313-cp313-win_amd64.whl", hash = "sha256:8991c2add0d8505178ff6c3ae54bd9386279e712be82fa3733c54067aae9eda1"},
    {file = "grpcio-1.78.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:d101fe49b1e0fb4a7aa36ed0c3821a0f67a5956ef572745452d2cd790d723a3f"},
    {file = "grpcio-1.78.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:5ce1855e8cfc217cdf6bcfe0cf046d7cf81ddcc3e6894d6cfd075f87a2d8f460"},
    {file = "grpcio-1.78.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:cd26048d066b51f39fe9206e2bcc2cea869a5e5b2d13c8d523f4179193047ebd"},
    {file = "grpcio-1.78.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:4b8d7fda614cf2af0f73bbb042f3b7fee2ecd4aea69ec98dbd903590a1083529"},
    {file = "grpcio-1.78.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:656a5bd142caeb8b1efe1fe0b4434ecc7781f44c97cfc7927f6608627cf178c0"},
    {file = "grpcio-1.78.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:99550e344482e3c21950c034f74668fccf8a546d50c1ecb4f717543bbdc071ba"},
    {file = "grpcio-1.78.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:8f27683ca68359bd3f0eb4925824d71e538f84338b3ae337ead2ae43977d7541"},
    {file = "grpcio-1.78.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:a40515b69ac50792f9b8ead260f194ba2bb3285375b6c40c7ff938f14c3df17d"},
    {file = "grpcio-1.78.1-cp314-cp314-win32.whl", hash = "sha256:2c473b54ef1618f4fb85e82ff4994de18143b74efc088b91b5a935a3a45042ba"},
    {file = "grpcio-1.78.1-cp314-cp314-win_amd64.whl", hash = "sha256:e2a6b33d1050dce2c6f563c5caf7f7cbeebf7fba8cde37ffe3803d50526900d1"},
    {file = "grpcio-1.78.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:559f58b6823e1abc38f82e157800aff649146f8906f7998c356cd48ae274d512"},
    {file = "grpcio-1.78.1-cp39-cp39-macosx_11_0_universal2.whl", hash = "sha256:36aeff5ba8aaf70ceb2cbf6cbba9ad6beef715ad744841f3e0cd977ec02e5966"},
    {file = "grpcio-1.78.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:0fa9943d4c7f4a14a9a876153a4e8ee2bb20a410b65c09f31510b2a42271f41b"},
    {file = "grpcio-1.78.1-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:75fa92c47d048d696f12b81a775316fca68385ffc6e6cb1ed1d76c8562579f74"},
    {file = "grpcio-1.78.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ca6aebae928383e971d5eace4f1a217fd7aadaf18d5ddd3163d80354105e9068"},
    {file = "grpcio-1.78.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:5572c5dd1e43dbb452b466be9794f77e3502bdb6aa6a1a7feca72c98c5085ca7"},
    {file = "grpcio-1.78.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:e49e720cd6b092504ec7bb2f60eb459aaaf4ce0e5fe20521c201b179e93b5d5d"},
    {file = "grpcio-1.78.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:ebeec1383aed86530a5f39646984e92d6596c050629982ac54eeb4e2f6ead668"},
    {file = "grpcio-1.78.1-cp39-cp39-win32.whl", hash = "sha256:263307118791bc350f4642749a9c8c2d13fec496228ab11070973e568c256bfd"},
    {file = "grpcio-1.78.1-cp39-cp39-win_amd64.whl", hash = "sha256:13937b28986f45fee342806b07c6344db785ad74a549ebcb00c659142973556f"},
    {file = "grpcio-1.78.1.tar.gz", hash = "sha256:27c625532d33ace45d57e775edf1982e183ff8641c72e4e91ef7ba667a149d72"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.78.1)"]

[[package]]
name = "grpcio-tools"
version = "1.49.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
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
protobuf = ">=4.21.3,<5.0dev"
setuptools = "*"

[[package]]
name = "librt"
version = "0.8.1"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
files = [
    {file = "librt-0.8.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:81fd938344fecb9373ba1b155968c8a329491d2ce38e7ddb76f30ffb938f12dc"},
    {file = "librt-0.8.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:5db05697c82b3a2ec53f6e72b2ed373132b0c2e05135f0696784e97d7f5d48e7"},
    {file = "librt-0.8.1-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:d56bc4011975f7460bea7b33e1ff425d2f1adf419935ff6707273c77f8a4ada6"},
    {file = "librt-0.8.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5cdc0f588ff4b663ea96c26d2a230c525c6fc62b28314edaaaca8ed5af931ad0"},
    {file = "librt-0.8.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:97c2b54ff6717a7a563b72627990bec60d8029df17df423f0ed37d56a17a176b"},
    {file = "librt-0.8.1-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:8f1125e6bbf2f1657d9a2f3ccc4a2c9b0c8b176965bb565dd4d86be67eddb4b6"},
    {file = "librt-0.8.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:8f4bb453f408137d7581be309b2fbc6868a80e7ef60c88e689078ee3a296ae71"},
    {file = "librt-0.8.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:c336d61d2fe74a3195edc1646d53ff1cddd3a9600b09fa6ab75e5514ba4862a7"},
    {file = "librt-0.8.1-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:eb5656019db7c4deacf0c1a55a898c5bb8f989be904597fcb5232a2f4828fa05"},
    {file = "librt-0.8.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:c25d9e338d5bed46c1632f851babf3d13c78f49a225462017cf5e11e845c5891"},
    {file = "librt-0.8.1-cp310-cp310-win32.whl", hash = "sha256:aaab0e307e344cb28d800957ef3ec16605146ef0e59e059a60a176d19543d1b7"},
    {file = "librt-0.8.1-cp310-cp310-win_amd64.whl", hash = "sha256:56e04c14b696300d47b3bc5f1d10a00e86ae978886d0cee14e5714fafb5df5d2"},
    {file = "librt-0.8.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:681dc2451d6d846794a828c16c22dc452d924e9f700a485b7ecb887a30aad1fd"},
    {file = "librt-0.8.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:a3b4350b13cc0e6f5bec8fa7caf29a8fb8cdc051a3bae45cfbfd7ce64f009965"},
    {file = "librt-0.8.1-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:ac1e7817fd0ed3d14fd7c5df91daed84c48e4c2a11ee99c0547f9f62fdae13da"},
    {file = "librt-0.8.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:747328be0c5b7075cde86a0e09d7a9196029800ba75a1689332348e998fb85c0"},
    {file = "librt-0.8.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f0af2bd2bc204fa27f3d6711d0f360e6b8c684a035206257a81673ab924aa11e"},
    {file = "librt-0.8.1-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:d480de377f5b687b6b1bc0c0407426da556e2a757633cc7e4d2e1a057aa688f3"},
    {file = "librt-0.8.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d0ee06b5b5291f609ddb37b9750985b27bc567791bc87c76a569b3feed8481ac"},
    {file = "librt-0.8.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:9e2c6f77b9ad48ce5603b83b7da9ee3e36b3ab425353f695cba13200c5d96596"},
    {file = "librt-0.8.1-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:439352ba9373f11cb8e1933da194dcc6206daf779ff8df0ed69c5e39113e6a99"},
    {file = "librt-0.8.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:82210adabbc331dbb65d7868b105185464ef13f56f7f76688565ad79f648b0fe"},
    {file = "librt-0.8.1-cp311-cp311-win32.whl", hash = "sha256:52c224e14614b750c0a6d97368e16804a98c684657c7518752c356834fff83bb"},
    {file = "librt-0.8.1-cp311-cp311-win_amd64.whl", hash = "sha256:c00e5c884f528c9932d278d5c9cbbea38a6b81eb62c02e06ae53751a83a4d52b"},
    {file = "librt-0.8.1-cp311-cp311-win_arm64.whl", hash = "sha256:f7cdf7f26c2286ffb02e46d7bac56c94655540b26347673bea15fa52a6af17e9"},
    {file = "librt-0.8.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:a28f2612ab566b17f3698b0da021ff9960610301607c9a5e8eaca62f5e1c350a"},
    {file = "librt-0.8.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:60a78b694c9aee2a0f1aaeaa7d101cf713e92e8423a941d2897f4fa37908dab9"},
    {file = "librt-0.8.1-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:758509ea3f1eba2a57558e7e98f4659d0ea7670bff49673b0dde18a3c7e6c0eb"},
    {file = "librt-0.8.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:039b9f2c506bd0ab0f8725aa5ba339c6f0cd19d3b514b50d134789809c24285d"},
    {file = "librt-0.8.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5bb54f1205a3a6ab41a6fd71dfcdcbd278670d3a90ca502a30d9da583105b6f7"},
    {file = "librt-0.8.1-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:05bd41cdee35b0c59c259f870f6da532a2c5ca57db95b5f23689fcb5c9e42440"},
    {file = "librt-0.8.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:adfab487facf03f0d0857b8710cf82d0704a309d8ffc33b03d9302b4c64e91a9"},
    {file = "librt-0.8.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:153188fe98a72f206042be10a2c6026139852805215ed9539186312d50a8e972"},
    {file = "librt-0.8.1-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:dd3c41254ee98604b08bd5b3af5bf0a89740d4ee0711de95b65166bf44091921"},
    {file = "librt-0.8.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e0d138c7ae532908cbb342162b2611dbd4d90c941cd25ab82084aaf71d2c0bd0"},
    {file = "librt-0.8.1-cp312-cp312-win32.whl", hash = "sha256:43353b943613c5d9c49a25aaffdba46f888ec354e71e3529a00cca3f04d66a7a"},
    {file = "librt-0.8.1-cp312-cp312-win_amd64.whl", hash = "sha256:ff8baf1f8d3f4b6b7257fcb75a501f2a5499d0dda57645baa09d4d0d34b19444"},
    {file = "librt-0.8.1-cp312-cp312-win_arm64.whl", hash = "sha256:0f2ae3725904f7377e11cc37722d5d401e8b3d5851fb9273d7f4fe04f6b3d37d"},
    {file = "librt-0.8.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:7e6bad1cd94f6764e1e21950542f818a09316645337fd5ab9a7acc45d99a8f35"},
    {file = "librt-0.8.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:cf450f498c30af55551ba4f66b9123b7185362ec8b625a773b3d39aa1a717583"},
    {file = "librt-0.8.1-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:eca45e982fa074090057132e30585a7e8674e9e885d402eae85633e9f449ce6c"},
    {file = "librt-0.8.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0c3811485fccfda840861905b8c70bba5ec094e02825598bb9d4ca3936857a04"},
    {file = "librt-0.8.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e4af413908f77294605e28cfd98063f54b2c790561383971d2f52d113d9c363"},
    {file = "librt-0.8.1-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5212a5bd7fae98dae95710032902edcd2ec4dc994e883294f75c857b83f9aba0"},
    {file = "librt-0.8.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e692aa2d1d604e6ca12d35e51fdc36f4cda6345e28e36374579f7ef3611b3012"},
    {file = "librt-0.8.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:4be2a5c926b9770c9e08e717f05737a269b9d0ebc5d2f0060f0fe3fe9ce47acb"},
    {file = "librt-0.8.1-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:fd1a720332ea335ceb544cf0a03f81df92abd4bb887679fd1e460976b0e6214b"},
    {file = "librt-0.8.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:93c2af9e01e0ef80d95ae3c720be101227edae5f2fe7e3dc63d8857fadfc5a1d"},
    {file = "librt-0.8.1-cp313-cp313-win32.whl", hash = "sha256:086a32dbb71336627e78cc1d6ee305a68d038ef7d4c39aaff41ae8c9aa46e91a"},
    {file = "librt-0.8.1-cp313-cp313-win_amd64.whl", hash = "sha256:e11769a1dbda4da7b00a76cfffa67aa47cfa66921d2724539eee4b9ede780b79"},
    {file = "librt-0.8.1-cp313-cp313-win_arm64.whl", hash = "sha256:924817ab3141aca17893386ee13261f1d100d1ef410d70afe4389f2359fea4f0"},
    {file = "librt-0.8.1-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:6cfa7fe54fd4d1f47130017351a959fe5804bda7a0bc7e07a2cdbc3fdd28d34f"},
    {file = "librt-0.8.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:228c2409c079f8c11fb2e5d7b277077f694cb93443eb760e00b3b83cb8b3176c"},
    {file = "librt-0.8.1-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:7aae78ab5e3206181780e56912d1b9bb9f90a7249ce12f0e8bf531d0462dd0fc"},
    {file = "librt-0.8.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:172d57ec04346b047ca6af181e1ea4858086c80bdf455f61994c4aa6fc3f866c"},
    {file = "librt-0.8.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6b1977c4ea97ce5eb7755a78fae68d87e4102e4aaf54985e8b56806849cc06a3"},
    {file = "librt-0.8.1-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:10c42e1f6fd06733ef65ae7bebce2872bcafd8d6e6b0a08fe0a05a23b044fb14"},
    {file = "librt-0.8.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:4c8dfa264b9193c4ee19113c985c95f876fae5e51f731494fc4e0cf594990ba7"},
    {file = "librt-0.8.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:01170b6729a438f0dedc4a26ed342e3dc4f02d1000b4b19f980e1877f0c297e6"},
    {file = "librt-0.8.1-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:7b02679a0d783bdae30d443025b94465d8c3dc512f32f5b5031f93f57ac32071"},
    {file = "librt-0.8.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:190b109bb69592a3401fe1ffdea41a2e73370ace2ffdc4a0e8e2b39cdea81b78"},
    {file = "librt-0.8.1-cp314-cp314-win32.whl", hash = "sha256:e70a57ecf89a0f64c24e37f38d3fe217a58169d2fe6ed6d70554964042474023"},
    {file = "librt-0.8.1-cp314-cp314-win_amd64.whl", hash = "sha256:7e2f3edca35664499fbb36e4770650c4bd4a08abc1f4458eab9df4ec56389730"},
    {file = "librt-0.8.1-cp314-cp314-win_arm64.whl", hash = "sha256:0d2f82168e55ddefd27c01c654ce52379c0750ddc31ee86b4b266bcf4d65f2a3"},
    {file = "librt-0.8.1-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:2c74a2da57a094bd48d03fa5d196da83d2815678385d2978657499063709abe1"},
    {file = "librt-0.8.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a355d99c4c0d8e5b770313b8b247411ed40949ca44e33e46a4789b9293a907ee"},
    {file = "librt-0.8.1-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:2eb345e8b33fb748227409c9f1233d4df354d6e54091f0e8fc53acdb2ffedeb7"},
    {file = "librt-0.8.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9be2f15e53ce4e83cc08adc29b26fb5978db62ef2a366fbdf716c8a6c8901040"},
    {file = "librt-0.8.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:785ae29c1f5c6e7c2cde2c7c0e148147f4503da3abc5d44d482068da5322fd9e"},
    {file = "librt-0.8.1-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:1d3a7da44baf692f0c6aeb5b2a09c5e6fc7a703bca9ffa337ddd2e2da53f7732"},
    {file = "librt-0.8.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5fc48998000cbc39ec0d5311312dda93ecf92b39aaf184c5e817d5d440b29624"},
    {file = "librt-0.8.1-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:e96baa6820280077a78244b2e06e416480ed859bbd8e5d641cf5742919d8beb4"},
    {file = "librt-0.8.1-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:31362dbfe297b23590530007062c32c6f6176f6099646bb2c95ab1b00a57c382"},
    {file = "librt-0.8.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:cc3656283d11540ab0ea01978378e73e10002145117055e03722417aeab30994"},
    {file = "librt-0.8.1-cp314-cp314t-win32.whl", hash = "sha256:738f08021b3142c2918c03692608baed43bc51144c29e35807682f8070ee2a3a"},
    {file = "librt-0.8.1-cp314-cp314t-win_amd64.whl", hash = "sha256:89815a22daf9c51884fb5dbe4f1ef65ee6a146e0b6a8df05f753e2e4a9359bf4"},
    {file = "librt-0.8.1-cp314-cp314t-win_arm64.whl", hash = "sha256:bf512a71a23504ed08103a13c941f763db13fb11177beb3d9244c98c29fb4a61"},
    {file = "librt-0.8.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:3dff3d3ca8db20e783b1bc7de49c0a2ab0b8387f31236d6a026597d07fcd68ac"},
    {file = "librt-0.8.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:08eec3a1fc435f0d09c87b6bf1ec798986a3544f446b864e4099633a56fcd9ed"},
    {file = "librt-0.8.1-cp39-cp39-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:e3f0a41487fd5fad7e760b9e8a90e251e27c2816fbc2cff36a22a0e6bcbbd9dd"},
    {file = "librt-0.8.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:bacdb58d9939d95cc557b4dbaa86527c9db2ac1ed76a18bc8d26f6dc8647d851"},
    {file = "librt-0.8.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b6d7ab1f01aa753188605b09a51faa44a3327400b00b8cce424c71910fc0a128"},
    {file = "librt-0.8.1-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:4998009e7cb9e896569f4be7004f09d0ed70d386fa99d42b6d363f6d200501ac"},
    {file = "librt-0.8.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:2cc68eeeef5e906839c7bb0815748b5b0a974ec27125beefc0f942715785b551"},
    {file = "librt-0.8.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:0bf69d79a23f4f40b8673a947a234baeeb133b5078b483b7297c5916539cf5d5"},
    {file = "librt-0.8.1-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:22b46eabd76c1986ee7d231b0765ad387d7673bbd996aa0d0d054b38ac65d8f6"},
    {file = "librt-0.8.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:237796479f4d0637d6b9cbcb926ff424a97735e68ade6facf402df4ec93375ed"},
    {file = "librt-0.8.1-cp39-cp39-win32.whl", hash = "sha256:4beb04b8c66c6ae62f8c1e0b2f097c1ebad9295c929a8d5286c05eae7c2fc7dc"},
    {file = "librt-0.8.1-cp39-cp39-win_amd64.whl", hash = "sha256:64548cde61b692dc0dc379f4b5f59a2f582c2ebe7890d09c1ae3b9e66fa015b7"},
    {file = "librt-0.8.1.tar.gz", hash = "sha256:be46a14693955b3bd96014ccbdb8339ee8c9346fbe11c1b78901b55125f14c73"},
]

[[package]]
name = "mypy"
version = "1.19.1"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.9"
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
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "mypy-protobuf"
version = "3.6.0"
description = "Generate mypy stub files from protobuf specs"
optional = false
python-versions = ">=3.8"
files = [
    {file = "mypy-protobuf-3.6.0.tar.gz", hash = "sha256:02f242eb3409f66889f2b1a3aa58356ec4d909cdd0f93115622e9e70366eca3c"},
    {file = "mypy_protobuf-3.6.0-py3-none-any.whl", hash = "sha256:56176e4d569070e7350ea620262478b49b7efceba4103d468448f1d21492fd6c"},
]

[package.dependencies]
protobuf = ">=4.25.3"
types-protobuf = ">=4.24"

[[package]]
name = "packaging"
version = "26.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
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
name = "platformdirs"
version = "4.4.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.9"
files = [
    {file = "platformdirs-4.4.0-py3-none-any.whl", hash = "sha256:abd01743f24e5287cd7a5db3752faf1a2d65353f38ec26d98e25a6db65958c85"},
    {file = "platformdirs-4.4.0.tar.gz", hash = "sha256:ca753cf4d81dc309bc67b0ea38fd15dc97bc30ce419a7f58d13eb3bf14c4febf"},
]

[package.extras]
docs = ["furo (>=2024.8.6)", "proselint (>=0.14)", "sphinx (>=8.1.3)", "sphinx-autodoc-typehints (>=3)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.3.4)", "pytest-cov (>=6)", "pytest-mock (>=3.14)"]
type = ["mypy (>=1.14.1)"]

[[package]]
name = "protobuf"
version = "4.25.8"
description = ""
optional = false
python-versions = ">=3.8"
files = [
    {file = "protobuf-4.25.8-cp310-abi3-win32.whl", hash = "sha256:504435d831565f7cfac9f0714440028907f1975e4bed228e58e72ecfff58a1e0"},
    {file = "protobuf-4.25.8-cp310-abi3-win_amd64.whl", hash = "sha256:bd551eb1fe1d7e92c1af1d75bdfa572eff1ab0e5bf1736716814cdccdb2360f9"},
    {file = "protobuf-4.25.8-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:ca809b42f4444f144f2115c4c1a747b9a404d590f18f37e9402422033e464e0f"},
    {file = "protobuf-4.25.8-cp37-abi3-manylinux2014_aarch64.whl", hash = "sha256:9ad7ef62d92baf5a8654fbb88dac7fa5594cfa70fd3440488a5ca3bfc6d795a7"},
    {file = "protobuf-4.25.8-cp37-abi3-manylinux2014_x86_64.whl", hash = "sha256:83e6e54e93d2b696a92cad6e6efc924f3850f82b52e1563778dfab8b355101b0"},
    {file = "protobuf-4.25.8-cp38-cp38-win32.whl", hash = "sha256:27d498ffd1f21fb81d987a041c32d07857d1d107909f5134ba3350e1ce80a4af"},
    {file = "protobuf-4.25.8-cp38-cp38-win_amd64.whl", hash = "sha256:d552c53d0415449c8d17ced5c341caba0d89dbf433698e1436c8fa0aae7808a3"},
    {file = "protobuf-4.25.8-cp39-cp39-win32.whl", hash = "sha256:077ff8badf2acf8bc474406706ad890466274191a48d0abd3bd6987107c9cde5"},
    {file = "protobuf-4.25.8-cp39-cp39-win_amd64.whl", hash = "sha256:f4510b93a3bec6eba8fd8f1093e9d7fb0d4a24d1a81377c10c0e5bbfe9e4ed24"},
    {file = "protobuf-4.25.8-py3-none-any.whl", hash = "sha256:15a0af558aa3b13efef102ae6e4f3efac06f1eea11afb3a57db2901447d9fb59"},
    {file = "protobuf-4.25.8.tar.gz", hash = "sha256:6135cf8affe1fc6f76cced2641e4ea8d3e59518d1f24ae41ba97bcad82d397cd"},
]

[[package]]
name = "pytokens"
version = "0.4.1"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
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
name = "setuptools"
version = "80.10.2"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
files = [
    {file = "setuptools-80.10.2-py3-none-any.whl", hash = "sha256:95b30ddfb717250edb492926c92b5221f7ef3fbcc2b07579bcd4a27da21d0173"},
    {file = "setuptools-80.10.2.tar.gz", hash = "sha256:8b0e9d10c784bf7d262c4e5ec5d4ec94127ce206e8738f29a437945fbc219b70"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1)", "ruff (>=0.8.0)"]
core = ["importlib_metadata (>=6)", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1)", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21)", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2)", "jaraco.develop (>=7.21)", "mypy (==1.14.*)", "pytest-mypy"]

[[package]]
name = "tomli"
version = "2.4.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
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
name = "types-grpcio"
version = "1.0.0.20251009"
description = "Typing stubs for grpcio"
optional = false
python-versions = ">=3.9"
files = [
    {file = "types_grpcio-1.0.0.20251009-py3-none-any.whl", hash = "sha256:112ac4312a5b0a273a4c414f7f2c7668f342990d9c6ab0f647391c36331f95ed"},
    {file = "types_grpcio-1.0.0.20251009.tar.gz", hash = "sha256:a8f615ea7a47b31f10da028ab5258d4f1611fbd70719ca450fc0ab3fb9c62b63"},
]

[[package]]
name = "types-protobuf"
version = "6.32.1.20251210"
description = "Typing stubs for protobuf"
optional = false
python-versions = ">=3.9"
files = [
    {file = "types_protobuf-6.32.1.20251210-py3-none-any.whl", hash = "sha256:2641f78f3696822a048cfb8d0ff42ccd85c25f12f871fbebe86da63793692140"},
    {file = "types_protobuf-6.32.1.20251210.tar.gz", hash = "sha256:c698bb3f020274b1a2798ae09dc773728ce3f75209a35187bd11916ebfde6763"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[metadata]
lock-version = "2.0"
python-versions = ">=3.9,<3.12"
content-hash = "da76641d504102f262aec8b34d2a4b5d2db2340a15205816bff96256924465bf"
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/pyproject.toml sha256=723728b8fadb718443dfe852c1e91e5a909755cb97b142ccffbff0b3443d1938 bytes=626 -->
## FILE: examples/pyproject.toml

- repository: `ni/grpc-device`
- source_path: `examples/pyproject.toml`
- sha256: `723728b8fadb718443dfe852c1e91e5a909755cb97b142ccffbff0b3443d1938`
- bytes: 626

````toml
[tool.poetry]
name = "ni-grpc-device-examples"
version = "1.8.2"
description = ""
authors = ["Christian Aguilar <christian.aguilar@ni.com>"]
package-mode = false

[tool.poetry.dependencies]
python = ">=3.9,<3.12"
grpcio = "^1.49.1"

[tool.poetry.group.dev.dependencies]
grpcio-tools = "1.49.1"
mypy = ">=1.0"
mypy-protobuf = "3.6.0"
types-protobuf = ">=5.28.3.20241203"
types-grpcio = ">=1.0"
black = ">=23.3.0"
setuptools = "^80.9.0"

[[tool.mypy.overrides]]
# nifpga has a field named "property" which shadows the built-in "@property" decorator.
module = ["nifpga_pb2"]
disable_error_code = "operator"
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/session/session-reservation.py sha256=ee5b096067aeec6e9efba35a281ee85b7aeae929ad89908d99f098f4be5dd83a bytes=7211 -->
## FILE: examples/session/session-reservation.py

- repository: `ni/grpc-device`
- source_path: `examples/session/session-reservation.py`
- sha256: `ee5b096067aeec6e9efba35a281ee85b7aeae929ad89908d99f098f4be5dd83a`
- bytes: 7211

````python
r"""Initiate a session and exercise some common reservation operations on the session.

This particular example is using NI-SCOPE but the session reservation API should work for any driver
session.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python session-reservation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.
"""

import sys

import grpc
import niscope_pb2 as niscope_types
import niscope_pb2_grpc as grpc_niscope
import session_utilities_pb2 as session_types
import session_utilities_pb2_grpc as grpc_session

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Resource name and options for a simulated 5164 client. Change them according to the NI-SCOPE
# model.
RESOURCE = "SimulatedScope"
OPTIONS = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe"

CLIENT_1_ID = "Client1"
CLIENT_2_ID = "Client2"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]
if len(sys.argv) >= 4:
    RESOURCE = sys.argv[3]
    OPTIONS = ""

# Create the communication channel for the remote host and create connections to the NI-SCOPE and
# session services.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
niscope_client = grpc_niscope.NiScopeStub(channel)
session_client = grpc_session.SessionUtilitiesStub(channel)


try:
    # Reset server to start in a fresh state.
    reset_server_response = session_client.ResetServer(session_types.ResetServerRequest())
    assert reset_server_response.is_server_reset

    # Open session to NI-SCOPE module with options.
    session_name = "NI-Scope-Session-1"
    print("\nInitializing session...")
    init_with_options_response = niscope_client.InitWithOptions(
        niscope_types.InitWithOptionsRequest(
            session_name=session_name, resource_name=RESOURCE, id_query=False, option_string=OPTIONS
        )
    )
    vi = init_with_options_response.vi
    print(f"Session initialized with name {session_name}.\n")

    # Check if session is reserved by client 1.
    # Note: The reservation_id is defined by and has meaning only for the client + Session
    # Reservation API.
    print(f"Checking if {session_name} is reserved by {CLIENT_1_ID}...")
    is_reserved_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_1_ID)
    )
    assert not is_reserved_response.is_reserved
    print(f"{session_name} is not reserved by {CLIENT_1_ID}.\n")

    # Reserve session for client 1.
    print(f"Reserving {session_name} for {CLIENT_1_ID}...")
    reserve_response = session_client.Reserve(
        session_types.ReserveRequest(reservation_id=session_name, client_id=CLIENT_1_ID)
    )
    is_reserved = reserve_response.is_reserved
    assert is_reserved
    is_reserved_by_client1_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_1_ID)
    )
    assert is_reserved_by_client1_response.is_reserved
    print(f"{session_name} is reserved by {CLIENT_1_ID}.\n")

    # Check reservation on client 2.
    print(f"Checking if {session_name} is reserved by {CLIENT_2_ID}...")
    is_reserved_by_client2_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_2_ID)
    )
    assert not is_reserved_by_client2_response.is_reserved
    print(f"{session_name} is not reserved by {CLIENT_2_ID}.\n")

    # Unreserve on client 1.
    print(f"Unreserving {session_name} reserved by {CLIENT_1_ID}...")
    is_unreserved_response = session_client.Unreserve(
        session_types.UnreserveRequest(reservation_id=session_name, client_id=CLIENT_1_ID)
    )
    assert is_unreserved_response.is_unreserved
    is_reserved_by_client1_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_1_ID)
    )
    assert not is_reserved_by_client1_response.is_reserved
    print(f"{session_name} is no longer reserved by {CLIENT_1_ID}.\n")

    print(f"Reserving {session_name} for {CLIENT_2_ID}...")
    reserve_response = session_client.Reserve(
        session_types.ReserveRequest(reservation_id=session_name, client_id=CLIENT_2_ID)
    )
    is_reserved = reserve_response.is_reserved
    assert is_reserved
    is_reserved_by_client2_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_2_ID)
    )
    assert is_reserved_by_client2_response.is_reserved
    print(f"{session_name} is reserved by {CLIENT_2_ID}.\n")

    # Reset server.
    print(f"Resetting the server...")
    reset_server_response = session_client.ResetServer(session_types.ResetServerRequest())
    assert reset_server_response.is_server_reset
    is_reserved_by_client2_response = session_client.IsReservedByClient(
        session_types.IsReservedByClientRequest(reservation_id=session_name, client_id=CLIENT_2_ID)
    )
    assert not is_reserved_by_client2_response.is_reserved
    print(f"All sessions have been closed and reservations have been cleared.\n")

# If NI-SCOPE API or Session API throws an exception, print the error message.
except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/session/session-utilities.py sha256=c991b4e1f13b031bb26918f7aa3a8340dcf65709972b736af2e509092d537ea3 bytes=6049 -->
## FILE: examples/session/session-utilities.py

- repository: `ni/grpc-device`
- source_path: `examples/session/session-utilities.py`
- sha256: `c991b4e1f13b031bb26918f7aa3a8340dcf65709972b736af2e509092d537ea3`
- bytes: 6049

````python
r"""Commands that can get information about the server.

Getting Started:

To run this example, install NI System Configuration on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.system-configuration.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from the command line:

usage: session-utilities.py [-h]
                   [server_address] [port_number]
                   {enumerate-devices,enumerate-software} ...

positional arguments:
  server_address        The IP address or machine name of the server. The default is localhost.
  port_number           The port number of the server. The default is 31763.

optional arguments:
  -h, --help            show the help message and exit

subcommands:
  {enumerate-devices,enumerate-software}
    enumerate-devices   Prints the list of devices connected to the server.
    enumerate-software  Prints the list of NI software packages installed on the server.
"""

import argparse

import grpc
import session_utilities_pb2 as session_types
import session_utilities_pb2_grpc as grpc_session


def main(args):
    """Open a connection to the server, then run the command specified in args."""
    # Store command line args
    server_address = args.server_address
    server_port = args.port_number
    action = args.action

    # Open communication with the server using gRPC APIs.
    channel = grpc.insecure_channel(f"{server_address}:{server_port}")
    client = grpc_session.SessionUtilitiesStub(channel)

    try:
        if action == "enumerate-devices":
            enumerate_devices(client)
        elif action == "enumerate-software":
            enumerate_software(client, args.show_hidden)

    # If the API throws an exception, print the error message.
    except grpc.RpcError as rpc_error:
        error_message = str(rpc_error.details() or "")
        for entry in rpc_error.trailing_metadata() or []:
            if entry.key == "ni-error":
                value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
                error_message += f"\nError status: {value}"
        if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
            error_message = f"Failed to connect to server on {server_address}:{server_port}"
        elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
            error_message = (
                "The operation is not implemented or is not supported/enabled in this service"
            )
        print(f"{error_message}")


def enumerate_devices(client):
    """Retrieve and print a list of devices (simulated and physical) connected to the server."""
    enumerate_devices_response = client.EnumerateDevices(session_types.EnumerateDevicesRequest())
    print_devices(enumerate_devices_response.devices)


def enumerate_software(client, show_hidden_packages):
    """Retrieve and print a list of NI packages installed on the server."""
    enumerate_software_response = client.EnumerateInstalledSoftware(
        session_types.EnumerateInstalledSoftwareRequest(
            include_hidden_packages=show_hidden_packages
        )
    )
    print_software(enumerate_software_response.software)


# Display devices connected to the server.
def print_devices(devices):
    """Print device info."""
    if not devices:
        print("No devices are connected.")
        return
    print(
        "\n-----------------------------------------------------------------------------------------------------\n"
    )
    print("  List of devices connected to the server: \n")
    print(
        "-----------------------------------------------------------------------------------------------------\n"
    )
    for device in devices:
        print(f"    {device.name}")
        print(f"        Model: {device.model}")
        print(f"        Vendor: {device.vendor}")
        print(f"        Serial Number: {device.serial_number} \n")


# Display software installed on the server.
def print_software(software):
    """Print software info."""
    if not software:
        print("No NI packages found.")
        return
    print(
        "\n-----------------------------------------------------------------------------------------------------\n"
    )
    print("  List of NI software installed on the server: \n")
    print(
        "-----------------------------------------------------------------------------------------------------\n"
    )
    for package in software:
        print(f"    Package ID: {package.package_id}")
        print(f"    Product Name: {package.product_name}")
        print(f"    Version: {package.package_version} \n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Commands that can get information about the server."
    )
    parser.add_argument(
        "server_address",
        help="The IP address or machine name of the server. The default is localhost.",
        nargs="?",
        default="localhost",
    )
    parser.add_argument(
        "port_number",
        help="The port number of the server. The default is 31763.",
        nargs="?",
        default="31763",
    )
    subparsers = parser.add_subparsers(title="subcommands", dest="action", required=True)
    subparsers.add_parser(
        "enumerate-devices",
        help="Prints the list of devices connected to the server.",
    )
    parser_enumerate_software = subparsers.add_parser(
        "enumerate-software",
        help="Prints the list of NI software packages installed on the server.",
    )
    parser_enumerate_software.add_argument(
        "--show-hidden",
        help="Include hidden packages in the list of software.",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()
    main(args)
````

<!--NI_OSS_SOURCE repo=grpc-device path=examples/visa/find-resources.py sha256=5ae7a1a1180bf0af3a8605f30d2d9f5ba456ebe269e6c582b044c5c694e06aee bytes=2566 -->
## FILE: examples/visa/find-resources.py

- repository: `ni/grpc-device`
- source_path: `examples/visa/find-resources.py`
- sha256: `5ae7a1a1180bf0af3a8605f30d2d9f5ba456ebe269e6c582b044c5c694e06aee`
- bytes: 2566

````python
r"""Perform continuous measure record.

The gRPC API is built from the C API. NI-VISA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\VISA\WinNT\NIvisa\ni-visa.chm

Getting Started:

To run this example, install "NI-VISA" on the server machine:
  https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python find-resources.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".
"""

import sys

import grpc
import visa_pb2 as visa_types
import visa_pb2_grpc as grpc_visa

SERVER_ADDRESS = "localhost"
SERVER_PORT = "31763"

# Read in cmd args
if len(sys.argv) >= 2:
    SERVER_ADDRESS = sys.argv[1]
if len(sys.argv) >= 3:
    SERVER_PORT = sys.argv[2]


# Create the communication channel for the remote host and a connection to the NI-VISA service.
channel = grpc.insecure_channel(f"{SERVER_ADDRESS}:{SERVER_PORT}")
client = grpc_visa.VisaStub(channel)

try:
    # Query for resources.
    find_resources_resp = client.FindRsrc(visa_types.FindRsrcRequest(expression="?*"))

    # Get information about each resource.
    for resource in find_resources_resp.instrument_descriptor:
        parse_resp = client.ParseRsrc(visa_types.ParseRsrcRequest(resource_name=resource))
        print(
            f"Resource: {parse_resp.expanded_unaliased_name}, Class: {parse_resp.resource_class}, Alias: {parse_resp.alias_if_exists}"
        )

except grpc.RpcError as rpc_error:
    error_message = str(rpc_error.details() or "")
    for entry in rpc_error.trailing_metadata() or []:
        if entry.key == "ni-error":
            value = entry.value if isinstance(entry.value, str) else entry.value.decode("utf-8")
            error_message += f"\nError status: {value}"
    if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
        error_message = f"Failed to connect to server on {SERVER_ADDRESS}:{SERVER_PORT}"
    elif rpc_error.code() == grpc.StatusCode.UNIMPLEMENTED:
        error_message = (
            "The operation is not implemented or is not supported/enabled in this service"
        )
    print(f"{error_message}")
````
