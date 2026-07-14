# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/.github/workflows/build.yml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `.github/workflows/build.yml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/.github/workflows/build.yml
- source_bytes: 1905
- source_sha256: `80bf8091ab1a925acd9ca56a1a36fac7da7100deb33baf9d86ade6996aa76887`
- decoded_as: `utf-8`


## EXACT SOURCE

````yaml
# This workflow will build a Java project with Maven, and cache/restore any dependencies to improve the workflow execution time
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-java-with-maven

# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

name: Java CI with Maven

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: '**'

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
    - name: Build with Maven
      run: ./mvnw -B clean verify --file pom.xml -Dsysml.build-tag=nightly-$(date +'%Y%m%d') -Dsysml.metadata-tag=$(date +'%Y%m%d')
    - name: Upload SysML Library .kpar files
      uses: actions/upload-artifact@v5
      with:
        name: sysml-library-kpar
        path: sysml.library/output/*.kpar
    - name: Publish Test Report
      uses: mikepenz/action-junit-report@v5
      if: success() || failure() # always run even if the previous step fails
      with:
        report_paths: '**/target/surefire-reports/TEST-*.xml'
        include_passed: true
    - name: Verify index generation
      run: echo $(git diff -- sysml.library/.index.json) | grep -e '^$' || (echo "Library index in the git repository is not up to date. Please re-generate it and push changes to the repository."; exit 1)
    - name: Publish to Github Packages
      if: github.event_name != 'pull_request'
      run: ./mvnw -B deploy -DskipTests=true
      env:
        GITHUB_TOKEN: ${{ github.token }} # GITHUB_TOKEN is the default env for the password

````
