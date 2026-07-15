# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/.github/workflows/maven-publish.yml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `.github/workflows/maven-publish.yml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/.github/workflows/maven-publish.yml
- source_bytes: 2661
- source_sha256: `49dc3c5ebf5bbd5d6fc8e79f0354766fd03bb34d11227ad56f1a3afe43f521cd`
- decoded_as: `utf-8`


## EXACT SOURCE

````yaml
# This workflow will build a Java project with Maven, and cache/restore any dependencies to improve the workflow execution time
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-java-with-maven

# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

name: Publish Release Build

on:
  workflow_dispatch:
  release:
      types: [published]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up JDK 21
      uses: actions/setup-java@v4
      with:
        java-version: '21'
        distribution: 'temurin'
        cache: maven
    # Keep the checkout unchanged and pass the non-SNAPSHOT revision to Maven
    # explicitly, because versions:set updates project.version but leaves the
    # revision property behind in this build.
    - name: Resolve release version
      run: |
        release_version=$(sed -n 's:.*<revision>\(.*\)</revision>.*:\1:p' pom.xml | head -n 1 | sed 's/-SNAPSHOT$//')
        echo "RELEASE_VERSION=${release_version}" >> "$GITHUB_ENV"
    - name: Publish to Github Packages
      run: ./mvnw -B clean deploy -DskipTests=true -Drevision=${{ env.RELEASE_VERSION }}
      env:
        GITHUB_TOKEN: ${{ github.token }} # GITHUB_TOKEN is the default env for the password
    - name: Upload SysML Library .kpar files
      uses: actions/upload-artifact@v5
      with:
        name: sysml-library-kpar
        path: sysml.library/output/*.kpar

  release:
    name: Release
    runs-on: ubuntu-latest
    needs: [build]
    if: ${{ startsWith(github.ref, 'refs/tags/') }}
    permissions:
      # Use to sign the release artifacts
      id-token: write
      # Used to upload release artifacts
      contents: write
      # Used to generate artifact attestation
      attestations: write
    steps:
      - uses: actions/download-artifact@v6
        with:
          name: sysml-library-kpar
          path: kpars
      - name: Generate artifact attestation
        uses: actions/attest-build-provenance@v3
        with:
          subject-path: 'kpars/*.kpar'
      - name: Create a release
        uses: softprops/action-gh-release@v2
        with:
          make_latest: true
          files: |
            kpars/*
          overwrite_files: false
          body:
          append_body: true
          name: ${{ github.event.inputs.tag_name || github.event.release.tag_name }} - SysML v2 Pilot Implementation

````
