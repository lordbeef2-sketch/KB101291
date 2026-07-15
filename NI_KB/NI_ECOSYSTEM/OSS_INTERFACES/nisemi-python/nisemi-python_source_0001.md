# NI OSS SOURCE SNAPSHOT: nisemi-python

<!--NI_OSS_SNAPSHOT repo=ni/nisemi-python commit=0da9300d33d2348311fd9ccd785b207c926ab824 -->

<!--NI_OSS_SOURCE repo=nisemi-python path=.github/CODEOWNERS sha256=fc46dd15515654de2c43cc3d39f30b8eaf4f5b263fb948699bc9e7439fa51856 bytes=11 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nisemi-python`
- source_path: `.github/CODEOWNERS`
- sha256: `fc46dd15515654de2c43cc3d39f30b8eaf4f5b263fb948699bc9e7439fa51856`
- bytes: 11

````text
* @jazbell3
````

<!--NI_OSS_SOURCE repo=nisemi-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=38fc7e18cac2586cb399989efface495bac65cf3da2bd46d0dce65a1893d25e7 bytes=363 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nisemi-python`
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

<!--NI_OSS_SOURCE repo=nisemi-python path=.github/workflows/PR.yml sha256=483a133bf4ea699245087d4d4bdcb7f0b01496567aaeee3e10fa33e134681578 bytes=945 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/nisemi-python`
- source_path: `.github/workflows/PR.yml`
- sha256: `483a133bf4ea699245087d4d4bdcb7f0b01496567aaeee3e10fa33e134681578`
- bytes: 945

````yaml
name: PR

on:
  pull_request:
    branches:
      - 'main'
      
env:
  POETRY_VERSION: 1.4.2
  
jobs:
  checks-nisdc:
    runs-on: ubuntu-latest
    env:
      PYTHON_VERSION: 3.8
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - uses: Gr1N/setup-poetry@v8
        with:
          poetry-version: ${{ env.POETRY_VERSION }}
      - uses: Gr1N/setup-poetry@v8
        with:
          poetry-version: ${{ env.POETRY_VERSION }}
      - name: Check for lock changes (nisdc)
        run: poetry lock --check
      - uses: actions/cache@v3
        with:
          path: ~/.cache/pypoetry/virtualenvs
          key: ${{ runner.os }}-poetry-${{ hashFiles('poetry.lock') }}
      - name: Install nisdc
        run: poetry install -v
      - name: Lint nisdc
        run: poetry run ni-python-styleguide lint
  
````

<!--NI_OSS_SOURCE repo=nisemi-python path=.github/workflows/Publish_NIMS.yml sha256=23ce0d0964d65565d24895c87bbe3178f4fe59ad47456c3e33f90a287f17f88c bytes=1871 -->
## FILE: .github/workflows/Publish_NIMS.yml

- repository: `ni/nisemi-python`
- source_path: `.github/workflows/Publish_NIMS.yml`
- sha256: `23ce0d0964d65565d24895c87bbe3178f4fe59ad47456c3e33f90a287f17f88c`
- bytes: 1871

````yaml
name:  Update docs and Publish NIMS

on:
  release:
    types: [released]

concurrency: publish_to_pypi

env:
  # Versions are also listed in PR.yml
  POETRY_VERSION: 1.4.2
  PYTHON_VERSION: 3.8

jobs:
  build:
    name: Publish NIMS Package to PyPI
    runs-on : ubuntu-latest 
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - uses: Gr1N/setup-poetry@v8
        with:
          poetry-version: ${{ env.POETRY_VERSION }}

      - name: Check for lock changes
        run: poetry lock --check

      - uses: actions/cache@v2
        with:
          path: ~/.cache/pypoetry/virtualenvs
          key: ${{ runner.os }}-poetry-${{ hashFiles('poetry.lock') }}

      - name: Setup NIMS
        run: poetry install

      - name: Lint NIMS
        run: poetry run ni-python-styleguide lint

      # If the tag is 0.1.0, this will set the version of NIMS package to 0.1.0
      - name: Store version from Tag
        id: vars
        run: echo ::set-output name=tag::${GITHUB_REF#refs/*/}

      - name: Update NIMS package version based on tag name.
        run: |
          poetry version ${{ steps.vars.outputs.tag }}

      - name: Setup NIMS with docs
        run: poetry install --with docs

      # To Test the Publish use : poetry publish --build --username __token__ --password ${{ secrets.TEST_PYPI_TOKEN }} -r test-pypi
      - name: Build NIMS Python package and publish to PyPI
        if: ${{ startsWith(github.event.release.target_commitish, 'main') }}
        run: |
          poetry publish --build --username __token__ --password ${{ secrets.PYPI_TOKEN }}
        
      - uses: actions/upload-artifact@v3
        with:
          name: NIMS Artifacts
          path: dist/ # path/to/artifact
````

<!--NI_OSS_SOURCE repo=nisemi-python path=CONTRIBUTING.md sha256=96a5bda5fed801aab4fd20af30af2e24d7ad3defd3e01bf7162b4fc9ad4ae3f9 bytes=3200 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nisemi-python`
- source_path: `CONTRIBUTING.md`
- sha256: `96a5bda5fed801aab4fd20af30af2e24d7ad3defd3e01bf7162b4fc9ad4ae3f9`
- bytes: 3200

````markdown
# Contributing to \<nisdc\> 

Contributions to \<nisdc\> are welcome from all!

\<nisdc\> is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on '[GitHub]<https://github.com/ni/nisdc/>'_.

\<nisdc\> follows a pull-request model for development.  If you wish to
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

1. Pre requisite: Install pythonnet and Semiconductor Device Control addon for InstrumentStudio 2019 from NI package manager. Refer to Installation section of [Readme](README.md) 
2. Clone the repository and make your changes to APIs and examples using the practices mentioend above. 
3. For instruction to build, please refer to [packaging-project](https://packaging.python.org/tutorials/packaging-projects/). setup.py file present in this repository has the specificiation to build packages. You can use this start building the API pypi packages.
4. The latest build are also maintained in this github repository under the 'dist' folder.

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

See [LICENSE](https://github.com/ni/<nisdc>/blob/master/LICENSE)
for details about how \<nisdc\> is licensed.
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/conf/isconfig.sdconfig sha256=c256f313bee0461ddbce252e3962fd1f62a9ef8c0c4a934e0edd2e7a7ea75c10 bytes=5106 -->
## FILE: examples/conf/isconfig.sdconfig

- repository: `ni/nisemi-python`
- source_path: `examples/conf/isconfig.sdconfig`
- sha256: `c256f313bee0461ddbce252e3962fd1f62a9ef8c0c4a934e0edd2e7a7ea75c10`
- bytes: 5106

````text
{"ActiveHardwareConfig":{"ConfigName":"default-hw-config","ConfigString":"<?xml version=\"1.0\" encoding=\"utf-16\"?>\u000d\u000a<HardwareConfigurationSupport xmlns:xsd=\"http:\/\/www.w3.org\/2001\/XMLSchema\" xmlns:xsi=\"http:\/\/www.w3.org\/2001\/XMLSchema-instance\">\u000d\u000a  <IsOnline>false<\/IsOnline>\u000d\u000a  <InterfaceProtocolConfigurations>\u000d\u000a    <InterfaceProtocolDetails>\u000d\u000a      <InterfaceDetails>\u000d\u000a        <InterfaceInstanceName>Simulation1<\/InterfaceInstanceName>\u000d\u000a        <InterfaceType>Simulation<\/InterfaceType>\u000d\u000a        <InterfaceSettingNames \/>\u000d\u000a        <InterfaceSettingValues \/>\u000d\u000a      <\/InterfaceDetails>\u000d\u000a      <ProtocolDetails>\u000d\u000a        <ProtocolDetails>\u000d\u000a          <ProtocolInstanceName>SIM1<\/ProtocolInstanceName>\u000d\u000a          <ProtocolType>Simulation<\/ProtocolType>\u000d\u000a          <ProtocolSettingsNames \/>\u000d\u000a          <ProtocolSettingValues \/>\u000d\u000a        <\/ProtocolDetails>\u000d\u000a        <ProtocolDetails>\u000d\u000a          <ProtocolInstanceName>SIM2<\/ProtocolInstanceName>\u000d\u000a          <ProtocolType>Simulation<\/ProtocolType>\u000d\u000a          <ProtocolSettingsNames \/>\u000d\u000a          <ProtocolSettingValues \/>\u000d\u000a        <\/ProtocolDetails>\u000d\u000a        <ProtocolDetails>\u000d\u000a          <ProtocolInstanceName>DIO1<\/ProtocolInstanceName>\u000d\u000a          <ProtocolType>DIO<\/ProtocolType>\u000d\u000a          <ProtocolSettingsNames \/>\u000d\u000a          <ProtocolSettingValues \/>\u000d\u000a        <\/ProtocolDetails>\u000d\u000a      <\/ProtocolDetails>\u000d\u000a    <\/InterfaceProtocolDetails>\u000d\u000a  <\/InterfaceProtocolConfigurations>\u000d\u000a  <RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>Control_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>Simulation1 - SIM1<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>Sensor_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>Simulation1 - SIM2<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>FIFO_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>Simulation1 - SIM1<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a  <\/RegisterMapping>\u000d\u000a  <DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>1<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_IO<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>2<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>CS<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>3<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>SDO<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>4<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>5<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_IO_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>6<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>CS_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>7<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>SDO_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>Simulation1 - DIO1<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>8<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a  <\/DIOMapping>\u000d\u000a<\/HardwareConfigurationSupport>"},"ActiveRegisterMap":{"FilePath":"C:\\Users\\Public\\Documents\\National Instruments\\Semi Device Control (64-bit)\\Examples\\LPS22HH using .NET APIs\\InstrumentStudio project\\register-map-LPS22HH.solireg","RegisterMapName":"register-map-LPS22HH","RegisterMapVersion":null},"ScriptFolderLocation":"C:\\Users\\Public\\Documents\\National Instruments\\Semi Device Control (64-bit)\\Examples\\LPS22HH using .NET APIs\\InstrumentStudio project\\Scripts"}
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/conf/LPS22HH I3C.sdconfig sha256=89a04e9e2cb169aeda99acfcc1cf1f41710db902c91aeda59379c9f59de08212 bytes=7486 -->
## FILE: examples/conf/LPS22HH I3C.sdconfig

- repository: `ni/nisemi-python`
- source_path: `examples/conf/LPS22HH I3C.sdconfig`
- sha256: `89a04e9e2cb169aeda99acfcc1cf1f41710db902c91aeda59379c9f59de08212`
- bytes: 7486

````text
{"ActiveHardwareConfig":{"ConfigName":"LPS22HH I3C","ConfigString":"<?xml version=\"1.0\" encoding=\"utf-16\"?>\u000d\u000a<HardwareConfigurationSupport xmlns:xsd=\"http:\/\/www.w3.org\/2001\/XMLSchema\" xmlns:xsi=\"http:\/\/www.w3.org\/2001\/XMLSchema-instance\">\u000d\u000a  <IsOnline>true<\/IsOnline>\u000d\u000a  <InterfaceProtocolConfigurations>\u000d\u000a    <InterfaceProtocolDetails>\u000d\u000a      <InterfaceDetails>\u000d\u000a        <InterfaceInstanceName>NI 657x<\/InterfaceInstanceName>\u000d\u000a        <InterfaceType>NI PXIe657x<\/InterfaceType>\u000d\u000a        <InterfaceSettingNames>\u000d\u000a          <string>Pattern Project<\/string>\u000d\u000a          <string>Pattern Project File<\/string>\u000d\u000a          <string>Pinmap Name<\/string>\u000d\u000a          <string>Resource Name<\/string>\u000d\u000a          <string>Simulate<\/string>\u000d\u000a          <string>Reset Instrument<\/string>\u000d\u000a          <string>Event 0: <\/string>\u000d\u000a          <string>Event 1: <\/string>\u000d\u000a          <string>Event 2: <\/string>\u000d\u000a          <string>Event 3: <\/string>\u000d\u000a        <\/InterfaceSettingNames>\u000d\u000a        <InterfaceSettingValues>\u000d\u000a          <string>Custom<\/string>\u000d\u000a          <string>C:\\Users\\Public\\Documents\\National Instruments\\Semi Device Control (64-bit)\\Examples\\LPS22HH with Protocol APIs\\LPS22HH with NI 657x I3C\\InstrumentStudio project\\Pattern Project\\LPS22HH I3C.digiproj<\/string>\u000d\u000a          <string>PinMap<\/string>\u000d\u000a          <string>NI6570<\/string>\u000d\u000a          <string \/>\u000d\u000a          <string>False<\/string>\u000d\u000a          <string>None<\/string>\u000d\u000a          <string>None<\/string>\u000d\u000a          <string>None<\/string>\u000d\u000a          <string>None<\/string>\u000d\u000a        <\/InterfaceSettingValues>\u000d\u000a      <\/InterfaceDetails>\u000d\u000a      <ProtocolDetails>\u000d\u000a        <ProtocolDetails>\u000d\u000a          <ProtocolInstanceName>I3C<\/ProtocolInstanceName>\u000d\u000a          <ProtocolType>I3C Master<\/ProtocolType>\u000d\u000a          <functionCategory>I3C Master<\/functionCategory>\u000d\u000a          <ProtocolSettingsNames>\u000d\u000a            <string>Pin Group<\/string>\u000d\u000a            <string>Data Pin<\/string>\u000d\u000a            <string>Bus<\/string>\u000d\u000a            <string>Timing File Name<\/string>\u000d\u000a            <string>Levels File Name<\/string>\u000d\u000a            <string>Clock Rate (kHz)<\/string>\u000d\u000a            <string>Slave Address 0x<\/string>\u000d\u000a            <string>Bus State<\/string>\u000d\u000a            <string>Image<\/string>\u000d\u000a          <\/ProtocolSettingsNames>\u000d\u000a          <ProtocolSettingValues>\u000d\u000a            <string>I3C<\/string>\u000d\u000a            <string>SDA_I3C<\/string>\u000d\u000a            <string>0<\/string>\u000d\u000a            <string>I3C Timeset<\/string>\u000d\u000a            <string>PinLevels<\/string>\u000d\u000a            <string>100<\/string>\u000d\u000a            <string>5C<\/string>\u000d\u000a            <string>Legacy I2C<\/string>\u000d\u000a            <string>C:\\Program Files\\National Instruments\\Semi Device Control\\Components\\Hardware Types\\Images\\NIDigitalI3C.LegacyI2C.png<\/string>\u000d\u000a          <\/ProtocolSettingValues>\u000d\u000a        <\/ProtocolDetails>\u000d\u000a        <ProtocolDetails>\u000d\u000a          <ProtocolInstanceName>DIO<\/ProtocolInstanceName>\u000d\u000a          <ProtocolType>DIO<\/ProtocolType>\u000d\u000a          <functionCategory>DIO<\/functionCategory>\u000d\u000a          <ProtocolSettingsNames>\u000d\u000a            <string>Levels File Name<\/string>\u000d\u000a          <\/ProtocolSettingsNames>\u000d\u000a          <ProtocolSettingValues>\u000d\u000a            <string>PinLevels<\/string>\u000d\u000a          <\/ProtocolSettingValues>\u000d\u000a        <\/ProtocolDetails>\u000d\u000a      <\/ProtocolDetails>\u000d\u000a    <\/InterfaceProtocolDetails>\u000d\u000a  <\/InterfaceProtocolConfigurations>\u000d\u000a  <RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>Control_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>NI 657x - I3C<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>Sensor_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>NI 657x - I3C<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a    <RegisterMapping>\u000d\u000a      <IPBlockName>LPS22HH<\/IPBlockName>\u000d\u000a      <RegisterGroupName>FIFO_Register<\/RegisterGroupName>\u000d\u000a      <InterfaceProtocolMapping>NI 657x - I3C<\/InterfaceProtocolMapping>\u000d\u000a    <\/RegisterMapping>\u000d\u000a  <\/RegisterMapping>\u000d\u000a  <DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>16<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_IO<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>23<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>CS<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>19<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>SDO<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>20<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>16<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>Vdd_IO_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>23<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>CS_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>19<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a    <DIOMapping>\u000d\u000a      <DIOName>SDO_LB<\/DIOName>\u000d\u000a      <InterfaceDIOMapping>NI 657x - DIO<\/InterfaceDIOMapping>\u000d\u000a      <ChannelNumber>20<\/ChannelNumber>\u000d\u000a    <\/DIOMapping>\u000d\u000a  <\/DIOMapping>\u000d\u000a<\/HardwareConfigurationSupport>"},"ActiveRegisterMap":{"FilePath":"C:\\Users\\Public\\Documents\\National Instruments\\Semi Device Control (64-bit)\\Examples\\LPS22HH with Protocol APIs\\LPS22HH with NI 657x I3C\\InstrumentStudio project\\register-map-LPS22HH.solireg","RegisterMapName":"register-map-LPS22HH","RegisterMapVersion":null},"ScriptFolderLocation":"C:\\Users\\Public\\Documents\\National Instruments\\Semi Device Control (64-bit)\\Examples\\LPS22HH with Protocol APIs\\LPS22HH with NI 657x I3C\\InstrumentStudio project\\Scripts"}
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/conf/Scripts/PowerDownInI2C.sdcscript sha256=4f87b77508ccb4f8b97a4bdd6f6f1f5da4953912a803deebc8c2418a33bb40f4 bytes=54 -->
## FILE: examples/conf/Scripts/PowerDownInI2C.sdcscript

- repository: `ni/nisemi-python`
- source_path: `examples/conf/Scripts/PowerDownInI2C.sdcscript`
- sha256: `4f87b77508ccb4f8b97a4bdd6f6f1f5da4953912a803deebc8c2418a33bb40f4`
- bytes: 54

````text
writedio Vdd_IO Low
writedio Vdd Low
writedio CS Low
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/conf/Scripts/PowerUpInI2C.sdcscript sha256=dde8dd3fa4d8dc15f917beecb7f1de7a27b279dbdb4219d51572609b2cedb67a bytes=75 -->
## FILE: examples/conf/Scripts/PowerUpInI2C.sdcscript

- repository: `ni/nisemi-python`
- source_path: `examples/conf/Scripts/PowerUpInI2C.sdcscript`
- sha256: `dde8dd3fa4d8dc15f917beecb7f1de7a27b279dbdb4219d51572609b2cedb67a`
- bytes: 75

````text
writedio Vdd High
writedio Vdd_IO High
writedio CS High
writedio SDO Low
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/dut_communication_using_semi_device_control.py sha256=8da3c1c04b81804ca6e2598c3264cfbef4feec6af655a3ac916c5f0d6cdbac60 bytes=2831 -->
## FILE: examples/dut_communication_using_semi_device_control.py

- repository: `ni/nisemi-python`
- source_path: `examples/dut_communication_using_semi_device_control.py`
- sha256: `8da3c1c04b81804ca6e2598c3264cfbef4feec6af655a3ac916c5f0d6cdbac60`
- bytes: 2831

````python
"""Overview:.
 
Demonstrates how to use the Semi Device Control APIs to 
establish communication sequence with the DUT.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration
"""
# flake8: noqa
import os
import sys
import time

import nisdc_device_elements

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402


# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "isconfig.sdconfig"
)


# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    # Using the DIO APIs to control Board/Device Pins
    """Pin State corresponding int values. 2-Terminate, 1-High, 0-Low."""

    semi_device_control.write_pin_state("Vdd", 1)
    semi_device_control.write_pin_state("Vdd_IO", 1)
    semi_device_control.write_pin_state("CS", 1)
    semi_device_control.write_pin_state("SDO", 0)

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the Write Register APIs to burst the register data to the device
    # Using the Read Register APIs to read the register data from the device
    for i in range(25):
        semi_device_control.write_register_by_name_device(
            nisdc_device_elements.Register.LPS22HH.Control_Register.THS_P_H, i
        )

        reg_data = semi_device_control.read_register_by_name_device(
            nisdc_device_elements.Register.LPS22HH.Control_Register.THS_P_H
        )

        print(hex(reg_data))
        time.sleep(0.5)

    semi_device_control.write_pin_state("Vdd_IO", 0)
    semi_device_control.write_pin_state("Vdd", 0)

except Exception as e:
    print("Exception occurred: {}".format(e))
    raise e

# Stop the Hardware sessions that are previously initialized during the Start
# operation, and closing the Device Control session using the destroy API
finally:
    try:
        semi_device_control.stop()
        semi_device_control.destroy()

    except Exception as e:
        print("Exception during close: {}".format(e))
        raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/dut_communication_using_semi_device_control_nidigital.py sha256=c5ee915f0ca17c05e079853dd3acc07a48fedf0915133275e726e365bfef4dfb bytes=4227 -->
## FILE: examples/dut_communication_using_semi_device_control_nidigital.py

- repository: `ni/nisemi-python`
- source_path: `examples/dut_communication_using_semi_device_control_nidigital.py`
- sha256: `c5ee915f0ca17c05e079853dd3acc07a48fedf0915133275e726e365bfef4dfb`
- bytes: 4227

````python
"""Overview:.

Demonstrates how to use the NI Digital Instance through
Semi Device Control APIs to establish communication sequence with the DUT.

Requirement: Python full development system.

Instructions:.
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.
"""
# flake8: noqa
import os
import sys
import time
import grpc

import nidigital

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "LPS22HH I3C.sdconfig"
)

#Name of the interface to fetch details
interface_name = "NI 657x"

# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None
nidigital_session = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    # Attach to the existing 657x gRPC session.
    # Get the resource name of the instrument session for NI 657x device.
    session_options = semi_device_control.get_session_options(interface_name)
    grpc_option = nidigital.GrpcSessionOptions(
        grpc_channel = session_options.grpc_channel,
        session_name = session_options.session_name,
        initialization_behavior = nidigital.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION)
    
    # get the existing 657x instrument session.
    nidigital_session = nidigital.Session(
        resource_name = session_options.resource_name,
        grpc_options = grpc_option)

    # Using the NI Digital DIO APIs to control Board/Device Pins
    pinset = nidigital_session.channels["3"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["4"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["7"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["0"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the Write Register APIs to burst the register data to the device
    # Using the Read Register APIs to read the register data from the device
    for i in range(25):
        semi_device_control.write_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H", i
        )

        reg_data = semi_device_control.read_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H"
        )

        print(hex(reg_data))
        time.sleep(0.5)

    pinset = nidigital_session.channels["4"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

    pinset = nidigital_session.channels["3"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

except Exception as e:
    print("Exception occurred: {}".format(e))
    raise e

# Stop the Hardware sessions that are previously initialized during the Start
# operation, and closing the Device Control session using the destroy API
finally:
    try:
        semi_device_control.stop()
        semi_device_control.destroy()

    except Exception as e:
        print("Exception during close: {}".format(e))
        raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/dut_communication_using_semi_device_control_scripts.py sha256=8f23b50415b0146de94547ebd90858702a8c5f39b277887c2851477020553a07 bytes=2534 -->
## FILE: examples/dut_communication_using_semi_device_control_scripts.py

- repository: `ni/nisemi-python`
- source_path: `examples/dut_communication_using_semi_device_control_scripts.py`
- sha256: `8f23b50415b0146de94547ebd90858702a8c5f39b277887c2851477020553a07`
- bytes: 2534

````python
"""Overview:.

Demonstrates how to use the Semi Device Control APIs to establish
communication sequence with the DUT using scripts.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.
"""
# flake8: noqa
import os
import sys
import time

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "isconfig.sdconfig"
)


# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    # Using the Script APIs to control Board/Device Pins

    semi_device_control.execute_script("PowerUpInI2C")

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the Write Register APIs to burst the register data to the device
    # Using the Read Register APIs to read the register data from the device
    for i in range(25):
        semi_device_control.write_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H", i
        )

        reg_data = semi_device_control.read_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H"
        )

        print(hex(reg_data))
        time.sleep(0.5)

    # Using the Script APIs to power down Board

    semi_device_control.execute_script("PowerDownInI2C")

except Exception as e:
    print("Exception occurred: {}".format(e))
    raise e

# Stop the Hardware sessions that are previously initialized during the Start
# operation, and closing the Device Control session using the destroy API
finally:
    try:
        semi_device_control.stop()
        semi_device_control.destroy()

    except Exception as e:
        print("Exception during close: {}".format(e))
        raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/dut_i3c_communication_using_semi_device_control.py sha256=f3a319c5d5cdf70967aa6fd338470dd246cebfc3745fe580d1fbb2e9e6085d74 bytes=3938 -->
## FILE: examples/dut_i3c_communication_using_semi_device_control.py

- repository: `ni/nisemi-python`
- source_path: `examples/dut_i3c_communication_using_semi_device_control.py`
- sha256: `f3a319c5d5cdf70967aa6fd338470dd246cebfc3745fe580d1fbb2e9e6085d74`
- bytes: 3938

````python
"""Overview:.

Demonstrates how to use the Semi Device Control APIs to establish
communication sequence with the DUT using I3C protocol.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.
"""
# flake8: noqa
import os
import sys
import time

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402
from nisdc_i3c.nisdc_i3c import SemiDeviceControlI3CSession  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "LPS22HH I3C.sdconfig"
)


# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None
i3c_session = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    interface_name = "NI 657x"
    protocol_name = "I3C"
    # Create I3C Session
    i3c_session = SemiDeviceControlI3CSession(
        semi_device_control, interface_name, protocol_name
    )

    # Using the Script APIs to control Board/Device Pins

    semi_device_control.write_pin_state("Vdd", 1)
    semi_device_control.write_pin_state("Vdd_IO", 1)
    semi_device_control.write_pin_state("CS", 1)
    semi_device_control.write_pin_state("SDO", 0)

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the write register and read register APIs to perform device operation in I2C mode
    semi_device_control.write_register_by_name_device(
        "LPS22HH-Control_Register-THS_P_H", 10
    )
    reg_data = semi_device_control.read_register_by_name_device(
        "LPS22HH-Control_Register-THS_P_H"
    )
    print(hex(reg_data))

    """CCC Types corresponding int values. 1=Direct ,0=Broadcast."""

    SETDASA_command = 135
    GETPID_command = 141
    RSTDAA_command = 6

    # SETDASA command in Dynamic Addressing mode
    i3c_session.execute_dynamic_addressing_ccc(1, SETDASA_command, 37)

    # GETPID command in SDR CCC mode
    device_id = i3c_session.execute_sdr_ccc_read(1, GETPID_command)
    data_as_hex = []
    for data in device_id:
        data_as_hex.append(hex(data))
    print(f"The device PID value is {','.join(data_as_hex)}")

    # Using the write register and read register APIs to perform device operation in I3C mode
    semi_device_control.write_register_by_name_device(
        "LPS22HH-Control_Register-THS_P_H", 15
    )
    reg_data = semi_device_control.read_register_by_name_device(
        "LPS22HH-Control_Register-THS_P_H"
    )
    print(hex(reg_data))
    time.sleep(0.5)

    # RSTDAA command that resets the DUT in Dynamic Addressing mode
    i3c_session.execute_dynamic_addressing_ccc(0, RSTDAA_command)

    semi_device_control.write_pin_state("Vdd_IO", 0)
    semi_device_control.write_pin_state("Vdd", 0)
    semi_device_control.write_pin_state("CS", 0)

except Exception as e:
    print("Exception occurred: {}".format(e))
    raise e

# Stop the Hardware sessions that are previously initialized during the Start
# operation, and closing the Device Control session using the destroy API
finally:
    try:
        semi_device_control.stop()
        semi_device_control.destroy()

    except Exception as e:
        print("Exception during close: {}".format(e))
        raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/generate_device_elements_using_semi_device_control.py sha256=1a98768ac8f22aed21b9635e5ffec28c265f3023bde2d7bf2775278c0a64031e bytes=1420 -->
## FILE: examples/generate_device_elements_using_semi_device_control.py

- repository: `ni/nisemi-python`
- source_path: `examples/generate_device_elements_using_semi_device_control.py`
- sha256: `1a98768ac8f22aed21b9635e5ffec28c265f3023bde2d7bf2775278c0a64031e`
- bytes: 1420

````python
"""Overview:.

Demonstrates how to use the "generate_device_elements" API to generate
the class file that contains all the device elements.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. Use the python file generated to easily access the register and field names.
"""
# flake8: noqa
import os
import sys


# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "isconfig.sdconfig"
)

# Instantiate the 'Device Control session'using the Instantiate API.
semi_device_control = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)

    # Generates the nisdc_device_elements.py with register names and bitfield names
    path = semi_device_control.generate_device_elements()
    print("The generated file is located at ", path)

    semi_device_control.destroy()

except Exception as e:
    print("Exception during close: {}".format(e))
    raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=examples/nisdc_device_elements.py sha256=479d4537abb30dfa9aa183e1a485bd9da66d4e68eabae9d4e05f351b75f5e1b8 bytes=6682 -->
## FILE: examples/nisdc_device_elements.py

- repository: `ni/nisemi-python`
- source_path: `examples/nisdc_device_elements.py`
- sha256: `479d4537abb30dfa9aa183e1a485bd9da66d4e68eabae9d4e05f351b75f5e1b8`
- bytes: 6682

````python
"""This file contains registers and field info."""
# flake8: noqa
class Register:
    """This class contains all register info."""
    class LPS22HH:
        """This class contains LPS22HH registers info."""
        class Control_Register:
            """"This class contains different registers info present in LPS22H."""
            INTERRUPT_CFG = "LPS22HH-Control_Register-INTERRUPT_CFG"
            THS_P_L = "LPS22HH-Control_Register-THS_P_L"
            THS_P_H = "LPS22HH-Control_Register-THS_P_H"
            IF_CTRL = "LPS22HH-Control_Register-IF_CTRL"
            WHO_AM_I = "LPS22HH-Control_Register-WHO_AM_I"
            CTRL_REG1 = "LPS22HH-Control_Register-CTRL_REG1"
            CTRL_REG2 = "LPS22HH-Control_Register-CTRL_REG2"
            CTRL_REG3 = "LPS22HH-Control_Register-CTRL_REG3"
            FIFO_CTRL = "LPS22HH-Control_Register-FIFO_CTRL"
            FIFO_WTM = "LPS22HH-Control_Register-FIFO_WTM"
            REF_P_L = "LPS22HH-Control_Register-REF_P_L"
            REF_P_H = "LPS22HH-Control_Register-REF_P_H"
            RESERVED = "LPS22HH-Control_Register-RESERVED"
            RPDS_L = "LPS22HH-Control_Register-RPDS_L"
            RPDS_H = "LPS22HH-Control_Register-RPDS_H"

        class Sensor_Register:
            """This class contains sensor registers info."""
            INT_SOURCE = "LPS22HH-Sensor_Register-INT_SOURCE"
            FIFO_STATUS1 = "LPS22HH-Sensor_Register-FIFO_STATUS1"
            FIFO_STATUS2 = "LPS22HH-Sensor_Register-FIFO_STATUS2"
            STATUS = "LPS22HH-Sensor_Register-STATUS"
            PRESS_OUT_XL = "LPS22HH-Sensor_Register-PRESS_OUT_XL"
            PRESS_OUT_L = "LPS22HH-Sensor_Register-PRESS_OUT_L"
            PRESS_OUT_H = "LPS22HH-Sensor_Register-PRESS_OUT_H"
            TEMP_OUT_L = "LPS22HH-Sensor_Register-TEMP_OUT_L"
            TEMP_OUT_H = "LPS22HH-Sensor_Register-TEMP_OUT_H"

        class FIFO_Register:
            """This class contains FIFO registers info."""
            FIFO_DATA_OUT_PRESS_XL = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_XL"
            FIFO_DATA_OUT_PRESS_L = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_L"
            FIFO_DATA_OUT_PRESS_H = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_PRESS_H"
            FIFO_DATA_OUT_TEMP_L = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_TEMP_L"
            FIFO_DATA_OUT_TEMP_H = "LPS22HH-FIFO_Register-FIFO_DATA_OUT_TEMP_H"


class Field:
    """This class contains field info."""
    class LPS22HH:
        """This class contains LPS22HH field info."""
        class Control_Register:
            """This class contains different field info in LPS22HH register."""
            AUTOREFP = "LPS22HH-Control_Register-AUTOREFP"
            RESET_ARP = "LPS22HH-Control_Register-RESET_ARP"
            AUTOZERO = "LPS22HH-Control_Register-AUTOZERO"
            RESET_AZ = "LPS22HH-Control_Register-RESET_AZ"
            DIFF_EN = "LPS22HH-Control_Register-DIFF_EN"
            LIR = "LPS22HH-Control_Register-LIR"
            PLE = "LPS22HH-Control_Register-PLE"
            PHE = "LPS22HH-Control_Register-PHE"
            THS = "LPS22HH-Control_Register-THS"
            INT_EN_I3C = "LPS22HH-Control_Register-INT_EN_I3C"
            SDA_PU_EN = "LPS22HH-Control_Register-SDA_PU_EN"
            SDO_PU_EN = "LPS22HH-Control_Register-SDO_PU_EN"
            PD_DIS_INT1 = "LPS22HH-Control_Register-PD_DIS_INT1"
            I3C_DISABLE = "LPS22HH-Control_Register-I3C_DISABLE"
            I2C_DISABLE = "LPS22HH-Control_Register-I2C_DISABLE"
            WHO_AM_I_BF = "LPS22HH-Control_Register-WHO_AM_I_BF"
            ODR = "LPS22HH-Control_Register-ODR"
            EN_LPFP = "LPS22HH-Control_Register-EN_LPFP"
            LPFP_CFG = "LPS22HH-Control_Register-LPFP_CFG"
            BDU = "LPS22HH-Control_Register-BDU"
            SIM = "LPS22HH-Control_Register-SIM"
            BOOT = "LPS22HH-Control_Register-BOOT"
            INT_H_L = "LPS22HH-Control_Register-INT_H_L"
            PP_OD = "LPS22HH-Control_Register-PP_OD"
            IF_ADD_INC = "LPS22HH-Control_Register-IF_ADD_INC"
            SWRESET = "LPS22HH-Control_Register-SWRESET"
            LOW_NOISE_EN = "LPS22HH-Control_Register-LOW_NOISE_EN"
            ONE_SHOT = "LPS22HH-Control_Register-ONE_SHOT"
            INT_F_FULL = "LPS22HH-Control_Register-INT_F_FULL"
            INT_F_WTM = "LPS22HH-Control_Register-INT_F_WTM"
            INT_F_OVR = "LPS22HH-Control_Register-INT_F_OVR"
            DRDY = "LPS22HH-Control_Register-DRDY"
            INT_S = "LPS22HH-Control_Register-INT_S"
            STOP_ON_WTM = "LPS22HH-Control_Register-STOP_ON_WTM"
            TRIG_MODES = "LPS22HH-Control_Register-TRIG_MODES"
            F_MODE = "LPS22HH-Control_Register-F_MODE"
            WTM = "LPS22HH-Control_Register-WTM"
            REFL = "LPS22HH-Control_Register-REFL"
            RPDS = "LPS22HH-Control_Register-RPDS"
            RESERVED_1 = "LPS22HH-Control_Register-RESERVED_1"
            RESERVED_2 = "LPS22HH-Control_Register-RESERVED_2"
            RESERVED_3 = "LPS22HH-Control_Register-RESERVED_3"
            RESERVED_4 = "LPS22HH-Control_Register-RESERVED_4"
            RESERVED_5 = "LPS22HH-Control_Register-RESERVED_5"
            RESERVED_6 = "LPS22HH-Control_Register-RESERVED_6"
            RESERVED_7 = "LPS22HH-Control_Register-RESERVED_7"
            RESERVED_8 = "LPS22HH-Control_Register-RESERVED_8"

        class Sensor_Register:
            """This class contains sensor register pin info."""
            BOOT_ON = "LPS22HH-Sensor_Register-BOOT_ON"
            IA = "LPS22HH-Sensor_Register-IA"
            PL = "LPS22HH-Sensor_Register-PL"
            PH = "LPS22HH-Sensor_Register-PH"
            RESERVED_9 = "LPS22HH-Sensor_Register-RESERVED_9"
            FSS = "LPS22HH-Sensor_Register-FSS"
            FIFO_WTM_IA = "LPS22HH-Sensor_Register-FIFO_WTM_IA"
            FIFO_OVR_IA = "LPS22HH-Sensor_Register-FIFO_OVR_IA"
            FIFO_FULL_IA = "LPS22HH-Sensor_Register-FIFO_FULL_IA"
            RESERVED_10 = "LPS22HH-Sensor_Register-RESERVED_10"
            T_OR = "LPS22HH-Sensor_Register-T_OR"
            P_OR = "LPS22HH-Sensor_Register-P_OR"
            T_DA = "LPS22HH-Sensor_Register-T_DA"
            P_DA = "LPS22HH-Sensor_Register-P_DA"
            RESERVED_11 = "LPS22HH-Sensor_Register-RESERVED_11"
            POUT = "LPS22HH-Sensor_Register-POUT"
            TOUT = "LPS22HH-Sensor_Register-TOUT"

        class FIFO_Register:
            """"This class contains FIFO registers pin info."""
            FIFO_P = "LPS22HH-FIFO_Register-FIFO_P"
            FIFO_T = "LPS22HH-FIFO_Register-FIFO_T"
````

<!--NI_OSS_SOURCE repo=nisemi-python path=LICENSE sha256=dc3be6f9a41cc094419bf22fda26abba350bedd49238727e156a8d297adce9f7 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/nisemi-python`
- source_path: `LICENSE`
- sha256: `dc3be6f9a41cc094419bf22fda26abba350bedd49238727e156a8d297adce9f7`
- bytes: 1091

````text
Copyright (c) 2021, National Instruments Corp.

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

<!--NI_OSS_SOURCE repo=nisemi-python path=nisdc/__init__.py sha256=60ec8e8253622348989e1df7a67bcc0b68467d3634ddedb3f276487394b2638b bytes=31 -->
## FILE: nisdc/__init__.py

- repository: `ni/nisemi-python`
- source_path: `nisdc/__init__.py`
- sha256: `60ec8e8253622348989e1df7a67bcc0b68467d3634ddedb3f276487394b2638b`
- bytes: 31

````python
""""This file is for init."""
````

<!--NI_OSS_SOURCE repo=nisemi-python path=nisdc/nisemidevicecontrol.py sha256=b5200f607394580810b5e286a429e884b18b9ceb18aa9bfaae3f44c35e976efe bytes=41722 -->
## FILE: nisdc/nisemidevicecontrol.py

- repository: `ni/nisemi-python`
- source_path: `nisdc/nisemidevicecontrol.py`
- sha256: `b5200f607394580810b5e286a429e884b18b9ceb18aa9bfaae3f44c35e976efe`
- bytes: 41722

````python
"""This file is used for Semi Device Control API."""
import os
import sys
import grpc

import clr
# flake8: noqa
device_control_path = (
    "C:\\Program Files\\National Instruments\\" + "Semi Device Control")

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)

clr.AddReference("SemiconductorDeviceControl")
from SemiconductorDeviceControl import SemiDeviceControlMain  # noqa:E402
from SemiconductorDeviceControl import PinState  # noqa:E402

def generate_class_string(element_type, device_element_list): 
    """This method generates the class string to be written to the auto generated file."""
    """Arguments: element_type {string},device_element_list {list}"""
    """Return: string - The entire string generated for the class """
    ipblock = ""
    registergroup = ""
    class_content = ""
    class_string = "class "
    hyphen_delimiter = "-"

    class_content += class_string + element_type + "():\n"
    for device_element in device_element_list:
        device_element_details = device_element.split(hyphen_delimiter)
        current_ipblock = device_element_details[0]
        current_register_group = device_element_details[1]
        current_device_element = device_element_details[2]

        if current_ipblock != ipblock:
            class_content += str.format(
                "\t" + class_string + "{}():\n", current_ipblock
            )
            ipblock = current_ipblock

        if current_register_group != registergroup:
            class_content += str.format(
                "\t\t" + class_string + "{}():\n", current_register_group
            )
            registergroup = current_register_group

        class_content += str.format(
            '\t\t\t{} = "{}"\n', current_device_element, device_element
        )
    class_content += "\n\n"
    return class_content

class GrpcSessionOptions:
    def __init__(self, session_name, resource_name, grpc_channel) :
        self.session_name = session_name
        self.resource_name = resource_name
        self.grpc_channel = grpc_channel

class SemiconductorDeviceControl:
    """This class is used for Instrument Studio export configuration."""

    def __init__(self, isconfigpath=None):
        """Create and return device control session using Instrument Studio export configuration.

        IS export configuration contains the register map and hardware configuration
        for Device Control.

        Args:
            isconfigpath : the isconfig path. if not specified, the device control session will not be created.
        """
        self.semidevicecontrol_main = None
        self.semidevicecontrol_session = None

        try:
            self.semidevicecontrol_main = SemiDeviceControlMain()
            if isconfigpath:
                self.semidevicecontrol_session = (
                    self.semidevicecontrol_main.CreateSemiDeviceControlSession(isconfigpath)
                )

        except Exception as e:
            print("Exception in accessing conf: {}".format(e))
            raise e
        
    def attach_to_existing_session(self):
        """Returns the instantiated device control session if any
        """
        try:
            self.semidevicecontrol_session = self.semidevicecontrol_main.AttachToExistingSession()
            return self
        
        except Exception as e:
            print("Error occurred while attaching to the instantiated semi device control session: {}".foramat(e))
            raise e

    def start(self):
        """Description:.

        Starts the Instrument/Hardware sessions configured for the device control
        through the IS export configuration.
        """
        try:
            self.semidevicecontrol_session.Start()

        except Exception as e:
            print("Exception in start(): {}".format(e))
            raise e

    def stop(self):
        """Stops the Instrument/Hardware sessions configured for the device control."""
        try:
            self.semidevicecontrol_session.Stop()

        except Exception as e:
            print("Exception is stop(): {}".format(e))
            raise e

    def destroy(self):
        """Destroys the device control session.

        Deallocates the reserved reference and data in memory.
        """
        try:
            self.semidevicecontrol_main.DestroySemiDeviceControlSession(
                self.semidevicecontrol_session
            )

        except Exception as e:
            print("Exception is destroy engine: {}".format(e))
            raise e

    # ---------------------------- Register Device ----------------------------

    def write_register_by_name_device(self, register_uid, register_data):
        """Writes the data to the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: string register uid
            register_data: int register data

        """
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Device(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_device(
        self, register_uid_list, register_data_list
    ):
        """Writes data to multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element,the corresponding element from the data array will be applied.

        Args:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Device(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_device(
        self, ip_block_name, register_address, register_data
    ):
        """Writes the data to the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string} ip black name
            register_address: {int} register address
            register_data: {int} register data
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Device(
                ip_block_name, register_address, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_device(
        self, ip_block_name_list, register_address_list, register_data_list
    ):
        """Write data to multiple registers on the device, using the register address.

        And IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding element
        from the data array will be applied.

        Args:
            ip_block_name_list: list of string
            register_address_list: list of int
            register_data_list: list of int
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Device(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_custom_register_by_address_device(
        self,
        register_address,
        address_size,
        register_data,
        register_size,
        interface_name,
        protocol_name,
    ):
        """Writes the data using the register address and register size.

           To the device with the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Args:
            register_address: {int}
            address_size: {int}
            register_data: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}
        """
        try:
            self.semidevicecontrol_session.WriteCustomRegisterByAddress_Device(
                register_address,
                address_size,
                register_data,
                register_size,
                interface_name,
                protocol_name,
            )
        except Exception as e:
            print("")
            raise e

    def read_register_by_name_device(self, register_uid):
        """Reads the data from the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid : {string}

        Returns:
            register_data : {int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByName_Device(
                register_uid
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_device(self, register_uid_list):
        """Reads data from multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Args:
            register_uid_list : {list of string}

        Returns:
            register_data_list : {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Device(
                    register_uid_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_device(self, ip_block_name, register_address):
        """Reads the data from the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name : {string}
            register_address : {int}

        Returns:
            register_data : {int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByAddress_Device(
                ip_block_name, register_address
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_device(
        self, ip_block_name_list, register_address_list
    ):
        """Reads data from multiple registers on the device.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list : {list of string}
            register_address_list : {list of int}

        Returns:
            register_data_list : {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress_Device(
                    ip_block_name_list, register_address_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_custom_register_by_address_device(
        self,
        register_address,
        address_size,
        register_size,
        interface_name,
        protocol_name,
    ):
        """Reads the data using the register address and register size from the device.

        With the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Arguments:
            register_address: {int}
            address_size: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}

        Returns:
            register_data: {int}
        """
        try:
            register_data = (
                self.semidevicecontrol_session.ReadCustomRegisterByAddress_Device(
                    register_address,
                    address_size,
                    register_size,
                    interface_name,
                    protocol_name,
                )
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def get_register_addresses(self):
        """Gets the list of unique ID and Register addresses.

        Returns:
            register_uid_list: {list of string}
            register_address_list: {list of int
        """
        try:
            register_details = self.semidevicecontrol_session.GetRegisterAddresses()
            register_uid_list = list(register.UniqueID for register in register_details)
            register_address_list = list(
                register.Address for register in register_details
            )
            return register_uid_list, register_address_list

        except Exception as e:
            raise e

    # --------------------------- Register Device ---------------------------

    # ----------------------------- Field Device -----------------------------
    def write_field_by_name_device(self, field_uid, field_data):
        """Writes the data to the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data :{int}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByName_Device(
                field_uid, field_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_device(self, field_uid_list, field_data_list):
        """Writes data to multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Device(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_device(self, field_uid, value_definition):
        """Write the data to the device using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Device(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_device(self, field_uid):
        """Reads the data from the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        """
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Device(
                field_uid
            )
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_device(self, field_uid_list):
        """Reads data from multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        """
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Device(
                    field_uid_list
                )
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    def get_field_definition_details(self, field_uid):
        """Gets the field display values, field values and field size for given unique ID.

        Arguments:
            field_uid: {string}

        Returns:
            field_display_values {list of string}
            field_values {list of int}
            field_size {int}
        """
        try:
            field_definition = self.semidevicecontrol_session.GetFieldDefinitionDetails(
                field_uid
            )
            return (
                list(field_definition.DisplayValues),
                list(field_definition.Values),
                field_definition.Size,
            )

        except Exception as e:
            raise e

    # ----------------------------- Field Device -----------------------------

    # ---------------------------- Register Cache ----------------------------
    def write_register_by_name_cache(self, register_uid, register_data):
        """Writes the data to the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}
            register_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Cache(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_cache(self, register_uid_list, register_data_list):
        """Writes data to multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.

        Array will be applied.

        Arguments:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Cache(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_cache(
        self, ip_block_name, register_address, register_data
    ):
        """Writes the data to the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Arguments:
            ip_block_name: {string}
            register_address: {int}
            register_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Cache(
                ip_block_name, register_address, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_cache(
        self, ip_block_name_list, register_address_list, register_data_list
    ):
        """Writes data to multiple registers on the cache.

        Using the register, address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Arguments:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Cache(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def read_register_by_name_cache(self, register_uid):
        """Reads the data from the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}

        Returns:
            register_data :{int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByName_Cache(
                register_uid
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_cache(self, register_uid_list):
        """Reads data from multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.
        array will be applied.

        Arguments:
            register_uid_list: {list of string}

        Returns:
            register_data_list: {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Cache(
                    register_uid_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_cache(self, ip_block_name, register_address):
        """Reads the data from the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string}
            register_address: {int}

        Returns:
            register_data :{int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByAddress_Cache(
                ip_block_name, register_address
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_cache(
        self, ip_block_name_list, register_address_list
    ):
        """Reads data from multiple registers on the cache.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}

        Returns:
            register_data_list: {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress(
                    ip_block_name_list, register_address_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    # ---------------------------- Register Cache ----------------------------

    # ----------------------------- Field Cache -----------------------------

    def write_field_by_name_cache(self, field_uid, field_data):
        """Writes the data to the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByName_Cache(field_uid, field_data)

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_cache(self, field_uid_list, field_data_list):
        """Writes data to multiple fields on the cache using the fields unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Cache(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_cache(self, field_uid, value_definition):
        """Writes the data to the cache using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Cache(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_cache(self, field_uid):
        """Read the data from the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        """
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Cache(field_uid)
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_cache(self, field_uid_list):
        """Reads data from multiple fields on the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        """
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Cache(
                    field_uid_list
                )
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    # ----------------------------- Field Cache -----------------------------

    # -------------------------------- Cache --------------------------------
    def write_from_cache_to_device(self):
        """Writes all the cache register data to the device, in the order.

        It is stored in the cache memory. The cache will be auto cleared.

        After this operation.
        """
        try:
            self.semidevicecontrol_session.WriteFromCacheToDevice()

        except Exception as e:
            print("Exception in writing software cache to hardware")
            raise e

    def clear_cache(self):
        """Clears all the cache register data from the device control session."""
        try:
            self.semidevicecontrol_session.ClearCache()

        except Exception as e:
            print("Exception in flush software cache")
            raise e

    # ------------------------------ DIO ------------------------------
    def read_pin_state(self, pin_name):
        """Reads the pin state (High / Low / Terminate) using the Pin name.

        Defined in the register map.

        Pin State corresponding int values.2-Terminate, 1=High, 0-Low.

        Args:
            pin_name: {string}

        Return:
            pin_state: {int}
        """
        try:
            pin_state = self.semidevicecontrol_session.ReadPinState(pin_name)
            return int(pin_state)

        except Exception as e:
            print("Exception occured at read pin state")
            raise e

    def write_pin_state(self, pin_name, pin_state):
        """Puts the pin to High / Low / Terminate state using the Pin name.

        defined in the register map.

        Args:
            pin_name: {string}
            pin_state: {int}

            Pin State corresponding int values.

            2-Terminate, 1=High, 0-Low.
        """
        try:
            self.semidevicecontrol_session.WritePinState(pin_name, PinState(pin_state))

        except Exception as e:
            print("Exception occured at write pin state")
            raise e

    # -------------------------------- SCRIPTS ------------------------------
    def execute_script(self, file_name, wait_until_complete=True):
        """Executes the script using the Script Name provided as a input.

        If a script is already running on the semi device control session.

        This API will throw error indicating that another script is running already.

        Using waitUntilScriptCompletion bool control, developer can configure.

        This API to run the script as a blocking call or run asynchronously.

        Args:
            file_name: {string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}
        """
        try:
            return self.semidevicecontrol_session.ExecuteScript(
                file_name, wait_until_complete
            )

        except Exception as e:
            print("Exception occured at execute script")
            raise e

    def execute_script_command(self, script_string, wait_until_complete=True):
        """Executes the Script String provided as the input to the API.

        If the Script String is invalid, error will be thrown, and execution will be skipped.
        If waitUntilComplete? is True, then the API will wait until the script is executed.
        Else the API will run the script asynchronously and stop.

        Args:
            script_string :{string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}.
        """
        try:
            return self.semidevicecontrol_session.ExecuteScriptCommand(
                script_string, wait_until_complete
            )

        except Exception as e:
            print("Exception occured at execute script command")
            raise e

    def abort_script(self):
        """Abort Script will abort the current running script on the semi device control session."""
        try:
            self.semidevicecontrol_session.AbortScript()

        except Exception as e:
            print("Exception occured at abort script")
            raise e

    # -------------------------------- UTILS --------------------------------
    def get_logs(self):
        """Get log details.

        Returns:
            logs {2d array of strings}
        """
        try:
            logs = self.semidevicecontrol_session.GetLogs()
            return logs

        except Exception as e:
            print("Exception occured at log function")
            raise e

    def reset_to_default_state(self):
        """Reset the device software register values and dio states to default."""
        try:
            self.semidevicecontrol_session.ResetToDefaultState()

        except Exception as e:
            print("Exception occured at reset to default state")
            raise e

    def get_script_names(self):
        """Gets the list of script file names available in the source folder location.

        Return:
            script_names {list of strings}
        """
        try:
            script_names = self.semidevicecontrol_session.GetScriptFileName()
            return script_names

        except Exception as e:
            print("Exception occured at get script names")
            raise e

    def get_protocol_dynamic_setting(self, interface_name, protocol_name, setting_name):
        """Gets the dynamic protocol setting value of the protocol setting.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}

        Return:
            setting_value {string}
        """
        try:
            return self.semidevicecontrol_session.GetProtocolDynamicSetting(
                interface_name, protocol_name, setting_name
            )

        except Exception as e:
            print("Exception occured at get protocol settings")
            raise e

    def set_protocol_dynamic_setting(
        self, interface_name, protocol_name, setting_name, setting_value
    ):
        """Updates the dynamic protocol settings of the protocol.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}
            setting_value: {string}
        """
        try:
            self.semidevicecontrol_session.SetProtocolDynamicSetting(
                interface_name, protocol_name, setting_name, setting_value
            )

        except Exception as e:
            print("Exception occured at update dynamic protocol settings")
            raise e

    def get_interface_dynamic_setting(self, interface_name, setting_name):
        """Gets the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}

        Return:
            setting_value: {string}
        """
        try:
            return self.semidevicecontrol_session.GetInterfaceDynamicSetting(
                interface_name, setting_name
            )

        except Exception as e:
            print("Exception occured at get interface settings")
            raise e

    def set_interface_dynamic_setting(
        self, interface_name, setting_name, setting_value
    ):
        """Updates the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}
            setting_value: {string}
        """
        try:
            self.semidevicecontrol_session.SetInterfaceDynamicSetting(
                interface_name, setting_name, setting_value
            )

        except Exception as e:
            print("Exception occured at update dynamic interface settings")
            raise e

    def get_instrument_session(self, interface_name):
        """Gets the session ID of the instrument.

        Return:
            int {session ID}
        """
        try:
            return self.semidevicecontrol_session.GetInterfaceSessionID(interface_name)

        except Exception as e:
            print("Exception occured at get instrument session")
            raise e
        
    def get_session_options(self, interface_name):
        """Gets the grpc options for the instrument session.
           Creates service server channel using the grpc options.

            Return:
                grpc_session_options {Object contains the session_name {string} and device_server_channel {grpc.Channel}}
        """

        try:
            grpc_session_options = self.semidevicecontrol_session.GetGrpcSessionOptions(interface_name)
            device_server_channel = grpc.insecure_channel(grpc_session_options.Address + ":" + str(grpc_session_options.Port))
            return GrpcSessionOptions(grpc_session_options.SessionName, grpc_session_options.ResourceName, device_server_channel)
        
        except Exception as e:
            print("Exception occured at get grpc session options")
            raise e

    def get_interface_details(self):
        """Gets the list of interface name and interface type.

        Return:
            interface_name_list {list of string}
            interface_type_list {list of string}
        """
        try:
            interface_details = self.semidevicecontrol_session.GetInterfaceDetails()
            interface_name_list = list(
                interface.Name for interface in interface_details
            )
            interface_type_list = list(
                interface.Type for interface in interface_details
            )
            return interface_name_list, interface_type_list

        except Exception as e:
            print("Exception occured at get interface details")
            raise e

    def get_script_string(self, script_name):
        """API provides the Script String and IsScriptFileValid status from Device Control session.

        For the given the Script Name input.

        Args:
            script_name: {string}

        Return:
            Tuple { bool - IsScriptValid, string - ScriptContent}
        """
        try:
            script_detail = self.semidevicecontrol_session.GetScriptString(script_name)
            return script_detail.IsScriptValid, script_detail.ScriptContent

        except Exception as e:
            print("Exception occured at get script string")
            raise e

    def generate_device_elements(self, directory=""):
        """This API generates a class file in the specified directory.

        That contains the register and field elements from the register map
        configured in the sdcconfig file.
        If the directory provided is empty, the file will be created in the working directory.

        Args:
            directory: {string}

        Return:
            string - The path where the file is created
        """
        try:
            if directory == "":
                directory = os.getcwd()
            elif not (os.path.exists(directory)):
                raise "Invalid path to generate the class file"
            directory += "\\nisdc_device_elements.py"
            device_state_keys = self.semidevicecontrol_session.GetDeviceStateKeys()

            with open(directory, "w+") as class_file:
                class_file.write(
                    generate_class_string(
                        "Register", list(device_state_keys.RegisterUIDs)
                    )
                )
                class_file.write(
                    generate_class_string("Field", list(device_state_keys.FieldUIDs))
                )
            return directory
        except Exception as e:
            print("Exception occured at generate device elements")
            raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=nisdc_i3c/__init__.py sha256=92f7164d23acca60b90717ec9c8e34c10f4a9a65feac093662d4eb176f07e3ef bytes=33 -->
## FILE: nisdc_i3c/__init__.py

- repository: `ni/nisemi-python`
- source_path: `nisdc_i3c/__init__.py`
- sha256: `92f7164d23acca60b90717ec9c8e34c10f4a9a65feac093662d4eb176f07e3ef`
- bytes: 33

````python
"""This is __init__.py file."""
````

<!--NI_OSS_SOURCE repo=nisemi-python path=nisdc_i3c/nisdc_i3c.py sha256=a85c9db4235803ea18b173ae926bb4f914e4ac35b77985603fa3358366bc63cb bytes=5599 -->
## FILE: nisdc_i3c/nisdc_i3c.py

- repository: `ni/nisemi-python`
- source_path: `nisdc_i3c/nisdc_i3c.py`
- sha256: `a85c9db4235803ea18b173ae926bb4f914e4ac35b77985603fa3358366bc63cb`
- bytes: 5599

````python
"""This file is used for Semi Device Control I3C API."""
import os
import sys

import clr

# flake8: noqa
device_control_path = "C:\\Program Files\\National Instruments\\Semi Device Control"

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)
clr.AddReference("SemiconductorDeviceControl.NIDigitalI3C.APISupport")

from SemiconductorDeviceControl.NIDigitalI3C.APISupport import (SemiconductorDeviceControlI3CSession,)  # noqa:E402

class SemiDeviceControlI3CSession:
    """"This class is used to create I3C session."""
    def __init__(self, semidevicecontrol_session, interface_name, protocol_name):
        """Creates and returns a I3C session using the Semi Device Control session.

        Args:
            semidevicecontrol_session: {Semi Device Control session object}
            interface_name: {string}
            protocol_name: {string}
        """
        self.i3c_session = None
        try:
            self.i3c_session = SemiconductorDeviceControlI3CSession(
                semidevicecontrol_session.semidevicecontrol_session,
                interface_name,
                protocol_name,
            )

        except Exception as e:
            print("Exception in accessing I3C Session: {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc(self, ccc_type, command_id, dynamic_address=-1):
        """Executes the CCC used for dynamic addressing based on the given inputs.
        
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values.1=Direct,0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}
        """
        try:
            self.i3c_session.ExecuteDynamicAddressingCCC(
                ccc_type, command_id, dynamic_address
            )

        except Exception as e:
            print("Exception in execute_dynamic_addressing_ccc(): {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc_with_read(
        self, ccc_type, command_id, dynamic_address=-1
    ):
        """Executes the CCC used for dynamic addressing based on the given inputs.
        
        And returns the data read back from the DUT.
        This API is only applicable for the ENTDAA in the current spec.
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}

        Return:
            read_data {list of int}
        """
        try:
            read_data = self.i3c_session.ExecuteDynamicAddressingCCCWithRead(
                ccc_type, command_id, dynamic_address
            )
            return read_data

        except Exception as e:
            print(
                "Exception in execute_dynamic_addressing_ccc_with_read(): {}".format(e)
            )
            raise e

    def execute_sdr_ccc_write(
        self, ccc_type, command_id, defining_byte=-1, write_data=None
    ):
        """Executes the write CCC commands used in SDR mode based on the given inputs.
        
        If for a given Command ID the defining byte
        and data are not applicable then they will be ignored.
        If the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            write_data: {list of int}
        """
        try:
            self.i3c_session.ExecuteSDRCCCWrite(
                ccc_type, command_id, defining_byte, write_data
            )

        except Exception as e:
            print("Exception in execute_sdr_ccc_write: {}".format(e))
            raise e

    def execute_sdr_ccc_read(
        self, ccc_type, command_id, defining_byte=-1, read_byte_length=-1
    ):
        """Executes the read CCC commands used in SDR mode based on the given inputs.
        
        And returns the read data.
        If for a given Command ID the Defining Byte is not applicable then they will be ignored.
        The  read Data Length will only be considered if the value is not provided in the csv file
        else it will take the value from the csv file.
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            read_byte_length: {int}

        Returns:
            read_data {list of int}
        """
        try:
            read_data = self.i3c_session.ExecuteSDRCCCRead(
                ccc_type, command_id, defining_byte, read_byte_length
            )
            return read_data

        except Exception as e:
            print("Exception in execute_sdr_ccc_read: {}".format(e))
            raise e
````

<!--NI_OSS_SOURCE repo=nisemi-python path=poetry.lock sha256=645dd14172f1cbcd60a7cb180241a6ff486a47c331b8cc47c1688104901757e1 bytes=50896 -->
## FILE: poetry.lock

- repository: `ni/nisemi-python`
- source_path: `poetry.lock`
- sha256: `645dd14172f1cbcd60a7cb180241a6ff486a47c331b8cc47c1688104901757e1`
- bytes: 50896

````text
# This file is automatically @generated by Poetry 1.4.2 and should not be changed by hand.

[[package]]
name = "black"
version = "23.3.0"
description = "The uncompromising code formatter."
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "black-23.3.0-cp310-cp310-macosx_10_16_arm64.whl", hash = "sha256:0945e13506be58bf7db93ee5853243eb368ace1c08a24c65ce108986eac65915"},
    {file = "black-23.3.0-cp310-cp310-macosx_10_16_universal2.whl", hash = "sha256:67de8d0c209eb5b330cce2469503de11bca4085880d62f1628bd9972cc3366b9"},
    {file = "black-23.3.0-cp310-cp310-macosx_10_16_x86_64.whl", hash = "sha256:7c3eb7cea23904399866c55826b31c1f55bbcd3890ce22ff70466b907b6775c2"},
    {file = "black-23.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:32daa9783106c28815d05b724238e30718f34155653d4d6e125dc7daec8e260c"},
    {file = "black-23.3.0-cp310-cp310-win_amd64.whl", hash = "sha256:35d1381d7a22cc5b2be2f72c7dfdae4072a3336060635718cc7e1ede24221d6c"},
    {file = "black-23.3.0-cp311-cp311-macosx_10_16_arm64.whl", hash = "sha256:a8a968125d0a6a404842fa1bf0b349a568634f856aa08ffaff40ae0dfa52e7c6"},
    {file = "black-23.3.0-cp311-cp311-macosx_10_16_universal2.whl", hash = "sha256:c7ab5790333c448903c4b721b59c0d80b11fe5e9803d8703e84dcb8da56fec1b"},
    {file = "black-23.3.0-cp311-cp311-macosx_10_16_x86_64.whl", hash = "sha256:a6f6886c9869d4daae2d1715ce34a19bbc4b95006d20ed785ca00fa03cba312d"},
    {file = "black-23.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6f3c333ea1dd6771b2d3777482429864f8e258899f6ff05826c3a4fcc5ce3f70"},
    {file = "black-23.3.0-cp311-cp311-win_amd64.whl", hash = "sha256:11c410f71b876f961d1de77b9699ad19f939094c3a677323f43d7a29855fe326"},
    {file = "black-23.3.0-cp37-cp37m-macosx_10_16_x86_64.whl", hash = "sha256:1d06691f1eb8de91cd1b322f21e3bfc9efe0c7ca1f0e1eb1db44ea367dff656b"},
    {file = "black-23.3.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:50cb33cac881766a5cd9913e10ff75b1e8eb71babf4c7104f2e9c52da1fb7de2"},
    {file = "black-23.3.0-cp37-cp37m-win_amd64.whl", hash = "sha256:e114420bf26b90d4b9daa597351337762b63039752bdf72bf361364c1aa05925"},
    {file = "black-23.3.0-cp38-cp38-macosx_10_16_arm64.whl", hash = "sha256:48f9d345675bb7fbc3dd85821b12487e1b9a75242028adad0333ce36ed2a6d27"},
    {file = "black-23.3.0-cp38-cp38-macosx_10_16_universal2.whl", hash = "sha256:714290490c18fb0126baa0fca0a54ee795f7502b44177e1ce7624ba1c00f2331"},
    {file = "black-23.3.0-cp38-cp38-macosx_10_16_x86_64.whl", hash = "sha256:064101748afa12ad2291c2b91c960be28b817c0c7eaa35bec09cc63aa56493c5"},
    {file = "black-23.3.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:562bd3a70495facf56814293149e51aa1be9931567474993c7942ff7d3533961"},
    {file = "black-23.3.0-cp38-cp38-win_amd64.whl", hash = "sha256:e198cf27888ad6f4ff331ca1c48ffc038848ea9f031a3b40ba36aced7e22f2c8"},
    {file = "black-23.3.0-cp39-cp39-macosx_10_16_arm64.whl", hash = "sha256:3238f2aacf827d18d26db07524e44741233ae09a584273aa059066d644ca7b30"},
    {file = "black-23.3.0-cp39-cp39-macosx_10_16_universal2.whl", hash = "sha256:f0bd2f4a58d6666500542b26354978218a9babcdc972722f4bf90779524515f3"},
    {file = "black-23.3.0-cp39-cp39-macosx_10_16_x86_64.whl", hash = "sha256:92c543f6854c28a3c7f39f4d9b7694f9a6eb9d3c5e2ece488c327b6e7ea9b266"},
    {file = "black-23.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3a150542a204124ed00683f0db1f5cf1c2aaaa9cc3495b7a3b5976fb136090ab"},
    {file = "black-23.3.0-cp39-cp39-win_amd64.whl", hash = "sha256:6b39abdfb402002b8a7d030ccc85cf5afff64ee90fa4c5aebc531e3ad0175ddb"},
    {file = "black-23.3.0-py3-none-any.whl", hash = "sha256:ec751418022185b0c1bb7d7736e6933d40bbb14c14a0abcf9123d1b159f98dd4"},
    {file = "black-23.3.0.tar.gz", hash = "sha256:1c7b8d606e728a41ea1ccbd7264677e494e87cf630e399262ced92d4a8dac940"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typed-ast = {version = ">=1.4.2", markers = "python_version < \"3.8\" and implementation_name == \"cpython\""}
typing-extensions = {version = ">=3.10.0.0", markers = "python_version < \"3.10\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.7.4)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "cffi"
version = "1.15.1"
description = "Foreign Function Interface for Python calling C code."
category = "main"
optional = false
python-versions = "*"
files = [
    {file = "cffi-1.15.1-cp27-cp27m-macosx_10_9_x86_64.whl", hash = "sha256:a66d3508133af6e8548451b25058d5812812ec3798c886bf38ed24a98216fab2"},
    {file = "cffi-1.15.1-cp27-cp27m-manylinux1_i686.whl", hash = "sha256:470c103ae716238bbe698d67ad020e1db9d9dba34fa5a899b5e21577e6d52ed2"},
    {file = "cffi-1.15.1-cp27-cp27m-manylinux1_x86_64.whl", hash = "sha256:9ad5db27f9cabae298d151c85cf2bad1d359a1b9c686a275df03385758e2f914"},
    {file = "cffi-1.15.1-cp27-cp27m-win32.whl", hash = "sha256:b3bbeb01c2b273cca1e1e0c5df57f12dce9a4dd331b4fa1635b8bec26350bde3"},
    {file = "cffi-1.15.1-cp27-cp27m-win_amd64.whl", hash = "sha256:e00b098126fd45523dd056d2efba6c5a63b71ffe9f2bbe1a4fe1716e1d0c331e"},
    {file = "cffi-1.15.1-cp27-cp27mu-manylinux1_i686.whl", hash = "sha256:d61f4695e6c866a23a21acab0509af1cdfd2c013cf256bbf5b6b5e2695827162"},
    {file = "cffi-1.15.1-cp27-cp27mu-manylinux1_x86_64.whl", hash = "sha256:ed9cb427ba5504c1dc15ede7d516b84757c3e3d7868ccc85121d9310d27eed0b"},
    {file = "cffi-1.15.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:39d39875251ca8f612b6f33e6b1195af86d1b3e60086068be9cc053aa4376e21"},
    {file = "cffi-1.15.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:285d29981935eb726a4399badae8f0ffdff4f5050eaa6d0cfc3f64b857b77185"},
    {file = "cffi-1.15.1-cp310-cp310-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3eb6971dcff08619f8d91607cfc726518b6fa2a9eba42856be181c6d0d9515fd"},
    {file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:21157295583fe8943475029ed5abdcf71eb3911894724e360acff1d61c1d54bc"},
    {file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5635bd9cb9731e6d4a1132a498dd34f764034a8ce60cef4f5319c0541159392f"},
    {file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2012c72d854c2d03e45d06ae57f40d78e5770d252f195b93f581acf3ba44496e"},
    {file = "cffi-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dd86c085fae2efd48ac91dd7ccffcfc0571387fe1193d33b6394db7ef31fe2a4"},
    {file = "cffi-1.15.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:fa6693661a4c91757f4412306191b6dc88c1703f780c8234035eac011922bc01"},
    {file = "cffi-1.15.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:59c0b02d0a6c384d453fece7566d1c7e6b7bae4fc5874ef2ef46d56776d61c9e"},
    {file = "cffi-1.15.1-cp310-cp310-win32.whl", hash = "sha256:cba9d6b9a7d64d4bd46167096fc9d2f835e25d7e4c121fb2ddfc6528fb0413b2"},
    {file = "cffi-1.15.1-cp310-cp310-win_amd64.whl", hash = "sha256:ce4bcc037df4fc5e3d184794f27bdaab018943698f4ca31630bc7f84a7b69c6d"},
    {file = "cffi-1.15.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:3d08afd128ddaa624a48cf2b859afef385b720bb4b43df214f85616922e6a5ac"},
    {file = "cffi-1.15.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:3799aecf2e17cf585d977b780ce79ff0dc9b78d799fc694221ce814c2c19db83"},
    {file = "cffi-1.15.1-cp311-cp311-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a591fe9e525846e4d154205572a029f653ada1a78b93697f3b5a8f1f2bc055b9"},
    {file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3548db281cd7d2561c9ad9984681c95f7b0e38881201e157833a2342c30d5e8c"},
    {file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:91fc98adde3d7881af9b59ed0294046f3806221863722ba7d8d120c575314325"},
    {file = "cffi-1.15.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:94411f22c3985acaec6f83c6df553f2dbe17b698cc7f8ae751ff2237d96b9e3c"},
    {file = "cffi-1.15.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:03425bdae262c76aad70202debd780501fabeaca237cdfddc008987c0e0f59ef"},
    {file = "cffi-1.15.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:cc4d65aeeaa04136a12677d3dd0b1c0c94dc43abac5860ab33cceb42b801c1e8"},
    {file = "cffi-1.15.1-cp311-cp311-win32.whl", hash = "sha256:a0f100c8912c114ff53e1202d0078b425bee3649ae34d7b070e9697f93c5d52d"},
    {file = "cffi-1.15.1-cp311-cp311-win_amd64.whl", hash = "sha256:04ed324bda3cda42b9b695d51bb7d54b680b9719cfab04227cdd1e04e5de3104"},
    {file = "cffi-1.15.1-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:50a74364d85fd319352182ef59c5c790484a336f6db772c1a9231f1c3ed0cbd7"},
    {file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e263d77ee3dd201c3a142934a086a4450861778baaeeb45db4591ef65550b0a6"},
    {file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:cec7d9412a9102bdc577382c3929b337320c4c4c4849f2c5cdd14d7368c5562d"},
    {file = "cffi-1.15.1-cp36-cp36m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4289fc34b2f5316fbb762d75362931e351941fa95fa18789191b33fc4cf9504a"},
    {file = "cffi-1.15.1-cp36-cp36m-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:173379135477dc8cac4bc58f45db08ab45d228b3363adb7af79436135d028405"},
    {file = "cffi-1.15.1-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.whl", hash = "sha256:6975a3fac6bc83c4a65c9f9fcab9e47019a11d3d2cf7f3c0d03431bf145a941e"},
    {file = "cffi-1.15.1-cp36-cp36m-win32.whl", hash = "sha256:2470043b93ff09bf8fb1d46d1cb756ce6132c54826661a32d4e4d132e1977adf"},
    {file = "cffi-1.15.1-cp36-cp36m-win_amd64.whl", hash = "sha256:30d78fbc8ebf9c92c9b7823ee18eb92f2e6ef79b45ac84db507f52fbe3ec4497"},
    {file = "cffi-1.15.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:198caafb44239b60e252492445da556afafc7d1e3ab7a1fb3f0584ef6d742375"},
    {file = "cffi-1.15.1-cp37-cp37m-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5ef34d190326c3b1f822a5b7a45f6c4535e2f47ed06fec77d3d799c450b2651e"},
    {file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8102eaf27e1e448db915d08afa8b41d6c7ca7a04b7d73af6514df10a3e74bd82"},
    {file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5df2768244d19ab7f60546d0c7c63ce1581f7af8b5de3eb3004b9b6fc8a9f84b"},
    {file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a8c4917bd7ad33e8eb21e9a5bbba979b49d9a97acb3a803092cbc1133e20343c"},
    {file = "cffi-1.15.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0e2642fe3142e4cc4af0799748233ad6da94c62a8bec3a6648bf8ee68b1c7426"},
    {file = "cffi-1.15.1-cp37-cp37m-win32.whl", hash = "sha256:e229a521186c75c8ad9490854fd8bbdd9a0c9aa3a524326b55be83b54d4e0ad9"},
    {file = "cffi-1.15.1-cp37-cp37m-win_amd64.whl", hash = "sha256:a0b71b1b8fbf2b96e41c4d990244165e2c9be83d54962a9a1d118fd8657d2045"},
    {file = "cffi-1.15.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:320dab6e7cb2eacdf0e658569d2575c4dad258c0fcc794f46215e1e39f90f2c3"},
    {file = "cffi-1.15.1-cp38-cp38-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1e74c6b51a9ed6589199c787bf5f9875612ca4a8a0785fb2d4a84429badaf22a"},
    {file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a5c84c68147988265e60416b57fc83425a78058853509c1b0629c180094904a5"},
    {file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3b926aa83d1edb5aa5b427b4053dc420ec295a08e40911296b9eb1b6170f6cca"},
    {file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87c450779d0914f2861b8526e035c5e6da0a3199d8f1add1a665e1cbc6fc6d02"},
    {file = "cffi-1.15.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4f2c9f67e9821cad2e5f480bc8d83b8742896f1242dba247911072d4fa94c192"},
    {file = "cffi-1.15.1-cp38-cp38-win32.whl", hash = "sha256:8b7ee99e510d7b66cdb6c593f21c043c248537a32e0bedf02e01e9553a172314"},
    {file = "cffi-1.15.1-cp38-cp38-win_amd64.whl", hash = "sha256:00a9ed42e88df81ffae7a8ab6d9356b371399b91dbdf0c3cb1e84c03a13aceb5"},
    {file = "cffi-1.15.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:54a2db7b78338edd780e7ef7f9f6c442500fb0d41a5a4ea24fff1c929d5af585"},
    {file = "cffi-1.15.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:fcd131dd944808b5bdb38e6f5b53013c5aa4f334c5cad0c72742f6eba4b73db0"},
    {file = "cffi-1.15.1-cp39-cp39-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7473e861101c9e72452f9bf8acb984947aa1661a7704553a9f6e4baa5ba64415"},
    {file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6c9a799e985904922a4d207a94eae35c78ebae90e128f0c4e521ce339396be9d"},
    {file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3bcde07039e586f91b45c88f8583ea7cf7a0770df3a1649627bf598332cb6984"},
    {file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:33ab79603146aace82c2427da5ca6e58f2b3f2fb5da893ceac0c42218a40be35"},
    {file = "cffi-1.15.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5d598b938678ebf3c67377cdd45e09d431369c3b1a5b331058c338e201f12b27"},
    {file = "cffi-1.15.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:db0fbb9c62743ce59a9ff687eb5f4afbe77e5e8403d6697f7446e5f609976f76"},
    {file = "cffi-1.15.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:98d85c6a2bef81588d9227dde12db8a7f47f639f4a17c9ae08e773aa9c697bf3"},
    {file = "cffi-1.15.1-cp39-cp39-win32.whl", hash = "sha256:40f4774f5a9d4f5e344f31a32b5096977b5d48560c5592e2f3d2c4374bd543ee"},
    {file = "cffi-1.15.1-cp39-cp39-win_amd64.whl", hash = "sha256:70df4e3b545a17496c9b3f41f5115e69a4f2e77e94e1d2a8e1070bc0c38c8a3c"},
    {file = "cffi-1.15.1.tar.gz", hash = "sha256:d400bfb9a37b1351253cb402671cea7e89bdecc294e8016a707f6d1d8ac934f9"},
]

[package.dependencies]
pycparser = "*"

[[package]]
name = "click"
version = "8.1.7"
description = "Composable command line interface toolkit"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "click-8.1.7-py3-none-any.whl", hash = "sha256:ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28"},
    {file = "click-8.1.7.tar.gz", hash = "sha256:ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}
importlib-metadata = {version = "*", markers = "python_version < \"3.8\""}

[[package]]
name = "clr-loader"
version = "0.2.6"
description = "Generic pure Python loader for .NET runtimes"
category = "main"
optional = false
python-versions = ">=3.7"
files = [
    {file = "clr_loader-0.2.6-py3-none-any.whl", hash = "sha256:79bbfee4bf6ac2f4836d89af2c39e0c32dce5d0c062596185aef380f317507a6"},
    {file = "clr_loader-0.2.6.tar.gz", hash = "sha256:019348ae6b6a83c7a406d14537c277cecf7a3a53b263ec342c81ded5845a67ee"},
]

[package.dependencies]
cffi = ">=1.13"

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
category = "dev"
optional = false
python-versions = ">=3.6.1"
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
importlib-metadata = {version = ">=1.1.0,<4.3", markers = "python_version < \"3.8\""}
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
category = "dev"
optional = false
python-versions = ">=3.8.1"
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
category = "dev"
optional = false
python-versions = ">=3.7"
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
category = "dev"
optional = false
python-versions = ">=3.7"
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
category = "dev"
optional = false
python-versions = "*"
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "grpcio"
version = "1.62.2"
description = "HTTP/2-based RPC framework"
category = "main"
optional = false
python-versions = ">=3.7"
files = [
    {file = "grpcio-1.62.2-cp310-cp310-linux_armv7l.whl", hash = "sha256:66344ea741124c38588a664237ac2fa16dfd226964cca23ddc96bd4accccbde5"},
    {file = "grpcio-1.62.2-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:5dab7ac2c1e7cb6179c6bfad6b63174851102cbe0682294e6b1d6f0981ad7138"},
    {file = "grpcio-1.62.2-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:3ad00f3f0718894749d5a8bb0fa125a7980a2f49523731a9b1fabf2b3522aa43"},
    {file = "grpcio-1.62.2-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:2e72ddfee62430ea80133d2cbe788e0d06b12f865765cb24a40009668bd8ea05"},
    {file = "grpcio-1.62.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:53d3a59a10af4c2558a8e563aed9f256259d2992ae0d3037817b2155f0341de1"},
    {file = "grpcio-1.62.2-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:a1511a303f8074f67af4119275b4f954189e8313541da7b88b1b3a71425cdb10"},
    {file = "grpcio-1.62.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:b94d41b7412ef149743fbc3178e59d95228a7064c5ab4760ae82b562bdffb199"},
    {file = "grpcio-1.62.2-cp310-cp310-win32.whl", hash = "sha256:a75af2fc7cb1fe25785be7bed1ab18cef959a376cdae7c6870184307614caa3f"},
    {file = "grpcio-1.62.2-cp310-cp310-win_amd64.whl", hash = "sha256:80407bc007754f108dc2061e37480238b0dc1952c855e86a4fc283501ee6bb5d"},
    {file = "grpcio-1.62.2-cp311-cp311-linux_armv7l.whl", hash = "sha256:c1624aa686d4b36790ed1c2e2306cc3498778dffaf7b8dd47066cf819028c3ad"},
    {file = "grpcio-1.62.2-cp311-cp311-macosx_10_10_universal2.whl", hash = "sha256:1c1bb80299bdef33309dff03932264636450c8fdb142ea39f47e06a7153d3063"},
    {file = "grpcio-1.62.2-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:db068bbc9b1fa16479a82e1ecf172a93874540cb84be69f0b9cb9b7ac3c82670"},
    {file = "grpcio-1.62.2-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e2cc8a308780edbe2c4913d6a49dbdb5befacdf72d489a368566be44cadaef1a"},
    {file = "grpcio-1.62.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d0695ae31a89f1a8fc8256050329a91a9995b549a88619263a594ca31b76d756"},
    {file = "grpcio-1.62.2-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:88b4f9ee77191dcdd8810241e89340a12cbe050be3e0d5f2f091c15571cd3930"},
    {file = "grpcio-1.62.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:2a0204532aa2f1afd467024b02b4069246320405bc18abec7babab03e2644e75"},
    {file = "grpcio-1.62.2-cp311-cp311-win32.whl", hash = "sha256:6e784f60e575a0de554ef9251cbc2ceb8790914fe324f11e28450047f264ee6f"},
    {file = "grpcio-1.62.2-cp311-cp311-win_amd64.whl", hash = "sha256:112eaa7865dd9e6d7c0556c8b04ae3c3a2dc35d62ad3373ab7f6a562d8199200"},
    {file = "grpcio-1.62.2-cp312-cp312-linux_armv7l.whl", hash = "sha256:65034473fc09628a02fb85f26e73885cf1ed39ebd9cf270247b38689ff5942c5"},
    {file = "grpcio-1.62.2-cp312-cp312-macosx_10_10_universal2.whl", hash = "sha256:d2c1771d0ee3cf72d69bb5e82c6a82f27fbd504c8c782575eddb7839729fbaad"},
    {file = "grpcio-1.62.2-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:3abe6838196da518863b5d549938ce3159d809218936851b395b09cad9b5d64a"},
    {file = "grpcio-1.62.2-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c5ffeb269f10cedb4f33142b89a061acda9f672fd1357331dbfd043422c94e9e"},
    {file = "grpcio-1.62.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:404d3b4b6b142b99ba1cff0b2177d26b623101ea2ce51c25ef6e53d9d0d87bcc"},
    {file = "grpcio-1.62.2-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:262cda97efdabb20853d3b5a4c546a535347c14b64c017f628ca0cc7fa780cc6"},
    {file = "grpcio-1.62.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:17708db5b11b966373e21519c4c73e5a750555f02fde82276ea2a267077c68ad"},
    {file = "grpcio-1.62.2-cp312-cp312-win32.whl", hash = "sha256:b7ec9e2f8ffc8436f6b642a10019fc513722858f295f7efc28de135d336ac189"},
    {file = "grpcio-1.62.2-cp312-cp312-win_amd64.whl", hash = "sha256:aa787b83a3cd5e482e5c79be030e2b4a122ecc6c5c6c4c42a023a2b581fdf17b"},
    {file = "grpcio-1.62.2-cp37-cp37m-linux_armv7l.whl", hash = "sha256:cfd23ad29bfa13fd4188433b0e250f84ec2c8ba66b14a9877e8bce05b524cf54"},
    {file = "grpcio-1.62.2-cp37-cp37m-macosx_10_10_universal2.whl", hash = "sha256:af15e9efa4d776dfcecd1d083f3ccfb04f876d613e90ef8432432efbeeac689d"},
    {file = "grpcio-1.62.2-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:f4aa94361bb5141a45ca9187464ae81a92a2a135ce2800b2203134f7a1a1d479"},
    {file = "grpcio-1.62.2-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:82af3613a219512a28ee5c95578eb38d44dd03bca02fd918aa05603c41018051"},
    {file = "grpcio-1.62.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:55ddaf53474e8caeb29eb03e3202f9d827ad3110475a21245f3c7712022882a9"},
    {file = "grpcio-1.62.2-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:c79b518c56dddeec79e5500a53d8a4db90da995dfe1738c3ac57fe46348be049"},
    {file = "grpcio-1.62.2-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:a5eb4844e5e60bf2c446ef38c5b40d7752c6effdee882f716eb57ae87255d20a"},
    {file = "grpcio-1.62.2-cp37-cp37m-win_amd64.whl", hash = "sha256:aaae70364a2d1fb238afd6cc9fcb10442b66e397fd559d3f0968d28cc3ac929c"},
    {file = "grpcio-1.62.2-cp38-cp38-linux_armv7l.whl", hash = "sha256:1bcfe5070e4406f489e39325b76caeadab28c32bf9252d3ae960c79935a4cc36"},
    {file = "grpcio-1.62.2-cp38-cp38-macosx_10_10_universal2.whl", hash = "sha256:da6a7b6b938c15fa0f0568e482efaae9c3af31963eec2da4ff13a6d8ec2888e4"},
    {file = "grpcio-1.62.2-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:41955b641c34db7d84db8d306937b72bc4968eef1c401bea73081a8d6c3d8033"},
    {file = "grpcio-1.62.2-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c772f225483905f675cb36a025969eef9712f4698364ecd3a63093760deea1bc"},
    {file = "grpcio-1.62.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:07ce1f775d37ca18c7a141300e5b71539690efa1f51fe17f812ca85b5e73262f"},
    {file = "grpcio-1.62.2-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:26f415f40f4a93579fd648f48dca1c13dfacdfd0290f4a30f9b9aeb745026811"},
    {file = "grpcio-1.62.2-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:db707e3685ff16fc1eccad68527d072ac8bdd2e390f6daa97bc394ea7de4acea"},
    {file = "grpcio-1.62.2-cp38-cp38-win32.whl", hash = "sha256:589ea8e75de5fd6df387de53af6c9189c5231e212b9aa306b6b0d4f07520fbb9"},
    {file = "grpcio-1.62.2-cp38-cp38-win_amd64.whl", hash = "sha256:3c3ed41f4d7a3aabf0f01ecc70d6b5d00ce1800d4af652a549de3f7cf35c4abd"},
    {file = "grpcio-1.62.2-cp39-cp39-linux_armv7l.whl", hash = "sha256:162ccf61499c893831b8437120600290a99c0bc1ce7b51f2c8d21ec87ff6af8b"},
    {file = "grpcio-1.62.2-cp39-cp39-macosx_10_10_universal2.whl", hash = "sha256:f27246d7da7d7e3bd8612f63785a7b0c39a244cf14b8dd9dd2f2fab939f2d7f1"},
    {file = "grpcio-1.62.2-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:2507006c8a478f19e99b6fe36a2464696b89d40d88f34e4b709abe57e1337467"},
    {file = "grpcio-1.62.2-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a90ac47a8ce934e2c8d71e317d2f9e7e6aaceb2d199de940ce2c2eb611b8c0f4"},
    {file = "grpcio-1.62.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99701979bcaaa7de8d5f60476487c5df8f27483624f1f7e300ff4669ee44d1f2"},
    {file = "grpcio-1.62.2-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:af7dc3f7a44f10863b1b0ecab4078f0a00f561aae1edbd01fd03ad4dcf61c9e9"},
    {file = "grpcio-1.62.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:fa63245271920786f4cb44dcada4983a3516be8f470924528cf658731864c14b"},
    {file = "grpcio-1.62.2-cp39-cp39-win32.whl", hash = "sha256:c6ad9c39704256ed91a1cffc1379d63f7d0278d6a0bad06b0330f5d30291e3a3"},
    {file = "grpcio-1.62.2-cp39-cp39-win_amd64.whl", hash = "sha256:16da954692fd61aa4941fbeda405a756cd96b97b5d95ca58a92547bba2c1624f"},
    {file = "grpcio-1.62.2.tar.gz", hash = "sha256:c77618071d96b7a8be2c10701a98537823b9c65ba256c0b9067e0594cdbd954d"},
]

[package.extras]
protobuf = ["grpcio-tools (>=1.62.2)"]

[[package]]
name = "importlib-metadata"
version = "4.2.0"
description = "Read metadata from Python packages"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "importlib_metadata-4.2.0-py3-none-any.whl", hash = "sha256:057e92c15bc8d9e8109738a48db0ccb31b4d9d5cfbee5a8670879a30be66304b"},
    {file = "importlib_metadata-4.2.0.tar.gz", hash = "sha256:b7e52a1f8dec14a75ea73e0891f3060099ca1d8e6a462a4dff11c3e119ea1b31"},
]

[package.dependencies]
typing-extensions = {version = ">=3.6.4", markers = "python_version < \"3.8\""}
zipp = ">=0.5"

[package.extras]
docs = ["jaraco.packaging (>=8.2)", "rst.linker (>=1.9)", "sphinx"]
testing = ["flufl.flake8", "importlib-resources (>=1.3)", "packaging", "pep517", "pyfakefs", "pytest (>=4.6)", "pytest-black (>=0.3.7)", "pytest-checkdocs (>=2.4)", "pytest-cov", "pytest-enabler (>=1.0.1)", "pytest-flake8", "pytest-mypy"]

[[package]]
name = "importlib-metadata"
version = "4.13.0"
description = "Read metadata from Python packages"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "importlib_metadata-4.13.0-py3-none-any.whl", hash = "sha256:8a8a81bcf996e74fee46f0d16bd3eaa382a7eb20fd82445c3ad11f4090334116"},
    {file = "importlib_metadata-4.13.0.tar.gz", hash = "sha256:dd0173e8f150d6815e098fd354f6414b0f079af4644ddfe90c71e2fc6174346d"},
]

[package.dependencies]
typing-extensions = {version = ">=3.6.4", markers = "python_version < \"3.8\""}
zipp = ">=0.5"

[package.extras]
docs = ["furo", "jaraco.packaging (>=9)", "jaraco.tidelift (>=1.4)", "rst.linker (>=1.9)", "sphinx (>=3.5)"]
perf = ["ipython"]
testing = ["flake8 (<5)", "flufl.flake8", "importlib-resources (>=1.3)", "packaging", "pyfakefs", "pytest (>=6)", "pytest-black (>=0.3.7)", "pytest-checkdocs (>=2.4)", "pytest-cov", "pytest-enabler (>=1.3)", "pytest-flake8", "pytest-mypy (>=0.9.1)", "pytest-perf (>=0.9.2)"]

[[package]]
name = "isort"
version = "5.11.5"
description = "A Python utility / library to sort Python imports."
category = "dev"
optional = false
python-versions = ">=3.7.0"
files = [
    {file = "isort-5.11.5-py3-none-any.whl", hash = "sha256:ba1d72fb2595a01c7895a5128f9585a5cc4b6d395f1c8d514989b9a7eb2a8746"},
    {file = "isort-5.11.5.tar.gz", hash = "sha256:6be1f76a507cb2ecf16c7cf14a37e41609ca082330be4e3436a18ef74add55db"},
]

[package.extras]
colors = ["colorama (>=0.4.3,<0.5.0)"]
pipfile-deprecated-finder = ["pip-shims (>=0.5.2)", "pipreqs", "requirementslib"]
plugins = ["setuptools"]
requirements-deprecated-finder = ["pip-api", "pipreqs"]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mypy-extensions"
version = "1.0.0"
description = "Type system extensions for programs checked with the mypy type checker."
category = "dev"
optional = false
python-versions = ">=3.5"
files = [
    {file = "mypy_extensions-1.0.0-py3-none-any.whl", hash = "sha256:4392f6c0eb8a5668a69e23d168ffa70f0be9ccfd32b5cc2d26a34ae5b844552d"},
    {file = "mypy_extensions-1.0.0.tar.gz", hash = "sha256:75dbf8955dc00442a438fc4d0666508a9a97b6bd41aa2f0ffe9d2f2725af0782"},
]

[[package]]
name = "ni-python-styleguide"
version = "0.4.5"
description = "NI's internal and external Python linter rules and plugins"
category = "dev"
optional = false
python-versions = "<4.0,>=3.7"
files = [
    {file = "ni_python_styleguide-0.4.5-py3-none-any.whl", hash = "sha256:a46298342523f1e665e027df443ad882556259e430d7fa867f2703aa68028704"},
    {file = "ni_python_styleguide-0.4.5.tar.gz", hash = "sha256:0ff8899cea1deed6a2d458765c1d645f85cc563089904c78bbafcba03bea2f91"},
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
importlib-metadata = {version = "<5.0", markers = "python_version < \"3.8\""}
isort = ">=5.10"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.7\" and python_version < \"3.12\""},
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
]
toml = ">=0.10.1"

[[package]]
name = "packaging"
version = "24.0"
description = "Core utilities for Python packages"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "packaging-24.0-py3-none-any.whl", hash = "sha256:2ddfb553fdf02fb784c234c7ba6ccc288296ceabec964ad2eae3777778130bc5"},
    {file = "packaging-24.0.tar.gz", hash = "sha256:eb82c5e3e56209074766e6885bb04b8c38a0c015d0a30036ebe7ece34c9989e9"},
]

[[package]]
name = "pathspec"
version = "0.11.2"
description = "Utility library for gitignore style pattern matching of file paths."
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "pathspec-0.11.2-py3-none-any.whl", hash = "sha256:1d6ed233af05e679efb96b1851550ea95bbb64b7c490b0f5aa52996c11e92a20"},
    {file = "pathspec-0.11.2.tar.gz", hash = "sha256:e0d8d0ac2f12da61956eb2306b69f9469b42f4deb0f3cb6ed47b9cce9996ced3"},
]

[[package]]
name = "pep8-naming"
version = "0.13.3"
description = "Check PEP-8 naming conventions, plugin for flake8"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "pep8-naming-0.13.3.tar.gz", hash = "sha256:1705f046dfcd851378aac3be1cd1551c7c1e5ff363bacad707d43007877fa971"},
    {file = "pep8_naming-0.13.3-py3-none-any.whl", hash = "sha256:1a86b8c71a03337c97181917e2b472f0f5e4ccb06844a0d6f0a33522549e7a80"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.0.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a \"user data dir\"."
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "platformdirs-4.0.0-py3-none-any.whl", hash = "sha256:118c954d7e949b35437270383a3f2531e99dd93cf7ce4dc8340d3356d30f173b"},
    {file = "platformdirs-4.0.0.tar.gz", hash = "sha256:cb633b2bcf10c51af60beb0ab06d2f1d69064b43abf4c185ca6b28865f3f9731"},
]

[package.dependencies]
typing-extensions = {version = ">=4.7.1", markers = "python_version < \"3.8\""}

[package.extras]
docs = ["furo (>=2023.7.26)", "proselint (>=0.13)", "sphinx (>=7.1.1)", "sphinx-autodoc-typehints (>=1.24)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=7.4)", "pytest-cov (>=4.1)", "pytest-mock (>=3.11.1)"]

[[package]]
name = "protobuf"
version = "4.24.4"
description = ""
category = "main"
optional = false
python-versions = ">=3.7"
files = [
    {file = "protobuf-4.24.4-cp310-abi3-win32.whl", hash = "sha256:ec9912d5cb6714a5710e28e592ee1093d68c5ebfeda61983b3f40331da0b1ebb"},
    {file = "protobuf-4.24.4-cp310-abi3-win_amd64.whl", hash = "sha256:1badab72aa8a3a2b812eacfede5020472e16c6b2212d737cefd685884c191085"},
    {file = "protobuf-4.24.4-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:8e61a27f362369c2f33248a0ff6896c20dcd47b5d48239cb9720134bef6082e4"},
    {file = "protobuf-4.24.4-cp37-abi3-manylinux2014_aarch64.whl", hash = "sha256:bffa46ad9612e6779d0e51ae586fde768339b791a50610d85eb162daeb23661e"},
    {file = "protobuf-4.24.4-cp37-abi3-manylinux2014_x86_64.whl", hash = "sha256:b493cb590960ff863743b9ff1452c413c2ee12b782f48beca77c8da3e2ffe9d9"},
    {file = "protobuf-4.24.4-cp37-cp37m-win32.whl", hash = "sha256:dbbed8a56e56cee8d9d522ce844a1379a72a70f453bde6243e3c86c30c2a3d46"},
    {file = "protobuf-4.24.4-cp37-cp37m-win_amd64.whl", hash = "sha256:6b7d2e1c753715dcfe9d284a25a52d67818dd43c4932574307daf836f0071e37"},
    {file = "protobuf-4.24.4-cp38-cp38-win32.whl", hash = "sha256:02212557a76cd99574775a81fefeba8738d0f668d6abd0c6b1d3adcc75503dbe"},
    {file = "protobuf-4.24.4-cp38-cp38-win_amd64.whl", hash = "sha256:2fa3886dfaae6b4c5ed2730d3bf47c7a38a72b3a1f0acb4d4caf68e6874b947b"},
    {file = "protobuf-4.24.4-cp39-cp39-win32.whl", hash = "sha256:b77272f3e28bb416e2071186cb39efd4abbf696d682cbb5dc731308ad37fa6dd"},
    {file = "protobuf-4.24.4-cp39-cp39-win_amd64.whl", hash = "sha256:9fee5e8aa20ef1b84123bb9232b3f4a5114d9897ed89b4b8142d81924e05d79b"},
    {file = "protobuf-4.24.4-py3-none-any.whl", hash = "sha256:80797ce7424f8c8d2f2547e2d42bfbb6c08230ce5832d6c099a37335c9c90a92"},
    {file = "protobuf-4.24.4.tar.gz", hash = "sha256:5a70731910cd9104762161719c3d883c960151eea077134458503723b60e3667"},
]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
category = "dev"
optional = false
python-versions = ">=3.8"
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pycparser"
version = "2.21"
description = "C parser in Python"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
files = [
    {file = "pycparser-2.21-py2.py3-none-any.whl", hash = "sha256:8ee45429555515e1f6b185e78100aea234072576aa43ab53aefcae078162fca9"},
    {file = "pycparser-2.21.tar.gz", hash = "sha256:e644fdec12f7872f86c58ff790da456218b10f863970249516d60a5eaca77206"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
importlib-metadata = {version = ">=2.0.0,<5.0.0", markers = "python_version < \"3.8\""}
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3)"]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
category = "dev"
optional = false
python-versions = ">=3.8"
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pythonnet"
version = "3.0.3"
description = ".NET and Mono integration for Python"
category = "main"
optional = false
python-versions = "<3.13,>=3.7"
files = [
    {file = "pythonnet-3.0.3-py3-none-any.whl", hash = "sha256:62486f860c7955b7dcf470e085e4d2b599512224ca24193f716e857b496c530f"},
    {file = "pythonnet-3.0.3.tar.gz", hash = "sha256:8d4b2e97158a023875f8647458a58f38817f4fe39af60abdd6b0d8adf1d77e75"},
]

[package.dependencies]
clr-loader = ">=0.2.6,<0.3.0"

[[package]]
name = "setuptools"
version = "68.0.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "setuptools-68.0.0-py3-none-any.whl", hash = "sha256:11e52c67415a381d10d6b462ced9cfb97066179f0e871399e006c4ab101fc85f"},
    {file = "setuptools-68.0.0.tar.gz", hash = "sha256:baf1fdb41c6da4cd2eae722e135500da913332ab3f2f5c7d33af9b492acb5235"},
]

[package.extras]
docs = ["furo", "jaraco.packaging (>=9)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-hoverxref (<2)", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (==0.8.3)", "sphinx-reredirects", "sphinxcontrib-towncrier"]
testing = ["build[virtualenv]", "filelock (>=3.4.0)", "flake8-2020", "ini2toml[lite] (>=0.9)", "jaraco.envs (>=2.2)", "jaraco.path (>=3.2.0)", "pip (>=19.1)", "pip-run (>=8.8)", "pytest (>=6)", "pytest-black (>=0.3.7)", "pytest-checkdocs (>=2.4)", "pytest-cov", "pytest-enabler (>=1.3)", "pytest-mypy (>=0.9.1)", "pytest-perf", "pytest-ruff", "pytest-timeout", "pytest-xdist", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel"]
testing-integration = ["build[virtualenv]", "filelock (>=3.4.0)", "jaraco.envs (>=2.2)", "jaraco.path (>=3.2.0)", "pytest", "pytest-enabler", "pytest-xdist", "tomli", "virtualenv (>=13.0.0)", "wheel"]

[[package]]
name = "snowballstemmer"
version = "2.2.0"
description = "This package provides 29 stemmers for 28 languages generated from Snowball algorithms."
category = "dev"
optional = false
python-versions = "*"
files = [
    {file = "snowballstemmer-2.2.0-py2.py3-none-any.whl", hash = "sha256:c8e1716e83cc398ae16824e5572ae04e0d9fc2c6b985fb0f900f5f0c96ecba1a"},
    {file = "snowballstemmer-2.2.0.tar.gz", hash = "sha256:09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
category = "dev"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.0.1"
description = "A lil' TOML parser"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "tomli-2.0.1-py3-none-any.whl", hash = "sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc"},
    {file = "tomli-2.0.1.tar.gz", hash = "sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f"},
]

[[package]]
name = "typed-ast"
version = "1.5.5"
description = "a fork of Python 2 and 3 ast modules with type comment support"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "typed_ast-1.5.5-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:4bc1efe0ce3ffb74784e06460f01a223ac1f6ab31c6bc0376a21184bf5aabe3b"},
    {file = "typed_ast-1.5.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:5f7a8c46a8b333f71abd61d7ab9255440d4a588f34a21f126bbfc95f6049e686"},
    {file = "typed_ast-1.5.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:597fc66b4162f959ee6a96b978c0435bd63791e31e4f410622d19f1686d5e769"},
    {file = "typed_ast-1.5.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d41b7a686ce653e06c2609075d397ebd5b969d821b9797d029fccd71fdec8e04"},
    {file = "typed_ast-1.5.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:5fe83a9a44c4ce67c796a1b466c270c1272e176603d5e06f6afbc101a572859d"},
    {file = "typed_ast-1.5.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:d5c0c112a74c0e5db2c75882a0adf3133adedcdbfd8cf7c9d6ed77365ab90a1d"},
    {file = "typed_ast-1.5.5-cp310-cp310-win_amd64.whl", hash = "sha256:e1a976ed4cc2d71bb073e1b2a250892a6e968ff02aa14c1f40eba4f365ffec02"},
    {file = "typed_ast-1.5.5-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:c631da9710271cb67b08bd3f3813b7af7f4c69c319b75475436fcab8c3d21bee"},
    {file = "typed_ast-1.5.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:b445c2abfecab89a932b20bd8261488d574591173d07827c1eda32c457358b18"},
    {file = "typed_ast-1.5.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cc95ffaaab2be3b25eb938779e43f513e0e538a84dd14a5d844b8f2932593d88"},
    {file = "typed_ast-1.5.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:61443214d9b4c660dcf4b5307f15c12cb30bdfe9588ce6158f4a005baeb167b2"},
    {file = "typed_ast-1.5.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:6eb936d107e4d474940469e8ec5b380c9b329b5f08b78282d46baeebd3692dc9"},
    {file = "typed_ast-1.5.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:e48bf27022897577d8479eaed64701ecaf0467182448bd95759883300ca818c8"},
    {file = "typed_ast-1.5.5-cp311-cp311-win_amd64.whl", hash = "sha256:83509f9324011c9a39faaef0922c6f720f9623afe3fe220b6d0b15638247206b"},
    {file = "typed_ast-1.5.5-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:44f214394fc1af23ca6d4e9e744804d890045d1643dd7e8229951e0ef39429b5"},
    {file = "typed_ast-1.5.5-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:118c1ce46ce58fda78503eae14b7664163aa735b620b64b5b725453696f2a35c"},
    {file = "typed_ast-1.5.5-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:be4919b808efa61101456e87f2d4c75b228f4e52618621c77f1ddcaae15904fa"},
    {file = "typed_ast-1.5.5-cp36-cp36m-musllinux_1_1_aarch64.whl", hash = "sha256:fc2b8c4e1bc5cd96c1a823a885e6b158f8451cf6f5530e1829390b4d27d0807f"},
    {file = "typed_ast-1.5.5-cp36-cp36m-musllinux_1_1_x86_64.whl", hash = "sha256:16f7313e0a08c7de57f2998c85e2a69a642e97cb32f87eb65fbfe88381a5e44d"},
    {file = "typed_ast-1.5.5-cp36-cp36m-win_amd64.whl", hash = "sha256:2b946ef8c04f77230489f75b4b5a4a6f24c078be4aed241cfabe9cbf4156e7e5"},
    {file = "typed_ast-1.5.5-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:2188bc33d85951ea4ddad55d2b35598b2709d122c11c75cffd529fbc9965508e"},
    {file = "typed_ast-1.5.5-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0635900d16ae133cab3b26c607586131269f88266954eb04ec31535c9a12ef1e"},
    {file = "typed_ast-1.5.5-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:57bfc3cf35a0f2fdf0a88a3044aafaec1d2f24d8ae8cd87c4f58d615fb5b6311"},
    {file = "typed_ast-1.5.5-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:fe58ef6a764de7b4b36edfc8592641f56e69b7163bba9f9c8089838ee596bfb2"},
    {file = "typed_ast-1.5.5-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:d09d930c2d1d621f717bb217bf1fe2584616febb5138d9b3e8cdd26506c3f6d4"},
    {file = "typed_ast-1.5.5-cp37-cp37m-win_amd64.whl", hash = "sha256:d40c10326893ecab8a80a53039164a224984339b2c32a6baf55ecbd5b1df6431"},
    {file = "typed_ast-1.5.5-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:fd946abf3c31fb50eee07451a6aedbfff912fcd13cf357363f5b4e834cc5e71a"},
    {file = "typed_ast-1.5.5-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:ed4a1a42df8a3dfb6b40c3d2de109e935949f2f66b19703eafade03173f8f437"},
    {file = "typed_ast-1.5.5-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:045f9930a1550d9352464e5149710d56a2aed23a2ffe78946478f7b5416f1ede"},
    {file = "typed_ast-1.5.5-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:381eed9c95484ceef5ced626355fdc0765ab51d8553fec08661dce654a935db4"},
    {file = "typed_ast-1.5.5-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:bfd39a41c0ef6f31684daff53befddae608f9daf6957140228a08e51f312d7e6"},
    {file = "typed_ast-1.5.5-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:8c524eb3024edcc04e288db9541fe1f438f82d281e591c548903d5b77ad1ddd4"},
    {file = "typed_ast-1.5.5-cp38-cp38-win_amd64.whl", hash = "sha256:7f58fabdde8dcbe764cef5e1a7fcb440f2463c1bbbec1cf2a86ca7bc1f95184b"},
    {file = "typed_ast-1.5.5-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:042eb665ff6bf020dd2243307d11ed626306b82812aba21836096d229fdc6a10"},
    {file = "typed_ast-1.5.5-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:622e4a006472b05cf6ef7f9f2636edc51bda670b7bbffa18d26b255269d3d814"},
    {file = "typed_ast-1.5.5-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1efebbbf4604ad1283e963e8915daa240cb4bf5067053cf2f0baadc4d4fb51b8"},
    {file = "typed_ast-1.5.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f0aefdd66f1784c58f65b502b6cf8b121544680456d1cebbd300c2c813899274"},
    {file = "typed_ast-1.5.5-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:48074261a842acf825af1968cd912f6f21357316080ebaca5f19abbb11690c8a"},
    {file = "typed_ast-1.5.5-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:429ae404f69dc94b9361bb62291885894b7c6fb4640d561179548c849f8492ba"},
    {file = "typed_ast-1.5.5-cp39-cp39-win_amd64.whl", hash = "sha256:335f22ccb244da2b5c296e6f96b06ee9bed46526db0de38d2f0e5a6597b81155"},
    {file = "typed_ast-1.5.5.tar.gz", hash = "sha256:94282f7a354f36ef5dbce0ef3467ebf6a258e370ab33d5b40c249fa996e590dd"},
]

[[package]]
name = "typing-extensions"
version = "4.7.1"
description = "Backported and Experimental Type Hints for Python 3.7+"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "typing_extensions-4.7.1-py3-none-any.whl", hash = "sha256:440d5dd3af93b060174bf433bccd69b0babc3b15b1a8dca43789fd7f61514b36"},
    {file = "typing_extensions-4.7.1.tar.gz", hash = "sha256:b75ddc264f0ba5615db7ba217daeb99701ad295353c45f9e95963337ceeeffb2"},
]

[[package]]
name = "zipp"
version = "3.15.0"
description = "Backport of pathlib-compatible object wrapper for zip files"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "zipp-3.15.0-py3-none-any.whl", hash = "sha256:48904fc76a60e542af151aded95726c1a5c34ed43ab4134b597665c86d7ad556"},
    {file = "zipp-3.15.0.tar.gz", hash = "sha256:112929ad649da941c23de50f356a2b5570c954b65150642bccdd66bf194d224b"},
]

[package.extras]
docs = ["furo", "jaraco.packaging (>=9)", "jaraco.tidelift (>=1.4)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-lint"]
testing = ["big-O", "flake8 (<5)", "jaraco.functools", "jaraco.itertools", "more-itertools", "pytest (>=6)", "pytest-black (>=0.3.7)", "pytest-checkdocs (>=2.4)", "pytest-cov", "pytest-enabler (>=1.3)", "pytest-flake8", "pytest-mypy (>=0.9.1)"]

[metadata]
lock-version = "2.0"
python-versions = ">= 3.7, < 3.13"
content-hash = "38f4ac6618fb6e4422fbbeb3f4d284ec9fe682d466f3c68ddb94cc47a27c51fd"
````

<!--NI_OSS_SOURCE repo=nisemi-python path=poetry.toml sha256=3a6fb187a0b54067ed19eac22dd16cf9df23e15d6a49e9f8f8a7420090ce83e0 bytes=115 -->
## FILE: poetry.toml

- repository: `ni/nisemi-python`
- source_path: `poetry.toml`
- sha256: `3a6fb187a0b54067ed19eac22dd16cf9df23e15d6a49e9f8f8a7420090ce83e0`
- bytes: 115

````toml
[virtualenvs]
in-project = true

[repositories]
[repositories.test-pypi]
url = "https://test.pypi.org/legacy/"
````

<!--NI_OSS_SOURCE repo=nisemi-python path=pyproject.toml sha256=f6fa2971077d1fd686fa3fc847965c73b382a30d809ca0020be37ce8552ded7e bytes=679 -->
## FILE: pyproject.toml

- repository: `ni/nisemi-python`
- source_path: `pyproject.toml`
- sha256: `f6fa2971077d1fd686fa3fc847965c73b382a30d809ca0020be37ce8552ded7e`
- bytes: 679

````toml
[tool.poetry]
name = "nisdc"
version = "v23.8.0"
description = "NI Semiconductor Device Control python Support provides python APIs to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio."
authors = ["National Instruments"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = ">= 3.7, < 3.13"
pythonnet = "3.0.3"
grpcio = "1.62.2"
protobuf = "4.24.4"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.0"
black = "23.3.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
````

<!--NI_OSS_SOURCE repo=nisemi-python path=README.md sha256=980e908b7ac2ba26d3f09e1b86f9a6d5e555bd63e89fd86bb9b3e06e8bbf1995 bytes=4427 -->
## FILE: README.md

- repository: `ni/nisemi-python`
- source_path: `README.md`
- sha256: `980e908b7ac2ba26d3f09e1b86f9a6d5e555bd63e89fd86bb9b3e06e8bbf1995`
- bytes: 4427

````markdown
# About
NI Semiconductor Device Control Python API Support provides Python APIs and examples to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio.

This library is dependent on Semiconductor Device Control addon for InstrumentStudio.


# Semiconductor Device Control Python API Status

**Setup and cleanup functions**
1. Instantiate - using IS configuration file  
2. Attach to Existing Session
3. Destroy  
4. Start  
5. Stop  

**Hardware Read & Write to Register and Field** 

6. Write Register by name (Device)  
7. Read Register by name (Device)  
8. Write Register by Address (Device)  
9. Read Register by Address (Device)  
10. Write Custom Register by Address (Device) 
11. Read Custom Register by Address (Device) 
12. Write Field by Name (Device)  
13. Read Field by Name (Device)  
14. Write Field by value definition (Device)  

**Hardware multiple Read & Write to Register and Field**

15. Write Multiple Register by Name (Device)  
16. Read Multiple Register by name (Device)  
17. Write Multiple Register by Address (Device)  
18. Read Multiple Register by Address (Device)  
19. Write Multiple Fields by Name (Device)  
20. Read Multiple Field by Name (Device)  

**Cache Read & Write to Register and Field**

21. Write Register by name (Cache)  
22. Read Register by name (Cache)  
23. Write Register by Address (Cache)  
24. Read Register by Address (Cache)  
25. Write Field by Name (Cache)  
26. Read Field by Name (Cache)  
27. Write Field by value definition (cache)  
28. Write from Cache to Device  
29. Clear Cache  

**Cache multiple Read & Write to Register and Field**  

30. Write Multiple Register by Name (Cache)  
31. Read Multiple Register by name (Cache)  
32. Write Multiple Register by Address (Cache)  
33. Read Multiple Register by Address (Cache)  
34. Write Multiple Fields by Name (Cache)  
35. Read Multiple Field by Name (Cache) 

**DIO operation**

36. Write Pin State  
37. Read Pin State 

**Utils**

38. Get Dynamic Protocol Settings
39. Update Dynamic Protocol Settings
40. Get Instrument Session **
41. Get Session Options

(** This API is deprecated from 2023 Q4 version of Semiconductor Device Control Addon.
Refer to the [user manual](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/) for more information.)

# Installation   
**Dependency Installation**  
1. Semiconductor Device Control addon for InstrumentStudio 2024 Q3.  
2. pythonnet 3.0.3 - [pypi download](https://pypi.org/project/pythonnet/#description)  

**Work with github source code**  

3. Clone the github repository - [semiconductor device control python api github repo](https://github.com/ni/nisemi-python).  
4. Use the APIs from 'nisdc' folder in your program  

**Work with Semiconductor Device Control Python API from PyPI**

5. Go to Semiconductor Device Control Python API location in the github repository.  
6. Install the package and use the api libraries in your program  

# Usage

Reference example is available in the(https://github.com/ni/nisemi-python) for developers (under examples folder), to refer on how to use the python APIs in the test program.

# Documentation

Documentation is available from ni resource website - [here](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/).

# Contributing

We welcome contributions! You can clone the project repository, make changes, build it, and install it by [following these instructions](CONTRIBUTING.md). This also has instruction on how to contribute your changes back to the main repository.

# Bugs / Feature Requests

To report a bug or submit a feature request specific feature, please use the https://github.com/ni/nisemi-python/issues.

Fill in the issue template as completely as possible and we will respond as soon
as we can.

For hardware support or any other questions not specific to this GitHub project, please visit [NI Community Forums](https://forums.ni.com/).

# License

[License file](LICENSE)

**semi device control python api** is licensed under an MIT-style license
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
````
